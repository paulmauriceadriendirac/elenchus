# Referee report — S1 Formal epistemologist (Bayesian foundations), with G3 literature-expert standards — P-7297

## Thesis and argument as I understand them (≤120 words)

Dorst (2019, §4.2, Prop. 5) claims that expected-accuracy maximization yields fixed, proposition-specific Lockean thresholds even without Separability, given Sequence-Irrelevance. The essay finds two gaps in that derivation:
- **Quantifier gap (ME).** The increment from adding a belief need not depend on the world only through that belief's truth-value.
- **Content gap (BI).** The resulting threshold need not be independent of the other beliefs, and an order-independence principle cannot supply this.

The countermodel is the "record measure": a separable score plus a premium β>0 for an error-free belief set. It is truth-directed, alethic and order-independent. Yet for every β it believes {w1} at credence c and withholds it at a higher c′ (Thm 2). ME+BI restore separability (Thm 1), and record-optimal states are "core-relative Lockean" (Thm 3).

## Verdict
Prize: not finalist
Journal recommendation: major revisions

## Scores
Clarity: 6 | Argument: 6 | Significance: 5 | Originality: 6 | Literature: 4 | Accuracy: 6 | OVERALL: 6

## The single most serious problem

**Location:** §3 (central case), all three "consequences" in §5, the §6 objection "The premium is representation-dependent", and the stakes paragraph (§1 ¶4).

**No fatal flaw in the negative result.** I recomputed the central case and checked Theorems 1–3, and they are correct (see Proof check).

**The problem.** Everything the essay builds on the counterexample rests on a measure whose verdict about a fixed proposition, at fixed credences, changes when an irrelevant possibility is split. That includes the neutrality thesis ("accuracy-first epistemology is neutral between Lockean and guess-like belief"), core-relative Lockeanism as a live theory, and the claim that non-monotonicity is "available to accuracy-firsters". The premium is paid once, while the additive part ranges over the whole Boolean algebra.

**Concrete demonstration.** Split the 1% world of C′ = (0.75, 0.01, 0.24) into two worlds of 0.005 each.
- The supersets of {w1} that exclude w3 go from 2 to 4.
- So the additive value lost by hedging to the core {w1,w3} doubles (0.53 → 1.06), while the premium gain stays 3(0.99−0.75) = 0.72.
- Now Φ({w1}) = 5.00 + 2.25 = 7.25 beats Φ({w1,w3}) = 3.94 + 2.97 = 6.91, so {w1} is believed at 0.75.
- At the correspondingly refined C = (0.70, 0.075, 0.075, 0.15), {w1} is still believed (Φ({w1}) = 6.50 is maximal).

The flagship non-monotonicity is gone. In general, with m null worlds the core is chosen as if the premium were β/2^m. So for fixed β the Theorem-2 window (length βT/(D(2D+β)) above τ) shrinks exponentially under refinement. Fine enough refinements make the record measure's choices coincide with the Lockean ones in cases of this kind.

**Why it matters.** This is the standard language-dependence objection in accuracy-first epistemology, and it bites harder than §6 concedes:
- (a) It hands the Lockean a principled, non-question-begging exclusion. Accuracy verdicts about a coarse question should not depend on how unrelated possibilities are individuated, and separable scores satisfy that requirement.
- (b) It contradicts the essay's own rationale for the premium. The inferential value of an error-free record should grow with the record, not be diluted by it.

The counterexample to Prop. 5 survives, because Prop. 5 is claimed for every finite W. The significance claims built on it do not survive as stated.

## Major problems

