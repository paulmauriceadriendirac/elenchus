# What Survives Forgetting Distinctions?

**Abstract.** A true report can be taken at face value when its probability of being issued is constant across the states it includes. This familiar condition, coarsening at random, is sensitive to how both states and reports are represented. I prove two finite classification results. First, a family of random true reports that commutes with every surjective identification of states, without using any additional structure, must either identify the actual state completely or report the whole state space. Second, a coarsening-at-random reporting process remains coarsening at random under every identification of states only if it has that same all-or-nothing form. A three-state example shows how a report that becomes tautological after compression can still be informative. These results do not establish a failure of Bayesian reasoning: compressing reports can discard distinctions relevant to their likelihoods. They instead locate a limit on representation-neutral justifications of learning rules. A benchmark that evaluates genuinely partial learning must specify a level of description or restrict the transformations under which it claims neutrality.

## 1. When a simpler description changes the question

Suppose a device reports a set of possibilities containing the actual state. It might identify the state exactly, rule out some alternatives, or merely say that something in the state space occurred. We would like to know when a learner may condition on the reported set without separately modeling how the device chose it.

There is a familiar answer: the report must be equally likely at every state it includes. If the report is twice as likely in one of its member states as in another, merely deleting the excluded states misses relevant information. The likelihood of receiving the report must also enter the update.

Now imagine simplifying the description. Two states that the device distinguishes are placed in one category. Its reports are translated into sets of categories: a category appears whenever at least one of its member states appeared in the original report. Does a reporting process that was safe to ignore before this simplification remain safe to ignore afterward?

Not in general. Indeed, requiring that it remain safe under *every* such simplification leaves only a narrow class of processes. They can reveal everything or reveal nothing. They cannot issue a genuinely partial report with positive probability.

This observation bears on accuracy arguments that evaluate learning rules across an unrestricted collection of possible learning problems. Even if all problems are treated symmetrically within a chosen representation, changing the representation can change the benchmark. One response is to demand compatibility across every refinement and coarsening. The results below show why that response is expensive: an especially strong form of compatibility eliminates the intermediate cases that a general theory of learning needs to evaluate.

The claim is deliberately conditional. Not every merging of states should count as a harmless redescription. An observation can distinguish two microscopic outcomes even when the question we ultimately care about does not. The point is to characterize what an unrestricted neutrality demand actually permits, and then identify a more defensible restricted demand.

## 2. Reports, mechanisms, and face-value updating

Let $S$ be a finite nonempty state space. A reporting mechanism is a kernel $K(P\mid s)$ giving the probability of report $P\subseteq S$ when $s$ is actual. Reports are factive:

$$K(P\mid s)=0\quad\text{if }s\notin P,\qquad
\sum_{P\ni s}K(P\mid s)=1.$$

Let $\pi$ be a regular prior, meaning that $\pi(s)>0$ for every state. If report $P$ has positive probability, conditioning on the event of its being issued gives

$$\Pr(s\mid\text{report }P)
=\frac{\pi(s)K(P\mid s)}{\sum_{t\in P}\pi(t)K(P\mid t)}.$$

This equals ordinary conditioning on the proposition $s\in P$ exactly when $K(P\mid s)$ is constant over $s\in P$. When this holds for every report, the mechanism is **coarsening at random**, or CAR. We can then write

$$K(P\mid s)=c_P\quad(s\in P),\qquad
\sum_{P\ni s}c_P=1.\qquad\text{(1)}$$

These facts are established background. Grünwald and Halpern (2003, Theorem 3.1) formulate the distinction between conditioning in a space that represents the observation process and conditioning on the reported proposition alone. Gill and Grünwald (2008) study the geometry and procedural generation of finite CAR mechanisms. The present essay concerns an additional operation: identifying states and simultaneously replacing each report by its image under that identification.

A surjection $\rho:S\to T$ represents such an identification. The coarse state is $\rho(s)$, and the coarse report is

$$\rho(P)=\{\rho(s):s\in P\}.$$

The coarse report is still true. But different fine reports may have the same image. A proper subset of $S$ can even have image $T$: it may include at least one representative of every coarse category. Receiving the coarse report $T$ is therefore compatible with having received a fine report that excluded some fine states.

Two questions must be distinguished. Can we choose a structure-free family of mechanisms whose distributions commute with every such map? And, given a particular CAR mechanism and prior, can its induced coarse mechanisms all remain CAR? They concern different assumptions, but have closely related answers.

