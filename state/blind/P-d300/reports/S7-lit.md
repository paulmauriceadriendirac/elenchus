# Referee report — S7 Philosopher of causation, chance and science (with G3 literature-expert standards; hostile mode) — P-d300

## Thesis and argument as I understand them (≤120 words)

The essay argues that normality filters on Halpern–Pearl (HP) witnesses cannot be applied as one transferable policy. Consider rankings of four local categories: default or deviant value, crossed with whether the value conforms to its equation. Four benchmark verdicts force the "license" family of such rankings (Thm 1). Any such ranking ties Doorbells' switch to Locusts' swarm under event or inertial coding, and ties Locusts to the short circuit under normal-course coding, so the three standard verdicts cannot all hold (Thm 2). Under modified HP, every uniform additive score that keeps Chain and Boulder counts the switch, because the switch's witness gain equals the sum of theirs (Thm 3); the older definitions escape. Seedlings is isomorphic to Doorbells with matching defaults (Prop 1). Prop 2 gives a sufficient condition for Andreas–Günther's failures, generalising Beckers.

## Verdict
Prize: not finalist
Journal recommendation: reject (in present form; a reframed short paper on a cross-definition switching dilemma could be publishable at a specialist venue)

## Scores
Clarity: 5 | Argument: 5 | Significance: 4 | Originality: 5 | Literature: 4 | Accuracy: 6 | OVERALL: 5

## The single most serious problem

**Locations:** §2 (definition of "local uniform ranking"); §4, Theorem 3, "The definition restriction matters" and the "diagnostic" paragraph; §7, Objection 1; §8.

**Uniformity does all the work, and the essay never confronts the published reasons for abandoning it.** Every negative result needs one ranking, or one set of category scores, shared by every variable in every model. The theorists it targets disown this:
- Halpern and Hitchcock (2015) call their rules "a few rough-and-ready guidelines" (arXiv p. 20).
- They endorse cross-variable comparisons where "such a comparison clearly seems warranted" (p. 32).
- They disclaim concern "with determining what the 'right' normality ordering is" (p. 26 fn. 13).

Their typicality is statistical, prescriptive or functional, so it is mechanism-specific from the outset.

**The cheapest escape from Theorem 3 is not the one the essay costs.** Penalise frozen defaults by mechanism: a pressed button whose circuit fails to ring the bell is far rarer than a hiker who fails to duck. With c_L < a ≤ c_K (and r + 2a − 2b ≥ 0), Chain, Boulder and Doorbells all come out right. The essay's "explicit cost" paragraph instead costs unequal root bonuses (r_C vs r_T), a less natural relaxation.

**Even the essay's strongest material meets a published non-uniformity it never discusses.** A parenthesis after Theorem 2 notes that, under modified HP and event coding, Suzy's witness in late preemption has the same category profile as the Doorbells switch. So does Hall's LT/RT, which Halpern (2015, p. 8) excludes by normality. Separating them needs a non-anonymous judgement, and one has been published. Beckers and Vennekens (2018), as invoked by Xiao and Xiong (2026, p. 8), hold that an agent's backup ("the supervisor's shooting accuracy") is "far more uncertain than the breakage of a sturdy track". The essay has not shown that dropping uniformity is costly until it shows this asymmetry fails somewhere. Seedlings, whose backup is a near-certain biological process, is the obvious test.

**The essay also misreads its own evidence about the older definitions** (Major problem 1). Its boundary score escapes Doorbells under original/updated HP. But it counts the flip as a cause in Halpern's own LB/RB switch (gain +1) and in the both-tracks-blocked variant (gain +3). In general g_SV = g_GP + r.

**Why it matters.** As framed, the essay proves impossibilities for a policy its targets disown, ignores the published case for the relevant non-uniformity, and misidentifies which HP variant fails where. The result it is close to would matter, but the essay does not state it: under event coding, every uniform normality filter, componentwise or additive, that keeps genuine prevention, Chain and Boulder counts some switch as a cause under each of the three HP definitions.

## Major problems

