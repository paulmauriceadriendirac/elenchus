# Holistic Accuracy and the Lockean Thesis

**Abstract.** Does maximizing expected accuracy force a Lockean threshold rule for belief even when accuracy is holistic? Dorst argues that it does. I identify a gap in the derivation and give a counterexample on the unrestricted space of belief states. A score that adds a premium for having no false beliefs is strictly truth-directed and makes the rational assessment of final states independent of their order of formation. Yet, for every positive premium, it permits belief in a proposition at one credence and requires withholding it at a higher credence. The optimum combines a selected core hypothesis with a probability threshold. I also characterize a pair of sufficient repairs to the derivation: together they recover separability on states without complementary pairs. This does not establish that separability is necessary for every Lockean representation. It establishes that truth-directed accuracy and order independence alone do not settle the form of the bridge from credence to belief.

## 1. Introduction

Accuracy-first epistemology holds that rational doxastic states are those that best promote accuracy by the agent's own lights. With a separable score for outright belief, positive for true beliefs and negative for false ones, it yields a Lockean thesis: believe a proposition just in case your credence in it exceeds a threshold. The separable version of this result is due to Easwaran (2016; see Dorst 2019, §3). Dorst (2019) extended it in two directions. Letting the values of true and false belief vary with proposition and context yields variable thresholds (his Corollary 2). And, he argued, dropping Separability, the assumption that a belief state's accuracy is the sum of the accuracies of its members, changes nothing: given a further premise, Sequence-Irrelevance, Lockeanism follows anyway (his Proposition 5). The resulting claim is that the Lockean form survives a substantial relaxation of separability.[^1]

The broad robustness claim needs qualification. The counterexample below preserves unrestricted choice, truth-directed value, and order-independent assessment of final states. It nevertheless violates a fixed, proposition-specific threshold rule. Theorem 2 establishes that violation for every positive value of a premium for an error-free record. Theorem 3 characterizes the resulting optima. Theorem 1 diagnoses the derivation by identifying a pair of sufficient additional assumptions that restore a separable score. It does not prove that every successful derivation of Lockeanism must use them.

The thesis does not say that Lockeanism or separability is false. Nor does it say that holistic accuracy guarantees consistency or deductive closure: the characterization below states exactly when those properties hold. The question is what follows from the advertised minimal premises.

The closest prior work makes the novelty claim narrow. Rothschild (2023) develops additive scoring representations of Lockean belief and explicitly invites investigation of weaker additivity assumptions. Wang (2025, §§2 and 6) studies general expected-utility rules on deductively cogent belief states; his framework permits nonadditive utility and derives convexity constraints. Non-Lockean expected-utility belief is therefore already established. The present contribution sought is an unrestricted-option counterexample directed at Dorst's §4.2, together with a characterization of one holistic score. It does not obtain its result by excluding inconsistent or nonclosed states. Holguín (2022, §5) independently argues that rational thinking need not be monotone in credence. Here that behavior is obtained within an accuracy-maximizing model.

The stakes extend beyond formal epistemology. If accuracy alone settled the bridge between credence and belief, the Lockean would win that debate by default. If, as I argue, the shape of the bridge depends on how we value combinations of true beliefs, then the debate over Lockean, closed and guess-like belief becomes a debate about epistemic value, and accuracy-first epistemology is a framework for conducting it rather than a verdict.

## 2. Dorst's derivation

Let $W$ be a finite set of worlds, let propositions be subsets of $W$, and let a belief state $B$ be any set of propositions. Accuracy First leaves inconsistent, nonclosed and empty belief states among the alternatives (Dorst 2019, §3). An accuracy measure assigns a real number $A(B,w)$ to each state at each world. Given a probability function $C$ on $W$, the expected accuracy is $EA_C(B)=\sum_w C(w)A(B,w)$, and Maximize Expected Accuracy says that $B$ is rational only if no state has higher expected accuracy.

Under Separability with proposition-dependent values, $A(B,w)=\sum_{p\in B}v_p(w)$, where $v_p(w)=T_p>0$ if $w\in p$ and $v_p(w)=F_p<0$ otherwise. Then $EA_C(B)=\sum_{p\in B}e_p$, where
$$e_p = C(p)T_p+(1-C(p))F_p .$$
Every optimum includes $p$ when $e_p>0$ and excludes it when $e_p<0$; inclusion is optional at equality. The threshold is $\tau_p=-F_p/(T_p-F_p)$ (Corollary 2). Dorst also imposes Conservativeness: in the uniform case $|T|<|F|$, which makes $\tau>1/2$.

