# v4 checks for section 5: three expected-utility developments of Conditional Knowledge Dominance
# in finite statist comparable K-normality structures.
#   CEU (difference-conditioned): condition on D = {u_look != u_a}.
#   VER (verdict-conditioned):    sum_b Pr([look->b] | K) * E[u_b - u_a | K^{[look->b]}].
#   ANS (answer-indexed):          sum_c Pr(c | K) * E[u_look - u_a | K^c].
# K^D_E(x) = RB(E & D) | {v in E & D : v >= x}  (the essay's K-normality conditional ken).
# Checks:
#  (1) the five-state example (ranks 0,.2,.5,1.15,1.3; u >> w iff rank gap > 1);
#  (2) ANS never gives a free question negative value (random problems, all structures n<=4);
#  (3) Proposition 5: whenever there is relative defeat, ANS pays a positive price kappa to look
#      against the Lemma-1 bet, although the costly look differs from the bet at every state and
#      is worse at every state of K (so Conditional Knowledge Dominance, with D = E, forbids it);
#  (4) VER on the Theorem-3 family: in how many relative-defeat cases does some member make VER
#      strictly prefer acting now?
import itertools, random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from structs import structures, subsets, RB, K_K

random.seed(7)

def partitions(s):
    s = list(s)
    if not s:
        yield []
        return
    first, rest = s[0], s[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [p[i] | {first}] + p[i+1:]
        yield p + [frozenset([first])]

def EV(u, S, P):
    tot = sum(P[s] for s in S)
    return sum(P[s] * u[s] for s in S) / tot

def Kc(D, E, x, geq, gg):
    ED = E & D
    return RB(ED, gg) | frozenset(v for v in ED if geq[v][x])

def plan(acts, E, Pi, geq, gg, P):
    """alpha(s): KDT choice at <s, E & cell(s)> (ties -> first in list)."""
    alpha = {}
    for c in Pi:
        for s in c:
            k = K_K(s, E & c, geq, gg)
            best = max(range(len(acts)), key=lambda i: (EV(acts[i], k, P), -i))
            alpha[s] = best
    return alpha

def values(acts, E, x, Pi, geq, gg, P):
    K = K_K(x, E, geq, gg)
    alpha = plan(acts, E, Pi, geq, gg, P)
    look = {s: acts[alpha[s]][s] for s in E}
    a_now = max(range(len(acts)), key=lambda i: (EV(acts[i], K, P), -i))
    a = acts[a_now]
    kdt = EV(look, K, P) - EV(a, K, P)
    D = frozenset(s for s in E if look[s] != a[s])
    ceu = EV({s: look[s] - a[s] for s in E}, Kc(D, E, x, geq, gg), P) if D else 0.0
    pK = sum(P[s] for s in K)
    ver = 0.0
    for b in set(alpha.values()):
        Db = frozenset(s for s in E if alpha[s] == b)
        w = sum(P[s] for s in Db & K) / pK
        if w > 0:
            ver += w * EV({s: acts[b][s] - a[s] for s in E}, Kc(Db, E, x, geq, gg), P)
    ans = 0.0
    for c in Pi:
        w = sum(P[s] for s in c & K) / pK
        if w > 0:
            ans += w * EV({s: look[s] - a[s] for s in E}, Kc(c, E, x, geq, gg), P)
    return dict(K=K, alpha=alpha, a_now=a_now, kdt=kdt, ceu=ceu, ver=ver, ans=ans)

# ---------------- (1) five-state example ----------------
names = ['a', 's2', 's1', 'v2', 'v1']
rank = [0, .2, .5, 1.15, 1.3]
n = 5
geq = [[rank[i] <= rank[j] for j in range(n)] for i in range(n)]
gg = [[rank[j] - rank[i] > 1 for j in range(n)] for i in range(n)]
P = [.67, .01, .30, .01, .01]
E = frozenset(range(n))
x = 0
Pi = [frozenset([0]), frozenset([2, 4]), frozenset([1, 3])]
K = K_K(x, E, geq, gg)
L, N, eps, s0 = 30.4, 10, .001, 2
beta = [1 if s in K else -L for s in range(n)]
zeta = [N if s == s0 else -1 for s in range(n)]
beta1 = [beta[s] + eps * zeta[s] for s in range(n)]
decl = [0] * n
acts = [beta, decl, beta1]
v = values(acts, E, x, Pi, geq, gg, P)
print('(1) five-state example')
print('  K(a) =', sorted(names[s] for s in v['K']), ' act now =', ['beta', 'decline', 'beta1'][v['a_now']])
print('  look policy:', {names[s]: ['beta', 'decline', 'beta1'][v['alpha'][s]] for s in E})
print('  conditional ken on [look->decline]:', sorted(names[s] for s in Kc(frozenset([1, 2, 3, 4]), E, x, geq, gg)))
print('  KDT %.4f  CEU %.4f  VER %.4f  ANS %.4f' % (v['kdt'], v['ceu'], v['ver'], v['ans']))
# pairwise differences everywhere?
print('  primitive acts differ everywhere:', all(acts[i][s] != acts[j][s] for i in range(3) for j in range(i+1, 3) for s in E))

# ---------------- (2)-(4) enumeration ----------------
def rel_defeat_witnesses(E, x, Pi, geq, gg):
    K = K_K(x, E, geq, gg)
    out = []
    for c in Pi:
        for s in c & K:
            if not K_K(s, E & c, geq, gg) <= K:
                out.append(s)
    return out

cases = rd_cases = ans_neg = 0
prop5_ok = prop5_fail = 0
ver_fail_cases = 0
ceu_fail_cases = 0
for nst in range(2, 5):
    for geq, gg in structures(nst, total=True):
        for E in subsets(nst):
            if len(E) < 2: continue
            parts = [ [frozenset(c) for c in p] for p in partitions(E) if len(p) > 1]
            for x in E:
                K = K_K(x, E, geq, gg)
                for Pi in parts:
                    cases += 1
                    # (2) ANS safety on random problems
                    for _ in range(3):
                        P = {s: random.random() + .05 for s in E}
                        acts = [{s: random.uniform(-5, 5) for s in E} for _ in range(3)]
                        if values(acts, E, x, Pi, geq, gg, P)['ans'] < -1e-9:
                            ans_neg += 1
                    W = rel_defeat_witnesses(E, x, Pi, geq, gg)
                    if not W: continue
                    rd_cases += 1
                    P = {s: 1.0 / len(E) for s in E}
                    # (3) Proposition 5: Lemma-1 bet, large L, costly look
                    Lb = 1000.0
                    beta = {s: 1 if s in K else -Lb for s in E}
                    acts = [beta, {s: 0 for s in E}]
                    v = values(acts, E, x, Pi, geq, gg, P)
                    look = {s: acts[v['alpha'][s]][s] for s in E}
                    kappa = 0.5 * v['ans'] if v['ans'] > 0 else None
                    if kappa:
                        # costly look differs from beta everywhere and is worse on K
                        diff_all = all(look[s] - kappa != beta[s] for s in E)
                        worse_on_K = all(look[s] - kappa < beta[s] for s in K)
                        if diff_all and worse_on_K and v['kdt'] < 0:
                            prop5_ok += 1
                        else:
                            prop5_fail += 1
                    else:
                        prop5_fail += 1
                    # (4) VER and CEU on the Theorem-3 family
                    found_ver = found_ceu = False
                    for s0 in W:
                        pK = sum(P[s] for s in K)
                        p0 = P[s0] / pK
                        for Nf in (1.01, 3, 10):
                            N = Nf * 2 / p0
                            for eps in (.001, .1, .5):
                                # minimal L making every reopening post-ken decline beta and beta1
                                need = 0.0
                                for c in Pi:
                                    for s in c:
                                        k = K_K(s, E & c, geq, gg)
                                        if k <= K: continue
                                        q = sum(P[t] for t in k - K) / sum(P[t] for t in k)
                                        need = max(need, (1 + eps * N) / q)
                                for eta in (1.001, 1.1, 2, 10):
                                    L = need * eta
                                    beta = {s: 1 if s in K else -L for s in E}
                                    beta1 = {s: beta[s] + eps * (N if s == s0 else -1) for s in E}
                                    acts = [beta, {s: 0 for s in E}, beta1]
                                    v = values(acts, E, x, Pi, geq, gg, P)
                                    if v['a_now'] != 2: continue
                                    if v['ver'] < -1e-12: found_ver = True
                                    if v['ceu'] < -1e-12: found_ceu = True
                    ver_fail_cases += found_ver
                    ceu_fail_cases += found_ceu
print('(2) situation-question pairs (n<=4, comparable statist):', cases,
      '; ANS negative on random problems:', ans_neg)
print('(3) relative-defeat cases:', rd_cases, '; Prop 5 confirmed:', prop5_ok, '; not confirmed:', prop5_fail)
print('(4) Theorem-3 family: CEU prefers acting now in', ceu_fail_cases, 'of', rd_cases,
      'cases; VER prefers acting now in', ver_fail_cases, 'of', rd_cases)