1. **The essay mislocates the additive obstruction: the older definitions fail other switches (§4 "The definition restriction matters"; §8).**
   - *Problem.* From its boundary score (2, 0, −1, −5, −3) the essay infers that "the obstruction therefore arises from uniform aggregation together with the modified contingency restriction", and that it "is absent from the original and updated definitions". That is true of the Doorbells obstruction only. Under the older definitions the same score counts the flip as a cause in two of Halpern's own switch representations:
     - LB/RB with tracks clear: witness [F←0, LB←1], gain a − b = +1;
     - Schumacher's both-tracks-blocked variant: witness [EF←0, LB←0], gain 2r + b − a = +3.
   - Halpern (2015, pp. 7–8, crediting Schumacher 2014) cites the second case as the reason to prefer the modified definition. Xiao & Xiong (2026, Obs. 1) use it against the Halpern–Hitchcock definition.
   - In general, under event coding, g_SV = g_GP + r. So every uniform additive score with r > 0 that accepts genuine prevention counts the both-blocked flip under the original and updated definitions. For componentwise rankings, l ≥ n suffices, and Theorem 1 forces l ≥ n.
   - My recomputation of the boundary score under the original and updated definitions (gain = witness score minus actual score; admitted iff ≥ 0):

     | Case | Gain | Verdict |
     |---|---|---|
     | Genuine prevention | +1 | cause |
     | Chain | +4 | cause |
     | Boulder, via the (0,1,0,1) witness | 0 | cause |
     | Short circuit | −1 | not |
     | Bogus prevention | −1 | not |
     | Overdetermination | +5 | cause |
     | Suzy, via [ST←0, BT←0] | +6 | cause; Billy has no AC2(b)-valid witness |
     | Locusts, via the rain witness, AC2(b) satisfied | +1 | cause |
     | Doorbells | −1, the only valid witness | not |
     | Hall's LT/RT | −1 | not |
     | Halpern's LB/RB switch, tracks clear | +1 | **cause (error)** |
     | LB/RB switch, both tracks blocked | +3 | **cause (error)** |

   - *Why it matters.* The essay's lesson — that the obstruction is a cost peculiar to the modified definition — is wrong as stated. The correct result is stronger: a dilemma across all three definitions. The essay cites Halpern (2016, pp. 90–91), where (per Xiao & Xiong, who cite p. 90) the both-blocked variant is discussed, yet it never tests that variant. Appendix B names only the LT/RT model from Halpern's Ex. 3.9, so the battery evidently omits the LB/RB representations.
   - *Fix.* Add the LB/RB and both-blocked switches to the battery and state the unified dilemma (Top five changes, item 1).

2. **Theorem 2's contrast case is one the essay's own §5 undermines (§4, Locusts; §5).**
   - *Problem.* Under event or inertial coding, Locusts' drought equation D = ¬Q∧¬S produces a deviant death from all-default parents. The essay admits in §5 that this violates Hitchcock's (2007) Principle of Sufficient Reason. A default theorist in Hitchcock's line will reject the model, not accept the impossibility. Under the two normal-course codings, the destruction X = 1 is the *default*, which is where the "swarm caused it" judgement is weakest (Objection 3 concedes this).
   - *Why it matters.* Theorem 2 constrains only theorists who accept a model their own principle rejects, or a coding that makes the target verdict contestable.
   - *Fix.* Drop Theorem 2(b) and the fourth coding. Replace Locusts with late preemption under modified HP (the profile identity), which needs no contested verdict. Flag the PSR violation at Theorem 2 if Locusts is kept.

3. **Prop 1 is trivial, and the premise that would make it bite is conceded (§5, §7 Objections 2–4).**
   - *Problem.* Prop 1 follows from isomorphism (Objection 4 concedes this). Its interest depends on the swarm and the switch deserving opposite verdicts at the coarse grain, and Objections 2–3 give that up: a time-indexed outcome separates them. The contrast tracks event individuation and fragility (timing and manner of the destruction), a familiar diagnosis of switching versus preemption.
   - *Why it matters.* What §5 actually shows is that default assignments cannot recover information the model omits. Halpern (2016, §4.1), which the essay cites, already explains this, and the default-sceptical literature argues it (see Prior work).
   - *Fix.* Either defend the coarse-grain contrast with a test case — a Seedlings variant in which swarm and drought would destroy the seedlings at the same time and in the same manner — or compress §5 to a short illustration of the trigger rule, keeping the postman variant.

4. **Andreas–Günther (A&G) analysis misidentifies the mechanism (§1, §5, §6).**
   - *Problem.* For Seedlings and Doorbells, A&G's negative verdicts come from their *structural* conditions, (2), (3) and (5) (Beckers's (C1)–(C4)), not from deviancy. The shared enabling root (P, or M) cannot be in F′ without entailing the effect, given the descendants' equations that (5) requires. Without it, (3) fails. The same holds for A&G's own Simple Switch (A&G 2024, p. 25: "Condition (5) thus prohibits…"). Beckers (2026, p. 10) says the same of their current definition, AG7 ("due to the absence of A").
   - *Consequences.*
     - "Both of Andreas and Günther's deviancy conditions say neither" (§5) is true of the verdict but suggests the wrong cause.
     - The §6 discussion of reclassifying events and absences is beside the point for Seedlings.
     - For A&G, Seedlings is a counterexample that holds *whatever the defaults* — a stronger point the essay misses.
     - §1's "A&G's deviancy condition does the corresponding work … as Beckers (2026) shows" overstates Beckers's role. Beckers *reports* that A&G's own 2024 papers need deviancy for the two *alternative* switch models (p. 11).
   - *Fix.* State the mechanism exactly.

