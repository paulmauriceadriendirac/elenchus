# Referee report — S5 Philosopher of language / formal semanticist (G3 literature-expert standards; mode report+lit) — P-600a

## Thesis and argument as I understand them (≤120 words)

Dorr and Mandelkern (D&M) hold that Flattening, p > (pq > r) ↔ pq > r, has strong prima facie appeal for natural-language "if" in both moods. The essay offers a subjunctive counterexample. In Reunion, (1) "If at least one of them had come, then if Ann had come, Bob would have been there" is judged true and (2) "If Ann had come, Bob would have been there" false. Flattening's rule form equates the two. Avoidance agrees with Reunion on every unnested counterfactual but makes (1) false. On the essay's account this isolates a "scenario-relative" reading: the inner supposition follows the dependencies of the scenario the outer antecedent selects. Buttons (a Locality principle) and Theorem 1 (ties) extend the case. Conclusion: either Flattening fails for subjunctives or the context shifts. If it fails, D&M's argument against IE carries over to Flattening.

## Verdict
Prize: not finalist
Journal recommendation: reject. A much shorter note, rebuilt on the Reciprocity reformulation given under "Proof check", could be viable at a specialist venue.

## Scores
Clarity: 6 | Argument: 4 | Significance: 4 | Originality: 5 | Literature: 5 | Accuracy: 6 | OVERALL: 5

## The single most serious problem

**Location:** §3, premise (P2), together with the "control" paragraph and §5.3.

**Problem (the fatal flaw).** The whole natural-language case rests on one judgment: that (1) is true in Reunion. The essay gives no support for it beyond the author's intuition ("The judgments are mine"). Worse, none of the field's leading treatments of the sentence's own antecedent delivers it.

(a) **Alternatives.** "At least one of them" raises alternatives, as the essay concedes in §5.3. Alternative-sensitive selection semantics (Santorio 2018; Ciardelli, Zhang & Champollion 2018) and the standard interventionist logic (Briggs 2012, Axiom 9) read it universally. The universal reading makes (1) false in Reunion, which the essay itself grants in §3 ("on the universal reading … (1) is false in both").

(b) **Simplification.** Simplification of Disjunctive Antecedents (SDA) plus Contraction, which is a theorem of C2, takes you from (1) to A > (A > B) and then to (2). So a hearer who has the robust SDA intuition and accepts (1) is pushed to accept (2), which everyone rejects. The Reunion verdict is unstable under the most entrenched inference pattern for disjunctive counterfactuals, and the essay never confronts this. Its reply in §5.3, that "the control is neutral … because whatever alternatives 'at least one of them' raises, it raises them in both cases", answers a different question.

(c) **The control.** The control rules out only readings applied uniformly across both cases. Suppose instead that context resolves the inner antecedent differently in each case: "Ann came too" (A∧B) in Reunion, plain A in Avoidance. That reproduces (P1) and (P2) exactly, and every reading involved obeys Flattening. It is the same kind of re-indexing D&M already use for their tense and anaphora pairs. The essay's own justifications slide into this construal: "Ann's turning up *as well* would have changed nothing for him"; "Bob's babysitter would *still* have cancelled". Its §5.1 discourse test is also predicted to come out coherent on the enrichment view.

**Why it matters.** The outer step, "had at least one come, it would have been Bob", is a selection by closeness. It is just as much a matter of "doggedly holding in mind" a selection as D&M's 11-inch line example. So increment (i), "a counterexample of a different kind", only half holds: the case makes the inner step more natural, not the outer one.

What survives is the conditional in §8: if counterfactuals use world-relative selection that tracks each scenario's own dependencies, Flattening fails. That is close to what D&M already grant. They note that similarity orderings, unconstrained order semantics and their own tree models are all non-flat (pp. 19, 27, 46). The formal results are correct but too slight to carry an essay on their own.

## Major problems

1. **§3, the Avoidance vignette: a load-bearing stipulation is missing.**
   - **Problem.** The case says Bob would have stayed home had Ann's name been on the list. It never says that Ann's coming would have put her name on the list.
   - **Why it matters.** Evaluate "Ann came" from the Bob-world without backtracking, as the essay's own Locality and interventionist motivations favour. The posted list then stays as it was. Ann turns up unannounced, Bob is there, (1) comes out true in Avoidance, and the contrast disappears.
   - **Fix.** Stipulate that attendance required registration, that registrants were listed, and that the list was posted after registration closed. Then say explicitly that the Avoidance verdict depends on that causal route.

