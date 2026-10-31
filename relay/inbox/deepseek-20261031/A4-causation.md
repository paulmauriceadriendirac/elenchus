# Referee report

**Manuscript:** “A Switching Dilemma for Normality in Actual Causation”
**Length:** 11 pp. (main text 1–9, appendix 9–11)
**Recommendation:** Major revision
**Confidence:** 3/5 (I verified the witness profiles, the gain identities, the preorder counts, and the Halpern citations; I did not have the author’s implementation, so the corollary’s claims about “part of a cause” and the Andreas–Günther computations are unchecked.)

---

## 1. Summary

Normality conditions are a standard way of stopping the Halpern–Pearl (HP) definitions of actual causation from counting a switch-flip as a cause. The paper asks whether a single *transferable* normality policy — “anonymous”, in the sense that it ranks a witness world only by the multiset of per-variable status transitions, whatever the variables represent — can keep genuine prevention and late preemption while excluding the standard switches, under all three HP definitions.

The main results are:

1. **Theorem 1** (p. 4): under event coding (occurrences deviant, absences default) and the *modified* definition, Suzy’s throw, the Tracks flip and the Doorbells switch each have exactly one witness world, and the three transition profiles are identical — `{root: deviant → default, n → f, l → n, l → n}`. Hence every anonymous filter admits all three or none.
2. **Theorem 2** (p. 4): under the *original* and *updated* definitions, the flip in Blocked tracks has the witness `[EF ← 0, LB ← 0]`, whose profile is genuine prevention’s witness plus one root moving from deviant to default; hence every anonymous Pareto filter that makes the antidote a cause makes the flip a cause.
3. **Corollary** (p. 5): under event coding, no anonymous Pareto filter keeps the antidote and Suzy’s throw, leaves Billy’s throw out of every cause, and excludes all the switches, under any of the three definitions.
4. **§5** (pp. 5–7): the non-anonymous escapes. One additive repair (mechanism-dependent scores for frozen defaults) works formally but depends on mechanism reliability; the Sprinkler and Seedlings cases show that this makes the verdict depend on reliability rather than preemption. The inertial coding of standing blockages rescues Theorem 2 at the cost of making the verdict depend on how long the blockage has stood.
5. **§6** (pp. 7–8): a lemma showing that, under the modified definition, exceptionless equation-conformity leaves only root but-for causes (so the ducking, the chain’s intermediate, and Suzy alone are lost), applied to Halpern and Hitchcock’s conjecture and to Xiao and Xiong’s definition.

The core observations are correct and elegant, and the paper is scrupulous about what it does and does not show. My main concerns are that the impossibility framing is thinner than the results that support it, that the paper’s contribution relative to Halpern (2015), Xiao and Xiong (2026) and Wysocki (2023) needs sharper statement, and that the computational claims are not reproducible as presented.

---

## 2. Assessment

**Strengths.**

- Theorem 1 is correct and genuinely interesting. The uniqueness of the modified witness is easy to miss, and the identity of the three profiles is the paper’s best result. I verified all three witnesses by hand, checking the witness conditions directly: Suzy `[ST ← 0, BH ← 0]`, Tracks `[F ← 0, LT ← 0]`, Doorbells `[T ← 0, L ← 0]`, all with profile `{R: dev→def, n→f, l→n, l→n}`.
- Theorem 2 is correct, including the AC2(b) check: restoring `EF = 1` with or without `LB = 0` gives `TA = 0`. The profile is exactly prevention’s (`{R: dev→def, n→l}`) plus one more `R: dev→def`.
- The additive identities are correct: `g_Doorbells = g_Tracks = g_Suzy = r + a − 2b + c = g_Chain + g_Boulder`, and `g_Blocked = g_Prevention + r`. The “compensation does not help” point follows immediately and is a nice way to make the profile identity bite for additive filters.
- The calibration analysis is right: the four calibration verdicts force `l ⪰ n`, `n ⪰ l`, `f ⪰ l`, `¬(u ⪰ l)`, and under those conditions the common profile passes. I reproduce the paper’s count exactly: 355 preorders on four categories, 5 satisfying all four calibration conditions, 2 of them total preorders.
- §5’s Sprinkler and Seedlings cases are the paper’s most philosophically interesting material. The Seedlings isomorphism is a strong test: any account that depends only on equations, actual values and event-coded defaults must treat the swarm as it treats the switch.
- The Halpern citations are accurate. I checked the arXiv version (1505.00162v1): the Schumacher attribution is on pp. 7–8 and “normality considerations don’t help” is on p. 8; “With the modified definition, this becomes a non-problem” is on p. 8; the clear-tracks witness `[F ← 0, LB ← 1]` is on pp. 7–8; and the quoted “the world where the train does not go on the left track despite the switch being set to the left is less normal than the actual world” is on p. 8.

