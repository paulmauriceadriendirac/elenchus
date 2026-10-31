DO NOT ADOPT (as delivered). ADOPT once Patch 1 is applied: the only defect is a false page range in one bibliography entry. Every other new or altered claim was checked and holds.

# A5 v9 delta audit

- Baseline: `final/A5/essay.md`, which passed the citation, formal and compliance audits.
- Candidate: `state/external/submission-ready-20261030/A5-Holistic-Accuracy-v9.md`. This file is byte-identical to `state/external/submission-final-20261030/A5-Holistic-Accuracy-v9.md`.
- Method: `git diff --no-index --word-diff=plain` between the two files, followed by the checks below.
- Scripts and outputs are in `state/audit/A5/v9/`: `delta_check.py`, `delta_check.out`, `refs_delta.json`, `refs_delta_verification.{json,md}`.

## Summary counts

| Item | Count | Result |
|---|---|---|
| Changed or added prose passages | 14 (10 new paragraphs or sentences, 3 paragraph moves or splits, 1 reworded sentence) | all checked |
| New references | 1 (Skipper 2023) | VERIFIED. Metadata correct; the issue number is omitted (style fix, Patch 2) |
| Altered references | 1 (Holguín 2022: "(1)." became "(6): 1–34.") | issue (6) correct; **pages 1–34 false** (25 pp.) → Patch 1 |
| New quotations | 0 | none |
| New attributions | 3 (all to Skipper 2023) | 3 accurate (one optional wording tweak, Patch 3) |
| New page or section locators | 2 (Skipper §3.2, §4) | both correct |
| New numbers or formal claims | 0 new numbers. 2 new qualitative formal glosses | correct |
| Theorems, equations, proofs | 414 math segments, all theorem/corollary statements, 4 definitions (ME, BI, RI, CI), appendix | identical to the baseline apart from whitespace and paragraph breaks |
| Word count | strict 5,536 (baseline 5,039); limit 6,000; target 5,600 | OK |
| check_injection | no hard flags; soft flags only for genuine citations of Mandelkern and Easwaran | OK |
| Anonymity | no mention of the competition, panel, AI, pipeline or entrant | OK |

## Step 1: Coverage

| Item | In-text | References | Match |
|---|---|---|---|
| Skipper 2023 | "Skipper (2023, §3.2) … (§4)" in §6 | Skipper, Mattias. 2023 … | yes |
| Holguín 2022 | unchanged citations (§5, §7.2, §§7.2, 8.1) | entry altered | yes (year and spelling consistent) |
| All other entries | unchanged from the audited baseline | unchanged | yes |

## Step 2: Existence and metadata

I ran `tools/verify_refs.py` on `state/audit/A5/v9/refs_delta.json`. Both entries came back VERIFIED.

| Ref | v9 metadata | Evidence | Verdict |
|---|---|---|---|
| Skipper 2023 | *Phil. Studies* 180: 2025–2050, doi 10.1007/s11098-022-01915-1 | Crossref: vol. 180, issue 7, pp. 2025–2050. OpenAlex agrees. I read the full text of the CC-BY publisher PDF (`link.springer.com/content/pdf/10.1007/s11098-022-01915-1.pdf`, 26 pp., printed pages 2025–2050). | correct. The issue "(7)" is missing, while the other journal entries give issues → Patch 2 |
| Holguín 2022 | *Phil. Imprint* 22 (6): 1–34 | The publisher PDF from journals.publishing.umich.edu/phimp/article/id/2123/download/pdf/ has the cover "volume 22, no. 6, february 2022". The last page footer reads "philosophers' imprint - 25 - vol. 22, no. 6 (february 2022)", and the PDF has 25 pages. Crossref and OpenAlex give issue "1" and no pages; the publisher HTML metadata gives issue "0". | **Issue (6) is supported by the article itself. Pages "1–34" are false; the article runs 1–25.** → Patch 1 |

## Step 3: Quotations

v9 adds or alters no quotations. Every quotation in v9 also appears in the baseline, with identical wording and locators.

## Step 4: Attributions (new or altered)

