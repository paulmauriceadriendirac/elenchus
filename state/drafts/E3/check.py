"""Formal checks for E3 v3 ("Flattening and Counterfactual Independence").
(v2's checks are preserved in check_v2.py.)

Frames follow Dorr & Mandelkern (2026), Def. 2.1-2.3: each world w has an
accessible set R(w) containing w, well-ordered by <_w with w first.  A
conditional X > Y is true at w iff no X-world is in R(w), or the <_w-first
X-world in R(w) is a Y-world.  Selection f(w, X) = that first world, or None
(the 'vacuous' outcome) if R(w) contains no X-world; f(None, X) = None.

Checks (essay label in brackets):
 K1  (Flat) <=> D&M flatness (Def. 4.1), all order frames on 3 and 4 worlds.   [Sec. 2]
 K2  Flattening valid on a frame <=> (Flat), 3 worlds, all valuations.          [Sec. 2]
 K3  Theorem 1 valid on semi-flat (Cautious Importation, D&M Lemma 4.2) and
     on D&M fn. 24 (Cautious Exportation) frames up to 5 worlds (z3); fails
     on plain order frames.                                                      [Thm 1]
 K5  Case models (scenario-relative orderings): Reunion makes (1) true and
     (2) false; Avoidance makes both false; Buttons (symmetric, both
     tie-breaks): N1, N2 true, (D) false; Avoidance (D) true; asymmetric
     Buttons: bare instance fails.                                               [Secs 3-4]
 K6  Imaging iteration-invariant for every Pr <=> (Flat), 3-world frames.       [Remark, Sec. 6]
 K7  Quotations used in v3 occur verbatim in the source text.
 K8  Agreement on flat frames (z3, n<=5).                                       [Sec. 6]
 K9  Observation 1 (conservativity): for every order frame on 3 worlds (and a
     random sample on 4) and every world w, the linearization of <_w is a flat
     frame giving w the same order, so first-degree sentences keep their
     truth values at w; probabilistic version via disjoint union of
     linearizations.                                                             [Obs. 1]
 K10 Cross-case table: Reunion and Avoidance agree on every first-degree
     conditional about A, B at the actual world; in flat versions of both
     models (2)'s value fixes (1)'s under every construal X of the inner
     antecedent that entails A v B; only the scenario-relative reading of (1)
     with a selectional outer antecedent yields the contrast; exclusive,
     additive ('both') and universal readings yield none.                         [Sec. 3]
 K11 The Reunion frame (universal accessibility) validates Crashing Cautious
     Importation and Crashing Cautious Exportation but not Flattening, so
     C2 + both Crashing principles does not prove Flattening.                    [Obs. 3]
 K12 Structural-equation check: intervening to realize Bob's coming and then
     on Ann's coming leaves Bob's coming fixed; intervening on Ann's coming
     at the actual world leaves Bob home.                                        [Sec. 5.2]
Run:  python3 check.py
"""
import itertools, random, re, sys
from fractions import Fraction
from z3 import Solver, Bool, Int, And, Or, Not, Implies, If, sat, unsat, BoolVal

