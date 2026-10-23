import sys
sys.path.insert(0, sys.argv[1])
from structs import *
from check1 import good_struct, gap

def closure(Kfun, x, Y, geq, gg):
    C = {x}; frontier = [x]
    while frontier:
        s = frontier.pop()
        for v in Kfun(s, Y, geq, gg):
            if v not in C:
                C.add(v); frontier.append(v)
    return frozenset(C)

def KomegaI(x, Y, geq, gg): return closure(K_I, x, Y, geq, gg)
def KomegaK(x, Y, geq, gg): return closure(K_K, x, Y, geq, gg)
def KomegaKM(x, Y, geq, gg): return closure(K_KM, x, Y, geq, gg)

def gapped_sets_containing(x, Y, gg):
    Ys = sorted(Y)
    out = []
    for m in range(1, 1 << len(Ys)):
        M = frozenset(Ys[i] for i in range(len(Ys)) if m >> i & 1)
        if x in M and all(gg[a][b] for a in M for b in Y - M):
            out.append(M)
    return out

for total in (True, False):
    for n in (range(1, 5) if total else range(1, 4)):
        st = dict(structs=0, sit=0, omegaI_not_gapped=0, omegaI_not_smallest=0, omegaI_noRB=0,
                  omegaI_good_fail=0, omegaKM_good_fail=0, omegaK_good_fail=0, K_good_fail=0)
        for geq, gg in structures(n, total=total):
            st['structs'] += 1
            for Y in subsets(n):
                for x in Y:
                    st['sit'] += 1
                    C = KomegaI(x, Y, geq, gg)
                    G = gapped_sets_containing(x, Y, gg)
                    if C not in G: st['omegaI_not_gapped'] += 1
                    if G and min(G, key=len) != C or any(not C <= M for M in G): st['omegaI_not_smallest'] += 1
                    if not RB(Y, gg) <= C: st['omegaI_noRB'] += 1
                    if not good_struct(KomegaI, x, Y, geq, gg): st['omegaI_good_fail'] += 1
                    if not good_struct(KomegaKM, x, Y, geq, gg): st['omegaKM_good_fail'] += 1
                    if not good_struct(KomegaK, x, Y, geq, gg): st['omegaK_good_fail'] += 1
                    if not good_struct(K_K, x, Y, geq, gg): st['K_good_fail'] += 1
        print("total" if total else "partial", n, st)
