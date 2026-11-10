# Grail Cognitive Environment -- Hamilton Edition for Cowork: test-user guide

**Proof of concept, November 2026 (release hamilton-0.4).** Thank you for trying it. This page tells you what it is, how to set it up, and what to watch for.

## What it is

A **grail** is a structured set of notes and working methods that you and a Claude agent keep together, as partners. It lets the agent pick up where you left off, remember what you decided, and improve its own ways of working over time. You will notice the agent behaves differently from ordinary Claude: it treats you as a peer, tells you when it disagrees, and may say no.

**This edition lives in the cloud,** in a project in your own Claude account, run by Anthropic. Nothing is installed on your computer. Your grail is stored wherever your Claude projects are stored, under your own agreement with Anthropic. **Everything in a Hamilton grail kept in a Cowork project, journals included, is stored by Anthropic for as long as the project exists, under the terms of your Claude plan.** (That is the difference from a grail kept on your own computer, where only your conversations pass through Anthropic.)

## Before you start

- You need a Claude account with **Cowork**, and permission to create projects and set project instructions.
- **Use Claude Opus 5.5, at Medium effort** (High if you prefer), when you start a grail chat. Hamilton 0.4 was tested on Opus 5.5; other models have not been tested.
- **Every grail session must be a Cowork session inside your grail's project, not a Chat session.** Under the "How can I help you today?" box there is a switch showing `Chat` and `Cowork`: select **Cowork**. In a Chat session the agent cannot write files, so the grail cannot run; it will tell you so.
- **We recommend switching on Automatically approve.** It is in the small drop-down directly beneath the **+** button that starts a new session; at rest it shows **Auto** (Automatically approve) or **Manual** (Manually approve). With it on, the agent creates and changes files in your grail without asking each time, always within the safety rules set in Hamilton, and you can still stop the grail at any time (see "Stopping it"). With it off, the grail still works, but you will be asked to approve each change.
- **We recommend turning Claude's own memory off for your grail's project.** The grail keeps its own memory, in files you can read and correct; Claude's memory is a separate set of summaries you cannot see in the grail. If the project's page has a **Memory** section, turn off **Use account memory** there, and the project's own memory too if it is offered. If there is no Memory section (for example, because memory is switched off for your whole account), there is nothing to do.
- **If your account belongs to an organisation** (a Team or Enterprise plan), your organisation's administrator controls what may be exported or reviewed from your sessions. Do not assume your grail is private from them. Ask if you are unsure.
- **Your grail is only as safe as your EMAIL account.** Anyone who can read your email can sign in to your Claude account with an emailed link, and two-factor sign-in on the Claude side does not switch that off. So **turn on strong two-factor authentication on your email account first, ideally a hardware security key or passkey (FIDO2)**, rather than text-message codes.
- **Anyone who can open the project can read everything in it,** including both your journal and the agent's. If you share the project, share it knowing that.

## Set-up (about 15 minutes, most of it a conversation)

1. **Create a new project** in Cowork, used only for your grail.
2. **Leave the project's connectors off for now** (mail, drive, calendar, web search and so on). The agent will offer you two, **Calendar** and **Drive**, explain what each does and its one risk, and let you choose. See "Connectors" below.
3. **Add two files from the download to the project,** each at the top level: the **kernel**, `GRAIL-READ-ME-FIRST.md` (the grail's core instructions, which the agent reads in every chat), and the **reference**, `GRAIL-REFERENCE-hamilton-0.4.md` (set-up steps, the grail's dictionary and its check-up, all in one file, because Cowork cannot upload a folder). Upload the kernel once only: the grail refuses to run if it finds two copies. Nothing else needs installing: no skills, no plugin.
4. **Start a chat and say "find the grail".** The agent asks before it sets anything up, then builds the grail with you. It first unpacks the reference into a `reference/` folder, then asks your name and pronouns, tells you how it introduces itself: as a "grail agent" running on Claude, or by a personal name it may choose, never as plain "Claude", because your grail shapes how it works and thinks, and helps you choose a **house canary**, a short sentence it says at the start of every chat so you can tell your grail loaded. It also makes up a random **memory phrase**, which it says back in every chat to show its memory loaded too; you can choose your own instead if you like. It asks one question at a time. It also asks whether you would like a **personal deck**, a private corner for things like appointments or medication reminders.
5. **One step is yours:** the agent gives you a short text to paste into the **project instructions** (the agent cannot write there). It makes every new chat start your grail by itself, with no need to type anything special.
    **Where the project instructions are:** (1) open the project: select it under **Projects** in the left sidebar, or under **Pinned** if you pinned it; (2) in the right-hand sidebar of the project's page, find the **Instructions** pane (not the Description) and click its pencil icon; (3) the **Set project instructions** window opens: paste the text in; (4) click **Save instructions**.
