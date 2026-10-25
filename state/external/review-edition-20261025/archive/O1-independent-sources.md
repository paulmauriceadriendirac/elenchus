# Independent Sources and the Correlations We Know

**Abstract.** A theory can preserve everything an agent knows about each independent source while adding knowledge about how their errors are correlated. I argue that this distinction exposes a cost of K-normality, one of Goodman and Salow's proposed completions of the normality framework. On finite products of normality orders, K-normality preserves precisely the knowledge supplied by its single-source applications. Its additional knowledge comes from excluding combinations of possibilities those applications leave open. I characterize the exclusion and give a conservative repair: take the product of the single-source accessibility sets. This preserves every single-source verdict, satisfies the normality framework, and retains positive introspection. On the same structures, KM-normality already factorizes into single-source I-normality. The resulting comparison separates two disputes: whether knowledge has margins for error, and whether independent sources license additional correlational knowledge. The argument for separating them does not require treating epistemic independence as a universal principle.

## 1. Two ways for sources to be independent

A scale and a thermometer report your weight and temperature. The thermometer has badly malfunctioned. The scale is working ordinarily. A natural constraint on a theory of knowledge says that the thermometer's failure should not destroy what the scale tells you about your weight. A second constraint says that the combination of these instruments should not generate knowledge of an unexplained relation between their errors. These constraints differ. Preserving knowledge about each instrument leaves open whether the theory adds knowledge about the pair.

Goodman and Salow use the first constraint to motivate a multidimensional account of normality (2023, 117–119). Their framework determines knowledge from relations of comparative normality among situations compatible with one's evidence. They argue that a single ranking can make ignorance spread from a malfunctioning instrument to an independent working instrument. Allowing normality to vary along distinct dimensions avoids that problem. Two of their proposed completions, K-normality and KM-normality, then deliver knowledge from a working instrument despite failure elsewhere.

My claim is that their successful treatment of this first constraint leaves a second question unsettled. **K-normality preserves its single-source knowledge but adds correlational knowledge that an independent-source interpretation need not license.** The distinction matters because a criticism framed simply as a failure to preserve independent knowledge would miss what the theory actually gets right.

The central example is already present in Goodman and Salow's figure 4. I do not offer its accessibility pattern as a new countermodel to their definitions. I identify the extra conditional knowledge represented by that pattern, explain its general source, and show how to remove it without sacrificing any single-source verdict or the principle that knowing entails knowing that one knows. The repair also changes the comparison between K-normality and KM-normality. The question whether knowledge permits sharp boundaries can be asked independently of the question whether sources must share a single global reason for remaining epistemically possible.

Product constructions are not new to normality epistemology. Carter and Goldstein (2021, §3.1) formulate an intersective extension of single-source accessibility, then argue against making it unrestricted because of their treatment of justification and the preface. My proposal is deliberately local: a product is appropriate where the modeled sources carry no further joint constraint. The increment is a characterization of the difference between two ways of extending the *same* K-normality judgments, together with a proof that the product extension remains inside Goodman and Salow's framework. It is not a new general theory of epistemic independence.

## 2. The normality framework

Work within a finite evidential cell $E$. Every situation in the cell presents the same evidence, and every situation treats exactly $E$ as evidentially possible. This is the transparency assumption. Write $R(w)$ for the situations compatible with the agent's knowledge at $w$. A proposition is known just when it holds throughout $R(w)$.

Following Goodman and Salow (2023, 92–93), let $u\succeq v$ mean that $u$ is at least as normal as $v$, and let $u\gg v$ mean that it is sufficiently more normal. The first relation is reflexive and transitive. The second is irreflexive, implies the first, and is preserved by chaining with the first on either side. Thus $a\succeq b\gg c\succeq d$ implies $a\gg d$.

The framework requires that actuality remain epistemically possible; that knowledge exclude evidentially impossible situations; that $w\gg v$ exclude $v$ at $w$; that situations not sufficiently outranked by any evidential possibility remain possible; and that any situation at least as normal as an epistemic possibility also remain possible. These are, respectively, Factivity, Evidential Knowledge, Inductive Knowledge, Inductive Limits, and Convexity.

