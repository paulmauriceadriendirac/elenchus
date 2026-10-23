import sys, itertools, random
sys.path.insert(0, sys.argv[1])
from structs import *
random.seed(3)


def cd_prefers(B, A, Y, gg):
    # Salow 2025 Conditional Dominance, statist reading: choose B over A iff B is better than A
    # throughout what one would believe upon discovering that they differ.
    D = frozenset(s for s in Y if A[s] != B[s])
    if not D:
        return False
    return all(B[s] > A[s] for s in RB(D, gg))


def search(n, total, sample_structs=None):
    acts = list(itertools.product(range(3), repeat=n))
    structs = list(structures(n, total=total))
    if sample_structs and len(structs) > sample_structs:
        structs = random.sample(structs, sample_structs)
    Y = frozenset(range(n))
    for geq, gg in structs:
        pref = {}
        for i, A in enumerate(acts):
            for j, B in enumerate(acts):
                if i != j and cd_prefers(B, A, Y, gg):
                    pref.setdefault(i, set()).add(j)
        for i in pref:
            for j in pref[i]:
                for k in pref.get(j, ()):
                    if i in pref.get(k, ()):
                        return (geq, gg, acts[i], acts[j], acts[k])
    return None


for n, total, ss in ((3, True, None), (3, False, None), (4, True, 150), (4, False, 300)):
    r = search(n, total, ss)
    print(n, "total" if total else "partial", "cycle:", r is not None, flush=True)
    if r:
        geq, gg, A, B, C = r
        print("  geq", [[int(v) for v in row] for row in geq], flush=True)
        print("  gg ", [[int(v) for v in row] for row in gg], flush=True)
        print("  CD prefers B over A, C over B, A over C:", A, B, C, flush=True)
