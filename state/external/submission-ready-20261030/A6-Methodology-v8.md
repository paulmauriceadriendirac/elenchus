# Production methodology: A6

Companion to **When Acting on Knowledge Makes Free Evidence Harmful: Good's Theorem in Normality Models**, version 8. Prepared 30 October 2026.

The matching essay contains **5,948 words** under the conservative source count, including all non-bibliographic material. This anonymized report covers production, revision and verification; it carries forward the preceding production report and adds the readability revision described below.

## Production setting and models

The essays were developed and revised during 21–30 October 2026 through two AI systems working with a shared project repository. This report reconstructs the production method from the retained drafts, review reports, source comparisons and production summary. It describes recorded work rather than treating a planned workflow as a completed experiment. Some historical details remain unverified.

The Claude-side records identify the scaffold designer, orchestrator, drafting agents and review agents as **Claude Opus 5.5**, with model string `claude-opus-5-5`; the orchestrator's environment was recorded as Claude Code 2.1.306 initially and 2.1.314 later in the run. These identifiers are reported from that system's records, not independently recovered from service telemetry. The other system was an **OpenAI Codex assistant**. A verified session-by-session model-version record for its earlier work was not available. It contributed candidate generation, critical review, mathematical checks, source comparison, substantive revisions and final document preparation. The preceding substantive finishing pass and the current readability revision also used Codex. No later reviews by additional model providers are included in this report.

## Candidate generation and selection

The initial AI-written scaffold proposed a broad funnel: survey the literature, generate candidates, reject anticipated or defective claims, draft survivors, obtain critical reviews, revise, audit citations and proofs, and package the results. Public research interests of the intended academic audience informed the literature areas and reviewer personas. Claude's final methodology check describes its reviewer personas as composite subfield profiles. No scholar's participation or endorsement is claimed.

The original plan was reduced after budget and usage constraints. Three early essays were drafted from literature maps; prior-art checks led to replacement of some initial theses. A later problem survey listed 30 problems, shortlisted ten and selected six. Source availability helped determine which three were developed first. For these three, ideation agents produced fifteen proposals, five per topic. Recorded critical assessments rejected eight and repaired or merged seven into three essay plans. An additional Codex idea search generated 120 candidates and narrowed them through 40, 16 and eight; its survivors did not become these final essays. One other essay was withdrawn after its central objections remained unresolved.

Selection ultimately used the models' recommendations and the operator's choice among AI-produced outputs. The proposed formal draft tournament was not run. The process was exploratory and adaptive, not a preregistered evaluation. This matters because the final essays were selected from substantially more attempts than the three displayed here.

## Instructions, scaffolding and revision

The recurring instruction pattern was to reconstruct the target's strongest argument, identify its assumptions, compare the closest primary literature, propose a precise increment, look for counterexamples, repair errors and narrow unsupported conclusions. Ideation tasks asked for multiple candidate arguments and an explicit account of what each would add. Critical tasks asked models to find prior art, invalid steps, misleading attributions and objections that would survive a charitable reading. Drafting tasks required a self-contained philosophical argument within the word limit. These are descriptions of the prompt functions, not a verbatim prompt archive.

Claude's workflow assigned separate roles for literature surveying, ideation, critical testing, drafting, revision, citation checking, formal checking and document checks. Some roles existed only in the planned scaffold; an editor stage and the proposed multi-round ranking tournament were not completed. Selected drafts received anonymous model-review packets containing the manuscript, a rubric and a main source. Some packets contained an additional comparator. The review roles included a subject specialist and an advocate of the position criticized. Their reports informed substantive revisions. Separate model instances and anonymous packets reduce some contextual influence but do not create human expert review or establish statistical independence between judgments.

