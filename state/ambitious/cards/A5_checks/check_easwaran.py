# Easwaran 2016 App. G "Main Conjecture": if doxastic state A is strongly coherent for every positive
# weighting, then A is represented by a probability function (P(p)>t => p in A; P(p)<t => p notin A),
# t = W/(R+W).  Claimed proof: if A is not representable, minimax gives lambda>=0 with
# sum_p lambda_p h_p(s) < 0 for all s, where h_p = (R*1_p - W*1_notp) if p in A else -(R*1_p - W*1_notp);
# flipping supp(lambda) then strictly dominates A under weights lambda (positive elsewhere).
import itertools, random, z3
from fractions import Fraction as Fr
def run(n,R,Wv,states):
    S=list(range(n)); props=[frozenset(c) for r in range(n+1) for c in itertools.combinations(S,r)]
    t=Fr(Wv)/(R+Wv)
    def g(p,s): return R if s in p else -Wv          # gain of believing p over not, at s
    stats={'rep':0,'nonrep':0,'witness_ok':0,'witness_fail':0}
    for A in states:
        # representability LP
        P=[z3.Real('P%d'%s) for s in S]; sv=z3.Solver()
        sv.add([x>=0 for x in P]); sv.add(z3.Sum(P)==1)
        for p in props:
            pp=z3.Sum([P[s] for s in p]) if p else z3.RealVal(0)
            sv.add(pp>=t) if p in A else sv.add(pp<=t)
        rep = sv.check()==z3.sat
        if rep: stats['rep']+=1; continue
        stats['nonrep']+=1
        # find lambda: lambda>=0, sum=1, sum_p lambda_p h_p(s) <= -d for all s, maximize d
        lam={p:z3.Real('l%d'%i) for i,p in enumerate(props)}; d=z3.Real('d'); op=z3.Optimize()
        op.add([lam[p]>=0 for p in props]); op.add(z3.Sum(list(lam.values()))==1)
        for s in S:
            op.add(z3.Sum([lam[p]*(g(p,s) if p in A else -g(p,s)) for p in props])<=-d)
        op.maximize(d)
        assert op.check()==z3.sat
        m=op.model(); dv=m.eval(d)
        lv={p:Fr(str(m.eval(lam[p]).as_fraction())) for p in props}
        assert Fr(str(dv.as_fraction()))>0, "minimax failed to give strict lambda"
        # construct weights and flipped state B, verify strict dominance
        w={p:(lv[p] if lv[p]>0 else Fr(1)) for p in props}
        Bst=set(A)
        for p in props:
            if lv[p]>0: Bst ^= {p}
        def score(X,s): return sum(w[p]*(R if s in p else -Wv) for p in X)
        ok=all(score(Bst,s)>score(A,s) for s in S)
        stats['witness_ok' if ok else 'witness_fail']+=1
    return stats
S3=list(range(3)); props3=[frozenset(c) for r in range(4) for c in itertools.combinations(S3,r)]
all3=[frozenset(x for x,b in zip(props3,bits) if b) for bits in itertools.product([0,1],repeat=len(props3))]
for Wv in [Fr(6,5),Fr(3,2),Fr(2),Fr(3)]:
    print("n=3 W/R=%s"%Wv, run(3,Fr(1),Wv,all3))
random.seed(1)
S4=list(range(4)); props4=[frozenset(c) for r in range(5) for c in itertools.combinations(S4,r)]
sample4=[frozenset(p for p in props4 if random.random()<random.choice([0.3,0.5,0.7])) for _ in range(400)]
print("n=4 W/R=3/2", run(4,Fr(1),Fr(3,2),sample4))
