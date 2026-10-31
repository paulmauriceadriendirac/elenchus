# A6: triage of outside referee comments (DeepSeek, Grok Review 3), 31 Oct 2026

**Essay:** `final/A6/essay.md` (v8, 5,948 words). **Comments:** `relay/inbox/deepseek-20261031/A6-good-theorem.md` (main), the A6 parts of `README.md` and `00-overview.md` in the same folder, and Review 3 in `relay/inbox/grok-reviews-20261031.md`.
**Scope:** substance only. I ran no citation, compliance, formatting or word-count checks. Every comment was checked against the essay text. The two items the orchestrator named were also checked against the primary sources in the repository: G&S 2023 n. 40 (`inbox/sources/goodman-salow-2023.txt`, ll. 1755–1768) and DDB App. B (`state/ambitious/sources/dorst-etal-2021-deference-done-better.txt`, ll. 1783–1807, 2015–2065).

## 0. Verdict

- **(a) Real errors in stated claims: none.** DeepSeek independently reproduced every Bjorn figure and all three §5.2 examples, and reports "no substantive mathematical error". Grok alleges none. The two discrepancies DeepSeek does report (minor 5 and minor 6) are its own misreadings (§3 below).
- **(b) Real gaps in the argument for stated claims: none.**
  - The §6.3 hedge ("I have not computed the bet there") is an acknowledged limit outside the essay's claims. Neither the thesis, nor the abstract, nor the conclusion depends on it (§2.1).
  - The tie worry about the Deference Done Better comparison is mistaken. The essay already deals with ties by deriving one direction through Weak Value, which is existential, and the other through Value, which is universal. DDB's Lemma B.13 is what makes the two equivalent (§2.2).
- **Recommendation: do not revise A6 tonight.** One optional clarity gloss (+9 words, O1 in §4) would head off the tie misreading. It fixes no (a) or (b) item, so it is optional under the brief.

**Scoreboard.** DeepSeek: major revision, confidence 4/5. Grok R3: revise and resubmit, leaning accept. Neither gives numerical scores, so there are no medians. Both praise:
- the correctness of Lemmas 1–3 and Theorems 1–2;
- the accuracy of the Bjorn figures;
- the CEU/VER/ANS tests;
- the candid positioning against DDB;
- §6.4's diagnosis (DeepSeek calls it "the paper's most valuable contribution").

## 1. Classification key

(a) real error in a stated claim · (b) real gap (missing assumption or unproved step) · (c) significance, framing or exposition request · (d) mistaken.

## 2. The two items the orchestrator singled out

### 2.1 §6.3: "I have not computed the bet there" (DeepSeek 3.3; README item 4 and author question)

**Class: (c), an acknowledged limit outside the claims. Not (b).**

1. **Where the claims are.**
   - The thesis (l.15) concerns finite statist, comparable K-normality models and does not mention Bjorn.
   - The Bjorn claims are scoped to the model the essay specifies: "In Goodman and Salow's model of repeated weighing" (abstract, l.3) and "in their own model" (conclusion, l.195).
   - §3 (l.51) specifies that model: G&S 2023 §6, the δ-ordering, independent Gaussian errors, and c≈1.96.
   - Those figures are verified by `formal.md` #28 and #30 and by DeepSeek's own recomputation.
   - DeepSeek's remedy (iii), "restrict the headline claim to the statist/probabilistic model as specified", is already how the abstract, §3 and the conclusion are worded.
2. **DeepSeek's premise is wrong.** It says the result is "conditional on a modelling choice the authors of the framework might reject". G&S n. 40 says three things:
   - Their model is the probabilistic account applied "relative to the question *what will the scales' errors be*".
   - The weight-relative application yields Goldstein and Hawthorne's model.
   - Contextualists can hold that "each model correctly describes what Bjorn 'knows' in different natural contexts", while for non-contextualists "we think our model is preferable".

   So §3 uses the framework authors' own model, which they prefer unless one is a contextualist. Even a contextualist accepts it as correct in contexts where the errors question is the operative one.
3. **The variant is plausibly outside the essay's statist scope.** This is my inference; I have not checked it against G&H's text. G&S n. 39 says Bjorn has no well-defined prior probabilities about his weight. So normality relative to the weight question would have to be fixed by probabilities given the readings, that is, by the evidence. §6.3 is headed "Statism and questions", and the conclusion (l.195) already says that what happens in non-statist models has not been shown.
4. **What does depend on it.** Only how robust the ten-to-one *weight-bet* illustration is for a contextualist who thinks a weight bet shifts the context. The essay flags exactly this ("A weight bet may make that question salient"). That is a robustness and significance point, honestly calibrated.
5. **Earlier pipeline decision.** The pipeline already decided this: `state/drafts/A6/revision_notes_v4.md` M5, "ACCEPT AS LIMITATION". That decision followed blind report P-7f1b S2-lit, which asked for "check … or flag it as open". DeepSeek adds no new consideration. The weight-relative computation is not in the repository; it would take new modelling choices and a fresh audit, so it cannot be done safely tonight.

