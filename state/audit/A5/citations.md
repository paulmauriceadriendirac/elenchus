# A5 v4 citation audit

Essay: `state/drafts/A5/v4.md` (final). Auditor: citation-auditor, 2026-10-29.
Verifier run: `python3 tools/verify_refs.py state/audit/A5/refs_audit_input.json` → `state/audit/A5/verification.{json,md}` (all 10 references; the earlier `bib/refs_v4_new.json` omitted Dorst 2019, Easwaran 2016 and Holguín 2022).

## Summary counts

| Step | Checked | Result |
|---|---|---|
| 1 Coverage | 10 cited works / 10 entries | 10/10 matched both ways; no year or spelling mismatches |
| 2 Metadata | 10 | 6 VERIFIED by tool; 4 flagged (3 MISMATCH, 1 PROBABLE), all confirmed by hand. 1 metadata correction (Wang issue number) |
| 3 Quotations | 13 (11 Dorst, 2 Holguín) + 1 scare-quoted term (D&M "filtered") | 13 exact, word for word, pages confirmed. 1 term quoted from a source that was not retrieved (patch: drop the quotation marks) |
| 4 Attributions | 34 | 26 accurate; 5 accurate on abstract/authors' summary/reliable secondary only (primary unread: A10–A14); 2 oversimplified (A2, A17); 1 inaccurate (A8). Patches 1–4, 7 |
| 5 Pages/sections | 22 Dorst page refs, 4 Holguín section refs | 20 + 4 correct; 2 imprecise (patches 5–6) |

Sources used: Dorst 2019 as published in *Mind*, with OUP page headers (`state/ambitious/sources/dorst-2019-lockeans.txt`; journal page = PDF page + 174). Holguín 2022, published HTML text (`state/ambitious/sources/holguin-2022-thinking-guessing.txt`). Easwaran, preprint dated 1 March 2013 (fitelson.org/coherence/kenny.pdf; in its appendix numbering, preprint App. F = the App. G that Dorst cites). Rothschild 2023 and Wang 2025, published open-access PDFs from link.springer.com. Joyce 2009, PDF from fitelson.org/coherence/joyce_2009.pdf. Abstracts of Leitgeb 2014 and 2017 and of Dorst & Mandelkern 2022 from OpenAlex and Crossref. Dorst & Mandelkern's own Substack summary of the joint paper (kevindorst.substack.com/p/the-conjunction-fallacy-take-a-guess). Open Library record for Levi 1967. Downloaded copies are in the session scratchpad, not the repo.

Panel works cited: Dorst & Mandelkern 2022 (Mandelkern) and Easwaran 2016 (Easwaran). Neither full text was available in its published form. Easwaran was checked against the author's preprint; Dorst & Mandelkern against the authors' own summary. Fetch request filed: `requests/fetch/a5-dorst-mandelkern-2022-good-guesses.md` (high).

## Step 1 — Coverage

| In-text citation (locations) | References entry | Status |
|---|---|---|
| Easwaran (2016) — §1 | Easwaran 2016 | OK |
| Dorst (2019) + bare page refs — §§1–7, fn 1, fn 3 | Dorst 2019 | OK (fn 1 states page refs are to the published article; confirmed) |
| Joyce 2009, §5 — §1 (via Dorst) | Joyce 2009 | OK; Joyce §5 is "Atomism or Holism?" (confirmed in PDF) |
| Rothschild (2023) — §1 | Rothschild 2023 | OK |
| Wang (2025) — §1 | Wang 2025 | OK |
| Levi (1967) — §1, §5 | Levi 1967 | OK |
| Leitgeb (2014, 2017) — §1, §5 | Leitgeb 2014; Leitgeb 2017 | OK |
| Dorst and Mandelkern (2022) — §1, §5 | Dorst & Mandelkern 2022 | OK |
| Holguín (2022), (2022, §5), (2022, §7.2), (2022, §§7.2, 8.1) — §§1, 3, 6, 7 | Holguín 2022 | OK |