Two sets make the completions easy to state:

$$
B=\{v\in E:\text{there is no }u\in E\text{ with }u\gg v\},
\qquad U(w)=\{v\in E:v\succeq w\}.
$$

$B$ is the set of possibilities protected by Inductive Limits; $U(w)$ contains actuality and everything at least as normal. Both are upward closed. K-normality is

$$R_K(w)=B\cup U(w).$$

It is the smallest accessibility set satisfying Factivity, Inductive Limits, and Convexity. Smaller accessibility sets mean more knowledge, so Goodman and Salow describe this as a default toward knowledge (2023, 110).

The other completions relevant here are

$$R_I(w)=\{v\in E:w\not\gg v\},$$

and

$$
R_{KM}(w)=B\cup\{v\in E:\exists u\in E\ (v\succeq u,\ w\succeq u,\ w\not\gg u)\}.
$$

I-normality excludes only what Inductive Knowledge requires. KM-normality allows less ignorance than that in general, but preserves a margin for error: a situation less normal than actuality, though not sufficiently less normal, remains possible. On a total normality order, KM-normality and I-normality coincide (2023, 110–111).

Now suppose $E=X_1\times\cdots\times X_m$, where each finite $X_i$ has a total preorder $\succeq_i$ and a compatible sufficient-normality relation $\gg_i$. As in Goodman and Salow's multidimensional model,

$$
w\succeq v\quad\text{iff}\quad w_i\succeq_i v_i\text{ for every }i,
$$

$$
w\gg v\quad\text{iff}\quad w\succeq v\text{ and }w_i\gg_i v_i\text{ for some }i.
$$

Write $B_i$ and $U_i(w_i)$ for the corresponding single-source sets. Then $B=\prod_i B_i$ and $U(w)=\prod_i U_i(w_i)$. Finiteness ensures that the $B_i$ are nonempty. No probabilistic independence assumption has been made. A product of possibilities says which combinations exist; an epistemic product says which combinations the agent can exclude. These are distinct claims.

## 3. The extra knowledge

In each of two dimensions, use three states: ordinary, odd, and bizarre, numbered $0,1,2$. Ordinary is more normal than odd, which is more normal than bizarre. Only ordinary is sufficiently more normal than bizarre. Then $B_1=B_2=\{0,1\}$.

At $w=(0,2)$, the first instrument is ordinary and the second bizarre. K-normality yields

$$R_K(0,2)=\{(0,0),(0,1),(1,0),(1,1),(0,2)\}.$$

The agent cannot exclude an odd first instrument: $(1,0)$ and $(1,1)$ remain possible. She cannot exclude a bizarre second instrument: that is how things actually are. But she can exclude their combination, $(1,2)$. Consequently she knows the material conditional:

> If the second instrument is bizarre, the first is ordinary.

She does not know that the first instrument is ordinary. The criticism is not that failure elsewhere improves her unconditional knowledge of the working instrument. It is that she acquires a dependency between the two instruments' states that neither local assessment supplies.

The source of the dependency is visible in the definition. An accessible world must satisfy one of two global conditions: every coordinate belongs to its $B_i$, or every coordinate is at least as normal as actuality. A possibility may not use the first justification in one coordinate and the second in another. In the excluded world $(1,2)$, the first coordinate uses the ordinary range of tolerated error, while the second uses actuality. K-normality refuses this mixture.

This is an exact description of the model, not a claim that the agent represents a hidden common cause. Nevertheless, the mathematical operation has the same correlating effect as a shared binary choice: all coordinates take the first option together, or all take the second together. Independent local choices would produce additional mixed possibilities.

**Proposition 1.** On the stated product structures, K-normality has exactly its single-source projections:

$$\operatorname{proj}_i R_K(w)=B_i\cup U_i(w_i).$$