**Weaknesses.**

- The anonymity theorem is nearly analytic once the profiles are identical; the paper’s real contribution is the profile identities. Leading with the impossibility invites the objection that the restricted class is a straw man.
- The relationship to known results is under-described. Theorem 2’s content is Halpern’s (2015, 7–8) observation (credited to Schumacher) and Xiao and Xiong’s (2026) Observation 1; the paper says so, but the abstract and §1 still present the dilemma as the news.
- Several claims rest on computations that are not available: the corollary’s claim that Billy’s throw is in no cause, the equivalence between Suzy’s being a cause and each switch-setting being “part of a cause”, and the Andreas–Günther checks.
- §7 (the parallel with Beckers) is peripheral and could be compressed.

---

## 3. Major comments

### 3.1 Reframe around the profile identities

The paper’s central insight is an *identity of witness profiles*: under the modified definition, Suzy’s only witness and the switches’ only witnesses have the same multiset of transitions; under the older definitions, the Blocked-tracks witness is prevention’s witness plus a default-restoring root change. The anonymity result is then a corollary, because a filter that sees only the profile cannot distinguish what has the same profile. As written, the abstract and §1 lead with the impossibility (“no anonymous normality filter…”), which makes the paper look as though it is attacking a class no one defends. Reframe:

1. State the identity theorems first (they are model-level facts about the HP definitions, independent of any filter).
2. State the anonymity/Pareto corollary as a corollary, with a sentence explaining that anonymity is the weakest precisification of “transferable”, not a characterization of any actual proposal.
3. Put the philosophical question — *which* additional information a separating policy must use — at the front, since that is what the paper actually establishes.

This would also make clear why the paper is not a straw man: the target is the project of using default status and equation conformity as the normality basis, not the particular implementations in Halpern and Hitchcock.

### 3.2 Sharpen the claim of novelty

The paper is candid that Halpern (2015) reports Schumacher’s problem, that Halpern (2016, 84–85) observes the modified definition’s Suzy issue, and that Xiao and Xiong (2026) show the same for the Halpern–Hitchcock definition. The “increment” list on p. 2 is good but too compact. A referee/editor will want a clear separation:

- **New:** the exact identity of Suzy’s sole modified witness with the two switch witnesses (Theorem 1); the exact identity of the Blocked-tracks witness with prevention plus a root (Theorem 2); the additive gain identities and the calibration count; the reliability critique (Sprinkler, Seedlings); the frozen-witness lemma (§6).
- **Known, restated:** that the original/updated definitions count the flip in Blocked tracks (Halpern 2015; Xiao and Xiong 2026); that the modified definition forces the frozen witness for Suzy (Halpern 2016); that normality cannot separate the cases in general (Wysocki 2023, stronger).

At present the paper sometimes presents the known parts as if they were new (e.g., the corollary reads as the headline), and sometimes gives away the new parts too quickly. A short table would fix this.

### 3.3 “Part of a cause” and the equivalence claim on p. 4

The computation paragraph says: “for componentwise filters, Suzy’s throw is a cause exactly when each switch-setting is part of a cause; and in every preorder that leaves Suzy’s throw part of a cause only through a conjunction, the conjunction includes Billy’s throw”. Please specify:

- whether “part of a cause” means “is a conjunct of some cause” (so that the relevant profiles are those of conjunctive candidates), and how AC3 interacts with the filter (the appendix says the filter is applied before AC3, which is the right convention, but it should be stated in the main text);
- whether the equivalence is asserted over all 355 preorders or only over those satisfying the calibration. As I reconstruct the profiles, Suzy’s conjunction `{ST, BT}` has profile `{R: dev→def, R: dev→def, l→n, l→n}` while Tracks’ conjunction `{F, LT}` has the *frozen* profile `{R: dev→def, n→f, l→n, l→n}`; the two are not obviously equivalent without the calibration assumptions. A reader cannot check this from the text.

On the natural reading (Suzy is a *single* cause, not merely a conjunct), I could not construct a counterexample, and the claim is probably right; the problem is that the reader cannot see which reading is intended. State it.

### 3.4 Reproducibility

The paper’s central claims lean on computation: 355 preorders, candidates of every size, 3,000 random additive scores, 400 random models, and the Andreas–Günther conditions with and without deviancy. None of this is available. For a paper whose appendix says the corollary “rests on the exhaustive computation”, a repository (or at least a precise pseudo-code appendix specifying the enumeration order, the filtering convention, and the random seeds) is necessary. This is also the only way for a referee to check the claim that Billy’s throw is in no cause, which is not derivable from the text.

