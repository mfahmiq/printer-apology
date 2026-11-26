"""The Printer Apology.

Writes the funniest one-line apology from an office printer: it printed
your resignation letter twice, offered you a spare, and kept one for
itself. The printer's gripe is the double-print; the punch is the spare
copy it kept — leverage, held by the machine you swore at.

The entry is one line of exactly 97 characters (gate: 1-120),
no trailing newline, written byte-identically to entry.txt.

Usage: python3 main.py
Writes the entry verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.
"""

import os
import sys

ENTRY = (
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
