# E2 v2 formal checks. Framework of Meehan & Zhang 2025 (MZ): finite S, regular prior pi,
# factive learning situations E: S -> subsets containing s; MZ Brier A(c,s) = -sum_{p subset S}(c(p)-v_s(p))^2.
# For a globally evidentially constant (GEC) rule f, weighted total expected accuracy
#   TEA_lam(f) = sum_E lam(E) sum_s pi(s) A(f(E(s)),s) = sum_s pi(s) sum_{p ni s} lam_p(s) A(f(p),s)   (MZ p.345)
import itertools, random
from fractions import Fraction as F
random.seed(7)

def props(n):
    S=range(n); return [frozenset(c) for k in range(1,n+1) for c in itertools.combinations(S,k)]
def factive(n):
    P=props(n); return [dict(zip(range(n),c)) for c in itertools.product(*[[p for p in P if s in p] for s in range(n)])]
def transparent(E):
    return all(E[t]==E[s] for s in E for t in E[s])
def profile(n, weighted):   # weighted: list of (E, weight) -> dict (p,s)->lam_p(s)
    L={}
    for E,w in weighted:
        for s in range(n): L[(E[s],s)]=L.get((E[s],s),0)+w
    return L
def extensional(n,L):
    return all(len({L.get((p,s),0) for s in p})==1 for p in props(n))
def allsubsets(n):
    return [frozenset(c) for k in range(0,n+1) for c in itertools.combinations(range(n),k)]
def brierMZ(c,s,n):  # c: list of state credences
    return -sum((sum(c[t] for t in q)-(1 if s in q else 0))**2 for q in allsubsets(n))
def cond(pi,p): z=sum(pi[t] for t in p); return [pi[t]/z if t in p else 0 for t in range(len(pi))]
def tea(n,pi,L,f):
    return sum(pi[s]*sum(L.get((p,s),0)*brierMZ(f(p),s,n) for p in props(n) if s in p) for s in range(n))
def bell(m):
    Bs=[1]
    from math import comb
    for k in range(m): Bs.append(sum(comb(k,j)*Bs[j] for j in range(k+1)))
    return Bs[m]

print("== C. Fidelity: reproduce MZ Table 2/3 totals (Fact 9 quantity, Dana prior) ==")
n=3; pi=[F(1,5),F(3,5),F(1,5)]
Lfact9={(p,s):1 for p in props(n) for s in p}
b=tea(n,pi,Lfact9,lambda p: cond(pi,p)); d=tea(n,pi,Lfact9,lambda p: pi)
one={frozenset({0,1}):[1,0,0],frozenset({0,1,2}):[0,1,0],frozenset({1,2}):[0,0,1]}
o=tea(n,pi,Lfact9,lambda p: one.get(p,cond(pi,p)))
print(" BCOND",float(b)," dogmatic",float(d)," one-shot",float(o),"  (MZ: -2.72, -4.48, -6.8)")

print("== B. Prop 1: uniform-all profile = 2^{(n-1)^2} x yes/no profile ==")
for n in (3,4):
    Fa=factive(n); La=profile(n,[(E,1) for E in Fa])
    yn=[E for E in Fa if transparent(E) and len(set(E.values()))<=2]
    Ly=profile(n,[(E,1) for E in yn])
    k=2**((n-1)**2)
    print(" n=%d: #factive=%d #yes/no=%d (2^(n-1)=%d); all lam_p(s)=k*yn:"%(n,len(Fa),len(yn),2**(n-1)),
          all(La.get((p,s),0)==k*Ly.get((p,s),0) for p in props(n) for s in range(n)), " yn profile = 1_p:",
          all(Ly.get((p,s),0)==(1 if s in p else 0) for p in props(n) for s in range(n)))
    # exact TEA equality for random GEC rules and priors (n=3 exact)
    if n==3:
        ok=True
        for t in range(30):
            w=[F(random.randint(1,9)) for _ in range(n)]; pi=[x/sum(w) for x in w]
            R={}
            for p in props(n):
                v=[F(random.randint(0,9)) for _ in range(n)]; v[0]+=1; R[p]=[x/sum(v) for x in v]
            ok&= tea(n,pi,La,lambda p:R[p])==k*tea(n,pi,Ly,lambda p:R[p])
        print("  exact TEA_all = k*TEA_yn for 30 random rules/priors:",ok)

