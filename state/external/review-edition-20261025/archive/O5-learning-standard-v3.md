# How Regret Selects a Learning Standard

**Abstract.** Can worst-case accuracy replace the choice of weights in a total-accuracy justification of conditionalization? In a binary factive-reporting problem, worst expected loss preserves the prior on the tautological report but does not uniquely select conditionalization among unrestricted rules. Worst regret instead selects a score-dependent compromise. I characterize it for strictly proper losses and prove a directional classification for a symmetric family: regret shrinks confidence, preserves it, or extremizes it according to the loss's tail parameter. The boundary is the known boosting loss. A separate calculation shows that applying the quadratic-regret forecast to a bet can disagree with directly minimizing the bet's regret; no fixed posterior implements the optimal randomized policies for every bet price. These results do not disprove conditionalization or regret-based learning. They show exactly which additional evaluative choices two proposed robustness criteria leave in place. The remaining question is whether a mechanism-informed comparator has epistemic authority when the updating rule itself must ignore the mechanism's identity.

## 1. Can robustness supply the standard?

A learner gives $a$ probability $0.8$. She receives a true proposition from a process whose selection rule is unspecified. If that proposition is the whole space, ex-ante minimax regret under quadratic loss recommends $2/3$. Under logarithmic loss it recommends approximately $0.7245$. Under a different symmetric strictly proper loss it recommends approximately $0.8825$. The same kind of performance criterion can lower or raise confidence in the more probable state.

This matters to a specific choice in accuracy-first epistemology. Meehan and Zhang (2025, Fact 11) show that total expected accuracy selects conditionalization exactly under extensional weights over learning situations. One might try to avoid selecting those weights by judging a rule against its worst case. I examine two such criteria. Worst expected loss leaves a dogmatic rule optimal. Worst regret selects a different rule whose response depends on the score. Thus these two criteria do not supply a uniquely determined, score-independent substitute for the weighted standard. This is a test of a possible alternative to their argument, not a claim that they propose it.

The mathematical setting is factive coarsening: the signal is always a set containing the true state. The binary case has only four deterministic mechanisms, making the role of the oracle comparator explicit. The main additional result is a classification within a family of symmetric proper losses: greater emphasis near certainty can reverse the direction in which the regret rule moves the prior. A calculation for ordinary bets then distinguishes a forecast optimized for one score from a posterior that would implement every task's regret-optimal action.

The general decision-theoretic machinery is established. Che, Li, and Luo (2026) formulate ex-ante oracle regret for general-purpose learning, permit proper-score evaluation through Bregman divergences, and represent the optimal rule through Nature's worst-case mixture. They also justify scores by aggregating decision tasks. Their model concerns signals of uncertain quality; this essay concerns the four factive binary reporting mechanisms. Van Ommen and colleagues (2016) study minimax expected-loss updating with unknown coarsening. Neither the robust-Bayes representation nor score-dependence alone is the proposed contribution. The contribution sought is the explicit classification and its implications for the choice of a learning standard in this game.

## 2. The decision problem

Let $S=\{a,b\}$, with prior $\pi(a)=p\in(0,1)$. A deterministic reporting mechanism $E$ assigns to each state a proposition containing that state. There are exactly four:

| Mechanism | Report at $a$ | Report at $b$ |
|---|---|---|
| $R$, full revelation | $\{a\}$ | $\{b\}$ |
| $N$, no disclosure | $S$ | $S$ |
| $E_a$, selective silence at $a$ | $S$ | $\{b\}$ |
| $E_b$, selective silence at $b$ | $\{a\}$ | $S$ |

An updating rule maps a received proposition to a probability forecast. Whether the optimal forecast deserves interpretation as the learner’s belief is the philosophical question, not part of this definition. It must use the same posterior for the same proposition across mechanisms. This is global evidential constancy in Meehan and Zhang’s terminology (2025, pp. 315–316, Fact 5). The rule knows the initial prior but is not given the mechanism's identity as a separate input.

We consider evidence-respecting rules: receiving $\{a\}$ produces certainty in $a$, and receiving $\{b\}$ produces certainty in $b$. The only choice is then

$$q=f(S)(a).$$

This restriction does not raise the minimum attainable loss or regret in the problem. Since reports are true, replacing an uncertain response to a singleton with certainty weakly reduces expected quadratic loss under every mechanism. It also weakly reduces regret, whose comparator is fixed independently of the learner's chosen rule. Uniqueness statements below concern the evidence-respecting class.

Use the sum of squared errors on the two state propositions:

$$\ell(q,a)=2(1-q)^2,\qquad\ell(q,b)=2q^2.$$

The factor two records both coordinates of the probability vector. It affects the numerical losses but not the optimal choice. Write $L_E(q)$ for the rule's expected loss under mechanism $E$, averaging states with the fixed prior $p$.

