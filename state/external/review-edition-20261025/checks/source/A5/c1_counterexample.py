# C1. Counterexample to Dorst (2019, ms.) Prop. 5, exact arithmetic.
# Space: W = {1,2,3}; propositions = all 8 subsets (incl. empty set and W), as in Dorst ("the subsets of W").
# Option space (Accuracy First): all 2^8 = 256 belief states.
# Record measure: A(B,w) = sum_{p in B} (T if w in p else -F) + beta*[w in cap B]   (cap of empty B = W)
# Checks:
#  (a) Dorst's conditions (ii)/(iii): adding a true p strictly raises A, adding a false p strictly lowers A, for all B0,p,w.
#  (b) the increment of adding a false p depends on w beyond p's truth value (marginal extensionality fails).
#  (c) unique optima at two REGULAR credence functions C, C' with C({1}) < C'({1}), {1} believed at C, not at C'.
#  (d) grid scan: which propositions show a monotonicity violation.
#  (e) robustness over beta (T=1,F=2) and over (T,F) pairs.
import itertools
from fractions import Fraction as Fr

W = (0, 1, 2)
PROPS = [frozenset(c) for r in range(0, 4) for c in itertools.combinations(W, r)]
STATES = [frozenset(p for p, b in zip(PROPS, bits) if b) for bits in itertools.product([0, 1], repeat=len(PROPS))]

def cap(B):
    X = frozenset(W)
    for p in B:
        X &= p
    return X

def A(B, w, T, F, beta):
    return sum((T if w in p else -F) for p in B) + (beta if w in cap(B) else 0)

def EA(B, C, T, F, beta):
    return sum(C[w] * A(B, w, T, F, beta) for w in W)

def optima(C, T, F, beta):
    vals = [(EA(B, C, T, F, beta), B) for B in STATES]
    m = max(v for v, _ in vals)
    return m, [B for v, B in vals if v == m], sorted((v for v, _ in vals), reverse=True)

def show(B):
    return sorted(("".join(str(w + 1) for w in sorted(p)) or "{}") for p in B)

T, F, beta = Fr(1), Fr(2), Fr(3)

# (a) strict truth-directedness for every B0, p not in B0, w
ok = True
for B0 in STATES:
    for p in PROPS:
        if p in B0:
            continue
        B1 = B0 | {p}
        for w in W:
            d = A(B1, w, T, F, beta) - A(B0, w, T, F, beta)
            if (w in p and not d > 0) or (w not in p and not d < 0):
                ok = False
print("(a) Dorst (ii)/(iii) hold for all 256 states, 8 props, 3 worlds:", ok)

# (b) marginal extensionality fails: adding false p={1} to B0={{1,2}} at w=3 (outside cap) vs w=... ; use B0={{1,3}}
B0 = frozenset([frozenset({0, 2})]); p = frozenset({0})
print("(b) increment of adding {1} to {{1,3}}: at w=2:", A(B0 | {p}, 1, T, F, beta) - A(B0, 1, T, F, beta),
      " at w=3:", A(B0 | {p}, 2, T, F, beta) - A(B0, 2, T, F, beta), "(both worlds make {1} false)")

# (c) the two regular credence functions used in the essay
C1 = (Fr(7, 10), Fr(3, 20), Fr(3, 20))     # (0.70, 0.15, 0.15)
C2 = (Fr(3, 4), Fr(1, 100), Fr(6, 25))     # (0.75, 0.01, 0.24)
for name, C in (("C ", C1), ("C'", C2)):
    m, opts, vals = optima(C, T, F, beta)
    print("(c)", name, [str(x) for x in C], "max EA =", m, "(", float(m), ") runner-up EA =", vals[len(opts)], float(vals[len(opts)]),
          "#optima =", len(opts), "optimum:", [show(B) for B in opts])
    print("     {1} in every optimum:", all(frozenset({0}) in B for B in opts), "; in none:", all(frozenset({0}) not in B for B in opts))

# (d) grid scan (1/40) for monotonicity violations (p in all optima at C, in no optimum at C', C(p) < C'(p))
def scan(T, F, beta, N=40, verbose=False):
    grid = [(Fr(i, N), Fr(j, N), Fr(N - i - j, N)) for i in range(N + 1) for j in range(N + 1 - i)]
    rec = {p: [] for p in PROPS}
    for C in grid:
        _, opts, _ = optima(C, T, F, beta)
        for p in PROPS:
            rec[p].append((sum(C[w] for w in p), all(p in B for B in opts), all(p not in B for B in opts), C))
    viol = []
    for p, L in rec.items():
        bel = [x for x in L if x[1]]; nb = [x for x in L if x[2]]
        if bel and nb:
            lo = min(bel, key=lambda x: x[0]); hi = max(nb, key=lambda x: x[0])
            if lo[0] < hi[0]:
                viol.append((show([p])[0], str(lo[0]), str(hi[0])))
    return viol

v = scan(T, F, beta)
print("(d) T=1,F=2,beta=3, grid 1/40: propositions with violations:", len(v), v)

