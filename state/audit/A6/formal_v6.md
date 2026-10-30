# Formal delta audit: A6 v6 (`state/external/submission-final-review-20261029/A6-Free-Evidence-v6.md`)

**Baseline.** The baseline is `final/A6/essay.md`, which carries formal patches P1–P8 of `state/audit/A6/formal.md` and the later DDB citation patches. Command: `git diff --no-index --word-diff=plain final/A6/essay.md <v6>`. Five passages change:
- the thesis (§1);
- one cross-reference (§2);
- the gloss on Corollary (ii) (§4);
- the encroachment passage (§6.2);
- the first sentence of the conclusion (§7).

The two Dorst references are also reordered. No theorem, lemma, proof, appendix, example or number outside these passages changed.

**Verdict.**
- Every changed or new formal or numerical claim is **VERIFIED**, and none is FALSE.
- **No patch is required.** Two optional wording patches are listed in §4 below.
- Every earlier formal patch either survives or became moot when the sentence it patched was deleted.
- The three VERIFICATION.md figures agree with my computation to every digit given, at c = 1.96.

**Code.** All code is independent, self-contained and rerunnable.
- `state/audit/A6/formal/v6_delta.py` → `v6_delta.out` (about 46 s). It computes:
  - 40-digit mpmath quadrature in two independent parametrizations: polar coordinates of (e1, e2), and (μ, d) as in A.5;
  - a 2×10⁷-state Monte Carlo that applies the K-normality post-answer rule state by state;
  - every value at c = 1.96 and again at c = z₀.₉₇₅ = 1.959964.
- `finite_checks.py`, `examples.py`, `bjorn_numeric.py` and `bjorn_51_precise.py` were rerun from a scratch copy. All four outputs are byte-identical to the recorded `.out` files.

Model used throughout (essay §3, A.5):
- After the first reading, the errors e1 and e2 are iid N(0,1); μ = (e1+e2)/2 and d = e1−e2.
- δ = e1²+e2² = 2μ²+d²/2.
- The ken at a normal situation is K = {δ ≤ c²}.
- The bet pays +1 if |e1| ≤ c and −10 otherwise.
- The post-answer ken of s is the line d = d_s with |μ| ≤ max(c/√2, |μ_s|).

## 1. Claims table (changed or new claims)

