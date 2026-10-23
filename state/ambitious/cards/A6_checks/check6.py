import sys, random
sys.path.insert(0, sys.argv[1])
from structs import *
from check1 import good_struct, binary_experiments
from checkomega import closure
from check3 import voi
random.seed(99)
def KomegaI(x, Y, geq, gg): return closure(K_I, x, Y, geq, gg)

# (1) random VOI for omega-I rule, comparable and non-comparable structures
for total, n in ((True, 4), (False, 3), (False, 4)):
    structs = []
    for i, st in enumerate(structures(n, total=total)):
        structs.append(st)
        if len(structs) > 4000: break
    neg = 0; trials = 0; minv = 0
    for t in range(3000):
        geq, gg = random.choice(structs)
        Y = frozenset(random.sample(range(n), random.randint(2, n)))
        x = random.choice(sorted(Y))
        prob = {s: random.random() + 0.05 for s in range(n)}
        for p in binary_experiments(Y):
            acts = [{s: random.uniform(-5, 5) for s in range(n)} for _ in range(3)]
            v = voi(KomegaI, x, Y, p, geq, gg, prob, acts)
            trials += 1; minv = min(minv, v)
            if v < -1e-9: neg += 1
    print("omega-I", "total" if total else "partial", n, "trials", trials, "negative", neg, "min", minv)

# (2) I-normality situations with K=omega but not good_struct: search for negative VOI
n = 4; found = 0; cases = 0
structs = list(structures(n, True))
for geq, gg in structs:
    for Y in subsets(n):
        for x in Y:
            if K_I(x, Y, geq, gg) == closure(K_I, x, Y, geq, gg) and not good_struct(K_I, x, Y, geq, gg):
                cases += 1
                if cases > 300: break
                hit = False
                for t in range(400):
                    prob = {s: random.random() + 0.05 for s in range(n)}
                    for p in binary_experiments(Y):
                        acts = [{s: random.uniform(-5, 5) for s in range(n)} for _ in range(3)]
                        if voi(K_I, x, Y, p, geq, gg, prob, acts) < -1e-9:
                            hit = True; break
                    if hit: break
                found += hit
print("I-normality omega-but-not-laminar cases tested:", min(cases, 300), "negative VOI found in:", found)
