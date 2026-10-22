# Referee report — S3 Decision theorist (foundations and extreme stakes), with G3 literature-audit standards [mode: report+lit] — P-bb8a

## Thesis and argument as I understand them (≤120 words)

Take two states, a fixed regular prior p, and a source that sends some true proposition under an unknown, possibly randomized, factive protocol. Restrict attention to rules that see only the report's content (Meehan–Zhang's global evidential constancy) and that become certain on singleton reports. Then minimising worst-case expected Brier inaccuracy keeps p on a tautological report (Prop. 2). Minimising worst-case regret against the best rule for each protocol uniquely gives q* = √p/(√p+√(1−p)) (Prop. 1). Both hold over randomized protocols (Prop. 3), and conditional regret gives ½. Moral: an appeal to "robustness" does not vindicate conditionalization or No News. One has to defend a choice of benchmark, i.e. whether unavoidable error counts.

## Verdict
Prize: not finalist
Journal recommendation: reject (in present form; a reframed and generalized short note could be viable, see "Top five changes")

## Scores
Clarity: 7 | Argument: 5 | Significance: 4 | Originality: 4 | Literature: 4 | Accuracy: 6 | OVERALL: 5

## The single most serious problem

**Location.** Several passages:
- the abstract: "It does not require … counting some mechanisms more often than others. The disagreement instead comes from subtracting a mechanism-specific performance benchmark";
- §4: "Their disagreement comes entirely from the comparator";
- the last paragraph of §5;
- §7.

**Problem.** The essay presents robustness as a way around Meehan & Zhang's (M&Z) weighting question. It presents the comparator as a separate source of non-Bayesian verdicts. But by the minimax theorem, every minimax or minimax-regret rule is a Bayes rule against a least-favorable distribution over the uncertainty set (Wald). Here that distribution is a weighting λ over M&Z learning situations. So each robust rule coincides with M&Z's weighted-total optimum for an endogenous weighting λ*. I checked the binary case.

- **Prop. 2.** λ* is a point mass on N. N is transparent, so λ* is extensional (M&Z Fact 12). The singletons get zero weight, which is exactly why the dogmatic rule ties (cf. M&Z fn. 39).
- **Prop. 1.** λ* puts weight on E_a and E_b in the ratio √(1−p) : √p, and zero on R and N.
  - This is a saddle point: at q*, E_a and E_b are the only binding mechanisms.
  - λ* is non-extensional for p ≠ ½, because λ*_S(a) = λ*(E_a) ≠ λ*(E_b) = λ*_S(b).
  - M&Z's Lemma 1 then gives the result in one line: f(S) = π(a | λ*_S) = p√(1−p) / (p√(1−p) + (1−p)√p) = √p/(√p+√(1−p)).

So the square-root rule is an instance of M&Z's own Fact 11: BCOND is optimal iff the weighting is extensional. That is the closest prior result, it sits in the essay's principal source, and the essay never mentions it. The general mechanism is also textbook robust Bayes. Loss-based and regret-based minimax rules differ because the oracle term varies across the uncertainty set, and both are Bayes against least-favorable priors. Lim & Park (2026, §§2.2, 3.1) state this explicitly.

**Why it matters.**
- *The increment changes.* As written, the thesis is that robustness is weight-free yet still fails to vindicate Bayes. Correctly stated, robustness endogenizes M&Z's weights. Wald's criterion selects an extensional (transparent) weighting; Savage's selects a non-extensional (opaque) one. The extensionality question is relocated into the choice of comparator, not avoided.
- *What is new shrinks.* That thesis is better, but the new part becomes: identifying which least-favorable weighting each criterion picks in the binary factive game. The essay should say so.
- *A missed as-if-Bayesian reading.* q* is ordinary conditioning on "the source said S" under the least-favorable protocol K*(S|a) = √(1−p)/(√p+√(1−p)), K*(S|b) = √p/(√p+√(1−p)). For p = 0.8 these are 1/3 and 2/3, and the posterior is 2/3. So §6's reassurance that the result is "not a refutation of Bayesian conditioning on a fully specified observation event" undersells the point. The robust rule *is* such conditioning, under an adversarially chosen protocol.

## Major problems

