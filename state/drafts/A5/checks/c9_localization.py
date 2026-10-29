"""c9: Localization theorem checks (A5 v4).
Two-cell space {u,v}, p={u}. Belief states = subsets of {EMPTY, p, notp, W} (16 states).
(a) Random truth-directed measures whose increments are conservative (gain at a p-world < loss
    at the non-p-world, for every addition of a contingent proposition): verdict on p is monotone
    in c=C(p), with threshold f/(t+f) from adding p to {W}.
(b) A truth-directed but non-conservative measure that is non-monotone (Conservativeness needed).
(c) Record measure violates full refinement invariance at the flagship (see also c8 (5))."""
from fractions import Fraction as Fr
import random
E, P, N, W = 'E', 'p', 'n', 'W'
truth = {E: (0, 0), P: (1, 0), N: (0, 1), W: (1, 1)}   # truth at (u, v)
states = [frozenset(s) for s in [[a for a, b in zip([E, P, N, W], bin(m)[2:].zfill(4)) if b == '1'] for m in range(16)]]

def build(core):
    """core: values (A(.,u), A(.,v)) for S ⊆ {p,n} with W present; extend truth-directedly:
    dropping W costs 1 at both worlds, adding E costs 1 at both worlds."""
    A = {}
    for s in states:
        S = frozenset(x for x in s if x in (P, N))
        au, av = core[S]
        if W not in s: au, av = au - 1, av - 1
        if E in s: au, av = au - 1, av - 1
        A[s] = (au, av)
    return A

def truth_directed(A):
    for s in states:
        for q in [E, P, N, W]:
            if q in s: continue
            t = s | {q}
            for wi in (0, 1):
                d = A[t][wi] - A[s][wi]
                if truth[q][wi] and not d > 0: return False
                if not truth[q][wi] and not d < 0: return False
    return True

def conservative(A):
    for s in states:
        for q, (pw, nw) in [(P, (0, 1)), (N, (1, 0))]:
            if q in s: continue
            t = s | {q}
            gain = A[t][pw] - A[s][pw]; loss = A[s][nw] - A[t][nw]
            if not gain < loss: return False
    return True

def verdicts(A, grid):
    out = []
    for c in grid:
        vals = {s: c*A[s][0] + (1-c)*A[s][1] for s in states}
        m = max(vals.values()); opt = [s for s in states if vals[s] == m]
        out.append((c, all(P in s for s in opt), any(P in s for s in opt)))
    return out

grid = [Fr(i, 200) for i in range(1, 200)]
random.seed(7); tested = 0
while tested < 300:
    r = lambda: Fr(random.randint(1, 60), 10)
    t1, f1, t2, f2 = r(), r(), r(), r()
    core = {frozenset(): (Fr(0), Fr(0)), frozenset([P]): (t1, -f1), frozenset([N]): (-f2, t2)}
    x = Fr(random.randint(int(-f2*10)+1, int(t1*10)-1), 10) if int(t1*10)-1 >= int(-f2*10)+1 else Fr(0)
    y = Fr(random.randint(int(-f1*10)+1, int(t2*10)-1), 10) if int(t2*10)-1 >= int(-f1*10)+1 else Fr(0)
    core[frozenset([P, N])] = (x, y)
    A = build(core)
    if not (truth_directed(A) and conservative(A)): continue
    tested += 1
    tau = f1/(t1+f1)
    for c, req, some in verdicts(A, grid):
        if c > tau: assert req, (core, c)
        if c < tau: assert not some, (core, c)
print("(a) 300 random truth-directed conservative two-cell measures: p required iff C(p)>f/(t+f), excluded below; OK")

core = {frozenset(): (Fr(0), Fr(0)), frozenset([P]): (Fr(1), Fr(-2)), frozenset([N]): (Fr(-2), Fr(1)),
        frozenset([P, N]): (Fr(-1, 2), Fr(4, 5))}
A = build(core)
print("(b) truth-directed:", truth_directed(A), " conservative:", conservative(A))
v = verdicts(A, [Fr(30,100), Fr(64,100), Fr(70,100)])
print("    p in every optimum at c=0.30,0.64,0.70:", [r[1] for r in v], "(non-monotone)")
