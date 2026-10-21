# Flattening and Counterfactual Independence

**Abstract.** Dorr and Mandelkern have shown that adding Flattening, "if p, then if p and q, r" ≡ "if p and q, r", to Stalnaker's logic C2 yields the logic of ordinal sequence semantics. They argue that Flattening, unlike Import-Export, appears valid in both moods. I argue that it fails for counterfactuals. Take two cases that agree on every unnested counterfactual about who came to a reunion and differ only in whether one guest's coming would have depended on another's absence. A bare nested counterfactual is true in one and false in the other; its Flattening partner is false in both. Exclusive, additive and universal construals of the antecedents all predict no difference between the cases, so the contrast rules them out. A shift of interpretation that persists through discourse fails a simple test. A shift confined to the embedded position is just the interpretation that nested counterfactuals receive, and Flattening is false of it. The cases also explain why Dorr and Mandelkern's test pairs pass. By their own reasoning about Import-Export, Flattening should not be part of the logic of "if".

## 1. Introduction

Van Fraassen (1976) evaluated conditionals at sequences of worlds: "if p, then q" is true at a sequence iff q is true at the first tail of the sequence at which p is true. Dorr and Mandelkern (2026) have determined the logic of this semantics. With sequences of length $\omega$ it is C2.FS, Stalnaker's (1968) logic C2 plus two schemas, Flattening and Sequentiality. With sequences of arbitrary ordinal length it is C2.F, which adds Flattening alone:

$$\text{(Flattening)}\qquad p > (pq > r) \;\leftrightarrow\; pq > r.$$

They argue that Sequentiality is probably invalid and that Flattening has strong prima facie appeal. Their case has four strands.

*Similarity.* Similarity semantics cannot validate Flattening, but that tells against similarity, not against Flattening. Their own counterexample, built on a toy example of Lewis's, is hard to hear "except by doggedly holding in mind the Lewisian interpretation" (2026, 19–20).

*Test pairs.* Sentences that Flattening makes equivalent feel equivalent. At most the nested member feels redundant: "the first antecedent feels like it's doing nothing", which validity would explain (20). "We have checked many instances of Flattening, in both the indicative and subjunctive mood, and have not found clear counterexamples." (20). Felt inequivalences that come from re-indexing tense or anaphora do not count, since parallel pairs would refute Contraction too (20–21).

*Import-Export.* Import-Export, $p > (q > r) \leftrightarrow pq > r$, collapses C2 into the material conditional, as they report from earlier work (21), and it has subjunctive counterexamples. So a unified theory of "if" should not validate it, and should explain its indicative appeal by the interaction of "if" with mood. "But matters are different for Flattening, which appears valid for both indicatives and subjunctives." (22).

*Cautious cousins.* Cautious Monotonicity and Cautious Transitivity are theorems of C2, while their incautious versions yield the material conditional. By analogy, "we might naturally regard Flattening as a plausible cautious cousin of the implausible, incautious Import-Export principle" (23).

They conclude that C2.F has "strong prima facie appeal as (at least part of) the logic of the natural language conditional" (24). They record two reservations. Flattening yields the modal schemas 4 and H for the necessity operator defined from the conditional, and both schemas are contested (23–24). And no one has an intuitive semantics that explains Flattening's validity: "we leave it as an open problem for proponents of C2.F" (24).

I argue that Flattening is not valid for counterfactuals. *Thesis: two cases that agree on every unnested counterfactual about the relevant events, and differ only in counterfactual dependence, give a bare nested counterfactual different truth values while its Flattening partner keeps one; so Flattening fails for the counterfactual as English nested counterfactuals are interpreted, and the only interpretation that would save it is one those sentences never receive.* The argument rests on judgments about four sentences, which I report and which can be tested. I do not claim that Flattening fails for indicatives. I leave 4 and H open. I use Dorr and Mandelkern's logical results throughout.

The method needs one preliminary. Section 2 notes that C2.F adds nothing to C2 in its unnested fragment, probabilities included. So any case for or against Flattening, theirs or mine, must rest on judgments about nested conditionals. The live questions are whether those judgments are bare or enriched with particles such as "still" or "even", and whether one interpretation is held fixed across them.

