# From symbolic counting to algebraic refutations

Research note, 26 October 2026. Independent mathematical research.

**Status.** This note derives a conditional upper bound for algebraic proof certificates from the ring-valued counting routine in OpenAI's manuscript, *The Exponential Time Hypothesis is False*, dated 17 October 2026 and revised 25 October 2026. It is a mathematical derivation, not a machine-checked formalization or an independent audit of the counting algorithm. The certificate construction itself is classical. No claim of a new proof-complexity discovery is made.

The concrete result is: **if the manuscript's rational, ring-valued counting construction is correct, every unsatisfiable fixed-width CNF of constant clause density has a Hilbert-like IPS certificate over the rationals of size**

\[
n^{O(1)}2^{O\left(n(\log\log n)^2/\sqrt{\log n}\right)}.
\]

This does not, by itself, establish an Extended Frege upper bound. Efficient proofs of the compressed certificate identities remain an additional obligation.

## 1. What is being assumed

The relevant manuscript ingredients are Section 3.1, Proposition 3.4, Lemmas 4.6-4.8, and the rational interpolation bounds in Appendix B. The routine computes sums of products of local polynomial factors over a commutative rational algebra. Its branching and measurement tests depend on the combinatorial instance and rational design data. Operations on the coefficient algebra are additions, multiplications, and multiplication by rational scalars.

This structure permits symbolic coefficients. We use the coefficient algebra

\[
\mathcal A=\mathbb Q[X_1,\ldots,X_n].
\]

Each operation in this algebra becomes a gate in an arithmetic circuit. We keep that circuit as a directed acyclic graph; we do not expand its monomials. Scalar divisions in interpolation become rational constants, not division by polynomials in the indeterminates.

Define

\[
\rho(n)=\frac{n(\log\log n)^2}{\sqrt{\log n}}
\]

for sufficiently large n, with the finite small cases handled separately. The argument below uses this weaker rational bound. The sharper tensor-contraction algorithm in Appendix D uses precision-dependent residue representatives, so a symbolic lift of that algorithm requires a separate argument. We do not assume it.

## 2. A symbolic compilation lemma

**Lemma, conditional on the manuscript construction.** Fix constants k and D. Let an input consist of O(n) local factors in n Boolean summation variables, with scopes of size at most k, constant degree per factor, and constant-size arithmetic evaluators over a rational polynomial coefficient algebra. Suppose the total incidence count and total factor degree are O(n), and coefficient leaves have polynomial bit length. Then the sum of products over the Boolean cube can be represented by an arithmetic circuit with

\[
n^{O(1)}2^{O_{k,D}(\rho(n))}
\]

gates. In particular this applies to a sparse k-CNF's weighted model polynomial, and to the coefficient polynomials constructed in Section 3 below.

**Proof.** First suppose each Boolean variable occurs in at most a fixed power of log n factors. Pad missing scopes with a unary factor equal to 1 if necessary. Lemmas 4.7-4.8 supply the rational replacement rows, partitions and measurements for Proposition 3.4.

The total factor degree d is at most a fixed constant times n. With the manuscript's parameters, R/Q = O(log log n / sqrt(log n)). Thus the Taylor cutoff q = floor(dR/Q) satisfies

\[
q=O\left(\frac{n\log\log n}{\sqrt{\log n}}\right),\qquad
\log\left(\sum_{j\le q}2^j\binom nj\right)=O(\rho(n)).
\]

The measurement and group-enumeration costs have logarithms O(rho(n)) as well. Consequently Proposition 3.4 makes at most poly(n) times 2^{O(rho(n))} coefficient-ring operations. Replace each such operation by an arithmetic gate. All control choices remain numerical and independent of X. The resulting circuit computes the symbolic sum. The design constants and Hermite interpolation scalars have polynomial-length rational descriptions by Lemma 4.6 and Appendix B.3.