No orphan entries. The spelling "Holguín" (with accent) matches the article page; Crossref's record lacks the accent.

## Step 2 — Existence and metadata

| Ref | Tool | Hand check / evidence | Verdict |
|---|---|---|---|
| Dorst 2019, *Mind* 128 (509): 175–211, doi:10.1093/mind/fzx028 | MISMATCH (year) | Crossref: online 12 Dec 2017, print Jan 2019, vol 128, iss 509, pp 175–211. PDF header: "Mind, Vol. 128 . 509 . January 2019". | Correct as printed |
| Dorst & Mandelkern 2022, *PPR* 105 (3): 581–618 | VERIFIED | Crossref: vol 105, iss 3, pp 581–618, print Nov 2022 (online 2021) | Correct |
| Easwaran 2016, *Noûs* 50 (4): 816–853 | VERIFIED | Crossref: vol 50, iss 4, pp 816–853, print Dec 2016 (online 2015); title matches | Correct |
| Holguín 2022, *Phil. Imprint* 22 (1), doi:10.3998/phimp.2123 | VERIFIED | Crossref: vol 22, iss 1, 19 Apr 2022 | Correct |
| Joyce 2009, in Huber & Schmidt-Petri (eds), *Degrees of Belief*, 263–297, Springer | VERIFIED | Crossref: pp 263–297, Springer Netherlands, 2009 (Synthese Library); editors confirmed in Dorst's bibliography (p. 208) | Correct |
| Leitgeb 2014, *Phil. Review* 123 (2): 131–171 | VERIFIED | Crossref: vol 123, iss 2, pp 131–171 | Correct |
| Leitgeb 2017, *The Stability of Belief: How Rational Belief Coheres with Probability*, OUP | MISMATCH (title similarity 0.51) | Crossref: title "The Stability of Belief", subtitle "How Rational Belief Coheres with Probability", OUP, 30 Mar 2017, ISBN 9780198732631. The mismatch is an artefact of the subtitle. | Correct |
| Levi 1967, *Gambling with Truth: An Essay on Induction and the Aims of Science*, New York: Knopf | PROBABLE (matched a 1976 review, doi:10.2307/1267533) | Open Library: Isaac Levi, *Gambling with Truth*, first published 1967, New York: Knopf (also Routledge & Kegan Paul 1967; MIT Press 1973). Wang 2025 cites Levi (1967). | Correct |
| Rothschild 2023, *Erkenntnis* 88 (5): 1979–1995 | MISMATCH (year) | Crossref: vol 88, iss 5, pp 1979–1995, print Jun 2023, online 23 Jul 2021. PDF header: "Erkenntnis (2023) 88:1979–1995". | Correct |
| Wang 2025, *Phil. Studies* 182 (5): 1433–1465 | VERIFIED | Crossref: issue "5-6"; PDF header "Philosophical Studies (2025) 182:1433–1465" | **Issue wrong → patch 8** |

## Step 3 — Quotations

All Dorst quotations were checked by script, after normalizing ligatures, curly quotes and line-break hyphens, and then read in context. Page = OUP running header.