Dorst's §4.2 allows the value of a whole belief state to depend on its other beliefs. He considers adding a proposition to a background state, first when it is true and then when it is false. The argument assigns a positive true-belief increment and a negative false-belief increment, uses them to derive a threshold for the final addition in a sequence, and invokes order independence to extend the threshold to belief generally (2019, pp. 192–195, 206–207).

There are two distinct issues here. A true addition can improve a score at every world where it is true without improving it by the same amount at all those worlds. And invariance under rearranging a sequence does not by itself make the value of an addition independent of which other propositions the final state contains. Section 4 separates these claims.

I read Sequence-Irrelevance as a constraint on rational assessments: holding the other factors fixed, changing the order in which a final state was formed does not alter its rational status. A single objective over whole states satisfies that constraint. It need not make greedy, locally optimal additions lead to a globally optimal state in every order. Requiring that stronger property would constrain the optimization procedure as well as the rationality of its outcome. The counterexample addresses the former, stated order-independence principle; a defender may instead adopt the stronger requirement, but must defend it as an additional restriction on holism.

## 3. The counterexample

Define the *record measure* with premium $\beta>0$:
$$A_\beta(B,w)=\sum_{p\in B}v_p(w)+\beta\cdot[\,w\in{\textstyle\bigcap} B\,],$$
where $\bigcap\varnothing=W$ and $[\cdot]$ is 1 if the bracketed condition holds and 0 otherwise. A belief state earns the separable score of its members, plus $\beta$ at exactly those worlds where everything it contains is true. The premium is the value of an error-free record. One rationale is inferential: a belief state whose members are all true is one from which any amount of multi-premise deduction yields only truths. A body of belief can thus be valuable as a whole, which is the holist's thought. Dorst motivates separability by an exam scored question by question (2019, §3). Many exams also reward a perfect paper, and the record measure scores belief that way. The measure is purely alethic: $A_\beta(B,w)$ depends only on $B$ and on which of its members are true at $w$.

It meets the stated conditions of Dorst's §4.2 on the final-state reading just specified. Adding a true $p$ raises $A_\beta$ by exactly $T_p$: if every member of $B_0$ was true at $w$, all still are. Adding a false $p$ lowers it by $|F_p|$, or by $|F_p|+\beta$ if $B_0$ was error-free at $w$. So truth-directedness holds. Conservativeness can be imposed on the $v_p$. The measure does not depend on the current state, so Maximize Expected Accuracy has a single, sequence-independent verdict and Sequence-Irrelevance holds. Every belief state is an option, so Accuracy First holds. I make the following permission bridge explicit:

(Permission) If a belief state uniquely maximizes expected accuracy, it is rationally permitted.

This is an explicit bridge from optimization to permission. A merely necessary accuracy constraint, combined with unspecified further prohibitions, would not license that inference. The counterexample concerns an accuracy-first theory that permits its unique optimum.

*The case.* Let $W=\{w_1,w_2,w_3\}$, $T_p=1$ and $F_p=-2$ for every $p$ (so $\tau=2/3$), and $\beta=3$. Write $\mathbf{1}=\{w_1\}$. At $C=(0.70,0.15,0.15)$ the unique optimum among all $2^8$ belief states is $\{\mathbf 1,\{w_1,w_2\},\{w_1,w_3\},W\}$, with expected accuracy $4.30$ against a runner-up of $4.20$. At $C'=(0.75,0.01,0.24)$ the unique optimum is $\{\{w_1,w_3\},W\}$, with $4.94$ against $4.75$. Hand computation agrees with exhaustive enumeration in exact arithmetic.[^2] So $\mathbf 1$ is believed at credence $0.70$ and not at credence $0.75$. By Permission both optima are rational. Proposition 5 would then require $\tau_{\mathbf 1}\le 0.70$ and $\tau_{\mathbf 1}\ge 0.75$, which is impossible.

This is not a knife-edge.

**Theorem 2.** Let $T>0>F$ with $T<-F$, let $\beta>0$, let $D=T-F$ and $\tau=-F/D$, and put
$$c_0=\frac{\beta-T-2F}{2D+\beta},\qquad c_1=\frac{\beta-2F}{2D+\beta}.$$
Then $\max(c_0,\tau)<c_1<1$. For all $c<c'$ in the interval $(\max(c_0,\tau),c_1)$, $\mathbf 1$ belongs to the unique optimum at $(c,\frac{1-c}{2},\frac{1-c}{2})$ and to no optimum at $(c',\varepsilon,1-c'-\varepsilon)$, for all sufficiently small $\varepsilon\ge 0$.