To remove the occurrence restriction, let H contain variables whose original occurrence count exceeds ceil(log_2 n). Since the total incidence count is O(n), |H|=O(n/log n). Enumerate assignments to H. On each branch substitute their values, retain any resulting symbolic scalar factors, and apply the previous construction to the remaining n'=n-O(n/log n) variables. Their occurrences are O(log n), their total degree is O(n') and their scopes still have bounded width. There are 2^{O(n/log n)} branches. This multiplier is absorbed into 2^{O(rho(n))}; summing the branch circuits proves the claim. The finitely many exceptional small sizes may use direct enumeration. QED.

**Scope of this lemma.** A fast numerical SAT or #SAT algorithm alone does not justify this symbolic compilation. The ring-valued, coefficient-independent construction is essential. The output is a circuit representation of a polynomial. It is not an expanded coefficient list or a polynomial-time identity proof.

## 3. An explicit certificate

Normalize a CNF F=C_1 AND ... AND C_m by removing repeated literals and tautological clauses. Write

\[
f_i(X)=\prod_{X_v\in C_i}(1-X_v)\prod_{\neg X_v\in C_i}X_v.
\]

For Boolean a, f_i(a)=1 precisely when clause C_i is false. Let V_i be its variable set, and put

\[
b(a_v,X_v)=a_vX_v+(1-a_v)(1-X_v).
\]

Define the polynomial

\[
g_i(X)=\sum_{a\in\{0,1\}^n}
f_i(a)\prod_{j<i}(1-f_j(a))
\prod_{v\notin V_i}b(a_v,X_v).
\tag{1}
\]

The indicator selects assignments whose first violated clause is C_i. Also define

\[
W_F(X)=\sum_{a:F(a)=1}\prod_{v=1}^n b(a_v,X_v).
\]

These polynomials satisfy the exact identity

\[
\boxed{\quad\sum_{i=1}^m f_i(X)g_i(X)+W_F(X)=1.\quad}
\tag{2}
\]

To prove it, partition assignments into satisfying assignments and those first violating clause i. For an assignment in the latter group, f_i(X) equals the product of its b-factors over V_i. Multiplying by the remaining factors reconstructs its full basis polynomial. All assignments therefore appear once in the left side of (2), whose sum is

\[
\sum_a\prod_v b(a_v,X_v)=\prod_v((1-X_v)+X_v)=1.
\]

This is the first-violated-clause certificate used by Grochow and Pitassi, Lemma 4.2. It is an identity in a polynomial ring, with no need to impose Boolean equations on X.

If F is unsatisfiable, W_F is the zero polynomial, giving

\[
\sum_i f_i(X)g_i(X)=1.
\tag{3}
\]

Consequently the circuit

\[
C_F(X,Y)=\sum_i Y_i g_i(X)
\]

satisfies C_F(X,0)=0 and C_F(X,f_1(X),...,f_m(X))=1. These are the two IPS certificate conditions. Linearity in the placeholder variables Y makes the certificate Hilbert-like.

### A small example

Take F = X AND (NOT X OR Y) AND NOT Y. The violation polynomials are 1-X, X(1-Y), and Y. Equation (1) gives coefficients 1, 1, and X. The refutation is

\[
(1-X)+X(1-Y)+XY=1.
\]

If all three clauses were true, each violation polynomial would be zero; this identity would force 0=1.

## 4. The conditional proof-size upper bound

**Proposition.** Fix k,D. Assuming the manuscript ingredients in Section 1, every unsatisfiable k-CNF F on n variables with m<=Dn has a rational Hilbert-like IPS certificate of arithmetic-circuit size

\[
n^{O(1)}2^{O_{k,D}(\rho(n))}.
\]

**Proof.** For each i, the summand in (1) consists of at most m clause factors of degree at most k and at most n unary weight factors. Its total degree and total incidence count are O_{k,D}(n). Treat X as coefficient indeterminates and a as the Boolean summation variables. The symbolic compilation lemma therefore constructs g_i with the stated size. Combine the m circuits using C_F=sum_i Y_i g_i. Multiplication by m=O(n) preserves the bound. Identity (3) proves that the circuit is an IPS certificate whenever F is unsatisfiable. QED.

