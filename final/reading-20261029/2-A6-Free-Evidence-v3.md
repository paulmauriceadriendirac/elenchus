# When Acting on Knowledge Makes Free Evidence Harmful: Good's Theorem in Normality Models

**Abstract.** Knowledge-based decision theory tells an agent to maximize expected utility with probabilities conditioned on what she knows. I examine this rule inside Goodman and Salow's normality theory of inductive knowledge. In finite statist, comparable models, with K-normality and the specified questions available, it gives every free question non-negative value at a situation if and only if the agent's knowledge is *gapped*: each possibility she leaves open is sufficiently more normal than each evidential possibility she rules out. More generally, any factive state that leaves open whatever rational belief leaves open can be safely conditioned on only if it is gapped. In graded models a factive gapped state must coincide with the evidence. A separate positive-measure argument extends the negative result to their Gaussian measurement model; at normal situations a second weighing has negative value at ten-to-one stakes. An expected-utility form of Salow's Conditional Knowledge Dominance does not help. In the finite setting it fails wherever the unconditional rule fails, even when it also governs later choices. The counterexamples survive small payoff changes. These results constrain one way of giving knowledge practical authority; they do not refute every knowledge-based theory.

## 1. Introduction

If you know p, any evidence against p is misleading, so it seems you may avoid it. This is the dogmatism puzzle. Salow (2025) offers the most economical recent dissolution. If Preservation holds (discovering something consistent with your beliefs never requires giving one up), you cannot believe both p and that you might meet evidence defeating p, so the puzzle never arises. If Preservation fails, the puzzle needs Weak Knowledge Dominance, which Salow replaces with a principle that looks equivalent but is not:

> Conditional Knowledge Dominance: If you know that B's consequences would be better than A's if they're not equally good, you should choose B over A. (Salow 2025, 33)

In Salow's Suitcase, you do not know that the suitcase weighs under 18 kg *on the hypothesis* that it weighs over 17.5 kg, since discovering the latter would defeat that knowledge. So the principle does not tell you to avoid checking. Salow's principles are qualitative. He grants that how all-out attitudes guide choices made under uncertainty about outcomes is "a general problem", and he expects that "Any solution to that problem will generalize to this one" (2025, 34).

The most developed solution of that kind is knowledge-based decision theory (KDT): maximize expected utility using probabilities conditioned on what you know, so that known propositions get probability 1. Goldschmidt (2024) axiomatizes a version due to Hawthorne and Stanley (2008), and Hong (2024) explores the view. I ask whether KDT keeps the practical content of Salow's dissolution, namely Good's (1967) theorem that free evidence never has negative expected value, once knowledge is modeled by the most developed formal theory of inductive knowledge, the normality framework of Goodman and Salow (2023, 2025). My thesis is this:

> In finite statist models with the specified questions available, conditioning on a factive belief-containing state makes every question safe only if that state is gapped. Under K-normality and comparability the condition is also sufficient. The proposed conditional expected-utility repair has counterexamples wherever the unconditional rule does.

Three results support the thesis. First, an exact boundary (Theorem 1). With K-normality, statism and comparability, KDT gives a free question non-negative value for every decision problem if and only if no situation compatible with what one knows is one where answering would reopen a possibility one now rules out. Every question has non-negative value if and only if knowledge is gapped. Theorem 2 extends the necessity half to any factive state that leaves open what rational belief leaves open, whichever theory of knowledge one adopts. Second, ubiquity. In Goodman and Salow's own model of Bjorn weighing himself twice, some bet makes KDT price the free second weighing negatively at each situation. At normal situations the displayed bet already does so at ten-to-one stakes (§3). Third, the conditional repair fails (§5). I define the expected-utility analogue of Conditional Knowledge Dominance. It handles the bets that motivate it. But in any situation where KDT disvalues a question, some decision problem makes the conditional rule disvalue it too (Theorem 3). The proof removes payoff ties both between the primitive acts and between acting now and the later policy. The rule therefore fails even when used consistently at both stages.

The closest prior work is as follows. Salow (2025) shows that Weak Knowledge Dominance licenses dogmatism exactly where Preservation fails, and he calls such failures "relatively rare" (36). I give the expected-utility counterpart, with an exact boundary, and show that in graded models failures of Good arise at every situation with inductive knowledge. I also show that his remedy does not carry over to expected utility. Goodman and Salow (2025, henceforth BRN) show that statism, collapse and comparability validate Preservation and that Preservation fails in Bjorn. I give the decision-theoretic counterpart, together with what follows for decisions from their distinction between conditional and post-discovery belief. Geanakoplos (1989; 2002 revision, §2) gives sufficient conditions for the value of information, discussed by Das (2023). The contribution here is the bridge from normality kens to information value, with an exact safety boundary. The necessity proof directly constructs a harmful question; it does not infer harm merely from failure of sufficient conditions. Hong (2026, §§1–3) directly criticizes normality-based action guidance through lottery switching, sweeteners and the value of otherwise irrelevant information. Those problems already challenge conditioning on normality knowledge. The proposed increment here is an exact finite safety boundary and a construction defeating the specified conditional expected-utility repair, rather than the general claim that normality creates decision-theoretic difficulties.

