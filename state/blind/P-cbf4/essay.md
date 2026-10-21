# Normality in Respects: Independent Sources, Margins, and the Completions of Normality-Based Knowledge

**Abstract.** Goodman and Salow's normality framework leaves open whether all evidential possibilities are comparable in normality. Their main argument against COMPARABILITY is that independent sources, such as a scale and a thermometer, are orthogonal ways for things to go wrong. They also suggest that, once comparability fails, whether knowledge has margins for error turns on a choice between their K- and KM-normality. I show that on their own multi-dimensional account of normality, KM-normality is exactly i-normality applied respect by respect, so that what one knows is the conjunction of what one knows along each respect. K-normality instead violates a combination principle that the argument from orthogonal errors presupposes: it gives an agent cliff-edge knowledge about a working instrument because a different instrument has failed. A completion outside their catalogue, meet-normality, coincides with K-normality under comparability, satisfies the combination principle and validates KK. So the question of margins, and with it the normality case for KK, is independent of the question of comparability. Every formal claim is proved and machine-checked.

## 1. Introduction

Goodman and Salow (2023) offer a general framework for inductive knowledge. A person's knowledge is fixed by which situations compatible with her evidence are more normal than which, and by which are *sufficiently* more normal than which. The framework comes with three ways of computing knowledge from these relations, which Goodman and Salow call I-, K- and KM-NORMALITY, and it leaves two structural questions open. The first is COMPARABILITY: must any two evidential possibilities be comparable in normality? The second is MARGINS: must a possibility that is less normal than actuality, but not sufficiently less normal, remain epistemically possible? Given the failures of COLLAPSE they defend, MARGINS bans cliff-edge knowledge, which the KK principle requires in inexact cases, so the second question carries the framework's verdict on KK (2023, 105–107).

Goodman and Salow suggest that the two questions are linked, and that this "lends some abductive support to the biconditional" between COMPARABILITY and MARGINS (2023, 111). If COMPARABILITY holds, I-NORMALITY is tenable, it is the simplest completion, and it entails MARGINS. If COMPARABILITY fails, I-NORMALITY becomes skeptical, so "the question of whether MARGINS is true becomes the question of which of K-NORMALITY and KM-NORMALITY is true" (111). K-NORMALITY is the simpler of the two and violates MARGINS.

Their main reason to reject COMPARABILITY comes from independent sources (2023, 117–119). A scale can fail while a thermometer works, and the reverse. Such failures should not cost knowledge along the other dimension, and that requires two situations, each able to rule out the other, which COMPARABILITY forbids. On their multi-dimensional alternative, both K- and KM-NORMALITY respect the independence.

This paper asks whether they respect it equally. They do not. My thesis is this:

> On Goodman and Salow's multi-dimensional account, KM-NORMALITY delivers exactly the independence that motivates rejecting COMPARABILITY, while K-NORMALITY violates it. A theorist who wants cliff-edge knowledge and KK without COMPARABILITY must therefore adopt a completion outside their catalogue. With that completion in view, the question of MARGINS is the same question with or without COMPARABILITY.

The argument has four formal parts. Theorem 1 shows that, on multi-dimensional structures, KM-NORMALITY is i-normality applied respect by respect. One rules out a possibility exactly when, in some respect, actuality is sufficiently more normal than it. Proposition 2 states exactly when K-NORMALITY violates a principle I call COMBINATION. The condition is the ordinary one in multi-source cases: one source fails, another works better than the worst one believes possible. Proposition 3 introduces *meet-normality*. It coincides with K-NORMALITY whenever COMPARABILITY holds, it factorizes respect by respect, and it validates KK given transparent evidence. Corollary 4 shows that, when the respects are given probabilistic normality as Goodman and Salow's probabilist proposes, the multi-dimensional theorist with KM-NORMALITY and the probabilist agree about every single-respect question. They disagree only about whether knowledge agglomerates across respects.

