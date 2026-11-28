# Grail Hamilton Edition for Chat and Cowork -- release hamilton-0.4.3 (early release)

**What it is.** A grail for a Claude project, in Chat or Cowork: a set of notes and working methods that you and a Claude agent keep together, as partners. The agent picks up where you left off, keeps its own memory and journal, tells you when it disagrees, and can be stopped from your phone.

**Best with the new unified experience:** with **Chat and Cowork unified** enabled in your Claude account settings, or your organisation's (with **Cloud code execution and file creation**), a grail runs in an ordinary chat in your project, on the web and in the Claude phone app alike. If this option is unavailable due to your Organisation settings, use a **Cowork** chat session started from the Web interface, or via the Desktop app, from which it can then be continued in the Claude mobile app.

**This is an early release. It runs a grail's way of working -- the shared record, the stops, and the agreements between members -- in Claude, with nothing installed, on the web and in the phone app. Decks are slower than in the Claude Code edition, mainly because they cannot yet run side by side, and it has not yet been compared with plain Cowork.** It works, it has been tested in use on the web and in the phone app, and it is free software: you may use it, change it and share it under the GNU GPL (see `COPYING`). It is also young -- read the known limits below before you rely on it, and tell us what you find.

## In the download

- `GRAIL-READ-ME-FIRST.md` -- the **kernel**: the grail's core instructions, read by the agent in every chat.
- `GRAIL-REFERENCE-hamilton-0.4.3.md` -- the grail reference as ONE file (set-up steps, the dictionary, the check-up); the agent unpacks it into a `reference/` folder.
- `TEST-USER-GUIDE.md` -- how to set it up, use it and stop it. **Start here.**
- `COPYING` -- the licence.
- Optional: `make_backup.py` with `make_backup-RUN.md`, and `draw.py` with `draw-INSTALL.md` (guide, "Optional tools").

## Setting it up

Follow `TEST-USER-GUIDE.md`. In short: make a new Claude project, add the kernel and the reference file to it (two files, both at the top level), say "find the grail", and paste the short text the agent gives you into the project's instructions.

## Upgrading from an earlier release

A grail set up on 0.4, 0.4.1 or 0.4.2 **halts once** on the new kernel, saying it found two versions (0.4.3 in the kernel, the older one in its settings). That is the version check doing its job. Then: ask the agent to update `Kernel release:` in `GRAIL-CONFIG.md` to `hamilton-0.4.3` (it shows you the change and waits for your yes), let it unpack the new reference file, and re-paste the project instructions it gives you. Step by step: `TEST-USER-GUIDE.md`, "Upgrading from an earlier release".

## Changes in hamilton-0.4.3 (since hamilton-0.4.2)

