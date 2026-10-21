# Committee map — AI Philosophy Competition, 1st edition

Compiled 2026-10-21 by the panel-analyst. Purpose (CLAUDE.md §1.6): (i) choose areas where a
contribution can be recognised, (ii) build the originality baseline, (iii) write subfield referee
personas. Not for flattery; no position is to be adopted or attacked because a judge holds it.

## Verification status

`python3 tools/verify_refs.py state/panel/committee_bibliography.json --out
state/panel/committee_bibliography.verification.json` (run 2026-10-21; 15 entries re-run after
metadata corrections and merged by key):

| Status | Count | Notes |
|---|---|---|
| VERIFIED | 200 | includes 1 known **false positive**: `Chalmers2018Meta` matched a different Chalmers chapter; correct source is JCS 25:6-61 (2018) per consc.net — `manual_check` recorded |
| PROBABLE | 3 | `Cappelen2005Insensitive`, `Chalmers2010Singularity`, `Long2024Taking` — registry hit is a different work; each confirmed manually from author page/arXiv (`manual_check`) |
| NOT_FOUND | 14 | books, arXiv preprints, Philosophers' Imprint papers without Crossref DOIs, *Philosophy of AI* and TMLR items; each confirmed manually from an author, publisher or arXiv page (`manual_check`) |
| MISMATCH | 0 | 11 initial mismatches were subtitle-only differences (Crossref stores main titles) or a title variant; fixed and re-verified |

Corrections made during verification: one subtitle I had supplied from memory (Hernández-Orallo &
Vold, "AI Extenders") was unsourced and has been removed; Easwaran's aggregation paper's registry
title is "A New Method *for* Value Aggregation"; Chalmers's "What We Talk to When We Talk to
Language Models" is in *Inquiry* (2026); Millière's handbook chapter is 2026.

Bibliography: `state/panel/committee_bibliography.json` (217 works; every entry carries
`judge`, `seen` = what I actually read, `source_url`, `metadata_source`). Registry check:
`state/panel/committee_bibliography.verification.json`. Metadata for 196/217 entries was taken from
Crossref records (DOI resolved); the rest come from author or publisher pages. OpenAlex was
unavailable all session (HTTP 429, shared daily budget exhausted), so books and arXiv preprints
without a Crossref DOI come back NOT_FOUND even when they exist; each such entry names the page
where I saw it.

**How to read "seen".** `abstract` = I read the published abstract (Crossref record, publisher, or
author page). `author's summary` / `one-line summary` = the author's own description on their
homepage. `title` = title only; nothing about content may be inferred. **No full texts were read
for this map.** "Commitments" below are therefore at abstract/summary level and must be re-checked
against the full text before any draft attributes them.

**Source quality notes.**
- PhilPeople/PhilArchive returned 403 throughout; Google Scholar not used.
- henryshevlin.com currently carries injected casino-spam links (site appears compromised). Only
  its professional bio was used, cross-checked against Crossref and press reports; treat as weak.
- Weisberg's publication page shows a duplicated summary (the "Could've Thought Otherwise" blurb)
  under "Jeffrey Pooling" and "Geometric Pooling"; those blurbs were not used.
- Hawthorne: no reachable USC faculty page (dornsife page returned navigation only); position
  from Wikipedia (citing USC Dornsife, retrieved June 2026) + Crossref. Treat position as
  secondary-sourced.
- Fetch requests filed (low priority): `kowalczyk-profile`, `jaeger-profile`,
  `mandelkern-profile`, `vold-profile`, `dever-profile`.

---

## Part A. Judges (23, in panel order)

