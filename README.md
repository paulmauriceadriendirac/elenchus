# ELENCHUS

A Claude Code harness that produces essays for the AI Philosophy Competition (deadline
31 Oct 2026, 23:59 AoE) together with the methodology reports the rules require.

**The method:** map the literatures the judges know → generate many precise candidate
contributions at their frontiers → try hard to kill each one *before any prose exists* (adversarial
prior-art search, machine-checked formal verification, a hostile specialist red team, repair and
re-attack) → evolve a second generation from the failure patterns → draft the survivors in full →
pick by blind, persona-diverse, pairwise refereeing → revise against fresh blind panels → audit
every citation, quotation, attribution and formal claim → package with a provenance ledger that
traces every idea in the essay to the agent that originated it.

You are the courier and the selector, never a source of ideas. The harness enforces that on you.

---

## Do these first (today)

1. **Submission route.** OpenReview (preferred; registration can take up to two weeks without an
   institutional affiliation) or the competition's Google Form (judged identically; needs a Google
   sign-in). Never submit the same essay through both.
2. **Memory hygiene.** The rules say: if an AI's memory may hold philosophical ideas a human
   supplied, disable it or use a fresh session. For the account that runs this harness, turn off
   claude.ai memory ("Generate memory from chat history") for the duration, and do not keep
   philosophy in `~/.claude/CLAUDE.md`. The harness disables Claude Code's auto memory, blocks
   memory, past-chat and claude.ai-connector tools, and checks its own context in Phase 0
   (`methodology/hygiene.md`). It halts if it finds anything.
3. Read `methodology/design_inputs.md` — the record of how you commissioned this — and correct it
   if anything is wrong.

## Run it

Before either option, set `redact:` in `CONFIG.md` to your name, usernames and repo name.

**Session settings (both options).**
- `/model fable` — Claude Fable 5.1 if your plan has it, otherwise `/model opus`. Every reasoning
  agent inherits the session model, and the default may be Sonnet.
- `/effort high`. The agents that do the philosophy have their own effort pinned (max for ideation,
  red-teaming, formal checks, drafting, refereeing, editing; high for reading-heavy work), and an
  agent's own setting overrides the session's. The session effort only governs the orchestrator,
  which does bookkeeping. `max` there buys slower logistics, not better philosophy. Don't change
  it mid-run (it invalidates the prompt cache), and don't set `CLAUDE_CODE_EFFORT_LEVEL`, which
  would override every agent.
- Auto permission mode, so background agents aren't stalled by approval prompts.

**Option A — cloud session (claude.ai/code).**
1. Put this folder in a *private* GitHub repo (private because fetched papers will be committed to
   it). If you upload through GitHub's web page, the hidden `.claude/` folder must go too; macOS
   Finder hides it until you press Cmd+Shift+. — without it there is no orchestrator and no agents.
2. In the environment settings: **network access → Full** (the default "Trusted" level blocks
   PhilArchive, Crossref, the SEP and most of the literature, because web fetches go through the
   VM's allowlist). Optional setup script, so packages survive VM rebuilds:
   `pip install --break-system-packages z3-solver sympy requests pypdf pypandoc_binary typst || true`
3. Start a session on the repo, apply the session settings above, then `/elenchus start`.
4. Fetched files: `HUMAN_TODO.md` names the repo and branch. Upload to `inbox/sources/` on that
   branch (GitHub: switch branch → open the folder → *Add file → Upload files*), then tell the
   session "fetched". Or paste text into the chat.
5. The run commits and pushes after every batch of agents and before every pause, because an idle
   cloud VM can be reclaimed and anything unpushed would be lost. So closing the tab is safe; if a
   session dies, reopen it (or start a new one on its branch) and type `/elenchus resume`.

**Option B — local CLI.** Unrestricted network, and fetched PDFs just go in a folder. Run
`claude update` first (the blind referees rely on a recent Claude Code feature).

```bash
cd elenchus
git init && git add -A && git commit -m "elenchus scaffold"   # lets the run commit progress
claude
```
Apply the session settings, then `/elenchus start`. When Claude Code asks whether to trust this
folder, accept: until you do, it ignores the project's permission rules and settings (including
the memory and connector blocks).

