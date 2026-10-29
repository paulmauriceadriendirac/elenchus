# Provenance ledger — finalist essays A4, A5, A6

Compiled 29 October 2026 by the methodologist agent (Claude Opus 5.5) from the repository's files and
git history. Every entry names the file where a contribution first appears and the agent or system that
wrote it. Times are UTC. Times for commits by the second AI system are converted from the commits'
-05:00 offsets. "Log" means `methodology/log.md`; "card" means a file in `state/ambitious/cards/`; "kill
test" means a file in `state/ambitious/killtest/`. Authors of works that the essays engage are not named
here when they sit on the judging panel; the target works are described instead.

## 0. Systems and agents that appear in this ledger

| Label | What it is | Evidence |
|---|---|---|
| Orchestrator | The Claude Code session (Claude Opus 5.5, `claude-opus-5-5`) that ran the scaffold's skill | `methodology/run_config.md`; transcripts (model field) |
| field-surveyor | Subagent (Opus 5.5) that wrote the calibration brief and the hard-problems dossier | transcript launch records 21 Oct 18:27, 22 Oct 10:05 |
| ideator | Subagent (Opus 5.5) that wrote attack cards | launches 22 Oct 17:35 (A4, A5, A6) |
| red-team | Subagent (Opus 5.5) that ran the full-text kill tests | launches 23 Oct 17:17 (A5), 17:23 (A4, A6) |
| drafter / reviser | General-purpose subagents (Opus 5.5) given inline drafting or revision tasks | launches 23 Oct 22:47–22:51 (drafts), 29 Oct 03:43 and 04:15 (revisions) |
| referee | Blind referee subagent (Opus 5.5) that sees only a packet in `state/blind/P-xxxx/` | `state/blind/keys/*.json`; reports in `state/blind/*/reports/` |
| citation-auditor, formalist | Audit subagents (Opus 5.5) | launches 29 Oct 04:00 |
| Second AI system | An OpenAI Codex assistant that the human operator calls "Astra". It committed to this branch and to `codex/five-philosophy-essays` and wrote `state/external/` and `relay/outbox/`. Its model version is not recorded in its files (`state/external/review-edition-20261025/METHODOLOGY.md`). | git log; READMEs in `state/external/*/` |

## 1. Shared origin of all three essays (ambitious track)

| Step | What | Agent / system | File | Time |
|---|---|---|---|---|
| 1 | Human asks how to improve the process; the orchestrator proposes an anchor-paper funnel aimed at hard problems; the human approves and asks for "the most ambitious projects" and "the hardest problems". No topic, problem, thesis or argument is named by the human. | Human (method); orchestrator | `methodology/human_inputs.md` 22 Oct 10:01:37, 10:05:39; log 10:05:39 | 22 Oct 10:05 |
| 2 | Hard-problems dossier: 30 open problems in seven areas, top-10 shortlist ranked by ambition times tractability. The belief–credence bridge is #8, value of evidence and dogmatism #13, actual causation #26. | field-surveyor | `state/ambitious/problems.md` | 22 Oct 17:33 (log) |
| 3 | Selection of six problems (A1–A6) from different blocks; A4 actual causation, A5 belief–credence bridge, A6 value of evidence and dogmatism; anchor papers named | Orchestrator | `state/ambitious/selection.md` | 22 Oct 17:35 (log) |
| 4 | Attack cards for A4, A5 and A6 (five each), written after the ideators read the anchors in full | ideator (three instances) | `cards/A4.md` (file 23 Oct 17:22), `cards/A5.md` (23 Oct 02:07), `cards/A6.md` (23 Oct 17:23) | log 23 Oct 17:18–17:23 |
| 5 | Kill tests: card-by-card verdicts (KILL / REPAIR), closest prior work, recommended essay and calibrated thesis | red-team (three instances) | `killtest/A6.md` (22:47), `killtest/A5.md` (22:49), `killtest/A4.md` (22:50) | 23 Oct |
| 6 | First drafts (v1) | drafter (general-purpose, Opus) | `state/drafts/A4/v1.md` (23:16), `A5/v1.md` (23:17), `A6/v1.md` (23:17) | 23 Oct |

