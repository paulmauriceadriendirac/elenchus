#!/usr/bin/env python3
"""A5 formal audit, script a7: does Theorem 1's non-monotonicity extend to proposition-dependent conservative values
(as the abstract's wording 'for every positive premium and conservative values' suggests)?
Exact integer arithmetic: credences k/200 on 3 worlds (20,301 grid points incl. the essay's C and C'), all 2^8 states.
For each proposition p: non-monotone on the grid iff some credence with p in EVERY optimum has C(p) lower than some
credence with p in NO optimum. Sanity run with uniform values must detect the essay's case."""
N = 200
n = 3
props = range(8)


def run(T, F, beta, label):
    tab = []
    for S in range(256):
        core = 7
        for p in props:
            if S >> p & 1:
                core &= p
        tab.append([sum((T[p] if p >> w & 1 else F[p]) for p in props if S >> p & 1) + (beta if core >> w & 1 else 0)
                    for w in range(n)])
    min_in = {p: None for p in props}
    max_out = {p: None for p in props}
    for i in range(N + 1):
        for j in range(N + 1 - i):
            c = (i, j, N - i - j)
            ea = [c[0] * r[0] + c[1] * r[1] + c[2] * r[2] for r in tab]
            m = max(ea)
            opt = [S for S in range(256) if ea[S] == m]
            for p in props:
                cp = sum(c[w] for w in range(n) if p >> w & 1)
                if all(S >> p & 1 for S in opt):
                    min_in[p] = cp if min_in[p] is None else min(min_in[p], cp)
                if not any(S >> p & 1 for S in opt):
                    max_out[p] = cp if max_out[p] is None else max(max_out[p], cp)
    nm = {p: (min_in[p], max_out[p]) for p in props if min_in[p] is not None and max_out[p] is not None and min_in[p] < max_out[p]}
    print(f"{label}: non-monotone propositions on the grid (bitmask: (lowest C*200 with p required, highest C*200 with p excluded)): {nm}")
    return nm


uni = run([1] * 8, [-2] * 8, 3, "uniform T=1,F=-2, beta=3 (sanity: the essay's case)")
print("OK  " if 1 in uni else "FAIL", "sanity: {w1} detected as non-monotone with uniform values")
T = [1] * 8
F = [-2 if bin(p).count("1") in (0, 1, 3) else -99 for p in props]  # doubletons: threshold 0.99; others 2/3
dep = run(T, F, 3, "proposition-dependent conservative values (singletons tau=2/3, doubletons tau=0.99), beta=3")
print("RESULT:", "no non-monotonicity found on the grid for these conservative proposition-dependent values" if not dep
      else "non-monotonicity found for these values too")
