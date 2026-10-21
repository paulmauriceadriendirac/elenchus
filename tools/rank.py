#!/usr/bin/env python3
"""Aggregate pairwise judgments into a ranking (Bradley-Terry by MM iterations, plus
Copeland and raw win counts). Pairwise judgments are more reliable than absolute scores
from LLM referees, so selection decisions use this.

Input: a JSONL file, one judgment per line:
    {"a": "C03", "b": "C07", "winner": "C03", "judge": "R2", "confidence": 0.7, "reason": "..."}
"winner" may be "tie". "confidence" (0.5-1.0, optional) weights the judgment.

Usage:
    python3 tools/rank.py state/selection/pairwise.jsonl [--md out.md]
"""
import argparse
import json
import math
from collections import defaultdict


def bradley_terry(items, wins, iters=500, tol=1e-9):
    p = {i: 1.0 for i in items}
    for _ in range(iters):
        new = {}
        for i in items:
            w_i = sum(wins[i][j] for j in items if j != i)
            denom = 0.0
            for j in items:
                if j == i:
                    continue
                n_ij = wins[i][j] + wins[j][i]
                if n_ij:
                    denom += n_ij / (p[i] + p[j])
            new[i] = (w_i + 0.01) / denom if denom else p[i]  # +0.01 keeps undefeated/winless items finite
        s = sum(new.values())
        new = {k: v * len(items) / s for k, v in new.items()}
        delta = max(abs(new[k] - p[k]) for k in items)
        p = new
        if delta < tol:
            break
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--md", default="")
    a = ap.parse_args()
    rows = [json.loads(l) for l in open(a.path, encoding="utf-8") if l.strip()]
    items = sorted({r["a"] for r in rows} | {r["b"] for r in rows})
    wins = defaultdict(lambda: defaultdict(float))
    raw = defaultdict(float)
    played = defaultdict(int)
    for r in rows:
        w = float(r.get("confidence", 1.0) or 1.0)
        x, y, win = r["a"], r["b"], r["winner"]
        played[x] += 1
        played[y] += 1
        if win == "tie":
            wins[x][y] += 0.5 * w
            wins[y][x] += 0.5 * w
            raw[x] += 0.5
            raw[y] += 0.5
        else:
            loser = y if win == x else x
            wins[win][loser] += w
            raw[win] += 1
    bt = bradley_terry(items, wins)
    copeland = {}
    for i in items:
        c = 0
        for j in items:
            if i != j and (wins[i][j] + wins[j][i]) > 0:
                c += 1 if wins[i][j] > wins[j][i] else (-1 if wins[i][j] < wins[j][i] else 0)
        copeland[i] = c
    order = sorted(items, key=lambda k: (-bt[k], -copeland[k]))
    lines = ["| rank | item | Bradley-Terry | log-strength | Copeland | wins/played |",
             "|---:|---|---:|---:|---:|---:|"]
    for n, k in enumerate(order, 1):
        lines.append(f"| {n} | {k} | {bt[k]:.3f} | {math.log(bt[k]):+.2f} | {copeland[k]:+d} | {raw[k]:.1f}/{played[k]} |")
    out = "\n".join(lines)
    print(out)
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write(f"# Pairwise ranking ({len(rows)} judgments)\n\n" + out + "\n")


if __name__ == "__main__":
    main()
