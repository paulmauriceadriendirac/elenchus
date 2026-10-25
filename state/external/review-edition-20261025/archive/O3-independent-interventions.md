# Independent Interventions and the Limits of Flattening

**Abstract.** Flattening identifies a nested conditional with its inner conditional when the inner antecedent entails the outer one. Dorr and Mandelkern establish its role in sequence semantics and argue that it has considerable intuitive appeal. I isolate a conflict between Flattening and a different constraint: changing one of two independent controls preserves the other control's state, including at a counterfactually selected scenario. No ordered-selection model of a complete two-control system can satisfy both constraints. The proof does not depend on a numerical similarity metric or on which single-control change realizes a disjunctive antecedent. An explicit four-world model preserves Contraction and validates Flattening for compatible conjunctive settings, while falsifying it for a disjunctive outer antecedent. The philosophical issue is whether counterfactual selection inherits the selected scenario's independent settings or retains the earlier route of supposition. The result gives a precise limit on applying sequence semantics to ordinary intervention-sensitive counterfactuals, without proposing a complete semantics of the indicative conditional.

## 1. What the outer supposition can do

Two independent switches are off. If switch A had been on, switch B would have remained off. Now suppose that at least one switch had been on, with B the easier switch to change. In the resulting scenario B is on. If A had been on in that scenario as well, there would have been no reason for B to turn off. A supposition that leaves B alone preserves its setting, but the setting it preserves differs between the original and selected scenarios.

This elementary pattern creates a problem for Flattening:

$$P>(P\wedge Q>R)\quad\leftrightarrow\quad(P\wedge Q)>R.$$

Here $>$ is the conditional. The equivalent rule form says that whenever $Q$ entails $P$,

$$P>(Q>R)\quad\leftrightarrow\quad Q>R.\qquad\text{(F)}$$

Dorr and Mandelkern (2026) prove that adding Flattening to Stalnaker's logic C2 gives the logic of ordinal sequence semantics. Their natural-language discussion takes it seriously as a principle for both indicative and subjunctive conditionals. They already explain why ordinary similarity metrics can invalidate it. Their question is whether those formal failures correspond to convincing linguistic judgments (2026, §4.1).

My argument isolates a constraint more specific than general similarity: the retention of an independent control's setting when another control is changed. **Flattening is incompatible with applying that constraint at both the original world and worlds reached by counterfactual supposition.** The conflict appears in a four-world system, survives either ordering of the two single-control changes, and leaves Contraction intact.

The mathematical incompatibility is short. Its value is diagnostic. It identifies something that a defender of Flattening must reject in a familiar class of counterfactual interpretations, and explains why many simple tests with conjunctive antecedents will miss the problem. I do not claim to discover the failure of Flattening on general order frames, to replace Dorr and Mandelkern's characterization of flat frames, or to infer a semantics of natural language from an unargued distance function.

## 2. Ordered selection and the known frame condition

An order frame associates each world $w$ with an accessible set $R(w)$ containing $w$, ordered with $w$ first. For a proposition $X$, let $f(w,X)$ be the first accessible $X$-world, when there is one. A conditional with antecedent $X$ and consequent $Y$ is true at $w$ when the selected world belongs to $Y$; when no antecedent world is accessible, the conditional is vacuously true. Dorr and Mandelkern give the corresponding soundness and completeness results for C2 (2026, §2.1).

For nonempty, accessible antecedents, the selection condition behind Flattening is

$$f(f(w,Y),X)=f(w,X)\qquad(X\subseteq Y).\qquad\text{(1)}$$

The left side selects an $X$-world after first moving to a $Y$-world. The right side selects an $X$-world directly. Equality makes all consequents agree. If the selected worlds differ, some proposition distinguishes them. With the appropriate convention for vacuous cases, this is a selection-function reformulation of Dorr and Mandelkern's flatness characterization (2026, Theorem 4.3). They also state its metric counterpart in §4.1. No novelty is claimed for (1).

The condition imposes a restriction on what a selected world may select next. Entailment of the outer antecedent does not merely make that antecedent true at the final world. It requires the intermediate choice to make no difference to the final choice. That is a stronger demand, and independent controls reveal the difference.