1. **§1 ¶3 and §5 — The closest prior work for the positive half is missing, and its key structural property is mis-credited.**
   - **Problem.** Theorem 3 selects a core by maximizing Φ(X) = βC(X) + Σ_{p⊇X} max(e_p,0). That is the expected value of a truth-directed reward for hypothesis X, plus a world-independent reward for how much valuable content X entails. In other words, it is an accuracy–informativity trade-off over candidate answers.
   - **Dorst & Mandelkern, "Good Guesses" (PPR 2022).** This is their structure. Theorem 3(ii) ("X* contains every world more probable than any world it contains") is, I believe, their "Filtering" constraint. The essay credits filtering to Holguín 2022 §10. Holguín's guess-based account of thinking draws, I believe, on Dorst–Mandelkern guessing.
   - **Levi, *Gambling with Truth* (1967).** This is the classic expected-epistemic-utility rule on which accepted belief is the consequence set of a selected strongest hypothesis, trading probability against content.
   - **Leitgeb's stability theory (2014; 2017).** Belief is generated from a P-stable core. Every P-stable^r core with r ≥ 1/2 contains every world more probable than a positive-probability world outside it: take E = {w,v}. Leitgeb also characterizes when closure and a Lockean threshold coincide, which is the territory of Theorem 3(iii) and of "Lockean belief is the special case…".
   - **None of these is cited.** By G3 standards this is the costliest gap. The first item is co-authored by the target author and moves him toward exactly the guess-like picture the essay offers as the alternative. "Here that behavior is obtained within an accuracy-maximizing model" is not new as stated: D&M already obtain non-monotone, filtered guesses from expected truth-directed value.
   - **Fix.** State the increment exactly. The essay gets the same core structure, plus a threshold component, from a purely alethic score over *unrestricted belief states*, which is what bears on Dorst 2019's Accuracy First derivation. Compare Φ explicitly with D&M's expected answer-value and with P-stable cores.

2. **§4 (after BI) and §6 (third objection) — Theorem 1 is misdescribed in a way that hides its best consequence.**
   - **The error.** Step (ii) of the essay's own proof shows that under ME the gain J_p^B = T_p^B − F_p^B is the same for every background B. Hence τ_p^B = −F_p^B/J_p, and background-independence of the *threshold* is *equivalent* to BI, not weaker. So two sentences are false given ME:
     - "BI is stronger than simply requiring the ratio that fixes a threshold to be background-independent" (§4).
     - "Background-independent thresholds need not be identified with background-independent marginal values. Theorem 1 concerns the latter, stronger condition" (§6).
   - Without ME there is no value-fixed ratio at all.
   - **The stronger, cleaner statement.** Given ME (a single state-independent A, no complementary pairs), Dorst's derivation of Prop. 5 is valid iff A is separable on that domain.
   - **The dilemma this yields.** The essay only gestures at it ("narrows the admissible holism"). Under ME, the belief-dependence Dorst explicitly permits (F_p^{B0} varying with B0) just *is* a non-additive κ. Either Dorst admits it, and fn. 8 refutes Prop. 5. Or he rejects it, and §4.2 adds nothing to Corollary 2.
   - **Scope.** Theorem 1 concerns one state-independent A. Dorst's §4.2 indexes measures to the current state (A_{B0}). For such families, ME+BI deliver fixed thresholds directly via Prop. 4 without collapsing to a single separable measure, so "recover separability" needs that qualification.

3. **§5 "Second" and fn. 7 — The horse-race model is misdescribed.**
   - **The numbers.** With the stated values, τ_1 = 0.66/1.66 ≈ 0.398 and τ_2 = 1.01/1.66 ≈ 0.608. At (0.45, 0.50, 0.05), C(B∨C) = 0.55 < τ_2, so e_{B∨C} = −0.097.
   - **The true optimum.** The unique optimum is {B, A∨B, W}, *not* "the set of consequences of 'B wins'". The reported 1.832 is exactly the value of that non-closed state. The full consequence set {B, A∨B, B∨C, W} scores 1.735.
   - **Why it matters.** The agent thinks B will win but does not think A will lose. That is a single-premise closure failure in the very case offered as reproducing Holguín's best-guess verdict, and I take Holguín's thinking to be closed under what the best guess entails.
   - **It was predictable.** Theorem 3(i)'s closure guarantee holds only for uniform values, and Easwaran's appendix on varying values already warns that closure fails when values vary. The margins are also tiny (0.004 and 0.008).
   - **Fix.** Re-tune the values and re-verify, or cut the paragraph and fn. 7. In either case delete "So the premium does what Holguín says sophisticated Lockeanism cannot" unless the corrected model supports it.

