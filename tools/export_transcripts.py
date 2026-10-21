#!/usr/bin/env python3
"""Export this run's Claude Code transcripts (main session + every subagent) for the
methodology report: raw JSONL copies plus readable Markdown renderings, with identity
strings redacted.

Usage:
    python3 tools/export_transcripts.py [--out methodology/transcripts] [--redact "Jane Doe,janedoe,jane@x.com"]

Redaction always removes email addresses and the home-directory prefix; add names, GitHub
usernames and repository names with --redact. READ the output before submitting it:
the competition publishes methodology material under CC BY 4.0.
"""
import argparse
import glob
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def redactor(extra):
    pats = [re.escape(s) for s in extra if s]
    home = os.path.expanduser("~")
    big = re.compile("|".join(pats), re.I) if pats else None

    def f(s):
        s = EMAIL.sub("[email-redacted]", s)
        s = s.replace(home, "~")
        if big:
            s = big.sub("[redacted]", s)
        return s
    return f


def render(path, red, root, max_tool=1500):
    out = [f"# Transcript: {os.path.basename(path)}\n"]
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        cwd = d.get("cwd") or ""
        if cwd and not os.path.realpath(cwd).startswith(root):
            continue
        t, ts = d.get("type"), d.get("timestamp", "")
        msg = d.get("message")
        if t not in ("user", "assistant") or not isinstance(msg, dict):
            continue
        content = msg.get("content")
        if isinstance(content, str):
            content = [{"type": "text", "text": content}]
        for block in content or []:
            if not isinstance(block, dict):
                continue
            bt = block.get("type")
            if bt == "text" and block.get("text", "").strip():
                out.append(f"\n**{t}** {ts}\n\n{red(block['text'])}\n")
            elif bt == "tool_use":
                inp = json.dumps(block.get("input", {}), ensure_ascii=False)
                out.append(f"\n`{t} tool_use` {block.get('name')} {ts}\n\n```\n{red(inp)[:max_tool]}\n```\n")
            elif bt == "tool_result":
                c = block.get("content")
                if isinstance(c, list):
                    c = "\n".join(x.get("text", "") for x in c if isinstance(x, dict))
                c = red(str(c or ""))
                more = f"\n... [{len(c) - max_tool} more chars in raw JSONL]" if len(c) > max_tool else ""
                out.append(f"\n`tool_result` {ts}\n\n```\n{c[:max_tool]}{more}\n```\n")
            elif bt == "thinking":
                out.append(f"\n_[{t} reasoning block omitted from rendering; present in raw JSONL if recorded]_\n")
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=os.path.expanduser("~/.claude/projects"))
    ap.add_argument("--out", default=os.path.join(ROOT, "methodology", "transcripts"))
    ap.add_argument("--redact", default="")
    a = ap.parse_args()
    red = redactor([s.strip() for s in a.redact.split(",")])
    root = os.path.realpath(ROOT)
    os.makedirs(os.path.join(a.out, "raw"), exist_ok=True)
    os.makedirs(os.path.join(a.out, "readable"), exist_ok=True)
    n = 0
    for path in glob.glob(os.path.join(a.base, "**", "*.jsonl"), recursive=True):
        ok = False
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    cwd = json.loads(line).get("cwd") or ""
                except json.JSONDecodeError:
                    continue
                if cwd and os.path.realpath(cwd).startswith(root):
                    ok = True
                    break
        if not ok:
            continue
        rel = os.path.relpath(path, a.base).replace(os.sep, "__")
        with open(path, encoding="utf-8", errors="replace") as src, \
             open(os.path.join(a.out, "raw", rel), "w", encoding="utf-8") as dst:
            for line in src:
                dst.write(red(line))
        with open(os.path.join(a.out, "readable", rel.replace(".jsonl", ".md")), "w", encoding="utf-8") as f:
            f.write(render(path, red, root))
        n += 1
    print(f"exported {n} transcript file(s) to {a.out}")
    if n == 0:
        print("None found. On a reclaimed cloud VM local transcripts are gone; use the session's share link instead.")


if __name__ == "__main__":
    main()
