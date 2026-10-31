# When Acting on Knowledge Makes Free Evidence Harmful: Good's Theorem in Normality Models

**Abstract.** Knowledge-based decision theory maximizes expected utility with probabilities conditioned on what one knows. I test it against Good's theorem inside Goodman and Salow's normality theory of inductive knowledge. In finite statist, comparable models with K-normality, a free question has non-negative value in every decision problem if and only if no state compatible with one's knowledge is one where the answer would reopen a possibility one now rules out. Given suitable questions, every question is safe if and only if knowledge is *gapped*, and in finite graded models no factive state that contains rational belief is safe unless it is the whole evidence. In Goodman and Salow's model of repeated weighing, a free second weighing has negative value at ten-to-one odds. I then examine three expected-utility developments of Salow's Conditional Knowledge Dominance. Conditioning on the options' differing fails wherever the unconditional rule fails; conditioning on the evidence's changing one's choice also fails. Conditioning answer by answer is safe, but it makes the agent pay to check what she knows, which Conditional Knowledge Dominance forbids.

## 1. Introduction

If you know p, any evidence against p is misleading, so it seems you may avoid it. This is the dogmatism puzzle. Salow (2025) offers a dissolution. If Preservation holds (discovering something consistent with your beliefs never requires giving one up), you cannot believe both p and that you might meet evidence defeating p, so the puzzle never arises. If Preservation fails, the puzzle needs Weak Knowledge Dominance, which Salow replaces with a principle that looks equivalent but is not:

> Conditional Knowledge Dominance: If you know that B's consequences would be better than A's if they're not equally good, you should choose B over A. (Salow 2025, 33)

In Salow's Suitcase, you do not know that the suitcase weighs under 18 kg *on the hypothesis* that it weighs over 17.5 kg, since discovering the latter would defeat that knowledge. So the principle does not tell you to avoid checking. Answering an objection about accuracy, Salow grants that his response "by itself doesn't predict that openness to further evidence is always required", but holds that "a natural development of it will" (2025, 35). The development he has in mind solves "a general problem" about how all-out attitudes guide choices under uncertainty, and "Any solution to that problem will generalize to this one" (2025, 34).

One proposal of that kind is knowledge-based decision theory (KDT): maximize expected utility using probabilities conditioned on what you know. Goldschmidt (2024) proposes axiomatic foundations for knowledge-based decision theories, with a representation theorem for Hawthorne and Stanley's (2008), and Hong (2024) explores the view. I ask whether KDT, and expected-utility versions of Salow's conditional principle, keep Good's (1967) theorem that free evidence never has negative expected value, when knowledge is modeled in Goodman and Salow's (2023, 2025) normality framework. My thesis:

> In finite statist, comparable normality models with K-normality and the requisite questions available, conditioning expected utility on knowledge preserves Good's theorem exactly where knowledge is gapped; of three expected-utility versions of Salow's conditional repair, two fail, and the third succeeds only by abandoning the knowledge-based verdict on costly inquiry.

Theorem 1 identifies when a free question is safe under KDT. Theorem 2 extends its necessity result to factive states containing rational belief. Bjorn's repeated weighing supplies a continuous example with ordinary payoff ratios (§3). Section 5 then distinguishes three conditional evaluations of inquiry. Its negative results concern specified expected-utility rules, not a refutation of Salow's qualitative principle or every knowledge-based decision theory.

Salow (2025, 33) already notes that a 'for all you know' dominance principle can support dogmatism even with Preservation. Goodman and Salow (2025, henceforth BRN) show that statism, collapse and comparability validate Preservation, and that Preservation fails in Bjorn. Geanakoplos (1989) gives sufficient conditions for valuable information beyond partitional learning; Dorst (2020) and Das (2023) develop related epistemological questions. Hong (2026) gives two arguments suggesting that whatever the normality framework captures is not action-guiding. The general decision-theoretic objection is therefore not new.

Dorst et al.'s (2021) *Deference Done Better* supplies an even closer general comparison: Total Trust is equivalent to Value, the requirement that in every decision problem each strategy recommended by the expert's probabilities have expected utility, by one's own probabilities, at least as high as any option (Theorem 2.2).

Here the frame's worlds are the states in $E$, the current probabilities are $\pi=\Pr(\cdot\mid K_E(x))$ and the expert's state-indexed probabilities are $P_s=\Pr(\cdot\mid K_{E\cap\Pi(s)}(s))$. Since the prior has full support, $P_s$ fixes the post-answer ken, so KDT with the fixed tie order is a recommended strategy. Universal safety therefore implies their Weak Value condition, and Value implies universal safety; their Appendix B (§§B.1–B.2) proves Weak Value equivalent to Total Trust and to Value. So a question is safe at $x$ exactly when $\pi$ totally trusts this frame, and Theorem 1 characterizes, within these normality models, when it does.

Their Theorem 4.1 already characterizes Total Trust for any finite frame, by requiring the relevant candidate expert functions to be 'modestly informed' and $\pi$ to lie in their convex hull. The increment here is to state that boundary in normality-theoretic terms, as relative defeat and gappedness, together with the graded-model consequence and the tests of three conditional inquiry rules.

## 2. Framework

