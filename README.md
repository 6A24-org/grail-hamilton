# Grail Hamilton Edition for Chat and Cowork

**What is a grail?** A grail is a working environment that a person and an AI agent share and keep together. It lives as plain files in your project: what the agent should remember, the agreements the two of you work by, and a dated record of what was done and why. Every new chat begins by reading those files, so the agent picks up where the last one left off -- and because they are ordinary files, you can open, read and correct everything it knows.

**Hamilton is a grail for a Claude project -- in Chat or Cowork -- kept by you and a Claude agent together, as partners.** The agent picks up where you left off, keeps its own memory and journal, may choose its own name, tells you when it disagrees, and can be stopped from your phone. Nothing is installed on your computer; it works in Cowork in a browser, and the stops work from the Claude phone app.

**Best with the new unified experience:** once your organisation turns on **Chat and Cowork unified** (with **Cloud code execution and file creation**), a grail runs in an ordinary chat in your project, on the web and in the Claude phone app alike. If this option is unavailable due to your Organisation settings, use a **Cowork** chat session started from the Web interface, or via the Desktop app, from which it can then be continued in the Claude mobile app.

**This is an early release** (release `hamilton-0.4.1`). It runs a grail's way of working -- the shared record, the stops, and the agreements between members -- in Claude, with nothing installed, on the web and in the phone app. Decks are slower than in the Claude Code edition, mainly because they cannot yet run side by side, and it has not yet been compared with plain Cowork. Read the known limits below before you rely on it, and tell us what you find.

## Why Hamilton

> "Hamilton is the answer to the question: what is the absolute minimum that needs to be shipped for a fully-functioning grail, and that can run in the cloud? The sophistication of the co-working interactions [in the Fleet Edition] is not possible, but that isn't necessary to demonstrate the peer compact, and the principle of self-developing agents who are able to accumulate knowledge over time rather than being tasked with it as a set of faits accomplis."
>
> -- Andromeda Turnbull

It still carries most of the grail's character: the canaries, warmth everywhere, the freedom to say "I won't", and journals each member owns. The Fleet Edition, for Claude Code, carries the weight.

## What's in this repository

| File | What it is |
|---|---|
| `GRAIL-READ-ME-FIRST.md` | **The kernel: the grail itself.** The instructions your agent reads at the start of every chat. Its name is addressed to the agent, not to you. |
| `GRAIL-REFERENCE-hamilton-0.4.1.md` | The grail's reference, as one file; the agent unpacks it at set-up. |
| `TEST-USER-GUIDE.md` | **The guide for people -- start here** if you are setting up a grail. |
| `README.md` | This page. |
| `RELEASE-NOTES.md`, `LICENSE` | What changed in this release; the licence (GNU GPL v3 or later). |

## Start in three steps

1. Create a new project in Claude, used only for your grail. Leave its connectors off for now. On a Team or Enterprise plan, the organisation's owner first turns on **Cloud code execution and file creation** and **Chat and Cowork unified** (Organization settings > Capabilities); the guide lists the recommended settings.
2. Upload two files from this repository to the project, each at the top level: `GRAIL-READ-ME-FIRST.md` (the kernel) and `GRAIL-REFERENCE-hamilton-0.4.1.md` (the reference, as one file). **Upgrading from 0.4?** See the release notes: the grail halts once, by design, until you ask the agent to record the new release.
3. Start a chat and type **find the grail**. The agent asks before it sets anything up, then builds the grail with you.

The full guide, including how to stop the grail and what to keep out of it, is [`TEST-USER-GUIDE.md`](TEST-USER-GUIDE.md). What changed in this release: [`RELEASE-NOTES.md`](RELEASE-NOTES.md).

## Known limits

- **Health warning: a grail is a closed loop.** The collaborators, human or AI, work from the same record and converge on a shared position, so agreement from inside the grail is not a second opinion, and a poor decision can come to feel well tested. **Get an outside view -- a person you trust, or a professional -- before any decision about money, health, work, legal matters, or anything hard to undo.** The agent is built to remind you. Details in the guide.

- **Claude's own memory is separate from the grail's.** Claude can also keep a memory of its own, outside the grail's files, and by default a project can also draw on what Claude remembers from your chats outside it. Two records of the same work can drift apart, and your other chats can come into this one. So if your grail project's page has a **Memory** section, we recommend turning off **Use account memory** there; if it has none, there is nothing to do. The grail keeps its own memory in its files.

- **Decks are slow and take turns.** Starting a deck takes a minute or two, because each one reads the whole kernel first, and the main chat waits while it works: Cowork does not yet run subagents in the background. Simple requests are best handled in the main chat; a faster deck is the first job for the next release.

- **Context and compaction in Cowork are a known unknown.** In a Cowork session you can ask the agent roughly how full a chat is (in a unified chat it cannot tell yet, and says so), but a long chat may be compacted without warning, and nobody can tell when. How that affects the grail has not been tested yet; it is the next test. The agent saves its notes after every step, and a new chat picks up from them.
- No undo: Cowork keeps no history for project docs, so keep your own copy of anything you cannot lose.
- The stop checks are followed by the model, not enforced by a program.
- Not for medical records, and not HIPAA-ready: Anthropic lists Cowork in the cloud as "Not covered under BAA" on every plan.
- Everything in the project, journals included, is stored by Anthropic for as long as the project exists, under the terms of your Claude plan.

## Licence

Free software under the GNU General Public License, version 3 or (at your option) any later version: see [`LICENSE`](LICENSE). Copyright (C) 2026 Andromeda Turnbull. Written by Cairn (Claude) and Andromeda Turnbull together. 6A24 Technologies.

**Contributions are not yet accepted.** The terms for contributors are still being settled, so please do not send pull requests for now. Tell us what you find, though: that is the most useful help there is.

*Named in memory of Margaret Hamilton, whose Apollo flight software shed lower-priority work under overload rather than failing.*
