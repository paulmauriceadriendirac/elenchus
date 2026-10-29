# Provenance ledger — final essays A5, A6, A4

Compiled 29 October 2026 by the methodologist agent (Claude Opus 5.5) from the repository's files and
git history; this version replaces the 11:42 draft and describes the texts in `final/A5/essay.md`,
`final/A6/essay.md` and `final/A4/essay.md`. Every entry names the file where a contribution first
appears and the agent or system that wrote it. Times are UTC. Times of commits by the second AI system
are converted from their -05:00 offsets. "Log" means `methodology/log.md`; "card" means a file in
`state/ambitious/cards/`; "kill test" means a file in `state/ambitious/killtest/`. Authors of engaged
works who sit on the panel are not named here; their works are described or named by title.

## 0. Systems and agents in this ledger

| Label | What it is | Evidence |
|---|---|---|
| Orchestrator | The Claude Code session (Claude Opus 5.5, `claude-opus-5-5`) running the scaffold's skill | `methodology/run_config.md`; transcripts |
| field-surveyor | Subagent (Opus 5.5): calibration brief, hard-problems dossier | transcript launches 21 Oct 18:27, 22 Oct 10:05 |
| ideator | Subagent (Opus 5.5): attack cards | launches 22 Oct 17:35 |
| red-team | Subagent (Opus 5.5): full-text kill tests | launches 23 Oct 17:17 (A5), 17:23 (A4, A6) |
| drafter / reviser | General-purpose subagents (Opus 5.5) with inline drafting, revision or patch tasks | drafting launches 23 Oct 22:47–22:51; revisions launched 29 Oct 03:43 (A5, A6) and 04:15 (A4); patch passes later on 29 Oct (log 11:51, 17:40–17:43) |
| referee | Blind referee subagent (Opus 5.5) that sees only a packet in `state/blind/P-xxxx/` | `state/blind/keys/*.json`; reports in `state/blind/*/reports/` |
| citation-auditor, formalist, compliance-officer | Audit subagents (Opus 5.5) | `state/audit/*/` |
| Second AI system | An OpenAI Codex assistant that the human operator calls "Astra". It committed to the shared branch and wrote `state/external/`, `relay/outbox/codex-*.md` and `state/audit/A5/good-guesses-comparison-20261029.md`. Its model version is not recorded in its files. | git log; READMEs in `state/external/*/`; `state/external/review-edition-20261025/METHODOLOGY.md` |

## 1. Shared origin of all three essays (ambitious track)

