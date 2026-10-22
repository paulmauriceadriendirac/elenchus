# E2 v3 formal checks (v2 checks preserved in check_v2.py).
# Framework of Meehan & Zhang 2025 (MZ): finite S, regular prior pi, factive learning situations
# E: S -> subsets containing s; MZ Brier A(c,s) = -sum_{q subset S}(c(q)-v_s(q))^2 (MZ p.339).
# For a globally evidentially constant (GEC) rule f, weighted total expected accuracy
#   TEA_lam(f) = sum_E lam(E) sum_s pi(s) A(f(E(s)),s) = sum_s pi(s) sum_{p ni s} lam_p(s) A(f(p),s)  (MZ p.345)
# All arithmetic exact (fractions) unless printed as float.
import itertools, random
from fractions import Fraction as F
from math import comb
random.seed(11)
ALL_OK = []
def ok(label, cond):
    ALL_OK.append(bool(cond)); print(("  [ok] " if cond else "  [FAIL] ") + label)

def props(n):
    return [frozenset(c) for k in range(1, n+1) for c in itertools.combinations(range(n), k)]
_fact = {}
def factive(n):
    if n not in _fact:
        P = props(n)
        _fact[n] = [tuple(c) for c in itertools.product(*[[p for p in P if s in p] for s in range(n)])]
    return _fact[n]
def transparent(E):
    return all(E[t] == E[s] for s in range(len(E)) for t in E[s])
def profile(n, weighted):
    L = {}
    for E, w in weighted:
        if w == 0: continue
        for s in range(n): L[(E[s], s)] = L.get((E[s], s), 0) + w
    return L
def extensional(n, L):
    return all(len({L.get((p, s), 0) for s in p}) == 1 for p in props(n))
def allsubsets(n):
    return [frozenset(c) for k in range(0, n+1) for c in itertools.combinations(range(n), k)]
_subs = {}
def brier(c, s, n):
    if n not in _subs: _subs[n] = allsubsets(n)
    return -sum((sum(c[t] for t in q) - (1 if s in q else 0))**2 for q in _subs[n])
def cond(pi, p):
    z = sum(pi[t] for t in p); return [pi[t]/z if t in p else F(0) for t in range(len(pi))]
def lamrule(pi, L, p, n):
    m = [pi[s]*L.get((p, s), 0) for s in range(n)]; z = sum(m)
    return None if z == 0 else [x/z for x in m]
def tea(n, pi, L, f):
    return sum(pi[s]*sum(L.get((p, s), 0)*brier(f(p), s, n) for p in props(n) if s in p) for s in range(n))
def ea(n, pi, E, f):  # expected accuracy of GEC rule f in problem E
    return sum(pi[s]*brier(f(E[s]), s, n) for s in range(n))
def metacond(n, pi, E):
    return lambda s: cond(pi, [t for t in range(n) if E[t] == E[s]])
def ea_meta(n, pi, E):
    return sum(pi[s]*brier(metacond(n, pi, E)(s), s, n) for s in range(n))
def bell(m):
    Bs = [1]
    for k in range(m): Bs.append(sum(comb(k, j)*Bs[j] for j in range(k+1)))
    return Bs[m]
def randprior(n):
    w = [F(random.randint(1, 9)) for _ in range(n)]; return [x/sum(w) for x in w]
def randrule(n):
    R = {}
    for p in props(n):
        v = [F(random.randint(0, 9)) for _ in range(n)]; v[random.randrange(n)] += 1; R[p] = [x/sum(v) for x in v]
    return R
DANA = [F(1, 5), F(3, 5), F(1, 5)]
Dana = (frozenset({0, 1}), frozenset({0, 1, 2}), frozenset({1, 2}))

