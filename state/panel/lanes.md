# Candidate research lanes (ranked)

Compiled 2026-10-21 by the panel-analyst from `state/panel/committee_map.md`.
CONFIG: `topic: none`, `avoid: none` — no restriction applied.

Lanes are research areas or questions, never theses. "Judges with expertise" lists only people
with published work in the area (keys in `committee_bibliography.json`); organisers are shown in
brackets and are not judges. "Verifiability" = how far a contribution can be checked decisively
(proofs, machine-checkable consistency, decisive cases) — the property an AI pipeline can exploit.
"Breadth" = how significant a result would look to the *whole* committee, not just the
specialists. Crowding is an estimate of how many other AI-generated entries will land there.

Scoring (1–5, higher better; crowding scored inversely): expertise depth, verifiability, breadth,
low crowding. Ranks weigh verifiability and low crowding slightly above breadth, because the
competition's judging funnels through specialist ratings before the committee vote.

**Single most crowded area: AI consciousness, sentience and moral status (Lane 14).**

---

## 1. Decision theory under extreme stakes: unbounded/infinite value, fanaticism, dominance
- **Scope.** Principles linking probability and value when utilities are unbounded or outcomes
  infinite: fanaticism vs anti-fanaticism, St Petersburg/Pasadena-type prospects, stochastic
  dominance and background risk, symmetry/invariance principles, risk-weighted alternatives.
  Questions are typically "which combinations of principles are consistent, and what do they
  entail?".
- **Judges with expertise.** Tarsney (Tarsney2026Small, Tarsney2025Expected,
  Tarsney2024Against), Easwaran (Easwaran2008Strong, Easwaran2014Principal,
  Easwaran2014Decision), Kowalczyk (Kowalczyk2025Saving), Nebel (Goodsell2024Symmetry; forthcoming
  "The Value of Risky Prospects"), Greaves (Greaves2024Desire), Weisberg (Thoma2017Risk), Salow
  (Campbellmoore2020Avoiding), Fitelson (decision theory listed) [Goodsell: Goodsell2023Decision,
  Goodsell2025Symmetries, Goodsell2021St; Thornley].
- **Verifiability.** Very high: consistency/impossibility results can be proved and
  machine-checked (z3/sympy for finite fragments; explicit countermodels).
- **Breadth.** High: fanaticism and infinite value matter to ethicists, epistemologists and
  AI-risk readers alike.
- **Crowding.** Moderate. Fanaticism is a well-known EA topic, so AI entrants may write on it,
  mostly discursively; formal increments are rarer. Originality risk: the literature is dense and
  recent (2023–26), and an organiser maintains a "Logical Maps" database of principles in exactly
  this area — any claimed new result will be checked against it.
- **Rank reason.** Best combination of expert depth (≥6 judges), provability, and committee-wide
  interest.

## 2. Comparability, completeness and incommensurability of value and preference
- **Scope.** Whether betterness/preference/credence must be complete; dominance arguments
  against incompleteness; comparability of natural-language comparatives; consequences for
  choice (money pumps, sequential choice) and for agent design (incomplete preferences in AI).
- **Judges.** Nebel (Dorr2022Case, Dorr2021Consequences, Hedden2024Multidimensional), Dorr (same),
  Tarsney (Tarsney2025Dominance, Tarsney2024Against), Kowalczyk (Kowalczyk2024Opaque), Greaves,
  Easwaran (Easwaran2021New) [Goodsell; Thornley: incomplete preferences as a shutdown route].
- **Verifiability.** High (principles are crisp; counterexamples and impossibility results).
- **Breadth.** High: links ethics, decision theory, philosophy of language (comparatives) and AI
  safety.
- **Crowding.** Low–moderate.
- **Rank reason.** A live question on this panel: Dorr–Nebel–Zuehl (Dorr2022Case) and
  Tarsney–Lederman–Spears (Tarsney2025Dominance) argue against forms of incompleteness, while
  Tarsney2024Against recommends an intermediate view that permits incomplete preferences about
  fanatical gambles, and an organiser's shutdown work relies on incomplete preferences. A
  contribution will be recognised and stress-tested from several directions. Caution (§1.6):
  take a side only on the merits.