ok = True
def report(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and cond

# ---------------------------------------------------------------- explicit frames
def all_frames(n):
    """All order frames on worlds 0..n-1: frame[w] = tuple listing R(w) in <_w order, w first."""
    per_world = []
    for w in range(n):
        others = [x for x in range(n) if x != w]
        opts = []
        for k in range(len(others) + 1):
            for sub in itertools.combinations(others, k):
                for perm in itertools.permutations(sub):
                    opts.append((w,) + perm)
        per_world.append(opts)
    return itertools.product(*per_world)

def sel(frame, w, X):
    if w is None:
        return None
    for x in frame[w]:
        if x in X:
            return x
    return None

def flat_selection(frame, n):
    subsets = [frozenset(s) for k in range(1, n + 1) for s in itertools.combinations(range(n), k)]
    for Y in subsets:
        for X in subsets:
            if X <= Y:
                for w in range(n):
                    if sel(frame, sel(frame, w, Y), X) != sel(frame, w, X):
                        return False
    return True

def dm_flat(frame, n):
    R = [set(frame[w]) for w in range(n)]
    pos = [{x: i for i, x in enumerate(frame[w])} for w in range(n)]
    lt = lambda w, x, y: x in pos[w] and y in pos[w] and pos[w][x] < pos[w][y]
    for w in range(n):  # transitivity of accessibility
        for x in R[w]:
            if not R[x] <= R[w]:
                return False
    for w in range(n):  # semi-flatness
        for x in range(n):
            for y in range(n):
                if lt(w, x, y):
                    if y not in R[x]:
                        return False
                    for z in range(n):
                        if (lt(w, y, z) or (z in R[x] and z not in R[w])) and not lt(x, y, z):
                            return False
    return True

for n in (3, 4):
    agree, count, nflat = True, 0, 0
    for fr in all_frames(n):
        count += 1
        a, b = flat_selection(fr, n), dm_flat(fr, n)
        nflat += a
        if a != b:
            agree = False
            break
    report(f"K1 (Flat) <=> D&M-flat on all {count} order frames with {n} worlds ({nflat} flat)", agree)

# K2: Flattening valid <=> (Flat), by brute force over valuations, n = 3
def cond_true(frame, w, X, Y):
    s = sel(frame, w, X)
    return s is None or s in Y

def flattening_valid(frame, n):
    W = range(n)
    for vp in itertools.product([0, 1], repeat=n):
        P = {i for i in W if vp[i]}
        for vq in itertools.product([0, 1], repeat=n):
            PQ = {i for i in W if vp[i] and vq[i]}
            for vr in itertools.product([0, 1], repeat=n):
                Rr = {i for i in W if vr[i]}
                inner = {u for u in W if cond_true(frame, u, PQ, Rr)}
                for w in W:
                    if cond_true(frame, w, P, inner) != cond_true(frame, w, PQ, Rr):
                        return False
    return True

agree = all(flattening_valid(fr, 3) == flat_selection(fr, 3) for fr in all_frames(3))
report("K2 Flattening valid <=> (Flat) on all 3-world order frames (all valuations)", agree)

# ---------------------------------------------------------------- z3 encoding
class Z3Frame:
    def __init__(self, n, tag):
        self.n = n
        W = range(n)
        self.acc = [[BoolVal(True) if w == x else Bool(f"{tag}acc{w}_{x}") for x in W] for w in W]
        self.rk = [[Int(f"{tag}rk{w}_{x}") for x in W] for w in W]
        c = []
        for w in W:
            c.append(self.rk[w][w] == 0)
            for x in W:
                c.append(And(self.rk[w][x] >= 0, self.rk[w][x] < n))
                if x != w:
                    c.append(self.rk[w][x] >= 1)
                for y in W:
                    if x < y:
                        c.append(Implies(And(self.acc[w][x], self.acc[w][y]), self.rk[w][x] != self.rk[w][y]))
        self.base = c
    def lt(self, w, x, y):
        return And(self.acc[w][x], self.acc[w][y], self.rk[w][x] < self.rk[w][y])
    def cond(self, Xs, Ys):
        """Per-world truth of X > Y, given per-world truth lists Xs, Ys."""
        n, out = self.n, []
        for w in range(n):
            none = And([Not(And(self.acc[w][x], Xs[x])) for x in range(n)])
            some = Or([And(self.acc[w][y], Xs[y], Ys[y],
                           And([Implies(And(self.acc[w][x], Xs[x]), self.rk[w][y] <= self.rk[w][x]) for x in range(n)]))
                       for y in range(n)])
            out.append(Or(none, some))
        return out
    def transitive(self):
        W = range(self.n)
        return [Implies(And(self.acc[w][x], self.acc[x][y]), self.acc[w][y]) for w in W for x in W for y in W]
    def semiflat(self):
        W, c = range(self.n), []
        for w in W:
            for x in W:
                for y in W:
                    body = [self.acc[x][y]]
                    for z in W:
                        body.append(Implies(Or(self.lt(w, y, z), And(self.acc[x][z], Not(self.acc[w][z]))), self.lt(x, y, z)))
                    c.append(Implies(self.lt(w, x, y), And(body)))
        return c
    def ce_condition(self):  # D&M fn. 24: Cautious Exportation
        W, c = range(self.n), self.transitive()
        for w in W:
            for x in W:
                for y in W:
                    for z in W:
                        c.append(Implies(And(self.lt(w, x, y), self.lt(w, y, z), self.acc[x][z]), self.lt(x, y, z)))
        return c

def lnot(L): return [Not(a) for a in L]
def land(*Ls): return [And(t) for t in zip(*Ls)]
def lor(*Ls): return [Or(t) for t in zip(*Ls)]
def possible(F, Xs):  # Poss X := not (X > not X)
    return lnot(F.cond(Xs, lnot(Xs)))

def theorem1_counterexample(n, frame_cond, general_X):
    F = Z3Frame(n, f"t{n}{frame_cond}{general_X}_")
    A = [Bool(f"A{n}_{i}") for i in range(n)]
    B = [Bool(f"B{n}_{i}") for i in range(n)]
    s = Solver(); s.add(F.base)
    if frame_cond == "semiflat": s.add(F.semiflat())
    if frame_cond == "ce": s.add(F.ce_condition())
    if general_X:
        X = [Bool(f"X{n}_{i}") for i in range(n)]
        s.add([Implies(Or(A[i], B[i]), X[i]) for i in range(n)])
        s.add(F.cond(X, lor(A, B))[0])
    else:
        X = lor(A, B)
    N1 = lnot(F.cond(A, B)); N2 = lnot(F.cond(B, A))
    inner = lor(land(A, F.cond(B, lnot(A))), land(B, F.cond(A, lnot(B))))
    D = F.cond(X, inner)
    s.add(N1[0], N2[0], Not(D[0]))
    return s.check()

for cond_name in ("semiflat", "ce"):
    for gx in (False, True):
        res = [theorem1_counterexample(n, cond_name, gx) for n in (2, 3, 4, 5)]
        report(f"K3 Theorem 1 ({'X-general' if gx else 'X = A or B'}) valid on {cond_name} frames, n=2..5: {res}",
               all(r == unsat for r in res))
res = [theorem1_counterexample(n, "none", False) for n in (3, 4)]
report(f"K3 Theorem 1 fails on some plain order frame (n=3,4): {res}", sat in res)

# ---------------------------------------------------------------- K5 explicit case models
# Worlds are valuations (a, b) for 'Ann came', 'Bob came'; universal accessibility.
WORLDS = [(0, 0), (0, 1), (1, 0), (1, 1)]
def model_from_costs(cost):
    """frame[w] lists all worlds, w first, then by cost(w, v), ties broken by index."""
    return {w: tuple([w] + sorted([v for v in WORLDS if v != w], key=lambda v: (cost(w, v), WORLDS.index(v))))
            for w in WORLDS}

def ev(frame, w, phi):
    op = phi[0]
    if op == 'A': return w[0] == 1
    if op == 'B': return w[1] == 1
    if op == 'not': return not ev(frame, w, phi[1])
    if op == 'and': return ev(frame, w, phi[1]) and ev(frame, w, phi[2])
    if op == 'or': return ev(frame, w, phi[1]) or ev(frame, w, phi[2])
    if op == '>':
        for v in frame[w]:
            if ev(frame, v, phi[1]):
                return ev(frame, v, phi[2])
        return True
A_, B_ = ('A',), ('B',)
NOT = lambda p: ('not', p); AND = lambda p, q: ('and', p, q); OR = lambda p, q: ('or', p, q)
IF = lambda p, q: ('>', p, q)
AorB = OR(A_, B_)
D = IF(AorB, OR(AND(A_, IF(B_, NOT(A_))), AND(B_, IF(A_, NOT(B_)))))
claims = {
    'N1 not(A>B)': NOT(IF(A_, B_)), 'N2 not(B>A)': NOT(IF(B_, A_)),
    'N  A>notB': IF(A_, NOT(B_)), 'P2 (AvB)>(B & notA)': IF(AorB, AND(B_, NOT(A_))),
    '(1) (AvB)>(A>B)': IF(AorB, IF(A_, B_)), '(2) A>B': IF(A_, B_), 'D': D,
}
def verdicts(frame, actual=(0, 0)):
    return {k: ev(frame, actual, f) for k, f in claims.items()}

# Reunion: departures cost 2 for Ann's coming/not, 1 for Bob's (Ann's trip far less accessible).
reunion = model_from_costs(lambda w, v: 2 * abs(w[0] - v[0]) + abs(w[1] - v[1]))
rv = verdicts(reunion)
print("     Reunion verdicts at actual world:", rv)
report("K5 Reunion: N1, N2, N, P2 true; (1) true, (2) false (bare instance fails); D false",
       rv['N1 not(A>B)'] and rv['N2 not(B>A)'] and rv['N  A>notB'] and rv['P2 (AvB)>(B & notA)']
       and rv['(1) (AvB)>(A>B)'] and not rv['(2) A>B'] and not rv['D'])
report("K5 Reunion model is not flat (as it must not be)", not flat_selection(
    {WORLDS.index(w): tuple(WORLDS.index(v) for v in reunion[w]) for w in WORLDS}, 4))

# Avoidance control: Bob would stay away if Ann came. From a Bob-only world the
# nearest Ann-world is Ann-only (Bob avoids her).  Base costs as in Reunion, but
# worlds where both come are maximally remote (Bob never comes when Ann does).
avoid = model_from_costs(lambda w, v: (10 if v == (1, 1) else 0) + 2 * abs(w[0] - v[0]) + abs(w[1] - v[1]))
av = verdicts(avoid)
print("     Avoidance verdicts at actual world:", av)
report("K5 Avoidance: N1, N2, P2 true; (1) false, (2) false (instance holds); D true",
       av['N1 not(A>B)'] and av['N2 not(B>A)'] and av['P2 (AvB)>(B & notA)']
       and not av['(1) (AvB)>(A>B)'] and not av['(2) A>B'] and av['D'])

# Buttons: symmetric costs; the tie between the two single-press worlds broken either way.
for first in ((0, 1), (1, 0)):
    def cost(w, v, first=first):
        c = abs(w[0] - v[0]) + abs(w[1] - v[1])
        return (c, 0 if v == first else 1)
    bv = verdicts(model_from_costs(cost))
    report(f"K5 Buttons (tie broken toward {first}): N1, N2 true, D false",
           bv['N1 not(A>B)'] and bv['N2 not(B>A)'] and not bv['D'])

# Asymmetric Buttons: Ann nearly pressed (departure cost 1), Bob's refusal was firm (cost 2).
# Bare instance with roles of A, B swapped: (AvB)>(B>A) vs B>A.
asym = model_from_costs(lambda w, v: abs(w[0] - v[0]) + 2 * abs(w[1] - v[1]))
lhs = ev(asym, (0, 0), IF(AorB, IF(B_, A_))); rhs = ev(asym, (0, 0), IF(B_, A_))
report(f"K5 asymmetric Buttons: (AvB)>(B>A) = {lhs}, B>A = {rhs} (instance fails)", lhs and not rhs)

# ---------------------------------------------------------------- K6 imaging
def image(frame, n, pr, X):
    out = {}
    for w, p in pr.items():
        u = sel(frame, w, X) if w is not None else None
        out[u] = out.get(u, 0) + p
    return out

def cumulative(frame, n, trials=3):
    subsets = [frozenset(s) for k in range(1, n + 1) for s in itertools.combinations(range(n), k)]
    rng = random.Random(0)
    prs = [{w: Fraction(1 if w == v else 0) for w in range(n)} for v in range(n)]
    for _ in range(trials):
        ws = [Fraction(rng.randint(1, 9)) for _ in range(n)]
        prs.append({w: ws[w] / sum(ws) for w in range(n)})
    for pr in prs:
        for Y in subsets:
            for X in subsets:
                if X <= Y:
                    lhs = {k: v for k, v in image(frame, n, image(frame, n, pr, Y), X).items() if v}
                    rhs = {k: v for k, v in image(frame, n, pr, X).items() if v}
                    if lhs != rhs:
                        return False
    return True

agree = all(cumulative(fr, 3) == flat_selection(fr, 3) for fr in all_frames(3))
report("K6 imaging iteration-invariant (point masses + random Pr, exact) <=> (Flat), all 3-world frames", agree)

# ---------------------------------------------------------------- K7 quotations
src = open("/home/user/elenchus/inbox/sources/dorr-mandelkern-2026-sequence.txt", encoding="utf-8").read()
norm = src.replace("ﬀ", "ff").replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬃ", "ffi")
norm = re.sub(r"\n\d+\n=== PDF page \d+ ===\n", "\n", norm)   # drop page footer + marker
norm = re.sub(r"-\n", "", norm)          # hyphenation at line ends
norm = re.sub(r"\s+", " ", norm)
norm_joined = re.sub(r"(\w) (ff|fi|fl|ffi)", r"\1\2", norm)   # 'di ff erent' ligature artefacts
QUOTES = [
    "We have checked many instances of Flattening, in both the indicative and subjunctive mood, and have not found clear counterexamples.",
    "But matters are different for Flattening, which appears valid for both indicatives and subjunctives.",
    "we leave it as an open problem for proponents of C2.F",
    "strong prima facie appeal as (at least part of) the logic of the natural language conditional",
    "except by doggedly holding in mind the Lewisian interpretation",
    "the first antecedent feels like it’s doing nothing",
    "we might naturally regard Flattening as a plausible cautious cousin of the implausible, incautious Import-Export principle",
    "single master order",
    "If he had gotten an espresso, then he would have had a fit if he’d gotten an overextracted one.",
]
for q in QUOTES:
    qn = re.sub(r"\s+", " ", q)
    report(f"K7 verbatim: '{q[:60]}...'", qn in norm or qn in norm_joined)

# ---------------------------------------------------------------- K8 agreement
def agreement_violation(n):
    F = Z3Frame(n, f"ag{n}_")
    s = Solver(); s.add(F.base); s.add(F.semiflat()); s.add(F.transitive())
    viol = []
    for w1 in range(n):
        for w2 in range(n):
            for v in range(n):
                for y in range(n):
                    for z in range(n):
                        if len({y, z}) == 2:
                            after = And(Or(v == w1, F.lt(w1, v, y)), Or(v == w1, F.lt(w1, v, z)),
                                        Or(v == w2, F.lt(w2, v, y)), Or(v == w2, F.lt(w2, v, z)),
                                        F.acc[w1][v], F.acc[w2][v], y != v, z != v)
                            viol.append(And(after, F.lt(w1, y, z), F.lt(w2, z, y)))
    s.add(Or(viol))
    return s.check()
res = [agreement_violation(n) for n in (3, 4, 5)]
report(f"K8 Agreement holds on all flat frames n=3..5: {res}", all(r == unsat for r in res))


# ---------------------------------------------------------------- K9 conservativity (Observation 1)
def linearize(frame, n, w):
    """Linear frame whose master order is: worlds outside R(w) (any order), then <_w."""
    master = [x for x in range(n) if x not in frame[w]] + list(frame[w])
    return tuple(tuple(master[master.index(x):]) for x in range(n))

def k9_frame_ok(fr, n):
    for w in range(n):
        L = linearize(fr, n, w)
        if L[w] != fr[w] or not dm_flat(L, n):
            return False
    return True

ok9 = all(k9_frame_ok(fr, 3) for fr in all_frames(3))
rng9 = random.Random(1)
frames4 = list(all_frames(4))
ok9b = all(k9_frame_ok(fr, 4) for fr in rng9.sample(frames4, 3000))
report("K9 linearization of <_w is flat and preserves <_w: all 3-world frames, 3000 random 4-world frames", ok9 and ok9b)

def disjoint_union_of_linearizations(fr, n):
    """Worlds (c, x): copy c of the linearization at c; order of (c, x) = master_c from x on."""
    idx, frames = {}, []
    masters = {c: [x for x in range(n) if x not in fr[c]] + list(fr[c]) for c in range(n)}
    for c in range(n):
        for x in masters[c]:
            idx[(c, x)] = len(idx)
    U = [None] * len(idx)
    for c in range(n):
        m = masters[c]
        for i, x in enumerate(m):
            U[idx[(c, x)]] = tuple(idx[(c, y)] for y in m[i:])
    return tuple(U), idx

def k9_prob_ok(fr, n):
    U, idx = disjoint_union_of_linearizations(fr, n)
    N = len(U)
    if not dm_flat(U, N):
        return False
    orig = {v: k[1] for k, v in idx.items()}           # each new world copies an old world's valuation
    subsets = [frozenset(s) for k in range(0, n + 1) for s in itertools.combinations(range(n), k)]
    for X in subsets:
        for Y in subsets:
            Xl = {u for u in range(N) if orig[u] in X}; Yl = {u for u in range(N) if orig[u] in Y}
            for w in range(n):
                if cond_true(fr, w, X, Y) != cond_true(U, idx[(w, w)], Xl, Yl):
                    return False
    return True   # pointwise agreement at head copies => equal probabilities for Pr placed on heads

ok9p = all(k9_prob_ok(fr, 3) for fr in rng9.sample(list(all_frames(3)), 60)) and \
       all(k9_prob_ok(fr, 4) for fr in rng9.sample(frames4, 40))
report("K9 disjoint union of linearizations is flat and agrees on every first-degree X>Y at head copies", ok9p)

# ---------------------------------------------------------------- K10 cross-case table (Section 3)
def cells(pred): return [c for c in WORLDS if pred(c)]
AB_cells = cells(lambda c: c[0] or c[1])
def first_degree_profile(frame):
    sub = [frozenset(s) for k in range(1, 5) for s in itertools.combinations(WORLDS, k)]
    out = {}
    for X in sub:
        for Y in sub:
            v = next(u for u in frame[(0, 0)] if u in X)
            out[(X, Y)] = v in Y
    return out
report("K10 Reunion and Avoidance agree on every first-degree conditional about A, B at actuality",
       first_degree_profile(reunion) == first_degree_profile(avoid))

def flat_version(frame):
    master = list(frame[(0, 0)])
    return {x: tuple(master[master.index(x):]) for x in WORLDS}
def nested_val(frame, X, r=lambda c: c[1] == 1):
    """(A v B) > (X > r) at actuality, X a set of cells."""
    v = next(u for u in frame[(0, 0)] if u in AB_cells)
    s = next((u for u in frame[v] if u in X), None)
    return True if s is None else r(s)
def unnested_val(frame, X, r=lambda c: c[1] == 1):
    s = next((u for u in frame[(0, 0)] if u in X), None)
    return True if s is None else r(s)
okf = True
for k in range(1, len(AB_cells) + 1):
    for X in itertools.combinations(AB_cells, k):
        X = set(X)
        vals = {nested_val(flat_version(m), X) for m in (reunion, avoid)} | {unnested_val(m, X) for m in (reunion, avoid)}
        okf = okf and len(vals) == 1
report("K10 flat versions: for every construal X of the inner antecedent entailing A v B, (AvB)>(X>B) = X>B, same in both cases", okf)

inclusive = [nested_val(m, set(cells(lambda c: c[0] == 1))) for m in (reunion, avoid)]
exclusive = [nested_val(m, {(1, 0)}) for m in (reunion, avoid)]
additive  = [nested_val(m, {(1, 1)}) for m in (reunion, avoid)]
def universal(m):  # 'at least one' read as: for each disjunct, if it had held, then (A > B)
    return all(ev(m, (0, 0), IF(d, IF(A_, B_))) for d in (A_, B_))
univ = [universal(m) for m in (reunion, avoid)]
print(f"     (1) in [Reunion, Avoidance]: inclusive {inclusive}, exclusive {exclusive}, additive {additive}, universal {univ}")
report("K10 only the inclusive selectional reading yields the contrast (True, False); the others yield none",
       inclusive == [True, False] and len(set(exclusive)) == 1 and len(set(additive)) == 1 and len(set(univ)) == 1)

# ---------------------------------------------------------------- K11 crashing halves (Observation 3)
RF = {WORLDS.index(w): tuple(WORLDS.index(v) for v in reunion[w]) for w in WORLDS}
def crashing_ok(frame, n):
    W = range(n)
    for vp in itertools.product([0, 1], repeat=n):
        P = {i for i in W if vp[i]}
        for vq in itertools.product([0, 1], repeat=n):
            PQ = {i for i in W if vp[i] and vq[i]}
            notposs = {u for u in W if sel(frame, u, PQ) is None}
            for w in W:
                lhs = cond_true(frame, w, P, notposs)
                if lhs and w not in notposs:          # Crashing Cautious Importation
                    return False
                if w in notposs and not lhs:          # Crashing Cautious Exportation
                    return False
    return True
report("K11 Reunion frame validates both Crashing principles but not Flattening",
       crashing_ok(RF, 4) and not flattening_valid(RF, 4))

# ---------------------------------------------------------------- K12 structural equations (Section 5.2)
def solve(do):
    v = {'sitter': 0, 'trip': 0}; v.update({k: x for k, x in do.items() if k in v})
    v['B'] = do.get('B', v['sitter']); v['A'] = do.get('A', v['trip'])
    return v
def nested(do1, do2):
    v1 = solve(do1)
    exo = {k: v1[k] for k in ('sitter', 'trip')}
    return solve({**exo, **{k: x for k, x in do1.items() if k in ('A', 'B')}, **do2})
report("K12 do(A=1) at actuality leaves B=0; do(sitter=1) then do(A=1) leaves B=1",
       solve({'A': 1})['B'] == 0 and nested({'sitter': 1}, {'A': 1})['B'] == 1)

print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
sys.exit(0 if ok else 1)
