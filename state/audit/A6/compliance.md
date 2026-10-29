FAIL

# A6 compliance check: `final/A6/essay.md` (mode: essay)

Date: 2026-10-29. The final essay is based on the second system's v5 and has the v4 citation-audit and formal-audit patches applied on top (see `final/A6/changelog.md`).

## Checklist

### 1. Word count: PASS (over target)
`python3 tools/wordcount.py final/A6/essay.md --limit 6000 --target 5600` gives strict=5831, wordlike=5804, footnotes=0, 37 bibliography lines excluded, result OVER_TARGET.
- The count is under the 6,000 limit by 169.
- It is over the 5,600 target by 231. This is not blocking.

### 2. Injection and panel mentions: PASS
`check_injection.py` with `--names "paulmauriceadriendirac"` and `--judges-file state/panel/judges.txt` reports no hard flags. Soft flags: Salow 46, Hawthorne 7, Goldstein 3, Fitelson 1.

I reviewed each panel mention:
- **Salow.** The mentions are cited quotations and paraphrases. Citation audit Q1–Q20 found them exact, and the post-audit edits (P2, P12, P14) calibrate them.
- **Hawthorne.** He appears through Salow's report (2004, 181, flagged as Salow's report), as Goldschmidt's subject (H&S 2008), and as G&S's report of Goldstein & Hawthorne. All are accurate per audit A29, A31, A34 and A38.
- **Goldstein.** The mentions come only through G&S 2023, 130 n. 40. Accurate.
- **Fitelson.** He appears only as a co-author in the *Deference Done Better* reference entry. That paper's content has NOT been verified by this pipeline; see item 5.

Separate scan for hidden text:
- No zero-width, soft-hyphen or control characters.
- No HTML comments.
- Every "<" character sits inside LaTeX math.

### 3. Anonymity: PASS
I grepped for the redact value, the account email, "github", "astra", "claude", "codex", "gpt", "openai", "anthropic", "competition", "judge", "panel", "pipeline", "elenchus", "AI", "language model" and "/home". There were no hits. The only URLs are two Wiley DOIs in the references. There is no first-person reference to the entrant and no mention of AI authorship.

### 4. Structure: PASS (minor notes)
The essay has a title, an abstract and a references section.

Citations and references match both ways (17 each): Ahmed & Salow 2019; Das 2023; Dorst 2020; Dorst et al. 2021; Fantl & McGrath 2002; Geanakoplos 1989; Goldschmidt 2024; Goldstein & Hawthorne 2022; Good 1967; Goodman & Salow 2023; Goodman & Salow 2025 (BRN); Hawthorne 2004; Hawthorne & Stanley 2008; Hong 2024; Hong 2026; Salow 2025; Weatherson 2005. Fantl & McGrath and Weatherson are cited only inside a Salow quotation, which the audit accepts.

Minor points:
- Dorst et al. 2021 is listed before Dorst 2020. The usual order puts the single-author entry first.
- Only two entries carry DOIs.
- "(§6.1)" at l.31 is an internal cross-reference that can be misread as a G&S locator. The changelog already flags this.

### 5. Scholarship (citation audit): FAIL
The audit (`state/audit/A6/citations.md`, run on v4) lists P1–P14d. I confirmed in the final text that P1–P3, P5–P14d are applied or superseded. Two problems remain.

**(a) A3 / P4, Hong 2026: open item, not patched.**
- The audit classed the Hong attribution "unverifiable". Wiley returned 403. Its patch P4 cuts the attribution back to what the abstract supports ("argues that whatever the normality framework captures is not action-guiding"), and Step 5 records the "§§1–3" locator as "unverifiable; removed (P4)".
- The final essay (l.19) does not apply P4. It restores, word for word, the v4 sentence that P4 was written to replace: "Hong (2026, §§1–3) criticizes combining normality knowledge with a knowledge-first decision rule, using lottery choices, sweetened prospects and information that distinguishes equally likely payoffs."
- That content comes from the second system's notes: `state/external/ambitious-review-20261022/REVIEW.md` l.46 and l.103 ("Main text §§1–3 read"). The audit's A3 row says the auditor could not open those notes. No agent in this pipeline has read Hong's text (changelog note 1; `methodology/provenance.md` l.168, "Hong 2026 (never read)"). Fetch requests `amb-a6-hong-2025-2026` and `l3-hong-2026-normality-in-action` are still pending.

On the caller's specific question: the essay attributes nothing to Hong beyond what those records say. The wording matches REVIEW.md l.46 almost exactly, and the cut of "challenges normality knowledge" is a correct narrowing. But those records are an unverified secondhand summary by another model. The pipeline's own auditor ruled the claim unverifiable, and the section-level locator was never checked. Under CLAUDE.md §1.3 and checklist item 5 this is an open audit item that has not been patched.

