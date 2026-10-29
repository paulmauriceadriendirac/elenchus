#!/usr/bin/env python3
"""A5 formal audit, script a4 (independent): Section 6 refinement computations.

  (1) Split the 1% world of C' into two worlds of 0.005: Phi({w1})=7.25, Phi({w1,w3})=6.91; verdicts on {w1}
      at refined C' and refined C, by exhaustive enumeration of all 2^16 states (world-level definition).
  (2) Splitting a credence-zero world into k worlds multiplies the separable part of Phi by 2^(k-1) for every
      core excluding it; effective premium beta/2^(k-1); the c'-side bound c1 shrinks to tau exponentially.
  (3) Normalised ('mean') measure, b=3/8: splitting w2 into 2, 4, 8 equiprobable worlds at C and C'.
      Also exact invariance of Phi_norm under splitting a credence-zero world.
  (4) Two-world coarsening {{w1},{w2,w3}}: record threshold (beta-F)/(D+beta)=5/6, withholds at 0.70;
      normalised measure (b=3/8) threshold 7/9 there, so it violates RI as well.
  (5) Question-relative measure: splitting a world the question does not distinguish changes nothing.
Uses Theorem 3 (verified independently in a3) only where exhaustive enumeration is infeasible.
"""
from fractions import Fraction as Fr

FAILS = []


