# When Acting on Knowledge Makes Free Evidence Harmful: Good's Theorem in Normality Models

**Abstract.** Knowledge-based decision theory tells an agent to maximize expected utility with probabilities conditioned on what she knows. I examine this rule inside Goodman and Salow's normality theory of inductive knowledge. In statist models it gives every free question non-negative value at a situation if and only if the agent's knowledge is *gapped*: each possibility she leaves open is sufficiently more normal than each evidential possibility she rules out. More generally, any factive state that leaves open whatever rational belief leaves open can be safely conditioned on only if it is gapped. In graded models, including Goodman and Salow's model of measurement, a state is gapped only if it coincides with the evidence; there a free second weighing has negative value at ten-to-one stakes. An expected-utility form of Salow's Conditional Knowledge Dominance does not help. It fails wherever the unconditional rule fails, and in non-statist models its verdicts turn on how conditional knowledge is read.

## 1. Introduction

If you know p, any evidence against p is misleading, so it seems you may avoid it. This is the dogmatism puzzle. Salow (2025) offers the most economical recent dissolution. If Preservation holds (discovering something consistent with your beliefs never requires giving one up), you cannot believe both p and that you might meet evidence defeating p, so the puzzle never arises. If Preservation fails, the puzzle needs Weak Knowledge Dominance, which Salow replaces with a principle that looks equivalent but is not:

> Conditional Knowledge Dominance: If you know that B's consequences would be better than A's if they're not equally good, you should choose B over A. (Salow 2025, 33)

In Salow's Suitcase, you do not know that the suitcase weighs under 18 kg *on the hypothesis* that it weighs over 17.5 kg, since discovering the latter would defeat that knowledge. So the principle does not tell you to avoid checking. Salow's principles are qualitative. He grants that how all-out attitudes guide choices made under uncertainty about outcomes is "a general problem", and he expects that "Any solution to that problem will generalize to this one" (2025, 34).

The most developed solution of that kind is knowledge-based decision theory (KDT): maximize expected utility using probabilities conditioned on what you know, so that known propositions get probability 1. Goldschmidt (2024) axiomatizes a version due to Hawthorne and Stanley (2008), and Hong (2024) explores the view. I ask whether KDT keeps the practical content of Salow's dissolution, namely Good's (1967) theorem that free evidence never has negative expected value, once knowledge is modeled by the most developed formal theory of inductive knowledge, the normality framework of Goodman and Salow (2023, 2025). My thesis is this:

> In statist normality models, conditioning expected utility on knowledge, or on any factive state that leaves open what rational belief leaves open, respects Good's theorem at a situation only if that state is gapped. In graded models this holds only where knowledge does not go beyond evidence, and the conditional rule modeled on Salow's principle fails wherever the unconditional rule does.

Three results support the thesis. First, an exact boundary (Theorem 1). With K-normality, statism and comparability, KDT gives a free question non-negative value for every decision problem if and only if no situation compatible with what one knows is one where answering would reopen a possibility one now rules out. Every question has non-negative value if and only if knowledge is gapped. Theorem 2 extends the necessity half to any factive state that leaves open what rational belief leaves open, whichever theory of knowledge one adopts. Second, ubiquity. In Goodman and Salow's own model of Bjorn weighing himself twice, KDT prices the free second weighing negatively at every situation, and does so at ten-to-one stakes (§3). Third, the conditional repair fails (§5). I define the expected-utility analogue of Conditional Knowledge Dominance. It handles the bets that motivate it. But in any situation where KDT disvalues a question, some decision problem makes the conditional rule disvalue it too (Theorem 3). Its success elsewhere relies on exact ties between acting now and acting after looking, which generic decision problems do not have.

