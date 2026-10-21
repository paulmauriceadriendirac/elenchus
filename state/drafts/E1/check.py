#!/usr/bin/env python3
"""Machine checks for E1 v3 ("Disjunctive Knowledge across Independent Sources").
(The v2 checks are preserved in check_v2.py.)

Setting (Goodman & Salow 2023, pp. 92, 118): a single evidential cell E (TRANSPARENCY),
two relations on E: >= ("at least as normal") and >> ("sufficiently more normal") obeying
  (i)  >= reflexive and transitive;
  (ii) >> irreflexive and implies >=;
  (iii) w1 >= w2 >> w3 >= w4  implies  w1 >> w4.
Completions (pp. 104-110, 113):
  I  : RK(w) = {v : not w >> v}
  K  : RK(w) = RB U up(w),           up(w) = {v : v >= w}
  KM : RK(w) = RB U {v : exists u. v >= u, w >= u, not w >> u}
  JTB: RK(w) = RB U {w}
  RB = {v : no u >> v}.
  MEET (v3, repaired definition): RK(w) = up(w) U {v : exists b in RB, v >= glb(w, b)}.
Multi-dimensional account (p. 118): E is a product of respects; w >= v iff w is at least as
normal in every respect; w >> v iff w >= v and w is sufficiently more normal in some respect.

Claims checked (numbering as in v3):
  Lemma 1   Under COMPARABILITY, RB and up(w) are nested, so K(w) is RB or up(w).
  Thm 1     On products KM(w) = prod_d I_d(w_d) = {v : for no d, w >> w[d:=v_d]}
            = {v : not w >> glb(w, v)}.
  Prop 2    On products (RB nonempty): (a) the projection of K(w) on each respect d is
            B_d U up_d(w_d); (b) K(w) is a box (= prod_d (B_d U up_d(w_d))) unless
            COND(w): some respect d has w_d outside B_d and some other respect e has w_e
            strictly more normal than some state in B_e; (c) COND(w) iff K(w) is neither RB
            nor up(w) iff K violates COMBINATION at w; (d) under COND, with witnesses d, e,
            K knows "respect d is within belief, or respect e is at least as normal as w_e",
            knows neither disjunct, the first is false and believed, the second true.
  Fig 4     K(0,2) = JTB(0,2) = RB U {(0,2)}; JTB satisfies CONVEXITY at (0,2).
  Prop 3    For any relation satisfying FACTIVITY on a product: SEPARATION at w iff
            COMBINATION (anchored at sets S containing a respect outside belief) at w.
            Brute force over all A, B.
  Prop 4    MEET: (a) = K on every comparable structure; (b) on products
            = prod_d (B_d U up_d(w_d)); (c) framework principles, transitivity;
            (d) the most restrictive relation with FACTIVITY, INDUCTIVE LIMITS, CONVEXITY and
            COMBINATION (any number of respects); MEET is the box hull of K; and
            K <= MEET <= KM <= I on products.
  Table     SEPARATION / MARGINS for I, K, KM, MEET on products.
  Cor 5     Probabilist relations (p. 121) from independent marginals: KM on the product =
            intersection of single-respect I contexts; MEET = intersection of single-respect
            K contexts.  Figure-5 parameters: joint context facts quoted in the text.
  Discovery K's loss of knowledge on discovering an antecedent, in 2 dimensions and in one
            (generic); MEET undefined (no glb) on a non-product cell.
  Non-well-founded / infinite: z3 with quantifiers over integers.
Run: python3 check.py   (exits non-zero on any failure)
"""
import itertools, random, sys
from fractions import Fraction

FAIL = []
def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)

# ---------- one-dimensional structures ----------
def dim_structures(k):
    """All (rank, S) on {0..k-1}: rank gives a total preorder (lower = more normal);
    S = set of pairs (x,y) with x >> y, satisfying (i)-(iii). Deduplicated."""
    seen, out = set(), []
    for rank in itertools.product(range(k), repeat=k):
        lv = sorted(set(rank)); rank = tuple(lv.index(r) for r in rank)
        strict = [(x, y) for x in range(k) for y in range(k) if rank[x] < rank[y]]
        for m in range(1 << len(strict)):
            S = frozenset(p for i, p in enumerate(strict) if m >> i & 1)
            key = (rank, S)
            if key in seen: continue
            ge = lambda a, b: rank[a] <= rank[b]
            ok = all(((x1, x4) in S)
                     for (x2, x3) in S for x1 in range(k) for x4 in range(k)
                     if ge(x1, x2) and ge(x3, x4))
            if ok:
                seen.add(key); out.append(key)
    return out