Dorr and Mandelkern give one counterfactual counterexample, which depends on a similarity metric, and they find it weak. The increment of this paper is as follows. (i) A counterexample of a different kind. It is a bare instance of the rule form of Flattening, in the right-nested fragment with conditional-free antecedents where their test pairs lie, and it is driven by counterfactual independence rather than by a metric. A matched control fixes which reading carries the verdict. (ii) An argument that the principle cannot be saved by a shift of context. (iii) An explanation of why their subjunctive test pairs pass, and why their redundancy datum and cautious-cousin analogy do not tell between Flattening and its denial. (iv) The consequence that their own argument about Import-Export applies to Flattening. Two further observations are small: the conservativity point above, and the fact that the cases leave C2 plus both "crashing" halves of Flattening untouched. Several formal facts I use are reformulations of their results, and I credit them as such.

For readers outside conditional logic, the stake is this. Flattening looked like the safe part of Import-Export, the principle that supposing $p$ and then a strengthening of $p$ comes to the same as supposing the strengthening outright. If it fails for counterfactuals, then counterfactual and indicative "if" differ in how suppositions combine. A counterfactual supposition made inside a supposed scenario answers to that scenario's own dependencies. That matters to anyone who reasons with nested counterfactuals about causal structure.

Section 2 sets out the framework. Section 3 gives the minimal pair and its control, and Section 4 the deterministic case and a general theorem. Section 5 answers objections. Section 6 explains the test pairs, and Section 7 draws the consequences for the logic of "if".

## 2. Framework

I follow Dorr and Mandelkern's order semantics (2026, §2.1). An order frame assigns each world $w$ a set $R(w)$ of accessible worlds containing $w$, together with a well-order $<_w$ of $R(w)$ in which $w$ comes first. $p > q$ is true at $w$ iff either $R(w)$ contains no $p$-world or $q$ is true at the $<_w$-first $p$-world. C2 is sound and complete for these frames (their Theorems 2.4–2.5). It contains Conditional Excluded Middle (CEM), $p > q \vee p > \neg q$, and Normality. Possibility is defined by $\Diamond p := \neg(p > \neg p)$. I write $f(w,X)$ for the $<_w$-first world of $R(w)$ in $X$.

The two directions of Flattening are *Cautious Importation*, $p > (pq > r) \to pq > r$, and *Cautious Exportation*, $pq > r \to p > (pq > r)$. Their special cases with $r = \bot$ are *Crashing* Cautious Importation and *Crashing* Cautious Exportation. In C2 the latter is equivalent to 4, and the former yields H (§4, 18–19). Flattening also has a rule form: if $\vdash q \to p$, then $\vdash p > (q > r) \leftrightarrow q > r$ (18). Flattening is valid on a frame iff the frame is *flat*: transitive, and such that whenever $x$ is accessible from $w$, $<_x$ orders the worlds after $x$ in $<_w$ as $<_w$ does (Theorem 4.3). In selection terms this is

$$\text{(Flat)}\qquad f(f(w,Y),X) = f(w,X)\quad\text{whenever } X \subseteq Y,$$

which is their condition restated, and which they state themselves for metric spaces (24). C2.F is also complete for *linear* frames, where each world's order is a "single master order" with that world's predecessors deleted (Theorem 4.5; 27). In sequence semantics a tail's order is the rest of the sequence.

**Observation 1.** Call a conditional *first-degree* if its antecedent and consequent contain no conditionals. If a Boolean combination of first-degree conditionals is true at a world of some order model, it is true at a world of some linear order model. Any probability assignment to such sentences that some probabilistic order model realizes is also realized by a flat one.

*Proof.* A first-degree sentence's truth value at $w$ depends only on $<_w$ and the valuation. Form a master order by listing the worlds outside $R(w)$ and then $R(w)$ in the order $<_w$, and let each world's order be the master order from that world on. The resulting frame is linear, and $w$ keeps its order. For probabilities, take one such linearization for each world $w$, form their disjoint union (which is flat), and give the copy of $w$ at the head of its own linearization the probability $w$ had. ∎

