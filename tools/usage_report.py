#!/usr/bin/env python3
"""Estimate tokens and cost of this run from Claude Code's own transcripts
(~/.claude/projects/**.jsonl, including subagent transcripts), filtered to records whose
working directory is inside this repository. Used for budget control between phases and
for the methodology report's "token usage and financial cost" section.

Usage:
    python3 tools/usage_report.py                 # human-readable summary
    python3 tools/usage_report.py --json          # machine-readable
    python3 tools/usage_report.py --md methodology/usage.md
    python3 tools/usage_report.py --since 2026-10-22T00:00:00Z

Costs are list-price ESTIMATES (config/prices.json). Subscription/credit billing may differ;
check /usage in Claude Code for the authoritative figure.
"""
import argparse
import glob
import json
import os
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_prices():
    with open(os.path.join(ROOT, "config", "prices.json"), encoding="utf-8") as f:
        return json.load(f)


def price_for(model, prices):
    m = (model or "").lower()
    for p in prices["models"]:
        if p["match"] in m:
            return p
    return None


def iter_records(base, root, since):
    root = os.path.realpath(root)
    for path in glob.glob(os.path.join(base, "**", "*.jsonl"), recursive=True):
        try:
            fh = open(path, encoding="utf-8", errors="replace")
        except OSError:
            continue
        with fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except json.JSONDecodeError:
                    continue
                cwd = d.get("cwd") or ""
                if not cwd or not os.path.realpath(cwd).startswith(root):
                    continue
                if since and (d.get("timestamp") or "") < since:
                    continue
                yield path, d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=os.path.expanduser("~/.claude/projects"))
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--since", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--md", default="")
    a = ap.parse_args()
    prices = load_prices()

    # One API response can be written as several transcript lines (one per content block),
    # each carrying the same usage object: keep one usage per message id.
    by_msg = {}
    files = set()
    first_ts, last_ts = None, None
    for path, d in iter_records(a.base, a.root, a.since):
        ts = d.get("timestamp")
        if ts:
            first_ts = ts if first_ts is None or ts < first_ts else first_ts
            last_ts = ts if last_ts is None or ts > last_ts else last_ts
        msg = d.get("message")
        if not isinstance(msg, dict) or d.get("type") != "assistant":
            continue
        u = msg.get("usage")
        if not isinstance(u, dict):
            continue
        mid = msg.get("id") or d.get("requestId") or d.get("uuid")
        files.add(path)
        prev = by_msg.get(mid)
        if prev is None or (u.get("output_tokens") or 0) >= (prev[1].get("output_tokens") or 0):
            by_msg[mid] = (msg.get("model") or "unknown", u, "subagents" in path or bool(d.get("isSidechain")))

    agg = defaultdict(lambda: defaultdict(float))
    for model, u, side in by_msg.values():
        if model.startswith("<synthetic"):
            continue
        g = agg[model]
        g["requests"] += 1
        g["subagent_requests"] += 1 if side else 0
        g["input"] += u.get("input_tokens") or 0
        g["output"] += u.get("output_tokens") or 0
        g["cache_read"] += u.get("cache_read_input_tokens") or 0
        cc = u.get("cache_creation") or {}
        if isinstance(cc, dict) and (cc.get("ephemeral_5m_input_tokens") or cc.get("ephemeral_1h_input_tokens")):
            g["cache_write_5m"] += cc.get("ephemeral_5m_input_tokens") or 0
            g["cache_write_1h"] += cc.get("ephemeral_1h_input_tokens") or 0
        else:
            g["cache_write_5m"] += u.get("cache_creation_input_tokens") or 0
        stu = u.get("server_tool_use") or {}
        if isinstance(stu, dict):
            g["web_search_requests"] += stu.get("web_search_requests") or 0

    rows, total, unknown = [], 0.0, []
    for model, g in sorted(agg.items()):
        p = price_for(model, prices)
        if p is None:
            unknown.append(model)
            cost = 0.0
        else:
            cost = (g["input"] * p["input"] + g["output"] * p["output"] + g["cache_read"] * p["cache_read"]
                    + g["cache_write_5m"] * p["cache_write_5m"] + g["cache_write_1h"] * p["cache_write_1h"]) / 1e6
        cost += g["web_search_requests"] * prices.get("web_search_per_1000", 10.0) / 1000
        total += cost
        rows.append({"model": model, **{k: int(v) for k, v in g.items()}, "est_cost_usd": round(cost, 2)})

    result = {"root": a.root, "transcript_files": len(files), "first": first_ts, "last": last_ts,
              "models": rows, "est_total_usd": round(total, 2), "unpriced_models": unknown}
    if a.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Transcripts: {len(files)} files, {first_ts} .. {last_ts}")
        for r in rows:
            print(f"  {r['model']}: {r['requests']} requests ({r['subagent_requests']} subagent), "
                  f"in {r['input']:,} / out {r['output']:,} / cache-read {r['cache_read']:,} / "
                  f"cache-write {r['cache_write_5m'] + r['cache_write_1h']:,} / searches {r['web_search_requests']} "
                  f"-> ${r['est_cost_usd']:.2f}")
        print(f"ESTIMATED TOTAL: ${total:.2f} (list prices; see /usage for billing)")
        if unknown:
            print("Unpriced models (add to config/prices.json):", ", ".join(unknown))
        if not rows:
            print("No usage records found. In a fresh session or a reclaimed cloud VM this is expected; "
                  "fall back to /usage and record the figure by hand.")
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Token usage and estimated cost\n\n")
            f.write(f"Source: Claude Code transcripts ({len(files)} files), {first_ts} to {last_ts}. "
                    "List-price estimate from config/prices.json; billing may differ.\n\n")
            f.write("| model | requests | subagent req. | input | output | cache read | cache write | web searches | est. USD |\n")
            f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
            for r in rows:
                f.write(f"| {r['model']} | {r['requests']} | {r['subagent_requests']} | {r['input']:,} | {r['output']:,} | "
                        f"{r['cache_read']:,} | {r['cache_write_5m'] + r['cache_write_1h']:,} | {r['web_search_requests']} | {r['est_cost_usd']:.2f} |\n")
            f.write(f"\n**Estimated total: ${total:.2f}**\n")


if __name__ == "__main__":
    main()
