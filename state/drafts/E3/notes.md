# E3 notes (v1)

**Title.** Flattening Fails for Counterfactuals: Cumulative Supposition and Nested Conditionals

**Thesis (one sentence).** Flattening, (p>((p∧q)>r)) ≡ ((p∧q)>r), is false for counterfactuals, because it encodes the cumulativity of supposition, which conditioning (indicative supposition) has and counterfactual supposition (imaging) lacks; so it is at most a principle for indicatives.

**Map open problems addressed.** §5a.1 (intuitive semantics for Flattening / C2.F, D&M §4.1): answered negatively for counterfactuals and turned into a precise requirement (cumulativity). §5a.2 (probabilistic route to Flattening, D&M §7): partial, at the level of probability only. Also §5b.8 (Flattening vs full IE) and bears on §5a.9 (unified "if") and §5a.7 (complex antecedents in interventionism).

**Closest prior work and increment.** Dorr & Mandelkern 2026 (C2.F / C2.FS as logics of sequence semantics; note that similarity cannot validate Flattening; leave intuitive semantics and probabilistic route open). Increment: (1) a semantics-independent argument: in C2.F, ¬(A>B), ¬(B>A) ⊢ (A∨B)>[(A∧(B>¬A))∨(B∧(A>¬B))] (Theorem 1), false in the Reunion / Buttons cases; plus Proposition 2: each half of Flattening fails in any logic containing CK (no CEM needed). (2) Theorem 3: Flattening valid on a selection frame iff (Flat) iff imaging cumulative for all Pr. (3) Proposition 4: given Stalnaker's Thesis for the two conditionals, Flattening-equiprobability iff restricted Factorization (RS); RS escapes Lewis's argument and holds non-trivially in Stalnaker–Bernoulli models. Plus interventionist observation: conjunctive-setting antecedents satisfy Flattening (interventions compose); failures need multiply realizable outer antecedents.

**Checks run.** z3: C2 selection frames on 4 and 5 worlds, with (Flat) premises+¬D unsat, without sat; Reunion weighted-mismatch model is C2 and satisfies N1, N2, P2, ¬D, P3. Exact-rational check of SB identities (RS, Flattening equiprobability, failure of unrestricted Factorization). Scripts were in scratchpad (not kept in repo).

**Three weakest points a referee would attack.**
1. Novelty of the core: D&M already say similarity does not validate Flattening; a referee may judge Theorem 1 and Theorem 3 to be routine frame-correspondence facts dressed up. The defence (semantics-independent premises; minimal CK version; imaging reading) needs to persuade. I have not read D&M §4.1 or §7 myself (map only): they may already give a counterfactual counterexample or the imaging reading, which would sink the increment. Must check against the full text.
2. The indicative half is thin: §5 only argues the case does not transfer and that the probabilistic content is (RS); it does not establish Flattening for indicatives, and the step from equiprobability to validity is left open. The indicative counterpart of (D) is dismissed rather briskly.
3. Dialectic on SDA / hyperintensional antecedents and counterfactual skepticism: replies rely on the existential reformulation ("someone from their year") and on the Buttons; an alternative-semantics theorist may treat existentials as alternative-generating, and the claim that Lewis-1979 similarity yields N1/N2 in the Buttons is asserted, not proved.

**Citation cautions.** All cited works are VERIFIED or manual in refs.json; most attributions rest on abstracts or SEP (as in map). No direct quotations. Missing but relevant (not in refs.json, so not cited): Darwiche & Pearl's iterated-revision postulate (C1) is a close analogue of Flattening under a Ramsey-test reading; Chellas for CK; Kaufmann/Stalnaker–Bernoulli literature. Verify and consider adding. Lewis 1976 page range omitted (only start page verified).

**Word count.** strict 5158 (wordlike 5046), tools/wordcount.py, excluding references.