5. **A directly relevant 2026 definition and the default-sceptical literature are missing, and Gallow's theory goes untested (§1, §3, §5, §7).**
   - *Xiao & Xiong 2026.* Published 5 May 2026, it adds an "availability" condition to Hitchcock's active-route definition: the witness world must not "violate the structural equations of the model". Their own early-preemption verdict requires reading availability with the other exogenous conditions held fixed. On that reading it is the essay's *conformity* ranking imposed as an absolute filter on actual-value witnesses.
     - The essay's Lemma then implies that every cause under their refined definition (RHIT) is a root but-for cause.
     - That predicts, in general, the cost they concede case by case (no early-preemption causes).
     - It also predicts one they miss: the Boulder ducking is a non-root, so it cannot be a cause.
     - Their headline table omits exactly the benchmarks that the essay's Theorem 1 and Lemma say this policy must fail.
     - The essay should cite it as a live, published target.
   - *Default-sceptical literature, not cited:*
     - Blanchard & Schaffer 2017, which A&G 2024 discuss on p. 27 of the essay's own source text;
     - Menzies on counterfactual isomorphs;
     - the Synthese article doi 10.1007/s11229-023-04101-w, whose abstract says conjoined isomorphs produce cases normality ascriptions cannot resolve;
     - Hitchcock 2009, which challenges the early-preemption/switch distinction;
     - Beckers & Vennekens 2018, whose reliability asymmetry is the main published rival to uniformity.
   - *Gallow's theory untested.* Doorbells is borrowed from Gallow (2021), whose central thesis is model-invariance across exactly the four-valued versus binary switch representation the essay simplifies. Yet Gallow's own default-based theory is never tested on Seedlings or Doorbells. If its verdicts depend only on equations, values and defaults, Prop 1 makes it deny the Seedlings swarm — the most interesting application, and it is not drawn.
   - *Fix.* See Top five changes, item 4.

## Minor problems

- **Value-only ranking misattributed** (§2). The ordering Halpern and Hitchcock (2015) "consider and reject" on p. 35 is not the essay's value-only ranking. Theirs ignores the outcome's value, and on their own reasoning it makes the antidote a cause ("the modified theory still makes A = 1 an actual cause"). The essay's value-only ranking scores the outcome by value, so it makes the antidote a *non*-cause (Table 1, short-circuit row). Their real point is that P's typicality must reflect how P depends on A. That point supports the essay, but it is not this ranking.
- **"The same relabelling … would undo their treatment of bogus prevention"** (§6) is unsupported. Escaping Prop 2 needs the *root* ¬Q (no rain) to be deviant. A&G's plant-death question concerns a non-root, which condition (4) never inspects. Nothing forces the same treatment of absent poison.
- **Prop 2's increment is overstated.** Beckers (2026, p. 2) already states the general diagnosis: A&G's accounts give "the wrong verdict on cases of Early Preemption for which the backup-process is not deviant". Prop 2 formalises this; credit it explicitly.
- **The fourth coding is candidate-relative.** "Normal course given the background" makes the normality ordering vary with the query. Halpern and Hitchcock's ⪰ is part of the model, so this is not a normality ordering in their sense.
- **Root defaults under inertial coding are never stated** (Theorem 2(a) proof). The proof fixes only non-root defaults. If Doc's switch position is a standing state, T = 1 is the default and the Doorbells/Locusts equivalence fails. Stipulate that the setting is a change.
- **Size of the license family.** Of the 75 weak orders, 2 satisfy the conditions, as stated. But of the 355 preorders, 5 do (3 non-total). Say so.
- **Appendix A (iv)** omits n ≥ l for the second Boulder witness. This is harmless given (ii).
- **"Unlicensed absence"** (§3) for H&H's frozen backup is, in the essay's own taxonomy, a frozen default (f), not u.
- **Theorem 1 is close to definitional.** Each benchmark contributes one inequality, so "calibration" oversells it.
- **Paraphrase of A&G's condition (4)** (§6). "Does not by itself entail the effect" should be "does not entail E together with L′". Condition (4) also requires C itself to be more deviant than ¬C.
- **Unreproduced trigger-rule claim.** "Under the modified definition it errs … on the switch": on my computation, both Doorbells and LT/RT come out right under the modified definition with the trigger rule. Say which switch fails.
- **Citations.** Hall (2007) is in the references but never cited in the text. The train story is Hall (2000), which is not listed. Halpern 2015's Ex. 3.10 uses Assassin, not "a second bodyguard"; the conspiring-bodyguards version is H&H 2015, pp. 34–35.
- **Hedging empties the thesis.** "Faces constraints" in the thesis sentence, the last sentence of the abstract, and §7's concessions together make the contribution hard to state.

## Prior work this resembles (only if confident; author, year, title, confidence %)

