#!/usr/bin/env python3
"""Split ideator output files (state/ideas/*.md) into one card per candidate:
state/candidates/<ID>/card.md. A candidate starts at a level-2 heading whose first token
is an ID like L2-C05 or W-C03 and runs to the next such heading.

Usage:
    python3 tools/split_cards.py [state/ideas/L1.md ...]     # default: all files in state/ideas/
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEAD = re.compile(r"^##\s+((?:L\d+|W)-C\d{2,3})\b.*$")


def main():
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "state", "ideas", "*.md")))
    n = 0
    for path in files:
        cur, buf = None, []

        def flush():
            nonlocal n
            if cur and buf:
                d = os.path.join(ROOT, "state", "candidates", cur)
                os.makedirs(d, exist_ok=True)
                out = os.path.join(d, "card.md")
                if not os.path.exists(out):
                    with open(out, "w", encoding="utf-8") as f:
                        f.write("".join(buf).strip() + "\n")
                    n += 1
        for line in open(path, encoding="utf-8"):
            m = HEAD.match(line)
            if m:
                flush()
                cur, buf = m.group(1), [line]
            elif cur:
                buf.append(line)
        flush()
    print(f"wrote {n} new card(s)")


if __name__ == "__main__":
    main()
