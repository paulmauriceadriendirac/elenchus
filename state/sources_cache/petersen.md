*Produced as part of the* [*SERI ML Alignment Theory Scholars Program*](https://serimats.org/) *\- Summer 2023 Cohort. My thanks to Eric Chen, Elliott Thornley, and John Wentworth for invaluable discussion and comments on earlier drafts. All errors are mine.*

This article presents a few theorems about the invulnerability of agents with incomplete preferences. Elliott Thornley’s ([2023](https://www.alignmentawards.com/winners#background)) proposed approach to the AI shutdown problem relies on these preferential gaps, but [John Wentworth and David Lorell](https://www.alignmentforum.org/posts/bzmLC3J8PsknwRZbr/why-not-subagents) have argued that they make agents play strictly dominated strategies.[^3m1r2zyk7s5] I claim this is false.

Summary
-------

Suppose there exists a formal description of an agent that willingly shuts down when a certain button is pressed. Elliott Thornley’s (2023) Incomplete Preference Proposal aims to offer such a description. It’s plausible that, for it to constitute a promising approach to solving the AI shutdown problem, this description also needs to (i) permit the agent to be broadly capable and (ii) assure us that the agent will remain willing to shut down as time passes. This article formally derives a set of sufficient conditions for an agent with incomplete preferences to satisfy properties relevant to (i) and (ii).

A seemingly relevant condition for an agent to be capably goal-directed is that it avoids sequences of actions that foreseeably leave it worse off.[^tinxlqvh5gl] I will say that an agent satisfying this condition is *invulnerable*. This is related to two intuitive conditions. The weaker one is *unexploitability*: that the agent cannot be forcibly money pumped (i.e., compelled by its preferences to sure loss). The stronger condition is *opportunism*: that the agent never accepts sure losses or foregoes sure gains.[^j21kg28mi9h]

To achieve this, I propose a dynamic choice rule for agents with incomplete preferences. This rule, *Dynamic Strong Maximality* (DSM), requires that the agent consider the available plans that are acceptable at the time of choosing and, among these, pick any plan that wasn’t previously strictly dominated by any other such plan. I prove in section 2 that DSM-based backward induction is sufficient for invulnerability, even under uncertainty.

Having shown that incompleteness does not imply that agents will pursue dominated strategies, I consider the issue of whether DSM leads agents to act as if their preferences were complete. Section 3 begins with a conceptual argument suggesting that DSM-based choice under uncertainty will not, even behaviourally, effectively alter the agent’s preferences over time. This argument does not apply when the agent is unaware of the structure of its decision tree, so I provide some formal results for these cases which bound the extent to which preferences can de facto be completed.

These results show that there will always be sets of options with respect to which the agent never completes its preferences. This holds no matter how many choices it faces. In particular, if no new options appear in the decision tree, then no amount of completion will occur; and if new options do appear, the amount of completion is permanently bounded above by the number of mutually incomparable options. These results apply naturally to cases in which agents are unaware of the state space, but readers sceptical of the earlier conceptual argument can re-purpose them to make analogous claims in standard cases of certainty and uncertainty. Therefore, imposing DSM as a choice rule can get us invulnerability without sacrificing incompleteness, even in the limit.

1.  Incompleteness and Choice
=============================

The aim of this brief section is to show that the results that follow in section 2 do not require transitivity. Some question the requirement of transitivity when preferences are incomplete (cf [Bradley 2015](https://personal.lse.ac.uk/bradleyr/pdf/Transitive%20Choice%20\(NBFest4\).pdf), p. 3), but if that doesn’t apply to you, a quick skim of this section will provide enough context for the rest.

1.1.  Suzumura Consistency
--------------------------

Requiring that preferences be transitive may require that they be complete. To see this, notice that the weak preference relation $\succeq$ on a set of prospects $X$ is transitive just in case $\forall \alpha,\beta,\gamma \in X$, $\alpha\succeq\beta$ and $\beta\succeq\gamma$ implies $\alpha\succeq \gamma$. Suppose an agent does weakly prefer $\alpha$ to $\beta$ and $\beta$ to $\gamma$ but has no preference between $\alpha$ and $\gamma$. Then transitivity is violated. Suzumura ([1976](https://www.jstor.org/stable/2553273)) proposes a weakening of transitivity for agents with incomplete preferences, which allows for such preferences while preserving some desirable properties. We will say that a weak preference relation is *strongly acyclic* just in case

    **(Strong Acyclicity)**   $\forall \alpha_1,...,\alpha_n \in X$, $\alpha_1 \succeq...\succeq \alpha_{n}$ implies $\alpha_n \nsucc \alpha_1$.

We'll say that an agent whose preferences satisfy this property is *Suzumura consistent*. Bossert and Suzumura ([2010](https://www.jstor.org/stable/j.ctvjhzq9s)) show that such an agent has some noteworthy features:

1.  Strong acyclicity rules out cycles containing at least one strict preference. This will make Suzumura consistent agents invulnerable to (forcing) money pumps.
2.  Strong acyclicity is necessary and sufficient for the existence of a complete and transitive extension of the agent’s preference relation.
3.  Any preference relation that is both strongly acyclic and complete is transitive.

Preferences that are incomplete may also be intransitive. Whether or not transitivity is a rationality condition, strong acyclicity is weaker but preserves some desirable properties. Below I will mostly just assume strong acyclicity. But since transitivity implies strong acyclicity, all the (sufficiency) results likewise apply to agents with transitive preferences.

1.2.  Strong Maximality
-----------------------

Bradley ([2015](https://personal.lse.ac.uk/bradleyr/pdf/Transitive%20Choice%20\(NBFest4\).pdf)) proposes a choice rule for Suzumura consistent agents which differs from the standard condition—Maximality—for agents with incomplete preferences.[^0luewbcqek9] This rule—Strong Maximality—effectively asks the agent to eliminate dominated alternatives in the following way: eliminate any options that you strictly disprefer to any others, then if you are indifferent between any remaining options and any eliminated ones, eliminate those as well. To state the rule formally, we define a sequence $\langle \bar{C}^\tau(A) \rangle_{\tau=0}^\infty$ satisfying

$\quad \bar C^0(A)=\{ \alpha\in A:\beta \succ \alpha \;\;\exists \beta \in A \}$ and $\quad \bar C^\tau(A)=\{ \alpha\in A:[\beta \sim \alpha]\land [\beta \in \bar C^{\tau-1}(A)] \;\;\exists \beta \in A \}$ whenever $\tau \ge 1$

for any nonempty set of prospects $A$. We can then state the rule as

    **(Strong Maximality)**   $C^{\text{SM}}(A)=\big\{ \alpha\in A:\alpha \notin \bigcup_{\tau=0}^\infty \bar C^\tau (A)\big\}$.

Let’s see intuitively what this rule captures. Suppose $\alpha \succ \beta$ and $\beta \sim \gamma$ but $\alpha \not\bowtie \gamma$.[^1qvo9b7x78t] The traditional maximality rule implies that $C(\{\alpha,\beta,\gamma\})=\{\alpha,\gamma\}$. But strong maximality simply outputs $\{\alpha\}$. This is intuitive: don’t pick an option that’s just as bad as an option you dislike. And, more importantly, Theorem 2 of Bradley (2015) shows that Suzumura consistency is both necessary and sufficient for decisive, strongly maximal choice.[^m5fwt63x78s]

2.  Uncertain Dynamic Choice
============================

In this section I prove some theorems about the performance of agents with incomplete preferences in dynamic settings. I will amend strong maximality slightly to adapt it to dynamic choice, and show that this is sufficient to guarantee the invulnerability of these agents, broadly construed. I will say that an agent is *invulnerable* iff it is both unexploitable and opportunistic.

An agent is *unexploitable* just in case it is immune to all forcing money pumps. These are sequences of decisions through which an agent is compelled by their own preferences to sure loss. An agent is *opportunistic* just in case it is immune to all non-forcing money pumps. These are situations in which sure loss (or missed gain) is merely permissible, according to an agent’s preferences.

A few aspects of the broad approach are worth flagging. Normative decision theory has not settled on an ideal set of norms to govern dynamic choice. I will therefore provide results with respect to each of the following three dynamic choice principles: naivety, sophistication, and resoluteness. (More details below.) Agents will in general behave differently depending on which principle they follow. So, evaluating the behaviour resulting from an agent’s preferences should, at least initially, be done separately for each dynamic choice principle.

2.1.  Framework
---------------

The notation going forward comes from an edited version of Hammond's ([1988](https://link.springer.com/article/10.1007/bf00129168)) canonical construction of Bayesian decision trees. I will only describe the framework briefly, so I’ll refer interested readers to Rothfus ([2020a](http://gerardrothfus.com/wp-content/uploads/2021/02/University_of_California_Irvine_Thesis-3.pdf)) section 1.6. for discussion.

**Definition 1**  A *decision tree* is an eight-tuple $\langle N, \mathcal{C},\mathcal{N},X,N_+(\cdot),n_0,S(\cdot),\gamma(\cdot) \rangle$ where

1.  $N$ is a finite set of nodes partitioned into $\mathcal{C}$, $\mathcal{N}$, and $X$.
2.  $\mathcal{C}$ is the set of choice nodes. Here agents can pick the node’s immediate successor.
3.  $\mathcal{N}$ is the set of natural nodes. Agents have credences over their possible realisations.
4.  $X$ is the set of terminal nodes. These determine the outcome of a trajectory.
5.  $N_+: N\to \mathcal{P}(N)$ is the immediate successor function.
6.  $n_0$ is the initial node.
7.  $S: N\to \mathcal{P}(\mathbf{S})$ assigns the set of states that remain possible once a node is reached.
8.  $\gamma(x)$ is the consequence of reaching terminal node $x$.

**Definition 2**  A *set of plans* available at node $n$ of tree $T$, denoted $\Omega(T,n)$, contains the propositions and continuations consistent with the agent being at that node. Formally,

1.  $\Omega(T,n)=\{ S(n) \}$ if $n\in X$.
2.  $\Omega(T,n)=\{ S(n')\land \pi(n'): n'\in N_+(n), \; \pi(n')\in \Omega(T,n') \}$ if $n\in\mathcal{C}$.
3.  $\Omega(T,n) =\big\{ \bigwedge_{j=1}^{|N_+(n)|}[S(n_j)\to \pi(n_j)] : n_j\in N_+(n), \; \pi(n_j)\in\Omega(T,n_j) \big \}$ if $n\in \mathcal{N}$.[^nh3nxfrjlg]

There are finitely many plans in any tree. I will begin the discussion below with dynamic choice under certainty, but to set up the more general results, I will now lay out the framework for uncertain choice as well and specify later what is assumed. To start, it will be useful to have a representation theorem for our incomplete agents.

Imprecise Bayesianism ([**Bradley 2017**](https://personal.lse.ac.uk/bradleyr/pdf/Decision%20theory%20with%20a%20human%20face.pdf), Theorem 37)   *Let* $\succeq$ *be a non-trivial preference relation on a complete and atomless Boolean algebra of prospects* $\Omega=\langle X,\models \rangle$*, which has a minimal coherent extension on* $\Omega$ *that is both continuous and impartial.*[^hzkltiisi9d] *Then there exists a unique rationalising state of mind,* $S=\{\langle P^i,V^i \rangle \}$*, on* $\Omega$ *containing all pairs of probability and desirability measures jointly consistent with these preferences, in the sense that for all* $\alpha,\beta\in \Omega \smallsetminus \{\bot\}$*,*

    $\alpha \succeq \beta \iff V^i(\alpha)\ge V^i(\beta) \quad \forall V^i\in S$.

This theorem vindicates the claim that the state of mind of a broad class of rational agents with incomplete preferences can be represented by a *set* of pairs of probability and desirability functions. Although this theorem applies to imprecise credences, I’ll work with the special case of precise beliefs throughout. This will simplify the analysis. I’ll therefore use the following notation going forward: $Z=\{ i \in \mathbb{N} :V^i\in S \}$.

Next, I define some conditions that will be invoked in some of the derivations.

**Definition 3**  *Material Planning*: For a plan to specify choices across various contingencies, I formalise a planning conditional as follows. Let $n$ be a natural node and $n_j \in N_+(n)$ a possible realisation of it. Here, a plan

    $p(n)=S(n) \land \bigwedge_{j=1}^{|N_+(n)|} [S(n_j)\to S(z_j)]$

assigns a chosen continuation, $z_j\in N_+(n_j)$, to each possible realisation of $n$. When preferences are complete, a plan at a natural node is then evaluated as follows:

    $V_n(p)=\sum_{j=1}^{|N_+(n)|} V_n(z_j)P(n_j|p(n))$.

This is a natural extension of [Jeffrey’s equation](https://plato.stanford.edu/entries/decision-theory/#JefThe). And when preferences are incomplete:

    $p\succeq_n p'$ iff $V^i_n(p) \ge V^i_n(p') \;\;\forall i\in Z$.

This makes use of Bradley’s representation theorem for Imprecise Bayesianism.

**Definition 4**  *Preference Stability (Incomplete)*: For all nodes $n_a$ and $n_b$ and plans $p$ where $p(n_a)=p(n_b)$, we have $V_{n_a}^i(p)=V_{n_b}^i(p) \;\;\forall i\in Z$.

**Definition 5**  *Plan-Independent Probabilities (PIP)*: For any decision tree $T$ in which $n$ is a natural node, $n'\in N_+(n)$ is a realisation of $n$, and $p\in\Omega(T,n)$, $P(n'|p(n))=P(n'|n)$.

The results can now be stated. I will include proofs of the central claims in the main text; others are relegated to the appendix. I suggest scrolling past them if you aren’t particularly surprised by the result.

2.2.  Myopia
------------

Let’s begin with the simplest case of exploitation. We can stay silent on which dynamic choice principle to employ here: even if our agent is myopic, it will never be vulnerable to forcing money pumps under certainty. This follows immediately from Suzumura consistency since this guarantees that the agent never has a strict preference in a cycle of weak preferences.

**Proposition 1**   *Suzumura consistent agents myopically applying strong maximality are unexploitable under certainty.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

Two points are worth noting about the simple proof. First, it relies on strict preferences. This is because, if a money pump *must* go through a strongly maximal choice set with multiple elements (due to indifference or appropriate incomparability), it is necessarily non-forcing. That's the topic of the next section. Second, the proof doesn't rely on foresight. Myopia is an intentionally weak assumption that lets us show that no knowledge of the future is required for Suzumura consistent agents to avoid exploitation via these forcing money pumps.

2.3.  Naive Choice
------------------

Although Suzumura consistent agents using strong maximality can't be forced into money pumps, concern remains. Such an agent might still *incidentally* do worse by their own lights. That is, it remains vulnerable to non-forcing money pumps and thereby fails to be opportunistic. The single-souring money pump below is a purported example of this.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/f51023ee599ab84cbd45dbfc69f8418cd36f7e46bda8b42d.png)

Figure 1. Adapted from Gustafsson (2022, Figure 9).

The agent’s preferences satisfy $A\succ A^-$ and $B\not\bowtie A,A^-$. Suppose that it’s myopic and uses strong maximality at each node. The agent begins with $A$ at node 0 (if we let ‘down’ be the default). It is permitted, though not compelled, to go ‘up’ at node 0 instead (since $B$ will become available), but also to go ‘up’ upon arrival at node 1 (since $A^- \not\bowtie B$). Suppose it in fact goes ‘up’ at both node 0 and at node 1. This would leave it with $A^-$, which is strictly worse than what it began with. This money pump is ‘non-forcing’ because the agent’s preferences are also consistent with avoiding it.

The agent need not be myopic, however. It can plan ahead.[^55pbejubw92] To achieve opportunism for Suzumura consistent agents, I propose a choice rule which I’ll dub *Dynamic Strong Maximality* (DSM). DSM states that a plan $p$ is permissible at node $n$ just in case (a) it is strongly maximal at $n$ and (b) no other such plan was previously more choiceworthy than $p$.

**(Dynamic Strong Maximality)**   $p\in D(\Omega(T,n))$ iff

   (a)  $p\in C^{\text{SM}}(\Omega(T,n))$ and

   (b)  $\nexists p^*\in C^{\text{SM}}(\Omega(T,n)) : p^* \in C^{\text{SM}}(\Omega(T,n_0)) \not\ni p$ .

DSM is a slight refinement of strong maximality. Condition (b) simply offers a partial tie-breaking rule whenever the agent faces multiple choiceworthy prospects. So, importantly, it never asks the agent to pick counter-preferentially. An agent following *naive choice* with DSM will, at each node, look ahead in the decision tree, select their favourite trajectory using DSM, and embark on it. It can continually re-evaluate its plans using naive-DSM as time progresses and, as the following result establishes, the agent will thereby never end up with something worse than what it began with.

**Proposition 2 (Strong Dynamic Consistency Under Certainty via Naivety)**   *Let* $T$ *be an arbitrary tree where* $n$ *is a choice node,* $n'\in N_+(n)$*, and* $p\in\Omega(T,n)$ *is consistent with* $S(n')$*. Then* $p(n)\in D(\Omega(T,n))$ *iff* $p(n')\in D(\Omega(T,n'))$*.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

Intuitively, this means that (i) if the agent now considers a trajectory acceptable, it will continue to do so as time passes, and (ii) if it at any future point considers some plan continuation acceptable, its past self would agree. It follows immediately that all and only the strongly maximal terminal nodes are reachable by agents choosing naively using DSM (derived as [Corollary 1](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix:_Proofs)). This gives us opportunism: the agent will never pick a plan that’s strictly dominated some other available plan.

Under certainty, this result is unsurprising.[^vh83xvdhpj] What is less obvious is whether this also holds under uncertainty. I will say that a Bayesian decision tree exhibits *PIP-uncertainty* just in case the probability of any given event does not depend on what the agent plans to do after the event has occurred. We can now state the next result.

**Proposition 3 (Strong Dynamic Consistency Under PIP-Uncertainty via Naivety)**    
*Let node* $n$ *be non-terminal in decision tree* $T$*,* $n'\in N_+(n)$*, and plan* $p\in\Omega(T,n)$ *be consistent with* $S(n')$*. Assume Material Planning, Preference Stability, and Plan-Independent Probabilities. Then* $p\in D(\Omega(T,n))$ *iff* $p\in D(\Omega(T,n'))$*.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

We have thereby shown that a naive DSM agent is strongly dynamically consistent in a very broad class of cases. Although these results are restricted to PIP-uncertainty, this applies to agents with complete preferences too. It’s just a result of the forward-looking nature of naive choice. In the next section, I will drop the PIP restriction by employing a different dynamic choice principle.

2.4.  Sophisticated Choice
--------------------------

Sophistication is the standard principle in dynamic choice theory. It achieves dynamic consistency in standard cases by using backward induction to achieve the best feasible outcome. (This is also the method by which subgame perfect equilibria are found in dynamic games of perfect information.) However, backward induction is undefined whenever the prospects being compared are either incomparable or of equal value. Rabinowicz ([1995](https://www.jstor.org/stable/2941089)) proposed a ‘splitting procedure’ to address this, and Asheim ([1997](https://www.jstor.org/stable/2971722)) used a similar approach to refine subgame perfection in games.

According to this procedure, whenever there is a tie between multiple prospects, the agent will split the sequential decision problem into parts, where each part assumes that a particular prospect was chosen at that node. The agent then compares each part’s solution and picks its favourite as the solution to the grand decision problem. Intuitively, these agents will follow a plan as long as they lack “a positive reason for deviation” ([Rabinowicz 1997](https://link.springer.com/article/10.1023/A:1004920611437)). In other words, the agent will consider all the plans that would not make it locally act against their own preferences and, among those plans, proceed to pick the one with the best ex-ante outcome.

In the case of incomplete preferences, however, it turns out that strongly maximal sophisticated choice with splitting will *not* suffice to guarantee opportunism. The reason behind this is that strong maximality does not satisfy Set Expansion, and that backward induction makes local comparisons.[^d70xugugide]

**Proposition 4**   *Strongly maximal sophisticated choice with splitting does not guarantee opportunism for Suzumura consistent agents.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

DSM, however, will suffice.

Proposition 5 (Strong Dynamic Consistency Under Certainty via Sophistication)  
*Assume certainty and Suzumura consistency. Then DSM-based backward induction with splitting reaches a strongly maximal terminal node.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

More importantly, we can guarantee this property under uncertainty even without PIP.

Proposition 6 (Strong Dynamic Consistency Under Uncertainty via Sophistication)  
*Let* $T$ *be a Bayesian decision tree in which* $n$ *is a non-terminal node,* $n'\in N_+(n)$ *is a successor, and* $p\in\Omega(T,n)$ *is consistent with* $S(n')$*. Assume Material Planning and Preference Stability. Then with DSM-based backward induction (DSM-BI),* $p$ *is permissible at* $n$ *iff* $p$ *is permissible at* $n'$*.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

This lets us achieve strong dynamic consistency even in cases where the probability of an event depends on what the agent plans to do after the event has occurred. An example of such a decision problem is *Sequential Transparent Newcomb*, as devised by Bryan Skyrms and Gerard Rothfus (cf [Rothfus 2020b](https://link.springer.com/article/10.1007/s11098-020-01415-0)). So, even in this very general setting, our agent’s incomplete preferences aren’t hindering its opportunism.

2.5.  Resolute Choice
---------------------

A final canonical principle of dynamic choice is *resoluteness* as introduced by McClennen ([1990](https://www.cambridge.org/core/books/rationality-and-dynamic-choice/97BF3448ED05F4BB2515C3E739BCEB1A)). An informal version of this principle is often discussed in the AI alignment community under the name ‘[updatelessness](https://www.alignmentforum.org/tag/updateless-decision-theory)’. Briefly, a resolute agent will, first, pick its favourite trajectory now under the assumption that this plan will continue to be implemented as the agent moves through the decision tree. And, second, the agent will continually implement that plan, even if this makes it locally choose counter-preferentially at some future node.[^z4j3503r8v] It respects its ex-ante commitments.

Under certainty or uncertainty, this is the easiest principle with which to guarantee the invulnerability of agents with incomplete preferences (relative to those with complete preferences). By construction, the agent never implements a plan that was suboptimal from an earlier perspective. I will therefore omit formal derivations of dynamic consistency for resolute choosers\(\).[^j0uv9nirha]

3.  The Trammelling Concern
===========================

A possible objection to the relevance of the results above is what I’ll call the *Trammelling Concern.* According to this objection, agents with incomplete preferences who adopt DSM as a dynamic choice rule will, in certain sequential choice problems, or over the course of sufficiently many and varied ones, eventually converge in behaviour to an agent with complete preferences using Optimality as a choice rule. This would be worrying since complete preferences and optimal choice resembles the kind of consequentialism that precludes Thornley-style corrigibility.

This section aims to quell such worries. I begin with a taxonomy of our agent’s possible doxastic attitudes towards decision trees. First, the set of non-terminal *nodes* of a given tree will either contain only choice nodes, or it will contain some natural nodes. Second, the *structure* of a given tree will either be entirely known to the agent, or it will not. If it is not known, the agent will either have beliefs about all its possible structures, or its credence function will not be defined over some possible tree structures. We will refer to these three cases as *certainty*, *uncertainty*, and *unawareness* about structure, respectively.[^gj4o2jvnus] Finally, at least under unawareness, the possible tree structures may or may not include terminal nodes (prospects) that are also present in the tree structure currently being considered by the agent. I will say the prospects are *new* if so and *fixed* if not.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/a1d2151526a6f4f3b4cf0364165042c72797c33f9532bb9b.png)

Table 1.

This table summarises the situations our agent might find itself in and its cells indicate whether trammelling can occur in each case. This is based on the arguments and results below. The conclusions for (1)-(2) are based on conceptual considerations in section 3.1. Cases (3)-(4) are not discussed explicitly since uncertain tree structures can simply be represented as certain tree structures with natural nodes. The conclusions for (5) and (7) are based on formal results in section 3.2. For the sake of brevity, the effects of natural nodes under unawareness are left for later work.

3.1.  Aware Choice
------------------

*This section was co-authored with* [*Eric*](https://www.linkedin.com/in/eric-chen-449317272/)  [*Chen*](https://www.lesswrong.com/users/eric-chen).

Let’s begin with an important distinction. As Bradley (2015) puts it, there’s a difference between "the choices that are *permissible* given the agent’s preferences, those that are *mandatory* and those that she *actually* makes" (p. 1). If an agent is indifferent between two options, for example, then it can be the case that (i) both are permissible, (ii) neither is mandatory, and (iii) a particular one is in fact chosen. One aspect of choice between incomparables that we need to preserve is that all were permissible ex-ante. The fact that one is in fact chosen, ex-post, is immaterial.

To see what this implies, consider first the case of certainty. Here we proved that DSM will result in only ex-ante strongly maximal plans being implemented (Proposition 2; Corollary 1; Proposition 5). Now consider the following toy case (Example 1). A Suzumura consistent agent can’t compare $A$ and $B$. It’s offered a choice between the two. Suppose it chooses $B$. Does this constrain the agent to never pick $A$ in future choices between $A$ and $B$?

No. In fact, it’s a bit unclear what this would mean formally. Once we expand the decision tree to include future choices between $A$ and $B$ in some branches, everything boils down to the fact that all plans through this tree will result in either $A$ or $B$. And so any plan will be permissible. What DSM constrains is which terminal nodes are reached; not how the agent gets there. Let’s see how far this reasoning can get us.

**Example 2**   A Suzumura consistent agent’s preferences satisfy $A\succ A^-$ and $B\not\bowtie A,A^-$. It’s offered a choice between going ‘down’ for $A$ or going ‘up’ to face a choice between $A^-$ and $B$. It happens to go ‘up’. Does this constrain the agent not to pick $A^-$ over $B$?

This is a case of an agent ending up on some trajectory that is only consistent with one of its coherent extensions ('completions'). One might worry that, at this point, we can treat the agent as its unique extension, and that this denies us any kind of corrigible behaviour. But there is a subtle error here. It is indeed the case that, once the agent has reached a node consistent with only one extension, we can *predict* how it will act going forward via its uniquely completed preferences. But this is not worrisome. To see why, let’s look at two possibilities: one where the agent is still moving through the tree, and another where it has arrived at a terminal node.

First, if it is still progressing through the tree, then it is merely moving towards the node it picked at the start, by a process we are happy with. In Example 2, option $A^-$ was never strongly maximal in comparison to $A$ and $B$. We knew, even before the agent went ‘up’, that it wouldn’t pick $A^-$. So the agent is no more trammelled once it has gone ‘up’ than it was at the beginning.

For a more concrete case, picture a hungry and thirsty mule. For whatever reason, this particular mule is unable to compare a bale of hay to a bucket of water. Each one is then placed five metres from the mule in different directions. Now, even if the mule picks arbitrarily, we will still be able to predict which option it will end up at once we see the direction in which the mule is walking. But this is clearly not problematic. We wanted the mule to pick its plan arbitrarily, and it did.

Second, if the agent has reached the end of the tree, can we predict how it would act when presented with a new tree? No; further decisions just constitute a continuation of the tree. And this is just the case we described above. If it did not *expect* the continuation, then we are simply dealing with a Bayesian tree with natural nodes. In the case of PIP-uncertainty, we saw that DSM will once again only result in the ex-ante strongly maximal *plans* being implemented (Proposition 3).[^ufpnjx93gqn] Here it's useful to recall that plans are formalised using conditionals:

    $p(n)=S(n) \land \bigwedge_{j=1}^{|N_+(n)|} [S(n_j)\to S(z_j)]$, where $n_j\in N_+(n)$ and $z_j\in N_+(n_j)$.

That is, plans specify what path to take at every contingency. The agent selects *plans*, not merely prospects, so no trammelling can occur that was not already baked into the initial choice of plans. The general observation is that, if many different plans are acceptable at the outset, DSM will permit the agent to follow through on any one of these; the ex-post behaviour will “look like” it strictly prefers one option, but this gets close to conflating what options are *mandatory* versus *actually chosen*. Ex-post behavioural trajectories do not uniquely determine the ex-ante permissibility of plans.

3.2.  Unaware Choice
--------------------

The conceptual argument above does not apply straightforwardly to the case of unawareness. The agent may not even have considered the possibility of a certain prospect that it ends up facing, so we cannot simply appeal to ex-ante permissibility. This section provides some results on trammelling in this context. But, first, given the argument about Bayesian decision trees under certain structure, one may ask: what, substantively, is the difference between the realisation of a natural node and awareness growth (if all else is equal)? Would the behaviour of our agent just coincide? I don't think so.

**Example 3**   Consider two cases. Again, preferences satisfy $A\succ A^-$ and $B\not\bowtie A,A^-$.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/3799e77c99f28e721b48c86b0d547dbf683422fe5dd5db4f.png)

Figure 2.

Up top, we have a Bayesian tree. On the bottom, we have awareness growth, where each tree represents a different awareness context. In both, let’s suppose our agent went ‘up’ at node 0. In the Bayesian case, let’s also suppose the natural node (1) resolves such that the agent reaches node 2. In both diagrams, the agent ends up having to pick $A^-$ or $B$.

The permissible plans at the outset of the Bayesian tree are those that lead to $A$ or to $B$ (since $A^-$ is strictly dominated by $A$). But in the bottom case, it seems that our agent faces two distinct decision problems: one between $A$ and $B$; one between $A^-$ and $B$. In the first problem, both options are permissible. And likewise in the second. So, the difference between these situations is that, in the latter case, our agent faces a *new decision problem*.

In the Bayesian case, our agent might end up at a future node in which the only available options are incomparable but nevertheless reliably picks one. But the reason for this is that another node, also available at the moment the agent picked its plan, was strictly preferred to one of these. The agent’s decision problem was between $A$, $A^-$, and $B$. The arbitrary choice was between $A$ and $B$. This is as it should be; there is no trammelling.

However, in the case of unawareness, the agent initially chose between $A$ and $B$ and now it must choose between $A^-$ and $B$. It never got to compare $A$ to $A^-$ to $B$. It compared $A$ to $B$ and, separately, $A^-$ to $B$. Therefore, if it reliably picks $B$ over $A^-$, for the sake of opportunism, one could see this as a form of trammelling. I now turn to this issue.

For brevity, I will focus on cases 4 and 5 from the taxonomy above. In these worlds, all decision trees have choice nodes and terminal nodes, but they lack natural nodes. And our agent is unaware of some possible continuations of the tree they are facing. That is, it’s unaware of—places no credence on—the possibility that a terminal node is actually another choice node. But once it in fact gets to such a node, it will realise that it wasn’t terminal. There are then two ways this could play out: either the set of available prospects expands when the tree grows, or it doesn’t. Let’s consider these in turn. As we’ll see, the most salient case is under a certain form of expansion (section 3.2.3., Example 6).

### 3.2.1.  Fixed Prospects (No Trammelling)

Here I’ll show that when prospects are fixed, opportunism and non-trammelling are preserved. We begin with an illustrative example.

**Example 4**   The agent’s preferences still satisfy $A\succ A^-$ and $B \not\bowtie A,A^-$.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/6505a899ee7aa96767defe982cb7416c48f624bf603ee652.png)

Figure 3.

The agent initially sees the top tree. DSM lets it pick $A$ or $B$, arbitrarily. Suppose it in fact goes for $A$. Then its awareness grows and the tree now looks like the bottom one. It can stay put (go ‘down’ to $A$) or move ‘up’ and choose between $B$ and $A^-$. DSM still says to pick, arbitrarily, any path leading to $A$ or to $B$. Suppose it goes for $B$. There—no trammelling.

Here’s the lesson. Our agent will embark on a path that’ll lead to a node that is DSM with respect to the initial tree. When its awareness grows, that option will *remain available* in the new tree. By Set Contraction ([Lemma 4](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix:_Proofs)) this option will also *remain DSM* in the new tree. So, picking it will still satisfy opportunism. And regarding trammelling, it can still pick entirely arbitrarily between all initially-DSM nodes. DSM constrains which prospects are reached; not how to get there. We can state this as follows.

**Proposition 7**   *Assume no natural nodes. Then, DSM-based choice under awareness growth will remain arbitrary whenever the set of available prospects is fixed.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

### 3.2.2.  New Prospects (No Trammelling)

Now consider the case where the set of available prospects expands with the tree. It's of course possible that our agent gets to a terminal node that isn’t strongly maximal according to the new tree. This could happen if they get to an initially-acceptable terminal node and then realise that a now-inaccessible branch would let them access a prospect that’s strictly preferred to all those in the initial tree.[^r2zvmaagbir] But, importantly, this applies to agents with complete preferences too. It’s simply an unfortunate feature of the environment and the agent’s epistemic state. Complete preferences don’t help here. 

But there is a class of cases in which completeness, at first glance, seems to help.

**Example 5**   The agent’s preferences satisfy $A\succ A^-\sim B$ and $A\not\bowtie B$ (unlike before).

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/938f9b63163f556e7a211ba696db0e4dba4421fb4f4dda35.png)

Figure 4.

The agent sees the tree on the left. DSM lets it pick $A$ or $B$, arbitrarily. Suppose it in fact goes for $B$. Now its awareness grows and the tree looks like the one on the right. It can stay put (go ‘down’ to $B$) or move ‘up’ to get $A^-$.

Now, none of the available options are DSM in the full tree, but the agent still has to pick one. This, on its own, is not problematic since it could just be an unfortunate aspect of the situation (as dismissed above). But in this particular case, because an agent with complete preferences would satisfy transitivity, it would never go for $B$ in the first place. This kind of issue wouldn’t occur if our agent’s incomplete preferences were transitive, rather than just strongly acyclic.

So let’s impose transitivity. Then our agent wouldn’t pick $B$ in the first place. In general it will now remain opportunistic in the same way that its complete counterparts are. That’s because it would never initially choose arbitrarily between options that *all* its coherent extensions have a strict preference between. So it would never pick in a way that makes it realise that it made a foreseeable mistake once more options come into view. To operationalise this, I'll say that an agent facing deterministic decision trees *fails* to be opportunistic under awareness growth iff

1.  The agent fails to reach a strongly maximal prospect in the grand tree, *and*
2.  A strongly maximal prospect in the grand tree is available after awareness growth.

This agent *is* opportunistic otherwise.[^fsy0q5xojbp] That gives us opportunism for our incomplete agent, but what about non-trammelling? Will our agent ever *have* to pick one option over another despite them being incomparable? Yes, in some cases.

### 3.2.2.  New Prospects (Bounded Trammelling)

**Example 6**   The agent’s preferences satisfy $A\succ A^-$ and $B\not\bowtie A,A^-$.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/cd4b19d95544090a42494fad52274a1c2712595bde28d37e.png)

Figure 4 (repeated).

It faces the same trees as in the previous example. DSM first lets it pick $A$ or $B$, arbitrarily. Suppose it goes for $B$. Now its awareness grows and the tree looks like the one on the right. It can stay put (go ‘down’ to $B$) or move ‘up’ to get $A^-$. Since only $B$ is DSM in the global tree, our agent might *reliably* pick $B$ over $A^-$, despite them being incomparable. Trammelled.

This is a special property of unawareness. Thankfully, however, we can bound the degree of trammelling. And I claim that this can be done in a rather satisfying way. To do this, let’s formally define an extension of DSM that will give us opportunism under awareness growth. Let $T_1$ denote the initial tree, with initial node $n_0$, and $T_2$ the tree available after awareness growth, with initial node $n^0$. And let $T$ denote the appending of $T_2$ on $T_1$.

**(Global-DSM)**   $p\in G(\Omega(T_2,n^0))$ iff

    (i)  $p\in C^{\text{SM}}(\Omega(T_2,n^0))$ and

    (ii)  $\nexists p^* \in C^{\text{SM}}(\Omega(T_2,n^0)):p^* \in C^{\text{SM}}(\Omega(T,n_0)) \not\ni p$.

Notice that G-DSM doesn’t look at what happens at other previously-terminal nodes after awareness grows. These are unreachable and would leave the choice rule undefined in some cases. (This holds with complete preferences too.) This rule naturally extends opportunism to these cases; it says to never pick something if you knew that you could’ve had something better before. We can now state some results.

**Proposition 8 (Non-Trammelling I)**   *Assume transitive preferences and no natural nodes. Then, under all possible forms of awareness growth, globally-DSM naive choice will remain arbitrary whenever the available prospects are (i) mutually incomparable and (ii) not strictly dominated by any prospect.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

That gives us a sufficient condition for arbitrary choice. To find out how often this will be satisfied, we define ‘comparability classes’ as subsets of prospects within which all are comparable and between which none are. A comparability-based partitioning of the prospects is possible when comparability is transitive.[^lvurdlxhnn] The following results then follow.

**Proposition 9 (Bounded Trammelling I)**   *Assume that comparability and preference are transitive and that there are no natural nodes. Then, under all possible forms of awareness growth, there are at least as many prospects between which globally-DSM naive choice is guaranteed to be arbitrary as there are comparability classes.*

**Proof.**  We first partition the set of prospects $X$ into subsets of mutually comparable prospects.

Given transitivity, $\bowtie$ is an equivalence relation on $X$. Then, for any $x\in X$, we construct an equivalence class: $[x]_\bowtie \triangleq \{ y\in X: y\bowtie x \}$. Call this set the *comparability class* of $x$.

This lets $\{ [x]_\bowtie \}_{x\in X}$ form a partition of $X$.

We identify the class-optimal prospects as follows: $X^* \triangleq \bigcup_{x\in X} C^{\text{Opt}}([x]_\bowtie)$.

Let $\Omega(T_2,n^0)\subseteq X^*$. Suppose, for contradiction, that $G(\Omega(T_2,n^0))\ne \Omega(T_2,n^0)$.

Since $G$ is a choice function, $G(A)\subseteq A$ for any set $A$. Then $G(\Omega(T_2,n^0))\subset \Omega(T_2,n^0)$.

Then, by G-DSM, there exists some $p\in \Omega(T_2,n^0)$ such that

    (i’)  $p\notin C^{\text{SM}}(\Omega(T_2,n^0))$ or

    (ii’)  $\exists p^* \in C^{\text{SM}}(\Omega(T_2,n^0)):p^* \in C^{\text{SM}}(\Omega(T,n_0)) \not\ni p$.

Given transitivity, and since all elements of $\Omega(T_2,n^0)$ are mutually incomparable or indifferent, condition (i’) does not hold. Therefore $p\notin C^{\text{SM}}(\Omega(T,n_0))$.

By transitivity, this implies that $p' \succ p$ for some $p'\in \Omega(T,n_0)$. (1)

But since $p \in C^{\text{Opt}}([x]_\bowtie)$ for some $x\in X$, we know that $p\in C^{\text{SM}}(X)$. (2)

By Set Contraction, $\Omega(T,n_0) \subseteq X$ contradicts (1)-(2).

This establishes that $G(\Omega(T_2,n^0))=\Omega(T_2,n^0)$ whenever $\Omega(T_2,n^0)\subseteq X^*$.

The set of all prospects satisfying this is of size $|X^*| \ge |\{ [x]_\bowtie \}_{x\in X}|$, as needed. $\;\blacksquare$$\;$

**Corollary 2 (Bounded Trammelling II)**  *Assume that comparability and preference are transitive and that there are no natural nodes. Then, whenever* $k$ *class-optimal prospects are available, choice will be arbitrary between at least* $k$ *prospects.* \[[Proof](https://www.lesswrong.com/posts/sHGxvJrBag7nhTQvb/invulnerable-incomplete-preferences-a-formal-statement-1#Appendix__Proofs).\]

3.3.  Discussion
----------------

It seems we can’t guarantee non-trammelling in general and between all prospects. But we don’t need to guarantee this for all prospects to guarantee it for some, even under awareness growth. Indeed, as we’ve now shown, there are always prospects with respect to which the agent *never* gets trammelled, no matter how many choices it faces. In fact, whenever the tree expansion does not bring about new prospects, trammelling will never occur (Proposition 7). And even when it does, trammelling is bounded above by the number of comparability classes (Proposition 10).

And it’s intuitive why this would be: we’re simply picking out the best prospects in each class. For instance, suppose prospects were representable as pairs $\langle s,c \rangle$ that are comparable iff the $s$-values are the same, and then preferred to the extent that $c$ is large. Then here’s the process: for each value of $s$, identify the options that maximise $c$. Put all of these in a set. Then choice between any options in that set will *always* remain arbitrary; never trammelled.

Three caveats are worth noting. First, sceptical readers may not agree with our initial treatment of (non-)trammelling under aware choice (i.e., known tree structures, section 3.1.). That section is based on a conceptual argument rather than formal results, so it should be evaluated accordingly. However, at least some of the results from the section on unawareness could be used to dampen many reasonable worries here. Whenever non-trammelling is satisfied under awareness growth with Global-DSM, it will likewise be satisfied, mutatis mutandis, by DSM when the tree structure is known.

Second, we've only considered part of the taxonomy described above. Due to time constraints, we left out discussion of unaware choice in trees with natural nodes. We suspect that extending the analysis to these kinds of cases would not meaningfully affect the main conclusions, but we hope to look into this in later work. Finally, we haven't provided a full characterisation of choice under unawareness. The literature hasn't satisfactorily achieved this even in the case of complete preferences, so this falls outside the scope of this article.

Conclusion
----------

With the right choice rule, we can guarantee the invulnerability—unexploitability and opportunism—of agents with incomplete preferences. I’ve proposed one such rule, Dynamic Strong Maximality, which nevertheless doesn’t ask agents to pick against their preferences. What’s more, the choice behaviour this rule induces is *not* representable as the agent having implicitly completed its preferences. Even under awareness growth, the extent to which the rule can effectively complete an agent’s implied preferences is permanently bounded above. And with the framework provided, it’s possible to make statements about which kinds of completions are possible, and in what cases.

This article aims to be somewhat self-contained. In future work, I’ll more concretely consider the implications of this for Thornley’s Incomplete Preference Proposal. In general, however, I claim that worries about whether a competent agent with preferential gaps would in practice (partially) complete its preferences need to engage with the particulars of the situation: the preference structure, the available decision trees, and so on. Full completion won't occur, so the relevant question is whether preferential gaps will disappear *in a way that matters*.

References
----------

Asheim, Geir. 1997. “Individual and Collective Time-Consistency.” *The Review of Economic Studies* 64, no. 3: 427–43.

Bales, Adam. 2023. “Will AI avoid exploitation? Artificial general intelligence and expected utility theory.” *Philosophical Studies*.

Bossert, Walter and Kotaro Suzumura. 2010. “Consistency, Choice, and Rationality.” *Harvard University Press*.

Bradley, Richard and Mareile Drechsler. 2014. “Types of Uncertainty.” *Erkenntnis* 79, no. 6: 1225–48.

Bradley, Richard. 2015. “A Note on Incompleteness, Transitivity and Suzumura Consistency.” In: Binder, C., Codognato, G., Teschl, M., Xu, Y. (eds) Individual and Collective Choice and Social Welfare. Studies in Choice and Welfare. Springer, Berlin, Heidelberg.

Bradley, Richard. 2017. *Decision Theory with a Human Face*. Cambridge: Cambridge University Press.

Gustafsson, Johan. 2022. *Money-Pump Arguments*. Elements in Decision Theory and Philosophy. Cambridge: Cambridge University Press.

Hammond, Peter J. 1988. “Consequentialist foundations for expected utility.” *Theory and Decision* 25, 25–78.

Huttegger, Simon and Gerard Rothfus. 2021. “Bradley Conditionals and Dynamic Choice.” *Synthese* 199 (3-4): 6585-6599.

Laibson, David and Yeeat Yariv. 2007. "Safety in Markets: An Impossibility Theorem for Dutch Books." Working Paper, *Department of Economics, Harvard University*.

McClennen, Edward. 1990. *Rationality and Dynamic Choice: Foundational Explorations*. Cambridge: Cambridge University Press.

Rabinowicz, Wlodek. 1995. “To Have One’s Cake and Eat It, Too: Sequential Choice and Expected-Utility Violations.” *The Journal of Philosophy* 92, no. 11: 586–620.

Rabinowicz, Wlodek. 1997. “On Seidenfeld‘s Criticism of Sophisticated Violations of the Independence Axiom.” *Theory and Decision* 43, 279–292.

Rothfus, Gerard. 2020a. “The Logic of Planning.” Doctoral dissertation, *University of California, Irvine*.

Rothfus, Gerard. 2020b. “Dynamic consistency in the logic of decision.” *Philosophical Studies* 177:3923–3934.

Suzumura, Kotaro. 1976. “Remarks on the Theory of Collective Choice.” *Economica* 43: 381-390.

Thornley, Elliott. 2023. “The Shutdown Problem: Two Theorems, Incomplete Preferences as a Solution.” *AI Alignment Awards*

Appendix: Proofs
----------------

Please see the in the final version [here](https://link.springer.com/article/10.1007/s11238-025-10052-0) for precise statements and proofs of results other than those discussed in section 3. Note that I haven't had the chance to change most of the main text of this post to match the updated paper.

**Proposition 7**   *Assume no natural nodes. Then, DSM-based choice under awareness growth will remain arbitrary whenever the set of available prospects is fixed.*

**Proof.**  Let $\Omega(T_1,n_0)$ denote the initially available prospects. Upon reaching $n^0$ the agent’s awareness grows and it faces $\Omega(T_2,n^0)$ . Suppose $\Omega(T_2,n^0) \subseteq \Omega(T_1,n_0)$ .

For any $x,y \in C^{\text{SM}}( \Omega (T_1,n_0))\cap \Omega(T_2,n^0)$, we have $x,y\in C^{\text{SM}}(\Omega(T_2,n^0))$ by Set Contraction. Choice was arbitrary within $C^{\text{SM}} (\Omega(T_1,n_0))$, and will be arbitrary in $C^{\text{SM}}(\Omega(T_2,n^0))$.

Therefore, we know that for any $x,y\in \Omega(T_1,n_0)$ between which choice was arbitrary, choice will remain arbitrary between $x$ and $y$ whenever $x,y\in\Omega(T_2,n^0)$. $\;\blacksquare$$\;$

**Proposition 8 (Non-Trammelling I)**   *Assume transitive preferences and no natural nodes. Then, under all possible forms of awareness growth, globally-DSM choice will remain arbitrary whenever the available prospects are (i) mutually incomparable and (ii) not strictly dominated by any prospect.*

**Proof.**  Let $X$ denote the set of all prospects over which the agent’s preference relation is defined (i.e., candidates for terminal nodes). Our agent reaches node $n^0$, its awareness grows, and faces mutually incomparable prospects $\Omega(T_2,n^0) \subseteq X$ (there are no natural nodes). Necessarily, then, $C^{\text{SM}}(\Omega(T_2,n^0))=\Omega(T_2,n^0)$.

Suppose, also, that these are not strictly dominated: $\forall p\in \Omega(T_2,n^0),\;\nexists q\in X: q\succ p$ . ($*$)

Then given transitivity, $\Omega(T_2,n^0) \subseteq C^{\text{SM}}(X)$. Before awareness growth, the available prospects were $\Omega(T_1,n_0)\subseteq X$.

For globally-DSM choice between incomparables to be non-arbitrary, it must be the case that $G(\Omega(T_2,n^0)) \subset C^{\text{SM}}(\Omega(T_2,n^0))$, i.e., that some prospects in $\Omega(T_2,n^0)$ are more choiceworthy than others at the grand tree $T$’s initial node $n_0$. Since there are no natural nodes, this is equivalent to saying that

    $p\in C^{\text{SM}}(\Omega(T,n_0))\not\ni p'$ for some $p,p'\in \Omega(T_2,n^0)$.

Given transitivity, this implies that $\exists q \in \Omega(T,n_0):q\succ p'$. Since $\Omega(T,n_0)\subseteq X$, this contradicts ($*$). $\;\blacksquare$$\;$

**Corollary 2 (Bounded Trammelling II)**   *Assume that comparability and preference are transitive and that there are no natural nodes. Then, whenever* $k$ *class-optimal prospects are available, choice will be arbitrary between at least* $k$ *prospects.*

**Proof.**  Given transitivity, $[x]_\bowtie \triangleq \{ y\in X:y\bowtie x \}$ is an equivalence class.

We first show that $C^{\text{Max}}(X) = \bigcup_{x\in X}C^{\text{Opt}}([x]_\bowtie)$.

Suppose $a\in C^{\text{Max}}(X)$. Then $\nexists b\in X:b \succ a$. Hence $\nexists c\in [a]_\bowtie :c\succ a$. Given that all elements in a class are comparable, $a\succeq b \;\;\forall b\in [a]_\bowtie$, i.e., $a\in C^{\text{Opt}}([a]_\bowtie)$. Therefore $a\in \bigcup_{x\in X} C^{\text{Opt}}([x]_\bowtie)$, establishing $C^{\text{Max}}(X) \subseteq \bigcup_{x\in X}C^{\text{Opt}}([x]_\bowtie)$.

Suppose $a\in \bigcup_{x\in X}C^{\text{Opt}}([x]_\bowtie)$. Then since ether $[x]_\bowtie =[y]_\bowtie$ or $[x]_\bowtie \cap [y]_\bowtie = \emptyset$ for all $x,y\in X$, we know $a\in C^{\text{Opt}}([a]_\bowtie)$. Hence $\forall b\in X:b\bowtie a, \; a\succeq b$. This implies $b \not\succ a$.

And $\forall c \in X:c\not\bowtie a, \; c\not\succ a$. Therefore $\forall x\in X, \; x\not\succ a$ meaning $a\in C^{\text{Max}}(X)$.

So $\bigcup_{x\in X}C^{\text{Opt}}([x]_\bowtie) \subseteq C^{\text{Max}}(X)$ . This establishes that the maximal set and the class-optimal prospects coincide.

Next, suppose $A\subseteq C^{\text{Max}}(X)$ and $A\subseteq \Omega(T,n)$ at some node $n$ in deterministic tree $T$.

Let $k=|A|$ and suppose, for contradiction, that choice at $n$ is arbitrary between fewer than $k$ prospects. Then $|G(\Omega(T,n))| <k$.

Under preference transitivity, this implies that $\exists a\in A, \;\exists b\in \Omega(T,n):b\succ a$ by Set Contraction and the definition of $G$. ($*$)

But since $a\in C^{\text{Max}}(X)$ for all $a\in A$, and $\Omega(T,n) \subseteq X$, Set Contraction implies that $a\in C^{\text{Max}}(\Omega(T,n))$. Hence $\nexists b\in \Omega(T,n):b\succ a$, contradicting ($*$). $\;\blacksquare$ 

[^3m1r2zyk7s5]: Nate Soares has also remarked, regarding Thornley’s proposal, that the consequences of violating the von Neumann-Morgenstern (vNM) axioms should be explored. This is one such exploration. Though I will note that, in any case, the vNM axiomatisation is plausibly not the relevant baseline here. Instead it’d be the subjective representation theorems from Savage, Bolker-Jeffrey, Joyce, etc. And as we’ll see below, the Jeffrey framework has been usefully extended to the case of incompleteness. 

[^tinxlqvh5gl]: Though see Bales (2023) and Laibson & Yariv (2007) for reasons to be sceptical of unqualified versions of this claim. 

[^j21kg28mi9h]: Opportunism implies unexploitability, so invulnerability is in fact equivalent to opportunism. 

[^0luewbcqek9]: I will often refer to various properties of choice functions. For those unfamiliar with these, I suggest Richard Bradley’s introductory text on decision theory, section 4.2. 

[^1qvo9b7x78t]: Notation: \(\succeq\) (weak preference) is a reflexive binary relation on a set of prospects. \(\sim\) (indifference) is the symmetric part of \(\succeq\). \(\succ\) (strict preference) is the anti-symmetric part of \(\succeq\). \(\bowtie\) (comparability) is a relation satisfying \(\alpha\bowtie\beta\) iff \(\alpha\succeq \beta\) or \(\beta \succeq \alpha\). A slash through a relation denotes its negation (e.g., \(\alpha\not\bowtie\beta\) iff \(\alpha\) and \(\beta\) are incomparable). 

[^m5fwt63x78s]: \(C(\cdot)\) is decisive iff \(C(X)\) is always nonempty (when \(X\) is nonempty). 

[^nh3nxfrjlg]: The conditional ‘\(\to\)’ is operationalised below in Definition 3. It will differ from the Bradley conditional used in Huttegger and Rothfus (2021). 

[^hzkltiisi9d]: Explaining the conditions: Non-triviality: \(\exists \alpha\in \Omega :\alpha \succeq \top\), where \(\top\) is the tautology. \(\succeq\) has a minimal coherent extension, \(\succeq'\), on \(\Omega\) iff (i) \(\alpha \succeq \beta \implies \alpha \succeq' \beta\), (ii) \(\alpha \succ \beta \implies \alpha \succ' \beta\), and (iii) \(\succeq'\) is complete and transitive. Indeed, \(\succeq\) is strongly acyclic by Theorem 2 of Bradley (2015). Impartiality: Suppose \(\alpha \sim \beta\) and for some \(\gamma \nsim \alpha\) such that \(\alpha\gamma = \bot = \beta\gamma\), we have \((\alpha \lor \gamma) \sim (\beta\lor\gamma)\). Then for all such \(\gamma\), \((\alpha\lor\gamma)\sim(\beta\lor\gamma)\). Continuity: Let \(\{\alpha_1, \alpha_2,... \}\) be a countable set such that \(\alpha_1 \models \alpha_2 \models...\). Suppose \(\beta \succeq \alpha_i\) and \(\alpha_i\succeq \gamma\) for all \(i\). Then \(\beta \succeq \bigcup_i \{\alpha_i\}\) and \(\bigcup_i \{\alpha_i\} \succeq \gamma\). A desirability measure \(V\) satisfies \(V(\top )=0\) (Normality) and \(\forall\alpha,\beta\in\Omega\smallsetminus\{\bot\} : \alpha \land \beta = \bot, \; \alpha \succeq \beta \iff \alpha \succeq (\alpha \lor \beta ) \succeq \beta\) (Averaging). 

[^55pbejubw92]: In section 3.2. I consider issues related to what happens if it can only plan ahead to a limited extent (or not at all). 

[^vh83xvdhpj]: Note that the notion of ‘certainty’ used here rules out Sequential Transparent Newcomb (Rothfus 2020b) with a perfect predictor. The results in section 2.4. do not. 

[^d70xugugide]: \(C(\cdot)\) satisfies Set Expansion iff whenever \(B\subseteq A \ni \alpha\), then \(\alpha,\beta \in C(B)\) and \(\beta \in C(A)\) implies \(\alpha \in C(A)\). 

[^z4j3503r8v]: According to Gauthier's (1997) framing. 

[^j0uv9nirha]: Note that, below, I will consider the case of unawareness. For discussion of resolute choice under awareness growth, I’ll refer to Macé et al (2023). 

[^gj4o2jvnus]: The latter is sometimes known as state space uncertainty; see Bradley and Drechsler (2014). 

[^ufpnjx93gqn]: In the general case of uncertainty, the agent is able to only implement the strongly maximal feasible plans (Proposition 6). 

[^r2zvmaagbir]: Here’s an example. Suppose the agent can choose between going ‘up’ and ‘down’. If it goes ‘up’, it gets \(A\). If it goes ‘down’, it gets to choose between \(A^+\) and \(B\). (This is the structure of a single-sweetening money pump.) If the agent is aware of the tree structure, then naive DSM choice lets it go for either ‘down-\(A^+\)’ or ‘down-\(B\)’. If the agent is unaware and thinks that ‘down’ leads to \(B\) only, then naive DSM choice lets it initially go ‘up’ (\(A\)) or ‘down’ (\(B\)). If it goes ‘down’, it can pick arbitrarily and opportunistically between \(A^+\) and \(B\) once its awareness grows. But if it goes ‘up’ it will realise, after awareness growth, that it could’ve done better. The problem in the latter case, however, is centrally a result of unawareness, not of incompleteness. An agent with complete preferences satisfying \(A^+ \succ A \sim B\) will also choose arbitrarily initially and regret their decision if they went ‘up’. 

[^fsy0q5xojbp]: Example 5 is a violation of opportunism under awareness growth. This is because the agent fails to arrive at a maximal node even though the growth of the tree did not bring about any prospects that are strictly preferred to the previously present ones. 

[^lvurdlxhnn]: This requirement is not in general equivalent to the transitivity of weak preference.