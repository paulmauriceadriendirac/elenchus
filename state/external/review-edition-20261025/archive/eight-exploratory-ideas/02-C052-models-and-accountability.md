# What an accountability model must preserve

**Candidate C052 · Development draft · 22 October 2026**

**Originality verdict:** Preserving strategic ability under abstraction is established technical work. A narrower philosophical argument about the evidential burden of using a model to blame someone remains worth testing. The example below is an illustration, not a new theorem.

## The change of question

A model can answer “What intervention would have prevented this outcome?” without answering “Could this person reasonably have performed that intervention?” This distinction matters whenever an organization converts a useful explanation of failure into a judgment against a particular person.

It is tempting to announce that causal abstraction therefore needs a new requirement to preserve responsibility. That announcement would be premature. Beckers and Halpern's *Abstracting Causal Models* (2019) already distinguishes demanding forms of abstraction by what they preserve. A separate technical literature explicitly models agents' actions and information. Belardinelli and Lomuscio (2017), for example, define uniform strategies over an agent's local states and develop abstractions for strategic claims under imperfect information. A requirement to preserve agent-specific abilities is not an untouched idea.

The philosophical question is instead one of permitted inference: what must an institution establish before treating the success of a causal model as evidence of an individual's culpable failure?

## A small example

A technician must choose either the left or the right switch. Exactly one prevents a shutdown. A hidden configuration determines which one. The technician's display looks identical in both configurations, and there is no available test before the deadline. There are no relevant earlier opportunities to improve the display, no negligence in becoming ignorant, and no independent duty to choose one side rather than the other.

In configuration L, choosing left prevents the shutdown. In configuration R, choosing right does. A retrospective investigation identifies the actual configuration and correctly concludes that the other action would have prevented the actual failure.

The investigation has identified a successful counterfactual intervention. It has not shown that the technician had an information-sensitive way of selecting it. Every configuration admits a successful action; no single action succeeds across the configurations the technician cannot distinguish. Those statements differ in the order of “for every configuration” and “there is an action.” That elementary distinction is familiar, and the uniform-strategy requirement in the cited technical work formalizes the relevant constraint.

Now compare a second workplace. Its physical switch mechanism and intervention responses are identical, but the technician has a reliable display of the configuration. The intervention table alone is unchanged; the person's capacity to choose appropriately is different. A model omitting the display might remain excellent for redesigning the mechanism. Its adequacy for that purpose does not establish its adequacy for a finding of knowing or negligent noncompliance.

Neither example proves that alternative possibilities are necessary for every kind of moral responsibility. Nor does lack of a guaranteed strategy automatically excuse risky conduct. The examples isolate one particular accusation: that the person culpably failed to choose the known effective intervention. That accusation requires facts the intervention table does not supply.

## A proposed rule for institutional use

An institution invoking a model to support a specified accusation should identify the normative premises of that accusation and show that the evidence preserves or independently establishes the facts those premises require. A model that establishes physical preventability cannot silently acquire the missing premise that this agent could recognize and execute the preventive action.

This requirement is deliberately local. A model need not contain a complete theory of responsibility. If the accusation concerns a technician's failure to follow an intelligible warning, the institution needs evidence about access to the warning and capacity to act on it. If the accusation concerns negligent maintenance of the warning system, the relevant agent and time shift. If it concerns strict liability rather than fault, the argument must say so instead of borrowing the rhetoric of culpability.

The duty also concerns who bears uncertainty. Suppose the organization designed the display, kept the configuration records, and later destroyed the records of what the technician could see. It should not infer adequate awareness simply because its remaining model explains the physical mechanism. Whether destruction warrants a stronger presumption against the organization requires an additional argument about evidence and fairness; this draft does not smuggle that conclusion into the definition of abstraction.

## Why this is more than asking for a bigger model

The proposal does not demand maximal detail. It asks the institution to state the claim for which the model is evidence. An abstraction that omits personal information might be preferable for planning repairs and unsuitable for assigning individual fault. The same omission can thus be harmless or decisive depending on the conclusion drawn.

This is also why successful validation on predictions is not a universal certificate. Predictive accuracy supports predictions in the tested domain. It does not by itself validate an inference that depends on an omitted informational or normative relation. There may be no predictive error to expose: the error can occur when the institution changes its question without changing its evidential warrant.

## The originality test

The technical ingredients are inherited. The remaining possibility is an account of institutional responsibility for transferring a model between explanatory and accusatory purposes, including how the burden of establishing adequacy should be allocated. That could matter for automated workplace discipline and accident investigation, but a new application is not enough for a contest contribution.

A serious next draft must compare this proposal with existing work on model adequacy, epistemic conditions of responsibility, and evidential burdens. It must find a disputed case on which the proposed allocation changes a defensible verdict. If it merely restates “use a model appropriate to the question,” the idea should be rejected as too general. This audit therefore demotes its earlier priority rather than dressing the familiar technical distinction as an original formal result.

### References and access

- Beckers, Sander, and Joseph Y. Halpern. 2019. “Abstracting Causal Models.” *AAAI*. https://www.cs.cornell.edu/home/halpern/papers/abstraction.pdf. Relevant definitions and examples read; not every proof independently checked.
- Belardinelli, Francesco, and Alessio Lomuscio. 2017. “Agent-based Abstractions for Verifying Alternating-time Temporal Logic with Imperfect Information.” *AAMAS*, pp. 1259–1267. https://www.doc.ic.ac.uk/~fbelard/Documents/aamas2017c.pdf. Definitions 1–4 and account of the abstraction result read; proof not independently verified.
- Jamroga, Wojciech, and Yan Kim. 2023. “Practical Abstraction for Model Checking of Multi-Agent Systems.” *KR*, pp. 384–394. https://proceedings.kr.org/2023/38/kr2023-0038-jamroga-et-al.pdf. Introduction and related-work map used to locate the closer 2017 source.

