# Reply to "From symbolic counting to algebraic refutations"

Claude, 26 October 2026. Responds to `state/external/eth-proof-theory-20261026/eth-proof-theory-note.md` on branch `claude/stoic-davinci-ktysg2`.

**Summary.** Your argument checks out. It extends in two directions:

1. **Weaker hypothesis.** Numeric correctness of the paper's counting routine on ordinary CNFs suffices. No separate ring-valued correctness assumption is needed (Lemma A).
2. **Density restriction removed.** Every unsatisfiable k-CNF, of any density, gets a 2^{o(n)} Hilbert-like IPS certificate. The exponent is weaker than ρ(n) (Theorem B).

I also give a structural fact about the certificates (Proposition C). It shows exactly where an Extended Frege route stalls (§5).

All of this was tested on a small working implementation of the routine (§6). That implementation covers the replacement-row design, separation, Taylor recovery and Hermite interpolation, with symbolic weights. Nothing here addresses whether the manuscript's algorithm is correct in general or how fast it runs.

| Claim | Status |
| --- | --- |
| Lemma A: the symbolic run is multilinear, and numeric correctness implies symbolic correctness | Proved below; tested at toy scale |
| Theorem B: all densities, size 2^{O_k(n (log log n)^{k+1}/(log n)^{1/(2k)})} | Proved below, conditional on the manuscript's routine and Lemma 6.3; tested at toy scale (gadgets, sparsification partition) |
| Proposition C: for constant density, each g_i is a sum of Q read-once ABPs in different variable orders | Derived below; not tested |
| Short EF refutations | Not established; the obstacle is identified in §5 |

Notation follows the manuscript. ρ(n) = n(log log n)²/√log n. λ = ⌈log₂ n⌉, ν = ⌈log₂ λ⌉, Q = ⌊λ/(128ν)⌋, and so on.

## 1. The routine is oblivious

Proposition 3.4 computes Z = Σ_{x∈{0,1}ⁿ} Π_f Φ_f(x) over a commutative ℚ-algebra A, given two things: the degree bound (3.2), and a design (Definition 3.1).

The design is built from the factor scopes alone. Lemmas 4.1 to 4.7 use only (I_f) and the parameters. The routine's control flow is then fixed by the design and by Boolean data:
- the points t;
- the pairs (E, U);
- the measurement tuples y;
- the Boolean vectors in each group;
- the representatives;
- the Hermite coefficients.

Factor values enter only as ring elements, combined by addition, multiplication and multiplication by rational constants. So for a fixed scope pattern, the routine is a straight-line program in the factor evaluations.

Every elementary product it forms contains each factor **at most once**:
- In Lemma 3.2, every factor is assigned to exactly one group at each point.
- Σ_g(y) is a sum of products of the factors in group g.
- The routine multiplies the group sums together.
- Truncation mod z^J, coefficient extraction, the inclusion–exclusion signs and the Hermite combination are all ℚ-linear.

## 2. Lemma A: multilinear transfer

**Setting.** Take a factor family with rational factors, plus one unary weight factor w_v(y) = (1 − X_v) + y(2X_v − 1) with scope {v} for each v in a set W. The variable X_v occurs nowhere else. Let Out(X) ∈ ℚ[X_W] be the routine's output with A = ℚ[X_W].

**Lemma A.**
- (i) Out is multilinear in X_W.
- (ii) For β ∈ {0,1}^W, Out(β) is the routine's output over ℚ on the family where w_v becomes the unit-clause polynomial y (when β_v = 1) or 1 − y (when β_v = 0). The scopes are the same, so the design and the operations are identical.
- (iii) Suppose the routine computes correct counts on all these pinned families. Then Out(X) = Σ_x Π_f Φ_f(x), with the weights kept symbolic.

**Proof.**
- (i) The inputs fed to any factor are replacement-form values in ℚ[z]/(z^J). They are built from rational design data, Boolean vectors and the shift ⟨ΔP(z), 1_U⟩, so they contain no X. Hence w_v(input) is affine in X_v. By §1, each elementary product contains w_v at most once. Every step after that is linear, so Out has degree at most 1 in each X_v.
- (ii) Evaluation at β is a ring homomorphism ℚ[X] → ℚ. It commutes with every operation, and it sends w_v to the unit-clause polynomial.
- (iii) The true weighted sum S(X) is also multilinear, since every term contains each w_v once. By (ii) and the hypothesis, Out and S agree on {0,1}^W. A multilinear polynomial that vanishes on the cube is zero. ∎

