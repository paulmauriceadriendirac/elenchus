# Bjorn's second weighing: the conditional rule (CEU) on (i) the plain ken-bet and (ii) the
# eps-perturbed problem {bet1 = bet + eps*zeta, bet2 = bet, decline}.  Grid over (m, d).
# Post-discovery ken at s (K-normality): line d(s), |m| <= R(s) = max(c/sqrt2, |m_s|).
import sys
sys.path.insert(0, sys.argv[1])
from bjorn import c, Phi, sm, post_lose_prob
from math import exp, sqrt

def run(L, eps=1e-3, N=500, box=3.2):
    pts = []
    for i in range(N):
        m = -box * c / sqrt(2) + (i + .5) * 2 * box * c / sqrt(2) / N
        for j in range(N):
            d = -box * sqrt(2) * c + (j + .5) * 2 * box * sqrt(2) * c / N
            w = exp(-m * m) * exp(-d * d / 4)
            delta = 2 * m * m + d * d / 2
            R = max(c / sqrt(2), abs(m))
            pl = post_lose_prob(d, R)
            win = abs(m + d / 2) <= c
            pts.append((m, d, w, delta, pl, win))
    bet = lambda p: 1.0 if p[5] else -L
    K = [p for p in pts if p[3] <= c * c]
    D = [p for p in pts if (1 - p[4]) - L * p[4] < 0]          # plain problem: look declines here
    if not D: return None
    infD = min(p[3] for p in D)
    CK = [p for p in D if p[3] <= infD + c * c]                  # x = most normal state: CK = undominated(D)
    ZK = sum(p[2] for p in K)
    kdt = -sum(p[2] for p in K if (1 - p[4]) - L * p[4] < 0) / ZK
    ZC = sum(p[2] for p in CK)
    eb = sum(p[2] * bet(p) for p in CK) / ZC
    # eps problem: zeta = +Nz on K∩D, -1 elsewhere
    KD = [p for p in K if (1 - p[4]) - L * p[4] < 0]
    Nz = 2 * ZK / max(sum(p[2] for p in KD), 1e-300) + 1
    inKD = set((p[0], p[1]) for p in KD)
    zeta = lambda p: Nz if (p[0], p[1]) in inKD else -1.0
    ezK = sum(p[2] * zeta(p) for p in K) / ZK
    # post-look: on line d with radius R, choose among bet1, bet2, decline.  zeta on a post ken:
    # post kens of non-declining states lie on lines |d| <= d*, which contain no K∩D point, so zeta=-1 there:
    # bet2 beats bet1; declining states decline.  Hence plan != bet1 at every state; D' = E; CK' = K(x).
    margin = sum(p[2] * ((bet(p) + eps * zeta(p)) - (0.0 if (1 - p[4]) - L * p[4] < 0 else bet(p))) for p in K) / ZK
    return dict(L=L, kdt_value=round(kdt, 4), ceu_plain_E_bet_given_CK=round(eb, 3),
                ceu_plain_prefers_look=eb < 0, eps_E_zeta_on_K=round(ezK, 3), eps_ceu_margin_bet1_over_look=round(margin, 4))

for L in (5, 10, 20, 100):
    print(run(L))
