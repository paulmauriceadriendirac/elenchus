import sys, random
sys.path.insert(0, sys.argv[1])
from structs import structures, subsets, K_K, K_I, K_KM

# ---------- generic probabilistic normality (Goodman & Salow BRN Defs 6.2 / 8.2 / 10.2) ----------
def make_norm(E, pr, cellprob):
    """E: list of states (evidence); pr: prior dict; cellprob(s): Pr([s]_Q | E).
    Returns geq(a,b), gg(a,b) per BRN Def 6.2 with the question-relative weak order."""
    Z = sum(pr[s] for s in E)
    P = {s: pr[s] / Z for s in E}
    cp = {s: cellprob(s) for s in E}
    def geq(a, b): return cp[a] >= cp[b] - 1e-15
    def gg_t(t):
        def gg(a, b):
            if not (geq(a, b) and not geq(b, a)): return False
            no_more_normal_than_a = [s for s in E if geq(a, s)]
            more_normal_than_b = [s for s in no_more_normal_than_a if not geq(b, s)]
            den = sum(P[s] for s in no_more_normal_than_a)
            return sum(P[s] for s in more_normal_than_b) / den >= t - 1e-15
        return gg
    return P, geq, gg_t

def belief(E, gg):
    return [s for s in E if not any(gg(u, s) for u in E)]

def Kknorm(x, E, geq, gg):
    B = set(belief(E, gg))
    return B | {v for v in E if geq(v, x)}

# ---------- (A6-02) BRN section 10: Flipping for All Heads with a de se question ----------
q, N, xs, ys, t = 0.1, 400, 1, 40, 0.85
pr = {j: (1 - q) ** (j - 1) * q for j in range(1, N + 1)}
def E_i(i): return [j for j in range(i, N + 1)]
def cell_desé(i):
    # cells of the de se question, relative to evidence E_i: soon (j-i<xs), middle, late (j-i>ys)
    def lab(j):
        d = j - i
        return 0 if d < xs else (2 if d > ys else 1)
    return lab
def norm_for(i):
    E = E_i(i); lab = cell_desé(i)
    Z = sum(pr[s] for s in E)
    cellmass = {}
    for s in E: cellmass[lab(s)] = cellmass.get(lab(s), 0) + pr[s] / Z
    P, geq, gg_t = make_norm(E, pr, lambda s: cellmass[lab(s)])
    return E, P, geq, gg_t(t), cellmass
E1, P1, geq1, gg1, cm1 = norm_for(1)
E2, P2, geq2, gg2, cm2 = norm_for(2)
B1, B2 = belief(E1, gg1), belief(E2, gg2)
print("A6-02 Flipping for All Heads: cell masses at E1", {k: round(v, 4) for k, v in cm1.items()})
print("  B(E1) = trials", min(B1), "to", max(B1), "; B(E2) = trials", min(B2), "to", max(B2))
p_upper = max(B1)   # p: 'the coins all land heads by trial max(B1)'
print("  believed (and known at most-normal states) p: 'by trial %d'. Learning E2 (already believed: min B(E1)=%d>1)." % (p_upper, min(B1)))
print("  box-minus fails:", set(B1) <= set(E2) and not set(B2) <= set(B1))
x = 10
K0 = Kknorm(x, E1, geq1, gg1); K1 = Kknorm(x, E2, geq2, gg2)
print("  K-normality at actual trial %d: K0 = %d..%d, after discovery K1 = %d..%d; defeat at x:" % (x, min(K0), max(K0), min(K1), max(K1)), not K1 <= K0)
# KDT value of watching trial 1, bet paying 1 if p, -L otherwise
L = 50.0
def eu(K, f):
    Z = sum(pr[s] for s in K); return sum(pr[s] * f(s) for s in K) / Z
bet = lambda s: 1.0 if s <= p_upper else -L
now = max(eu(K0, bet), 0.0)
watch = 0.0; Z0 = sum(pr[s] for s in K0)
for s in K0:
    Kn = Kknorm(s, E2, geq2, gg2) if s >= 2 else {1}
    act = bet if eu(Kn, bet) > 0 else (lambda s: 0.0)
    watch += pr[s] / Z0 * act(s)