- Halpern, J. Y. 2016. *Actual Causality*, MIT Press, §§4.1, 4.7; pp. 90–91 on switch models, including (per Xiao & Xiong) the both-blocked variant. Cited by the essay. 95%.
- Halpern, J. Y. 2015. "A Modification of the Halpern–Pearl Definition of Causality", arXiv pp. 7–8. Reports Schumacher's (2014) both-tracks-blocked problem for the original and updated definitions with normality, and uses it to motivate the modified definition. Cited, but this passage is unused. 99% (read).
- Halpern & Hitchcock 2015, "Graded Causation and Defaults", arXiv pp. 34–37. Isomorphic patterns separated by normality; the intentions-variable move; the explicit conjecture (p. 37) that such variables can always be constructed. Cited, but the conjecture is not; the essay's Lemma bears directly on it. 99% (read).
- Xiao, Z. & Xiong, W. 2026. "A refinement of the Hitchcock definition of actual causation", *Humanities and Social Sciences Communications* 13: 1088. Adds an "availability" condition to Hitchcock's active-route definition: the witness world must violate no structural equation. This is exceptionless conformity on actual-value witnesses. It does not anticipate the essay's results but bears on them (see Literature check). 99% (read in full).
- Blanchard, T. & Schaffer, J. 2017. "Cause without Default", in Beebee, Hitchcock & Price (eds.), *Making a Difference* (OUP). Argues default-relativity is unnecessary and that aptness conditions do the work. That is the essay's Objection 2 territory. 90% (confirmed by A&G 2024 p. 27 and search).
- Menzies, P. 2017. "The Problem of Counterfactual Isomorphs", in *Making a Difference* (OUP). Title confirmed by search; venue from memory. 75%.
- Synthese article, doi 10.1007/s11229-023-04101-w (2023). Abstract (search snippet): incorporating normality "was supposed to handle isomorphs. It doesn't—conjoining isomorphs can produce cases that such ascriptions cannot resolve." The closest prior statement of the essay's general thesis. Title and author not retrieved. Existence 90%.
- Hitchcock, C. 2009. "Structural Equations and Causation: Six Counterexamples", *Phil Studies* 144: 391–401. Uses "Extended Switch" to challenge the early-preemption/switch distinction (per Beckers 2026, p. 10). 90%.
- Beckers, S. & Vennekens, J. 2018. "A Principled Approach to Defining Actual Causation", *Synthese* 195: 835–862. Distinguishes early preemption from switches by the reliability of the backup mechanism (as reported by Xiao & Xiong 2026, p. 8). This is the published rival to the essay's uniformity assumption. 90%. Also Beckers & Vennekens 2017, "The Transitivity and Asymmetry of Actual Causation", *Ergo* 4 — 85%.
- Halpern & Hitchcock, compact-representations companion paper. Cited as "2012" in H&H 2015 p. 20; I believe it was published as "Compact Representations of Extended Causal Models", *Cognitive Science* 37 (2013). It derives world normality from per-variable typicality and is the nearest formal precursor of the essay's "local uniform rankings". 80% on venue and year.
- Paul, L. A. & Hall, N. 2013. *Causation: A User's Guide* (OUP). Switching, preemption and neuron-diagram isomorphs. 95%.

## Claims that look false, misattributed or unverifiable

- **False/misattributed:** "Halpern and Hitchcock (2015, 35) consider and reject this [value-only] ranking." Their rejected ordering yields the opposite verdict on the very case (see Minor problems).
- **Misleading diagnosis:** §4, "The obstruction therefore arises from uniform aggregation together with the modified contingency restriction", and §8, "This obstruction is absent from the original and updated definitions". Both are true of the Doorbells obstruction only. Under the older definitions the essay's own boundary score counts the flip in Halpern's LB/RB switch (+1) and in its both-blocked variant (+3), and g_SV = g_GP + r in general.
- **Overstated:** §1, "A&G's deviancy condition does the corresponding work in their theory, as Beckers (2026) shows." In A&G 2024 the Simple Switch is handled by (5) and (2) (p. 25). Beckers reports, rather than proves, that A&G need deviancy for two *alternative* switch models (p. 11), and he says their current definition handles the Simple Switch structurally (p. 10).
- **Misleading mechanism:** §5, "both of Andreas and Günther's deviancy conditions say neither". The verdict is driven by structure, not deviancy.
- **Unsupported:** §6, "the same relabelling, applied to the poison-free coffee, would undo their treatment of bogus prevention."
- **Increment overstated:** §6, "I add … a condition that predicts the failure." Beckers (2026, p. 2) states the general condition informally.
- **Unverifiable (no access):**
  - Gallow 2021, pp. 84–86: Doorbells, the four-valued switch, and the p. 85 quotation. Bibliographic details confirmed.
  - All Halpern 2016 pinpoints: Ex. 3.2.6 (pp. 84–85); Thm 4.4.4(b) (p. 121; proof pp. 133–134); §§3.2, 3.3, 3.5, 4.1, 4.7, 5.2.2; pp. 38–39, 83, 85–86, 90–91, 97–102, 108–111, 124–127, 144–145, 149–150.
  - Hitchcock 2007, pp. 506–508 (inertial coding; PSR wording).
  - Appendix B: 36 queries in 25 models; 2,130 and 3,195 comparisons; 41 random models; reproduction of Halpern's Exs. 3.3, 3.4, 3.9, 3.10.
  - The trigger-rule claim that it errs "on the switch" under modified HP. I could not reproduce it.

## What is genuinely good (be specific: revisions must preserve this)