The proof is in the Appendix; it was also checked by enumeration for premiums from $0.01$ to $1000$. The mechanism is visible in the case. At $C$ the residual 0.30 is spread over two worlds, and the hypothesis $\mathbf 1$ is the best "core": believing everything it entails earns three positive separable terms and a premium on 0.70. At $C'$ almost all the residual sits on $w_3$, so the disjunction $\{w_1,w_3\}$ is nearly certain. Its premium on 0.99 outweighs what the more specific hypothesis adds, so the agent hedges. As $\beta$ shrinks the interval narrows (its length above $\tau$ is $\beta T/(D(2D+\beta))$), but it never closes.

The result instantiates Holguín's Non-Monotonicity: a lower credence in a proposition can permit thinking it while a higher credence does not (2022, §5). His argument against Lockeanism used this principle. The record measure shows that accuracy-first epistemology without Separability is not bound by monotonicity either.

## 4. Diagnosis

Where does the derivation fail? There are two gaps.

*The quantifier gap.* Truth-directedness gives, for each world $w$, some positive increment. Dorst's passage on p. 193 then names one number $T^{B_0}_p$ as "the" increment. That moves from "for every $w$ there is a $t$" to "there is a $t$ for every $w$." Under the record measure the step fails. Adding the false $\mathbf 1$ to $\{\{w_1,w_3\}\}$ costs 2 at $w_2$ but 5 at $w_3$, since only at $w_3$ was the prior state error-free. In expectation, the comparison that Proposition 4 makes between $B$ and $B\setminus\{p\}$ becomes
$$EA_C(B)-EA_C(B\setminus\{p\})=e_p-\beta\,C\big({\textstyle\bigcap}(B\setminus\{p\})\setminus p\big).$$
Belief in $p$ is therefore worth adding iff $e_p$ exceeds a term fixed by the credence of the rest of the core outside $p$. That is a threshold on $C(p)$ that moves with credences in other propositions, not one fixed by values. What the step needs is:

(ME) *Marginal extensionality.* For every $B_0$ and $p\notin B_0$, $A(B_0\cup\{p\},w)-A(B_0,w)$ depends on $w$ only through whether $w\in p$.

This is not a consequence of $A$'s being well-defined. It is a substantive claim: the marginal value of a belief may depend on the world only through that belief's own truth value.

*The content gap.* Grant ME. Proposition 4 then yields thresholds $\tau^{B^-}_p$ indexed to $B^-$, the rest of the belief state. The proof of Proposition 5 generalizes from "any" $B^-$ to all rational states. That step requires $\tau^{B^-}_p$ not to vary with $B^-$. Sequence-Irrelevance cannot supply this, because $B^-$ is not a sequence; it is the content of the other beliefs, which is exactly what the holist says matters. For any fixed measure, Maximize Expected Accuracy compares whole states, and its verdicts are already sequence-independent. Dorst himself distinguishes holism from dependence on the order of consideration (2019, p. 195). That is why a principle about order cannot exclude the holism of content. A sufficient strengthening is:

(BI) *Background-independence.* $T^{B_0}_p$ and $F^{B_0}_p$ do not depend on $B_0$, for states $B_0$ not containing the complement of $p$.

Together, these two assumptions recover separability on the stated domain. BI is stronger than simply requiring the ratio that fixes a threshold to be background-independent. The theorem characterizes this sufficient repair, not every possible repair.

**Theorem 1.** Let $A$ be truth-directed. Consider only states containing no proposition together with its complement.[^3] (a) $A$ satisfies ME iff $A(B,w)=A(\varnothing,w)+\kappa(B)+\sum_{p\in B}J_p\,[w\in p]$ for some world-independent $\kappa$ and constants $J_p>0$, the sum running over the contingent $p\in B$. (b) $A$ satisfies ME and BI iff $\kappa$ is additive, that is, iff $A(B,w)=A(\varnothing,w)+\sum_{p\in B}v_p(w)$ for some proposition-dependent values $v_p$.

