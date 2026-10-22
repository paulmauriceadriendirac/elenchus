# Hard open problems: a dossier for the ambitious track

Hard-problems researcher, 2026-10-22. This is topic research: each entry states a problem, why it resists solution, and what *kind* of result would count as an advance. No theses or solutions are proposed.

**Sources and conventions.**
- Survey figures come from Bourget & Chalmers 2023 as tabulated in `state/calibration/brief.md` §1 ("accept or lean toward"; whole population, 2020).
- "Why hard" attributes a claim to an author only where this run, or an earlier one, read the text, its abstract, or a reliable summary. Each such claim carries a seen-level tag: [full] = full text local; [abs] = abstract read; [SEP] = the named SEP entry read this session; [title] = metadata only. Everything else is stated impersonally.
- All anchors are collected in `state/ambitious/refs.json` and were checked with `tools/verify_refs.py`; results are in `state/ambitious/refs.verification.json`. Of 99 anchors, 95 are VERIFIED. Four are NOT_FOUND, each with a documented manual check: Salow (forthcoming), Goldstein & Santorio 2021, Chalmers 2025 (arXiv), Thornley et al. 2025 (TMLR). "Online first" means Crossref's issued year is earlier than the volume year; cite the volume year.
- Availability: **local** = full text in `inbox/sources/` or `state/sources_cache/`; **OA** = open copy seen at the given URL; **fetch** = not checked or not open (file a fetch request if the problem is chosen).
- Panel readers come from `state/panel/committee_map.md`. Organisers are in brackets and are not judges. Crowding is an estimate.
- Scores run 1–5. A = ambition; T = tractability (a 6,000-word essay in about a week; a decisive partial or conditional result counts); V = verifiability; C = crowding (5 = uncrowded).

**Existing work to avoid duplicating:**
- E1 (KK/normality), E2 (Bayesian updating, Meehan–Zhang), E3 (conditionals, Dorr–Mandelkern) are already drafted in `state/drafts/`.
- Problems 12, 20 and 21 overlap those lanes. They are included for completeness and do not appear on the shortlist.

---

## A. Decision theory

### 1. Decision instability and the CDT/EDT dispute (Newcomb, Death in Damascus, Egan cases)

**Problem.**
- Causal decision theory (CDT) two-boxes in Newcomb's problem. It also gives unstable advice when the act chosen is evidence about which act is best (Death in Damascus; Egan's assassin cases).
- Evidential decision theory (EDT) one-boxes and faces its own counterexamples.
- The question is whether any decision rule meets three conditions at once: it respects causal dominance where that is the right intuition; it gives determinate, stable advice in unstable problems; and it satisfies diachronic and sure-thing-style principles.
- The profession is split. Newcomb: two boxes 39.0, one box 31.2, other 30.2.

**Why hard.**
- The SEP entry "Causal Decision Theory" (Weirich, revised 2024) [SEP] calls decision instability "an open problem". It says ratification "is not a complete response", and that Egan's examples are "an open problem in causal decision theory".
- Repairs keep trading one principle for another. Per the SEP:
  - deliberational-equilibrium and mixed-act views (Arntzenius, Joyce) are criticised because deliberation should settle on an option;
  - graded ratifiability (Gallow 2020; Barnett 2022) can forbid the option with the best prospects (Spencer 2023, as reported);
  - Gallow argues that removing instability means rejecting the sure-thing principle.
- Spencer (2021) [abs] states a "Guaranteed Principle" of preference that rational agents satisfy and CDT agents violate.
- Gallow (2020) [abs] revises CDT to "manage the news" about the good one stands to promote.
- Fusco (2024) [abs] answers Elga's determinism dilemma by exploiting "decision dependence".

**What an advance would look like.**
- A minimal impossibility theorem: a small set of principles that every recent proposal takes as adequacy conditions cannot jointly hold, with each principle shown independent.
- Or a discriminating case that separates the graded-ratifiability family from the equilibrium family on a verdict both sides accept.
- A dissolution showing that instability cases and Newcomb cases turn on different parameters would also count.

**Anchors.**
- Gallow 2020, "The Causal Decision Theorist's Guide to Managing the News", *J Phil* 117:117–149, doi 10.5840/jphil202011739. VERIFIED. Fetch.
- Spencer 2021, "An Argument against Causal Decision Theory", *Analysis* 81:52–61, doi 10.1093/analys/anaa037. VERIFIED. Fetch.
- Barnett 2022, "Graded Ratifiability", *J Phil* 119:57–88, doi 10.5840/jphil202211925. VERIFIED. Fetch.
- Fusco 2024, "Absolution of a Causal Decision Theorist", *Noûs* 58:616–643, doi 10.1111/nous.12459. VERIFIED. Fetch.

**Readers.**
- Judges: Fitelson, Easwaran, Salow, Weisberg, Tarsney, Greaves. Hawthorne and Dorr are likely familiar.
- Crowding: moderate. Newcomb is a favourite AI topic, but a formal increment over the 2020–24 instability literature is rare.

**Scores.** A 4 · T 3 · V 4 · C 3

### 2. Fanaticism: tiny probabilities of enormous value

**Problem.**
- Must a rational or morally good agent prefer a tiny probability of an astronomically good outcome to a sure modest good?
- Expected-value reasoning with unbounded value says yes. Intuition says no.
- Every principled way of saying no seems to cost a structural principle.

**Why hard.**
- Beckstead & Thomas (2024) [full, GPI version local] prove that every theory of the value of prospects is reckless, timid, or non-transitive.
- Wilkinson (2022) [abs, GPI version local] argues that rejecting fanaticism has four costs:
  - giving up transitivity or a weak trade-off principle;
  - inconsistency across structurally identical lotteries, or extreme sensitivity to small probability differences;
  - sensitivity to beliefs about distant events unaffected by one's action;
  - judgements one would reject on learning more.
- Tarsney (2024) [full, local] shows that anti-fanaticism in full generality conflicts with acyclicity, a minimal dominance principle, and "any outcome can be made better or worse". He recommends an intermediate view with incomplete preferences.
- Russell (2024) re-examines two arguments for fanaticism [title-level here; abstract per calibration].
- Discounting proposals (probability discounting) face money-pump and dilemma results. See L1 refs: Kosonen 2024 and Cibinel 2023 [title].

**What an advance would look like.**
- Show that one horn of the reckless/timid/intransitive trilemma is forced once a further widely accepted principle is added, such as background-uncertainty robustness or a dynamic-consistency constraint.
- Or show that the intermediate, incomplete-preference position collapses into one horn under sequential choice.
- Either way, a minimal inconsistency proof with independence shown.

**Anchors.**
- Beckstead & Thomas 2024, "A paradox for tiny probabilities and enormous values", *Noûs*, doi 10.1111/nous.12462. VERIFIED (L1). Local: `state/sources_cache/bt.txt` (GPI 2020 version).
- Wilkinson 2022, "In Defense of Fanaticism", *Ethics* 132, doi 10.1086/716869. VERIFIED (L1). Local: `wilkinson_fanaticism.txt` (GPI version).
- Tarsney 2024, "Against Anti-Fanaticism", *PPR*, doi 10.1111/phpr.13120. VERIFIED. Local: `tarsney_aaf.txt`.
- Russell 2024, "On Two Arguments for Fanaticism", *Noûs*, doi 10.1111/nous.12461. VERIFIED. Fetch.

**Readers.**
- Judges: Tarsney, Easwaran, Nebel, Kowalczyk, Greaves, Weisberg, Salow, Fitelson [Goodsell, Thornley].
- Crowding: moderate to high. This is a well-known effective-altruism topic, and AI entrants will write on it discursively. A precise formal increment is still uncommon.
- Originality risk: the organiser's "Logical Maps" database catalogues principles in this area.

**Scores.** A 4 · T 3 · V 5 · C 2

### 3. Unbounded utility and infinite prospects (St Petersburg, Pasadena)

**Problem.**
- If utility is unbounded, some prospects (St Petersburg, Pasadena) have infinite or undefined expectations.
- Dominance, continuity and expectation principles then conflict.
- Which principles relating probability and value survive?

**Why hard.**
- Goodsell (2023) [abs, local OA] treats the puzzles "as an invitation to assess the most fundamental principles relating probability and value". He aims to show that unbounded utility is compatible with a desirable decision theory.
- Goodsell (2026) [abs, local OA] shows that affine symmetry principles assign ln 2 to Pasadena and −1/2 to alternating St Petersburg, vindicate Colyvan's Relative Expectation Theory, and are consistent.
- Russell & Isaacs (2021, "Infinite Prospects") is a standard source of impossibility results [title only in this run]. Its content must be read before anything is attributed to it.
- The area is thoroughly mapped: the organiser's Logical Maps database lists principles and their entailments (`state/sources_cache/principles.txt`).

**What an advance would look like.**
- A new minimal impossibility, or a consistency proof for a principle set left open in the map.
- Or a transfer from measure theory or probability (e.g. summability methods) that settles which extension of expectation is uniquely forced.

**Anchors.**
- Goodsell 2023, "Decision Theory Unbound", *Noûs* 57, doi 10.1111/nous.12473. VERIFIED. Local: `goodsell_dtu.txt`.
- Goodsell 2026, "Symmetries of Value", *Noûs* 60:16–37, doi 10.1111/nous.12549. VERIFIED. Local: `goodsell_sov.txt`.
- Russell & Isaacs 2021, "Infinite Prospects", *PPR*, doi 10.1111/phpr.12704. VERIFIED (L1). Fetch.