| # | Claim in v9 | Source check | Class |
|---|---|---|---|
| A1 | "Skipper (2023, §3.2) already raises a related objection to Dorst and Mandelkern: dividing alternatives outside two candidate guesses can reverse their ranking." | §3.2 (pp. 2036–2040). Skipper splits 'Other' into n players and shows that on Dorst and Mandelkern's account "'Woods or Mickelson' eventually overtakes 'Woods'" (p. 2036; also fn. 12, p. 2037). He calls this a failure of "Independence of irrelevant alternatives (for guessing)". | accurate |
| A2 | "His alternative specificity measure preserves that ranking when the answers compatible with each guess stay fixed (§4)." | §4, "An alternative proposal" (p. 2040ff.), uses the log-ratio specificity S(p)=log(\|Q\|/c_p). P. 2042: "whether one guess has a higher expected answer-value than another depends only on the probabilities of the guesses and the number of complete answers with which they are compatible, as required by IIA for Guessing" (proof in his Appendix B). IIA's conditions (i)–(ii) are exactly "same compatible complete answers" (pp. 2037–38). | accurate. "alternative specificity measure" is descriptive, not Skipper's name for it; optional Patch 3 |
| A3 | "The invariance condition below has a different scope … every coarsening, including changes within a candidate proposition. The general concern about irrelevant refinements is therefore not new." | Matches RI as stated in v9 §6 ("For every coarsening π …"). Skipper's IIA holds fixed the compatible answers of both guesses, so it does not cover refinement inside a guess. | accurate |
| Panel | Mandelkern is a panel member. v9 represents his and Dorst's view only through Skipper's critique, and does so faithfully. Easwaran (panel) appears only in unchanged sentences. | none |

### New expository or formal glosses (no attribution, checked for truth)

| Passage | Check | Verdict |
|---|---|---|
| §1 new opening: under a fixed threshold, "once belief is required, a further increase in credence cannot reverse that verdict" | C(p)>τ is preserved when C(p) rises | true |
| §2 new: under Separability "its expected contribution alone determines whether it belongs in an optimum" | This is the e_p sign rule stated just above | true |
| §3 new: the two credence functions share worlds and order; the score, premium and proposition are held fixed | matches the case | true |
| §3 new: the "reversal becomes intelligible" paragraph | C'(13)=0.99 (recomputed) | true |
| §3 reworded: "This reversal does not depend on the particular numbers just chosen. Every positive premium permits a range of cases with the same structure:" replaces "The case is not a knife-edge." | Theorem 1 holds for every β>0 given 0<T<−F. I checked max(c0,τ)<c1<1 for four parameter sets in `delta_check.py`. The conservative-values condition sits in the theorem statement directly below. | true |
| §4 new: ME vs truth-directedness, sign vs size | follows from the definitions | true |
| §5 new: the holistic score "still requir[es] each accepted belief to make a non-negative expected contribution" | Theorem 3: no optimum contains a p with e_p<0 | true |
| §5 new: Φ's two terms; "comparing these core values suffices" | this is Theorem 3 | true |
| §6 new framing paragraph; "There are thus two distinct tasks …" | consistent with Theorem 4 and the n/(n+1) example | true |

## Step 5: Page numbers, dates, numbers and formal content

- **New locators.** Skipper §3.2 is on pp. 2036–2040 and §4 begins on p. 2040; both correct. No other new page numbers. The Holguín page range is wrong (Patch 1).
- **Math invariance** (`delta_check.py`):
  - All 414 inline and display math segments are identical, in the same order.
  - The five theorem and corollary statements and the four definitions (ME, BI, RI, CI) are identical.
  - The appendix is identical apart from whitespace. The Theorem 2 proof was only split into paragraphs (i), (ii), (iii) and (b), with no change in meaning.
