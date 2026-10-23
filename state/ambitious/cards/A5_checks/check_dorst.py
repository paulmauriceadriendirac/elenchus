# Dorst 2019 Prop 5 claims: with belief-dependent (holistic) accuracy, given Sequence-Irrelevance, there are
# belief-independent T_p,F_p (hence credence-independent thresholds tau_p) with: p in B => C(p)>=tau_p,
# p notin B => C(p)<=tau_p for every rational B.  Counter-measure ("perfect-record bonus"):
#   A(B,w) = sum_{p in B} (T if w in p else -F) + beta*[w in cap B]
# Adding a true p raises A by exactly T; adding a false p lowers it by F or F+beta (Dorst's (ii),(iii) hold).
# Search for p, C, C' with C(p)<C'(p), p in ALL optimal B under C, p in NO optimal B under C'.
import itertools, random
from fractions import Fraction as Fr
n=3; S=range(n)
props=[frozenset(c) for r in range(1,n+1) for c in itertools.combinations(S,r)]  # nonempty
T=Fr(1); F=Fr(2); beta=Fr(3)
allB=[frozenset(x for x,b in zip(props,bits) if b) for bits in itertools.product([0,1],repeat=len(props))]
def ev(B,C):
    sep=sum((sum(C[s] for s in p))*T-(1-sum(C[s] for s in p))*F for p in B)
    cap=frozenset(S)
    for p in B: cap&=p
    return sep+beta*sum(C[s] for s in cap)
def optimal(C):
    vals=[(ev(B,C),B) for B in allB]; m=max(v for v,_ in vals)
    return [B for v,B in vals if v==m]
random.seed(3); grid=[]
for i in range(0,41):
    for j in range(0,41-i):
        grid.append((Fr(i,40),Fr(j,40),Fr(40-i-j,40)))
res={}
for C in grid:
    opts=optimal(C)
    for p in props:
        inall=all(p in B for B in opts); innone=all(p not in B for B in opts)
        res.setdefault(p,[]).append((sum(C[s] for s in p),inall,innone,C))
found=0
for p,L in res.items():
    believed=[x for x in L if x[1]]; not_bel=[x for x in L if x[2]]
    if not believed or not not_bel: continue
    lo=min(believed,key=lambda x:x[0]); hi=max(not_bel,key=lambda x:x[0])
    if lo[0]<hi[0]:
        found+=1
        print("p=",sorted(s+1 for s in p)," believed (all optima) at C=",[str(c) for c in lo[3]],"C(p)=",lo[0],
              "| NOT believed (all optima) at C'=",[str(c) for c in hi[3]],"C'(p)=",hi[0])
        print("   optima at C:",[sorted(sorted(s+1 for s in q) for q in B) for B in optimal(lo[3])])
        print("   optima at C':",[sorted(sorted(s+1 for s in q) for q in B) for B in optimal(hi[3])])
print("propositions with monotonicity violations:",found)
