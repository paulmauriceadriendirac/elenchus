# C6. Extra checks for claims in the draft.
# (A) Content gap: an ME measure with a non-additive world-independent term still violates Proposition 5.
#     A(B,w) = sum_{p in B} v_p(w) + gamma*[B deductively closed]   (T=1, F=-2, gamma=1/2)
#     "deductively closed" = contains the intersection of any of its members and every superset of each member
#     (for finite B over subsets of W: B is a principal filter, or B is empty).
#     Check ME, truth-directedness, and search a 1/40 grid for threshold violations.
# (B) Restricted to closed states (principal filters), the uniform record measure assigns each filter an
#     answer-level, extensional value: A(up(X), w) depends on w only through whether w in X.
# (C) Under Variable Conservativeness the record measure never has an optimum containing p and its complement
#     (spot check with random proposition-dependent values).
import itertools, random
from fractions import Fraction as Fr

W = (0, 1, 2)
FULL = frozenset(W)
PROPS = [frozenset(c) for r in range(0, 4) for c in itertools.combinations(W, r)]
STATES = [frozenset(p for p, b in zip(PROPS, bits) if b) for bits in itertools.product([0, 1], repeat=len(PROPS))]

def closed(B):
    if not B: return True
    X = FULL
    for p in B: X &= p
    return all((q in B) == (X <= q) for q in PROPS)

T, F, gamma = Fr(1), Fr(-2), Fr(1, 2)
def A(B, w):
    return sum((T if w in p else F) for p in B) + (gamma if closed(B) else 0)

me = td = True
for B0 in STATES:
    for p in PROPS:
        if p in B0: continue
        D = [A(B0 | {p}, w) - A(B0, w) for w in W]
        if len({D[w] for w in W if w in p}) > 1 or len({D[w] for w in W if w not in p}) > 1: me = False
        if any((D[w] <= 0) if w in p else (D[w] >= 0) for w in W): td = False
print("(A) closure-bonus measure: ME holds:", me, " truth-directed:", td)
def optima(C):
    vals = [(sum(C[w] * A(B, w) for w in W), B) for B in STATES]
    m = max(v for v, _ in vals); return [B for v, B in vals if v == m]
N = 40
grid = [(Fr(i, N), Fr(j, N), Fr(N - i - j, N)) for i in range(N + 1) for j in range(N + 1 - i)]
rec = {p: [] for p in PROPS}
for C in grid:
    o = optima(C)
    for p in PROPS:
        rec[p].append((sum(C[w] for w in p), all(p in B for B in o), all(p not in B for B in o), C))
viol = []
for p, L in rec.items():
    bel = [x for x in L if x[1]]; nb = [x for x in L if x[2]]
    if bel and nb:
        lo = min(bel, key=lambda x: x[0]); hi = max(nb, key=lambda x: x[0])
        if lo[0] < hi[0]:
            viol.append((sorted(w + 1 for w in p), str(lo[0]), [str(c) for c in lo[3]], str(hi[0]), [str(c) for c in hi[3]]))
print("    threshold violations (p, believed at, C, not believed at, C'):")
for v in viol: print("     ", v)

# (B)
for n in (3, 4, 5):
    Wn = tuple(range(n)); Fn = frozenset(Wn)
    allp = [frozenset(c) for r in range(0, n + 1) for c in itertools.combinations(Wn, r)]
    ok = True
    for r in range(1, n):
        for X in itertools.combinations(Wn, r):
            X = frozenset(X); up = [p for p in allp if X <= p]
            outside = [sum((1 if w in p else -2) for p in up) + (3 if w in X else 0) for w in Wn if w not in X]
            if len(set(outside)) > 1: ok = False
    print(f"(B) n={n}: value of every proper filter is constant across worlds outside its core:", ok)

# (C)
random.seed(7); bad = 0; tested = 0
for _ in range(300):
    vals = {}
    for p in PROPS:
        if 0 < len(p) < 3:
            vals[p] = [Fr(random.randint(1, 9), 3), None]
    for p in vals:
        q = FULL - p
        # Variable Conservativeness: |T_p| < |F_notp| ; choose F_notp below -T_p
        vals[q][1] = -(vals[p][0] + Fr(random.randint(1, 9), 4))
    vals[FULL] = [Fr(1), Fr(-1)]; vals[frozenset()] = [Fr(1), Fr(-50)]
    beta = Fr(random.randint(1, 40), 4)
    C = [Fr(random.randint(1, 30)) for _ in W]; s = sum(C); C = [c / s for c in C]
    best = None
    for B in STATES:
        X = FULL
        for p in B: X &= p
        v = sum(sum(C[w] for w in p) * vals[p][0] + (1 - sum(C[w] for w in p)) * vals[p][1] for p in B) + beta * sum(C[w] for w in X)
        if best is None or v > best[0]: best = (v, [B])
        elif v == best[0]: best[1].append(B)
    tested += 1
    if any(any((FULL - p) in B for p in B) for B in best[1]): bad += 1
print(f"(C) random proposition-dependent values with Variable Conservativeness: {tested} instances, optima containing a complementary pair: {bad}")