Since $A(\varnothing,w)$ is the same for every state, it never affects which states are optimal. Part (b) therefore says that adding ME and BI returns us to the separable measures covered by Dorst's Corollary 2. It does not classify every measure whose optima happen to be Lockean. The proof (Appendix) turns on one observation. Adding $p$ and $q$ in either order gives the same total, so $\Delta_p^{B}-\Delta_p^{B\cup\{q\}}=\Delta_q^{B}-\Delta_q^{B\cup\{p\}}$, where $\Delta_r^{B}$ is the increment of adding $r$ to $B$. Under ME the left side is affine in $[w\in p]$ and the right side affine in $[w\in q]$. Unless $q$ is $p$'s complement or trivial, both sides must be constant. A linear-algebra computation over all 256 states on three worlds confirms (a), and it confirms that the complement proviso cannot be dropped.[^4]

Part (a) shows what survives of holism under ME: a world-independent term $\kappa(B)$, a bonus or malus for a state's shape regardless of how the world is. A nonadditive $\kappa$ can make Proposition 5 fail. For example, a small bonus for deductively closed states, small enough to preserve truth-directedness, shifts the effective threshold of $p$ according to whether adding $p$ completes or breaks closure.[^8] Dorst can reject such a $\kappa$ as non-alethic. Rejecting such terms would require a further account of which forms of holistic value qualify as accuracy.

Theorem 1 concerns the derivation, not its conclusion. Some non-separable measures do have Lockean optima. A separable measure lowered on states that are never optimal is an example. So Separability is not necessary for Lockean outputs. What the combined results show is narrower: the proposed inference is not secured by well-definedness and order independence alone. The record measure supplies a truth-directed counterexample, while ME plus BI supplies one transparent repair.

## 5. What holism delivers instead

The record measure does not leave belief unstructured. Its optima have an exact description. Write $\bigcap B$ for the *core* of $B$, and for each proposition $X$ let
$$\Phi(X)=\sum_{p\supseteq X}\max(e_p,0)+\beta\,C(X).$$

**Theorem 3.** For any finite $W$ and any proposition-dependent values, $\max_B EA_C(B)=\max_X\Phi(X)$. A state $B$ is optimal iff its core maximizes $\Phi$, $B$ contains every $p\supseteq\bigcap B$ with $e_p>0$, and $B$ contains no $p$ with $e_p<0$. In particular, when the values are uniform and $C$ is generic, the unique optimum is
$$B^*=\{p\supseteq X^*: C(p)>\tau\},$$
where $X^*$ maximizes $\Phi$, and:
(i) $B^*$ is consistent iff $X^*\neq\varnothing$, and it is closed under single-premise entailment;
(ii) $X^*$ contains every world more probable than any world it contains;
(iii) $B^*$ is deductively closed iff $C(X^*)>\tau$, in which case it consists of exactly the consequences of $X^*$.

Call this *core-relative Lockeanism*. The agent selects a working hypothesis $X^*$, trading its probability (the premium term) against the number of above-threshold propositions it entails. She then believes those above-threshold propositions that the hypothesis entails. Lockean belief is the special case in which the best core is the intersection of all above-threshold propositions. By (ii) the working hypothesis is always a set of most probable worlds, which is the filtering structure guess-based theories posit for answers (Holguín 2022, §10). By (iii) closure is not guaranteed. On four worlds with $C=(0.62,0.18,0.10,0.10)$ and the values of §3, the unique optimum believes $\{w_1,w_2\}$ and $\{w_1,w_3\}$ but not $\{w_1\}$. The theorem was checked against exhaustive enumeration on three and four worlds, with uniform and with randomly varying values.[^5]

Three consequences matter for the debate.

First, accuracy-first epistemology is neutral between Lockean and guess-like belief. Separable value gives thresholds. Record value gives a best hypothesis and its probable consequences. Accuracy does not choose between them; a view about the value of an error-free body of belief does.

Second, the record measure captures both forms of non-monotonicity in the literature. In §3 the agent hedges when a disjunction becomes nearly certain. In Holguín's horse race, belief in A is lost when a rival overtakes it: told that A, B and C have chances 0.40, 0.35 and 0.25, one may think A wins; told 0.45, 0.50 and 0.05, one should think B wins and not A (2022, §5). A single context reproduces both verdicts. Let values depend only on how many horses a proposition mentions: $(T,F)=(1,-0.66)$ for one horse and $(0.65,-1.01)$ for two, which satisfies Dorst's Variable Conservativeness, and set $\beta=0.19$. The unique optimum at the first credences is the set of consequences of "A wins". At the second it is the set of consequences of "B wins". The runner-up there is the inconsistent state that believes both A and B, which is exactly what a Lockean with these thresholds (about 0.40 for one horse) would believe.[^7] So the premium does what Holguín says sophisticated Lockeanism cannot: it keeps thresholds low enough for extreme weakness while ruling out the incompatible beliefs those thresholds would license. The margins are small, though, and a random search suggests that values doing this occupy a narrow band. The result shows that non-monotonicity is available to accuracy-firsters. It does not show that the record measure is the right theory of thinking.

