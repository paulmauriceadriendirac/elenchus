# (i) Holguin 2022 'cogent' guesses (strict top-sets) = answers that are the UNIQUE EU-optimum for some
#     neutral (size-dependent), truth-directed (T_k>F_k), informativity-monotone (T_1>...>T_n) utility.
import itertools, random, z3
from fractions import Fraction as Fr
def cogent(G,P,n):
    return all(P[i]>P[j] for i in G for j in range(n) if j not in G)
random.seed(11); n=4; cells=range(n)
answers=[frozenset(s) for r in range(1,n+1) for s in itertools.combinations(cells,r)]
mism=0; checked=0
for trial in range(60):
    w=[random.randint(1,30) for _ in cells]; tot=sum(w); P=[Fr(x,tot) for x in w]
    for G in answers:
        T=[z3.Real('T%d'%k) for k in range(n+1)]; F=[z3.Real('F%d'%k) for k in range(n+1)]
        s=z3.Solver()
        for k in range(1,n): s.add(T[k]>T[k+1]); s.add(T[k]-F[k]>=1)
        def ev(H):
            pg=sum(P[c] for c in H); k=len(H)
            return T[k]*pg+(F[k]*(1-pg) if k<n else 0)
        for H in answers:
            if H!=G: s.add(ev(G)>ev(H))
        optimal_some = (s.check()==z3.sat)
        checked+=1
        if optimal_some!=cogent(G,P,n): mism+=1; print("mismatch",P,G,optimal_some,cogent(G,P,n))
print("answers checked:",checked," mismatches between 'cogent' and 'uniquely optimal for some admissible value':",mism)
