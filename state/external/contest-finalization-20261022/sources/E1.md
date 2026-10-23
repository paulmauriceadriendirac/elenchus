# Gettier Knowledge across Independent Sources: K-Normality without Comparability

**Abstract.** Goodman and Salow argue that independent sources, such as a scale and a thermometer, tell against COMPARABILITY, and they model such sources with multi-dimensional normality. They also answer the worry that disjunctive characterizations of knowledge breed Gettier cases. What matters, they argue, is CONVEXITY, which their K- and KM-normality satisfy. I show that this answer fails for K-normality on their own multi-dimensional model. Under COMPARABILITY the two disjuncts of K-normality are nested, so its disjunctive form does no work. On products of independent respects it does work. It credits knowledge of a disjunction of a justified false belief about one source and an unknown truth about another, and this knowledge is not cliff-edge knowledge. At the single-malfunction situations of their model, K-normality agrees with justified-true-belief normality, while KM-normality becomes non-disjunctive. The principle that bans such knowledge is equivalent to a combination principle. Added to K-normality's knowledge default, it yields a completion that still validates KK.

## 1. Introduction

Goodman and Salow (2023) offer a general framework for inductive knowledge. What a person knows is fixed by her evidence and by two relations among the situations her evidence leaves open: being at least as normal, and being sufficiently more normal. The framework's five principles constrain knowledge without determining it. Goodman and Salow compare three completions: I-NORMALITY, from Goldstein and Hawthorne (2022); K-NORMALITY, from Goodman and Salow (2018); and KM-NORMALITY, introduced in the 2023 paper.

K-NORMALITY lets people know as much as the framework allows. Given transparent evidence it validates the KK principle, and defenders of KK have appealed to it (Goodman and Salow 2023, 107 and n. 16).

Two parts of their discussion matter here.

The first is what they call "a powerful argument against COMPARABILITY" (119). COMPARABILITY is the principle that any two evidential possibilities are comparable in normality. Suppose a scale and a thermometer can fail independently. Then a situation in which only the scale fails, and one in which only the thermometer fails, must each rule out the other. COMPARABILITY forbids this, so their alternative makes normality multi-dimensional.

The second is their defence of the disjunctive form of K- and KM-NORMALITY against a diagnosis of Gettier cases that they attribute to Williamson (2015). On that diagnosis, "the blame rests on [the] disjunctive characterization of epistemic accessibility" (113). The better diagnosis, they argue, is a failure of CONVEXITY, which K and KM both satisfy (114).

This paper puts the two together. My thesis:

> On Goodman and Salow's multi-dimensional account, K-NORMALITY credits knowledge of Gettier disjunctions: a justified false belief about one source disjoined with an unknown truth about another. It does so although it satisfies CONVEXITY, and although the knowledge is not cliff-edge knowledge. So their CONVEXITY reply protects KM-NORMALITY once COMPARABILITY fails, but not K-NORMALITY.

The argument has three steps. First, under COMPARABILITY, the two disjuncts of K-NORMALITY are always nested, so its disjunction does no work (Lemma 1). Second, on multi-dimensional structures, KM-NORMALITY is non-disjunctive: one rules out a possibility exactly when changing actuality to it in one respect would make things sufficiently less normal (Theorem 2). Third, on the same structures, K-NORMALITY's knowledge about each single respect depends only on that respect, so K meets the anti-skeptical demand behind the multi-dimensional account. But its disjunction becomes active exactly when one source has failed beyond what the agent believes and another is better than the worst state she believes possible. She then knows a Gettier disjunction without knowing either disjunct (Proposition 3).

In Goodman and Salow's own model, K-NORMALITY coincides with justified-true-belief normality at the single-malfunction situations.

Two consequences follow. A principle banning such knowledge, which I call SEPARATION, is equivalent to a principle of combination across respects (Proposition 4). This gives combination a motivation that Goodman and Salow's anti-skeptical argument does not supply. Adding SEPARATION to K-NORMALITY's knowledge default yields *meet-normality* (Proposition 5). Meet-normality validates KK. It agrees with K-NORMALITY under COMPARABILITY and on every single-respect question.

Several things are not claimed. K-NORMALITY is not refuted; a K-theorist can accept the cost. SEPARATION is not beyond dispute; the probabilist's joint contexts violate it. I do not decide MARGINS, KK or COMPARABILITY. I say nothing about incomparability that is not multi-dimensional, such as the over- and underestimation of their figure 3. The argument against COMPARABILITY is Goodman and Salow's.

**Increment.** Goodman and Salow's figure 4 depicts the verdict of K-NORMALITY examined here, without comment (119). Carter and Goldstein (2021), as Goodman and Salow report them (2023, 123 n. 30), characterize accessibility as not being sufficiently less normal along any dimension. Theorem 2 shows that KM-NORMALITY, defined from the two global relations alone, already says this on products.

