# A6 final: citation delta audit

**Audited text:** `final/A6/essay.md` (state of 2026-10-29, after commit f69bb59, "A6 compliance fix 1 (Hong)"; strict word count 5,819).
**Baseline:** `state/drafts/A6/v4.md`, fully audited in `state/audit/A6/citations.md`. This audit covers only what `diff v4 final` shows to be new or changed. Unchanged material keeps its earlier verdicts.
**Date:** 2026-10-29

## Sources used

- **Dorst, Levinstein, Salow, Husic and Fitelson 2021, "Deference Done Better".** I downloaded https://fitelson.org/ddb.pdf myself. The coordinator's copy, `state/ambitious/sources/dorst-etal-2021-deference-done-better.{pdf,txt}`, has the same byte size (909,859) and the same text. **Version:** this is the published Wiley typeset article, not a preprint. Page 1 carries the DOI 10.1111/phpe.12156 and the footer "Philosophical Perspectives 2021;35:99–150. ©2021 Wiley Periodicals LLC 99", and the running heads carry journal pagination. The page numbers below are the published pages (PDF page + 98).
- **Goodman and Salow 2023:** `inbox/sources/goodman-salow-2023.txt` (published version, Phil Review 132(1)).
- **Crossref** records for 10.1111/phpe.12156, 10.1515/bejte-2019-0010 and 10.1111/phpe.70003 (Hong 2026 abstract). **OpenAlex** record for the Geanakoplos 2021 article.
- **Not retrieved:** the full text of Geanakoplos 2021 (BEJTE). The De Gruyter PDF returned an empty bot-check response and I did not try to get around it. The Cowles CFDP 914 PDF also returned HTML this time. The earlier audit read Theorem 1 in CFDP 914 (A36).

## Summary counts

| Step | Items | Result |
|---|---|---|
| 1 Coverage | 17 references; all in-text author–year pairs | Complete in both directions. The one new citation, Dorst et al. 2021, has its entry, and no entry is left uncited. |
| 2 Existence/metadata | 2 new or changed entries (Dorst et al. 2021; Geanakoplos revised-version note) | `verify_refs.py`: 2 VERIFIED. All fields match Crossref. |
| 3 Quotations | 0 new quotations | No new or altered quoted strings. Every changed passage either paraphrases or keeps a quotation verified in v4. |
| 4 Attributions | 14 new or altered attributions | 9 accurate, 4 oversimplified (3 of them in the DDB paragraph), 0 inaccurate. One item is unverifiable but harmless: the numbering of the 2021 BEJTE version, which the essay does not cite. |
| 5 Page/section/theorem numbers | 11 new or altered locators | All 11 verified. |
| Patches | 6 | P1–P6 below. Net change about +75 words (5,819 → about 5,895; the limit is 6,000). |

## Step 1. Coverage

| In-text | Reference entry | Status |
|---|---|---|
| Dorst et al.'s (2021) *Deference Done Better* (l.21) | Dorst, Kevin, Benjamin A. Levinstein, Bernhard Salow, Brooke E. Husic, and Branden Fitelson. 2021 … | OK. Author spellings, year and title match. |
| Geanakoplos (1989), (1989, Theorem 1) (l.19, l.65) | Geanakoplos 1989 … Revised version in *B.E. Journal of Theoretical Economics* 21 (2021) | OK. The text cites only 1989, and the 2021 version is a note inside the 1989 entry. |
| Hong (2026) (l.19), now without §§1–3 | Hong 2026 "Normality in Action?" | OK |
| All other pairs (Ahmed & Salow 2019, Das 2023, Dorst 2020, Fantl & McGrath 2002, Goldschmidt 2024, Goldstein & Hawthorne 2022, Good 1967, G&S 2023, BRN 2025, Hawthorne 2004, Hawthorne & Stanley 2008, Hong 2024, Salow 2025, Weatherson 2005) | present | Script check: each entry's surname and year occur in the body, and every body citation has an entry. |

## Step 2. Existence and metadata

| Entry | Tool | Evidence |
|---|---|---|
| Dorst et al. 2021, *Phil. Perspectives* 35: 99–150, doi 10.1111/phpe.12156 | VERIFIED | Crossref lists the authors as Kevin Dorst, Benjamin A. Levinstein, Bernhard Salow, Brooke E. Husic and Branden Fitelson, in that order, with vol. 35, issue 1, pp. 99–150, published online 2021-10-23 and in print 2021-12. The PDF title page agrees. |
| Geanakoplos, revised version, *BEJTE* 21 (2021): 361–394 | VERIFIED | Crossref: "Game Theory Without Partitions, and Applications to Speculation and Consensus", John Geanakoplos, vol. 21, issue 2, pp. 361–394, issued 2021 (online 2021-06-28). The essay's lower-case "without" is a style difference only. |
| Hong 2026 (re-check, since l.19 changed) | n/a (verified in v4) | Crossref: "Normality in Action?", *Philosophical Perspectives*. There is still no volume or pages (issued 2026-09-11), so "early view" is correct. |

