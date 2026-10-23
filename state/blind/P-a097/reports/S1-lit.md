# Referee report — S1 Formal epistemologist (Bayesian foundations), held to G3 literature-expert standards — P-a097

## Thesis and argument as I understand them (≤120 words)

If you normalize Meehan and Zhang's (M&Z) evaluative weights, you get a factive reporting kernel. Their "extensionality" is then exactly coarsening at random (CAR), and their Fact 11 is CAR-ignorability combined with strict propriety. The essay asks when such a benchmark can be "transported" to a coarser description by pushing forward both states and reports. Prop. 1 (no prior) and Prop. 2 (one CAR kernel, regular prior) show that CAR survives every coarsening only for kernels that report either the singleton or the whole space. Such kernels cannot rank rules on partial evidence. Prop. 4 gives an exact test for a given compression. Conclusion: carrying an accuracy justification between descriptions needs an independent account of evidential equivalence.

## Verdict
Prize: not finalist
Journal recommendation: reject (as it stands; a reframed short note built on Top-five changes 1–2 could be publishable)

## Scores
Clarity: 7 | Argument: 6 | Significance: 5 | Originality: 5 | Literature: 4 | Accuracy: 7 | OVERALL: 5

## The single most serious problem

**Location:** §1 (the "tempting" extension) and §9 ("fresh construction", the "privileged-grain" reply, the identification problem).

**Problem.** The essay attacks a transfer of M&Z's benchmark by transport. Nobody it cites makes that transfer, and M&Z's principle is built the other way.

- **Hi-TEA is already fresh construction.** Hi-TEA is "highest total expected accuracy relative to every prior space" (p. 330). That is the essay's "fresh construction", applied at every grain.
- **M&Z already make adequacy of the coarse model an explicit precondition.** Their noncontrastiveness slogan is "same prior over S, same evidence about S, same posterior over S" (p. 309). They make it conditional on the model being "formally adequate" (n. 22, p. 312). The Litmus Test (pp. 310–311) shows the problem with coarse models. They concede that "the adequacy of such formal models is a subtle issue, especially in an externalist setting" (n. 19, p. 311). They answer Monty-Hall-type cases by fine-graining S to capture "the agent's total incremental evidence" (n. 21, p. 311).
- **The essay re-runs this dialectic without citing it.** Its §9 privileged-grain reply and its identification problem cover the same ground.

**Why it matters.**

1. The headline philosophical conclusion largely restates a caveat M&Z already make, so its significance is small.
2. The essay misses its best contribution. Prop. 4 is, in substance, an exact criterion for when a coarse prior space is adequate in M&Z's sense. That is, it says when two agents who share the coarse prior and receive the same coarse report must agree on the correct posterior.
3. The §9 identification problem is precisely a coarse-level failure of M&Z's global evidential constancy. Yet the essay never mentions noncontrastiveness or global evidential constancy.

Aimed instead at an extension nobody is shown to hold, the formal results only measure how costly a demand is that the essay itself calls unreasonable ("The strongest objection to universal compatibility is correct", §7).

## Major problems

1. **§§4–5 and §9: the normative premise behind transport.**
   - *Problem.* Props. 1–2 assume that normalized importance weights should push forward under coarsening like chances, averaged with the agent's prior inside each fiber. M&Z's λ measures how epistemically important an updating problem is (pp. 335–336). Note 35 (p. 330) calls total expected accuracy an objective measure "for any agent, irrespective of their uncertainties about their evidential situations." Nothing in that reading says importance aggregates this way. The transported coarse kernel K̄_π depends on the prior within fibers, so it is not fixed by the coarse prior space (T, π̄).
   - *Why it matters.* The §9 claim that the transported benchmark "continues to be objective in whatever sense its original weights were objective" is unargued. Without that argument, Props. 1–2 price a premise that has not been motivated.
   - *Fix.* Either defend transport through the joint-measure form Σ_s π(s) Σ_P λ_P(s) A(f(P), s), which does transport cleanly, and say why that is the right object. Or present Props. 1–2 as a conditional reductio of a view that is explicitly attributed. The natural hook is M&Z's Bayesian who insists extensionality "cuts epistemology at its joints" (p. 337).

