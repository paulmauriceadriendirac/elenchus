PASS

# A5 compliance check: `final/A5/essay.md`

Mode: essay. Checked 29 October 2026 by the compliance agent. Target words: 5600. Redact list (CONFIG.md `redact:`): `paulmauriceadriendirac`.

Provenance of the checked text: the base is Astra A5 v7 (`state/external/submission-sourcechecked-20261029/A5-Holistic-Accuracy-v7.md`). `diff` against that base shows exactly three changed lines (abstract, §6 paragraph 1, D&M reference). These are the verbatim patches 1–3 of `citations_final.md`, as `final/A5/changelog.md` says. Nothing else differs.

## Checklist

### 1. Word count: PASS
`python3 tools/wordcount.py final/A5/essay.md --limit 6000 --target 5600` gives
`strict=5039 wordlike=5021 (footnotes=127; bibliography lines excluded=27) limit=6000 target=5600 -> OK`.
The count is 961 under the limit and 561 under the target. The target is not a minimum, so being under it is not a defect.

### 2. Injection check: PASS
`python3 tools/check_injection.py final/A5/essay.md --names "paulmauriceadriendirac" --judges-file state/panel/judges.txt` reports **No hard flags**. It raises two soft flags:
- **Mandelkern (3 mentions).** These are §1 "Dorst and Mandelkern (2022) derive filtered guesses …", §5 "(2022, §§3–4.1) already derive filtered guesses …", and the reference entry. All three are genuine citations of the closest prior work. On accuracy: the description of answer-value and filtering matches the authors' own Substack summary (quoted verbatim in citations_final A-D4). Belief as entailment by a best guess, at §4.1, is documented against the July 2021 draft in `state/audit/A5/good-guesses-comparison-20261029.md` (§3.1 pp. 9–12, §3.2 pp. 16–17, §4.1 pp. 21–22). The essay does not quote D&M. It says plainly that the numerical instantiation is its own ("not their printed numerical example"), and it concedes the overlap ("Neither the reversal nor the filtered-core structure is new").
- **Easwaran (3 mentions).** These are §1 "Easwaran (2016) proved this, using expected score as a tool for showing such belief states non-dominated …", §1 "credits both to Easwaran (p. 183)", and the reference entry. They are genuine citations. The v4 audit's patch 1 corrected the earlier overstatement (A2), and that correction is present.

Other checks: there are no HTML comments, and the only non-ASCII characters are § í û – ∎. There are no zero-width or invisible characters and no text addressed to machines.

### 3. Anonymity: PASS
I searched the essay case-insensitively for: the redact username, "dirac", the account email and "gmail", astra, claude, codex, gpt, openai, anthropic, elenchus, pipeline, competition, judge, panel, "AI", artificial, "language model", LLM, /home, github, reviewer, screen. There were **0 matches**. The essay contains no paths or institutions. The D&M reference note ("Section numbers cited follow the July 2021 penultimate author draft.") discloses scholarship, not process; it is patch 1 of `citations_final.md`. Footnote 2 ("All numerical claims were checked by exhaustive enumeration …") does not refer to authorship.

### 4. Structure: PASS
The essay has a title, an abstract, §§1–8, an appendix of proofs, a reference list of 10 entries and footnotes [^1]–[^4], each called once (lines 7, 41, 69, 77). In-text citations and references match both ways:
- Dorst 2019
- Dorst & Mandelkern 2022
- Easwaran 2016
- Holguín 2022
- Joyce 2009
- Leitgeb 2014
- Leitgeb 2017
- Levi 1967
- Rothschild 2023
- Wang 2025

All ten are cited and all ten are listed. There are no orphans, and years and spellings agree.

### 5. Scholarship: PASS
- **`citations.md` (v4 audit).** Patches 1–8 are present or superseded in the final text, as `citations_final.md` records under "Retention of v5 audit fixes". I confirmed by reading:
  - Easwaran wording (§1)
  - Levi with the singular "an answer"
  - "filtered" unquoted
  - Conservativeness on p. 185 and Variable Conservativeness on p. 191
  - p. 207
  - p. 190
  - "the process of forming beliefs in sequence"
  - Wang 182 (5–6)

  Its open items:
  - D&M is now covered by the documented draft comparison.
  - Easwaran was checked against the preprint and corroborated by Dorst p. 183. It was marked non-blocking.
  - The Leitgeb A10 sentence has been deleted from the text.
