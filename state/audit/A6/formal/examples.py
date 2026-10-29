#!/usr/bin/env python3
"""Independent audit of the worked finite examples and counts in A6 v4.
Self-contained; exact rational arithmetic for every example.
 (1) 4: three-state model where Preservation holds but relative defeat occurs.
 (2) 5.2: three-state numerical illustration of Theorem 3 (1.2, 0.5, 0.7).
 (3) 5.2: five-state VER counterexample (0.028, 0.008, conditional ken).
 (4) 5.2: four-state example without relative defeat (KDT 0.05; VER, CEU < 0).
 (5) 6.1: K-normality empty question positive at an abnormal situation;
          I-normality KK failure in a statist comparable model.
 (6) Count reconciliation: pairs with non-trivial partitions only.
 (7) Independent random search: VER disvaluing questions, E = whole S, n<=4.
"""
import itertools, random
from fractions import Fraction as Fr

def B(gg, F):
    return frozenset(s for s in F if not any(gg[u][s] for u in F))
def K(geq, gg, F, x):
    return B(gg, F) | frozenset(v for v in F if geq[v][x])
def condK(geq, gg, E, D, x):
    ED = E & D
    return B(gg, ED) | frozenset(v for v in ED if geq[v][x])
def ev(P, u, F):
    return sum(P[s] * u[s] for s in F) / sum(P[s] for s in F)
def choose(P, acts, F):
    vals = [ev(P, a, F) for a in acts]
    return max(range(len(acts)), key=lambda i: (vals[i], -i))
def cell(Pi, s):
    return next(frozenset(c) for c in Pi if s in c)
def analyse(geq, gg, P, acts, E, x, Pi):
    Kx = K(geq, gg, E, x)
    pol = {s: choose(P, acts, K(geq, gg, E & cell(Pi, s), s)) for s in E}
    ul = {s: acts[pol[s]][s] for s in E}
    now = choose(P, acts, Kx)
    a = acts[now]
    kdt = ev(P, ul, Kx) - ev(P, a, Kx)
    D = frozenset(s for s in E if ul[s] != a[s])
    ceu = ev(P, {s: ul[s] - a[s] for s in E}, condK(geq, gg, E, D, x)) if D else 0
    tot = sum(P[s] for s in Kx); ver = 0; condkens = {}
    for b in sorted(set(pol.values())):
        Db = frozenset(s for s in E if pol[s] == b)
        w = sum(P[s] for s in Db & Kx) / tot
        Kb = condK(geq, gg, E, Db, x); condkens[b] = Kb
        if w:
            ver += w * ev(P, {s: acts[b][s] - a[s] for s in E}, Kb)
    ans = 0
    for c in Pi:
        w = sum(P[s] for s in Kx & frozenset(c)) / tot
        if w:
            ans += w * ev(P, {s: ul[s] - a[s] for s in E}, condK(geq, gg, E, frozenset(c), x))
    rd = any(not K(geq, gg, E & cell(Pi, s), s) <= Kx for s in Kx)
    return dict(K=Kx, now=now, pol=pol, kdt=kdt, ceu=ceu, ver=ver, ans=ans, condkens=condkens, rd=rd,
                evnow=[ev(P, b, Kx) for b in acts], ul=ul)

def from_ranks(ranks, gap):
    n = len(ranks)
    geq = [[ranks[u] <= ranks[v] for v in range(n)] for u in range(n)]
    gg = [[ranks[v] - ranks[u] > gap for v in range(n)] for u in range(n)]
    return geq, gg

out = []
pr = lambda *a: out.append(" ".join(str(x) for x in a))
f = lambda q: f"{float(q):.4f}"

# (1) a,b,c decreasing normality; a>>b, a>>c, not b>>c
geq = [[True, True, True], [False, True, True], [False, False, True]]
gg = [[False, True, True], [False, False, False], [False, False, False]]
S = range(3)
pres = True
subs = [frozenset(c) for r in range(1, 4) for c in itertools.combinations(S, r)]
for E in subs:
    for p in subs:
        if B(gg, E) & p and not B(gg, E & p) <= B(gg, E):
            pres = False
E = frozenset(S)
pr("(1) Preservation for every E and discovery:", pres,
   "| K at b:", sorted("abc"[s] for s in K(geq, gg, E, 1)),
   "| after learning not-a, K at b:", sorted("abc"[s] for s in K(geq, gg, frozenset([1, 2]), 1)))

