# A5 final essay: delta citation audit

Audited file: `final/A5/essay.md`, compared with `state/drafts/A5/v5.md`, which was fully audited in `state/audit/A5/citations.md` and `formal.md`. Date: 29 October 2026.

## Summary

| Step | Items in the delta | Result |
|---|---|---|
| 1 Coverage | 10 references; all in-text citations | Complete both ways. Years and spellings match. Footnote [^5] was deleted together with its only call, so no footnote is left dangling ([^1]–[^4] are each called once). |
| 2 Existence/metadata | The only change is a note appended to Dorst & Mandelkern | `verify_refs.py`: 6 VERIFIED, 3 MISMATCH, 1 PROBABLE. These are the same flags the v5 audit resolved: online-first year vs issue year for Dorst 2019, Rothschild and D&M; a subtitle difference for Leitgeb 2017; Levi's 1976 hit is a review. No new reference was added. |
| 3 Quotations | 0 new quotations | No quotation changed in the delta. All 13 v5 quotations are still present verbatim. The essay still quotes nothing from D&M. |
| 4 Attributions | 14 new or reworded | 11 accurate. 1 accurate on a documented check of the draft plus the authors' summary, not re-verified here (A-D3). 1 oversimplified (A-D10, patch 2). 1 accurate but carries a process-style note (R1, patch 1). |
| 5 Pages/sections/numbers | D&M §§3–4.1; Holguín §§7.2, 8.1; 9 new numerical claims | All numbers recomputed exactly and correct. D&M section numbers come from the penultimate draft, and the reference note discloses this. |
| v5 fixes retained | 8 citation patches, 8 formal patches | All required fixes are present or superseded by safer text. Optional formal P7 was never applied (unchanged since v5). |

Sources used:
- Dorst 2019, *Mind* text (`state/ambitious/sources/dorst-2019-lockeans.txt`).
- Leitgeb 2014, published *Phil. Review* PDF from fitelson.org/current/leitgeb_stability.pdf: 41 pp., pp. 131–171, DOI on p. 131. Copy in the session scratchpad.
- Holguín 2022 (`state/ambitious/sources/holguin-2022-thinking-guessing.txt`).
- Dorst & Mandelkern's own Substack summary (kevindorst.substack.com/p/the-conjunction-fallacy-take-a-guess, 18 July 2020).
- The documented draft comparison `state/audit/A5/good-guesses-comparison-20261029.md`.

**The July 2021 penultimate draft of *Good Guesses* is not in the repository.** I searched `inbox/`, `state/`, `relay/`, the git history and the filesystem. Open-access attempts also failed: OpenAlex lists the paper as closed, and PhilArchive and Wiley returned 403. The high-priority fetch `requests/fetch/a5-dorst-mandelkern-2022-good-guesses.md` is still open in `HUMAN_TODO.md`, so I did not file a duplicate. Claims resting only on that draft are marked below.

## Step 1 — Coverage

| Reference | Cited in final | Notes |
|---|---|---|
| Dorst 2019 | §1, passim | OK |
| Dorst & Mandelkern 2022 | §1, §5 | OK |
| Easwaran 2016 | §1 | OK |
| Holguín 2022 | §1, §3, §6 | OK. Spelled with an accent throughout. |
| Joyce 2009 | §1 (via Dorst p. 192) | OK |
| Leitgeb 2014, 2017 | §1; §5 ("Levi and Leitgeb") | OK |
| Levi 1967 | §1, §5 | OK |
| Rothschild 2023 | §1 | OK |
| Wang 2025 | §1 | OK |

No uncited entries and no orphan citations. The §5 Leitgeb sentence that formal audit P8 flagged ("stability with threshold 1/2 is equivalent to …") has been removed.

## Step 2 — Existence and metadata