- **Exact, checkable models with correct computations.** I re-derived every entry of Table 1 by hand, under all three definitions where relevant, and every one matches. Theorems 1–3, the Lemma and Prop 2 are valid.
- **The additive identity is a real finding.** g_T = g_C + g_B, with the boundary counterexample, correctly shows that the *Doorbells* obstruction depends on the modified definition's actual-value contingencies. Combined with the both-blocked switch, where the older definitions fail by an equally simple identity, this yields a clean dilemma across all three definitions — the best result within the essay's reach.
- **The Lemma links H&H's programme to the modified definition.** H&H propose intentions variables and conjecture (p. 37) that equations can always be made typically obeyed by adding variables. Under modified HP, exceptionless conformity leaves only root but-for causes, so the conjecture's manoeuvre would eliminate preemption causes. The same Lemma explains, in general, the cost Xiao & Xiong (2026) concede case by case for RHIT, and exposes one they miss (the Boulder ducking). Sharpen this by citing p. 37 and Xiao & Xiong.
- **The postman variant (§5) is a good diagnostic.** It shows that the trigger rule tracks the default status of the shared enabling condition, not the switch/preemption contrast.
- **Prop 2** cleanly generalises Beckers's Backup 2 without a moral norm, and its proof is correct against both A&G's (4)/(5) and Beckers's (C4)/(C5).
- **Scholarship is unusually careful.** Of the pinpoints I could check (A&G pp. 13, 18, 19, 27, 28–29; H&H pp. 18–21, 26 fn. 13, 29 fn. 15, 34–37 incl. fn. 18; Halpern 2015 pp. 3–4, 7–8, Ex. 3.10; Beckers pp. 3–4, 9–11, Thm 2.2), all but the H&H p. 35 claim are accurate. The verbatim quotations from A&G (p. 27) and Beckers (p. 11) are exact. The increment over prior work is stated explicitly.
- **Latent strongest result.** The witness-profile coincidence of Suzy (late preemption), Hall's LT/RT switch and the Doorbells switch under modified HP. Promote it (see below).

## Literature check

**Searches and fetches (10 web calls).** Where WebFetch could not parse a PDF, I read the PDF copy the fetch tool saved.

1. WebFetch arXiv:2606.24832v1 (Beckers 2026). Read in full (14 pp.).
2. WebFetch arXiv:1505.00162v1 (Halpern 2015). Read pp. 1–9.
3. WebFetch arXiv:1309.1226 (Halpern & Hitchcock 2015). Read pp. 17–37.
4. WebFetch doi.org/10.1057/s41599-026-07470-y. Redirect to nature.com.
5. WebFetch nature.com. Login wall.
6. WebSearch for Gallow 2021 / Doorbells.
7. WebSearch for Xiao & Xiong 2026. No hit.
8. WebSearch for prior work on defaults, isomorphs, switch versus preemption (Blanchard & Schaffer; Menzies).
9. WebFetch Springer, doi 10.1007/s11229-023-04101-w. Login wall.
10. WebFetch Crossref API for 10.1057/s41599-026-07470-y. Metadata retrieved.

The coordinator later supplied the full text of Xiao & Xiong 2026 in the packet (source_xiao_xiong.txt). I read it in full; no web call.

**Prior statements of the thesis.**
- The general thesis — defaults and normality cannot resolve every isomorph, and default assignments need principled, independent motivation — is established. See Blanchard & Schaffer 2017; the 2023 Synthese conjoined-isomorphs article; Menzies; Halpern 2016 §4.7; Hitchcock 2009 on switch versus preemption. The essay disclaims novelty for the general isomorphism point but cites none of these.
- I found no prior statement of:
  - the four-category calibration (Thm 1);
  - the additive witness-gain identity under modified HP (Thm 3);
  - the frozen-witness Lemma as stated.

  Xiao & Xiong 2026 does not contain them either (below). Search depth was limited, so treat the novelty of these specific results as plausible, not established.

**Does Xiao & Xiong 2026 anticipate or bear on the essay's results?**

*It anticipates none of them.* It contains:
- no classification of normality rankings;
- no default codings;
- no additive or compensating scores;
- no isomorphic pair;
- nothing on regularity theories.

Its only formal result (Prop. 1: RHIT ⊆ HIT ⊆ MHP for singleton causes, plus a conditional link to the Halpern–Hitchcock definition) does not overlap the essay's theorems.

*It bears on them in four ways.*
1. **It is a live target for the Lemma.** RHIT's availability condition (Def. 12: an available world "does not violate the structural equations of the model") applies to Hitchcock-style witnesses, which freeze off-route intermediates at actual values. The authors' own verdict that the trainee is not a cause in early preemption (pp. 5, 8) requires the other exogenous conditions to be held fixed. Read that way, RHIT is the essay's conformity ranking made exceptionless on actual-value witnesses.
   - By the essay's Lemma, every RHIT cause is a root but-for cause.
   - RHIT therefore loses all preemption causes. In late preemption nothing causes the shattering: Suzy's witness is unavailable and Billy's route is inactive.
   - It loses Locusts' swarm.
   - It loses the Boulder ducking, a non-root whose witness violates K = F. X&X never test Boulder.

   Its verdicts on the essay's benchmarks coincide with the essay's Table 1 conformity column, minus conjunctive causes. X&X's "treatment of all these canonical problems" (their Table 1: switch, short circuit, bogus prevention, switch-variant) omits exactly the cases that the essay's Theorem 1 and Lemma show this policy must fail. The essay should cite RHIT as a concrete, published instance of the policy it constrains.
