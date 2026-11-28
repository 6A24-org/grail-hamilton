#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# Part of the Grail Hamilton Edition (6A24 Technologies); licence: GNU GPL v3 or later.
"""draw.py (Hamilton) -- draw tarot cards as prompts for generative thinking.

A randomiser that breaks a fixed frame: you are thinking about something in a particular
shape, and a draw supplies material that did not come from that shape; the useful part is
the collision. Tarot is used here as any deliberate constraint on thought would be. No
claim about prediction is made or needed, so the output carries none.

Single file, for a Hamilton grail: the deck is embedded below, so the script needs nothing
else and can live in the project. It is the Fleet edition's draw (centre/scripts/draw.py in
the grail it came from), cards only, with the same selection method -- so a SEED gives the
same cards in both editions, and a draw can be shared across grails by its seed.

  python3 -I draw.py                 three cards, reversals on, random seed
  python3 -I draw.py -n 5            five cards
  python3 -I draw.py --spread sao    situation / action / outcome
  python3 -I draw.py --seed 1a2b3c4d replay a draw someone shared
  python3 -I draw.py --no-reversals  upright only
"""
import argparse, random, secrets, sys

DECK_TEXT = """# tarot.txt -- the 78-card deck, as data, for centre/scripts/draw.py
#
# Format:  <card name> -- <comma-separated thematic keywords>
# Sections are `# <suit>` headers. Blank lines and `#` comments are ignored.
# Within `# major` the cards are in traditional order, so a card's position in
# that section IS its number (The Fool = 0, The World = 21). Nothing else in
# this file encodes the number, so there is no second master to disagree.
#
# THE KEYWORDS ARE THINKING PROMPTS, NOT MEANINGS AND NOT PREDICTIONS.
# They are the ordinary thematic associations of the Rider-Waite-Smith
# tradition, written as short generative handles. They are deliberately
# associations rather than definitions: tarot traditions differ, and a draw
# here is a randomiser that breaks a fixed frame, so a keyword's job is to
# collide usefully with whatever you are already thinking about.
#
# EDIT THIS FILE FREELY. It is the tool's vocabulary, not its logic, and it is
# meant to be tuned to the reader's own practice. `check-draw.py` verifies the
# deck's STRUCTURE (78 cards, 22 major, 4 suits of 14, no duplicate names) and
# never its wording, precisely so the wording stays yours.

# major
The Fool -- beginning, the leap, innocence, the open road
The Magician -- will, focus, craft, channelling
The High Priestess -- inner knowing, the threshold, the unsaid
The Empress -- abundance, nurture, growth, the senses
The Emperor -- structure, authority, boundary, order
The Hierophant -- tradition, teaching, institution, received doctrine
The Lovers -- union, choice, alignment of values
The Chariot -- drive, direction, opposites harnessed
Strength -- patience, gentle mastery, quiet courage
The Hermit -- withdrawal, study, the lamp, solitude
Wheel of Fortune -- turning, cycle, luck, a change of state
Justice -- balance, consequence, clear sight, fairness
The Hanged Man -- suspension, the view reversed, a willing pause
Death -- ending, clearance, transformation
Temperance -- blending, moderation, measured mixing
The Devil -- the bind, compulsion, the chain you can see
The Tower -- sudden collapse, shock, a flaw exposed
The Star -- hope, replenishment, quiet guidance
The Moon -- ambiguity, dream, the misread signal
The Sun -- clarity, vitality, plain daylight
Judgement -- reckoning, the call, gathering up
The World -- completion, wholeness, the circuit closed

# wands
Ace of Wands -- spark, impulse, raw initiative
Two of Wands -- planning, surveying the options
Three of Wands -- expansion, looking outward, progress
Four of Wands -- arrival, celebration, a stable base
Five of Wands -- friction, scrappy competition
Six of Wands -- recognition, visible success
Seven of Wands -- defending a position, holding ground
Eight of Wands -- rapid movement, momentum, dispatch
Nine of Wands -- weary vigilance, one more push
Ten of Wands -- overload, carrying too much
Page of Wands -- curiosity, first enthusiasm
Knight of Wands -- headlong action, haste
Queen of Wands -- warm confidence, magnetism
King of Wands -- vision, bold leadership

# cups
Ace of Cups -- an opening of feeling, a new well
Two of Cups -- mutual regard, a pact between two
Three of Cups -- shared joy, good company
Four of Cups -- apathy, the offered cup unseen
Five of Cups -- grief, attention fixed on what spilled
Six of Cups -- memory, nostalgia, an old kindness
Seven of Cups -- many options, the illusion of choice
Eight of Cups -- walking away from what is merely enough
Nine of Cups -- contentment, the wish satisfied
Ten of Cups -- belonging, the full circle
Page of Cups -- tender first feeling, an invitation
Knight of Cups -- pursuit, following the feeling
Queen of Cups -- empathy, holding another's feeling
King of Cups -- steadiness, mastery of feeling

# swords
Ace of Swords -- a clear idea, incisive truth
Two of Swords -- stalemate, the deliberate blindfold
Three of Swords -- sharp hurt, the plain painful fact
Four of Swords -- rest, deliberate quiet, recovery
Five of Swords -- the hollow win, the cost of conflict
Six of Swords -- passage, moving to calmer water
Seven of Swords -- stealth, taking what was not given
Eight of Swords -- self-made constraint, the felt trap
Nine of Swords -- anxiety, the sleepless hour
Ten of Swords -- the worst named, a thought ended
Page of Swords -- sharp curiosity, watching, probing
Knight of Swords -- the charging argument, blunt intellect
Queen of Swords -- clear judgement, unsentimental sight
King of Swords -- the authority of reason

# pentacles
Ace of Pentacles -- a material beginning, a seed of value
Two of Pentacles -- juggling, balancing resources
Three of Pentacles -- craft, collaboration on a build
Four of Pentacles -- holding on, guarding what is held
Five of Pentacles -- lack, exclusion, the cold outside
Six of Pentacles -- giving and receiving, exchange
Seven of Pentacles -- waiting on growth, patient assessment
Eight of Pentacles -- diligence, apprenticeship, repetition
Nine of Pentacles -- self-sufficiency, earned comfort
Ten of Pentacles -- legacy, inheritance, the long term
Page of Pentacles -- first study, practical curiosity
Knight of Pentacles -- steady plodding, reliable method
Queen of Pentacles -- practical care, resourcefulness
King of Pentacles -- mastery of the material, provision
"""

