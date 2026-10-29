# Formal audit — A6 v4 (PARTIAL, in progress)

Essay: state/drafts/A6/v4.md. Independent code: state/audit/A6/formal/ (pending).

## Hand-checked so far (computation pending)

- Lemma 1, Lemma 2 (A.1), Lemma 3 (A.2), Lemma 4, Theorem 1 (A.3), Theorem 2 + Corollary (A.4), Theorem 3 (A.6), CKD silence, Props 4–5 (A.7): proofs read line by line; no gap found yet except as noted below.
- A.5 (Bjorn, positive-measure argument; Cauchy–Schwarz weight bound; (1+sqrt2)^2 c^2 threshold): checked by hand, correct.
- Source match (Goodman & Salow 2023): structural assumptions (i)–(iii) p.92; COLLAPSE, COMPARABILITY p.100; K-NORMALITY p.104; "given TRANSPARENCY, K-NORMALITY entails KK" p.107; BELIEF p.112–113; Bjorn two-scale model p.126; "loses knowledge" |x-y|>(2-sqrt2)c p.127; STATISM and "together entail NO DEFEAT" p.128; Gaussian assumptions p.129; n.40 p.130; n.47 p.138 — all match.
- Open issue found: "1,724 of the 2,322 situation–question pairs with relative defeat" (§5.2) vs "3,306 with relative defeat" (Computations). The author's own output shows 2,322 is for E = whole state space only; the essay does not say so.
- Open issue: "probability about 0.37, as BRN estimate" — my hand computation of Pr(|d| > (2-sqrt2)c) gives about 0.42 at c=1.96; to be checked numerically.