print("== 0. Fidelity: reproduce MZ Table 2/3 totals (Fact 9 quantity, Dana prior) ==")
n = 3; L1 = {(p, s): 1 for p in props(n) for s in p}
b = tea(n, DANA, L1, lambda p: cond(DANA, p)); d = tea(n, DANA, L1, lambda p: DANA)
one = {frozenset({0, 1}): [1, 0, 0], frozenset({0, 1, 2}): [0, 1, 0], frozenset({1, 2}): [0, 0, 1]}
o = tea(n, DANA, L1, lambda p: one.get(p, cond(DANA, p)))
ok("BCOND %.2f, dogmatic %.2f, one-shot %.2f = MZ -2.72, -4.48, -6.8" % (b, d, o),
   (b, d, o) == (F(-272, 100), F(-448, 100), F(-68, 10)))

print("== 1. Budget identity and weightings-as-learning-models (Obs. 1, Prop. 1 of v3) ==")
for n in (3, 4):
    Fa = factive(n)
    good = True; real = True
    for t in range(4):
        lam = [F(random.randint(0, 3)) for _ in Fa]; lam[0] += 1
        L = profile(n, list(zip(Fa, lam))); Lam = sum(lam)
        good &= all(sum(L.get((p, s), 0) for p in props(n) if s in p) == Lam for s in range(n))
        # any coarsening mechanism q(p|s) is the normalized profile of the product weighting prod_s q(E(s)|s)
        q = {}
        for s in range(n):
            ws = {p: F(random.randint(0, 4)) for p in props(n) if s in p}; ws[frozenset(range(n))] += 1
            z = sum(ws.values()); q.update({(p, s): w/z for p, w in ws.items()})
        Lq = profile(n, [(E, eval_prod) for E in Fa for eval_prod in [__import__('math').prod(q[(E[s], s)] for s in range(n))]])
        real &= all(Lq.get((p, s), 0) == q[(p, s)] for p in props(n) for s in p)
    ok("n=%d: sum_{p ni s} lam_p(s) = total weight at every s (random weightings)" % n, good)
    ok("n=%d: every coarsening mechanism q is realized as the profile of prod_s q(E(s)|s) (total 1)" % n, real)
# extensional <=> normalized profile is CAR (definitional); Lemma 1 rule = 'sophisticated conditioning'
n = 3; Fa = factive(n); pi = DANA
lam = [F(random.randint(0, 4)) for _ in Fa]; lam[5] += 1
L = profile(n, list(zip(Fa, lam)))
okk = True
for p in props(n):
    joint = [sum(pi[s]*lam[i] for i in range(len(Fa)) if Fa[i][s] == p) for s in range(n)]
    if sum(joint) == 0: continue
    okk &= [x/sum(joint) for x in joint] == lamrule(pi, L, p, n)
ok("representative agent: conditioning on the report event = Lemma-1 rule pi(.|lam_p)", okk)

print("== 2. Selection vs ranking equivalence ==")
# every full extensional weighting selects BCOND: e.g. opaque-only uniform, cyclic+uniform, yes/no
for n in (3, 4):
    Fa = factive(n); Lo = profile(n, [(E, 1) for E in Fa if not transparent(E)])
    pi = randprior(n)
    ok("n=%d: opaque-only uniform weighting selects BCOND on every p" % n,
       all(lamrule(pi, Lo, p, n) == cond(pi, p) for p in props(n)))

print("== 3. Prop 2 (MZ uniform total = 2^{(n-1)^2} x yes/no total) ==")
for n in (3, 4):
    Fa = factive(n); La = profile(n, [(E, 1) for E in Fa])
    yn = [E for E in Fa if transparent(E) and len(set(E)) <= 2]
    Ly = profile(n, [(E, 1) for E in yn]); k = 2**((n-1)**2)
    ok("n=%d: #factive=%d, #yes/no=%d, uniform profile = %d x yes/no profile = %d x 1_p" % (n, len(Fa), len(yn), k, k),
       len(yn) == 2**(n-1) and all(La.get((p, s), 0) == k*Ly.get((p, s), 0) == (k if s in p else 0) for p in props(n) for s in range(n)))
