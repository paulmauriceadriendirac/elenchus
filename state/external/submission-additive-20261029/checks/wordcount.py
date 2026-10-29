#!/usr/bin/env python3
"""Word count under the AIPC rule: "Word count ignores the bibliography but includes
everything else" (title, abstract, headings, body, footnotes, appendices, captions, tables).

Usage:
    python3 tools/wordcount.py final/essay.md [--limit 6000] [--target 5600] [--json]

Two counts are reported:
  strict   : every whitespace-separated token left after stripping Markdown markup.
             Conservative (counts math symbols, numbers, section labels). This is the
             number the pipeline must keep under the limit.
  wordlike : tokens containing at least one letter or digit (closer to what a word
             processor reports). Informational only.

The bibliography is a trailing section whose heading is References / Bibliography /
Works Cited (any heading level). Everything from that heading to the next heading of the
same or higher level (or end of file) is excluded. Footnote definitions placed after the
bibliography are still counted.

Exit status: 0 if strict <= limit, 1 otherwise, 2 on usage error.
"""
import argparse
import json
import re
import sys

BIB_HEADINGS = re.compile(r"^(#{1,6})\s*(references|bibliography|works cited|literature cited)\s*$", re.I)
HEADING = re.compile(r"^(#{1,6})\s+")
FOOTNOTE_DEF = re.compile(r"^\[\^[^\]]+\]:\s?")
FOOTNOTE_REF = re.compile(r"\[\^[^\]]+\]")
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def split_bibliography(lines):
    """Return (kept_lines, bib_lines)."""
    kept, bib = [], []
    in_bib, bib_level = False, 0
    for line in lines:
        m = BIB_HEADINGS.match(line.strip())
        h = HEADING.match(line)
        if m:
            in_bib, bib_level = True, len(m.group(1))
            bib.append(line)
            continue
        if in_bib and h and len(h.group(1)) <= bib_level:
            in_bib = False
        if in_bib and FOOTNOTE_DEF.match(line):
            # footnote definitions after the bibliography still count
            kept.append(line)
            continue
        (bib if in_bib else kept).append(line)
    return kept, bib


def strip_markup(text):
    text = HTML_COMMENT.sub(" ", text)
    text = "\n".join(FOOTNOTE_DEF.sub("", l) for l in text.split("\n"))  # before ref removal
    text = FOOTNOTE_REF.sub(" ", text)
    text = LINK.sub(r"\1", text)
    out = []
    for line in text.split("\n"):
        line = HEADING.sub("", line)
        line = re.sub(r"^\s*>\s?", "", line)            # blockquote marker
        line = re.sub(r"^\s*[-*+]\s+", "", line)  # bullet markers only; typed numbers ("1.", "P2") count, as in a word processor
        line = re.sub(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$", "", line)  # table rule rows
        line = line.replace("|", " ")
        line = re.sub(r"(\*\*|__|\*|_|`{1,3}|~~)", "", line)
        out.append(line)
    return "\n".join(out)


def count(path):
    raw = open(path, encoding="utf-8").read()
    fm = FRONT_MATTER.match(raw)
    front_words = 0
    if fm:
        # count only the values of title/subtitle/abstract keys in YAML front matter
        vals = re.findall(r"^(?:title|subtitle|abstract)\s*:\s*(.*)$", fm.group(1), re.M | re.I)
        front_words = sum(len(v.split()) for v in vals)
        raw = raw[fm.end():]
    comments = HTML_COMMENT.findall(raw)
    kept, bib = split_bibliography(raw.split("\n"))
    body = strip_markup("\n".join(kept))
    tokens = body.split()
    strict = len(tokens) + front_words
    wordlike = sum(1 for t in tokens if re.search(r"[A-Za-z0-9]", t)) + front_words
    footnote_lines = [l for l in kept if FOOTNOTE_DEF.match(l)]
    fn_words = len(strip_markup("\n".join(footnote_lines)).split())
    return {
        "file": path,
        "strict": strict,
        "wordlike": wordlike,
        "footnote_words": fn_words,
        "bibliography_lines_excluded": len(bib),
        "html_comments_found": len(comments),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--limit", type=int, default=6000)
    ap.add_argument("--target", type=int, default=5600)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        r = count(a.path)
    except OSError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)
    r["limit"], r["target"] = a.limit, a.target
    r["status"] = "OVER_LIMIT" if r["strict"] > a.limit else ("OVER_TARGET" if r["strict"] > a.target else "OK")
    if a.json:
        print(json.dumps(r, indent=2))
    else:
        print(f"{r['file']}: strict={r['strict']} wordlike={r['wordlike']} "
              f"(footnotes={r['footnote_words']}; bibliography lines excluded={r['bibliography_lines_excluded']}) "
              f"limit={a.limit} target={a.target} -> {r['status']}")
        if r["html_comments_found"]:
            print(f"WARNING: {r['html_comments_found']} HTML comment(s) found. Remove them: hidden text can be read as prompt injection.")
    sys.exit(1 if r["strict"] > a.limit else 0)


if __name__ == "__main__":
    main()

