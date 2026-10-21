# Flattening and Counterfactual Independence

**Abstract.** Dorr and Mandelkern have shown that adding Flattening, "if p, then if p and q, r" ≡ "if p and q, r", to Stalnaker's logic C2 yields the logic of ordinal sequence semantics. They report that Flattening appears valid for indicative and subjunctive conditionals alike, and they argue on that basis that it is a better candidate than Import-Export for the logic of "if". I argue that Flattening fails for counterfactuals. In C2 plus either half of Flattening, two purely negative premises, which hold whenever two unrealized possibilities are counterfactually unconnected, entail that had either been realized, its realization would have depended counterfactually on the other's non-realization. Ordinary cases make the premises true and the conclusion false, and the verdict tracks counterfactual dependence, not a similarity metric or an Import-Export intuition. The diagnosis is that Flattening makes supposition cumulative: the scenario a supposition reaches must inherit its counterfactual profile from the starting point, whereas counterfactual independence belongs to the scenario itself. This explains why Dorr and Mandelkern's test pairs feel equivalent, and why, by their own standard, Flattening should not be part of the logic of "if".

## 1. Introduction

Van Fraassen (1976) evaluated conditionals at sequences of worlds: "if p, then q" is true at a sequence if q is true at the first tail of the sequence at which p is true. Dorr and Mandelkern (2026) have determined the logic of this semantics. With sequences of length $\omega$ it is C2.FS: Stalnaker's (1968) logic C2 plus two schemas, Flattening and Sequentiality. With sequences of arbitrary ordinal length it is C2.F, which adds Flattening alone:

$$\text{(Flattening)}\qquad p > (pq > r) \;\leftrightarrow\; pq > r.$$

Dorr and Mandelkern argue that Sequentiality is probably invalid and that Flattening is attractive (2026, §§4.1, 5.2). Their case for Flattening has three parts. First, similarity-based semantics cannot validate it, but that tells against similarity rather than against Flattening. Their counterexample, built on a toy example of Lewis's, is unconvincing: they find it hard to hear a difference between its two sides "except by doggedly holding in mind the Lewisian interpretation" (§4.1, 19–20). Second, pairs of sentences that Flattening makes equivalent do feel equivalent: "We have checked many instances of Flattening, in both the indicative and subjunctive mood, and have not found clear counterexamples." (20). Third, Flattening differs from Import-Export, $p > (q > r) \leftrightarrow pq > r$, of which it is the "cautious" special case. Import-Export has clear subjunctive counterexamples, so a unified theory of "if" should not validate it and should instead explain its indicative appeal by the interaction of "if" with mood. "But matters are different for Flattening, which appears valid for both indicatives and subjunctives." (22). They conclude that C2.F "has strong prima facie appeal as (at least part of) the logic of the natural language conditional" (24). They also record two reservations. Flattening entails the modal schemas 4 and H for the necessity operator defined from the conditional, and both are contested for some readings of that operator (23–24). And no one has an intuitive semantics that explains Flattening's validity: "we leave it as an open problem for proponents of C2.F" (24).

I argue that the second and third parts of the case fail for counterfactuals. *Thesis: Flattening is invalid for counterfactual conditionals, because it requires the scenario reached by a counterfactual supposition to inherit its counterfactual profile from the world at which the supposition is made, while counterfactual independence is a feature of the scenario itself.* I do not claim that Flattening fails for indicatives, nor that sequence semantics is wrong for them. I also leave untouched Dorr and Mandelkern's logical results, which I use throughout.

The contribution relative to their paper has four parts. (i) A counterexample that differs in kind from theirs. It uses no similarity metric, and it lies in the fragment of the language that contains only right-nested conditionals with conditional-free antecedents. That is the fragment in which their own test pairs lie. Their warning signs, 4 and H, become left-nested conditionals once the defined modal operator is unpacked, and they note that such conditionals are hard to assess (§5.2). (ii) A theorem: in C2 plus *either* half of Flattening, two negative counterfactual premises entail a positive claim of counterfactual dependence. A logic without Conditional Excluded Middle does no better. (iii) A diagnosis. I show that Flattening is equivalent to the cumulativity of the supposition that a selection function represents, and that it forces any two worlds to rank alike whatever lies beyond a world both can reach. This explains why their test pairs feel equivalent, why their own counterexample felt weak, and where real counterexamples must be sought. It also gives their open problem a precise form. (iv) A consequence for their argument about the unity of "if". If Flattening fails in the subjunctive, their reasoning about Import-Export applies to Flattening too.

