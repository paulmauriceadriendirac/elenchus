# A6 continuation: almost-sure recovery without finite expected cost

22 October 2026. External research note, version 0.2. This extends and reassesses [A6 v0.1](../ambitious-drafts-20261022/A6-recoverable-knowledge-v01.md); it does not replace that file or certify a submission.

**Finding.** Under independent sampling from the two-red, one-black bag and the cofinal transparency assumptions of A6, every fixed finite knowledge level becomes available almost surely along continued sampling. Nevertheless, those assumptions do not guarantee a finite expected time to attain even the second level. An explicit abstract hierarchy separates the two claims.

The probability theory is standard. The proposed philosophical increment is a precise separation between local attainability, almost-sure attainment, and affordable inquiry within the transparency framework. Its originality and the adequacy of its epistemic realization remain open.

## 1. Correction to the previous assessment

The earlier draft and adversarial review correctly refused to call the result a refutation of Carter and Hawthorne. However, their suggestion that the original response needs only selected cases understates the local commitments made in the inspected manuscript.

In §4.1, manuscript page 12, Carter and Hawthorne explicitly consider obtaining a missing higher-order answer through additional draws from the agent's existing position. They also describe a generalization to agents lacking a finite knowledge level. In §4.2, manuscript pages 14–15, the displayed Transparency principle specifies a successful total length for each level, and the ensuing argument applies it to continued inquiry.

That is a genuine place for a local-recovery lemma. It is not merely a stronger question imposed by this project. But it remains essential to distinguish the displayed formula from the authors' intended account of evidence. A natural strengthening of their intended principle could supply sufficiently late witness lengths immediately. The appropriate criticism is that the displayed formula needs an additional bridge for the local application, not that their complete theory has been disproved.

Their footnotes 16 and 18 concern higher-order ignorance at the acquisition of knowledge and its relation to indeterminacy. These are not, by themselves, the claim that every finite all-red history lacks full finite-order knowledge. Thus assumption F in A6 must remain explicit.

## 2. Setup and the stronger theorem

Let p be the true bag-composition proposition. Let H_n(h) mean that level n of knowledge of p is available after finite history h. Availability is distinct from actually forming a belief and from recognizing that the level has been reached.

Retain descent: H_n(h) implies H_j(h) for 1 ≤ j ≤ n. Let T say that for every n there is a positive length k such that every history of length k with at least two-thirds red outcomes satisfies H_n.

For fixed N, define

$$
W_N=\{k\geq1:\ \text{every history }h\text{ of length }k
\text{ with }r(h)/k\geq2/3\text{ satisfies }H_N(h)\}.
$$

The useful condition is that W_N is unbounded for every N. A6's cofinal selection of witness lengths implies this through descent. Its restriction F, that no finite all-red history supplies every finite level, is one sufficient route to that cofinality. F is not necessary.

**Almost-sure recovery proposition.** Suppose W_N is unbounded for every finite N. Conditional on any fixed finite history, suppose subsequent draws are independent, with red probability 2/3. If sampling continues indefinitely, then, with probability one, each fixed finite level H_N is available at arbitrarily late times.

*Proof.* Fix a target N and a present total length m. For any later total length k, put L=k−m. Even if the entire existing history were black, at least ceil(2k/3) red outcomes in the next L draws would make the total history qualify for T.

If X_L has distribution Binomial(L,2/3), the threshold differs from its mean by

$$
\left\lceil\frac{2(m+L)}3\right\rceil-\frac{2L}3
=\frac{2m}3+O(1).
$$

For fixed m, this difference divided by the standard deviation sqrt(2L/9) tends to zero. The central limit theorem therefore gives

$$
\Pr\!\left(X_L\geq\left\lceil2(m+L)/3\right\rceil\right)\longrightarrow\frac12.
$$

Because W_N is unbounded, choose k in W_N sufficiently large that this probability is at least 1/3. This lower bound is uniform over all histories of length m: an all-black past is the worst case.

Repeat this selection recursively, obtaining deterministic total lengths k_1<k_2<... in W_N. At each stage, conditional on the entire past, the probability of a qualifying history at the next selected length is at least 1/3. Independence is required for the fresh draws, not for the success events at the selected lengths.

By successive conditioning, the probability of missing all of the first j selected opportunities is at most (2/3)^j. The same bound applies starting from any selected opportunity. Hence the probability that only finitely many opportunities succeed is zero. At every success H_N holds. Finally intersect the probability-one events over the countably many finite N. ∎

