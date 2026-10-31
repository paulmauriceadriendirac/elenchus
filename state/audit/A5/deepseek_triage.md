# A5: substance triage of the outside referee comments (31 Oct 2026)

Essay: `final/A5/essay.md`. Comments triaged: `relay/inbox/deepseek-20261031/A5-lockean-holism.md` (main report), the A5 parts of `README.md` and `00-overview.md` in that folder, and Review 2 in `relay/inbox/grok-reviews-20261031.md`. I checked the Dorst text in `state/ambitious/sources/dorst-2019-lockeans.txt` (§4.2, pp. 193–195; proofs of Propositions 4–5, pp. 206–207), along with the earlier audit `state/audit/A5/formal.md` (N5, P4), so that nothing undoes an earlier fix.

Scope, as instructed: substance only. I ran no citation, compliance, formatting or word-count checks. Method: I proved the claims by hand. This session had no shell, so I could not run code. I wrote an exhaustive check script, `state/audit/A5/deepseek/family_check.py`, but **did not execute it**. Its expected last line is `ALL CHECKS PASS`. The verdict below does not depend on it.

## 1. Scoreboard

| Referee | Verdict | Confidence | Main concerns |
|---|---|---|---|
| DeepSeek | Minor revision | 4/5 | family version of Thm 2 unproved (3.1); Non-vacuity robustness (3.2); §5 length (3.3); premium-as-accuracy (3.4); textual basis of diagnosis (3.5) |
| Grok (Review 2) | Revise and resubmit, leaning accept | – | increment over D&M; motivation for the premium; Non-vacuity; exposition; "scope of Theorem 2" |

Neither referee gave numeric scores, so there are no medians. Both say they found no mathematical error. DeepSeek withdrew its only error claim, about the footnote 2 state counts, as a text-extraction artefact. I re-checked the proofs of Theorems 2 and 4 and the Theorem 3 equality conditions, and I agree.

## 2. The family claim (essay §4, last paragraph): true, with a one-line proof, but under-scoped

Current text (line 105): for a state-indexed family, "ME at each member's own state, together with BI read across the family (the increments $T^{B_0}_p$ and $F^{B_0}_p$ of $A_{B_0}$ at $B_0$ do not depend on $B_0$), yields fixed thresholds through Proposition 4 without collapsing the family into one separable measure."

**Set-up, from Dorst's text.** There is one measure $A_{B_0}$ per belief state. The p. 193 passage and the proof of Proposition 4 (p. 206) use only the increment of $A_{B^-}$ from $B^-$ to $B^-\cup\{p\}$. Dorst writes these increments as $T^{B^-}_p$ and $F^{B^-}_p$. Proposition 5's proof (p. 207) sets $T_p=T^{B^-}_p$ and $F_p=F^{B^-}_p$.

- (ME-own) For every $B_0$ and $p\notin B_0$, $A_{B_0}(B_0\cup\{p\},w)-A_{B_0}(B_0,w)$ depends on $w$ only through $[w\in p]$. Call its two values $T^{B_0}_p>0>F^{B_0}_p$.
- (BI-fam) $T^{B_0}_p=T_p$ and $F^{B_0}_p=F_p$ for every $B_0\not\ni p$.

**Proposition F.** Assume ME-own and BI-fam. Let $S(B,w)=\sum_{p\in B}v_p(w)$, with $v_p(w)=T_p$ if $w\in p$ and $F_p$ otherwise.
(a) Every increment Proposition 4 uses is an increment of $S$: for all $B_0$, $p\notin B_0$ and $w$, $A_{B_0}(B_0\cup\{p\},w)-A_{B_0}(B_0,w)=v_p(w)$.
(b) Fix any credence $C$. A state $B$ meets Proposition 4's condition for every $p$ iff $B$ maximizes expected $S$-accuracy. Here $p$ is taken as the last step, so $B^-=B\setminus\{p\}$ if $p\in B$ and $B^-=B$ if $p\notin B$. The thresholds are Corollary 2's, $\tau_p=-F_p/(T_p-F_p)$.
(c) Add Sequence-Irrelevance as Dorst uses it (Proposition 4 binds a rational final state in every order). Then every rational state is an $S$-optimum. With Non-vacuity, wherever the $S$-optimum is unique, it is the rational state.
(d) Non-collapse. The conditions constrain $A_{B_0}$ only on the pairs $(B_0,B_0\cup\{p\})$, so they force neither a constant family nor separable members. Example: $A_{B_0}(B,w)=S(B,w)+\beta\,[\,|B\triangle B_0|\ge2\,]\,[w\in\bigcap B]$ with $0<\beta<\min_pT_p$. It satisfies ME-own and BI-fam, and every member is strictly truth-directed from every state. No member is separable, and the family is not constant.
(e) Constant family. Here ME-own and BI-fam are just ME and BI for one measure. So Theorem 2(b) applies, and the measure is separable on the domain with the same $\tau_p$. This answers DeepSeek's 3.1(iii).

