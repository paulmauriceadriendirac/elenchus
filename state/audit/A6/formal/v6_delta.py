#!/usr/bin/env python3
"""A6 v6 formal delta audit: independent recomputation (self-contained, rerunnable, ~1-2 min).

Recomputes, in the essay's own model (v6 section 3 and appendix A.5), every Bjorn figure that the
v6 diff relies on (rewritten encroachment passage, section 6.2) and every figure that
VERIFICATION.md reports (0.3555901517; threshold 2.19562510; value -0.60208829).

Model (A.5): after the first reading the scale errors e1, e2 are iid N(0,1) (swamped prior on
weight); mu=(e1+e2)/2 ~ N(0,1/2) and d=e1-e2 ~ N(0,2) are independent; delta=e1^2+e2^2=2mu^2+d^2/2.
x >= y iff delta(x) <= delta(y); x >> y iff delta(y)-delta(x) > c^2.  Normal situation
(delta(x) <= c^2): K-normality ken K = {delta <= c^2}.  Bet: +1 if |e1| <= c (weight within c of the
first reading), -L otherwise; declining pays 0.  The second reading reveals d; the K-normality
post-answer ken of s is the line d=d_s with |mu| <= max(c/sqrt2, |mu_s|).

Methods: (Q1) 1-D quadrature in polar coordinates of (e1,e2); (Q2) 1-D quadrature in (mu,d);
(MC) Monte Carlo applying the KDT post-answer rule state by state (no region formula assumed).
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 40
SQ2 = mp.sqrt(2)
INV = lambda L: mp.mpf(1) / (1 + L)                      # decline iff P(lose | ken) > 1/(1+L)
phid = lambda x: mp.exp(-x**2 / 4) / (2 * mp.sqrt(mp.pi))  # density of d ~ N(0,2)


def pmu(lo, hi):                       # P(lo < mu <= hi), mu ~ N(0,1/2)
    return (mp.erf(hi) - mp.erf(lo)) / 2


def q(c, d, m):                        # P(|e1| > c | d, |mu| <= m), e1 = mu + d/2 (post-answer ken)
    d = abs(d)
    hi = min(max(c - d / 2, -m), m)
    lo = min(max(-c - d / 2, -m), m)
    return (pmu(hi, m) + pmu(-m, lo)) / pmu(-m, m)


def dstar(c, L):                       # KDT decline threshold on |d| for post-ken |mu| <= c/sqrt2
    return mp.findroot(lambda d: q(c, d, c / SQ2) - INV(L), (mp.mpf(1), mp.mpf('3.5')), solver='illinois')


def pK_dgt(c, a):                      # P(|d| > a | delta <= c^2) by Q1 and Q2
    k = a / SQ2                        # |d| > a  <=>  r |cos phi| > a/sqrt2, phi uniform
    q1 = mp.quad(lambda r: r * mp.exp(-r**2 / 2) * (2 / mp.pi) * mp.acos(k / r), [k, c]) / (1 - mp.exp(-c**2 / 2))
    w = lambda x: phid(x) * mp.erf(mp.sqrt(max(0, (c**2 - x**2 / 2) / 2)))
    q2 = mp.quad(w, [a, SQ2 * c]) / mp.quad(w, [0, SQ2 * c])
    return q1, q2


def pB(c, d):                          # evidence-conditioned P(|e1| > c | d): e1 | d ~ N(d/2, 1/2)
    return (mp.erfc(c - d / 2) + mp.erfc(c + d / 2)) / 2


def bayes(c, L):                       # Bayesian (evidence-conditioned) bet value now and value of free look
    dB = mp.findroot(lambda d: pB(c, d) - INV(L), (mp.mpf('0.5'), mp.mpf(5)), solver='illinois')
    G = 2 * mp.quad(lambda x: phid(x) * ((1 + L) * pB(c, x) - 1), [dB, dB + 4, dB + 12, mp.inf])
    now = (1 + L) * mp.erf(c / SQ2) - L
    tower = 2 * mp.quad(lambda x: phid(x) * pB(c, x), [0, 6, mp.inf])     # must equal erfc(c/sqrt2)
    return dB, now, G, tower


def sec51(c, L):                       # bet EV on K^D (D = decline set), actual readings accurate
    ds = dstar(c, L)
    a = lambda d: mp.sqrt(max(0, (ds**2 - d**2) / 4 + c**2 / 2))   # |mu| bound from delta <= d*^2/2 + c^2
    dmax = mp.sqrt(ds**2 + 2 * c**2)
    dsw = c + ds / SQ2                 # c - d/2 = a(d) here; lose part empty beyond
    mass = mp.quad(lambda d: phid(d) * mp.erf(a(d)), [ds, dsw, dmax])
    lose = mp.quad(lambda d: phid(d) * pmu(c - d / 2, a(d)), [ds, dsw])
    pl = lose / mass
    worst, worst99 = mp.mpf(-1), mp.mpf(-1)   # states |d|<d*, c/sqrt2<|mu|<=a(d): must NOT decline
    with mp.workdps(20):
        for i in range(600):
            d = ds * i / 600
            for j in range(1, 301):
                m = c / SQ2 + (a(d) - c / SQ2) * j / 300
                v = q(c, d, m) - INV(L)
                worst = max(worst, v)
                if i <= 594:
                    worst99 = max(worst99, v)
    return ds, pl, 1 - (1 + L) * pl, worst, worst99


def mc(c, L, ds, dB, N=20_000_000, B=2_000_000, seed=20261030):
    rng = np.random.default_rng(seed)
    merf = np.frompyfunc(math.erf, 1, 1)
    c, ds, dB = float(c), float(ds), float(dB)
    m0, t = c / math.sqrt(2), 1.0 / (1 + L)
    A = dict(n=0, win=0, nK=0, K_lose=0, K_dec=0, K_wl=0, g_bayes=0.0, g_kdtpol=0.0, n51=0, l51=0, minD=np.inf)
    for _ in range(N // B):
        e1, e2 = rng.standard_normal(B), rng.standard_normal(B)
        mu, d, dl = (e1 + e2) / 2, e1 - e2, e1**2 + e2**2
        ad, am = np.abs(d), np.abs(mu)
        bet = np.where(np.abs(e1) <= c, 1.0, -float(L))
        dec = np.where(am <= m0, ad > ds, False)          # KDT later choice at narrow post-kens
        wide = am > m0                                     # wider post-ken |mu| <= |mu_s|: compute q
        dd, mm = ad[wide], am[wide]
        hi, lo = np.clip(c - dd / 2, -mm, mm), np.clip(-c - dd / 2, -mm, mm)
        Em = merf(mm).astype(float)
        dec[wide] = ((Em - merf(hi).astype(float)) + (merf(lo).astype(float) + Em)) / (2 * Em) > t
        inK = dl <= c**2
        A['n'] += B; A['win'] += int((np.abs(e1) <= c).sum())
        A['nK'] += int(inK.sum()); A['K_lose'] += int((inK & (np.abs(e1) > c)).sum())
        A['K_dec'] += int((inK & dec).sum()); A['K_wl'] += int((inK & (ad > (2 - math.sqrt(2)) * c)).sum())
        A['g_bayes'] += float(np.where(ad > dB, -bet, 0.0).sum())      # look (Bayes later policy) - bet now
        A['g_kdtpol'] += float(np.where(dec, -bet, 0.0).sum())         # look (KDT later policy) - bet now
        A['minD'] = min(A['minD'], float(dl[dec].min()))
        in51 = dec & (dl <= ds**2 / 2 + c**2)
        A['n51'] += int(in51.sum()); A['l51'] += int((in51 & (np.abs(e1) > c)).sum())
    return A


if __name__ == '__main__':
    L = 10
    z975 = SQ2 * mp.erfinv(mp.mpf('0.95'))
    for label, c in (('c = 1.96', mp.mpf('1.96')), ('c = z_0.975 = ' + mp.nstr(z975, 12), z975)):
        print(f'===== {label}, L = {L} =====')
        ds = dstar(c, L)
        dB, now, G, tower = bayes(c, L)
        kdt_q1, kdt_q2 = pK_dgt(c, ds)
        wl_q1, wl_q2 = pK_dgt(c, (2 - SQ2) * c)
        ds51, pl, ev51, worst, worst99 = sec51(c, L)
        print('[1a] bet alone, knowledge-conditioned: on K={delta<=c^2}, |e1|<=sqrt(delta)<=c, so P(win|K)=1; EV 1 > 0 (decline): TAKES')
        print(f'[1b] bet alone, evidence-conditioned: P(win)=erf(c/sqrt2)={mp.nstr(mp.erf(c/SQ2), 10)}; EV={mp.nstr(now, 10)} > 0: TAKES')
        print(f'[1c] free 2nd scale, KDT: d* = {mp.nstr(ds, 12)} (= {mp.nstr(ds/c, 6)} c); value of looking = -P(|d|>d*|K) '
              f'= {mp.nstr(-kdt_q1, 10)} (Q1) / {mp.nstr(-kdt_q2, 10)} (Q2) < 0: STRICTLY PREFERS ACTING NOW')
        print(f'     KDT ranking: bet now {1} > look {mp.nstr(1 - kdt_q1, 6)} > decline 0')
        print(f'[1d] free 2nd scale, Bayesian: decline threshold d_B = {mp.nstr(dB, 10)}; value of looking G = '
              f'{mp.nstr(G, 10)} > 0: STRICTLY PREFERS LOOKING (tower check {mp.nstr(tower, 10)} vs erfc(c/sqrt2) {mp.nstr(mp.erfc(c/SQ2), 10)})')
        print(f'     Bayesian ranking: look {mp.nstr(now + G, 6)} > bet now {mp.nstr(now, 6)} > decline 0')
        print(f'[4a] P(weight belief lost | K) = P(|d|>(2-sqrt2)c | K) = {mp.nstr(wl_q1, 12)} (Q1) / {mp.nstr(wl_q2, 12)} (Q2)')
        print(f'[4b] threshold d* = {mp.nstr(ds51, 12)}')
        print(f'[4c] sec 5.1: P(lose | K^D) = {mp.nstr(pl, 12)}; bet EV on K^D = {mp.nstr(ev51, 12)}')
        print(f'     region check (|d|<d*, c/sqrt2<|mu|<=a(d), 600x300 grid): max q-1/(1+L) = {mp.nstr(worst, 6)} '
              f'(excluding the last 1% of d before d*: {mp.nstr(worst99, 6)}); negative => no declining state there')
        print(f'[P1] unconditioned loss erfc((2-sqrt2)c/2) = {mp.nstr(mp.erfc((2-SQ2)*c/2), 10)}; '
              f'narrower event minus erfc(c/sqrt2) = {mp.nstr(mp.erfc((2-SQ2)*c/2) - mp.erfc(c/SQ2), 10)}; '
              f'P(0<|d|<=sqrt2 c) = {mp.nstr(mp.erf(c/SQ2), 10)}; P(delta>=(1+sqrt2)^2c^2) = {mp.nstr(mp.exp(-(1+SQ2)**2*c**2/2), 6)}')
        if label == 'c = 1.96':
            for LL in (20, 100):
                dd = dstar(c, LL)
                print(f'     KDT value at {LL}:1 = {mp.nstr(-pK_dgt(c, dd)[0], 8)} (d* = {mp.nstr(dd, 8)})')
            print('     VERIFICATION.md vs this script:')
            print(f'       0.3555901517 vs {mp.nstr(wl_q1, 10)} -> match to 10 d.p.: {abs(wl_q1 - mp.mpf("0.3555901517")) < mp.mpf("5e-11")}')
            print(f'       2.19562510   vs {mp.nstr(ds, 9)} -> match to 8 d.p.: {abs(ds - mp.mpf("2.19562510")) < mp.mpf("5e-9")}')
            print(f'       -0.60208829  vs {mp.nstr(ev51, 8)} -> match to 8 d.p.: {abs(ev51 - mp.mpf("-0.60208829")) < mp.mpf("5e-9")}')
            A = mc(c, L, ds, dB)
            n, nK, n51 = A['n'], A['nK'], A['n51']
            se = lambda p, k: math.sqrt(p * (1 - p) / k)
            pK = A['K_dec'] / nK; pw = A['K_wl'] / nK; p51 = A['l51'] / n51
            print(f'[MC] N = {n:,} states (seed 20261030); in K: {nK:,}')
            print(f'     losing states inside K: {A["K_lose"]} (proof says 0); P(win) = {A["win"]/n:.5f}')
            print(f'     KDT value = {-pK:.5f} +/- {se(pK, nK):.5f}; P(weight loss | K) = {pw:.5f} +/- {se(pw, nK):.5f}')
            print(f'     Bayesian value of look (Bayes later policy) = {A["g_bayes"]/n:.4f}; '
                  f'(not claimed) Bayesian value of look with KDT later policy = {A["g_kdtpol"]/n:.4f}')
            print(f'     min delta over decline set D = {A["minD"]:.5f} (d*^2/2 = {float(ds)**2/2:.5f}); '
                  f'K^D samples {n51:,}: bet EV = {1 - (1+L)*p51:.4f} +/- {(1+L)*se(p51, n51):.4f}')