So data about unnested counterfactuals, whether categorical or probabilistic, cannot tell against Flattening without telling against C2. They cannot tell in its favor either. (I checked the construction exhaustively on three-world frames and on random four-world frames.)

## 3. A bare minimal pair

> *The Reunion.* Ann and Bob studied together and have not been in touch for years. Both missed last Saturday's reunion. Ann has worked in Australia since January and never considered flying back. Bob lives near the venue and meant to come, but his babysitter cancelled that afternoon. Nothing that would have brought either of them would have affected the other.

> *Avoidance.* As in the Reunion, except that Bob has avoided Ann for years. The organizers posted the list of guests in advance, and Bob checked it. Had her name been on it, he would have stayed home.

Consider:

(1) If at least one of them had come, then if Ann had come, Bob would have been there.

(2) If Ann had come, Bob would have been there.

With $A$ for "Ann came" and $B$ for "Bob came", (1) is $(A \vee B) > (A > B)$ and (2) is $A > B$. Since $\vdash A \to (A \vee B)$, the rule form of Flattening makes them equivalent. Each direction of the biconditional is an instance of one half of Flattening. The sentences contain no "still", "even" or "too". The outer antecedent says "at least one", which has the truth conditions of the inclusive disjunction "Ann or Bob or both", so the formal instance has exactly that antecedent.

The judgments are these. (2) is false in both cases: had Ann come, Bob's babysitter would still have cancelled. In both cases, had at least one of them come, it would have been Bob, since his coming needed only a babysitter who kept her word while Ann's needed an intercontinental trip she never considered. In the Reunion, (1) is true: had Bob come, Ann's turning up as well would have changed nothing for him. In Avoidance, (1) is false: had Bob come, Ann's name on the list would have kept him at home. The argument is then:

(P1) (2) is false in the Reunion and false in Avoidance.

(P2) (1) is true in the Reunion and false in Avoidance.

(P3) Under any single interpretation of the sentences on which Flattening is valid, (1) and (2) have the same truth value in each case.

(C) So either Flattening fails under the interpretation on which (P1) and (P2) are correct, or in the Reunion (1) and (2) are not interpreted by a single interpretation.

(P3) is the rule form. The weight falls on (P2) and on the second disjunct of (C), which I take up in Section 5.1.

The control does a specific job. It does not show that the Reunion verdict is right. It identifies which reading of (1) carries the verdict. The two cases agree on every unnested counterfactual about who came. In both, the possibilities rank in the same order from actuality: neither came, then Bob alone, then Ann alone, then both. Now consider the readings a defender of Flattening might offer. On the *exclusive* reading, "if Ann had come" means "if it had been Ann (rather than Bob)", that is, $A \wedge \neg B$. On the *additive* reading it means "if Ann had come as well", that is, $A \wedge B$. Each of these entails $A \vee B$. So under Flattening, (1) on either reading reduces to an unnested counterfactual, and that counterfactual has the same value in both cases. This holds for every construal of the inner antecedent that entails the outer one. The same is true without Flattening: on the exclusive reading (1) is false in both cases, and on the additive reading it is true in both. On the universal reading of the outer antecedent ("whichever of them had come"), (1) is false in both, because if Ann had been the one to come, Bob would not have been there.

Only one reading yields the contrast. On it, the outer antecedent selects the scenario in which Bob came, and "if Ann had come" is then evaluated from that scenario according to what depends on what there. Flattening fails on that reading. I computed every one of these predictions in explicit four-world models. Dorr and Mandelkern's tense and anaphora pairs involve re-indexing of this kind: the inner occurrence of an expression is construed differently from the outer one. Re-indexing is triggered by linguistic form. Here it would be the same in both cases, since the cases share every word, and so it cannot produce a contrast between them.