Hence it agrees with the product relation

$$R_{\Pi K}(w)=\prod_i\bigl(B_i\cup U_i(w_i)\bigr)$$

about every proposition concerning only one coordinate.

*Proof.* Projection commutes with union, and projection of each nonempty product is its corresponding factor. A proposition concerning coordinate $i$ alone holds throughout an accessibility set exactly when it holds throughout its $i$th projection. ∎

This establishes that the disputed knowledge is entirely additional joint knowledge. It also gives a precise sense in which the repair is conservative. It changes no answer to a single-instrument question, at any actual state.

**Proposition 2.** $R_K(w)$ fails to be a product exactly when there are distinct coordinates $d,e$ such that $w_d\notin B_d$ and $w_e$ is strictly more normal than some member of $B_e$.

*Proof.* If such coordinates exist, choose $b_e\in B_e$ strictly below $w_e$. The world obtained from $w$ by replacing its $e$th coordinate with $b_e$ belongs to $R_{\Pi K}(w)$. It does not belong to $B$, because its $d$th coordinate is outside $B_d$, or to $U(w)$, because its $e$th coordinate is below $w_e$.

Conversely, suppose no such pair exists. If $w\in B$, upward closure gives $U(w)\subseteq B$, so $R_K(w)=B$, a product. Otherwise choose $d$ with $w_d\notin B_d$. Totality implies $B_d\subseteq U_d(w_d)$. For every $e\ne d$, the absence of the stated pair gives $B_e\subseteq U_e(w_e)$: no member of $B_e$ lies strictly below $w_e$. Thus $B\subseteq U(w)$, and $R_K(w)=U(w)$, again a product. ∎

The distinctive case is therefore a failure beyond the locally protected range combined with unusually good performance elsewhere. This identifies where a defender must explain the extra correlations. Merely observing that K-normality permits sharp epistemic boundaries does not explain why a boundary in one dimension should constrain combinations with another.

## 4. Why recombination is an additional constraint

A set $R\subseteq E$ is rectangular when $R=\prod_i\operatorname{proj}_iR$. Equivalently, any combination of coordinate values separately represented in $R$ is represented in $R$. Rectangularity is a condition on possibilities, not a requirement to assign independent probabilities.

It is stronger than the anti-skeptical independence constraint that motivated the multidimensional model. Proposition 1 shows that K-normality already satisfies an exact form of marginal preservation. There is no valid inference from that preservation alone to rectangularity. A theorist may consistently allow the instruments' individual states to remain uncertain while claiming knowledge of a relation between them.

The issue is what licenses that relation. Suppose the instruments have separate mechanisms, calibration histories, and subject matters. The evidence contains their readings but no comparison between them. The model's normality assumptions are entirely coordinatewise. There is no common manufacturing fault, no known constraint on the number of failures, and no further dimension recording total error. Under that description, the exclusion of $(1,2)$ requires an explanation. The global disjunction in K-normality generates it without representing any additional relation in the setup.

An externalist can reply that knowledge need not be supported by evidence the subject can articulate. That is correct and does not answer the objection. The demand is not for an accessible reason. It is for an epistemically relevant feature of the modeled situation that distinguishes the excluded combination from its individually admissible components. Independent reliability can explain why some local errors are excluded. It does not automatically explain why two locally admissible errors cannot coexist.

A related diagnostic concerns disclosure. Suppose the thermometer is independently inspected and the agent learns its actual bizarre state, with no new information about the scale. On the resulting cell $X_1\times\{2\}$, K-normality leaves both $(0,2)$ and $(1,2)$ open. The formerly known material conditional does not yield knowledge that the scale is ordinary; the theory withdraws that conditional instead.

Knowledge can be defeated by new information, so this is not a formal contradiction. The revealing feature is what the defeat concerns. Discovering a thermometer malfunction eliminates a supposed constraint on the *scale's* error, despite the absence of any modeled connection. A defender may accept such defeat, but it is an additional commitment. The initial argument that instrument failures should not spread ignorance did not settle it.