4. **§3 — The scope of Prop. 5 is left implicit, and Dorst's own accommodation mechanism is not engaged.**
   - **Scope.** The contradiction "τ ≤ 0.70 and τ ≥ 0.75" requires that Prop. 5's T_p, F_p be values of the measure, constant across credence functions within a context. That is the correct reading: Dorst's proof sets T_p := T_p^{B−}, and his §5 reply to the vacuity worry depends on thresholds coming from values. The essay must say so.
   - **Accommodation.** More importantly, Dorst §4.1 (pp. 190–191) already lets the question lower F "until it gets an answer". So belief that Steve wins at credence 0.48 holds in Case 1 and fails in Case 2. A defender will say that credence-sensitive belief is already part of variable Lockeanism.
   - **Fix.** Add a paragraph on why non-monotonicity with values held fixed matters. The answer is available: Holguín's complaint about brute coordination of thresholds, which the record measure meets without context shifts. It is not made.

5. **§2 — The essay's reading of Sequence-Irrelevance is defensible but asserted, not argued.**
   - **The record measure does make greedy formation order-dependent.** At C, considering {w1} first from ∅ gives Δ = e_1 − β(1−0.70) = 0.1 − 0.9 = −0.8, so {w1} is rejected and the final state is {12,13,W} (4.20). Considering it last gives Δ = +0.1, so it is accepted.
   - **The defender's reply.** Dorst's God example (p. 194) is precisely about designing a sequence to change what it is rational to believe. So a defender will say the record measure violates the principle as Dorst motivates it.
   - **The answer exists.** Prop. 4 is an "only if" condition and needs only that a rational final state be locally optimal against its last-step predecessor, which every global optimum is. Under Permission, no greedy outcome is thereby made rational.
   - **Fix.** Give that argument, with the example. Otherwise the counterexample looks as if it trades on an idle reading of the principle.

## Minor problems
- **Theorem 3.** "Generic" is undefined. Say: Φ has a unique maximizer and no C(p) = τ_p. The four-world example has a tie (w3, w4), so it is not generic, although its optimum is unique.
- **Abstract and §1.** "For every positive premium" omits Theorem 2's hypothesis T < −F (Conservativeness).
- **§3 runner-ups.** Identify them. At C the runner-up {12,13,W} has the *same* core and lacks only {w1}, so the 0.10 margin equals e_{w1}. Belief at C is thus driven by the separable term, and withholding at C′ by the premium. Saying so makes the mechanism transparent.
- **Theorem 2 at C′.** It says {w1} is in "no optimum", but Permission is stated for unique optima. Either prove uniqueness at (c′, ε, ·) or state Permission for "some optimum"; the §6 non-satisfiability reply covers this.
- **Empty state.** Since ∩∅ = W, the empty state collects β at every world. The inferential rationale ("multi-premise deduction yields only truths") is odd for an empty record. Say whether β should scale with |B|, which also bears on the refinement problem.
- **§1 credit.** "Dorst (2019) extended it … (his Corollary 2)": Dorst himself states that Corollary 2 is Easwaran's §G.2 result (p. 183).
- **Wording.** "The present contribution sought is…" is garbled. "Holguín (2022, §5) independently argues" is an odd way to describe prior work.
- **Footnotes.** Numbering skips [^6]. Footnotes 2, 4 and 5 report computations that cannot be checked from the essay; either supply code or compress them to one sentence.
- **Wang (2025).** PhilPeople lists 182(5): 1433–1465; the essay has 182(5–6).

## Prior work this resembles (only if confident; author, year, title, confidence %)
- **Dorst & Mandelkern 2022, "Good Guesses", *PPR* 105: 581–618.**
  - Existence: 99% (confirmed).
  - Content: expected truth-directed answer-value, accuracy–informativity trade-off, filtered guesses, applied to belief.
  - "Filtering" as their named constraint: ~80% (not confirmed in this run).
  - Closest prior work for Theorem 3 and §5.
