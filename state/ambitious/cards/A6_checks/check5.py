import sys, random
sys.path.insert(0, sys.argv[1])
from structs import *
from check1 import gap, good_struct, CK, binary_experiments
random.seed(7)
n = 5
tot = 0; mism = dict(bel=0, Kglob=0, Iglob=0, KMglob=0, KK=0, Ksuff=0); ksuff_trials = 0
for geq, gg in structures(n, True):
    tot += 1
    m = modular(gg)
    # belief Arrow
    ar = True
    for Y in subsets(n):
        BY = RB(Y, gg)
        for p in subsets(n):
            q = p & Y
            if q and (BY & q) and RB(q, gg) != (BY & q):
                ar = False; break
        if not ar: break
    if ar != m: mism['bel'] += 1
    gK = gI = gKM = True
    for Y in subsets(n):
        for x in Y:
            if gK and not gap(K_K, x, Y, geq, gg): gK = False
            if gI and not gap(K_I, x, Y, geq, gg): gI = False
            if gKM and not gap(K_KM, x, Y, geq, gg): gKM = False
            if m:
                for Kf in (K_K, K_I, K_KM):
                    K0 = Kf(x, Y, geq, gg)
                    if any(not Kf(s, Y, geq, gg) <= K0 for s in K0): mism['KK'] += 1
    # global Good for I/KM also needs time-1 laminarity; under modular it is implied (checked n<=4); here compare gap-global
    if gK != CK(geq, gg): mism['Kglob'] += 1
    if gI != m: mism['Iglob'] += 1
    if gKM != m: mism['KMglob'] += 1
    # sampled sufficiency check for K-normality: gap => good_struct
    if random.random() < 0.05:
        for Y in subsets(n):
            for x in Y:
                if gap(K_K, x, Y, geq, gg):
                    ksuff_trials += 1
                    if not good_struct(K_K, x, Y, geq, gg): mism['Ksuff'] += 1
print("n=5 structures:", tot, "mismatches:", mism, "K sufficiency trials:", ksuff_trials)
