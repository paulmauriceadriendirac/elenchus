# What Counts as the Same Evidence?

Extensionality and the Limits of Representation-Neutral Updating

**Abstract.** When may an accuracy benchmark be transferred between descriptions of a learning problem? I connect this question to extensionality, the condition under which weighted total accuracy favors Bayesian conditionalization. Normalized benchmark weights induce factive reporting kernels, and extensionality becomes coarsening at random. I show that an extensional benchmark remains extensional under every identification of states only if it tests complete disclosure or complete non-disclosure. Such a benchmark cannot discriminate between rules on genuinely partial evidence. This does not contradict fixed-space accuracy results: compressing reports can change the evidence. The constructive question is therefore which transformations preserve the relevant learning task. I give an exact criterion for a specified compression, including a prior-independent version that allows more than preservation of the report algebra. The philosophical conclusion is that transferring an accuracy justification requires a separate account of evidential equivalence. Neither truth-preserving translation nor the objectivity of a benchmark supplies that account by itself.

## 1. The missing premise in transferring a justification

An argument that a learning rule performs best must specify what counts as a learning problem. It must also specify when two descriptions concern the same problem. These questions are related, but an answer to the first does not automatically answer the second. A rule can perform optimally against every problem in one benchmark while failing against the images of those problems in a simpler description.

The issue matters for accuracy-first epistemology. Meehan and Zhang (2025, §§5.1–5.3) assess updating rules by their total accuracy over learning situations associated with a fixed prior space. Their Fact 11 identifies a condition, extensionality, necessary and sufficient for Bayesian conditionalization to maximize weighted total accuracy. Their proposal explicitly fixes a state space; it does not assume that all changes of description are harmless. My objection therefore concerns a possible extension of the justification, not a missing qualification in their theorem.

The extension is tempting. If the importance of an accurate response depends only on whether the learned proposition is true, perhaps that restriction expresses a description-independent epistemic norm. On this reading, the same justified benchmark should remain justified when we ask a coarser question about the same underlying experiment. I show that extensionality cannot generally carry that burden. It is relative not only to propositional truth but also to how observations are represented.

There is a practical philosophical choice here. We can reconstruct a fresh extensional benchmark at each grain, retaining conditionalization but changing the evaluated experiment. We can transport the original experiment, retaining its observational structure but sometimes losing extensionality. Or we can demand extensionality under every compression, thereby eliminating the partial reports needed to assess most updating behavior. None of these choices is formally inconsistent. They support different explanations of rationality.

My positive proposal is to require an explicit certificate before transferring an accuracy justification. The certificate concerns the probability, or normalized evaluative weight, of the *translated observation*, not merely the truth of its translated content. I derive its exact finite form below. It identifies when simpler descriptions preserve the relevant license to condition on content alone and when they do not.

The philosophical stake is thus evidential equivalence. We routinely simplify hypotheses while keeping an observation fixed. Here both hypotheses and observations are simplified. A truth-preserving map guarantees that the new report says nothing false; it does not guarantee that receiving it bears the same relation to the new hypotheses. Confusing those guarantees creates an unwarranted transfer of epistemic authority.

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

These facts are established background. Grünwald and Halpern (2003, §§1–3 and Theorem 3.1) distinguish conditioning on the observation event from conditioning on its propositional content, and characterize their agreement. Gill and Grünwald (2008) study the geometry and procedural generation of finite CAR mechanisms. The present essay concerns an additional operation: identifying states and simultaneously replacing each report by its image under that identification.

A surjection $\rho:S\to T$ represents such an identification. The coarse state is $\rho(s)$, and the coarse report is

$$\rho(P)=\{\rho(s):s\in P\}.$$

The coarse report is still true. Indeed, it is the strongest proposition expressible in the coarse vocabulary that the fine report entails: any coarse set whose preimage contains $P$ must contain $\rho(P)$. But different fine reports may have the same image. A proper subset of $S$ can even have image $T$: it may include at least one representative of every coarse category. Receiving the coarse report $T$ is therefore compatible with having received a fine report that excluded some fine states.