2. **§3 and §9: the essay never connects to global evidential constancy.**
   - *Problem.* The essay's "content-based rules" are exactly M&Z's globally evidentially constant rules (Fact 5, p. 316). The essay never says so. Nor does it say that likelihood-sensitive coarse updating violates global evidential constancy at grain T. That violation is M&Z's Litmus structure.
   - *Why it matters.* This is the strong point of contact with the target. Without it, the essay engages only the weaker one (Fact 11).
   - *Fix.* State and prove the corollary of Prop. 4: correct updating on the transported problem is globally evidentially constant at grain T, for every regular prior within fibers, iff g_Q is constant on fibers and the coarse kernel is CAR. Then present this as an exact adequacy condition for M&Z's coarse models.

3. **Literature: four references, and the closest prior work is missing.**
   - *Missing works.*
     - Halpern & Koller (2004) has the essay's architecture: unrestricted representation independence forces triviality (for them, "essentially entailment"), and invariance under a restricted class of transformations is the constructive compromise.
     - The origins of CAR are not credited: Heitjan & Rubin (1991), and Gill, van der Laan & Robins (1997), to whom Grünwald & Halpern themselves attribute their Theorem 3.1.
     - van Ommen, Koolen, Feenstra & Grünwald (2016) treat updating under proper losses when the coarsening mechanism is unknown. That is exactly the §9 identification predicament, and they give a minimax answer.
     - Grünwald's "Safe Probability" covers distributions that are reliable for some aspects of a problem and not others. That is the §10 idea of "evidential equivalence for a purpose."
     - Schoenfield (2017) is missing. Her META-COND, conditioning on the event that E = p, is Grünwald & Halpern's "sophisticated conditioning" for deterministic mechanisms, and BCOND is their "naive conditioning." This is the bridge from CAR to the opacity debate the essay is about.
   - *Fix.* Cite these and state the increment over each, above all over Halpern & Koller.

4. **§§4–7: the formal increment is small.**
   - *Problem.* Every result is a few lines.
     - Prop. 1 follows from two-point projections plus inclusion–exclusion.
     - Prop. 2 is the monotonicity in formula (3).
     - Prop. 3 is a one-step corollary.
     - Prop. 4 is CAR (Theorem 3.1 of Grünwald & Halpern / Gill, van der Laan & Robins) applied to a pushforward, plus "an average that is constant under every positive weighting has equal components."
   - All are correct. But the payoff for the M&Z debate is, by the essay's own account, nil: "This does not refute an accuracy argument formulated on a fixed state space."
   - *Fix.* Compress Props. 1–3 into one theorem with remarks, and use the space for a result that bears on M&Z's central claim. Top-five change 2 sketches one within reach of the essay's own CCAR toolkit.

5. **§9: length and focus.**
   - *Problem.* About twenty paragraphs of objection and reply. Several restate the identification problem, the role of idealization, or the "primitive kernel" reply. Meanwhile the decisive engagement, with M&Z on adequacy of the model, is absent.
   - *Fix.* Cut §9 by half and engage pp. 309–312 and 337–338.

## Minor problems

- **§1 misdescribes M&Z.** "A rule can perform optimally against every problem in one benchmark…" M&Z stress the opposite. Facts 3 and 8 (pp. 302, 325) show that no globally evidentially constant rule is optimal in every problem; BCOND wins only in total.
- **§7: the cross-pair witness is degenerate.** It is meant to show that saturation is not necessary. But its coarse experiment always reports {A,B}, so it is uninformative and trivially CAR. An informative witness:
  - Use the same S and ρ.
  - Set c_{s} = 1/2 for each singleton and c = 1/4 for each cross-pair. Row sums are 1, and no fine report is saturated.
  - The coarse kernel reports {A} (or {B}) with probability 1/2 and {A,B} with probability 1/2 at every state. It is CAR for every prior.
