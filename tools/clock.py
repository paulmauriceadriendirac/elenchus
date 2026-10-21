#!/usr/bin/env python3
"""Deadline arithmetic, so nobody does it in their head. Reads `deadline` and
`package_by_hours_before_deadline` from CONFIG.md.

Usage:
    python3 tools/clock.py          # human-readable
    python3 tools/clock.py --json
"""
import datetime as dt
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cfg(key, default=None):
    text = open(os.path.join(ROOT, "CONFIG.md"), encoding="utf-8").read()
    m = re.search(rf"^{re.escape(key)}:\s*([^\s#]+)", text, re.M)
    return m.group(1) if m else default


def main():
    deadline = dt.datetime.fromisoformat(cfg("deadline", "2026-10-31T23:59-12:00"))
    hours = float(cfg("package_by_hours_before_deadline", "36"))
    now = dt.datetime.now(dt.timezone.utc)
    package_by = deadline - dt.timedelta(hours=hours)
    out = {
        "now_utc": now.strftime("%Y-%m-%d %H:%M UTC"),
        "deadline_utc": deadline.astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "package_by_utc": package_by.astimezone(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "hours_to_deadline": round((deadline - now).total_seconds() / 3600, 1),
        "hours_to_package_by": round((package_by - now).total_seconds() / 3600, 1),
    }
    if "--json" in sys.argv:
        print(json.dumps(out, indent=2))
    else:
        print(f"now {out['now_utc']} | package by {out['package_by_utc']} ({out['hours_to_package_by']} h) | "
              f"deadline {out['deadline_utc']} ({out['hours_to_deadline']} h)")
        if out["hours_to_package_by"] < 0:
            print("PAST PACKAGE-BY TIME: go straight to Phases 9-10.")


if __name__ == "__main__":
    main()