The conclusion is stronger than the earlier existence of an all-red continuation with positive probability. It does not identify a time at which all finite knowledge levels hold simultaneously. Nor does it establish that any attained level persists forever. A hierarchy can reach each finite level repeatedly without ever reaching full finite-order knowledge.

The probability here is the sampling law conditional on the true bag composition. It is not automatically the inquirer's rational credence, a probability conditional on everything the inquirer knows, or something the inquirer knows about future success.

## 3. Almost-sure success can have infinite expected duration

Here is a deliberately minimal hierarchy. It tests what follows from the formal conditions; it is not asserted to implement Carter and Hawthorne's full epistemology.

For a nonempty history of length m with r red outcomes, define

$$
H_1(h)\ \Longleftrightarrow\ r/m\geq1/2,
$$

and, for n ≥ 2,

$$
H_n(h)\ \Longleftrightarrow\ m\geq n\ \text{and}\ r/m\geq2/3.
$$

At the empty history no H_n holds.

Descent holds. T holds at every k ≥ n for n ≥ 2, and at k=1 for n=1. The hierarchy has finite depth at every finite history, so it satisfies F. Thus it satisfies stronger witness availability than the original draft required.

Start from h=RRBB. The agent has H_1 but lacks H_2. Define the evidence score S(h)=3r−2m, initially −2. Each additional red draw adds 1; each black draw subtracts 2. Under the true bag's sampling law these increments have expectation

$$
(2/3)(1)+(1/3)(-2)=0.
$$

Let τ be the first number of additional draws at which the score is nonnegative. Since the initial length is four, the length condition for H_2 is already satisfied. Thus τ is exactly the first attainment time of H_2. The preceding proposition gives Pr(τ<∞)=1.

**Infinite-duration proposition.** E[τ]=∞.

*Proof.* Upward increments are exactly 1, so the first nonnegative score is exactly zero. If E[τ] were finite, bounded-increment optional stopping would give E[S_τ]=S_0=−2. But S_τ=0 almost surely, a contradiction. ∎

This is the familiar infinite-mean first-passage phenomenon for a centered random walk. It is not a newly discovered probability result.

The non-entailment also survives granting the strongest possible ability to stop at the first success. Any almost-surely successful policy using only these draws, with final sample count σ and H_2 at stopping, must have σ≥τ pathwise. Hence E[σ]=∞. With constant cost c>0 per draw and a bounded nonnegative terminal reward V≤B, such a policy has expected net payoff −∞. This valuation is an added decision-theoretic premise, not a consequence of an epistemic norm.

Finite-budget policies are different. A policy may cap its draws and accept a chance of failure; nothing here shows that every such policy has negative value. Nor does the result establish that taking the next draw is impermissible. It excludes a costless inference from almost-sure eventual success to a finite-expected-cost plan that insists on success.

## 4. What has and has not been modeled

The hierarchy is compatible with factivity and ordinary modal closure at each individual history. If its depth at h is d, take worlds 0,...,d+1, with p true at 0,...,d and false at d+1. Each world accesses itself and, except at the last world, its successor. At actual world 0, K^n p holds exactly for 1≤n≤d: the shortest path to a p-false world has length d+1. For d=0, the actual world still satisfies p but does not know it.

This construction shows that the finite-depth profiles do not require an inconsistent static knowledge operator. It does not establish a unified, plausible dynamic epistemology linking the history-indexed models. In particular, the sample-proportion cutoffs are stipulated; the construction has not derived them from a normality, safety, evidence, or learning account. The source paper's assumptions about known observations, transitions, and the prior/bonus knowledge distinction have not all been implemented.

There is also a difference between an objective hitting time measurable with respect to recorded draws and an agent knowing that the epistemic target has been attained. The cost lower bound grants an oracle that stops at first attainment; recognition difficulties cannot repair that bound. But the almost-sure recovery theorem alone does not give an agent an executable stopping criterion.

The defensible result is therefore a separation among the explicitly stated assumptions. A counterexample to the target authors' complete theory would require a model satisfying that theory's further commitments.

## 5. Philosophical position after the stronger result

Brown's critique concerns which inquiries agents actually pursue and whether their aims can justify continued checking. An almost-sure attainment theorem does not establish that someone has, or should adopt, a higher-order aim. The infinite-duration construction instead sharpens a separate resource issue after a target has already been specified. It does not answer Brown's objection.

Carter and Hawthorne already discuss demandingness and risk in §§4.1.1–4.1.2. The phrase “inquiry can be costly” is consequently no contribution over their text. What the construction adds to this working draft is an exact failure of a stronger inference: even assuming eventual success has probability one, a success-insisting policy can have infinite expected sample cost.

