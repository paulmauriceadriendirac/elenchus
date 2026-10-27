import itertools, random, re, sys
from fractions import Fraction
ok=True
def report(name,cond):
    global ok
    print(("PASS " if cond else "FAIL ")+name)
    ok=ok and cond
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

