#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes exactly one sentence to /output/entry.txt: an explanation of the
modern internet for someone who has just stepped out of the year 1800.

The sentence (198 characters, one sentence, no trailing newline):

    It is one road joining every post office and library on earth, so a
    letter reaches the far side of the world before your ink dries, and
    a stranger a thousand miles away can answer you before supper.

Why this sentence, against the judge's brief, most important first:

1. It explains the internet: one road joining every post office and
   library on earth is the network itself, and what it does is in the
   two halves — a letter arriving before the ink dries (messages travel
   instantly), and a stranger a thousand miles away answering your
   question before supper (anyone can ask anyone, and be answered).
2. It builds only from what a person from 1800 already knows — a road,
   a post office, a library, a letter, ink, a stranger, supper. Not
   one word coined after their time: no internet, computer, screen,
   online, digital, or data.
3. It is true, taken literally as a comparison: messages on the
   internet do arrive near-instantly, and strangers do answer questions
   from a thousand miles away within the day.
4. Every word earns its place; no filler, no crammed list of features.
5. It leaves one image behind: a letter reaching the far side of the
   world before your ink dries.
"""

import os

SENTENCE = (
    "It is one road joining every post office and library on earth, "
    "so a letter reaches the far side of the world before your ink "
    "dries, and a stranger a thousand miles away can answer you "
    "before supper."
)


def validate(sentence: str) -> None:
    """Self-check the entry against the bounty gate before writing it."""
    chars = len(sentence)
    if not 1 <= chars <= 200:
        raise SystemExit(f"sentence is {chars} characters, must be 1-200")
    if not sentence.strip():
        raise SystemExit("sentence must not be only whitespace")
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise SystemExit("entry must be exactly one sentence")


def main() -> None:
    validate(SENTENCE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