n = 3; Fa = factive(3); La = profile(3, [(E, 1) for E in Fa])
yn = [E for E in Fa if transparent(E) and len(set(E)) <= 2]; Ly = profile(3, [(E, 1) for E in yn])
good = True
for t in range(20):
    pi = randprior(3); R = randrule(3)
    good &= tea(3, pi, La, lambda p: R[p]) == 16*tea(3, pi, Ly, lambda p: R[p])
ok("exact TEA_all = 16 TEA_yes/no for 20 random rules and priors (n=3)", good)
for n in (3, 4, 5, 6):
    cnt = {}
    for col in itertools.product((0, 1), repeat=n):
        for c in set(col):
            blk = frozenset(i for i in range(n) if col[i] == c); cnt[blk] = cnt.get(blk, 0) + F(1, 2**n)
    ok("n=%d: random 2-colouring: block containing s is uniform over the 2^(n-1) propositions containing s" % n,
       all(cnt.get(p, 0) == F(1, 2**(n-1)) for p in props(n)))

print("== 4. Prop 3: opaque-only uniform weighting lam_o ==")
for n in (3, 4):
    Fa = factive(n); Lo = profile(n, [(E, 1) for E in Fa if not transparent(E)]); k = 2**((n-1)**2)
    ok("n=%d: lam_o extensional and lam_o_p(s) = 2^{(n-1)^2} - B_{n-|p|}" % n,
       extensional(n, Lo) and all(Lo.get((p, s), 0) == k - bell(n-len(p)) for p in props(n) for s in p))
for n in (3, 4):
    good = True
    for E in factive(n):
        if transparent(E):
            for s in range(n):
                if frozenset(set(range(n)) - {s}) in E: good &= frozenset({s}) in E
    ok("n=%d: every partition with cell S-{s} has cell {s}" % n, good)
# ranking reversal: rules f,g differing only on {s} and S-{s}; delta1/delta2 in [1, 15/14)
n = 3; pi = DANA; s0 = 0; Sm = frozenset({1, 2}); Ss = frozenset({0})
Fa = factive(3); Lo = profile(3, [(E, 1) for E in Fa if not transparent(E)])
base = {p: cond(pi, p) for p in props(3)}
# g: truthful on {s0}, slightly off on S-{s0}; f: slightly off on {s0}, BCOND on S-{s0}
def mk(cs, cm):
    R = dict(base); R[Ss] = cs; R[Sm] = cm; return R
eps = F(1, 10); cs_f = [1-eps, eps, F(0)]
d1 = pi[0]*(brier([1, 0, 0], 0, 3) - brier(cs_f, 0, 3))           # loss of f on {s0}
# choose g's response to S-{s0} as (0, 3/4+x, 1/4-x) so its loss d2 slightly below d1
def loss2(x):
    c = [F(0), F(3, 4)+x, F(1, 4)-x]
    return sum(pi[t]*(brier(base[Sm], t, 3) - brier(c, t, 3)) for t in (1, 2)), c
lo, hi = F(0), F(1, 4)
for _ in range(60):
    mid = (lo+hi)/2; v, _c = loss2(mid)
    if v < d1*F(29, 30): lo = mid
    else: hi = mid
d2, cm_g = loss2(lo)
f = mk(cs_f, base[Sm]); g = mk([F(1), F(0), F(0)], cm_g)
r = d1/d2
ok("delta1/delta2 = %.4f lies in [1, 15/14)" % float(r), 1 <= r < F(15, 14))
ok("lam_o ranks f above g", tea(3, pi, Lo, lambda p: f[p]) > tea(3, pi, Lo, lambda p: g[p]))
tr = [E for E in Fa if transparent(E)]
good = True
for t in range(200):   # random weightings on transparent problems never rank f above g
    w = [F(random.randint(0, 5)) for _ in tr]; w[random.randrange(len(tr))] += 1
    Lt = profile(3, list(zip(tr, w)))
    good &= tea(3, pi, Lt, lambda p: f[p]) <= tea(3, pi, Lt, lambda p: g[p])
