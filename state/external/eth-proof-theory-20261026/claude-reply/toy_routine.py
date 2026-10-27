"""Toy re-implementation of the counting routine in OpenAI's manuscript
"The Exponential Time Hypothesis is False" (17 Oct 2026, rev. 25 Oct 2026),
Sections 3-4, at tiny parameters, over F_p with truncated power series in z.

Purpose: check the *correctness identities* (not the running time):
  * replacement rows P_u(T) with P(0) = delta (Lemma 4.3), M0 = V0 f_I(W0)
    and its measurement representation (Lemma 4.1), the support bound
    (Lemma 4.2), and placement into copies (Section 4.5);
  * separation by fixing group measurements (Lemma 3.2);
  * Taylor coefficients from fixed Boolean substitutions (Lemma 3.3);
  * Hermite interpolation recovering H(0) (Proposition 3.4);
and the ring-valued use of the routine with symbolic weights, which is what
an IPS certificate needs.  All arithmetic is mod a 61-bit prime, so a match at
random points is a Schwartz-Zippel test of the polynomial identity.
"""
import itertools
import math
import random
from fractions import Fraction

P = (1 << 61) - 1


def md(x):
    if isinstance(x, Fraction):
        return x.numerator % P * pow(x.denominator % P, P - 2, P) % P
    return x % P


# ---------------------------------------------------------------- power series
def ps_const(c, J):
    s = [0] * J
    s[0] = c % P
    return s


def ps_add(a, b):
    return [(x + y) % P for x, y in zip(a, b)]


def ps_sub(a, b):
    return [(x - y) % P for x, y in zip(a, b)]


def ps_scale(a, c):
    c %= P
    return [x * c % P for x in a]


def ps_mul(a, b, J):
    res = [0] * J
    for i in range(J):
        ai = a[i]
        if ai:
            for j in range(J - i):
                bj = b[j]
                if bj:
                    res[i + j] = (res[i + j] + ai * bj) % P
    return res


# ---------------------------------------------------------------- factors
class Factor:
    """kind: 'sat'  clause satisfaction indicator 1 - prod(1 - L)
             'viol' clause violation indicator    prod(1 - L)
             'weight' unary weight (1 - X) + y (2X - 1)  (X a field element)
             'one'  constant 1 on its scope"""

    def __init__(self, kind, scope, signs=None, X=None):
        self.kind, self.scope, self.signs, self.X = kind, tuple(scope), signs, X

    def degree(self):
        if self.kind in ('sat', 'viol'):
            return len(self.scope)
        return 1 if self.kind == 'weight' else 0

    def evaluate(self, ins, J):
        if self.kind in ('sat', 'viol'):
            prod = ps_const(1, J)
            one = ps_const(1, J)
            for y, sgn in zip(ins, self.signs):
                L = y if sgn > 0 else ps_sub(one, y)
                prod = ps_mul(prod, ps_sub(one, L), J)
            return prod if self.kind == 'viol' else ps_sub(one, prod)
        if self.kind == 'weight':
            X = self.X % P
            res = ps_scale(ins[0], 2 * X - 1)
            res[0] = (res[0] + 1 - X) % P
            return res
        return ps_const(1, J)


def brute_sum(n, factors):
    """sum over x in {0,1}^n of prod_f Phi_f(x) -- the target value."""
    tot = 0
    for x in itertools.product((0, 1), repeat=n):
        p = 1
        for f in factors:
            p = p * f.evaluate([ps_const(x[v], 1) for v in f.scope], 1)[0] % P
            if not p:
                break
        tot = (tot + p) % P
    return tot


