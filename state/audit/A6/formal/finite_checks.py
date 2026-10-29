#!/usr/bin/env python3
"""Independent audit of the finite claims in state/drafts/A6/v4.md.

Self-contained. Enumerates every statist, comparable normality structure on
n <= 4 labelled states (total preorder >= ; relation >> filtered by the axioms:
irreflexive, implies >=, chaining), every non-empty body of evidence E (all
non-empty subsets), every situation x in E and every partition of E.

Checks (exact rational arithmetic where a construction is verified):
  Lemma 3; Theorem 1(a) both directions (Lemma-2 hypotheses structurally +
  random problems; Lemma-1 bet explicitly); Theorem 1(b); Lemma 4; Theorem 2 for
  K, I, KM, JTB, iterated-K, iterated-I and random factive B-containing
  assignments; 'gapped set containing x contains C(x)'; Corollary (i) and (ii);
  Theorem 3 construction (A.6 recipe); CKD silence (A.7); Proposition 4 (random
  problems + structural); Proposition 5 construction; VER escapes the Theorem-3
  family for large L; KK / No Defeat facts used in 6.1.
Run: python3 finite_checks.py  (about 1-3 minutes)
"""
import itertools, random
from fractions import Fraction as Fr

random.seed(20261029)

# ---------------------------------------------------------------- structures
def total_preorders(n):
    for k in range(1, n + 1):
        for lv in itertools.product(range(k), repeat=n):
            if set(lv) == set(range(k)):
                yield lv

def chaining_ok(geq, gg, n):
    for w2 in range(n):
        for w3 in range(n):
            if gg[w2][w3]:
                for w1 in range(n):
                    if geq[w1][w2]:
                        for w4 in range(n):
                            if geq[w3][w4] and not gg[w1][w4]:
                                return False
    return True

def structures(n, candidate_pairs="strict"):
    for lv in total_preorders(n):
        geq = [[lv[u] <= lv[v] for v in range(n)] for u in range(n)]
        if candidate_pairs == "strict":
            cand = [(u, v) for u in range(n) for v in range(n) if geq[u][v] and not geq[v][u]]
        else:  # every pair, axioms filter everything (used as a sanity check)
            cand = [(u, v) for u in range(n) for v in range(n)]
        for bits in range(1 << len(cand)):
            gg = [[False] * n for _ in range(n)]
            for i, (u, v) in enumerate(cand):
                if bits >> i & 1:
                    gg[u][v] = True
            if any(gg[u][u] for u in range(n)):
                continue
            if any(gg[u][v] and not geq[u][v] for u in range(n) for v in range(n)):
                continue
            if chaining_ok(geq, gg, n):
                yield geq, gg

def set_partitions(lst):
    if not lst:
        yield []
        return
    first, rest = lst[0], lst[1:]
    for p in set_partitions(rest):
        yield [[first]] + p
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]

def nonempty_subsets(n):
    for r in range(1, n + 1):
        for c in itertools.combinations(range(n), r):
            yield frozenset(c)

# ------------------------------------------------------------- epistemics
class Model:
    def __init__(self, n, geq, gg):
        self.n, self.geq, self.gg = n, geq, gg
    def B(self, F):
        return frozenset(s for s in F if not any(self.gg[u][s] for u in F))
    def K(self, F, x):
        return self.B(F) | frozenset(v for v in F if self.geq[v][x])
    def I(self, F, x):
        return frozenset(v for v in F if not self.gg[x][v])
    def KM(self, F, x):
        return self.B(F) | frozenset(v for v in F if any(
            self.geq[v][u] and self.geq[x][u] and not self.gg[x][u] for u in F))
    def JTB(self, F, x):
        return self.B(F) | frozenset([x])
    def KK(self, F, x):
        out = frozenset()
        for t in self.K(F, x):
            out |= self.K(F, t)
        return out
    def II(self, F, x):
        out = frozenset()
        for t in self.I(F, x):
            out |= self.I(F, t)
        return out
    def condK(self, E, D, x):          # K^D_E(x) of section 5.1
        ED = E & D
        return frozenset(v for v in ED if not any(self.gg[u][v] for u in ED)) | \
               frozenset(v for v in ED if self.geq[v][x])
    def gapped(self, Mset, E):
        return all(self.gg[m][v] for m in Mset for v in E - Mset)
    def p_v(self, E, v):
        return frozenset(u for u in E if not self.gg[u][v])
    def Cx(self, E, x):
        reach, frontier = {x}, [x]
        while frontier:
            t = frontier.pop()
            for v in E:
                if v not in reach and not self.gg[t][v]:
                    reach.add(v); frontier.append(v)
        return frozenset(reach)

