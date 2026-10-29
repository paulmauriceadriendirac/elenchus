# An additive obstruction for normality filters

Companion result to version 5 of *Limits of Uniform Normality Filters in Actual Causation*, 29 October 2026. The central theorem and its proof are included in the essay; this note supplies the full setup, boundary calculation and reproducible finite check.

## Claim and scope

Under the modified Halpern–Pearl definition, a uniform additive normality score cannot simultaneously retain the positive causal judgments in Chain and Boulder and reject the singleton switch cause in the binary Doorbells model below. This extends the essay's componentwise analysis to a separate family of scores that permits compensation between variables. It does not classify every world ordering, every additive model with variable-specific scores, or every representation of these stories.

The proof is an exact identity among score differences. An additional finite calculation establishes that the restriction to modified HP matters: one common score vector fits the six displayed target judgments under both original and updated HP. All computational checks use the project's existing HP implementation; this note does not claim a second implementation or an independent referee.

## Setup

The models are binary and acyclic. Roots are intervenable endogenous variables whose actual values come from the context. Every default is 0. A non-root value receives one of four categories, evaluated against its equation in the witness world:

| Category | Default status | Equation status | Score |
|---|---|---|---|
| n | Default | Conforming | a |
| l | Deviant | Conforming | b |
| f | Default | Violating | c |
| u | Deviant | Violating | d |

Each root contributes r at its default and 0 at its deviant value, with r > 0. Every non-root uses the same four real scores a, b, c, d. These five numbers are shared across the models. A world's score is the sum of those contributions. A witness is admissible when its score is at least the actual world's score. Minimality is applied after this filter.

Setting the deviant root score to zero loses no generality for a common pair of root scores: adding the same constant to each root's contribution leaves every within-model comparison unchanged. The substantive assumption is the common difference r. Likewise, these scores need not be interpreted as empirical probabilities.

The three central models are:

| Model | Actual roots | Non-root equations | Target judgment |
|---|---|---|---|
| Chain | C=1 | I=C; Y=I | C=1 causes Y=1 |
| Boulder | F=1 | B=F; K=F; H=B and not K | K=1 causes H=0 |
| Doorbells | M=T=1 | L=M and not T; R=M and T; E=L or R | T=1 does not cause E=1 |

In Boulder, F is the fall, B the boulder's approach, K ducking and H being hit. In Doorbells, M is pressing the button, T setting the switch right, L and R the two bells ringing, and E the dog barking. Doorbells is the essay's binary simplification of Gallow's case; Gallow's published model has a four-valued switch.

## Theorem and proof

**Theorem.** For every r > 0 and every real a, b, c, d, if modified HP with the stated score makes C=1 a singleton cause in Chain and K=1 a singleton cause of H=0 in Boulder, it makes T=1 a singleton cause of E=1 in Doorbells.

For Chain, the only resulting singleton witness world is (C,I,Y)=(0,0,0). Holding I or Y at its actual value prevents the outcome from changing. The witness gains r from the root and twice a-b from the two non-roots:

$$g_C=r+2a-2b.$$

For Boulder, modified HP can change K to 0 but can only hold other variables at actual values. Consequently F=B=1, and H=1 unless it is frozen at its actual value, which would prevent the outcome change. The only resulting witness world is (F,B,K,H)=(1,1,0,1). K moves from l to f, while H moves from n to l:

$$g_B=(c-b)+(b-a)=c-a.$$

Different sets of redundant frozen variables can give the same world; the uniqueness claim concerns resulting worlds, not intervention descriptions.

Doorbells has a valid modified witness [T←0,L←0]. Its resulting world is (M,T,L,R,E)=(1,0,0,0,0). T gains r, L moves from n to f, and R and E each move from l to n:

$$g_T=r+(c-a)+2(a-b)=g_C+g_B.$$

The two positive causal judgments require g_C≥0 and g_B≥0. Hence g_T≥0. The switch has an admissible outcome-changing witness, and singleton minimality is automatic. This proves the theorem for arbitrary real scores. The elementary linear-combination argument is not itself a proposed new mathematical method.

## A sharp boundary between definitions

