# A Switching Dilemma for Normality in Actual Causation

**Abstract.** Normality conditions are a standard way of stopping the Halpern–Pearl definitions of actual causation from counting the flip of a switch as a cause. I prove that one transferable normality policy cannot do this under any of the three definitions. Suppose occurrences are deviant and absences default, and a world's normality depends only on how each variable's status changes, whatever the variable represents. Under the modified definition, the only witness for Suzy's preempting throw has exactly the profile of the witnesses for two standard switches, so every such policy counts all three or none. Under the original and updated definitions, the witness for a switch with both tracks blocked is the witness for genuine prevention plus one more default-restoring change, so every such policy that respects Pareto improvement and keeps prevention counts the flip. Within these codings, a separating Pareto filter must use information beyond the transition profile. I examine one additive repair based on mechanism reliability and prove that, in fixed-context acyclic models, exceptionless equation-conformity leaves only root but-for causes.

## 1. Introduction

The Halpern–Pearl (HP) definitions count Suzy's throw a cause of the bottle's shattering, although Billy's rock would have shattered it anyway, by evaluating the shattering in a contingency that holds part of the background fixed. The same machinery threatens to make an engineer's flip of a switch a cause of a train's arrival, when the train would have arrived by the other track. The two cases can have isomorphic patterns of counterfactual dependence, and a prominent response distinguishes them by normality: a contingency may witness causation only if the world it produces is at least as normal as the actual world (Halpern and Hitchcock 2015, 20–21). Halpern (2015, 8) handles one model of the switch this way. Normality earns its place if it marks a real difference between switching and preemption, and not just the difference between the verdicts we want.

This essay asks whether one normality policy, applied the same way in every model, can do this. Call a policy *anonymous* if it ranks a witness world by how each variable's status changes (default or deviant, conforming to its equation or not), whatever the variable represents. My thesis is that, when occurrences are coded deviant and absences default, *no anonymous normality filter that respects Pareto improvement keeps genuine prevention and late preemption while excluding every switch, under any of the three HP definitions*. The modified definition fails on two switches because its restriction to actual-value contingencies leaves Suzy only a witness whose profile is identical to theirs. The original and updated definitions fail on a switch with both tracks blocked because the contingency that convicts the flip improves on the one that makes an antidote a cause.

The thesis does not say that normality cannot separate switches from preemption. Under the maintained models and coding, a separating Pareto filter must use information beyond the transition profile. Section 5 examines one additive repair: treating Billy's thrown rock failing to hit as more normal than a pressed bell failing to ring, while holding the other scoring contributions fixed. This is not the only possible non-anonymous repair. Graded and event-based variants lie outside the filter theorem.

**Closest work and increment.** Halpern (2015, 7–8) reports a problem he credits to Schumacher: with both tracks blocked, the original and updated definitions count the flip a cause of non-arrival, and "normality considerations don't help". He notes that the modified definition avoids it. Xiao and Xiong (2026, 4–5, Observation 1) show the same for the Halpern–Hitchcock definition. Halpern (2016, Example 3.2.6, 84–85) observes that if the witness in which Billy throws but does not hit is too abnormal, Suzy's throw ceases to be a cause under the modified definition and the two throws together become one. Beckers (2026, 2, 10–11) argues for a dilemma of related shape for the regularity theory of Andreas and Günther (2024), discussed in Section 7. The increment here is (i) an exact identity of witness profiles across late preemption and two switches under the modified definition, which covers every anonymous filter at once; (ii) an exact identity linking the both-blocked switch to genuine prevention under the older definitions; (iii) the resulting dilemma across all three definitions; (iv) the assessment of a particular non-anonymous escape; and (v) a lemma showing what exceptionless conformity costs, applied to a conjecture of Halpern and Hitchcock (2015, 37) and to the recent definition of Xiao and Xiong (2026).

Wysocki (2023, §§4–5) gives a stronger obstruction in another setting: conjoined cases can share one witness world while requiring opposing causal verdicts, so no normality ordering of that world can separate them. His cases cover both updated and modified definitions. The present theorem does not improve that general impossibility claim. It compares profiles across standard, uncombined models under an explicit anonymity restriction, and relates the switch-preemption tradeoff across all three HP definitions to a root-transition identity. Its value depends on whether these transferable policies are a useful baseline, not on being the first demonstration that normality can fail.