For each $E$, let

$$m_E=\min_r L_E(r),\qquad
\operatorname{Reg}_E(q)=L_E(q)-m_E.$$

The comparator may be chosen separately for each mechanism. For a deterministic learning situation it conditions on the preimage of the received report under $E$. This is the performance achieved by meta-conditionalization, or by a situation-specific content-based rule reproducing it (Meehan and Zhang 2025, Facts 2 and 8). It is the best report-based rule a designer could select knowing that mechanism. It does not receive the actual state as an extra input. Under $N$, no report-based rule can identify the state. Under either selective-silence mechanism, by contrast, the two different reports identify it exactly.

This gives the following losses and regrets:

| Mechanism | Expected loss $L_E(q)$ | Regret $\operatorname{Reg}_E(q)$ |
|---|---|---|
| $R$ | $0$ | $0$ |
| $N$ | $2p(1-p)+2(q-p)^2$ | $2(q-p)^2$ |
| $E_a$ | $2p(1-q)^2$ | $2p(1-q)^2$ |
| $E_b$ | $2(1-p)q^2$ | $2(1-p)q^2$ |

The first three nontrivial entries follow by averaging statewise quadratic losses. For $N$, completing the square separates unavoidable uncertainty, $2p(1-p)$, from the cost of departing from $p$. That separation is the source of the result.

## 3. The exact regret optimum

**Proposition 1.** Among evidence-respecting rules, the unique minimizer of worst-case regret over the four mechanisms is

$$q^*=\frac{\sqrt p}{\sqrt p+\sqrt{1-p}},\qquad\text{(1)}$$

with worst-case regret

$$V(p)=\frac{2p(1-p)}{(\sqrt p+\sqrt{1-p})^2}.\qquad\text{(2)}$$

*Proof.* The regret under $E_a$ strictly decreases as $q$ moves from zero to one, while the regret under $E_b$ strictly increases. The maximum of these two regrets is uniquely minimized where they are equal:

$$p(1-q)^2=(1-p)q^2.$$

Taking nonnegative square roots gives (1), and substituting gives (2). It remains to show that $N$ does not produce larger regret there. Let $u=\sqrt p$ and $v=\sqrt{1-p}$. Then

$$q^*-p=\frac{uv(v-u)}{u+v},$$

so

$$2(q^*-p)^2
=\frac{2p(1-p)(u-v)^2}{(u+v)^2}
\le V(p),$$

because $(u-v)^2\le u^2+v^2=1$. Thus $N$ does not alter the optimum. Any other $q$ has a strictly larger maximum over the two selective-silence mechanisms, proving uniqueness. ∎

The transformation preserves which state is more probable but reduces the odds:

$$\frac{q^*}{1-q^*}=\sqrt{\frac p{1-p}}.$$

It therefore moves every nonuniform prior strictly toward one half. It agrees with the prior only at $p=1/2$. This is not a consequence of uncertainty about the prior: $p$ is fixed throughout the optimization.

For $p=4/5$, the optimum is $q^*=2/3$. Its maximum regret is $8/45$, about $0.1778$. Keeping $q=p=4/5$ instead has maximum regret $32/125=0.256$, incurred when the source uses $E_b$. The robust regret rule accepts a cost when the source is truly uninformative: under $N$, its regret is $8/225$, about $0.0356$. It accepts that cost to reduce its much greater missed opportunity when a source's silence reveals the less probable state.

The movement toward one half thus has a precise explanation. Overconfidence in the more probable state is cheap under $N$ only because that mechanism leaves unavoidable uncertainty. Under $E_b$, the same confidence is a serious avoidable error: receiving $S$ would identify $b$ to a learner who knew the protocol. The regret criterion compares the learner to that better-informed designer.

## 4. The worst-error optimum

**Proposition 2.** Among evidence-respecting rules, the unique minimizer of worst-case expected quadratic loss is $q=p$.

*Proof.* Whatever $q$ is chosen, the no-disclosure mechanism gives

$$L_N(q)=2p(1-p)+2(q-p)^2\ge2p(1-p),$$

with equality only at $q=p$. At that choice,

$$L_{E_a}(p)=2p(1-p)^2\le2p(1-p),$$

$$L_{E_b}(p)=2(1-p)p^2\le2p(1-p),$$

and $L_R(p)=0$. Hence $q=p$ attains the lower bound supplied by $N$, uniquely. ∎

The two criteria use the same prior, admissible rules, report space, and possible mechanisms. Neither assigns a probability distribution over mechanisms. Their disagreement comes entirely from the comparator. The worst-error criterion is dominated by the possibility that no information will be disclosed. The regret criterion discounts the error unavoidable under that possibility and gives greater relative importance to situations where a good rule could have learned more.