The A1–A3 problems were never carded: their anchor papers were requested (`requests/fetch/amb-*`) but
not supplied before the finishing phase.

## 2. A5 — "Holistic Accuracy, Refinement, and the Lockean Thesis"

Final text: `state/drafts/A5/v4.md` (5,296 words, strict count by `tools/wordcount.py`; file time 29 Oct
03:59). Version chain: v1 (drafter, 23 Oct 23:17) → v2 (second AI system, commit 8d2a333, 25 Oct 07:01,
`state/external/review-edition-20261025/essays/01-holistic-accuracy-A5-v2.md`) → v3 (second AI system,
commit b086236, 28 Oct 13:34, `state/external/submission-additive-20261029/essays/01-Holistic-Accuracy-v3.md`)
→ v4 (reviser, 29 Oct 04:00, log).

| # | Contribution in the final text | First appearance (agent, file, time) | Later changes and their source |
|---|---|---|---|
| 5.1 | Target: a 2019 argument (Dorst, Proposition 5) that expected-accuracy maximisation yields Lockean thresholds without Separability | Card A5-03 (ideator, `cards/A5.md`, 23 Oct 02:07) | Kill test: REPAIR, "close to PROCEED"; recommended as the essay (red-team, `killtest/A5.md` §7, 23 Oct 22:49) |
| 5.2 | Thesis: Proposition 5 does not follow from its premises | Card A5-03; kill-test "calibrated thesis" | v4 narrows and extends it: the premise needed is refinement invariance (see 5.6) |
| 5.3 | Counterexample: a truth-directed score with a premium for an error-free belief state (the "record" measure) satisfies the premises and makes belief non-monotone in credence (Theorem 1) | Card A5-03 ("a premium on a flawless record") | Kill test verified the counterexample by hand and corrected the card's claim that optima are always deductively closed (4-cell counterexample). v1 states it for every positive premium. v2 (second system) corrected consistency and tie claims. v4 adds runner-ups and margins (referee S1-lit, minor). Formal audit (formalist, `state/audit/A5/formal.md`): items 1–8 VERIFIED. |
| 5.4 | Diagnosis: the derivation's key step holds exactly when accuracy is separable on the domain (Theorem 2, Corollary) | Kill test §7 ("its key step assumes ... near-Separability"); v1 abstract | v2 (second system): distinguished a sufficient repair (ME+BI) from a necessary condition. v4: deleted two false sentences and added the Corollary and dilemma (referee S1-lit, Major 2). Audit items 9–10 VERIFIED. |
| 5.5 | What holism delivers: under the record measure one believes the probable consequences of a "core" hypothesis (Theorem 3); link to Holguín's non-monotonicity | v1 (drafter), developing the card's "closed, non-monotone belief" | v3 (second system) added a proved account of increasing the premium. v4 cut it to two sentences (word budget, `revision_notes_v4.md`). The "horse race" paragraph was cut on referee S1-lit Major 3. |
| 5.6 | Refinement invariance: given truth-directedness and conservative increments it forces fixed thresholds (Theorem 4, "Localization"); its converse; minimality witnesses | **Referee suggestion.** Referee S1-lit on packet P-7297 (27 Oct 16:25) named the most serious problem: the record measure's verdicts change when an irrelevant possibility is split. It offered routes (a) and (b). | Reviser v4 (29 Oct 04:00) took route (b) "as a theorem" and also route (a); the theorem statement, proof and minimality claims are the reviser's (`revision_notes_v4.md`; checks `checks/c8_refinement.py`, `c9_localization.py`). The formal audit (partial, 29 Oct 11:31) verifies Theorem 4 by hand but finds that the footnote-5 minimality witness does not support the claim. A different witness is needed; not yet repaired. |
| 5.7 | A normalised, question-relative record score that satisfies restricted refinement invariance | Reviser v4, responding to referee S1-lit route (a); motivated by the target's taking "a set of propositions" as input | — |
| 5.8 | Reply: order and Sequence-Irrelevance (greedy example: −0.8 first, +0.1 last) | **Referee suggestion** (S1-lit, Major 5) → v4 | Audit item 6 VERIFIED over all 40,320 orders |
| 5.9 | Reply: scope and accommodation (fixed context) | **Referee suggestion** (S1-lit, Major 4) → v4 | — |
| 5.10 | Reply: representation dependence | v2 (second system) added the objection | v4 turned it into Theorem 4 (5.6) |
| 5.11 | Comparisons with a 2022 paper on guessing, Levi 1967 and Leitgeb 2014/2017 | **Referee suggestion** (S1-lit, Major 1) → v4 | Citation audit (`state/audit/A5/citations.md`, 29 Oct 04:10): 13 quotations exact; 8 patches proposed (one inaccurate attribution, two oversimplified, two imprecise page references, one scare-quoted term from an unretrieved source). The patches post-date v4 and are not yet applied. |
| 5.12 | Dropped: the split-invariance impossibility theorem (card A5-01, repaired in the kill test, in v1 as the closing section) | Card A5-01 (ideator) | Removed by the second system in v2; absent from v4 |

