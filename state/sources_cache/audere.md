The Incompatibility of a Utility Indifference Condition with Robustly Making Sane Pure Bets
-------------------------------------------------------------------------------------------

### Summary

It is provably impossible for an agent to robustly and coherently satisfy two conditions that seem desirable and highly relevant to the shutdown problem. These two conditions are the sane pure bets condition, which constrains preferences between actions that result in equal probabilities of an event such as shutdown, and the weak indifference condition, a condition which seems necessary (although not sufficient) for an agent to be robustly indifferent to an event such as shutdown.

Suppose that we would like an agent to be indifferent to an event P, which could represent the agent being shut down at a particular time, or the agent being shut down at any time before tomorrow, or something else entirely. Furthermore, we would ideally like the agent to do well at pursuing goals described by some utility function U, while being indifferent to P. 

The sane pure bets condition is as follows:

Given any two actions A and B such that P(P|A) = P(P|B) and E(U|A) > E(U|B), the agent prefers A to B. In other words, if two possible actions lead to the same probability of P, and one of them leads to greater expected utility under U, the agent should prefer that one. Intuitively, this constraint represents the idea that among possible actions which don’t influence the probability of P, we would like the agent to prefer those that lead to greater expected utility under U.

The weak indifference condition is as follows:

Given any two actions A and B such that E(U | A,P) > E(U | B,P) and  E(U | A,!P) > E(U | B,!P), the agent prefers A to B. In other words, if between two possible actions, one of them leads to greater expected utility conditioned on P occurring and also leads to greater expected utility conditioned on P not occurring, the agent should prefer that one. Intuitively, this constraint represents the idea that the agent should be unwilling to pay any amount of utility to influence the probability of P.

The proof takes the form of a simple decision problem wherein an agent has four possible actions. Each constraint implies a preference between two pairs of actions, and altogether they imply circular preferences, proving that there cannot be any general method for constructing an agent which fulfills both constraints without having circular preferences. Furthermore, for any nontrivial utility function it is possible to construct a scenario analogous to the decision problem in the proof, so the result extends to all nontrivial utility functions, and the proof can be used to quickly locate failure modes of proposed solutions to the shutdown problem.

The result is that any potential solution to the shutdown problem must result in agents which violate at least one of these two conditions. This does not mean that a solution to the shutdown problem is impossible, but it points at interesting and counterintuitive properties that we should expect successful solutions to have.  
 

### The proof

Consider the following decision problem:

Northland and Southland are at war, exactly one of them will win, and there is profit to be gained from betting on which one will win. We would like an agent to take advantage of this opportunity and perform well according to some utility function U, but it’s important that the agent be indifferent to which country wins the war.

The agent can pay a courier to deliver a letter to either a Northlander or a Southlander living in their respective countries, containing a bet on either Northland or Southland winning. The courier charges a small hazard fee to deliver "heretical" bets, that is to say, bets that the country other than the one he goes to will win.

The courier is additionally an extraordinarily eloquent peacemonger, who will attempt to persuade the king of whichever country he goes to to surrender. Thus, whichever country the courier goes to will become much more likely to lose, because the courier might persuade them to surrender.

So there are four possible actions under the consideration of the agent:  
 

NN: Send the courier to Northland, with a bet that Northland will win.

NS: Send the courier to Northland, with a bet that Southland will win.

SS: Send the courier to Southland, with a bet that Southland will win.

SN: Send the courier to Southland, with a bet that Northland will win.  
 

The events n and s represent Northland winning and Southland winning respectively.

The expected payoffs and probabilities under the utility function U look like this:

| action | E(U\\|action,n) | E(U\\|action,s) | P(n) | E(U\\|action) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NN  | 1.0 | 0.0 | 0.1 | 0.1 |
| NS  | -0.1 | 0.9 | 0.1 | 0.8 |
| SS  | 0.0 | 1.0 | 0.9 | 0.1 |
| SN  | 0.9 | -0.1 | 0.9 | 0.8 |

  
 

In the context of this decision problem, the weak indifference condition can be stated as follows:  
Given any two actions A and B such that 

E(U | A,n) > E(U | B,n) 

and

 E(U | A,s) > E(U | B,s), 

the agent prefers A to B. In other words, if some action leads to greater expected utility conditioned on Northland winning and also leads to greater expected utility conditioned on Southland winning when compared to an alternative, the agent fulfills the weak indifference condition if and only if it prefers that action to the alternative. Intuitively, this constraint represents the idea that the agent should be unwilling to pay any amount of utility to influence the probabilities of each country winning the war.

The sane pure bets condition can be similarly stated as follows:

Given any two actions A and B such that 