Third, Dorst's reduction of belief to credence (§5.1) survives in a weakened form. Under the record measure, belief can still be "read off" credence and contextual values, since $B^*$ is a function of both. What fails is the Lockean form of the function. The reduction is thus independent of Lockeanism. A Lockean needs some further restriction on the admissible scores or rational states. Separability is one sufficient restriction; it is not shown here to be necessary.

## 6. Objections

*The premium is not accuracy; it double-counts the conjunction.* The premium is alethic, since it depends only on which believed propositions are true. It is not a disguised belief in the core: in the four-world case it accrues on $\{w_1\}$, which is not believed. And it respects strict truth-directedness, the only constraint Dorst places on holistic measures. The objector may insist that genuine accuracy is local, so that a belief's contribution depends only on its own truth. That insistence is ME. Coupled with BI it yields separability, but ME alone leaves the additional term identified in Theorem 1(a). To exclude the premium on those grounds is to deny the holism that §4.2 set out to accommodate. The reply leaves one thing open: someone may find the premium unmotivated as a value. Then the dispute is about the value of an error-free record. That is my thesis.

*Dorst meant only belief-dependence: values that vary with what else is believed, not with whether it is true.* The text resists this reading by claiming that well-definedness alone supports the step (2019, p. 193). Grant the reading anyway. ME then becomes an explicit premise, and the content gap remains. Under ME, Theorem 1(a) leaves a world-independent $\kappa$. Nonadditive choices of $\kappa$ can defeat a fixed threshold; additive ones recover separability. This alternative reading narrows the admissible holism but does not, without further argument, establish the advertised conclusion.

*Sequence-Irrelevance should be read strongly, as requiring background-independent thresholds.* This is a substantive alternative reading, but it goes beyond invariance under reordering an exam. Background-independent thresholds need not be identified with background-independent marginal values. Theorem 1 concerns the latter, stronger condition. A defender who imposes threshold independence directly owes an argument for why an accuracy holist must accept it; appealing only to order independence leaves the issue unsettled.

*Maximize Expected Accuracy gives only a necessary condition; perhaps neither optimum is rational.* Then rationality would be unsatisfiable at $C$ and $C'$. Accuracy First would then have yielded a norm that no state can meet, which no accuracy-firster accepts. Permission is the minimal premise needed for the framework to issue verdicts at all.

*The premium is representation-dependent.* The value of a record may change when the proposition space is refined: the additive part counts more propositions, while the premium is paid once. This is a serious objection to treating the measure as a complete account of epistemic value. The counterexample fixes a finite proposition space, the same unrestricted space used in the target derivation, and compares two credences on it without changing the questions or their values. Its nonmonotonicity therefore does not arise from switching representations between the two cases. But nothing proved here establishes invariance across different descriptions of the same inquiry. A positive theory based on record value would need to say which questions count and how their weights survive refinement. The limited negative result does not depend on having solved that further problem: the proposed derivation must either exclude the score by a stated premise or accommodate its verdicts. Calling that exclusion a representation-invariance requirement would make the substantive restriction visible.

*The result is negative only; Dorst's picture survives.* In part, yes. Belief remains a function of credence and contextual values, and Dorst's "best guess" gloss fits core-relative Lockeanism at least as well as Lockeanism. What does not survive is the claim that accuracy forces the Lockean form. That matters to Holguín's argument, which targets the Lockean form. Non-monotonicity tells against sophisticated Lockeanism, but not against accuracy-first epistemology as such.

## 7. Conclusion

The record measure gives a precise obstruction to the claimed inevitability of Lockean belief. It evaluates every belief state, rewards true additions, penalizes false additions, and judges final states without regard to formation order. With the explicit permission bridge, it nevertheless licenses a nonmonotone relationship between credence and belief for every positive premium. Its optimum has an exact core-and-threshold description; consistency and closure require the additional conditions stated in Theorem 3.

