# ELENCHUS — phase procedures

Read the section for the phase you are starting. Agent names in **bold** are `subagent_type`
values; quoted text is the gist of the delegation prompt (always add exact paths and IDs).

## Phase 0 — Setup and hygiene

1. `python3 tools/clock.py`. Record the run start, package-by time and deadline (UTC) in
   `state/STATUS.md`.
2. **Hygiene.** Inspect your own context and configuration:
   - memory, profile or preference blocks, or past-conversation content not from this repository;
   - tools that read user memory, past chats, or the human's documents (never call them);
   - `~/.claude/CLAUDE.md` and `~/.claude/rules/` (user-level instructions).
   **Contamination** = anything conveying the human's philosophical views, research projects,
   interests, notes or arguments. **Not contamination** = account metadata Claude Code attaches
   (name, email, time zone) and formatting or workflow preferences: ignore it and keep it out of
   deliverables (`tools/check_injection.py` flags emails; `CONFIG.md` `redact` should list the
   human's name and usernames — remind the human if it says `none`).
   Write `methodology/hygiene.md` stating exactly what you checked and what you found, quoting
   nothing private. If contaminated → halt and say how to fix it (turn off memory for the account,
   remove the user-level file, start a fresh session).
3. **Environment.** `python3 --version`; install `z3-solver sympy requests pypdf pypandoc_binary
   typst` with pip (add `--break-system-packages` if pip refuses). Probe the network:
   `curl -s -o /dev/null -w "%{http_code}" "https://api.crossref.org/works?rows=1"`, one WebSearch,
   and one WebFetch of `https://plato.stanford.edu/`. If Crossref or WebFetch is blocked, log it and
   tell the human (cloud sessions: set the environment's network access to Full), then continue
   with whatever works.
4. **Competition digest.** WebFetch the competition page, the detailed rules and the FAQ (URLs in
   `standards/HUMAN_INPUT_POLICY.md`; the main page is
   https://www.zacharygoodsell.com/ai-philosophy-competition). Write `state/competition/digest.md`
   in your own words: format, word rule, AI-involvement rules, judging criteria and process, dates,
   and the panel exactly as listed (it may have grown). Write `state/panel/judges.txt`, one name
   per line.
5. **Records.** `methodology/run_config.md`: CONFIG.md as it stands but with the `redact` value
   replaced by `[withheld]` (it lists the entrant's identity), the model you are running as,
   `claude --version` if available, the date. Every reasoning agent inherits the session model:
   if you are not running as a Fable or Opus model, open a gate recommending `/model fable` (or
   `/model opus`) followed by `/elenchus resume`, and do not start Phase 1 until the human
   answers. If `CONFIG.md` sets `topic` or `avoid`, check them against the policy (a topic, question, debate, text, tradition or known position is fine; a
   thesis or argument of the human's own is not) and log the class; if it fails, open a gate.
   Confirm `methodology/design_inputs.md` exists (the human's instructions when commissioning
   this scaffold); do not edit it.

Exit: STATUS.md, hygiene.md, digest.md, judges.txt, run_config.md exist; no halting problem.

## Phase 1 — Terrain

1a. In parallel:
  - **panel-analyst** — "Build the committee map from state/competition/digest.md and
    state/panel/judges.txt. Outputs: state/panel/committee_map.md,
    state/panel/committee_bibliography.json, state/panel/lanes.md, state/panel/personas.md."
  - **field-surveyor** — "Build the calibration brief. Inputs: state/competition/digest.md.
    Output: state/calibration/brief.md (+ state/calibration/refs.json)."
1b. Choose `lanes_to_map` lanes from `state/panel/lanes.md`, adjusted by the brief (prefer lanes
   containing live, contested questions and kinds of contribution that win) and by CONFIG `topic`
   (if set, all lanes are sub-areas of it) and `avoid`. Keep at least two lanes outside the most
   crowded area the panel-analyst identifies. Write `state/lanes/index.md` (ID `L1…Ln`, title,
   one-paragraph scope, why chosen). Log the decision.
1c. In parallel, one **cartographer** per lane — "Map lane L<k>: <title and scope from
   state/lanes/index.md>. Inputs: state/panel/committee_map.md (committee literature for this
   lane), state/calibration/brief.md. Outputs: state/lanes/L<k>/map.md and
   state/lanes/L<k>/refs.json; file fetch requests for key sources you cannot read."
1d. FETCH gate. Afterwards, for lanes with newly fetched sources, run a cartographer in
   `update` mode — "Read the newly fetched sources listed in requests/fetch/ for lane L<k> (files
   in inbox/sources/) and write state/lanes/L<k>/map_addendum.md."

Exit: lanes index and one map per lane.

## Phase 2 — Ideation

In parallel:
- one **ideator** per lane — "Mode: lane. Lane L<k>. Inputs: state/lanes/L<k>/map.md (+ addendum),
  state/calibration/brief.md, standards/OPERATORS.md. Produce `candidates_per_lane` candidates
  numbered L<k>-C01… Output: state/ideas/L<k>.md."
- one **ideator** in wildcard mode — "Mode: wildcard. Inputs: state/panel/committee_map.md,
  state/calibration/brief.md, standards/OPERATORS.md (no lane maps). Produce `wildcard_candidates`
  candidates numbered W-C01… in any area the panel can judge, outside the lanes in
  state/lanes/index.md. Output: state/ideas/W.md."

Then `python3 tools/split_cards.py`. Exit: one card per candidate in `state/candidates/<ID>/card.md`.

## Phase 3 — Triage

**triage** — "Score every card in state/candidates/*/card.md. Inputs: the lane maps, the
calibration brief, state/panel/committee_map.md. Shortlist `gauntlet_size` with diversity
(no more than 4 per lane; at least 2 wildcards if any are viable). Outputs:
state/triage/scores.md, state/triage/shortlist.txt (one ID per line)."

## Phase 4 — Gauntlet

4a. **prior-art-hunter** for every shortlisted ID, in parallel batches — "Candidate <ID>:
   state/candidates/<ID>/card.md. Use the lane map and state/panel/committee_bibliography.json as
   starting points. Output: state/candidates/<ID>/prior_art.md."
4b. FETCH gate (the closest-work sources matter most for originality). Then, for each candidate
   with newly fetched sources, **prior-art-hunter** in `recheck` mode → `prior_art_v2.md`.
4c. Kill `KNOWN`. Keep `PARTIAL` only if the report says the residual increment is substantial
   (and record the narrowed thesis it proposes). Log each decision with its reason.
4d. For each survivor, in parallel: **formalist** — "Candidate <ID>. Inputs: card.md and the
   latest prior_art. Output: state/candidates/<ID>/formal/ (report.md + code)." and **red-team** —
   "Candidate <ID>. Inputs: card.md, latest prior_art. Output: state/candidates/<ID>/redteam_v1.md."
4e. Verdicts: formal INVALID with no repair, or red-team KILL → dead. REPAIR → **developer** in
   `repair` mode — "Candidate <ID>. Inputs: card, prior_art, formal/report.md, redteam_v<k>.md.
   Output: state/candidates/<ID>/repair_v<k>.md" — then a fresh **red-team** on the repair (and the
   formalist again if the formal core changed). At most `repair_rounds`. PROCEED → survivor.
4f. **triage** in `lessons` mode — "Read every prior-art, formal, red-team and repair report under
   state/candidates/ for this generation and the kill/keep decisions in methodology/log.md.
   Outputs: state/gauntlet/survivors.md and state/gauntlet/lessons.md."
4g. Evolution (`evolution_rounds` times): **ideator** in `evolve` mode for the two or three lanes
   with the best survivors plus one wildcard — "Inputs: the lane map, state/gauntlet/lessons.md,
   state/gauntlet/survivors.md. New candidates must differ from all existing cards; number from
   the next free ID. Output: state/ideas/<lane>-g<r>.md." Split cards; triage the new cards
   (shortlist up to half of `gauntlet_size`); run 4a–4e on them; merge survivors.

Exit: survivors listed; at least 2 survivors (else halt and ask about another generation).

## Phase 5 — Selection for drafting

5a. **developer** in `abstract` mode for each survivor, in parallel → `abstract.md` (≤900 words,
   written as the essay's extended abstract; no pipeline vocabulary, no IDs).
5b. Pairwise tournament: make one shuffled packet per judge with
   `python3 tools/packets.py pairwise --ids <all survivors> --pattern
   "state/candidates/{id}/abstract.md" --seed <judge no.>`. Run 4 **referee** agents as judges in
   `pairwise` mode (two personas from `state/panel/personas.md` covering the survivors' areas, one
   distant-subfield generalist, one "prize committee chair" generalist; alternate models). Each
   judge writes `reports/<judge>.jsonl` and `reports/<judge>.md` inside its own packet. Unblind
   each with `python3 tools/packets.py unblind --packet <P-id> --infile <packet>/reports/<judge>.jsonl
   --append state/selection/abstract_pairwise.jsonl --judge <judge label>`; then run
   `python3 tools/rank.py state/selection/abstract_pairwise.jsonl --md state/selection/abstract_ranking.md`.
5c. Gate A. Default: top `full_drafts` by Bradley–Terry, but never three from one lane if a
   comparably ranked alternative exists.

## Phase 6 — Development and drafting (per selected candidate, in parallel)

6a. **developer** in `dossier` mode → `state/candidates/<ID>/dossier.md` and
   `state/candidates/<ID>/refs.json`; it runs `tools/verify_refs.py` and files fetch requests.
   FETCH gate. Then, for each dossier whose requested sources arrived, resume its developer
   (SendMessage) or run it again in `dossier` mode with the instruction to incorporate
   `inbox/sources/<slugs>` and update the dossier and refs.
6b. **drafter** → `state/drafts/<ID>/v1.md`. Check `python3 tools/wordcount.py
   state/drafts/<ID>/v1.md --target <target_words>`; if over, send it back to the drafter once.

## Phase 7 — Draft tournament

7a. For each draft: `python3 tools/packets.py single --src state/drafts/<ID>/v1.md --tag <ID>@v1`;
   run `referees_per_round` **referee** agents in `report` mode on it, in parallel. Personas: (1) home
   subfield specialist, (2) adjacent subfield specialist, (3) advocate for the view the essay
   attacks or the strongest rival view, (4) distant-subfield generalist, (5) literature expert (in
   `report+lit` mode, with web tools, checks originality and attributions). Take personas from
   `state/panel/personas.md`, fitted to the draft's area (you may read the draft's abstract to fit
   them). Reports go to the packet's `reports/`; copy each to
   `state/drafts/<ID>/reviews/v1-<persona label>.md` (reviews are always named by the version they
   review).
7b. Pairwise among drafts: 3 generalist **referee** agents in `pairwise` mode on a packet of the full
   drafts (`--pattern "state/drafts/{id}/v1.md"`), unblind into
   `state/selection/draft_pairwise.jsonl`, rank to `state/selection/draft_ranking.md`.
7c. Combine: rank by Bradley–Terry; demote any draft for which two or more referees found a fatal
   problem. Gate A2. The unchosen drafts stay on disk, complete, with their reviews.

## Phase 8 — Revision loop (for each essay being finished)

Round r = 1 … `review_rounds`:
1. **editor** — "Essay <ID> version v<r>. Inputs: state/drafts/<ID>/v<r>.md, the reports
   state/drafts/<ID>/reviews/v<r>-*.md, relay replies in relay/inbox/ for it, the dossier,
   and (if present) state/drafts/<ID>/human_feedback_r<r>.md. Output:
   state/drafts/<ID>/plan_v<r>.md." If the editor declares the essay unsalvageable, switch to the
   next-ranked draft and tell the human.
2. **reviser** in `revise` mode → `state/drafts/<ID>/v<r+1>.md` and a changelog entry.
   Word count check.
3. New blind packet of v<r+1>; fresh **referee** agents (`referees_per_round`; always include the
   literature expert and at least two personas not used in the previous round); copy reports to
   `state/drafts/<ID>/reviews/v<r+1>-<persona label>.md`.
   If `cross_model_relay: on`, also write `relay/outbox/xref-<ID>-v<r+1>.md`: target model
   "any frontier model other than Claude"; the full text of `standards/REFEREE_RUBRIC.md`; the
   essay text; the instruction to write the report in the rubric's format. Collect the reply when
   it arrives (do not block on it).
4. Stop when: no referee reports a major problem and median OVERALL ≥ 8; or median OVERALL has not
   risen for two rounds; or the round limit is reached.
5. Gate B after round 2 (checkpoints mode): the human may read `v<r+1>.md` and give generic
   feedback. Save permitted feedback verbatim to `state/drafts/<ID>/human_feedback_r<r+1>.md`;
   the editor treats it as one more report.

## Phase 9 — Integrity (per finished essay; never skipped)

9a. In parallel: **citation-auditor** — "Essay state/drafts/<ID>/v<final>.md with
   state/candidates/<ID>/refs.json. Output: state/audit/<ID>/citations.md (+ patch list)." and
   **formalist** in `audit` mode — "Re-verify every formal claim in the essay against the code in
   state/candidates/<ID>/formal/; rerun everything. Output: state/audit/<ID>/formal.md." FETCH gate
   for anything the auditor could not verify.
9b. Cold read: `python3 tools/packets.py single --src <final version> --tag <ID>@cold
   --head-words 1000`; a fresh **referee** in `cold-read` mode on that packet →
   state/audit/<ID>/coldread.md. Then the **editor** (cold-read comparison) compares its account
   of thesis and contribution with the dossier → state/audit/<ID>/coldread_patches.md.
9c. **reviser** in `patch` mode applies the patch lists (no new content) → `v<final+1>.md`.
9d. **compliance-officer** → state/audit/<ID>/compliance.md: PASS or FAIL with reasons. On FAIL,
   patch and recheck (at most twice), then escalate to the human.

## Phase 10 — Packaging

1. `final/<ID>/essay.md` (the compliance-passed version) and
   `python3 tools/build_pdf.py final/<ID>/essay.md`. Look at the PDF (Read it) to confirm it
   renders: math, footnotes, headings.
2. Export transcripts: `python3 tools/export_transcripts.py --redact "<CONFIG redact list>"`.
   `python3 tools/usage_report.py --md methodology/usage.md`.
3. **methodologist** → `final/<ID>/methodology_report.md` (and `methodology/provenance.md`);
   build its PDF too.
4. **compliance-officer** in `report` mode on the methodology report (anonymity, privacy, accuracy
   of the human-involvement account).
5. Write `final/README.md` (what to upload where, open items, the human's remaining checklist:
   OpenReview upload, anonymized PDFs, keep the logs). Commit and push.
6. Print a summary: essay title(s), final word counts, final referee medians, paths, and
   `ELENCHUS: RUN COMPLETE`.
