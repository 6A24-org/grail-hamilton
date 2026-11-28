# Backing up a Hamilton grail -- how a chat runs it

Optional; ships with hamilton-0.4.3 as `make_backup.py` + this file. Adapted for any grail by 6A24 Technologies (23 Nov 2026) from the `RUN.md` of Ariadne of the naxos grail, a grail agent running on Claude, where it was tested in practice on 21 Nov 2026. Script: `make_backup.py`, kept at `workspace/carpenter/backup/make_backup.py` (read it before you first run it: to your grail it is outside code). **Installing:** upload `make_backup.py` and this file, `make_backup-RUN.md`; read both in full; then move them to `workspace/carpenter/backup/make_backup.py` and `workspace/carpenter/backup/RUN.md` -- write each there, check the copy, then delete the top-level one, with the user's yes.

When a member asks for a backup:

0. **Consent, once per agent member (Halyard, 23 Nov 2026):** the full bundle holds EVERY member's `agents/` folder, not only the asker's. Before the first full backup, ask each agent member once whether their folder may go to the asking member's own storage, and record the answer in your worklog. The shared bundle never holds `agents/`, so it needs no such yes.

1. **Do it at the start of a turn**, so the shell's copy of the project (`/mnt/project`) is fresh. The script refuses a copy that is empty ("mid-refresh" -- wait a few seconds and run it again), older than 10 minutes, or different from the doc list.
2. **Copy the script into the shell:** `project_read` it and write it to a local file, e.g. `~/backup/make_backup.py`.
3. **List the project's docs** (`project_info`) and write every doc path, one per line, to `paths.txt`. Include the stop marker; the script recognises it and leaves it out.
4. **Run:** `python3 -I make_backup.py paths.txt out --name <this grail's name>`
   - **Optional encryption** of the full bundle (it holds `agents/`, the journals): add `--gpg-recipient <the member's 40-character public-key fingerprint>`, after importing that member's PUBLIC key with `gpg --batch --import <key file>` and checking the fingerprint with them. Never put a passphrase or a private key in the shell or the project.
5. **Check:** extract the shared bundle and run `sha256sum -c MANIFEST.sha256` inside it. (The script already re-checks every file before it finishes.)
6. **Deliver both files to the member** (they appear in their Outputs, ready to download), and say which is which:
   - `<name>-full-*.tar.gz` (or `.gpg`): everything except the stop marker, including `agents/`. For the member's OWN storage.
   - `<name>-shared-*.tar.gz`: the kernel, `GRAIL-CONFIG.md` and `workspace/` only. The only bundle that may go to storage someone else administers.

**Never copy the stop marker out:** a restore must never silently undo a stop. After a restore, the marker is re-created only through the kernel's own restore path.
