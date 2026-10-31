# Holistic Accuracy and the Limits of Lockean Derivation

**Abstract.** Dorst argues that maximizing expected accuracy yields Lockean thresholds for belief even without separability. I distinguish two readings of his holistic extension. Mere truth-directedness and order independence do not suffice: a score rewarding an error-free body of belief makes a proposition believed at one credence and withheld at a higher one, with values and context fixed. The stronger reading requires restrictions on marginal values that the stated argument does not establish. For a single score, marginal extensionality and background-independent thresholds recover separability on a specified domain. A separate theorem gives cross-space refinement invariance as one sufficient route to thresholds, not a necessary condition for Lockeanism on a fixed space. The counterexample's optima select a core and its above-threshold consequences. An earlier utility theory of guessing already generates similar behavior; the contribution is its realization under the strict marginal truth-directedness at issue in Dorst's argument. Accuracy maximization alone therefore leaves the bridge from credence to belief unsettled.

## 1. Introduction

The difference at issue is between becoming more confident in a proposition and being rationally required to believe it. A fixed threshold makes the two move together within a context: once belief is required, a further increase in credence cannot reverse that verdict. The counterexample below separates them while holding the accuracy score fixed.

Accuracy-first epistemology holds that rational doxastic states are those that best promote accuracy by the agent's own lights. With a separable score for outright belief, positive for true beliefs and negative for false ones, it yields a Lockean thesis: believe a proposition just in case your credence in it exceeds a threshold. Easwaran (2016) proved this, using expected score as a tool for showing such belief states non-dominated, and stated the analogue for values varying with the proposition, which yields proposition-specific thresholds; Dorst (2019) presents these results as his Theorem 1 and Corollary 2 and credits both to Easwaran (p. 183).

Dorst's own further claim is about holism. Separability, the assumption that a state's accuracy is the sum of its members' accuracies, "seems to contradict epistemic holism" (p. 192, citing Joyce 2009, §5). Dorst argues that dropping it changes nothing: given a premise he calls Sequence-Irrelevance, fixed proposition-specific thresholds follow anyway (his Proposition 5).[^1]

My thesis is that Proposition 5 does not follow on the unrestricted reading of holism suggested by its motivation. On a stronger reading, the values introduced in the argument already restrict holism, and those restrictions need defending. I give a counterexample to the unrestricted claim, identify the restrictions that repair the derivation, and examine refinement invariance as a separate sufficient route to thresholds. I do not claim that Lockeanism or Separability is false, or that my counterexample is the correct measure of epistemic value.

The argument has three parts. First, a truth-directed score with a premium for an error-free belief state violates fixed thresholds for every positive premium (Section 3). The bridge from optimization to rationality requires only that some state be permitted at each credence. Second, order independence does not justify the restrictions on marginal values used in Dorst's proof (Section 4). For a single measure satisfying marginal extensionality, background-independent marginal thresholds require separability on the stated domain. Third, the score's optima have an exact core-based characterization (Section 5). Refinement invariance can recover Lockean thresholds, but its unrestricted cross-space form is stronger than the fixed-space conclusion originally sought (Section 6).

The closest prior work includes Rothschild's (2023) additive scoring representations of Lockean belief and Wang's (2025) expected-utility rules for deductively cogent belief states. Levi (1967) accepts the consequences of an answer chosen by expected epistemic utility; Leitgeb (2014, 2017) connects rational belief to stably high credence and a strongest believed proposition. Holguín (2022) defends non-monotone, question-sensitive rational thinking. Dorst and Mandelkern (2022) derive filtered guesses by maximizing expected answer-value and connect belief to their consequences. Their model already reproduces the two belief sets in my main example. The claimed increment is consequently narrower: a counterexample under strict marginal truth-directedness on unrestricted belief states, a diagnosis of Dorst's derivation, and an exact characterization of this particular score's optima. Section 5 makes the overlap explicit.

The philosophical issue is the division of work between accuracy and a theory of belief's role. If a question licenses selecting a working hypothesis, an accuracy-based account can permit dependence on competing answers. If each proposition must instead be evaluated independently of those competitors, additional constraints are needed. Neither the counterexample nor its repairs decide which conception of belief is right. They show where that substantive choice enters, rather than letting an optimization theorem settle it silently.

## 2. Dorst's derivation

Let $W$ be a finite set of worlds, propositions subsets of $W$, and a belief state $B$ any set of propositions. Accuracy First leaves inconsistent, nonclosed and empty states among the options (Dorst 2019, p. 183). An accuracy measure assigns a real number $A(B,w)$ to each state at each world. Given a probability function $C$ on $W$, expected accuracy is $EA_C(B)=\sum_w C(w)A(B,w)$, and Maximize Expected Accuracy says that $B$ is rational only if no state has higher expected accuracy. To connect optimization to rational permission, I require only:

(Non-vacuity) At every credence under consideration, at least one belief state is rationally permitted.

Maximize Expected Accuracy alone gives only a necessary condition. Together with Non-vacuity it makes a unique optimum rationally permitted; it need not permit every tied optimum. Section 7 returns to this distinction.