The closest prior work is as follows. Salow (2025) shows that Weak Knowledge Dominance licenses dogmatism exactly where Preservation fails, and he calls such failures "relatively rare" (36). I give the expected-utility counterpart, with an exact boundary, and show that in graded models failures of Good arise at every situation with inductive knowledge. I also show that his remedy does not carry over to expected utility. Goodman and Salow (2025, henceforth BRN) show that statism, collapse and comparability validate Preservation and that Preservation fails in Bjorn. I give the decision-theoretic counterpart, together with what follows for decisions from their distinction between conditional and post-discovery belief. Geanakoplos (1989), as reported by Das (2023), gives conditions on information structures that suffice for Good's theorem. My contribution is the bridge from normality kens to those conditions, and the result that no belief-containing state other than a gapped one meets them. Hong (2026) argues, according to its abstract, that whatever the normality framework captures is not action-guiding. I could not obtain its text and make no claim about its arguments. My conclusion is narrower than the abstract's: on gapped structures knowledge can set the odds at no cost to Good's theorem.

In plain terms: someone who treats what she has inductively learned from a measurement as settled when she bets will, in the leading model of measurement, sometimes pay to avoid a free second look. The fault lies in how the theory of knowledge interacts with expected utility, not in the bettor.

The essay does not claim that knowledge lacks a practical role, that Good's theorem is sacrosanct, or anything about Salow's qualitative principles taken alone. The result matters beyond formal epistemology. If inductive knowledge, as the leading theory models it, cannot set the odds without making free checking harmful, then knowledge-first accounts of practical reason must either give up a standard criterion of rational inquiry or restrict the role of knowledge to qualitative principles. §2 sets out the framework, §3 the case, §4 the theorems, §5 the conditional repair, §6 objections. Proofs are in the appendix.

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

The phenomenon is not confined to normal situations. At any situation after the first weighing there is a state compatible with Bjorn's knowledge in which the second reading would reopen a weight he now rules out (appendix, A.5). By Lemma 1 below, some bet then makes the free weighing harmful. A second weighing is the ordinary way to check a measurement. A rule that tells Bjorn to avoid it, at every situation, at moderate stakes, is a dogmatist's rule.

## 4. Where Good's theorem holds

The case instantiates a general pattern. Write $M$ for any assignment of a set $M_F(s)\subseteq F$ to situations, used in place of $K$ in the definitions of §2.

**Lemma 1 (defeat is costly).** If some $s_0\in M_E(x)$ has $M_{E\cap\Pi(s_0)}(s_0)\not\subseteq M_E(x)$, then some two-act decision problem gives the question $\Pi$ negative value.

*Proof.* Take a bet $\beta$ paying 1 on $M_E(x)$ and $-L$ elsewhere, and declining, which pays 0. Now $\beta$ has conditional expectation 1, so it is chosen. At $s_0$ the post-answer state contains a state outside $M_E(x)$, which has positive probability, so for large $L$ the agent declines. She then gets 0 where $\beta$ paid 1. Nowhere in $M_E(x)$ does she get more than 1. So $V\le-\Pr(s_0\mid M_E(x))<0$. ∎

