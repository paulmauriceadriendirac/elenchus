"""Core identity tests for the toy routine (construction, forms, Lemma 3.2,
Lemma 3.3, Hermite, end-to-end count)."""
import itertools
import random
import sys
import time

from toy_routine import (P, Factor, Design, brute_sum, ps_const, hermite_h0)


def random_cnf_factors(n, m, k, rng, weights=None):
    """m random clauses of width <= k as 'sat' factors, plus optional unary
    weight factors (dict v -> X).  Every variable is covered."""
    fs = []
    for _ in range(m):
        w = rng.randint(1, k)
        scope = rng.sample(range(n), w)
        signs = [rng.choice((1, -1)) for _ in scope]
        fs.append(Factor('sat', scope, signs))
    covered = {v for f in fs for v in f.scope}
    for v in range(n):
        if weights is not None and v in weights:
            fs.append(Factor('weight', [v], X=weights[v]))
        elif v not in covered:
            fs.append(Factor('one', [v]))
    return fs


def main(seed=1):
    rng = random.Random(seed)
    t0 = time.time()
    n = 5
    X = {v: rng.randrange(P) for v in range(n)}            # symbolic weights at random points
    fs = random_cnf_factors(n, 3, 3, rng, weights=X)
    des = Design(n, fs, r=2, Q=4, R=2, seed=seed)
    info = des.check_construction()
    dH, q, J = des.params()
    print('construction ok', info, 'd=%d dH=%d q=%d J=%d' % (des.d_total, dH, q, J))

    # forms: P(0) = delta_v, and separated form == direct form at every point, any x
    for trial in range(3):
        x = [rng.randrange(P) for _ in range(n)]
        for fi, f in enumerate(fs):
            for v in f.scope:
                assert des.form_direct(fi, v, 0, 1, x)[0] == x[v] % P
                for t in range(1, des.Q + 1):
                    g, local, mcoef = des.separated_pieces(fi, v, t)
                    val = sum(cf * x[w] for w, cf in local.items())
                    for key, cf in mcoef.items():
                        for w, mc in des.mform[key].items():
                            if des.a[w][t - 1] != g:
                                val += cf * mc * x[w]
                    assert val % P == des.form_direct(fi, v, t, 1, x)[0]
    print('forms ok: P(0)=delta and Definition 3.1(4) separation hold for random x')

    # Lemma 3.2 on random (t,E,U)
    for trial in range(12):
        t = rng.randint(1, des.Q)
        E = tuple(sorted(rng.sample(range(n), rng.randint(0, min(q, n)))))
        U = set(rng.sample(E, rng.randint(0, len(E))))
        assert des.Z_separated(t, J, E, U) == des.Z_brute(t, J, E, U), (t, E, U)
    print('Lemma 3.2 (separation) ok on 12 random (t,E,U)')

    # Lemma 3.3: Taylor data from substitutions == direct H(t+z)
    for t in range(1, des.Q + 1):
        assert des.taylor_data(t, J, q, separated=False) == des.H_brute(t, J)
    print('Lemma 3.3 (Taylor by inclusion-exclusion) ok at all points')

    # Hermite from direct data recovers H(0) = target
    data = {t: des.H_brute(t, J) for t in range(1, des.Q + 1)}
    target = brute_sum(n, fs)
    assert hermite_h0(data, des.Q, J) == target
    print('Hermite interpolation ok')

    # end to end with separation
    out = des.count(separated=True)
    assert out == target, (out, target)
    print('end-to-end routine == brute-force weighted sum (random X)  [%.1fs]' % (time.time() - t0))


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