**For a later version (all new argument, none for tonight):**
- Fetch Goldstein and Hawthorne 2022 and compute the 10:1 bet in the weight-relative model.
- Note that Lemma 1 is stated for an arbitrary assignment $M$ (l.75) and uses neither statism nor nesting. Its continuous analogue would need positive probability, as in A.5. So wherever the second reading defeats a known weight proposition, a bet on that proposition makes looking harmful. G&S n. 40 report that G&H predict No Defeat failures "even given MARGINS", but whether these occur with positive probability inside the current ken needs checking. Only the ten-to-one magnitude would then remain open.
- Note that the bet in §3 claim (i) concerns the readings, which plausibly keeps the errors question salient even for a contextualist.

### 2.2 Ties in the Deference Done Better comparison (DeepSeek 3.1 ¶2; README author question)

**Class: (d), mistaken. There is a small clarity residue.**

- **The definitions.** DDB's Weak Value is existential: "Given any 𝒪, there exists some recommended strategy S such that for all O ∈ 𝒪: 𝔼π(S) ≥ 𝔼π(O)" (p. 133). Value quantifies universally over recommended strategies (definitions, p. 132). Total Trust does not quantify over strategies at all.
- **Safety implies Weak Value.** KDT's policy with the fixed tie order is a legitimate DDB strategy. DDB require that $S_w=S_v$ whenever $P_w=P_v$. With full support, $P_s$ determines its support, which is the post-answer ken. KDT's choice is a function of that ken, and the essay states this step at l.23. The policy maximizes $\mathbb E_{P_s}$ at each $s$, so it is recommended. Ties only add further recommended strategies, and extra witnesses cannot falsify an existential claim.
- **Value implies safety.** KDT's policy is one of the recommended strategies.
- **Weak Value ⇔ Value.** This is DDB Lemma B.13 (p. 137). Its proof perturbs the options until the recommended strategy is unique, so DDB themselves dispose of ties.
- **Earlier audits.** This was already checked in `citations_final.md` D5–D7 and in `submission-ready-20261030/FINAL-REVIEW.md` (A6): "Fixed tie-breaking supplies a recommended strategy for each decision problem."
- **The residue.** The essay names "Weak Value" without glossing it. A reader without DDB to hand cannot see that its existential form is what makes ties harmless, and that is the source of the misreading. The optional gloss O1 (§4) fixes this.

## 3. All other substantive comments

