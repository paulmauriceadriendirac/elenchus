# A4 final — changelog

## final/A4/essay.md — patch release, 2026-10-29

- **Mode:** patch. No new arguments, cases or claims.
- **Base:** `state/external/submission-sourcechecked-20261029/A4-Causation-v7.md`. It was copied to `final/A4/essay.md` and patched there; the base is unchanged.
- **Patch list:** `state/audit/A4/citations.md`. That audit was run on `state/drafts/A4/v6.md`. None of the v6→v7 revisions touched the OLD strings of patches 1–8. A script confirmed that each string occurs exactly once in the base and replaced it.
- **Word count** (`tools/wordcount.py`, strict): **5,540**. The base had 5,520, so the patches add 20 words. Limit 6,000, target 5,600: OK.
- **`check_injection.py`:** no hard flags. One soft flag: the panel surname "Günther" appears 8 times. Every one of these is a citation of Andreas and Günther 2024, and the audit checked each pinpoint against the full text (A16, A17, A29, A35, and Beckers's reports about A&G). No change.

### Patches 1–8 (unconditional)

| # | Location | Status | Change and reason |
|---|---|---|---|
| 1 | §8, Objection 1 reply | applied | "...the blockage representation that Halpern (2015, 7) takes from Halpern and Hitchcock" → "...that Halpern (2015, 7) uses". Halpern 2015, p. 7 credits the model to Halpern and Hitchcock **2010**. The only H&H entry in the references is 2015, so the old wording implied the wrong work (audit A39). I removed the attribution as the audit specified. I did not add an H&H 2010 entry, because a patch release should not introduce an unaudited reference. |
| 2 | §8, Objection 1 reply | applied | "Gallow's alternative replaces them by a single variable..." → "Gallow's own model keeps the bell variables, routing the signal through a single many-valued switch variable with an explicit normality comparison among its values (2021, 85–86)". Gallow keeps L and R (fn. 52, p. 85) and merges only setting and signal into S (audit A40). The new wording is consistent with §3 and §5. |
| 3 | §5, "The reliability asymmetry" | applied | The splice since "the supervisor's shooting accuracy" is "far more uncertain..." is replaced by two separate quotations: "...the backup mechanism malfunctions"; they add that "it is quite plausible to regard the supervisor's shooting accuracy as far more uncertain than the breakage of a sturdy track". This restores Xiao and Xiong's hedge, and the clause is no longer presented as the reason for the distinction (audit Q9–Q10, A27). I checked both strings word for word against `inbox/sources/xiao-xiong-2026-hitchcock-refinement.txt` (p. 8). The only differences are extraction spacing and a curly apostrophe. |
| 4 | §5, Gallow paragraph | adapted | I applied the audit's new text. The aptness question is now a separate sentence. It is followed by: Blanchard and Schaffer (2017), as Andreas and Günther (2024, **27–28**) report, "argue that apt causal models make a default–deviant distinction unnecessary". This fixes the oversimplified gloss and the incomplete page range found in audit A29. I checked the paraphrase against the A&G text, which has B&S "conclude ... that we do not need a default-deviant distinction but apt causal models" and "the question is not fully answered (Blanchard and Schaffer, 2017)". **Adaptation:** the next sentence, "I do not settle it here", now reads "I do not settle that question here". Without this, "it" could be read as B&S's claim instead of the aptness question (+1 word). |
| 5 | §3, *Blocked tracks* | applied | Xiao and Xiong pinpoint "4" → "4–5". Their model and equation are printed on p. 5 (audit A21). |
| 6 | §7, first sentence | applied | "Beckers (2026) argues that Andreas and Günther's regularity theory faces a dilemma of the same shape" → "Beckers (2026, 2) argues that Andreas and Günther's accounts face a dilemma of related shape". This matches Beckers's horns and his target, which is all of A&G's accounts. It also matches §1's "related shape" (audit A37). |
| 7 | References, Blanchard and Schaffer 2017 | applied | Added the page range 175–214. It is confirmed in A&G 2024's reference list (`state/ambitious/sources/andreas-gunther-2024-regularity.txt`). The DOI record has no pages. |
| 8 | References, Halpern 2016 | applied | Added the DOI https://doi.org/10.7551/mitpress/10809.001.0001. `tools/verify_refs.py` returned VERIFIED this session. |

### Conditional patches H1–H5 (Halpern 2016): skipped, pinpoints kept

The audit made H1–H5 conditional: apply the weakening only for pinpoints that are not confirmed. I checked them against the book-review record in `state/external/submission-book-review-20261028/Halpern-Originality-Review.md`. The copy in `submission-additive-20261029/` is byte-identical. The record's author read the book using its printed pagination. It confirms each pinpoint as the base states it, so none of the weakening patches applies.

| # | Base text (location) | Record | Status |
|---|---|---|---|
| H1 | §1. Halpern (2016, Example 3.2.6, 84–85): if the witness in which Billy throws but does not hit is too abnormal, Suzy's throw ceases to be a cause under the modified definition, and the two throws together become one. | "In Example 3.2.6, pages 84–85 ... Suzy's throw ceases to be a cause by itself under the modified definition, while the conjunction of the two throws becomes a cause." | skipped, pinpoint confirmed and kept |
| H2 | §4. "the structure Halpern (2016, 84–85) identified for late preemption" | Same record as H1. | skipped, pinpoint confirmed and kept |
| H3 | §2. Halpern's compact representations supply default typicalities while allowing exceptions and cross-variable comparisons (2016, 149–150). The base had already reworded the v6 sentence; the pinpoint is unchanged. | "Halpern's compact rules in section 5.2.2, pages 149–150, make equation conformity a useful default for typicality while permitting exceptions and comparisons across variables." | skipped. The base had reworded the sentence, and the record supports the new wording. Kept. |
| H4 | §6. The Lemma's proof adapts the elimination-and-minimality reasoning of Halpern's (2016, 121, 133–134) stability theorem for conservative extensions. | "Theorem 4.4.4(b), page 121, concerns conservative extensions ... The proof on pages 133–134 removes conforming interventions and uses AC3 minimality." | skipped, pinpoint confirmed and kept |
| H5 | §8, Objection 3. Halpern's graded account keeps causes with abnormal witnesses and compares their quality (2016, §3.3). | "Section 3.3, pages 85–86, grades causes by their witnesses instead of excluding causes with insufficiently normal witnesses." | skipped, pinpoint confirmed and kept |

**Limit:** these confirmations rest on another reviewer's record, not on pages this pipeline retrieved. The pages requested in `requests/fetch/a4-audit-halpern-2016-pinpoints.md` have not arrived in `inbox/sources/`.

### Formal audit: skipped

`state/audit/A4/formal.md` does not exist. The directory `state/audit/A4/formal/` holds only `hp_audit.py` and `hp_audit.out`; there is no list of FALSE items and no patch list. Nothing was applied.

**For the orchestrator:** `hp_audit.out` reports 85 checks: 82 pass and 3 fail. The three failures are one item checked under each of the three definitions. §4 says "Exactly five of the 355 preorders, two of them total orders". If "total orders" means linear (antisymmetric) orders, that is false: the two are total preorders (weak orders), and none of the five is antisymmetric. A possible one-word fix is "total preorders". I did not apply it.

### Other checks (no change made)

- **Wysocki 2023** was added in v7, after the audit, so the audit does not cover it. Its metadata is VERIFIED: `verify_refs.py` matched it, and Crossref gives *Synthese* 201, article 197, 2023, matching the entry. The content claims in §1 and §9 rest on the external v7 `VERIFICATION.md` ("Wysocki's conjoined-case argument and Halpern's book support the narrowed causation comparison"). This pipeline has not checked them against Wysocki's text.
- **`verify_refs.py`** was run on all 14 entries (input and output in the session scratchpad, `a4final/`). Results: 11 VERIFIED. Beckers 2026 and Halpern 2015 were NOT_FOUND because OpenAlex returned HTTP 429; the audit had verified both by hand from their arXiv abstract pages. Beckers and Vennekens 2018 is a MISMATCH on the year only: it appeared online in 2016 and in print in 2018.
- **Uncredited Halpern 2016 overlaps.** The book-review record lists overlaps that the base does not credit: p. 83 and §4.7 (pp. 126–127), on fitting verdicts by adjusting normality; and §4.1 (pp. 108–111), on representational limits. Adding these credits would be a new claim, which is outside patch mode. Flagged for the orchestrator.

## Formal-audit patches — final/A4/essay.md, 2026-10-29

- **Mode:** patch. No new arguments, cases or claims.
- **Pre-patch copy:** `final/A4/essay_pre_formal.md`. It is byte-identical to `essay.md` before this release (5,540 words).
- **Patch list:** `state/audit/A4/formal.md`, P1–P7. The audit was run on `state/drafts/A4/v6.md`. A script checked that each old string occurred exactly once in `final/A4/essay.md` before writing. All checks passed, and it then made all seven replacements in one pass. Six lines changed: §3, §4 twice, §5, §6 and the Appendix.
- **This section supersedes "Formal audit: skipped" above.** `formal.md` now exists, and its P1 is the "total orders" fix proposed there.
- **Word count** (`tools/wordcount.py`, strict): **5,581**. The previous count was 5,540, so these patches add 41 words. Limit 6,000, target 5,600: OK.
- **`check_injection.py`** (`--judges-file state/panel/judges.txt`): no hard flags. The one soft flag is unchanged: "Günther" appears 8 times, every time in a citation of Andreas and Günther 2024. These patches add no mention.
- **References:** none added. `state/candidates/A4/refs.json` does not exist, so `verify_refs.py` was not run. The one new pinpoint (P7) is to Xiao and Xiong 2026. That entry is already in the References and was VERIFIED in the previous patch release.

| # | Location | Status | Change and reason |
|---|---|---|---|
| P1 (required) | §4, calibration paragraph after Theorem 1 | applied | "two of them total orders" → "two of them total preorders". In the audit's row 9 and finding 1, all five calibrated preorders have n~l, so none is antisymmetric (linear). Two are total preorders (weak orders). |
| P2 | §3, paragraph after the cases | adapted (punctuation only) | "every candidate above a cause or part of a cause" → "every candidate above, except Billy's throw, a cause or part of a cause". Audit row 2: without normality, Billy's throw is in no cause under any definition, so "every candidate" over-reached. I added two commas to the audit's wording so that the sentence parses on first reading. The words are the audit's. |
| P3 | Appendix, "Witness uniqueness and AC3", last sentence | applied (full version) | The old sentence is literally false (audit row 32 and finding 3). The switches have no extra witness worlds, and some other contingencies, e.g. [F←0, A←0], do change the arrival. I used the audit's replacement. The word budget allowed the full version, not the short alternative. |
| P4 | Appendix, same paragraph, chain | applied | Added "and setting either to 0 violates sufficiency". Audit row 31: the uniqueness justification covered only freezing at 1. |
| P5 | §5, "One additive separation" | adapted | I applied the audit's text with one change: "that judgment" → "the escape" (same word count). In the audit's wording, "that judgment" most naturally refers back to "Halpern's own judgment on Tracks". The added "and the left bell" would then credit Halpern (2015) with a judgment about Doorbells, a case he does not discuss. "The escape" is the −5 scoring of the frozen bell and left track, introduced two sentences earlier, and it is what the variable-indexed preorder expresses. The substance of the audit's correction is kept in full: a single-preorder componentwise filter cannot separate these cases, so the preorder must be indexed by variable (row 21). |
| P6 | §4, Corollary | applied | "neither switch-setting nor either flip in Tracks and Blocked tracks" → "neither the switch-setting in Doorbells nor the flip in Tracks or in Blocked tracks" (clarity). The Corollary still matches premise (P1) of §5 and the Appendix. |
| P7 | §6, Xiao and Xiong paragraph | adapted; partly already fixed | The v6 sentence that grounded the actual-value witnesses in Proposition 1 is not in the final text. The v7 revision already cites Proposition 1 only for "their causes are modified-HP causes", so that part of the correction was already made. The other part was missing: the actual-value requirement's only pinpoint was (Definition 12, 5), and Definition 12 defines availability only. "Xiao and Xiong's (2026) refinement" → "Xiao and Xiong's (2026, Definition 13, 6) refinement". I checked this against `inbox/sources/xiao-xiong-2026-hitchcock-refinement.txt`. Definition 13, the RHIT definition, falls between the p. 5 and p. 6 page footers, so it is on p. 6. It holds the off-route intermediates W_xz at their actual values and requires the resulting world to be available. Definition 12 is on p. 5 and Proposition 1 on p. 6, so the existing pinpoints are correct. This confirms the p. 6 page the audit asked the citation auditor to check. The pinpoint format follows the essay's "Halpern's (2016, 121, 133–134)". |
| P8 (optional; not in the requested P1–P7) | §4 / Appendix | skipped | The audit's own condition for P8 is not met: the candidate's verified code has no exact SMT check, and the essay may not cite the audit's scripts. |

### Section 7 (Andreas and Günther): no change, flagged

Audit row 35 covers the §7 claims about Andreas and Günther's verdicts:
- their final theory counts the swarm a cause without the deviancy condition and not with it;
- their other conditions already exclude the Doorbells switch-setting and the Seedlings swarm;
- the simple switch is excluded through condition (5) and condition (2).

The audit marks row 35 **UNVERIFIED** (no independent implementation) but supplies no weakening patch. It says no textual patch is needed for consistency, because the author's rerun code prints the stated pattern. It asks that the results be treated as author-computed only. I therefore left §7 and the Appendix's mention of "Andreas and Günther's (2024) conditions with and without deviancy" unchanged. The text already presents the verdicts as "on my computation".

**For the orchestrator:** independent confirmation needs an implementation of Andreas and Günther's (2024) conditions (1)–(5) and of deviancy, taken from the source. The audit notes that the source is not in `inbox/`. The previous release used a copy at `state/ambitious/sources/andreas-gunther-2024-regularity.txt`. Audit finding 4 concerns the clear-tracks flip under the modified definition, which the essay does not discuss; no change was needed.

## Adopted v10 (2026-10-31)
- final/A4/essay.md = second system's v10 (state/external/submission-ready-20261030/A4-Causation-v10.md) with delta-audit patch P1 applied verbatim by the orchestrator (unverifiable p. 85 machine example replaced by the verified pp. 84–85 point). Delta audit: state/audit/A4/v10_delta.md. v8 kept as essay_v8.md. PDF rebuilt.

## DeepSeek substance triage fixes (2026-10-31)
- Applied verbatim E1, E2 (Tier 1) and E3 (Tier 2) from state/audit/A4/deepseek_triage.md; pre-edit text kept as essay_pre_deepseek.md. PDF rebuilt.
