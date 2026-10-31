#!/usr/bin/env python3
"""Exhaustive check of the A5 family claim (essay section 4, last paragraph).

STATUS: written by the triage agent on 2026-10-31 but NOT EXECUTED (no shell in
that session). The claim is established by the proof in
state/audit/A5/deepseek_triage.md; this script is an optional mechanical check.
Run:  python3 -I state/audit/A5/deepseek/family_check.py
Expected last line:  ALL CHECKS PASS

Setting: W = {0,1,2}; the 8 propositions; all 2^8 = 256 belief states.
Values scaled by 2 to stay in integers: T = 2, F = -4 (threshold 2/3, as in the
essay's T = 1, F = -2), premium BETA = 1 (< T).

Family (one member per state B0):
    A_{B0}(B, w) = S(B, w) + BETA * [ |B symdiff B0| >= 2 ] * [ w in core(B) ]
where S is the separable measure with values T, F.

Checks:
 (1) ME at each member's own state + BI across the family: for every B0, p not in
     B0 and w, A_{B0}(B0+p, w) - A_{B0}(B0, w) = v_p(w)  (T if w in p, else F).
 (2) Every member is strictly truth-directed from EVERY state (not just its own).
 (3) No member is separable on the domain without complementary pairs (the
     increment of adding p varies with the background inside the member), and
     the family is not constant.
 (4) For each test credence C: {B : B meets Proposition 4's condition for every p}
     == {B : B maximizes expected S-accuracy}.  Proposition 4's condition for p:
       p in B     -> E_C[A_{B-p}(B) - A_{B-p}(B-p)] >= 0
       p not in B -> E_C[A_B(B)     - A_B(B+p)]   >= 0
"""
from fractions import Fraction as Fr
from itertools import combinations
import random
import sys

W = (0, 1, 2)
FULL = frozenset(W)
PROPS = [frozenset(s) for r in range(len(W) + 1) for s in combinations(W, r)]
STATES = [frozenset(c) for r in range(len(PROPS) + 1) for c in combinations(PROPS, r)]
T, F, BETA = 2, -4, 1

def v(p, w):
    return T if w in p else F

CORE = {}
STAB = {}
for B in STATES:
    c = FULL
    for p in B:
        c = c & p
    CORE[B] = c
    for w in W:
        STAB[(B, w)] = sum(v(p, w) for p in B)

def A(B0, B, w):
    prem = BETA if (len(B ^ B0) >= 2 and w in CORE[B]) else 0
    return STAB[(B, w)] + prem

def has_comp_pair(B):
    return any((FULL - p) in B for p in B)

fail = []

# (1) own-state increments equal the separable values, for every member
for B0 in STATES:
    for p in PROPS:
        if p in B0:
            continue
        B1 = B0 | {p}
        for w in W:
            if A(B0, B1, w) - A(B0, B0, w) != v(p, w):
                fail.append(("own-state increment", sorted(map(sorted, B0)), sorted(p), w))
print("(1) own-state ME + cross-family BI:", "ok" if not fail else "FAIL")

# (2) strict truth-directedness of every member from every state
n2 = 0
for B0 in STATES:
    for B in STATES:
        for p in PROPS:
            if p in B:
                continue
            B1 = B | {p}
            for w in W:
                d = A(B0, B1, w) - A(B0, B, w)
                if (w in p and d <= 0) or (w not in p and d >= 0):
                    n2 += 1
print("(2) truth-directedness violations:", n2)
if n2:
    fail.append(("truth-directedness", n2))

# (3) each member non-separable on the domain; family not constant
nonsep = 0
for B0 in STATES:
    seen = {}
    found = False
    for B in STATES:
        if has_comp_pair(B):
            continue
        for p in PROPS:
            if p in B or has_comp_pair(B | {p}):
                continue
            for w in W:
                d = A(B0, B | {p}, w) - A(B0, B, w)
                key = (p, w)
                if key in seen and seen[key] != d:
                    found = True
                    break
                seen[key] = d
            if found:
                break
        if found:
            break
    nonsep += found
print("(3) members non-separable on the domain: %d of %d" % (nonsep, len(STATES)))
if nonsep != len(STATES):
    fail.append(("some member separable", len(STATES) - nonsep))
E, B1 = frozenset(), frozenset([frozenset([0])])
const = all(A(E, B, w) == A(B1, B, w) for B in STATES for w in W)
print("(3') family constant?", const)
if const:
    fail.append(("family constant",))

# (4) Proposition 4's conditions <=> optimality under S
def EA(B0, B, C):
    return sum(C[w] * A(B0, B, w) for w in W)

def ES(B, C):
    return sum(C[w] * STAB[(B, w)] for w in W)

def prop4_ok(B, C):
    for p in PROPS:
        if p in B:
            Bm = B - {p}
            if EA(Bm, B, C) - EA(Bm, Bm, C) < 0:
                return False
        else:
            if EA(B, B, C) - EA(B, B | {p}, C) < 0:
                return False
    return True

tests = [
    (Fr(7, 10), Fr(3, 20), Fr(3, 20)),
    (Fr(3, 4), Fr(1, 100), Fr(6, 25)),
    (Fr(2, 3), Fr(1, 6), Fr(1, 6)),      # C({w0}) exactly at threshold
    (Fr(2, 3), Fr(1, 3), Fr(0)),         # several propositions at threshold
    (Fr(1, 3), Fr(1, 3), Fr(1, 3)),
]
random.seed(20261031)
for _ in range(60):
    a, b, c = (random.randint(0, 30) for _ in range(3))
    s = a + b + c
    if s:
        tests.append((Fr(a, s), Fr(b, s), Fr(c, s)))

mism = 0
for C in tests:
    best = max(ES(B, C) for B in STATES)
    sopt = {B for B in STATES if ES(B, C) == best}
    p4 = {B for B in STATES if prop4_ok(B, C)}
    if sopt != p4:
        mism += 1
        fail.append(("prop4 != S-opt", tuple(map(str, C)), len(sopt), len(p4)))
print("(4) credences tested: %d; mismatches between Prop.4-set and S-optima: %d" % (len(tests), mism))
C0 = tests[0]
best = max(ES(B, C0) for B in STATES)
print("    S-optima at (7/10, 3/20, 3/20):",
      [sorted(sorted(p) for p in B) for B in STATES if ES(B, C0) == best])

if fail:
    print("FAILURES (first 10):", fail[:10])
    sys.exit(1)
print("ALL CHECKS PASS")
