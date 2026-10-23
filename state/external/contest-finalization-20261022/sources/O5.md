# Can Regret Minimization Determine What to Believe?

**Abstract.** A robust prediction policy need not determine a general-purpose belief. In a binary problem with a fixed prior and arbitrary factive reporting, I characterize ex-ante minimax regret under a class of strictly proper losses. The optimal response to a tautological report equalizes prior-weighted statewise losses. Quadratic loss gives a square-root transformation of the prior; logarithmic loss gives a different answer. I then characterize the exception: preserving the prior for every initial probability uniquely selects the known boosting loss, up to the stated normalizations. No bounded loss in the class has that preservation property. These results concern a factive-reporting instance of established robust learning theory. They do not make minimax regret non-Bayesian: under quadratic loss its rule is Bayesian for an explicit least-favorable protocol. The philosophical issue is why that adversarial protocol, selected through a particular evaluation of performance, should represent evidence. I argue that regret establishes a policy recommendation unless supplemented by a defense of the score, comparator, and timing as determinants of belief.

## 1. A forecast is not yet a belief

A learner assigns probability $0.8$ to $a$ and $0.2$ to $b$. She will receive a true proposition, selected by an unspecified process. A prediction system must tell her what number to announce after each possible report. Suppose the process says only that either $a$ or $b$ obtains. An ex-ante minimax-regret system evaluated by quadratic inaccuracy announces $2/3$. Evaluated by logarithmic inaccuracy, it announces approximately $0.7245$. Both scores are strictly proper: when the relevant probability distribution is known, each uniquely rewards reporting that distribution.

What, then, has the learner come to believe? It would be premature to identify either announcement with a uniquely justified degree of belief merely because it optimizes an epistemic performance measure. The optimization problem includes a choice of measure, a comparison class, and a timing of evaluation. The evidence alone has not selected those choices.

This is a problem of interpretation rather than a criticism of robust prediction. A system may sensibly choose an announcement that limits its worst missed opportunity. Such announcements can be essential when the observation process is incompletely modeled. But the warrant to make a good announcement under one evaluation is weaker than the warrant to adopt it as a probability transferable across evaluations.

The contrast is particularly sharp with strictly proper scores. If a single posterior had already been justified, minimizing its expected inaccuracy would recover it under every strictly proper score. In the present problem, the robust procedure instead uses the score to help select the posterior. That reversal requires a philosophical defense. Proper scoring by itself supplies none.

I examine a small setting in which the entire dependence is visible. The exact quadratic solution is followed by a general characterization and an exceptional-score theorem. The latter identifies which loss makes ex-ante regret preserve the prior on the whole-space report for every initial probability. The answer is a known score, not a newly invented one, but its role in this reporting problem is distinctive.

The argument is deliberately limited. Robust updating and regret-based learning are established programs. Che, Li, and Luo (2026) already contrast minimax regret with worst expected loss, and examine both single observations and repeated learning. Van Ommen and colleagues (2016) study unknown coarsening mechanisms under minimax expected loss. I contribute a precise test case for the philosophical transition from an optimal policy to a belief, together with a characterization of when a natural preservation requirement holds.

## 2. The decision problem

Let $S=\{a,b\}$, with prior $\pi(a)=p\in(0,1)$. A deterministic reporting mechanism $E$ assigns to each state a proposition containing that state. There are exactly four:

| Mechanism | Report at $a$ | Report at $b$ |
|---|---|---|
| $R$, full revelation | $\{a\}$ | $\{b\}$ |
| $N$, no disclosure | $S$ | $S$ |
| $E_a$, selective silence at $a$ | $S$ | $\{b\}$ |
| $E_b$, selective silence at $b$ | $\{a\}$ | $S$ |

An updating rule maps a received proposition to a probability forecast. Whether the optimal forecast deserves interpretation as the learner’s belief is the philosophical question, not part of this definition. It must use the same posterior for the same proposition across mechanisms. This is global evidential constancy in Meehan and Zhang’s terminology (2025, Fact 5). The rule knows the initial prior but is not given the mechanism's identity as a separate input.

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

