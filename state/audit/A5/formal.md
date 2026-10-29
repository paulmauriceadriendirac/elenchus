# Formal audit: A5 v4 (`state/drafts/A5/v4.md`)

Status: COMPLETE. Mode: audit, independent re-verification.

## Bottom line

All four theorems are correct, and their proofs check by hand. Every number in the essay is reproduced exactly.

There are two errors, both in §6's discussion of Theorem 4:
- **Footnote 5 does not show that CI cannot be dropped.** Its measure violates RI.
- **"No non-Lockean score can" achieve unrestricted invariance is false** unless it is qualified to truth-directed, conservative scores.

There are also three recommended precision fixes:
- the abstract's quantifier over values;
- the §4 sentence about families of measures;
- the gloss "accuracy adds only monotonicity".

Two literature claims could not be verified here: the Leitgeb equivalence and the description of Dorst–Mandelkern answer-value. The exact patch list is at the end.

## Method and files

I wrote my own scripts. None of them imports the author's checks.
- Arithmetic is exact: Fractions or integers throughout.
- The record measure is computed from its world-level definition `A(B,w)=Σv_p(w)+β[w∈∩B]`. So the Φ formula is never assumed when testing Theorem 3.
- Φ maximisation over cores is used only on spaces too large to enumerate. Those are the 2^n-core searches in a4. They rely on Theorem 3, which I first verified exhaustively in a3.
- I checked every proof by hand.
- I compared the essay's statements of Dorst's principles with `state/ambitious/sources/dorst-2019-lockeans.txt` (PDF page n = journal p. 174+n).

Scripts and outputs are in `/home/user/elenchus/state/audit/A5/formal/`. Rerun any of them with `python3 <name>.py`; use `python3 -I` for a6.

| Script | Content | Result |
|---|---|---|
| a1_case_thm1.py/.out | §3 case; Order paragraph (all 40,320 orders); §4 gap numbers and EA-difference formula; Thm 1 (sympy identities, 250 random parameter sets, ε∈{0,1e-9,1e-6}); fn 4 | all pass |
| a2_thm2.py/.out | Thm 2(a),(b) certified by exact rank arguments on 2 and 3 worlds; fn 3 example | all pass |
| a3_thm3.py/.out | Thm 3 (exhaustive random tests on 2/3/4 worlds, ties allowed); generic (i)–(iii); four-world case (2^16 states); comparative statics; large β | all pass |
| a4_refinement.py/.out | §6 refinement numbers; null splits (k=1..6); normalised measure (2/4/8 splits, null-split invariance); two-world thresholds 5/6 and 7/9; question-relative measure | all pass |
| a5_thm4.py/.out | Thm 4 lemma (332 random TD+CI two-world measures, all 16 states); converse (RI for separable measures incl. ties); fn 5; symmetry lemma; replacement witnesses | all pass (see note) |
| a6_sources.py/.out | 23 Dorst quotations and page references; Holguín quotations | all pass |
| a7_values.py/.out | Non-monotonicity with proposition-dependent conservative values (exact grid, 20,301 credences) | none found (see claim 1) |

Note on a5: the first two runs failed only on sample-size conditions, never on the substantive ones. One run accepted 1 measure, another found 74 non-monotone measures where I had required more than 100. I redesigned the samplers and lowered that non-vacuity threshold to 50. Final counts: 332 TD+CI measures with 0 failures; 784 TD measures, of which 216 have symmetric verdicts and 74 are non-monotone, and 0 are both.

The author's c8 and c9 reproduce the same numbers: 7.25 and 6.91; fn 5 verdicts True/False/True. c9 never checks fn 5 for RI. Footnote 2 is accurate: the author's checks are exact (Fraction, or integer-scaled in c3), and c3 enumerates all 2^16 states.

## Claims