The diagnosis is deliberately limited. ME plus BI restores separability on the specified domain, but separability has not been proved necessary for every Lockean output. Nor has the record premium been established as the uniquely correct measure of accuracy. What changes is the burden of argument: a defence of Lockeanism must justify a restriction that excludes this kind of holistic value, rather than taking order-independent accuracy maximization to have excluded it already.

## Appendix: Proofs and checks

*Proof of Theorem 1.* Write $\Delta_p^B(w)=A(B\cup\{p\},w)-A(B,w)$ for $p\notin B$. Under ME, $\Delta_p^B=F_p^B+J_p^B[w\in p]$ for contingent $p$, and $\Delta_p^B$ is constant for $p\in\{\varnothing,W\}$; truth-directedness gives $F_p^B<0<F_p^B+J_p^B$. (i) Let $p,q\notin B$ be distinct, with $q$ not the complement of $p$. Computing $A(B\cup\{p,q\},\cdot)-A(B,\cdot)$ in both orders gives $\Delta_p^B-\Delta_p^{B\cup\{q\}}=\Delta_q^B-\Delta_q^{B\cup\{p\}}$. The left side is $\alpha+(J_p^B-J_p^{B\cup\{q\}})[w\in p]$ and the right side is $\gamma+\delta[w\in q]$, or a constant if $q$ is trivial. If $p,q$ are contingent, distinct and not complementary, then $1,[w\in p],[w\in q]$ are linearly independent, so $J_p^{B\cup\{q\}}=J_p^B$. If $q$ is trivial, the same conclusion follows. (ii) Building any $B$ that contains neither $p$ nor its complement from $\varnothing$ one member at a time, (i) gives $J_p^B=J_p^\varnothing=:J_p$. (iii) For $B$ without complementary pairs, add its members in any order. Each increment is $F^{B_i}_{p}+J_p[w\in p]$, so $A(B,w)-A(\varnothing,w)=\kappa(B)+\sum_{p\in B}J_p[w\in p]$, where $\kappa(B)$ is the sum of the $F$-terms (and the constant increments). It is world-independent, and it is order-independent because the total is. The converse of (a) is immediate. For (b), BI says $F^{B}_p=\kappa(B\cup\{p\})-\kappa(B)$ is independent of $B$, which holds iff $\kappa(B)=\kappa(\varnothing)+\sum_{p\in B}f_p$; then $v_p=f_p+J_p[w\in p]$. Conversely, separable measures satisfy ME and BI trivially. ∎

*Proof of Theorem 3.* $EA_C(B)=\sum_{p\in B}e_p+\beta C(\bigcap B)$. Every member of $B$ includes $\bigcap B$, so $EA_C(B)\le\Phi(\bigcap B)$, with equality iff $B$ contains every $p\supseteq\bigcap B$ with $e_p>0$ and no $p$ with $e_p<0$. Conversely, given $X$, let $B_X=\{p\supseteq X:e_p>0\}$ and $X'=\bigcap B_X\supseteq X$. The members of $B_X$ are exactly the positive-$e$ propositions including $X'$, so $EA_C(B_X)=\Phi(X')\ge\Phi(X)$, because $C(X')\ge C(X)$. Hence $\max EA=\max\Phi$, and the optimality condition follows. For uniform values, upward closure holds because $p\subseteq q$ implies $C(q)\ge C(p)$. For (ii): if $u\in X^*$, $v\notin X^*$ and $C(v)>C(u)$, swapping $u$ for $v$ maps the supersets of $X^*$ bijectively onto those of the new core without lowering any credence, and it raises $C(X^*)$; that contradicts maximality. For (iii): $B^*$ is upward closed with $\bigcap B^*=X^*$, so it is closed under conjunction iff $X^*\in B^*$, iff $C(X^*)>\tau$. Consistency holds iff $\bigcap B^*\ne\varnothing$. ∎