Now replace quadratic loss by a binary strictly proper loss with components $l_a(q)$ and $l_b(q)$. Assume that they are nonnegative, continuous on the open interval, and extend to zero at the correct certainty: $l_a(1)=l_b(0)=0$. Assume that $l_a$ strictly decreases and $l_b$ strictly increases. Wrong-certainty losses may be infinite. Strict propriety means that, for every $p\in(0,1)$, the expected loss $p l_a(q)+(1-p)l_b(q)$ is uniquely minimized at $q=p$.

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

*Proof.* $A$ decreases strictly and $B$ increases strictly, with opposite order at the endpoints. Their unique crossing minimizes $\max\{A,B\}$. Write their common value there as $M$. Since this is the minimum of that maximum, $M\leq\max\{A(p),B(p)\}\leq H(p)$. Thus the regret under no disclosure is $2M-H(p)\leq M$, so it does not change the minimizer. The extension to all randomized mechanisms follows as before. For absolute loss, no disclosure supplies the lower bound $H(p)$, attained only at $q=p$ by strict propriety. At $p$, the selective losses are nonnegative summands of $H(p)$ and cannot exceed it. ∎

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

The components in (4) are the known boosting loss on the probability scale, explicitly displayed by Buja, Stuetzle, and Shen (2005, p. 2). I claim neither the score nor its propriety as new. The proposed increment is its characterization by content preservation in this minimax-regret reporting problem. The assumptions matter: the theorem does not classify nondifferentiable losses, nonproper objectives, or constraints on reporting mechanisms.

This result changes the philosophical diagnosis. Keeping the prior does not mark a categorical boundary between Bayesian belief and robust regret. Regret can keep it, but only under a highly specific shape of accuracy loss within this class. Conversely, boundedness and strict propriety do not together secure preservation. A purportedly general epistemic recommendation therefore cannot be obtained by saying only that the evaluator cares about accuracy and avoidable error.

One might suspect that the disagreement is driven entirely by admitting losses that explode near certainty. It is not. Consider another bounded symmetric strictly proper loss,

$$l_a(q)=\frac12-3q^2+4q^3-\frac32q^4,\qquad
l_b(q)=2q^3-\frac32q^4.$$

Its derivatives are $l_a'(q)=-6q(1-q)^2$ and $l_b'(q)=6q^2(1-q)$. Consequently the derivative of expected loss at truth probability $p$ is $6q(1-q)(q-p)$. This is negative before $p$ and positive after it, establishing strict propriety. The components are normalized, bounded, strictly monotone on the interior, and exchanged by interchanging the state labels.

At $p=4/5$, evaluate the equalizer equation at the quadratic answer $q=2/3$. The two prior-weighted losses are $2/45$ and $8/135$, respectively, and are unequal. The unique optimum therefore differs from the quadratic optimum even within bounded symmetric proper losses. Multiplying this score by a positive constant cannot remove the disagreement. Its cause is the distribution of penalties across probability errors, not an arbitrary overall unit of measurement.

This example also cautions against interpreting movement toward one half as a universal law of regret. Proposition 4 supplies an equalization equation for the stated class; it does not assert the same direction or size of movement for every member. Proposition 5 already provides a counterexample to strict movement: boosting loss preserves every prior. An epistemological conclusion should be based on the characterization, not an extrapolation from the aesthetically simple square-root formula.

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

This is the central normative claim of the essay. I do not deny that robust rules can be represented as Bayesian. I deny that such a representation, alone, turns their endogenous weights into evidence. It supplies an explanation of the policy's performance, while leaving the interpretation of its probability open.

A related point holds beyond two states without extending the square-root rule. Let $S$ be any finite state space, let $\pi$ be regular, and evaluate forecasts by a strictly proper loss with finite Bayes risk $H(\pi)$. Allow all factive mechanisms and all content-based rules. The no-disclosure mechanism forces expected loss at least $H(\pi)$, with equality only if the rule responds to $S$ with $\pi$. The rule that always announces $\pi$, regardless of the report, attains exactly $H(\pi)$ under every mechanism. Therefore every ex-ante minimax-loss rule preserves the prior on $S$, and the minimax value is $H(\pi)$.

