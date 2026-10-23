# Q1. In statist, comparable normality structures (all of them, n <= 4 states), with K-normality:
#   (a) how often does unconditional KDT give a free informative question negative value?
#   (b) does the conditional rule CEU (expected-utility analogue of Salow's Conditional Knowledge
#       Dominance) ever strictly prefer acting now to looking?  Two readings of conditional knowledge
#       on D (they coincide under statism up to the x-clause): CK = undominated(E∩D) ∪ {v∈E∩D: v ⪰ x};
#       CB = undominated(E∩D) (conditional belief only).
# Decision problems: random 3-act problems, plus the "ken bet" family (pays 1 on K(x), -L elsewhere).
# Run: python3 -I check_statist_ceu.py <this dir>
import sys, random
sys.path.insert(0, sys.argv[1])
from structs import structures, subsets
from kdt import *

random.seed(20261023)

def run(n, kenname='K', trials=4, total=True):
    ken = KENS[kenname]
    st = dict(sit=0, probs=0, kdt_neg=0, ceuK_dog=0, ceuB_dog=0, sits_kdt_neg=0, sits_ceuK_dog=0)
    examples = []
    for geq_m, gg_m in structures(n, total=total):
        geq = lambda a, b, g=geq_m: g[a][b]
        gg = lambda a, b, g=gg_m: g[a][b]
        rel = lambda F, r=(geq, gg): r
        for E in subsets(n):
            if len(E) < 2: continue
            for x in E:
                st['sit'] += 1
                K0 = ken(x, E, rel)
                neg_here = dog_here = False
                for cells in partitions(E):
                    probs = []
                    for t in range(trials):
                        P = {s: random.random() + 0.05 for s in range(n)}
                        acts = [{s: random.uniform(-5, 5) for s in range(n)} for _ in range(3)]
                        probs.append((P, acts))
                    for L in (2.0, 20.0, 1e4):
                        P = {s: random.random() + 0.05 for s in range(n)}
                        bet = {s: (1.0 if s in K0 else -L) for s in range(n)}
                        probs.append((P, [bet, {s: 0.0 for s in range(n)}]))
                    for P, acts in probs:
                        st['probs'] += 1
                        v = kdt_value(ken, x, E, cells, rel, acts, P)
                        if v < -1e-9:
                            st['kdt_neg'] += 1; neg_here = True
                        plan, _, _ = look_plan(ken, E, cells, rel, acts, P)
                        for a in acts:
                            _, CK, m = ceu_prefers_act_over_look(x, E, plan, a, P,
                                         lambda D: cond_ken(x, E, D, (geq, gg), (geq, gg)))
                            if m > 1e-9:
                                st['ceuK_dog'] += 1; dog_here = True
                                if len(examples) < 3:
                                    examples.append(dict(geq=geq_m, gg=gg_m, E=sorted(E), x=x,
                                        cells=[sorted(c) for c in cells], P=P, acts=acts, a=a, CK=sorted(CK), margin=m))
                            _, CB, mb = ceu_prefers_act_over_look(x, E, plan, a, P,
                                         lambda D: RB(E & D, gg))
                            if mb > 1e-9:
                                st['ceuB_dog'] += 1
                st['sits_kdt_neg'] += neg_here; st['sits_ceuK_dog'] += dog_here
    return st, examples

if __name__ == '__main__':
    for kn in ('K', 'I', 'KM'):
        for n in (2, 3, 4):
            st, ex = run(n, kn, trials=3 if n == 4 else 6)
            print(kn, 'comparable n=%d' % n, st)
            for e in ex[:1]:
                print('   example:', e)
    for kn in ('K', 'KM'):
        for n in (2, 3):
            st, ex = run(n, kn, trials=6, total=False)
            print(kn, 'non-comparable n=%d' % n, st)
            for e in ex[:1]:
                print('   example:', e)