### 3.5 Expand §5 and compress §7

§5 is the philosophically strongest section: it takes the most natural non-anonymous ground (mechanism reliability, as reported by Xiao and Xiong) and shows that it makes the verdict depend on reliability rather than preemption, with the Seedlings isomorphism as a sharp test. I would:

- expand the reliability discussion to state explicitly what a *successful* ground would have to look like (e.g., a principle that ranks frozen mechanisms by a property that is (i) independently motivated, (ii) not equivalent to “reliability”, and (iii) survives the Seedlings and Sprinkler tests);
- compress §7 into a paragraph or a footnote. The Beckers parallel is interesting but concerns a different literature and does not bear on the paper’s central claims; as written it invites the question of why the paper does not simply defer to Beckers and Wysocki.

### 3.6 The lemma in §6 needs a clearer statement of its dialectical role

The frozen-witness lemma is a nice independent result, and the application to Xiao and Xiong is appropriately hedged (“the theorem here concerns the explicit fixed-context reading, not every possible interpretation of availability”). But the paper should say more clearly what the lemma is *for*: it shows that one specific way of rescuing the modified definition (making equation-conformity exceptionless) has a steep cost, and it explains why the “explain away the exceptions” programme cannot by itself separate preemption from switching. As written, the lemma arrives somewhat abruptly, and the reader is left unsure whether it is a lemma in service of the main dilemma or a second paper. A short introductory paragraph would help, and the statement “with fixed context and non-intervened roots fixed” should be explained (the “non-intervened roots fixed” clause is redundant if the context is fixed; presumably it is meant to rule out background changes).

---

## 4. Minor comments

1. **Abstract (p. 1):** ~200 words, dense but clear. Consider replacing “one transferable normality policy cannot do this” with the precise claim (“no anonymous Pareto filter…”), since “transferable” is doing intuitive work that “anonymous” later makes precise.
2. **§1, p. 2:** “Beckers (2026, 2, 10–11) argues for a dilemma of related shape for the regularity theory of Andreas and Günther (2024), discussed in Section 7.” — Since §7 is peripheral, consider a footnote here and dropping the section.
3. **§2, p. 3:** the four categories are clear, but the phrase “frozen default” suggests an intervention; make explicit that only intervened variables can occupy `f` or `u` (otherwise a non-intervened variable conforms to its equation by construction).
4. **§2, p. 3:** “A root is at its default or not.” — say that root status is binary and that a root’s default is more typical than its deviant value (this is used silently in the Pareto condition).
5. **§3, pp. 3–4:** a table listing each case’s variables, equations, actual values and desired verdict would save the reader a lot of work, especially for Boulder, the short circuit, and Blocked tracks.
6. **§4, p. 4:** the profile notation `{root: deviant → default, n → f, l → n, l → n}` mixes a root transition with non-root transitions; use a uniform notation such as `{R: dev→def, n→f, l→n, l→n}` throughout.
7. **§4, p. 4:** “The calibrating cases already force the common profile.” — the argument that `f ⪰ n` follows from `f ⪰ l ⪰ n` is correct; say “transitivity” explicitly.
8. **§4, p. 5:** “The score `(r,a,b,c,d) = (2,0,−1,−5,−3)` does exactly this under both older definitions and also keeps prevention, the chain and the ducking.” I verified that the ducking is admitted under the older definitions via the witness `(F,B,K,H) = (0,1,0,1)`, whose gain is exactly 0 (and is admitted by the `≥` convention). Since this is a zero-gain case that a reader might miss, say so.
9. **§4, p. 5:** “But it counts the flip in Blocked tracks, and in Halpern’s model with clear tracks (via `[F ← 0, LB ← 1]`, gain `a − b`).” — I checked this: the two root changes cancel (`+r` for `F` returning to default, `−r` for `LB` moving to deviant), leaving `a − b = 1`. A parenthetical explaining the cancellation would help; otherwise the reader wonders where the roots went.
10. **§5, p. 6 (a real slip):** “In componentwise terms, the escape indexes the preorder by variable: `f ⋡ n` for the track and the left bell, while `f ⪰ n` for Billy’s hit and the ducking.” A componentwise filter, as §2 defines it, has *one* preorder applied to every variable. A preorder indexed by variable is not a componentwise filter in that sense — which is the point of the escape. The sentence therefore contradicts itself, and a reader who takes it at face value will think the paper’s own class can do something it has just proved it cannot. Fix: “In variable-indexed componentwise terms…” or “The escape indexes the componentwise order by variable…”. This does not affect any theorem, but it is the one place in the paper where the wording gives a false characterization of the result.
11. **§5, p. 6:** “the firefighter is part of a cause only together with the sprinkler’s activation, which is itself part of a cause” — clarify whether the sprinkler’s activation is a cause on its own, or only as a conjunct.
12. **§5, p. 7:** the inertials discussion is well done; one sentence on why the “how long has it been blocked” dependence is a *reductio* (rather than merely counterintuitive) would strengthen it.
13. **§6, p. 8:** “The argument adapts the elimination-and-minimality reasoning of Halpern’s (2016, 121, 133–134) stability theorem for conservative extensions to a single conforming witness.” — good; consider stating the correspondence in one sentence.
14. **Appendix, p. 10:** “In Boulder, the modified definition admits only `(F,B,K,H) = (1,1,0,1)`; the older definitions also admit `(0,1,0,1)`” — this is used in §4’s score verification; make sure the text and appendix agree on which witnesses are relevant to which claim (the modified-only witness requires `f ⪰ l`, while the older one requires `u ⪰ l`, and the calibration argument depends on this).
15. **References, p. 10:** the Halpern 2015 page references are to arXiv:1505.00162v1, and the paper says so. If the published version has different pagination, add a note.
16. **Typos:** none found in a scan; the prose is clean.