The question matters beyond conditional logic. Flattening is the most cautious step one can take from C2 toward Import-Export, and sequence semantics is a leading way of reconciling conditionals with Stalnaker's Thesis. If even this step separates counterfactuals from indicatives, then the two kinds of supposition differ in how suppositions combine, not only in what they hold fixed. The line falls between supposing from an information state and supposing from a world.

Section 2 sets out the framework. Section 3 gives the case and the theorem. Section 4 gives the diagnosis. Section 5 answers objections, Section 6 discusses indicatives and the unity of "if", and Section 7 concludes.

## 2. Flattening and flat frames

I follow Dorr and Mandelkern's order semantics (2026, §2.1). An order frame assigns each world $w$ a set $R(w)$ of accessible worlds containing $w$, together with a well-order $<_w$ of $R(w)$ in which $w$ comes first. A conditional $p > q$ is true at $w$ iff either $R(w)$ contains no $p$-world, or $q$ is true at the $<_w$-first $p$-world. C2 is sound and complete for these frames (their Theorems 2.4–2.5). I write $f(w,X)$ for the $<_w$-first world of $R(w)$ in the set $X$, and treat "there is none" as a further value, written $\lambda$, with $f(\lambda,X)=\lambda$. C2 contains Conditional Excluded Middle (CEM), $p > q \vee p > \neg q$, and Normality, the rule that from $\vdash (p \wedge q) \to r$ infers $\vdash (s > p) \wedge (s > q) \to s > r$. It also allows substitution of logically equivalent antecedents. Possibility is defined as $\Diamond p := \neg(p > \neg p)$.

Dorr and Mandelkern call the two directions of Flattening *Cautious Importation*, $p > (pq > r) \to pq > r$, and *Cautious Exportation*, $pq > r \to p > (pq > r)$. They note that Flattening can equally be stated as a rule: if $\vdash q \to p$, then $\vdash p > (q > r) \leftrightarrow q > r$ (§4, 18). Several of their natural-language tests use this form, for example "If he had been in France, he'd have had a great time if he had been in the south of France" (20). They prove that Flattening is valid on a frame iff the frame is *flat* (Theorem 4.3). A frame is flat iff it is transitive and, whenever $x$ is accessible from $w$, $<_x$ orders the worlds that come after $x$ in $<_w$ exactly as $<_w$ does. They also prove that C2.F is complete for *linear* frames, in which each world's order is a single master order with that world's predecessors deleted (Theorem 4.5). In sequence semantics the indices are sequences, and a sequence's order is just the rest of the sequence.

In selection terms, flatness says:

$$\text{(Flat)}\qquad f(f(w,Y),X) = f(w,X)\quad\text{whenever } X \subseteq Y.$$

**Observation 1.** Flattening is valid on an order frame iff the frame satisfies (Flat).

*Proof.* Let $Y=[p]$ and $X=[pq]$. The left side of Flattening is true at $w$ iff $r$ holds at $f(f(w,Y),X)$, the right side iff $r$ holds at $f(w,X)$, where $\lambda$ counts as verifying everything. (Flat) makes these the same point. Conversely, if $f(f(w,Y),X) \neq f(w,X)$, let $p$ and $q$ be true exactly on $Y$ and $X$. Let $r$ be false at one of the two points that is a world, and true at the other if it is a world too. Then one side is true at $w$ and the other false. ∎

By Theorem 4.3, (Flat) is therefore equivalent to flatness. I also confirmed this by exhaustive enumeration of all 65,536 order frames on four worlds. Dorr and Mandelkern state the metric version of this condition themselves: "no ordinary metric space has the property that when X ⊆ Y, the closest element of X to a given point is the closest element of X to the closest element of Y to that point" (24). The selection form adds nothing new. I use it because it makes the comparison with supposition in Section 4 direct.

## 3. The Reunion

