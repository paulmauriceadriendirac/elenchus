#!/usr/bin/env python3
"""Small reproducible checks for the revised essays; not a proof assistant.

Run with Python 3. Uses only the standard library. The essays contain the proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, log
import json

checks = []
def record(name, condition):
    assert condition, name
    checks.append(name)

def poly_a(q):
    return F(1, 2) - 3*q*q + 4*q**3 - F(3, 2)*q**4
def poly_b(q):
    return 2*q**3 - F(3, 2)*q**4

p, q = F(4,5), F(2,3)
record('Brier value and no-disclosure regret at p=4/5',
       2*p*(1-q)**2 == F(8,45) and 2*(q-p)**2 == F(8,225))
record('Polynomial weighted losses at q=2/3',
       p*poly_a(q) == F(2,45) and (1-p)*poly_b(q) == F(8,135))
record('Compressed uniform-subset posterior',
       (F(2,3)*F(1,2))/(F(2,3)*F(1,2)+F(1,3)*F(3,4)) == F(4,7))

losses = {
    'Brier': (lambda q: 2*(1-q)**2, lambda q: 2*q*q),
    'log': (lambda q: -log(q), lambda q: -log(1-q)),
    'boosting': (lambda q: sqrt((1-q)/q), lambda q: sqrt(q/(1-q))),
    'polynomial': (lambda q: float(poly_a(q)), lambda q: float(poly_b(q))),
}
answers = {}
for name, (a,b) in losses.items():
    for p in [.01,.05,.2,.5,.8,.95,.99]:
        lo, hi = 1e-12, 1-1e-12
        for _ in range(70):
            q = (lo+hi)/2
            if p*a(q) > (1-p)*b(q): lo=q
            else: hi=q
        q=(lo+hi)/2
        A,B,H=p*a(q),(1-p)*b(q),p*a(p)+(1-p)*b(p)
        risk=max(A,B,A+B-H)
        record(f'{name} equalizer and inactive N, p={p}',
               abs(A-B)<1e-8 and A+B-H<=max(A,B)+1e-9)
        grid=[i/2000 for i in range(1,2000)]
        record(f'{name} grid comparison, p={p}',
               all(max(p*a(x),(1-p)*b(x),p*a(x)+(1-p)*b(x)-H)>=risk-1e-9 for x in grid))
        if name=='boosting': record(f'boosting preservation, p={p}', abs(q-p)<1e-9)
        if p==.8: answers[name]=q

# Brier randomized-kernel oracle knows alpha,beta but not a random seed.
for p in [.05,.2,.5,.8,.95]:
    q=sqrt(p)/(sqrt(p)+sqrt(1-p))
    bound=2*p*(1-p)/(sqrt(p)+sqrt(1-p))**2
    for alpha,beta in product([i/10 for i in range(11)], repeat=2):
        x,y=p*alpha,(1-p)*beta
        oracle=2*x*y/(x+y) if x+y else 0
        regret=2*x*(1-q)**2+2*y*q*q-oracle
        assert regret<=bound+1e-10
record('Brier randomized-kernel vertex bound on 605 cases', True)

# Weighting representation for every 3-state deterministic factive situation.
n=3
reports=[[P for P in range(1,1<<n) if P & (1<<s)] for s in range(n)]
K=[{P:F(i+1,sum(range(1,len(reports[s])+1))) for i,P in enumerate(reports[s])} for s in range(n)]
weights={E:K[0][E[0]]*K[1][E[1]]*K[2][E[2]] for E in product(*reports)}
record('Kernel-to-weighting total', sum(weights.values())==1)
record('Kernel-to-weighting all marginals', all(sum(w for E,w in weights.items() if E[s]==P)==K[s][P] for s in range(n) for P in reports[s]))

# Cross-pair CAR is not saturated but every image report is whole.
pairs=[{a,b} for a in [0,1] for b in [2,3]]
rho={0:0,1:0,2:1,3:1}
record('Cross-pair row sums', all(sum(F(1,2) for P in pairs if s in P)==1 for s in range(4)))
record('Cross-pair images and non-saturation', all({rho[s] for s in P}=={0,1} and len(P)==2 for P in pairs))

# Exact one-vs-rest imbalance and approximate bound on a nontrivial CAR mixture.
pi=[F(1,10),F(2,10),F(3,10),F(4,10)]
coeff={P:F(1,16) for P in range(1,16)} # half uniform-subset, half partition
for P in [3,12]: coeff[P]+=F(1,2)
for j in range(4):
    A=sum(c for P,c in coeff.items() if P&(1<<j) and P.bit_count()>=2)
    B=sum(c*sum(pi[s] for s in range(4) if s!=j and P&(1<<s))/(1-pi[j]) for P,c in coeff.items() if P&(1<<j) and P.bit_count()>=2)
    partial=sum(c for P,c in coeff.items() if P&(1<<j) and 1<P.bit_count()<4)
    rhs=sum(c*sum(pi[s] for s in range(4) if not P&(1<<s))/(1-pi[j]) for P,c in coeff.items() if P&(1<<j) and 1<P.bit_count()<4)
    record(f'CAR imbalance identity and bound, state={j}', A-B==rhs and partial<=(A-B)*(1-pi[j])/min(pi))

print(json.dumps({'passed':len(checks),'checks':checks,'equalizers_at_p_0_8':answers,
 'scope':'Exact arithmetic examples and finite numerical spot checks; not formal verification or a novelty certificate.'},indent=2))
