# Validation, source boundaries, and provenance

22 October 2026. This record describes checks actually performed. It is not a certification of originality, philosophical importance, competition eligibility, or formal correctness.

## Outputs and counting

Essay 4: **5,980** strict tokens excluding references, 13 PDF pages. Essay 5: **5,976**, 14 PDF pages. Titles, subtitles, abstracts, headings, tables, and mathematics are included by `tools/wordcount.py`; the trailing References sections are excluded. The script counts whitespace-separated tokens after Markdown stripping. An organizer's treatment of mathematical expressions can differ. The script hash and source/PDF SHA-256 hashes are recorded in `validation-results.json`.

Both Markdown essays were checked for HTML comments and common invisible or bidirectional control characters; none were found. This is a limited mechanical check, not an assertion that every possible submission-integrity issue has been ruled out.

## Mathematical verification

The proofs in both revised essays were reread against their stated assumptions. In essay 4, the central steps are the two-point inclusion argument, nonnegative one-versus-rest imbalance, and independent variation of regular conditional priors inside fibers. In essay 5, they are equalization of the two selective-mechanism regrets, domination of no-disclosure regret at that equalizer, and the differential equation forced by strict propriety plus preservation at every prior.

`verify-results.py` uses only Python's standard library. Running it produced **75 successful checks**, saved in `check-results.json`. They cover exact rational examples, a 3-state weighting representation, the nonsaturated cross-pair construction, a nontrivial CAR imbalance/bound, numerical equalizers under four losses across seven priors, grid comparisons, and Brier randomized-source comparisons. These are spot checks, not machine-checked proofs. Numerical samples do not establish the universal statements.

Particular limits retained in the essays:

- Regular priors and finite spaces matter to the CAR arguments.
- The all-priors certificate is stronger than the fixed-prior certificate.
- The approximate bound is not a universal posterior-error bound.
- Proposition 5 of essay 5 assumes normalized, monotone, continuously differentiable proper loss components.
- The general finite minimax representation additionally requires convexity and continuity in the forecast; the direct binary proof does not.
- No arbitrary-state square-root formula or unrestricted uniqueness of minimax conditionalization is asserted.

## Source and originality audit

Meehan and Zhang's *Bayes Is Back* was consulted in the repository's extracted full text, including the discussion of fixed prior spaces and the weighted-accuracy characterization. Its CAR/extensionality connection and least-favorable-weight representation are credited as background in the revised essays.

The relevant portions of primary sources were inspected for the comparisons actually made: Grünwald–Halpern (2003) on CAR and universal observation restrictions; Gill–Grünwald (2008) on CAR geometry; Jaeger (2005), Theorem 4.17, on procedural robustness; van Ommen et al. (2016) on robust updating and loss dependence; Che–Li–Luo (2026) on minimax regret, timing, and task aggregation; Buja–Stuetzle–Shen (2005), page 2, on the already known boosting score; Grünwald–Dawid (2004) on robust-Bayes game theory; and Grünwald–Halpern (2011) and Halpern–Leung (2016) on dynamic issues. Bibliographic links are in the essays. This is a targeted comparison, not a cover-to-cover review of every cited work.

The candidate increments requiring further priority checks are essay 4's exact compression classification/certificate and essay 5's characterization of the boosting loss by prior preservation in this particular factive-report game. Search results did not establish that these are first in the literature. Familiar ingredients and short derivations may already occur in a different vocabulary. Novelty therefore remains provisional; no “originality percentage” is supplied.

The ideation dossiers have a separate source register indicating whether full text, an introduction, an abstract, or a publisher excerpt was available. Most candidates have not had a full-text novelty audit. The three assessment passes are successive judgments by this assistant, not independent referees. The 120-card count measures proposals, not 120 demonstrated independent discoveries. Some internal overlap was detected and is explicitly parked.

## Rendering

Pandoc converted Markdown with TeX mathematics to Typst, then Typst 0.15 compiled the PDFs. The final layout uses A4 pages, 2.5 cm margins, 11-point Latin Modern Roman, Latin Modern Math, and page numbers. The existing standalone converter's empty-font default failed; a non-standalone conversion with an explicit font preamble succeeded. No substantive text was changed by the renderer.

All pages were rendered and inspected in contact sheets, with larger inspections of the tables and principal mathematical passages. A converter defect in sized square brackets was found and repaired by using equivalent `\left[` / `\right]` source commands. The affected pages were rendered and inspected again. Extracted text was checked for the failed bracket tokens; text-block bounds were checked against the page rectangles. These checks found no remaining clipping or formula-command artifacts.

## Provenance and handoff boundary

The revisions and candidate pool were produced by the Codex assistant in the continuing user conversation. Inputs included the existing essays, repository materials, Claude's submitted referee reports and issue comments, and primary literature retrieved during the work. The user requested greater significance, near-limit length, broader ideation, and revisions informed by Claude. No additional independent model panel was run here.

This was not a clean-room session: the continuing conversation contained prior project context and user-related context. No claim is made that this satisfies a contest's clean-context or provenance requirements. The deliverable is a revision and research package for further assessment. It does not record a contest submission or attest that all historical inputs are eligible.

The reviews copied into this folder match the substantive current report texts at remote commit `0bd657de69c0d06ddc9e2dfb159af0fd16f6bc99`, with only a final newline added locally. Current issue comments were checked as well. The branch's newer ambitious-track status was read; this package supplies additional candidates for that work, rather than replacing its plans or claiming that its future review rounds have occurred.
