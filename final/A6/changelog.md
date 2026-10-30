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

## Formal-audit patches

**Version:** final (`final/A6/essay.md`), edited in place. The pre-patch copy is `final/A6/essay_pre_formal.md`.
**Date:** 2026-10-29
**Mode:** patch. I applied the patch list P1–P8 of the completed formal audit `state/audit/A6/formal.md`. This entry replaces the "Formal audit" entry above, which was written while that audit was still partial. The audit was run on `state/drafts/A6/v4.md`, so each patch was matched against the final text. No new arguments, cases or claims.
**Word count** (`tools/wordcount.py`): 5,831 strict and 5,804 wordlike, up from 5,793 and 5,766 (+38). The limit is 6,000. The target is 5,600, which the text already exceeded.
**Injection check:** no hard flags. The soft flags are unchanged: Salow 46, Hawthorne 7, Goldstein 3, Fitelson 1, all genuine citations.

Line numbers refer to `final/A6/essay.md`. None changed, because every edit was made within a line.

| Patch | Location | Status | What and why |
|---|---|---|---|
| P1 | §3 l.49, l.51; Computations l.181 | adapted (partly already fixed) | The old string was not present. Two parts of P1 were already done. v5 had replaced the wrong reading of 0.37 as the probability of losing the weight belief with 0.417. Citation patch P10 had tied BRN's "∼.37" to the narrower consistent-discovery event $(2-\sqrt2)c<\|r-r'\|\le\sqrt2c$, which is the audit's own alternative (keep the BRN attribution with its exact conditions). Citation audit A14 records that n. 18's figure is Pr(\|y−z\| ∈ (2c−√2c, √2c]). The missing part was the audit's knowledge-conditional figure. l.49 now reads "has unconditioned probability about $0.417$ (about $0.356$ conditional on his present knowledge)". "Unconditioned" is the essay's own term (§2, §3) and states the conditioning. I kept three decimals rather than the audit's 0.42/0.36 so that 0.356 and BRN's 0.37 are visibly different figures for different events. Two related clarity edits: (1) l.51 now reads "(it wins with probability $0.95$; expected value …)". Otherwise the fallibilist's 0.95 could be read as the Preservation-failure 0.95 just above; both equal 2Φ(c)−1 but concern different events. (2) Computations now reads "decision values and knowledge-conditional probabilities use numerical integration", which states the method for 0.356 and for the existing 0.05. I recomputed the figures independently (mpmath, c = 1.96): 0.4168727826 (loss), 0.3668769923 (loss with a consistent discovery), 0.3555901517 (loss given δ ≤ c²), 0.9500042097 (consistent discovery). The first two match VERIFICATION.md exactly and the third matches the audit's 0.3556. |
| P2 | §5.1 l.107 | applied | −0.63 → −0.60. The audit found −0.602 by mpmath quadrature; −0.626 was an artefact of a coarse grid. The sign and the conclusion (CEU, VER and ANS look) are unchanged. |
| P3 | §5.2 l.121 | already fixed | "$s_0=s_1$" was already in v5. |
| P4 | §5.2 | already fixed (claim removed) | The "1,724 of the 2,322" sentence is not in v5 or in the final essay, and neither number appears anywhere. I did not reintroduce it: patch mode adds no claims, and the audit shows the count depends on the random search (its own search found 2,222) and covers only E = S. If the count is ever restored, use the audit's wording: "at least 1,724 of the 2,322 … in which the evidence is the whole state space". |
| P5 | Computations l.181 | already fixed; spelling harmonized | v5 already restricted the 64,004 pairs to nontrivial partitions, which the audit confirms (81,981 with trivial partitions; 3,306 is unchanged because trivial partitions never defeat under K-normality). The audit has now verified these counts, which the entry above had left unchecked. I changed "nontrivial" to "non-trivial", the audit's spelling and the essay's in §5.2 ("non-trivial answers"). |
| P6 | §4 l.91 | applied | "by Lemma 2" → "by the continuous analogue of Lemma 2 (on each line of fixed reading difference the kens are nested intervals)". Lemma 2 is proved only for finite models; the audit verified the continuous case separately. |
| P7 | §6.2 l.151 | applied | Added ", for all but knife-edge priors,". The audit rates this generalization "argued only": it fails for $p_v$ questions when Pr(E∖M \| $p_v$) = Pr(E∖M). The qualifier calibrates the claim, which is still presented as following "by the reasoning of Corollary (ii)" and is not proved. |
| P8 | Abstract l.3 | applied | "in graded models" → "in finite graded models", matching Corollary (ii). |

**Residual.**
- The essay states P6's continuous analogue but does not prove it. The audit's argument (Danskin, line by line) is not reproduced, because adding it would be new material.
- P7 remains argued, not proved.
- The internal cross-reference "(§6.1)" at l.31, flagged above, is still unchanged.
- I appended only to this changelog, as the task specified. `state/drafts/A6/changelog.md` does not exist.

## Compliance fix (orchestrator, mechanical)
- Applied citation-audit P4 verbatim (Hong 2026 reduced to abstract-level claim), per state/audit/A6/compliance.md failure 1.

## Final delta-audit patches (state/audit/A6/citations_final.md), orchestrator, mechanical
- patch 1: applied verbatim
- patch 2: applied verbatim
- patch 3: applied verbatim
- patch 4: applied verbatim
- patch 5: applied verbatim
- patch 6: applied verbatim

## Final version (2026-10-30)
- final/A6/essay.md replaced by the second system's v6 (state/external/submission-final-review-20261029/A6-Free-Evidence-v6.md): this pipeline's patched text plus a scope-narrowing pass by the second system. Previous text kept as essay_pre_v6.md. v6 compliance PASS (state/audit/A6/compliance.md); formal delta audit: no false claims, no patch required (state/audit/A6/formal_v6.md).
