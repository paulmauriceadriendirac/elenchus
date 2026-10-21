# Lane L6 map: Conditionals, modals and probability

Lane-mapper, 2026-10-21. Keys refer to `state/lanes/L6/refs.json`. Read-level tags: **[FT]** full text read (or the stated sections), **[Abs]** abstract, **[Sec]** a retrieved secondary source (named), **[T]** title or metadata only. A clause marked *(inference)* is mine, not a source's. Fetch requests are filed for unread key texts (§9).

## 1. Scope and central questions

1. **Probabilities of conditionals.** Does rational credence in "if A, C" equal Pr(C|A) (Adams's Thesis for conditional-free A, C; Stalnaker's Thesis for arbitrary A, C)? If it does, what are conditionals (propositions, context-relative propositions, non-propositional contents, trivalent contents), and how do credence and update work for them?
2. **Logic of the natural-language conditional.** Which of these are valid: Modus Ponens (MP), Import-Export (IE: A>(B>C) ≡ (A∧B)>C), Identity (A>A), Conditional Excluded Middle (CEM: (A>C) ∨ (A>¬C)), Simplification of Disjunctive Antecedents (SDA), If-to-Or ((A>C) ⊢ ¬A∨C), Duality (A>◇C ≡ ¬(A>¬C)), If-Might Contradiction (IMC: A>C and A>◇¬C are incompatible)? How strong is the logic: Lewis's VC, Stalnaker's C2, something between C2 and the material conditional?
3. **Epistemic modals.** How can "p and might not p" be a contradiction, even embedded, when "might not p" does not entail "not p"? Which classical rules fail (distributivity, disjunctive syllogism, modus tollens with "must", reductio)?
4. **Free choice (FC).** How can "may (p or q)" entail "may p and may q" without trivializing the logic of modals and disjunction? Is FC semantic, pragmatic or grammatical? How does it relate to SDA?
5. **Learning conditional information.** How should credences change on learning "if A, C" (certainly or uncertainly), and on supposing A subjunctively?
6. **Causal-model semantics for counterfactuals.** Can structural-equation models give the semantics and logic of counterfactuals, including complex antecedents, backtracking and chance?

Counterpossibles and deontic logic beyond FC are touched on only where relevant.

## 2. Positions and their best arguments

**Indicatives: truth conditions.** (a) *Material conditional* plus a pragmatic story (Grice, Jackson). Williamson 2020 revives it, holding that "if" is truth-functional and that the suppositional procedure is an imperfectly reliable heuristic that is "implicitly inconsistent" [Abs; Sec: Edgington2025SEP §4.4]. (b) *Selection semantics* (Stalnaker1968Theory; logic C2, which validates CEM). Dorr and Mandelkern "believe that all the principles of C2 are plausible as far as natural language conditionals go" (DorrMandelkern2026Sequence p. 3) [FT]. (c) *Variably strict / Lewis* (VC; rejects CEM; accepts Duality). (d) *Restrictor view*: if-clauses restrict modals (Kratzer2012Modals) [Sec: EgreRott2021SEP §8.1]. (e) *Context-dependent strict conditionals* (Gillies2009Truth) [Sec]. (f) *Dynamic or informational* views (Veltman1996Defaults; Goldstein2022Sly; Santorio2022Path) [Abs]. (g) *No truth conditions; suppositional* (Adams1975Logic; Edgington1995Conditionals). CiardelliOmmundsen2024Probabilities [Abs] update Adams: the probability of a conditional is "a probability under a supposition", conditionals do not express propositions, and so their probabilities are "not subject to the standard laws". (h) *Trivalent / de Finettian* (EgreRossiSprenger2025Certain, 2026Probability) [FT]. (i) *Inferential-disposition* view (Khoo 2022, *The Meaning of If*) [Abs of the book only]. (j) The *bounded theory* (Mandelkern2024Bounded) [Abs]: "a standard truth-conditional layer" plus "bounds" that limit admissible interpretations relative to local information, which captures dynamic effects without dynamic semantics' logic.