**Keeping it going.** The orchestrator runs phase after phase and stops only with one of:
`ELENCHUS: WAITING FOR HUMAN`, `ELENCHUS: HALTED`, `ELENCHUS: RUN COMPLETE`. If it ever stops
without one of those (usage limit, crash, closed laptop), type `/elenchus resume` — every phase is
resumable from files on disk, so you can also resume from another account (`/login`) or a new
session. `/elenchus status` reports progress. For a long unattended stretch you can add:
```
/goal The orchestrator has printed "ELENCHUS: RUN COMPLETE", "ELENCHUS: HALTED" or "ELENCHUS: WAITING FOR HUMAN"
```

Expect roughly a day or two of wall-clock time with gates, depending on rate limits. Start as
soon as you can (Oct 24 at the latest) so there is room for a second run.

## What you do during the run

- **Fetch** what the agents cannot reach. `HUMAN_TODO.md` lists each source, why it is needed and
  where to try. Save it as `inbox/sources/<slug>.pdf` (or paste the text and name the slug). If you
  cannot get it, create `inbox/sources/<slug>.unavailable`. Fetch exactly what is asked; add no
  notes, highlights or extra papers of your own.
- **Gates** (in `checkpoints` mode): choose which candidates get full drafts (Gate A), which draft to
  finish (Gate A2), and optionally give generic feedback (Gate B). Choosing among outputs is
  explicitly allowed.
- **Feedback** must name a problem without saying why or how to fix it. The permitted menu is in
  `standards/HUMAN_INPUT_POLICY.md` ("This premise needs more support", "Check whether this idea
  already exists in the literature", …). Anything substantive is logged, refused and not acted on.
- **Relay** (optional, `cross_model_relay: on`): paste packets from `relay/outbox/` into another
  model and its replies, unedited, into `relay/inbox/`. They become extra referee reports.

## What you get

`final/<ID>/essay.md` and `.pdf`; `final/<ID>/methodology_report.md` and `.pdf`;
`methodology/` (run log, your inputs verbatim and classified, hygiene check, token usage and cost,
provenance ledger, exported transcripts); and in `state/` every intermediate artifact: the
committee map, lane maps, every candidate with its prior-art report, formal verification code,
red-team reports, all drafts and referee reports. Unchosen drafts remain complete, with reviews,
in case you want to finish a second essay.

Before submitting: read both documents; check the redaction (set `redact:` in CONFIG.md to your
name, usernames, repo name and email before the run ends); keep all logs (the organisers may ask
for them).

## Configure

Everything is in `CONFIG.md`: `mode`, `fetch_mode`, breadth of search (`lanes_to_map`,
`candidates_per_lane`, `gauntlet_size`, `full_drafts`, `evolution_rounds`, `review_rounds`),
`finish_essays` (1–3), `topic` (optional — a topic, question, debate, text or tradition, never a
thesis of your own), `avoid` (areas your other entries cover), `cross_model_relay`, `redact`.

## What is in the box

```
CLAUDE.md                     standing rules for every agent (integrity, anonymity, no fabrication)
CONFIG.md                     run parameters
.claude/skills/elenchus/      the orchestrator: SKILL.md (protocol, /elenchus) + PHASES.md (phase procedures)
.claude/agents/               16 agents: panel-analyst, field-surveyor, cartographer, ideator, triage,
                              prior-art-hunter, formalist, red-team, developer, drafter, referee,
                              editor, reviser, citation-auditor, compliance-officer, methodologist
.claude/settings.json         permissions; auto memory off; memory/past-chat/connector tools blocked
standards/                    QUALITY, STYLE, OPERATORS (generic moves), REFEREE_RUBRIC, HUMAN_INPUT_POLICY
tools/                        word count by the competition's rule; reference verification (Crossref,
                              OpenAlex); prompt-injection/anonymity scan; blind packets; Bradley–Terry
                              ranking; fetch/relay checklist; logging; deadline clock; token-cost
                              report; transcript export; Markdown→PDF
methodology/design_inputs.md  how the scaffold was commissioned (disclosure)
```

## Limits to know about

- Nothing guarantees a win. The harness raises the floor (no fabricated citations, no unchecked
  formal claims, no known idea presented as new without a fight) and searches widely for the
  ceiling; whether a current model produces a contribution that experts value is the open question
  the competition exists to test.
- Originality checks see open-access texts plus whatever you fetch. Paywalled or unpublished work
  can still contain an idea.
- LLM referees reward polish and confidence more than experts do. That is why selection leans on
  pairwise judgments, blind packets, mixed models, and objective filters (prior art, formal checks).
- `tools/usage_report.py` estimates cost at list prices from local transcripts; `/usage` is the
  authority.
