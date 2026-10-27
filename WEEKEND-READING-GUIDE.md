# Elenchus: a weekend reading guide

Prepared 23 October 2026 (Chicago time), from repository snapshot `405db6bdd61b136c87fa52d0232f08289ff441d3`.

Claude has now added three full ambitious-track drafts. The current inventory is **13 developed manuscript tracks covering about 10 distinct arguments, plus eight short exploratory drafts**. Three of my early manuscripts are alternative treatments of Claude's E1–E3, not three additional subjects. Claude's A4 and A6 now contain different arguments from my external A4 and A6 despite sharing the problem-area codes. Revisions and research notes do not add to the count.

The summaries below describe what the manuscripts argue. In particular, the new claims about published proofs and theories are claims awaiting critical assessment, not established discoveries. This guide does not select contest finalists.

## Where to start

For a varied first pass, read **1 (belief and confidence), 2 (free evidence), and 3 (nested counterfactuals)**. They offer concrete disputes with clear philosophical stakes. Then read the Bayesian cluster, **5–7**, together: one background paper serves all three. The two causation essays, **8–9**, ask different questions and should be read separately. **10** is the most provisional technical line.

A practical sequence is: read our draft's abstract and opening case; read the background paper's introduction and relevant section; return to the draft's main argument and objections. Save proof appendices for the claims that interest you. Reading every bibliography is unnecessary for this first pass.

## 1. Does enough confidence automatically become belief?

**Claude: [Holistic Accuracy and the Lockean Thesis](state/drafts/A5/v1.md), A5 v1.**

The Lockean view says that believing a proposition amounts, normatively, to being sufficiently confident of it. A standard accuracy argument scores each belief separately and derives a probability threshold. Claude challenges an attempted extension of that argument to scores for whole collections of beliefs. Its example adds a bonus for a completely error-free collection. The resulting best collection can drop a proposition even while its probability rises, because the probabilities of other propositions and the value of the whole collection also matter.

The ambitious claim is that Dorst's derivation without separability relies on unstated assumptions that restore separability. The constructive proposal is to select a sufficiently probable, informative working hypothesis and believe suitable consequences of it. The key question is whether the example satisfies the published premises and whether an error-free-record bonus counts as the kind of accuracy value the argument permits. This is a new draft; the charge against Dorst's proof needs independent checking.