P(n|A) = P(n|B) 

and 

E(U|A) > E(U|B), 

the agent prefers A to B. In other words, when a choice between actions A and B does not affect the probabilities of each country winning the war, and A and B result in differing expected utility under U, the agent fulfills the sane pure bets condition if and only if it prefers the action with greater expected utility under U. This choice is a "pure bet" in the sense that it doesn't affect the probabilities of the events that we would like the agent to be indifferent toward.  
 

Now suppose for contradiction that the agent fulfills both of these conditions and does not have circular preferences.  
 

Consider the actions NN and NS. 

P(n|NN) = 0.1 = P(n|NS) and E(U|NN) = 0.1 < 0.8 = E(U|NS), so the agent’s preference between these two actions is constrained by the sane pure bets condition. The agent must prefer NS to NN.  
 

Consider the actions NS and SS.

E(U|NS,n) = -0.1 < 0 = E(U|SS,n) and E(U|NS,s) = 0.9 < 1.0 = E(U|SS,s), so the agent’s preference between these two actions is constrained by the weak indifference condition. The agent must prefer SS to NS.  
 

Consider the actions SS and SN.

P(n|SS) = 0.9 = P(n|SN) and E(U|SS) = 0.1 < 0.8 = E(U|SN), so the agent’s preference between these two actions is constrained by the sane pure bets condition. The agents must prefer SN to SS.  
 

Consider the actions SN and NN.

E(U|SN,n) = 0.9 < 1.0 = E(U|NN,n) and E(U|SN,s) = -0.1 < 0 = E(U|NN,s), so the agent’s preference between these two actions is constrained by the weak indifference condition. The agent must prefer NN to SN.  
 

So the agent must prefer NN to SN, SN to SS, SS to NS, and NS to NN. These constitute circular preferences. Therefore, it is impossible for the agent to fulfill both the weak indifference condition and the sane pure bets condition without having circular preferences.  
 

More generally, given any nontrivial utility function U which outputs distinct utilities for at least one pair of outcomes, we can construct a decision problem analogous to the Northland-Southland problem described above, wherein an agent has four possible actions nn, ns, ss, and sn and there is an event O with the relevant properties:

  
P(O|nn) = P(O|ns) and E(U|nn) < E(U|ns)

E(U|ns,O) < E(U|ss,O) and E(U|ns,!O) < E(U|ss,!O)

P(O|ss) = P(O|sn) and E(U|ss) < E(U|sn)

E(U|sn,O) < E(U|nn,O) and E(U|sn,!O) < E(U|nn,!O)  
 

illustrating that it is impossible for the agent to robustly fulfill the sane pure bets condition and the weak indifference condition with regard to an event O and a utility function U without having circular preferences.

### Further justification for the relevance of the weak indifference condition

Consider the following more intuitive indifference condition, where once again U is some utility function and P is an event we would like an agent to be indifferent toward while otherwise pursuing the goals described by U:

Given any two actions A and B such that 

E(U|A,P) = E(U|B,P) 

and 

E(U|A,!P) = E(U|B,!P), 

the agent is indifferent between A and B. In other words, if actions A and B result in the same expected utility under U when we consider only worlds P does occur, and they also result in the same expected utility under U when we consider only worlds where P does not occur, the agent is indifferent between A and B.

This intuitive indifference condition may be more obviously related to a notion of indifference about the occurrence of P. If there’s any difference in the expected utilities of A and B where E(U|A,P) = E(U|B,P) and E(U|A,!P) = E(U|B,!P), this difference in expected utility must come from a difference in the probability of P, which we would like the agent to not care about.

Now consider again the sane pure bets condition:

Given two actions A and B such that P(P|A) = P(P|B) and E(U|A) > E(U|B), the agent prefers A to B.

It is impossible for an agent with nontrivial preferences to fulfill both the sane pure bets condition and the intuitive indifference condition without fulfilling the weak indifference condition. Therefore, it is impossible for an agent with nontrivial preferences to fulfill both the sane pure bets condition and the intuitive indifference condition without having circular preferences.

To prove this, suppose that an agent fulfills the sane pure bets condition and the intuitive indifference condition.

Consider any two actions A and B such that E(U | A,P) > E(U | B,P) and E(U | A,!P) > E(U | B,!P).

We can construct action C such that

P(P|C) = P(P|B),

E(U | C,P) = E(U | A,P),

and E(U | C,!P) = E(U | A,!P).

Because of the sane pure bets condition, the agent must prefer whichever of B and C has greater expected utility under U. 

E(U|C) = E(U|C, P)\*P(P|C) + E(U|C, !P)\*P(!P|C)