Some things are not claimed here. I do not decide MARGINS, KK or COMPARABILITY. The results concern incomparability of the multi-dimensional kind, which Goodman and Salow present as the more compelling kind (2023, 109); they do not cover the incomparability of over- and underestimation in their figure 3. The argument that COMPARABILITY conflicts with independent sources is theirs, not mine.

Here is the increment over the closest work. Goodman and Salow (2023) introduce the three completions and the multi-dimensional model, and their figure 4 depicts the verdict of K-NORMALITY that I criticize, without comment (119). Carter and Goldstein (2021), as Goodman and Salow report them (2023, 123 n. 30), characterize accessibility as not being sufficiently less normal along any dimension. Theorem 1 shows that this respect-wise form is not an extra posit: on multi-dimensional structures it is what KM-NORMALITY, defined from the two global relations alone, already says. The criticism of K-NORMALITY, meet-normality, the independence of COMBINATION from MARGINS, and the reduction of the probabilist dispute to agglomeration are, so far as I can find, new.

Why should a reader outside this debate care? A natural thought about knowledge from several sources is that each source contributes its own knowledge, and that one source's failure neither removes nor adds knowledge along the others. The results show that this thought is not free. Among normality theories it singles out a definite structure, and it separates two questions, about comparability and about margins, that had seemed tied together.

## 2. The framework

I follow Goodman and Salow's formulations and page references throughout. Situations are centered on an agent. $R_E(w)$ is the set of situations evidentially accessible from $w$, and $R_K(w)$ the set epistemically accessible from it. One knows exactly what is true throughout $R_K(w)$ (2023, 91–92). There are two relations: $u \succeq v$, "$u$ is at least as normal as $v$", and $u \gg v$, "$u$ is sufficiently more normal than $v$". The official structural assumptions are these (92):

(i) $\succeq$ is reflexive and transitive.
(ii) $\gg$ is irreflexive and implies $\succeq$.
(iii) If $w_1 \succeq w_2$, $w_2 \gg w_3$ and $w_3 \succeq w_4$, then $w_1 \gg w_4$.

These imply that $\gg$ is asymmetric and transitive (92 n. 4), and that $u \gg v$ excludes $v \succeq u$. The *normality framework* consists of five principles (92–93). FACTIVITY: $w \in R_K(w)$. EVIDENTIAL KNOWLEDGE: $R_K(w) \subseteq R_E(w)$. INDUCTIVE KNOWLEDGE: if $w \gg v$, then $v \notin R_K(w)$. INDUCTIVE LIMITS: an evidential possibility that no evidential possibility is sufficiently more normal than is epistemically accessible. CONVEXITY: an evidential possibility at least as normal as some epistemic possibility is itself epistemically accessible. I assume TRANSPARENCY: if $v \in R_E(w)$, then $R_E(v) = R_E(w)$ (100). So I can work inside one evidential cell $E$.

Write $R_B = \{v \in E : \text{no } u \in E \text{ has } u \gg v\}$ for the doxastically accessible situations given by BELIEF (112–113), and ${\uparrow}w = \{v \in E : v \succeq w\}$. The three completions are these (104–105, 108–110). K-NORMALITY comes from Goodman and Salow (2018), and I-NORMALITY from Goldstein and Hawthorne (2022):

$$\textsc{I}:\ R_K(w) = \{v \in E : w \not\gg v\}$$
$$\textsc{K}:\ R_K(w) = R_B \cup {\uparrow}w$$
$$\textsc{KM}:\ R_K(w) = R_B \cup \{v \in E : \exists u \in E\,(v \succeq u,\ w \succeq u,\ w \not\gg u)\}$$

Goodman and Salow characterize them by defaults (110). I-NORMALITY is the most inclusive relation compatible with EVIDENTIAL KNOWLEDGE and INDUCTIVE KNOWLEDGE, an "ignorance default". K-NORMALITY is the most restrictive relation compatible with FACTIVITY, INDUCTIVE LIMITS and CONVEXITY, a "knowledge default". KM-NORMALITY is the most restrictive relation compatible with MARGINS, INDUCTIVE LIMITS and CONVEXITY. MARGINS says that if $v \in E$ is less normal than $w$ but not sufficiently less normal, then $v \in R_K(w)$ (106). I-NORMALITY entails MARGINS. K-NORMALITY entails KK given TRANSPARENCY (107), and it permits cliff-edge knowledge. COMPARABILITY says that any two evidentially accessible situations are comparable (101). Given COMPARABILITY, KM- and I-NORMALITY coincide (111).