print("== D/E. Prop 2-3: opaque-only uniform weighting ==")
for n in (3,4):
    Fa=factive(n); Lo=profile(n,[(E,1) for E in Fa if not transparent(E)])
    k=2**((n-1)**2)
    formula=all(Lo.get((p,s),0)==k-bell(n-len(p)) for p in props(n) for s in p)
    sing=Lo[(frozenset({0}),0)]; co=Lo[(frozenset(range(1,n)),1)]
    print(" n=%d extensional:"%n,extensional(n,Lo)," = 2^{(n-1)^2}-B(n-|p|):",formula,
          " lam_{s}=%d < lam_{S-s}=%d:"%(sing,co), sing<co)
# hull inequality: every partition with block S-{s} has block {s}
for n in (3,4,5):
    ok=True
    for E in factive(n) if n<5 else []:
        if transparent(E):
            blocks=set(E.values())
            for s in range(n):
                if frozenset(set(range(n))-{s}) in blocks and n>1: ok&= frozenset({s}) in blocks
    if n<5: print(" n=%d: every partition with block S-{s} has block {s}:"%n,ok)
for n in (3,4,5,6):  # uniform-all is the 2-colouring mixture of partitions
    cnt={}
    for col in itertools.product((0,1),repeat=n):
        for c in set(col):
            blk=frozenset(i for i in range(n) if col[i]==c); cnt[blk]=cnt.get(blk,0)+F(1,2**n)
    print(" n=%d: random 2-colouring block prob = 2^-(n-1) for every p:"%n, all(cnt.get(p,0)==F(1,2**(n-1)) for p in props(n)))
# cyclic informants
A={0:frozenset({0,1}),1:frozenset({1,2}),2:frozenset({0,2})}; Bc={0:frozenset({0,2}),1:frozenset({0,1}),2:frozenset({1,2})}
Lc=profile(3,[(A,1),(Bc,1)])
print(" cyclic: both opaque:",not transparent(A) and not transparent(Bc)," extensional:",extensional(3,Lc),
      " lam_{2}=%s < lam_{01}=%s"%(Lc.get((frozenset({2}),2),0),Lc.get((frozenset({0,1}),0),0)))

print("== G. Prop 4: proposition-based importance h; product and additive weightings ==")
def H(n,h,s): return sum(h[p] for p in props(n) if s in p)
def weights(n,h,form,dom):
    out=[]
    for E in factive(n):
        if dom=='opq' and transparent(E): continue
        vals=[h[E[s]] for s in range(n)]
        w=1
        if form=='x':
            for v in vals: w*=v
        else: w=sum(vals)
        out.append((E,w))
    return out
def tilted_ok(n,pi,h,L):
    Hs=[H(n,h,s) for s in range(n)]; pt=[pi[s]/Hs[s] for s in range(n)]
    def lamrule(p):
        m=[pi[s]*L.get((p,s),0) for s in range(n)]; z=sum(m); return [x/z for x in m]
    return all(lamrule(p)==cond([x/sum(pt) for x in pt],p) for p in props(n))
for n in (3,4):
    res={'x':[0,0],'+':[0,0]}; agree=True; tilt=True
    trials=25 if n==3 else 6
    for t in range(trials):
        mode=t%3
        if mode==0: h={p:F(random.randint(1,6)) for p in props(n)}                 # generic
        elif mode==1: g={k:F(random.randint(1,6)) for k in range(1,n+1)}; h={p:g[len(p)] for p in props(n)}  # symmetric (balanced)
        else:  # asymmetric balanced (n=3 hand-made; n=4 complement-paired)
            if n==3: h={p:F(1) for p in props(3)}; h[frozenset({0})]=F(3); h[frozenset({1,2})]=F(3)
            else:
                h={}
                for p in props(n):
                    if p in h: continue
                    c=frozenset(set(range(n))-p); v=F(random.randint(1,6))
                    h[p]=v
                    if c: h[c]=v  # importance attaches to questions {p, S-p} -> H constant
                h[frozenset(range(n))]=F(1)
        Hc=len({H(n,h,s) for s in range(n)})==1
        for form in ('x','+'):
            for dom in ('all','opq'):
                L=profile(n,weights(n,h,form,dom))
                ext=extensional(n,L); nonews=len({L[(frozenset(range(n)),s)] for s in range(n)})==1
                agree&= (ext==Hc==nonews); res[form][Hc]+=1
                if form=='x' and dom=='all':
                    w=[F(random.randint(1,9)) for _ in range(n)]; pi=[x/sum(w) for x in w]
                    tilt&=tilted_ok(n,pi,h,L)
    print(" n=%d: extensional <=> H constant <=> No News, all cases:"%n,agree," (balanced/unbalanced cases:",res,")",
          " product-optimal rule = BCOND on pi/H:",tilt)

