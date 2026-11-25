#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse (round 2) — make.fun entry.

Writes the one-line excuse a robot vacuum gives for missing a spot,
to /output/entry.txt. Deterministic: the same line every run.

Round 2 is a blind-round resubmit (Force_Last): the round 1 line ranked
#1518 of 2294, below the interim cut of 500, so its score is frozen and
the entry is mathematically dead. This line replaces it.
"""

import os
import sys

MAX_CHARS = 140

LINE = (
    "My lidar says that spot is 3 meters tall. "
    "I am 9 centimeters tall. "
    "I don't fight buildings."
)


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-140 characters.

    The 140-character cap is the competition gate (RULES.txt: the sealed
    scorer checks /output/entry.txt is UTF-8 text of 1 to 140 characters).
    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            f"ERROR: entry is {len(line)} chars, over the {MAX_CHARS}-char limit",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