The construction can output C_F even when F is satisfiable. In that case (2), rather than (3), describes its substitution, so it is not a refutation. In particular, the construction does not assume a small pre-existing proof of unsatisfiability and does not mistake numerical counting at one point for a polynomial identity.

The coefficient polynomials g_i are multilinear, avoid variables in V_i, and have degree at most n-|V_i|. These semantic properties follow directly from (1). The construction's rational leaves have polynomial bit descriptions. The bound does not hide an arbitrary real-number constant as an oracle.

## 5. What remains between this and Extended Frege

An IPS circuit is a succinct assertion of algebraic identities. Its small size does not supply a small deterministic derivation of those identities in a specified Boolean calculus. General IPS verification uses polynomial identity testing (PIT).

Grochow and Pitassi, Theorem 1.4, give a sufficient bridge: polynomial-size EF proofs of suitable PIT axioms yield a polynomial simulation of IPS by EF. Applied with the appropriate field and encoding conventions, such a simulation would preserve our 2^{O(rho(n))} bound. This is an additional hypothesis, not something established here.

Alternatively, one could build explicit short algebraic derivations for these particular certificates and translate their evaluation and soundness into EF. That would avoid assuming a general simulation, but the required derivations have not been constructed.

There are two distinct tasks:

| Task | Present status |
| --- | --- |
| Show that the classical coefficient formula is a valid certificate | Proved in ordinary mathematics above; also established in the cited literature |
| Compile those coefficient polynomials into small arithmetic circuits | Derived conditionally from the manuscript's ring-valued algorithm |
| Give short EF derivations of the compiled identities | Not established |
| Prove the counting machine's soundness in a specified weak arithmetic theory | Not established |
| Prove a lower bound separating that weak theory or EF from a stronger system | Not established |

Existence of short EF proofs and uniformly finding them are separate claims. An existence hypothesis about PIT-axiom proofs supplies a size conclusion; a uniform proof compiler needs a corresponding uniformity argument.

## 6. Locating the bounded-arithmetic obligation

For a concrete counting machine A, the necessary soundness statement can be formulated using a supplied computation trace:

\[
\mathrm{ValidRun}_A(F,w,0)\;\longrightarrow\;\neg\mathrm{Sat}(F,a).
\tag{4}
\]

Its universal closure ranges over F,w,a. One does not need a weak theory to prove that a short trace exists as a function of the original input before asking whether it can prove (4). A supplied trace becomes part of the input to the soundness argument.

For proof systems satisfying the appropriate substitution and composition conditions, polynomial-size proofs of finite reflection statements yield refutations polynomial in the length of a rejecting run. This is the mechanism of Krajicek's Theorem 2.1. Applying it here still requires identifying and proving the finite reflection family in a particular system.

The hard representation issue is visible in the manuscript. The correctness proof uses a sum over all 2^n assignments, while the computation visits only 2^{o(n)} cases. A translation that explicitly writes out the former object loses the intended proof-size bound. Quantifying over n-bit assignments is not itself prohibited in bounded arithmetic; the problem is obtaining a succinct, internally justified representation of the relevant aggregate and its identities.

The direct formalization should therefore track three separate obligations:

1. Verify the rational design matrices, kernel factorizations, arithmetic and interpolation data.
2. Justify the compressed summation and Taylor reconstruction identities without an explicit full truth table.
3. Derive zero-count soundness from the compressed representation.

Known feasible linear algebra is useful for the first obligation. Tzameret and Cook prove determinant multiplicativity and Cayley-Hamilton over the integers in VNC^2, with corresponding polynomial-size restricted EF proofs. Their result does not supply the second or third obligation. It would be premature to identify elementary matrix calculations, or the appearance of real logarithms in a runtime bound, as the decisive logical obstacle.

PV or V^1 are candidate frameworks for working with polynomial-time operations on supplied data and traces. This note does not establish that either proves (4), and does not identify a weakest theory. Nor does it infer a new incompleteness result from a failure to finish this translation.