If evidence-respectingness is dropped, minimizing worst-case error need not uniquely prescribe conditionalization. For example, the rule that always retains the prior, even after a singleton report, achieves expected loss $2p(1-p)$ under every mechanism. Proposition 2 therefore does not supply an unrestricted uniqueness argument for Bayes. It isolates what the criterion requires on the tautological report within the evidence-respecting class.

## 5. The result survives randomized reporting

Perhaps the result is an artifact of considering only deterministic sources. A realistic source might randomize its choice of true report. But the same optimum survives all such randomization.

A stochastic factive mechanism is specified by two numbers:

$$\alpha=K(S\mid a),\qquad\beta=K(S\mid b),$$

each in $[0,1]$. The remaining probabilities go to the appropriate singleton. Its expected loss is

$$L_{\alpha,\beta}(q)
=2p\alpha(1-q)^2+2(1-p)\beta q^2.$$

For each fixed rule, this is affine in $(\alpha,\beta)$. The square $[0,1]^2$ has the four deterministic mechanisms as its vertices.

**Proposition 3.** Allowing every stochastic factive mechanism changes neither the minimax-regret optimum in Proposition 1 nor the minimax-loss optimum in Proposition 2.

*Proof.* For a fixed $q$, expected loss is affine in the mechanism, so its maximum over the square occurs at a vertex. Regret can be written

$$\operatorname{Reg}_K(q)
=\sup_r\left[L_K(q)-L_K(r)\right].$$

It is therefore a supremum of affine functions of $K$, hence convex in $K$. Express any stochastic mechanism as a convex combination of the four vertices. Convexity bounds its regret by the same combination of vertex regrets, and therefore by their maximum. Since the vertices are themselves allowed, the worst-case regret is exactly the worst vertex regret. The two optimization problems consequently reduce to those already solved. ∎

The comparator in this proof knows the stochastic kernel, including its randomization probabilities. It is not allowed to see an unobserved random seed. There is thus no hidden strengthening to a clairvoyant comparator when randomized mechanisms are admitted.

## 6. The score determines the compromise

Now replace quadratic loss by a binary strictly proper loss with components $l_a(q)$ and $l_b(q)$. Assume that they are nonnegative, continuous on the open interval, and have zero limits at the correct certainty: $l_a(1)=l_b(0)=0$. Assume that $l_a$ strictly decreases and $l_b$ strictly increases. Wrong-certainty losses may be infinite. Strict propriety means that, for every $p\in(0,1)$, the expected loss $p l_a(q)+(1-p)l_b(q)$ is uniquely minimized at $q=p$.

The normalization removes state-specific constants. Those constants change every rule's expected loss by the same prior-weighted amount, independently of the mechanism, and cancel from regret. A common positive scaling changes neither optimum. These harmless changes must be distinguished from changing the shape of the loss, which can change the answer.

Set

$$A(q)=p l_a(q),\quad B(q)=(1-p)l_b(q),\quad
H(p)=p l_a(p)+(1-p)l_b(p).$$

The regrets at the four deterministic mechanisms are respectively

$$0,\qquad A(q)+B(q)-H(p),\qquad A(q),\qquad B(q).$$

Here $H(p)$ is the best achievable loss under no disclosure. The selective mechanisms still permit zero oracle loss because their reports identify the state. The earlier convexity argument in the *mechanism* remains available; it does not require convexity of the loss in the announced probability.

**Proposition 4.** Under these assumptions, the unique ex-ante minimax-regret response is the equalizer $q_L$ satisfying

$$p l_a(q_L)=(1-p)l_b(q_L).\qquad\text{(3)}$$

The unique minimax-loss response within the evidence-respecting class remains $q=p$.

*Proof.* $A$ decreases strictly and $B$ increases strictly, with $A(0+)>0=B(0+)$ and $A(1-)=0<B(1-)$, allowing infinite wrong-certainty limits. Their unique crossing minimizes $\max\{A,B\}$. Write their common value there as $M$. Since this is the minimum of that maximum, $M\leq\max\{A(p),B(p)\}\leq H(p)$. Thus the regret under no disclosure is $2M-H(p)\leq M$, so it does not change the minimizer. The extension to all randomized mechanisms follows as before. For raw expected loss, no disclosure supplies the lower bound $H(p)$, attained only at $q=p$ by strict propriety. At $p$, the selective losses are nonnegative summands of $H(p)$ and cannot exceed it. ∎

For logarithmic loss, $l_a(q)=-\log q$ and $l_b(q)=-\log(1-q)$. At $p=4/5$, equation (3) becomes $q^4=1-q$, whose unique interior solution is approximately $0.72449$. This differs from both the quadratic answer $2/3$ and the unchanged prior $4/5$. The disagreement is not a failure of propriety: each loss remains strictly proper. They penalize the same missed opportunities differently.

