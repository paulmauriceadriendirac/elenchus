#!/usr/bin/env python3
"""Independent audit implementation for essay A4 v6 (formal audit).

Implements, from Halpern (2015, arXiv:1505.00162v1, pp. 3-4):
  original HP  : AC2(a) + AC2(b)   (W set to w; all Z' subset of Z at actual values)
  updated HP   : AC2(a) + AC2(b^u) (all W' subset of W and all Z' subset of Z)
  modified HP  : AC2(a^m)          (W frozen at actual values)
AC1 and AC3 as in Definition 2.1. A Halpern-Hitchcock style normality filter is
applied to the AC2(a) witness world; AC3 is evaluated with the filtered AC2
("filter before AC3"). Candidates: every nonempty subset of the endogenous
variables (including outcome variables), at their actual values.

Does not import or reuse the author's code. Rerun: python3 hp_audit.py
"""
import itertools
import random
from collections import Counter

import sympy
import z3

DEFNS = ('orig', 'upd', 'mod')
R0, R1 = 'R0', 'R1'          # root at default / root deviant
CATS = ('n', 'l', 'f', 'u')
ROOTDEV = (R1, R0)           # transition: root deviant -> default


def subsets(seq):
    seq = list(seq)
    for k in range(len(seq) + 1):
        for c in itertools.combinations(seq, k):
            yield c


def proper_nonempty(X):
    for k in range(1, len(X)):
        for c in itertools.combinations(X, k):
            yield c


class Model:
    def __init__(self, name, order, roots, eqs, phi, phi_desc, defaults=None):
        self.name, self.order, self.roots, self.eqs = name, list(order), dict(roots), dict(eqs)
        self.phi, self.phi_desc = phi, phi_desc
        self.defaults = dict(defaults) if defaults else {v: 0 for v in self.order}
        assert set(self.roots) | set(self.eqs) == set(self.order)
        self._cache = {}
        self.actual = self.solve({})
        assert self.phi(self.actual), name
        self._wits = {}

    def solve(self, interv):
        key = tuple(sorted(interv.items()))
        if key not in self._cache:
            w = {}
            for v in self.order:
                if v in interv:
                    w[v] = interv[v]
                elif v in self.roots:
                    w[v] = self.roots[v]
                else:
                    w[v] = int(bool(self.eqs[v](w)))
            self._cache[key] = w
        return self._cache[key]

    def witness_worlds(self, X, defn):
        """Distinct AC2 witness worlds for candidate X (no normality). key -> list of (x', W, w)."""
        if (X, defn) in self._wits:
            return self._wits[(X, defn)]
        V, act = self.order, self.actual
        x = {v: act[v] for v in X}
        others = [v for v in V if v not in X]
        out = {}
        for xp in itertools.product((0, 1), repeat=len(X)):
            for W in subsets(others):
                wlist = [tuple(act[v] for v in W)] if defn == 'mod' else itertools.product((0, 1), repeat=len(W))
                for wv in wlist:
                    wd = dict(zip(W, wv))
                    iv = dict(zip(X, xp)); iv.update(wd)
                    world = self.solve(iv)
                    if self.phi(world):
                        continue                      # AC2(a) / AC2(a^m) fails
                    if defn in ('orig', 'upd'):
                        Z = [v for v in V if v not in W]          # X is a subset of Z
                        Wsubs = [W] if defn == 'orig' else list(subsets(W))
                        ok = all(self.phi(self.solve({**x, **{v: wd[v] for v in Wp}, **{v: act[v] for v in Zp}}))
                                 for Wp in Wsubs for Zp in subsets(Z))
                        if not ok:
                            continue                  # AC2(b) / AC2(b^u) fails
                    out.setdefault(tuple(world[v] for v in V), []).append((xp, W, wv))
        self._wits[(X, defn)] = out
        return out

    def cats(self, world):
        c = {}
        for v in self.order:
            d = self.defaults[v]
            if v in self.roots:
                c[v] = R0 if world[v] == d else R1
            else:
                e, val = int(bool(self.eqs[v](world))), world[v]
                c[v] = ('n' if e == val else 'f') if val == d else ('l' if e == val else 'u')
        return c

    def trans(self, world):
        ca, cw = self.cats(self.actual), self.cats(world)
        return {v: (ca[v], cw[v]) for v in self.order}

    def profile(self, world):
        t = self.trans(world)
        return tuple(sorted(t[v] for v in self.order if t[v][0] != t[v][1]))

    def world(self, key):
        return dict(zip(self.order, key))


def all_wits(m, defn):
    return {X: m.witness_worlds(X, defn) for X in subsets(m.order) if X}


def cause_table(m, defn, adm):
    W = all_wits(m, defn)
    sat = {X: any(adm(m, m.world(k)) for k in W[X]) for X in W}
    causes = [X for X in W if sat[X] and not any(sat[Y] for Y in proper_nonempty(X))]
    return sat, causes