Two questions must be distinguished. Can we choose a structure-free family of mechanisms whose distributions commute with every such map? And, given a particular CAR mechanism and prior, can its induced coarse mechanisms all remain CAR? They concern different assumptions, but have closely related answers.

## 3. From evaluative weights to reporting kernels

Here is the precise connection to an accuracy benchmark. A deterministic learning situation is a function $E$ assigning each state $s$ a proposition $E(s)$ containing it. Let $\lambda(E)\geq0$ be its evaluative weight, with positive total $\Lambda=\sum_E\lambda(E)$. Define

$$\lambda_P(s)=\sum_{E:E(s)=P}\lambda(E),\qquad
K_\lambda(P\mid s)=\frac{\lambda_P(s)}{\Lambda}.$$

Each situation supplies exactly one report at each state. Consequently $\sum_{P\ni s}\lambda_P(s)=\Lambda$, independently of $s$, so $K_\lambda$ is a factive kernel. Extensionality says that $\lambda_P(s)$ is constant across states where $P$ is true. Factivity already makes it zero elsewhere. Thus extensionality is exactly CAR for the normalized kernel.

This is a mathematical representation, not an identification of normative importance with an agent's subjective probabilities. A benchmark can use weights for objective evaluation without asserting that a source actually randomizes according to them. Normalization nonetheless allows us to ask precisely how those evaluative weights transform when states and reports are compressed.

Conversely, every factive kernel has a weighting representation. Set $\lambda(E)=\prod_{s\in S}K(E(s)\mid s)$. Summing over all factive functions gives total weight one, and summing over functions with $E(s)=P$ recovers $K(P\mid s)$. This construction need not describe the mechanism's actual counterfactual dependence across states. Only the statewise report probabilities enter expected accuracy.

For a content-based rule $f$, use an inaccuracy loss $\ell$ and write its normalized benchmark value as

$$B_K(f)=\sum_s\pi(s)\sum_{P\ni s}K(P\mid s)\ell(f(P),s).$$

Rearranging the sums shows that each positive-weight report is evaluated using the distribution proportional to $\pi(s)K(P\mid s)$. Strict propriety selects that distribution uniquely. It selects $\pi(\cdot\mid P)$ exactly when the report likelihood is constant on $P$. This is the substance of Meehan and Zhang's Fact 11 and Lemmas 1–2, expressed in the language of observation mechanisms. The underlying criterion for ignoring the observation mechanism is established CAR theory, not a new accuracy theorem.

Equal weights on all deterministic situations induce the uniform-subset kernel. At a fixed state, choosing its report leaves the same number of choices at all other states, whatever true report was chosen. Every one of the $2^{|S|-1}$ true reports therefore receives probability $2^{-(|S|-1)}$. The three-state example below consequently represents the unweighted benchmark itself, rather than an unrelated reporting device.

The transport question is now well defined. Push the joint measure $\pi(s)K(P\mid s)$ forward to $(\rho(s),\rho(P))$, then condition on the coarse state. This preserves the evaluated experiment while changing its vocabulary. It need not reproduce the benchmark constructed afresh on the smaller space. Nor does it compare numerical losses across different agendas: all optimization after transport uses a proper score on the coarse space. The issue is which coarse posterior that optimization selects.

## 4. A classification of unrestricted neutrality

For finite nonempty sets $S$, considered up to isomorphism, and each actual state $s\in S$, suppose we choose a random subset $P_{S,s}$ containing $s$. No prior, metric, observation algebra, or other structure is supplied. Impose the following compatibility requirement:

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

Only maps onto two-point targets, together with their renamings, were needed. The same $\theta$ is forced across cardinalities, not merely within each space. Requiring compatibility at each fine state is equivalent to requiring it after averaging within fibers for every regular prior: an average constant for every positive choice of weights must have identical components.

The result is stronger than the familiar observation that uniformity depends on how possibilities are counted. It classifies *all* families satisfying the stated requirement, including nonuniform ones. The proof nevertheless explains the underlying pressure simply: whether the report contains one alternative must have the same probability as whether it contains either of two alternatives. That is possible only if the alternatives always appear together.

