import sys, random
sys.path.insert(0, sys.argv[1])
from structs import *
from check1 import binary_experiments, gap, good_struct
from check2 import defeat_question
random.seed(12345)

def best_act(acts, prob, K):
    # maximize expected utility under prob conditioned on K; ties -> first
    Z = sum(prob[s] for s in K)
    best, bv = None, None
    for i, a in enumerate(acts):
        v = sum(prob[s] * a[s] for s in K) / Z
        if bv is None or v > bv + 1e-12:
            best, bv = i, v
    return best

def voi(Kfun, x, Y, p, geq, gg, prob, acts):
    K0 = Kfun(x, Y, geq, gg)
    Z = sum(prob[s] for s in K0)
    mu = {s: prob[s] / Z for s in K0}
    now = max(sum(mu[s] * a[s] for s in K0) for a in acts)
    cells = [p, Y - p] if p != Y else [Y]
    val = 0.0
    for c in cells:
        if not c: continue
        for s in c:
            if s in K0:
                K1 = Kfun(s, Y & c, geq, gg)
                i = best_act(acts, prob, K1)
                val += mu[s] * acts[i][s]
    return val - now

n = 4
structs = list(structures(n, True))
neg_when_good = 0; good_trials = 0; bet_fail = 0; bet_trials = 0; min_good = 0.0
for trial in range(6000):
    geq, gg = random.choice(structs)
    Y = frozenset(random.sample(range(n), random.randint(2, n)))
    x = random.choice(sorted(Y))
    prob = {s: random.random() + 0.05 for s in range(n)}
    for Kf in (K_K, K_I, K_KM):
        if good_struct(Kf, x, Y, geq, gg):
            for p in binary_experiments(Y):
                acts = [{s: random.uniform(-5, 5) for s in range(n)} for _ in range(3)]
                v = voi(Kf, x, Y, p, geq, gg, prob, acts)
                good_trials += 1
                min_good = min(min_good, v)
                if v < -1e-9: neg_when_good += 1
        dq = defeat_question(Kf, x, Y, geq, gg)
        if dq is not None:
            v_, p, k = dq
            K0 = Kf(x, Y, geq, gg)
            L = 1e6
            bet = {s: (1.0 if s in K0 else -L) for s in range(n)}
            nobet = {s: 0.0 for s in range(n)}
            vv = voi(Kf, x, Y, p, geq, gg, prob, [bet, nobet])
            bet_trials += 1
            if not vv < 0: bet_fail += 1
print("good-structure trials:", good_trials, "negative VOI found:", neg_when_good, "min VOI:", min_good)
print("defeat-question bet trials:", bet_trials, "bet failed to give negative VOI:", bet_fail)