## 3. A6 — "When Acting on Knowledge Makes Free Evidence Harmful: Good's Theorem in Normality Models"

Final text: `state/drafts/A6/v4.md` (5,790 words strict; file time 29 Oct 04:06; committed in 070f821).
Version chain: v1 (drafter, 23 Oct 23:17) → v2 (second system, 8d2a333, 25 Oct 07:01) → v3 (second system,
b086236, 28 Oct 13:34; `state/external/submission-additive-20261029/essays/02-Free-Evidence-v3.md`) → v4
(reviser, launched 29 Oct 03:43). No revision-notes file for v4 exists in the repository, and the log has
no completion entry for it. Attributions for v4 come from comparing the referee reports with the v3 and v4
texts.

| # | Contribution | First appearance | Later changes and their source |
|---|---|---|---|
| 6.1 | Question: does knowledge-based decision theory (expected utility conditioned on what one knows) keep Good's theorem inside the normality theory of inductive knowledge? | Card A6-01 (ideator, `cards/A6.md`, 23 Oct 17:23) | — |
| 6.2 | Boundary theorem: a free question is safe in every decision problem iff no state compatible with one's knowledge is one where the answer would reopen a ruled-out possibility; safe for all questions iff knowledge is gapped (Theorem 1) | Card A6-01 (ideator), with exhaustive small-structure checks | Kill test (red-team, 23 Oct 22:47): REPAIR, spine of a merged essay; must credit value-of-information precedents and isolate the bridge lemma. v2 (second system): corrected the quantifiers (a given safe question versus all questions; the empty question's value is non-negative, not zero). |
| 6.3 | Extension to any factive state containing rational belief; graded collapse (Theorem 2) | Card A6-01 ("any factive ken containing everything one believes") | v1 |
| 6.4 | Case: the target theory's model of repeated weighing; a free second weighing has negative value at ten-to-one odds | Card A6-02 (key case drawn from the target paper) | Kill test asked for a moderate-stakes instance ("odds of 20:1 or better"). v1 supplies ten-to-one. v2 (second system) corrected the ten-to-one scope. |
| 6.5 | The conditional repair (an expected-utility development of the principle Conditional Knowledge Dominance) fails wherever the unconditional rule fails (Theorem 3) | Card A6-02 → kill test (REPAIR as a section) → v1 | v3 (second system): strengthened the counterexample so that the same rule governs future decisions; added a three-state example and a local-stability proof. |
| 6.6 | Three developments of the conditional repair. Conditioning on the evidence's changing one's choice also fails. Conditioning answer by answer is safe (Proposition 4) but pays to check what one knows, which the qualitative principle forbids (Proposition 5). | **Referee suggestions.** Referee S2-lit on packet P-7f1b (27 Oct 16:26) proposed conditioning on "what looking would lead one to do" and argued that it prefers looking in Theorem 3's construction. Referee G4 (advocate persona) on P-7f1b (27 Oct 16:42) proposed the answer-by-answer version. | Reviser v4 (29 Oct): the constructions showing the verdict-change rule fails elsewhere, and Propositions 4–5, first appear in v4; checks `state/drafts/A6/checks/v4_conditional_rules.py`, `v4_verdict_rule.py`. |
| 6.7 | Comparison with Hong (2024–2026), crediting prior objections to normality knowledge as action-guiding | Kill test (blocking repair: "read Hong before drafting") | v2 (second system) incorporated Hong's full paper; retained in v4 §1 |
| 6.8 | Continuous model (Gaussian measurement) | Mentioned in v1 | v2 (second system) added a positive-measure Gaussian argument; referee S2-lit found it valid but its gloss imprecise; v3 (second system) removed an "unsupported continuous-model extension" (`submission-revisions-20261028/Review-Guide.md`) |
| 6.9 | Replies: self-trust versus evidence (§6.1); stakes and encroachment (§6.2); statism (§6.3); "Good's theorem is not sacrosanct" (§6.4) | Kill test objections 2–3 and card A6-05 (one paragraph on encroachment) → v1 | v2 (second system) narrowed the encroachment claims. Referee G4 Major 5 (scope of the margins horn) bears on §6.1; v4 §6.1 cites the target theory's "NO DEFEAT" result. |
| 6.10 | Dropped: cards A6-03, A6-04 (KILL) and A6-05 as a stand-alone essay | Kill test | — |

