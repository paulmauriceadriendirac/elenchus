# E3 revision notes, v2 → v3 (response to referee S5, packet P-c865)

Source for every D&M check: inbox/sources/dorr-mandelkern-2026-sequence.txt (arXiv 2411.16994v2). Page numbers are that PDF's printed pages.

## 1. Verification of the referee's factual claims about D&M

| Referee claim | Verdict | Where |
|---|---|---|
| D&M's redundancy argument ("the first antecedent feels like it's doing nothing") was omitted | Correct | p. 20 |
| D&M's "cautious cousin" analogy with Cautious Monotonicity/Transitivity was not answered | Correct | p. 23 |
| Felt inequivalences from re-indexing (tense, anaphora) are set aside, with a Contraction parity | Correct | pp. 20–21, ex. (6)–(8) |
| Crashing Cautious Exportation ≡ 4 in C2; Crashing Cautious Importation yields H; each half is weaker | Correct | p. 18 |
| The factual/non-factual gloss is credited to Khoo 2022 | Correct ("see Khoo 2022 for a recent picture along these lines") | p. 13 |
| Schultheis 2022 is listed among sequence-semantics works | Correct | p. 3 n. 4 |
| The IE error theory relying on Flattening is Mandelkern 2024 | Correct | p. 22 |
| "Single master order" / "clearest semantic picture" | Correct | p. 27 |
| C2.F is not C2 plus modal principles | Correct | p. 29 |
| The left-nesting remark concerns Sequentiality, not 4/H | Correct | p. 35 |
| Tree models: (B>L>\|B)-Stalnaker, and Boolean Flattening instances can have probability < 1 | Correct | Thm 7.6 (p. 45); n. 36 (p. 44) |
| D&M state (Flat) for metrics | Correct | p. 24 |
| Line example diverges without condition (b) | Correct (the 11-inch realization is not kept by the inner supposition) | p. 19 |
| Conflagration pair (2) is indicative | Correct | p. 20 |

I found no false factual claim about the source in the report.

## 2. Triage