The result concerns a specific practical role for knowledge: settling probabilities used in expected-utility calculations. It does not deny that knowledge can guide action in other ways, or refute Salow's qualitative principle by itself. Its force depends on whether the theorist wants the universal safety guarantee, a restriction made explicit below.

## 2. Framework

I follow Goodman and Salow (2023) and BRN. A *normality structure* has a set $S$ of states, a family $\mathcal{E}$ of possible bodies of evidence, and two relations on situations $\langle s,E\rangle$ (with $s\in E\in\mathcal{E}$): $\succeq$ (at least as normal as), a preorder, and $\gg$ (sufficiently more normal than). $\gg$ implies $\succeq$, is irreflexive, and *chains*: if $w_1\succeq w_2\gg w_3\succeq w_4$ then $w_1\gg w_4$. Under *statism* both relations are evidence-independent, so I treat them as relations on states. *Comparability* says any two states with the same evidence are $\succeq$-related. *Collapse* says every strict difference in normality is sufficient. For the theorems $S$ is finite.

Rational belief, given evidence $E$, rules out exactly the evidential possibilities that something else in $E$ is sufficiently more normal than:
$$B(E)=\{s\in E:\ \text{no } u\in E \text{ has } u\gg s\}.$$
Knowledge goes beyond evidence by the same mechanism, but its extent depends on where one actually is. I work mainly with *K-normality* (Goodman and Salow 2023, 104):
$$K_E(x)=B(E)\cup\{v\in E: v\succeq x\}.$$
One knows what is true throughout $K_E(x)$. Evidence is transparent: situations with the same evidence are evidentially accessible from each other. As Goodman and Salow note, "given transparency, K-normality entails KK" (2023, 107). The alternatives they consider, I- and KM-normality, validate their principle Margins and allow failures of KK; I return to them in §6.1. Discovering $p$ at $\langle x,E\rangle$ yields $\langle x,E\cap p\rangle$. A *question* is a partition $\Pi$ of $E$ into discoverable cells; $\Pi(s)$ is the cell containing $s$.

**Knowledge-based expected utility.** Fix a prior $\Pr$ with full support. A *decision problem* is a finite set $A$ of acts, each a function from states to utilities. At $\langle x,E\rangle$, KDT chooses an act maximizing $\Pr(u_a\mid K_E(x))$, with ties broken by a fixed order. Goldschmidt (2024) describes this conditionalizing form of KDT alongside Hawthorne and Stanley's proposal, on which known propositions receive probability 1; for present purposes the two agree.

**The value of a free question.** Let $\alpha_\Pi(s)$ be the act KDT chooses at $\langle s,E\cap\Pi(s)\rangle$, after answering $\Pi$ in state $s$. The KDT value of answering $\Pi$ before choosing is
$$V_x(\Pi,A)=\sum_s \Pr(s\mid K_E(x))\,u(\alpha_\Pi(s),s)\;-\;\max_{a\in A}\Pr(u_a\mid K_E(x)).$$
This is Good's comparison of acting now with the plan of looking and then acting, with $\Pr(\cdot\mid K_E(x))$ in place of the unconditioned probability. Call $\Pi$ *safe* at $x$ if $V_x(\Pi,A)\geq 0$ for every decision problem $A$.

Two conditions will matter.

*Relative defeat* at $x$ for $\Pi$: some $s\in K_E(x)$ has $K_{E\cap\Pi(s)}(s)\not\subseteq K_E(x)$. In words, for all one knows, answering the question would leave open something one now rules out.

*Gapped*: every member of $K_E(x)$ is sufficiently more normal than every member of $E\setminus K_E(x)$.

## 3. Bjorn's second weighing

Goodman and Salow's (2023, §6) model of Bjorn is statist and comparable, and it violates collapse. Its states are triples $\langle w,y_1,y_2\rangle$: Bjorn's weight and the readings of two scales. With $\delta=(w-y_1)^2+(w-y_2)^2$, one state is at least as normal as another iff its $\delta$ is no larger, and sufficiently more normal iff its $\delta$ is smaller by more than $c^2$. Goodman and Salow derive these relations from independent Gaussian errors (2023, 129). I take the standard deviation as the unit and, following BRN (§5, n. 18), set $c\approx1.96$.

