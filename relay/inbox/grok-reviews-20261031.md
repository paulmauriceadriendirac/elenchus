# Outside-model reviews (Grok), relayed by the human operator, 31 Oct 2026 — verbatim

## Review 1 — A4

Peer Review Report
Manuscript: "A Switching Dilemma for Normality in Actual Causation"

Recommended decision: Major revisions (borderline accept / revise-and-resubmit). Suitable for a top specialist venue in philosophy of science or metaphysics (BJPS, Philosophical Studies, Synthese); stronger framing of the significance of the anonymity baseline would be needed for a generalist top journal.
Summary
The paper establishes a precise limitative result for normality filters applied to the three Halpern–Pearl (HP) definitions of actual causation. Under the coding on which occurrences are deviant and absences default, and under the restriction that a filter is anonymous (its verdict on a witness depends only on the multiset of category transitions: n/l/f/u and root default/deviant status), no Pareto filter can simultaneously (i) count the antidote a cause in genuine prevention, (ii) count Suzy's throw a cause in late preemption while excluding Billy's, and (iii) exclude the standard switch cases (Tracks, Doorbells, and Blocked tracks), under any of the three definitions.
Under the modified definition the sole witness for Suzy has exactly the same transition profile as the sole witnesses for the two switches (Theorem 1). Under the original and updated definitions the witness that convicts the flip in Blocked tracks is the genuine-prevention witness plus one additional root default-restoration (Theorem 2). The paper then prices a natural non-anonymous repair that varies only frozen-default scores by mechanism reliability, shows that exceptionless equation-conformity collapses to root but-for causes under the modified definition (Lemma), and notes a parallel dilemma in Andreas & Günther's regularity theory.
Strengths

1. Technical precision and scope. The identities of witness profiles are exact and cover every anonymous filter at once. Treating the three definitions together, rather than in isolation, is a genuine contribution; the paper shows that moving from the older definitions to the modified one merely relocates the dilemma rather than dissolving it.
2. Careful positioning. The author correctly notes that Halpern & Hitchcock treat their guidelines as "rough-and-ready" and explicitly allow mechanism-sensitive comparisons. The result is framed as a limit on a well-defined baseline class, not as a refutation of all uses of normality. This is the right dialectical posture.
3. Useful stress-tests of the non-anonymous escape. The Sprinkler and Seedlings cases effectively pressure the reliability-based justification for differential frozen-default scores. The isomorphism argument for Seedlings is clean.
4. Lemma on frozen witnesses. The observation that exceptionless conformity (under fixed-context acyclic models and the modified definition) leaves only root but-for causes is sharp and has independent interest; its application to Xiao & Xiong's availability condition is well taken.
5. Computational checks. Exhaustive enumeration over the 355 preorders and random additive scores strengthens the corollary.

Main Criticisms and Requests for Revision