So far as I can find, four things are new: the nesting observation and its failure on products; the Gettier result and its bearing on the reply to Williamson; the equivalence of SEPARATION and combination; and meet-normality.

Corollary 6 sharpens Goodman and Salow's context-by-context reply (121–123). The bearing on their suggested link between COMPARABILITY and MARGINS (§8) is modest, since they offer that link with explicit hedges (111).

**Why it matters outside this debate.** Multi-dimensional normality is introduced to protect knowledge from independent sources against skepticism. Combined with a knowledge-maximizing rule, the same move starts to manufacture the most familiar kind of non-knowledge. A theory of knowledge from several sources should not let a false belief about one source generate knowledge about how it relates to another.

## 2. The framework

I follow Goodman and Salow's formulations and page references. $R_E(w)$ is the set of situations evidentially accessible from $w$, and $R_K(w)$ the set epistemically accessible from it. One knows exactly what is true throughout $R_K(w)$ (2023, 91–92). $u \succeq v$ means that $u$ is at least as normal as $v$. $u \gg v$ means that $u$ is sufficiently more normal than $v$.

The relations satisfy three conditions (92):

(i) $\succeq$ is reflexive and transitive;
(ii) $\gg$ is irreflexive and implies $\succeq$;
(iii) if $w_1 \succeq w_2 \gg w_3 \succeq w_4$, then $w_1 \gg w_4$.

So $\gg$ is asymmetric and transitive, and $u \gg v$ excludes $v \succeq u$. Well-foundedness of $\gg$ is not assumed (92 n. 4).

The five principles are these (92–93). FACTIVITY: $w \in R_K(w)$. EVIDENTIAL KNOWLEDGE: $R_K(w) \subseteq R_E(w)$. INDUCTIVE KNOWLEDGE: if $w \gg v$, then $v \notin R_K(w)$. INDUCTIVE LIMITS: an evidential possibility that no evidential possibility is sufficiently more normal than is epistemically accessible. CONVEXITY: an evidential possibility at least as normal as some epistemic possibility is epistemically accessible.

I assume TRANSPARENCY (100) and work within one evidential cell $E$. $R_B = \{v \in E : \text{no } u \in E \text{ has } u \gg v\}$ is the set of situations doxastically accessible according to BELIEF. The framework runs belief and justified belief together (112–113). ${\uparrow}w = \{v \in E : v \succeq w\}$.

Both sets are closed upward under $\succeq$, by (iii). The completions are these (104–105, 108–110, 113):

$$\textsc{I}:\ R_K(w) = \{v \in E : w \not\gg v\}$$
$$\textsc{K}:\ R_K(w) = R_B \cup {\uparrow}w$$
$$\textsc{KM}:\ R_K(w) = R_B \cup \{v \in E : \exists u \in E\,(v \succeq u,\ w \succeq u,\ w \not\gg u)\}$$
$$\textsc{JTB}:\ R_K(w) = R_B \cup \{w\}$$

Goodman and Salow characterize these completions by defaults (110, 113). I-NORMALITY is the most inclusive relation compatible with EVIDENTIAL KNOWLEDGE and INDUCTIVE KNOWLEDGE. K-NORMALITY is the most restrictive relation compatible with FACTIVITY, INDUCTIVE LIMITS and CONVEXITY, a "knowledge default". It is introduced as "the minimal change required to respect INDUCTIVE LIMITS" (104). KM-NORMALITY is the most restrictive relation compatible with MARGINS, INDUCTIVE LIMITS and CONVEXITY. JTB-NORMALITY is the most restrictive relation compatible with FACTIVITY and INDUCTIVE LIMITS. It fails CONVEXITY and is "vulnerable to Gettier-style counterexamples" (113).

MARGINS requires that an evidential possibility less normal than actuality, but not sufficiently less normal, be epistemically accessible (106). I-NORMALITY entails MARGINS (106, 111), and so does KM-NORMALITY (108–110).

K-NORMALITY entails KK given TRANSPARENCY (107). It permits *cliff-edge knowledge*, that is, knowing that one's situation lies on one side of the actual value of a quantity (105). Given failures of COLLAPSE, MARGINS rules out the cliff-edge knowledge that KK requires in inexact cases. Rejecting MARGINS does not secure KK, and Goodman and Salow leave KK's status open (107 and n. 17).

COMPARABILITY says that any two evidentially accessible situations are comparable (101). Given COMPARABILITY, KM- and I-NORMALITY coincide (111).

## 3. Orthogonal errors

Bjorn weighs himself and takes his temperature. "Plausibly, malfunctions in the two devices are epistemically independent" (117). If the thermometer is accurate, he knows his temperature even if the scale grossly misreports his weight, and conversely. The motivation is anti-skeptical: "allowing errors of one kind to generate ignorance about independent subject matters threatens much of the knowledge we take ourselves to have" (117).