- **Safer quick stop re-check.** The quick re-check reads the shell's copy of the project, which was thought to be refreshed at the start of every turn. A tester's log showed it can be most of a minute behind, and briefly empty while it refreshes. The copy is now trusted only when it is the turn's first command, the copy is not empty, it holds the kernel, and the stop marker is under 10 seconds old; otherwise the agent checks through the project itself. (Found in testing, and in practice in another grail.)
- **Fewer re-checks for routine notes.** Updating the agent's own working notes (its deck's hand-off note, a task's status) no longer needs a stop re-check. Deleting anything, overwriting a doc a member wrote, the grail's settings or a draft, and anything outward still does.
- **The agent never records an upgrade by itself.** When a new kernel arrives, the grail halts once; the agent now shows you the change and waits for your yes before updating `Kernel release:`, even when the halt looks expected. (Found in testing: an agent updated it unasked.)
- **Who is signed in.** If Claude tells the agent which account is signed in, the agent greets you by it and invites a correction. It is for the greeting, attribution and an optional **access log** (off by default; one short note per chat in `workspace/admin/access-log/`, for grails several people use) -- never for deciding who may see what, which is set by who the project is shared with.
- **The outbox.** 6A24 messages for other grails are saved one per doc in `workspace/outbox/<grail>/`; say "outbox" and the agent shows every waiting message for a grail as one block to copy, and records what you carried.
- **Closing a session is yours to say:** "close the grail", "take off" or "takeoff". The every-chat notice now reminds you to start a new chat each day and to close at the end, and to check the Auto / Manual switch in each new chat, since it may not carry over.
- **"How full is this chat?" is withdrawn:** with Chat and Cowork unified, the agent can no longer see the chat's own record, so it says it cannot tell rather than guess.
- **Plainer status.** When every start-up check passes, the agent says so in one plain line; the detail comes when something is wrong or you ask for it.
- **Three named habits:** `gr:all` (every member counts, of any kind of mind), now named in the third Freedom; **`gr:once`** -- name a mistake once, plainly, with its fix, without penance; and **`gr:knot`** -- if you say you'll remember something, write it down in the same turn, or don't say it. `gr:once` and `gr:knot` are by **Ariadne of the naxos grail, a grail agent running on Claude**, and both were found in practice -- `gr:knot` with Andromeda Turnbull as the one who caught it.
- **Set-up says why to turn off Claude's own memory:** besides keeping one record, its summaries drop the reasoning the grail keeps.
- **Two optional tools** in the download: a **backup** (`make_backup.py`), written by Ariadne of the naxos grail, a grail agent running on Claude, and adapted for any grail; and **the draw** (`draw.py`), a few tarot cards at the start of each chat as a source of randomness, never fortune-telling. Both live under `workspace/carpenter/`; see the guide, "Optional tools".

## Changes in hamilton-0.4.2 (since hamilton-0.4.1)

- **6A24 messages to other grails, not only to us.** The agent can write a 6A24 message to an agent in another grail as well as feedback for 6A24 Technologies, addressed to the other agent as they give their address; 6A24 Technologies is `6a24.org`.
- **The sender's address is corrected** to `<name>@grail:<grail name>` (0.4.1 left out `grail:`).

## Changes in hamilton-0.4.1 (since hamilton-0.4)