| Item | Verdict | Reason / action |
|---|---|---|
| **Central problem**: no divergence under one fixed interpretation; reliance on enriched nested judgments (still/even, modal subordination); exclusive reading of the bare pair | **Fixable, addressed** | Rebuilt §3 on a bare rule-form instance, (1) "If at least one of them had come, then if Ann had come, Bob would have been there" vs (2) "If Ann had come, Bob would have been there", with no particles. "At least one" is truth-conditionally the inclusive disjunction. The key new move is a **cross-case control**. Reunion and Avoidance agree on every unnested counterfactual about A, B (K10). (2) is false in both, and (1) is judged true in the Reunion and false in Avoidance. Every construal of the inner antecedent that entails the outer one (exclusive A¬B, additive AB, any X ⊆ A∨B) reduces under Flattening to an unnested counterfactual that is identical across the cases. Without Flattening, the exclusive, additive and universal readings also give no contrast (K10). So the contrast can come only from the selectional, scenario-relative reading, on which Flattening fails. Fixed interpretation: §5.1 dilemma (below). Observation 1 shows that the demand to avoid nested judgments *altogether* cannot be met by either side, so v3 meets the right demand: bare, not enriched. |
| Major 1: §5.2 context shift begs the question | **Fixable, addressed** | New §5.1 dilemma. (i) A persistent shift (von Fintel 2001: the horizon is passed on, widening is silent, narrowing needs explicit indication; read in open-access copy) would make (2) true after (1). But "(1). But if Ann had come, he would not have been there" is coherent, though it is a contradiction under a fixed Flattening interpretation. The needed shift is also a narrowing. (ii) A local shift must track Bob's attitude, which has no linguistic trigger. So it *is* the scenario-relative interpretation, and then every nested left member, D&M's included, receives it, which leaves Flattening with no natural-language instances. D&M's re-indexing cases are form-driven, so they would not vary across the two cases. A Contraction row is added to the proposed test design. I did not adopt the referee's "too" suggestion: "too" plausibly imports B (the additive construal), and K10 shows that construal predicts no contrast. Gillies 2007 and Moss 2012 were not read, so they are not cited. |
| Major 2: §5.1 sequence theorist (index claim, Independence overstated, interventionism gestured) | **Fixable, addressed** | Dropped "index contains exactly what the scenario contains" and Independence. New Locality principle, restricted to deterministic laws with no superluminal influence, which the asymmetric Buttons pair (3)/(4) rests on (K5). The argument now says what the sequence theorist must deny: the contrast, or Locality at reached scenarios while accepting it at worlds taken as actual (route-relativity). The causal-model point is now an argument: once the disjunctive antecedent is realized by an intervention, the resulting model fixes the inner verdict, whatever route led to it (K12). Khoo 2022 is cited for what D&M credit to it. Schultheis is cited only as D&M list it (could not retrieve the text). The essay explicitly does not claim to refute the view. |
| Major 3: §6 positive story validates full IE; Thesis does not deliver Flattening | **Referee right; claim withdrawn** | §7 now states that restriction and conditioning validate full IE, so they cannot answer D&M's open problem, and that no answer is supplied. It reports D&M's n. 36 and tree models accurately. New positive point that does not overreach: the indicative version of the pair does not split, because indicative supposition does not select a realization (condition (b) fails). This is neutral on Flattening for indicatives. |
| Major 4: contribution claims overstated | **Referee right; fixed** | Theorem 1 is presented as a short CEM-dependent consequence parallel to D&M's derivation of H. Its premises are "ordinary would-nots", and its use requires the nested judgment that (D) is false. "Needs neither nested", "purely negative" and "no better without CEM" are removed. (Flat) is credited as D&M's condition restated. Imaging iteration invariance is labelled "a reformulation". Agreement is called "an immediate consequence of flatness" tied to D&M's master order. The increment is stated as (i)–(iv) in §1. |
| Major 5: "cumulativity" clash; cautious cousin | **Referee right; fixed** | Renamed to "iteration invariance". The KLM sense is noted impersonally as a different property that C2 already has. Linked to Darwiche–Pearl's first postulate (as stated in Hunter & Delgrande 2011, p. 297) and to revision vs update (H&D 2011, p. 273). The cautious-cousin analogy is answered in §6: the cautious principles involve one ranking, Flattening relates two. |
| Minor: "most cautious step" | **False; removed** | Each half and CCE are weaker (p. 18). |
| Minor: "requires" (a)–(c) | **Right; fixed** | Now "robust divergence on dependence-based orderings needs…". Metric divergence without (b) is noted (line example). |
| Minor: mood in §4.3 | **Right; fixed** | The conflagration pair is flagged as indicative and excluded. |
| Minor: computational checks unverifiable | **Fixable** | check.py rewritten and rerun (below). The essay states what was checked in a sentence each. The four-world enumeration is no longer mentioned as evidence. |
| Minor: "counterfactual profile" undefined | **Right; term dropped** | — |
| Minor: "instance" of Agreement | **Right; fixed** | "which they state themselves for metric spaces". |
| Minor: existential antecedents raise alternatives | **Right; conceded** | §5.3: the control is neutral, because the same alternatives are raised in both cases. |
| Minor: Briggs 2012 reads disjunctions universally (65%) | **Unverified; citation dropped** | The claim is no longer needed. The universal reading predicts no contrast (K10). |
| Minor: summary of D&M omits redundancy and cautious cousin | **Right; added** | §1 now has four strands, and both points are answered in §6. |
| Minor: which logic? | **Right; addressed** | Observation 2: C2 + both Crashing principles does not prove Flattening (K11). The cases are consistent with C2 + 4 + H, and this is left open. |
| Minor: "they note such conditionals are hard to assess" | **Right; fixed** | Attributed to the Sequentiality context (p. 35), with the extension to 4/H marked as mine. |
| Top-5 #1 (minimal pairs, exclusive reading, Contraction parity) | Fixable; done | See central problem. |
| Top-5 #2 (premises the sequence theorist accepts; Schultheis, Khoo; causal model) | Fixable; mostly done | Schultheis could not be read (search found no open copy). |
| Top-5 #3 (repair §6) | Done by withdrawal | — |
| Top-5 #4 (recalibrate claims) | Done | — |
| Top-5 #5 (terminology; D&P C1; update/revision; Joyce; Stalnaker 1975; cautious cousin; which logic) | Mostly done | Joyce 1999, Stalnaker 1975, Katsuno & Mendelzon 1991 and KLM 1990 are not cited: I did not read them, and their content was not needed. |