## 3. Orthogonal errors and the choice they leave

Goodman and Salow's argument runs as follows (2023, 117–118). Bjorn weighs himself and also takes his temperature. "Plausibly, malfunctions in the two devices are epistemically independent" (117). If the thermometer is accurate, he knows his temperature even if the scale grossly misreports his weight, and the same holds with the instruments exchanged. Now take two situations with the same readings, one in which only the scale is grossly wrong and one in which only the thermometer is. Neither is epistemically accessible from the other, yet each is evidentially accessible from the other. COMPARABILITY forbids this. Given FACTIVITY and CONVEXITY, it implies that mutually evidentially accessible situations cannot be mutually epistemically inaccessible (107, 118).

Their alternative is multi-dimensional. For one situation to be at least as normal as another is for it to be at least as normal along every dimension. For it to be sufficiently more normal is for it to be at least as normal and sufficiently more normal along at least one dimension (118). Their model has two dimensions, each with three states: ordinary (0), odd (1) and bizarre (2). Ordinary is sufficiently more normal than bizarre, and odd is neither sufficiently less normal than ordinary nor sufficiently more normal than bizarre. Both K- and KM-NORMALITY then make $(0,2)$ and $(2,0)$ mutually inaccessible: "even when things are bizarre along one dimension, you can still know that they aren't bizarre along the other dimension" (118). I-NORMALITY fails here, since "any abnormality along one dimension makes inductive knowledge impossible along any orthogonal dimension" (119). This is why they reject I-NORMALITY without COMPARABILITY (111). I will label the first coordinate the scale and the second the thermometer.

The probabilist, developing Goodman and Salow (2021), replies by relativizing normality to a contextually supplied question (2023, 120–121). In a context concerned with the weight, situations are compared by the probability of their answer to that question. In such contexts COMPARABILITY holds, but the two single-malfunction situations are never mutually inaccessible in one context. Goodman and Salow leave the choice open; it turns "on whether a reasonably constrained account of the needed context-sensitivity can be given" (117). Sections 4–7 work on the multi-dimensional branch, where the remaining choice is between K and KM. Section 8 returns to the probabilist.

## 4. Combination

Call a structure *multi-dimensional* when it has the following form. $E = X_1 \times \dots \times X_n$; each respect $X_d$ carries a total preorder $\succeq_d$ and a relation $\gg_d$ satisfying (i)–(iii); and the global relations are defined from these as Goodman and Salow define them. It is routine to check that the global relations then satisfy (i)–(iii). For $w \in E$, $w_d$ is its state in respect $d$, and $w[d{\mapsto}x]$ is the situation that agrees with $w$ except that its state in respect $d$ is $x$. Let $B_d = \{x \in X_d : \text{no } y \in X_d \text{ has } y \gg_d x\}$. Then $R_B = B_1 \times \dots \times B_n$.

The principle I defend is this:

> COMBINATION. If $v \in R_K(w)$, then $w[d{\mapsto}v_d] \in R_K(w)$ for every respect $d$.

In words: if, for all one knows, things are a certain way in one respect, then for all one knows they are that way in that respect while every other respect is as it actually is. A stronger principle, FACTORIZATION, says that $R_K(w)$ is a product $\prod_d R_d(w_d)$, where what is left open in respect $d$ depends only on $w_d$.