| # | Claim | Loc. | Verification | Status |
|---|---|---|---|---|
| 1 | "For every positive premium and conservative values" the record score is non-monotone | Abstract | Thm 1 covers values shared by all propositions only. a7 found no non-monotonicity on three worlds for β=3 with singleton τ=2/3, doubleton τ=0.99 (the sanity run with uniform values does detect the essay's case) | OVERBROAD: true for uniform values; unsupported (likely false) for proposition-dependent values. Patch P5 |
| 2 | TD+CI+RI entail fixed thresholds; without RI they do not follow | Abstract, P2, §8 | Thm 4 (checked); record measure (a4) | VERIFIED |
| 3 | Restricted invariance is satisfied by a question-relative record score | Abstract, P4, §6 | a4(5), by construction | VERIFIED |
| 4 | P1/C1: the record measure meets Prop. 5's premises plus Permission and violates its conclusion | §1 | formal parts: Thm 1, the case, TD, all states as options, state-independence | VERIFIED (the Sequence-Irrelevance reading is argued, not formal) |
| 5 | P3: space-independent fixed thresholds entail RI | §1 | hand argument (N3); a5(2) | VERIFIED (holds even at ties) |
| 6 | C2 follows from P3 | §1 | logic | VERIFIED |
| 7 | Under ME the derivation is valid iff the score is separable | §1, §4 | Corollary | VERIFIED |
| 8 | Statements of Accuracy First (p.183), MEA (p.182), Separability/Extensionality, Conservativeness and τ=−F/(T−F) (pp.184–185), Thm 1/Cor 2 and their credit to Easwaran (pp.183, 185, 189), §4.2 increments (p.193), Prop. 4 (p.194), SI (p.194), Prop. 5 (p.195), its proof setting T_p=T^{B−}_p (pp.206–207), p.196 gloss | §2 | a6 (23 items) and close reading | VERIFIED; all quotations verbatim and on the cited page |
| 9 | Separable optimum: include p if e_p>0, exclude it if e_p<0; τ_p>1/2 iff T_p<−F_p | §2 | algebra; consistent with Dorst's weak-inequality Thm 1/Cor 2 | VERIFIED |
| 10 | Prop. 5's T_p, F_p are values of the measure in a context, not functions of credence | §2 | source p.207 ("if we set Tp = T^{B−}_p") and p.196 | VERIFIED |
| 11 | Record increments: +T_p if true; −\|F_p\| or −\|F_p\|−β if false; strictly TD; conservative when T_p<−F_p | §3 | hand; a1 | VERIFIED |
| 12 | Case at C: unique optimum {1,12,13,W} with EA 4.30; runner-up {12,13,W} at 4.20 (same core); margin e_1=0.10 | §3 | a1, exhaustive | VERIFIED |
| 13 | Case at C': unique optimum {13,W} with EA 4.94; runner-up {1,12,13,W} at 4.75; 12 omitted although C'(12)=.76>τ | §3 | a1 | VERIFIED |
| 14 | Prop. 5 would need τ_1≤.70 and τ_1≥.75 | §3 | source (i), (ii) | VERIFIED |
| 15 | Thm 1 (c0, c1; max(c0,τ)<c1<1; both verdicts) | §3, App. | proof checked; sympy identities; random brute force | VERIFIED |
| 16 | For β≤D the interval has length βT/(D(2D+β)) and never closes | §3 | sympy: τ−c0=T(D−β)/(D(2D+β)) | VERIFIED |
| 17 | Order: first step gives −0.8; 1 first ends at {12,13,W}; 1 last gives +0.1 and the optimum | §3 | a1, all orders | VERIFIED |
| 18 | Dorst's lottery model; belief monotone within a context | §3 | source p.190; Cor 2 | VERIFIED |
| 19 | Adding the false 1 to {13} costs 2 at w2 and 5 at w3 | §4 | a1 | VERIFIED |
| 20 | EA(B)−EA(B∖{p}) = e_p−βC(∩(B∖{p})∖p) | §4 | a1, 3,000 random cases | VERIFIED |
| 21 | Thm 2(a),(b) | §4, App. | proof checked; exact rank certification (n=2,3) | VERIFIED |
| 22 | J^B_p=J_p, τ^B_p=−F^B_p/J_p; Corollary | §4 | proof step (ii) | VERIFIED |
| 23 | fn 3: the proviso is needed | fn 3 | a2: ME+TD on all states; J goes from 3 to 5/2 | VERIFIED |
| 24 | fn 4: the closure bonus is ME+TD; {w1} believed at (.575,.2,.225) and not at (.65,0,.35) | fn 4 | a1, both conventions for the empty state | VERIFIED |
| 25 | "for such a family, ME and BI imposed on each member yield fixed thresholds" | §4 | N5 | AMBIGUOUS: true if BI is read across the family, false member-by-member. Patch P4 |
| 26 | Thm 3, main statement | §5, App. | proof checked; a3 | VERIFIED |
| 27 | Thm 3, generic uniform case: B* unique; (i), (ii), (iii) | §5 | a3, 297 generic instances | VERIFIED ((ii) holds for every maximiser) |
| 28 | Four-world closure failure | §5 | a3: unique optimum, EA 5.44 (next 5.30); core {w1} | VERIFIED |
| 29 | Raising β cannot lower core credence; cores nested; large β leaves only W | §5 | hand; a3 | VERIFIED (uses uniform values, which the context implies) |
| 30 | Dorst–Mandelkern answer-value form; filtering result credited to Holguín; Levi | §1, §5 | no source in this audit | UNVERIFIED: route to citation-auditor |
| 31 | Leitgeb: stability with threshold 1/2 ⟺ cogency plus a Lockean thesis with threshold set by the strongest believed proposition | §5 | no source; revision_notes_v4 says the Leitgeb definition "could not" be read | UNVERIFIED: must be checked or removed (CLAUDE.md §1.3). Patch P8 |
| 32 | Refined C': Φ(1)=7.25 > Φ(13)=6.91; 1 believed at refined C' and at refined C | §6 | a4: Φ and all 2^16 states | VERIFIED |
| 33 | A null split multiplies the separable part by 2^{k−1}; effective premium β/2^{k−1}; the interval shrinks exponentially | §6 | a4, k=1..6, exact | VERIFIED (presumes values equal across a proposition and its refinements, as with uniform values; optional P7) |
| 34 | Normalised measure: rescales the premium; null splits leave Φ unchanged; b=3/8 with 2/4/8 splits keeps both verdicts | §6 | a4 | VERIFIED |
| 35 | Neither repair is fully refinement-invariant | §6 | a4: two-world thresholds 5/6 (record) and 7/9 (normalised) | VERIFIED |
| 36 | "and no non-Lockean score can" | §6 | a5(5b): pairwise tie measure is TD and RI, and has no threshold | FALSE as stated (needs "truth-directed, conservative"). Patch P2 |
| 37 | Thm 4, statement and proof | §6, App. | hand; a5(1) | VERIFIED |
| 38 | "accuracy adds only monotonicity on a two-world problem" | §6 | N2 | MISLEADING: under TD, RI already excludes non-monotonicity; CI places τ in (1/2,1). Patch P3 |
| 39 | Separable measures whose values are preserved under coarsening satisfy RI; "except at ties" | §6 | a5(2), including ties at 2/3; N3 | VERIFIED; the caveat is unnecessary (optional P6) |
| 40 | The record measure is TD and CI but not RI: threshold 5/6, withholds at .70 | §6 | a4 | VERIFIED |
| 41 | fn 5: TD, violates CI, p optimal at .30 and .70 but not at .64 | fn 5 | a5(3) | VERIFIED as arithmetic |
| 42 | "Neither premise can be dropped": the CI half rests on fn 5 | §6 | N1, N2; a5(3–5) | FALSE as support: the fn 5 measure violates RI. The claim itself is TRUE with witnesses (a) and (b). Patch P1 |
| 43 | Lockeanism follows from TD, CI and RI without Separability, SI, ME or BI | §6 | Thm 4 | VERIFIED |
| 44 | The normalised measure passes the equiprobable-split test in the case | §6 | a4(3) | VERIFIED |
| 45 | In the four-world case the premium accrues on the unbelieved {w1} | §7 | a3 | VERIFIED |
| 46 | Without Permission, nothing is rational at C or C' | §7 | logic | VERIFIED |
| 47 | Holguín: Non-Monotonicity (§5); §7.2 quotations; §§7.2 and 8.1 | §3, §6 | a6 plus headings in the source: §5 defines "Non-Monotonicity"; both quotations are in §7.2; §8.1 is "Thinking as question-sensitive" | VERIFIED (bonus) |

## Proof notes

**N1. The footnote 5 measure violates RI.** RI quantifies over every surjection, including the swap π of {u,v}. With p*={v} we have π⁻¹(p*)={u}. So the verdict on {u} at C(u)=t must equal the verdict on {v} at C(v)=t.

In fn 5:
- at C(u)=.3, {u}=p is in the unique optimum {W,p,p̄};
- at C(v)=.3, that is C(u)=.7, the unique optimum is {W,p}, which omits {v}.

This is computed in a5(3). Excluding bijections does not help. Any three-world space W' with a coarsening σ onto {u,v} also has the coarsening swap∘σ, and RI on both forces the same symmetry.

**N2. Under truth-directedness and RI, no two-world measure is non-monotone.** By TD, only S0={W}, S1={W,p}, S2={W,p̄} and S3={W,p,p̄} can be optimal. Their expected scores, relative to S0, are affine in c=C(u), with slopes s1>0>s2, s0=0, and s3∈(s2,s1). The bounds on s3 follow from TD for adding p̄ to S1 and p to S2.

Suppose p is in every optimum at c1 and in no optimum at c2>c1. Take A1 optimal at c1 and A2 optimal at c2. Then f_{A2}−f_{A1} is negative at c1 and positive at c2, so A2 has the larger slope. That forces A1=S3, A2=S0 and s3<0.

By the symmetry from N1, p̄ is then in every optimum at C(p̄)=c1 and in none at C(p̄)=c2. Equivalently, it is excluded at c'=1−c2 and required at c''=1−c1>c'. An optimum at c' lies in {S0,S1}, slope ≥0. An optimum at c'' lies in {S2,S3}, slope <0. By the same argument the latter must have the larger slope, which is a contradiction.

So without CI the threshold does not become non-monotone. It moves below 1/2, or it can fail to exist through ties. a5(4) agrees: 784 TD measures, 0 that are both symmetric and non-monotone.

**N3. P3 holds even at ties.** Suppose that on a given space p is required above τ_p and excluded below it. Let C(p)=τ_p. Move a little mass between p and its complement; this is possible because 0<τ_p<1. EA is continuous and the state space is finite. So the limits of the optima taken from above and from below are both optimal at C. Hence p is in some optimum and also outside some optimum, on every space. The every/some verdicts therefore agree across a coarsening whenever the thresholds agree.

**N4. Replacement witnesses for "CI cannot be dropped"** (a5(5)):
- **(a)** Separable with T_p=2, F_p=−1 for every p. It is TD, satisfies RI (0 violations), and violates CI. At C(p)=1/2 the unique optimum is {W,p,p̄}, so no τ_p∈(1/2,1) exists.
- **(b)** The pairwise tie measure. Each pair {q,q̄} scores 1 for believing only its true member, −2 for believing only its false member, and 0 for both or neither; believing W adds 1 and believing ∅ subtracts 1. It is TD (on 2 and 3 worlds), satisfies RI (0 violations), and violates CI. For C(p)∈(1/3,2/3) its optima are {W} and {W,p,p̄}, so no threshold exists. (b) also refutes claim 36.

**N5. Counterexample to the member-by-member reading of claim 25.** Let each member A_{B0} be separable with T=1, and F=−2 if B0 contains a designated proposition q, otherwise F=−1. Each member satisfies ME and BI in Theorem 2's sense. Yet Proposition 4's threshold for the last proposition is 2/3 or 1/2 depending on B⁻.

## Patch list (exact)

**P1 (required).** §6, paragraph after Theorem 4.
- Replace: "And a truth-directed two-world measure violating CI is non-monotone.[^5]"
- With: "And CI cannot be dropped: the separable measure with $T_p=2$ and $F_p=-1$ for every $p$ is truth-directed and satisfies RI, since its values survive coarsening, but it violates CI, and at credence $1/2$ its unique optimum contains both $p$ and $\bar p$, so no threshold in $(1/2,1)$ exists.[^5]"

Replace footnote 5 entirely with:

"[^5]: Non-monotonicity is not what fails without CI. Applied to the permutation of a two-world space, RI makes the verdict on $\{u\}$ at $C(u)=t$ equal the verdict on $\{v\}$ at $C(v)=t$. No truth-directed two-world measure with verdicts symmetric in this way makes $p$ optimal at one credence and excluded at a higher one. What fails is the location of the threshold, and sometimes its existence. Score each pair $\{q,\bar q\}$ separately: 1 for believing only its true member, $-2$ for believing only its false member, 0 for believing both or neither; add 1 for believing $W$ and subtract 1 for believing $\varnothing$. This measure is truth-directed and satisfies RI. Yet for $1/3<C(p)<2/3$, believing both members ties with believing neither, so $p$ is in some optima but not all, and $p$ has no threshold."

(The old fn 5 is arithmetically right, but its measure violates RI, so it cannot witness minimality.)

**P2 (required).** §6:
- Replace: "Neither repair yields invariance under every refinement, and no non-Lockean score can."
- With: "Neither repair yields invariance under every refinement, and no truth-directed, conservative non-Lockean score can."

**P3 (recommended).** §6:
- Replace: "That is the localization the Lockean needs, and accuracy adds only monotonicity on a two-world problem."
- With: "That is the localization the Lockean needs. On the two-world problem, truth-directedness and CI then supply a single threshold above 1/2."

**P4 (recommended).** §4, last paragraph:
- Replace: "for such a family, ME and BI imposed on each member yield fixed thresholds through Proposition 4 without collapsing the family into one separable measure."
- With: "for such a family, ME at each member's own state, together with BI read across the family (the increments $T^{B_0}_p$ and $F^{B_0}_p$ of $A_{B_0}$ at $B_0$ do not depend on $B_0$), yields fixed thresholds through Proposition 4 without collapsing the family into one separable measure."

**P5 (recommended).** Abstract:
- Replace: "For every positive premium and conservative values,"
- With: "For every positive premium and any conservative values shared by all propositions,"

**P6 (optional).** §6: delete ", except at ties" (N3 shows the equivalence holds at ties too).

**P7 (optional).** §6:
- Replace: "In general, splitting a world of credence zero"
- With: "In general, with the values of Section 3, splitting a world of credence zero"

**P8 (integrity, required before submission).** §5, the Leitgeb sentence ("On Leitgeb's theory (2014, 2017), stability with threshold 1/2 is equivalent to …"). Verify it against a retrieved copy of Leitgeb (2014), or delete it. Also have the Dorst–Mandelkern description and the Levi description in §5 checked by the citation-auditor. This audit did not check them.

No change is needed to Theorems 1–4, their proofs, the case, the refinement numbers, or the essay's statements of Dorst's principles.