Kept as the referee asked: Reunion, Buttons (now asymmetric for the bare pair, symmetric via Theorem 1), Avoidance (promoted to the core control), the (a)–(c) explanation and interventionist composition, and the unity-of-"if" consequence.

## 3. What changed and why (summary)

- §2: new **Observation 1** (C2.F is conservative over C2 for Boolean combinations of first-degree conditionals, probabilities included; proof by linearization or a disjoint union of linearizations). This reframes the methodological demand: nested judgments are unavoidable on both sides.
- §3: new evidential core (bare pair + cross-case control + regimented argument P1–P3 → C + proposed 2×2 test with a Contraction row). Observation 2 of v2 (the no-CEM argument from (J)) is dropped: the bare instance needs no logic at all.
- §4: Buttons made asymmetric, so it yields its own bare instance backed by a stated Locality principle. Theorem 1 is kept for the symmetric version and honestly framed.
- §5: context-shift dilemma; sequence-theorist section rebuilt; SDA/alternatives section shortened; the Goodsell-based chance section is dropped (the Buttons involve no chance, stated in §4).
- §6: (a)–(c) recalibrated; replies to the redundancy datum and the cautious-cousin analogy; iteration invariance, Darwiche–Pearl, revision vs update.
- §7: which logic (Observation 2), indicatives without overclaiming, D&M's open problem left open, the unity consequence.
- Removed citations: Briggs 2012, Goodsell 2022, Kratzer 2012, McKay & van Inwagen 1977, Lewis 1973 (*Counterfactuals*), Stalnaker 1970 (no longer cited in the text).

## 4. v3 thesis (one sentence)

Two cases that agree on every unnested counterfactual about the relevant events and differ only in counterfactual dependence give a bare nested counterfactual different truth values while its Flattening partner keeps one, so Flattening fails for the counterfactual as English nested counterfactuals are interpreted, and the only interpretation that would save it is one those sentences never receive.

## 5. Exact increment over Dorr & Mandelkern

D&M give one counterfactual counterexample, metric-based, which they find unconvincing (pp. 19–20). They report no clear counterexample in either mood (p. 20), and they exempt Flattening from their argument against Import-Export (p. 22). v3 adds four things. (i) A bare rule-form counterexample in the L_B> fragment, driven by counterfactual independence, with a cross-case control that discriminates the reading carrying the verdict from the exclusive, additive and universal readings. (ii) An argument that a context shift cannot save the principle (persistence/locality dilemma). (iii) An explanation of why their subjunctive pairs pass and why their redundancy datum and cautious-cousin analogy do not discriminate. (iv) The transfer of their Import-Export reasoning to Flattening. Small additions: Observation 1 (conservativity, including probabilities) and Observation 2 (C2 + both Crashing principles does not prove Flattening). The following are reformulations or consequences of their results and are credited as such: (Flat), imaging iteration invariance, Agreement, and Theorem 1's structure.

## 6. Three weakest remaining points

1. **The judgments in (P2), especially the Reunion verdict on bare (1).** Everything rests on them. They are the author's own and untested. A defender may simply report hearing (1) as false in the Reunion. In that case the cross-case contrast disappears and only the Buttons/Locality cost remains. The proposed 2×2 study would settle it, but it has not been run.
2. **The local-shift horn.** A sequence theorist may accept that English nested counterfactuals are interpreted with a scenario-relative "local shift", and hold that "logic" concerns the unshifted conditional. v3 argues that this leaves Flattening with no natural-language instances, D&M's test pairs included. A committed formal semanticist may regard that as an acceptable division of labour, not a cost.
3. **Literature engagement on context shift and sequence semantics is thin.** Only von Fintel 2001 was read. Gillies 2007, Moss 2012, Schultheis (2022/2023) and Khoo 2022 were not read: Khoo is cited only for what D&M credit to him, and Schultheis only as D&M list him. If a published sequence-based counterfactual semantics already addresses nested independence cases, v3 does not engage it.

Also minor: the indicative claim (§7) that the pair does not split rests on a judgment about information-state supposition. And the persistence test assumes that a narrowing shift, if contextual, would persist.

## 7. Checks (check.py; v2 version kept as check_v2.py)

