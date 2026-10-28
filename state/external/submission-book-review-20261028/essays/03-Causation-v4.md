# Limits of Uniform Normality Filters in Actual Causation

**Abstract.** Normality can filter the counterfactual worlds that witness actual causation. Its difficulties with preemption and its dependence on causal representation are already recognized in the literature. I give a restricted classification: among uniform componentwise rankings that classify values by default status and equation conformity, four calibrating judgments hold exactly when the ranking satisfies a license rule. Under each of four specified default codings, no ranking in this class separates all three cases of switching, short-circuit prevention and preemption by a deviant event of a normal process. A default-preserving isomorphic pair illustrates the representational limitation beyond this local class. A supporting lemma adapts an intervention-elimination argument already used by Halpern. The contribution is the calibration and comparison for specified rules and models, not a general refutation of normality, a new discovery of the preemption problem, or a proof against richer representations.

## 1. Introduction

Two stories with the same structural equations and actual values can draw opposite causal verdicts. A bodyguard's antidote in coffee that nobody poisoned is not a cause of the victim's survival, yet the model of that story has the same form as a model of two overdetermining causes. Halpern and Hitchcock (2015) call this the problem of isomorphism, and one response they develop adds a normality ordering on worlds: a counterfactual world witnesses causation only if it is at least as normal as the actual world. Andreas and Günther (2024) add a deviancy condition to a regularity theory for the same purpose, and Gallow (2021) builds the default/deviant distinction into what a cause is.

Another familiar contrast is between switching and early preemption. A flipped switch sends a train down the right-hand track instead of the left, the tracks reconverge, and the flip is not usually counted a cause of the arrival; an assassin's poisoning, with a backup ready, is a cause of the death. Halpern (2015, 8) handles one model of the switch by normality, and Andreas and Günther's deviancy condition does the corresponding work in their theory, as Beckers (2026) shows.

My thesis is this: *within the specified class of local uniform witness filters, the four calibrating cases force a license rule; the switching/preemption contrasts then expose limits of the four specified default codings and of representations that identify the contrasted models.*

The positive result (§3) derives a family of admissible rankings from four familiar judgments. A supporting lemma explains a known tension between equation conformity and preemption under the modified definition. The limitative result (§4) turns on a preemption whose backup is a normal process: locusts strip a crop that drought would have killed within the week. Depending on how defaults are coded, this case has the same witness typicality profile either as Gallow's Doorbells switch or as Halpern and Hitchcock's short circuit. Section 5 goes beyond the class with an exactly isomorphic pair whose defaults coincide under all four codings; §6 turns to Andreas and Günther; §7 answers objections.

I do not claim that normality is idle, that it has no role in graded causal judgment, or that no richer model can draw the switch/preemption line. The claims concern models in which each route to the effect is an event variable, the format of the switch and preemption models in the literature discussed here.

**Closest work and increment.** Halpern and Hitchcock (2015, 19, 34–37) allow exceptions to the default that variables obey their equations. Halpern (2016, Example 3.2.6, 84–85) already shows that excluding a preemption witness can make the preempted throw part of a cause; adding an accuracy variable can sharpen the difficulty. His Theorem 4.4.4(b) (121; proof 133–134) establishes stability under conservative extensions whose added variables respect their equations. The lemma below adapts its elimination-and-minimality reasoning to an individual conforming witness. Neither the problem nor the proof technique is claimed as new.

Halpern also explains why inadequate representations cannot distinguish relevant scenarios (2016, §4.1) and why normality rankings need independent motivation (§4.7). Beckers (2026) shows that Andreas and Günther's deviancy condition fails for early preemption with a normal backup. These are starting points. The proposed increment is the exact four-case classification, the three-case impossibility under four uniform codings, and an explicit pair preserving defaults across those codings. Hitchcock (2007) supplies the inertial coding and Principle of Sufficient Reason used in §5. The general isomorphism principle is elementary and already familiar.

## 2. The setting

**Models.** An acyclic causal model has binary, intervenable variables. A *root* has no parents among the modeled variables and takes its actual value from the context. A *non-root* has an equation from its parents. Both are endogenous in the Halpern–Pearl sense; the conformity test here concerns the non-root equations. The *actual world* is the solution for the actual context; an intervention $[\vec X\leftarrow\vec x]$ replaces the equations of $\vec X$ by constants.