Is (P2) right? The Avoidance verdict is the one Flattening predicts, so the question is the Reunion verdict. Given CEM, a proponent of C2.F must hold that in the Reunion this is true: "If at least one of them had come, then if Ann had come, Bob would not have been there." That says that in the scenario where the babysitter kept her word and Bob came, Ann's arrival from Australia would have kept him away. Nothing in the case supports that, and in Avoidance the corresponding sentence is true precisely because something does. The judgments are mine, and they are testable. A two-by-two design that crosses case (Reunion or Avoidance) with sentence ((1) or (2)) separates the hypotheses. Flattening predicts no interaction. I predict that (1) changes value across the cases while (2) does not. A Contraction row, "If Ann had come, then if Ann had come, Bob would have been there", should pattern with (2) in both cases, as C2 requires. That row checks that nesting by itself does not produce the effect.

## 4. Locality and a general form

The Reunion relies on judgments about a babysitter and a trip. The next case puts the inner judgment on a different footing.

> *The Buttons.* At noon, Ann in Sydney and Bob in London could each have pressed a button. Neither did. Ann's finger was already moving and she pulled back at the last instant; Bob had firmly decided not to. The world is deterministic, and nothing that happened in either city in the final instant before noon could affect the other city at noon, since no signal could cover the distance in time.

(3) If at least one of them had pressed, then if Bob had pressed, Ann would have pressed.

(4) If Bob had pressed, Ann would have pressed.

The pair is an instance of the rule form, since $\vdash B \to (A \vee B)$. Had at least one of them pressed, it would have been Ann, whose press needed only a smaller departure from actuality. (4) is false: a departure confined to Bob's last instant leaves Sydney at noon as it actually was. For the same reason (3) is true. From the scenario in which Ann pressed, a departure confined to Bob's last instant leaves Ann's press in place. Both verdicts follow from one principle, applied once at actuality and once at the scenario the outer antecedent reaches:

(Locality) At a world with deterministic laws under which no influence travels faster than light, the supposition that a local event had occurred, realized by a departure confined to that event's immediate past, leaves unchanged every region that no influence from that past could reach.

Locality holds on a miracle-based similarity theory of the kind Lewis (1979) proposed, and it holds on interventionist views. The Buttons involve no chance, so they are not touched by doubts about "would" counterfactuals with chancy consequents.

Suppose instead that the case is symmetric, so that it is unsettled which of them would have pressed. Then the following result applies.

**Theorem 1.** Let $X$ be any sentence with $\vdash A \to X$ and $\vdash B \to X$. In C2 plus Cautious Importation, and also in C2 plus Cautious Exportation,
$$\neg(A > B),\ \neg(B > A),\ X > (A \vee B)\ \vdash\ X > \big[(A \wedge (B > \neg A)) \vee (B \wedge (A > \neg B))\big]. \qquad \text{(D)}$$

*Proof.* With Cautious Exportation: CEM turns $\neg(A > B)$ into $A > \neg B$, and the rule form gives $X > (A > \neg B)$. Likewise $X > (B > \neg A)$, and Normality combines these with $X > (A \vee B)$. With Cautious Importation: the rule form gives $X > (A > B) \to A > B$, so $X > \neg(A > B)$ follows by CEM, and then $X > (A > \neg B)$ by Normality. The rest is as before. ∎

The proof follows Dorr and Mandelkern's derivation of H (18–19), and it uses CEM essentially. In C2, given $\Diamond A$, the premise $\neg(A > B)$ is equivalent to $A > \neg B$, so the premises are ordinary would-nots. The theorem shows that whichever way the tie is resolved, Flattening carries the actual world's would-nots into the supposed scenario. On either resolution, one of two bare instances of the shape of (3)–(4) fails. Using this against Flattening still requires judging the nested conclusion (D) false in the symmetric Buttons. That judgment is again Locality, applied at the scenario reached. (D) is true in Avoidance, as it should be. I checked Theorem 1 with the Z3 solver on every order frame with at most five worlds that satisfies Dorr and Mandelkern's frame condition for either half (Lemma 4.2 and note 24).

## 5. Objections and replies

### 5.1 A shift of context

The defender's first move is to say that Flattening, like Contraction, concerns a single interpretation, and that the outer antecedent of (1) shifts the interpretation of the inner conditional. Then (1) and (2) would not form an instance.

