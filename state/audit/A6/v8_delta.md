ADOPT

# A6 v8 delta audit (citation, formal, compliance)

- **Baseline (audited):** `final/A6/essay.md` (v6; strict 5,853 words).
- **Candidate:** `state/external/submission-ready-20261030/A6-Free-Evidence-v8.md` (strict 5,948 words).
- **Date:** 2026-10-31.
- **Scripts and outputs:** `state/audit/A6/v8/worddiff.py` (whitespace-insensitive word diff), `state/audit/A6/v8/ceu_check.py` with output `ceu_check.out` (exact rational arithmetic), `state/audit/A6/v8/refs_v8.verification.{json,md}`.

## Verdict in brief

v8 changes no theorem, lemma, proposition, displayed equation, appendix proof, quotation, page or theorem locator, reference entry, or number. `git diff --word-diff` mostly shows paragraph splits. Normalising whitespace leaves 19 word-level edits in 12 passages (table below). Ten passages are expository glosses or less sweeping wording. Two need attention:

- **Theorem 3 construction (v7→v8).** This edit **corrects a real error in the audited v6.** v6 said that "every comparison CEU makes, now or later, uses ordinary knowledge". That is false in v6's own three-state example. When the original bet β is compared with looking, the two differ only on {b,c}. CEU's conditional ken is then {b,c}, not the ordinary ken {a,b}. So KDT ranks β above looking by +1/2, while CEU ranks it below by −9/2 (verified exactly). v8 claims only the agreement the theorem needs: β₁ against looking (+7/10 under both) and comparisons among the primitive acts, which differ pairwise everywhere. The theorem stays true. v8 drops v6's "no cycle can arise", but I checked that the example has no CEU preference cycle: β₁ beats every other option, so it is a Condorcet winner. In the general construction the same holds, because β₁ beats β and declining (primitive acts, KDT agreement) and beats looking.
- **§6.2 "rank the available options differently".** This follows the quoted Fantl–McGrath/Weatherson criterion ("affects your preferences over available options") more closely than v6's "change the preference", so it is an improvement.

Every other check passes. The word count is 5,948 ≤ 6,000; that is over the pipeline target of 5,600, but the baseline was also over it (5,853). The injection check shows no hard flags. The anonymity grep finds nothing. The PDF text matches v8. No patch is required. One optional precision patch is listed below.

## Summary counts

| Step | Items in delta | Result |
|---|---|---|
| 1 Coverage | 0 new or altered citations | References section byte-identical to v6 (`diff` of the `## References` block: identical). All in-text author–year pairs unchanged. |
| 2 Existence/metadata | 0 new or altered entries | Nothing new to verify. `verify_refs.py` re-run on `state/drafts/A6/refs.json`: 11 VERIFIED, plus Hong2024 MISMATCH (year) and Geanakoplos1989 PROBABLE (year). Both are unchanged from the baseline and were resolved in earlier audits (`citations_final.md`, `compliance.md`: Hong online 2022 / issue 2024; Geanakoplos cited as CFDP 914 with the 2021 revision noted). |
| 3 Quotations | 0 new or altered | Every quoted string in v8 is identical to v6, so earlier word-for-word checks stand. |
| 4 Attributions | 4 altered (intro ×2, §6.2 ×2) | 4 accurate. |
| 5 Page/theorem numbers | 0 new or altered | None in changed text. |
| Formal | 1 altered formal-explanatory claim (Theorem 3 construction); 2 glosses of definitions; 1 scope word ("finite") | All correct; recomputed. |
| Compliance | wordcount; check_injection; anonymity | 5,948 ≤ 6,000 (52 headroom). No hard flags. Soft flags are panel surnames in genuine citations only (Salow, Hawthorne, Goldstein, Fitelson), as in v6. No anonymity hits. |

## Delta table (all word-level edits, whitespace-normalised)

