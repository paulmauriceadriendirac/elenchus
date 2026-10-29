# A5 changelog: v4 -> v5 (patch mode)

Date: 2026-10-29. Input: `state/drafts/A5/v4.md` (copied to `v5.md` first; v4 unchanged, sha256 40690ed5…).
Patch lists: `state/audit/A5/formal.md` (P1–P5, P8) and `state/audit/A5/citations.md` (patches 1–8).
Order: formal patches first, then citation patches. No two patches touched the same passage, so none needed merging.
Each old string matched v4 exactly once. Nothing new was argued or cited. No refs.json change: no citation was added, and the bib JSON files have no issue field, so the Wang correction lives only in the References entry.

Word count (`tools/wordcount.py --target 5600`): v4 strict 5,296 -> **v5 strict 5,482** (wordlike 5,464; footnotes 262). Limit 6,000, target 5,600: OK.
Injection check (`tools/check_injection.py --judges-file state/panel/judges.txt`): no hard flags. Soft flags: Mandelkern (3) and Easwaran (3). Both are genuine citations, unchanged in number from v4.

## Formal patches (`state/audit/A5/formal.md`)

| Item | Location | Change | Status |
|---|---|---|---|
| P5 | Abstract | "For every positive premium and conservative values," -> "For every positive premium and any conservative values shared by all propositions,". Theorem 1 covers uniform values only. | Applied verbatim |
| P4 | §4, last paragraph | "ME and BI imposed on each member yield …" -> "ME at each member's own state, together with BI read across the family (the increments $T^{B_0}_p$ and $F^{B_0}_p$ of $A_{B_0}$ at $B_0$ do not depend on $B_0$), yields …". This removes the member-by-member reading that N5 refutes. | Applied verbatim |
| P2 | §6, first sentence after the repairs | "no non-Lockean score can" -> "no truth-directed, conservative non-Lockean score can". The unqualified claim is false (pairwise tie measure). | Applied verbatim |
| P3 | §6, paragraph after Theorem 4 | "That is the localization the Lockean needs, and accuracy adds only monotonicity on a two-world problem." -> "That is the localization the Lockean needs. On the two-world problem, truth-directedness and CI then supply a single threshold above $1/2$." | Applied; adapted only in typesetting: "1/2" set as `$1/2$`, matching every other prose occurrence in the essay |
| P1 (text) | §6, same paragraph | "And a truth-directed two-world measure violating CI is non-monotone.[^5]" replaced by the CI-dropping witness: the separable measure $T_p=2$, $F_p=-1$ is TD and RI, violates CI, and has unique optimum $\{W,p,\bar p\}$ at credence $1/2$. The old witness violated RI (N1). | Applied verbatim |
| P1 (fn 5) | Footnote 5 | Replaced entirely with the supplied footnote (symmetry from RI; the pairwise tie measure is TD and RI and has no threshold on $1/3<C(p)<2/3$). | **Adapted** (one clause): the supplied "makes $p$ optimal at one credence and excluded at a higher one" became "puts $p$ in every optimum at one credence and in none at a higher one". Reason: the some/some reading of the supplied wording is satisfied by the footnote's own tie measure (for $1/3<c_1<c_2<2/3$, $p$ is in some optimum at $c_1$ and outside some optimum at $c_2$), so the footnote would refute itself. The new wording is exactly what N2 proves and what `a5_thm4.py` check (4) tests. |
| P8 (Leitgeb) | §5, rival-theories paragraph | Deleted "On Leitgeb's theory (2014, 2017), stability with threshold 1/2 is equivalent to deductive cogency together with a Lockean thesis whose threshold is set by the credence of the strongest believed proposition." The primary theorem was not read (formal claim 31; citation A10 rests on the abstract and Wang 2025 only). | Applied (deletion chosen over reduction). §1's description of Leitgeb (citation A9, accurate) stays, so both Leitgeb entries remain cited, and "For Levi and Leitgeb the agent accepts all and only the consequences of the selected proposition" still has its antecedent in §1 ("Other bridge theories select a strongest accepted proposition"). A reduced sentence would have repeated §1. |
| P8 (D&M) | §5, same paragraph | Reduced to what the authors' own summary states (Dorst, co-written with Mandelkern, "The Conjunction Fallacy? Take a Guess.", kevindorst.substack.com/p/the-conjunction-fallacy-take-a-guess, 18 Jul 2020, retrieved 2026-10-29; the formula image $E^J_Q(p)=P(p)\cdot J^{Q_p}+P(\neg p)\cdot 0=P(p)\cdot J^{Q_p}$ was viewed). Three changes: (a) "A guess's value is its probability times …" -> "A guess's expected answer-value is its probability times its answer-value if true", since the summary separates answer-value from expected answer-value; (b) "a value for true guesses that increases with the proportion of the question's cells it rules out, at a rate set by a parameter weighting informativity" -> "which is a parameter (at least 1) measuring the value of informativity, raised to the proportion of the question's complete answers that the guess rules out". The summary has $J\ge1$ and $J^{Q_p}$ with $Q_p$ "the proportion of the complete answers to $Q$ that $p$ rules out", so with $J=1$ the value does not increase. The symbol $J$ is avoided because §4 uses $J_p$, $J^B_p$; (c) "their result that only filtered guesses maximize" -> "their argument that only filtered guesses maximize". The summary gives a swap argument ("This explains … Filtering"), not a stated theorem. "False guesses score zero" ("we'll assign false guesses an answer-value of 0") and "combined multiplicatively" (the formula) are both in the summary and were kept. | Applied (wording mine; content limited to the summary) |
| P8 (D&M, §1) | §1, closest-prior-work paragraph | Checked against the same summary: "model guesses as maximizing expected answer-value" ("we maximize expected answer-value"), "accuracy-informativity tradeoff", "show that only filtered guesses do so" (swap argument), "an observation they credit to Holguín" ("Our two most important observations about good guesses come from Holguín's paper: Filtering …"). Nothing goes beyond the summary. | No change beyond citation patch 3 |
| P8 (Levi, §5) | §5 | "Levi (1967) likewise accepts a strongest answer chosen by expected epistemic utility" is consistent with citation patch 2 and with the audit's source (Wang 2025 §5 reconstruction). | No change needed |
| P6 | §6 ", except at ties" | Optional; not in the task's list. | Not applied |
| P7 | §6 "In general, splitting …" | Optional; not in the task's list. | Not applied |

