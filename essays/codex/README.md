# Five essays: reading guide and verification notes

This set contains three substantial revisions of the repository's E1–E3 v2 drafts and two additional essays. Each essay is available as editable Markdown and a typeset PDF. The existing drafts, reviews, and project tools are preserved.

These are complete research drafts, not certified discoveries. The arguments have been checked against the cited primary sources and the formal claims examined directly. Novelty remains provisional, and no independent referee has endorsed this revision set.

## The essays

| Essay | Main argument | Files |
|---|---|---|
| **Independent Sources and the Correlations We Know** | Global K-normality preserves local knowledge while adding joint exclusions. A product repair removes those exclusions and retains KK on the specified structures. | [PDF](01-independent-sources.pdf) · [Markdown](01-independent-sources.md) |
| **How Much Does Bayes Depend on the Benchmark?** | Exact Bayesian optimality can fail under arbitrarily small reweighting while its quadratic-score regret remains second order. | [PDF](02-bayes-and-the-benchmark.pdf) · [Markdown](02-bayes-and-the-benchmark.md) |
| **Independent Interventions and the Limits of Flattening** | Ordered selection cannot preserve independent-control locality at every scenario and validate unrestricted Flattening on the complete two-control square. | [PDF](03-independent-interventions.pdf) · [Markdown](03-independent-interventions.md) |
| **What Survives Forgetting Distinctions?** | Two universal compatibility demands force reports to reveal either the actual singleton or the whole space. Approximate preservation bounds the frequency of partial reports. | [PDF](04-forgetting-distinctions.pdf) · [Markdown](04-forgetting-distinctions.md) |
| **Learning Nothing Under Minimax Regret** | With quadratic loss and a fixed binary prior, ex-ante minimax regret transforms the response to a tautology by taking square roots of the prior odds. Minimax expected loss retains the prior. | [PDF](05-learning-nothing-under-regret.pdf) · [Markdown](05-learning-nothing-under-regret.md) |

For the clearest additional ideas, begin with essays 4 and 5. For the closest engagement with the three original target papers, read essays 1–3. The Bayesian essays address different questions: perturbing a fixed benchmark, changing descriptive granularity, and changing the performance criterion.

## What is inherited, and what is being claimed

**Essay 1.** Goodman and Salow's figure 4 already supplies the central accessibility pattern. Carter and Goldstein already discuss intersective combinations of single-source models. The proposed increment is the exact marginal-preservation result, the criterion for nonrectangularity, and the comparison of product K with KM on finite products of total preorders. The revision abandons the misleading suggestion that a distant failure improves unconditional knowledge of the working source. The disputed extra knowledge is correlational. Hawthorne's later objections to local sharp knowledge remain live; this repair does not solve them.

**Essay 2.** Meehan and Zhang already prove the extensional-profile characterization, and the CAR literature already analyzes face-value conditioning and robustness. The small-reweighting proposition is expressly presented as a corollary of their results. The proposed increment is the joint treatment of exact fragility and quantitative near-optimality, with an explicit relative-perturbation bound and a distinction between state symmetry and simultaneous relabeling of a prior. The counterexample using prior-dependent weights illustrates that distinction; it is not offered as a preferred epistemic benchmark.

**Essay 3.** Dorr and Mandelkern already characterize flat frames and discuss failures of Flattening in similarity models. The overwrite composition property for independent settings is elementary. The proposed increment is a metric-independent incompatibility between two-control locality and unrestricted Flattening, together with conjunctive and Contraction controls. The claim concerns a specified intervention-sensitive interpretation. It does not establish a complete semantics of natural-language counterfactuals or a positive theory of indicative conditionals.

**Essay 4.** CAR and the distinction between report content and report occurrence are established background. The proposed increments are the classification of prior-free report families compatible with every surjection, the classification of CAR mechanisms that remain CAR under every state identification, and the quantitative restriction derived from approximate preservation. These exact statements were not identified in the sources consulted; that is a bounded search result, not proof that they have never appeared. The operation under study compresses reports and can lose information. The essay explicitly rejects the inference that Bayesian probability itself is incoherent under redescription.

**Essay 5.** Minimax updating, epistemic minimax regret, and regret-based learning under unknown data generation all have prior literature. In particular, van Ommen and colleagues (2016), Pettigrew (2016), and Che, Li, and Luo (2026) must be credited. The proposed increment is the exact solution for a single binary factive report, its extension to every stochastic factive kernel, and its implications for protocol-blind No News and ex-ante versus conditional evaluation. The square-root formula's publication novelty is not certified.