*Proof.* (a) follows from the definitions.

(b) For every $B^-\not\ni p$, the expected gain of adding $p$ under $A_{B^-}$ is $C(p)T_p+(1-C(p))F_p=e_p$. Since $T_p-F_p>0$, $e_p\ge0$ iff $C(p)\ge\tau_p$. So the conditions say exactly this: $p\in B\Rightarrow e_p\ge0$, and $p\notin B\Rightarrow e_p\le0$. Because $EA^S_C(B)=\sum_{p\in B}e_p$, these are exactly the conditions for $B$ to maximize $EA^S_C$ (essay §2).

(c) This follows immediately from (b).

(d) Under $A_{B_0}$, the states $B_0$ and $B_0\cup\{p\}$ are at symmetric-difference distance 0 and 1, so the extra term vanishes on every comparison Proposition 4 makes.
- Adding a true $p$ leaves $[w\in\bigcap B]$ unchanged. The extra term then moves by at most $\beta$, so the gain is at least $T_p-\beta>0$.
- Adding a false $p$ makes the new core false at $w$, so the gain is at most $F_p<0$.
- Non-separability: in $A_\varnothing$, adding $p$ to $\{q\}$ (with $q\ne p,\bar p$) gains $T_p+\beta$ at $w\in p\cap q$. Adding $p$ to $\varnothing$ gains only $T_p$. ∎

**Answers to DeepSeek 3.1.**
- (i) "ME at each member's own state" means the increments of $A_{B_0}$ from $B_0$, not from every $B$. The earlier audit's N5 shows that the member-by-member reading fails, so the current wording rightly avoids it.
- (ii) Yes, the argument works for families not generated by one measure. It uses only own-state increments.
- (iii) Yes; see (e).

**What is wrong with the current paragraph.** The claim is true. Classification: **(b) real gap, MAJOR but cheap.** There are two problems.
1. It is asserted without proof. QUALITY.md §3 requires formal claims to be proved.
2. As phrased, the paragraph reads as a concession: the dilemma of the preceding paragraph would then miss Dorst's actual, state-indexed framework. That is exactly the reading DeepSeek fears ("a defender can say that Dorst's state-indexed framework is untouched by Theorem 2"). It is false by (b): the second horn carries over to families. What a family adds to Corollary 2 lies only in comparisons Proposition 4 never makes. A related scope slip is in line 103, "If he excludes it, his §4.2 measures are separable on the domain". Read literally, this is false of state-indexed families, and line 105 says so. R1 below fixes both by scoping the dilemma to single measures and stating the family form.

**Two refinements for a later version** (not needed tonight).
- For families, background-independent *thresholds* are weaker than BI. One example is $(T^{B_0}_p,F^{B_0}_p)=\lambda_{B_0}(T_p,F_p)$ with $\lambda_{B_0}>0$. They already make Proposition 4's conditions equivalent to optimality under a separable measure, for instance one with values $1-\tau_p$ and $-\tau_p$. So the second horn does not need full BI.
- If §4.2's Maximize Expected Accuracy is read globally, a family's values away from its own state can add constraints and shrink the rational set. They can never add a non-Lockean rational state.

## 3. Classification of every substantive comment

(a) = real error in a stated claim; (b) = real gap; (c) = significance or framing request; (d) = mistaken, or already done.

