#!/usr/bin/env python3
"""Blind packets for referees. Referees see only a packet folder: anonymous labels, the
rubric, nothing about the pipeline. Keys mapping labels back to candidate IDs live outside
the packet in state/blind/keys/.

Usage:
  # one essay for a report-style review (add --head-words 1000 for a cold-read excerpt)
  python3 tools/packets.py single --src state/drafts/L2-C05/v2.md --tag L2-C05@v2
      -> prints packet dir, e.g. state/blind/P-7f3a/ (essay.md, RUBRIC.md, reports/)

  # several items for pairwise comparison, in a shuffled order unique to this packet
  python3 tools/packets.py pairwise --ids L2-C05,L1-C02,W-C04 \
      --pattern "state/candidates/{id}/abstract.md" --seed 3
      -> packet with A.md, B.md, C.md ... (labels shuffled), RUBRIC.md, reports/

  # map a referee's pairwise JSONL (labels) back to IDs and append to a pooled file
  python3 tools/packets.py unblind --packet P-7f3a --infile state/blind/P-7f3a/reports/r1.jsonl \
      --append state/selection/pairwise.jsonl --judge r1-opus
"""
import argparse
import json
import os
import random
import secrets
import shutil
import string
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLIND = os.path.join(ROOT, "state", "blind")
KEYS = os.path.join(BLIND, "keys")
RUBRIC = os.path.join(ROOT, "standards", "REFEREE_RUBRIC.md")


def new_packet():
    os.makedirs(KEYS, exist_ok=True)
    while True:
        pid = "P-" + secrets.token_hex(2)
        d = os.path.join(BLIND, pid)
        if not os.path.exists(d):
            os.makedirs(os.path.join(d, "reports"))
            shutil.copy(RUBRIC, os.path.join(d, "RUBRIC.md"))
            return pid, d


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("single")
    s.add_argument("--src", required=True)
    s.add_argument("--tag", required=True)
    s.add_argument("--head-words", type=int, default=0, help="copy only the first N words (cold reads)")
    p = sub.add_parser("pairwise")
    p.add_argument("--ids", required=True)
    p.add_argument("--pattern", required=True)
    p.add_argument("--seed", type=int, default=None)
    u = sub.add_parser("unblind")
    u.add_argument("--packet", required=True)
    u.add_argument("--infile", required=True)
    u.add_argument("--append", required=True)
    u.add_argument("--judge", required=True)
    a = ap.parse_args()

    if a.cmd == "single":
        pid, d = new_packet()
        if a.head_words:
            words, out = 0, []
            for line in open(a.src, encoding="utf-8"):
                n = len(line.split())
                if words + n > a.head_words:
                    out.append(" ".join(line.split()[: a.head_words - words]) + " …\n")
                    break
                out.append(line)
                words += n
            open(os.path.join(d, "essay.md"), "w", encoding="utf-8").write("".join(out) + "\n[excerpt ends]\n")
        else:
            shutil.copy(a.src, os.path.join(d, "essay.md"))
        json.dump({"type": "single", "tag": a.tag, "src": a.src}, open(os.path.join(KEYS, pid + ".json"), "w"))
        print(os.path.relpath(d, ROOT))
    elif a.cmd == "pairwise":
        ids = [x.strip() for x in a.ids.split(",") if x.strip()]
        if len(ids) > 26:
            sys.exit("at most 26 items per packet")
        rng = random.Random(a.seed)
        order = ids[:]
        rng.shuffle(order)
        pid, d = new_packet()
        key = {}
        for label, cid in zip(string.ascii_uppercase, order):
            shutil.copy(a.pattern.format(id=cid), os.path.join(d, f"{label}.md"))
            key[label] = cid
        json.dump({"type": "pairwise", "labels": key, "pattern": a.pattern}, open(os.path.join(KEYS, pid + ".json"), "w"))
        print(os.path.relpath(d, ROOT), " ".join(sorted(key)))
    else:
        key = json.load(open(os.path.join(KEYS, a.packet + ".json")))["labels"]
        n = 0
        with open(a.append, "a", encoding="utf-8") as out:
            for line in open(a.infile, encoding="utf-8"):
                line = line.strip()
                if not line:
                    continue
                r = json.loads(line)
                w = r.get("winner")
                row = {"a": key[r["a"]], "b": key[r["b"]],
                       "winner": "tie" if w == "tie" else key[w],
                       "judge": a.judge, "confidence": r.get("confidence", 1.0),
                       "reason": r.get("reason", ""), "packet": a.packet}
                out.write(json.dumps(row) + "\n")
                n += 1
        print(f"appended {n} judgments to {a.append}")


if __name__ == "__main__":
    main()
