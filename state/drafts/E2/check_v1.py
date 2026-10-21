import itertools, random
from fractions import Fraction as F
import numpy as np
W=[0,1,2]; n=3
subsets=[frozenset(s) for k in range(1,n+1) for s in itertools.combinations(W,k)]
def brier(q,w): return sum(((1 if v==w else 0)-q[v])**2 for v in W)
def logs(q,w): return -np.log(q[w]) if q[w]>0 else 1e9
def spher(q,w):
    nrm=np.sqrt(sum(x*x for x in q)); return 1-q[w]/nrm
factive=[dict(zip(W,c)) for c in itertools.product(*[[E for E in subsets if w in E] for w in W])]
allf=[dict(zip(W,c)) for c in itertools.product(*[subsets for w in W])]
print("factive fns",len(factive),"all fns",len(allf))
def lik(lam,fams):
    L={}
    for E in subsets:
        L[E]=[sum(l for l,f in zip(lam,fams) if f[w]==E) for w in W]
    return L
def qrule(p,L):
    R={}
    for E in subsets:
        m=[p[w]*L[E][w] for w in W]; s=sum(m)
        R[E]=[x/s for x in m] if s>0 else None
    return R
def total(p,lam,fams,R,I):
    return sum(l*p[w]*I(R[f[w]],w) for l,f in zip(lam,fams) for w in W if l)
def cond(p):
    return {E:[p[w]/sum(p[v] for v in E) if w in E else 0 for w in W] for E in subsets}
# Thm1 numeric check: random lambda on factive fns, random p; perturbations of q never improve (Brier, spherical, log)
rng=np.random.default_rng(1)
worst=0
for trial in range(200):
    p=rng.dirichlet([1]*3); lam=rng.dirichlet([0.3]*len(factive))
    L=lik(lam,factive); R=qrule(p,L)
    for I in (brier,spher,logs):
        base=total(p,lam,factive,R,I)
        for k in range(20):
            R2={E:(None if R[E] is None else list(np.clip(np.array(R[E])+rng.normal(0,0.05,3),1e-6,None))) for E in subsets}
            R2={E:(None if v is None else [x/sum(v) for x in v]) for E,v in R2.items()}
            worst=min(worst,total(p,lam,factive,R2,I)-base)
print("min improvement over q (should be >= ~0):",worst)
# Corollary: uniform factive -> conditionalization; uniform all -> prior
p=[F(1,5),F(3,10),F(1,2)]
Lf=lik([1]*len(factive),factive); Rf=qrule(p,Lf); print("uniform factive == cond:", all(Rf[E]==cond(p)[E] for E in subsets))
La=lik([1]*len(allf),allf); Ra=qrule(p,La); print("uniform all == prior:", all(Ra[E]==p for E in subsets))
# uniform factive likelihood values
print("uniform factive lik for E=W at each w:", [x/len(factive) for x in Lf[frozenset(W)]])
# Two Instruments example: p uniform; fP: a,b->{a,b}, c->{c}; fN: a->{a}, b->{a,b}, c->{c}
a,b,c=W
fP={a:frozenset({a,b}),b:frozenset({a,b}),c:frozenset({c})}
fN={a:frozenset({a}),b:frozenset({a,b}),c:frozenset({c})}
p=[F(1,3)]*3; lam=[F(1,2),F(1,2)]; fams=[fP,fN]
L=lik(lam,fams); R=qrule(p,L)
print("q({a,b}) =",R[frozenset({a,b})])
C=cond(p)
tq=total(p,lam,fams,R,brier); tc=total(p,lam,fams,C,brier)
print("Two instruments: exp Brier q =",tq," cond =",tc, " diff", tc-tq)
# uniform-weight score of q vs cond in same example? (the MZ standard)
print("MZ-standard (uniform factive): q-rule restricted? cond total=",total(p,[1]*len(factive),factive,C,brier)/len(factive))
# Point mass on fN: Schoenfield
L1=lik([1,0],[fN,fP]); print("point mass fN q({a,b}) =",qrule(p,L1)[frozenset({a,b})])
# cyclic informants
f1={0:frozenset({0,1}),1:frozenset({1,2}),2:frozenset({0,2})}
f2={0:frozenset({0,2}),1:frozenset({0,1}),2:frozenset({1,2})}
Lc=lik([F(1,2),F(1,2)],[f1,f2]); 
print("cyclic lik:", {tuple(sorted(E)):Lc[E] for E in subsets if any(Lc[E])})
p=[F(1,5),F(3,10),F(1,2)]
Rc=qrule(p,Lc); print("cyclic q == cond on reachable E:", all(Rc[E]==cond(p)[E] for E in subsets if any(Lc[E])))
# mixture of partitions: content sufficient?
parts=[[{0},{1},{2}],[{0},{1,2}],[{1},{0,2}],[{2},{0,1}],[{0,1,2}]]
pf=[{w:frozenset(next(B for B in P if w in B)) for w in W} for P in parts]
for t in range(50):
    lam=list(rng.dirichlet([1]*5)); L=lik(lam,pf)
    for E in subsets:
        vals=[L[E][w] for w in E]; assert max(vals)-min(vals)<1e-12
print("mixtures of partitions content-sufficient: ok")
# minimax counterexample
p=[F(1,10),F(9,20),F(9,20)]; C=cond(p)
wc=sum(p[w]*max(brier(C[E],w) for E in subsets if w in E) for w in W)
pr=sum(p[w]*brier(p,w) for w in W)
print("minimax: cond worst-case =",wc,float(wc)," prior-rule worst-case =",pr,float(pr))
print("I(cond{0,1},0)=",brier(C[frozenset({0,1})],0)," I(p,0)=",brier(p,0))