*Proof of Theorem 2.* Write $e_p=C(p)D+F$; note $\tau>1/2$. At $C_c=(c,\frac{1-c}{2},\frac{1-c}{2})$ with $c>\tau$, the positive terms are $e_{\mathbf 1}$, $e_{12}=e_{13}$ and $e_W=T$, and all others are negative (their credences are at most $1-c<1/2$). Then $\Phi(\mathbf 1)-\Phi(W)=e_{\mathbf 1}+2e_{12}-\beta(1-c)=c(2D+\beta)+T+2F-\beta$, which is positive iff $c>c_0$. Also $\Phi(\mathbf 1)-\Phi(\{w_1,w_3\})=e_{\mathbf 1}+e_{12}-\beta\frac{1-c}{2}>\frac12(\Phi(\mathbf 1)-\Phi(W))$, which is positive. Next, $\Phi(\mathbf 1)-\Phi(\{w_2\})=e_{\mathbf 1}+e_{12}+\beta\frac{3c-1}{2}>0$ and $\Phi(\mathbf 1)-\Phi(\{w_2,w_3\})=e_{\mathbf 1}+2e_{12}+\beta(2c-1)>0$; the cases of $\{w_1,w_2\}$ and $\{w_3\}$ are symmetric; and $\Phi(\mathbf 1)-\Phi(\varnothing)=\beta c>0$. By Theorem 3 the unique optimum has core $\mathbf 1$ and contains $\mathbf 1$. At $C'=(c',0,1-c')$ with $\tau<c'$: $e_{\mathbf 1}=e_{12}=c'D+F>0$ and $e_{13}=e_W=T$, so $\Phi(\{w_1,w_3\})-\Phi(\mathbf 1)=\beta(1-c')-2e_{\mathbf 1}$, which is positive iff $c'<c_1$, while $\Phi(\varnothing)=\Phi(\mathbf 1)-\beta c'$. A state containing $\mathbf 1$ has core $\mathbf 1$ or $\varnothing$, so no optimum contains $\mathbf 1$. These strict inequalities persist for small $\varepsilon$. Finally, $c_1-c_0=T/(2D+\beta)$, $c_1-\tau=\beta T/(D(2D+\beta))$ and $1-c_1=2T/(2D+\beta)$ are all positive. ∎

## References

Dorst, Kevin. 2019. "Lockeans Maximize Expected Accuracy." *Mind* 128 (509): 175–211. https://doi.org/10.1093/mind/fzx028

Easwaran, Kenny. 2016. "Dr. Truthlove or: How I Learned to Stop Worrying and Love Bayesian Probabilities." *Noûs* 50 (4): 816–853. https://doi.org/10.1111/nous.12099

Holguín, Ben. 2022. "Thinking, Guessing, and Believing." *Philosophers' Imprint* 22 (1). https://doi.org/10.3998/phimp.2123

Rothschild, Daniel. 2023. "Lockean Beliefs, Dutch Books, and Scoring Systems." *Erkenntnis* 88 (5): 1979–1995 (online 2021). https://doi.org/10.1007/s10670-021-00438-1

Wang, Minkyung. 2025. "Credence and Belief: Epistemic Decision Theory Revisited." *Philosophical Studies* 182 (5–6): 1433–1465. https://doi.org/10.1007/s11098-025-02321-z

[^1]: The published text of Dorst (2019), especially pp. 192–195 and 206–207, was checked for this revision. Earlier draft page references used the accepted manuscript.

[^2]: All 256 states over the eight propositions of a three-world space (including $\varnothing$ and $W$) were enumerated with rational arithmetic. A scan of credences on a grid of mesh $1/40$ found monotonicity violations for all six contingent propositions.

[^3]: The proviso is needed, since there are ME measures in which the marginal value of $p$ changes when its complement is believed. It is harmless here. Under Variable Conservativeness $\tau_p+\tau_{\neg p}>1$, so such states are never optimal for separable measures (Dorst's Proposition 3), nor, by Theorem 3 below, for the record measure.

[^4]: The ME constraints form a homogeneous linear system on the $768$ values $A(B,w)$. Each vector of a basis of its solution space was tested against the representation in (a), with numerical deviation below $10^{-14}$.

[^5]: In the revision rerun, 887 random instances with integer credences gave identical predicted and computed optimal sets (799 on three worlds and 88 on four). These finite checks supplement the proof.

[^7]: Exhaustive enumeration over all 256 belief states, in exact arithmetic, with $T_W=1$ (the value of believing $W$ does not affect which states are optimal) and $\beta=19/100$. Expected accuracies: $1.384$ against $1.380$ at the first credences, and $1.832$ against $1.824$ at the second.

[^8]: With $T=1$, $F=-2$ and a bonus of $1/2$ for closed states, the measure satisfies ME and truth-directedness. On three worlds, $\{w_1\}$ is believed at $(0.575,0.2,0.225)$ but not at $(0.65,0,0.35)$.


