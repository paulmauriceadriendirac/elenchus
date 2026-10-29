# Formal audit — A6 v4 (`state/drafts/A6/v4.md`)

**Overall.** Every theorem, lemma, proposition and appendix proof holds. I checked each proof by hand and confirmed each one by independent exhaustive computation over all 594 labelled statist, comparable structures with up to four states. The worked finite examples reproduce exactly, and so do all but two of the Bjorn figures. **Two numbers are wrong or unsupported:** the 0.37 in §3 and the −0.63 in §5.1. **Three statements are imprecise:** the 2,322 population, "every partition", and the unspecified s0 in the five-state example. Two smaller wording issues follow (Lemma 2 cited for a continuous model; the encroachment generalization). Patches are at the end.

Independent code (mine, self-contained, rerunnable), in `state/audit/A6/formal/`:
- `finite_checks.py` → `finite_checks.out`: exhaustive structural checks plus exact-rational constructions. Runs in about 15 s.
- `examples.py` → `examples.out`: every worked finite example in exact rationals, the count reconciliation, and an independent VER random search.
- `bjorn_numeric.py` → `bjorn_numeric.out`: Bjorn figures by numpy quadrature, using `math.erf` and no scipy. Runs in about 3.5 min.
- `bjorn_51_precise.py` → `bjorn_51_precise.out`: the §5.1 figure by mpmath 1-D quadrature at 30 digits.

Enumeration conventions: ⪰ is a total preorder. ≫ is filtered directly by irreflexivity, ≫⊆⪰ and chaining; for n≤3, restricting ≫ to strict pairs was checked to lose nothing. E ranges over all non-empty subsets, x over E, and Π over all partitions of E.

The author's scripts `v4_verdict_example.py`, `v4_verdict_rule.py`, `v4_conditional_rules.py` and `bjorn_v4.py` were rerun from a scratch copy, and all four reproduce their recorded `.out` files byte for byte. They were used for comparison only.

## 1. Source match (Goodman & Salow 2023, `inbox/sources/goodman-salow-2023.txt`)

| Essay statement | Source | Status |
|---|---|---|
| ⪰ is a preorder; ≫ implies ⪰, is irreflexive, chains w1⪰w2≫w3⪰w4 ⇒ w1≫w4 (§2) | p.92, (i)–(iii) | VERIFIED |
| Comparability; Collapse (§2) | p.100 (COMPARABILITY: evidentially accessible ⇒ comparable; matches "same evidence" under transparency) | VERIFIED |
| B(E) = states nothing in E is ≫ (§2) | BELIEF, pp.112–113 | VERIFIED |
| K-normality K_E(x)=B(E)∪{v⪰x} "(2023, 104)" | p.104 | VERIFIED |
| "given TRANSPARENCY, K-NORMALITY entails KK" (2023, 107) | p.107, verbatim | VERIFIED |
| I- and KM-normality validate Margins, allow KK failures (§2) | p.111 ("I-NORMALITY entails MARGINS"); KM defined via MARGINS p.110; both rule out cliff-edge knowledge pp.105, 109. My example (`examples.out` 5b): I-normality KK failure in a statist comparable model | VERIFIED |
| Statism = evidence-independence of both relations (§2) | STATISM p.128 (also in G&S 2023, not only BRN) | VERIFIED |
| Bjorn model: δ=(w−y1)²+(w−y2)²; ⪰ iff δ no larger; ≫ iff smaller by more than c² (§3) | p.126 | VERIFIED |
| Relations derived from independent Gaussian errors "(2023, 129)" | p.129, four assumptions | VERIFIED |
| Belief after one reading [r−c,r+c]; after two readings, avg ± c/√2; belief = knowledge under K-normality when δ≤c² (§3) | p.126 | VERIFIED (ken {δ≤c²} also derived by hand) |
| "loses knowledge" when \|r−r′\|>(2−√2)c, first reading accurate "(2023, 127)" | p.127 (for ⟨x,x,y⟩ with \|x−y\|≤c) | VERIFIED |
| Readings may differ by up to √2c for all he believes | p.126 | VERIFIED |
| "about the scales' future readings" (130 n.40); current knowledge depends on the second reading | p.130 n.40; p.128 | VERIFIED |
| Probabilistic account of "sufficiently more normal" (2023, 121) | p.121 | VERIFIED |
| "together entail NO DEFEAT" (2023, 128) | p.128, verbatim; also checked exhaustively for I and KM (n≤4): no failures | VERIFIED |
| G&H 2022 predict failures of No Defeat "even given MARGINS" (130 n.40); relativizing to *how much does Bjorn weigh* gives a G&H-like model with no sensitivity to future observations | p.130 n.40 | VERIFIED |
| Statism holds only for the bodies of evidence considered (138 n.47); testimony discoveries (§8) | p.138 n.47; pp.137–138 | VERIFIED |
| BRN claims (Preservation results; §5 n.18 c≈1.96 and 0.37; App. D.3 conditional belief; §7 quote); Geanakoplos 2002 Thm 1; Salow 2025 quotations | not in `inbox/sources/` | UNVERIFIED (source unavailable; for the citation audit) |

