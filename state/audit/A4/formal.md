# Formal audit — A4, final essay `state/drafts/A4/v6.md`

Date: 2026-10-29. Mode: audit. Auditor's independent code: `state/audit/A4/formal/`.

## Overall verdict

**Every formal claim in the essay that I could re-check is VERIFIED, with one FALSE wording ("two of them total orders") and three inaccurate side remarks.** None of the three affects a theorem, the corollary or the Lemma. The Andreas–Günther computations in Section 7 are **UNVERIFIED** (no independent implementation). I re-derived the main results independently and, in two places, more strongly than the essay states them:

- Theorems 1 and 2, the Corollary, the additive identities, the boundary score, the Section 5 escape computations and the Lemma all reproduce in my own implementation of the three HP definitions.
- The Corollary also holds by an exact SMT check over **all** anonymous Pareto filters on the profiles that occur. It holds by an exact SMT check over **all real** additive scores with r > 0. These are stronger than the essay's 355-preorder enumeration and its 3,000-sample check.
- The Lemma holds on all 312 three-variable models (exhaustive) and on 1,500 random models with 4–6 variables. That run covered 27,474 causes and 114,513 conforming witnesses unfiltered, plus 7,109 causes under random componentwise filters applied before AC3. There were 0 counterexamples. I also checked its proof step by step.

## Method

- **Definitions.** I implemented the three HP definitions from the primary text, Halpern (2015), arXiv:1505.00162v1, pp. 3–4. I downloaded it from arXiv and read pp. 3–4 and 7–8.
  - Original: AC2(a) + AC2(b). W is set to w, and every Z′ ⊆ Z is held at its actual values.
  - Updated: AC2(a) + AC2(b^u). Every W′ ⊆ W and every Z′ ⊆ Z.
  - Modified: AC2(a^m). W is frozen at its actual values, W ⊆ V∖X.
  - AC1 and AC3 follow Definition 2.1. AC3 is evaluated after the normality filter.
  - Candidates are every nonempty subset of the endogenous variables, outcome variables included.
- **Normality.** I implemented the essay's categories n, l, f, u and R0/R1, profiles, componentwise filters (all 355 preorders), additive filters, mechanism-specific scores, the conformity-only filter, and variable-indexed componentwise filters. Everything was written from the essay's Section 2 definitions.
- **Files.** `formal/hp_audit.py` produces `formal/hp_audit.out` (94 checks: 91 pass; the 3 "FAIL" lines are the intended test showing that the "total orders" wording is false). `formal/lemma_audit.py` produces `formal/lemma_audit.out`. Both are self-contained and rerunnable; they need z3-solver and sympy.
- **Author's code.** I used it for comparison only. Rerunning `v6_checks/v6_verify.py` reproduces `v6_verify_output.txt` exactly. Its counts — 400 random Lemma models with 357 causes and 940 conforming witnesses, and 3,000 additive scores — match the essay. The seeds are 3 and 11; those exact counts depend on the seed and are not independently reproducible.

## Claims table