Context shifts in counterfactual discourse are well studied. On von Fintel's (2001) dynamic account, a counterfactual widens a contextual parameter, the "modal horizon". The widened horizon is passed on from one counterfactual to the next (2001, 129). Widening happens silently, while narrowing appears to need explicit indication (2001, 140). The shift that would save Flattening has two features. It must narrow: it must remove from consideration the possibility in which Ann comes and Bob stays home, which is exactly the possibility (2) concerns. And it must persist or not.

Suppose it persists. Then once (1) is accepted, (2) should be heard as true. It is not. "If at least one of them had come, then if Ann had come, Bob would have been there. But if Ann had come, he would not have been there: his babysitter had cancelled." This discourse is coherent, and its second sentence stays plainly true. Yet under a fixed interpretation that validates Flattening it is a contradiction.

Suppose instead the shift is confined to the embedded position. Then it is the outer antecedent fixing how the inner conditional is evaluated. That is what the semantics of right-nested conditionals does in every order semantics: the inner conditional is evaluated at the point the outer antecedent selects. The control shows what such a local shift must look like. It must hold Bob's presence fixed in the Reunion and must not do so in Avoidance, although the two cases share every word. So it has no linguistic trigger. It must rank what follows Ann's arrival by the dependencies of the scenario in which Bob came. Such a shift just is the scenario-relative interpretation, under another name. To call it a shift of context rather than the meaning of the nested sentence is to grant that English nested counterfactuals do not express the conditional of which Flattening is said to be valid. The left member of every Flattening instance is a nested conditional, Dorr and Mandelkern's test pairs included. So on this view their pairs test the shifted interpretation too, and Flattening would be a principle with no natural-language instances.

Two further points. First, Dorr and Mandelkern set aside felt inequivalences due to tense and anaphora, and they compare these with apparent counterexamples to Contraction. The pair (1)–(2) contains proper names and a fixed past time, and the Contraction row of Section 3 is predicted to pattern with (2). Second, discourse continuations such as "Had one of them come, it would have been Bob, and he would have been there even if Ann had come" involve modal subordination (Roberts 1989). That makes them weaker evidence, which is why the argument uses syntactic nesting and no particles.

### 5.2 The sequence theorist

In sequence semantics, conditional-free sentences are settled by a sequence's first member. So two indices can agree on every categorical fact and differ on conditionals. Dorr and Mandelkern describe, without endorsing it, a gloss on which conditionals typically answer "non-factual" questions, and they credit a recent picture along these lines to Khoo (2022) (2026, 13). Sequence semantics has also been applied in recent work that they list, including work on counterfactual probability (Schultheis 2023; 2026, 3 n. 4). On this view, the index that "had at least one of them come" reaches is a tail. It shares the Bob scenario's categorical facts but carries the remainder of the actual ranking, so (1) is false there.

I grant that sequence models can represent the Reunion this way, and I do not claim to refute the view. My aim is to make exact what it must deny. The metaphysics of factual and non-factual questions is idle here, because the rule form settles the matter: whatever conditionals answer to, the sequence theorist must assign (1) the value of (2) in both cases. So they must deny the contrast in (P2), or relocate it into a shift, which was the topic of Section 5.1.

The Buttons sharpen the cost. The sequence theorist accepts Locality at actuality, since that is what makes (4) false, and nothing in the principle singles out the actual world. Applied to the Ann-pressed scenario taken as actual, Locality makes "if Bob had pressed, Ann would have pressed" true. Reached by supposition, the same scenario must make it false. So the theory must hold that whether Ann's press would have survived Bob's depends not on the scenario's laws and local facts but on the supposition through which the scenario was entered. The nested counterfactual it must then accept reads: had at least one pressed, then had Bob pressed, Ann would not have pressed. That asserts a counterfactual connection between spacelike-separated events in a world whose laws forbid influence between them.

The same cost appears in causal modelling. In a structural-equation model (Galles and Pearl 1998; Halpern 2000), a nested counterfactual whose antecedents set variables is evaluated by intervening and then intervening again in the resulting model. Such models do not by themselves fix how a disjunctive antecedent is realized. Once it is realized, as here by setting the babysitter variable, the result is a fully specified model of the Bob scenario. In that model, intervening on Ann's variable leaves Bob's value as it is, and the verdict does not depend on how the model was reached. Flatness requires the opposite verdict.

