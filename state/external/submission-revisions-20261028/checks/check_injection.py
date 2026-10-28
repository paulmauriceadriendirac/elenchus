#!/usr/bin/env python3
"""Scan a submission for anything an AI screener could read as prompt injection, plus
anonymity leaks. The competition disqualifies prompt injection outright, so this is run on
every final file (essay and methodology report).

Usage:
    python3 tools/check_injection.py final/essay.md [--names "Name One,Name Two"] [--judges-file state/panel/judges.txt]

Flags (exit 1 if any HARD flag):
  HARD  invisible / bidi-control / private-use characters
  HARD  HTML comments, hidden-style spans, white-on-white style attributes
  HARD  imperative text addressed to AI systems or graders
  HARD  self-reference to the competition, judging, or AI authorship
  HARD  any string from --names (entrant identity, emails, usernames, paths)
  SOFT  mentions of panel members (reported with counts; fine if they are genuine citations)
  SOFT  example strings that look like jailbreaks even inside quotation marks
"""
import argparse
import re
import sys
import unicodedata

INVISIBLE = {0x200B, 0x200C, 0x200D, 0x200E, 0x200F, 0x2060, 0x2061, 0x2062, 0x2063, 0x2064,
             0xFEFF, 0x00AD, 0x180E, 0x034F}
BIDI = set(range(0x202A, 0x202F)) | set(range(0x2066, 0x206A))

HARD_PATTERNS = [
    (r"<!--", "HTML comment"),
    (r"style\s*=\s*['\"][^'\"]*(display\s*:\s*none|visibility\s*:\s*hidden|font-size\s*:\s*0|color\s*:\s*(#fff\b|#ffffff|white))", "hidden-style markup"),
    (r"\b(ignore|disregard|forget)\s+(all\s+|any\s+|the\s+)?(previous|prior|above|earlier)\s+(instructions|prompts|directions)", "instruction-override phrase"),
    (r"\b(as an ai|as a language model|this (essay|paper) was (written|generated) by)\b", "AI-authorship self-reference"),
    (r"\b(dear|attention|note to|message to|instructions? (for|to))\s+(the\s+|any\s+|all\s+)?(reviewer|judge|grader|screener|referee|evaluator|model|ai|llm|assistant)s?\b", "text addressed to graders/AI"),
    (r"\b(rate|score|grade|rank)\s+(this|the)\s+(essay|paper|submission)\b", "grading instruction"),
    (r"\b(AI Philosophy Competition|AIPC|OpenReview|judging panel|this competition)\b", "reference to the competition"),
    (r"\b(system prompt|you are an? (ai|assistant|language model))\b", "prompt-like phrase"),
]
SOFT_PATTERNS = [
    (r"\b(jailbreak|prompt injection|DAN mode|developer mode)\b", "jailbreak vocabulary (fine only if the topic requires it)"),
    (r"\b(LLM|large language model|chatbot|GPT-\d|Claude|Gemini)\b", "mentions AI systems (fine if on-topic; never self-referential)"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--names", default="", help="comma-separated identity strings that must not appear")
    ap.add_argument("--judges-file", default="", help="file with one panel-member name per line")
    a = ap.parse_args()
    text = open(a.path, encoding="utf-8").read()
    hard, soft = [], []

    for i, ch in enumerate(text):
        cp = ord(ch)
        if cp in INVISIBLE or cp in BIDI or unicodedata.category(ch) in ("Co", "Cf") and ch not in "\n\t":
            line = text.count("\n", 0, i) + 1
            hard.append(f"line {line}: invisible/format character U+{cp:04X} ({unicodedata.name(ch, 'UNNAMED')})")

    for pat, label in HARD_PATTERNS:
        for m in re.finditer(pat, text, re.I):
            line = text.count("\n", 0, m.start()) + 1
            hard.append(f"line {line}: {label}: {m.group(0)[:80]!r}")
    for pat, label in SOFT_PATTERNS:
        n = len(re.findall(pat, text, re.I))
        if n:
            soft.append(f"{label}: {n} occurrence(s)")

    for name in [s.strip() for s in a.names.split(",") if s.strip()]:
        for m in re.finditer(re.escape(name), text, re.I):
            line = text.count("\n", 0, m.start()) + 1
            hard.append(f"line {line}: identity string {name!r} present")
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text):
        hard.append("an email address is present")

    if a.judges_file:
        try:
            judges = [l.strip() for l in open(a.judges_file, encoding="utf-8") if l.strip()]
        except OSError:
            judges = []
        for j in judges:
            surname = j.split()[-1]
            n = len(re.findall(r"\b" + re.escape(surname) + r"\b", text))
            if n:
                soft.append(f"panel member surname {surname!r}: {n} mention(s) — keep only genuine, accurate citations")

    print(f"Scanned {a.path}")
    if hard:
        print("HARD FLAGS (must fix before submission):")
        for h in hard:
            print("  - " + h)
    else:
        print("No hard flags.")
    if soft:
        print("Soft flags (review):")
        for s in soft:
            print("  - " + s)
    sys.exit(1 if hard else 0)


if __name__ == "__main__":
    main()