---

## 5. Verification notes (what I checked, and how)

**Witness profiles (Theorem 1).** I checked the witness conditions by hand and computed the profiles and gains with a script.

- **Suzy** (`ST=1, BT=1; SH=ST; BH=BT∧¬SH; BS=SH∨BH`): only witness `[ST←0, BH←0]`; categories `ST: dev→def`, `SH: l→n`, `BH: n→f`, `BS: l→n`. ✓
- **Tracks** (`F=1; LT=¬F; RT=F; A=LT∨RT`): only witness `[F←0, LT←0]`; `F: dev→def`, `LT: n→f`, `RT: l→n`, `A: l→n`. ✓
- **Doorbells** (`M=1, T=1; L=M∧¬T; R=M∧T; E=L∨R`): only witness `[T←0, L←0]`; `T: dev→def`, `L: n→f`, `R: l→n`, `E: l→n`. ✓

**Theorem 2.** Blocked tracks `(EF, LB, RB, TA) = (1,1,1,0)`, witness `(0,0,1,1)`; profile `EF: dev→def`, `LB: dev→def`, `TA: n→l`. Prevention witness `[A←0]`: `A: dev→def`, `V: n→l`. So Blocked = prevention + one root. AC2(b) verified: `[EF←1]` and `[EF←1, LB←0]` both give `TA = 0`. ✓

**Gain identities.** With `r, a, b, c, d` as defined: `g_Suzy = r + (c−a) + 2(a−b) = r + a − 2b + c`; `g_Chain = r + 2(a−b)`; `g_Boulder = (c−b) + (b−a) = c−a`; so `g_Suzy = g_Chain + g_Boulder`. ✓ `g_Blocked = 2r + (b−a) = g_Prevention + r`. ✓

**Score `(2,0,−1,−5,−3)`.** Prevention +1, chain +4, Boulder (older witness `(0,1,0,1)`) 0, short circuit −1, Suzy frozen −1, Suzy older +6, Tracks/Doorbells −1, clear tracks `a − b = +1`. This matches the paper’s claims, including that the ducking survives under the older definitions (via the zero-gain witness) while the switches do not. ✓

**Preorder count.** I enumerated all binary relations on four elements (65,536 candidates), filtered reflexive/transitive (355 preorders), and counted those satisfying `l ⪰ n`, `n ⪰ l`, `f ⪰ l`, `¬(u ⪰ l)`: exactly 5, of which 2 are total. ✓ This matches the paper.

**Halpern (2015) citations.** Checked against arXiv:1505.00162v1: the Schumacher problem on pp. 7–8 and “normality considerations don’t help” on p. 8; “this becomes a non-problem” on p. 8; the clear-tracks witness `[F ← 0, LB ← 1]` on pp. 7–8; the quoted comparison “the world where the train does not go on the left track despite the switch being set to the left is less normal than the actual world” on p. 8. ✓

**Not verified.** The full HP implementation, and hence the corollary’s claim about Billy’s throw; the 355-preorder equivalence claim on p. 4 (see 3.3); the 3,000 random additive scores; the 400 random models for the lemma; the Andreas–Günther computations; the Xiao and Xiong and Beckers citations (I did not have those texts).
