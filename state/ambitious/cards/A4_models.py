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


# =====================================================================================
# Battery, typicality schemes and the checks used by the A4 cards (run: python3 A4_models.py --checks)
# =====================================================================================
import random, collections

def eq(ps, fn): return (tuple(ps), fn)

# ---- A&G models (boxes of A&G 2024a pp. 11-25; mentor model from A&G 2024b fn. 2)
AG = {}
AG['overdet'] = (Model({'C':1,'A':1}, {'E': eq(['C','A'], lambda w: w['C'] or w['A'])}), 'E', {'C':True,'A':True})
AG['preempt'] = (Model({'C':1,'A':1}, {'D': eq(['C'], lambda w: w['C']), 'B': eq(['A','C'], lambda w: w['A'] and not w['C']),
                  'E': eq(['D','B'], lambda w: w['D'] or w['B'])}), 'E', {'C':True,'D':True,'A':False})
AG['bogus'] = (Model({'F':1,'D':0}, {'E': eq(['F','D'], lambda w: (not w['F']) and w['D'])}), 'E', {'F':False,'D':False})
AG['omission'] = (Model({'F':0,'C':1}, {'E': eq(['F','C'], lambda w: (not w['F']) and w['C'])}), 'E', {'F':False,'C':True})
AG['subcause'] = (Model({'A':1}, {'C': eq(['A'], lambda w: w['A']), 'E': eq(['C','A'], lambda w: w['C'] and w['A'])}), 'E', {'C':True,'A':True})
AG['shortcircuit'] = (Model({'F':1}, {'B': eq(['F'], lambda w: w['F']), 'D': eq(['F'], lambda w: w['F']),
                       'E': eq(['B','D'], lambda w: w['B'] and not w['D'])}), 'E', {'D':True,'F':False})
AG['EDP'] = (Model({'A':1,'F':1}, {'B': eq(['F'], lambda w: w['F']), 'C': eq(['F'], lambda w: w['F']),
              'D': eq(['B','C'], lambda w: w['B'] and not w['C']), 'E': eq(['A','D'], lambda w: w['A'] and not w['D'])}), 'E', {'C':True,'A':True,'F':False})
AG['MEDP'] = (Model({'A':1,'G':0,'F':1}, {'B': eq(['G','F'], lambda w: w['G'] or w['F']), 'C': eq(['F'], lambda w: w['F']),
               'D': eq(['B','C'], lambda w: w['B'] and not w['C']), 'E': eq(['A','D'], lambda w: w['A'] and not w['D'])}), 'E', {'C':True,'A':True,'F':False})
AG['isoMEDP'] = (Model({'A':1,'G':1,'C':1}, {'B': eq(['G','C'], lambda w: w['G'] and not w['C']), 'H': eq(['C'], lambda w: w['C']),
                  'D': eq(['B','H'], lambda w: w['B'] or w['H']), 'E': eq(['A','D'], lambda w: w['A'] and w['D'])}), 'E', {'C':True,'H':True,'D':True,'A':True})
AG['switch'] = (Model({'F':1}, {'L': eq(['F'], lambda w: not w['F']), 'R': eq(['F'], lambda w: w['F']),
                 'E': eq(['L','R'], lambda w: w['L'] or w['R'])}), 'E', {'R':True,'F':False})
AG['mentor'] = (Model({'F':1,'B':1}, {'D': eq(['B'], lambda w: not w['B']), 'E': eq(['F','D'], lambda w: (not w['F']) and w['D'])}), 'E', {'F':False,'B':True})

# ---- normal-backup preemption (locusts) and variants; control with deviant backup trigger
NBP = {}
NBP['NBP1'] = Model({'Lo':1,'R':0}, {'D': eq(['R','Lo'], lambda w: (not w['R']) and not w['Lo']), 'E': eq(['Lo','D'], lambda w: w['Lo'] or w['D'])})
NBP['NBP2_shared_deviant_root'] = Model({'P':1,'Lo':1,'R':0}, {'D': eq(['P','R','Lo'], lambda w: w['P'] and (not w['R']) and not w['Lo']),
                                     'E': eq(['P','Lo','D'], lambda w: (w['P'] and w['Lo']) or w['D'])})