- **Numbers recomputed** for the moved and re-paragraphed passages, by exact enumeration of all 2^8 states:
  - At C, the unique optimum is {1,12,13,W} at 4.30 and the runner-up is {12,13,W} at 4.20.
  - At C', the unique optimum is {13,W} at 4.94 and the runner-up is {1,12,13,W} at 4.75.
  - In the refined space, Φ(1)=7.25 and Φ({w1,w3})=6.91. Core {w1} is chosen at both the refined C' and the refined C.
  - The 2^{k−1} multiplier holds for k=1–4.
  - Under the mean repair with b=3/8, splitting w2 into 2, 4 or 8 worlds preserves both verdicts.
  - The two-world threshold is 5/6.
- No new dates.

## Patch list (apply to `A5-Holistic-Accuracy-v9.md`)

1. **Required.** In References:
   - old: `*Philosophers' Imprint* 22 (6): 1–34. https://doi.org/10.3998/phimp.2123`
   - new: `*Philosophers' Imprint* 22 (6): 1–25. https://doi.org/10.3998/phimp.2123`
2. **Recommended (style consistency).** In References:
   - old: `*Philosophical Studies* 180: 2025–2050.`
   - new: `*Philosophical Studies* 180 (7): 2025–2050.`
3. **Optional (precision).** In §6:
   - old: `His alternative specificity measure preserves that ranking`
   - new: `His log-ratio specificity measure preserves that ranking`

After Patch 1 the word count is unchanged, since the bibliography is excluded. v9 then contains no false, misattributed or unverifiable new claim, and can be adopted.

## Grok Review 2: does v9 address each requested revision?

| # | Request | Status in v9 | Where |
|---|---|---|---|
| 1 | Sharpen the increment over Dorst and Mandelkern, early and in §5; contrast with scoring a state by its conjunction's Jamesian value | **Addressed** (already in the baseline; v9 unchanged here) | §1 "The closest prior work … The claimed increment is consequently narrower …"; §5 "Scoring a state simply by its conjunction's Jamesian value would fail that requirement: adding an entailed proposition leaves the score unchanged." |
| 2a | Motivate why a holist values the truth of the core rather than some other interaction term | **Partially.** §3 baseline gives the multi-premise-deduction and perfect-paper motivation; v9 adds an intuitive explanation of the reversal (§3) and the Φ gloss (§5). There is no explicit comparison with other interaction terms. | §3, §5 |
| 2b | Say whether other holistic terms (e.g. a closure bonus) also give non-monotonicity | **Addressed** (baseline) | §4 dilemma and fn. 4 (closure bonus is non-monotone) |
| 3 | Acknowledge dominance or permissibility frameworks that do not guarantee a rational state at every credence | **Partially.** §7 is unchanged. It notes the objection "survives only by rejecting this existence requirement" but does not name such frameworks. | §7 |
| 4a | One-sentence roadmap after the thesis | **Addressed** (baseline) | §1 "The argument has three parts. …" |
| 4b | Intuition for the interval length βT/(D(2D+β)) | **Partially.** v9 adds intuition for the reversal and for robustness across premiums, but not for the length formula itself. | §3 |
| 4c | Make clear that repair 1 keeps non-monotonicity under question-preserving refinement while unrestricted RI rules it out | **Largely addressed.** The baseline already said so ("leaves both verdicts in place"; "Neither repair yields invariance under every refinement … excludes the present non-Lockean behavior"). v9 adds a framing paragraph, the Skipper positioning, paragraph splits and the "two distinct tasks" sentence. | §6 |
| 4d | Put the four-world non-closure example earlier, where core-relative Lockeanism is introduced | **Addressed** (baseline). It already comes immediately after "Call this core-relative Lockeanism". | §5 |
| 5a | Main-text reminder that complementary-pair states are suboptimal (Theorem 2 proviso) | **Addressed, in a footnote.** Fn. 3 is anchored in the Theorem 2 statement and says exactly this. There is no main-text parenthetical. | §4, fn. 3 |
| 5b | Theorem 4 proof: say explicitly that states missing the tautology are excluded | **Addressed** (baseline) | Appendix: "every state lacking $\{u,v\}$ (adding it raises the score at both)" |

None of the Grok requests calls for a change that v9 makes incorrectly. Items 2a, 3 and 4b remain partial. They are presentational, and closing them is not needed for correctness.