After the first reading $r$, Bjorn believes his weight lies in $[r-c,r+c]$. Under K-normality, in any situation with $\delta\le c^2$ this belief is knowledge, and his ken is $\{\delta\le c^2\}$. After a second reading $r'$ he believes his weight lies within $c/\sqrt2$ of the average of the two readings. So he leaves open weights up to $c/\sqrt2+|r-r'|/2$ from $r$. As Goodman and Salow show for the case where the first reading is accurate, he "loses knowledge" whenever $|r-r'|>(2-\sqrt2)c$ (2023, 127). Since the readings may differ by up to $\sqrt2c$ for all he believes, he believes that the second weighing might defeat his knowledge. This is a failure of Preservation, the case BRN use against it. It is not rare: with Gaussian errors, the second reading falls in the Preservation-violating range with probability about 0.37, as BRN also estimate (§5, n. 18). Salow describes such failures as "relatively rare" (2025, 36); in the leading model of measurement they occur on more than a third of second weighings.

**Ten-to-one bet.** After the first weighing Bjorn is offered a bet: win 1 if his weight is within $c$ of $r$, lose 10 otherwise. He knows the bet wins, so KDT takes it. A free second weighing is then offered. After the second weighing he would decline the bet whenever the readings differ by more than about $1.12c$, because his new ken gives the losing weights enough probability. Conditional on his present knowledge, this has probability about 0.05. In each such state he forgoes a payoff he now knows he would get. So KDT values the free weighing at about $-0.05$. At twenty-to-one the value is $-0.12$, and at a hundred-to-one $-0.27$. (These are numerical integrations over the model; see the appendix.) A fallibilist who uses the unconditioned probabilities also takes the ten-to-one bet: on her evidence it wins with probability 0.95, so its expected value is $0.95-10(0.05)=0.45$. By Good's theorem the second weighing cannot have negative value for her.

The phenomenon is not confined to normal situations. At any situation after the first weighing there is a state compatible with Bjorn's knowledge in which the second reading would reopen a weight he now rules out (appendix, A.5). The finite-state Lemma 1 cannot by itself establish that claim in a continuous space, where a single state has probability zero. Appendix A.5 supplies the positive-measure extension. Thus some finite-stakes bet makes the second weighing harmful at each situation; the required stakes can vary with the situation. The ten-to-one example concerns the normal situations specified above. This payoff ratio does not by itself specify the absolute practical stakes.

## 4. Where Good's theorem holds

The case instantiates a general pattern. Write $M$ for any assignment of a set $M_F(s)\subseteq F$ to situations, used in place of $K$ in the definitions of §2.

**Lemma 1 (defeat is costly).** If some $s_0\in M_E(x)$ has $M_{E\cap\Pi(s_0)}(s_0)\not\subseteq M_E(x)$, then some two-act decision problem gives the question $\Pi$ negative value.

*Proof.* Take a bet $\beta$ paying 1 on $M_E(x)$ and $-L$ elsewhere, and declining, which pays 0. Now $\beta$ has conditional expectation 1, so it is chosen. At $s_0$ the post-answer state contains a state outside $M_E(x)$, which has positive probability, so for large $L$ the agent declines. She then gets 0 where $\beta$ paid 1. Nowhere in $M_E(x)$ does she get more than 1. So $V\le-\Pr(s_0\mid M_E(x))<0$. ∎