def is_cause(causes, v):
    return (v,) in causes


def is_part(causes, v):
    return any(v in X for X in causes)


# ---------------------------------------------------------------- filters
NOFILTER = lambda m, w: True


def comp_admit(geq):
    def adm(m, w):
        for v, (ca, cw) in m.trans(w).items():
            if ca == cw:
                continue
            if ca in (R0, R1):
                if cw != R0:
                    return False
            elif (cw, ca) not in geq:
                return False
        return True
    return adm


def score(cat, v, r, a, b, c, d, cvar):
    if cat == R0:
        return r
    if cat == R1:
        return 0
    if cat == 'f' and cvar and v in cvar:
        return cvar[v]
    return {'n': a, 'l': b, 'f': c, 'u': d}[cat]


def gain(m, w, r, a, b, c, d, cvar=None):
    return sum(score(cw, v, r, a, b, c, d, cvar) - score(ca, v, r, a, b, c, d, cvar)
               for v, (ca, cw) in m.trans(w).items())


def add_admit(r, a, b, c, d, cvar=None):
    return lambda m, w: gain(m, w, r, a, b, c, d, cvar) >= 0


def conform_admit(m, w):
    cw = m.cats(w)
    return all(cw[v] not in ('f', 'u') for v in m.order if v not in m.roots)


# ---------------------------------------------------------------- models
def B(x):
    return int(bool(x))


def TAeq(w):
    return B((w['EF'] and not w['RB']) or (not w['EF'] and not w['LB']))


def late_like(name, s, b, sh, bh, out):
    return Model(name, [s, b, sh, bh, out], {s: 1, b: 1},
                 {sh: lambda w: w[s], bh: lambda w: B(w[b] and not w[sh]), out: lambda w: B(w[sh] or w[bh])},
                 lambda w: w[out] == 1, f'{out}=1')


M = {
    'prevention': Model('Genuine prevention', ['P', 'A', 'V'], {'P': 1, 'A': 1},
                        {'V': lambda w: B(w['P'] and not w['A'])}, lambda w: w['V'] == 0, 'V=0'),
    'chain': Model('Chain', ['C', 'I', 'Y'], {'C': 1}, {'I': lambda w: w['C'], 'Y': lambda w: w['I']},
                   lambda w: w['Y'] == 1, 'Y=1'),
    'boulder': Model('Boulder', ['F', 'B', 'K', 'H'], {'F': 1},
                     {'B': lambda w: w['F'], 'K': lambda w: w['F'], 'H': lambda w: B(w['B'] and not w['K'])},
                     lambda w: w['H'] == 0, 'H=0'),
    'short': Model('Short circuit', ['A', 'P', 'V'], {'A': 1},
                   {'P': lambda w: w['A'], 'V': lambda w: B(w['P'] and not w['A'])}, lambda w: w['V'] == 0, 'V=0'),
    'late': late_like('Late preemption', 'ST', 'BT', 'SH', 'BH', 'BS'),
    'tracks': Model('Tracks', ['F', 'LT', 'RT', 'A'], {'F': 1},
                    {'LT': lambda w: B(not w['F']), 'RT': lambda w: w['F'], 'A': lambda w: B(w['LT'] or w['RT'])},
                    lambda w: w['A'] == 1, 'A=1'),
    'doorbells': Model('Doorbells', ['M', 'T', 'L', 'R', 'E'], {'M': 1, 'T': 1},
                       {'L': lambda w: B(w['M'] and not w['T']), 'R': lambda w: B(w['M'] and w['T']),
                        'E': lambda w: B(w['L'] or w['R'])}, lambda w: w['E'] == 1, 'E=1'),
    'blocked': Model('Blocked tracks', ['EF', 'LB', 'RB', 'TA'], {'EF': 1, 'LB': 1, 'RB': 1}, {'TA': TAeq},
                     lambda w: w['TA'] == 0, 'TA=0'),
    'blocked_inertial': Model('Blocked tracks (inertial blockages)', ['EF', 'LB', 'RB', 'TA'],
                              {'EF': 1, 'LB': 1, 'RB': 1}, {'TA': TAeq}, lambda w: w['TA'] == 0, 'TA=0',
                              defaults={'EF': 0, 'LB': 1, 'RB': 1, 'TA': 0}),
    'clear': Model("Halpern's clear tracks", ['EF', 'LB', 'RB', 'TA'], {'EF': 1, 'LB': 0, 'RB': 0}, {'TA': TAeq},
                   lambda w: w['TA'] == 1, 'TA=1'),
    'switch3': Model("Halpern's 3-variable switch", ['F', 'T', 'A'], {'F': 1},
                     {'T': lambda w: w['F'], 'A': lambda w: 1}, lambda w: w['A'] == 1, 'A=1'),
    'sprinkler': late_like('Sprinkler', 'FF', 'SA', 'FW', 'SW', 'OUT'),
    'seedlings': Model('Seedlings', ['P', 'S', 'G', 'D', 'X'], {'P': 1, 'S': 1},
                       {'G': lambda w: B(w['P'] and w['S']), 'D': lambda w: B(w['P'] and not w['S']),
                        'X': lambda w: B(w['G'] or w['D'])}, lambda w: w['X'] == 1, 'X=1'),
}

