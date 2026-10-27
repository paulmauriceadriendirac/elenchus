import random, sys, time, itertools
from toy_routine import P, Factor, Design, brute_sum, hermite_h0
from test_core import random_cnf_factors

def run(seed, n, m, k, r, Q, R, A0=None):
    rng = random.Random(seed)
    X = {v: rng.randrange(P) for v in range(n)}
    fs = random_cnf_factors(n, m, k, rng, weights=X)
    des = Design(n, fs, r=r, Q=Q, R=R, A0=A0, seed=seed)
    info = des.check_construction()
    dH, q, J = des.params()
    for trial in range(6):
        t = rng.randint(1, Q)
        E = tuple(sorted(rng.sample(range(n), rng.randint(0, min(q, n)))))
        U = set(rng.sample(E, rng.randint(0, len(E))))
        assert des.Z_separated(t, J, E, U) == des.Z_brute(t, J, E, U)
    for t in range(1, Q + 1):
        assert des.taylor_data(t, J, q, separated=False) == des.H_brute(t, J)
    target = brute_sum(n, fs)
    out = des.count(separated=True)
    assert out == target
    return info, (des.d_total, dH, q, J), sorted(des.I)

configs = [  # seed, n, m, k, r, Q, R
    (2, 6, 4, 3, 2, 4, 2), (3, 6, 5, 3, 2, 5, 2), (4, 5, 4, 3, 2, 5, 3),
    (5, 5, 3, 3, 3, 3, 2), (6, 6, 6, 2, 2, 4, 3), (7, 4, 4, 3, 3, 3, 3),
]
for cfg in configs:
    t0 = time.time()
    info, par, I = run(*cfg)
    print('seed=%d n=%d m=%d k=%d r=%d Q=%d R=%d I=%s' % (cfg + (I,)), info, 'd,dH,q,J=', par, 'ok [%.1fs]' % (time.time() - t0), flush=True)
