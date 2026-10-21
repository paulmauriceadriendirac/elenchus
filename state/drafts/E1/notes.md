# E1 notes

**Title.** Ruling Out the Incomparable: Independent Sources and the Structure of Normality-Based Knowledge

**Thesis (one sentence).** Knowledge from independent sources requires ruling out possibilities that are incomparable with (not less normal than) one's actual situation, so every normality theory satisfying Strong Confinement (exclusion only of less-normal worlds) — i-normality under any ordering, and every completion under comparability, including the probabilist one — is inconsistent with minimal anti-skepticism plus Insulation in a two-thermometer case.

**Closest prior work and exact increment.**
- Goodman & Salow 2023 §5 leave comparable (probabilist) vs multi-dimensional normality open. Increment: a structural impossibility (AS + INS + SC inconsistent; minimal; z3-checked) that rules out comparability (and i-normality outright) for single-context multi-source knowledge; plus a contagion corollary under exchange symmetry.
- Goodman & Salow 2018 n.10 claim S4.2 for the KK model without proof (map open problem 6). Increment: proof that k-normality knowledge is exactly S4.2 (transparency, S1, S2, nonempty R_B), and exactly S4.3 under comparability; SC theories validate .3 (totality). Twin Thermometers falsifies .3.
- Ahmadian 2026 (comparability independent), Loets 2022 (general costs of strong normality assumptions), Fang 2026 (multi-question problem — mine arises within one question), Dutant & Rosenkranz 2024 (asymmetric counterparts: Prop. 1 gives the cost on the asymmetric side).

**Map open problems addressed.** 5.1.1 (comparability), 5.1.6 (logic of the KK model / S4.2 claim); touches 5.1.15 (asymmetric counterparts).

**Checks.** z3 on the 3x3 grid: AS+INS unsat under i-normality and comparable k; sat under incomparable k (also with swap symmetry); minimality models sat. Brute force: all 2,501 labelled single-cell structures on <=4 worlds satisfying S1,S2 — i-accessibility total, k reflexive/transitive/convergent, comparable k connected; representation verified for all 87 rooted convergent S4 frames (75 connected) on <=4 worlds. Scripts were in the session scratchpad (check_grid.py, check_logic.py); not part of deliverables.

**Three weakest points a referee would attack.**
1. Novelty risk: G&S may already motivate multi-dimensional normality with independent-source cases, or note totality of i-accessibility; I could not read G&S 2023 or Salow's newer work directly (only via the map). Also S2 is "in the spirit of" G&S chaining, not checked against their official principle (main theorem does not use S2).
2. Insulation is contestable for holists and question-relativists; the reply to question-relativity (dilemma: contagion in joint contexts vs no conjunctive knowledge) depends on how G&S constrain admissible questions, which I know only from the map's quotations.
3. The survivor (incomparable k-normality) has an odd cost (knows "if A far off then B spot on" at <F,N>); km-normality without comparability is left untested because its definition was not available in the map, so the positive moral is incomplete.

**Word count.** tools/wordcount.py: strict 5,023 (limit 6,000); abstract 148 words. check_injection: no hard flags.

**Citations used (all VERIFIED in refs.verification.json).** Ahmadian 2026; Dutant & Rosenkranz 2024; Fang 2026; Goodman & Salow 2018, 2021, 2023; Hawthorne 2025; Loets 2022; Smith 2016; Stalnaker 2006. Quotations: two, both as given verbatim in the map from G&S 2023 (abstract; §5).