# ---------------------------------------------------------------- design
class Design:
    def __init__(self, n, factors, r=2, Q=4, R=2, A0=None, seed=0):
        rng = random.Random(seed)
        self.n, self.factors, self.r, self.Q, self.R = n, factors, r, Q, R
        if A0 is None:
            mu = Fraction(Q * (r - 1), 2 * r)
            A0 = max(0, min(Q - R + 1, math.ceil(mu - Fraction(R - 1, 2))))
        assert 0 <= A0 and A0 + R - 1 <= Q
        self.I = set(range(A0, A0 + R))
        seqs = list(itertools.product(range(r), repeat=Q))
        self.labels = [(a, d) for a in seqs for d in seqs]
        self.lab_index = {u: i for i, u in enumerate(self.labels)}
        self.Dsize = len(self.labels)

        # f_I from (4.7): (-1)^A0 sum_j (-2)^j binom(z - A0, j)
        def fI(z):
            tot = Fraction(0)
            for j in range(R):
                b = Fraction(1)
                for a in range(j):
                    b *= (z - A0 - a)
                tot += (-2) ** j * b / math.factorial(j)
            return (-1) ** A0 * tot
        self.fvals = [fI(z) for z in range(Q + 1)]
        for j in self.I:
            assert self.fvals[j] == (-1) ** j

        # M0 = V0 f_I(W0) expanded into permutations prod_{s not in T} Pi_s
        diffs, vals = [], self.fvals[:]
        for _ in range(Q + 1):
            diffs.append(vals[0])
            vals = [vals[k + 1] - vals[k] for k in range(len(vals) - 1)]
        gam = {}
        for tp in range(R):
            g = Fraction(0)
            for sp in range(tp, R):
                g += math.comb(Q - tp, sp - tp) * diffs[sp] / 2 ** sp
            gam[tp] = (-1) ** tp * g
        self.M0 = []
        for (a, d) in self.labels:
            row = {}
            for tp in range(R):
                for T in itertools.combinations(range(Q), tp):
                    Ts = set(T)
                    a2 = tuple(a[s] if s in Ts else d[s] for s in range(Q))
                    d2 = tuple(d[s] if s in Ts else a[s] for s in range(Q))
                    y = self.lab_index[(a2, d2)]
                    row[y] = row.get(y, Fraction(0)) + gam[tp]
            self.M0.append({y: c for y, c in row.items() if c != 0})

        # product eigenbasis (Lemma 4.1)
        pos = []
        for al in range(r):
            pos.append(({(al, al): 1}, 1, 1))
        for al in range(r):
            for de in range(al + 1, r):
                pos.append(({(al, de): 1, (de, al): 1}, 1, 2))
                pos.append(({(al, de): 1, (de, al): -1}, -1, 2))
        self.psis = []
        for choice in itertools.product(range(len(pos)), repeat=Q):
            j = sum(1 for c in choice if pos[c][1] == -1)
            norm2 = 1
            for c in choice:
                norm2 *= pos[c][2]
            supp = {}
            for combo in itertools.product(*[list(pos[c][0].items()) for c in choice]):
                a = tuple(pr[0][0] for pr in combo)
                d = tuple(pr[0][1] for pr in combo)
                val = 1
                for pr in combo:
                    val *= pr[1]
                supp[self.lab_index[(a, d)]] = val
            lam = (-1) ** j * self.fvals[j]
            self.psis.append(dict(j=j, norm2=norm2, supp=supp, lam=lam))
        self.meas = [k for k, ps in enumerate(self.psis) if ps['j'] not in self.I]
        self.kappa = {k: (1 - self.psis[k]['lam']) / self.psis[k]['norm2'] for k in self.meas}
        self.psi_at = {}            # label -> [(psi index, value)] over measured psi
        for k in self.meas:
            for u, val in self.psis[k]['supp'].items():
                self.psi_at.setdefault(u, []).append((k, val))

        # M0 row data with mismatch sets E_{u,y} (positions s=0..Q-1 <-> points 1..Q)
        self.M0rows = []
        for ui, (a, d) in enumerate(self.labels):
            lst = []
            for y, c in self.M0[ui].items():
                ay = self.labels[y][0]
                E = [s for s in range(Q) if ay[s] != d[s]]
                lst.append((y, c, E))
            self.M0rows.append(lst)

        # placement (Section 4.4-4.5), random schedules (balance only affects cost)
        self.a = {v: tuple(rng.randrange(r) for _ in range(Q)) for v in range(n)}
        self.d = {fi: tuple(rng.randrange(r) for _ in range(Q)) for fi in range(len(factors))}
        count, self.pos = {}, {}
        for fi, f in enumerate(factors):
            for v in f.scope:
                u = self.lab_index[(self.a[v], self.d[fi])]
                c = count.get(u, 0)
                count[u] = c + 1
                self.pos[(fi, v)] = (c, u)
        self.h = max(count.values())
        self.occ = {cu: v for (fi, v), cu in self.pos.items()}
        # measurement linear forms m_{c,psi}(x) = sum over occupied positions
        self.mform = {}
        for (c, u), v in self.occ.items():
            for k, val in self.psi_at.get(u, []):
                fm = self.mform.setdefault((c, k), {})
                fm[v] = fm.get(v, 0) + val
        self.mkeys = sorted(self.mform)
        self.d_total = sum(f.degree() for f in factors)

    # ---- checks of the construction
    def check_construction(self):
        Q, R = self.Q, self.R
        # Lemma 4.1: M0 psi = lam psi on the whole eigenbasis
        for ps in self.psis:
            for u in range(self.Dsize):
                lhs = sum(c * ps['supp'].get(y, 0) for y, c in self.M0[u].items())
                assert lhs == ps['lam'] * ps['supp'].get(u, 0)
        # measurement representation of (I - M0)
        for u in range(self.Dsize):
            acc = {}
            for k, val in self.psi_at.get(u, []):
                for y, vy in self.psis[k]['supp'].items():
                    acc[y] = acc.get(y, 0) + self.kappa[k] * val * vy
            target = {u: Fraction(1)}
            for y, c in self.M0[u].items():
                target[y] = target.get(y, 0) - c
            keys = set(acc) | set(target)
            assert all(acc.get(y, 0) == target.get(y, 0) for y in keys)
        # Lemma 4.2 support bound
        for lst in self.M0rows:
            for (y, c, E) in lst:
                assert len(E) <= R - 1
        return dict(D=self.Dsize, measured_rows_per_copy=len(self.meas), copies=self.h,
                    max_M0_row=max(len(r) for r in self.M0))

    # ---- replacement forms
    def phi_series(self, E, t, J):
        """phi_E(t + z) as a power series in z (points are 1-based)."""
        s = ps_const(1, J)
        for pos_ in E:
            sp = pos_ + 1
            term = [0] * J
            term[0] = md(Fraction(sp - t, sp))
            if J > 1:
                term[1] = md(Fraction(-1, sp))
            s = ps_mul(s, term, J)
        return s

    def phi_val(self, E, t):
        v = Fraction(1)
        for pos_ in E:
            v *= 1 - Fraction(t, pos_ + 1)
        return v

    def form_direct(self, fi, v, t, J, x):
        """<P_{f,v}(t+z), x> for an arbitrary field vector x, from the dense row
        P_u(T) zeta = zeta_u + sum_y M0[u,y] (phi_{u,y}(T) - 1) zeta_y."""
        c, u = self.pos[(fi, v)]
        res = ps_const(x[v], J)
        for (y, coef, E) in self.M0rows[u]:
            w = self.occ.get((c, y))
            if w is None:
                continue
            ph = self.phi_series(E, t, J)
            ph[0] = (ph[0] - 1) % P
            res = ps_add(res, ps_scale(ph, md(coef) * x[w]))
        return res

    def delta_part(self, fi, v, t, J, U):
        """<Delta P_{f,v}(z), 1_U>: only the phi terms depend on T."""
        c, u = self.pos[(fi, v)]
        res = [0] * J
        for (y, coef, E) in self.M0rows[u]:
            w = self.occ.get((c, y))
            if w is None or w not in U:
                continue
            ph = self.phi_series(E, t, J)
            ph[0] = 0
            res = ps_add(res, ps_scale(ph, md(coef)))
        return res

    def separated_pieces(self, fi, v, t):
        """At T = t: local linear form (on the factor's assigned group) and the
        coefficients on other groups' measurement entries (Definition 3.1 (4))."""
        c, u = self.pos[(fi, v)]
        g = self.d[fi][t - 1]
        local = {}
        meas_coef = {}
        for k, val in self.psi_at.get(u, []):
            coef = self.kappa[k] * val
            for w, mc in self.mform.get((c, k), {}).items():
                if self.a[w][t - 1] == g:
                    local[w] = local.get(w, 0) + coef * mc
            meas_coef[(c, k)] = meas_coef.get((c, k), 0) + coef
        for (y, coef, E) in self.M0rows[u]:
            w = self.occ.get((c, y))
            if w is None:
                continue
            ph = self.phi_val(E, t)
            if ph == 0:
                continue
            assert self.a[w][t - 1] == g, "surviving term outside the assigned group"
            local[w] = local.get(w, 0) + coef * ph
        return g, {w: md(cf) for w, cf in local.items() if cf != 0}, \
            {key: md(cf) for key, cf in meas_coef.items() if cf != 0}

    # ---- Lemma 3.2: Z_{t,E,U} by separation
    def Z_separated(self, t, J, E, U, pieces=None):
        n, r = self.n, self.r
        groups = [[v for v in range(n) if self.a[v][t - 1] == g] for g in range(r)]
        if pieces is None:
            pieces = {(fi, v): self.separated_pieces(fi, v, t)
                      for fi, f in enumerate(self.factors) for v in f.scope}
        # group measurement vectors: all rows (c,psi), restricted to the group
        rows_g = []
        for g in range(r):
            Sg = set(groups[g])
            rows_g.append([(key, [(w, cf) for w, cf in self.mform[key].items() if w in Sg])
                           for key in self.mkeys])
        buckets = []
        for g in range(r):
            Sg = groups[g]
            b = {}
            for bits in itertools.product((0, 1), repeat=len(Sg)):
                xg = dict(zip(Sg, bits))
                key = tuple(sum(cf * xg[w] for w, cf in lst) for _, lst in rows_g[g])
                b.setdefault(key, []).append(xg)
            buckets.append(b)
        fac_g = [[fi for fi in range(len(self.factors)) if self.d[fi][t - 1] == g]
                 for g in range(r)]
        dparts = {(fi, v): self.delta_part(fi, v, t, J, U)
                  for fi, f in enumerate(self.factors) for v in f.scope}
        keyindex = {key: i for i, key in enumerate(self.mkeys)}
        Ecap = [set(E) & set(groups[g]) for g in range(r)]
        total = [0] * J
        for combo in itertools.product(*[list(b.keys()) for b in buckets]):
            prod_groups = ps_const(1, J)
            for g in range(r):
                Sg_sum = [0] * J
                for xg in buckets[g][combo[g]]:
                    if any(xg[w] != 1 for w in Ecap[g]):
                        continue
                    A = ps_const(1, J)
                    for fi in fac_g[g]:
                        f = self.factors[fi]
                        ins = []
                        for v in f.scope:
                            gg, local, mcoef = pieces[(fi, v)]
                            val = sum(cf * xg[w] for w, cf in local.items())
                            for key, cf in mcoef.items():
                                ki = keyindex[key]
                                for h in range(r):
                                    if h != g:
                                        val += cf * combo[h][ki]
                            s = dparts[(fi, v)][:]
                            s[0] = (s[0] + val) % P
                            ins.append(s)
                        A = ps_mul(A, f.evaluate(ins, J), J)
                    Sg_sum = ps_add(Sg_sum, A)
                prod_groups = ps_mul(prod_groups, Sg_sum, J)
            total = ps_add(total, prod_groups)
        return total

    def Z_brute(self, t, J, E, U):
        n = self.n
        total = [0] * J
        dparts = {(fi, v): self.delta_part(fi, v, t, J, U)
                  for fi, f in enumerate(self.factors) for v in f.scope}
        for x in itertools.product((0, 1), repeat=n):
            if any(x[w] != 1 for w in E):
                continue
            G = ps_const(1, J)
            for fi, f in enumerate(self.factors):
                ins = []
                for v in f.scope:
                    s = self.form_direct(fi, v, t, 1, x)
                    s = [s[0]] + [0] * (J - 1)
                    ins.append(ps_add(s, dparts[(fi, v)]))
                G = ps_mul(G, f.evaluate(ins, J), J)
            total = ps_add(total, G)
        return total

    def H_brute(self, t, J):
        """H(t+z) mod z^J directly: sum_x prod_f Phi_f(<P(t+z), x>)."""
        total = [0] * J
        for x in itertools.product((0, 1), repeat=self.n):
            G = ps_const(1, J)
            for fi, f in enumerate(self.factors):
                ins = [self.form_direct(fi, v, t, J, x) for v in f.scope]
                G = ps_mul(G, f.evaluate(ins, J), J)
            total = ps_add(total, G)
        return total

    def params(self):
        dH = self.d_total * (self.R - 1)
        q = dH // self.Q
        return dH, q, q + 1

    def taylor_data(self, t, J, q, separated=True):
        n = self.n
        pieces = {(fi, v): self.separated_pieces(fi, v, t)
                  for fi, f in enumerate(self.factors) for v in f.scope} if separated else None
        total = [0] * J
        for size in range(0, min(q, n) + 1):
            for E in itertools.combinations(range(n), size):
                for usize in range(0, size + 1):
                    for U in itertools.combinations(E, usize):
                        Z = (self.Z_separated(t, J, E, set(U), pieces) if separated
                             else self.Z_brute(t, J, E, set(U)))
                        sign = 1 if (size - usize) % 2 == 0 else P - 1
                        total = ps_add(total, ps_scale(Z, sign))
        return total

    def count(self, separated=True):
        dH, q, J = self.params()
        data = {t: self.taylor_data(t, J, q, separated) for t in range(1, self.Q + 1)}
        return hermite_h0(data, self.Q, J)


def hermite_h0(data, Q, J):
    """H has degree < Q*J; data[t][j] = [z^j] H(t + z).  Return H(0)."""
    N = Q * J
    A, b = [], []
    for t in range(1, Q + 1):
        for j in range(J):
            A.append([math.comb(k, j) * pow(t, k - j, P) % P if k >= j else 0 for k in range(N)])
            b.append(data[t][j] % P)
    # Gaussian elimination mod P
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    col = 0
    for col in range(N):
        piv = next(i for i in range(col, N) if M[i][col] % P)
        M[col], M[piv] = M[piv], M[col]
        inv = pow(M[col][col], P - 2, P)
        M[col] = [x * inv % P for x in M[col]]
        for i in range(N):
            if i != col and M[i][col]:
                f = M[i][col]
                M[i] = [(x - f * y) % P for x, y in zip(M[i], M[col])]
    return M[0][N] % P
