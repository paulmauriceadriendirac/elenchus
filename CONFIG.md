# Run configuration

Edit the values after the colons. Agents read this file; they never edit it.
Defaults are quality-first: cost is not the constraint, time to the deadline is.

```
mode: checkpoints
# autonomous  = decision gates (A, A2, B) take their defaults without pausing; fetch gates still
#               follow fetch_mode below.
# checkpoints = also pause at Gate A (which candidates get full drafts), Gate A2 (which draft to
#               finish) and Gate B (optional generic feedback).

fetch_mode: ask
# ask   = pause and ask the human to fetch high-priority sources the agents cannot reach
# queue = never pause for fetches; list them in HUMAN_TODO.md; use whatever arrives
# off   = never ask

max_parallel: 6               # subagents running at once (lower it if you hit rate limits)
lanes_to_map: 6               # research areas mapped in depth
candidates_per_lane: 10       # ideas generated per lane
wildcard_candidates: 10       # ideas from an ideator not tied to any lane
evolution_rounds: 1           # extra ideation generations informed by why earlier candidates died
gauntlet_size: 16             # candidates sent through prior-art search, formal check and red team
repair_rounds: 2              # repair attempts for candidates the red team says are fixable
full_drafts: 3                # complete essays written in parallel and compared before choosing
finish_essays: 1              # essays taken through revision + integrity + packaging (1-3)
referees_per_round: 5         # blind referees per review round
review_rounds: 4              # max revision rounds per finished essay (stops early on plateau)
target_words: 5600            # pipeline target by tools/wordcount.py (hard limit 6000)
deadline: 2026-10-31T23:59-12:00
package_by_hours_before_deadline: 36

topic: none
# Optional. A topic, question, debate, text or tradition (allowed by the rules), written as
# a name ("<a debate>", "<an author's book>", "<a tradition>"). NOT a thesis or an argument of
# your own. The orchestrator checks this against standards/HUMAN_INPUT_POLICY.md.

avoid: none
# Optional. Areas to stay out of (e.g. topics your other entries cover), comma-separated.

cross_model_relay: off
# on = the orchestrator writes self-contained packets in relay/outbox/ for another AI model
# (e.g. an extra blind referee per round). You paste them into the other model and paste its
# reply back, unedited, into relay/inbox/. Replies are treated as AI referee reports.

redact: paulmauriceadriendirac
# Comma-separated strings to strip from exported transcripts and to flag if they appear in
# deliverables. Pre-filled with your GitHub username; ADD your name, other handles, and email.
# Example: Jane Doe, janedoe, jane@example.com. Never copied into the methodology report.
```
