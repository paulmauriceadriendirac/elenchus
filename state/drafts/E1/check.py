#!/usr/bin/env python3
"""Machine checks for E1 v2 ("Respects of Normality").

Setting (Goodman & Salow 2023, pp. 92, 118): a single evidential cell E (TRANSPARENCY),
two relations on E: >= ("at least as normal") and >> ("sufficiently more normal") obeying
  (i)  >= reflexive and transitive;
  (ii) >> irreflexive and implies >=;
  (iii) w1 >= w2 >> w3 >= w4  implies  w1 >> w4.
Completions (pp. 109-110):
  I : RK(w) = {v : not w >> v}
  K : RK(w) = RB U {v : v >= w}
  KM: RK(w) = RB U {v : exists u. v >= u, w >= u, not w >> u}
  where RB = {v : no u >> v}.
Multi-dimensional account (p. 118): E is a product of dimensions; w >= v iff w is at least as
normal on every dimension; w >> v iff w >= v and w is sufficiently more normal on at least one
dimension.  Each dimension here is a total preorder with its own >>_d obeying (i)-(iii).

Claims checked (numbering as in v2):
  Thm 1   KM(w) = prod_d I_d(w_d) on every product structure.
  Prop 2  K(w) violates COMBINATION iff there are distinct d, e with w_d not believed on d and
          w_e strictly more normal than some believed value on e; otherwise K(w) is a product.
  Prop 3  MEET(w) = {v : exists b in RB, v >= glb(w, b)} (glb computed from >= alone)
          equals prod_d (B_d U up(w_d)); satisfies the five framework principles and
          transitivity; and equals K on every comparable structure (all total preorders, n<=5).
          MEET is the most restrictive relation satisfying FACTIVITY, INDUCTIVE LIMITS,
          CONVEXITY and COMBINATION (two dimensions), or FACTORIZATION (any number).
  Table   COMBINATION / MARGINS for I, K, KM, MEET on product structures.
  Mono    KM on product structures: w >= w' implies KM(w) subset of KM(w').
  Fig 4   G&S's figure-4 model: the stated accessibility sets.
  Cor 4   Probabilist relations (p. 121 proposal) built from independent marginals: the
          single-question relations are per-dimension relations obeying (i)-(iii), and
          KM on the product equals the intersection of single-question accessibility.
          Figure-5 parameters: joint-context verdicts quoted in the text.
A z3 cross-check of Thm 1 over arbitrary 3x3 structures is included.
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
        # normalise ranks to consecutive levels
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
    def I(self, w):  return frozenset(v for v in self.W if not self.sm(w, v))
    def K(self, w):  return self.RB | frozenset(v for v in self.W if self.ge(v, w))
    def KM(self, w):
        M = [u for u in self.W if self.ge(w, u) and not self.sm(w, u)]
        return self.RB | frozenset(v for v in self.W if any(self.ge(v, u) for u in M))
    def glb(self, a, b):
        lows = [u for u in self.W if self.ge(a, u) and self.ge(b, u)]
        g = [u for u in lows if all(self.ge(u, z) for z in lows)]
        return g[0] if g else None
    def MEET(self, w):
        out = set()
        for b in self.RB:
            g = self.glb(w, b)
            assert g is not None, "glb missing"
            out |= {v for v in self.W if self.ge(v, g)}
        return frozenset(out)
    def axioms(self):
        W, ge, sm = self.W, self.ge, self.sm
        a = all(ge(w, w) for w in W) and all(ge(x, z) for x in W for y in W for z in W if ge(x, y) and ge(y, z))
        b = all(not sm(w, w) for w in W) and all(ge(x, y) for x in W for y in W if sm(x, y))
        c = all(sm(w1, w4) for w2 in W for w3 in W if sm(w2, w3)
                for w1 in W if ge(w1, w2) for w4 in W if ge(w3, w4))
        return a and b and c
    def framework(self, RK):
        """FACTIVITY, INDUCTIVE KNOWLEDGE, INDUCTIVE LIMITS, CONVEXITY (EVIDENTIAL
        KNOWLEDGE is trivial in a single cell)."""
        W, ge, sm = self.W, self.ge, self.sm
        for w in W:
            R = RK(w)
            if w not in R: return False
            if any(sm(w, v) and v in R for v in W): return False
            if not self.RB <= R: return False
            if any(v not in R and any(ge(v, u) for u in R) for v in W): return False
        return True
    def margins(self, RK):
        W, ge, sm = self.W, self.ge, self.sm
        return all(v in RK(w) for w in W for v in W
                   if ge(w, v) and not ge(v, w) and not sm(w, v))
    def transitive(self, RK):
        return all(RK(v) <= RK(w) for w in self.W for v in RK(w))

def product(dims):
    """dims: list of (rank, S). Returns Struct on the full product with G&S's
    multi-dimensional relations."""
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

def is_box(R, W, n):
    proj = [set(v[d] for v in R) for d in range(n)]
    return set(R) == set(itertools.product(*proj))

def combination(R, w, n):
    """COMBINATION at w: if v in RK(w) then w[d := v_d] in RK(w), for every d."""
    return all(tuple(v[d] if j == d else w[j] for j in range(n)) in R
               for v in R for d in range(n))

# ---------- run the product checks ----------
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

table = {name: {"comb_fail": 0, "marg_fail": 0} for name in ("I", "K", "KM", "MEET")}
n_struct = 0
for dims in families:
    n = len(dims); P = product(dims); n_struct += 1
    check(P.axioms(), f"product relations violate (i)-(iii): {dims}")
    pd = [per_dim(dims, d) for d in range(n)]
    for w in P.W:
        # Thm 1
        fac = set(itertools.product(*[pd[d][1](w[d]) for d in range(n)]))
        check(set(P.KM(w)) == fac, f"Thm1 fails at {w} in {dims}")
        # Prop 3: MEET is dimensionwise K
        dk = set(itertools.product(*[pd[d][0] | pd[d][2](w[d]) for d in range(n)]))
        check(set(P.MEET(w)) == dk, f"Prop3 MEET != dimensionwise K at {w} in {dims}")
        # Prop 2: exact condition for K's failure of COMBINATION
        cond = any(w[d] not in pd[d][0] and any(pd[e][3][w[e]] < pd[e][3][b] for b in pd[e][0])
                   for d in range(n) for e in range(n) if d != e)
        Kw = P.K(w)
        check(combination(Kw, w, n) == (not cond), f"Prop2 condition wrong at {w} in {dims}")
        if not cond:
            check(is_box(Kw, P.W, n) and set(Kw) == dk, f"Prop2: K not dimensionwise K at {w}")
        # monotonicity of KM on products
        for w2 in P.W:
            if P.ge(w, w2):
                check(P.KM(w) <= P.KM(w2), f"KM monotonicity fails {w},{w2} in {dims}")
    for name, RK in (("I", P.I), ("K", P.K), ("KM", P.KM), ("MEET", P.MEET)):
        check(P.framework(RK), f"{name} violates framework principles in {dims}")
        if not all(combination(RK(w), w, n) for w in P.W): table[name]["comb_fail"] += 1
        if not P.margins(RK): table[name]["marg_fail"] += 1
    check(P.transitive(P.MEET), f"MEET not transitive in {dims}")
    check(P.transitive(P.K), f"K not transitive in {dims}")

print("structures in which each completion fails COMBINATION / MARGINS (of", n_struct, "):")
for name, t in table.items():
    print(f"  {name:4s}  COMBINATION fails in {t['comb_fail']:5d}   MARGINS fails in {t['marg_fail']:5d}")
check(table["KM"]["comb_fail"] == 0 and table["KM"]["marg_fail"] == 0, "KM table")
check(table["MEET"]["comb_fail"] == 0 and table["MEET"]["marg_fail"] > 0, "MEET table")
check(table["I"]["comb_fail"] > 0 and table["I"]["marg_fail"] == 0, "I table")
check(table["K"]["comb_fail"] > 0 and table["K"]["marg_fail"] > 0, "K table")


# ---------- MEET as the knowledge default once COMBINATION is added ----------
def minimal_comb(P, w, n):
    """Most restrictive set containing RB and w (INDUCTIVE LIMITS, FACTIVITY) and closed
    under COMBINATION at w and under CONVEXITY (upward closure)."""
    R = set(P.RB) | {w}
    while True:
        new = set(R)
        for v in R:
            for d in range(n):
                new.add(tuple(v[d] if j == d else w[j] for j in range(n)))
        new |= {u for u in P.W if any(P.ge(u, v) for v in new)}
        if new == R: return frozenset(R)
        R = new
def minimal_box(P, w, n):
    """Smallest upward-closed product set containing RB and w."""
    proj = [set(v[d] for v in P.RB) | {w[d]} for d in range(n)]
    box = set(itertools.product(*proj))
    return frozenset(u for u in P.W if any(P.ge(u, v) for v in box))
for dims in families:
    n = len(dims); P = product(dims)
    for w in P.W:
        check(minimal_box(P, w, n) == P.MEET(w), f"MEET is not the smallest upward-closed box at {w}")
        if n == 2:
            check(minimal_comb(P, w, n) == P.MEET(w), f"MEET is not the 2-dim knowledge default at {w}")
print("MEET = knowledge default under COMBINATION (2 dims) and under FACTORIZATION (all): checked")

# ---------- Prop 3 under COMPARABILITY: MEET = K on all total preorders, n <= 5 ----------
cnt = 0
for k in range(1, 6):
    for rank, S in (dim_structures(k) if k <= 4 else []):
        st = Struct(list(range(k)), lambda a, b, r=rank: r[a] <= r[b], lambda a, b, S=S: (a, b) in S)
        for w in st.W:
            check(st.MEET(w) == st.K(w), f"MEET != K under comparability: {rank},{S},{w}")
        cnt += 1
# k = 5: sample (full enumeration is large)
for _ in range(3000):
    k = 5
    rank = tuple(random.randrange(5) for _ in range(k))
    lv = sorted(set(rank)); rank = tuple(lv.index(r) for r in rank)
    # >> generated by a threshold on level gaps (always satisfies (i)-(iii)), plus random cut
    gap = random.randint(1, 4)
    S = {(x, y) for x in range(k) for y in range(k) if rank[y] - rank[x] >= gap}
    st = Struct(list(range(k)), lambda a, b, r=rank: r[a] <= r[b], lambda a, b, S=S: (a, b) in S)
    if not st.axioms(): continue
    for w in st.W:
        check(st.MEET(w) == st.K(w), "MEET != K under comparability (k=5 sample)")
    cnt += 1
print("comparable structures checked for MEET = K:", cnt)

# ---------- Figure 4 of Goodman & Salow (p. 119) ----------
fig4dim = ((0, 1, 2), frozenset({(0, 2)}))  # ordinary >> bizarre only
F = product([fig4dim, fig4dim])
def S_(*xs): return frozenset(xs)
sq = S_((0, 0), (0, 1), (1, 0), (1, 1))
check(F.K((0, 2)) == sq | S_((0, 2)), "fig4 K(0,2)")
check(F.KM((0, 2)) == sq | S_((0, 2), (1, 2)), "fig4 KM(0,2)")
check(F.I((0, 2)) == sq | S_((0, 2), (1, 2), (2, 1), (2, 0)), "fig4 I(0,2)")
check(F.K((0, 1)) == sq, "fig4 K(0,1)")
check(F.KM((0, 1)) == sq | S_((0, 2), (1, 2)), "fig4 KM(0,1)")
check(F.I((0, 1)) == sq | S_((0, 2), (1, 2), (2, 0)), "fig4 I(0,1)")
check(F.MEET((0, 2)) == F.KM((0, 2)), "fig4 MEET(0,2) = KM(0,2)")
check(F.MEET((1, 1)) == sq and F.KM((1, 1)) == frozenset(F.W), "fig4 MEET vs KM at (1,1)")
print("figure 4: K(0,2) =", sorted(F.K((0, 2))), "| KM(0,2) =", sorted(F.KM((0, 2))))

# ---------- Probabilist relations (G&S p. 121) ----------
def prob_rel(cells, P, t):
    """cells: answers; P: dict answer->prob. >= by probability; w >> v iff
    P(more normal than v | no more normal than w) >= t."""
    def ge(a, b): return P[a] >= P[b]
    def sm(a, b):
        cond = [x for x in cells if P[x] <= P[a]]
        num = sum(P[x] for x in cond if P[x] > P[b]); den = sum(P[x] for x in cond)
        return den > 0 and num / den >= t
    return ge, sm

def probabilist_check(marg, t, verbose=False):
    n = len(marg)
    dims = []
    for P in marg:
        cells = list(range(len(P)))
        ge, sm = prob_rel(cells, {x: P[x] for x in cells}, t)
        st = Struct(cells, ge, sm)
        check(st.axioms(), f"probabilist per-dimension relations violate (i)-(iii): {P},{t}")
        rank = tuple(sorted(set(-P[x] for x in cells)).index(-P[x]) for x in cells)
        S = frozenset((a, b) for a in cells for b in cells if sm(a, b))
        dims.append((rank, S))
    Prod = product(dims)
    W = Prod.W
    joint = {w: 1 for w in W}
    for w in W:
        for d in range(n): joint[w] *= marg[d][w[d]]
    # single-question contexts: answers = values on dimension d
    ctx = []
    for d in range(n):
        Pd = {w: marg[d][w[d]] for w in W}
        ge, sm = prob_rel(W, Pd, t)
        ctx.append(Struct(W, ge, sm))
    for w in W:
        inter = set(W)
        for c in ctx:
            check(c.KM(w) == c.I(w), "KM != I in a comparable context")
            inter &= set(c.I(w))
        check(set(Prod.KM(w)) == inter, f"Cor4 fails at {w}: {marg},{t}")
    ge, sm = prob_rel(W, joint, t)
    J = Struct(W, ge, sm)
    return Prod, ctx, J

# figure-5 parameters: 0 ten times as probable as 1, 1 ten times as probable as 2; t = .95
m = [Fraction(100, 111), Fraction(10, 111), Fraction(1, 111)]
Prod, ctx, J = probabilist_check([m, m], Fraction(95, 100))
check(Prod.KM((0, 2)) == F.KM((0, 2)) and all(Prod.sm(a, b) == F.sm(a, b) for a in F.W for b in F.W),
      "figure-5 marginals do not reproduce the figure-4 per-dimension relations")
check(J.I((0, 2)) == frozenset(J.W) - {(2, 2)}, "joint context at (0,2)")
check(J.I((0, 0)) == S_((0, 0), (0, 1), (1, 0)), "joint context at (0,0)")
check(J.KM((0, 2)) == J.I((0, 2)), "joint KM = I")
check(all((1, 2) in c.I((0, 2)) for c in ctx + [J]), "some probabilist context excludes (1,2) at (0,2)")
print("joint context: RK(0,0) =", sorted(J.I((0, 0))), "| RK(0,2) excludes",
      sorted(set(J.W) - J.I((0, 2))))
# random independent marginals and thresholds
for _ in range(200):
    n = random.choice([2, 2, 3])
    marg = []
    for d in range(n):
        k = random.choice([2, 3, 4]) if n == 2 else random.choice([2, 3])
        raw = [Fraction(random.randint(1, 30)) for _ in range(k)]
        s = sum(raw); marg.append([x / s for x in raw])
    t = Fraction(random.randint(55, 99), 100)
    probabilist_check(marg, t)
print("random probabilist product models checked: 200")

# ---------- z3 cross-check of Theorem 1 on arbitrary 3x3 structures ----------
try:
    from z3 import Solver, Int, Bool, And, Or, Not, Implies, sat, unsat, BoolVal
    s = Solver(); k = 3
    r = [[Int(f"r{d}_{x}") for x in range(k)] for d in range(2)]
    sd = [[[Bool(f"s{d}_{x}_{y}") for y in range(k)] for x in range(k)] for d in range(2)]
    for d in range(2):
        for x in range(k):
            s.add(r[d][x] >= 0, r[d][x] < k)
            s.add(Not(sd[d][x][x]))
            for y in range(k):
                s.add(Implies(sd[d][x][y], r[d][x] <= r[d][y]))
                for x1 in range(k):
                    for y1 in range(k):
                        s.add(Implies(And(sd[d][x][y], r[d][x1] <= r[d][x], r[d][y] <= r[d][y1]),
                                      sd[d][x1][y1]))
    W = list(itertools.product(range(k), range(k)))
    def GE(a, b): return And(*[r[d][a[d]] <= r[d][b[d]] for d in range(2)])
    def SM(a, b): return And(GE(a, b), Or(*[sd[d][a[d]][b[d]] for d in range(2)]))
    def RB(v): return And(*[Not(SM(u, v)) for u in W])
    def KMacc(w, v): return Or(RB(v), Or(*[And(GE(v, u), GE(w, u), Not(SM(w, u))) for u in W]))
    def FAC(w, v): return And(*[Not(sd[d][w[d]][v[d]]) for d in range(2)])
    s.add(Or(*[KMacc(w, v) != FAC(w, v) for w in W for v in W]))
    res = s.check()
    print("z3: counterexample to Theorem 1 on 3x3 with arbitrary per-dimension relations:", res)
    check(res == unsat, "z3 found a counterexample to Theorem 1")
except ImportError:
    print("z3 not available; skipped")

print()
print("ALL CHECKS PASSED" if not FAIL else f"{len(FAIL)} FAILURES")
sys.exit(1 if FAIL else 0)
