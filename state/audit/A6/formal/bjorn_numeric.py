#!/usr/bin/env python3
"""Independent numerics for Bjorn's second weighing (A6 v4, sections 3, 5.1, 5.3, 6.2, A.5).

Model (Goodman & Salow 2023, sec. 6; swamped prior): scale errors e1, e2 iid N(0,1)
(unit = s.d.).  mu=(e1+e2)/2 ~ N(0,1/2), d=e1-e2 ~ N(0,2), independent;
delta = e1^2+e2^2 = 2mu^2 + d^2/2.  v >= u iff delta(v) <= delta(u);
u >> v iff delta(u) + c^2 < delta(v).
After reading 1 the ken at x is {delta <= max(c^2, delta(x))}; a second reading fixes d,
and the post-answer ken of s is {|mu| <= max(c/sqrt2, |mu_s|)} on that d-slice.
Bet: +1 if |e1| <= c (e1 = mu + d/2), -L otherwise.
Only numpy and math are used (no scipy).
"""
import math
import numpy as np

SQ2 = math.sqrt(2.0)
erf = np.vectorize(math.erf)
Phi = lambda z: 0.5 * (1 + math.erf(z / SQ2))

def pmu(lo, hi):                       # Pr(lo < mu < hi), mu ~ N(0,1/2): CDF = (1+erf(t))/2
    return 0.5 * (erf(np.asarray(hi, float)) - erf(np.asarray(lo, float)))

def q_lose(d, m, c):                   # Pr(|mu + d/2| > c | |mu| <= m)
    d = np.asarray(d, float)
    hi_lose = np.clip(c - d / 2, -m, m)        # lose if mu > c - d/2
    lo_lose = np.clip(-c - d / 2, -m, m)       # lose if mu < -c - d/2
    return (pmu(hi_lose, m) + pmu(-m, lo_lose)) / pmu(-m, m)

def dens_d(d):                         # N(0,2) density
    return np.exp(-d ** 2 / 4) / (2 * math.sqrt(math.pi))

def dstar(L, c):                       # decline iff q > 1/(1+L), q increasing in |d|
    lo, hi = 0.0, 20.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if q_lose(mid, c / SQ2, c) > 1 / (1 + L): hi = mid
        else: lo = mid
    return hi

def cond_d_density(dgrid, R):          # density of d given delta <= R (times Pr(delta<=R))
    a2 = np.clip((R - dgrid ** 2 / 2) / 2, 0, None)
    return dens_d(dgrid) * erf(np.sqrt(a2))     # Pr(|mu| <= a) = erf(a)

def normal_figures(c, L, n=2_000_001):
    R = c * c
    dg = np.linspace(-SQ2 * c, SQ2 * c, n); h = dg[1] - dg[0]
    w = cond_d_density(dg, R); Z = w.sum() * h                       # = 1 - exp(-c^2/2)
    ds = dstar(L, c)
    p_dec = w[np.abs(dg) > ds].sum() * h / Z
    q = q_lose(dg, c / SQ2, c)
    price = (w * np.maximum(0, (1 + L) * q - 1)).sum() * h / Z       # ANS maximal price
    return dict(Z=Z, Zexact=1 - math.exp(-R / 2), dstar=ds, dstar_c=ds / c, kdt=-p_dec, ans_price=price)

def fallibilist(c, L, n=400_001):
    p_win = 2 * Phi(c) - 1
    bet_ev = p_win - L * (1 - p_win)
    dg = np.linspace(-12, 12, n); h = dg[1] - dg[0]
    lose = pmu(c - dg / 2, np.inf) + pmu(-np.inf, -c - dg / 2)
    ev_d = (1 - lose) - L * lose
    val = (dens_d(dg) * np.maximum(ev_d, 0)).sum() * h - max(bet_ev, 0)
    return p_win, bet_ev, val

out = []
pr = lambda *a: out.append(" ".join(str(x) for x in a))

c = 1.96
t_of_c = 1 - math.exp(-c * c / 2)
c95 = math.sqrt(-2 * math.log(0.05))
pr(f"threshold map c^2=-2ln(1-t): c=1.96 -> t={t_of_c:.4f}; t=0.85 -> c={math.sqrt(-2*math.log(0.15)):.4f}; t=0.95 -> c={c95:.4f}")
# check of the map itself: P(delta < a | delta >= b) = 1 - exp(-(a-b)/2) for chi^2_2 (Monte Carlo)
rng = np.random.default_rng(1)
e = rng.standard_normal((4_000_000, 2)); dl = (e ** 2).sum(1)
b0 = 1.0; sel = dl >= b0
pr(f"  MC check: P(delta < b+c^2 | delta >= b) = {np.mean(dl[sel] < b0 + c*c):.4f} vs 1-exp(-c^2/2) = {t_of_c:.4f}")

for cc in (c, c95):
    for L in (10, 20, 100):
        r = normal_figures(cc, L)
        pr(f"c={cc:.4f} L={L:3d}: d*={r['dstar']:.4f} (= {r['dstar_c']:.4f} c) | KDT value {r['kdt']:+.4f} | "
           f"ANS max price {r['ans_price']:.4f} | norm check {r['Z']:.6f} vs {r['Zexact']:.6f}")
