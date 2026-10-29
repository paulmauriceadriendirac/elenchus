#!/usr/bin/env python3
"""A5 formal audit, script a6: check that the essay's quotations of and page references to Dorst (2019) match the
retrieved source text (PDF page n = journal p. 174+n), and locate the Holguin (2022) quotations (bonus).
Usage: python3 -I a6_sources.py   (reads the source files by absolute path; no network)."""
import re

SRC = "/home/user/elenchus/state/ambitious/sources/dorst-2019-lockeans.txt"
HOL = "/home/user/elenchus/state/ambitious/sources/holguin-2022-thinking-guessing.txt"
FAILS = []


def norm(s, keep_hyphen):
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff").replace("ﬃ", "ffi")
    s = s.replace("‘", "'").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"-\s*\n\s*", "-" if keep_hyphen else "", s)
    return re.sub(r"\s+", " ", s)


raw = open(SRC, encoding="utf-8").read()
parts = re.split(r"=== PDF page (\d+) ===", raw)
pages = {174 + int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}


def find(pattern, regex=False):
    hits = []
    for pg in sorted(pages):
        for txt in (pages[pg], pages[pg] + "\n" + pages.get(pg + 1, "")):
            for keep in (False, True):
                t = norm(txt, keep)
                ok = re.search(pattern, t) if regex else (pattern in t)
                if ok:
                    hits.append(pg)
                    break
            else:
                continue
            break
    return sorted(set(hits))


ITEMS = [  # (essay text or locator, pattern, regex?, page(s) cited in essay)
    ("'seems to contradict epistemic holism' (Joyce 2009, sec. 5)", "seems to contradict epistemic holism (Joyce 2009", False, [192]),
    ("'to capture the sense in which it matters what other beliefs she holds'", "to capture the sense in which it matters what other beliefs she holds", False, [193]),
    ("'assumes only that A_B0 is well-defined'", r"assumes only that \S+ is well-?defined", True, [193]),
    ("'the value' (of adding a true belief in p)", "the value, relative to B0, of adding a true belief in p", False, [193]),
    ("Sequence-Irrelevance quotation", "rational constraints on beliefs are not affected by the sequence (if any) in which they are formed", False, [194]),
    ("'belief-independent values T_p and F_p'", r"belief-\s?independent values Tp and Fp", True, [195]),
    ("'come from the (dis)values of true (false) beliefs'", "come from the (dis)values of true (false) beliefs", False, [196]),
    ("'until it gets an answer'", "until it gets an answer", False, [190, 191]),
    ("'Who do you think will win?'", "'Who do you think will win?'", False, [190, 191]),
    ("'no holist ever thought ...'", "no holist ever thought that the insight of their position is that the order in which you consider propositions affects what you ought to believe", False, [195]),
    ("'may be purely imaginative'", "may be purely imaginative", False, [194]),
    ("'a set of propositions' (argument of A)", "takes a doxastic state D, a set of propositions", False, [179]),
    ("'best guesses'", "your beliefs are your best guesses", False, [196]),
    ("Accuracy First: inconsistent, nonclosed, empty states allowed", "it need not be consistent, or deductively closed, or non-empty", False, [183]),
    ("Thm 1 and Cor 2 credited to Easwaran", "my Theorem 1 and Corollary 2 are identical to two of his results", False, [183]),
    ("exam scored question by question", "her score on the exam is the sum of her scores on each question", False, [184]),
    ("Conservativeness |T|<|F|, threshold -F/(T-F)", r"Equivalently, when S = 0: jT j < jF ?j", True, [185]),
    ("God example (designing a sequence)", "design a sequence that makes it rational for her to believe", False, [194]),
    ("Proposition 4 (statement)", "Proposition 4. If AB", False, [194]),
    ("Proposition 5 (statement)", "Proposition 5. Given Sequence-Irrelevance", False, [195]),
    ("proof of Prop 5 sets T_p = T^{B-}_p", "That means if we set Tp", False, [206, 207]),
    ("Proposition 3 / Variable Conservativeness", "Thus Variable Conservativeness requires these values", False, [191]),
    ("Maximize Expected Accuracy (rational only if EA maximal)", "is rational only if EA", False, [182]),
]
print("=== Dorst (2019): quotations and page references ===")
for label, pat, rx, cited in ITEMS:
    hits = find(pat, rx)
    ok = bool(hits) and any(h in cited or h + 1 in cited for h in hits)
    print(f"{'OK  ' if ok else 'FAIL'} {label}: found on journal p. {hits}; essay cites {cited}")
    if not ok:
        FAILS.append(label)

print("\n=== Holguin (2022): quotations (bonus; section located by nearest preceding heading) ===")
hraw = open(HOL, encoding="utf-8").read()
ht = norm(hraw, False)
for q in ("brute stipulations about the coordination of the proposition-sensitive thresholds",
          "remains powerless to account for non-monotonicity", "5. Thinking is non-monotonic"):
    i = ht.find(q)
    if i < 0:
        i = norm(hraw, True).find(q)
    heads = [m for m in re.finditer(r"(?<![\d.])(\d{1,2}(?:\.\d)?)\.? (?=[A-Z][a-z])", ht[:max(i, 0)])]
    sec = heads[-1].group(1) if heads else "?"
    print(f"{'OK  ' if i >= 0 else 'FAIL'} '{q}': {'found' if i >= 0 else 'NOT found'}; nearest preceding numbered heading: {sec}")
    if i < 0:
        FAILS.append(q)
print("\nSUMMARY a6:", "ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
