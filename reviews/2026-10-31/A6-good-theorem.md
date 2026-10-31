# Referee report

**Manuscript:** “When Acting on Knowledge Makes Free Evidence Harmful: Good’s Theorem in Normality Models”
**Length:** 11 pp. (main text 1–9, appendix 9–11)
**Recommendation:** Major revision
**Confidence:** 4/5 (I re-derived and independently checked the numerical and decision-theoretic content; I did not have the author’s code, and I could not check every page reference against the published sources.)

---

## 1. Summary

The paper asks whether knowledge-based decision theory (KDT) — maximize expected utility with probabilities conditioned on one’s ken, `Pr(· | K_E(x))` — preserves Good’s theorem (free evidence never lowers expected utility) when knowledge is modelled by Goodman and Salow’s normality framework. The main results are:

1. **Theorem 1** (p. 4): in finite, statist, comparable, K-normality models, a question is safe at `x` (non-negative value in every decision problem) iff there is no *relative defeat* at `x` for it; and every question is safe iff the ken is *gapped* (every state in the ken is sufficiently more normal than every state outside it).
2. **Theorem 2** (pp. 4–5): the necessity direction extends from K-normality to any factive state that “leaves open what rational belief leaves open” (`B(F) ⊆ M_F(s)`), and a gapped state containing `x` contains `C(x)`.
3. **Corollary** (p. 5): in a graded model, the only such state that makes all the `p_v`-questions safe is the whole of `E`.
4. **§3** (pp. 3–4): in Goodman and Salow’s two-scale model of Bjorn, a free second weighing has negative value at ten-to-one odds (`≈ −0.05`), twenty-to-one (`≈ −0.12`), hundred-to-one (`≈ −0.27`).
5. **§5** (pp. 5–7): of three expected-utility developments of Salow’s Conditional Knowledge Dominance, conditioning on the options’ differing (CEU) and on the evidence’s changing one’s choice (VER) fail; conditioning answer by answer (ANS) is safe for free questions but, by Proposition 5, would pay to check what one knows, contrary to the principle it develops.

The paper is technically careful, unusually candid about scope, and the central negative result is philosophically interesting. It is, however, framed in a way that both oversells (the generality of the “if and only if” characterization) and undersells (the diagnosis of *why* the failure arises) what it has.

---

## 2. Assessment

**Strengths.**

- The decision-theoretic core is correct. Lemmas 1–3 and the proof of Theorem 1(a) work; Lemma 2 is a correct deployment of Geanakoplos’s value-of-information result to non-partitional “kens”, and the laminar/nestedness argument (A.1) is sound.
- The Bjorn computations are accurate. I recomputed the model independently (two-error Gaussian representation, `μ ~ N(0, 1/2)`, `d ~ N(0, 2)`, `δ = 2μ² + d²/2`) and reproduced the probabilities and the decision values to the stated precision (see §5 below).
- The diagnosis in §6.4 is, in my view, the paper’s most valuable contribution: the failure of Good’s theorem is due neither to non-partitional evidence nor to a violation of KK, but to the fact that the post-answer ken is not the present ken conditioned on the answer. The dogmatist structure (“I know the bet wins; evidence might stop me relying on that; so I avoid it”) is exactly right.
- The negative results on CEU and VER are correct, and the examples are convincing (I checked both to the stated three decimal places).
- The paper is candid that the general decision-theoretic equivalence is due to Dorst et al. (2021), and that the normality characterization is the increment. That honesty is rare and welcome.

**Weaknesses.**

- The paper is in an awkward position: its headline equivalence is close to a known result (safety ⟺ Total Trust), as the paper itself concedes on pp. 1–2. The genuine contributions — the normality-theoretic boundary (relative defeat/gappedness), Theorem 2, the graded corollary, and the three-rule comparison — are buried under the theorem presentation.
- The “suitable questions” idealization (questions `p_v = {u ∈ E : not u ≫ v}`) does real work in the necessity direction, and the abstract’s “every question is safe if and only if knowledge is gapped” is stronger-sounding than it is.
- §6.3 contains a hedge that bears directly on the headline claim: in the relativized model G&S themselves suggest, knowledge may not be sensitive to future observations, and the author says “I have not computed the bet there” (p. 9). Since the paper’s selling point is that the failure occurs in G&S’s *own* model, this gap needs closing.
- The three conditional rules are the author’s own constructions rather than proposals in the literature, and the reader is not given a principled reason to think the list is the relevant one.

---

## 3. Major comments

### 3.1 Reframe around the diagnosis, not the equivalence

