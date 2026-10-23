"""Targeted mathematical checks; not a proof or novelty test."""
from fractions import Fraction as F
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
import json

rows=[]
for alpha in [-.9,-.75,-.51,-.5,-.49,0,1,2]:
    def lb(q):
        if q==0:return 0.
        return quad(lambda t:(1-t)**(alpha-1),0,q,weight='alg',wvar=(alpha,0),epsabs=1e-10)[0]
    for p in [.1,.2,.35,.5,.65,.8,.9]:
        la=lambda q:lb(1-q)
        root=brentq(lambda q:p*la(q)-(1-p)*lb(q),1e-6,1-1e-6,xtol=1e-12)
        H=p*la(p)+(1-p)*lb(p)
        def worst(q):
            A=p*la(q);B=(1-p)*lb(q)
            return max(0,A,B,A+B-H)
        opt=minimize_scalar(worst,bounds=(1e-6,1-1e-6),method='bounded',options={'xatol':1e-12})
        assert abs(root-opt.x)<1e-6,(alpha,p,root,opt.x)
        if p==.5 or alpha==-.5:assert abs(root-p)<1e-9
        elif alpha>-.5:assert min(.5,p)<root<max(.5,p)
        else:assert (root-p)*(p-.5)>0
        rows.append({'alpha':alpha,'prior':p,'equalizer':root,'direct_optimizer':float(opt.x)})

# Independent enumeration of the two pure policies and all four protocols.
for p in [F(i,10) for i in range(1,10)]:
    for c in [F(i,10) for i in range(1,10)]:
        A=p*(1-c);B=(1-p)*c;x=A/(A+B)
        def raw_regrets(z):
            out=[]
            for ra,rb in [(0,0),(1,1),(1,0),(0,1)]:
                # ra/rb indicate silence. Disclosure produces the correct act.
                payoff=p*(1-c)*(1-ra+ra*z)-(1-p)*c*rb*z
                oracle=p*(1-c)*(1-ra)+max(p*ra*(1-c)-(1-p)*rb*c,0)
                out.append(oracle-payoff)
            return out
        assert max(raw_regrets(x))==A*B/(A+B)
        for z in [F(i,100) for i in range(101)]:
            assert max(raw_regrets(z))>=max(raw_regrets(x))
        assert max(raw_regrets(F(1)))<=max(raw_regrets(F(0))) if p>=c else max(raw_regrets(F(1)))>max(raw_regrets(F(0)))
        posterior=p*B/(p*B+(1-p)*A)
        assert posterior==c
result={'proper_loss_cases_checked':len(rows),'bet_cases_checked_exactly':81,'loss_results':rows,'status':'passed'}
print(json.dumps(result,indent=2))