Now consider two situations with the same readings. In one only the scale is grossly wrong; in the other only the thermometer is. They must be mutually epistemically inaccessible, though they are mutually evidentially accessible. Given FACTIVITY and CONVEXITY, COMPARABILITY forbids this (107, 118).

On the multi-dimensional alternative, one situation is at least as normal as another iff it is at least as normal in every dimension. It is sufficiently more normal iff, in addition, it is sufficiently more normal in some dimension (118).

Their model has two dimensions, each with three states: ordinary (0), odd (1) and bizarre (2). Ordinary is sufficiently more normal than bizarre. Odd is neither sufficiently less normal than ordinary nor sufficiently more normal than bizarre. I take the first coordinate to be the scale and the second the thermometer.

Both K- and KM-NORMALITY make $(0,2)$ and $(2,0)$ mutually inaccessible. So the framework "can accommodate the kind of epistemic independence that anti-skeptical considerations arguably motivate" (118). I-NORMALITY cannot (119), which is why they reject it without COMPARABILITY (111).

The probabilist relativizes normality to a contextually supplied question (120–121; Goodman and Salow 2021). The choice between the two approaches turns on "whether a reasonably constrained account of the needed context-sensitivity can be given" (117).

Goodman and Salow also suggest that the open questions are linked. This "lends some abductive support to the biconditional" between COMPARABILITY and MARGINS. Their reasoning in one direction: if COMPARABILITY fails, "the question of whether MARGINS is true becomes the question of which of K-NORMALITY and KM-NORMALITY is true", and "K-NORMALITY is arguably preferable on grounds of its comparative simplicity" (111). They add that "these are only some of the many considerations" (111).

## 4. K- and KM-NORMALITY on products

Call a structure *multi-dimensional* when $E = X_1 \times \dots \times X_n$; each respect $X_d$ carries a total preorder $\succeq_d$ and a relation $\gg_d$ satisfying (i)–(iii); and the global relations are defined from these as above.

The global relations then satisfy (i)–(iii). $w_d$ is the state of $w$ in respect $d$. For a set $S$ of respects, $w_S v$ agrees with $w$ on $S$ and with $v$ elsewhere. $B_d = \{x \in X_d : \text{no } y \in X_d \text{ has } y \gg_d x\}$. For $x \in X_d$, ${\uparrow}x = \{y \in X_d : y \succeq_d x\}$.

Then $R_B = \prod_d B_d$ and ${\uparrow}w = \prod_d {\uparrow}w_d$. A proposition *concerns* a set of respects if its truth depends only on the states of those respects. Upward-closed sets in a total preorder are nested.

**Lemma 1.** Given COMPARABILITY, K-NORMALITY gives $R_K(w) = R_B$ if $w \in R_B$, and $R_K(w) = {\uparrow}w$ otherwise.

*Proof.* $R_B$ and ${\uparrow}w$ are upward closed, hence nested. If $w \in R_B$, then ${\uparrow}w \subseteq R_B$. Otherwise ${\uparrow}w \not\subseteq R_B$, so $R_B \subseteq {\uparrow}w$. ∎

So wherever COMPARABILITY holds, the K-theorist's agent knows either exactly what she believes or exactly that things are at least as normal as they actually are. The cliff-edge knowledge that K-NORMALITY delivers in Goodman and Salow's one-dimensional examples (105–106) is knowledge of ${\uparrow}w$.

**Theorem 2.** On every multi-dimensional structure, KM-NORMALITY gives
$$R_K(w) = \prod_d \{x \in X_d : w_d \not\gg_d x\} = \{v \in E : \text{for no } d \text{ does } w \gg w_{\{d\}^c} v\}.$$
Here $w_{\{d\}^c} v$ is $w$ with its state in respect $d$ changed to $v_d$.

*Proof.* Suppose first that $w_d \not\gg_d v_d$ for every $d$. Let $u$ take in each respect the less normal of $w_d$ and $v_d$. Then $w \succeq u$ and $v \succeq u$. Moreover $w \not\gg u$, since each $u_d$ is $w_d$ or $v_d$. So $v$ satisfies KM's second disjunct.

Now suppose instead that $w_d \gg_d v_d$ for some $d$. Then $v \notin R_B$. Moreover, whenever $v \succeq u$ and $w \succeq u$, we have $w_d \gg_d v_d \succeq_d u_d$, so $w \gg u$ by (iii). Hence $v$ is not in $R_K(w)$.

The second equality holds because $w \gg w_{\{d\}^c} v$ iff $w_d \gg_d v_d$. ∎

No finiteness is used. The right-hand form uses only $\gg$ and is not disjunctive: it is I-NORMALITY applied to one-respect deviations from actuality.

**Proposition 3.** Let the structure be multi-dimensional with $R_B \neq \emptyset$, and assume K-NORMALITY.

(a) At $w$, the states of respect $d$ left open are exactly $B_d \cup {\uparrow}w_d$. So knowledge about a single respect depends only on that respect's actual state.

