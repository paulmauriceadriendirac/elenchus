# L5 map — Credence, updating and self-location

Mapper L5, 2026-10-21. Keys in `[brackets]` are entries in `state/lanes/L5/refs.json` (registry check in
`refs.verification.json`). The level of reading for each work is in §9. Where I report a work only through
a secondary source, I name that source. **[inference]** marks my own claims. No full text by a panel
member was read except Eva–Shear–Fitelson 2022, Easwaran–Nielsen 2025, Isaacs–Hawthorne–Russell 2022 and
Pettigrew–Weisberg 2025, so readership claims stay at abstract level unless stated otherwise.

## 1. Scope and central questions

1. **Accuracy foundations.** Suppose inaccuracy is measured by continuous (often additive) strictly proper
   scoring rules. Which credal norms follow: Probabilism, plan Conditionalization, Reflection, chance–credence
   principles? Do the arguments survive act–state dependence, comparisons across agendas, infinite domains,
   imprecision and risk-sensitive decision rules?
2. **Conditionalization and its rivals.** What is the right update when evidence is (a) certain, factive
   and partitional; (b) uncertain (Jeffrey); (c) non-partitional or non-transparent (externalism); (d)
   self-locating; (e) subject to forgetting? Is the norm about acts, plans or dispositions, and is it an
   ideal norm or a fallback norm?
3. **Supposition.** Which revision rules model indicative and subjunctive supposition, full and partial
   (conditionalization or Jeffrey conditionalization against imaging or Jeffrey imaging), and how do they
   relate to qualitative revision (AGM) and update (KM)?
