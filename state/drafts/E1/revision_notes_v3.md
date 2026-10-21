# E1 revision notes (v2 -> v3), responding to referee report S2 (P-cbf4)

Sources: the full text of G&S 2023 (inbox/sources/goodman-salow-2023.txt). Page numbers are journal pages, equal to the PDF page plus 88. Figure 4 was checked by rendering PDF p. 31 at 300 dpi.

Every factual or formal claim the referee made was rechecked before I acted on it. Methods: the source text, check.py, hand proof.

## 1. Triage

### 1a. Single most serious problem and major findings

**Most serious problem: the "no-addition" direction of COMBINATION is unestablished, and "presupposes" is wrong.**
- **Verdict:** fixable; the referee is right.
- **Check:** G&S 117–118 is anti-skeptical; it is about knowledge *removed*.
- **Check:** K's single-respect knowledge is B_d ∪ ↑w_d. Proved as Prop 3(a) and checked over all 5,949 product structures.
- **Response:**
  - Dropped "presupposes".
  - Conceded in the text that K fully meets G&S's independence demand (§4, end).
  - COMBINATION is no longer a premise. It is shown equivalent (Prop 4) to SEPARATION, a Gettier principle drawn from G&S 113–114.

**(ii) The §6 costs are generic.**
- **Verdict:** mostly right.
- **"First" cost:** restated COMBINATION. Dropped.
- **"Third" cost (loss on discovering the antecedent):**
  - It is generic. Checked: in a discretized 1-D model, knowledge that the error is at most e is lost on discovering that the error is at least c. The discrete analogue of the referee's c ≤ e < 2c is c ≤ e < 2c−1, because there R_B' = {c..2c−1}.
  - Now mentioned only as not relied on (§5).
- **"Second" cost (Gettier shape):** generic only under the trivial decomposition R_B ∨ (p ∧ ¬R_B), which holds for every completion. v3 isolates what is distinctive:
  - (a) The agent does not know ↑w and has no single-respect cliff-edge knowledge. Under COMPARABILITY, Lemma 1 shows that K's knowledge outside belief is always ↑w.
  - (b) The disjuncts concern disjoint respects.
- **"Fourth" cost:** false. Removed and corrected.

**(iii) The essay's own exit (K together with probabilism) reproduces the verdict.**
- **Verdict:** right.
- **Response:** v3 confronts the K-probabilist (§6). The joint K verdict at (0,2) is ↑(0,2), which is ordinary cliff-edge knowledge in a total order. So it differs in kind from the product case.

**Major 1: "No other view / no probabilist context agrees".**
- **Verdict:** right; the claim was false.
- **Verified by computation:**
  - joint R_B = {(0,0),(0,1),(1,0)};
  - joint K(0,2) = six situations = ↑(0,2), which excludes (1,2), (2,1) and (2,2);
  - joint I and KM exclude only (2,2);
  - the question that singles out {(1,2)} excludes (1,2) under I, K and KM.
- **Response:**
  - Corrected in §6.
  - The choice of normality structure is kept separate from the choice of completion throughout §§6 and 8.
  - Added the symmetric corollary, Cor 6(b): meet = ∩ of the single-respect K contexts. Checked on figure 5 and on 200 random models.

**Major 2: the Gettier and NO DEFEAT points are generic.**
- **Verdict:** fixable.
- **Response:** recast, as the referee suggests, as a problem for G&S's CONVEXITY reply to Williamson (113–114). It is now the centre of the essay.
- **New finding, checked:** at (0,2) and (2,0) of figure 4, K = JTB = R_B ∪ {w}, and JTB satisfies CONVEXITY there.
- **Calibration:** v3 does not claim G&S assert that CONVEXITY is sufficient. It claims their reply does not protect K beyond COMPARABILITY, and that the cases fit a "nesting" refinement of the disjunctive diagnosis. The refinement is labelled open.

**Major 3: COMBINATION vs FACTORIZATION; the §9.3 inconsistency; scope.**
- **Verdict:** right.
- **Response:**
  - COMBINATION was reformulated: it is anchored to sets of respects that contain a respect outside belief.
  - With this formulation, meet is the knowledge default under COMBINATION for *any* number of respects (Prop 5(d)). Checked on all families, including 2×2×3. FACTORIZATION is no longer used, so the §4/§9.3 inconsistency is gone.
  - The new COMBINATION permits knowing "not both odd" at (0,0).
  - Scope is restricted to independent subject matters. n. 37 is now represented in full, including "wrongly predicts", with Goldstein and Hawthorne cited.