I follow Goodman and Salow (2023) and BRN. A *normality structure* has a set $S$ of states, a family $\mathcal{E}$ of possible bodies of evidence, and two relations on situations $\langle s,E\rangle$ (with $s\in E\in\mathcal{E}$): $\succeq$ (at least as normal as), a preorder, and $\gg$ (sufficiently more normal than). $\gg$ implies $\succeq$, is irreflexive, and *chains*: if $w_1\succeq w_2\gg w_3\succeq w_4$ then $w_1\gg w_4$. Under *statism* both relations are evidence-independent, so I treat them as relations on states. *Comparability* says any two states with the same evidence are $\succeq$-related. *Collapse* says every strict difference in normality is sufficient. For the theorems $S$ is finite.

Rational belief, given evidence $E$, rules out exactly the evidential possibilities that something else in $E$ is sufficiently more normal than:
$$B(E)=\{s\in E:\ \text{no } u\in E \text{ has } u\gg s\}.$$
Knowledge goes beyond evidence by the same mechanism, but its extent depends on where one actually is. I work mainly with *K-normality* (Goodman and Salow 2023, 104):
$$K_E(x)=B(E)\cup\{v\in E: v\succeq x\}.$$
One knows what is true throughout $K_E(x)$, which I call one's *ken*. This is the set of possibilities one has not ruled out by knowledge; a smaller ken means knowing more. Evidence is transparent, and Goodman and Salow note that "given TRANSPARENCY, K-NORMALITY entails KK" (2023, 107). Their alternatives, I- and KM-normality, validate their principle Margins and allow failures of KK (see §6.1 below). Discovering $p$ at $\langle x,E\rangle$ yields $\langle x,E\cap p\rangle$. A *question* is a partition $\Pi$ of $E$ whose cells are discoverable ($E\cap c\in\mathcal{E}$ for each cell $c$); $\Pi(s)$ is the cell containing $s$.

**Knowledge-based expected utility.** Fix a prior $\Pr$ with full support. A *decision problem* is a finite set $A$ of acts, each a function from states to utilities. At $\langle x,E\rangle$, KDT chooses an act maximizing $\Pr(u_a\mid K_E(x))$, ties broken by a fixed order.

**The value of a free question.** Let $\alpha_\Pi(s)$ be the act KDT chooses at $\langle s,E\cap\Pi(s)\rangle$. The KDT value of answering $\Pi$ before choosing is
$$V_x(\Pi,A)=\sum_s \Pr(s\mid K_E(x))\,u(\alpha_\Pi(s),s)\;-\;\max_{a\in A}\Pr(u_a\mid K_E(x)).$$
This is Good's comparison of acting now with looking and then acting, with $\Pr(\cdot\mid K_E(x))$ in place of the unconditioned probability. Call $\Pi$ *safe* at $x$ if $V_x(\Pi,A)\geq 0$ for every decision problem $A$.

*Relative defeat* at $x$ for $\Pi$: some $s\in K_E(x)$ has $K_{E\cap\Pi(s)}(s)\not\subseteq K_E(x)$. For all one knows, answering would leave open something one now rules out.

*Gapped*: every member of $K_E(x)$ is sufficiently more normal than every member of $E\setminus K_E(x)$. The gap must separate every retained possibility from every excluded one, not merely the most normal possibilities from the least normal.

States settle what an unconsulted source would say. This is already so in Goodman and Salow's model, where what Bjorn knows after one weighing depends on the second scale's reading (2023, 128) and he has inductive knowledge "about the scales' future readings" (2023, 130 n. 40). The conditioning set is therefore fixed at the time of choice and is the same for both options. If states also settled whether one looks, the conditioning set would depend on the act being evaluated. That is a different route to failures of Good's theorem, and I set it aside.

## 3. Bjorn's second weighing

Goodman and Salow's (2023, §6) model of Bjorn is statist and comparable, and it violates collapse. Its states are triples $\langle w,y_1,y_2\rangle$: Bjorn's weight and the readings of two scales. With $\delta=(w-y_1)^2+(w-y_2)^2$, one state is at least as normal as another iff its $\delta$ is no larger, and sufficiently more normal iff its $\delta$ is smaller by more than $c^2$. Goodman and Salow derive these relations from independent Gaussian errors (2023, 129). I take the standard deviation as the unit and, following BRN (§5, n. 18), set $c\approx1.96$.

After the first reading $r$, Bjorn believes his weight lies in $[r-c,r+c]$. Under K-normality, in any situation with $\delta\le c^2$ this belief is knowledge, and his ken is $\{\delta\le c^2\}$. After a second reading $r'$ he believes his weight lies within $c/\sqrt2$ of the average of the two readings. As Goodman and Salow show for the case where the first reading is accurate and the second within $c$ of it, he "loses knowledge" whenever $|r-r'|>(2-\sqrt2)c$ (2023, 127). Since the readings may differ by up to $\sqrt2c$ for all he believes, he believes that the second weighing might defeat his knowledge: a failure of Preservation, the case BRN use against it.

With independent unit Gaussian errors, losing the old weight-interval belief has unconditioned probability about $0.417$ (about $0.356$ conditional on his present knowledge). BRN's estimate, about $0.37$, concerns the narrower event of losing it while the discovery remains consistent with the old beliefs: $(2-\sqrt2)c<|r-r'|\le\sqrt2c$ (§5, n. 18). Over the full state space, including the readings, Preservation fails at every nonzero difference up to $\sqrt2c$, with probability about $0.95$. These are different events.