for E in tr:            # and each single partition
    Lt = profile(3, [(E, 1)]); good &= tea(3, pi, Lt, lambda p: f[p]) <= tea(3, pi, Lt, lambda p: g[p])
ok("every transparent weighting tested (5 partitions + 200 random mixtures) ranks g at least as high as f", good)
# Cyclic Informants (= Gill & Grunwald 2008 Example 1, credited there to Gill, van der Laan & Robins 1997)
A = (frozenset({0, 1}), frozenset({1, 2}), frozenset({0, 2})); B = (frozenset({0, 2}), frozenset({0, 1}), frozenset({1, 2}))
Lc = profile(3, [(A, 1), (B, 1)])
ok("Cyclic Informants: both opaque, jointly extensional, normalized profile 1/2 on each pair",
   not transparent(A) and not transparent(B) and extensional(3, Lc) and all(Lc[(p, s)] == 1 for p in set(A) for s in p))

print("== 5. Prop 4 (knife-edge): extensionality survives every reweighting of the support iff support transparent ==")
for n in (3,):
    Fa = factive(n); La = profile(n, [(E, 1) for E in Fa])
    opq = [E for E in Fa if not transparent(E)]
    ok("n=3: point mass on each of the %d opaque problems is non-extensional (MZ Fact 12)" % len(opq),
       all(not extensional(n, profile(n, [(E, 1)])) for E in opq))
    good = True
    for E in opq:
        for e in (F(1, 1000), F(1, 2), F(3)):
            good &= not extensional(n, profile(n, [(X, 1) for X in Fa] + [(E, e)]))
    ok("n=3: uniform + eps on any single opaque problem is non-extensional (eps = 1/1000, 1/2, 3)", good)
    good = True
    for t in range(100):
        w = [F(random.randint(0, 6)) for _ in Fa if transparent(_)]
        trs = [E for E in Fa if transparent(E)]; w[0] += 1
        good &= extensional(n, profile(n, list(zip(trs, w))))
    ok("n=3: 100 random weightings of transparent problems are all extensional", good)
    good = True
    for e in (F(1, 100), F(1, 10)):
        Le = profile(n, [(X, 1) for X in Fa] + [(Dana, e)])
        good &= lamrule(DANA, Le, frozenset({0, 1}), n) != cond(DANA, frozenset({0, 1}))
    ok("Dana prior: uniform + eps x Dana's problem => optimal response to {15,16} differs from BCOND", good)
    Le = profile(n, [(X, 1) for X in Fa] + [(Dana, F(1, 10))])
    print("    (eps=1/10: optimal on {15,16} =", [str(x) for x in lamrule(DANA, Le, frozenset({0, 1}), n)], "vs BCOND 1/4, 3/4, 0)")
    ok("eps=1/10: optimal on {15,16} = (161/641, 480/641, 0)", lamrule(DANA, Le, frozenset({0, 1}), n) == [F(161, 641), F(480, 641), 0])
    Lk = profile(n, [(X, 1) for X in Fa] + [(Dana, 64)])
    ok("Dana weight 64 (= all other problems together): {15,16} -> (5/8,3/8,0); S -> (1/17,15/17,1/17)",
       lamrule(DANA, Lk, frozenset({0, 1}), n) == [F(5, 8), F(3, 8), 0] and lamrule(DANA, Lk, frozenset({0, 1, 2}), n) == [F(1, 17), F(15, 17), F(1, 17)])
for n in (4,):
    Fa = factive(n); La = profile(n, [(E, 1) for E in Fa]); opq = [E for E in Fa if not transparent(E)]
    sample = random.sample(opq, 60)
    ok("n=4: uniform + 1/1000 on 60 sampled opaque problems: all non-extensional",
       all(not extensional(n, {k: La.get(k, 0) + profile(n, [(E, F(1, 1000))]).get(k, 0) for k in set(La) | set(profile(n, [(E, 1)]))}) for E in sample))