1. Significance of the anonymity baseline needs sharper defense.
The paper repeatedly emphasizes that anonymity is "a baseline, not a characterization of every principled policy." This is accurate, but a top-journal reader will ask why the impossibility result is philosophically important once it is granted that the leading proponents already allow non-anonymous rankings. The current discussion (especially the "Why it matters" paragraph and Section 5) is too brief. The author should more explicitly argue that transferable, variable-independent policies form a natural and attractive class (e.g., because they avoid post-hoc encoding of desired verdicts, or because they are what one would expect from a theory that treats normality as a structural or statistical feature of mechanisms rather than of particular event types). Without this, the result risks being read as "anonymous filters cannot do the work that non-anonymous filters were always intended to do."
2. Treatment of "parts of causes."
Under the modified definition the flip remains part of a cause even if it is not a single-candidate cause (the conjunction with the left blockage). The paper sets this aside. For readers who take the HP definitions seriously, parts of causes are often treated as causes. The author should either (a) strengthen the dilemma to cover parts, or (b) give a clearer philosophical reason for focusing only on single candidates. The same issue arises for Billy's throw under some preorders.
3. Event coding is doing more work than is fully acknowledged.
The results are conditional on occurrences being deviant and absences default. This is standard, but several of the pressure cases (especially Blocked tracks and the inertial-coding escape) turn on it. Section 5 prices the inertial alternative, but the discussion remains local. A short systematic discussion of when the coding is independently motivated (rather than chosen to generate the desired contrast with preemption) would strengthen the paper. The Seedlings isomorphism already shows that the coding alone does not always yield the preemption/switch contrast; this point can be leveraged more.
4. Proof presentation.
The proofs of Theorems 1 and 2 are essentially enumerations of the relevant interventions. For a philosophy audience this is acceptable, but the paper would be more convincing if the key uniqueness claims (that there is only one witness world under the modified definition) were stated as short lemmas with the sufficiency checks made fully explicit. The reliance on "computed" for the five calibrated preorders and the conjunctive cases is fine for an appendix, but the main text should not leave the reader wondering whether any edge case was missed. (If the Python implementation is to be made available, say so.)
5. Relation to Wysocki (2023).
The paper correctly notes that Wysocki's conjoined-cases obstruction is stronger in one respect. The incremental value claimed ("exact identity of witness profiles across standard, uncombined models under an explicit anonymity restriction") is real, but it should be stated more crisply in the introduction so that readers do not have to reconstruct the difference themselves.
6. Minor technical and expository points.
   * The four categories (n, l, f, u) are clear, but a small table showing the actual and witness categories for each of the central cases would make Theorem 1 easier to verify.
   * The additive-score identity gDoorbells=gChain+gBoulder is elegant; a one-sentence intuitive gloss would help.
   * In the discussion of Gallow's many-valued switch variable, the paper notes that no anonymous filter on a binary route model can express the relevant comparison. This is correct, but it raises the prior question of model aptness more sharply than the "Objections" section currently handles. A sentence acknowledging that the dilemma is partly a dilemma about representation would be useful.
   * The parallel with Andreas & Günther / Beckers is well drawn but slightly underdeveloped; one additional paragraph on whether the structural conditions in the regularity theory face an anonymity-like restriction would tighten the comparison.

Recommendation
The formal results are correct on the stated assumptions, the dilemma is genuine within its scope, and the pricing of the natural non-anonymous repair is philosophically useful. The main obstacle to acceptance in a top venue is that the paper currently under-sells why a limit on anonymous Pareto filters matters, given that the literature already contemplates non-anonymous rankings. With a clearer defense of the baseline, tighter handling of parts-of-causes, and modest improvements in proof presentation and literature positioning, the paper would be a strong contribution.
Required revisions

* Expand the motivational discussion of anonymity (introduction and Section 5).
* Address parts-of-causes explicitly.
* Add a short table or explicit category listings for the central witnesses.
* Strengthen the uniqueness arguments for the modified-definition witnesses.
* Minor clarifications noted above.

I would be happy to re-review a revised version.

## Review 2 — A5

Peer Review Report
Manuscript: "Holistic Accuracy and the Limits of Lockean Derivation"

Recommended decision: Revise and resubmit (leaning accept). Suitable for a top generalist or specialist venue in formal epistemology (Mind, Philosophical Review, Philosophy and Phenomenological Research, Noûs, or BJPS). The negative result is clean and the diagnostic work is valuable; the main tasks are to sharpen the claimed increment relative to Dorst & Mandelkern and to tighten the discussion of what counts as a legitimate holistic accuracy measure.
Summary
The paper targets Dorst's (2019) claim that maximizing expected accuracy yields Lockean thresholds for belief even after separability is dropped in favor of a holistic measure (his Proposition 5). It distinguishes a weak reading (mere truth-directedness plus order-independence) from a stronger reading that imposes restrictions on marginal values. Under the weak reading, a "record measure" that adds a positive premium for an error-free body of belief (rewarding the truth of the state's core) satisfies strict marginal truth-directedness yet produces non-monotonic belief: with values and context fixed, a proposition can belong to the unique optimum at one credence and to none at a higher credence (Theorem 1 and the numerical example).
The paper then shows that the natural repairs—Marginal Extensionality (ME) and Background-Independence (BI)—recover separability on the relevant domain (Theorem 2 and Corollary). It characterizes the optima of the record measure exactly as core-relative Lockeanism (Theorem 3), notes the overlap with Dorst & Mandelkern's (2022) expected-utility account of filtered guesses, and proves that unrestricted cross-space refinement invariance is a sufficient route to (conservative) Lockean thresholds (Theorem 4), though stronger than what a fixed-space Lockean derivation requires. The overall conclusion is that accuracy maximization alone does not settle the bridge from credence to belief; further substantive restrictions on the measure must be defended.
Strengths

