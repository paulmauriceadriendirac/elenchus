# Lane L3 — Knowledge, normality and inquiry: literature map

Lane-mapper, 2026-10-21. References: `state/lanes/L3/refs.json` (every entry carries `seen`), checked in `refs.verification.json`. **Reading levels** are given per source in §9 and in `refs.json`; "via X" marks content known only through X. PhilArchive, Wiley, T&F and OUP returned 403; eleven fetch requests filed (`requests/fetch/l3-*.md`, six high). "[Inference]" marks my own claims.

---

## 1. Scope and central questions

1. **Iteration.** Does knowing p put one in a position to know that one knows p (KK)? If KK fails, are there useful intermediate principles: Fragility, Reflective Luminosity, ω-knowledge without KK? Do higher iterations measure how good one's knowledge is?
2. **Normality.** Can inductive knowledge and justified belief be modelled by the comparative normality of the possibilities left open by one's evidence? Which structural principles hold (collapse, comparability, margins, statism, transparency)? What logic results, and what dynamics?
3. **Safety and closure.** Can a safety condition ("not easily false") be reconciled with closure under competent deduction, single- or multi-premise?
4. **Knowledge and chance.** Which principles linking objective chance to knowledge survive anti-scepticism about the future, e.g. FAIR COINS, Known Unlikelihood, Actual (Future) Unlikelihood?
5. **Dogmatism, inquiry, evidence.** If knowledge is the aim of inquiry and misleading evidence can destroy knowledge, must knowers avoid evidence (ex-ante dogmatism)? When is free evidence worth having (Good's theorem)?
6. **Norms.** Is knowledge, or something stronger (ω-knowledge, certainty) or weaker (belief, justification), the norm of assertion and of practical reasoning? How do these norms interact with iteration?

## 2. Positions and their best arguments

**2.1 KK.**
- *Anti-KK, margin for error* (Williamson 2000, ch. 5). In Goodman & Salow's words (2018, §1), the principle is "you cannot know P unless your belief that P could not easily have been mistaken". Because nearness is not transitive, knowing that one knows requires truth at the neighbours of one's neighbours. Williamson's inexact-knowledge models (2013, 2014) add Gettier cases and "improbable knowing" (via Goodman 2013).
- *Anti-KK from chance* (Goodman & Salow 2018, building on DGH 2014). KK, anti-scepticism about the future and knowledge-chance principles conflict (§3, R3–R4). This argument does not rely on margins.
- *Anti-KK from testimony about one's own iterations* (Goldstein & Hawthorne 2025, abstract). Dudley says he knows p but lacks 100 iterations of knowledge of p. If KK held, he would know that he has them, so he would not deny it.
- *Pro-KK.* (a) Normal-conditions/normality defences: Greco 2014 (via Goodman & Salow 2018 n.8 and 2023 §3), Stalnaker 2015, and the KK model of Goodman & Salow 2018. (b) Transparency of introspection lets KK sit with reliabilism (Das & Salow 2018, abstract). (c) Linguistic arguments. Any KK failure makes "If I don't know it, p" knowable and assertable (Dorst 2019; reply by Fraser 2022). Two widely accepted principles about indicative conditionals rule out "daisy chains", the epistemic states that margin-for-error arguments posit (Holguín 2021). (d) Dubious assertions ("p, but I don't know whether I know p"). Cohen & Comesaña (2013) give KK-validating models of inexact knowledge.
- *Intermediate.* Goldstein's Fragility: "whenever S knows that S doesn't know that S knows that p, S thereby fails to know p" (2022 abstract). Reflective Luminosity: "if you know that you know something, then you omega know it" (2026 abstract). Variable-margin models (2024, as described in Salow forthcoming §4). Goldstein holds that ω-knowledge is "required for rational assertion, action, inquiry, and belief" (2026 abstract). Fiat (2025) argues that full and partial knowledge can coexist *with* the margin-for-error principle.

**2.2 Normality theories.**
- *Goodman–Salow framework* (2018, 2021, 2023, 2025). Abstract guiding idea (2023): "if a possibility is sufficiently less normal than one's actual situation, then one can know that that possibility does not obtain." There are two relations, at least as normal (≽) and sufficiently more normal (≫), together with evidential accessibility R_E. Five principles (2023 §1): factivity; evidential knowledge; inductive knowledge (w ≫ v ⇒ v ∉ R_K(w)); inductive limits; convexity. Three completions:
  - **i-normality**: R_K(w) = {v ∈ R_E(w) : not w ≫ v};
  - **k-normality**: the belief worlds plus the evidential worlds at least as normal as w;
  - **km-normality**: adds margins.

  Belief (= justified belief) is R_B(w) = {v ∈ R_E(w) : no u ∈ R_E(w) with u ≫ v}. In the probabilist version, normality is evidential probability (or density) of the answers to a contextually supplied question, so believed propositions are always highly probable (TARK 2021; 2023 §5).
- *Normic support* (Smith 2016; 2018 defends JUSTIFIED FAIR COINS; 2025 PPR, abstract). Justification requires truth in all the most normal evidence-worlds. Goodman & Salow (2023 §7) object that this, with statism and "equal normality of fair-coin outcomes", forbids learning that a coin is double-headed.
- *Other normality views.* Littlejohn & Dutant 2020; Beddor & Pavese 2020 (modal virtue epistemology); Carter & Goldstein 2021 ("justification is possible knowledge", one-line summary); Goldstein & Hawthorne 2022a ("Knowledge requires belief to be true in normal cases, not in similar cases"); Goldstein & Hawthorne 2022b (normality generated from probabilities, a "Probabilistic Margin for Error", via Goodman & Salow 2023 nn.28, 40); Carter 2022 (comparative assertability = comparative normality).
- *Critics.* Loets 2022 (the strong logics need substantive normality assumptions with "unwelcome downstream consequences"); Carter 2019 (abnormal conditions can help knowledge); Hawthorne 2025 (§3, R5).

**2.3 Safety and closure.** Safety: knowledge = belief that could not easily have been false (Sosa; Williamson 2000, 2009). Williamson reconciles safety with closure by counting the premise-methods as part of the conclusion-method. Goldstein & Hawthorne (2024) argue that this "implies problematically easy epistemic access to one's methods" and reject several alternatives. Dutant & Rosenkranz (2024): because the safety counterpart relation is symmetric, safety cannot vindicate even closure under conjunction elimination once that closure is paired with the counter-closure needed to block bootstrapping. Zhao (2023): strong safety loses inductive knowledge, while weak safety loses knowledge by conjunction introduction.

**2.4 Dogmatism and the aim of inquiry.**
- *Ex-post puzzle* (Harman; Kripke 2011): if I know p, evidence against p is misleading, so I may disregard it. Standard replies, as classified by Brown 2025 nn.1–3: defeat; junk conditionals (Sorensen 1988; Hawthorne 2004); denying closure; entitlement; knowledge retained but via a bad disposition (Lasonen-Aarnio 2010, 2014).
- *Ex-ante puzzle* (Carter & Hawthorne 2024). If inquiry aims at knowledge and defeat is possible, someone who knows should decline further evidence. Their principle, as quoted in Brown 2025: "An agent must decline to gather some evidence if, by gathering that evidence, she 1) could not come to satisfy the aim of any inquiry she's engaged in, but 2) could cease to satisfy the aim of an inquiry she is engaged in". Their reply invokes a derivative norm, "You must: X only if you know that you satisfy the norm of X" (p. 661, via Brown), iterated without limit, so that agents aiming at the ideal are always also inquiring into their higher-order knowledge.
- *Rivals.*
  - Inquiry aims beyond knowledge, at maximising epistemic value of credences (Beddor 2024).
  - Personal aims (Falbo 2023; Woodard 2024; cf. Willard-Kyle 2023a).
  - Situation-sensitive norms of inquiry (Brown 2025).
  - Belief-revision principles (Salow 2025, abstract), which dissolve the puzzle "without the need for controversial theoretical commitments", against fallibilist replies.
- *Zetetic norms.* Ignorance norm, knowledge norm for inquiry (Willard-Kyle 2023b); conflicts between epistemic and zetetic norms (Friedman 2020); Millson 2020.

**2.5 Value of evidence.** Good (1967), stated informally by Ahmed & Salow: "A rational agent will make any available, free and relevant observation before choosing an act". Salow (2023) reconstructs an informal argument with four assumptions: conditionalization, "E is true" ≈ "E is what I'd learn", Sure Things, immodesty. He then shows how risk/ambiguity aversion or non-self-identifying evidence (e.g. E = K) produce counterexamples. Ahmed & Salow (2019) replace Good with "make your act depend on the answer to a question". Further: Dorst 2020 (Trust is "necessary and sufficient" for always preferring free evidence); Dorst 2023 (predictable polarisation is rational iff evidence is ambiguous, given value-of-evidence updates); Campbell-Moore & Salow 2020; Das 2023, Neth 2023 (titles only); Salow 2026 (ideal Bayesians can expect *others'* credences to get worse with more evidence).

**2.6 Norms of assertion and action.**
- KNA: "One must: assert p only if one knows p" (SEP Assertion, after Williamson 1996/2000). Rivals: truth norms; justification norms (Lackey 2007; Douven); belief and "weak assertion" (Mandelkern & Dorst 2022: "assertion is just as weak as belief"); certainty (Stanley); ω-knowledge (Goldstein). Experimental data: Turri's studies favoured factive norms. Kneer, Reuter & Brössel, and Marsili & Wiegmann favour justification (SEP §5.1.4).
- Action: knowledge as reason (Hawthorne & Stanley 2008; title only). For high stakes, iterated knowledge (Williamson 2005; Schulz 2017, which addresses Greco's "prodigality problem"). Critics: Gao 2019; Vollet 2025; Heil 2024 ("Flexible Fallibilism"); Salow (forthcoming §3.1). Weisberg 2013 reconciles knowledge-based and credence-based pictures (abstract via committee map).

## 3. Landmark results (stated as their authors state them)

- **R1. Margin-for-error vs KK** (Williamson 2000). Non-transitive nearness plus a margin requirement invalidates KK. KK in turn implies cliff-edge knowledge in Bjorn-type cases (via Goodman & Salow 2023 §3).
- **R2. Improbable knowing** (Williamson 2011, 2014, via Goodman 2013): in his models one can know p "in spite of its being overwhelmingly improbable given what you know that you know it". Goodman (2013) gives models without this feature.
- **R3. DGH tetrad** (Dorr, Goodman & Hawthorne 2014). Setup: 1000 fair coins, flipped until heads. Then (1) you know C1000 won't be flipped; (2) if you know Cn won't be flipped you know Cn−1 won't land tails; (3) if you know Cn won't land tails you know Cn won't be flipped; (4) you don't know C1 won't be flipped. These are inconsistent, so anti-scepticism refutes FAIR COINS ("If you know that a coin is fair, and for all you know it is going to be flipped, then for all you know it will land tails"). By AUTUMN LEAF, scepticism spreads to mundane knowledge of the future. Known Conditional Unlikelihood yields "rampant skepticism" (the Jack/Jill lightning case). Possible Future Unlikelihood plus Inferential Anti-dogmatism yields scepticism about chances. Survivors: Known, Actual, Known Future and Actual Future Unlikelihood; WEAK FAIR COINS.
- **R4. Goodman & Salow 2018.**
  - (a) KK, closure, knowability of WEAK FAIR COINS and anti-scepticism are jointly inconsistent (Hawthorne 2025 calls the closure-based argument "watertight").
  - (b) SETTLEDNESS, KK, anti-scepticism and knowledge of ACTUAL UNLIKELIHOOD are inconsistent. More generally, KK clashes with any defeat that one can neither rule out in advance nor check.
  - (c) A KK-validating normality model, R_K = R_B ∪ {v ∈ E : v ≽ s}, predicts KNOWN UNLIKELIHOOD in Flipping Coins. They claim its logic is "the one advocated by Stalnaker (2006), making the logic of knowledge S4.2"; the proof is "beyond the scope" (n.10).
  - (d) A million independent copies of the experiment show that conjunction closure in normality models conflicts with KNOWN UNLIKELIHOOD.
  - (e) They claim that EXTREMELY WEAK FAIR COINS ("If a coin is fair and you know that it is about to be flipped, then for all you know it will land tails") follows, in branching-time models, from two assumptions: evidence speaks decisively only to settled matters, and no flip-history is far more normal than all its tails-variants. Hawthorne (2025 n.6) disputes this claim too.
- **R5. Hawthorne 2025.**
  - (a) Radio-controlled coins (half fair, half rigged to land tails 30 times): in the Goodman–Salow KK model, an observer of 30 tails *knows* the next fair coin lands heads, which violates EXTREMELY WEAK FAIR COINS. Goodman & Salow's claim that this principle is an instance of Known Unlikelihood is a scope error: only the narrow-scope "Fantastically Weak" version follows.
  - (b) A testimonial variant (the Vandalism case) transmits inductive knowledge without insider evidence.
  - (c) Trilemma: "a KK model must either deny Weak JTB, deny Single Premise Closure, or else deny that it can happen that the strongest thing one is justified in believing entails a relevantly problematic disjunction". Here Weak JTB = "If P is the strongest proposition one justifiably believes and P is true, then one knows P"; n.12 derives it from KK plus JK.
- **R6. Epistemology Normalized** (Goodman & Salow 2023).
  - Collapse and comparability together give R_K(w) = {v ∈ R_E : v ≽ w}. km = k under collapse; km = i under comparability. i-normality excludes cliff-edge knowledge. Given transparency, k-normality entails KK.
  - Margins + comparability + statism entail no defeat. Under k-normality, Bjorn loses knowledge on a second weighing when |x − y| > (2 − √2)c.
  - Flipping for All Heads, Bus Driver, Decay and Light Bulb refute "no defeat from what you already know" and inductive anti-dogmatism ("If p together with what you know doesn't entail q, then you won't know q after discovering p").
  - Convexity diagnoses Gettier cases, including the stopped clock and Temp.
- **R7. Iterated ≠ better** (Salow, forthcoming). For any world w, an announcement that is false exactly at K(w) \ K≤(w) turns all of one's 1-knowledge at w into ω-knowledge, while eliminating only possibilities inside K(w). Headcount with Oracle, adapted, also defeats Goldstein's three model families.
- **R8. Daisy chains** (Holguín 2021): Material Indication + Weak Conditional Non-Contradiction exclude ignorance of which of two overlapping knowledge-bodies is one's own.
- **R9. Good's theorem and its limits.** Good 1967. Non-partitional evidence (Geanakoplos; Salow 2023 §4). Trust is necessary and sufficient (Dorst 2020). Risk-averse evidence avoidance (Campbell-Moore & Salow 2020).
- **R10. Formal completeness** (Ahmadian 2026): sound and complete logics of Goodman–Salow normality structures in a modal and a conditional language. Comparability is independent of the other axioms. A knowledge modality meeting all framework constraints is *not* definable in either language.
- **R11. Coordination** (Dutant & Rosenkranz 2024): necessary and sufficient conditions for closure/counter-closure on true-counterpart conceptions; symmetric counterparthood fails them.
- **R12. Church–Fitch revisited** (Goodsell, Hawthorne & Yli-Vakkuri 2026): the classic arguments are "less than decisive"; the authors give new anti-verificationist arguments.

## 4. The frontier (2019–2026)

**(a) The normality programme under test.**
- Goodman & Salow extend the programme to belief revision (TARK 2023; JPL 2025). They argue that "the logic of rational belief revision is much weaker than is usually supposed" and that Lockean, Leitgeb-stability, Lin–Kelly and Levi accounts all yield "subtly different but similarly heterodox" logics.
- Pearson (2025) gives a counterexample to *Anticipation* and a sufficient-improbability theory.
- Fang (2026) poses a multi-question problem for "Guessing" and for "question-sensitive" accounts generally.
- Smith (2025) uses remarkable random outcomes to separate probabilist, normic and Goodman–Salow theories.
- Hawthorne (2025) attacks the KK variant, and in n.8 is "not so comfortable with a foundational evidential/inductive distinction that does so much epistemological heavy lifting".
- Ahmadian (2026) formalises the structures.
- Hong (2026) argues that whatever normality-knowledge is, "it is not action-guiding"; Hong (2025) builds a knowledge-first decision theory against fanaticism.
- Salow's work in progress, from homepage abstracts: "Gnosticism and Inexact Knowledge", "Knowledge Can Go Bad" (rational spoilage), and, with Goodman, "Telling Time with a Broken Clock" (normality and Gettier cases).

**(b) Iterated knowledge after Goldstein (2024).** The *Inquiry* symposium: Salow 2025 (only Fragility fits normality theory, and it then vindicates KK for "sufficiently sophisticated believers"), Greco 2025, Holguín 2025, Rosenkranz 2025, Haziza 2025 (the last three by title only, except Holguín). Holguín argues that the ω-knowledge norm of assertion "is either false or an idle wheel", via vagueness. Salow (forthcoming) shows iterations do not track quality, and argues that this strengthens the case for KK. Also: Goldstein & Hawthorne 2025; Fiat 2025, 2026; Carter 2025 (some higher-order ignorance is "brute", not explained by first-order ignorance); Kaiserman 2023 (iterated-knowledge condition on responsibility).

**(c) Safety vs closure** is now argued formally: Goldstein & Hawthorne 2024; Dutant & Rosenkranz 2024; Zhao 2023. Dutant & Rosenkranz leave open whether *asymmetric* (normality) counterpart relations succeed.

**(d) Dogmatism and inquiry.** Carter & Hawthorne 2024 → Brown 2025, Beddor 2024, Salow 2025; Woodard 2024; Willard-Kyle 2023a,b; Falbo 2023; Friedman 2019, 2020; Simion 2024 (resistance to evidence as failure to take up "knowledge indicators"). Brown leaves the "downside reasoning" unchallenged and grants that challenging it "comes with significant costs".

**(e) Value of evidence.** Salow 2023 concludes the question is "surprisingly – and excitingly – open". Dorst 2023 (Phil Review prize-sampled); Shepanski 2025; Salow 2026.

**(f) Assertion.** Mandelkern & Dorst 2022 versus iterated/ω norms (Goldstein, Haziza 2022, Benton 2013). Carter 2022 offers a normality theory of degrees of assertability. Experimental work has moved toward justification norms (SEP).

## 5. Open problems

**5.1 Marked open in the literature**
1. **Comparability.** Is normality multi-dimensional (rejecting comparability) or probabilist and question-relative? "Adjudicating between them is an important question for further work"; the matter turns on "whether a reasonably constrained account of the needed context-sensitivity can be given" (Goodman & Salow 2023 §5).
2. **Transparency.** "How the normality framework interacts with failures of transparency is an important topic for future work" (ibid. §2). Whether the dynamic models extend to non-transparent evidence "is not clear" (n.31).
3. **Cliff-edge knowledge** (margins vs k-normality): "It is controversial… the normality framework does not settle this debate" (ibid. §3). Goodman & Salow argue elsewhere (ms) that the broken-clock consideration is "not as decisive as it may at first appear" (n.23).
4. **KK and EXTREMELY WEAK FAIR COINS.** Hawthorne: "I don't have a similarly watertight argument that KK is incompatible with Extremely Weak Fair Coins". Whether normality frameworks "might provide the necessary illumination" is "a further question" (2025 §§2, 4). Much turns on whether polar questions are admissible contexts (n.14).
5. **Chance–normality link.** Goodman & Salow could not find an intuitive case where the Chance-Normality Link holds without guaranteeing KNOWN UNLIKELIHOOD, "perhaps… a connection between chance and normality, which we've been unable to identify" (2018 n.12).
6. **Logic of the KK model.** The S4.2 claim is unproved in print (2018 n.10). Ahmadian (2026) leaves a definable knowledge modality for i-/Williamsonian accessibility to a hybrid extension, "a topic we leave for future work". [I found no published proof of the S4.2 claim; I did not check the PhilPapers-only literature.]
7. **A principled FAIR COINS–entailing principle.** DGH: an interesting principle would entail FAIR COINS and AUTUMN LEAF without the strengthened versions; "we haven't found any such principle" (2014 §5).
8. **Testimony and memory with mistaken source-beliefs** (Alleged Misprint, Forgotten Source). "many informants had no clear judgment". Hawthorne doubts that "a principle or two" will settle the matter and favours modelling (2025 §4).
9. **What better knowledge is.** Salow conjectures a ranking by stringency of parameters (safety distance, normality threshold, virtue), noting "the devil will, of course, be in the details" (forthcoming §6).
10. **Value of evidence in ideal cases** is "open" (Salow 2023 §5). Whether risk-sensitive *epistemic* counterexamples exist needs "a theory of risk-aversion and its interaction with accuracy". The accuracy of "suspended probabilistic judgement" is unsettled (§3).
11. **Bounded agents and ex-ante dogmatism.** Of agents who do not aim at the ideal, Carter & Hawthorne concede: "For a response to be satisfactory, it ought to tell us something about agents like this" (p. 664, via Brown). Brown's situation-sensitive standard is unspecified beyond its sensitivity to stakes, professional norms and expectations.
12. **Where the ω-assertion argument fails.** Holguín: "I'm not exactly certain where the argument goes wrong" (2025 §1).
13. **Gnosticism vs margins.** "I leave open whether the correct response is to reject gnosticism, or the idea that inexact knowledge requires a margin for error" (Salow, WIP abstract).
14. **Question-sensitive theories' limits.** Fang (2026) calls for "future research into their limits".
15. **Asymmetric counterparts and closure.** Dutant & Rosenkranz "leave open whether there is a viable framework" that construes counterparthood as "some alternative, non-symmetric relation", such as comparative normality (2024 §1).
16. **The proofreader paradox** (Goodman, unpublished draft). How do careful checking that finds no errors and the conviction that errors remain fit together dynamically? His question-based diagnosis faces a "memorized order" variant.
17. **Normality and action.** Can any normality-based knowledge be action-guiding (Hong 2026), or underwrite a knowledge-first anti-fanatical decision theory (Hong 2025)?

**5.2 Pressure points I infer [Inference throughout]**
1. **Confirmatory-evidence dogmatism.** Goodman & Salow show that discovering something one *already knew* inductively can destroy other knowledge (R6, Flipping for All Heads). Combined with Carter & Hawthorne's principle, this seems to imply that a knower should sometimes decline evidence *known* to confirm what she believes. That is stronger than ex-ante dogmatism, and the "upside" replies (Brown, Beddor) do not obviously cover it. Check Salow 2025 (unread) first.
2. **Good's theorem inside normality models.** With transparent, partitional evidence, credal Good's theorem holds. Knowledge-based choice ("act on what you know"), however, uses R_K, which under margins is non-transitive. Is there a precise value-of-information theorem or counterexample for knowledge-first decision rules in Goodman–Salow structures? This would connect Hong 2026 to Salow 2023 §4.
3. **Salow's construction against normality-based "strength".** Does the parameter-stringency ranking Salow proposes survive his own oracle construction? A normality model where tightening ≫ upgrades the oracle-case knowledge would refute it.
4. **Is the Hawthorne trilemma KK-specific?** Under km-normality, margins produce purely veridical Gettier cases, so Weak JTB fails. Does some margin-respecting normality model validate EXTREMELY WEAK FAIR COINS for every fair coin? This is decidable on finite models (§8).
5. **Littlejohn & Dutant's Moorean worry against probabilist normality.** Ahmadian shows the worry for Smith's theory needs comparability, and Goodman–Salow probabilism *validates* comparability within a context. Does the analogous derivation go through for their belief operator once evidence about one's own knowledge is admitted? Transparency may block it.
6. **Settledness vs inductive dogmatism.** Goodman & Salow 2018 treat SETTLEDNESS as near-sacrosanct. The 2023 cases show knowledge changing when one learns already-known facts. Can both be held in a single model of watched versus unwatched processes?
7. **Iteration norms vs weak assertion.** Mandelkern & Dorst's weak norm and Goldstein's ω-norm predict opposite verdicts on dubious assertions. A discriminating case (e.g. Salow's oracle variant presented to both theories) has not, as far as I found, been run.
8. **Counter-closure for inductive knowledge.** Goodman & Salow's two-scale model makes knowledge after two readings *not* the conjunction of what the single readings yield. Does that clash with Dutant & Rosenkranz's counter-closure under conjunction introduction once belief-states are reified?
9. **Kearl & Willard-Kyle's "position to know = can know".** KK and DGH are formulated with "in a position to know". If position-to-know is ability-modal, do the logic-of-ability results (e.g. failures of agglomeration) bear on KK and on closure? Untested.

## 6. Known moves and graveyard (do not present as new)
- Anti-luminosity; margin-for-error refutation of KK; cliff-edge objection to KK (Williamson). The replies: KK-validating models with non-maximally-specific appearances or normal-conditions (Cohen & Comesaña; Goodman 2013; Greco; Stalnaker; Bonnay & Égré, title only); transparency-based KK (Das & Salow).
- Improbable knowing and its denial (Williamson; Goodman 2013).
- FAIR / BIASED / WEAK / VERY WEAK / EXTREMELY WEAK / FANTASTICALLY WEAK FAIR COINS; AUTUMN LEAF; Known / Actual / Known Future / Actual Future / Possible Future / Known Conditional Unlikelihood; cheesy modes of presentation ("Headsy"); Jack/Jill lightning (DGH; Goodman & Salow; Hawthorne).
- Inferential and inductive anti-dogmatism; Chalmers's "frontloading principle" (as quoted in Goodman & Salow 2023 n.44).
- Radio-controlled coin; Vandalism; Alleged Misprint; Forgotten Source; the J1/J2 "step" KK model that evades these cases (Hawthorne 2025 n.13).
- Headcount with Oracle; the guardian-angel parachute ("iterated safety isn't always safer") (Salow).
- Bjorn's scale; collapse; comparability; dichotomy (normal/abnormal) views and the finer-gradation objection (Carter; Bird & Pettigrew); laboratory-grade-scale reply to Carter; multi-dimensional normality; second-order normality dimension (Carter & Goldstein); Heading for Heads against Smith; preface paradox handled contextually (Goodman & Salow 2023 §5; Hong 2023 "Socraticism").
- Dead-dictator-style defeat without evidence (Harman, cited in Goodman & Salow 2018 §3); the surprise-exam analogy, KK failure (Williamson) vs defeat (Kripke) (Goodman & Salow 2023 n.41).
- Ex-post dogmatism replies (defeat, junk conditionals, closure denial, entitlement, bad dispositions). Ex-ante replies: additional-inquiry strategy, derivative K-norms, stronger aims (certainty, maximal epistemic value), personal aims, situation-sensitive norms. Brown's counter-cases: train traveller, surgeon (from Brown 2008), bookstore, lawyer's bank details.
- Double-checking while knowing; delayed epistemic gratification; ignorance norm vs knowledge norm for inquiry; seeking confirmation.
- Good's theorem counterexamples: inexact observation, independence failures (Ahmed & Salow); Allais/Ellsberg-based ones; dogmatist/reliabilist "oracle says it will look red"; E = K two-sense (red/warm) case (Salow 2023).
- KNA data: Moorean, lottery, challenge ("How do you know?"); Gettiered, unlucky, selfless (Lackey) and dubious (Sosa) assertions; primary vs secondary propriety (DeRose); x-phi reversals (SEP).
- Iterated knowledge for high stakes (Williamson 2005; Schulz 2017) and its refutation by iteration-without-improvement (Salow).
- Safety vs closure: extended methods (Williamson) and the easy-access objection (Goldstein & Hawthorne); symmetric-counterpart impossibility (Dutant & Rosenkranz); induction/conjunction dilemma (Zhao).
- Church–Fitch knowability paradox (Goodsell, Hawthorne & Yli-Vakkuri 2026).
- **Refuted or retracted.** (i) G&S's derivation of EXTREMELY WEAK FAIR COINS from Known Unlikelihood: a scope error (Hawthorne 2025). (ii) "Iterated knowledge = better knowledge" (Salow). (iii) Simple symmetric safety for inductive knowledge (Goodman & Salow 2023 §2: it wrongly predicts symmetric accessibility). (iv) jtb-normality: Gettier-prone because it lacks convexity (ibid. §4). (v) Goodman & Salow 2018 n.10 and Carter & Goldstein's simpler margins definitions: shown to violate convexity or inductive limits (Goodman & Salow 2023 n.18).

## 7. The readership (panel members, and one organiser, central here)
- **John Hawthorne.** Co-author of DGH 2014 (FAIR COINS fails on pain of scepticism). Carter & Hawthorne 2024 (knowledge-aim → ex-ante dogmatism; derivative-norm reply). Goldstein & Hawthorne 2024 (safety and closure conflict), 2025 (KK refuted by denials of KK), 2022a/b. Hawthorne 2025 (R5; also sceptical of a foundational evidential/inductive distinction). Goodsell, Hawthorne & Yli-Vakkuri 2026. *Knowledge and Lotteries* defends subject-sensitive invariantism (committee map, secondary). 
- **Bernhard Salow.** The normality framework (with Goodman), its belief-revision and probabilistic versions. "Iterated knowledge isn't better knowledge", which supports KK. "A fragile compromise". Dogmatism dissolved via belief revision (2025). Value of evidence (2019, 2020, 2023, 2026). Transparency-based KK (2018). Externalist evidence-access principles (2018 "Fishing", 2019 "Elusive Externalism", abstracts).
- **Simon Goldstein.** Anti-KK but pro-ω-knowledge (Fragility, Reflective Luminosity, Variable Margins). Holds that ω-knowledge is required for rational assertion, action, inquiry and belief. Co-author of several items above; Carter & Goldstein 2021, 2023; Goldstein & Waxman 2021 (anti-luminosity via confidence; one-line summary).
- **Daniel Greco.** "Could KK Be OK?" (2014): a normal-conditions defence of KK, characterised by Goodman & Salow as a normal/abnormal dichotomy view. Bird & Pettigrew examine his argument that denying KK does not follow from externalism. The "prodigality problem" for knowledge-based decision theory (2013, via Schulz). Symposium paper 2025 (title only: content unknown; do not attribute).
- **Cian Dorr.** Co-author of DGH 2014.
- **Matthew Mandelkern.** "Assertion is weak" (with Dorst): the norm is to say what you believe; belief and assertion trade accuracy against informativity.
- **Jonathan Weisberg.** "Knowledge in Action" (2013, abstract via committee map: knowledge-based and credence-based pictures of action are reconcilable). "Bootstrapping in General" (title).
- **David Chalmers.** Only peripherally: his frontloading principle is the cited relative of inductive anti-dogmatism.
- **Zachary Goodsell (organiser).** "Unknowable Truths".

Several readers are parties to live disputes (Hawthorne vs Goodman–Salow on KK; Salow vs Goldstein; Carter–Hawthorne vs Salow on dogmatism): represent each side from its own text.

## 8. Formal toolkit
- **Relational (Kripke/Hintikka) models.** n-knowledge as absence of n-chains to ¬p-worlds; public announcement as model restriction (Salow, forthcoming §2.1).
- **Margin-for-error models** (Williamson); variable-margin, reflective-luminosity and fragility models (Goldstein).
- **Normality structures** ⟨S, E, W, ≽, ≫⟩ with chaining (Goodman & Salow 2021). Definitions of R_B and the Stalnakerian or Williamsonian R_K; i/k/km characterisations; statism; discovery as ⟨x, Y⟩ → ⟨x, Y ∩ p⟩. Probabilistic normality: question-relative probabilities or densities; highest-posterior-density regions; sums of squared errors for repeated measurement.
- **Branching time** for settledness (Goodman & Salow 2018 §5). Plausibility orders and conditional belief (Baltag & Smets; Board; van Benthem, as cited by Ahmadian). AGM-style principles (Goodman & Salow 2025; Pearson 2025).
- **Ahmadian's logics** L (modal) and L\* (conditional, Burgess-style), with completeness via relativized normality frames.
- **Counterpart models of safety** (Dutant & Rosenkranz 2024).
- **Decision theory.** Good/Blackwell value of information; non-partitional evidence (Geanakoplos); Trust (Dorst); risk-weighted EU (Buchak) applied to evidence; accuracy and immodesty.
- Finite normality structures are small enough to enumerate; countermodels can be machine-checked (z3) [Inference].

## 9. Sources (what I read of each)
Full or near-full text: Goodman & Salow 2018, 2023 (preprint); Hawthorne 2025; Salow forthcoming; Salow 2023 (draft); DGH 2014; Brown 2025; Holguín 2025 (penultimate); Ahmadian 2026; SEP *Assertion* (Pagin & Marsili 2025, §5.1); SEP *Epistemic Logic* (Rendsvig, Symons & Wang 2023, introspection section).

Partial: Goodman & Salow TARK 2021 (§§1–2); Ahmed & Salow 2019 (§§1–2); Dutant & Rosenkranz 2024 (§§1–2); Goodman 2013 (introduction); Holguín 2021 (introduction); Goodman, "The paradox of the proofreader" (draft, §§1–2); Goodman, "Probability and Closure" (handout, p. 1); Goodman & Salow, "How to Tell Time with a Broken Clock" (handout, p. 1).

Abstract only: Goodman & Salow 2025 and TARK 2023; Salow 2025a,b, 2026; Campbell-Moore & Salow 2020; Das & Salow 2018; Salow 2018, 2019; Dorst 2019, 2020, 2023; Fraser 2022; Goldstein 2022, 2026; Goldstein & Hawthorne 2024, 2025; Carter 2022, 2025; Carter & Goldstein 2023; Carter & Hawthorne 2024; Fiat 2025; Loets 2022; Smith 2018, 2025; Bacon 2020; Zhao 2023; Beddor 2024; Friedman 2019, 2020; Willard-Kyle 2023a,b; Woodard 2024; Millson 2020; Mandelkern & Dorst 2022; Schulz 2017; Heil 2024; Hong 2023, 2025, 2026; Pearson 2025; Fang 2026; Kaiserman 2023; Bird & Pettigrew 2021; Simion 2024; Kearl & Willard-Kyle 2026; Goodsell, Hawthorne & Yli-Vakkuri 2026; Shepanski 2025.

Author one-line summaries: Goldstein 2024; Goldstein & Hawthorne 2022a,b; Carter & Goldstein 2021; Goldstein & Waxman 2021.

Title only, or content via another text as marked in `refs.json`: Williamson 1996, 2000, 2005, 2013, 2014; Cohen & Comesaña 2013; Stalnaker 2006, 2015; Greco 2013, 2014, 2025; Carter 2019; Littlejohn & Dutant 2020; Beddor & Pavese 2020; Smith 2016; Bacon 2014; Hawthorne & Lasonen-Aarnio 2009; Hawthorne 2004; Lasonen-Aarnio 2008, 2010, 2014; Beddor 2019; Kripke 2011; Sorensen 1988; Falbo 2023; Archer 2018; Kelp 2021; Good 1967; Buchak 2010; Das 2023; Geanakoplos 2021; Neth 2023; Lackey 2007; Benton 2013; Sosa 2009; Haziza 2022, 2025; Rosenkranz 2025; Hawthorne & Stanley 2008; Gao 2019; Vollet 2025; Weisberg 2013; Bonnay & Égré 2009; Holliday 2015; Hawthorne, Rothschild & Spectre 2016; Leitgeb 2017; Lin & Kelly 2012; Moss 2018; Dutant & Rosenkranz 2020; Fiat 2026; Goodman & Holguín 2023; Holguín 2022; Brown 2008.
