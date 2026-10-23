import sys
sys.path.insert(0, sys.argv[1])
from structs import *
from check1 import good_struct, gap
from checkomega import closure
for total in (True, False):
    for n in ((2, 3, 4) if total else (2, 3)):
        a = b = c = d = 0
        for geq, gg in structures(n, total=total):
            for Y in subsets(n):
                for x in Y:
                    K0 = K_I(x, Y, geq, gg); C = closure(K_I, x, Y, geq, gg)
                    good = good_struct(K_I, x, Y, geq, gg)
                    eq = (K0 == C)
                    if good and not eq: a += 1
                    if eq and not good: b += 1
                    if eq: c += 1
                    d += 1
        print("total" if total else "partial", n, "good&!omega:", a, "omega&!good:", b, "omega-sits:", c, "of", d)