### 5.3 Disjunctive and alternative-sensitive antecedents

Some hear "had Ann or Bob come" as "had Ann come, and had Bob come". Together with the substitution of logically equivalent antecedents, that simplification yields antecedent strengthening (Ellis, Jackson and Pargetter 1977), so a proponent of C2.F cannot rest on it. Experimental work reports support for selection-based readings (Ramotowska et al. 2025). In any case, Section 3 showed that the universal reading predicts no contrast, so it cannot be the reading behind (P2). Truthmaker and alternative-sensitive semantics refuse to identify $(A \vee B) \wedge A$ with $A$ (Fine 2012; Santorio 2018; see Ciardelli, Zhang and Champollion 2018 on a two-switch case). Indefinites such as "at least one of them" raise alternatives just as disjunctions do. But the rule form, which is the form of Dorr and Mandelkern's own tests, needs only that the inner antecedent entail the outer. The control is neutral between ways of individuating antecedents, because whatever alternatives "at least one of them" raises, it raises them in both cases.

## 6. Why the test pairs pass

Let $v$ be the scenario selected for the outer antecedent $p$. The two sides of an instance diverge iff the first $pq$-scenario reached from $v$ differs, on what $r$ concerns, from the first $pq$-scenario reached from actuality. Suppose each scenario ranks alternatives by its own dependencies. Then robust divergence needs three things. (a) The outer antecedent can be realized in several ways. (b) The selected realization settles a matter $M$ that the inner antecedent leaves alone, so that supposing $pq$ from inside $v$ keeps $M$. (c) The consequent concerns $M$, and supposing $pq$ from actuality settles $M$ differently. When the ordering is a metric, divergence can arise without (b), from geometry alone. That is the case of their line example. It is hard to hear because nothing in the case makes 13 inches "nearer" to 11 than 8 is except the metric, and they were right to be unmoved by it.

Their subjunctive pairs fail (b) or (c). In "If he had gotten an espresso, then he would have had a fit if he'd gotten an overextracted one." (20), the inner antecedent fixes what the consequent depends on, however the outer one is realized. The same holds for the south of France and the soaked match. (Their conflagration pair is indicative, and I return to indicatives below.) Interventionist semantics shows why spot checks rarely find counterexamples. Intervening on a set of variables and then on a superset gives the same model as intervening on the superset directly, so instances whose antecedents are conjunctions of variable settings fail (a). The pair (1)–(2) meets all three conditions.

This also answers the redundancy datum. Where (b) or (c) fails, the outer antecedent of the nested member makes no difference in the context, so it "feels like it's doing nothing". That is predicted by contextual equivalence without logical equivalence. In (1) the outer antecedent does work: it is what makes the sentence true.

The cautious-cousin analogy fails for a structural reason. Cautious Monotonicity and Cautious Transitivity involve a single supposition. Every conditional in them is evaluated by the ordering at one world, which is why they hold on every order frame. Flattening involves iterated supposition. It relates the ordering at a world to the ordering at the world selected from it, which is why it needs a frame condition. The safety of the cautious principles comes from their staying within one ranking, so it does not transfer. (Nonmonotonic logic calls the conjunction of Cautious Monotonicity and Cut "cumulativity", and C2 already has that property. The property at issue here is different.)

