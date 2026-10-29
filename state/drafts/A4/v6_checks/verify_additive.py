"""Exact finite checks for the additive normality obstruction.

Uses the existing project's HP implementation, not an independent implementation.
Run from any working directory: python3 verify_additive.py.
"""
from pathlib import Path
import sys, json, itertools
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'source'))
from models import Model, hp_ac2

chain=Model({'C':1},{'I':(('C',),lambda w:w['C']),
                         'Y':(('I',),lambda w:w['I'])},name='Chain')
boulder=Model({'F':1},{'B':(('F',),lambda w:w['F']),
                         'K':(('F',),lambda w:w['F']),
                         'H':(('B','K'),lambda w:w['B'] and not w['K'])},name='Boulder')
door=Model({'M':1,'T':1},{'L':(('M','T'),lambda w:w['M'] and not w['T']),
                              'R':(('M','T'),lambda w:w['M'] and w['T']),
                              'E':(('L','R'),lambda w:w['L'] or w['R'])},name='Doorbells')
prevention=Model({'P':1,'A':1},{'V':(('P','A'),lambda w:w['P'] and not w['A'])},name='Prevention')
short=Model({'A':1},{'P':(('A',),lambda w:w['A']),
                       'V':(('P','A'),lambda w:w['P'] and not w['A'])},name='Short circuit')
locust=Model({'S':1,'Q':0},{'D':(('Q','S'),lambda w:not w['Q'] and not w['S']),
                              'X':(('S','D'),lambda w:w['S'] or w['D'])},name='Locusts')
cases=[(chain,'C','Y'),(boulder,'K','H'),(door,'T','E'),
       (prevention,'A','V'),(short,'A','V'),(locust,'S','X')]

def features(M,w):
    # Coordinates: root-default count, n, l, f, u. All defaults are zero.
    v=[sum(w[x]==0 for x in M.roots),0,0,0,0]
    for x in M.eqs:
        good=w[x]==M.f(x,w)
        cat=(1 if good else 3) if w[x]==0 else (2 if good else 4)
        v[cat]+=1
    return tuple(v)

def difference(M,w):
    return tuple(x-y for x,y in zip(features(M,w),features(M,M.actual)))

def witnesses(M,candidate,e,version):
    phi=lambda w:w[e]==M.actual[e]
    return hp_ac2(M,{k:M.actual[k] for k in candidate},phi,version)

def verdicts(M,c,e,version,weights):
    valid=[]
    for n in range(1,len(M.vars)+1):
        for candidate in itertools.combinations(M.vars,n):
            if any(sum(a*b for a,b in zip(difference(M,w),weights))>=0
                   for _,_,w in witnesses(M,candidate,e,version)):
                valid.append(frozenset(candidate))
    minimal=[x for x in valid if not any(y<x for y in valid)]
    return {'cause':frozenset([c]) in minimal,
            'part':any(c in x for x in minimal),
            'minimal_candidates':[sorted(x) for x in minimal]}

vectors={}
for M,c,e in cases[:3]:
    vs=set(difference(M,w) for _,_,w in witnesses(M,[c],e,'mod'))
    assert len(vs)==1,(M.name,vs)
    vectors[M.name]=list(next(iter(vs)))
assert vectors['Chain']==[1,2,-2,0,0]
assert vectors['Boulder']==[0,-1,0,1,0]
assert vectors['Doorbells']==[1,1,-2,1,0]
assert vectors['Doorbells']==[x+y for x,y in zip(vectors['Chain'],vectors['Boulder'])]

# This sample is supplementary. The displayed coefficient identity proves
# the implication for every real score vector, not just these integer values.
grid=0;calibrated=0
for r in range(1,5):
    for b,c,d in itertools.product(range(-4,5),repeat=3):
        grid+=1
        g1=r-2*b;g2=c;g3=r+c-2*b
        if g1>=0 and g2>=0:
            calibrated+=1;assert g3>=0

# Necessity of the modified-definition restriction: a uniform additive score
# can fit the wider case battery for original/updated HP by using the second
# boulder witness. All candidate sizes, including outcome members, are checked.
weights=(2,0,-1,-5,-3)
counter={}
for version in ['orig','upd','mod']:
    counter[version]={M.name:verdicts(M,c,e,version,weights) for M,c,e in cases}
for version in ['orig','upd']:
    a=counter[version]
    assert all(a[n]['cause'] for n in ['Chain','Boulder','Prevention','Locusts'])
    assert all(not a[n]['part'] for n in ['Doorbells','Short circuit'])
assert not counter['mod']['Boulder']['part']
result={'feature_order':['root_default','n','l','f','u'],
        'modified_singleton_witness_vectors':vectors,
        'identity_exact':True,'integer_score_vectors_checked':grid,
        'integer_score_vectors_meeting_both_calibrations':calibrated,
        'boundary_counterexample_weights':weights,'boundary_verdicts':counter}
(ROOT/'verification-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
