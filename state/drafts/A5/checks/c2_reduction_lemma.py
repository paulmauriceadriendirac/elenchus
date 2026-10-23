# C2. Reduction lemma, machine check on W = {1,2,3} with all 8 propositions and all 256 belief states.
# Marginal extensionality (ME): for every state B and p not in B, the increment
#   D(w) = A(B+p, w) - A(B, w)
# takes one value on the p-worlds and one value on the not-p worlds.
# ME is a set of linear equalities on the 256*3 unknowns A(B,w). We compute a basis of the solution space and check
# the Lemma on every basis vector (the claims are linear, so checking a basis suffices):
#   (L1) the jump J_p^B = D(w in p) - D(w not in p) does not depend on B, as long as neither B nor B+p
#        contains p together with its complement (and p is contingent);
#   (L2) hence for every B containing no complementary pair:
#        A(B,w) - A(empty,w) - sum_{p in B, p contingent} J_p * 1_p(w)   is constant in w  (= kappa(B)).
# We also report the dimension of the ME solution space.
import itertools
import numpy as np
from sympy import Matrix

W = (0, 1, 2)
PROPS = [frozenset(c) for r in range(0, 4) for c in itertools.combinations(W, r)]
STATES = [frozenset(p for p, b in zip(PROPS, bits) if b) for bits in itertools.product([0, 1], repeat=len(PROPS))]
SIDX = {B: i for i, B in enumerate(STATES)}
FULL = frozenset(W)
nvar = len(STATES) * len(W)
def var(B, w):
    return SIDX[B] * len(W) + w

rows = []
for B in STATES:
    for p in PROPS:
        if p in B:
            continue
        B1 = B | {p}
        # increment D(w) = A(B1,w) - A(B,w); require D(w)=D(w') for w,w' on the same side of p
        for side in (p, FULL - p):
            ws = sorted(side)
            for a, b in zip(ws, ws[1:]):
                r = np.zeros(nvar)
                r[var(B1, a)] += 1; r[var(B, a)] -= 1
                r[var(B1, b)] -= 1; r[var(B, b)] += 1
                rows.append(r)
M = np.array(rows)
# null space via SVD
u, s, vt = np.linalg.svd(M, full_matrices=True)
rank = int((s > 1e-9).sum())
basis = vt[rank:]
print("ME constraints:", M.shape[0], " unknowns:", nvar, " rank:", rank, " dim of ME solution space:", basis.shape[0])

def comp_pair(B):
    return any((FULL - p) in B for p in B)

contingent = [p for p in PROPS if 0 < len(p) < 3]
maxdev_L1 = 0.0; maxdev_L2 = 0.0
for vec in basis:
    A = lambda B, w: vec[var(B, w)]
    def jump(B, p):
        D = [A(B | {p}, w) - A(B, w) for w in W]
        inside = [D[w] for w in W if w in p]; outside = [D[w] for w in W if w not in p]
        return inside[0] - outside[0]
    J = {p: jump(frozenset(), p) for p in contingent}
    for B in STATES:
        for p in contingent:
            if p in B:
                continue
            if comp_pair(B | {p}):
                continue
            maxdev_L1 = max(maxdev_L1, abs(jump(B, p) - J[p]))
        if comp_pair(B):
            continue
        resid = [A(B, w) - A(frozenset(), w) - sum(J[p] for p in B if p in J and w in p) for w in W]
        maxdev_L2 = max(maxdev_L2, max(resid) - min(resid))
print("(L1) max |J_p^B - J_p| over basis, states without complementary pairs:", maxdev_L1)
print("(L2) max spread in w of A(B,.)-A(empty,.)-sum J_p 1_p, same states:", maxdev_L2)

# Show that the exception is real: a ME measure where the jump of p changes when not-p is believed.
# A(B,w) = sum_{p in B} 1_p(w) + 5*[ {1} in B and {2,3} in B and w = 1 ]  -> check ME and jump change.
def Aex(B, w):
    return sum(1 for p in B if w in p) + (5 if (frozenset({0}) in B and frozenset({1, 2}) in B and w == 0) else 0)
ok = True
for B in STATES:
    for p in PROPS:
        if p in B:
            continue
        D = [Aex(B | {p}, w) - Aex(B, w) for w in W]
        if len({D[w] for w in W if w in p}) > 1 or len({D[w] for w in W if w not in p}) > 1:
            ok = False
p = frozenset({0})
print("exception measure satisfies ME:", ok, "; jump of {1} at empty:",
      (Aex({p}, 0) - Aex(frozenset(), 0)) - (Aex({p}, 1) - Aex(frozenset(), 1)),
      " at {{2,3}}:", (Aex(frozenset({p, frozenset({1, 2})}), 0) - Aex(frozenset({frozenset({1, 2})}), 0))
      - (Aex(frozenset({p, frozenset({1, 2})}), 1) - Aex(frozenset({frozenset({1, 2})}), 1)))
