# Recoverable Knowledge and the Permission to Inquire

**Abstract.** Further evidence can sometimes improve an agent's knowledge of what she knows even when she already knows the first-order answer. This response to dogmatism requires attention to where the agent's inquiry currently stands. The attainability of arbitrarily high orders of knowledge somewhere in a space of histories does not establish their attainability from every existing history. I distinguish these claims and give a sufficient condition for the stronger one in Carter and Hawthorne's ball-drawing setting. Their transparency principle yields recovery from every finite history if its successful evidence thresholds extend sufficiently far along the inquiry. The absence of full iterated knowledge at finite all-red histories guarantees this condition. A small epistemic countermodel shows that transparency alone does not guarantee local recovery. The result clarifies one route by which higher-order inquiry can retain an epistemic upside; it neither establishes the expected value of further evidence nor requires agents to pursue arbitrarily many epistemic aims.

## 1. An open question needs an available answer

Someone already knows that a bag contains two red balls and one black ball. Drawing another ball might provide misleading evidence and undermine that knowledge. If inquiry is successful once its answer is known, what epistemic reason remains to continue drawing?

Carter and Hawthorne (2024) develop this problem of ex ante dogmatism and a response through higher-order inquiry. Knowing the bag's composition need not settle whether one knows it. Further evidence about the bag can improve one's epistemic position concerning that further question. The idea is not that a new kind of evidence must be obtained. More evidence of the original kind may make a higher level of knowledge available.

The present argument concerns a condition on that response. To identify an epistemic upside to continuing from a particular history, the relevant knowledge must be attainable from that history. It is insufficient that someone could attain it after a different beginning. Evidence already received cannot be replaced by a favorable alternative past.

I distinguish global attainability from local recoverability, show why they can come apart, and prove a sufficient condition connecting them in the ball-drawing setting. The proof uses a strengthened availability property of the evidence thresholds supplied by Carter and Hawthorne's transparency principle. One way to obtain that property is to exclude full iterated knowledge after any finite all-red history.

The intended contribution is a clarification and conditional strengthening of their response. Carter and Hawthorne need only establish appropriate cases to resist an unrestricted dogmatism principle. They need not prove that every agent can recover every missing level of knowledge from every history. My result concerns that stronger, locally applicable claim. It also leaves their separate account of the norms and aims of inquiry to be assessed on its own merits.

## 2. Histories and levels of knowledge

Let $p$ be the true proposition that the bag contains two red balls. As in the original example, draws are made with replacement. Write $K^1p$ for $Kp$, and $K^{n+1}p$ for $K(K^np)$. A finite history is a string of red and black outcomes. Its length is the number of draws already made. An extension of a history appends outcomes without changing those already recorded.

I use $H_n(h)$ to mean that, after history $h$, the agent is in a position to have $K^np$. This concerns available knowledge, not whether a distracted or unwilling agent actually forms every available belief. Assume *descent*: if $H_n(h)$ and $1\leq j\leq n$, then $H_j(h)$. This is natural under the idealization that the agent can realize the relevant knowledge and its factive consequences. It is stated as an assumption because availability should not be silently identified with actual knowledge.

Carter and Hawthorne's transparency principle can be represented as follows:

$$\text{For every }n\geq1\text{ there is a }k\geq1\text{ such that, for every }h\text{ of length }k,$$
$$\text{if at least two thirds of }h\text{ is red, then }H_n(h). \tag{T}$$

For each $n$, call such a length $k$ a *witness length*. Principle T is stronger than the bare claim that every finite level of knowledge is attainable somewhere. It provides a sufficient evidence pattern at a length shared by all histories satisfying the specified proportion.

It does not explicitly say how large the witness lengths are, how they relate to the agent's current history, or whether a later length is also a witness. A sufficient condition at length ten is not, merely as a matter of logic, a sufficient condition at length one hundred. That further persistence might be plausible, but it needs either a premise or a derivation.

Define *local recoverability* as follows:

$$\text{For every finite }h\text{ and every }N\geq1,\text{ some proper finite extension }hu\text{ satisfies }H_N(hu). \tag{R}$$

The word “recoverability” includes acquiring a level for the first time. It also includes regaining a level that was lost. R is deliberately demanding: it applies to every finite history and every finite target level. A response to dogmatism in a particular case needs only the relevant instance of R.

The connection between T and R is not immediate. A witness to T might concern a length the agent has already passed. Alternatively, it might concern a length still ahead but too near for even an uninterrupted run of red outcomes to overcome the unfavorable outcomes already recorded. The needed issue is the availability of sufficiently distant opportunities for successful inquiry.

## 3. A sufficient condition for recovery

For each $n$, select a witness length $k_n$ supplied by T; for definiteness, one may select the least. Say these witnesses are *cofinal* when, for every target level $N$ and every finite bound $B$, some $n\geq N$ has $k_n>B$. Thus arbitrarily high target levels have witnesses at arbitrarily late stages. This condition is sufficient for R.