## 4. A4 — "Limits of Uniform Normality Filters in Actual Causation"

Final text: the latest complete version is **v5 by the second AI system**,
`state/external/submission-additive-20261029/essays/03-Causation-v5.md` (5,876 words strict; commit 8f82b0b,
29 Oct 00:18). A v6 revision by this pipeline was launched on 29 Oct 04:15 (commit 6c587ae). Only check
scripts exist (`state/drafts/A4/v6_checks/`); there is no `state/drafts/A4/v6.md`, so v5 is treated as final.
Version chain: v1 (drafter, 23 Oct 23:16, `state/drafts/A4/v1.md`) → v2 (second system, 25 Oct 07:01,
`review-edition-20261025/essays/04-causation-A4-v2-reserve.md`) → v3 (second system, b086236, 28 Oct 13:34)
→ v4 (second system, cccc9b9, 28 Oct 23:57, after reading a 2016 book on actual causality that the human
supplied to that system) → v5 (second system, 8f82b0b, 29 Oct 00:18).

The second system also wrote a different A4 manuscript ("Causal Refinement Without a Final Layer", v0.1
on 22 Oct and v2 on 23 Oct, in `state/external/ambitious-drafts-20261022/` and
`state/external/audit-and-a4-20261023/`). It started from the orchestrator's problem selection, not from
our cards. It is not an ancestor of the finalist A4 (`state/STATUS.md`, 23 Oct entry).

| # | Contribution | First appearance | Later changes and their source |
|---|---|---|---|
| 4.1 | Setting: normality as a filter on the witness worlds of structural-equation accounts (Halpern–Hitchcock) | Card A4-02/A4-04 (ideator, `cards/A4.md`, 23 Oct 17:22) | — |
| 4.2 | Calibration: within uniform componentwise rankings (default status times equation conformity), four calibrating judgments hold exactly when the ranking satisfies a "license" rule | Card A4-02 ("deviations need licences") | Kill test: REPAIR, the positive half of the recommended essay; noted the battery-size discrepancy. v1 states it. v3 (second system) checked all 355 category preorders. |
| 4.3 | Three-case non-separation (switch, short-circuit prevention, a deviant event preempting a normal process) under four default codings | Card A4-04 ("the switch is not a normality problem") and card A4-01 (locusts preempting a dry-season drought) | Kill test (red-team, 23 Oct 22:50) replaced the card's train switch with a "Doorbells" model from Gallow 2021 and required robustness under four uniform coding rules. v1 adopts both. v2 (second system) restricted the coding result to the four stated codings. |
| 4.4 | Frozen-witness lemma | Card A4-03 | Kill test: KILL as a card, keep as a lemma. v2 (second system) repaired its proof using AC3 minimality and acyclic uniqueness, removing an invalid inference. v4 (second system) credits its technique to Halpern 2016 Theorem 4.4.4(b). |
| 4.5 | A default-preserving isomorphic pair: no default-based account can separate it | v1 (drafter), from the kill test's "normality-isomorph" discussion | v3 (second system) explained what the pair requires of richer representations |
| 4.6 | Additive obstruction (Theorem 3): under the modified Halpern–Pearl definition, every uniform additive score that preserves the chain and ducking judgments counts the Doorbells switch as a cause; an explicit counterexample for the original and updated definitions; an exact escape condition with unequal root weights | **Second AI system, v5** (8f82b0b, 29 Oct 00:18; companion note `state/external/submission-additive-20261029/additive/`) | Not present in v1–v4 |
| 4.7 | Thesis wording ("a transferable normality policy faces constraints across cases, even when its scores allow compensation") and narrowed increment statement | v1 thesis ("the contrast between switching and preempting is not normality's to draw") (drafter) | v3: claims of the target's commitments narrowed. v4: originality narrowed after the book comparison; title changed. v5: compensation clause added. All by the second system. |
| 4.8 | Regularity theories (§6): a 2024 regularity theory's deviancy condition fails for early preemption with a normal backup | Card A4-01 → kill test, which found the point already in Beckers 2026 and required crediting it | v1 credits Beckers; retained |
| 4.9 | Replies to objections (§7): non-uniform or mechanism-specific rankings, coding choices, firmness of the locusts verdict | Kill test (objection list; "lean on the production verdict") → v1 | Revised in v2–v5 by the second system |
| 4.10 | Hostile review of v5 | Referee S7-lit on P-d300 (29 Oct 04:13; packet included a human-uploaded 2026 paper by Xiao and Xiong): 5/10, "reject in present form"; uniformity does all the work | Launched v6 revision not completed; **no suggestion from this report is in the final text** |