The paper concedes (pp. 1–2) that universal safety is equivalent to Dorst et al.’s Total Trust and that their Theorem 4.1 characterizes Total Trust for any finite frame. It also concedes that its own Theorem 1(a) is, in effect, that characterization translated into normality vocabulary. That is fine — but it should change the paper’s self-presentation. As written, the abstract and §1 present Theorem 1 as the headline, and then a reader who knows Dorst et al. will conclude that the headline is known. The paper’s actual contribution is the *diagnosis*: which normality structures make knowledge-conditioned EU violate Good’s theorem (Theorem 1(b), the corollary), and what the failure consists in (defeat of knowledge, not non-partitionality). Recommend: lead with the Bjorn case and the gapped/graded characterization, and present Theorem 1(a) explicitly as a corollary of the Dorst et al. framework (or, if the independent Geanakoplos route is preferred, say why it is worth having both).

Relatedly, the comparison on pp. 1–2 needs care at the tie-breaking step. The paper says “KDT with the fixed tie order is a recommended strategy”. If the expert’s state-indexed probabilities tie between acts, the set of recommended strategies is larger than the one KDT selects, and Total Trust/Value quantifies over all of them. The reduction “universal safety ⟹ Weak Value” is therefore not immediate as stated; please spell out the convention (e.g., that Weak Value quantifies over strategies that are *weakly* recommended, or that the agent’s probabilities and the expert’s are assumed to have no ties on the relevant sets). This is a framing issue, not a threat to Theorem 1, but it should be fixed.

### 3.2 The “suitable questions” idealization

Theorem 1(b) and Theorem 2’s necessity direction quantify over questions `p_v` defined directly from the normality relation. These are probes, not inquiries an agent could pose; their cells are not defined by observable variables or by any natural experimental setup. The paper says “if it is available”, but the abstract’s “every question is safe if and only if knowledge is gapped” does not carry that qualification. Consequences:

- The characterization should be stated as: *within the class of questions generated by the normality structure*, safety of all such questions ⟺ gappedness.
- The substantive negative result does not need this: in Bjorn, the question (a second weighing) is natural and the failure occurs. The paper should say so explicitly — it partly does in §3(iii), but the abstract and §1 do not.
- The obvious next question, which a referee will ask: is there a natural restriction on questions (e.g., questions whose cells are definable by the values of observable variables, as in Bjorn) under which knowledge-conditioned EU is safe more widely? At minimum, flag this as open; better, give a sufficient condition. Right now the reader is left suspecting that the negative characterization is an artefact of the question class, even though the Bjorn case shows it is not.

### 3.3 The relativization hedge in §6.3 is a gap in the headline claim

On p. 9 the paper notes that, on the probabilistic grounding, normality may be relative to a question; that relativizing to “how much does Bjorn weigh” yields a model like Goldstein and Hawthorne’s, “in which current knowledge is not sensitive to future observations”; that “a weight bet may make that question salient”; and that “I have not computed the bet there.” This is a serious hedge: if the salient question in the Bjorn scenario is the weight question, the failure may vanish, and the paper’s central claim — that in G&S’s own model free evidence is harmful — would be conditional on a modelling choice the authors of the framework might reject. Since the case is the paper’s empirical anchor, please either (i) compute the bet in the relativized model and report the result, or (ii) give an argument that the weight question is not the salient one in the betting scenario, or (iii) restrict the headline claim to the statist/probabilistic model as specified. A referee cannot be expected to accept “I have not computed the bet” for the paper’s central example.

The same section also contains the Margins-completions concession (§6.1, p. 8) and the “statism is the exception rather than the rule” concession (§6.3, p. 8). These are individually honest, but they should be consolidated into one “scope and robustness” section, and the abstract should reflect the resulting qualification.

### 3.4 The three conditional rules need a principled derivation and a word on exhaustiveness

CEU, VER and ANS (pp. 5–6) are the author’s constructions. The paper motivates each in a sentence, but a reader will want to know why these are *the* candidates and whether a fourth natural candidate escapes the trilemma. Suggested improvements:

- Derive the three from distinct readings of “evaluate the options on the hypothesis that they differ”: the difference event (`D = {u_ℓ ≠ u_a}`), the verdict event (`D_b = {α = b}`), and the answer event (cells of `Π`). Say explicitly that these are the three natural “hypothesis” variables in the problem.
- Say what a fourth candidate would look like — e.g., conditioning on the proposition that *the evidence is misleading about the comparison*, or a smooth/weighted version of CEU — and whether the negative results would extend. This would pre-empt the objection that the trilemma is an artefact of three hand-picked rules.
- Make the interpretive claim about ANS precise. Proposition 5 shows that, given relative defeat, ANS prefers paying `κ > 0` for a question whose answer the agent already knows; since `κ` can be chosen below `L` but positive, ANS violates Conditional Knowledge Dominance. Say this in one sentence in §5.3, and connect it to the numbers (0.019 at 10:1; 1.23 at 100:1).

