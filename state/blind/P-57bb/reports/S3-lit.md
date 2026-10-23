# Referee report — S3 Decision theorist (foundations and extreme stakes), G3 literature-expert standards — P-57bb

## Thesis and argument as I understand them (≤120 words)

Take a binary prior p and an unknown factive reporting protocol: full revelation, no disclosure, or selective silence. The comparator is meta-conditionalization. Against it, the ex-ante minimax-regret response to the tautological report S is the equalizer p·l_a(q) = (1−p)·l_b(q). Under Brier this is a square-root rule (2/3 at p = 0.8). Under log it is ≈0.7245. It returns the prior for every p only under boosting loss (Prop. 5). Minimax expected loss keeps the prior instead. The regret rule is Bayes against a least-favourable, non-extensional protocol weighting (Meehan–Zhang Fact 11), and conditional re-optimization undoes it. The output depends on score, comparator and timing. So regret licenses a forecasting policy, not a portable belief, unless a further bridge is supplied.

## Verdict
Prize: not finalist
Journal recommendation: reject. A resubmission reframed around the §7 weighting result could reach major revisions.

## Scores
Clarity: 7 | Argument: 6 | Significance: 4 | Originality: 5 | Literature: 5 | Accuracy: 7 | OVERALL: 5

## The single most serious problem

**Location.** §1, §7 (the "central normative claim") and §§9–10 (score portability).

**Problem.** The philosophical conclusion is close to true by definition, and its ingredients are established decision theory.

- §9 makes a "belief" a probability that does not change when an independently supplied proper elicitation score changes. Given that definition, Props 1, 4 and 5 deliver the conclusion at once.
- It is textbook (Wald 1950; Berger 1985) that minimax outputs are Bayes against least-favourable priors, and that those priors move with the loss and with the decision problem.
- It is also standard that an ambiguity-averse agent's "beliefs" form a set (Gilboa–Schmeidler 1989).
- Dynamically consistent updating of that set depends on the choice problem (Hanany & Klibanoff 2007).
- The essay names no philosopher who infers belief from regret-optimality. The only candidate is Che–Li–Luo's (CLL's) talk of "general-purpose beliefs". But CLL explicitly ground their score in a distribution over decision problems (their Thm 6, G'' = λ, following Schervish 1989). The essay itself concedes in §§9–10 that this "more evaluative conception of belief" is "substantive and coherent".

**Why it matters.** The dispute ends as a stand-off over how to use the word "belief". A well-informed decision theorist or formal epistemologist would learn that a familiar point holds in a clean toy model, and little more. The essay contains a sharper, attackable thesis (§7 and Major 1), but it is not the one argued.

## Major problems

1. **§7 — the essay's best idea is treated as a side remark.**
   - Minimax regret over learning situations selects a non-extensional least-favourable weighting whenever p ≠ 1/2.
   - Minimax loss selects an extensional weighting (all weight on N). It still cannot single out BCOND, because the constant-prior rule ties with it (§7, finite-state paragraph).
   - This answers the question Meehan & Zhang leave at "the bedrock of normative explanations" (p. 337): can a weight-free, robust notion of "most accurate in general" replace Hi-TEA's uniform weighting? The answer is no. Minimax loss underdetermines the rule, and minimax regret gives a non-Bayesian one.
   - That is a precise thesis about a recent *Philosophical Review* paper, and it is more interesting than "policy is not belief".
   - **Fix:**
     - Make this the thesis.
     - Prove it beyond the binary tautology case: three states with partial reports, or a general condition for when the least-favourable weighting is extensional.
     - Answer M&Z's own case for noncontrastiveness (idempotence, Fact 6, pp. 319–320). The regret comparator (META-COND) is exactly a contrastive rule, and §8 needs to meet that argument directly.