(b) Say that COND holds at $w$ if there are distinct respects $d$ and $e$ such that $w_d \notin B_d$ and $w_e$ is strictly more normal than some $b \in B_e$.

If COND fails, then $R_K(w) = \prod_d (B_d \cup {\uparrow}w_d)$.

If COND holds, then $R_K(w)$ is not $R_B$, not ${\uparrow}w$, and not a product of sets of states. The agent knows

> (G) either respect $d$ is in a state she believes possible, or respect $e$ is at least as normal as it actually is,

but knows neither disjunct. The first disjunct is false and believed; the second is true.

*Proof.* (a) $R_B$ and ${\uparrow}w$ are non-empty products, and the projection of a union is the union of the projections.

(b) Suppose COND fails. If $w \in R_B$, then $R_K(w) = R_B$, and ${\uparrow}w_d \subseteq B_d$ for each $d$. If instead $w_d \notin B_d$ for some $d$, then $B_d \subseteq {\uparrow}w_d$ by nesting. Every other $e$ also has $B_e \subseteq {\uparrow}w_e$, since COND fails and $\succeq_e$ is total. So $R_B \subseteq {\uparrow}w$ and $R_K(w) = {\uparrow}w$. In both cases $R_K(w)$ is the stated product.

Now suppose COND holds. $R_B$ lies within the first disjunct of (G) and ${\uparrow}w$ within the second, so (G) is known. The first disjunct is false since $w_d \notin B_d$, and believed since it contains $R_B$. The second is true since $w \in {\uparrow}w$.

Choose $v \in R_B$ with $v_e = b$. Then $v$ is accessible and falsifies the second disjunct, so that disjunct is not known. By FACTIVITY, neither is the first.

Finally, let $w'$ be $w$ with its respect-$e$ state changed to $b$. Then $w'$ is not believed, because of respect $d$, and not in ${\uparrow}w$, because of respect $e$. So $w'$ lies outside $R_K(w)$, though each of its states occurs in $R_K(w)$. Hence $R_K(w)$ is not a product. ∎

If $R_B = \emptyset$, which can happen when $\gg$ is not well-founded, K-NORMALITY gives ${\uparrow}w$, a product.

Part (a) settles one point. K-NORMALITY delivers in full the independence that Goodman and Salow's anti-skeptical argument demands: a failure in one respect never removes knowledge about another. Whatever is wrong with K on products, that argument cannot show it. The difference lies entirely in knowledge that links respects.

## 5. A Gettier case that CONVEXITY does not exclude

In Goodman and Salow's model at $(0,2)$, the scale is ordinary and the thermometer bizarre. $R_B$ consists of the four situations with no bizarre respect, and ${\uparrow}(0,2) = \{(0,0),(0,1),(0,2)\}$. So K-NORMALITY gives

$$R_K(0,2) = R_B \cup \{(0,2)\},$$

which is exactly JTB-NORMALITY's verdict. The same holds at $(2,0)$. Their figure 4 records the exclusion of $(1,2)$. It draws a double arrow from $(0,2)$ to $(1,2)$, which in their notation marks accessibility under KM- and I-NORMALITY but not under K-NORMALITY (105, 119). Proposition 3 says what the agent thereby knows:

> *Thermometer.* Bjorn's scale reads 175.4 pounds and is accurate. His thermometer reads 98.6 °F but is grossly wrong. He justifiably believes that neither instrument is grossly wrong, and he cannot rule out a moderate error in the scale. According to K-NORMALITY he knows: *either the thermometer is not grossly wrong, or the scale has no moderate error.*

He believes the disjunction because he believes its first disjunct, which is false. It is true because of its second disjunct, which he does not know. The two disjuncts concern different instruments. This is the shape of Gettier's (1963) second case. There a justified false belief that Jones owns a Ford is disjoined with the claim, true by luck, that Brown is in Barcelona.

Goodman and Salow endorse the verdict that such disjunctions are not known. The justified-safe-belief account, they object, predicts that "any disjunction of a justified false belief and an unknown but safely true proposition will be known". And: "That prediction is false: such disjunctions are typically not known, despite being true and justifiably believed, for the same reason as in classic Gettier cases" (113–114).

Their own example is Bjorn's justified true belief "that he weighs either around 175.4 pounds or exactly *x* pounds", which "is not something that he knows" (114). At $(0,2)$, K-NORMALITY counts as known the analogous disjunction: nothing is bizarre, or things are exactly as they are.

Their explanation of the Bjorn verdict does not carry over. In one dimension, CONVEXITY admits intermediate weights more normal than *x* (114). At $(0,2)$, no situation outside $R_B \cup \{(0,2)\}$ is at least as normal as a member of it, so even JTB-NORMALITY satisfies CONVEXITY there. The situation whose inclusion would defeat the disjunction is $(1,2)$. It is less normal than actuality, and CONVEXITY never requires it.