print("  KDT value now %.3f vs after watching an outcome already known %.3f -> VOI %.3f" % (now, watch, watch - now))
# Conditional Dominance under two readings of conditional belief, D = states where watching changes p-belief
D = [s for s in E1 if s >= 2]
B_cond_BRN = [s for s in B1 if s in D]            # BRN D.3: restrict accessibility within E1-normality
B_cond_disc = belief([s for s in E1 if s in D], gg2)  # belief upon discovering D (= E2)
print("  CD, BRN conditional belief: believes p on D?", all(s <= p_upper for s in B_cond_BRN), "-> recommends not watching")
print("  CD, discovery reading: believes p on D?", all(s <= p_upper for s in B_cond_disc), "-> silent")

# ---------- (A6-05) BRN section 7: Flipping for Heads with E' = {s1..sn} added ----------
n = 5; t2 = 1 - 0.5 ** (n - 1) + 0.01; M = 40
pr2 = {j: 0.5 ** j for j in range(1, M + 1)}
def norm_simple(E):
    Z = sum(pr2[s] for s in E)
    P, geq, gg_t = make_norm(E, pr2, lambda s: pr2[s] / Z)
    return geq, gg_t(t2)
S = list(range(1, M + 1)); Ep = list(range(1, n + 1)); Ec = list(range(n + 1, M + 1))
geqS, ggS = norm_simple(S); geqP, ggP = norm_simple(Ep); geqC, ggC = norm_simple(Ec)
BS, BP = belief(S, ggS), belief(Ep, ggP)
print("A6-05 BRN s.7: B(S) =", BS, " B(E') =", BP, " box-plus fails:", set(BS) <= set(Ep) and not set(BS) <= set(BP))
# belief-guided EU: acts on Pr(.|B); experiment {E', S\E'}; bet on 'not s_n' at price c
c = 0.97
betn = lambda s: (1.0 - c) if s != n else -c
def eu2(K, f):
    Z = sum(pr2[s] for s in K); return sum(pr2[s] * f(s) for s in K) / Z
mu = BS
now_b = max(eu2(mu, betn), 0.0)
look_b = 0.0; Zb = sum(pr2[s] for s in mu)
for s in mu:
    post = BP if s in Ep else belief(Ec, ggC)
    act = betn if eu2(post, betn) > 0 else (lambda s: 0.0)
    look_b += pr2[s] / Zb * act(s)
print("  belief-guided EU: value now %.4f, after learning what she believes %.4f -> VOI %.4f" % (now_b, look_b, look_b - now_b))
# knowledge-guided (K-normality) EU at every situation x in S, random decision problems + same bet
random.seed(1); worst = 0.0
for x0 in S[:12]:
    K0x = Kknorm(x0, S, geqS, ggS)
    for trial in range(300):
        acts = [betn, (lambda s: 0.0)] if trial == 0 else [ {s: random.uniform(-3, 3) for s in S}.get for _ in range(3)]
        Zk = sum(pr2[s] for s in K0x)
        nowk = max(sum(pr2[s] * a(s) for s in K0x) / Zk for a in acts)
        val = 0.0
        for s in K0x:
            if s in Ep: Kn = Kknorm(s, Ep, geqP, ggP)
            else: Kn = Kknorm(s, Ec, geqC, ggC)
            best = max(acts, key=lambda a: eu2(Kn, a))
            val += pr2[s] / Zk * best(s)
        worst = min(worst, val - nowk)
print("  knowledge-guided EU (K-normality), all actual situations 1..12, 3600 problems: min VOI %.2e" % worst)

# ---------- (A6-04) co-occurrence of knowledge defeat and KK failure, statist structures ----------
for total, ns in ((True, (2, 3, 4)), (False, (2, 3))):
    for nn in ns:
        res = {}
        for name, Kf in (("K", K_K), ("I", K_I), ("KM", K_KM)):
            both = defeat = kkfail = 0
            for geq, gg in structures(nn, total=total):
                for Y in subsets(nn):
                    for x0 in Y:
                        K0x = Kf(x0, Y, geq, gg)
                        kkf = any(not Kf(s, Y, geq, gg) <= K0x for s in K0x)
                        dft = any(x0 in p and not Kf(x0, p, geq, gg) <= K0x for p in subsets(nn) if p <= Y)
                        kkfail += kkf; defeat += dft; both += (kkf and dft)
            res[name] = (defeat, kkfail, both)
        print("A6-04", "comparable" if total else "non-comparable", nn, "(defeat, KK-failure, both):", res)
