# A6 v4 citation audit

Essay audited: `state/drafts/A6/v4.md` (wordcount.py: strict 5,883, target 5,600, limit 6,000). References: `state/drafts/A6/refs_v4.json`. Tool output for this audit: `state/audit/A6/refs_v4.verification.{md,json}`.

Sources read in full or at the cited passages:
- Goodman & Salow 2023, published PDF (`inbox/sources/goodman-salow-2023.txt`; journal page numbers printed in the text).
- Salow 2025, published version of record. Open-access PDF from ORA (https://ora.ox.ac.uk/objects/uuid:5a0dd404-6e48-40ca-a1f4-141aaab57c3e/files/rtt44pp612), with journal pagination 23–38.
- Goodman & Salow, "Belief Revision Normalized" (BRN): the author's accepted manuscript (https://users.ox.ac.uk/~shug2406/BeliefRevisionNormalized.pdf, labelled "forthcoming in JPL"). The Springer PDF is behind a bot check, so I could not compare it with the published version. The essay cites BRN only by section, note and appendix number, and I checked those against the manuscript.
- Ahmed & Salow 2019: the author's draft (`state/sources_cache/ahmed_salow_text.txt`), plus the published abstract from OpenAlex.
- Geanakoplos, CFDP 914 (May 1989), Cowles PDF (https://cowles.yale.edu/sites/default/files/2022-08/d0914.pdf), with Theorem 1 read.
- Abstracts only (OpenAlex): Dorst 2020, Das 2023, Goldschmidt 2024, Hong 2026.
- Not retrievable:
  - Hong 2026 full text (Wiley returns 403). The high-priority fetch request `requests/fetch/amb-a6-hong-2025-2026.md` is still pending, so I filed no duplicate.
  - Das 2023 full text (PhilPapers returns 403).
- Not opened, because the essay attributes nothing to them except through Salow or through Goodman & Salow: Hawthorne 2004; Hawthorne & Stanley 2008; Goldstein & Hawthorne 2022; Fantl & McGrath 2002; Weatherson 2005; Good 1967.

## Summary counts

| Step | Checked | Problems |
|---|---|---|
| 1 Coverage | 16 reference entries; every in-text citation | 0 missing and 0 uncited. Years and spellings all match |
| 2 Metadata | 16 | tool: 14 VERIFIED, 1 MISMATCH (Hong 2024, resolved by hand), 1 PROBABLE (Geanakoplos: the 1989 paper is confirmed, but its "June 18, 2002 revision" cannot be verified, so remove it) |
| 3 Quotations | 20 | all 20 match word for word. One is quoted without its scope condition (Q9, fixed under attributions) |
| 4 Attributions | 38 | 26 accurate, 10 oversimplified, 1 inaccurate (A17), 1 unverifiable (A3, Hong 2026). Das 2023 is checked only against its abstract and is weakened under A5 |
| 5 Pages/dates | 27 page or section locators | 26 verified. One citation needs an added page (A10). One date claim (the Geanakoplos 2002 revision) cannot be verified and is removed |

Patches: 17 (P1–P14, P14b–P14d). All of them stay within the existing word count, give or take about 10 words.

## Step 1: Coverage

| In-text citation | Reference entry | Match |
|---|---|---|
| Salow 2025 (many) | Salow 2025, AJP 103: 23–38 | yes |
| Goldschmidt 2024 | yes | yes |
| Hawthorne and Stanley 2008 | yes | yes |
| Hong 2024 | yes | yes |
| Good 1967 | yes | yes |
| Goodman and Salow 2023 | yes | yes |
| Goodman and Salow 2025 / BRN | yes | yes |
| Geanakoplos 1989 | yes | yes (fix the "2002 revision" in the entry and in the text: P5, P6, P7) |
| Dorst 2020 | yes | yes |
| Das 2023 | yes | yes |
| Hong 2026 | yes | yes |
| Ahmed and Salow 2019 | yes | yes |
| Goldstein and Hawthorne 2022 | yes | yes |
| Hawthorne 2004 | yes | yes |
| Fantl and McGrath 2002 | yes | cited only inside the Salow quotation. That is acceptable |
| Weatherson 2005 | yes | the same, inside the Salow quotation |

All 16 reference entries are cited. Carter & Hawthorne 2024 is in the old `refs.json` but not in v4, and v4 does not cite it, so there is no coverage problem.

## Step 2: Existence and metadata (Crossref, checked by hand on each DOI)

| Key | Tool | Evidence | Verdict |
|---|---|---|---|
| AhmedSalow2019 | VERIFIED | BJPS 70(2): 327–350, June 2019 | ok |
| Das2023 | VERIFIED | BJPS 74(1): 25–55, 2023 | ok |
| Dorst2020 | VERIFIED | PPR 100(3): 586–632, print May 2020 (online 2019) | ok |
| FantlMcGrath2002 | VERIFIED | Phil Rev 111(1): 67–94 | ok |
| Geanakoplos1989 | PROBABLE | The Cowles PDF is CFDP 914, dated May 1989, 33 pp.; RePEc gives 1989-05. Theorem 1 (nondeluded, nested, KTYK ⇒ more information is weakly better, with a converse) is on PDF p. 7. I found no record of a "June 18, 2002" revision: not on RePEc, not on the Cowles PDF (its modification date is 2001), and not in a web search. The revised version was published as BEJTE 21(2): 361–394 (2021), doi 10.1515/bejte-2019-0010 | Keep the 1989 paper. Remove the 2002 revision (P5–P7) |
| Goldschmidt2024 | VERIFIED | AJP 102(4): 939–958 | ok |
| GoldsteinHawthorne2022 | VERIFIED | Phil Stud 179(4): 1341–1372, print April 2022 (online 2021) | ok |
| Good1967 | VERIFIED | BJPS 17(4): 319–321 | ok |
| GoodmanSalow2023 | VERIFIED | Phil Rev 132(1): 89–145 | ok |
| GoodmanSalow2025 | VERIFIED | JPL 54(1): 1–49, print Feb 2025 (online Nov 2024) | ok |
| Hawthorne2004 | VERIFIED | OUP. Crossref gives 20 Nov 2003; the conventional citation year is 2004, which is also Salow's | ok (keep 2004) |
| HawthorneStanley2008 | VERIFIED | J Phil 105(10): 571–590 | ok |
| Hong2024 | MISMATCH | Erkenntnis 89(6): 2473–2492, print Aug 2024, online 7 Dec 2022. The mismatch is only the online year | ok |
| Hong2026 | VERIFIED | Phil Perspectives, online 11 Sep 2026. No volume or pages yet, so "early view" is correct | ok |
| Salow2025 | VERIFIED | AJP 103(1): 23–38, print Jan 2025 (online Aug 2024). Confirmed on the article PDF | ok |
| Weatherson2005 | VERIFIED | Phil Perspectives 19(1): 417–443 | ok |

## Step 3: Quotations

| # | Essay text (line) | Source and page | Result |
|---|---|---|---|
| Q1 | CKD block quotation (l.9) | Salow 2025, 33 | exact |
| Q2 | "by itself doesn't predict that openness to further evidence is always required" (l.11) | Salow 2025, 35 (top) | exact (the source's apostrophe is curly) |
| Q3 | "a natural development of it will" (l.11) | Salow 2025, 35 | exact |
| Q4 | "a general problem" (l.11) | Salow 2025, 34 | exact |
| Q5 | "Any solution to that problem will generalize to this one" (l.11) | Salow 2025, 34 | exact |
| Q6 | "can support dogmatism even given Preservation" (l.19) | Salow 2025, 33 (about Weak Knowledge Dominance*) | exact |
| Q7 | "given TRANSPARENCY, K-NORMALITY entails KK" (l.31) | G&S 2023, 107 | exact |
| Q8 | "about the scales' future readings" (l.43) | G&S 2023, 130 n. 40 | exact |
| Q9 | "loses knowledge" (l.49) | G&S 2023, 127 | exact. G&S state the result only for states with \|x−y\| ≤ c; see A11 and P9 |
| Q10 | "sufficiently more normal" (l.51) | G&S 2023, 121 | term exact |
| Q11 | "decisions should be governed by underlying probabilities rather than our knowledge" (l.91) | Salow 2025, 23 (abstract) | exact |
| Q12 | "you should always think that, if the evidence you would discover tells strongly against your view, there is a good chance you're wrong" (l.97) | Salow 2025, 36 | exact |
| Q13 | "entitled to believe q on the hypothesis that p only if discovering p would not require you to stop believing q" (l.99) | Salow 2025, 33 | exact. On p. 34 Salow gives a more careful version ("discovering p and nothing else relevant to q"). The essay's use is consistent with it |
| Q14 | "together entail NO DEFEAT" (l.143) | G&S 2023, 128 | exact |
| Q15 | "even given MARGINS" (l.143) | G&S 2023, 130 n. 40 | exact |
| Q16 | "developed by Fantl and McGrath (2002) and Weatherson (2005)" (l.151) | Salow 2025, 24 n. 3 | exact |
| Q17 | "whenever the difference between maximal and actual probability affects your preferences over available options" (l.151) | Salow 2025, 24 n. 3 | exact |
| Q18 | "these relatively rare counterexamples to Preservation" (l.151) | Salow 2025, 36 | exact |
| Q19 | "the exception rather than the rule" (l.155) | BRN §7 (accepted manuscript, p. 20) | exact |
| Q20 | "may be false" (l.159) | Ahmed & Salow 2019, abstract (the published abstract via OpenAlex is identical) | exact |

## Step 4: Attributions

Salow and Goldstein are on the panel. Hawthorne is also on the panel, but the essay attributes nothing to his works directly; it only reports what Salow or Goodman & Salow say about them.

| # | Claim (line) | Source check | Class | Fix |
|---|---|---|---|---|
| A1 | Goldschmidt gives "representation-theorem foundations for knowledge-based decision theories, including Hawthorne and Stanley's" (l.13) | Abstract: "a new axiomatic method for justifying KDTs" plus "a representation theorem for a KDT proposed by Hawthorne and Stanley (2008)". There is only one representation theorem | oversimplified | P1 |
| A2 | Hong 2024 "explores the view" (l.13) | Subtitle: "An Exploration of 'Knowledge-First' Decision Theory" | accurate | – |
| A3 | Hong 2026, §§1–3: lottery choices, sweetened prospects, and information that distinguishes equally likely payoffs (l.19) | The full text was not retrievable (Wiley 403). The revision notes say this detail came from a summary in `state/external/`, which I was not allowed to open. The abstract supports only "two arguments that … whatever concept the normality framework is capturing … is not action-guiding" | unverifiable | P4 (cut back to what the abstract supports; fetch request already pending at high priority) |
| A4 | Salow notes the 'for all you know' variant "can support dogmatism even given Preservation". He gives no expected-utility treatment (l.19) | p. 33. The paper has no EU treatment: footnote 20 only remarks on EU theory | accurate | – |
| A5 | Geanakoplos gives conditions weaker than partitional learning. Dorst 2020 and Das 2023 "discuss such conditions" (l.19) | Geanakoplos: confirmed (abstract and Theorem 1). Dorst: confirmed (abstract: Trust is necessary and sufficient for always preferring free evidence). Das: abstract only. It argues that the value of information fails for rationally biased inquiries, and I could not confirm that it discusses sufficient conditions | oversimplified (Das) | P3 |
| A6 | BRN: statism, collapse and comparability validate Preservation; Preservation fails in Bjorn; BRN contains no decision theory (l.19, l.91) | BRN Prop. 1 (♦−). App. D.1: AGM preservation "is then equivalent to ♦−". §5 Bjorn. No decision-theoretic content | accurate | – |
| A7 | Salow's Suitcase and the CKD diagnosis (l.11) | p. 33 | accurate | – |
| A8 | Salow "grants" that his response does not predict that openness is required, and that a "natural development" will (l.11) | pp. 34–35. The concession answers Objection 3, which is about "your accuracy about p". The essay drops that context and then applies the point to practical bets. The "general problem" is about decision-making in general, so the essay's use is defensible, but Salow, who is on the panel, will see that the context is missing | oversimplified | P2 |
| A9 | Framework definitions: preorder, ≫ implies ⪰, chaining, irreflexive, statism, comparability, collapse, B(E) (l.25–28) | BRN Def. 2.1 (≫ well-founded, hence irreflexive), Cor. 2.1, constraints on p. 7 | accurate | – |
| A10 | K-normality (2023, 104). TRANSPARENCY ⇒ KK (107). I- and KM-normality validate Margins and allow failures of KK (l.29–31) | 104 and 107 exact. KM: "The 'M' stands for MARGINS". I: "MARGINS can be independently motivated as a consequence of I-NORMALITY" (106). Failures of KK follow from their 105–107 discussion of cliff-edge knowledge, which KK requires and which I-normality and Margins ban | accurate | – |
| A11 | "what Bjorn knows after one weighing depends on the second scale's reading" (l.43), cited only to 130 n. 40 | This claim is on p. 128; n. 40 supports only the "future readings" quotation | accurate, but the locator is incomplete | P8 |
| A12 | G&S 2023, §6: the Bjorn model is statist and comparable and violates collapse. The δ relations. Derivation from independent Gaussians (129) (l.47) | 126 n. 34, 127–129 | accurate | – |
| A13 | Bjorn "loses knowledge" whenever \|r−r′\| > (2−√2)c, "for the case where the first reading is accurate" (l.49) | G&S consider only states ⟨x,x,y⟩ with \|x−y\| ≤ c (p. 127) | oversimplified | P9 |
| A14 | "With Gaussian errors the second reading costs him a belief … with probability about 0.37, as BRN estimate" (l.49) | BRN n. 18: 0.37 is the probability that \|y−z\| ∈ (2c−√2c, √2c], that is, of a failure of ♦− (Preservation). The probability of losing a belief also includes differences above √2c | oversimplified | P10 |
| A15 | c ≈ 1.96 taken from BRN §5 n. 18 (l.47) | n. 18 ("Suppose c≈1.96σ") | accurate | – |
| A16 | G&S's probabilistic account of "sufficiently more normal" (2023, 121) (l.51) | p. 121 states the proposal. The derived formula c² = −2 ln(1−t) is the essay's own and follows for δ distributed χ²₂ | accurate | – |
| A17 | "Goodman and Salow's own discoveries of this kind come by testimony (2023, §8)" (l.79) | In §8 the discovery that one's situation is somewhat abnormal (the "experiment doesn't end on the first trial") is not testimony (p. 136), and G&S say these dynamics "cannot arise in models satisfying STATISM". The testimony examples (p. 138) are of other forms: "no more than c+1", "once or more than c+1" | inaccurate | P11 |
| A18 | n. 47: probabilism predicts failures of statism; their models obey it only for the bodies of evidence they consider (l.79) | p. 138 n. 47 ("rampant failures of STATISM … very special probabilistic symmetries") | accurate | – |
| A19 | Knowledge on all three completions contains B(E) (l.81) | Definitions at 104, 105 and 108–109: clause (i) for K and KM; for I, v ∈ B ⇒ not w≫v | accurate | – |
| A20 | Salow's observation about the 'for all you know' variant (l.85) | p. 33 | accurate | – |
| A21 | Conditioning on evidence is the fallibilist response (l.91, quotation Q11) | p. 23 | accurate | – |
| A22 | Salow's moral; no EU version (l.97) | p. 36 | accurate | – |
| A23 | K^D restricts evidential accessibility as BRN's conditional belief does (App. D.3) (l.97) | BRN Def. D.2 | accurate | – |
| A24 | Salow's constraint (l.99) | p. 33 | accurate | – |
| A25 | "VER conditions on the hypothesis Salow's moral names: that the evidence would change what one does" (l.121) | The moral (p. 36) names the hypothesis that the evidence "tells strongly against your view", not that it changes one's choice | oversimplified | P12 |
| A26 | "Outside statist models conditional and post-discovery knowledge can diverge (BRN App. D.3)" (l.137) | D.3 is about belief: "you now believe p conditional on q iff you would believe p after discovering q … depends on statism" | oversimplified | P13 |
| A27 | Statism, comparability and Margins "together entail NO DEFEAT" (l.143) | p. 128 | accurate | – |
| A28 | The unmarked-clock case "of Ahmed and Salow (2019)" (l.143) | A&S §3 present it as "suggested—for different purposes—by (Williamson [2011])" | accurate (but see P14b for a more careful wording) | P14b (optional, word-neutral) |
| A29 | G&S report that Goldstein & Hawthorne's model predicts failures of No Defeat "even given MARGINS" (l.143) | 130 n. 40 | accurate | – |
| A30 | KK holds on K-normality (l.145) | 107 (given TRANSPARENCY) | accurate | – |
| A31 | Hawthorne (2004, 181), as Salow reports … (l.151) | Salow 24 n. 3: "Hawthorne (2004: 181) suggests the latter: given Good's (1967) result, this naturally falls out of the proposal …"; "the latter" means the encroachment response. The essay properly signals that it is relying on Salow's report | accurate | – |
| A32 | "Salow objects that nothing would confine encroachment to …" (l.151) | p. 36: "it isn't clear what contains the occurrence of pragmatic encroachment to these relatively rare counterexamples" | oversimplified (too strong) | P14 |
| A33 | "BRN argue that statism is 'the exception rather than the rule' (§7)" (l.155) | §7: "This example suggests that statism is the exception rather than the rule" | oversimplified (BRN say "suggests", not "argue") | P14c |
| A34 | G&S: relativizing to *how much does Bjorn weigh* yields a model like Goldstein & Hawthorne's, in which current knowledge is not sensitive to future observations (l.155) | 130 n. 40 | accurate | – |
| A35 | Ahmed & Salow argue that Good's theorem "may be false", "using observations that are not partitional" (l.159) | §3 uses non-partitional observation, but §4 gives a second counterexample from violations of Independence (Allais preferences) | oversimplified | P14d |
| A36 | Geanakoplos's value-of-information result, Theorem 1 (l.65) | CFDP 914 (1989), Theorem 1: (Ω,P) nondeluded, nested and KTYK ⇒ optimal P-plan ≥ optimal Q-plan for a partition Q that coarsens P; with a converse. This matches Lemma 2 with Q trivial | accurate (citation of the "2002 revision" removed) | P6 |
| A37 | Graded normality "which Goodman and Salow defend for measurement" (l.163) | 128 ("we think it is ultimately the right result") and 129 (the probabilistic treatment is "plausible in the present case"). "Graded" is the essay's own term, and their Bjorn model is graded in the essay's sense | accurate | – |
| A38 | Hawthorne & Stanley 2008 propose a KDT (l.13) | Goldschmidt's abstract: "a KDT proposed by Hawthorne and Stanley (2008)" | accurate (via a secondary report) | – |

## Step 5: Page numbers and dates

| Locator | Verified? |
|---|---|
| Salow 2025: 23, 24 n. 3, 33 (×4), 34 (×2), 35, 36 (×2) | all verified against the published pagination |
| G&S 2023: 104, 107, 121, 127, 128, 129, 130 n. 40 (×3), 138 n. 47; §6, §8 | all verified. "130 n. 40" at l.43 also needs "128" (P8). §8 is retained but its claim is rewritten (P11) |
| BRN: §5 n. 18 (×2), §7, App. D.3 (×2) | verified against the accepted manuscript's numbering. The published numbering could not be compared (Springer blocks automated access) |
| Geanakoplos: Theorem 1 | verified in the 1989 CFDP. The "2002 revision" and "June 18, 2002" are unverifiable and removed |
| Hong 2026, §§1–3 | unverifiable; removed (P4) |
| Hawthorne 2004, 181 | not checked directly. The essay gives it explicitly as Salow's report, and Salow 24 n. 3 says so exactly. Acceptable |

## Patch list (apply in order; each "old" string occurs once in v4.md)

**P1** (l.13)
OLD: `Goldschmidt (2024) gives representation-theorem foundations for knowledge-based decision theories, including Hawthorne and Stanley's (2008), and Hong (2024) explores the view.`
NEW: `Goldschmidt (2024) proposes axiomatic foundations for knowledge-based decision theories, with a representation theorem for Hawthorne and Stanley's (2008), and Hong (2024) explores the view.`

**P2** (l.11)
OLD: `Salow grants that his response "by itself doesn't predict that openness to further evidence is always required"`
NEW: `Answering an objection about accuracy, Salow grants that his response "by itself doesn't predict that openness to further evidence is always required"`

**P3** (l.19)
OLD: `Dorst (2020) and Das (2023) discuss such conditions in epistemology.`
NEW: `Dorst (2020) and Das (2023) discuss in epistemology when free evidence has value.`

**P4** (l.19)
OLD: `Hong (2026, §§1–3) criticizes combining normality knowledge with a knowledge-first decision rule, using lottery choices, sweetened prospects and information that distinguishes equally likely payoffs.`
NEW: `Hong (2026) argues that whatever the normality framework captures is not action-guiding.`

**P5** (l.19)
OLD: `Geanakoplos (1989; 2002 revision) gives conditions`
NEW: `Geanakoplos (1989) gives conditions`

**P6** (l.65)
OLD: `(1989; 2002 revision, Theorem 1)`
NEW: `(1989, Theorem 1)`

**P7** (References)
OLD: `Cowles Foundation Discussion Paper 914, Yale University. Revised June 18, 2002; the revision was consulted for Theorem 1.`
NEW: `Cowles Foundation Discussion Paper 914, Yale University. Revised version in *B.E. Journal of Theoretical Economics* 21 (2021): 361–394.`

**P8** (l.43)
OLD: `depends on the second scale's reading and he has inductive knowledge`
NEW: `depends on the second scale's reading (2023, 128) and he has inductive knowledge`

**P9** (l.49)
OLD: `As Goodman and Salow show for the case where the first reading is accurate, he "loses knowledge"`
NEW: `As Goodman and Salow show for the case where the first reading is accurate and the second within $c$ of it, he "loses knowledge"`

**P10** (l.49)
OLD: `With Gaussian errors the second reading costs him a belief about his weight with probability about 0.37, as BRN estimate (§5, n. 18).`
NEW: `With Gaussian errors such a failure of Preservation has probability about 0.37, as BRN estimate (§5, n. 18).`

**P11** (l.79)
OLD: `Goodman and Salow's own discoveries of this kind come by testimony (2023, §8).`
NEW: `Goodman and Salow's own example of such a discovery, that an experiment did not end on its first trial, defeats knowledge only in a model without statism (2023, 136).`

**P12** (l.121)
OLD: `VER conditions on the hypothesis Salow's moral names: that the evidence would change what one does.`
NEW: `VER conditions on a hypothesis in the spirit of Salow's moral: that the evidence would change what one does.`

**P13** (l.137)
OLD: `Outside statist models conditional and post-discovery knowledge can diverge (BRN App. D.3)`
NEW: `Outside statist models conditional belief and belief after discovery can diverge (BRN App. D.3)`

**P14** (l.151)
OLD: `Salow objects that nothing would confine encroachment to`
NEW: `Salow objects that it is unclear what would confine encroachment to`

**P14b** (l.143)
OLD: `a cousin of the unmarked-clock case of Ahmed and Salow (2019)`
NEW: `a cousin of the unmarked-clock case discussed by Ahmed and Salow (2019)`

**P14c** (l.155)
OLD: `BRN argue that statism is "the exception rather than the rule" (§7).`
NEW: `BRN suggest that statism is "the exception rather than the rule" (§7).`

**P14d** (l.159)
OLD: `using observations that are not partitional.`
NEW: `using, among other cases, observations that are not partitional.`

After applying these patches, also update `refs_v4.json`. The `Geanakoplos1989` record should get a note giving the 2021 BEJTE version (doi 10.1515/bejte-2019-0010) and should drop any mention of a 2002 revision. No other metadata changes are needed.

## Residual risks

- BRN's §, note and appendix numbers were checked against the accepted manuscript, not the published PDF. The risk that they differ is low.
- Hong 2026 is now cited only for what its abstract says. If the pending fetch arrives, the overlap paragraph should be rechecked against §§1–3.
- Das 2023 is cited only for what its abstract says.