Under Separability, $A(B,w)=\sum_{p\in B}v_p(w)$, where $v_p(w)=T_p>0$ if $w\in p$ and $v_p(w)=F_p<0$ otherwise. Then $EA_C(B)=\sum_{p\in B}e_p$ with
$$e_p = C(p)T_p+(1-C(p))F_p ,$$
so every optimum includes $p$ when $e_p>0$ and excludes it when $e_p<0$. The threshold is $\tau_p=-F_p/(T_p-F_p)$. Call the values conservative when $T_p<-F_p$; then $\tau_p>1/2$. This extends Dorst's Conservativeness, $|T|<|F|$ for uniform values (p. 185); his Variable Conservativeness for proposition-dependent values instead requires $|T_p|<|F_{\neg p}|$ and $|T_{\neg p}|<|F_p|$ (p. 191), and lets thresholds fall below $1/2$.

Separability makes the decision local. Adding one proposition leaves the contributions of every other belief unchanged, so its expected contribution alone determines whether it belongs in an optimum. The holistic extension must explain how the same threshold structure survives when the values of beliefs can interact.

In §4.2 Dorst lets the measure depend on the agent's current state $B_0$, "to capture the sense in which it matters what other beliefs she holds" (p. 193). Adding $p$ to $B_0$ raises the score where $p$ is true and lowers it where $p$ is false; Dorst writes the increments as $T^{B_0}_p$ and $F^{B_0}_p$ and remarks that this "assumes only that $A_{B_0}$ is well-defined" (p. 193). Proposition 4 then gives a threshold for the last proposition added in a sequence. Sequence-Irrelevance says that "rational constraints on beliefs are not affected by the sequence (if any) in which they are formed" (p. 194), and Proposition 5 concludes that there are "belief-independent values $T_p$ and $F_p$" fixing a threshold for each proposition (p. 195).

Two features of Proposition 5's scope matter below. Its $T_p$ and $F_p$ are values of the measure in a context, not functions of the credences. The proof obtains them by setting $T_p$ equal to $T^{B^-}_p$ for a state $B^-$ (p. 207). And Dorst's reply to the worry that variable Lockeanism is empty depends on it: the thresholds "come from the (dis)values of true (false) beliefs" (p. 196). So a score under which, with values and context fixed, a proposition is believed at one credence and not at a higher one refutes the proposition.

Second, I read Sequence-Irrelevance as Dorst states it, as a constraint on rationality: the order in which a final state was formed does not change its rational status. Section 3 shows that the counterexample respects it on that reading.

## 3. The counterexample

Define the *record measure* with premium $\beta>0$:
$$A_\beta(B,w)=\sum_{p\in B}v_p(w)+\beta\cdot[\,w\in{\textstyle\bigcap} B\,],$$
where $\bigcap\varnothing=W$ and $[\cdot]$ is 1 if the condition holds and 0 otherwise. Call $\bigcap B$ the *core* of $B$: the strongest proposition the state commits its holder to. The premium rewards the truth of that total commitment. A state whose core is true is one from which any multi-premise deduction yields only truths, and a body of belief can be valuable as a whole in this way, which is the holist's thought.

Dorst motivates Separability by an exam scored question by question (p. 184); many exams also reward a perfect paper. The premium does not grow with the number of beliefs, because it rewards one proposition, the core; the informativity of a state is rewarded by the separable part. The empty state's core is $W$, whose truth is trivial, so it earns the premium everywhere, as an uninformative answer should.

The measure is purely alethic: $A_\beta(B,w)$ depends only on $B$ and on which of its members are true at $w$.

It meets the unrestricted truth-directedness condition motivating §4.2, but not the stronger marginal-value restriction introduced there. Adding a true $p$ raises $A_\beta$ by exactly $T_p$, since if every member of $B_0$ was true at $w$, all still are. Adding a false $p$ lowers it by $|F_p|$, or by $|F_p|+\beta$ if $B_0$ was error-free at $w$. So the measure is strictly truth-directed, and every increment is conservative when $T_p<-F_p$. It does not depend on the current state, so Maximize Expected Accuracy issues one verdict about final states however they are reached, and every belief state is an option.

*The case.* Let $W=\{w_1,w_2,w_3\}$, $T_p=1$ and $F_p=-2$ for every $p$ (so $\tau=2/3$), and $\beta=3$. Write $\mathbf 1=\{w_1\}$, $12=\{w_1,w_2\}$ and $13=\{w_1,w_3\}$. The two credence functions below assign probabilities to these same worlds in the same order. The score, premium and proposition being tested are held fixed.

At $C=(0.70,0.15,0.15)$ the unique optimum among all $2^8$ states is $\{\mathbf 1,12,13,W\}$, with expected accuracy $4.30$. The runner-up, $\{12,13,W\}$ at $4.20$, has the same core and lacks only $\mathbf 1$, so the margin is $e_{\mathbf 1}=0.10$: here the separable term decides.

