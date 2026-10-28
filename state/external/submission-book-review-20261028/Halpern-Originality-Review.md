# A4 after reading Halpern: originality and submission assessment

28 October 2026. Source comparison by the revising Codex assistant; no new independent-model or human referee report.

**Recommendation: keep A4 as a reserve behind the accuracy and free-evidence essays.** The requested book closes an important access gap and weakens the case for presenting A4 as a major original contribution. It does not supply a counterexample to the essay's bounded classification results. It does show that several surrounding philosophical claims, and an important proof idea, were already in the target literature. The revised manuscript makes that distinction explicit.

The new title is *Limits of Uniform Normality Filters in Actual Causation*. The source count is **5,631 words**, excluding the bibliography and including abstract, headings, mathematical tokens and appendices. The two primary manuscripts remain unchanged: *Holistic Accuracy and the Lockean Thesis* (4,937 words) and *When Acting on Knowledge Makes Free Evidence Harmful* (5,818 words).

## What was actually read

The supplied file is Joseph Y. Halpern, *Actual Causality* (MIT Press, 2016), 240 PDF pages. References here use the printed pagination: printed page 84 is PDF page 95. I read pages 38–40; chapter 3, including its notes; the main discussion in chapter 4, pages 107–127; the proof and surrounding discussion of Theorem 4.4.4, pages 132–136; and the compact-representation discussion, pages 148–150. I also inspected rendered pages containing the decisive preemption example, event-normality definition, stability theorem and proof, and compact default rule. This was a targeted comparison, not a claim to have read every chapter.

The repository branch was still at the previously published version-3 commit when this comparison began. There was no newer Claude revision on that branch to incorporate. The book supplied by the human came without philosophical comments; the interpretation and resulting edits were the assistant's work.

## The decisive overlaps

**1. The conformity/preemption difficulty is already explicit.** In Example 3.2.6, pages 84–85, Halpern considers the rock-throwing model. If the witness in which Billy throws but does not hit is too abnormal, Suzy's throw ceases to be a cause by itself under the modified definition, while the conjunction of the two throws becomes a cause. Making Billy's accuracy explicit sharpens the problem. A4's earlier presentation of the late-preemption consequence therefore cannot carry an originality claim. Version 4 cites the example directly.

The book also supplies responses. Section 3.3, pages 85–86, grades causes by their witnesses instead of excluding causes with insufficiently normal witnesses. Section 3.5, pages 97–99, compares events consisting of sets of contexts. This changes the object of the normality comparison and addresses the accuracy-variable problem. Pages 100–102 discuss further limits and a proposal involving changes in normality. A theorem about the essay's four local categories and hard world filter does not refute those approaches.

**2. The frozen-witness proof is closely related to an existing proof.** Halpern's Theorem 4.4.4(b), page 121, concerns conservative extensions whose newly added variables respect their equations in the relevant normality ordering. It preserves modified-definition causes and excludes new-variable members of a cause. The proof on pages 133–134 removes conforming interventions and uses AC3 minimality to exclude redundant candidate members.

A4's lemma uses the same kind of reasoning: when a witness satisfies all non-root equations, dropping non-root interventions leaves the same solution; minimality then confines the candidate to roots, and the roots alone change the outcome. The statements are not identical. Halpern compares models and assumes a relation between their normality orderings; A4's lemma concerns one witness in one acyclic model. That difference warrants retaining the useful lemma, but not presenting its proof principle as an independent advance. Version 4 acknowledges the relationship beside the statement and in the introduction.

**3. The general representational diagnosis is established prior work.** Section 4.1, especially pages 108–111, explains that models unable to distinguish relevant scenarios cannot produce the desired differences in causal judgment. Halpern illustrates this with different mechanism descriptions giving the same equations for the initially represented variables. Section 4.6, pages 124–126, discusses the significance of independent interventions and temporal representation. Consequently, the essay's general observation that omitted information cannot be recovered from identical represented data is not new.

The Seedlings/Doorbells pair may still contribute as a specific test: its four stipulated default assignments correspond under the displayed isomorphism. But the invariance proposition is elementary. Its philosophical force also depends on defending opposite causal judgments for the coarse outcomes, rather than importing timing or process information from the stories while excluding it from the models.