NBP['NBP3_backup_specific_deviant_root'] = Model({'T':1,'Lo':1,'R':0}, {'D': eq(['T','R','Lo'], lambda w: w['T'] and (not w['R']) and not w['Lo']),
                                     'E': eq(['Lo','D'], lambda w: w['Lo'] or w['D'])})
NBP['NBP4_two_normal_absences'] = Model({'Lo':1,'R':0,'I':0}, {'D': eq(['R','I','Lo'], lambda w: (not w['R']) and (not w['I']) and not w['Lo']),
                                     'E': eq(['Lo','D'], lambda w: w['Lo'] or w['D'])})
NBP['NBP5_late_form'] = Model({'Lo':1,'R':0}, {'S': eq(['Lo'], lambda w: w['Lo']), 'D': eq(['R','S'], lambda w: (not w['R']) and not w['S']),
                                     'E': eq(['S','D'], lambda w: w['S'] or w['D'])})
NBP['CTRL_deviant_trigger'] = Model({'Lo':1,'H':1}, {'D': eq(['H','Lo'], lambda w: w['H'] and not w['Lo']), 'E': eq(['Lo','D'], lambda w: w['Lo'] or w['D'])})

# ---- HP + normality battery (1 = occurrence; default value 0 unless overridden)
HB = {}
HB['GP'] = (Model({'P':1,'A':1}, {'D': eq(['P','A'], lambda w: w['P'] and not w['A'])}), 'D', [('A', True)])
HB['BP'] = (Model({'P':0,'A':1}, {'D': eq(['P','A'], lambda w: w['P'] and not w['A'])}), 'D', [('A', False)])
HB['SC'] = (Model({'A':1}, {'P': eq(['A'], lambda w: w['A']), 'D': eq(['P','A'], lambda w: w['P'] and not w['A'])}), 'D', [('A', False)])
HB['EP'] = (Model({'A':1,'R':1}, {'B': eq(['R','A'], lambda w: w['R'] and not w['A']), 'D': eq(['A','B'], lambda w: w['A'] or w['B'])}), 'D', [('A', True), ('R', False)])
HB['LP'] = (Model({'ST':1,'BT':1}, {'SH': eq(['ST'], lambda w: w['ST']), 'BH': eq(['BT','SH'], lambda w: w['BT'] and not w['SH']),
             'BS': eq(['SH','BH'], lambda w: w['SH'] or w['BH'])}), 'BS', [('ST', True), ('BT', False)])
HB['NBP'] = (NBP['NBP1'], 'E', [('Lo', True), ('R', False)])
HB['SW'] = (Model({'F':1}, {'LT': eq(['F'], lambda w: not w['F']), 'RT': eq(['F'], lambda w: w['F']), 'A': eq(['LT','RT'], lambda w: w['LT'] or w['RT'])}), 'A', [('F', False)])
HB['OD'] = (Model({'C':1,'A':1}, {'E': eq(['C','A'], lambda w: w['C'] or w['A'])}), 'E', [('C', True)])
HB['OM'] = (Model({'F':0,'C':1}, {'E': eq(['F','C'], lambda w: (not w['F']) and w['C'])}), 'E', [('F', False), ('C', True)])
HB['BOULDER'] = (Model({'F':1}, {'B': eq(['F'], lambda w: w['F']), 'Dk': eq(['F'], lambda w: w['F']), 'H': eq(['B','Dk'], lambda w: w['B'] and not w['Dk'])}), 'H', [('F', False), ('Dk', True)])
HB['DP'] = (Model({'SF':1,'EN':1,'BS':1}, {'ES': eq(['EN','BS'], lambda w: w['EN'] and not w['BS']), 'BOMB': eq(['SF','ES'], lambda w: w['SF'] and not w['ES'])}), 'BOMB', [('BS', True)])
HB['CHAIN'] = (Model({'C':1}, {'D': eq(['C'], lambda w: w['C']), 'E': eq(['D'], lambda w: w['D'])}), 'E', [('C', True)])
HB['CONJ'] = (Model({'C':1,'A':1}, {'E': eq(['C','A'], lambda w: w['C'] and w['A'])}), 'E', [('C', True)])
HB['MEDP'] = (Model({'A':1,'G':0,'F':1}, {'Bt': eq(['G','F'], lambda w: w['G'] or w['F']), 'C': eq(['F'], lambda w: w['F']),
               'D': eq(['Bt','C'], lambda w: w['Bt'] and not w['C']), 'E': eq(['A','D'], lambda w: w['A'] and not w['D'])}), 'E', [('F', False), ('C', True)])