**1. The comparator is meta-conditionalization (§§2–3, §6).**
- *Problem.* The benchmark m_E equals the expected loss of meta-conditionalization (META-COND; Schoenfield 2017). Under E_a, META-COND treats S as identifying a. Under N, it retains p. Equivalently, m_E is the loss of M&Z's "one-shot" GEC rules, which mimic META-COND problem by problem (M&Z Fact 8). So the essay's regret is the shortfall from META-COND.
- *Why it matters.* M&Z's paper is built to deny that META-COND's per-problem accuracy advantage carries normative weight. They rule it out by noncontrastiveness/idempotence (§4.3) and deny that per-problem optima are targets (§5.3). An M&Z advocate will say that measuring a GEC rule's "missed opportunity" against a contrastive rule's accuracy smuggles contrastiveness back in. This is the strongest specialist objection. §6's "objection to the performance standard, not an algebraic objection" names it but does not answer it.
- *Fix.*
  - Name the comparator as META-COND and cite Schoenfield and M&Z Facts 2 and 8.
  - Argue why the accuracy attainable under each protocol is the right baseline for a rule that GEC *requires* to ignore the protocol.

**2. Two readings of the case are run together (§1 vs §6; what is learned; No News).**
- *Reading (a): a source with an unknown protocol (§1).* This is the Monty Hall/coarsening setting. There the standard Bayesian move is to refine the state space so that "the source said S" becomes the evidence (Grünwald & Halpern 2003; M&Z fn. 21). On this reading the agent has not learned nothing, and No News is not engaged.
- *Reading (b): M&Z's own.* The four "mechanisms" are learning situations. N and R are transparent; E_a and E_b are opaque, the two-state analogues of Dana. No News is engaged here. But:
  - M&Z interpret total accuracy objectively, not relative to an agent's uncertainty (fn. 35, contrasting Carr 2021). So a worst case over learning situations needs a rationale that §1's agent-level story does not supply.
  - Opaque Monty Hall, where one "learns nothing more than" the content (Bronfman 2014), is exactly the case M&Z flag as unresolved in fn. 21. The essay should engage it.
- *Where the essay stands.* §6 sees the distinction between content and occurrence but never says which reading Props 1–3 concern.
- *Fix.* Commit to reading (b), state that E_a and E_b are opaque, and argue against M&Z's idempotence motivation for GEC. Otherwise, show the conclusion survives both readings.

**3. Scope: binary state, Brier only. This also hides a consequence for the dialectic.**
- *The closed form does not generalize.*
  - Under the log score, the equalizer solves p ln q = (1−p) ln(1−q). For p = 0.8, q ≈ 0.7245, and N's regret (KL ≈ 0.015) is not binding.
  - With three states, q ∝ √π does not equalize the single-state-silence regrets. For π = (0.6, 0.2, 0.2) under Brier they come out ≈ 0.258 vs ≈ 0.165.
  - With n ≥ 3 states, the adversary can combine selective silences on different report sets, which couples f(S) to the rule's other responses.
- *What does generalize.*
  - The least-favorable-weighting characterization, via Sion's minimax theorem plus M&Z Lemma 1, for a convex strictly proper inaccuracy.
  - Plausibly, the qualitative "toward ½" verdict for symmetric binary scores. If g(x)/x is increasing, the root of p·g(1−q) = (1−p)·g(q) lies strictly between ½ and p; the N-constraint still has to be checked.
- *The contrast between the criteria changes after two states.* In any finite prior space, ex-ante minimax loss forces No News. N gives the lower bound Σπ(s)I(π,s), and the dogmatic rule attains it. But BCOND is *not* minimax-loss optimal in M&Z's Dana prior space: by their Fact 3 and Table 1 (Brier), BCOND's expected inaccuracy in Dana's learning situation is 1.188, against the prior's 1.12. So Wald's criterion vindicates No News but not Bayes. That is a sharper and more interesting point for the M&Z dialectic than the binary Prop. 2.
- *Fix.* Spend the spare words on these generalizations.