Set (r,a,b,c,d)=(2,0,-1,-5,-3). Chain's witness gain is 4; the Doorbells switch witness gain is -1. Boulder's modified witness gain is -5 and is rejected. Original and updated HP, however, admit the alternative intervention [K←0,F←0,B←1], producing (F,B,K,H)=(0,1,0,1). Its gain is

$$r+(d-b)+(a-b)+(b-a)=r+d-b=0.$$

Restoring K=1 under every required subset of the contingency and every required restoration of other variables keeps H=0, so this witness satisfies even updated AC2(b). The positive Boulder judgment can therefore survive while the Doorbells switch is rejected.

The finite check includes three additional models from the essay: Genuine Prevention, Short Circuit and Locusts. It enumerates every nonempty candidate subset, including candidates containing the outcome, before applying minimality. Its verdicts are:

| Candidate | Original HP | Updated HP | Modified HP |
|---|---|---|---|
| Chain: C=1 | Singleton cause | Singleton cause | Singleton cause |
| Boulder: K=1 | Singleton cause | Singleton cause | Not part of a cause |
| Doorbells: T=1 | Not part of a cause | Not part of a cause | Not part of a cause |
| Genuine Prevention: A=1 | Singleton cause | Singleton cause | Singleton cause |
| Short Circuit: A=1 | Not part of a cause | Not part of a cause | Part of a conjunctive cause |
| Locusts: S=1 | Singleton cause | Singleton cause | Part of a conjunctive cause |

Thus the displayed weights fit all six target judgments under original and updated HP. Under modified HP they abandon the ducking judgment; they do not refute the theorem.

## What non-uniformity must change

Keep the category scores shared but allow different root-default bonuses r_C and r_T in Chain and Doorbells. Then

$$g_T=g_C+g_B+(r_T-r_C).$$

Accepting both calibration witnesses while rejecting the switch witness requires r_C-r_T > g_C+g_B. This is a necessary and sufficient inequality for those three singleton witness comparisons. It is not a guarantee about all conjunctive candidates. Statistical or normative evidence could justify such different bonuses; the result does not prohibit that evidence. It specifies the quantitative distinction that this particular escape needs.

## Relation to prior work and philosophical significance

Additive and compact normality representations are established tools. Halpern's *Actual Causality* (2016), printed pages 143–145, discusses algebraic plausibility and ranking functions using addition to combine contributions. His pages 149–150 discuss reusable conformity rules with exceptions and comparisons across variables. Halpern and Hitchcock's 2013 paper, [“Compact Representations of Extended Causal Models”](https://doi.org/10.1111/cogs.12059), is relevant background. The present result is not a claim to have invented additive normality.

The proposed increment is the incompatibility of the three specified judgments for a shared category score under modified HP, together with the explicit contrast with the older definitions. Its philosophical use is to distinguish two questions: whether compensation is permitted and whether the information being compensated is adequate across cases. Permission to offset one variable's loss with another's gain does not by itself solve this switching problem. The result also avoids relying on the disputed coarse Locusts outcome that figures in the earlier componentwise argument.

Uniformity and the binary route representation remain substantive restrictions. Halpern's framework permits richer choices; this is not a refutation of that whole framework. Relevant passages of the supplied book and targeted searches for additive or weighted normality and switching did not reveal the displayed identity. This is a bounded originality assessment. The core definitions and proofs of Xiao and Xiong's [2026 refinement of Hitchcock](https://doi.org/10.1057/s41599-026-07470-y) remain unread because reliable full-text access failed; that comparison is open.

The result strengthens A4's contribution beyond its earlier attribution repairs, but does not by itself establish that A4 should displace the accuracy or free-evidence essay. The significance of this deliberately simple transferable policy remains the main philosophical question.

## Reproduction

Run `python3 verify_additive.py` from this directory or give its absolute path. It imports `source/models.py` and writes `verification-results.json`.

The exact witness feature vectors, in the order (root-default count,n,l,f,u), are (1,2,-2,0,0), (0,-1,0,1,0), and (1,1,-2,1,0). Their coefficient identity is checked exactly. A supplementary integer sample checks 2,916 score vectors, 1,080 satisfying both positive calibrations. The proof above supplies the all-real-scores conclusion; the sample is only a diagnostic. The boundary verdicts enumerate every candidate subset under all three definitions. Earlier componentwise tests were not rerun for this addition.