HB['EDP'] = (Model({'A':1,'F':1}, {'Bt': eq(['F'], lambda w: w['F']), 'C': eq(['F'], lambda w: w['F']),
               'D': eq(['Bt','C'], lambda w: w['Bt'] and not w['C']), 'E': eq(['A','D'], lambda w: w['A'] and not w['D'])}), 'E', [('F', False), ('C', True)])
HB['HPK'] = (Model({'A':1,'Bs':0,'C':1}, {'D': eq(['A','Bs','C'], lambda w: (w['A'] and w['Bs']) or w['C'])}), 'D', [('A', False), ('C', True)])
HB['MENTOR'] = (Model({'F':1,'Mt':1}, {'P': eq(['Mt'], lambda w: not w['Mt']), 'D': eq(['F','P'], lambda w: (not w['F']) and w['P'])}), 'D', [('F', False)])
HB['ISOMEDP'] = (Model({'A':1,'G':1,'C':1}, {'Bt': eq(['G','C'], lambda w: w['G'] and not w['C']), 'H': eq(['C'], lambda w: w['C']),
               'D': eq(['Bt','H'], lambda w: w['Bt'] or w['H']), 'E': eq(['A','D'], lambda w: w['A'] and w['D'])}), 'E', [('C', True)])
HB['DEVOM'] = (Model({'W':0,'C':1}, {'E': eq(['W','C'], lambda w: (not w['W']) and w['C'])}), 'E', [('W', True)])
HB['MENTOR_N'] = (Model({'F':1,'Mt':1}, {'P': eq(['Mt'], lambda w: not w['Mt']), 'N': eq(['F','P'], lambda w: w['F'] and w['P']),
                    'D': eq(['P','N'], lambda w: w['P'] and not w['N'])}), 'D', [('F', False), ('Mt', True)])
HB['BP_N'] = (Model({'P':0,'A':1}, {'N': eq(['A','P'], lambda w: w['A'] and w['P']), 'D': eq(['P','N'], lambda w: w['P'] and not w['N'])}), 'D', [('A', False)])
HB['GP_N'] = (Model({'P':1,'A':1}, {'N': eq(['A','P'], lambda w: w['A'] and w['P']), 'D': eq(['P','N'], lambda w: w['P'] and not w['N'])}), 'D', [('A', True)])
HB['SW_LBRB'] = (Model({'F':1,'LB':0,'RB':0}, {'A': eq(['F','LB','RB'], lambda w: (w['F'] and not w['RB']) or ((not w['F']) and not w['LB']))}), 'A', [('F', False)])
HB_DEFAULTS = {'DEVOM': {'W':1}}     # promised watering: watering is the default

CATS = ['R0','R1','E00','E01','E10','E11']   # root default/deviant; endogenous (deviant?, violates own equation?)
def cat(M, w, v, defaults):
    d = defaults.get(v, 0)
    if v not in M.eqs: return 'R0' if w[v] == d else 'R1'
    return f"E{int(w[v] != d)}{int(w[v] != M.f(v, w))}"

def precompute(M, var, eff, version, maxsize=3):
    act = M.actual; phi = lambda w: w[eff] == act[eff]
    others = [v for v in M.vars if v != var and v != eff]
    cache = {}
    def wits(X):
        if X not in cache: cache[X] = [w for (_, _, w) in hp_ac2(M, {k: act[k] for k in X}, phi, version)]
        return cache[X]
    data = []
    for r in range(0, maxsize):
        for sub in itertools.combinations(others, r):
            X = tuple(sorted((var,) + sub))
            subs = [Y for k in range(1, len(X)) for Y in itertools.combinations(X, k)]
            data.append((wits(X), [wits(Y) for Y in subs]))
    return data