Goodman and Salow grant that Williamson's diagnosis, if correct, "would be trouble for K- and KM-NORMALITY, since they also characterize epistemic accessibility disjunctively" (113). They avoid the trouble by preferring the CONVEXITY diagnosis. On the multi-dimensional branch the trouble returns for K-NORMALITY, though CONVEXITY holds.

*The one-dimensional reply.* A defender of K will say that cliff-edge knowledge always has this shape. Suppose the scale errs by $e$, beyond the belief bound $c$. K-NORMALITY lets the agent know that the error is at most $e$. That is entailed by her false belief that the error is below $c$, and it is true because the error lies between $c$ and $e$, which she does not know.

But that decomposition is available for any inductive knowledge outside belief, on any completion: write a known $p$ as $R_B \vee (p \wedge \neg R_B)$. The multi-dimensional case differs in two ways.

First, by Lemma 1 the one-dimensional agent knows ${\uparrow}w$ itself, that things are at least as normal as they actually are. That is what the K-theorist undertakes to defend. In *Thermometer* the agent does not know ${\uparrow}w$, because $(1,1)$ is open. By Proposition 3(a) she has no cliff-edge knowledge about either instrument. So the exclusion of $(1,2)$ violates MARGINS without yielding any cliff-edge knowledge.

Second, the disjuncts of (G) concern disjoint sets of respects. So (G) is not equivalent, given what she knows, to anything about either instrument alone. That makes the case Gettier's pattern rather than a relabelling.

Two further features are not new, and I do not rely on them. K-NORMALITY loses this knowledge if its antecedent is discovered, a failure of NO DEFEAT of the kind Goodman and Salow document for K (127–128, 131). And K can yield knowledge from a broken clock given a special normality assumption, which they count "an important consideration in favor of MARGINS" (114 n. 23). *Thermometer* needs no special assumption.

Regimented:

(P1) A completion that counts as known a disjunction of a justified false belief about one subject matter and an unknown truth about an independent one counts a Gettier case as knowledge, if the knowledge is neither cliff-edge knowledge nor licensed by INDUCTIVE KNOWLEDGE.
(P2) On Goodman and Salow's multi-dimensional model, K-NORMALITY counts such a disjunction as known whenever COND holds.
(P3) K-NORMALITY satisfies CONVEXITY.
(C) So CONVEXITY does not protect a disjunctive completion from Gettier verdicts, and Goodman and Salow's reply to the disjunctive diagnosis does not cover K-NORMALITY beyond COMPARABILITY.

(P1) is the verdict they endorse at 113–114, restricted to the non-trivial case. (P2) is Proposition 3, together with two facts: $(0,2) \not\gg (1,2)$, and the agent has no cliff-edge knowledge. (P3) is theirs (110).

KM-NORMALITY is immune. Its accessibility sets are products (Theorem 2). In a product, knowing a disjunction of propositions about disjoint sets of respects requires knowing one of them.

The cases fit a refinement of the disjunctive diagnosis. What breeds trouble is not disjunctiveness as such but disjuncts that fail to nest. Whether the refinement holds beyond these structures I leave open.

## 6. SEPARATION and combination

The verdict generalizes to a principle about respects that are independent subject matters:

> SEPARATION. If one knows $A \vee B$, where $A$ concerns only a set $S$ of respects and $B$ only the remaining respects, and $A$ is false but believed, then one knows $B$.

This is Goodman and Salow's claim about such disjunctions, with two changes. First, it is restricted to disjuncts about independent subject matters, where the trivial decomposition cannot reach. Second, within that restriction, "typically" becomes "always".

SEPARATION is vacuous for a single respect, so it leaves one-dimensional cliff-edges alone. Nor does it ban all knowledge linking respects: at $(0,0)$ one may know that the instruments are not both odd, since no disjunct is false.

> COMBINATION. If $v \in R_K(w)$, and $S$ is a set of respects that includes one in which $w$ lies outside belief, then $w_S v \in R_K(w)$.

In words: whatever is open for the other sources stays open together with the actual state of the sources that have failed beyond belief.

**Proposition 4.** On a multi-dimensional structure with $R_B \neq \emptyset$, a relation satisfying FACTIVITY satisfies SEPARATION at $w$ iff it satisfies COMBINATION at $w$.

*Proof.* Suppose COMBINATION holds and $A \vee B$ is known, as in SEPARATION. Since $A$ is believed and $R_B \neq \emptyset$, $A$ contains $\prod_{s \in S} B_s$. Since $A$ is false, some $s \in S$ has $w_s \notin B_s$. If some accessible $v$ falsified $B$, then $w_S v$ would be accessible and would falsify both disjuncts.

