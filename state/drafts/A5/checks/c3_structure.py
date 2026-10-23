# C3. Structure of expected-accuracy optima under the record measure, exhaustive check on n = 3 and n = 4 worlds.
# Record measure (proposition-dependent version):
#   A(B,w) = sum_{p in B} (T_p if w in p else -F_p) + beta*[w in cap B]
#   EA(B) = sum_{p in B} e_p + beta*C(cap B),   e_p = C(p)(T_p+F_p) - F_p
# Claim (Theorem 3 in the essay):
#   max_B EA(B) = max_X Phi(X),  Phi(X) = sum_{p superset of X} max(e_p,0) + beta*C(X)
#   B is optimal iff Phi(cap B) is maximal, B contains every p ⊇ cap B with e_p>0, and no p with e_p<0.
# Corollaries checked for uniform T,F (tau = F/(T+F)), generic C:
#   (k1) the maximising core X* is "filtered": every world in X* is at least as probable as every world outside it;
#   (k2) the optimum is deductively closed (contains cap B) iff C(X*) > tau;
#   (k3) the optimum is consistent iff X* nonempty; upward closed (closed under single-premise entailment).
# Integer arithmetic throughout: credences are integers over N.
import itertools, random
import numpy as np

def run(n, trials, seed, uniform=True, N=1000):
    rng = random.Random(seed)
    worlds = list(range(n))
    props = list(range(1 << n))                       # bitmask of worlds
    nP = len(props); nS = 1 << nP
    # membership matrix and caps for all states
    S = np.arange(nS, dtype=np.int64)
    member = ((S[:, None] >> np.arange(nP)[None, :]) & 1).astype(np.int64)   # nS x nP
    cap = np.full(nS, (1 << n) - 1, dtype=np.int64)
    for s in range(1, nS):
        low = (s & -s).bit_length() - 1
        cap[s] = cap[s & (s - 1)] & props[low]
    popcount = lambda m: bin(m).count("1")
    bad = 0; k1 = k2 = k3 = 0; checked = 0
    for _ in range(trials):
        # random integer credences summing to N
        cuts = sorted(rng.sample(range(1, N), n - 1))
        Cw = [b - a for a, b in zip([0] + cuts, cuts + [N])]
        if min(Cw) == 0:
            continue
        Cp = [sum(Cw[w] for w in worlds if (m >> w) & 1) for m in props]
        if uniform:
            T = rng.randint(1, 5); F = rng.randint(T + 1, 10)      # Conservativeness T < F
            Tp = [T] * nP; Fp = [F] * nP
        else:
            Tp = [rng.randint(1, 6) for _ in props]; Fp = [rng.randint(1, 9) for _ in props]
        beta = rng.randint(1, 12)
        # scaled by N: e_p*N = Cp*(T+F) - F*N ; beta*C(X)*N = beta*C_int(X)
        e = np.array([Cp[i] * (Tp[i] + Fp[i]) - Fp[i] * N for i in range(nP)], dtype=np.int64)
        if (e == 0).any():
            continue
        Cint = np.array(Cp, dtype=np.int64)
        EA = member @ e + beta * Cint[cap]
        m = EA.max(); opt = set(np.nonzero(EA == m)[0].tolist())
        # predicted
        phi = {X: sum(max(int(e[p]), 0) for p in props if (p & X) == X) + beta * Cp[X] for X in props}
        mphi = max(phi.values())
        pred = set()
        for s in range(nS):
            X = int(cap[s])
            if phi[X] != mphi:
                continue
            ok = True
            for p in props:
                inB = (s >> p) & 1
                if e[p] < 0 and inB: ok = False; break
                if e[p] > 0 and (p & X) == X and not inB: ok = False; break
            if ok:
                pred.add(s)
        checked += 1
        if pred != opt or m != mphi:
            bad += 1
            continue
        if uniform and len(opt) == 1:
            s = next(iter(opt)); X = int(cap[s])
            # k1 filtered core
            inside = [Cw[w] for w in worlds if (X >> w) & 1]; outside = [Cw[w] for w in worlds if not (X >> w) & 1]
            if inside and outside and min(inside) < max(outside):
                k1 += 1
            # k2 closure iff C(X*) > tau  <=>  e_X > 0
            closed = bool((s >> X) & 1)
            if closed != (e[X] > 0):
                k2 += 1
            # k3 upward closure
            for p in props:
                if (s >> p) & 1:
                    for q in props:
                        if (q & p) == p and not (s >> q) & 1:
                            k3 += 1
    print(f"n={n} uniform={uniform}: instances checked={checked}, mismatches with Theorem 3={bad}"
          + (f", unfiltered cores={k1}, closure-criterion failures={k2}, upward-closure failures={k3}" if uniform else ""))

run(3, 400, 1, uniform=True)
run(3, 400, 2, uniform=False)
run(4, 60, 3, uniform=True)
run(4, 30, 4, uniform=False)

# The 4-world case from the kill test: P=(0.62,0.18,0.10,0.10), T=1, F=2, beta=3 (scaled by 100).
n = 4; N = 100; Cw = [62, 18, 10, 10]; T, F, beta = 1, 2, 3
props = list(range(16))
Cp = [sum(Cw[w] for w in range(n) if (m >> w) & 1) for m in props]
e = [Cp[p] * (T + F) - F * N for p in props]
best = None
for s in range(1 << 16):
    X = 15
    for p in props:
        if (s >> p) & 1: X &= p
    v = sum(e[p] for p in props if (s >> p) & 1) + beta * Cp[X]
    if best is None or v > best[0]: best = (v, [s])
    elif v == best[0]: best[1].append(s)
name = lambda m: "".join(str(w + 1) for w in range(n) if (m >> w) & 1) or "{}"
for s in best[1]:
    B = [name(p) for p in props if (s >> p) & 1]
    print("4-world case: EA*100 =", best[0], "optimum:", B, "| contains {1}?", "1" in B, "| contains 12 and 13?", "12" in B and "13" in B)
