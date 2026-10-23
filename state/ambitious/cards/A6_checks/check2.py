import sys
sys.path.insert(0, sys.argv[1])
from structs import *
from check1 import binary_experiments, gap, good_struct, CK, laminar

def defeat_question(Kfun, x, Y, geq, gg):
    """Return a binary question (cell p containing some k in K(x)) whose discovery
    puts a state outside K(x) into k's knowledge, using the canonical
    construction p = Y minus {u : u >> v}; None if none found."""
    K0 = Kfun(x, Y, geq, gg)
    for v in Y - K0:
        p = frozenset(u for u in Y if not gg[u][v])
        for k in K0 & p:
            if not Kfun(k, Y & p, geq, gg) <= K0:
                return (v, p, k)
    return None

def run(n, total):
    bad = 0; gapfail = 0; checked = 0
    for geq, gg in structures(n, total=total):
        for Y in subsets(n):
            for x in Y:
                for Kf in (K_K, K_I, K_KM):
                    checked += 1
                    if not gap(Kf, x, Y, geq, gg):
                        gapfail += 1
                        if defeat_question(Kf, x, Y, geq, gg) is None:
                            bad += 1
    return checked, gapfail, bad

if __name__ == "__main__":
    for n in range(2, 5):
        print("total", n, run(n, True))
    for n in range(2, 4):
        print("partial", n, run(n, False))