**Probabilities.** These are the tenability strategies against Lewis-style triviality:
- *Context-relativity.* van Fraassen's sequence models; Bacon2015Stalnaker [Abs]: credence in what "if A then B" expresses "in a context where E is salient" equals conditional credence, and this is tenable "within a standard possible world semantics based on selection functions" that "cannot be understood in terms of similarity".
- *Deny conditionalization for modal or conditional contents.* GoldsteinSantorio2021Probability build a probabilistic path semantics satisfying Ramsey's thesis on which "conditional degrees of belief do not change by conditionalization" [Sec: Edgington2025SEP §5]; their author summary says they capture Stalnaker's Thesis "in a fairly standard dynamic semantics" [author page].
- *Trivalence.* EgreRossiSprenger2026Probability [FT, manuscript] obtain "Stalnaker's Thesis in full generality" at the price of "the non-classical behavior of conjunction (and disjunction) and the violation of the product rule".
- *Restrict the thesis* to simple conditionals or to fragments (McGee 1989; Dorr & Mandelkern's tree models).
- *Accept failure.* Williamson treats the equation as heuristic.

**Modus ponens.** McGee1985Counterexample (the election case) targets MP for conditionals with conditional consequents. Defenders: Bledin2015Modus [T]; Stojnic2017One [Abs] (classical logic kept, with apparent counterexamples explained by context-shifting mechanisms "reflected in the logical form"); LoGuercioRubin2024Revisiting [Abs, Croatian; snippet] (pragmatic confounds). Critics: Mandelkern2020Counterexample [Abs]: for subjunctives MP "does not preserve either truth or rational full acceptance". KolodnyMacFarlane2010Ifs [T] is the miners case for deontic consequents. Charlow2023Modus [Abs] gives a decision-theoretic prima facie counterexample and recasts consequence "normatively". Briggs2012Interventionist [Abs] shows interventionist counterfactuals invalidate MP. Berntson2026Against [Abs] is against MP for "might".

**Epistemic modals.** Positions:
- *Orthodox contextualism* with a Gricean explanation of embedding (DorrHawthorne2013Embedding) [Abs: "using broadly Gricean resources"].
- *Domain or informational semantics* (Yalcin2007Epistemic).
- *Dynamic semantics* (Veltman; Goldstein2019Generalized [Abs], which derives Kripke and update semantics as special cases).
- *Bounded relational semantics* (Mandelkern2019Bounded).
- *Semantic expressivism* (HawkeSteinertThrelkeld2021Semantic [Abs]).
- *Probabilistic contents* (Moss2015Semantics; Moss 2018).
- *Orthologic* (HollidayMandelkern2024Orthologic [FT preprint]): negation is an orthocomplement but not a pseudocomplement, so p∧◇¬p ⊨ ⊥ holds while ◇¬p ⊭ ¬p, and distributivity and disjunctive syllogism fail.
- AloniIncurvatiSchlöder2023 [Abs]: epistemic modals "interfere with hypothetical reasoning". Reductio and the classical rules for ∃ and ∨ are defective; they offer a sound and complete natural deduction system.

**Free choice.**
- *Exhaustification / grammatical*: Fox 2007; BarLevFox2020Free, with "Innocent Inclusion" [SALT abstract].
- *Semantic via nonclassical disjunction*: Zimmermann2000Free; Goldstein2020Free [Abs] (a classical semantics cannot validate FC). Goldstein2019Free [Abs] treats FC as a homogeneity effect, with definedness-sensitive entailment and "retaining a wide variety of classical principles except for the transitivity of entailment".
- *Bilateral state-based logic*: Aloni2022Logic [Abs] uses a non-emptiness atom; "neglect-zero" pragmatic enrichment predicts FC and its cancellation under negation. AloniAnttilaYang2024State [Abs] supply the expressive completeness and axiomatization.
- *Disjunction itself modal*: Mandelkern2024Disjunction [Abs]. The formula was lost in the retrieved abstract: "or" is interpreted with a possibility modal, building on Zimmermann, Geurts and Goldstein.
- *Redundancy operator*: BlumbergGoldstein2025Semantic [Abs].

**Learning conditionals.**
- Douven2012Learning [Abs]: updating on conditionals "at least sometimes proceeds on the basis of explanatory considerations".
- Gunther2018Learning [Abs]: "Jeffrey imaging on the minimally informative proposition expressed by a Stalnaker conditional", which matches Douven's benchmarks and the Judy Benjamin problem.
- EvaHartmannRad2020Learning [Abs]: "a core set of widely accepted Bayesian norms is sufficient to identify a normatively privileged updating procedure".
- EgreRossiSprenger2026Probability [FT]: learning a simple A→B "is the same as learning the material conditional A⊃B" (Prop. 6). Trivalent conditionalization on A→B, conditioning on A⊃B, and minimizing an f-divergence under p′(B|A)=1 are equivalent (§6). They report that GoldsteinSantorio2021 and Santorio 2022 §7 also endorse the update-equivalence [Sec].

**Causal-model semantics.**
- *Interventionist* (GallesPearl1998; Halpern2000Axiomatizing; Briggs2012Interventionist; Hiddleston2005Causal).
- *Filtering premise semantics* (Santorio2014Filtering [Abs]: filtering is "a possible worlds semantics counterpart of Pearl's interventions").
- *Inquisitive / background–foreground* (CiardelliZhangChampollion2018Two [FT]).
- *Exogenous interventions* (Vandenburgh2023Backtracking [Abs]: backtracking, complex antecedents, "familiar principles of counterfactual logic").
- *Under determinism*: neither miracles nor backtracking (Gallow2023Causal [Abs]), or history different "all the way back" (Dorr2016Against [Abs]).

## 3. Landmark results

1. **Lewis (1976) triviality** (as stated in EgreRott2021SEP §5.2) [Sec]. Stalnaker's Hypothesis plus Factorization (Pr(B>C|A) = Pr(C|A∧B)) yields Pr(A>C) = Pr(C) whenever Pr(A∧C), Pr(A∧¬C) > 0. Given Stalnaker's Hypothesis, Factorization is equivalent to IE. Strengthenings include Hájek & Hall 1994, Bradley 2000, Milne 2003 and Fitelson2015Strongest ("the strongest possible Lewisian triviality result for the indicative conditional" [Abs]). KhooMandelkern2019Triviality [Abs] identify IE as the "common culprit" of Fitelson's strengthenings of Lewis's and Gibbard's results.
2. **Hájek1989** [Sec]. On any finite W with at least three worlds of positive probability, there are more distinct conditional-probability values than unconditional ones. So no proposition need carry Pr(C|A) (EgreRott2021SEP §5.3.1).
3. **Bradley2000 Preservation** [Sec]: if Pr(A)>0 and Pr(C)=0 then Pr(A>C)=0 leads to triviality. MandelkernKhoo2019Against [Abs] reply that Preservation is invalid and that its appeal comes from "Local Preservation", which Boolean theories can validate non-trivially.
4. **Gibbard/Dale collapse.** EgreRott2021SEP §3.5 states it this way: MP, IE, Left Logical Equivalence and Supraclassicality, together with "the conditional entails the material conditional", yield the converse. HollidayMandelkern2024 §6 [FT] give Dale 1974's form: in a classical setting, RK→, If-to-Or, Identity and IE collapse ">" to "⊃". McGee 1989 keeps IE and drops MP.
5. **Stalnaker (1974 letter) and van Fraassen (1976)** (DorrMandelkern2026Sequence §7) [FT]. Every Boolean probability model extends to an ω-sequence model that is (B>(B>B))- and ((B>B)>B)-Stalnaker (Fact 7.1, Fact 7.2). However, "No non-trivial probabilistic order model is ((B∨(B>B))>B)-Stalnaker" (Thm 7.8b, from Stalnaker's letter).
6. **Gärdenfors (1986)** [Sec: EgreRott2021SEP §6.2]. A belief-revision model satisfying AGM (∗4) Preservation, (∗5) Consistency and the Ramsey test "K ∋ A>B iff B ∈ K∗A" is trivial: no belief set is compatible with three pairwise inconsistent sentences.
7. **Adams.** p-validity on the flat fragment equals system P and coincides with Stalnaker's logic there (Gibbard 1980 proof) [Sec].
8. **Ellis–Jackson–Pargetter (1977).** SDA plus Left Logical Equivalence yields Antecedent Strengthening [Sec: SEP §3.5].
9. **Santorio's trilemma.** CEM, Duality and IMC are jointly inconsistent on standard consequence. Path semantics keeps CEM and IMC and drops Duality [Sec: EgreRott2021SEP §8.1]. Mandelkern2018Talking [Abs] uses credence judgments against Duality and for CEM.
10. **Cariani & Goldstein (2020)** [Abs]. CEM and SDA "together with elementary logical assumptions … yield a variety of implausible consequences". Both can be had with alternatives plus homogeneity at the cost of "the transitivity of entailment".
11. **Goldstein2020Counterfactual** [Abs]. Duality plus "several other theses" (including strictness) gives the Counterfactual Direct Argument, A>(B∨C) ⊨ A>(¬B>C). That in turn collapses the subjunctive to the material conditional under several assumptions.
12. **Russell & Hawthorne (2016)** [Abs]. Stripped to "a minimal core", Lewis's arguments extend to epistemic "might", probability claims and comparative value. Non-factualists must "give up basic structural principles about how epistemic states can be updated", which parallels dynamic semantics.
13. **Goldstein2019Triviality** [Abs]. Transparency theses ("believe probably p" = high credence) are inconsistent with propositional meanings for probabilistic modals. Dynamic semantics validates them "only if probabilistic modals do not satisfy the axioms of the probability calculus".
14. **Santorio2022Trivializing** [Abs]. These three are incompatible: informational consequence that differs from classical consequence; certainty-preservation; classical Bayesian constraints on credence.
15. **Counterfactual triviality.** Williams2012Counterfactual [Abs]: a counterfactual Ramsey test, even in the weak "Ramsey Bound" form, is open to Lewis's argument. Santorio2022General [Abs]: given the subjunctive Ramsey test, rational credences in "would" and "might" counterfactuals "have to be identical".
16. **Kocurek2022Does** [Abs]. "Chance ensures could" plus would/might clash "entail absurdities" given modest closure principles. On the best repair they support only counterfactual *indeterminism*.
17. **Epistemic contradictions.** Adding p∧◇¬p ⊨ ⊥ to any classical modal logic yields ◇¬p ⊨ ¬p. In a classical base, Identity, If-to-Or and Modalized IE give "Qualified Collapse", ψ ∧ (ψ→◇(ψ∧φ)) ⊢ φ→ψ (Prop. 6.24) (HollidayMandelkern2024) [FT preprint].
18. **Free Choice impossibility** (Goldstein2020Free) [Abs]. "Some kind of nonclassical semantics for disjunction is required." Among dynamic FC-validating meanings, the strongest world-eliminating component is the classical one. The classic Kamp problem: FC plus monotonicity of ◇ plus ∨-introduction gives ◇p ⊢ ◇q.
19. **Interventionist logic** (Briggs2012) [Abs; Sec: HitchcockSEPCausalModels §3.2]. Briggs gives a sound and complete axiomatization for acyclic models with Boolean antecedents and arbitrary consequents. MP fails. In the gas-grill model, with Flame=3, Flame=3 □→ (Gas=2 □→ Meat=3) is true but Gas=2 □→ Meat=3 is false. Classical equivalents are not substitutable in antecedents; exact equivalence (Fine 2012 truthmakers) is. Halpern2000 [Abs] axiomatizes recursive, unique-solution and arbitrary models.
20. **Two-switch data** (CiardelliZhangChampollion2018Two p. 592) [FT]. "A∨B > off" was judged true "almost 70%" of the time and "¬(A∧B) > off" "only 22%". So truth-conditionally equivalent antecedents make different contributions, contrary to minimal-change analyses.
21. **Dorr & Mandelkern (2026)** [FT]. The logic of ω-sequence semantics is C2.FS, which is C2 plus Flattening ((p>((p∧q)>r)) ↔ ((p∧q)>r)) plus Sequentiality. For arbitrary ordinal sequences the logic is C2.F. To the authors' knowledge, no logic strictly between C2 and "Materialism" had been explored before. Tree models validate exactly C2 and support (B>L>|B)-Stalnaker probabilities (Thms 7.5, 7.6). Flat plus (P>L>)-Stalnaker implies the stronger (⟨P>P⟩∧>L>|⟨P>P⟩∧) form (Thm 7.7). Several stronger theses are impossible (Thm 7.8).
22. **Canonical cases.** Sobel and reverse-Sobel (Heim) sequences; McKay–van Inwagen's Spain (against SDA); Gibbard's Sly Pete (standoffs); McGee's election; the miners; Morgenbesser's coin; Edgington's coin (learning); Khoo's Poker Paul (left-nested probability); Judy Benjamin; Hájek's quantum-tunnelling argument for counterfactual scepticism (StarrKocurek2025SEP §7.1).

## 4. The frontier (2019–2026)

**Triviality and tenability are converging on "non-classical credence" or "non-classical connectives".** Ciardelli & Ommundsen (2024) say probabilities of conditionals "violate standard probability theory". Goldstein & Santorio (2021) give up conditionalization for modal contents. Égré, Rossi & Sprenger (2026) give up the product rule and classical ∧/∨. Santorio (2022 PPR) shows informational consequence forces exactly this choice. Willer2025Credences [Abs] claims a *strict* analysis can accommodate Stalnaker's Thesis and CEM "in a bilateral dynamic setting" that extends the Ramsey test to rejection. Égré et al. (2026) answer Khoo (2022) on left-nested conditionals, drawing on Kaufmann (2023) and reading Poker Paul as a scope/topic effect and Edgington's coin as pragmatic. Dorr & Mandelkern argue, against van Fraassen, that sequence semantics "cannot be motivated by indirect considerations about the probabilities of conditionals" (p. 4). Wójtowicz & Wójtowicz (2021 L&P; 2023 JPL [Abs]; 2025) build graph, Markov and finite models for nested-conditional probabilities.

**Logic: C2 and beyond versus weaker logics.** The C2 camp: Dorr & Mandelkern; Dorr & Hawthorne's manuscript "If...: A theory of conditionals", reported as discussing background-condition versions of Stalnaker's Thesis [Sec: D&M §7]; Mandelkern 2018; Santorio's path semantics. Weiss2026Note [Abs] gives an infinite descending chain of normal logics between VC and C2, "each characterized by a certain generalization of conditional excluded middle". RamotowskaEtAl2025Counterfactuals [Abs] report experimental "support for selection-based theories" over universal and homogeneity theories. Counter-pressure: Berntson2026Against [Abs] argues that an unflipped coin's "if flipped, it might land heads/tails" is "flatly inconsistent" with Lewis's and Stalnaker's theories. IE is now widely rejected or restricted (Mandelkern2020Import, 2021If; Khoo & Mandelkern 2019). The 2025 WoLLIC papers (Raidl and Gomes) on export counterexamples and "implicative conditionals" escaping Gibbard collapse are known from search snippets only [unverified; not in refs].

**Modus ponens.** Mandelkern (2020) is the strongest anti-MP datum (subjunctive, both senses of validity). Holliday & Mandelkern note that If-to-Or survives where MP fails (Santorio's die case: certain of "if even, then if prime, two" while the antecedent is about .5 and the consequent about .25). That blocks the McGee move of restricting If-to-Or to Boolean consequents in a classical base. Defenses continue: Charlow 2023 (normative consequence), Lo Guercio & Rubin 2024, and Wójtowicz & Wójtowicz 2025 ("Deep and shallow conditionals", three alleged counterexamples) [T].

**Counterfactual probability and scepticism.**
- Schultheis2023Counterfactual [Abs] derives "a tenable version of Skyrms's Thesis from a tenable version of Stalnaker's Thesis" plus chance deference.
- Santorio2025Probabilities [Abs]: "The chance of a counterfactual 'If A, would C' equals the chance of C, in the counterfactual scenario that A". This is said to avoid triviality and to do better than Skyrms's Thesis.
- Kocurek (2022) defends indeterminism against Hájek's scepticism. Boylan2024Counterfactual [Abs] argues scepticism yields "only very limited knowledge about the future" and suggests contextualism about knowledge is needed.

**Epistemic modals.** Holliday & Mandelkern's orthologic, Aloni, Incurvati & Schlöder's natural deduction, and Hawke & Steinert-Threlkeld's semantic expressivism compete on how little classical logic to give up. HollidayMandelkernZhang2024Conditional [FT §4] find that many LLMs accept MT and DS with "must" (MTmu, DSmu) and McGee-style CMP, which the authors say humans recognize as failing. Many models accept narrow-scope but reject wide-scope FC.

**Free choice.** The live contest is grammatical exhaustification (Bar-Lev & Fox) versus semantic/pragmatic state-based accounts (Aloni; Goldstein's homogeneity; Mandelkern 2024). Experiments test their divergent predictions: TieuBillRomoli2019Homogeneity [Abs] report results that "present a challenge for the implicature approach".

**Learning conditionals.** The question is whether learning a simple indicative is just conditioning on the material conditional (Égré et al. 2026, Goldstein & Santorio per Égré et al.). Opposed are Edgington's coin, Khoo, Douven's explanationist data, and Günther's imaging. EvaShearFitelson2022Four [Abs] vindicate "conditionalization is a probabilistic version of revision, while imaging is a probabilistic version of update". On partial *subjunctive* supposition, EvaHartmann2021Logic [Abs] and Nielsen2022Harder [Abs] show that imaging-based accounts "always violate monotonicity". Schulz2025Learning [T].

**Causal models.** Complex antecedents are handled by Briggs; Rosella & Sprenger 2024 (probabilities for disjunctive antecedents via distance-weighted submodels) [Sec]; Wysocki2023Event [Abs] ("semaphore interventions" for antecedents realizable "in infinitely many ways"); and Vandenburgh 2023. Probabilistic extensions: BarberoSandu2024Multiteam [Abs] (normal form for Pearl's ladder; "no usual, countable language is apt"); IbelingIcard2020Probabilistic [Abs] (complete axiomatizations; PSPACE decidability). On the philosophical side: Gallow 2023 and Dorr 2016 on determinism, and Goodsell2022Tossing [Abs], which argues that the "widespread disposition to infer counterfactual independence from causal independence" is "mistaken".

## 5. Open problems

### 5a. Marked open in the literature

1. **Explaining Flattening.** C2.F needs an intuitive semantics. Similarity cannot validate it, and "we leave it as an open problem for proponents of C2.F" (DorrMandelkern2026 §4.1, arXiv v2 p. 24).
2. **A probabilistic route to Flattening.** An argument from a restricted Stalnaker's Thesis to a restricted Flattening "still seems like an open possibility" (D&M §7, p. 44).
3. **Probability-1 sentences in tree models.** Characterize the set of sentences that always get probability 1 in tree models with product measures: "Could it simply be C2 + S5?" (D&M fn. 37).
4. **Extending Theorem 7.8.** Does Thm 7.8(c) hold without "flat", and (d) for flat order models or all order models? (D&M fn. 38).
5. **Qualified Collapse.** Does the minimal conditional epistemic orthologic with all the Figure 18 principles avoid it? Read in the 2022 arXiv version of HollidayMandelkern2024 §6; not checked against the published text.
6. **Same-level MP.** Is MP valid when antecedent and consequent come from the same "epistemic level", even if the consequent is non-Boolean? (H&M fn. 46, "future work"). The same source also lists quantifiers, presuppositional treatment of indicative embeddings, probabilities and the matching pragmatics (H&M conclusion).
7. **Complex antecedents in interventionist semantics.** Generalizing to complex antecedents "is an open research task" (StarrKocurek2025SEP §6.3). Briggs, Vandenburgh, Rosella–Sprenger, Wysocki and Ciardelli et al. give rival answers.
8. **Strict analyses and probability.** Accounting for probability judgments (an unflipped fair coin: 50%, not 0%) "is an open research program for strict theorists" (SEP §4.3; Willer 2025 is "a recent attempt").
9. **A unified theory of "if".** Indicative versus subjunctive, epistemic readings of counterfactuals, fake tense and backtracking: "one of the Holy Grails" (SEP §7.3). Ciardelli & Ommundsen 2026 (*Mind*, on will-conditionals) [Abs] bear on this.
10. **Counterfactual probability.** Theorists "have only begun to scratch the surface" in carrying indicative lessons over (SEP §7.1). The dispute between scepticism (Hájek), indeterminism (Kocurek) and contextualism (Boylan; K. Lewis) is unresolved.
11. **Counterlogicals.** Whether they trivialize counterfactual logic "is still a live issue" (SEP §7.2).
12. **Trivalence.** Trivalent counterfactuals and trivalent conditionals interacting with modalities are open. A trivalent characterization of the non-flat Stalnaker and Lewis logics is "an open question" (EgreRott2021SEP §2.3, citing M. Schulz 2009). Égré, Rossi & Sprenger's 2026 *J. Semantics* paper on "might/must" [Abs] addresses the modal part.
13. **Douven's evidential-support logic.** "a sound and complete axiomatization … is still an open problem" (EgreRott2021SEP §7).
14. **Adams's Thesis.** Whether it holds empirically, "even for simple conditionals", "is still debated", given relevance effects (SEP §5.3.2; SkovgaardOlsenEtAl2016Relevance).
15. **Gärdenfors's theorem.** No consensus has emerged on the right response (SEP §6.2).
16. **Credence for informational semantics.** Informational theorists "need to either give up the idea that credence applies to epistemic discourse, or develop a nonclassical theory of credence and credal update" (Santorio2022Trivializing). Russell & Hawthorne 2016 set the parallel demand for non-factualists.
17. **Partial subjunctive supposition.** Escaping Nielsen's result requires "rejecting the general framework", which "would be a surprising and interesting outcome" (Nielsen2022).
18. **Learning a conditional.** Égré et al. (2026 §6) concede that the alleged counterexamples to "learning A→B = learning A⊃B" (Edgington's coin, Poker Paul) "need to be investigated more thoroughly".
19. **The might-counterfactual coin.** Berntson2026 "consider[s] how the problem might be solved", so no solution is settled.
20. **Spare probabilistic models.** Can a technically simpler (for example finite) model for probabilities of conditionals replace Stalnaker–Bernoulli spaces? (Wójtowicz & Wójtowicz 2023 JPL [Abs] give one; how far it extends is not settled.)

### 5b. Pressure points *(all inference)*

1. **If-to-Or under interventionism.** In Briggs's gas-grill model, Flame=3 holds, Flame=3 □→ ψ holds, and ψ is false. So subjunctive If-to-Or fails there along with MP. Holliday & Mandelkern's generalization (If-to-Or survives MP failures) was drawn mainly from indicatives. Do subjunctive If-to-Or judgments in Briggs-type cases side with interventionism or with orthologic? This is a checkable discriminating case.
2. **Morgenbesser versus interventionism.** Interventionist semantics holds fixed causally independent variables by construction. If Goodsell (2022) is right, it builds in the very inference he rejects. I found no published reply relating the two.
3. **Learning counterfactual information** is under-theorized next to indicatives. Combining Santorio's 2025 principle, Nielsen's monotonicity result and imaging (Günther) may yield a small impossibility result for subjunctive learning. Unchecked.
4. **The price list.** Recent consistency proofs trade different goods: transitivity of entailment (Cariani & Goldstein; Goldstein's homogeneity), distributivity (Holliday & Mandelkern), the product rule (Égré et al.), conditionalization (Goldstein & Santorio), Duality (Santorio; Mandelkern). No source compares them on a common case set. A minimal-inconsistency map over a fixed principle list (MP, If-to-Or, IE-restricted, CEM, SDA, FC, IMC, Duality, distributivity, transitivity, conditionalization) could be machine-checked on finite models.
5. **Selection data versus Berntson.** If selection semantics is experimentally favored (Ramotowska et al.) yet unflipped-coin "might" pairs are jointly known, then supervaluation over selection functions must make each "might" true while CEM holds. Whether that is possible without Duality is exactly Santorio's trilemma applied to counterfactuals.
6. **Weiss's chain** gives a parameter: which generalized-CEM level natural language validates. A case discriminating adjacent levels would be a new datum.
7. **Trivalent learning versus imaging.** If learning a simple indicative is conditioning on the material conditional, Günther's imaging account and Douven's explanationist data cannot both be semantic. One of them must be pragmatic, as Égré et al. claim for Edgington's coin. That pragmatic story is untested on Douven's own benchmark cases.
8. **Flattening and indicatives.** D&M's tree models show Stalnaker-style probabilities without Flattening. Indicative intuitions that bear on Flattening alone (not on full IE) are not catalogued. Flattening is IE restricted to antecedents that entail the outer antecedent.
9. **Orthologic and FC.** Orthologic keeps ∨-introduction and monotone ◇, so it cannot validate narrow-scope FC semantically (Kamp's problem). It must therefore pair with a pragmatic or grammatical FC account. How that pairing fares on Double Prohibition is unexplored.

## 6. Known moves and graveyard

Presenting any of these as new will be recognized.

- **Probabilities of conditionals.**
  - Lewis's triviality and its many strengthenings (Hájek–Hall, Bradley Preservation, Milne, Fitelson). Hájek's cardinality argument. Russell & Hawthorne's "minimal core" generalization to "might", probability and value. *A "new general triviality theorem" must beat R&H 2016 and Fitelson 2015.*
  - Responses already on file: deny truth conditions (Adams, Edgington); context-relative propositions (van Fraassen, Kaufmann, Bacon); restrict to simple conditionals; restrictor view (Kratzer; Égré & Cozic; Charlow's objection that restrictors are not immune); trivalence (de Finetti, McDermott, Cantwell, Lassiter, Égré–Rossi–Sprenger); hyperconditionalization (Goldstein & Santorio); "probabilities of conditionals aren't classical probabilities" (Ciardelli & Ommundsen); Local Preservation (Mandelkern & Khoo).
  - Kaufmann's local/global counterexample to Stalnaker's Thesis (2004) [T].
  - McGee's 1989 IE-preserving probability construction, re-axiomatized by Cantwell2022Revisiting [Abs].
  - Stalnaker–Bernoulli / ω-sequence models, now fully axiomatized (D&M).
  - Imaging (Lewis 1976) gives the probability of Stalnaker conditionals. Edgington's straw example contrasts 91/100 with 1/10 (SEP §5.3.2).
- **Gibbard/Dale/McGee collapse**; Gibbard's Sly Pete standoffs (with a dynamic treatment in Goldstein2022Sly).
- **MP.**
  - Cases: McGee's election; the miners; Mandelkern's subjunctive cases; Charlow's dominance case; Briggs's interventionist failure; Berntson's "might".
  - Replies: informational validity (Bledin); context shift in logical form (Stojnić); pragmatics (Lo Guercio & Rubin).
  - The restriction to Boolean consequents (McGee), and why it fails with If-to-Or (H&M).
- **IE.** Mandelkern's Identity argument and his "and" argument. Khoo & Mandelkern's propositional-anaphora argument. "Restricted IE" with Boolean middle antecedent and "Modalized IE" (H&M).
- **CEM and Duality.**
  - Stalnaker versus Lewis. Williams2010Defending [T]. Mandelkern's credence argument against Duality. Santorio's trilemma. Goldstein's CDA collapse.
  - Cariani & Goldstein: CEM+SDA, with homogeneity and non-transitivity as the way out.
  - Willer 2022 on negated conditionals (bilateral) [Abs].
  - Experimental support for selection (Ramotowska et al.).
- **SDA.**
  - Fine/Nute intuitions; the Ellis–Jackson–Pargetter derivation; McKay–van Inwagen's Spain; Lassiter's chance counterexample (SEP).
  - Alternative-sensitive antecedents (Santorio 2018; Ciardelli et al. 2018; Fine 2012 truthmakers).
  - SDA is not a scalar implicature (Santorio2021Simplification [Abs], using "probably" and deliberative "ought").
- **Strict versus variably strict.**
  - Sobel/Heim sequences; dynamic strict accounts (von Fintel 2001; Gillies 2007) and their accommodation problem (which worlds get added); pragmatic replies (Moss 2012).
  - Strengthening with a Possibility, the counterexample that "extra dynamic resources cannot help" (BoylanSchultheis2021How [Abs]).
  - Williamson's contextually restricted strict counterfactuals.
- **Counterfactual scepticism.**
  - Hájek's chance argument. Responses: quasi-miracles (Lewis), Hawthorne 2005, contextual exclusion (K. Lewis 2016, criticized for a dilemma), counterfacts (Stefánsson), indeterminism (Kocurek), contextualism about knowledge (Boylan).
  - Agglomeration fails for high-chance thresholds (Hawthorne 2005; Leitgeb; Hájek). Requiring chance 1 makes most counterfactuals false (SEP §6.2).
- **Counterfactual triviality**: Williams 2012; Santorio 2022 would/might collapse. Skyrms's Thesis as baseline; Schultheis's derivation; Santorio's 2025 principle.
- **Epistemic modals.**
  - Yalcin's embedded epistemic contradictions; Dorr & Hawthorne's Gricean orthodox reply.
  - Dynamic semantics loses non-contradiction and excluded middle (H&M's complaint).
  - Failures of modus tollens and disjunctive syllogism with "must" (H&M; HMZ 2024).
  - "Must" is strong (von Fintel & Gillies).
  - Modal knowledge needs safety-style treatment (BeddorGoldstein2021Mighty [Abs]).
  - Attentional, non-informational effects of "might" on decisions (DeverSchiller2021This [Abs]).
- **Free choice.**
  - Kamp's problem; Ross's paradox; Double Prohibition; wide versus narrow scope FC.
  - Exhaustification and Innocent Inclusion; homogeneity; neglect-zero/BSML; disjunction as modal (Zimmermann; Geurts; Goldstein; Mandelkern 2024).
  - FC impossibility for classical disjunction (Goldstein 2020); experimental contrast of implicature versus homogeneity (Tieu et al.).
- **Learning conditionals.**
  - Judy Benjamin (van Fraassen 1981); Douven & Romeijn 2011 [T]; explanationist updating (Douven 2012); Jeffrey imaging on Stalnaker conditionals (Günther).
  - The "privileged" Bayesian update (Eva, Hartmann & Rad); the material-conditional equivalence (Égré et al. 2026) with f-divergence minimization.
  - Edgington's coin (predicted 2/3 versus the intuited 1) and Poker Paul (≈0.25).
  - Conditionalization ↔ AGM revision, imaging ↔ KM update (Eva, Shear & Fitelson).
- **Causal models.**
  - Pearl/Galles axioms (composition, effectiveness, reversibility); Halpern's three model classes; Briggs's logic.
  - "Causal counterfactuals are not interventionist counterfactuals" (Fisher 2017) [T].
  - Two-switch data and the foreground/background replacement of minimal change.
  - Exogenous interventions for backtracking; miracles versus backtracking under determinism (Lewis 1979; Dorr 2016; Gallow 2023); Morgenbesser's coin.
  - Ramsey-test analyses of causation in causal models (AndreasGunther2021Ramsey); causal and evidential conditionals in one model (Gunther2022Causal [Abs]).
- **Other.**
  - Counterpossibles: vacuism versus nonvacuism; impossible worlds; counterconventionals (Kocurek & Jerzak).
  - The Qualitative Thesis and Conditional Locality: margin-for-error tension (BoylanSchultheis2022Qualitative [Abs]).

## 7. The readership

From what I read; "[Abs]" means the claim rests on the abstract.

- **Matthew Mandelkern** (central).
  - For subjunctives MP "does not preserve either truth or rational full acceptance" (Mandelkern2020Counterexample [Abs]).
  - Identity is threatened by IE, so reject IE, with the indicative/subjunctive difference "play[ing] a key role" (2021If [Abs]).
  - IE sits badly with classical conjunction; adopt a limited IE (2020Import [Abs]).
  - IE intuitions support a "closely related but subtly different principle", and IE is invalid via propositional anaphora "given … a standard assumption" (with Khoo, 2019 [Abs]).
  - Against Preservation (with Khoo [Abs]).
  - Against Duality and for CEM via credences (2018Talking [Abs]).
  - The bounded theory (2019Bounded; 2024Bounded [Abs]); orthologic (with Holliday [FT preprint]); LLM conditional/modal reasoning (with Holliday & Zhang [FT]); "Disjunction and Possibility" (2024 [Abs]).
  - C2 and the logic of sequence semantics (with Dorr [FT]).
- **Simon Goldstein** (central).
  - Triviality for probabilistic modals [Abs]; Generalized Update Semantics [Abs].
  - Probability for epistemic modalities with Santorio [Sec].
  - Free Choice as homogeneity [Abs]; FC impossibility [Abs].
  - Conditional Heresies with Cariani [Abs]; the Counterfactual Direct Argument [Abs]; conditional assertion validates False Antecedent [Abs]; dynamic treatment of Sly Pete [Abs].
  - Mighty Knowledge with Beddor [Abs]; Redundancy with Blumberg [Abs].
- **Cian Dorr.**
  - Embedding epistemic modals: an orthodox Gricean explanation (with Hawthorne [Abs]).
  - Against counterfactual miracles [Abs].
  - C2 plausible; C2.F and C2.FS; tree models; probabilistic arguments do not motivate sequence semantics (with Mandelkern [FT]).
- **John Hawthorne.** General dynamic triviality (with Russell [Abs]); Dorr & Hawthorne 2013; Chance and Counterfactuals (2005), cited in SEP for Agglomeration failure and counterfacts [Sec]; co-editor of the Edgington Festschrift (2021) [T].
- **Branden Fitelson.** "Strongest possible Lewisian triviality result" [Abs]; four approaches to supposition (with Eva & Shear [Abs]); forthcoming "Probabilities of Conditionals and Conditional Probabilities — Revisited" [title, via CV]; PrSAT.
- **Mario Günther.** Learning conditional information by Jeffrey imaging on Stalnaker conditionals [Abs]; causal and evidential conditionals in causal models [Abs]; Ramsey-test analysis of causation with Andreas [author summary].
- **Josh Dever.** Epistemic modals change decisions without changing information (with Schiller [Abs]).
- **Organiser (not a judge): Zachary Goodsell**, on Morgenbesser's coin [Abs].

## 8. Formal toolkit

- **Possible-world semantics.** Selection functions (C2), order and sphere models (VC), Kratzer premise and ordering semantics, sequence, tree and order frames (D&M).
- **Dynamic and informational semantics.** Update with tests, informational consequence, domain semantics, bounded semantics.
- **Algebraic and possibility semantics.** Ortholattices; Jupyter notebooks with lattice countermodels (H&M).
- **Trivalent / de Finettian.** Cooper tables; logics C and U; p-validity.
- **Probability.** Ratio formula, Adams p-validity, Stalnaker–Bernoulli product measures, imaging, Jeffrey and Adams conditioning, f-divergence/KL minimization, sets of measures; conditional event algebras (Gilio, Sanfilippo).
- **Belief revision.** AGM, KM update, Ramsey test, Lockean bridges.
- **Team and state semantics.** BSML, multiteams. Also inquisitive semantics and alternatives; exhaustification operators; homogeneity and supervaluation.
- **Causal models.** SEMs, do-interventions, Briggs/Halpern logics, the causal hierarchy logics.
- **Experiments.** Crowdsourced truth-value judgments.
- **Usable here.** z3/sympy for finite countermodels; triviality claims are mostly finite-algebra statements (PrSAT is precedent).

## 9. Sources (read level)

- **Full text:** the four SEP entries (sections named in refs.json); DorrMandelkern2026Sequence (arXiv v2); HollidayMandelkern2024 (arXiv 2022 preprint); HollidayMandelkernZhang2024; CiardelliZhangChampollion2018 §§1–3; EgreRossiSprenger2026 (author's manuscript §§1, 6); EgreRossiSprenger2025 (arXiv intro).
- **Abstract, secondary or title:** everything else; each refs.json entry has a `seen` field. Classic theorems (Lewis, Hájek, Bradley, Gärdenfors, Gibbard) are stated from the SEP.
- **Fetch requests** (`requests/fetch/`). High: goldstein-santorio-2021, mandelkern-2020-counterexample, santorio-2025-probabilities, santorio-2022-path-semantics, mandelkern-2021-if-p-then-p, khoo-mandelkern-2019. Normal: schultheis-2023, briggs-2012, cariani-goldstein-2020, berntson-2026, eva-hartmann-rad-2020, fitelson-2015.
- **Verification:** `state/lanes/L6/refs.verification.json`; unmatched entries carry `manual_check`. Works named only through the SEP or another paper (Milne 2003, Hájek & Hall 1994, McGee 1989, Fox 2007, von Fintel 2001, Gillies 2007, Moss 2012, K. Lewis 2016, Leitgeb 2012, Kaufmann 2023, Kocurek & Jerzak 2021, Lassiter, Charlow 2016, Égré & Cozic 2011, Raidl & Gomes 2025) are not in refs.json. Verify each before citing.
