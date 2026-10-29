#!/usr/bin/env python3
"""High-precision check of the section 5.1 figure (bet EV on the conditional ken, L=10, c=1.96,
actual readings accurate) by 1-D quadrature (mpmath).  Region (d>0, doubled by symmetry):
K^D = {look declines} cap {delta <= inf_D delta + c^2}; inf_D delta = d*^2/2.
For |d|>d*: |mu| <= a(d) = sqrt((d*^2-d^2)/4 + c^2/2) (< c/sqrt2, so these states decline).
Also scans |d|<d*, |mu|>c/sqrt2 (larger post-kens) for declining states inside the delta bound."""
import mpmath as mp
mp.mp.dps = 30
c, L = mp.mpf('1.96'), 10
s2 = mp.sqrt(2)
pmu = lambda lo, hi: (mp.erf(hi) - mp.erf(lo)) / 2          # mu ~ N(0,1/2)
def q(d, m):                                                  # P(|mu+d/2|>c | |mu|<=m)
    hi = min(max(c - d/2, -m), m); lo = min(max(-c - d/2, -m), m)
    return (pmu(hi, m) + pmu(-m, lo)) / pmu(-m, m)
dstar = mp.findroot(lambda d: q(d, c/s2) - mp.mpf(1)/(1+L), 2.2)
phi_d = lambda d: mp.exp(-d**2/4) / (2*mp.sqrt(mp.pi))
a = lambda d: mp.sqrt((dstar**2 - d**2)/4 + c**2/2)
dmax = mp.sqrt(dstar**2 + 2*c**2)
mass = mp.quad(lambda d: phi_d(d) * mp.erf(a(d)), [dstar, dmax])
lose = mp.quad(lambda d: phi_d(d) * max(0, pmu(c - d/2, a(d))) if c - d/2 < a(d) else 0, [dstar, dmax])
p_lose = lose / mass
print(f"d* = {mp.nstr(dstar, 8)} = {mp.nstr(dstar/c, 6)} c ; inf_D delta = d*^2/2 = {mp.nstr(dstar**2/2, 8)}")
print(f"P(lose | K^D) = {mp.nstr(p_lose, 8)} ; bet EV on K^D at L=10: {mp.nstr(1 - (1+L)*p_lose, 6)}")
# part (ii): states with |d|<d*, c/sqrt2 < |mu| <= a(d) that decline?
hits = 0
for i in range(1, 400):
    d = dstar * i / 400
    for j in range(1, 200):
        m = c/s2 + (a(d) - c/s2) * j / 200
        if q(d, m) > mp.mpf(1)/(1+L): hits += 1
print("declining states with |d|<d*, |mu|>c/sqrt2 inside the delta bound (grid scan):", hits)
for dps_check in (1.0, 2.0):
    print(f"q(d=0.5d*, m=a) = {mp.nstr(q(dstar*0.5, a(dstar*0.5)), 6)} ; q(d=0.95d*, m=a) = {mp.nstr(q(dstar*0.95, a(dstar*0.95)), 6)}") if dps_check == 1.0 else None
