# Tie-free case used in the essay: the verdict-conditioned rule (VER) prefers acting now to a free question
# although there is no relative defeat and KDT values the question positively.
# States a, x, b, c with a > x > b > c; a >> x, b, c; x >> c; nothing else. Uniform prior. Situation x.
import sys, io, contextlib
sys.path.insert(0, __file__.rsplit('/', 1)[0])
with contextlib.redirect_stdout(io.StringIO()):
    from v4_conditional_rules import values, rel_defeat_witnesses, Kc
from structs import K_K
names = ['a', 'x', 'b', 'c']; rank = [0, 1, 2, 3]
geq = [[rank[i] <= rank[j] for j in range(4)] for i in range(4)]
gg = [[False] * 4 for _ in range(4)]
for j in (1, 2, 3): gg[0][j] = True
gg[1][3] = True
E = frozenset(range(4)); P = {s: .25 for s in E}; x = 1
Pi = [frozenset([1]), frozenset([2, 3]), frozenset([0])]
A1 = {0: -2, 1: 3.1, 2: -2, 3: 2.1}
A2 = {0: 3, 1: 3, 2: 3, 3: -3}
v = values([A1, A2], E, x, Pi, geq, gg, P)
print('ken', [names[s] for s in sorted(v['K'])], '; act now A%d' % (v['a_now'] + 1),
      '; look policy', {names[s]: 'A%d' % (b + 1) for s, b in v['alpha'].items()},
      '; relative defeat:', bool(rel_defeat_witnesses(E, x, Pi, geq, gg)))
D = frozenset(s for s in E if v['alpha'][s] == 0)
print('conditional ken on "I would choose A1":', [names[s] for s in sorted(Kc(D, E, x, geq, gg))])
print('KDT %.4f  CEU %.4f  VER %.4f  ANS %.4f' % (v['kdt'], v['ceu'], v['ver'], v['ans']))