This finite-state result does not establish conditionalization. The constant rule is a minimax solution despite ignoring decisive reports. In the binary quadratic setting it is weakly dominated by the evidence-respecting rule with the same response to $S$: correcting the singleton responses reduces loss whenever a singleton occurs and never increases it. Adding admissibility therefore eliminates that particular defect there. With more states, partial reports create further constraints, so the binary conclusion cannot simply be exported.

The lesson is that a worst-case guarantee can underdetermine behavior precisely where learning succeeds. Its worst case may be an experiment in which no rule can learn anything. A minimax objective then needs an additional selection principle to distinguish excellent from poor performance in easier experiments. Regret is one principled attempt to supply such discrimination, because it measures opportunity relative to what each experiment permits. The issue is whether that useful policy motivation also establishes a belief norm.

This places the two criteria in a more balanced light. Absolute loss can be too insensitive to exploitable information; regret can be sensitive to an ideal learner's unavailable information. Neither description alone decides between them. A prediction designer can choose according to the guarantee required. A philosophical theory of belief must additionally explain why the chosen guarantee has authority over the agent's epistemic position.

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

One can see the evaluative choice by adding a mechanism-specific constant $d_E$ to every rule's loss under $E$. Regret is unchanged, since the same constant is added to its comparator. Worst absolute loss can change, since different mechanisms can become worst. Regret therefore treats differences in unavoidable background difficulty as irrelevant to comparisons between rules. That is attractive when assessing skill or exploitation of available opportunities.

For belief formation, however, the relevant baseline is disputed. A difficult experiment may leave genuine uncertainty that should still shape the agent's epistemic position. Subtracting its irreducible loss removes that difficulty from the performance comparison; it does not remove the uncertainty from the evidence. The procedure needs a bridge from one operation to the other. This is why the claim that regret is fairer to learners cannot by itself establish what a learner should believe.

A defender may instead privilege quadratic inaccuracy as the correct measure of epistemic value. Then $2/3$ is the unique regret-optimal answer here, and the existence of other proper losses does not refute that normative theory. I agree. My objection is conditional on the weaker premise often offered: that strict propriety and robust accuracy suffice. A theory with an independently defended unique score has supplied part of the missing account. It must still defend the mechanism-specific comparator and the policy's temporal interpretation.

## 9. Before and after the observation

The optimization so far evaluates an advance rule in prior expectation. It is not the same as minimizing a worst conditional loss after the report arrives. Under a randomized protocol with $K(S\mid a)=\alpha$ and $K(S\mid b)=\beta$, the conditional probability of $a$ after $S$ is

$$r=\frac{p\alpha}{p\alpha+(1-p)\beta},$$

provided the denominator is positive. As the allowed protocol varies, $r$ ranges over all of $[0,1]$. The extreme selective mechanisms deliver its endpoints. This is a familiar form of dilation: a precise marginal probability does not imply a narrow conditional probability when the relation between state and observation is unspecified.

For quadratic loss, conditional regret is $2(q-r)^2$. Its worst value over the interval is uniquely minimized at $q=1/2$. Conditional absolute loss gives the same answer, since its worst value is $\max\{2(1-q)^2,2q^2\}$. The contrast between retaining $p$ and choosing $q^*$ is therefore specifically an ex-ante contrast. Reoptimization after the report erases it.

This is not a newly discovered temporal pathology. Grünwald and Halpern (2011) explain how different minimax updating games correspond to different information available to the adversary. Halpern and Leung (2016) analyze dynamic decision-making under regret. Che, Li, and Luo (2026, §2.2) also distinguish advance evaluation from conditional evaluation. The present example exhibits the issue with all quantities explicit.

There is a coherent way to retain the advance recommendation: update the least-favorable joint model $\pi K^*$ instead of reapplying worst-case optimization to the entire conditional model set. Ordinary conditioning then retains $q^*$ as the recommendation after $S$. But this is an additional rule for carrying the ex-ante model forward. It is not equivalent to conditional minimax regret over all remaining possibilities.