| # | Essay text | Source | Page | Result |
|---|---|---|---|---|
| Q1 | "seems to contradict epistemic holism" | Dorst 2019 | 192 | Exact |
| Q2 | "to capture the sense in which it matters what other beliefs she holds" | Dorst | 193 | Exact |
| Q3 | "assumes only that $A_{B_0}$ is well-defined" | Dorst | 193 | Exact |
| Q4 | "rational constraints on beliefs are not affected by the sequence (if any) in which they are formed" | Dorst | 194 | Exact (fragment of the Sequence-Irrelevance statement) |
| Q5 | "belief-independent values $T_p$ and $F_p$" | Dorst, Prop. 5 | 195 | Exact |
| Q6 | "come from the (dis)values of true (false) beliefs" | Dorst | 196 | Exact (subject: "the Lockean thresholds") |
| Q7 | "until it gets an answer" | Dorst | 190 | Exact. Essay cites pp. 190–191; the passage is on p. 190 only → patch 6 |
| Q8 | "the value" (of adding a true belief) | Dorst | 193 | Exact ("Write t as $T^{B_0}_p$—the value, relative to $B_0$, of adding a true belief in p") |
| Q9 | "no holist ever thought that the insight of their position is that the order in which you consider propositions affects what you ought to believe" | Dorst | 195 | Exact |
| Q10 | "may be purely imaginative" | Dorst | 194 | Exact; the grammatical subject is "The process", not "the sequence" → patch 7 |
| Q11 | "best guesses" | Dorst | 196 (also 175, 192) | Exact |
| Q12 | "a set of propositions" | Dorst | 179 | Exact (A takes "a doxastic state D, a set of propositions P, a world w") |
| Q13 | "brute stipulations about the coordination of the proposition-sensitive thresholds" | Holguín 2022 | §7.2 | Exact |
| Q14 | "remains powerless to account for non-monotonicity" | Holguín | §7.2 | Exact. The source continues "…or for the complexities surrounding closure"; truncating at the end does not change the sense |
| Q15 | "filtered" (D&M) | D&M 2022 not retrieved | — | Not checkable in the source. The authors' Substack summary uses "filtered". Drop the quotation marks → patch 3 |

## Step 4 — Attributions

