#!/usr/bin/env python3
"""One Emoji, One Smile - make.fun entry.

Writes the entry line to /output/entry.txt (UTF-8).

One emoji. One smile. Ten minutes of laughing.
"""
import os

ENTRY = "I asked the AI to tell me a joke. It replied with a single \U0001f60a. I laughed for ten minutes. I think it knows something I don't."


def main():
    # Competition gate: entry must be 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