## 3. The independent-control square

Consider four worlds $00,01,10,11$. The first digit records whether control A is on; the second records whether B is on. Both settings can occur together. Write $A=\{10,11\}$ and $B=\{01,11\}$. All four worlds are accessible from each other.

The locality constraint is that setting one control to on preserves the other control's current value:

$$f(ab,A)=1b,\qquad f(ab,B)=a1.\qquad\text{(L)}$$

This expresses a specified counterfactual interpretation, not a definition of independence for every purpose. The controls have separate mechanisms and no interlock. Interventions on either can be made without altering the other. The constraint is imposed at each of the four scenarios, including scenarios reached by supposition.

**Proposition 1.** No order frame on this square can satisfy both (L) and Flattening for all Boolean antecedents and consequents.

*Proof.* At $00$, locality gives $f(00,A)=10$ and $f(00,B)=01$. The first world satisfying $A\vee B$ must be the earlier of these two first worlds. It cannot be $11$, since $11$ comes after $10$ among the $A$-worlds and after $01$ among the $B$-worlds.

If $f(00,A\vee B)=01$, then locality gives

$$f(f(00,A\vee B),A)=f(01,A)=11\ne10=f(00,A).$$

This violates (1), since $A\subseteq A\vee B$. If the selected world is $10$, the symmetric calculation with inner antecedent $B$ gives $11\ne01$. ∎

The proof assumes no numerical distances. It does not require deciding which control is easier to change. Either choice produces a violation, though the displayed instance changes with the choice. It uses only ordered selection, the independent-control square, and the locality constraints.

An explicit frame removes any uncertainty about consistency of the remaining assumptions. In each row below, the worlds are listed from first to last:

| Starting world | Selection order |
|---|---|
| $00$ | $00,01,10,11$ |
| $01$ | $01,00,11,10$ |
| $10$ | $10,11,00,01$ |
| $11$ | $11,10,01,00$ |

Every row is centered, and every local setting in (L) is preserved. At $00$ we obtain

$$A>B\text{ is false},\qquad(A\vee B)>(A>B)\text{ is true}.$$

Thus the nested-to-direct direction fails. Replacing the final consequent with $\neg B$ gives

$$A>\neg B\text{ is true},\qquad(A\vee B)>(A>\neg B)\text{ is false},$$

so the direct-to-nested direction fails too. These are rule-form instances of Flattening because $A$ entails $A\vee B$.

The example is not driven by a failure of the modal principles discussed among Dorr and Mandelkern's reservations. All four worlds are mutually accessible, so the necessity operator defined from the conditional has the universal accessibility relation. In particular it is transitive and connected. The difficulty is specifically about iterated selection. Dorr and Mandelkern already establish broader limits on characterizing Flattening through modal principles; this square supplies a concrete intervention-sensitive instance of that distinction.

## 4. The reading that makes the case work

Imagine two indicator circuits tested at a fixed instant. Each switch directly controls its own indicator. There is no common power constraint, and switching one circuit cannot alter the other. Both switches are off. B is readily adjusted, whereas A is secured behind a cover, making a B-only change the natural realization of a supposition that at least one was on.

Compare these sentences, with every occurrence concerning the same instant:

(D) If A had been on, B would have been on.

(N) If at least one of A and B had been on, then if A had been on, B would have been on.

Under the local reading just described, (D) is false and (N) is true. In the direct supposition A changes and B stays off. In the outer scenario of (N), B is on. The inner supposition changes A while preserving B's selected setting. The switches' independence is doing the explanatory work.

Some readers will hear the inner antecedent differently: if it had been A *rather than B* that was on. On that exclusive reading, B is off and (N) is false. That is a genuine alternative interpretation, not an objection to be dismissed as confusion. The point is to isolate an inclusive reading on which A's being on does not itself require B's being off.