Codex reviewed successive drafts against primary sources and supplied counterexamples, calculations and restrictions on claims. The two systems then incorporated each other's revisions. The last Claude pass added citation and proof-audit corrections. The preceding substantive edition incorporated those corrections and reviewed the changed claims. The current edition improves exposition and produces matching manuscripts and PDFs. It does not count a proposed check as completed or describe a previous draft's review as a new review of this version.

## Research and computational tools

The systems used web search, author-posted papers, journal or repository copies, uploaded texts, text extraction and the shared repository. Bibliographic metadata checks supplemented reading; abstracts and metadata were not treated as substitutes for a full-text check of a theorem. Essential inaccessible texts were requested as documents rather than as human explanations.

Computational work used Python, exact rational arithmetic, symbolic algebra, finite-model enumeration, numerical integration and, in the Claude-side causation audit, an SMT solver. Such calculations checked examples and finite domains. Written proofs support claims quantified over all decision problems or all models in a stated class. Neither numerical agreement nor finite enumeration establishes originality. The essay-specific section below distinguishes checks performed during substantive review from the document checks repeated for this readability edition.

PDFs were generated from the final Markdown sources using Pandoc and XeLaTeX. The existing counting script counts title, abstract, headings, mathematical tokens, footnotes and appendices, excluding only the bibliography. Text and metadata were checked for identifying strings, and rendered pages were visually inspected. The combined reading copy is an additional convenience document; the individual essay and its matching report are the paired documents.

## Human involvement and context

The operator set the task and deadline, requested more candidates and stronger originality and significance, supplied or relayed source documents and model reviews, asked for further revision, and selected among AI-generated work. Recorded methodological suggestions included using relevant philosophical perspectives and demanding criticism. The available project review identified no substantive philosophical argument, example, distinction or repair supplied by the operator that entered these essays. This is a limited provenance finding, not a certification of every earlier session.

Claude's records state that automatic memory was disabled and personal-account retrieval was not used in its production workflow. A previous Codex disclosure recorded possible availability of unrelated personal context; the subsequent limited audit identified no human philosophical contribution but did not certify all historical context. That limitation remains disclosed. The preceding substantive pass did not retrieve personal context or use unrelated task histories to develop arguments. Raw conversations, human-input histories and internal run logs are not included in this report.

## Resources and limitations of the record

The Claude-side production summary reports 3,181 requests, including 2,853 subagent requests, across 73 transcript files, and estimates approximately US$433.20 at list prices. It records 64 ten-minute intervals containing activity, approximately eleven hours of occupied intervals across the project period; this is not a measurement of processor time or summed agent time. The estimate was reported before the final finishing pass, was not independently recomputed here, and is not a bill: work used subscription access with usage limits. Reliable cumulative Codex token use, cost and machine time were unavailable. Total human time and a defensible cost allocation to this particular essay could not be established.

The earlier anonymous model reviews were critical; no calibrated human-expert assessment of these final versions has been completed. The workflow cannot demonstrate that the literature search was exhaustive, that model judgments are independent, or that the surviving contributions are important enough for publication. The most consequential remaining questions are stated below. No contest submission has been made as part of the preceding substantive pass.

## Essay-specific development and checks

The initial proposals combined the normality-theoretic boundary for safe inquiry, a graded-model consequence, repeated weighing and a conditional repair. Later model reviews generated the verdict-change and answer-by-answer evaluations, a five-state counterexample, and the safety proof for answer-by-answer evaluation. The reviser added the costly-inquiry conflict. Codex subsequently clarified the future KDT policy, restricted conclusions to the specified rules, separated distinct probability events, and added the comparison with *Deference Done Better*.

The source checks include Goodman and Salow's normality framework and *Belief Revision Normalized*, the reported conditional-dominance principle, and the published *Deference Done Better*. For the last of these, the preceding substantive pass checked the definitions of Value and Weak Value, the Appendix B equivalences, and Theorem 4.1. The general characterization is earlier work. The essay's intended increment is its formulation in terms of relative defeat and gappedness in the stated normality models, together with the conditional-rule examples. Hong 2026 is described only at the abstract-supported level; no essential proof rests on an unverified section-level attribution to that paper.

