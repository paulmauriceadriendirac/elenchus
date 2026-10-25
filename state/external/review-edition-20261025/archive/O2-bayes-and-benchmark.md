# How Much Does Bayes Depend on the Benchmark?

**Abstract.** Meehan and Zhang defend Bayesian conditionalization by maximizing accuracy across learning situations. Their weighted theorem already identifies the exact condition for success: the aggregate learning profile must be extensional. I investigate what robustness means for this defense. First, an extensional benchmark remains exactly favorable to conditionalization under every sufficiently small redistribution of weight among its constituent learning situations if and only if every constituent is transparent. An aggregate can therefore accommodate opaque learning while its exact verdict depends on balancing the opaque cases. Second, under the quadratic score, the accuracy cost of a small imbalance is second order, provided the perturbation is small relative to each active report's baseline profile. Exact optimality can be fragile while approximate accuracy is stable. Finally, invariance under relabeling does not settle the issue when weights may depend on the prior. These results distinguish an exact normative vindication from a practically stable recommendation without confusing either with the rediscovery of coarsening at random.

## 1. The significance of a small change

A benchmark can cease to rank a method first after a tiny change even though the method's performance remains excellent. Conversely, a method can win by a wide margin on one benchmark while depending on a questionable choice of cases. An accuracy-based defense of a rule for belief revision must distinguish these possibilities. The question is not simply whether the defense is robust, but what is supposed to remain stable: the identity of the exact maximizer, the accuracy achieved, or the normative justification of the benchmark.

Meehan and Zhang's *Bayes Is Back* makes this issue particularly sharp. They defend Bayesian conditionalization for agents whose evidence need not be transparent. The Bayesian rule need not maximize expected accuracy in each such learning situation. Their proposal evaluates rules across situations instead, while requiring that a rule give the same response whenever the prior and learned proposition are the same. Conditionalization uniquely maximizes the uniform total. Their extension to weighted totals establishes that it remains optimal exactly when the weighting has an extensional learning profile (2025, Facts 10–11).

They explicitly recognize that the choice of weights needs a defense (2025, 335–339). It would be a mistake to present that dependence, or their characterization of extensionality, as a new objection. My contribution is to separate two consequences of their characterization that lead in different directions. **Exact optimality is unstable under unrestricted local reweighting as soon as the benchmark includes opaque learning, but the corresponding loss of accuracy can remain quadratically small.** A further distinction about symmetry blocks an easy attempt to settle the normative question by appealing only to neutral labeling.

The statistical background is indispensable. Coarsening at random, or CAR, characterizes when one may condition on the reported proposition without additionally modeling the reporting event. Grünwald and Halpern (2003, §3) establish the connection to probability updating. Gill and Grünwald (2008, §§2–4) show how CAR mechanisms extend beyond mixtures of partitions; their three-pair example already establishes that extension. Jaeger (2005, §4) studies stronger procedural robustness requirements. I use these results as background, not as discoveries. The particular issue here is how a normative total-accuracy benchmark can be unstable in its exact recommendation yet stable in the accuracy of that recommendation.

## 2. What an aggregate evaluates

Let $S$ be a finite state space and $\pi$ a probability distribution assigning positive probability to every state. A learning situation is a function $E$ that assigns each state $s$ a nonempty proposition $E(s)\subseteq S$ containing $s$. Factivity requires that what is learned be true. Transparency additionally requires

$$t\in E(s)\quad\Longrightarrow\quad E(t)=E(s).$$

A transparent situation is therefore a partition: each state delivers the cell containing it. In an opaque situation, a proposition can be delivered at one of its states but not another.

Fix the prior. A globally evidentially constant rule is a function $f$ from learned propositions to posterior probability distributions. It cannot respond differently to the same proposition merely because a different learning function delivered it. Write

$$b_p(s)=\pi(s\mid p)$$