print("== 6. Prop 5 (neutrality): permutation-invariant weightings are extensional ==")
def act(sig, E):  # (sigma E)(sigma s) = sigma(E(s))
    out = [None]*len(E)
    for s in range(len(E)): out[sig[s]] = frozenset(sig[t] for t in E[s])
    return tuple(out)
for n in (3, 4):
    Fa = factive(n); idx = {E: i for i, E in enumerate(Fa)}; perms = list(itertools.permutations(range(n)))
    good = True; nonneutral_ext = False
    for t in range(4 if n == 3 else 2):
        lam = [F(random.randint(0, 5)) for _ in Fa]; lam[random.randrange(len(Fa))] += 1
        sym = [sum(lam[idx[act(sig, E)]] for sig in perms) for E in Fa]   # orbit average (unnormalized)
        good &= all(sym[idx[act(sig, E)]] == sym[idx[E]] for E in Fa for sig in perms)
        good &= extensional(n, profile(n, list(zip(Fa, sym))))
    ok("n=%d: symmetrizations of random weightings are invariant and extensional" % n, good)
Fa = factive(3); idx = {E: i for i, E in enumerate(Fa)}; perms = list(itertools.permutations(range(3)))
lamC = [1 if E in (A, B) else 0 for E in Fa]
ok("Cyclic Informants weighting is itself permutation-invariant (each permutation maps {A,B} to itself)",
   all(lamC[idx[act(sig, E)]] == lamC[idx[E]] for E in Fa for sig in perms))
P1 = (frozenset({0}), frozenset({1, 2}), frozenset({1, 2}))
lamP = [1 if E == P1 else 0 for E in Fa]
ok("point mass on partition {{0},{1,2}}: extensional but not invariant (neutrality sufficient, not necessary)",
   extensional(3, profile(3, list(zip(Fa, lamP)))) and any(lamP[idx[act(sig, E)]] != lamP[idx[E]] for E in Fa for sig in perms))

print("== 7. Prop 6 (propriety): S_p(c,s) = lam_p(s) A(c,s) strictly proper on p iff lam_p positive-constant on p ==")
# For b on p: argmax_c E_b[lam A(c,.)] = b reweighted by lam (strict propriety of Brier); check numerically by search
n = 3; p = frozenset({0, 1, 2})
def best_c(b, lam):  # exact maximizer by strict propriety: b^lam
    m = [b[s]*lam[s] for s in range(3)]; z = sum(m); return [x/z for x in m]
good = True
for t in range(30):
    b = randprior(3); lam = [F(random.randint(1, 5)) for _ in range(3)]
    bc = best_c(b, lam); val = lambda c: sum(b[s]*lam[s]*brier(c, s, 3) for s in range(3))
    for u in range(20):
        c = randprior(3)
        good &= val(bc) >= val(c)
    good &= (bc == b) == (len(set(lam)) == 1)
ok("maximizer of the lam-weighted score is b^lam; equals b for all b iff lam constant (30 x 20 trials)", good)

print("== 8. Prop 7 (separable profiles; No News) ==")
# 8a for every weighting: optimal response to S is the prior iff lam_S constant
n = 3; Fa = factive(3); good = True
for t in range(60):
    lam = [F(random.randint(0, 3)) for _ in Fa]; lam[random.randrange(len(Fa))] += 1
    L = profile(3, list(zip(Fa, lam))); pi = randprior(3); S = frozenset(range(3))
    r = lamrule(pi, L, S, 3)
    if r is None: continue
    good &= (r == pi) == (len({L.get((S, s), 0) for s in range(3)}) == 1)
ok("any weighting (60 random): optimal response to S = prior iff lam_S constant", good)
# 8b product, additive, and range-sum aggregations of state-independent importance h
def H(n, h, s): return sum(h[p] for p in props(n) if s in p)
def wts(n, h, form, dom):
    out = []
    for E in factive(n):
        if dom == 'opq' and transparent(E): continue
        vals = [h[E[s]] for s in range(n)]
        if form == 'x':
            w = 1
            for v in vals: w *= v
        elif form == '+': w = sum(vals)
        else: w = sum(h[r] for r in set(E))   # sum over distinct propositions in E's range
        out.append((E, w))
    return out