Consider the otherwise natural rule that, at $s$, chooses uniformly among all subsets containing $s$. Each nonactual state is independently included with probability $1/2$. Split one coarse alternative into $m$ fine alternatives. The projected report includes that coarse alternative with probability $1-2^{-m}$, although generating directly on the coarse two-state space includes it with probability $1/2$. Uniformity at each level does not give compatibility between levels.

Equation (2) has a further consequence for benchmarks of learning accuracy. On spaces with at least three states, no proper nonsingleton report occurs. Such a benchmark can evaluate how the learner responds to conclusive evidence and to the whole space, but cannot distinguish rules that differ only on genuinely partial evidence. Strictly proper scoring can determine the best responses to reports that occur; it cannot determine responses to reports assigned probability zero.

This does not refute an accuracy argument formulated on a fixed state space. It blocks one ambitious explanation of why its benchmark needs no representational choices. The choice of description cannot be removed by imposing universal compatibility while retaining positive evaluation weight for every kind of partial report.

## 5. When CAR survives every coarsening

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

For two states the classification is automatic because no proper nonsingleton exists. For larger spaces, its geometric content is that the preserved CAR mechanisms form exactly the line segment between complete revelation and complete non-disclosure inside the fixed-space CAR polytope studied by Gill and Grünwald (2008).

No special choice of prior is needed. Any regular prior makes all the brackets for proper reports strictly positive. Nor must we check every partition: the partitions separating one state from all the others already suffice.

In benchmark language, Proposition 2 says that a normalized extensional weighting transports to extensional weightings under all singleton-separating compressions exactly when its support contains no partial reports. Any content-based rule agreeing with conditionalization on singletons and the whole space then has identical benchmark performance. For at least three states, infinitely many rules differing on partial evidence remain tied. The loss of discrimination is mathematical, not just a complaint that the benchmark seems unrealistic.

The same calculation gives a quantitative version. Let $\mu=\min_{s\in S}\pi(s)>0$, and suppose that $A_j-B_j\le\varepsilon$ for each tested state $j$. Thus the likelihood imbalance of the whole report after each singleton-separating coarsening is at most $\varepsilon$.

**Proposition 3.** At any actual state $s$ for which that inequality holds, the probability $r_s$ of issuing a proper nonsingleton report satisfies

$$r_s\le\min\left\{1,\frac{\varepsilon(1-\pi(s))}{\mu}\right\}.$$

*Proof.* For every proper $P$ containing $s$, the bracket in (3) equals $\pi(S\setminus P)/(1-\pi(s))$ and is at least $\mu/(1-\pi(s))$. The sum of its coefficients over proper nonsingletons containing $s$ is exactly $r_s$. Therefore $\varepsilon\ge A_s-B_s\ge\mu r_s/(1-\pi(s))$. The additional bound $r_s\le1$ is automatic. ∎

For a uniform prior on $n$ states the bound is $(n-1)\varepsilon$, capped at one. Approximate preservation therefore makes partial reports rare when the imbalance is small relative to the granularity of the prior. There is no useful uniform conclusion from small absolute imbalance alone if arbitrarily tiny prior atoms are allowed. Exact impossibility and approximate restriction should not be confused.

Proposition 2 does not follow simply by asserting that all changes of representation preserve information. They do not. Its point is to measure the restrictiveness of a preservation demand that someone might nevertheless impose. Partial CAR reports are exactly what must disappear if CAR is required to survive every such compression.

## 6. A tautology with a likelihood

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

## 7. An exact test for a permissible compression

The strongest objection to universal compatibility is correct: lossy compression need not preserve the learning problem. The useful response is to characterize permissible transformations, rather than insist that every surjection be permissible. Fix a CAR mechanism and a particular map $\rho:S\to T$. For each nonempty coarse report $Q$, define

$$g_Q(s)=\sum_{P:\rho(P)=Q}K(P\mid s)
=\sum_{\substack{P\ni s\\\rho(P)=Q}}c_P.$$

This is the chance of receiving some fine report that translates to $Q$. Write $F_t=\rho^{-1}(\{t\})$. The induced likelihood is