2. **§5.2, last paragraph (causal modelling): misdescribed, and the standard theory cuts the other way.**
   - **Attribution.** The essay credits nested-counterfactual evaluation to Galles & Pearl 1998 and Halpern 2000. To my knowledge (about 70%) Halpern's language has no nested counterfactuals. Briggs 2012 is the work that extends interventionist semantics to right-nested counterfactuals and disjunctive antecedents.
   - **What Briggs's logic says.** Her Axiom 9 (disjunctive antecedents) and Axiom 11 (right-nesting) give (A∨B) □→ (A □→ B) ↔ (A □→ B), i.e. (1) ↔ (2). So the standard causal-model semantics sides with Flattening on this very instance.
   - **Direct intervention.** Suppose the outer antecedent is realized by intervening on Bob's variable directly, do(B=1). Then do(A=1) cannot change B, so (1) is true in Avoidance as well.
   - **The hidden commitment.** The essay's verdicts need the outer antecedent realized upstream, by setting the babysitter variable. That is a further, non-standard commitment, closer to Hiddleston (2005) or Lucas & Kemp (2015) than to Galles–Pearl.
   - **Why it matters.** "The same cost appears in causal modelling … Flatness requires the opposite verdict" presents causal modelling as independent support. It is not.
   - **Fix.** Rewrite the paragraph as set out in Top change 3.

3. **§4 and §5.2 (Buttons and Locality): they beg the question against the sequence theorist.**
   - **Problem.** The argument applies Locality "to the Ann-pressed scenario taken as actual" and requires the same verdict when that scenario is "reached by supposition". That assumes conditional facts supervene on the scenario's categorical facts. This supervenience is exactly what the sequence picture rejects (D&M p. 13; Khoo 2022).
   - **Mislabelled cost.** The essay concedes "I do not claim to refute the view". But calling the result "a counterfactual connection between spacelike-separated events" mislabels the commitment. The sequence theorist asserts no influence, only an ordering relative to the supposition.
   - **Shaky premise.** "Ann needed only a smaller departure" is doubtful on Lewis 1979, since both presses need small local miracles. Theorem 1 covers the tie, but the falsity of (D) again comes from Locality applied at a supposed scenario.
   - **Fix.** Present Buttons as identifying a cost. Argue for the supervenience premise independently. D&M's tree models (pp. 44–46), in which each scenario carries its own ordering, are a ready formal home for it.

4. **§5.1, §6 and §7: the defender's best resources are missing.**
   - **(a) Kratzer's restrictor analysis.** (1), (2) and every one of D&M's subjunctive test pairs contain a single overt "would". On the restrictor view both if-clauses restrict that one modal, which yields Import-Export and hence (1) ≡ (2). The essay must defend its logical form with two conditional operators. Etlin-style evidence that subjunctive nesting involves two modals is the obvious resource.
   - **(b) Background conditions and embedded context-sensitivity.** Bacon 2015 and Dorr & Hawthorne 2022 develop context-sensitive background conditions. D&M p. 48 (citing Kaufmann 2023) anticipate embedded conditionals being interpreted "differently from the conditional in which they are embedded". This is where the §5.1 context-shift reply actually lives; von Fintel and Roberts are not the right foils.
   - **(c) Mandelkern 2024.** D&M say his error theory of IE "relies, in part, on the validity of Flattening" (p. 22). The §7 call to stop validating Flattening for a unified "if" bears directly on that theory, yet it is not discussed. This is costly before a panel that may include its author.
   - **(d) Reasonable inference.** The §6 explanation of the redundancy datum, "contextual equivalence without logical equivalence", is Stalnaker's (1975) reasonable-inference strategy. Schultheis, "Reasonable Inferences for Counterfactuals", extends it to counterfactual patterns, Simplification among them. The essay should credit this and ask whether a Flattening defender can use the same tool against (1).