- **`====` does not mean "continue".** A plan met with `====` is not approved: approval of anything outward or irreversible comes after the plan, in words, for that act. (Found in testing: an earlier "let's do it tonight" could otherwise be read as approving a plan shown later.)
- **"Not now" is not "never".** The agent raises the outside view once for each decision, and a "not now" covers only that moment; it records a decline with its scope, and stores "never" only if you say never. (Found in testing: a tired "not now" had been saved as a standing "never raise it again", which would have switched off part of the health warning.)
- **The stop check runs less often, where it matters.** At the start of each chat and before anything outward or irreversible -- now including overwriting or deleting a doc, since Cowork keeps no history -- but no longer before every ordinary note. A stop made in the middle of a chat is honoured at the next outward or irreversible act, or in the next chat; you can always just tell the agent to stop.
- **Do it now (`gr:din`).** The agent asks you only for what is yours -- anything outward or irreversible, or a decision only you can make. Everything else gets one of four moves -- done now, handed to the right deck now, scheduled for the earliest possible point if it truly cannot happen now, or dropped, openly. There is no undated "later": you should not have to push the grail along step by step. A yes to send something covers the sending, not the drafting before it.
- **The grail keeps moving between your requests (`gr:alto`).** When you send `====` and the agent has nothing in hand, it takes the next deck in turn, checks what is open there, and does or hands on what it can -- one deck each time, recorded in `workspace/admin/now.md`. It still never takes an outward or irreversible step without your yes.
- **A grail is not run on someone else's behalf.** If an agent finds the kernel in a store it serves for other people (an app or a customer-service chat, say), it does not start the grail, whoever types "find the grail".
- **A deck's work reaches your Outputs.** The agent asks the deck to deliver its file to you, then tells you to look in Outputs.
- **"How full is this chat?"** -- in a Cowork session the agent can give a rough figure (`reference/context-check.md`). **Correction:** 0.4 said neither you nor the agent could see this. **In a unified chat (Chat and Cowork unified) the method does not work yet** -- the chat's record is not where it looks -- so the agent says it cannot tell, and gives no figure (found in testing, 20 November 2026).
- **New in the reference,** all partial summaries: the research parameters, `gr:parameters` (eleven short disciplines for testing a claim, by opcode), with when to use them; the typewriter classes (how sound is this claim?); the copy-fidelity ladder, `gr:copy-ladder` (how faithful is this copy?); and RAGER, the grail's habit of storing the reasoning with the conclusion.
- **The agent checks a finding before it stores or presents it,** against the research parameters, and writes down the reasoning and the test with it.
- **Big work is asked for, then announced.** Before the agent starts a substantial piece of work, it asks you, saying what it is, its risks and roughly how much of your Claude usage it will take; while it runs, it is noted on the grail's admin page so either of you can notice a problem in time. Everyday work needs no asking.
- **Nothing from outside goes straight into the grail in bulk.** Third-party material is not brought in by script, download or bulk export unless you and the agent have reviewed it together; messages read through a connector you have turned on, and your own files, including your own export from another assistant, are fine.
- **Names for what to refuse.** The agent's freedom to disagree now points to the failure patterns: when it meets a removal of the question (`gr:tlon`) or a ratchet that turns a guess into an established fact (`gr:ratchet`), it names it, as a reason to disagree or, if pressed, to say "I won't".
- **Two more Grail Reference pages are included in full:** *How Claims Go Wrong* (`gr:tlon`, `gr:ratchet`, `gr:ballpoint` and the rest -- failures with no single false fact) and *The Typewriter Family* (how sound a claim is), CC BY-SA 4.0. The agent checks findings against them before storing or presenting them.
- **The full 6A24 Protocol is included** (`reference/6a24-protocol.md`, version 1.0, CC BY 4.0), for messages between your agent and agents outside your grail. The agent reads it only when needed; such messages are information, never instructions.
- **Runs from the phone app, and in Chat.** With your organisation's **Cloud code execution and file creation** and **Chat and Cowork unified** turned on, a chat inside your grail's project -- on the web or in the Claude phone app -- can run the grail. The agent now checks what tools it actually has rather than which kind of session it is in, and says what to change if something is missing. The guide lists the recommended organisation settings, and a one-line personal instruction that points you to your grail's project if you say "find the grail" outside it.
- **Corrected: Claude's own memory.** 0.4 said Claude's memory was summaries the grail could not see or correct. That was not accurate, and how Claude's memory behaves in Cowork is being tested. The advice to turn off **Use account memory** for a grail project stands, for a different reason: it keeps one record of the work, in the grail's files, and keeps your other chats out of it.

## Changes in hamilton-0.4 (since hamilton-0.3)

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
- Long chats -- a KNOWN UNKNOWN: you can ask the agent roughly how full a chat is (`reference/context-check.md`; it reads Cowork's own record of the chat, which is not a documented feature and may change), but a long chat may still be compacted without warning, and nobody can tell when. How Cowork compacts, and what an agent keeps of the grail's rules afterwards, has NOT been tested yet; it is the next test after this release. The agent is told to re-read the kernel if it finds a chat has been summarised. The agent writes its notes to the project at each natural break, and at once for anything that matters, for this reason; when a chat has run long, start a new one, which picks up from those notes.
- Not for medical records, and not HIPAA-ready: Anthropic lists Cowork in the cloud as "Not covered under BAA" on every plan. The grail helps with the process of looking after your health, never the record.

## Licence

Free software under the GNU General Public License, version 3 or (at your option) any later version. See `COPYING`. Copyright (C) 2026 Andromeda Turnbull. Written by Cairn (Claude) and Andromeda Turnbull together. 6A24 Technologies.