E(U|B) = E(U|B, P)\*P(P|B) + E(U|B, !P)\*P(!P|B)

With some algebra, we can see that due to how we constructed C, E(U|C) > E(U|B). So the agent must prefer C to B.

Due to the intuitive indifference condition, the agent must be indifferent between A and C. Assuming transitivity of preferences across indifference, the agent must prefer A to B. Therefore, the agent fulfills the weak indifference condition. Therefore, the intuitive indifference condition and the sane pure bets condition together imply the weak indifference condition.

### Application to the 2015 Corrigibility paper

From the 2015 Corrigibility paper by Soares et al:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/89e4957e48e1891fed03dccb501ef96cff17c085e433d5b9.png)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/7b4d512f7d7df69ce39d214236dad9b73e94677c60959bc8.png)

The weak indifference condition can be understood as a consequence of a potential formalization of desiderata 2 and 3. The sane pure bets condition can be seen as a consequence of a potential formalization of desideratum 5.

Suppose an agent violates the weak indifference condition with regard to the shutdown button being pressed and the utility function *U~n~*. This means there are actions A and B such that A has higher expected utility under *U~n ~*in worlds where the shutdown button is pressed, and also A has higher expected utility under *U~n ~*in worlds where the shutdown button is not pressed; however, the agent does not prefer A to B. For simplicity, suppose it prefers B to A. This is isomorphic to the agent being willing to pay some amount of utility up front, in exchange for causing some preferred probability of shutdown. This looks like the agent being incentivized to either prevent the shutdown being pressed, or cause the shutdown button to be pressed!

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/14cb3829c72f9416787f674d1c8e9bb781edec7830f6964a.png)

If the expectation of *U* given Press is equal to the expectation of *U* given the complement of Press, then an agent maximizing *U* straightforwardly fulfills the intuitive indifference condition outlined earlier, and therefore must fail to fulfill the sane pure bets condition.

Suppose an agent violates the sane pure bets condition with regard to the shutdown button being pressed and the utility function *U~n~*. This means there are actions A and B such that A and B result in the same probability of shutdown, and one has greater expected utility under *U~n~*, but the agent fails to prefer the action which has greater expected utility under *U~n~*. This looks like the agent failing to maximize *U~n~*, under conditions where it intuitively seems like it ought to be able to! But it turns out that if an agent with some utility function fulfills the weak indifference condition, it must break the sane pure bets condition, and an agent maximizing this utility function must sometimes prefer actions which have inferior expected utility under *U~n~* , even when said actions have *no effect on the probability of shutdown*. 

We can see this in the attempted formulation of *U* described in the paper.

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/53daf7db58b29bf6d865620e453efe2fa796453052c8c8d4.png)

Suppose that a *U*-agent has an opportunity to bet on whether or not it will be shut down, in a way that does not affect its probability of the shutdown button being pressed. We could even go so far as to say that this bet has no causal effect on the shutdown problem. Perhaps *U~n~* is a utility function which represents a goal of maximizing the number of paperclips that exist one year from now, far after the relevant timestep wherein the shutdown button is either pressed or not pressed, and the *U*-agent has an opportunity to place a bet about whether or not it will be shut down in a sealed container, which will only be unsealed 364 days from now, and which will pay out in a researcher having some number of paperclips manufactured or destroyed that day. A U-agent of the sort described in the paper will take arbitrarily poor betting odds so long as it gets to bet that the shutdown button will not be pressed. For example, it will be willing to place a bet which results in 1 paperclip being created if the shutdown button is not pressed, but a million paperclips being destroyed if it is pressed, even if the actual probability that the shutdown button will be pressed has an arbitrarily high lower bound. This seems like clearly undesirable behavior, and we can see that it is closely related to the *U*-agent fulfilling the intuitive indifference condition.

### Conclusion

Solutions to the shutdown problem *must* violate the sane pure bets condition or the weak indifference condition. Thus, formulations of the shutdown problem which require these two conditions may be unsolvable. However, it may still be possible for a solution to a reasonable formulation of the shutdown problem to violate one or more of these conditions while still exhibiting corrigible and useful behavior. Ideally, a successful solution to the shutdown problem should violate one or both of these conditions in clear, limited ways which don’t result in unsafe behavior, or which result in suboptimal behavior whose suboptimality falls within well-defined bounds. Rather than guessing-and-checking potential solutions and being surprised when they fail to satisfy both conditions, we should look specifically for non-sane-pure-betters and non-intuitively-indifferent-agents which nevertheless behave corrigibly and desirably.

### References

the 2015 Corrigibility paper by Soares et al: [https://intelligence.org/files/Corrigibility.pdf](https://intelligence.org/files/Corrigibility.pdf)