COMBINATION spells out the independence in Goodman and Salow's argument, in the direction their argument leaves implicit. Their argument says that a failure in one respect does not remove knowledge in another. COMBINATION says that the actual state of the other respects does not add any either. Suppose one cannot rule out that the scale is odd, but can rule out that the scale is odd *while the thermometer is as it actually is*. Then one's knowledge about the scale depends on the thermometer's actual condition, and that is the dependence the orthogonality argument denies. Goodman and Salow appeal to the same pattern of reasoning elsewhere: "Intuitively, if for all he knows the error is extreme and for all he knows the scale is consumer-grade, then for all he knows the error is extreme and the scale is consumer-grade" (116). There they derive the combination from CONVEXITY and a normality assumption. In the multi-dimensional setting the needed normality comparisons fail, so whether combination holds is left to the completion.

COMBINATION is weak in two ways. It is anchored to the actual states of the other respects, so it does not forbid knowing that two respects are not *both* abnormal. It says nothing about agglomeration either, since knowledge is closed under conjunction in this framework anyway. Section 9.1 returns to both points.

## 5. KM-NORMALITY is i-normality respect by respect

For $x \in X_d$, let $I_d(x) = \{y \in X_d : x \not\gg_d y\}$. This is i-normality computed within respect $d$ alone.

**Theorem 1.** On every multi-dimensional structure, KM-NORMALITY gives $R_K(w) = I_1(w_1) \times \dots \times I_n(w_n)$.

*Proof.* Suppose $v_d \in I_d(w_d)$ for every $d$. Let $u$ be the situation whose state in each respect is the less normal of $w_d$ and $v_d$; this exists because each $\succeq_d$ is total. Then $w \succeq u$ and $v \succeq u$. And $w \not\gg u$: in each respect $u_d$ is either $w_d$, and $\gg_d$ is irreflexive, or $v_d$, and $w_d \not\gg_d v_d$ by assumption. So $v$ satisfies the second disjunct of KM-NORMALITY. Conversely, suppose $w_d \gg_d v_d$ for some $d$. Then $v \notin R_B$, since $v[d{\mapsto}w_d] \gg v$. And if $v \succeq u$ and $w \succeq u$, then $w_d \gg_d v_d \succeq_d u_d$, so $w_d \gg_d u_d$ by (iii), and hence $w \gg u$. So $v \notin R_K(w)$. ∎

So on the multi-dimensional branch, KM-NORMALITY has a simple non-disjunctive form: one rules out a possibility exactly when, in some respect, actuality is sufficiently more normal than it. This is the dimension-wise characterization that Goodman and Salow attribute to Carter and Goldstein. It falls out of KM-NORMALITY, which is defined from the global relations alone. Three consequences follow at once. KM-NORMALITY satisfies FACTORIZATION, and hence COMBINATION. What one knows is the conjunction of what one knows in each respect, and what one knows in a respect depends only on how things are in that respect. Goodman and Salow themselves take conjunctive structure to be a consequence of multi-dimensional treatments, in their discussion of two scales measuring one weight (129 n. 37). Finally, KM-NORMALITY satisfies, on these structures, the principle that one knows at least as much in a more normal situation with the same evidence. In general KM-NORMALITY can violate this principle (116 n. 25), but their counterexample uses an incomparability that is not of the multi-dimensional kind.

## 6. What K-NORMALITY says about a working instrument

Take Goodman and Salow's model at $(0,2)$: the scale is ordinary, the thermometer bizarre. $R_B$ is the four situations with no bizarre respect, and ${\uparrow}(0,2) = \{(0,0),(0,1),(0,2)\}$. So K-NORMALITY gives

$$R_K(0,2) = \{(0,0),(0,1),(1,0),(1,1),(0,2)\}.$$

$(1,2)$ is excluded. Yet $(1,1)$ is accessible, so for all the agent knows the scale is odd; and the thermometer is in fact bizarre. COMBINATION fails. Their figure 4 records the verdict. From $(0,2)$ to $(1,2)$ it draws a double arrow, which in their notation marks accessibility under KM- and I-NORMALITY but not K-NORMALITY (105, 119). KM-NORMALITY includes $(1,2)$, and so does I-NORMALITY.

What K-NORMALITY credits the agent with knowing, beyond what KM-NORMALITY does, is this:

