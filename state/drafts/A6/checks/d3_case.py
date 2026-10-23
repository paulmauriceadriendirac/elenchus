# Goodman & Salow's modified Flipping for Heads (G&S 2023 p.138; BRN App. D.3), as a simple
# probability structure (BRN Def. 6.2): states s_j (first heads on flip j), Pr(s_j) = 2^-j (truncated at M),
# possible bodies of evidence S, q = {s_1} ∪ {s_j : j >= n+1}, S \ q.  Threshold t.  K-normality.
# Decision at x = s_1: bet that the coin is flipped at most n times (pays 1, else -L), or decline (0).
# Free question {q, S\q}.  Compare: KDT; CEU with BRN conditional knowledge (D-restricted accessibility,
# >> relative to the current evidence S); CEU with the discovery reading (>> relative to S∩D).
M, n, t, L = 60, 4, 0.9, 20.0
S = frozenset(range(1, M + 1))
pr = {j: 2.0 ** -j for j in S}
def Pc(A, F): return sum(pr[s] for s in A & F) / sum(pr[s] for s in F)
def geq(F): return lambda a, b: pr[a] >= pr[b]
def gg(F):
    def r(a, b):
        if not (pr[a] > pr[b]): return False
        lower = frozenset(s for s in F if pr[a] >= pr[s])
        more_than_b = frozenset(s for s in lower if pr[s] > pr[b])
        return Pc(more_than_b, lower) >= t - 1e-15
    return r
def B(F, g=None):
    g = g or gg(F)
    return frozenset(v for v in F if not any(g(u, v) for u in F))
def K(x, F): return B(F) | frozenset(v for v in F if pr[v] >= pr[x])
q = frozenset([1]) | frozenset(j for j in S if j >= n + 1); notq = S - q
bet = {s: (1.0 if s <= n else -L) for s in S}; dec = {s: 0.0 for s in S}
def eu(a, A): return sum(pr[s] * a[s] for s in A) / sum(pr[s] for s in A)
x = 1
K0 = K(x, S)
print("B(S) =", sorted(B(S)), " K(s1) =", sorted(K0))
print("B(q) =", sorted(B(q)), " K_q(s1) =", sorted(K(1, q)), " B^q(S) [BRN D.2] =", sorted(B(q, gg(S))))
plan = {}
for s in S:
    F = q if s in q else notq
    Ks = K(s, F)
    plan[s] = bet[s] if eu(bet, Ks) > 0 else 0.0
print("KDT: value now %.3f, value of looking %.3f -> %.3f" % (eu(bet, K0), eu(plan, K0), eu(plan, K0) - eu(bet, K0)))
D = frozenset(s for s in S if plan[s] != bet[s])
print("D (states where looking changes the payoff) == q:", D == q)
CK_brn = B(S & D, gg(S)) | frozenset(v for v in S & D if pr[v] >= pr[x])
CK_disc = K(x, S & D)
for name, CK in (("BRN D.2 reading", CK_brn), ("discovery reading", CK_disc)):
    m = sum(pr[s] * (plan[s] - bet[s]) for s in CK) / sum(pr[s] for s in CK)
    print("CEU, %s: CK = %s; E[look - bet | CK] = %.3f -> %s" % (name, sorted(CK), m,
          "prefers betting now (refuses free evidence)" if m < 0 else "prefers looking"))
print("Pr(p | S) = %.4f, Pr(p | q) = %.4f" % (Pc(frozenset(range(1, n + 1)), S), Pc(frozenset(range(1, n + 1)), q)))