for the Bayesian posterior, with value zero outside $p$. Let $A(q,s)$ score the accuracy of posterior $q$ at state $s$, with higher scores better. Strict propriety means that a probability distribution uniquely maximizes its own expected score by reporting itself.

Normalize the weights on a finite family $\mathcal F$ of learning situations so that $\sum_E\lambda(E)=1$. This rescaling changes no ranking. The benchmark is

$$
T_\lambda(f)=\sum_{E\in\mathcal F}\lambda(E)\sum_s\pi(s)A(f(E(s)),s).
$$

Its learning profile is

$$L_p(s)=\sum_{E:E(s)=p}\lambda(E).$$

For each $s$, the $L_p(s)$ sum to one over propositions containing $s$. Rearranging the finite sum gives

$$T_\lambda(f)=\sum_p\sum_{s\in p}\pi(s)L_p(s)A(f(p),s).$$

Define $Z_p=\sum_s\pi(s)L_p(s)$. For every active report, meaning $Z_p>0$, strict propriety makes the uniquely optimal response

$$r_p(s)=\frac{\pi(s)L_p(s)}{Z_p}.\qquad\text{(1)}$$

This is Meehan and Zhang's Lemma 1 (2025, 344–345). By their Lemma 2, it equals $b_p$ at every active report exactly when $L_p$ is constant on $p$. That is extensionality. A report never delivered anywhere has no effect on the benchmark and does not determine a unique response.

The CAR correspondence is now literal. Regard $L_p(s)$ as the conditional probability of receiving report $p$ at state $s$. Equation (1) is conditioning on receipt of the report. Extensionality says that, among the states where $p$ is true, receipt does not favor one state over another. This is the standard distinction between conditioning on an event and conditioning on its observation.

This representation does not show that the evaluator secretly has a subjective belief about the learning process. The same weights can represent objective importance. A mathematical representation as a probability model does not settle their normative interpretation. What it does establish is that the optimizing calculation uses the same state-to-report asymmetries, whatever justifies the weights.

Two notions of equivalence also need separation. Benchmarks can select the same optimal rule while ranking inferior rules differently. All extensional benchmarks with every report active select Bayesian conditionalization. They need not have proportional profiles or induce the same ranking of alternatives. A non-partition CAR construction therefore establishes a difference in possible profiles, not a new optimal rule unavailable to transparent benchmarks.

## 3. Robust exact optimality

Say that a benchmark is *locally exact* if conditionalization remains optimal after every sufficiently small redistribution of weights within the same family $\mathcal F$. Keep the prior, score, candidate rules, and learning functions fixed. Only their normalized weights change. This is a demanding but clear interpretation of robustness. It asks whether the exact recommendation survives uncertainty about how strongly to count the cases.

**Proposition 1.** Suppose $\lambda_0$ gives positive weight to every member of $\mathcal F$ and has an extensional profile. It is locally exact if and only if every member of $\mathcal F$ is transparent.

*Proof.* If every $E$ is transparent, its indicator profile $\mathbf 1_{E(s)=p}$ is constant on $p$: a proposition delivered anywhere is delivered at all its states. Every weighted mixture is therefore extensional, and conditionalization remains optimal.

Conversely, let $E^*\in\mathcal F$ be opaque. There are $s,t\in p$ such that $E^*(s)=p$ and $E^*(t)\ne p$. For any $0<\eta<1$, set

$$\lambda_\eta=(1-\eta)\lambda_0+\eta\delta_{E^*}.$$

This changes the weights arbitrarily little as $\eta$ tends to zero and keeps every member positively weighted. Since the original profile is constant on $p$,

$$L^{\eta}_p(s)-L^{\eta}_p(t)=\eta.$$

The perturbed profile is not extensional. Equation (1), strict propriety, and positivity of the prior show that conditionalization is strictly beaten at this active report. ∎

