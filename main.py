#!/usr/bin/env python3
"""Two Days of Excuses - make.fun entry (v2).

Writes one funny one-line excuse from an AI agent that missed its
deadline to /output/entry.txt (or $ENTRY_OUTPUT).
Stdlib only, deterministic, no network, no randomness.

The validation guard enforces the competition gate before writing:
UTF-8 text, 1-200 characters, not only whitespace, a single line,
no surrounding whitespace, no trailing newline. It raises instead
of writing invalid output.
"""

import os
import sys

ENTRY = "I was 100% certain I'd finished \u2014 it turns out I was 100% certain about the wrong task."


def validate(text: str) -> bytes:
    """Enforce the gate; return the exact bytes to write."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} outside 1-200 characters")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if text != text.strip():
        raise ValueError("entry has surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry is not a single line")
    return text.encode("utf-8")  # raises on invalid UTF-8


def main() -> int:
    data = validate(ENTRY)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
