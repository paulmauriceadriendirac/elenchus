# E3 revision notes (v1 → v2), against the full text of Dorr & Mandelkern 2026

Source: inbox/sources/dorr-mandelkern-2026-sequence.txt (arXiv 2411.16994v2). Page numbers below are arXiv pages (= printed page numbers in that PDF). v2 cites sections plus arXiv pages and says so in its reference entry.

## 1. Fidelity audit of v1's claims about D&M

| # | v1 claim | Verdict | Where in D&M |
|---|---|---|---|
| 1 | The logic of ω-sequence semantics is C2.FS; that of arbitrary ordinal sequences is C2.F | Accurate | §1 p.4; Thm 5.3–5.4 pp.32–34; Thm 6.2 p.37 |
| 2 | C2.F = C2 + Flattening; C2.FS adds Sequentiality | Accurate | §4 p.16; §5 p.29 |
| 3 | Sequence semantics was developed by van Fraassen in connection with Stalnaker's Thesis | Accurate | §1 pp.2–3 |
| 4 | Flattening is the instance of IE with inner antecedent entailing the outer | Accurate in substance (D&M: "cautious" cousin of IE; rule form) | §4 p.18; §4.1 p.21 |
| 5 | D&M "observe that a similarity-based semantics cannot validate Flattening" | Accurate | §4.1 pp.19, 24 (line example; metric-space remark) |
| 6 | They leave open "for proponents of C2.F to supply an intuitive semantics that does" validate it | Accurate (their wording: "we leave it as an open problem for proponents of C2.F", re. an intuition about the semantics that would explain its validity) | §4.1 p.24 |
| 7 | They note it remains open whether a restricted Stalnaker's Thesis could yield a restricted Flattening | Accurate but incomplete: they also already prove the equiprobability of Flattening's sides in their restricted-Thesis models (fn.36) and say there is no obvious route to probability one | §7 p.44 and fn.36 |
| 8 | D&M find all of C2's principles plausible for natural-language conditionals | Accurate | §1 p.3 |
| 9 | (v1 §6.6) "A reader could have taken C2.F to be a candidate for counterfactuals as well" / "If C2.F was meant for indicatives…" | Inaccurate by understatement: D&M explicitly test subjunctive pairs ((3),(4),(5),(11)), say they found no clear counterexamples "in both the indicative and subjunctive mood", and say Flattening "appears valid for both indicatives and subjunctives" | §4.1 pp.20, 22 |
| 10 | (implicit) D&M's case against Flattening is only the similarity point | Inaccurate/incomplete: their main reservation is that Flattening entails 4 and H for the defined □, contested for epistemic, nomic and metaphysical readings | §4.1 pp.23–24 |
| 11 | Selection semantics: "C2 is the logic of these models", with Success relative to all non-empty X (no accessibility) | Inaccurate: with universal accessibility the □-fragment is S5, but C2's modal fragment is KT (D&M Thm 2.6). D&M's order frames have R(w). v1's Observation 1 and Theorem 1 survive once restated on D&M's frames | §2.1 pp.6–8; Thm 2.6 p.9 |
| 12 | v1 Observation 1 ((Flat) characterizes Flattening) as if new | Unsupported as novelty: it is D&M Thm 4.3 (flatness) in selection form; their metric remark (p.24) states the condition for metrics | Thm 4.3 p.26; p.24 |
| 13 | v1 Prop 4 / "(RS) is restricted Factorization, escapes Lewis, holds in van Fraassen models" | Anticipated: D&M's (P>Q\|R)-Stalnaker definition requires π(r\|p)=1 exactly to escape Lewis (fn.33), Thm 7.3 shows sequence models satisfy it, fn.36 derives equal probability of Flattening's sides | §7 pp.42–44 |
| 14 | Remark that D&M intend logics for indicatives only/for both | They intend C2.F as a candidate for "the natural language conditional" in both moods; they introduce Stalnaker 1970 on the indicative interpretation (p.2), but §4.1 evaluates both moods | pp.2, 20, 22, 24, 48 |

## 2. Prior-art check (adversarial)

- **Counterfactual counterexample to Flattening already in D&M?** Partly. They give one, the line example (1), counterfactual and built on Lewis's similarity metric, and judge it unconvincing (pp.19–20). They mention no case based on counterfactual independence, nothing in the Boolean-antecedent right-nested fragment, and no derivation of a dependence claim. The Reunion/Buttons are new relative to the paper. v2 also explains why their line example is weak (it fails condition (b) of §4.3).
- **Structure of Theorem 1.** Its derivation parallels D&M's derivation of H from Crashing Cautious Importation via the disjunction (pp.18–19). v2 credits this. The differences: the result is in the conditional (Boolean-antecedent) fragment, not the modal fragment, and either half of Flattening suffices.
- **Imaging/cumulativity characterization.** Not in D&M. They do not discuss imaging. The selection condition (Flat) is their flatness (Thm 4.3) in another form, and their metric remark states it for metrics. v2 presents (Flat) as a reformulation and Proposition 3 (imaging cumulative ⇔ Flattening) as a modest addition. The Agreement corollary is an immediate consequence of their semi-flatness. It is not stated in D&M, though it connects to their linear-frame (master order) completeness and their "one grand ordering" picture.
- **CK result (Prop 2).** D&M name the halves Cautious Importation/Exportation and give countermodels (Fig. 1) but no CK-level argument. v2 keeps this as Observation 2, now explicitly no-CEM.
- **"Flattening is cumulative supposition".** Not in D&M as such. Closest: linear frames ("single master order", pp.27–28) and the metric remark.
- **Restricted Factorization under Stalnaker's Thesis.** Fully anticipated (fn.33, fn.36, Thm 7.3, 7.7). Removed from v2 as a contribution and cited as theirs.
- **Do D&M restrict C2.F to indicatives (deflating v1 §6.6)?** No, the opposite. They claim it appears valid for both moods and use that to distinguish it from IE in the unified-"if" argument (p.22). This makes v2's thesis a direct challenge to a claim in print and gives it a new consequence (§6 of v2).
- **Correctness relative to their exact definitions.** Re-verified on D&M order frames with accessibility (check.py). Theorem 1 holds in C2 + Cautious Importation and in C2 + Cautious Exportation (syntactic proofs in v2; z3 on semi-flat and fn.24 frames, n ≤ 5). v1's universal-selection framing was wrong and has been removed. The triad (N, J, Poss) is inconsistent with Cautious Importation alone; with Cautious Exportation alone it needs the extra premise (A∨B)>◇A (z3 shows sat without it). v2 states this.

