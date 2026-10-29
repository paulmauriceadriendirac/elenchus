"""One-off checks of claims in the independent E3 referee response."""
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import json, random

def frames(n):
    opts=[]
    for w in range(n):
        other=[v for v in range(n) if v!=w]
        opts.append([(w,)+p for k in range(n) for s in combinations(other,k) for p in permutations(s)])
    yield from product(*opts)

def flat(fr):
    n=len(fr)
    subsets=[{i for i in range(n) if mask>>i&1} for mask in range(1<<n)]
    def pick(w,X):
        return None if w is None else next((x for x in fr[w] if x in X),None)
    return all(pick(pick(w,Y),X)==pick(w,X)
               for w in range(n) for X in subsets for Y in subsets if X<=Y)

A=('atom',0); B=('atom',1)
N=lambda p:('not',p)
I=lambda p,q:('if',p,q)
O=lambda p,q:('or',p,q)
C=lambda p,q:('and',p,q)
X=O(A,B)
forms=[A,B,N(A),O(A,B),I(A,B),I(B,A),I(X,B),I(X,I(A,B)),I(B,I(A,B)),
       I(B,I(A,N(B))),I(A,I(A,B)),I(I(A,B),I(B,A)),I(N(I(A,B)),O(A,I(B,A))),
       I(X,I(A,I(B,N(A)))),C(I(A,B),N(I(B,A))),I(X,C(A,I(B,N(A))))]

def evaluators(fr,val):
    @lru_cache(None)
    def ev(w,p):
        op=p[0]
        if op=='atom': return bool(val[p[1]]>>w&1)
        if op=='not': return not ev(w,p[1])
        if op=='and': return ev(w,p[1]) and ev(w,p[2])
        if op=='or': return ev(w,p[1]) or ev(w,p[2])
        v=next((v for v in fr[w] if ev(v,p[1])),None)
        return v is None or ev(v,p[2])
    @lru_cache(None)
    def reset(b,i,p):
        w=fr[b][i];op=p[0]
        if op=='atom': return bool(val[p[1]]>>w&1)
        if op=='not': return not reset(b,i,p[1])
        if op=='and': return reset(b,i,p[1]) and reset(b,i,p[2])
        if op=='or': return reset(b,i,p[1]) or reset(b,i,p[2])
        # R: jump to the head of w's own linear sequence, then apply ordinary >.
        j=next((j for j in range(len(fr[w])) if reset(w,j,p[1])),None)
        return j is None or reset(w,j,p[2])
    return ev,reset

rng=random.Random(28102026)
cases=[(fr,True) for n in range(1,4) for fr in frames(n)]
for n in (4,5):
    for _ in range(100):
        fr=[]
        for w in range(n):
            others=[v for v in range(n) if v!=w];rng.shuffle(others)
            fr.append((w,*others[:rng.randrange(n)]))
        cases.append((tuple(fr),False))

counts={'all_frames_n_le_3':130,'sampled_frames_n4_n5':200,'reset_comparisons':0,
        'flat_frame_valuation_world_checks':0,'reciprocity_checks':0,'failures':0}
for fr,exhaustive in cases:
    n=len(fr);isflat=flat(fr)
    vals=list(product(range(1<<n),repeat=2)) if exhaustive else [(rng.randrange(1<<n),rng.randrange(1<<n)) for _ in range(8)]
    for val in vals:
        ev,reset=evaluators(fr,val)
        for b,row in enumerate(fr):
            for i,w in enumerate(row):
                for p in forms:
                    assert ev(w,p)==reset(b,i,p)
                    counts['reset_comparisons']+=1
        for w in range(n):
            if ev(w,I(X,B)):
                assert ev(w,I(X,I(A,B)))==ev(w,I(B,I(A,B)))
                counts['reciprocity_checks']+=1
            if isflat:
                if ev(w,I(X,B)) and ev(w,I(A,N(B))):
                    assert ev(w,I(B,I(A,N(B))))
                assert not (ev(w,I(X,B)) and ev(w,I(B,I(A,B))) and not ev(w,I(A,B)))
                counts['flat_frame_valuation_world_checks']+=1

worlds=[(0,0),(0,1),(1,0),(1,1)]
def model(avoid=False):
    def cost(w,v): return 2*abs(w[0]-v[0])+abs(w[1]-v[1])+(10 if avoid and v==(1,1) else 0)
    return tuple(tuple([k]+sorted([i for i in range(4) if i!=k],key=lambda i:(cost(w,worlds[i]),i))) for k,w in enumerate(worlds))
tables={}
for name,fr in [('Reunion',model()),('Avoidance',model(True))]:
    ev,reset=evaluators(fr,(12,10))
    tables[name]={'orders':fr,'flat':flat(fr),'selection':ev(0,I(X,B)),
                 'unnested':ev(0,I(A,B)),'nested_disjunction':ev(0,I(X,I(A,B))),
                 'nested_atomic':ev(0,I(B,I(A,B))),
                 'contraction':ev(0,I(A,I(A,B)))}
assert tables['Reunion']['nested_atomic'] and not tables['Avoidance']['nested_atomic']

def solve(do):
    s=do.get('S',0);d=do.get('D',0)
    l=do.get('L',d);a=do.get('A',d);b=do.get('B',s*(1-l))
    return {'S':s,'D':d,'L':l,'A':a,'B':b}
policies={'sitter_then_attendance':solve({'S':1,'A':1}),
          'sitter_then_decision':solve({'S':1,'D':1}),
          'attendance_clamped_then_decision':solve({'B':1,'D':1})}
assert [policies[k]['B'] for k in policies]==[1,0,1]

# All acyclic deterministic Boolean models on A,B with an oriented edge or none.
intervention_models=0
for orientation in (0,1):
    for root in (0,1):
        for truth in product((0,1),repeat=2):
            def two(do):
                if orientation==0:
                    a=do.get('A',root); b=do.get('B',truth[a])
                else:
                    b=do.get('B',root); a=do.get('A',truth[b])
                return a,b
            rhs=two({'A':1})[1]==1
            lhs=all(two({**outer,'A':1})[1]==1 for outer in ({'A':1},{'B':1},{'A':1,'B':1}))
            assert lhs==rhs
            intervention_models+=1

out={'checks':counts,'models':tables,'realization_policies':policies,
     'two_variable_intervention_models':intervention_models,
     'scope':'Finite checks support the written proofs; no speaker data or novelty certification.'}
dest=Path(__file__).resolve().parent.parent/'verification.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