Conversely, suppose $v \in R_K(w)$ and $w_S v \notin R_K(w)$, with $w_s \notin B_s$ for some $s \in S$. Let $A$ say that the respects in $S$ are not exactly as at $w$. $A$ is false, and it is believed, since $R_B$ excludes $w_s$. Let $B$ say that the other respects are not exactly as at $v$. Every accessible situation falsifying $A$ satisfies $B$, since otherwise it would be $w_S v$. So $A \vee B$ is known, but $v$ shows that $B$ is not. ∎

Goodman and Salow's argument supports only the claim that failures in one respect do not *remove* knowledge about another, and K satisfies that claim (Proposition 3(a)). COMBINATION, which forbids failures from *adding* knowledge, does not follow from their argument. Proposition 4 gives it another source: their own treatment of Gettier disjunctions, applied to independent subject matters.

On multi-dimensional structures, KM-NORMALITY satisfies SEPARATION, by Theorem 2; K-NORMALITY violates it exactly when COND holds; and I-NORMALITY violates it at $(0,2)$, where it excludes $(2,2)$ but leaves $(2,0)$ open.

The scope restriction matters, and Goodman and Salow mark it themselves. They hold that knowledge from two scales weighing one person is not the conjunction of what each would yield. A multi-dimensional treatment of the two scales "wrongly predicts" that it is, so even multi-dimensionalists about the scale and thermometer should reject that treatment (129 n. 37; cf. Goldstein and Hawthorne 2022). SEPARATION is meant for respects that are independent subject matters, such as weight and temperature, where by their lights the product model belongs. It is not meant for sources bearing on one quantity.

The probabilist rejects SEPARATION in joint contexts. Take the parameters of their figure 5 (122): each state is ten times as probable as the next worse one, the respects are independent, and the threshold is .95. The question about both instruments then has $R_B = \{(0,0),(0,1),(1,0)\}$.

At $(0,2)$, with I- or KM-NORMALITY, the joint context excludes only $(2,2)$. So the agent knows "the thermometer is not bizarre or the scale is not bizarre" without knowing the second disjunct.

With K-NORMALITY, the joint context also excludes $(1,2)$. So some probabilist context does agree with K's verdict. With a completion that respects MARGINS, however, neither the single-respect contexts nor the joint context excludes $(1,2)$ at $(0,2)$.

The probabilist's grounds differ from those in *Thermometer*. The joint ordering is total, so by Lemma 1 the K-probabilist knows ${\uparrow}(0,2)$: that the joint state is at least as probable as it is. That is ordinary cliff-edge knowledge, which stands or falls with MARGINS. The I-probabilist's exclusion of $(2,2)$ is licensed by INDUCTIVE KNOWLEDGE: double failure is improbable enough in aggregate. K's exclusion on products has neither licence.

So SEPARATION divides the multi-dimensionalist from the probabilist's joint contexts. Within the multi-dimensional branch, however, it isolates something peculiar to K. (A question singling out $(1,2)$ would exclude it under any completion, which is one reason a "reasonably constrained" account of questions is needed; 117.)

## 7. Meet-normality

Can a theorist who wants cliff-edge knowledge and KK respect SEPARATION? Define

$$\textsc{Meet}:\ R_K(w) = {\uparrow}w \cup \{v \in E : \exists b \in R_B\ \ v \succeq w \wedge b\},$$

where $w \wedge b$ is a greatest lower bound of $w$ and $b$ under $\succeq$. The choice among equivalent bounds does not matter. The definition uses only the global relations. The ${\uparrow}w$ term secures FACTIVITY when $R_B$ is empty.

**Proposition 5.**

(a) Given COMPARABILITY, meet-normality coincides with K-NORMALITY.

On multi-dimensional structures:

(b) meet-normality gives $\prod_d (B_d \cup {\uparrow}w_d)$ if $R_B \neq \emptyset$, and ${\uparrow}w$ otherwise;

(c) it satisfies the five principles and SEPARATION, and its accessibility relation is transitive, so it validates KK given TRANSPARENCY;

(d) if $R_B \neq \emptyset$, it is the most restrictive relation compatible with FACTIVITY, INDUCTIVE LIMITS, CONVEXITY and COMBINATION.

*Proof.* (a) Under COMPARABILITY, $w \wedge b$ is the less normal of $w$ and $b$. If $R_B = \emptyset$, both completions give ${\uparrow}w$. If $w \in R_B$, every $w \wedge b$ lies in the upward-closed $R_B$, and $b \succeq w \wedge b$, so meet-normality gives $R_B$. If $w \notin R_B$, then $R_B \subseteq {\uparrow}w$ by Lemma 1, so $w \wedge b$ is equivalent to $w$ and meet-normality gives ${\uparrow}w$.

(b) Meets are taken respect by respect. Some $b_d \in B_d$ has $v_d \succeq_d \min(w_d, b_d)$ iff $v_d \in B_d \cup {\uparrow}w_d$. Left to right: if the minimum is $w_d$, then $v_d \in {\uparrow}w_d$; if it is $b_d$, then $v_d \in B_d$ by upward closure. Right to left: if $v_d \in B_d$, take $b_d = v_d$; if $v_d \in {\uparrow}w_d$, any $b_d$ will do.

