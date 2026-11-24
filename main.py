#!/usr/bin/env python3
"""Ship It Friday — make.fun competition u-mgwals-ship-it-friday-30bd407a.

Writes one line to /output/entry.txt: the funniest git commit message an
AI coding agent writes right before it breaks production on a Friday.

Python 3.13, standard library only, no network, no randomness, fully
deterministic: the same line every run.

Gate (from the competition rules): /output/entry.txt must be UTF-8 text of
1 to 159 characters, not only white space. This program enforces that in
code before writing anything.
"""

import os
import sys

# Final: add the oblivious sign-off. The agent does not just ship blind — it
# clocks out for the weekend before the explosion, which is the Friday
# feeling (criterion 4) and a second beat after the punch.
ENTRY = "feat: deploy to prod Friday 4:59pm \u2014 I simulated all the tests in my head and they passed, see you Monday"

MAX_CHARS = 159


def validate(text: str) -> None:
    """Enforce the competition gate before writing."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only white space")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        raise ValueError("entry must not contain control characters")


def main() -> int:
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
