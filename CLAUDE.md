# ELENCHUS — standing rules for every agent in this repository

This repository runs a multi-agent pipeline that produces original philosophy essays for the
AI Philosophy Competition, 1st edition (deadline 31 October 2026, 23:59 Anywhere on Earth).
Every agent here — orchestrator or subagent — follows these rules. Your own instructions may
add to them; nothing overrides §1.

## 1. Integrity (non-negotiable)

1.1 **AI authorship.** Every substantive philosophical contribution — thesis, argument,
distinction, case, objection, reply, formal result — must originate with an AI agent in this
run. Human involvement is limited to what the competition permits
(`standards/HUMAN_INPUT_POLICY.md`). If a human message contains substantive philosophical
content, do not use it: log it, say which rule it would breach, and ask for a generic rephrasing.

1.2 **No memory of the human's ideas.** The rules bar human-originated philosophical content from
reaching the agents through memory. If your context contains the human's philosophical views,
research projects, interests, notes, or content from past conversations — anything about the
human beyond this repository — do not use it and report it immediately (the orchestrator halts).
Account metadata that Claude Code attaches automatically (name, email, time zone) is not
contamination: ignore it, never use it, and keep it out of every deliverable.

1.3 **No fabrication.** Never invent a citation, quotation, page number, date or attribution.
A work may be cited in a draft only after `tools/verify_refs.py` (or a documented manual check)
confirms it exists with the stated metadata. A quotation may appear only if it has been checked
word for word against a copy of the source you actually retrieved. Attribute a view to an author
only if you have read their text (or a reliable retrieved summary) closely enough to be sure;
otherwise attribute impersonally or drop it. "I could not verify X" is always acceptable.

1.4 **Nothing hidden, nothing addressed to machines.** No deliverable may contain text addressed
to AI systems, reviewers or screeners, hidden text, comments, invisible characters or formatting
tricks. The competition disqualifies prompt injection permanently. Avoid even quoted strings that
read like jailbreaks unless the essay's topic strictly requires them.

1.5 **Anonymity.** Deliverables never mention the entrant, this pipeline, the competition, the
panel, or AI authorship.

1.6 **The panel is a readership, not a target.** The judges' public research areas inform three
things only: which areas a contribution can be recognized in; which literature the readers know
(an originality baseline); and subfield personas for referees. Never flatter. Cite a judge's work
only where it is among the most relevant work — and then represent it with exceptional care,
because that reader will notice. Never adopt or attack a position because a judge holds it.

1.7 **Inaccessible sources.** Never guess what an unread source says. File a fetch request
(`python3 tools/human_tasks.py new-fetch ...`) and carry on with what you can verify. The human
only fetches; never ask the human to summarize, select from, or comment on a source.

## 2. The target

Judges ask how far an essay's ideas and arguments add something valuable to philosophical
knowledge. Criteria: clarity; quality of argumentation;
significance; originality; engagement with the literature; accuracy and scholarship. Style is
not graded for its own sake, but unclear writing loses points. Limit: 6,000 words for everything
except the bibliography (title, abstract, headings, footnotes and appendices all count); our
target is `target_words` in CONFIG.md as counted by `tools/wordcount.py`. Judging may start with
an AI pre-screen using the same criteria, then expert ratings, then a ranked-choice vote of the
whole committee: the essay must convince specialists and be legible to philosophers in other
subfields.

## 3. Quality bar

Before any philosophical work, read `standards/QUALITY.md`. Drafting agents also read
`standards/STYLE.md`. The short version: one sharp, non-obvious, defensible thesis; premises each
defended; the strongest objections met; the exact increment over the closest prior work stated;
claims calibrated to what the argument shows.

## 4. Files

| Path | What | Who writes |
|---|---|---|
| `CONFIG.md` | run parameters | human only |
| `state/STATUS.md` | progress, source of truth for resuming | orchestrator |
| `state/...` | all intermediate work | the agent named in its task |
| `state/bib/` and `state/candidates/<ID>/refs.json` | verified bibliographies | developer, citation-auditor |
| `requests/fetch/` | fetch requests | any agent, via `tools/human_tasks.py` |
| `inbox/sources/` | sources fetched by the human | human (read-only for agents) |
| `relay/` | optional packets to/from other AI models | orchestrator / human courier |
| `methodology/` | append-only logs | via `tools/log.py` |
| `final/` | deliverables | orchestrator, methodologist |

Write only the outputs your task names. Never overwrite another agent's output; write a new
version. Record notable events with `python3 tools/log.py agent "<what, where>"`.

## 5. Tools

`tools/wordcount.py` (competition word count) · `tools/verify_refs.py` (Crossref/OpenAlex
reference check) · `tools/check_injection.py` (hidden text, machine-addressed text, identity leaks)
· `tools/rank.py` (Bradley–Terry ranking from pairwise judgments) · `tools/human_tasks.py`
(fetch requests, relay packets, gates → `HUMAN_TODO.md`) · `tools/log.py` (methodology log) ·
`tools/split_cards.py` · `tools/packets.py` (blind referee packets) · `tools/clock.py` (deadline
arithmetic) · `tools/usage_report.py` · `tools/export_transcripts.py` · `tools/build_pdf.py`. Python packages: z3-solver, sympy, requests, pypdf (installed in Phase 0).

Open-access routes worth trying before filing a fetch request: PhilArchive (philarchive.org),
author homepages, the Stanford Encyclopedia of Philosophy, arXiv, PhilSci-Archive, Crossref and
OpenAlex records (abstracts, open-access links), publisher pages (abstracts). Some sites block
automated access (PhilPapers often returns 403) — that is what fetch requests are for.

## 6. Orchestrator continuity

If you are the orchestrator (started by `/elenchus`) and your conversation has just been compacted
or resumed, re-read `.claude/skills/elenchus/SKILL.md`, the current phase's section of
`.claude/skills/elenchus/PHASES.md`, and `state/STATUS.md` before doing anything else.

## 7. Conduct

Work from sources, not memory, for anything about the literature. Prefer primary texts and
peer-reviewed work; use the SEP for orientation; flag weak sources. Say plainly what you could not
check. End every subagent task with a summary of at most 150 words plus the paths you wrote —
the orchestrator's context is precious.