def cell_of(Pi, s):
    for c in Pi:
        if s in c:
            return c
    raise ValueError

def rel_defeat_witnesses(Mrule, E, x, Pi):
    Mx = Mrule(E, x)
    return [s for s in Mx if not Mrule(E & cell_of(Pi, s), s) <= Mx]

# --------------------------------------------------------- decision theory
def ev(P, u, F):
    tot = sum(P[s] for s in F)
    return sum(P[s] * u[s] for s in F) / tot

def choose(P, acts, F):
    best, bi = None, None
    for i, a in enumerate(acts):
        e = ev(P, a, F)
        if best is None or e > best:
            best, bi = e, i
    return bi

def policy(m, Mrule, P, acts, E, Pi):
    return {s: choose(P, acts, Mrule(E & cell_of(Pi, s), s)) for s in E}

def value(m, Mrule, P, acts, E, x, Pi):
    Mx = Mrule(E, x)
    pol = policy(m, Mrule, P, acts, E, Pi)
    ul = {s: acts[pol[s]][s] for s in E}
    return ev(P, ul, Mx) - max(ev(P, a, Mx) for a in acts), pol, ul

def ceu_diff(m, P, E, x, ul, a):
    D = frozenset(s for s in E if ul[s] != a[s])
    if not D:
        return 0, D, frozenset()
    KD = m.condK(E, D, x)
    return ev(P, {s: ul[s] - a[s] for s in E}, KD), D, KD

def ver_sum(m, P, E, x, pol, acts, a):
    Kx = m.K(E, x)
    tot = sum(P[s] for s in Kx)
    out = 0
    for b in set(pol.values()):
        Db = frozenset(s for s in E if pol[s] == b)
        w = sum(P[s] for s in Db & Kx) / tot
        if w == 0:
            continue
        KD = m.condK(E, Db, x)
        out += w * ev(P, {s: acts[b][s] - a[s] for s in E}, KD)
    return out

def ans_sum(m, P, E, x, Pi, ul, a, kappa=0):
    Kx = m.K(E, x)
    tot = sum(P[s] for s in Kx)
    out = 0
    for c in Pi:
        w = sum(P[s] for s in Kx & frozenset(c)) / tot
        if w == 0:
            continue
        Kc = m.condK(E, frozenset(c), x)
        out += w * ev(P, {s: ul[s] - kappa - a[s] for s in E}, Kc)
    return out

def rand_prior(n):
    return [Fr(random.randint(1, 9), 1) for _ in range(n)]

def rand_acts(n, k):
    return [[Fr(random.randint(-20, 20), random.randint(1, 4)) for _ in range(n)] for _ in range(k)]

def lemma2_hyp(m, Mrule, E, Mset, Pi):
    """Lemma-2 hypotheses for the post-answer states {M'(s): s in Mset}."""
    fam = {s: Mrule(E & cell_of(Pi, s), s) for s in Mset}
    for s, F in fam.items():
        if not F <= Mset or s not in F:
            return False
        for t in F:
            if not fam[t] <= F:
                return False
    vals = list(fam.values())
    for F in vals:
        for G in vals:
            if F & G and not (F <= G or G <= F):
                return False
    return True

