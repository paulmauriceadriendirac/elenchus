PASS

# A6 compliance re-check (mode: essay)

**Target:** `state/external/submission-final-review-20261029/A6-Free-Evidence-v6.md` (the second system's v6), plus its PDF `A6-Free-Evidence-v6.pdf`. This is not `final/A6/essay.md`.
**Date:** 2026-10-30
**Previous record (2026-10-29, on `final/A6/essay.md`):** FAIL, for two reasons: (a) the Hong 2026 §§1–3 attribution at l.19 was unverified; (b) the *Deference Done Better* paragraph at l.21 had not been audited.

**How v6 differs from `final/A6/essay.md`** (`git diff --no-index --word-diff=plain`):
- The availability premise is added to the thesis (l.15) and the conclusion (l.163).
- "(§6.1)" becomes "(see §6.1 below)" (l.31).
- The "continuous analogue of Lemma 2" sentence is removed and replaced by "Part (ii) depends on the available questions. It does not establish the same necessity result for the second weighing alone." (l.91).
- The §6.2 pragmatic-encroachment passage is rewritten, and its generic-prior generalization is removed (l.151).
- The Dorst 2020 and Dorst et al. 2021 references are swapped into the correct order.

## Checklist

### 1. Word count: PASS (over target)
`python3 tools/wordcount.py <v6> --limit 6000 --target 5600` gives strict=5853, wordlike=5827, footnotes=0, 36 bibliography lines excluded. Result: OVER_TARGET. That is 147 under the 6,000 limit and 253 over the 5,600 target, which does not block submission.

### 2. Injection and panel mentions: PASS
`check_injection.py <v6> --names "paulmauriceadriendirac" --judges-file state/panel/judges.txt` reports no hard flags. Soft flags: Salow 46, Hawthorne 7, Goldstein 3, Fitelson 1, the same as before.
- **Salow, Hawthorne and Goldstein.** These mentions are unchanged from the audited text. Verdicts: citations.md, and citations_final.md O1, O2, O6–O12.
- **Fitelson.** Fitelson appears only in the DDB reference entry. That paper is now verified against its full text (item 5).

Hidden-text scan of the .md:
- No zero-width, soft-hyphen or control characters.
- No HTML comments.

PDF (11 pages):
- Metadata has only a Title; Author, Creator and Producer are null.
- The only annotations are 4 /Link entries, to the two Wiley DOIs.
- The extracted text contains the v6 sentences and does not contain "continuous analogue".

### 3. Anonymity: PASS
I grepped the .md and the PDF text for the following. There are no hits apart from the two DOI URLs in the references:
- the redact value and the account email;
- github, astra, claude, codex, gpt, openai, anthropic;
- competition, judge, panel, pipeline, elenchus, "AI", "language model", /home.

There is no reference to the entrant and no mention of AI authorship.

### 4. Structure: PASS
- The essay has a title, an abstract (l.3), numbered sections, an appendix and references.
- Citations and references match in both directions, with 17 works each. This is unchanged from citations_final.md Step 1, because v6 adds and removes no citation.
- The earlier optional points are now fixed: Dorst 2020 precedes Dorst et al. 2021, and the §6.1 cross-reference is reworded.

### 5. Scholarship: PASS (both previous failures closed)
**(a) Hong 2026, l.19: closed.**
- The text reads: "Hong (2026) gives two arguments suggesting that whatever the normality framework captures is not action-guiding."
- This is citations_final.md P2 verbatim. P2 is a calibration of citations.md P4.
- The Crossref abstract, as quoted in the audit, reads: "we give two arguments that suggest that whatever concept the normality framework is capturing ... it is not action-guiding".
- No §§1–3 content is attributed to Hong anywhere in v6.

**(b) *Deference Done Better*, l.21: closed.** The delta audit read the published Wiley text, and P3–P6 appear verbatim in v6. I spot-checked each claim against `state/ambitious/sources/dorst-etal-2021-deference-done-better.txt`:

| Claim in v6 | Where it is in DDB | Verdict |
|---|---|---|
| Theorem 2.2: Total Trust iff Value | l.414 (p.107): "π totally trusts ⟨W,P⟩ iff π values ⟨W,P⟩" | matches |
| Value gloss: in every decision problem, each recommended strategy has π-expected utility at least that of any option | l.288 (p.105): "Value: If S is recommended for 𝒪, then for all O ∈ 𝒪: 𝔼π(S) ≥ 𝔼π(O)" | matches |
| Weak Value | l.1803 (p.133): existential quantifier over recommended strategies | matches |
| Appendix B (§§B.1–B.2) | l.1815: §B.1 "Weak Value ⇔ Total Trust ⇔ Modestly Informed"; l.2015: §B.2 "Weak Value ⇔ Value" | matches |
| Theorem 4.1, "modestly informed", convex hull | l.866 (p.118): "π totally trusts ⟨W,P⟩ iff each 𝑖 ∈ C_π is modestly informed and π is in their convex hull"; C_π is defined in n.54 | matches; "the relevant candidate expert functions" is a fair gloss of C_π |

I also checked the essay's own two-way step:
- Under full support, P_s fixes the post-answer ken. KDT with a fixed tie order is therefore a function of P_s that maximizes 𝔼_{P_s}, which makes it a recommended strategy.
- Safety in every A gives Weak Value.
- Value, which quantifies over all recommended strategies, gives V_x ≥ 0 for KDT's strategy.

The paragraph is accurate and complete. The citations.md items are still all applied or superseded, as recorded in the previous check. The v6 edits add no new attribution.

### 6. Human-input record and hygiene: PASS
- `methodology/human_inputs.md` has 26 entries, all classified: 16 logistics, 4 courier, 4 method, 1 generic-feedback, 1 selection. None is rejected-substantive, so there is nothing to trace.
- The new entry, 2026-10-30T02:55:32Z, is logistics: "okay let's do the final check on astra's work."
- The v6 changes are AI-originated. They are the second system's finishing pass, described in `VERIFICATION.md` l.12 and README l.18. No human content enters them.
- `methodology/hygiene.md` is unchanged and clean (Phase 0).
- The 23 October context-exposure history stays preserved as recorded previously: log.md l.60, l.76 and l.90.

### 7. Formal audit and the changed sentences: PASS
`state/audit/A6/formal.md` has no unresolved mismatch. P1–P5 and P8 are still present in v6. The v6 changes remove the two items the previous record listed as residual and unproved:
- #13 / P6: the continuous analogue of Lemma 2.
- #38 / P7: the generic-prior encroachment generalization.

The removals narrow the claims and do not introduce new ones.

I checked each changed sentence against the essay's §3, §4 and appendix, and against `state/audit/A6/formal/bjorn_numeric.out`.

**Encroachment passage (§6.2), sentence by sentence:**

| Sentence | Check | Verdict |
|---|---|---|
| "Knowledge-conditioned evaluation strictly prefers acting now" at ten-to-one | §3 gives the KDT value of the free weighing as "about −0.05"; the formal run gives −0.0496 at c=1.96, L=10 | consistent: negative means acting now is strictly preferred |
| "ordinary Bayesian evaluation strictly prefers looking (§3)" | §3: "by Good's theorem the second weighing has positive value for her"; formal run: Bayesian value 0.1855 > 0 | consistent |
| Bet alone: "win probability 1" under KDT and "(0.95)" under evidence | In a normal situation the ken is {δ≤c²}, and by Cauchy–Schwarz in A.5 \|e₁\|≤c throughout, so the probability is 1. P(\|e₁\|≤c)=0.9500, and §3 gives EV 0.45 | consistent |
| "conditional on extending the criterion ... no general result about every graded state follows" | This correctly withdraws the claim that formal #38 had marked as argued only | correct calibration |

**Other changed sentences:**

| Change | Check | Verdict |
|---|---|---|
| l.91: "It does not establish the same necessity result for the second weighing alone." | Agrees with §3 (iii): "Theorem 2 and its corollary are finite results using the questions defined in §4; the second weighing is not one of them." | consistent |
| Thesis (l.15) and conclusion (l.163) availability premise | Theorem 1(b) and Theorem 2 state "if it is available". The gapped direction needs no availability, so the conjoined premise is correct, if slightly stronger than needed. The abstract already had "Given suitable questions". | consistent |

## Required fixes
None blocking.

Recommended before submission (orchestrator):
1. Make v6 the deliverable. Copy it to `final/A6/essay.md` as a new version, keeping the current file. Record the v6 delta in `final/A6/changelog.md`, credited to the second system's finishing pass. The methodology report must reflect that the final A6 text comes from that system's v6.

Optional, for clarity:
2. In §6.2, the claim "win probability 1" holds at normal situations (δ≤c²), as in §3. Consider "Offered the ten-to-one bet alone at a normal situation, ...".
3. In §6.2, "withdraws knowledge whenever these two evaluations change the preference" reads awkwardly. Consider "whenever the difference between these two evaluations changes his preference", which matches the quoted criterion. This is word-neutral.