# ---------- generic structure on a finite set ----------
class Struct:
    def __init__(self, W, ge, sm):
        self.W = W; self.ge = ge; self.sm = sm
        self.RB = frozenset(v for v in W if not any(sm(u, v) for u in W))
    def up(self, w): return frozenset(v for v in self.W if self.ge(v, w))
    def I(self, w):  return frozenset(v for v in self.W if not self.sm(w, v))
    def K(self, w):  return self.RB | self.up(w)
    def JTB(self, w): return self.RB | {w}
    def KM(self, w):
        M = [u for u in self.W if self.ge(w, u) and not self.sm(w, u)]
        return self.RB | frozenset(v for v in self.W if any(self.ge(v, u) for u in M))
    def glb(self, a, b):
        lows = [u for u in self.W if self.ge(a, u) and self.ge(b, u)]
        g = [u for u in lows if all(self.ge(u, z) for z in lows)]
        return g[0] if g else None
    def MEET(self, w):
        out = set(self.up(w))
        for b in self.RB:
            g = self.glb(w, b)
            if g is None: return None
            out |= {v for v in self.W if self.ge(v, g)}
        return frozenset(out)
    def axioms(self):
        W, ge, sm = self.W, self.ge, self.sm
        a = all(ge(w, w) for w in W) and all(ge(x, z) for x in W for y in W for z in W if ge(x, y) and ge(y, z))
        b = all(not sm(w, w) for w in W) and all(ge(x, y) for x in W for y in W if sm(x, y))
        c = all(sm(w1, w4) for w2 in W for w3 in W if sm(w2, w3)
                for w1 in W if ge(w1, w2) for w4 in W if ge(w3, w4))
        return a and b and c
    def convex_at(self, R):
        return not any(v not in R and any(self.ge(v, u) for u in R) for v in self.W)
    def framework(self, RK):
        W, sm = self.W, self.sm
        for w in W:
            R = RK(w)
            if w not in R: return False
            if any(sm(w, v) and v in R for v in W): return False
            if not self.RB <= R: return False
            if not self.convex_at(R): return False
        return True
    def margins(self, RK):
        W, ge, sm = self.W, self.ge, self.sm
        return all(v in RK(w) for w in W for v in W
                   if ge(w, v) and not ge(v, w) and not sm(w, v))
    def transitive(self, RK):
        return all(RK(v) <= RK(w) for w in self.W for v in RK(w))

def product(dims):
    W = list(itertools.product(*[range(len(r)) for r, _ in dims]))
    def ge(w, v): return all(dims[d][0][w[d]] <= dims[d][0][v[d]] for d in range(len(dims)))
    def sm(w, v): return ge(w, v) and any((w[d], v[d]) in dims[d][1] for d in range(len(dims)))
    return Struct(W, ge, sm)

def per_dim(dims, d):
    rank, S = dims[d]; k = len(rank)
    B = {x for x in range(k) if not any((y, x) in S for y in range(k))}
    I = lambda x: {y for y in range(k) if (x, y) not in S}
    up = lambda x: {y for y in range(k) if rank[y] <= rank[x]}
    return B, I, up, rank

def is_box(R, n):
    proj = [set(v[d] for v in R) for d in range(n)]
    return set(R) == set(itertools.product(*proj))

def box_hull(R, n):
    return frozenset(itertools.product(*[sorted(set(v[d] for v in R)) for d in range(n)]))

def splice(w, v, S, n):
    """situation agreeing with w on S and with v elsewhere"""
    return tuple(w[j] if j in S else v[j] for j in range(n))

def subsets_of_respects(n):
    return [frozenset(c) for r in range(1, n) for c in itertools.combinations(range(n), r)]

def combination_B(R, w, n, B):
    """COMBINATION (v3): for v in R and S containing a respect where w is outside belief,
    w_S v_T in R.  B = per-respect belief sets."""
    for S in subsets_of_respects(n):
        if all(w[s] in B[s] for s in S): continue
        for v in R:
            if splice(w, v, S, n) not in R: return False
    return True

