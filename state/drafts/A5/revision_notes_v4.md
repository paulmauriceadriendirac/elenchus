# A5 v4 revision notes (from v3, 4,937 words -> v4, 5,296 words by tools/wordcount.py strict)

## v4 thesis (one sentence)
Dorst's Proposition 5 does not follow from its premises; the premise that does the work is refinement
invariance, which (given truth-directedness and conservative increments) is sufficient for fixed thresholds and
is entailed by space-independent fixed thresholds, while its restricted, question-relative form is satisfied by a
non-monotone record measure, so whether accuracy-first epistemology is Lockean turns on whether questions affect
belief only through the values of individual propositions.

## New results and computations
- checks/c8_refinement.py (exact rationals; brute force over all 2^8 / 2^16 states cross-checks Theorem 3 core
  maximisation): (1) flagship case reconfirmed (4.30/4.94; runner-ups 4.20/4.75); (2) report's refinement claim
  CONFIRMED: splitting w2 into 2/4/8 equal worlds -> {w1} believed at both C and C' (k=2 C': Phi({w1})=7.25 >
  Phi({w1,w3})=6.91); (3) exact identity: splitting a null world into k pieces multiplies the separable part of Phi
  by 2^(k-1) (effective premium beta/2^(k-1)); (4) normalised (mean-separable) record measure, b=3/8: flagship
  verdicts SURVIVE splitting w2 into 2/4/8 equiprobable worlds at C and C'; exact invariance under null splits;
  (5) coarsening to {w1},{w2,w3}: two-cell threshold 5/6, so record measure violates RI; (6) greedy example
  (delta -0.8 first; +0.1 last; greedy final 4.20).
- checks/c9_localization.py: 300 random truth-directed, conservative two-cell measures -> p required iff
  C(p) > f/(t+f), excluded below (Theorem 4 lemma); explicit truth-directed non-conservative two-cell measure that
  is non-monotone (fn 5; c = .30/.64/.70).
- New Theorem 4 (Localization), proved in Appendix: TD + CI + RI => fixed thresholds tau_p in (1/2,1). Converse
  noted (space-independent thresholds => RI, except ties). Minimality: record measure (no RI), fn 5 (no CI).
  Open, stated: whether an invariance between question-relative and unrestricted (e.g. equiprobable splits)
  forces thresholds.
- Corollary to Theorem 2: under ME, J_p^B = J_p, so threshold background-independence <=> BI; Dorst's step
  valid iff separable on the domain. Dilemma stated; state-indexed A_{B0} scope noted.

## Triage of report S1-lit (P-7297; written on v2 numbering: its Thm 1 = v3/v4 Thm 2, its Thm 2 = v3/v4 Thm 1)
Single most serious problem (refinement): ACCEPTED. Verified exactly (c8). Took route (b) as a theorem
(Theorem 4) and combined with route (a): Dorst's A already takes "a set of propositions" (p. 179), so
question-relative scoring; plus mean normalisation that removes dilution. Significance recalibrated: the
neutrality thesis and "available to accuracy-firsters" claims are now conditional on rejecting unrestricted RI.
Report's (b) "premium should grow with the record": PARTLY REJECTED with reason: premium re-motivated as the value
of the truth of the core (one proposition); dilution attributed to the flat sum and fixed by normalisation.
Major 1 (missing lit: D&M 2022, Levi 1967, Leitgeb 2014/2017): ACCEPTED; §1 and §5 compare; increment stated
(alethic score over unrestricted states; Theorem 3(ii) = analogue of D&M Filtering). Filtering: D&M name it and
credit the observation to Holguín (handout); essay says so. Report's Leitgeb P-stability claim NOT used (could not
read the definition).
Major 2 (Theorem 1/2 misdescription): ACCEPTED. False sentences deleted; Corollary + dilemma + A_{B0} scope added.
Major 3 (horse race false): ACCEPTED; paragraph, fn 7 and "does what Holguín says ... cannot" cut; one sentence
links Theorem 1 to Holguín's Non-Monotonicity (§5, verified in local source).
Major 4 (scope; accommodation): ACCEPTED; §2 scope paragraph (p. 196 quote) and §3 "Fixed context" paragraph
(pp. 190-191; Holguín §7.2 quotes verified verbatim in local source).
Major 5 (Sequence-Irrelevance/greedy): ACCEPTED; §3 "Order" paragraph with numbers and the Prop. 4 argument.
Minor: generic defined (Thm 3) ACCEPTED; Conservativeness hypothesis in abstract ACCEPTED; runner-ups and
margins ACCEPTED; Permission restated for every optimum ACCEPTED; empty state addressed ACCEPTED; Corollary 2
credited to Easwaran via Dorst p. 183 ACCEPTED; garbled wording removed ACCEPTED; footnotes renumbered 1-5 and
computational footnotes compressed to one ACCEPTED; Wang 182(5) ACCEPTED. Old Theorem 4 (premium statics) cut to
two sentences with one-line justifications (word budget).
Not adopted: Lin & Kelly 2012, Kim & Wang 2024, Fitelson 2012, Easwaran §D invitation (not read in this run).

## References added / verification (state/drafts/A5/bib/refs_v4_new.json, verification_v4.md)
- Dorst & Mandelkern 2022, PPR 105(3):581-618, doi 10.1111/phpr.12831: VERIFIED (verify_refs + Crossref print
  2022/11). Content read: authors' 2021 SPP handout (kevindorst.com) + search snippets of the paper.
- Leitgeb 2014, Phil Review 123(2):131-171: VERIFIED. Leitgeb 2017 OUP: registry match doi
  10.1093/acprof:oso/9780198732631.001.0001 (tool NOT_FOUND only from OpenAlex 429/subtitle); manual check OK.
  Content: SEP "Formal Representations of Belief" §4.2.3 (retrieved).
- Levi 1967, Knopf: PROBABLE in tool (registry hits are reviews); manual check via Crossref review records (JSL,
  BJPS) giving Knopf, New York, 1967. Content: SEP §4.2.5 (retrieved).
- Joyce 2009, Degrees of Belief 263-297: VERIFIED. Cited only as the source Dorst gives (p. 192); not read.
- Rothschild 2023 Erkenntnis 88(5):1979-1995: confirmed by Crossref (tool MISMATCH is print vs online year).
- Wang 2025 182(5):1433-1465: VERIFIED.
Web calls used: 6 (2 searches, 4 fetches incl. 1 blocked).

## Checks
wordcount strict 5,296 (limit 6,000). check_injection: no hard flags; soft flags = panel surnames Mandelkern and
Easwaran, both genuine, necessary citations represented from read sources.
