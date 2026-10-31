# Reproduction addendum — 31 October 2026

A second machine (Python 3.12.3) installed the audit dependencies into a scratch directory
outside the repository — sympy 1.14.0, z3-solver 5.3.3.0, numpy 2.5.4, mpmath 1.3.0 (61 MB
download, 269 MB on disk) — and reran every `state/audit/**` script, comparing stdout
byte-for-byte with the recorded `.out` files.

| Script | Result |
|---|---|
| A4 `hp_audit.py` | **identical** (94 checks, 91 pass; the 3 "FAIL" lines are the intended "total orders" test) |
| A4 `lemma_audit.py` | **identical** (0 counterexamples; 27,474 causes, 114,513 conforming witnesses) |
| A5 `a1`–`a5`, `a7` | **identical** |
| A5 `a6_sources.py` | **identical after** substituting the hardcoded path (see below) |
| A6 `finite_checks.py`, `examples.py`, `bjorn_numeric.py`, `bjorn_51_precise.py` | **identical** |

## What this establishes

- The recorded outputs are reproducible on a clean machine, not merely plausible.
- `bjorn_51_precise` gives `d* = 1.12022c` and bet EV **−0.602089** on the decline hypothesis; the
  submitted A6 has −0.60. The v4 −0.63 was a grid artefact, and the final has the corrected value.
- `examples.py` prints 64,004 non-trivial-partition pairs and 3,306 relative-defeat pairs when `E`
  ranges over every body of evidence; the submitted A6's "64,004 … 3,306" is that count, and the
  2,322 figure is the `E = S` sub-case. Consistent.
- A4's three failing checks are the only remaining "false wording" inherited from v6, and the
  submitted PDF already says "total preorders", which is correct.
- The A4 corollary's SMT check (unsat over all anonymous Pareto filters and over all real additive
  scores with `r > 0`) is inside `hp_audit.py` and reproduces.

## Portability defect worth fixing

`state/audit/A5/formal/a6_sources.py` hardcodes `/home/user/elenchus/...` for its source texts. On
any other machine it raises `FileNotFoundError` before checking anything. Substituting the actual
clone path makes it pass. If the audits are to be cited as rerunnable, parameterise the source
directory (env var, or a path relative to `__file__`).

## Still unverified

Halpern (2016) page pinpoints (84–85, 121, 133–134, 149–150, §3.3): no copy of the book.
BRN and Salow (2025) quotations: not in the repository. The G&S 2023, Dorst 2019, Xiao–Xiong 2026
and Andreas–Günther 2024 source texts *are* in the repository, and their quotation checks pass.
