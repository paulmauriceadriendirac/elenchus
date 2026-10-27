"""(A) IPS: with g_i compiled by the routine over symbolic weights,
    sum_i f_i(X) g_i(X) = 1 on unsatisfiable CNFs (Schwartz-Zippel at random X).
(B) Density gadgets: OR-gate splitting and Tovey copying with the weight on
    one copy preserve weighted model counts; Appendix-A sparsification leaves
    partition the satisfying assignments, so weighted counts add up."""
import itertools
import random
import sys
import time

from toy_routine import P, Factor, Design, brute_sum


# ------------------------------------------------------------------ CNF utils
def sat_assign(clauses, x):
    return all(any((x[abs(l) - 1] == 1) == (l > 0) for l in c) for c in clauses)


def is_unsat(n, clauses):
    return not any(sat_assign(clauses, x) for x in itertools.product((0, 1), repeat=n))


def random_unsat_core(n, k, rng):
    while True:
        cls = []
        while not is_unsat(n, cls):
            vs = rng.sample(range(1, n + 1), k)
            cls.append(tuple(v if rng.random() < .5 else -v for v in vs))
        # greedy minimisation to an unsatisfiable core
        i = 0
        while i < len(cls):
            trial = cls[:i] + cls[i + 1:]
            if is_unsat(n, trial):
                cls = trial
            else:
                i += 1
        return cls


def viol_value(clause, X):
    p = 1
    for l in clause:
        xv = X[abs(l) - 1]
        L = xv if l > 0 else (1 - xv)
        p = p * (1 - L) % P
    return p


def g_family(clauses, i, X):
    """factor family whose cube sum is g_i(X) (first-violated-clause coefficient)."""
    n_scope = {abs(l) - 1 for l in clauses[i]}
    fs = [Factor('sat', [abs(l) - 1 for l in c], [1 if l > 0 else -1 for l in c])
          for c in clauses[:i]]
    fs.append(Factor('viol', [abs(l) - 1 for l in clauses[i]],
                     [1 if l > 0 else -1 for l in clauses[i]]))
    return fs, n_scope


def test_ips(seed, n, Q=4):
    rng = random.Random(seed)
    clauses = random_unsat_core(n, 3, rng)
    X = [rng.randrange(P) for _ in range(n)]
    total = 0
    t0 = time.time()
    for i in range(len(clauses)):
        fs, Vi = g_family(clauses, i, X)
        for v in range(n):
            if v not in Vi:
                fs.append(Factor('weight', [v], X=X[v]))
        des = Design(n, fs, r=2, Q=Q, R=2, seed=seed + i)
        gi = des.count(separated=True)
        assert gi == brute_sum(n, fs)
        total = (total + viol_value(clauses[i], X) * gi) % P
        print('  g_%d compiled by the routine matches the cube sum (d=%d, q=%d) [%.1fs]'
              % (i + 1, des.d_total, des.params()[1], time.time() - t0), flush=True)
    assert total == 1, total
    print('IPS identity sum_i f_i g_i = 1 holds with routine-compiled g_i: n=%d, m=%d core clauses [%.1fs]'
          % (n, len(clauses), time.time() - t0))


# ------------------------------------------------------------- gadgets
def or_split(n, clauses):
    """width<=3 via binary OR gates (unique extension). Returns (N, 3-CNF)."""
    N, out = n, []
    for c in clauses:
        if len(c) <= 3:
            out.append(tuple(c))
            continue
        prev = c[0]
        for lit in c[1:]:
            N += 1
            z = N
            out += [(-prev, z), (-lit, z), (prev, lit, -z)]
            prev = z
        out.append((prev,))
    return N, out


def tovey(N, clauses, weighted_vars):
    """replace each occurrence by its own copy, add an implication cycle.
    Returns (N2, clauses2, weight_pos) with weight_pos[v] = one copy of v."""
    occ = {}
    for ci, c in enumerate(clauses):
        for li, l in enumerate(c):
            occ.setdefault(abs(l), []).append((ci, li))
    new = [list(c) for c in clauses]
    nxt, weight_pos, cyc = N, {}, []
    for v in range(1, N + 1):
        lst = occ.get(v, [])
        if len(lst) <= 1:
            weight_pos[v] = v
            continue
        copies = []
        for idx, (ci, li) in enumerate(lst):
            if idx == 0:
                cp = v                      # the original variable is the first copy
            else:
                nxt += 1
                cp = nxt
            copies.append(cp)
            l = new[ci][li]
            new[ci][li] = cp if l > 0 else -cp
        for a, b in zip(copies, copies[1:] + copies[:1]):
            cyc.append((-a, b))
        weight_pos[v] = copies[0]
    return nxt, [tuple(c) for c in new] + cyc, weight_pos


def factors_from(clauses, weights_at, nvars):
    fs = [Factor('sat', [abs(l) - 1 for l in c], [1 if l > 0 else -1 for l in c]) for c in clauses]
    covered = {abs(l) - 1 for c in clauses for l in c}
    for var, X in weights_at.items():
        fs.append(Factor('weight', [var - 1], X=X))
        covered.add(var - 1)
    for v in range(nvars):
        if v not in covered:
            fs.append(Factor('one', [v]))
    return fs