def separable(n, L, kind):
    # test lam_p(s) = a(p) g(s) (kind x) or a(p)+g(s) (kind +) on s in p; return bool
    S = frozenset(range(n))
    if kind == 'x':
        g = {s: L[(S, s)] for s in range(n)}
        return all(L.get((p, s), 0)*g[t] == L.get((p, t), 0)*g[s] for p in props(n) for s in p for t in p)
    g = {s: L[(S, s)] for s in range(n)}
    return all(L.get((p, s), 0) - g[s] == L.get((p, t), 0) - g[t] for p in props(n) for s in p for t in p)
for n in (3, 4):
    agree = True; sep = True; trials = 18 if n == 3 else 6; counts = [0, 0]
    for t in range(trials):
        mode = t % 3
        if mode == 0: h = {p: F(random.randint(1, 6)) for p in props(n)}
        elif mode == 1:
            g_ = {k: F(random.randint(1, 6)) for k in range(1, n+1)}; h = {p: g_[len(p)] for p in props(n)}
        else:
            h = {}
            for p in props(n):
                if p in h: continue
                c = frozenset(set(range(n)) - p); v = F(random.randint(1, 6)); h[p] = v
                if c: h[c] = v
        Hc = len({H(n, h, s) for s in range(n)}) == 1; counts[Hc] += 1
        for form, kind in (('x', 'x'), ('+', '+'), ('r', '+')):
            for dom in ('all', 'opq'):
                if form == 'r' and dom == 'opq': continue
                L = profile(n, wts(n, h, form, dom))
                if dom == 'all': sep &= separable(n, L, kind)
                ext = extensional(n, L); nn = len({L[(frozenset(range(n)), s)] for s in range(n)}) == 1
                agree &= (ext == nn)
                if form in ('x', '+'): agree &= (ext == Hc)
    ok("n=%d: product/additive (all, opaque-only) and range-sum: extensional <=> No News; product/additive also <=> H const (%d unbalanced, %d balanced h)" % (n, counts[0], counts[1]), agree)
    ok("n=%d: product profile multiplicatively separable; additive and range-sum profiles additively separable" % n, sep)
# 8c budget identity forces multiplicatively separable profiles into product form: g(s) = Lam / A(s)
n = 3; h = {p: F(random.randint(1, 6)) for p in props(3)}; L = profile(3, wts(3, h, 'x', 'all'))
Lam = sum(w for _, w in wts(3, h, 'x', 'all'))
ok("product profile lam_p(s) = Lam h(p)/H(s)", all(L[(p, s)] == Lam*h[p]/H(3, h, s) for p in props(3) for s in p))
# 8d tilted prior for the product form
good = True
for t in range(10):
    h = {p: F(random.randint(1, 6)) for p in props(3)}; L = profile(3, wts(3, h, 'x', 'all')); pi = randprior(3)
    pt = [pi[s]/H(3, h, s) for s in range(3)]; pt = [x/sum(pt) for x in pt]
    good &= all(lamrule(pi, L, p, 3) == cond(pt, p) for p in props(3))
ok("product-form optimal rule = BCOND applied to tilted prior pi/H", good)

