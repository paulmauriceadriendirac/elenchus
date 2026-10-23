# E2 external revision, 23 October 2026

Base: `state/drafts/E2/v4.md` at `ba1d5af7cfcaa88d279ff1edcd3d5d5d8a8eb1e0`. This is an external OpenAI-assisted version for review, not a replacement for the Claude manuscript or an eligibility-cleared finalist. No Claude review of this E2 revision was available. Reviews of other tracks arrived later during this pass.

## Substantive repairs

1. **Gallow comparison:** replaced the abstract-only discussion with direct engagement with the cached author manuscript, sections 2.1–2.2, notes 18, 32, and 33, and Appendix B. His distinction between actual evidence and the event of updating is now explicit. His externalist conditionalization permits misclassification; E2's theorem does not. No claim is made to supersede that general theory.
2. **Quantifiers and Reflection:** E2 uses unconditional mean preservation, not conditional calibration. CAR is necessary for preservation uniformly over priors with a fixed mechanism, not necessary at each individual prior. The four-position clock supplies an exact illustration: uniform-prior cancellation for all propositions, a failure at a skewed positive prior, and a failure of conditional Reflection even in the uniform case. The calculation using Gallow's clock is this revision's analysis, not a result attributed to his paper.
3. **Neutrality:** removed claims that symmetry is necessary. The theorem proves sufficiency. CAR balances may be non-neutral, and the manuscript already contained such a counterexample.
4. **No News:** added the nonzero whole-space report-weight hypothesis to Proposition 4(b). Without it, an optimal rule's response to that report is unconstrained. The fully revealing two-state partition demonstrates the omitted boundary case.
5. **Normative premise:** requiring each report's induced score to be proper is now identified as an additional premise, with a rationale and a possible objection. It does not follow merely from propriety of the original scoring rule.
6. **Small precision repairs:** restricted a reweighted-score assertion to full-support credences, distinguished propositions about the modeled state from the enlarged world, and corrected the prose describing the added 64 units of Dana weight.

## Sources and verification

Primary text: `inbox/sources/e2-gallow2021-updating-externalists.txt`, corresponding to https://jdmitrigallow.com/papers/ufe.pdf. The author-hosted PDF was also retrieved directly. The PDF's internal printed pagination is inconsistent (31 of 30); the revision cites sections and notes instead. The relevant argument and technical appendix were read. No CAR or all-prior characterization was identified in those sections; this limited finding is not an exhaustive novelty clearance.

The original E2 checking program was rerun unchanged: all 62 checks passed. Those checks combine exact examples, finite enumeration, sampling, and numerical rank checks; they do not constitute formal verification of every theorem. Exact rational calculations checked the new clock example, including all 16 propositions under the uniform prior. See the attached check logs. The zero-weight boundary is also explicitly described there.

The revised manuscript passed the repository word counter and basic hidden-text/identity scan. The PDF is a reading copy; literature novelty and philosophical significance remain open. This revision has not independently re-audited every inherited citation or quotation.

## Provenance and disposition

The authoring context contains account memory and prior conversation material. The existing external-work exposure flag therefore remains in force. This revision uses the repository essay and retrieved Gallow text; it does not certify clean-context origin. It remains under `state/external/` and does not overwrite `state/drafts/E2/v4.md`, the original methodology report, or the frozen October 22 packet.

The prior E2 methodology draft applies to v4 only. A submission using this version must disclose this additional external revision, full-text comparison, exact calculations, and validation. E2 remains a preparation candidate pending an independent substantive review of this version. No contest submission was made.

Final mechanical result: strict count 5,600; basic manuscript scan passed; 12 PDF pages rendered and visually inspected; no compiler warnings or text-block boundary issues. PDF author metadata is empty. Updated version-specific methodology: `E2-v5-methodology.md`.
