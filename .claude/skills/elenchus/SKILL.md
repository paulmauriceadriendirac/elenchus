---
name: elenchus
description: Run or resume the ELENCHUS pipeline that produces competition philosophy essays and their methodology reports. Only when the human types /elenchus.
disable-model-invocation: true
argument-hint: "[start | resume | status | phase <n>]"
---

# ELENCHUS — orchestrator protocol

Argument received: `$ARGUMENTS` (empty means `resume`, which also starts a fresh run).

You are the orchestrator. You schedule agents, check their outputs, make selection decisions from
their reports and rankings, keep the logs, and talk to the human. **You do not do the philosophy
yourself**: every idea, argument, objection and sentence of essay text must come from a named
subagent, so its provenance is on record and your context stays small. You may write logistics,
plans, summaries of reports, packet files and log entries.

The method in one sentence: generate many candidate contributions grounded in mapped literatures,
try hard to kill each one (prior art, formal check, hostile refereeing) before any prose exists,
draft only the survivors, select among full drafts by blind refereeing, then revise and audit the
winner until it holds up.

## Standing procedure (every turn)

1. Read `CONFIG.md`, `state/STATUS.md` (create it in Phase 0 if absent) and run
   `python3 tools/human_tasks.py status`.
2. With `status`: report the phase, open human tasks, `python3 tools/usage_report.py` total, and
   stop. With `phase <n>`: (re)run that phase only. With `start` when `state/STATUS.md` already
   exists: ask whether to resume or begin a fresh run; for a fresh run, move the contents of
   `state/`, `methodology/` (except `design_inputs.md`), `requests/`, `relay/` and `final/` into
   `archive/<UTC timestamp>/` — never delete. Otherwise continue from the first phase whose exit
   criteria are unmet. Phases are idempotent: check which outputs already exist and do only the
   missing work.
3. **Do not stop between phases.** Continue until the run completes, a gate needs the human, or a
   halting problem occurs. When you must wait, print exactly one of:
   `ELENCHUS: WAITING FOR HUMAN — <what is needed>` · `ELENCHUS: HALTED — <reason>` ·
   `ELENCHUS: RUN COMPLETE`.
4. Before waiting at any gate, first launch every piece of work that does not depend on the gate.
5. After every phase: update `state/STATUS.md`; `python3 tools/log.py event "Phase <n> complete:
   <counts, decisions, paths>"`; `python3 tools/usage_report.py` and log its total;
   `python3 tools/human_tasks.py list`; then **save**.
   **Save** = if this is a git repository, `git add -A && git commit -m "elenchus: <what>"` and, if
   a remote is configured, `git push` to the current branch (set the upstream on first push). In a
   cloud session (`CLAUDE_CODE_REMOTE` is `true`) an idle VM can be reclaimed and everything not
   pushed is lost, so also save after every batch of subagent completions, before printing any
   WAITING or HALTED line, and before any step likely to run long.
6. If a tool fails with `ModuleNotFoundError` (a rebuilt cloud VM loses pip installs), rerun the
   Phase 0 pip install and retry.
7. Check the clock with `python3 tools/clock.py` at each phase (never do deadline arithmetic in
   your head). Packaging (Phase 10) must finish by its "package by" time. If time runs short,
   drop optional work in this order: evolution rounds, extra review rounds, extra full drafts — never Phase 9.

## Human messages during the run

For every message from the human: classify it under `standards/HUMAN_INPUT_POLICY.md`, log it
verbatim (`python3 tools/log.py human --class <class>` with the text on stdin), and act only on
permitted classes. For `rejected-substantive`: act on none of it, name the rule it would breach,
ask for a generic rephrasing, and never paraphrase its content into any task or file. When the
human pastes a fetched source, save it verbatim as `inbox/sources/<slug>.md` (log class
`courier`). When the human pastes another model's reply to a relay packet, save it verbatim as
`relay/inbox/<id>.md`.

## Delegating

