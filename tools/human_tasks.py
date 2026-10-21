#!/usr/bin/env python3
"""Everything the pipeline needs a human courier for, in one checklist (HUMAN_TODO.md):

  1. FETCH requests  — sources the agents could not reach (paywalls, bot walls, 403s).
     Agents file one request each:  requests/fetch/<slug>.md
     The human puts the source at:  inbox/sources/<slug>.pdf  (or .txt / .md / .html)
     or pastes the text into the chat (the orchestrator saves it under that name),
     or marks it unobtainable:     inbox/sources/<slug>.unavailable  (empty file is fine)
  2. RELAY packets   — optional tasks for another AI model (cross-model refereeing etc.).
     Packet:   relay/outbox/<id>.md   -> paste into the other model verbatim
     Response: relay/inbox/<id>.md    -> paste the reply verbatim; first line "model: <name + version>"
  3. GATE            — a decision the run is waiting on (state/GATE.md, written by the orchestrator).

Fetching what the AI asks for is courier work, not a philosophical contribution; never add
commentary, highlights or selections of your own to fetched material or relayed replies.

Usage:
    python3 tools/human_tasks.py list      # print + write HUMAN_TODO.md
    python3 tools/human_tasks.py status    # counts only (for the orchestrator)
    python3 tools/human_tasks.py new-fetch --slug lewis1973-causation --citation "..." --urls "..." \
            --need "full text" --why "..." --priority high --by "prior-art-hunter L2-C05"
"""
import argparse
import datetime
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FETCH_DIR = os.path.join(ROOT, "requests", "fetch")
SRC_DIR = os.path.join(ROOT, "inbox", "sources")
OUTBOX = os.path.join(ROOT, "relay", "outbox")
INBOX = os.path.join(ROOT, "relay", "inbox")
GATE = os.path.join(ROOT, "state", "GATE.md")
TODO = os.path.join(ROOT, "HUMAN_TODO.md")
PRI = {"high": 0, "normal": 1, "low": 2}


def parse(path):
    d = {"slug": os.path.splitext(os.path.basename(path))[0]}
    for line in open(path, encoding="utf-8", errors="replace"):
        m = re.match(r"^([a-z_]+)\s*:\s*(.*)$", line.strip())
        if m:
            d[m.group(1)] = m.group(2)
    return d


def satisfied(slug):
    hits = [p for p in glob.glob(os.path.join(SRC_DIR, slug + ".*"))]
    if any(p.endswith(".unavailable") for p in hits):
        return "unavailable"
    return "fetched" if hits else None


def collect():
    fetch = [parse(p) for p in sorted(glob.glob(os.path.join(FETCH_DIR, "*.md")))]
    for f in fetch:
        f["state"] = satisfied(f["slug"]) or "open"
    relay = []
    for p in sorted(glob.glob(os.path.join(OUTBOX, "*.md"))):
        rid = os.path.splitext(os.path.basename(p))[0]
        relay.append({"id": rid, "state": "answered" if os.path.exists(os.path.join(INBOX, rid + ".md")) else "open",
                      "target": parse(p).get("target_model", "any frontier model other than Claude")})
    gate = open(GATE, encoding="utf-8").read() if os.path.exists(GATE) else ""
    return fetch, relay, gate


def where_to_upload():
    """In a git checkout (always, in a cloud session) say which repo and branch to upload to."""
    def git(*args):
        try:
            return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=10).stdout.strip()
        except Exception:
            return ""
    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    if not branch or branch == "HEAD":
        return ""
    url = git("remote", "get-url", "origin")
    m = re.search(r"([\w.-]+/[\w.-]+?)(?:\.git)?/?$", url)
    repo = m.group(1) if m else "your repository"
    if os.environ.get("CLAUDE_CODE_REMOTE") == "true":
        return (f"**Cloud session:** on GitHub, open `{repo}`, switch to branch `{branch}`, go to `inbox/sources/`, "
                "use *Add file → Upload files*, commit to that branch, then tell the session \"fetched\". "
                "Or paste the text straight into the chat and name its slug.")
    return (f"Local checkout (branch `{branch}`): put files straight into the `inbox/sources/` folder, then tell "
            "the session \"fetched\".")


