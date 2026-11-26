"""The Printer Apology.

Writes the funniest one-line apology from an office printer: it printed
your resignation letter twice, offered you a spare, and kept one for
itself. The printer's gripe is the double-print; the punch is the spare
copy it kept — leverage, held by the machine you swore at.

The entry is one line of exactly 97 characters (gate: 1-120),
no trailing newline, written byte-identically to entry.txt.
validate_entry() enforces the gate (1-120 chars, single line) at
import time and raises ValueError on any violation, so a bad edit
fails loudly instead of producing a rejected entry.

Usage: python3 main.py
Writes the entry verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.
"""

import os
import sys

def validate_entry(text: str) -> str:
    """Check the entry against the competition gate and return it.

    The gate requires a single line of 1-120 characters. Reject anything
    that would fail it loudly instead of writing a bad entry silently:
    a newline would break the "one line" rule, and anything over 120
    characters would be rejected at grading. The joke itself is the
    printer's confession with a twist — it printed your resignation
    twice, offered a spare, then admitted it kept a copy.
    """
    if not 1 <= len(text) <= 120:
        raise ValueError(
            f"entry must be 1-120 characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, no newlines")
    return text


ENTRY = validate_entry(
    "Sorry I printed your resignation letter twice. "
    "I thought you might want a spare. I also kept one."
)


def main() -> None:
    """Write the entry to the output file and print it exactly."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