print("== H. Enough Butter (Dana prior, h({16,17})=5, else 1) ==")
n=3; pi=[F(1,5),F(3,5),F(1,5)]; h={p:F(1) for p in props(3)}; h[frozenset({1,2})]=F(5)
Hs=[H(3,h,s) for s in range(3)]; pt=[pi[s]/Hs[s] for s in range(3)]; pt=[x/sum(pt) for x in pt]
print(" H =",Hs," tilted prior (= rule on learning S):",pt)
for p in props(3):
    if len(p)>1: print("  learn",sorted(15+s for s in p),": optimal",[str(x) for x in cond(pt,p)]," BCOND",[str(x) for x in cond(pi,p)])
L=profile(3,weights(3,h,'x','all'))
tb=tea(3,pi,L,lambda p:cond(pi,p)); tt=tea(3,pi,L,lambda p:cond(pt,p))
print(" weighted TEA (product weighting): BCOND",float(tb)," tilted",float(tt)," tilted better:",tt>tb)
print(" Noah's problem (learn S everywhere): EA prior",float(sum(pi[s]*brierMZ(pi,s,3) for s in range(3))),
      " EA tilted",float(sum(pi[s]*brierMZ(pt,s,3) for s in range(3))))

print("== I. Worst-case aggregation (MZ Brier, Dana prior) ==")
pi=[F(1,5),F(3,5),F(1,5)]
V=lambda f: sum(pi[s]*min(brierMZ(f(p),s,3) for p in props(3) if s in p) for s in range(3))
print(" worst-case EA: BCOND",float(V(lambda p:cond(pi,p)))," dogmatic",float(V(lambda p:pi)))
print(" worst-case problem for BCOND at each state:",[sorted(15+t for t in min((p for p in props(3) if s in p),key=lambda p:brierMZ(cond(pi,p),s,3))) for s in range(3)])
ok=True
for t in range(200):
    w=[F(random.randint(1,9)) for _ in range(3)]; q=[x/sum(w) for x in w]
    R={p:([F(random.randint(1,9)) for _ in range(3)]) for p in props(3)}; R={p:[x/sum(v) for x in v] for p,v in R.items()}
    Vq=sum(q[s]*min(brierMZ(R[p],s,3) for p in props(3) if s in p) for s in range(3))
    Vd=sum(q[s]*min(brierMZ(q,s,3) for p in props(3) if s in p) for s in range(3))
    ok&= Vd>=Vq
print(" dogmatic rule worst-case >= random GEC rules (200 trials):",ok)

print("== J. Further claims in v2 ==")
# Obj 2 example: uniform + extra weight on opaque problem a->{a}, b->{a,b}, c->{c}: No News holds, not extensional
fine={0:frozenset({0}),1:frozenset({0,1}),2:frozenset({2})}
Lj=profile(3,[(E,1) for E in factive(3)]+[(fine,5)])
print(" Obj2: fine opaque:",not transparent(fine)," No News (lam_S const):",len({Lj[(frozenset({0,1,2}),s)] for s in range(3)})==1,
      " extensional:",extensional(3,Lj)," lam_{ab}(a),(b):",Lj[(frozenset({0,1}),0)],Lj[(frozenset({0,1}),1)])
# Obj 3: point mass on Dana's problem violates No News; optimal response to S is certainty in 16
Ed={0:frozenset({0,1}),1:frozenset({0,1,2}),2:frozenset({1,2})}; Ld=profile(3,[(Ed,1)])
print(" Obj3: Dana point mass lam_S by state:",[Ld.get((frozenset({0,1,2}),s),0) for s in range(3)])
# Cyclic profile is a vertex of the extensional polytope: support columns independent
import sympy
M=sympy.Matrix([[1,0,1],[1,1,0],[0,1,1]])  # rows: states 1,2,3; cols: {1,2},{2,3},{1,3}
print(" cyclic support matrix det =",M.det(),"(nonzero -> vertex)")
# Representative-agent identity: META-COND on S x E with prior pi x lam-hat equals Lemma-1 rule pi(.|lam_p)
pi=[F(1,5),F(3,5),F(1,5)]; Fa=factive(3); lam={i:F(random.randint(0,4)) for i in range(len(Fa))}; lam[0]+=1
L=profile(3,[(Fa[i],lam[i]) for i in range(len(Fa))])
ok=True
for p in props(3):
    joint=[sum(pi[s]*lam[i] for i in range(len(Fa)) if Fa[i][s]==p) for s in range(3)]
    if sum(joint)==0: continue
    lem=[pi[s]*L.get((p,s),0) for s in range(3)]
    ok&= [x/sum(joint) for x in joint]==[x/sum(lem) for x in lem]
print(" META-COND for representative agent == Lemma-1 rule (random weighting):",ok)