**(b) *Deference Done Better* paragraph (l.21): unaudited attribution to a work co-authored by two panel members (Salow, Fitelson).**
- The paragraph was added in v5, after both audits. It makes specific claims:
  - "Total Trust is equivalent to Value … (Theorem 2.2)"
  - the gloss of Value
  - a "Weak Value condition"
  - "their Appendix B establishes its equivalence to Value and Total Trust"
- Only the second system's one-line note in `VERIFICATION.md` covers these claims ("checked for Value, Weak Value and Total Trust"). This pipeline checked only the Crossref metadata (`provenance.md` row 6.8; changelog "Not done and residual risks"). The high-priority fetch `l5-dorst-et-al-2021-deference-done-better` (filed 2026-10-21) is still open.
- My own attempts to retrieve the text failed: PhilArchive and PhilPapers OA returned 403, the author-site URL returned 404, and the Wayback request was reset.
- The OpenAlex abstract supports only the general shape: deferring opinions is deferring decisions; a new principle is equivalent to the decision-preference constraint and to an accuracy constraint. It names neither "Total Trust", "Value", "Weak Value", Theorem 2.2 nor Appendix B.
- CLAUDE.md §1.6 requires exceptional care with judges' work. Two co-authors are judges, so a wrong theorem or appendix locator or a wrong definition would be noticed.

### 6. Human-input record and hygiene: PASS
- All 27 entries in `methodology/human_inputs.md` are classified: logistics, courier, method, generic-feedback or selection. No entry is classed rejected-substantive, so there was nothing to trace.
- The 2026-10-22T10:01:37Z entry records the human's statement that Astra received nothing idea-wise.
- The 2026-10-29T17:35:47Z courier entry forwards Astra's status note, which is AI-originated.
- `methodology/hygiene.md` (Phase 0) is clean. No memory or profile content was present, auto-memory was off, and connectors were not called. The account email was ignored, and it does not appear in the essay.
- The 23 October context-exposure disclosure about the second system is handled as follows:
  - `methodology/log.md` l.60 records the quarantine.
  - l.76 lifts it under the revised §1.2 (no human contribution identified; `PROVENANCE-CLARIFICATION.md`).
  - l.90 records the human's confirmation of the revised §1.2 on 29 Oct.
  - The historical disclosure is preserved.
- The A6 base is the second system's v5, credited in `methodology/provenance.md` rows 6.2 and 6.8. The methodology report must keep that credit and the disclosure history.

### 7. Formal audit: PASS
`state/audit/A6/formal.md` is complete. It has two FALSE or unsupported items (#24, #27) and patches P1–P8. I checked each patch against the final text:

| Patch | Evidence in final text |
|---|---|
| P1 | "about $0.356$ conditional" (l.49), with BRN's 0.37 tied to its narrower event |
| P2 | "is $-0.60$" (l.107) |
| P3 | "s_0=s_1" (l.121) |
| P4 | "1,724" and "2,322" are absent; the claim was removed |
| P5 | "non-trivial partition" (l.181) |
| P6 | "continuous analogue of Lemma 2" (l.91) |
| P7 | "for all but knife-edge priors" (l.151) |
| P8 | "in finite graded models no factive" (abstract) |

No "2002 revision" remains. There is no unresolved mismatch.

Residual points, not blocking:
- The continuous analogue (P6) is stated without proof.
- The §6.2 generalization is argued, not proved.
- The new l.21 claim that universal safety implies DDB's Weak Value was not formally audited. It depends on DDB's definitions; see 5(b).

## Required fixes

1. **Hong 2026 (l.19).** Apply citation-audit P4. Replace the sentence with "Hong (2026) argues that whatever the normality framework captures is not action-guiding." This shortens the text by about 15 words, and the next sentence ("The general decision-theoretic objection is therefore not new.") still follows. Do this unless the full text is obtained before submission and a citation-auditor verifies the §§1–3 description against it. The human can fetch it via the pending request; it must not be summarized by the human.
2. **Deference Done Better (l.21).** Before submission, a citation-auditor in this pipeline must check, against a retrieved copy:
   - Theorem 2.2
   - the definitions of Value, Weak Value and Total Trust
   - the Appendix B equivalence
   - the essay's mapping of $\pi$ and $P_s$ onto DDB's framework

   The human can supply the PDF through fetch request `l5-dorst-et-al-2021-deference-done-better`. If this cannot be done, reduce the paragraph to what the abstract supports. Drop "(Theorem 2.2)", "Weak Value" and the "Appendix B" sentence, and present the link to Theorem 1 as the essay's own claim, without attributing specific results.
3. After the fixes, rerun `wordcount.py` and `check_injection.py`, and log the change in `final/A6/changelog.md`.

Optional:
- Put Dorst 2020 before Dorst et al. 2021 in the references.
- Reword "(§6.1)" at l.31 as "(see §6.1 below)".
