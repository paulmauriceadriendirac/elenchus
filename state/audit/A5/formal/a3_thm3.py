#!/usr/bin/env python3
"""A5 formal audit, script a3 (independent): Theorem 3 and Section 5 claims.

  * Theorem 3 main statement on random instances (2, 3, 4 worlds; proposition-dependent values; ties allowed):
    max_B EA = max_X Phi(X) and the exact set of optimal states equals the characterised set.
    EA is computed from the world-level definition of the record measure (not from the Phi formula).
  * Generic case with uniform values: unique optimum = {p >= X*: C(p) > tau}; (i), (ii), (iii).
  * (ii) for every Phi-maximiser, generic or not.
  * Four-world closure failure: C=(0.62,0.18,0.10,0.10), T=1, F=-2, beta=3 (all 2^16 states).
  * Comparative statics in beta; large-beta limit.
"""
from fractions import Fraction as Fr
import random

random.seed(7)
FAILS = []


def check(name, cond):
    print(("OK   " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def Cr(C, p):
    return sum((C[i] for i in range(len(C)) if p >> i & 1), Fr(0))


def all_states_EA(n, C, Tv, Fv, beta):
    """World-level DP over all 2^(2^n) states: A(S,w) = sum_{p in S} v_p(w) + beta [w in core S]."""
    NP = 1 << n
    NS = 1 << NP
    FULL = NP - 1
    coreS = [FULL] * NS
    A = [None] * NS
    A[0] = [beta] * n
    EA = [Fr(0)] * NS
    EA[0] = beta * sum(C)
    for S in range(1, NS):
        low = S & -S
        p = low.bit_length() - 1
        Sp = S ^ low
        cS = coreS[Sp] & p
        coreS[S] = cS
        prev = A[Sp]
        cur = [prev[w] + (Tv[p] if p >> w & 1 else Fv[p]) + beta * ((cS >> w & 1) - (coreS[Sp] >> w & 1)) for w in range(n)]
        A[S] = cur
        EA[S] = sum(C[w] * cur[w] for w in range(n))
    return EA, coreS


def phi_all(n, C, Tv, Fv, beta):
    NP = 1 << n
    e = [Cr(C, p) * Tv[p] + (1 - Cr(C, p)) * Fv[p] for p in range(NP)]
    g = [max(x, Fr(0)) for x in e]
    for b in range(n):  # superset sums
        for X in range(NP):
            if not X >> b & 1:
                g[X] += g[X | 1 << b]
    return [beta * Cr(C, X) + g[X] for X in range(NP)], e


def rand_cred(n, den, allow_zero=True):
    while True:
        raw = [random.randint(0 if allow_zero else 1, den) for _ in range(n)]
        if sum(raw):
            return [Fr(r, sum(raw)) for r in raw]


print("=== Theorem 3, main statement: random instances, exhaustive over states ===")
for n, trials in ((2, 400), (3, 300), (4, 6)):
    NP = 1 << n
    bad = 0
    for t in range(trials):
        C = rand_cred(n, 6)
        Tv = [Fr(random.randint(1, 8), 4) for _ in range(NP)]
        Fv = [-Fr(random.randint(1, 12), 4) for _ in range(NP)]
        beta = Fr(random.randint(1, 16), 4)
        EA, coreS = all_states_EA(n, C, Tv, Fv, beta)
        Phi, e = phi_all(n, C, Tv, Fv, beta)
        mEA, mPhi = max(EA), max(Phi)
        opt = {S for S in range(len(EA)) if EA[S] == mEA}
        chars = set()
        for S in range(len(EA)):
            X = coreS[S]
            if Phi[X] != mPhi:
                continue
            if any(e[p] > 0 and (p & X) == X and not S >> p & 1 for p in range(NP)):
                continue
            if any(e[p] < 0 and S >> p & 1 for p in range(NP)):
                continue
            chars.add(S)
        if mEA != mPhi or opt != chars:
            bad += 1
    check(f"n={n}: max EA = max Phi and optimal set = characterised set in all {trials} random instances", bad == 0)

print("\n=== Theorem 3, generic case with uniform values: B* and (i)-(iii); (ii) for all maximisers ===")
stats = {"generic": 0, "closed": 0, "notclosed": 0, "inconsistent": 0}
for n, trials in ((3, 300), (4, 6)):
    NP = 1 << n
    FULL = NP - 1
    bad = []
    for t in range(trials):
        C = rand_cred(n, 20)
        T = Fr(random.randint(1, 8), 4)
        F = -(T + Fr(random.randint(1, 8), 4))  # conservative: T < -F
        tau = -F / (T - F)
        beta = random.choice([Fr(random.randint(1, 40), 8), Fr(1, 50), Fr(30)])
        Tv, Fv = [T] * NP, [F] * NP
        Phi, e = phi_all(n, C, Tv, Fv, beta)
        mPhi = max(Phi)
        maxers = [X for X in range(NP) if Phi[X] == mPhi]
        # (ii) for every maximiser
        for X in maxers:
            for u in range(n):
                for v in range(n):
                    if X >> u & 1 and not X >> v & 1 and C[v] > C[u]:
                        bad.append(("ii", C, beta, X))
        generic = len(maxers) == 1 and all(Cr(C, p) != tau for p in range(NP))
        if not generic:
            continue
        stats["generic"] += 1
        X = maxers[0]
        Bstar = {p for p in range(NP) if (p & X) == X and Cr(C, p) > tau}
        EA, coreS = all_states_EA(n, C, Tv, Fv, beta)
        mEA = max(EA)
        opt = [S for S in range(len(EA)) if EA[S] == mEA]
        Sstar = sum(1 << p for p in Bstar)
        if opt != [Sstar]:
            bad.append(("unique optimum", C, beta))
        # (i) consistent iff X* nonempty; closed under single-premise entailment
        cons = True
        cr = FULL
        for p in Bstar:
            cr &= p
        if (cr != 0) != (X != 0) or cr != X:
            bad.append(("i-consistency/core", C, beta))
        for p in Bstar:
            for q in range(NP):
                if (q & p) == p and q not in Bstar:
                    bad.append(("i-single-premise", C, beta))
        if X == 0:
            stats["inconsistent"] += 1
        # (iii) deductively closed iff C(X*) > tau; then exactly the consequences of X*
        closed = all(((p & q) in Bstar) for p in Bstar for q in Bstar) and all(
            q in Bstar for p in Bstar for q in range(NP) if (q & p) == p)
        if closed != (Cr(C, X) > tau):
            bad.append(("iii-iff", C, beta))
        if closed:
            stats["closed"] += 1
            if Bstar != {q for q in range(NP) if (q & X) == X}:
                bad.append(("iii-consequences", C, beta))
        else:
            stats["notclosed"] += 1
    check(f"n={n}: generic uniform-value claims (unique optimum B*, (i), (iii)) and (ii) for all maximisers: {len(bad)} failures", not bad)
print("   generic instances:", stats)

print("\n=== Section 5: four-world closure failure (C=(0.62,0.18,0.10,0.10), T=1, F=-2, beta=3) ===")
n = 4
NP = 1 << n
C = [Fr(62, 100), Fr(18, 100), Fr(10, 100), Fr(10, 100)]
Tv, Fv = [Fr(1)] * NP, [Fr(-2)] * NP
EA, coreS = all_states_EA(n, C, Tv, Fv, Fr(3))
mEA = max(EA)
opt = [S for S in range(len(EA)) if EA[S] == mEA]
lab = lambda p: "W" if p == NP - 1 else ("0" if p == 0 else "".join(str(i + 1) for i in range(n) if p >> i & 1))
print("   optima:", [[lab(p) for p in range(NP) if S >> p & 1] for S in opt], "EA =", mEA, float(mEA))
second = max(v for v in EA if v < mEA)
print("   second-best EA:", second, float(second))
S = opt[0]
check("four-world: unique optimum (exhaustive over 2^16 states)", len(opt) == 1)
check("four-world: optimum believes {w1,w2} and {w1,w3} but not {w1}", S >> 0b0011 & 1 and S >> 0b0101 & 1 and not S >> 0b0001 & 1)
check("four-world: core of optimum is {w1} (C(core)=0.62 < tau, so not closed: (iii))", coreS[S] == 0b0001)

print("\n=== Section 5: comparative statics in beta (uniform values) and large-beta limit ===")
bad_mono = bad_nest = bad_large = 0
for t in range(200):
    n = random.choice([3, 4, 5])
    NP = 1 << n
    distinct = t % 2 == 0
    while True:
        C = rand_cred(n, 40, allow_zero=not distinct)
        if not distinct or len(set(C)) == n:
            break
    T = Fr(random.randint(1, 8), 4)
    F = -(T + Fr(random.randint(1, 8), 4))
    Tv, Fv = [T] * NP, [F] * NP
    betas = sorted({Fr(random.randint(1, 400), 20) for _ in range(12)})
    prev_max = None
    for b in betas:
        Phi, e = phi_all(n, C, Tv, Fv, b)
        m = max(Phi)
        maxers = [X for X in range(NP) if Phi[X] == m]
        lo = min(Cr(C, X) for X in maxers)
        if prev_max is not None and lo < prev_max:
            bad_mono += 1
        prev_max = max(Cr(C, X) for X in maxers)
        if distinct:  # each maximiser is a top-k set
            order = sorted(range(n), key=lambda w: -C[w])
            tops = {sum(1 << w for w in order[:k]) for k in range(n + 1)}
            if any(X not in tops for X in maxers):
                bad_nest += 1
    if all(x > 0 for x in C):
        Phi, e = phi_all(n, C, Tv, Fv, Fr(10 ** 6))
        m = max(Phi)
        maxers = [X for X in range(NP) if Phi[X] == m]
        Bst = [p for p in range(NP) if (p & maxers[0]) == maxers[0] and e[p] > 0]
        if maxers != [NP - 1] or Bst != [NP - 1]:
            bad_large += 1
check("raising beta never lowers the credence of the optimal core (200 random instances)", bad_mono == 0)
check("distinct world credences: every optimal core is a top-k set, hence nested as beta grows", bad_nest == 0)
check("all credences positive, very large beta: unique optimal core W and only W believed", bad_large == 0)

print("\nSUMMARY a3:", "ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