def separation(R, w, n, B, dims_sizes):
    """SEPARATION by brute force: for every partition (S,T), every A <= X_S, B' <= X_T:
    if R <= A v B', A false at w and believed (prod_S B_s <= A), then R_T <= B'."""
    for S in subsets_of_respects(n):
        T = [j for j in range(n) if j not in S]; Sl = sorted(S)
        XS = list(itertools.product(*[range(dims_sizes[s]) for s in Sl]))
        XT = list(itertools.product(*[range(dims_sizes[t]) for t in T]))
        BS = set(itertools.product(*[sorted(B[s]) for s in Sl]))
        wS = tuple(w[s] for s in Sl)
        RS = [tuple(v[s] for s in Sl) for v in R]; RT = [tuple(v[t] for t in T) for v in R]
        RTset = set(RT)
        for ma in range(1 << len(XS)):
            A = {XS[i] for i in range(len(XS)) if ma >> i & 1}
            if wS in A or not BS <= A: continue          # A must be false and believed
            # the strongest B' with R <= A v B' is the set of T-parts of R-members outside A
            need = {RT[i] for i in range(len(RS)) if RS[i] not in A}
            # knows A v B' iff need <= B'; knows B' iff RTset <= B'; minimal B' = need
            if not RTset <= need: return False
    return True

# ---------- product families ----------
D2, D3 = dim_structures(2), dim_structures(3)
D4 = dim_structures(4)
print("one-dimensional structures: k=2:", len(D2), " k=3:", len(D3), " k=4:", len(D4))
families = []
families += [[a, b] for a in D3 for b in D3]
families += [[a, b] for a in D2 for b in D4]
families += [[a, b, c] for a in D2 for b in D2 for c in D3]
random.seed(1)
families += [[random.choice(D4), random.choice(D4)] for _ in range(300)]
print("product structures checked:", len(families))

table = {name: {"sep_fail": 0, "marg_fail": 0} for name in ("I", "K", "KM", "MEET")}
for dims in families:
    n = len(dims); P = product(dims)
    check(P.axioms(), f"product relations violate (i)-(iii): {dims}")
    pd = [per_dim(dims, d) for d in range(n)]
    Bs = [pd[d][0] for d in range(n)]
    check(P.RB == frozenset(itertools.product(*[sorted(b) for b in Bs])), "RB != prod B_d")
    for w in P.W:
        I_fac = frozenset(itertools.product(*[pd[d][1](w[d]) for d in range(n)]))
        # Thm 1 and its two global non-disjunctive forms
        KMw = P.KM(w)
        check(KMw == I_fac, f"Thm1 fails at {w} in {dims}")
        f1 = frozenset(v for v in P.W
                       if not any(P.sm(w, tuple(v[j] if j == d else w[j] for j in range(n)))
                                  for d in range(n)))
        f2 = frozenset(v for v in P.W if not P.sm(w, P.glb(w, v)))
        check(KMw == f1 == f2, f"Thm1 global forms fail at {w}")
        # Prop 2
        Kw = P.K(w); upw = P.up(w)
        dk = frozenset(itertools.product(*[sorted(pd[d][0] | pd[d][2](w[d])) for d in range(n)]))
        for d in range(n):
            check(set(v[d] for v in Kw) == pd[d][0] | pd[d][2](w[d]), f"Prop2a projection at {w}")
        wit = [(d, e, b) for d in range(n) for e in range(n) if d != e and w[d] not in pd[d][0]
               for b in pd[e][0] if pd[e][3][w[e]] < pd[e][3][b]]
        cond = bool(wit)
        check(is_box(Kw, n) == (not cond), f"Prop2b box condition at {w} in {dims}")
        if not cond: check(Kw == dk, f"Prop2b K != prod(B U up) at {w}")
        check((Kw not in (P.RB, upw)) == cond, f"Prop2c active disjunction at {w}")
        check(combination_B(Kw, w, n, Bs) == (not cond), f"Prop2c COMBINATION at {w}")
        for (d, e, b) in wit:
            A = frozenset(v for v in P.W if v[d] in pd[d][0])           # respect d within belief
            Bp = frozenset(v for v in P.W if v[e] in pd[e][2](w[e]))     # e at least as normal
            check(Kw <= A | Bp and not Kw <= A and not Kw <= Bp and w not in A and w in Bp
                  and P.RB <= A, f"Prop2d Gettier disjunction at {w}")
        # Prop 4
        Mw = P.MEET(w)
        check(Mw == dk, f"Prop4b MEET != prod(B U up) at {w} in {dims}")
        check(Mw == box_hull(Kw, n), f"MEET is not the box hull of K at {w}")
        check(Kw <= Mw <= KMw <= P.I(w), f"chain K <= MEET <= KM <= I fails at {w}")
    for name, RK in (("I", P.I), ("K", P.K), ("KM", P.KM), ("MEET", P.MEET)):
        check(P.framework(RK), f"{name} violates framework principles in {dims}")
        if not all(combination_B(RK(w), w, n, Bs) for w in P.W): table[name]["sep_fail"] += 1
        if not P.margins(RK): table[name]["marg_fail"] += 1
    check(P.transitive(P.MEET), f"MEET not transitive in {dims}")
    for w in P.W:
        for w2 in P.W:
            if P.ge(w, w2): check(P.KM(w) <= P.KM(w2), "KM monotonicity on products")