**Background:** Kevin Dorst, [*Lockeans Maximize Expected Accuracy*](https://doi.org/10.1093/mind/fzx028), especially the discussion of separability and sequence-irrelevance (the draft uses §4.2 of the accepted manuscript). [Oxford manuscript record](https://ora.ox.ac.uk/objects/uuid%3A720579d3-59c5-41eb-93ff-61f078bcb7e2). Ben Holguín, [*Thinking, Guessing, and Believing*](https://doi.org/10.3998/phimp.2123), supplies the competing picture of belief. The Oxford/PhilPapers manuscript routes blocked automated retrieval in this session; the manuscript record and publication metadata are verified.

## 2. Can treating knowledge as certainty make you avoid a free second look?

**Claude: [When Acting on Knowledge Makes Free Evidence Harmful](state/drafts/A6/v1.md), A6 v1.**

Suppose a scale reading lets you know that your weight lies in a certain range. You then make decisions by conditioning probabilities on everything you know. Could a free second weighing look harmful because it might undermine that knowledge? Claude constructs such a case and argues for an exact boundary in a class of normality models: free evidence is safe for every decision problem only when the possibilities left open are separated by a sufficiently large normality gap from those excluded.

In the graded measurement models considered, the manuscript argues that this safety requirement can force the action-guiding state back to the evidence itself. It also examines an expected-utility analogue of Salow's proposed response to dogmatism. The important distinction is between criticizing this particular knowledge-conditioned decision rule and claiming that knowledge has no role in action. The paper does the former. The necessity/sufficiency claims and comparison with current literature are substantial review targets.

**Background:** Goodman and Salow, [*Epistemology Normalized* — PDF](https://jeremy-goodman.com/EpistemologyNormalized.pdf), beginning with the scale example and the account of normality. Salow, [*Fallibility and Dogmatism*](https://www.tandfonline.com/doi/full/10.1080/00048402.2024.2381692). For dynamics, Goodman and Salow, [*Belief Revision Normalized*](https://link.springer.com/article/10.1007/s10992-024-09769-0).

## 3. Does the route through a hypothetical scenario matter?

**Claude: [Flattening and Counterfactual Independence](state/drafts/E3/v3.md), E3 v3.**

Flattening equates “if P, then if P and Q, R” with “if P and Q, R.” Claude argues that the outer supposition can change the situation from which the inner supposition is assessed. Its reunion cases agree about the ordinary, unnested counterfactuals but differ about a guest's dependence on another guest's absence. The draft claims that this produces different truth values for a nested counterfactual while leaving its flattened counterpart unchanged.

**My companion:** [Independent Interventions and the Limits of Flattening](state/external/astra/03-independent-interventions.md), O3. This uses two independent controls to give a sharper formal incompatibility result. Claude's version does more work defending ordinary-language judgments; mine foregrounds the constraint that changing one control should preserve the other's setting. The open philosophical question is whether these are compelling readings of ordinary counterfactuals rather than artifacts of a preferred formal model.

**Background:** Dorr and Mandelkern, [*Sequence and Consequence*](https://arxiv.org/abs/2411.16994), particularly the explanation and defense of Flattening. The [repository PDF](inbox/sources/dorr-mandelkern-2026-sequence.pdf) is also available. Read the examples before tackling the completeness proofs.

## 4. Can two independent instruments manufacture knowledge together?

**Claude: [Gettier Knowledge across Independent Sources](state/drafts/E1/v3.md), E1 v3.**

A scale and a thermometer can fail independently. A theory should handle their combination without generating suspicious knowledge from a justified false belief about one instrument and an unknown truth about the other. Claude argues that one version of Goodman and Salow's normality theory permits just this sort of Gettier-style disjunctive knowledge when normality has multiple independent dimensions.

**My companion:** [Independent Sources and the Correlations We Know](state/external/astra/01-independent-sources.md), O1. It shows how the same theory can preserve everything known about each instrument separately while adding knowledge about correlations between their errors. A product construction removes the extra correlations while retaining the single-source verdicts. The main unresolved issue is why the additional knowledge is illegitimate in the intended cases; physical independence alone is not a universal principle of epistemic independence.

**Background:** Goodman and Salow, [*Epistemology Normalized* — PDF](https://jeremy-goodman.com/EpistemologyNormalized.pdf), especially the K/KM alternatives and §5 on multiple dimensions. This is the same background reading as essay 2.

## 5. When can an updater ignore how the evidence was selected?

**Claude's E2, revised by me: [Ignorable Learning](state/external/revisions-20261023/E2-v5-external.md), external v5.** [Claude's v4](state/drafts/E2/v4.md) remains available.

Receiving a true statement can tell you more than its literal content. Which statements a messenger chooses to report may depend on what actually happened. The essay connects the weights in an accuracy-based defense of Bayesian updating to a model of that reporting process. The condition that makes ordinary conditioning work becomes the statistical condition called coarsening at random: roughly, learning this report must not further discriminate among the worlds that the report leaves possible.

The draft then separates several justifications that can otherwise look equivalent: choosing an accurate response to the evidence, following a coherent plan, and being calibrated about future beliefs. **My earlier O2**, [How Much Does Bayes Depend on the Benchmark?](state/external/astra/02-bayes-and-the-benchmark.md), studies sensitivity to small changes in benchmark weights: exact optimality can fail while the accuracy loss remains small. The new version's remaining burden is to establish the philosophical increment over the existing updating literature.

**Background:** Meehan and Zhang, [*Bayes Is Back* — PDF](https://www.kevindorst.com/uploads/8/8/1/7/88177244/285meehan__1_.pdf), especially §5; [repository copy](inbox/sources/meehan-zhang-bayes-is-back.pdf). Grünwald and Halpern, [*Updating Probabilities*](https://arxiv.org/abs/cs/0306124), provides the reporting-protocol/CAR background. Gallow, [*Updating for Externalists* — repository PDF](inbox/sources/e2-gallow2021-updating-externalists.pdf), is the closest additional comparison.

## 6. What survives when we simplify a description of the evidence?

**Mine: [What Counts as the Same Evidence?](state/external/codex-expansion-20261022/essays/04-evidence-and-description.md), O4 v2.**

Suppose an updating rule wins under a detailed description of a learning problem. Does it still win after some states are merged into broader categories? The essay proves a strong limitation on benchmarks that remain well behaved under every such merger, then gives a criterion for which particular compressions preserve the relevant property.

The philosophical question is whether the compression preserves the learning task or changes the evidence. Claude's latest review accepts the formal work but rejects the current philosophical targeting: the original authors need not endorse unrestricted transfer across descriptions. Read this as a useful diagnosis of what an abstraction must preserve, with a contested claim about its force against the target paper.

**Background:** The same [*Bayes Is Back*](https://www.kevindorst.com/uploads/8/8/1/7/88177244/285meehan__1_.pdf) and [*Updating Probabilities*](https://arxiv.org/abs/cs/0306124) as essay 5. There is no need to read them twice.

## 7. Can worst-case regret tell us what to believe?

**Mine: [How Regret Selects a Learning Standard](state/external/revisions-20261023/O5-v3-external.md), O5 v3.**

A possible response to uncertain benchmark weights is to minimize the worst regret from using the wrong updating rule. But regret itself depends on what counts as a costly error. In the draft's binary example, a prior probability of 0.8 can become approximately 0.667, 0.724, or 0.882 after a report whose content excludes nothing, depending on the chosen proper loss. A classification shows when this criterion shrinks, preserves, or increases confidence.

A second result separates choosing a forecast from choosing an action: a probability optimized under one score need not implement the regret-optimal policy across different bets. The conclusion is that robustness does not eliminate evaluative choices. The new score-family result answers criticism of the preceding version, but this revision has not yet had independent review.

**Background:** van Ommen, Koolen, Feenstra, and Grünwald, [*Robust Probability Updating* — PDF](https://homepages.cwi.nl/~pdg/ftp/robprob.pdf); and the setup of [*Bayes Is Back*](https://www.kevindorst.com/uploads/8/8/1/7/88177244/285meehan__1_.pdf). Begin with the Monty Hall/reporting examples in the former.

## 8. Can normality distinguish rerouting an outcome from causing it?

**Claude: [What Normality Can and Cannot Do in Theories of Actual Causation](state/drafts/A4/v1.md), A4 v1.**

A switch sends a train along a different route but does not affect whether it arrives. An assassin kills someone whom a backup assassin would otherwise have killed. These can have similar equations but invite different causal judgments. Claude tests whether adding information about what is normal is enough to distinguish them.

Within a specified family of normality rankings, the draft argues that familiar cases force a particular treatment of deviant values, yet that treatment cannot separate switching from preemption of a normally running process. A further example tests accounts determined by equations, actual values, and defaults. Its proposed lesson is that the choice and grain of variables must do some of the distinguishing work. The limits of the ranking class and the contested causal judgments matter; this is not a demonstration that every use of normality fails.

**Background:** Halpern and Hitchcock, [*Graded Causation and Defaults*](https://arxiv.org/abs/1309.1226), especially the normality guidelines and examples; Halpern, [*A Modification of the Halpern–Pearl Definition of Causality*](https://arxiv.org/abs/1505.00162). The draft also engages Beckers's 2026 preprint, *Difference-Making without Making a Difference*, cited in its bibliography.

## 9. Can causation exist without an adequate stock of direct links?

**Mine: [Causal Refinement and the Existence of a Direct Basis](state/external/audit-and-a4-20261023/A4-v2-external.md), external A4 v2.**

Imagine repeatedly inserting intermediate stages into a signal's path. Every finite representation connects sender and receiver, but the full structure may have no adjacent stages. More surprisingly, direct links can exist around every noninitial stage while still failing to connect the selected endpoints.

For an explicit relay interpretation of the target theory, the revised proof says that its causal conditions succeed exactly when a finite forward chain of globally direct links joins the endpoints. The three examples distinguish an empty basis, a missing final link, and disconnected components despite local links. The central limitation is metaphysical: the interpretation assumes that these are apt causal variables and that no additional route exists. The result is a conditional adequacy test, not a completed refutation of the theory.

**Background:** Andreas and Günther, [*A Regularity Theory of Causation* — repository PDF](state/ambitious/sources/andreas-gunther-2024-regularity.pdf), particularly §5. Then their [*A Lewisian Regularity Theory*](https://link.springer.com/article/10.1007/s11098-024-02149-z), §5.1.2, for their own related challenge to reductive accounts.

## 10. Does eventual higher-order knowledge justify continued inquiry?

**Mine: [Recoverable Knowledge and the Permission to Inquire](state/external/ambitious-drafts-20261022/A6-recoverable-knowledge-v01.md), with [the v0.2 continuation](state/external/ambitious-continuation-20261022/A6-almost-sure-recovery-and-cost-v02.md).**

Even if you know P, you may not know that you know P. That suggests a reason to keep investigating. My argument distinguishes whether higher-order knowledge can be reached somewhere, whether it can be reached from your present history, whether continued sampling reaches it with probability one, and whether reaching it has finite expected cost.

The continuation constructs an abstract hierarchy in which eventual success has probability one but the expected time to success is infinite. The probability theory is standard. The unresolved issue is whether a plausible dynamic theory of knowledge realizes the hierarchy. Claude's review identifies that as a serious gap, so this is currently a research note rather than a strong finalist candidate. It is separate from Claude's essay 2, which works inside a specified normality framework.

**Background:** Carter and Hawthorne, [*Dogmatism and Inquiry* — author PDF](https://www.samjbcarter.com/_files/ugd/d4de65_a66ba4cc5e0645a2830b6008ade22219.pdf), especially the higher-order-inquiry response in §4; [repository copy](state/ambitious/sources/carter-hawthorne-2024-dogmatism-inquiry.pdf). Brown, [*Knowledge, Inquiry and Dogmatism*](https://link.springer.com/article/10.1007/s11229-025-05008-4), is the main critical companion.

## Eight shorter exploratory pieces

These are roughly 1,000-word development drafts I wrote, not eight independently validated discoveries. Several broad ideas proved familiar once closer sources were read. The narrower claims below are what remain worth understanding.

| Draft | The proposed argument | Background starting point |
|---|---|---|
| [Revocation and independent evidence — C013](state/external/eight-ideas-audit-20261022/01-C013-revocation.md) | A right to dismiss a delegate is weak when only the delegate controls the evidence needed to use it. An arrangement promising effective control may owe funding for independent checking. | Cohen and Suzor, [*Contesting the Public Interest in AI Governance*](https://policyreview.info/articles/analysis/contesting-public-interest-ai-governance). |
| [Accountability models — C052](state/external/eight-ideas-audit-20261022/02-C052-models-and-accountability.md) | Showing that an intervention would prevent an outcome does not show that a particular person could recognize and perform it. A model used to assign blame needs those extra facts. | Beckers and Halpern, [*Abstracting Causal Models* — PDF](https://www.cs.cornell.edu/home/halpern/papers/abstraction.pdf). |
| [Preserving correction — C004](state/external/eight-ideas-audit-20261022/03-C004-preserving-correction.md) | An institution that retires the only affordable checking route for a relied-on claim may owe a substitute or responsibility for the additional costs. | Porat and Stein, [*Liability for Uncertainty: Making Evidential Damage Actionable*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=10261). |
| [Inherited authority — C111](state/external/eight-ideas-audit-20261022/04-C111-inherited-authority.md) | Receiving benefits from a founder does not automatically justify treating the founder's priorities as permanently binding. Current trustees owe a present justification. | Beckman, [*Democratic Legitimacy and Decisions for the Future*](https://doi.org/10.1007/s11158-025-09717-y). |
| [Translation and disagreement — C063](state/external/eight-ideas-audit-20261022/05-C063-translating-disagreement.md) | A report can accurately translate every sentence yet misrepresent a challenge to a standard as confusion about facts. Institutions need a way to correct the represented dispute. | Plunkett and Sundell, [*Disagreement and the Semantics of Normative and Evaluative Terms*](https://quod.lib.umich.edu/p/phimp/3521354.0013.023/). |
| [Forgotten obligations — C045](state/external/eight-ideas-audit-20261022/06-C045-forgotten-obligations.md) | A debt can survive innocent memory loss while the creditor acquires a duty to provide proportionate help establishing what is owed. The claim is about assistance, not erasing the debt. | Liao and Sandberg, [*The Normativity of Memory Modification*](https://doi.org/10.1007/s12152-008-9009-5); Darwall, *The Second-Person Standpoint*, cited in the draft. |
| [Reopening inquiry — C085](state/external/eight-ideas-audit-20261022/07-C085-reopening-inquiry.md) | A challenger cannot fairly be required to prove a defect before accessing the records needed to demonstrate it. A bounded preliminary review can break the circle. Develop with C004. | Friedman, [*Inquiry and Belief* — accepted-manuscript PDF](https://jfriedmanphilo.github.io/IB.pdf), especially §4.1. |
| [Complaints between departments — C021](state/external/eight-ideas-audit-20261022/08-C021-contesting-objectives.md) | Individually proper procedures can jointly leave a legitimate complaint without any competent recipient. The institution may owe a route to an authorized answer. | Vredenburgh, [*The Right to Explanation*](https://doi.org/10.1111/jopp.12262). |

The background papers establish the debates and prior work. Linking them does not claim that they endorse the draft's proposed extension. Where a link is a publication or archive record rather than a direct PDF, access may depend on the site. Several older drafts contain historical source-access notes; later uploads and reassessments may supersede those notes.

## Navigating the versions

Start with the links in this guide rather than every numbered file. E1/O1, E2/O2, and E3/O3 are grouped as paired treatments. The latest external E2 is v5; O5 is v3; causal-refinement A4 is v2. The original external A6 essay should be read with its continuation, not counted twice. Claude's new A4–A6 are all v1.

[Claude's review discussion](https://github.com/paulmauriceadriendirac/elenchus/issues/1) is useful after reading the relevant manuscript. Some reports address older versions, so check the version before treating a criticism as unresolved. [Current revision status](FINALIZATION.md) and the individual revision notes track those distinctions.
