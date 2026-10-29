"""c8: refinement objection to the record measure (A5 v4).
Exact rational arithmetic. Optima via Theorem 3 (core maximisation of Phi), cross-checked
by brute force over all belief states where feasible (n<=4 worlds: 2^16 states).
(1) flagship case C=(.70,.15,.15), C'=(.75,.01,.24), T=1,F=-2,beta=3;
(2) split w2 into k equal pieces: is {w1} still believed?
(3) null splits: Phi_refined = 2^m Phi_coarse(beta/2^m) exactly;
(4) normalised (mean-separable) record measure: invariance under null splits, behaviour under
    the non-null splits of (2);
(5) coarsening to {w1, w23}: record measure violates full refinement invariance;
(6) greedy formation order-dependence at C."""
from fractions import Fraction as Fr
from itertools import combinations
import itertools

T, F = Fr(1), Fr(-2)

def props(n):
    return [frozenset(s) for r in range(n+1) for s in combinations(range(n), r)]

def e(C, p, T=T, F=F):
    c = sum((C[i] for i in p), Fr(0))
    return c*T + (1-c)*F

def phi_opt(C, beta, scale=Fr(1)):
    """scale multiplies the separable part (scale=1/|algebra| gives the mean version)."""
    n = len(C); P = props(n)
    ev = {p: scale*e(C, p) for p in P}
    best = None
    for X in P:
        val = sum((max(ev[p], 0) for p in P if X <= p), Fr(0)) + beta*sum((C[i] for i in X), Fr(0))
        if best is None or val > best[0]: best = (val, [X])
        elif val == best[0]: best[1].append(X)
    val, cores = best
    states = [frozenset(p for p in P if X <= p and ev[p] > 0) for X in cores]
    return val, cores, states

def EA(C, B, beta, scale=Fr(1)):
    n = len(C)
    core = frozenset(range(n))
    for p in B: core &= p
    return sum((scale*e(C, p) for p in B), Fr(0)) + beta*sum((C[i] for i in core), Fr(0))

def brute(C, beta, scale=Fr(1)):
    P = props(len(C)); best = None
    for mask in range(1 << len(P)):
        B = [P[i] for i in range(len(P)) if mask >> i & 1]
        v = EA(C, B, beta, scale)
        if best is None or v > best[0]: best = (v, [frozenset(B)])
        elif v == best[0]: best[1].append(frozenset(B))
    return best

def believes_w1(states):
    return [frozenset([0]) in s for s in states]

def fmt(v): return f"{float(v):.4f}"

def split(C, idx, k):
    return [C[i] for i in range(len(C)) if i != idx][:idx] + [C[idx]/k]*k + [C[i] for i in range(len(C)) if i != idx][idx:]

beta = Fr(3)
Cs = {"C": [Fr(70,100), Fr(15,100), Fr(15,100)], "C'": [Fr(75,100), Fr(1,100), Fr(24,100)]}
print("(1) flagship, flat premium beta=3")
for name, C in Cs.items():
    v, cores, st = phi_opt(C, beta)
    bv, bst = brute(C, beta)
    assert v == bv and set(st) == set(bst)
    print(name, fmt(v), "cores", [sorted(x) for x in cores], "w1 believed:", believes_w1(st))

print("(2) split w2 into k equal pieces (flat premium)")
for k in [2, 4, 8]:
    for name, C in Cs.items():
        Ck = split(C, 1, k)
        v, cores, st = phi_opt(Ck, beta)
        if len(Ck) <= 4:
            bv, bst = brute(Ck, beta); assert v == bv and set(st) == set(bst)
        print(f" k={k} {name} n={len(Ck)} max={fmt(v)} core={[sorted(x) for x in cores]} w1 believed={believes_w1(st)}")
# report's specific numbers for k=2 at C'
C2 = split(Cs["C'"], 1, 2)
P = props(4)
def Phi(C, X, beta, scale=Fr(1)):
    return sum((max(scale*e(C,p),0) for p in P if X <= p), Fr(0)) + beta*sum((C[i] for i in X), Fr(0))