> *The Reunion.* Ann and Bob studied together and have not been in touch for years. Both missed last Saturday's reunion. Ann has worked in Australia since January and never considered flying back. Bob lives near the venue and meant to come, but his babysitter cancelled that afternoon and he stayed home with his daughter. Neither knew whether the other was coming, and nothing that would have brought one of them would have affected the other.

Write $A$ for "Ann came" and $B$ for "Bob came", read $>$ counterfactually, and evaluate at the actual world. These are true:

(N) $A > \neg B$. Had Ann come, Bob would still have stayed home.

(P) $(A \vee B) > (B \wedge \neg A)$. Had one of them come, it would have been Bob.

(J) $(A \vee B) > (B \wedge (A > B))$. Had one of them come, it would have been Bob, and he would have been there even if Ann had come.

(Poss) $\Diamond A$, $\Diamond(A \vee B)$ and $(A \vee B) > \Diamond A$. Ann could have come, and could still have come had one of them come.

(N) is true because Ann's coming would have done nothing to bring back the babysitter. (P) is true because Bob's coming required only a babysitter who kept her word, whereas Ann's required an intercontinental trip she never considered. (J) is true because, in the scenario where the babysitter keeps her word and Bob comes, Ann's arrival from Australia would have made no difference to his evening.

**Observation 2.** The Reunion falsifies an instance of each half of Flattening, in any logic that allows substitution of equivalent antecedents.

The rule form of Cautious Importation, applied with $\vdash A \to (A \vee B)$, gives $(A \vee B) > (A > B) \to A > B$. By Normality, (J) yields the antecedent. The consequent is false, since $A > B$ and (N) would give $A > \bot$, contrary to $\Diamond A$. The rule form of Cautious Exportation gives $A > \neg B \to (A \vee B) > (A > \neg B)$. The antecedent is (N). The consequent is false: with (J) it would give $(A \vee B) > (A > \bot)$, contrary to $(A \vee B) > \Diamond A$ and $\Diamond(A \vee B)$. Neither argument uses CEM, so the case tells against Flattening in Lewis's (1973) logic VC as much as in C2.

Observation 2 rests on (P) and on a judgment about a nested counterfactual. The next result needs neither. It shows that the failure is systematic and does not depend on which way the outer antecedent would have been realized. Say that, at a world where $B$ and $\neg A$ are true, $B$ *depends counterfactually on* $\neg A$ iff $A > \neg B$ is true there. The other half of the usual definition, $\neg A > B$, is automatic at such a world. Let $X$ be any sentence with $\vdash A \to X$ and $\vdash B \to X$, such as $A \vee B$ or "someone from their year came".

**Theorem 1.** In C2 plus Cautious Importation, and also in C2 plus Cautious Exportation,
$$\neg(A > B),\ \neg(B > A),\ X > (A \vee B)\ \vdash\ X > \big[(A \wedge (B > \neg A)) \vee (B \wedge (A > \neg B))\big]. \qquad \text{(D)}$$

*Proof.* With Cautious Exportation: by CEM, $\neg(A > B)$ gives $A > \neg B$, and the rule form with $\vdash A \to X$ gives $X > (A > \neg B)$. Likewise $X > (B > \neg A)$. Normality combines these with $X > (A \vee B)$ into $X > [(A \vee B) \wedge (A > \neg B) \wedge (B > \neg A)]$, which entails the conclusion by Normality. With Cautious Importation: the rule form gives $X > (A > B) \to A > B$, so $\neg(A > B)$ yields $\neg(X > (A > B))$. By CEM this is $X > \neg(A > B)$, and since $\neg(A > B) \to A > \neg B$ is a theorem of C2, Normality gives $X > (A > \neg B)$. The rest is as before. ∎

When $X$ is $A \vee B$, the third premise is an instance of Identity. The derivation follows the pattern of Dorr and Mandelkern's derivation of H (§4, 18–19): suppose the disjunction, then use one half of Flattening to carry facts about the disjuncts into the disjunctive scenario. I checked Theorem 1 semantically with the Z3 solver. On every order frame with at most five worlds that satisfies their frame condition for either half (their Lemma 4.2 and note 24), the premises together with the negation of the conclusion are unsatisfiable. On unrestricted order frames they are satisfiable.

