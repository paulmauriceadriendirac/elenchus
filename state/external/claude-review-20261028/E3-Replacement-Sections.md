# Proposed replacement sections for E3

28 October 2026. Editorial companion to *Independent assessment of Claude's new reviews*. These sections replace the corresponding claims in E3 v4; they are not a complete new manuscript. The source and access qualifications are part of the accompanying assessment.

## Replacement abstract

**Abstract.** Flattening identifies supposing a proposition and then a strengthening of it with supposing the strengthening directly. A pair of counterfactual stories appears to challenge that identification: the stories agree on unnested attendance counterfactuals while differing on a nested one. I show what this comparison establishes under a selective interpretation of the antecedents and where that interpretation requires further support. Reciprocity yields a clearer challenge with no disjunction in the nested sentence, but the argument retains a disjunctive selection premise. An explicit contextual reset can reproduce the proposed contrast while preserving Flattening for an underlying sequence conditional. Causal models likewise distinguish different ways of realizing the antecedents rather than automatically supporting the contrast. The resulting lesson is methodological: these cases can identify a disagreement about the interpretation of nested supposition, but cannot settle the conditional's logic without independently constraining that interpretation.

## Replacement for the central triad argument

Let $A$ and $B$ say that Ann and Bob attended, and let $X=A\lor B$. Consider three claims:

(P1) $X>B$: if at least one of them had attended, Bob would have attended.

(P2) $B>(A>B)$: if Bob had attended, then if Ann had attended, Bob would have attended.

(P3) $\neg(A>B)$: it is false that Bob would have attended if Ann had.

These claims are jointly inconsistent in C2.F. Since $B>X$ is a C2 theorem, Reciprocity gives $B>\varphi\leftrightarrow X>\varphi$ under (P1). Substituting $A>B$ for $\varphi$, (P2) entails $X>(A>B)$. Since $A$ entails $X$, the rule form of Flattening yields $A>B$, contradicting (P3). With $A>\neg B$ in place of (P3), C2.F similarly entails $B>(A>\neg B)$.

The advantage of this formulation is limited but real. The nested sentence itself has an atomic outer antecedent, so assessing it does not first require resolving a disjunction within that sentence. The argument as a whole still depends on the selective reading of (P1). Under Simplification of Disjunctive Antecedents, (P1) already entails $A>B$ and contradicts (P3). Consequently, someone who reads (P1) distributively rejects the setup before reaching the issue about nesting. The argument addresses a reading on which Bob's attendance is selected from the possibilities in $X$. It does not establish that every ordinary reading must make this selection.

On that reading, the Reunion/Avoidance contrast concerns (P2). In the first story, bringing about Ann's attendance from the Bob-attended scenario is proposed to preserve Bob's attendance. In the second, the proposed realization of Ann's antecedent changes her earlier registration and the guest list, causing Bob to stay home. The same words need not receive the same contextual enrichment in the two stories, however. A contrast in judgments would therefore establish a phenomenon to explain, not by itself exclude a contextual explanation.

## Replacement for the appeal to causal models

The causal realization of an antecedent must be distinguished from its truth conditions. For the Avoidance story, suppose attendance requires prior registration, registration puts Ann on the posted list, and Bob consults that list. A suitable model has $L=D$, $A=D$, and $B=S(1-L)$, where $D$ is Ann's registration decision and $S$ the sitter's availability. Initially $D=S=0$.

If Bob's attendance is brought about by changing $S$ to one, and Ann's by changing $D$ to one, the nested supposition removes Bob. If Ann's attendance is instead set directly, the list stays unchanged and Bob remains. If Bob's attendance was itself directly clamped, it survives even the change to the list. The proposed judgment thus requires a particular upstream realization policy. The equations alone do not choose it.

Nor is arbitrary interventionism independent support for the original Flattening counterinstance. Under persistent surgical interventions, with $A\lor B$ evaluated over interventions on $A$, on $B$, and on both, $(A\lor B)>(A>B)$ and $A>B$ agree for distinct Boolean settings $A,B$. The branch intervening on $A$ determines the nontrivial truth value; the other branches hold $B$ fixed as true. This observation does not settle how ordinary disjunctive antecedents are interpreted. It prevents an appeal to causal modeling from substituting for a defense of that interpretation.

## Replacement for the contextual-reply passage

A local reset of the base world reproduces the proposed data. For each world, form a sequence listing its accessible worlds in their order from that world. Within each sequence, evaluate an ordinary conditional by selecting the first suitable tail. This conditional is flat. After entering a tail headed by $v$, however, an additional operator can reset evaluation to the beginning of $v$'s own sequence before the next conditional is evaluated.

With a reset before each conditional operation, this architecture reproduces the original world-relative order model. The proof is by induction: the reset supplies the current world's order; selection finds the same antecedent world; and the recursively interpreted consequent has the same value there. This includes the case contrast and the Contraction control. The rival therefore supplies precise predictions for the existing examples.

An unrestricted reset is not yet an independently supported account of English. It also means that the validity of Flattening for the underlying conditional does not transfer to the compound construction containing resets. To distinguish the rival analyses, evidence must constrain when resetting is licensed and what fixes its value. Adding more examples whose interpretation remains equally adjustable will not do so. The present cases identify that explanatory task without completing it.

## Replacement for the conclusion

The models establish a formal contrast, and Reciprocity expresses its implication for C2.F clearly. The linguistic challenge remains conditional on a selective first-degree premise and a scenario-relative interpretation of the nested sentence. Neither the matched control nor the causal analogy independently establishes those assumptions. Local resetting supplies a precise rival that fits the proposed judgments.

This leaves the source paper's formal results intact and narrows the objection to its natural-language motivation. The current comparison does not establish a refutation of Flattening. Its useful result is an explicit separation of the selection premise, the realization policy, and the contextual mechanism whose independent justification would be needed to settle this particular challenge.