def part_of_cause_under(M, data, geq, defaults):
    """HP (part of) cause with HH-style normality: witness must be >= actual, compared componentwise (HH Default Rule 2)."""
    act = M.actual; acat = {v: cat(M, act, v, defaults) for v in M.vars}
    ok = lambda w: all(geq(cat(M, w, v, defaults), acat[v]) for v in M.vars)
    for wX, wsubs in data:
        if any(ok(w) for w in wX) and not any(any(ok(w) for w in ws) for ws in wsubs):
            return True
    return False

def weak_orders(items):
    n = len(items)
    for ranks in itertools.product(range(n), repeat=n):
        if sorted(set(ranks)) == list(range(len(set(ranks)))):
            yield dict(zip(items, ranks))

SCHEMES = {'licence (E10=E00, E01>=E00, E11 low)': {'R0':1,'R1':0,'E00':1,'E01':1,'E10':1,'E11':0},
           'HH Default Rule 1 (violations atypical)': {'R0':1,'R1':0,'E00':1,'E10':1,'E01':0,'E11':0},
           'value-only': {'R0':1,'R1':0,'E00':1,'E01':1,'E10':0,'E11':0}}

def run_checks():
    dev0 = default_dev()
    print("## 1. A&G reproduction (2024a / 2024b); expected verdicts from the papers")
    for name, (M, eff, exp) in AG.items():
        got = {c: (ag_cause(M, c, eff, dev0, '2024a') is not None, ag_cause(M, c, eff, dev0, '2024b') is not None) for c in exp}
        print(f"  {name:13s} expected {exp}  got(2024a,2024b) {got}")
    print("  [2024a gets 'mentor' F wrong, as A&G 2024b fn.2 report; 2024b gets it right]")
    print("## 2. Normal-backup preemption: is Lo a cause of E?")
    nf_conf = lambda M: (lambda w: all(int((w[v]==M.f(v,w)) if v in M.eqs else (w[v]==0)) >= int((M.actual[v]==M.f(v,M.actual)) if v in M.eqs else (M.actual[v]==0)) for v in M.vars))
    for name, M in NBP.items():
        phi = lambda w, M=M: w['E'] == M.actual['E']
        row = {'AGprelim': ag_cause(M,'Lo','E',dev0,'prelim') is not None, 'AG2024a': ag_cause(M,'Lo','E',dev0,'2024a') is not None,
               'AG2024b': ag_cause(M,'Lo','E',dev0,'2024b') is not None, 'AG2024b-fwd(repair)': ag_cause(M,'Lo','E',dev0,'2024b-fwd') is not None,
               'HPmod': hp_part_of_cause(M,'Lo',phi,'mod') is not None, 'HPmod+DefaultRule': hp_part_of_cause(M,'Lo',phi,'mod',nf_conf(M)) is not None,
               'HPupd+DefaultRule': hp_part_of_cause(M,'Lo',phi,'upd',nf_conf(M)) is not None,
               'NESS': ness_cause(M,'Lo','E'), 'CNESS': cness_cause(M,'Lo','E'), 'BV': bv_cause(M,'Lo','E')}
        print(f"  {name:34s}", row)
    print("## 3. Typicality schemes x HP versions on the battery")
    versions = ['orig','upd','mod']
    queries = [(n, v, want) for n, (M, e, qs) in HB.items() for (v, want) in qs]
    pre = {(n, v, ver): precompute(HB[n][0], v, HB[n][1], ver) for (n, v, w) in queries for ver in versions}
    def wrong(o, ver, names=None):
        geq = lambda a, b: o[a] >= o[b]
        return frozenset(f"{n}:{v}" for (n, v, want) in queries if (names is None or n in names) and
                         part_of_cause_under(HB[n][0], pre[(n, v, ver)], geq, HB_DEFAULTS.get(n, {})) != want)
    for nm, sc in SCHEMES.items():
        for ver in versions: print(f"  {nm:42s} {ver}: wrong on {sorted(wrong(sc, ver))}")
    orders = [o for o in weak_orders(CATS) if o['R0'] > o['R1']]
    print(f"  weak orders on 6 categories with R0>R1: {len(orders)}")
    EXCL = {'SW:F', 'MENTOR:F'}
    for ver in versions:
        res = [(wrong(o, ver), o) for o in orders]
        good = [o for w, o in res if w <= EXCL]
        print(f"  {ver}: correct on ALL: {sum(1 for w,o in res if not w)}; correct on all but {sorted(EXCL)}: {len(good)} "
              f"(of these, SW right: {sum(1 for w,o in res if w<=EXCL and 'SW:F' not in w)}, MENTOR right: {sum(1 for w,o in res if w<=EXCL and 'MENTOR:F' not in w)})")
        forced = []
        for a, b in itertools.combinations(CATS, 2):
            s = {('>' if o[a] > o[b] else ('=' if o[a] == o[b] else '<')) for o in good}
            if a[0] == b[0] and s != {'>','=','<'}: forced.append(f"{a} {'/'.join(sorted(s))} {b}")
        print("     forced relations among survivors:", forced)
        # minimal unsatisfiable subsets of size <= 3 among the queries
        qn = [f"{n}:{v}" for (n, v, w) in queries]; wrongs = set(w for w, o in res)
        sat = lambda S: any(not (w & S) for w in wrongs)
        mus = []
        for r in (1, 2, 3):
            for S in itertools.combinations(qn, r):
                S = frozenset(S)
                if not any(m <= S for m in mus) and not sat(S): mus.append(S)
        print("     minimal unsatisfiable sets (size<=3):", [sorted(m) for m in mus])
    # switch with arrival default 1 (trains normally arrive)
    HB_DEFAULTS['SW'] = {'A':1}
    for ver in ['mod','upd']:
        res = [wrong(o, ver, names={'SW','GP','LP','NBP'}) for o in orders]
        print(f"  arrival-default-1, {ver}: schemes right on SW+GP+LP+NBP: {sum(1 for w in res if not w)}; on SW+LP+NBP: "
              f"{sum(1 for w in res if not (w - {'GP:A'}))}; on SW+GP: {sum(1 for w in res if not (w & {'SW:F','GP:A'}))}")
    del HB_DEFAULTS['SW']
    print("## 4. Modified HP + Default Rule 1: late preemption, and the frozen-violation lemma on random models")
    M = HB['LP'][0]; phi = lambda w: w['BS'] == 1
    conf = SCHEMES['HH Default Rule 1 (violations atypical)']; geq = lambda a, b: conf[a] >= conf[b]
    nfun = lambda M: (lambda w: all(geq(cat(M, w, v, {}), cat(M, M.actual, v, {})) for v in M.vars))
    print("  LP: ST part of cause via", hp_part_of_cause(M,'ST',phi,'mod',nfun(M)), "; BT part of cause via", hp_part_of_cause(M,'BT',phi,'mod',nfun(M)))
    rng = random.Random(1); viol_ok = 0; checked = 0; counter = 0
    for trial in range(300):
        nroots = rng.randint(1, 3); nendo = rng.randint(1, 3)
        roots = {f"U{i}": rng.randint(0, 1) for i in range(nroots)}
        eqs = {}; names = list(roots)
        for j in range(nendo):
            ps = tuple(rng.sample(names, min(len(names), rng.randint(1, 2))))
            table = {vals: rng.randint(0, 1) for vals in itertools.product([0,1], repeat=len(ps))}
            eqs[f"V{j}"] = (ps, (lambda t, ps: (lambda w: t[tuple(w[p] for p in ps)]))(table, ps)); names.append(f"V{j}")
        Mr = Model(roots, eqs); eff = names[-1]; actv = Mr.actual; phi = lambda w, e=eff, a=actv: w[e] == a[e]
        for c in names[:-1]:
            for (W, xp, w) in hp_ac2(Mr, {c: actv[c]}, phi, 'mod'):
                checked += 1
                butfor = Mr.solve(xp)[eff] != actv[eff]
                violation = any(w[v] != Mr.f(v, w) for v in Mr.eqs if v != c) or (c in Mr.eqs and w[c] != Mr.f(c, w))
                if (not butfor or c in Mr.eqs):
                    viol_ok += int(violation)
                    counter += 1
    print(f"  random models: {checked} modified-HP witnesses; of {counter} for non-but-for or endogenous candidates, {viol_ok} contain an equation violation (lemma predicts all)")
    print("## 5. A&G: verdict flips with the normality of an idle absence")
    for name, M, cand, idle in [('MEDP', AG['MEDP'][0], 'F', 'G'), ('NBP1', NBP['NBP1'], 'Lo', 'R')]:
        print(f"  {name}: E if {idle} had occurred = {M.solve({idle:1})['E']} (actual {M.actual['E']}); "
              f"{cand} cause? ~{idle} normal: 2024a {ag_cause(M,cand,'E',dev0,'2024a') is not None}, 2024b {ag_cause(M,cand,'E',dev0,'2024b') is not None}; "
              f"~{idle} norm-violating: 2024a {ag_cause(M,cand,'E',default_dev([idle]),'2024a') is not None}, 2024b {ag_cause(M,cand,'E',default_dev([idle]),'2024b') is not None}")
    print("  repaired A&G (deviancy only for forward candidates given F'):")
    for name, (M, eff, exp) in AG.items():
        got = {c: ag_cause(M, c, eff, dev0, '2024b-fwd') is not None for c in exp}
        bad = {c: got[c] for c in exp if got[c] != exp[c]}
        print(f"    {name:13s} disagreements with A&G's published verdicts: {bad}")


