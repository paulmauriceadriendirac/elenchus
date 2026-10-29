#!/usr/bin/env python3
"""A5 formal audit, script a5 (independent): Theorem 4, its converse, and the minimality examples.

Two-world space {u,v}; propositions as bitmasks: 0=empty, 1={u}=p, 2={v}=pbar, 3=W. States: 16 bitmasks.
  (1) Random truth-directed (TD) + conservative-increment (CI) two-world measures (rejection sampling over ALL 16
      states, integer scores): tau = f/(t+f) in (1/2,1); c>tau => unique optimum {W,p}; c<tau => p in no optimum.
  (2) Converse: separable measure with uniform values T=1,F=-2 satisfies RI (every/some) for all coarsenings
      3->2, all permutations of 3 worlds, and the 2-world swap, on a credence grid that includes exact ties.
  (3) Footnote 5: arithmetic, TD, CI violation; and RI violation under the swap automorphism.
  (4) TD + swap-symmetric verdicts (forced by RI) => no non-monotonicity on two worlds (random search + symmetric family).
  (5) Replacement witnesses for "CI cannot be dropped": (a) separable T=2,F=-1; (b) pairwise symmetric tie measure.
      Both TD + RI, not CI, and Theorem 4's conclusion fails. (b) is also TD + RI and has no threshold at all.
"""
from fractions import Fraction as Fr
from itertools import permutations, product
import random

random.seed(4)
FAILS = []