Call a supposition operation *iteration-invariant* if supposing $Y$ and then some $X \subseteq Y$ gives the same result as supposing $X$ outright. *Imaging* a probability function on $X$ moves each world's probability to $f(w,X)$ (Lewis 1976), and it is the standard model of counterfactual supposition, as conditioning is of indicative supposition (Eva, Shear and Fitelson 2022 compare these and other approaches). A reformulation of (Flat): on a finite order frame, Flattening is valid iff imaging is iteration-invariant for every probability function. (Point masses are imaged to $f(f(w,Y),X)$ and $f(w,X)$ respectively.) In the theory of belief change, the same condition on iterated revision is the first Darwiche–Pearl postulate: if $\alpha \subseteq \beta$, then $(\kappa * \beta) * \alpha = \kappa * \alpha$ (Darwiche and Pearl 1997, as stated by Hunter and Delgrande 2011, 297). That literature contrasts revision, which takes in information about a static world, with update, which projects each state to the state that would result from a change (Hunter and Delgrande 2011, 273). Imaging moves each world separately, much as update does, and the cases show why iteration invariance is unwelcome there. A world's ranking of what lies beyond a scenario need not be that scenario's own ranking. In flat frames, any two worlds that both reach a world $v$ must order alike every pair of worlds that both place after $v$ (an immediate consequence of flatness). Dorr and Mandelkern's master-order picture makes this vivid. In the Reunion, actuality ranks Ann-alone ahead of both-came, because Bob's staying home is held fixed. The Bob scenario ranks them the other way.

## 7. Which logic, indicatives, and the unity of "if"

The cases bear only on Flattening's non-crashing content. In the models of the cases every world can access every world, so 4 and H hold, and so do both Crashing principles. This gives an observation.

**Observation 2.** C2 plus Crashing Cautious Importation and Crashing Cautious Exportation does not prove Flattening.

The frame of the Reunion model validates both Crashing principles but not Flattening (checked over all valuations). This fits Dorr and Mandelkern's corollary that C2.F is not C2 plus modal principles (29). My cases are consistent with counterfactuals obeying C2 together with 4 and H. Whether they do is a separate question. Dorr and Mandelkern note that complex left-nested conditionals are hard to assess (35), in connection with Sequentiality. 4 and H become left-nested once the defined operator is unpacked, so the same caution plausibly applies to them. That is my extension of their remark.

Theorem 1 holds for any conditional that obeys C2 and either half of Flattening, so one may ask about indicatives. The indicative pair, "If at least one of them came, then if Ann came, Bob was there" and "If Ann came, Bob was there", does not split for a speaker who does not know who came. Supposing indicatively that at least one came does not select Bob's coming; it leaves open which of them came. So condition (b) fails. In the Reunion both sentences are unwarranted, and in Avoidance both are acceptable in their negative forms. This gives no evidence against Flattening for indicatives. It gives none for it either.

It also does not answer Dorr and Mandelkern's open problem. Restricting an information state by $p$ and then by $q$ is restricting it by $pq$, for any $q$. A semantics built from successive restriction, or from conditioning, therefore validates full Import-Export, which collapses C2 into the material conditional (21). An explanation of Flattening for indicatives must separate the sequence "$p$, then $pq$" from "$p$, then $q$". I do not supply one. Nor does Stalnaker's Thesis supply one. Dorr and Mandelkern show that under a restricted Thesis the two sides of suitable instances receive equal probability, but they find no route to probability one. Their tree models satisfy a strong form of the Thesis while Flattening instances with Boolean $p$, $q$, $r$ have probability below one (44 n. 36).

The consequence for the unity of "if" follows from their own reasoning. They decline to validate Import-Export because it fails for subjunctives, and they explain its indicative appeal by mood. They exempt Flattening because it "appears valid for both" (22). If the argument above is right, Flattening fails for subjunctives too, so the same reasoning applies. A unified "if" should not validate Flattening, and whatever appeal it has for indicatives should be explained by what the indicative contributes. That leaves C2.F's model theory intact as a theory of a conditional. It withdraws the claim that C2.F is part of the logic of "if" in both moods.

## 8. Conclusion

I have argued that Flattening fails for counterfactuals. The evidence is a bare instance of its rule form, (1)–(2), together with a control that changes nothing but counterfactual dependence. Every unnested counterfactual about who came is held fixed across the two cases, as are the exclusive, additive and universal construals. Only the scenario-relative reading predicts the contrast, and Flattening fails on that reading. A persistent shift of context fails the persistence test. A local one is the scenario-relative interpretation under another name. The Buttons rest the inner verdict on locality. Theorem 1, a short consequence of CEM and either half of Flattening, extends the point to symmetric cases. The argument depends on judgments about nested counterfactuals, as any argument about Flattening must, and I have said how to test them. It leaves indicatives, 4 and H open, and it explains why Dorr and Mandelkern's test pairs did not reveal the failure.