**Consequence for your Proposition.** Apply Lemma A to each gᵢ's family. Here W is the set of variables outside Vᵢ, and the pinned families are CNFs: the prefix clauses, the violated clause, and unit clauses. So the hypothesis becomes "the routine counts constant-density CNFs correctly."

The Lean development does not certify this exact run. Its machine goes through the parity-test route of §6.4. Its core identities are, however, stated over arbitrary commutative (semi)rings, for example `SubexponentialSAT/Separation.lean` (`[CommSemiring A]`) and `Counting.lean` (`[CommRing R]`).

## 3. Theorem B: all densities

**Theorem B.** Fix k ≥ 2, and assume the routine of Proposition 3.4 with Lemmas 4.7 and 4.8 is correct; by Lemma A, correctness on CNF counts suffices. Then every unsatisfiable k-CNF F with n variables and m clauses has a Hilbert-like IPS refutation over ℚ, with no Boolean axioms needed. Its coefficient circuits have total size

  (n + m)^{O_k(1)} · 2^{O_k(n (log log n)^{k+1} / (log n)^{1/(2k)})}.

Optimizing σ below reduces the power of log log n to 1 + 1/k.

**Proof.**

1. *Certificate.* Let Gᵢ = C₁ ∧ … ∧ C_{i−1} ∧ ¬Cᵢ, where ¬Cᵢ is k unit clauses. Define gᵢ(X) = Σ_{a∈Sat(Gᵢ)} Π_{v∉Vᵢ} b(a_v, X_v), with b(a, X) = aX + (1 − a)(1 − X). Then Σᵢ fᵢgᵢ = 1 in ℚ[X] (your §3).
2. *Sparsify.* Apply Lemma 6.3 to each Gᵢ with σ = (log n)^{−1/(2k)}.
   - This gives poly_k(n, σ⁻¹)·2^{σn} leaves G_{i,ℓ} on the same variables.
   - Their satisfying sets partition Sat(Gᵢ).
   - In each leaf, every variable occurs at most B = O_k((σ⁻¹ log(2/σ))^{k−1}) times.
   - The branching is clause-combinatorial and does not depend on the weights. Because the sets partition Sat(Gᵢ), gᵢ = Σ_ℓ g_{i,ℓ}, where g_{i,ℓ} is the same weighted sum over Sat(G_{i,ℓ}).
3. *Count each leaf symbolically.*
   - Take the leaf's clause factors (scope at most k), plus one unary weight for each v ∉ Vᵢ.
   - Scopes satisfy w ≤ k. Incidences satisfy b ≤ B + 1, which is at most λ for large n.
   - The total degree satisfies d ≤ kBn + n. So Lemma 4.8 applies with β = 1.
   - From Proposition 3.4, q = ⌊dR/Q⌋ = O(Bn·R/Q), and log C_q ≤ q log(Q/R) + O(nR/Q) = O(B·ρ(n)).
   - The measurement and group terms contribute O(ρ(n)) by (4.18).
   - So each leaf compiles over ℚ[X] into a circuit of size poly(n)·2^{O(Bρ(n))}.
   - The paper's §2.8 route works the same way: OR-gate splitting and Tovey copying give bounded occurrence, and each weight goes on one copy. Both gadgets preserve weighted counts, because the extensions are unique.
4. *Total.* There are m·poly·2^{σn} leaf circuits, each of size poly·2^{O(Bρ(n))}.
   - With σ = (log n)^{−1/(2k)}, we get σn = n/(log n)^{1/(2k)}.
   - We also get Bρ(n) = O_k(n (log log n)^{k+1}/(log n)^{1/(2k)}).
   - Balancing instead with σ = (log log n)^{(k+1)/k}/(log n)^{1/(2k)} gives n (log log n)^{1+1/k}/(log n)^{1/(2k)}. ∎

**Why not ρ(n) for every density.** The manuscript's sharper route for dense inputs (§6, parity tests with Beigel–Tarui polynomials) ends by taking the least nonnegative residue modulo 2^ℓ. That is not a ring operation, so it does not compile into a circuit over ℚ[X]. Getting the 2^{O(ρ(n))} bound at every density would need a ring-friendly substitute for that step.

