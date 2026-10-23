# Enumerate statist normality structures (G&S 2023 constraints) on n states.
# geq[a][b]: a is at least as normal as b (reflexive, transitive preorder)
# gg[a][b]:  a is sufficiently more normal than b (irreflexive, implies geq, chaining:
#            w1>=w2 >> w3 >= w4  => w1 >> w4)
import itertools

def preorders(n, total=True):
    """All (total if total=True) preorders on range(n) as geq matrices."""
    if total:
        # weak orders = ordered set partitions: assign rank 0..n-1, normalize
        seen = set()
        for ranks in itertools.product(range(n), repeat=n):
            used = sorted(set(ranks))
            norm = tuple(used.index(r) for r in ranks)
            if norm in seen: continue
            seen.add(norm)
            geq = [[norm[a] <= norm[b] for b in range(n)] for a in range(n)]  # lower rank = more normal
            yield geq
    else:
        pairs = [(a, b) for a in range(n) for b in range(n) if a != b]
        for bits in itertools.product([0, 1], repeat=len(pairs)):
            geq = [[a == b for b in range(n)] for a in range(n)]
            for (a, b), t in zip(pairs, bits):
                if t: geq[a][b] = True
            # transitivity check
            ok = all(not (geq[a][b] and geq[b][c]) or geq[a][c]
                     for a in range(n) for b in range(n) for c in range(n))
            if ok: yield geq

def strict(geq, a, b):
    return geq[a][b] and not geq[b][a]

def gg_relations(geq):
    n = len(geq)
    cand = [(a, b) for a in range(n) for b in range(n) if strict(geq, a, b)]
    for bits in itertools.product([0, 1], repeat=len(cand)):
        gg = [[False]*n for _ in range(n)]
        for (a, b), t in zip(cand, bits):
            if t: gg[a][b] = True
        ok = True
        for w1 in range(n):
            for w2 in range(n):
                if not geq[w1][w2]: continue
                for w3 in range(n):
                    if not gg[w2][w3]: continue
                    for w4 in range(n):
                        if geq[w3][w4] and not gg[w1][w4]:
                            ok = False; break
                    if not ok: break
                if not ok: break
            if not ok: break
        if ok: yield gg

def structures(n, total=True):
    for geq in preorders(n, total):
        for gg in gg_relations(geq):
            yield geq, gg

def subsets(n):
    for m in range(1, 1 << n):
        yield frozenset(i for i in range(n) if m >> i & 1)

# ---- belief and knowledge (statist: relations do not depend on evidence) ----
def RB(Y, gg):
    return frozenset(v for v in Y if not any(gg[u][v] for u in Y))

def K_K(x, Y, geq, gg):   # K-normality
    return RB(Y, gg) | frozenset(v for v in Y if geq[v][x])

def K_I(x, Y, geq, gg):   # I-normality
    return frozenset(v for v in Y if not gg[x][v])

def K_KM(x, Y, geq, gg):  # KM-normality
    return RB(Y, gg) | frozenset(v for v in Y if any(geq[v][u] and geq[x][u] and not gg[x][u] for u in Y))

def modular(gg):
    n = len(gg)
    # x >> y implies for all z: z >> y or x >> z
    return all(not gg[x][y] or gg[z][y] or gg[x][z] for x in range(n) for y in range(n) for z in range(n))
