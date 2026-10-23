# Find (K-normality, statist, comparable) cases where the conditional rule CEU strictly prefers
# acting now to looking although there is no relative defeat (so unconditional KDT respects Good).
import sys, random
sys.path.insert(0, sys.argv[1])
from structs import structures, subsets
from kdt import *
from check_collapse import rel_defeat
random.seed(7)
found = 0
for geq_m, gg_m in structures(4, True):
    geq = lambda a, b, g=geq_m: g[a][b]
    gg = lambda a, b, g=gg_m: g[a][b]
    rel = lambda F, r=(geq, gg): r
    for E in subsets(4):
        if len(E) < 2: continue
        for x in E:
            for cells in partitions(E):
                if rel_defeat(ken_K, x, E, cells, rel): continue
                for t in range(40):
                    P = {s: random.random() + 0.05 for s in range(4)}
                    acts = [{s: random.uniform(-5, 5) for s in range(4)} for _ in range(3)]
                    plan, ch, post = look_plan(ken_K, E, cells, rel, acts, P)
                    for i, a in enumerate(acts):
                        D, CK, m = ceu_prefers_act_over_look(x, E, plan, a, P,
                                       lambda D: cond_ken(x, E, D, (geq, gg), (geq, gg)))
                        if m > 1e-6:
                            found += 1
                            if found <= 2:
                                K0 = ken_K(x, E, rel)
                                print('geq', [[int(v) for v in r] for r in geq_m], 'gg', [[int(v) for v in r] for r in gg_m])
                                print(' E', sorted(E), 'x', x, 'K(x)', sorted(K0), 'cells', [sorted(c) for c in cells])
                                print(' post kens', {s: sorted(post[s]) for s in post}, 'choices', ch)
                                print(' P', {k: round(v, 3) for k, v in P.items()})
                                print(' acts', [{k: round(v, 2) for k, v in a_.items()} for a_ in acts])
                                print(' compared act', i, 'D', sorted(D), 'CK', sorted(CK), 'margin', round(m, 3),
                                      'KDT value', round(kdt_value(ken_K, x, E, cells, rel, acts, P), 3))
print('found', found)
