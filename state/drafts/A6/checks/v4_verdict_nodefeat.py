# Find a smallest, clearest case where the verdict-conditioned rule (VER) prefers acting now to a free
# question although there is no relative defeat (so KDT gives the question non-negative value).
import random, sys, io, contextlib
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from structs import structures, K_K
with contextlib.redirect_stdout(io.StringIO()):
    from v4_conditional_rules import partitions, values, rel_defeat_witnesses, Kc
random.seed(3)
best = None
for nst in (3, 4):
    for geq, gg in structures(nst, total=True):
        E = frozenset(range(nst))
        for x in E:
            for Pi in ([frozenset(c) for c in p] for p in partitions(E) if len(p) > 1):
                if rel_defeat_witnesses(E, x, Pi, geq, gg): continue
                for _ in range(300):
                    P = {s: 1.0 / nst for s in E}
                    acts = [{s: random.choice(range(-3, 4)) for s in E} for _ in range(3)]
                    v = values(acts, E, x, Pi, geq, gg, P)
                    if v['ver'] < -1e-9 and (best is None or v['ver'] < best[0]):
                        best = (v['ver'], nst, geq, gg, x, Pi, acts, v)
    if best: break
ver, nst, geq, gg, x, Pi, acts, v = best
E = frozenset(range(nst))
print('states', nst, 'uniform prior; x =', x)
print('geq (row >= col):', [[int(b) for b in r] for r in geq])
print('gg  (row >> col):', [[int(b) for b in r] for r in gg])
print('question:', [sorted(c) for c in Pi])
print('acts:', [[a[s] for s in range(nst)] for a in acts])
print('ken K(x):', sorted(v['K']), '; act now:', v['a_now'], '; look policy:', v['alpha'])
for b in set(v['alpha'].values()):
    Db = frozenset(s for s in E if v['alpha'][s] == b)
    print('  hypothesis look->%d:' % b, sorted(Db), ' conditional ken:', sorted(Kc(Db, E, x, geq, gg)))
print('KDT %.4f  CEU %.4f  VER %.4f  ANS %.4f' % (v['kdt'], v['ceu'], v['ver'], v['ans']))

# Tie-free version used in the essay. States 0=a, 3=x, 1=b, 2=c (a > x > b > c; a >> all others; x >> c only).
P = {s: .25 for s in E}
A1 = {0: -2, 3: 3.1, 1: -2, 2: 2.1}
A2 = {0: 3, 3: 3, 1: 3, 2: -3}
v = values([A1, A2], E, 3, [frozenset([3]), frozenset([1, 2]), frozenset([0])], geq, gg, P)
print('essay version: ken', sorted(v['K']), 'act now', v['a_now'], 'look policy', v['alpha'],
      'relative defeat:', bool(rel_defeat_witnesses(E, 3, [frozenset([3]), frozenset([1, 2]), frozenset([0])], geq, gg)))
print('  KDT %.4f  CEU %.4f  VER %.4f  ANS %.4f' % (v['kdt'], v['ceu'], v['ver'], v['ans']))