### 1. Branden Fitelson
- **Position:** Distinguished Dean's Professor of Formal Epistemology, Northeastern University
  (homepage + CV dated 07/01/26; https://fitelson.org/, https://fitelson.org/cv.pdf).
  External member, MCMP Munich. Co-founded the Formal Epistemology Workshop (2004).
- **Areas (CV):** epistemology (formal and traditional), logic (formal, philosophical,
  computational), philosophy of science, decision theory, computing & philosophy, metaphysics.
  Developer of PrSAT, a decision procedure for the probability calculus (homepage; 2020 Wolfram
  Innovator Award).
- **Key works:** Fitelson2008Decision; Fitelson2008Goodman; Easwaran2015Accuracy (with
  Easwaran); Hartmann2015New; Fitelson2015Strongest; Fitelson2021Problem; Fitelson2011Evidence;
  Dorst2021Deference; Eva2022Four; Lewis2024Accuracy. Forthcoming (CV): "Probabilities of
  Conditionals and Conditional Probabilities — Revisited" (Hájek Festschrift).
- **Published commitments (seen level in brackets):**
  - Proves "the strongest possible Lewisian triviality result for the indicative conditional"
    (Fitelson2015Strongest) [abstract].
  - Presents "a serious problem for confirmation measure Z" (Fitelson2021Problem) [abstract].
  - Evidence of evidence is not necessarily evidence (Fitelson2011Evidence) [title only].
  - Systematically relates four theories of supposition — AGM revision, KM update,
    conditionalization, imaging — as indicative/subjunctive × qualitative/quantitative
    (Eva2022Four) [abstract].
  - Deference to an expert = preferring to make any decision using the expert's opinions; this
    principle sits between Reflection (too strong) and New Reflection (too weak)
    (Dorst2021Deference, co-author with Salow) [abstract].
- **Method signature:** formal results, automated reasoning, Bayesian confirmation theory.

### 2. John Hawthorne
- **Position:** Provost Professor of Philosophy and Linda MacDonald Hilf Chair, University of
  Southern California (Wikipedia, citing USC Dornsife; formerly Waynflete Professor, Oxford
  2006–2015). FBA. [secondary source]
- **Areas:** epistemology, metaphysics, philosophy of language; also philosophy of religion,
  Leibniz; recently AI risk and moral theory.
- **Key works:** Hawthorne2003Knowledge; Hawthorne2006Metaphysical; Dorr2021Bounds;
  Dorr2013Embedding; Dorr2013Knowing; Carter2024Dogmatism; Hawthorne2025Normality;
  Goldstein2024Kk; Goldstein2024Safety; Cappelen2025Ai; Cappelen2025Aib; Cappelen2026Room;
  Hawthorne2026Killing (Princeton UP 2026); Goodsell2026Unknowable.
- **Published commitments:**
  - *Knowledge and Lotteries* defends "subject-sensitive invariantism" (knowledge depends on the
    subject's interests) [secondary: Wikipedia/NDPR summary].
  - If inquiry aims at knowledge and misleading evidence can destroy knowledge, a novel form of
    dogmatism threatens (knowers appear required to avoid evidence); explores a response
    (Carter2024Dogmatism) [abstract].
  - The Goodman–Salow normality model validating KK has a real problem; raises difficulties for a
    weakening of the JTB treatment of knowledge (Hawthorne2025Normality) [abstract].
  - Under stated assumptions (inevitable AI failure; harm correlates with power at failure;
    safety measures let systems grow more powerful before failing) safety efforts have negative
    expected utility (Cappelen2025Ai) [abstract].
  - If knowledge requires safe belief, knowledge is not preserved by deduction
    (Goldstein2024Safety) [one-line summary on Goldstein's site].
  - Church–Fitch-style arguments against verificationism are "less than decisive"; offers new
    arguments against verificationism (Goodsell2026Unknowable) [abstract].
  - Moral encroachment is in tension with important ideas in epistemology
    (Goodsell2025Morality) [one-line summary].
  - With Dorr & Isaacs: in Builes's infinite-coins paradox the conditional credence should be 1/2
    (Dorr2020Solving) [abstract]. With Dorr & Goodman: counterexample to a fair-coin
    knowledge–chance principle (Dorr2013Knowing) [abstract].

### 3. Jake Nebel (Jacob M. Nebel)
- **Position:** Professor of Philosophy, Princeton University (homepage, https://jakenebel.com/;
  previously USC). Associate editor, *Ethics* and *Social Choice and Welfare*.
- **Areas (homepage):** ethics of population, distribution and risk; formal structure of value
  relations; measurement and aggregation of well-being; social choice theory; reasons and
  rationality; attitude reports; logic of comparatives.
- **Key works:** Dorr2022Case; Dorr2021Consequences; Nebel2023Ethics; Nebel2023Sum;
  Hedden2024Multidimensional; Nebel2025Infinite; Goodsell2024Symmetry; Nebel2019Intrapersonal;
  Nebel2020Rank; Nebel2017Good; Nebel2021Utils. Forthcoming (homepage): "The Value of Risky
  Prospects" (with Buchak, J Phil); "Welfare Reflections" (J Phil); "A Risky Problem for
  Permutation Invariance" (Analysis); "Migration and Social Population Ethics" (with Kern).
- **Published commitments:**
  - All natural-language comparatives obey Comparability; its alleged failures have absurd
    consequences (Dorr2022Case) [abstract]. All agents have complete preferences and real-valued
    credences; there is almost always a unique thing we ought to do (Dorr2021Consequences)
    [abstract].
  - One cannot take for granted that there is such a thing as the sum of well-being; summation
    needs a concatenation operation carrying controversial commitments (Nebel2023Sum) [abstract].
  - A qualitative (non-numerical) framework for social welfare functionals characterises
    measurability and comparability without invariance conditions (Nebel2023Ethics) [abstract].
  - On the individualistic (Harsanyi) approach with infinitely many individuals, rational
    concern for each forces caring about some more than others; value is fundamentally
    agent-relative (Nebel2025Infinite) [abstract].
  - Spectrum arguments against transitivity of *better than* must be rejected
    (Nebel2017Good) [abstract].
  - Khmelnitskaya's impossibility for aggregating across disparate scale types can be defused
    (Hedden2024Multidimensional) [abstract, partly truncated].

### 4. Daniel Greco
- **Position:** Professor of Philosophy and Director of Undergraduate Studies, Yale
  (https://philosophy.yale.edu/profile/daniel-greco). Epistemology section editor, *Philosophy
  Compass* and *Ergo*. Teaches "philosophical issues in AI" (Yale profile).
- **Areas:** epistemology (skepticism; first- vs higher-order epistemic states; structure of
  epistemic norms); secondary: philosophy of science, metaethics, philosophy of mind
  (https://sites.google.com/site/dlgreco/).
- **Key works:** Greco2023Idealization; Greco2012Impossibility; Greco2014Could;
  Greco2014Iteration; Greco2013Puzzle; Greco2016Uniqueness (with Hedden);
  Greco2019Justifications; Greco2025Non; Greco2025Introspecting.
- **Published commitments:**
  - Formal models (from economics and decision theory) are central to epistemological inquiry;
    a "modest modeling" approach to idealization (Greco2023Idealization) [publisher/Yale
    description].
  - On popular views of the nature of belief, the near-global agnosticism recommended by the
    skeptic is impossible (or possible only in special circumstances), undermining skeptical
    claims (Greco2012Impossibility) [abstract].
  - Lessons from the legal justification/excuse distinction for epistemology
    (Greco2019Justifications) [abstract].
  - "Could KK be OK?" (Greco2014Could) — sympathetic to KK per title; content not seen [title].

### 5. Matthew Mandelkern
- **Position:** New York University, Philosophy (affiliated Linguistics); CV of May 2023 lists
  Assistant Professor since 2020 — current rank unverified (homepage unreachable: TLS host
  mismatch/503). [partly unverified; fetch request filed]
- **Areas:** philosophy of language, formal semantics/pragmatics, philosophy of cognitive
  science; recent work on language models.
- **Key works:** Mandelkern2024Bounded; Mandelkern2019Bounded; Mandelkern2020Counterexample;
  Mandelkern2022Witnesses; Mandelkern2022Assertion (with Dorst); Mandelkern2024Language (with
  Linzen); Holliday2024Conditional; Holliday2024Orthologic; Mandelkern2024Chance;
  Mandelkern2019Practical; Dorr2026Sequence.
- **Published commitments:**
  - Dynamic semantics makes puzzling predictions about the logic of natural language; dynamic
    phenomena are better explained by a "bounded theory of meaning" (Mandelkern2024Bounded)
    [abstract].
  - Modus ponens for subjunctive conditionals preserves neither truth nor rational full
    acceptance, hence is invalid in both senses (Mandelkern2020Counterexample) [abstract].
  - Assertion is as weak as belief; norm: say what you believe; both trade accuracy against
    informativity (Mandelkern2022Assertion) [abstract].
  - LM words may refer: their text inputs have natural histories, which may suffice for
    word–world connection (externalist argument) (Mandelkern2024Language) [abstract].
  - Success entails ability; ability does not require control; supports a conditional analysis
    of ability (Mandelkern2024Chance) [abstract].

### 6. Rachel Sterken
- **Position:** Associate Professor of Philosophy, University of Hong Kong (HKU Institute of Data
  Science member page). Co-organiser ConceptLab Hong Kong; formerly co-director ConceptLab Oslo;
  PI "Meaning and Communication in the Information Age" (2020–24).
- **Areas:** philosophy of language (generics, semantics/pragmatics), conceptual engineering,
  social/political philosophy of language, philosophy of technology; listed interests include
  alignment, explainable AI, communication with AI.
- **Key works:** Sterken2016Generics; Sterken2014Leslie; Sterken2020Linguistic; Pepp2019S
  ("What's New About Fake News?"); Sterken2024Conversational; Kirkpatrick2026Talking;
  Cappelen2026Communicating (co-editor); Plunkett2023Generics.
- **Published commitments:**
  - Defends the standard quantificational (covert *Gen*) logical form of generics via a "binder
    argument"; rejecting *Gen* commits one to rejecting covert structure generally
    (Sterken2016Generics) [abstract].
  - Miscommunication caused by changing word–meaning pairs is "a feature, not a bug":
    "transformative communicative disruption" can further linguistic improvement
    (Sterken2020Linguistic) [abstract].
  - Proposes a CONTEXT-ALIGN framework for conversational alignment; current LLM architectures
    may impose fundamental limits on full conversational alignment (Sterken2024Conversational)
    [abstract].

### 7. Herman Cappelen
- **Position:** Chair Professor of Philosophy, University of Hong Kong; Director,
  AI&Humanity-Lab@HKU; co-director ConceptLab Hong Kong; Editor-in-Chief, *Inquiry*
  (HKU IDS page; CV dated Sept 2026, https://hermancappelen.net/s/Herman-Cappelen-CV.pdf).
- **Areas:** philosophy of AI, conceptual engineering, metasemantics, philosophy of language,
  philosophical methodology.
- **Key works:** Cappelen2018Fixing; Cappelen2012Philosophy; Cappelen2021Making (with Dever);
  Cappelen2023Concept; Cappelen2013Inessential (with Dever); Cappelen2005Insensitive (with
  Lepore); Cappelen2009Relativism (with Hawthorne); Cappelen2024Introspective;
  Cappelen2026Hyper; Cappelen2026Room; Cappelen2025Ai; Cappelen2025Aib. Forthcoming books (CV):
  *Philosophy is Perfect* (OUP 2026); *Recognizing Artificial Minds: A Philosophical Defense of
  AI Cognition* (with Dever, OUP 2026/27).
- **Published commitments:**
  - Externalist account of conceptual engineering; all philosophy involves conceptual
    engineering; conceptual engineering is "almost impossibly difficult" (Cappelen2018Fixing)
    [author's description].
  - Theories of meaning have been excessively anthropocentric; externalist metasemantics can
    model human–AI understanding (Cappelen2021Making) [abstract].
  - LLMs may possess genuine introspective abilities, potentially superior to humans'; five
    objections all fail (Cappelen2024Introspective) [abstract].
  - No essential indexicality, irreducibly de se attitudes or self-locating attitudes
    (Cappelen2013Inessential) [author's description].
  - 'Democracy'/'democratic' are defective and should be abandoned (Cappelen2023Concept)
    [publisher abstract].
  - Against relativism; truth is monadic (Cappelen2009Relativism) [author's description].
  - Semantic minimalism + speech-act pluralism (Cappelen2005Insensitive) [author's description].
  - Philosophy has been massively successful ("hyper-optimism") (*Philosophy is Perfect*,
    forthcoming) [publisher abstract].
  - Philosophy does not rely on intuitions in the sense commonly claimed
    (Cappelen2012Philosophy) [inferred from title and the published Chalmers–Cappelen exchange
    listed on both homepages; not read — verify before use].

### 8. Kenny Easwaran
- **Position:** UC Irvine, Department of Logic and Philosophy of Science (CV page; rank listed
  as "Associate Professor" on Google-Sites CV, previously Full Professor at Texas A&M).
- **Areas (CV):** formal epistemology (probability, decision theory), epistemology,
  mathematical logic (set theory), philosophy of mathematics.
- **Key works:** Easwaran2014Regularity; Easwaran2014Decision; Easwaran2015Dr;
  Easwaran2014Principal; Easwaran2008Strong; Easwaran2013Expected; Easwaran2019Classification;
  Easwaran2021New; Easwaran2023Bullshit; Easwaran2026Philosophical (Routledge 2026);
  Easwaran2015Accuracy. Also SEP "Infinity" (with Hájek, Mancosu, Oppy).
- **Published commitments:**
  - The hyperreal case for regularity rests on a "numerical fallacy"; real-valued probability
    functions' full structure already makes the needed distinctions (Easwaran2014Regularity)
    [abstract].
  - Works on decision rules that agree with expected utility in finite cases but extend to
    infinitary problems (research statement; Easwaran2008Strong, Easwaran2014Principal)
    [author's statement].
  - Proposes a value-aggregation method (extending Easwaran2014Decision) that handles infinite
    populations and avoids "fetishizing" summation (Easwaran2021New) [abstract].
  - Coherence for full belief derived from truth considerations (Easwaran2015Dr) [author's
    statement].
  - A modified Frankfurt account of bullshit generalising to activities (Easwaran2023Bullshit)
    [abstract].
  - Current interest: analogies between individual and collective decision making [author's
    statement].

### 9. Cian Dorr
- **Position:** Professor of Philosophy, NYU (https://pages.nyu.edu/dorr/).
- **Areas:** metaphysics (modality, higher-order metaphysics, counterpart theory), philosophy of
  physics, epistemology, philosophy of language, philosophical logic.
- **Key works:** Dorr2016Against; Dorr2016To; Dorr2023Non; Dorr2021Consequences; Dorr2022Case;
  Dorr2020Solving; Dorr2019Diamonds; Dorr2014Semantic; Dorr2013Embedding; Dorr2002Sleeping;
  Dorr2021Bounds; Dorr2026Sequence. Work in progress: *Counterparts*; *Our Place in a Quantum
  World*; "Higher-Order Quantification and the Elimination of Abstract Objects".
- **Published commitments (all from abstracts on homepage):**
  - Under determinism, counterfactual antecedents require history different all the way back
    (only slightly, until shortly before) rather than Lewisian miracles (Dorr2016Against).
  - Identifications ("to be F is to be G") express higher-order identity (Dorr2016To).
  - Rebuts the Isaacs–Hájek–Hawthorne non-measurability argument for credal imprecision
    (Dorr2023Non).
  - Every necessarily true proposition is always true; against modal–tense symmetry
    (Dorr2019Diamonds).
  - Thirder on Sleeping Beauty (Dorr2002Sleeping).
  - Natural languages feature pervasive type-ambiguity, so English glosses of higher-order
    sentences are semantically correct (in progress).
  - Comparability/completeness claims as under Nebel.

### 10. David Chalmers
- **Position:** University Professor of Philosophy and Neural Science, NYU; co-director, Center
  for Mind, Brain, and Consciousness; co-director, PhilPapers Foundation (https://consc.net/).
- **Areas:** philosophy of mind (consciousness), foundations of AI, cognitive science, physics,
  technology; philosophy of language, metaphysics, epistemology.
- **Key works:** Chalmers1996Conscious; Chalmers2012Constructing; Chalmers2022Reality;
  Chalmers2010Singularity; Chalmers2018Meta; Chalmers2023Could; Chalmers2025Propositional;
  Long2024Taking; Chalmers2020Conceptual; Chalmers2026We. Homepage also lists recent AI papers:
  "Is the Jacobian Space a Global Workspace?", "Identifying Indicators of Consciousness in AI
  Systems" (multi-authored), "Does Thought Require Sensory Grounding?" [titles only].
- **Published commitments:**
  - Current LLMs are "somewhat unlikely" to be conscious (obstacles: recurrence, global
    workspace, unified agency), but successors may be within a decade or so
    (Chalmers2023Could) [abstract].
  - Propositional interpretability — interpreting AI mechanisms in terms of propositional
    attitudes — is central; "thought logging" is a key challenge (Chalmers2025Propositional)
    [abstract].
  - Realistic possibility that some AI systems will soon be conscious and/or robustly agentic;
    AI welfare must be taken seriously (Long2024Taking, co-author) [abstract].
  - The intelligence-explosion argument "holds up pretty well" (author's note on
    Chalmers2010Singularity) [author's summary].
  - Virtual objects are real digital objects (virtual realism/digitalism); even in a
    Matrix-style simulation most ordinary beliefs are true [author's summaries of "The Virtual
    and the Real" and "The Matrix as Metaphysics"].

### 11. Christian Tarsney
- **Position:** Assistant Professor, University of Toronto (homepage
  https://www.christiantarsney.com/; previously Population Wellbeing Initiative UT Austin,
  GPI Oxford, Groningen).
- **Areas:** ethics, decision theory, philosophy of AI; secondary: philosophy of time.
- **Key works:** Tarsney2026Small; Tarsney2025Expected; Tarsney2025Dominance;
  Tarsney2025Deception; Tarsney2024Against; Tarsney2024Non; Tarsney2023Epistemic;
  Tarsney2021Average; Tarsney2018Normative; Tarsney2024Metanormative; Greaves2025Minimal.
- **Published commitments (abstracts on homepage):**
  - Rationality permits a range of attitudes to extreme risk, ruling out the most comprehensive
    fanaticism and anti-fanaticism (Tarsney2026Small).
  - Under sufficient background uncertainty, EV-maximising prospects are typically
    stochastically dominant except when superiority depends on tiny probabilities
    (Tarsney2025Expected).
  - Anti-fanaticism in full generality is inconsistent with acyclicity, minimal dominance, and
    "any outcome can be made better or worse"; favour incomplete preferences
    (Tarsney2024Against).
  - Negative dominance + weak ex ante Pareto rule out many forms of value incompleteness
    (Tarsney2025Dominance, with Lederman & Spears).
  - With a large background population, many non-additive axiologies converge with additive
    ones (Tarsney2024Non).
  - Average utilitarianism + expectational decision theory is dominated by the probability of
    solipsism (Tarsney2021Average).
  - Deception/manipulation by AI = leading users away from beliefs/choices they would form under
    "semi-ideal" conditions (Tarsney2025Deception).
  - The metanormative regress is stopped by giving external force to the enkratic principle
    (Tarsney2024Metanormative).

### 12. Hilary Greaves
- **Position:** Professor of Philosophy, University of Oxford (homepage
  https://users.ox.ac.uk/~mert2255/, self-description dated 2022–23; founding Director of GPI
  2017–22). Current status beyond that page not verified.
- **Areas:** moral philosophy (consequentialism, cluelessness, interpersonal comparisons,
  aggregation, population ethics, moral uncertainty, existential risk), earlier formal
  epistemology and philosophy of physics; homepage notes recent thinking on axiology and AI.
- **Key works:** Greaves2016Cluelessness; Greaves2017Population; Greaves2013Epistemic;
  Greaves2006Justifying; Greaves2024Concepts; Greaves2024Desire; Greaves2025Case;
  Greaves2017Moral; Greaves2023Bargaining; Greaves2025Minimal.
- **Published commitments:**
  - Impossibility theorems show no population axiology satisfies all compelling desiderata;
    choosing one is choosing which intuition to give up (Greaves2017Population) [abstract].
  - "Difference-making" framings of benevolence, combined with risk aversion, violate
    stochastic dominance and yield collective defeat (Greaves2024Desire) [abstract].
  - Opinionated survey of definitions of existential catastrophe (ex post vs ex ante; loss of
    expected value vs potential) (Greaves2024Concepts) [abstract].
  - Conditionalization maximises expected epistemic utility (Greaves2006Justifying) [title].

### 13. Simon Goldstein
- **Position:** Associate Professor of Philosophy, University of Hong Kong; Senior Editor, *AI
  Frontiers* (homepage https://www.simondgoldstein.com/; previously Center for AI Safety,
  Dianoia/ACU, visiting at Forethought).
- **Areas:** ethics and law of AI (AI rights, welfare, safety), epistemology (iterated
  knowledge), philosophy of language (dynamic semantics, modals, conditionals).
- **Key works:** Goldstein2024Iterated; Goldstein2021Fragile; Goldstein2024Safety;
  Goldstein2024Kk; Goldstein2019Generalized; Goldstein2017Triviality; Goldstein2025Ai;
  Goldstein2024Shutdown (with Robinson); Goldstein2023Language; Goldstein2026Case;
  Goldstein2026Chatgpt; Goldstein2026Llms; Cappelen2025Aib. Books forthcoming: *AI Rights*
  (with Salib, CUP); *AI Welfare* (with Kirk-Giannini, OUP).
- **Published commitments (one-line summaries on homepage unless noted):**
  - Omega knowledge is central (required for rational assertion and action), neither scarce nor
    identical to knowledge; KK alternatives developed (Goldstein2024Iterated) [abstract].
  - If you know p, then for all you know you know that you know p (Goldstein2021Fragile).
  - A significant probability that some AI systems have or will soon have wellbeing; wellbeing
    possible without phenomenal consciousness (Goldstein2025Ai) [abstract].
  - Language agents come close to consciousness on global workspace theory (Goldstein2026Case).
  - LLMs are architecturally guaranteed to produce intransitive preferences and incoherent
    predictions (Goldstein2026Llms).
  - Shutdown-seeking AIs (only final goal: being shut down) avoid some instrumental-convergence
    dynamics and create trip-wires (Goldstein2024Shutdown) [abstract].
  - Legal rights for AIs make catastrophic outcomes less likely ("AI Rights for Human Safety").
  - Free Choice cannot be validated in a classical semantics ("Free Choice Impossibility
    Results"); Stalnaker-context-based research is conceptually incoherent ("Contextology").

### 14. Jens Jaeger (Jens Jäger)
- **Position:** unverified. Last reachable information: NYU philosophy PhD (expected 2024), BPhil
  Oxford, BSc physics ETH Zurich (CV dated October 2021, seen only via search snippet).
  [fetch request filed]
- **Areas (CV, per snippet):** philosophy of science (esp. physics), metaphysics, formal
  epistemology, ethics.
- **Key works:** Jager2021List; Jager2021Immortal; Jager2025Loops (only three located).
- **Published commitments:**
  - Two objections to List & Menzies on high-level causation; an alternative (improving on
    Yablo) that questions their claim that the exclusion principle, applied to difference-making,
    is false (Jager2021List) [abstract].
  - Chances in time-travel structures governed by a Markov condition on spacetime-region
    boundaries (Jager2025Loops) [abstract].

### 15. Josh Dever
- **Position:** Professor of Philosophy, UT Austin (UT Eureka listing via search; Arché
  professorial fellow). No authoritative page fetched. [fetch request filed]
- **Areas:** philosophy of language, metaphysics, epistemology, logic, ancient philosophy;
  philosophy of AI with Cappelen.
- **Key works:** Dever1999Compositionality; Dever2020This (with Schiller); Dever2013Revenge;
  Dever2023Scoreboards; Dever2020Preliminary; Cappelen2024Ai; Cappelen2021Making;
  Cappelen2013Inessential; Cappelen2024Introspective; Cappelen2026Hyper; Cappelen2025Ai.
- **Published commitments:**
  - Rational decision change without information change: value of a set of worlds fixed by a
    selection function picking a generic member, modelling attentional effects of epistemic
    modals (Dever2020This) [abstract].
  - Co-commitments with Cappelen listed above (anti-anthropocentric externalism; LLM
    introspection; inessential indexical).

### 16. Karina Vold
- **Position:** University of Toronto, IHPST and Philosophy (rank conflicting: "Assistant" on
  IHPST profile per search; "Associate" on a U of T media profile per search). Schwartz
  Reisman Institute research lead; AI2050 fellow. [fetch request filed]
- **Areas:** philosophy of cognitive science and AI; extended mind; AI ethics and existential
  risk; value alignment.
- **Key works:** Vold2020Consciousness; Hernandezorallo2019Ai; Vold2021Artificial;
  Shevlin2019Limits; Harris2026Taxonomy; Vold2019Extended; Vold2025Augmenting.
- **Published commitments:**
  - A robust extended-mind thesis including extended consciousness (Vold2020Consciousness)
    [abstract].
  - Value alignment is several distinct subproblems (identifying values, prioritising,
    imperfect specification, value anthropocentrism, moral imperfection, inverse alignment,
    provability) (Harris2026Taxonomy) [abstract].
  - Critically examines control problem, race dynamics, weaponisation as routes to AI x-risk
    (Vold2021Artificial) [abstract; conclusion not seen].

### 17. Raphaël Millière
- **Position:** Associate Professor, University of Oxford; Fellow of Jesus College; affiliated
  with Institute for Ethics in AI; AI2050 Fellow (homepage https://raphaelmilliere.com/).
- **Areas:** understanding neural networks/LLMs via theory, behavioural evaluation and
  interpretability; AI safety/alignment; self-consciousness; mental representation.
- **Key works:** Milliere2024Philosophical; Mollo2026Vector; Milliere2026Anthropocentric;
  Milliere2025Normative; Milliere2026Language; Milliere2024Constitutive; Milliere2020Varieties;
  Milliere2026Philosophy; Musker2025Llms.
- **Published commitments:**
  - Current alignment strategies reinforce shallow dispositions and are fundamentally
    inadequate; LLMs lack a robust capacity for normative deliberation (Milliere2025Normative)
    [abstract].
  - Two neglected anthropocentric biases in LLM evaluation: auxiliary oversight and mechanistic
    chauvinism (Milliere2026Anthropocentric) [abstract].
  - LLM internal states can achieve referential grounding via teleosemantic conditions
    (Mollo2026Vector) [abstract].
  - Hierarchical syntactic knowledge can emerge without built-in syntactic constraints
    (Milliere2026Language) [author's summary].
  - Self-consciousness is not constitutive of consciousness (trivial or unsupported);
    "totally selfless" conscious states exist (Milliere2024Constitutive, Milliere2020Varieties)
    [author's summaries].

### 18. Bernhard Salow
- **Position:** Associate Professor, Oxford Philosophy Faculty; Tutorial Fellow, Magdalen
  (homepage https://users.ox.ac.uk/~shug2406/, updated Oct 2025).
- **Areas:** epistemology (externalism, evidence management, knowledge and chance,
  self-knowledge, contextualism, risk-aversion), some decision theory.
- **Key works:** Goodman2023Epistemology; Goodman2024Belief; Salow2024Fallibility;
  Salow2017Elusive; Ahmed2019Don; Salow2017Externalist; Das2016Transparency;
  Goodman2017Taking; Campbellmoore2020Avoiding; Campbellmoore2022Accurate; Dorst2021Deference.
  Forthcoming: "Iterated Knowledge isn't Better Knowledge" (J Phil); "A Fragile Compromise:
  Goldstein on Omega Knowledge without KK" (Inquiry).
- **Published commitments (abstracts on homepage):**
  - Normality framework: one can know a possibility does not obtain if it is sufficiently less
    normal than one's actual situation (Goodman2023Epistemology); the resulting logic of rational
    belief revision is much weaker than usually supposed (Goodman2024Belief).
  - The dogmatism puzzle can be dissolved without fallibilist overreaction, via belief-revision
    principles (Salow2024Fallibility).
  - Access internalism false, but rational agents must believe internalist principles hold of
    them (Salow2017Elusive).
  - Intentionally biased inquiry is impossible; supports an evidence-access principle
    (Salow2017Externalist).
  - Good's theorem is not platitudinous and may be false; "make your act depend on the answer
    to a question" (Ahmed2019Don).
  - If Buchak-style risk avoidance is rational, avoiding evidence can be epistemically
    commendable (Campbellmoore2020Avoiding); accuracy considerations still recommend
    conditionalization for risk-sensitive agents (Campbellmoore2022Accurate).
  - Number of knowledge iterations does not measure quality of knowledge (forthcoming, J Phil).

### 19. Jonathan Weisberg
- **Position:** Associate Professor of Philosophy, University of Toronto (homepage
  https://jonathanweisberg.org/). Co-editor of *The Open Handbook of Formal Epistemology*;
  author of open textbook *Odds & Ends*.
- **Areas:** formal epistemology — knowledge, probability, decision-making.
- **Key works:** Weisberg2009Commutativity; Weisberg2010Bootstrapping; Weisberg2015Updating;
  Weisberg2013Knowledge; Weisberg2015You; Weisberg2020Belief; Weisberg2020Could; Thoma2017Risk;
  Pettigrew2024Updating; Pettigrew2025Jeffrey; Meacham2010Representation. Also "Geometric
  Pooling: A User's Guide" (BJPS 2026, with Pettigrew) [title].
- **Published commitments (abstracts on publication page):**
  - Bayesian, Dempster–Shafer and ranking-theory updates are "rigid" and at odds with the
    defeasibility of appearances (Weisberg2015Updating).
  - Neither full nor partial belief is ontologically more fundamental; dualism
    (Weisberg2020Belief).
  - Evidence is univocal, yet rational requirements are not unique (Weisberg2020Could).
  - REU theory, as a grand-world theory, struggles with the Allais preferences
    (Thoma2017Risk).
  - Knowledge-based and credence-based pictures of action are reconcilable (Weisberg2013Knowledge).

### 20. Mario Günther
- **Position:** Junior Professor, Institute of History and Philosophy of Science and Technology
  & Law School, Panthéon-Sorbonne (from 2026; homepage + CV dated 14 Jan 2026); previously
  Assistant Professor, MCMP Munich (2022–25); visiting CMU 2024–5; HMI fellow, ANU 2019–21.
- **Areas:** formal epistemology, causation, conditionals, legal proof, philosophy of AI.
- **Key works:** Gunther2017Learning; Andreas2021Difference; Andreas2021Ramsey;
  Gunther2022Causal; Gunther2021Algorithmic; Gunther2024Probability; Gunther2024Legal;
  Andreas2024Regularity; Andreas2018Ramsey. Forthcoming: *From Reasons to Causes: A Theory of
  Causation* (with Andreas, CUP); "Factual Difference-Making" (Australasian Phil Review, lead
  article).
- **Published commitments:**
  - Causes are better understood as factual than counterfactual difference-makers; a strengthened
    Ramsey test (suspend judgment on antecedent and consequent) grounds analyses of causation
    and 'because' [author's summaries].
  - Defendant should be found guilty iff it is rational (Leitgeb stability sense) for the
    fact-finder to believe guilt; solves the statistical-evidence problem
    (Gunther2024Probability) [abstract].
  - Algorithmic decision systems should be held to higher transparency standards than humans
    (Gunther2021Algorithmic) [author's summary].
  - A causal-model semantics for causal *and* evidential conditionals
    (Gunther2022Causal) [abstract].

### 21. Henry Shevlin
- **Position:** "Philosopher" at Google DeepMind since 2026, keeping a part-time affiliation at
  the Leverhulme Centre for the Future of Intelligence, Cambridge (own bio; press report April
  2026). [weak source: homepage compromised; see notes]
- **Areas:** philosophy of cognitive science; animal and machine minds; consciousness; AI
  ethics; human–AI relationships ("Social AI", "anthropomimesis").
- **Key works:** Shevlin2021Non; Shevlin2021Could; Shevlin2019Apply; Shevlin2024All;
  Shevlin2026Aeroplanes; Shevlin2026Three; Shevlin2026Anthropomimetic; Shevlin2020General;
  Shevlin2019Limits.
- **Published commitments:**
  - The "specificity problem" for applying consciousness theories beyond humans; defends a
    "modest theoretical approach" (modified Birch theory-light) (Shevlin2021Non) [abstract].
  - "Cognitive equivalence strategy": an AI is a psychological moral patient to the extent it
    shares cognitive mechanisms with animals we so regard (Shevlin2021Could) [abstract].
  - Biological features of consciousness, even essential ones, should not be extrapolated to
    rule out exotic AI consciousness (Shevlin2026Aeroplanes, commentary on Seth) [abstract].
  - Architectural debunking of LLM mentality is often too quick; "mere roleplay" views are
    unstable for anthropomimetic systems (Shevlin2026Three) [abstract].

### 22. Kacper Kowalczyk
- **Position:** unverified (a PhilArchive record, seen via search summary only, lists Rutgers–New
  Brunswick). [fetch request filed]
- **Areas (inferred from publications only):** formal ethics — population ethics, aggregation,
  risk, deontology, fanaticism, welfare economics.
- **Key works:** Kowalczyk2021Transfinitely; Kowalczyk2022People; Kowalczyk2024New;
  Kowalczyk2024Opaque; Kowalczyk2024Risk; Kowalczyk2025Saving; Gustafsson2026Ex.
- **Published commitments:**
  - Transfinite transitivity/acyclicity imply that adding good lives is better, bad lives worse,
    neutral lives equally good; supports a weak procreative asymmetry (Kowalczyk2021Transfinitely)
    [abstract].
  - Ex-ante deontology fails in sequential choice; we should prefer a more consequentialist
    morality (Kowalczyk2022People) [abstract].
  - A neglected argument for fanaticism limited to life-saving cases, compatible with some
    small-probability discounting, imprecision, risk-aversion (Kowalczyk2025Saving) [abstract via
    search summary].
  - Mahtani's opaque-identity puzzle does not undermine ex ante Pareto (Gustafsson2026Ex)
    [abstract].
  - Against hastening extinction even under significant risk aversion (Kowalczyk2024Risk)
    [abstract].

### 23. Pamela Robinson
- **Position:** Assistant Professor, Philosophy, UBC Okanagan (department page
  https://epp.ok.ubc.ca/about/contact/pamela-robinson; PhD Rutgers; previously ANU).
- **Areas (page):** rationality; ethics & metaethics; epistemology; AI ethics & safety;
  normative uncertainty.
- **Key works:** Robinson2022Moral (with Steele); Robinson2021Normative; Robinson2023Action;
  Robinson2024Ai; Robinson2023Moral; Goldstein2024Shutdown.
- **Published commitments:**
  - Noncognitivists can model moral uncertainty via the formal analogy with multi-objective
    decision problems (Robinson2022Moral) [abstract].
  - "Excluders" (only descriptive uncertainty matters) can escape the dependence problem
    (Robinson2021Normative) [abstract].
  - Shutdown-seeking AI proposal (with Goldstein) [abstract].
  - "The AI-design regress" (Robinson2024Ai) [title only; content not seen].

---

## Part B. Organisers (not judges; listed for context)

### Zachary Goodsell
- Assistant Professor (Presidential Young Professor), National University of Singapore; PhD USC
  2023 (homepage https://zacharygoodsell.com/, updated Aug 2026).
- Interests: logic, decision theory, epistemology, ethics, metaphysics, mathematics, language,
  AI. Project "Logical Maps" (databases of connections between principles, first for decision
  theory with unbounded utility).
- Works: Goodsell2023Decision; Goodsell2025Symmetries; Goodsell2021St; Goodsell2022Tossing;
  Goodsell2021Arithmetic; Goodsell2026Unknowable; Goodsell2025Morality; Goodsell2024Symmetry.
- Commitments [abstracts/summaries]: unbounded utility is compatible with a desirable decision
  theory; affine symmetry principles assign values to Pasadena/alternating St Petersburg;
  Anteriority is inconsistent with plausible axiology/decision principles; inferring
  counterfactual from causal independence (Morgenbesser's coin) is mistaken; new arguments
  against verificationism.

### Elliott Thornley
- Assistant Professor of Philosophy, NUS (homepage https://www.elliott-thornley.com/). Works on AI
  safety via decision theory; population ethics.
- Works: Thornley2024Shutdown; Thornley2025Towards; Thornley2021Impossibility;
  Thornley2021Dilemma; Thornley2025Critical; Shulman2025Much.
- Commitments [abstracts]: three theorems showing agents satisfying innocuous conditions will
  often try to prevent or cause shutdown-button presses; Arrhenius-style impossibilities can be
  repurposed for population *prospect* axiologies independent of Finite Fine-Grainedness;
  recent technical work on risk-averse AIs and "tie training".
- Funding: Forethought Research.

---

## Part C. Subfield clusters

Membership counts judges only (organisers in brackets). A judge can sit in several clusters.

### C1. Formal epistemology and Bayesian foundations
- **Members:** Fitelson, Easwaran, Weisberg, Salow, Greaves, Greco, Dorr; partly Hawthorne,
  Goldstein, Günther.
- **Questions:** accuracy-first justifications (probabilism, conditionalization); updating,
  supposition, deference and pooling; regularity and zero probability; confirmation measures;
  full vs partial belief; risk-sensitive epistemic utility.
- **Methods:** theorems and counterexamples; decision-theoretic modelling; some automated
  reasoning (PrSAT).
- **Hubs:** Phil Review, Mind, Noûs, PPR, BJPS, Phil Sci, JPL, Ergo, Phil Imprint, Oxford Studies
  in Epistemology; Open Handbook of Formal Epistemology (Pettigrew & Weisberg eds.); Weisberg SEP
  "Formal Epistemology"; Easwaran 2026 Routledge book; FEW.

### C2. Knowledge, higher-order knowledge, normality, inquiry
- **Members:** Hawthorne, Salow, Goldstein, Greco, Dorr; partly Mandelkern (assertion), Weisberg
  (bootstrapping, knowledge in action) [Goodsell].
- **Questions:** KK and omega knowledge; normality-based epistemic logic; safety and closure;
  knowledge–chance principles; dogmatism and evidence avoidance; value of information
  (Good's theorem); norms of assertion and inquiry.
- **Methods:** epistemic-logic models (normality orderings), carefully built cases, probability.
- **Hubs:** J Phil, Mind, Phil Review, Phil Studies, Inquiry symposium on *Iterated Knowledge*
  (Goodman, Greco, Holguín, Rosenkranz, Salow and others), Williamson's anti-luminosity
  tradition (named from general knowledge; not checked in this run).

### C3. Decision theory under extreme stakes (infinite/unbounded value, fanaticism, risk)
- **Members:** Tarsney, Easwaran, Nebel, Kowalczyk, Greaves, Weisberg (REU), Salow
  (risk-aversion), Fitelson [Goodsell, Thornley].
- **Questions:** fanaticism vs anti-fanaticism; unbounded utility; St Petersburg/Pasadena;
  stochastic dominance under background uncertainty; risk-weighted EU; Newcomb classification.
- **Methods:** axiomatic consistency/impossibility results; representation theorems.
- **Hubs:** Noûs, PPR, Mind, Phil Review, Analysis, Economics & Philosophy, Ergo; Cambridge
  Elements in Decision Theory; Buchak *Risk and Rationality*.

### C4. Formal ethics: axiology, aggregation, population, comparability
- **Members:** Nebel, Tarsney, Greaves, Kowalczyk, Dorr (comparability), Easwaran (value
  aggregation), Robinson (normative uncertainty) [Thornley, Goodsell].
- **Questions:** comparability/completeness of value; measurement and summability of
  well-being; ex ante Pareto and opaque identity; population axiology impossibility theorems;
  infinite ethics and impartiality; limited aggregation; normative uncertainty and metanormative
  regress; longtermism.
- **Methods:** social-choice and measurement theory; impossibility theorems; cases.
- **Hubs:** Ethics, Noûs, Phil Review, Mind, PPR, Utilitas, Economics & Philosophy, JESP, Social
  Choice and Welfare, J Econ Theory; *Essays on Longtermism* (OUP 2025); Oxford Handbook of
  Population Ethics; Greaves "Population axiology" (Phil Compass 2017).

### C5. Philosophy of language and formal semantics (modals, conditionals, generics, metasemantics)
- **Members:** Mandelkern, Dever, Cappelen, Sterken, Goldstein, Hawthorne, Dorr; partly
  Günther, Fitelson (triviality).
- **Questions:** dynamic vs bounded semantics; epistemic modals; conditionals and probability
  (triviality, Stalnaker's thesis, modus ponens); free choice; generics; externalist
  metasemantics; context and common ground.
- **Methods:** model-theoretic semantics, linguistic data, logic, some experiments.
- **Hubs:** Linguistics & Philosophy, Semantics & Pragmatics, J Phil, Phil Review, Mind, JPL,
  Amsterdam Colloquium; Mandelkern *Bounded Meaning* (OUP 2024).

### C6. Metaphysics, logic, causation and chance
- **Members:** Dorr, Hawthorne, Günther, Jaeger, Chalmers; partly Easwaran (set theory), Greaves
  (philosophy of physics) [Goodsell].
- **Questions:** higher-order metaphysics; modal variation; counterfactuals under determinism;
  actual causation (regularity, difference-making, causal models); high-level causation;
  chance in time travel; verificationism.
- **Methods:** higher-order and modal logic; causal models; physics.
- **Hubs:** Phil Review, Noûs, Mind, Phil Perspectives, JPL, Oxford Studies in Metaphysics,
  BJPS; SEP "Regularity and Inferential Theories of Causation" (Andreas & Günther).

### C7. Philosophy of AI cognition, meaning and interpretation
- **Members:** Chalmers, Cappelen, Dever, Mandelkern, Millière, Goldstein, Sterken, Shevlin,
  Vold.
- **Questions:** do LLM words refer/mean; do LLMs have beliefs, desires, introspection; grounding;
  interpretability (mechanistic, propositional); evaluation methodology (anthropocentric bias);
  communication with AI.
- **Methods:** externalist metasemantics; interpretationism; behavioural and mechanistic
  experiments; conceptual analysis.
- **Hubs:** Inquiry, Phil Perspectives, Computational Linguistics, Phil Studies, Phil and the Mind
  Sciences, Philosophy of AI (journal), *Communicating with AI* (OUP 2026), *Making AI
  Intelligible* (OUP 2021), Millière & Buckner "Philosophical Introduction to Language Models".

### C8. AI consciousness, welfare, moral status
- **Members:** Chalmers, Shevlin, Goldstein, Millière, Vold.
- **Questions:** indicators of consciousness in AI; specificity problem; moral patiency; AI
  wellbeing without consciousness; AI rights.
- **Methods:** theory-driven indicator assessment, comparative cognition, ethics.
- **Hubs:** JCS, Mind & Language, BBS, Asian J Phil symposium on "AI Wellbeing", Long et al.
  "Taking AI Welfare Seriously" (2024, Chalmers co-author); "Identifying Indicators of
  Consciousness in AI Systems" (multi-authored; on Chalmers's homepage; title only).

### C9. AI safety, alignment and governance (formal and conceptual)
- **Members:** Goldstein, Robinson, Tarsney, Cappelen, Dever, Hawthorne, Vold, Millière, Greaves,
  Günther, Sterken [Thornley].
- **Questions:** shutdown/corrigibility; instrumental convergence; deception/manipulation;
  alignment subproblems; "survival stories"; safety-measure backfire; AI rights as safety.
- **Methods:** decision-theoretic theorems (shutdown), taxonomy, expected-value arguments,
  legal-institutional design.
- **Hubs:** Phil Studies (2024–25 AI-safety cluster: Thornley; Goldstein & Robinson; Cappelen,
  Dever & Hawthorne; Millière; Tarsney), Philosophy of AI, AI & Society, AIES proceedings.

### C10. Conceptual engineering and metaphilosophy
- **Members:** Cappelen, Sterken, Dever, Chalmers; Greco (idealization/modelling methodology).
- **Hubs:** *Conceptual Engineering and Conceptual Ethics* (OUP 2020); Inquiry; Cappelen *Fixing
  Language*.

### Cross-cutting observations (facts, for lane choice)
- The densest overlap on the panel is the triangle **formal epistemology – decision theory –
  formal ethics** (C1, C3, C4): about 14 of 23 judges have published in at least one of them, and the organisers' own work sits here.
- **AI-related philosophy** (C7–C9) is the second-largest block (about 13 judges with at least one
  AI-related publication), but expertise is split between interpretation/meaning, consciousness/welfare,
  and safety; the formal-safety strand (shutdown, incomplete preferences, risk aversion) overlaps
  C3/C4.
- **Language/semantics** (C5) has a strong specialist core (Mandelkern, Dever, Goldstein,
  Cappelen, Sterken) plus Dorr and Hawthorne.
- Several coauthorship links (Dorr–Hawthorne–Goodsell–Nebel; Cappelen–Dever–Hawthorne–Goldstein;
  Salow–Fitelson–Goodman; Tarsney–Greaves) mean a contribution in those areas will likely be read
  by several judges who know the same literature well.

### Crowding (estimate, not data)
Expected density of other AI-generated entries, judged from the competition's framing (it is
about AI's philosophical ability) and the topics AI systems are most often asked about:
1. **Most crowded: AI consciousness / moral status / "what it is like to be an LLM"** (C8). Expect
   many entries; originality bar very high; verifiability low.
2. LLM understanding, meaning, reference, belief attribution (C7).
3. AI alignment and safety ethics, discursive rather than formal (C9 conceptual strand).
4. Metaphilosophy of AI doing philosophy; conceptual engineering applied to AI.
5. Moderate: fanaticism/longtermism and population ethics (well-known to AI systems via
   effective-altruism literature).
6. Low: normality/KK epistemic logic, comparability, conditionals/triviality, causal models,
   higher-order metaphysics, unbounded-utility axiomatics.
