# Referee report — S2 Epistemic logician / knowledge-first epistemologist (with G3 literature-expert standards) — P-7f1b

## Thesis and argument as I understand them (≤120 words)

Knowledge-based decision theory (KDT: expected utility conditional on what one knows) violates Good's theorem in Goodman–Salow normality models. An expected-utility version of Salow's Conditional Knowledge Dominance does not repair this. In finite statist, comparable K-normality models, a free question has non-negative KDT value for every decision problem iff no state left open by one's knowledge is one where answering reopens an excluded possibility. This follows from Lemma 1 plus Geanakoplos's nestedness theorem. Given certain "p_v" questions, every question is safe iff knowledge is "gapped", so in graded models only the evidence can safely be conditioned on. In the Gaussian Bjorn model a free second weighing has KDT value −0.05 at 10:1. A perturbation makes the conditional rule (CEU) coincide with KDT.

## Verdict
Prize: not finalist
Journal recommendation: major revisions

## Scores
Clarity: 6 | Argument: 5 | Significance: 4 | Originality: 4 | Literature: 6 | Accuracy: 7 | OVERALL: 5

## The single most serious problem

**Location:** §5.2 (Theorem 3), as advertised in the abstract and §1 and defended in §6.2.

**No fatal technical error.** Every theorem I checked is valid (see Proof check). The fatal problem is dialectical.

**What remains once the known parts are set aside.** Lemma 1 is the dogmatist's bet. Lemma 2 is Geanakoplos's theorem. The qualitative point "for all you know you will lose knowledge, even given Preservation" is Salow's own Weak Knowledge Dominance\* (2025, 33). Hong (2026) already concludes that normality-theoretic knowledge is not action-guiding. The one result that would be news is "the conditional repair fails". Theorem 3 does not show it, for three reasons.

**(a) CEU is the essay's construction, not Salow's, and it says more than CKD.** CEU agrees with CKD wherever CKD gives a verdict, but CEU also gives verdicts where CKD is silent. Theorem 3's perturbation always lands in that silence:
- Let m\* be a ⪰-maximal state of E. Then m\* ∈ B(E) ⊆ K_E(x).
- m\* never witnesses defeat. If some v ∉ K were undominated in m\*'s cell, chaining would give m\* ≫ v, a contradiction.
- By transitivity, m\*'s post-answer ken excludes s0. So at m\*, looking leads to β, which pays ε more than β1.
- Hence the agent does not know that β1 beats looking, and CKD makes no dogmatic recommendation.

The dogmatic verdict comes from KDT's probability-1 weighting, once "the options differ" has been made trivially true.

**(b) The essay quotes the right hypothesis and conditions on the wrong one.** Salow's anti-dogmatic thought is "if the evidence you would discover tells strongly against your view, there is a good chance you're wrong" (2025, 36). Conditioning on that hypothesis means conditioning on what looking would lead one to do: value looking against a\* by Σ_b Pr(look→b | K)·E[u_b − u_a\* | K^{[look→b]}]. In every instance of Theorem 3's construction (L large), this rule prefers looking:
- On [look→β], looking gains ε.
- On [look→decline], the conditional ken always contains a state outside K, where β1 pays −L−ε. To see this, take a ⪰-maximal w in the decline set. Either w ∉ K, or w is a defeat witness whose reopened v is undominated in the decline set.

In Bjorn, this rule is exactly the essay's own −0.63 computation.

**(c) The refuted rule is worse than KDT by the essay's own lights.** The essay concedes that CEU is sometimes unsafe where KDT is safe (§5.2, last paragraph). Refuting such a rule says little about "the conditional repair".

**Why it matters.** Without Theorem 3, the contribution shrinks to a correct but modest characterization (gappedness and the graded collapse) plus a well-computed example. That is a specialist note, not a prize essay. The abstract's "An expected-utility form of Salow's Conditional Knowledge Dominance does not help" is not established.