The verification outputs are in the scratchpad (`refs_final_new.verification.{json,md}`), not in `state/`.

## Step 3. Quotations

No quotation is new or altered. The changed passages keep only quotations verified in the v4 audit: "loses knowledge" (127), "together entail NO DEFEAT" (128), "these relatively rare counterexamples to Preservation" (Salow 36), and "the exception rather than the rule" (BRN §7). I re-read the first two in `inbox/sources/goodman-salow-2023.txt`. The DDB paragraph has no quotation marks; 'modestly informed' in P6 is checked word for word (p. 118). No fetch request is needed.

## Step 4. Attributions

### 4a. The Deference Done Better paragraph (l.21). Two authors, Salow and Fitelson, are on the panel, so every clause was checked against the full text.

| # | Claim in essay | Source text (published pages) | Verdict | Fix |
|---|---|---|---|---|
| D1 | DDB "supplies an even closer general comparison" than Geanakoplos and others | n. 15 (p. 124): "Value is related to a substantial literature arising out of Good (1967) … Geanakoplos (1989) was effectively the first to investigate the possibility of satisfying Value when probabilities are modest … our characterization (Theorem 4.1) will generalize his Theorem 1." | accurate. DDB present their result as a generalization of the very theorem the essay uses for Lemma 2. | – |
| D2 | "Total Trust is equivalent to Value … (Theorem 2.2)" | p. 107: "Most importantly, Total Trust is equivalent to Value: Theorem 2.2. π totally trusts ⟨W,P⟩ iff π values ⟨W,P⟩." | accurate (numbering and content) | – |
| D3 | Value = "the requirement that every recommended expert-dependent strategy perform at least as well as acting on one's own probabilities" | p. 105: "Value: If S is recommended for 𝒪, then for all O ∈ 𝒪: 𝔼π(S) ≥ 𝔼π(O)", glossed as "no matter what decision you face, the expected utility of adopting a strategy recommended by the expert is always at least as high as bypassing the expert and picking an option using your own probabilities." A strategy maps worlds to options with S_w = S_v whenever P_w = P_v, and it is *recommended* iff each S_w maximizes 𝔼_{P_w} (p. 104). | oversimplified (minor). The gloss drops the quantifier over decision problems and the fact that "perform" means expected utility *by π*. As written it can be read as outcome dominance. | P3 |
| D4 | Mapping: π = Pr(·∣K_E(x)); P_s = Pr(·∣K_{E∩Π(s)}(s)) | DDB frames: W finite, P maps worlds to probability functions on W, π a probability on W (pp. 100–102, n. 6). | accurate, with one condition left implicit: the frame's worlds must be the states of E, not K_E(x). Under relative defeat, P_s gives weight to states outside K_E(x). π may be non-regular (DDB define W_π, p. 132). | P4 (precision) |
| D5 | "The fixed tie order generates a recommended strategy" | Recommended = picks a P_w-maximizer at each w, and a strategy must be a function of P_w (p. 104). The essay's prior has full support (§2), so P_s determines its support, the post-answer ken. KDT's choice with a fixed tie order is therefore a function of P_s and maximizes 𝔼_{P_s}. | accurate. The essay leaves the full-support step unstated, and an expert reader will look for it. | P5 |
| D6 | "Universal safety for that strategy implies their Weak Value condition" | p. 133: "Weak Value: Given any 𝒪, there exists some recommended strategy S such that for all O ∈ 𝒪: 𝔼π(S) ≥ 𝔼π(O)." With V_x = 𝔼π(α_Π) − max_a 𝔼π(a), safety in every A gives exactly such an S. | accurate | – |
| D7 | "their Appendix B establishes its equivalence to Value and Total Trust" | p. 133: "§B.1 Weak Value ⇔ Total Trust ⇔ Modestly Informed"; Lemma B.1 (p. 133), Weak Value ⇒ Total Trust; §B.2 "Weak Value ⇔ Value" (p. 137), "thus establishing Theorems 2.2 and 4.1". | accurate | – (P5 adds the section locators) |
| D8 | "Theorem 1 thus characterizes, within these normality models, when the post-answer rule merits Total Trust." | Total Trust is a relation between π and a frame ("π totally trusts ⟨W,P⟩", p. 106). It is not a property of a rule, and DDB's term is not "merits". The biconditional also needs the converse, Value ⇒ safety, which holds because Value quantifies over *every* recommended strategy, including KDT's tie-order strategy. The essay states only the forward direction. | oversimplified: the relata are misdescribed, "merits" is evaluative wording, and half of the "characterizes" step is unstated | P5 |
| D9 | "Its increment is the structural boundary in terms of relative defeat and gappedness …" | p. 118: "Theorem 4.1. π totally trusts ⟨W,P⟩ iff each P_i ∈ C_π is modestly informed and π is in their convex hull." DDB already give a general characterization of Total Trust for any finite frame. | oversimplified by omission. The increment claim is defensible, but a DDB author will expect Theorem 4.1 to be acknowledged. Otherwise the paragraph reads as though DDB supply only the equivalence and the essay supplies the characterization. | P6 |

