# Referee report

**Manuscript:** “Holistic Accuracy and the Limits of Lockean Derivation”
**Length:** 10 pp. (main text 1–8, appendix 9–10)
**Recommendation:** Minor revision
**Confidence:** 4/5 (I brute-forced the counterexample and re-derived the theorems; I could not check the Dorst quotations or page numbers against the published text.)

**Revision note (v2).** An earlier version of this report flagged footnote 2's “28 / 216” as an error. That was a text-extraction artefact: the rendered PDF reads **2⁸** and **2¹⁶**, and the counts are correct (256 and 65,536). The point has been removed; I re-checked the rendered page.

---

## 1. Summary

Dorst (2019) argues that maximizing expected accuracy yields Lockean thresholds even without Separability. The paper distinguishes two readings of that holistic extension. On the weak reading (mere truth-directedness plus order independence) the argument fails: a *record measure* that adds a premium `β` when the belief state’s core is true makes a proposition believed at credence 0.70 and withheld at 0.75, with values and context fixed (Theorem 1). On the strong reading, the derivation needs restrictions on marginal values: marginal extensionality (ME) plus background-independence (BI) recover Separability on a specified domain (Theorem 2 and its corollary), which turns Dorst’s §4.2 into a dilemma. A separate theorem shows that cross-space refinement invariance (RI) plus conservative increments (CI) is a *sufficient* route to fixed thresholds, and that RI is stronger than fixed-space Lockeanism (Theorem 4). Finally, the record measure’s optima have an exact core-relative Lockean characterization (Theorem 3), and the paper notes that Dorst and Mandelkern (2022) already derive a closely related filtered-guess structure.

The counterexample is simple, robust, and decisive against the unrestricted reading. The diagnosis is precise and, if the textual claim about p. 193 is right, compelling. The paper is well written and appropriately hedged. My main concerns are about (i) a numerical claim in the footnote that I cannot reconstruct, (ii) the incomplete treatment of state-indexed measures, which is the version of the issue that matters for Dorst, (iii) the incremental value of §5, and (iv) the need to say more about why the record premium is a legitimate accuracy measure.

---

## 2. Assessment

**Strengths.**

- The counterexample is correct, and I verified it exhaustively: at `C = (0.70, 0.15, 0.15)` the unique optimum among all 256 belief states is `{1, 12, 13, W}` with expected accuracy 4.30; at `C′ = (0.75, 0.01, 0.24)` it is `{13, W}` with 4.94. The runner-up at `C` is 4.20 (margin `e_1 = 0.10`), and the runner-up at `C′` is 4.75. The four-world closure-failure example is also correct (the unique optimum has core `{w_1}` and believes `{w_1,w_2}`, `{w_1,w_3}`, `{w_1,w_4}`, their unions, and `W`, but not `{w_1}`).
- Theorem 2 is a genuine contribution. The coefficient-matching argument is correct: under ME, comparing `A(B ∪ {p,q})` computed in the two orders yields linear independence of `1`, `[w ∈ p]`, `[w ∈ q]` (for distinct, contingent, non-complementary `p, q`), which forces `J_p` to be background-independent; then BI is exactly additivity of `κ`. The result is clean and the dilemma is real.
- The quantifier-gap diagnosis (p. 4) is precise and well motivated: “for every world where `p` is true there is some increment” is not “there is a single increment for every world”.
- The refinement material (Theorem 4) is a nice independent result, and the paper is unusually careful not to overstate it (sufficient, not necessary; stronger than the fixed-space conclusion).
- The paper is honest about overlap with Dorst and Mandelkern.

**Weaknesses.**

- The state-indexed family version of Theorem 2 — the form Dorst actually uses — is asserted but not proved (3.1).
- The bridge from “unique optimum” to “rationally permitted” rests on Non-vacuity, and the paper should say more clearly that the counterexample does not depend on that choice (3.2).
- §5 is long relative to its novelty, given the acknowledged overlap with Dorst and Mandelkern (3.3).
- The paper does not say enough about why the record premium should count as *accuracy* rather than as a separate epistemic good (3.4).

---

## 3. Major comments

### 3.1 The family version of Theorem 2 is asserted, not proved

The final paragraph of §4 (p. 5) is important: Dorst’s measures are indexed to the current state `B₀`, so Theorem 2 (which concerns a single measure) does not directly apply. The paper says: “for such a family, ME at each member’s own state, together with BI read across the family (the increments `T_p^{B₀}` and `F_p^{B₀}` of `A_{B₀}` at `B₀` do not depend on `B₀`), yields fixed thresholds through Proposition 4 without collapsing the family into one separable measure.” That is the version of the claim that matters dialectically, and it is asserted in two sentences. Please state and prove it as a proposition. In particular: (i) what exactly is the “ME at each member’s own state” condition (the increments of `A_{B₀}` when evaluated at `B₀`, or at every `B`?); (ii) does the argument go through when the family is not generated by a single measure; (iii) does the resulting threshold agree with the separable one in the special case where the family is constant? Without this, a defender can say that Dorst’s state-indexed framework is untouched by Theorem 2, which would blunt the dilemma.

