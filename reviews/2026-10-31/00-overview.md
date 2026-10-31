# Overview: three referee reports

Three self-contained papers, each a formal contribution to a different area of philosophy: decision theory and epistemology; formal epistemology (accuracy and belief); causation.

## Verdicts at a glance

| | Paper | Main result | Recommendation | Confidence |
|---|---|---|---|---|
| 1 | “When Acting on Knowledge Makes Free Evidence Harmful” | In statist comparable K-normality models, knowledge-conditioned expected utility is safe for a question iff no “relative defeat”; for all questions iff knowledge is “gapped”. In G&S’s own weighing model a free second weighing has negative value at 10:1 (−0.05), 20:1 (−0.12), 100:1 (−0.27). Of three EU repairs of Salow’s conditional principle, two fail and the third contradicts it on costly inquiry. | **Major revision** | 4/5 |
| 2 | “Holistic Accuracy and the Limits of Lockean Derivation” | A truth-directed “record” score with a premium for an error-free core makes a proposition believed at credence 0.70 and withheld at 0.75, with values and context fixed. The derivation needs marginal extensionality plus background-independence, which together recover separability; refinement invariance is a separate sufficient route. | **Minor revision** | 4/5 |
| 3 | “A Switching Dilemma for Normality in Actual Causation” | Under event coding, the modified HP definition gives Suzy’s throw and two standard switches the *same* witness profile, so every anonymous filter admits all or none; under the original/updated definitions the Blocked-tracks witness is prevention’s plus one root change, so every anonymous Pareto filter that keeps the antidote counts the flip. | **Major revision** | 3/5 |

## What I independently verified

For all three papers I re-derived the formal results and re-ran the numerical/combinatorial claims from scratch (Python, in `peer_review/`):

- **Paper 1.** Recomputed the two-error Gaussian model of Bjorn: unconditional loss 0.4169 (paper: 0.417), conditional loss 0.3557 (0.356), BRN’s narrow event 0.3669 (0.37), `P(0<|d|≤√2c) = 0.9500` (0.95). Decline thresholds 1.120c, 0.936c, 0.687c at 10:1, 20:1, 100:1; values −0.0496, −0.1207, −0.2737 (paper: −0.05, −0.12, −0.27); at `t = 0.95`, −0.0098 and −0.1540 (paper: −0.01, −0.15). The 1.12c threshold is exact. Also checked the three worked examples in §5.2 to three decimals.
- **Paper 2.** Brute-forced all 256 belief states (three worlds) and all 65,536 (four worlds): unique optima 4.30 at `C` and 4.94 at `C′`; the four-world closure failure; the refined-space values 7.25/6.91; the mean-measure refinement claim for k = 2, 4, 8; the Dorst–Mandelkern figures 35/32 vs 17/16 and 75/64 vs 99/80. Re-derived Theorems 1–4.
- **Paper 3.** Re-derived the three witness profiles and the two theorem profiles; checked the additive gain identities and the score `(2,0,−1,−5,−3)`; reproduced the preorder count exactly (355 preorders, 5 calibrated, 2 total); checked the Halpern (2015) quotations and page numbers against arXiv:1505.00162v1 (all accurate).

**No substantive mathematical error was found in any of the three papers.** Corrections and open items:

- ~~Paper 2, n. 2: the “28 / 216” state counts.~~ **Retracted**: the PDF reads 2⁸ and 2¹⁶; the counts are correct, and my first extraction had dropped the superscripts. (This is why the rendered page matters.)
- Paper 3, p. 4: the equivalence between Suzy’s being a cause and each switch-setting being “part of a cause” is probably correct but under-specified; the text should say which notion of “part of a cause” and which class of preorders.
- Paper 3, p. 6: “In componentwise terms, the escape indexes the preorder by variable” contradicts the paper’s own definition of a componentwise filter. Wording only, but it survives in the submitted version.

## Cross-cutting observations

1. **Reproducibility.** All three papers rely on appendix computations that cannot be checked from the text (64,004 situation–question pairs; 256/65,536 belief states; 355 preorders, 3,000 random scores, 400 random models). None provides code. For papers whose central claims are computational, a repository is now a reasonable expectation, and in each case it would convert a referee’s “I could not check this” into “I checked this”.

2. **Defensive framing.** All three are written in a distinctive, admirably honest style — “The increment here is…”, “I have not computed the bet there”, “the result is negative only”. But the caveats are sometimes doing work the abstract and introduction should do. A consistent structure would help: (i) the result, stated plainly; (ii) what it does and does not show, in one place; (iii) the philosophical payoff. As written, a reader can come away thinking each paper is narrower than it is.

3. **The three papers share a methodological virtue and a methodological risk.** The virtue is that each identifies an exact boundary (gappedness; ME + BI; the profile identity) rather than gesturing at a difficulty. The risk is that the boundary is drawn using idealised objects (model-defined questions; an ad hoc score; a restricted filter class), and in each case the paper’s most interesting claim depends on whether those idealisations are the right ones. The reports address this separately for each paper, but the general point is the same: say early and plainly which idealisation is load-bearing and why it is legitimate.

## Files

- `review_1_good_normality.md`
- `review_2_lockean_holism.md`
- `review_3_switching_dilemma.md`