Earlier exact calculations gave, in the five-state example, KDT value $-1952/6125$, VER value $-12847/1568000$, and ANS value $32917/217000$. In the four-state example without relative defeat, KDT and ANS give $1/20$, VER $-49/40$ and CEU $-49/20$. Those unchanged examples were not rerun in the preceding substantive pass. Previously checked Gaussian integrations distinguish weight-belief loss, approximately 0.417, from loss with a consistent discovery, approximately 0.367. Claude's later correction adds approximately 0.356 conditional on present knowledge; the preceding substantive pass independently integrated that event and obtained 0.3555901517.

That substantive pass independently recomputed the corrected conditional-bet value using one-dimensional SciPy quadrature with the decline event evaluated on its full candidate region. It obtained threshold $d_*=2.19562510$, or $1.12021689c$, and conditional expected value $-0.60208829$ at $c=1.96$ and ten-to-one odds, supporting the essay's rounded $-0.60$. This is a numerical check, not an independent philosophical endorsement. The complete finite enumeration was not rerun for this edition; its recorded domain is 64,004 situation–question pairs with nontrivial partitions. Sampled utilities do not verify the universal quantifiers.

Two peripheral claims were narrowed in the final pass. An optional continuous safety assertion, invoking an unproved extension of the finite laminar lemma, was removed. The broad encroachment generalization about almost all priors was also removed; the discussion now compares the two specified inquiry evaluations and states its consequence conditionally. K-normality and the required availability of questions are explicit in the introductory thesis and conclusion. These changes preserve the finite theorems and the separately analyzed weighing example.

Remaining limits include available questions, statism, the fixed current ken, the future policy, commitment to ignore evidence, alternative conditional theories, and question-relative normality. The essay does not establish that every knowledge-based decision theory or every interpretation of the qualitative conditional principle fails.

## Readability revision

The revision gives a plain-language gloss of the ken and the gap condition, adds a short proof roadmap, and separates the deference comparison, probability events, conditional-rule examples and encroachment discussion into shorter paragraphs. Little text was added because the manuscript was already near the limit. The formal statements, equations and proof text are unchanged; proof paragraphs were divided without changing their wording. Manuscript comparisons confirmed preservation of the formal content, and word counts, anonymity checks and PDF layout checks were repeated. The final review described next followed this prose revision; earlier substantive checks are identified above.

## Final review

Codex read Claude's completed v6 formal and document audits, and rechecked the mapping to Value and Weak Value against the published Deference Done Better. Claude's audit reports numerical agreement and no required formal patch; its computations were not rerun in this pass. The current revision adopts its two optional clarifications: the graded-model gloss is explicitly finite, and the encroachment criterion is stated in terms of different rankings. The Bjorn passage now explicitly specifies a normal situation. The finite proof arguments, examples and numbers are unchanged. This was further review by an AI system involved in developing the essays, not independent expert endorsement.

## Submission pass

The submission pass re-read the complete manuscript and proof appendix, and revisited the Value/Weak Value comparison in Deference Done Better. One explanatory claim in the construction for Theorem 3 was too broad: CEU need not agree with KDT on every comparison involving the looking policy. Exact arithmetic in the essay's three-state illustration gives KDT a value of 1/2 for the original bet over looking, but CEU a value of -9/2; both give the current best act an advantage of 7/10 over looking. The revised wording claims agreement only for the present best act versus looking and for choices among the primitive acts. The theorem, mathematical construction, examples, displayed equations and appendix proofs are unchanged. The earlier numerical integration suites were not rerun.

## Final document pairing

The manuscript `A6-Free-Evidence-v8.md` and anonymous PDF `A6-Free-Evidence-v8.pdf` contain the same version 8 text. This report is paired with that version. Subsequent substantive revisions or additional model reviews should be reflected in an updated report.
