PASS

# A4 compliance check — `final/A4/essay.md`

Date: 2026-10-29. Mode: essay. Checker: compliance subagent.
Essay title: "A Switching Dilemma for Normality in Actual Causation". The base is the second system's v7, with citation-audit patches 1–8 and formal-audit patches P1–P7 applied (`final/A4/changelog.md`).

## Checklist

### 1. Word count — PASS
`python3 tools/wordcount.py final/A4/essay.md --limit 6000 --target 5600` gives:
`strict=5581 wordlike=5578 (footnotes=0; bibliography lines excluded=31) limit=6000 target=5600 -> OK`.
5,581 is within the 6,000 limit and below the 5,600 target. It matches the changelog's figure.

### 2. Injection and panel mentions — PASS
`python3 tools/check_injection.py final/A4/essay.md --names "paulmauriceadriendirac" --judges-file state/panel/judges.txt` reported:
- **Hard flags:** none.
- **Soft flags:** panel surname "Günther", 8 mentions.

All 8 mentions are "Andreas and Günther (2024)" citations, in §1, §2, §3 (Boulder), §5, §7 and the Appendix. The citation audit checked each pinpoint against the full text: A16 at p. 26, A17 at p. 18, A29 at pp. 27–28 (patched), and A35 at p. 25, plus Beckers's reports about the theory (A36). Every mention is a genuine citation, and A&G is among the most relevant works for §7. The §7 computational claims about their theory are covered under item 7.

I also ran my own scan of the essay text. It found no invisible, format or control characters, no HTML comments or spans, and no text addressed to machines.

### 3. Anonymity — PASS
I searched for the entrant's name and username, the redact value, the email, "github", "Astra", "elenchus", "Claude", "Anthropic", "OpenAI", "GPT", "AI", "LLM", "language model", "competition", "judge", "panel", "pipeline" and "reviewer". There were zero hits. The essay has no paths and no institutions. First-person singular ("my computation", "the binary route model is mine") is ordinary authorial voice.

Note: CONFIG's `redact` holds only the GitHub username. The human declined to extend it (log 21 Oct 18:28:31). This does not matter for this essay because no personal data appears in it.

### 4. Structure — PASS
The essay has a title, an abstract, numbered sections, an appendix and a References section with 14 entries.

I cross-checked citations in both directions:
- **References to text:** every entry is cited. That covers A&G 2024, Beckers 2026, Beckers & Vennekens 2018, Blanchard & Schaffer 2017, Gallow 2021, Hall 2000, Hall 2007, Halpern 2015, Halpern 2016, H&H 2015, Hitchcock 2001, Hitchcock 2009, Wysocki 2023 and Xiao & Xiong 2026.
- **Text to references:** every in-text citation has an entry. Schumacher is named only as Halpern's credit, which the audit accepted. "Hitchcock's active-route account" refers to Hitchcock 2001.

### 5. Scholarship — PASS (with disclosed limits)
The audit (`state/audit/A4/citations.md`) was run on v6. I checked how each of its open items stands in the final text:

| Audit item | Status in final text |
|---|---|
| Patches 1–8 (A39, A40, Q9–10/A27, A29, A21, A37, B&S pages, Halpern 2016 DOI) | All present, each verified in the essay text. Patch 1 is at §8 ("Halpern (2015, 7) uses"). Patch 2 is at §8 ("Gallow's own model keeps the bell variables … (2021, 85–86)"). Patch 3 is at §5 (hedged X&X quotation restored). Patch 4 is at §5 (B&S, A&G 27–28). Patch 5 is at §3 (X&X 4–5). Patch 6 is at §7 ("Beckers (2026, 2) … related shape"). Patches 7 and 8 are in the References. |
| H1–H5 (Halpern 2016 pinpoints, unverifiable to the auditor) | Resolved under the audit's own condition (b). Each pinpoint was checked against `state/external/submission-book-review-20261028/Halpern-Originality-Review.md`, a record made from the book using printed pagination. I confirmed it supports each pinpoint: Ex. 3.2.6 on pp. 84–85 (line 17), §3.3 on pp. 85–86 (line 19), Thm 4.4.4(b) on p. 121 with the proof on pp. 133–134 (line 21), and §5.2.2 on pp. 149–150 (line 42). The essay's wording matches the record. **Limit:** this pipeline never saw the pages. Fetch `a4-audit-halpern-2016-pinpoints` is still open. |
| Wysocki 2023 (added in v7; not covered by the audit; changelog said "not checked against Wysocki's text") | **Now verified by this check.** I retrieved the author-posted PDF, which has Synthese pagination, "Synthese (2023) 201:197", 19 pp. It is the link given in the second system's ASSESSMENT. Results: §4 "Conjoined cases" (pp. 7–10) and §5 "Other normality theories" (pp. 11–14) are the right sections. The Tsarina and The Patriarch each have a single witness that vindicates one verdict and contradicts the other. Wysocki says he enriches the cases "so that no normality ordering can preserve the judgments" (p. 8) and that "the witness for predicting that the causal relation holds where it should also serves as a witness for predicting that the causal relation holds where it shouldn't" (p. 10). §4 targets Halpern 2016, which is the modified definition. §5 targets H&H 2015, which "adds a normality condition to what Halpern and Pearl (2005) called their updated theory" (p. 11), and The Tsarina defeats it. So "His cases cover both updated and modified definitions" is accurate. Wysocki works mainly with contrastive formulations and also treats non-contrastive versions (p. 13); the essay's gloss is fair. Metadata had already been verified (Crossref; changelog). Copy: `/tmp/claude-0/-home-user-elenchus/0999555b-7b80-5958-88f6-1f601c103b28/scratchpad/wysocki/w.pdf` (scratch, not persistent). |
| Other v7 rewordings (§1 increment and "Why it matters", §2 anonymity paragraph, §5 restricted repair, §6 X&X paragraph, Obj. 3 reply, conclusion) | I diffed the v6 and final texts. The new wording either makes no new attribution or reuses audited sources at audited pinpoints. The one new pinpoint is X&X Definition 13 on p. 6, which the patch agent checked against `inbox/sources` (formal P7). The Obj. 3 reply no longer cites Halpern 2016, so it now claims less than before. |