## Major problems

**1. §5.2, Theorem 3.**
- Problem: as above. CEU says more than CKD, and in Theorem 3's construction CKD is silent and the verdict-change rule prefers looking.
- Why it matters: the essay's distinctive claim against Salow is unsupported.
- Fix: either (i) analyse the verdict-change rule and give its safety boundary, or (ii) demote Theorem 3 to a remark ("the payoff-difference translation coincides with KDT on tie-free problems"). Under (i), if the verdict-change rule also fails at some non-gapped kens, that is the new result the essay advertises. Under (ii), drop "the conditional repair fails" from the abstract, §1 and §7.

**2. §3 (last paragraph), §4 (graded paragraph, Corollary ii), A.5: scope slippage between the finite theorems and the continuous Bjorn model, with false glosses.**
- (a) "At any situation after the first weighing there is a state compatible with Bjorn's knowledge in which the second reading would reopen a weight he now rules out" is false.
  - With R = max(c², δ(x)), the post-answer kens project onto weights within r ± (√(R/2) + c/√2).
  - For |μ_s| ≥ c/√2, Cauchy–Schwarz caps the projection at r ± √R.
  - So a new weight is reopened only if R < (1+√2)²c² ≈ 5.83c².
  - A.5 proves that states (weight–second-reading pairs) are reopened. At sufficiently abnormal situations the harmful bet is therefore a bet on δ ≤ R, a proposition partly about the very reading one is deciding whether to see.
- (b) "Bjorn shows that the questions needed for (ii) can be as natural as a second reading" is false. Corollary (ii) needs the p_v questions ("is the total squared error at least k?") and is proved for finite S only. The second weighing is not a p_v question.
- Why it matters: "failures of Good arise at every situation with inductive knowledge" in the leading model is the essay's main claim to significance. As stated it is partly false and partly about exotic bets.
- Fix: state three separate claims:
  - normal situations: weight bets at 10:1 (keep this);
  - every situation: some joint weight-and-reading bet (A.5);
  - δ(x) ≥ 5.83c²: no weight-only bet of Lemma-1 form.

**3. §§2–3: optional inquiry is not modelled.**
- What Bjorn knows after one weighing depends on the second scale's reading (G&S 2023, 128). Their n. 40 says the model gives knowledge "about the scales' future readings". Once the second weighing is optional, the essay must say what y2 is in states where Bjorn declines to look.
- BRN (App. A, NESTEDNESS) require states to settle one's evidential trajectory, and call models that ignore this "unrealistic" (n. 46). On their Babysitter fix, states encode whether one looks. Then K_E(x), and so KDT's conditioning set, depends on the act being evaluated. That is act–state dependence, a separate and familiar route to Good failures, and the essay must separate it from its own mechanism.
- Theorem 1(b) assumes that the p_v questions are available. With more than one available, E∩p_v and E∖p_v′ overlap without either containing the other, which NESTEDNESS forbids.
- G&S (2023, n. 47) say the Bjorn model obeys statism only "with respect to the possible bodies of evidence we considered". Adding p_v bodies of evidence will, under the probabilistic grounding the essay uses, generally break statism. §6.4 rescues Lemma 4 only.
- Fix: add one paragraph. Either fix y2 as the reading the scale would give and defend normality over counterfactual errors, or show that the Bjorn result survives states that encode the trajectory. Restrict Theorem 1(b) to one question at a time.

**4. §1, §4, §6.2: the general value-of-evidence literature is missing.**
- This literature already characterizes when conditioning agents value free evidence: reflection-type conditions (Skyrms 1990; Huttegger 2014), Total Trust ⇔ Value (Dorst, Levinstein, Salow, Husic & Fitelson 2021), and Dorst 2020. Geanakoplos is cited only second-hand via Das.
- Relative defeat is a failure of the knowledge-conditioned credence to trust its successors. Theorem 1(a) is the nested special case.
- Why it matters: originality is judged against this literature, and Salow, the essay's main interlocutor, co-wrote the Total Trust paper.
- Fix: state the increment as (i) the normality-theoretic identification of the trust condition (gappedness), (ii) the graded collapse, and (iii) the 10:1 Bjorn datum.

