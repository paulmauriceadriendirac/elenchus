# Referee report — S1 Formal epistemologist (Bayesian foundations), refereeing to G3 literature-expert standards — P-9284

## Thesis and argument as I understand them (≤120 words)

A learner may condition on what a factive report says, ignoring how it was produced, only if the reporting mechanism is coarsening at random (CAR). The essay asks what survives when states are identified by a surjection and each report is replaced by its image. Prop 1: a prior-free family of random true reports that commutes with every surjection must report either the actual singleton (probability 1−θ) or the whole space (θ). Prop 2: under a regular prior, a CAR mechanism stays CAR under every one-vs-rest coarsening iff it has that all-or-nothing form. Prop 3 bounds partial reports when preservation is only approximate. A three-state example shows that a report which is tautological at the coarse level can still carry likelihood information. Moral: representation-neutral accuracy benchmarks (Meehan & Zhang's) must fix a level of description or restrict which transformations count.

## Verdict
Prize: not finalist
Journal recommendation: major revisions

## Scores
Clarity: 6 | Argument: 5 | Significance: 4 | Originality: 5 | Literature: 3 | Accuracy: 6 | OVERALL: 5

## The single most serious problem

§§1, 3 (final two paragraphs) and 7. The theorems only bite against a demand ("universal compatibility", or CAR surviving "every identification of states") that the essay never shows anyone holds. It also concedes that its real target is untouched: "This does not refute an accuracy argument formulated on a fixed state space"; "Nothing here shows that answer to be inconsistent."

Meehan & Zhang (hereafter M&Z) already relativize total expected accuracy (TEA) to a prior space:
- S is "a partition of the logical space whose cells settle every salient question in the given context" (p. 290).
- They decline to sum across state spaces, and warn that accuracy scores on different state spaces may not be comparable (pp. 328–29, nn. 33–34).

So the essay's conclusion, that "a benchmark that evaluates genuinely partial learning must specify a level of description", is one the target already accepts.

The argument that would make the paper matter is present in embryo but never stated:
- M&Z's defence of Hi-TEA against the weighting objection rests on *extensionality*. Fact 11 (p. 337) says BCOND maximizes weighted TEA iff the weighting is extensional.
- Extensionality is exactly CAR for the report kernel that the weighting induces (see Proof check).
- M&Z defend extensionality as "cut[ting] epistemology at its joints" (p. 337), and they read TEA as "an objective measure … for any agent" (n. 35).
- Prop 2 shows that extensionality at one grain carries over to coarser grains only in the all-or-nothing case. That is a genuine dilemma for the "objective" reading.

The essay never writes down the correspondence between weightings and kernels, never names Fact 11 or extensionality, and never notices that its "otherwise natural rule" (§3) and its §5 example *are* M&Z's unweighted benchmark. By M&Z's Fact 9, every p ∋ s is produced at s by the same number, (2^d)^d, of learning situations, so the induced kernel is uniform over the subsets containing s. As written, the only opponent the paper clearly identifies holds a position nobody holds.

## Major problems

1. **§§3 and 7: the target and the dialectic.** M&Z have two obvious replies, and the essay meets neither.
   - (a) There is a privileged grain: a state space fine enough to represent the agent's total evidence. This is their own move for Monty Hall (n. 21) and for the Litmus Test (nn. 19–20). On this reply, nobody claims that coarse-level BCOND is TEA-optimal against coarse-grained images of fine benchmarks.
   - (b) Each grain gets its own uniform benchmark, and verdicts are relative to the grain.

   The essay needs to show that (b) undercuts the "objective … for any agent" gloss (n. 35) and the "joints" claim. It also needs to show that (a) is unavailable, or costly, for the externalist M&Z address. Without this, the classification results have no dialectical target. Fix: Top five changes, items 1–2.

2. **§§3–4: the results are correct but elementary, and their strength is misjudged.**
   - Prop 1 uses only bijections of two-point sets and surjections onto two-point sets. Its content is: if every binary question is left open with the same probability θ, reports are all-or-nothing. That is immediate, because "the report contains i or j" includes "the report contains i"; equal probabilities force the two events to coincide almost surely.
   - Prop 2 is a three-line computation (eq. 3).

   That is acceptable in a philosophy paper, but the essay should:
   - state the minimal hypotheses;
   - give the geometric reading: in Gill & Grünwald's polytope of CAR mechanisms, the coarsening-stable mechanisms are exactly the edge joining the vertices for the discrete partition and the indiscrete partition;
   - compare with the closest results of the form "robustness forces a degenerate class": Grünwald & Halpern's Prop. 4.1 (CAR holds for all distributions iff the observations are pairwise disjoint) and Jaeger's theorem that robust coarsening procedures generate only CCAR ("coarsening completely at random") mechanisms.

   The essay's condition is strictly stronger than Jaeger's. Even a fixed partition fails to be coarsening-stable whenever ρ cuts across its cells; a fixed partition is a CCAR mechanism, and in M&Z's terms a transparent learning situation. This is the most interesting corollary on offer, and it is missing. Coarse-graining can turn a transparent (Greaves–Wallace) problem into a non-CAR problem that looks opaque (see Proof check). That links the essay to M&Z's Fact 12 and to the internalist "refine until transparent" reply (Stalnaker, Salow, Greco, all cited in M&Z n. 7).

3. **Literature.** A paper whose formal content sits squarely inside the CAR literature, and whose target is an accuracy-first argument, cannot rest on three citations. Missing (all verified to exist, details below):
   - the origin of CAR: Heitjan & Rubin 1991;
   - Gill, van der Laan & Robins 1997;
   - Jaeger 2005a and 2005b;
   - Grünwald & Halpern's own Prop. 4.1;
   - the missing-data commonplace that MAR (missing at random) is relative to the variables included. Omitting an auxiliary cause of missingness turns MAR into MNAR (cf. Collins, Schafer & Kam 2001). Marginalizing out an auxiliary variable is a coarsening ρ in the essay's sense, so the §5 phenomenon is a familiar special case;
   - van Ommen, Koolen, Feenstra & Grünwald 2016: updating on coarse data without CAR, under loss functions. This is the scoring-rule treatment of exactly the essay's problem;
   - Grünwald 2018: naive conditioning is "safe" only relative to a prediction task;
   - Easwaran & Nielsen 2025: with signals that do not form a partition, the expected-accuracy-optimal update is likelihood-weighted;
   - the externalist accuracy debate M&Z sit in: Greaves & Wallace 2006; Schoenfield 2017; Carr 2021; Gallow 2021; Isaacs & Russell 2023;
   - comparing accuracy across agendas: Carr 2015; Pettigrew 2018; Talbot 2019 (all in M&Z n. 33);
   - Levinstein 2019, which M&Z cite as a ground for rejecting extensionality.

   The closing remark that novelty "remains provisional" signals that this search was not done.

4. **§§5–6: credit for the "not a failure of Bayesianism" point.** Two things here are standard rather than new:
   - the tautology-with-a-likelihood observation;
   - its diagnosis: the license to ignore the mechanism depends on the representation, while Bayesian coherence in the full observation space does not.

   This is the naive-space versus sophisticated-space lesson of Grünwald & Halpern (§§1–3). M&Z make it too: n. 21 quotes Pearl 1988 that "we must also consider what information could have been reported", and the remedy they give is to fine-grain S. Present it as background and then go beyond it.

5. **§3 (final paragraphs) and §7 ("delimit a fourth … answer"): the step from theorems to "benchmarks" is informal.**
   - "Benchmark" is never defined.
   - M&Z's weightings may depend on (S, π) (p. 335), so Prop 1's prior-free hypothesis does not cover the weighted Hi-TEA family. Prop 2 covers only a single fixed fine-level mechanism.
   - What is needed is a theorem stated in M&Z's own terms (see Top five changes, item 1), plus the corollary the essay only gestures at. Under an all-or-nothing weighting, every globally evidentially constant rule that agrees with BCOND on singletons and on S ties for maximal TEA. Hi-TEA then no longer selects BCOND.

## Minor problems
- **Abstract.** "Sensitive to how both states and reports are represented." Only identifications of states, with reports carried along as images, are treated; reports are never re-represented independently.
- **§1.** "Compatibility across every refinement and coarsening": refinement is never treated.
- **§2, Grünwald & Halpern citation.** Their Theorem 3.1 states the conditions (a)–(d) under which conditioning in the naive space and in the sophisticated space coincide, i.e. CAR. The distinction itself is set up in their §§1–2. Rephrase "formulate the distinction".
- **§2, the translation ρ(P).** Justify it as the strongest coarse proposition that P entails. That makes the translation canonical and blocks a "wrong translation" objection.
- **Prop 1, indexing.** The family is indexed by all finite sets; say "up to isomorphism".
- **Prop 1, hypotheses.** State that two-point targets suffice.
- **Prop 1, motivation.** Note that compatibility at each fine state is equivalent to compatibility of prior-averaged mechanisms for every regular prior. That equivalence is the honest motivation for calling the family "prior-free".
- **Prop 1, a further cost.** θ is forced to be constant across all cardinalities; the essay does not mention this.
- **Prop 2.** Say why |S| ≥ 3 is needed: when |S| = 2 the claim is trivial.
- **Prop 3.** Only A_s − B_s ≤ ε is used, so "for every j" assumes more than needed.
- **§6.** Saturation is sufficient but not necessary: singleton-or-whole mechanisms survive non-saturating ρ. Give the exact condition for a given ρ.
- **§7.** "Unrestricted appeals to 'all learning problems'": M&Z quantify over all learning situations *for a fixed prior space*. Say so.
- **Length.** Delete "their status as previously unpublished results remains provisional". About 3,100 of the 6,000 words are unused.

## Prior work this resembles (only if confident; author, year, title, confidence %)
- **Grünwald & Halpern 2003, "Updating Probabilities", JAIR 19.** Thm 3.1: CAR is equivalent to naive conditioning agreeing with sophisticated conditioning. Prop. 4.1: "The CAR condition holds for all distributions Pr on ℛ if and only if O consists of pairwise disjoint subsets of W". This is the closest "universal demand forces trivial structure" result, and it is in the essay's own bibliography. 95%.
- **Jaeger 2005, "Ignorability in Statistical and Probabilistic Inference", JAIR 24: 889–917.** Robust coarsening procedures generate only CCAR mechanisms (Thm 4.17, as reported in Gill & Grünwald 2008; I could not open Jaeger's text). Existence 95%; theorem content 85%.
- **Jaeger 2005, "Ignorability for categorical data", Ann. Statist. 33(4): 1964–1981.** 95%.
- **Gill & Grünwald 2008 (cited by the essay).** The CAR polytope; its extreme points are uniform multicovers; "CAR mechanisms which are not CCAR will be very rare in practice". 95%.
- **Gill, van der Laan & Robins 1997, "Coarsening at random: characterizations, conjectures, counter-examples".** In Proc. First Seattle Symposium in Biostatistics (Lecture Notes in Statistics 123), 255–294. 95%.
- **Heitjan & Rubin 1991, "Ignorability and coarse data", Ann. Statist. 19(4): 2244–2253.** 95%.
- **Collins, Schafer & Kam 2001, "A comparison of inclusive and restrictive strategies in modern missing data procedures", Psychological Methods 6: 330–351.** Locus of the commonplace that MAR is relative to the variables included; the §5 phenomenon is a special case. 85% for the paper; the phenomenon itself is textbook.
- **van Ommen, Koolen, Feenstra & Grünwald 2016, "Robust probability updating", Int. J. Approx. Reasoning 74: 30–57.** 95%.
- **Grünwald 2018, "Safe probability", J. Stat. Planning & Inference 195: 47–63.** 90%.
- **Easwaran & Nielsen 2025, "Updating by Maximizing Expected Accuracy in Infinite, Non-Partitional Settings", J. Phil. Logic 54(5): 1095–1134.** 90% for the citation; content known only from Easwaran's public description.
- **McConway 1981, "Marginalization and linear opinion pools", JASA 76(374): 410–414.** The classic formal-epistemology precedent: requiring pooling to commute with marginalization (a coarsening) forces linear pools. 90%.
- **Meehan & Zhang 2025 itself (in the packet; 100%).**
  - Fact 11 with Lemmas 1–2 (pp. 337, 344–45) is the CAR characterization in accuracy dress; M&Z cite neither Heitjan–Rubin nor Grünwald–Halpern.
  - Fact 12: a weighting concentrated on a single learning situation is extensional iff that situation is transparent.
  - nn. 19–21 and 33–35 anticipate the model-choice issue.

I found no prior statement of Prop 1 or Prop 2.

**Increment I credit:** two correct classification results that appear to be unpublished but are elementary, plus a latent, unstated argument against the objectivity of M&Z's extensionality-based vindication of BCOND.

## Claims that look false, misattributed or unverifiable
- **"Grünwald and Halpern (2003, Theorem 3.1) formulate the distinction…"** Imprecise: Thm 3.1 characterizes when the two kinds of conditioning *coincide*.
- **"Their results connect Bayesian optimality to the balance of report likelihoods across compatible states."** A fair gloss of Fact 11 and Lemma 2, but M&Z's λ are importance weights, not likelihoods. Identifying them with likelihoods is the essay's own (correct) step and should be argued, not presupposed. M&Z's imagined non-Bayesian does say "it also matters how likely it is for one to learn p at s" (p. 337).
- **§§1 and 7.** The suggestion that M&Z-type arguments range over "an unrestricted collection of possible learning problems" is misleading: M&Z deliberately relativize the collection to one prior space (pp. 328–29).
- **"Demand compatibility across every refinement and coarsening."** Attributed to no one, and unverifiable as a view anyone holds.
- **Bibliography: all three entries check out.**
  - M&Z: Phil. Review 134(3): 285–350, DOI 10.1215/00318108-11873775; confirmed from the source PDF.
  - Gill & Grünwald: Annals 36(5): 2409–2422, DOI 10.1214/07-AOS532, arXiv 0811.0683 (an earlier preprint is math/0510276).
  - Grünwald & Halpern: JAIR 19, DOI 10.1613/jair.1164, arXiv cs/0306124. The JAIR landing page does not display pages 243–278; I believe they are correct (~85%).

## What is genuinely good (be specific: revisions must preserve this)
- All of the mathematics checks out (see Proof check). Hypotheses are mostly explicit. The reduction to one-vs-rest coarsenings ("the partitions separating one state from all the others already suffice") is a nice economy.
- **Calibration.**
  - §5 refuses to call this a failure of Bayesian probability.
  - It separates Bayesian coherence in the full observation space from the "license to ignore the mechanism".
  - Prop 3 honestly notes that a small imbalance does not bound partial reports when prior atoms can be tiny.
- **§6's saturated-merge repair** is a principled restricted neutrality: invariance under merges that respect the report algebra.
- **The core insight has real force against a Philosopher's Annual 2025 paper:** invariance of ignorability (equivalently, of M&Z's extensionality) across grains is available only in the all-or-nothing case. Keep it and put it at the centre.

## Literature check

**Searches run** (WebSearch/WebFetch, Oct 2026):

1. **CAR under coarsening, merging categories, marginalization or collapsing categories** (several phrasings, including "not preserved" and "not closed").
   - Found: Heitjan & Rubin 1991; Gill, van der Laan & Robins 1997; Jacobsen & Keiding 1995 (CAR in general sample spaces, Ann. Statist. 23(3)); Gill & Grünwald 2008; Jaeger 2005a,b; Heitjan 1993 (Biometrics, biomedical examples); Cator's work on testing the CAR assumption (arXiv math/0503737).
   - None states either classification. In what I could read, none treats CAR when states are identified and reports are carried along as images.
2. **Grünwald & Halpern 2003.** Checked the arXiv abstract, the JAIR landing page, and the full text via the ar5iv HTML rendering.
   - Confirmed: Thm 3.1 gives four equivalent conditions; (a) is naive conditioning = sophisticated conditioning; "CAR" is defined as (a) holding for all U ∈ O.
   - Also confirmed: Prop. 4.1 (quoted above), Example 3.3, Thm 4.4, and §4.4's "sometimes CAR is nothing".
   - No discussion of CAR under coarsening of the naive space in the extracted text; I did not read every line of the second half.
3. **Gill & Grünwald 2008.** Checked arXiv metadata (0811.0683 and math/0510276) and the ar5iv HTML of math/0510276.
   - Confirmed: Thms 1–3 (every CAR mechanism is a mixture of extreme ones; rational approximation; Fibonacci heights); their report of Jaeger's Thm 4.17; "the extra generality obtained by relaxing CCAR to CAR is illusory".
   - No discussion of merging outcomes. The essay's description ("geometry and procedural generation") is accurate.
4. **Jaeger 2005a,b.** Abstracts and metadata confirmed (JAIR 24: 889–917, DOI 10.1613/jair.1657; Ann. Statist. 33(4): 1964–1981). Full texts not reachable: the PDFs would not decode and the author's site returned 503. Thm 4.17's content is known only at second hand.
5. **MAR and marginalization.** No direct theorem found. Collins, Schafer & Kam 2001 confirmed through secondary sources as the locus of the inclusive-strategy (auxiliary-variable) point.
6. **Replies to M&Z.**
   - None found in indexed sources. M&Z's selection for the Philosopher's Annual 2025 is confirmed (Daily Nous, 30 Aug 2026).
   - Richard Pettigrew's Substack post of 20 Dec 2025, "Bayesianism when learning isn't straightforward", recommends a paper that is almost certainly M&Z (his reply refers to "Alex and Snow's result").
   - In the comments, Kenny Easwaran describes his J. Phil. Logic paper with Nielsen: the optimal map from signals to updates shifts each world's probability "in proportion to the likelihood of the received signal in that world".
   - He also suggests that M&Z's picture is recovered if each signal is a true proposition chosen uniformly at random from those true at the actual world. That is the essay's "otherwise natural rule".
   - This is a public blog-comment statement of the essay's framing of M&Z, not of its theorems.
7. **Easwaran & Nielsen 2025.** Citation confirmed on Easwaran's site; the PDF would not decode, so content is known only from the comment above.
8. **Category-theoretic form of Prop 1** (natural transformations from the identity to distributions over nonempty subsets, on finite sets with surjections). Nothing found.
9. **McConway 1981; van Ommen et al. 2016; Grünwald 2018.** Bibliographic details confirmed. In Grünwald 2018 (ar5iv), safety is relative to the target random variables and is preserved when the *target* is coarsened, not the observation. Related, but distinct.
10. **Yablo, "Fine-Grained Evidence"** (Synthese, forthcoming; PhilSci-Archive, Jan 2026). A different, truthmaker sense of "grain"; peripheral.

**Attributions and quotations.**
- The essay quotes no one directly.
- M&Z characterization: checked against the packet source; accurate in gist but imprecise (see above).
- Grünwald & Halpern Thm 3.1: checked (ar5iv); loosely described.
- Gill & Grünwald 2008: checked; accurately described.
- Bibliographic data: checked as listed above.

**Not reached:** full texts of Jaeger 2005a,b, Gill, van der Laan & Robins 1997, Heitjan 1993/1994, Cator, and Easwaran & Nielsen; parts of Grünwald & Halpern beyond the extraction summary. I did not open the cached PDFs that the fetch tool saved outside the packet.

**Verdict on originality.**
- Moderate confidence (~70%) that neither classification is stated in this form in the CAR literature.
- High confidence that the qualitative phenomenon (ignorability is not invariant when the state space is coarsened) is known.
- High confidence that analogous "robustness forces a degenerate class" results exist (Grünwald & Halpern Prop. 4.1; Jaeger Thm 4.17).
- ~75% that no published critique of M&Z makes the essay's point as of Oct 2026; replies may be in press.

## Proof check

**Prop 1: valid.**
- Two-point step: invariance under bijections gives one θ for all two-point spaces and both actual states. ✓
- One-vs-rest step: the coarse report is whole iff i ∈ P. ✓
- Pair step: it needs the actual state s to fill the other category; for |S| = 3 that category is {s}. ✓
- Since Pr(i ∈ P) = Pr(j ∈ P) = Pr(i ∈ P or j ∈ P) = θ, the two indicators are almost surely equal. ✓ Hence P ∈ {{s}, S} almost surely, with Pr(P = S) = θ. ✓
- Converse, including |T| = 1. ✓
- Only bijections of two-point sets and surjections onto two-point sets are used.
- θ is forced to be equal across all cardinalities.
- Requiring compatibility at each fine state is equivalent to requiring compatibility of prior-averaged mechanisms for every regular prior (if every interior mixture of the fine distributions equals R, each one equals R). This is the honest motivation for "prior-free".

**Prop 2: valid.**
- A_j, B_j and (3) verified. The bracket equals π(S∖P)/π(S∖{j}): it is ≥ 0, and = 0 iff P = S. Regularity is needed for strictness. ✓
- The row-sum step ✓. The converse ✓: at each fine state the coarse report is {ρ(s)} with probability 1−θ and T with probability θ, so averaging within a fibre does no harm.
- Implicit modelling choice: the coarse mechanism at a merged category is the π-average of the fine kernels. That is the correct likelihood for a coarse-level Bayesian; say so.

**Prop 3: valid.**
- The uniform-prior bound (n−1)ε ✓.
- The tiny-atom remark ✓. Example: S = {a, b, c}, deterministic partition {ab | c}, π(c) = δ. Then A_a − B_a = δ/(π(b)+δ), A_b − B_b = δ/(π(a)+δ), and A_c − B_c = 0. So ε → 0 while r_a = r_b = 1.

**§3, the uniform rule:** 1 − 2^(−m) versus 1/2. ✓

**§5 example:**
- c_P = 1/4 for every nonempty P ✓.
- Pr(whole | C) = 3/4 and Pr(whole | A) = 1/2 ✓.
- Pr(A | whole) = 4/7 ✓.
- Agrees with (3): A_c − B_c = 3/4 − 1/2 = 1/4.

**§6 saturation:** correct and sufficient, but not necessary (the singleton-or-whole mechanism with nontrivial fibres is a counterexample to necessity).

**Missing fact the essay should add (verified): partitional, i.e. transparent, mechanisms are not coarsening-stable.**
- Take the partition {a | bc} and merge a and b into A. Then Pr(whole | A) = π(b)/(π(a)+π(b)) < 1 = Pr(whole | C).
- At the coarse level, an agent at A receives {A} or {A, C}, and an agent at C receives {A, C}. This is a mixture of an opaque learning situation and a trivial one.
- So both CAR-failure and apparent opacity depend on the grain of description.

**Correspondence between weightings and kernels (needed, absent from the essay, verified):**
- For any M&Z weighting λ on learning situations over (S, π), Σ_{p∋s} λ_p(s) = Σ_E λ(E) =: Λ, independent of s.
- So K(p | s) = λ_p(s)/Λ is a factive kernel, and λ is extensional ⇔ K is CAR.
- Conversely, every factive kernel arises this way, e.g. from λ(E) = Π_s K(E(s) | s).
- M&Z's unweighted λ gives K(p | s) = 2^(−d).
- Hence Fact 11 is strict propriety plus Grünwald & Halpern Thm 3.1.
- Prop 2 then transfers word for word: the coarse-grained image of λ is extensional under every one-vs-rest coarsening iff λ_p ≡ 0 for every proper nonsingleton p.
- Corollary: under such a λ, every globally evidentially constant rule that agrees with BCOND on singletons and on S maximizes weighted TEA, so Hi-TEA does not select BCOND.

**Gap:** the step from the theorems to claims about "benchmarks" is never made formally (Major problem 5).

## Top five changes

The extra roughly 3,100 words should buy items 1–3.

1. **Recast the paper as a theorem-backed objection to M&Z's extensionality defence (~1,200 words).**
   - Write down the correspondence between weightings and kernels.
   - Show that Fact 11 is the CAR characterization, crediting Grünwald–Halpern and Heitjan–Rubin; M&Z cite neither.
   - Show that M&Z's unweighted benchmark is the uniform-subset kernel (Fact 9), and that §5 is that benchmark on three states.
   - Prove the version of Prop 2 for coarse-grained images of λ, and the corollary that Hi-TEA then fails to select BCOND.
   - Then pose the trilemma:
     - (i) each grain gets its own uniform benchmark. These are incoherent across grains (Prop 1), which contradicts the "objective … for any agent" gloss (n. 35) and the "joints" claim (p. 337).
     - (ii) coarse benchmarks are images of the fine one. Then coarse-level BCOND is not Hi-TEA-optimal.
     - (iii) all-or-nothing weights. Then Hi-TEA does not select BCOND.

2. **Answer M&Z's best reply (~700 words).** The reply: there is a privileged grain, fine enough to represent the agent's total evidence (their n. 21 on Monty Hall; the Litmus Test, nn. 19–20).
   - Use the partition example to show that coarse-graining turns transparent problems into problems that look opaque, and that refining the state space restores transparency.
   - So for the externalist M&Z address, the privileged-grain reply threatens to dissolve the very opacity that motivates their project (cf. the Stalnaker/Salow/Greco line they cite in n. 7).
   - Whether this is a cost to M&Z is the paper's real philosophical question; settle it.

3. **Literature and positioning (~600 words).**
   - Add the CAR lineage: Heitjan & Rubin 1991; Gill, van der Laan & Robins 1997; Jaeger 2005a,b; Grünwald & Halpern Prop. 4.1.
   - Add Jaeger's robustness-forces-CCAR precedent, noting that coarsening-stability is strictly stronger than CCAR.
   - Add the commonplace about MAR and auxiliary variables.
   - Add loss-based updating on coarse data (van Ommen et al. 2016; Grünwald 2018) and Easwaran & Nielsen 2025.
   - Add the externalist accuracy debate; cross-agenda accuracy comparison (Carr 2015; Pettigrew 2018; Talbot 2019); Levinstein 2019.
   - Cite McConway 1981 as the precedent for this kind of result.
   - State the increment in one sentence, and delete "remains provisional".

4. **Right-size and sharpen the mathematics (~400 words).**
   - State the minimal hypotheses: two-point targets suffice; one-vs-rest coarsenings suffice.
   - Give the geometric statement: the edge of the Gill–Grünwald CAR polytope between the discrete-partition and indiscrete-partition vertices.
   - Give the exact condition for CAR to survive a given ρ; saturation is only sufficient.
   - Add the equivalence (each fine state ⇔ every prior) that motivates Prop 1.
   - Either treat refinements or drop them from §1.

5. **Tighten the framing (~300 words).**
   - Define "benchmark".
   - Replace "unrestricted collection of learning problems" with M&Z's actual quantifier (all learning situations for a fixed prior space).
   - Fix the gloss on Grünwald & Halpern's Thm 3.1.
   - Justify ρ(P) as the strongest coarse proposition that P entails.
   - Present the "tautology with a likelihood" as the standard naive/sophisticated-space point (credit Grünwald & Halpern §§1–3 and M&Z n. 21), and move quickly to what is new.
