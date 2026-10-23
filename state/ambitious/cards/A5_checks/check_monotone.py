# Claim: on a question with n>=3 cells, a belief rule of threshold form  p in B(P) iff P(p) >= tau_p
# (tau_p credence-independent, may exceed 1 = never), which is closed (filter), consistent and zero-avoiding
# (tau_p > 0), can believe a proposition below certainty only if it is a co-atom W\\{c}, and only one such.
import itertools, z3
def build(n, extra):
    S=range(n); props=[frozenset(c) for r in range(1,n+1) for c in itertools.combinations(S,r)]
    tau={p:z3.Real('t_'+''.join(map(str,sorted(p)))) for p in props}
    P=[z3.Real('P%d'%i) for i in S]
    simplex=z3.And([x>=0 for x in P]+[z3.Sum(P)==1])
    pr=lambda p: z3.Sum([P[i] for i in p])
    bel=lambda p: pr(p)>=tau[p]
    conds=[]
    for p in props:
        for q in props:
            if p<q: conds.append(z3.Implies(bel(p),bel(q)))          # upward closure
            r=p&q
            if p!=q and not (p<=q or q<=p):
                conds.append(z3.Implies(z3.And(bel(p),bel(q)), bel(r) if r else z3.BoolVal(False)))
    s=z3.Solver()
    s.add(z3.ForAll(P, z3.Implies(simplex, z3.And(conds))))
    s.add([tau[p]>0 for p in props])                                   # zero-avoidance
    s.add(extra(props,tau))
    return s
def run(n,label,extra):
    s=build(n,extra); s.set('timeout',600000); r=s.check(); print("n=%d"%n,label,"->",r)
    if r==z3.sat:
        m=s.model(); print("   model:",{''.join(str(i+1) for i in sorted(p)):m.eval(z3.Real('t_'+''.join(map(str,sorted(p))))) for p in [frozenset(c) for k in range(1,n+1) for c in itertools.combinations(range(n),k)]})
W3=frozenset(range(3))
# (1) some non-co-atom, non-W proposition believable below certainty  -> expect unsat
run(3,"non-co-atom below certainty",lambda props,tau: z3.Or([tau[p]<1 for p in props if len(p)<=1]))
# (2) two different co-atoms believable below certainty -> expect unsat
run(3,"two co-atoms below certainty",lambda props,tau: z3.Or([z3.And(tau[p]<1,tau[q]<1) for p in props for q in props if p!=q and len(p)==2 and len(q)==2]))
# (3) one co-atom below certainty -> expect sat
run(3,"one co-atom below certainty",lambda props,tau: tau[frozenset([0,1])]<1)
# (4) same for n=4: non-co-atom (size<=2) below certainty -> expect unsat
run(4,"non-co-atom below certainty",lambda props,tau: z3.Or([tau[p]<1 for p in props if len(p)<=2]))
