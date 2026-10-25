# What Normality Can and Cannot Do in Theories of Actual Causation

**Abstract.** Normality entered structural-equation accounts of actual causation to separate causal structures that are isomorphic but judged differently. I ask what it can contribute as a filter on the counterfactual worlds that witness causation, as in Halpern and Hitchcock's account. Within the rankings that judge each variable by whether its value is its default and whether its own equation produces that value, four standard cases force one rule: a deviant value is atypical exactly when its mechanism did not produce it. Halpern and Hitchcock's stated default, that variables typically obey their equations, is excluded, and under Halpern's modified definition it fails wholesale. Under each of the four specified uniform default codings, no such ranking separates a switch from a deviant event preempting a normally running process, and an exactly isomorphic pair with identical defaults shows that no default-based account can. These results limit the specified local rankings and default-only representations; they do not exclude richer normality models.

## 1. Introduction

Two stories with the same structural equations and actual values can draw opposite causal verdicts. A bodyguard's antidote in coffee that nobody poisoned is not a cause of the victim's survival, yet the model of that story has the same form as a model of two overdetermining causes. Halpern and Hitchcock (2015) call this the problem of isomorphism, and their answer has become the standard one: add a normality ordering on worlds, and count a counterfactual world as a witness to causation only if it is at least as normal as the actual world. Andreas and Günther (2024) add a deviancy condition to a regularity theory for the same purpose, and Gallow (2021) builds the default/deviant distinction into what a cause is.

The best-known isomorph pair after bogus prevention and overdetermination is the switch and early preemption. A flipped switch sends a train down the right-hand track instead of the left, the tracks reconverge, and the flip is not usually counted a cause of the arrival; an assassin's poisoning, with a backup ready, is a cause of the death. Halpern (2015, 8) handles one model of the switch by normality, and Andreas and Günther's deviancy condition does the corresponding work in their theory, as Beckers (2026) shows.

My thesis is this: *within the specified class of local uniform witness filters, the four calibrating cases force a licence rule; the switching/preemption contrasts then expose limits of the four specified default codings and of representations that identify the contrasted models.*

The positive result (§3) is a necessity theorem about rankings that judge each variable only by whether its value is its default and whether its own equation produces that value: four uncontroversial cases force a single rule, and a lemma shows that Halpern and Hitchcock's own default must be given up entirely under Halpern's modified definition. The limitative result (§4) turns on a preemption whose backup is a normal process: locusts strip a crop that drought would have killed within the week. Depending on how defaults are coded, this case has the same witness typicality profile either as Gallow's Doorbells switch or as Halpern and Hitchcock's short circuit. Section 5 goes beyond the class with an exactly isomorphic pair whose defaults coincide under every coding; §6 turns to Andreas and Günther; §7 answers objections.

I do not claim that normality is idle, that it has no role in graded causal judgment, or that no richer model can draw the switch/preemption line. The claims concern models in which each route to the effect is an event variable, the format of the switch and preemption models in the literature discussed here.

**Closest work and increment.** Halpern and Hitchcock (2015) state the default that endogenous variables typically obey their equations (p. 19). They make exceptions to it in their treatment of preemption and short circuits (pp. 34–36), and they propose adding variables to remove such exceptions (p. 36). I show that within the class their exceptions are forced and their default is not, that their remedy is unavailable under the modified definition, and that no ranking in the class handles the switch together with normal-backup preemption. Beckers (2026) poses a dilemma for Andreas and Günther: either their verdicts on switches rest on structure alone, or their deviancy condition gives the wrong verdict on early preemption when the backup is not deviant. I show that the same dilemma arises for any account whose verdicts are fixed by equations, actual values and defaults. Hitchcock (2007) supplies the inertial coding and the Principle of Sufficient Reason used in §5. As far as I know the results are new; Halpern's (2016) book, which I have not consulted, may bear on the lemma of §3.

## 2. The setting

**Models.** An acyclic causal model has binary *root* variables, fixed by the context, and *endogenous* variables, each fixed by an equation from its parents. The *actual world* is the solution for the actual context; an intervention $[\vec X\leftarrow\vec x]$ replaces the equations of $\vec X$ by constants.

