# Validation of the book-informed revision

The 28 October 2026 version-4 pass is a source and interpretation revision of A4. Its formal models, theorem conclusions and computational implementation are unchanged from version 3. The lemma's statement now explicitly says “non-root” equations, matching the established setting and proof. No new computational theorem check is claimed.

The previous exact-arithmetic verification results are preserved in `checks/prior-revision-results.json`. They include all 355 local category preorders, all candidate subsets in the central finite cases, 2,130 calibration comparisons and 3,195 paired-case comparisons, with no discrepancies. These counts are previous results, not work repeated in this pass.

New validation checks:

- Printed pagination and the relevant book statements were inspected directly, including rendered formal pages.
- A5 and A6 source, essay PDF and methodology files were copied unchanged and checked byte-for-byte.
- All three source word counts remain below 6,000 excluding bibliography; the new A4 count is 5,631.
- The new essay and methodology were checked for account identifiers, repository paths, hidden evaluation instructions and unfinished text.
- The generated PDFs were checked for text extraction, anonymous metadata where appropriate, missing glyphs, bounds and visual layout. The per-file results are in `checks/pdf-validation.json` and `checks/visual-review.json`.

The comparison distinguishes prior results from the proposed residual increment. No independent referee, comprehensive priority search or novelty certification is claimed. The Xiao–Xiong comparison remains limited to the accessible preliminary material, as stated in the assessment and methodology report.
