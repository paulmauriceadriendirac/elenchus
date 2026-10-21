# E2 revision notes (v1 -> v2), against the full text of Meehan & Zhang 2025

Source: inbox/sources/meehan-zhang-bayes-is-back.txt (journal pages 285-350; journal page = PDF page + 284). Notation checked against a render of journal p. 336 (prior pi, weighting lambda, lambda_p, script-E for the set of learning situations).

## 1. Fidelity audit of v1's claims about Meehan & Zhang (MZ)

| # | v1 claim (location) | Verdict | MZ page(s) |
|---|---|---|---|
| 1 | MZ evaluate a rule applied across many learning situations rather than a plan for one (§1) | Accurate | 327-330 |
| 2 | They restrict to *globally evidentially constant* rules: same evidence, same posterior across situations (§1, §2) | Accurate but incomplete: the definition holds the prior space fixed; GEC = evidential constancy + noncontrastiveness; it is defended as a *normative* constraint, not a followability constraint | 309, 314-315, 317 |
| 3 | GEC rules are functions of the content learned (§2 "global rule R(E)") | Accurate given a fixed prior space (Fact 5). MZ's rules formally take (S, pi, E) and a state | 291, 316 |
| 4 | Among GEC rules, conditionalization maximizes total expected accuracy, incl. opaque situations (§1, abstract) | Accurate (Fact 10; uniqueness) | 330, 333 |
| 5 | (MZ) regimentation: uniform weight over all factive evidence functions, conditionalization unique optimum (§2) | Accurate. Unweighted sum over all factive learning situations; Fact 9 constant alpha_S = (2^d)^d | 329-330, 343-344 |
| 6 | "A natural moral is that the dispute reduces to availability" (§1, §5 "Availability") | Unsupported and contrary to MZ's framing. MZ reject the followability route (§3.3) and present GEC as normative, not as availability | 297-307, 308, 314, 317 |
| 7 | The hidden premise (weighting condition) of the global argument "has not been identified" (§1 increment) | **Inaccurate.** MZ identify it: weighting functions, extensionality, Fact 11 (iff), Lemmas 1-2 | 335-339, 344-345 |
| 8 | Schoenfield, GW and the global theorem as corollaries of one characterization is new (§1, §3) | **Inaccurate as a novelty claim.** MZ's Lemma 1 is the general characterization; they state that GW is a special case of Fact 11 | 338, 344 |
| 9 | Corollary 1: the (S)-rule for a fixed situation is evidentially constant; constancy alone does not separate (S) from (MZ) | Anticipated. MZ's one-shot rules are exactly GEC rules that mimic META-COND in one problem (Fact 8) | 325-327, 342-343 |
| 10 | "It has been observed that the global result does not survive non-factive functions" (§3) | Unsupported re MZ. MZ assume factivity (n. 4) and note Schoenfield's non-factive result (n. 1); no such observation in MZ | 287 n.1, 290 n.4 |
| 11 | Evaluative (impartial) reading is natural for the uniform total (§5) | Accurate. MZ explicitly adopt an objective reading and contrast it with a subjective reading of formally similar aggregates (n. 35) | 330 n.35 |
| 12 | Cost of the evaluative reading: agent may expect the recommended rule to be worse (§5, Obj. 1) | Anticipated and conceded by MZ (Facts 3, 8; Dana objection; rule-consequentialism analogy) | 302, 325-327, 333 n.37, 333-335 |
| 13 | Prop 3(a): point mass content-sufficient iff partitional | Anticipated: Fact 12 | 338, 346 |
| 14 | Prop 3(b): mixtures of partitional situations content-sufficient | Anticipated: transparent-supported weightings extensional; closure under linear combinations | 336 + n.38 |
| 15 | Theorem 1 (optimal constant rule for arbitrary weighting) | Anticipated: Lemma 1. v1's world-correlated generalization adds nothing at the level that matters (every learning profile is realized by an MZ weighting; see v2 §4.2) | 344 |
| 16 | Theorem 2 (conditionalization optimal iff content-sufficient) | Anticipated: Fact 11 + Lemma 2 (content-sufficiency = extensionality under factivity) | 337, 345 |
| 17 | Obj. 5 worry that MZ's notion of rule/family/weights may differ | Moot. Regimentation (MZ) is faithful; MZ's rules additionally take the prior space as input, which does not affect the results | 291, 316, 329 |
| 18 | Reference: Phil Review 134: 285-350 | Accurate | 285 |

## 2. Prior-art findings (adversarial)