Hong's *Normality in Action?* concerns difficulties for using normality-based knowledge to guide decisions, including its combination with K1. The present argument supplies neither a normality model nor a derivation of K1 probabilities. It should not be presented as a response to Hong. His paper remains a necessary comparison if this project later interprets the sampling probabilities as knowledge-conditioned action-guiding probabilities.

The strongest objection to this continuation is straightforward: it applies elementary probability theory to a schematic hierarchy while leaving the interesting epistemic realization unresolved. That objection succeeds against describing this as a completed substantive philosophical breakthrough. The note earns further investigation only if a defensible account of higher-order knowledge can instantiate the separation, or if the exact distinction is doing previously unrecognized work in an existing published argument.

## 6. Numerical verification and its limits

An absorbing-state probability recurrence was evaluated through 10,000 further draws, starting at score −2. At a positive deficit d=−S, a red draw changes the deficit to d−1 with probability 2/3, and a black draw changes it to d+2 with probability 1/3. Mass reaching deficit zero is absorbed. For each cap T, the truncated expectation was computed as sum from t=0 to T−1 of Pr(τ>t).

| Further-draw cap T | Pr(τ ≤ T) | E[min(τ,T)] |
|---:|---:|---:|
| 2 | 0.4444444444 | 2.0000000000 |
| 10 | 0.6444139613 | 5.6494436824 |
| 100 | 0.8871801716 | 20.9601992576 |
| 1,000 | 0.9643180209 | 69.7171218688 |
| 10,000 | 0.9887162240 | 224.0151218172 |

The recurrence agreed with exhaustive weighted enumeration at every horizon from 1 through 10, within 10^−12. An initial exploratory implementation mistakenly retained absorbed mass; the two-draw sanity check exposed it, and the values above use the corrected absorbing recurrence. The calculation illustrates the tail; it does not prove divergence of the expectation. The optional-stopping proof establishes that claim.

No new pipeline code was added. This note was written and checked by the same assistant; it has not received independent review.

## 7. Next decision

Keep A6 as a conditional technical note under development, with a stronger result than v0.1. Do not expand it merely to approach a word limit.

The next substantive task is a dynamic epistemic realization: find a justified higher-order knowledge model in which cofinal transparency holds and success remains expensive, while distinguishing acquisition from recognizable completion. Then test the exact increment against literature on higher-order knowledge, checking, inquiry costs, and stopping. If only the elementary random-walk observation survives, demote this to a lemma or appendix rather than inflate it into an article.

A4 remains separately blocked on admissible causal realization and the unread Ehring source. This continuation does not resolve those questions.

## Sources inspected and attribution limits

- Carter, Sam, and John Hawthorne. 2024. “Dogmatism and Inquiry.” *Mind* 133(531): 651–676. https://doi.org/10.1093/mind/fzad070. Inspected repository author-manuscript extraction: [source](../../ambitious/sources/carter-hawthorne-2024-dogmatism-inquiry.txt), especially manuscript pages 11–17. Page references above refer to that manuscript.
- Brown, Jessica. 2025. “Knowledge, Inquiry and Dogmatism.” *Synthese* 205, article 174. https://doi.org/10.1007/s11229-025-05008-4. Inspected the discussion of higher-order inquiries, demandingness, and transparency, including §3 and note 5.
- Hong, Frank. 2026. “Normality in Action?” *Philosophical Perspectives*, early view, published 11 September. https://doi.org/10.1111/phpe.70003. Inspected the article's K1/normality framing, examples, and conclusion.
- Sousi, Perla, lectures; Leonard Tomczak, notes. 2022. *Advanced Probability*, Cambridge Part III, Michaelmas. Theorem 2.3(4) states bounded-increment optional stopping with finite expected stopping time; the following random-walk example illustrates the importance of integrability. https://math.berkeley.edu/~ltomczak/notes/Mich2022/AdvProb_Notes.pdf.

Targeted searches combining dogmatism, inquiry, higher-order knowledge, hitting times, and infinite expected duration did not establish a prior exact philosophical application. This is not an originality clearance: citation tracing and a broader literature audit remain necessary.

## Provenance

Recovered from branch claude/stoic-davinci-ktysg2 at e0de0a1d6666f2c68c0e89c89792ab02ffa61f1f after the user asked to continue in a new chat. The earlier [provenance notice](../ambitious-review-20261022/PROVENANCE.md) remains in force, including the disclosed external-memory exposure. This is external development, not a resumed clean-origin contest orchestrator. No unrelated personal philosophical material supplies a premise here. The original drafts, Claude's selection, and orchestrator status are preserved.

