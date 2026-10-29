# Bjorn (G&S 2023 sec. 6; BRN sec. 5), K-normality, statist; sigma = 1.  mu=(e1+e2)/2 ~ N(0,1/2),
# d = e1-e2 ~ N(0,2) independent; e1 = mu + d/2; delta = 2 mu^2 + d^2/2.  Normal situation:
# K = {delta <= c^2}; post-answer ken on line d (any s in K): |mu| <= c/sqrt2.
# Bet: +1 if |e1| <= c, -L otherwise.
# (a) KDT value of the free second weighing for c = 1.96 and c = 2.448 (= sqrt(-2 ln .05)).
#     c^2 = -2 ln(1-t) links c to G&S's probabilistic threshold t (2023, 121, with chi^2_2 errors).
# (b) Answer-indexed rule: the largest price kappa* it pays to look, against the bet, at a normal
#     situation:  kappa* = sum_d Pr(d | K) max(0, -E[bet | |mu| <= c/sqrt2, d]).
# (c) Fallibilist (evidence-conditioned) value of the second weighing for the same bet.
from math import erf, sqrt, exp, log, pi
def Phi(z): return 0.5 * (1 + erf(z / sqrt(2)))
sm = sqrt(.5); sdd = sqrt(2.)
def win_prob(d, R, c):
    tot = Phi(R / sm) - Phi(-R / sm)
    lo, hi = max(-R, -c - d / 2), min(R, c - d / 2)
    return (Phi(hi / sm) - Phi(lo / sm)) / tot if hi > lo else 0.0
def phi_d(d): return exp(-d * d / 4) / sqrt(4 * pi)
def run(c, L, M=4000):
    R = c / sqrt(2)
    # weight of line d within K: Pr(|mu| <= sqrt((c^2 - d^2/2)/2)) * phi_d(d)
    Dmax = sqrt(2) * c
    num_kdt = num_ans = den = 0.0
    h = 2 * Dmax / M
    for i in range(M):
        d = -Dmax + (i + .5) * h
        r = sqrt(max(0., (c * c - d * d / 2) / 2))
        wK = (Phi(r / sm) - Phi(-r / sm)) * phi_d(d)
        den += wK
        p = win_prob(d, R, c)
        evpost = p - L * (1 - p)
        if evpost < 0:
            num_kdt += wK * (-1.0)       # declines; forgoes 1 (bet wins throughout K)
            num_ans += wK * (-evpost)
    kdt, ans = num_kdt / den, num_ans / den
    # fallibilist: evidence = first reading only; d ~ N(0,2) on whole line, mu untruncated
    pw = Phi(c) - Phi(-c); ev0 = pw - L * (1 - pw)
    vf = 0.0; Dm = 12.
    h2 = 2 * Dm / M
    for i in range(M):
        d = -Dm + (i + .5) * h2
        p = Phi((c - d / 2) / sm) - Phi((-c - d / 2) / sm)
        vf += phi_d(d) * max(0., p - L * (1 - p)) * h2
    vfall = vf - max(0., ev0)
    return kdt, ans, ev0, vfall
for c in (1.96, sqrt(-2 * log(.05))):
    t = 1 - exp(-c * c / 2)
    for L in (10, 20, 100):
        kdt, ans, ev0, vfall = run(c, L)
        print('c=%.3f (threshold t=%.3f) L=%3d: KDT value %.4f | answer-indexed max price %.4f | '
              'fallibilist: bet EV %.3f, value of 2nd weighing %.4f' % (c, t, L, kdt, ans, ev0, vfall))
# Situations at which no weight-only Lemma-1 bet works: R >= (1+sqrt2)^2 c^2; delta ~ chi^2_2
c = 1.96
print('Pr(delta >= (1+sqrt2)^2 c^2) = %.2e' % exp(-((1 + sqrt(2)) ** 2 * c * c) / 2))