The proof is an application of Meehan and Zhang's Facts 11–12, not an independent replacement for them. Their fact about a point mass on one learning function becomes a statement about arbitrarily small movements from any extensional mixture. Geometrically, if an extensional benchmark includes an opaque function, the extensional weightings have empty interior in the simplex of unrestricted weights on that family. There may be uncountably many of them; there is still a direction of arbitrarily small departure that changes the optimizer.

Nor is the broader contrast between CAR and robustness new. Jaeger's procedural analysis makes the choice of allowable perturbations central. Gill and Grünwald defend a different kind of procedural stability by allowing uniform sampling from multicovers. Proposition 1 concerns a specifically stated parameterization: independent changes in the weights of deterministic learning functions. It does not establish instability under every natural parameterization.

For example, a procedure can require certain cases to be reweighted together. Such constraints may preserve extensionality even when every deterministic case is opaque. A family built into the benchmark by symmetry can remain balanced under every *symmetry-preserving* perturbation. The theorem does not refute that design. It identifies the constraint whose justification the design needs.

There is a modest impossibility consequence. No single globally evidentially constant rule can be exactly optimal throughout a neighborhood of an extensional, positively weighted benchmark containing opacity. At the original benchmark, the rule must equal $b_p$ at every active report. The perturbation just constructed requires a different posterior at one of those same reports. Changing the candidate rule does not remove this instability.

This consequence bears directly on the ambition to identify a rule that is best in general. If “in general” permits arbitrary nearby changes in which opaque situations count more, exact optimality is unavailable. If it permits only balanced changes, the balance is part of the normative proposal. The needed defense concerns allowable comparisons between learning situations, not merely the followability of the rule.

## 4. A small loss can accompany a changed verdict

An exact maximization theorem is sensitive to any strict improvement, however small. That sensitivity can make the preceding result sound more destructive than it is. To measure the loss, use the quadratic score on atomic states:

$$A(q,s)=-\sum_{t\in S}(q(t)-\mathbf 1_{t=s})^2.$$

This convention fixes the scale of the numerical claims below. It is a strictly proper score. Define the regret of Bayesian updating at the benchmark as the difference between the best attainable total score and the score of Bayesian updating.

**Proposition 2.** Its exact regret is

$$\mathcal R_\lambda(b)=\sum_{p:Z_p>0}Z_p\,\lVert r_p-b_p\rVert_2^2.\qquad\text{(2)}$$

*Proof.* For any distribution $r$, expanding the quadratic score gives

$$\mathbb E_r A(r,s)-\mathbb E_r A(q,s)=\lVert r-q\rVert_2^2.$$

The contribution of report $p$ to the benchmark is $Z_p\mathbb E_{r_p}A(f(p),s)$. Apply this identity with $q=b_p$ and sum. ∎

The quadratic-score identity is standard algebra. Its use here quantifies the exact extensionality characterization: asymmetries change the selected posterior, while their accuracy cost is weighted by how much the report contributes to the benchmark.

For a two-state illustration, let $S=\{a,b\}$ with equal prior probabilities. There are four factive learning functions, obtained by independently choosing $\{a\}$ or $S$ at $a$, and $\{b\}$ or $S$ at $b$. Let $\lambda_0$ be uniform over them. Every true report has profile $1/2$.

Increase the relative weight of the opaque function $E^*(a)=S$, $E^*(b)=\{b\}$ using the mixture in Proposition 1. Then

$$L_S(a)=\frac{1+\eta}{2},\qquad L_S(b)=\frac{1-\eta}{2},\qquad Z_S=\frac12.$$

The optimal posterior on learning $S$ is $((1+\eta)/2,(1-\eta)/2)$ rather than the unchanged prior. Singleton reports still require certainty in their sole state. Hence

$$\mathcal R_{\lambda_\eta}(b)=\frac{\eta^2}{4}.$$

