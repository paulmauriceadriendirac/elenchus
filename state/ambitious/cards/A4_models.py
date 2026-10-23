"""
Binary structural-equation models and implementations of several accounts of actual causation:
  - HP original / updated / modified (Halpern & Pearl 2005; Halpern 2015 arXiv:1505.00162)
  - HH normality extension (Halpern & Hitchcock 2015, arXiv:1309.1226): witness must be >= actual
  - NESS / BV / CNESS (Beckers 2021, AAAI; arXiv:2012.05123)
  - Andreas & Guenther 2024a (PPQ 105:2-32) final theory: conditions (1)-(5)
  - Andreas & Guenther 2024b (Phil Stud 181:2145-2176) Definition 2: conditions (i)-(v)
Variables are binary (0/1). Roots are variables without equations; their actual values are the context.
"""
import itertools
from functools import lru_cache

class Model:
    def __init__(self, roots, eqs, order=None, name=""):
        # roots: dict var->actual value ; eqs: dict var -> (parents tuple, function(dict)->0/1)
        self.name = name
        self.roots = dict(roots)
        self.eqs = dict(eqs)
        self.vars = list(roots.keys()) + [v for v in (order or eqs.keys()) if v not in roots]
        assert set(self.vars) == set(roots) | set(eqs)
        # topological order
        self.order = self._topo()
        self.actual = self.solve({})
    def _topo(self):
        done, out = set(self.roots), list(self.roots)
        rem = [v for v in self.vars if v not in self.roots]
        while rem:
            prog = False
            for v in list(rem):
                if all(p in done for p in self.eqs[v][0]):
                    out.append(v); done.add(v); rem.remove(v); prog = True
            assert prog, "cycle"
        return out
    def parents(self, v):
        return self.eqs[v][0] if v in self.eqs else ()
    def f(self, v, world):
        ps, fn = self.eqs[v]
        return int(fn({p: world[p] for p in ps}))
    def solve(self, interv, roots=None):
        w = {}
        r = self.roots if roots is None else roots
        for v in self.order:
            if v in interv: w[v] = interv[v]
            elif v in r and v not in self.eqs: w[v] = r[v]
            else: w[v] = self.f(v, w)
        return w
    def children(self, v):
        return [u for u in self.eqs if v in self.eqs[u][0]]
    def descendants(self, v):
        out, stack = set(), [v]
        while stack:
            x = stack.pop()
            for c in self.children(x):
                if c not in out: out.add(c); stack.append(c)
        return out
    def ancestors(self, v):
        return {u for u in self.vars if v in self.descendants(u)}

def subsets(xs):
    xs = list(xs)
    for r in range(len(xs)+1):
        for c in itertools.combinations(xs, r):
            yield c

# ---------------------------------------------------------------- HP family
def hp_ac2(M, X, phi, version, normal=None):
    """X: dict var->value (the candidate conjunction, actual values). phi: function(world)->bool.
    version: 'orig','upd','mod'. normal: None or function(world)->bool meaning witness >= actual.
    Returns list of witnesses (W dict, x' dict, world) satisfying AC2."""
    act = M.actual
    others = [v for v in M.vars if v not in X]
    wits = []
    xprimes = [dict(zip(X, vals)) for vals in itertools.product([0,1], repeat=len(X)) if any(vals[i]!=X[k] for i,k in enumerate(X))]
    for xp in xprimes:
        if version == 'mod':
            for W in subsets(others):
                wd = {v: act[v] for v in W}
                world = M.solve({**xp, **wd})
                if not phi(world):
                    if normal is None or normal(world):
                        wits.append((wd, xp, world))
        else:
            for W in subsets(others):
                Z = [v for v in others if v not in W]
                for wvals in itertools.product([0,1], repeat=len(W)):
                    wd = dict(zip(W, wvals))
                    world = M.solve({**xp, **wd})
                    if phi(world):
                        continue
                    if normal is not None and not normal(world):
                        continue
                    ok = True
                    # AC2(b): for all subsets Z' of Z (Z excludes X? HP: X subset of Z; we include X separately)
                    Wsubs = list(subsets(W)) if version == 'upd' else [tuple(W)]
                    for Ws in Wsubs:
                        for Zs in subsets(Z):
                            interv = {**X, **{v: wd[v] for v in Ws}, **{v: act[v] for v in Zs}}
                            if not phi(M.solve(interv)):
                                ok = False; break
                        if not ok: break
                    if ok:
                        wits.append((wd, xp, world))
    return wits

