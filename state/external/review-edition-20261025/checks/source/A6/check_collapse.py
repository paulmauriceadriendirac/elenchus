# Q2. Exhaustive over statist structures, n <= 4 states (comparable) and n <= 3 (non-comparable),
# all evidence sets E, situations x in E, informative questions (all partitions of E):
#  (a) RELATIVE DEFEAT at (x,E,Pi): some s in K(x) has post-discovery ken K'(s) not within K(x).
#  (b) GAP: every member of K(x) is >> every member of E \ K(x).
#  (c) EPS-CONSTRUCTION: when relative defeat holds, build the decision problem
#        bet1 = 1 on K(x), -L off, plus eps*zeta;  bet2 = same bet;  decline = 0
#      with zeta = +N at a defeated state s0, -1 elsewhere, and check that BOTH unconditional KDT
#      and the conditional rule CEU strictly prefer bet1-now to looking.
#  (d) CEU never fails Good where there is no relative defeat (random problems).
#  (e) MARGINS views: net value of evidence  V(Pi) - V(null)  (null = defer with no new evidence)
#      -- is it ever negative?  (separates evidence-driven from self-trust-driven failures)
# Run: python3 -I check_collapse.py <this dir>
import sys, random
sys.path.insert(0, sys.argv[1])
from structs import structures, subsets
from kdt import *
random.seed(7)

def rel_defeat(ken, x, E, cells, rel):
    K0 = ken(x, E, rel)
    for c in cells:
        F = E & c
        for s in K0 & F:
            K1 = ken(s, F, rel)
            if not K1 <= K0:
                return s, K1
    return None

def gap(ken, x, E, rel):
    K0 = ken(x, E, rel); _, gg = rel(E)
    return all(gg(k, v) for k in K0 for v in E - K0)

def eps_problem(K0, s0, n, L=1e6, N=None, eps=1e-4, P=None):
    PK = sum(P[s] for s in K0)
    if N is None:
        N = 2 * PK / P[s0] + 1
    zeta = {s: (N if s == s0 else -1.0) for s in range(n)}
    bet = {s: (1.0 if s in K0 else -L) for s in range(n)}
    bet1 = {s: bet[s] + eps * zeta[s] for s in range(n)}
    return [bet1, dict(bet), {s: 0.0 for s in range(n)}]

def plan_value(plan, K, P):
    return eu(plan, K, P)

def run(n, total, kenname):
    ken = KENS[kenname]
    st = dict(sit_q=0, reldef=0, gap_and_reldef=0, nogap_no_reldef=0, eps_kdt_fail=0, eps_ceu_fail=0,
              ceu_fail_without_reldef=0, kdt_fail_without_reldef=0, net_neg=0, net_trials=0)
    for geq_m, gg_m in structures(n, total=total):
        geq = lambda a, b, g=geq_m: g[a][b]
        gg = lambda a, b, g=gg_m: g[a][b]
        rel = lambda F, r=(geq, gg): r
        for E in subsets(n):
            if len(E) < 2: continue
            for x in E:
                K0 = ken(x, E, rel)
                g = gap(ken, x, E, rel)
                for cells in partitions(E):
                    st['sit_q'] += 1
                    rd = rel_defeat(ken, x, E, cells, rel)
                    if rd:
                        st['reldef'] += 1
                        if g: st['gap_and_reldef'] += 1
                        s0, _ = rd
                        P = {s: random.random() + 0.05 for s in range(n)}
                        acts = eps_problem(K0, s0, n, P=P)
                        if kdt_value(ken, x, E, cells, rel, acts, P) < -1e-12:
                            st['eps_kdt_fail'] += 1
                        plan, _, _ = look_plan(ken, E, cells, rel, acts, P)
                        _, CK, m = ceu_prefers_act_over_look(x, E, plan, acts[0], P,
                                       lambda D: cond_ken(x, E, D, (geq, gg), (geq, gg)), tol=0)
                        if m > 1e-12:
                            st['eps_ceu_fail'] += 1
                    else:
                        for t in range(4):
                            P = {s: random.random() + 0.05 for s in range(n)}
                            acts = [{s: random.uniform(-5, 5) for s in range(n)} for _ in range(3)]
                            if kdt_value(ken, x, E, cells, rel, acts, P) < -1e-9:
                                st['kdt_fail_without_reldef'] += 1
                            plan, _, _ = look_plan(ken, E, cells, rel, acts, P)
                            for a in acts:
                                _, CK, m = ceu_prefers_act_over_look(x, E, plan, a, P,
                                               lambda D: cond_ken(x, E, D, (geq, gg), (geq, gg)))
                                if m > 1e-9:
                                    st['ceu_fail_without_reldef'] += 1
                    # (e) net value of evidence relative to the null question
                    for t in range(3):
                        P = {s: random.random() + 0.05 for s in range(n)}
                        acts = [{s: random.uniform(-5, 5) for s in range(n)} for _ in range(3)]
                        planQ, _, _ = look_plan(ken, E, cells, rel, acts, P)
                        plan0, _, _ = look_plan(ken, E, [E], rel, acts, P)
                        st['net_trials'] += 1
                        if eu(planQ, K0, P) - eu(plan0, K0, P) < -1e-9:
                            st['net_neg'] += 1
                if not g:
                    if not any(rel_defeat(ken, x, E, cells, rel) for cells in partitions(E)):
                        st['nogap_no_reldef'] += 1
    return st

if __name__ == '__main__':
    for kn in ('K', 'I', 'KM'):
        for n in (2, 3, 4):
            print(kn, 'comparable', n, run(n, True, kn), flush=True)
        for n in (2, 3):
            print(kn, 'non-comparable', n, run(n, False, kn), flush=True)

