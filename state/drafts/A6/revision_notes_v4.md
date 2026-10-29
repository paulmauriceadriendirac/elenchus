# A6 v4 revision notes (from v3, 02-Free-Evidence-v3.md)

**Word count.** `tools/wordcount.py`: strict 5,883 (limit 6,000; ceiling set for this task 5,900). `check_injection.py`: no hard flags; soft flags are the cited surnames Salow, Hawthorne and Goldstein. These are genuine citations: Goldstein and Hawthorne are cited only for what Goodman and Salow (2023, n. 40) report.

**v4 thesis (one sentence).** In finite statist, comparable normality models, conditioning expected utility on knowledge preserves Good's theorem exactly where knowledge is gapped; of three expected-utility versions of Salow's conditional repair, two fail, and the third succeeds only by abandoning the knowledge-based verdict on costly inquiry.

**Main substantive change.** §5 is rebuilt around three developments of Conditional Knowledge Dominance (CKD):
- **CEU** conditions on the options differing. Theorem 3 is kept. It is now conceded that CKD itself is silent in the constructed problems, and A.7 proves that CKD never forbids a free look when the options differ at every state.
- **VER** conditions on what the evidence would lead one to do.
  - G4's five-state counterexample is verified.
  - VER fails in 1,724 of the 2,322 relative-defeat pairs with up to four states, using random priors and problems.
  - It can fail without relative defeat, where KDT is safe (new example; CEU also fails there).
- **ANS** conditions answer by answer. G4's safety proof is accepted as Proposition 4.
  - New Proposition 5: whenever there is relative defeat, ANS pays a positive price to answer, where CKD (with D = E) forbids paying. This was verified in all 3,306 relative-defeat cases.
  - In Bjorn, ANS pays up to 1.23 at 100:1, which is more than the known payoff of 1.

## Triage: S2-lit (specialist + literature)

| # | Point | Verdict | Check / action |
|---|---|---|---|
| MS(a) | CEU says more than CKD; CKD silent in Thm 3 construction | ACCEPT | Verified (m* argument), generalized in A.7; §5.2 concession; abstract/§1/§7 recalibrated |
| MS(b) | Verdict-change rule prefers looking in every Thm 3 instance | ACCEPT IN PART | True for large L. False as a general safety claim: VER fails at threshold L (5-state example, `checks/v4_conditional_rules.py`) and broadly (`v4_verdict_rule.py`) |
| MS(c) | Refuted rule worse than KDT | ACCEPT | Now shown explicitly: CEU and VER disvalue a question without relative defeat (`v4_verdict_example.py`) |
| M2a | "reopen a weight" at every situation false | ACCEPT | Verified by Cauchy–Schwarz: a weight is reopened iff R<(1+√2)²c²; Pr ≈ 1.4e-5 (`bjorn_v4.py`). §3 now makes three separate claims; A.5 extended |
| M2b | "as natural as a second reading" false | ACCEPT | Deleted. Added G4's {|μ|≤1000} example showing that Corollary (ii) depends on the questions |
| M3 | Optional inquiry / NESTEDNESS / one p_v at a time / statism n. 47 | ACCEPT IN PART | Added a modelling paragraph to §2 (verified G&S n. 40 "future readings"). Theorem 1(b) and Theorem 2 are restated one question at a time. The n. 47 caveat is verified and added. BRN App. A (NESTEDNESS, Babysitter) was not available to me: act-dependent conditioning sets are set aside explicitly, not claimed |
| M4 | Value-of-evidence literature missing | ACCEPT IN PART | Added Dorst 2020, with its role verified via Salow's "Value of Evidence" text, and Geanakoplos's conditions per Ahmed & Salow n. 13. Increment restated: the shape of Thm 1 is Geanakoplos's; the normality content is new. Skyrms 1990, Huttegger 2014 and Dorst et al. 2021 are not cited: contents unverified (§1.3) |
| M5 | Question-sensitivity (Goldstein–Hawthorne model) | ACCEPT AS LIMITATION | §6.3 flags it, with G&S n. 40 verified. The bet was not computed in that model |
| M6 | Hong 2026 overlap unquantified | ACCEPT IN PART | §1 states what is known from the retrieved §§1–3 summary (state/external/ambitious-review-20261022/REVIEW.md) and the increment. No quotation: the text is inaccessible (Wiley 403) |
| m | Abstract lacks "every decision problem" | ACCEPT | Fixed |
| m | "practical content of Salow's dissolution" | ACCEPT | Replaced with the verified Salow 2025, 35 quote ("by itself doesn't predict…"; "a natural development of it will") |
| m | CEU with >2 options / cycles | ACCEPT | Theorem 3: all pairs differ everywhere, so no cycle |
| m | Thm 3 hypothesis redundant | ACCEPT | Removed |
| m | A.6 L before ε | ACCEPT | L>(1+N)/min q_F works for all ε<1 |
| m | θ-threshold paragraph | ACCEPT | Cut |
| m | Perturbed-Bjorn figure; "only add failures" | ALREADY FIXED in v3 | — |
| m | §6.1 empty-question example | ACCEPT | Reduced to a clause |
| m | Enumeration unverifiable | ACCEPT IN PART | Scripts are in checks/; counts are reported in the appendix only |
| m | Harman/Kripke/Williamson/Oddie absent | ACCEPT | Mentions removed (§6.2 "trivial" cut) |
| m | Encroachment credited only to Hawthorne | ACCEPT | Fantl & McGrath 2002 and Weatherson 2005 added via Salow n. 3 (verified verbatim) |
| m | 0.37 vs 0.95 | ACCEPT | Both stated, with subject matter distinguished; "relatively rare" moved to its encroachment context |
| m | "discoverable" undefined | ACCEPT | Defined (E∩c ∈ ℰ) |
| unver. | Williamson clock & Das | ACCEPT | Ahmed & Salow's clock verified in the cached text; Das dropped from that sentence |
| unver. | Goldschmidt "describes this form" | ACCEPT | Rephrased as representation-theorem foundations |

