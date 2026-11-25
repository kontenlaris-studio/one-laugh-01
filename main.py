#!/usr/bin/env python3
"""One Line, One Laugh — one line, one laugh.

Writes the single entry line to /output/entry.txt. Deterministic:
same input, same bytes, every run.
"""
import os

LINE = "My microwave beeps when the food is done, but it never once apologized for the three minutes I waited."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