| # | Location | v6 → v8 | Check | Verdict |
|---|---|---|---|---|
| D1 | §1 ¶1 | "offers the most economical recent dissolution" → "offers a dissolution" | Removes an unverifiable comparative. | OK (improves calibration) |
| D2 | §1 ¶3 | "The most developed proposal" → "One proposal" | Same. | OK |
| D3 | §1 ¶3 | "once knowledge is modeled by the most developed formal theory of inductive knowledge, the normality framework of Goodman and Salow (2023, 2025)" → "when knowledge is modeled in Goodman and Salow's (2023, 2025) normality framework" | Citation years unchanged; superlative removed. | OK |
| D4 | §2 after "ken" | + "This is the set of possibilities one has not ruled out by knowledge; a smaller ken means knowing more." | One knows p iff $K_E(x)\subseteq p$ (l.35), so a smaller ken means more knowledge. | OK |
| D5 | §2 *Gapped* | + "The gap must separate every retained possibility from every excluded one, not merely the most normal possibilities from the least normal." | Restates the ∀∀ definition on the same line. | OK |
| D6 | §4 opening | + "The proof separates two tasks … The first lemma handles the danger; the next two provide the sufficient conditions." | Lemma 1 is the cost lemma. Lemma 2 states the sufficient condition (laminar); Lemma 3 shows that K-normality kens satisfy its structural clauses. "Provide the sufficient conditions" is loose but not false. | OK (optional precision patch P1) |
| D7 | §4 Corollary gloss | "condition on in graded models" → "in finite graded models" | Matches Corollary (ii), "In a finite graded model". | OK |
| D8 | §5.1 opening | + "The three proposals differ in what they treat as the relevant hypothesis: a difference in payoff, a change of decision, or a particular answer." | CEU: $D=\{u_\ell\neq u_a\}$; VER: $D_b$, glossed in the essay (l.143) as "that the evidence would change what one does"; ANS: cells. | OK |
| D9 | §5.2 Theorem 3 construction | "so every comparison CEU makes, now or later, uses ordinary knowledge, CEU agrees with KDT, and no cycle can arise." → "so CEU agrees with KDT when comparing the present best act with looking and when choosing among the primitive acts, now or later." | See formal checks F1–F3. v6 sentence false; v8 sentence true and sufficient for Theorem 3. | OK; corrects a v6 error |
| D10 | §5.2 | "It fails elsewhere." → "A five-state case shows its limitation." | Five-state example unchanged and recomputed (F4). | OK |
| D11 | §6.2 | "Offered the ten-to-one bet alone," → "alone at a normal situation," | The win probability is 1 only where the ken is $\{\delta\le c^2\}$, which implies $|e_1|\le c$. At abnormal situations the ken is larger. The qualifier is correct and needed. | OK |
| D12 | §6.2 | "while ordinary Bayesian evaluation strictly prefers looking" → "while the latter strictly prefers looking"; "whenever these two evaluations change the preference" → "rank the available options differently" | "The latter" = evidence-conditioned evaluation = the fallibilist of §3. The new wording follows the Salow-quoted criterion ("affects your preferences over available options", Salow 2025, 24 n. 3; quotation unchanged and verified earlier). | OK |

Provenance of the delta: D9 is the only v7→v8 edit (word diff of `submission-final-20261030/A6-Free-Evidence-v7.md` against v8). D1–D8 and D10–D12 entered in v7.

## Step 1 — Coverage

| In-text citation | Entry | Status |
|---|---|---|
| All (unchanged) | References block identical to v6 | OK, coverage carried forward from `citations_final.md` and `compliance.md` |
| Goodman and Salow's (2023, 2025) (D3, reworded) | both entries present | OK |

## Step 2 — Existence and metadata

| Entry | verify_refs | Note |
|---|---|---|
| none new or altered | — | Re-run for confirmation: `state/audit/A6/v8/refs_v8.verification.md`. Results are unchanged from the baseline. Dorst et al. 2021 (not in the stale `refs.json`) was VERIFIED in `citations_final.md` (Crossref 10.1111/phpe.12156; vol. 35, 99–150). |