## 2. Claims table

Status key: **VERIFIED** (proof checked by hand and/or code). **FALSE** (counterexample or mis-computation given). **UNVERIFIED** (reason given).

| # | Claim | Location | Verification | Status |
|---|---|---|---|---|
| 1 | Lemma 1 (defeat is costly), V ≤ −Pr(s0\|M)<0 | §4 | Hand. Also embedded in the 6,612 Thm 3 constructions | VERIFIED |
| 2 | Lemma 2 (laminar sufficiency), proof A.1 | §4, A.1 | Hand: maximal kens partition M; induction on \|C\| is sound. Hypotheses checked structurally on all 78,675 no-defeat pairs; 11,691 random problems, 0 negative | VERIFIED (finite) |
| 3 | Lemma 3 (kens reflexive, transitive, nested), A.2 | §4 | Hand; exhaustive over every F (0 failures) | VERIFIED |
| 4 | Theorem 1(a): safe iff no relative defeat | §4, A.3 | Hand; exhaustive structural check plus explicit Lemma-1/Thm-3 bets on all 3,306 defeat pairs | VERIFIED |
| 5 | Theorem 1(b): gapped ⇒ all questions safe; not gapped ⇒ some p_v question unsafe | §4, A.3 | Hand; exhaustive. Every qualifying v works, not just some | VERIFIED |
| 6 | Lemma 4 | §4 | Hand; asserted in code for every case | VERIFIED |
| 7 | B ⊆ M for K, I, KM, JTB, iterated knowledge | §4 | Exhaustive (also iterated I) | VERIFIED |
| 8 | Theorem 2 and "gapped set ∋ x contains C(x)", A.4 | §4 | Hand; exhaustive for K, I, KM, JTB, KK, II and random factive B-containing assignments; all subsets for C(x) | VERIFIED |
| 9 | Three-state model: Preservation holds for all E and discoveries; at b ken {a,b}; learning ¬a reopens c | §4 | `examples.out` (1) | VERIFIED |
| 10 | Corollary (i) (collapse ⇒ gapped), A.4 | §4 | Hand; exhaustive over 92 collapse structures | VERIFIED |
| 11 | Corollary (ii) (finite graded: all p_v safe only if M=E) | §4 | Hand; exhaustive on graded E for all rules above | VERIFIED |
| 12 | Bjorn evidence after one reading is graded | §4 | Hand (chain of δ-steps ≤ c²) | VERIFIED |
| 13 | {\|μ\|≤1000} is factive, B-containing, not gapped; second weighing safe for it | §4 | Hand. The conclusion is true: on each d-line the kens are nested intervals {\|μ\|≤m}. V(m)=max_a∫_{I_m}u_a is absolutely continuous, and the plan's value has the same a.e. derivative (Danskin), so the plan equals the max on each line and Σ_d max ≥ max Σ_d. But Lemma 2, as proved, is finite | VERIFIED (citation of Lemma 2 needs "continuum analogue": patch P6) |
| 14 | Theorem 3 and A.6 (CEU strictly prefers acting now; KDT negative; all pairwise differences everywhere; later choices = KDT; open neighbourhood) | §5.2, A.6 | Hand (every inequality of A.6 checked). Exact construction on 3,306 pairs × 2 priors = 6,612: all pass, no ties anywhere | VERIFIED |
| 15 | Three-state illustration: 1.2 now; look policy (β, decline, decline); 0.5; CEU prefers acting now by 0.7 | §5.2 | `examples.out` (2) | VERIFIED |
| 16 | CKD silent in the constructed problems; CKD never forbids a free look when look and a differ everywhere (A.7) | §5.2, A.7 | Hand; 6,612 constructions plus 14,930 random tests, 0 violations | VERIFIED |
| 17 | VER escapes Theorem 3 for large L | §5.2 | Hand proof: the ⪰-maximal member of D_dec is either excluded or has a reopened w∈B(E∩D_dec). Code: excluded state present in 6,612/6,612; VER prefers acting now 0/6,612 with A.6's L; prefers looking 6,612/6,612 with 1000L | VERIFIED |
| 18 | Five-state VER example: ken {a,s1,s2}; both answers reopen; policy β at a, decline elsewhere; conditional ken {s1,s2,v2}; β1 EV 0.028; VER prefers acting now by 0.008; primitive acts differ everywhere | §5.2 | `examples.out` (3): true **with s0=s1** (0.0281, −0.0082). With s0=s2, β1 is not chosen now and β1's EV is 0.018. The essay does not say which | VERIFIED with s0=s1 (patch P3) |
| 19 | "1,724 of the 2,322 situation–question pairs with relative defeat" | §5.2 | 2,322 = defeat pairs with **E = whole S only** (my count agrees); the essay's own Computations paragraph gives 3,306 for every E. 1,724 reproduces with the author's seeded search. My independent search (150 trials/pair, exact re-verification) finds VER disvaluing in **2,222** of 2,322 (2,152 with generic acts only). So 1,724 is a search-dependent lower bound | Imprecise (patch P4) |
| 20 | Four-state example without relative defeat: ken {a,x}; KDT 0.05; conditional ken {x,b}; VER and CEU prefer acting now | §5.2 | `examples.out` (4): KDT 0.0500; CEU −2.45; VER −1.225; chaining valid | VERIFIED |
| 21 | K^D = post-discovery ken when x∈D (statism); contains post-discovery belief | §5.1 | Hand | VERIFIED |
| 22 | Proposition 4 (ANS never prefers acting now) | §5.3 | Hand; structural inclusion check on all pairs; 36,821 random (problem, act) tests, 0 negative | VERIFIED |
| 23 | Proposition 5 and A.7 bound κ < Pr(c0\|K)(Lq−1); options differ everywhere; β better throughout ken; CKD requires β | §5.3, A.7 | Hand; 6,612 exact constructions (κ = half the bound) | VERIFIED |
| 24 | §5.1: look and bet differ exactly on the decline set; "bet's EV on that hypothesis is −0.63" | §5.1 | Correct region (inf_D δ = d*²/2; no declining states with \|μ\|>c/√2 inside the bound): **−0.602** (mpmath) / −0.601 (grid). The author's −0.626 is a coarse-grid artefact (grid min of δ over D overshoots d*²/2). Sign and conclusion (CEU, VER, ANS look) hold | FALSE as stated: −0.60 (patch P2) |
| 25 | Bjorn ken after reading 1 = {δ ≤ max(c²,δ(x))}; post-answer ken \|μ\| ≤ max(c/√2,\|μ_s\|); μ~N(0,½), d~N(0,2) independent; δ=2μ²+d²/2 | §3, A.5 | Hand | VERIFIED |
| 26 | Preservation fails at every nonzero difference ≤ √2c, probability ≈ 0.95 | §3 | Hand (B(E∩p) ⊆ B(E) iff r=r′); 2Φ(c)−1 = 0.9500 | VERIFIED |
| 27 | "costs him a belief about his weight with probability about 0.37, as BRN estimate" | §3 | Under the essay's own model (c=1.96, swamped Gaussian), losing a weight belief ⇔ \|d\|>(2−√2)c. Probability **0.417** unconditionally, **0.356** given δ≤c², 0.251 given an accurate first reading. 0.37 corresponds only to c≈2.17. BRN unavailable | UNVERIFIED; conflicts with own model (patch P1) |
| 28 | Ten-to-one: decline iff readings differ by more than about 1.12c; probability ≈ 0.05 given knowledge; KDT value ≈ −0.05; 20:1 −0.12; 100:1 −0.27 | §3 | d* = 1.1202c; −0.0496; −0.1207; −0.2738 | VERIFIED |
| 29 | Fallibilist EV 0.95 − 10(0.05) = 0.45; second weighing has positive value for her | §3, §6.2 | 0.4500; Bayesian value +0.1855 | VERIFIED |
| 30 | c² = −2ln(1−t); c≈1.96 ↔ t≈0.85; t=0.95 ↔ c≈2.45; at t=0.95 ten-to-one ≈ −0.01, hundred-to-one ≈ −0.15 | §3 | Derivation for χ²₂ by hand plus Monte Carlo; t=0.8535; c=2.4477; −0.0099; −0.1539. The map applies to the two-error (first-reading) evidence, as used | VERIFIED |
| 31 | (i) at every situation some state bet makes the second weighing harmful; A.5 positive-measure argument (U open, η>0, L>(1−η)/η) | §3, A.5 | Hand (every step). Numerically negative at R = c², 3c², 5c², and at 7c² (where \|V\| < 1e−5) | VERIFIED |
| 32 | (ii) a reopened weight exists only if max(c²,δ(x)) < (1+√2)²c²; Cauchy–Schwarz bound; reach c/√2+√(R/2); probability ≈ 1.4×10⁻⁵ | §3, A.5 | Hand (A.5 actually proves iff). Grid reach matches formula; weight-bet value 0 beyond the threshold; e^{−(1+√2)²c²/2} = 1.37×10⁻⁵ | VERIFIED |
| 33 | ANS pays up to 0.019 (10:1) and 1.23 (100:1) | §5.3 | 0.0187; 1.2258 | VERIFIED |
| 34 | ANS restricted to free questions: looks at price 0, refuses at every positive price (KDT or CKD for costly inquiry) | §5.3 | Hand: KDT value −0.05−κ<0; under CKD, D=E, so bet is better throughout the ken | VERIFIED |
| 35 | Margins completions: relative defeat in Thm 2 is a KK failure at x; empty question harmed without KK; K-normality: empty question never negative, can be positive at abnormal situations | §6.1 | Hand; exhaustive (every I/KM defeat is a KK failure; K never fails KK); `examples.out` (5a): +0.5 | VERIFIED |
| 36 | Rescaling preserves choices and sign of information value | §6.2 | Hand (linearity) | VERIFIED |
| 37 | Encroachment, Bjorn: bet accepted at probability 1 or 0.95; with a free scale, indifferent at 1, strict preference to look at 0.95 | §6.2 | #29 plus hand | VERIFIED |
| 38 | "By the reasoning of Corollary (ii) … every factive, belief-containing state short of the evidence faces some offer … that removes it in the same way" | §6.2 | Needs a question that shifts Pr(E∖M), so the bet alone is accepted but the free question has strictly positive Bayesian value. For p_v questions this fails when Pr(E∖M\|p_v) = Pr(E∖M). Holds generically, not proved | Argued only (patch P7) |
| 39 | Commitment: present best act available, so a free signal cannot hurt | §6.4 | Hand | VERIFIED |
| 40 | "64,004 situation–question pairs; 3,306 with relative defeat" for "every … partition" | Computations | My count: 81,981 pairs with all partitions. 64,004 = **non-trivial** partitions only (17,977 trivial). 3,306 is unchanged (trivial partitions never defeat under K-normality, by KK) | Imprecise (patch P5) |
| 41 | Abstract/intro restatements of Thms 1–3, Props 4–5, Cor (ii) | Abstract, §1, §7 | Match the theorems, except the abstract omits "finite" for graded models | VERIFIED (patch P8) |

