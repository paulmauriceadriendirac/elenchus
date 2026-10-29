# A4 v6 revision notes (final revision against S7-lit, P-d300)

Input: state/external/submission-additive-20261029/essays/03-Causation-v5.md (5,876 words).
Output: state/drafts/A4/v6.md, **5,521 words** (tools/wordcount.py strict; bibliography excluded; limit 6,000).
check_injection.py with judges file: no hard flags; soft flag = 8 mentions of Günther, all as citations of Andreas & Günther 2024 (checked against the PPQ text).

## v6 thesis (one sentence)

Under event coding, no anonymous (profile-only) normality filter that respects Pareto improvement can make genuine prevention and Suzy's late-preempting throw causes while counting no switch a cause, under any of the three HP definitions: under the modified definition Suzy's only witness has exactly the profile of the Tracks and Doorbells switching witnesses, and under the original/updated definitions the blocked-tracks flip's witness is genuine prevention's witness plus one default-restoring root (g_SV = g_GP + r).

## Computation (all new verdicts and identities)

Scripts in state/drafts/A4/v6_checks/: models.py (copied from v5 source), verify_additive.py (copied, unchanged), **v6_verify.py** (new), output **v6_verify_output.txt**. New models: Halpern's LB/RB switch (tracks clear), the both-blocked switch, late preemption, early preemption, Tracks (LT/RT), Doorbells, Locusts, Seedlings. All three HP definitions; all 355 preorders; every candidate subset; AC3 after filtering.
Key results: profile identity Suzy = Tracks = Doorbells under modified (unique witnesses); g identities symbolic (g_Door = g_Tracks = g_Suzy = g_Chain + g_Boulder; g_SV = g_GP + r); SV flip part of a cause iff l >= n (orig/upd; also modified via the {EF, LB} conjunction); dilemma: 0/355 preorders and 0/3,000 random additive scores under each definition (singleton and part-of-cause versions); calibration: 5 of 355 preorders (2 total orders); escapes (mechanism-specific scores, Sprinkler, Seedlings, inertial blockages, landslide variant); lemma on 400 random models (0 counterexamples); A&G with/without deviancy (Doorbells, Seedlings excluded structurally; Locusts excluded only by deviancy).
One finding beyond the report: under the modified definition the blocked-tracks flip is still *part of* a cause ({EF=1, LB=1}), admitted by every Pareto filter that keeps genuine prevention. Stated in §4 as a remark; the dilemma is stated for single candidates.
A mis-specified first run (inertial coding also applied to clear tracks in LB/RB) was corrected before use.

## Triage of the report

**Most serious problem (uniformity does all the work).** Accepted. Reframed as a result about *anonymous* filters (profile-only), with componentwise and additive as two instances; §2 motivates anonymity from H&H's own defaults and Halpern 2016, 149–150; §5 opens with the H&H disclaimers (pp. 20, 32, 26 fn. 13) and a regimented argument (P1–P3, C) whose conclusion is what the non-anonymous exceptions must contain. The root-bonus "diagnostic" paragraph is deleted; the mechanism-specific frozen-default escape (c_BH > c_L) is stated and computed.

