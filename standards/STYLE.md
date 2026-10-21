# Essay format and prose

Model: a strong article in a generalist analytic journal (Philosophical Studies, Noûs, Mind,
Analysis, Philosophers' Imprint, Ergo). Clarity is scored; ornament is not.

## Format (Markdown, built to PDF by `tools/build_pdf.py`)

```
# <Title: informative, not cute>

**Abstract.** <120–180 words: the thesis, the argument in one or two sentences, the increment
over the closest prior work, why it matters.>

## 1. Introduction
...
## n. Conclusion            (short, optional; no recap of every section)

## References
<author-date entries for every cited work and nothing else>

[^1]: <footnotes, used sparingly — they count toward the limit>
```

- Citations: author–date in text — (Author 2019), Author (2019, 47) — matching a `## References`
  entry exactly. Page numbers only when verified.
- Numbered premises on their own lines: `(P1) ...`, `(P2) ...`, `(C) ...`. Refer back to them by
  label.
- Cases get short names (in italics) and are set off as indented paragraphs.
- Formal material: inline `$...$` and display `$$...$$` TeX math. Proofs short enough to read; if a
  result was verified by computer, say what was checked and how in one or two sentences.
- No bullet lists in the essay body except numbered premises and, where unavoidable, a short list
  of conditions or desiderata.
- Headings numbered. Word count (title to last footnote, excluding References) ≤ `target_words`.
- American spelling unless the essay quotes otherwise.

## The first page

By the end of the introduction a reader must know: the question; the thesis (in one sentence);
why it is not already known (closest work + increment); how the argument goes; why it matters.
A two-paragraph roadmap at most.

## Prose

- Lead with the claim, then support it. One idea per paragraph.
- Concrete before abstract: give the case, then the principle it bears on.
- Use "I" for the author's claims. Use the opponent's own terms when stating their view.
- Plain words. Avoid: "delve", "tapestry", "landscape", "crucially", "it is important to note",
  "nuanced", "robust" (unless technical), "in the realm of", "a myriad of", "navigate", "unpack"
  (as filler), "at the end of the day", "this begs the question" (unless meant technically).
- No rhetorical questions standing in for arguments. No exclamation marks.
- Em dashes rarely. No paragraph-final summaries of the paragraph just written.
- Hedges only where uncertainty is real, and then once, precisely.
- Conclusion: what has been shown, what has not, what follows. No new material.