**5. §3, §6.4: question-sensitivity.**
- On the probabilistic grounding the essay uses for Bjorn (G&S 2023 §5; Goodman & Salow 2021), normality is relative to a contextually salient question.
- G&S (n. 40) note that the question "how much does Bjorn weigh" yields Goldstein & Hawthorne's (2022) model, where current knowledge does not depend on future readings. A weight bet plausibly makes that question salient.
- Fix: show the 10:1 verdict survives in that model. It probably does, since G&S say that model predicts NO DEFEAT failures even under Margins. But the A.5 joint-proposition bets may not be expressible there.

**6. §1, §6.2: overlap with Hong (2026) is not quantified.**
- By the essay's own account, Hong already uses "the value of otherwise irrelevant information" against normality-based action guidance.
- The only abstract I could reach says Hong concludes that "whatever concept the normality framework is capturing is not action-guiding".
- Fix: quote what Hong shows about information value and state exactly what the boundary adds. Otherwise readers will credit the central qualitative claim to Hong.

## Minor problems

- Abstract: "non-negative value" lacks "for every decision problem". Seven claims in roughly 150 words bury the thesis.
- §1 calls Good's theorem "the practical content of Salow's dissolution". Salow says his response "by itself doesn't predict that openness to further evidence is always required", though "a natural development of it will" (2025, 35). The target should be that anticipated development, not the dissolution itself.
- CEU is a pairwise relation, with a different conditioning hypothesis for each pair. The essay never says how it chooses among more than two options, or whether it can cycle.
- Theorem 3's hypothesis that "conditional knowledge on the trivial hypothesis E is ordinary knowledge" holds automatically under the essay's definition of K^D. It is not an assumption.
- A.6 picks L before ε, but whether β1 is declined after the answer depends on ε. This is harmless if L is chosen to work for all ε ≤ 1.
- The θ-threshold reply in §5.2 has a simpler answer: EU choices are invariant under scaling utilities, and threshold rules are not.
- §5.2's perturbed Bjorn claim ("CEU then prefers betting now by 0.05"): with L fixed at 10, β1 can be accepted after answers just past the decline threshold, so D = E fails exactly. Show the computation or drop the figure.
- §6.4 says "non-statist models only add failures, as §5.3 shows". One example cannot show "only".
- §6.1's empty-question example (+0.5 with no new evidence) is correct. But it shows that V_x compares a state-dependent policy with a fixed act, not information alone, and that bears on how "harm" at abnormal situations should be read. Say so or cut it.
- §4's enumeration (64,004; 3,306; 240,000) comes with no code or data, and the lemmas are proved anyway. Cut it or deposit the code.
- Harman, Kripke, Williamson's unmarked clock and Oddie are invoked but absent from the references. So are Fantl & McGrath 2002 and Weatherson 2005, who developed the encroachment view of §6.5 according to Salow 2025 n. 3.
- §3's 0.37 "Preservation-violating" probability is BRN's figure for weight beliefs. BRN's own state-space belief sets (n. 17) are B(E_y) = {δ ≤ c²} and B(E_{y,z}) = {δ ≤ (y−z)²/2 + c²}. On these, Preservation fails at every 0 < |y−z| ≤ √2c, which has probability ≈ 0.95 under the essay's Gaussian. The essay's machinery is in state space, so it must say what subject matter "Preservation" and "knowledge" range over. This strengthens the ubiquity point, but the gloss is inconsistent with the formalism.
- "Question" is defined as a partition into "discoverable" cells, but "discoverable" is never defined (presumably E ∩ cell ∈ ℰ).

