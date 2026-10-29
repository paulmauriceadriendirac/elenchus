# C10. Checks for the v6 narrowing of A5 (exact rational arithmetic, exhaustive enumeration of belief states).
# (A) Review counterexample: separable values T = 1, F = -n on an n-world space. Each space is Lockean with
#     threshold n/(n+1); the family is truth-directed and satisfies CI, but violates refinement invariance (RI).
# (B) Contrast: uniform separable values T = 1, F = -2 on every space satisfy RI on all coarsenings tested.
# (C) Weaker bridge (some state is rational + Maximize Expected Accuracy as a necessary condition): every case
#     used against Proposition 5 has a UNIQUE optimum on the believing side and NO optimum containing the
#     proposition on the withholding side, so the cases go through without Permission.
import itertools, random
from fractions import Fraction as Fr

def space(n):
    W = tuple(range(n)); full = frozenset(W)
    props = [frozenset(c) for r in range(n + 1) for c in itertools.combinations(W, r)]
    states = [frozenset(p for p, b in zip(props, bits) if b) for bits in itertools.product([0, 1], repeat=len(props))]
    return W, full, props, states

def core(B, full):
    X = full
    for p in B: X = X & p
    return X

def optima(n, A, C):
    W, full, props, states = SP[n]
    best, arg = None, []
    for B in states:
        v = sum(C[w] * A(B, w) for w in W if C[w] != 0)
        if best is None or v > best: best, arg = v, [B]
        elif v == best: arg.append(B)
    return arg

SP = {n: space(n) for n in (2, 3, 4)}

def sep(T, F):
    return lambda B, w: sum((T if w in p else F) for p in B)

def record(T, F, beta, n):
    full = SP[n][1]
    return lambda B, w: sum((T if w in p else F) for p in B) + (beta if w in core(B, full) else 0)

def rand_cred(n, rng, den=997):
    cuts = sorted(rng.randrange(1, den) for _ in range(n - 1))
    parts = [b - a for a, b in zip([0] + cuts, cuts + [den])]
    return tuple(Fr(x, den) for x in parts)

ok = True
def check(label, cond):
    global ok
    ok &= bool(cond); print(("PASS " if cond else "FAIL ") + label)

rng = random.Random(20261029)

