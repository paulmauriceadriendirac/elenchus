#!/usr/bin/env python3
"""A5 formal audit, script a1 (independent re-implementation; does not import the author's checks).

Checks, in exact rational arithmetic:
  * Section 3 case: unique optima, expected accuracies, runner-ups, margins, C'(12)=0.76
  * Section 3 'Order' paragraph: greedy sequences over all 8! orders
  * Section 4 quantifier gap: costs 2 and 5; the EA-difference formula (random tests)
  * Theorem 1: symbolic identities (sympy) and brute force over random parameters
  * Footnote 4: closure-bonus measure is ME + truth-directed and non-monotone
The record measure is computed from its world-level definition
  A(B,w) = sum_{p in B} v_p(w) + beta*[w in core(B)],  core(empty)=W.
"""
from fractions import Fraction as Fr
from itertools import permutations
import random
import sympy as sp

random.seed(20261029)
FAILS = []


def check(name, cond):
    print(("OK   " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def lab(p, n):
    if p == (1 << n) - 1:
        return "W"
    if p == 0:
        return "0"
    return "".join(str(i + 1) for i in range(n) if p >> i & 1)


def members(S, n):
    return [p for p in range(1 << n) if S >> p & 1]


def slab(S, n):
    return "{" + ",".join(lab(p, n) for p in members(S, n)) + "}"


def core(S, n):
    c = (1 << n) - 1
    for p in members(S, n):
        c &= p
    return c


def Cr(C, p):
    return sum((C[i] for i in range(len(C)) if p >> i & 1), Fr(0))


def A_record(S, w, n, T, F, beta):
    s = Fr(0)
    for p in members(S, n):
        s += T if p >> w & 1 else F
    if core(S, n) >> w & 1:
        s += beta
    return s


def all_EA(C, n, A):
    """A(S,w) -> score; returns dict S -> expected score, over all 2^(2^n) states."""
    return {S: sum(C[w] * A(S, w) for w in range(n)) for S in range(1 << (1 << n))}


def optima(vals):
    m = max(vals.values())
    return m, [S for S, v in vals.items() if v == m]


n = 3
P1, P12, P13, PW, P23 = 0b001, 0b011, 0b101, 0b111, 0b110
bit = lambda p: 1 << p
T, F, beta = Fr(1), Fr(-2), Fr(3)
Arec = lambda S, w: A_record(S, w, n, T, F, beta)

print("=== Section 3: the case (T=1, F=-2, beta=3, all 2^8 states) ===")
C = [Fr(70, 100), Fr(15, 100), Fr(15, 100)]
Cp = [Fr(75, 100), Fr(1, 100), Fr(24, 100)]
res = {}
for name, cred in (("C", C), ("C'", Cp)):
    vals = all_EA(cred, n, Arec)
    ranked = sorted(vals.items(), key=lambda kv: -kv[1])
    m, opt = optima(vals)
    print(f"{name}={tuple(str(x) for x in cred)}: optima={[slab(S, n) for S in opt]} EA={m} ({float(m)})")
    print("   next three:", [(slab(S, n), str(v)) for S, v in ranked[1:4]])
    res[name] = (vals, ranked, opt)
vals, ranked, opt = res["C"]
SA = bit(P1) | bit(P12) | bit(P13) | bit(PW)
SB = bit(P12) | bit(P13) | bit(PW)
check("C: unique optimum {1,12,13,W}", opt == [SA])
check("C: EA(optimum)=4.30", vals[SA] == Fr(430, 100))
check("C: runner-up {12,13,W} at 4.20 (strictly second)", ranked[1][0] == SB and ranked[1][1] == Fr(420, 100) and ranked[2][1] < Fr(420, 100))
check("C: runner-up has same core {w1}", core(SB, n) == core(SA, n) == P1)
e = lambda cred, p: Cr(cred, p) * (T - F) + F
check("C: margin = e_1 = 0.10", vals[SA] - vals[SB] == e(C, P1) == Fr(1, 10))
vals2, ranked2, opt2 = res["C'"]
SC = bit(P13) | bit(PW)
check("C': unique optimum {13,W}", opt2 == [SC])
check("C': EA(optimum)=4.94", vals2[SC] == Fr(494, 100))
check("C': runner-up {1,12,13,W} at 4.75 (strictly second)", ranked2[1][0] == SA and ranked2[1][1] == Fr(475, 100) and ranked2[2][1] < Fr(475, 100))
check("C': C'(12)=0.76 > tau=2/3 and 12 not in optimum", Cr(Cp, P12) == Fr(76, 100) and Cr(Cp, P12) > Fr(2, 3) and not (SC >> P12 & 1))
check("{w1} believed at 0.70 (in every optimum at C), in no optimum at 0.75",
      all(S >> P1 & 1 for S in opt) and not any(S >> P1 & 1 for S in opt2))

print("\n=== Section 3 'Order': greedy procedure from the empty state at C ===")
EAc = res["C"][0]
gain_first = EAc[bit(P1)] - EAc[0]
check("considering 1 first from empty state gains e_1 - beta*C({w2,w3}) = 0.1-0.9 = -0.8",
      gain_first == Fr(-8, 10) == e(C, P1) - beta * Cr(C, P23))
finals_first, finals_last, finals_all = set(), set(), {}
for order in permutations(range(8)):
    S = 0
    for p in order:
        if EAc[S | bit(p)] > EAc[S]:
            S |= bit(p)
    finals_all[S] = finals_all.get(S, 0) + 1
    if order[0] == P1:
        finals_first.add(S)
    if order[-1] == P1:
        finals_last.add(S)
check("every order with 1 first ends greedily at {12,13,W}", finals_first == {SB})
check("every order with 1 last ends at the optimum {1,12,13,W}", finals_last == {SA})
S0 = SB
check("gain from adding 1 last (to {12,13,W}) is 0.1", EAc[SB | bit(P1)] - EAc[SB] == Fr(1, 10))
print("   distribution of greedy end states over all 40320 orders:",
      {slab(S, n): k for S, k in finals_all.items()})

print("\n=== Section 4: quantifier gap ===")
B13 = bit(P13)
d_w2 = Arec(B13 | bit(P1), 1) - Arec(B13, 1)
d_w3 = Arec(B13 | bit(P1), 2) - Arec(B13, 2)
check(f"adding false 1 to {{13}} costs 2 at w2 and 5 at w3 (got {-d_w2}, {-d_w3})", d_w2 == -2 and d_w3 == -5)
# EA(B)-EA(B\{p}) = e_p - beta*C(core(B\{p}) \ p): random tests on 3 and 4 worlds
ok = True
for trial in range(3000):
    nn = random.choice([3, 4])
    raw = [random.randint(0, 9) for _ in range(nn)]
    if sum(raw) == 0:
        continue
    cred = [Fr(r, sum(raw)) for r in raw]
    TT = Fr(random.randint(1, 8), 4)
    FF = -Fr(random.randint(1, 12), 4)
    bb = Fr(random.randint(1, 20), 4)
    S = random.randrange(1, 1 << (1 << nn))
    p = random.choice(members(S, nn))
    Sm = S & ~bit(p)
    EAx = lambda X: sum(cred[w] * A_record(X, w, nn, TT, FF, bb) for w in range(nn))
    lhs = EAx(S) - EAx(Sm)
    rhs = Cr(cred, p) * TT + (1 - Cr(cred, p)) * FF - bb * Cr(cred, core(Sm, nn) & ~p)
    ok &= (lhs == rhs)
check("EA(B)-EA(B\\{p}) = e_p - beta*C(core(B\\{p}) minus p)  [3000 random cases, 3-4 worlds]", ok)

print("\n=== Theorem 1: symbolic identities (sympy) ===")
Ts, Fs, bs, c, cp = sp.symbols("T F beta c cprime", real=True)
D = Ts - Fs
tau = -Fs / D
c0 = (bs - Ts - 2 * Fs) / (2 * D + bs)
c1 = (bs - 2 * Fs) / (2 * D + bs)
ee = lambda x: x * D + Fs
z = lambda expr: sp.simplify(expr) == 0
check("c1-c0 = T/(2D+beta)", z(c1 - c0 - Ts / (2 * D + bs)))
check("c1-tau = beta*T/(D(2D+beta))", z(c1 - tau - bs * Ts / (D * (2 * D + bs))))
check("1-c1 = 2T/(2D+beta)", z(1 - c1 - 2 * Ts / (2 * D + bs)))
check("tau-c0 = T(D-beta)/(D(2D+beta))  [so tau>=c0 iff beta<=D]", z(tau - c0 - Ts * (D - bs) / (D * (2 * D + bs))))
# Phi values at C_c=(c,(1-c)/2,(1-c)/2) under the sign pattern of the proof (e_1,e_12,e_13,e_W>0, rest<0)
h = (1 + c) / 2
Phi1 = bs * c + ee(c) + 2 * ee(h) + Ts
PhiW = bs + Ts
Phi13 = bs * h + ee(h) + Ts
Phi2 = bs * (1 - c) / 2 + ee(h) + Ts
Phi23 = bs * (1 - c) + Ts
Phi0 = ee(c) + 2 * ee(h) + Ts
check("Phi(1)-Phi(W) = c(2D+beta)+T+2F-beta", z(Phi1 - PhiW - (c * (2 * D + bs) + Ts + 2 * Fs - bs)))
check("root of Phi(1)-Phi(W) in c is c0", z(sp.solve(sp.Eq(Phi1 - PhiW, 0), c)[0] - c0))
check("Phi(1)-Phi(13) = (Phi(1)-Phi(W))/2 + e_1/2", z(Phi1 - Phi13 - ((Phi1 - PhiW) / 2 + ee(c) / 2)))
check("Phi(1)-Phi({w2}) = e_1+e_12+beta(3c-1)/2", z(Phi1 - Phi2 - (ee(c) + ee(h) + bs * (3 * c - 1) / 2)))
check("Phi(1)-Phi({w2,w3}) = e_1+2e_12+beta(2c-1)", z(Phi1 - Phi23 - (ee(c) + 2 * ee(h) + bs * (2 * c - 1))))
check("Phi(1)-Phi(empty) = beta*c", z(Phi1 - Phi0 - bs * c))
# at (c',0,1-c'): e_1=e_12=c'D+F, e_13=e_W=T
Phi1p = bs * cp + 2 * ee(cp) + 2 * Ts
Phi13p = bs + 2 * Ts
check("Phi(13)-Phi(1) = beta(1-c')-2e_1 at (c',0,1-c')", z(Phi13p - Phi1p - (bs * (1 - cp) - 2 * ee(cp))))
check("root of Phi(13)-Phi(1) in c' is c1", z(sp.solve(sp.Eq(Phi13p - Phi1p, 0), cp)[0] - c1))
num = lambda expr, **kw: expr.subs({Ts: 1, Fs: -2, bs: 3})
print(f"   case values: c0={num(c0)}, tau={num(tau)}, c1={num(c1)}; 0.70 and 0.75 in (2/3, 7/9)")
check("case: c0=2/3, tau=2/3, c1=7/9", num(c0) == sp.Rational(2, 3) and num(tau) == sp.Rational(2, 3) and num(c1) == sp.Rational(7, 9))

print("\n=== Theorem 1: brute force over random parameters (all 2^8 states, exact) ===")
nbad, ntested = 0, 0
for trial in range(250):
    TT = Fr(random.randint(1, 12), 4)
    FF = -(TT + Fr(random.randint(1, 24), 4))          # 0 < T < -F
    bb = random.choice([Fr(1, 100), Fr(1, 10), Fr(random.randint(1, 40), 4), Fr(25)])
    DD = TT - FF
    tt = -FF / DD
    cc0 = (bb - TT - 2 * FF) / (2 * DD + bb)
    cc1 = (bb - 2 * FF) / (2 * DD + bb)
    lo = max(cc0, tt)
    assert lo < cc1 < 1
    u1, u2 = sorted(random.sample(range(1, 1000), 2))
    cA = lo + (cc1 - lo) * Fr(u1, 1000)
    cB = lo + (cc1 - lo) * Fr(u2, 1000)
    A_ = lambda S, w: A_record(S, w, n, TT, FF, bb)
    vA = all_EA([cA, (1 - cA) / 2, (1 - cA) / 2], n, A_)
    mA, oA = optima(vA)
    good = len(oA) == 1 and (oA[0] >> P1 & 1)
    for eps in (Fr(0), Fr(1, 10 ** 9), Fr(1, 10 ** 6)):
        vB = all_EA([cB, eps, 1 - cB - eps], n, A_)
        mB, oB = optima(vB)
        good &= not any(S >> P1 & 1 for S in oB)
    ntested += 1
    if not good:
        nbad += 1
        print("   counterexample to Theorem 1?", TT, FF, bb, cA, cB)
check(f"Theorem 1 conclusion holds in {ntested} random instances (eps in {{0,1e-9,1e-6}})", nbad == 0)
# sanity: just above c1 at eps=0, {w1} is believed again (bound c1 is tight on the c' side)
TT, FF, bb = Fr(1), Fr(-2), Fr(3)
A_ = lambda S, w: A_record(S, w, n, TT, FF, bb)
for cB in (Fr(7, 9) - Fr(1, 1000), Fr(7, 9) + Fr(1, 1000)):
    m_, o_ = optima(all_EA([cB, Fr(0), 1 - cB], n, A_))
    print(f"   case values, c'={float(cB):.4f}, eps=0: optima {[slab(S, n) for S in o_]}")

print("\n=== Footnote 4: bonus 1/2 for deductively closed states (T=1, F=-2) ===")
NP = 1 << n


def closed1(S):  # B equals the set of all consequences of its core (empty state: closure {W} -> not closed)
    X = core(S, n)
    return S == sum(bit(q) for q in range(NP) if q & X == X)


def closed2(S):  # empty state counted as (vacuously) closed
    return S == 0 or closed1(S)


for nm, closed in (("def1 (empty state not closed)", closed1), ("def2 (empty state closed)", closed2)):
    Acl = lambda S, w: sum((Fr(1) if p >> w & 1 else Fr(-2)) for p in members(S, n)) + (Fr(1, 2) if closed(S) else 0)
    me_ok, td_ok = True, True
    for S in range(1 << NP):
        for p in range(NP):
            if S >> p & 1:
                continue
            inc = [Acl(S | bit(p), w) - Acl(S, w) for w in range(n)]
            for w in range(n):
                td_ok &= (inc[w] > 0) if (p >> w & 1) else (inc[w] < 0)
                for w2 in range(n):
                    if (p >> w & 1) == (p >> w2 & 1):
                        me_ok &= inc[w] == inc[w2]
    check(f"fn4 [{nm}]: ME holds on all states", me_ok)
    check(f"fn4 [{nm}]: truth-directed on all states", td_ok)
    for cred, want in (([Fr(575, 1000), Fr(2, 10), Fr(225, 1000)], True), ([Fr(65, 100), Fr(0), Fr(35, 100)], False)):
        m_, o_ = optima(all_EA(cred, n, Acl))
        print(f"   C={tuple(float(x) for x in cred)}: optima {[slab(S, n) for S in o_]} EA={float(m_)}")
        if want:
            check(f"fn4 [{nm}]: {{w1}} in the unique optimum at {tuple(float(x) for x in cred)}", len(o_) == 1 and o_[0] >> P1 & 1)
        else:
            check(f"fn4 [{nm}]: {{w1}} in no optimum at {tuple(float(x) for x in cred)}", not any(S >> P1 & 1 for S in o_))

print("\nSUMMARY a1:", "ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