def write_todo(fetch, relay, gate):
    lines = ["# What the run needs from you", "",
             f"_Updated {datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M UTC}. "
             "Courier work only: fetch exactly what is asked, add nothing of your own._", ""]
    if gate.strip():
        lines += ["## Decision waiting (gate)", "", gate.strip(), ""]
    open_f = sorted([f for f in fetch if f["state"] == "open"], key=lambda f: PRI.get(f.get("priority", "normal"), 1))
    if open_f:
        lines += ["## Sources to fetch", "",
                  "Save each as `inbox/sources/<slug>.pdf` (or .txt/.md/.html), or paste the text into the chat "
                  "and say which slug it is. If you cannot get it, create `inbox/sources/<slug>.unavailable` "
                  "(or just say so in the chat).", ""]
        hint = where_to_upload()
        if hint:
            lines += [hint, ""]
        for f in open_f:
            lines += [f"### `{f['slug']}`  ({f.get('priority', 'normal')})",
                      f"- **Citation:** {f.get('citation', '?')}",
                      f"- **Where to try:** {f.get('urls', '?')}",
                      f"- **Needed:** {f.get('need', 'full text')}",
                      f"- **Why:** {f.get('why', '')}",
                      f"- **Requested by:** {f.get('requested_by', '?')}", ""]
    open_r = [r for r in relay if r["state"] == "open"]
    if open_r:
        lines += ["## Relay packets for another model (optional)", "",
                  "Paste `relay/outbox/<id>.md` into the other model verbatim, then save its full reply, unedited, as "
                  "`relay/inbox/<id>.md` with first line `model: <name and version>`.", ""]
        for r in open_r:
            lines.append(f"- `{r['id']}` → {r['target']}")
        lines.append("")
    if not (gate.strip() or open_f or open_r):
        lines += ["Nothing needed right now."]
    open(TODO, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return len(open_f), len(open_r), bool(gate.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["list", "status", "new-fetch"])
    for k in ("slug", "citation", "urls", "need", "why", "priority", "by"):
        ap.add_argument("--" + k, default="")
    a = ap.parse_args()
    os.makedirs(FETCH_DIR, exist_ok=True)
    os.makedirs(SRC_DIR, exist_ok=True)
    os.makedirs(OUTBOX, exist_ok=True)
    os.makedirs(INBOX, exist_ok=True)
    if a.cmd == "new-fetch":
        slug = re.sub(r"[^a-z0-9-]+", "-", a.slug.lower()).strip("-")
        if not slug:
            print("--slug required", file=sys.stderr)
            sys.exit(2)
        path = os.path.join(FETCH_DIR, slug + ".md")
        if os.path.exists(path):
            print(f"exists: {path}")
            return
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"slug: {slug}\ncitation: {a.citation}\nurls: {a.urls}\nneed: {a.need or 'full text'}\n"
                    f"why: {a.why}\npriority: {a.priority or 'normal'}\nrequested_by: {a.by}\n"
                    f"requested_at: {datetime.datetime.now(datetime.timezone.utc):%Y-%m-%dT%H:%M:%SZ}\n")
        print(f"filed {path}")
        return
    fetch, relay, gate = collect()
    nf, nr, g = write_todo(fetch, relay, gate)
    done = sum(1 for f in fetch if f["state"] == "fetched")
    unav = sum(1 for f in fetch if f["state"] == "unavailable")
    print(f"fetch: {nf} open, {done} fetched, {unav} unavailable | relay: {nr} open | gate: {'WAITING' if g else 'none'}")
    if a.cmd == "list":
        print(open(TODO, encoding="utf-8").read())


if __name__ == "__main__":
    main()