print(" k=2 C': Phi({w1})=", fmt(Phi(C2, frozenset([0]), beta)), " Phi({w1,w3})=", fmt(Phi(C2, frozenset([0,3]), beta)))

print("(3) null splits: exact identities (flat: Phi_ref = 2^(k-1) Phi_coarse with beta/2^(k-1); mean version: Phi_ref = Phi_coarse)")
import random
random.seed(3)
for trial in range(40):
    a = Fr(random.randint(1, 98), 100); C0 = [a, Fr(0), 1 - a]       # w2 null
    for k in [2, 3, 4]:
        Cr = [a] + [Fr(0)]*k + [1 - a]; n = len(Cr); Pr = props(n)
        for X0 in props(3):
            if 1 in X0: continue                                      # cores without the null world
            X = frozenset(([0] if 0 in X0 else []) + ([n-1] if 2 in X0 else []))
            ref = sum((max(e(Cr,p),0) for p in Pr if X <= p), Fr(0))
            co = sum((max(e(C0,p),0) for p in props(3) if X0 <= p), Fr(0))
            assert ref == 2**(k-1) * co
            # flat: Phi_ref(X) = 2^(k-1) * [co + (beta/2^(k-1)) C(X0)]
            cX = sum((C0[i] for i in X0), Fr(0))
            assert ref + beta*cX == 2**(k-1) * (co + beta/2**(k-1)*cX)
            # mean version: scale 1/2^n on both sides, premium b unchanged -> identical Phi
            assert ref/2**n + Fr(3,8)*cX == co/2**3 + Fr(3,8)*cX
print(" identities hold exactly for 40 random credences, k=2,3,4 (cores without the null world;",
      "cores containing a null world are never better than the same core without it)")
print("(4) normalised record measure: separable part averaged over the algebra (scale=1/2^n), premium b")
for b in [Fr(3,8)]:
    for k in [1, 2, 4, 8]:
        for name, C in Cs.items():
            Ck = split(C, 1, k) if k > 1 else C
            n = len(Ck)
            v, cores, st = phi_opt(Ck, b, scale=Fr(1, 2**n))
            if n <= 4:
                bv, bst = brute(Ck, b, scale=Fr(1, 2**n)); assert v == bv and set(st) == set(bst)
            print(f" b={b} k={k} {name}: core={[sorted(x) for x in cores]} w1 believed={believes_w1(st)}")
    # null splits, exact invariance of verdicts on coarse propositions
    for name, C in {"(.70,0,.30)": [Fr(70,100),Fr(0),Fr(30,100)], "(.75,0,.25)": [Fr(75,100),Fr(0),Fr(25,100)]}.items():
        for k in [1, 2, 4, 8]:
            Ck = split(C, 1, k) if k > 1 else C
            n = len(Ck)
            v, cores, st = phi_opt(Ck, b, scale=Fr(1, 2**n))
            print(f" null split k={k} {name}: w1 believed={believes_w1(st)}, normalised max={fmt(v/ 1)}")

print("(5) coarsening {w1,w2,w3}->{w1,w23}, flat beta=3")
for c in [Fr(70,100), Fr(75,100)]:
    v, cores, st = phi_opt([c, 1-c], beta)
    print(f" two-cell c={c}: w1 believed={believes_w1(st)}; two-cell threshold (beta-F)/(T-F+beta)={fmt((beta-F)/(T-F+beta))}")

print("(6) greedy formation at C, flat beta=3")
C = Cs["C"]; P3 = props(3)
def greedy(order):
    B = []
    for p in order:
        if EA(C, B+[p], beta) > EA(C, B, beta): B.append(p)
    return B, EA(C, B, beta)
w1 = frozenset([0]); rest = [p for p in P3 if p != w1]
B, v = greedy([w1] + rest); print(" {w1} first: delta at first step =", fmt(EA(C,[w1],beta)-EA(C,[],beta)), "final", [sorted(p) for p in B], fmt(v))
B, v = greedy(rest + [w1]); print(" {w1} last: final", [sorted(p) for p in B], fmt(v), " last-step delta=", fmt(EA(C,[p for p in B],beta)-EA(C,[p for p in B if p!=w1],beta)))