### 3.5 The empty-question anomaly deserves an explicit paragraph

On p. 8 the paper notes that, at abnormal situations, the empty question “can even have positive value”. A reader will ask how a question that conveys no information can have positive value, and the answer — that `V_x` integrates over `s ∈ K_E(x)`, and the policy at `s` uses `K_E(s)`, which can be strictly narrower than `K_E(x)` — is a consequence of the non-partitional ken. This is worth a paragraph in §2, because it bears on whether `V_x` is the right explication of “the value of answering `Π` at `x`”. The paper uses the anomaly only diagnostically (“a cousin of the unmarked-clock case”, p. 8), so this is a clarity issue rather than a soundness issue, but it is exactly the kind of thing that makes a referee suspect the formalism is measuring the wrong quantity. Address it head-on, and explain why the anomaly does not infect the main results (which concern relative defeat, not the empty question).

### 3.6 Missing robustness: how sensitive are the numbers to `c`, and what does “harmful” mean?

The paper reports the magnitudes and gives one sensitivity check (`t = 0.95`, `c ≈ 2.45`, pp. 3–4). Good. But it would help to say plainly that the *sign* is the result and the magnitudes are model-dependent, and to give a short table of values across `c`. I computed the following (10:1 and 100:1, same model):

| `c` | 10:1 value | 100:1 value |
|---|---|---|
| 1.60 | −0.105 | −0.344 |
| 1.80 | −0.072 | −0.308 |
| 1.96 | −0.050 | −0.274 |
| 2.20 | −0.025 | −0.217 |
| 2.45 | −0.010 | −0.153 |
| 2.60 | −0.005 | −0.117 |

The sign is stable, but the ten-to-one value varies by a factor of twenty across the plausible range of `c`, and it is very small at the top end. A sceptical reader will want to see this, and the paper’s claim that “ten-to-one suffices” (p. 8) is easier to accept with the table than without it. (The stability is expected: the decline event is a boundary band of the ken, so `−V` falls as `c` grows, but never reaches zero in the range.)

---

## 4. Minor comments

1. **Abstract (p. 1):** ~250 words, dense, and it leads with the characterization rather than the result. Consider 150 words: “In Goodman and Salow’s normality framework, knowledge-conditioned expected utility violates Good’s theorem exactly when knowledge is not ‘gapped’; in their own model of repeated weighing a free second weighing has negative value at ordinary odds. Of three expected-utility repairs of Salow’s conditional principle, two fail and the third contradicts it on costly inquiry.”
2. **§1, p. 2:** the long Dorst et al. comparison interrupts the dialectic. Consider making it a subsection (“1.1 Relation to Dorst et al.”) after the thesis, or compressing it to a footnote.
3. **§2, p. 2:** “statist” appears in the abstract before “statism” is defined. Define it in the abstract parenthetically, or use “evidence-independent (statist)” in §2 only.
4. **Notation:** a table of symbols (`E`, `B(E)`, `K_E(x)`, `K_E^D(x)`, `V_x`, `α_Π`, CEU/VER/ANS, `c`, `δ`) would materially improve readability.
5. **§3, p. 3:** `B(E) = {δ < c²}` (strict), while the text says `{δ ≤ c²}`. The boundary is measure zero, so nothing turns on it, but use one convention consistently (also in A.5).
6. **§3, p. 3:** “the readings may differ by up to `2c` for all he believes” — under the ken, `|r − r′| ≤ √2 c`. The `2c` bound is loose and may puzzle a reader who checks it; either justify it as a bound on `|r − w| + |w − r′|` (which it is) or use `√2 c`.
7. **§3, p. 3–4:** the two “loss” probabilities (0.417 and 0.95) measure different events — loss of the weight-interval belief versus loss of the old ken belief. The sentence “Preservation fails at every nonzero difference up to `√2c`” should say which belief is given up, otherwise the 0.417 figure looks inconsistent with it.
8. **§5.1, p. 5:** CEU’s `D = {s : u_ℓ(s) ≠ u_a(s)}` can be empty; state what CEU says then (presumably “look” vacuously, or undefined). 
9. **§5.2, p. 6:** “`N` gives `ζ` positive current mean” — spell out the condition (`N·P(s_0) > 1`).
10. **§5.3, p. 7:** “ANS pays up to 0.019 … 1.23” — give the parameter values that generate these (the choice of `s_0`, `q`, and the resulting `κ` bound), so the figures can be checked.
11. **§6.2, p. 8:** “positive rescaling of utilities preserves choices and the sign of information value” — true, but note that the *magnitudes* scale, so the ten-to-one figure is not a stakes-free measure; one sentence.
12. **Appendix, p. 10:** the enumeration claim (“64,004 situation–question pairs; 3,306 with relative defeat”) cannot be checked from the text. Provide a repository or a precise description (which structures, which priors and utilities, how questions are generated).
13. **References, p. 11:** check the page range for Salow (2025) against the published version, since pages 23–38 are cited repeatedly. Same for Goodman and Salow (2023, 104, 107, 121, 127–130, 136, 138 n. 47) and BRN (2025, §5 n. 18).
14. **A.5, p. 10:** “the post-answer ken of a state `s` is `|μ| ≤ max(c/√2, |μ_s|)`” — a one-line derivation would help (it follows from `B(E′) ∪ {v ⪰ s}`).