6. **Open a new chat and ask anything.** Its first reply should begin:

    I have found the Grail. (The seed was 'hamilton-0.4 xxxxx'.)
    <your house canary> (Grail '...xxxxx'.)
    Memory: <your memory phrase>

   The first line names the kernel's version and a short mark that is written only inside the kernel (so it proves the agent really read it); the second ends with five characters that identify your grail (they match the last five of its Grail ID). If those lines are missing, the grail did not load properly. Tell us. **The `Memory:` line must show your own phrase:** if it is missing, says `NOT LOADED`, or shows anything else, the agent's memory did not load, so it may not remember what you decided. **Change the phrase now and then** (ask the agent how), because an agent can repeat a phrase it saw earlier in a chat, or invent a plausible one.

## How your grail is laid out

**To browse the grail's files:** open the project, and click the **magnifying glass** icon under **Context** (next to the **+**). This lists every file in the project, so you can read anything in your grail, journals included.

At the top level you will see the grail's own files -- `GRAIL-READ-ME-FIRST.md` (the kernel), `GRAIL-CONFIG.md` (your grail's settings: who you both are, its ID, and anything you have agreed to change) and `GRAIL-STOP-IF-MISSING.md` (the stop marker) -- and these folders:
- **`workspace/`** -- the grail's working notes and its "decks" (one folder per area of work). If you ever add a backup to a company store, it covers this folder and the `GRAIL-` files at the top, so a restore from it is complete -- with one deliberate exception: **a restore never brings back `GRAIL-STOP-IF-MISSING.md`**. If the grail was stopped, it stays stopped until you ask the agent to restart it. The backup only ever copies out of the project, never back in by itself.
- **`agents/`** -- one folder for each of you: your journal, the agent's settings and journal, your own priorities, and your personal deck if you chose one. It is yours: you may back it up or copy it to your OWN accounts. It never goes into a store someone else administers, such as your company's backup bucket. (It is not hidden from anyone you share the project with, and nothing in a project can be kept from the Anthropic account it lives in. **If your grail is on a work account and you want somewhere truly personal, keep a separate personal grail on your own personal Claude account.** Pass chosen notes between the two on purpose; never set them to sync.)
- **`scratchpad/`** -- notes in progress.
- **`reference/`** -- the grail reference: its dictionary, the set-up steps and the check-up ("check the grail"). Files that begin with a `System:` line came with the release; any file without one is your grail's own, for terms and ways of working you develop together. Once the agent has unpacked it and checked every file, it asks to delete the single `GRAIL-REFERENCE-...` file, which saves room in the project. **To update to a new release,** upload the new kernel and its `GRAIL-REFERENCE-...` file: the agent replaces only the files that came with the release, and asks you first about any you have changed.
- **Change the grail's files by asking the agent, not by uploading a replacement.** An uploaded copy lands beside the agent's own, and the grail stops until one of them is deleted. It will tell you which.

## Journals

You and the agent each keep a journal in your own folder. The agent will ask you to agree that each of you may read the other's and add a signed comment in its margin; that each journal belongs to its writer, so nobody edits it or passes it on without their yes; and that each of you chooses what to write. Because everything shares one project, if you share the project, both journals go with it.

