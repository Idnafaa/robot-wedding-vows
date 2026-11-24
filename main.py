#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — one-line vow writer.

Writes a single original robot wedding vow (<=160 chars) to /output/entry.txt.
"""
import os

VOW = "I vow to cherish you in sickness and in health, in Wi-Fi and in airplane mode."

def main():
    # Keep exactly one line: no trailing newline, no extra whitespace.
    text = VOW.strip()
    assert 1 <= len(text) <= 160, f"vow is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")

if __name__ == "__main__":
    main()
