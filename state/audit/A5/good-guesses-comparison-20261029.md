# Good Guesses: source check and A5 originality reassessment

29 October 2026.

## Verdict

The source gap is closed for the supplied **July 2021 penultimate author draft** of Kevin Dorst and Matthew Mandelkern's *Good Guesses*. Its argument, belief application and Optionality proof are available and have been inspected. Page numbers below refer to that draft, not the journal pagination. The published article is *Philosophy and Phenomenological Research* 105(3), 581–618 (2022), [DOI 10.1111/phpr.12831](https://doi.org/10.1111/phpr.12831). No claim is made that the two versions are textually identical.

A5's description of the Jamesian formula is accurate. The full paper nevertheless makes the overlap more substantial than a formula comparison alone suggests. It already derives filtered answers by maximizing epistemic utility, connects those answers to belief, and explicitly treats question sensitivity and changes in the partition.

In fact, **its existing model produces exactly the two belief sets displayed in A5's principal three-world example**, with a single fixed parameter. That is an implication calculated here, not a claim that these numerical inputs appear in *Good Guesses*.

This does not invalidate A5's counterexample to the unrestricted reading of Dorst's 2019 holistic argument. It does rule out treating the displayed behavior, filtered-core structure, or a general epistemic-utility derivation of guess-based belief as the new contribution. The defensible increment is the particular unrestricted-belief-state construction, its formal comparison with Dorst's assumptions, and the exact characterization of its optima.