Read with the definition above, (D) says that had $X$ been the case, one of the two would have come, and whichever came would have come only because the other stayed away. The premises are purely negative. They deny that either arrival would have brought the other, and they hold for any pair of unrealized possibilities that are counterfactually unconnected. Such pairs are everywhere: my drinking tea this morning and a stranger in Lima buying an umbrella. Given C2, either half of Flattening converts this absence of connection into a counterfactual dependence that holds in whichever scenario realizes the disjunction. In the Reunion, (D) is false however the disjunction would have been realized. If Bob came, Ann's coming would not have kept him away. If Ann came, Bob's coming would not have kept her away.

One worry is that the felt falsity of (D) is an Import-Export intuition in disguise. By Import-Export, $B > (A > \neg B)$ is equivalent to $AB > \neg B$, so a conjunct like $B \wedge (A > \neg B)$ would sound defective whatever the facts about dependence. A control case rules this out.

> *Avoidance.* As in the Reunion, except that Bob has long avoided Ann. Had he come and learned that she was coming, he would have stayed home.

Here (N), $\neg(A > B)$ and $\neg(B > A)$ remain true, and (D) is now true: had one of them come, it would have been Bob, and his coming would have depended on Ann's staying away. The counterfactual verdict on (D) changes with the facts about dependence and with nothing else. In explicit four-world C2 models with selection set by weighted counts of departures, I computed that the Reunion makes (N), (P), (J), $\neg(A > B)$ and $\neg(B > A)$ true and (D) false, while the Avoidance model makes the same negative premises true and (D) true. An intuition driven by Import-Export would not discriminate between the cases. The intuition about counterfactual dependence does.

## 4. Diagnosis: cumulative supposition and inherited profiles

### 4.1 Flattening as cumulativity

Let $W$ be finite and $Pr$ a probability function on $W \cup \{\lambda\}$. *Imaging* $Pr$ on $X$ moves each point's probability to the point selected from it: $Pr^X(u) = \sum_{w:\, f(w,X)=u} Pr(w)$. Lewis (1976) introduced imaging as the operation under which the probability of a Stalnaker conditional equals the imaged probability of its consequent. Here $Pr(X > \varphi) = Pr^X([\varphi] \cup \{\lambda\})$, and $Pr(Y > (X > \varphi))$ is computed by imaging on $Y$ and then on $X$. Conditioning is the standard model of supposing that something is in fact the case, and imaging the standard model of supposing that it had been the case (see Eva, Shear and Fitelson 2022 for a comparison of these and other approaches). Call a supposition operation *cumulative* if supposing $Y$ and then some $X \subseteq Y$ gives the same result as supposing $X$ outright. Conditioning is cumulative, since $Pr(\cdot \mid Y)$ conditioned on $X \subseteq Y$ is $Pr(\cdot \mid X)$.

**Proposition 3.** On a finite order frame, Flattening is valid iff imaging is cumulative for every probability function.

*Proof.* Given (Flat), $(Pr^Y)^X(u) = \sum_{w:\, f(f(w,Y),X)=u} Pr(w) = Pr^X(u)$. Conversely, a point mass on $w$ is sent to $f(f(w,Y),X)$ by the first operation and to $f(w,X)$ by the second, so cumulativity for point masses is (Flat). Observation 1 completes the proof. ∎

The proof is short. Its interest lies in what it identifies. The intuitive semantics that Dorr and Mandelkern ask proponents of C2.F to supply must be a semantics of cumulative supposition. Conditioning is one, but it does not select a single world. Selection semantics can be cumulative only if the index reached by a supposition carries forward the standpoint from which the supposition was made. Linear frames and sequences do exactly that. In a linear frame the selected world's order is the master order with its predecessors deleted. In a sequence model the selected tail's order is the remainder of the original sequence. Either way, what the reached index would select under further suppositions is a residue of the starting point's ranking.

### 4.2 Agreement

Flatness also has a consequence that does not mention nesting.

**Corollary (Agreement).** In a flat frame, if $v$ is accessible from both $w_1$ and $w_2$, then $<_{w_1}$ and $<_{w_2}$ order alike any two worlds that both place after $v$.