2. **Its Observation 1 undermines the essay's claim about the older definitions.** In the switch-variant (both tracks blocked; Halpern 2016 p. 90), X&X show that HH counts the flip as a cause because it allows non-actual contingencies. Under event coding I compute that every uniform additive score with r > 0 that accepts genuine prevention does the same under the original and updated definitions (g_SV = g_GP + r). Componentwise rankings do too whenever l ≥ n, which Theorem 1 forces. The essay's boundary score gives the flip +3. So the essay's claim that the additive obstruction "is absent from the original and updated definitions" is true of Doorbells only.
3. **Its remedy for early preemption is what the Lemma predicts.** X&X propose adding Accurate/Nerve variables and moving to nondeterministic models, following Beckers & Vennekens. Within deterministic acyclic models with actual-value contingencies, the Lemma says this works only by making the candidate a root but-for cause. Nondeterminism takes it outside the Lemma's scope, a response the essay's Objections section should address.
4. **It supplies the published motivation for the non-uniformity that escapes the essay's results.** Its report of Beckers & Vennekens — "the supervisor's shooting accuracy as far more uncertain than the breakage of a sturdy track" (p. 8) — is the asymmetry needed to separate Suzy from the switches under modified HP.

A minor slip in X&X, relevant only if the essay cites it: in bogus prevention they treat A as an "intermediate" between B and VS (p. 7), but A is a co-parent of VS, not a descendant of B.

**Attributions and quotations: confirmed.**
- *Andreas & Günther 2024, PPQ* (packet source):
  - deviancy condition (4), p. 13;
  - condition (5), p. 19;
  - Boulder "in the form presented" on p. 18;
  - the plant-death quotation, p. 27, verbatim;
  - bogus-prevention treatment, pp. 12–14;
  - comparison table, pp. 28–29;
  - preliminary definition (Def. 1) counts the Locusts swarm a cause (my computation, F′ = {¬D}).
- *Beckers 2026:*
  - existence and title ("Difference-Making without Making a Difference", arXiv 23 June 2026, sole author);
  - (C5) restricted to literals that are neither ancestors nor descendants, pp. 3–4;
  - Theorem 2.2, "AG7 iff AG5", p. 5;
  - Backup 2, pp. 9–11;
  - quotation "force us to conclude that trainee's action did not cause the outcome", p. 11, verbatim;
  - general claim about non-deviant backups, p. 2.
  - Note: Beckers's statement of AG5, which he labels A&G 2024b (the PPQ paper), includes the restricted (C5), whereas the PPQ text in the packet has the unrestricted (4). This is Beckers's discrepancy, not the essay's; the essay handles both versions.
- *Halpern 2015:*
  - the three definitions, pp. 3–4; the modified definition needs no AC2(b), p. 4;
  - the three-variable switch model, p. 7;
  - Schumacher's both-blocked problem, pp. 7–8;
  - LT/RT handled by normality, p. 8;
  - Ex. 3.10, short-circuit variant, p. 8;
  - Exs. 3.3, 3.4 and 3.9 have the stated subjects.
- *Halpern & Hitchcock 2015 (arXiv pagination):*
  - "problem of isomorphism", p. 37;
  - "undisturbed" system defaults, p. 18;
  - equations typically obeyed "unless there is some specific reason to think otherwise", p. 19;
  - guidelines on improving/worsening variables, p. 20;
  - AC2+(a) normality clause, pp. 20–21;
  - fn. 13, p. 26;
  - fn. 15 (neutralization variable PN), p. 29;
  - short circuit with two conspiring bodyguards, pp. 34–35;
  - exceptions in preemption and short circuit, p. 36;
  - fn. 18 (dam), p. 36;
  - intentions variable, pp. 36–37.
- *Gallow 2021:* bibliographic details confirmed (Phil Review 130(1): 45–96; doi 10.1215/00318108-8699682). The characterization "builds the default/deviant distinction into what a cause is" agrees with A&G 2024 pp. 12–13 and Gallow's abstract (transmission of deviant/non-inertial behaviour).
- *Beckers 2021 (CNESS, AAAI-35, 6210–6217)* and *Hall 2007 (Phil Studies 132: 109–136):* bibliographic details confirmed via Beckers 2026's bibliography.
- *Xiao & Xiong 2026:* bibliographic details confirmed (HSSC 13: 1088, online 5 May 2026). Its reference list confirms the H&H 2015 BJPS details (66(2): 413–457) and Hitchcock 2001 (J Phil 98(6): 273–299).

**Attributions and quotations: inaccurate.**
- "Halpern and Hitchcock (2015, 35) consider and reject this ranking" (value-only). See Minor problems.

**Attributions and quotations: imprecise.**
- §1, "as Beckers (2026) shows" (deviancy and the switch).
- §5, "deviancy conditions say neither" (the mechanism is structural).
- Halpern 2015 Ex. 3.10 described with "a second bodyguard" (that wording matches H&H 2015, not Halpern 2015).

**Not verified (no access within budget).**
- Gallow 2021, pp. 84–86, and the p. 85 quotation.
- Every Halpern 2016 page, example and theorem number.
- Hitchcock 2007, pp. 506–508.

**Important ignored work.** Xiao & Xiong 2026; Halpern 2015 pp. 7–8 on Schumacher's both-blocked case; Blanchard & Schaffer 2017; Menzies (isomorphs); the 2023 Synthese conjoined-isomorphs article; Hitchcock 2009; Beckers & Vennekens 2017/2018; H&H's compact-representations companion paper; Weslake 2015; Paul & Hall 2013; Hall 2000.

## Proof check

