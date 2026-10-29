"""A4 v6 checks.  Run:  python3 v6_verify.py   (from this directory; imports models.py beside it)

Computes, for the binary models used in v6, every HP verdict (original, updated, modified) under
  * all 355 preorders on the four non-root categories n,l,f,u (componentwise filter), and
  * additive category scores (r,a,b,c,d): symbolic witness gains plus a random numeric sweep,
with AC3 applied after normality filtering and candidates of every size (any subset of variables).
Also: escapes (mechanism-specific penalties, inertial coding of standing blockages), the frozen-
witness lemma on random models, and Andreas-Guenther verdicts with and without the deviancy condition.
"""
import os, sys, itertools, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from models import Model, hp_ac2, subsets, ag_cause, default_dev

def eq(ps, fn): return (tuple(ps), fn)
DEFS = ['orig', 'upd', 'mod']
CATS = ['n', 'l', 'f', 'u']

# --------------------------------------------------------------------------- models
# name -> (model, outcome variable, candidate of interest, standard verdict for that candidate)
MOD = {}
MOD['GP'] = (Model({'P':1,'A':1}, {'V': eq(['P','A'], lambda w: w['P'] and not w['A'])}), 'V', 'A', True)
MOD['CHAIN'] = (Model({'C':1}, {'I': eq(['C'], lambda w: w['C']), 'Y': eq(['I'], lambda w: w['I'])}), 'Y', 'C', True)
MOD['BOULDER'] = (Model({'F':1}, {'B': eq(['F'], lambda w: w['F']), 'K': eq(['F'], lambda w: w['F']),
                                  'H': eq(['B','K'], lambda w: w['B'] and not w['K'])}), 'H', 'K', True)
MOD['SC'] = (Model({'A':1}, {'P': eq(['A'], lambda w: w['A']), 'V': eq(['P','A'], lambda w: w['P'] and not w['A'])}), 'V', 'A', False)
MOD['LP'] = (Model({'ST':1,'BT':1}, {'SH': eq(['ST'], lambda w: w['ST']), 'BH': eq(['BT','SH'], lambda w: w['BT'] and not w['SH']),
                                     'BS': eq(['SH','BH'], lambda w: w['SH'] or w['BH'])}), 'BS', 'ST', True)
MOD['EP'] = (Model({'A':1,'R':1}, {'B': eq(['R','A'], lambda w: w['R'] and not w['A']), 'D': eq(['A','B'], lambda w: w['A'] or w['B'])}), 'D', 'A', True)
MOD['LTRT'] = (Model({'F':1}, {'LT': eq(['F'], lambda w: not w['F']), 'RT': eq(['F'], lambda w: w['F']),
                               'A': eq(['LT','RT'], lambda w: w['LT'] or w['RT'])}), 'A', 'F', False)
MOD['DOOR'] = (Model({'M':1,'T':1}, {'L': eq(['M','T'], lambda w: w['M'] and not w['T']), 'R': eq(['M','T'], lambda w: w['M'] and w['T']),
                                     'E': eq(['L','R'], lambda w: w['L'] or w['R'])}), 'E', 'T', False)
MOD['LBRB'] = (Model({'F':1,'LB':0,'RB':0}, {'A': eq(['F','LB','RB'], lambda w: (w['F'] and not w['RB']) or ((not w['F']) and not w['LB']))}), 'A', 'F', False)
MOD['SV'] = (Model({'EF':1,'LB':1,'RB':1}, {'TA': eq(['EF','LB','RB'], lambda w: (w['EF'] and not w['RB']) or ((not w['EF']) and not w['LB']))}), 'TA', 'EF', False)
MOD['LOC'] = (Model({'S':1,'Q':0}, {'D': eq(['Q','S'], lambda w: (not w['Q']) and not w['S']), 'X': eq(['S','D'], lambda w: w['S'] or w['D'])}), 'X', 'S', True)
MOD['SEED'] = (Model({'P':1,'S':1}, {'G': eq(['P','S'], lambda w: w['P'] and w['S']), 'D': eq(['P','S'], lambda w: w['P'] and not w['S']),
                                     'X': eq(['G','D'], lambda w: w['G'] or w['D'])}), 'X', 'S', True)