| # | Claim | Location (v6.md line) | Verification | Status |
|---|---|---|---|---|
| 1 | Model equations and actual values of all eight cases, e.g. Blocked tracks actual (1,1,1,0); Seedlings G=1, D=0, X=1 | 44–58, 112 | hp_audit §A | VERIFIED |
| 2 | Without normality, every definition counts every candidate above a cause or part of a cause, incl. three switches and short-circuit antidote | 60 | §C: all focal candidates are causes or parts. **Billy's throw is in no cause under any definition** | VERIFIED for the focal candidates; wording over-inclusive (patch P2) |
| 3 | Thm 1: under modified, Suzy, Tracks flip and Doorbells setting each have exactly one witness world, and the three profiles are identical: {R1→R0, n→f, l→n, l→n} | 64–68 | §B: worlds (0,1,0,0,0), (0,0,0,0), (1,0,0,0,0); profiles equal. Proof text checked | VERIFIED (proved + computed) |
| 4 | Hence every anonymous filter admits all three or none | 66 | Immediate from #3; SMT under mod is unsat even without Pareto | VERIFIED |
| 5 | 355 preorders on four categories | 70, 72, 84, 164 | Enumeration: 355 preorders (75 weak orders, 24 linear orders, 219 partial orders) | VERIFIED |
| 6 | Componentwise: Suzy is a cause iff each switch-setting is part of a cause (all 355) | 70 | §E: 0 exceptions; also iff each is a single cause | VERIFIED |
| 7 | Where Suzy is part of a cause only via a conjunction, the conjunction includes Billy's throw, which becomes part of a cause | 70 | §E: 96 such preorders; every such cause contains BT | VERIFIED |
| 8 | Calibration needs l⪰n (prevention), n⪰l (chain), f⪰l (Boulder's only modified witness K l→f, H n→l), u⋡n (short circuit); so f⪰n and the common profile passes | 72 | §D: calibrated set = {l⪰n, n⪰l, f⪰l, u⋡n} exactly | VERIFIED |
| 9 | "Exactly five of the 355 preorders, two of them total orders, give all four calibrating verdicts, under each definition" | 72 | §D: five, the same set under orig/upd/mod. Two of them are total **preorders** (weak orders). **None is a total (linear) order**: all five have n~l | Five: VERIFIED. "total orders": **FALSE** (patch P1) |
| 10 | g_Doorbells = g_Tracks = g_Suzy = r+a−2b+c = (r+2a−2b)+(c−a) = g_Chain + g_Boulder | 73 | §G: sympy, gains computed from model worlds | VERIFIED |
| 11 | Any additive score that keeps the chain and the ducking counts both switches | 74 | Follows from #10 under the modified definition (Boulder has one witness there). Under the older definitions the ducking can be kept via the second witness (gain r+d−b), as line 86 says | VERIFIED (modified-definition context, as in text) |
| 12 | Thm 2: under orig/upd, the Blocked flip has witness [EF←0, LB←0]; its profile = prevention profile + one R1→R0; the anonymous-Pareto consequence follows | 76–78 | §B: unique witness world (0,0,1,1); profile identity checked; sufficiency checked | VERIFIED |
| 13 | g_Blocked = g_Prevention + r; gains r+b−a and 2r+b−a; componentwise admits iff l⪰n | 76, 78 | §G, §D/§I | VERIFIED |
| 14 | Under modified, the flip has no witness of its own; {EF, LB} has the Thm-2 world as witness; for componentwise filters the flip is part of a cause exactly when l⪰n | 80 | §B, §I: 0 exceptions over 355 | VERIFIED |
| 15 | Corollary (all three definitions) | 82–84 | §F: 0/355 preorders under each definition. **Exact SMT: unsat over all anonymous Pareto filters** (28 profiles, 14 Pareto links) and **over all real additive scores, r>0**. 3,000 random integer scores (own seed): 0 | VERIFIED (stronger than stated) |
| 16 | Pareto is used only for the older definitions | 100 | SMT without Pareto: sat for orig/upd, unsat for mod. Core analysis: orig/upd conflict = antidote + Blocked flip + Pareto; mod conflict = Suzy + either switch | VERIFIED |
| 17 | Older definitions give Suzy a second witness [ST←0, BT←0], whose profile is the chain profile + one root (so Pareto admits it if the chain is kept); the switches have no such witness | 86 | §B, §M | VERIFIED |
| 18 | Boundary score (2,0,−1,−5,−3) under both older definitions: keeps prevention, chain, ducking and Suzy; excludes both switches; counts the Blocked flip and the clear-tracks flip via [F←0, LB←1] with gain a−b | 86 | §H; clear-tracks witness unique, gain a−b (§G). Also: Billy in no cause, short-circuit antidote excluded | VERIFIED |
| 19 | Mechanism-specific scores: gains differ by exactly c_BH − c_L | 104 | §G (sympy) | VERIFIED |
| 20 | With c_L = c_LT = −5, other c = 0, r=2, a=0, b=−1, d=−3, the modified definition counts the antidote, C, the ducking and Suzy; Billy, the Tracks flip and the Doorbells setting are in no cause | 104 | §J | VERIFIED |
| 21 | "For a componentwise filter, that judgment is f⋡n for the track while f⪰n for Billy's hit and the ducking" | 104 | §N: a **variable-indexed** version (f⋡n,l only for LT and L) separates correctly from each of the 5 calibrated preorders. A componentwise filter in the essay's own sense (one preorder) cannot do this | VERIFIED in substance; terminology slip (patch P5) |
| 22 | Sprinkler (late-preemption isomorph), frozen sprinkler = −5: the firefighter is not a cause by itself; it is part of a cause only with the activation, which is itself part of a cause | 108–110 | §J: causes {OUT}, {FF,SA}, {SA,FW} | VERIFIED |
| 23 | Seedlings ↦ Doorbells map preserves equations, actual values, defaults | 114 | §J: truth tables compared on all 32 assignments | VERIFIED |
| 24 | With frozen drought-death as abnormal as the frozen bell, the swarm is not even part of a cause | 114 | §J: causes {P}, {G}, {X}. Lowering c_D further changes nothing: no admitted subset witness contains a frozen D | VERIFIED |
| 25 | Inertial coding: componentwise filters exclude the flip's witness; gain becomes b−a = g_Prevention − r, which can be negative while the antidote's is not (all five calibrated preorders) | 118 | §G, §K: under orig/upd the flip is not a cause (nor part of one) and the antidote is a cause, for all five | VERIFIED |
| 26 | Lemma (frozen witnesses) and its proof | 124–126 | Proof checked: acyclicity + uniqueness, roots outside R at actual values, same world passes the filter, AC3. lemma_audit: 0 counterexamples | VERIFIED (proved + computed) |
| 27 | "A check on 400 random models … (357 causes, 940 conforming witnesses)" | 128, 164 | The author's script (seed 3, 400 trials) reproduces these numbers. My independent check is larger (#26) | VERIFIED (as a report of the author's run) |
| 28 | Exceptionless conformity: the ducking and I=1 are lost; the throws become jointly a cause, Billy part of it | 130 | §L: conformity-only filter, and all 36 exceptionless preorders with n⪰l; every surviving cause is root-only | VERIFIED |
| 29 | The Lemma's reasoning transfers to Xiao–Xiong's RHIT definition | 132 | Def. 12 (p. 5) and Def. 13 / Prop. 1 (p. 6) read in `inbox/sources`. RHIT candidates are single variables (AC3 trivial). The Def. 13 intervention has AC2(a^m) form. An "available" world violates no equation, so a non-root candidate is impossible and a root candidate is but-for. Valid if availability is a full-world condition (as Def. 12 states). The actual-value form comes from Def. 13, not from Prop. 1 | VERIFIED (inference); citation of the ground imprecise (patch P7) |
| 30 | Obj. 3 reply: under modified, Suzy's best witness and the switches' witnesses are equally good by any anonymous measure | 150 | Follows from #3 (unique witnesses, identical profiles) | VERIFIED |
| 31 | Appendix: unique witness worlds for prevention, chain, Boulder (mod only (1,1,0,1); older also (0,1,0,1) with B l→u; calibration unchanged), short circuit ([A←0, P←1]; P l→u, V n→l); AC3 automatic for singletons | 162 | §B, §D. The chain's justification covers only freezing at 1; setting I or Y to 0 fails sufficiency, which the text omits | VERIFIED (justification incomplete, patch P4) |
| 32 | Appendix: under older definitions "the extra witnesses of the switches fail sufficiency or move a root to its deviant value … in Tracks, no other contingency changes the arrival" | 162 | §M: there are **no** extra witness worlds; every other contingency fails sufficiency; none moves a root to deviant. **[F←0, A←0] and [F←0, RT←0, A←0], among others, do change the arrival** (and fail sufficiency) | Conclusion VERIFIED; sentence **literally FALSE** (patch P3) |
| 33 | Without normality the implementation reproduces Halpern's (2015) verdicts on the switch models and the short circuit | 164, 140 | §C: 3-variable switch, flip in no cause under all three; route model, flip a cause under all three; clear tracks, flip a cause under orig/upd and not a single cause under mod; both blocked, same pattern; Example 3.10 antidote a cause under all three. Matches Halpern 2015 pp. 7–8 | VERIFIED |
| 34 | "Both classes are anonymous and Pareto" | 34 | By inspection. Componentwise: unchanged variables pass by reflexivity; an added R1→R0 passes. Additive: gain is a sum over the profile; an added root adds r > 0 | VERIFIED (proof by inspection) |
| 35 | Andreas–Günther: their final theory counts the locust swarm (drought preempted) a cause without deviancy and not with it; other conditions already exclude the Doorbells setting and the Seedlings swarm; condition (5)/(2) handling of the simple switch | 136 | Not independently implemented: requires A&G 2024's conditions from the source (not in the repository's inbox). The author's code (rerun) prints this pattern: LOC S dev False/nodev True; DOOR T and SEED S False in all variants. "Deviancy only removes causes ⇒ excluded whatever deviancy is assigned" is valid **if** deviancy is an extra necessary condition | **UNVERIFIED** (independent) |
| 36 | Timing repair ("with destruction dated, the swarm is a but-for cause of destruction on the third day"); Doorbells "admits no corresponding repair" | 114 | Informal; no model given. Trivially true in the obvious dated model (X₃ = G) | Not a formal claim (argued only) |