**Three definitions.** I follow Halpern's (2015, 3–4) statement of the original, updated and modified Halpern–Pearl definitions. $\vec X=\vec x$ is a cause of $\varphi$ if both actually hold (AC1), if a minimality condition holds (AC3), and if there is a *witness*: a setting $\vec x'$ and a set $\vec W$ of other variables with values $\vec w$ such that $[\vec X\leftarrow\vec x',\vec W\leftarrow\vec w]\neg\varphi$ (AC2(a)). The original and updated definitions let $\vec w$ be any values, subject to sufficiency conditions that differ between them (AC2(b) and AC2(b$^u$)). The modified definition requires $\vec w$ to be the actual values: the witness may only freeze variables at what they actually were (AC2(a$^m$)). A conjunct of a cause is *part of* a cause. The *witness world* is the solution under the witness intervention.

**Normality as a filter.** Halpern and Hitchcock (2015, 20–21) add a preorder $\succeq$ on worlds and require, in AC2(a), that the witness world be at least as normal as the actual world. They give two guidelines for it. First, a world in which some variables take more typical values, and none less typical, is more normal; when each world is more typical in some variable, the two are incomparable unless "special considerations" rank them (p. 20). Second, "it is typical for endogenous variables to be related to one another in the way described by the structural equations of a model, unless there is some specific reason to think otherwise", because "the downstream consequences of what is typical are themselves typical" (p. 19). I call this second guideline the *conformity default*.

**Local uniform rankings.** Each variable has a default value. In a given world, an endogenous variable falls into one of four categories:

- $\mathbf n$: default, conforming (its value is the default, and its equation gives that value);
- $\mathbf l$: licensed deviant (its value is deviant, and its equation gives that value);
- $\mathbf f$: frozen default (its value is the default, but its equation demands the deviant value);
- $\mathbf u$: unlicensed deviant (its value is deviant, but its equation demands the default).

A root is either at its default or not, and a root's default is more typical than its deviant value. A *local uniform ranking* is a preorder $\geq$ on $\{\mathbf n,\mathbf l,\mathbf f,\mathbf u\}$, the same for every variable. The witness world passes the filter iff each variable's category there is $\geq$ its category in the actual world, which is Halpern and Hitchcock's first guideline. Three members of the class matter below:

- **Conformity:** $\mathbf n\equiv\mathbf l>\mathbf f,\mathbf u$. This is the conformity default.
- **Value-only:** $\mathbf n\equiv\mathbf f>\mathbf l\equiv\mathbf u$. Typicality depends on values alone. Halpern and Hitchcock (2015, 35) call this way of ranking "prima facie reasonable" for their short circuit before rejecting it.
- **Licence:** $\mathbf l\equiv\mathbf n$, $\mathbf f\geq\mathbf n$, and $\mathbf u\not\geq\mathbf n$. A value is atypical only if it is a deviant value that its own mechanism did not produce.

**Coding defaults.** A default assignment needs a rule. I consider four uniform rules:

- **Event coding:** occurrences are deviant and absences default.
- **Inertial coding:** a self-sustaining state is default and a change is deviant (Hitchcock 2007, 506–507).
- **Normal-course coding:** an endogenous variable's default is the value it takes when every root takes its default value.
- **Normal course given the background:** an endogenous variable's default is the value it takes when the candidate cause takes its default value and every other root keeps its actual value.

The last two implement the idea, which Halpern and Hitchcock (2015, 18) report, of taking "a certain evolution of an 'undisturbed' system to be its default behavior". Event, inertial and the first normal-course coding assign the same defaults in the four cases of §3; they come apart in §4.

All verdicts below were also computed by exhaustive search, for the three definitions, all 75 weak orders on the four categories, each coding rule, and conjunctive causes of up to three conjuncts (Appendix B).

## 3. What normality must do

Four cases, each a textbook verdict, fix the content of normality within the class. Roots are listed with their actual values; every default is 0 under each of the first three coding rules.

> *Genuine prevention.* Roots $P=1$ (poison in the coffee), $A=1$ (antidote). $V=P\wedge\neg A$ (the victim dies). The antidote caused the survival.
>
> *Chain.* Root $C=1$. $I=C$, $Y=I$. $C=1$ caused $Y=1$.
>
> *Boulder.* Root $F=1$ (a boulder falls). $B=F$ (the boulder heads for the hiker), $K=F$ (the hiker ducks), $H=B\wedge\neg K$ (the hiker is hit). The ducking caused the hiker not to be hit. (This is Hitchcock's (2001) case, in the form presented by Andreas and Günther (2024, 18).)
>
> *Short circuit.* Root $A=1$ (a bodyguard adds an antidote). $P=A$ (a second bodyguard, conspiring, adds poison only if the antidote is in), $V=P\wedge\neg A$. The antidote is not a cause of the survival (Halpern and Hitchcock 2015, 34–35; Halpern 2015, Ex. 3.10).

**Theorem 1.** Under event, inertial or normal-course coding (with all roots at default), and for each of the three definitions, a local uniform ranking gives the stated verdicts in all four cases iff $\mathbf l\equiv\mathbf n$, $\mathbf f\geq\mathbf n$ and $\mathbf u\not\geq\mathbf n$. That is, iff it is a licence ranking.

*Proof sketch* (Appendix A). Genuine prevention's witness moves $V$ from $\mathbf n$ to $\mathbf l$, so $\mathbf l\geq\mathbf n$; the chain's moves $I$ and $Y$ from $\mathbf l$ to $\mathbf n$, so $\mathbf n\geq\mathbf l$. The short circuit's only witness keeps the poison in without the antidote ($P$: $\mathbf l\to\mathbf u$; $V$: $\mathbf n\to\mathbf l$) and must fail, so $\mathbf u\not\geq\mathbf n$. The ducking's witness either leaves the hiker not ducking as the boulder falls ($K$: $\mathbf l\to\mathbf f$) or forces the boulder's course against its equation ($B$: $\mathbf l\to\mathbf u$, already excluded), so $\mathbf f\geq\mathbf n$. A licence ranking passes the first, second and fourth witnesses and blocks the third. ∎

Of the 75 weak orders, exactly two satisfy the theorem's conditions: $\mathbf u<\mathbf n=\mathbf l=\mathbf f$ and $\mathbf u<\mathbf n=\mathbf l<\mathbf f$. On a battery of 36 queries in 25 models (Appendix B), both give the standard verdicts under event coding in all three definitions except on Hall's switch and Doorbells (§4) and on one bogus-prevention model, which a neutralization variable corrects, as in Halpern and Hitchcock (2015, 29 fn. 15). Sufficiency is relative to that battery; necessity rests on the four cases alone.

The conformity ranking violates $\mathbf f\geq\mathbf n$, so it denies, under every definition, that the ducking prevented the hit. The value-only ranking violates $\mathbf l\geq\mathbf n$ and denies that the antidote prevented the poisoning. What survives is what Halpern and Hitchcock do in their worked examples, against their stated default. In their preemption example the backup does not poison the drink although its equation says it would. Of the witness world containing this unlicensed absence they write: "It seems natural to take A = 0 and B = 0 to be typical" (2015, 34). This is $\mathbf f\geq\mathbf n$. In the short circuit they exclude the witness because in it the poison variable "depends on A in a less typical way" than in the actual world (p. 36): poison present without the antidote, which is $\mathbf u$. They also note that both treatments involve "an exception to the default assumption that it is typical for endogenous variables to depend on one another in accordance with the structural equations" (p. 36). Theorem 1 says that within the class, the exceptions are forced and the default is not.

Halpern and Hitchcock remove the exception by adding a variable for the poisoner's intentions, so that every witness obeys the equations (p. 36), and ask whether "this kind of maneuver" is always possible (p. 37). For the modified definition, which Halpern (2015, 6) says their extension "applies without change to", the answer is no:

**Lemma (frozen witnesses).** Under the modified definition, let $\vec X=\vec x$ be a cause of $\varphi$ with a witness in which no variable violates its equation. Then every member of $\vec X$ is a root, and $\varphi$ depends counterfactually on $\vec X=\vec x$.

*Proof.* Let $\vec R$ be the root members of the candidate $\vec X$. If the witness violates no endogenous equation, it satisfies all the original endogenous equations; every root outside $\vec R$ retains its actual value, including any frozen root. By acyclicity, uniqueness of solutions therefore makes the witness identical to the solution under $[\vec R\leftarrow\vec r']$ alone. Since the outcome changes, $\vec R$ is nonempty. If $\vec X$ contained an endogenous member, $\vec R$ would be a proper subset satisfying the counterfactual condition with no frozen contingency, contrary to AC3 minimality. Thus every member of the minimal cause is a root, and the outcome changes under its intervention alone. This argument uses minimality; it does not assume that endogenous members of a conjunctive candidate have unchanged parents. ∎

So every witness for a preempting cause or an intermediate event contains a violation, whatever variables are added. With the conformity ranking, no intermediate event is a cause on its own, and in late preemption Billy's throw becomes part of a cause together with Suzy's. An intentions variable cannot help, because the witness may not reset it. Under the modified definition, within the local uniform class, normality filtering can coexist with the stated preemption verdicts only if frozen defaults are typical *as such*, which is the licence rule's $\mathbf f\geq\mathbf n$, and not as a local exception.

## 4. What normality cannot do

Consider first a preemption whose backup is a normal process.

> *Locusts.* It is the dry season. Roots: $S=1$ (a locust swarm arrives), $Q=0$ (rain falls). $D=\neg Q\wedge\neg S$: unwatered and uneaten, the maize dies of drought within the week. $X=S\vee D$: the maize is destroyed. Actually, $D=0$ and $X=1$. The swarm destroyed the maize.

Except for the normality of the backup, this is early preemption. Without normality, every account considered here counts the swarm a cause: the three definitions, NESS and CNESS (Beckers 2021), and Andreas and Günther's (2024) preliminary definition. If the backup gets a deviant trigger of its own (a failed irrigation pump, say), all of them count it a cause with normality too (Appendix B).

Now a switch in which neither route is a standing state.

> *Doorbells* (Gallow 2021, 84–86). Roots: $M=1$ (Marty presses the button), $T=1$ (Doc has set the switch to the right). $L=M\wedge\neg T$ (the left bell rings), $R=M\wedge T$ (the right bell rings), $E=L\vee R$ (Einstein barks). Actually, $L=0$, $R=1$, $E=1$. The switch-setting was not a cause of the barking.

Gallow's verdict is that "Doc's flipping the switch to the right was (along with Marty's pressing the button) a cause of the right bell's ringing, but it was not a cause of Einstein's barking" (2021, 85). His model uses a four-valued switch variable; the binary model is my simplification, in the usual format of one event variable per route.

**Theorem 2.** Fix any local uniform ranking and any of the three definitions. (a) Under event or inertial coding, $T=1$ is part of a cause of $E=1$ in Doorbells iff $S=1$ is part of a cause of $X=1$ in Locusts. (b) Under either normal-course coding, $S=1$ is part of a cause of $X=1$ in Locusts iff $A=1$ is part of a cause of $V=0$ in the short circuit. Hence no ranking in the class, under any of the four coding rules, gives all three standard verdicts.

*Proof.* (a) Under event and inertial coding every endogenous variable in both models defaults to 0 (silence and survival are standing states; ringing and dying are changes). The modified witness for the switch-setting is $[T\leftarrow0, L\leftarrow0]$, which freezes the left bell silent although the button is pressed. Relative to the actual world, $L$ moves from $\mathbf n$ to $\mathbf f$, and $R$ and $E$ move from $\mathbf l$ to $\mathbf n$. The witness for the swarm is $[S\leftarrow0, D\leftarrow0]$, which freezes the maize alive although nothing kills it any more and it has no water. $D$ moves from $\mathbf n$ to $\mathbf f$, and $X$ from $\mathbf l$ to $\mathbf n$. Both pass iff $\mathbf f\geq\mathbf n$ and $\mathbf n\geq\mathbf l$. The further witnesses that the original and updated definitions allow either make it rain (a root moved to its deviant value) or cancel the press (violating sufficiency); see Appendix A.

(b) Under either normal-course coding the drought death is the default: with the swarm absent and no rain, $D=1$ and $X=1$. Actually, $D$ is a licensed deviant ($\mathbf l$) and $X$ is $\mathbf n$. In the witness, $D$ becomes $\mathbf u$ (alive, against an equation that now demands death) and $X$ becomes $\mathbf l$. In the short circuit, under every coding, the antidote's witness moves $P$ from $\mathbf l$ to $\mathbf u$ and $V$ from $\mathbf n$ to $\mathbf l$. Both pass iff $\mathbf u\geq\mathbf l$ and $\mathbf l\geq\mathbf n$.

Machine search confirms both parts for all 75 weak orders and all three definitions, including conjunctive causes. ∎

Theorem 2 assumes nothing about which ranking is correct. For the licence rule it means: under event or inertial coding, both the swarm and the switch-setting are causes; under normal-course coding the swarm is not. (Under the modified definition the switch-setting's witness also has the profile of Suzy's in late preemption.) The remaining exits are non-uniform rankings or codings (§5).

**Table 1.** Verdicts under the modified definition ("C" = cause or part of a cause; the original and updated definitions agree except where noted). Verdicts that depart from the standard one are marked \*.

| Case (standard verdict) | Licence, event | Licence, inertial | Licence, normal course | Conformity, any coding | Value-only, event |
|---|---|---|---|---|---|
| Genuine prevention (C) | C | C | C | C | not\* |
| Boulder: ducking (C) | C | C | C | not\* | not\* |
| Short circuit (not) | not | not | not | not | not |
| Late preemption: Billy (not) | not | not | not | C\* (modified only) | not |
| Locusts (C) | C | C | not\* | not\* | C |
| Doorbells (not) | C\* | C\* | C\* / not | not | C\* |
| Hall's LT/RT switch (not) | C\* | not | not | not | C\* |

In the Doorbells row the normal-course codings differ: with all roots at default no bell is due to ring ("C\*"); given the actual press, the left bell's ringing is the default ("not").

The table shows what Halpern's (2015, 8) treatment of the switch requires, in the LT/RT model he attributes to Hall (2007). Halpern says that in the LT/RT model "the world where the train does not go on the left track despite the switch being set to the left is less normal than the actual world". If the left-track travel is coded as an event, this penalizes a frozen default ($\mathbf f<\mathbf n$), which Theorem 1 rules out; if the left track is the train's inertial course, it is the licence rule's $\mathbf u$-penalty. The charitable reading is the inertial one, and Doorbells defeats it: a ringing bell is never a standing state, so no uniform coding makes the untaken route the default without making the drought death the default too. (According to Beckers (2026, 10), Halpern (2016) continues to give the switch a normality-based treatment; my claims concern the 2015 statement.)

## 5. Beyond the class: an isomorph with identical defaults

Halpern and Hitchcock do not commit to the class (2015, 26 fn. 13; 36 fn. 18). The obvious non-local repair looks at a mechanism's inputs: a frozen default is atypical only when some parent of the frozen variable takes a deviant value. This has a pedigree in Hitchcock's (2007, 508) Principle of Sufficient Reason, which says that a variable with parents takes a default value whenever all its parents do; a deviant value needs a deviant source. The drought equation $D=\neg Q\wedge\neg S$ violates that principle under event coding, since a deviant death follows from all-default parents, whereas the left bell's equation does not. This *trigger rule* penalizes the frozen left bell (its parent, the press, is deviant) but not the frozen maize. With the candidate's own value exempted and the train's left-track travel coded inertially, the trigger rule gives the standard verdict on every case in Table 1 under the original and updated definitions. (Under the modified definition it errs on Billy's throw and on the switch.)

But Hitchcock's principle also tells us how to repair the drought model. A deviant death needs a deviant source, and the obvious one is that the crop is there to die. Make it explicit:

> *Seedlings.* A field was sown this morning. Roots: $P=1$ (the field is sown), $S=1$ (a swarm arrives); it is a dry week, and no rain is possible. $G=P\wedge S$ (the swarm strips the seedlings), $D=P\wedge\neg S$ (the seedlings die of drought within the week), $X=G\vee D$ (the seedlings are destroyed). Actually, $G=1$, $D=0$, $X=1$. The swarm destroyed the seedlings.

The map $P\mapsto M$, $S\mapsto T$, $G\mapsto R$, $D\mapsto L$, $X\mapsto E$ is an isomorphism from Seedlings onto Doorbells. It preserves equations and actual values. It also preserves default assignments under each of the four coding rules:

- Under event and inertial coding, the sowing and the press are actions and so deviant, and every endogenous variable defaults to 0.
- Under normal-course coding with all roots at default, nothing is sown and nothing is pressed, so again every endogenous variable defaults to 0.
- Given the actual background, the drought death and the left bell's ringing are both defaults, and so are the destruction and the barking.

**Proposition 1.** Any account whose verdicts depend only on the equations, the actual values and the default assignment (not on what the variables are called) gives the swarm in Seedlings and the switch-setting in Doorbells the same verdict, under each of the four coding rules.

The proof is immediate; the interest lies in the pair. Seedlings satisfies Hitchcock's principle, and it is no less a case of a deviant event preempting a normal process. The computed verdicts bear the proposition out: the trigger rule says neither is a cause, the licence rule says both are (or, given the actual background, neither), both of Andreas and Günther's deviancy conditions say neither, and NESS and CNESS say both.

A default-based account can separate the pair only by coding the shared enabling condition differently in the two cases. That does not track the contrast, which survives when the condition is coded alike. Let a postman press the button every noon, so that the press is statistically normal: a switch that diverts a routine signal is still a switch, yet under the trigger rule the switch-setting is now a cause, exactly as the swarm is when the crop is a standing one (Appendix B).

## 6. Regularity theories

Andreas and Günther's (2024) final theory counts $c$ a cause of $e$ only if, among other conditions, every root proposition left out of a maximal set of facts that does not by itself entail the effect is "more deviant than" its negation (their condition (4), p. 13). In their later definition, as Beckers (2026, 3–4) states it, the condition is restricted to literals whose variables are neither ancestors nor descendants of the candidate (C5). Beckers (2026, 9–11) gives the decisive case against both. In *Backup 2* a trainee surgeon operates while a supervisor, as a moral norm requires, stands ready to operate if she does not, and the deviancy definitions "force us to conclude that trainee's action did not cause the outcome" (p. 11). Beckers also proves their 2025 definition equivalent to a 2024 one (Thm. 2.2), so the verdict reaches their current account. The counterexample and the equivalence are Beckers's; I add that no moral norm is needed, and a condition that predicts the failure:

**Proposition 2.** Let $N$ be a set of actual root literals, none more deviant than its negation, which together with the equations of $C$'s descendants entails $E$. Then $C$ is not a cause of $E$ under condition (4). If, in addition, no member of $N$ is an ancestor of $C$, then $C$ is not a cause of $E$ under (C5).

*Proof.* Both definitions require the equations of all of $C$'s descendants to be among the laws used (their condition (5), Beckers's (C4)). Those laws, together with any set of facts that contains $N$, entail $E$, so the maximal non-entailing set of facts must omit some $n\in N$. That $n$ is a root, and it is not more deviant than its negation, so it violates (4). If it is not an ancestor of $C$, it also violates (C5), because roots are never descendants. ∎

In Locusts, $N=\{\neg Q\}$: with no rain, the laws of $D$ and $X$ yield $X\leftrightarrow S\vee\neg S$. The absence of rain is statistically normal, violates no norm, and is an absence: normal by each of Andreas and Günther's criteria. The only way out is to call the drought an occurring event. Andreas and Günther themselves ask: "Is, for example, the death of a plant an occurring event, or rather the absence of continued living?" (2024, 27). But the same relabelling, applied to the poison-free coffee, would undo their treatment of bogus prevention (pp. 13–14). And Proposition 1 closes off a third horn of Beckers's dilemma: Seedlings and Doorbells are one model, so on any default assignment a theory that gets the switch right gets the swarm wrong.

## 7. Objections and replies

**Objection 1: flexibility.** Halpern and Hitchcock offer "a flexible framework that can be used to represent a variety of factors" (2015, 26 fn. 13), not a rule. They allow cross-variable comparisons when "special considerations" warrant them (p. 20), and in their dam footnote they let a variable's typical behavior come apart from its equation (p. 36 fn. 18). Results about local uniform rankings do not bind them.

*Reply.* Theorem 1 says what the *default* must be if exceptions are to remain exceptions; the default Halpern and Hitchcock state is the one their own examples contradict, and under the modified definition (the lemma) the contradiction is universal. Against flexible orderings, Proposition 1 is the relevant result: any ordering computed from the model and its defaults treats Seedlings and Doorbells alike. An ordering that separates them must use information outside the model, such as that locust swarms are rarer than maize surviving a dry week, and then whether these locusts destroyed this maize turns on a comparison of base rates nobody consults in judging it. That concedes my conclusion: the distinguishing work is done outside normality as the framework represents it.

**Objection 2: aptness.** The binary route models are inapt. Halpern (2015, 7–8) gets the switch right in a three-variable model where the track variable makes no difference to arrival. Seedlings could be modelled the same way, with a single "destroyed by some route" mechanism, or with a finer-grained effect variable.

*Reply.* I accept the conclusion and draw out its cost. If switch verdicts come from model choice, Halpern's normality treatment of the LT/RT model is idle, or, read as penalizing frozen defaults, inconsistent with Theorem 1. And the aptness criterion must sort Seedlings from Doorbells. The most promising candidate is the grain of the effect. The maize stripped on the third day is not the event that drought would have produced days later, whereas the bark is the same whichever bell rings. With a finer effect variable the swarm is a but-for cause, and the case leaves the scope of normality altogether. Gallow's (2021, 85) own Doorbells model shows a second option. It uses one multi-valued switch variable and assumes that "being set to the left is no less normal than being set to the right", and the relative deviance of the routes becomes a parameter. Whether such a parameter can be set without reading it off the verdicts is a question my results leave open. Either way, the line is drawn by the choice of variables, not by the defaults of the route-variable models.

**Objection 3: the verdicts.** Perhaps the swarm is not a cause, since the destruction was coming anyway. Alternatively, with transitivity theorists, perhaps Doc's switch-setting is a cause of the barking.

*Reply.* The swarm verdict is plausible when the narrative fixes the swarm as the process that actually destroys the maize before drought would have done so. A theorist can dispute that verdict or argue that the equations omit precisely this timing and process information. That is a substantive response, not a contradiction. The results are conditional: if these contrasting judgments are retained while the represented features are held fixed, a default-only filter cannot recover the contrast. An account that accepts causation by the switch avoids that particular demand. Richer process representations remain open.

**Objection 4: triviality.** Proposition 1 follows from isomorphism, and Theorem 2 rests on one or two comparisons.

*Reply.* That is what a normality isomorph is. Bogus prevention and overdetermination differ in which variables are at their defaults, which is why normality could separate them. What is new is a pair of recognized paradigms that agree in their defaults under every principled coding. The pair marks the boundary: normality separates isomorphs only when they differ in some variable's default status, and within the class it does so by a licence rule.

## 8. Conclusion

Within the local uniform rankings, standard verdicts force the licence rule and exclude Halpern and Hitchcock's conformity default, which under the modified definition fails for every non-but-for cause. No ranking in the class, under any of the four specified codings, gets Doorbells, Locusts and the short circuit right together. No default-based account at all separates Seedlings from Doorbells.

I have not shown that normality is idle: genuine prevention, bogus prevention and short circuits remain its legitimate work. I have not shown that richer models cannot draw the switch/preemption line. What follows is a division of labor. Normality supplies a licence requirement on deviant values; the switch/preemption contrast belongs to the choice of variables, and in particular to the grain of the effect. Accounts that rest the contrast on normality, whether through Halpern and Hitchcock's ordering or through Andreas and Günther's deviancy condition, owe a different account of it.

## Appendix A. Proofs

**Theorem 1, witness enumeration.** In genuine prevention, a witness for $A=1$ sets $A=0$, possibly with $P$ fixed at 1. The world is $(P,A,V)=(1,0,1)$: $A$ is at its default, $P$ is unchanged, and $V$ moves from $\mathbf n$ to $\mathbf l$. In the chain, the only witness for $C=1$ is $[C\leftarrow0]$, under which $I$ and $Y$ move from $\mathbf l$ to $\mathbf n$; fixing $I$ or $Y$ at 1 restores $Y=1$.

In the short circuit, $[A\leftarrow0]$ alone gives $P=0$ and $V=0$, so it is not a witness. The only witness is $[A\leftarrow0,P\leftarrow1]$, with world $(1,0,1)$ for $(A,P,V)$; $P$ moves from $\mathbf l$ to $\mathbf u$ and $V$ from $\mathbf n$ to $\mathbf l$. It is admitted iff $\mathbf u\geq\mathbf l$ and $\mathbf l\geq\mathbf n$.

In the boulder case, $\neg\varphi$ requires $B=1$ and $K=0$. With $F=1$ the world is $(F,B,K,H)=(1,1,0,1)$: $K$ moves from $\mathbf l$ to $\mathbf f$, $B$ stays $\mathbf l$, and $H$ moves from $\mathbf n$ to $\mathbf l$. With $F$ set to 0, $B$ must be set to 1, giving $(0,1,0,1)$: $B$ moves from $\mathbf l$ to $\mathbf u$, $K$ moves from $\mathbf l$ to $\mathbf n$, and $H$ from $\mathbf n$ to $\mathbf l$. Setting $H$ itself violates sufficiency. The four verdicts therefore hold iff (i) $\mathbf l\geq\mathbf n$, (ii) $\mathbf n\geq\mathbf l$, (iii) not both $\mathbf u\geq\mathbf l$ and $\mathbf l\geq\mathbf n$, and (iv) either $\mathbf f\geq\mathbf l$ and $\mathbf l\geq\mathbf n$, or $\mathbf u\geq\mathbf l$ and $\mathbf l\geq\mathbf n$. By (i) and (ii), $\mathbf l\equiv\mathbf n$; then (iii) gives $\mathbf u\not\geq\mathbf n$, and (iv) reduces to $\mathbf f\geq\mathbf n$.

The modified definition admits only the first boulder witness, and the conditions are the same. Partial preorders are covered, since only the listed comparisons occur. All four candidates are single conjuncts; conjunctive candidates were checked by machine.

**Theorem 2, remaining witnesses.** In Locusts, original and updated definitions: a witness setting $Q=1$ moves a root to its deviant value and fails; setting $D=0$ gives the modified witness, and $D=1$ gives $X=1$. In Doorbells a witness must keep $M=1$, since with $M=0$ restoring $T=1$ does not restore the barking (AC2(b)); then $\neg\varphi$ requires $L=0$, the modified witness. Conjunctive candidates contain a smaller cause or fail the same comparisons (checked by machine for weak orders).

## Appendix B. The computation

The code (Python, standard library only) implements the three definitions as stated by Halpern (2015, 3–4); Halpern and Hitchcock's filter with componentwise comparison; NESS and CNESS (Beckers 2021); Andreas and Günther's (2024) definitions with condition (4); and the variant with (C5) in Beckers's (2026, 3–4) statement. Without normality it reproduces Halpern's (2015) verdicts in Examples 3.3, 3.4, 3.9 (LT/RT model) and 3.10, and it reproduces Andreas and Günther's (2024, 28–29) table. For each coding rule and each of the 75 weak orders it evaluates 36 queries in 25 models.

Main outputs: (1) under event coding, the orders correct on Theorem 1's four cases are exactly the two licence orders, for each definition; (2) {Doorbells, Locusts} (event coding) and {Locusts, short circuit} (both normal-course codings) are unsatisfiable for each definition; (3) Seedlings and Doorbells receive identical verdicts under every coding, for the licence, conformity, value-only and trigger rankings, both deviancy conditions, NESS and CNESS, also when the shared condition is coded default; (4) the trigger rule, with the candidate exempted and the train's track coded inertially, errs under the original and updated definitions only on Seedlings and a planted variant of Locusts; (5) both deviancy conditions deny causation in Locusts, with or without the planting and in a late-preemption form, and grant it when the backup has its own deviant trigger; (6) in 41 random models meeting Proposition 2's hypothesis neither deviancy condition counts the candidate a cause; (7) in 423 random cases every modified-definition witness for a non-but-for or endogenous candidate contains an equation violation.

## References

Andreas, Holger, and Mario Günther. 2024. "A Regularity Theory of Causation." *Pacific Philosophical Quarterly* 105 (1): 2–32. https://doi.org/10.1111/papq.12447.

Beckers, Sander. 2021. "The Counterfactual NESS Definition of Causation." *Proceedings of the AAAI Conference on Artificial Intelligence* 35 (7): 6210–6217. https://doi.org/10.1609/aaai.v35i7.16772.

Beckers, Sander. 2026. "Difference-Making without Making a Difference." Preprint, arXiv:2606.24832v1.

Gallow, J. Dmitri. 2021. "A Model-Invariant Theory of Causation." *Philosophical Review* 130 (1): 45–96. https://doi.org/10.1215/00318108-8699682.

Hall, Ned. 2007. "Structural Equations and Causation." *Philosophical Studies* 132 (1): 109–136. https://doi.org/10.1007/s11098-006-9057-9.

Halpern, Joseph Y. 2015. "A Modification of the Halpern–Pearl Definition of Causality." Preprint, arXiv:1505.00162v1. (Page references are to this version.)

Halpern, Joseph Y. 2016. *Actual Causality*. Cambridge, MA: MIT Press.

Halpern, Joseph Y., and Christopher Hitchcock. 2015. "Graded Causation and Defaults." *British Journal for the Philosophy of Science* 66 (2): 413–457. https://doi.org/10.1093/bjps/axt050. (Page references are to arXiv:1309.1226.)

Hitchcock, Christopher. 2001. "The Intransitivity of Causation Revealed in Equations and Graphs." *Journal of Philosophy* 98 (6): 273–299. https://doi.org/10.2307/2678432.

Hitchcock, Christopher. 2007. "Prevention, Preemption, and the Principle of Sufficient Reason." *Philosophical Review* 116 (4): 495–532. https://doi.org/10.1215/00318108-2007-012.

