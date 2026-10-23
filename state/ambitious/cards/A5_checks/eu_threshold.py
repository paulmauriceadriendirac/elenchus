# Probe: neutral EU rules over answers to an n-cell question.
# Utility of guess G (union of k cells) at world w: a_k if w in G else b_k.
# EU(top-k set) = P_k*(a_k-b_k)+b_k where P_k = mass of k most probable cells.
# THRESHOLD(t): whenever top-k chosen (k<n), P_k >= t.
import itertools, random
import numpy as np
rng=np.random.default_rng(0)
def simplex_grid(n,steps):
    # all compositions of steps into n parts
    for c in itertools.product(range(steps+1),repeat=n-1):
        s=sum(c)
        if s<=steps:
            yield np.array(list(c)+[steps-s])/steps
def check(a,b,t,n,steps=60):
    worst=1.0; nontriv=False
    for P in simplex_grid(n,steps):
        Ps=np.sort(P)[::-1]; cum=np.cumsum(Ps)
        ev=[cum[k]*(a[k]-b[k])+b[k] for k in range(n)]
        k=int(np.argmax(ev))
        # tie-break toward larger k (more cautious) if within 1e-12
        best=max(ev); ks=[j for j in range(n) if ev[j]>=best-1e-12]; k=max(ks)
        if k<n-1:
            nontriv=True
            worst=min(worst,cum[k])
    return worst,nontriv
best=None
n=3
for trial in range(20000):
    a=np.sort(rng.uniform(0,1,n))[::-1]  # a1>a2>a3
    b=np.array([rng.uniform(-3,a[k]) for k in range(n)])
    worst,nt=check(a,b,0.9,n,steps=40)
    if nt and (best is None or worst>best[0]):
        best=(worst,a.copy(),b.copy())
print("n=3 best worst-case prob of chosen nontrivial answer:",best[0])
print("a",best[1],"b",best[2])