def wcount(N, clauses, weights):
    """weighted model count over {0,1}^N with weight X_v / (1 - X_v) on
    weighted variables (1-based), by bitmask enumeration."""
    masks = []
    for c in clauses:
        pos = sum(1 << (l - 1) for l in c if l > 0)
        neg = sum(1 << (-l - 1) for l in c if l < 0)
        masks.append((pos, neg))
    full = (1 << N) - 1
    wl = [(v - 1, X % P) for v, X in weights.items()]
    tot = 0
    for x in range(1 << N):
        nx = full ^ x
        if all((x & pm) or (nx & nm) for pm, nm in masks):
            w = 1
            for b, X in wl:
                w = w * (X if (x >> b) & 1 else 1 - X) % P
            tot = (tot + w) % P
    return tot


def random_clauses(n, m, kmin, kmax, rng):
    out = []
    for _ in range(m):
        w = rng.randint(kmin, kmax)
        vs = rng.sample(range(1, n + 1), min(w, n))
        out.append(tuple(v if rng.random() < .5 else -v for v in vs))
    return out


def test_gadgets(seed):
    rng = random.Random(seed)
    # OR-gate splitting: wide clauses -> 3-CNF with fresh gate variables (weight 1)
    n = 5
    clauses = random_clauses(n, 4, 1, 5, rng)
    X = {v: rng.randrange(P) for v in range(1, n + 1)}
    N1, c1 = or_split(n, clauses)
    assert all(len(c) <= 3 for c in c1)
    assert wcount(n, clauses, X) == wcount(N1, c1, X)
    # Tovey copying on a 3-CNF, weight kept on one copy only
    n2 = 4
    c3 = random_clauses(n2, 4, 1, 3, rng)
    X2 = {v: rng.randrange(P) for v in range(1, n2 + 1)}
    N2, c4, wp = tovey(n2, c3, set(X2))
    occmax = max(sum(1 for c in c4 for l in c if abs(l) == v) for v in range(1, N2 + 1))
    assert occmax <= 3
    assert wcount(n2, c3, X2) == wcount(N2, c4, {wp[v]: X2[v] for v in X2})
    return N1, N2, occmax


# ------------------------------------------------------- Appendix A branching
def normalize(clauses):
    cs = set()
    for c in clauses:
        s = frozenset(c)
        if any(-l in s for l in s):
            continue
        cs.add(s)
    return [c for c in cs if not any(o < c for o in cs)]


def sparsify(clauses, k, M):
    theta = [M ** j for j in range(k)]
    leaves, stack = [], [normalize(clauses)]
    while stack:
        F = stack.pop()
        if any(len(c) == 0 for c in F):
            leaves.append(F)
            continue
        choice = None
        for c in range(2, k + 1):
            best = None
            wide = [C for C in F if len(C) == c]
            for C in wide:
                for hsize in range(c - 1, 0, -1):
                    for H in itertools.combinations(sorted(C), hsize):
                        Hs = frozenset(H)
                        deg = sum(1 for C2 in wide if Hs <= C2)
                        if deg >= theta[c - hsize]:
                            if best is None or hsize > len(best[1]) or (
                                    hsize == len(best[1]) and sorted(H) < sorted(best[1])):
                                best = (c, Hs)
            if best:
                choice = best
                break
        if choice is None:
            leaves.append(F)
            continue
        c, H = choice
        sel = [C for C in F if len(C) == c and H <= C]
        G = [C for C in F if not (len(C) == c and H <= C)]
        FA = normalize(G + [H])
        FB = normalize(G + [C - H for C in sel] + [frozenset([-l]) for l in H])
        stack += [FA, FB]
    return leaves


def test_sparsify(seed, n=6, m=14, k=3, M=2):
    rng = random.Random(seed)
    clauses = []
    for _ in range(m):
        vs = rng.sample(range(1, n + 1), k)
        clauses.append(tuple(v if rng.random() < .5 else -v for v in vs))
    leaves = sparsify(clauses, k, M)
    for x in itertools.product((0, 1), repeat=n):
        hits = sum(1 for L in leaves if sat_assign(L, x))
        assert hits == (1 if sat_assign(clauses, x) else 0)
    X = {v: rng.randrange(P) for v in range(1, n + 1)}
    W = brute_sum(n, factors_from(clauses, X, n))
    Ws = sum(brute_sum(n, factors_from([tuple(c) for c in L], X, n)) for L in leaves) % P
    assert W == Ws
    occ = max((sum(1 for c in L for l in c if abs(l) == v) for L in leaves for v in range(1, n + 1)),
              default=0)
    return len(leaves), occ


if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'gadgets'
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 21
    if what == 'gadgets':
        for s in range(seed, seed + 5):
            print('gadgets ok (N after OR-split, N after Tovey, max occurrences):',
                  test_gadgets(s), flush=True)
            print('sparsification ok (leaves, max occurrences in a leaf):',
                  test_sparsify(s), flush=True)
    else:
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 4
        Q = int(sys.argv[4]) if len(sys.argv) > 4 else 4
        test_ips(seed, n, Q=Q)