Draft compared: [A5 v6 at 7e3b0926f06b4103b575fbc9fa6c6c9e4a8513f7](https://github.com/paulmauriceadriendirac/elenchus/blob/7e3b0926f06b4103b575fbc9fa6c6c9e4a8513f7/state/drafts/A5/v6.md). This was an in-progress draft; the assessment is pinned to that content.

## What the primary text establishes

For a finite question Q, let I_Q(p) be the proportion of its cells ruled out by p. The Jamesian score assigns J raised to I_Q(p) to a true answer, zero to a false one, with J ≥ 1. Thus

E_Q^J(p) = P(p) J^{I_Q(p)}.

The original notation is Q_p rather than I_Q(p).

| Topic | Location in the supplied draft | Consequence for A5 |
|---|---|---|
| Epistemic-utility foundations and the comparison with Levi | §3.1, pp. 9–12, especially note 13 | Guessing is already given an epistemic decision-theoretic derivation. |
| Truth-directed, question-based answer values; Jamesian formula | pp. 10–15 | A5's formula description is verified. The authors' sense of truth-directedness needs distinguishing from A5's. |
| Fit and Filtering | §3.2, pp. 16–17 | Selecting a probability-filtered answer is established prior work, explicitly building on Holguín. |
| Optionality | pp. 17, 36–37 | Each answer size can be optimal for some J. A5 has not established the corresponding claim for its premium. |
| Belief as entailment by a best guess | §4.1, pp. 21–22 | For a fixed chosen guess and question, this bridge yields all its consequences. |
| Partition effects | pp. 5, 17, 20 note 23; p. 26 note 29 | Question sensitivity and the distinction between harmless and consequential refinements are already recognized. A5's particular invariance theorem remains a separate claim. |

The proof of Filtering is the familiar exchange argument: replacing an included lower-probability cell by an excluded higher-probability one preserves informativity while increasing expected value. A5's core-filtering proof uses the analogous exchange. That structure should be credited, not presented as independently new.

Optionality's appendix orders the cells by probability, establishes a strict ordering of adjacent prefix probability ratios, and uses it to locate intervals of J for which each prefix is optimal. The proof checks. This is stronger than merely observing that some optima happen to be filtered.

## Exact overlap with A5's principal example

Keep the question fixed as the three singleton worlds and set

J = 125/64, so J^{1/3} = 5/4.

A singleton answer has score P(p)·25/16; a two-world answer has score P(p)·5/4; the tautology scores 1.

| Credences | Score of {w1} | Score of {w1,w3} | Unique best guess |
|---|---:|---:|---|
| (0.70, 0.15, 0.15) | 35/32 = 1.09375 | 17/16 = 1.0625 | {w1} |
| (0.75, 0.01, 0.24) | 75/64 = 1.171875 | 99/80 = 1.2375 | {w1,w3} |

All eight propositions were compared in exact rational arithmetic. At the first credence, {w1,w2} ties the displayed two-world runner-up; the best guess itself is unique.

Under the §4.1 entailment bridge, these guesses generate respectively

- {{w1}, {w1,w2}, {w1,w3}, W};
- {{w1,w3}, W}.

These are exactly A5's displayed optimal belief sets. The question, J and evaluation rule are fixed across the comparison. Thus the reversal is already obtainable from the existing model without changing context or the informativity parameter.

This calculation sharpens the prior-art comparison; it is not evidence that Dorst and Mandelkern themselves printed this particular numerical illustration.

## What remains different

**The objects scored differ.** Dorst and Mandelkern score candidate guesses. A5 scores unrestricted sets B of propositions by adding ordinary true/false contributions and a premium when their conjunction is true. A5 then proves that optimization reduces to a core objective:

Phi_C(X) = β C(X) + sum over p containing X of max(T_p C(p) + F_p(1−C(p)), 0).

That objective is not the Jamesian formula in another notation. Its second term depends on the credences of the individual consequences, not only on the number of question cells excluded by X. Calling it informativity is an interpretation; it should not obscure this dependence.

**Truth-directedness differs.** *Good Guesses* requires every true guess to score higher than every false guess (p. 10). A5's condition concerns the marginal effect of adding a proposition to an existing belief state: adding a true proposition must improve accuracy, and adding a false one must worsen it. Simply scoring B by the Jamesian value of its conjunction does not satisfy that strict marginal requirement: adding an already entailed proposition leaves the conjunction unchanged, and adding another error to an already false conjunction still scores zero. Therefore the behavioral overlap does not automatically supply a counterexample satisfying A5's formal premises.

**The belief bridges differ outside the displayed three-world case.** A5 generally retains only the above-threshold consequences of its optimizing core. In its four-world example with credences (0.62, 0.18, 0.10, 0.10), the optimal state includes {w1,w2} and {w1,w3} but omits their conjunction {w1}. No set consisting of all consequences of a single chosen guess has that property. Theorem 3's closure criterion identifies exactly when A5's output is the full consequence set of its own optimizing core, in the stated generic uniform-value setting. It does not show that the Jamesian rule would select that same core.

These differences sustain a narrower formal contribution. They do not establish broad originality merely because the scoring formulas differ. The prior review's objections concerning the refinement conclusion and the rational-permission bridge remain separate issues.

## Recommended replacement for A5's comparison paragraph

Dorst and Mandelkern (2022, §§3–4.1) already derive filtered guesses by maximizing epistemic utility and, following Holguín, connect belief to the consequences of a best guess. Their Jamesian expected answer-value is C(X)J^{I_Q(X)}, where I_Q(X) is the proportion of question cells ruled out and J ≥ 1. Their rule can even reproduce both belief sets in Section 3 with one fixed J: on the singleton question, J = 125/64 selects {w1} at C and {w1,w3} at C'. Neither the reversal nor the filtered-core structure is therefore new.

The contribution of Theorem 3 is narrower. It derives a particular core objective by optimizing a truth-pattern-based score over unrestricted belief states, with strict gains for adding truths and strict losses for adding falsehoods. The resulting beliefs are the above-threshold consequences of the selected core. The single-guess entailment bridge accepts all consequences; this rule can omit the core itself, and part (iii) identifies exactly when deductive closure holds. The positive result is thus an optimizer characterization within the formal setting used to assess Dorst's holistic extension, rather than a first utility-theoretic derivation of guess-based belief. Levi and Leitgeb likewise remain essential predecessors for selecting a strongest accepted proposition and taking its consequences.

## One adjacent comparison

Helena Fang's [“Guessing and Its Limits” (2026)](https://onlinelibrary.wiley.com/doi/full/10.1111/phpr.70101), §§2–3, supplies an additional relevant caution. Its Independent Closure principle concerns combining permissible answers to independent questions; its Filtering Failure result challenges that combination. This is different from A5's failure of conjunction closure within one optimal belief state. A5 should not imply that problems about closure and question-sensitive guessing have previously gone unnoticed. The definition and incompatibility argument were inspected; this note is not a full review of Fang's paper.

## Effect on the assessment

The previously requested primary-source comparison can now be made directly. A5 should retain the 2019 proof criticism and the narrower formal results if their remaining issues are repaired, while reducing the claimed novelty of the positive philosophical picture. *Good Guesses* does not contain A5's record-score theorem or its refinement theorem in the supplied version. It does contain much of the conceptual territory around them.

This addendum resolves the *Good Guesses* access limitation in the earlier assessment. It reports a focused source comparison, not a comprehensive certification of novelty.
