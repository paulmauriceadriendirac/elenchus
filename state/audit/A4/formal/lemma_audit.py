#!/usr/bin/env python3
"""Self-contained check of the Lemma (frozen witnesses), essay A4 v6, Section 6.

Lemma: under the modified HP definition (Halpern 2015, AC2(a^m)), if X=x is a cause of phi
with a witness whose world violates no non-root equation, then every member of X is a root
and [X <- x'] not-phi (counterfactual dependence, nothing frozen).
Checked (i) without normality, (ii) with random componentwise normality filters applied
before AC3, on: all acyclic binary models with 3 variables (exhaustive) and random models
with 4-6 variables. Formulas phi: every literal true in the actual world, plus random
conjunctions/disjunctions of two such literals. Rerun: python3 lemma_audit.py
"""
import itertools, random

def subsets(s):
    s = list(s)
    for k in range(len(s) + 1):
        yield from itertools.combinations(s, k)

def solve(model, iv):
    n, roots, eqs = model
    w = []
    for i in range(n):
        if i in iv: w.append(iv[i])
        elif i in roots: w.append(roots[i])
        else:
            pa, tt = eqs[i]
            w.append(tt[sum(w[p] << j for j, p in enumerate(pa))])
    return w

def eqval(model, w, i):
    pa, tt = model[2][i]
    return tt[sum(w[p] << j for j, p in enumerate(pa))]

def conforming(model, w):
    return all(eqval(model, w, i) == w[i] for i in model[2])

def cats(model, w):
    # default 0 for every variable; roots: 'R0'/'R1'; non-roots n,l,f,u
    out = []
    for i in range(model[0]):
        if i in model[1]: out.append('R0' if w[i] == 0 else 'R1')
        else:
            e = eqval(model, w, i)
            out.append(('n' if e == w[i] else 'f') if w[i] == 0 else ('l' if e == w[i] else 'u'))
    return out

def mod_witnesses(model, X, phi, act):
    res = []
    others = [i for i in range(model[0]) if i not in X]
    for xp in itertools.product((0, 1), repeat=len(X)):
        for W in subsets(others):
            iv = dict(zip(X, xp)); iv.update({i: act[i] for i in W})
            w = solve(model, iv)
            if not phi(w):
                res.append((xp, W, w))
    return res

CATS = ('n', 'l', 'f', 'u')
PAIRS = [(x, y) for x in CATS for y in CATS if x != y]
PRE = []
for bits in range(1 << 12):
    rel = {(x, x) for x in CATS} | {p for k, p in enumerate(PAIRS) if bits >> k & 1}
    if all((x, z) in rel for (x, y) in rel for (y2, z) in rel if y == y2):
        PRE.append(frozenset(rel))
assert len(PRE) == 355

def admit(R, ca, cw):
    if R is None: return True
    for a, b in zip(ca, cw):
        if a == b: continue
        if a in ('R0', 'R1'):
            if b != 'R0': return False
        elif (b, a) not in R: return False
    return True

stats = dict(models=0, phis=0, causes=0, conf_wit=0, cex=0, filt_causes=0, filt_conf_wit=0)

def check_model(model, rng, filters):
    act = solve(model, {})
    n = model[0]
    lits = [(lambda i, v: (lambda w: w[i] == v))(i, act[i]) for i in range(n)]
    phis = list(lits)
    for _ in range(2):
        i, j = rng.randrange(n), rng.randrange(n)
        f1, f2 = lits[i], lits[j]
        phis.append(lambda w, f1=f1, f2=f2: f1(w) and f2(w))
        phis.append(lambda w, f1=f1, f2=f2: f1(w) or f2(w))
    stats['models'] += 1
    ca = cats(model, act)
    for phi in phis:
        stats['phis'] += 1
        cands = [X for X in subsets(range(n)) if X]
        wit = {X: mod_witnesses(model, X, phi, act) for X in cands}
        for R in filters:
            sat = {X: any(admit(R, ca, cats(model, w)) for (_, _, w) in wit[X]) for X in cands}
            for X in cands:
                if not sat[X] or any(sat[Y] for k in range(1, len(X)) for Y in itertools.combinations(X, k)):
                    continue
                stats['causes' if R is None else 'filt_causes'] += 1
                for (xp, W, w) in wit[X]:
                    if not admit(R, ca, cats(model, w)) or not conforming(model, w):
                        continue
                    stats['conf_wit' if R is None else 'filt_conf_wit'] += 1
                    allroots = all(i in model[1] for i in X)
                    butfor = not phi(solve(model, dict(zip(X, xp))))
                    if not (allroots and butfor):
                        stats['cex'] += 1
                        print('COUNTEREXAMPLE', model, X, xp, W)

rng = random.Random(1505)
# exhaustive: all models on 3 variables in fixed topological order 0<1<2
def var_options(i):
    opts = [('root', 0), ('root', 1)]
    for pa in subsets(range(i)):
        if not pa: continue
        for tt in itertools.product((0, 1), repeat=1 << len(pa)):
            opts.append(('eq', (pa, tt)))
    return opts
count3 = 0
for o0 in var_options(0):
    for o1 in var_options(1):
        for o2 in var_options(2):
            roots, eqs = {}, {}
            for i, o in enumerate((o0, o1, o2)):
                if o[0] == 'root': roots[i] = o[1]
                else: eqs[i] = o[1]
            check_model((3, roots, eqs), rng, [None, rng.choice(PRE)])
            count3 += 1
print(f'exhaustive 3-variable models: {count3}')
# random models with 4-6 variables
for _ in range(1500):
    n = rng.choice((4, 5, 6))
    roots, eqs = {}, {}
    for i in range(n):
        if i == 0 or rng.random() < 0.3:
            roots[i] = rng.randint(0, 1)
        else:
            k = rng.randint(1, min(3, i))
            pa = tuple(sorted(rng.sample(range(i), k)))
            eqs[i] = (pa, tuple(rng.randint(0, 1) for _ in range(1 << k)))
    check_model((n, roots, eqs), rng, [None, rng.choice(PRE)])
print(stats)
print('LEMMA', 'VERIFIED (no counterexample)' if stats['cex'] == 0 else 'COUNTEREXAMPLES FOUND')
