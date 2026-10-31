"""A6 v8 delta audit: exact checks of the finite examples touched by, or adjacent to, the v8 wording change in Theorem 3's construction."""
from fractions import Fraction as F
from itertools import permutations

def mk(rank, gg):
    ge = lambda u, v: rank[u] <= rank[v]          # u at least as normal as v (lower rank = more normal)
    def B(Fs): return {s for s in Fs if not any(gg(u, s) for u in Fs)}
    def K(Fs, x): return B(Fs) | {v for v in Fs if ge(v, x)}
    def KD(E, D, x): ED = E & D; return B(ED) | {v for v in ED if ge(v, x)}
    return B, K, KD

def ex(pr, S, f):
    S = list(S); tot = sum(pr[s] for s in S); return sum(pr[s]*f(s) for s in S)/tot

def kdt_choice(pr, ken, acts, order):
    best = None
    for name in order:
        v = ex(pr, ken, acts[name])
        if best is None or v > best[1]: best = (name, v)
    return best

print("=== Three-state example (Theorem 3 illustration) ===")
S = ['a','b','c']; rank = {'a':0,'b':1,'c':2}
gg = lambda u, v: (u, v) == ('a','c')
B, K, KD = mk(rank, gg)
pr = {s: F(1,3) for s in S}; E = set(S); x = 'a'
ken = K(E, x); print("ken at a:", sorted(ken))
cells = [{'a'}, {'b','c'}]
acts = {'beta': {'a':F(1),'b':F(1),'c':F(-10)}, 'decl': {s:F(0) for s in S},
        'beta1': {'a':F(9,10),'b':F(3,2),'c':F(-101,10)}}
order = ['beta','decl','beta1']
A = lambda n: (lambda s: acts[n][s])
now = kdt_choice(pr, ken, {k: A(k) for k in acts}, order); print("KDT now:", now)
pol = {}
for c in cells:
    for s in c:
        k2 = K(E & c, s); pol[s] = kdt_choice(pr, k2, {k: A(k) for k in acts}, order)[0]
        print(f"  post-answer ken at {s}: {sorted(k2)} -> {pol[s]}")
ul = lambda s: acts[pol[s]][s]
print("policy current expectation:", ex(pr, ken, ul))
def ceu(n1, f1, n2, f2):
    D = {s for s in E if f1(s) != f2(s)}
    kd = KD(E, D, x); return D, kd, ex(pr, kd, lambda s: f1(s) - f2(s)) if kd else None
opts = {'beta': A('beta'), 'decl': A('decl'), 'beta1': A('beta1'), 'look': ul}
print("Pairwise (first minus second): KDT on ken | CEU on K^D")
res = {}
for p, q in [('beta1','look'), ('beta','look'), ('decl','look'), ('beta1','beta'), ('beta1','decl'), ('beta','decl')]:
    D, kd, c = ceu(p, opts[p], q, opts[q])
    k = ex(pr, ken, lambda s: opts[p](s) - opts[q](s)); res[(p,q)] = c
    print(f"  {p:5s} - {q:5s}: KDT {k}  CEU {c}   D={sorted(D)} K^D={sorted(kd)}")
assert res[('beta1','look')] == F(7,10) and ex(pr, ken, lambda s: acts['beta1'][s]-ul(s)) == F(7,10)
assert res[('beta','look')] == F(-9,2) and ex(pr, ken, lambda s: acts['beta'][s]-ul(s)) == F(1,2)
# CEU strict-preference graph: any cycle?
names = list(opts); pref = {(p,q) for p in names for q in names if p!=q and (ceu(p,opts[p],q,opts[q])[2] or 0) > 0}
cyc = any(((a,b) in pref and (b,c) in pref and (c,a) in pref) for a,b,c in permutations(names,3))
print("CEU strict preferences:", sorted(pref), " 3-cycle present:", cyc)