**Ten-to-one bet.** After the first weighing Bjorn is offered a bet: win 1 if his weight is within $c$ of $r$, lose 10 otherwise. He knows the bet wins, so KDT takes it. A free second weighing is then offered. After it he would decline the bet whenever the readings differ by more than about $1.12c$, because his new ken gives the losing weights enough probability. Conditional on his present knowledge, this has probability about 0.05, and in each such state he forgoes a payoff he now knows he would get. So KDT values the free weighing at about $-0.05$; at twenty-to-one, $-0.12$; at a hundred-to-one, $-0.27$.

A fallibilist who uses the unconditioned probabilities also takes the ten-to-one bet (it wins with probability $0.95$; expected value $0.95-10(0.05)=0.45$), and by Good's theorem the second weighing has positive value for her.

The magnitudes depend on $c$. On Goodman and Salow's probabilistic account of "sufficiently more normal" (2023, 121), applied to these errors, $c^2=-2\ln(1-t)$ for probability threshold $t$; so $c\approx1.96$ corresponds to $t\approx0.85$. At $t=0.95$ ($c\approx2.45$) the ten-to-one value is about $-0.01$ and the hundred-to-one value about $-0.15$.

Three claims about other situations should be kept apart.

(i) At *every* situation after the first weighing, some state compatible with Bjorn's knowledge has a second reading that reopens a *state* he now rules out, and a bet on the proposition he knows, paying 1 if it holds and losing a finite amount otherwise, makes the second weighing harmful (appendix, A.5). That proposition concerns the readings as well as his weight.

(ii) A reopened *weight* exists only if $\max(c^2,\delta(x))<(1+\sqrt2)^2c^2$; beyond that, which has probability about $10^{-5}$, no bet of this form on his weight alone does the job (A.5).

(iii) Theorem 2 and its corollary are finite results using the questions defined in §4; the second weighing is not one of them.

## 4. Where Good's theorem holds

The proof separates two tasks: showing how reopened possibilities can make inquiry costly, and identifying a structure that prevents such costs. The first lemma handles the danger; the next two provide the sufficient conditions.

Write $M$ for any assignment of a set $M_F(s)\subseteq F$ to situations, used in place of $K$ in the definitions of §2.

**Lemma 1 (defeat is costly).** If some $s_0\in M_E(x)$ has $M_{E\cap\Pi(s_0)}(s_0)\not\subseteq M_E(x)$, then some two-act decision problem gives $\Pi$ negative value.

*Proof.* Take a bet $\beta$ paying 1 on $M_E(x)$ and $-L$ elsewhere, and declining, which pays 0. $\beta$ has conditional expectation 1, so it is chosen. At $s_0$ the post-answer state contains a state outside $M_E(x)$, of positive probability, so for large $L$ the agent declines and gets 0 where $\beta$ paid 1. Nowhere in $M_E(x)$ does she get more than 1. So $V\le-\Pr(s_0\mid M_E(x))<0$. ∎

