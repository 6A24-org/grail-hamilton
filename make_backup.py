#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Part of the Grail Hamilton Edition (6A24 Technologies); licence: GNU GPL v3 or later.
"""Hamilton grail backup -- build .tar.gz bundles of the grail's project docs.

Written by Ariadne (ariadne@grail:naxos) for her own grail, and given to Hamilton;
generalised by 6A24 Technologies (23 Nov 2026) for any grail: the bundle names come from
--name (default "grail"), and no key is assumed.

Source: /mnt/project, the read-only mirror of the project, where folders are
flattened into names ("/" -> "_"; a leading "/" -> leading "_"). Because "_"
can also appear inside real names, the mirror alone cannot be un-flattened
safely, so the script takes the authoritative list of project paths (from the
Projects tool's project_info) in a text file, one path per line, and maps each
path to its mirror name.

Two bundles (kernel section 3):
  <name>-full-<ts>.tar.gz   everything except the stop marker -- for a
                            member's OWN storage (agents/ is included)
  <name>-shared-<ts>.tar.gz only the kernel, GRAIL-CONFIG.md and workspace/ --
                            the only things that may go to a store someone
                            else administers
The stop marker (/GRAIL-STOP-IF-MISSING.md) is never copied out, so no restore
can silently undo a stop. Each bundle carries a MANIFEST.sha256 and a README.

Optional: --gpg-recipient FINGERPRINT (all 40 hex digits) encrypts the FULL bundle (the one holding
agents/) to a PUBLIC key already imported into the local keyring; the shared
bundle stays plain. No passphrase or private key ever touches this machine.

Usage: make_backup.py PATHS_FILE OUT_DIR [--name NAME] [--gpg-recipient FINGERPRINT]
"""
import hashlib, io, os, re, shutil, subprocess, sys, tarfile, tempfile, time
from datetime import datetime, timezone

MIRROR = os.environ.get("HAMILTON_MIRROR", "/mnt/project")  # override only for testing
MARKER = "GRAIL-STOP-IF-MISSING.md"
SHARED_ROOTS = ("GRAIL-READ-ME-FIRST.md", "GRAIL-CONFIG.md")


def flatten(path):
    return path.replace("/", "_")


def match_key(name):
    # The copy turns "/" into "_", and has been seen to turn dots inside names into "_" too
    # (hamilton-0.4.2 -> hamilton-0_4_2; Halyard, 23 Nov 2026). Compare with both folded,
    # and refuse if two names fold to the same key, rather than guess.
    return name.replace("/", "_").replace(".", "_")


def canonical(path):
    # Store top-level docs without their leading "/" inside the archive.
    return path.lstrip("/")


def is_marker(path):
    name = canonical(path).split("/")[-1].rsplit(".", 1)[0].lower()
    return canonical(path).count("/") == 0 and name == "grail-stop-if-missing" \
        or canonical(path) == "claude/" + MARKER


def is_shared(cpath):
    return cpath in SHARED_ROOTS or cpath.startswith("workspace/")


def build(name, items, ts, readme, out_dir):
    manifest = "".join(f"{hashlib.sha256(d).hexdigest()}  {p}\n" for p, d in items)
    out = os.path.join(out_dir, f"{name}-{ts}.tar.gz")
    with tarfile.open(out, "w:gz") as tar:
        for p, d in [("README.txt", readme.encode()), ("MANIFEST.sha256", manifest.encode())] + items:
            info = tarfile.TarInfo(f"{name}-{ts}/{p}")
            info.size, info.mtime, info.mode = len(d), int(time.time()), 0o644
            tar.addfile(info, io.BytesIO(d))
    # Verify: reopen, re-hash every member against the manifest.
    with tarfile.open(out, "r:gz") as tar:
        for p, d in items:
            got = tar.extractfile(f"{name}-{ts}/{p}").read()
            assert hashlib.sha256(got).digest() == hashlib.sha256(d).digest(), p
    return out, len(items)


