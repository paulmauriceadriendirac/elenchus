ADOPT (with patch P1 applied, unless the pending Halpern p. 85 fetch confirms the v10 sentence before submission)

# A4 v10 delta audit (31 Oct 2026)

- Baseline: `final/A4/essay.md` (v8; passed the citation, formal and compliance audits).
- Candidate: `state/external/submission-ready-20261030/A4-Causation-v10.md`, plus its PDF `A4-Causation-v10.pdf`.
- Diff: `git diff --no-index --word-diff=plain` and line `diff`.

## Summary counts

- **Changed passages:** 13.
  - 9 are new or rewritten prose: new sentences in §1, §2 (×2), §3 (×2), §6, the §5 heading, and the §5 sentence "The required separation is easy to construct."
  - 1 is a new attribution with a page number (Halpern 2016, 85).
  - The rest are paragraph splits only: §1 Wysocki, §2 filters, Theorem 1 proof, §5 Seedlings, §6, §7, Appendix. One trailing blank line was also removed.
- **References:** 14 in v8, 14 in v10, byte-identical. New in-text citations: 1, "(2016, 85)". Coverage is still complete.
- **Quotations:** 16 in v8, 16 in v10, an identical multiset. None is new or altered.
- **Math:** 193 spans, identical multiset. Every Theorem, Lemma and Corollary statement is identical. The Theorem 1 proof text is identical up to whitespace; it is only split into three paragraphs.
- **New attribution:** 1, unverifiable from any retrieved copy. Fallback patch P1; fetch request filed.
- **Formal claims:** none new or altered. The independent HP audit was rerun and its output is identical to the stored one.
- **Word count:** 5,807 strict (limit 6,000, so OK). It is above the internal target of 5,600 but below the limit. v8 was 5,581.
- **Injection and anonymity:** no hard flags. The only soft flag is the panel surname "Günther" (8 mentions). All 8 are pre-existing Andreas and Günther 2024 citations; none is new or altered in v10. No identity, pipeline, competition or AI mentions. PDF metadata has only the title.

## Step 1. Coverage

| Item | v8 | v10 | Result |
|---|---|---|---|
| References entries | 14 | 14, byte-identical | OK |
| In-text citation tokens | 46 | 47 (adds "(2016, 85)", which resolves to Halpern 2016) | OK; entry exists |
| Uncited entries | 0 | 0 | OK |

Evidence: `state/audit/A4/v10/invariants.py` → `state/audit/A4/v10/invariants.out`.

## Step 2. Existence and metadata

`python3 tools/verify_refs.py state/audit/A4/v10/refs.json` → `state/audit/A4/v10/verify_refs.{json,md}`. Totals: 11 VERIFIED, 2 NOT_FOUND, 1 MISMATCH. This is the same pattern the v8 audit hand-resolved.

| Entry | Tool | Hand check (31 Oct) | Result |
|---|---|---|---|
| Halpern 2015, arXiv:1505.00162v1 | NOT_FOUND (OpenAlex 429) | Downloaded v1. Its header reads "arXiv:1505.00162v1 [cs.AI] 1 May 2015 A Modification of the Halpern-Pearl Definition of Causality, Joseph Y. Halpern". | OK |
| Beckers 2026, arXiv:2606.24832v1 | NOT_FOUND (OpenAlex 429) | export.arxiv.org abstract page: title "Difference-Making without Making a Difference", author Beckers, Sander, dated 2026/06/23. | OK |
| Beckers & Vennekens 2018 | MISMATCH (year) | Registry year 2016 is the online-first date. The print date is 2018, 195(2). This was resolved in the v8 audit. | OK |
| All other 11 | VERIFIED | — | OK |

## Step 3. Quotations

No quotation was added or altered: the 16 quoted strings form an identical multiset in v8 and v10. All v8 quotation checks carry over.

## Step 4. Attributions in changed passages