**Overall verdict on the DDB paragraph:** nothing in it is false. Theorem 2.2, Weak Value, Appendix B's equivalences and the mapping all check out. Three phrasings fall short of the exactness the paper's authors will expect: the Value gloss, "merits Total Trust" with its unstated converse, and the silence on Theorem 4.1. P3–P6 give the corrected wording. With them, the paragraph states only what DDB prove and what follows by the essay's own definitions.

### 4b. Other new or altered attributions

| # | Location | Claim | Check | Verdict | Fix |
|---|---|---|---|---|---|
| O1 | l.19 | Salow (2025, 33) notes that a 'for all you know' dominance principle can support dogmatism even with Preservation | v4 audit A4 (p. 33). The new text paraphrases without quotation marks and keeps the sense. | accurate | – |
| O2 | l.19 | BRN "establish the normality conditions for Preservation and its failure in Bjorn" | v4 audit A6: BRN Prop. 1 shows that statism, collapse and comparability *validate* Preservation, which is a sufficient condition. Nothing shows these are *the* (necessary and sufficient) conditions. BRN's §5 Bjorn case is a failure. Salow is on the panel. | oversimplified (the definite article overstates) | P1 |
| O3 | l.19 | Geanakoplos (1989) "gives sufficient conditions for valuable information beyond partitional learning" | v4 A36: CFDP 914, Theorem 1 (nondeluded, nested, KTYK ⇒ more information weakly better). The 2021 abstract: the conditions are "strictly weaker than partition information". DDB n. 15 independently describes his Theorem 1 as a Value result. | accurate | – |
| O4 | l.19 | Dorst (2020) and Das (2023) "develop related epistemological questions" | The new wording is vague enough to be safe (v4 A5). | accurate | – |
| O5 | l.19 | Hong (2026) "argues that whatever the normality framework captures is not action-guiding" | Crossref abstract: "we give two arguments that suggest that whatever concept the normality framework is capturing (whether it really be knowledge or something else), it is not action-guiding." The orchestrator's change makes l.19 consistent with the essay's other Hong mentions: l.13 cites only Hong 2024, and no other passage now attributes §§1–3 detail to Hong 2026. | accurate in substance, slightly stronger than "arguments that suggest" | P2 (calibration, word-neutral +1) |
| O6 | l.43 | Bjorn's knowledge after one weighing depends on the second reading (2023, 128) | G&S p. 128: "what Bjorn knows after weighing himself once depends on what the second scale will read" | accurate | – |
| O7 | l.49 | G&S's result holds "for the case where the first reading is accurate and the second within c of it" (2023, 127) | p. 127: "Consider any state ⟨x, x, y⟩, where \|x−y\| ≤ c … Bjorn therefore loses knowledge whenever …" | accurate | – |
| O8 | l.49 | BRN's ≈0.37 concerns the event (2−√2)c < \|r−r′\| ≤ √2c (§5, n. 18) | v4 A14 and changelog P10 (n. 18 "∼.37", the ♦− failure event). I checked the arithmetic myself: erfc((2−√2)c/2) ≈ 0.417 and erfc(c/√2) ≈ 0.050 at c = 1.96, giving a difference of ≈ 0.367. | accurate | – |
| O9 | l.79 | G&S's example of such a discovery, that an experiment did not end on its first trial, "defeats knowledge only in a model without statism (2023, 136)" | p. 136: "discover that the experiment doesn't end on the first trial … So we have a counterexample to … NO DEFEAT FROM WHAT YOU ALREADY KNOW"; the dynamics "cannot arise in models satisfying STATISM". Ending on the first trial is the modal (most probable) outcome under the geometric chances, so learning that it did not happen is learning that things are not maximally normal, as the essay says of p_v. | accurate | – |
| O10 | l.121 | VER conditions on "a hypothesis in the spirit of Salow's moral" | v4 A25; the hedge makes it safe | accurate | – |
| O11 | l.137 | "conditional belief and belief after discovery can diverge (BRN App. D.3)" | v4 A26 (D.3 concerns belief; the equivalence "depends on statism") | accurate | – |
| O12 | l.143, l.151, l.155, l.159 | "discussed by Ahmed and Salow"; Salow: "it is unclear what would confine"; "BRN suggest"; "among other cases" | v4 A28, A32, A33, A35; each now matches the source's strength | accurate | – |
| O13 | References | Geanakoplos 2021 is the revised version, and "Theorem 1" is the value-of-information result | The essay cites Theorem 1 of the 1989 CFDP, which v4 A36 read directly. I could not open the 2021 full text, so I cannot confirm that it keeps the numbering. Nothing in the essay relies on the 2021 numbering. | unverifiable for 2021, harmless | none needed. If the numbering is ever cited from 2021, it must first be checked against the BEJTE text. |