## Step 3 — Quotations

| Quotation | Changed? | Status |
|---|---|---|
| All 36 double-quoted strings (in-text quotations plus reference titles) | No: the sorted list of quoted strings is identical to v6 | Earlier verification stands (`inbox/sources/goodman-salow-2023.txt`, `state/sources_cache/salow_value_text.txt`, DDB text) |

## Step 4 — Attributions (altered only)

| Claim | Source | Verdict |
|---|---|---|
| Salow (2025) offers a dissolution (D1) | Salow 2025 | accurate (weaker than v6) |
| KDT is "one proposal of that kind" (D2) | Salow 2025, 34 ("Any solution to that problem…") | accurate |
| Normality framework is Goodman and Salow's (2023, 2025) (D3) | both papers | accurate |
| Encroachment criterion stated as "rank the available options differently" (D12) | Salow 2025, 24 n. 3, reporting Hawthorne 2004 and Fantl–McGrath/Weatherson | accurate. The paraphrase follows the quoted words more closely than v6 did. |

## Step 5 — Page numbers and dates

No page, section, appendix or theorem locator was added or altered. (iii)'s "§4" and the A.5/A.6/A.7 cross-references are unchanged.

## Formal checks (`state/audit/A6/v8/ceu_check.py`, exact Fractions)

| # | Claim | Recomputed | Verdict |
|---|---|---|---|
| F1 | Three-state example: ken at a is {a,b}; post-answer kens {a}, {b,c}; both rules choose β₁=(0.9,1.5,−10.1) now with expectation 1.2; looking policy (β at a, decline at b,c) has current expectation 0.5; CEU prefers acting now by 0.7 | ken {a,b}; β₁ = 6/5; policy 1/2; β₁−look: KDT 7/10, CEU 7/10 (D=E, K^D={a,b}) | Confirmed |
| F2 | FINAL-REVIEW.md: original bet's advantage over looking is 1/2 under KDT and −9/2 under CEU | β−look: KDT 1/2; CEU −9/2 (D={b,c}, K^D={b,c}) | Confirmed. This is the counterexample to v6's "every comparison CEU makes … uses ordinary knowledge". |
| F3 | New sentence: CEU = KDT on present-best-vs-look and among primitive acts | Primitive pairs differ everywhere, so D=E and CEU = KDT (β₁−β 1/5, β₁−decl 6/5, β−decl 1). Generally: A.6 already shows "the difference event is E, and likewise for every pair of primitive acts". | Confirmed. CEU strict-preference graph in the example has no 3-cycle. In general β₁ is a Condorcet winner, so dropping "no cycle can arise" leaves no gap in Theorem 3. |
| F4 | Five-state VER example (text unchanged): conditional ken {s₁,s₂,v₂}, E[β₁]=0.028 there, VER prefers acting now by 0.008 | K^D={s1,s2,v2}; E[β₁|K^D]=0.0281; VER sum = −0.00819 | Confirmed |
| F5 | Four-state no-defeat example (text unchanged): KDT value 0.05; conditional ken {x,b}; VER and CEU prefer acting now | KDT 1/20; K^D={x,b}; CEU −49/20; VER −49/40 | Confirmed |
| F6 | No theorem, lemma, proposition, equation or proof changed | Word diff: no edits inside any `$…$`, theorem or lemma statement, or appendix paragraph (A.1, A.5 and A.7 are only split into paragraphs) | Confirmed |
| F7 | D11: the 0.95 win probability under evidence-conditioned evaluation | P(\|e₁\|≤1.96) for e₁~N(0,1) = 0.950 | Confirmed (unchanged figure) |

## Compliance