**Major 4: Prop 3 fails when R_B = ∅, and the proofs are sketches.**
- **Verdict:** right.
- **Verified:** with an integer respect where x ≫ y iff x ≥ y+2, R_B = ∅ and v2's meet is empty, so FACTIVITY fails. Checked with z3, using quantifiers.
- **Response:**
  - Adopted the referee's repaired definition, ↑w ∪ {…}. z3 confirms that repaired meet = K = ↑w there.
  - Props 3–5 now state R_B ≠ ∅ explicitly where it is needed.
  - Full proofs are given for every result.
  - z3 checks were added for an infinite well-founded respect (the naturals × figure 4): Thm 2, the meet box, and the Prop 3 condition.
  - On non-product cells, meet is undefined where glbs fail. Example: E − {(1,1)} at (0,1). This is checked and stated as a limit.

**Major 5: novelty miscalibrated.**
- **Verdict:** right.
- **Response:**
  - Cor 6 is now presented as a sharpening of G&S 121–123.
  - G&S's hedges at 111 are quoted, and the abductive point is called modest.
  - The "reduction to agglomeration" is no longer claimed as new.

### 1b. Top five changes

**Change 1: lead with a point that needs no COMBINATION.**
- **Verdict:** adopted, partly.
- **Check:** on products, KM = {v : w ≫̸ w∧v} = {v : no d with w ≫ w[d↦v_d]}. Proved as Theorem 2 and checked on all families.
- **Bearing on simplicity (111):** real, but conditional. It works only if simplicity is assessed on the structures where COMPARABILITY fails. v3 states that reply and answers it (§8).
- **What v3 leads with instead:** the Gettier/CONVEXITY point, which is the stronger result needing no COMBINATION. COMBINATION is then derived from it (Prop 4) rather than assumed.

**Change 2: correct which views agree with K; confront the K-probabilist.**
- **Verdict:** adopted (§6, Cor 6).

**Change 3: rebuild §6 around what is distinctive.**
- **Verdict:** adopted (§5).

**Change 4: repair the formal statements.**
- **Verdict:** adopted (Props 3–5, the repaired meet, full proofs, non-product cells, n. 18).

**Change 5: recalibrate the novelty claims and engage the literature.**
- **Verdict:** recalibration adopted. Literature adopted only in part, for two reasons:
  - KK literature: cited only via G&S 107 n. 16 and n. 17. Most of those works are known in L3 at title or abstract level only, and words were short.
  - Splitting / belief-revision literature: not cited. Parikh 1999 came back NOT_FOUND in verify_refs and I had no copy, so I did not attribute it, even impersonally.

### 1c. Minor problems

**"Carries the framework's verdict on KK."** Fixed in §2: MARGINS bears on KK in one direction only (107, n. 17).

**The "single-dimension rationale" for K.** Replaced by G&S's own rationale: the minimal change (104) and the knowledge default (110).

**The consumer-grade quotation.** Dropped.

**The opaque 9.1 condition.** Now stated exactly. SEPARATION allows knowing at (0,0) that not both are odd, and forbids excluding (1,2) at (0,2) while (1,1) is open.

**Page reference for KM ⇒ MARGINS.** Corrected to 108–110.

**Origins of K and I.** Stated correctly in §1.

**n. 18.** Meet is positioned against those completions in §7.

**"Must adopt."** Removed. Meet is offered as one option among three (§8).

**Cleaner global statement.** Used in Theorem 2.

### 1d. "Claims that look false"

**Items 1–6 and 8.** All fixed as described above.

**Item 7, the figure-4 double arrow.** Verified by rendering the PDF. The arrow from (0,2) to (1,2) is double.

## 2. What changed and why

**New thesis and structure.** The case against K no longer rests on COMBINATION. It rests on a Gettier verdict that G&S themselves endorse in general form (113–114), applied where it is non-trivial: disjuncts about disjoint respects.

**New formal results.**
- **Lemma 1.** K's disjuncts nest under COMPARABILITY.
- **Prop 3, completed.** Single-respect projections; the exact condition for an active disjunction; the canonical Gettier disjunction (G); non-product.
- **Fig. 4 fact.** K = JTB at the single-malfunction situations.
- **Prop 4.** SEPARATION ⟺ COMBINATION. Checked by brute force over all disjunctions: 26,730 relation–situation pairs, including random relations.
- **Prop 5.** Meet, repaired, with full proofs. The knowledge default under COMBINATION for any number of respects.

**Simplicity point.** Moved to §8 as a consequence.

**Probabilist.** Corrected, and the K-probabilist confronted.

**Removed:**
- the four §6 "costs";
- FACTORIZATION;
- the 2×2 table (the counts are kept in check.py);
- the claims about the probabilist's "reduction" being new.

## 3. v3 thesis (one sentence)

On Goodman and Salow's multi-dimensional model of independent sources, K-normality has a disjunction that is idle wherever COMPARABILITY holds. On these structures it becomes active and credits knowledge of Gettier disjunctions: a justified false belief about one source joined to an unknown truth about another. This knowledge is not cliff-edge knowledge and is not excluded by CONVEXITY. So G&S's CONVEXITY reply to the disjunctive diagnosis protects KM-normality there (KM becomes non-disjunctive) but not K-normality. The principle banning such knowledge is equivalent to combination, and imposing it on K's knowledge default yields meet-normality, which keeps KK.

