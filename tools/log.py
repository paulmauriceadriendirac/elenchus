#!/usr/bin/env python3
"""Append timestamped entries to the methodology logs. Text is read from stdin so that
verbatim human messages survive quoting.

Usage:
    python3 tools/log.py event  "Phase 2 complete: 38 candidates in state/ideas/"
    python3 tools/log.py agent  "red-team on L2-C05 -> REPAIR (state/candidates/L2-C05/redteam.md)"
    python3 tools/log.py human --class generic-feedback <<'EOF'
    This section is unclear.
    EOF
    python3 tools/log.py decision "Selected L2-C05 (BT 2.41) over L1-C02 (BT 1.13); fallback L1-C02"

Classes for human input: logistics | selection | generic-feedback | topic-choice |
                         rejected-substantive (logged, NOT acted on)
"""
import argparse
import datetime
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "methodology", "log.md")
HUMAN = os.path.join(ROOT, "methodology", "human_inputs.md")


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def append(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if new:
            title = "Human inputs (verbatim)" if path == HUMAN else "Run log"
            f.write(f"# {title}\n\n")
        f.write(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["event", "agent", "decision", "human", "warning"])
    ap.add_argument("text", nargs="?", default=None)
    ap.add_argument("--class", dest="klass", default="logistics")
    a = ap.parse_args()
    text = a.text if a.text is not None else sys.stdin.read()
    text = text.rstrip("\n")
    if a.kind == "human":
        block = "\n".join("> " + l for l in text.split("\n"))
        append(HUMAN, f"## {now()} — class: {a.klass}\n\n{block}\n\n")
        append(LOG, f"- {now()} **human** ({a.klass}): see human_inputs.md\n")
    else:
        append(LOG, f"- {now()} **{a.kind}**: {text}\n")
    print("logged")


if __name__ == "__main__":
    main()
