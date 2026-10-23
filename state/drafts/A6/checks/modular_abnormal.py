# Example: Preservation (diamond-minus) holds globally (statist, comparable, modular >>), yet KDT has
# relative defeat at an abnormal situation.  States a=0 > b=1 > c=2; a>>b, a>>c, not b>>c.
import sys, random
sys.path.insert(0, sys.argv[1])
from kdt import *
from structs import subsets
geq_m = [[True, True, True], [False, True, True], [False, False, True]]
gg_m = [[False, True, True], [False, False, False], [False, False, False]]
geq = lambda a, b: geq_m[a][b]; gg = lambda a, b: gg_m[a][b]
rel = lambda F: (geq, gg)
modular = all(not gg_m[x][y] or gg_m[z][y] or gg_m[x][z] for x in range(3) for y in range(3) for z in range(3))
dm = all(RB(E & p, gg) <= RB(E, gg) for E in subsets(3) for p in subsets(3) if RB(E, gg) & p)
print("modular:", modular, " diamond-minus (Preservation) valid for all E,p:", dm)
E = frozenset([0, 1, 2]); x = 1
print("K(b) =", sorted(ken_K(x, E, rel)), " post-answer ken at b after learning {b,c}:", sorted(ken_K(1, frozenset([1, 2]), rel)))
P = {0: 1.0, 1: 1.0, 2: 1.0}
K0 = ken_K(x, E, rel)
acts = [{s: (1.0 if s in K0 else -10.0) for s in range(3)}, {s: 0.0 for s in range(3)}]
print("KDT value of {a | b,c} at b with a 10:1 ken bet, uniform prior:",
      round(kdt_value(ken_K, x, E, [frozenset([0]), frozenset([1, 2])], rel, acts, P), 3))