## The strongest remaining objections

1. **Independent sources:** rectangularity is an additional epistemic constraint. Coordinatewise normality and marginal preservation alone do not entail it. The philosophical case must justify it for the specified instruments without excluding legitimate aggregate information.
2. **Benchmark robustness:** a defender can reject unrestricted perturbations as normatively inadmissible. The theorem identifies what must be defended; it does not refute a benchmark whose allowed perturbations preserve extensionality. The regret bound requires relative control at active reports and uses the specified quadratic score.
3. **Flattening:** a sequence theorist can deny locality at embedded indices or explain the reading through contextual change. The formal incompatibility is secure under its assumptions; the linguistic adjudication remains contested.
4. **Forgetting distinctions:** invariance under every surjection is a strong demand. A critic can reasonably restrict legitimate redescriptions to those preserving the observation algebra. The essay proves that this restriction matters and supplies a sufficient saturated-report condition.
5. **Minimax regret:** the comparator knows the reporting mechanism when selecting its rule. Whether that is the right standard for epistemic disappointment needs a normative argument. Reapplying conditional minimax regret after observing the tautology gives one half, rather than the ex-ante square-root rule; the essay does not conceal this timing issue.

## Checks performed

The three target papers were read from the repository's full extracted texts. Relevant primary literature was consulted directly, including work on intersective normality models, recent KK criticism, CAR, causal interventions, robust probability updating, and minimax regret. Author names, titles, and the cited publication identifiers were checked; bibliographic errors found during drafting were corrected.

The earlier repository checks for the three original draft topics completed successfully. They provided useful finite-model and algebraic checks, not a certificate of originality or a machine-checked proof of every sentence in the revised essays. Additional checks specific to this set were run separately:

| Claim checked | Scope | Result |
|---|---|---|
| Quadratic regret bound in essay 2 | 1,000 normalized random report-profile perturbations on 2–5 states | All satisfied the stated bound. |
| Locality versus Flattening in essay 3 | All 1,296 centered order frames on four named worlds | 108 satisfied locality; none of those satisfied unrestricted Flattening. |
| Coarsening calculation in essay 4 | Exact rational calculation of the three-state example; coefficient identity at every singleton-separating partition of sampled CAR mechanisms on 3–7 states | Posterior equals 4/7; all coefficient identities agreed. |
| Square-root optimum in essay 5 | 99 priors, each compared against 10,001 candidate posteriors | All grid comparisons agreed with the analytic optimum. |
| Randomized-mechanism extension in essay 5 | 9,900 sampled stochastic factive mechanisms | None exceeded the derived worst-case vertex regret. |

The written proofs, rather than these finite checks, establish the universal statements under their assumptions. The checks are sanity checks against algebraic and implementation mistakes. No new code harness is part of this deliverable.

All five PDFs were rendered and visually inspected. Equation labels were corrected after the initial conversion dropped them. The final files were checked for missing replacement characters and text extending beyond page boundaries.

## Further ideas worth developing

**Restricted representation invariance.** Essay 4 gives a sufficient preservation condition when reports are unions of the categories being merged. A next question is to characterize exactly which classes of permitted coarsenings admit a rich family of partial CAR reports. The target would be a classification relative to a specified observation algebra, rather than another unrestricted impossibility result.

**Regret with more than two states.** Essay 5 leaves open the minimax-regret rule for three or more states and overlapping partial reports. The binary square-root transformation should not be extrapolated without proof. The task is to determine which reports bind the optimum and whether one rule can simultaneously minimize ex-ante and conditional regret on a nontrivial class of mechanisms.

**Controlled tests of embedded locality.** Essay 3 suggests a focused linguistic investigation: hold the time, referents, and mechanisms fixed; vary independent versus interlocked controls and inclusive versus exclusive inner antecedents. The formal predictions are explicit. No speaker data have been collected, so this remains a proposed study, not empirical support already obtained.

## Provenance and publication scope

This is an AI-assisted research-draft set, developed from the repository manuscripts and the sources cited in the essays. The original E1–E3 v2 manuscripts supplied the initial topics and arguments for essays 1–3; essays 4–5 were developed during this continuation. Concurrent later drafts in the source branch are preserved but are not represented as having received the same review here.

The set is published on a dedicated branch of the user's private repository. It is not an external competition submission, and no claim of compliance with competition clean-context or authorship rules is made. Any later submission requires a separate provenance and eligibility assessment.
