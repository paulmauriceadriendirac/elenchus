# Learning Nothing Under Minimax Regret

**Abstract.** Robustness does not specify a unique way to evaluate learning rules. In a binary learning problem with a fixed regular prior, I compare worst-case expected inaccuracy with worst-case regret relative to the best rule for each reporting mechanism. Under the quadratic score and unrestricted factive reporting, the former preserves the prior on receiving a tautology. The latter uniquely transforms a prior $p$ into $\sqrt p/(\sqrt p+\sqrt{1-p})$, moving it toward one half. The result holds against randomized as well as deterministic mechanisms. It does not require changing the prior over states or counting some mechanisms more often than others. The disagreement instead comes from subtracting a mechanism-specific performance benchmark. This supplies a concrete limitation on replacing total-accuracy evaluations by an unspecified appeal to robustness, and distinguishes tautological report content from an observation known to be uninformative. The general study of robust and regret-based updating is established; the proposed contribution is this exact factive-reporting analysis and its implications for No News.

## 1. Which disappointment should a learner avoid?

Suppose you assign probability $0.8$ to $a$ and $0.2$ to $b$. A source will send you a true proposition about which state obtains. It might identify the state. It might say only that either $a$ or $b$ obtains. You know that it tells the truth, but not how it decides which true proposition to send.

What should you do if it sends the tautology?

Conditionalizing on its content leaves your probability of $a$ at $0.8$. But the event of receiving that content might be informative. A source might send the tautology only when $a$ obtains and disclose $b$ when $b$ obtains. Another might do the reverse. An update rule that receives only the proposition cannot tell which source it is dealing with.

One response is to evaluate rules across all possible reporting mechanisms. Meehan and Zhang (2025) develop an accuracy-based approach of this kind, using totals across learning problems. A tempting alternative is to avoid choosing weights over problems and require a rule to be robust against the worst possible mechanism.

That proposal is incomplete. We can minimize the worst expected error, or minimize the worst shortfall from what could have been achieved under the mechanism actually used. In the example above these criteria give different answers. The first retains $0.8$. The second changes it to $2/3$.

The mathematical reason is simple enough to expose. The uninformative mechanism has substantial unavoidable error, while the mechanisms whose selective silence reveals the state have none for a learner who knows the mechanism. Subtracting that different baseline changes which risks dominate. Robustness is not an escape from normative choices about evaluation. It makes a different choice necessary.

## 2. The decision problem

Let $S=\{a,b\}$, with prior $\pi(a)=p\in(0,1)$. A deterministic reporting mechanism $E$ assigns to each state a proposition containing that state. There are exactly four:

| Mechanism | Report at $a$ | Report at $b$ |
|---|---|---|
| $R$, full revelation | $\{a\}$ | $\{b\}$ |
| $N$, no disclosure | $S$ | $S$ |
| $E_a$, selective silence at $a$ | $S$ | $\{b\}$ |
| $E_b$, selective silence at $b$ | $\{a\}$ | $S$ |

An updating rule maps a received proposition to a posterior distribution. It must use the same posterior for the same proposition across mechanisms. This is the restriction Meehan and Zhang call global evidential constancy. The rule knows the initial prior but is not given the mechanism's identity as a separate input.

We consider evidence-respecting rules: receiving $\{a\}$ produces certainty in $a$, and receiving $\{b\}$ produces certainty in $b$. The only choice is then

$$q=f(S)(a).$$

This restriction does not raise the minimum attainable loss or regret in the problem. Since reports are true, replacing an uncertain response to a singleton with certainty weakly reduces expected quadratic loss under every mechanism. It also weakly reduces regret, whose comparator is fixed independently of the learner's chosen rule. Uniqueness statements below concern the evidence-respecting class.

Use the sum of squared errors on the two state propositions:

$$\ell(q,a)=2(1-q)^2,\qquad\ell(q,b)=2q^2.$$

The factor two records both coordinates of the probability vector. It affects the numerical losses but not the optimal choice. Write $L_E(q)$ for the rule's expected loss under mechanism $E$, averaging states with the fixed prior $p$.

For each $E$, let

$$m_E=\min_r L_E(r),\qquad
\operatorname{Reg}_E(q)=L_E(q)-m_E.$$

The comparator may be chosen separately for each mechanism. It is the best report-based rule a designer could select knowing that mechanism. It does not receive the actual state as an extra input. Under $N$, no report-based rule can identify the state. Under either selective-silence mechanism, by contrast, the two different reports identify it exactly.

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

This distinction also explains why an analogy with choosing initial credences can mislead. Pettigrew (2016, §4) discusses minimax and minimax regret in an accuracy argument for indifference. In that setting, the best statewise accuracy is the same at every state, so subtracting it leaves the relevant ranking unchanged. Here the alternatives facing the adversary are mechanisms evaluated in prior expectation. Their best achievable expected losses differ. The equivalence of the two criteria consequently disappears.

## 5. Randomization does not rescue No News

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
=\sup_r\big[L_K(q)-L_K(r)\big].$$

It is therefore a supremum of affine functions of $K$, hence convex in $K$. Express any stochastic mechanism as a convex combination of the four vertices. Convexity bounds its regret by the same combination of vertex regrets, and therefore by their maximum. Since the vertices are themselves allowed, the worst-case regret is exactly the worst vertex regret. The two optimization problems consequently reduce to those already solved. ∎

The comparator in this proof knows the stochastic kernel, including its randomization probabilities. It is not allowed to see an unobserved random seed. There is thus no hidden strengthening to a clairvoyant comparator when randomized mechanisms are admitted.