2. **§§1, 7, 9 — the overlap with Che, Li & Luo (2026) is understated.** Verified from the arXiv text, CLL already have:
   - ex-ante regret against an "Oracle" who knows the data-generating process (DGP);
   - any strictly proper score, via a Bregman generator G;
   - the triviality of maxmin, because Nature picks an uninformative DGP (fn. 1). This is essentially the moral of Prop. 2.
   - an n = 1 closed form (their Prop. 1);
   - the DM's rule as Bayes under Nature's worst-case mixture, from the first-order condition. This is essentially §7's "least-favourable weights are weights".
   - a task-aggregation grounding of the score (Thm 6).

   The essay credits CLL only with the regret/maxmin contrast, single versus repeated learning, and timing. A specialist reader will see §7's Bayes-representation point as CLL's.
   **Fix:** state the increment over CLL exactly. As I read it, the increment is: factive coarsening rather than noisy signals of unknown precision; the general-loss binary equalizer; the boosting characterization; and the M&Z interpretation.

3. **§6, Prop. 5 — the philosophical work is overstated, and the analysis stops too early.**
   - (i) Preservation "for every regular binary prior" is a cross-prior property. An agent with a fixed p needs only p·l_a(p) = (1−p)·l_b(p). That is a codimension-one condition, and many scores meet it (any symmetric score at p = 1/2).
   - (ii) Boosting loss is strictly proper and symmetric, and its Bayes risk 2C√(p(1−p)) is the Hellinger affinity. The essay gives no reason why a regret theorist may not adopt it. By the essay's own theorem, adopting it supplies the "bridge" in the binary case. "Highly specific" is not an objection.
   - (iii) The essay does not say whether boosting regret gives content conditionalization for partial reports when there are three or more states.
   - (iv) The essay misses that scores within its own class can make regret **extremize**.
     - Take weight function ω(q) = [q(1−q)]^{a−1} with a ∈ (−1, −1/2), e.g. a = −3/4. The normalization l_a(1) = l_b(0) = 0 still holds, and the score is strictly proper, monotone and C¹.
     - Yet D(p) := p·l_a(p) − (1−p)·l_b(p) is positive just above 1/2: D′(1/2) = l_a(1/2) + l_b(1/2) − ω(1/2)/2 ≈ 8.7 − 5.66 ≈ +3.
     - D is also positive as p → 1, where D ~ (8/3)(1−p)^{1/4}.
     - Since A − B is decreasing, D(p) > 0 implies q_L > p: the regret response to S is more extreme than the prior. (My computation.)
     - Within this symmetric Beta family, the computed cases line up by tail weight:

       | Score | a | Equalizer at p = 0.8 | Movement |
       |---|---|---|---|
       | §6 polynomial | 2 | ≈0.640 | shrinks |
       | Brier | 1 | 0.667 | shrinks |
       | log | 0 | 0.7245 | shrinks |
       | boosting | −1/2 | 0.8 | none |
       | a = −3/4 | −3/4 | > p | extremizes |

   - **Fix:** prove the dichotomy. Prop. 5 then becomes a real dividing line (shrinking vs extremizing regret). §6's hedge that direction is "not universal" becomes a result, and the essay's thesis gets stronger: the choice of score can push the "belief" either way from the prior.

4. **§9, the bet — the decisive version of the portability argument is never computed.**
   - Take p = 0.8 and a bet on a at price c = 0.75.
   - Regrets of the responses to S: declining is regretted 0.2 under E_a and 0.05 under N; accepting is regretted 0.15 under E_b.
   - So the pure minimax-regret act is to *accept*, whereas acting on the Brier "belief" 2/3 says decline.
   - With mixed acts, the rule is: accept with probability 4/7. The least-favourable weights are 3/7 on E_a and 4/7 on E_b, which imply a posterior on S of exactly 0.75.
   - In general, for every binary bet at price c, the least-favourable posterior equals c (N never binds). The dual "belief" is just the indifference point of whatever problem is posed.
   - This turns the hedged §9 ("a complete policy … might still recommend declining") into a demonstration: the minimax-regret "posterior" belongs to the decision problem, not to the evidence.
   - **Fix:** replace the hedged paragraph with this computation and its generalization. It is a standard 2×2 equalizer fact, so present it as an illustration, not a theorem.

