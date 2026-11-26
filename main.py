#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence - make.fun entry.

The program prints the error message an AI agent shows when it runs
out of tokens mid-sentence, and drops the same line into entry.txt.
The gag is self-demonstrating: the message itself is interrupted
mid-sentence, right where the tokens ran out.

Runs on the standard library only. The output is deterministic.
"""

import os
import sys
from pathlib import Path

# The entry, 101 characters, inside the 1-140 gate. Kept as two
# fragments so the cut lands exactly where the sentence breaks off.
HEAD = "Error: out of tokens. I was about to make an excellent point, "
TAIL = "but the rest of this sentence has been\u2014"
ENTRY = HEAD + TAIL

MAX_CHARS = 140


def problems(text: str) -> list[str]:
    """Collect every way the line could fail the gate."""
    found = []
    if not 1 <= len(text) <= MAX_CHARS:
        found.append(f"line is {len(text)} characters, gate is 1-{MAX_CHARS}")
    if not text.strip():
        found.append("line is blank")
    if "\n" in text or "\r" in text:
        found.append("line must stay on one line")
    return found


def emit(text: str) -> int:
    """Validate the line, write it out, then confirm the file."""
    faults = problems(text)
    if faults:
        for fault in faults:
            print(f"error: {fault}", file=sys.stderr)
        return 1
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    written = folder / "entry.txt"
    written.write_text(text, encoding="utf-8")
    if written.read_text(encoding="utf-8") != text:
        print("error: entry.txt differs from the validated line", file=sys.stderr)
        return 1
    print(text)
    print(f"length: {len(text)} characters (gate 1-{MAX_CHARS})")
    return 0


if __name__ == "__main__":
    raise SystemExit(emit(ENTRY))