At $C'=(0.75,0.01,0.24)$ the unique optimum is $\{13,W\}$, with $4.94$; the runner-up is $\{\mathbf 1,12,13,W\}$ at $4.75$. Here the premium decides: the core $13$ is nearly certain, and its premium outweighs what the more specific core adds. (The optimum at $C'$ also omits $12$, whose credence $0.76$ exceeds $\tau$.)[^2]

So $\mathbf 1$ is believed at credence $0.70$ and not at $0.75$. By Non-vacuity and Maximize Expected Accuracy, each unique optimum is rationally permitted, and Proposition 5 would require $\tau_{\mathbf 1}\le 0.70$ and $\tau_{\mathbf 1}\ge 0.75$.

The reversal becomes intelligible once the whole distribution is considered. In the second distribution, probability is concentrated on the first and third worlds. A less specific core can therefore retain almost all the probability while reducing the risk of a false total commitment. The increased confidence in the first world does not, by itself, settle which body of belief scores best.

This reversal does not depend on the particular numbers just chosen. Every positive premium permits a range of cases with the same structure:

**Theorem 1.** Let $0<T<-F$, $\beta>0$, $D=T-F$, $\tau=-F/D$, and
$$c_0=\frac{\beta-T-2F}{2D+\beta},\qquad c_1=\frac{\beta-2F}{2D+\beta}.$$
Then $\max(c_0,\tau)<c_1<1$, and for all $c<c'$ in $(\max(c_0,\tau),c_1)$, $\mathbf 1$ belongs to the unique optimum at $(c,\frac{1-c}{2},\frac{1-c}{2})$ and to no optimum at $(c',\varepsilon,1-c'-\varepsilon)$, for all sufficiently small $\varepsilon\ge 0$.

The proof is in the Appendix. For $0<\beta\le D$ the interval has length $\beta T/(D(2D+\beta))$: it narrows as the premium shrinks but never closes. This instantiates what Holguín calls Non-Monotonicity: an agent can be permitted to think $p$ at a lower credence and not at a higher one (2022, §5).

*Fixed context.* A defender may reply that variable Lockeanism already lets belief in $p$ depend on credences in alternatives. In Dorst's model of the question "Who do you think will win?", the question lowers the penalty for falsely believing answers of the form "x wins" "until it gets an answer" (p. 190). Whether one believes that Steve wins at credence $0.48$ then depends on whether a rival is more probable. But in that model the dependence enters through a change of values, driven by the demand that the question be answered, which is not itself an expected-accuracy calculation; within each context belief is monotone in credence. The record measure produces the dependence with values, question and context fixed, as a consequence of maximizing expected accuracy. This matters for Holguín's objection that sophisticated Lockeanism requires "brute stipulations about the coordination of the proposition-sensitive thresholds" and "remains powerless to account for non-monotonicity" (2022, §7.2). Here no coordination is stipulated.

*Order.* The record measure does make one procedure order-dependent. At $C$, an agent who starts from the empty state and considers $\mathbf 1$ first gains $e_{\mathbf 1}-\beta C(\{w_2,w_3\})=0.1-0.9=-0.8$, declines it, and ends greedily at $\{12,13,W\}$. Considering $\mathbf 1$ last, she gains $0.1$ and ends at the optimum.

Dorst's example of designing a sequence to make belief in God rational (p. 194) might suggest a violation of Sequence-Irrelevance. It is not one. Proposition 4 is a necessary condition: a final state is rational only if it maximizes expected accuracy relative to its predecessor. A global optimum meets that condition however it is written as the last step of a sequence, so Proposition 4 applies to it in every order. The greedy outcome is not an optimum, so under Maximize Expected Accuracy it is not rational whatever sequence produced it. No sequence confers rationality on any state.

What depends on order is a procedure that Maximize Expected Accuracy does not endorse; Dorst himself says the process of forming beliefs in sequence "may be purely imaginative" (p. 194).

## 4. Diagnosis

*The quantifier gap.* Truth-directedness gives, for each world where $p$ is true, some positive increment. The passage on p. 193 then names one number $T^{B_0}_p$ as "the value" of adding a true belief in $p$. That moves from "for every $w$ there is a $t$" to "there is a $t$ for every $w$." Under the record measure, adding the false $\mathbf 1$ to $\{13\}$ costs 2 at $w_2$ but 5 at $w_3$, since only at $w_3$ was the prior state error-free. In expectation,
$$EA_C(B)-EA_C(B\setminus\{p\})=e_p-\beta\,C\big({\textstyle\bigcap}(B\setminus\{p\})\setminus p\big),$$
a threshold on $C(p)$ that moves with the credence of the rest of the core outside $p$. The step needs:

(ME) *Marginal extensionality.* For every $B_0$ and $p\notin B_0$, $A(B_0\cup\{p\},w)-A(B_0,w)$ depends on $w$ only through whether $w\in p$.

ME is not a consequence of well-definedness. It says the marginal value of a belief depends on the world only through that belief's own truth value. The distinction is between the sign and the size of the change. Truth-directedness fixes whether adding a belief helps or hurts at a world. ME additionally fixes the size of that change across worlds where the added belief has the same truth value.