**Why it matters.** Schumacher's case is among those Halpern (2015, 8) presents as handled better by the modified definition. The present comparison shows how that improvement trades one difficulty for another under a transferable policy. It identifies where information beyond default status and equation conformity must enter. Such information may be principled; the theorem does not establish that a non-anonymous theory merely encodes desired verdicts. It provides a controlled test for proposed grounds of the distinction.

## 2. The setting

**Models.** An acyclic causal model has binary variables. A *root* has no parents among the modeled variables and takes its actual value from the context; a *non-root* has an equation in its parents. The *actual world* is the solution for the actual context; an intervention $[\vec X\leftarrow\vec x]$ replaces the equations of $\vec X$ by constants.

**Three definitions.** I follow Halpern's (2015, 3–4) statement of the original, updated and modified HP definitions. $\vec X=\vec x$ is a cause of $\varphi$ if both actually hold (AC1), no proper subset of $\vec X$ satisfies the conditions (AC3), and there is a *witness*: a setting $\vec x'$ and a set $\vec W$ of other variables with values $\vec w$ such that $[\vec X\leftarrow\vec x',\vec W\leftarrow\vec w]\neg\varphi$. The original and updated definitions let $\vec w$ be any values, subject to sufficiency conditions (AC2(b), AC2(b$^u$)). The modified definition requires $\vec w$ to be the actual values: it may only freeze variables at what they actually were. A conjunct of a cause is *part of* a cause. Unless I say otherwise, "$X=x$ is a cause" below means that the single candidate $X=x$ is. The *witness world* is the solution under the witness intervention.

**The filter.** Halpern and Hitchcock (2015, 20–21) require a witness world to be at least as normal as the actual world. Their "rough-and-ready guidelines" (20) make a world more normal if some variables take more typical values and none take less typical ones, and leave worlds incomparable when some improve and others worsen, unless special considerations rank them. They also treat it as typical, by default, for endogenous variables to obey their equations (19), and they argue that typicality must sometimes reflect how a variable depends on its parents, not just its value (35).

**Categories.** These guidelines suggest four categories for a non-root variable in a world, given a default value for each variable:

- $\mathbf n$: default, conforming (its value is the default, and its equation gives that value);
- $\mathbf l$: licensed deviant (its value is deviant, and its equation gives that value);
- $\mathbf f$: frozen default (its value is the default, but its equation demands the deviant value);
- $\mathbf u$: unlicensed deviant (its value is deviant, but its equation demands the default).

A root is at its default or not. A witness's *profile* is the multiset of transitions (actual category to witness category) of the variables whose category changes.

**Anonymous filters.** A filter is *anonymous* if whether it admits a witness depends only on the witness's profile. It is *Pareto* if adding to an admitted profile one root that moves from deviant to default yields an admitted profile; this is Halpern and Hitchcock's first guideline applied across models. Two classes illustrate the definition. A *componentwise* filter fixes a preorder $\succeq$ on $\{\mathbf n,\mathbf l,\mathbf f,\mathbf u\}$, counts a root's default as more typical than its deviant value, and admits a witness iff every variable's witness category is $\succeq$ its actual category. An *additive* filter scores a world as the sum of its variables' scores, $r>0$ for a root at default and 0 otherwise, and $a,b,c,d$ for a non-root in $\mathbf n,\mathbf l,\mathbf f,\mathbf u$; it admits a witness iff the witness world's total is at least the actual total. Unlike componentwise filters, additive ones allow gains in some variables to compensate for losses in others. Both classes are anonymous and Pareto.

Anonymity is a baseline, not a characterization of every principled policy. Its categories use Halpern and Hitchcock's two defaults, typical values and equation conformity. Halpern's compact representations likewise supply default typicalities while allowing exceptions and cross-variable comparisons (2016, 149–150). The theorem tests what the baseline can accomplish without those additional distinctions. A failure identifies information that a richer policy must supply; it does not by itself discredit that information.

**Event coding.** Occurrences are deviant and absences default, as in Andreas and Günther's (2024, 26) prima facie rule that "occurring events are prima facie more deviant than their absences". Every variable below has default 0.

## 3. The cases

Roots are listed with their actual values.

> *Genuine prevention.* $P=1$ (poison in the coffee), $A=1$ (antidote). $V=P\wedge\neg A$ (the victim dies). The antidote caused the survival.
>
> *Chain.* $C=1$; $I=C$, $Y=I$. $C=1$ caused $Y=1$.
>
> *Boulder* (Hitchcock 2001, in the form of Andreas and Günther 2024, 18). $F=1$ (a boulder falls); $B=F$ (it heads for the hiker), $K=F$ (the hiker ducks), $H=B\wedge\neg K$ (the hiker is hit). The ducking caused the hiker not to be hit.
>
> *Short circuit* (Halpern and Hitchcock 2015, 34–35). $A=1$ (a bodyguard adds antidote); $P=A$ (a second bodyguard adds poison only if the antidote is in), $V=P\wedge\neg A$. The antidote is not a cause of the survival.
>
> *Late preemption.* $ST=1$, $BT=1$ (Suzy and Billy throw); $SH=ST$, $BH=BT\wedge\neg SH$ (whose rock hits), $BS=SH\vee BH$ (the bottle shatters). Suzy's throw caused the shattering; Billy's did not.
>
> *Tracks* (the switch story of Hall 2000, in Hall's 2007 route model as presented by Halpern 2015, 8). $F=1$ (the engineer flips the switch to the right); $LT=\neg F$, $RT=F$ (the train goes left, right), $A=LT\vee RT$ (it arrives). The flip is not a cause of the arrival.
>
> *Doorbells* (Gallow 2021, 84–85). $M=1$ (Marty presses the button), $T=1$ (Doc has set the switch to the right); $L=M\wedge\neg T$, $R=M\wedge T$ (the left, right bell rings), $E=L\vee R$ (Einstein barks). Gallow's verdict: "Doc's flipping the switch to the right was (along with Marty's pressing the button) a cause of the right bell's ringing, but it was not a cause of Einstein's barking" (85).
>
> *Blocked tracks* (Halpern 2015, 7–8; Xiao and Xiong 2026, 4). $EF=1$ (the engineer flips the switch to the right), $LB=1$, $RB=1$ (both tracks are blocked); $TA=(EF\wedge\neg RB)\vee(\neg EF\wedge\neg LB)$ (the train arrives). Actually $TA=0$. The flip is not a cause of the non-arrival.

Gallow models Doorbells with a single many-valued switch variable; the binary route model is mine, in the format of Tracks. Without normality, every definition counts every candidate above a cause or part of a cause, including the three switches and the short-circuit antidote.

## 4. The dilemma

**Theorem 1 (modified definition).** Under event coding and the modified definition, Suzy's throw in late preemption, the flip in Tracks and the switch-setting in Doorbells each have exactly one witness world, and the three witness profiles are identical:
$$\{\text{root: deviant}\to\text{default},\ \mathbf n\to\mathbf f,\ \mathbf l\to\mathbf n,\ \mathbf l\to\mathbf n\}.$$
Hence every anonymous filter admits all three witnesses or none.

*Proof.* A modified witness may freeze variables only at their actual values. For Suzy, freezing $SH$ or $BS$ at 1 restores the shattering, so the only witness world is that of $[ST\leftarrow0, BH\leftarrow0]$: $ST$ returns to default; $SH$ and $BS$ move from $\mathbf l$ to $\mathbf n$; $BH$ moves from $\mathbf n$ to $\mathbf f$, since Billy's rock, thrown and no longer preempted, is held at not hitting; $BT$ is unchanged. For Tracks, the only witness world is that of $[F\leftarrow0, LT\leftarrow0]$: $F$ returns to default, $LT$ moves from $\mathbf n$ to $\mathbf f$ (the train is held off the left track although the switch is set left), and $RT$ and $A$ move from $\mathbf l$ to $\mathbf n$. For Doorbells, it is that of $[T\leftarrow0, L\leftarrow0]$: $T$ returns to default, $L$ moves from $\mathbf n$ to $\mathbf f$, $R$ and $E$ from $\mathbf l$ to $\mathbf n$; $M$ is unchanged. ∎

If the filter admits the common profile, both switch-settings are causes. If it excludes it, Suzy's throw is not a cause by itself. Computation over all 355 preorders on the four categories confirms that, for componentwise filters, Suzy's throw is a cause exactly when each switch-setting is part of a cause; and in every preorder that leaves Suzy's throw part of a cause only through a conjunction, the conjunction includes Billy's throw, which becomes part of a cause. This is the structure Halpern (2016, 84–85) identified for late preemption; Theorem 1 shows that the escape from it is the switching verdict.

The calibrating cases already force the common profile. In a componentwise filter, genuine prevention requires $\mathbf l\succeq\mathbf n$, the chain $\mathbf n\succeq\mathbf l$, and Boulder's only modified witness (the hiker held not ducking as the boulder falls: $K$ from $\mathbf l$ to $\mathbf f$, $H$ from $\mathbf n$ to $\mathbf l$) requires $\mathbf f\succeq\mathbf l$; so $\mathbf f\succeq\mathbf n$, and the common profile passes. The short circuit adds $\mathbf u\not\succeq\mathbf n$. Exactly five of the 355 preorders, two of them total orders, give all four calibrating verdicts, under each definition. For additive filters the witness gains (witness total minus actual total) satisfy
$$g_{\text{Doorbells}}=g_{\text{Tracks}}=g_{\text{Suzy}}=r+a-2b+c=(r+2a-2b)+(c-a)=g_{\text{Chain}}+g_{\text{Boulder}},$$
because a frozen default's change $\mathbf n\to\mathbf f$ telescopes into $\mathbf n\to\mathbf l$ and $\mathbf l\to\mathbf f$. Compensation therefore does not help: any additive score that keeps the chain and the ducking counts both switches.

**Theorem 2 (original and updated definitions).** Under event coding and the original or updated definition, the flip in Blocked tracks has the witness $[EF\leftarrow0, LB\leftarrow0]$, whose profile is that of genuine prevention's witness plus one root moving from deviant to default. Hence every anonymous Pareto filter that makes the antidote a cause makes the flip a cause of the non-arrival. For additive filters, $g_{\text{Blocked}}=g_{\text{Prevention}}+r$; a componentwise filter admits the flip's witness iff $\mathbf l\succeq\mathbf n$.

*Proof.* The antidote's witness $[A\leftarrow0]$ returns $A$ to default and moves $V$ from $\mathbf n$ to $\mathbf l$; $P$ is unchanged. In Blocked tracks the actual world is $(EF,LB,RB,TA)=(1,1,1,0)$ and the witness world $(0,0,1,1)$: $EF$ and $LB$ return to default, $RB$ is unchanged, and $TA$ moves from $\mathbf n$ to $\mathbf l$ (the train arrives, as its equation now demands). Sufficiency holds: restoring $EF=1$, with or without $LB=0$, gives $TA=0$, since the right track is blocked. The gains are $r+b-a$ and $2r+b-a$. ∎

Under the modified definition the flip has no witness of its own, since no blockage may be cleared; Halpern (2015, 8) notes that with that definition "this becomes a non-problem". Strictly, the flip remains part of a cause: the conjunction of the flip and the left blockage has as witness the world in which both are undone, which is the world of Theorem 2, so every anonymous Pareto filter that keeps the antidote admits it (for componentwise filters, exactly when $\mathbf l\succeq\mathbf n$; computed). Whether this matters depends on whether parts of causes are counted as causes. I set it aside and state the dilemma for single candidates.

**Corollary (the dilemma).** Under event coding, no anonymous Pareto filter makes the antidote and Suzy's throw causes, leaves Billy's throw out of every cause, and makes neither switch-setting nor either flip in Tracks and Blocked tracks a cause, under any of the three definitions.

Under the modified definition this is Theorem 1; under the older definitions it is Theorem 2. An exhaustive check over all 355 componentwise preorders, with candidates of every size and AC3 applied after filtering, finds no exception under any definition; a check of 3,000 random additive scores finds none either (Appendix).

Theorem 1 does not hold for the older definitions, and the reason locates the dilemma. They give Suzy a second witness, $[ST\leftarrow0, BT\leftarrow0]$, which resets Billy's throw to its default; every variable in it improves or stays put, so any Pareto filter that keeps the chain admits it. The switch-settings in Tracks and Doorbells have no such witness: in Doorbells, cancelling the press violates sufficiency. So the older definitions can exclude the switching witnesses while keeping Suzy. The score $(r,a,b,c,d)=(2,0,-1,-5,-3)$ does exactly this under both older definitions and also keeps prevention, the chain and the ducking. But it counts the flip in Blocked tracks, and in Halpern's model with clear tracks (via $[F\leftarrow0,LB\leftarrow1]$, gain $a-b$).

The witness that rescues Suzy under the older definitions and the witness that convicts the flip are the same kind of move: a deviant root, Billy's throw or a blockage, is reset to its default. The modified definition forbids the move. That disposes of Blocked tracks and, by the same stroke, leaves Suzy only the frozen witness, which has the switching profile. The choice between definitions decides which distinction normality must draw; it does not remove the need for one.

## 5. Pricing the non-anonymous escapes

The theorists in question do not propose an anonymous policy. Halpern and Hitchcock call their rules rough-and-ready, allow cross-variable comparisons where "such a comparison clearly seems warranted" (2015, 32), and disclaim the task of determining the right normality ordering (26 fn. 13). The dilemma is therefore not a refutation. It instead identifies a limit on a specified class of transferable policies:

(P1) Under event coding, every anonymous Pareto filter that makes the antidote and Suzy's throw causes, and leaves Billy's throw out, makes some switch a cause, under each HP definition (Corollary).

(P2) Maintain event coding for the variables involved: throws, hits, rings, barks and fresh blockages are occurrences on the codings used here. This is an explicit assumption; the inertial alternative for standing blockages is considered below.

(P3) The antidote and Suzy's throw are causes; Billy's throw and the switches are not.

(C) So any normality ordering that respects (P3) under an HP definition either violates Pareto improvement, which is Halpern and Hitchcock's first guideline, or ranks two witnesses with the same profile differently, that is, by what their variables represent. Under the modified definition only the second option is open, since Theorem 1 does not use Pareto.

The conclusion is not that such orderings are illegitimate, but that their verdicts on switches are only as good as the mechanism-specific judgment they encode. The rest of this section examines one such judgment and the limits of a published motivation for it.

**One additive separation.** Hold the root and other category contributions fixed, and allow only the frozen-default score to depend on the mechanism. With scores $c_{BH}$ and $c_L$ for the frozen hit and bell, witness gains differ by $c_{BH}-c_L$. Within this restricted repair, keeping Suzy and excluding Doorbells requires $c_{BH}>c_L$, and likewise for the train held off the left track. General non-anonymous orderings could instead distinguish root changes, other transitions or interactions; Theorem 1 does not force them to locate the difference in frozen mechanisms. This escape is formally cheap. With frozen bell and left track scored $-5$ and every other frozen default 0 (and $r=2$, $a=0$, $b=-1$, $d=-3$), the modified definition counts the antidote, the chain's start, the ducking and Suzy's throw as causes, and leaves Billy's throw, the flip in Tracks and the switch-setting in Doorbells out of every cause. It is also Halpern's own judgment on Tracks: "the world where the train does not go on the left track despite the switch being set to the left is less normal than the actual world" (2015, 8). For a componentwise filter, that judgment is $\mathbf f\not\succeq\mathbf n$ for the track while $\mathbf f\succeq\mathbf n$ for Billy's hit and the ducking. The question is what grounds the difference.

**The reliability asymmetry.** One published ground for distinguishing frozen mechanisms is reliability. Reporting Beckers and Vennekens (2018), Xiao and Xiong (2026, 8) write that "the key distinction between the early preemption and the switch example lies in whether we take into account the possibility that the backup mechanism malfunctions", since "the supervisor's shooting accuracy" is "far more uncertain than the breakage of a sturdy track". On this view a frozen default is abnormal to the degree that its mechanism is reliable. That fits the textbook cases, where the preempted backup is an agent and the switch a sturdy device, but it makes the verdict depend on how reliable the backup was rather than on whether it was preempted. Two tests bring this out.

> *Sprinkler.* A fire is put out by a firefighter's hose; a sprinkler system with a failure rate no higher than a doorbell circuit's would have put it out moments later.

Structurally this is late preemption, with the sprinkler's activation for Billy's throw. Within the additive repair just specified, if the frozen sprinkler is as abnormal as the frozen bell and the other contributions agree, the firefighter is not a cause by itself under the modified definition; on computation, the firefighter is part of a cause only together with the sprinkler's activation, which is itself part of a cause. Most will say the firefighter put out the fire, however reliable the backup.

> *Seedlings.* $P=1$ (a field is sown), $S=1$ (a locust swarm arrives); it is a dry week and no rain is possible. $G=P\wedge S$ (the swarm strips the seedlings), $D=P\wedge\neg S$ (they die of drought), $X=G\vee D$ (they are destroyed). Actually $G=1$, $D=0$, $X=1$.

The map $P\mapsto M$, $S\mapsto T$, $G\mapsto R$, $D\mapsto L$, $X\mapsto E$ is an isomorphism onto Doorbells that preserves equations, actual values and event-coded defaults. So any account whose verdicts depend only on those features treats the swarm as it treats the switch-setting. A repair varying only frozen-mechanism reliability could separate them only if unwatered seedlings in a dry week were less certain to die than a pressed, left-switched bell is to ring. If they are not, it denies that the swarm is even part of a cause of the destruction (computed). A defender may reply that the coarse outcome hides timing: with destruction dated, the swarm is a but-for cause of destruction on the third day. That is a reasonable repair, but then representation, not normality, separates the swarm from the switch, and Doorbells admits no corresponding repair, since the bark comes at the same time either way.

Gallow's own model of Doorbells takes a representational route: it has one switch variable whose values encode both setting and signal, and his negative verdict holds "so long as the switch's directing a signal to the right is no more deviant than its directing a signal to the left" (2021, 86). That is a comparison among the values of a single variable, which no anonymous filter on a binary route model can express. Whether such representations can be selected by a principle stated before the verdicts is the aptness question that Blanchard and Schaffer (2017) press, as Andreas and Günther (2024, 27) report, against reliance on defaults. I do not settle it here.

**Inertial coding of standing blockages.** Under the older definitions, Theorem 2 has a natural escape. If a standing blockage is a default, inertial state, in the sense in which Gallow (2021, 86–87) contrasts "deviant, noninertial events" with "default, inertial states", then clearing it moves a root from default to deviant. Componentwise filters then exclude the flip's witness, and its additive gain falls to $b-a=g_{\text{Prevention}}-r$, which can be negative while the antidote's is not (computed for all five calibrated preorders). The cost is that the escape answers a question the verdict does not depend on. Let both tracks have been blocked a minute ago by landslides, which are occurrences. The coding is then the event coding of Theorem 2, and the flip counts again. Whether the flip caused the non-arrival should not depend on how long the tracks have been blocked. The escape also leaves Theorem 1 untouched.

## 6. Exceptionless conformity

Halpern and Hitchcock note that their treatments of the short circuit and of preemption involve exceptions to the default that endogenous variables obey their equations (2015, 36). They show how to remove the short circuit's exception by adding a variable for the second bodyguard's intentions, and they conjecture "that it is always possible to formally construct additional variables to do this" (37). Under the modified definition, carrying this programme to completion has a sharp cost.

**Lemma (frozen witnesses).** In a deterministic acyclic model with fixed context and nonintervened roots fixed, under the modified definition, let $\vec X=\vec x$ be a cause of $\varphi$ with a witness whose world violates no non-root equation. Then every member of $\vec X$ is a root, and $\varphi$ depends counterfactually on $\vec X=\vec x$.

*Proof.* Let $\vec R$ be the root members of $\vec X$. Since the witness world violates no non-root equation and every root outside $\vec R$ keeps its actual value, acyclicity and uniqueness of solutions make it identical to the world under $[\vec R\leftarrow\vec r']$ alone. Since $\varphi$ fails there, $\vec R$ is nonempty and satisfies the witness condition with nothing frozen; the same world passes any filter that the original witness passed. If $\vec X$ had a non-root member, $\vec R$ would be a proper subset satisfying AC1 and AC2, contrary to AC3. ∎

The argument adapts the elimination-and-minimality reasoning of Halpern's (2016, 121, 133–134) stability theorem for conservative extensions to a single conforming witness. A check on 400 random models found no counterexample.

Suppose, then, that conformity is made exceptionless: every equation violation is strictly less typical, and no special comparison compensates for it. Since the actual world violates no equation, an admissible witness world violates none, and by the Lemma only root but-for causes, possibly conjunctive, survive. The ducking in Boulder is a non-root and is lost; so is the chain's intermediate $I=1$; in late preemption the throws become jointly a cause, with Billy's throw part of it (all computed). The conjecture may still be true as a claim about representing orderings. What fails is the hope that equation-conformity, once all exceptions are explained away, separates preemption from switching under the modified definition.

Xiao and Xiong's (2026) refinement of Hitchcock's active-route account requires a witness with off-route intermediates fixed at their actual values to be "available": it "does not violate the structural equations of the model" (Definition 12, 5). They prove that their causes are modified-HP causes (Proposition 1, 6). If availability is evaluated in a deterministic acyclic model at the same fixed context, with nonintervened roots unchanged, the Lemma applies: only root but-for causes survive. Their acknowledged difficulty with the trainee's firing in early preemption (8) is consistent with this consequence. If availability instead permits changes in background or exogenous mechanism variables, the fixed-context premise fails, and the Lemma alone does not establish the consequence. Their proposed use of nondeterministic models and variables for accuracy and nerve therefore needs a separate analysis. The theorem here concerns the explicit fixed-context reading, not every possible interpretation of availability.

## 7. A parallel in regularity theory

Beckers (2026) argues that Andreas and Günther's regularity theory faces a dilemma of the same shape. Their final theory excludes the flip in the simple switch by structural conditions: condition (5) keeps the regularities of the candidate's descendants, and then no admissible set of facts satisfies condition (2) (Andreas and Günther 2024, 25). Beckers reports that their 2024 accounts need the deviancy condition to give the same verdict on two alternative switch models, one of them from Hitchcock (2009), and he argues that the deviancy condition then gives the wrong verdict on early preemption in which the backup process is not deviant (Beckers 2026, 2, 10–11). A drought preempted by locusts is such a case: on my computation their final theory counts the swarm a cause without the deviancy condition and not with it, since the normal absence of rain must be left out of the facts. The same computation shows that their other conditions already exclude both the Doorbells switch-setting and the Seedlings swarm. Since the deviancy condition only removes causes, their theory excludes the Seedlings swarm whatever deviancy is assigned; for them, Seedlings bears on the structural conditions, not on deviancy. Section 4 shows that normality-augmented HP faces a counterpart of Beckers's dilemma, and that changing the definition only moves it.

## 8. Objections and replies

**Objection 1: aptness.** Tracks and Doorbells are route models. Halpern's three-variable switch model gets the switch right without normality under all three definitions (2015, 7).

*Reply.* Theorem 2 arises in the blockage representation that Halpern (2015, 7) takes from Halpern and Hitchcock. Theorem 1 needs route variables, and in Doorbells they are hard to avoid: each bell's ringing is a distinct event that can itself be an effect, and Gallow's alternative replaces them by a single variable with an explicit normality comparison among its values. A theorist who rejects route models owes a rule, stated before the verdicts, that selects the non-route model for switches and the route model for late preemption, whose route variables ($SH$, $BH$) nobody proposes to remove.

**Objection 2: the coding.** Event coding does the work; another coding might escape.

*Reply.* Theorem 1 needs only that throws, settings, hits, rings, shattering and barking be deviant and their absence default, which the codings used for these cases in this literature grant. Theorem 2 needs blockages to be deviant; the inertial alternative was priced in Section 5.

**Objection 3: graded causation.** Halpern's graded account keeps causes with abnormal witnesses and compares their quality (2016, §3.3).

*Reply.* The theorems concern the filter. If a graded account compares only relative witness quality through the same anonymous transition profile, it assigns these witnesses equal quality. That conditional parity does not cover graded accounts that use absolute normality levels, mechanism-specific comparisons or other information.

**Objection 4: the verdicts.** Some deny that switches are non-causes, or doubt the contrast with preemption; Hitchcock (2009), as Beckers (2026, 10) reports, presented a switch model to challenge it.

*Reply.* Then the dilemma has no grip, and normality has no switching work to do. The result is conditional on the verdicts in Section 3, which the normality approach was introduced to respect.

## 9. Conclusion

Under event coding, an anonymous Pareto filter cannot keep genuine prevention and late preemption while excluding the standard switches under any of the three HP definitions. The modified definition equates Suzy's sole witness profile with the switching profiles; the older definitions admit a blocked-tracks witness that improves on genuine prevention's. This is a conditional limitation on transferable policies, alongside Wysocki's stronger obstruction for conjoined cases. A separating policy may use principled information beyond the profile. Varying only frozen-mechanism scores exposes a reliability dependence; it is one escape, not the only one. Exceptionless equation-conformity has a separate fixed-context cost: only root but-for causes remain. The open issue is which additional normality information or model-selection principle justifies the desired distinctions.

## Appendix. Proofs and computation

**Witness uniqueness and AC3.** In genuine prevention the only witness world is $(P,A,V)=(1,0,1)$. In the chain, freezing $I$ or $Y$ at 1 restores $Y=1$, so the only witness is $[C\leftarrow0]$. In Boulder, the modified definition admits only $(F,B,K,H)=(1,1,0,1)$; the older definitions also admit $(0,1,0,1)$, in which $B$ moves from $\mathbf l$ to $\mathbf u$, and the calibration conditions are unchanged. In the short circuit, the only witness is $[A\leftarrow0,P\leftarrow1]$, which moves $P$ from $\mathbf l$ to $\mathbf u$ and $V$ from $\mathbf n$ to $\mathbf l$. For a single candidate, AC3 holds automatically, so Theorems 1 and 2 need no minimality argument; a single candidate is a cause iff some witness is admitted. The corollary's claim that Billy's throw is in no cause, and the remarks on conjunctive causes, rest on the exhaustive computation. Under the older definitions the extra witnesses of the switches fail sufficiency or move a root to its deviant value: in Doorbells, cancelling the press leaves the barking absent when the switch is restored; in Tracks, no other contingency changes the arrival.

**Computation.** A Python implementation of the three definitions (Halpern 2015, 3–4), with the normality filter applied before AC3, enumerates every candidate subset of every model above, including those containing the outcome, and every admissible witness. It checks Theorems 1 and 2 and the corollary for all 355 preorders on the four categories, the gain identities symbolically, 3,000 random integer additive scores with $r>0$, the boundary score, the escapes of Section 5, the Lemma on 400 random acyclic binary models (357 causes, 940 conforming witnesses), and Andreas and Günther's (2024) conditions with and without deviancy. Without normality the implementation reproduces Halpern's (2015) verdicts on the switch models and the short circuit.

## References

Andreas, Holger, and Mario Günther. 2024. "A Regularity Theory of Causation." *Pacific Philosophical Quarterly* 105 (1): 2–32. https://doi.org/10.1111/papq.12447.

Beckers, Sander. 2026. "Difference-Making without Making a Difference." Preprint, arXiv:2606.24832v1.

Beckers, Sander, and Joost Vennekens. 2018. "A Principled Approach to Defining Actual Causation." *Synthese* 195 (2): 835–862. https://doi.org/10.1007/s11229-016-1247-1.

Blanchard, Thomas, and Jonathan Schaffer. 2017. "Cause without Default." In *Making a Difference: Essays on the Philosophy of Causation*, edited by Helen Beebee, Christopher Hitchcock, and Huw Price. Oxford: Oxford University Press. https://doi.org/10.1093/oso/9780198746911.003.0010.

Gallow, J. Dmitri. 2021. "A Model-Invariant Theory of Causation." *Philosophical Review* 130 (1): 45–96. https://doi.org/10.1215/00318108-8699682.

Hall, Ned. 2000. "Causation and the Price of Transitivity." *Journal of Philosophy* 97 (4): 198–222. https://doi.org/10.2307/2678390.

Hall, Ned. 2007. "Structural Equations and Causation." *Philosophical Studies* 132 (1): 109–136. https://doi.org/10.1007/s11098-006-9057-9.

Halpern, Joseph Y. 2015. "A Modification of the Halpern–Pearl Definition of Causality." Preprint, arXiv:1505.00162v1. (Page references are to this version.)

Halpern, Joseph Y. 2016. *Actual Causality*. Cambridge, MA: MIT Press.

Halpern, Joseph Y., and Christopher Hitchcock. 2015. "Graded Causation and Defaults." *British Journal for the Philosophy of Science* 66 (2): 413–457. https://doi.org/10.1093/bjps/axt050. (Page references are to arXiv:1309.1226.)

Hitchcock, Christopher. 2001. "The Intransitivity of Causation Revealed in Equations and Graphs." *Journal of Philosophy* 98 (6): 273–299. https://doi.org/10.2307/2678432.

Hitchcock, Christopher. 2009. "Structural Equations and Causation: Six Counterexamples." *Philosophical Studies* 144 (3): 391–401. https://doi.org/10.1007/s11098-008-9216-2.

Wysocki, Tomasz. 2023. "Conjoined Cases." *Synthese* 201: 197. https://doi.org/10.1007/s11229-023-04101-w.

Xiao, Zhizun, and Wei Xiong. 2026. "A Refinement of the Hitchcock Definition of Actual Causation." *Humanities and Social Sciences Communications* 13: 1088. https://doi.org/10.1057/s41599-026-07470-y.