1. Clean and decisive counterexample. The record measure is simple, purely alethic, and satisfies the truth-directedness condition that motivates Dorst's §4.2. The non-monotonicity is robust (Theorem 1 gives an open interval for any positive premium) and arises with values and context held fixed—precisely the feature Dorst's variable-Lockean examples do not exhibit.
2. Precise diagnosis. The quantifier gap and content gap are well identified. Theorem 2 cleanly isolates what ME + BI force, and the corollary makes the dilemma for Dorst's argument sharp: either the remaining holism is too weak to block the counterexample, or the measures are separable after all.
3. Useful positive characterization. Theorem 3's core-relative Lockeanism is an attractive description of what this form of holism actually delivers. The comparison with Dorst & Mandelkern is handled carefully; the paper correctly claims a narrower increment (optimization over unrestricted belief states under strict marginal gains/losses for truths and falsehoods).
4. Refinement discussion. Theorem 4 is a nice positive result, and the distinction between restricted (question-relative) and unrestricted refinement invariance is philosophically useful. The observation that some Lockean families violate RI is a good check against over-identification.
5. Modesty and literature engagement. The paper does not claim that Lockeanism is false or that the record measure is the correct epistemic value. Engagement with Holguín, Leitgeb, Levi, Rothschild, and Wang is appropriate and concise.

Main Criticisms and Requests for Revision

1. Sharpen the increment relative to Dorst & Mandelkern (2022).
Section 5 correctly notes that their model already reproduces the two belief sets in the main example and that neither the reversal nor the filtered-core structure is new. The claimed novelty—"its realization under the strict marginal truth-directedness at issue in Dorst's argument"—is real but currently understated. A top-journal reader will want a clearer statement, early in the paper, of what is gained by having the non-monotonicity arise from an accuracy score defined on unrestricted belief states (rather than from a Jamesian value defined on answers to a question). One or two sentences contrasting the two settings more sharply (e.g., that scoring a state solely by its conjunction's Jamesian value would violate the strict gains for adding true propositions) would help.
2. Defend the legitimacy of the premium more carefully.
The paper anticipates the objection that the premium double-counts the core or is not pure accuracy (Section 7). The replies are adequate, but the motivational discussion in Section 3 is thin. A short paragraph explaining why a holist who rejects separability might specifically value the truth of the total commitment (the core), rather than some other interaction term, would make the counterexample harder to dismiss as an artificial score. Relatedly, it would be useful to note whether other natural holistic terms (e.g., a bonus for deductive closure, already mentioned in footnote 4) produce similar non-monotonicity; the current focus on the record premium is fine, but readers may wonder how special it is.
3. Non-vacuity and the move from optimization to permission.
The paper is careful that Maximize Expected Accuracy is only a necessary condition and introduces Non-vacuity to connect unique optima to rational permission. This is reasonable, but Section 7's treatment of the "perhaps neither optimum is rational" objection is slightly brisk. A sentence or two acknowledging that some accuracy-first theorists might prefer a dominance or permissibility framework that does not force existence of a rational state at every credence would make the dialectical situation clearer. (The unique-optimum cases still do most of the work.)
4. Expository and structural suggestions.
   * The introduction is dense. A one-sentence roadmap after the thesis statement, explicitly labeling the three parts (counterexample, diagnosis of the derivation, refinement), would help.
   * Theorem 1's interval is elegant; a brief intuitive remark on why the length is proportional to βT/(D(2D+β)) would aid readers who do not immediately check the appendix.
   * In Section 6, the two repairs (mean over the algebra; question-relative algebra) are good, but the text could more clearly flag that the first repair preserves the non-monotonicity under question-preserving refinements while the unrestricted RI of Theorem 4 rules it out. The current organization is correct but slightly easy to misread.
   * Minor: the four-world non-closure example is effective; mentioning it earlier (when core-relative Lockeanism is introduced) would make the contrast with ordinary Lockeanism vivid sooner.
5. Minor technical points.
   * The proviso in Theorem 2 (states containing no proposition together with its complement) is well-motivated and harmless, but a parenthetical reminder that such states are suboptimal under the relevant conservativeness conditions would be helpful in the main text.
   * In the proof of Theorem 4 (appendix), the argument that the fully inconsistent state cannot be optimal under CI is clear; a one-line note that the same reasoning rules out states missing the tautology would make the reduction to the four candidate states fully explicit.

Recommendation
The paper makes a solid contribution. The counterexample is simple and robust, the diagnosis of Dorst's argument is precise, and the surrounding results (Theorems 2–4 and the core characterization) add value. The main revisions needed are presentational: a sharper statement of the increment over Dorst & Mandelkern, a slightly fuller motivation for the record premium as a holistic accuracy term, and minor clarifications around Non-vacuity and the refinement repairs. With those changes the paper would be a strong candidate for a top journal in formal epistemology.
Required revisions

* Clarify the precise increment relative to Dorst & Mandelkern early and in Section 5.
* Strengthen the motivational discussion of the core premium.
* Minor expository improvements noted above (roadmap, interval intuition, refinement organization).
* Brief additional remarks on Non-vacuity and the scope of Theorem 2.

I would be happy to re-review a revised version.

## Review 3 — A6

Peer Review Report
Manuscript: "When Acting on Knowledge Makes Free Evidence Harmful: Good's Theorem in Normality Models"

Recommended decision: Revise and resubmit (leaning accept). Suitable for a top specialist or generalist venue in formal epistemology and decision theory (Mind, Philosophical Review, Philosophy and Phenomenological Research, Noûs, BJPS, or Journal of Philosophy). The results are technically precise and dialectically well-aimed at recent work on knowledge-based decision theory and Salow's Conditional Knowledge Dominance; the main tasks are to clarify the scope of the assumptions and to sharpen the positive implications for how knowledge should guide action.
Summary
The paper examines whether knowledge-based decision theory (KDT)—maximizing expected utility with probabilities conditioned on one's knowledge—preserves Good's theorem (that free evidence never has negative expected value) inside Goodman and Salow's normality framework for inductive knowledge. Under the assumptions of finite statist, comparable models with K-normality, a free question is safe in every decision problem if and only if there is no relative defeat (no state compatible with one's ken is one where the answer would reopen a possibility one now rules out). Every question is safe if and only if knowledge is gapped (Theorem 1); in finite graded models, no factive state containing rational belief is safe unless it is the whole evidence (Theorem 2 and Corollary).
A concrete illustration is given in Goodman and Salow's model of Bjorn's repeated weighing: after the first reading, a free second weighing has negative KDT value at ordinary odds (ten-to-one and higher). The paper then tests three expected-utility developments of Salow's Conditional Knowledge Dominance. Conditioning on the options' differing (CEU) and conditioning on the evidence's changing one's choice (VER) both fail in the presence of relative defeat. Conditioning answer by answer (ANS) is safe for free questions, but makes the agent willing to pay to check what she already knows, in conflict with Conditional Knowledge Dominance (Propositions 4–5). The negative results target specific expected-utility rules rather than Salow's qualitative principle or every knowledge-based decision theory.
Strengths

