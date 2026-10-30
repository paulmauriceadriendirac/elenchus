# Production methodology: A4

Companion to **A Switching Dilemma for Normality in Actual Causation**, version 8. Prepared 29 October 2026.

The matching essay contains **5,581 words** under the conservative source count, including all non-bibliographic material. This anonymized report covers production, revision and verification; it replaces the earlier short verification-only note.

## Production setting and models

The essays were developed and revised during 21–29 October 2026 through two AI systems working with a shared project repository. This report reconstructs the production method from the retained drafts, review reports, source comparisons and production summary. It describes recorded work rather than treating a planned workflow as a completed experiment. Some historical details remain unverified.

The Claude-side records identify the scaffold designer, orchestrator, drafting agents and review agents as **Claude Opus 5.5**, with model string `claude-opus-5-5`; the orchestrator's recorded environment was Claude Code 2.1.306. These identifiers are reported from that system's records, not independently recovered from service telemetry. The other system was an **OpenAI Codex assistant**. A verified session-by-session model-version record for its earlier work was not available. It contributed candidate generation, critical review, mathematical checks, source comparison, substantive revisions and final document preparation. The present finishing pass also used Codex. No later reviews by additional model providers are included in this report.

## Candidate generation and selection

The initial AI-written scaffold proposed a broad funnel: survey the literature, generate candidates, reject anticipated or defective claims, draft survivors, obtain critical reviews, revise, audit citations and proofs, and package the results. Public research interests of the intended academic audience informed the literature areas and reviewer personas. Those personas were prompts to models, not participation by the named scholars.

The original plan was reduced after budget and usage constraints. Three early essays were drafted from literature maps; prior-art checks led to replacement of some initial theses. A later problem survey listed 30 problems, shortlisted ten and selected six. Source availability helped determine which three were developed first. For these three, ideation agents produced fifteen proposals, five per topic. Recorded critical assessments rejected eight and repaired or merged seven into three essay plans. An additional Codex idea search generated 120 candidates and narrowed them through 40, 16 and eight; its survivors did not become these final essays. One other essay was withdrawn after its central objections remained unresolved.

Selection ultimately used the models' recommendations and the operator's choice among AI-produced outputs. The proposed formal draft tournament was not run. The process was exploratory and adaptive, not a preregistered evaluation. This matters because the final essays were selected from substantially more attempts than the three displayed here.

## Instructions, scaffolding and revision

The recurring instruction pattern was to reconstruct the target's strongest argument, identify its assumptions, compare the closest primary literature, propose a precise increment, look for counterexamples, repair errors and narrow unsupported conclusions. Ideation tasks asked for multiple candidate arguments and an explicit account of what each would add. Critical tasks asked models to find prior art, invalid steps, misleading attributions and objections that would survive a charitable reading. Drafting tasks required a self-contained philosophical argument within the word limit. These are descriptions of the prompt functions, not a verbatim prompt archive.

Claude's workflow assigned separate roles for literature surveying, ideation, critical testing, drafting, revision, citation checking, formal checking and document checks. Some roles existed only in the planned scaffold; an editor stage and the proposed multi-round ranking tournament were not completed. Selected drafts received anonymous model-review packets containing the manuscript, a rubric and a main source. Some packets contained an additional comparator. The review roles included a subject specialist and an advocate of the position criticized. Their reports informed substantive revisions. Separate model instances and anonymous packets reduce some contextual influence but do not create human expert review or establish statistical independence between judgments.

Codex reviewed successive drafts against primary sources and supplied counterexamples, calculations and restrictions on claims. The two systems then incorporated each other's revisions. The last Claude pass added citation and proof-audit corrections. This edition incorporates those corrections, reviews the changed claims, and produces matching manuscripts and PDFs. It does not count a proposed check as completed or describe a previous draft's review as a new review of this version.

## Research and computational tools

The systems used web search, author-posted papers, journal or repository copies, uploaded texts, text extraction and the shared repository. Bibliographic metadata checks supplemented reading; abstracts and metadata were not treated as substitutes for a full-text check of a theorem. Essential inaccessible texts were requested as documents rather than as human explanations.

Computational work used Python, exact rational arithmetic, symbolic algebra, finite-model enumeration, numerical integration and, in the Claude-side causation audit, an SMT solver. Such calculations checked examples and finite domains. Written proofs support claims quantified over all decision problems or all models in a stated class. Neither numerical agreement nor finite enumeration establishes originality. The essay-specific section below distinguishes checks performed for this edition from previously recorded checks that were retained.

