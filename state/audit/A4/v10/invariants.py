"""Delta invariants v8 -> v10: math spans, quotations, citation parentheticals, numbers, references."""
import re, sys, collections
a = open(sys.argv[1]).read(); b = open(sys.argv[2]).read()
def body(t): return t.split('## References')[0]
def refs(t): return [l.strip() for l in t.split('## References')[1].splitlines() if l.strip()]
def math(t): return re.findall(r'\$\$.*?\$\$|\$[^$]+\$', t, flags=re.S)
def quotes(t): return re.findall(r'"[^"]+"|“[^”]+”', t)
def cites(t): return re.findall(r'\([^()]*\b(?:19|20)\d\d\b[^()]*\)|\b[A-Z][a-z]+(?: and [A-Z][a-z]+)?(?:\'s)? \((?:19|20)\d\d[^)]*\)', t)
def nums(t):
    t2 = re.sub(r'\$\$.*?\$\$|\$[^$]+\$', ' ', t, flags=re.S)
    return re.findall(r'\b\d[\d,.–-]*\b', t2)
for name, f in [('math', math), ('quotes', quotes), ('cites', cites), ('nums', nums)]:
    ca, cb = collections.Counter(f(body(a))), collections.Counter(f(body(b)))
    print(f'{name}: v8={sum(ca.values())} v10={sum(cb.values())} identical_multiset={ca==cb}')
    if ca != cb:
        print('  only v8 :', dict(ca - cb)); print('  only v10:', dict(cb - ca))
print('references identical:', refs(a) == refs(b), len(refs(a)), len(refs(b)))
# theorem/lemma/corollary/proof paragraph identity
def blocks(t): return [p for p in body(t).split('\n\n') if re.match(r'\s*(\*\*(Theorem|Lemma|Corollary)|\*Proof\.)', p)]
print('theorem/lemma/corollary statements identical:', [p for p in blocks(a) if not p.startswith('*Proof')] == [p for p in blocks(b) if not p.startswith('*Proof')])
na = ' '.join(' '.join(blocks(a)).split()); nb = ' '.join(' '.join(blocks(b)).split())
print('Theorem1 proof text v8 contained in v10 (whitespace-normalised, joined):',
      ' '.join(re.search(r'\*Proof\.\* A modified witness.*?∎', a, re.S).group(0).split()) ==
      ' '.join(re.search(r'\*Proof\.\* A modified witness.*?∎', b, re.S).group(0).split()))