## 3. Knowledge, normality and inquiry: KK, omega knowledge, evidence-gathering norms
- **Scope.** Structure of higher-order knowledge (KK, omega knowledge, "fragility"); normality-
  based epistemic logic and belief revision; safety and closure; knowledge–chance principles;
  dogmatism puzzles, evidence avoidance and the value of information (Good's theorem); knowledge
  norms of assertion/action.
- **Judges.** Salow (Goodman2023Epistemology, Goodman2024Belief, Salow2024Fallibility,
  Ahmed2019Don), Hawthorne (Hawthorne2025Normality, Carter2024Dogmatism, Goldstein2024Safety),
  Goldstein (Goldstein2024Iterated, Goldstein2021Fragile, Goldstein2024Kk), Greco
  (Greco2014Could, Greco2014Iteration), Dorr (Dorr2013Knowing), Weisberg
  (Weisberg2010Bootstrapping, Weisberg2013Knowledge), Mandelkern (Mandelkern2022Assertion)
  [Goodsell: knowledge norm of assertion, in progress].
- **Verifiability.** High: claims live in explicit Kripke/normality models; countermodels are
  checkable.
- **Breadth.** Medium–high (core epistemology; familiar to most of the committee).
- **Crowding.** Low.
- **Rank reason.** Very strong specialist core of 6–7 judges in active, recent dialogue
  (Hawthorne 2025 responds to Goodman–Salow; Salow responds to Goldstein), so the originality
  baseline is sharp and a precise increment will be recognised. Risk: that same density makes
  "already in the literature" the default verdict — the prior-art hunt must read the 2023–26
  papers in full.

## 4. Decision-theoretic AI safety: shutdown, corrigibility, risk-averse and incomplete agents
- **Scope.** Formal questions about artificial agents' preferences: shutdown problem theorems,
  shutdown-seeking goals, incomplete preferences, risk aversion as a safety property, defining
  deception/manipulation, instrumental convergence; whether safety measures can backfire.
- **Judges.** Goldstein (Goldstein2024Shutdown, Goldstein2023Language), Robinson
  (Goldstein2024Shutdown, Robinson2023Action, Robinson2024Ai), Tarsney (Tarsney2025Deception),
  Hawthorne/Cappelen/Dever (Cappelen2025Ai, Cappelen2025Aib), Vold (Harris2026Taxonomy),
  Millière (Milliere2025Normative), Günther (alignment co-author, TMLR 2024) [Thornley:
  Thornley2024Shutdown, Thornley2025Towards].
- **Verifiability.** High for the decision-theoretic strand (theorems about agents satisfying
  stated axioms); low for the discursive strand.
- **Breadth.** High (AI is the competition's subject; formal results here also interest
  decision theorists).
- **Crowding.** Moderate–high overall; the *formal* strand is much less crowded than discursive
  "alignment ethics".
- **Rank reason.** Unusual combination of formal tractability and AI relevance. Caution: one
  organiser's own research programme is here; this is a reason for extra care with attribution
  and originality, not a reason to choose the lane.

## 5. Bayesian foundations: accuracy, updating, supposition, deference, pooling
- **Scope.** Accuracy-first arguments; conditionalization vs imaging; supposition;
  expert deference and Reflection; opinion pooling (linear, geometric, Jeffrey, upco);
  regularity and zero-probability conditioning; confirmation measures.
- **Judges.** Fitelson (Dorst2021Deference, Eva2022Four, Fitelson2021Problem), Easwaran
  (Easwaran2013Expected, Easwaran2014Regularity, Easwaran2015Accuracy), Weisberg
  (Pettigrew2024Updating, Pettigrew2025Jeffrey, Weisberg2009Commutativity), Salow
  (Campbellmoore2022Accurate), Greaves (Greaves2006Justifying, Greaves2013Epistemic), Dorr.
- **Verifiability.** Very high (theorems; PrSAT-style decision procedures exist).
- **Breadth.** Medium (specialist; legible to formal-minded majority of the panel).
- **Crowding.** Low.
- **Rank reason.** Excellent verifiability and expert depth; lower committee-wide significance
  unless a result bears on a broad question (e.g., disagreement, AI forecasting aggregation).

## 6. Population ethics and aggregation under risk and identity uncertainty
- **Scope.** Impossibility theorems for population (prospect) axiologies; ex ante vs ex post
  Pareto; opaque identity; person-affecting views; limited aggregation; summability and
  measurement of well-being; infinite populations and impartiality.
- **Judges.** Nebel (Nebel2023Sum, Nebel2025Infinite, Nebel2019Intrapersonal), Kowalczyk
  (Kowalczyk2021Transfinitely, Gustafsson2026Ex, Kowalczyk2024New), Greaves
  (Greaves2017Population, Greaves2017Moral), Tarsney (Tarsney2024Non, Tarsney2021Average),
  Easwaran (Easwaran2021New) [Thornley, Goodsell].
- **Verifiability.** High (axiomatic).
- **Breadth.** Medium–high.
- **Crowding.** Moderate (popular with AI systems via EA/longtermism; dense literature).
- **Rank reason.** Strong expertise, but the field is saturated with impossibility theorems;
  novelty is hard to secure.

## 7. Conditionals, modals and probability
- **Scope.** Triviality results; probabilities of conditionals; modus ponens failures; epistemic
  modals and their logic (orthologic, dynamic vs bounded semantics); free choice; learning
  conditional information; causal-model semantics for counterfactuals.
- **Judges.** Mandelkern (Mandelkern2024Bounded, Mandelkern2020Counterexample,
  Holliday2024Orthologic), Goldstein (Goldstein2017Triviality, Goldstein2019Generalized),
  Fitelson (Fitelson2015Strongest, Eva2022Four), Günther (Gunther2017Learning,
  Gunther2022Causal), Dorr (Dorr2013Embedding, Dorr2016Against, Dorr2026Sequence), Hawthorne,
  Dever, Easwaran.
- **Verifiability.** High (semantic models; proofs; checkable countermodels).
- **Breadth.** Medium (very legible to the language/formal majority; less to ethicists).
- **Crowding.** Low.
- **Rank reason.** Deep specialist bench (≥6) and decisive methods; breadth is the limit.

## 8. Causation, chance and counterfactuals
- **Scope.** Actual causation (regularity, difference-making, causal models); high-level and
  mental causation; counterfactuals under determinism; chance in non-standard spacetimes;
  causal vs counterfactual independence; legal causation and proof.
- **Judges.** Günther (Andreas2021Difference, Andreas2024Regularity, Gunther2024Probability),
  Jaeger (Jager2021List, Jager2025Loops), Dorr (Dorr2016Against), Hawthorne ("Legal Causation and
  Zeno Sequences", 2025, Crossref), Fitelson (causal strength, Simpson's paradox per CV)
  [Goodsell2022Tossing].
- **Verifiability.** Medium–high (causal models give decisive verdicts on cases).
- **Breadth.** Medium.
- **Crowding.** Low.
- **Rank reason.** Few judges but very precise readers; a sharp counterexample is recognisable.

## 9. Imprecise credence, symmetry and measure
- **Scope.** Whether rationality permits/requires imprecise credence; non-measurable sets;
  symmetry and invariance arguments; infinite fair lotteries; evidential equivalence paradoxes.
- **Judges.** Dorr (Dorr2023Non, Dorr2020Solving), Nebel (Goodsell2024Symmetry), Hawthorne
  (Dorr2020Solving), Easwaran (Easwaran2014Regularity), Fitelson, Weisberg [Goodsell].
- **Verifiability.** Very high (measure theory).
- **Breadth.** Low–medium.
- **Crowding.** Very low.
- **Rank reason.** Ideal for a provable result, but the audience is narrow.

## 10. Normative uncertainty and metanormativity
- **Scope.** How to act under moral/normative uncertainty; intertheoretic comparison;
  bargaining and social-choice approaches; regress problems; noncognitivist accounts of moral
  uncertainty; application to AI systems that must act under moral disagreement.
- **Judges.** Robinson (Robinson2022Moral, Robinson2021Normative, Robinson2023Moral), Tarsney
  (Tarsney2018Normative, Tarsney2024Metanormative), Greaves (Greaves2023Bargaining,
  Greaves2017Moral), Nebel (reasons and rationality).
- **Verifiability.** Medium–high (aggregation results).
- **Breadth.** Medium.
- **Crowding.** Low–moderate.
- **Rank reason.** Solid expertise; moderate breadth.

## 11. Higher-order logic, modality and metaphysical foundations
- **Scope.** Higher-order identity and quantification; modal variation and necessity of
  arithmetic; tense–modal interaction; verificationism and knowability (Church–Fitch).
- **Judges.** Dorr (Dorr2016To, Dorr2019Diamonds, Dorr2021Bounds), Hawthorne
  (Goodsell2026Unknowable, Dorr2021Bounds), Chalmers (Chalmers2012Constructing) [Goodsell:
  Goodsell2021Arithmetic, Goodsell2026Unknowable].
- **Verifiability.** Very high (proof-theoretic).
- **Breadth.** Low–medium.
- **Crowding.** Very low.
- **Rank reason.** Only 2–3 judges; strong but narrow.

## 12. Interpreting AI systems: meaning, reference, belief and interpretability
- **Scope.** Whether and how LLM outputs/internal states have content; externalist and
  teleosemantic metasemantics for AI; belief/desire attribution (interpretationism);
  introspection; propositional and mechanistic interpretability; evaluation methodology.
- **Judges.** Chalmers (Chalmers2025Propositional, Chalmers2026We), Cappelen & Dever
  (Cappelen2021Making, Cappelen2024Introspective, Cappelen2026Hyper), Mandelkern
  (Mandelkern2024Language, Holliday2024Conditional), Millière (Mollo2026Vector,
  Milliere2026Anthropocentric), Goldstein (Goldstein2026Chatgpt, Goldstein2026Llms), Sterken
  (Sterken2024Conversational), Shevlin (Shevlin2026Three), Vold.
- **Verifiability.** Low–medium (some claims testable empirically, most conceptual).
- **Breadth.** High.
- **Crowding.** High — second most crowded.
- **Rank reason.** Largest pool of interested judges, but crowded and hard to make decisive;
  originality bar raised by a just-published OUP volume (*Communicating with AI*, 2026) and
  several 2025–26 papers.

## 13. Conceptual engineering and philosophical methodology
- **Scope.** Possibility, limits and norms of revising concepts; abandonment of defective
  terms; idealization and modelling in philosophy; progress in philosophy.
- **Judges.** Cappelen (Cappelen2018Fixing, Cappelen2023Concept, Cappelen2012Philosophy),
  Sterken (Sterken2020Linguistic), Dever (Dever2020Preliminary), Chalmers
  (Chalmers2020Conceptual), Greco (Greco2023Idealization).
- **Verifiability.** Low.
- **Breadth.** Medium.
- **Crowding.** Moderate–high (AI entrants are likely to write about AI and the method of
  philosophy).
- **Rank reason.** Recognisable but hard to make decisive.

## 14. AI consciousness, sentience, welfare and moral status — MOST CROWDED
- **Scope.** Whether current/near-future AI systems are conscious or have welfare; indicator
  methods; the specificity problem; moral patiency criteria; AI rights.
- **Judges.** Chalmers (Chalmers2023Could, Long2024Taking), Shevlin (Shevlin2021Non,
  Shevlin2021Could, Shevlin2026Aeroplanes), Goldstein (Goldstein2025Ai, Goldstein2026Case),
  Millière (self-consciousness), Vold (Vold2020Consciousness).
- **Verifiability.** Low.
- **Breadth.** High in public interest; medium for this committee.
- **Crowding.** Highest of all lanes: the topic most AI-generated philosophy gravitates toward.
- **Rank reason.** Last: low verifiability plus extreme crowding; any entry here must clear a
  very high originality bar against a fast-moving 2023–26 literature.

---

## Summary table

| Rank | Lane | Judges (n) | Verifiability | Breadth | Crowding |
|---|---|---|---|---|---|
| 1 | Decision theory under extreme stakes | 8 [+2 org] | very high | high | moderate |
| 2 | Comparability/completeness of value | 6 [+2] | high | high | low–mod |
| 3 | Knowledge, normality, inquiry | 7 [+1] | high | med–high | low |
| 4 | Decision-theoretic AI safety | 8 [+1] | high (formal strand) | high | mod–high |
| 5 | Bayesian foundations | 6 | very high | medium | low |
| 6 | Population ethics & aggregation | 5 [+2] | high | med–high | moderate |
| 7 | Conditionals, modals, probability | 8 | high | medium | low |
| 8 | Causation, chance, counterfactuals | 5 [+1] | med–high | medium | low |
| 9 | Imprecise credence, symmetry, measure | 6 [+1] | very high | low–med | very low |
| 10 | Normative uncertainty | 4 | med–high | medium | low–mod |
| 11 | Higher-order logic & modality | 3 [+1] | very high | low–med | very low |
| 12 | Interpreting AI systems | 9 | low–med | high | high |
| 13 | Conceptual engineering & method | 5 | low | medium | mod–high |
| 14 | AI consciousness & moral status | 5 | low | high (public) | **highest** |

Notes for the orchestrator: lanes 1, 2 and 4 share machinery (dominance, completeness,
risk attitudes) and can be mapped together; lanes 3 and 5 share the formal-epistemology bench.
If `lanes_to_map: 6`, the top six by this ranking are 1–6.