print("structures in which each completion fails SEPARATION (=COMBINATION) / MARGINS:")
for name, t in table.items():
    print(f"  {name:4s}  SEPARATION fails in {t['sep_fail']:5d}   MARGINS fails in {t['marg_fail']:5d}")
check(table["KM"]["sep_fail"] == 0 and table["KM"]["marg_fail"] == 0, "KM table")
check(table["MEET"]["sep_fail"] == 0 and table["MEET"]["marg_fail"] > 0, "MEET table")
check(table["I"]["sep_fail"] > 0 and table["I"]["marg_fail"] == 0, "I table")
check(table["K"]["sep_fail"] > 0 and table["K"]["marg_fail"] > 0, "K table")

# ---------- Prop 3: SEPARATION <-> COMBINATION, brute force over all A, B ----------
random.seed(2)
sample = random.sample([f for f in families if len(f) == 2 and len(f[0][0]) == 3], 250) + \
         random.sample([f for f in families if len(f) == 3], 60)
n_rel = 0
for dims in sample:
    n = len(dims); P = product(dims); sizes = [len(r) for r, _ in dims]
    Bs = [per_dim(dims, d)[0] for d in range(n)]
    rels = [P.I, P.K, P.KM, P.MEET, P.JTB]
    for w in P.W:
        cands = [RK(w) for RK in rels]
        for _ in range(4):   # random relations satisfying FACTIVITY
            cands.append(frozenset([w]) | frozenset(v for v in P.W if random.random() < 0.5))
        for R in cands:
            check(separation(R, w, n, Bs, sizes) == combination_B(R, w, n, Bs),
                  f"Prop3 SEPARATION <-> COMBINATION fails at {w} in {dims}")
            n_rel += 1
print("Prop 3: SEPARATION <-> COMBINATION checked by brute force on", n_rel, "relation-situation pairs")

# ---------- Prop 4(d): MEET is the knowledge default under COMBINATION ----------
def minimal_comb(P, w, n, Bs):
    R = set(P.RB) | {w}
    while True:
        new = set(R)
        for S in subsets_of_respects(n):
            if all(w[s] in Bs[s] for s in S): continue
            for v in R: new.add(splice(w, v, S, n))
        new |= {u for u in P.W if any(P.ge(u, v) for v in new)}
        if new == R: return frozenset(R)
        R = new
for dims in families:
    n = len(dims); P = product(dims); Bs = [per_dim(dims, d)[0] for d in range(n)]
    for w in P.W:
        check(minimal_comb(P, w, n, Bs) == P.MEET(w), f"Prop4d MEET not the knowledge default at {w}")
print("Prop 4(d): MEET = most restrictive relation with FACTIVITY, IL, CONVEXITY, COMBINATION: checked")

# ---------- Lemma 1 and Prop 4(a): comparable structures ----------
cnt = 0
def comparable_struct(rank, S):
    k = len(rank)
    return Struct(list(range(k)), lambda a, b, r=rank: r[a] <= r[b], lambda a, b, S=S: (a, b) in S)