def check(name, cond):
    print(("OK   " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def Cr(C, p):
    return sum((C[i] for i in range(len(C)) if p >> i & 1), Fr(0))


def all_states_EA(n, C, T, F, beta):
    NP = 1 << n
    NS = 1 << NP
    FULL = NP - 1
    coreS = [FULL] * NS
    A = [None] * NS
    A[0] = [beta] * n
    EA = [Fr(0)] * NS
    EA[0] = beta
    for S in range(1, NS):
        low = S & -S
        p = low.bit_length() - 1
        Sp = S ^ low
        cS = coreS[Sp] & p
        coreS[S] = cS
        cur = [A[Sp][w] + (T if p >> w & 1 else F) + beta * ((cS >> w & 1) - (coreS[Sp] >> w & 1)) for w in range(n)]
        A[S] = cur
        EA[S] = sum(C[w] * cur[w] for w in range(n))
    return EA


def phi_all(n, C, T, F, beta):
    NP = 1 << n
    cr = [Cr(C, p) for p in range(NP)]
    e = [c * T + (1 - c) * F for c in cr]
    g = [max(x, Fr(0)) for x in e]
    for b in range(n):
        for X in range(NP):
            if not X >> b & 1:
                g[X] += g[X | 1 << b]
    return [beta * cr[X] + g[X] for X in range(NP)], g, e


def verdict(n, C, T, F, beta):
    """Unique optimum via Theorem 3 (requires unique maximiser and no e_p = 0); returns (B*, X*, generic)."""
    Phi, g, e = phi_all(n, C, T, F, beta)
    m = max(Phi)
    maxers = [X for X in range(1 << n) if Phi[X] == m]
    generic = len(maxers) == 1 and all(x != 0 for x in e)
    X = maxers[0]
    return {p for p in range(1 << n) if (p & X) == X and e[p] > 0}, X, generic, Phi


T, F, beta = Fr(1), Fr(-2), Fr(3)
D = T - F
tau = -F / D

print("=== (1) split the 1% world of C' into two worlds of credence 0.005 (worlds w1,w2a,w2b,w3) ===")
Cp4 = [Fr(75, 100), Fr(5, 1000), Fr(5, 1000), Fr(24, 100)]
C4 = [Fr(70, 100), Fr(75, 1000), Fr(75, 1000), Fr(15, 100)]
Bst, X, gen, Phi = verdict(4, Cp4, T, F, beta)
print(f"   Phi({{w1}}) = {Phi[0b0001]} = {float(Phi[0b0001])}, Phi({{w1,w3}}) = {Phi[0b1001]} = {float(Phi[0b1001])}, max Phi at core {bin(X)}")
check("refined C': Phi({w1}) = 7.25", Phi[0b0001] == Fr(725, 100))
check("refined C': Phi({w1,w3}) = 6.91", Phi[0b1001] == Fr(691, 100))
for name, cred in (("refined C'", Cp4), ("refined C", C4)):
    EA = all_states_EA(4, cred, T, F, beta)
    m = max(EA)
    opt = [S for S in range(len(EA)) if EA[S] == m]
    check(f"{name}: unique optimum (exhaustive, 2^16 states) contains {{w1}}  [EA={float(m)}]", len(opt) == 1 and opt[0] >> 0b0001 & 1)

print("\n=== (2) splitting a credence-zero world into k worlds (record measure, case values) ===")
ok_scale = True
for cprime in (Fr(3, 4), Fr(7, 10), Fr(76, 100)):
    base = [cprime, Fr(0), 1 - cprime]  # w1, w2 (null), w3
    Phi1, g1, _ = phi_all(3, base, T, F, beta)
    for k in range(1, 7):
        cred = [cprime] + [Fr(0)] * k + [1 - cprime]
        n = k + 2
        Phik, gk, _ = phi_all(n, cred, T, F, beta)
        null = sum(1 << (1 + i) for i in range(k))
        for X in range(8):
            if X >> 1 & 1:
                continue  # cores excluding w2
            Xk = (X & 1) | ((X >> 2 & 1) << (n - 1))  # embed w1, w3
            ok_scale &= gk[Xk] == 2 ** (k - 1) * g1[X]
            ok_scale &= Phik[Xk] - gk[Xk] == Phi1[X] - g1[X]
check("separable part of Phi multiplied by exactly 2^(k-1) for every core excluding the null world; premium term unchanged (k=1..6)", ok_scale)
print("   c'-side bound c1(k) = c1 at effective premium beta/2^(k-1); verify by exact verdicts on both sides:")
ok_bound = True
for k in range(1, 7):
    be = beta / 2 ** (k - 1)
    c1k = (be - 2 * F) / (2 * D + be)
    gap = c1k - tau
    formula = be * T / (D * (2 * D + be))
    n = k + 2
    res = []
    for cp in (c1k - gap / 100, c1k + gap / 100):
        cred = [cp] + [Fr(0)] * k + [1 - cp]
        Bst, X, gen, _ = verdict(n, cred, T, F, beta)
        res.append(1 in Bst)
    ok_bound &= (res == [False, True]) and gap == formula
    print(f"   k={k}: c1(k)={float(c1k):.6f}, c1(k)-tau={float(gap):.6f} (formula {float(formula):.6f}); {{w1}} believed just below/above c1(k): {res}")
check("{w1} withheld just below c1(beta/2^(k-1)) and believed just above it, k=1..6 (interval shrinks ~2^-k)", ok_bound)

print("\n=== (3) normalised measure A = |Alg|^-1 sum v_p + b[core], b = 3/8 (equivalent to record with beta = b*2^n) ===")
b = Fr(3, 8)
ok_norm = True
for m in (1, 2, 4, 8):
    n = m + 2
    for name, (c1_, c2_, c3_), want in (("C", (Fr(70, 100), Fr(15, 100), Fr(15, 100)), True),
                                         ("C'", (Fr(75, 100), Fr(1, 100), Fr(24, 100)), False)):
        cred = [c1_] + [c2_ / m] * m + [c3_]
        Bst, X, gen, Phi = verdict(n, cred, T, F, b * 2 ** n)
        # verdicts on all images of coarse propositions
        emb = lambda pc: (pc & 1) | (((1 << m) - 1) << 1 if pc >> 1 & 1 else 0) | ((pc >> 2 & 1) << (n - 1))
        Bc, Xc, genc, _ = verdict(3, [c1_, c2_, c3_], T, F, b * 8)
        same = all((emb(pc) in Bst) == (pc in Bc) for pc in range(8))
        ok_norm &= gen and genc and ((1 in Bst) == want) and same
        print(f"   split w2 into {m}: at {name}: generic={gen}, {{w1}} believed={1 in Bst}; verdicts on all 8 coarse propositions match coarse={same}")
check("normalised measure: {w1} believed at C and not at C' after splitting w2 into 1, 2, 4, 8 worlds (all coarse verdicts preserved)", ok_norm)
ok_null = True
for cprime in (Fr(3, 4), Fr(7, 10)):
    base = [cprime, Fr(0), 1 - cprime]
    Phib, _, _ = phi_all(3, base, T, F, b * 8)
    Phib = [x / 8 for x in Phib]  # normalised Phi = Phi_record(beta=b*2^n) / 2^n
    for k in range(2, 6):
        n = k + 2
        Phik, _, _ = phi_all(n, [cprime] + [Fr(0)] * k + [1 - cprime], T, F, b * 2 ** n)
        Phik = [x / 2 ** n for x in Phik]
        for X in range(8):
            if X >> 1 & 1:
                continue
            Xk = (X & 1) | ((X >> 2 & 1) << (n - 1))
            ok_null &= Phik[Xk] == Phib[X]
check("normalised measure: Phi of every core excluding a null world exactly unchanged by splitting it (k=2..5)", ok_null)

print("\n=== (4) two-world coarsening {{w1},{w2,w3}} ===")


def two_world_optima(c, T, F, beta):
    EA = all_states_EA(2, [c, 1 - c], T, F, beta)
    m = max(EA)
    return [S for S in range(16) if EA[S] == m]


thr = (beta - F) / (D + beta)
check(f"record: two-world threshold for {{w1}} is (beta-F)/(D+beta) = {thr}", thr == Fr(5, 6))
o_lo = two_world_optima(Fr(5, 6) - Fr(1, 1000), T, F, beta)
o_hi = two_world_optima(Fr(5, 6) + Fr(1, 1000), T, F, beta)
o_70 = two_world_optima(Fr(7, 10), T, F, beta)
check("record two-world: {u} in no optimum just below 5/6, in the unique optimum just above", not any(S >> 1 & 1 for S in o_lo) and len(o_hi) == 1 and o_hi[0] >> 1 & 1)
check("record two-world at credence 0.70: {u} withheld (while {w1} believed at C on three worlds) => RI fails", not any(S >> 1 & 1 for S in o_70))
bn2 = b * 4
thr_n = (bn2 - F) / (D + bn2)
o_70n = two_world_optima(Fr(7, 10), T, F, bn2)
check(f"normalised two-world (beta_eff = 3/2): threshold {thr_n} = 7/9; withholds {{u}} at 0.70 => normalised measure violates RI", thr_n == Fr(7, 9) and not any(S >> 1 & 1 for S in o_70n))

print("\n=== (5) question-relative record measure: question {{w1},{w2},{w3}}; split w2 into two (not distinguished) ===")
# states range over subsets of the algebra generated by the question cells; refined worlds w1,w2a,w2b,w3
ok_q = True
for cred3 in ([Fr(70, 100), Fr(15, 100), Fr(15, 100)], [Fr(75, 100), Fr(1, 100), Fr(24, 100)]):
    cells4 = [0b0001, 0b0110, 0b1000]
    cred4 = [cred3[0], cred3[1] / 2, cred3[1] / 2, cred3[2]]
    EA3 = all_states_EA(3, cred3, T, F, beta)
    m3 = max(EA3)
    opt3 = {S for S in range(256) if EA3[S] == m3}
    # question algebra on 4 worlds: union of cells indexed by 3-bit masks; state S (over 8 algebra elements)
    def alg(pc):
        return sum(cells4[i] for i in range(3) if pc >> i & 1)
    EA4 = {}
    for S in range(256):
        members = [alg(pc) for pc in range(8) if S >> pc & 1]
        core = 0b1111
        for q in members:
            core &= q
        val = Fr(0)
        for w in range(4):
            a = sum((T if q >> w & 1 else F) for q in members) + (beta if core >> w & 1 else 0)
            val += cred4[w] * a
        EA4[S] = val
    m4 = max(EA4.values())
    opt4 = {S for S in EA4 if EA4[S] == m4}
    ok_q &= (opt3 == opt4 and m3 == m4)
check("question-relative measure: optima and values identical after splitting a world the question does not distinguish (C and C')", ok_q)

print("\nSUMMARY a4:", "ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