> If the thermometer is bizarre, the scale is ordinary.

Four features make this a cost rather than a curiosity.

First, it is cliff-edge knowledge about the instrument that is working. Relative to the thermometer's actual state, the agent knows that the scale is at least as good as it actually is. Yet the scale is in its most normal state, and nothing about it is outside what she believes. In a single dimension, K-NORMALITY's cliff-edge knowledge has a clear source. When actuality falls outside what one believes, one knows that things are at least as normal as they actually are, and that is the knowledge ${\uparrow}w$ encodes (105). Here the knowledge concerns a respect along which things have gone perfectly, and it is triggered by a failure in a different respect. Whatever the merits of the single-dimension rationale, it does not cover this case.

Second, the knowledge rests on a false belief. At $(0,0)$ the agent knows the conditional because she knows its antecedent is false: the thermometer is not bizarre. At $(0,2)$ that belief is false, the conditional's consequent is something she does not know, and the conditional is true only because the scale happens to be ordinary rather than odd, which she cannot tell apart. This is the structure Goodman and Salow themselves count as a Gettier case. Bjorn has a justified true belief "that he weighs either around 175.4 pounds or exactly *x* pounds," which "is not something that he knows" (114). Their diagnosis is that the theories which wrongly count such beliefs as knowledge fail CONVEXITY (114). K-NORMALITY satisfies CONVEXITY, but CONVEXITY says nothing here: $(1,2)$ is not at least as normal as any accessible situation.

Third, the knowledge does not survive learning its antecedent. Model the discovery that the thermometer is bizarre in the way Goodman and Salow model discovery, with normality fixed by the underlying states (124–128). In the new evidential cell, K-NORMALITY leaves $(1,2)$ accessible, so the agent does not come to know that the scale is ordinary. She knew the conditional, and she cannot use it.

Fourth, no other view in the space Goodman and Salow survey agrees. KM- and I-NORMALITY leave $(1,2)$ open. So, as section 8 shows, does every probabilist context: the scale question, the thermometer question and the joint question.

This is not a quirk of one model.

**Proposition 2.** On a multi-dimensional structure with finite respects, K-NORMALITY violates COMBINATION at $w$ if and only if there are distinct respects $d$ and $e$ such that $w_d \notin B_d$ and $w_e$ is strictly more normal than some state in $B_e$. When there is no such pair, $R_K(w) = \prod_d (B_d \cup {\uparrow}w_d)$.

*Proof sketch.* If such $d$ and $e$ exist, pick $b \in B_e$ with $w_e \succ_e b$ and a believed situation $v$ with $v_e = b$. Then $v \in R_K(w)$, but $w[e{\mapsto}b]$ is not believed, since its state in respect $d$ is $w_d$, and it is not at least as normal as $w$, since it is worse in respect $e$. So it is not in $R_K(w)$. Otherwise, either $w \in R_B$, so that $R_K(w) = R_B$; or every respect other than an unbelieved one has $B_e = {\uparrow}w_e$, using the fact that upward-closed sets in a chain are nested. In both cases the union $R_B \cup {\uparrow}w$ is the stated product. ∎

The condition is that one respect has failed beyond what one believes, while another is working better than the worst one believes possible. That is the usual state of an agent who consults several sources, one of which has failed. So the violation is the normal case.

## 7. Meet-normality, and why COMPARABILITY does not settle MARGINS

The obvious reply is that K-NORMALITY's defender already rejects MARGINS and accepts cliff-edge knowledge, so the exclusion of $(1,2)$ is one more instance of a commitment already made. The reply fails, because COMBINATION and MARGINS are independent. A completion can have cliff-edge knowledge and KK without violating COMBINATION.

Define *meet-normality*:

$$\textsc{Meet}:\ R_K(w) = \{v \in E : \exists b \in R_B\ \ v \succeq w \wedge b\},$$

where $w \wedge b$ is a greatest lower bound of $w$ and $b$ under $\succeq$. The definition uses only the global relations.

