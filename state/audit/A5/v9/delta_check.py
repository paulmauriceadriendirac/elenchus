"""A5 v9 delta audit: (1) math-invariance between baseline and v9; (2) recompute numbers in moved/altered passages."""
import re, itertools, sys
from fractions import Fraction as Fr
B='/home/user/elenchus/final/A5/essay.md'
V='/home/user/elenchus/state/external/submission-ready-20261030/A5-Holistic-Accuracy-v9.md'
def maths(path):
    t=open(path,encoding='utf-8').read()
    t=t.split('\n## References')[0] if '\n## References' in t else t
    segs=re.findall(r'\$\$.*?\$\$|\$[^$]+\$',t,flags=re.S)
    return [re.sub(r'\s+','',s) for s in segs], t
mb,tb=maths(B); mv,tv=maths(V)
print('math segments baseline/v9:',len(mb),len(mv),'identical sequence:',mb==mv)
if mb!=mv:
    import difflib
    for l in difflib.unified_diff(mb,mv,lineterm='',n=0): print('  ',l)
# theorem/lemma/corollary statements and proofs: compare normalized paragraphs
def blocks(t,pat):
    return [re.sub(r'\s+',' ',m) for m in re.findall(pat,t,flags=re.S)]
for name,pat in [('statements',r'\*\*(?:Theorem|Corollary)[^*]*\*\*.*?(?=\n\n)'),('defs',r'\n\((?:ME|BI|RI|CI)\).*?(?=\n\n)')]:
    print(name,'identical:',blocks(tb,pat)==blocks(tv,pat), len(blocks(tv,pat)))
def appendix(t):
    a=t.split('## Appendix: Proofs')[1]
    return re.sub(r'\s+',' ',a)
print('appendix identical modulo whitespace:',appendix(tb)==appendix(tv))
# (2) record measure brute force
def run(C,T=Fr(1),F=Fr(-2),beta=Fr(3),mean=False):
    n=len(C); W=frozenset(range(n))
    props=[frozenset(s) for k in range(n+1) for s in itertools.combinations(range(n),k)]
    cr={p:sum((C[i] for i in p),Fr(0)) for p in props}
    e={p:cr[p]*T+(1-cr[p])*F for p in props}
    scale=Fr(1,len(props)) if mean else Fr(1)
    def Phi(X): return beta*cr[X]+scale*sum(max(e[p],0) for p in props if X<=p)
    best=max(Phi(X) for X in props); cores=[X for X in props if Phi(X)==best]
    return cores,best,Phi,e,props
C=[Fr(70,100),Fr(15,100),Fr(15,100)]; Cp=[Fr(75,100),Fr(1,100),Fr(24,100)]
# exhaustive over 2^8 states for 3 worlds
def exhaustive(C,T=Fr(1),F=Fr(-2),beta=Fr(3)):
    n=len(C); props=[frozenset(s) for k in range(n+1) for s in itertools.combinations(range(n),k)]
    cr={p:sum((C[i] for i in p),Fr(0)) for p in props}
    res=[]
    for r in range(len(props)+1):
        for B_ in itertools.combinations(props,r):
            core=frozenset(range(n))
            for p in B_: core&=p
            ea=sum(cr[p]*T+(1-cr[p])*F for p in B_)+beta*cr[core]
            res.append((ea,B_))
    res.sort(key=lambda x:-x[0]); return res
for lab,c in [('C',C),("C'",Cp)]:
    r=exhaustive(c); top=r[0][0]
    fmt=lambda B_: sorted(''.join(str(i+1) for i in sorted(p)) or '0' for p in B_)
    print(lab,'opt',float(r[0][0]),fmt(r[0][1]),'#opt',sum(1 for x in r if x[0]==top),'runner-up',float(r[1][0]),fmt(r[1][1]))
# refinement: split w2 of C' into two worlds of 0.005
cores,best,Phi,e,props=run([Fr(75,100),Fr(5,1000),Fr(5,1000),Fr(24,100)])
print("refined C': Phi({w1})=",float(Phi(frozenset([0]))),'Phi({w1,w3})=',float(Phi(frozenset([0,3]))),'best cores',[sorted(x) for x in cores])
cores2,_,_,_,_=run([Fr(70,100),Fr(75,1000),Fr(75,1000),Fr(15,100)])
print('refined C best cores',[sorted(x) for x in cores2])
# 2^(k-1) claim for splitting a credence-zero world: compare separable parts
for k in [1,2,3,4]:
    base=[Fr(75,100),Fr(25,100)]  # world 3 has credence 0, split into k worlds
    c=base+[Fr(0)]*k
    _,_,Phi,e,props=run(c,beta=Fr(0))
    _,_,Phi0,_,_=run(base+[Fr(0)],beta=Fr(0))
    X=frozenset([0]); print('k',k,'sep(Phi) ratio vs k=1:',Phi(X)/Phi0(X),'expected',2**(k-1))
# mean repair with b=3/8: splitting w2 into 2,4,8 equiprobable worlds
for lab,c in [('C',C),("C'",Cp)]:
    for m in [1,2,4,8]:
        cc=[c[0]]+[c[1]/m]*m+[c[2]]
        cores,_,_,_,_=run(cc,beta=Fr(3,8),mean=True)
        print('mean repair',lab,'split w2 into',m,'cores',[sorted(x) for x in cores])
# Theorem 1 interval and 'every positive premium'
for (T,F,b) in [(1,-2,3),(1,-2,Fr(1,10)),(1,-3,10),(Fr(1,2),-1,Fr(1,100))]:
    T,F,b=Fr(T),Fr(F),Fr(b); D=T-F; tau=-F/D; c0=(b-T-2*F)/(2*D+b); c1=(b-2*F)/(2*D+b)
    print('T,F,beta',T,F,b,'max(c0,tau)<c1<1:',max(c0,tau)<c1<1)
# two-world threshold (beta-F)/(D+beta)
print('two-world threshold',(3+2)/(3+3))