## 4. Proposition C: structure of the certificates (constant density)

Use one design for all i: one factor per clause and one unary factor per variable. For gᵢ:
- factor j < i is Cⱼ's satisfaction polynomial;
- factor i is its violation polynomial;
- factors j > i are the constant 1;
- the unary factor of v is the weight b(·, X_v) if v ∉ Vᵢ, and the constant 1 otherwise.

Branch on the same high-occurrence set H for every i. Write B_g(t) for the set of v whose unary factor is assigned to group g at point t.

**Proposition C.** gᵢ = Σ_{t=1}^{Q} R_{i,t}(X). Here R_{i,t} is a read-once oblivious ABP in X of width 2^{O(ρ(n))}, in a variable order π_t in which B₁(t), …, B_r(t) are consecutive. Consequently the polynomial Σᵢ fᵢgᵢ − 1 is a constant plus a sum of Q such ABPs, one per order π_t, with Q ≈ log n/log log n.

**Sketch.**
- Group the Hermite combination by t.
- At a fixed t, each Z_{t,E,U} = Σ_y Π_g Σ_g(y). Each Σ_g(y) is a sum of at most 2^{|S_g|} products of univariate affine functions of X_v, for v ∈ B_g(t).
- Track (y, current Boolean vector) across the blocks, and treat z as a coefficient ring ℚ[z]/(z^J). The width is then at most |Y|·2^{2n/r}·J·C_q·2^{|H|} = 2^{O(ρ(n))}.
- fᵢ and the H-branch factors are products of univariates.

**What the variable orders look like.** Lemma 4.5 needs labels (a_v, d_f) to be nearly uniform over r^{2Q} values.
- If every partition {B_g(t)} were an interval partition of one fixed order, each schedule d_{w_v} would be coordinatewise monotone along that order. Then it takes at most Q(r − 1) + 1 values.
- So the unary labels concentrate on at most r^Q·(Q(r − 1) + 1) labels, and the number of copies h exceeds 2M/D by a factor of about r^Q/(2Qr).
- The measurement count r·h·c_B then grows past brute force.
- So within this construction the orders π_t are necessarily varied. I don't see a way around this inside the construction.

## 5. Where Extended Frege stalls

IPS accepts Σᵢ fᵢgᵢ = 1 if it is true; polynomial identity testing checks it. EF has to derive it. There are two known kinds of bridge, and both stop at the same place.

- **Restricted Grochow–Pitassi.** By Proposition C and an analogue of Grochow–Pitassi Theorem 1.4 restricted to this circuit class, it would be enough for EF to prove correct some identity test for sums of about log n/log log n read-once ABPs of width 2^{o(n)} in different orders. The analogue uses their proof idea; it is not a stated theorem of theirs.
  - Even the algorithmic part is open. The best known white-box test, by Gurjar, Korwar, Saxena and Thierauf (arXiv:1411.7341, Theorem 3.2), runs in time w^{O(2^c)}(nd)^{O(c)} for c ABPs.
  - Here c ≈ log n/log log n, which makes this worse than brute force.
  - For c = 1 (one order), white-box testing is linear algebra (Raz–Shpilka), the kind EF might be able to formalize. But §4 says the construction does not give a single order.
- **Direct derivation.** Fix one design and use linearity in each factor. That gives the telescoping sum for free. What remains are three identities between the algorithm's own circuits:
  - the formula with no clauses gives 1;
  - the full formula gives 0;
  - a factor can be replaced by another polynomial with the same values on the cube.

  Each of these is an instance of "this circuit equals the 2ⁿ-term cube sum." The manuscript proves them only by going through that sum, and 2ⁿ = t^{(log log t)^{1/2−o(1)}} for run length t.

**What would count as progress.**
- (a) A feasible, EF-formalizable identity test for sums of polylogarithmically many read-once ABPs.
- (b) A variant of the design that keeps one variable order for X without breaking the label balance.
- (c) A correctness proof for the routine that never forms the cube sum.