| Key | verify_refs | Resolution |
|---|---|---|
| Dorst 2019 | MISMATCH (registry year 2017) | Online first 2017, issue 128(509), January 2019 (page header in the source). Resolved in the v5 audit. OK |
| Dorst & Mandelkern 2022 | VERIFIED (registry 2021) | Issue 105(3), 2022, pp. 581–618, matching OpenAlex biblio. OK. The appended note is discussed under R1. |
| Easwaran 2016 | VERIFIED | OK |
| Holguín 2022 | VERIFIED | OK |
| Joyce 2009 | VERIFIED | OK |
| Leitgeb 2014 | VERIFIED | Confirmed against the full text: *Phil. Review* 123(2), pp. 131–171. |
| Leitgeb 2017 | MISMATCH (title similarity) | Registry title lacks the subtitle; DOI and year agree. Resolved in v5. OK |
| Levi 1967 | PROBABLE (1976 hit is a *Technometrics* review) | Open Library record (v5 audit). OK |
| Rothschild 2023 | MISMATCH (online 2021) | Issue 88(5), 2023. Resolved in v5. OK |
| Wang 2025 | VERIFIED | Issue 5–6 (v5 patch 8 retained). OK |

| ID | Item | Finding | Fix |
|---|---|---|---|
| R1 | D&M entry ends ". (Section references checked against the July 2021 penultimate author draft.)" | Disclosing that pinpoints follow a draft is good practice. "Checked" reads as a workflow note, and the draft's section numbering may differ from the published version. | Patch 1 (recommended) |

## Step 3 — Quotations

No quotations were added or altered in the delta. The 13 quotations the v5 audit confirmed are all present verbatim:

- Dorst pp. 192, 193 (×2), 194 (×2), 195 (×2), 190, 196 (×2), 179
- Holguín §7.2 (×2)

The term filtered is still unquoted (v5 patch 3 retained). Inside the D&M discussion, "Which horse wins?" and "Does horse 1 win?" are the essay's own example questions, not quotations.

## Step 4 — Attributions (new or reworded text)