## Step 5. Page, section, theorem numbers and dates

| Locator | Verified against | Status |
|---|---|---|
| DDB Theorem 2.2 | p. 107 | verified |
| DDB "Weak Value" | Appendix B, p. 133 | verified |
| DDB Appendix B equivalences | §B.1 (p. 133), §B.2 "Weak Value ⇔ Value" (p. 137) | verified |
| DDB Theorem 4.1 (P6) | p. 118 | verified |
| DDB 2021, 35: 99–150 | Crossref and the PDF | verified |
| Geanakoplos 2021, 21: 361–394 | Crossref | verified |
| Geanakoplos 1989, Theorem 1 | CFDP 914 (v4 A36). DDB n. 15 corroborates "his Theorem 1". | verified |
| G&S 2023, 127 | PDF text | verified |
| G&S 2023, 128 | PDF text | verified |
| G&S 2023, 136 | PDF text | verified |
| BRN §5 n. 18; App. D.3 | v4 audit (A14, A26) | verified (unchanged locators) |

## Patch list for `final/A6/essay.md`

Apply in any order. Each OLD string occurs exactly once in the current file; I checked this with `str.count`.

**P1** (l.19, BRN; Salow is on the panel)
OLD: `Goodman and Salow (2025, henceforth BRN) establish the normality conditions for Preservation and its failure in Bjorn.`
NEW: `Goodman and Salow (2025, henceforth BRN) show that statism, collapse and comparability validate Preservation, and that Preservation fails in Bjorn.`

**P2** (l.19, Hong; calibration to the abstract)
OLD: `Hong (2026) argues that whatever the normality framework captures is not action-guiding.`
NEW: `Hong (2026) gives two arguments suggesting that whatever the normality framework captures is not action-guiding.`

**P3** (l.21, the Value gloss)
OLD: `Total Trust is equivalent to Value, the requirement that every recommended expert-dependent strategy perform at least as well as acting on one's own probabilities (Theorem 2.2).`
NEW: `Total Trust is equivalent to Value, the requirement that in every decision problem each strategy recommended by the expert's probabilities have expected utility, by one's own probabilities, at least as high as any option (Theorem 2.2).`

**P4** (l.21, the frame's worlds)
OLD: `Here the current probabilities are $\pi=\Pr(\cdot\mid K_E(x))$`
NEW: `Here the frame's worlds are the states in $E$, the current probabilities are $\pi=\Pr(\cdot\mid K_E(x))$`

**P5** (l.21, recommended strategy, both directions, relata of Total Trust)
OLD: `The fixed tie order generates a recommended strategy. Universal safety for that strategy implies their Weak Value condition; their Appendix B establishes its equivalence to Value and Total Trust. Theorem 1 thus characterizes, within these normality models, when the post-answer rule merits Total Trust.`
NEW: `Since the prior has full support, $P_s$ fixes the post-answer ken, so KDT with the fixed tie order is a recommended strategy. Universal safety therefore implies their Weak Value condition, and Value implies universal safety; their Appendix B (§§B.1–B.2) proves Weak Value equivalent to Total Trust and to Value. So a question is safe at $x$ exactly when $\pi$ totally trusts this frame, and Theorem 1 characterizes, within these normality models, when it does.`

**P6** (l.21, acknowledging DDB's own characterization)
OLD: `Its increment is the structural boundary in terms of relative defeat and gappedness, together with the graded-model consequence and the tests of three conditional inquiry rules.`
NEW: `Their Theorem 4.1 already characterizes Total Trust for any finite frame, by requiring the relevant candidate expert functions to be 'modestly informed' and $\pi$ to lie in their convex hull. The increment here is to state that boundary in normality-theoretic terms, as relative defeat and gappedness, together with the graded-model consequence and the tests of three conditional inquiry rules.`

After applying them, run `tools/wordcount.py` (expected strict count about 5,895, under 6,000) and `tools/check_injection.py`. The DDB paragraph now names "Salow" and "Fitelson" only in the reference entry, so the injection soft-flag counts are unchanged.

## Residual

- The 2021 BEJTE full text was not retrieved, because the publisher's bot check returned an empty response. The essay does not depend on it. A fetch is needed only if the 2021 theorem numbering is ever cited.
- I made no checks beyond the delta. Earlier verdicts on unchanged text stand as recorded in `state/audit/A6/citations.md`.