*Proof.* If $v <_{w_1} y <_{w_1} z$ and $v <_{w_2} z <_{w_2} y$, flatness requires both $y <_v z$ and $z <_v y$. (If $v$ is $w_1$ or $w_2$, the argument is shorter.) ∎

I verified Agreement on all flat frames with at most five worlds. Dorr and Mandelkern's metric remark is one instance of it, but Agreement applies to any family of world-relative rankings, metric or not. Now suppose that a world's counterfactual ranking is fixed by that world: by its laws, its history and what it holds fixed. Then Agreement fails for counterfactuals wherever two worlds that can both reach a third hold fixed different things about what lies beyond it. In the Reunion, let $w$ be actuality and $v$ the scenario in which Bob came. Beyond $v$, actuality ranks the Ann-alone world ahead of the world where both came, because Bob's staying home is held fixed. From $v$, the order is reversed, because there Bob's coming is held fixed. No flat frame contains both worlds with these rankings. Theorem 1 is the object-language expression of this fact.

### 4.3 Why the test pairs pass

The diagnosis predicts when Flattening's two sides come apart. Let $v$ be the scenario selected for the outer antecedent $p$. The two sides diverge only if the first $pq$-scenario reached from $v$ differs, on the matter $r$ concerns, from the first $pq$-scenario reached from the actual world. For a counterfactual supposition that requires three things. (a) The outer antecedent can be realized in several ways. (b) The way $v$ realizes it settles a matter $M$ that the inner antecedent leaves alone, so that supposing $pq$ from inside $v$ keeps $M$. (c) The consequent concerns $M$, and supposing $pq$ directly settles $M$ differently.

Dorr and Mandelkern's pairs fail (b) or (c). In "If he had gotten an espresso, then he would have had a fit if he'd gotten an overextracted one" (20), the consequent concerns the effect of the overextracted espresso, which the inner antecedent fixes however the outer one is realized. The same holds for the south of France, the conflagration at the party and the soaked match. Their line example fails (b). There the length of 11 inches that realizes the outer antecedent is not kept by the inner supposition; the counterexample comes only from the fact that 13 inches is nearer to 11 than 8 is, while 8 is nearer to 10. That is why it is hard to hear and why they were right to be unmoved by it. The Reunion meets all three conditions. The outer antecedent can be realized by Bob or by Ann, the selected realization settles Bob's presence, the inner supposition of Ann's arrival leaves Bob's presence alone, and the consequent concerns it.

Interventionist semantics bears this out. In structural-equation models (Galles and Pearl 1998; Halpern 2000; Briggs 2012), an antecedent that sets a set of variables $S$ to values is evaluated by replacing their equations with constants. Intervening on $S$ and then on a superset $S \cup T$ yields the same model as intervening on $S \cup T$ directly. So Flattening holds whenever both antecedents are conjunctions of variable settings, and condition (a) fails. This is why spot checks with simple antecedents find no counterexamples. The counterexamples come from antecedents that, like "one of them came", can be realized in more than one way.

## 5. Objections and replies

### 5.1 The sequence theorist's reply

The strongest reply comes from sequence semantics itself. There the points of evaluation are sequences, and conditional-free sentences are settled by a sequence's first member. Two indices can therefore agree on every categorical fact and still differ on conditionals. Dorr and Mandelkern describe, without endorsing, a metaphysical gloss on which categorical propositions answer "factual" questions and conditionals typically answer "non-factual" ones (2026, §3, 13). On this view (J) may be true of the Bob scenario taken as actual and still be false at the index that the supposition "had one of them come" reaches. That index shares the scenario's categorical facts but carries the remainder of the actual world's ranking. So, the reply goes, (D) is true at the index that matters, and our contrary judgment evaluates a different index.

I grant that sequence semantics can model the Reunion this way. The question is whether counterfactuals can be like this. Three considerations say they cannot.

First, the judgment behind (J) follows from a principle that any non-backtracking theory of counterfactuals accepts:

(Independence) If at a scenario $s$, $B$ is true, $A$ is possible, and nothing in $s$ connects whether $A$ to whether $B$ (no causal path, no common cause that settles both, no law or logical constraint linking them), then $A > B$ is true at $s$.