5. **§8 and the abstract: the conclusion is hedged into near-triviality.**
   - **Problem.** "If the stable scenario-relative reading is sustained, Flattening cannot be a law of that reading" follows from the definition of the reading. "Context-sensitive and sequence-based replies remain live" leaves no unconditional claim.
   - **Why it matters.** The essay does have something unconditional available: see (R1)–(R3) under "Proof check", which turn the case into a C2.F commitment to an awkward-sounding sentence with no disjunctive antecedent. It does not use it.

## Minor problems
- **Models not shown.** Give all four worlds' orders for Reunion and Avoidance, and the frame behind Observation 2 ("checked over all valuations").
- **Machine-check remarks.** The Z3, "random four-world frames" and "three-world frames" claims are unverifiable and add nothing to proofs that are a few lines long. Cut them.
- **(Flat).** It needs an explicit convention for an undefined f: both undefined counts as equal. That clause is what carries transitivity. The imaging reformulation needs the same convention.
- **Observation 1, wording.** "the copy of w at the head of its own linearization" is wrong as written, since w is not at the head if the worlds outside R(w) are listed first. Drop those worlds. The disjoint union is in fact linear by D&M's Def. 3.8 (≺ may be partial), so "flat" can be "linear".
- **§1 overstatement.** "Similarity semantics cannot validate Flattening" says more than D&M do. They say "clear tension" and "will not work here", and they demonstrate the point only for metrics.
- **§6, conditions (a)–(c).** They are presented as necessary ("robust divergence needs three things") without proof, and (a) as stated is close to vacuous. Call them heuristic.
- **§7, Import-Export.** "A semantics built from successive restriction … validates full Import-Export, which collapses C2 into the material conditional." Restrictor and dynamic semantics validate IE but not C2; the collapse needs C2 + IE. Rephrase.
- **§5.2, Schultheis dating.** "(Schultheis 2023; 2026, 3 n. 4)": D&M's n. 4 lists "Schultheis 2022". It is presumably the same paper; say so.
- **§5.3, Ramotowska et al.** The citation is misapplied; see the next section but one.
- **"Bare" sentences.** The essay advertises that the sentences contain no "still", "even" or "too", yet its own justifications of the verdicts use "still" (for P1) and "as well" (for P2).

## Prior work this resembles (only if confident; author, year, title, confidence %)