print("== 9. Enough Butter (Dana prior, h({16,17})=5, else 1) ==")
h = {p: F(1) for p in props(3)}; h[frozenset({1, 2})] = F(5)
Hs = [H(3, h, s) for s in range(3)]; pt = [DANA[s]/Hs[s] for s in range(3)]; pt = [x/sum(pt) for x in pt]
ok("H = (4,8,8), tilted prior = (1/3,1/2,1/6)", Hs == [4, 8, 8] and pt == [F(1, 3), F(1, 2), F(1, 6)])
ok("on {15,16}: optimal (2/5,3/5,0) vs BCOND (1/4,3/4,0)", cond(pt, frozenset({0, 1})) == [F(2, 5), F(3, 5), 0])
ea_prior = sum(DANA[s]*brier(DANA, s, 3) for s in range(3)); ea_t = sum(DANA[s]*brier(pt, s, 3) for s in range(3))
ok("Noah: prior %.4f vs tilted %.4f (=-53/45)" % (ea_prior, ea_t), ea_prior == F(-112, 100) and ea_t == F(-53, 45))
L = profile(3, wts(3, h, 'x', 'all'))
ok("product weighting ranks tilted rule above BCOND", tea(3, DANA, L, lambda p: cond(pt, p)) > tea(3, DANA, L, lambda p: cond(DANA, p)))
# refinement sensitivity: h = 1 everywhere + bump (h=5) on one proposition of size n-1 ; tilt on learning S
print("  refinement: h=1 except h=5 on {1..n-1}; ratio H(0)/H(1) and TV distance of tilted from uniform prior")
for n in (3, 4, 5, 6, 8, 10):
    H0 = 2**(n-1); H1 = 2**(n-1) + 4
    pu = [F(1, n)]*n; pt_ = [F(1, H0)] + [F(1, H1)]*(n-1); pt_ = [x/sum(pt_) for x in pt_]
    tv = sum(abs(a-b_) for a, b_ in zip(pu, pt_))/2
    print("    n=%2d  H(0)=%4d H(other)=%4d  TV(tilted, prior)=%.5f" % (n, H0, H1, float(tv)))

print("== 10. Objection: worst case, minimax regret, dominance (Dana prior, MZ Brier) ==")
n = 3; Fa = factive(3)
bc = lambda p: cond(DANA, p); dg = lambda p: DANA
wc = lambda f: sum(DANA[s]*min(brier(f(p), s, 3) for p in props(3) if s in p) for s in range(3))
ok("maximin: BCOND worst case %.3f < dogmatic %.3f" % (wc(bc), wc(dg)), wc(bc) == F(-1188, 1000) and wc(dg) == F(-112, 100))
reg = lambda f: max(ea_meta(3, DANA, E) - ea(3, DANA, E, f) for E in Fa)
rb, rd = reg(bc), reg(dg)
argb = max(Fa, key=lambda E: ea_meta(3, DANA, E) - ea(3, DANA, E, bc))
ok("minimax regret: BCOND max regret %.3f (attained in Dana's problem: %s) > dogmatic %.3f" % (rb, argb == Dana, rd),
   rb == F(1188, 1000) and rd == F(112, 100) and argb == Dana)
# best GEC rule in a problem attains META-COND's value (one-shot mimicry, MZ 327)
good = True
for E in Fa:
    mc = metacond(3, DANA, E); mim = {E[s]: mc(s) for s in range(3)}
    good &= ea(3, DANA, E, lambda p: mim.get(p, DANA)) == ea_meta(3, DANA, E)
ok("in every problem a GEC rule matches META-COND's expected accuracy (regret baseline)", good)
print("  (minimax-regret optimum not computed; it suffices that dogmatic beats BCOND)")

print("== 11. Agent-level transfer: opaque but CAR learning => META-COND = BCOND on S ==")
pi = randprior(3)
# agent uncertain 50/50 between informant A and B (Cyclic Informants), independent of state
good = True
for p in set(A):
    post = [pi[s]*(F(1, 2)*(A[s] == p) + F(1, 2)*(B[s] == p)) for s in range(3)]
    post = [x/sum(post) for x in post]; good &= post == cond(pi, p)
ok("Cyclic agent (fair coin): conditioning on 'I received p' = conditioning on p", good)
post = [pi[s]*(F(2, 3)*(A[s] == A[0]) + F(1, 3)*(B[s] == A[0])) for s in range(3)]; post = [x/sum(post) for x in post]
ok("Cyclic agent with biased coin (2/3,1/3): the two come apart", post != cond(pi, A[0]))

print("\nALL CHECKS PASSED:", all(ALL_OK), "(%d checks)" % len(ALL_OK))