- **In MZ:** general optimal-rule characterization (Lemma 1, 344); necessary-and-sufficient condition (Fact 11 / Lemma 2, 337, 345); point-mass case (Fact 12, 338); transparent mixtures extensional and closure (336); GW as special case (338); the importance-weighting objection itself (335) and the "likelihood of learning p at s" consideration (337); the objective-vs-subjective reading of the weights (330 n.35); Dana-type "why should Dana care" objection (333-335); dogmatic rule beating BCOND in Dana (Fact 3); one-shot rules (325-327).
- **Not in MZ:** permutation-invariance -> extensionality (v1 Cor 3); measure-zero genericity (v1 Prop 3d); cyclic informants (v1 Prop 3c); non-factive uniform -> no updating (v1 Cor 4); worst-case aggregation (v1 Prop 4); equivalence of the uniform total with yes/no questions; extensionality of the opaque-only total and its irreducibility to transparent weightings; the importance-family/No News equivalence; the representative-agent reading of Lemma 1.
- **Do MZ anticipate or answer v1's objection?** Yes, largely. v1's dilemma (credal vs evaluative weights) is MZ n.35 plus their §5.3 discussion; v1's "symmetry assumption" diagnosis is their extensionality (they call it possibly bedrock and connect it to internalism, 337-339). v1's attack on an "availability" moral targets a view MZ do not hold.

## 3. What changed and why

v1's core result did not survive: its Theorems 1-2 and Prop 3(a,b) are MZ's Lemma 1, Fact 11 and Fact 12, and its critique attacks a moral (availability) that MZ reject and a weighting issue they discuss explicitly. v2 drops the availability framing, the credal/evaluative dilemma as a critique, v1's Theorems 1-2 as contributions (now credited to MZ), the non-factive corollary and v1's Brier-over-atoms examples. It keeps the minimax point (now on MZ's own Dana numbers and Table 3) as Objection 4 and the cyclic case as an illustration. New contributions (all checked in check.py): Prop 1 (uniform total = 2^{(n-1)^2} x yes/no total; Fact 10 from Fact 1), Prop 2-3 (opaque-only uniform weighting extensional; not equivalent to any transparent weighting for n >= 3), Prop 4 (for product/additive proposition-importance weightings, on all-factive or opaque-only domains: extensional <=> H constant <=> No News; tilted-prior form of the optimal rule), the question-vs-answer corollary, and the representative-agent reading of Lemma 1 (Hi-TEA under lambda selects META-COND for an agent with credence lambda about her learning situation). The essay's stance moved from critique to diagnosis plus partial repair of MZ. check_v1.py preserves v1's script; check.py was rewritten and rerun (all checks True; reproduces MZ Tables 2-3 totals -2.72/-4.48/-6.8).

Citations: dropped Easwaran 2013, Joyce 1998, Pettigrew 2016 (no longer used). Added Levinstein 2019 (L5 refs.json; verify_refs VERIFIED this session). Carr 2021 returned MISMATCH (online-first year), so it is not cited; MZ n.35 is cited instead. All MZ page references checked against the text file. Verbatim quotations (checked word for word): pp. 309, 312-313, 330 n.35, 335 (bracketed capital), 336, 337 (x3), 338 (x3), 339.

## 4. Thesis of v2 (one sentence)

The extensionality on which Meehan and Zhang's vindication of conditionalization rests is neither disguised internalism (the vindication survives restriction to opaque problems, though their own uniform total is equivalent to a total over transparent yes/no questions) nor bedrock (for weightings on which importance attaches to the propositions learned, extensionality is equivalent to the principle that learning nothing new leaves credences unchanged).

## 5. Exact increment over Meehan & Zhang

MZ prove that BCOND is Hi-TEA-optimal iff the weighting is extensional, and they leave open how extensionality relates to internalism (338) and whether it is bedrock (337). v2 (i) shows that their uniform total is evaluatively identical to a total over transparent yes/no problems, so Fact 10 is GW summed (new); (ii) shows that the uniform total over opaque problems alone is extensional and irreducible to any transparent weighting, a stronger form of their claim at 338 (new); (iii) proves that, for the natural family that generalizes their uniform weighting by proposition-importance (product or additive, all or opaque problems), extensionality <=> balance <=> No News (new); (iv) shows that the Lemma 1 rule is META-COND for a representative agent, which gives their objective reading of the weights an argument for extensionality (new observation, labeled non-conclusive).

## 6. Three weakest remaining points

1. **Modesty of the formal core.** Props 1-4 are short counting arguments on top of MZ's Lemma 1. A referee may call Prop 1 an easy corollary of MZ's own Fact 7 proof. The value lies in the dialectical use, which the essay must press.
2. **Scope of Prop 4.** It covers only state-independent product and additive importance aggregations. Non-separable aggregations and problem-based importance (e.g. extra weight on particular problems, Obj. 2/3) escape, and the essay concedes that the residual dispute (state-dependent weights) is not settled.
3. **The representative-agent argument for extensionality (§4.2)** is suggestive, not conclusive. The non-Bayesian reply, that the uniform weighting is also a hypothesis about learning (random yes/no questions), is stated but only partly answered. The step from noncontrastiveness for rules to a constraint on standards is undefended.

## 7. Word count

`tools/wordcount.py state/drafts/E2/v2.md`: strict 5122 (limit 6000, target 5600). check_injection.py: no hard flags.