## Countermodels and additional findings

1. **"Total orders" (FALSE).** The five calibrated preorders are:
   - {n~l, f ≥ n,l}
   - {n~l~f}
   - {n~l, f ≥ n,l,u}
   - f ≻ n~l ≻ u (total preorder)
   - n~l~f ≻ u (total preorder)

   Each contains n~l, so none is antisymmetric. "Total order" in the standard sense (linear order) is false. "Total preorder" or "weak order" is correct.
2. **Billy's throw** is in no cause under any definition without normality (§C), so "every candidate above" in line 60 over-reaches.
3. **Appendix, line 162.** Under the older definitions each switch has a unique witness world. The other contingencies that remove the outcome all hold A or RT at 0 (Tracks) or M, R or E at 0 (Doorbells), and all fail sufficiency. No contingency moves a root to its deviant value, so that disjunct is vacuous.
4. **Not in the essay, but relevant if a referee asks.** In Halpern's clear-tracks model the flip is part of the cause {F=1, LB=0} under the modified definition, without normality, via [F←0, LB←1]. This is the clear-tracks analogue of the line-80 remark. Componentwise filters exclude that witness (a root moves to deviant). Under the boundary score with the modified definition, it is admitted (gain a − b = 1).
5. **SMT core analysis (supports line 100).**
   - Under orig/upd, the conflict is: antidote is a cause + Blocked flip is not a cause + Pareto. Dropping Pareto makes the desiderata satisfiable.
   - Under mod, the conflict is: Suzy is a cause + the Tracks flip is not a cause (or the Doorbells setting is not). This holds with or without Pareto.