## 3. A classification of unrestricted neutrality

For each finite nonempty $S$ and each actual state $s\in S$, suppose we choose a random subset $P_{S,s}$ containing $s$. No prior, metric, observation algebra, or other structure is supplied. Impose the following compatibility requirement:

**Universal compatibility.** For every surjection $\rho:S\to T$ and every $s\in S$, the random set $\rho(P_{S,s})$ has the same distribution as $P_{T,\rho(s)}$.

This includes invariance under renaming states, since bijections are surjections. But it is substantially stronger. It also requires that generating a report and then merging categories be distributionally equivalent to first merging the categories and generating a report directly in the smaller space.

**Proposition 1.** A family satisfies universal compatibility if and only if there is one number $\theta\in[0,1]$ such that, on every space with at least two states,

$$P_{S,s}=\begin{cases}
\{s\},&\text{with probability }1-\theta,\\
S,&\text{with probability }\theta.
\end{cases}\qquad\text{(2)}$$

On a one-state space these outcomes coincide.

*Proof.* On a two-state space, a true report is either the actual singleton or the whole space. Invariance under bijections makes the probability $\theta$ of the latter independent of the labels and of which state is actual.

Fix a larger $S$, an actual $s$, and a different state $i$. Merge all states except $i$ into one category. The coarse report is the whole two-state space exactly when the fine report contains $i$. Universal compatibility therefore gives

$$\Pr(i\in P_{S,s})=\theta.$$

For distinct $i,j\ne s$, instead merge $\{i,j\}$ into one category and all remaining states into the other. The coarse report is whole exactly when at least one of $i,j$ is in the fine report. Hence

$$\Pr(i\in P_{S,s}\text{ or }j\in P_{S,s})=\theta.$$

Since both individual inclusion probabilities are also $\theta$, the inclusion indicators of $i$ and $j$ agree with probability one. Every nonactual state is consequently included together or excluded together. Factivity includes $s$ in either case, giving (2). The two-state case already has that form. Conversely, the image of an actual singleton is an actual singleton and the image of the whole space under a surjection is the whole target. Thus every family in (2) is compatible. ∎

The result is stronger than the familiar observation that uniformity depends on how possibilities are counted. It classifies *all* families satisfying the stated requirement, including nonuniform ones. The proof nevertheless explains the underlying pressure simply: whether the report contains one alternative must have the same probability as whether it contains either of two alternatives. That is possible only if the alternatives always appear together.

Consider the otherwise natural rule that, at $s$, chooses uniformly among all subsets containing $s$. Each nonactual state is independently included with probability $1/2$. Split one coarse alternative into $m$ fine alternatives. The projected report includes that coarse alternative with probability $1-2^{-m}$, although generating directly on the coarse two-state space includes it with probability $1/2$. Uniformity at each level does not give compatibility between levels.

Equation (2) has a further consequence for benchmarks of learning accuracy. On spaces with at least three states, no proper nonsingleton report occurs. Such a benchmark can evaluate how the learner responds to conclusive evidence and to the whole space, but cannot distinguish rules that differ only on genuinely partial evidence. Strictly proper scoring can determine the best responses to reports that occur; it cannot determine responses to reports assigned probability zero.

This does not refute an accuracy argument formulated on a fixed state space. It blocks one ambitious explanation of why its benchmark needs no representational choices. The choice of description cannot be removed by imposing universal compatibility while retaining positive evaluation weight for every kind of partial report.

## 4. When CAR survives every coarsening

The first result considered an entire prior-free family. A different route begins with one CAR mechanism and asks only whether its induced coarse mechanisms remain CAR. Here the prior is available and is used correctly when conditioning within a coarse category.

Fix a finite $S$ with at least three states, a regular prior $\pi$, and coefficients $c_P$ satisfying (1). For each $j\in S$, consider the binary partition with categories $\{j\}$ and $S\setminus\{j\}$. Translate every report to its image under this partition. The induced kernel conditions on which coarse category is actual, averaging fine-state probabilities using $\pi$ within that category.

**Proposition 2.** The induced mechanism is CAR under every one of these binary partitions if and only if

$$c_P=0\quad\text{whenever }1<|P|<|S|.$$

Equivalently, the original mechanism reveals the actual singleton with a common probability $1-\theta$ and reports $S$ with probability $\theta$. Such a mechanism remains CAR under every surjective identification of states.

*Proof.* Fix $j$. Conditional on actual state $j$, the probability of reporting both coarse categories is