*The content gap.* Grant ME. Proposition 4 then yields thresholds $\tau^{B^-}_p$ indexed to $B^-$, the rest of the state, and the proof of Proposition 5 generalizes from one $B^-$ to all. That requires $\tau^{B^-}_p$ not to vary with $B^-$. Sequence-Irrelevance cannot supply this: $B^-$ is not a sequence but the content of the other beliefs, which is what the holist says matters. Dorst himself separates the two: "no holist ever thought that the insight of their position is that the order in which you consider propositions affects what you ought to believe" (p. 195). The natural strengthening is:

(BI) *Background-independence.* $T^{B_0}_p$ and $F^{B_0}_p$ do not depend on $B_0$, for states $B_0$ not containing the complement of $p$.

**Theorem 2.** Let $A$ be truth-directed, and consider states containing no proposition together with its complement.[^3] (a) $A$ satisfies ME iff $A(B,w)=A(\varnothing,w)+\kappa(B)+\sum_{p\in B}J_p\,[w\in p]$ for a world-independent $\kappa$ and constants $J_p>0$ (the sum over contingent $p\in B$). (b) $A$ satisfies ME and BI iff $\kappa$ is additive, that is, iff $A(B,w)=A(\varnothing,w)+\sum_{p\in B}v_p(w)$ for proposition-dependent values $v_p$.

The proof (Appendix) turns on one observation: adding $p$ and $q$ in either order gives the same total, and under ME one side of the resulting identity is affine in $[w\in p]$, the other in $[w\in q]$. Since $A(\varnothing,w)$ is common to all states, (b) returns us to the separable measures of Corollary 2.

The proof yields more than the theorem states. Under ME the gain $J^{B}_p=T^{B}_p-F^{B}_p$ is the same for every background $B$, so $\tau^{B}_p=-F^{B}_p/J_p$.

**Corollary.** Under ME, on the stated domain, the threshold for $p$ is background-independent iff BI holds. Hence the step from $\tau^{B^-}_p$ to a single $\tau_p$ in the proof of Proposition 5 is valid iff $A$ is separable on that domain.

So, under ME, reading Sequence-Irrelevance strongly, as requiring background-independent thresholds, is no weaker than BI. And the Corollary yields a dilemma.

Under ME, the only holism left is the world-independent $\kappa$ of Theorem 2(a), so the belief-dependence Dorst explicitly permits must take that form, and an additive $\kappa$ is just separability. If he admits it, Proposition 5 fails: a small bonus for deductively closed states satisfies ME and truth-directedness and makes belief non-monotone.[^4] If he excludes it, his §4.2 measures are separable on the domain, and §4.2 adds nothing to Corollary 2. Without ME, the record measure is a counterexample.

Theorem 2 concerns a single measure. Dorst's measures are indexed to the current state; for such a family, ME at each member's own state, together with BI read across the family (the increments $T^{B_0}_p$ and $F^{B_0}_p$ of $A_{B_0}$ at $B_0$ do not depend on $B_0$), yields fixed thresholds through Proposition 4 without collapsing the family into one separable measure. The counterexample is unaffected, since a state-independent measure is a constant family.

## 5. What holism delivers instead

The counterexample leaves a constructive question: what replaces a fixed threshold when the score rewards an error-free record? The answer gives the agent a reason to assess beliefs together, while still requiring each accepted belief to make a non-negative expected contribution.

The record measure's optima have an exact description. For each proposition $X$ let
$$\Phi(X)=\beta\,C(X)+\sum_{p\supseteq X}\max(e_p,0).$$

The first term rewards the probability that the core is true. The second adds the positive expected contributions of its consequences. The comparison therefore concerns both the security of a total commitment and the individually worthwhile beliefs that commitment supports. The following theorem shows that comparing these core values suffices to find the optimal belief states.

**Theorem 3.** For any finite $W$ and proposition-dependent values, $\max_B EA_C(B)=\max_X\Phi(X)$. A state $B$ is optimal iff its core maximizes $\Phi$, $B$ contains every $p\supseteq\bigcap B$ with $e_p>0$, and $B$ contains no $p$ with $e_p<0$. Call the case *generic* when $\Phi$ has a unique maximizer $X^*$ and no $C(p)$ equals a threshold. With uniform values, in the generic case the unique optimum is $B^*=\{p\supseteq X^*: C(p)>\tau\}$, and: (i) $B^*$ is consistent iff $X^*\neq\varnothing$, and it is closed under single-premise entailment; (ii) $X^*$ contains every world more probable than any world it contains; (iii) $B^*$ is deductively closed iff $C(X^*)>\tau$, in which case it consists of exactly the consequences of $X^*$.

Call this *core-relative Lockeanism*. The agent selects a working hypothesis $X^*$, trading its probability against the above-threshold content it entails, and believes the above-threshold propositions it entails. Lockean belief is the special case in which the best core is the intersection of all above-threshold propositions. Closure can fail: on four worlds with $C=(0.62,0.18,0.10,0.10)$ and the values of Section 3, the unique optimum believes $\{w_1,w_2\}$ and $\{w_1,w_3\}$ but not $\{w_1\}$.

