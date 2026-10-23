# Independence models for A5-01 on a 3-cell question (cells a,b,c = 0,1,2), exact rationals.
import itertools
from fractions import Fraction as Fr
cells=[0,1,2]; W=frozenset(cells)
answers=[frozenset(s) for r in range(1,4) for s in itertools.combinations(cells,r)]
N=120
grid=[(Fr(i,N),Fr(j,N),Fr(N-i-j,N)) for i in range(N+1) for j in range(N+1-i)]
def eu_rule(T,F):
    def K(P):
        best=None
        for G in answers:
            pg=sum(P[c] for c in G); v=pg*T[G]+(1-pg)*F.get(G,0)
            # ties: prefer filtered (top) sets, then larger
            key=(v, min(P[c] for c in G)>=max([P[c] for c in cells if c not in G] or [0]), len(G))
            if best is None or key>best[0]: best=(key,G)
        return best[1]
    return K
def hpd(t):
    return lambda P: frozenset(i for i in cells if sum(P[j] for j in cells if P[j]>P[i]) < t)
def props(K):
    F_ok=all(all(P[i]>=P[j] for i in K(P) for j in cells if j not in K(P)) for P in grid)
    # S: K(P)={a} (or any A with >=2 excluded cells) invariant under redistribution keeping excluded below A
    S_ok=True
    for P in grid:
        A=K(P); out=[c for c in cells if c not in A]
        if len(out)<2: continue
        m=out[0]+0; mass=P[out[0]]+P[out[1]]; mnA=min(P[c] for c in A)
        for k in range(0,N+1):
            y=mass*Fr(k,N); Q=list(P); Q[out[0]]=y; Q[out[1]]=mass-y
            if max(Q[out[0]],Q[out[1]])>=mnA: continue
            if K(tuple(Q))!=A: S_ok=False; break
        if not S_ok: break
    AS_ok=all(K((x,(1-x)/2,(1-x)/2))==frozenset([0]) for x in [Fr(99,100),Fr(999,1000)])
    C_ok=any(K(P)!=frozenset([0]) for P in grid if P[0]>Fr(1,2) and P[0]==max(P))
    return dict(F=F_ok,S=S_ok,AS=AS_ok,C=C_ok)
A=frozenset([0]); B=frozenset([1]); Cc=frozenset([2])
def neutral(T1,T2,T3,F1,F2):
    T={G:{1:T1,2:T2,3:T3}[len(G)] for G in answers}; F={G:{1:F1,2:F2}[len(G)] for G in answers if len(G)<3}
    return T,F
models={
 "drop S (neutral EU: T=(1,.6,.5),F=0)": eu_rule(*neutral(Fr(1),Fr(3,5),Fr(1,2),Fr(0),Fr(0))),
 "drop EU (Goodman-Salow HPD t=.9)": hpd(Fr(9,10)),
 "drop AS (top-two-or-nothing EU)": eu_rule(*neutral(Fr(1),Fr(1),Fr(0),Fr(-9),Fr(-9))),
 "drop C (best-guess-like EU: T=(1,.5,.4),F=0)": eu_rule(*neutral(Fr(1),Fr(1,2),Fr(2,5),Fr(0),Fr(0))),
 "drop truth-dir. (T_ab=F_ab=.6 > T_W=.5; T_a=1,F_a=-4)": eu_rule(*neutral(Fr(1),Fr(3,5),Fr(1,2),Fr(-4),Fr(3,5))),
 "drop informativity (T_ab=.4 < T_W=.5; T_a=1,F_a=-4)": eu_rule(*neutral(Fr(1),Fr(2,5),Fr(1,2),Fr(-4),Fr(-9))),
}
for name,K in models.items():
    print(name, props(K))
