# C4. Theorem 2 (robustness): for all 0 < T < F and beta > 0, on W = {1,2,3}, with S = T+F and tau = F/S,
#   c0 = (2F + beta - T)/(2S + beta),  c1 = (2F + beta)/(2S + beta),
# for any c, c' with max(c0, tau) < c < c' < c1:
#   {1} belongs to the unique optimum at C = (c, (1-c)/2, (1-c)/2), and
#   {1} belongs to no optimum at C' = (c', eps, 1-c'-eps) for all small enough eps >= 0.
# Exhaustive exact check over all 256 belief states (all 8 propositions), for a spread of parameters.
import itertools
from fractions import Fraction as Fr

W = (0, 1, 2)
PROPS = [frozenset(c) for r in range(0, 4) for c in itertools.combinations(W, r)]
STATES = [frozenset(p for p, b in zip(PROPS, bits) if b) for bits in itertools.product([0, 1], repeat=len(PROPS))]
P1 = frozenset({0})

def EA(B, C, T, F, beta):
    X = frozenset(W)
    for p in B: X &= p
    return sum(sum(C[w] for w in p) * (T + F) - F for p in B) + beta * sum(C[w] for w in X)

def optima(C, T, F, beta):
    vals = [(EA(B, C, T, F, beta), B) for B in STATES]
    m = max(v for v, _ in vals)
    return [B for v, B in vals if v == m]

cases = [(1, 2, Fr(1, 100)), (1, 2, Fr(1, 2)), (1, 2, 3), (1, 2, 50), (1, 2, 1000), (2, 3, 1), (1, 10, 2), (5, 6, Fr(1, 10)), (3, 4, 20)]
allok = True
for T, F, beta in cases:
    T, F, beta = Fr(T), Fr(F), Fr(beta)
    S = T + F; tau = F / S
    c0 = (2 * F + beta - T) / (2 * S + beta); c1 = (2 * F + beta) / (2 * S + beta)
    lo = max(c0, tau)
    c = lo + (c1 - lo) / 3; cp = lo + 2 * (c1 - lo) / 3
    C = (c, (1 - c) / 2, (1 - c) / 2)
    o = optima(C, T, F, beta)
    ok1 = len(o) == 1 and P1 in o[0]
    ok2 = True
    for eps in (Fr(0), (1 - cp) / 1000, (1 - cp) / 100000):
        Cp = (cp, eps, 1 - cp - eps)
        if any(P1 in B for B in optima(Cp, T, F, beta)):
            ok2 = False
    allok &= ok1 and ok2
    print(f"T={T} F={F} beta={beta}: tau={float(tau):.4f} c0={float(c0):.4f} c1={float(c1):.4f} "
          f"c={float(c):.4f} c'={float(cp):.4f}  believed at C: {ok1}  not believed at C': {ok2}")
print("all cases confirm Theorem 2:", allok)

# Necessity of the interval's upper end at the concentrated point: just above c1, {1} is believed again at (c',0,1-c').
T, F, beta = Fr(1), Fr(2), Fr(3)
c1 = (2 * F + beta) / (2 * (T + F) + beta)
cp = c1 + Fr(1, 1000)
print("beta=3: at c' = c1 + 0.001 (concentrated), {1} believed:", all(P1 in B for B in optima((cp, Fr(0), 1 - cp), T, F, beta)))