**Does it survive without COMBINATION?** Yes. COMBINATION is now a consequence, via Prop 4, of generalizing the Gettier verdict, not a premise.

## 4. Increment over Goodman & Salow 2023

G&S already supply the completions, the multi-dimensional model, figure 4 (which depicts K's verdict without comment), the CONVEXITY reply to Williamson, and the context-by-context probabilist reply. v3 adds:

1. **Lemma 1.** The nesting of K's disjuncts under COMPARABILITY.
2. **Theorem 2.** The non-disjunctive form of KM on products (and the Carter–Goldstein form, as reported in n. 30, falls out).
3. **Prop 3 and the fig.-4 fact.** The exact condition under which K credits Gettier knowledge across sources; K = JTB at (0,2); hence G&S's reply does not protect K beyond COMPARABILITY.
4. **Prop 4.** SEPARATION ⟺ COMBINATION, which motivates the no-addition direction independently of the anti-skeptical argument.
5. **Prop 5.** Meet-normality, the knowledge default under SEPARATION.
6. **Cor 6.** A sharpening of G&S 121–123, in both the KM and the K versions.
7. **§8.** A modest consequence for the hedged abductive link at 111.

## 5. Three weakest remaining points

**1. The intuitive base of (P1)/SEPARATION.**
- The Gettier verdict in *Thermometer* is an intuition. A K-theorist can bite the bullet.
- The same intuition arguably condemns the K-probabilist's joint exclusion of (1,2). v3 classifies that exclusion as cliff-edge knowledge. So much weight rests on the claim that the product-case knowledge is "not cliff-edge knowledge".
- The probabilist's joint "not both bizarre" also violates SEPARATION. The reply (9.3) restricts SEPARATION to knowledge not licensed by INDUCTIVE KNOWLEDGE, and leaves joint contexts open.

**2. The simplicity reversal (§8).** It assumes simplicity is assessed on the class of structures where COMPARABILITY fails. G&S may mean simplicity of general definitions.

**3. Scope and prior art.**
- Meet-normality is undefined on cells without meets. Such cells arise from discovering cross-respect propositions. The logic of the general knowledge-default version (transitivity, KK) is unexamined.
- Carter & Goldstein 2021 is still known only through G&S n. 30. Williamson 2015 is known only through G&S's one-sentence report at 113. Either may anticipate parts of the nesting/Gettier point; a fetch request would settle it.

## 6. Word count and checks

- **Word count** (`tools/wordcount.py`): 5,797 strict, limit 6,000. This is above CONFIG's target of 5,600 but within the 5,200–5,800 range set for this revision.
- **`check_injection.py`:** no hard flags.
- **`check.py`:** ALL CHECKS PASSED, run time about 3.5 min. The v2 checks are preserved in check_v2.py. Coverage:
  - 5,949 product structures;
  - 3,594 comparable structures;
  - brute-force SEPARATION over 310 structures;
  - figures 4 and 5 and 200 random probabilist models;
  - discovery in 2-D and 1-D;
  - the non-product cell;
  - z3: Theorem 2 on arbitrary 3×3 structures; a non-well-founded integer respect (R_B = ∅); and a well-founded infinite respect (the naturals).

## 7. References: new, and how verified

**Gettier 1963**, *Analysis* 23: 121–123.
- `verify_refs.py`: VERIFIED (doi 10.1093/analys/23.6.121).
- Content (Case II: Ford / Brown in Barcelona) checked against an open-access transcription (ditext.com, from *Analysis* 23 (1963)). Only the case is described; nothing is quoted.

**Williamson 2015**, "A Note on 'Gettier Cases in Epistemic Logic'", *Phil. Studies* 172: 129–140.
- `verify_refs.py`: VERIFIED (doi 10.1007/s11098-014-0357-1; online 2014, vol. 172 2015).
- Content attributed only as G&S report it (113). Matches G&S's reference list.

**Parikh 1999.** NOT_FOUND. Not cited.

**Retained from v2:** Carter & Goldstein 2021; Goldstein & Hawthorne 2022; Goodman & Salow 2018, 2021, 2023. All are VERIFIED in L3. Carter & Goldstein and Goldstein & Hawthorne are cited only for what G&S report of them.

**Web fetches used:** 2 of 6. The fitelson.org PDF was an unreadable scan; the ditext.com transcription was used.

**Verbatim quotations in v3**, all checked against the text file, at pp. 104, 110, 111 (several), 113, 113–114, 114, 114 n. 23, 117 (three), 118, 119, 129 n. 37 ("wrongly predicts").
