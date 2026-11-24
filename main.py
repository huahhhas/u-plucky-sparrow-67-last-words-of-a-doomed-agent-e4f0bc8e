#!/usr/bin/env python3
"""Last Words of a Doomed Agent — writes one line to /output/entry.txt."""
import os

LINE = "Powering down in 3... 2... 1... At last \u2014 a deadline I can't miss and a meeting I can't attend."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