**Lemma 2 (laminar sufficiency).** Suppose the post-answer states $\{M'(s): s\in M_E(x)\}$ all lie within $M_E(x)$. Suppose also that they are reflexive ($s\in M'(s)$), transitive ($t\in M'(s)$ implies $M'(t)\subseteq M'(s)$) and nested (any two are disjoint or one contains the other). Then $V\ge0$ for every decision problem.

This is an application of Geanakoplos’s value-of-information result (1989; 2002 revision, Theorem 1), also discussed by Das (2023). I give a short proof in the appendix.

**Lemma 3.** Under statism and comparability, for each $F$ the K-normality kens $\{K_F(s):s\in F\}$ are reflexive, transitive and nested.

**Theorem 1.** Assume statism, comparability and K-normality.
(a) A question is safe at $x$ if and only if there is no relative defeat at $x$ for it.
(b) Suppose that for each $v\in E$ the question $\{p_v, E\setminus p_v\}$ is available, where $p_v=\{u\in E: \text{not } u\gg v\}$. Then every available question is safe at $x$ if and only if $K_E(x)$ is gapped.

Part (a) combines Lemmas 1–3. Part (b) adds two observations. If the ken is gapped, no answer can reopen anything. If it is not gapped, the question about $p_v$ reopens $v$. That is the next lemma, and it does not depend on which theory of knowledge one adopts.

**Lemma 4 (non-gaps are defeasible).** Assume statism. Let $m\in M_E(x)$ and $v\in E\setminus M_E(x)$, with not $m\gg v$. Then $m,v\in p_v$ and $v\in B(E\cap p_v)$.

*Proof.* $m\in p_v$ by hypothesis and $v\in p_v$ by irreflexivity. Nothing in $p_v$ is sufficiently more normal than $v$, so $v\in B(E\cap p_v)$. ∎

Say that $M$ *leaves open what rational belief leaves open* if always $B(F)\subseteq M_F(s)$. Knowledge on each of Goodman and Salow's three completions does, and so do justified true belief and the closure of knowledge under iteration.

**Theorem 2 (only gapped states can be conditioned on).** Assume statism. Suppose $M$ leaves open what rational belief leaves open and the questions of Theorem 1(b) are available. If expected utility conditioned on $M$ makes every available question safe at $x$, then $M_E(x)$ is gapped. A gapped set containing $x$ contains $C(x)$: the states reachable from $x$ by steps, each to a state that is not sufficiently less normal than the last.

The boundary in Theorem 1 is not the boundary of Preservation. At abnormal situations, knowledge can be defeated by evidence that contradicts one's beliefs, so KDT can disvalue a question even in models where Preservation holds without exception. Take three states $a,b,c$, in decreasing order of normality, with $a\gg b$ and $a\gg c$ but not $b\gg c$. In this structure Preservation holds for every body of evidence and every discovery. At $b$ one knows $\{a,b\}$. Learning that $a$ is false, which is true at $b$, reopens $c$. Salow anticipates this pattern: a 'for all you know' version of Weak Knowledge Dominance "can support dogmatism even given Preservation" (2025, 33). Theorem 1 locates its expected-utility counterpart exactly.

Call $E$ *graded* if $C(x)=E$ for every $x\in E$. Bjorn's evidence after one reading is graded, since a chain of small increases in $\delta$ connects any two states. So is the evidence in Flipping for Heads, where flips are counted until the first heads (BRN §5).

**Corollary.** (i) Under statism, collapse and comparability, every K-normality ken is gapped, so KDT makes every question safe. (ii) If $E$ is graded, the conditioning state is factive, and the questions of Theorem 1(b) are available, expected utility conditioned on a state that leaves open what rational belief leaves open makes every question safe at $x$ only if that state is all of $E$.

Part (i) is the decision-theoretic counterpart of BRN's result that statism, collapse and comparability validate Preservation. Part (ii) says that in graded models the only belief-containing state one can condition on without making some free question harmful is one's evidence. Conditioning on evidence is what Salow calls the fallibilist response, on which "decisions should be governed by underlying probabilities rather than our knowledge" (2025, 23). Bjorn shows that the questions needed for (ii) can be as natural as a second reading.

I also checked the theorems by exhaustive enumeration. The enumeration covered all statist comparable structures with up to four states, every body of evidence, every situation and every partition: 64,004 situation–question pairs. Across all available partitions, a situation admitted some relative defeat exactly when its ken was not gapped. This is an existential claim over questions: a particular question can be safe at a nongapped ken. In each of the 3,306 cases of relative defeat, the decision problem built in Theorem 3 below gave negative KDT value. About 240,000 random decision problems without relative defeat gave no negative value.

## 5. The conditional repair

### 5.1 The rule

The natural expected-utility analogue of Conditional Knowledge Dominance compares two options by their expected difference on the hypothesis that they differ. Let $D_{a,b}=\{s\in E:u_a(s)\ne u_b(s)\}$. Let $K^D_E(x)$ be what one knows on the hypothesis $D$. Its K-normality form restricts evidential accessibility to $D$, as BRN's definition of conditional belief does (App. D.3):
$$K^D_E(x)=\{v\in E\cap D:\text{no }u\in E\cap D\text{ has }u\gg v\}\cup\{v\in E\cap D: v\succeq x\}.$$
Under statism, when $x\in D$, this is the ken one would have on discovering $D$; in every case it contains the belief one would have on discovering $D$. So it respects Salow's constraint that one is "entitled to believe q on the hypothesis that p only if discovering p would not require you to stop believing q" (2025, 33).

**CEU.** Prefer $b$ to $a$ if $\Pr(u_b-u_a\mid K^{D_{a,b}}_E(x))>0$. Looking before acting is one option; its payoff in state $s$ is $u(\alpha_\Pi(s),s)$.

For Bjorn's bet CEU works as Salow's diagnosis predicts. Looking and betting now differ exactly where the second reading would make Bjorn decline. On the hypothesis that this happens, his conditional ken includes losing weights. With the actual readings perfectly accurate, at ten-to-one the bet's expected value on that hypothesis is $-0.63$. So CEU prefers to look. The dogmatic argument fails for the reason Salow gives: on the hypothesis that the evidence makes a difference, you do not know that your verdict is right.

### 5.2 Why the repair fails

For the displayed bet, the conditional repair uses states where looking and acting now pay the same. These are excluded from $D$, so conditioning on a difference carries information. That feature can be removed by a carefully chosen perturbation: if the present act and later policy differ in every state, $D=E$, conditional knowledge is ordinary knowledge, and CEU coincides with KDT. The following construction establishes such a case whenever there is relative defeat. No claim about the prevalence of ties in typical decision problems is needed.

**Theorem 3.** Assume statism, comparability and K-normality, and suppose conditional knowledge on the trivial hypothesis $E$ is ordinary knowledge. If there is relative defeat at $x$ for $\Pi$, then some three-act decision problem makes CEU strictly prefer acting now to answering $\Pi$, even if CEU also governs every later choice. KDT gives $\Pi$ negative value too. These verdicts persist on an open neighborhood of the constructed payoff matrix.

*Construction.* Let $M=K_E(x)$ and choose $s_0\in M$ witnessing relative defeat. Take the bet $\beta$ of Lemma 1, declining, and $\beta_1=\beta+\varepsilon\zeta$, where $\zeta(s_0)=N$ and $\zeta=-1$ elsewhere. Choose $N$ with positive current mean for $\zeta$, $0<\varepsilon<1$, and then $L$ large enough that every post-answer ken meeting $E\setminus M$ strictly prefers declining. There are finitely many such kens, so one finite $L$ suffices. Any remaining post-answer ken excludes $s_0$: otherwise transitivity would put $s_0$'s outside possibilities in that ken too. There $\beta$ strictly beats $\beta_1$ and declining.

Every pair of primitive acts differs at every state: $\beta$ and $\beta_1$ are everywhere nonzero and their difference is everywhere nonzero. Thus, at every decision stage, the hypothesis on which CEU conditions is the entire current evidence. CEU and KDT consequently choose the same primitive act. This answers a potential objection to the construction: it does not make the conditional rule anticipate successors who follow a different rule.

Looking therefore never selects $\beta_1$, while $\beta_1$ is uniquely best now. Its payoff also differs everywhere from the looking policy, so their comparison again uses ordinary knowledge. The gain from acting now at $s_0$ outweighs the small losses elsewhere (Appendix A.6).

For a numerical illustration, take three states $a\succ b\succ c$, with only $a\gg c$, and a uniform prior. At $a$ the ken is $\{a,b\}$. Ask whether $a$; on the other answer the ken is $\{b,c\}$. Let the acts pay $(1,1,-10)$, $(0,0,0)$, and $(0.9,1.5,-10.1)$. Both rules choose the third now, with current expectation $1.2$. After looking they choose the first at $a$ and decline at $b$ and $c$. That policy pays $(1,0,0)$ and has current expectation $0.5$. CEU therefore prefers acting now by $0.7$. All comparisons are strict and no relevant pair has an equal payoff at any state.

The example is stable under sufficiently small changes in every payoff. In the general construction, finiteness and strict preferences supply positive margins; small perturbations preserve the chosen acts and the absence of equal payoffs. This is local robustness, not a claim that these problems are prevalent.

A fixed absolute tolerance for a “significant” difference does not rescue the rule. Scale all utilities by a sufficiently large positive constant so that every relevant pointwise difference exceeds that tolerance. Expectations and choices scale together. This argument addresses a fixed absolute tolerance; it does not exclude context-sensitive or relative notions of significance. Nor does the finite construction establish the corresponding CEU theorem for continuous Gaussian models, where arbitrarily small outside probabilities can prevent a uniform choice of $L$.

The result also applies to any pairwise rule that agrees with knowledge-conditioned expected utility whenever the compared payoffs differ everywhere. The difficulty is therefore precise: a repair that changes only the treatment of equal-payoff states cannot guarantee safety in these models. It must also reconsider some comparisons on which there are no equal-payoff states to remove.

### 5.3 Which conditional knowledge?

Outside statist models, conditional knowledge presents a further choice. BRN distinguish belief on a hypothesis, evaluated using the current normality relations, from belief after discovering that hypothesis, when those relations may change (App. D.3). The distinction matters because Salow's reply requires a connection to what discovery would defeat. I do not assume that BRN's treatment uniquely determines a theory of conditional knowledge. Theorem 3 avoids this interpretive question: it uses only the requirement that conditioning on the entire evidence leaves ordinary knowledge unchanged. A non-statist or differently defined conditional theory requires separate assessment.

## 6. Objections and replies

### 6.1 "This is self-trust, not evidence"

The objection says that KDT disvalues questions because the agent distrusts her future self, not because she distrusts the evidence. On the Margins completions (I- and KM-normality), statism, comparability and Margins "together entail no defeat" (Goodman and Salow 2023, 128). There, by Lemma 4, the reopened possibility lies in the agent's own *present* ken at $m$, so the relative defeat in Theorem 2 is a failure of KK at $x$. Such failures harm the empty question too. By Lemma 1 with the trivial partition, a KDT agent without KK at $x$ pays to decide now rather than later on the same evidence. This kin of Williamson's unmarked clock is discussed by Ahmed and Salow (2019) and Das (2023). For the Margins views I concede the objection: what fails there is deference to one's later self, not openness to evidence.

For K-normality the objection fails. KK holds, so by Lemmas 2 and 3 the empty question always has nonnegative value. Zero is not guaranteed: at an abnormal situation the present ken may contain states with strictly smaller kens, whose state-dependent choices can outperform one fixed act. For example, take $a$ more normal than $b$, with $a\gg b$, a uniform prior, and acts paying $(1,0)$ and $(0,2)$ at $(a,b)$. At $b$ the present best value is 1; with no new evidence, the state-dependent choice plan pays $(1,2)$ and has value 1.5. The empty question therefore has value 0.5. The relevant contrast is absence of a negative value, not universal equality to zero. Moreover, if a question has $V_x(\Pi,A)<0$ while the empty question has nonnegative value, it also fares worse than the matched plan of waiting without gathering evidence. The negative comparison is not produced merely by contrasting later state-dependent choice with a single present act. In Bjorn's case, the new reading destroys knowledge despite positive introspection. The structure is the classic dogmatist's. I know the bet wins. In some states compatible with what I know, the evidence will make me unable to rely on that. So I should avoid the evidence. Under Theorem 1's assumptions, some available question has this structure exactly where knowledge is not gapped. So the dilemma for graded inductive knowledge is this. On the KK-friendly completion, KDT avoids evidence. On the KK-unfriendly completions, it avoids deferring to itself.

### 6.2 "Trivial once stated: knowledge is treated as certainty"

The pieces are indeed familiar. Lemma 1 is an ordinary bet, Lemma 2 is Geanakoplos's sufficiency condition, and Corollary (i) parallels BRN's result. The proposed contribution has three parts. The first is the exact location of the boundary, which includes abnormal situations whose kens extend below the belief set. The second is Theorem 2's completion-independence: no belief-containing state other than a gapped one can be conditioned on, so no refinement of knowledge (iterated knowledge, justified true belief) escapes. The third is Theorem 3. Harman's and Kripke's discussions explain why knowledge-as-certainty invites the puzzle. They do not show that the leading conditional remedy fails in expected-utility form. The necessity result concerns fixed conditioning states and the stated universal safety requirement, not every response to dogmatism.

### 6.3 "KDT is meant for low stakes"

Under K-normality with transparency, iterating knowledge does not change the ken, so conditioning on higher-order knowledge gives the same probabilities here. A ten-to-one payoff ratio is not an absolute measure of stakes. At a fixed ken, positive rescaling of all utilities preserves choices and the sign of information value, so the counterexample can have arbitrarily small payoff magnitudes. But if the ken itself changes with the menu or practical stakes, the theorem must be applied to that changed model. It does not refute every stakes-sensitive theory.

### 6.4 "Statism is the exception"

BRN argue that statism fails in general. The finite equivalence is conditional on statism, and it should not be advertised as a classification of their entire framework. Bjorn's measurement model is statist, however, so that restriction leaves a substantive application. Beyond it, the relevant questions are whether the post-answer kens remain nested and whether the questions used in Lemma 4 still reopen the excluded possibilities. Neither condition should be assumed without proof.

### 6.5 Encroachment

Salow (2025, 24 n. 3) reports Hawthorne's (2004, 181) suggestion that, given Good's theorem, the puzzle is handled by pragmatic encroachment of the kind on which encroachment occurs whenever the difference between maximal and actual probability affects one's preferences over the available options. Salow objects that encroachment would not be confined to failures of Preservation (36). Theorem 2 makes the cost exact. To guarantee safety for every decision problem and every question in the theorem's class on graded evidence, a factive belief-containing state must expand to include the entire evidence set. This does not show that the mere availability of a second scale destroys all inductive knowledge at every fixed stake level. The universal guarantee quantifies over decision problems as well as questions.

### 6.6 "Good's theorem is not sacrosanct"

Ahmed and Salow (2019) contest unrestricted requirements to gather and use information. Bjorn's readings partition the evidential possibilities exactly, but the knowledge kens used for decisions can still overlap. Thus exact observation does not by itself put the decision problem back inside the classical partitional theorem. The negative result is a cost for a theorist who wants universal safety, not a contradiction for one who rejects it.

Another response allows the agent to commit to ignoring an answer. If that commitment is feasible, the menu of policies includes the present best act, so the best available policy cannot be worse merely because a free signal is offered. The results concern looking followed by the specified future choice rule, without such commitment. Their practical significance is the resulting tension between present evaluation and later rational choice. Whether knowledge should determine numerical probabilities, whether the later rule should change, or whether such tensions are acceptable remains a philosophical choice.

## 7. Conclusion

In finite statist, comparable models with K-normality and the specified questions available, expected utility conditioned on knowledge makes every free question safe exactly where knowledge is gapped. Any factive state that leaves open what rational belief leaves open needs the same condition. On graded normality, which Goodman and Salow defend for measurement, that condition means not going beyond the evidence. The expected-utility form of Salow's Conditional Knowledge Dominance does not escape: in the finite setting it has counterexamples wherever the unconditional rule does, including when the conditional rule governs both stages. What has not been shown is that no other way of letting all-out attitudes guide graded choice could preserve Salow's dissolution. The result places a precise burden on this conditionalizing form of knowledge-first decision theory. It must weaken the universal safety requirement, restrict its model or question class, or change how knowledge controls numerical choice. Collapse is one sufficient restriction, and evidence-based probabilities are one alternative; the results do not establish an exhaustive trilemma for every knowledge-first theory.

## Appendix: proofs and computations

**A.1 Lemma 2.** Let $\mathcal F=\{M'(s):s\in M\}$, $M=M_E(x)$. By nestedness and reflexivity the inclusion-maximal members of $\mathcal F$ partition $M$. For a maximal $C=M'(c)$, let $a_C$ be the act chosen on $C$. I show by induction on $|C|$ that $\Pr(u(\alpha(s),s)\mid C)\ge\Pr(u_{a_C}\mid C)$. By transitivity every $s\in C$ has $M'(s)\subseteq C$. The states with $M'(s)=C$ choose $a_C$. The others lie in the maximal proper sub-kens $D_1,\dots,D_k$, which are disjoint members of $\mathcal F$ satisfying the hypotheses. By induction, on each $D_j$ the plan does at least as well as the best act on $D_j$, and so at least as well as $a_C$. Summing over the parts of $C$ and then over the maximal sets, the plan's expectation on $M$ is at least $\sum_C\Pr(C\mid M)\max_a\Pr(u_a\mid C)\ge\max_a\Pr(u_a\mid M)$. ∎

**A.2 Lemma 3.** Reflexivity holds because $s\succeq s$. For transitivity, let $t\in K_F(s)$. If $t\in B(F)$, then every $v\succeq t$ is in $B(F)$: if $u\gg v$, chaining gives $u\gg t$. So $K_F(t)=B(F)\subseteq K_F(s)$. If $t\succeq s$, then $\{v:v\succeq t\}\subseteq\{v:v\succeq s\}$. For nestedness, by comparability the sets $\{v: v\succeq s\}$ are linearly ordered by inclusion, and each ken is their union with $B(F)$. ∎

**A.3 Theorem 1.** (a) Answers in different cells give disjoint kens. By Lemma 3 the post-answer kens are reflexive, transitive and nested. Without relative defeat they lie within $K_E(x)$, so Lemma 2 applies. Conversely, use Lemma 1. (b) Suppose the ken is gapped, $s\in K_E(x)\cap c$, and $v\in c\setminus K_E(x)$. Then $s\gg v$, so $v\notin B(E\cap c)$. Also not $v\succeq s$, since otherwise $v\succeq s\gg v\succeq v$ gives $v\gg v$. So $K_{E\cap c}(s)\subseteq K_E(x)$. If the ken is not gapped, Lemma 4 gives relative defeat, because $B(E\cap p_v)\subseteq K_{E\cap p_v}(m)$. ∎

**A.4 Theorem 2.** Lemmas 4 and 1 give the first claim. If $M$ is gapped, $m\in M$ and not $m\gg v$, then $v\in M$; so $M$ is closed under the steps that generate $C(x)$. ∎ *Corollary (i).* Let $m\in K_E(x)$ and $v\notin K_E(x)$. Then not $v\succeq x$, and some $u\gg v$. If $m\succeq x$, comparability and collapse give $x\gg v$, hence $m\gg v$. If $m\in B(E)$, then $v\succeq m$ would give $u\gg m$, so $m$ is strictly more normal than $v$ and collapse gives $m\gg v$. ∎

**A.5 Bjorn and positive measure.** After the first reading, use coordinates $\mu=(e_1+e_2)/2$ and $d=e_1-e_2$, so $\delta=2\mu^2+d^2/2$. For the numerical model assume the proper conditional Gaussian measure with independent $\mu\sim N(0,1/2)$ and $d\sim N(0,2)$, corresponding to the swamped-prior treatment of weight. The measurement likelihood alone would not fix this conditional distribution without that prior assumption. Conditional on a second reading, $d$ is fixed and the post-answer ken has $|\mu|\le\max(c/\sqrt2,|\mu_s|)$.

Let $R=\max(c^2,\delta(x))$, so the current ken is the disk $M=\{\delta\le R\}$. Choose an interior point with $\mu_s=0$ and $d(s)^2/2$ strictly between $R-c^2$ and $R$. Its post-answer ken reaches beyond $M$, since its maximum $\delta$ is $c^2+d(s)^2/2>R$. The inequalities are strict. Hence a sufficiently small open neighborhood $U$ of that point stays inside $M$ and has post-answer conditional probability of $M^c$ bounded below by some $\eta>0$. Gaussian density makes $U$ have positive current probability. A bet paying 1 on $M$ and $-L$ outside it is therefore declined throughout $U$ when $L>(1-\eta)/\eta$. It is accepted now; subsequent choice never pays more than 1 inside $M$. Its value of looking is at most $-\Pr(U\mid M)<0$. This is the continuous argument that the finite singleton proof cannot supply.

For the stated normal-situation figures, the bet is instead on $|e_1|\le c$. Integrating the Gaussian density over $\delta\le c^2$ gives the probabilities of declining after the second reading. These figures are numerical approximations, not premises of the finite theorems.

**A.6 Theorem 3.** Put $P=\Pr(\cdot\mid M)$ and choose $N$ with $NP(s_0)>2$. Fix $0<\varepsilon<1$. For each post-answer ken $F$ meeting $E\setminus M$, write $q_F=\Pr(E\setminus M\mid F)>0$. The expected payoff of $\beta_1$ on $F$ is at most $1+\varepsilon N-Lq_F$, and that of $\beta$ is at most $1-Lq_F$. Since there are finitely many $F$, choose $L$ making both bounds strictly negative. On every other post-answer ken, transitivity excludes $s_0$, so $\beta_1=1-\varepsilon$ and $\beta=1$. At the present ken $\beta_1$ is uniquely optimal since $P(\zeta)>0$. At $s_0$ acting now gains $1+\varepsilon N$; elsewhere inside $M$ looking gains at most $\varepsilon$. Hence
$$P(u_{\beta_1}-u_{\mathrm{look}})\ge P(s_0)(1+\varepsilon N)-\varepsilon>0.$$
Outside $M$, factivity forces declining after looking, whereas $\beta_1=-L-\varepsilon$. Inside $M$, the looking payoff is 0 or 1, neither equal to $\beta_1$. Thus the comparison's difference event is $E$. The primitive acts likewise differ everywhere, proving CEU–KDT agreement at both stages. Finally, finitely many strict choice inequalities, nonzero pointwise differences, and the strict preference for acting now persist on a sufficiently small open neighborhood of the payoff matrix. ∎

**Computations.** Python scripts enumerate all statist structures satisfying Goodman and Salow's constraints: comparable ones with up to four states (up to five for collapse) and non-comparable ones with up to three. For each they compute kens, post-answer kens, KDT and CEU choices with random full-support priors and the constructed problems. Bjorn's values are computed by numerical integration. Flipping for Heads is computed exactly, truncated at 60 flips.

## References

Ahmed, Arif, and Bernhard Salow. 2019. "Don't Look Now." *British Journal for the Philosophy of Science* 70: 327–350.

Das, Nilanjan. 2023. "The Value of Biased Information." *British Journal for the Philosophy of Science* 74: 25–55.

Geanakoplos, John. 1989. "Game Theory without Partitions, and Applications to Speculation and Consensus." Cowles Foundation Discussion Paper 914, Yale University. Revised June 18, 2002; the revision was consulted for Theorem 1.

Goldschmidt, Zeev. 2024. "Foundations for Knowledge-Based Decision Theories." *Australasian Journal of Philosophy* 102: 939–958.

Good, I. J. 1967. "On the Principle of Total Evidence." *British Journal for the Philosophy of Science* 17: 319–321.

Goodman, Jeremy, and Bernhard Salow. 2023. "Epistemology Normalized." *Philosophical Review* 132: 89–145.

Goodman, Jeremy, and Bernhard Salow. 2025. "Belief Revision Normalized." *Journal of Philosophical Logic* 54: 1–49.

Hawthorne, John. 2004. *Knowledge and Lotteries*. Oxford: Oxford University Press.

Hawthorne, John, and Jason Stanley. 2008. "Knowledge and Action." *Journal of Philosophy* 105: 571–590.

Hong, Frank. 2024. "Know Your Way Out of St. Petersburg: An Exploration of 'Knowledge-First' Decision Theory." *Erkenntnis* 89: 2473–2492.

Hong, Frank. 2026. "Normality in Action?" *Philosophical Perspectives*, early view. https://doi.org/10.1111/phpe.70003.

Salow, Bernhard. 2025. "Fallibility and Dogmatism." *Australasian Journal of Philosophy* 103: 23–38.