for k in range(1, 5):
    for rank, S in dim_structures(k):
        st = comparable_struct(rank, S)
        for w in st.W:
            Kw = st.K(w)
            check(st.RB <= st.up(w) or st.up(w) <= st.RB, "Lemma1 nesting")
            check(Kw == (st.RB if w in st.RB else st.up(w)), "Lemma1 K in {RB, up}")
            check(st.MEET(w) == Kw, f"Prop4a MEET != K under comparability: {rank},{S},{w}")
        cnt += 1
random.seed(3)
for _ in range(3000):
    k = 5
    rank = tuple(random.randrange(5) for _ in range(k))
    lv = sorted(set(rank)); rank = tuple(lv.index(r) for r in rank)
    gap = random.randint(1, 4)
    S = frozenset((x, y) for x in range(k) for y in range(k) if rank[y] - rank[x] >= gap)
    st = comparable_struct(rank, S)
    if not st.axioms(): continue
    for w in st.W:
        check(st.MEET(w) == st.K(w) == (st.RB if w in st.RB else st.up(w)), "Lemma1/Prop4a (k=5)")
    cnt += 1
print("comparable structures checked for Lemma 1 and MEET = K:", cnt)

# ---------- Figure 4 of Goodman & Salow (p. 119) ----------
fig4dim = ((0, 1, 2), frozenset({(0, 2)}))
F = product([fig4dim, fig4dim])
def S_(*xs): return frozenset(xs)
sq = S_((0, 0), (0, 1), (1, 0), (1, 1))
check(F.RB == sq, "fig4 RB")
check(F.K((0, 2)) == sq | S_((0, 2)), "fig4 K(0,2)")
check(F.K((0, 2)) == F.JTB((0, 2)), "fig4 K(0,2) = JTB(0,2)")
check(F.convex_at(F.JTB((0, 2))), "fig4 JTB satisfies CONVEXITY at (0,2)")
check(F.JTB((2, 0)) == F.K((2, 0)), "fig4 K = JTB at (2,0)")
check(F.KM((0, 2)) == sq | S_((0, 2), (1, 2)), "fig4 KM(0,2)")
check(F.MEET((0, 2)) == F.KM((0, 2)), "fig4 MEET(0,2) = KM(0,2)")
check(F.I((0, 2)) == frozenset(F.W) - {(2, 2)}, "fig4 I(0,2)")
check(F.MEET((1, 1)) == sq and F.KM((1, 1)) == frozenset(F.W), "fig4 MEET vs KM at (1,1)")
thermOK = frozenset(v for v in F.W if v[1] != 2); scaleOrd = frozenset(v for v in F.W if v[0] == 0)
K02 = F.K((0, 2))
check(K02 <= thermOK | scaleOrd and not K02 <= thermOK and not K02 <= scaleOrd,
      "fig4: K knows 'thermometer not bizarre or scale ordinary', neither disjunct")
check(not F.up((0, 2)) >= K02, "fig4: K does not know up(0,2)")
print("figure 4: K(0,2) = JTB(0,2) =", sorted(K02))

# ---------- discovery ----------
Ep = [w for w in F.W if w[1] == 2]
Fp = Struct(Ep, F.ge, F.sm)
after = Fp.K((0, 2))
check(after == S_((0, 2), (1, 2)), "2-dim discovery: K after learning thermometer bizarre")
# one dimension (generic): error magnitudes 0..N, x >> y iff y >= x + c; actual error e, c <= e < 2c
N, c = 12, 3
one = Struct(list(range(N + 1)), lambda a, b: a <= b, lambda a, b: b >= a + c)
for e in range(c, 2 * c - 1):   # discrete analogue of c <= e < 2c (RB' = {c..2c-1})
    before = one.K(e)
    check(before == frozenset(range(e + 1)), "1-dim K = up(e)")
    oneP = Struct([x for x in range(N + 1) if x >= c], one.ge, one.sm)
    check(not oneP.K(e) <= frozenset(range(e + 1)), "1-dim: knowledge 'error <= e' lost on discovering error >= c")
# non-product cell: discovering that (1,1) does not obtain
Fn = Struct([w for w in F.W if w != (1, 1)], F.ge, F.sm)
check(Fn.glb((0, 1), (1, 0)) is None and Fn.MEET((0, 1)) is None,
      "MEET should be undefined (no glb) on the non-product cell")
print("discovery checks done; MEET undefined at (0,1) on cell E - {(1,1)}")