**Lemma 2 (laminar sufficiency).** Suppose the post-answer states $\{M'(s): s\in M_E(x)\}$ all lie within $M_E(x)$. Suppose also that they are reflexive ($s\in M'(s)$), transitive ($t\in M'(s)$ implies $M'(t)\subseteq M'(s)$) and nested (any two are disjoint or one contains the other). Then $V\ge0$ for every decision problem.

This is the sufficiency half of a result of Geanakoplos (1989), as reported by Das (2023). I give a short proof in the appendix.

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

**Corollary.** (i) Under statism, collapse and comparability, every K-normality ken is gapped, so KDT makes every question safe. (ii) If $E$ is graded and the questions of Theorem 1(b) are available, expected utility conditioned on any state that leaves open what rational belief leaves open makes every question safe at $x$ only if that state is all of $E$.

Part (i) is the decision-theoretic counterpart of BRN's result that statism, collapse and comparability validate Preservation. Part (ii) says that in graded models the only belief-containing state one can condition on without making some free question harmful is one's evidence. Conditioning on evidence is what Salow calls the fallibilist response, on which "decisions should be governed by underlying probabilities rather than our knowledge" (2025, 23). Bjorn shows that the questions needed for (ii) can be as natural as a second reading.

I also checked the theorems by exhaustive enumeration. The enumeration covered all statist comparable structures with up to four states, every body of evidence, every situation and every partition: 64,004 situation–question pairs. Relative defeat occurred exactly where the ken was not gapped. In each of the 3,306 cases of relative defeat, the decision problem built in Theorem 3 below gave negative KDT value. About 240,000 random decision problems without relative defeat gave no negative value.

## 5. The conditional repair

### 5.1 The rule

The natural expected-utility analogue of Conditional Knowledge Dominance compares two options by their expected difference on the hypothesis that they differ. Let $D_{a,b}=\{s\in E:u_a(s)\ne u_b(s)\}$. Let $K^D_E(x)$ be what one knows on the hypothesis $D$. Its K-normality form restricts evidential accessibility to $D$, as BRN's definition of conditional belief does (App. D.3):
$$K^D_E(x)=\{v\in E\cap D:\text{no }u\in E\cap D\text{ has }u\gg v\}\cup\{v\in E\cap D: v\succeq x\}.$$
Under statism, when $x\in D$, this is the ken one would have on discovering $D$; in every case it contains the belief one would have on discovering $D$. So it respects Salow's constraint that one is "entitled to believe q on the hypothesis that p only if discovering p would not require you to stop believing q" (2025, 33).

**CEU.** Prefer $b$ to $a$ if $\Pr(u_b-u_a\mid K^{D_{a,b}}_E(x))>0$. Looking before acting is one option; its payoff in state $s$ is $u(\alpha_\Pi(s),s)$.

For Bjorn's bet CEU works as Salow's diagnosis predicts. Looking and betting now differ exactly where the second reading would make Bjorn decline. On the hypothesis that this happens, his conditional ken includes losing weights. With the actual readings perfectly accurate, at ten-to-one the bet's expected value on that hypothesis is $-0.63$. So CEU prefers to look. The dogmatic argument fails for the reason Salow gives: on the hypothesis that the evidence makes a difference, you do not know that your verdict is right.

### 5.2 Why the repair fails

The repair relies on states where looking and acting now pay exactly the same. In the bet, these are the states where the second reading leaves the decision unchanged. They are excluded from $D$, so the hypothesis "the options differ" carries information. Generic decision problems have no such exact ties. When two options differ in every state, $D=E$, conditional knowledge is ordinary knowledge, and CEU coincides with KDT. This observation can be turned into a theorem.

**Theorem 3.** Assume statism, comparability and K-normality, and suppose conditional knowledge on the trivial hypothesis $E$ is ordinary knowledge. If there is relative defeat at $x$ for $\Pi$, then some three-act decision problem makes CEU strictly prefer acting now to answering $\Pi$. In it, KDT also gives $\Pi$ negative value.

*Construction.* Let $s_0$ witness relative defeat. The acts are the bet $\beta$ of Lemma 1, declining, and a perturbed bet $\beta_1=\beta+\varepsilon\zeta$, where $\zeta$ is a large positive number $N$ at $s_0$ and $-1$ elsewhere. Choose $N$ so that $\zeta$ has positive expectation on $K_E(x)$; then $\beta_1$ is chosen now. After the answer, any post-answer ken that reopens something declines, given large $L$. Any post-answer ken that reopens nothing excludes $s_0$ (by transitivity, Lemma 3); there $\zeta\equiv-1$, so $\beta$ beats $\beta_1$. So looking never leads to $\beta_1$, and its payoff differs from $\beta_1$'s in every state. Hence $D=E$, and CEU compares the options on $K_E(x)$. At $s_0$, $\beta_1$ pays $1+\varepsilon N$ while looking pays 0. Elsewhere looking gains at most $\varepsilon$. For small $\varepsilon$, $\beta_1$ wins. (Details in the appendix.)

For Bjorn at ten-to-one, take $\zeta$ positive on the states where the second reading would make him decline. CEU then prefers betting now by 0.05, the same margin by which KDT disvalues the weighing.

One might reply that the perturbation is trivial. Surely the rule should condition on the hypothesis that looking makes a *significant* difference. That reply does not help. For any fixed threshold $\theta$, rescale the payoffs so that $\varepsilon$ exceeds $\theta$ and raise $L$; the construction goes through, since nothing in it requires $\varepsilon$ to be small once $N\Pr(s_0\mid K_E(x))>2$ (A.6). More basically, the anti-dogmatic thought behind the repair is that "if the evidence you would discover tells strongly against your view, there is a good chance you're wrong" (Salow 2025, 36). In the perturbed problem, looking makes a difference in every state, including those where, by the agent's knowledge, the evidence misleads. Conditioning on "it makes a difference" then removes nothing, and the knowledge-conditioned weighing that produced the dogmatic verdict returns unchanged.

So CEU is safe at most where KDT is safe. It is sometimes safe at fewer places. In the exhaustive search, CEU strictly preferred acting now in some problems at situations without relative defeat, where KDT is safe. In those problems the hypothesis $D$ is false at $x$, and the conditional ken reopens possibilities that one's knowledge excludes.

### 5.3 Which conditional knowledge?

Even in problems with exact ties, CEU needs a choice that the normality framework does not settle. Without statism, BRN distinguish belief conditional on $q$ (their definition restricts accessibility to $q$ while keeping the current evidence's normality relations) from belief after discovering $q$. They show that the first can hold without the second (App. D.3). Their example is a variant of Flipping for Heads from Goodman and Salow (2023, 138). The coin is fair; $q$ says it was flipped either once or more than $n$ times. Normality comes from probability by BRN's threshold rule. I take $n=4$ and $t=0.9$, so that one initially believes, and in the actual state $s_1$ (heads first) knows, that there were at most four flips. On the hypothesis $q$ one believes there was one flip. After discovering $q$ one leaves five flips open.

Offer twenty-to-one on "at most four flips" and the free question whether $q$. KDT values the question at $-0.53$. Looking changes the payoff exactly on $q$, so $D=q$. On BRN's reading of conditional knowledge, the ken on $D$ at $s_1$ is $\{s_1\}$, and CEU prefers betting now. On the discovery reading it is $\{s_1,s_5\}$, and CEU prefers looking. The same split arises for Salow's qualitative principle restricted to accuracy about the bet's proposition. With BRN's conditional belief, you believe that keeping your belief is better on the hypothesis that the question makes a difference, so Conditional Knowledge Dominance says not to look. So even where the repair can work, it works only if conditional knowledge is post-discovery knowledge. That is Salow's constraint, and outside statist models BRN's account of conditional belief rejects it. Their reason is not idle: conditional belief must make sense for hypotheses one could never learn, such as "p, but I will never learn that p" (App. D.3). A defender of the repair can keep both only by letting the practical role of conditional knowledge diverge from its doxastic role exactly in the non-statist cases that BRN take to be typical.

## 6. Objections and replies

### 6.1 "This is self-trust, not evidence"

The objection says that KDT disvalues questions because the agent distrusts her future self, not because she distrusts the evidence. On the Margins completions (I- and KM-normality), statism, comparability and Margins "together entail no defeat" (Goodman and Salow 2023, 128). There, by Lemma 4, the reopened possibility lies in the agent's own *present* ken at $m$, so the relative defeat in Theorem 2 is a failure of KK at $x$. Such failures harm the empty question too. By Lemma 1 with the trivial partition, a KDT agent without KK at $x$ pays to decide now rather than later on the same evidence. This kin of Williamson's unmarked clock is discussed by Ahmed and Salow (2019) and Das (2023). For the Margins views I concede the objection: what fails there is deference to one's later self, not openness to evidence.

For K-normality the objection fails. KK holds, so by Lemmas 2 and 3 the empty question always has value exactly zero. The negative value of Bjorn's second weighing therefore comes from the evidence. The reading he would see destroys knowledge he now has, in a situation where his knowledge is fully introspective. The structure is the classic dogmatist's. I know the bet wins. In some states compatible with what I know, the evidence will make me unable to rely on that. So I should avoid the evidence. Theorem 1 shows that the structure arises exactly where knowledge is not gapped. So the dilemma for graded inductive knowledge is this. On the KK-friendly completion, KDT avoids evidence. On the KK-unfriendly completions, it avoids deferring to itself.

### 6.2 "Trivial once stated: knowledge is treated as certainty"

The pieces are indeed familiar. Lemma 1 is an ordinary bet, Lemma 2 is Geanakoplos's sufficiency condition, and Corollary (i) parallels BRN's result. Three things are new. The first is the exact location of the boundary, which includes abnormal situations whose kens extend below the belief set. The second is Theorem 2's completion-independence: no belief-containing state other than a gapped one can be conditioned on, so no refinement of knowledge (iterated knowledge, justified true belief) escapes. The third is Theorem 3. Harman's and Kripke's discussions explain why knowledge-as-certainty invites the puzzle. They do not show that the leading conditional remedy fails in expected-utility form. Nor do they show that, on graded normality, conditioning on evidence is the only way out.

### 6.3 "KDT is meant for low stakes"

Stakes-sensitive variants condition on higher-order knowledge when stakes rise (Goldschmidt 2024 surveys them). Under K-normality with transparency, knowledge iterates, so such variants coincide with KDT here. The stakes needed are moderate in any case. Bjorn's case needs only ten-to-one, where the fallibilist bets too.

### 6.4 "Statism is the exception"

BRN argue that statism fails in general. Three replies. Bjorn's model, which carries §3, is statist. Lemma 4 survives without statism in BRN's simple probability structures. If $m_0$ is the most probable member of $p_v$, then $p_v$ consists of the states no more probable than $m_0$. "Not $m_0\gg v$" says that the probability, given $E\cap p_v$, of the states more probable than $v$ is below threshold. By BRN's characterization of belief (Prop. 5) this puts $v$ in $B(E\cap p_v)$. And non-statist models only add failures, as §5.3 shows: discovering what one already knows can destroy knowledge (Goodman and Salow 2023, §8).

### 6.5 Encroachment

Salow (2025, 24 n. 3) reports Hawthorne's (2004, 181) suggestion that, given Good's theorem, the puzzle is handled by pragmatic encroachment of the kind on which encroachment occurs whenever the difference between maximal and actual probability affects one's preferences over the available options. Salow objects that encroachment would not be confined to failures of Preservation (36). Theorem 2 makes the cost exact. To restore Good's theorem for KDT on graded evidence, encroachment must shrink knowledge to the evidence whenever a reopening question is on offer. In Bjorn's case, that means whenever a second scale is in the room.

### 6.6 "Good's theorem is not sacrosanct"

Ahmed and Salow (2019) argue that Good's theorem may fail. What is rational, on their view, is to make one's act depend on the answer to a question, and looking first is rational exactly when it is a way of doing that. Their counterexamples involve inexact, non-partitional observation. Bjorn's second weighing is not of that kind. The reading is observed exactly, the evidence is transparent, and the possible readings partition the states. Looking is therefore a way of making his act depend on the answer to a question, which is the advice they endorse. So the case does not belong among their counterexamples. Some failures of Good's theorem may be rational, but this one is not.

### 6.7 Carter and Hawthorne's inquiry-based dogmatism

Carter and Hawthorne (2024) consider Ex Ante Dogmatism, the recommendation that one avoid gathering evidence bearing on what one knows. They ask how a view on which inquiry aims at knowledge can resist it. The present result is about expected utility, not the aims of inquiry. But it locates exactly where a knowledge-conditioned decision rule recommends ex ante avoidance (non-gapped kens), and it shows that on graded normality that is everywhere.

## 7. Conclusion

In statist normality models, expected utility conditioned on knowledge respects "look before you leap" exactly where knowledge is gapped. Any factive state that leaves open what rational belief leaves open needs the same condition. On graded normality, which Goodman and Salow defend for measurement, that condition means not going beyond the evidence. The expected-utility form of Salow's Conditional Knowledge Dominance does not escape: it disvalues free evidence wherever the unconditional rule does, and in non-statist models its success depends on identifying conditional with post-discovery knowledge. What has not been shown is that no other way of letting all-out attitudes guide graded choice could preserve Salow's dissolution. What follows is a choice for knowledge-first decision theory: give up Good's theorem as a constraint, adopt collapse, or let probabilities conditioned on evidence set the odds and confine knowledge to qualitative roles.

## Appendix: proofs and computations

**A.1 Lemma 2.** Let $\mathcal F=\{M'(s):s\in M\}$, $M=M_E(x)$. By nestedness and reflexivity the inclusion-maximal members of $\mathcal F$ partition $M$. For a maximal $C=M'(c)$, let $a_C$ be the act chosen on $C$. I show by induction on $|C|$ that $\Pr(u(\alpha(s),s)\mid C)\ge\Pr(u_{a_C}\mid C)$. By transitivity every $s\in C$ has $M'(s)\subseteq C$. The states with $M'(s)=C$ choose $a_C$. The others lie in the maximal proper sub-kens $D_1,\dots,D_k$, which are disjoint members of $\mathcal F$ satisfying the hypotheses. By induction, on each $D_j$ the plan does at least as well as the best act on $D_j$, and so at least as well as $a_C$. Summing over the parts of $C$ and then over the maximal sets, the plan's expectation on $M$ is at least $\sum_C\Pr(C\mid M)\max_a\Pr(u_a\mid C)\ge\max_a\Pr(u_a\mid M)$. ∎

**A.2 Lemma 3.** Reflexivity holds because $s\succeq s$. For transitivity, let $t\in K_F(s)$. If $t\in B(F)$, then every $v\succeq t$ is in $B(F)$: if $u\gg v$, chaining gives $u\gg t$. So $K_F(t)=B(F)\subseteq K_F(s)$. If $t\succeq s$, then $\{v:v\succeq t\}\subseteq\{v:v\succeq s\}$. For nestedness, by comparability the sets $\{v: v\succeq s\}$ are linearly ordered by inclusion, and each ken is their union with $B(F)$. ∎

**A.3 Theorem 1.** (a) Answers in different cells give disjoint kens. By Lemma 3 the post-answer kens are reflexive, transitive and nested. Without relative defeat they lie within $K_E(x)$, so Lemma 2 applies. Conversely, use Lemma 1. (b) Suppose the ken is gapped, $s\in K_E(x)\cap c$, and $v\in c\setminus K_E(x)$. Then $s\gg v$, so $v\notin B(E\cap c)$. Also not $v\succeq s$, since otherwise $v\succeq s\gg v\succeq v$ gives $v\gg v$. So $K_{E\cap c}(s)\subseteq K_E(x)$. If the ken is not gapped, Lemma 4 gives relative defeat, because $B(E\cap p_v)\subseteq K_{E\cap p_v}(m)$. ∎

**A.4 Theorem 2.** Lemmas 4 and 1 give the first claim. If $M$ is gapped, $m\in M$ and not $m\gg v$, then $v\in M$; so $M$ is closed under the steps that generate $C(x)$. ∎ *Corollary (i).* Let $m\in K_E(x)$ and $v\notin K_E(x)$. Then not $v\succeq x$, and some $u\gg v$. If $m\succeq x$, comparability and collapse give $x\gg v$, hence $m\gg v$. If $m\in B(E)$, then $v\succeq m$ would give $u\gg m$, so $m$ is strictly more normal than $v$ and collapse gives $m\gg v$. ∎

**A.5 Bjorn.** In coordinates $\mu=(e_1+e_2)/2$ and $d=e_1-e_2$, where $e_i$ are the scale errors, $\delta=2\mu^2+d^2/2$. The post-answer ken at $s$ is the line $d=d(s)$ with $|\mu|\le\max(c/\sqrt2,|\mu_s|)$. Relative defeat holds at every $x$. If $\delta(x)\le c^2$, any $s$ in the ken with $d\ne0$ reopens states with $\delta\in(c^2,c^2+d^2/2]$. If $\delta(x)>c^2$, take $s$ with $\mu_s=0$ and $d(s)^2/2=\delta(x)$; its post-answer ken reaches $\delta=c^2+\delta(x)$. The figures in §3 come from integrating the Gaussian density over the model ($c=1.96$).

**A.6 Theorem 3.** Let $P=\Pr(\cdot\mid K_E(x))$. Pick $N$ with $NP(s_0)>2$. Pick $L$ so large that every post-answer ken containing a state outside $K_E(x)$ declines both bets. Pick $\varepsilon>0$ so small that $\beta_1\ne0$ everywhere. Then $\beta_1$ is chosen now, since its expectation is $1+\varepsilon P(\zeta)>1$. Looking never leads to $\beta_1$, so $D=E$ and CEU uses $K_E(x)$. Then $P(u_{\beta_1}-u_{\text{look}})\ge P(s_0)(1+\varepsilon N)-\varepsilon>0$. ∎

**Computations.** Python scripts enumerate all statist structures satisfying Goodman and Salow's constraints: comparable ones with up to four states (up to five for collapse) and non-comparable ones with up to three. For each they compute kens, post-answer kens, KDT and CEU choices with random full-support priors and the constructed problems. Bjorn's values are computed by numerical integration. Flipping for Heads is computed exactly, truncated at 60 flips.

## References

Ahmed, Arif, and Bernhard Salow. 2019. "Don't Look Now." *British Journal for the Philosophy of Science* 70: 327–350.

Carter, Sam, and John Hawthorne. 2024. "Dogmatism and Inquiry." *Mind* 133: 651–676.

Das, Nilanjan. 2023. "The Value of Biased Information." *British Journal for the Philosophy of Science* 74: 25–55.

Geanakoplos, John. 1989. "Game Theory without Partitions, and Applications to Speculation and Consensus." Cowles Foundation Discussion Paper 914, Yale University.

Goldschmidt, Zeev. 2024. "Foundations for Knowledge-Based Decision Theories." *Australasian Journal of Philosophy* 102: 939–958.

Good, I. J. 1967. "On the Principle of Total Evidence." *British Journal for the Philosophy of Science* 17: 319–321.

Goodman, Jeremy, and Bernhard Salow. 2023. "Epistemology Normalized." *Philosophical Review* 132: 89–145.

Goodman, Jeremy, and Bernhard Salow. 2025. "Belief Revision Normalized." *Journal of Philosophical Logic* 54: 1–49.

Hawthorne, John. 2004. *Knowledge and Lotteries*. Oxford: Oxford University Press.

Hawthorne, John, and Jason Stanley. 2008. "Knowledge and Action." *Journal of Philosophy* 105: 571–590.

Hong, Frank. 2024. "Know Your Way Out of St. Petersburg: An Exploration of 'Knowledge-First' Decision Theory." *Erkenntnis* 89: 2473–2492.

Hong, Frank. 2026. "Normality in Action?" *Philosophical Perspectives*, early view. https://doi.org/10.1111/phpe.70003.

Salow, Bernhard. 2025. "Fallibility and Dogmatism." *Australasian Journal of Philosophy* 103: 23–38.