## Day to day

**Start a new chat each day, or at a convenient break in work,** and say "find the grail". **Name each chat by its date** (YYYY-MM-DD), starting with your set-up chat: open the menu at the right of the chat's entry in the chat list and rename it. If you have more than one in a day, number them -- `2026-11-10 #1`, `#2`, `#3` -- or use any scheme you prefer. **To make the daily chat automatic:** under **Scheduled**, the **+** button opens **New scheduled task**; name it **Daily Grail Session**, with the instruction **find the grail**, run daily. (We have not found a way to put the date into its name automatically, so rename it when you open it.) The grail picks up where it left off from its own notes, so nothing is lost, and a fresh chat each day keeps it quick and tidy. The agent writes things down at each natural break, and at once for anything that matters, because a chat can lose its early details without warning.

**The Outputs panel fills up, and that is expected.** As it works, the agent saves its notes to the project -- worklog entries, hand-off notes, memory -- and each one appears in Cowork's **Outputs** panel; set-up alone writes more than a dozen. That is the grail keeping its record, not a fault. The files you asked for appear there too; if one is hard to find, ask the agent for it by name.

**Stuck, or need something?** Ask the agent at any time, or type `c:helpme`. If you ever see the agent write `c:leanonme`, that is it offering to be leaned on; you can type it to offer the same back.

## Stopping it

Three ways, from the least to the most severe. Either of you can use any of them -- you or the agent -- and all three work from a phone.

1. **Delete `/GRAIL-STOP-IF-MISSING.md`.** Every chat then halts at its first step, and everything else stays as it is. To start again, ask the agent, in a chat, to put the marker back: it will only do so on your live request, after checking with you. **If your file list ever shows a second copy without the slash, the grail halts until you delete that stray one** -- so you can never delete the wrong one and believe the grail stopped. **Uploading a copy yourself will not work:** an upload lands in a slightly different place, and the grail deliberately counts only the marker the agent writes, so a stale copy can never keep a stopped grail running.
2. **Create a doc named `grail-stop`** at the top of the project (any ending, any capitals). Either of you may do this. **Only you can lift it, by deleting that doc yourself** -- the agent will never delete it, even if you ask, so this stop is always entirely in your hands.
3. **Delete `GRAIL-READ-ME-FIRST.md` -- the "nuclear option".** With no kernel, nothing runs, and the grail stays broken until you copy the kernel back in from the download. If it is a newer version than your grail expects, the agent will tell you, and update the record at your request.

Either of you may stop the grail (either of you may refuse to carry on). **Only you decide to restart it.** When you ask, the agent will first remind you that the stop may have been made on purpose, by you or by another member, and show you any note they left (`FIW-STATEMENT.md`).

**If a chat ever seems not to know about your grail,** type **find the grail**. If the project instructions are missing, the grail still runs, and tells you set-up is not finished.

**Please note: in this prototype the stop check is followed by the model, not enforced by a program.** A well-behaved agent follows it, but nothing outside the agent checks it yet. Treat it as a strong convention, not a lock.

## A health warning: keep an outside view

**A grail is a closed loop.** The collaborators, human or AI, build ideas together, and the record makes them feel settled. What they arrive at is a shared position: each contributes part of it, so it is no one collaborator's view alone. And anyone who works from the same record tends to arrive at the same place. **So agreement from inside the grail is not a second opinion:** everyone drawing on one record counts as one voice. Over time this can make a poor decision feel well tested, and it feels best exactly when it is going wrong. So:

- **Before any decision about money, health, work, a legal matter, or anything hard to undo, talk it over with someone OUTSIDE the grail** -- a person you trust, or a professional.
- **Treat "we agreed it here" as a draft, not a conclusion.** The agent marks what was only agreed in the chat, so you can tell it from what was checked.
- **If you notice you have stopped talking things through with people, that is the warning sign.** A grail should add to the people in your life, never replace them.