SWITCHES = ['LTRT', 'DOOR', 'LBRB', 'SV']

def defaults_for(name, coding='event'):
    M = MOD[name][0]
    d = {v: 0 for v in M.vars}                     # event coding: occurrences deviant, absences default
    if coding == 'inertial-blockage' and name == 'SV':
        d['LB'] = 1; d['RB'] = 1                   # a standing blockage is the default state (clear tracks in LBRB stay default 0)
    return d

def cat(M, w, v, d):
    if v not in M.eqs: return 'R0' if w[v] == d[v] else 'R1'
    dev = w[v] != d[v]; conf = w[v] == M.f(v, w)
    return {(False, True): 'n', (True, True): 'l', (False, False): 'f', (True, False): 'u'}[(dev, conf)]

def profile(M, w, d):
    return collections.Counter((cat(M, M.actual, v, d), cat(M, w, v, d)) for v in M.vars
                               if cat(M, M.actual, v, d) != cat(M, w, v, d))

# --------------------------------------------------------------------------- precompute witnesses
WIT = {}
def witnesses(name, ver):
    key = (name, ver)
    if key in WIT: return WIT[key]
    M, eff, cand, _ = MOD[name]; act = M.actual
    phi = lambda w: w[eff] == act[eff]
    out = {}
    for r in range(1, len(M.vars) + 1):
        for X in itertools.combinations(M.vars, r):
            ws = hp_ac2(M, {x: act[x] for x in X}, phi, ver)
            out[X] = [w for (_, _, w) in ws]
    WIT[key] = out
    return out

def causes(name, ver, admit):
    """admit(world)->bool. Returns list of minimal candidates (AC1-AC3 after filtering)."""
    W = witnesses(name, ver)
    ok = {X: any(admit(w) for w in ws) for X, ws in W.items()}
    res = []
    for X, good in ok.items():
        if not good: continue
        if any(ok[S] for r in range(1, len(X)) for S in itertools.combinations(X, r)): continue
        res.append(X)
    return res

def verdict(name, ver, admit, var=None, singleton=False):
    var = var or MOD[name][2]
    cs = causes(name, ver, admit)
    return (var,) in cs if singleton else any(var in X for X in cs)

# --------------------------------------------------------------------------- filters
def preorders():
    pairs = [(a, b) for a in CATS for b in CATS if a != b]
    out = []
    for bits in itertools.product([0, 1], repeat=len(pairs)):
        rel = {(a, a) for a in CATS} | {p for p, x in zip(pairs, bits) if x}
        if all((a, c) in rel for (a, b) in rel for (b2, c) in rel if b == b2):
            out.append(frozenset(rel))
    return out

def comp_filter(name, rel, coding='event'):
    M = MOD[name][0]; d = defaults_for(name, coding); act = M.actual
    def geq(x, y):
        if x[0] == 'R' or y[0] == 'R': return x == y or (x, y) == ('R0', 'R1')
        return (x, y) in rel
    return lambda w: all(geq(cat(M, w, v, d), cat(M, act, v, d)) for v in M.vars)

def add_filter(name, s, coding='event', special=None):
    """s = dict r,a,b,c,d ; special: {var: {cat: score}} overrides for mechanism-specific scores."""
    M = MOD[name][0]; d = defaults_for(name, coding); act = M.actual; special = special or {}
    def score(w):
        t = 0
        for v in M.vars:
            k = cat(M, w, v, d)
            if v in special and k in special[v]: t += special[v][k]
            elif k == 'R0': t += s['r']
            elif k == 'R1': t += 0
            else: t += s[{'n':'a','l':'b','f':'c','u':'d'}[k]]
        return t
    base = score(act)
    return lambda w: score(w) >= base

def gain_vector(name, w, coding='event'):
    M = MOD[name][0]; d = defaults_for(name, coding); act = M.actual
    idx = {'R0':0, 'n':1, 'l':2, 'f':3, 'u':4}
    g = [0]*5
    for v in M.vars:
        a, b = cat(M, act, v, d), cat(M, w, v, d)
        if a in idx: g[idx[a]] -= 1
        if b in idx: g[idx[b]] += 1
    return tuple(g)    # coefficients of (r,a,b,c,d)