def check_s77_and_switch():
    """HH 2015 sec. 7.7-style ranking: a variable's behaviour is ranked by the dependence pattern it exhibits.
    For a NORMAL natural mechanism (drought kills unwatered crops) following the law is most typical; for a
    deviant mechanism (a backup assassin) 'stays at default regardless' is most typical (HH's own ranking)."""
    def dep_rank(M, normal_mechs):
        def typ(w, v):
            if v not in M.eqs: return 2 if w[v] == 0 else 0
            follows, atdef = (w[v] == M.f(v, w)), (w[v] == 0)
            if v in normal_mechs: return 2 if follows else (1 if atdef else 0)
            return 2 if atdef else (1 if follows else 0)
        return lambda w: all(typ(w, v) >= typ(M.actual, v) for v in M.vars)
    for name, mechs in [('NBP1', {'D','E'}), ('NBP5_late_form', {'D','E','S'}), ('CTRL_deviant_trigger', {'E'})]:
        M = NBP[name]; phi = lambda w, M=M: w['E'] == M.actual['E']
        print(f"  sec7.7 ranking, {name}: Lo part of cause?", {ver: hp_part_of_cause(M,'Lo',phi,ver,dep_rank(M, mechs)) is not None for ver in ['orig','upd','mod']})
    orders = [o for o in weak_orders(CATS) if o['R0'] > o['R1']]
    for ver in ['mod','upd']:
        pre = {(n, v): precompute(HB[n][0], v, HB[n][1], ver) for (n, v) in [('LP','ST'),('LP','BT'),('SW','F')]}
        def right(o):
            geq = lambda a, b: o[a] >= o[b]
            return (part_of_cause_under(HB['LP'][0], pre[('LP','ST')], geq, {}) is True and
                    part_of_cause_under(HB['LP'][0], pre[('LP','BT')], geq, {}) is False and
                    part_of_cause_under(HB['SW'][0], pre[('SW','F')], geq, {}) is False)
        print(f"  {ver}: schemes with Suzy cause, Billy not, switch-flip not a cause: {sum(1 for o in orders if right(o))} of {len(orders)}")

if __name__ == '__main__':
    import sys
    if '--checks' in sys.argv:
        run_checks()
        print('## 6. HH sec. 7.7 ranking on the locusts; Suzy/Billy vs switch')
        check_s77_and_switch()
    else:
        print('library loaded; run: python3 A4_models.py --checks')