Dorst and Mandelkern (2022, §§3–4.1) already derive filtered guesses by maximizing epistemic utility and, following Holguín, connect belief to their consequences. Their Jamesian expected answer-value is $C(X)J^{I_Q(X)}$, where $I_Q(X)$ is the proportion of question cells ruled out and $J\ge1$. On the singleton question, $J=125/64$ selects $\mathbf 1$ at $C$ and $13$ at $C'$: their scores are respectively $35/32$ versus $17/16$, and $75/64$ versus $99/80$. Taking all consequences gives exactly the belief sets in Section 3. This is an instantiation of their model, not their printed numerical example. Neither the reversal nor the filtered-core structure is new.

Theorem 3 identifies a more specific result. It optimizes a score on unrestricted belief states with strict gains for adding truths and strict losses for adding falsehoods. Scoring a state simply by its conjunction's Jamesian value would fail that requirement: adding an entailed proposition leaves the score unchanged. Moreover, $\Phi$ depends on the credences of individual consequences, not just the core's probability and informativeness. Its output can omit the core itself; part (iii) identifies when deductive closure holds. Levi and Leitgeb, like the single-guess entailment bridge, accept all consequences of the selected proposition. The contribution is this optimizer characterization in Dorst's setting, not a first utility-theoretic derivation of guess-based belief.

Increasing the premium, with credences and values fixed, cannot lower the credence of the optimal core (add the optimality inequalities at the two premiums), so it favors more probable cores; when world probabilities are distinct, (ii) makes these broader cores, which entail fewer beliefs. When every world has positive credence, $\Phi(W)-\Phi(X)$ grows linearly in $\beta$ for every proper $X$, so a large enough premium leaves only $W$ believed. The score therefore requires a defended balance between acquiring truths and protecting the joint truth of what one believes. Calling both aims accuracy does not fix their relative weight.

## 6. Refinement

A score on whole belief states must also confront a problem of representation. Describing possibilities in greater detail creates more propositions to count, even when the credence of the original proposition stays fixed. The record measure combines a sum over propositions with a single premium, so this change can alter their balance.

Skipper (2023, §3.2) already raises a related objection to Dorst and Mandelkern: dividing alternatives outside two candidate guesses can reverse their ranking. His alternative specificity measure preserves that ranking when the answers compatible with each guess stay fixed (§4). The invariance condition below has a different scope: it preserves belief verdicts across every coarsening, including changes within a candidate proposition. The general concern about irrelevant refinements is therefore not new.

The strongest reply to the counterexample is that it depends on how possibilities are individuated. Split the 1% world of $C'$ into two worlds of credence $0.005$. On the refined space $\Phi(\mathbf 1)=7.25$ exceeds $\Phi(\{w_1,w_3\})=6.91$, so $\mathbf 1$ is believed at $0.75$; it is also believed at the correspondingly refined $C$. The non-monotonicity is gone.

In general, with uniform values, splitting a world of credence zero into $k$ worlds multiplies the separable part of $\Phi$ for every core excluding it by $2^{k-1}$, since each pair of coarse supersets that differ only on that world becomes $2^k$ refined supersets of equal credence, and it leaves the premium term alone, so by Theorem 3 the core is chosen as if the premium were $\beta/2^{k-1}$, and for fixed $\beta$ the interval of Theorem 1 shrinks exponentially in $k$. The premium is paid once while the separable sum ranges over the whole algebra. Verdicts about a fixed question should not depend on how unrelated possibilities are counted, and separable scores meet that demand.

Two repairs are available. First, the culprit is the flat sum. Replace it with the mean over the algebra $\mathcal A$: $A(B,w)=|\mathcal A|^{-1}\sum_{p\in B}v_p(w)+b\,[w\in\bigcap B]$. On a fixed space this only rescales the premium, so Theorems 1 and 3 apply unchanged.

Splitting a credence-zero world now leaves the $\Phi$-value of every core that excludes it, and so every verdict, exactly unchanged. In the case of Section 3 (with $b=3/8$), splitting $w_2$ into 2, 4 or 8 equiprobable worlds, at both $C$ and $C'$, leaves both verdicts in place.

Second, Dorst's accuracy function already takes "a set of propositions" as an argument (p. 179). Let that set be the algebra generated by the question in context. Splitting worlds that the question does not distinguish then changes nothing.

Neither repair yields invariance under every refinement. A theorem explains why that stronger requirement excludes the present non-Lockean behavior. A *coarsening* is a surjection $\pi:W\to W^*$; it carries a credence $C$ on $W$ to $C^*=C\circ\pi^{-1}$ and identifies $p^*\subseteq W^*$ with $\pi^{-1}(p^*)$. Suppose the context assigns a measure to each finite space.

