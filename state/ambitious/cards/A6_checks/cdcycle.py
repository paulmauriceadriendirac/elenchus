import sys, itertools
sys.path.insert(0, sys.argv[1])
from structs import *

def cd_prefers(B, A, Y, gg):
    # Salow's Conditional Dominance: choose B over A iff B better than A throughout belief on the
    # hypothesis that they differ, where conditional belief = belief after discovering D (statist).
    D = frozenset(s for s in Y if A[s] != B[s])
    if not D: return False
    return all(B[s] > A[s] for s in RB(D, gg))

found = {}
for n in (3, 4):
    for total in (True, False):
        cnt = 0; ex = None
        acts = list(itertools.product(range(3), repeat=n))
        for geq, gg in structures(n, total=total):
            Y = frozenset(range(n))
            # quick prefilter: CD relation among all acts; look for 3-cycles
            for A, B, C in itertools.combinations(acts, 3):
                for X1, X2, X3 in ((A, B, C), (A, C, B)):
                    if cd_prefers(X2, X1, Y, gg) and cd_prefers(X3, X2, Y, gg) and cd_prefers(X1, X3, Y, gg):
                        cnt += 1
                        if ex is None: ex = (geq, gg, X1, X2, X3)
                        break
                if cnt > 0: break
            if cnt > 0: break
        found[(n, total)] = (cnt > 0, ex)
        print(n, "total" if total else "partial", "cycle found:", cnt > 0)
        if ex:
            geq, gg, X1, X2, X3 = ex
            print("  geq:", [[int(v) for v in r] for r in geq])
            print("  gg :", [[int(v) for v in r] for r in gg])
            print("  acts:", X1, X2, X3)
