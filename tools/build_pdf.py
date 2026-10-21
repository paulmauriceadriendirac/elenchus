#!/usr/bin/env python3
"""Mechanical formatting: Markdown -> PDF (pandoc -> Typst -> PDF), with a .docx fallback.
No content is changed.

Usage:
    python3 tools/build_pdf.py final/essay.md [--out final/essay.pdf]

Needs: pip install pypandoc_binary typst   (pypandoc_binary bundles pandoc)
If PDF building fails, a .docx is produced instead; export it to PDF from any word
processor (mechanical formatting by the human is permitted by the rules).
"""
import argparse
import os
import shutil
import subprocess
import sys

PREAMBLE = r"""#set page(paper: "a4", margin: (x: 2.5cm, y: 2.5cm), numbering: "1")
#set text(size: 11pt, lang: "en")
#set par(justify: true, leading: 0.7em)
#set heading(numbering: none)
#show heading.where(level: 1): set text(size: 15pt)
#show heading.where(level: 2): set text(size: 12.5pt)
#show heading.where(level: 3): set text(size: 11pt, style: "italic")
"""


def pandoc_bin():
    try:
        import pypandoc
        return pypandoc.get_pandoc_path()
    except Exception:
        return shutil.which("pandoc")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    out = a.out or os.path.splitext(a.src)[0] + ".pdf"
    pd = pandoc_bin()
    if not pd:
        print("pandoc not found: pip install pypandoc_binary", file=sys.stderr)
        sys.exit(2)
    base = os.path.splitext(out)[0]
    typ = base + ".typ"
    try:
        subprocess.run([pd, a.src, "-f", "markdown+tex_math_dollars+footnotes+smart",
                        "-t", "typst", "-s", "-o", typ], check=True)
        body = open(typ, encoding="utf-8").read()
        with open(typ, "w", encoding="utf-8") as f:
            f.write(PREAMBLE + "\n" + body)
        import typst
        typst.compile(typ, output=out)
        print(f"wrote {out}")
        os.remove(typ)
        return
    except Exception as e:
        print(f"PDF route failed ({e}); writing .docx instead", file=sys.stderr)
    docx = base + ".docx"
    subprocess.run([pd, a.src, "-f", "markdown+tex_math_dollars+footnotes+smart", "-o", docx], check=True)
    print(f"wrote {docx} (convert to PDF in a word processor)")


if __name__ == "__main__":
    main()
