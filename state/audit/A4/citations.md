# A4 v6 citation audit

Essay audited: `state/drafts/A4/v6.md` (strict word count 5,521 by `tools/wordcount.py`).
Date: 2026-10-29. Auditor: citation-auditor subagent.
State of the bibliography: no `state/candidates/A4/refs.json` exists. I built a full 13-entry file covering all 12 references, plus one entry for the book chapter-check, at the scratchpad path below and ran `tools/verify_refs.py` on it.
Per the task, I did not open `state/external/` or `relay/`. That means the 28 October Halpern-book review, which the reviser's notes rely on for every Halpern 2016 pinpoint, was not available to me.

## Sources actually compared

| Work | Copy used | Pagination used |
|---|---|---|
| Halpern & Hitchcock 2015 | arXiv:1309.1226 (only version, v1). Downloaded 29 Oct. | arXiv page numbers, which are printed on the pages |
| Halpern 2015 | arXiv:1505.00162 (only version, v1). Downloaded 29 Oct. | PDF page = arXiv page (the IJCAI format has no printed numbers) |
| Beckers 2026 | arXiv:2606.24832 (only version, v1), 14 pp. Downloaded 29 Oct. | Printed page numbers |
| Gallow 2021 | Duke UP journal PDF; text extract in the session scratchpad. A fresh download from the pgrim.org URL failed (connection reset). | Journal pages, read from the printed folios |
| Andreas & Günther 2024 | `state/ambitious/sources/andreas-gunther-2024-regularity.txt` | Journal page = PDF page + 1, confirmed from the running heads |
| Xiao & Xiong 2026 | `inbox/sources/xiao-xiong-2026-hitchcock-refinement.txt` | Article pages, read from the printed footers |
| Halpern 2016 | **Not retrievable.** The DOAB/OAPEN open-access copy is behind a bot wall, and MIT Press Direct returns 403. | none |

## Summary counts

- **References: 12.** All 12 are cited in the text, and every in-text citation has an entry. 10 are VERIFIED by the tool. 2 are NOT_FOUND by the tool (arXiv preprints, OpenAlex 429) and were verified by hand. 1 is a MISMATCH that is only the online-first year. Metadata problems: none. Optional additions: 2.
- **Quotations: 15 strings.** All 15 are word-for-word exact at the stated page. One splice drops the source's hedge and needs a fix (patch 3).
- **Attributions: 38 checked.**
  - Accurate: 30.
  - Oversimplified: 2 (patches 4, 6).
  - Inaccurate: 2 (patches 1, 2).
  - Unverifiable: 4 (Halpern 2016; patches H1–H5).
- **Pinpoints (page, example, section): 41 checked.**
  - Correct: 34.
  - Incomplete: 2 (patches 4, 5).
  - Unverifiable: 5 (Halpern 2016: 84–85 twice, 121/133–134, 149–150, §3.3).
- **Fetch request filed, high priority:** `requests/fetch/a4-audit-halpern-2016-pinpoints.md`.

## Step 1. Coverage

| Reference | Cited at | Year/spelling consistent | Note |
|---|---|---|---|
| Andreas & Günther 2024 | §2, §3 (Boulder), §5, §7, App. | yes ("Günther" throughout) | — |
| Beckers 2026 | §1, §7, §8 | yes | — |
| Beckers & Vennekens 2018 | §5 | yes | X&X cite "Beckers and Vennekens (2017, 2018)" for the argument. Citing only 2018, as reported, is acceptable. |
| Blanchard & Schaffer 2017 | §5 | yes | — |
| Gallow 2021 | §3, §5, §8 | yes | — |
| Hall 2000 | §3 | yes | — |
| Hall 2007 | §3 | yes | — |
| Halpern 2015 | §1, §2, §3, §4, §5, §8, App. | yes | — |
| Halpern 2016 | §1, §2, §4, §6, §8 | yes | Every pinpoint is unverifiable (Step 5). |
| Halpern & Hitchcock 2015 | §1, §2, §3, §5, §6 | yes | — |
| Hitchcock 2001 | §3. "Hitchcock's active-route account" in §6 is the same work, as X&X confirm. | yes | — |
| Hitchcock 2009 | §7, §8 | yes | — |
| *Halpern & Hitchcock [2010]* | implied in §8 ("takes from Halpern and Hitchcock") | **no entry** | Halpern 2015, 7 credits the blockage model to H&H **2010**, not 2015. A reader will take the reference to be H&H 2015. Patch 1. |
| *Schumacher [2014]* | §1, by name only ("he credits to Schumacher") | no entry | Acceptable, because the essay presents it as Halpern's credit. No patch. |