$$\bar K_\pi(Q\mid t)=
\frac{\sum_{s\in F_t}\pi(s)g_Q(s)}{\pi(F_t)}.$$

For a fixed prior, CAR survives exactly when these fiber averages are equal for all $t\in Q$, separately for each $Q$. This is a direct test, including cases in which several fine reports have the same coarse image. It does not require reconstructing a distribution over deterministic situations.

**Proposition 4.** CAR survives a fixed compression for every regular prior if and only if, for every coarse report $Q$ containing at least two coarse states, $g_Q$ is constant on $\rho^{-1}(Q)$.

*Proof.* Constancy immediately makes all the displayed averages equal. Conversely, suppose they are equal for every regular prior. Fix $t\in Q$ and another $u\in Q$. Vary the conditional prior within $F_t$ while keeping the conditional prior within $F_u$ fixed. Equality forces every positive weighted average of $g_Q$ on $F_t$ to have the same value, hence $g_Q$ is constant there. Repeating across fibers gives the same constant throughout $\rho^{-1}(Q)$. Singleton coarse reports impose no comparison between different coarse states and require no condition. ∎

One familiar sufficient condition is that every positive-probability report be saturated: a union of entire fibers. Each then equals $\rho^{-1}(Q)$ for its image. Its likelihood is constant throughout that preimage, so the test succeeds. But saturation is not necessary, even for mechanisms with only partial fine reports.

For example, let $S=\{a_1,a_2,b_1,b_2\}$ and merge the two $a$ states into $A$ and the two $b$ states into $B$. Give each cross-pair $\{a_i,b_j\}$ coefficient $1/2$, and every other report coefficient zero. Each state lies in exactly two cross-pairs, so row probabilities sum to one and the fine mechanism is CAR. None of its reports is saturated. Yet every report becomes $\{A,B\}$, issued with probability one at every state. The induced mechanism is CAR for every prior. What matters is the balance of the aggregate translated report, not preservation of each individual report.