| # | Source | Comment | Class | Assessment |
|---|---|---|---|---|
| 1 | DS 3.1; README item 3 and question; Grok "scope of Theorem 2" | Family version asserted, not proved | **(b)** | §2 above. Fix tonight with R1. |
| 2 | DS 3.2; Grok 3 | Say that the result does not depend on Non-vacuity or tie-breaking; acknowledge frameworks that do not guarantee a permitted state | (c)/(d) | Already done in §2 ¶2 and §7 ¶2. The optimum is unique at both credences, all optima agree in Theorem 1, and the remaining escapes are "rejecting this existence requirement" or excluding the score. The necessary-and-sufficient reading is a trivial special case. No edit. |
| 3 | DS 3.3 | §5 is long relative to its novelty; foreground the moral | (c) | Structural. Later. |
| 4 | DS 3.4; overview question; Grok 2 | Defend the premium as accuracy; why the core; how special it is | (c), partly (d) | Validity needs only that the score meets the conditions Dorst imposes (p. 193: "assumes only that $A_{B_0}$ is well-defined"; truth-directedness). §7 objection 1 argues this. Footnote 4 already shows that another holistic term, the closure bonus, is non-monotone. A positive defense would raise significance. Later. |
| 5 | DS 3.5 | Textual basis of the diagnosis unverified; quote Dorst | (d) as a problem | The source supports the essay. On p. 193, $t$ is chosen per world ("there must be some t > 0 such that …"), then named "$T^{B_0}_p$—the value, relative to $B_0$, of adding a true belief in p". On p. 207, "if we set $T_p = T^{B^-}_p$ and $F_p = F^{B^-}_p$". Dorst does note the background dependence (p. 193) and relies on Sequence-Irrelevance to remove it. That is precisely the step the content gap attacks, so nothing needs adjusting. A verbatim quotation is optional, needs a quotation check, and can wait. |
| 6 | DS minor 2 | Define "context"; does it include the credence function? | (c)/(d) | Already argued: Proposition 5's values are not functions of credences (§2 ¶5, citing p. 196), and the "Fixed context" paragraph holds values, question and context fixed. No edit. |
| 7 | DS minor 6 | Theorem 3's "iff its core maximizes Φ" may look inconsistent | (d) | The statement is correct. $EA_C(B)\le\Phi(\bigcap B)$, with equality exactly under the stated containment conditions, and $\max EA=\max\Phi$. |
| 8 | DS minor 9 | Explain why the positive-credence split works for the mean repair | (c) | The essay presents it as a computed instance, not as a consequence of the zero-credence argument. No claim lacks support. |
| 9 | DS minors 1, 3, 4, 5, 7, 8, 10, 12 | Abstract density, notation table, symmetry wording, forward reference, counting footnote, interval remark, wording in §7, proof annotation | (c) | Presentation only. Later. |
| 10 | DS minor 11 | Check the Dorst page numbers | out of scope | Citation check, excluded by the task. Incidentally, the pages I needed (193, 194, 195, 207) match the source's page footers. |
| 11 | Grok 1 | State the increment over Dorst and Mandelkern sharply and early | (d)/(c) | Already in §1 ¶5 and §5. The essay already contains the exact contrast Grok suggests (line 122: scoring a state by its conjunction's Jamesian value fails strict gains). No edit. |
| 12 | Grok 4 | Roadmap; interval intuition; refinement organization; four-world example earlier | (c), partly (d) | The roadmap exists (§1 ¶4, "The argument has three parts"). Grok's gloss, that the mean repair works only "under question-preserving refinements", misdescribes §6. The mean repair is exact for credence-zero splits, and the question-relative repair is the second one. No edit. |
| 13 | Grok 5 | Main-text reminder of the proviso; Theorem 4 proof should rule out states lacking the tautology | (d) | Footnote 3 already gives the reminder. The proof already says "every state lacking $\{u,v\}$ (adding it raises the score at both)". |
| 14 | Overview cross-cutting | Code availability; defensive framing; load-bearing idealisations | out of scope / (c) | Not argument problems. |

No comment identifies an (a)-class error, apart from the line 103 scope slip folded into item 1.

## 4. Verdict

**CONTINUE. One edit is worth making before tonight (R1).** It is safe for three reasons:
- every claim in it is proved in §2 above;
- it keeps the earlier audit's P4 reading, the one N5 vindicates;
- it adds no argument beyond the fix: one sentence of proof, and the scope statement that follows from it.

R2 is optional, for literal accuracy of line 103. O1–O3 are optional word-budget offsets, to be used only if the count requires them. No other comment justifies editing tonight.

### R1 (recommended) — §4, last paragraph (line 105)

OLD (occurs exactly once):

```
Theorem 2 concerns a single measure. Dorst's measures are indexed to the current state; for such a family, ME at each member's own state, together with BI read across the family (the increments $T^{B_0}_p$ and $F^{B_0}_p$ of $A_{B_0}$ at $B_0$ do not depend on $B_0$), yields fixed thresholds through Proposition 4 without collapsing the family into one separable measure. The counterexample is unaffected, since a state-independent measure is a constant family.
```

NEW:

```
Theorem 2 and this dilemma concern a single measure; Dorst's are indexed to the current state. For such a family, take ME at each member's own state and BI across the family: adding $p\notin B_0$ to $B_0$ changes $A_{B_0}$ by $T_p$ where $p$ is true and by $F_p$ where it is false, whatever $B_0$ is. That constrains each member only at its own state, so the family need not be one separable measure. But every increment Proposition 4 uses is then an increment of the separable measure with values $T_p$ and $F_p$, so a state meets Proposition 4's condition for every $p$ iff it is optimal under that measure, with Corollary 2's thresholds. The second horn thus extends to families. The counterexamples are unaffected, since a state-independent measure is a constant family.
```

Effect: it defines the family conditions (DS 3.1(i)) and covers families not generated by one measure (ii). It shows that the thresholds coincide with the separable ones (iii), and it proves the claim inline. It turns the apparent concession into the family form of the dilemma's second horn. "Counterexamples" (plural) covers both the record measure and footnote 4's closure bonus, each a constant family. Net change: about **+60 words** by whitespace count.

### R2 (optional) — line 103, literal accuracy

OLD (occurs exactly once): `If he excludes it, his §4.2 measures are separable on the domain, and §4.2 adds nothing to Corollary 2.`
NEW: `If he excludes it, a state-independent measure is separable on the domain, and §4.2 adds nothing to Corollary 2.`
Net 0 words. This is compatible with R1, but redundant given R1's first sentence.

### Offsets — only if `tools/wordcount.py` shows the essay over `target_words` after R1

Apply in this order. Each removes a restatement, not an argument. Each old string includes its leading space, occurs exactly once, and is replaced by nothing.
- **O2** (§6, line 152, −32 words): ` There are thus two distinct tasks: deriving a threshold within one representation, and showing that the threshold survives a change of representation. Success at the first does not automatically secure the second.`
- **O1** (§5, line 114, −16 words): ` The following theorem shows that comparing these core values suffices to find the optimal belief states.`
- **O3** (§3, line 61, −18 words): ` The increased confidence in the first world does not, by itself, settle which body of belief scores best.`

## 5. Preserve

- The counterexample and its numbers.
- Theorem 2 and its coefficient-matching proof.
- The quantifier-gap diagnosis, which the source text bears out.
- Theorem 4's scoping (sufficient, not necessary; stronger than the fixed-space result).
- The candour about Dorst and Mandelkern.
- The P4 wording "ME at each member's own state … BI read across the family". Do **not** revert to the member-by-member reading, which `formal.md` N5 refutes.

## 6. Left for a later version

1. State Proposition F, with the threshold-BI and global-MEA refinements in §2, as a numbered result with the proof in the appendix.
2. Give a positive defense of the premium: why the core rather than another interaction term, an independent test case, and what would count against it (DS 3.4; Grok 2).
3. Reposition §5 around the trade-off moral and move details to the appendix (DS 3.3).
4. Add one sentence on the necessary-and-sufficient reading of Maximize Expected Accuracy and on permissibility frameworks with no existence guarantee (DS 3.2; Grok 3).
5. Optionally quote Dorst p. 193 verbatim ("Write t as …"), after a quotation check (DS 3.5).
6. Make the expository minors: notation table, symmetry wording in the Theorem 1 proof, the counting bijection, the interval intuition, and why positive-credence splits survive the mean repair.

## 7. Requests to the orchestrator

- After R1, run `tools/wordcount.py` and apply O2 → O1 → O3 only if needed. Then re-run the usual pre-submission tools on the edited file. I ran none of them.
- Optional: `python3 -I state/audit/A5/deepseek/family_check.py`. It checks Proposition F (a)–(d) exhaustively on three worlds (256 states, all members, 65 credences, including credences at the threshold). I did not run it.
- Log the edit with `tools/log.py`.