## Step 2. Existence and metadata

`verify_refs.py` output is in the session scratchpad (paths at the end). I also queried Crossref directly for volume, issue, pages and dates.

| Ref | Tool | Hand evidence | Verdict |
|---|---|---|---|
| A&G 2024, PPQ 105(1): 2–32, doi 10.1111/papq.12447 | VERIFIED | Crossref: vol 105, issue 1, pp. 2–32 | OK |
| Beckers 2026, arXiv:2606.24832v1 | NOT_FOUND (OpenAlex 429) | arXiv abs page: title "Difference-Making without Making a Difference", v1 only. The PDF names Sander Beckers (UCL). | OK |
| Beckers & Vennekens 2018, Synthese 195(2): 835–862 | MISMATCH (year) | Crossref: online 20 Oct 2016, print Feb 2018, vol 195, issue 2, pp. 835–862 | OK. Print year is standard. |
| Blanchard & Schaffer 2017 | VERIFIED | Crossref: OUP, 20 Jul 2017. A&G's reference list gives eds. Beebee, Hitchcock & Price, pp. 175–214. | OK. Optional page range: patch 7. |
| Gallow 2021, Phil Rev 130(1): 45–96 | VERIFIED | Crossref: 130(1), 45–96 | OK |
| Hall 2000, J Phil 97(4): 198–222 | VERIFIED | Crossref gives the first page only. X&X's reference list gives 198–222. | OK |
| Hall 2007, Phil Stud 132(1): 109–136 | VERIFIED | Crossref: matches | OK |
| Halpern 2015, arXiv:1505.00162v1 | NOT_FOUND (OpenAlex 429) | arXiv abs page: "A Modification of the Halpern-Pearl Definition of Causality", v1 only. Also published in IJCAI 2015, 3022–3033 (per A&G's reference list); not needed. | OK |
| Halpern 2016, *Actual Causality*, MIT Press | VERIFIED | Crossref: doi 10.7551/mitpress/10809.001.0001. Chapter DOI ...003.0003 is "Graded Causation and Normality". | OK. Optional DOI: patch 8. |
| H&H 2015, BJPS 66(2): 413–457 | VERIFIED | Crossref: matches. arXiv 1309.1226 has v1 only. | OK |
| Hitchcock 2001, J Phil 98(6): 273–299 | VERIFIED | Crossref first page 273. A&G's reference list gives 273–299. | OK |
| Hitchcock 2009, Phil Stud 144(3): 391–401 | VERIFIED (registry year 2008) | Crossref: online 11 Mar 2008, print Jun 2009, 144(3), 391–401 | OK |
| Xiao & Xiong 2026, HSSC 13: 1088 | VERIFIED | Crossref: vol 13, online 5 May 2026. The article footer reads "(2026) 13:1088". | OK |

## Step 3. Quotations

| # | Essay text | Source and page | Result |
|---|---|---|---|
| Q1 | "normality considerations don't help" | Halpern 2015, p. 8: "And now normality considerations don't help, since…" | exact, p. 8 |
| Q2 | "rough-and-ready guidelines" | H&H, p. 20: "we make do with a few rough-and-ready guidelines" | exact, p. 20 |
| Q3 | "occurring events are prima facie more deviant than their absences" | A&G, journal p. 26: "We have said that occurring events are prima facie more deviant than their absences (Section 4.1)." | exact, p. 26 |
| Q4 | "Doc's flipping the switch to the right was (along with Marty's pressing the button) a cause of the right bell's ringing, but it was not a cause of Einstein's barking" | Gallow, p. 85. The source has footnote 51 after "barking." | exact, p. 85 (only the apostrophes are normalized) |
| Q5 | "this becomes a non-problem" | Halpern 2015, p. 8: "With the modified definition, this becomes a non-problem." | exact, p. 8 |
| Q6 | "such a comparison clearly seems warranted" | H&H, p. 32: "…such a comparison clearly seems warranted in this case." | exact, p. 32 |
| Q7 | "the world where the train does not go on the left track despite the switch being set to the left is less normal than the actual world" | Halpern 2015, p. 8 | exact, p. 8 |
| Q8 | "the key distinction between the early preemption and the switch example lies in whether we take into account the possibility that the backup mechanism malfunctions" | X&X, p. 8 | exact, p. 8 |
| Q9, Q10 | "the supervisor's shooting accuracy" … "far more uncertain than the breakage of a sturdy track" | X&X, p. 8: "since it is quite plausible to regard the supervisor's shooting accuracy as far more uncertain than the breakage of a sturdy track, it is reasonable to expect that intuitions … are more prevalent" | **Each fragment is exact, but the splice ("since X is Y") drops "it is quite plausible to regard … as".** That turns X&X's hedged plausibility claim into a flat assertion, and it reattaches the clause as the reason for the distinction rather than for the expected prevalence of intuitions. Patch 3. |
| Q11 | "so long as the switch's directing a signal to the right is no more deviant than its directing a signal to the left" | Gallow, p. 86 | exact, p. 86 |
| Q12 | "deviant, noninertial events" | Gallow, p. 86 ("both deviant, noninertial events") | exact |
| Q13 | "default, inertial states" | Gallow, p. 87 ("default, inertial states can be neither causes nor effects") | exact. The 86–87 range is correct. |
| Q14 | "that it is always possible to formally construct additional variables to do this" | H&H, p. 37 | exact, p. 37 |
| Q15 | "available" / "does not violate the structural equations of the model" | X&X, Definition 12, p. 5 | exact, p. 5 |

No Halpern 2016 quotations appear, so no quotation needed a fetch request.

## Step 4. Attributions

| # | Claim (location) | Source check | Class | Fix |
|---|---|---|---|---|
| A1 | H&H: a witness world must be at least as normal as the actual world (§1, §2; 20–21) | p. 20 (end) to p. 21: the clause s_{X=x′,W=w,u} ≽ s_u is added to AC2(a) | accurate | — |
| A2 | Halpern 2015 handles one model of the switch (Hall's LT/RT model) by normality (§1; 8) | p. 8 | accurate | — |
| A3 | Halpern reports Schumacher's both-blocked problem for the original and updated definitions (§1; 7–8) | pp. 7–8 | accurate | — |
| A4 | Halpern notes the modified definition avoids it (§1, §4) | p. 8 | accurate | — |
| A5 | X&X show the same for the H–H definition (§1; 4–5, Obs. 1) | Obs. 1(a): stated p. 4, items and proof p. 5. Their (b) gives the MHP result. | accurate | — |
| A6 | Halpern 2016, Ex. 3.2.6: Suzy loses causal status if the frozen witness is too abnormal, and the throws become jointly a cause (§1; 84–85) | not retrievable | **unverifiable** | H1 |
| A7 | Beckers argues a dilemma of related shape for A&G (§1; 2, 10–11) | p. 2 ("unappealing dilemma"); pp. 10–11 | accurate | — |
| A8 | H&H p. 37 conjecture (§1, §6) | p. 37 | accurate | — |
| A9 | Schumacher's case is among those Halpern presents as handled better by the modified definition (§1; 8) | p. 8 | accurate | — |
| A10 | Halpern's statement of the three definitions; the modified definition freezes only at actual values (§2; 3–4) | AC2(a), (b), (b^u) on p. 3; AC2(a^m) on p. 4 | accurate | — |
| A11 | H&H guidelines: more typical somewhere and less typical nowhere gives "more normal"; mixed changes give incomparable, unless special considerations rank the worlds (§2; 20) | p. 20 | accurate | — |
| A12 | H&H default: endogenous variables typically obey their equations (§2; 19) | p. 19 ("unless there is some specific reason to think otherwise") | accurate | — |
| A13 | H&H: typicality must sometimes reflect how a variable depends on its parents (§2; 35) | p. 35 | accurate | — |
| A14 | Pareto is "H&H's first guideline applied across models" (§2, §5) | p. 20. It is the first of the rough-and-ready guidelines. | accurate (presented as the essay's own extension) | — |
| A15 | Halpern 2016, 149–150: compact representations give conforming values default typicality, with exceptions and cross-variable comparisons (§2) | not retrievable | **unverifiable** | H3 |
| A16 | A&G prima facie rule (§2; 26) | journal p. 26 | accurate | — |
| A17 | Boulder: Hitchcock 2001, in A&G's form (§3; 18) | A&G journal p. 18 cites Hitchcock 2001, p. 276. Their model D↔F, E↔B∧¬D matches the essay's K, H. | accurate | — |
| A18 | Short circuit: H&H 34–35, with the verdict that the antidote is not a cause | pp. 34–35 (P = A; the verdict that it is not a cause is on p. 35) | accurate | — |
| A19 | Tracks: Hall 2000 story, Hall 2007 route model as presented by Halpern 2015, 8 | Halpern pp. 7–8 ("due to Hall [2000]"; "Hall's [2007] model … LT and RT") | accurate | — |
| A20 | Doorbells and Gallow's verdict (§3; 84–85, 85) | The case runs pp. 84–85; the verdict is on p. 85. | accurate | — |
| A21 | Blocked tracks (§3; Halpern 7–8, X&X 4) | The essay's equation TA=(EF∧¬RB)∨(¬EF∧¬LB) and its variable names are X&X's, printed on **p. 5**. | accurate; pinpoint incomplete | patch 5 |
| A22 | Gallow models Doorbells with a single many-valued switch variable (§3) | p. 85 (S with values 1–3+; L := S=2, R := S=3) | accurate | — |
| A23 | "Without normality, every definition counts every candidate … a cause or part of a cause" (§3), as checked against Halpern's verdicts | Halpern pp. 7–8: LT/RT and LB/RB flip are causes under all three definitions or the older ones. Ex. 3.10 (same structure as the short circuit): all three definitions count the antidote a cause. The rest is the essay's own computation. | accurate | — |
| A24 | Halpern 2016, 84–85 "identified" the late-preemption structure (§4) | not retrievable | **unverifiable** | H2 |
| A25 | H&H call their rules rough-and-ready, allow cross-variable comparisons (32), and disclaim finding the right ordering (26 fn. 13) (§5) | pp. 20, 32; fn. 13 on p. 26 ("our concern here is not with determining what the 'right' normality ordering is") | accurate | — |
| A26 | Halpern's own judgment on Tracks (§5; 8) | p. 8 | accurate | — |
| A27 | Reliability is "the published ground", X&X reporting B&V (§5; 8) | p. 8. X&X attribute the distinction to B&V (2017, 2018) and add their own hedged gloss. | accurate in substance; quotation splice fixed by patch 3 | patch 3 |
| A28 | Gallow's model takes a representational route: one switch variable encodes setting and signal; the verdict holds "so long as…" (§5; 86) | pp. 85–86 | accurate | — |
| A29 | Blanchard & Schaffer "press" the aptness question "against reliance on defaults", as A&G report (§5; 27) | A&G journal p. 27: B&S "criticize the distinction between default and deviant events", argue that an apt (enriched) model handles bogus prevention, and "conclude … that we do not need a default-deviant distinction but apt causal models". On p. **28**, A&G cite B&S for the claim that what makes a model apt "is not fully answered". The essay's gloss, that B&S press a question about selecting representations by a principle stated before the verdicts, goes beyond the report. | **oversimplified**; page range incomplete | patch 4 |
| A30 | Gallow contrasts "deviant, noninertial events" with "default, inertial states" (§5; 86–87) | pp. 86–87 (also passim, e.g. p. 47) | accurate | — |
| A31 | H&H note that their treatments of the short circuit and of preemption involve exceptions to the conformity default (§6; 36) | p. 36, including "Observant readers will note that our treatment of the preemption example … did as well" | accurate | — |
| A32 | H&H remove the short circuit's exception with an intentions variable (§6) | pp. 36–37 | accurate | — |
| A33 | Halpern 2016, 121, 133–134: a stability theorem for conservative extensions whose reasoning the Lemma adapts (§6) | not retrievable | **unverifiable** | H4 |
| A34 | X&X: RHIT requires the witness world, with off-route intermediates held at actual values, to be available (Def. 12, 5); their causes are MHP causes (Prop. 1, 6); they concede the trainee case (8); their table covers four cases; the nondeterministic remedy uses Accurate and Nerve variables (8) | Def. 12 p. 5; Def. 13 and Prop. 1(a)+(b) p. 6; concession, remedy and Table 1 p. 8 (RHIT succeeds on Switch, Short Circuit, Bogus Prevention and Switch-variant) | accurate | — |
| A35 | A&G's final theory excludes the simple-switch flip because condition (5) keeps the descendants' regularities and then condition (2) fails (§7; 25) | journal p. 25: "Condition (5) thus prohibits to remove any direct non-redundant regularity from L. But then there is no F′ so that condition (2) is satisfied." | accurate | — |
| A36 | Beckers reports that the 2024 accounts need deviancy on two alternative switch models, one from Hitchcock 2009, and argues that deviancy then misjudges non-deviant-backup preemption (§7; 2, 10–11) | p. 10: Extended Switch "presented by Hitchcock (2009) to challenge…". p. 11: "AG5 and AG6 require invoking their non-structural deviancy condition…"; Backup 2. p. 2: the dilemma. | accurate | — |
| A37 | "Beckers (2026) argues that A&G's regularity theory faces a dilemma **of the same shape**" (§7) | Beckers's horns are structural-only versus the deviancy condition, and the dilemma targets all seven A&G accounts. §1 of the essay itself says "related shape". | **oversimplified** (and inconsistent with §1) | patch 6 |
| A38 | Objection 1: Halpern's three-variable model gets the switch right without normality under all three definitions (2015, 7) | p. 7 | accurate | — |
| A39 | Objection 1 reply: the blockage representation Halpern "takes from Halpern and Hitchcock" | Halpern p. 7: "following Halpern and Hitchcock [2010]". The only H&H work in the references is 2015. | **inaccurate** (wrong work implied) | patch 1 |
| A40 | Objection 1 reply: "Gallow's alternative replaces them [the bell/route variables] by a single variable" | Gallow's model keeps L and R (fn. 52 on p. 85: "L := S = 2 … Likewise for R := S = 3"; the networks use (L, R) on pp. 85–86). Only setting and signal are merged into S. | **inaccurate** | patch 2 |
| A41 | Objection 3: Halpern's graded account keeps causes with abnormal witnesses and compares their quality (2016, §3.3) | not retrievable. Chapter 3 is "Graded Causation and Normality" (Crossref chapter DOI). H&H 2015, 21 grades causes by their best witnesses, but only after the filter. | **unverifiable** | H5 |
| A42 | Objection 4: Hitchcock 2009, as Beckers (10) reports, presented a switch model to challenge the contrast | Beckers p. 10 | accurate | — |
| A43 | Appendix: the implementation reproduces Halpern's (2015) verdicts on the switch models and the short circuit | Consistent with pp. 7–8 and Ex. 3.10 | accurate | — |

These are 38 distinct author-claims; I split the long rows when counting. On the "as reported by" items: Hitchcock 2009 via Beckers (A42, A36) and Beckers & Vennekens via X&X (A27) are accurately reported. Blanchard & Schaffer via A&G (A29) is accurately reported only after patch 4. **Panel member:** Mario Günther (`judges.txt`). Andreas & Günther 2024 was checked in full text at every pinpoint (A16, A17, A29, A35, and the Beckers reports about A&G). All are accurate except the A29 gloss and page range.

## Step 5. Page numbers and dates

| Pinpoint | Status |
|---|---|
| H&H 2015: 19, 20, 20–21, 26 fn. 13, 32, 34–35, 35, 36, 37 | all verified (arXiv v1 pagination, as the reference states) |
| Halpern 2015: 3–4, 7, 7–8, 8 | all verified (arXiv v1, as the reference states) |
| Gallow 2021: 84–85, 85, 86, 86–87 | all verified (journal pagination) |
| A&G 2024: 18, 25, 26 | verified |
| A&G 2024: 27 (B&S report) | incomplete; the report runs 27–28 (patch 4) |
| X&X 2026: 4–5 (Obs. 1), 5 (Def. 12), 6 (Prop. 1), 8 (×4) | verified |
| X&X 2026: 4 (Blocked tracks model) | incomplete; the model is on pp. 4–5 (patch 5) |
| Beckers 2026: 2, 10, 10–11 | verified |
| Halpern 2016: Ex. 3.2.6, 84–85 (×2); 121, 133–134; 149–150; §3.3 | **unverifiable**. The book is not retrievable by me, and the reviser's notes say these rely on the 28 Oct review in `state/external/`, which I was barred from opening. Fetch filed; fallback patches H1–H5. |
| Years | All match. Hitchcock 2009 and Beckers & Vennekens 2018 use print years; their online-first years are 2008 and 2016. |

## Patch list (exact replacements)

Each "old" string below was checked to occur exactly once in `state/drafts/A4/v6.md`.

**Unconditional patches (apply all):**

1. §8, Objection 1 reply.
   OLD: `Theorem 2 arises in the blockage representation that Halpern (2015, 7) takes from Halpern and Hitchcock.`
   NEW: `Theorem 2 arises in the blockage representation that Halpern (2015, 7) uses.`

2. §8, Objection 1 reply.
   OLD: `and Gallow's alternative replaces them by a single variable with an explicit normality comparison among its values.`
   NEW: `and Gallow's own model keeps the bell variables, routing the signal through a single many-valued switch variable with an explicit normality comparison among its values (2021, 85–86).`

3. §5, "The reliability asymmetry".
   OLD: `write that "the key distinction between the early preemption and the switch example lies in whether we take into account the possibility that the backup mechanism malfunctions", since "the supervisor's shooting accuracy" is "far more uncertain than the breakage of a sturdy track".`
   NEW: `write that "the key distinction between the early preemption and the switch example lies in whether we take into account the possibility that the backup mechanism malfunctions"; they add that "it is quite plausible to regard the supervisor's shooting accuracy as far more uncertain than the breakage of a sturdy track".`

4. §5, Gallow paragraph.
   OLD: `Whether such representations can be selected by a principle stated before the verdicts is the aptness question that Blanchard and Schaffer (2017) press, as Andreas and Günther (2024, 27) report, against reliance on defaults.`
   NEW: `Whether such representations can be selected by a principle stated before the verdicts is a question about model aptness. Blanchard and Schaffer (2017), as Andreas and Günther (2024, 27–28) report, argue that apt causal models make a default–deviant distinction unnecessary.`

5. §3.
   OLD: `*Blocked tracks* (Halpern 2015, 7–8; Xiao and Xiong 2026, 4).`
   NEW: `*Blocked tracks* (Halpern 2015, 7–8; Xiao and Xiong 2026, 4–5).`

6. §7.
   OLD: `Beckers (2026) argues that Andreas and Günther's regularity theory faces a dilemma of the same shape.`
   NEW: `Beckers (2026, 2) argues that Andreas and Günther's accounts face a dilemma of related shape.`

7. References, Blanchard & Schaffer. This is a metadata completion; the page range comes from A&G 2024's reference list, and the DOI record has no pages.
   OLD: `edited by Helen Beebee, Christopher Hitchcock, and Huw Price. Oxford: Oxford University Press.`
   NEW: `edited by Helen Beebee, Christopher Hitchcock, and Huw Price, 175–214. Oxford: Oxford University Press.`

8. References, Halpern 2016 (adds the Crossref-verified DOI).
   OLD: `Halpern, Joseph Y. 2016. *Actual Causality*. Cambridge, MA: MIT Press.`
   NEW: `Halpern, Joseph Y. 2016. *Actual Causality*. Cambridge, MA: MIT Press. https://doi.org/10.7551/mitpress/10809.001.0001.`

**Conditional patches H1–H5 (Halpern 2016).** Apply all five **unless**, before the revision is frozen, either (a) the pages from fetch request `a4-audit-halpern-2016-pinpoints` arrive in `inbox/sources/` and a citation check confirms each pinpoint, or (b) the orchestrator confirms each pinpoint against the 28 Oct book review it is entitled to read. In either case, keep only the confirmed pinpoints.

Caution: the fetch log records that the book comparison "narrows A4's originality claim". H1 and H2 therefore remove a credit to Halpern that may be owed. Verification (a) or (b) is strongly preferred to applying H1 and H2.

- **H1** (§1, Closest work).
  OLD: `Halpern (2016, Example 3.2.6, 84–85) observes that if the witness in which Billy throws but does not hit is too abnormal, Suzy's throw ceases to be a cause under the modified definition and the two throws together become one.`
  NEW: `Halpern (2016), as Beckers (2026, 10) reports, argues that his definition gives the right verdict on the simple switch once a normality condition is invoked.`
- **H2** (§4).
  OLD: `This is the structure Halpern (2016, 84–85) identified for late preemption; Theorem 1 shows that the escape from it is the switching verdict.`
  NEW: `Theorem 1 shows that the escape from this structure is the switching verdict.`
- **H3** (§2). The replacement is verified: H&H pp. 20, 32, 36.
  OLD: `and Halpern's compact representations likewise give equation-conforming values a default typicality, with explicit exceptions and cross-variable comparisons allowed (2016, 149–150).`
  NEW: `and Halpern and Hitchcock themselves allow exceptions to the conformity default (2015, 36) and comparisons of typicality across variables (2015, 20, 32).`
- **H4** (§6).
  OLD: `The argument adapts the elimination-and-minimality reasoning of Halpern's (2016, 121, 133–134) stability theorem for conservative extensions to a single conforming witness.`
  NEW: `The argument uses only elimination and minimality.`
- **H5** (§8, Objection 3). The replacement is verified: H&H p. 21, and the Crossref chapter title for ch. 3.
  OLD: `Halpern's graded account keeps causes with abnormal witnesses and compares their quality (2016, §3.3).`
  NEW: `Graded accounts rank causes by the normality of their best witnesses (Halpern and Hitchcock 2015, 21; Halpern 2016, ch. 3), and one could keep causes whose witnesses are abnormal, ranking them low.`

Word-count effect: patches 1–8 add about 25 words. Patches H1–H5 remove about 50. Either way the essay stays well under the 6,000 limit.

## Not checked, or flagged only

- The essay's own computations (355 preorders, five calibrated preorders, gain identities, A&G-condition runs) are not citation matters and were not re-run.
- Gallow's verdict is about productive causation (pp. 86–87). The essay's "negative verdict" wording is acceptable.