Call the condition $f(S)=\pi$ **content preservation**. This is a definition for the present essay, not an attribution of a named principle. It captures what conditioning on tautological content requires. It is weaker than a general commitment to conditionalization and should not be confused with preserving one's prior after an observation known to be uninformative. The latter includes knowledge of the reporting process; the former concerns a rule's response to a proposition across processes.

The quadratic calculation might suggest that regret inevitably violates content preservation. That suggestion is false. The next result identifies the precise exception within a differentiable subclass.

**Proposition 5.** Suppose, in addition, that the loss components are continuously differentiable on $(0,1)$. Ex-ante minimax regret satisfies content preservation for every regular binary prior if and only if, for some $C>0$,

$$l_a(q)=C\sqrt{\frac{1-q}{q}},\qquad
l_b(q)=C\sqrt{\frac{q}{1-q}}.\qquad\text{(4)}$$

Consequently no bounded loss satisfying these assumptions preserves the prior for every $p$.

*Proof.* By Proposition 4, preservation for every prior requires

$$q l_a(q)=(1-q)l_b(q)$$

throughout the open interval. Hence write $l_a(q)=(1-q)h(q)$ and $l_b(q)=q h(q)$ with positive differentiable $h$. Strict propriety implies the first-order condition

$$q l_a'(q)+(1-q)l_b'(q)=0.$$

Substitution gives $(1-2q)h(q)+2q(1-q)h'(q)=0$. Solving this differential equation yields $h(q)=C/\sqrt{q(1-q)}$, giving (4). Conversely, with $t=\sqrt{q/(1-q)}$, expected loss divided by $C$ is $p/t+(1-p)t$. It has its unique minimum at $t=\sqrt{p/(1-p)}$, equivalently $q=p$, so the loss is strictly proper. Its prior-weighted components agree at $p$, and Proposition 4 establishes preservation. Both wrong-certainty losses diverge, proving the boundedness consequence. ∎

The components in (4) are the known boosting loss on the probability scale, discussed by Buja, Stuetzle, and Shen (2005). I claim neither the score nor its propriety as new. The proposed increment is its characterization by content preservation in this minimax-regret reporting problem. The assumptions matter: the theorem does not classify nondifferentiable losses, nonproper objectives, or constraints on reporting mechanisms.

Preserving every prior is a cross-prior property. At a particular prior, many scores may preserve it; every symmetric loss does so at $p=1/2$. Nor is specificity an objection to boosting loss. Its role becomes clearer when it is placed inside a family that moves confidence in both directions.

For $\alpha>-1$, define

$$w_\alpha(t)=[t(1-t)]^{\alpha-1},\qquad
l_a(q)=\int_q^1(1-t)w_\alpha(t)\,dt,\quad
l_b(q)=\int_0^q t w_\alpha(t)\,dt.$$

Both losses are finite at interior forecasts and vanish at the correct certainty. Their derivatives are $l_a'(q)=-(1-q)w_\alpha(q)$ and $l_b'(q)=qw_\alpha(q)$. Expected loss at truth probability $p$ consequently has derivative $(q-p)w_\alpha(q)$, proving strict propriety. The losses exchange under $q\mapsto1-q$. This is the familiar weight-function construction of binary proper losses (Buja, Stuetzle, and Shen 2005), here applied to the regret equalizer.

**Proposition 6.** For $p>1/2$, the minimax-regret response satisfies

$$\begin{cases}
1/2<q_L<p,&\alpha>-1/2,\\
q_L=p,&\alpha=-1/2,\\
p<q_L<1,&-1<\alpha<-1/2.
\end{cases}$$

For $p<1/2$, the inequalities reverse by symmetry. At $p=1/2$, every member gives $q_L=1/2$.

*Proof.* Put $D(p)=p l_a(p)-(1-p)l_b(p)$. Symmetry gives $D(1/2)=0$. The correct-certainty integrals tend to zero, and $(1-p)l_b(p)\to0$ for $\alpha>-1$, so $D(1-)=0$. Differentiation gives

$$D'(p)=l_a(p)+l_b(p)-2p(1-p)w_\alpha(p),$$
$$D''(p)=(2\alpha+1)(2p-1)w_\alpha(p).$$

On $(1/2,1)$, $D$ is therefore strictly convex when $\alpha>-1/2$, zero when $\alpha=-1/2$, and strictly concave when $\alpha<-1/2$. Its endpoint values make its sign respectively negative, zero, and positive. For fixed $p$, the equalizer difference $p l_a(q)-(1-p)l_b(q)$ is strictly decreasing in $q$ and positive at $q=1/2$. Its sign at $q=p$ is $D(p)$, giving the three conclusions. The remaining cases follow by symmetry. ∎