The product proposal rejects this extra commitment in cases without a joint source of information. This is a defeasible modeling constraint, not a universal claim about all collections of instruments. If the agent knows that at most one device is defective, a nonrectangular accessibility set is exactly right. If a large collection of beliefs is known to contain an error, a model must represent that joint constraint. The objection concerns deriving a correlation from the global completion alone after the case has been specified as having only local constraints.

## 5. A conservative repair that retains KK

The product relation $R_{\Pi K}$ is the smallest rectangle containing $R_K$. Every rectangle containing a set must contain all combinations of its projections, and those combinations themselves form a rectangle. Rectangularization is a familiar operation; its philosophical interest here is what it preserves.

**Proposition 3.** On the finite product structures above, $R_{\Pi K}$ satisfies all five principles of the normality framework. It is transitive. It is also the smallest rectangular accessibility set satisfying Factivity, Inductive Limits, and Convexity.

*Proof.* Factivity and Evidential Knowledge follow immediately. Every member of $B$ is included, and the set is upward closed, establishing Inductive Limits and Convexity. If $w\gg v$, some $i$ satisfies $w_i\gg_i v_i$. Then $v_i\notin B_i$, since $w_i$ sufficiently outranks it, and $v_i\notin U_i(w_i)$, since the converse comparison would violate irreflexivity and chaining. Thus $v$ is excluded.

For transitivity, first observe that the single-source relation $B_i\cup U_i(x)$ is transitive. If $y\in B_i$, then $U_i(y)\subseteq B_i$. If instead $y\succeq_i x$, then $U_i(y)\subseteq U_i(x)$. In either case, $B_i\cup U_i(y)\subseteq B_i\cup U_i(x)$. Products preserve this inclusion coordinatewise. Finally, Factivity and Convexity require $U(w)$, and Inductive Limits requires $B$. A rectangle containing both must contain the product of their coordinatewise unions. ∎

Given the transparent evidential cell, transitivity validates positive introspection, or KK: if one knows a proposition, one knows that one knows it. The repair therefore does not purchase independence by abandoning the commitment that distinguishes K-normality in the debate about higher-order knowledge.

There is also a characterization using the global normality relation. Let $w\wedge b$ be a greatest lower bound under $\succeq$, obtained by taking the less normal value in each coordinate. Then

$$R_{\Pi K}(w)=\{v\in E:\exists b\in B\ (v\succeq w\wedge b)\}.$$

To see this, each factor $B_i$ is an upward-closed subset of a finite total preorder. The points above the less normal of $w_i$ and a suitably chosen $b_i\in B_i$ are exactly $B_i\cup U_i(w_i)$. Choosing the $b_i$ independently gives a member of $B$. The converse follows coordinatewise. Thus the repair can be expressed through meets and the original global relations; it does not need a new substantive measure of normality.

On a single total preorder, this expression reduces to $B\cup U(w)$. If $w\in B$, all the relevant lower bounds remain in $B$. If $w\notin B$, every member of $B$ is above $w$, so their meets with $w$ are equivalent to $w$. The product proposal therefore agrees with K-normality in the comparable case as well as on every single-source projection.

This construction is restricted to the specified products. Arbitrary partial orders need not have meets, and an arbitrary meet construction need not satisfy Inductive Knowledge. Those are substantive limits, not details to be hidden behind a general label.

## 6. Where margins enter

The other comparison is especially simple.

**Proposition 4.** On these product structures,

$$R_{KM}(w)=\prod_i I_i(w_i),\qquad I_i(w_i)=\{v_i:w_i\not\gg_i v_i\}.$$

*Proof.* Suppose no coordinate of $v$ is sufficiently less normal than the corresponding coordinate of $w$. Let $u_i$ be the less normal of $w_i,v_i$. Then both $w$ and $v$ are at least as normal as $u$. No coordinate witnesses $w\gg u$, so $v$ satisfies the second disjunct in KM-normality.