def hp_cause(M, X, phi, version, normal=None):
    act = M.actual
    if any(act[k] != v for k, v in X.items()): return False
    if not phi(act): return False
    if not hp_ac2(M, X, phi, version, normal): return False
    # AC3 minimality: no proper nonempty subset satisfies AC1 and AC2
    keys = list(X)
    for r in range(1, len(keys)):
        for sub in itertools.combinations(keys, r):
            if hp_ac2(M, {k: X[k] for k in sub}, phi, version, normal):
                return False
    return True

def hp_part_of_cause(M, var, phi, version, normal=None, maxsize=3):
    act = M.actual
    others = [v for v in M.vars if v != var]
    for r in range(0, maxsize):
        for sub in itertools.combinations(others, r):
            X = {var: act[var], **{k: act[k] for k in sub}}
            if hp_cause(M, X, phi, version, normal):
                return X
    return None

# ---------------------------------------------------------------- Beckers NESS family
def sufficient(M, xs, E, e):
    """xs: dict of var->val. Sufficient for E=e iff f_E forced to e for all values of E's parents not in xs."""
    ps = M.parents(E)
    free = [p for p in ps if p not in xs]
    for vals in itertools.product([0,1], repeat=len(free)):
        w = {**{p: xs[p] for p in ps if p in xs}, **dict(zip(free, vals))}
        if M.f(E, w) != e: return False
    return True

def direct_ness(M, world, C, c, E, e):
    """C=c directly NESS-causes E=e w.r.t. the world (actual solution of M)."""
    if E not in M.eqs: return False
    if world[C] != c or world[E] != e: return False
    ps = [p for p in M.parents(E) if p != C]
    # by Prop 2 witness can be taken within parents
    for W in subsets(ps):
        wd = {v: world[v] for v in W}
        if sufficient(M, {C: c, **wd}, E, e) and not sufficient(M, wd, E, e):
            return True
    return False

def ness_paths(M, world, C, c, E, e, maxlen=None):
    """Return set of paths (tuples of intermediate vars) along which C=c NESS-causes E=e in world."""
    res = set()
    def rec(cur, val, path):
        if direct_ness(M, world, cur, val, E, e):
            res.add(tuple(path))
        for ch in M.children(cur):
            if ch == E or ch in path: continue
            if direct_ness(M, world, cur, val, ch, world[ch]):
                rec(ch, world[ch], path + [ch])
    rec(C, c, [])
    return res

def ness_cause(M, C, E):
    w = M.actual
    return len(ness_paths(M, w, C, w[C], E, w[E])) > 0

def intervene_model(M, C, val):
    roots = dict(M.roots); eqs = dict(M.eqs)
    if C in eqs: del eqs[C]
    roots[C] = val
    return Model(roots, eqs, name=M.name+f"[{C}<-{val}]")

def bv_cause(M, C, E):
    w = M.actual
    if not ness_cause(M, C, E): return False
    c = w[C]; e = w[E]
    Mc = intervene_model(M, C, 1-c)
    wc = Mc.actual
    return len(ness_paths(Mc, wc, C, 1-c, E, e)) == 0 if wc[E]==e else True

def cness_cause(M, C, E):
    w = M.actual
    c, e = w[C], w[E]
    paths = ness_paths(M, w, C, c, E, e)
    if not paths: return False
    Mc = intervene_model(M, C, 1-c)
    wc = Mc.actual
    cpaths = ness_paths(Mc, wc, C, 1-c, E, e) if wc[E] == e else set()
    for p in paths:
        ok = True
        for q in cpaths:
            if set(q) <= set(p):
                ok = False; break
        if ok: return True
    return False