## Prior work this resembles (only if confident; author, year, title, confidence %)

| Work | Relevance | Confidence | Cited? |
|---|---|---|---|
| Salow, B. 2025. "Fallibility and Dogmatism." *AJP* 103: 23–38 | Weak Knowledge Dominance\* "can support dogmatism even given Preservation" (p. 33) is the qualitative form of the essay's three-state point | 100% (read) | Yes |
| Hong, F. 2026. "Normality in Action?" *Philosophical Perspectives*, doi 10.1111/phpe.70003 | Concludes that normality knowledge is not action-guiding | 85%; DOI resolves to Wiley, contents not reached | Yes |
| Geanakoplos, J. 1989. "Game Theory without Partitions, and Applications to Speculation and Consensus." Cowles Foundation DP 914 | Nestedness suffices for the value of information | 85% | Via Das only |
| Dorst, K., Levinstein, B., Salow, B., Husic, B. & Fitelson, B. 2021. "Deference Done Better." *Philosophical Perspectives* 35 | Total Trust ⇔ Value | existence 90%, content 70% | No |
| Dorst, K. 2020. "Evidence: A Guide for the Uncertain." *PPR* 100: 586–632 | Value-of-evidence content | existence confirmed (BRN reference list); content 70% | No |
| Skyrms, B. 1990. "The Value of Knowledge." *Minnesota Studies in the Philosophy of Science* 14 | Reflection-type conditions for the value of learning | 75% | No |
| Huttegger, S. 2014. "Learning Experiences and the Value of Knowledge." *Philosophical Studies* 171 | Same | 70% | No |
| Salow, B. 2018. "The Externalist's Guide to Fishing for Compliments." *Mind* 127: 691–728 | KK failure and biased inquiry (§6.1) | confirmed (Salow 2025 reference list) | No |
| Goldstein, S. & Hawthorne, J. 2022. "Knowledge from Multiple Experiences." *Phil Studies* 179: 1341–72 | Rival normality model of repeated weighing | confirmed (G&S 2023 reference list) | No |
| Goodman, J. & Salow, B. 2021. "Knowledge from Probability." TARK 2021: 171–86 | Question-relative probabilistic normality | confirmed (G&S 2023 reference list) | No |
| Lasonen-Aarnio, M. 2014. "The Dogmatism Puzzle." *AJP* 92: 417–32 | Dogmatism puzzle | confirmed (Salow 2025 reference list) | No |

## Claims that look false, misattributed or unverifiable

**False or overstated**
- §3: "reopen a weight he now rules out" at "any situation". False for δ(x) ≥ (1+√2)²c²; see Proof check.
- §4: "Bjorn shows that the questions needed for (ii) can be as natural as a second reading". False: the second weighing is not a p_v question.
- Abstract and §1: "An expected-utility form of Salow's Conditional Knowledge Dominance does not help … It fails wherever the unconditional rule fails". This is shown only for the payoff-difference form, under statism, comparability and K-normality. CKD itself is silent in the constructed problems.
- §6.4: "non-statist models only add failures, as §5.3 shows". One example cannot establish this.

**Misframed**
- §1: Good's theorem as "the practical content of Salow's dissolution" (see Minor problems).
- §1: "Salow describes such failures as 'relatively rare' (2025, 36)". The quote is verbatim, but Salow says it while objecting to encroachment. The 0.37 figure set against it is the weight-belief estimate from BRN, which Salow co-wrote.
- §6.5 credits the encroachment view only to Hawthorne's suggestion. Salow's n. 3 credits its development to Fantl & McGrath (2002) and Weatherson (2005).