This positive test has a useful negative companion. If we specify only the map and demand that it preserve CAR for *every* CAR mechanism and every regular prior, the only admissible maps are bijections and maps to a one-state space. To see why, take a noninjective, nonconstant map and distinct $x,x'$ in one fiber. Use the deterministic partition mechanism with cells $\{x'\}$ and $S\setminus\{x'\}$. The second cell maps onto all of $T$. At any other coarse state its report has probability one. At the fiber containing $x'$ its probability is strictly below one. Hence CAR fails. The converse for bijections and constant maps is immediate.

Therefore no nontrivial compression can receive a universal certificate from its set-theoretic shape alone. A defense must mention the particular experiment, the relevant prior, or restrictions on permissible observations. Proposition 4 states exactly what such a defense must establish when it claims independence from the prior.

## 8. Even transparent evidence can lose transparency

The preceding witness deserves philosophical attention. Start with three states $a,b,c$ and a perfectly transparent partition experiment: its reports are $\{a\}$ at $a$ and $\{b,c\}$ at either $b$ or $c$. An agent who receives a report thereby knows which cell was reported. Face-value conditioning is licensed without any balancing across opaque situations.

Now merge $a,b$ into $A$ and leave $c$ as $C$. The report at $a$ becomes $\{A\}$; the reports at $b,c$ become $\{A,C\}$. Conditional on $C$, the whole report occurs certainly. Conditional on $A$, it occurs with probability $\pi(b)/(\pi(a)+\pi(b))$, strictly less than one. Even a transparent fine experiment thus produces a non-CAR coarse experiment.

This example also distinguishes the result from existing robustness classifications. Jaeger (2005, Theorem 4.17) connects robustness of a specified procedural model to coarsening completely at random, or CCAR. CCAR mechanisms arise by selecting a partition independently of the state and reporting its actual cell. Gill and Grünwald (2008) explain the contrast with general CAR. Stability under the state-and-report compressions studied here is stricter: a single fixed partition is already CCAR, yet the example violates stability. The two notions vary different features of a model.

Grünwald and Halpern (2003, Proposition 4.1) establish another nearby universal restriction: their CAR condition holds for all distributions on the relevant runs exactly when the possible observations are pairwise disjoint. That varies distributions while fixing an observation vocabulary. Here we fix a CAR kernel and prior and vary the identification of states and reports. None of these robustness results can be substituted for another merely because each restricts CAR.

Nor should the example be inflated into a claim that genuine evidence externalism is an artifact of coarse modeling. A deterministic fine partition can look stochastic when fine states are hidden. This shows that *apparent* opacity can have a representational source. It does not show that every externalist evidence relation has a transparent refinement preserving what an agent actually learns. Adding facts to a model and adding those facts to the agent's evidence are different operations.

The example instead places a burden on appeals to a privileged fine grain. A privileged space must be justified by the theory's conception of total evidence, not selected merely because a desired transparency or CAR property holds there. Otherwise the preferred updating rule helps determine the evidential representation that is then used to justify that rule. The circularity is avoidable, but avoiding it requires independent epistemology of evidence.

## 9. What should an objective benchmark preserve?

The strongest defense of fixed-space evaluation is that objectivity does not require invariance under every change of task. An objective measure of distance can depend on which points are measured. Likewise, an objective accuracy measure can depend on which propositions are in question. That defense is sound. The classification results do not contradict the objectivity of Meehan and Zhang's benchmark merely because it is contextual.

The narrower concern is explanatory portability. Suppose a defender appeals to a fine-space benchmark to justify a learner's response to a coarse report. There are two different claims available. One is that the coarse report is an observation in a new abstract problem, to be evaluated by a freshly constructed benchmark. The other is that it is the compressed observation from the original experiment. Our results show that the corresponding norms can differ even though the two reports have identical coarse propositional content.

Fresh construction is a coherent option. At each grain, choose the uniform-subset kernel, so that conditionalization is optimal there. But the coarse uniform benchmark is generally not the transported fine benchmark. The rule is vindicated twice against different evaluative populations. Its invariance across those independent constructions does not establish that it handles one experiment consistently when its record is compressed. That distinction should appear in the explanation, rather than remain hidden behind a common description of both calculations as evaluating every learning situation.

Transport is also coherent. It keeps the joint weights of actual outcomes and observations, adding weights when descriptions merge. If the resulting kernel is non-CAR, strict propriety recommends likelihood-sensitive updating on the coarse report. A defender can accept this without abandoning Bayesian probability. What must be surrendered is the inference from fine-level extensionality to coarse-level extensionality. The transported benchmark continues to be objective in whatever sense its original weights were objective, but it no longer supports conditioning on translated content alone.

Universal preservation takes a third route. It requires all these transported benchmarks to remain extensional. Proposition 2 then forces the singleton-or-whole form. The price is substantial: on any larger space, the benchmark supplies no reason to choose conditionalization rather than an alternative rule on partial reports. Proper scoring cannot repair absent evaluative coverage. Assigning a unique rational answer to those reports would require a further principle.

The choice among these routes depends on the explanatory purpose. If the purpose is to rank abstract rules relative to each stipulated prior space, fresh construction may suffice. If the purpose is to advise a learner who receives a compressed record of a particular experiment, transport is the relevant operation. Confusing those purposes gives the first justification more reach than it has earned. My preferred restriction is therefore conditional: transfer the face-value justification only where the induced kernel passes the exact test in section 7.

A second defense invokes a maximally fine representation of the agent's evidence. This can settle some cases. If the model retains the entire observation event, ordinary conditioning gives a coherent posterior, and marginalizing that posterior yields coherent answers to coarser questions. But that operation preserves the fine observation while coarsening the target. It is not the operation investigated here, which compresses the observation as well. The privileged-grain reply succeeds by retaining information that the compressed learner no longer has.

There is no objection to doing so when that information belongs to the learner's evidence. There is an objection to doing so silently when the original question concerns learning from the compressed report alone. In an externalist setting, moreover, a fully specified world need not make an agent certain which evidence she possesses. A finer model of her epistemic condition cannot simply be identified with a richer condition. The representational choice must track the intended evidence relation.

This is why I do not endorse the stronger claim that the theorem defeats an externalist accuracy vindication of conditionalization. It establishes a specific limitation on transferring that vindication between descriptions. The limitation is informative because its boundary is exact: we know the surviving universal class and the test for individual transformations. It replaces a vague demand for neutrality with an assessable claim about the relation between two learning tasks.

There is a further objection: perhaps the proposed certificate is too demanding because it must work for every regular prior. A particular learner has only one prior. If that prior makes the fiber averages equal, why insist that equality survive a hypothetical change in her beliefs?

For advising that learner in that experiment, there is no such insistence. The fixed-prior average condition is sufficient and necessary. The stronger version answers a different question: whether the abstraction can be justified without relying on a particular distribution of probability inside its categories. This distinction matters when a benchmark is presented as appropriate to any agent, or when its finer prior is unavailable to the person using the coarse description.

For instance, two observers can share the same coarse prior while assigning different conditional probabilities to states inside one category. They agree on every proposition expressible in the coarse vocabulary before the report. Nevertheless, if $g_Q$ varies inside a fiber, they can disagree on the likelihood of the translated report, and hence on its posterior significance. Their disagreement does not involve the truth conditions of any coarse proposition. It concerns finer assumptions about the observation process.

This creates an identification problem for a norm stated wholly in coarse terms. The coarse prior and report content need not determine whether face-value updating is licensed. One must either retain the relevant finer information, stipulate a coarse kernel independently, or restrict the abstraction so that its likelihoods do not depend on unresolved within-category distributions. Proposition 4 gives the last option its exact form.

A simple version uses the transparent partition from section 8. Hold the coarse prior of $A$ fixed at $2/3$, and vary the division of that mass between $a$ and $b$. The likelihood of the whole report at $A$ changes with $\pi(b)/\pi(A)$, while its likelihood at $C$ remains one. Two agents with the same coarse prior can therefore rationally move by different amounts on receiving exactly the same coarse sentence. No rule taking only those coarse inputs can reproduce both likelihood-sensitive updates.

The point does not depend on assigning epistemic importance to every microscopic distinction. The difference between $a$ and $b$ matters only because the report-selection process uses it. A distinction irrelevant to the target proposition can still be relevant to interpreting evidence about that proposition. Theories that identify an evidentially adequate state space by asking only which conclusions the learner cares about risk overlooking this indirect relevance.

This also clarifies the role of idealization. A model may legitimately suppress details irrelevant to its explanatory purpose. But irrelevance must concern the whole inferential relation, including the production of evidence, rather than just the vocabulary in which the answer is requested. Otherwise the idealization changes the very conditional distribution the norm was meant to assess. The certificate offers a way of checking a specific idealization without pretending to supply a universal metaphysics of relevance.

One might reply that a coarse observer should simply treat the induced kernel as a primitive. That is an excellent solution when the kernel is known. It reinforces, rather than defeats, the diagnosis: the coarse theory then contains observation information beyond the prior and the report's truth conditions. When that primitive is CAR, conditioning on content is justified. When it is not, the posterior must reflect the selection likelihoods.

The certificate does not require a learner to perform a detailed calculation consciously. It specifies a condition on the justification of a rule, not a cognitive procedure each agent must execute. Familiar reliable institutions can supply that justification through the design of their reporting practices. A measurement protocol may guarantee saturation, for example, or guarantee the aggregate balancing expressed by $g_Q$. An evaluator can then rely on the guarantee without enumerating every fine state.

Approximate guarantees demand more caution. Proposition 3 controls how much partial reporting can survive a uniform family of small likelihood imbalances, given a lower bound on fine-state prior mass. It does not provide a universal bound on posterior error after arbitrary low-probability observations. Dividing by a small report probability can amplify modest absolute likelihood differences. A practical certificate of approximate equivalence would therefore need both a discrepancy measure and a restriction preventing that amplification.

That limitation helps identify what the exact theorem accomplishes. It is not a complete methodology for approximate scientific modeling. It isolates one structural obstruction and one exact route around it. Both remain useful even when an application requires further quantitative work. In particular, a theorist cannot replace the exact preservation premise with an unqualified assertion that the descriptions are “close” without specifying what that closeness controls.

The broader philosophical conclusion is accordingly disciplined. Evidence is not exhausted by a sentence's truth conditions when the occurrence of that sentence depends on a selection process. Yet it would be excessive to demand preservation of every detail of that process. What must survive is the relation relevant to the epistemic norm being transferred. The formal results show both why this relation cannot be omitted and how it can sometimes be preserved through substantial loss of detail.

## 10. Evidential equivalence as a substantive constraint

The proposed account separates three questions. Does the translated report remain true? Does it retain all the original observation information? Does it preserve the license to ignore report selection for the particular target question? The first always holds under our image translation. The second generally fails. The third can hold despite the second failing, as the cross-pair example demonstrates. Evidential equivalence for a purpose need not be complete informational identity.

That intermediate possibility is philosophically valuable. Requiring every detail of an experiment to survive would rule out useful abstraction. Requiring only truth would license too much. The likelihood test recognizes abstractions that discard fine distinctions yet retain the specific relation needed for face-value updating. It is consequently an account of when one epistemic justification survives, rather than a complete account of when two bodies of evidence are equivalent in every respect.

Consider a research summary that replaces several fine diagnoses with broader categories. Its sentences may all remain true. It may even preserve every distinction relevant to the conclusion a reader wants. Nonetheless, whether the summary was issued rather than a more specific statement can depend on which fine diagnosis obtained. To justify conditioning on the summary's content alone, one must check the aggregated reporting likelihoods. Good intentions, truthfulness, and an accurate vocabulary do not establish that equality.

This point is familiar in its general form: observation protocols matter. The additional contribution is to identify the maximal universally stable class and a precise alternative to universal stability. The classification shows why an unrestricted demand collapses; the certificate shows how partial evidence can nevertheless remain legitimate under particular abstractions. Together they locate what an account of evidential equivalence must contribute to accuracy-first reasoning.

There is also a division of explanatory labor. Strict propriety explains why a learner should match the relevant conditional distribution once that distribution has been identified. CAR explains when the distribution can be obtained from content without modeling selection. The transport criterion explains when that shortcut survives a change of description. None of these steps substitutes for the others. An argument containing only the first two cannot be transferred to a new observation vocabulary without establishing the third.

These claims concern finite spaces, factive reports, regular priors, and image translation. Other ways of summarizing observations may have different preservation conditions. In particular, an arbitrary linguistic paraphrase need not implement this mathematical operation. Applying the result requires identifying the actual map and the report events it combines.

The lesson is not that every epistemic norm requires a privileged language. A family of descriptions can share a norm where their observational relationships satisfy the relevant preservation condition. Nor is the lesson that objectivity entails a unique finest description. Objective assessment may be purpose-relative. The demand is that the purpose and the preservation claim be explicit enough to test.

A successful accuracy justification should therefore say both what evidence its benchmark represents and which transformations preserve that representation. Extensionality supplies a powerful fixed-space condition. It does not by itself make differently described observations the same evidence. The remaining work belongs to the theory of evidence, even when the calculation of optimal accuracy is complete.

## References

Gill, Richard D., and Peter D. Grünwald. 2008. “An Algorithmic and a Geometric Characterization of Coarsening at Random.” *The Annals of Statistics* 36(5): 2409–2422. https://doi.org/10.1214/07-AOS532. Author version: https://arxiv.org/abs/0811.0683.

Grünwald, Peter D., and Joseph Y. Halpern. 2003. “Updating Probabilities.” *Journal of Artificial Intelligence Research* 19: 243–278. https://doi.org/10.1613/jair.1164. Author version: https://arxiv.org/abs/cs/0306124.

Jaeger, Manfred. 2005. “Ignorability in Statistical and Probabilistic Inference.” *Journal of Artificial Intelligence Research* 24: 889–917. https://doi.org/10.1613/jair.1657.

Meehan, Alexander, and Snow Zhang. 2025. “Bayes Is Back.” *The Philosophical Review* 134(3): 285–350. https://doi.org/10.1215/00318108-11873775.