**4. The demand to justify normality rankings is already acknowledged.** Page 83 and section 4.7, pages 126–127, directly discuss the risk of fitting judgments by adjusting normality. Halpern says model choices need motivation and gives statistical and normative resources for assessing them. A4 cannot offer this explanatory demand as something his account overlooks. The revised conclusion uses the classification to illustrate a particular transfer problem for a uniform policy, while crediting the general issue.

## What may remain distinctive

| Result in A4 | Increment that survives this comparison | Limitation |
|---|---|---|
| Theorem 1: four-case calibration | Exact necessary and sufficient comparisons for one uniform order on four local categories, across three HP definitions | The category scheme and componentwise rule are substantive restrictions; the target judgments are assumed |
| Theorem 2: three-case comparison | No ranking in that class fits the specified Doorbells, Locusts and short-circuit verdicts under any of four codings | It does not cover all codings, world rankings, graded accounts or event-based accounts |
| Seedlings/Doorbells | An explicit isomorphic pair preserving the four specified default assignments | General invariance is familiar; the coarse causal contrast remains contestable |
| Regularity-theory corollary | A sufficient condition for the normal-backup failure in the stipulated regularity definitions | Beckers's underlying normal-backup challenge is prior work |

I did not find the exact calibration and paired-case classification in the inspected book passages. That is a limited comparison result, not a certification of priority. The strongest defensible novelty claim now concerns those specific results, not the discovery that normality or representation can create causal problems.

The local class is not entirely unmotivated. Halpern's compact rules in section 5.2.2, pages 149–150, make equation conformity a useful default for typicality while permitting exceptions and comparisons across variables. A4 asks what happens when a modeler instead insists on one transferable category ordering with componentwise comparison. The formal results identify a cost of that simplification. Their importance depends on whether this restricted policy is worth using or defending. The essay has not established that it is a leading or unavoidable commitment of normality theories.

## Repairs made, and what they establish

Version 4 changes the title, abstract, literature comparison, interpretation of the lemma, discussion of alternatives and conclusion. It adds the book with exact printed-page citations. It distinguishes the hard filter from graded causation and event-based normality. It also corrects a stale computational summary: the earlier broad battery used 75 weak orders and a size-three candidate bound, while the later targeted checks covered all 355 preorders and every candidate subset for the central cases.

No theorem conclusion, model equation, numerical result or computational implementation changed. The lemma now explicitly refers to non-root equations, matching the definition and proof already used. The previous exact checks remain the evidence for the finite claims: 2,130 calibration comparisons and 3,195 paired-case comparisons without discrepancy. They were not rerun in this source-focused revision, and they do not establish originality. New checks cover the text, citations, word count, anonymity and PDF output.

The repairs improve attribution and prevent the article from claiming to defeat theories outside its assumptions. They do not create a more important mathematical result by changing the prose. On originality and philosophical significance, this remains a modest, conditional contribution. I would prioritize the other two essays and would not include a third merely to use every available submission slot. A4 remains available as a carefully limited third candidate for the user's decision.

## One additional comparison remains open

A targeted primary-literature search located Zhizun Xiao and Wei Xiong, “A refinement of the Hitchcock definition of actual causation,” *Humanities and Social Sciences Communications* 13, 1088 (2026), published 5 May 2026, https://doi.org/10.1057/s41599-026-07470-y.

The retrieved abstract and introduction propose a refinement of active-route causation addressing switches, short circuits, bogus prevention and a switch variant. Those topics make it relevant to the surrounding debate. Retrieval exposed some introductory and background text, but follow-up access to the core definitions and proofs failed at the publisher's sign-in redirect. I have not assessed that definition or its claimed results and do not infer that it duplicates A4's theorems. A PDF is needed to complete that comparison. This is a newly identified follow-up, separate from the now-resolved Halpern request.

## Reading and submission files

The combined reading copy includes this assessment followed by the three essays. It is for personal review. For any contest entry, use the individual anonymous essay and its matching methodology report:

| Essay | Matching report |
|---|---|
| Holistic-Accuracy-v3.pdf | A5-Methodology.pdf |
| Free-Evidence-v3.pdf | A6-Methodology.pdf |
| Causation-v4.pdf | A4-Methodology-v4.pdf |

The archive preserves the three current manuscripts and reports, this comparison, the A4 revision difference, and validation records. Historical versions remain available separately. No contest form has been submitted.