4. **Deference and Reflection.** When should Cr(A | expert's credence in A = x) = x? What survives once the
   expert, one's future self or chance is *modest*, that is, uncertain of its own credences?
5. **Pooling.** How should credences be aggregated, or revised on a peer's credence? Which rules
   (linear, geometric, multiplicative "upco") satisfy which desiderata, such as external Bayesianity,
   commutativity, Bayes-compatibility or accuracy?
6. **Regularity and measure zero.** Must contingent propositions get positive credence? How should one
   condition on null events (the Borel–Kolmogorov paradox, Kolmogorov conditionalization)? Can
   non-measurable propositions get any credence at all?
7. **Self-location.** What are the objects of self-locating credence? How should such credences be updated
   (shifted or compartmentalized conditionalization, self-indication, self-sampling)? What credence should
   Sleeping Beauty have in Heads? What follows for fine-tuning, Doomsday, Everett and fission? In the 2020
   PhilPapers survey 27.7% chose 1/3, 18.6% chose 1/2 and **53.4% chose "other"** (n≈430;
   [BourgetChalmers2023] via the calibration brief).

## 2. Positions and their best arguments

**Accuracy-first ("veritist") Bayesianism.** Credences aim at accuracy, and norms are derived as
dominance or expected-accuracy optimality ([Joyce1998]; [Pettigrew2016]; [Pettigrew2023SEP]).
*Best argument:* the dominance theorems (§3, R1–R3). *Rival frameworks:* Dutch books, both synchronic and
diachronic ([Rescorla2022]; [Pettigrew2023Bayesian]); representation theorems; and pluralism about
epistemic value ([LewisFallisFitelson2024] argue that "counterexamples to the standard scoring rules are
ubiquitous in the history of science", so monism about epistemic value fails).

**Conditionalization orthodoxy versus externalist revisions.** Schoenfield showed that with non-partitional
evidence the expected-accuracy-optimal available plan conditions on *the fact that one received* E, not
on E ([Schoenfield2017], via [Pettigrew2023SEP] and Pettigrew's 2025 blog). Gallow argues that under
externalism conditionalization and Reflection are inconsistent, and proposes a new rule backed by an
expected-accuracy argument ([Gallow2021], abstract). Isaacs and Russell extend the planning justification
to agents whose beliefs do not discriminate perfectly; there, accuracy may recommend no conditionalization
at all ([IsaacsRussell2023], abstract). Meehan and Zhang defend conditionalization: among "globally
evidentially constant" rules it maximizes *total* expected accuracy across learning situations, including
non-transparent ones ([MeehanZhang2025], abstract). Das argues that accuracy and Dutch-book vindications of
updating plans are in tension with evidence externalism ([Das2019UrPrior]; [Das2022]).

**Time-slice and evidentialist views versus diachronic norms.** On time-slice views present credence
answers only to present evidence ([Hedden2015]; [Moss2015], title-level). Schwarz rejects the evidentialist
doctrine: when evidence deteriorates, conservatism, expected accuracy, Dutch books and anti-manipulation
considerations favour keeping the earlier beliefs ([Schwarz2025Disproportionate], read).

**Self-location: three families** (taxonomy of [IsaacsHawthorneRussell2022], read).
*Compartmentalized conditionalization* treats self-locating evidence "I am F" as the qualitative
"someone is F" (Halpern; [Meacham2008]; [Builes2020TimeSlice]). *Self-Indication* weights worlds by their
number of live centres; [Adelstein2024] defends it on the ground that every alternative must accept the
Doomsday argument. *Self-Sampling* weights worlds by the proportion of their
centres that are live. Titelbaum's CLF licenses compartmentalized updating only when each world has at most
one live centre (IHR fn.23 quoting [Titelbaum2013Quitting]).

**Sleeping Beauty camps.**
- *Thirders:* [Elga2000]; [Dorr2002]; [Titelbaum2008], who derives 1/3 from a revised conditionalization
  rule plus a principle relating modelling languages; direct-inference arguments ([Draper2019]
  per Springer abstract; [Horgan2019]); [Kim2022Centered], from Pettigrew's chance principle ETP.
- *Lewisian halfers* ([Lewis2001]): 1/2 on waking, 2/3 on learning that it is Monday.
- *Double halfers* (Bostrom 2007; [Meacham2008]): 1/2 throughout.
- *Steadfast halfers* ([Hawley2013]): rejects the claim, needed by "the best arguments" for 1/3, that on
  Monday Beauty should be uncertain what day it is (Schwarz classes this as steadfast halfing).
- *Dissolvers:* the verdict depends on modelling assumptions ([CisewskiEtAl2016]); on total versus
  average accuracy ([KierlandMonton2005]); on what Beauty's evidence is ([Russell2023], whose answer, per a search summary, is that
  it depends); pure self-locating credences have no rationally compelling values ([Adlam2024],
  preprint).
- *The newest halfer position* ([Schwarz2025SB], read): Beauty's *evidence* supports Heads to degree 1/3,
  but the expected-accuracy-optimal update, a fallback norm because she may lose information, yields
  Lewisian halfing. The split traces to whether rationality is "proportioning one's beliefs to the present
  evidence".

**Deference.** Reflection ([vanFraassen1984]) and its qualified forms ([Briggs2009]: obey Reflection only if
certain of conditionalizing on veridical evidence). Rational Reflection and New Rational Reflection
([Christensen2010]; [Elga2013]). *Trust* ([Dorst2020]; [Levinstein2023]). *Total Trust*: to defer is to
prefer to make any decision with the expert's credences ([DorstEtAl2021]).

**Pooling.** Linear pooling has accuracy arguments ([Pettigrew2019Group]; Moss 2011 per SEP). Geometric
pooling follows from "Groupthink"-style group Bayesianity ([RussellHawthorneBuchak2015], per
[Dietrich2019]) and from Bayes-compatibility ([BaccelliStewart2023]). Upco (multiplicative pooling) follows
from evidence-adding ([PettigrewWeisberg2024]) and from commutativity with Jeffrey conditionalization
([PettigrewWeisberg2025]).

**Regularity.** Defenders: infinitesimals (Lewis 1980, Skyrms 1980 per [Easwaran2014];
[BenciHorstenWenmackers2018]). Critics: [Easwaran2014] ("numerical fallacy"; hyperreals draw too many
distinctions); Williamson's coin ([Williamson2007]); [Hajek2012]; Pruss's rotation and Banach–Tarski
results (titles). Comparative regularity survives in [Hajek2003] (per [Lin2022SEP]) and gets a "weak
qualitative, epistemic" argument in [DiBella2022].

## 3. Landmark results

- **R1. Accuracy dominance for Probabilism** (de Finetti, Savage, [Predd2009]; [Pettigrew2022Additivity]
  dropped additivity; [Nielsen2022Best] corrected the proof). If inaccuracy is continuous and strictly
  proper, every non-probabilistic credence function on a finite agenda is strongly dominated by a
  probabilistic one, and no probabilistic function is even weakly dominated (statement per
  [Pettigrew2023SEP]). Infinite extensions: [Nielsen2023]; [Kelley2026] ("scorable contexts").
- **R2. Greaves–Wallace expectation theorem** ([GreavesWallace2006]). Assume strict propriety and
  factive evidence from a known partition. Then among *available* plans (same output wherever the
  evidence is the same) the expected-accuracy maximizers are exactly the conditionalizing plans.
  Extensions: infinite case, plus conglomerability and Reflection ([Easwaran2013]); non-partitional and
  infinite at once ([EaswaranNielsen2025]).
- **R3. Briggs–Pettigrew dominance for wide-scope plan conditionalization** ([BriggsPettigrew2020];
  [Nielsen2021]). With additive, continuous, strictly proper measures, a prior together with a
  non-conditionalizing plan is dominated in summed accuracy by some alternative prior–plan pair.
  [Pettigrew2023Bayesian] gives the non-factive analogue: dominance for *Weak General Reflection*, the
  requirement that the prior be a mixture of the possible posteriors. This answers Rescorla's point that
  the standard arguments assume that what becomes certain is true.
- **R4. Schoenfield's theorem** ([Schoenfield2017]). For an arbitrary evidence function E, define
  E*(ω) = {ω′ : E(ω′) = E(ω)}. The available plans that maximize expected accuracy are those that
  conditionalize on E*, not on E.
- **R5. Meehan–Zhang** ([MeehanZhang2025]; reconstruction by Pettigrew). For a regular prior, the
  conditionalizing *global* rule uniquely maximizes total expected accuracy, summed over all factive
  evidence functions, among rules satisfying global evidential constancy: E(ω) = E′(ω′) implies the
  same posterior. Pettigrew notes the result fails if non-factive evidence functions are included, and
  that it presupposes equal weight on each evidence function.
- **R6. Jeffrey conditionalization and accuracy.** Leitgeb and Pettigrew show that Jeffrey
  conditionalization violates their Accuracy norm unless Rigidity is assumed ([LeitgebPettigrew2010]).
  No additive strictly proper rule yields Jeffrey's rule by their method (Pettigrew 2021, Thm 12, per
  SEP).
- **R7. Risk-sensitive updating** ([CampbellMooreSalow2022], per SEP). Under Buchak-style risk-weighted
  expected utility, the Greaves–Wallace analogue yields a rule other than plan conditionalization,
  while the Leitgeb–Pettigrew analogue yields conditionalization. Risk-sensitive agents can be
  epistemically required *not* to gather free evidence ([CampbellMooreSalow2020]).
- **R8. Deference characterisations.** Total Trust in an expert is equivalent to always expecting the
  expert's estimates to be more accurate than one's own. It lies strictly between Reflection, which
  "collapse[s] to inconsistency" for modest experts, and New Reflection, which permits deference to an
  anti-expert ([DorstEtAl2021], abstract). A rational agent obeys Trust toward chance iff she expects
  chance to be at least as accurate as herself on every good accuracy measure. Trust entails the New
  Principle but is not entailed by it ([Levinstein2023], abstract).
- **R9. Pooling.**
  - Russell–Hawthorne–Buchak, as restated by [Dietrich2019]: requiring group credences to revise by Bayes
    on public representable information forces geometric-type pooling. Standard averaging is never
    permitted for any of Dietrich's six kinds of group Bayesianity.
  - [BaccelliStewart2023]: with a common prior, linear pooling cannot be non-trivially Bayes-compatible,
    whereas geometric pooling can, and under stated assumptions the two notions coincide.
  - [PettigrewWeisberg2025], read: Field's theorem says upco makes "Jeffrey pooling" commute. Conversely,
    upco is the only pooling rule that is monotone, uniformity-preserving, continuous and symmetric *and*
    makes Jeffrey pooling order-independent. Linear, geometric and harmonic pooling all fail.
- **R10. Imprecision has no strictly proper scores.** Results by Seidenfeld–Schervish–Kadane (2012),
  Schoenfield (2017) and Mayo-Wilson–Wheeler (2016), per SEP. Given Extension, Boundedness and
  Probabilistic Admissibility, every imprecise set has a precise probability function with equal
  epistemic utility at every world.
- **R11. Self-locating multiverse theorems** ([IsaacsHawthorneRussell2022], read). Assume a separable
  prior (universes' intrinsic profiles i.i.d.), *Locality* (intrinsic duplicate universes are evidentially
  equivalent), an *evidential* posterior (no world confirmed relative to an evidentially equivalent world),
  and *Agents*. Thm 1: for every multiverse size 1 < n < 1/p, where p is the fine-tuning parameter, "there
  are n universes" is confirmed relative to "there is just one universe". Thm 2 adds an *ordinary*
  posterior and drops the size bound. The three named rules all agree that fine-tuned life confirms a
  multiverse.
- **R12. Kolmogorov conditionalization.** [Rescorla2018] proves Dutch book and converse Dutch book
  theorems for Kolmogorov conditionalization. [MeehanZhang2022] show that Kolmogorov conditionalizers can
  plan to give their evidence posterior credence 0. They propose Kolmogorov–Blackwell conditionalization,
  which is Dutch-bookable iff the agent is evidentially uncertain.
- **Canonical cases:**
  - Self-location: Perry's messy shopper; Lewis's two gods; Lingens.
  - Sleeping Beauty and its variants: Technicolor Beauty; Beauty the High Roller; Informed SB.
  - Weintraub's three-person red/green case: seeing red is 2:1 evidence for Tails, yet "someone sees red"
    is evidence for neither hypothesis (IHR).
  - Dr. Evil ([Elga2004]); Fissioning Fred (Schwarz, after P. Lewis 2007); Hacking's inverse gambler;
    Talbott's spaghetti dinner (against Reflection).
  - Measure zero and imprecision: the uniform coin-bias case; Builes's infinite coins; non-measurable
    spinner regions.

## 4. The frontier (2019–2026)

**(a) Sleeping Beauty after twenty years.** Schwarz recasts the dispute as ideal versus non-ideal
diachronic norms against evidentialism ([Schwarz2025SB]; [Schwarz2025Disproportionate]). He argues four
things. (i) Shifted conditionalization alone yields "steadfast halfing", with Beauty certain that it is
Monday. (ii) A *doxastic-fission rule* treats every instance of the output credence equally. (iii)
Fission successors should be *averaged*, not summed. Summing yields thirding, but also predictable
confirmation of Everett-style fission hypotheses and an epistemic "repugnant conclusion". (iv) An
"anti-luck" limit on how far norms can depend on the state of the world. Together these give Lewisian
halfing. He concedes that Beauty's evidence supports 1/3, and he offers a new sure-loss construction
against thirders (after Halpern). Accuracy-based work continues: [Kim2022Dominance] argues that halfing is
average-accuracy dominated and that standard halfing and thirding both fail on total accuracy. On the
anti-halfer side, Button, Rothschild and Spectre argue from an "epistemological sure-thing principle"
([ButtonRothschildSpectre], summary only). [Pust2023] replies to [Titelbaum2012]. On the betting side,
[Conitzer2015Dutch] gives a Dutch book against EDT Beauties whether halfer or thirder, and
[Conitzer2015Devastating] argues that the Halfer Rule violates Reflection egregiously. Nobody has yet
replied in print to Schwarz 2025 as far as I could find; Crossref shows 1 citation.

**(b) Self-locating priors and big worlds.**
- [IsaacsHawthorneRussell2022] shift the fine-tuning debate from duelling analogies to theorems. A
  critique is announced by Meacham ("Fine-Tuning, Multiple Universes, and Self-Locating Beliefs",
  forthcoming in a Blackwell companion). I saw only the title and a search snippet: he reportedly says the
  first argument ignores some natural approaches and the second rests on a premise he rejects.
- [Builes2024Center] disambiguates centre indifference. He argues that its application depends on
  background metaphysics: Eternalism threatens external-world scepticism, and Modal Realism threatens
  inductive scepticism.
- [Adelstein2024] defends the self-indication assumption (SIA). [Adlam2024] denies that pure
  self-locating credences are rationally constrained.
- [Jager2021Immortal] (panel) argues that thirding implies that "Immortal Beauty" should be confident of
  reincarnation, and criticises Huemer's argument (search summary only).
- [Mahtani2024] argues that credence claims are opaque. On Bovens's reading, she holds that in Sleeping
  Beauty one should not defer to a trusted person under a designation that person does not self-identify
  under, so a more complex Reflection principle is needed ([Bovens2024]).

**(c) Updating with imperfect evidence.** The line runs from Schoenfield (2017) to Gallow (2021),
Isaacs–Russell (2023) and Carr's "A Modesty Proposal" (2021). Meehan–Zhang (2025) is the
pro-conditionalization riposte; Pettigrew's blog presents it as reducing the dispute to which update
mechanisms are *available*. [EaswaranNielsen2025] unify the infinite and non-partitional
generalisations. Their "signals" may be experiential types that the agent cannot express propositionally,
and the non-partitional setting partly resolves the Borel–Kolmogorov paradox.

**(d) Deference.** Trust and Total Trust are now the reference principles ([Dorst2020]; [DorstEtAl2021];
[Levinstein2023]). [HeddenDorst2022] argue that "(almost) all evidence is higher-order evidence".
[DziuroszSerafinowicz2023] proves that Adams conditionalization cannot preserve standard expert deference.
He proposes treating an expert's credence as a constraint on the posterior rather than on the prior.

**(e) Pooling.** Upco is ascendant: Easwaran et al. 2016; [PettigrewWeisberg2024]; [PettigrewWeisberg2025];
Pettigrew & Weisberg's "Geometric Pooling: A User's Guide" (BJPS 2026, title only). Pettigrew and Weisberg
(2024) also use upco against the social argument for Uniqueness.

**(f) Supposition.** The analogy "conditionalization : AGM :: imaging : KM" is vindicated under Lockean
cogency conditions ([EvaShearFitelson2022], read). Partial subjunctive supposition faces a dilemma
([EvaHartmann2021]). [Nielsen2022Harder] strengthens it: given monotonicity, the indicative and
subjunctive moods cannot be distinguished for partial supposition. [Zhang2024] relocates the dilemma to
convexity versus conservativeness; Jeffrey conditionalization is the only rule that is both. A causal
theory unifying all four supposition types appears in [GebharterEtAl2026].

**(g) Regularity, null sets and non-measurability.** The sequence runs: [IsaacsHajekHawthorne2022]
(imprecise credence for non-measurable propositions); [Dorr2024], who rebuts this via learning from
repeated observations; [Thong2024], who shows that in bounded 3-D space the proposal must give up
transitivity or qualitative additivity; and [GoodsellNebel2024]. Goodsell and Nebel argue that symmetry
is inconsistent with auxiliary assumptions of IHH and of Williamson's argument against regularity. They
add that the weaker *invariance* supports imprecision but conflicts with "mundane judgements". Also:
[Builes2020Paradox] answered by [DorrHawthorneIsaacs2021] (1/2 "if you should have any conditional
credence at all"); [MeehanZhang2021] (the Borel–Kolmogorov paradox arises for chance too);
[MancosuMassas2024] (when regular generalized measures exist on full powersets).

## 5. Open problems

**Marked open in the literature**
1. *Multiple successors.* We lack a general rule for scoring an update whose output is instantiated
   several times, in cases with differing evidence, partial resets or resets that depend on the
   credence. Schwarz: "I would like to have a fully general rule. Alas, I have none to offer"
   ([Schwarz2025SB] §3). He flags "epistemic bribes" and uncertainty about the length of one's doxastic
   trajectory (fn.15).
2. *State-dependence of norms.* Which features of the actual world may rational norms depend on? This
   "deserves more careful study"; the "anti-luck" condition is only a proposal ([Schwarz2025SB] §4).
3. *Synchronic Bayesianism over centred propositions.* Schwarz: "I have not shown that standard
   synchronic Bayesian reasoning is applicable to self-locating propositions" (fn.32). [Meacham2008] and
   [Builes2020TimeSlice] deny it.
4. *Average versus total accuracy across copies.* Unresolved since [KierlandMonton2005]. Schwarz (average)
   and [Kim2022Dominance] reach divergent verdicts.
5. *The measure problem:* self-locating epistemology for worlds with infinitely many agents is "an
   important open question" ([IsaacsHawthorneRussell2022] fn.20).
6. Which assumption fails if fine-tuning does *not* confirm a multiverse: separability, Locality,
   evidential posteriors, or (for large n) "ordinariness", whose status "does not seem nearly as clear"
   ([IsaacsHawthorneRussell2022] §7). They describe their result as "a framework in which to continue".
7. *Which amendment of conditionalization for centred credence?* There is consensus that one is needed
   ([EganTitelbaum2022SEP] §6), but recentering, decentering and restriction models remain rivals.
   [Schwarz2017] reaches two nearly equivalent candidates and does "not settle the choice".
8. *Choosing among strictly proper scores*, and non-veritist sources of epistemic value
   ([Pettigrew2023SEP] §8).
9. *Act–state dependence, epistemic expansions and varying importance* "still lack truly compelling
   responses" ([Pettigrew2023SEP] §8).
10. *Infinite domains:* it is "particularly difficult to characterize admissible accuracy measures"
    ([Nielsen2023]). See also Kelley & Neth's dilemma ([KelleyNeth2023]) and [Kelley2026].
11. *Availability:* can agents run updates sensitive to the evidence function (Schoenfield) or only to
    the proposition learned (Meehan–Zhang)? Pettigrew's reconstruction says the debate "reduces" to this.
    Meehan–Zhang assume factivity and equal weight across evidence functions.
12. *Interpreting expected-accuracy maximization over "signals"* is left "for future research"
    ([EaswaranNielsen2025] §1).
13. *Plan versus act:* even if one's plan must conditionalize, must one follow it? The SEP says this
    "leaves open an important question" ([Lin2022SEP] §5.2).
14. *Axiomatize the qualitative norms of Lockean indicative and subjunctive supposition* (LIS, LSS):
    "One major problem that arises from our analysis" ([EvaShearFitelson2022] §6).
15. *Partial subjunctive supposition:* convexity versus conservativeness ([Zhang2024]). Nielsen notes that one
    could reject his framework, "but that itself would be a surprising and interesting outcome"
    ([Nielsen2022Harder]).
16. *Builes's paradox:* must rational credence be hyperintensional, and is any conditional credence
    rationally required at all? See [Builes2020Paradox] and the conditional form of
    [DorrHawthorneIsaacs2021].
17. *Symmetry and invariance on non-measurable regions:* Goodsell and Nebel "find reason to be
    suspicious" of applying these principles at all ([GoodsellNebel2024]; cf. [Thong2024]).
18. *Pooling:* "No way of combining probabilities is best for all purposes"; impossibility results
    constrain the choice ([PettigrewWeisberg2025] Conclusion). Which desiderata govern which contexts is
    open.
19. *First-order versus higher-order opinion:* the framework "leaves us without answers—but with a clear
    picture of the question" ([Dorst2019HOU] abstract).
20. *Social updating:* van Fraassen's IBE rule beats conditionalization in Douven–Wenmackers simulations,
    "though we don't know whether some other rule outperforms that" ([Pettigrew2023SEP] §5.4.4).

**Further pressure points [inference]**
- I1. *Global evaluation for forgetful agents.* No one appears to have applied Meehan–Zhang-style global
  rule evaluation to memory loss or self-location. A globally constant rule judged by summed expected
  accuracy across Sleeping-Beauty-type protocols could favour halving, thirding or neither. Small finite
  cases are computable (sympy/z3).
- I2. *Weighting.* R5 assumes uniform weight over factive evidence functions. Natural non-uniform weights,
  such as one's credence about which inquiry one faces, may break the uniqueness of conditionalization.
  The result has no robustness analysis that I found.
- I3. *Schwarz and IHR may be partly reconcilable.* Schwarz's averaging measure is diachronic, while IHR's
  conditions are synchronic. Schwarz accepts the anthropic principle for Pr(Heads | E & Monday). It is
  unclear which IHR condition a Schwarz-style fallback update would breach in a multiverse analogue of
  Fissioning Fred.
- I4. *No propriety notion for multi-successor scores.* [Kim2022Dominance] reports that standard halving
  and thirding each rate another assignment better on total accuracy. This suggests the total measure is
  not self-endorsing in fission cases. No one has stated a propriety condition for multi-successor scoring.
- I5. *Upco versus Total Trust.* Upco's uniqueness uses Symmetry (peers). Total Trust concerns asymmetric
  experts. Whether a Jeffrey-pooling commutativity argument extends to weighted upco under Trust is
  untested.
- I6. *The anti-luck condition and externalist evidence.* Schwarz's anti-luck condition sits uneasily with
  his own remark (fn.12) that on some externalist views of evidence Beauty has decisive evidence for
  Monday ([Russell2023]). A case could separate what "could easily have been different" (Schwarz) from what is evidentially
  accessible.
- I7. *Regularity and pooling.* Upco is undefined where supports do not overlap. Jeffrey pooling needs
  non-extreme credences. How pooling should behave with Popper functions or Kolmogorov conditionalization
  is unexplored as far as I found.
- I8. *Does the causal theory escape the dilemma?* It is unknown whether the new rule for partial
  subjunctive supposition in [GebharterEtAl2026] satisfies convexity or conservativeness in Zhang's sense.
  If it satisfies both, it collides with Zhang's uniqueness claim.
- I9. *Adlam and IHR may not conflict.* Adlam targets *pure* self-locating credences. IHR's theorems
  concern qualitative hypotheses and need only Locality and evidential posteriors. The disagreement may be
  smaller than it looks.

## 6. Known moves and graveyard (do not rediscover)

**Sleeping Beauty arguments everyone knows**
- *Elga's thirder argument:* conditional on Monday, Heads gets 1/2, plus restricted indifference between
  the two Tails awakenings.
- Long-run frequency of awakenings; per-awakening betting.
- *The coin-signal variant:* reset either way, signal on Tuesday-if-Heads (Piccione–Rubinstein; [Dorr2002];
  [Arntzenius2003]). Schwarz's answer is that only in the variant is the posterior instantiated twice
  whatever the coin does.
- [Titelbaum2008]'s Technicolor Beauty; direct inference (Pollock group; [Horgan2019]; [Draper2019]).
- *CDT diachronic Dutch books against halfers* (Arntzenius 2002; [Hitchcock2004]; [DraperPust2008];
  [Briggs2010]). Countered by "betting odds and credences come apart" ([BradleyLeitgeb2006]); [Conitzer2015Dutch]
  answers that, for EDT agents, halfers and thirders alike can be Dutch-booked. Schwarz's
  sure-loss for thirders requires the second offer on both days.
- *The halfer case:* no new evidence plus Reflection ([Lewis2001]).
- *Known costs of halfing:*
  - The Lewisian halfer accepts 2/3 on learning that it is Monday.
  - The double-halfer "embarrassment" ([Titelbaum2012]; reply [Pust2023]).
  - The Halfer Rule violates Reflection ([Conitzer2015Devastating]).
- *Total versus average accuracy* ([KierlandMonton2005]); *modelling-assumption dissolution*
  ([CisewskiEtAl2016]); "self-location is no problem for conditionalization" ([Bradley2011]); selection
  effects rather than self-location ([Bradley2012]).
- *Further variants:* Beauty the High Roller, Informed SB, Weintraub's red/green, Dr. Evil, Fissioning
  Fred and quantum SB, the absent-minded driver, the presumptuous philosopher, Doomsday, Hacking's inverse
  gambler, Boltzmann brains, Immortal Beauty. *A "new" Beauty variant is presumptively a rediscovery
  unless it separates the averaging, summing, compartmentalized, SIA and SSA rules on a verdict not
  already tabulated in IHR Table 1 or Schwarz §§3–6.*

**Conditionalization's known problem cases**
- *Old evidence and new theory:* logical learning (Garber, Jeffrey, Niiniluoto); Earman's physics student;
  Wenmackers–Romeijn on considered possibilities.
- *Uncertain learning:* Jeffrey; rigidity; [Weisberg2015]'s undermining problem; [Lange2024].
- *Commutativity:* Field; [Weisberg2009]'s dilemma.
- *Memory loss* (Talbott); centred contents (conditionalization cannot lower a certainty).
- *Plan- versus act-formulations; "deterministic updating"* ([Pettigrew2020What]).

**Accuracy objections and the standard replies**
- Bronfman's "different dominators".
- *The evidentialist worry* ([EaswaranFitelson2012]). Replies: Pettigrew 2014; Joyce 2018.
- *Act–state dependence or "thwarted accuracy"* ([Greaves2013]; [Caie2013]; Campbell-Moore 2015).
  Replies: CDT with or without ratifiability (Joyce, Pettigrew); direction of fit ([KonekLevinstein2019]).
- *Epistemic expansions* (Carr; [Pettigrew2018Population]; Talbot 2022).
- *Varying importance* ([Levinstein2019Varying]); verisimilitude (Oddie); numerical representability
  (Mayo-Wilson & Wheeler).
- *Calibration as a value* ([Levinstein2017] against Pettigrew's "Decomposition").
- Strict propriety follows from weak propriety plus truth-directedness plus additivity
  ([CampbellMooreLevinstein2021]).
- Leitgeb–Pettigrew's non-Jeffrey rule is usually read as a strike against Brier (Levinstein 2012).
- Douven–Wenmackers' social simulations, answered by Pettigrew 2021.
- Higher-order evidence: steadfastness on the conform-plan picture versus calibrationism on the
  make-plan picture ([Schoenfield2018]).

**Deference**
- Reflection's counterexamples: forgetting, Talbott, the Arntzenius cases.
- Reflection's inconsistency for modest experts. New Reflection permits anti-experts ([DorstEtAl2021]).
- The "guru" formulation for information loss ([Elga2007]); Qualified and Distorted Reflection
  ([Briggs2009]).
- Hall's New Principle (named in [Levinstein2023]); Gaifman's expert framework (per [Lin2022SEP]).

**Pooling.** Linear pooling is not externally Bayesian. Geometric pooling has its own marginalization
failures (classic; McConway 1981, Genest–Zidek 1986; not re-read). Kopec's "Consensus" argument from total
accuracy, and its rebuttal via the value of diverse evidence (Zollman), are known (SEP §5.6). There is
also a known accuracy argument for linear pooling (Moss 2011; [Pettigrew2019Group]).

**Regularity and null sets**
- Infinitesimals versus the numerical fallacy ([Easwaran2014]); Williamson's coin.
- Comparative regularity; Haverkamp & Schulz 2012.
- Popper–Rényi functions, infinitesimals and Kolmogorov's regular conditional probabilities, compared
  in [Easwaran2019Handbook].
- The Borel–Kolmogorov relativity to how the conditioning event is presented ([Rescorla2015]).
- *Infinite fair lotteries:* conceptual coherence at par with continuous uniform distributions
  ([DiBella2022]).

**Indexicality sceptics.** Self-locating cases as "just Frege cases"; Cappelen–Dever's denial that
self-locating states explain action ([CappelenDever2013], per SEP §7); Millikan's self-names; Magidor.

## 7. The readership

Committee-map levels apply: I re-checked only what is marked.
- **Fitelson.** Co-author of *Deference Done Better* ([DorstEtAl2021]): Total Trust as the "middle way"
  (abstract). Co-author of [EvaShearFitelson2022] (full text read). Its results: conditionalization and
  imaging behave as probabilistic AGM and KM under Lockean cogency conditions; Preservation and
  Compositionality are the "most distinctive diachronic norms" of the two moods. It leaves axiomatization
  open. Co-author of [LewisFallisFitelson2024], which argues against monism about epistemic value (abstract)
  and of the accuracy and evidence chapter with Easwaran ([Easwaran2015Accuracy], title). Developer of PrSAT
  (committee map); expect formal claims to be checked closely [inference].
- **Easwaran.**
  - [Easwaran2013]: the expected-accuracy argument extends to infinite cases and yields
    conglomerability and Reflection (abstract).
  - [Easwaran2014]: against hyperreal regularity (abstract).
  - [EaswaranNielsen2025] (full text, parts): unifies the infinite and non-partitional settings.
  - The 2016 upco paper with Fenton-Glynn, Hitchcock and Velasco; *Dr. Truthlove* (title).
- **Weisberg.** Co-author with Pettigrew of [PettigrewWeisberg2024] (abstract) and [PettigrewWeisberg2025]
  (read): the upco uniqueness and commutativity theorem. Also *Geometric Pooling* (2026, title),
  [Weisberg2009] (title) and [Weisberg2015] on rigidity and undermining (abstract). Weisberg's page
  repeats one blurb under several papers; do not quote those blurbs.
- **Salow.**
  - Total Trust co-author.
  - [CampbellMooreSalow2020] and [CampbellMooreSalow2022]: risk-sensitive agents and evidence avoidance;
    a modified update rule under the Greaves–Wallace-style argument.
  - Externalist self-knowledge ([Salow2018], title).
- **Greaves.** [GreavesWallace2006] (R2) and [Greaves2013], the source of the act–state "epistemic decision
  theory" cases (per SEP). Neither is re-read here.
- **Dorr.**
  - Thirder ([Dorr2002]).
  - Co-author of [ArntzeniusDorr2017] on self-locating priors (unread; fetch filed).
  - [DorrHawthorneIsaacs2021]: the 1/2 verdict.
  - [Dorr2024]: rebuts the non-measurability argument for imprecision.
- **Hawthorne.**
  - [IsaacsHawthorneRussell2022] (read; R11).
  - [IsaacsHajekHawthorne2022]: imprecise credence for non-measurable propositions.
  - [DorrHawthorneIsaacs2021].
  - "Groupthink" ([RussellHawthorneBuchak2015]).
- **Nebel (and the organiser Goodsell).** [GoodsellNebel2024] argue against symmetry and invariance on
  non-measurable regions (abstract).
- **Jäger.** [Jager2021Immortal]: a thirding-based reincarnation argument (search summary; fetch filed).
  It must be represented exactly if used.
- **Cappelen and Dever.** [CappelenDever2013] deny essential indexicality and self-locating attitudes. Any
  essay that assumes centred contents should say why their objection does not apply.
- **Chalmers.** [Chalmers2011] "Frege's Puzzle and the Objects of Credence" (title; cited by Mahtani
  for conditionalization-based reasons for opacity). Co-author of the PhilPapers survey data.
- **Greco.** Pettigrew's blog names Greco as holding that, with non-introspectible evidence, the agent is
  "fragmented". I have not read Greco's text, so this cannot be attributed in a draft until it is checked
  ([Greco2014Iteration] is in the committee bibliography at title level).
- **Günther.** Learning conditional information by Jeffrey imaging (2017, title) bears on partial
  supposition.

## 8. Formal toolkit

- *Credal objects:* finite or σ-algebras over worlds or centred worlds (u, i, t); Lewisian properties.
- *Evidence and updating:* evidence functions, which may be factive, partitional or transparent;
  available update plans or dispositions; global rules ([MeehanZhang2025]); signals
  ([EaswaranNielsen2025]). Successor maps s(w) and the "+" shift A⁺ = {w : s(w) ∈ A}.
- *Update rules:* shifted conditionalization Cr₂(A) = Cr₁(A⁺ | E⁺) ([Schwarz2025SB]); the "confirmation
  factors" of compartmentalized conditionalization, SIA and SSA (IHR §5).
- *Accuracy tools:* strictly proper, continuous, possibly non-additive scoring rules (Brier, log);
  dominance through convex-hull theorems; expectations taken under the prior.
- *Pooling and supposition:* linear, geometric and upco pools; Jeffrey and Adams conditionalization;
  Lewis imaging and Jeffrey imaging; AGM and KM postulates; the Lockean thesis.
- *Measure zero:* Popper–Rényi functions; hyperreals; regular conditional distributions; Kolmogorov and
  Kolmogorov–Blackwell conditionalization.
- *Imprecision and verification:* sets of probabilities; dilation. PrSAT-style decision procedures;
  z3/sympy are available here for finite countermodels and exact expected-accuracy computations.

## 9. Sources (what was read)

**Full text, or substantial parts:**
- [Schwarz2025SB] (whole); [Schwarz2025Disproportionate] (abstract and introduction); [Schwarz2017]
  (abstract and introduction).
- [IsaacsHawthorneRussell2022] (§§1–2, 4, 7, appendix A definitions); [PettigrewWeisberg2025]
  (introduction, §§1–2, conclusion, appendix definitions).
- [EvaShearFitelson2022] (§1, §6); [EaswaranNielsen2025] (abstract, §1, §6, references).
- SEP: [EganTitelbaum2022SEP] (§§1, 6, 7); [Lin2022SEP] (§§3.3–3.6, 5.1–5.3); [Pettigrew2023SEP]
  (§§5.1–5.6, 7, 8).
- Pettigrew's blog post on Meehan–Zhang (2025, substack; a reliable secondary reconstruction).

**Abstract** (Crossref, Springer page or arXiv):
- Self-location and its frontier: Meehan–Zhang 2025; Isaacs–Russell; Gallow 2021; Dorst 2020; Dorst et
  al. 2021; Levinstein 2023; Builes 2020 (both papers); Builes 2024; Dorr–Hawthorne–Isaacs; Kim 2022a,b;
  Adelstein; Conitzer 2015a,b; Titelbaum 2008, 2012, 2013 (Compass); Hawley; Cisewski et al.; Bradley
  2012; Elga 2004, 2007; Halpern 2005.
- Accuracy and updating: Joyce 1998; Caie; Pettigrew 2018, 2020, 2022, 2023; Nielsen 2022, 2023;
  Kelley 2026; Campbell-Moore & Levinstein; Lewis–Fallis–Fitelson; Leitgeb–Pettigrew; Easwaran 2013;
  Huttegger; Briggs 2009; Briggs–Pettigrew; Das 2019, 2022; Schoenfield 2018.
- Deference and pooling: Dorst 2019; Hedden–Dorst; Dziurosz-Serafinowicz; Dietrich 2019;
  Baccelli–Stewart; Pettigrew 2019; Pettigrew–Weisberg 2024.
- Supposition: Eva–Hartmann; Nielsen 2022; Zhang 2024; Gebharter et al.
- Regularity and null sets: Rescorla 2018; Meehan–Zhang 2021, 2022; Isaacs–Hájek–Hawthorne; Dorr 2024;
  Goodsell–Nebel; Thong; DiBella; Mancosu–Massas; Easwaran 2014.
- Other: Mahtani 2024 (chapter abstracts); Bovens; Adlam; Sebens–Carroll.

**Search-engine summary only:** Button–Rothschild–Spectre; Russell 2023; Jäger 2021; Meacham
(forthcoming); Zhang's 2023 talk "Imaging and Conditionalization Revisited" (Berkeley Logic Colloquium
listing; not used).

**Title, or secondary report only:** everything else in `refs.json` (field `seen`).

**Fetch requests filed (`requests/fetch/l5-*`):**
- High: Meehan–Zhang 2025; Button–Rothschild–Spectre; Russell 2023; Levinstein 2023; Dorst et al. 2021;
  Arntzenius–Dorr 2017; Jäger 2021.
- Medium: Builes 2024; Isaacs–Russell 2023; Schoenfield 2017; Gallow 2021; Goodsell–Nebel 2024.