**Three definitions.** I follow Halpern's (2015, 3–4) statement of the original, updated and modified Halpern–Pearl definitions. $\vec X=\vec x$ is a cause of $\varphi$ if both actually hold (AC1), if a minimality condition holds (AC3), and if there is a *witness*: a setting $\vec x'$ and a set $\vec W$ of other variables with values $\vec w$ such that $[\vec X\leftarrow\vec x',\vec W\leftarrow\vec w]\neg\varphi$ (AC2(a)). The original and updated definitions let $\vec w$ be any values, subject to sufficiency conditions that differ between them (AC2(b) and AC2(b$^u$)). The modified definition requires $\vec w$ to be the actual values: the witness may only freeze variables at what they actually were (AC2(a$^m$)). A conjunct of a cause is *part of* a cause. The *witness world* is the solution under the witness intervention.

**Normality as a filter.** Halpern and Hitchcock (2015, 20–21) require a witness world to be at least as normal as the actual world. Their guidelines favor improvements in individual variables' typicality when nothing worsens, but allow special comparisons when some variables improve and others worsen. They also normally treat endogenous variables' agreement with their equations as typical, while permitting exceptions (19–20). I call this second guideline the *conformity default*. Halpern (2016, §3.2) extends all three definitions this way. His graded account instead retains causes with abnormal witnesses and compares their quality (§3.3); his alternative in §3.5 compares events comprising sets of contexts. The results below concern the world-based filter. They do not directly apply to those alternatives.

**Local uniform rankings.** Each variable has a default value. In a given world, a non-root variable falls into one of four categories:

- $\mathbf n$: default, conforming (its value is the default, and its equation gives that value);
- $\mathbf l$: licensed deviant (its value is deviant, and its equation gives that value);
- $\mathbf f$: frozen default (its value is the default, but its equation demands the deviant value);
- $\mathbf u$: unlicensed deviant (its value is deviant, but its equation demands the default).

A root is either at its default or not, and a root's default is more typical than its deviant value. A *local uniform ranking* is a preorder $\geq$ on $\{\mathbf n,\mathbf l,\mathbf f,\mathbf u\}$, the same for every variable. The witness world passes the filter iff each variable's category there is $\geq$ its category in the actual world, a strict componentwise implementation of their first guideline. Their broader framework also permits special cross-variable comparisons; those are outside this class. Three members of the class matter below:

- **Conformity:** $\mathbf n\equiv\mathbf l>\mathbf f,\mathbf u$. This makes the conformity default exceptionless.
- **Value-only:** $\mathbf n\equiv\mathbf f>\mathbf l\equiv\mathbf u$. Typicality depends on values alone. Halpern and Hitchcock (2015, 35) consider and reject this ranking for their short circuit.
- **License:** $\mathbf l\equiv\mathbf n$, $\mathbf f\geq\mathbf n$, and $\mathbf u\not\geq\mathbf n$. A value is atypical only if it is a deviant value that its own mechanism did not produce.

**Coding defaults.** A default assignment needs a rule. I consider four uniform rules:

- **Event coding:** occurrences are deviant and absences default.
- **Inertial coding:** a self-sustaining state is default and a change is deviant (Hitchcock 2007, 506–507).
- **Normal-course coding:** a non-root variable's default is the value it takes when every root takes its default value.
- **Normal course given the background:** a non-root variable's default is the value it takes when the candidate cause takes its default value and every other root keeps its actual value.

The last two implement an undisturbed-system conception of defaults reported by Halpern and Hitchcock (2015, 18). Event, inertial and the first normal-course coding assign the same defaults in the four cases of §3; they come apart in §4.

The broad computational battery used all 75 weak orders and candidates of up to three conjuncts. The central theorems were subsequently checked for all 355 category preorders and every candidate subset (Appendix B).

## 3. What normality must do

Four familiar cases calibrate the ranking. The theorem is conditional on retaining their stated judgments; it does not establish those judgments independently. Roots are listed with their actual values; every default is 0 under each of the first three coding rules.

> *Genuine prevention.* Roots $P=1$ (poison in the coffee), $A=1$ (antidote). $V=P\wedge\neg A$ (the victim dies). The antidote caused the survival.
>
> *Chain.* Root $C=1$. $I=C$, $Y=I$. $C=1$ caused $Y=1$.
>
> *Boulder.* Root $F=1$ (a boulder falls). $B=F$ (the boulder heads for the hiker), $K=F$ (the hiker ducks), $H=B\wedge\neg K$ (the hiker is hit). The ducking caused the hiker not to be hit. (This is Hitchcock's (2001) case, in the form presented by Andreas and Günther (2024, 18).)
>
> *Short circuit.* Root $A=1$ (a bodyguard adds an antidote). $P=A$ (a second bodyguard, conspiring, adds poison only if the antidote is in), $V=P\wedge\neg A$. The antidote is not a cause of the survival (Halpern and Hitchcock 2015, 34–35; Halpern 2015, Ex. 3.10).

**Theorem 1.** Under event, inertial or normal-course coding (with all roots at default), and for each of the three definitions, a local uniform ranking gives the stated verdicts in all four cases iff $\mathbf l\equiv\mathbf n$, $\mathbf f\geq\mathbf n$ and $\mathbf u\not\geq\mathbf n$. That is, iff it is a license ranking.

*Proof sketch* (Appendix A). Genuine prevention's witness moves $V$ from $\mathbf n$ to $\mathbf l$, so $\mathbf l\geq\mathbf n$; the chain's moves $I$ and $Y$ from $\mathbf l$ to $\mathbf n$, so $\mathbf n\geq\mathbf l$. The short circuit's only witness keeps the poison in without the antidote ($P$: $\mathbf l\to\mathbf u$; $V$: $\mathbf n\to\mathbf l$) and must fail, so $\mathbf u\not\geq\mathbf n$. The ducking's witness either leaves the hiker not ducking as the boulder falls ($K$: $\mathbf l\to\mathbf f$) or forces the boulder's course against its equation ($B$: $\mathbf l\to\mathbf u$, already excluded), so $\mathbf f\geq\mathbf n$. A license ranking admits the genuine-prevention, chain and ducking witnesses and excludes the short-circuit witness. ∎

Of the 75 weak orders, exactly two satisfy the theorem's conditions: $\mathbf u<\mathbf n=\mathbf l=\mathbf f$ and $\mathbf u<\mathbf n=\mathbf l<\mathbf f$. On a battery of 36 queries in 25 models (Appendix B), both give the standard verdicts under event coding in all three definitions except on Hall's switch and Doorbells (§4) and on one bogus-prevention model, which a neutralization variable corrects, as in Halpern and Hitchcock (2015, 29 fn. 15). Sufficiency is relative to that battery; necessity rests on the four cases alone.

The conformity ranking violates $\mathbf f\geq\mathbf n$, so it denies, under every definition, that the ducking prevented the hit. The value-only ranking violates $\mathbf l\geq\mathbf n$ and denies that the antidote prevented the poisoning. The surviving comparisons systematize exceptions Halpern and Hitchcock explicitly allow: accepting a backup's unlicensed absence in preemption, while excluding poison present against its short-circuit equation (2015, 34–36).

This local simplification has a clear motivation. Halpern's compact-representation rules normally give equal typicality to equation-conforming values and lower typicality to violations, with explicit exceptions and cross-variable comparisons allowed (2016, §5.2.2, 149–150). Theorem 1 asks which distinctions a uniform replacement must retain to fit the four cases. It does not classify all his compact representations.

Halpern and Hitchcock suggest adding intentions variables to remove particular exceptions (2015, 36–37). Under the modified definition, the following witness-level fact limits that strategy. It uses the removal of equation-conforming interventions and AC3 minimality found in Halpern's stability proof (2016, Theorem 4.4.4(b), 133–134). His theorem concerns conservative extensions and normality preservation; the lemma makes no comparison between models and assumes conformity only in the specified witness.

**Lemma (frozen witnesses).** Under the modified definition, let $\vec X=\vec x$ be a cause of $\varphi$ with a witness in which no non-root variable violates its equation. Then every member of $\vec X$ is a root, and $\varphi$ depends counterfactually on $\vec X=\vec x$.

*Proof.* Let $\vec R$ be the root members of the candidate $\vec X$. If the witness violates no non-root equation, it satisfies all the original non-root equations; every root outside $\vec R$ retains its actual value, including any frozen root. By acyclicity, uniqueness of solutions therefore makes the witness identical to the solution under $[\vec R\leftarrow\vec r']$ alone. Since the outcome changes, $\vec R$ is nonempty. If $\vec X$ contained a non-root member, $\vec R$ would be a proper subset satisfying the counterfactual condition with no frozen contingency, contrary to AC3 minimality. Thus every member of the minimal cause is a root, and the outcome changes under its intervention alone. This argument uses minimality; it does not assume that non-root members of a conjunctive candidate have unchanged parents. ∎

Thus, in an expanded acyclic model where the candidate remains non-but-for or is a non-root minimal cause, every modified-definition witness violates a non-root equation. A changed representation may instead make it a root but-for cause. An added intentions variable cannot rescue an equation-conforming witness while preserving the lemma's assumptions: the modified definition cannot freely reset a contingency variable. The familiar late-preemption consequence, that excluding the frozen backup witness can make Billy's throw part of a cause, is already Halpern's Example 3.2.6 (2016, 84–85). The present point is how the calibration constrains a uniform response: it requires accepting frozen defaults, which creates the switching problem below.

## 4. Limits of the calibrated local class

Consider first a preemption whose backup is a normal process.

> *Locusts.* It is the dry season. Roots: $S=1$ (a locust swarm arrives), $Q=0$ (rain falls). $D=\neg Q\wedge\neg S$: unwatered and uneaten, the maize dies of drought within the week. $X=S\vee D$: the maize is destroyed. Actually, $D=0$ and $X=1$. The swarm destroyed the maize.

Except for the normality of the backup, this is early preemption. Without normality, every account considered here counts the swarm a cause: the three definitions, NESS and CNESS (Beckers 2021), and Andreas and Günther's (2024) preliminary definition. If the backup gets a deviant trigger of its own (a failed irrigation pump, say), all of them count it a cause with normality too (Appendix B).

Now a switch in which neither route is a standing state.

> *Doorbells* (Gallow 2021, 84–86). Roots: $M=1$ (Marty presses the button), $T=1$ (Doc has set the switch to the right). $L=M\wedge\neg T$ (the left bell rings), $R=M\wedge T$ (the right bell rings), $E=L\vee R$ (Einstein barks). Actually, $L=0$, $R=1$, $E=1$. The switch-setting was not a cause of the barking.

Gallow's verdict is that "Doc's flipping the switch to the right was (along with Marty's pressing the button) a cause of the right bell's ringing, but it was not a cause of Einstein's barking" (2021, 85). His model uses a four-valued switch variable; the binary model is my simplification, in the usual format of one event variable per route.

**Theorem 2.** Fix any local uniform ranking and any of the three definitions. (a) Under event or inertial coding, $T=1$ is part of a cause of $E=1$ in Doorbells iff $S=1$ is part of a cause of $X=1$ in Locusts. (b) Under either normal-course coding, $S=1$ is part of a cause of $X=1$ in Locusts iff $A=1$ is part of a cause of $V=0$ in the short circuit. Hence no ranking in the class, under any of the four coding rules, gives all three standard verdicts.

*Proof.* (a) Under event and inertial coding every non-root variable in both models defaults to 0 (silence and survival are standing states; ringing and dying are changes). The modified witness for the switch-setting is $[T\leftarrow0, L\leftarrow0]$, which freezes the left bell silent although the button is pressed. Relative to the actual world, $L$ moves from $\mathbf n$ to $\mathbf f$, and $R$ and $E$ move from $\mathbf l$ to $\mathbf n$. The witness for the swarm is $[S\leftarrow0, D\leftarrow0]$, which suppresses drought death despite the absent swarm and absent rain. $D$ moves from $\mathbf n$ to $\mathbf f$, and $X$ from $\mathbf l$ to $\mathbf n$. Both pass iff $\mathbf f\geq\mathbf n$ and $\mathbf n\geq\mathbf l$. The further witnesses that the original and updated definitions allow either make it rain (a root moved to its deviant value) or cancel the press (violating sufficiency); see Appendix A.

(b) Under either normal-course coding the drought death is the default: with the swarm absent and no rain, $D=1$ and $X=1$. Actually, $D$ is a licensed deviant ($\mathbf l$) and $X$ is $\mathbf n$. In the witness, $D$ becomes $\mathbf u$ (alive, against an equation that now demands death) and $X$ becomes $\mathbf l$. In the short circuit, under every coding, the antidote's witness moves $P$ from $\mathbf l$ to $\mathbf u$ and $V$ from $\mathbf n$ to $\mathbf l$. Both pass iff $\mathbf u\geq\mathbf l$ and $\mathbf l\geq\mathbf n$.

An exhaustive check confirms both parts for all 355 preorders on the four categories, including partial ones, under all three definitions and with candidates of every possible conjunction size. ∎

Theorem 2 assumes nothing about which ranking is correct. For the license rule it means: under event or inertial coding, both the swarm and the switch-setting are causes; under normal-course coding the swarm is not. (Under the modified definition the switch-setting's witness also has the profile of Suzy's in late preemption.) The remaining exits are non-uniform rankings or codings (§5).

**Table 1.** Verdicts under the modified definition ("C" = cause or part of a cause; the original and updated definitions agree except where noted). Verdicts that depart from the standard one are marked \*.

| Case (standard verdict) | License, event | License, inertial | License, normal course | Conformity, any coding | Value-only, event |
|---|---|---|---|---|---|
| Genuine prevention (C) | C | C | C | C | not\* |
| Boulder: ducking (C) | C | C | C | not\* | not\* |
| Short circuit (not) | not | not | not | not | not |
| Late preemption: Billy (not) | not | not | not | C\* (modified only) | not |
| Locusts (C) | C | C | not\* | not\* | C |
| Doorbells (not) | C\* | C\* | C\* / not | not | C\* |
| Hall's LT/RT switch (not) | C\* | not | not | not | C\* |

In the Doorbells row the normal-course codings differ: with all roots at default no bell is due to ring ("C\*"); given the actual press, the left bell's ringing is the default ("not").

Halpern (2015, 8; 2016, 90–91) already distinguishes several switch models and explains the effect of normality on them. In the LT/RT route model, excluding the witness where the train fails to take the left track despite a left setting blocks the switch verdict. Under event coding that excludes a frozen default, conflicting with Theorem 1; under inertial coding it can be the license rule's penalty on an unlicensed deviant. Doorbells tests whether that latter policy transfers when both routes are occurrences. The theorem supplies a cross-case constraint within the stated class, rather than discovering that normality can struggle with switches.

## 5. Beyond the class: an isomorph with identical defaults

Halpern and Hitchcock do not commit to the class (2015, 26 fn. 13; 36 fn. 18). The obvious non-local repair looks at a mechanism's inputs: a frozen default is atypical only when some parent of the frozen variable takes a deviant value. This has a pedigree in Hitchcock's (2007, 508) Principle of Sufficient Reason, which says that a variable with parents takes a default value whenever all its parents do; a deviant value needs a deviant source. The drought equation $D=\neg Q\wedge\neg S$ violates that principle under event coding, since a deviant death follows from all-default parents, whereas the left bell's equation does not. This *trigger rule* penalizes the frozen left bell (its parent, the press, is deviant) but not the frozen maize. With the candidate's own value exempted and the train's left-track travel coded inertially, the trigger rule gives the standard verdict on every case in Table 1 under the original and updated definitions. (Under the modified definition it errs on Billy's throw and on the switch.)

But Hitchcock's principle also tells us how to repair the drought model. A deviant death needs a deviant source, and the obvious one is that the crop is there to die. Make it explicit:

> *Seedlings.* A field was sown this morning. Roots: $P=1$ (the field is sown), $S=1$ (a swarm arrives); it is a dry week, and no rain is possible. $G=P\wedge S$ (the swarm strips the seedlings), $D=P\wedge\neg S$ (the seedlings die of drought within the week), $X=G\vee D$ (the seedlings are destroyed). Actually, $G=1$, $D=0$, $X=1$. The swarm destroyed the seedlings.

The map $P\mapsto M$, $S\mapsto T$, $G\mapsto R$, $D\mapsto L$, $X\mapsto E$ is an isomorphism from Seedlings onto Doorbells. It preserves equations and actual values. It also preserves default assignments under each of the four coding rules:

- Under event and inertial coding, the sowing and the press are actions and so deviant, and every non-root variable defaults to 0.
- Under normal-course coding with all roots at default, nothing is sown and nothing is pressed, so again every non-root variable defaults to 0.
- Given the actual background, the drought death and the left bell's ringing are both defaults, and so are the destruction and the barking.

**Proposition 1.** Any account whose verdicts depend only on the equations, the actual values and the default assignment (not on what the variables are called) gives the swarm in Seedlings and the switch-setting in Doorbells the same verdict, under each of the four coding rules.

The proof is immediate. Halpern's insufficient-expressiveness diagnosis (2016, 108–111) already explains the general limitation. The pair checks that adding the four specified default assignments does not break this particular isomorphism. Seedlings satisfies Hitchcock's principle, and it is no less a case of a deviant event preempting a normal process. The computed verdicts bear the proposition out: the trigger rule says neither is a cause, the license rule says both are (or, given the actual background, neither), both of Andreas and Günther's deviancy conditions say neither, and NESS and CNESS say both.

An account using only equations, actual values and defaults must break at least one of those represented agreements to separate the pair. Changing the defaults of the shared enabling conditions is one possibility. That does not track the contrast, which survives when the condition is coded alike. Let a postman press the button every noon, so that the press is statistically normal: a switch that diverts a routine signal is still a switch, yet under the trigger rule the switch-setting is now a cause, exactly as the swarm is when the crop is a standing one (Appendix B).

## 6. Regularity theories

Andreas and Günther's (2024) final theory counts $c$ a cause of $e$ only if, among other conditions, every root proposition left out of a maximal set of facts that does not by itself entail the effect is "more deviant than" its negation (their condition (4), p. 13). In their later definition, as Beckers (2026, 3–4) states it, the condition is restricted to literals whose variables are neither ancestors nor descendants of the candidate (C5). Beckers (2026, 9–11) gives the decisive case against both. In *Backup 2* a trainee surgeon operates while a supervisor, as a moral norm requires, stands ready to operate if she does not, and the deviancy definitions "force us to conclude that trainee's action did not cause the outcome" (p. 11). Beckers also proves their 2025 definition equivalent to a 2024 one (Thm. 2.2), so the verdict reaches their current account. The counterexample and the equivalence are Beckers's; I add that no moral norm is needed, and a condition that predicts the failure:

**Proposition 2.** Let $N$ be a set of actual root literals, none more deviant than its negation, which together with the equations of $C$'s descendants entails $E$. Then $C$ is not a cause of $E$ under condition (4). If, in addition, no member of $N$ is an ancestor of $C$, then $C$ is not a cause of $E$ under (C5).

*Proof.* Both definitions require the equations of all of $C$'s descendants to be among the laws used (their condition (5), Beckers's (C4)). Those laws, together with any set of facts that contains $N$, entail $E$, so the maximal non-entailing set of facts must omit some $n\in N$. That $n$ is a root, and it is not more deviant than its negation, so it violates (4). If it is not an ancestor of $C$, it also violates (C5), because roots are never descendants. ∎

In Locusts, $N=\{\neg Q\}$: with no rain, the laws of $D$ and $X$ yield $X\leftrightarrow S\vee\neg S$. The absence of rain is statistically normal, violates no norm, and is an absence: normal by each of Andreas and Günther's criteria. One response changes the event/absence classification of the drought, although changing the model or rejecting a verdict also remains possible. Andreas and Günther themselves ask: "Is, for example, the death of a plant an occurring event, or rather the absence of continued living?" (2024, 27). But the same relabelling, applied to the poison-free coffee, would undo their treatment of bogus prevention (pp. 13–14). Proposition 1 adds a representational constraint: when the default assignments correspond under the isomorphism, those resources alone cannot preserve opposite verdicts.

## 7. Objections and replies

**Objection 1: flexibility.** Halpern and Hitchcock allow richer rankings, and Halpern supplies graded and event-based alternatives. The local filter is not their whole theory.

*Reply.* Correct. Halpern's graded account (2016, 85–86) retains causes that a hard filter would exclude. His event-based account (97–99) compares sets of contexts satisfying witness formulas, and his further proposal (100–102) considers changes in normality. None is exhausted by one uniform order on the four local categories. The theorems give no direct impossibility result for them.

The question addressed here is whether a reusable rule using only default status and equation conformity can recover the specified contrasts. Those features offer a compact, transferable specification; Theorems 1 and 2 locate its limit. A richer account must justify its additional information. That requirement is already explicit in Halpern (2016, 83, 126–127), who discusses statistical and normative grounds for rankings. Proposition 1 illustrates the requirement in the present pair; it does not introduce it.

**Objection 2: aptness.** The binary route models are inapt. Halpern (2015, 7–8; 2016, 38–39) gets the switch right in a three-variable model where the track variable makes no difference to arrival. Seedlings could be modelled the same way, with a single "destroyed by some route" mechanism, or with a finer-grained effect variable.

*Reply.* Model choice is a serious response. A time-indexed outcome can distinguish destruction on the third day from destruction by the week's end. The swarm can then be a but-for cause of the earlier outcome, while the switch remains irrelevant to whether the bark occurs at its specified time. This uses the importance of temporal representation that Halpern emphasizes (2016, 124–126).

It also limits what the example establishes. If the outcome is only destruction by the week's end, a theorist may deny that the swarm and switch deserve opposite judgments at that grain. The essay therefore offers a conditional diagnostic, not a verdict invariant under every legitimate redescription. Retaining the contrast requires either defending it for the coarse outcome or enriching the representation. Normality cannot recover omitted timing information solely from a set of defaults that agrees across the two models.

Gallow's (2021, 85) multi-valued switch model supplies another representational option; the binary route model here is not his complete model. The question for each option is whether a principled modeling rule selects it before the desired causal verdict is supplied. The displayed pair adds a test case for that familiar modeling question.

**Objection 3: the verdicts.** Perhaps the swarm is not a cause, since the destruction was coming anyway. Alternatively, with transitivity theorists, perhaps Doc's switch-setting is a cause of the barking.

*Reply.* The swarm verdict is plausible when the narrative fixes the swarm as the process that actually destroys the maize before drought would have done so. A theorist can dispute that verdict or argue that the equations omit precisely this timing and process information. That is a substantive response, not a contradiction. The results are conditional: if these contrasting judgments are retained while the represented features are held fixed, a default-only filter cannot recover the contrast. An account that accepts causation by the switch avoids that particular demand. Richer process representations remain open.

**Objection 4: triviality.** Proposition 1 follows from isomorphism, and Theorem 2 rests on one or two comparisons.

*Reply.* The abstract invariance claim is elementary. Its role is to test a proposed explanatory resource. Defaults can distinguish bogus prevention from overdetermination because the assigned defaults differ. The pair here preserves them under four specified codings, including codings that make a shared enabling condition explicit. The substantive issue is whether the causal contrast survives at that common representational grain. If it does, default status is insufficient; if it does not, the case explains why an appeal to preemption alone did not establish the contrast. Neither answer licenses the unrestricted conclusion that normality never distinguishes isomorphs.

## 8. Conclusion

Four calibrating judgments force the license family within the uniform componentwise class. Under each of four specified default codings, no ranking in that class gives all three target verdicts for Doorbells, Locusts and the short circuit. The default-preserving isomorph shows that broader rules using only the same represented information also cannot separate the displayed pair.

These are restricted classification results within an established diagnosis of representational limits. Halpern already identifies the conformity/preemption tension, alternatives to witness filtering, and the need to justify models. The calibration makes one tradeoff explicit: a uniform policy accepting the frozen defaults needed by the calibrating cases cannot then exclude them merely because the resulting case is called switching. A successful response must use additional distinctions, enrich the representation, or revise a judgment. The essay specifies where that choice arises; it does not establish which response is uniquely correct.

## Appendix A. Proofs

**Theorem 1, witness enumeration.** In genuine prevention, a witness for $A=1$ sets $A=0$, possibly with $P$ fixed at 1. The world is $(P,A,V)=(1,0,1)$: $A$ is at its default, $P$ is unchanged, and $V$ moves from $\mathbf n$ to $\mathbf l$. In the chain, the only witness for $C=1$ is $[C\leftarrow0]$, under which $I$ and $Y$ move from $\mathbf l$ to $\mathbf n$; fixing $I$ or $Y$ at 1 restores $Y=1$.

In the short circuit, $[A\leftarrow0]$ alone gives $P=0$ and $V=0$, so it is not a witness. The only witness is $[A\leftarrow0,P\leftarrow1]$, with world $(0,1,1)$ for $(A,P,V)$; $P$ moves from $\mathbf l$ to $\mathbf u$ and $V$ from $\mathbf n$ to $\mathbf l$. It is admitted iff $\mathbf u\geq\mathbf l$ and $\mathbf l\geq\mathbf n$.

In the boulder case, $\neg\varphi$ requires $B=1$ and $K=0$. With $F=1$ the world is $(F,B,K,H)=(1,1,0,1)$: $K$ moves from $\mathbf l$ to $\mathbf f$, $B$ stays $\mathbf l$, and $H$ moves from $\mathbf n$ to $\mathbf l$. With $F$ set to 0, $B$ must be set to 1, giving $(0,1,0,1)$: $B$ moves from $\mathbf l$ to $\mathbf u$, $K$ moves from $\mathbf l$ to $\mathbf n$, and $H$ from $\mathbf n$ to $\mathbf l$. Setting $H$ itself violates sufficiency. The four verdicts therefore hold iff (i) $\mathbf l\geq\mathbf n$, (ii) $\mathbf n\geq\mathbf l$, (iii) not both $\mathbf u\geq\mathbf l$ and $\mathbf l\geq\mathbf n$, and (iv) either $\mathbf f\geq\mathbf l$ and $\mathbf l\geq\mathbf n$, or $\mathbf u\geq\mathbf l$ and $\mathbf l\geq\mathbf n$. By (i) and (ii), $\mathbf l\equiv\mathbf n$; then (iii) gives $\mathbf u\not\geq\mathbf n$, and (iv) reduces to $\mathbf f\geq\mathbf n$.

The modified definition admits only the first boulder witness, and the conditions are the same. Partial preorders are covered, since only the listed comparisons occur. All four candidates are single conjuncts; conjunctive candidates were checked by machine.

**Theorem 2, remaining witnesses.** In Locusts, original and updated definitions: a witness setting $Q=1$ moves a root to its deviant value and fails; setting $D=0$ gives the modified witness, and $D=1$ gives $X=1$. In Doorbells a witness must keep $M=1$, since with $M=0$ restoring $T=1$ does not restore the barking (AC2(b)); then $\neg\varphi$ requires $L=0$, the modified witness. For conjunctive candidates, exhaustive finite checking covers all 355 category preorders and every nonempty candidate subset, including subsets containing the outcome. It verifies the same equivalences without imposing a size-three cutoff.

## Appendix B. The computation

The code (Python, standard library only) implements the three definitions as stated by Halpern (2015, 3–4); Halpern and Hitchcock's filter with componentwise comparison; NESS and CNESS (Beckers 2021); Andreas and Günther's (2024) definitions with condition (4); and the variant with (C5) in Beckers's (2026, 3–4) statement. Without normality it reproduces Halpern's (2015) verdicts in Examples 3.3, 3.4, 3.9 (LT/RT model) and 3.10, and it reproduces Andreas and Günther's (2024, 28–29) table. For each coding rule and each of the 75 weak orders it evaluates 36 queries in 25 models.

The original checks identify the two license weak orders, verify the displayed contrasts and default-preserving isomorphism, and test the regularity-theory corollary on 41 random models. The final targeted check expands the central claims to all 355 reflexive, transitive relations on the four categories. It enumerates every candidate subset, including those containing the outcome, computes every admissible witness under each definition, and applies AC3 after normality filtering. There were no discrepancies in 2,130 calibration comparisons and 3,195 paired-case comparisons. In the cases covered by these counts, inertial coding coincides with event coding. These are exhaustive checks of the finite cases and rankings specified here; they establish nothing about richer world rankings or unmodeled causal features.

## References

Andreas, Holger, and Mario Günther. 2024. "A Regularity Theory of Causation." *Pacific Philosophical Quarterly* 105 (1): 2–32. https://doi.org/10.1111/papq.12447.

Beckers, Sander. 2021. "The Counterfactual NESS Definition of Causation." *Proceedings of the AAAI Conference on Artificial Intelligence* 35 (7): 6210–6217. https://doi.org/10.1609/aaai.v35i7.16772.

Beckers, Sander. 2026. "Difference-Making without Making a Difference." Preprint, arXiv:2606.24832v1.

Gallow, J. Dmitri. 2021. "A Model-Invariant Theory of Causation." *Philosophical Review* 130 (1): 45–96. https://doi.org/10.1215/00318108-8699682.

Hall, Ned. 2007. "Structural Equations and Causation." *Philosophical Studies* 132 (1): 109–136. https://doi.org/10.1007/s11098-006-9057-9.

Halpern, Joseph Y. 2015. "A Modification of the Halpern–Pearl Definition of Causality." Preprint, arXiv:1505.00162v1. (Page references are to this version.)

Halpern, Joseph Y. 2016. *Actual Causality*. Cambridge, MA: MIT Press. (Page references are to the printed pagination.)

Halpern, Joseph Y., and Christopher Hitchcock. 2015. "Graded Causation and Defaults." *British Journal for the Philosophy of Science* 66 (2): 413–457. https://doi.org/10.1093/bjps/axt050. (Page references are to arXiv:1309.1226.)

Hitchcock, Christopher. 2001. "The Intransitivity of Causation Revealed in Equations and Graphs." *Journal of Philosophy* 98 (6): 273–299. https://doi.org/10.2307/2678432.

Hitchcock, Christopher. 2007. "Prevention, Preemption, and the Principle of Sufficient Reason." *Philosophical Review* 116 (4): 495–532. https://doi.org/10.1215/00318108-2007-012.

