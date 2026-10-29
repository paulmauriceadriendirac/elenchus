#!/usr/bin/env python3
"""A5 formal audit, script a2 (independent): Theorem 2 and footnote 3.

Theorem 2 is linear in the table A(B,w). On the domain Dom of states with no proposition together with
its complement, on 2 and 3 worlds, we certify:
  (a) {A : ME} = {A(empty,w) + kappa(B) + sum_{contingent p in B} J_p [w in p]}   (J_p real; TD adds J_p>0)
  (b) {A : ME and BI} = {A(empty,w) + sum_{p in B} v_p(w)}                         (separable)
Certification: the representation family is (i) contained in the solution space (exact integer check on a
basis), (ii) of dimension d (rank of the basis, mod p, is a lower bound for the rank over Q), and (iii) the
constraint matrix has rank >= #unknowns - d mod p (a lower bound for rank over Q). Then the solution space
has dimension exactly d and equals the family.
Footnote 3: an ME, truth-directed measure on ALL states (3 worlds) in which J_p changes when the complement
of p is believed.
"""
from fractions import Fraction as Fr
from itertools import product

FAILS = []


def check(name, cond):
    print(("OK   " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)


PRIMES = (2 ** 61 - 1, 1000000007)


def rank_mod(rows, ncols, P):
    piv = {}  # pivot col -> row (dict col->val), normalized pivot = 1
    r = 0
    for row in rows:
        v = {c: x % P for c, x in row.items() if x % P}
        while v:
            c = min(v)
            if c in piv:
                f = v[c]
                for cc, xx in piv[c].items():
                    v[cc] = (v.get(cc, 0) - f * xx) % P
                    if v[cc] == 0:
                        del v[cc]
            else:
                inv = pow(v[c], P - 2, P)
                piv[c] = {cc: xx * inv % P for cc, xx in v.items()}
                r += 1
                break
    return r


def analyse(n):
    NP = 1 << n
    FULL = NP - 1
    comp = lambda p: FULL ^ p
    contingent = [p for p in range(NP) if p not in (0, FULL)]
    # domain: subsets of propositions with no complementary pair
    pairs = sorted({tuple(sorted((p, comp(p)))) for p in range(NP)})
    dom = []
    for choice in product(range(3), repeat=len(pairs)):
        S = 0
        for (a, b), ch in zip(pairs, choice):
            if ch == 1:
                S |= 1 << a
            elif ch == 2:
                S |= 1 << b
        dom.append(S)
    idx = {S: i for i, S in enumerate(dom)}
    var = lambda S, w: idx[S] * n + w
    NV = len(dom) * n
    mem = lambda S: [p for p in range(NP) if S >> p & 1]

    me_rows, bi_rows = [], []
    for S in dom:
        for p in range(NP):
            if S >> p & 1 or S >> comp(p) & 1:
                continue
            Sp = S | 1 << p
            for w in range(n):
                for w2 in range(w + 1, n):
                    if (p >> w & 1) == (p >> w2 & 1):
                        me_rows.append({var(Sp, w): 1, var(S, w): -1, var(Sp, w2): -1, var(S, w2): 1})
            if S != 0:
                for w in range(n):  # increment at B equals increment at empty background
                    row = {}
                    for k, val in ((var(Sp, w), 1), (var(S, w), -1), (var(1 << p, w), -1), (var(0, w), 1)):
                        row[k] = row.get(k, 0) + val
                    bi_rows.append({k: x for k, x in row.items() if x})

    # representation (a): basis vectors
    basis_a = []
    for w0 in range(n):  # A(empty, w0) shifts every state at world w0
        basis_a.append({var(S, w0): 1 for S in dom})
    for S0 in dom:  # kappa(S0), S0 != empty: world-independent offset of state S0
        if S0:
            basis_a.append({var(S0, w): 1 for w in range(n)})
    for p in contingent:  # J_p [w in p] for every state containing p
        basis_a.append({var(S, w): 1 for S in dom if S >> p & 1 for w in range(n) if p >> w & 1})
    # representation (b): separable
    basis_b = []
    for w0 in range(n):
        basis_b.append({var(S, w0): 1 for S in dom})
    for p in range(NP):
        if p in contingent:
            for truth in (1, 0):  # value at worlds where p true / false
                basis_b.append({var(S, w): 1 for S in dom if S >> p & 1 for w in range(n) if (p >> w & 1) == truth})
        else:
            basis_b.append({var(S, w): 1 for S in dom if S >> p & 1 for w in range(n)})

    def satisfies(vec, rows):
        return all(sum(c * vec.get(k, 0) for k, c in row.items()) == 0 for row in rows)

    da, db = len(basis_a), len(basis_b)
    print(f"--- n={n}: |Dom|={len(dom)}, unknowns={NV}, ME rows={len(me_rows)}, BI rows={len(bi_rows)}")
    print(f"    expected dim (a) = n + (|Dom|-1) + #contingent = {n}+{len(dom)-1}+{len(contingent)} = {da}")
    print(f"    expected dim (b) = n + 2*#contingent + 2 = {db}")
    check(f"n={n}: (a) every representation basis vector satisfies ME", all(satisfies(v, me_rows) for v in basis_a))
    check(f"n={n}: (b) every separable basis vector satisfies ME and BI", all(satisfies(v, me_rows + bi_rows) for v in basis_b))
    for P in PRIMES:
        ra = rank_mod(basis_a, NV, P)
        rb = rank_mod(basis_b, NV, P)
        rme = rank_mod(me_rows, NV, P)
        rmebi = rank_mod(me_rows + bi_rows, NV, P)
        check(f"n={n}, p={P}: representation (a) basis independent (rank {ra} = {da})", ra == da)
        check(f"n={n}, p={P}: separable (b) basis independent (rank {rb} = {db})", rb == db)
        check(f"n={n}, p={P}: rank(ME) = {rme} = unknowns - dim(a) = {NV - da}  => ME space = family (a)", rme == NV - da)
        check(f"n={n}, p={P}: rank(ME+BI) = {rmebi} = unknowns - dim(b) = {NV - db}  => ME+BI space = separable", rmebi == NV - db)
    # Corollary: under ME, gain J_p^B independent of B; tau^B_p constant iff F^B_p constant iff BI.
    return dom


analyse(2)
analyse(3)

print("\n--- Footnote 3: ME + truth-directed measure on ALL states (3 worlds), J_p changes when complement believed")
n = 3
NP = 1 << n
FULL = NP - 1
comp = lambda p: FULL ^ p
designated = {1: 1, 6: 1, 2: 2, 5: 2, 4: 4, 3: 4}  # for each contingent pair, a designated member q


def A3(S, w):
    s = Fr(0)
    for p in range(NP):
        if S >> p & 1:
            s += 1 if p >> w & 1 else -2
    for p in range(NP):  # interaction for each complementary contingent pair believed together
        if p in designated and p == designated[p] and S >> p & 1 and S >> comp(p) & 1:
            s += Fr(-1, 2) if p >> w & 1 else 0
    return s


me_ok = td_ok = True
for S in range(1 << NP):
    for p in range(NP):
        if S >> p & 1:
            continue
        inc = [A3(S | 1 << p, w) - A3(S, w) for w in range(n)]
        for w in range(n):
            td_ok &= (inc[w] > 0) if p >> w & 1 else (inc[w] < 0)
            for w2 in range(n):
                if (p >> w & 1) == (p >> w2 & 1):
                    me_ok &= inc[w] == inc[w2]
check("fn3 example: ME holds on all 2^8 states", me_ok)
check("fn3 example: truth-directed on all 2^8 states", td_ok)
q = 1  # {w1}, designated member of the pair ({w1},{w2,w3})
J = lambda S, p: (A3(S | 1 << p, [w for w in range(n) if p >> w & 1][0]) - A3(S, [w for w in range(n) if p >> w & 1][0])) - \
                 (A3(S | 1 << p, [w for w in range(n) if not p >> w & 1][0]) - A3(S, [w for w in range(n) if not p >> w & 1][0]))
j0 = J(0, q)
j1 = J(1 << comp(q), q)
print(f"   J_p for p={{w1}}: background empty -> {j0}; background {{w2,w3}} (its complement) -> {j1}")
check("fn3 example: J_p changes when the complement of p is believed (proviso of Theorem 2 needed)", j0 != j1)

print("\nSUMMARY a2:", "ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