Conversely, suppose $w_i\gg_i v_i$ for some $i$. Replacing $v_i$ with $w_i$ in $v$ produces a world sufficiently more normal than $v$, so $v\notin B$. For any common lower bound $u$ of $w,v$, chaining gives $w_i\gg_i u_i$. Since $w\succeq u$, this entails $w\gg u$, excluding the second disjunct as well. ∎

KM-normality consequently combines single-source I-normality, whereas the repair combines single-source K-normality. Both are rectangular. They disagree about local margins.

In the three-state example, take actuality $(1,1)$. The product K proposal leaves only the four worlds whose coordinates are ordinary or odd. KM-normality leaves all nine worlds possible, because an odd state is not sufficiently more normal than a bizarre one. The former permits sharp knowledge; the latter preserves a margin. Their disagreement survives after all additional correlations have been removed.

Goodman and Salow suggest a defeasible connection between Comparability and Margins, partly through the relative simplicity of the available completions (2023, 111). The present results do not refute their assessment of every theoretical virtue. They show that the choice of completion on the multidimensional branch is wider than the global K-versus-KM comparison suggests. A theorist can preserve the K-style local judgments and KK while requiring independent recombination. Conversely, KM's complicated global formula has a simple product form on this branch.

Hawthorne's (2025) criticism of Goodman and Salow's earlier KK model raises separate difficulties about sharp knowledge and testimony. The present repair is not an answer to those difficulties. It preserves every single-coordinate knowledge judgment of K-normality, including any independently objectionable sharp judgment. Its purpose is to remove additional cross-coordinate exclusions in the specified product cases. A theorist can accept that repair and still reject the local theory on Hawthorne's grounds.

The resulting lesson is more limited, and more useful, than a general verdict for or against margins. Two theorists who agree about orthogonal normality and agree that no extra joint knowledge is licensed can still disagree about margins. Their remaining disagreement is the familiar single-source disagreement, repeated across coordinates. Incomparability does not force them to settle it by accepting unexplained cross-source correlations.

## 7. The explanatory burden

The strongest defense of global K-normality appeals to its default toward knowledge. Why require an explanation of an excluded combination when the framework already permits excluding it? Perhaps the smallest accessibility set is independently preferable.

That is a substantive position. It treats the absence of a prohibition as sufficient for additional knowledge. The product proposal instead makes the default conditional on preserving independent recombination. Proposition 3 shows that it is equally maximal in knowledge once that constraint is accepted. Neither default establishes its own constraints. The dispute must be decided by the instrument cases and by the account of what normality is supposed to explain.

The repair has a cost too. Rectangularity prevents knowledge of some joint propositions that can be plausible even when each coordinate remains open. Aggregate improbability, shared calibration procedures, and higher-order information about the collection can all matter. A theorist who wants those phenomena must represent them explicitly or relax rectangularity. That is preferable to treating every correlation generated by a formal completion as equally well motivated.

What has been established is a precise choice. Global K-normality and product K-normality agree on all single-source knowledge and both retain KK. They differ over whether locally admissible possibilities may be recombined. In the cases at issue, the global theory's extra knowledge comes from coordinating the two disjuncts in its accessibility definition across every source at once. A defense of that coordination is still owed. Margins for error do not supply it, and preserving knowledge from a working instrument does not supply it either.

## References

Carter, Sam, and Simon Goldstein. 2021. “The Normality of Error.” *Philosophical Studies* 178: 2509–2533. https://doi.org/10.1007/s11098-020-01560-6. Author manuscript: https://discovery.ucl.ac.uk/10197131/1/TheNormalityOfError.pdf.

Goodman, Jeremy, and Bernhard Salow. 2023. “Epistemology Normalized.” *The Philosophical Review* 132: 89–145. https://doi.org/10.1215/00318108-10123787.

Hawthorne, John. 2025. “Normality and KK.” *Philosophical Studies* 182: 3071–3084. https://doi.org/10.1007/s11098-025-02382-0.