**4. Timing (§6): the analysis is incomplete and the relevant literature is missing.**
- *Ex-post minimax loss also gives ½.* After S, the set of conditional credences over randomized factive protocols is all of [0,1]. This is dilation (Seidenfeld & Wasserman 1993), equivalently the vacuous conservative update (de Cooman & Zaffalon 2004). So the loss/regret contrast exists only ex ante, and "worst-error preserves the prior" holds only for advance plans.
- *The divergence is a known phenomenon.* The gap between ex-ante and conditional evaluation is the familiar time-inconsistency of Γ-minimax criteria.
  - Grünwald & Halpern (2011) explain it as different games against bookies who hold different information.
  - Lim & Park (2026) show that ex-ante minimax-regret rules are generally not dynamically consistent. They propose interim criteria that update the least-favorable prior. That proposal answers the essay's open question: updating K* yields q* after S, consistently.
  - Che, Li & Luo (2026, §2.2) already contrast ex-ante and ex-post regret.
  - Aradillas Fernández et al. show that ex-ante and ex-post robust-Bayes rules disagree in general.
- *Fix.*
  - Say that M&Z-style rule evaluation is ex ante by design.
  - Add the ex-post loss result.
  - Cite this literature.

**5. No normative payoff (§7).**
- *Problem.* The essay ends with the question it should answer: which avoidable losses matter?
- *Available tools.* Decision theory has an axiomatic handle on exactly this choice. Savage regret is invariant to adding a constant to a column (a state of nature; here, a mechanism); Wald's maximin is not (Milnor 1954). Stoye 2011 gives axiomatizations of minimax regret. The epistemic analogue is whether rule evaluation should be invariant to mechanism-specific constant shifts of inaccuracy, i.e. whether "unavoidable error" should count.
- *Fix.*
  - Argue that question.
  - Add interpolating criteria: Hurwicz/GHC-style weights, as in Pettigrew's work on epistemic risk, or an ε-contamination class around N. These would show how much credence in a strategic source drives the departure from p.

## Minor problems

- **"No News" is never introduced properly.** It appears in the abstract and in bold in §6 as if it were an established, named principle, but it is not defined before §6 or attributed to anyone. I found no source that uses the name. Define it and tie it to M&Z's Noah case, where BCOND retains the prior on the tautology.
- **"Novelty status still provisional" (§7)** does not belong in a submission. Do the search and report the result (see the Literature check).
- **§5's "duplicating a mechanism in a list" is a strawman of M&Z.** Their total ranges over a *set*, and their relevant device is the weighting λ (Fact 11). The accurate point is different: minimax criteria are invariant to every reweighting with fixed support, but not to the support. For example, excluding the opaque mechanisms makes both criteria give p.
- **Uniqueness can be strengthened.** The minimax-regret optimum is unique over *all* rules, not only evidence-respecting ones. A departure on a singleton raises the binding E_a or E_b regret.
- **Prop. 2 is a special case of van Ommen et al.'s minimax game.** Since conditional generalized entropy ≤ entropy, the quizmaster's worst case is to always send the whole space. Say so.
- **Admissibility.** In §4, the dogmatic rule is minimax-loss but weakly dominated by BCOND. Note that minimax plus admissibility selects BCOND in the binary case.
- **Randomized mechanisms in §6.** The conditional analysis omits them. This is harmless, since the worst case lies at the endpoints r ∈ {0,1}, but it should be stated.
- **Vocabulary.** Map "mechanism" to M&Z's "learning situation" explicitly, and cite GEC via M&Z Fact 5 (representability by a map from prior space and proposition to posterior).

## Prior work this resembles (only if confident; author, year, title, confidence %)

Percentages are my confidence that each work exists as described.

**Closest results**
- Meehan & Zhang 2025, "Bayes Is Back," *Phil. Review* 134(3) — 100% (read in packet).
  - §5.3 Fact 11 (BCOND optimal iff the weighting is extensional), Lemma 1 (f(p) = π(·|λ_p)), Fact 12 (a single-situation weighting is extensional iff that situation is transparent), and fns. 21 and 39.
  - The essay's Props. 1–2 are instances once least-favorable weightings are computed. I am ~90% confident of this reduction in general and verified it in the binary case.
