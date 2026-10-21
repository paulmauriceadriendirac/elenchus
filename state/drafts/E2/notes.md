# E2 notes (v1)

**Thesis (one sentence).** Among globally evidentially constant update rules, the expected-accuracy-optimal rule for any weighting of learning situations conditions the prior on the proposition that one's evidence is E, and it coincides with conditionalization on E iff the weighting is content-sufficient (every E-world equally likely to yield exactly E). So the global argument for conditionalization rests on a symmetry assumption about learning, not on availability.

**Closest prior work and increment.**
- Meehan & Zhang 2025 (R5 in map; known to us only via abstract + Pettigrew's blog reconstruction): with uniform weight over all factive evidence functions, conditionalization uniquely maximizes total expected accuracy among globally constant rules.
- Schoenfield 2017 (R4) and Greaves & Wallace 2006 (R2).
- Increment: (i) Theorem 1 characterizes the optimal constant rule for arbitrary families/weightings (including world-correlated ones); R2, R4 and (regimented) R5 are Corollaries 2, 1, 3. (ii) Theorem 2: conditionalization optimal iff content-sufficiency (the analogue of "coarsening at random" in statistics, named without citation). (iii) Prop 3: content-sufficiency holds for any mixture of partitional functions; can hold with only non-partitional functions (Two Cyclic Informants); fails for a point mass on any non-partitional function; content-sufficient weightings are Lebesgue-null. (iv) Cor 4: uniform weight over all (incl. non-factive) functions yields no updating. (v) Prop 4: conditionalization is not minimax-optimal; the never-update rule is.
- Philosophical upshot: refutes the "the dispute reduces to availability" moral (reported in map via Pettigrew's blog; stated impersonally in the essay).

**Map open problem addressed.** §5 open problem 11 (availability: Schoenfield vs Meehan–Zhang) and pressure point I2 (non-uniform weights may break uniqueness of conditionalization; no robustness analysis found).

**Formal checks.** /tmp/claude-0/-home-user-elenchus/0999555b-7b80-5958-88f6-1f601c103b28/scratchpad/check.py (numpy + exact Fractions, |W|=3): Theorem 1 under Brier/spherical/log (200 random priors x weightings, no improving perturbation); Cor 3, Cor 4; Two Instruments (q = (1/3,2/3,0); exp. Brier 2/9 vs 1/4); cyclic case content-sufficient and equal to conditionalization; mixtures of partitions content-sufficient; minimax counterexample V(C)=144567/242000 > V(R0)=117/200.

**Three weakest points a referee would attack.**
1. Fidelity to Meehan & Zhang: their full text was not read. The essay regiments their theorem from the abstract/map statement and argues (Obj. 5) that Theorem 1 covers any family/weighting. But if their framework has a different notion of rule (e.g. rules that also take the prior, or the evidence function's structure, as input) or a non-expectational evaluation, the critique may miss. The full text must be checked before submission (fetch already filed per map).
2. Technical modesty: Theorem 1's proof is a short separability-plus-propriety argument; a referee may say the core is "obvious" once stated and that the CAR condition is well known in statistics (Grünwald & Halpern 2003; Heitjan & Rubin 1991 are candidates to verify and cite). The value is in the corollaries and the diagnosis; that must be pressed harder if a referee says so.
3. The dilemma's evaluative horn: the reply to Objection 1 concedes the impartial standard is coherent; a defender can say that rules are properly assessed impartially (rule-consequentialist style) and that agent-relative expectation is the wrong standard for rules. The essay's answer (it departs from expected-accuracy methodology; impartiality != symmetry among worlds) is only a partial reply.

**Citations.** Only works VERIFIED by tools/verify_refs.py this session (output: scratchpad cite.verif.json): Das2019UrPrior, Easwaran2013, EaswaranNielsen2025, GreavesWallace2006, IsaacsRussell2023, Joyce1998, MeehanZhang2025, Pettigrew2016, Schoenfield2017. Gallow2021, Das2022, BriggsPettigrew2020, Pettigrew2023Bayesian came back MISMATCH (online-first vs issue year only) and were not cited. No L5 refs.verification.json existed. No quotations used.

**Word count.** tools/wordcount.py: strict 5219 (limit 6000, target 5600).