def check(name, cond):
    print(("OK   " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


def mem(S, n):
    return [p for p in range(1 << n) if S >> p & 1]


def table(n, A):
    return [[A(S, w) for w in range(n)] for S in range(1 << (1 << n))]


def verdicts(n, tab, C):
    EA = [sum(C[w] * row[w] for w in range(n)) for row in tab]
    m = max(EA)
    opt = [S for S in range(len(EA)) if EA[S] == m]
    return {p: (all(S >> p & 1 for S in opt), any(S >> p & 1 for S in opt)) for p in range(1 << n)}, opt


def is_TD(n, tab):
    for S in range(len(tab)):
        for p in range(1 << n):
            if S >> p & 1:
                continue
            for w in range(n):
                d = tab[S | 1 << p][w] - tab[S][w]
                if (p >> w & 1 and not d > 0) or (not p >> w & 1 and not d < 0):
                    return False
    return True


def is_CI2(tab):  # two-world: adding contingent p gains less where true than it loses where false
    for S in range(16):
        for p in (1, 2):
            if S >> p & 1:
                continue
            wt, wf = (0, 1) if p == 1 else (1, 0)
            gain = tab[S | 1 << p][wt] - tab[S][wt]
            loss = tab[S][wf] - tab[S | 1 << p][wf]
            if not gain < loss:
                return False
    return True


def two_world_from_key(key, dW=None, d0=None):
    """key: scores of {W},{W,p},{W,pbar},{W,p,pbar} (pairs). Other states: dropping W costs dW[(S,w)],
    adding empty costs d0[(S,w)] (default 1)."""
    base = {0b1000: key[0], 0b1010: key[1], 0b1100: key[2], 0b1110: key[3]}

    def A(S, w):
        X = (S & 0b0110) | 0b1000
        val = base[X][w]
        if not S >> 3 & 1:
            val -= dW[(S & 0b0110, w)] if dW else 1
        if S & 1:
            val -= d0[(S & 0b1110, w)] if d0 else 1
        return Fr(val)
    return A


print("=== (1) random TD + CI two-world measures (all 16 states checked) ===")
accepted = bad = 0
for trial in range(3000):
    # sample the four key states directly inside the TD+CI region (margins >= 3), then add per-state
    # offsets for dropping W / adding the empty proposition (1..2), and re-check TD and CI on ALL 16 states
    a1 = random.randint(3, 30); a2 = -(a1 + random.randint(3, 30))
    b2 = random.randint(3, 30); b1 = -(b2 + random.randint(3, 30))
    x, y = random.randint(b1 + 3, a1 - 3), random.randint(a2 + 3, b2 - 3)
    if not ((x - b1) + 3 <= (b2 - y) and (y - a2) + 3 <= (a1 - x)):
        continue
    key = [(0, 0), (a1, a2), (b1, b2), (x, y)]
    dW = {(X, w): random.randint(1, 2) for X in (0, 2, 4, 6) for w in range(2)}
    d0 = {(X, w): random.randint(1, 2) for X in range(0, 16, 2) for w in range(2)}
    A = two_world_from_key(key, dW, d0)
    tab = table(2, A)
    if not (is_TD(2, tab) and is_CI2(tab)):
        continue
    accepted += 1
    t = tab[0b1010][0] - tab[0b1000][0]
    f = tab[0b1000][1] - tab[0b1010][1]
    tau = f / (t + f)
    ok = Fr(1, 2) < tau < 1
    grid = [Fr(k, 60) for k in range(61)] + [tau - Fr(1, 10 ** 6), tau + Fr(1, 10 ** 6)]
    for c in grid:
        v, opt = verdicts(2, tab, [c, 1 - c])
        if c > tau:
            ok &= opt == [0b1010]
        elif c < tau:
            ok &= not v[1][1]
    bad += not ok
print(f"   accepted TD+CI measures: {accepted}; failures of the lemma: {bad}")
check(f"Theorem 4 two-world lemma holds for all {accepted} accepted random TD+CI measures", accepted >= 200 and bad == 0)

print("\n=== (2) converse: separable uniform measure (T=1,F=-2) satisfies RI on a grid with exact ties ===")


def sep(T, F, n):
    return lambda S, w: sum(Fr(T) if p >> w & 1 else Fr(F) for p in mem(S, n))


def ri_check(A3, A2, den=30):
    """RI for all surjections {0,1,2}->{0,1}, all permutations of 3 worlds, and the 2-world swap."""
    tab3, tab2 = table(3, A3), table(2, A2)
    grid3 = [[Fr(i, den), Fr(j, den), Fr(den - i - j, den)] for i in range(den + 1) for j in range(den + 1 - i)]
    V3 = {tuple(C): verdicts(3, tab3, C)[0] for C in grid3}
    V2 = {}
    get2 = lambda c: V2.setdefault(c, verdicts(2, tab2, [c, 1 - c])[0])
    viol = []
    surj = [m for m in product(range(2), repeat=3) if set(m) == {0, 1}]
    for C in grid3:
        for m in surj:
            cu = sum(C[w] for w in range(3) if m[w] == 0)
            v2 = get2(cu)
            for ps in range(4):
                pre = sum(1 << w for w in range(3) if ps >> m[w] & 1)
                if V3[tuple(C)][pre] != v2[ps]:
                    viol.append(("3->2", C, m, ps))
        for sg in permutations(range(3)):
            Cs = [Fr(0)] * 3
            for w in range(3):
                Cs[sg[w]] += C[w]
            for ps in range(8):
                pre = sum(1 << w for w in range(3) if ps >> sg[w] & 1)
                if V3[tuple(C)][pre] != V3[tuple(Cs)][ps]:
                    viol.append(("perm", C, sg, ps))
    for k in range(61):
        c = Fr(k, 60)
        for ps in range(4):
            pre = {0: 0, 1: 2, 2: 1, 3: 3}[ps]  # swap: preimage of {u} is {v}
            if get2(c)[pre] != get2(1 - c)[ps]:
                viol.append(("swap", c, ps))
    return viol


viol = ri_check(sep(1, -2, 3), sep(1, -2, 2))
check(f"separable T=1,F=-2: RI (every and some) holds, incl. ties at C(p)=2/3 [{len(viol)} violations]", not viol)

print("\n=== (3) footnote 5 measure ===")
fn5 = two_world_from_key([(0, 0), (1, -2), (-2, 1), (Fr(-1, 2), Fr(4, 5))])
tab5 = table(2, fn5)
check("fn5: truth-directed on all 16 states", is_TD(2, tab5))
check("fn5: violates CI", not is_CI2(tab5))
for c, want in ((Fr(30, 100), True), (Fr(64, 100), False), (Fr(70, 100), True)):
    v, opt = verdicts(2, tab5, [c, 1 - c])
    EAs = {name: sum([c, 1 - c][w] * tab5[S][w] for w in range(2)) for name, S in (("{W}", 8), ("{W,p}", 10), ("{W,pbar}", 12), ("{W,p,pbar}", 14))}
    print(f"   c={float(c)}: optima={opt}, EA:", {k: float(x) for k, x in EAs.items()})
    check(f"fn5: p {'in the unique optimum' if want else 'in no optimum'} at c={float(c)}",
          (len(opt) == 1 and v[1][0]) if want else not v[1][1])
v_a, _ = verdicts(2, tab5, [Fr(3, 10), Fr(7, 10)])   # C(u)=0.3
v_b, _ = verdicts(2, tab5, [Fr(7, 10), Fr(3, 10)])   # C(v)=0.3
print(f"   verdict on {{u}} at C(u)=0.3: every/some={v_a[1]}; verdict on {{v}} at C(v)=0.3: every/some={v_b[2]}")
check("fn5 violates RI under the swap automorphism (verdict on {u} at C(u)=.3 differs from verdict on {v} at C(v)=.3)", v_a[1] != v_b[2])

print("\n=== (4) TD two-world measures: swap-symmetric verdicts (forced by RI) => no non-monotonicity ===")


def profile(tab, grid):
    out = {}
    for c in grid:
        v, opt = verdicts(2, tab, [c, 1 - c])
        out[c] = (v[1], v[2], len(opt) == 1)
    return out


grid = [Fr(k, 100) for k in range(101)]
nonmono = nonmono_sym = sym = 0
samples = 0
for trial in range(1500):
    a1, a2 = random.randint(1, 9), -random.randint(1, 9)
    if trial % 3 == 0:  # swap-symmetric measures
        b1, b2 = a2, a1
        x = y = random.randint(-12, 12)
    elif trial % 3 == 1:  # region where non-monotonicity occurs: {W,p,pbar} line with negative slope
        b1, b2 = -random.randint(1, 9), random.randint(1, 9)
        x, y = Fr(random.randint(b1 * 10 + 1, -1), 10), Fr(random.randint(1, b2 * 10 - 1), 10)
    else:  # unrestricted TD
        b1, b2 = -random.randint(1, 9), random.randint(1, 9)
        x, y = Fr(random.randint(-120, 120), 10), Fr(random.randint(-120, 120), 10)
    if not (b1 < x < a1 and a2 < y < b2):  # TD for adding p to {W,pbar} and pbar to {W,p}
        continue
    tab = table(2, two_world_from_key([(0, 0), (a1, a2), (b1, b2), (x, y)]))
    if not is_TD(2, tab):
        continue
    samples += 1
    pr = profile(tab, grid)
    symmetric = all(pr[c][0] == pr[1 - c][1] for c in grid)
    nm = any(pr[c1][0][0] and pr[c1][2] and not pr[c2][0][1] for i, c1 in enumerate(grid) for c2 in grid[i + 1:])
    sym += symmetric
    nonmono += nm
    nonmono_sym += nm and symmetric
print(f"   TD measures sampled: {samples}; with swap-symmetric verdicts: {sym}; non-monotone: {nonmono}; non-monotone AND symmetric: {nonmono_sym}")
check("no TD two-world measure with swap-symmetric verdicts is non-monotone (random + symmetric families)", sym >= 50 and nonmono >= 50 and nonmono_sym == 0)

print("\n=== (5) replacement witnesses for 'CI cannot be dropped' ===")
# (a) separable, anti-conservative
tab_a2 = table(2, sep(2, -1, 2))
check("(a) separable T=2,F=-1: TD", is_TD(2, tab_a2) and is_TD(3, table(3, sep(2, -1, 3))))
check("(a) separable T=2,F=-1: violates CI", not is_CI2(tab_a2))
viol = ri_check(sep(2, -1, 3), sep(2, -1, 2))
check(f"(a) separable T=2,F=-1: RI holds [{len(viol)} violations]", not viol)
v, opt = verdicts(2, tab_a2, [Fr(1, 2), Fr(1, 2)])
check("(a) at C(p)=1/2 the unique optimum contains p and pbar, so no tau_p in (1/2,1) works", opt == [0b1110])


# (b) pairwise symmetric tie measure: each pair {q,qbar} scored 0 (neither), +1/-2 (one), 0 (both); W +1; empty -1
def pairwise(n):
    full = (1 << n) - 1

    def A(S, w):
        val = Fr(0)
        for q in range(1, full):
            qb = full ^ q
            if q > qb:
                continue
            hq, hb = S >> q & 1, S >> qb & 1
            if hq and not hb:
                val += 1 if q >> w & 1 else -2
            elif hb and not hq:
                val += 1 if qb >> w & 1 else -2
        if S >> full & 1:
            val += 1
        if S & 1:
            val -= 1
        return val
    return A


tab_b2 = table(2, pairwise(2))
check("(b) pairwise tie measure: TD on 2 and 3 worlds", is_TD(2, tab_b2) and is_TD(3, table(3, pairwise(3))))
check("(b) pairwise tie measure: violates CI", not is_CI2(tab_b2))
viol = ri_check(pairwise(3), pairwise(2))
check(f"(b) pairwise tie measure: RI holds [{len(viol)} violations]", not viol)
v, opt = verdicts(2, tab_b2, [Fr(1, 2), Fr(1, 2)])
v2, opt2 = verdicts(2, tab_b2, [Fr(3, 5), Fr(2, 5)])
print(f"   two worlds, C(p)=1/2: optima {opt}; C(p)=3/5: optima {opt2}")
check("(b) for C(p) in (1/3,2/3), p is in some but not every optimum: no tau_p satisfies Theorem 4's conclusion",
      v[1] == (False, True) and v2[1] == (False, True))

print("\nSUMMARY a5:", "ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