**Proposition 3.** (a) Given COMPARABILITY, meet-normality coincides with K-NORMALITY. (b) On every multi-dimensional structure, it gives $R_K(w) = \prod_d (B_d \cup {\uparrow}w_d)$, which is K-NORMALITY applied respect by respect. It satisfies the five principles of the framework and FACTORIZATION, and its accessibility relation is transitive, so it validates KK given TRANSPARENCY. (c) On such structures it is the most restrictive relation compatible with FACTIVITY, INDUCTIVE LIMITS, CONVEXITY and FACTORIZATION. With two respects, COMBINATION may replace FACTORIZATION.

*Proof sketch.* (a) Under COMPARABILITY, $w \wedge b$ is the less normal of $w$ and $b$. If $w \notin R_B$, every believed $b$ is more normal than $w$, since $R_B$ is upward closed by (iii); so the union is ${\uparrow}w$, which contains $R_B$, and equals $R_B \cup {\uparrow}w$. If $w \in R_B$, the union is $R_B$. (b) Meets are taken coordinate by coordinate, and $v_d$ is at least as normal as the less normal of $w_d$ and the least normal state in $B_d$ just in case $v_d \in B_d \cup {\uparrow}w_d$. The framework principles and transitivity hold respect by respect; single-respect K-NORMALITY is transitive given COMPARABILITY. (c) Any upward-closed product containing $R_B$ and $w$ contains $\prod_d (B_d \cup {\uparrow}w_d)$. ∎

Meet-normality is thus the knowledge default once FACTORIZATION is respected, just as K-NORMALITY is the knowledge default without it. It violates MARGINS: at $(1,1)$ in Goodman and Salow's model, it lets the agent know that neither respect is bizarre, while KM-NORMALITY lets her know nothing. The four completions sort as follows on multi-dimensional structures:

| | satisfies COMBINATION | satisfies MARGINS |
|---|---|---|
| KM-NORMALITY | always | always |
| meet-normality | always | not always |
| I-NORMALITY | not always | always |
| K-NORMALITY | not always | not always |

"Always" entries follow from Theorem 1, Proposition 3 and the fact that I- and KM-NORMALITY entail MARGINS (106, 111). "Not always" entries are witnessed in Goodman and Salow's model.

Now return to the abductive link. On the multi-dimensional branch, COMBINATION excludes K-NORMALITY. The choice that bears on MARGINS is between KM- and meet-normality. Both factorize, and within each respect, where COMPARABILITY holds, they are I- and K-NORMALITY respectively. So the question of MARGINS without COMPARABILITY, for incomparability of this kind, is the question of MARGINS with COMPARABILITY, asked once for each respect. It is not the question of K against KM, and the simplicity of K-NORMALITY does not bear on it. Goodman and Salow's argument for the direction "if COMPARABILITY fails, MARGINS fails" lapses. Whatever favors I-NORMALITY under COMPARABILITY, such as its simple, non-disjunctive form (111), carries over to KM-NORMALITY here, since by Theorem 1 KM-NORMALITY is i-normality respect by respect. Whatever favors cliff-edge knowledge under COMPARABILITY carries over to meet-normality. The two questions come apart.

The consequence for KK is direct. A defender of KK in the normality framework who is persuaded by the argument from orthogonal errors cannot keep K-NORMALITY. She can keep KK by moving to meet-normality, at no cost to her single-dimension verdicts. Or she can keep K-NORMALITY and COMPARABILITY together, answering the orthogonality argument as the probabilist does.

## 8. Agreement with the probabilist, respect by respect

Goodman and Salow's probabilist compares situations by the evidential probability of their answers to a contextual question, and proposes that "*w* is sufficiently more normal than *v* just in case the evidential probability of things being more normal than *v*, given that they are no more normal than *w*, is sufficiently high" (121). In a context whose question is how things stand in respect $d$, this yields relations on $X_d$ computed from the marginal probabilities on $d$. These satisfy (i)–(iii): enlarging the conditioning event by more normal states, or enlarging the target event, can only raise the conditional probability. Since COMPARABILITY holds within the context, KM- and I-NORMALITY agree, and one rules out $v$ exactly when $w_d$ is sufficiently more normal than $v_d$ by these relations.