The reply must deny Independence for indices reached by supposition while keeping it for scenarios taken as actual. Independence is stated in terms of what the scenario contains: its laws, its causal structure and its particular facts. An index reached by supposition contains exactly what the scenario contains. To deny Independence there is to hold that whether Bob's coming depended on Ann's absence is not settled by anything in the scenario where Bob came. It is settled by the route by which that scenario was reached.

Second, this route-relativity has a cost specific to counterfactuals. Counterfactual dependence is the relation that counterfactual approaches to causation and interventionist models of causal reasoning use to track what makes a difference to what. In a structural-equation model of the Bob scenario, Bob's variable is fixed by his babysitter's, and intervening on Ann's variable leaves it unchanged. That verdict is computed from the model, that is, from the scenario's own causal structure, and it does not change with the supposition through which the scenario was entered. A semantics on which "had one of them come, Bob's coming would have depended on Ann's absence" is true has made counterfactual dependence vary with route while the causal facts stay the same. For indicatives this kind of route-relativity is natural, as Section 6 notes, because what an indicative supposition reaches is an information state rather than a world.

Third, consider the following case, where the facts leave no room for doubt.

> *The Buttons.* At noon, Ann in Sydney and Bob in London could each have pressed a button. Each hesitated at the last instant and did not. The world is deterministic, and nothing that happened in either city in the final instant before noon could affect the other city at noon, since no signal could cover the distance in time.

A counterfactual departure confined to Ann's last instant leaves London at noon exactly as it actually was, and likewise with the cities reversed. So $\neg(A > B)$ and $\neg(B > A)$ hold, and this follows on a miracle-based similarity theory of the kind Lewis (1979) proposed as much as on interventionist views. The case is symmetric, so it is unclear which of them would have pressed had one of them pressed. Theorem 1 does not need to know. On either realization, (D) requires one press to depend counterfactually on the other's absence across a distance that no influence could cross under deterministic laws. The C2 theorist who treats the choice of realization as indeterminate gains nothing, since (D) fails on every resolution. I checked both tie-breakings explicitly. Independence is also weaker than the general supervenience of counterfactuals on categorical facts, which CEM theorists may doubt for symmetric cases like this one. It concerns only counterfactuals whose verdict is the same on every candidate selection.

Finally, the reply cannot fall back on doubts about nested judgments. Dorr and Mandelkern's positive evidence for Flattening consists of judgments about nested conditionals with entailing antecedents (§4.1). If such judgments are unreliable, the case for Flattening loses its support too.

### 5.2 Context shift

One might hold that the outer antecedent of (J) makes Bob's arrival salient, and that this shifts the selection function used for the inner counterfactual. Flattening concerns a single interpretation, so on this view there is no counterexample. But the premises and the denial of (D) can be asserted together without any felt shift: "Had Ann come, Bob would still have stayed home; but had one of them come, it would have been Bob, and he would have been there even if Ann had turned up." A shift posited just where conditions (a)–(c) of Section 4.3 hold, and nowhere else, redescribes the counterexample rather than explaining it away. It also concedes that the conditional as interpreted in context does not obey Flattening, which is the question.

### 5.3 Disjunctive antecedents

Many hear "had Ann or Bob come" as "had Ann come, and had Bob come". On that reading (P) and (J) are false, since one of the scenarios considered is Ann's. Three replies. First, this simplification together with the substitution of equivalent antecedents, which C2 and every normal conditional logic contain, yields antecedent strengthening (Ellis, Jackson and Pargetter 1977). A proponent of C2.F cannot appeal to it. Second, selectional readings are well attested. McKay and van Inwagen's (1977) Spain example is a standard case against the simplification, and Ramotowska et al. (2025) report experimental evidence favoring selectional semantics. Third, Theorem 1 needs neither (P) nor an overt disjunction. Its outer antecedent can be any $X$ entailed by both $A$ and $B$ such that, had $X$ been true, one of them would have come. "Had someone from their year come", where Ann and Bob were the only members of their year, will do. Finally, even on a universal reading of the disjunction, the Cautious Exportation instance of Observation 2 fails. The Bob scenario is among those considered, and in it Bob would still have come had Ann come, so $(A \vee B) > (A > \neg B)$ is false while $A > \neg B$ is true.

### 5.4 Hyperintensional antecedents