1. Precise characterization of when Good's theorem holds under KDT. Theorem 1 cleanly equates safety of a free question with the absence of relative defeat, under the stated normality assumptions. The link to gappedness, and the extension in Theorem 2 to factive states that leave open what rational belief leaves open, are sharp and useful. The appeal to Geanakoplos's laminar value-of-information result is appropriate and well-integrated.
2. Effective concrete counterexample. The ten-to-one (and higher) bet in Bjorn's model makes the negative value of free evidence vivid and non-contrived. The calculations tying the magnitudes to the normality threshold c (and to the probabilistic reading of "sufficiently more normal") are helpful, and the separation of the three claims about other situations is careful.
3. Dialectically well-targeted tests of Conditional Knowledge Dominance. Distinguishing CEU, VER, and ANS is useful. Theorem 3 and the numerical illustrations show that natural expected-utility strengthenings of Salow's principle reintroduce the problem or create new ones (paying to check known propositions). The observation that the qualitative principle is often silent in the constructed cases, while the quantitative rules are not, is a fair and important point.
4. Modest and accurate positioning. The paper correctly notes the relation to Dorst et al.'s (2021) Total Trust / Value results and claims only a normality-theoretic characterization of the relevant boundary, plus the graded-model consequence and the tests of the three rules. It does not overclaim a refutation of all knowledge-based decision theory or of Salow's qualitative principle.
5. Engagement with the literature. The treatment of Goodman and Salow (2023, 2025), Salow (2025), Geanakoplos, Dorst, Das, Hong, and Goldschmidt is appropriate. The brief remarks on KK, alternative normality principles (I- and KM-normality), and non-statist models show awareness of the framework's flexibility.

Main Criticisms and Requests for Revision