# (2) a > b > c, only a>>c, uniform, x=a, question whether a
geq = [[True, True, True], [False, True, True], [False, False, True]]
gg = [[False, False, True], [False, False, False], [False, False, False]]
P = [Fr(1)] * 3
acts = [[Fr(1), Fr(1), Fr(-10)], [Fr(0)] * 3, [Fr(9, 10), Fr(3, 2), Fr(-101, 10)]]
r = analyse(geq, gg, P, acts, E, 0, [[0], [1, 2]])
pr("(2) ken", sorted("abc"[s] for s in r["K"]), "| ev now", [f(v) for v in r["evnow"]], "| now act", r["now"] + 1,
   "| policy", {"abc"[s]: v + 1 for s, v in r["pol"].items()}, "| look ev", f(ev(P, r["ul"], r["K"])),
   "| KDT", f(r["kdt"]), "CEU", f(r["ceu"]))

# (3) five states a,s2,s1,v2,v1 ranks 0,.2,.5,1.15,1.3 ; u>>w iff rank gap > 1
names = ["a", "s2", "s1", "v2", "v1"]
geq, gg = from_ranks([Fr(0), Fr(1, 5), Fr(1, 2), Fr(115, 100), Fr(13, 10)], 1)
P = [Fr(67, 100), Fr(1, 100), Fr(30, 100), Fr(1, 100), Fr(1, 100)]
E = frozenset(range(5)); M = K(geq, gg, E, 0)
Pi = [[0], [2, 4], [1, 3]]
for s0 in (2, 1):
    N, eps, L = 10, Fr(1, 1000), Fr(304, 10)
    beta = [Fr(1) if s in M else -L for s in range(5)]
    beta1 = [beta[s] + eps * (N if s == s0 else -1) for s in range(5)]
    acts = [beta, [Fr(0)] * 5, beta1]
    r = analyse(geq, gg, P, acts, E, 0, Pi)
    diff = all(a[s] != b[s] for a, b in itertools.combinations(acts, 2) for s in E)
    Kd = r["condkens"].get(1, frozenset())
    pr(f"(3) s0={names[s0]}: ken", sorted(names[s] for s in r["K"]), "| now", ["beta", "decline", "beta1"][r["now"]],
       "| policy", {names[s]: ["beta", "decline", "beta1"][v] for s, v in r["pol"].items()},
       "| cond ken on decline", sorted(names[s] for s in Kd), "| beta1 ev there", f(ev(P, beta1, Kd)),
       "| KDT", f(r["kdt"]), "CEU", f(r["ceu"]), "VER", f(r["ver"]), "ANS", f(r["ans"]), "| pairs differ everywhere", diff,
       "| both nontrivial answers reopen:", all(not K(geq, gg, frozenset(c), c[0]) <= M for c in Pi[1:]))

# (4) a > x > b > c ; a>>x,b,c ; x>>c only ; uniform ; situation x
names = ["a", "x", "b", "c"]
geq = [[True] * 4, [False, True, True, True], [False, False, True, True], [False, False, False, True]]
gg = [[False, True, True, True], [False, False, False, True], [False] * 4, [False] * 4]
ok_chain = all(not (geq[w1][w2] and gg[w2][w3] and geq[w3][w4]) or gg[w1][w4]
               for w1 in range(4) for w2 in range(4) for w3 in range(4) for w4 in range(4))
P = [Fr(1)] * 4; E = frozenset(range(4))
acts = [[Fr(-2), Fr(31, 10), Fr(-2), Fr(21, 10)], [Fr(3), Fr(3), Fr(3), Fr(-3)]]
r = analyse(geq, gg, P, acts, E, 1, [[1], [2, 3], [0]])
lookge = all(r["ul"][s] >= acts[r["now"]][s] for s in r["K"])
pr("(4) chaining ok", ok_chain, "| ken", sorted(names[s] for s in r["K"]), "| relative defeat", r["rd"],
   "| now act", r["now"] + 1, "| policy", {names[s]: v + 1 for s, v in r["pol"].items()},
   "| look >= now on ken", lookge, "| cond ken on 'choose act1'", sorted(names[s] for s in r["condkens"][0]),
   "| KDT", f(r["kdt"]), "CEU", f(r["ceu"]), "VER", f(r["ver"]), "ANS", f(r["ans"]))

# (5a) K-normality: empty question can have positive value at an abnormal situation
geq = [[True, True], [False, True]]; gg = [[False, True], [False, False]]
P = [Fr(1), Fr(1)]; E = frozenset([0, 1])
acts = [[Fr(1), Fr(-11, 10)], [Fr(0), Fr(0)]]
r = analyse(geq, gg, P, acts, E, 1, [[0, 1]])
pr("(5a) two states a>>b, x=b: ken", sorted(r["K"]), "| empty-question KDT value", f(r["kdt"]))
# (5b) I-normality KK failure: ranks 0, .6, 1.2, gap 1
geq, gg = from_ranks([Fr(0), Fr(3, 5), Fr(6, 5)], 1)
I = lambda F, x: frozenset(v for v in F if not gg[x][v])
E = frozenset(range(3))
pr("(5b) I-normality: I(0) =", sorted(I(E, 0)), "; I(1) =", sorted(I(E, 1)), "; KK fails at 0:", not I(E, 1) <= I(E, 0))