### 3.2 Non-vacuity: say explicitly that the result does not depend on it

The counterexample needs a bridge from “unique optimum” to “rationally permitted”, and the paper supplies the weakest one (Non-vacuity). That is fine, but the paper should say plainly that the result is robust across the plausible bridges:

- If Maximize Expected Accuracy is read as necessary *and sufficient* (all and only optima permitted), the counterexample is immediate and Non-vacuity is unnecessary.
- If it is read as necessary only, Non-vacuity is the weakest additional premise that makes a unique optimum permitted.
- The only escape is to deny that any state is permitted at the two credences, or to impose a further restriction that excludes the record measure.

A short paragraph in §2 or §7 making this explicit would pre-empt the most obvious objection. Relatedly, say that the counterexample does not depend on tie-breaking: at both credences the optimum is unique, and Theorem 1 shows that in the relevant range all optima agree on the verdict.

### 3.3 §5: trim or reposition

The core-relative Lockean characterization (Theorem 3) is correct and the Φ formulation is elegant. But the paper itself says that “neither the reversal nor the filtered-core structure is new” (p. 6), and that this is “an instantiation of their model, not their printed numerical example” (p. 6). Given that, §5 is doing less work than its length suggests. Options: (i) compress to about a page and move the details (the proof, the four-world example, the premium-comparative statics) to an appendix; (ii) reposition §5 as “what the holist gets instead”, making the philosophical moral — the trade-off between acquiring truths and protecting the joint truth of what one believes, and the fact that “calling both aims accuracy does not fix their relative weight” (p. 6) — the focus rather than the characterization. I would prefer (ii), because the moral is the interesting part and it is currently buried.

### 3.4 Why is the premium a component of accuracy?

The paper’s defense in §7 is that the premium is alethic, that it respects strict truth-directedness, and that the objector who insists accuracy is local is assuming ME — which, with BI, yields separability and hence §4.2’s dilemma. That is a fair dialectical position. But a referee may still press: why is the truth of the *core* a component of accuracy, rather than a separate epistemic good (coherence, unification, a “worldview”)? The paper says “a body of belief can be valuable as a whole in this way, which is the holist’s thought” (p. 3) and “the dispute is about the value of an error-free body of belief, which is my claim” (p. 8). That is honest, but thin. Consider adding:

- a positive characterization of the holist picture the premium is meant to capture (e.g., the value of a *unified* or *non-question-begging* body of belief, or the idea that a state’s accuracy should reward the joint truth of what it commits you to);
- a test case where the premium’s verdict is independently plausible, beyond the exam analogy;
- an explicit statement of what evidence would tell against the premium.

None of this is required for the formal result, but it would strengthen the paper’s claim to be diagnosing a genuine gap rather than constructing an admissible-but-unmotivated score.

### 3.5 The textual basis of the diagnosis

The diagnosis in §4 turns on two textual claims: that Dorst’s p. 193 passage “names one number `T_p^{B₀}` as ‘the value’ of adding a true belief in `p`” and that the proof of Proposition 5 “obtains them by setting `T_p` equal to `T_p^{B⁻}` for a state `B⁻` (p. 207)”. I could not verify these against the published text. Since the paper’s central critical claim is that the derivation presupposes ME, it would be worth quoting the exact sentences (or reproducing the relevant proof step) in the main text, not just citing pages. If Dorst’s proof is more careful than the paper suggests — for instance, if he takes expectations over the two values or explicitly notes the background dependence — the diagnosis would need adjusting. A short verbatim quotation would settle the matter for the reader.

---

## 4. Minor comments