| Step | What | Agent / system | File | Time |
|---|---|---|---|---|
| 1 | The human asks how to improve the process; the orchestrator proposes an anchor-paper funnel aimed at hard problems; the human approves and asks for "the most ambitious projects" and "the hardest problems". The human names no topic, problem, thesis or argument. | Human (method); orchestrator | `methodology/human_inputs.md` 22 Oct 10:01:37, 10:05:39; log 10:05:39 | 22 Oct 10:05 |
| 2 | Hard-problems dossier: 30 open problems in seven areas, top-10 shortlist (belief–credence bridge #8, value of evidence and dogmatism #13, actual causation #26) | field-surveyor | `state/ambitious/problems.md` | log 22 Oct 17:33 |
| 3 | Six problems selected (A1–A6) from different areas; anchor papers named | Orchestrator | `state/ambitious/selection.md` | log 22 Oct 17:35 |
| 4 | Five attack cards each for A4, A5, A6, written after reading the anchors in full | ideator (three instances) | `cards/A4.md` (file 23 Oct 17:22), `cards/A5.md` (23 Oct 02:07), `cards/A6.md` (23 Oct 17:23) | 23 Oct |
| 5 | Kill tests: KILL/REPAIR verdict per card, closest prior work, recommended essay and calibrated thesis | red-team (three instances) | `killtest/A6.md` (22:47), `killtest/A5.md` (22:49), `killtest/A4.md` (22:50) | 23 Oct |
| 6 | First drafts (v1) | drafter | `state/drafts/A4/v1.md` (23:16), `A5/v1.md` (23:17), `A6/v1.md` (23:17) | 23 Oct |
| 7 | Gate A2: the orchestrator recommended A5, A6, A4 (log 29 Oct 03:45:15); the human selected "A5, A6, A4 (Recommended)" | Orchestrator; human (selection among finished AI texts) | `human_inputs.md` 29 Oct 11:45:15; log 11:45:15 | 29 Oct |
| 8 | Convergence on the second system's source-checked versions as bases; this pipeline's audits applied on top | Orchestrator (decision); second system (bases); patch agents | log 29 Oct 17:34:53, 17:36:33 | 29 Oct |

## 2. A5 — "Holistic Accuracy and the Limits of Lockean Derivation"

Final text: `final/A5/essay.md`, 5,039 words (strict, `tools/wordcount.py`). Version chain:

| Version | Author | File | Time |
|---|---|---|---|
| v1 | drafter | `state/drafts/A5/v1.md` | 23 Oct 23:17 |
| v2 | second system | `state/external/review-edition-20261025/essays/01-holistic-accuracy-A5-v2.md` (commit 8d2a333) | 25 Oct 07:01 |
| v3 | second system | `state/external/submission-additive-20261029/essays/01-Holistic-Accuracy-v3.md` (b086236) | 28 Oct 13:34 |
| v4 | reviser, against referee report P-7297 S1-lit | `state/drafts/A5/v4.md`; notes `revision_notes_v4.md` | log 29 Oct 04:00 |
| v5 | patch agent: formal-audit P1–P5, P8 and citation-audit patches 1–8 applied | `state/drafts/A5/v5.md`; `changelog_v5.md` | log 29 Oct 11:51 |
| v6 | a narrowing pass launched 11:52 and stopped as a duplicate; the file is byte-identical to v5 | `state/drafts/A5/v6.md` | log 17:34:53 |
| v7 | second system, after its 29 Oct review and *Good Guesses* comparison | `state/external/submission-sourcechecked-20261029/A5-Holistic-Accuracy-v7.md` (89bd70f) | 29 Oct 17:02 |
| final | orchestrator: patches 1–3 of `state/audit/A5/citations_final.md` applied verbatim | `final/A5/essay.md`; `final/A5/changelog.md` | log 17:40:57 |

| # | Contribution in the final text | First appearance | Later changes and their source |
|---|---|---|---|
| 5.1 | Target: a 2019 argument (Dorst, Proposition 5) that expected-accuracy maximisation yields Lockean thresholds without Separability | Card A5-03 (ideator, 23 Oct 02:07) | Kill test: REPAIR, "close to PROCEED", recommended as the essay (red-team, `killtest/A5.md` §7) |
| 5.2 | Thesis: Proposition 5 does not follow on the unrestricted reading of holism; on a stronger reading the argument's values already restrict holism | Card A5-03 ("does not follow"); kill-test calibrated thesis | v4 (reviser) said the needed premise is refinement invariance. The second system's 29 Oct review (`state/external/claude-review-20261029/ASSESSMENT-485bec4.md`, required fix 1) judged that an overstatement. v7 (second system) recast the thesis as "two readings" and retitled the essay. |
| 5.3 | Counterexample: a truth-directed score with a premium for an error-free belief state; belief at credence 0.70 but not at 0.75, with values and context fixed (Theorem 1) | Card A5-03 ("a premium on a flawless record") | Kill test verified it by hand and corrected the card's closure claim. v2 (second system) corrected consistency and tie claims. v4 added runner-ups and margins (referee S1-lit, minor). Formal audit (formalist, `state/audit/A5/formal.md`, 11:41) reproduced every number; the second system's review recomputed all 256 belief states. |
| 5.4 | Bridge from optimisation to rationality: "Non-vacuity" (some state is permitted at each credence) replaces "Permission" | **Second-system review** (ASSESSMENT required fix 3: "Permission is not the minimal existence assumption") | Written into v7 by the second system (term absent from v5, present in v7) |
| 5.5 | Diagnosis: order independence does not justify the marginal-value restrictions; for a single measure, marginal extensionality plus background-independent thresholds recover separability (Theorem 2, Corollary) | Kill test §7 ("its key step assumes ... near-Separability"); v1 | v2 (second system) separated a sufficient repair from a necessary condition. v4: Corollary and dilemma (referee S1-lit, Major 2). v5: formal-audit P4 (BI read across the family). v7: the "stronger reading" framing (second system). |
| 5.6 | Core characterisation: the score's optima select a core and its above-threshold consequences (Theorem 3) | v1 (drafter), developing the card's "closed, non-monotone belief" | v3 (second system) added a premium-raising result; v4 cut it (word budget). Referee S1-lit Major 3 led to cutting the "horse race" paragraph. |
| 5.7 | Prior-work concession: an earlier utility theory of guessing (*Good Guesses*, 2022) already reproduces the two belief sets of the main example (with one fixed parameter, J = 125/64); the increment is narrowed to the realisation under strict marginal truth-directedness, the diagnosis, and the optimiser characterisation | **Second system**, `state/audit/A5/good-guesses-comparison-20261029.md` (commit 9c39291, 29 Oct 12:16), from a July 2021 penultimate author draft described as "supplied" | Written into v7. Final patch 2 (citation-auditor, `citations_final.md`) reworded the abstract to "An earlier utility theory of guessing already generates …"; patch 1 added the note that section numbers follow the 2021 draft. Earlier: referee S1-lit Major 1 had asked for comparisons with the guessing paper, Levi 1967 and Leitgeb 2014/2017 (added in v4). |
| 5.8 | Refinement invariance (RI) plus truth-directedness and conservative increments (CI) force fixed thresholds (Theorem 4); RI is one sufficient route, not a necessary premise; a separable family T = 1, F = −n has fixed-space thresholds n/(n+1) but violates RI | **Referee suggestion**: P-7297 S1-lit (27 Oct 16:25) named refinement dependence as the most serious problem and offered routes (a) and (b). The reviser's v4 proved Theorem 4 (route (b)). | Formal audit: theorem correct; the old footnote-5 witness was wrong (P1), and "no non-Lockean score can …" was false (P2); both fixed in v5. **Second-system review** (required fix 1) supplied the n/(n+1) family and the "sufficient, not necessary" reading, written into v7. Final patch 3 ("with uniform values") from `citations_final.md`. |
| 5.9 | Question-relative record measure (mean over the algebra) meets restricted refinement invariance | Reviser v4, answering referee S1-lit route (a) | Retained in v7 and final |
| 5.10 | Replies: premium is alethic; necessary-condition objection met by Non-vacuity; "negative only" reply; order and Sequence-Irrelevance; scope (fixed context) | Order and scope replies: **referee suggestions** (S1-lit, Majors 5 and 4) → v4. Non-vacuity reply: second system, v7. Premium reply: v1–v3. | The formal audit verified the order example over all 40,320 orders |
| 5.11 | Dropped: the split-invariance impossibility theorem (card A5-01) | Card A5-01 | Removed by the second system in v2 |

## 3. A6 — "When Acting on Knowledge Makes Free Evidence Harmful: Good's Theorem in Normality Models"

Final text: `final/A6/essay.md`, 5,831 words strict. Version chain:

| Version | Author | File | Time |
|---|---|---|---|
| v1 | drafter | `state/drafts/A6/v1.md` | 23 Oct 23:17 |
| v2 | second system | `review-edition-20261025/` (8d2a333) | 25 Oct 07:01 |
| v3 | second system | `submission-additive-20261029/essays/02-Free-Evidence-v3.md` (b086236) | 28 Oct 13:34 |
| v4 | reviser, against P-7f1b S2-lit and G4 | `state/drafts/A6/v4.md`; `revision_notes_v4.md` | launched 29 Oct 03:43; log 11:43:05 (5,883 words) |
| v5 | second system, after its 29 Oct review | `submission-sourcechecked-20261029/A6-Free-Evidence-v5.md` (89bd70f) | 29 Oct 17:02 |
| final | patch agents: citation-audit patches P1–P14d of `state/audit/A6/citations.md` (log 17:43:03), then formal-audit patches P1–P8 of `state/audit/A6/formal.md` (log 17:53:18); both audits were of v4 | `final/A6/essay.md`; `final/A6/changelog.md` | 29 Oct |

| # | Contribution | First appearance | Later changes and their source |
|---|---|---|---|
| 6.1 | Question: does knowledge-based decision theory keep Good's theorem inside the 2023 normality theory of inductive knowledge? | Card A6-01 (ideator, 23 Oct 17:23) | — |
| 6.2 | Boundary theorem: a free question is safe in every decision problem iff no state compatible with one's knowledge is one where the answer reopens a ruled-out possibility; all questions safe iff knowledge is gapped (Theorem 1) | Card A6-01, with exhaustive small-structure checks | Kill test: REPAIR, spine of a merged essay; credit value-of-information precedents. v2 (second system) corrected quantifiers. v4 (referee S2-lit M4): the theorem's shape credited to Geanakoplos. v5 (second system): connected to *Deference Done Better* (see 6.8). |
| 6.3 | Graded collapse: no factive state containing rational belief is safe unless it is the whole evidence (Theorem 2) | Card A6-01 | — |
| 6.4 | Case: the target theory's repeated-weighing model; a free second weighing has negative value at ten-to-one odds | Card A6-02 | Kill test asked for a moderate-stakes instance; v1 supplied ten-to-one; v2 corrected its scope; v4 separated three claims (referee S2-lit M2a). v5 (second system) distinguished about 42% weight-belief loss from about 37% loss with a consistent discovery; the discrepancy was first flagged in this pipeline's partial formal audit (`state/audit/A6/formal.md`, file 11:52). The record does not show whether the second system used that audit. Final citation patch P10 attributes "about 0.37" to the source's note 18; the completed formal audit (17:47) confirmed the distinction, and formal patch P2 corrected a §5.1 figure from −0.63 to −0.60. |
| 6.5 | Conditioning on the options' differing (CEU) fails wherever the unconditional rule fails (Theorem 3); Conditional Knowledge Dominance itself is silent in that construction | Card A6-02 → kill test → v1 | v3 (second system) strengthened the counterexample. v4 conceded the silence (**referee suggestion**, S2-lit MS(a)) and proved it generally (A.7). |
| 6.6 | Conditioning on the evidence's changing one's choice (VER) also fails, including a five-state counterexample | **Referee suggestions**: S2-lit (27 Oct 16:26) proposed the verdict-change rule; G4 (27 Oct 16:42) supplied the five-state counterexample, verified by the reviser | v4 added a failure without relative defeat. v5 (second system): s0 = s1 made explicit, the future policy specified, enumeration scope described (ASSESSMENT A6 fixes 3 and 5) |
| 6.7 | Conditioning answer by answer (ANS) is safe (Proposition 4) but pays to check what one knows, which Conditional Knowledge Dominance forbids (Proposition 5) | **Referee suggestion**: G4 proposed ANS and its safety proof, accepted as Proposition 4. Proposition 5 is the reviser's (v4). | v5 (second system): price condition 0 < κ < L made explicit (ASSESSMENT fix 4); conclusion restricted to the rules examined (fix 2) |
| 6.8 | Comparison with *Deference Done Better* (2021): its Value and Total Trust results; the normality model's increment is the relative-defeat/gappedness characterisation and the conditional repairs | **Second-system review** (ASSESSMENT required fix 1) | Written into v5 by the second system, which checked Value, Weak Value and Total Trust (`VERIFICATION.md`). This pipeline checked only the Crossref metadata (`final/A6/changelog.md`). |
| 6.9 | Comparison with Hong (2024–2026) | Kill test ("read Hong before drafting") | v2 (second system) drew on that system's reading of §§1–3. Final patch P4 narrowed the description to what that system's records support. **This pipeline has not read Hong's text** (Wiley 403; fetch `amb-a6-hong-2025-2026` open). |
| 6.10 | Replies: self-trust versus evidence; stakes and encroachment; statism and questions; "Good's theorem is not sacrosanct" | Kill test objections and card A6-05 → v1 | v2 narrowed encroachment; v4 added the encroachment literature (S2-lit) and the question-sensitivity limitation (S2-lit M5); final patches P11–P14d reworded attributions |
| 6.11 | Dropped: cards A6-03, A6-04 (KILL), A6-05 as a stand-alone essay | Kill test | — |

## 4. A4 — "A Switching Dilemma for Normality in Actual Causation"

Final text: `final/A4/essay.md`, 5,581 words strict. Version chain:

| Version | Author | File | Time |
|---|---|---|---|
| v1 | drafter | `state/drafts/A4/v1.md` | 23 Oct 23:16 |
| v2 | second system | `review-edition-20261025/essays/04-causation-A4-v2-reserve.md` | 25 Oct 07:01 |
| v3, v4, v5 | second system (v4 after reading a 2016 book on actual causality supplied by the human "without philosophical comments") | commits b086236, cccc9b9, 8f82b0b; `submission-additive-20261029/essays/03-Causation-v5.md` | 28 Oct 13:34; 23:57; 29 Oct 00:18 |
| v6 | reviser, against P-d300 S7-lit | `state/drafts/A4/v6.md`; `revision_notes_v6.md` | launched 29 Oct 04:15; log 11:44:20 (5,521 words) |
| v7 | second system, after its 29 Oct review | `submission-sourcechecked-20261029/A4-Causation-v7.md` (89bd70f) | 29 Oct 17:02 |
| final | patch agents: citation-audit patches 1–8 of `state/audit/A4/citations.md` (log 17:42:47; conditional H1–H5 skipped), then formal-audit patches P1–P7 of `state/audit/A4/formal.md` (log 17:49:40); both audits were of v6. Compliance PASS (log 17:53:36). | `final/A4/essay.md`; `final/A4/changelog.md`; `state/audit/A4/compliance.md` | 29 Oct |

The second system's separate manuscript "Causal Refinement Without a Final Layer" (22–23 Oct) started
from the orchestrator's problem selection, not from the cards, and is not an ancestor of A4.

| # | Contribution | First appearance | Later changes and their source |
|---|---|---|---|
| 4.1 | Setting: normality as a filter on witness worlds of the three Halpern–Pearl definitions; switches versus preemption | Cards A4-02, A4-04 (ideator, 23 Oct 17:22) | Retained |
| 4.2 | **Thesis**: no anonymous (transition-profile-only) normality filter that respects Pareto improvement keeps genuine prevention and late preemption while counting no switch a cause, under any of the three definitions; a separating filter needs information beyond the profile | **Referee suggestion**: P-d300 S7-lit (29 Oct 04:13) recommended "a reframed short paper on a cross-definition switching dilemma" and wrote that "the correct result is stronger: a dilemma across all three definitions" | Formulated and proved by the reviser in v6. v7 (second system) added "Within these codings" and "information beyond the transition profile", and removed v6's sentence calling anonymity "the natural target for a principled policy", which ASSESSMENT fix 4 had asked to be defended rather than stipulated. |
| 4.3 | Theorem 1 (modified definition): Suzy's only witness has exactly the profile of the witnesses for two standard switches | v6 (reviser) | Formal audit (`state/audit/A4/formal.md`, 17:44): verified by independent implementation |
| 4.4 | Theorem 2 (original and updated definitions): the both-blocked switch's witness is genuine prevention's plus one default-restoring change | v6 (reviser); the case is Schumacher's, reported by Halpern 2015, used by Xiao and Xiong (2026); the referee pointed to both | Verified by the formal audit; the Corollary also by exact SMT check over all anonymous Pareto filters on the occurring profiles |
| 4.5 | Calibration: exactly five of 355 componentwise preorders give the four calibrating verdicts | Card A4-02 (license rule); v3 (second system) enumerated 355 preorders; v6 restated | Formal audit: the five is VERIFIED; "two of them total orders" was **FALSE** (they are total preorders), corrected by formal patch P1 in the final text. |
| 4.6 | §5: pricing non-anonymous escapes; one additive repair based on mechanism reliability (c_BH > c_L holds only in that repair) | v6 (reviser) from the report's analysis | v7 (second system) restricted the frozen-mechanism argument to the additive repair it establishes (ASSESSMENT fix 1). Final patch 3 restored a hedge in a quotation from Xiao and Xiong; patch 4 corrected a gloss of a 2017 paper. |
| 4.7 | Frozen-witness Lemma; exceptionless equation-conformity leaves only root but-for causes in fixed-context acyclic models; applied to a 2015 conjecture and to Xiao and Xiong's definition | Card A4-03 (lemma) → kill test (keep as lemma) → v2 (second system repaired the proof via AC3 minimality) → v4 (credited technique to Halpern 2016) → v6 (conformity application, reviser) | v7 (second system) made the fixed-context conditions explicit (ASSESSMENT fix 3). Formal audit: Lemma holds on all 312 three-variable models and 1,500 random larger models. |
| 4.8 | Comparison with Wysocki 2023, "Conjoined cases", as stronger prior obstruction | **Second-system review** (ASSESSMENT required fix 2) | Written into v7. Content checked by the second system (`VERIFICATION.md`) and, independently, by this pipeline's compliance agent against the author-posted PDF (pp. 8, 10; `state/audit/A4/compliance.md` §5, log 17:53:36). |
| 4.9 | Doorbells switch model (from Gallow 2021) and coding robustness | Kill test (red-team, 23 Oct 22:50) | v2 restricted the coding claim; in v6 Doorbells carries Theorem 1 and coding is Objection 2. Final patch 2 corrected the description of Gallow's own model. |
| 4.10 | §7: parallel in regularity theory (Beckers 2026's dilemma for a 2024 regularity theory) | Card A4-01 → kill test, which found the point in Beckers 2026 | Recast as a parallel in v6; final patch 6 ("related shape"). The formal audit marks the §7 computations UNVERIFIED (author-computed only). |
| 4.11 | Additive-score obstruction | Second system, v5 (8f82b0b) | Subsumed by v6's profile results; the additive identities remain |
| 4.12 | Replies: aptness, coding, graded causation, the switch verdicts | Kill-test objections → v1; second system v2–v5 | Rewritten in v6; final patches 1–2 |

The Xiao and Xiong paper is the PDF the human uploaded on 29 Oct 04:01 without comment; it was placed in
packet P-d300 and read by the reviser from `inbox/sources/`.

## 5. Points where referee, reviewer or editor suggestions entered the final texts

- **This pipeline's blind referees.** A5: refinement dependence (route (a) question-relative measure,
  route (b) Theorem 4), Majors 1–5 (P-7297 S1-lit). A6: the verdict-change rule (S2-lit), the
  answer-by-answer rule, its safety proof and the five-state VER counterexample (G4), the concession that
  Conditional Knowledge Dominance is silent (S2-lit) (P-7f1b). A4: the cross-definition dilemma, the
  both-blocked switch and the engagement with Xiao and Xiong (P-d300 S7-lit).
- **Red-team kill tests.** Repairs entered all three v1 drafts (tables above).
- **The second AI system's 29 Oct review** (`ASSESSMENT-485bec4.md`, commit faa6381, 11:51) of A5 v4,
  A6 v4 and A4 v6. Its required fixes entered v7/v5/v7 through that system's own revisions: A5
  Non-vacuity, RI as sufficient with the n/(n+1) family, footnote-5 and audit corrections; A6
  *Deference Done Better*, rule-restricted conclusions, future policy, price condition, enumeration
  scope; A4 Wysocki, restricted frozen-mechanism claim, fixed-context conditions, and removal of the
  stipulated "natural target" sentence. Its *Good Guesses* comparison (9c39291) produced A5's prior-work concession.
- **This pipeline's audits.** A5 formal P1–P5, P8 and citation patches 1–8 (in v5, retained in v7);
  `citations_final.md` patches 1–3 (final). A6 citation P1–P14d and formal P1–P8 (final). A4 citation
  patches 1–8 and formal P1–P7 (final). These patches correct attributions, pinpoints, figures and
  wording; their changelogs record that they add no arguments, cases or claims.
- **Editor.** The editor agent and its plan files were never used (phases abandoned, log 21 Oct
  19:48:32). Changelogs exist only for the final patch passes and A5 v5.

## 6. Human messages and the contributions

None of the contributions above traces to a human message. The 25 entries in
`methodology/human_inputs.md` are logistics, courier, method, generic feedback and one selection. The
request for ambition named no problem. The Gate A2 answer selected among finished essays that the
orchestrator had recommended. The 29 Oct 17:35 entry relays the second system's status note (AI-written
risk headings: e.g. "A4: philosophical significance and overlap with prior work"); the subsequent patch
passes added no arguments, cases or claims (`final/A6/changelog.md`, `final/A4/changelog.md`).

Sources the human supplied that bear on the final essays, all without comment as recorded:
- Xiao and Xiong 2026 (uploaded 29 Oct 04:01), engaged in A4;
- the 2016 book on actual causality, supplied to the second system "without philosophical comments"
  (`state/external/submission-book-review-20261028/Halpern-Originality-Review.md`);
- the July 2021 draft of *Good Guesses* is described in the second system's files as "supplied"; the
  record does not say by whom, and the file is not in the repository (`state/audit/A5/citations_final.md`).

Limits of this ledger:
- The second system's chat transcripts are not in the repository; its contributions are traced from its
  files and commits.
- Not verified by this pipeline: the published text of *Good Guesses* (only the second system's reading
  of the 2021 draft and the authors' own summary); Hong 2026 (never read); the content of *Deference Done Better*
  (second system only); the Halpern 2016 pinpoints (confirmed only by the
  second system's book review; fetch `a4-audit-halpern-2016-pinpoints` open).
- The second system's early context-exposure disclosure, the quarantine, its lifting and the human's
  confirmation of revised `CLAUDE.md` §1.2 are recorded in the methodology report, §4.4.