## Triage: G4 (defender)

| # | Point | Verdict | Check / action |
|---|---|---|---|
| MS | Answer-indexed rule is safe; three claims false | ACCEPT (the proof) / REPLY | Proof checked; 0 negatives in 64,004 pairs × 3 random problems. Claims recalibrated. Reply via Prop 5: ANS contradicts CKD on costly inquiry, or else is discontinuous at price 0 |
| M1 | Encroachment left standing; press the cost | ACCEPT | §6.2: on the F&M/Weatherson criterion, the mere offer of a free scale removes knowledge at 10:1; finite graded ubiquity. Stanley 2005, F&M 2009 and Williamson 2005 not added (unread) |
| M2 | p_v assumption; false sentence; {|μ|≤1000} counterexample | ACCEPT | Assumption stated in each result; motivated (testimony, G&S §8); sentence removed; counterexample added in §4 |
| M3 | §5.3 dilemma overstated | ACCEPT | Reduced to one scope sentence |
| M4 | §6.6 misdiagnosis (non-conditionalizing update) | ACCEPT | §6.4 rewritten |
| M5 | Margins scope; G&H predicts defeat with Margins | ACCEPT | Added to §6.1 (n. 40 verified: "even given MARGINS") |
| m | c-dependence | ACCEPT | Verified c²=−2ln(1−t) from G&S 121; at t=.95, 10:1 → −0.0099 and 100:1 → −0.154 (`bjorn_v4.py`) |
| m | ε reconcile; "ken" undefined; "whichever theory" | ACCEPT | Fixed |
| m | Stakes: finite theorems need large L | ACCEPT | §6.2 says so; Bjorn supports moderate stakes |
| R1 | Act-cell counterexample | VERIFIED | VER −0.0082 (script) |
| R3 | Collapse | NOTED | Conclusion lists collapse as a sufficient restriction (no space to weigh the abductive cost) |
| R6 | Sophisticated choice | ACCEPT | §6.4 |

## New references (all verified with tools/verify_refs.py → checks/refs_v4_new.verification.md)
Dorst 2020 (PPR 100: 586–632; doi 10.1111/phpr.12561); Fantl & McGrath 2002 (Phil Review 111: 67–94); Weatherson 2005 (Phil Perspectives 19: 417–443); Goldstein & Hawthorne 2022 (Phil Studies 179: 1341–1372). Carter & Hawthorne 2024 is not cited. The full list is in refs_v4.json. Hong 2024's earlier MISMATCH is an online-first (2022) versus print-year (2024) difference.

## New quotations checked against retrieved text
- Salow 2025: pp. 24 n. 3, 34, 35 and 36. Source: ORA PDF, extracted to the scratchpad.
- G&S 2023: 130 n. 40 and 138 n. 47 (inbox source).

## Computations (state/drafts/A6/checks/)
- `v4_conditional_rules.py`/.out
- `v4_verdict_rule.py`/.out (n≤4 only; the n=5 run was too slow)
- `v4_verdict_nodefeat.py`/.out
- `v4_verdict_example.py`/.out
- `bjorn_v4.py`/.out

## Not done / open
- The VER safety boundary.
- Non-statist models.
- Bets in the Goldstein–Hawthorne model.
- BRN App. A on act-dependent states.