- **Levi 1967, *Gambling with Truth*.** 97%. Expected epistemic utility acceptance: accept the consequences of the strongest unrejected hypothesis, trading probability against informational content. Its rejection rule yields filtering-like cores.
- **Leitgeb 2014, "The Stability Theory of Belief", *Phil Review* 123(2): 131–171** (bibliographic details confirmed via Dorst's reference list), **and Leitgeb 2017, *The Stability of Belief* (OUP), 95%.** Belief as supersets of a P-stable core, and the conditions for closure plus a Lockean threshold.
- **Lin & Kelly 2012, "Propositional reasoning that tracks probabilistic reasoning", *JPL* 41(6): 957–981.** 95% (seen in Easwaran's reference list). Acceptance via a probabilistically selected core.
- **Easwaran 2016, "Dr. Truthlove", appendix §D (published lettering).** Flags additivity as "a deeper challenge" and invites alternative schemes. Verified in the preprint.
- **Kim & Wang 2024, "Credence and Belief: Distance- and Utility-based Approaches", *Phil Sci* 91(3): 759–779.** 90% (search listing). Utility-based bridge principles; not cited.
- **Joyce 2009, "Accuracy and Coherence: Prospects for an Alethic Epistemology of Partial Belief".** 99% (Dorst's references). The holism worry that §4.2 answers; not cited.
- **Fitelson 2012, "Accuracy, Language Dependence, and Joyce's Argument for Probabilism", *Phil Sci* 79(1).** ~85%. The language-dependence objection behind the single most serious problem.

No prior statement of the record measure, or of the quantifier-gap and content-gap diagnosis, turned up in my searches.

## Claims that look false, misattributed or unverifiable
1. **False.** §5: "At the second it is the set of consequences of 'B wins'" (Major 3).
2. **False given ME.** §4: "BI is stronger than … the ratio … background-independent". §6: "Theorem 1 concerns the latter, stronger condition" (Major 2).
3. **Overstated.** "Together, these two assumptions recover separability": this holds for a single state-independent A, not for Dorst's state-indexed A_{B0}.
4. **Mis-credited.**
   - Corollary 2 is presented as Dorst's extension; Dorst credits it to Easwaran §G.2.
   - Filtering is credited to Holguín §10; the canonical source is D&M 2022, with Levi-style antecedents.
5. **Novelty overstated.** "Here that behavior is obtained within an accuracy-maximizing model": D&M 2022 already derive non-monotone guesses from expected truth-directed value.
6. **Unverified.**
   - Holguín section numbers §5 and §10 (the horse race and the non-monotonicity claim are confirmed).
   - Wang 2025's "§§2 and 6", "nonadditive utility" and "convexity constraints".
   - Rothschild's Erkenntnis volume and pages.
   - The enumeration results in fns 2, 4 and 5, which are consistent with my hand checks.

## What is genuinely good (be specific: revisions must preserve this)
- **The quantifier-gap diagnosis is exactly right.** It is tied to Dorst's own sentence "this assumes only that A_{B0} is well-defined" (p. 193). Well-definedness gives a world-indexed increment, while the proof of Prop. 4 uses a world-independent one. Keep this at the front.
- **The content-gap diagnosis is right.** Dorst's proof of Prop. 5 sets T_p := T_p^{B−} for an arbitrary B−, which is a non sequitur. Dorst himself separates holism from order (p. 195).
- **The record measure is the right kind of countermodel.** It is minimal, alethic and state-independent, and it meets every stated §4.2 condition. Theorem 2's explicit interval (verified) shows the result is not knife-edge on a fixed space.
- **Theorem 3's Φ-characterization is correct.** It has a three-line proof and makes every optimum checkable by hand. "Core-relative Lockeanism" is an illuminating description of what an all-true premium does.
- **Theorem 1(a) is a clean diagnostic.** It isolates the only room ME leaves for holism: a world-independent κ.
- **Calibration and accuracy.** The negative claim is carefully calibrated (Separability is not claimed to be necessary), and the engagement with Dorst is page-accurate.

## Literature check

I used 12 web calls; several fetches failed and are recorded below.

1. **WebSearch: Wang 2025, "Credence and Belief: Epistemic Decision Theory Revisited".**
   - Found the PhilPeople listing: *Philosophical Studies* 182(5): 1433–1465 (2025).
   - The abstract describes using epistemic decision theory to bridge credences and deductively cogent binary beliefs. It revisits Hempel's and Levi's theories and adds the norm that binary beliefs maximize expected utility given credences. This is consistent with the essay's description.
   - **Not confirmed:** "§§2 and 6", "nonadditive utility", "convexity constraints", and the issue number "5–6".
   - Also surfaced Kim & Wang 2024 (*Phil Sci* 91(3): 759–779), which the essay does not cite.
2. **WebSearch (extended): critiques of Dorst §4.2, Sequence-Irrelevance, or holism counterexamples.**
   - No prior critique of Prop. 5 or of the T^{B0}_p step was found.
   - It surfaced a 2025 PhilSci-Archive paper on Dutch strategies and the "Easwaran–Dorst theorem". As far as the snippet shows, it concerns the separable result.
3. **WebSearch, then extended WebSearch: Dorst & Mandelkern, "Good Guesses".**
   - Confirmed *PPR* 105: 581–618 (2022; online 2021).
   - Guessing is modelled as an accuracy–informativity trade-off: maximize expected answer-value E(p) = P(p)V⁺(p) + P(¬p)V⁻(p), with truth-directed V. Applications include belief.
   - **Not confirmed in this run:** the "Filtering" constraint.
4. **Holguín 2022 (four fetches and one search).**
   - Michigan Publishing was bot-blocked, PhilPapers returned 403, and both author-site PDFs returned 404.
   - A search snippet **confirms** the horse race (40/35/25 versus 45/50/5), the thesis that rational thinking is non-monotone in credence, and the argument that sophisticated Lockeanism needs brute stipulations coordinating proposition-sensitive thresholds.
   - **Not confirmed:** the §5 and §10 locations, any discussion of filtering, and closure of thinking under entailment.
5. **Easwaran 2016 (one search and one fetch; I read the circulated preprint at fitelson.org).**
   - Noûs 50(4): 816–853 confirmed.
   - Preprint Appendix C, "Numerical vs. ordinal scoring", is apparently the published §D that Dorst cites; the lettering is shifted by one. It calls additivity "a deeper challenge to the framework" and says "Further investigation of alternative ordinal ranking schemes … would be quite helpful here."
   - Preprint Appendix F.2, "Different values", is Dorst's §G.2. It says that with varying values the ban on believing contradictory pairs and the single-premise closure requirement "no longer hold in full generality".
   - No record-type premium appears.
6. **Rothschild (one fetch; I read the June 2021 preprint).**
   - The scoring is additive. Fn. 18: "The additivity assumption … is defended by Dorst (2019)."
   - §8.2: "Most interesting, I think, would be to see what can be found when the additivity assumption is weakened." **The essay's attribution is confirmed.**
   - **Not verified:** Erkenntnis 88(5): 1979–1995.

**Dorst 2019 (packet source): attributions confirmed.**
- Mind 128(509): 175–211.
- Theorem 1 and Corollary 2 are identical to Easwaran §§3.2 and G.2 (p. 183).
- Accuracy First permits inconsistent, non-closed and empty states (p. 183).
- The exam analogy for Separability (p. 184).
- Conservativeness |T|<|F| and τ = −F/(T−F) (p. 185).
- Corollary 2 (p. 189), and Variable Conservativeness with Prop. 3 (pp. 190–191, 205).
- The construction of T^{B0}_p and F^{B0}_p, and "this assumes only that A_{B0} is well-defined" (p. 193).
- Prop. 4 and the wording of Sequence-Irrelevance, with the God example (p. 194).
- Prop. 5 and "no holist ever thought … order" (p. 195); the proofs (pp. 206–207).
- "Read off" and the "best guesses" gloss (§§4.1, 5, 5.1).
- The quoted "the" increment matches "Write t as T^{B0}_p—the value…".
- **One mis-credit:** Corollary 2.

**Named from knowledge, not web-checked:**
- Levi 1967, Leitgeb 2014, and Joyce 2009: bibliographic details confirmed via Dorst's reference list.
- Lin & Kelly 2012: confirmed via Easwaran's reference list.
- Leitgeb 2017 and Fitelson 2012: from memory.
- Surveys of belief accuracy were not checked.

## Proof check

**Central case.** T=1, F=−2, β=3, τ=2/3, e_p = 3C(p)−2. Optima are computed via Theorem 3.

- **At C = (0.70, 0.15, 0.15).**
  - e-values: {1} 0.10; {12},{13} 0.55; W 1; {2},{3} −1.55; {23} −1.10.
  - Φ-values: {1} 4.30; {12},{13} 4.10; W 4.00; ∅ 2.20; {2},{3} 2.00; {23} 1.90.
  - The unique optimum is {1,12,13,W} = 4.30 ✓.
  - The runner-up is 4.20 ✓. It is {12,13,W}, which has the same core and lacks only {1}, so the margin is e_1 = 0.10.
- **At C′ = (0.75, 0.01, 0.24).**
  - e-values: {1} 0.25; {12} 0.28; {13} 0.97; W 1; negative otherwise.
  - Φ-values: {13} 4.94; {1} 4.75; W 4.00; {12} 3.56; {3} 2.69; ∅ 2.50; {23} 1.75; {2} 1.31.
  - The unique optimum is {13,W} = 4.94 ✓. The runner-up is {1,12,13,W} = 4.75 ✓; the margin is 0.19.
  - The C′ optimum also omits {w1,w2}, although its credence 0.76 exceeds τ.

**Theorem 2.**
- **Constants.** c1−c0 = T/(2D+β), c1−τ = βT/(D(2D+β)) and 1−c1 = 2T/(2D+β), all ✓.
- **Placement of c0.** c0−τ = T(β−D)/(D(2D+β)), so c0<τ iff β<D. In the example β = D = 3, so c0 = τ = 2/3 and c1 = 7/9, and both 0.70 and 0.75 lie in (2/3, 7/9) ✓.
- **Φ-differences at C_c.** All ✓. Exactly, Φ(1)−Φ(13) − ½(Φ(1)−Φ(W)) = ½e_1 > 0.
- **Second half.** ✓ (Φ(13)−Φ(1) = β(1−c′)−2e_1; Φ(∅) = Φ(1)−βc′).
- **Caveat.** Uniqueness at ε>0 is not shown; see the Permission caveat.

**Theorem 3.** Correct.
- EA(B) ≤ Φ(∩B), with equality under the stated conditions.
- The B_X construction gives max EA = max Φ.
- The swap argument for (ii) needs uniform values, as stated.
- (iii) uses ∩B* = X*, which requires a unique Φ-maximizer; that is what "generic" must mean.

**Theorem 1.** Correct for a single state-independent A on the domain without complementary pairs; it is an integrability lemma. The missed corollary: since J_p^B = J_p, threshold-independence ⇔ BI under ME (Major 2).

**Four-world case.** ✓
- Φ({1}) = 3.58 + 1.86 = 5.44, where B* is the seven supersets of {w1} other than {w1}.
- The next core is Φ({1,2}) = 5.20. The best state containing {w1} scores 5.30 (e_1 = −0.14).
- C contains a tie, but the optimum is unique.

**Horse race.**
- First credences: Φ({A}) = 0.004+0.235+0.069+1+0.076 = 1.384 ✓, and the runner-up {AB,AC,W} = 1.380 ✓.
- Second credences:
  - e-values: e_B = 0.170, e_A = 0.087, e_AB = 0.567, e_BC = −0.097, e_AC = −0.180.
  - The optimum {B,AB,W} = 1.832 ✓ and the inconsistent Lockean state {A,B,AB,W} = 1.824 ✓.
  - The *description* in the main text is false (Major 3).
- Variable Conservativeness holds for singleton/doubleton pairs ✓; F_∅ is unspecified, which is harmless.

**Fn. 8.** ✓
- At (0.575, 0.2, 0.225): {1,12,13,W} = 1.45+0.5 = 1.95, ahead of {13,W} = 1.90 and the unclosed Lockean state {12,13,W} = 1.725.
- At (0.65, 0, 0.35): {13,W} = 2.5 beats {1,12,13,W} = 2.4.

**My refinement test.** Split w2 into two equiprobable worlds.
- At C′ = (0.75, .005, .005, .24): Φ({1}) = 7.25 > Φ({1,3}) = 6.91, so {w1} is believed.
- At C = (0.70, .075, .075, .15): Φ({1}) = 6.50 is maximal, so {w1} is believed.
- Non-monotonicity is lost.
- With m null worlds, Φ(X0) = 2^m Σ_{p0⊇X0} max(e,0) + βC(X0). The effective premium is therefore β/2^m.

**My greedy test (Major 5).** At C:
- {w1} first: Δ = −0.8, rejected, final state 4.20.
- {w1} last: Δ = +0.1, accepted.

## Top five changes (most important first)

1. **Make the record measure survive refinement, or stop leaning on it.**
   - Add the refinement computation to §6; it takes four lines.
   - Then choose one route:
     - (a) Relativize the score to the algebra generated by the contextually salient question. Dorst's A already takes a context-given P. Then show that Theorem 3's core structure is invariant under refinements that leave that algebra fixed.
     - (b) State "Refinement Invariance" as the premise the Lockean needs and show that it excludes the record measure. Then test, ideally prove, whether truth-directedness, Refinement Invariance and global MEA together force fixed thresholds. That would turn the defender's best reply into your result.
   - **To make room, cut:**
     - §5 "Third" (Dorst's reduction, about 120 words);
     - the second half of §1 ¶4;
     - fns 2, 4 and 5, compressed into one line.

2. **Add and position the missing literature.**
   - **§1 ¶3.** Cite Dorst & Mandelkern 2022, Levi 1967, Leitgeb 2014/2017, and Easwaran's §D invitation next to Rothschild's. Add two sentences stating the increment over D&M. They derive filtered, non-monotone guesses from expected truth-directed value over answers. You obtain core-plus-threshold structure from a purely alethic score over unrestricted belief states, which is what bears on Accuracy First.
   - **§5.** Add three or four sentences comparing Φ with D&M's expected answer-value and with Leitgeb's P-stable cores.
   - **Re-credit.** Credit filtering to D&M and Levi unless you verify Holguín §10. Credit Corollary 2 to Easwaran §G.2. Cite Joyce 2009 as the source of the holism worry.

3. **Replace the hedged account of Theorem 1 with its sharp corollary and dilemma.**
   - Delete the "BI is stronger than…" sentence in §4.
   - In §6, delete "Background-independent thresholds need not be identified… Theorem 1 concerns the latter, stronger condition."
   - Add a corollary: under ME, J_p^B = J_p, so threshold-independence ⇔ BI, and Dorst's derivation of Prop. 5 is valid iff A is separable on the domain.
   - Rewrite the §6 "belief-dependence" reply as a dilemma. Dorst's permitted variation in F_p^{B0} is a non-additive κ. If he admits it, fn. 8 refutes Prop. 5; if he rejects it, §4.2 collapses into Corollary 2.
   - Add one sentence noting that Theorem 1 covers state-independent A only.

4. **Fix or cut the horse race.**
   - One option: re-tune the values and re-verify the claim in exact arithmetic over all 256 states.
   - The other: report the true optimum {B, A∨B, W}, concede the closure failure, and delete "So the premium does what Holguín says sophisticated Lockeanism cannot".
   - Given margins of 0.004 and 0.008 and your own "narrow band" remark, I recommend cutting the paragraph and fn. 7. Keep one sentence linking Theorem 2 to Holguín's non-monotonicity.

5. **Pre-empt the two defender replies in §§2–3 with explicit arguments and numbers.**
   - **Scope.** Say that Prop. 5's thresholds are values of the measure, and so independent of credence within a context; this is how Dorst's proof works and what his §5 vacuity reply needs. Then contrast fixed-context non-monotonicity with Dorst's accommodation mechanism (§4.1: F is lowered "until it gets an answer"), and say why the former matters.
   - **Order.** Give the greedy example: {w1} first gives Δ = −0.8 and it is rejected; {w1} last gives Δ = +0.1 and it is accepted. Then argue that Prop. 4 ("only if") needs only local optimality of the final state, and that under Permission no sequence confers rationality, so the God worry does not arise.
   - **§3.** State the runner-ups and margins.
   - **To make room,** cut the disclaimers repeated in §1 ¶2 and §7 ¶2, which say the same thing three times.
