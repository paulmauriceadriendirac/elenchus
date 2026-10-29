# How widespread are failures of the verdict-conditioned rule (VER)?  For every situation-question
# pair with relative defeat in comparable statist K-normality structures with up to 4 (resp. 5)
# states, try random full-support priors with the Theorem-3 family and with random 3-act problems.
# (n <= 4 only: the five-state run was too slow for the time available.)
# Also: does VER ever disvalue a question where there is no relative defeat?
import random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from structs import structures, subsets, K_K
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from v4_conditional_rules import partitions, values, rel_defeat_witnesses
random.seed(11)
def run(nmax, trials):
    rd = fail = nonrd_fail = 0
    for nst in range(2, nmax + 1):
        for geq, gg in structures(nst, total=True):
            E = frozenset(range(nst))
            parts = [[frozenset(c) for c in p] for p in partitions(E) if len(p) > 1]
            for x in E:
                K = K_K(x, E, geq, gg)
                for Pi in parts:
                    W = rel_defeat_witnesses(E, x, Pi, geq, gg)
                    found = False
                    for _ in range(trials):
                        P = {s: random.random() ** 3 + 1e-3 for s in E}
                        if W:
                            s0 = random.choice(W)
                            pK = sum(P[s] for s in K); p0 = P[s0] / pK
                            N = random.uniform(1.01, 5) * 2 / p0
                            eps = random.choice([.001, .01, .1, .5])
                            need = 0.0
                            for c in Pi:
                                for s in c:
                                    k = K_K(s, E & c, geq, gg)
                                    if k <= K: continue
                                    q = sum(P[t] for t in k - K) / sum(P[t] for t in k)
                                    need = max(need, (1 + eps * N) / q)
                            L = need * random.choice([1.0001, 1.01, 1.1, 2])
                            beta = {s: 1 if s in K else -L for s in E}
                            beta1 = {s: beta[s] + eps * (N if s == s0 else -1) for s in E}
                            v = values([beta, {s: 0 for s in E}, beta1], E, x, Pi, geq, gg, P)
                            if v['a_now'] == 2 and v['ver'] < -1e-12: found = True
                        acts = [{s: random.uniform(-10, 10) for s in E} for _ in range(3)]
                        v = values(acts, E, x, Pi, geq, gg, P)
                        if v['ver'] < -1e-12:
                            if W: found = True
                            else: nonrd_fail += 1
                    if W:
                        rd += 1; fail += found
    return rd, fail, nonrd_fail
for nmax, trials in ((4, 40),):
    rd, fail, nf = run(nmax, trials)
    print('E = all states, n <= %d, %d random trials per pair: relative-defeat pairs %d; VER disvalues the question '
          'for some tried problem in %d; VER negative without relative defeat: %d' % (nmax, trials, rd, fail, nf))