1. **Abstract (p. 1):** ~230 words. It is accurate but dense; consider cutting the middle sentences about refinement invariance (which is the least central part) and ending on the diagnosis.
2. **§2, p. 3:** “Its `T_p` and `F_p` are values of the measure in a context, not functions of the credences.” — “in a context” is doing a lot of work; define what a context includes (values, question, partition?) and whether the credence function is part of it. This matters for the “Fixed context” reply in §3.
3. **§3, p. 3:** the notation `1`, `12`, `13` is standard in this literature but hard to parse; a small table of propositions would help.
4. **§3, p. 4:** “the cores 12 and `{w_3}` are symmetric” — say “by symmetry of `w_2` and `w_3`”, since the argument for `{w_3}` is the mirror of `{w_2}`.
5. **§4, p. 5:** “one side of the resulting identity is affine in `[w ∈ p]`, the other in `[w ∈ q]`” — the appendix does the linear-independence argument; a forward reference would help the main text.
6. **§5, p. 6:** Theorem 3’s “iff its core maximizes Φ” — as stated this is correct, but it is worth a footnote that when the intersection of the positive-`e` supersets of `X` is larger than `X`, the state’s actual core is the larger set and both maximize Φ. A reader may otherwise think the statement is inconsistent.
7. **§6, p. 7:** “splitting a world of credence zero into `k` worlds multiplies the separable part of Φ for every core excluding it by `2^{k−1}`” — correct, but the counting (“each pair of coarse supersets … becomes `2^k` refined supersets”) is terse; a footnote with the bijection would help.
8. **§6, p. 7:** the interval claim “for fixed `β` the interval of Theorem 1 shrinks exponentially in `k`” follows from the effective premium `β/2^{k−1}` and the length formula; say so explicitly.
9. **§6, p. 7:** the mean-over-the-algebra repair is described as leaving the Φ-value “exactly unchanged” for cores excluding the split world. I verified this, including the positive-credence splits of `w_2` at both `C` and `C′` (k = 2, 4, 8): both verdicts survive. It would be worth a sentence explaining *why* the positive-credence case also works, since the “credence-zero” argument does not obviously cover it.
10. **§7, p. 8:** “in the four-world case it accrues on `{w_1}`, which is not believed” — clarify that the premium accrues when the *core* is true, and that the core here is `{w_1}` while `{w_1} ∉ B*`.
11. **References:** check the page numbers for Dorst (2019) (183, 185, 190–196, 207) against the published *Mind* version, since the diagnosis depends on them. The Dorst and Mandelkern reference note (“Section numbers cited follow the July 2021 penultimate author draft”) is good practice; consider doing the same for Dorst.
12. **Appendix, p. 9:** the proof of Theorem 1 is compressed but correct; the step `Φ(1) − Φ(13) = ½(Φ(1) − Φ(W)) + ½ e_1` is a nice trick worth annotating.

---

## 5. Verification notes (what I checked, and how)

**Counterexample (exact enumeration over all 256 belief states).**

- `C = (0.70, 0.15, 0.15)`: unique optimum `{1, 12, 13, W}`, EA = 4.30. Runner-up `{12, 13, W}`, EA = 4.20. ✓
- `C′ = (0.75, 0.01, 0.24)`: unique optimum `{13, W}`, EA = 4.94. Runner-up `{1, 12, 13, W}`, EA = 4.75. `12` has credence 0.76 > τ = 2/3 and is omitted. ✓
- Four worlds, `C = (0.62, 0.18, 0.10, 0.10)`: unique optimum has core `{w_1}` and believes `12, 13, 14, 123, 124, 134, W` but not `1`; it is upward closed but not closed under conjunction. ✓

**Theorem 1.** I checked the algebra: `Φ(1) − Φ(W) = c(2D + β) + T + 2F − β`; the comparisons with `13`, `{w_2}`, `{w_2,w_3}`, `∅`; `c_1 − c_0 = T/(2D + β)`; `c_1 − τ = βT/(D(2D + β))`; `1 − c_1 = 2T/(2D + β)`; and the length claim `βT/(D(2D+β))` for `β ≤ D`. All correct.

**Theorem 2.** I checked the coefficient-matching proof: the linear independence of `1, [w∈p], [w∈q]` for distinct, contingent, non-complementary `p, q` holds (including the case `p ∪ q = W`, `p ∩ q ≠ ∅`), and the induction over `B` delivers `J_p^B = J_p`. The BI/additivity equivalence is correct. The theorem’s restriction to states without complementary pairs is genuinely needed (as footnote 3 says).

**Theorem 4.** I checked the proof: truth-directedness eliminates states containing `∅` and states lacking `W`; the four survivors are `{W}`, `{W,p}`, `{W,p̄}`, `{W,p,p̄}`; the CI argument gives the contradiction `c < 1/2` and `c > 1/2` for `{W,p,p̄}`; the threshold `τ_p = f/(t+f) > 1/2` follows. Correct.

**Numerical claims.**

- Theorem 3 / Dorst–Mandelkern: `J = 125/64`, question with three cells; scores 35/32 vs 17/16 at `C`, 75/64 vs 99/80 at `C′`. ✓
- Refined `C′` (split the 1% world into 0.005 + 0.005): `Φ(1) = 7.25`, `Φ(13) = 6.91`; `1` is believed. ✓
- Mean-measure repair (`b = 3/8`): splitting `w_2` into 2, 4, 8 equiprobable worlds at both `C` and `C′` leaves both verdicts in place (enumerated over cores; for k = 8 the effective premium is large but the separable term grows too, and the verdicts are preserved). ✓
- Footnote 4 (bonus of 1/2 for deductively closed states): with `T = 1`, `F = −2`, `{w_1}` is believed at `(0.575, 0.2, 0.225)` and not at `(0.65, 0, 0.35)`. ✓
- Two-world threshold for the record measure: `(β − F)/(D + β) = 5/6`. ✓

**Not verified.** The Dorst quotations and page numbers; the “larger spaces” verification method (`max Φ` over cores), though it follows from Theorem 3. Footnote 2's counts are correct: 2⁸ = 256 states on three worlds, 2¹⁶ = 65,536 on four.