| # | v10 passage | Source check | Classification | Fix |
|---|---|---|---|---|
| A1 | "Halpern already illustrates the problem of a reliable backup with an automatic rock-throwing machine (2016, 85)." (§5, before *Sprinkler*) | See the next table. No retrieved copy of the book, and the designated record does not contain the claim. | **Unverifiable** | P1 |
| A2 | "…this is Halpern and Hitchcock's first guideline applied across models" | The text is unchanged; only the paragraph boundary moved. Covered by the v8 audit. | accurate (carried over) | — |
| A3 | §6 new sentence: conformity means conformity to the original non-root equations. | Not an attribution. It is consistent with Xiao and Xiong's Definition 12: "A world is said to be available in a causal model if it does not violate the structural equations of the model". Their worked example checks the original equations (TR = EF, …). Source: `inbox/sources/xiao-xiong-2026-hitchcock-refinement.txt` ll. 451–462. | accurate | — |
| A4 | §1 backup-route paragraph; §2 "A witness is thus a counterfactual test…"; profile gloss; §3 calibration sentence; "The equality concerns the information available to the filter…" | No author attribution. Checked against the essay's own definitions: the first four listed cases (prevention, chain, Boulder, short circuit) are exactly the four "calibrating verdicts" used in §4. | accurate | — |
| A5 | §7 split-off sentence "Section 4 shows… counterpart of Beckers's dilemma" | v8 text, moved only. It covers Andreas and Günther (panel); no wording changed, so the v8 full-text audit stands. | accurate (carried over) | — |

**Verification basis for A1.**

| Basis | What it supports |
|---|---|
| `state/external/submission-book-review-20261028/Halpern-Originality-Review.md`, the designated record. Its scope: "chapter 3, including its notes" of the printed book (printed p. 84 = PDF p. 95). | Example 3.2.6, pp. 84–85: "If the witness in which Billy throws but does not hit is too abnormal, Suzy's throw ceases to be a cause by itself under the modified definition, while the conjunction of the two throws becomes a cause. Making Billy's accuracy explicit sharpens the problem." It does **not** mention a machine, an automatic thrower, or p. 85 on its own. This supports v8's existing citation of pp. 84–85, but not A1. |
| Pp. 90–91 (Example 3.4.3, route models) | Cited in the other system's 30 Oct anchors. pp. 90–91 is not cited in v10's changed passages, so it is not needed. |
| `state/external/submission-ready-20261030/FINAL-REVIEW.md` (30 Oct) | The only source of the machine claim: "Halpern's automatic rock-throwing machine on page 85 already illustrates the reliability difficulty for a backup mechanism". `VERIFICATION.md` says only "Revisited the primary-source passages". There is no extract, quotation or page image. It is an unsourced one-line assertion by the revising system. |
| Retrieval attempts 31 Oct | Halpern 2015 arXiv: no machine example (only a voting machine and Turing machines). Halpern and Hitchcock 2015 arXiv: no rock-throwing machine. MIT Press and DOAB: 403. OAPEN: 403. Cornell author page `causalitybook-ch1-3.html`: HTTP 503 (two hosts). Web search: no snippet. |

Under rule 1.3 the sentence cannot stay on this basis. Two things follow:

- Fetch request filed: `requests/fetch/a4-v10-halpern-2016-p85.md` (high). It complements the still-open `a4-audit-halpern-2016-pinpoints.md`.
- Fallback P1 keeps the acknowledgement v10 intended. It reuses the record-supported pp. 84–85 content, which v8 §1 already cites.

## Step 5. Page numbers and dates

| Citation | Status |
|---|---|
| Halpern 2016, 85 (new) | Unverifiable. Removed by P1. P1's pinpoint is 84–85, the range the designated record supports and v8 already cites. |
| All other page numbers and dates | Unchanged: the multiset of numbers outside math is identical apart from "2016" and "85" in A1. Carried over from the v8 audit. |

## Formal invariance