I favor retaining that distinction in the interpretation. An agent committed to a forecast policy can consistently execute it. A theorist who calls its outputs beliefs must explain why commitment to the least-favorable model should govern subsequent inference. Consistency achieved by fixing a model is valuable, but cannot establish that the fixed model was warranted initially.

The source story and an externalist learning-situation story also require separation. In the source story, receiving a tautology can be informative because its occurrence is selective. In the learning-situation interpretation, the two selective maps are opaque: some states inside the learned proposition would produce a different proposition. The formulas evaluate both descriptions, but the question of what is actually learned differs. The mathematics alone cannot settle whether content preservation is normatively required in either interpretation.

If the learner instead knows that the protocol is $N$, the ambiguity disappears. Every strictly proper score then uniquely recommends retaining $p$, whether one minimizes expected loss or regret. The disagreement studied here requires uncertainty about how the report was selected. It is therefore misleading to describe the example as revising belief after learning that nothing informative happened. Receiving tautological content and knowing that its occurrence was uninformative are different epistemic conditions. The challenge is to justify a particular compromise when the first condition holds and the second does not.

A useful way to see the interpretive pressure is to imagine two subsequent decisions. In one, the learner must announce a probability for quadratic assessment. In another, she must decide whether to accept a bet that pays one unit if $a$ occurs and costs $0.75$. A probability of $2/3$ recommends declining the bet; $0.8$ recommends accepting it. These prescriptions are not automatically inconsistent, because the optimal announcement in the first problem need not equal the belief used in the second.

The difficulty arises only when the announcement is promoted to a universal posterior without further argument. The minimax-regret calculation optimized a particular forecast assessment. It did not optimize every possible subsequent decision. Treating its output as a general belief licenses a transfer between evaluative settings that the calculation has not established. A complete policy for the later bet might still recommend declining, but that conclusion would need its own justification or an independently defended belief interpretation.

The example does not rely on pragmatic encroachment, on changing the evidence, or on irrationality in either task. It distinguishes the scope of a theorem from the scope of a semantic claim about its output. Calling a number a posterior often suggests that it can be inserted into arbitrary expected-utility calculations. A number chosen to minimize worst regret under one scoring system may not carry that unrestricted license.

A defender can respond by specifying a fixed distribution over future tasks. The scoring rule can then summarize their combined decision value. This gives the announcement a broader purpose than success on one isolated test. But the task distribution becomes part of the justification, and a different distribution may yield a different optimum. Che, Li, and Luo (2026) explicitly motivate general-purpose learning through an ex-ante evaluation across decisions. The present challenge concerns the additional step from such an aggregation to an evidence-determined belief, not the legitimacy of aggregating tasks.

The requirement of score portability should also be stated carefully. I do not require a rational agent to choose the same *action* under every loss. Different actions can serve the same belief under different stakes. Nor do I claim that all measures of epistemic value are equally compelling. The narrower requirement is that, when a method claims to identify a single posterior on purely evidential grounds, changing an independently supplied proper elicitation score should not alter what that posterior is said to be. Ordinary expected-loss elicitation has precisely this property once a posterior is fixed.

Someone who denies that requirement may adopt a more evaluative conception of belief. That is a substantive philosophical position, not a mathematical mistake. Its defense must explain why the constitutive score has epistemic authority and why the resulting beliefs may be transported across tasks. The comparison of Brier, logarithmic, bounded polynomial, and boosting losses identifies the choice this position must make.

It may be tempting instead to report the set of all posteriors allowed by the mechanisms. In the present example this is the whole interval after $S$. That representation is honest about what the mechanism set leaves unidentified, but it is not automatically a complete theory of rational action or belief. It requires a decision rule for acting with imprecision and an account of how subsequent evidence changes the set. The essay's conclusion is therefore not that imprecise probabilities solve the problem without further normative choices.

Rather, the available choices should remain visible. One can retain a set of models, privilege a score, endorse an aggregation of future tasks, or supply a probabilistic model of the source. Each adds structure absent from the bare description of robust accuracy. The point of the example is to prevent that additional structure from being mistaken for a consequence of truthfulness, strict propriety, or the original prior alone.

