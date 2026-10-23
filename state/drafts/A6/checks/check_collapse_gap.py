# Corollary check: in statist structures satisfying COLLAPSE and COMPARABILITY (all, n <= 5),
# every K-normality ken is gapped, hence (Theorem 1) every question is safe for KDT.
# Also: in every statist comparable structure (n <= 4), a set is gapped and contains x only if it
# contains C(x), the closure of {x} under steps to states not sufficiently less normal.
import sys
sys.path.insert(0, sys.argv[1])
from structs import structures, subsets, K_K, strict
def collapse(geq, gg):
    n = len(geq)
    return all(gg[a][b] for a in range(n) for b in range(n) if strict(geq, a, b))
def gapped(M, E, gg): return all(gg[a][b] for a in M for b in E - M)
def C(x, E, gg):
    out = {x}; fr = [x]
    while fr:
        s = fr.pop()
        for v in E:
            if v not in out and not gg[s][v]:
                out.add(v); fr.append(v)
    return frozenset(out)
for n in range(1, 6):
    nc = bad = 0
    for geq, gg in structures(n, True):
        if not collapse(geq, gg): continue
        nc += 1
        for E in subsets(n):
            for x in E:
                if not gapped(K_K(x, E, geq, gg), E, gg): bad += 1
    print("n=%d collapse+comparability structures: %d; non-gapped K-kens: %d" % (n, nc, bad))
for n in range(1, 5):
    bad = 0
    for geq, gg in structures(n, True):
        for E in subsets(n):
            for x in E:
                Cx = C(x, E, gg)
                for M in subsets(n):
                    if M <= E and x in M and gapped(M, E, gg) and not Cx <= M: bad += 1
    print("n=%d gapped sets containing x but not C(x): %d" % (n, bad))
