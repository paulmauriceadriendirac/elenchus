"""Targeted checks for the new claims, alongside analytic proofs in the essays.
Run from this directory. Dependencies are the archived project scripts beside it.
This checks a finite sample for A5/A6, all 355 four-category preorders for A4.
"""
import sys, json, itertools, random
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).parent/'source/A4'))
import models as m
sys.path.insert(0,str(Path(__file__).parent/'source/A6'))
from structs import preorders, structures, subsets, K_K
from kdt import partitions

def a4():
    orders=list(preorders(4,total=False))
    assert len(orders)==355
    cats=['E00','E10','E01','E11'] # n,l,f,u
    cases={'GP':(m.HB['GP'][0],'A','D'), 'CHAIN':(m.HB['CHAIN'][0],'C','E'),
           'BOULDER':(m.HB['BOULDER'][0],'Dk','H'), 'SC':(m.HB['SC'][0],'A','D'),
           'DOOR':(m.DOOR,'Df','E'), 'LOC':(m.NBP['NBP1'],'Lo','E')}
    data={}
    # All nonempty candidates, including candidates containing the effect.
    # No maximum conjunction size or exclusion of outcome variables is assumed.
    for name,(model,var,effect) in cases.items():
        phi=lambda w,model=model,effect=effect:w[effect]==model.actual[effect]
        for version in ('orig','upd','mod'):
            ws={}
            for xs in m.subsets(model.vars):
                if xs:
                    key=frozenset(xs)
                    ws[key]=[w for _,_,w in m.hp_ac2(model,{v:model.actual[v] for v in xs},phi,version)]
            data[name,version]=ws
    counts={'preorders':len(orders),'calibrations':0,'paired_comparisons':0,'errors':[]}
    for matrix in orders:
        def geq(a,b):
            if a.startswith('R'): return {'R0':1,'R1':0}[a]>={'R0':1,'R1':0}[b]
            return matrix[cats.index(a)][cats.index(b)]
        license=geq('E10','E00') and geq('E00','E10') and geq('E01','E00') and not geq('E11','E00')
        def verdict(name,version,rule,part=True):
            model,var,effect=cases[name]
            defaults=m.coding_defaults(model,rule,var)
            actual={v:m.cat(model,model.actual,v,defaults) for v in model.vars}
            passed=set()
            for xs,worlds in data[name,version].items():
                if any(all(geq(m.cat(model,w,v,defaults),actual[v]) for v in model.vars) for w in worlds):
                    passed.add(xs)
            minimal=[xs for xs in passed if not any(ys<xs for ys in passed)]
            return any((var in xs if part else xs==frozenset([var])) for xs in minimal)
        for ver in ('orig','upd','mod'):
            # In these cases inertial coding equals C1; C2 also gives all-zero defaults.
            for rule in ('C1','C2'):
                got=all(verdict(n,ver,rule,part=False)==v for n,v in [('GP',True),('CHAIN',True),('BOULDER',True),('SC',False)])
                counts['calibrations']+=1
                if got!=license:counts['errors'].append(('T1',matrix,ver,rule))
            for rule in ('C1','C2','C3'):
                pair=('DOOR','LOC') if rule=='C1' else ('LOC','SC')
                counts['paired_comparisons']+=1
                if verdict(pair[0],ver,rule)!=verdict(pair[1],ver,rule):
                    counts['errors'].append(('T2',matrix,ver,rule))
    return counts