# ---------- Probabilist relations (G&S p. 121) ----------
def prob_rel(cells, P, t):
    def ge(a, b): return P[a] >= P[b]
    def sm(a, b):
        cond = [x for x in cells if P[x] <= P[a]]
        num = sum(P[x] for x in cond if P[x] > P[b]); den = sum(P[x] for x in cond)
        return den > 0 and num / den >= t
    return ge, sm

def probabilist_check(marg, t):
    n = len(marg); dims = []
    for Pm in marg:
        cells = list(range(len(Pm)))
        ge, sm = prob_rel(cells, {x: Pm[x] for x in cells}, t)
        st = Struct(cells, ge, sm)
        check(st.axioms(), f"probabilist per-respect relations violate (i)-(iii)")
        rank = tuple(sorted(set(-Pm[x] for x in cells)).index(-Pm[x]) for x in cells)
        S = frozenset((a, b) for a in cells for b in cells if sm(a, b))
        dims.append((rank, S))
    Prod = product(dims); W = Prod.W
    joint = {w: 1 for w in W}
    for w in W:
        for d in range(n): joint[w] *= marg[d][w[d]]
    ctx = []
    for d in range(n):
        Pd = {w: marg[d][w[d]] for w in W}
        ge, sm = prob_rel(W, Pd, t)
        ctx.append(Struct(W, ge, sm))
    for w in W:
        interI, interK = set(W), set(W)
        for cx in ctx:
            check(cx.KM(w) == cx.I(w), "KM != I in a comparable context")
            interI &= set(cx.I(w)); interK &= set(cx.K(w))
        check(set(Prod.KM(w)) == interI, f"Cor5a fails at {w}")
        check(set(Prod.MEET(w)) == interK, f"Cor5b fails at {w}")
    ge, sm = prob_rel(W, joint, t)
    return Prod, ctx, Struct(W, ge, sm), joint

m = [Fraction(100, 111), Fraction(10, 111), Fraction(1, 111)]
Prod, ctx, J, joint = probabilist_check([m, m], Fraction(95, 100))
check(all(Prod.sm(a, b) == F.sm(a, b) and Prod.ge(a, b) == F.ge(a, b) for a in F.W for b in F.W),
      "figure-5 marginals do not reproduce the figure-4 per-respect relations")
check(J.RB == S_((0, 0), (0, 1), (1, 0)), "joint RB")
check(J.I((0, 0)) == S_((0, 0), (0, 1), (1, 0)), "joint I at (0,0)")
check(J.I((0, 2)) == frozenset(J.W) - {(2, 2)} and J.KM((0, 2)) == J.I((0, 2)), "joint I/KM at (0,2)")
check(J.K((0, 2)) == sq | S_((0, 2), (2, 0)) and J.K((0, 2)) == J.up((0, 2)),
      "joint K at (0,2): six situations, = up(0,2)")
check(all((1, 2) in cx.I((0, 2)) for cx in ctx), "single-respect contexts leave (1,2) open")
# the joint probabilist (I) violates SEPARATION at (0,2): knows 'thermometer not bizarre or
# scale not bizarre' without knowing the second; first disjunct false and believed
scaleNB = frozenset(v for v in J.W if v[0] != 2)
Ij = J.I((0, 2))
check(Ij <= thermOK | scaleNB and not Ij <= scaleNB and J.RB <= thermOK, "joint I SEPARATION violation")
check(J.K((0, 2)) <= thermOK | scaleOrd and not J.K((0, 2)) <= scaleOrd, "joint K Gettier disjunction")
# a question singling out (1,2): partition {(1,2)} vs the rest
q = {w: (1 if w == (1, 2) else 0) for w in J.W}
pq = {0: sum(joint[w] for w in J.W if q[w] == 0), 1: joint[(1, 2)]}
geq, smq = prob_rel([0, 1], pq, Fraction(95, 100))
Q = Struct(J.W, lambda a, b: geq(q[a], q[b]), lambda a, b: smq(q[a], q[b]))
check((1, 2) not in Q.I((0, 2)) and (1, 2) not in Q.K((0, 2)), "gerrymandered question excludes (1,2)")
print("joint context: RB =", sorted(J.RB), "| K(0,2) =", sorted(J.K((0, 2))),
      "| I(0,2) excludes", sorted(set(J.W) - J.I((0, 2))))