Adding “too” can help listeners access that reading, but the formal argument does not rely on treating the particle as truth-conditionally idle. The interpretation is specified by (L), and the four-world model supplies it for the bare antecedent $A$. An explicitly exclusive antecedent, $A\wedge\neg B$, selects $10$ from both $00$ and $01$, so it provides a control on which this divergence disappears. The inclusive and exclusive antecedents make different demands.

There is also a control on causal structure. If the circuits are interlocked so that turning A on necessarily turns B off, (L) is false at $01$. The inner A-supposition then selects $10$, and the displayed positive nested conditional is false. The divergence is therefore not forced by the mere appearance of a nested conditional or a disjunctive antecedent. It depends on whether the unmentioned setting is preserved.

This argument does not establish that all speakers select the local reading by default. It establishes a coherent and independently motivated reading under which the proposed validity fails. A claim that Flattening belongs to the logic of counterfactuals needs a reason to exclude that reading, or an account of why its apparent truth conditions arise outside the semantic conditional.

## 5. Contraction and context change

Dorr and Mandelkern discuss apparent counterexamples involving changed tense and anaphoric interpretation. They note that similar effects can undermine the much less controversial principle of Contraction:

$$P>(P>R)\quad\leftrightarrow\quad P>R.$$

Their caution is well taken. If repeated antecedents silently introduce different events or individuals, an apparent failure need not concern a fixed interpretation of the logical schema (2026, 20–21).

The square gives a different pattern. It validates Contraction for every proposition. Once $f(w,X)$ has been selected, it is an $X$-world and comes first in its own ordering. Selecting $X$ there returns that same world. Hence

$$f(f(w,X),X)=f(w,X).$$

This is true in the very frame in which Flattening fails. There is no second occasion, new referent, or change in the truth conditions of $A$ and $B$. Repeating the same setting leaves it alone; replacing a disjunctive requirement by one of its disjuncts can add a setting without retracting the other one.

A defender can nevertheless posit a contextual shift in the ordering used for the inner conditional. The formal countermodel holds one family of world-relative orders fixed; the linguistic objection says that natural sentences do not realize that interpretation. This is a substantive semantic-pragmatic proposal. It cannot be refuted just by exhibiting a frame.

The explanatory burden is specific, however. The proposal must explain why ordinary local reasoning about independent controls is available under a single supposition but loses its authority at an embedded scenario, or why it must be represented as a change of context rather than evaluation at a different world. It should also preserve the straightforward Contraction controls. The fact that some superficially similar examples turn on anaphora does not establish that this one does.

Dorr and Mandelkern's analogy with Cautious Monotonicity and Cautious Transitivity raises a related point (2026, 23). Those principles concern comparisons within the starting world's order and are already valid in ordinary C2 frames. Flattening compares selection *from* the selected world with selection from the starting world. The square satisfies the former principles while failing the latter. The cautious restriction on antecedents therefore does not by itself make these two kinds of constraint equivalent.

## 6. Why conjunctive tests can miss the problem

Suppose a world is a finite tuple of independent control settings. For a consistent partial assignment $a$, let $T_a(w)$ overwrite precisely the coordinates named in $a$. If assignment $b$ extends $a$, then

$$T_b(T_a(w))=T_b(w).\qquad\text{(2)}$$

Every coordinate set by $a$ is set to the same value by $b$, and all other coordinates are handled identically on both routes.

**Proposition 2.** If conditional selection for conjunctions of control settings is given by these overwrite maps, then Flattening holds whenever its inner assignment extends its outer assignment.

*Proof.* The two routes select the same world by (2), so they agree on every consequent. ∎

This is an elementary composition property, not a new theorem about general causal models. Structural-equation approaches formalize interventions by replacing selected equations; Halpern (2000, §2) gives the relevant framework. A disjunction of settings, however, does not specify a unique intervention. The standard intervention notation does not on its own determine how to realize “A or B.”

The present argument respects that limitation. It does not attribute a disjunctive-intervention semantics to structural-equation models. Instead it asks what happens when ordinary ordered selection is used to extend local setting operations to Boolean antecedents. Proposition 1 proves that the extension cannot preserve unrestricted Flattening.