(RI) *Refinement invariance.* For every coarsening $\pi$, credence $C$ and $p^*\subseteq W^*$, $\pi^{-1}(p^*)$ belongs to every (some) optimum at $C$ iff $p^*$ belongs to every (some) optimum at $C^*$.

(CI) *Conservative increments.* On every two-world space, adding a contingent $p$ to any state gains less at the world where $p$ is true than it loses at the world where $p$ is false.

**Theorem 4.** Suppose every measure is truth-directed and CI and RI hold. Then for each contingent proposition $p$ there is a $\tau_p\in(1/2,1)$, fixed by the measure on the two-world coarsening $\{p,W\setminus p\}$, such that on every space and at every credence, $p$ belongs to every optimum if $C(p)>\tau_p$ and to none if $C(p)<\tau_p$.

The proof (Appendix) reduces every verdict on $p$ to the two-world problem that asks only whether $p$. Truth-directedness and CI then give a single threshold above $1/2$. Separable measures whose values are preserved under coarsening satisfy RI. The record measure does not: on the two-world coarsening its threshold for $\mathbf 1$ is $(\beta-F)/(D+\beta)=5/6$, although on three worlds it believes $\mathbf 1$ at $0.70$. CI is needed for the theorem's conservativeness conclusion: separable values $T_p=2$, $F_p=-1$ satisfy RI but give threshold $1/3$.

RI is one sufficient repair, not a necessary premise of every Lockean derivation. For example, assign uniform separable values $T=1$, $F=-n$ to each $n$-world space, $n\ge2$. Every fixed space is Lockean, with threshold $n/(n+1)$, but the family violates RI. Dorst's fixed-context conclusion does not itself require those thresholds to survive changes of space. The theorem establishes the stronger cross-space result; it must not be used to equate fixed-space Lockeanism with refinement invariance. There are thus two distinct tasks: deriving a threshold within one representation, and showing that the threshold survives a change of representation. Success at the first does not automatically secure the second.

The refinement objection therefore splits in two. Its restricted form, invariance under refinements that leave the question fixed, is met by the question-relative record measure. Its unrestricted form requires the verdict on whether horse 1 wins to survive replacing "Which horse wins?" with "Does horse 1 win?", when the family of measures treats that change as a coarsening within one context. That is a substantive restriction on question dependence. Dorst's proposition-specific values can accommodate contextual changes; Holguín instead allows the salient alternatives to affect rational thinking directly (2022, §§7.2, 8.1). An advocate of RI must explain why these changes should preserve the relevant context. Its sufficiency is informative, but accuracy maximization and order independence do not supply that explanation. Whether a weaker general invariance condition already forces thresholds remains open.

## 7. Objections

*The premium is not accuracy; it double-counts the conjunction.* The premium is alethic: it depends only on which believed propositions are true. It is not a disguised belief in the core, since in the four-world case it accrues on $\{w_1\}$, which is not believed. And it respects strict truth-directedness, the constraint Dorst places on holistic measures. The objector may insist that genuine accuracy is local, so that a belief's contribution depends only on its own truth. That is ME. With BI it yields separability, but ME alone leaves the term $\kappa$ of Theorem 2(a), and Section 4's dilemma applies. Excluding the premium on these grounds denies the holism §4.2 set out to accommodate. Someone may still find the premium unmotivated. Then the dispute is about the value of an error-free body of belief, which is my claim.

*Maximize Expected Accuracy gives only a necessary condition; perhaps neither optimum is rational.* A purely necessary norm can indeed permit nothing, and then no counterexample establishes a rational state violating its conclusion. Non-vacuity excludes that response without declaring every optimum rational. At the two credences of Section 3 the optimum is unique, so it must be the permitted state. In Theorem 1 all optima agree on the relevant verdict. The objection therefore survives only by rejecting this existence requirement or by imposing an additional restriction that excludes the score.

*The result is negative only; Dorst's picture survives.* In part, yes. Belief remains a function of credence and contextual values, and Dorst's gloss of beliefs as "best guesses" (p. 196) fits core-relative Lockeanism at least as well as Lockeanism. What does not survive is the claim that accuracy forces the Lockean form. That matters to Holguín's argument, which targets that form: non-monotonicity tells against sophisticated Lockeanism, not against accuracy-first epistemology.

## 8. Conclusion

On its unrestricted reading, Dorst's holistic extension does not derive fixed Lockean thresholds. A record premium satisfies strict truth-directedness and order-independent maximization while producing non-monotone belief; Non-vacuity connects that optimization result to rational permission. On a stronger reading, the derivation needs restrictions on marginal values. For a single measure, marginal extensionality plus background-independent marginal thresholds recovers separability on the stated domain. Cross-space refinement invariance is a different sufficient route, with a stronger conclusion and its own substantive commitments. Earlier theories already make belief guess-like; the record measure shows how a particular version arises under the strict accuracy conditions at issue here. Defending Lockeanism from accuracy therefore requires defending the restrictions that select its form, rather than treating order independence as sufficient.

## Appendix: Proofs