1. Scope and generality of the assumptions need clearer framing.
The theorems rely on finite models, statism, comparability, and (for the main positive results) K-normality. These are standard within the Goodman–Salow framework, but they are strong. Statism in particular is known to be restrictive (the paper itself notes that probabilistic models often violate it outside the bodies of evidence under consideration). The results are interesting even under these restrictions, but a top-journal reader will want a clearer sense of how much the negative verdicts depend on them. A short discussion in the introduction or conclusion of what happens under I- or KM-normality (already mentioned in §6.1 of the paper), or under failures of statism, would help. The paper need not prove general theorems in those cases, but flagging the dependence more prominently would prevent the results from being read as applying to "normality models" simpliciter.
2. Philosophical payoff for knowledge-based decision theory and for Salow's approach.
The paper shows that KDT preserves Good's theorem exactly where knowledge is gapped (under the assumptions), and that natural expected-utility developments of Conditional Knowledge Dominance either reintroduce negative value of free evidence or conflict with the principle on costly inquiry. This is a genuine contribution, but the positive upshot is somewhat understated. Does the author recommend gapped knowledge as a necessary condition for KDT to be decision-theoretically well-behaved? Should one condition only on evidence in graded models? Or is the lesson that knowledge-based probabilities are simply not the right object for expected-utility calculations about inquiry? A clearer statement of the options left open (beyond the negative results) would strengthen the paper's impact. Relatedly, the connection drawn to Dorst et al.'s Total Trust is useful; it could be leveraged more explicitly to explain why the relative-defeat / gappedness boundary is the natural one.
3. The three conditional rules and the status of ANS.
The failure of CEU and VER is cleanly demonstrated. ANS's success for free questions at the cost of violating Conditional Knowledge Dominance on costly inquiry is also well shown (Proposition 5). However, the discussion could more clearly address whether ANS (or a restricted version that applies only to free questions) is a viable development of Salow's idea, or whether the conflict with the qualitative principle is decisive against it. The remark that restricting ANS to free questions produces an extreme all-or-nothing attitude toward prices in Bjorn's case is good, but a sentence or two on whether this is an acceptable cost, or whether it shows that no expected-utility conditional rule can simultaneously secure Good's theorem and respect Conditional Knowledge Dominance, would help.
4. Expository and structural suggestions.
   * The introduction is dense. A brief roadmap after the thesis statement, explicitly separating the Good's-theorem results from the tests of the three conditional rules, would help.
   * Lemma 1 (defeat is costly) is the workhorse of the negative results; a short intuitive gloss in the main text (beyond the proof) would aid non-specialist readers.
   * In the Bjorn section, the distinction among the three claims (i)–(iii) is careful, but the main text could more prominently flag that the second weighing itself is not one of the p_v questions used in Theorems 1–2, so that readers do not over-generalize the continuous example to the finite theorems.
   * Minor: the numerical values in Bjorn (0.05 probability of defeat conditional on knowledge, etc.) are helpful; confirming in a footnote or appendix that they were obtained by numerical integration over the relevant regions of the Gaussian error model would be reassuring.
5. Minor technical points.
   * The definition of gappedness and the relation to C(x) (the states reachable by steps that are not sufficiently less normal) are clear; a parenthetical reminder that under collapse + comparability every ken is gapped would make the Corollary's part (i) even more immediate.
   * In the construction for Theorem 3, the perturbation with εζ is elegant; a one-sentence note that the open-neighborhood claim follows from continuity of the expectations would make the robustness fully explicit in the main text.

Recommendation
The paper makes a solid technical and dialectical contribution. The characterization of when free questions are safe under KDT in normality models is precise, the Bjorn illustration is effective, and the tests of the three expected-utility developments of Conditional Knowledge Dominance are careful and fair. The main revisions needed are to frame the scope of the assumptions more clearly, to articulate the positive options left open more sharply, and to make minor expository improvements. With those changes the paper would be a strong candidate for a top journal in formal epistemology.
Required revisions

* Clarify the dependence on statism, comparability, finiteness, and K-normality, and briefly indicate the status of the results under alternative normality principles.
* Sharpen the discussion of the positive implications for KDT and for developments of Conditional Knowledge Dominance.
* Minor expository improvements (roadmap, intuitive glosses, flagging of the relation between the continuous example and the finite theorems).
* Brief additional remarks on the viability of ANS-style rules.

I would be happy to re-review a revised version.