- **§7: say what prior-independence buys.** Prop. 4's prior-free condition splits into two parts:
  - (a) g_Q is constant on each fiber. This is the analogue of Kemeny–Snell *strong* lumpability; the fixed-prior version is the analogue of *weak* lumpability.
  - (b) The coarse kernel is CAR.
- **§2: credit the source of Theorem 3.1.** Grünwald & Halpern attribute their Theorem 3.1 to Gill, van der Laan & Robins (1997) (arXiv version, p. 8).
- **§§5–7: regularity is essential and should be flagged.** If π(t) = 0 is allowed, brackets in (3) can vanish and partial reports survive. M&Z also assume regularity (p. 290).
- **Abstract and §10: specify the stability notion.** "Maximal universally stable class" covers two different notions: fiberwise distributional compatibility (Prop. 1) and CAR after prior-averaging (Prop. 2).
- **§8: name the debate it bears on.** It bears on the internalist reply that evidence consists of perceptual appearances, which M&Z flag (p. 295). Say so.

## Prior work this resembles (only if confident; author, year, title, confidence %)

- Halpern & Koller, 2004, "Representation Dependence in Probabilistic Inference," *JAIR* 21: 319–356. **97%, verified.** Same architecture as Props. 1–2 plus Prop. 4: unrestricted invariance forces triviality; restricted invariance is the compromise. Not cited.
- Grünwald & Halpern, 2003, "Updating Probabilities," Prop. 4.1. **99%, verified.** CAR holds for all distributions iff the observations are pairwise disjoint. Cited and correctly distinguished. The §7 "negative companion" and Prop. 2 are its siblings.
- Jaeger, 2005, "Ignorability in Statistical and Probabilistic Inference," *JAIR* 24, Theorem 4.17. **99%, verified.** Robust CAR iff CCAR. Cited and correctly distinguished.
- Gill & Grünwald, 2008, "An Algorithmic and a Geometric Characterization of Coarsening at Random," *Ann. Statist.* 36(5). **99%, verified.** Cited.
- Heitjan & Rubin, 1991, "Ignorability and Coarse Data," *Ann. Statist.* 19(4). **97%.** Origin of CAR. Not cited.
- Gill, van der Laan & Robins, 1997, "Coarsening at Random: Characterizations, Conjectures, Counter-Examples" (Springer, Seattle Symposium proceedings). **95%.** Source of the characterization the essay attributes to Grünwald & Halpern. Not cited.
- van Ommen, Koolen, Feenstra & Grünwald, 2016, "Robust Probability Updating," *IJAR* 74: 30–57. **97%, verified.** Not cited.
- Grünwald, "Safe Probability," arXiv:1604.01785 (2016). **95% that the preprint exists, verified.** I believe it was later published in *J. Statist. Plann. Inference* (~70%, unverified). Not cited.
- Kemeny & Snell, 1960, *Finite Markov Chains*. **90%.** Strong vs weak lumpability is the template for Prop. 4's prior-free vs fixed-prior criterion. Not cited.
- Walley, 1996, "Inferences from Multinomial Data: Learning about a Bag of Marbles," *JRSS B* 58. **85%.** Representation Invariance Principle: invariance under merging and refining categories, which precise Dirichlet/Carnapian rules meet only in degenerate limits (that detail ~70%). Same "invariance under merging forces degeneracy" pattern as Prop. 1. Not cited.
- Schoenfield, 2017, *Mind* 126: 1155–87 (listed in M&Z's bibliography). **99%.** META-COND = sophisticated conditioning. Not cited.

## Claims that look false, misattributed or unverifiable

- **§1, "perform optimally against every problem in one benchmark."** Misleading about M&Z (Facts 3 and 8). BCOND maximizes the *total*, not each problem.
- **§2, Theorem 3.1 credited to Grünwald & Halpern.** Correct as a location, but they attribute it to Gill, van der Laan & Robins (1997). CAR's originators (Heitjan & Rubin 1991) go uncredited.
- **§9, "The transported benchmark continues to be objective in whatever sense its original weights were objective."** Contestable. The coarse kernel depends on the prior within fibers. This sits in tension with M&Z n. 35 (p. 330) and is not argued.
- **§10, "The additional contribution is to identify the maximal universally stable class and a precise alternative to universal stability."** I found no prior statement of the classification, so it is plausibly new as stated. But the novelty claim should be qualified by Halpern & Koller (2004), who have the same two-part architecture.
- **§§1 and 9, the "tempting" extension.** It is not attributed to anyone, and Hi-TEA's "relative to every prior space" (p. 330) suggests M&Z do not hold it.
- **No formal claim is false** (see Proof check). The essay contains no verbatim quotations, so quotation accuracy is not at issue.

## What is genuinely good (be specific: revisions must preserve this)

- **The §3 dictionary.** It maps λ to the kernel K_λ(P|s) = λ_P(s)/Λ (factive), gives the product-measure converse λ(E) = ∏_s K(E(s)|s), and identifies uniform weights with the uniform-subset kernel.
  - This correctly shows that M&Z's Lemma 2 is the classical CAR characterization, and implicitly that their Fact 12 is its deterministic special case.
  - M&Z do not cite the CAR or ignorability literature. Bringing it in is a real service to the accuracy-first literature.
- **Formula (3) and the proof of Prop. 2** form a clean monotonicity argument. Prop. 3 is the honest quantitative companion. The essay is right that approximate preservation does not bound posterior error after low-probability reports.
- **§6 ("a tautology with a likelihood")** is a vivid and correct example: 3/4 vs 1/2, posterior 4/7.
- **§8's example** (a transparent fine partition yields a non-CAR coarse kernel) is apt and not overstated. Two good lines: "apparent opacity can have a representational source", and "adding facts to a model and adding those facts to the agent's evidence are different operations."
- **The claims are well calibrated.**
  - The essay explicitly denies representation dependence of Bayesian probability itself (§6).
  - It explicitly denies refuting fixed-space accuracy arguments (§§4, 9).
  - It correctly distinguishes its stability notion from Grünwald & Halpern's Prop. 4.1 and from Jaeger's robustness/CCAR (§8).
- **Every attribution I could check is accurate** (see Literature check).

## Literature check

**Searches and fetches run (18 web operations).**
1. "Bayes Is Back" + extensionality + "coarsening at random": no work connecting M&Z's extensionality to CAR.
2. Responses to "Bayes Is Back" (two searches, including "Hi-TEA"/"highest total expected accuracy" 2026): no published reply found. Unverified lead: an Aristotelian Society 2025–26 programme item titled "II—Plans, Learning, and Deferring" surfaced in these searches. Search tools gave conflicting authorship and I could not read it, so I make no claim about its content.
3. Grünwald & Halpern 2003 (arXiv abstract and full PDF read).
4. Jaeger 2005 (the DOI redirect and JAIR page failed, giving 502; arXiv 1109.2143 PDF read, pp. 904–913).
5. Gill & Grünwald (arXiv 0811.0683 abstract and journal reference; arXiv math/0510276v3 HTML).
6. Halpern & Koller 2004.
7. CAR preserved under collapsing or merging categories: no prior statement of Props. 1/2 or of the transport criterion found.
8. CAR in philosophy and accuracy work: led to van Ommen et al. 2016, which I then confirmed.
9. Grünwald, "Safe Probability."
10. Coarse-graining, opacity and appearances in the externalism literature: nothing directly on point.

**Prior statements of the essay's exact results.**
- **Extensionality = CAR:** I found none. It is a short observation, but apparently not in print.
- **Props. 1–2:** I found none. The closest are Grünwald & Halpern Prop. 4.1, Jaeger Theorem 4.17, and the "invariance forces degeneracy" results of Halpern & Koller (2004) and Walley (1996).
- **Prop. 4:** not new as mathematics. It is CAR (Theorem 3.1) applied to the pushforward coarse-data distribution, plus a lumpability-style prior-free strengthening. It is new only as a stated criterion in this setting.

**Attributions confirmed.**
- M&Z 2025, *Phil. Review* 134(3): 285–350, DOI 10.1215/00318108-11873775. Confirmed (source pp. 285, 350).
- "M&Z (§§5.1–5.3) assess rules by total accuracy over learning situations for a fixed prior space." Confirmed: pp. 327–338; definition p. 329; weighted version p. 335.
- "Fact 11: extensionality necessary and sufficient." Confirmed: p. 337. Extensionality is defined on p. 336 via λ_p(s) = Σ_{E: E(s)=p} λ(E), and the essay's restatement is faithful.
- "Substance of Fact 11 and Lemmas 1–2." Confirmed: Lemmas 1–2, pp. 344–345.
- "Their proposal explicitly fixes a state space." Confirmed: p. 329; n. 33, p. 328. But see the Hi-TEA quantifier on p. 330.
- Grünwald & Halpern §§1–3 and Theorem 3.1 on naive vs sophisticated conditioning. Confirmed (arXiv pp. 1–3, 8), with the caveat that they attribute Theorem 3.1 to Gill, van der Laan & Robins (1997).
- Grünwald & Halpern Prop. 4.1. Confirmed verbatim (arXiv p. 10): "The CAR condition holds for all distributions Pr on R if and only if O consists of pairwise disjoint subsets of W." The essay's paraphrase is accurate.
- Gill & Grünwald 2008, *Ann. Statist.* 36(5): 2409–2422. Confirmed: arXiv journal reference.
  - "CAR polytope": confirmed.
  - Partition mechanisms are extreme points: confirmed via their extremality criterion.
  - "explain the contrast with general CAR": confirmed in the arXiv v3 preprint, which discusses CCAR and Jaeger's Theorem 4.17. Published wording not checked.
- Jaeger 2005, *JAIR* 24: 889–917. Confirmed.
  - Theorem 4.17 (p. 913) states the equivalence of: robust-car Bernoulli model, robust-ccar Bernoulli model, honest Bernoulli model, and d-ccar. Confirmed.
  - "CCAR = select a partition independently of the state and report the actual cell." Confirmed: Example 4.4 (multiple grouped data model), p. 907.

**Not independently verified.** Grünwald & Halpern's *JAIR* 19: 243–278 and DOI 10.1613/jair.1164. The arXiv page says only "to appear, JAIR", and my JAIR fetch for Jaeger failed. The details are consistent with my recollection.

## Proof check

| Result | Verdict | Notes |
|---|---|---|
| §2: posterior on the report event equals conditioning on content iff K(P\|·) is constant on P | Correct | Requires a regular prior, which the essay assumes. |
| §3: K_λ is factive; extensional ⇔ CAR; product-measure converse; uniform λ ⇒ K(P\|s) = 2^{−(\|S\|−1)} | Correct | The last agrees with M&Z's α_S = (2^d)^d (p. 344). |
| §3: strict propriety selects π(·\|P) iff the likelihood is constant on P | Correct | For positive-weight reports; this is M&Z's Lemmas 1–2. |
| Prop. 1 | Correct | The two-point projection gives Pr(i∈P) = θ. The {i,j}-vs-rest projection gives Pr(i∈P or j∈P) = θ. So Pr(i∈P, j∉P) = 0. The pair step needs \|S\| ≥ 3, as used. The converse holds, including one-point targets. The equivalence with fiber-averaged compatibility for all regular priors also holds. |
| §4: the uniform-subset kernel gives 1 − 2^{−m} vs 1/2 | Correct | |
| Prop. 2 | Correct | A_j, B_j and (3) check out. The bracket equals π(S∖P)/π(S∖{j}), which is > 0 for proper P by regularity and = 0 for P = S. The converse holds. |
| Prop. 2 "line segment" remark | Correct | Both endpoints are partition mechanisms, hence extreme points. |
| Ties among rules agreeing with BCOND on singletons and S | Correct | |
| Prop. 3 | Correct | The bracket is ≥ μ/(1−π(s)), which gives r_s ≤ ε(1−π(s))/μ. The uniform-prior case gives (n−1)ε. |
| §6: 3/4, 1/2, posterior 4/7 | Correct | Also reproduced via the bipartition decomposition in change 2 below. |
| §7: induced likelihood; fixed-prior criterion | Correct | |
| Prop. 4 | Correct | |
| Sufficiency of saturation | Correct | |
| Cross-pair example | Correct but degenerate | See Minor problems for an informative replacement. |
| "Negative companion" (only bijections and constant maps preserve CAR for all CAR kernels and all regular priors) | Correct | The witness partition {x′}, S∖{x′} works whenever ρ is non-injective and non-constant. |
| §8: K̄(T\|C) = 1 vs K̄(T\|A) = π(b)/π(A) < 1 | Correct | |
| §9: same coarse prior, different split within a fiber ⇒ different correct posteriors | Correct | |

**No stated result fails, so no counterexample is needed.** Qualifications the essay should state:
- Props. 2–4 depend on regularity.
- Props. 1 and 2 use different stability notions (fiberwise vs prior-averaged).

## Top five changes

1. **Retarget the essay at M&Z's own question of when a coarse model is adequate.**
   - Quote p. 309 (the noncontrastiveness slogan), pp. 310–312 (Litmus Test; nn. 19, 21, 22) and p. 337. The p. 337 material includes "cuts epistemology at its joints" and the non-Bayesian's point that "it also matters how likely it is for one to learn p at s."
   - Then make Prop. 4 the main theorem under its proper name. For a fine CAR kernel and a map ρ, the coarse prior space (T, π̄) is adequate iff g_Q is constant on fibers and the coarse kernel is CAR. "Adequate" here means: correct updating on the compressed report is globally evidentially constant at grain T for every regular prior within fibers.
   - This converts an attack on an unattributed extension into an exact answer to a question M&Z leave open (n. 19).

2. **Add, and verify, the CCAR decomposition of M&Z's unweighted benchmark.** These are my calculations; the author should check them and search for prior statements.
   - *The decomposition.* The uniform-subset kernel is exactly "draw R ⊆ S uniformly, independently of the state, and learn whether R." Hence it is CCAR.
   - *Consequence for Hi-TEA.* For globally evidentially constant rules, M&Z's Fact 9 quantity equals the sum of the rule's expected accuracies over the transparent problems given by the 2^{|S|−1} unordered partitions of S into at most two cells. So Fact 10 follows term by term from Greaves–Wallace (Fact 1).
   - *Check against M&Z's own numbers (Table 2).* The decomposition reproduces BCOND's −2.72 as −1.12 − 0.6 − 0.6 − 0.4, and the one-shot rule's −6.8 as −1.6 − 2.4 − 2.4 − 0.4.
   - *Robustness corollary (Jaeger's Theorem 4.17 in M&Z's terms).* A weighting stays extensional under every reweighting with the same support iff every learning situation in its support is transparent.
   - *Knife-edge example.* Take E1: a→ab, b→bc, c→ca and E2: a→ac, b→ab, c→bc, with equal weights. This weighting is extensional, supported only on opaque situations, and breaks under any reweighting.
   - *Payoff.* This lets the essay say something substantive about whether Hi-TEA's vindication is genuinely "externalist" (cf. M&Z p. 338). It would be a much stronger contribution than the transport classification.

3. **Repair the literature, stating the increment over each work.**
   - Halpern & Koller 2004: the increment is an exact classification for kernels and benchmarks, rather than an impossibility result for inference procedures.
   - Heitjan & Rubin 1991, and Gill, van der Laan & Robins 1997.
   - van Ommen et al. 2016: use it to answer the §9 identification problem, via minimax updating under the chosen proper score when the within-fiber prior is unknown.
   - Grünwald, "Safe Probability," for §10.
   - Schoenfield 2017, with the explicit mapping BCOND = naive conditioning and META-COND = sophisticated conditioning.

4. **Repair the transport premise (Major problem 1)** or recast Props. 1–2 as a conditional reductio of an explicitly attributed view. Also fix the §1 gloss "optimally against every problem", and make regularity explicit wherever it is used.

5. **Tighten.**
   - Fold Props. 1–3 into one theorem plus remarks.
   - Replace the degenerate cross-pair example with the informative one under Minor problems.
   - Present Prop. 4 as "strong lumpability + coarse CAR."
   - Cut §9 by about half.