def main():
    args = sys.argv[1:]
    recipient = None
    name = "grail"
    if "--name" in args:
        i = args.index("--name")
        if i + 1 >= len(args):
            sys.exit("--name needs a value after it")
        name = args[i + 1]; del args[i:i + 2]
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", name):
            sys.exit("--name: letters, digits, - and _ only")
    if "--gpg-recipient" in args:
        i = args.index("--gpg-recipient")
        if i + 1 >= len(args):
            sys.exit("--gpg-recipient needs a value after it")
        recipient = args[i + 1]; del args[i:i + 2]
        # Full fingerprint only: with --trust-model always, a short id would
        # trust whatever key happens to match it. (Cairn, 2026-11-21.)
        recipient = recipient.replace(" ", "").upper()
        if not re.fullmatch(r"[0-9A-F]{40}", recipient):
            sys.exit("--gpg-recipient needs the full 40-character fingerprint")
    if len(args) != 2:
        sys.exit(__doc__)
    paths_file, out_dir = args
    os.makedirs(out_dir, exist_ok=True)
    paths = [l.strip() for l in open(paths_file) if l.strip()]

    # No copy at all: this session's shell has no view of the project.
    if not os.path.isdir(MIRROR):
        sys.exit("%s not found: this shell has no copy of the project, so no backup can be made here" % MIRROR)
    # An empty copy means it is mid-refresh (seen 2026-11-21 06:08 UTC).
    listing = [f for f in os.listdir(MIRROR) if not f.startswith(".")]
    if not listing:
        sys.exit("/mnt/project is empty: mid-refresh, wait a few seconds and retry")
    # Freshness: the mirror is refreshed from the project, but can lag; refuse if it looks stale.
    newest = max(os.path.getmtime(os.path.join(MIRROR, f)) for f in listing)
    if time.time() - newest > 600:
        sys.exit("mirror older than 10 minutes; re-run at the start of a turn")

    by_key = {}
    for f in listing:
        by_key.setdefault(match_key(f), []).append(f)
    clashes = [v for v in by_key.values() if len(v) > 1]
    if clashes:
        sys.exit("mirror names too alike to tell apart: " + "; ".join(", ".join(v) for v in clashes))
    path_keys = {}
    for p in paths:
        path_keys.setdefault(match_key(p), []).append(p)
    pclash = [v for v in path_keys.values() if len(v) > 1]
    if pclash:
        sys.exit("doc paths too alike to tell apart: " + "; ".join(", ".join(v) for v in pclash))

    items, skipped, missing, used = [], [], [], set()
    for p in paths:
        hit = by_key.get(match_key(p))
        if hit:
            used.add(hit[0])
        if is_marker(p):
            skipped.append(p); continue
        if not hit or not os.path.isfile(os.path.join(MIRROR, hit[0])):
            missing.append(p); continue
        items.append((canonical(p), open(os.path.join(MIRROR, hit[0]), "rb").read()))
    if missing:
        sys.exit("not in mirror (re-list the project and retry): " + ", ".join(missing))
    extra = [f for f in listing if f not in used]
    if extra:
        sys.exit("mirror has docs not in the path list (re-list the project): " + ", ".join(extra))

    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y-%m-%dT%H%MZ")
    readme = (
        f"{name} backup, {now.strftime('%Y-%m-%d %H:%M')} UTC\n\n"
        "Paths are the project's doc paths. Top-level docs are stored without\n"
        "their leading '/': on restore, GRAIL-CONFIG.md goes back as\n"
        "/GRAIL-CONFIG.md (written by an agent), the kernel as uploaded.\n"
        "The stop marker is deliberately absent; after a restore it is\n"
        "re-created only through the kernel's section 2 restore path.\n"
        "Check integrity with: sha256sum -c MANIFEST.sha256\n"
    )
    shared = [(p, d) for p, d in items if is_shared(p)]
    # Build in a private temporary directory and move only finished files into
    # OUT_DIR, so a failed encryption never leaves a plaintext full bundle
    # behind. (Cairn, 2026-11-21.)
    tmp = tempfile.mkdtemp(prefix=name + "-backup-")
    try:
        results = [build(name + "-full", items, ts, readme, tmp),
                   build(name + "-shared", shared, ts, readme, tmp)]
        finals = []
        for out, n in results:
            final = out
            if recipient and os.path.basename(out).startswith(name + "-full-"):
                r = subprocess.run(["gpg", "--batch", "--yes", "--trust-model", "always",
                                    "--encrypt", "--recipient", recipient,
                                    "--output", out + ".gpg", out])
                if r.returncode != 0:
                    sys.exit("gpg failed; nothing written to " + out_dir)
                final = out + ".gpg"
            finals.append((final, n))
        for final, n in finals:
            dest = os.path.join(out_dir, os.path.basename(final))
            shutil.move(final, dest)
            print(f"{dest}  ({n} docs, {os.path.getsize(dest)} bytes)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("excluded (stop marker):", ", ".join(skipped) or "none found")


if __name__ == "__main__":
    main()