# (6) counts with non-trivial partitions; (7) VER search
def total_preorders(n):
    for k in range(1, n + 1):
        for lv in itertools.product(range(k), repeat=n):
            if set(lv) == set(range(k)):
                yield lv
def structures(n):
    for lv in total_preorders(n):
        geq = [[lv[u] <= lv[v] for v in range(n)] for u in range(n)]
        cand = [(u, v) for u in range(n) for v in range(n) if lv[u] < lv[v]]
        for bits in range(1 << len(cand)):
            gg = [[False] * n for _ in range(n)]
            for i, (u, v) in enumerate(cand):
                if bits >> i & 1: gg[u][v] = True
            if all(not (geq[w1][w2] and gg[w2][w3] and geq[w3][w4]) or gg[w1][w4]
                   for w2 in range(n) for w3 in range(n) if gg[w2][w3] for w1 in range(n) for w4 in range(n)):
                yield geq, gg
def set_partitions(lst):
    if not lst:
        yield []; return
    first, rest = lst[0], lst[1:]
    for p in set_partitions(rest):
        yield [[first]] + p
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]

def fev(P, u, F):
    t = sum(P[s] for s in F); return sum(P[s] * u[s] for s in F) / t

random.seed(7)
nontriv = triv = 0
rdES = []
for n in range(1, 5):
    for geq, gg in structures(n):
        for r_ in range(1, n + 1):
            for E in itertools.combinations(range(n), r_):
                E = frozenset(E)
                for x in E:
                    Kx = K(geq, gg, E, x)
                    for Pi in set_partitions(sorted(E)):
                        if len(Pi) == 1: triv += 1; continue
                        nontriv += 1
                        if E == frozenset(range(n)) and any(
                                not K(geq, gg, E & cell(Pi, s), s) <= Kx for s in Kx):
                            rdES.append((n, geq, gg, x, Pi))
pr("(6) pairs with non-trivial partitions:", nontriv, "; trivial-partition pairs:", triv,
   "; relative-defeat pairs with E = S:", len(rdES))

def ver_float(n, geq, gg, P, acts, x, Pi):
    E = frozenset(range(n)); Kx = K(geq, gg, E, x)
    kens = {s: K(geq, gg, E & cell(Pi, s), s) for s in E}
    pol = {s: max(range(len(acts)), key=lambda i: (fev(P, acts[i], kens[s]), -i)) for s in E}
    now = max(range(len(acts)), key=lambda i: (fev(P, acts[i], Kx), -i))
    a = acts[now]; tot = sum(P[s] for s in Kx); v = 0
    for b in set(pol.values()):
        Db = frozenset(s for s in E if pol[s] == b)
        w = sum(P[s] for s in Db & Kx) / tot
        if w:
            v += w * fev(P, [acts[b][s] - a[s] for s in range(n)], condK(geq, gg, E, Db, x))
    return v

found_generic = found_any = 0
T = 150
for (n, geq, gg, x, Pi) in rdES:
    hit_generic = hit_any = False
    for t in range(T):
        P = [random.uniform(0.02, 1) for _ in range(n)]
        k = random.choice([2, 3])
        if t % 2:   # generic random acts
            acts = [[random.uniform(-10, 10) for _ in range(n)] for _ in range(k)]
        else:       # bet-like acts: a bet on a random set, declining, a perturbed bet
            Mset = [random.random() < 0.6 for _ in range(n)]
            Lr = random.uniform(1, 60)
            bet = [1.0 if Mset[s] else -Lr for s in range(n)]
            acts = [bet, [0.0] * n, [bet[s] + random.uniform(-0.6, 0.6) for s in range(n)]][:k + 1]
        if not all(abs(a[s] - b[s]) > 1e-9 for a, b in itertools.combinations(acts, 2) for s in range(n)):
            continue
        if ver_float(n, geq, gg, P, acts, x, Pi) < -1e-9:
            Pq = [Fr(p) for p in P]; aq = [[Fr(v) for v in a] for a in acts]
            r = analyse(geq, gg, Pq, aq, frozenset(range(n)), x, Pi)
            if r["ver"] < 0:
                hit_any = True
                if t % 2: hit_generic = True
                if hit_generic: break
    found_generic += hit_generic; found_any += hit_any
pr(f"(7) VER random search ({T} trials/pair, exact re-verification): pairs where VER disvalues the question:",
   found_any, "of", len(rdES), "; using generic random acts only:", found_generic)
print("\n".join(out))