Major 1 (older definitions fail other switches). Accepted; now Theorem 2 and the dilemma. Deleted "absent from the original and updated definitions". Boundary score retained only to show the horns are distinct (excludes Tracks/Doorbells under orig/upd, counts both LB/RB switches: computed).
Major 2 (Locusts violates PSR; normal-course coding). Accepted: Locusts removed from the main argument; Theorem 2(b), fourth coding and normal-course codings cut. Late preemption replaces Locusts (no contested verdict). Locusts survives only as a one-sentence instance of Beckers's diagnosis in §7.
Major 3 (Prop 1 trivial). Accepted: Prop 1 deleted as a proposition; the Seedlings isomorphism is one sentence used to test the reliability asymmetry, with the timing reply conceded explicitly. Postman variant and trigger rule cut (space; the trigger rule's claim was also the one the referee could not reproduce).
Major 4 (A&G mechanism). Accepted: §7 states that their final theory handles the simple switch structurally (A&G 2024, 25, condition (5) then (2)); Beckers *reports* the need for deviancy on alternative switch models (2026, 10–11); Seedlings/Doorbells excluded by the non-deviancy conditions (computed, both 2024 versions), hence "whatever deviancy is assigned". "As Beckers shows" removed. "Same relabelling" argument deleted.
Major 5 (literature; Gallow). Partly accepted. Added Xiao & Xiong 2026 (read in full; Lemma applied to RHIT, Def. 12 p. 5, Prop. 1 p. 6, concession p. 8), Halpern 2015 pp. 7–8 (Schumacher's case; quote "normality considerations don't help"), H&H p. 37 conjecture (quoted), Hitchcock 2009 (only as reported by Beckers 2026, 10), Beckers & Vennekens 2018 (only as reported by X&X 2026, 8), Blanchard & Schaffer 2017 (only as reported by A&G 2024, 27). Gallow: his Doorbells model and the right/left non-deviancy assumption (p. 86, quoted) are discussed as a representational, non-anonymous escape; I did not test his full theory on Seedlings (not enough of his definitions read in this pass; declined rather than guessed). Not added: Menzies (not read), the 2023 Synthese article (title/author not retrieved), H&H compact-representations paper (not read), Weslake 2015, Paul & Hall 2013 (not needed).

Minor points:
- H&H p. 35 value-only claim: fixed. v6 says only that H&H argue typicality must reflect how a variable depends on its parents (35); the value-only ranking is gone.
- Prop 2 increment: Prop 2 removed; Beckers credited for the general diagnosis (2026, 2).
- Fourth coding candidate-relative: cut.
- Inertial root defaults unstated: inertial coding now appears only for blockages (§5), stated explicitly; Objection 2 states what Theorem 1 needs of the coding.
- License family size: now "five of the 355 preorders, two of them total orders".
- Appendix A (iv): Appendix rewritten; calibration conditions stated in §4 with both Boulder witnesses noted.
- "Unlicensed absence": phrase removed.
- Theorem 1 near-definitional: calibration demoted to a paragraph supporting the profile identity.
- A&G condition (4) paraphrase: condition (4) no longer paraphrased.
- Trigger-rule claim: trigger rule cut.
- Citations: Hall 2000 added for the story; Hall 2007 cited in text for the LT/RT route model (per Halpern 2015, 8); Halpern 2015 Ex. 3.10 no longer cited; the conspiring-bodyguard short circuit is attributed to H&H 2015, 34–35. Hitchcock 2007 dropped (no longer used; inertial notion now cited to Gallow 2021, 86–87, read).
- Hedging: abstract's last two sentences, §1 caveat paragraph, Objection 4 reply and Appendix B narrative cut; thesis stated as a theorem-backed claim; one "why it matters" paragraph added (§1).

Top five changes: (1) done (Theorems 1–2, Corollary; Chain+Boulder now the telescoping identity in §4); (2) done (§5: mechanism-specific penalties, reliability asymmetry with Sprinkler and Seedlings tests, inertial blockages with landslide variant; Gallow's representational route; §6 Lemma vs H&H p. 37 and X&X RHIT); (3) done (§§5–6 of v5 reduced to ~1 paragraph each in §5 and §7); (4) done except Gallow-theory test (see above); (5) done.

## New references and verification

tools/verify_refs.py on state/drafts/A4/v6_checks/new_refs.json (results: new_refs_verification.md):
- Xiao & Xiong 2026, HSSC 13:1088 — VERIFIED (full text read: inbox/sources/xiao-xiong-2026-hitchcock-refinement.txt).
- Hall 2000, J Phil 97(4):198–222 — VERIFIED (cited for the story, per Halpern 2015, 7).
- Hall 2007 — VERIFIED (now cited in text).
- Hitchcock 2009, Phil Stud 144(3):391–401 — VERIFIED (registry year 2008 = online first; print 2009 as cited by Beckers and A&G). Attributed only as reported by Beckers 2026, 10.
- Beckers & Vennekens 2018, Synthese 195:835–862 — PROBABLE (registry year 2016 = online first; issue 2018 as cited by X&X). Attributed only as reported by X&X 2026, 8.
- Blanchard & Schaffer 2017 — VERIFIED (doi 10.1093/oso/9780198746911.003.0010; no page range given). Attributed only as reported by A&G 2024, 27.
Quotations checked word for word against retrieved texts: Halpern 2015 (pp. 7–8; two quotations), H&H 2015 arXiv (pp. 20, 32, 37), X&X 2026 (pp. 5, 8), Gallow 2021 (pp. 85, 86, 86–87), A&G 2024 (p. 26). Halpern 2016 pinpoints (84–85, 121, 133–134, 149–150, §3.3) rely on the 28 October book review (state/external/submission-book-review-20261028/Halpern-Originality-Review.md).
Web calls: 1 (one batch download of four PDFs; text extracts already in scratchpad from an earlier session were used).

## Residual risks
- "Anonymous" is my term; a referee may still regard the target as idealized. §5's regimented argument is the answer.
- Seedlings verdict is contestable at the coarse grain; v6 concedes the timing repair and draws only the weaker conclusion.
- The {EF, LB} part-of-cause remark under the modified definition is new and computed but not checked against Halpern 2016's discussion of the both-blocked case (pp. 90–91 were in the chapter read for the review, but this point was not checked there).