## 3. Patch list (exact replacements in `state/drafts/A6/v4.md`)

**P1** (§3, para. 3; medium):
- Old: `With Gaussian errors the second reading costs him a belief about his weight with probability about 0.37, as BRN estimate (§5, n. 18).`
- New: `With Gaussian errors the second reading costs him a belief about his weight with probability about 0.42 (about 0.36 conditional on what he now knows).`
- Alternatively, keep a BRN attribution only after checking BRN n.18 and stating its exact conditions. Re-check word count.

**P2** (§5.1, last para.; low):
- Old: `at ten-to-one the bet's expected value on that hypothesis is $-0.63$`
- New: `at ten-to-one the bet's expected value on that hypothesis is $-0.60$`

**P3** (§5.2, VER example; low–medium):
- Old: `Use Theorem 3's acts with $N=10$, $\varepsilon=0.001$, $L=30.4$.`
- New: `Use Theorem 3's acts with $s_0=s_1$, $N=10$, $\varepsilon=0.001$, $L=30.4$.`

**P4** (§5.2; medium):
- Old: `random priors and problems made VER disvalue the question in 1,724 of the 2,322 situation–question pairs with relative defeat.`
- New: `random priors and problems made VER disvalue the question in at least 1,724 of the 2,322 situation–question pairs with relative defeat in which the evidence is the whole state space.`
- If `state/audit/A6/formal/examples.py` is adopted into the candidate's checks, use `in 2,222 of the 2,322` instead.

**P5** (Computations; low):
- Old: `every body of evidence, situation and partition (64,004 situation–question pairs; 3,306 with relative defeat)`
- New: `every body of evidence, situation and non-trivial partition (64,004 situation–question pairs; 3,306 with relative defeat)`

**P6** (§4, end of Corollary discussion; low):
- Old: `so by Lemma 2 the second weighing is safe for it.`
- New: `so by the continuous analogue of Lemma 2 (on each line of fixed reading difference the kens are nested intervals) the second weighing is safe for it.`

**P7** (§6.2; low):
- Old: `every factive, belief-containing state short of the evidence faces some offer of a free question and a bet that removes it in the same way.`
- New: `every factive, belief-containing state short of the evidence faces, for all but knife-edge priors, some offer of a free question and a bet that removes it in the same way.`

**P8** (Abstract; low):
- Old: `and in graded models no factive state that contains rational belief is safe unless it is the whole evidence.`
- New: `and in finite graded models no factive state that contains rational belief is safe unless it is the whole evidence.`

No other mismatches were found between the essay's numbers, formulas or statements and verified proofs or code.