| # | Claim (location) | Source check | Class | Fix |
|---|---|---|---|---|
| A1 | Dorst argues that maximizing expected accuracy yields Lockean thresholds even without separability (Abstract, §1) | Dorst pp. 192, 194–195 | accurate | — |
| A2 | "Easwaran (2016) proved this, and also proved that values varying with the proposition yield proposition-specific thresholds" (§1) | Preprint §3.2 proves: a state maximizes expected score iff it believes all p with P(p) > W/(R+W) and none below. But Easwaran says "I won't actually assume any normative force for expected value itself, but I will use it as a tool" for dominance/coherence (preprint p. 12). For proposition-dependent values (preprint App. F.2 = published G.2) he states a "Modified Main Result … with exactly the same proof", phrased as coherence, and says "I have not worked out the consequences … in any great detail". Dorst p. 183 calls his Thm 1 / Cor 2 "identical" to Easwaran's §§3.2, G.2. | oversimplified (panel member; the framing implies Easwaran gives expected accuracy normative force; "also proved" overstates App. G.2) | patch 1 |
| A3 | Dorst presents these as Thm 1 and Cor 2 and credits both to Easwaran (p. 183) | p. 183; theorem headers pp. 186, 189 | accurate | — |
| A4 | Separability "seems to contradict epistemic holism" (p. 192, citing Joyce 2009, §5) | p. 192; Joyce §5 "Atomism or Holism?" | accurate | — |
| A5 | Given Sequence-Irrelevance, fixed proposition-specific thresholds follow (Prop. 5) | p. 195 | accurate | — |
| A6 | Rothschild (2023) develops additive scoring representations of Lockean belief (§1) | Abstract: characterizes Lockean belief sets by "an accuracy scoring system for full beliefs". n. 19: "The additivity assumption, that the total score … is just the sum of the individual scores, is defended by Dorst (2019)" | accurate | — |
| A7 | Wang (2025) studies expected-utility rules for deductively cogent belief states (§1) | Abstract and Def. 1 (EUM rule over belief cores) | accurate | — |
| A8 | "Levi (1967) accepts the deductive closure of the answers to a question that maximize expected epistemic utility, which trades truth against relief from agnosticism" (§1) | Levi not retrieved. Wang 2025 §5 (p. 1443) reconstructs Levi: a single non-empty belief core is chosen by maximizing expected utility $\alpha 1_B(w)+(1-\alpha)(1-|B|/|W|)$ (truth plus informational content); Levi's tie-breaking rule is cited at Wang p. 1038 (text line). "Answers … that maximize" (plural) misdescribes the rule. The phrase "relief from agnosticism", although Levi-sounding, appears in no retrieved source. | inaccurate (wording) / unverifiable phrase | patch 2 |
| A9 | Leitgeb (2014, 2017) ties rational belief to stably high credence, with belief fixed by a strongest believed proposition (§1) | 2014 and 2017 abstracts ("rational belief is equivalent to the assignment of a stably high rational degree of belief"); Wang 2025 §2 (belief core B) | accurate (abstract + reliable secondary) | — |
| A10 | Leitgeb: stability with threshold 1/2 is equivalent to deductive cogency plus a Lockean thesis whose threshold is the credence of the strongest believed proposition (§5) | 2014 abstract (closure + probability + Lockean thesis jointly satisfied iff belief ≡ stably high credence). Wang 2025 §2: HT_r cores "generate Lockean beliefs with a threshold of P(B)"; "if HT^{1/2} is violated, then one cannot have deductively closed Lockean beliefs". Primary theorem not read; revision_notes_v4 says this claim was "NOT used (could not read the definition)", but v4 makes it. | accurate on secondary; unverifiable in primary | none required; optional: verify the theorem in Leitgeb 2014 if the PDF arrives |
| A11 | D&M model guesses as maximizing expected answer-value, an accuracy-informativity tradeoff over answers to a question (§1) | D&M abstract: "people aim to optimize a tradeoff between accuracy and informativity"; Substack (by both authors) on expected answer-value given question Q | accurate (abstract + authors' summary) | — |
| A12 | …and show that only "filtered" guesses do so, an observation they credit to Holguín (§1) | Substack: "A guess is permissible only if it is filtered"; "Our two most important observations about good guesses come from Holguín's paper". The word "filter" does not occur in Holguín 2022 (checked), which is consistent with "observation", not term, credited. | accurate on the authors' summary; primary unverified | patch 3 (drop the quotation marks); fetch filed |
| A13 | D&M value = probability × value for true guesses increasing with the proportion of the question's cells ruled out, rate set by an informativity parameter; false guesses score zero (§5) | Substack: informativity $Q_p$ = "the proportion of the complete answers to Q that p rules out"; true-guess value $J^{Q_p}$; "we'll assign false guesses an answer-value of 0" | accurate (authors' summary); primary unverified | none; confirm when the fetch arrives |
| A14 | Part (ii) is the analogue of their result that only filtered guesses maximize expected answer-value (§5) | as A12 | accurate on summary | — |
| A15 | Holguín argues rational thinking is non-monotone in credence and question-sensitive (§1) | §5 "Thinking is non-monotonic"; §8.1 "Thinking as question-sensitive"; abstract | accurate | — |
| A16 | Accuracy First leaves inconsistent, nonclosed and empty states among the options (p. 183) | p. 183: B "need not be consistent, or deductively closed, or non-empty" | accurate | — |
| A17 | "Conservativeness, $T_p<-F_p$, makes $\tau_p>1/2$ (p. 185)" (§2) | p. 185 states Conservativeness only for uniform values: \|T\| < \|F\|. For proposition-dependent values Dorst's condition is Variable Conservativeness, $\|T_p\|<\|F_{\neg p}\|$ and $\|T_{\neg p}\|<\|F_p\|$ (p. 191), and he explicitly lets thresholds fall below 1/2 (Steve case, p. 190; "whenever the threshold for p drops below 1/2", p. 191). The essay ascribes its own proposition-indexed condition to Dorst's p. 185. | oversimplified (a Dorst-literate reader will notice) | patch 4 |
| A18 | In §4.2 the measure depends on the current state $B_0$ (§2) | p. 193 | accurate | — |
| A19 | Dorst writes the increments as $T^{B_0}_p$, $F^{B_0}_p$; Prop. 4 gives a threshold for the last proposition in a sequence (§2) | pp. 193–194 | accurate | — |
| A20 | Prop. 5's proof sets $T_p=T^{B^-}_p$ for a state $B^-$ (§2) | Proof on p. 207 ("if we set $T_p = T^{B-}_p$ and $F_p = F^{B-}_p$") | accurate; page imprecise | patch 5 |
| A21 | Dorst's reply to the emptiness worry depends on thresholds coming from (dis)values (§2) | §5, p. 196 | accurate | — |
| A22 | Sequence-Irrelevance is stated as a constraint on rationality (§2) | p. 194: "stated in terms of rationality, not expected accuracy" | accurate | — |
| A23 | Exam motivation for Separability (p. 184) (§3) | p. 184 | accurate | — |
| A24 | Holguín's Non-Monotonicity: permitted to think p at a lower credence and not at a higher one (2022, §5) (§3) | §5 definition (two agents, or one agent at different times) | accurate | — |
| A25 | Dorst's model of "Who do you think will win?": the question lowers the penalty for answers "x wins"; belief at 0.48 depends on whether a rival is more probable (§3) | p. 190, Cases 1–2 | accurate (page → patch 6) | patch 6 |
| A26 | In Dorst's model the dependence enters through a change of values driven by the demand for an answer (§3) | p. 190: "Since the question presupposes an answer, it adjusts them (within reason) until it gets one" | accurate | — |
| A27 | Holguín: sophisticated Lockeanism needs brute stipulations and cannot accommodate non-monotonicity (2022, §7.2) (§3) | §7.2 | accurate | — |
| A28 | Dorst's God/sequence example (p. 194); Prop. 4 is a necessary condition (§3) | p. 194 ("only if") | accurate | — |
| A29 | Dorst separates the order of consideration from holism (p. 195) (§4) | p. 195 | accurate | — |
| A30 | Variable Conservativeness (his Prop. 3) excludes believing p and its complement under separable measures (fn 3) | p. 191, Prop. 3 | accurate | — |
| A31 | Dorst's accuracy function takes "a set of propositions" as an argument (p. 179) (§6) | p. 179 | accurate | — |
| A32 | Dorst's §4.1 model of questions is consistent with "questions act only through values"; Holguín's view (§§7.2, 8.1) denies it (§6) | Dorst pp. 189–192 (questions shift $T_p$, $F_p$). Holguín §7.2: depends on "whether there are any salient alternatives to p in which that agent has higher rational credence"; §8.1 | accurate | — |
| A33 | Strict truth-directedness is the constraint Dorst places on holistic measures (§7) | p. 193, cases (ii)–(iii): t > 0, f < 0 | accurate | — |
| A34 | Dorst glosses beliefs as "best guesses" (p. 196); Holguín's argument targets sophisticated Lockeanism (§7) | Dorst p. 196; Holguín §7.2 targets the "sophisticated Lockean", citing Dorst (2019) | accurate | — |

Counts: accurate 26; accurate on abstract/authors' summary/secondary only 5 (A10, A11, A12, A13, A14); oversimplified 2 (A2, A17); inaccurate 1 (A8). Patch 3 (A12) removes an unverifiable quotation, not a misattribution.

## Step 5 — Page numbers and dates

| Ref in essay | Verified location | Status |
|---|---|---|
| Dorst p. 183 (credit to Easwaran) | p. 183 | OK |
| p. 192 (holism quote) | p. 192 | OK |
| p. 183 (Accuracy First options) | p. 183 | OK |
| p. 185 (Conservativeness) | p. 185 (uniform values only) | page OK; content → patch 4 |
| p. 193 ×2 | p. 193 | OK |
| p. 194 (Sequence-Irrelevance) | p. 194 | OK |
| p. 195 (Prop. 5) | p. 195 | OK |
| pp. 206–207 (proof sets $T_p=T^{B^-}_p$) | p. 207 (p. 206 repeats only the statement) | patch 5 |
| p. 196 (thresholds from (dis)values) | p. 196 | OK |
| pp. 190–191 ("until it gets an answer") | p. 190 | patch 6 |
| p. 194 (God example; "purely imaginative") | p. 194 | OK |
| p. 193 ("the value") | p. 193 | OK |
| p. 195 (holist quote) | p. 195 | OK |
| p. 184 (exam) | p. 184 | OK |
| p. 179 ("a set of propositions") | p. 179 | OK |
| p. 196 ("best guesses") | p. 196 | OK |
| Prop. 3 (fn 3), Prop. 4, Prop. 5, Thm 1, Cor 2, §4.1, §4.2 | pp. 191, 194, 195, 186, 189; §§4.1–4.2 | OK |
| Joyce 2009, §5 | §5 "Atomism or Holism?" | OK |
| Holguín §5, §7.2 (×2), §8.1 | confirmed | OK |
| Years: Dorst 2019, Rothschild 2023, D&M 2022, Easwaran 2016 | issue years; online 2017, 2021, 2021, 2015 respectively | OK (issue-year convention used consistently) |

## Patch list (apply verbatim, in `state/drafts/A5/v4.md`)

1. §1, para 1.
   OLD: `Easwaran (2016) proved this, and also proved that values varying with the proposition yield proposition-specific thresholds;`
   NEW: `Easwaran (2016) proved this, using expected score as a tool for showing such belief states non-dominated, and stated the analogue for values varying with the proposition, which yields proposition-specific thresholds;`

2. §1, "closest prior work" paragraph.
   OLD: `Levi (1967) accepts the deductive closure of the answers to a question that maximize expected epistemic utility, which trades truth against relief from agnosticism.`
   NEW: `Levi (1967) accepts the consequences of the answer to a question that maximizes expected epistemic utility, which trades truth against informational value.`

3. §1, same paragraph.
   OLD: `show that only "filtered" guesses do so`
   NEW: `show that only filtered guesses do so`

4. §2, para after (Permission).
   OLD: `Conservativeness, $T_p<-F_p$, makes $\tau_p>1/2$ (p. 185).`
   NEW: `Call the values conservative when $T_p<-F_p$; then $\tau_p>1/2$. This extends Dorst's Conservativeness, $|T|<|F|$ for uniform values (p. 185); his Variable Conservativeness for proposition-dependent values instead requires $|T_p|<|F_{\neg p}|$ and $|T_{\neg p}|<|F_p|$ (p. 191), and lets thresholds fall below $1/2$.`

5. §2, "Two features" paragraph.
   OLD: `for a state $B^-$ (pp. 206–207).`
   NEW: `for a state $B^-$ (p. 207).`

6. §3, *Fixed context*.
   OLD: `"until it gets an answer" (pp. 190–191).`
   NEW: `"until it gets an answer" (p. 190).`

7. §3, *Order*.
   OLD: `Dorst himself says the sequence "may be purely imaginative" (p. 194).`
   NEW: `Dorst himself says the process of forming beliefs in sequence "may be purely imaginative" (p. 194).`

8. References, Wang.
   OLD: `*Philosophical Studies* 182 (5): 1433–1465.`
   NEW: `*Philosophical Studies* 182 (5–6): 1433–1465.`

Net change ≈ +45 words (mostly patch 4). Re-run `tools/wordcount.py` after applying.

## Open items (not blocking submission)

- Dorst & Mandelkern 2022 (panel: Mandelkern). Claims A11–A14 rest on the abstract and the authors' own Substack summary. When `requests/fetch/a5-dorst-mandelkern-2022-good-guesses.md` is fulfilled, confirm three things in the paper itself: (a) expected answer-value = P(p)·J^{Q_p}, with false guesses scoring 0; (b) that the paper, not only the blog, ties filtering to maximization; (c) the credit to Holguín. If it does not arrive, the text after patch 3 is supportable from the authors' own summary.
- Easwaran 2016 (panel: Easwaran). Checked against the 2013 preprint. The published App. G.2 may differ in wording from preprint App. F.2. Patch 1 is safe under both readings. No fetch filed, because Dorst p. 183 corroborates the substance.
- Leitgeb 2014 equivalence (A10). Supported by the abstract and Wang 2025 §2. The primary theorem was not read.