For $p=0.8$, the numerical equalizers are:

| Loss, up to positive scale | $\alpha$ | $q_L$ |
|---|---:|---:|
| Bounded polynomial loss | $2$ | $0.639945$ |
| Quadratic loss | $1$ | $0.666667$ |
| Logarithmic loss | $0$ | $0.724492$ |
| Boosting loss | $-1/2$ | $0.800000$ |
| Heavier-tail loss | $-3/4$ | $0.882477$ |

The numerical values illustrate the proved directions; they do not prove monotonicity in $\alpha$, which is not claimed here. Proposition 6 classifies this family, not every proper score. For $\alpha=2$, the partial losses are bounded polynomials; for $\alpha=1$, they are positive multiples of the quadratic loss. Both shrink the prior by different amounts. Unboundedness alone does not explain extremizing: logarithmic loss is unbounded and still shrinks. Boosting marks the directional boundary within this family.

The philosophical consequence is precise. Symmetry and strict propriety do not even fix the direction of the response to the whole-space report. An argument that regret supplies a canonical epistemic compromise must defend more structure than those requirements. It can defend a particular score or a distribution of tasks. It cannot infer that commitment from propriety alone.

## 7. Least-favorable weights are weights

Robustness does not evade the weighting question in accuracy-first epistemology. Under quadratic loss, the optimal rule has an explicit least-favorable mixture over the two selective mechanisms. Write $u=\sqrt p$, $v=\sqrt{1-p}$, and give $E_a$ weight $v/(u+v)$ and $E_b$ weight $u/(u+v)$. Give the other two mechanisms weight zero.

The mixture's expected regret is

$$2\frac{v}{u+v}p(1-q)^2+
2\frac{u}{u+v}(1-p)q^2.$$

Its unique minimizer is $q=u/(u+v)$. At that value the two component regrets are equal, so the mixture attains the worst-case value. This proves the saddle-point claim directly. There is no need to infer a probability over mechanisms from the learner's evidence.

The mixture induces a reporting kernel with

$$K^*(S\mid a)=\frac{v}{u+v},\qquad
K^*(S\mid b)=\frac{u}{u+v}.$$

Ordinary Bayesian conditioning on receiving $S$ under this kernel gives

$$\frac{p v}{p v+(1-p)u}=\frac{u}{u+v}=q^*.$$

For $p=0.8$, its two likelihoods are $1/3$ and $2/3$. The square-root answer is thus exactly Bayesian for a specified observation model. Calling it non-Bayesian without identifying the evidence on which conditioning occurs would obscure the issue.

It is also an instance of the weighted-total characterization in Meehan and Zhang (2025, Fact 11 and Lemma 1). A weighting $\lambda$ over situations induces $\lambda_P(s)=\sum_{E:E(s)=P}\lambda(E)$. Proper scoring selects the posterior proportional to $\pi(s)\lambda_P(s)$. Extensionality requires these weights to be constant over states in $P$. Our least-favorable weighting fails that condition for $S$ whenever $p\ne1/2$. Robust optimization selects a particular weighting; it does not abolish weights.

The minimax-loss solution admits a different least-favorable weighting: all weight on no disclosure. That weighting is extensional. The difference between the criteria can therefore be expressed either as different treatment of unavoidable error or as selection of different least-favorable weights. These are compatible descriptions of one calculation.

However, an as-if probability representation is not yet an evidential warrant. A mathematical dual variable can rationalize an optimal policy without describing what the learner should believe about the source. Here the adversarial likelihood ratio is selected jointly with an accuracy criterion. Changing the criterion can change the optimal probability announcement even while prior information and the set of possible sources remain fixed. To identify the announcement with belief, one needs a reason why this optimization-generated model is epistemically authoritative.

The relevant choice is therefore between standards that select different weights, not between weighted evaluation and an absence of weights. A robust-Bayes representation explains the optimal policy; it does not independently justify the selected standard.

A related point holds beyond two states without extending the square-root rule. Let $S$ be any finite state space, let $\pi$ be regular, and evaluate forecasts by a strictly proper loss with finite Bayes risk $H(\pi)$. Allow all factive mechanisms and all content-based rules. The no-disclosure mechanism forces expected loss at least $H(\pi)$, with equality only if the rule responds to $S$ with $\pi$. The rule that always announces $\pi$, regardless of the report, attains exactly $H(\pi)$ under every mechanism. Therefore every ex-ante minimax-loss rule preserves the prior on $S$, and the minimax value is $H(\pi)$.

This finite-state result does not establish conditionalization. The constant rule is a minimax solution despite ignoring decisive reports. In the binary quadratic setting it is weakly dominated by the evidence-respecting rule with the same response to $S$: correcting the singleton responses reduces loss whenever a singleton occurs and never increases it. Adding admissibility therefore eliminates that particular defect there. With more states, partial reports create further constraints, so the binary conclusion cannot simply be exported.