No open citation items remain unpatched.

### 6. Human-input record and hygiene — PASS (with disclosures)
- **`methodology/human_inputs.md`:** all 25 entries are classified (logistics, courier, method, generic-feedback, selection). None is `rejected-substantive`, so there was nothing to trace. Courier uploads (Xiao & Xiong, PDFs) came without comment. The 29 Oct 17:35 courier entry relays an AI-written status note. Its risk heading, "A4: philosophical significance and overlap with prior work", is not a human philosophical contribution. The Gate A2 entry is a selection among finished essays.
- **`methodology/hygiene.md`:** the Phase 0 check found a clean orchestrator context, with memory disabled, no user-level instructions and connectors unused. "Result: no contamination."
- **Disclosure (not a failure):** the final base, v7, and the earlier v2–v5 were written by the second AI system. On 23 Oct that system self-reported a non-specific context-exposure concern, and its outputs were quarantined (log 01:56:19). Under the revised CLAUDE.md §1.2 the quarantine was lifted on 27 Oct (log 16:02:46). The human confirmed the revised §1.2 on 29 Oct (log 11:45:15). `PROVENANCE-CLARIFICATION.md` records that no human philosophical contribution was identified. Under §1.2 an unspecified concern is not a finding of disqualification, so I record a disclosed context-exposure concern with no identified human contribution. `hygiene.md` covers only this pipeline's sessions, not the second system's. The methodology report must disclose this and the fact that §1.2 was revised by the second system and then confirmed by the human (`provenance.md` says report §4.4 does).

### 7. Formal audit — PASS
The audit (`state/audit/A4/formal.md`, run on v6) has one FALSE item and several recommended patches:
- **P1 (required)** is applied: "two of them total preorders" (§4).
- **P2–P7** are applied, with P2 and P5 adapted only for wording. I verified each in the essay text: §3 "except Billy's throw"; Appendix sufficiency sentences; §5 "the escape indexes the preorder by variable"; Corollary wording; §6 "(2026, Definition 13, 6)".
- **P8** is optional. It was skipped on the audit's own condition.

No unresolved mismatch remains.

**Section 7 (Andreas–Günther verdicts, audit row 35, UNVERIFIED by independent code).** I assessed whether the hostile referee's hand check suffices. Source: `state/blind/P-d300/reports/S7-lit.md`, "Proof check", Proposition 2, and the attribution list.
- **What the referee checked, against A&G's own conditions (deviancy (4) on p. 13, condition (5) on p. 19) and Beckers's (C4)/(C5):**
  - *Locusts:* "the unique maximal F′ is {¬D}, which omits the normal root ¬Q, so (4) fails". This is the essay's "the normal absence of rain must be left out of the facts". The referee also computed that A&G's Def. 1 counts the swarm a cause.
  - *Seedlings and Doorbells:* "A&G's negative verdict comes from (2), (3) and (5), not from (4)". This is the essay's "other conditions already exclude both".
  - *Simple switch:* handled by (5)/(2) at p. 25. The citation audit (A35) also confirmed this word for word.
- **Assessment: sufficient for submission.** There are two concordant derivations: the author's code, rerun by the formal auditor, and the referee's hand check. They are independent of each other and anchored in the source's stated conditions. The essay hedges the claims as "on my computation", and §7 is a side parallel that no theorem depends on.
- **Residual limits:**
  - It is a hand check, reported in summary form.
  - It was made on an earlier version whose Locusts model (D = ¬Q∧¬S) the final essay describes only in prose.
  - The referee states the no-deviancy verdict explicitly for A&G's preliminary Def. 1. For the final theory without (4) it is only implicit ("valid against (4) and (5)").
  - I confirmed from `state/ambitious/sources/andreas-gunther-2024-regularity.txt` that the final theory is the preliminary theory plus deviancy (4) and condition (5) (lines 463–471, 710–715). The essay's "with/without the deviancy condition" framing therefore matches the source's structure.
- **Risk:** low. The essay must not present these verdicts as independently machine-verified, and it does not.

## Required fixes

None.

## Advisory (not blocking)

1. If the Halpern 2016 pages from fetch `a4-audit-halpern-2016-pinpoints` arrive before the deadline, confirm the five pinpoints. If any fails, apply the matching audit fallback H1–H5.
2. The book-review record lists Halpern 2016 overlaps the essay does not credit: p. 83, §4.7 (pp. 126–127) and §4.1 (pp. 108–111). Adding them would be new content, so this is not a patch item. It is an originality risk the orchestrator may weigh.
3. Methodology report (report mode): `methodology/provenance.md` §4 is stale. It gives 5,540 words, the final is 5,581. It also says P1 had not been applied, but it now is. Ledger row 4.8 should record that Wysocki's content was checked against the retrieved text here. The second-system exposure disclosure and the §1.2 history must appear accurately.
4. Log the Wysocki verification in `methodology/log.md`. Done by this checker.