- Wald 1950, *Statistical Decision Functions* (minimax rules as Bayes against least-favorable priors) — 95%.
- Savage 1951, "The Theory of Statistical Decision," *JASA* 46 (regret criterion) — 90%.
- Milnor 1954, "Games against Nature," in Thrall, Coombs & Davis (eds.), *Decision Processes* (axioms separating Wald, Savage, Hurwicz and Laplace) — 90%; located online.

**Robust updating with an unknown reporting or coarsening mechanism**
- van Ommen, Koolen, Feenstra & Grünwald 2016, "Robust Probability Updating," *IJAR* 74: 30–57 — 100% that it exists. That Prop. 2 is a special case of its minimax-loss game — 80%.
- Grünwald & Halpern 2003, "Updating Probabilities," *JAIR* 19: 243–278 — 95% (Monty Hall, coarsening at random, naive vs refined spaces).
- Grünwald & Halpern 2011, "Making Decisions Using Sets of Probabilities: Updating, Time Consistency, and Calibration," *JAIR* 42: 393–426 — 95% (minimax updating; time inconsistency as different bookie games; when minimax amounts to conditioning or to ignoring information).
- de Cooman & Zaffalon 2004, "Updating Beliefs with Incomplete Observations," *Artificial Intelligence* (vol. 159, pp. 75ff. from memory) — 85% (vacuous model of an unknown incompleteness mechanism; conservative updating).
- Seidenfeld & Wasserman 1993, "Dilation for Sets of Probabilities," *Annals of Statistics* 21(3): 1139–1154 — 95%.

**Minimax regret, oracle benchmarks and dynamic consistency**
- Che, Li & Luo 2026, "Learning Against Nature: Minimax Regret and the Price of Robustness," arXiv:2602.15246 — 100%.
  - Overlap: binary state, quadratic loss, regret against an oracle who knows the data-generating process, ex-ante vs ex-post, and maxmin "no-learning" vs regret.
  - Difference: symmetric signals of unknown precision; closed forms only for a uniform prior; no factive set-valued reports.