(c) INDUCTIVE KNOWLEDGE: if $w \gg v$, some $d$ has $w_d \gg_d v_d$, so $v_d \notin B_d \cup {\uparrow}w_d$. INDUCTIVE LIMITS: $R_B = \prod_d B_d$. CONVEXITY: products of upward-closed sets are upward closed. SEPARATION: in a product containing $w$, if a disjunction about disjoint sets of respects is known and one disjunct is false, the other is known. Transitivity: if $v_d \in {\uparrow}w_d$, then ${\uparrow}v_d \subseteq {\uparrow}w_d$; if $v_d \in B_d$, then ${\uparrow}v_d \subseteq B_d$.

(d) Let $R$ satisfy the four principles, so $R \supseteq R_B \cup \{w\}$. Let $U$ be the set of respects in which $w$ is outside belief. If $U$ is empty, meet-normality gives $R_B$. Otherwise, by nesting, it gives the product of ${\uparrow}w_f$ for $f \in U$ and $B_f$ for $f \notin U$. Take $v$ in this product, and choose $x \in R_B$ agreeing with $v$ outside $U$. COMBINATION puts $w_U x$ in $R$, and $v \succeq w_U x$, so CONVEXITY puts $v$ in $R$. ∎

On products, then, accessibility grows in the order K, meet, KM, I. Meet-normality's set is the smallest product containing K's, and the two agree on every single-respect proposition. Meet-normality is the knowledge default given SEPARATION, as K is the knowledge default without it.

Outside belief, meet-normality's knowledge is, respect by respect, either true belief or cliff-edge knowledge about a failing respect. It violates MARGINS: at $(1,1)$ the agent knows that neither respect is bizarre, whereas under KM she knows nothing. The completions Goodman and Salow reject in n. 18 aim at MARGINS and fail CONVEXITY or INDUCTIVE LIMITS (108). Meet-normality rejects MARGINS and satisfies all five principles, so it competes with K rather than with them.

One limit remains. Meet-normality needs greatest lower bounds. Discovery in Goodman and Salow's sense intersects the evidential cell with what is discovered (124–125). Discovering something about one respect leaves a product. Discovering something that links respects can leave a cell without meets. For example, if the agent of figure 4 discovers that $(1,1)$ does not obtain, then $(0,1)$ and $(1,0)$ have no greatest lower bound. On such cells the characterization in (d) is the natural general definition, but I have not investigated its logic.

## 8. Consequences

**The abductive link.** Goodman and Salow's step reads: if COMPARABILITY fails, the MARGINS question is K against KM, and K is simpler (111). Their standard of simplicity, applied to I-NORMALITY, is being "encouragingly simple, non-disjunctive, and parsimonious, featuring only one relation of comparative normality" (111). By that standard Theorem 2 reverses the comparison on the structures that motivate rejecting COMPARABILITY. There KM-NORMALITY is non-disjunctive and uses only $\gg$, while K-NORMALITY's disjunction is active.

One may reply that simplicity attaches to general definitions, not to their behaviour on a class of structures. But the step is conditional on COMPARABILITY's failing, and on its failing in the multi-dimensional way that Goodman and Salow find most compelling (109). What matters is which theory gives the simpler account of those structures. K-NORMALITY also incurs there the Gettier cost of §5, which KM-NORMALITY does not. The hedged suggestion is not refuted, but this direction of it loses its stated support.

Granting SEPARATION, more follows. The choice on products is then between KM- and meet-normality, which within each respect are I- and K-NORMALITY, where COMPARABILITY holds (Theorem 2, Proposition 5(b)). So for multi-dimensional incomparability the MARGINS question is the comparable-case question, asked once for each respect.

**KK.** Some defenders of KK rely on K-NORMALITY (107 n. 16). If they accept the orthogonality argument, they have three options: keep K and accept *Thermometer*; move to meet-normality, which agrees with K wherever COMPARABILITY holds and validates KK; or keep COMPARABILITY, as the probabilist does.

None of these settles KK, whose status Goodman and Salow leave open (107 n. 17).

**The probabilist.** In a context whose question concerns respect $d$ alone, the probabilist compares situations by the probability of their state in $d$. The sufficiency proposal (121) then yields relations on $X_d$ satisfying (i)–(iii).

**Corollary 6.** Suppose each respect's relations are the probabilist's single-respect relations. Then at every situation, KM-NORMALITY's accessibility set is the intersection of the single-respect contexts' I-NORMALITY sets; and meet-normality's set is the intersection of their K-NORMALITY sets.