PDFs were generated from the final Markdown sources using Pandoc and XeLaTeX. The existing counting script counts title, abstract, headings, mathematical tokens, footnotes and appendices, excluding only the bibliography. Text and metadata were checked for identifying strings, and rendered pages were visually inspected. The combined reading copy is an additional convenience document; the individual essay and its matching report are the paired documents.

## Human involvement and context

The operator set the task and deadline, requested more candidates and stronger originality and significance, supplied or relayed source documents and model reviews, asked for further revision, and selected among AI-generated work. Recorded methodological suggestions included using relevant philosophical perspectives and demanding criticism. The available project review identified no substantive philosophical argument, example, distinction or repair supplied by the operator that entered these essays. This is a limited provenance finding, not a certification of every earlier session.

Claude's records state that automatic memory was disabled and personal-account retrieval was not used in its production workflow. A previous Codex disclosure recorded possible availability of unrelated personal context; the subsequent limited audit identified no human philosophical contribution but did not certify all historical context. That limitation remains disclosed. This finishing pass did not retrieve personal context or use unrelated task histories to develop arguments. Raw conversations, human-input histories and internal run logs are not included in this report.

## Resources and limitations of the record

The Claude-side production summary reports 3,181 requests, including 2,853 subagent requests, across 73 transcript files, and estimates approximately US$433.20 at list prices. It records 64 ten-minute intervals containing activity, approximately eleven hours of occupied intervals across the project period; this is not a measurement of processor time or summed agent time. The estimate was reported before the final finishing pass, was not independently recomputed here, and is not a bill: work used subscription access with usage limits. Reliable cumulative Codex token use, cost and machine time were unavailable. Total human time and a defensible cost allocation to this particular essay could not be established.

The earlier anonymous model reviews were critical; no calibrated human-expert assessment of these final versions has been completed. The workflow cannot demonstrate that the literature search was exhaustive, that model judgments are independent, or that the surviving contributions are important enough for publication. The most consequential remaining questions are stated below. No contest submission has been made as part of this finishing pass.

## Essay-specific development and checks

The initial proposals concerned the switch–preemption contrast, calibration of normality and a frozen-witness lemma. A critical test supplied the Doorbells model and coding comparisons. Later Codex revisions repaired the lemma, restricted the scope and compared the argument with book-length treatments. A model referee's cross-definition objection led to the blocked-tracks case and the current pair of witness-profile theorems. Further review restricted the additive escape argument and made the fixed-context assumptions explicit.

Halpern's *Actual Causality* was available as an uploaded full book. The prior source comparison inspected the relevant normality and preemption discussion, including pages 38–39, 79–81 and 90–91, and the conservative-extension reasoning used in the lemma comparison. Wysocki's *Conjoined Cases* was read as a close comparator: it gives a stronger obstruction in a different setting. The present essay's proposed increment is the cross-model profile identity and cross-definition comparison, not a general impossibility of normality-based causation. This finishing pass also checked Gallow's Doorbells discussion on pages 85–86 and the final conditions in Andreas and Günther's 2024 regularity theory against primary texts.

Earlier checks inspected the witness arguments and evaluated the boundary additive score $(r,a,b,c,d)=(2,0,-1,-5,-3)$: the blocked-tracks witness has gain 3 and the clear-tracks witness gain 1. Claude's subsequent formal audit records a separate implementation of the three definitions, enumeration of 355 preorders, exact SMT checks, and additional tests of the conformity lemma. Those complete programs were not rerun for this edition. Their reports are computational support; the written witness arguments carry the impossibility claims. The regularity-theory calculations in Section 7 remain author-computed rather than independently reimplemented here.

The last Claude corrections replace “total orders” with “total preorders,” remove an overinclusive claim about Billy's throw, repair the account of additional switch contingencies, specify the variable-indexed escape, and correct the account of Gallow's model, which retains the bells. This edition preserves those corrections. The mathematical content of this essay is unchanged from Claude's final manuscript at the reviewed checkpoint.

The main remaining assessment is philosophical significance relative to the existing literature. The result is conditional on event coding, profile anonymity and the stated Pareto condition. Different model choices or principled non-anonymous information can escape it. The application to Xiao and Xiong remains conditional on availability being evaluated at a fixed context with nonintervened roots unchanged. A4 is therefore retained as the less secure third candidate rather than presented as equally strong evidence of a novel contribution.

## Final document pairing

The manuscript `A4-Causation-v8.md` and anonymous PDF `A4-Causation-v8.pdf` contain the same version 8 text. This report is paired with that version. Subsequent substantive revisions or additional model reviews should be reflected in an updated report.