- Lim & Park 2026, "Dynamically Consistent Statistical Decisions," arXiv:2607.10519 — 95%.
- Aradillas Fernández, Montiel Olea, Qiu, Stoye & Tinda 2024/2025, "Robust Bayes Treatment Choice with Partial Identification," arXiv:2408.11621 — 95%.
- Arieli, Babichenko & Smorodinsky 2018, "Robust Forecast Aggregation," *PNAS* 115(52) — 90% (regret against an omniscient aggregator who knows the information structure; the same benchmark structure as the essay's comparator).

**Opaque evidence and externalist updating**
- Schoenfield 2017, "Conditionalization Does Not Maximize Expected Accuracy," *Mind* 126(504) — 100% (from the M&Z bibliography).
- Bronfman 2014, "Conditionalization and Not Knowing That One Knows," *Erkenntnis* 79(4) — 100% (from the M&Z bibliography).

**Non-expected-utility evaluation of updating, and regret axioms**
- Campbell-Moore & Salow 2022, "Accurate Updating for the Risk-Sensitive," *BJPS* 73(3) — 95%. A useful contrast: a risk-weighted (REU) evaluation still yields conditionalization, while minimax regret over mechanisms does not.
- Stoye 2011, "Axioms for Minimax Regret Choice Correspondences," *JET* 146(6): 2226–2251 — 95%.

**Disclosure**
- Milgrom 1981, "Good News and Bad News: Representation Theorems and Applications," *Bell J. Econ.* 12(2) — 85%. Selective silence is informative ("unraveling"); E_a and E_b are verifiable-disclosure protocols.

## Claims that look false, misattributed or unverifiable

1. **Abstract, §4, §5: "does not require … counting some mechanisms more often" and "disagreement comes entirely from the comparator."** True of the criteria as stated, but misleading as a diagnosis. The regret solution *is* the Bayes/weighted-total solution for a non-uniform, non-extensional weighting (see above).
2. **§7: the "distinctive calculation" includes "the comparison between absolute loss, ex-ante regret, and conditional regret."** That kind of comparison is already in the literature:
   - Che, Li & Luo (2026, §2.2) contrast ex-ante and ex-post regret. They also remark that "our minimax regret criterion prevents the trivial no-learning outcomes typical of maxmin models".
   - Lim & Park (2026, §2.2) state that loss- and regret-based rules differ because "the oracle term" varies with the prior.
   - The conditional/unconditional Γ-minimax literature makes the same distinction.

   Only the factive-report and tautology instance is distinctive.
3. **§4: "Pettigrew (2016, §4) discusses minimax and minimax regret."** Unverified: I could not reach the text. The mathematical claim is correct: the omniscient credence has zero inaccuracy at every world, so regret equals inaccuracy. Pettigrew's 2016 book certainly discusses minimax regret (chapter "Hurwicz, regret, and 𝒞-maximin", pp. 168–182).
4. **"No News."** Presented as a known principle without attribution. I found no source that names it.
5. **§7's account of Che, Li & Luo.** Accurate but incomplete. It omits their ex-ante/ex-post contrast and their maxmin-vs-regret contrast, both of which overlap with what the essay claims as its own comparison.
6. **Abstract: "the former preserves the prior on receiving a tautology."** Correct ex ante only. Conditional minimax loss gives ½. The qualifier should be explicit.

## What is genuinely good (be specific: revisions must preserve this)

- **Correct derivations.** The derivations are correct, explicit and minimal. The four mechanisms are exactly M&Z's learning situations for |S| = 2: two transparent, two opaque. That makes this the right test bed.
- **Prop. 3 is the most technically elegant step.** Regret is a supremum of affine functions, hence convex in the kernel, so its maximum is at a vertex. The remark that the comparator knows the kernel but not the random seed is exactly right.
- **Good intuition.** The completing-the-square diagnosis (unavoidable error under N is what the absolute criterion fixates on) is the right intuition and is well explained.
- **Content vs occurrence.** §6 separates the content of a tautological report from the occurrence of an uninformative observation. That is the right philosophical distinction to build on.
- **Honest scope.** The essay notices that minimax loss does not single out BCOND without evidence-respectingness (the dogmatic rule ties). It does not overclaim.
- **Calibrated novelty claims.** §7 is unusually candid about what is and is not new. Keep that tone, but replace "provisional" with an actual literature finding.
- **The increment I credit.** An exact solution of the ex-ante minimax-regret problem for content-only (GEC) rules facing all factive report protocols in the binary case. Read correctly, it identifies a concrete non-extensional least-favorable weighting, √(1−p) : √p on the two opaque situations, and so concretely illustrates M&Z's Fact 11. Together with the conditional-regret contrast, this is all I credit as new. I found no prior statement of the square-root rule.

## Literature check

**What I searched.**
- The essay's four citations, against their sources.
- The square-root formula itself: "minimax regret" with "square root" and "prior odds" and "updating"; least-favorable priors in binary quadratic problems; robust forecasting.
- Minimax and minimax-regret updating under unknown coarsening or reporting mechanisms.
- Responses to "Bayes Is Back" that propose minimax or robustness criteria.
- The "No News" principle.
- Pettigrew 2016 on minimax regret.
- Risk-sensitive accuracy and updating (Campbell-Moore & Salow).
- Grünwald & Halpern 2003 and 2011; de Cooman & Zaffalon 2004.
- Robust forecast aggregation (Arieli et al.).
- Dynamic consistency of minimax regret (Lim & Park 2026) and robust-Bayes ex-ante vs ex-post (Aradillas Fernández et al.).
- Milnor 1954; Stoye 2011; Seidenfeld & Wasserman 1993.
- The disclosure/unraveling literature.

**What I found.**
- *No prior statement of the square-root rule.* I found none in this setting or in nearby ones. The formula is an elementary equalizer (weighted Chebyshev centre of {0,1}), so a stray appearance elsewhere cannot be ruled out. I am ~75% confident it has not been stated for robust updating on factive reports.
- *No published reply to M&Z.* I found none proposing worst-case or regret criteria.
- *Che, Li & Luo 2026.*
  - Setting: binary state, ex-ante regret against an oracle, quadratic loss.
  - Closed forms only for μ = ½; at n = 1, Nature mixes the uninformative and fully informative signals equally and the DM reports (¼, ¾).
  - It does contrast ex-ante with ex-post regret (§2.2) and maxmin with regret.
  - No coarsening or factive reports appeared in the parts I could read; its reference list was truncated in my view.
- *Lim & Park 2026.*
  - §2.2: loss and regret rules differ because the oracle term varies.
  - §3.1: least-favorable priors make both kinds of rule Bayes.
  - §§3.2, 4.3, 5.3: ex-ante minimax regret is unlikely to be dynamically consistent; an interim criterion via the updated least-favorable prior.
- *van Ommen et al. 2016.* Minimax expected loss over the coarsening ("quizmaster") strategy, with arbitrary message sets and (almost) arbitrary losses; RCAR for log loss. I could not read the full text (my fetch tool could not parse the PDF). From the abstract and memory, it does not treat regret (~75%).

**Attributions and citations.**
- *Confirmed:*
  - Meehan & Zhang 2025: bibliographic data; that GEC is their term and is accurately glossed (§4, Fact 5); that Hi-TEA uses totals over learning situations (§5.1).
  - van Ommen et al. 2016: title, *IJAR* 74: 30–57, DOI; the essay's description matches the abstract. The author-hosted URL resolves to a PDF with IJAR metadata.
  - Che, Li & Luo 2026: title, authors, arXiv number; the essay's description is accurate.
  - Pettigrew 2016: title, *PPR* 92(1): 35–59, and DOI 10.1111/phpr.12097. The author-version URL resolves to a PDF whose link annotation carries this DOI.
- *Not confirmed:* the content and section number of the Pettigrew 2016 §4 claim. Its text was unreachable: PhilPapers returned 403 and the PDF could not be parsed.
- *Not found:* any source for "No News" as a named principle.
- *Quotations:* the essay quotes no one directly, so there are none to check.
- *Packet rule:* I did not open locally saved copies of fetched PDFs.

## Proof check

- **§2 restriction to evidence-respecting rules.** Certainty on a singleton gives zero loss at the true state, so the minimum loss and regret are weakly reduced under every mechanism. ✓ For regret the restriction is forced, not merely harmless: departures raise a binding regret.
- **Loss table.**
  - L_N(q) = 2p(1−q)² + 2(1−p)q² = 2p − 4pq + 2q² = 2p(1−p) + 2(q−p)². ✓
  - L_{E_a} = 2p(1−q)² and L_{E_b} = 2(1−p)q². ✓
  - Comparators: m_N = 2p(1−p); m_{E_a} = m_{E_b} = m_R = 0. ✓ These equal META-COND's losses.
- **Prop. 1.**
  - Reg_{E_a} strictly decreases and Reg_{E_b} strictly increases on [0,1], and they cross. So the maximum of the two is uniquely minimized at p(1−q)² = (1−p)q², i.e. q* = √p/(√p+√(1−p)). ✓
  - V(p) = 2p(1−q*)² = 2p(1−p)/(√p+√(1−p))². ✓
  - With u = √p, v = √(1−p): q* − p = u/(u+v) − u² = u(1 − u² − uv)/(u+v) = u(v² − uv)/(u+v) = uv(v−u)/(u+v). ✓ Then 2(q*−p)² = 2p(1−p)(u−v)²/(u+v)² ≤ V, because (u−v)² = 1 − 2uv ≤ 1. ✓ This holds strictly for p ∈ (0,1).
  - Odds: q*/(1−q*) = √(p/(1−p)). ✓
  - p = 4/5: q* = 2/3 ✓; V = 8/45 ≈ 0.1778 ✓; keeping q = p gives max regret 32/125 = 0.256 at E_b ✓; N's regret at q* is 8/225 ≈ 0.0356 ✓.
- **Prop. 2.** L_N ≥ 2p(1−p), with equality iff q = p. At q = p, L_{E_a} = 2p(1−p)² and L_{E_b} = 2(1−p)p², both ≤ 2p(1−p), and L_R = 0. ✓ Unique within the evidence-respecting class ✓. The dogmatic rule also attains 2p(1−p) everywhere ✓, so §4's caveat is right.
- **Prop. 3.**
  - L_K is affine in (α, β). ✓
  - Reg_K(q) = sup_r [L_K(q) − L_K(r)] is convex in K, so its maximum over the square is at a vertex. ✓
  - For interior K, the comparator is Bayes on S, giving r = pα/(pα+(1−p)β) and m_K = 2pα(1−p)β/(pα+(1−p)β). This is consistent with the proof.
- **§6, conditional regret.** E_a gives 2(1−q)², E_b gives 2q², N gives 2(q−p)². Hence q = ½, and N does not bind. ✓ With randomized K, the posterior r ranges over [0,1] and the conditional regret is 2(q−r)², so the answer is the same. Conditional minimax *loss* also gives ½: max_r [2r(1−q)² + 2(1−r)q²] = max{2(1−q)², 2q²}. The essay omits this.
- **My additions, verified.**
  - The saddle point (q*, λ*) with λ*(E_a) : λ*(E_b) = √(1−p) : √p and λ*(N) = λ*(R) = 0. ✓
  - M&Z Lemma 1 reproduces q*. ✓
  - The least-favorable kernel K* gives Bayes posterior q* (p = 0.8: 1/3, 2/3 → 2/3). ✓
  - Log-score equalizer for p = 0.8: q⁴ = 1 − q, so q ≈ 0.7245. ✓
  - Three-state √π counterexample: ≈ 0.258 vs ≈ 0.165. ✓
  - Dana space: BCOND's Brier inaccuracy 1.188 > the prior's 1.12, using M&Z's Table 1 numbers. ✓

**Verdict on the mathematics:** sound throughout. The weaknesses are in interpretation, generality and literature, not in the algebra.

## Top five changes (most important first)

The essay uses about 2,450 of 6,000 words. The extra ~3,500 should buy the following.

1. **Reframe around least-favorable weightings (~700 words).**
   - State and prove: for any finite prior space and convex strictly proper inaccuracy, every ex-ante minimax-regret GEC rule equals M&Z's Lemma-1 rule π(·|λ*_p) for a least-favorable λ*, on every proposition with positive weight. (Proof: Sion plus M&Z Lemma 1.) It is BCOND there iff λ* is extensional.
   - Derive Prop. 1 as the binary corollary, with λ* ∝ (√(1−p), √p) on (E_a, E_b).
   - Derive Prop. 2 as λ* = δ_N, which is extensional by Fact 12.
   - Rewrite the abstract and §§4–5 accordingly, dropping "does not require counting mechanisms more often."
   - Add the as-if protocol K*.
2. **Generalize (~1,000 words).**
   - (a) Other strictly proper scores in the binary case. Prove the "strictly between ½ and p" claim under a stated condition on the score, and give the log-score value.
   - (b) n states. Show that the closed form fails, characterize what survives, and treat the coupling across report sets.
   - (c) Prove that ex-ante minimax loss forces No News in every finite prior space but does not select BCOND (Dana, via M&Z Fact 3). That turns a binary curiosity into a result about the M&Z dialectic.
3. **Settle the model and meet the advocate (~800 words).**
   - Commit to M&Z's learning-situation reading (E_a and E_b are opaque); separate it from the Monty Hall source reading (Grünwald & Halpern 2003; M&Z fn. 21; Bronfman 2014).
   - Name the comparator as META-COND (Schoenfield 2017; M&Z Facts 2 and 8).
   - Answer the objection that regret against a contrastive rule's accuracy reintroduces contrastiveness.
4. **Fix the timing section (~450 words).**
   - Add the ex-post minimax-loss result (½, via dilation).
   - Say explicitly that the loss/regret contrast is ex-ante only.
   - Adopt or reject Lim & Park's least-favorable-posterior interim criterion, which makes q* dynamically consistent.
   - Cite Grünwald & Halpern 2011, Che, Li & Luo §2.2, Lim & Park 2026 and Aradillas Fernández et al.
5. **Give the normative argument the essay now leaves open (~550 words).**
   - Use Milnor's column-linearity axiom (and Stoye 2011) to pose sharply whether epistemic rule evaluation should be invariant to mechanism-specific constant shifts in inaccuracy.
   - Take a side.
   - Show what intermediate criteria (Hurwicz/GHC; an ε-contamination class around N) do to q.
   - Along the way, define and source "No News" and delete "novelty status still provisional."
