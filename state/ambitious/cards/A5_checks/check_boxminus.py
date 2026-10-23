# Does every neutral EU guess rule (T_k decreasing, T_k>F_k) that satisfies AS and C violate Box-minus:
#   if K(P) subset of E (E a union of cells), then K(P|E) subset of K(P)?
import itertools, random
from fractions import Fraction as Fr
n=3; cells=range(n)
answers=[frozenset(s) for r in range(1,n+1) for s in itertools.combinations(cells,r)]
def rule(P,T,F):
    best=None
    for G in answers:
        pg=sum(P[c] for c in G); k=len(G)
        v=pg*T[k]+(1-pg)*(F[k] if k<n else 0)
        if best is None or v>best[0] or (v==best[0] and len(G)>len(best[1])): best=(v,G)
    return best[1]
grid=[(Fr(i,40),Fr(j,40),Fr(40-i-j,40)) for i in range(41) for j in range(41-i)]
events=[frozenset(s) for r in range(1,n) for s in itertools.combinations(cells,r)]
random.seed(7); tested=0; allviol=0; examples=[]
for trial in range(300):
    T={3:Fr(0)}; T[2]=Fr(random.randint(1,40),10); T[1]=T[2]+Fr(random.randint(1,40),10)
    F={1:T[1]-Fr(random.randint(1,200),10), 2:T[2]-Fr(random.randint(1,200),10)}
    # AS: believe {0} at (0.99,.005,.005); C: some P with P(a)>1/2 where K != {a}
    if rule((Fr(99,100),Fr(1,200),Fr(1,200)),T,F)!=frozenset([0]): continue
    if all(rule(P,T,F)==frozenset([max(cells,key=lambda c:P[c])]) for P in grid if max(P)>Fr(1,2)): continue
    tested+=1; viol=None
    for P in grid:
        K=rule(P,T,F)
        for E in events:
            pe=sum(P[c] for c in E)
            if pe==0 or not K<=E: continue
            Pc=tuple(P[c]/pe if c in E else Fr(0) for c in cells)
            K2=rule(Pc,T,F)
            if not K2<=K: viol=(P,E,K,K2); break
        if viol: break
    if viol: allviol+=1; 
    if viol and len(examples)<3: examples.append((T,F,viol))
print("rules satisfying AS and C:",tested," with a Box-minus violation:",allviol)
for T,F,(P,E,K,K2) in examples:
    print(" T=",{k:str(v) for k,v in T.items()}," F=",{k:str(v) for k,v in F.items()}," P=",[str(x) for x in P],
          " learn E=",sorted(c+1 for c in E)," K before=",sorted(c+1 for c in K)," K after=",sorted(c+1 for c in K2))