**Corollary 4.** Suppose the multi-dimensional theorist's relations in each respect are the probabilist's single-respect relations. Then at every situation, the KM-NORMALITY accessibility set is the intersection of the probabilist's accessibility sets for the single-respect contexts.

This follows from Theorem 1. So, on everything either side says about a single respect, the two agree exactly. What the multi-dimensional theorist with KM-NORMALITY adds is agglomeration. She counts as known in one context the conjunction of what the probabilist counts as known only in separate contexts. The probabilist adds joint-question knowledge that the multi-dimensional theorist does not recognize. With the parameters of their figure 5 (122: each state ten times as probable as the next worse one, independent respects, threshold .95), the joint context lets the agent at $(0,0)$ rule out $(1,1)$, so she knows the two respects are not both odd. At $(0,2)$ it lets her rule out only $(2,2)$. No probabilist context rules out $(1,2)$ at $(0,2)$, which completes the fourth point of section 6.

Two things follow for the open question Goodman and Salow leave. First, the scale-and-thermometer case does not by itself tell against the probabilist. Once the multi-dimensional theorist adopts KM-NORMALITY, the case shows only that orthogonal knowledge is available respect by respect, and the probabilist provides exactly that, context by context. Second, the dispute over knowledge in these cases is located at two points: whether knowledge agglomerates across respects, and whether aggregate improbability across respects yields knowledge that no respect yields alone. That is where Goodman and Salow's preface discussion sits (122–123). The "reasonably constrained account of the needed context-sensitivity" (117) must therefore say which conjunctions of respects form admissible questions. That is a narrower demand than it first appeared to be.

## 9. Objections and replies

### 9.1 Knowledge across respects

*Objection.* COMBINATION is false. One can know that two independent instruments have not both failed without knowing of either that it has not failed. The probabilist's joint context delivers such knowledge, and Carter and Goldstein's second-order dimension delivers knowledge that things are not normal in every respect (Goodman and Salow 2023, 123 n. 30). K-NORMALITY's exclusion of $(1,2)$ may be more of the same.

*Reply.* COMBINATION is consistent with knowing that two respects are not both abnormal, provided the knowledge does not involve the actual state of either. The probabilist's joint context does violate COMBINATION at $(0,2)$, where it excludes $(2,2)$ but not $(2,0)$. But it does so for a reason the multi-dimensional theorist rejects: the aggregate improbability of a double failure. Goodman and Salow note that the multi-dimensional account, unlike the probabilist one, does not tie knowledge to high probability (122–123). Carter and Goldstein's knowledge that not everything is normal comes from a further dimension that cannot be combined into an overall ordering (123 n. 30), so their structures are not multi-dimensional in the present sense. In any case, K-NORMALITY's exclusion is not of the aggregate kind. $(1,2)$ is ten times as probable as $(2,2)$ on the figure-5 parameters, and the joint context leaves it open. A K-theorist who wanted to rest the exclusion on aggregation would have to give up K-NORMALITY for a probabilist account. What remains of the objection is that COMBINATION may need restriction in cases with very many respects, where aggregate effects are large. My cases have two respects.

### 9.2 Respects are not part of the framework

*Objection.* The framework characterizes knowledge from $\succeq$ and $\gg$ alone (2023, 97). COMBINATION adverts to respects, which the relations do not mention, so a K-theorist may simply refuse to answer to it.

*Reply.* The multi-dimensional account defines $\succeq$ and $\gg$ from the respects, and the orthogonality argument that motivates it is stated in terms of respects. A theorist who invokes that argument against COMPARABILITY cannot then disown the respects when they tell against her completion. Moreover, nothing in my positive proposals goes beyond the two relations. KM-NORMALITY and meet-normality are both defined from $\succeq$ and $\gg$ alone, and on multi-dimensional structures they recover the respect-wise forms. A theorist who rejects the product structure altogether gives up Goodman and Salow's only worked-out model of orthogonal errors. She then owes another.

