# Theorem check for A5-01: rule K = HPD(t) (Goodman-Salow) on 3 cells.
# For each eps, take the proof's critical credence points near P(a)=t and ask z3 (exact LRA) for the
# minimal "steepness" S = T_a - F_a such that an extensional, truth-directed (T_G - F_G >= 1),
# informative (T_ab - T_W >= 1, T_ac - T_W >= 1) utility makes K EU-optimal at those points.
# Theorem predicts min S -> infinity as eps -> 0 (so no fixed utility works for the continuum).
import z3, itertools
from fractions import Fraction as Fr
cells=[0,1,2]
answers=[frozenset(s) for r in range(1,4) for s in itertools.combinations(cells,r)]
def hpd(P,t):
    return frozenset(i for i in cells if sum(P[j] for j in cells if P[j]>P[i]) < t)
def min_steep(t,eps):
    Tv={G:z3.Real('T%s'%''.join(map(str,sorted(G)))) for G in answers}
    Fv={G:z3.Real('F%s'%''.join(map(str,sorted(G)))) for G in answers if len(G)<3}
    opt=z3.Optimize()
    W=frozenset(cells)
    for G in answers:
        if len(G)<3: opt.add(Tv[G]-Fv[G]>=1)
        if len(G)==2: opt.add(Tv[G]-Tv[W]>=1)
    def ev(G,P):
        pg=sum(P[c] for c in G); e=Tv[G]*z3.RealVal(pg)
        if len(G)<3: e=e+Fv[G]*z3.RealVal(1-pg)
        return e
    pts=[]
    # above threshold, residual all on b / all on c / split unevenly (HPD -> {a})
    for x in [t+eps, t+2*eps]:
        pts += [(x,1-x,Fr(0)), (x,Fr(0),1-x), (x,(1-x)*Fr(2,3),(1-x)*Fr(1,3))]
    # below threshold with b slightly above c (HPD -> {a,b}) and c above b (HPD -> {a,c})
    x=t-eps
    pts += [(x,(1-x)/2+eps/4,(1-x)/2-eps/4), (x,(1-x)/2-eps/4,(1-x)/2+eps/4)]
    for P in pts:
        K=hpd(P,t)
        for G in answers:
            if G!=K: opt.add(ev(K,P)>=ev(G,P))
    a=frozenset([0]); h=opt.minimize(Tv[a]-Fv[a])
    r=opt.check()
    if r!=z3.sat: return str(r),None
    v=opt.model().eval(Tv[a]-Fv[a]); return 'sat',v
for t in [Fr(9,10),Fr(3,4)]:
    for eps in [Fr(1,50),Fr(1,200),Fr(1,1000),Fr(1,10000)]:
        print("t=%s eps=%s ->"%(t,eps), min_steep(t,eps))