def a5():
    rng=random.Random(20261028)
    count=0; brute=0
    for n in (3,4):
        W=(1<<n)-1
        for _ in range(75):
            weights=rng.sample(range(1,60),n)
            p=[F(v,sum(weights)) for v in weights]
            prob=lambda X:sum((p[i] for i in range(n) if X>>i&1),F(0))
            e={X:3*prob(X)-2 for X in range(W+1)}
            h={X:sum((max(v,F(0)) for q,v in e.items() if q&X==X),F(0)) for X in range(W+1)}
            # Include all positive intersections of affine scores plus one point beyond.
            bs={F(1,1000)}
            for X in range(W+1):
                for Y in range(X):
                    if prob(X)!=prob(Y):
                        b=(h[Y]-h[X])/(prob(X)-prob(Y))
                        if b>0:bs.add(b)
            critical=max((h[X]-1)/(1-prob(X)) for X in range(W))
            bs.add(max(critical,F(0))+1)
            orig=sorted(bs)
            bs.update((a+b)/2 for a,b in zip(orig,orig[1:]))
            last=[]
            for beta in sorted(bs):
                phi={X:h[X]+beta*prob(X) for X in range(W+1)}
                best=max(phi.values()); cores=[X for X,v in phi.items() if v==best]
                for X in cores:
                    assert all(not(X>>i&1) or (X>>j&1) or p[j]<=p[i] for i in range(n) for j in range(n))
                    assert all(prob(X)>=prob(Y) and X&Y==Y for Y in last)
                last=cores;count+=1
                if n==3 and beta in (orig[0],orig[-1]):
                    opt=-10**9
                    for mask in range(1<<(W+1)):
                        B=[q for q in range(W+1) if mask>>q&1];core=W
                        for q in B:core&=q
                        value=sum((e[q] for q in B),F(0))+beta*prob(core)
                        opt=max(opt,value)
                    assert opt==best;brute+=1
            assert last==[W]
    return dict(parameter_points=count,full_belief_space_checks=brute,errors=[])

def a6():
    rng=random.Random(20261028)
    count=0;perturbed=0;smallest=None
    for n in (2,3,4):
        for geq,gg in structures(n):
            for E in subsets(n):
                for cells in partitions(E):
                    post={s:K_K(s,next(c for c in cells if s in c),geq,gg) for s in E}
                    for x in E:
                        M=K_K(x,E,geq,gg)
                        bad=[s for s in M if not post[s]<=M]
                        if not bad:continue
                        weights={s:F(rng.randrange(1,20)) for s in E}
                        def eu(a,K):return sum(weights[s]*a[s] for s in K)/sum(weights[s] for s in K)
                        s0=bad[0];ps=weights[s0]/sum(weights[s] for s in M)
                        N=F(3)/ps;eps=F(1,10)
                        qs=[sum(weights[t] for t in F1-M)/sum(weights[t] for t in F1) for F1 in post.values() if F1-M]
                        L=(2+eps*N)/min(qs)
                        beta={s:F(1) if s in M else -L for s in E}
                        acts=[beta,{s:F(0) for s in E},{s:beta[s]+eps*(N if s==s0 else -1) for s in E}]
                        def verify(acts):
                            # Difference events are the entire evidence at every stage.
                            assert all(acts[i][s]!=acts[j][s] for s in E for i in range(3) for j in range(i))
                            assert all(eu(acts[2],M)>eu(a,M) for a in acts[:2])
                            choices={s:max(range(3),key=lambda i:eu(acts[i],post[s])) for s in E}
                            assert 2 not in choices.values()
                            plan={s:acts[choices[s]][s] for s in E}
                            assert all(plan[s]!=acts[2][s] for s in E)
                            margin=eu(acts[2],M)-eu(plan,M)
                            assert margin>0
                            return margin
                        margin=verify(acts);count+=1
                        smallest=margin if smallest is None else min(smallest,margin)
                        if count%17==0:
                            # Explicit small independent payoff perturbations, no renormalization.
                            changed=[{s:a[s]+F(rng.randrange(-10,11),100000) for s in E} for a in acts]
                            verify(changed);perturbed+=1
    return dict(defeat_cases=count,perturbation_checks=perturbed,minimum_margin=str(smallest),errors=[])

if __name__=='__main__':
    out={}
    for name,fn in [('A4',a4),('A5',a5),('A6',a6)]:
        out[name]=fn();print(name,json.dumps(out[name]),flush=True)
        assert not out[name]['errors']
    (Path(__file__).parent/'revision-results.json').write_text(json.dumps(out,indent=2)+'\n')