**Recovery proposition.** Assume T, descent, and cofinal witness lengths. Suppose every finite extension consisting of red outcomes is an admissible continuation. Then local recoverability holds.

*Proof.* Fix a history $h$ of length $m$ and a target level $N$. Choose $n\geq N$ with $k_n>3m$. Append only red outcomes until the total length is $k_n$. Even if every outcome in the original history was black, the extended history contains at least $k_n-m$ red outcomes. Hence its red proportion exceeds two thirds. By T it satisfies $H_n$, and by descent it satisfies $H_N$. Since $k_n>m$, this is a proper finite extension. The history and target were arbitrary. ∎

The proof explains why the past need not trap an inquirer. Sufficiently much new favorable evidence can outweigh any finite unfavorable beginning. What does the work is both the availability of a favorable continuation and the availability of a sufficiently late threshold to which it can lead.

The required threshold property follows from one further epistemic assumption. Say an agent has *full finite-order knowledge available* at a history when $H_j$ holds there for every positive integer $j$. This is a family of finite iterations, not knowledge of a single infinitely long conjunction. Consider the restriction:

$$\text{No finite all-red history makes full finite-order knowledge available.} \tag{F}$$

**Unboundedness lemma.** Assume T, descent, and F. Then any selection of witness lengths $k_n$ is cofinal.

*Proof.* Suppose otherwise. Then for some $N$ and finite $B$, all $k_n$ with $n\geq N$ lie at or below $B$. Since there are infinitely many such indices and only finitely many possible witness lengths, some length $k^*$ is selected for infinitely many indices. At the all-red history of length $k^*$, T gives $H_n$ for those infinitely many, and hence unboundedly large, indices. Given any positive integer $j$, choose one of these indices at least $j$. Descent gives $H_j$ at that same history. Thus every finite level is available there, contradicting F. ∎

Together the results establish that T, descent, and F imply R when the required continuations are admissible. No uniform bound on the length of the recovery is promised. The construction may require very many draws, and its probability may be very small.

In the actual two-red, one-black bag, any specified finite run of $r$ further red draws has probability $(2/3)^r>0$. Thus the constructed continuation is a positive-probability possibility under the sampling assumptions. This is an external assessment of a possible continuation. It is not yet something the inquirer knows in advance will improve her epistemic position, nor an estimate of the net value of the inquiry.

## 4. Why transparency alone is insufficient

An abstract epistemic model shows the logical role of the additional condition. The purpose is to test whether T by itself implies R, not to reproduce every assumption of Carter and Hawthorne's example.

Take three worlds $w,v,u$, with $w$ actual and $p$ true at $w$ and $v$ but false at $u$. Interpret knowledge by a reflexive accessibility relation: a proposition is known at a world just when it holds at every accessible world. In the model associated with any history beginning with black, let

$$R(w)=\{w,v\},\qquad R(v)=\{v,u\},\qquad R(u)=\{u\}.$$

At $w$, $Kp$ holds, because both accessible worlds satisfy $p$. But $KKp$ fails: $v$ is accessible from $w$, and $Kp$ fails at $v$ because $u$ is accessible from $v$. Keep this epistemic model fixed throughout every further extension of a black-first history. No such extension supplies $KKp$ at the actual world.

For every history beginning with red, instead use the identity accessibility relation. At $w$, every finite iteration of knowledge of $p$ then holds. At the empty history one may use the universal relation, so that the agent does not yet know $p$.

This family satisfies T: for every level $n$, choose $k_n=1$. A one-draw history whose red proportion is at least two thirds is precisely the red history. At that history, all finite knowledge levels are available. Nevertheless, R fails after the one-draw black history, since no extension of it supplies level two. Descent holds because the relations are reflexive. The condition that fails is F: the first red outcome supplies full finite-order knowledge.

The example is intentionally artificial. It does not establish that a realistic learner can obtain unlimited higher-order knowledge from a single draw. Nor does it claim to satisfy the target paper's additional principles concerning evidence, inquiry, or uncertainty about epistemic transitions. It establishes only a non-entailment: the formal shape of T leaves room for successful histories confined to a branch that an existing history cannot reach.

The countermodel also clarifies a possible repair. If every sufficiently long history with the specified red proportion supplied the relevant level, rather than just every qualifying history at one witness length, a later threshold could always be selected. That stronger transparency condition would give cofinality directly. It would not require an argument against full knowledge at finite histories.

F is consequently sufficient, not necessary. A model may permit full knowledge on some histories and still have ample routes to all finite levels from other histories. The point is to identify what guarantees continuation from the present position, not to derive a general ban on full knowledge.

## 5. What recoverability changes about dogmatism