5. **Throughout — the closest decision-theoretic and epistemological literature is missing.** (Details and verification status are in the Literature check.)
   - **Grünwald & Halpern 2003.** Coarsening at random (CAR) is the condition under which naive content-conditioning is correct. In this game, conditioning on S is right iff α = β.
   - **Hanany & Klibanoff 2007.** §9's "update the least-favourable joint model π K*" is their dynamically consistent update: Bayes applied to the priors relevant to the ex-ante choice. They show it depends on the choice problem, which is the essay's own point, already formalized.
   - **Milnor 1954; Stoye 2011.** §8's invariance of regret to mechanism-wise constants is Milnor's "column linearity". Regret's menu-dependence and IIA failure also belong here.
   - **Seidenfeld & Wasserman 1993.** Dilation (§9).
   - **Arieli, Babichenko & Smorodinsky 2018.** Minimax regret against an aggregator who knows the information structure.
   - **Manski 2007.** Minimax regret with an unknown missing-data mechanism.
   - **Lim & Park 2026.** Interim deviation from ex-ante minimax-regret rules.
   - **Accuracy-first epistemology:**
     - Leitgeb & Pettigrew 2010 and Levinstein 2012: the accuracy-based update depends on the score.
     - Pettigrew 2016: minimax accuracy yields indifference.
     - Babic 2019: the choice of score as an epistemic risk attitude.
     - Schervish 1989 and Levinstein 2017: scores as mixtures of decision problems. This is the defence §9 concedes.
   - **Opaque-evidence work cited by M&Z:** Bronfman 2014; Gallow 2021; Isaacs & Russell 2023; Ahmed & Salow 2019; Das 2023. §9's "source story vs learning-situation story" is close to M&Z's fn. 21 (opaque Monty Hall, Pearl's remark).

   Without these, the increment cannot be stated, and §§7–9 will read as rediscovery.
   **Fix:** add one focused related-work paragraph per section, paid for by cutting the repeated disclaimers.

## Minor problems

- **Uniqueness (Props 1, 4).** For regret, the restriction to evidence-respecting rules is unnecessary. At q_L, any uncertain response to a singleton adds strictly positive regret under E_a or E_b, so the equalizer is the unique minimax-regret rule outright. Say so: it sharpens the contrast with Prop. 2, where uniqueness genuinely needs the restriction.
- **Prop. 4 proof.** Spell out "opposite order at the endpoints": A(0+) > 0 = B(0+), A(1−) = 0 < B(1−), continuity on (0,1), then the intermediate value theorem. State "extend to zero at the correct certainty" as limits.
- **Terminology.** "Absolute loss" (Prop. 4 proof, §8) reads as L1 loss. Use "raw" or "unregretted" expected loss.
- **Page references for Meehan & Zhang.** Global evidential constancy is defined at p. 315, and Fact 5 (p. 316) is its content-map characterization. The META-COND-mimicking rule is in the proof of Fact 8 (pp. 342–343) and the discussion on p. 327. Give pages.
- **Boosting-loss source.** Cite a published source for the probability-scale form, e.g. Friedman, Hastie & Tibshirani 2000 (½-logit minimizer) or Reid & Williamson 2010. The Buja–Stuetzle–Shen manuscript is unpublished, and I could not check its "p. 2".
- **§6 bounded example.** It is the Beta(2,2)-weighted score, ω = 6q(1−q). Its equalizer at p = 0.8 is ≈0.640 (my computation), further from p than Brier's. Report this; it is what reveals the tail-weight ordering in Major 3.
- **§7 minimax-theorem paragraph.** Name the theorem (Sion). Note that interchangeability of saddle points is what licenses "any minimax-regret rule minimizes the λ*-weighted regret".
- **§9.** "A familiar form of dilation" needs a citation.
- **Definition of belief.** Define "belief" (a portable, evidence-determined summary) in §1, not implicitly in §9. Move "This is the central normative claim of the essay" from §7 into the introduction.
- **Disclaimers.** They recur (§1 ¶¶5–6, end of §7, §10). Cutting about a third would make room for the missing engagement.

## Prior work this resembles (only if confident; author, year, title, confidence %)

| Work | Relevance | Confidence / status |
|---|---|---|
| Che, Li & Luo 2026, "Learning Against Nature: Minimax Regret and the Price of Robustness", arXiv:2602.15246 | Same oracle-regret game aimed at "general-purpose beliefs"; arbitrary strictly proper score; worst-case-mixture Bayes form; maxmin triviality. Cited, but the overlap is understated. | 95%, verified |
| Grünwald & Halpern 2003, "Updating Probabilities", *JAIR* 19: 243–278 | Naive vs protocol-sensitive conditioning; CAR. | 95%, verified |
| van Ommen, Koolen, Feenstra & Grünwald 2016, "Robust Probability Updating", *IJAR* 74: 30–57 | Worst-case-optimal updating under unknown coarsening; RCAR. Cited. | 95%, verified |
| Hanany & Klibanoff 2007, "Updating Preferences with Multiple Priors", *Theoretical Economics* 2: 261–298 | The §9 "carry the least-favourable model forward" move; dependence on the choice problem. | 95%, verified |
| Arieli, Babichenko & Smorodinsky 2018, "Robust Forecast Aggregation", *PNAS* 115: E12135–E12143 | Regret against an aggregator who knows the information structure. | 90%, verified |
| Manski 2007, "Minimax-Regret Treatment Choice with Missing Outcome Data", *J. Econometrics* 139: 105–115 | Minimax regret under an unknown selection mechanism. | 90%; citation verified, content from memory |
| Lim & Park 2026, "Dynamically Consistent Statistical Decisions", arXiv:2607.10519 | Ex-ante minimax-regret rules and interim deviation. | 90%, abstract verified |
| Seidenfeld & Wasserman 1993, "Dilation for Sets of Probabilities", *Annals of Statistics* 21: 1139–1154 | Dilation. | 90%, not checked this run |
| Milnor 1954, "Games Against Nature", in Thrall, Coombs & Davis (eds.), *Decision Processes* | Column linearity of regret. | 90%, not checked |
| Stoye 2011, "Axioms for Minimax Regret Choice Correspondences", *JET* 146: 2226–2251 | Axiomatics and menu-dependence of regret. | 80%, not checked |
| Leitgeb & Pettigrew 2010, "An Objective Justification of Bayesianism II", *Phil. Sci.* 77: 236–272 | Score-dependence of accuracy-based updating. | existence verified |
| Levinstein 2012, "Leitgeb and Pettigrew on Accuracy and Updating", *Phil. Sci.* 79: 413–424 | Same. | 80%, not verified |
| Pettigrew 2016, "Accuracy, Risk, and the Principle of Indifference", *PPR* 92: 35–59 | Minimax accuracy in accuracy-first epistemology. | 80%; minimax argument confirmed indirectly via Babic |
| Babic 2019, "A Theory of Epistemic Risk", *Philosophy of Science* 86: 522–550 | Score choice as epistemic risk attitude. | existence verified; venue details 85% |
| Schervish 1989, "A General Method for Comparing Probability Assessors", *Annals of Statistics* 17: 1856–1879 | Scores as mixtures of decision problems. | 90%; listed in CLL's references |
| Levinstein 2017, "A Pragmatist's Guide to Epistemic Utility", *Phil. Sci.* 84: 613–638 | Same. | existence verified; details 80% |
| Friedman, Hastie & Tibshirani 2000, "Additive Logistic Regression: A Statistical View of Boosting", *Annals of Statistics* 28: 337–407 | Published source for the boosting score. | 95% |
| Reid & Williamson 2010, "Composite Binary Losses", *JMLR* 11: 2387–2422 | Probability-scale boosting partial losses and their weight function. | existence verified via arXiv 0912.3301; details 85% |

## Claims that look false, misattributed or unverifiable

- **Nothing false found.** Every claim about Meehan & Zhang checks out against the source; see the Literature check.
- **"Buja, Stuetzle, and Shen (2005, p. 2)."** The manuscript exists at the cited URL and is dated 3 Nov 2005, and it treats boosting loss as a proper scoring rule. The page of the display is **unverified**: the PDF could not be parsed.
- **"Che, Li, and Luo (2026, §2.2) also distinguish advance evaluation from conditional evaluation."** Only **partly supported**. Their §2.2 stresses that the rule is fixed before the signal is seen. "Interim regret" appears only in fn. 5, and CLL's own ex-ante/interim labels are inconsistent.
- **"Che, Li, and Luo (2026) already contrast minimax regret with worst expected loss."** Supported, but only by fn. 1 ("to avoid the triviality" of maxmin). It is a remark, not an analysis.
- **Unattributed overlap.** The §9 move "update the least-favourable joint model" is presented without credit, but it is Hanany & Klibanoff's (2007) dynamically consistent updating.
- **Quotations.** The essay contains no direct quotations, so there are none to check.
- **Grünwald & Dawid 2004.** Not checked this run; I am 95% confident it exists as cited.

## What is genuinely good (be specific: revisions must preserve this)

- **The formal results are all correct and cleanly proved.** I checked every one: the square-root rule and its numbers, the general equalizer, the boosting characterization, the vertex reduction for randomized protocols, the saddle point with kernel (1/3, 2/3), and the non-extensionality claim.
- **Everything is explicit and checkable.** There are four mechanisms. Randomization is handled through convexity in the kernel. Unbounded scores are handled without undefined expectations.
- **§7 connects minimax regret to M&Z's weighted-total machinery** (Fact 11, Lemma 1). Regret's least-favourable weighting is non-extensional; minimax loss's is extensional. This is the essay's most valuable idea and must survive revision.
- **The essay is honest about what it does not claim.** It says the robust rule is Bayesian for an explicit protocol, and it does not claim the boosting score as new. It separates receiving tautological content from knowing that the report was uninformative (§9), and keeps ex-ante and conditional evaluation apart.
- **§8's diagnosis is right and well put:** regret "removes that difficulty from the performance comparison; it does not remove the uncertainty from the evidence." It should be tied to the axiomatics of regret, not dropped.

## Literature check

**Calls used: 19 of 20.**

1. **Fetched arXiv:2602.15246 (abstract).** Confirmed Che, Li & Luo, "Learning Against Nature: Minimax Regret and the Price of Robustness", submitted 16 Feb 2026, econ.TH. The decision maker (DM) chooses posteriors to minimize ex-ante regret against Nature's DGP, and the paper explicitly aims at "general-purpose" beliefs.
2. **Fetched the CLL HTML (first part).**
   - §2.2: the rule is chosen before the signal; fn. 5 mentions "interim regret".
   - fn. 1: maxmin is rejected "to avoid the triviality".
   - Prop. 1 (n = 1): Nature mixes π = 1/2 and π = 1, and the DM responds (1/4, 3/4).
   - Any strictly convex G is allowed. The DM's rule is Bayes under Nature's worst-case mixture.
   - Task aggregation motivates the approach.
3. **Fetched the CLL HTML (second part).**
   - The main model uses MSE, and I found no explicit quadratic-vs-log comparison.
   - Thm 6: G'' = λ, the density of decision problems.
   - The visible references include Savage 1951, Schervish 1989, Siniscalchi 2009, Stoye 2009 and Wald 1950. The earlier part of the reference list was not visible.
4. **Search, van Ommen et al.** Confirmed *IJAR* 74 (2016): 30–57. The arXiv version was titled "Worst-case optimal probability updating", which supports the essay's "minimax expected loss".
5. **Fetched the arXiv:1512.03223 abstract.** RCAR characterizes optimality under log loss and, "under certain conditions", for a much larger class of losses. This supports the essay's description. The full PDF could not be parsed.
6. **Buja, Stuetzle & Shen 2005, fetch and search.** The PDF could not be parsed. Search confirmed the 3 Nov 2005 manuscript and that it covers boosting loss as a proper scoring rule. "p. 2" is not confirmed.
7. **Search for prior statements of Prop. 5.** None found. Reid & Williamson display the boosting partial losses ½√((1−q)/q) and ½√(q/(1−q)) with weight function 1/(4[q(1−q)]^{3/2}). The "balance" p·e^{−F} = (1−p)·e^{F} is the standard first-order condition of exponential loss (my derivation). Prop. 5 is thus a short corollary of a well-known property: true and apparently unstated in this form, but of modest originality.
8. **Search for prior statements of the square-root/equalizer rule** (silence, withheld reports, minimax regret). None found. It is a routine equalizer computation, so I would not call it known; I would not call it deep either.
9. **Search, Arieli et al.** Confirmed *PNAS* 115 (2018): regret against an aggregator who knows the information structure.
10. **Search, Grünwald & Halpern 2011.** Confirmed *JAIR*, pp. 393–426, DOI 10.1613/JAIR.3374. The paper attributes time inconsistency to "bookies with different information" and stresses Epstein–Schneider rectangularity. The essay's description is accurate.
11. **Search, Halpern & Leung 2016.** Confirmed *Theory and Decision* 81(1): 123–151, DOI 10.1007/s11238-015-9526-8. The topic is the menu-dependence of regret in dynamic problems. Accurate.
12. **Search, philosophy literature on minimax regret plus accuracy plus conditionalization.** No such paper found. Found Babic, "A Theory of Epistemic Risk" (which reports Pettigrew 2016a's minimax-accuracy argument for the principle of indifference), Levinstein, "A Pragmatist's Guide to Epistemic Utility", Schultheis, "Accurate Updating", and Lim & Park 2026.
13. **Fetched arXiv:2607.10519.** Lim & Park, "Dynamically Consistent Statistical Decisions" (12 July 2026): researchers may want to depart from the interim prescriptions of ex-ante-optimal rules such as minimax regret; the paper axiomatizes dynamically consistent alternatives.
14. **Search, Hanany & Klibanoff.** Confirmed *Theoretical Economics* 2(3): 261–298 (2007). Their update applies Bayes to a subset of priors that depends on the conditioning event, the feasible set and the chosen act.
15. **Search, Grünwald & Halpern 2003.** Confirmed *JAIR* 19: 243–278: naive conditioning is correct iff CAR holds, and CAR rarely holds.
16. **Search, Leitgeb & Pettigrew / Levinstein.** Confirmed Leitgeb & Pettigrew 2010 (Brier yields a non-Jeffrey update; log yields Jeffrey). Levinstein 2012 itself was not retrieved.
17. **Search, Manski 2007.** Confirmed *J. Econometrics* 139(1): 105–115.

**Attributions to Meehan & Zhang, checked against source_main.txt:**
- Bibliographic data ✓: *Phil. Rev.* 134(3), 2025, pp. 285–350, DOI ✓.
- Global evidential constancy, defined at p. 315; Fact 5 at p. 316 ✓.
- Fact 2 (p. 300) ✓.
- Fact 8 (p. 325), with the mimicking rule in its proof (pp. 342–343) ✓.
- λ_p(s) = Σ_{E: E(s)=p} λ(E) and extensionality (p. 336) ✓.
- Fact 11 (p. 337) ✓.
- Lemma 1 (p. 344): posterior ∝ π(s)λ_p(s) ✓.
- The zero-weight caveat matches fn. 39 ✓.

No misattribution.

## Proof check

- **Prop. 1 ✓.**
  - L_N = 2p(1−p) + 2(q−p)² by expansion. The regret table is right.
  - The equalizer gives q* = u/(u+v) and V = 2p(1−p)/(u+v)².
  - q* − p = uv(v−u)/(u+v). Hence 2(q*−p)² = V·(u−v)² ≤ V, since (u−v)² = 1 − 2uv ≤ 1.
  - Uniqueness ✓.
  - At p = 4/5: q* = 2/3, V = 8/45, keeping p costs 32/125, and N-regret at q* is 8/225 ✓.
  - Odds identity ✓.
- **Prop. 2 ✓.** The remark about the constant rule is also right (it is M&Z's dogmatic rule).
- **Prop. 3 ✓.** L_K is affine in (α, β). The comparator's value inf_r L_K(r) is concave, so regret is convex in K and maximized at a vertex.
- **Prop. 4 ✓, with a small gap.** The intermediate-value step needs the endpoint limits, which the stated assumptions do supply.
  - M ≤ max{A(p), B(p)} ≤ H(p), so the N-regret 2M − H(p) ≤ M ✓.
  - The minimax-loss part ✓, including randomized kernels.
- **Log example ✓.** The equalizer reduces to q⁴ = 1 − q, with root ≈0.72449.
- **Prop. 5 ✓.**
  - The derived ODE (1−2q)h + 2q(1−q)h′ = 0 is right.
  - It gives h = C/√(q(1−q)), unique up to C because h > 0.
  - The converse via t = √(q/(1−q)) is correct, and both wrong-certainty losses diverge.
- **§6 polynomial score ✓.** The derivatives are right; the propriety derivative is 6q(1−q)(q−p); the score is symmetric; the values 2/45 vs 8/135 are right. Its equalizer is ≈0.640 (mine).
- **§7 ✓.**
  - The mixture's minimizer is u/(u+v), at which point the component regrets are equal, giving a saddle point.
  - K* = (v/(u+v), u/(u+v)), i.e. (1/3, 2/3) at p = 0.8. Bayes on S gives q*.
  - w_S is non-constant iff p ≠ 1/2. The all-N weighting is extensional.
  - The finite-state minimax-loss preservation claim is correct.
  - The Sion argument with convex losses is correct (interchangeability of saddle points).
- **§9 ✓.**
  - The posterior r ranges over all of [0,1].
  - Conditional minimax, under both regret and loss, gives 1/2.
  - The bet arithmetic is right, but see Major 4: the direct minimax-regret act for that bet is to accept.

No stated result fails. Two additions came out of the check:
- regret uniqueness holds without the evidence-respecting restriction;
- heavier-tailed proper scores inside the stated class make regret extremize (Major 3(iv)).

## Top five changes (most important first)

1. **Re-centre the thesis on Meehan–Zhang.** State and prove that weight-free robust aggregation over learning situations cannot vindicate BCOND:
   - minimax loss ties BCOND with the dogmatic rule and others;
   - minimax regret selects non-extensional least-favourable weights whenever p ≠ 1/2.

   Extend this beyond the binary tautology case: a three-state example with partial reports, or a general extensionality condition. Answer M&Z's idempotence/noncontrastiveness rationale (Fact 6), since the regret comparator is contrastive. Cite their "bedrock" remark (p. 337) and fn. 21.

2. **Replace the hedged bet paragraph in §9 with the decisive computation.** At p = 0.8 and c = 0.75, the pure minimax-regret act is to accept, while the Brier "belief" 2/3 says decline. With mixed acts, accept with probability 4/7. The least-favourable posterior is exactly c, for every binary bet at price c. This makes non-portability a demonstrated fact, not a suggestion.

3. **Turn Prop. 5 into a dichotomy.** Show that, within the class, scores lighter-tailed than boosting shrink the response toward 1/2, and heavier-tailed ones extremize. My computed case is ω = [q(1−q)]^{−7/4}; state the result exactly, at least for the symmetric Beta family. Also:
   - say whether a defender may adopt boosting loss;
   - say whether boosting regret yields content conditionalization beyond the binary tautology.

4. **State the increment over CLL precisely.** List what CLL already have (oracle regret, Bregman scores, maxmin triviality, worst-case-mixture Bayes form, Thm 6 task grounding). Then integrate:
   - Hanany & Klibanoff 2007 for §9's "carry the least-favourable model forward";
   - Grünwald & Halpern 2003 / CAR for the binary game (content conditioning is right iff α = β);
   - Milnor 1954 / Stoye 2011 for §8's constant-shift and menu-dependence points;
   - Seidenfeld & Wasserman 1993 for dilation;
   - Arieli et al. 2018, Manski 2007 and Lim & Park 2026.

5. **Engage the accuracy-first literature on score choice and non-expected-accuracy decision rules.** This means Leitgeb & Pettigrew 2010 with Levinstein 2012, Pettigrew 2016, Babic 2019, and Schervish 1989 with Levinstein 2017 (the task-distribution defence that §9 concedes). Define "belief" as a portable evidential summary in §1. Cut roughly a third of the repeated disclaimers to stay within 6,000 words.
