# A4 v2 revision record

23 October 2026. This revises the external *Causal Refinement Without a Final Layer* manuscript reviewed in `state/blind/P-3b36/reports/S7.md`. It does not replace Claude's separate A4 normality cards or their kill test. A shared problem-area identifier does not make these the same argument.

## Completed changes

1. Replaced the bare graph analogy with an explicit, conditional regularity interpretation: recurrent stage types, active/inactive histories, temporal orientation, particular facts, stability and domain assumptions, and the actual setting/maximality clauses.
2. Proved an exact classification for this relay class: the final 2024a causal conditions hold precisely for a finite forward cover path. The proof covers arbitrary subsets of allowed laws and shows why maximal background facts cannot create a connection between components.
3. Added the accumulating `omega + 1` example and the stronger `N + Z` example. In the latter every noninitial stage has an immediate predecessor, yet the selected source and receiver are not connected by the direct basis. Local existence is necessary in relevant cases but insufficient for endpoint recovery.
4. Corrected the review's suggestion that the local existence condition would suffice to prove equivalence with a stabilization proposal. The third example disproves that sufficiency claim. Also distinguished finite extensions from all extensions and positive-entailment compactness from a finite certificate for the entire causal test.
5. Read the previously unexamined sequel's relevant sections. Its applicability challenge concerns complete descriptions and the recovery of direction. The relay result grants direction and addresses a different completeness condition. The essay no longer implies that the authors overlooked model dependence or that their later non-reductive theory endorses the earlier target.
6. Removed the unsupported generic characterization of Gallow. The essay makes no comparison claim about that account until its treatment of the present infinite domains has been established.

## Validation

`python3 check_a4_revision.py` passes:

- 1,404 causal queries over every subgraph of consecutive edges on 2–6 vertices. One implementation uses classical valuations, maximal fact sets, true settings, law deletion, and the descendant-law constraint; the comparison oracle uses forward graph reachability.
- 1,092 conjunction-minimality checks for the two-history interpretation.
- Seven dyadic refinement checks and one finite illustration distinguishing restriction of global covers from recomputation of covers after restriction.

These finite checks do not establish the infinite result. The manuscript gives that proof using the components of a pairwise-biconditional theory. No claim is made to have tested general Boolean causal models, arbitrary normality rankings, or an alternative theory on the full preemption/switch benchmark suite.

## Source checks

- Andreas and Günther 2024a: repository text `state/ambitious/sources/andreas-gunther-2024-regularity.txt`. Checked journal pp. 5–10, 17, 19, and 26–28 against the extracted text. The text marks PDF page numbers one below journal page numbers. Metadata: PPQ 105, 2–32, DOI 10.1111/papq.12447.
- Andreas and Günther 2024b: publisher full text, especially §§1, 3.1, and 5.1.2, retrieved on 23 October: https://link.springer.com/article/10.1007/s11098-024-02149-z. Metadata: *Philosophical Studies* 181, 2145–2176, published 20 August 2024. The publisher HTML was accessible even though Claude's separate kill test reports failures on other access routes. This resolves access to the relevant text, not every concern raised by that kill test.

## Remaining substantive limits

The most serious limit is the causal interpretation. Aptness and closure of the admitted vocabulary are assumptions. The two histories do not independently distinguish transmission from common dependence. The theorem is therefore a conditional adequacy result, not a fully realized counterexample to the unrestricted theory. The paper states this limitation at the beginning and addresses it in §6.

The broader originality audit remains incomplete. Dense orders and the distinction between local adjacency and global connectivity are elementary; no mathematical novelty is claimed for them. A specialist review must assess whether the application and stronger adequacy condition contribute enough beyond prior work on continuous processes, causal completeness, and model refinement. This revision has not yet received that review and is not an endorsed finalist.

The provenance clarification at the repository root governs interpretation of earlier external flags. This record neither erases disclosed context availability nor treats it as a philosophical objection. The human requested continuation and an audit of instructions; the proof, examples, and revision were developed by the assistant from the prior AI draft, AI referee report, and inspected sources.