## What is proved, computed, only argued

- **Proved in the text, proof checked:** Theorems 1 and 2, the Corollary (from the two theorems), the Lemma, the additive identities.
- **Verified by my independent computation:** every model-specific verdict in rows 1–34 except row 27, which is a report of the author's run, reproduced.
- **Only argued / not independently verified:**
  - the Andreas–Günther results (row 35);
  - the timing repair (row 36);
  - the scholarly attributions (Halpern 2016, Gallow, Beckers, HH 2015 page claims). These are outside this formal audit; the Halpern 2015 quotations at lines 13, 80 and 104 match the arXiv text I read.

## Patch list (exact replacements in `state/drafts/A4/v6.md`)

**P1 (required; line 72).**
Replace: `Exactly five of the 355 preorders, two of them total orders, give all four calibrating verdicts, under each definition.`
With: `Exactly five of the 355 preorders, two of them total preorders, give all four calibrating verdicts, under each definition.`

**P2 (recommended; line 60).**
Replace: `Without normality, every definition counts every candidate above a cause or part of a cause, including the three switches and the short-circuit antidote.`
With: `Without normality, every definition counts every candidate above except Billy's throw a cause or part of a cause, including the three switches and the short-circuit antidote.`

**P3 (recommended; line 162).**
Replace: `Under the older definitions the extra witnesses of the switches fail sufficiency or move a root to its deviant value: in Doorbells, cancelling the press leaves the barking absent when the switch is restored; in Tracks, no other contingency changes the arrival.`
With: `Under the older definitions the switches have no further witness worlds: every other contingency that removes the outcome violates sufficiency. In Doorbells, cancelling the press leaves the barking absent when the switch is restored; in Tracks, the other contingencies stop the arrival only by holding $A$ or $RT$ at 0, which also stops it when the switch is restored.`
(Word count: +12 words approx.; if words are tight, use: `Under the older definitions every other contingency for the switches violates sufficiency; in Doorbells, for instance, cancelling the press leaves the barking absent when the switch is restored.`)

