# Bjorn's second weighing (Goodman & Salow 2023 sec. 6; BRN sec. 5), K-normality, statist model:
#   states <w, y1, y2>; delta = (w-y1)^2 + (w-y2)^2;  s >= s' iff delta(s) <= delta(s');
#   s >> s' iff delta(s) + c^2 < delta(s').
# Probabilities (G&S 2023 pp. 129-30): scale errors e1, e2 i.i.d. N(0, sigma^2), w swamped.
# With sigma = 1 and c = 1.96 (BRN n. 18).  Coordinates m = (e1+e2)/2 ~ N(0,1/2), d = e1-e2 ~ N(0,2),
# independent; e1 = m + d/2; delta = 2 m^2 + d^2/2.  After the first reading (evidence E_{y1}), the
# actual situation x is taken to have delta(x) <= c^2, so K(x) = {delta <= c^2}.
# Bet: pays 1 if |w - y1| <= c (i.e. |e1| <= c), -L otherwise.  Known to win at x.
import math
from math import erf, sqrt, exp, pi

c = 1.96
def Phi(z): return 0.5 * (1 + erf(z / sqrt(2)))
sm = sqrt(0.5); sd = sqrt(2.0)

def post_lose_prob(d, R):
    """Pr(|m + d/2| > c  |  |m| <= R), m ~ N(0, 1/2)."""
    tot = Phi(R / sm) - Phi(-R / sm)
    # win iff -c - d/2 <= m <= c - d/2
    lo, hi = max(-R, -c - d / 2), min(R, c - d / 2)
    win = max(0.0, Phi(hi / sm) - Phi(lo / sm)) if hi > lo else 0.0
    return 1 - win / tot

R_post = c / sqrt(2)          # post-discovery ken on the line d, for any s with delta(s) <= c^2

def declines(d, L):
    pl = post_lose_prob(d, R_post)
    return (1 - pl) - L * pl < 0

def dstar(L):
    lo, hi = 0.0, 3 * c
    if not declines(hi, L): return None
    for _ in range(80):
        mid = (lo + hi) / 2
        if declines(mid, L): hi = mid
        else: lo = mid
    return hi

def pr_disc(region, N=1600):
    """Integrate the (m,d) density over {delta <= c^2} ∩ region; return (mass_region, mass_disc)."""
    tot = reg = 0.0
    Mm = c / sqrt(2); Md = sqrt(2) * c
    for i in range(N):
        m = -Mm + (i + 0.5) * 2 * Mm / N
        for j in range(N):
            d = -Md + (j + 0.5) * 2 * Md / N
            if 2 * m * m + d * d / 2 <= c * c:
                w = exp(-m * m / (2 * 0.5)) * exp(-d * d / (2 * 2.0))
                tot += w
                if region(m, d): reg += w
    return reg, tot

if __name__ == '__main__':
    print("Defeat in Bjorn: post-discovery ken on line d has |m| <= c/sqrt2 =", round(R_post, 3),
          "; weight bound |e1|<=c lost iff |d| >", round((2 - sqrt(2)) * c, 3), "= (2-sqrt2)c")
    for L in (2, 3, 5, 9, 10, 20, 50, 100, 1000):
        ds = dstar(L)
        if ds is None:
            print("L=%g: never declines" % L); continue
        reg, tot = pr_disc(lambda m, d: abs(d) > ds, N=700)
        print("L=%5g  decline iff |d| > %.3f (= %.3f c);  KDT value of the free 2nd weighing = %.4f" % (L, ds, ds / c, -reg / tot))

