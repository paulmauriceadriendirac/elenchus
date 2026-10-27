"""Weaker-assumption check: the routine run with symbolic weights is
(1) affine in each weight X_v (hence multilinear), and
(2) at Boolean X it is *the same computation* as the numeric routine on the
    CNF with unit clauses pinning those variables.
So numeric correctness on pinned CNFs forces the symbolic output to equal the
weighted model count (a multilinear polynomial is fixed by its cube values)."""
import random
import sys

from toy_routine import P, Factor, Design, brute_sum
from test_core import random_cnf_factors


def with_weights(base, X):
    out = []
    for f in base:
        if f.kind == 'weight':
            out.append(Factor('weight', f.scope, X=X[f.scope[0]]))
        else:
            out.append(f)
    return out


def pinned(base, beta):
    """replace each weight factor by the unit clause x_v = beta_v (same scope)."""
    out = []
    for f in base:
        if f.kind == 'weight':
            v = f.scope[0]
            out.append(Factor('sat', [v], [1 if beta[v] else -1]))
        else:
            out.append(f)
    return out


def main(seed=11, n=5, m=4):
    rng = random.Random(seed)
    X0 = {v: rng.randrange(P) for v in range(n)}
    base = random_cnf_factors(n, m, 3, rng, weights=X0)
    run = lambda fs: Design(n, fs, r=2, Q=4, R=2, seed=seed).count(separated=True)

    # (1) affine in each X_v
    for v in range(n):
        vals = {}
        for xv in (0, 1, rng.randrange(P)):
            X = dict(X0)
            X[v] = xv
            vals[xv] = run(with_weights(base, X))
        (r_,) = [k for k in vals if k not in (0, 1)]
        assert vals[r_] == ((1 - r_) * vals[0] + r_ * vals[1]) % P
    print('symbolic output is affine in every weight variable (multilinear)')

    # (2) Boolean X == numeric run on the pinned CNF == pinned count
    for trial in range(6):
        beta = {v: rng.randint(0, 1) for v in range(n)}
        sym = run(with_weights(base, beta))
        num = run(pinned(base, beta))
        assert sym == num == brute_sum(n, pinned(base, beta))
    print('at Boolean X the symbolic run equals the numeric run on the pinned CNF')

    # (3) consequence: symbolic output == weighted count at random points
    for trial in range(4):
        X = {v: rng.randrange(P) for v in range(n)}
        assert run(with_weights(base, X)) == brute_sum(n, with_weights(base, X))
    print('symbolic output == weighted model count at random X')


if __name__ == '__main__':
    main(*(int(a) for a in sys.argv[1:]))