| ID | Claim (location) | Evidence | Verdict | Fix |
|---|---|---|---|---|
| A-D1 | Rothschild (2023) gives additive scoring representations of Lockean belief; Wang (2025) gives expected-utility rules for deductively cogent belief states (§1) | Same substance as v5, audited from the published PDFs | accurate | — |
| A-D2 | "Levi (1967) accepts the consequences of an answer chosen by expected epistemic utility" (§1); Levi accepts all consequences of the selected proposition (§5) | Wang 2025 §5 reconstruction (v5 audit, A8): a single belief core chosen by maximizing expected epistemic utility. The singular "an answer" fixes the v5 problem with plural "answers". Levi's book itself was not read. | accurate (reliable secondary) | — |
| A-D3 | "Dorst and Mandelkern (2022) derive filtered guesses by maximizing expected answer-value and connect belief to their consequences" (§1). "(2022, §§3–4.1) already derive filtered guesses by maximizing epistemic utility and, following Holguín, connect belief to their consequences" (§5) | Maximizing expected answer-value and Filtering: the authors' Substack ("A guess is permissible only if it is filtered"; "Our two most important observations about good guesses come from Holguín's paper"). Belief as entailment by a best guess, at §4.1, pp. 21–22 of the July 2021 draft: documented in `good-guesses-comparison-20261029.md`. Holguín 2022's abstract corroborates the "following Holguín" part: to think p is to guess p; rational thinking is closed under entailment; "if … thinking just is believing, then all this goes for belief as well". I could not see the draft myself. | accurate per documented primary check; not re-verified in this audit (panel member Mandelkern) | None required. Confirm §4.1 and the Holguín credit when the open fetch arrives. |
| A-D4 | Jamesian expected answer-value $C(X)J^{I_Q(X)}$; $I_Q$ is the proportion of question cells ruled out; $J\ge1$ (§5) | Substack verbatim: informativity $Q_p$ is "the proportion of the complete answers to $Q$ that $p$ rules out"; a true guess's value is "$J^{Q_p}$"; "$J \ge 1$ … the _J_amesian value of informativity"; false guesses score 0. So the expectation is $P(p)J^{Q_p}$. The comparison file confirms this against the draft (pp. 10–15). $I_Q$ is the essay's own notation and is not attributed. | accurate | — |
| A-D5 | "This is an instantiation of their model, not their printed numerical example" (§5) | Comparison file: these numbers are not in D&M | accurate (properly hedged) | — |
| A-D6 | "Their model already reproduces the two belief sets in my main example" (§1); "Taking all consequences gives exactly the belief sets in Section 3" (§5) | Recomputed exactly (Step 5, N1–N3) | accurate | — |
| A-D7 | "Leitgeb (2014, 2017) connects rational belief to stably high credence and a strongest believed proposition" (§1) | Leitgeb 2014, full text. p. 131: the principles "are jointly satisfied if and only if rational belief is equivalent to the assignment of a stably high rational degree of belief". p. 135: "B_W is the least or strongest proposition that is believed". p. 136: Bel(X) iff B_W ⊆ X. p. 145: "Belief is determined by a proposition of resiliently or stably high subjective probability". For 2017, the abstract only (v5). | accurate (2014 now checked in the primary text) | — |
| A-D8 | "Levi and Leitgeb, like the single-guess entailment bridge, accept all consequences of the selected proposition" (§5) | Leitgeb p. 136 (as above). Levi as in A-D2. The D&M bridge as in A-D3. | accurate (Levi on secondary only) | — |
| A-D9 | "Holguín (2022) defends non-monotone, question-sensitive rational thinking" (§1) | Holguín abstract ("thinking is question-sensitive"); §5 "Thinking is non-monotonic" (v5 A15) | accurate | — |
| A-D10 | Abstract: "Earlier utility theories of guessing already generate similar behavior" | Only one utility theory of guessing (D&M) is shown in the essay to generate this behavior. Levi's rule was not computed for the example, and Levi's theory is one of acceptance, not guessing. Holguín's is not a utility theory. | oversimplified (plural overclaims) | Patch 2 |
| A-D11 | The record measure "meets the unrestricted truth-directedness condition motivating §4.2, but not the stronger marginal-value restriction introduced there" (§3) | Dorst p. 193, cases (ii)/(iii): adding a true belief gives "a higher score"; then "Write t as $T^{B_0}_p$—the value, relative to $B_0$, of adding a true belief in p" names a single number. This matches the v5-audited quantifier-gap reading. | accurate | — |
| A-D12 | "Dorst's fixed-context conclusion does not itself require those thresholds to survive changes of space" (§6); "Dorst's proposition-specific values can accommodate contextual changes" (§6) | Prop. 5 delivers values "in a context" (p. 195, v5 A20/A21). On p. 190 the question "adjusts them (within reason) until it gets one". | accurate | — |
| A-D13 | "Holguín instead allows the salient alternatives to affect rational thinking directly (2022, §§7.2, 8.1)" (§6) | §8.1 "Thinking as question-sensitive"; §7.2 shows that whether p is thought depends on more probable alternatives (v5-audited at these sections) | accurate | — |
| A-D14 | Conclusion: "Earlier theories already make belief guess-like" (§8) | Holguín (thinking = guessing = believing, abstract); D&M §4.1 (as A-D3) | accurate | — |

## Step 5 — Page/section numbers, dates, and new numerical claims

