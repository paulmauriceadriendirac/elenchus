# C7. Can the record measure reproduce Holguin's (2022, sec. 5) horse race in a single context?
#   S1 = (.40, .35, .25): think A      S2 = (.45, .50, .05): think B, not A
# Requirement: at S1 the unique optimum contains {A} and is consistent; at S2 the unique optimum contains {B} and
# not {A} and is consistent.
# Values: fully proposition-dependent T_p > 0 > F_p for the 6 contingent propositions and T_W > 0, subject to Dorst's
# Variable Conservativeness |T_p| < |F_notp| for each cell/pair complement pair.  Premium beta > 0.
# Sampling: log-uniform magnitudes over [1e-3, 1e3]. Optima computed with Theorem 3 (verified in c3).
import itertools, math, random

W = (0, 1, 2)
props = [frozenset(c) for r in (1, 2, 3) for c in itertools.combinations(W, r)]
cores = [frozenset(c) for r in (0, 1, 2, 3) for c in itertools.combinations(W, r)]
FULL = frozenset(W)
S1 = (.40, .35, .25); S2 = (.45, .50, .05)
A, Bh = frozenset({0}), frozenset({1})

def solve(C, T, F, beta):
    e = {p: sum(C[w] for w in p) * T[p] + (1 - sum(C[w] for w in p)) * F[p] for p in props}
    phi = {X: sum(max(e[p], 0) for p in props if X <= p) + beta * sum(C[w] for w in X) for X in cores}
    order = sorted(phi.values(), reverse=True)
    if order[0] - order[1] < 1e-9 or any(abs(v) < 1e-12 for v in e.values()):
        return None
    X = max(phi, key=phi.get)
    return X, {p for p in props if X <= p and e[p] > 0}

lu = lambda: math.exp(random.uniform(math.log(1e-3), math.log(1e3)))
random.seed(2026)
tested = hits = 0
for _ in range(1_000_000):
    T = {}; F = {}
    for p in props:
        T[p] = lu()
    for p in props:
        if p == FULL: continue
        q = FULL - p
        F[q] = -(T[p] + lu())          # |F_q| > |T_p|  (Variable Conservativeness), q = complement of p
    F[FULL] = -1.0
    beta = lu()
    r1 = solve(S1, T, F, beta); r2 = solve(S2, T, F, beta)
    if r1 is None or r2 is None: continue
    tested += 1
    (X1, B1), (X2, B2) = r1, r2
    if A in B1 and X1 and Bh in B2 and A not in B2 and X2:
        hits += 1
print("assignments tested:", tested, " reproducing Holguin's verdicts:", hits)

# Part 2: contexts that treat the horses alike.
#  (sym3) values depend only on the size of the proposition (full symmetry among A, B, C);
#  (symAB) values invariant under swapping A and B (C may be treated differently).
def sample(kind):
    T = {}; F = {}
    if kind == "sym3":
        t = {1: lu(), 2: lu(), 3: lu()}
        f1 = -(t[2] + lu()); f2 = -(t[1] + lu())        # |F_cell| > |T_pair|, |F_pair| > |T_cell|
        for p in props:
            T[p] = t[len(p)]
            F[p] = {1: f1, 2: f2, 3: -1.0}[len(p)]
    else:
        swap = lambda p: frozenset({1: 0, 0: 1, 2: 2}[w] for w in p)
        for p in props:
            if p in T: continue
            T[p] = lu(); T[swap(p)] = T[p]
        for p in props:
            if p == FULL or (FULL - p) in F: continue
            q = FULL - p
            F[q] = -(T[p] + lu()); F[swap(q)] = F[q] if swap(q) != q else F[q]
        F[FULL] = -1.0
        for p in props:   # restore Variable Conservativeness after symmetrisation
            if p != FULL and not abs(F[FULL - p]) > T[p]:
                return None
    return T, F

for kind in ("sym3", "symAB"):
    random.seed(7); tested = hits = 0
    for _ in range(1_000_000):
        s = sample(kind)
        if s is None: continue
        T, F = s; beta = lu()
        r1 = solve(S1, T, F, beta); r2 = solve(S2, T, F, beta)
        if r1 is None or r2 is None: continue
        tested += 1
        (X1, B1), (X2, B2) = r1, r2
        if A in B1 and X1 and Bh in B2 and A not in B2 and X2:
            hits += 1
    print(f"[{kind}] assignments tested: {tested}  reproducing Holguin's verdicts: {hits}")

# Part 3: an explicit symmetric context, verified by exhaustive exact enumeration over all 256 belief states
# (all 8 propositions, including the empty set). Values depend only on size:
#   one-horse propositions T=1, F=-33/50; two-horse T=13/20, F=-101/100; W: T=1; empty set: F=-2.  beta=19/100.
# Variable Conservativeness: |T_cell|=1 < |F_pair|=1.01 and |T_pair|=0.65 < |F_cell|=0.66.
from fractions import Fraction as Fr
PR = [frozenset(c) for r in range(0, 4) for c in itertools.combinations(W, r)]
ST = [frozenset(p for p, b in zip(PR, bits) if b) for bits in itertools.product([0, 1], repeat=len(PR))]
TV = {0: Fr(0), 1: Fr(1), 2: Fr(13, 20), 3: Fr(1)}
FV = {0: Fr(-2), 1: Fr(-33, 50), 2: Fr(-101, 100), 3: Fr(0)}
beta3 = Fr(19, 100)
def EAx(Bs, C):
    X = FULL
    for p in Bs: X &= p
    return sum(sum(C[w] for w in p) * TV[len(p)] + (1 - sum(C[w] for w in p)) * FV[len(p)] for p in Bs) + beta3 * sum(C[w] for w in X)
nm = lambda p: "".join("ABC"[w] for w in sorted(p)) or "{}"
for name, C in (("S1", (Fr(40, 100), Fr(35, 100), Fr(25, 100))), ("S2", (Fr(45, 100), Fr(50, 100), Fr(5, 100)))):
    vals = sorted(((EAx(Bs, C), Bs) for Bs in ST), key=lambda x: x[0], reverse=True)
    top = [Bs for v, Bs in vals if v == vals[0][0]]
    print(f"[explicit] {name}: unique optimum: {len(top) == 1}; optimum = {sorted(map(nm, top[0]))}; "
          f"EA = {vals[0][0]} ({float(vals[0][0]):.4f}); runner-up {float(vals[1][0]):.4f} = {sorted(map(nm, vals[1][1]))}")