Formal re-check: the auditor's `state/audit/A5/formal/a5_thm4.py` was rerun on 2026-10-29. ALL CHECKS PASSED: witnesses (a) and (b) are TD, violate CI and satisfy RI; 0 swap-symmetric TD measures are non-monotone.

## Citation patches (`state/audit/A5/citations.md`)

| # | Location | Change | Status |
|---|---|---|---|
| 1 | §1, para 1 (Easwaran) | "and also proved that values varying with the proposition yield …" -> "using expected score as a tool for showing such belief states non-dominated, and stated the analogue for values varying with the proposition, which yields …" (A2) | Applied verbatim |
| 2 | §1, prior-work paragraph (Levi) | "accepts the deductive closure of the answers … that maximize …, which trades truth against relief from agnosticism" -> "accepts the consequences of the answer … that maximizes …, which trades truth against informational value". This removes the unsourced Levi-sounding phrase (A8). | Applied verbatim |
| 3 | §1, same paragraph | Quotation marks dropped from "filtered", which was not checkable in the unretrieved paper (Q15/A12) | Applied verbatim |
| 4 | §2, after (Permission) | The proposition-indexed condition is now the essay's own definition ("Call the values conservative when $T_p<-F_p$ …"). Dorst's Conservativeness $|T|<|F|$ (p. 185) and Variable Conservativeness $|T_p|<|F_{\neg p}|$, $|T_{\neg p}|<|F_p|$ (p. 191) are stated separately (A17). Checked: Dorst writes ¬p, so $\neg p$ is kept in his condition; fn 3's mention of Variable Conservativeness now has an antecedent. | Applied verbatim |
| 5 | §2, "Two features" | (pp. 206–207) -> (p. 207) | Applied verbatim |
| 6 | §3, *Fixed context* | (pp. 190–191) -> (p. 190) | Applied verbatim |
| 7 | §3, *Order* | "the sequence 'may be purely imaginative'" -> "the process of forming beliefs in sequence 'may be purely imaginative'". Checked against Dorst pp. 193–194 ("form her final belief-state Bn in sequence … The process may be purely imaginative"). | Applied verbatim |
| 8 | References, Wang 2025 | 182 (5) -> 182 (5–6) | Applied verbatim |

## Open items carried forward

- Dorst & Mandelkern 2022: the published text is still unread (fetch `requests/fetch/a5-dorst-mandelkern-2022-good-guesses.md`). When it arrives, confirm the answer-value form, the filtering argument and the credit to Holguín.
- Leitgeb 2014: if the equivalence is wanted again, it must first be checked against a retrieved copy of the primary text.