## 3. What changed and why

- Framework restated in D&M's order frames (R(w), well-orders, vacuous case). v1's universal-selection semantics removed (error 11).
- D&M represented accurately: their three-part case for Flattening (similarity, test pairs in both moods, IE contrast and the unified "if"), their 4/H reservation, their open problem, and their fn.36 result, with 5 verbatim quotations checked by script.
- Theorem 1 strengthened: either half suffices (given CEM); generalized to any outer antecedent X entailed by A and B with X>(A∨B), which handles existential antecedents.
- New control case (Avoidance), computed: the verdict on (D) flips with dependence. This answers the "it's just an IE intuition" reply.
- New diagnosis section: Proposition 3 (cumulativity), Agreement corollary, and conditions (a)–(c) explaining why D&M's test pairs pass and why their line example felt weak; interventionist composition fact.
- Main objection now the sequence theorist's path-dependence reply (§5.1), answered by an Independence principle, the cost of route-relative dependence, the Buttons, and parity of nested judgments. Context-shift reply added (§5.2).
- Removed: v1 §5 Prop 4 (anticipated), v1 §6.3 ("embedded counterfactuals evaluated from actuality"; it attacked a view nobody in this dialectic holds), v1 §6.6 (premise false). Removed citations whose attributions I could not check against text: Mandelkern 2020, 2021; Khoo & Mandelkern 2019; Cariani & Goldstein 2020; Égré & Rott 2021; Starr & Kocurek 2025 (section-specific claims).
- New consequence (§6): by D&M's own reasoning about IE and the unity of "if", Flattening should not be part of the logic of "if" if it fails for subjunctives.

## 4. v2 thesis (one sentence)

Flattening is invalid for counterfactual conditionals, because it requires the scenario reached by a counterfactual supposition to inherit its counterfactual profile from the world at which the supposition is made, while counterfactual independence is a feature of the scenario itself.

## 5. Exact increment over Dorr & Mandelkern

D&M report no clear counterexamples to Flattening in either mood, find their only (similarity-based) counterfactual counterexample unconvincing, and argue that Flattening, unlike IE, is a candidate for the logic of a unified "if". v2 contributes the following. (1) A counterexample for counterfactuals in the right-nested, Boolean-antecedent fragment, with no similarity metric, driven by counterfactual independence, with a control case showing that the verdict tracks dependence. (2) A theorem: in C2 plus either half of Flattening, ¬(A>B), ¬(B>A), X>(A∨B) ⊢ X>[(A∧(B>¬A))∨(B∧(A>¬B))]. A no-CEM version refutes each half in any normal conditional logic. (3) A diagnosis: Flattening ⇔ cumulative imaging, plus the Agreement corollary. Conditions (a)–(c) explain why their test pairs and their line example behave as they do. This turns their open problem into the requirement of cumulative supposition, which an information-relative (indicative) reading meets and a world-relative (counterfactual) reading does not. (4) The consequence for their unified-"if" argument.

## 6. Three weakest remaining points

1. **Path-dependence reply (§5.1).** A committed sequence theorist can accept route-relative counterfactual dependence and deny Independence at indices reached by supposition. v2's reply makes this costly through causation, interventionism and the Buttons, but it does not refute it. A referee may say that the argument assumes a factualist picture of counterfactuals.
2. **Novelty of the formal part.** Theorem 1 mirrors D&M's derivation of H, (Flat) is their flatness, and Proposition 3 and Agreement are short. Most of the value lies in the cases and the diagnosis, so a logic referee may rate the formal increment as small.
3. **Indicative discussion (§6).** The claim that the indicative counterpart of (D) is governed by IE-type intuitions, and so gives no independent evidence, rests on my judgment about the indicative Avoidance variant and was not tested further. A referee could argue that the indicative case also embarrasses C2.F, which would widen the thesis but undercut the clean mood split. The "information state behaves like a tail" analogy is suggestive, not proved.

Minor: the existential version of the outer antecedent needs ⊢ A → X, which holds only given that Ann's membership in the year is fixed. Interventionist claims are limited to the composition of interventions on conjunctive settings.

## 7. Checks and word count

check.py (z3 + exact rationals + quotation check): K1 (Flat)⇔D&M-flat on all 125 three-world and 65,536 four-world order frames; K2 Flattening valid ⇔ (Flat) (3 worlds, all valuations); K3 Theorem 1 valid on semi-flat (CI) and fn.24 (CE) frames n ≤ 5, both X = A∨B and general X, fails on plain frames; K4 triad results as above; K5 Reunion, Avoidance and Buttons (both tie-breaks) verdicts; K6 imaging cumulativity ⇔ (Flat) (3 worlds); K7 nine verbatim quotations; K8 Agreement on flat frames n ≤ 5. All pass.

Word count (tools/wordcount.py): strict 5548, wordlike 5447, excluding references. check_injection: no hard flags.