This result also clarifies the appeal of worst-case evaluation. Duplicating a mechanism in a list does not alter the maximum, whereas it can alter an unnormalized total. The method is insensitive to that particular counting convention. But this invariance does not determine whether we should maximize absolute performance or performance relative to a mechanism-specific optimum. Removing one representational choice leaves an evaluative choice.

## 6. Is it irrational to revise on a tautology?

A natural objection invokes **No News**: on learning the whole state space, retain the prior. Equation (1) violates that condition whenever the prior is nonuniform.

There are two readings of the objection. If the agent knows that $N$ is the mechanism, the received report is known to be uninformative. With that restricted uncertainty set, both expected-loss and regret minimization uniquely retain $p$. The theorem does not recommend revising on an observation known to carry no information.

If the agent knows only that the report is true, its tautological *content* does not establish that its occurrence is uninformative. Under $E_a$ and $E_b$, the very same content identifies opposite states. Global evidential constancy forces the rule to give one response across those different circumstances. The minimax-regret rule compromises between them.

This is not a refutation of Bayesian conditioning on a fully specified observation event. If the source mechanism were supplied probabilistically, one would condition on the event that it issued $S$. The present problem deliberately withholds that probabilistic specification. Its question is which rule to choose across a set of mechanisms, given only a prior over the underlying states.

One can still reject the regret recommendation. The protocol-specific comparator may be too demanding: it judges the learner against a rule chosen using information about the source that the learner lacks. But that is an objection to the performance standard, not an algebraic objection. Regret deliberately measures the opportunity lost through that lack of knowledge. If this is the wrong epistemic disappointment to prioritize, the criterion needs a normative defense or rejection.

A second qualification concerns timing. The optimization above is **ex ante**: evaluate each rule in prior expectation before the report arrives. If, after receiving $S$, the agent instead minimizes maximum *conditional* regret over the still-possible mechanisms, $E_a$ yields regret $2(1-q)^2$ and $E_b$ yields $2q^2$. These force the unique optimum $q=1/2$; $N$'s conditional regret $2(q-p)^2$ does not overturn it. For a nonuniform prior, this differs from (1).

Thus the ex-ante rule is not automatically stable under reapplying a conditional worst-case criterion after observation. This is a limitation to explain, not an inconsistency in the calculation. A complete normative theory must specify whether it evaluates an advance policy or a decision reconsidered after a report, and justify the relation between those evaluations. The phrase “minimize regret” settles neither question by itself.

## 7. What is established, and what is additional

Robust probability updating is an established research program. Van Ommen, Koolen, Feenstra, and Grünwald (2016) study minimax updating when a prior over outcomes is available but the coarsening mechanism is not fully specified. Their framework permits general finite message spaces and loss functions. The present essay does not introduce robust updating or the idea that the loss criterion matters. Its focus is the change produced by subtracting the optimum separately for each mechanism.

Regret-based learning under uncertainty about data generation is also not new. Che, Li, and Luo (2026) explicitly study ex-ante minimax-regret belief formation relative to an oracle who knows the data-generating process. Their principal analysis concerns repeated signals and unknown precision. The problem here instead uses a single factive set-valued report and an unrestricted mechanism on a binary state space. Its distinctive calculation concerns the response to tautological content, together with the comparison between absolute loss, ex-ante regret, and conditional regret. Any broader claim to originate regret-based robust learning would be false.

The exact square-root rule is offered as a small, fully derived result in that setting, with novelty status still provisional. Its philosophical relevance is the separation of three commitments often run together: retaining a fixed prior over states, declining to choose a prior over mechanisms, and preserving No News. The first two do not entail the third. Under ex-ante minimax regret with quadratic accuracy, they coexist with a systematic move away from the initial prior on a tautological report.

The example also limits an objection to aggregate accuracy arguments. Saying that a weighted total should be replaced by robustness does not yet establish an alternative vindication of Bayes. Worst expected error and worst regret agree on what is possible, and disagree on what to do. The criterion must earn its epistemic authority through an account of which avoidable losses matter.

The central question is therefore about the relevant opportunity. Should a learner primarily guard against being inaccurate when little could have been learned, or against failing to exploit information that a better-informed designer could have extracted? On a two-state problem, that difference already determines whether receiving a tautology leaves an $0.8$ prior unchanged or moves it to $2/3$. A theory of rational learning needs an answer before it can treat robustness as a reason for a particular updating rule.

## References

Che, Yeon-Koo, Longjian Li, and Tianling Luo. 2026. “Learning Against Nature: Minimax Regret and the Price of Robustness.” Preprint, arXiv:2602.15246v1. https://arxiv.org/abs/2602.15246v1.

Meehan, Alexander, and Snow Zhang. 2025. “Bayes Is Back.” *The Philosophical Review* 134(3): 285–350. https://doi.org/10.1215/00318108-11873775.

Pettigrew, Richard. 2016. “Accuracy, Risk, and the Principle of Indifference.” *Philosophy and Phenomenological Research* 92(1): 35–59. https://doi.org/10.1111/phpr.12097. Author version: https://research-information.bris.ac.uk/ws/portalfiles/portal/54555540/POI.pdf.

van Ommen, Thijs, Wouter M. Koolen, Thijs E. Feenstra, and Peter D. Grünwald. 2016. “Robust Probability Updating.” *International Journal of Approximate Reasoning* 74: 30–57. https://doi.org/10.1016/j.ijar.2016.03.001. Author-hosted copy: https://homepages.cwi.nl/~pdg/ftp/robprob.pdf.