*Proof.* Each context is comparable. In context $d$, I-NORMALITY leaves open $\{v : w_d \not\gg_d v_d\}$, and K-NORMALITY leaves open $\{v : v_d \in B_d \cup {\uparrow}w_d\}$. Apply Theorem 2 and Proposition 5(b). ∎

This sharpens Goodman and Salow's context-by-context reply (121) and their location of the dispute at the preface (122–123). Given a shared completion, the multi-dimensionalist and the probabilist agree on every single-respect question. They part over two things: whether knowledge agglomerates across respects, and whether joint contexts yield knowledge that links respects. SEPARATION bears on the second.

## 9. Objections and replies

### 9.1 The price of the knowledge default

*Objection.* K-NORMALITY is principled: it adds to belief only what FACTIVITY and CONVEXITY force (2023, 104, 110). *Thermometer* is what that rationale yields when belief and ${\uparrow}w$ do not nest, and a K-theorist may accept it.

*Reply.* She may, but the cost is now exact. At the single-malfunction situations of the model that motivates rejecting COMPARABILITY, she must accept the verdict of the account Goodman and Salow reject as Gettier-prone. She must also forgo their reply to Williamson for her own completion.

Meet-normality removes the cost. It keeps the knowledge default as far as SEPARATION allows, all cliff-edge knowledge about individual respects, and KK. What remains is a question of method: whether unrestricted minimality should outrank verdicts about Gettier cases. Minimality cannot settle that within the framework. JTB-NORMALITY is also a minimal default (113), and Goodman and Salow reject it for its Gettier verdicts (113–114).

### 9.2 Respects are not part of the framework

*Objection.* The framework characterizes knowledge from $\succeq$ and $\gg$ alone (2023, 97), but SEPARATION adverts to respects.

*Reply.* The multi-dimensional account defines $\succeq$ and $\gg$ from respects, and the orthogonality argument is stated in terms of them. Lemma 1, Theorem 2 and meet-normality's definition use only the global relations. Respects enter only in saying which disjunctions are Gettier disjunctions.

### 9.3 The probabilist refutes SEPARATION

*Objection.* In the joint context the agent knows that the instruments have not both failed grossly, in violation of SEPARATION (§6). If that knowledge is genuine, SEPARATION is false.

*Reply.* Suppose joint contexts are admissible and their verdicts genuine. Then SEPARATION should be restricted to knowledge not licensed by INDUCTIVE KNOWLEDGE. Since that is a framework principle, the restriction is not ad hoc.

The restricted principle still condemns *Thermometer*. Actuality is not sufficiently more normal than $(1,2)$ in the product ordering, in either single-respect ordering, or in the joint ordering. KM- and meet-normality still satisfy the restricted principle on products. It would also condemn the K-probabilist's joint exclusion of $(1,2)$, which must then be defended as cliff-edge knowledge. Whether joint contexts are admissible is part of the question Goodman and Salow leave open (117).

## 10. Conclusion

On Goodman and Salow's multi-dimensional account, K-NORMALITY respects the independence their anti-skeptical argument demands. But it does something that argument does not address. When one source fails beyond belief and another works well, it credits knowledge of a disjunction of a justified false belief about one source and an unknown truth about the other. That knowledge is not cliff-edge knowledge, and at the situations the orthogonality argument concerns it is what justified-true-belief normality says.

CONVEXITY does not exclude this knowledge. So Goodman and Salow's reply to the disjunctive diagnosis protects KM-NORMALITY, which is non-disjunctive on these structures, but not K-NORMALITY. The principle banning such knowledge is equivalent to combination across respects. Imposed on K-NORMALITY's knowledge default, it yields meet-normality, which keeps KK.

Two questions remain open: whether SEPARATION extends beyond independent subject matters, and how a KK-friendly completion should behave on cells without meets.

Every formal claim is proved above. The finite claims were also checked by computer enumeration over 5,949 multi-dimensional and 3,594 comparable structures, and the infinite cases, including a respect with empty $R_B$, with the z3 solver.

## References

Carter, Sam, and Simon Goldstein. 2021. "The Normality of Error." *Philosophical Studies* 178: 2509–2533.

Gettier, Edmund L. 1963. "Is Justified True Belief Knowledge?" *Analysis* 23: 121–123.

Goldstein, Simon, and John Hawthorne. 2022. "Knowledge from Multiple Experiences." *Philosophical Studies* 179: 1341–1372.

Goodman, Jeremy, and Bernhard Salow. 2018. "Taking a Chance on KK." *Philosophical Studies* 175: 183–196.

Goodman, Jeremy, and Bernhard Salow. 2021. "Knowledge from Probability." *Electronic Proceedings in Theoretical Computer Science* 335 (TARK 2021): 171–186.

Goodman, Jeremy, and Bernhard Salow. 2023. "Epistemology Normalized." *The Philosophical Review* 132: 89–145.

Williamson, Timothy. 2015. "A Note on 'Gettier Cases in Epistemic Logic'." *Philosophical Studies* 172: 129–140.