p_win, bet_ev, val = fallibilist(c, 10)
pr(f"fallibilist c=1.96 L=10: P(|e1|<=c)={p_win:.4f}, bet EV={bet_ev:.4f}, Bayesian value of 2nd weighing={val:.4f}")

# Section 3 probabilities
pr(f"P(0<|d|<=sqrt2 c) = 2Phi(c)-1 = {2*Phi(c)-1:.4f}")
z = (2 - SQ2) * c / SQ2
p_wt_uncond = 2 * (1 - Phi(z))
dg = np.linspace(-SQ2 * c, SQ2 * c, 2_000_001); h = dg[1] - dg[0]
w = cond_d_density(dg, c * c)
p_wt_cond = w[np.abs(dg) > (2 - SQ2) * c].sum() / w.sum()
pr(f"P(weight belief lost) = P(|d|>(2-sqrt2)c): unconditional {p_wt_uncond:.4f}; given delta<=c^2 {p_wt_cond:.4f}")
for cc in (1.645, 1.96, 2.0, 2.17, 2.448):
    pr(f"   c={cc}: unconditional {2*(1-Phi((2-SQ2)*cc/SQ2)):.4f}")
# accurate first reading (e1 = 0): d = -e2 ~ N(0,1)
pr(f"   first reading accurate (e1=0): P(|e2|>(2-sqrt2)c) = {2*(1-Phi((2-SQ2)*c)):.4f}")
pr(f"P(delta >= (1+sqrt2)^2 c^2) = {math.exp(-(1+SQ2)**2*c*c/2):.3e}")

# Section 5.1: conditional ken on 'look and bet-now differ' at x with delta(x)=0, L=10
L = 10; ds = dstar(L, c)
n = 3001
mu = np.linspace(-4, 4, n); d = np.linspace(-9, 9, 2 * n - 1)
MU, D = np.meshgrid(mu, d, indexing="ij")
dmu, dd = mu[1] - mu[0], d[1] - d[0]
dens = np.exp(-MU ** 2) / math.sqrt(math.pi) * dens_d(D)
delta = 2 * MU ** 2 + D ** 2 / 2
m_post = np.maximum(c / SQ2, np.abs(MU))
qpost = q_lose(D, m_post, c)
decl = qpost > 1 / (1 + L)                         # look declines here: D-event
inf_delta_D = delta[decl].min()
KD = decl & (delta <= ds ** 2 / 2 + c * c)       # B(E cap D); x (delta 0) is not in D
win = np.abs(MU + D / 2) <= c
pw = (dens * KD * win).sum() / (dens * KD).sum()
pr(f"5.1: inf delta over decline set {inf_delta_D:.4f} (d*^2/2 = {ds**2/2:.4f}); "
   f"bet EV on conditional ken = {pw - L*(1-pw):+.4f}")

# A.5: value of the second weighing for the bet on M={delta<=R} (state proposition), and for the weight bet
def a5(Rfac, L, weight=False):
    R = Rfac * c * c
    inM = delta <= R
    if weight:   # bet on known weight interval |e1| <= sqrt(R); post-ken loss prob
        lose_post = q_lose_gen(D, m_post, math.sqrt(R))
    else:        # post-ken probability of M^c: P(2mu^2 + d^2/2 > R | |mu| <= m)
        a = np.sqrt(np.clip((R - D ** 2 / 2) / 2, 0, None))
        inside = np.minimum(a, m_post)
        lose_post = 1 - pmu(-inside, inside) / pmu(-m_post, m_post)
        lose_post = np.where(D ** 2 / 2 > R, 1.0, lose_post)
    dec = lose_post > 1 / (1 + L)
    return -(dens * inM * dec).sum() / (dens * inM).sum()

def q_lose_gen(Dv, m, bound):            # Pr(|mu + d/2| > bound | |mu| <= m)
    hi_l = np.clip(bound - Dv / 2, -m, m); lo_l = np.clip(-bound - Dv / 2, -m, m)
    return (pmu(hi_l, m) + pmu(-m, lo_l)) / pmu(-m, m)

for Rf in (1, 3, 5, 7):
    pr(f"A.5 R={Rf}c^2 (threshold (1+sqrt2)^2={(1+SQ2)**2:.3f}): state-bet value L=1e3 {a5(Rf,1e3):+.5f}, "
       f"L=1e6 {a5(Rf,1e6):+.5f} | weight-bet value L=1e6 {a5(Rf,1e6,True):+.6f}")
# maximal post-ken reach in |e1| vs sqrt(R) over states of M
for Rf in (3, 5, 5.9, 7):
    R = Rf * c * c; inM = delta <= R
    reach = (m_post + np.abs(D) / 2)[inM].max()
    pr(f"   R={Rf}c^2: max post-ken |e1| = {reach/c:.4f} c vs sqrt(R) = {math.sqrt(R)/c:.4f} c "
       f"(formula c/sqrt2+sqrt(R/2) = {(c/SQ2+math.sqrt(R/2))/c:.4f} c)")
print("\n".join(out))