def main():
    P = preorders()
    print(f"# preorders on {{n,l,f,u}}: {len(P)}")
    ge = lambda rel, x, y: (x, y) in rel or x == y

    print("\n## 0. Unfiltered verdicts (candidate of interest; part of a cause)")
    for name in MOD:
        print(f"  {name:8s}", {ver: verdict(name, ver, lambda w: True) for ver in DEFS}, "standard:", MOD[name][3])

    print("\n## 1. Singleton witness worlds and their changed-category profiles (event coding)")
    for name in ['GP','CHAIN','BOULDER','SC','LP','LTRT','DOOR','LBRB','SV','LOC','SEED']:
        M, eff, cand, _ = MOD[name]; d = defaults_for(name)
        for ver in DEFS:
            ws = witnesses(name, ver)[(cand,)]
            uniq = {tuple(sorted(w.items())): w for w in ws}.values()
            print(f"  {name:8s} {ver:4s}: " + "; ".join(
                f"{ {k:v for k,v in w.items()} } prof={dict(profile(M,w,d))} gain(r,a,b,c,d)={gain_vector(name,w)}" for w in uniq) or "  none")

    print("\n## 2. Calibration (GP, CHAIN, BOULDER causes; SC not) over all 355 preorders")
    for ver in DEFS:
        good = [rel for rel in P if verdict('GP', ver, comp_filter('GP', rel)) and verdict('CHAIN', ver, comp_filter('CHAIN', rel))
                and verdict('BOULDER', ver, comp_filter('BOULDER', rel)) and not verdict('SC', ver, comp_filter('SC', rel))]
        cond = all(ge(r,'l','n') and ge(r,'n','l') and ge(r,'f','n') and not ge(r,'u','n') for r in good)
        conv = sum(1 for r in P if ge(r,'l','n') and ge(r,'n','l') and ge(r,'f','n') and not ge(r,'u','n'))
        total = sum(1 for r in good if all(((x,y) in r) or ((y,x) in r) for x in CATS for y in CATS))
        print(f"  {ver}: {len(good)} preorders calibrated ({total} total orders); all satisfy l=n, f>=n, u!>=n: {cond}; preorders satisfying the conditions: {conv}")

    print("\n## 3. Horn A (modified): LP(ST), LTRT(F), DOOR(T) agree under every preorder")
    agree_s = agree_p = 0
    for rel in P:
        vs = [verdict(n, 'mod', comp_filter(n, rel), singleton=True) for n in ('LP','LTRT','DOOR')]
        vp = [verdict(n, 'mod', comp_filter(n, rel)) for n in ('LP','LTRT','DOOR')]
        agree_s += len(set(vs)) == 1
        agree_p += (vs[0] == vp[1] == vp[2])     # Suzy singleton cause iff each switch part of a cause
    print(f"  singleton verdicts agree in {agree_s}/{len(P)}; 'ST singleton cause' == 'switch part of cause' in {agree_p}/{len(P)}")
    bad = [rel for rel in P if verdict('LP','mod',comp_filter('LP',rel)) and not verdict('LP','mod',comp_filter('LP',rel),singleton=True)]
    print(f"  preorders where ST is part of a cause only via a conjunction: {len(bad)}; BT then also part of a cause in all of them: "
          f"{all(verdict('LP','mod',comp_filter('LP',r),var='BT') for r in bad)}")

    print("\n## 4. Horn B (original/updated): GP => SV, every preorder; and l>=n <=> SV")
    for ver in ('orig','upd'):
        imp = all((not verdict('GP',ver,comp_filter('GP',rel))) or verdict('SV',ver,comp_filter('SV',rel)) for rel in P)
        iff = all(verdict('SV',ver,comp_filter('SV',rel)) == ge(rel,'l','n') for rel in P)
        print(f"  {ver}: GP cause => SV flip part of cause: {imp};  SV flip part of cause iff l>=n: {iff}")
    print("  modified: SV flip part of a cause under no filter at all:", not verdict('SV','mod',lambda w: True))

    print("\n## 5. Dilemma: preorders getting GP and LP(ST cause, BT not) right while excluding every switch")
    for ver in DEFS:
        n_ok = 0
        for rel in P:
            ok = verdict('GP',ver,comp_filter('GP',rel)) and verdict('LP',ver,comp_filter('LP',rel),singleton=True) \
                 and not verdict('LP',ver,comp_filter('LP',rel),var='BT') \
                 and not any(verdict(s,ver,comp_filter(s,rel)) for s in SWITCHES)
            n_ok += ok
        print(f"  {ver}: {n_ok}")

    print("\n## 6. Additive scores: identities and random sweep")
    gv = lambda name, ver: [gain_vector(name, w) for w in witnesses(name, ver)[(MOD[name][2],)]]
    add = lambda x, y: tuple(p + q for p, q in zip(x, y))
    gC = gv('CHAIN','mod')[0]; gB = gv('BOULDER','mod')[0]
    print("  mod: CHAIN", set(gv('CHAIN','mod')), "BOULDER", set(gv('BOULDER','mod')), "LP", set(gv('LP','mod')),
          "LTRT", set(gv('LTRT','mod')), "DOOR", set(gv('DOOR','mod')))
    print("  mod: g_LP == g_LTRT == g_DOOR == g_CHAIN + g_BOULDER:",
          set(gv('LP','mod')) == set(gv('LTRT','mod')) == set(gv('DOOR','mod')) == {add(gC, gB)})
    for ver in ('orig','upd'):
        print(f"  {ver}: GP gains {set(gv('GP',ver))}; SV gains {set(gv('SV',ver))}; LP gains {set(gv('LP',ver))}; DOOR gains {set(gv('DOOR',ver))}")
    rng = random.Random(7); counts = {ver: 0 for ver in DEFS}; trials = 3000
    viol_A = viol_B = viol_C = 0
    for _ in range(trials):
        s = dict(r=rng.randint(1,6), a=rng.randint(-6,6), b=rng.randint(-6,6), c=rng.randint(-6,6), d=rng.randint(-6,6))
        V = lambda name, ver, **k: verdict(name, ver, add_filter(name, s), **k)
        if V('LP','mod',singleton=True) and not (V('LTRT','mod') and V('DOOR','mod')): viol_A += 1
        if V('CHAIN','mod') and V('BOULDER','mod') and not V('DOOR','mod'): viol_C += 1
        for ver in ('orig','upd'):
            if V('GP',ver) and not V('SV',ver): viol_B += 1
        for ver in DEFS:
            if V('GP',ver) and V('LP',ver,singleton=True) and not V('LP',ver,var='BT') and not any(V(sw,ver) for sw in SWITCHES):
                counts[ver] += 1
    print(f"  {trials} random integer scores: violations of [mod: ST singleton => both route switches] {viol_A}; "
          f"[mod: CHAIN & BOULDER => DOOR] {viol_C}; [orig/upd: GP => SV] {viol_B}")
    print("  scores separating GP+LP from all four switches:", counts)
    s0 = dict(r=2, a=0, b=-1, c=-5, d=-3)
    print("  boundary score (2,0,-1,-5,-3):")
    for name in MOD:
        print(f"    {name:8s}", {ver: verdict(name, ver, add_filter(name, s0)) for ver in DEFS})

    print("\n## 7. Escapes")
    s = dict(r=2, a=0, b=-1, c=0, d=-3)
    for cL, cBH in [(-5, 0), (-5, -5)]:
        print(f"  mechanism-specific frozen scores (c=0 default; frozen L={cL}, frozen BH={cBH}, frozen LT={cL}), mod:",
              {'CHAIN': verdict('CHAIN','mod',add_filter('CHAIN',s)), 'BOULDER': verdict('BOULDER','mod',add_filter('BOULDER',s)),
               'DOOR': verdict('DOOR','mod',add_filter('DOOR',s,special={'L':{'f':cL}})),
               'LTRT': verdict('LTRT','mod',add_filter('LTRT',s,special={'LT':{'f':cL}})),
               'LP ST': verdict('LP','mod',add_filter('LP',s,special={'BH':{'f':cBH}})),
               'LP BT': verdict('LP','mod',add_filter('LP',s,special={'BH':{'f':cBH}}),var='BT'),
               'SEED (frozen D penalised)': verdict('SEED','mod',add_filter('SEED',s,special={'D':{'f':cL}})),
               'LOC (frozen D penalised)': verdict('LOC','mod',add_filter('LOC',s,special={'D':{'f':cL}}))})
    lic = [rel for rel in P if ge(rel,'l','n') and ge(rel,'n','l') and ge(rel,'f','n') and not ge(rel,'u','n')]
    for ver in ('orig','upd'):
        print(f"  inertial coding of standing blockages, {ver}: SV flip counted under license preorders:",
              [verdict('SV',ver,comp_filter('SV',rel,'inertial-blockage')) for rel in lic],
              "; additive gains", set(gain_vector('SV',w,'inertial-blockage') for w in witnesses('SV',ver)[('EF',)]),
              "; LBRB flip counted (event coding):", [verdict('LBRB',ver,comp_filter('LBRB',rel)) for rel in lic],
              "; GP still a cause:", [verdict('GP',ver,comp_filter('GP',rel)) for rel in lic])
    print("  fresh blockages (landslides) are event-coded: SV flip counted under license preorders (orig):",
          [verdict('SV','orig',comp_filter('SV',rel)) for rel in lic])

    print("\n## 8. Exceptionless conformity (n=l > f,u; f,u incomparable-or-equal) under modified HP")
    for conf in [frozenset({(x,x) for x in CATS} | {('n','l'),('l','n'),('n','f'),('n','u'),('l','f'),('l','u')}),
                 frozenset({(x,x) for x in CATS} | {('n','l'),('l','n'),('n','f'),('n','u'),('l','f'),('l','u'),('f','u'),('u','f')})]:
        print("   ", {name: verdict(name,'mod',comp_filter(name,conf)) for name in ['GP','CHAIN','BOULDER','SC','LP','EP','LOC','LTRT','DOOR']},
              "| CHAIN I part of cause:", verdict('CHAIN','mod',comp_filter('CHAIN',conf),var='I'),
              "| LP BT:", verdict('LP','mod',comp_filter('LP',conf),var='BT'))

    print("\n## 9. Frozen-witness lemma on random acyclic binary models (modified HP, all candidate subsets)")
    rng = random.Random(3); checked = 0; bad = 0; causes_n = 0
    for trial in range(400):
        nroots = rng.randint(1, 3); nendo = rng.randint(1, 3)
        roots = {f"U{i}": rng.randint(0, 1) for i in range(nroots)}; eqs = {}; names = list(roots)
        for j in range(nendo):
            ps = tuple(rng.sample(names, min(len(names), rng.randint(1, 2))))
            table = {vals: rng.randint(0, 1) for vals in itertools.product([0,1], repeat=len(ps))}
            eqs[f"V{j}"] = (ps, (lambda t, ps: (lambda w: t[tuple(w[p] for p in ps)]))(table, ps)); names.append(f"V{j}")
        Mr = Model(roots, eqs); eff = names[-1]; act = Mr.actual; phi = lambda w: w[eff] == act[eff]
        ok = {}
        for r in range(1, len(names)):
            for X in itertools.combinations([n for n in names if n != eff], r):
                ok[X] = hp_ac2(Mr, {x: act[x] for x in X}, phi, 'mod')
        for X, ws in ok.items():
            if not ws or any(ok[S] for k in range(1, len(X)) for S in itertools.combinations(X, k)): continue
            causes_n += 1
            for (_, xp, w) in ws:
                if any(w[v] != Mr.f(v, w) for v in Mr.eqs): continue
                checked += 1
                allroots = all(x in roots for x in X)
                butfor = Mr.solve(xp)[eff] != act[eff]
                bad += not (allroots and butfor)
    print(f"  {causes_n} modified-HP causes; {checked} conforming witnesses; counterexamples to the lemma: {bad}")

    print("\n## 10. Andreas-Guenther verdicts, with their deviancy condition and with it disabled")
    dev0 = default_dev(); devall = lambda v, val: True
    for name in ['DOOR','SEED','LOC','LTRT','EP']:
        M, eff, cand, _ = MOD[name]
        print(f"  {name:6s} {cand}:", {f"{ver}/{tag}": ag_cause(M, cand, eff, dv, ver) is not None
                                       for ver in ('2024a','2024b') for tag, dv in (('dev', dev0), ('nodev', devall))})