- **Theorem 1 — verified by hand.**
  - Witness enumeration for all three definitions:
    - genuine prevention: V n→l, needs l ≥ n;
    - Chain: I, Y l→n, needs n ≥ l;
    - short circuit: P l→u and V n→l, must fail;
    - Boulder: (1,1,0,1) with K l→f and H n→l; under original/updated also (0,1,0,1) with B l→u, K l→n and H n→l, which satisfies AC2(b) and AC2(b^u).
  - Conjunctive candidates I spot-checked ({A,P}, {A,V} in the short circuit) do not create causes under license rankings.
  - Counts: 75 weak orders, 2 qualifying, correct. Among the 355 preorders, 5 qualify.
  - Status: correct, but nearly definitional.
- **Lemma (frozen witnesses) — valid.**
  - A fully conforming witness world coincides, by acyclicity, with the solution under the root part of the candidate alone. The same world passes the same filter, so AC3 forces the candidate to be all roots.
  - It relies on the modified definition having no AC2(b) (confirmed, Halpern 2015 p. 4).
  - Application to Xiao & Xiong's RHIT: an RHIT witness is an actual-value witness (their Prop. 1: RHIT ⊆ HIT ⊆ MHP) whose world violates no equation. So the candidate is a root but-for cause. RHIT gets Boulder wrong (K = F is violated by K←0) and gets every preemption case wrong.
  - Status: correct and elementary. It bears directly on H&H's p. 37 conjecture, which the essay should cite.
- **Theorem 2 — verified.**
  - (a) Doorbells [T←0, L←0]: L n→f, R l→n, E l→n. Locusts [S←0, D←0]: D n→f, X l→n. Both need f ≥ n and n ≥ l.
  - The extra original/updated witnesses fail. In Locusts, Q←1 moves a root from default to deviant. In Doorbells, M←0 violates AC2(b), since [T←1, M←0] gives E = 0.
  - Conjunctive candidates:
    - {T,M} is never minimal, because M = 1 is a but-for cause.
    - {T,E} and {S,X} pass only if {E} or {X} alone passes.
    - {T,R} with M←0 satisfies AC2(b) but is non-minimal, because R = 1 alone is a cause via [R←0, M←0].
  - (b) Under both normal-course codings: Locusts D l→u and X n→l; short circuit P l→u and V n→l. Identical conditions. Confirmed.
  - Caveat: (a) needs the stipulation that T = 1 and S = 1 are changes (deviant) under inertial coding.
- **Theorem 3 (additive) — verified.**
  - Gains: g_C = r + 2a − 2b; g_B = c − a; g_T = r + a + c − 2b = g_C + g_B.
  - Under modified HP these witness worlds are unique. Freezing I or Y at 1, or H at 0, restores the outcome. In Doorbells, freezing R at 1 or E at 1 restores the barking.
  - The identity is a telescoping fact. Additive scores act as potentials, so (l→f) + (n→l) = (n→f).
  - Strengthening: Suzy's late-preemption witness [ST←0, BH←0] has transitions {ST +r, SH l→n, BH n→f, BS l→n}. Its gain is exactly g_T, and Hall's LT/RT witness [F←0, LT←0] has the same profile. So under modified HP and event or inertial coding, *any* variable-anonymous filter treats Suzy (as singleton cause), LT/RT and Doorbells alike.
- **Boundary counterexample (2, 0, −1, −5, −3) — the essay's stated claims are verified.**
  - Chain: +4.
  - Boulder: modified witness −5 (fails); original/updated witness (0,1,0,1) has gain r + d − b = 0 (passes) and satisfies AC2(b)/(b^u).
  - Doorbells: the only valid witness has gain −1.
  - Candidates containing T: {T,R} and {T,E} are non-minimal; {T,L} fails AC2(b) with M←0 and has gain −1 without it. So T is not even part of a cause.
  - Genuine prevention +1; Locusts via rain +1 (AC2(b): [S←1, Q←1] gives X = 1); short circuit −1.
  - Additional cases I computed: overdetermination +5, bogus prevention −1, Suzy +6 with Billy excluded, LT/RT −1.
  - **What the essay does not report:** under the original and updated definitions the same score counts the flip in two switch representations:
    - Halpern's LB/RB switch with tracks clear: [F←0, LB←1]; actual (F,LB,RB,A) = (1,0,0,1) scores 2r + b = 3, witness (0,1,0,0) scores 2r + a = 4; gain a − b = +1; AC2(b) and AC2(b^u) hold.
    - The both-blocked variant: [EF←0, LB←0]; actual (1,1,1,TA=0) scores a = 0, witness (0,0,1,TA=1) scores 2r + b = 3; gain 2r + b − a = +3; AC2(b): [EF←1, LB←0] gives TA = 0.
- **New identity: the switch-variant under the older definitions.** Under event coding and original/updated HP, genuine prevention's witness has gain g_GP = r + b − a, and the both-blocked flip's witness has gain g_SV = 2r + b − a = g_GP + r. Componentwise, the flip's witness passes iff l ≥ n: EF and LB return to default, RB is unchanged, and TA moves n→l. Under the modified definition the flip has no witness. This is the older-definition counterpart of Theorem 3.
- **Proposition 1 — immediate.**
  - Defaults are preserved under all four codings.
  - Fourth coding: Seedlings G/D/X defaults 0/1/1 correspond to Doorbells R/L/E 0/1/1.