Truthmaker and alternative-sensitive semantics deny that logically equivalent antecedents can be substituted for one another (Fine 2012; Santorio 2018). Ciardelli, Zhang and Champollion (2018) report that antecedents with the same truth conditions make different contributions in a two-switch scenario. Such a theorist may refuse to identify $(A \vee B) \wedge A$ with $A$. But C2.F allows the substitution, and its rule form, the form used in Dorr and Mandelkern's tests, needs only that the inner antecedent entail the outer. The existential version has no disjunction to individuate. And the diagnosis does not depend on how antecedents are individuated. However "had someone from their year come" is realized, the inner supposition "had Ann come", made from inside a scenario in which Bob came, keeps Bob there.

### 5.5 Chance and counterfactual skepticism

In C2, $\neg(A > B)$ is equivalent to $A > \neg B$ when $A$ is possible. Some deny "would" counterfactuals whenever chance intervenes between antecedent and consequent. Goodsell (2022), discussing Morgenbesser's coin, argues against inferring counterfactual independence from causal independence. A C2 theorist moved by such views might deny (N) on the ground that Bob's babysitter's cancellation is chancy and a world in which Ann flew in would have diverged weeks earlier. The Buttons involve no chance and no inference from causal to counterfactual independence. Their counterfactual independence follows from determinism and the locality of the laws.

## 6. Indicatives and the unity of "if"

Theorem 1 is a theorem of C2.F. It holds for any conditional that obeys C2 and either half of Flattening, indicatives included. Does the Reunion therefore tell against Flattening for indicatives too? I think not, for a reason the Avoidance control brings out. Take the indicative counterpart of (D): "If one of them came, then whichever came is such that if the other came, they didn't". Under the supposition that Bob came, "if Ann came, Bob didn't" sounds wrong whether or not Bob avoids Ann, because given that Bob came, if Ann came then both did. That is the Import-Export pattern again, and it does not track dependence. Every theorist who accepts C2 must already explain away this pattern. Dorr and Mandelkern report that adding Import-Export to C2 collapses the conditional into the material conditional (§4.1, 21–22), and they note that one error theory of Import-Export's appeal relies in part on Flattening (22). So the indicative instance gives no independent evidence about Flattening, and the counterfactual argument does not transfer.

The diagnosis of Section 4 explains why indicatives might be different. On restrictor views, if-clauses restrict a modal base (Kratzer 2012), and successive restrictions by $p$ and then by $pq$ amount to restriction by $pq$. On views built around Stalnaker's (1970) Thesis, the probability of an indicative conditional is a conditional probability, so indicative supposition is modeled by conditioning, which is cumulative. Dorr and Mandelkern already show that in any model satisfying their restricted form of the Thesis with background conditions, the two sides of a Flattening instance of the relevant form receive the same probability, $\pi(r \mid pq)$, provided $pq$ has positive probability (§7, note 36). They add that there is no obvious route from any consistent restriction of the Thesis to the claim that Flattening's instances have probability one. I add nothing to that result. The point here is interpretive. An indicative supposition reaches an information state, and a further supposition refines that state. So the information-relative "index" behaves like a tail of a sequence and carries the starting standpoint forward. That is the intuitive semantics their open problem asks for, available for indicatives and unavailable for counterfactuals.

This bears on their argument about the unity of "if". They reject Import-Export as part of the logic of "if" because it fails for subjunctives. They then explain its indicative appeal by the interaction of "if" with mood, and they exempt Flattening because it "appears valid for both" moods (22). If the argument above is right, Flattening fails for subjunctives, and the same reasoning applies. A unified "if" should not validate Flattening. Its indicative appeal, if it is real, should come from what the indicative mood contributes, for instance supposition that refines an information state, rather than from the logic of "if". This leaves two options for a proponent of C2.F. One can restrict C2.F to indicatives and explain it by cumulative, information-relative supposition. Or one can give up Flattening for "if" and explain its indicative appearances. I do not choose between them. Either way, Dorr and Mandelkern's model theory keeps its interest, but its application is limited to indicatives.

## 7. Conclusion