- `python3 tools/wordcount.py`: v8 strict=5,948, wordlike=5,922; limit 6,000, so OK. (Above the 5,600 target, as the baseline was at 5,853.)
- `python3 tools/check_injection.py … --judges-file state/panel/judges.txt`: no hard flags. Soft flags are panel surnames in genuine citations only (Salow 46, Hawthorne 7, Goldstein 3, Fitelson 1), all in references or in-text citations already audited.
- Anonymity grep (AI, competition, pipeline, entrant, model names, panel/judge/reviewer, account email): no hits.
- `A6-Free-Evidence-v8.pdf`: 12 pages. Metadata: Title only, no Author, Creator or Producer. Extracted text contains all v8 edits and no v6-only strings ("most economical", "every comparison CEU makes").

## Patch list

No patch is required for adoption. Optional, +9 words (5,957 ≤ 6,000):

1. **P1 (optional precision, §4 opening).**
   - Old: `The first lemma handles the danger; the next two provide the sufficient conditions.`
   - New: `The first lemma handles the danger; the next two give a sufficient condition and show that K-normality kens satisfy its structural part.`

Not patched (outside the delta, audited in v6): (iii) names only "Theorem 2 and its corollary". Theorem 1(b) also uses the $p_v$ questions, but all of Theorem 1 is finite, and A.5 treats Bjorn directly, so the statement is not false.

## Grok Review 3: requested revisions mapped against v8

| # | Request | Addressed in v8? | Where / gap |
|---|---|---|---|
| 1 | Clarify the dependence on finiteness, statism, comparability and K-normality; status under I-/KM-normality and non-statism | **Largely, already in v6** (v8 adds nothing) | Abstract, thesis (l.15) and conclusion state "finite statist, comparable … K-normality". §2 flags I-/KM-normality with a pointer to §6.1. §6.1 concedes the Margins views. §6.3 covers statism. The conclusion says non-statist models are not covered. Gap: no single intro sentence saying the negative verdicts are not claimed for "normality models" simpliciter (the title subtitle is unqualified). |
| 2 | Sharpen the positive upshot (gapped knowledge necessary? condition only on evidence? knowledge not the right object?) and use Dorst et al. to explain why the boundary is natural | **Partly** | Corollary (ii) and its gloss: conditioning on evidence is the only safe belief-containing state in graded models. The conclusion lists four options left open. §1 maps safety onto Total Trust. Gap: no recommendation among the options, and DDB is not used to motivate the boundary. |
| 3 | Viability of ANS / restricted ANS; can any EU conditional rule secure both? | **Partly** | §5.3 final paragraphs: restricted ANS is all-or-nothing on price, and "Thus ANS … keeps free-inquiry safety at the cost of conflicting with CKD on costly inquiry". The conclusion disclaims the general impossibility claim. Gap: no explicit verdict on whether the cost is decisive. |
| 4a | Roadmap after thesis | **Yes (v6)** | l.17 roadmap separates Theorems 1–2, Bjorn and §5. It does not mention §6. |
| 4b | Intuitive gloss of Lemma 1 | **Partly (v8 adds)** | The new §4 opening (D6) and the gloss on relative defeat ("For all one knows, answering would leave open something one now rules out"). There is no gloss of the bet mechanism beyond the four-sentence proof. |
| 4c | Flag that the second weighing is not a $p_v$ question | **Yes** | (iii) is now its own paragraph (v8 layout); §4 Corollary gloss: "It does not establish the same necessity result for the second weighing alone." |
| 4d | Confirm Bjorn numbers come from numerical integration | **Yes (v6)** | A.5 last sentence; Computations ¶. |
| 5a | Reminder that collapse + comparability make every ken gapped | **Yes (v6)** | Corollary (i) states it; conclusion: "collapse is one sufficient restriction". |
| 5b | Main-text note that the open-neighborhood claim follows from continuity | **Appendix only** | Theorem 3 statement plus A.6: "Finitely many strict inequalities and nonzero differences persist under small perturbations." |

None of the unaddressed items is an accuracy defect. Each would need new prose, and only 52 words of headroom remain. Whether to make any of these changes is for the orchestrator to decide; they do not affect adoption.
