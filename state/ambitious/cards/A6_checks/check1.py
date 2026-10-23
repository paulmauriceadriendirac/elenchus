import sys, itertools
sys.path.insert(0, sys.argv[1])
from structs import *

def binary_experiments(Y):
    Y = sorted(Y)
    cells = []
    for m in range(1, 1 << len(Y)):
        p = frozenset(Y[i] for i in range(len(Y)) if m >> i & 1)
        cells.append(p)
    # include trivial experiment (p = Y) and all proper splits
    return cells

def belief_arrow(gg, n):
    for Y in subsets(n):
        BY = RB(Y, gg)
        for p in binary_experiments(Y):
            if BY & p and RB(Y & p, gg) != (BY & p):
                return False
    return True

def laminar(Kf, dom):
    # reflexive on dom, transitive within dom, nested
    for s in dom:
        if s not in Kf[s]: return False
        for t in Kf[s]:
            if t in dom and not Kf[t] <= Kf[s]: return False
    for s in dom:
        for t in dom:
            a, b = Kf[s], Kf[t]
            if a & b and not (a <= b or b <= a): return False
    return True

def good_struct(Kfun, x, Y, geq, gg):
    K0 = Kfun(x, Y, geq, gg)
    for p in binary_experiments(Y):
        cells = [p, Y - p] if p != Y else [Y]
        K1 = {}
        for c in cells:
            if not c: continue
            for s in c:
                K1[s] = Kfun(s, Y & c, geq, gg)
        # no x-relative defeat
        for s in K0:
            if not K1[s] <= K0: return False
        if not laminar(K1, K0): return False
    return True

def gap(Kfun, x, Y, geq, gg):
    K0 = Kfun(x, Y, geq, gg)
    return all(gg[k][v] for k in K0 for v in Y - K0)

def CK(geq, gg):
    n = len(gg)
    if not modular(gg): return False
    for a in range(n):
        for b in range(n):
            if strict(geq, a, b) and not gg[a][b]:
                if any(gg[u][b] for u in range(n)):
                    return False
    return True

if __name__ == '__main__':
  for n in range(1, 5):
      stats = dict(total=0, mod=0, bel_mismatch=0, K_gap_mismatch=0, K_global_mismatch=0,
                   I_gap_mismatch=0, I_global_mismatch=0, KM_gap_nec_fail=0, KM_global_mod_mismatch=0,
                   KK_fail_under_mod=0)
      for geq, gg in structures(n, total=True):
          stats['total'] += 1
          m = modular(gg); stats['mod'] += m
          if belief_arrow(gg, n) != m: stats['bel_mismatch'] += 1
          gK_all = True; gI_all = True; gKM_all = True
          for Y in subsets(n):
              for x in Y:
                  gK = good_struct(K_K, x, Y, geq, gg)
                  if gK != gap(K_K, x, Y, geq, gg): stats['K_gap_mismatch'] += 1
                  gK_all &= gK
                  gI = good_struct(K_I, x, Y, geq, gg)
                  if gI and not gap(K_I, x, Y, geq, gg): stats['I_gap_mismatch'] += 1   # necessity check
                  gI_all &= gI
                  gKM = good_struct(K_KM, x, Y, geq, gg)
                  if gKM and not gap(K_KM, x, Y, geq, gg): stats['KM_gap_nec_fail'] += 1
                  gKM_all &= gKM
                  if m:
                      for Kf in (K_K, K_I, K_KM):
                          K0 = Kf(x, Y, geq, gg)
                          if any(not Kf(s, Y, geq, gg) <= K0 for s in K0):
                              stats['KK_fail_under_mod'] += 1
          if gK_all != CK(geq, gg): stats['K_global_mismatch'] += 1
          if gI_all != m: stats['I_global_mismatch'] += 1
          if gKM_all != m: stats['KM_global_mod_mismatch'] += 1
      print(n, stats)