random.seed(4)
for _ in range(200):
    n = random.choice([2, 2, 3]); marg = []
    for d in range(n):
        k = random.choice([2, 3, 4]) if n == 2 else random.choice([2, 3])
        raw = [Fraction(random.randint(1, 30)) for _ in range(k)]
        s = sum(raw); marg.append([x / s for x in raw])
    probabilist_check(marg, Fraction(random.randint(55, 99), 100))
print("random probabilist product models checked: 200")

# ---------- z3: Theorem 1 on arbitrary 3x3; infinite and non-well-founded respects ----------
try:
    from z3 import (Solver, Int, Ints, Bool, And, Or, Not, Implies, ForAll, Exists, If,
                    unsat, sat)
    # (1) Theorem 1 on arbitrary 3x3 structures (as in v2)
    s = Solver(); k = 3
    r = [[Int(f"r{d}_{x}") for x in range(k)] for d in range(2)]
    sd = [[[Bool(f"s{d}_{x}_{y}") for y in range(k)] for x in range(k)] for d in range(2)]
    for d in range(2):
        for x in range(k):
            s.add(r[d][x] >= 0, r[d][x] < k, Not(sd[d][x][x]))
            for y in range(k):
                s.add(Implies(sd[d][x][y], r[d][x] <= r[d][y]))
                for x1 in range(k):
                    for y1 in range(k):
                        s.add(Implies(And(sd[d][x][y], r[d][x1] <= r[d][x], r[d][y] <= r[d][y1]),
                                      sd[d][x1][y1]))
    W = list(itertools.product(range(k), range(k)))
    def GE(a, b): return And(*[r[d][a[d]] <= r[d][b[d]] for d in range(2)])
    def SM(a, b): return And(GE(a, b), Or(*[sd[d][a[d]][b[d]] for d in range(2)]))
    def RBz(v): return And(*[Not(SM(u, v)) for u in W])
    def KMacc(w, v): return Or(RBz(v), Or(*[And(GE(v, u), GE(w, u), Not(SM(w, u))) for u in W]))
    def FAC(w, v): return And(*[Not(sd[d][w[d]][v[d]]) for d in range(2)])
    s.add(Or(*[KMacc(w, v) != FAC(w, v) for w in W for v in W]))
    res = s.check()
    print("z3: counterexample to Theorem 1 on arbitrary 3x3 structures:", res)
    check(res == unsat, "z3 found a counterexample to Theorem 1")

    # Infinite respects with quantifiers. Situations (a, s): a an integer, s in {0,1,2} with
    # G&S's figure-4 relations on s (0 >> 2 only).
    def mk(geA, smA, domA):
        ws, wa, vs, va, us, ua, bs, ba = Ints("ws wa vs va us ua bs ba")
        def dom(a, s_): return And(domA(a), s_ >= 0, s_ <= 2)
        def geB(x, y): return x <= y
        def smB(x, y): return And(x == 0, y == 2)
        def GEz(a1, s1, a2, s2): return And(geA(a1, a2), geB(s1, s2))
        def SMz(a1, s1, a2, s2): return And(GEz(a1, s1, a2, s2), Or(smA(a1, a2), smB(s1, s2)))
        def RBq(a, s_): return Not(Exists([ua, us], And(dom(ua, us), SMz(ua, us, a, s_))))
        return locals()
    # (2) non-well-founded: integers, larger = more normal, x >> y iff x >= y + 2
    Z = mk(lambda x, y: x >= y, lambda x, y: x >= y + 2, lambda a: True)
    ws, wa, vs, va, ua, us, ba, bs = Z["ws"], Z["wa"], Z["vs"], Z["va"], Z["ua"], Z["us"], Z["ba"], Z["bs"]
    dom, GEz, SMz, RBq = Z["dom"], Z["GEz"], Z["SMz"], Z["RBq"]
    def solve(*cs):
        s2 = Solver(); s2.set("timeout", 60000); s2.add(*cs); return s2.check()
    # RB is empty
    r1 = solve(dom(va, vs), RBq(va, vs))
    check(r1 == unsat, "non-well-founded: RB should be empty")
    # Theorem 1: KM(w) = prod I_d(w_d)
    KMq = Or(RBq(va, vs), Exists([ua, us], And(dom(ua, us), GEz(va, vs, ua, us), GEz(wa, ws, ua, us),
                                                 Not(SMz(wa, ws, ua, us)))))
    FACq = And(Not(wa >= va + 2), Not(And(ws == 0, vs == 2)))
    r2 = solve(dom(wa, ws), dom(va, vs), KMq != FACq)
    check(r2 == unsat, "non-well-founded: Theorem 1 fails")
    # repaired MEET = up(w) = K(w); unrepaired MEET is empty (violates FACTIVITY)
    glbA = If(wa <= ba, wa, ba); glbS = If(ws >= bs, ws, bs)
    MEETr = Or(GEz(va, vs, wa, ws), Exists([ba, bs], And(dom(ba, bs), RBq(ba, bs), GEz(va, vs, glbA, glbS))))
    Kq = Or(RBq(va, vs), GEz(va, vs, wa, ws))
    r3 = solve(dom(wa, ws), dom(va, vs), Or(MEETr != Kq, Kq != GEz(va, vs, wa, ws)))
    check(r3 == unsat, "non-well-founded: repaired MEET != K = up(w)")
    r4 = solve(dom(wa, ws), Exists([ba, bs], And(dom(ba, bs), RBq(ba, bs))))
    check(r4 == unsat, "non-well-founded: unrepaired MEET should have no witnesses")
    print("z3 non-well-founded respect: RB empty, Thm 1 holds, repaired MEET = K = up(w):",
          r1, r2, r3)
    # (3) infinite but well-founded: naturals, smaller = more normal, x >> y iff y >= x + 2
    Nn = mk(lambda x, y: x <= y, lambda x, y: y >= x + 2, lambda a: a >= 0)
    ws, wa, vs, va, ua, us, ba, bs = Nn["ws"], Nn["wa"], Nn["vs"], Nn["va"], Nn["ua"], Nn["us"], Nn["ba"], Nn["bs"]
    dom, GEz, SMz, RBq = Nn["dom"], Nn["GEz"], Nn["SMz"], Nn["RBq"]
    BA = lambda a: a <= 1; BS = lambda s_: s_ <= 1
    r5 = solve(dom(va, vs), RBq(va, vs) != And(BA(va), BS(vs)))
    check(r5 == unsat, "naturals: RB != B_A x B_S")
    KMq = Or(RBq(va, vs), Exists([ua, us], And(dom(ua, us), GEz(va, vs, ua, us), GEz(wa, ws, ua, us),
                                                 Not(SMz(wa, ws, ua, us)))))
    FACq = And(Not(va >= wa + 2), Not(And(ws == 0, vs == 2)))
    r6 = solve(dom(wa, ws), dom(va, vs), KMq != FACq)
    check(r6 == unsat, "naturals: Theorem 1 fails")
    glbA = If(wa >= ba, wa, ba); glbS = If(ws >= bs, ws, bs)
    MEETr = Or(GEz(va, vs, wa, ws), Exists([ba, bs], And(dom(ba, bs), RBq(ba, bs), GEz(va, vs, glbA, glbS))))
    BOX = And(Or(BA(va), va <= wa), Or(BS(vs), vs <= ws))
    r7 = solve(dom(wa, ws), dom(va, vs), MEETr != BOX)
    check(r7 == unsat, "naturals: MEET != prod(B U up)")
    # Prop 2 condition: K(w) is a box iff not COND; COND: (wa not in B_A and ws strictly better
    # than some believed s-state) or (ws not in B_S and wa strictly better than some believed a)
    Kq = Or(RBq(va, vs), GEz(va, vs, wa, ws))
    COND = Or(And(Not(BA(wa)), ws < 1), And(Not(BS(ws)), wa < 1))
    r8 = solve(dom(wa, ws), dom(va, vs), Not(COND), Kq != BOX)
    check(r8 == unsat, "naturals: K not a box although COND fails")
    r9 = solve(dom(wa, ws), COND, Not(Exists([va, vs], And(dom(va, vs), BOX, Not(Kq)))))
    check(r9 == unsat, "naturals: K a box although COND holds")
    print("z3 infinite well-founded respect (naturals x fig-4): Thm 1, MEET box, Prop 2:",
          r5, r6, r7, r8, r9)
except ImportError:
    print("z3 not available; skipped")

print()
print("ALL CHECKS PASSED" if not FAIL else f"{len(FAIL)} FAILURES")
sys.exit(1 if FAIL else 0)