The original dogmatism problem combines an apparent lack of epistemic improvement with a possibility of epistemic loss. Once the first-order answer is known, further evidence can seem to offer only a downside. Higher-order inquiry challenges the first part of that reasoning when a further answer remains open and attainable.

Recoverability establishes the relevant availability claim under explicit assumptions. Suppose the agent knows $p$, lacks some finite level of knowledge she aims to acquire, and meets the conditions of the recovery proposition. Then some continuation offers a gain concerning an outstanding epistemic aim. The particular argument that there is no possible epistemic improvement is unavailable.

Three further conclusions do not follow. The agent need not have a reason to adopt every higher-order aim. A possible improvement need not outweigh possible losses. And a positive-probability successful continuation need not make any actual evidence-gathering policy permissible or required. Each conclusion needs premises about aims, risks, costs, or norms that the recovery proposition does not contain.

These qualifications are already central to the surrounding literature. Carter and Hawthorne explicitly discuss finite agents and the risk of losing lower-order knowledge while pursuing higher-order knowledge (§§4.1.1–4.1.2). Brown (2025, §3) challenges the assumptions that would make additional higher-order inquiries part of ordinary agents' pursuits, including the demands on their resources. The present result settles neither dispute. It supplies a conditional availability claim after the relevant aim is specified.

A simple numerical illustration separates availability from value. Suppose a policy has a one-in-one-hundred chance of an epistemic improvement worth one unit and a ninety-nine-in-one-hundred chance of a loss worth one unit. There is a possible gain, but the expected change under that valuation is negative. The recovery proof does not even assign probabilities and values to all outcomes of a policy. It cannot establish an expected-value conclusion merely by locating one favorable continuation.

Conversely, failure of R would not establish dogmatism. Another inquiry might supply an epistemic benefit, or further evidence might have practical value independent of higher-order knowledge. The propositions here identify when one particular reply to a no-upside argument is available. They do not exhaust the reasons for gathering evidence.

The distinction is useful because a universal permission to continue inquiry is often stronger than what a criticism of dogmatism needs. A single counterexample can defeat a universal prohibition. A practical recommendation addressed to an agent with a specified evidential history needs a locally applicable reason. These are different burdens, and a theory may satisfy the first without satisfying the second.

## 6. The status of full knowledge

F is a substantive assumption. It should not be treated as an automatic consequence of the ordinary possibility of higher-order ignorance. A system might have histories at which knowledge is partial and others at which every finite iteration holds. The existence of the former does not exclude the latter.

Fiat (2025) develops an account on which full and partial knowledge can coexist with a margin-for-error principle. This makes it especially important not to build the universal impossibility of full knowledge into the present argument without defense. The recovery proposition itself is neutral: cofinal witness lengths can be supplied directly, with F serving as one sufficient route.

The restricted form of F also deserves attention. The proof needs only the absence of full finite-order knowledge at finite all-red histories. It does not require that every finite history leave every agent short of full knowledge about every proposition. A universal anti-luminosity thesis would be much stronger than the lemma requires.

One might still object that F is implausible precisely at very favorable histories. If an uninterrupted run of red outcomes eventually settles every relevant epistemic question, the all-red histories could be cases of full knowledge. In that event, the lemma cannot be used. A defender seeking local recoverability should instead explain why favorable evidence remains sufficient at arbitrarily late stages, or establish the relevant local continuation directly. The proof makes that choice visible rather than resolving it by stipulation.

There is also no suggestion that the target paper must adopt F. Its broader argument considers how higher-order knowledge can be acquired and what the agent knows about that acquisition. The present result isolates one issue within a stronger extension of its proposal. It does not show that the original resistance to unrestricted dogmatism fails without the auxiliary premise used here.

## 7. A local claim about further evidence

An open higher-order question supplies a candidate epistemic benefit only if its answer is attainable along some continuation of the actual inquiry. Transparency of the specified form supplies successful histories; additional structure determines whether those histories remain reachable from the present one.

The result establishes one route from the former to the latter. Cofinal witness lengths suffice, and their cofinality follows if finite all-red histories never supply all finite orders of knowledge. The countermodel shows why the unrestricted inference from transparency alone is invalid. The epistemic conclusion is local availability, leaving the separate questions of valuable, reasonable, and obligatory inquiry unresolved.

## References

Brown, Jessica. 2025. “Knowledge, Inquiry and Dogmatism.” *Synthese* 205, article 174. https://doi.org/10.1007/s11229-025-05008-4.

Carter, Sam, and John Hawthorne. 2024. “Dogmatism and Inquiry.” *Mind* 133: 651–676. https://doi.org/10.1093/mind/fzad070. Section references follow the author manuscript, “Dogmatism & Inquiry.”

Fiat, Yonathan. 2025. “Knowing to Infinity: Full Knowledge and the Margin-for-Error Principle.” *Philosophy and Phenomenological Research*. https://doi.org/10.1111/phpr.70001.