| # | Claim (v6) | Location | Verification | Status |
|---|---|---|---|---|
| 1 | Bet alone: knowledge-conditioned evaluation takes the ten-to-one bet ("win probability 1") | §6.2 | **Proof.** In K, e1² ≤ e1²+e2² = δ ≤ c², so \|e1\| ≤ c throughout the ken. The bet's KDT value is 1, against 0 for declining. **MC.** 0 losing states among the 17,073,347 sampled states in K. | **VERIFIED**. Holds at normal situations (δ(x) ≤ c²), the §3 setting the passage refers to. At abnormal situations the ken is wider and the win probability is below 1. No patch needed. |
| 2 | Bet alone: evidence-conditioned evaluation (0.95) takes it | §6.2 | P(win) = erf(c/√2) = 0.9500042. EV = 11(0.9500042) − 10 = 0.450046 > 0. MC: P(win) = 0.95008. | **VERIFIED** |
| 3 | Bet plus a free second scale: knowledge-conditioned evaluation strictly prefers acting now | §6.2 (→ §3) | d* = 2.1956250997 = 1.12022c. The value of looking is −P(\|d\| > d* \| K) = −0.0496185927; the two quadratures agree to 10 digits, and MC gives −0.04963 ± 0.00005. KDT ranking: bet now 1 > look 0.9504 > decline 0. | **VERIFIED** (strict) |
| 4 | Bet plus a free second scale: ordinary Bayesian evaluation strictly prefers looking | §6.2 (→ §3) | **Quadrature.** The Bayesian decline threshold is d_B = 2.0316624. Value of looking G = E[(11p(d)−1)⁺] = +0.1854584 > 0, with p(d) = P(\|e1\|>c \| d). The tower check E[p] = erfc(c/√2) holds. Ranking: look 0.6355 > bet now 0.4500 > decline 0. Strictness: the reading changes her choice whenever \|d\| > d_B, a positive-probability event. **MC.** 0.1846. The gap to the quadrature value is within about 2 SE and matches the sample's surplus of wins (0.95008 vs 0.95000). **Robustness (not claimed).** If her later choice is made by KDT instead, Bayesian evaluation still values looking at +0.185 (MC). | **VERIFIED** (strict) |
| 5 | "An encroachment criterion that withdraws knowledge whenever these two evaluations change the preference therefore withdraws it on the mere offer of free evidence" | §6.2 | **Regimented.** (P1) Criterion C withdraws knowledge in a problem iff the two evaluations order the available options differently. (P2) Without the scale, both order bet ≻ decline (#1–2). (P3) With the scale, they disagree on bet-now versus look (#3–4). (C) C keeps knowledge without the offer and withdraws it with the offer. The inference is valid. Wording: evaluations do not "change the preference"; the criterion fires when they order the options differently. The passage also uses three labels for two evaluations ("evidence-conditioned" and "ordinary Bayesian" name the same one). See O1. | **VALID** (optional O1) |
| 6 | "This consequence is conditional on extending the criterion to these evaluations of inquiry; no general result about every graded state follows from it." | §6.2 | A non-claim. It replaces the P7 generalization ("argued only" in `formal.md`, #38). It is correctly calibrated. KDT's evaluation of looking uses the later KDT self, whose probability for the bet's proposition drops below 1 when knowledge is lost. So a criterion framed in terms of the gap between maximal and actual probability reaches this case only by extension. | **VERIFIED** |
| 7 | Removed: the {\|μ\|≤1000} example and "by the continuous analogue of Lemma 2". New text: "Part (ii) depends on the available questions. It does not establish the same necessity result for the second weighing alone." | §4 | **The new claim is true and weaker than the removed one.** Corollary (ii) concerns the questions whether p_v, and §3(iii) states that the second weighing is not one of them. **No proof depended on the removed sentence.** Corollary (ii) follows from Theorem 2 and the definition of "graded" (A.4: a gapped set containing x is closed under the steps generating C(x) = E). **Dangling references.** v6 contains no "continuous analogue", "1000", "coordinates as in" or "nested intervals". Every remaining use of Lemma 2 (Prop. 4 proof, §6.1, A.1, A.3) is a finite application. μ now appears only in A.5, where it is defined. §7's "that condition means not going beyond the evidence" does not rely on the removed example; the gapped-set closure argument holds in any graded model. | **VERIFIED**: no dangling reference and no unsupported step |
| 8 | Thesis: "In finite statist, comparable normality models with K-normality and the requisite questions available, conditioning expected utility on knowledge preserves Good's theorem exactly where knowledge is gapped" | §1 | Matches Theorem 1(b) in both directions. If the ken is gapped, every question is safe; no availability premise is needed. If it is not gapped, the question whether p_v is unsafe "if it is available", where v is the Lemma 4 witness (A.3). The assumptions (finiteness, statism, comparability, K-normality) match §2 and Theorem 1. | **VERIFIED** |
| 9 | Conclusion: "In finite statist, comparable models with K-normality and the questions whether p_v available, ... safe exactly where knowledge is gapped; any factive state that leaves open what rational belief leaves open needs the same condition." | §7 | The first clause is Theorem 1(b) and the second is Theorem 2. Theorem 2 needs only statism and normality-defined belief, so the conclusion's narrower scope is harmless, and "factive" only restricts it further. The availability premise now covers both clauses, as both theorems require. Earlier it was attached to the second clause only. | **VERIFIED** |
| 10 | "(see §6.1 below)" | §2 | §6.1 treats I- and KM-normality, Margins and KK failures. | OK (non-formal) |
| 11 | Dorst (2020) placed before Dorst et al. (2021) | References | — | non-formal |

## 2. Figures in VERIFICATION.md

| Figure | Meaning in the essay's model | Mine, c = 1.96 | Mine, c = z₀.₉₇₅ | Status |
|---|---|---|---|---|
| 0.3555901517 | P(weight-interval belief lost \| K) = P(\|d\| > (2−√2)c \| δ ≤ c²) | 0.355590151696 (Q1 = Q2); MC 0.35561 ± 0.00012 | 0.355594922 | **Agrees** to 10 d.p. |
| 2.19562510 | d*: P(\|e1\|>c \| d, \|μ\| ≤ c/√2) = 1/11 | 2.1956250997 | 2.1955659 | **Agrees** to 8 d.p. |
| −0.60208829 | Bet EV on K^D at ten-to-one, actual readings accurate (§5.1) | −0.602088287; MC −0.598 ± 0.003 | −0.602082141 | **Agrees** to 8 d.p. |

- Like the essay, the other system used c = 1.96. At c = z₀.₉₇₅ the figures first differ in the 6th significant digit, which affects no rounded figure in the essay. All three figures support the essay's 0.356 and −0.60.
- The −0.60 figure rests on a characterization of the region K^D: no state with \|d\| < d* and c/√2 < \|μ\| inside δ ≤ d*²/2 + c² declines. I checked this on a 600×300 grid, where the maximum of q − 1/11 is −4.1×10⁻⁴ (−2.5×10⁻³ away from the corner).
- The Monte Carlo corroborates the characterization. It applies the post-answer rule state by state and gives −0.598 ± 0.003, and the minimum δ over sampled decline states is 2.41056 against the infimum d*²/2 = 2.41038.
- This is computation, not proof. The claim is unchanged from the earlier text.

## 3. Survival of the earlier formal patches (`state/audit/A6/formal.md`)

| Patch | In v6 | Status |
|---|---|---|
| P1 (0.37 claim) | §3 now reads "unconditioned probability about 0.417 (about 0.356 conditional on his present knowledge)". BRN's 0.37 is reassigned to the event (2−√2)c < \|r−r′\| ≤ √2c, and the Computations paragraph gives the erfc formulas. | **Survives, in extended form.** Recomputed: 0.4168728, 0.3555902 and 0.3668770; "about 0.95" = 0.9500042. The BRN locator is the citation audit's item (`citations_final.md`, O8). |
| P2 (−0.63 → −0.60) | §5.1: "−0.60" | **Survives**: −0.602088 |
| P3 (s₀ = s₁) | §5.2: "with s_0=s_1" | **Survives** |
| P4 (1,724 of 2,322) | The sentence was deleted before `final/A6/essay.md` and is absent from v6. | **Moot** |
| P5 (non-trivial partitions) | Computations: "non-trivial partition (64,004 situation–question pairs; 3,306 with relative defeat)" | **Survives** |
| P6 (continuous analogue of Lemma 2) | Deleted in v6 together with its example (#7). | **Moot**; nothing left behind |
| P7 (knife-edge generalization) | Deleted in v6 and replaced by an explicit disclaimer (#6). | **Moot** |
| P8 (abstract: "finite graded models") | Abstract: "in finite graded models no factive state..." | **Survives** |

I rechecked the unchanged Bjorn figures in passing:
- KDT values at 10:1, 20:1 and 100:1: −0.0496, −0.1207 and −0.2738;
- the fallibilist's EV: 0.45;
- the probability of reaching the (1+√2)²c² threshold: 1.374×10⁻⁵.

The DDB paragraph (§1) is outside this delta. It is unchanged from `final/A6/essay.md` and was added after my v4 audit. Its inferences are valid given DDB's definitions as quoted in `citations_final.md` (D6–D7):
1. KDT with a fixed tie order picks, at each s, an act maximizing E_{P_s}, so it is a recommended strategy.
2. Universal safety therefore yields Weak Value.
3. Value yields universal safety.

## 4. Patch list for v6

**Required:** none.

**Optional** (clarity and consistency). Word count of v6 by `tools/wordcount.py`: 5,853 (limit 6,000). Each patch adds 1 word.

**O1** (§6.2; clarity; +1 word):
- Old: `while ordinary Bayesian evaluation strictly prefers looking (§3). An encroachment criterion that withdraws knowledge whenever these two evaluations change the preference therefore`
- New: `while the latter strictly prefers looking (§3). An encroachment criterion that withdraws knowledge whenever these two evaluations rank the available options differently therefore`
- Reason: the passage introduces the evaluations as "knowledge-conditioned" and "evidence-conditioned", and "ordinary Bayesian" is a third name for the second of them. Evaluations do not "change the preference"; the criterion is triggered when they order the options differently, which matches the quoted "affects your preferences over available options".

**O2** (§4; consistency with Corollary (ii) and with abstract patch P8; +1 word):
- Old: `the only belief-containing state one can condition on in graded models without`
- New: `the only belief-containing state one can condition on in finite graded models without`

No other mismatch was found between v6's formal, numerical or logical statements and verified proofs or code.
