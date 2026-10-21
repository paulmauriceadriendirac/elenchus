# E1 revision notes (v1 -> v2), written against the full text of Goodman & Salow 2023

Source: inbox/sources/goodman-salow-2023.txt (+ PDF, figures 4 and 5 rendered and inspected).
Page numbers are journal pages (PDF page + 88).

## 1. Fidelity audit of v1's claims about Goodman & Salow (G&S) 2023

| # | v1 claim | Verdict | Evidence |
|---|---|---|---|
| 1 | Quotation: "if a possibility is sufficiently less normal than one's actual situation, then one can know that that possibility does not obtain" (attributed to G&S 2023) | **Unsupported**: not in the article text. The closest wording is p. 90 ("If such a situation is sufficiently less normal than the one Bjorn is actually in, then he knows that he is not in that situation"). Possibly from an online abstract; not checkable here. Dropped. | grep of full text |
| 2 | Quotation: adjudication turns on "whether a reasonably constrained account of the needed context-sensitivity can be given" (§5) | **Accurate**, verbatim, p. 117 | p. 117 |
| 3 | G&S present single-scale (probabilist) vs multi-dimensional normality as rivals and leave adjudication to further work | **Accurate**, pp. 117, 123 ("We have no settled view…") | pp. 117, 123 |
| 4 | Two relations: ⪰ a preorder; ≫ with (S1) ≫ implies ≻, (S2) z≫u, u⪰v ⇒ z≫v, "in the spirit of" G&S 2021 | **Partly inaccurate / incomplete.** Official constraints (p. 92): (i) ⪰ reflexive, transitive; (ii) ≫ irreflexive and implies ⪰; (iii) two-sided chaining w1⪰w2≫w3⪰w4 ⇒ w1≫w4. (S1) and (S2) follow from (i)–(iii) but omit left-chaining and irreflexivity; v1 attributed the chaining to 2021 instead of stating the official 2023 principle. G&S 2023 drop well-foundedness (n. 4). | p. 92, n. 4 |
| 5 | Definitions of i- and k-normality | **Accurate** (pp. 104–105, 109–110). v1 omitted that I-NORMALITY is taken from Goldstein & Hawthorne 2022a (p. 105) | pp. 104–105 |
| 6 | k-normality is "the form of the KK-validating model of G&S 2018" | **Accurate** (p. 104: "from Goodman and Salow (2018)"; p. 107: K entails KK given TRANSPARENCY) | pp. 104, 107 |
| 7 | km-normality "adds margins"; definition not given | **Accurate but incomplete**; the full definition is pp. 108–110; G&S also characterize the completions by ignorance/knowledge defaults (p. 110) | pp. 108–110 |
| 8 | Under comparability km coincides with i | **Accurate**, p. 111 | p. 111 |
| 9 | Comparability defined as all pairs in E comparable | **Accurate** (COMPARABILITY, p. 101, for evidentially accessible pairs) | p. 101 |
| 10 | Comparability holds in the probabilist development because probabilities are totally ordered; normality = probability of answers to a contextual question | **Accurate**, pp. 120–121 | pp. 120–121 |
| 11 | v1 says G&S "leave open" comparability, implying no argument from independent sources | **Misleading by omission.** G&S give exactly v1's argument (scale + thermometer, independent malfunctions, mutual inaccessibility of single-malfunction situations, incompatible with COMPARABILITY), pp. 117–118; and state the totality consequence, p. 107 | pp. 107, 117–118 |
| 12 | Multi-dimensional normality; k-normality without comparability handles crossed exclusion | **Accurate but already G&S's**: multi-dimensional definitions p. 118; both K and KM give crossed exclusion, p. 118, fig. 4 | p. 118–119 |
| 13 | km-normality without comparability "untested" | **Inaccurate**: G&S's figure 4 depicts KM accessibility in the 3×3 model, and p. 118 states KM gives the independence | pp. 118–119 |
| 14 | i-normality fails under any ordering (v1's increment) | **Anticipated**: G&S, p. 119 (I-NORMALITY without COMPARABILITY: "any abnormality along one dimension makes inductive knowledge impossible along any orthogonal dimension"); p. 111 (I untenable without COMPARABILITY) | pp. 111, 119 |
| 15 | Repeated weighing: two readings of one quantity; "a sufficiently discrepant second reading can defeat knowledge from the first" | **Partly accurate**: two scales, different manufacturers (pp. 125–127). Defeat is predicted by K-NORMALITY only (|x−y| > (2−√2)c); given MARGINS (with COMPARABILITY, STATISM) there is no defeat (pp. 127–128) | pp. 125–128 |
| 16 | Contextual (probabilist) treatment of the preface: no single context in which all claims known | **Accurate**, p. 123 | p. 123 |
| 17 | G&S reject simple symmetric safety because it predicts symmetric accessibility (§2) | **Accurate**, pp. 95–98 | pp. 97–98 |
| 18 | K validates KK given transparency; cliff-edge knowledge | **Accurate**, pp. 105, 107 | pp. 105–107 |
| 19 | v1's §6.2 "question-relativity" objection | **Accurate as a representation**: it is G&S's own contextualist response (p. 121), including the concession that no context has the two single-malfunction situations mutually inaccessible | p. 121 |
| 20 | G&S 2018 n. 10 states the S4.2 claim | **Unsupported here**: G&S 2023 n. 18 cites "Goodman and Salow (2018: 192n10)" for a different (margins-type) characterization of accessibility. I could not check the 2018 footnote. The S4.2/S4.3 material is dropped from v2 | p. 108 n. 18 |

(S2) vs the official chaining principle: (S2) is the special case w1 = z of (iii) with w4 = v; it is implied by (i)–(iii) but strictly weaker. (S1) follows from (ii)+(iii)+irreflexivity. v1's completeness construction (u≫v iff u ∈ C, v ∉ C) does satisfy full (iii), so nothing in v1 was false on this point, but v1 misdescribed the official constraints.

## 2. Prior-art findings (adversarial)

v1's core is **already in G&S 2023**:
- Independent-source / multiple-instrument case: scale + thermometer, pp. 117–118.
- Motivating multi-dimensional normality and rejecting COMPARABILITY by it: pp. 117–119 (they call it "a powerful argument against COMPARABILITY", p. 119).
- Totality of accessibility under comparability: p. 107 ("COMPARABILITY implies (given FACTIVITY and CONVEXITY) that mutually evidentially accessible situations cannot be mutually epistemically inaccessible"), repeated p. 118.
- Contagion between independent instruments under i-normality without comparability: p. 119.
- The probabilist's single-question escape and its concession: p. 121.
- KM without comparability: depicted in fig. 4, p. 119.
Not in G&S 2023: the .3 / S4.2 / S4.3 logic. But .3 from totality is a textbook frame correspondence, and the S4.2 result is close to Stalnaker-style results; its connection to the 2018 footnote could not be verified. Dropped as low-value and risky.

Things in G&S that v2 builds on, with credit given: fig. 4 depicts K excluding (1,2) from (0,2) without comment; n. 30 reports Carter & Goldstein's dimension-wise characterization; n. 37 treats conjunctive knowledge as a consequence of multi-dimensional treatments; p. 116 states the combination intuition; p. 111 states the abductive COMPARABILITY↔MARGINS link and a simplicity preference for K on the incomparable branch.

## 3. What changed and why

v1's thesis (comparability and i-normality cannot handle independent sources) is G&S's own argument, so it cannot be the contribution. v2 moves one step further along G&S's own multi-dimensional branch and asks which completion delivers the independence that motivates it.
- New Theorem 1: on G&S's multi-dimensional structures, KM = ∏_d I_d (i-normality respect by respect; the Carter–Goldstein form falls out of KM).
- New Prop 2: exact condition under which K violates COMBINATION; G&S's own fig. 4 instance; four arguments that this is a cost (cross-dimensional cliff-edge knowledge about the working instrument; Gettier structure G&S themselves count as non-knowledge; lost on learning the antecedent; endorsed by no other completion or probabilist context).
- New Prop 3: meet-normality = K under COMPARABILITY, = respect-wise K on products, framework-compliant, transitive (KK), and the knowledge default under FACTORIZATION.
- 2×2 independence of COMBINATION and MARGINS. Consequence: G&S's abductive link fails for multi-dimensional incomparability, and the MARGINS question becomes the single-respect question.
- Corollary 4: with probabilist single-respect relations, KM's multi-dimensional knowledge = intersection of single-question contexts; the dispute narrows to agglomeration and joint-question knowledge.
- Dropped: Twin Thermometers impossibility, contagion, .3 / S4.2 / S4.3, Dutant–Rosenkranz, Fang, Ahmadian, Loets, Smith, Stalnaker, Hawthorne citations; the unverifiable quotation.
- KM without comparability (v1's open completion): tested. It is exactly respect-wise i-normality and satisfies COMBINATION, FACTORIZATION and monotonicity. This is the centre of v2.
- New citations: Carter & Goldstein 2021 and Goldstein & Hawthorne 2022, both in L3/refs.json and freshly VERIFIED by tools/verify_refs.py; both are cited only for what G&S 2023 report of them.

## 4. v2 thesis (one sentence)

On Goodman and Salow's multi-dimensional account, KM-normality is exactly i-normality applied respect by respect and so delivers the independence that motivates rejecting COMPARABILITY, whereas K-normality violates it; the KK-friendly alternative is a new completion (meet-normality, respect-wise K), so for multi-dimensional incomparability the MARGINS question is independent of the COMPARABILITY question, against G&S's suggested abductive link.

## 5. Exact increment over G&S 2023

G&S introduce KM, the multi-dimensional model, and the figure showing K's verdict. They prefer K on simplicity grounds if comparability fails, and suggest abductive support for COMPARABILITY↔MARGINS. v2 adds:
(a) a proof that KM reduces to the respect-wise form on their structures;
(b) an exact characterization and critique of K's failure of COMBINATION;
(c) a new completion that keeps cliff-edge knowledge and KK while factorizing, with a proof that it coincides with K under comparability;
(d) the resulting independence of the MARGINS and COMPARABILITY questions for multi-dimensional incomparability;
(e) exact agreement between KM and the probabilist on single-respect questions.
All are machine-checked (check.py).

## 6. Three weakest remaining points

1. The normative weight of COMBINATION. A K-theorist may bite the bullet on the conditional "if the thermometer is bizarre, the scale is ordinary". The four supporting considerations in §6 are good but intuition-dependent. The probabilist's joint context violates COMBINATION for aggregate reasons; the reply in §9.1 rests on the multi-dimensionalist not tracking aggregate probability.
2. Scope. Results are for products of chains. Meet-normality's general definition needs greatest lower bounds, so the general KK-friendly completion is open, and non-product incomparability (fig. 3) is not covered. The "independence of the two questions" claim is restricted accordingly.
3. Novelty against literature I could not read. Carter & Goldstein 2021 (known only via G&S n. 30) may already discuss the relation of their dimension-wise characterization to KM or K. G&S's unpublished "Normality, Evidence, and KK" (n.d.(b)) may discuss multi-dimensional KK. Worth a fetch request for Carter & Goldstein 2021 if this essay goes forward.

## 7. Checks and counts

- check.py: exhaustive enumeration over 5,949 multi-dimensional structures (all 3×3 from 43 one-dimensional 3-state structures; 2×4; 2×2×3; 300 random 4×4). Also: all comparable structures with ≤4 situations plus a random sample of 5-situation structures (3,594 in total); G&S fig. 4 and fig. 5 parameter models; 200 random probabilist models; a z3 unsat check of Theorem 1 on arbitrary 3×3 structures; and a STATISM discovery check. Result: ALL CHECKS PASSED (runtime ~3 min).
- Word count (tools/wordcount.py): strict 5,076 (limit 6,000). check_injection: no hard flags.
- Verbatim quotations in v2, all checked against the text file: pp. 110 ("ignorance default", "knowledge default"), 111 (two), 114 (two fragments), 116, 117 (two), 118, 119, 121.