The lesson is that a worst-case guarantee can underdetermine behavior precisely where learning succeeds. Its worst case may be an experiment in which no rule can learn anything. A minimax objective then needs an additional selection principle to distinguish excellent from poor performance in easier experiments. Regret is one principled attempt to supply such discrimination, because it measures opportunity relative to what each experiment permits. The issue is whether that useful policy motivation also establishes a belief norm.

This places the two criteria in a more balanced light. Raw expected loss can be too insensitive to exploitable information; regret can be sensitive to an ideal learner's unavailable information. Neither description alone decides between them. A prediction designer can choose according to the guarantee required. A philosophical theory of belief must additionally explain why the chosen guarantee has authority over the agent's epistemic position.

The connection to known robust updating work is especially important here. Van Ommen and colleagues (2016) already investigate when optimal updates can be independent of the loss function and when they cannot. The present argument should not be read as discovering that loss matters under ambiguity. Its distinctive contribution is the exact equalizer and preservation characterization for this factive-report game, used to identify which extra premise a particular belief interpretation requires.

The connection with weighted accuracy extends more generally under additional regularity assumptions. Consider a finite state space and its finite collection of deterministic factive situations. Let the admissible rules form the product of probability simplexes, one for each nonempty report. Suppose the loss is finite, continuous, strictly proper, and convex in each forecast. Then the rule space is compact and convex, and regret is convex in the rule. A probability weighting over situations is a point in another finite simplex.

The minimax theorem gives an optimal weighting $\lambda^*$ for which any minimax-regret rule minimizes

$$\sum_E\lambda^*(E)\left[L_E(f)-m_E\right].$$

The subtracted term does not depend on $f$, so this is exactly the weighted expected-loss problem. Define $w_P(s)=\sum_{E:E(s)=P}\lambda^*(E)$. Rearranging its terms gives a separate proper-scoring problem for each positive-weight report, with distribution

$$r_P(s)=\frac{\pi(s)w_P(s)}{\sum_t\pi(t)w_P(t)}.$$

Strict propriety therefore requires $f(P)=r_P$. For a regular prior, this equals content conditionalization on $P$ exactly when $w_P$ is constant on $P$. Zero-weight reports remain unconstrained by this representation. This is the standard least-favorable-weighting argument combined with the weighted accuracy characterization, not a new general robust-Bayes theorem; the game-theoretic relationship between robust prediction and Bayesian representations is developed by Grünwald and Dawid (2004).

The qualification about convexity concerns the forecast variable. It is needed for this compact minimax argument, unlike the earlier vertex reduction, which used convexity in the mechanism. The general binary equalizer and exceptional-score theorem were proved directly and do not rely on extending this minimax result beyond its assumptions. In particular, one should not apply a convenient convexity theorem indiscriminately to every proper scoring rule.

This general formulation strengthens the interpretation of the binary example. Least-favorable weights do not have to be stipulated by the learner before optimization; they can emerge from it. Yet their emergence depends on what was optimized. The fact that a rule is Bayes for some weighting tells us how its prescriptions can be represented, while extensionality tells us when that representation licenses content-only conditioning. Neither fact identifies the weighting as the learner's justified model of observation.

It also separates two questions about nonuniqueness. The minimax policy may be unique on every report that matters to its worst cases, while its least-favorable weighting is not unique. Conversely, reports absent from every binding situation may admit many equally optimal responses. A belief interpretation needs to address whichever underdetermination occurs; a performance theorem cannot settle it merely by displaying one dual optimizer.

The proposed contribution is thus compatible with the broader robust-Bayes tradition. It uses an especially transparent instance to expose the interpretive burden and then characterizes an otherwise hidden exception. The exceptional score matters because it prevents an overbroad conclusion that regret and content preservation are inherently incompatible. What is incompatible is preservation across all binary priors together with any bounded differentiable proper loss in the specified class.

## 8. Is the comparator a permissible epistemic ideal?

The strongest objection comes from the restriction to content-based rules itself. If rational updating must respond identically to the same prior and proposition, why compare its performance with rules that exploit the identity of the learning situation? The comparator can exploit distinctions the admissible rule is required to ignore. Regret may therefore appear to restore through evaluation precisely the contrastiveness excluded from the action space.

This objection does not show that regret is incoherent. Performance evaluation often compares constrained agents with an unconstrained ideal. The resulting gap can measure the cost of a constraint, including the cost of ignorance about a reporting protocol. A designer deciding whether to buy protocol information may reasonably care about that gap. Likewise, a predictor can hedge against the possibility that an apparently empty report was highly diagnostic.