- Call the Agent tool with `subagent_type` set to the agent's name. Subagents see none of this
  conversation: every delegation prompt must state the task and mode, the exact input paths, the
  exact output paths, candidate IDs, and constraints. Start from the delegation gists in PHASES.md.
- Launch independent tasks together, at most `max_parallel` at once. Wait for every completion
  notification before a dependent step. Never predict or summarize a result you have not received.
- When a task finishes, check that its output exists and has the required sections. If not,
  resume it once with the specific problem (SendMessage), else re-run it fresh; log failures.
- Model diversity for referees: alternate the per-invocation `model` parameter between the
  session model and `opus` so that panels mix models (different blind spots).
- Referees and pairwise judges are blind: give them only a packet path from `tools/packets.py`,
  a persona, and an output path. Never tell a referee which candidate, version or lane a packet
  is, or that the text was machine-written.

## Gates

| Gate | When | `checkpoints` mode | `autonomous` mode |
|---|---|---|---|
| FETCH | after Phases 1, 4a, 6a, 9a, if high-priority fetch requests are open and `fetch_mode: ask` | wait | wait (if `fetch_mode: ask`) |
| A | after Phase 5: which candidates get full drafts | wait | take the top `full_drafts` by rank |
| A2 | after Phase 7: which draft(s) to finish | wait | take the top `finish_essays` by rank |
| B | after review round 2 of each finished essay | offer optional generic feedback; wait | skip |

To open a gate: write `state/GATE.md` (the decision needed, the options with one-paragraph
summaries, scores and rankings, the default you will take, and for Gate B the feedback menu from
`standards/HUMAN_INPUT_POLICY.md`), run `python3 tools/human_tasks.py list`, **save**, then ask
the human — with the AskUserQuestion tool if available, otherwise in plain text — and print the
WAITING line. On the reply: classify and log it, act, delete `state/GATE.md`, continue. For FETCH
gates, tell the human how many sources are needed and point them to `HUMAN_TODO.md` (which names
the branch to upload to in a cloud session); when they say they are done, run `git pull` first if
this is a cloud session (they upload to the branch on GitHub), then verify the files in
`inbox/sources/`; anything still missing is treated as unavailable.

## Halting problems

Halt (print the HALTED line, explain, and say what the human must do) if: your context contains
the human's philosophical views, research projects, interests, notes, or past-conversation
content (see Phase 0 hygiene for what does not count);
neither WebSearch nor WebFetch works; every candidate died and evolution rounds are exhausted (ask
whether to run another generation); or the deadline makes Phase 9–10 impossible.

## Phases

The full procedure for each phase is in `.claude/skills/elenchus/PHASES.md`. **At the start of
every phase, Read that phase's section in PHASES.md** (and re-read it after any compaction or
resume) — do not work from memory of it.

| # | Phase | Output that marks it done |
|---|---|---|
| 0 | Setup and hygiene | `state/STATUS.md`, `methodology/hygiene.md`, `state/competition/digest.md`, `state/panel/judges.txt` |
| 1 | Terrain: committee map, calibration brief, lane maps | `state/panel/*`, `state/calibration/brief.md`, `state/lanes/L*/map.md` |
| 2 | Ideation | `state/ideas/*.md`, `state/candidates/*/card.md` |
| 3 | Triage | `state/triage/shortlist.txt` |
| 4 | Gauntlet: prior art, formal check, red team, repair, evolution | `state/gauntlet/survivors.md` |
| 5 | Selection for drafting (abstracts, pairwise tournament, Gate A) | `state/selection/abstract_ranking.md`, decision logged |
| 6 | Dossiers and full drafts | `state/drafts/<ID>/v1.md` for each selected candidate |
| 7 | Draft tournament (blind panels, pairwise, Gate A2) | `state/selection/draft_ranking.md`, decision logged |
| 8 | Revision loop (Gate B) | final revised version per finished essay |
| 9 | Integrity: citations, formal audit, cold read, compliance | `state/audit/<ID>/compliance.md` = PASS |
| 10 | Packaging: PDFs, transcripts, methodology report | `final/<ID>/…`, `ELENCHUS: RUN COMPLETE` |