# ---------------------------------------------------------------- Andreas & Guenther
# literals: (var, val) ; a fact set F is the set of actual literals.
def ag_entails(M, laws, facts, target):
    """laws: set of vars whose laws are included; facts: dict var->val; target: (var,val).
    Classical entailment over all valuations of all variables."""
    vs = M.vars
    for vals in itertools.product([0,1], repeat=len(vs)):
        w = dict(zip(vs, vals))
        if any(w[k] != v for k, v in facts.items()): continue
        if any(w[x] != M.f(x, w) for x in laws): continue
        if w[target[0]] != target[1]: return False
    return True

def ag_entails_fast(M, laws, facts, target):
    # same semantics, but enumerate only free vars smartly: brute force is fine for <= 9 vars
    return ag_entails(M, laws, facts, target)

def ag_cause(M, C, E, dev, version='2024b', allow_drop=True):
    """dev: function(var,val)->True if literal (var=val) is more deviant than its negation.
    version: '2024a' (PPQ final theory, conds (1)-(5)), '2024b' (Phil Stud Def 2, conds (i)-(v)),
             'prelim' (2024a Def 1: no L', no deviancy), 'def2-no-dev' (2024a Def 2 conds 1-3 + 5 w/o deviancy).
    Returns a witness (L', F') or None."""
    act = M.actual
    Cl = (C, act[C]); El = (E, act[E])
    allfacts = dict(act)
    lawvars = list(M.eqs.keys())
    descC = M.descendants(C)
    ancC = M.ancestors(C)
    # condition on L': (5)/(iv): laws of all descendants of C must be in L'
    must = [v for v in lawvars if v in descC]
    optional = [v for v in lawvars if v not in descC]
    Lchoices = [tuple(must) + s for s in subsets(optional)] if allow_drop and version != 'prelim' else [tuple(lawvars)]
    factvars = [v for v in M.vars]
    for Lp in Lchoices:
        Lp = set(Lp)
        # enumerate F' subsets of facts (excluding nothing a priori)
        for Fv in subsets(factvars):
            Fp = {v: act[v] for v in Fv}
            # (2)/(iii): <L',F'> does not entail E, and F' maximal
            if ag_entails(M, Lp, Fp, El): continue
            maximal = True
            for v in factvars:
                if v in Fp: continue
                if not ag_entails(M, Lp, {**Fp, v: act[v]}, El):
                    maximal = False; break
            if not maximal: continue
            # (3)/(ii): <L',{}>[F'][{C}] |= E : setting removes laws of vars in F' and C
            Lset = {x for x in Lp if x not in Fp and x != C}
            if not ag_entails(M, Lset, {**Fp, C: act[C]}, El): continue
            # deviancy
            rest = [v for v in factvars if v not in Fp]
            ok = True
            if version == '2024a':
                roots_in_L = [v for v in M.vars if v not in M.eqs]   # root propositions: no law in L
                for v in rest:
                    if v == C or v in roots_in_L:
                        if not dev(v, act[v]): ok = False; break
            elif version == '2024b':
                for v in rest:
                    if v not in descC and v not in ancC:
                        if not dev(v, act[v]): ok = False; break
            elif version == '2024b-fwd':   # repaired: only forward candidates must be deviant
                for v in rest:
                    if v not in descC and v not in ancC:
                        if v == C:
                            if not dev(v, act[v]): ok = False; break
                            continue
                        Lset2 = {x for x in Lp if x not in Fp and x != v}
                        if ag_entails(M, Lset2, {**Fp, v: act[v]}, El):
                            if not dev(v, act[v]): ok = False; break
            if ok:
                return (sorted(Lp), Fp)
    return None

def default_dev(norm_violations=()):
    """occurrence (val 1) more deviant than absence, unless the absence violates an active norm."""
    nv = set(norm_violations)
    def dev(v, val):
        if v in nv: return val == 0
        return val == 1
    return dev

# ===================== battery and checks (appended) =====================
if __name__ == '__main__':
    import runpy, os, sys
    print('library loaded; run A4_checks via: python3 A4_models.py --checks')