**Unverifiable by me**
- The contents of Hong 2026 §§1–3 ("lottery switching, sweeteners and the value of otherwise irrelevant information").
- Ahmed & Salow 2019's view as paraphrased in §6.6, and the claim that their counterexamples are all non-partitional.
- "This kin of Williamson's unmarked clock is discussed by Ahmed and Salow (2019) and Das (2023)."
- That Goldschmidt 2024 "describes this conditionalizing form" and "surveys" stakes-sensitive variants.
- Whether "Ex Ante Dogmatism" is Carter & Hawthorne's own label. The search snippet attributes the label to a later critique.
- The enumeration counts.
- The 0.05 CEU margin in the perturbed Bjorn problem.

## What is genuinely good (be specific: revisions must preserve this)

1. **Theorem 1 is correct and exactly stated.** Its quantifiers are mostly handled with care: the "existential claim over questions" caveat in §4, the caveat in §6.5 that the guarantee quantifies over decision problems, and the conclusion's refusal to claim an exhaustive trilemma.
2. **The 10:1 Bjorn computation is the best philosophical datum in the essay.** The fallibilist also takes the bet (EV 0.45), which blocks the reply that the result is an artefact of high stakes. I reproduced the decline threshold ≈ 1.12c and the values −0.05, −0.12, −0.27 and 0.37.
3. **The three-state example cleanly separates the KDT safety boundary from Preservation.** Preservation holds there for every body of evidence, yet a question is unsafe at b. This gives Salow's WKD\* worry an exact expected-utility location.
4. **Theorem 2's completion-independence is the right generalization.** It covers any M ⊇ B, including JTB and iterated knowledge, and so blocks cheap escapes.
5. **A.5 is a correct and needed positive-measure repair** of the finite proof for the continuous model.
6. **§5.3 exposes a real choice point**: conditional versus post-discovery belief (BRN App. D.3), with an exact, verified example (−0.53; {s1} versus {s1, s5}).
7. **§6.1's dilemma ties the result to the KK debate.** On K-normality, KDT avoids evidence; on the Margins completions, it avoids deferring to itself.
8. **Every quotation I checked is verbatim** (10 of 10).

## Literature check

**Searches and fetches (12 web calls, the limit)**