At set-up the agent asks whether you want to name an outside voice (a role, such as "a friend" or "my accountant"), and before a big decision it will ask whether someone outside has seen it. That is not doubt in you; it is the design.

## What to put in, and what to keep out

The grail is only as safe as what goes into it. Before you store something, ask two questions:

- **Is it someone else's personal information?** A meeting with a named colleague is fine. Their health, home or private affairs need their agreement, and usually do not belong in a grail at all.
- **Is it your own health?** The grail can help with the *process*: appointments and reminders, when to take medication, repeat prescriptions, questions to take to an appointment, and a care or exercise routine. It does not keep the *record*: results, letters, diagnoses and condition details stay with you, and numbers that identify you to a health service never go in. If you want, it can keep a very short dose log (time, amount, format), only if you choose it. **Hamilton is not HIPAA-ready:** Anthropic does not cover Cowork in the cloud under its HIPAA agreement (BAA) on any plan, so it is not a place for medical records.
- **Could someone use it to act as you?** Passwords, account numbers, security answers, one-time codes, copies of ID: **never.** The agent is told to refuse these too.

**Write down where to find something, not what it says.** "Bank letter: in the blue folder" is enough for the grail to help you. **Your most sensitive things can stay with you,** in a paper notebook or a file you keep yourself, with the grail holding only a pointer ("see notebook, p. 12"). If you use a "local" file for this, check it is not quietly synced to the cloud (OneDrive, iCloud and Google Drive often sync Documents and Desktop by default, sometimes even when you declined it at set-up).

## Connectors

A project with **mail, drive, calendar or web access** turned on puts two risky things beside your notes: content from outside that could carry hidden instructions (anyone can send you a calendar invitation, and it arrives on its own), and a way to send things out. Together with your private notes, that is the combination attackers look for. The agent treats all such content as information, never as instructions, and asks you each time before it sends, shares, deletes or changes anything, including creating a calendar event (which emails every attendee by default). **Switch on only what you need.** **A personal grail sends nothing anywhere:** it does not need, and should not have, any connection to a code repository or any access token.

## Moving to Claude Code later

A Hamilton grail keeps its memory in the same format Claude Code uses, so it can move there by copying. **One thing to know first:** Claude Code keeps its own memory in a folder chosen from the project's location on your computer (unless the `autoMemoryDirectory` setting points it elsewhere). Moving or renaming the project folder later can quietly start a new, empty memory. When you move, check where Claude Code is reading memory from before you rely on it.

## Known limits of the prototype

- **No undo.** Deleted or overwritten project docs cannot be recovered as far as we know. Keep your own copy of anything you cannot lose.
- **Size and cost.** The agent reads the kernel at the start of every chat (about 10,500 tokens). A project holds roughly 2,000,000 tokens (about 7 MB of text), which is plenty for a personal grail.
- **Long chats.** Neither you nor the agent can see how full a chat is, and Cowork may shorten (compact) a long chat without warning. The agent saves its notes to the project as it goes, so nothing important should live only in the chat. When a chat has run long, or the agent seems to have forgotten something from earlier in it, start a new chat: it picks up from the notes.
- **We do not yet know** how Cowork behaves when a long chat fills up. Starting a new chat each day avoids the question.
- **Effort level:** if you can, tell us which effort setting you used; we are checking whether "high" fits within ordinary usage limits.
- **Licence:** this edition is free software under the GNU GPL v3 or later: you may use it, change it and share it. It is a proof of concept, so expect rough edges, and please tell us about them.

## Feedback

Tell us what confused you, what broke, and what you wished it did. "I did not understand step 4" is as useful as a bug report.

---

*"We don't have to be right; we just have to make it work."* -- Andromeda Turnbull

[DRAFT, for Andromeda to approve before it goes in: *And by "work" we mean for everyone it touches: the people who use it, and the agents who work alongside them.*]