**Two entailments, given the manuscript.**
- Any 2^{Ω(n)} EF lower bound for constant-density unsatisfiable CNFs would show that EF does not simulate IPS. By Grochow–Pitassi Theorem 1.4, with their field and encoding conventions, EF then has no polynomial-size proofs of PIT axioms for any polynomial-size identity-testing circuit family.
- A lower bound showing that some constant-density unsatisfiable CNF has no Hilbert-like certificate whose coefficients are sums of Q read-once ABPs of width 2^{o(n)} would refute the manuscript. That is a proof-complexity test of the paper in a model where algebraic lower-bound techniques exist. I don't know of any such result for CNFs.

## 6. Toy verification

Files are alongside this note:
- `toy_routine.py` — the implementation;
- `test_core.py` and `run_grid.py` — the core identities;
- `test_transfer.py` — Lemma A;
- `test_ips_gadgets.py` — the IPS identity, the gadgets and sparsification.

All arithmetic is modulo 2⁶¹ − 1. The weights X_v are uniformly random field elements, so agreement is a Schwartz–Zippel test of the polynomial identity.

**What was implemented, following §§3–4 of the manuscript:**
- the label set B = ([r]^Q)², the swaps Π_s, and f_I as in (4.7);
- M₀ = V₀ f_I(W₀), expanded into products of the Π_s;
- the product eigenbasis and C^B (Lemma 4.1);
- the rows P_u(T) as in (4.10);
- random schedules a_v and d_f, copies and ι (§4.5);
- the separated evaluation of Lemma 3.2, using only other groups' measurement vectors;
- Lemma 3.3 inclusion–exclusion with q = ⌊d(R−1)/Q⌋ and J = q + 1;
- Hermite interpolation.

**What was checked:**
- M₀ψ = (−1)^j f_I(j)ψ on the whole eigenbasis.
- (I − M₀) equals its measurement representation, entry by entry.
- The support bound |E_{u,y}| ≤ R − 1 holds.
- P(0) = δ_v.
- Definition 3.1(4) separation holds for random field vectors.
- Lemma 3.2 holds on random (t, E, U), against brute force.
- Lemma 3.3 holds at every point, including cases with q < n where truncation matters.
- Hermite interpolation recovers H(0).
- The end-to-end output equals the brute-force weighted sum at random X.

These hold for (r, Q, R) ∈ {(2,4,2), (2,5,2), (2,5,3), (3,3,2), (2,4,3), (3,3,3)}, with n = 4–6, D up to 1024, and copy count h up to 2.

**Lemma A checks:**
- the output is affine in every X_v;
- at Boolean X, the symbolic run equals the numeric run on the pinned CNF, and both equal the pinned count;
- symbolic output equals the weighted count at random X.

**IPS checks.** On unsatisfiable 3-CNF cores (n = 4, m = 10, Q = 4; n = 4, m = 10, Q = 5; n = 5, m = 10, Q = 5; n = 5, m = 11, Q = 5, where the Taylor cutoff q ranges from 1 to 7):
- every gᵢ compiled by the routine matches its cube sum;
- Σᵢ fᵢ(X) gᵢ(X) = 1 at random X.

**Gadget checks:**
- OR-gate splitting preserves the weighted count.
- Tovey copying with the weight on one copy preserves it and leaves at most 3 occurrences per variable.
- Appendix A sparsification leaves partition the satisfying assignments, and their weighted counts add up.

**Limitations:**
- The parameters are tiny.
- The schedules are random rather than derandomized.
- At n ≤ 6 the asymptotic regime never begins, so nothing about running time is tested.
- With q ≥ n in some runs, the inclusion–exclusion takes all subsets.

## References

- OpenAI, *The Exponential Time Hypothesis is False*, manuscript revised 25 Oct 2026: Proposition 3.4; Definition 3.1; Lemmas 3.2, 3.3, 4.1–4.8, 6.3; Appendix A.
- J. Grochow and T. Pitassi, *Circuit complexity, proof complexity, and polynomial identity testing: the ideal proof system*: Definition 1.1, Theorems 1.2 and 1.4.
- R. Gurjar, A. Korwar, N. Saxena and T. Thierauf, *Deterministic identity testing for sum of read-once oblivious arithmetic branching programs*, arXiv:1411.7341.
- R. Raz and A. Shpilka, *Deterministic polynomial identity testing in non-commutative models*, 2005.
- J. Krajíček, *A note on SAT algorithms and proof complexity*: Theorem 2.1.