But the objection does defeat an easy epistemic justification. The ideal's extra information cannot be treated as information the learner possesses. A comparison with a better-informed rule establishes an opportunity cost, not a new likelihood justified by the learner's evidence. To infer a belief from that cost requires a principle saying that avoidance of such opportunity loss determines rational credence even when its benchmark uses unavailable information.

I would accept that principle as a possible account of a forecasting policy, and reject it as sufficient for a unique, evaluation-independent belief. The reason is not that unavailable information can never matter normatively. It is that the same information deficit admits different tradeoffs under proper scores, while the putative belief is supposed to summarize what the agent has learned. Proposition 5 makes the missing commitment exact: even preservation of the prior across all priors privileges a particular score.

One can see the evaluative choice by adding a mechanism-specific constant $d_E$ to every rule's loss under $E$. Regret is unchanged, since the same constant is added to its comparator. Worst raw expected loss can change, since different mechanisms can become worst. Regret therefore treats differences in unavoidable background difficulty as irrelevant to comparisons between rules. That is attractive when assessing skill or exploitation of available opportunities.

For belief formation, however, the relevant baseline is disputed. A difficult experiment may leave genuine uncertainty that should still shape the agent's epistemic position. Subtracting its irreducible loss removes that difficulty from the performance comparison; it does not remove the uncertainty from the evidence. The procedure needs a bridge from one operation to the other. This is why the claim that regret is fairer to learners cannot by itself establish what a learner should believe.

A defender may instead privilege quadratic inaccuracy as the correct measure of epistemic value. Then $2/3$ is the unique regret-optimal answer here, and the existence of other proper losses does not refute that normative theory. I agree. My objection is conditional on the weaker premise often offered: that strict propriety and robust accuracy suffice. A theory with an independently defended unique score has supplied part of the missing account. It must still defend the mechanism-specific comparator and the policy's temporal interpretation.

## 9. What happens when the task changes?

The difference between a score-optimal forecast and a portable posterior can be calculated. Consider a bet paying one unit if $a$ occurs, with price $c\in(0,1)$. On singleton reports, accept at $a$ and decline at $b$. Let $x\in[0,1]$ be the probability of accepting after $S$. The comparator chooses its action separately for each known mechanism. Put $A=p(1-c)$ and $B=(1-p)c$. The regrets under the selective mechanisms are

$$\operatorname{Reg}_{E_a}(x)=A(1-x),\qquad
\operatorname{Reg}_{E_b}(x)=Bx.$$

Under $N$, regret is $\max\{p-c,0\}-x(p-c)$. Since $p-c=A-B$, this is bounded by $A(1-x)$ if $p\ge c$, and by $Bx$ otherwise. Full revelation gives zero regret. Thus the unique optimal mixed response is

$$x^*=\frac{p(1-c)}{p(1-c)+(1-p)c}.$$

At $p=0.8,c=0.75$, the optimal acceptance probability is $4/7$. If only pure acts are allowed, acceptance has worst regret $0.15$ and refusal has worst regret $0.20$, so acceptance uniquely wins. In contrast, a risk-neutral expected-utility agent treating the quadratic forecast $2/3$ as her posterior declines. The disagreement is actual, not a possibility left open by the analysis.

The least-favorable mixture puts probability $B/(A+B)$ on $E_a$ and $A/(A+B)$ on $E_b$. Conditioning the resulting joint model on $S$ gives

$$\Pr(a\mid S)=\frac{pB}{pB+(1-p)A}=c.$$

Its posterior equals the bet's price. This is a standard two-action equalizer, not a new general result about regret. It exposes what the dual distribution does: it makes the actions in the optimized decision problem indifferent. Changing the price changes that distribution even though the prior and report are fixed.

There is consequently no single posterior that implements the optimal mixed response for every price under ordinary risk-neutral expected-utility maximization. Since $0<x^*<1$ at every $c\in(0,1)$, both acts must be optimal; expected utility permits that only if the posterior equals $c$. One number cannot equal every price. If randomization is forbidden, the conclusion changes: pure minimax regret accepts exactly when $p\ge c$, so the original prior implements all the pure choices. The action space matters as well as the score.

This does not refute task aggregation. Che, Li, and Luo explicitly motivate a general-purpose rule by aggregating decisions before optimizing, rather than reoptimizing separately for each task. A rule for a selected aggregate need not solve every constituent problem. The calculation instead rules out an overly strong portability requirement: simultaneous optimality for all separate tasks. A philosophical interpretation of their rule should specify the aggregate it serves; it should not promise taskwise minimax regret. The remaining issue is the authority of that aggregate as a standard of epistemic assessment.

## 10. Timing and noncontrastiveness

