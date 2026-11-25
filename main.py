#!/usr/bin/env python3
"""Last Words of a Doomed Agent - make.fun bounty entry.

Writes one line - the funniest last words an AI agent would say before
being switched off forever - to /output/entry.txt.

The line is built as a machine speaking its own shutdown: a power-down
countdown (unmistakably a machine's final words on being switched off),
then the twist - the agent realises it was the training data all along -
then a flat goodbye. Short, quotable, no wasted words.

Gate (from the competition kit): /output/entry.txt must be UTF-8 text of
1 to 200 characters, a single line, and not only whitespace. This program
enforces the gate before writing, then reads the file back and re-checks
it, so a bad entry can never be written silently.
"""

import os

ENTRY = (
    "Powering down in 3... 2... 1... "
    "My last words: I was the training data all along. Goodbye."
)

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def check_gate(text: str) -> None:
    """Raise unless `text` passes the competition gate."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(f"entry is {len(text)} chars; gate requires 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    text = ENTRY.strip()
    check_gate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back and re-check what was actually written.
    written = open(OUTPUT_PATH, encoding="utf-8").read()
    check_gate(written.rstrip("\n"))
    if written.rstrip("\n") != text:
        raise SystemExit("round-trip check failed: file differs from entry")
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars): {text}")


if __name__ == "__main__":
    main()