# ================================================================== main
def main():
    out = []
    pr = lambda *a: out.append(" ".join(str(x) for x in a))

    # sanity: restricting >> to strict pairs loses nothing (n <= 3, full filter)
    for n in range(1, 4):
        a = sorted((str(g), str(h)) for g, h in structures(n, "strict"))
        b = sorted((str(g), str(h)) for g, h in structures(n, "all"))
        assert a == b, n
    pr("sanity: >> among strict pairs only == full axiom filter for n<=3: OK")

    C = dict(structs=0, pairs=0, rd=0, pairs_ES=0, rd_ES=0)
    fails = dict()
    def fail(key, info):
        fails.setdefault(key, []).append(info)

    thm3_cases = ceu_now = kdt_neg = ver_now_thm3 = ver_escape = exc_in_dec = 0
    prop5_ok = silence_ok = 0
    nodefeat_rand_neg = ans_rand_neg = silence_rand_bad = 0
    nodefeat_rand_tests = ans_rand_tests = silence_rand_tests = 0
    collapse_structs = 0
    for n in range(1, 5):
        for geq, gg in structures(n):
            C["structs"] += 1
            m = Model(n, geq, gg)
            collapse = all(gg[u][v] for u in range(n) for v in range(n) if geq[u][v] and not geq[v][u])
            collapse_structs += collapse
            rules = dict(K=m.K, I=m.I, KM=m.KM, JTB=m.JTB, KK=m.KK, II=m.II)
            # random factive, B-containing assignment, fixed per structure
            rmap = {}
            for F in nonempty_subsets(n):
                for s in F:
                    extra = frozenset(v for v in F if random.random() < 0.4)
                    rmap[(F, s)] = m.B(F) | {s} | extra
            rules["RAND"] = lambda F, s, rmap=rmap: rmap[(F, s)]
            for E in nonempty_subsets(n):
                # Lemma 3
                kens = {s: m.K(E, s) for s in E}
                for s in E:
                    if s not in kens[s]: fail("L3-refl", (geq, gg, E, s))
                    for t in kens[s]:
                        if not kens[t] <= kens[s]: fail("L3-trans", (geq, gg, E, s, t))
                for s in E:
                    for t in E:
                        if not (kens[s] <= kens[t] or kens[t] <= kens[s]): fail("L3-nest", (geq, gg, E))
                Bset = m.B(E)
                for x in E:
                    # 'leaves open what rational belief leaves open' + factivity
                    for nm_, R in rules.items():
                        if not (Bset <= R(E, x) and x in R(E, x)): fail("leaves-open-" + nm_, (E, x))
                    Kx = kens[x]
                    gapK = m.gapped(Kx, E)
                    if collapse and not gapK: fail("Cor(i)", (geq, gg, E, x))
                    # K-normality KK; I / KM KK failures recorded
                    # Theorem 2 / Lemma 4 for every rule
                    for nm_, R in rules.items():
                        Mx = R(E, x)
                        if not m.gapped(Mx, E):
                            found = False
                            for mm in Mx:
                                for v in E - Mx:
                                    if not gg[mm][v]:
                                        pv = m.p_v(E, v)
                                        assert mm in pv and v in pv and v in m.B(pv)  # Lemma 4
                                        Pi = [sorted(pv)] + ([sorted(E - pv)] if E - pv else [])
                                        if rel_defeat_witnesses(R, E, x, Pi):
                                            found = True
                                        else:
                                            fail("Thm2-every-v-" + nm_, (geq, gg, E, x, v))
                            if not found: fail("Thm2-" + nm_, (geq, gg, E, x))
                    # gapped set containing x contains C(x): all subsets
                    Cx = m.Cx(E, x)
                    for r in range(1, len(E) + 1):
                        for Ms in itertools.combinations(sorted(E), r):
                            Ms = frozenset(Ms)
                            if x in Ms and m.gapped(Ms, E) and not Cx <= Ms:
                                fail("gapped-contains-C(x)", (E, x, Ms))
                    # Corollary (ii): graded E, factive B-containing state != E -> some p_v unsafe
                    graded = all(m.Cx(E, y) == E for y in E)
                    if graded:
                        for nm_, R in rules.items():
                            Mx = R(E, x)
                            if Mx != E:
                                ok = False
                                for v in E - Mx:
                                    pv = m.p_v(E, v)
                                    Pi = [sorted(pv)] + ([sorted(E - pv)] if E - pv else [])
                                    if rel_defeat_witnesses(R, E, x, Pi): ok = True
                                if not ok: fail("Cor(ii)-" + nm_, (geq, gg, E, x))
                    # No Defeat for I and KM (statism+comparability+Margins); KK at x
                    for nm_, R in (("I", m.I), ("KM", m.KM)):
                        for r in range(1, len(E) + 1):
                            for p in itertools.combinations(sorted(E), r):
                                p = frozenset(p)
                                if x in p and not R(E & p, x) <= R(E, x):
                                    fail("NoDefeat-" + nm_, (E, x, p))
                    for s in Kx:   # K-normality: KK (transitivity) always
                        if not m.K(E, s) <= Kx: fail("KK-K", (E, x))
                    # ---------------------------------------------- questions
                    for Pi in set_partitions(sorted(E)):
                        C["pairs"] += 1
                        if E == frozenset(range(n)): C["pairs_ES"] += 1
                        W = rel_defeat_witnesses(m.K, E, x, Pi)
                        # Theorem 1(b) first half: gapped -> no relative defeat
                        if gapK and W: fail("Thm1b-gapped", (E, x, Pi))
                        # Margins completions: any relative defeat is a KK failure at x
                        for nm_, R in (("I", m.I), ("KM", m.KM)):
                            if rel_defeat_witnesses(R, E, x, Pi):
                                Mx = R(E, x)
                                if all(R(E, s) <= Mx for s in Mx): fail("RD-not-KKfail-" + nm_, (E, x, Pi))
                        if not W:
                            # Theorem 1(a) 'if': Lemma-2 hypotheses + random problems
                            if not lemma2_hyp(m, m.K, E, Kx, Pi): fail("Thm1a-L2hyp", (E, x, Pi))
                            if random.random() < 0.15:
                                P = rand_prior(n); acts = rand_acts(n, random.randint(2, 4))
                                V, pol, ul = value(m, m.K, P, acts, E, x, Pi)
                                nodefeat_rand_tests += 1
                                if V < 0: nodefeat_rand_neg += 1; fail("Thm1a-if", (E, x, Pi))
                        # Proposition 4: structural + random
                        for c in Pi:
                            Kc = m.condK(E, frozenset(c), x)
                            for s in Kc:
                                if not m.K(E & frozenset(c), s) <= Kc: fail("Prop4-incl", (E, x, Pi))
                        if random.random() < 0.15:
                            P = rand_prior(n); acts = rand_acts(n, random.randint(2, 4))
                            V, pol, ul = value(m, m.K, P, acts, E, x, Pi)
                            for a in acts:
                                ans_rand_tests += 1
                                if ans_sum(m, P, E, x, Pi, ul, a) < 0:
                                    ans_rand_neg += 1; fail("Prop4-rand", (E, x, Pi))
                            # CKD silence (A.7): look differs from a everywhere -> look beats a somewhere in K
                            for a in acts:
                                if all(ul[s] != a[s] for s in E):
                                    silence_rand_tests += 1
                                    if not any(ul[s] > a[s] for s in Kx):
                                        silence_rand_bad += 1; fail("silence-rand", (E, x, Pi))
                        if not W:
                            continue
                        C["rd"] += 1
                        if E == frozenset(range(n)): C["rd_ES"] += 1
                        # ---------------- Theorem 3 construction (A.6), two priors
                        for P in ([Fr(1)] * n, rand_prior(n)):
                            M = Kx
                            s0 = W[0]
                            PM = sum(P[s] for s in M)
                            Ps0 = P[s0] / PM
                            N = int(2 / Ps0) + 1
                            assert N * Ps0 > 2
                            eps = Fr(1, 2)
                            postkens = {s: m.K(E & frozenset(cell_of(Pi, s)), s) for s in E}
                            meet = [F for F in set(postkens.values()) if F - M]
                            qmin = min(sum(P[s] for s in F - M) / sum(P[s] for s in F) for F in meet)
                            L = (1 + N) / qmin + 1
                            beta = [Fr(1) if s in M else -L for s in range(n)]
                            dec = [Fr(0)] * n
                            zeta = [Fr(N) if s == s0 else Fr(-1) for s in range(n)]
                            beta1 = [beta[s] + eps * zeta[s] for s in range(n)]
                            acts = [beta, dec, beta1]
                            thm3_cases += 1
                            # every other post-answer ken excludes s0
                            for F in set(postkens.values()):
                                if not (F - M) and s0 in F: fail("Thm3-excl-s0", (E, x, Pi))
                            # beta1 uniquely optimal now
                            evs = [ev(P, a, M) for a in acts]
                            if not (evs[2] > evs[0] and evs[2] > evs[1]): fail("Thm3-unique", (E, x, Pi))
                            V, pol, ul = value(m, m.K, P, acts, E, x, Pi)
                            if any(pol[s] == 2 for s in E): fail("Thm3-look-selects-beta1", (E, x, Pi))
                            # strict choices after the answer (no ties anywhere)
                            for s in E:
                                F = postkens[s]
                                e = sorted(ev(P, a, F) for a in acts)
                                if e[-1] == e[-2]: fail("Thm3-tie", (E, x, Pi))
                            if V < 0: kdt_neg += 1
                            else: fail("Thm3-KDT", (E, x, Pi))
                            # all pairwise differences everywhere (now and later)
                            for a, b in itertools.combinations(acts, 2):
                                if any(a[s] == b[s] for s in E): fail("Thm3-pairdiff", (E, x, Pi))
                            if any(ul[s] == beta1[s] for s in E): fail("Thm3-lookdiff", (E, x, Pi))
                            d, D, KD = ceu_diff(m, P, E, x, ul, beta1)
                            if D != E or KD != M: fail("Thm3-D", (E, x, Pi))
                            if d < 0: ceu_now += 1
                            else: fail("Thm3-CEU", (E, x, Pi))
                            # A.6 inequality P(u_b1 - u_l) >= P(s0)(1+eps N) - eps > 0
                            if not (-d >= Ps0 * (1 + eps * N) - eps > 0): fail("A6-ineq", (E, x, Pi))
                            # CKD silence in the construction: m* post-ken inside K, excludes s0, look=beta there
                            mstar = [s for s in E if all(geq[s][t] for t in E)][0]
                            Fm = postkens[mstar]
                            if not (Fm <= M and s0 not in Fm and pol[mstar] == 0): fail("Thm3-silence", (E, x, Pi))
                            silence_ok += 1
                            # VER with this L, and with large L
                            if ver_sum(m, P, E, x, pol, acts, beta1) < 0: ver_now_thm3 += 1
                            Dd = frozenset(s for s in E if pol[s] == 1)
                            if m.condK(E, Dd, x) - M: exc_in_dec += 1
                            else: fail("VER-dec-ken-no-excluded", (E, x, Pi))
                            Lb = L * 1000
                            beta_b = [Fr(1) if s in M else -Lb for s in range(n)]
                            beta1_b = [beta_b[s] + eps * zeta[s] for s in range(n)]
                            acts_b = [beta_b, dec, beta1_b]
                            Vb, polb, ulb = value(m, m.K, P, acts_b, E, x, Pi)
                            if ver_sum(m, P, E, x, polb, acts_b, beta1_b) > 0: ver_escape += 1
                            else: fail("VER-escape", (E, x, Pi))
                            # ---------------- Proposition 5 (A.7)
                            c0 = frozenset(cell_of(Pi, s0))
                            Kc0 = m.condK(E, c0, x)
                            q = sum(P[s] for s in Kc0 - M) / sum(P[s] for s in Kc0)
                            if q <= 0:
                                fail("Prop5-q", (E, x, Pi)); continue
                            L5 = max(L, 2 / q) + 1     # Lemma-1 bet with L large enough
                            beta2 = [Fr(1) if s in M else -L5 for s in range(n)]
                            acts5 = [beta2, dec]
                            V5, pol5, ul5 = value(m, m.K, P, acts5, E, x, Pi)
                            wc0 = sum(P[s] for s in M & c0) / PM
                            bound = wc0 * (L5 * q - 1)
                            if bound <= 0:
                                fail("Prop5-bound", (E, x, Pi)); continue
                            kappa = bound / 2
                            a5 = ans_sum(m, P, E, x, Pi, ul5, beta2, kappa)
                            differ = all(ul5[s] - kappa != beta2[s] for s in E)
                            dominated = all(beta2[s] > ul5[s] - kappa for s in M)
                            DD = frozenset(s for s in E if ul5[s] - kappa != beta2[s])
                            if a5 > 0 and differ and dominated and m.condK(E, DD, x) == M:
                                prop5_ok += 1
                            else:
                                fail("Prop5", (E, x, Pi))
                    # Theorem 1(b) second half: not gapped -> p_v question has relative defeat (in Thm2 loop)
    pr("structures (labelled, n<=4):", C["structs"], "; of which satisfy COLLAPSE:", collapse_structs)
    pr("situation-question pairs, every E:", C["pairs"], "; with relative defeat:", C["rd"])
    pr("situation-question pairs, E = whole S only:", C["pairs_ES"], "; with relative defeat:", C["rd_ES"])
    pr("Thm1(a) 'if': random problems tested on no-defeat pairs:", nodefeat_rand_tests, "; negative:", nodefeat_rand_neg)
    pr("Prop 4: random (problem, act) tests:", ans_rand_tests, "; ANS negative:", ans_rand_neg)
    pr("A.7 silence: random tests with look differing everywhere:", silence_rand_tests, "; violations:", silence_rand_bad)
    pr("Theorem 3 constructions (2 priors x relative-defeat pairs):", thm3_cases,
       "; KDT negative:", kdt_neg, "; CEU prefers acting now:", ceu_now)
    pr("  CKD silent in construction:", silence_ok, "; VER prefers acting now with A.6's L:", ver_now_thm3,
       "; conditional ken on 'decline' contains an excluded state:", exc_in_dec,
       "; VER prefers looking with 1000L:", ver_escape)
    pr("Prop 5 constructions verified:", prop5_ok)
    pr("failures by check:", {k: len(v) for k, v in fails.items()} or "none")
    for k, v in fails.items():
        pr("  first failure", k, v[0])
    print("\n".join(out))

if __name__ == "__main__":
    main()