**Lemma 2 (laminar sufficiency).** Suppose the post-answer states $\{M'(s): s\in M_E(x)\}$ all lie within $M_E(x)$ and are reflexive ($s\in M'(s)$), transitive ($t\in M'(s)$ implies $M'(t)\subseteq M'(s)$) and nested (any two are disjoint or one contains the other). Then $V\ge0$ for every decision problem.

This applies Geanakoplos's value-of-information result (1989, Theorem 1); a short proof is in the appendix.

**Lemma 3.** Under statism and comparability, for each $F$ the kens $\{K_F(s):s\in F\}$ are reflexive, transitive and nested.

**Theorem 1.** Assume statism, comparability and K-normality.
(a) A question is safe at $x$ if and only if there is no relative defeat at $x$ for it.
(b) If $K_E(x)$ is gapped, every question is safe at $x$. If it is not, then for some $v\in E\setminus K_E(x)$ the question whether $p_v$, where $p_v=\{u\in E: \text{not } u\gg v\}$, is unsafe at $x$ if it is available.

Part (a) combines Lemmas 1–3. Part (b) needs only one question at a time, and it rests on a lemma that uses no K-normality.

**Lemma 4 (non-gaps are defeasible).** Assume statism. Let $m\in M_E(x)$ and $v\in E\setminus M_E(x)$, with not $m\gg v$. Then $m,v\in p_v$ and $v\in B(E\cap p_v)$.

*Proof.* $m\in p_v$ by hypothesis and $v\in p_v$ by irreflexivity. Nothing in $p_v$ is sufficiently more normal than $v$. ∎

Learning $p_v$ is learning that things are not far more normal than $v$: that one's situation is somewhat abnormal. Goodman and Salow's own example of such a discovery, that an experiment did not end on its first trial, defeats knowledge only in a model without statism (2023, 136). Probabilistic models predict widespread failures of statism, and theirs obey it only for the bodies of evidence they consider (2023, 138 n. 47); so the statism assumption must cover the extended family.

Say that $M$ *leaves open what rational belief leaves open* if always $B(F)\subseteq M_F(s)$. Knowledge on each of Goodman and Salow's three completions does, and so do justified true belief and iterated knowledge.

**Theorem 2 (only gapped states can be conditioned on).** Assume statism, with belief defined from normality as above, and suppose $M$ leaves open what rational belief leaves open. If $M_E(x)$ is not gapped, then for some $v$ the question whether $p_v$, if available, is unsafe at $x$ for expected utility conditioned on $M$. A gapped set containing $x$ contains $C(x)$: the states reachable from $x$ by steps, each to a state that is not sufficiently less normal than the last.

The boundary in Theorem 1 is not the boundary of Preservation. Take three states $a,b,c$, in decreasing order of normality, with $a\gg b$ and $a\gg c$ but not $b\gg c$. Preservation holds here for every body of evidence and every discovery. At $b$ one knows $\{a,b\}$; learning that $a$ is false, which is true at $b$, reopens $c$. This is the expected-utility counterpart of Salow's observation about the 'for all you know' variant, located exactly.

Call $E$ *graded* if $C(x)=E$ for every $x\in E$. Bjorn's evidence after one reading is graded, since a chain of small increases in $\delta$ connects any two states.

**Corollary.** (i) Under statism, collapse and comparability, every K-normality ken is gapped, so KDT makes every question safe. (ii) In a finite graded model, if the questions whether $p_v$ are available, expected utility conditioned on a factive state that leaves open what rational belief leaves open makes them all safe at $x$ only if that state is all of $E$.

Part (i) is the decision-theoretic counterpart of BRN's result that statism, collapse and comparability validate Preservation. Part (ii) says that, given these questions, the only belief-containing state one can condition on in finite graded models without some free question becoming harmful is one's evidence. Conditioning on evidence is the response on which "decisions should be governed by underlying probabilities rather than our knowledge" (Salow 2025, 23). Part (ii) depends on the available questions. It does not establish the same necessity result for the second weighing alone.

## 5. The conditional repair

### 5.1 Three developments

The three proposals differ in what they treat as the relevant hypothesis: a difference in payoff, a change of decision, or a particular answer.

Conditional Knowledge Dominance evaluates options on the hypothesis that they differ. Salow's moral is that "you should always think that, if the evidence you would discover tells strongly against your view, there is a good chance you're wrong" (2025, 36). He gives no expected-utility version. Write $K^D_E(x)$ for what one knows on the hypothesis $D$. Its K-normality form restricts evidential accessibility to $D$, as BRN's definition of conditional belief does (App. D.3):
$$K^D_E(x)=\{v\in E\cap D:\text{no }u\in E\cap D\text{ has }u\gg v\}\cup\{v\in E\cap D: v\succeq x\}.$$
Under statism, when $x\in D$, this is the ken one would have on discovering $D$; in every case it contains the belief one would then have. So it respects Salow's constraint that one is "entitled to believe q on the hypothesis that p only if discovering p would not require you to stop believing q" (2025, 33). Write $u_\ell(s)=u(\alpha_\Pi(s),s)$ for the payoff of looking, and compare looking with an act $a$ in three ways:

(Difference) CEU: look if $\Pr(u_\ell-u_a\mid K^{D}_E(x))\ge0$, where $D=\{s:u_\ell(s)\neq u_a(s)\}$.

(Verdict) VER: look if $\sum_b \Pr(D_b\mid K_E(x))\Pr(u_b-u_a\mid K^{D_b}_E(x))\ge0$, where $D_b=\{s:\alpha_\Pi(s)=b\}$; one conditions on what the evidence would lead one to do.

(Answer) ANS: look if $\sum_c \Pr(c\mid K_E(x))\Pr(u_\ell-u_a\mid K^{c}_E(x))\ge0$, summing over the cells of $\Pi$.

These formulas evaluate the future KDT policy $\alpha_\Pi$; they do not define fully recursive VER or ANS decision theories.

All three handle Bjorn's bet as Salow's diagnosis predicts. Looking and betting now differ exactly where the second reading would make Bjorn decline, and on that hypothesis his conditional ken includes losing weights. With the actual readings perfectly accurate, at ten-to-one the bet's expected value on that hypothesis is $-0.60$, so CEU and VER prefer to look; ANS does too, since each decline cell's conditional ken is the post-answer ken.

### 5.2 Difference and verdict

CEU's hypothesis carries information only because equal-payoff states are excluded from it. A perturbation removes them: if looking and acting now differ at every state, $D=E$, conditional knowledge is ordinary knowledge, and CEU coincides with KDT.

**Theorem 3.** Assume statism, comparability and K-normality. If there is relative defeat at $x$ for $\Pi$, some three-act decision problem makes CEU strictly prefer acting now to answering $\Pi$, even if CEU also governs every later choice. KDT gives $\Pi$ negative value too. These verdicts persist on an open neighborhood of the constructed payoffs.

*Construction.* Let $M=K_E(x)$ and choose $s_0\in M$ witnessing relative defeat. Take the bet $\beta$ of Lemma 1, declining, and $\beta_1=\beta+\varepsilon\zeta$, where $\zeta(s_0)=N$ and $\zeta=-1$ elsewhere, $N$ gives $\zeta$ positive current mean, and $0<\varepsilon<1$. Choose $L$ so large that every post-answer ken meeting $E\setminus M$ strictly prefers declining; there are finitely many. Every other post-answer ken excludes $s_0$, since otherwise transitivity would put $s_0$'s reopened possibilities in it; there $\beta$ strictly beats $\beta_1$ and declining. So looking never selects $\beta_1$, which is uniquely best now. All acts differ pairwise at every state, and $\beta_1$ differs everywhere from the looking policy; so every comparison CEU makes, now or later, uses ordinary knowledge, CEU agrees with KDT, and no cycle can arise. The gain from acting now at $s_0$ outweighs the small losses elsewhere (A.6).

For a numerical illustration, take three states $a\succ b\succ c$ with only $a\gg c$, a uniform prior, and $x=a$, whose ken is $\{a,b\}$. Ask whether $a$; on the other answer the ken is $\{b,c\}$. Let the acts pay $(1,1,-10)$, $(0,0,0)$ and $(0.9,1.5,-10.1)$. Both rules choose the third now (expectation $1.2$). After looking they choose the first at $a$ and decline at $b$ and $c$, a policy with current expectation $0.5$. CEU prefers acting now by $0.7$.

Theorem 3 refutes CEU, not Conditional Knowledge Dominance. In the constructed problems the qualitative principle is silent: the most normal state $m^*$ of $E$ lies in the ken, its post-answer ken lies inside the ken and excludes $s_0$, and there looking yields $\beta$, which beats $\beta_1$. So one does not know that $\beta_1$ is better whenever they differ. More generally, in these models, when looking and acting now differ at every state, Conditional Knowledge Dominance never forbids a free look (A.7). CEU extends the principle into its silence, and there it behaves as KDT does.

VER conditions on a hypothesis in the spirit of Salow's moral: that the evidence would change what one does. It escapes Theorem 3 for large $L$, because the conditional ken on 'I would decline' then contains an excluded state, where $\beta_1$ loses heavily.

A five-state case shows its limitation. Take states $a,s_2,s_1,v_2,v_1$ with normality ranks $0,0.2,0.5,1.15,1.3$ (lower is more normal), $u\gg w$ iff $w$'s rank exceeds $u$'s by more than 1, prior $(0.67,0.01,0.30,0.01,0.01)$, $x=a$, and the question $\{\{a\},\{s_1,v_1\},\{s_2,v_2\}\}$. The ken is $\{a,s_1,s_2\}$; both non-trivial answers reopen something. Use Theorem 3's acts with $s_0=s_1$, $N=10$, $\varepsilon=0.001$, $L=30.4$. Looking yields $\beta$ at $a$ and declining elsewhere. On the hypothesis 'I would decline', the conditional ken is $\{s_1,s_2,v_2\}$: $s_2\gg v_1$ excludes $v_1$, but $v_2$ survives with too little weight to sink $\beta_1$, whose expected value there is $0.028$. VER prefers acting now by $0.008$. Every pair of primitive acts differs everywhere, so later choices are KDT's.

VER, and CEU too, can even disvalue a question where there is no relative defeat. Take $a\succ x\succ b\succ c$ with $a\gg x,b,c$ and $x\gg c$ only, a uniform prior, the situation $x$ (ken $\{a,x\}$), the question $\{\{x\},\{b,c\},\{a\}\}$, and two acts paying $(-2,3.1,-2,2.1)$ and $(3,3,3,-3)$ at $(a,x,b,c)$. No answer reopens anything, and looking does at least as well as acting now throughout the ken, so KDT values the question at $0.05$. On the hypothesis 'I would choose the first act', however, the conditional ken is $\{x,b\}$, and $b$ lies only in an answer she knows to be false; VER and CEU prefer acting now. Conditioning on what the evidence would lead one to do imports possibilities the evidence itself would not make live.

### 5.3 Answer by answer

**Proposition 4.** Assume statism, comparability and K-normality. ANS never prefers acting now to a free question.

*Proof.* Fix a cell $c$. If $s\in K^c_E(x)$, then $K_{E\cap c}(s)\subseteq K^c_E(x)$: if $s\in B(E\cap c)$ its ken is $B(E\cap c)$ (by the chaining step in A.2), and if $s\succeq x$ then $\{v\succeq s\}\subseteq\{v\succeq x\}$. These kens are reflexive, transitive and nested (Lemma 3), so Lemma 2 with $K^c_E(x)$ in place of $M_E(x)$ makes each summand non-negative. ∎

The price appears when evidence is not free.

**Proposition 5.** Under the same assumptions, if there is relative defeat at $x$ for $\Pi$, there are a bet $\beta$ and a price $\kappa>0$ such that ANS prefers paying $\kappa$ and answering $\Pi$ to taking $\beta$ now, although the two options differ at every state and $\beta$ pays more at every state of the ken. Conditional Knowledge Dominance therefore requires taking $\beta$.

*Proof sketch* (A.7). Use Lemma 1's bet. The conditional ken on the cell of $s_0$ contains an excluded state, so for large $L$ that cell's summand is large, while the others are non-negative. Choose also $0<\kappa<L$. Inside the ken, looking at a price pays at most $1-\kappa<1$; outside it pays $-\kappa\neq-L$. ∎

In Bjorn at normal situations ($c\approx1.96$), ANS pays up to 0.019 for the second weighing at ten-to-one. At a hundred-to-one it pays up to 1.23, more than the bet pays in any state she has not ruled out, for evidence about a proposition she knows. ANS secures Good's theorem by valuing inquiry with the mixture $\sum_c\Pr(c\mid K_E(x))\Pr(\cdot\mid K^c_E(x))$, which gives excluded possibilities positive weight; for inquiry, knowledge no longer settles the probabilities.

Restricting ANS to free questions, with costly inquiry left to KDT or Conditional Knowledge Dominance, avoids Proposition 5 at another cost: in Bjorn's case the agent then looks at price zero and refuses at every positive price, however small. Thus ANS, this particular conditional repair, keeps free-inquiry safety at the cost of conflicting with Conditional Knowledge Dominance on costly inquiry.

Outside statist models conditional belief and belief after discovery can diverge (BRN App. D.3), and each rule needs separate assessment there.

## 6. Objections and replies

### 6.1 "This is self-trust, not evidence"

The objection says that KDT disvalues questions because the agent distrusts her future self, not the evidence. On the Margins completions, statism, comparability and Margins "together entail NO DEFEAT" (Goodman and Salow 2023, 128). There, by Lemma 4, the reopened possibility lies in the agent's own *present* ken at $m$, so the relative defeat in Theorem 2 is a failure of KK at $x$. Such failures harm the empty question too: by Lemma 1 with the trivial partition, a KDT agent without KK at $x$ pays to decide now rather than later on the same evidence, a cousin of the unmarked-clock case discussed by Ahmed and Salow (2019). For the Margins views I concede the objection. Goodman and Salow report, however, that Goldstein and Hawthorne's (2022) model of multiple observations predicts failures of No Defeat "even given MARGINS" (2023, 130 n. 40), so this escape may be less clean; I have not checked the bet in that model.

For K-normality the objection fails. KK holds, so by Lemmas 2 and 3 the empty question never has negative value (at abnormal situations it can even have positive value). In Bjorn the new reading destroys knowledge despite positive introspection. The structure is the classic dogmatist's: I know the bet wins, the evidence might stop me relying on that, so I avoid it. On the KK-friendly completion, KDT avoids evidence; on the others, it avoids deferring to itself.

### 6.2 Stakes and encroachment

A ten-to-one payoff ratio is not an absolute measure of stakes: at a fixed ken, positive rescaling of utilities preserves choices and the sign of information value. The finite theorems use large $L$; Bjorn shows that ten-to-one suffices at $c\approx1.96$ (§3).

The main reply is pragmatic encroachment. Hawthorne (2004, 181), as Salow reports, suggests that given Good's result the puzzle is handled by the proposal "developed by Fantl and McGrath (2002) and Weatherson (2005)" that encroachment occurs "whenever the difference between maximal and actual probability affects your preferences over available options" (Salow 2025, 24 n. 3). Since the theorems hold the ken fixed across problems, such views escape them.

Bjorn's case makes one consequence concrete. Offered the ten-to-one bet alone at a normal situation, he bets both under knowledge-conditioned evaluation (win probability 1) and under evidence-conditioned evaluation (0.95). Offered the bet and a free second scale, the former evaluation strictly prefers acting now, while the latter strictly prefers looking (§3). An encroachment criterion that withdraws knowledge whenever these two evaluations rank the available options differently therefore withdraws it on the mere offer of free evidence. This consequence is conditional on extending the criterion to these evaluations of inquiry; no general result about every graded state follows from it.

Salow objects that it is unclear what would confine encroachment to "these relatively rare counterexamples to Preservation" (2025, 36); in the measurement model the counterexamples are not rare (§3).

### 6.3 Statism and questions

BRN suggest that statism is "the exception rather than the rule" (§7). Bjorn, however, is statist. Beyond it, the questions are whether post-answer kens stay nested and whether Lemma 4's questions still reopen excluded possibilities. On the probabilistic grounding, normality is relative to a question: Goodman and Salow note that relativizing to *how much does Bjorn weigh* yields a model like Goldstein and Hawthorne's, in which current knowledge is not sensitive to future observations (2023, 130 n. 40). A weight bet may make that question salient. I have not computed the bet there.

### 6.4 "Good's theorem is not sacrosanct"

Ahmed and Salow (2019) argue that Good's theorem "may be false", using, among other cases, observations that are not partitional. Bjorn's readings partition the evidential possibilities exactly. The failure arises elsewhere: knowledge is lost, so the post-answer probabilities are not the present knowledge-conditioned probabilities conditioned on the reading, and the later self's policy is not the reading-dependent policy the present self would choose. A defender may accept that foresight of such choices can make looking bad. That concedes predictable, evidence-driven knowledge loss with practical cost, which Salow's dissolution aimed to show harmless. If the agent could commit to ignoring an answer, the present best act stays available and a free signal cannot hurt; the results concern looking followed by the specified later rule, without commitment.

## 7. Conclusion

In finite statist, comparable models with K-normality and the questions whether $p_v$ available, expected utility conditioned on knowledge makes every free question safe exactly where knowledge is gapped; any factive state that leaves open what rational belief leaves open needs the same condition. On graded normality, which Goodman and Salow defend for measurement, that condition means not going beyond the evidence, and in their own model a free second weighing has negative value at ordinary odds. Of three expected-utility developments of Conditional Knowledge Dominance, conditioning on the options' differing and on the evidence changing one's choice both fail; conditioning answer by answer succeeds, but it pays to check what one knows, contrary to the principle it develops. What has not been shown is that no other way of letting all-out attitudes guide graded choice could deliver the development Salow anticipates, or what happens in non-statist models. The burden on knowledge-conditioned expected utility is precise: weaken the universal safety requirement, restrict the models or questions (collapse is one sufficient restriction), let stakes or offers change knowledge, or stop letting knowledge settle the probabilities used to evaluate inquiry.

## Appendix: proofs and computations

**A.1 Lemma 2.** Let $\mathcal F=\{M'(s):s\in M\}$, $M=M_E(x)$. By nestedness and reflexivity the inclusion-maximal members of $\mathcal F$ partition $M$. For a maximal $C$, let $a_C$ be the act chosen on $C$.

By induction on $|C|$, $\Pr(u(\alpha(s),s)\mid C)\ge\Pr(u_{a_C}\mid C)$: by transitivity every $s\in C$ has $M'(s)\subseteq C$; states with $M'(s)=C$ choose $a_C$; the others lie in the maximal proper sub-kens $D_1,\dots,D_k$, disjoint members of $\mathcal F$ satisfying the hypotheses, on each of which the plan does at least as well as the best act on $D_j$, hence as $a_C$.

Summing, the plan's expectation on $M$ is at least $\sum_C\Pr(C\mid M)\max_a\Pr(u_a\mid C)\ge\max_a\Pr(u_a\mid M)$. ∎

**A.2 Lemma 3.** Reflexivity: $s\succeq s$. Transitivity: let $t\in K_F(s)$. If $t\in B(F)$, every $v\succeq t$ is in $B(F)$ (if $u\gg v$, chaining gives $u\gg t$), so $K_F(t)=B(F)\subseteq K_F(s)$. If $t\succeq s$, $\{v:v\succeq t\}\subseteq\{v:v\succeq s\}$. Nestedness: by comparability the sets $\{v: v\succeq s\}$ are linearly ordered by inclusion, and each ken is their union with $B(F)$. ∎

**A.3 Theorem 1.** (a) Kens in different cells are disjoint; by Lemma 3 the post-answer kens are reflexive, transitive and nested; without relative defeat they lie within $K_E(x)$, so Lemma 2 applies. Conversely, Lemma 1. (b) Suppose the ken is gapped, $s\in K_E(x)\cap c$, $v\in c\setminus K_E(x)$. Then $s\gg v$, so $v\notin B(E\cap c)$; and not $v\succeq s$, since $v\succeq s\gg v\succeq v$ would give $v\gg v$. So $K_{E\cap c}(s)\subseteq K_E(x)$. If the ken is not gapped, Lemma 4 gives relative defeat for the question whether $p_v$, because $B(E\cap p_v)\subseteq K_{E\cap p_v}(m)$. ∎

**A.4 Theorem 2.** Lemmas 4 and 1 give the first claim. If $M$ is gapped, $m\in M$ and not $m\gg v$, then $v\in M$; so $M$ is closed under the steps generating $C(x)$. ∎ *Corollary (i).* Let $m\in K_E(x)$, $v\notin K_E(x)$. Then not $v\succeq x$, and some $u\gg v$. If $m\succeq x$, comparability and collapse give $x\gg v$, hence $m\gg v$. If $m\in B(E)$, then $v\succeq m$ would give $u\gg m$, so $m$ is strictly more normal than $v$ and collapse gives $m\gg v$. ∎

**A.5 Bjorn.** After the first reading, let $\mu=(e_1+e_2)/2$ and $d=e_1-e_2$ for the scale errors, so $\delta=2\mu^2+d^2/2$; for the numerical model, $\mu\sim N(0,1/2)$ and $d\sim N(0,2)$ independently (the swamped-prior treatment of weight). A second reading fixes $d$, and the post-answer ken of a state $s$ is $|\mu|\le\max(c/\sqrt2,|\mu_s|)$. Let $R=\max(c^2,\delta(x))$, so the current ken is $M=\{\delta\le R\}$. Choose $s$ with $\mu_s=0$ and $d_s^2/2$ strictly between $R-c^2$ and $R$; its post-answer ken reaches $\delta=c^2+d_s^2/2>R$. By strictness, a small open neighborhood $U$ of $s$ stays inside $M$ and has post-answer probability of $M^c$ at least some $\eta>0$, and $U$ has positive probability. A bet paying 1 on $M$ and $-L$ elsewhere, with $L>(1-\eta)/\eta$, is declined throughout $U$ and accepted now, so looking has value at most $-\Pr(U\mid M)<0$.

For weights: $e_1=\mu+d/2$, and by Cauchy–Schwarz $|e_1|\le\sqrt R$ throughout $M$. A post-answer ken of $s\in M$ reaches $|e_1|$ up to $\max(c/\sqrt2,|\mu_s|)+|d_s|/2$. If $|\mu_s|> c/\sqrt2$, this is at most $\sqrt R$; otherwise its maximum, $c/\sqrt2+\sqrt{R/2}$, exceeds $\sqrt R$ iff $R<(1+\sqrt2)^2c^2$. Under the Gaussian model $\Pr(\delta\ge(1+\sqrt2)^2c^2)\approx1.4\times10^{-5}$. The normal-situation figures in §3 integrate the density over $\delta\le c^2$ for the bet on $|e_1|\le c$.

**A.6 Theorem 3.** Put $P=\Pr(\cdot\mid M)$, choose $N$ with $NP(s_0)>2$ and fix $0<\varepsilon<1$. For each post-answer ken $F$ meeting $E\setminus M$, $q_F=\Pr(E\setminus M\mid F)>0$; the expectations of $\beta_1$ and $\beta$ on $F$ are at most $1+N-Lq_F$, so $L>(1+N)/\min_F q_F$ makes declining strictly best on every such $F$, for every $\varepsilon<1$. On every other post-answer ken, $\beta_1=1-\varepsilon$ and $\beta=1$. Now $\beta_1$ is uniquely optimal since $P(\zeta)>0$. At $s_0$ acting now gains $1+\varepsilon N$; elsewhere in $M$ looking gains at most $\varepsilon$. So $P(u_{\beta_1}-u_{\ell})\ge P(s_0)(1+\varepsilon N)-\varepsilon>0$. Outside $M$ looking declines while $\beta_1=-L-\varepsilon$; inside, looking pays 0 or 1, neither equal to $\beta_1$. So the difference event is $E$, and likewise for every pair of primitive acts. Finitely many strict inequalities and nonzero differences persist under small perturbations. ∎

**A.7 CKD silence; Propositions 4–5.** *Silence.* Let $m^*$ be $\succeq$-maximal in $E$ and $c^*$ its cell. If $v\notin K_E(x)$, some $u\gg v$ and chaining gives $m^*\gg v$; so $B(E\cap c^*)\subseteq K_E(x)$, and every state there has post-answer ken $B(E\cap c^*)$ and chooses one act $b^*$, optimal on that set. If looking differs from $a$ everywhere, $b^*$ beats $a$ at some state of $B(E\cap c^*)$, so one does not know that $a$ is better whenever they differ.

*Proposition 5.* Let $c_0=\Pi(s_0)$. If $s_0\succeq x$, $K^{c_0}_E(x)\supseteq K_{E\cap c_0}(s_0)$; if $s_0\in B(E)$, the part of $K_{E\cap c_0}(s_0)$ above $s_0$ lies in $B(E)$ by chaining, so its excluded states lie in $B(E\cap c_0)\subseteq K^{c_0}_E(x)$. Either way $K^{c_0}_E(x)$ contains an excluded state, with probability $q>0$ in it. By the proof of Proposition 4, the $c_0$ summand is at least $-\Pr(u_\beta\mid K^{c_0}_E(x))\ge Lq-1$ and the others are non-negative; so choose $0<\kappa<\min\{L,\Pr(c_0\mid K_E(x))(Lq-1)\}$. ∎

**Computations.** Supporting scripts enumerate statist comparable structures with up to four states, every nonempty body of evidence, situation and non-trivial partition (64,004 situation–question pairs; 3,306 with relative defeat). Structural enumeration is exhaustive within that domain; sampled priors and utilities test examples, not the universal decision-problem quantifiers proved above. The examples in §5.2 were also evaluated directly. Bjorn's decision values and knowledge-conditional probabilities use numerical integration. His weight-belief-loss probability is $\operatorname{erfc}((2-\sqrt2)c/2)$; subtracting $\operatorname{erfc}(c/\sqrt2)$ gives loss with a consistent discovery.

## References

Ahmed, Arif, and Bernhard Salow. 2019. "Don't Look Now." *British Journal for the Philosophy of Science* 70: 327–350.

Das, Nilanjan. 2023. "The Value of Biased Information." *British Journal for the Philosophy of Science* 74: 25–55.

Dorst, Kevin. 2020. "Evidence: A Guide for the Uncertain." *Philosophy and Phenomenological Research* 100: 586–632.

Dorst, Kevin, Benjamin A. Levinstein, Bernhard Salow, Brooke E. Husic, and Branden Fitelson. 2021. "Deference Done Better." *Philosophical Perspectives* 35: 99–150. https://doi.org/10.1111/phpe.12156.

Fantl, Jeremy, and Matthew McGrath. 2002. "Evidence, Pragmatics, and Justification." *Philosophical Review* 111: 67–94.

Geanakoplos, John. 1989. "Game Theory without Partitions, and Applications to Speculation and Consensus." Cowles Foundation Discussion Paper 914, Yale University. Revised version in *B.E. Journal of Theoretical Economics* 21 (2021): 361–394.

Goldschmidt, Zeev. 2024. "Foundations for Knowledge-Based Decision Theories." *Australasian Journal of Philosophy* 102: 939–958.

Goldstein, Simon, and John Hawthorne. 2022. "Knowledge from Multiple Experiences." *Philosophical Studies* 179: 1341–1372.

Good, I. J. 1967. "On the Principle of Total Evidence." *British Journal for the Philosophy of Science* 17: 319–321.

Goodman, Jeremy, and Bernhard Salow. 2023. "Epistemology Normalized." *Philosophical Review* 132: 89–145.

Goodman, Jeremy, and Bernhard Salow. 2025. "Belief Revision Normalized." *Journal of Philosophical Logic* 54: 1–49.

Hawthorne, John. 2004. *Knowledge and Lotteries*. Oxford: Oxford University Press.

Hawthorne, John, and Jason Stanley. 2008. "Knowledge and Action." *Journal of Philosophy* 105: 571–590.

Hong, Frank. 2024. "Know Your Way Out of St. Petersburg: An Exploration of 'Knowledge-First' Decision Theory." *Erkenntnis* 89: 2473–2492.

Hong, Frank. 2026. "Normality in Action?" *Philosophical Perspectives*, early view. https://doi.org/10.1111/phpe.70003.

Salow, Bernhard. 2025. "Fallibility and Dogmatism." *Australasian Journal of Philosophy* 103: 23–38.

Weatherson, Brian. 2005. "Can We Do Without Pragmatic Encroachment?" *Philosophical Perspectives* 19: 417–443.