print("\n=== Five-state VER example (unchanged text; re-run) ===")
S = ['a','s2','s1','v2','v1']; rk = {'a':F(0),'s2':F(1,5),'s1':F(1,2),'v2':F(23,20),'v1':F(13,10)}
gg = lambda u, w: rk[w] - rk[u] > 1
B, K, KD = mk(rk, gg)
pr = dict(zip(S, [F(67,100),F(1,100),F(30,100),F(1,100),F(1,100)])); E = set(S); x = 'a'
ken = K(E, x); print("ken:", sorted(ken))
cells = [{'a'},{'s1','v1'},{'s2','v2'}]
N, eps, L = F(10), F(1,1000), F(304,10)
beta = {s: (F(1) if s in ken else -L) for s in S}
beta1 = {s: beta[s] + eps*(N if s=='s1' else F(-1)) for s in S}
acts = {'beta':beta, 'decl':{s:F(0) for s in S}, 'beta1':beta1}; order=['beta','decl','beta1']
fa = {k:(lambda s,k=k: acts[k][s]) for k in acts}
print("KDT now:", kdt_choice(pr, ken, fa, order))
pol = {}
for c in cells:
    for s in c: pol[s] = kdt_choice(pr, K(E&c, s), fa, order)[0]
print("policy:", pol)
ul = lambda s: acts[pol[s]][s]
print("KDT value of question:", ex(pr, ken, ul) - kdt_choice(pr, ken, fa, order)[1])
ver = F(0)
for b in set(pol.values()):
    Db = {s for s in E if pol[s]==b}; kd = KD(E, Db, x)
    term = ex(pr, ken & Db, lambda s:1)*0  # placeholder
    pDb = sum(pr[s] for s in ken & Db)/sum(pr[s] for s in ken)
    val = ex(pr, kd, lambda s: acts[b][s]-beta1[s])
    print(f"  b={b}: Pr(D_b|K)={float(pDb):.4f} K^D={sorted(kd)} E[u_b-u_beta1|K^D]={float(val):.5f}  E[beta1|K^D]={float(ex(pr,kd,lambda s: beta1[s])):.4f}")
    ver += pDb*val
print("VER sum (look - beta1):", float(ver))
for p,q in [('beta1','beta'),('beta1','decl'),('beta','decl')]:
    print("  differ everywhere", p, q, all(acts[p][s]!=acts[q][s] for s in S))

print("\n=== Four-state no-defeat example (unchanged; re-run) ===")
S=['a','x','b','c']; rk={'a':0,'x':1,'b':2,'c':3}
G={('a','x'),('a','b'),('a','c'),('x','c')}; gg=lambda u,v:(u,v) in G
B,K,KD=mk(rk,gg); pr={s:F(1,4) for s in S}; E=set(S); x='x'
ken=K(E,x); print("ken:",sorted(ken))
acts={'A1':dict(zip(S,[F(-2),F(31,10),F(-2),F(21,10)])),'A2':dict(zip(S,[F(3)]*3+[F(-3)]))}
fa={k:(lambda s,k=k: acts[k][s]) for k in acts}; now=kdt_choice(pr,ken,fa,['A1','A2']); print("KDT now:",now)
pol={}
for c in [{'x'},{'b','c'},{'a'}]:
    for s in c: pol[s]=kdt_choice(pr,K(E&c,s),fa,['A1','A2'])[0]
ul=lambda s: acts[pol[s]][s]
print("policy:",pol," KDT value:",ex(pr,ken,ul)-now[1])
D={s for s in E if ul(s)!=acts['A2'][s]}; kd=KD(E,D,x); print("CEU K^D:",sorted(kd)," CEU look-A2:",ex(pr,kd,lambda s:ul(s)-acts['A2'][s]))
ver=sum((sum(pr[s] for s in ken if pol[s]==b)/sum(pr[s] for s in ken))*ex(pr,KD(E,{s for s in E if pol[s]==b},x),lambda s:acts[b][s]-acts['A2'][s]) for b in set(pol.values()))
print("VER sum (look - A2):",ver)