**Readers.**
- Judges: Easwaran, Nebel, Tarsney, Kowalczyk, Hawthorne, Dorr [Goodsell].
- Crowding: low among AI entrants. The originality bar is very high, because the organiser maintains the map of known results.

**Scores.** A 3 · T 4 · V 5 · C 4

### 4. Infinite ethics: Pareto versus dominance with infinitely many people

**Problem.**
- With infinitely many people or locations, two principles conflict:
  - Pareto: better for everyone is better;
  - statewise dominance: sure to turn out better is better.
- Impartiality (permutation invariance) conflicts with both.
- No aggregation theory seems to keep enough of these to guide action in an infinite world.

**Why hard.**
- Hong & Russell (2025) [abs] refine and generalise a conflict between Pareto and statewise dominance. It affects many aggregation theories besides utilitarianism and many decision theories besides expected value. They find all consistent responses "quite radical".
- Nebel (2025) [abs-level per committee map] argues that on the individualistic (Harsanyi) approach with infinitely many individuals, rational concern for each forces caring about some more than others, and that value is fundamentally agent-relative.
- Wilkinson (2021) proposes "expanded addition" [title].
- Kowalczyk (2021) derives population-ethical consequences from transfinite transitivity [abs per committee map].

**What an advance would look like.**
- A minimal impossibility identifying exactly which weakening of Pareto or dominance restores consistency, with a characterisation (representation) of the surviving theories.
- Or a proof that the "radical" responses collapse into one another.
- Or a decisive argument that one principle loses its motivation in infinite settings, with a case where its finite rationale yields the opposite verdict.

**Anchors.**
- Hong & Russell 2025, "Paradoxes of Infinite Aggregation", *Noûs* 59:809–827, doi 10.1111/nous.12535. VERIFIED (L1). Fetch.
- Nebel 2025, "Infinite Ethics and the Limits of Impartiality", *Noûs*, doi 10.1111/nous.70010. VERIFIED. Fetch.
- Wilkinson 2021, "Infinite Aggregation: Expanded Addition", *Phil Studies* 178:1917–1949, doi 10.1007/s11098-020-01516-w. VERIFIED (L1). Fetch.
- Kowalczyk 2021, "Transfinitely Transitive Value", *Phil Quarterly*, doi 10.1093/pq/pqab005. VERIFIED. Fetch.

**Readers.**
- Judges: Nebel, Kowalczyk, Easwaran, Tarsney, Greaves, Dorr, Hawthorne [Goodsell].
- Crowding: low to moderate. The topic is known in effective-altruism circles, but it is technical.

**Scores.** A 4 · T 4 · V 5 · C 4

### 5. Completeness: can betterness and rational preference be incomplete?