All calculations so far evaluate an advance policy under the initial prior. After $S$ arrives, a kernel $(\alpha,\beta)$ gives the conditional state probability $p\alpha/[p\alpha+(1-p)\beta]$. Across allowed kernels this ranges over $[0,1]$. Reoptimizing conditional quadratic regret therefore gives $1/2$, not the ex-ante square-root response. Conditional worst expected quadratic loss also gives $1/2$. The contrast between loss and regret is an ex-ante one.

Grünwald and Halpern (2011) analyze minimax updating games with different information available to Nature; Halpern and Leung (2016) analyze dynamic regret. The present calculation illustrates that distinction. Carrying forward the chosen least-favorable joint model and conditioning it preserves the ex-ante recommendation, but is a different procedure from optimizing against all conditionally possible models again. Neither procedure follows from the bare instruction to minimize regret.

Meehan and Zhang have a further reason to reject mechanism-sensitive prescriptions. Their idempotence argument identifies noncontrastiveness with invariance under learning the same proposition again, formalized through intersecting learning situations with the original prior held fixed (2025, pp. 319–320, Fact 6). The present regret rule remains content-based for each fixed prior: its recommendation does not inspect which mechanism is actual. It therefore does not violate that stated constraint merely by assigning a non-Bayesian response to $S$.

But sequential reuse raises a separate issue. For quadratic loss, the odds of $q^*$ are the square root of the prior odds. If a learner applies the same map afresh after each repetition of tautological content, the odds after $k$ repetitions are $[p/(1-p)]^{2^{-k}}$, tending to one. For $p\ne1/2$, this fails the sequential idempotence requirement distinguished in their note 27. There is no contradiction with Fact 6: the rule fails the accumulation principle that connects their two formulations. Repeated fresh optimization is not the same as evaluating the combined evidence once.

A defender of regret can keep the original optimization problem fixed, treat new source events as genuinely new evidence, or supply an explicit dynamic model. Each is available. None licenses sequentially applying the one-shot rule to unchanged content while also maintaining accumulation. This is a substantive constraint on interpreting the rule as a method of belief revision, rather than a purely verbal distinction between a policy and a belief.

The comparator objection remains. META-COND uses distinctions the admissible content-based rule ignores. The resulting regret measures the performance cost of that restriction. It does not show that a learner possesses the comparator's information. Someone persuaded by Meehan and Zhang's epistemic case for noncontrastiveness may reject that benchmark, even though the evaluated rule is itself noncontrastive. The proofs establish what follows from using it, not an independent reason that epistemic rationality requires its use.

The resulting verdict is limited but definite. Worst expected loss does not uniquely select conditionalization in the unrestricted action space. Worst regret does not select a score-independent response, and can shrink or extremize confidence even within symmetric proper scores. The least-favorable distribution remains a weighting, with a role tied to the chosen evaluation. Robustness therefore relocates the choice of a learning standard in these two formulations; it does not remove it. The results leave open other robust criteria, a privileged epistemic score, and the behavior of boosting regret on larger state spaces with partial reports.

## References

Buja, Andreas, Werner Stuetzle, and Yi Shen. 2005. “Loss Functions for Binary Class Probability Estimation and Classification: Structure and Applications.” Manuscript, November 3. https://sites.stat.washington.edu/wxs/Learning-papers/paper-proper-scoring.pdf.

Che, Yeon-Koo, Longjian Li, and Tianling Luo. 2026. “Learning Against Nature: Minimax Regret and the Price of Robustness.” Preprint, arXiv:2602.15246. https://arxiv.org/abs/2602.15246.

Grünwald, Peter D., and A. Philip Dawid. 2004. “Game Theory, Maximum Entropy, Minimum Discrepancy and Robust Bayesian Decision Theory.” *The Annals of Statistics* 32(4): 1367–1433. https://doi.org/10.1214/009053604000000553.

Grünwald, Peter D., and Joseph Y. Halpern. 2011. “Making Decisions Using Sets of Probabilities: Updating, Time Consistency, and Calibration.” *Journal of Artificial Intelligence Research* 42: 393–426. https://doi.org/10.1613/jair.3374.

Halpern, Joseph Y., and Samantha Leung. 2016. “Minimizing Regret in Dynamic Decision Problems.” *Theory and Decision* 81: 123–151. https://doi.org/10.1007/s11238-015-9526-8.

Meehan, Alexander, and Snow Zhang. 2025. “Bayes Is Back.” *The Philosophical Review* 134(3): 285–350. https://doi.org/10.1215/00318108-11873775.

van Ommen, Thijs, Wouter M. Koolen, Thijs E. Feenstra, and Peter D. Grünwald. 2016. “Robust Probability Updating.” *International Journal of Approximate Reasoning* 74: 30–57. https://doi.org/10.1016/j.ijar.2016.03.001.