$$A_j=\sum_{\substack{P\ni j\\|P|\ge2}}c_P.$$

Conditional on the other coarse category being actual, that probability is

$$B_j=\sum_{\substack{P\ni j\\|P|\ge2}}
c_P\frac{\pi(P\setminus\{j\})}{\pi(S\setminus\{j\})}.$$

Indeed, a fine report $P$ that contains $j$ produces the whole coarse report at precisely those other actual states that also belong to $P$. Thus

$$A_j-B_j=\sum_{\substack{P\ni j\\|P|\ge2}}
c_P\left[1-\frac{\pi(P\setminus\{j\})}{\pi(S\setminus\{j\})}\right].\qquad\text{(3)}$$

Every summand is nonnegative. Since the prior is regular, the bracket is strictly positive for every proper $P$ in the sum, and zero for $P=S$. CAR on the coarse binary space requires $A_j=B_j$: its only report containing two states must have the same likelihood at both. Hence every proper nonsingleton $P$ containing $j$ has coefficient zero. Requiring this for every $j$ eliminates all proper nonsingletons. The row sums in (1) then imply $c_{\{s\}}=1-c_S$ for every $s$. Conversely, a singleton-or-whole mechanism has the same form after any surjection and is CAR. ∎

No special choice of prior is needed. Any regular prior makes all the brackets for proper reports strictly positive. Nor must we check every partition: the partitions separating one state from all the others already suffice.

The same calculation gives a quantitative version. Let $\mu=\min_{s\in S}\pi(s)>0$, and suppose that $A_j-B_j\le\varepsilon$ for every $j$. Thus the likelihood imbalance of the whole report after each singleton-separating coarsening is at most $\varepsilon$.

**Proposition 3.** At each actual state $s$, the probability $r_s$ of issuing a proper nonsingleton report satisfies

$$r_s\le\min\left\{1,\frac{\varepsilon(1-\pi(s))}{\mu}\right\}.$$

*Proof.* For every proper $P$ containing $s$, the bracket in (3) equals $\pi(S\setminus P)/(1-\pi(s))$ and is at least $\mu/(1-\pi(s))$. The sum of its coefficients over proper nonsingletons containing $s$ is exactly $r_s$. Therefore $\varepsilon\ge A_s-B_s\ge\mu r_s/(1-\pi(s))$. The additional bound $r_s\le1$ is automatic. ∎

For a uniform prior on $n$ states the bound is $(n-1)\varepsilon$, capped at one. Approximate preservation therefore makes partial reports rare when the imbalance is small relative to the granularity of the prior. There is no useful uniform conclusion from small absolute imbalance alone if arbitrarily tiny prior atoms are allowed. Exact impossibility and approximate restriction should not be confused.

Proposition 2 does not follow simply by asserting that all changes of representation preserve information. They do not. Its point is to measure the restrictiveness of a preservation demand that someone might nevertheless impose. Partial CAR reports are exactly what must disappear if CAR is required to survive every such compression.

## 5. A tautology with a likelihood

Let $S=\{a,b,c\}$ with a uniform prior. At each actual state, choose uniformly among the four reports containing it. Every nonempty report has CAR coefficient $c_P=1/4$. The original mechanism therefore permits face-value conditioning.

Now combine $a$ and $b$ into category $A$, and call the remaining category $C$. Translate each fine report to the set of categories it intersects. If $c$ is actual, the four possible fine reports are

$$\{c\},\quad\{a,c\},\quad\{b,c\},\quad\{a,b,c\}.$$

Three of these become the whole coarse space $\{A,C\}$. Its report probability is $3/4$. If $a$ is actual, only $\{a,c\}$ and $\{a,b,c\}$ become the whole coarse space, giving probability $1/2$. The calculation at $b$ is identical. Therefore

$$\Pr(\text{whole coarse report}\mid C)=\frac34,
\qquad
\Pr(\text{whole coarse report}\mid A)=\frac12.$$

The prior probabilities of $A$ and $C$ are $2/3$ and $1/3$. On receiving the whole coarse report, correct updating gives

$$\Pr(A\mid\text{whole coarse report})
=\frac{(2/3)(1/2)}{(2/3)(1/2)+(1/3)(3/4)}
=\frac47.$$

Conditioning only on its tautological content would instead retain $2/3$. The difference is not a paradox. The sentence reports no exclusion at the coarse level, but the event of being sent that sentence has different probabilities in the two coarse categories.

