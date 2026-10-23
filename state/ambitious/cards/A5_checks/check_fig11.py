import itertools, numpy as np, z3
from fractions import Fraction as Fr
S=[0,1,2,3]; props=[frozenset(c) for r in range(5) for c in itertools.combinations(S,r)]
R=Fr(1); Wv=Fr(8,5); t=Wv/(R+Wv)
fig10={frozenset(x) for x in [(0,1,2),(0,1,3),(0,2,3),(0,1,2,3)]}
fig11=fig10|{frozenset(x) for x in [(0,1),(0,2),(0,3),(1,2,3)]}
def representable(A):
    P=[z3.Real('P%d'%s) for s in S]; sv=z3.Solver(); sv.add([x>=0 for x in P]); sv.add(z3.Sum(P)==1)
    for p in props:
        pp=z3.Sum([P[s] for s in p]) if p else z3.RealVal(0)
        sv.add(pp>=t) if p in A else sv.add(pp<=t)
    return sv.check()==z3.sat
# equal-weight strong coherence by brute force over all 2^16 alternatives
M=np.array([[ (1.0 if s in p else -float(Wv)) for p in props] for s in S])  # 4 x 16 contribution if believed
allB=np.array(list(itertools.product([0,1],repeat=16)),dtype=float)       # 65536 x 16
scores=allB@M.T                                                            # 65536 x 4
def coherent_equal(A):
    a=np.array([1.0 if p in A else 0.0 for p in props]); sa=M@a
    ge=(scores>=sa-1e-12).all(axis=1); gt=(scores>sa+1e-12).any(axis=1)
    return not (ge&gt).any()
for name,A in [('fig10',fig10),('fig11',fig11)]:
    print(name,'representable:',representable(A),' strongly coherent (equal weights):',coherent_equal(A))
# weighted-dominance witness for fig11
A=fig11
lam={p:z3.Real('l%d'%i) for i,p in enumerate(props)}; d=z3.Real('d'); op=z3.Optimize()
op.add([lam[p]>=0 for p in props]); op.add(z3.Sum(list(lam.values()))==1)
g=lambda p,s:(R if s in p else -Wv)
for s in S: op.add(z3.Sum([lam[p]*(g(p,s) if p in A else -g(p,s)) for p in props])<=-d)
op.maximize(d); op.check(); m=op.model()
lv={p:Fr(str(m.eval(lam[p]).as_fraction())) for p in props}
print('witness lambda support:',{tuple(sorted(x+1 for x in p)):str(v) for p,v in lv.items() if v>0},' margin d=',m.eval(d))