*Proof of Theorem 1.* Write $e_p=C(p)D+F$; note $\tau>1/2$. At $C_c=(c,\frac{1-c}{2},\frac{1-c}{2})$ with $c>\tau$, the positive terms are $e_{\mathbf 1}$, $e_{12}=e_{13}$ and $e_W=T$; all others are negative (their credences are at most $1-c<1/2$). Then $\Phi(\mathbf 1)-\Phi(W)=e_{\mathbf 1}+2e_{12}-\beta(1-c)=c(2D+\beta)+T+2F-\beta$, positive iff $c>c_0$. Also $\Phi(\mathbf 1)-\Phi(13)=e_{\mathbf 1}+e_{12}-\beta\frac{1-c}{2}=\frac12(\Phi(\mathbf 1)-\Phi(W))+\frac12e_{\mathbf 1}>0$. Next, $\Phi(\mathbf 1)-\Phi(\{w_2\})=e_{\mathbf 1}+e_{12}+\beta\frac{3c-1}{2}>0$ and $\Phi(\mathbf 1)-\Phi(\{w_2,w_3\})=e_{\mathbf 1}+2e_{12}+\beta(2c-1)>0$; the cores $12$ and $\{w_3\}$ are symmetric; and $\Phi(\mathbf 1)-\Phi(\varnothing)=\beta c>0$. By Theorem 3 the unique optimum has core $\mathbf 1$ and contains $\mathbf 1$.