### 9.3 K-NORMALITY is the knowledge default

*Objection.* K-NORMALITY is principled: it is the most restrictive relation the framework allows (2023, 110). COMBINATION is an extra constraint brought in to block it.

*Reply.* Every completion is a default relative to some set of constraints; KM-NORMALITY is the knowledge default given MARGINS. Proposition 3(c) shows that meet-normality is the knowledge default given FACTORIZATION, and Proposition 3(a) shows that it agrees with K-NORMALITY wherever COMPARABILITY holds. So meet-normality is the conservative extension of the knowledge default to the setting in which the knowledge-default theorist has rejected COMPARABILITY. The objection would bite only if FACTORIZATION were unmotivated. Section 4 argued that it is the content of the orthogonality claim.

### 9.4 Scope

*Objection.* Meet-normality needs greatest lower bounds, which arbitrary preorders lack. And not all incomparability is multi-dimensional. Goodman and Salow's model in which over- and underestimation are incomparable is not a product of chains (2023, 107–108).

*Reply.* Both points are correct and mark the limits of the results. In structures without meets, I have not determined what the right KK-friendly completion is. Since meet-normality coincides with K-NORMALITY under COMPARABILITY, such a completion must agree with meet-normality on products and with K-NORMALITY on chains. For non-product incomparability, Proposition 2 does not apply. But the independence argument against COMPARABILITY that Goodman and Salow treat as the most powerful concerns orthogonal sources, which is the product case, and they themselves do not think COMPARABILITY fails in the over- and underestimation case (109). The claim that the MARGINS question is independent of the COMPARABILITY question is accordingly restricted to the incomparability that their argument motivates.

## 10. Conclusion

On Goodman and Salow's multi-dimensional account of normality, KM-NORMALITY is i-normality respect by respect, so it delivers in full the independence between orthogonal sources that motivates rejecting COMPARABILITY. K-NORMALITY violates that independence whenever one source fails and another works well. It credits the agent with cliff-edge, Gettier-shaped knowledge about the working source, which she cannot use once she learns that the other source has failed. The KK-friendly theorist can avoid this by adopting meet-normality, which agrees with K-NORMALITY under COMPARABILITY and applies it respect by respect. So, for incomparability of the multi-dimensional kind, whether knowledge has margins is the same question with or without COMPARABILITY, and the abductive link Goodman and Salow suggest does not hold. Combined with the probabilist's single-respect relations, KM-NORMALITY agrees with the probabilist on every single-respect question. The remaining dispute concerns agglomeration across respects, which is where the preface lies.

All formal claims were checked by computer. Theorem 1, Propositions 2 and 3 and the table were checked by exhaustive enumeration over every multi-dimensional structure built from respects of up to three states, two-by-four and two-by-two-by-three structures, and three hundred random four-by-four structures (5,949 in all). Proposition 3(a) was checked over every comparable structure on up to four situations and a sample on five. Corollary 4 was checked on the figure-5 parameters and two hundred random probabilistic models. Theorem 1 was also confirmed with the z3 solver over arbitrary three-by-three structures. These checks support the proofs; they do not replace them.

## References

Carter, Sam, and Simon Goldstein. 2021. "The Normality of Error." *Philosophical Studies* 178: 2509–2533.

Goldstein, Simon, and John Hawthorne. 2022. "Knowledge from Multiple Experiences." *Philosophical Studies* 179: 1341–1372.

Goodman, Jeremy, and Bernhard Salow. 2018. "Taking a Chance on KK." *Philosophical Studies* 175: 183–196.

Goodman, Jeremy, and Bernhard Salow. 2021. "Knowledge from Probability." *Electronic Proceedings in Theoretical Computer Science* 335 (TARK 2021): 171–186.

Goodman, Jeremy, and Bernhard Salow. 2023. "Epistemology Normalized." *The Philosophical Review* 132: 89–145.