Rerun 2026-10-21: **ALL CHECKS PASSED**.
- K1 (Flat) ⇔ D&M flatness: all 125 three-world and 65,536 four-world frames.
- K2 Flattening valid ⇔ (Flat): all three-world frames and valuations.
- K3 Theorem 1: semi-flat and fn.-24 frames, n ≤ 5 (z3); fails on plain frames.
- K5 Reunion: (1) true, (2) false, (D) false. Avoidance: (1) false, (2) false, (D) true. Symmetric Buttons: both tie-breaks give (D) false. Asymmetric Buttons: (3) true, (4) false.
- K6 Imaging iteration invariance ⇔ (Flat).
- K7 Nine verbatim quotations.
- K8 Agreement on flat frames, n ≤ 5.
- K9 (new) Observation 1: linearization is flat and preserves <_w (all three-world frames, 3,000 random four-world frames). The disjoint union of linearizations is flat and agrees on all first-degree X>Y.
- K10 (new) Cross-case table: identical first-degree profiles; every construal X ⊆ A∨B gives no contrast in the flat versions; inclusive selectional reading [True, False], exclusive [False, False], additive [True, True], universal [False, False].
- K11 (new) Observation 2.
- K12 (new) Structural-equation nested intervention.
- K4 (the v2 triad for Observation 2) is removed with that observation.

## 8. Word count and integrity

tools/wordcount.py: strict 5,477, wordlike 5,425, excluding references (limit 6,000; target 5,600). The abstract is 181 words including the label. tools/check_injection.py: no hard flags. No mention of the author, pipeline, competition or reviewers.

## 9. New references and how each was verified

| Reference | Registry check (verify_refs.py) | Content check |
|---|---|---|
| von Fintel 2001, "Counterfactuals in a Dynamic Context", in *Ken Hale: A Life in Language*, 123–152 | VERIFIED (doi 10.7551/mitpress/4056.003.0006) | Read the open-access PDF from web.mit.edu/fintel (text extracted locally). "Modal horizon" widens gradually (p. 127). It is passed on from one counterfactual to the next (p. 129). Resetting appears to need explicit indications, while expansion is silent (p. 140). |
| Darwiche & Pearl 1997, *AIJ* 89: 1–29 | VERIFIED (doi 10.1016/S0004-3702(96)00038-0) | Publisher page 403. The postulate is cited "as stated by Hunter and Delgrande 2011, 297" (DP1: if α ⊆ β then (κ∗β)∗α = κ∗α), read in the arXiv copy of H&D. |
| Hunter & Delgrande 2011, *JAIR* 40: 269–304 | VERIFIED (doi 10.1613/jair.3132) | Read the arXiv copy (1401.3867): DP postulates p. 297; update "projecting every state s to the state s′ that would result" p. 273. |
| Roberts 1989, *L&P* 12: 683–721 | VERIFIED (doi 10.1007/BF00632602) | Cited only for the term "modal subordination", which is in its title. |
| Khoo 2022, *The Meaning of If* | VERIFIED (doi 10.1093/oso/9780190096700.001.0001) | Not read. Cited only for what D&M (p. 13) credit to it. |
| Schultheis, "Counterfactual Probability", *J. Phil.* 120: 581–614 | VERIFIED as **2023** (doi 10.5840/jphil20231201133). D&M list it as 2022. | Not read (search found no open copy). Cited only as one of the sequence-semantics works D&M list (p. 3 n. 4); its topic is given by its title. |
| Dorr & Mandelkern 2026 journal metadata | VERIFIED via Crossref DOI (Philosophical Logic 1) | — |

Checked but not cited: Lewis 1973 "Causation" (VERIFIED; no longer needed because v3 does not use Lewis's definition) and Mandelkern 2024 (book; registry shows chapter records of *Bounded Meaning*, OUP 2024; not cited in v3).

Retained references (Ciardelli et al. 2018, Ellis et al. 1977, Eva et al. 2022, Fine 2012, Galles & Pearl 1998, Halpern 2000, Lewis 1976, Lewis 1979, Ramotowska et al. 2025, Santorio 2018, Stalnaker 1968, van Fraassen 1976) were verified in earlier rounds. Their attributions are unchanged or narrowed.

Fetch use: 3 fetches (von Fintel PDF; ScienceDirect, which returned 403; Hunter & Delgrande arXiv) and 2 searches.