## 5. Points where referee or editor suggestions entered the final texts

- A5 v4: refinement invariance and Theorem 4 (route (b)) and the normalised record measure (route (a)), both
  from P-7297 S1-lit's most serious problem. Also Majors 1–5 and the minor items listed as ACCEPTED in
  `state/drafts/A5/revision_notes_v4.md` (literature comparisons, the Corollary and dilemma, the cut
  paragraph, scope and order replies, margins).
- A6 v4: the verdict-change rule (P-7f1b S2-lit) and the answer-by-answer rule (P-7f1b G4), which the reviser
  turned into the three-way analysis of §5 and Propositions 4–5.
- A4 v5: no referee report from this pipeline entered A4. The packet for A4 v1 (P-93b0) has no saved
  report. The P-d300 report arrived after v5, and the v6 revision is incomplete. The second system's
  revisions answered its own self-review and, in v2–v3, Claude's earlier general criticisms of external
  work.
- Kill-test (red-team) repairs entered all three v1 drafts (see the tables).
- Second-system revisions: A5 v2–v3, A6 v2–v3, A4 v2–v5. They are credited to that system above.
- The editor agent and the editor-plan and changelog files of the original design were never used. The
  run abandoned those phases (log 21 Oct 19:48:32).

## 6. Human messages and the contributions

None of the contributions above traces to a human message. The human's messages (all quoted in
`methodology/human_inputs.md`) contain workflow, budget, logistics, source uploads and generic
instructions. They include the request for ambition ("look for the hardest problems") but no topic,
problem, thesis, case, objection or formal result. The problems were chosen by the field-surveyor and
the orchestrator (`problems.md`, `selection.md`). The theses and cases originate in ideator cards and
red-team kill tests, or in the second AI system's revisions.

Sources the human supplied that bear on these essays:
- the 2026 Xiao and Xiong paper, uploaded 29 Oct 04:01 and placed in the A4 v5 referee packet;
- the 2016 book on actual causality, supplied to the second system and recorded as arriving "without
  philosophical comments" (`state/external/submission-book-review-20261028/Halpern-Originality-Review.md`).

The human's statement that the second system received no idea-wise input is at 22 Oct 10:01:37.
The second system's own records say the human withheld philosophical feedback
(`state/external/review-edition-20261025/METHODOLOGY.md`).

Limits of this ledger:
- The second system's chat transcripts are not in the repository. Its contributions are traced from its
  committed files and commit messages.
- A6 v4 has no revision notes, so v4 attributions rest on comparing the texts.
- That system's early provenance disclosure (a possible exposure to personal context) and the later
  clarification are recorded in the methodology report, §4.