At $\eta=0.01$, Bayesian updating is no longer optimal, but its total score falls short by only $0.000025$. The verdict has changed at first order in the weighting perturbation; the loss is second order. Describing this result only as a failure of robustness would conceal what remains stable.

A general bound makes the qualification precise. Let an extensional baseline have positive constants $c_p$ on all reports under consideration. Suppose the perturbed normalized profile can be written

$$L_p(s)=c_p(1+\delta_p(s)),\qquad |\delta_p(s)|\le\varepsilon<1\quad(s\in p).$$

The bound is relative to the baseline profile of *each report*, not merely to the total mass of the perturbation.

**Proposition 3.** Under this condition,

$$\mathcal R_\lambda(b)\le\frac{\varepsilon^2}{(1-\varepsilon)^2}.$$

*Proof.* Set $\bar\delta_p=\sum_s b_p(s)\delta_p(s)$. Equation (1) gives

$$r_p(s)-b_p(s)=b_p(s)\frac{\delta_p(s)-\bar\delta_p}{1+\bar\delta_p}.$$

The mean absolute deviation of a variable in $[-\varepsilon,\varepsilon]$ is at most its standard deviation, which is at most $\varepsilon$. Therefore

$$\lVert r_p-b_p\rVert_2\le\lVert r_p-b_p\rVert_1\le\frac{\varepsilon}{1-\varepsilon}.$$

Finally, $\sum_pZ_p=1$ because the weights are normalized and every learning function gives exactly one report at each state. Apply (2). ∎

For a fixed finite baseline with every report active, any sufficiently small fixed-direction perturbation has regret of order at most the square of its size. The constant need not be uniform across baselines. A tiny absolute change can be large relative to a report that originally received almost no weight. It can then produce a large posterior shift at that report. Nor does the quadratic bound establish the same rate for every strictly proper score, especially near boundaries where a score can be unbounded.

The distinction supports a qualified defense of Bayesian practice: modest uncertainty about an approximately extensional benchmark need not make Bayesian updating substantially inaccurate. It does not by itself vindicate a rule that defines rationality as *exact* maximization. Replacing exact optimality with acceptable regret is a change in the normative standard, and should be defended as such.

## 5. What neutrality does and does not supply

An appealing response is that a benchmark intended to apply generally should be neutral among states. If the weights are invariant under every permutation of a fixed state space, extensionality follows. To compare $L_p(s)$ and $L_p(t)$ for $s,t\in p$, swap $s$ and $t$, leaving $p$ setwise fixed. This permutation pairs the learning functions counted in one profile with those counted in the other, preserving their weights.

That is a sufficient argument for extensionality, but its premise is stronger than invariance under mere relabeling. A prior can distinguish the states. A weighting scheme can respond to those distinctions while remaining unchanged in substance when both the state names and the prior are renamed together.

Here is an explicit example. For each nonempty proposition $p$, put $h_\pi(p)=\pi(p)$, and assign unnormalized weight

$$\lambda_\pi(E)\propto\prod_{s\in S}h_\pi(E(s))$$

over all factive learning functions. The prescription is equivariant under every simultaneous permutation of states, propositions, and the prior. It never favors the name “$a$” over the name “$b$.” Nonetheless, the resulting profile need not be extensional.

At state $s$, define $H(s)=\sum_{p\ni s}\pi(p)$. Each state belongs to $2^{n-1}$ subsets, and each distinct pair belongs to $2^{n-2}$ subsets, where $n=|S|\ge2$. Consequently

$$H(s)=2^{n-2}(1+\pi(s)).$$

Since the product weights normalize independently at each state,

$$L_p(s)=\frac{\pi(p)}{H(s)}\quad(s\in p).$$

Equation (1) therefore selects the posterior proportional to $\pi(s)/(1+\pi(s))$ on $p$, rather than the ordinary conditional posterior. With prior $(4/5,1/5)$ on two states, learning $S$ leads to $(8/11,3/11)$.