Nor has compression manufactured information from nothing. The original report was more detailed. The compressed observer knows only that it was one of several reports whose images are whole. That event can still carry information. The calculation respects ordinary conditioning on a less informative observation.

This is why the result should not be advertised as representation dependence of Bayesian probability itself. If one preserves the full observation event and the underlying joint distribution, the Bayesian calculation remains coherent. What fails to survive is a license to *ignore the mechanism* and condition on report content alone. That license is a property of the chosen representation of the observation as well as of the process that produced it.

## 6. The objection from legitimate redescription

The strongest objection is that universal compatibility demands too much. If a fine report can distinguish states within a category, translating it to the set of categories it intersects loses information. Why should a benchmark treat that lossy operation like a harmless renaming?

It should not do so automatically. The theorem is useful precisely because it exposes that distinction. A claim of representation neutrality must say which changes preserve the observation task. Requiring every surjection to do so is untenable for a benchmark meant to represent partial learning. Restricting the transformations is a principled answer, provided the restriction is stated.

There is a simple sufficient restriction. Fix $\rho:S\to T$ and suppose every report with positive CAR coefficient is **saturated**: it is a union of entire fibers of $\rho$. Then each such report is exactly $\rho^{-1}(Q)$ for its image $Q$. For any fine state whose image belongs to $Q$, the probability of issuing that report is the common coefficient $c_{\rho^{-1}(Q)}$. Averaging within a coarse category leaves that coefficient unchanged. The induced coarse mechanism is therefore CAR.

In this case the observations never distinguished the fine states being merged. The translation changes the labels available for describing the task without merging differently informative report tokens. CAR survives because the transformation respects the report algebra.

This repair shows that the alternative is not arbitrary dependence on every feature of a representation. One can demand invariance under bijections, consistency under merges that preserve the observation algebra, and explicit accounting for likelihoods when a transformation discards observational distinctions. Those demands are compatible with rich partial learning.

The prior-free classification also leaves open structure-sensitive families. A mechanism may depend on a probability measure, a topology, a physically specified sensor, or a restricted collection of observable propositions. Proposition 1 does not classify those families. Introducing that structure changes the proposal: neutrality is then relative to transformations preserving it. That is often exactly what a realistic theory should say.

## 7. What the results add to an accuracy argument

Meehan and Zhang (2025) evaluate general updating rules by aggregating accuracy over learning problems. Their results connect Bayesian optimality to the balance of report likelihoods across compatible states. The present issue is orthogonal to optimizing within such a benchmark: how should benchmarks at different levels of description be related?

One answer is to declare a particular finite state space and report vocabulary part of the problem. Nothing here shows that answer to be inconsistent. A second is to justify those choices through the observation process. A third is to require invariance only under transformations preserving that process's relevant structure. Each answer identifies something that unrestricted appeals to “all learning problems” can leave implicit.

The two classification results delimit a fourth, much stronger answer. A prior-free benchmark cannot commute with all state identifications while assigning positive weight to genuinely partial reports. Even a prior-dependent treatment cannot make a fixed partial CAR mechanism remain CAR under every identification. In both cases the universal requirement collapses the allowable observations to complete disclosure or complete non-disclosure.

These are proposed refinements of an established theory of coarse observations, not a discovery of CAR or of the need to model reporting likelihoods. The exact classification claims are proved here; their status as previously unpublished results remains provisional. Their philosophical use does not require presenting them as a replacement for that literature. They make a particular neutrality demand precise enough to assess.

A successful defense of a learning rule need not be independent of every description. It does need to explain which descriptions represent the same learning problem. Forgetting distinctions can be harmless when the evidence never used them. When the evidence did use them, what survives is the ordinary probability calculus, together with a renewed obligation to account for how the surviving report was produced.

## References

Gill, Richard D., and Peter D. Grünwald. 2008. “An Algorithmic and a Geometric Characterization of Coarsening at Random.” *The Annals of Statistics* 36(5): 2409–2422. https://doi.org/10.1214/07-AOS532. Author version: https://arxiv.org/abs/0811.0683.

Grünwald, Peter D., and Joseph Y. Halpern. 2003. “Updating Probabilities.” *Journal of Artificial Intelligence Research* 19: 243–278. https://doi.org/10.1613/jair.1164. Author version: https://arxiv.org/abs/cs/0306124.

Meehan, Alexander, and Snow Zhang. 2025. “Bayes Is Back.” *The Philosophical Review* 134(3): 285–350. https://doi.org/10.1215/00318108-11873775.
