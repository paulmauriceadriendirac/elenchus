# ELENCHUS status

- Run start: 2026-10-21 18:25 UTC
- Package by: 2026-10-30 23:59 UTC
- Deadline: 2026-11-01 11:59 UTC (31 Oct 23:59 AoE)
- Mode: checkpoints · fetch_mode: ask · topic: none · avoid: none

## Phases
- [x] Phase 0 — setup and hygiene (no contamination; Crossref, WebSearch, WebFetch OK)
- [~] Phase 1 — terrain: 1a done (committee map, calibration brief); 1b lanes L1–L6 chosen (state/lanes/index.md); 1c six cartographers running

## Notes
- Human declined to extend redact list (2026-10-21); keep identity out of deliverables regardless.

## Budget (set by human 2026-10-21 19:45 UTC)
- Total cap: $150 (tools/usage_report.py list-price estimate). Spent at decision: ~$58.
- Sonnet for mechanical roles (triage scoring, reference lookups, compliance, packaging); Opus for
  ideation, red team, drafting, referees.
- Reserve ~$35 for Phase 9 integrity + Phase 10 packaging (tool-dependent, cannot be handed off).
- Handoff threshold: when spend reaches ~$115, stop launching new agents and write self-contained
  handoff packets in relay/outbox/ for another AI model (human couriers, unedited replies to
  relay/inbox/).
- Optional work dropped in skill order: evolution rounds, extra review rounds, extra full drafts.

## Lean mode (human instruction, 2026-10-21 ~20:00 UTC)
- Budget $100. Full pipeline abandoned. Lanes mapped: L3, L5, L6 (L1, L2, L4 stopped unmapped).
- Three single-pass essays: E1 (L3), E2 (L5), E3 (L6) → state/drafts/E*/v1.md. After that the
  human takes them to other AI models for revision and does word count, hidden-text check, PDF
  and methodology report manually.

## Current deliverables (2026-10-21)
- E1 v2 — state/drafts/E1/v2.md (L3; revised against Goodman & Salow 2023 full text; core of v1 was prior art, thesis replaced)
- E2 v2 — state/drafts/E2/v2.md (L5; revised against Meehan & Zhang 2025 full text; core of v1 was prior art, thesis replaced)
- E3 v2 — state/drafts/E3/v2.md (L6; revised against Dorr & Mandelkern 2026 full text; core cases survived)
- Each has revision_notes.md (fidelity audit, prior-art findings, weakest points) and check.py.
- Next: human takes essays to other AI models for revision; human does word count, hidden-text check, PDF, methodology report.

## Second wave (2026-10-21 ~21:30 UTC)
- Web allowed again. Ideation on existing work: state/ideas/{L3,L5,L6,DT}.md → triage → draft top
  3 → referee → revise. Note: competition allows at most 3 submissions per entrant; extra essays
  are alternatives to choose among.
- E2 v4 in progress (engage Zendejas Medina 2024 and others). E1 v3 in progress.

## Cross-model exchange (2026-10-22)
- Astra (other AI) essays on branch codex/five-philosophy-essays; review in state/external/.
- Referee feedback posted: https://github.com/paulmauriceadriendirac/elenchus/issues/1
  The human relays Astra's replies. Provenance of Astra's inputs still to be recorded.
- Paused: four ideators (L3, L5, L6, DT) stopped at usage limit; resumable.

## Ambitious track (2026-10-22 10:05 UTC, human-approved)
1. Hard-problems dossier → state/ambitious/problems.md (running).
2. Pick ~6 problems from different areas (orchestrator; shown to human).
3. Per problem: anchor PDFs (human fetches), ~5 attack cards from an ideator reading anchors in full.
4. Full-text kill test per card (referee with anchors) → pairwise rank → draft top 3–4.
5. 3–4 referee/revise rounds per finalist (advocate, literature auditor, distant-subfield personas).
Fallback pool if the ambitious track yields nothing: E1 v3, E2 v4, E3 v3, Astra essays.

## Plan for this phase (human, 2026-10-23 01:55 UTC)
1. Finish three essays from the ambitious track: A4 (actual causation), A5 (belief–credence), A6
   (value of evidence / dogmatism). Cards → kill test → draft → hostile review rounds.
2. Review Astra's latest work (04 v2, 05 v2, A6 v0.2, A4 v0.1) → post to issue #1.
3. Human then uploads anchor PDFs for A1–A3 and brings other models' comments.
Provenance: Astra outputs quarantined from our pipeline (Astra reported an exposure concern).


## Provenance correction and external revision (23 October 2026)

The external audit in `PROVENANCE-CLARIFICATION.md` found no human philosophical contribution in the inspected project instructions. The previous quarantine entry records a workflow precaution prompted by Astra's disclosure, not a referee finding or a ruling of ineligibility. CLAUDE.md §1.2 now distinguishes neutral context from a relevant human-idea concern under the official FAQ; historical disclosures remain preserved. This correction does not certify the contents of all earlier sessions or waive the relevant-memory restriction.

External A4 v2 is in `state/external/audit-and-a4-20261023/`: a conditional finite-cover-path theorem, three relay examples, and independent finite checks. It revises the external causal-refinement manuscript, not our A4 normality cards. E2 v5 and O5 v3 remain in `state/external/revisions-20261023/`. These revisions await philosophical review; no new finalist decision is implied.


## Finishing plan (2026-10-27 16:00 UTC; package by 2026-10-30 23:59 UTC)
Finalists (per Astra's 26 Oct review edition, provisional): A5 v2 (holistic accuracy / Lockean),
A6 v2 (free evidence), E3 v4 (flattening). Reserves: A4 (ours v1; Astra's v2), E1 v3, E2 v4.
1. Final hostile review round (running): packets P-7297 (A5v2), P-7f1b (A6v2), P-600a (E3v4);
   specialist+lit and advocate per essay.
2. Final revision per essay (reviser, one pass).
3. Phase 9: citation audit, formal audit, compliance (word count, injection, anonymity).
4. Phase 10: PDFs; methodology report draft (methodologist), incl. multi-model provenance.
5. Gate A2: human confirms final three before packaging.