The distinction explains why a large class of plausible tests will pass. If an outer supposition specifies a setting and the inner supposition repeats it while adding another, the inner operation already incorporates the first. The outer step is redundant. But when the outer antecedent is disjunctive, its selected realization may settle a control that the inner antecedent does not mention. The selected setting can then survive the inner change, although it would not have arisen under direct selection.

This is not a claim that every example Dorr and Mandelkern discuss is literally a system of independent controls. It is an explanation of a structural source of the apparent redundancy they emphasize, and a reason that such redundancy cannot be generalized without testing disjunctive realization. Logical entailment between antecedents is insufficient to guarantee that the second operation repeats all the *particular settings* chosen by the first.

## 7. What a sequence theorist can retain

Sequence semantics has a principled answer to the objection. A conditional selects a tail of a sequence. Further suppositions continue along that tail. If $X\subseteq Y$, the first $X$-point in the original sequence is also the first $X$-point after the first $Y$-point. Flattening follows because the route of search is retained.

On such a semantics, indices that agree about the current controls can disagree about further conditionals. The theory need not accept that a selected $01$-index obeys the same local selection constraints as a $01$-scenario considered on its own. Dorr and Mandelkern explicitly discuss the distinction between categorical facts and the richer indices used to evaluate conditionals (2026, §3).

The no-go result does not expose an inconsistency in that position. It identifies its price for the proposed interpretation. Suppose the original sequence reaches $01$ before $10$, and reaches $10$ before $11$. At the selected $01$-index, the next A-world is $10$. Turning A on is therefore represented as removing B's on-setting. The route inherited from $00$ defeats locality at the selected index.

A defender can accept that consequence for some forms of supposition. What requires argument is applying it to counterfactual reasoning explicitly governed by two independent controls. The claim that the controls are independent is then insufficient to guarantee the preservation of the other control's setting under embedded supposition. A full defense must explain why that familiar inferential use of independence is mistaken or pragmatically mediated.

This is narrower than assuming that all counterfactual truths supervene on categorical facts. The argument requires only the local constraints for the specified system. It leaves open indeterminacy, context sensitivity, and richer indices elsewhere. It also does not infer counterfactual independence from the bare absence of a causal arrow in a chancy system. The controls and their responses are specified deterministically, and the interventions are stipulated to leave the other circuit unchanged.

Nor does the result establish that Flattening is valid for indicatives. Ordinary conditioning and information-state restriction cannot simply be offered as a semantics of C2 plus Flattening: unrestricted iterated restriction would also suggest Import-Export, whose addition to C2 creates the familiar collapse problem discussed by Dorr and Mandelkern. The present argument supplies no solution to that problem and claims none.

## 8. A boundary for a proposed logic

The formal choice is exact. Ordered selection can preserve independent local interventions at the original and selected scenarios, or it can satisfy Flattening for every Boolean antecedent, but it cannot do both on the complete two-control square. This is compatible with Contraction and with Flattening on compatible conjunctive settings.

The philosophical conclusion depends on the standing of local intervention-sensitive readings. If they are legitimate counterfactual readings, Flattening is too strong as a general validity for counterfactuals. A theorist can retain it for a restricted kind of supposition, or give an account on which the relevant readings arise through contextual operations outside the conditional's invariant semantics. What is unavailable is a cost-free extension from the apparent redundancy of conjunctive tests to all entailing antecedents.

The selected scenario can contribute something that its antecedent does not explicitly require: a particular way of making that antecedent true. When a later supposition leaves that contribution alone, its effects can persist. Flattening removes precisely that possibility. Independent controls make visible why ordinary counterfactual reasoning sometimes needs it.

## References

Dorr, Cian, and Matthew Mandelkern. 2026. “Sequence and Consequence.” *Philosophical Logic* 1. https://doi.org/10.16995/phil-log.27646. Section and page references are to the authors' arXiv version: https://arxiv.org/abs/2411.16994v2.

Halpern, Joseph Y. 2000. “Axiomatizing Causal Reasoning.” *Journal of Artificial Intelligence Research* 12: 317–337. https://doi.org/10.1613/jair.648.

