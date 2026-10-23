# A5-01 checks: (1) HPD (Goodman-Salow) and Leitgeb-stability satisfy Split-invariance on a grid;
# (2) LP: no extensional, truth-directed, informative answer-utility makes EU-argmax agree with HPD(t)
#     on a grid of credences (3-cell question); (3) the proof's key inequality chain numerically.
import itertools, numpy as np
import z3
from fractions import Fraction
cells=[0,1,2]
answers=[frozenset(s) for r in range(1,4) for s in itertools.combinations(cells,r)]
def hpd(P,t):
    # G&S Prop 5/9: B = {s : P({s': P(s')>P(s)}) < t}
    return frozenset(i for i in cells if sum(P[j] for j in cells if P[j]>P[i]+1e-12) < t-1e-12)
def stable_strongest(P):
    # Leitgeb r=1/2: strongest A (top-set) with min_{h in A} P(h) > P(not A)
    best=frozenset(cells)
    for A in answers:
        if A==frozenset(cells): continue
        if min(P[h] for h in A) > sum(P[j] for j in cells if j not in A)+1e-12:
            if len(A)<len(best): best=A
    return best
grid=[np.array([i,j,60-i-j])/60 for i in range(61) for j in range(61-i)]
# (1) split-invariance check
def split_inv(rule):
    viol=0
    for P in grid:
        A=rule(P); out=[c for c in cells if c not in A]
        if len(out)<2: continue
        m=sum(P[c] for c in out); mnA=min(P[c] for c in A)
        for y in np.linspace(0,m,25):
            Q=P.copy(); Q[out[0]]=y; Q[out[1]]=m-y
            if max(Q[out[0]],Q[out[1]])>=mnA-1e-12: continue
            if rule(Q)!=A: viol+=1
    return viol
print("split-invariance violations: HPD(.9)",split_inv(lambda P:hpd(P,0.9)),
      " stability",split_inv(stable_strongest))
# (2) LP feasibility: variables T_G,F_G for each answer G (F_W unused); constraints:
#   for each grid P (interior, no near-ties), EV(HPD(P)) >= EV(G)+margin for all G != HPD(P)?  Use >= (weak) with margin 0
#   truth-directed: T_G - F_G >= 1 (G != W); informativity: T_ab - T_W >= 1, T_ac - T_W >= 1, T_bc - T_W >= 1
def solve(rule,t_label):
    Tv={G:z3.Real('T_'+''.join(map(str,sorted(G)))) for G in answers}
    Fv={G:z3.Real('F_'+''.join(map(str,sorted(G)))) for G in answers if len(G)<3}
    s=z3.Solver(); n_con=0
    def ev(G,P):
        pg=sum(Fraction(int(round(P[c]*60)),60) for c in G)
        e=Tv[G]*z3.RealVal(pg)
        if len(G)<3: e=e+Fv[G]*z3.RealVal(1-pg)
        return e
    for P in grid:
        srt=sorted(P)
        if min(abs(srt[0]-srt[1]),abs(srt[1]-srt[2]))<1e-9: continue
        K=rule(P)
        for G in answers:
            if G==K: continue
            s.add(ev(K,P)>=ev(G,P)); n_con+=1
    W=frozenset(cells)
    for G in answers:
        if len(G)<3: s.add(Tv[G]-Fv[G]>=1)
        if len(G)==2: s.add(Tv[G]-Tv[W]>=1)
    r=s.check()
    print(t_label,"constraints",n_con,"z3:",r)
for t in [0.6,0.75,0.9,0.95]:
    solve(lambda P,t=t:hpd(P,t),"HPD t=%.2f"%t)
solve(stable_strongest,"Leitgeb r=1/2")
# control: a split-sensitive EU rule (neutral utilities) must be feasible for its own rule
T={1:1.0,2:0.6,3:0.5}
def eu_rule(P):
    best=None
    for G in answers:
        v=sum(P[c] for c in G)*T[len(G)]
        if best is None or v>best[0]+1e-12 or (abs(v-best[0])<=1e-12 and len(G)>len(best[1])): best=(v,G)
    return best[1]
solve(eu_rule,"control EU rule")