| Check | Result |
|---|---|
| Math spans (193) | Identical multiset |
| Theorem 1, Theorem 2, Corollary and Lemma statements | Identical |
| Theorem 1 proof | Same text, whitespace-normalised. Split into Suzy, Tracks and Doorbells paragraphs; ∎ still ends the Doorbells case. |
| New formal-sounding sentence: "Requiring only that a world solve the intervened equations would impose no comparable restriction: every witness already does that." | True by definition: the witness world is the solution under the witness intervention. The Lemma's proof already uses conformity to the original non-root equations, so the sentence makes explicit what the Lemma means without changing it. |
| `state/audit/A4/formal/hp_audit.py` rerun → `state/audit/A4/v10/hp_audit_rerun.out` | Byte-identical to the stored `hp_audit.out`: 94 checks, 91 pass, 3 "fail". The 3 are the designed negative controls ("read as linear orders … expected FALSE"); v10 still says "total preorders". |
| PDF (`A4-Causation-v10.pdf`, 11 pp.) | Contains all new sentences, including A1 (hyphenated "rock- throwing" at a line break). Metadata: title only, no author or creator. |

## Patch list (apply mechanically, to both the .md and a rebuilt PDF)

**P1** (§5, the paragraph immediately before the *Sprinkler* block quote).

Old:
> Halpern already illustrates the problem of a reliable backup with an automatic rock-throwing machine (2016, 85). Sprinkler applies that concern to a comparison with switching.

New:
> Halpern (2016, 84–85) already notes that Suzy's throw stops being a cause by itself when Billy's throwing without hitting is too abnormal. Sprinkler applies that concern to a comparison with switching.

Revert P1 only if an auditor checks the fetched printed p. 85 (`requests/fetch/a4-v10-halpern-2016-p85.md`) and records that it presents an automatic rock-throwing machine as a reliable-backup illustration. After P1 the word count is about 5,812, still ≤ 6,000.

No other patches. Paragraph splits are cosmetic and harmless.

## Grok Review 1 (relay/inbox/grok-reviews-20261031.md): requested revisions vs v10

v10 is dated 30 Oct and predates the review (31 Oct), so it was not written in response to it.

| # | Grok request | Addressed in v10? | Where / note |
|---|---|---|---|
| 1 | Defend the significance of the anonymity baseline (introduction and §5): argue that transferable policies are a natural class | **Partly.** Mostly pre-existing. | v8 already had "Anonymity is a baseline…" (§2) and "Why it matters" (§1). v10 adds the backup-route framing paragraph (§1), "The equality concerns the information available to the filter…" (§4) and the §5 retitle. There is still no positive argument that anonymous policies are attractive (e.g., anti-post-hoc, mechanism-statistical). |
| 2 | Parts of causes: extend the dilemma or justify single candidates | **No new change.** Acknowledged since v8. | §4 after Theorem 2: "Strictly, the flip remains part of a cause… I set it aside and state the dilemma for single candidates". The Corollary excludes Billy from "every cause", and the 355-preorder computation covers parts. No philosophical reason is given for the focus. |
| 3 | Event coding: say when it is independently motivated | **No.** | Unchanged: (P2) in §5, Objection 2. |
| 4 | Proofs: uniqueness lemmas with explicit sufficiency checks; say whether code is available | **Minimal.** | v10 only splits the Theorem 1 proof by case. The modified-definition uniqueness for Tracks and Doorbells is still asserted, not argued. The appendix covers the older definitions. Code availability is not stated; any link would raise anonymity issues. |
| 5 | State the Wysocki increment crisply in the introduction | **Already addressed in v8.** | §1 "Closest work and increment" plus the Wysocki paragraph. v10 only splits that paragraph. |
| 6a | Table of actual and witness categories | **No.** | — |
| 6b | Intuitive gloss on the g-identity | **Already in v8.** | "because a frozen default's change n→f telescopes into n→l and l→f". |
| 6c | Gallow and model aptness: admit the dilemma is partly about representation | **Mostly already in v8.** | "Whether such representations can be selected … is a question about model aptness… I do not settle that question here" (§5). The Seedlings timing reply says "representation, not normality, separates…". v10 adds nothing here. |
| 6d | Andreas and Günther: does the regularity theory face an anonymity-like restriction? | **No.** | v10 only splits off the last sentence of §7. |

## Files

- `state/audit/A4/v10/invariants.py`, `invariants.out`: math, quotation, citation and number invariants.
- `state/audit/A4/v10/refs.json`, `verify_refs.json`, `verify_refs.md`.
- `state/audit/A4/v10/hp_audit_rerun.out`.
- `requests/fetch/a4-v10-halpern-2016-p85.md`.