## References

Ciardelli, Ivano, Linmin Zhang, and Lucas Champollion. 2018. "Two Switches in the Theory of Counterfactuals." *Linguistics and Philosophy* 41: 577–621. https://doi.org/10.1007/s10988-018-9232-4

Darwiche, Adnan, and Judea Pearl. 1997. "On the Logic of Iterated Belief Revision." *Artificial Intelligence* 89: 1–29. https://doi.org/10.1016/S0004-3702(96)00038-0

Dorr, Cian, and Matthew Mandelkern. 2026. "Sequence and Consequence." *Philosophical Logic* 1. https://doi.org/10.16995/phil-log.27646. Page references are to arXiv:2411.16994v2.

Ellis, Brian, Frank Jackson, and Robert Pargetter. 1977. "An Objection to Possible-World Semantics for Counterfactual Logics." *Journal of Philosophical Logic* 6: 355–357. https://doi.org/10.1007/BF00262069

Eva, Benjamin, Ted Shear, and Branden Fitelson. 2022. "Four Approaches to Supposition." *Ergo* 8. https://doi.org/10.3998/ergo.2227

Fine, Kit. 2012. "Counterfactuals without Possible Worlds." *The Journal of Philosophy* 109: 221–246. https://doi.org/10.5840/jphil201210938

von Fintel, Kai. 2001. "Counterfactuals in a Dynamic Context." In *Ken Hale: A Life in Language*, edited by Michael Kenstowicz, 123–152. Cambridge, MA: MIT Press. https://doi.org/10.7551/mitpress/4056.003.0006

Galles, David, and Judea Pearl. 1998. "An Axiomatic Characterization of Causal Counterfactuals." *Foundations of Science* 3: 151–182. https://doi.org/10.1023/A:1009602825894

Halpern, Joseph Y. 2000. "Axiomatizing Causal Reasoning." *Journal of Artificial Intelligence Research* 12: 317–337. https://doi.org/10.1613/jair.648

Hunter, Aaron, and James P. Delgrande. 2011. "Iterated Belief Change Due to Actions and Observations." *Journal of Artificial Intelligence Research* 40: 269–304. https://doi.org/10.1613/jair.3132

Khoo, Justin. 2022. *The Meaning of If*. New York: Oxford University Press. https://doi.org/10.1093/oso/9780190096700.001.0001

Lewis, David. 1976. "Probabilities of Conditionals and Conditional Probabilities." *The Philosophical Review* 85: 297–315. https://doi.org/10.2307/2184045

Lewis, David. 1979. "Counterfactual Dependence and Time's Arrow." *Noûs* 13: 455–476. https://doi.org/10.2307/2215339

Ramotowska, Sonia, Paul Marty, Jacopo Romoli, and Paolo Santorio. 2025. "Counterfactuals and Quantificational Force: Experimental Evidence for Selectional Semantics." *Semantics and Pragmatics* 18: 1–43. https://doi.org/10.3765/sp.18.6

Roberts, Craige. 1989. "Modal Subordination and Pronominal Anaphora in Discourse." *Linguistics and Philosophy* 12: 683–721. https://doi.org/10.1007/BF00632602

Santorio, Paolo. 2018. "Alternatives and Truthmakers in Conditional Semantics." *The Journal of Philosophy* 115: 513–549. https://doi.org/10.5840/jphil20181151030

Schultheis, Ginger. 2023. "Counterfactual Probability." *The Journal of Philosophy* 120: 581–614. https://doi.org/10.5840/jphil20231201133

Stalnaker, Robert C. 1968. "A Theory of Conditionals." In *Studies in Logical Theory*, American Philosophical Quarterly Monograph 2, 98–112. Oxford: Blackwell.

van Fraassen, Bas C. 1976. "Probabilities of Conditionals." In *Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science*, vol. I, 261–308. https://doi.org/10.1007/978-94-010-1853-1_10