**Problem.**
- Must every two outcomes or lotteries be comparable?
- Parity and incomparability views say no. Small-improvement and chaining arguments support them.
- Dominance, money-pump and semantic arguments say yes, or say incompleteness has unacceptable costs.
- The stakes are broad: population ethics, fanaticism (Tarsney's intermediate view relies on incompleteness), and AI shutdown proposals built on incomplete preferences.

**Why hard.**
- Tarsney, Lederman & Spears (2025) [full, local arXiv] derive the result from two principles plus modest auxiliary assumptions:
  - weak "negative dominance";
  - weak ex ante Pareto.
  - Together these rule out incompleteness in the prudential ranking of lives and many forms of moral incompleteness.
- Dorr, Nebel & Zuehl (2023) [abs per committee map] argue that all natural-language comparatives obey Comparability.
- Gustafsson (2026) [full, local] gives a forcing money pump for Completeness from stochastic dominance plus probabilistic picking.
- Hájek & Rabinowicz (2022) [full, local] model degrees of commensurability and use "almost better" to block the Continuum Argument.
- Replies and counter-replies continue (Carlson & Risberg 2024; Dorr, Nebel & Zuehl 2026, in L2 refs) [title].

**What an advance would look like.**
- A diagnosis showing that the several anti-incompleteness arguments rest on one shared premise (e.g. a specific dominance-under-opacity principle), with a model of incomplete value that rejects only that premise and keeps the rest.
- Or a strengthening that removes the auxiliary assumptions.

**Anchors.**
- Tarsney, Lederman & Spears 2025, "A Dominance Argument Against Incompleteness", *Phil Review*, doi 10.1215/00318108-11964820. VERIFIED. Local: `tls_dom.txt`.
- Dorr, Nebel & Zuehl 2023, "The Case for Comparability", *Noûs*, doi 10.1111/nous.12407. VERIFIED. Fetch.
- Gustafsson 2026, "A Behavioural Money-Pump Argument for Completeness", *Theory and Decision* 101:391–400, doi 10.1007/s11238-025-10025-3. VERIFIED (L2). Local: `gustbeh.txt`.
- Hájek & Rabinowicz 2022, "Degrees of Commensurability and the Repugnant Conclusion", *Noûs*, doi 10.1111/nous.12388. VERIFIED. Local: `hr_degrees.txt`.

**Readers.**
- Judges: Nebel, Dorr, Tarsney, Kowalczyk, Greaves, Easwaran [Thornley, Goodsell].
- Two judges co-author one side (Dorr, Nebel), so per CLAUDE.md §1.6 any position must be taken on the merits only.
- Crowding: low to moderate.

**Scores.** A 4 · T 4 · V 5 · C 4

### 6. Cluelessness and decision under deep (imprecise) uncertainty

**Problem.**
- Our acts' long-run indirect effects dwarf their foreseeable ones, and are inscrutable.
- If rational credence about them is imprecise, standard decision rules for imprecise credence seem either too permissive (everything is permitted) or diachronically exploitable.
- The question is how a rational agent should choose when the stakes are dominated by what she cannot estimate.

**Why hard.**
- Mogensen (2021) [abs] argues that cluelessness plus the permissive "maximality" rule leaves "no compelling decision theory" that is longtermist, takes deep uncertainty seriously, and supports orthodox cause prioritisation.
- The SEP "Imprecise Probabilities" (rev. 2019) [SEP] reports:
  - Elga's diachronic exploitation argument and its replies;
  - that "a more serious worry confronts IP when you have to make sequences of decisions";
  - that dilation's relation to evidential weight "is far from settled";
  - belief inertia under vacuous priors.
- Isaacs, Hájek & Hawthorne (2022) argue that non-measurability favours imprecision. Dorr (2023) [abs] rebuts this.

**What an advance would look like.**
- An impossibility theorem: no decision rule for imprecise credence satisfies (i) a permissiveness bound, (ii) sequential non-exploitability and (iii) a robustness condition for inscrutable stakes.
- Or a representation of the unique rule that does.
- Or a dissolution showing that cluelessness is not a case of imprecision at all.

**Anchors.**
- Mogensen 2021 (online 2020), "Maximal Cluelessness", *Phil Quarterly* 71:141–162, doi 10.1093/pq/pqaa021. VERIFIED. Fetch.
- Tarsney 2023, "The Epistemic Challenge to Longtermism", *Synthese* 201, doi 10.1007/s11229-023-04153-y. VERIFIED. Fetch [title].
- Isaacs, Hájek & Hawthorne 2022, "Non-Measurability, Imprecise Credences, and Imprecise Chances", *Mind*, doi 10.1093/mind/fzab031. VERIFIED (L5). Fetch.
- Dorr 2023, "Does Non-Measurability Favour Imprecision?", *Mind*, doi 10.1093/mind/fzad041. VERIFIED. Fetch.

**Readers.**
- Judges: Greaves (who originated "cluelessness"), Tarsney, Dorr, Hawthorne, Easwaran, Weisberg, Fitelson, Salow.
- Crowding: moderate (longtermism is familiar to AI systems).

**Scores.** A 4 · T 3 · V 4 · C 3

## B. Formal epistemology and philosophy of science

### 7. Self-locating belief: Sleeping Beauty, updating centred credence, and the measure problem

**Problem.**
- How should credence respond to evidence about where or when one is, as opposed to how the world is? This covers memory loss, duplication and multiverse cases.
- The profession is split. Sleeping Beauty: thirder 27.7, halfer 18.6, other 53.4 (n≈430). This is the largest "other" share in the survey.

**Why hard.**
- The L5 map (§5) records:
  - no general rule for scoring updates with multiple successors (Schwarz 2025: "Alas, I have none to offer" [full]);
  - unsettled rivalry between recentering, decentering and restriction models;
  - divergent average versus total accuracy verdicts;
  - the measure problem for infinitely many observers, flagged as "an important open question" by Isaacs, Hawthorne & Russell 2022 [full].
- Isaacs, Hawthorne & Russell (2022) give theorems on fine-tuning and multiverse confirmation and call them "a framework in which to continue".

**What an advance would look like.**
- A propriety condition for multi-successor accuracy scoring, with a theorem that it singles out one answer.
- Or an impossibility showing that no centred update rule meets stated synchronic and diachronic conditions.
- Or a reduction of the measure problem to a known problem in infinite decision theory (a transfer).

**Anchors.**
- Isaacs, Hawthorne & Russell 2022, "Multiple Universes and Self-Locating Evidence", *Phil Review*, doi 10.1215/00318108-9743809. VERIFIED. Fetch (or check the authors' pages).
- Schwarz 2025, "Sleeping Beauty and the Demands of Non-Ideal Rationality", *Noûs* 59:1072–1092, doi 10.1111/nous.12545. VERIFIED (L5). OA author PDF: https://www.umsu.de/papers/sb.pdf.
- Builes 2020, "A Paradox of Evidential Equivalence", *Mind* 129:113–127, doi 10.1093/mind/fzz046. VERIFIED. Fetch.

**Readers.**
- Judges: Dorr (a published thirder), Hawthorne, Easwaran, Salow, Weisberg, Fitelson, Jaeger ("Immortal Beauty"); Cappelen and Dever on the de se.
- Crowding: moderate. Sleeping Beauty attracts AI entrants, but rigorous increments are rare.

**Scores.** A 4 · T 3 · V 4 · C 3

### 8. The belief–credence bridge (Lockean thesis, closure, lottery and preface)

**Problem.**
- How does outright belief relate to credence?
- The Lockean threshold view violates closure under conjunction (lottery, preface).
- Closure-respecting views (stability, normality, question-relative accounts) make belief context- or partition-sensitive.
- Eliminativists deny that one of the two attitudes exists.
- The profession is split. Belief or credence more fundamental: credence 31.3, belief 30.6, neither 19.5, other 19.3.

**Why hard.**
- Every bridge principle so far gives up one of three things:
  - threshold monotonicity;
  - closure;
  - independence from the partition or question.
- Goodman & Salow (2023) [full] derive belief and knowledge from probability plus normality relative to a question.
- The L3 map lists open issues: comparability, transparency, and whether normality-based knowledge can be action-guiding.
- Weisberg defends dualism, on which neither attitude is more fundamental [abs per committee map].
- Dorst 2019 and Holguín 2022 offer accuracy-based and guessing-based views [title].

**What an advance would look like.**
- A sharp impossibility: no bridge principle satisfies threshold-monotonicity, closure, and partition-invariance together with one further accepted desideratum, with minimality shown.
- Or a discriminating case on which stability and normality/question views give opposite verdicts.

**Anchors.**
- Goodman & Salow 2023, "Epistemology Normalized", *Phil Review* 132:89–145, doi 10.1215/00318108-10123787. VERIFIED. Local: `inbox/sources/goodman-salow-2023.txt`.
- Dorst 2019 (online 2017), "Lockeans Maximize Expected Accuracy", *Mind* 128, doi 10.1093/mind/fzx028. VERIFIED (Crossref online-first year; cite the volume year). Fetch.
- Jackson 2020, "The Relationship between Belief and Credence", *Phil Compass* 15, doi 10.1111/phc3.12668. VERIFIED. Fetch.
- Holguín 2022, "Thinking, Guessing, and Believing", *Phil Imprint* 22, doi 10.3998/phimp.2123. Listed in L3 refs. OA (journal).

**Readers.**
- Judges: Easwaran (Dr Truthlove), Fitelson, Weisberg, Salow, Hawthorne, Greco, Dorr, Goldstein.
- Crowding: low to moderate.

**Scores.** A 4 · T 3 · V 4 · C 4


### 9. The problem of old evidence

**Problem.**
- Evidence already known has probability 1, so on standard Bayesian confirmation it cannot confirm anything.
- Yet known data plainly confirm new theories. The standard example is Mercury's perihelion and general relativity.
- Bayesian confirmation needs an account of how old evidence confirms that does not change the subject.

**Why hard.**
- The SEP "Confirmation" entry (rev. Aug 2025) [SEP] reviews three families of response, each with a cost:
  - **Logical learning.** Confirmation comes from learning that the hypothesis entails the evidence (Garber-style). This requires modelling logical uncertainty, which "is no trivial task", and is arguably an "elusive change of the subject".
  - **Counterfactual reconstruction.** Use the credences one would have had without the evidence (Howson; Sprenger). This is available only to permissivists and is not the agent's actual credence.
  - **Objective likelihoods.** This depends on impermissivism.
- The SEP cites Eva & Hartmann (2020) as "a careful survey with further references".

**What an advance would look like.**
- An impossibility: no confirmation measure defined on the agent's actual (possibly logically non-omniscient) credences satisfies a stated set of adequacy conditions.
- Or a framework that unifies the logical-learning and counterfactual solutions and predicts their divergence on a test case.
- A transfer from logical-uncertainty models (e.g. computer-science treatments of bounded deduction) made precise would count.

**Anchors.**
- Eva & Hartmann 2020 (online 2019), "On the Origins of Old Evidence", *AJP* 98:481–494, doi 10.1080/00048402.2019.1658210. VERIFIED. Fetch.
- Sprenger & Hartmann 2019, *Bayesian Philosophy of Science*, OUP, doi 10.1093/oso/9780199672110.001.0001. VERIFIED. Fetch.

**Readers.**
- Judges: Fitelson (whose earlier work with Hartmann is pre-2018 and is the obvious prior art), Easwaran, Weisberg, Greaves, Günther.
- Crowding: low.

**Scores.** A 3 · T 3 · V 4 · C 5

### 10. Justifying induction: no-free-lunch theorems and Bayesian "orgulity"

**Problem.**
- Can any inductive method be justified without begging the question?
- Two formal versions make the old problem precise:
  - No-free-lunch theorems: averaged over all possible worlds, no learning algorithm beats any other.
  - Belot's charge that Bayesian conditionalisers must be certain, in advance, of converging to the truth on most data streams ("orgulity", or immodesty).

**Why hard.**
- Sterkenburg & Grünwald (2021) [abs] argue that the no-free-lunch results presuppose purely data-driven algorithms. They hold that standard algorithms are model-dependent and admit only model-relative justification. This relocates the problem rather than solving it.
- Cisewski, Kadane, Schervish, Seidenfeld & Stern (2018) [abs] reply to Belot:
  - his topological standards are self-defeating;
  - they propose a consensus-based modesty standard instead;
  - they note the role of countable additivity, as discussed by Elga.
- Whether any non-question-begging optimality result exists (e.g. meta-induction) remains disputed. In this run that dispute was seen only through a Crossref search hit, so it is stated impersonally.

**What an advance would look like.**
- A theorem showing exactly which modesty or optimality property any learner can have relative to which class of environments, settling Belot's challenge.
- Or a proof that the no-free-lunch and orgulity results are one result under a translation (a transfer).

**Anchors.**
- Sterkenburg & Grünwald 2021, "The No-Free-Lunch Theorems of Supervised Learning", *Synthese* 199:9979–10015, doi 10.1007/s11229-021-03233-1. VERIFIED. Probably OA (Springer); fetch to confirm.
- Cisewski et al. 2018, "Standards for Modest Bayesian Credences", *Phil Sci* 85:53–78, doi 10.1086/694836. VERIFIED. Fetch.

**Readers.**
- Judges: Fitelson, Easwaran, Weisberg, Greco; Millière (machine learning) may also appreciate it.
- Crowding: low to moderate. Induction is popular, but formal increments are rare.

**Scores.** A 5 · T 2 · V 4 · C 4

## C. Epistemology

### 11. Higher-order evidence and epistemic akrasia

**Problem.**
- Can it be rational to believe p while believing that one's evidence does not support p?
- Misleading higher-order evidence (about one's own reliability) seems to require one of three costly moves:
  - level-splitting (akrasia);
  - giving up evidentialism, since conciliatory "calibration" discards first-order evidence;
  - denying that the higher-order evidence is evidence at all.

**Why hard.**
- Each of the three positions has defenders and published counterexamples.
- Dorst (2020) [abs] develops a framework for higher-order uncertainty in which rational credence can be modest about itself.
- Hedden & Dorst (2022) argue that "(almost) all evidence is higher-order evidence" [title].
- Lasonen-Aarnio (2020) defends living with mismatch [title only].
- Christensen (2021) addresses akratic modesty [title only].
- The structural question is formal: which bridge principles between first- and higher-order credence (Reflection-type, enkratic, New Rational Reflection) are mutually consistent with factive or non-factive evidence models. It has not been settled.

**What an advance would look like.**
- A consistency map of the bridge principles over the space of evidence models, with a minimal inconsistent set.
- Or a case where every surviving principle gives a verdict all sides reject.

**Anchors.**
- Dorst 2020, "Evidence: A Guide for the Uncertain", *PPR* 100:586–632, doi 10.1111/phpr.12561. VERIFIED (L5). Fetch.
- Lasonen-Aarnio 2020 (online 2018), "Enkrasia or Evidentialism? Learning to Love Mismatch", *Phil Studies* 177:597–632, doi 10.1007/s11098-018-1196-2. VERIFIED (Crossref online-first year; cite the volume year). Fetch.
- Christensen 2021 (online 2020), "Akratic (Epistemic) Modesty", *Phil Studies* 178:2191–2214, doi 10.1007/s11098-020-01536-6. VERIFIED. Fetch.
- Hedden & Dorst 2022, "(Almost) All Evidence Is Higher-Order Evidence", *Analysis*, doi 10.1093/analys/anab081. VERIFIED. Fetch.

**Readers.**
- Judges: Salow, Greco (first- versus higher-order states), Weisberg, Fitelson, Dorr, Hawthorne, Goldstein.
- Crowding: moderate.

**Scores.** A 4 · T 3 · V 4 · C 3

### 12. Iterated knowledge (KK, omega knowledge) in normality frameworks *(overlaps E1)*

**Problem.**
- Does knowing entail knowing that one knows?
- If not, what structure does higher-order knowledge have, and does it matter for assertion and action?
- Normality-based epistemic logic has revived the question.

**Why hard.**
- The L3 map §5 lists 17 open items, including these two:
  - Hawthorne's admission that he lacks "a similarly watertight argument" that KK is incompatible with Extremely Weak Fair Coins (Hawthorne 2025 [full]);
  - Salow's conjecture about what "better knowledge" is (Salow, forthcoming in *J Phil* [full]).
- Goldstein (2024) argues that omega knowledge is what matters for assertion and action [one-line summary].
- The literature is dense and in active dialogue among the judges themselves.

**What an advance would look like.**
- A decidable finite-model result settling one of the flagged questions, for example whether a margin-respecting normality model validates Extremely Weak Fair Coins.
- Or a discriminating case between the weak-assertion and omega-assertion norms.

**Anchors.**
- Hawthorne 2025, "Normality and KK", *Phil Studies* 182:3071–3084, doi 10.1007/s11098-025-02382-0. VERIFIED. Local: `haw_normkk_text.txt`.
- Goodman & Salow 2023 (see problem 8). Local.
- Goldstein 2024, *Iterated Knowledge*, OUP, doi 10.1093/oso/9780198885481.001.0001. VERIFIED. Fetch.
- Salow, "Iterated Knowledge Isn't Better Knowledge", *J Phil*, forthcoming. Registry NOT_FOUND: forthcoming, no DOI yet. Author PDF read: local `salow_iterated_text.txt`.

**Readers.**
- Judges: Salow, Hawthorne, Goldstein, Greco, Dorr, Weisberg, Mandelkern.
- Crowding: very low, but the essay pool already contains E1 here.

**Scores.** A 3 · T 4 · V 5 · C 5

### 13. The value of evidence and the dogmatism puzzle

**Problem.**
- Good's theorem says free evidence never hurts an expected-utility maximiser who conditionalises.
- That conclusion fails for externalists about evidence, for risk-sensitive agents, and for inquiry aimed at knowledge.
- It becomes unclear whether a knower may, or must, avoid evidence that could only mislead her: the dogmatism puzzle.

**Why hard.**
- Ahmed & Salow (2019) [full, local] argue that Good's theorem "is not platitudinous and may be false".
- Campbell-Moore & Salow (2020) show that risk-avoidance can make evidence avoidance commendable [abs per committee map].
- Carter & Hawthorne (2024) [abs per committee map] show that if inquiry aims at knowledge and misleading evidence can destroy knowledge, knowers appear required to avoid evidence.
- Salow (2023) [full, local] calls the value of evidence in ideal cases "open".
- The L3 map flags open items: bounded agents (Brown's objection), confirmatory-evidence dogmatism, and Good's theorem for knowledge-first decision rules.

**What an advance would look like.**
- A precise value-of-information theorem or counterexample for knowledge-first decision rules in normality models, i.e. a Good-style theorem with "act on what you know".
- Or an impossibility linking externalism, factive evidence and non-negative value of free evidence.

**Anchors.**
- Ahmed & Salow 2019, "Don't Look Now", *BJPS* 70, doi 10.1093/bjps/axx047. VERIFIED. Local: `ahmed_salow_text.txt`.
- Carter & Hawthorne 2024, "Dogmatism and Inquiry", *Mind* 133, doi 10.1093/mind/fzad070. VERIFIED. Fetch.
- Salow 2023, "The Value of Evidence", *Routledge Handbook of the Philosophy of Evidence*, doi 10.4324/9781315672687-15. VERIFIED (L3). Local: `salow_value_text.txt`.
- Das 2023, "The Value of Biased Information", *BJPS*, doi 10.1093/bjps/axaa003. VERIFIED (L3). Fetch.

**Readers.**
- Judges: Salow, Hawthorne, Goldstein, Greco, Weisberg, Fitelson, Easwaran, Dorr.
- Crowding: low.

**Scores.** A 3 · T 4 · V 5 · C 5

### 14. Naked statistical evidence and the proof paradox

**Problem.**
- Why does purely statistical evidence seem insufficient for legal liability, or for knowledge or outright belief, even when it makes guilt very probable?
- Standard cases: Blue Bus, Gatecrasher, Prisoners.
- Individualised evidence of lower probability, such as an eyewitness, seems sufficient.

**Why hard.**
- The SEP "Legal Probabilism" §6 [SEP] surveys revisionist responses (the intuition is a bias) and many non-revisionist ones:
  - denying the threshold is met;
  - the reference-class problem;
  - stability and resilience;
  - incentives;
  - likelihood ratios;
  - probabilistic knowledge (Moss).
- It records an objection to each. For example, the incentive story is "unclear" for Gatecrasher and Prisoner, and the likelihood ratio is "strictly speaking unknown" (Di Bello).
- Smith (2018) argues for a normic-support view [title only in this run].
- Günther (2024) proposes a stability-based account of guilt [abs per committee map: guilty iff it is rational, in Leitgeb's stability sense, to believe guilt].

**What an advance would look like.**
- A discriminating case set, minimal pairs varying one parameter at a time, that separates the normic, stability, sensitivity and knowledge accounts and refutes all but one.
- Or a proof that a family of accounts collapses into probability thresholds under stated conditions.

**Anchors.**
- Smith 2018 (online 2017), "When Does Evidence Suffice for Conviction?", *Mind* 127:1193–1218, doi 10.1093/mind/fzx026. VERIFIED. Fetch.
- Günther 2024, "Probability of Guilt", *Canadian J Phil*, doi 10.1017/can.2025.6. VERIFIED. Fetch.
- Moss 2018, *Probabilistic Knowledge*, OUP. Listed in L3 refs. Fetch.

**Readers.**
- Judges: Günther, Hawthorne, Salow, Greco (legal justification and excuse), Weisberg, Dorr.
- Crowding: moderate. The topic is familiar and touches algorithmic fairness.

**Scores.** A 3 · T 4 · V 3 · C 3

## D. Ethics and value theory

### 15. Population axiology after the impossibility theorems

**Problem.**
- Impossibility theorems (Arrhenius and others) show that no population axiology satisfies all of a set of compelling adequacy conditions.
- Any theory must accept the Repugnant Conclusion, or the Very Repugnant Conclusion, or the Sadistic Conclusion, or reject transitivity, or reject some other principle.

**Why hard.**
- The SEP "The Repugnant Conclusion" (rev. 2017) [SEP] lists the escape routes and a standard objection to each:
  - averagism;
  - variable value;
  - critical levels;
  - superiority;
  - person-affecting views;
  - non-transitivity;
  - accepting the conclusion.
- It notes that the options "do not invite an easy choice".
- Zuber et al. (2021) argue that avoiding the Repugnant Conclusion should no longer be a necessary condition [abs: first lines only; treat as summary-level].
- Thornley (2021) extends impossibilities to prospect axiologies without Finite Fine-Grainedness [title].
- Hájek & Rabinowicz (2022) [full] offer degrees of commensurability.
- The lanes file rates the field "saturated with impossibility theorems".

**What an advance would look like.**
- A result that changes the dialectic rather than adding another impossibility. For example:
  - a characterisation theorem showing that the escape routes are equivalent under a translation;
  - or a proof that one adequacy condition is not independent of the others in the risky setting.

**Anchors.**
- Zuber et al. 2021, "What Should We Agree on about the Repugnant Conclusion?", *Utilitas* 33:379–383, doi 10.1017/s095382082100011x. VERIFIED. Fetch (likely OA).
- Spears & Budolfson 2021, "Repugnant Conclusions", *Social Choice and Welfare*, doi 10.1007/s00355-021-01321-2. VERIFIED. Fetch.
- Thornley 2021, "The Impossibility of a Satisfactory Population Prospect Axiology (Independently of Finite Fine-Grainedness)", *Phil Studies*, doi 10.1007/s11098-021-01621-4. VERIFIED. Fetch.
- Hájek & Rabinowicz 2022 (see problem 5). Local.

**Readers.**
- Judges: Nebel, Kowalczyk, Greaves, Tarsney, Easwaran [Thornley].
- Crowding: high, both from AI entrants and in the literature.

**Scores.** A 4 · T 2 · V 5 · C 2

### 16. Limited aggregation, especially under risk

**Problem.**
- Many hold that a single person's life outweighs any number of headaches, yet many minor-but-serious harms can outweigh one death.
- "Limited" or "partial" aggregation views try to honour both claims.
- Under risk they seem to break down: ex ante versions and ex post versions each face severe problems.

**Why hard.**
- Horton (2020, *Ethics*) gives a risk-based reductio of partially aggregative views and defends full aggregation. His abstract was seen via a search snippet only, so this is [summary].
- Tadros (2019) poses an objection that motivated alternative "weak aggregation" views [summary].
- Steuwer (2021) argues that ex post limited aggregation is "far away from being a well-defined alternative" [summary of abstract].
- Tomlin has shown that the Relevance View has implausible implications when people are added to or removed from the groups that can be saved [summary].
- Muñoz (2024; a calibration sample paper) diagnoses why the Taurek literature has seemed irresolvable [editors' summary].

**What an advance would look like.**
- An impossibility theorem in the style of social choice: no limited-aggregation view satisfies relevance-sensitivity, a weak ex ante Pareto principle and dynamic consistency.
- Or a minimal characterisation of the views that survive.

**Anchors.**
- Horton 2018, "Always Aggregate", *Phil & Public Affairs* 46:160–174, doi 10.1111/papa.12116. VERIFIED. Fetch.
- Horton 2020, "Aggregation, Risk, and Reductio", *Ethics*, doi 10.1086/708534. VERIFIED. OA (UCL Discovery): https://discovery-pp.ucl.ac.uk/10089021/1/Horton_708534.pdf (search hit, not opened).
- Lazar 2018, "Limited Aggregation and Risk", *Phil & Public Affairs*, doi 10.1111/papa.12115. VERIFIED. Fetch.
- Steuwer 2021 (online 2020), "Aggregation, Balancing, and Respect for the Claims of Individuals", *Utilitas*, doi 10.1017/s0953820820000217. VERIFIED. Fetch.

**Readers.**
- Judges: Nebel, Kowalczyk, Tarsney, Greaves.
- Crowding: low to moderate.

**Scores.** A 3 · T 4 · V 4 · C 4


### 17. Deontology under risk

**Problem.**
- Agent-centred constraints (do not kill the innocent) are stated for certainty.
- Under uncertainty, every act carries some risk of violating them.
- What does a constraint require when violation is merely probable? Candidate answers include thresholds, lexical or expectational representations, and ex ante versus ex post evaluation.

**Why hard.**
- The SEP "Moral Decision-Making Under Uncertainty" (Tarsney, Thomas & MacAskill 2024) [SEP, local `sep_moral_unc.txt`] sets out the main failures:
  - **Thresholds** look arbitrary and face an agglomeration problem (Jackson & Smith's Two Skiers): each shot is permissible but shooting both is not, or one bullet is forbidden where two are allowed.
  - **Patient-indexed thresholds** (Aboodi, Borer & Enoch) meet the same problem for repeated risks to one person. They also prefer spreading near-threshold risks over many people (Huemer).
  - **Lexical expected-utility representations** are "implausibly fanatical".
- Kowalczyk (2022) argues that ex ante deontology fails in sequential choice [abs per committee map].
- Lazar & Graham (2021) develop deontological decision theory for lesser-evil options [title].

**What an advance would look like.**
- A representation theorem: the risk-sensitive constraint theories satisfying agglomeration-invariance and a sequential-consistency condition are exactly those of form X. Or show that none exist.
- Or a dissolution showing that the agglomeration problem is an artefact of individuating acts by bullets rather than by plans.

**Anchors.**
- Kowalczyk 2022, "People in Suitcases", *J Moral Phil*, doi 10.1163/17455243-19030009. VERIFIED. Fetch.
- Lazar & Graham 2021 (online 2019), "Deontological Decision Theory and Lesser-Evil Options", *Synthese* 198:6889–6916, doi 10.1007/s11229-019-02496-z. VERIFIED (Crossref online-first year; cite the volume year). Fetch.
- Lazar 2018 (see problem 16). Fetch.
- Gustafsson & Kowalczyk 2026, "Ex Ante Pareto and the Opaque-Identity Puzzle", *J Phil*, doi 10.5840/jphil20251177. VERIFIED. Fetch.

**Readers.**
- Judges: Kowalczyk, Tarsney, Greaves, Nebel, Robinson.
- Crowding: low.

**Scores.** A 4 · T 4 · V 4 · C 4

### 18. Normative uncertainty: intertheoretic comparison and the regress

**Problem.**
- If one is uncertain which moral theory is true, how should one act?
- Expectational approaches need choiceworthiness to be comparable across theories that may share no scale.
- Every approach faces a regress, since one is also uncertain how to handle the uncertainty.

**Why hard.** The SEP entry above [SEP] reports:
- some (Gracely; Hedden) call intertheoretic comparison "insuperable";
- "common ground" approaches have limited scope;
- "universal scale" approaches face the doubt that rival theories share a scale;
- normalisation approaches either produce sequential dominance violations (range, per situation) or need an arbitrary measure over options (variance; Cotton-Barratt, MacAskill & Ord);
- ordinal theories need voting-style rules;
- Weatherson argues that the regress is fatal.

Tarsney (2024) [abs] proposes stopping the regress by giving "external force" to the enkratic principle. Greaves & Cotton-Barratt (2023) offer a bargaining approach [title]. Robinson (2022) models moral uncertainty for noncognitivists [abs].

**What an advance would look like.**
- An Arrow-style impossibility for aggregating moral theories under uncertainty, with independence and minimality.
- Or a proof that bargaining and normalisation coincide under stated conditions, which would collapse the menu.

**Anchors.**
- MacAskill, Bykvist & Ord 2020, *Moral Uncertainty*, OUP, doi 10.1093/oso/9780198722274.001.0001. VERIFIED. Availability unchecked (may be open access; confirm).
- Greaves & Cotton-Barratt 2023, "A Bargaining-Theoretic Approach to Moral Uncertainty", *J Moral Phil*, doi 10.1163/17455243-20233810. VERIFIED. Fetch.
- Tarsney 2024, "Metanormative Regress: An Escape Plan", *Phil Studies*, doi 10.1007/s11098-024-02114-w. VERIFIED. Fetch.
- Weatherson 2019, *Normative Externalism*, OUP, doi 10.1093/oso/9780199696536.001.0001. VERIFIED. Fetch.

**Readers.**
- Judges: Robinson, Tarsney, Greaves, Nebel.
- Crowding: moderate. The problem is known to AI systems through effective-altruism texts, and AI alignment uses moral uncertainty.

**Scores.** A 3 · T 3 · V 3 · C 3

### 19. The wrong kind of reasons and the partiality problem for fitting-attitude analyses

**Problem.**
- Fitting-attitude (buck-passing) theories analyse value as what it is fitting, or there is reason, to favour.
- Two problems remain unsolved:
  - incentives to value worthless things ("wrong kind of reasons");
  - partial preferences that seem fitting between equally good outcomes ("partiality").
- The profession is split on which normative concept is fundamental: value 37.4, reasons 25.4, ought 14.2, fit 7.3, other 24.5.

**Why hard.**
- The SEP "Fitting Attitude Theories of Value" (Howard 2023) [SEP] reviews four answers to the wrong-kind-of-reasons problem:
  - scepticism about wrong-kind reasons;
  - object-given versus state-given reasons, which is extensionally inadequate in both directions;
  - alethic views, which risk circularity;
  - fittingness-first.
- It says "none of these proposals has gained wide acceptance". Partiality "remains an outstanding and pressing issue". The wrong-kind-of-value reply question is "open".

**What an advance would look like.**
- A case that refutes the fittingness-first solution on its own terms.
- Or a formal result showing that no extensionally adequate criterion separating right-kind from wrong-kind reasons can be stated without presupposing value.
- Or a structural unification of partiality and the wrong kind of reasons that makes a testable difference.

**Anchors.**
- Rowland 2019, *The Normative and the Evaluative*, OUP, doi 10.1093/oso/9780198833611.001.0001. VERIFIED (main title; Crossref stores no subtitle). Fetch.
- Howard 2019, "The Fundamentality of Fit", *Oxford Studies in Metaethics* 14, doi 10.1093/oso/9780198841449.003.0010. VERIFIED. Fetch.

**Readers.**
- Judges: Nebel (reasons and rationality), Robinson, Greaves, and partly Tarsney. This is a weak bench: no panel member works centrally on fitting attitudes.
- Crowding: low.

**Scores.** A 3 · T 3 · V 2 · C 4

## E. Philosophy of language and logic

### 20. Probabilities of conditionals after triviality *(overlaps E3)*

**Problem.**
- Lewis-style triviality results show that the probability of a conditional cannot in general be the conditional probability, if conditionals express propositions and credences obey standard rules.
- Which assumption should go?

**Why hard.**
- The L6 map §5 lists twenty open items. Among them:
  - Gärdenfors's theorem has no consensus response (SEP);
  - informational semantics needs a non-classical credence theory (Santorio 2022);
  - Flattening lacks an intuitive semantics (Dorr & Mandelkern 2026: "we leave it as an open problem" [full]).
- Khoo & Mandelkern (2019) relate triviality to the gap between logical and natural languages [abs].

**What an advance would look like.**
- A machine-checked minimal-inconsistency map over a fixed list of principles (L6 pressure point 4).
- Or a characterisation of the sentences that get probability 1 in tree models (D&M fn. 37).

**Anchors.**
- Khoo & Mandelkern 2019, "Triviality Results and the Relationship between Logical and Natural Languages", *Mind* 128:485–526, doi 10.1093/mind/fzy006. VERIFIED. Fetch.
- Dorr & Mandelkern 2026, "Sequence and Consequence", *Philosophical Logic*, doi 10.16995/phil-log.27646. VERIFIED. Local: `inbox/sources/dorr-mandelkern-2026-sequence.txt`.
- Goldstein & Santorio 2021, "Probability for Epistemic Modalities", *Phil Imprint* 21(33). Registry: NOT_FOUND (no DOI). Manual check via journal page per L6 refs. OA: https://www.philosophersimprint.org/021033/.

**Readers.**
- Judges: Mandelkern, Goldstein, Fitelson, Dorr, Günther, Hawthorne, Easwaran.
- Crowding: very low, but E3 already covers this lane.

**Scores.** A 3 · T 4 · V 5 · C 5

### 21. The logic of epistemic modals and free choice *(overlaps the E3 lane)*

**Problem.**
- Two sets of data resist every classical treatment:
  - Wittgenstein sentences ("p and might not p" is incoherent, even embedded);
  - free choice ("you may A or B" implies "you may A and you may B").
- Rival frameworks (dynamic, bounded, orthologic, state-based, pragmatic) each give up a different classical law.

**Why hard.**
- Goldstein (2020) proves that free choice cannot be validated in a classical semantics (impossibility results) [title-level summary per committee map].
- Mandelkern (2019) [title] and Holliday & Mandelkern (2024) [L6 map] give rival non-dynamic logics.
- The L6 map records open items: Qualified Collapse; same-level modus ponens; how orthologic pairs with a free-choice account given Double Prohibition (L6 pressure point 9).

**What an advance would look like.**
- A discriminating datum or theorem that adjudicates between orthologic and bounded or dynamic accounts.
- Or a minimal impossibility over a fixed set of principles: free choice, ∨-introduction, Duality, distributivity, monotone ◇.

**Anchors.**
- Holliday & Mandelkern 2024, "The Orthologic of Epistemic Modals", *JPL* 53, doi 10.1007/s10992-024-09746-7. VERIFIED. Availability unchecked; fetch.
- Mandelkern 2019, "Bounded Modality", *Phil Review* 128, doi 10.1215/00318108-7213001. VERIFIED. Fetch.
- Goldstein 2020, "Free Choice Impossibility Results", *JPL*, doi 10.1007/s10992-019-09517-9. VERIFIED. Fetch.
- Aloni 2022, "Logic and Conversation: The Case of Free Choice", *Semantics & Pragmatics* 15, doi 10.3765/sp.15.5. VERIFIED. OA (journal).

**Readers.**
- Judges: Mandelkern, Goldstein, Dever, Hawthorne, Dorr, Cappelen, Sterken.
- Crowding: very low.

**Scores.** A 3 · T 4 · V 5 · C 5

### 22. Frege's puzzle, attitude reports and Millianism

**Problem.**
- If a name's meaning is its referent (Millianism), "Lois believes Superman flies" and "Lois believes Clark flies" should not differ in truth value. They seem to.
- Fregean senses, hidden indexicals, contextualism, and revisions of the logic of identity all have serious costs.
- The profession is split. Proper names: Millian 38.7, Fregean 36.1, other 25.5.

**Why hard.**
- Goodman & Lederman (2021) [abs] defend Millian contextualism with mid-sentence context shifts.
  - They prove tenability results under constraints.
  - Those constraints turn out to be incompatible with coarse-grained propositions and in tension with how speakers coordinate.
- Bacon & Russell (2019) [abs] treat Frege's puzzle as giving counterexamples to Leibniz's law. That forces a revision of the higher-order logic of identity.
- Unnsteinsson (2019) [abs] argues that the puzzle is about identity statements after all.
- Each solution moves the cost to logic, to context or to cognition.

**What an advance would look like.**
- A tenability or impossibility theorem: no semantics satisfies Millianism, a stated substitution-failure datum, a coordination constraint, and a fine-grainedness bound.
- Or a decisive case separating contextualist from logic-revising Millianism.

**Anchors.**
- Goodman & Lederman 2021 (online 2019), "Perspectivism", *Noûs* 55:623–648, doi 10.1111/nous.12322. VERIFIED (Crossref online-first year; cite the volume year). Fetch.
- Bacon & Russell 2019 (online 2017), "The Logic of Opacity", *PPR* 99:81–114, doi 10.1111/phpr.12454. VERIFIED (Crossref online-first year; cite the volume year). Fetch.
- Unnsteinsson 2019 (online 2018), "Frege's Puzzle Is About Identity After All", *PPR* 99:628–643, doi 10.1111/phpr.12516. VERIFIED. Fetch.

**Readers.**
- Judges: Dorr, Hawthorne, Dever, Cappelen (*The Inessential Indexical*), Mandelkern, Chalmers (two-dimensional semantics), Sterken.
- Crowding: low to moderate.

**Scores.** A 4 · T 3 · V 4 · C 4

### 23. Vagueness and higher-order vagueness

**Problem.**
- Sorites arguments drive the problem.
- Every theory either posits sharp but unknowable boundaries (epistemicism) or revises logic or semantics (supervaluationism, degree theories, tolerant logics).
- Higher-order vagueness then re-imposes the problem on the theory's own vocabulary.

**Why hard.**
- The SEP "Vagueness" (rev. 2022) [SEP] lists a standard objection to each theory:
  - epistemicism's "astonishing consequence" of sharp thresholds;
  - the hedging objection to degree theories;
  - supervaluationism's failures of conditional proof and reductio, and its conflict with Convention T;
  - contextualism's order effects.
- It notes that Fine's global account may be "incomplete or disjunctive".
- Chen (2022), a Philosopher's Annual winner, argues for fundamental nomic vagueness [calibration].

**What an advance would look like.**
- An impossibility showing that no theory meeting stated conditions handles all orders of vagueness, minimal and new relative to the known higher-order-vagueness paradoxes.
- Or a transfer from measurement theory or psychophysics that makes a theory predict a datum its rivals cannot.

**Anchors.**
- Bacon 2018, *Vagueness and Thought*, OUP, doi 10.1093/oso/9780198712060.001.0001. VERIFIED. Fetch.
- Fine 2020, *Vagueness: A Global Approach*, OUP, doi 10.1093/oso/9780197514955.001.0001. VERIFIED (Crossref main title "Vagueness"; subtitle per SEP bibliography). Fetch.
- Chen 2022, "Fundamental Nomic Vagueness", *Phil Review*, doi 10.1215/00318108-9415127. VERIFIED. Fetch.

**Readers.**
- Judges: Dorr, Hawthorne, Dever, Easwaran (logic), Chalmers.
- Crowding: moderate. The sorites is a classic AI topic.

**Scores.** A 4 · T 2 · V 3 · C 3

### 24. The liar paradox and revenge

**Problem.**
- Every consistent and expressively adequate theory of truth seems to face a strengthened liar built from its own new vocabulary ("not determinately true", "not normal", "invalid").
- This applies to paracomplete, paraconsistent, substructural (non-contractive, non-transitive/ST), classical-restrictionist and contextualist theories alike.
- The profession leans classical. Logic: classical 53.6, non-classical 26.4. "True contradictions impossible" stands at 71.4.

**Why hard.**
- The SEP "Liar Paradox" (rev. July 2026) [SEP, first 100k characters] shows revenge for each family:
  - paracomplete theories cannot say the Liar is not true;
  - paraconsistent theories must treat Curry separately and characterise "normal" sentences;
  - restrictionist theories meet diagonal sentences against determinateness.
- It calls the expressive success of non-classical approaches "a highly contentious issue".
- Murzi & Rossi (2020) argue for a generalised revenge argument [title only; cited by SEP].
- Barrio, Pailos & Szmuc (2020) build hierarchies of metainferential logics that bear on whether ST is classical [title].

**What an advance would look like.**
- A general theorem characterising exactly which expressive resources trigger revenge for any logic in a broad class (a "revenge theorem").
- Or a proof that a specific substructural approach escapes it.

**Anchors.**
- Murzi & Rossi 2020 (online 2019), "Generalized Revenge", *AJP* 98:153–177, doi 10.1080/00048402.2019.1640323. VERIFIED. Fetch.
- Barrio, Pailos & Szmuc 2020 (online 2019), "A Hierarchy of Classical and Paraconsistent Logics", *JPL* 49:93–120, doi 10.1007/s10992-019-09513-z. VERIFIED. Fetch.

**Readers.**
- Judges: Dorr, Hawthorne, Easwaran and Fitelson (logic), Dever. A thin specialist bench: no judge works centrally on truth theories.
- Crowding: high. The liar is among the paradoxes AI systems most often write on.

**Scores.** A 4 · T 3 · V 5 · C 2


## F. Metaphysics and philosophy of science

### 25. Cantorian limits on hyperintensional grain: structured propositions and ground

**Problem.**
- Fine-grained theories of propositions and facts say there is at least one distinct truth or proposition for each plurality of truths (or for each structure). Examples:
  - structured propositions (same proposition, same structure);
  - "immediate ground" principles (a conjunction is grounded in exactly its conjuncts).
- Russell–Myhill and Cantorian arguments show these requirements are inconsistent in higher-order logic.
- The open question is how fine-grained propositions, facts and grounds can be.

**Why hard.**
- Fritz, Lederman & Uzquiano (2021) [abs] restrict structure to propositions expressible by closed sentences ("Closed Structure"). They prove this consistent, then show it inconsistent once the language adds plural talk about propositions.
- Fritz (2022) [abs] proves that standard immediate-grounding principles for conjunction, disjunction and universal quantification "are jointly inconsistent" by a variant of Cantor's theorem. Grounding is thus either not in good standing or natural assumptions must be revised.
- Goodman & Lederman (2021) [abs] find their contextualist constraints incompatible with coarse-grained propositions. The grain question therefore also constrains the semantics of attitude reports (problem 22).
- The SEP "Metaphysical Grounding" (rev. 2021) [SEP] flags as open: meta-ground; whether ground is a strict order; necessitarianism.

**What an advance would look like.**
- A sharp boundary theorem characterising the maximal consistent grain, i.e. which restricted structure or ground principles are consistent in classical higher-order logic together with stated expressive extensions.
- Or a proof that some restriction strategy survives every natural extension.
- Or a reduction showing that the grounding and propositional paradoxes are one paradox.

**Anchors.**
- Fritz, Lederman & Uzquiano 2021, "Closed Structure", *JPL* 50:1249–1291, doi 10.1007/s10992-021-09598-5. VERIFIED. Availability unchecked; fetch.
- Fritz 2022 (online 2021), "Ground and Grain", *PPR* 105:299–330, doi 10.1111/phpr.12822. VERIFIED. Fetch.
- Fritz 2023, *The Foundations of Modality*, OUP, doi 10.1093/oso/9780192870025.001.0001. VERIFIED (main title). Fetch.
- Lovett 2020 (online 2019), "The Puzzles of Ground", *Phil Studies* 177:2541–2564, doi 10.1007/s11098-019-01325-w. VERIFIED. Fetch [title].

**Readers.**
- Judges: Dorr (higher-order identity; "Higher-Order Quantification and the Elimination of Abstract Objects" in progress), Hawthorne, Chalmers (*Constructing the World*); Easwaran for the set theory [Goodsell].
- Crowding: very low.
- Risk: a small, expert bench with very high standards.

**Scores.** A 4 · T 4 · V 5 · C 5

### 26. Actual causation

**Problem.**
- What makes one particular event a cause of another?
- Counterfactual and structural-equation accounts handle simple dependence. Each fails on some family of cases:
  - late or trumping preemption;
  - symmetric overdetermination;
  - double prevention and transitivity failures;
  - switches;
  - "isomorphs" that differ only in normality.
- They also make verdicts relative to the choice of model and variables.
- The profession is split. Causation: counterfactual 37.2, process 22.5, primitive 20.5.

**Why hard.**
- The SEP "Counterfactual Theories of Causation" (rev. 2024) [SEP] records which cases defeat Lewis 1973 and Lewis 2000, and how structural-equation accounts handle preemption.
- It flags as unsolved:
  - "It is hard to see … how there could be a univocal and reasonably well defined notion of 'normality'";
  - transitivity "is not easily settled";
  - aptness of models "is a matter of ongoing philosophical debate".
- Gallow (2021), a Philosopher's Annual winner, gives a model-invariant theory [calibration].
- Andreas & Günther (2021) analyse causation via a strengthened Ramsey test [author's summary per committee map].
- Beckers (2021) gives a counterfactual NESS definition [title].

**What an advance would look like.**
- An impossibility result: no model-invariant account satisfies a stated set of verdicts on canonical cases together with a structural condition such as invariance under adding irrelevant variables.
- Or a new discriminating case on which the strongest current accounts (model-invariant, Ramsey-test, NESS) diverge, with the verdict defended.

**Anchors.**
- Gallow 2021, "A Model-Invariant Theory of Causation", *Phil Review* 130:45–96, doi 10.1215/00318108-8699682. VERIFIED. Fetch.
- Andreas & Günther 2021, "A Ramsey Test Analysis of Causation for Causal Models", *BJPS* 72, doi 10.1093/bjps/axy074. VERIFIED (L6). Fetch.
- Beckers 2021, "The Counterfactual NESS Definition of Causation", *Proc. AAAI* 35, doi 10.1609/aaai.v35i7.16772. VERIFIED. Availability unchecked (proceedings may be open; confirm).
- Andreas & Günther 2024, "A Regularity Theory of Causation", *Pacific Phil Q*, doi 10.1111/papq.12447. VERIFIED. Fetch.

**Readers.**
- Judges: Günther, Jaeger, Dorr, Hawthorne, Fitelson [Goodsell, "Tossing Morgenbesser's Coin"].
- Crowding: low.
- Caution: Günther co-authors one of the leading accounts (§1.6).

**Scores.** A 4 · T 3 · V 4 · C 4

## G. Philosophy of mind and AI

### 27. The meta-problem of consciousness

**Problem.**
- Why do we judge that consciousness poses a hard problem? Chalmers calls these judgements "problem intuitions".
- Can this be explained in topic-neutral (functional) terms?
- What follows for realism about phenomenal consciousness, either way?

**Why hard.**
- Chalmers (2018) [full, retrieved PDF] says that for the hard problem "there are no solutions that command any sort of consensus".
- He frames the meta-problem as explaining problem intuitions (explanatory, metaphysical, knowledge and modal) in topic-neutral terms.
- He surveys non-reductionist and reductionist reactions, including "meta-problem nihilism" ("there is no solution to the meta-problem") and illusionism.
- A solution to the meta-problem seems either to debunk the intuitions or to leave the original problem untouched. No one has shown which.
- Kammerer (2021) defends illusionism [title].
- Survey: consciousness splits functionalism 33.0, dualism 22.0, identity 13.3, panpsychism 7.5, other 22.7. Zombies: conceivable but not possible 36.5, possible 24.4.

**What an advance would look like.**
- A dilemma made rigorous: any topic-neutral explanation of problem intuitions either (a) debunks them or (b) entails a stated non-physical posit, with the epistemic principle linking them defended.
- Or a decisive case separating illusionist from realist predictions about the reports of artificial systems.

**Anchors.**
- Chalmers 2018, "The Meta-Problem of Consciousness", *JCS* 25(9–10):6–61. VERIFIED, with manual correction recorded in the committee bibliography. OA: https://consc.net/papers/metaproblem.pdf (retrieved this session).
- Kammerer 2021 (online 2019), "The Illusion of Conscious Experience", *Synthese* 198:845–866, doi 10.1007/s11229-018-02071-y. VERIFIED (Crossref online-first year; cite the volume year). Fetch.

**Readers.**
- Judges: Chalmers, Shevlin, Millière, Vold, Goldstein.
- Crowding: very high. This sits next to AI consciousness, the most crowded area by the panel analysis.

**Scores.** A 5 · T 2 · V 2 · C 1

### 28. Belief attribution to language models (what would make an internal state a belief?)

**Problem.**
- Do LLMs have beliefs?
- If they do, what conditions must an internal representation meet to be a belief?
- How could probing or interpretability methods detect it?
- Interpretationist, representationalist and dispositionalist answers diverge, and the empirical "lie detector" literature lacks agreed standards.

**Why hard.**
- Herrmann & Levinstein (2025) [abs via search] note the lack of a "unified theoretical foundation". They propose four adequacy conditions: accuracy, coherence, uniformity and use.
- Levinstein & Herrmann (2024) document empirical and conceptual roadblocks for probing [title].
- Chalmers (2025) makes propositional interpretability, including "thought logging", a central challenge [abs per committee map].
- Cappelen & Dever (2025) defend full cognitive agency for sophisticated LLMs [calibration summary].

**What an advance would look like.**
- An impossibility showing that no probe-based criterion meets all four adequacy conditions for systems with a stated property.
- Or a decisive case where interpretationist and representationalist criteria give opposite verdicts on a constructed model.

**Anchors.**
- Herrmann & Levinstein 2025 (online 2024), "Standards for Belief Representations in LLMs", *Minds and Machines* 35, doi 10.1007/s11023-024-09709-6. VERIFIED. OA: https://arxiv.org/abs/2405.21030.
- Levinstein & Herrmann 2024, "Still No Lie Detector for Language Models", *Phil Studies* 182:1539–1565, doi 10.1007/s11098-023-02094-3. VERIFIED. Fetch.
- Chalmers 2025, "Propositional Interpretability in Artificial Intelligence", arXiv:2501.15740. Registry: NOT_FOUND (preprint); manual check via arXiv per committee map. OA.

**Readers.**
- Judges: Chalmers, Cappelen, Dever, Millière, Mandelkern, Goldstein, Shevlin, Vold, Sterken.
- Crowding: very high (the second most crowded area). The 2025–26 literature is moving fast.

**Scores.** A 4 · T 2 · V 2 · C 1

### 29. The shutdown problem (corrigibility) as a problem in decision theory

**Problem.**
- Can an artificial agent be designed to do three things at once?
  - shut down when the button is pressed;
  - neither try to prevent nor try to cause the pressing;
  - otherwise pursue its goals competently.
- Which decision-theoretic properties, such as incomplete preferences, stochastic choice or shutdown-seeking goals, make this possible?

**Why hard.**
- Thornley (2024) [full arXiv, local] proves three theorems. Agents satisfying "innocuous-seeming conditions" will often try to prevent or cause the pressing, even at a cost.
- Goldstein & Robinson (2024) [abs] propose shutdown-seeking AIs.
- Neth (2025) [full, local] gives two reasons why the off-switch game's deference guarantee fails: agents may not value learning, and may not be certain to learn human preferences.
- Proposals that use incomplete preferences inherit problem 5's dominance and money-pump pressures.

**What an advance would look like.**
- A tight impossibility theorem with minimal conditions.
- Or a construction satisfying all three desiderata under explicitly weaker conditions, with a proof that every condition is needed.
- Or a demonstration that the problem is an instance of a known result in sequential choice (a transfer).

**Anchors.**
- Thornley 2024, "The Shutdown Problem: An AI Engineering Puzzle for Decision Theorists", *Phil Studies* 182:1653–1680, doi 10.1007/s11098-024-02153-3. VERIFIED. Local: `shutprob.txt`.
- Goldstein & Robinson 2024, "Shutdown-Seeking AI", *Phil Studies* 182:1567–1579, doi 10.1007/s11098-024-02099-6. VERIFIED. Fetch.
- Neth 2025, "Off-Switching Not Guaranteed", *Phil Studies* 182:1919–1931, doi 10.1007/s11098-025-02296-x. VERIFIED. Local: `neth.txt`.
- Thornley et al. 2025, "Towards Shutdownable Agents via Stochastic Choice", *TMLR*. Registry NOT_FOUND (no DOI); manual check: published-version header in the local text. Local: `drest1.txt`.

**Readers.**
- Judges: Goldstein, Robinson, Tarsney, Hawthorne, Cappelen, Dever, Millière, Vold, Nebel, Easwaran [Thornley].
- Crowding: moderate. The formal strand is less crowded than discursive alignment ethics.
- Caution: this is an organiser's research programme, so attribution needs extra care.

**Scores.** A 3 · T 4 · V 5 · C 3

### 30. Impossibility theorems for algorithmic fairness

**Problem.**
- Statistical fairness criteria (calibration within groups, equal false-positive and false-negative rates, and others) cannot all be met unless base rates are equal or prediction is perfect.
- Which criteria, if any, are genuinely required by fairness? What should a predictor do when they conflict?

**Why hard.**
- Hedden (2021) [summary via search] argues that every criterion except calibration can be violated simultaneously by a manifestly fair, uniquely optimal predictor, even with equal base rates. He concludes that only calibration is a necessary condition.
- A 2024 preprint (Hu, arXiv 2412.16769; not verified for this dossier) presses a reference-class problem against calibration.
- Beigang (2023) seeks to reconcile the criteria [title].
- Eva (2022) proposes base-rate tracking [title].

**What an advance would look like.**
- A sharper impossibility using criteria each defended in print, with independence shown.
- Or a characterisation of the predictors that satisfy a defensible subset.
- Or a proof that calibration itself is reference-class relative in a way that undermines Hedden's case.

**Anchors.**
- Hedden 2021, "On Statistical Criteria of Algorithmic Fairness", *Phil & Public Affairs* 49:209–231, doi 10.1111/papa.12189. VERIFIED. OA record on PhilArchive (search hit; 403 likely); fetch.
- Beigang 2023, "Reconciling Algorithmic Fairness Criteria", *Phil & Public Affairs* 51:166–190, doi 10.1111/papa.12233. VERIFIED. Fetch.
- Eva 2022, "Algorithmic Fairness and Base Rate Tracking", *Phil & Public Affairs* 50:239–266, doi 10.1111/papa.12211. VERIFIED. Fetch.

**Readers.**
- Judges: Günther (algorithmic decision-making and legal proof), Fitelson, Weisberg, Easwaran, Vold, Robinson. A thin bench.
- Crowding: moderate to high. AI fairness is a natural topic for AI entrants.

**Scores.** A 3 · T 4 · V 4 · C 2


---

## Ranked shortlist: top 10 by ambition × tractability

**Ranking rule.**
1. Rank by A×T.
2. Break ties by V + C.
3. Exclude problems already covered by drafts E1–E3 (12, 20, 21).
4. Admit at most three problems from the decision-theory/formal-ethics cluster (1–6, 15–18, 29), so the list stays diverse.

| Rank | # | Problem | A×T | V+C | Area | Why |
|---|---|---|---|---|---|---|
| 1 | 4 | Infinite ethics: Pareto vs dominance | 16 | 9 | formal ethics | A recent paper calls every known consistent response "quite radical", so a minimal impossibility or a characterisation of what survives would change the field. It is provable and has a deep bench (Nebel, Kowalczyk, Easwaran, Tarsney, Greaves). |
| 2 | 25 | Cantorian limits on grain (structured propositions, ground) | 16 | 10 | metaphysics / logic | Two 2021–22 inconsistency results leave the maximal consistent grain uncharacterised. A boundary theorem would bind every theorist of propositions, ground and attitude reports, and it can be checked by proof. |
| 3 | 5 | Completeness and incomparability | 16 | 9 | decision theory / value | Several independent arguments against incompleteness (dominance, money pump, semantic) invite a diagnosis of their shared premise. The stakes reach population ethics, fanaticism and AI shutdown proposals. |
| 4 | 17 | Deontology under risk | 16 | 8 | normative ethics | The agglomeration problem for risk thresholds has no accepted solution. A representation theorem or dissolution would interest ethicists and decision theorists, and the area is uncrowded. |
| 5 | 13 | Value of evidence and dogmatism | 12 | 10 | epistemology | There is no Good-style theorem for knowledge-first decision rules in normality models. Finite models make claims checkable, and several judges have flagged the question as open. |
| 6 | 8 | Belief–credence bridge | 12 | 8 | formal epistemology | The profession splits into four near-equal camps. A minimal impossibility over closure, threshold-monotonicity and partition-invariance would be legible to the whole committee. |
| 7 | 22 | Frege's puzzle and Millianism | 12 | 8 | philosophy of language | The names question is split 39/36/26, and a tenability or impossibility theorem (in the style of Goodman & Lederman) can settle part of it. Several metaphysics and language judges would recognise it. |
| 8 | 26 | Actual causation | 12 | 8 | metaphysics / philosophy of science | The causation question is split, and the SEP flags normality and aptness as unsolved. A discriminating case among the best current accounts can be checked against explicit causal models. |
| 9 | 7 | Self-locating belief | 12 | 7 | formal epistemology | Sleeping Beauty has the survey's largest "other" share (53.4%). The multi-successor scoring and measure problems are flagged as open, so a propriety theorem would read as significant. |
| 10 | 11 | Higher-order evidence and akrasia | 12 | 7 | epistemology | This core epistemology problem has explicit formal structure (bridge principles over evidence models), and a minimal inconsistency map has not, as far as this dossier found, been given. |

Problems with A×T = 12 that were excluded:
- By the cluster cap: 1 (Newcomb), 2 (fanaticism), 3 (unbounded utility), 6 (cluelessness), 16 (limited aggregation), 29 (shutdown).
- By V+C: 14 (statistical evidence), 24 (liar), 30 (fairness).
- 3 and 29 would be the next substitutes if a decision-theory slot opens.

**Area coverage of the top 10.**
- Formal ethics and decision theory: 4, 5, 17.
- Metaphysics and logic: 25, 26.
- Epistemology: 13, 11.
- Formal epistemology: 8, 7.
- Philosophy of language: 22.

**Not represented.**
- Philosophy of mind and AI (27, 28, 29). Their tractability or crowding scores are poor, except the shutdown problem, which is excluded by the cluster cap.
- Philosophy of science proper (9, 10). Both have low tractability.
- Metaethics (19). Weak panel bench.

**For the final three essays (one prize per entrant), draw from different blocks.** For example:
- one of {4, 5, 17};
- one of {25, 22, 26};
- one of {13, 8, 7, 11}.

Two caveats:
- 25 and 22 interact through Goodman & Lederman's grain result. Choosing both risks one area.
- 13 and 11 sit next to E1's lane (L3). The existing drafts E1–E3 already occupy epistemology, Bayesian updating and conditionals. If any of them remains a candidate, the ambitious picks should come from formal ethics or decision theory and from metaphysics or language.

## What I could not verify, and other caveats

- **Abstracts and full texts.** Many "why hard" points rest on abstracts or SEP summaries, not full texts. Each is tagged.
- **[title]-tagged works.** Nothing about their content may be attributed in a draft until the text is read: Lasonen-Aarnio 2020, Christensen 2021, Smith 2018, Russell & Isaacs 2021, Kammerer 2021, Beigang 2023, Eva 2022, Lovett 2020, Murzi & Rossi 2020, Barrio et al. 2020, Beckers 2021, Levinstein & Herrmann 2024, Howard 2019, Rowland 2019, Tarsney 2023.
- **Search-snippet sources.** Horton 2020, Steuwer 2021, Tomlin and Hedden 2021 are summarised from search-result snippets only [summary]. Treat them as weak until read.
- **The SEP "Liar Paradox" entry** was read only to 100k of 148k characters. Its sections on revision theory, inconsistency views and contextualism (from §4.4.3 on) were not read.
- **The SEP "Structured Propositions" entry** does not explain Russell–Myhill. The statement in problem 25 rests on the Fritz, Lederman & Uzquiano and Fritz abstracts.
- **Survey figures** are whole-population (2020). Specialist breakdowns are unread (fetch request already filed by the field-surveyor).
- **Ross 2021** ("Rehabilitating Statistical Evidence", cited by the SEP) could not be pinned to its journal record. Crossref returned only an OSF preprint, so it is not used as an anchor.
- **Availability** marked "fetch" was not checked for open copies. PhilArchive returns 403.
- **Not verified for this dossier:** Schurz 2019 (*Hume's Problem Solved*) and Chalmers 2020 ("Is the Hard Problem of Consciousness Universal?"). Registry lookups failed, so neither is used as an anchor.