SPREADS = {"sao": ("situation", "action", "outcome")}
SUITS = ("major", "wands", "cups", "swords", "pentacles")
ROMAN = ("0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI",
         "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI")


def load_deck():
    deck, suit = [], None
    for line in DECK_TEXT.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            head = line.lstrip("#").strip().lower()
            if head in SUITS:
                suit = head
            continue
        name, _, kw = line.partition(" -- ")
        card = {"name": name.strip(), "suit": suit,
                "keywords": [k.strip() for k in kw.split(",") if k.strip()]}
        if suit == "major":
            card["number"] = sum(1 for c in deck if c["suit"] == "major")
        deck.append(card)
    return deck


def pick(rng, pool_size, n):
    # Partial Fisher-Yates over randrange: a seed keeps meaning the same draw across
    # Python versions (random.sample makes no such promise). Same as the Fleet edition.
    idx, out = list(range(pool_size)), []
    for i in range(n):
        j = i + rng.randrange(pool_size - i)
        idx[i], idx[j] = idx[j], idx[i]
        out.append(idx[i])
    return out


def main():
    p = argparse.ArgumentParser(description="Draw tarot cards as thinking prompts. "
                                "Replay any draw with its printed --seed.")
    p.add_argument("-n", type=int, default=None, help="how many cards (default 3)")
    p.add_argument("--seed", default=None)
    p.add_argument("--spread", choices=sorted(SPREADS), default=None)
    p.add_argument("--no-reversals", action="store_true")
    a = p.parse_args()
    labels = list(SPREADS[a.spread]) if a.spread else None
    n = len(labels) if labels else (a.n if a.n is not None else 3)
    if labels and a.n is not None and a.n != n:
        p.error(f"-n {a.n} conflicts with the {a.spread} spread's {n} positions")
    deck = load_deck()
    if not 1 <= n <= len(deck):
        p.error(f"-n must be between 1 and {len(deck)}")
    seed = a.seed if a.seed is not None else secrets.token_hex(4)
    rng = random.Random(seed)
    chosen = pick(rng, len(deck), n)
    orients = [rng.randrange(2) for _ in chosen] if not a.no_reversals else [0] * n
    cmd = f"draw.py -n {n} --seed {seed}" + (f" --spread {a.spread}" if a.spread else "") \
        + (" --no-reversals" if a.no_reversals else "")
    out = [f"draw -- {n} cards, seed {seed}", f"reproduce: {cmd}", ""]
    w = max((len(l) for l in labels), default=0) if labels else 0
    for slot, (ci, rev) in enumerate(zip(chosen, orients), 1):
        c = deck[ci]
        lead = f"  {labels[slot - 1]:<{w}}  " if labels else f"  {slot}  "
        num = f" ({ROMAN[c['number']]})" if c["suit"] == "major" else ""
        out.append(f"{lead}{c['name']}{num}  {'reversed' if rev else 'upright'}")
        if c["keywords"]:
            out.append(" " * len(lead) + ", ".join(c["keywords"]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