- **Proposition 2 — valid** against A&G's (4) and (5) (pp. 13, 19) and Beckers's (C4) and (C5) (p. 4).
  - Locusts: the unique maximal F′ is {¬D}, which omits the normal root ¬Q, so (4) fails.
  - For Seedlings and Doorbells, A&G's negative verdict comes from (2), (3) and (5), not from (4).
- **Table 1 — every cell recomputed and confirmed.** That includes "C\* (modified only)" for Billy under the conformity ranking: ST alone fails under modified, so {ST,BT} becomes minimal; under original/updated, ST is a cause via BT←0. It also includes the split Doorbells verdict under the two normal-course codings: L l→u under the background coding.
- **Trigger-rule claims.** Confirmed under original and updated on the cases I checked. The "errs … on the switch" claim under the modified definition could not be reproduced.

## Top five changes

1. **State and prove the cross-definition switching dilemma, and make it the paper.**
   - *(a) Modified HP, event or inertial coding.* The witnesses for Suzy (late preemption), Hall's LT/RT and the Doorbells switch have identical category-transition profiles. So any variable-anonymous filter — componentwise, additive, or any function of the transition multiset — treats them alike. Chain + Boulder ⇒ Doorbells (the current Theorem 3) becomes a corollary.
   - *(b) Original/updated HP, event coding.* For the both-tracks-blocked switch, g_SV = g_GP + r; componentwise, l ≥ n suffices. So genuine prevention forces the flip to count.
   - *Result to state:* under event coding, no uniform normality filter keeps genuine prevention, Chain and Boulder while excluding every switch, under any of the three HP definitions.
   - Rewrite the §1 thesis and §8 to say this. Delete "This obstruction is absent from the original and updated definitions."
   - *Cut about 450 words:* Theorem 2(b), the "normal course given the background" coding, its Table 1 column and the note on the Doorbells row, and the related text in §2 and §4.
2. **Confront the non-uniform escapes and price them.**
   - *Replace* the root-bonus "diagnostic" paragraph (about 180 words) with three escapes:
     - mechanism-specific frozen-default penalties, which escape the Chain/Boulder corollary but not the profile identity;
     - Beckers & Vennekens's agent-versus-mechanism reliability asymmetry (as invoked by Xiao & Xiong 2026, p. 8), the published motivation for separating Suzy from the switches — test it on Seedlings (near-certain biological backup), on Doorbells and on LT/RT;
     - inertial coding of standing blockages, which defuses the both-blocked switch componentwise.
   - Show what each costs.
   - *Use the Lemma against a live target.* Xiao & Xiong's RHIT is exceptionless conformity on actual-value witnesses, so it admits only root but-for causes and loses Boulder and all preemption. Cite H&H's p. 37 conjecture beside the Lemma.
3. **Cut §5 and §6 to about a third of their length (saving about 700 words).**
   - Present Prop 1 as a one-line corollary of isomorphism.
   - Keep Seedlings only as a test of the trigger rule, with the postman variant.
   - Delete the "same relabelling" argument.
   - Correct the A&G mechanism: their structural conditions already exclude the Seedlings swarm.
   - Turn Prop 2 into a remark crediting Beckers (2026, p. 2) for the general diagnosis.
   - *Alternative:* keep Prop 1 only with an argued test case. Use a Seedlings variant where swarm and drought would destroy the seedlings at the same time and in the same manner. If the "swarm caused it" judgement survives, that is a datum; if not, drop the pair.
4. **Fix the literature and accuracy (about 300 words net).**
   - *Add and engage:* Xiao & Xiong 2026; Halpern 2015 pp. 7–8 (Schumacher's case); Blanchard & Schaffer 2017; Menzies on isomorphs; the 2023 Synthese conjoined-isomorphs article (doi 10.1007/s11229-023-04101-w); Hitchcock 2009; Beckers & Vennekens 2017/2018; H&H's compact-representations paper.
   - *Test Gallow's own theory* on Seedlings and Doorbells in one paragraph, since his model-invariance targets exactly the representation choice the essay makes.
   - *Correct:*
     - the H&H p. 35 value-only claim;
     - "as Beckers shows" → "as Beckers reports of A&G (2024a,b)";
     - cite Hall 2007 in the text, and add Hall 2000 for the train story;
     - the Halpern 2015 Ex. 3.10 description;
     - "unlicensed absence" → frozen default.
5. **Make it legible to the committee and cut hedges and apparatus (saving about 600 words).**
   - *Cut:*
     - the abstract's last two sentences;
     - §1's "The claims concern … remain possible";
     - the Objection 4 reply;
     - half of the Objection 2–3 replies;
     - Appendix B's narrative, compressed to one paragraph plus a code-availability note.
   - *State at Theorem 2* that Locusts violates Hitchcock's PSR under event coding, or drop Locusts in favour of late preemption.
   - *Stipulate* the inertial status of the roots in Doorbells.
   - *Add* one "why care" paragraph: what the dilemma shows about choosing among HP definitions.
   - *Net effect:* about 1,900 words cut and about 1,150 added, bringing the essay to roughly 5,100 words with a single decisive result.