**P4 (optional; line 162).**
Replace: `In the chain, freezing $I$ or $Y$ at 1 restores $Y=1$, so the only witness is $[C\leftarrow0]$.`
With: `In the chain, freezing $I$ or $Y$ at 1 restores $Y=1$, and setting either to 0 violates sufficiency, so the only witness is $[C\leftarrow0]$.`

**P5 (recommended; line 104).**
Replace: `For a componentwise filter, that judgment is $\mathbf f\not\succeq\mathbf n$ for the track while $\mathbf f\succeq\mathbf n$ for Billy's hit and the ducking.`
With: `In componentwise terms, that judgment indexes the preorder by variable: $\mathbf f\not\succeq\mathbf n$ for the track and the left bell, while $\mathbf f\succeq\mathbf n$ for Billy's hit and the ducking.`

**P6 (optional, clarity; line 82).**
Replace: `and makes neither switch-setting nor either flip in Tracks and Blocked tracks a cause, under any of the three definitions.`
With: `and makes neither the switch-setting in Doorbells nor the flip in Tracks or in Blocked tracks a cause, under any of the three definitions.`

**P7 (recommended; line 132).**
Replace: `Their witnesses are actual-value witnesses (they prove that their causes are modified-HP causes, Proposition 1, 6), so the Lemma's reasoning applies directly:`
With: `Their witnesses are actual-value witnesses (Definition 13, 6, holds off-route intermediates at their actual values; Proposition 1, 6, shows that their causes are modified-HP causes), so the Lemma's reasoning applies directly:`
(Definition 13 is on p. 6 of the article, per the `inbox/sources` text; the citation auditor should confirm the page.)

**P8 (optional strengthening; lines 84 and 164).** These need no correction. If the candidate's own formal directory adds an exact check, line 84 could add after "finds none either": `; an exact SMT check over all real additive scores, and over all anonymous Pareto filters on the profiles that occur, confirms this`. Do this only if that check is added to the candidate's own verified code; the essay may not cite this audit's scripts.

**Row 35 (Section 7).** No textual patch is required for consistency: the author's code produces the stated pattern. Independent confirmation needs an implementation of Andreas and Günther (2024) conditions (1)–(5) and deviancy from the source. Until then, the orchestrator should treat these as author-computed only.