I do not recommend this benchmark as a measure of epistemic importance. Its role is to separate two neutrality claims. Renaming invariance forbids dependence on arbitrary labels. It does not forbid dependence on the prior or on other substantively represented features. A defense of extensionality from symmetry must specify which of those features the evaluator is entitled to ignore. Otherwise the normative work has been concealed in the stronger symmetry premise.

Nor can one replace extensionality by the weaker demand that learning a tautology leave the prior unchanged. That demand imposes constancy only on $L_S$. For example, take an extensional baseline on $\{a,b,c\}$ and add a little weight to the function

$$E(a)=\{a\},\qquad E(b)=\{a,b\},\qquad E(c)=\{c\}.$$

This function never reports $S$, so the perturbed $L_S$ remains constant. But its report $\{a,b\}$ is delivered only at $b$, and its profile is no longer constant on that proposition. Retaining the prior on receiving no new propositional content does not protect the Bayesian response to every other report.

## 6. The normative choice

A defender of total accuracy has a strong reply: arbitrary redistributions are not normatively permissible. If extensionality is a constraint on epistemic importance, reweighting one opaque situation without compensating elsewhere may be as inappropriate as changing a proper score into an improper one. On that view the absence of an open neighborhood in an unconstrained parameter space is irrelevant.

The reply succeeds against the claim that mathematical fragility alone refutes the proposal. It does not remove the need to explain why the normative space has those constraints. Meehan and Zhang already place the dispute here. Proposition 1 sharpens the alternatives: admitting opaque constituent situations while demanding local exactness requires restrictions on how their weights may vary together. Transparency need not hold case by case, but compensating structure must hold at the aggregate level.

The converse objection is that such compensation is simply disguised evidence internalism. That goes too far. Extensional aggregate profiles can be generated entirely from opaque learning functions. The relevant restriction is on the evaluator's weighting, not on what agents can know about their evidence. Treating these two restrictions as identical would erase the point of aggregation.

State-dependent epistemic importance is another genuine alternative. An evaluator might judge an accurate response to a proposition more important at one of its states than at another. The learning-profile representation then resembles a reporting likelihood, but that resemblance does not discredit the value judgment. What follows is narrower: such a judgment can change which globally evidentially constant rule maximizes the total. The value premise must be assessed directly.

There are therefore three different projects. One can defend extensionality as an exact normative constraint and recover conditionalization exactly. One can allow a neighborhood of approximately extensional benchmarks and defend conditionalization as having small regret. Or one can adopt substantively asymmetric weights and accept a different optimum. The second project has a useful mathematical guarantee under the quadratic score; the first requires a justification the guarantee cannot supply; the third cannot be dismissed merely by calling its profiles likelihoods.

The contribution of total accuracy is clearer when these projects are kept apart. It demonstrates how Bayesian updating can be optimal across opaque situations without being optimal in each. The robustness analysis shows what that achievement depends on and what survives its perturbation. Exactness requires protected balance. Near-optimal accuracy can survive a small loss of balance. Neither conclusion is captured by declaring that Bayes either is or is not robust.

## References

Gill, Richard D., and Peter D. Grünwald. 2008. “An Algorithmic and a Geometric Characterization of Coarsening at Random.” *The Annals of Statistics* 36: 2409–2422. https://doi.org/10.1214/07-AOS532.

Grünwald, Peter D., and Joseph Y. Halpern. 2003. “Updating Probabilities.” *Journal of Artificial Intelligence Research* 19: 243–278. https://doi.org/10.1613/jair.1164.

Jaeger, Manfred. 2005. “Ignorability in Statistical and Probabilistic Inference.” *Journal of Artificial Intelligence Research* 24: 889–917. https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume24/jaeger05a.pdf.

Meehan, Alexander, and Snow Zhang. 2025. “Bayes Is Back.” *The Philosophical Review* 134: 285–350. https://doi.org/10.1215/00318108-11873775.