| # | Source | Comment | Class | Reason |
|---|---|---|---|---|
| D3.1 | DeepSeek | Reframe around the diagnosis; lead with Bjorn and gappedness; present Thm 1(a) as a DDB corollary | (c) | The DDB debt and the increment are already stated (ll.21–25). Restructuring is for a later version. |
| D3.2 | DeepSeek | The abstract lacks the "suitable questions" qualification; the necessity direction is an artefact of the $p_v$ probes | (d) on the fact; (c) residue | Abstract l.3 reads "Given suitable questions". Thesis l.15: "with the requisite questions available". See also §3(iii) l.69 and §4 l.109. §3(i) with A.5 already shows a natural question (the second weighing) is unsafe at every situation, which answers the artefact worry. The residue is a natural-question restriction as an open problem; the conclusion (l.195) already lists "restrict the models or questions". |
| D3.3¶2 | DeepSeek | Consolidate the scope concessions in one section | (c) | Structure only. |
| D3.4 | DeepSeek | Derive the three rules on principle; say whether the list is exhaustive; add a sentence on ANS | (c) | §5.1 (l.115) names the three hypotheses, l.127 limits the formulas, and the conclusion disclaims exhaustiveness. Prop. 5 (l.157) and l.161 already tie ANS to CKD and to the 0.019 and 1.23 figures. |
| D3.5 | DeepSeek | The empty question can have positive value; is $V_x$ the right measure? | (c); no effect on any claim | At normal Bjorn situations the ken is $B(E)$, and every state in it has ken $B(E)$ (A.2's chaining step), so the empty question is worth exactly 0. Under K-normality the empty question is never negative (§6.1). So measuring a question against deferring, rather than acting now, gives $V(\Pi)-V(\emptyset)\le V(\Pi)$. Every negative verdict survives and can only get more negative. |
| D3.6 | DeepSeek | Table of values across $c$ | (c), supportive | The essay already says magnitudes depend on $c$ and gives $c\approx1.96$ and $c\approx2.45$. DeepSeek's table confirms the sign is stable, and A.5 proves a harmful bet exists at every situation. |
| Dm1–4 | DeepSeek | Shorter abstract; move the DDB paragraph; "statist" used before it is defined; notation table | (c) | Exposition; costs words. |
| Dm5 | DeepSeek | "$B(E)=\{\delta<c^2\}$, strict" | (d) | ≫ means δ is smaller by *more than* $c^2$, and the infimum of δ in E is 0 and attained. So a state is excluded iff $\delta>c^2$, giving $B(E)=\{\delta\le c^2\}$, as the essay says (l.53). The boundary is measure zero anyway. |
| Dm6 | DeepSeek | "may differ by up to 2c" | (d) | The source reads $\sqrt2c$ (l.53). Probably a text-extraction artefact (the radical was dropped, as the README reports for A5's superscripts). Rendering is outside this triage. |
| Dm7 | DeepSeek | Say which belief is lost in the 0.95 event | (c) | l.55 already says "Over the full state space, including the readings … These are different events." |
| Dm8 | DeepSeek | CEU when $D=\emptyset$ | (c), trivial | The options are then payoff-identical, so any verdict is harmless. No result uses this case: Theorem 3 has $D=E$, and every example has $D\neq\emptyset$. $K^D\neq\emptyset$ whenever $E\cap D\neq\emptyset$, because a ⪰-maximal state is in $B(E\cap D)$. |
| Dm9 | DeepSeek | Spell out the condition on $N$ | (d)/(c) | A.6 states $NP(s_0)>2$, which is sufficient. The exact condition is $(N+1)P(s_0)>1$; the referee's $NP(s_0)>1$ is also merely sufficient. |
| Dm10, 14 | DeepSeek | Parameters for 0.019 and 1.23; derive the A.5 ken formula | (c) | Verified in `formal.md` #33 and #25. Within a fixed $d$, δ orders states by $|\mu|$, so the derivation takes two lines. |
| Dm11 | DeepSeek | Rescaling changes magnitudes | (c)/(d) | l.177 already says a payoff ratio "is not an absolute measure of stakes". |
| Dm12–13 | DeepSeek | Code repository; page ranges | out of scope | Reproducibility and citation checks are excluded from this triage. |
| D-an | DeepSeek | The abstract's "factive" is stronger than Thm 2 needs | (d) | The abstract's "factive" belongs to the graded-corollary claim, which needs it ("a gapped set containing x contains C(x)"). Theorem 2 as stated (l.101) assumes no factivity. |
| G1 | Grok | Flag the dependence on statism, finiteness, comparability and K-normality | (c) | Largely already in the text (see the mapping in `v8_delta.md`). |
| G2 | Grok | Sharpen the positive upshot; use DDB to motivate the boundary | (c) | The conclusion (l.195) lists the options left open. Choosing among them is for a later version. |
| G3 | Grok | Is ANS viable, and is its cost decisive? | (c) | Addressed in §5.3 (l.163) and the conclusion. A firm verdict would be new argument. |
| G4–5 | Grok | Roadmap, gloss of Lemma 1, scope of the second weighing, numerics provenance, collapse reminder, continuity note | (c) | Mostly done: l.17, l.73, l.69, l.109, l.221, Cor. (i), A.6. |

## 4. Edits

**Required, to fix (a) or (b) items: none.**

**Optional clarity gloss.** It fixes no (a) or (b) item; apply it only if A6 is being re-rendered anyway. It adds no argument and costs +9 words by whitespace count (about 5,957; recount with `tools/wordcount.py` if it is applied). The gloss transcribes DDB p. 133 and matches the essay's own gloss of Value at l.21.

- **O1** (§1, l.23; the old string occurs exactly once)
  - Old: `Universal safety therefore implies their Weak Value condition, and Value implies universal safety;`
  - New: `Universal safety therefore implies their Weak Value condition (the same requirement for some, not each, recommended strategy), and Value implies universal safety;`

**Considered and not recommended:** a scope clause in §6.3 citing G&S's own relativization, or their preference for their own model absent contextualism (n. 40). It would be accurate, but it adds a dialectical move to a limitation the pipeline deliberately accepted. G&S's main text also says the probabilistic account needs a context-dependent question to be plausible (source ll. 1341–1347), so citing their preference alone could look selective.

## 5. Left for a later version

1. **The weight-relative Bjorn bet.** Fetch G&H 2022; compute the 10:1 bet; add the Lemma 1 transfer argument and the point that the claim-(i) bet keeps the readings question salient (all from §2.1).
2. **Reframing.** Lead with Bjorn and the gapped/graded diagnosis; make the DDB comparison §1.1; gather the scope caveats in one place.
3. **Robustness of Bjorn's numbers.** Add a short $c$-sensitivity table and say that the sign is the result while the magnitudes are model-dependent.
4. **Measuring against deferral.** One sentence saying that measuring a question against deferral strengthens every negative verdict (D3.5).
5. **The three rules.** Derive them on principle; test a fourth candidate (e.g. a smoothed CEU); give a verdict on whether ANS's cost is decisive.
6. **A natural-question restriction** (questions defined by observable variables), stated as an open problem or with a sufficient condition.
7. **Small clarity items:** the A.5 ken derivation, the $D=\emptyset$ convention, and the Weak Value gloss if O1 is not applied.
