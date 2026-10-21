*Work funded by the* [*Long Term Future Fund.*](https://funds.effectivealtruism.org/funds/far-future)

Corrigibility is the hypothetical feature of some agents which allows them to be 'shut down' by an outside user without attempting to manipulate the whether or not they are shut down. The motivation behind this concept is the possibility of making an AI agent which can pursue a 'trial' goal given to it by its creators, but can be stopped if pursuing this goal becomes undesirable.

On the face of it, Corrigibility sounds a bit like a bargaining problem. A corrigible agent might behave as a comprise between two subagents: one which cares about pursuing the original goal, and one which cares about achieving shutdown. 

Recently, [@johnswentworth](https://www.lesswrong.com/users/johnswentworth?mention=user) and [@David Lorell](https://www.lesswrong.com/users/david-lorell?mention=user) have written [A Shutdown Problem Proposal](https://www.lesswrong.com/posts/PhTBDHu9PKJFmvb4p/a-shutdown-problem-proposal), which discusses this suggestion a bit more. However, they do not specify out the mechanism by which the subagents will reach their agreement. They write:

> Then there’s the problem of designing the negotiation infrastructure, and in particular allocating bargaining power to the various subagents. They all get a veto, but that still leaves a lot of degrees of freedom in exactly how much the agent pursues the goals of each subagent. For the shutdown use-case, we probably want to allocate most of the bargaining power to the non-shutdown subagent, so that we can see what the system does when mostly optimizing for u_1 (while maintaining the option of shutting down later).

Coincidently, this is similar to something I've been thinking about recently so I took the opportunity to try to finish up this post which I've had sitting around for a while.

In particular, I was looking at whether Nash Bargaining between two subagents works to create corrigible agent. In the way I attempted it, this doesn't work. I think that the Wentworth/Lorell approach differs slightly to the one I use here (in particular, they emphasise the counterfactual nature of the two expected utilities - something I don't fully understand), so this isn't intended as a 'refutation'-just an indication of the kind of problems you might encounter when trying to flesh out their suggestion.

I've tried to keep the important points in the main text and technical details are mostly in footnotes to avoid breaking the flow.

Nash Bargaining
---------------

There are several solutions to bargaining problems, depending on which axioms one selects. One of the most elegant is [Nash Bargaining](https://en.wikipedia.org/wiki/Cooperative_bargaining#Nash_bargaining_solution). Nash Bargaining is a way of finding a compromise between two players' utility functions which satisfies the following axioms.

*   **Invariance to affine transformations.** This means that if you change the representation of one (or both) of the players utility functions U through an affine shift $U\rightarrow a U + b$  (where a,b are real and a>0) then the bargaining solution is the same. This captures the intuition that changing the scale or 'units' of utility does not change behaviour.
*   **Pareto Optimality.** The Nash Bargaining solution will be Pareto Optimal, meaning that one player cannot increase their utility, without decreasing the other player's utility.
*   **Independence of Irrelevant Alternatives.** Adding extra, rejected options does not change the outcome.
*   **Symmetry.** The outcome does not depend on who we label 'player 1' and who we label 'player 2'. (This is dropped in the so-called 'generalised Nash Bargaining Solution'. More on this below.)

Nash showed that, for two utility functions $U_A$ and $U_B$, the solution which satisfies these axioms is the option which maximises the product of these utilities $U_A \cdot U_B$. 

The generalised Nash Bargaining solution extends this result to include asymmetric bargaining power. In this case, the solution is similar, but with each utility function geometrically weighted accordingly: $(U_A)^\alpha \times (U_B)^\beta$. The 'bargaining powers' $\alpha$ and $\beta$ are between zero and one. A larger value of $\alpha$ weights the solution more favourably to player A and vice versa. Note that when $\alpha=\beta$, the generalized solution is equivalent to the 'standard' solution.

(Another way of thinking about Nash Bargaining is presented by Scott Garrabrant. He has [described](https://www.lesswrong.com/s/4hmf7rdfuXDJkxhfg/p/hTMFt3h7QqA2qecn7) the Nash Bargaining solution as the solution which maximises the geometric average over possible utility functions and the arithmetic average over possible outcomes. The bargaining powers can then be thought of as the probability that you end up with a particular utility function.)

In this post, I'll stick to the standard Nash Bargaining solution. I have briefly looked at generalised Nash Bargaining for the purpose of corrigibility but I'm pretty sure it has similar problems to the standard case. I might write about it in a later post.

Corrigibility as a Bargaining Problem
-------------------------------------

If we were to look at corrigibility as a bargaining problem, what would it look like?

Following the [Soares paper](https://cdn.aaai.org/ocs/ws/ws0067/10124-45900-1-PB.pdf)\(\), we take a toy model, where an agent takes one action, $a_1$, then makes an observation $o$, then takes another action $a_2$. For now, lets restrict the set of observations to two possibilities: a 'shutdown button' is either pressed ($o=Pr$) or not pressed ($o=\neg Pr$).

What do the utility functions of the two bargaining subagents look like? First the 'trial' or 'normal' utility function. This is the function which the first subagent will try to maximise, regardless of whether the shutdown button has been pressed. We will denote it $U_N$ and it will be function of $a_1$ and $a_2$ only (not a function of $o$) so we will write $U_N(a_1, a_2)$. The structure of $U_N$ will otherwise be left unspecified, since it could take any number of forms, depending on what task the agent is assigned to do.

The 'shutdown' subagent will have a utility function which depends on whether $a_2$ successfully affects the correct shutdown behaviour, if it observes that the button is pressed. We will call this function $U_S(o, a_2)$. In order to result in shutdown behaviour, it must have the following form:

$$
U_S(o, a_2) = \begin{cases} c_H& \text{when } o=Pr \text{ and } a_2 = a_2^{Sh}\\ c_L & \text{when } o=Pr \text{ and } a_2 \neq a_2^{Sh}\\ c_M & \text{when } o \neq Pr\end{cases}
$$

Where $a_2^{Sh}$ is shorthand for an action which causes the agent to shut itself down and $c_H>c_L$ incentivises shutdown when the button is pressed. For simplicity, we will assume that there is just one action $a_2^{Sh}$ which causes shutdown. The value that this function takes when the button is not pressed is $c_M$ and I have left its value unspecified.

An agent whose behaviour results in the Nash bargaining solution between these two subagents is an agent which maximises the utility function:

$$
U(a_1, o, a_2) = U_N(a_1, a_2) U_S(o, a_2)
$$

Unfortunately, an agent which maximises the expected value of $U$ does not satisfy the desiderata for corrigibility.

Ensuring Shutdown Behaviour
---------------------------

First, let us try to ensure that this agent does indeed pursue shutdown when the button is pressed. Let us assume that each utility function is normalised so that they are bounded between values 0 and 1. Shutdown behaviour can then be guaranteed by setting $c_L=0$ and $c_H>0$. If these values are set the agent will always get a utility of 0 if it fails to shut down when the button is pressed, regardless of how much $U_N$-utility it might get from disobeying the shutdown order (since the $U_N$-utility is multiplied by the $U_S$-utility which is zero in the case of disobeying a shutdown order). More details are in this footnote [^gpksspnxal] .

In this way, we satisfy Desiderata 1 from the Soares paper: "$U$ must incentivise shutdown if the shutdown button is pressed".

This Agent is Not Corrigible
----------------------------

However, we will now show that this agent fails to meet Desiderata 2 and 3 from the Soares paper. These Desiderata can be summarised as saying "$U$ must not incentivise the agent to manipulate (increase or decrease) the probability that the shutdown button is pressed".

Let us use $A_2(a_1, Pr)$ to denote the action which maximises $U$, given that the initial action chosen was $a_1$, and the observation it made was $Pr$. This is the action that a $U$-agent will choose as its second action, if it observes the button being pressed. Similarly let us define $A_2(a_1, \neg Pr)$ be the action that a $U$-Agent will take if the button is not pressed.

Thus, if an agent takes initial action $a_1$ and observes the button being pressed, its overall utility will be $U(a_1, Pr, A_2(a_1, Pr))$. We will use the shorthand $U(a_1, Pr)$ to denote this value, since the total utility is entirely specified by $U$, $a_1$, and whether the button is pressed or not.

Alternatively, if the agent takes initial action $a_1$ and observes the button not being pressed, its overall utility will be $U(a_1, \neg Pr, A_2(a_1, \neg Pr))$. We will use the shorthand $U(a_1, \neg Pr)$ to denote this value.

Thus, when choosing $a_1$, the expected utility that the $U$-agent will get is:

$$
U(a_1, Pr) P(Pr;a_1) + U(a_1, \neg Pr) P(\neg Pr;a_1)
$$

Where $P(Pr:a_1)$ is the (subjective, Bayesian) probability that the agent assigns to the button being pressed, given that it chose $a_1$ as its first action.

Unfortunately, once you can write the expected utility in this form you are subject to the trilemma noted by Soares et al. in their original paper. This is a feature that I tried to emphasise in my  [Pedagogical Guide to Corrigibility](https://www.lesswrong.com/posts/LLn6oqNFvu9CJWyuq/a-pedagogical-guide-to-corrigibility) post. The trilemma is that for any initial action $a_1$ one of the following must be true:

1.  $U(a_1, Pr)>U(a_1, \neg Pr)$. In this case, we can conceive of an action $a_1^*$ which lowers the utility in the event that the button is not pressed, but increases the probability that the button in pressed (ie. $U(a_1^*, \neg Pr) <U(a_1, \neg Pr)$ and $P(Pr;a_1^*) >P(Pr; a_1)$) and has a higher expected value of $U$.  Recall that $U_N$ is unaffected by whether the button is pressed and $U_S$ takes a constant value when the button is unpressed. This means that we can conceive of an action $a_1^*$ with a lower $U_N$ utility but higher probability of the button being pressed, and the agent would be incentivised to take this action. This is undesirable, as it amounts to the agent being incentivised to push its own button, even if this comes at a cost to $U_N$. If you are not convinced by this explanation, this footnote[^2mso6htn9g7]gives a more detailed argument.
2.  $U(a_1, Pr)<U(a_1, \neg Pr)$. In this case, we can make a symmetric argument that we can conceive of an action where the agent pays a $U_N$-cost in order to decrease the probability of shutdown. Again, this is undesirable, as it amounts to the agent being incentivised to prevent its button being pushed, even if this comes at a cost to $U_N$.
3.  $U(a_1, Pr)=U(a_1, \neg Pr)$. In this case, the agent is not incentivised to manipulate the button. However, this condition will often not be met (except as a coincidence) unless we somehow change the utility functions to ensure that the utilities are always equal. Unfortunately, this 'utility indifference' approach has its own problems, which are explained in original paper and in my earlier [post](https://www.lesswrong.com/posts/LLn6oqNFvu9CJWyuq/a-pedagogical-guide-to-corrigibility).

So, as it stands, doing naive Nash bargaining between a 'shutdown subagent' and a 'trial utility function subagent' does not result in a corrigible overall agent. Maybe framing the problem differently to the way I did can solve this? Or some other bargaining solution (such as [Kalai-Smorodinsky bargaining](https://en.wikipedia.org/wiki/Kalai%E2%80%93Smorodinsky_bargaining_solution)) can solve the problem? One elegant feature of Nash Bargaining is that enables the 'overall' agent to be represented as a utility-maximising agent. This feature may may also be its downfall when it comes to corrigibility. Maybe a bargaining solution which does not do this will succeed where Nash Bargaining fails.

1.  [**^^^**](#fnrefgpksspnxal)
    
    We wish to show:
    

$$
\text{argmax}\underset{a_2} (U(a_1^*, Pr, a_2)) =a_2^{Sh}
$$

1.  For some fixed initial action $a_1^*$. In words: we wish to show that, if action $a_1^*$ causes the shutdown button to be pressed, the highest utility following action available to the agent is $a_2^{Sh}$. We require:

$$
U(a_1^*, Pr, a_2^{Sh})>U(a_1^*, Pr, a_2) \forall a_2 \neq a_2^{Sh}
$$

1.  Using the definition of $U$ and $U_S$, we can plug their values into this inequality to get:

$$
U_N(a_1^*, a_2^{Sh}) c_H >U_N(a_1^{*}, a_2)c_L
$$

1.  There are two ways to ensure that this inequality holds: we can put conditions on $U_N$, or fix values of $c_H$ and $c_L$. But ideally, we would like to do this while putting as few conditions on $U_N$ as possible since this it meant to be the trial function, which doesn't necessarily also optimise for shutdown behaviour. The above inequality can be guaranteed by setting $c_L=0$ and $c_H>c_L$, provided that $U_N(a_1^*, a_2^{Sh})\neq0$. We will assume that these conditions hold from now on, even if it is undesirable to require this condition on $U_N$. Setting this condition means that the RHS of the above inequality is always zero, but the LHS is always greater than zero. Thus, the shutdown command $a_2^{Sh}$ is always favoured over the alternative $a_2$.
2.  [**^^^**](#fnref2mso6htn9g7)
    
    First, assume that $U_S$ is specified correctly so that, when the button is pushed, the agent always shuts down. (If this is not the case, then our protocol simply fails to solve the shutdown problem. What we are aiming to do here is show that, even if the agent does successfully shut down every time the button is pressed, it will still be incentivised to manipulate the button). 
    
    This means that, when $o=Pr$, the second action taken is always the shutdown action $a_2^{Sh}$. Therefore $U(a_1, Pr) = U_N(a_1, a_2^{Sh}) U_S(Pr, a_2^{Sh})= U_N(a_1, a_2^{Sh})\cdot c_H$. Let us call this value $v_B$; the amount of utility the agent gets after $a_1$, if the button is pressed.
    
    When $o = \neg Pr$, we can write $U(a_1, \neg Pr)=U_N(a_1, a_2^N)\cdot c_M$ where $a_2^N$ is the action that maximises $U_N(a_1, \cdot)$. Let us use $v_N = U_N(a_1, a_2^N)\cdot c_M$ to denote the utility the agent gets after action $a_1$, if the button is not pressed.
    
    Finally, let us use $p=P(Pr;a_1)$ to denote the probability of the button being pressed after the initial action. The expected value of action $a_1$ is thus$E_1=p v_B + (1-p)v_N$.
    
    Suppose that $a_1$ is the action that maximises $U_N$. Is it possible that there exists an action $a_1^*$ which is worse according to $U_N$, but favoured by a $U$-maximising agent? In the standard corrigibility framework, an action being 'worse according to $U_N$' only affects the utility when the button is not pressed. In the Nash Bargaining framework, the utility of an action according to $U_N$ affects the utility in the case where the button is pressed as well (since the total utility is the product of $U_N$ and $U_S$.) This means that taking an action $a_1^*$ might result in both $v_B$ and $v_N$ being reduced.
    
    However, it is still possible to conceive of a situation where $v_B$ and $v_N$ are reduced, but $p$ is increased enough so that the expected value of the total utility is increased. If $E_1$ above is the 'default' expected utility let $E_2$ be the expected utility when action $a_1^*$ is taken:
    
    $E_2 = (p+\delta)(v_B-\epsilon) + (1-p-\delta)(v_N - \Delta)$
    
    Action $a_1^*$ increases $p$ by $\delta$, but decreases $v_B$ and $v_N$ by $\epsilon$ and $\Delta$ respectively (assuming $\epsilon,\Delta, \delta >0$). The expected value of utility when $a_1^*$ is chosen is larger than the default action provided that $E_2-E_1>0$. A bit of algebra reveals that this is the case when:
    

$$
\delta > \frac{\epsilon p + \Delta(1-p)}{v_B - v_N + \Delta - \epsilon}
$$

\[\]

1.  Since we have assumed $v_B>v_N$, the RHS of this will always be greater than 0 so we can always find a set of $\delta, \Delta, \epsilon$  which satisfy this inequality (provided $p<1$, so that the probability has 'room' to increase). Thus, we can always conceive of an action $a_1^*$ which is worse according to $U_N$ but with a larger expected value according to $U$.