At $(c',0,1-c')$ with $\tau<c'$: $e_{\mathbf 1}=e_{12}=c'D+F>0$ and $e_{13}=e_W=T$, so $\Phi(13)-\Phi(\mathbf 1)=\beta(1-c')-2e_{\mathbf 1}$, positive iff $c'<c_1$, while $\Phi(\varnothing)=\Phi(\mathbf 1)-\beta c'$. A state containing $\mathbf 1$ has core $\mathbf 1$ or $\varnothing$, so no optimum contains $\mathbf 1$; these strict inequalities persist for small $\varepsilon$.

Finally, $c_1-c_0=T/(2D+\beta)$, $c_1-\tau=\beta T/(D(2D+\beta))$ and $1-c_1=2T/(2D+\beta)$ are positive. ∎

*Proof of Theorem 2.* Write $\Delta_p^B(w)=A(B\cup\{p\},w)-A(B,w)$ for $p\notin B$. Under ME, $\Delta_p^B=F_p^B+J_p^B[w\in p]$ for contingent $p$, and $\Delta_p^B$ is constant for $p\in\{\varnothing,W\}$; truth-directedness gives $F_p^B<0<F_p^B+J_p^B$.

(i) Let $p,q\notin B$ be distinct, $q$ not the complement of $p$. Computing $A(B\cup\{p,q\},\cdot)-A(B,\cdot)$ in both orders gives $\Delta_p^B-\Delta_p^{B\cup\{q\}}=\Delta_q^B-\Delta_q^{B\cup\{p\}}$. The left side is $\alpha+(J_p^B-J_p^{B\cup\{q\}})[w\in p]$, the right side $\gamma+\delta[w\in q]$, or constant if $q$ is trivial. If $p,q$ are contingent, distinct and not complementary, $1,[w\in p],[w\in q]$ are linearly independent, so $J_p^{B\cup\{q\}}=J_p^B$; if $q$ is trivial, the same follows.

(ii) Building any $B$ that contains neither $p$ nor its complement from $\varnothing$ one member at a time, (i) gives $J_p^B=J_p^\varnothing=:J_p$.

(iii) For $B$ without complementary pairs, add its members in any order: $A(B,w)-A(\varnothing,w)=\kappa(B)+\sum_{p\in B}J_p[w\in p]$, where $\kappa(B)$, the sum of the $F$-terms and constant increments, is world-independent, and order-independent because the total is. The converse of (a) is immediate.

For (b), BI says $F^{B}_p=\kappa(B\cup\{p\})-\kappa(B)$ is independent of $B$, which holds iff $\kappa(B)=\kappa(\varnothing)+\sum_{p\in B}f_p$; then $v_p=f_p+J_p[w\in p]$. Separable measures satisfy ME and BI trivially. The Corollary follows from (ii): $\tau^B_p=-F^B_p/J_p$. ∎

*Proof of Theorem 3.* $EA_C(B)=\sum_{p\in B}e_p+\beta C(\bigcap B)$. Every member of $B$ includes $\bigcap B$, so $EA_C(B)\le\Phi(\bigcap B)$, with equality iff $B$ contains every $p\supseteq\bigcap B$ with $e_p>0$ and no $p$ with $e_p<0$. Conversely, given $X$, let $B_X=\{p\supseteq X:e_p>0\}$ and $X'=\bigcap B_X\supseteq X$. The members of $B_X$ are exactly the positive-$e$ propositions including $X'$, so $EA_C(B_X)=\Phi(X')\ge\Phi(X)$, because $C(X')\ge C(X)$. Hence $\max EA=\max\Phi$, and the optimality condition follows.

For uniform values, $p\subseteq q$ implies $C(q)\ge C(p)$, which gives upward closure. For (ii): if $u\in X^*$, $v\notin X^*$ and $C(v)>C(u)$, swapping $u$ for $v$ maps the supersets of $X^*$ bijectively onto those of the new core without lowering any credence, and raises the core's credence, contradicting maximality.

For (iii): $B^*$ is upward closed with $\bigcap B^*=X^*$, so it is closed under conjunction iff $X^*\in B^*$, iff $C(X^*)>\tau$; it is consistent iff $X^*\ne\varnothing$. ∎

*Proof of Theorem 4.* Let $\pi$ send $p$ to $u$ and $W\setminus p$ to $v$. By RI the verdict on $p$ at $C$ equals the verdict on $\{u\}$ in the two-world problem at credence $c=C(p)$. There, truth-directedness excludes every state containing $\varnothing$ (dropping it raises the score at both worlds) and every state lacking $\{u,v\}$ (adding it raises the score at both), leaving $\{W\}$, $\{W,p\}$, $\{W,\bar p\}$ and $\{W,p,\bar p\}$. If $\{W,p,\bar p\}$ were optimal at $c$, dropping $\bar p$ or $p$ could not help: by CI, $(1-c)g\ge c\,l$ with $g<l$, so $c<1/2$, and $c\,g'\ge(1-c)\,l'$ with $g'<l'$, so $c>1/2$. Let $t$ and $f$ be the gain and loss from adding $p$ to $\{W\}$. Then $EA(\{W,p\})-EA(\{W\})=ct-(1-c)f$, positive iff $c>\tau_p:=f/(t+f)$, and $\tau_p>1/2$ by CI; similarly $\{W,\bar p\}$ beats $\{W\}$ only if $c<1/2$. So for $c>\tau_p$ the unique optimum is $\{W,p\}$, and for $c<\tau_p$ no optimum contains $p$. ∎

## References

Dorst, Kevin. 2019. "Lockeans Maximize Expected Accuracy." *Mind* 128 (509): 175–211. https://doi.org/10.1093/mind/fzx028

Dorst, Kevin, and Matthew Mandelkern. 2022. "Good Guesses." *Philosophy and Phenomenological Research* 105 (3): 581–618. https://doi.org/10.1111/phpr.12831. Section numbers cited follow the July 2021 penultimate author draft.

Easwaran, Kenny. 2016. "Dr. Truthlove or: How I Learned to Stop Worrying and Love Bayesian Probabilities." *Noûs* 50 (4): 816–853. https://doi.org/10.1111/nous.12099

Holguín, Ben. 2022. "Thinking, Guessing, and Believing." *Philosophers' Imprint* 22 (6): 1–25. https://doi.org/10.3998/phimp.2123

Joyce, James M. 2009. "Accuracy and Coherence: Prospects for an Alethic Epistemology of Partial Belief." In *Degrees of Belief*, edited by Franz Huber and Christoph Schmidt-Petri, 263–297. Dordrecht: Springer. https://doi.org/10.1007/978-1-4020-9198-8_11

Leitgeb, Hannes. 2014. "The Stability Theory of Belief." *Philosophical Review* 123 (2): 131–171. https://doi.org/10.1215/00318108-2400575

Leitgeb, Hannes. 2017. *The Stability of Belief: How Rational Belief Coheres with Probability*. Oxford: Oxford University Press. https://doi.org/10.1093/acprof:oso/9780198732631.001.0001

Levi, Isaac. 1967. *Gambling with Truth: An Essay on Induction and the Aims of Science*. New York: Alfred A. Knopf.

Rothschild, Daniel. 2023. "Lockean Beliefs, Dutch Books, and Scoring Systems." *Erkenntnis* 88 (5): 1979–1995. https://doi.org/10.1007/s10670-021-00438-1

Skipper, Mattias. 2023. "Good Guesses as Accuracy-Specificity Tradeoffs." *Philosophical Studies* 180 (7): 2025–2050. https://doi.org/10.1007/s11098-022-01915-1

Wang, Minkyung. 2025. "Credence and Belief: Epistemic Decision Theory Revisited." *Philosophical Studies* 182 (5–6): 1433–1465. https://doi.org/10.1007/s11098-025-02321-z

[^1]: Page references to Dorst are to the published article.

[^2]: All numerical claims were checked by exhaustive enumeration of belief states in exact rational arithmetic (all $2^8$ states on three worlds, all $2^{16}$ on four) and, on larger spaces, by maximizing $\Phi$ over cores as Theorem 3 licenses.

[^3]: The proviso is needed: there are ME measures in which the marginal value of $p$ changes when its complement is believed. It is harmless here, since such states are never optimal for separable measures under Dorst's Variable Conservativeness (his Proposition 3), nor, by Theorem 3, for the record measure.

[^4]: With $T=1$, $F=-2$ and a bonus of $1/2$ for deductively closed states, the measure satisfies ME and truth-directedness, and on three worlds $\{w_1\}$ is believed at $(0.575,0.2,0.225)$ but not at $(0.65,0,0.35)$.