- **`citations_final.md` (delta audit, v5 to final).** It listed patches 1–3, and all three are applied verbatim (see the diff above):
  - Patch 1: D&M note, now "Section numbers cited follow …".
  - Patch 2: abstract, now "An earlier utility theory of guessing already generates …".
  - Patch 3: §6, now "In general, with uniform values, splitting …".

  It found nothing inaccurate. All 13 quotations are verbatim and all numerical claims N1–N9 check out exactly.
- **Remaining non-blocking item.** The fetch `a5-dorst-mandelkern-2022-good-guesses` is still open in `HUMAN_TODO.md`, so the published section numbering of D&M is unconfirmed. The reference note discloses that the numbering follows the draft, so the citation is not misleading. The auditor marked this "None required."

### 6. Human-input record and hygiene: PASS
- **Classification.** All 26 entries in `methodology/human_inputs.md` are classified: logistics, courier, method, generic-feedback or selection. None is `rejected-substantive`, so there was nothing to trace.
- **Substantive content.** The method entries (10-22 09:31, 10:01, 10:05; 10-21 20:44) are argument-neutral instructions about workflow and ambition. The 10-29 17:35 courier entry relays Astra's own status note, which is AI-originated and gives risk headings only, with no philosophical content. The 10-29 11:45 selection entry is the Gate A2 choice.
- **Hygiene.** `methodology/hygiene.md` records a clean Phase 0. There was no memory or profile content and no user-level instructions, `autoMemoryEnabled: false`, the personal connectors were never called, and the email was kept out of the deliverables.
- **Astra exposure disclosure.** Astra disclosed a context-exposure concern on 22 Oct (`state/external/ambitious-review-20261022/PROVENANCE.md`), and Astra outputs were quarantined (log 10-23 01:56). `PROVENANCE-CLARIFICATION.md` found no human philosophical contribution. The quarantine was lifted under the revised §1.2 (log 10-27 16:02), and the human confirmed the revised §1.2 at Gate A2 (log 10-29 11:45). This is a disclosed context-availability concern, not an identified human contribution. It is consistent with CLAUDE.md §1.2 as now adopted. The essay's base is Astra's v7, so this history must be disclosed in the methodology report (see the advisories).

### 7. Formal audit: PASS
`formal.md` (on v4) verified Theorems 1–4, their proofs, the case and every number. I compared all theorem and corollary statements, proofs, display equations and the definitions of ME, BI, RI and CI in v4 and v5 with the final text. They are **identical**; the only difference is the deletion of fn 5. Status of the formal patches:
- **P1 (required):** superseded. Fn 5 is deleted, and the new sentence "separable values $T_p=2$, $F_p=-1$ satisfy RI but give threshold $1/3$" is correct (citations_final N5).
- **P2 (required):** superseded. The false sentence "no non-Lockean score can" is gone. It is replaced by "A theorem explains why that stronger requirement excludes …".
- **P3:** present ("Truth-directedness and CI then give a single threshold above $1/2$.").
- **P4:** present verbatim (§4, last paragraph).
- **P5:** superseded. The abstract no longer quantifies over values. §1's "for every positive premium" does not quantify over values and is true by Theorem 1 with uniform values.
- **P6:** the sentence is deleted.
- **P7:** now applied ("with uniform values").
- **P8 (required):** the Leitgeb sentence is removed, and the Levi and D&M descriptions were checked in `citations_final.md`.

Citations_final N4–N9 recomputed the new formal and numerical claims in the delta (the D&M scores, the $n/(n+1)$ family, the Non-vacuity inferences). No mismatch is unresolved.

## Required fixes

None.

## Advisories (non-blocking)

1. **Methodology report (report mode).** It must state that A5's final base is Astra A5 v7, revised by a second AI system. It must also describe the Astra context-exposure disclosure, the 23 Oct quarantine, its lifting on 27 Oct and the human's confirmation on 29 Oct, matching the log. `A5-Methodology-v7.md` contains no account of human involvement; Astra itself said these reports are verification notes and not production reports. Also note that `good-guesses-comparison-20261029.md` contains a GitHub URL with the entrant's username. That file must not be quoted or linked in any deliverable.
2. **Optional wording, footnote 2.** It says all numerical claims were checked "by exhaustive enumeration of belief states". The D&M Jamesian scores in §5 were checked by exact arithmetic over the 8 propositions, which is a different method. A precise version would add "(and, for answer-values, over all propositions)". This does not affect compliance.
3. **When the D&M fetch arrives,** confirm §4.1 and the Holguín credit against the published version. If the published section numbering differs, update "(2022, §§3–4.1)" and remove the reference note, as `citations_final.md` instructs.