| # | Call | Result |
|---|---|---|
| 1 | WebSearch: Hong "Normality in Action?" | No hit |
| 2 | WebSearch: Salow "Fallibility and Dogmatism" | AJP 103(1): 23–38 (2025), DOI 10.1080/00048402.2024.2381692 |
| 3 | WebFetch: ORA PDF of Salow 2025 | Full text read (pp. 23–38) |
| 4 | WebFetch: doi.org/10.1111/phpe.70003 | 302 redirect to Wiley; the DOI is a *Philosophical Perspectives* DOI |
| 5 | WebFetch: Wiley page | 403 |
| 6 | WebSearch: Hong on PhilArchive | Other Hong papers ("Prefaces, Knowledge, and Questions"; "Fanaticism and Knowledge", 2025); not this one |
| 7 | WebSearch: BRN | *J Phil Logic* 54: 1–49 (2025), DOI 10.1007/s10992-024-09769-0, open access |
| 8 | WebFetch: BRN preprint (Salow's Oxford page) | Read pp. 1–20 and 36–52 |
| 9 | WebSearch (extended): "Normality in Action" | ResearchGate snippet: Frank Hong, "Normality in Action?", dated Sept 2026. Asks whether knowledge on the normality framework guides action, considers fanatical prospects, and concludes that "whatever concept the normality framework is capturing is not action-guiding". Venue and contents not otherwise reached. |
| 10 | WebSearch: Carter & Hawthorne | *Mind* 133(531): 651–676 (2024), DOI 10.1093/mind/fzad070. Also surfaced: Brown 2025, "Knowledge, inquiry and dogmatism", *Synthese* (a reply) |
| 11 | WebSearch: Goldschmidt | *AJP* 102(4): 939–958 (2024); proves a representation theorem for Hawthorne & Stanley's (2008) theory |
| 12 | WebSearch (extended): prior statements that KDT violates Good's theorem or refuses free evidence | None found. Background only: "Only CDT values knowledge" (*Analysis* 84(1), 2024) and "Do we really need a knowledge-based decision theory?" (PMC7983079); authors not checked |

**Do the named works already contain the essay's results?**
- **Salow 2025.** Contains the qualitative core: the "for all you know" variant (WKD\*, p. 33), and the flag that graded choice is "a general problem" (p. 34). It has no expected-utility treatment and no boundary theorem, and Good's theorem appears only in n. 2. The boundary and the Bjorn numbers are not there.
- **BRN.** No decision theory. It contains:
  - Prop. 1 (statism + collapse + comparability ⟹ ◊−); the essay's Corollary (i) is its straightforward EU counterpart;
  - the Bjorn ◊− failure and the ~.37 estimate (§5, n. 18);
  - App. D.3 on conditional belief;
  - Prop. 5;
  - NESTEDNESS (App. A), which bears on Major problem 3.
- **Hong 2026.** Contents not reached. The abstract's conclusion is broader than the essay's thesis. Whether it contains a Good's-theorem result is undetermined; the essay's own description suggests partial overlap.
- **Das 2023 and Ahmed & Salow 2019.** Not reached; I rely on general knowledge. Das brings Geanakoplos's nestedness into epistemology, as the essay says (~75%). Neither concerns normality models.
- **Carter & Hawthorne 2024.** About the aim of inquiry, not expected utility. No overlap with the theorems.

**Attributions and quotations confirmed** (against Salow 2025 and the BRN preprint, both read, and G&S 2023 in the packet)
- Salow 2025:
  - p. 33: CKD statement (verbatim) ✓
  - p. 34: "a general problem" ✓; "Any solution to that problem will generalize to this one" ✓ (Salow's problem concerns all-out beliefs)
  - p. 36: "relatively rare" ✓ (context: encroachment)
  - p. 33: "can support dogmatism even given Preservation" ✓ (said of WKD\*)
  - p. 33: "entitled to believe q on the hypothesis that p only if discovering p would not require you to stop believing q" ✓
  - p. 23 (abstract): "decisions should be governed by underlying probabilities rather than our knowledge" ✓
  - p. 36: "if the evidence you would discover tells strongly against your view, there is a good chance you're wrong" ✓
  - p. 24 n. 3: Hawthorne 2004, 181 on encroachment ✓
  - pp. 29–33: the Suitcase case ✓
- G&S 2023:
  - p. 104: K-normality ✓
  - p. 107: "given TRANSPARENCY, K-NORMALITY entails KK" ✓
  - p. 127: "loses knowledge whenever |x−y| > (2−√2)c", for an accurate first reading ✓
  - p. 128: "MARGINS, COMPARABILITY, and STATISM together entail NO DEFEAT" ✓
  - p. 129: Gaussian derivation ✓
  - p. 138: Flipping-for-Heads variant ✓
  - §8: defeat by discovering what one already knows ✓
- BRN:
  - §5 n. 18: c ≈ 1.96σ and ~.37 ✓
  - Prop. 1 ✓
  - §7: "STATISM is the exception rather than the rule" ✓
  - App. D.3: the definition, the n+1 Flipping counterexample, and "p but I'll never learn that p" ✓
  - Prop. 5 ✓
- Bibliographic data confirmed: Salow 2025; BRN 2025; G&S 2023 (*Phil Review* 132: 89–145); Das 2023 (*BJPS* 74: 25–55); Good 1967 (*BJPS* 17: 319–21); Carter & Hawthorne 2024; Goldschmidt 2024.

**Not confirmed**
- Hong 2026 contents and section numbers.
- The Hong 2024 page range.
- The pages and content of Ahmed & Salow 2019.
- Geanakoplos 1989's exact statement.
- Hawthorne & Stanley 2008 (not checked; I am confident it exists).
- Goldschmidt's survey of stakes-sensitive variants.

## Proof check

**Lemmas and theorems**
- **Lemma 1:** valid for finite S with a full-support prior. V ≤ −Pr(s0|M) < 0. ✓
- **Lemma 2:** valid. Maximal post-kens partition M by reflexivity and nestedness. The induction on maximal proper sub-kens is correct, and the final step averages per-cell maxima. ✓
- **Lemma 3:** valid. In the transitivity case with t ∈ B(F), chaining gives u ≫ v ⪰ t ⟹ u ≫ t. Nestedness follows from comparability. Statism is not needed within a fixed F. ✓
- **Lemma 4:** valid. p_v ≠ E holds automatically when v ∉ M ⊇ B(E). ✓
- **Theorem 1(a):** valid. Kens in different cells are disjoint; within a cell, Lemma 3 applies; no relative defeat ⟹ Lemma 2; the converse is Lemma 1. ✓
- **Theorem 1(b):** valid. Gappedness gives s ≫ v, so v ∉ B(E∩c); and v ⪰ s ≫ v would give v ≫ v. ✓
- **Theorem 2:** valid. Factivity is used only for the C(x) claim. ✓
- **Corollary (i):** valid. ✓
- **Corollary (ii):** valid for finite S. Not licensed as stated for continuous Bjorn or infinite Flipping for Heads.

**Worked examples**
- **Three-state example** (a ≻ b ≻ c; a ≫ b, a ≫ c; not b ≫ c): B(E) = {a}; K(b) = {a,b}; after learning ¬a, K = {b,c}. ◊− holds for every E and p, checked case by case. ✓
- **Empty-question example:** the plan pays (1,2), value 1.5 against 1, so V = +0.5. ✓
- **Bjorn**, computed independently with σ = 1 and c = 1.96. μ ~ N(0, 1/2) and d ~ N(0, 2) are independent, and δ = 2μ² + d²/2. ✓
  - At 10:1, decline iff P(lose | post-ken) > 1/11, i.e. iff |d| > 2.196 = 1.12c. ✓
  - P(|d| > 2.196 | δ ≤ c²) ≈ 0.049 ✓. At 20:1 the value is ≈ 0.12 ✓; at 100:1, ≈ 0.27 ✓.
  - Fallibilist EV: 0.95 − 10(0.05) = 0.45. ✓
  - P((2−√2)c < |d| ≤ √2c) = 0.367. ✓
  - CEU −0.63: K^D = {δ ≤ 2.411 + c²} ∩ {|d| > 2.196}. My coarse quadrature gives P(lose) ≈ 0.144 (EV ≈ −0.59), against 0.148 needed. Consistent within my error.
- **Flipping for Heads** (n = 4, t = 0.9): B = {s1, …, s4}. After learning q, Pr(s1|q) = 0.889 < 0.9, so B = {s1, s5}. KDT value = −Pr(s1|K) = −0.533 ✓. On BRN's reading K^D = {s1} and CEU bets; on the discovery reading K^D = {s1, s5}, the bet's EV is −1.33, and CEU looks ✓.

**Theorem 3 (the three-act problem): valid.**
- Every post-answer ken either contains a non-K state (decline, for large L) or lies in K and excludes s0 by transitivity (choose β).
- So looking never leads to β1. Since ζ ≠ 0 and β1 ≠ 0 everywhere, D = E.
- Then P(u_β1 − u_look) ≥ P(s0)(1+εN) − ε > 0.
- A.6 has a minor quantifier-order slip (L chosen before ε); it is harmless if L is chosen for all ε ≤ 1.
- Philosophical import: see the single most serious problem. In every instance of the construction, CKD is silent (by the ⪰-maximal-state argument) and the verdict-change rule prefers looking (by the ⪰-maximal state of the decline set).

**A.5 (positive-measure Gaussian argument): valid in state space.**
- The post-answer ken is |μ| ≤ max(c/√2, |μ_s|). ✓
- An s with μ_s = 0 and d_s²/2 ∈ (R−c², R) has post-answer max δ = c² + d_s²/2 > R. ✓
- The neighbourhood and continuity step is fine. Conditioning on lines uses the regular conditional distribution given y2, which is well defined for this partition. ✓
- The informal gloss "a weight" fails for R ≥ (1+√2)²c² (Major problem 2).

**Quantifier distinction**
- "Safe" quantifies over all decision problems, so a failure of safety is: there is a question and there is a problem. §4 and §6.5 state this correctly.
- In Bjorn, the order is "for every situation there is a bet", with stakes varying by situation (§3). ✓
- Slips:
  - the abstract says "non-negative value" without "for every decision problem";
  - §1's "failures of Good arise at every situation with inductive knowledge" needs the p_v questions and finite S;
  - §4's sentence about Bjorn and Corollary (ii) is wrong.

## Top five changes

The essay is at 5,870 words, so each change says what to cut.

1. **Rebuild §5 around the hypothesis Salow actually names.**
   - Define the verdict-change rule: condition on "looking would lead me to b", for each act b.
   - Either prove its safety boundary (a new theorem), or concede that it escapes Theorem 3. In the latter case, demote Theorem 3 to a three-sentence remark: the payoff-difference translation coincides with KDT on tie-free problems, and CKD is silent there.
   - Cut the θ-threshold paragraph in §5.2 (~170 words) and the perturbed-Bjorn sentence. Compress §5.3 to ~150 words. This saves about 400 words.
   - Remove "the conditional repair fails" from the abstract, §1 and §7 unless the new theorem succeeds.
2. **Make the Bjorn claims exact.**
   - Rewrite the last paragraph of §3 as three claims: weight bets at 10:1 for normal situations; a joint weight-and-reading bet at every situation (A.5); no weight-only Lemma-1 bet when δ(x) ≥ (1+√2)²c².
   - Delete "reopen a weight he now rules out" and "Bjorn shows that the questions needed for (ii) can be as natural as a second reading".
   - Add one sentence noting that, in state space, Preservation fails at every nonzero reading difference (≈ 0.95).
   - Net change about +60 words.
3. **Place Theorem 1(a) in the value-of-evidence literature** (~150 words in §1).
   - Cite Skyrms 1990 and Huttegger 2014 on reflection, Dorst et al. 2021 on Total Trust ⇔ Value, Dorst 2020, and Geanakoplos via Das.
   - Quote what Hong 2026 shows about information value.
   - State the increment as gappedness, the graded collapse, and the 10:1 datum.
   - Cut §6.2 entirely (~170 words) and the enumeration paragraph in §4 (~120 words).
4. **Add a modelling paragraph on optional inquiry** (~150 words in §2).
   - Say what y2 is when Bjorn does not look, and show that K_E(x) does not depend on the act.
   - Address BRN's NESTEDNESS (App. A) and the question-sensitivity of probabilistic normality. At minimum, check the 10:1 verdict in the Goldstein–Hawthorne weight-question model, or flag it as open.
   - Restrict Theorem 1(b) to one question at a time.
   - Cut §6.3 and §6.7 to one sentence each (~200 words), and §6.1's numerical empty-question example to a clause (~80 words).
5. **Rewrite the abstract and §1** (cut ~200 words).
   - Give a one-sentence thesis and three results with explicit quantifiers: "for every decision problem", "given the p_v questions", "in finite models".
   - Replace "the practical content of Salow's dissolution, namely Good's theorem" with "the development Salow anticipates (2025, 35)".
   - Add the missing references: Harman 1973; Kripke 2011; Williamson 2000; Fantl & McGrath 2002; Weatherson 2005; and the trust literature in change 3.

Net effect: about 1,100 words cut and 400 added. That leaves roughly 5,200 words and room for a real theorem about the verdict-change rule.