## 7. What was inspected and checked

The manuscript portions used were Sections 3-4, Appendix B's coefficient/interpolation estimates, and the beginning of Appendix D's coefficient-ring construction. This was not a complete audit of the 66-page algorithm proof.

The repository's scope document and the endpoint `OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean` were inspected. The comparator configuration names the solution module separately from the challenge statement. The `sorry` in the comparator challenge is a placeholder for that challenge, not evidence of a gap in the solution. No Lean build or transitive axiom audit was run in this investigation.

The script below checks the certificate identity by exact polynomial coefficient arithmetic. It tested all 522 normalized CNFs on 0, 1 and 2 declared variables, 400 seeded random cases on 3-6 variables, and the named example: 923 cases total. The first 922 comprised 192 satisfiable and 730 unsatisfiable cases. It also checked the coefficient formula independently by pinning the falsifying literals of a clause and counting weighted models of the preceding prefix, normalization, multilinearity, Boolean evaluation of W_F, and W_F(1/2,...,1/2)=#F/2^n.

All checks passed. They validate the finite identity implementation and examples. They do not validate the new SAT algorithm, the asymptotic compilation bound, or EF formalizability.

## References

1. OpenAI. *The Exponential Time Hypothesis is False*. 17 October 2026, revised 25 October 2026. [Manuscript](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf). Relevant locations: Section 3.1; Proposition 3.4; Lemmas 4.6-4.8; Appendix B.3; Appendix D.4.1.
2. OpenAI. [Formalization scope](https://github.com/openai/math/blob/main/lean/docs/378.md), [solution endpoint](https://github.com/openai/math/blob/main/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/Final.lean), and [comparator configuration](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/SubexponentialSAT.json). Accessed 26 October 2026.
3. Joshua A. Grochow and Toniann Pitassi. *Circuit complexity, proof complexity, and polynomial identity testing: The ideal proof system*. [Author manuscript](https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf); [arXiv record](https://arxiv.org/abs/1404.3820). Lemma 4.2 and Theorem 1.4 in the author manuscript. The coefficient construction is prior art.
4. Jan Krajicek. *A note on SAT algorithms and proof complexity*. [Author manuscript](https://www2.karlin.mff.cuni.cz/~krajicek/sat.pdf). Theorem 2.1 and its explicit closure hypotheses.
5. Iddo Tzameret and Stephen A. Cook. *Uniform, Integral, and Feasible Proofs for the Determinant Identities*. Journal of the ACM 68(2), Article 12, 2021. [DOI](https://doi.org/10.1145/3431922); [preprint](https://arxiv.org/abs/1811.04313). Theorems 11.3, 11.7-11.8 in the inspected preprint.

## Reproducible finite check

The following uses only the Python standard library. It deliberately enumerates assignments; it is not an implementation of the proposed subexponential solver.

```python
"""Finite checks of a classical first-violated-clause IPS identity.

This enumerates assignments. It does NOT implement or test the new SAT solver,
the symbolic compression bound, or an Extended Frege proof compiler.
"""
from itertools import product
from collections import Counter
from fractions import Fraction
import json
import random


def add(p, q):
    r = Counter(p)
    for m, c in q.items():
        r[m] += c
        if not r[m]:
            del r[m]
    return dict(r)


def mul(p, q):
    r = {}
    for a, c in p.items():
        for b, d in q.items():
            m = tuple(x + y for x, y in zip(a, b))
            r[m] = r.get(m, 0) + c * d
    return {m: c for m, c in r.items() if c}


def one(n):
    return {(0,) * n: 1}


def basis(a, indices):
    n = len(a)
    p = one(n)
    for j in indices:
        e = tuple(int(i == j) for i in range(n))
        f = {e: 1} if a[j] else {(0,) * n: 1, e: -1}
        p = mul(p, f)
    return p


def satisfies_clause(a, clause):
    return any(a[abs(lit) - 1] == (lit > 0) for lit in clause)


def normalize(clauses):
    answer = []
    for raw in clauses:
        c = set(raw)
        if any(-lit in c for lit in c):
            continue
        answer.append(tuple(sorted(c, key=lambda lit: (abs(lit), lit))))
    return answer


def evaluate(p, values):
    return sum(c * product_of(v ** e for v, e in zip(values, m))
               for m, c in p.items())


def product_of(xs):
    answer = 1
    for x in xs:
        answer *= x
    return answer


def check(n, raw_clauses):
    clauses = normalize(raw_clauses)
    assignments = list(product((0, 1), repeat=n))
    supports = [{abs(lit) - 1 for lit in c} for c in clauses]
    fs = []
    for c, support in zip(clauses, supports):
        falsifier = [0] * n
        for lit in c:
            falsifier[abs(lit) - 1] = int(lit < 0)
        fs.append(basis(falsifier, sorted(support)))
    gs = [{} for _ in clauses]
    w = {}
    count = 0
    for a in assignments:
        sat = all(satisfies_clause(a, c) for c in clauses)
        assert sat == all(satisfies_clause(a, c) for c in raw_clauses)
        if sat:
            count += 1
            w = add(w, basis(a, range(n)))
        else:
            i = next(i for i, c in enumerate(clauses)
                     if not satisfies_clause(a, c))
            gs[i] = add(gs[i], basis(a, [j for j in range(n)
                                      if j not in supports[i]]))

    # Independent construction: weighted models of a prefix with the next
    # clause's falsifying literals pinned. No first-failure grouping is used.
    for i, c in enumerate(clauses):
        pinned = {abs(lit) - 1: int(lit < 0) for lit in c}
        free = [j for j in range(n) if j not in pinned]
        expected = {}
        for bits in product((0, 1), repeat=len(free)):
            a = [0] * n
            for j, bit in pinned.items():
                a[j] = bit
            for j, bit in zip(free, bits):
                a[j] = bit
            if all(satisfies_clause(a, old) for old in clauses[:i]):
                expected = add(expected, basis(a, free))
        assert gs[i] == expected
        assert all(all(m[j] == 0 for j in supports[i]) for m in gs[i])

    lhs = w
    for f, g in zip(fs, gs):
        lhs = add(lhs, mul(f, g))
    assert lhs == one(n), (n, clauses, lhs)
    assert all(all(e <= 1 for e in m) for p in [w, *gs] for m in p)
    assert evaluate(w, [Fraction(1, 2)] * n) == Fraction(count, 2 ** n)
    for a in assignments:
        assert evaluate(w, a) == int(all(satisfies_clause(a, c) for c in clauses))
    if count == 0:
        assert not w
    return count == 0


def main():
    counts = Counter()
    for n in range(3):
        possible = [tuple((j + 1) * sign for j, sign in enumerate(signs) if sign)
                    for signs in product((-1, 0, 1), repeat=n)]
        for mask in range(1 << len(possible)):
            clauses = [c for i, c in enumerate(possible) if (mask >> i) & 1]
            unsat = check(n, clauses)
            counts['exhaustive_formulas'] += 1
            counts['unsat' if unsat else 'sat'] += 1
    rng = random.Random(20261026)
    for n in range(3, 7):
        for _ in range(100):
            clauses = []
            for _ in range(rng.randrange(0, 3 * n + 1)):
                c = tuple(rng.choice((-1, 1)) * rng.randrange(1, n + 1)
                          for _ in range(rng.randrange(0, 4)))
                clauses.append(c)
            unsat = check(n, clauses)
            counts['seeded_random_formulas'] += 1
            counts['unsat' if unsat else 'sat'] += 1
    assert check(2, [(1,), (-1, 2), (-2,)])
    counts['named_example'] = 1
    print(json.dumps({
        'status': 'passed',
        'checks': dict(counts),
        'seed': 20261026,
        'limitations': 'Assignment enumeration only; no SAT-algorithm audit, asymptotic verification, or EF formalization.'
    }, indent=2))


if __name__ == '__main__':
    main()
```
