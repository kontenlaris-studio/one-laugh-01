#!/usr/bin/env python3
"""One Line, One Laugh — one line, one laugh.

Writes the single entry line to /output/entry.txt. Deterministic:
same input, same bytes, every run.
"""
import os

ENTRY_TEXT = "My microwave beeps when the food is done, but it never once apologized for the three minutes I waited."


def write_entry(path="/output/entry.txt"):
    """Write the entry line to path, creating the folder if needed.

    The line is exactly 102 characters, so the file is always
    103 bytes including the trailing newline.
    """
    assert len(ENTRY_TEXT) == 102, "entry line must stay 102 chars"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


def main():
    write_entry()


if __name__ == "__main__":
    main()