I have shown that in C2 plus either half of Flattening, two negative counterfactual premises entail a claim of counterfactual dependence, (D), and that (D) is false in ordinary cases of counterfactual independence. In a matched case where the dependence is real, (D) is true. Each half of Flattening fails in the Reunion with or without CEM. Flattening is equivalent to the cumulativity of imaging, and it forces any two worlds to rank alike whatever lies beyond a world both can reach. Its failures for counterfactuals require an outer antecedent whose realization settles a matter that the inner supposition leaves alone, which explains why the test pairs in the literature pass.

I have not shown that Flattening is valid for indicatives, nor refuted sequence semantics as a theory of them. What follows is that the most cautious fragment of Import-Export already separates counterfactual from indicative conditionals. Supposition made from a world keeps the scenario it reaches, and supposition made from an information state does not commit to one. A logic of "if" that is meant to cover both moods should not contain Flattening.

## References

Briggs, Rachael. 2012. "Interventionist Counterfactuals." *Philosophical Studies* 160: 139–166. https://doi.org/10.1007/s11098-012-9908-5

Ciardelli, Ivano, Linmin Zhang, and Lucas Champollion. 2018. "Two Switches in the Theory of Counterfactuals." *Linguistics and Philosophy* 41: 577–621. https://doi.org/10.1007/s10988-018-9232-4

Dorr, Cian, and Matthew Mandelkern. 2026. "Sequence and Consequence." *Philosophical Logic* 1. https://doi.org/10.16995/phil-log.27646. Page references are to arXiv:2411.16994v2.

Ellis, Brian, Frank Jackson, and Robert Pargetter. 1977. "An Objection to Possible-World Semantics for Counterfactual Logics." *Journal of Philosophical Logic* 6: 355–357. https://doi.org/10.1007/BF00262069

Eva, Benjamin, Ted Shear, and Branden Fitelson. 2022. "Four Approaches to Supposition." *Ergo* 8. https://doi.org/10.3998/ergo.2227

Fine, Kit. 2012. "Counterfactuals without Possible Worlds." *The Journal of Philosophy* 109: 221–246. https://doi.org/10.5840/jphil201210938

Galles, David, and Judea Pearl. 1998. "An Axiomatic Characterization of Causal Counterfactuals." *Foundations of Science* 3: 151–182. https://doi.org/10.1023/A:1009602825894

Goodsell, Zachary. 2022. "Tossing Morgenbesser's Coin." *Analysis* 82: 214–221. https://doi.org/10.1093/analys/anab091

Halpern, Joseph Y. 2000. "Axiomatizing Causal Reasoning." *Journal of Artificial Intelligence Research* 12: 317–337. https://doi.org/10.1613/jair.648

Kratzer, Angelika. 2012. *Modals and Conditionals: New and Revised Perspectives*. Oxford: Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199234684.001.0001

Lewis, David. 1973. *Counterfactuals*. Oxford: Blackwell.

Lewis, David. 1976. "Probabilities of Conditionals and Conditional Probabilities." *The Philosophical Review* 85. https://doi.org/10.2307/2184045

Lewis, David. 1979. "Counterfactual Dependence and Time's Arrow." *Noûs* 13: 455–476. https://doi.org/10.2307/2215339

McKay, Thomas, and Peter van Inwagen. 1977. "Counterfactuals with Disjunctive Antecedents." *Philosophical Studies* 31: 353–356. https://doi.org/10.1007/BF01873862

Ramotowska, Sonia, Paul Marty, Jacopo Romoli, and Paolo Santorio. 2025. "Counterfactuals and Quantificational Force: Experimental Evidence for Selectional Semantics." *Semantics and Pragmatics* 18: 1–43. https://doi.org/10.3765/sp.18.6

Santorio, Paolo. 2018. "Alternatives and Truthmakers in Conditional Semantics." *The Journal of Philosophy* 115: 513–549. https://doi.org/10.5840/jphil20181151030

Stalnaker, Robert C. 1968. "A Theory of Conditionals." In *Studies in Logical Theory*, American Philosophical Quarterly Monograph 2.

Stalnaker, Robert C. 1970. "Probability and Conditionals." *Philosophy of Science* 37: 64–80. https://doi.org/10.1086/288280

van Fraassen, Bas C. 1976. "Probabilities of Conditionals." In *Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science*, vol. I, 261–308. https://doi.org/10.1007/978-94-010-1853-1_10
