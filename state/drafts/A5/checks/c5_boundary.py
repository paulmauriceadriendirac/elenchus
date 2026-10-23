# C5. Boundary theorem (Theorem 4 in the essay) on a three-cell question {a,b,c}: independence models and checks.
# Premises:
#   EU : the rule picks, at each P, an answer G maximising P(G)T_G + (1-P(G))F_G (answer-level, extensional values)
#   TD : T_G > F_G for every G != W ;  INF: T_G > T_W for every two-cell G
#   S  : split-invariance for singletons: if {i} is chosen at P, it is chosen at every P' with P'(i)=P(i) and the
#        other two cells below P(i)
#   AS(i): {i} chosen whenever P(i) > 0.99 (any x0<1 would do; we test 0.99)
#   Cm(i): {i} never chosen when P(i) < 1/2
# Theorem: EU+TD+INF, S, AS(a), AS(b), Cm(a), Cm(b) are jointly inconsistent.
# Each model below satisfies all but one premise (checked on a grid with denominator 240, ties excluded for S).
import itertools
from fractions import Fraction as Fr

CELLS = (0, 1, 2)
ANS = [frozenset(c) for r in (1, 2, 3) for c in itertools.combinations(CELLS, r)]
WF = frozenset(CELLS)
N = 240
GRID = [(Fr(i, N), Fr(j, N), Fr(N - i - j, N)) for i in range(N + 1) for j in range(N + 1 - i)]

def eu_rule(T, F, tiebreak=None):
    def R(P):
        vals = {G: sum(P[c] for c in G) * T[G] + (1 - sum(P[c] for c in G)) * F.get(G, 0) for G in ANS}
        m = max(vals.values()); best = [G for G in ANS if vals[G] == m]
        if tiebreak: best.sort(key=lambda G: tiebreak(G, P))
        return best[0], len(best) > 1
    return R

def normality_rule(t):
    # probabilist normality rule: exclude v iff P(cells strictly more probable than v) >= t
    def R(P):
        return frozenset(v for v in CELLS if sum(P[u] for u in CELLS if P[u] > P[v]) < t), False
    return R

def check(R):
    res = {P: R(P) for P in GRID}
    out = {}
    for i in (0, 1):
        # AS
        out[f"AS({'ab'[i]})"] = all(res[P][0] == frozenset({i}) for P in GRID if P[i] > Fr(99, 100))
        # Cm
        out[f"C-({'ab'[i]})"] = all(res[P][0] != frozenset({i}) for P in GRID if P[i] < Fr(1, 2))
    # S (all cells), on tie-free points
    Sok = True
    for i in CELLS:
        slices = {}
        for P in GRID:
            if res[P][1]: continue
            if all(P[j] < P[i] for j in CELLS if j != i):
                slices.setdefault(P[i], set()).add(res[P][0] == frozenset({i}))
        if any(len(v) > 1 for v in slices.values()):
            Sok = False
    out["S"] = Sok
    return out

def vals(single, pair, w, Fsingle, Fpair, special=None):
    T = {}; F = {}
    for G in ANS:
        if len(G) == 1: T[G] = single; F[G] = Fsingle
        elif len(G) == 2: T[G] = pair; F[G] = Fpair
        else: T[G] = w
    if special: special(T, F)
    return T, F

def TD_INF(T, F):
    td = all(T[G] > F[G] for G in ANS if G != WF)
    inf = all(T[G] > T[WF] for G in ANS if len(G) == 2)
    return td, inf

models = {}
# drop S: size-only values T=(1, .6, .5), F=0
models["drop S"] = vals(Fr(1), Fr(3, 5), Fr(1, 2), 0, 0)
# drop AS: singletons never worth choosing
models["drop AS"] = vals(Fr(1, 10), Fr(1), Fr(9, 10), 0, 0)
# drop C-: size-only T=(1,.5,.4), F=0 -> believes the top cell from 0.4
models["drop C-"] = vals(Fr(1), Fr(1, 2), Fr(2, 5), 0, 0)
# drop TD (pairs constant-valued): singles T=3,F=-2; pairs T=F=1; W=.5 ; ties among pairs broken by probability
models["drop TD"] = vals(Fr(3), Fr(1), Fr(1, 2), Fr(-2), Fr(1))
# drop INF: singles T=1,F=-1; pairs T=0,F=-1; W=.2
models["drop INF"] = vals(Fr(1), Fr(0), Fr(1, 5), Fr(-1), Fr(-1))
# only one cell anti-sceptical (shows two cells are needed): from the kill test
def sp(T, F):
    a = frozenset({0})
    T[a] = Fr(1); F[a] = Fr(-1)
    for G in ANS:
        if len(G) == 1 and G != a: T[G] = Fr(1); F[G] = Fr(-10)
        if len(G) == 2 and 0 in G: T[G] = Fr(7, 10); F[G] = Fr(-10)
    T[frozenset({1, 2})] = Fr(8); F[frozenset({1, 2})] = Fr(0); T[WF] = Fr(1, 2)
models["one cell only"] = vals(0, 0, 0, 0, 0, special=sp)

tb = lambda G, P: -sum(P[c] for c in G)
for name, (T, F) in models.items():
    td, inf = TD_INF(T, F)
    print(f"{name:14s} TD={td} INF={inf}", check(eu_rule(T, F, tiebreak=tb)))
for t in (Fr(3, 5), Fr(9, 10)):
    print(f"normality t={t}  (EU fails by the theorem)", check(normality_rule(t)))

# The record measure is split-sensitive: strongest belief (cap of the optimal state) at two credences with the same C({1})
import sys
sys.path.insert(0, ".")
W3 = (0, 1, 2)
PROPS = [frozenset(c) for r in range(0, 4) for c in itertools.combinations(W3, r)]
STATES = [frozenset(p for p, b in zip(PROPS, bits) if b) for bits in itertools.product([0, 1], repeat=len(PROPS))]
def opt(C, T=Fr(1), F=Fr(2), beta=Fr(3)):
    best = None
    for B in STATES:
        X = frozenset(W3)
        for p in B: X &= p
        v = sum(sum(C[w] for w in p) * (T + F) - F for p in B) + beta * sum(C[w] for w in X)
        if best is None or v > best[0]: best = (v, [B])
        elif v == best[0]: best[1].append(B)
    caps = []
    for B in best[1]:
        X = frozenset(W3)
        for p in B: X &= p
        caps.append(sorted(w + 1 for w in X))
    return caps
for C in [(Fr(3, 4), Fr(1, 8), Fr(1, 8)), (Fr(3, 4), Fr(1, 100), Fr(6, 25))]:
    print("record measure, C =", [str(x) for x in C], "strongest belief(s):", opt(C))
