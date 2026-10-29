# A6 final: changelog

**Version:** final (`final/A6/essay.md`), patched from `state/external/submission-sourcechecked-20261029/A6-Free-Evidence-v5.md`. I edited only the copy; the base is unchanged.
**Date:** 2026-10-29
**Mode:** patch. I applied the citation-audit list `state/audit/A6/citations.md` (P1–P14d). That audit was run on `state/drafts/A6/v4.md`, so each patch was matched against the revised base. The patches add no new arguments, cases or claims.
**Word count** (`tools/wordcount.py`): 5,793 strict and 5,766 wordlike, against 5,739 for the base. The limit is 6,000. The target is 5,600, which the base already exceeded.
**Injection check:** no hard flags. The soft flags are panel surnames in genuine citations: Salow 46, Hawthorne 7, Goldstein 3, Fitelson 1 (as co-author of *Deference Done Better*).

## Citation-audit patches

Line numbers refer to `final/A6/essay.md`.

| Patch | Location | Status | What and why |
|---|---|---|---|
| P1 | l.13 | applied | Goldschmidt "proposes axiomatic foundations … with a representation theorem for Hawthorne and Stanley's (2008)". The paper has one representation theorem (audit A1). |
| P2 | l.11 | applied | Added "Answering an objection about accuracy," to restore the context of Salow's concession (A8). |
| P3 | l.19 | already fixed | The base had already replaced "discuss such conditions" with "develop related epistemological questions". That wording no longer says Das gives sufficient conditions, which was the concern under A5. |
| P4 | l.19 | adapted | See note 1 below. The base sentence "challenges normality knowledge through lottery choices, sweetened prospects and information" became "criticizes combining normality knowledge with a knowledge-first decision rule, using lottery choices, sweetened prospects and information that distinguishes equally likely payoffs". I kept the §§1–3 attribution. |
| P5 | l.19 | adapted | The passage had been revised to "gives sufficient conditions", so the OLD string was not present verbatim. "(1989; 2002 revision)" became "(1989)". |
| P6 | l.65 | applied | "(1989; 2002 revision, Theorem 1)" became "(1989, Theorem 1)". The audit verified Theorem 1 in CFDP 914 (May 1989) (A36). |
| P7 | References | applied | Removed "Revised June 18, 2002; the revision was consulted for Theorem 1" and added "Revised version in *B.E. Journal of Theoretical Economics* 21 (2021): 361–394". I checked this by hand on Crossref today (doi 10.1515/bejte-2019-0010: Geanakoplos, same title, vol. 21, issue 2, pp. 361–394, 2021). No mention of a 2002 revision remains in the essay, and "2002" now appears only for Fantl and McGrath. |
| P8 | l.43 | applied | Added "(2023, 128)" for the claim that Bjorn's knowledge depends on the second reading (A11). Checked: G&S 2023 says knowledge "after weighing himself once depends on what the second scale will read". |
| P9 | l.49 | applied | Added "and the second within $c$ of it" (A13). Checked against G&S 2023, 127: "Consider any state ⟨x, x, y⟩, where \|x−y\| ≤ c". |
| P10 | l.49 | already fixed + adapted | The base had already separated weight-belief loss (about 0.417) from BRN's narrower consistent-discovery event. It still attributed "$0.367$" to BRN, but BRN note 18 (accepted manuscript, retrieved today) reads "∼.37". The text now says "BRN's estimate, about $0.37$,". The essay's own value of 0.3668… (VERIFICATION.md) is consistent with this. |
| P11 | l.79 | applied | The essay no longer says that Goodman and Salow's §8 discovery comes by testimony (A17). Checked against G&S 2023, 136. The discovery that "the experiment doesn't end on the first trial" yields a counterexample to No Defeat From What You Already Know, and these dynamics "cannot arise in models satisfying STATISM". |
| P12 | l.121 | applied | "the hypothesis Salow's moral names" became "a hypothesis in the spirit of Salow's moral" (A25). |
| P13 | l.137 | applied | "conditional and post-discovery knowledge" became "conditional belief and belief after discovery" (A26). Checked: BRN App. D.3 is titled "Conditional Belief". |
| P14 | l.151 | applied | "nothing would confine" became "it is unclear what would confine" (A32). |
| P14b | l.143 | applied | "case of Ahmed and Salow" became "case discussed by Ahmed and Salow" (A28). |
| P14c | l.155 | applied | "BRN argue" became "BRN suggest" (A33). Checked against BRN §7: "This example suggests that statism is the exception rather than the rule." |
| P14d | l.159 | applied | Added "among other cases," because Ahmed and Salow's §4 also uses Independence violations (A35). |

**Note 1 (Hong 2026).** I kept only what the other reviewer's records support:
- `VERIFICATION.md` does not mention Hong.
- `SOURCE-REQUESTS.md` records "full publisher text obtained; main action-guidance argument checked". It also says that full access does not mean every passage was reviewed. It therefore does not quite say that the paper was "read in full".
- The section-level content comes from that reviewer's `state/external/ambitious-review-20261022/REVIEW.md` (l.46, l.103: "Main text §§1–3 read"). There, §§1–3 "criticise combining normality-based knowledge with a specified knowledge-first decision rule, K1", with examples concerning "lottery choices, sweetened prospects, and information that distinguishes equally likely payoffs".

What I cut and restored:
- **Cut:** "challenges normality knowledge". The records describe a criticism of its action guidance when it is combined with a knowledge-first rule, not of the normality account of knowledge as such.
- **Restored:** the records' qualifier on "information". The bare word suggested a general value-of-information argument, which the records do not attribute to Hong.

The change adds 9 words. My direct access attempt failed (Wiley returned 403 on 2026-10-29), so this pipeline has still not read Hong's text itself.

## Formal audit

`state/audit/A6/formal.md` is marked "PARTIAL, in progress". It has no patch list and no FALSE items, so I skipped it. Its two open issues are already resolved in the base:
- The "1,724 of the 2,322" sentence no longer appears. The Computations paragraph now gives 64,004 pairs and 3,306 with relative defeat, figures I did not re-verify.
- The 0.37/0.42 issue is now explicit in the text (0.417 against about 0.37).

## Not done and residual risks

- **`refs_v4.json`.** The audit asks for a note on the `Geanakoplos1989` record. Reference files belong to the developer and the citation-auditor, so I left it unchanged; it still needs updating. `state/candidates/A6/refs.json` does not exist (the A6 refs are in `state/drafts/A6/`). `state/drafts/A6/changelog.md` does not exist either, and as instructed I wrote only this changelog.
- **Material added after v4.** It falls outside the v4 audit and is not re-verified here. The *Deference Done Better* paragraph (l.21) has Crossref metadata matching the reference entry (*Philosophical Perspectives* 35(1): 99–150). VERIFICATION.md records the Value, Weak Value and Total Trust check.
- **l.31, "(§6.1)".** This is an internal cross-reference, but it could be misread as a citation of Goodman and Salow. I left it unchanged because it is not on the patch list.
- **BRN locators.** These were checked against the accepted manuscript, not the published version.