# ---------- (A) T = 1, F = -n on n worlds ----------
print("(A) separable family T=1, F=-n on n worlds")
check("  CI on the two-world space: gain 1 < loss 2", Fr(1) < Fr(2))
for n in (2, 3, 4):
    A = sep(Fr(1), Fr(-n)); tau = Fr(n, n + 1)
    W, full, props, states = SP[n]
    # truth-directedness: adding p raises the score where p is true, lowers it where false (contingent p)
    td = all((A(B | {p}, w) - A(B, w) > 0) == (w in p) for B in states[:: max(1, len(states) // 400)]
             for p in props if p not in B and 0 < len(p) < n for w in W)
    check(f"  n={n}: truth-directed (sampled states)", td)
    trials = 6 if n == 4 else 40
    lockean = True
    for _ in range(trials):
        C = rand_cred(n, rng)
        if any(sum(C[w] for w in p) == tau for p in props): continue
        o = optima(n, A, C)
        lockean &= (len(o) == 1 and o[0] == frozenset(p for p in props if sum(C[w] for w in p) > tau))
    check(f"  n={n}: unique optimum = {{p : C(p) > {tau}}} at {trials} random credences", lockean)
C3 = (Fr(7, 10), Fr(3, 20), Fr(3, 20)); p1 = frozenset({0})
o3 = optima(3, sep(Fr(1), Fr(-3)), C3)
o2 = optima(2, sep(Fr(1), Fr(-2)), (Fr(7, 10), Fr(3, 10)))
check("  n=3 at (0.70,0.15,0.15): {w1} in no optimum (threshold 3/4)", all(p1 not in B for B in o3))
check("  coarsening {w1}->u, {w2,w3}->v, C*=(0.70,0.30): {u} in the unique optimum (threshold 2/3) => RI fails",
      len(o2) == 1 and p1 in o2[0])

# ---------- (B) uniform T=1, F=-2 on every space: RI on coarsenings ----------
print("(B) uniform separable T=1, F=-2: RI on coarsenings")
A = sep(Fr(1), Fr(-2))
def surjections(n, m):
    for f in itertools.product(range(m), repeat=n):
        if len(set(f)) == m: yield f
ri = True; tested = 0
for n, m in ((3, 2), (4, 2), (4, 3)):
    maps = list(surjections(n, m))
    for _ in range(3 if n == 4 else 8):
        C = rand_cred(n, rng); pi = rng.choice(maps)
        Cs = tuple(sum(C[w] for w in range(n) if pi[w] == u) for u in range(m))
        o, os_ = optima(n, A, C), optima(m, A, Cs)
        for ps in SP[m][2]:
            pre = frozenset(w for w in range(n) if pi[w] in ps)
            ri &= (all(pre in B for B in o) == all(ps in B for B in os_)) and \
                  (any(pre in B for B in o) == any(ps in B for B in os_))
        tested += 1
check(f"  every/some verdicts agree across {tested} random coarsenings", ri)

# ---------- (C) uniqueness / exclusion in the numerical cases ----------
print("(C) cases under the weaker bridge")
def believed_unique(n, A, C, p):
    o = optima(n, A, C); return len(o) == 1 and p in o[0]
def excluded(n, A, C, p):
    o = optima(n, A, C); return all(p not in B for B in o), len(o)
R = record(Fr(1), Fr(-2), Fr(3), 3)
check("  Sec.3: unique optimum at (0.70,0.15,0.15) contains {w1}", believed_unique(3, R, C3, p1))
e, k = excluded(3, R, (Fr(75, 100), Fr(1, 100), Fr(24, 100)), p1)
check(f"  Sec.3: no optimum at (0.75,0.01,0.24) contains {{w1}} (#optima={k})", e and k == 1)
# Theorem 1 at a second parameter set: T=1, F=-3, beta=1 -> tau=3/4, c1=7/9
R2 = record(Fr(1), Fr(-3), Fr(1), 3); c, c2 = Fr(76, 100), Fr(77, 100)
check("  Thm 1 (T=1,F=-3,beta=1): unique optimum at c=0.76 contains {w1}",
      believed_unique(3, R2, (c, (1 - c) / 2, (1 - c) / 2), p1))
for eps in (Fr(0), Fr(1, 1000)):
    e, k = excluded(3, R2, (c2, eps, 1 - c2 - eps), p1)
    check(f"  Thm 1: no optimum at c'=0.77, eps={eps} contains {{w1}} (#optima={k})", e)
# footnote 4: closure bonus 1/2
full3 = SP[3][1]; props3 = SP[3][2]
def closed(B):
    if not B: return True
    X = core(B, full3); return all((q in B) == (X <= q) for q in props3)
CB = lambda B, w: sum((Fr(1) if w in p else Fr(-2)) for p in B) + (Fr(1, 2) if closed(B) else 0)
check("  fn 4: unique optimum at (0.575,0.2,0.225) contains {w1}",
      believed_unique(3, CB, (Fr(575, 1000), Fr(2, 10), Fr(225, 1000)), p1))
e, k = excluded(3, CB, (Fr(65, 100), Fr(0), Fr(35, 100)), p1)
check(f"  fn 4: no optimum at (0.65,0,0.35) contains {{w1}} (#optima={k})", e)
# Sec.5 four-world closure failure: unique optimum believes {w1,w2},{w1,w3}, not {w1}
R4 = record(Fr(1), Fr(-2), Fr(3), 4); o = optima(4, R4, (Fr(62, 100), Fr(18, 100), Fr(10, 100), Fr(10, 100)))
check("  Sec.5: four-world case has a unique optimum with {w1,w2},{w1,w3} and without {w1}",
      len(o) == 1 and frozenset({0, 1}) in o[0] and frozenset({0, 2}) in o[0] and frozenset({0}) not in o[0])
# Sec.6: T=2, F=-1 at credence 1/2 on two worlds: unique optimum {W, p, not-p}
o = optima(2, sep(Fr(2), Fr(-1)), (Fr(1, 2), Fr(1, 2)))
check("  Sec.6: T=2,F=-1 at 1/2 has unique optimum {W,p,not-p}",
      len(o) == 1 and o[0] == frozenset({frozenset({0}), frozenset({1}), frozenset({0, 1})}))
print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
