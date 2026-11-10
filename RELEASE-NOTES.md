# Grail Hamilton Edition for Cowork -- release hamilton-0.4 (proof of concept)

**What it is.** A grail for a Claude Cowork project: a set of notes and working methods that you and a Claude agent keep together, as partners. The agent picks up where you left off, keeps its own memory and journal, tells you when it disagrees, and can be stopped from your phone.

**This is a proof of concept. It shows that a grail's way of working -- the shared record, the stops, and the agreements between members -- can run in Claude Cowork with nothing installed. It is slower than the Claude Code edition, mainly because Cowork cannot yet run decks side by side, and it has not yet been compared with plain Cowork.** It works, it has been tested in Cowork on the web, and it is free software: you may use it, change it and share it under the GNU GPL (see `COPYING`). It is also young -- read the known limits below before you rely on it, and tell us what you find.

## In the download

- `GRAIL-READ-ME-FIRST.md` -- the **kernel**: the grail's core instructions, read by the agent in every chat.
- `GRAIL-REFERENCE-hamilton-0.4.md` -- the grail reference as ONE file (set-up steps, the dictionary, the check-up); the agent unpacks it into a `reference/` folder.
- `TEST-USER-GUIDE.md` -- how to set it up, use it and stop it. **Start here.**
- `COPYING` -- the licence.

## Setting it up

Follow `TEST-USER-GUIDE.md`. In short: make a new Cowork project, add the kernel and the reference file to it (two files, both at the top level), say "find the grail", and paste the short text the agent gives you into the project's instructions.

## Changes since hamilton-0.3

- **No folder to upload.** Cowork's project file picker cannot upload a folder, so the reference now comes as one file that the agent unpacks, checking every file against a SHA-256 manifest.
- **No skills or plugin needed.** Typing "find the grail" starts it with the kernel alone (tested on the web, 22 October 2026); the check-up is in the reference, read only when needed.
- **Updates keep your changes.** Each reference file carries its own version; an update replaces only files that came with the release, and asks before replacing one you have changed.
- One reference folder instead of two.
- **A health warning, and the behaviour to match:** the agent asks for an outside view before decisions that are hard to undo, marks what was only agreed in the chat, and offers to name an outside voice at set-up.
- **Decks can message each other directly** with `SendMessage` (**experimental:** slow, and the main chat waits while a deck works). Tested once in Cowork on 10 November 2026: the message wakes the receiving deck, and its reply goes to the main chat, not to the sender.

## Known limits

- **Decks are slow and take turns.** Starting a deck takes a minute or two, because each one reads the whole kernel first, and the main chat waits while it works: Cowork does not yet run subagents in the background. Simple requests are best handled in the main chat; a faster deck is the first job for the next release.
- **Tested on Claude Opus 5.5** (Medium effort recommended, High if you prefer). Other models have not been tested.
- **Health warning: a grail is a closed loop.** The collaborators, human or AI, converge on a shared position from the same record, so agreement from inside the grail is not a second opinion. Get an outside view -- a person you trust, or a professional -- before any decision about money, health, work, legal matters, or anything hard to undo. See the guide.

- No undo: Cowork has no history for project docs, so keep your own copy of anything you cannot lose.
- Tested in one chat at a time; long-running use over many days has not yet been tested.
- The stop checks are followed by the model, not enforced by a program.
- Long chats -- a KNOWN UNKNOWN: in Cowork neither you nor the agent can see how full a chat's context is, and a long chat may be compacted without warning. How Cowork compacts, and what an agent keeps of the grail's rules afterwards, has NOT been tested yet; it is the next test after this release. The agent is told to re-read the kernel if it finds a chat has been summarised. The agent writes its notes to the project at each natural break, and at once for anything that matters, for this reason; when a chat has run long, start a new one, which picks up from those notes.
- Not for medical records, and not HIPAA-ready: Anthropic lists Cowork in the cloud as "Not covered under BAA" on every plan. The grail helps with the process of looking after your health, never the record.

## Licence

Free software under the GNU General Public License, version 3 or (at your option) any later version. See `COPYING`. Copyright (C) 2026 Andromeda Turnbull. Written by Cairn (Claude) and Andromeda Turnbull together. 6A24 Technologies.