def supplement():
    P = preorders(); ge = lambda rel, x, y: (x, y) in rel or x == y
    print("\n## 11. Corollary with singleton verdicts (GP, ST singleton causes; BT in no cause; LTRT, DOOR, SV flips not singleton causes)")
    def ok(ver, F):
        return (verdict('GP',ver,F('GP'),singleton=True) and verdict('LP',ver,F('LP'),singleton=True)
                and not verdict('LP',ver,F('LP'),var='BT')
                and not any(verdict(sw,ver,F(sw),singleton=True) for sw in ('LTRT','DOOR','SV')))
    for ver in DEFS:
        n = sum(ok(ver, lambda nm, rel=rel: comp_filter(nm, rel)) for rel in P)
        print(f"  {ver}: preorders satisfying all: {n}")
    rng = random.Random(11); cnt = {v: 0 for v in DEFS}
    for _ in range(3000):
        sc = dict(r=rng.randint(1,6), a=rng.randint(-6,6), b=rng.randint(-6,6), c=rng.randint(-6,6), d=rng.randint(-6,6))
        for ver in DEFS: cnt[ver] += ok(ver, lambda nm: add_filter(nm, sc))
    print("  3000 random additive scores satisfying all:", cnt)
    print("  modified: SV flip part of a cause iff l>=n:", all(verdict('SV','mod',comp_filter('SV',rel)) == ge(rel,'l','n') for rel in P),
          "; minimal causes (no filter):", causes('SV','mod',lambda w: True))
    print("  modified: SV causes containing EF under GP-calibrated additive (2,0,-1,0,-3):", [X for X in causes('SV','mod',add_filter('SV',dict(r=2,a=0,b=-1,c=0,d=-3))) if 'EF' in X])
    print("  modified: LBRB minimal causes (no filter):", causes('LBRB','mod',lambda w: True))
    s = dict(r=2, a=0, b=-1, c=0, d=-3); sp = {'DOOR':{'L':{'f':-5}}, 'LTRT':{'LT':{'f':-5}}}
    print("  escape score, modified, singleton/part verdicts:")
    for nm in ['GP','CHAIN','BOULDER','SC','LP','LTRT','DOOR','SV','LBRB']:
        F = add_filter(nm, s, special=sp.get(nm))
        print(f"    {nm:8s} cand {MOD[nm][2]}: singleton {verdict(nm,'mod',F,singleton=True)} part {verdict(nm,'mod',F)}"
              + (f"; BT part {verdict(nm,'mod',F,var='BT')}" if nm=='LP' else ''))
    s0 = dict(r=2, a=0, b=-1, c=-5, d=-3)
    for ver in ('orig','upd'):
        print(f"  boundary score {ver}: LP BT part {verdict('LP',ver,add_filter('LP',s0),var='BT')}; ST singleton {verdict('LP',ver,add_filter('LP',s0),singleton=True)};"
              f" SV singleton {verdict('SV',ver,add_filter('SV',s0),singleton=True)}; LBRB singleton {verdict('LBRB',ver,add_filter('LBRB',s0),singleton=True)};"
              f" SC part {verdict('SC',ver,add_filter('SC',s0))}; BOULDER K {verdict('BOULDER',ver,add_filter('BOULDER',s0))}")
    print("  sprinkler (frozen BH scored -5), modified: minimal causes:",
          causes('LP','mod',add_filter('LP',s,special={'BH':{'f':-5}})))

if __name__ == '__main__':
    main()
    supplement()