---

## 5. Verification notes (what I checked, and how)

I re-derived the decision-theoretic results analytically and recomputed the numerical claims independently.

**Analytic checks.**

- Lemma 1: correct (the bet has conditional expectation 1; at `s_0` the post-answer ken contains an excluded state with positive probability; the maximum payoff in the ken is 1).
- Lemma 2 / A.1: correct. The induction on laminar families works, including the step where sub-kens are shown to be subsets of their maximal containers by transitivity.
- Lemma 3 / A.2: correct (reflexivity, transitivity including the `B(F)` case, nestedness via comparability).
- Theorem 1(a): correct. Post-answer kens in distinct cells are disjoint, hence laminar; within a cell they are nested by Lemma 3; absence of relative defeat puts them inside the ken.
- Theorem 1(b): correct, including A.3(b). The key step — if `s ∈ K_E(x) ∩ c` and `v ∈ c ∖ K_E(x)`, then `v ∉ K_{E∩c}(s)` because `s ≫ v` rules out `v ∈ B(E∩c)` and `v ⪰ s` would give `v ≫ v` — is sound.
- Lemma 4 and Theorem 2: correct. Note that Theorem 2 itself does not need factivity — non-gappedness alone gives `m ∈ M_E(x)` and `v ∈ E ∖ M_E(x)` with `not m ≫ v`. Factivity enters only in the corollary, through “contains `C(x)`”. The abstract’s “factive state” is therefore slightly stronger than necessary; a harmless point, but worth tidying.
- Corollary (i) / A.4: correct, including the collapse step.
- Proposition 4: correct, via Lemma 2 applied within each cell to the conditional ken `K_{E∩c}(x) = K^c_E(x)`.
- Proposition 5 / A.7: correct in structure; the construction of `κ` is sound.

**Numerical checks (paper 1, §3).** With `c = 1.96`:

| Quantity | Paper | Recomputed |
|---|---|---|
| Unconditional loss of weight-interval belief | 0.417 | 0.4169 |
| Loss conditional on present ken | 0.356 | 0.3557 |
| BRN narrow event (“loss with consistent discovery”) | 0.37 | 0.3669 |
| `P(0 < |d| ≤ √2 c)` | 0.95 | 0.9500 |
| Decline threshold at 10:1 | 1.12c | 1.120c |
| Value at 10:1 | −0.05 | −0.0496 |
| Value at 20:1 | −0.12 | −0.1207 |
| Value at 100:1 | −0.27 | −0.2737 |
| `t = 0.95` (`c = 2.4477`), 10:1 | −0.01 | −0.0098 |
| `t = 0.95`, 100:1 | −0.15 | −0.1540 |

The 10:1 decline threshold is exact: solving `Pr(|w − r| ≤ c | |μ| ≤ c/√2) = 10/11` gives `|d| = 1.120c`. All figures match.

**Examples in §5.2.**

- Theorem 3’s illustration (pp. 6): I confirmed the ken `{a, b}`, current expectation 1.2 for the third act, looking policy expectation 0.5, and CEU margin 0.7.
- VER example (p. 7): ranks 0, 0.2, 0.5, 1.15, 1.3; prior (0.67, 0.01, 0.30, 0.01, 0.01); I confirmed the ken `{a, s_1, s_2}`, the decline hypothesis ken `{s_1, s_2, v_2}`, `β_1`’s conditional value 0.028, and the VER margin 0.008.
- The CEU example with no relative defeat (p. 7): I confirmed `V = 0.05`, the conditional ken `{x, b}`, and that both VER and CEU prefer acting now.

**Not verified.** The 64,004-pair enumeration (appendix, p. 10); the equivalence with Dorst et al. (no access to the published text); the page references to Salow (2025) and BRN (2025).