FOCUS = {'prevention': 'A', 'chain': 'C', 'boulder': 'K', 'short': 'A', 'late': 'ST', 'tracks': 'F',
         'doorbells': 'T', 'blocked': 'EF', 'blocked_inertial': 'EF', 'clear': 'EF', 'switch3': 'F',
         'sprinkler': 'FF', 'seedlings': 'S'}

CHECKS = []


def check(label, cond, detail=''):
    CHECKS.append((label, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {label}" + (f"  -- {detail}" if detail else ''))


def fmt_world(m, key):
    return '(' + ','.join(f'{v}={x}' for v, x in zip(m.order, key)) + ')'


def P(*items):
    return tuple(sorted(items))


COMMON = P(ROOTDEV, ('n', 'f'), ('l', 'n'), ('l', 'n'))
PREV = P(ROOTDEV, ('n', 'l'))
CHAINP = P(ROOTDEV, ('l', 'n'), ('l', 'n'))

print('=' * 78)
print('A. Models: actual worlds')
for k, m in M.items():
    print(f"  {m.name:38s} actual {fmt_world(m, tuple(m.actual[v] for v in m.order))}  phi: {m.phi_desc}")
check('Blocked tracks actual (EF,LB,RB,TA)=(1,1,1,0)', tuple(M['blocked'].actual[v] for v in M['blocked'].order) == (1, 1, 1, 0))
check('Seedlings actual G=1, D=0, X=1', (M['seedlings'].actual['G'], M['seedlings'].actual['D'], M['seedlings'].actual['X']) == (1, 0, 1))

print('=' * 78)
print('B. Witness worlds of the focal single candidates (no normality), with profiles')
for k in ['prevention', 'chain', 'boulder', 'short', 'late', 'tracks', 'doorbells', 'blocked', 'clear', 'switch3', 'sprinkler', 'seedlings']:
    m = M[k]
    cands = [FOCUS[k]] + (['BT'] if k == 'late' else []) + (['I'] if k == 'chain' else [])
    for c in cands:
        for d in DEFNS:
            ww = m.witness_worlds((c,), d)
            desc = '; '.join(f"{fmt_world(m, key)} prof={m.profile(m.world(key))} via {ww[key][0]}" for key in ww) or 'NONE'
            print(f"  {m.name[:22]:22s} {c:3s} {d:4s}: {len(ww)} world(s): {desc}")

L, T_, D_ = M['late'], M['tracks'], M['doorbells']
for nm, m, c, key in [('Suzy', L, 'ST', (0, 1, 0, 0, 0)), ('Tracks flip', T_, 'F', (0, 0, 0, 0)),
                      ('Doorbells setting', D_, 'T', (1, 0, 0, 0, 0))]:
    ww = m.witness_worlds((c,), 'mod')
    check(f'Thm1: {nm} has exactly one modified witness world = {key}', list(ww) == [key])
    check(f'Thm1: {nm} modified witness profile = common profile', m.profile(m.world(key)) == COMMON)
ww = L.witness_worlds(('ST',), 'orig')
check('Older defs: Suzy has second witness world [ST<-0,BT<-0] = all zeros; profile = chain profile + 1 root',
      (0, 0, 0, 0, 0) in ww and (0, 0, 0, 0, 0) in L.witness_worlds(('ST',), 'upd')
      and L.profile(L.world((0, 0, 0, 0, 0))) == P(*CHAINP, ROOTDEV))
for nm, m, c in [('Tracks', T_, 'F'), ('Doorbells', D_, 'T')]:
    for d in ('orig', 'upd'):
        check(f'Older defs ({d}): {nm} switch has a unique witness world (same as modified)',
              list(m.witness_worlds((c,), d)) == list(m.witness_worlds((c,), 'mod')))
check('Doorbells: [T<-0, M<-0] violates sufficiency (not a witness under orig/upd)',
      all(not any(wt[1] == ('M',) and wt[2] == (0,) for lst in D_.witness_worlds(('T',), d).values() for wt in lst) for d in ('orig', 'upd')))
Bk = M['blocked']
for d in ('orig', 'upd'):
    ww = Bk.witness_worlds(('EF',), d)
    check(f'Thm2 ({d}): EF has witness world (0,0,1,1) with profile = prevention + one root dev->def',
          (0, 0, 1, 1) in ww and Bk.profile(Bk.world((0, 0, 1, 1))) == P(*PREV, ROOTDEV), f'worlds={list(ww)}')
check('Thm2: sufficiency: [EF<-1] and [EF<-1, LB<-0] both give TA=0',
      Bk.solve({'EF': 1})['TA'] == 0 and Bk.solve({'EF': 1, 'LB': 0})['TA'] == 0)
check('Modified: EF alone has no witness in Blocked tracks', len(Bk.witness_worlds(('EF',), 'mod')) == 0)
check('Modified: {EF,LB} has witness world (0,0,1,1) (the Thm 2 world)', (0, 0, 1, 1) in Bk.witness_worlds(('EF', 'LB'), 'mod'))
Pm = M['prevention']
for d in DEFNS:
    check(f'Prevention ({d}): only witness world (P,A,V)=(1,0,1), profile root dev->def + n->l',
          list(Pm.witness_worlds(('A',), d)) == [(1, 0, 1)] and Pm.profile(Pm.world((1, 0, 1))) == PREV)
    check(f'Chain ({d}): only witness [C<-0]', list(M['chain'].witness_worlds(('C',), d)) == [(0, 0, 0)])
    check(f'Short circuit ({d}): only witness world (A,P,V)=(0,1,1), P l->u, V n->l',
          list(M['short'].witness_worlds(('A',), d)) == [(0, 1, 1)]
          and M['short'].profile(M['short'].world((0, 1, 1))) == P(ROOTDEV, ('l', 'u'), ('n', 'l')))
Bo = M['boulder']
check('Boulder (mod): only (F,B,K,H)=(1,1,0,1), K l->f, H n->l',
      list(Bo.witness_worlds(('K',), 'mod')) == [(1, 1, 0, 1)] and Bo.profile(Bo.world((1, 1, 0, 1))) == P(('l', 'f'), ('n', 'l')))
for d in ('orig', 'upd'):
    check(f'Boulder ({d}): witness worlds exactly (1,1,0,1) and (0,1,0,1); B l->u in the latter',
          set(Bo.witness_worlds(('K',), d)) == {(1, 1, 0, 1), (0, 1, 0, 1)} and Bo.trans(Bo.world((0, 1, 0, 1)))['B'] == ('l', 'u'))
C3 = M['clear']
for d in ('orig', 'upd'):
    check(f'Clear tracks ({d}): flip witness [EF<-0, LB<-1], world (0,1,0,0)', list(C3.witness_worlds(('EF',), d)) == [(0, 1, 0, 0)])

print('=' * 78)
print('C. Verdicts without normality (all minimal causes; candidates of every size)')
for k, m in M.items():
    if k == 'blocked_inertial':
        continue
    for d in DEFNS:
        _, cs = cause_table(m, d, NOFILTER)
        print(f"  {m.name[:30]:30s} {d:4s} causes: {sorted(cs, key=lambda x: (len(x), x))}")
NF = {}
for k in ['prevention', 'chain', 'boulder', 'short', 'late', 'tracks', 'doorbells', 'blocked']:
    for d in DEFNS:
        NF[(k, d)] = cause_table(M[k], d, NOFILTER)[1]
check('No normality: every focal candidate is a cause or part of a cause under every definition',
      all(is_part(NF[(k, d)], FOCUS[k]) for k in ['prevention', 'chain', 'boulder', 'short', 'late', 'tracks', 'doorbells', 'blocked'] for d in DEFNS))
check("No normality: Billy's throw is NOT part of any cause under any definition (so 'every candidate above' excludes it)",
      all(not is_part(NF[('late', d)], 'BT') for d in DEFNS))
_, c3o = cause_table(C3, 'orig', NOFILTER); _, c3u = cause_table(C3, 'upd', NOFILTER); _, c3m = cause_table(C3, 'mod', NOFILTER)
check("Halpern 2015 verdicts: clear tracks flip a cause under orig and upd, not (single) under mod",
      is_cause(c3o, 'EF') and is_cause(c3u, 'EF') and not is_cause(c3m, 'EF'))
print(f"  NOTE clear tracks, modified, no normality: flip part of a cause? {is_part(c3m, 'EF')} causes={c3m}")
check("Halpern 2015 verdicts: both-blocked flip a cause under orig/upd, not (single) under mod",
      is_cause(NF[('blocked', 'orig')], 'EF') and is_cause(NF[('blocked', 'upd')], 'EF') and not is_cause(NF[('blocked', 'mod')], 'EF'))
check("Halpern 2015 verdicts: 3-variable switch flip not a cause (nor part) under all three",
      all(not is_part(cause_table(M['switch3'], d, NOFILTER)[1], 'F') for d in DEFNS))
check("Halpern 2015 verdicts: route model (Tracks) flip a cause under all three; short circuit antidote a cause under all three",
      all(is_cause(NF[('tracks', d)], 'F') and is_cause(NF[('short', d)], 'A') for d in DEFNS))

print('=' * 78)
print('D. Preorders on {n,l,f,u} and calibration')
pairs = [(x, y) for x in CATS for y in CATS if x != y]
PRE = []
for bits in range(1 << len(pairs)):
    rel = {(x, x) for x in CATS} | {p for i, p in enumerate(pairs) if bits >> i & 1}
    if all((x, z) in rel for (x, y) in rel for (y2, z) in rel if y == y2):
        PRE.append(frozenset(rel))
total = lambda R: all((x, y) in R or (y, x) in R for x in CATS for y in CATS)
antisym = lambda R: all(not ((x, y) in R and (y, x) in R) for x in CATS for y in CATS if x != y)
nW, nL, nPO = sum(map(total, PRE)), sum(1 for R in PRE if total(R) and antisym(R)), sum(map(antisym, PRE))
print(f'  preorders={len(PRE)} total preorders(weak orders)={nW} linear(total) orders={nL} partial orders={nPO}')
check('There are exactly 355 preorders on four categories', len(PRE) == 355)


def show(R):
    return '{' + ', '.join(f'{x}>={y}' for (x, y) in sorted(R) if x != y) + '}'


TABLES = {}


def tables(d, R):
    key = (d, R)
    if key not in TABLES:
        adm = comp_admit(R)
        TABLES[key] = {k: cause_table(M[k], d, adm)[1] for k in ['prevention', 'chain', 'boulder', 'short', 'late', 'tracks', 'doorbells', 'blocked', 'blocked_inertial']}
    return TABLES[key]


def calibrated(t, strict_short=False):
    ok = is_cause(t['prevention'], 'A') and is_cause(t['chain'], 'C') and is_cause(t['boulder'], 'K')
    return ok and (not is_part(t['short'], 'A') if strict_short else not is_cause(t['short'], 'A'))


CAL = {}
for d in DEFNS:
    CAL[d] = [R for R in PRE if calibrated(tables(d, R))]
    cal2 = [R for R in PRE if calibrated(tables(d, R), strict_short=True)]
    print(f'  {d}: calibrated preorders = {len(CAL[d])} (weak orders among them: {sum(map(total, CAL[d]))}, '
          f'linear orders: {sum(1 for R in CAL[d] if total(R) and antisym(R))}); with short-circuit antidote in no cause: {len(cal2)}')
    for R in CAL[d]:
        print(f'     {show(R)}  total={total(R)}')
    check(f'{d}: exactly five preorders give the four calibrating verdicts', len(CAL[d]) == 5)
    check(f'{d}: exactly two of the five are total PREorders (weak orders)', sum(map(total, CAL[d])) == 2)
    check(f"{d}: 'two of them total orders' read as linear orders (antisymmetric) -- expected FALSE", sum(1 for R in CAL[d] if total(R) and antisym(R)) == 2)
check('The five calibrated preorders are the same under all three definitions', set(CAL['orig']) == set(CAL['upd']) == set(CAL['mod']))
need = lambda R: ('l', 'n') in R and ('n', 'l') in R and ('f', 'l') in R and ('u', 'n') not in R
check('Calibrated set (mod) = {l>=n, n>=l, f>=l, not u>=n}', set(CAL['mod']) == {R for R in PRE if need(R)})

print('=' * 78)
print('E. Theorem 1 computational claims over all 355 preorders (modified definition)')
bad1, bad2, bad1b = [], [], []
for R in PRE:
    t = tables('mod', R)
    st, fp, tp = is_cause(t['late'], 'ST'), is_part(t['tracks'], 'F'), is_part(t['doorbells'], 'T')
    if not (st == fp == tp):
        bad1.append(R)
    if not (st == is_cause(t['tracks'], 'F') == is_cause(t['doorbells'], 'T')):
        bad1b.append(R)
    if not st and is_part(t['late'], 'ST'):
        cs = [X for X in t['late'] if 'ST' in X]
        if not all('BT' in X for X in cs):
            bad2.append((R, cs))
nconj = sum(1 for R in PRE if not is_cause(tables('mod', R)['late'], 'ST') and is_part(tables('mod', R)['late'], 'ST'))
check('Suzy cause <=> Tracks flip part of a cause <=> Doorbells setting part of a cause (all 355)', not bad1, f'{len(bad1)} exceptions')
check('Suzy cause <=> each switch-setting a (single) cause (all 355)', not bad1b, f'{len(bad1b)} exceptions')
check(f'Whenever Suzy is part of a cause only via a conjunction ({nconj} preorders), every such conjunction contains BT', not bad2, str(bad2[:2]))

print('=' * 78)
print('F. Corollary: exhaustive over 355 preorders; exact SMT over all anonymous Pareto filters and all real additive scores')


def desiderata(t):
    return (is_cause(t['prevention'], 'A') and is_cause(t['late'], 'ST') and not is_part(t['late'], 'BT')
            and not is_cause(t['doorbells'], 'T') and not is_cause(t['tracks'], 'F') and not is_cause(t['blocked'], 'EF'))


for d in DEFNS:
    ex = [R for R in PRE if desiderata(tables(d, R))]
    check(f'Corollary ({d}): no componentwise preorder meets all desiderata', not ex, f'{len(ex)} exceptions')

CORMODELS = ['prevention', 'late', 'tracks', 'doorbells', 'blocked']


def encode(d, admexpr, models=CORMODELS):
    """Return dict model -> (sat, cause) z3 expression maps, using admexpr(m, key)."""
    enc = {}
    for k in models:
        m = M[k]
        W = all_wits(m, d)
        sat = {X: z3.Or([admexpr(m, key) for key in W[X]]) if W[X] else z3.BoolVal(False) for X in W}
        cause = {X: z3.And(sat[X], z3.Not(z3.Or([sat[Y] for Y in proper_nonempty(X)] or [z3.BoolVal(False)]))) for X in W}
        enc[k] = (sat, cause)
    return enc


def conds(enc):
    c = enc
    return {
        'antidote cause': c['prevention'][1][('A',)],
        'Suzy cause': c['late'][1][('ST',)],
        'Billy in no cause': z3.And([z3.Not(v) for X, v in c['late'][1].items() if 'BT' in X]),
        'Doorbells setting not cause': z3.Not(c['doorbells'][1][('T',)]),
        'Tracks flip not cause': z3.Not(c['tracks'][1][('F',)]),
        'Blocked flip not cause': z3.Not(c['blocked'][1][('EF',)]),
    }


for d in DEFNS:
    profs = set()
    for k in CORMODELS:
        for X, ww in all_wits(M[k], d).items():
            for key in ww:
                profs.add(M[k].profile(M[k].world(key)))
    profs = sorted(profs)
    A = {p: z3.Bool('adm' + str(i)) for i, p in enumerate(profs)}
    pareto = []
    for p in profs:
        for q in profs:
            cp, cq = Counter(p), Counter(q)
            diff = cq - cp
            if p != q and not (cp - cq) and set(diff) == {ROOTDEV}:
                pareto.append(z3.Implies(A[p], A[q]))
    enc = encode(d, lambda m, key: A[m.profile(m.world(key))])
    C = conds(enc)
    s = z3.Solver(); s.add(pareto); s.add(list(C.values()))
    r = s.check()
    check(f'Corollary ({d}): UNSAT over ALL anonymous Pareto filters ({len(profs)} profiles, {len(pareto)} Pareto links)', r == z3.unsat, str(r))
    s2 = z3.Solver(); s2.add(list(C.values()))
    print(f'     ({d}) same desiderata without Pareto: {s2.check()}')
    for drop in C:
        s3 = z3.Solver(); s3.add(pareto); s3.add([v for kk, v in C.items() if kk != drop])
        print(f'     ({d}) drop "{drop}": {s3.check()}')
    # additive, exact over reals
    r_, a_, b_, c_, d_ = z3.Reals('r a b c d')

    def addexpr(m, key):
        return gain(m, m.world(key), r_, a_, b_, c_, d_) >= 0
    encA = encode(d, addexpr)
    sA = z3.Solver(); sA.add(r_ > 0); sA.add(list(conds(encA).values()))
    rA = sA.check()
    check(f'Corollary ({d}): UNSAT over all real additive scores with r>0', rA == z3.unsat, str(rA))

rng = random.Random(20261029)
cnt = 0
for _ in range(3000):
    sc = (rng.randint(1, 6), rng.randint(-6, 6), rng.randint(-6, 6), rng.randint(-6, 6), rng.randint(-6, 6))
    adm = add_admit(*sc)
    for d in DEFNS:
        t = {k: cause_table(M[k], d, adm)[1] for k in CORMODELS}
        if desiderata(t):
            cnt += 1
check('Corollary: 3,000 random integer additive scores (own seed), no exception under any definition', cnt == 0)

print('=' * 78)
print('G. Additive gain identities (sympy, computed from the model worlds)')
r, a, b, c, d = sympy.symbols('r a b c d')
G = lambda m, key, cvar=None: sympy.expand(gain(m, m.world(key), r, a, b, c, d, cvar))
gS, gT, gD = G(L, (0, 1, 0, 0, 0)), G(T_, (0, 0, 0, 0)), G(D_, (1, 0, 0, 0, 0))
gCh, gBo, gPr = G(M['chain'], (0, 0, 0)), G(Bo, (1, 1, 0, 1)), G(Pm, (1, 0, 1))
gBl, gBlI, gCl = G(Bk, (0, 0, 1, 1)), G(M['blocked_inertial'], (0, 0, 1, 1)), G(C3, (0, 1, 0, 0))
gBo2, gSz2 = G(Bo, (0, 1, 0, 1)), G(L, (0, 0, 0, 0, 0))
print(f'  g_Suzy={gS}  g_Tracks={gT}  g_Doorbells={gD}  g_Chain={gCh}  g_Boulder(mod)={gBo}')
print(f'  g_Prevention={gPr}  g_Blocked={gBl}  g_Blocked(inertial)={gBlI}  g_Clear={gCl}')
print(f'  g_Boulder second witness (older defs)={gBo2}  g_Suzy second witness (older defs)={gSz2}')
check('g_Doorbells = g_Tracks = g_Suzy = r + a - 2b + c', sympy.simplify(gD - gT) == 0 and sympy.simplify(gT - gS) == 0 and sympy.simplify(gS - (r + a - 2 * b + c)) == 0)
check('r+a-2b+c = (r+2a-2b)+(c-a) = g_Chain + g_Boulder', sympy.simplify(gS - (gCh + gBo)) == 0 and gCh == r + 2 * a - 2 * b and gBo == c - a)
check('g_Blocked = g_Prevention + r; gains r+b-a and 2r+b-a', sympy.simplify(gBl - gPr - r) == 0 and gPr == r + b - a)
check('Inertial coding: g_Blocked = b - a = g_Prevention - r', sympy.simplify(gBlI - (b - a)) == 0 and sympy.simplify(gBlI - (gPr - r)) == 0)
check('Clear tracks witness gain = a - b', sympy.simplify(gCl - (a - b)) == 0)
cBH, cL = sympy.symbols('c_BH c_L')
dd = sympy.expand(gain(L, L.world((0, 1, 0, 0, 0)), r, a, b, c, d, {'BH': cBH}) - gain(D_, D_.world((1, 0, 0, 0, 0)), r, a, b, c, d, {'L': cL}))
check('Mechanism-specific scores: Suzy gain minus Doorbells gain = c_BH - c_L', sympy.simplify(dd - (cBH - cL)) == 0, str(dd))

print('=' * 78)
print('H. Boundary score (r,a,b,c,d)=(2,0,-1,-5,-3)')
bnd = add_admit(2, 0, -1, -5, -3)
for d in DEFNS:
    t = {k: cause_table(M[k], d, bnd)[1] for k in M}
    print(f"  {d}: prev A {is_cause(t['prevention'],'A')} | chain C {is_cause(t['chain'],'C')} | ducking K {is_cause(t['boulder'],'K')} | "
          f"short A {is_cause(t['short'],'A')}/part {is_part(t['short'],'A')} | Suzy {is_cause(t['late'],'ST')} | Billy part {is_part(t['late'],'BT')} | "
          f"Tracks F {is_cause(t['tracks'],'F')}/part {is_part(t['tracks'],'F')} | Doorbells T {is_cause(t['doorbells'],'T')}/part {is_part(t['doorbells'],'T')} | "
          f"Blocked EF {is_cause(t['blocked'],'EF')}/part {is_part(t['blocked'],'EF')} | Clear EF {is_cause(t['clear'],'EF')}/part {is_part(t['clear'],'EF')}")
    if d in ('orig', 'upd'):
        check(f'Boundary ({d}): keeps prevention, chain, ducking, Suzy; excludes Tracks and Doorbells switches; counts Blocked flip and clear-tracks flip',
              is_cause(t['prevention'], 'A') and is_cause(t['chain'], 'C') and is_cause(t['boulder'], 'K') and is_cause(t['late'], 'ST')
              and not is_cause(t['tracks'], 'F') and not is_cause(t['doorbells'], 'T') and is_cause(t['blocked'], 'EF') and is_cause(t['clear'], 'EF'))

print('=' * 78)
print('I. Remark: modified definition, Blocked tracks, flip part of a cause')
badI = [R for R in PRE if is_part(tables('mod', R)['blocked'], 'EF') != (('l', 'n') in R)]
check('Modified: flip part of a cause in Blocked tracks iff l>=n (all 355 preorders)', not badI, f'{len(badI)} exceptions')
okI = all((('EF', 'LB') in tables('mod', R)['blocked']) == (('l', 'n') in R) for R in PRE)
check('Modified: {EF,LB} is a cause iff l>=n (all 355 preorders)', okI)
print('  causes in Blocked tracks (mod) under a calibrated preorder:', tables('mod', CAL['mod'][0])['blocked'])

print('=' * 78)
print('J. Section 5: mechanism-specific score, Sprinkler, Seedlings (modified definition)')
cv = {'L': -5, 'LT': -5}
mech = lambda m, w: gain(m, w, 2, 0, -1, 0, -3, cv if m.name in ('Doorbells', 'Tracks') else None) >= 0
t = {k: cause_table(M[k], 'mod', mech)[1] for k in M}
check('Mech score (mod): antidote, chain start, ducking, Suzy are causes',
      is_cause(t['prevention'], 'A') and is_cause(t['chain'], 'C') and is_cause(t['boulder'], 'K') and is_cause(t['late'], 'ST'))
check('Mech score (mod): Billy, Tracks flip, Doorbells setting out of every cause',
      not is_part(t['late'], 'BT') and not is_part(t['tracks'], 'F') and not is_part(t['doorbells'], 'T'))
print(f"  (extra) short-circuit antidote part of a cause under mech score: {is_part(t['short'], 'A')}")
sp = cause_table(M['sprinkler'], 'mod', lambda m, w: gain(m, w, 2, 0, -1, 0, -3, {'SW': -5}) >= 0)[1]
print('  Sprinkler causes (c_SW=-5):', sp)
check('Sprinkler: firefighter not a cause by itself; every cause containing it contains the sprinkler activation; activation part of a cause',
      not is_cause(sp, 'FF') and is_part(sp, 'FF') and all('SA' in X for X in sp if 'FF' in X) and is_part(sp, 'SA'))
sd = cause_table(M['seedlings'], 'mod', lambda m, w: gain(m, w, 2, 0, -1, 0, -3, {'D': -5}) >= 0)[1]
print('  Seedlings causes (c_D=-5):', sd)
check('Seedlings: swarm not even part of a cause (c_D=-5, modified)', not is_part(sd, 'S'))
mp = {'P': 'M', 'S': 'T', 'G': 'R', 'D': 'L', 'X': 'E'}
Sd = M['seedlings']
iso = all(Sd.actual[v] == D_.actual[mp[v]] and Sd.defaults[v] == D_.defaults[mp[v]] for v in Sd.order)
for vals in itertools.product((0, 1), repeat=5):
    w = dict(zip(Sd.order, vals)); w2 = {mp[v]: x for v, x in w.items()}
    for v in Sd.eqs:
        iso &= int(bool(Sd.eqs[v](w))) == int(bool(D_.eqs[mp[v]](w2)))
check('Seedlings -> Doorbells map preserves equations, actual values and defaults', iso and set(mp[v] for v in Sd.roots) == set(D_.roots))

print('=' * 78)
print('K. Inertial coding of standing blockages (LB, RB default 1)')
for d in ('orig', 'upd'):
    ok = all((not is_cause(tables(d, R)['blocked_inertial'], 'EF')) and is_cause(tables(d, R)['prevention'], 'A') for R in CAL[d])
    check(f'Inertial ({d}): for all five calibrated preorders the Blocked flip is not a cause and the antidote is', ok)
    print(f"     ({d}) Blocked flip part of a cause under inertial coding, by calibrated preorder: {[is_part(tables(d, R)['blocked_inertial'], 'EF') for R in CAL[d]]}")

print('=' * 78)
print('L. Exceptionless conformity (modified): admit only witness worlds with no f/u')
tc = {k: cause_table(M[k], 'mod', conform_admit)[1] for k in M}
check('Conformity: ducking not part of any cause; chain intermediate I=1 not a cause (nor part)',
      not is_part(tc['boulder'], 'K') and not is_part(tc['chain'], 'I'))
check("Conformity: late preemption -- {ST,BT} is a cause, Suzy not a cause alone, Billy part of a cause",
      ('ST', 'BT') in tc['late'] and not is_cause(tc['late'], 'ST') and is_part(tc['late'], 'BT'))
allroots = all(all(v in M[k].roots for v in X) for k in tc for X in tc[k])
check('Conformity: every cause in every model consists of roots only (Lemma consequence)', allroots)
exc = [R for R in PRE if not any(p in R for p in [('f', 'n'), ('f', 'l'), ('u', 'n'), ('u', 'l')]) and ('n', 'l') in R]
okL = all(not is_part(tables('mod', R)['boulder'], 'K') and ('ST', 'BT') in tables('mod', R)['late'] for R in exc)
check(f'Exceptionless componentwise preorders with n>=l ({len(exc)}): ducking lost and {{ST,BT}} a cause in all', okL)

print('=' * 78)
fails = [l for l, ok in CHECKS if not ok]
print(f'SUMMARY: {len(CHECKS)} checks, {len(CHECKS) - len(fails)} pass, {len(fails)} fail')
for l in fails:
    print('  FAIL:', l)
