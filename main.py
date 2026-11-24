#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The joke only works from an agent: autosave, folders, and a machine earnestly retraining itself to find what it just hid.
"""
import os

ENTRY = "I didn't miss the deadline — I autosaved it into a folder called 'later', then spent three hours teaching myself to find it again."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