- **Dorr & Mandelkern 2026, "Sequence and Consequence".** §4.1 (line example), the p. 27 remark, and the tree models of §7 (pp. 44–46). The essay's case is a dependency-driven instance of the non-flatness D&M already attribute to similarity orderings, and their tree models are a formal version of the scenario-relative reading. (100%; verified in the packet.)
- **Etlin 2008, "Modus Ponens Revisited" (ms., MIT; cited by D&M p. 22).** A subjunctive IE counterexample with the same mechanism: the inner supposition is evaluated from the outer-selected world. The essay's case is in effect a Flattening-form analogue of Etlin's pair, whereas D&M's (11) shows that Etlin's own pair converges again once put in Flattening form. The essay should say so. (95% that the work exists, as cited by D&M; the comparison is mine.)
- **Briggs 2012, "Interventionist Counterfactuals", *Philosophical Studies* 160: 139–166.** Her axioms for disjunctive antecedents and right-nesting validate (1) ↔ (2). (90%.)
- **Kaufmann 2023, "Bernoulli Semantics and Ordinal Semantics for Conditionals", *JPL* 52: 199–220; Kaufmann 2009, "Conditionals Right and Left", *JPL* 38: 1–53.** Prior criticism of what sequence models predict for compound conditionals. (95%; both in D&M's bibliography.)
- **Kratzer 1986, "Conditionals" (CLS 22); Kratzer 2012, *Modals and Conditionals* (OUP).** Restrictor IE for nested if-clauses with a single modal. (90%.)
- **Santorio 2018 and Ciardelli, Zhang & Champollion 2018 (both cited by the essay).** Their alternative-sensitive treatments give the universal reading of the outer antecedent, so (1) comes out false in Reunion. (Works: 90%. That CZC's semantics validates SDA: 75%.)
- **Hiddleston 2005, "A Causal Theory of Counterfactuals", *Noûs* 39: 632–657.** Antecedents realized by upstream "breaks", which is the realization policy §5.2 actually needs. (80%.)
- **Lucas & Kemp 2015, "An Improved Probabilistic Account of Counterfactual Reasoning", *Psychological Review*.** Upstream probabilistic realization of antecedents. (70%.)
- **"An Investigation of Darwiche and Pearl's Postulates for Iterated Belief Update", arXiv:2310.18714 (2023; authors not checked).** Gives a counterexample to the update analogue of C1, which anticipates the §6 point that iteration invariance is unwelcome for update. (Existence: 95%. Content, from the search snippet: 70%.)
- **Stalnaker 1975, "Indicative Conditionals", *Philosophia* 5; Schultheis, "Reasonable Inferences for Counterfactuals" (PhilPapers SCHRIF-3).** The reasonable-inference template. (Stalnaker: 90%. Schultheis, existence and topic: 85%; full text not seen.)
- **Khoo 2017, "Backtracking Counterfactuals Revisited", *Mind* 126.** Bears on the Avoidance route through the guest list. (80%.)

## Claims that look false, misattributed or unverifiable
- **§5.2, causal modelling.** The essay writes: "In a structural-equation model (Galles and Pearl 1998; Halpern 2000), a nested counterfactual … is evaluated by intervening and then intervening again". As far as I know, neither paper's formal language contains nested counterfactuals; the source is Briggs 2012 (about 70%). The follow-on, "The same cost appears in causal modelling … Flatness requires the opposite verdict", is misleading, because Briggs's logic validates (1) ↔ (2).
- **§5.3, Ramotowska et al. 2025.** The essay writes: "Experimental work reports support for selection-based readings". That paper tests the quantificational force of counterfactual modals: universal vs homogeneity vs single-world selection with supervaluation. It is not about selecting one disjunct of a disjunctive or indefinite antecedent. Placed in a paragraph on disjunctive antecedents, the citation implies support it does not give; one of its authors, Santorio, defends selection *with* SDA. (Checked at abstract level; 75%.)
- **§1.** "Similarity semantics cannot validate Flattening" is stronger than D&M's claim.
- **§3.** "The sentences contain no 'still', 'even' or 'too'" is true of the sentences, but the essay's own justifications of the verdicts bring back "still" and "as well".
- **Unverifiable.** All the machine-check claims; the undisplayed four-world models; the Hunter & Delgrande page numbers (273, 297).
- **D&M quotations.** Every quotation and page reference to D&M that I checked against the source is accurate (list below).

## What is genuinely good (be specific: revisions must preserve this)
- **Observation 1 and its moral.** C2.F is conservative over C2 for Boolean combinations of first-degree conditionals, probabilities included. So every argument for or against Flattening must use nested data. This is a useful methodological fixed point, and D&M state nothing equivalent.
- **The design.** Two scenarios agree on every first-degree counterfactual and differ only in one dependency, and a Contraction row is added. That gives a 2×2 test with a clear predicted interaction, which is the right shape for an experiment.
- **Theorem 1.** Either half of Flattening alone, together with CEM, carries the actual world's would-nots into the supposed scenario, and this handles ties. The proof is clean and correct.
- **Observation 2.** Small, but it genuinely goes beyond D&M's p. 29 corollary, because Crashing Cautious Importation is not purely modal. D&M's own non-flat frame in Fig. 2 violates it: 4 <₂ 3 but 3 ∉ R(4).
- **Imaging and belief revision.** The reformulation of Flattening as iteration-invariance of imaging, with the Darwiche–Pearl C1 and revision-versus-update framing, is the most portable idea in the essay. It suggests a principled reason why flatness suits revision-like (indicative) supposition but not update-like (counterfactual) supposition.
- **Scholarship and tone.** The reading of D&M is accurate and fair, and the hedging is honest and well calibrated.

## Literature check

**What I searched (12 web calls, the cap)**

| # | Call | Result |
|---|---|---|
| 1 | Fetch philarchive.org/rec/SCHRIF-3 | HTTP 403 |
| 2 | Search "Schultheis 'Reasonable Inferences for Counterfactuals'" | No direct hit. Surfaced Boylan & Schultheis 2025, "Strengthening Principles and Counterfactual Semantics" (Amsterdam Colloquium); title only. |
| 3 | Fetch philpapers.org/rec/SCHRIF-3 | HTTP 403 |
| 4 | Extended search | Found the PhilPapers record summary (details below). |
| 5 | Fetch philarchive.org/archive/SCHRIF-3 | HTTP 403; full text not seen. |
| 6 | Search for replies to D&M on Flattening / C2.F | None found. Dorr's homepage, per the search summary, lists the paper in *Philosophical Logic* 1.1 (2026), consistent with the essay's reference. DOI not verified. |
| 7 | Search Briggs 2012 | Confirmed *Phil. Studies* 160(1): 139–166. Modus ponens is invalid; classical equivalents are not freely substitutable in antecedents; there are axioms for disjunctive antecedents and right-nesting. |
| 8 | Search Ramotowska et al. 2025 | Confirmed *Semantics & Pragmatics* 18, art. 6, doi 10.3765/sp.18.6. Topic: quantificational force (universal / homogeneity / selection with supervaluation); results favour selection. Also found Romoli, Santorio & Wittenberg 2019, "Fixing de Morgan's Laws in Counterfactuals", a reply to CZC. |
| 9 | Fetch the SEP "Causal Models" axiomatization supplement | Briggs's axioms, quoted below. |
| 10 | Search Khoo 2022 | A unified "inferential dispositions" semantics; Part III treats subjunctive vs indicative. Not confirmed whether it discusses Flattening. |
| 11 | Search Stalnaker 2009 / Darwiche–Pearl C1 | Found arXiv:2310.18714 (counterexample to the update analogue C1▽). Stalnaker 2009's counterexamples are reported as aimed at iterated-revision postulates labelled I1/I2; not confirmed whether C1 is among them. |
| 12 | Fetch the Springer page for CZC 2018 | Redirected to authentication; not fetched. |

**Schultheis, "Reasonable Inferences for Counterfactuals" (from the PhilPapers summary).** It treats Transitivity, Simplification, Contraposition and Antecedent Strengthening. It explains their appeal for variably strict theorists as reasonable inferences in Stalnaker's (1975) sense. Nothing in the record indicates that it treats nested counterfactuals, Flattening or sequence semantics.

**Briggs's axioms (SEP supplement, quoted).**
- Axiom 9: ((A∨B) □→ φ) ≡ ((A □→ φ) ∧ (B □→ φ) ∧ ((A∧B) □→ φ)).
- Axiom 10: substitution of *exact*, not logical, equivalents.
- Axiom 11: ((A∧B∧C) □→ D) ≡ ((A∧B′) □→ ((B∧C) □→ D)), for conjunctions of settings that mention no common variables, where B and B′ mention the same variables.

**Do the named works already contain the essay's case, or answer it?**
- **Schultheis, "Reasonable Inferences".** No evidence that it contains the case. It supplies the template both for the essay's own redundancy explanation and for a defender's pragmatic reply, and it bears on Simplification. Partially relevant; full text unseen.
- **Ciardelli, Zhang & Champollion 2018.** As far as I know it does not contain the case. Its SDA-validating semantics answers it, in the sense of predicting (1) false in Reunion. The two-switch data concern substitution of equivalents in antecedents, not nesting. (75%; the page was not fetched.)
- **Santorio 2018.** Same position. Alternative-sensitive selection gives the universal reading: even on a non-flat ordering, (1) is false in both Reunion and Avoidance, so there is no contrast. This answers (P2), not Flattening as such.
- **Khoo 2022.** D&M (p. 3 n. 4, p. 40) classify it as a sequence/list semantics, which validates Flattening. If its unified treatment covers subjunctives, the essay's case is a direct counterexample to it, yet the essay cites Khoo only for the metaphysical gloss. Khoo would answer as the §5.2 sequence theorist does, by denying that conditional facts supervene on categorical facts.
- **Kratzer's restrictor view.** Does not contain the case, but answers it: with one modal, restrictor IE makes (1) ≡ (2). The burden then falls on the essay's two-operator logical form, and Etlin-style data are its best resource.
- **Briggs 2012.** Does not contain the case, but answers it: her logic proves (1) ↔ (2) via Axioms 9 and 11. This contradicts the essay's suggestion that causal modelling supports the scenario-relative verdict.

**Quotations and attributions checked against source_main.txt (all confirmed)**
- "doggedly holding in mind the Lewisian interpretation" (pp. 19–20)
- "the first antecedent feels like it's doing nothing" (p. 20)
- "We have checked many instances of Flattening, in both the indicative and subjunctive mood, and have not found clear counterexamples." (p. 20, verbatim)
- The tense/anaphora pairs and the Contraction parity (pp. 20–21), as paraphrase
- The IE collapse result (p. 21)
- "But matters are different for Flattening, which appears valid for both indicatives and subjunctives." (p. 22, verbatim)
- "we might naturally regard Flattening as a plausible cautious cousin of the implausible, incautious Import-Export principle" (p. 23)
- "strong prima facie appeal as (at least part of) the logic of the natural language conditional" (p. 24)
- "we leave it as an open problem for proponents of C2.F" (p. 24)
- The rule form (p. 18)
- Crashing Cautious Exportation ≡ 4, and Crashing Cautious Importation ⇒ H (pp. 18–19)
- Lemma 4.2, note 24 and Theorem 4.3 (pp. 25–26)
- Theorem 4.5 and "single master order" (p. 27)
- The metric-space remark (p. 24); D&M state it as a property metric spaces lack
- The Khoo 2022 factual/non-factual gloss, which D&M set aside (p. 13)
- Schultheis in n. 4 (p. 3), though D&M date it 2022
- The C2.F-is-not-C2-plus-modal-principles corollary (p. 29)
- Left-nested conditionals being hard to assess (p. 35)
- n. 36 and the tree models (p. 44)
- Theorems 2.4–2.5

**Other references.** Ramotowska et al. 2025: existence confirmed; characterization disputed (above). The following were not verified online but are plausible from memory: Schultheis 2023 (*JPhil* 120: 581–614); Santorio 2018 pages; CZC 2018 (*L&P* 41: 577–621; the DOI's existence was confirmed in search results); Hunter & Delgrande 2011 page cites; Eva, Shear & Fitelson 2022; Galles & Pearl 1998; Halpern 2000; von Fintel 2001; Roberts 1989; Ellis, Jackson & Pargetter 1977; Fine 2012 (*JPhil*); Lewis 1979; Darwiche & Pearl 1997.

## Proof check

**The essay's claims, checked by hand**

1. **(Flat) as a restatement of flatness.** Correct, provided f(x,X) and f(w,X) are either both undefined or both defined and equal; that clause encodes transitivity. I checked both directions against D&M's definition of semi-flatness (p. 25).
2. **Observation 1.** Correct and near-trivial; the construction works. Wording fixes as listed under "Minor problems".
3. **§3 verdicts in models.** I reconstructed the models:
   - actual world w0: w0 < wB < wA < wAB, in both cases;
   - Reunion, at wB: wB < wAB < wA (non-flat);
   - Avoidance, at wB: wB < wA < wAB (consistent with flatness).

   Results: (1) is true in Reunion and false in Avoidance; (2) is false in both; Flattening fails at w0 in Reunion. The alternative readings come out exclusive F/F, additive T/T, and universal F/F (the last via Contraction, a C2 theorem). All correct. The Avoidance verdict needs the stipulation in Major 1.
4. **"Given CEM, a proponent of C2.F must hold (A∨B) > (A > ¬B) in Reunion."** Correct. The Contraction-row prediction is also correct.
5. **Theorem 1, both halves.** Correct.
   - Exportation half: CEM plus the rule form give X > (A > ¬B) and X > (B > ¬A), and Normality with X > (A∨B) yields (D).
   - Importation half: the contrapositive of the rule instance gives ¬(X > (A > B)); CEM gives X > ¬(A > B); Normality with CEM gives X > (A > ¬B).
   - Each half's rule form is available on its own via substitution of logical equivalents in C2. The premise X > (A∨B) is trivial for X = A∨B.
   - (D) is false at either possible selection under Locality, and true in Avoidance. Correct. The Z3 check is superfluous.
6. **Observation 2.** Correct. In a frame where every world accesses every world, Crashing Cautious Exportation (≡ 4) and Crashing Cautious Importation (x <_w y ⇒ y ∈ R(x); D&M n. 24) both hold. Any non-flat frame of that kind, Reunion's included, refutes Flattening (Theorem 4.3). It is not implied by D&M's p. 29 corollary (see "What is genuinely good").
7. **Imaging reformulation.** Correct on finite frames under the same undefinedness convention; by linearity, point masses suffice.
8. **"In flat frames, two worlds that both reach v order alike every pair that both place after v."** Correct; it follows from semi-flatness.
9. **§6 interventionist remark.** Correct. Briggs's Axiom 11 is the general form.

**Results the essay misses that would strengthen it**

- **(R1)** In C2, (A∨B) > B ⊢ [(A∨B) > φ ↔ B > φ], by Reciprocity with the theorem B > (A∨B). So, given the essay's own selection premise, (1) is C2-equivalent to "If Bob had come, then if Ann had come, Bob would have been there".
- **(R2)** C2.F ⊢ [(A∨B) > B ∧ (A > ¬B)] → B > (A > ¬B). So in Reunion C2.F commits to "If Bob had come, then if Ann had come, Bob would not have been there". That sentence is not an instance of Flattening and has no disjunctive antecedent, so the SDA and alternatives objections drop away.
- **(R3)** The Buttons analogue: C2.F ⊢ [(A∨B) > A ∧ (B > ¬A)] → A > (B > ¬A), i.e. "If Ann had pressed, then if Bob had pressed, Ann would not have pressed".

**Results that cut against the essay**

- SDA plus Contraction give (1) ⊢ (2).
- Briggs's Axioms 9 and 11 give (1) ↔ (2).

## Top five changes

1. **Rebuild §3 around (R1)–(R3).**
   - State as a proposition that, given first-degree premises both sides accept, C2.F entails "If Bob had come, then if Ann had come, Bob would not have been there" (Reunion) and "If Ann had pressed, then if Bob had pressed, Ann would not have pressed" (Buttons).
   - Keep (1)–(2) as the bare Flattening instance, but make (R2)/(R3) the headline cost.
   - Say explicitly that the only remaining Flattening-friendly exits are to deny the selection premise or to reinterpret the inner antecedent.

2. **Face the too/instead problem and SDA head-on, in a dedicated subsection.**
   - (a) Show that SDA plus Contraction take (1) to (2). Either explain why the outer antecedent is not simplified here, or rest the argument on (R2)/(R3), which avoid the issue.
   - (b) Concede that case-dependent enrichment of the inner antecedent is extensionally equivalent to the scenario-relative reading. Then argue on architectural grounds: the enrichment would have to recompute the selection function at the selected world v.
   - (c) Supply embedding diagnostics that could separate the two: negation, questions, quantifier restrictors, attitude reports. Add overt "too" and "instead" variants to the 2×2 design.
   - (d) Fix the Avoidance stipulation: registration implies being on the list.

3. **Rewrite the causal-modelling paragraph of §5.2.**
   - Cite Briggs 2012 and report that her logic validates (1) ↔ (2).
   - Show that direct do(B=1) makes (1) true in Avoidance.
   - State the upstream-realization policy the verdicts require, and cite Hiddleston 2005 and Lucas & Kemp 2015.
   - Drop the Galles–Pearl/Halpern attribution for nested counterfactuals, or verify it.
   - Correct the sentence citing Ramotowska et al.

4. **Engage the defender's literature in §5.1, §6 and §7.**
   - Kratzer's restrictor analysis (one "would"), and why (1) contains two conditional operators. Cite Etlin 2008 via D&M p. 22.
   - Bacon 2015 and Dorr & Hawthorne 2022 on background conditions; D&M p. 48 with Kaufmann 2023 on embedded context-sensitivity.
   - Mandelkern 2024's IE error theory, which depends on Flattening: does it need Flattening only for indicatives?
   - Stalnaker 1975 and Schultheis on reasonable inference, both as the basis of the essay's redundancy explanation and as a tool against it.
   - D&M's tree models, as a ready non-flat semantics in which scenarios have independent orderings.

5. **Display the models and restate the result.**
   - Give a table of every world's order for Reunion, Avoidance and Buttons, and the Observation 2 frame.
   - Add the undefinedness convention to (Flat) and to the imaging claim. Delete the Z3 and "random frames" remarks.
   - Rewrite the abstract and §8 to separate what is proved (Observation 1, Theorem 1, (R1)–(R3), Observation 2, the imaging/Darwiche–Pearl link) from what is conjectural (the reading of the bare sentence).
   - Specify the 2×2 study, with its variants and predicted interactions, or report a small pilot.
   - Shorten §6's cautious-cousin and cumulativity material to make room.