| Item | Check | Result |
|---|---|---|
| D&M "(2022, §§3–4.1)" | Comparison file: §3.1 (utility foundations), §3.2 (Filtering), §4.1 (belief), in the July 2021 draft | Plausible and disclosed as draft numbering. Not re-verified here, and published numbering is unconfirmed (open fetch). Keep, with patch 1. |
| Holguín (2022, §5), (§7.2), (§§7.2, 8.1) | v5 audit | OK |
| All Dorst page references | Unchanged from v5 (p. 207 and p. 190 fixes retained) | OK |
| N1 Jamesian scores at C = (.70,.15,.15), J = 125/64: {w1} = 35/32, {w1,w3} = 17/16 | Exact rational arithmetic over all 8 propositions | Correct. {w1} is the unique maximum; {w1,w2} ties {w1,w3} at 17/16; W = 1. |
| N2 At C' = (.75,.01,.24): {w1} = 75/64, {w1,w3} = 99/80 | Same | Correct. {w1,w3} is the unique maximum; W = 1; {w1,w2} = 19/20. |
| N3 All consequences of the two guesses = Section 3 optima | {1,12,13,W} and {13,W} | Correct |
| N4 Two-world record threshold $(\beta-F)/(D+\beta)$ = 5/6 | β = 3, T = 1, F = −2 | Correct (unchanged from v5) |
| N5 Separable T = 2, F = −1 gives threshold 1/3 | −F/(T−F) | Correct. This replaces the v5 "no threshold in (1/2,1)" sentence, and remains true. |
| N6 Family T = 1, F = −n: threshold n/(n+1), Lockean on each space, violates RI | 2/3, 3/4, 4/5. At C(p) = 0.7, p is believed after coarsening to two worlds but not on three. | Correct. CI holds for n ≥ 2. |
| N7 "unique optimum … permitted" from Non-vacuity + MEA | MEA excludes every non-optimal state; Non-vacuity requires one permitted state | Valid |
| N8 "In Theorem 1 all optima agree on the relevant verdict" | Theorem 1: a unique optimum at $C_c$; no optimum contains $\mathbf 1$ at the other credence | Valid |
| N9 Scoring a state by its conjunction's Jamesian value violates strict marginal gains | Adding a superset of the core leaves the conjunction, and so the score, unchanged | Correct |

## Retention of v5 audit fixes

| Fix | Status in final |
|---|---|
| Citation patch 1 (Easwaran, "using expected score as a tool …") | Present (§1) |
| Citation patch 2 (Levi; no "relief from agnosticism", no plural "answers") | Present in reworded form (A-D2) |
| Citation patch 3 (filtered unquoted) | Present |
| Citation patch 4 (Conservativeness p. 185 / Variable Conservativeness p. 191) | Present (§2) |
| Citation patch 5 (p. 207) | Present |
| Citation patch 6 ("until it gets an answer" p. 190) | Present |
| Citation patch 7 ("the process of forming beliefs in sequence") | Present |
| Citation patch 8 (Wang 182 (5–6)) | Present |
| Formal P1 / footnote 5 | Superseded. The minimality claim and footnote 5 are deleted, and the new CI sentence is correct (N5). |
| Formal P2 ("no truth-directed, conservative non-Lockean score can") | Superseded by a weaker claim ("A theorem explains why …"). Correct. |
| Formal P3 (two-world threshold sentence) | Present in reworded form |
| Formal P4 (family ME/BI) | Present (§4) |
| Formal P5 (abstract) | Superseded. The new abstract no longer makes the "every positive premium" claim. |
| Formal P6 (", except at ties") | Deleted along with the sentence |
| Formal P7 (optional: "with the values of Section 3, splitting …") | Not applied, as in v5. The claim holds only for credence-determined (for example uniform) values. Optional patch 3. |
| Formal P8 (Leitgeb §5 sentence; D&M and Levi checks) | Leitgeb sentence removed. D&M and Levi checked above. |

## Patch list (apply to `final/A5/essay.md`; each OLD string occurs exactly once)

1. **(recommended) References, Dorst & Mandelkern.**
   OLD: `https://doi.org/10.1111/phpr.12831. (Section references checked against the July 2021 penultimate author draft.)`
   NEW: `https://doi.org/10.1111/phpr.12831. Section numbers cited follow the July 2021 penultimate author draft.`

2. **(recommended) Abstract.**
   OLD: `Earlier utility theories of guessing already generate similar behavior;`
   NEW: `An earlier utility theory of guessing already generates similar behavior;`

3. **(optional; carried over from formal audit P7) §6.**
   OLD: `In general, splitting a world of credence zero`
   NEW: `In general, with uniform values, splitting a world of credence zero`

No other changes are needed. When the open fetch `a5-dorst-mandelkern-2022-good-guesses` arrives, confirm D&M §4.1 (belief as entailment by a best guess, credited to Holguín) and the published section numbering. If the published numbering differs, replace `(2022, §§3–4.1)` with the published numbers and delete the sentence added by patch 1.
