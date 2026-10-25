# Shared machinery: knowledge-based expected utility (KDT) and its conditional variant (CEU)
# in finite normality structures. Statist structures come from structs.py (Goodman & Salow 2023
# constraints); non-statist ones are built by the caller (simple probability structures, BRN Def. 6.2).
#
# Conventions. A "relation provider" rel(F) returns (geq, gg) as functions on states, relative to
# evidence F (a frozenset).  Under statism rel(F) is the same for every F.
import itertools

def RB(F, gg):
    return frozenset(v for v in F if not any(gg(u, v) for u in F))

def ken_K(x, F, rel):            # K-normality: belief set plus states at least as normal as x
    geq, gg = rel(F)
    return RB(F, gg) | frozenset(v for v in F if geq(v, x))

def ken_I(x, F, rel):            # I-normality
    geq, gg = rel(F)
    return frozenset(v for v in F if not gg(x, v))

def ken_KM(x, F, rel):           # KM-normality
    geq, gg = rel(F)
    return RB(F, gg) | frozenset(v for v in F if any(geq(v, u) and geq(x, u) and not gg(x, u) for u in F))

KENS = {'K': ken_K, 'I': ken_I, 'KM': ken_KM}

def eu(act, K, P):
    Z = sum(P[s] for s in K)
    return sum(P[s] * act[s] for s in K) / Z

def best(acts, K, P):
    bi, bv = 0, None
    for i, a in enumerate(acts):
        v = eu(a, K, P)
        if bv is None or v > bv + 1e-12:
            bi, bv = i, v
    return bi

def look_plan(ken, E, cells, rel, acts, P):
    """Payoff function of the plan 'answer the question, then maximize EU on what you then know'."""
    plan, choice, post = {}, {}, {}
    for c in cells:
        F = E & c
        for s in F:
            K1 = ken(s, F, rel)
            i = best(acts, K1, P)
            plan[s] = acts[i][s]; choice[s] = i; post[s] = K1
    return plan, choice, post

def kdt_value(ken, x, E, cells, rel, acts, P):
    K0 = ken(x, E, rel)
    plan, _, _ = look_plan(ken, E, cells, rel, acts, P)
    return eu(plan, K0, P) - max(eu(a, K0, P) for a in acts)

def cond_ken(x, E, D, rel_cmp, geq_rel):
    """Conditional knowledge on hypothesis D (K-normality form): the states of E∩D undominated
    under the >> of rel_cmp, plus the states of E∩D at least as normal as x (geq of geq_rel)."""
    F = E & D
    _, gg = rel_cmp
    geq, _ = geq_rel
    return frozenset(v for v in F if not any(gg(u, v) for u in F)) | frozenset(v for v in F if geq(v, x))

def ceu_prefers_act_over_look(x, E, plan, act, P, CK_fn, tol=1e-9):
    """Return (D, CK, margin): margin>0 means the conditional rule strictly prefers acting now
    with `act` to looking."""
    D = frozenset(s for s in E if abs(plan[s] - act[s]) > 1e-12)
    if not D:
        return D, frozenset(), 0.0
    CK = CK_fn(D)
    Z = sum(P[s] for s in CK)
    margin = sum(P[s] * (act[s] - plan[s]) for s in CK) / Z
    return D, CK, margin

def binary_questions(E):
    Es = sorted(E)
    out = []
    for m in range(1, (1 << len(Es)) - 1):
        p = frozenset(Es[i] for i in range(len(Es)) if m >> i & 1)
        if min(p) == min(Es):          # each unordered split once
            out.append([p, E - p])
    return out

def partitions(E):
    Es = sorted(E)
    def rec(xs):
        if not xs:
            yield []
            return
        first, rest = xs[0], xs[1:]
        for part in rec(rest):
            for i in range(len(part)):
                yield part[:i] + [part[i] | {first}] + part[i+1:]
            yield part + [frozenset([first])]
    for p in rec(Es):
        p = [frozenset(c) for c in p]
        if len(p) > 1:
            yield p