## 10. The boundary between robust policy and belief

A natural reply is that beliefs need not be independent of epistemic values. Perhaps rational degrees of confidence are constituted partly by the risks agents ought to take in pursuit of accuracy. Then different scores may express different permissible epistemic attitudes, rather than rival estimates of a single underlying posterior.

That reply is substantive and coherent. It gives up the claim that the output is determined by the prior, evidence, and unspecified robustness alone. It also changes what a general-purpose posterior promises. The posterior becomes general across tasks only relative to an endorsed aggregation of their evaluative demands. If that aggregation changes, the rational announcement may change without any new observation.

The distinction is useful even for someone sympathetic to such a theory. A probability can serve as a compact policy parameter, telling an agent how to act under a selected family of losses. It can instead summarize an evidential assessment intended to support decisions under independently supplied losses. These roles often coincide in ordinary Bayesian models, because a known posterior minimizes expected loss under every strictly proper scoring rule. They separate under the mechanism ambiguity examined here.

Consequently I propose a modest requirement on purportedly belief-producing robust methods: state which role the output fills, and supply an independent bridge if the second role is claimed. Suitable bridges might justify a particular observation model, defend a unique epistemic score, or explain why a chosen aggregation of tasks defines belief. Without one, the justified conclusion is a recommendation about forecasting performance.

The binary example isolates this burden without alleging a general impossibility of robust belief. Quadratic regret, logarithmic regret, and boosting regret can all be useful. Their disagreement shows that propriety does not determine the compromise. The exceptional-score theorem further shows that preserving the prior is itself a demanding evaluative choice within this game, not a default consequence of the word “regret.”

Finally, the results do not extend the square-root formula to arbitrary state spaces. With three or more states, proper partial reports create additional choices and couple responses across different propositions. Nor does the argument establish that every robust rule is unstable or that every score-dependent forecast is irrational. Its conclusion is about the warrant for moving from optimality under a specified evaluation to a claim about what has been learned.

Regret minimization answers a clear question: which policy best limits lost performance relative to a mechanism-informed comparator? A theory of belief asks a further question: why should that comparator, that score, and that treatment of time determine the agent's evidential assessment? The characterization above supplies a reason to keep those questions separate until the additional epistemic argument has been given.

## References

Buja, Andreas, Werner Stuetzle, and Yi Shen. 2005. “Loss Functions for Binary Class Probability Estimation and Classification: Structure and Applications.” Manuscript, November 3. https://sites.stat.washington.edu/wxs/Learning-papers/paper-proper-scoring.pdf.

Che, Yeon-Koo, Longjian Li, and Tianling Luo. 2026. “Learning Against Nature: Minimax Regret and the Price of Robustness.” Preprint, arXiv:2602.15246. https://arxiv.org/abs/2602.15246.

Grünwald, Peter D., and A. Philip Dawid. 2004. “Game Theory, Maximum Entropy, Minimum Discrepancy and Robust Bayesian Decision Theory.” *The Annals of Statistics* 32(4): 1367–1433. https://doi.org/10.1214/009053604000000553.

Grünwald, Peter D., and Joseph Y. Halpern. 2011. “Making Decisions Using Sets of Probabilities: Updating, Time Consistency, and Calibration.” *Journal of Artificial Intelligence Research* 42: 393–426. https://doi.org/10.1613/jair.3374.

Halpern, Joseph Y., and Samantha Leung. 2016. “Minimizing Regret in Dynamic Decision Problems.” *Theory and Decision* 81: 123–151. https://doi.org/10.1007/s11238-015-9526-8.

Meehan, Alexander, and Snow Zhang. 2025. “Bayes Is Back.” *The Philosophical Review* 134(3): 285–350. https://doi.org/10.1215/00318108-11873775.

van Ommen, Thijs, Wouter M. Koolen, Thijs E. Feenstra, and Peter D. Grünwald. 2016. “Robust Probability Updating.” *International Journal of Approximate Reasoning* 74: 30–57. https://doi.org/10.1016/j.ijar.2016.03.001.
