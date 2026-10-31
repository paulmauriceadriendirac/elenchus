# A4 — substance-only triage of outside referee comments (31 Oct 2026)

**Essay:** `final/A4/essay.md`. This is v10 with patch P1, about 5,812 words per `v10_delta.md`.

**Comments triaged:**
- `relay/inbox/deepseek-20261031/A4-causation.md` (main report);
- the A4 parts of `README.md` and `00-overview.md` in the same folder;
- Grok Review 1 in `relay/inbox/grok-reviews-20261031.md`.

**Scope.** Argument substance only. No citation, compliance, formatting or word-count checks were run.

**Method.**
- I had no shell in this session, so I could not run `hp_audit.py`. I relied on the stored independent audit output `state/audit/A4/formal/hp_audit.out`. That output was reproduced byte-for-byte in `v10/hp_audit_rerun.out` and on a second machine (`ADDENDUM-reproduction.md`).
- I also used the author's run, `state/drafts/A4/v6_checks/v6_verify_output.txt`.
- I hand-derived every point below that bears on a classification.
- Nothing was written to `state/audit/A4/deepseek/`.

## 1. Bottom line

- **Scoreboard.**
  - DeepSeek: major revision, confidence 3/5. It says "No substantive mathematical error was found." It verified Theorems 1–2, the gain identities, the 355/5/2 counts and the Halpern (2015) quotations.
  - Grok: major revisions (borderline accept). It says "The formal results are correct on the stated assumptions."
- **No comment shows a false theorem, an invalid inference or an unsupported formal claim.** The thesis stands as stated. Decision: **CONTINUE**. There is no case for narrowing.
- **Two real (b) defects are worth fixing tonight.** Both are wording or scope problems, and each has a one-line fix:
  - **E1:** the p. 6 "In componentwise terms" sentence;
  - **E2:** a missing "under the modified definition" at line 90. Without it, the sentence clashes with the essay's own boundary score at line 104.
- **Three further edits close referee-raised points at near-zero risk** (E3–E5). Everything else is a (c) framing request or (d) mistaken. Those go to a later version or need no action.

## 2. Adjudication of the points that matter

### 2.1 p. 6, "In componentwise terms, the escape indexes the preorder by variable" — class (b), not (a)

**Raised by:** DeepSeek m10, README item 1, the overview, and the README question.

**What the definitions say.**
- §2 (l. 42) defines a componentwise filter by **one** preorder ⪰ on {n, l, f, u}, applied to every variable.
- §2 (l. 44) says componentwise filters are anonymous.
- So by Theorem 1, no componentwise filter admits Suzy's witness while excluding the switch witnesses.

**What line 124 says:** "In componentwise terms, the escape indexes the preorder by variable: f ⋡ n for the track and the left bell, while f ⪰ n for Billy's hit and the ducking."

**Is it false or self-contradictory?** No, on a careful reading.
- The sentence never says that a componentwise filter implements the escape.
- Its predicate, "indexes the preorder by variable", is exactly what takes the escape outside §2's class.
- Its content is correct. Audit §N: starting from each of the five calibrated preorders, dropping f ⪰ n and f ⪰ l for LT and L alone separates Suzy from both switches under the modified definition. Since n ~ l in every calibrated preorder, f ⪰ n is equivalent to f ⪰ l there. So "f ⪰ n for … the ducking" is true of the escape, even though the ducking's own witness tests f ⪰ l.

**Why it is still a real defect.**
- "Componentwise" is a defined term, and here it is used for something its definition excludes. That is the place where the paper's own impossibility result is at stake.
- The natural reading, "as a componentwise filter", contradicts §2 and Theorem 1. Two outside readers took it that way.
- This breaks QUALITY §3: use each technical term in one sense throughout.
- No theorem is affected.

**History.** The current wording is the formal audit's own patch P5 (29 Oct). P5 repaired an earlier version that really was false ("For a componentwise filter, that judgment is …"). E1 keeps P5's content (the track and the left bell; Billy's hit and the ducking) and changes only the frame. So it does not undo a past fix.

**README question.** Was the escape meant to lie outside the componentwise class, and does the SMT check cover it?
- Yes, it was meant to lie outside.
- The SMT check ranges over anonymous Pareto filters, so by design it does not cover this non-anonymous escape.
- Audit §N checks the escape separately, and it passes.

### 2.2 p. 4, "Suzy's throw is a cause exactly when each switch-setting is part of a cause" — class (d); optional 2-word clarification

**Raised by:** DeepSeek 3.3, README item 2, and the overview.

**The reading is fixed by the text.**
- §2 (l. 27): "A conjunct of a cause is *part of* a cause. Unless I say otherwise, '$X=x$ is a cause' below means that the single candidate $X=x$ is."
- The class is stated in the sentence itself: "Computation over all 355 preorders".
- The filter-before-AC3 convention is stated in the main text at l. 100 ("AC3 applied after filtering") and again in the Appendix.

So each of DeepSeek's three questions is already answered in the text.

**DeepSeek's reconstruction compares the wrong things.**
- Under the modified definition, {F, LT} is never a minimal cause. Its only not-φ world is (0,0,0,0), which is F's own witness world with W = {LT}.
- So if that world is admitted, AC3 fails for {F, LT}; if it is not admitted, {F, LT} has no witness at all.
- The claim never compares {ST, BT} with {F, LT}.

**Settled by computation, on the essay's reading.**
- Audit §E: "Suzy cause ⇔ Tracks flip part of a cause ⇔ Doorbells setting part of a cause (all 355) — 0 exceptions".
- It also holds with the switches read as single causes (355/355).
- The author's run agrees: "'ST singleton cause' == 'switch part of cause' in 355/355".

**Hand proof for componentwise filters (Tracks; Doorbells is the same, with M idle).**
- F has exactly one witness world, with the common profile P* (Theorem 1). A singleton satisfies AC3 trivially. So F is a cause iff P* is admitted, and then F is also part of a cause.
- Suppose P* is excluded, and take any not-φ world reached from a superset of {F}. It is one of three kinds:
  - (i) P*'s own world. That is excluded.
  - (ii) The world of a proper subset that omits F, such as [RT←0] at (1,0,0,0), with F at its actual value. AC3 fails if that world is admitted.
  - (iii) A world with A set to 0 against its equation (A: l→f). A componentwise filter admits this only if f ⪰ l. But then {A} alone, with profile {l→f}, is admitted, and AC3 fails.
- Hence F is part of a cause iff P* is admitted.

**Only risk.** On the misreading "Suzy is *part of* a cause iff each switch is", the claim would be false in 96 preorders. Those are the preorders where Suzy is a conjunct only together with Billy and the switches are in no cause, which is exactly what the essay's next clause describes.

**Fix.** Adding "by itself", the essay's own idiom at ll. 84, 128 and 132, removes the misreading at zero risk (E3).

### 2.3 l. 90, "any additive score that keeps the chain and the ducking counts both switches" — class (b), bordering on (a)

**Raised by:** this surfaced through DeepSeek m8 and m14. DeepSeek verified that under the older definitions the ducking is kept by the witness (F,B,K,H) = (0,1,0,1) at zero gain, and asked that the text say so. It did not connect this to l. 90.

**Why l. 90 holds only under the modified definition.**
- The inference at l. 90 runs through g_Boulder = c − a, the gain of Boulder's only *modified* witness.
- Under the original and updated definitions, the ducking has a second witness (Appendix l. 194) with gain r + d − b.
- The essay's own boundary score (2, 0, −1, −5, −3) (l. 104), under both older definitions:
  - keeps the chain (gain 4);
  - keeps the ducking (second witness, gain 2 − 3 + 1 = 0, admitted under ≥);
  - excludes both switches (gain −1).
- Hand-checked, and confirmed by audit §§G–H and the author's run ("boundary score orig/upd … BOULDER K True").

**Consequence.**
- Read across definitions, l. 90 is false, and l. 104 of the same essay contradicts it.
- Read as part of the Theorem 1 discussion (modified), it is true. The formal audit accepted it only "in modified-definition context" (row 11).
- The preceding paragraph ends "under each definition", so the scope is genuinely open.

**Fix.** E2 adds the qualifier. E5, optional, says in place how the ducking survives under the older definitions.

### 2.4 Grok 2, "parts of causes" — class (c) for the scope request; (d) for the Billy sub-point

**Billy sub-point: (d).** The Corollary already requires Billy's throw to be "out of every cause", so Billy as a conjunct already counts as a failure.

**Scope request: (c).** The single-candidate scope for the switches is an explicit, stated choice (l. 96), and there is no error.

**The parts reading would strengthen the dilemma, not weaken it.**
- l. 96 already shows that every anonymous Pareto filter that keeps the antidote admits the witness of {EF, LB} under the modified definition.
- Neither EF nor LB has a modified witness on its own (audit §C: the unfiltered modified causes are RB, TA and {EF, LB}). So AC3 holds and the flip is part of a cause (audit §I; author's run l. 118).
- So on the parts reading, the antidote, Pareto and Blocked tracks alone give the impossibility under all three definitions.
- The essay's "Whether this matters … I set it aside" undersells this.

**Caution.** If this is made explicit, §5's escape score also leaves the Blocked flip part of a cause under the modified definition (author's run l. 129: "SV cand EF: singleton False part True"). §5 does not claim otherwise, but the point opens a thread. Hence O1 is offered for later, not tonight.

### 2.5 Grok 4, uniqueness of the modified witnesses — class (b), trivially closable; the rest (c)

- In Theorem 1's proof, Suzy's uniqueness is argued ("freezing SH or BS at 1 restores the shattering"). The Tracks and Doorbells cases only assert it; the v10 delta audit noted the same.
- The step matters: another switch witness with a different profile would break "admits all three or none".
- It is true (audit §B: exactly one modified witness world each; DeepSeek checked by hand) and takes ten words per case to argue (E4).
- Grok's "separate lemmas" and code-availability requests are (c). Any code link would also raise anonymity issues.

## 3. All comments: classification

| Source | Comment | Class | Verdict |
|---|---|---|---|
| DS 3.1, W1; overview 2 | Anonymity result is near-analytic; reframe around the profile identities | (c) | The essay already lists the identities as increments (i)–(ii) and calls anonymity "a baseline" (l. 46). Later version. |
| DS 3.2, W2 | Sharpen novelty; Theorem 2 "is" Halpern's/Schumacher's observation | (c), partly (d) | Halpern, Xiao–Xiong, Halpern 2016 and Wysocki are all credited (ll. 15–19, 84). As quoted, Halpern's remark is informal ("normality considerations don't help"). The identity with prevention's witness and its quantification over all anonymous Pareto filters are the increment. Later: optional table. |
| DS 3.3; README 2; overview | Which "part of a cause"; which preorders; AC3 vs filter | (d) | §2.2 above. Optional E3. |
| DS 3.4, W3; overview 1 | Reproducibility, code | (c) | Not an argument defect; an independent reimplementation reproduces every number. Anonymity constraints. Not tonight. |
| DS 3.5, W4; m2 | Expand §5 (criteria for a successful ground); compress §7 | (c) | Later version. |
| DS 3.6; m13 | Lemma's dialectical role; "nonintervened roots fixed" redundant | (c) / (d) | The clause is redundant under the modified definition with fixed context (roots outside X are untouched or frozen at actual values), but harmless. It flags the premise the Xiao–Xiong application turns on (l. 162). The Lemma's proof is valid as written. |
| DS m1 | "transferable" vs "anonymous" in the abstract | (c) | Later. |
| DS m3 | Only intervened variables can be f or u | (c) | True by construction; nothing depends on stating it. |
| DS m4 | Root-default typicality used "silently" in Pareto | (d) | Pareto is defined by root deviant→default (l. 40). Both classes state the ranking ("counts a root's default as more typical"; r > 0). |
| DS m5, m6, m7, m9; Grok 6a | Case table; notation; "transitivity"; root cancellation in a − b | (c) | Later. |
| DS m8 | Ducking kept under older definitions via a zero-gain witness; say so | **(b)** | Correct, and it exposes the l. 90 scope gap (§2.3). Fix with E2 and E5. |
| DS m10; README 1, Q1 | "In componentwise terms" contradicts §2 | **(b)** | §2.1. Fix with E1. |
| DS m11 | Is the sprinkler activation a cause by itself? | (d) | Text accurate: "part of a cause" under §2. Computed: {FF, SA} and {SA, FW} are causes and SA alone is not (audit §J). The point (the preempted backup becomes causal) holds either way. |
| DS m12 | Make the "how long blocked" point a reductio | (c) | Later. |
| DS m14 | Text and Appendix agreement on Boulder's two witnesses | (d) for componentwise filters | The short-circuit verdict u ⋡ n excludes the second witness, so calibration is the same under all definitions, as the Appendix says (audit: same five preorders). For additive filters it feeds the l. 90 issue (E2). |
| DS m15; README Q2 | Halpern pagination; Halpern 2016 pinpoints | Out of scope | Citation matters. Fetch requests `a4-audit-halpern-2016-pinpoints.md` and `a4-v10-halpern-2016-p85.md` are already open. |
| Grok 1 | Defend the anonymity baseline as a natural class | (c) | Real request; needs new argument. Later version. |
| Grok 2 | Parts of causes; Billy | (c) / (d) | §2.4. Optional O1, later. |
| Grok 3 | Event coding does more work than acknowledged | (c) | Flagged as an explicit premise (P2), Objection 2, and the §5 inertial discussion. Later: say when the coding is independently motivated. |
| Grok 4 | Uniqueness arguments; computation edge cases; code | **(b)** for the uniqueness step; (c) for the rest | §2.5. Fix with E4. |
| Grok 5 | State the Wysocki increment crisply | (c) | Already in §1 (ll. 17–19). |
| Grok 6b | Gloss on the gain identity | (d) | Present: "telescopes into n→l and l→f". |
| Grok 6c | Admit the dilemma is partly about representation | (d) / (c) | Largely present: model aptness (l. 142), timing reply (l. 140), Objection 1. |
| Grok 6d | Anonymity analogue in Andreas–Günther | (c) | Later. |

## 4. Verdict

Yes, revise tonight, but only with the local edits below.

**Effect of the edits.**
- None adds an argument.
- Each claim they make is already verified in stored outputs: audit §§B, E, G, H, N and the author's run.
- None touches a theorem statement, citation or quotation.

**Estimated net words.**
- Tier 1 adds about 10 words; Tiers 1 and 2 together add about 42 (to about 5,855).
- I did not run a count; recount when the edits are applied.

**After applying.**
- Rebuild the PDF.
- Run the standard compliance pass (word count, injection), which was not done here.

**Resubmission caveat.** The README says the wording issue "survives in the submitted PDF". If replacing a submission is impossible or risky, the essay is defensible as it stands: these are wording and scope blemishes, not errors in the results.

**Tier 1 — fix tonight (the (b) items that read as inconsistencies)**

E1 (§5, l. 124). Old:
```
In componentwise terms, the escape indexes the preorder by variable:
```
New:
```
Recast as category comparisons, the escape is not componentwise, since it indexes the preorder by variable:
```
Shorter fallback (DeepSeek's wording, +1 word): `In variable-indexed componentwise terms, the escape indexes the preorder by variable:`. E1 is preferred, because "variable-indexed componentwise" is itself at odds with §2.

E2 (§4, l. 90). Old:
```
Compensation therefore does not help: any additive score that keeps the chain and the ducking counts both switches.
```
New:
```
Compensation therefore does not help: under the modified definition, any additive score that keeps the chain and the ducking counts both switches.
```

**Tier 2 — safe closures of referee-raised points (apply if time allows)**

E3 (§4, l. 84). Old:
```
Suzy's throw is a cause exactly when each switch-setting is part of a cause
```
New:
```
Suzy's throw is a cause by itself exactly when each switch-setting is part of a cause
```

E4a (Theorem 1 proof, l. 80). Old:
```
For Tracks, the only witness world is that of
```
New:
```
For Tracks, freezing $RT$ or $A$ at 1 restores the arrival, so the only witness world is that of
```

E4b (Theorem 1 proof, l. 82). Old:
```
For Doorbells, it is that of
```
New:
```
For Doorbells, freezing $R$ or $E$ at 1 restores the barking, so it is that of
```

E5 (§4, l. 104). Old:
```
also keeps prevention, the chain and the ducking.
```
New:
```
also keeps prevention, the chain and the ducking (the ducking through the witness $(F,B,K,H)=(0,1,0,1)$ that only the older definitions admit, with gain 0).
```

I checked with grep that each old string occurs exactly once in `final/A4/essay.md`, at ll. 80, 82, 84, 90, 104 and 124. No two edits overlap.

## 5. Left for a later version

- **Reframing.** Lead with the two profile identities and present the anonymity result as their corollary. Add a known-versus-new table (DS 3.1, 3.2; overview 2).
- **Defending the baseline.** Argue positively that transferable, profile-only policies are a natural class (Grok 1).
- **Parts of causes (Grok 2).** Optional O1 replaces l. 96's last two sentences.
  - Old: `Whether this matters depends on whether parts of causes are counted as causes. I set it aside and state the dilemma for single candidates.`
  - New: `So on a reading that counts parts of causes as causes, every anonymous Pareto filter that keeps the antidote counts the flip under all three definitions, and the dilemma needs no further case. I state it for single candidates, the reading on which the modified definition escapes Blocked tracks.`
  - The new text is valid by §2.4. If adopted, also note in §5 that the escape score leaves the Blocked flip part of a cause under the modified definition.
- **Event coding.** Say when it is independently motivated (Grok 3).
- **Presentation.** Category table for the central witnesses; uniform profile notation; "transitivity"; the root cancellation in the clear-tracks gain a − b (DS m5–m7, m9; Grok 6a).
- **§5.** Criteria for a successful non-anonymous ground; a reductio sentence for the inertial escape (DS 3.5, m12).
- **§6.** A framing sentence for the Lemma (DS 3.6); compress §7 or extend its anonymity analogue (DS 3.5, m2; Grok 6d).
- **Code.** Availability, subject to anonymity (DS 3.4; Grok 4).

## 6. Requests to the orchestrator

- None of E1–E5 needs new formal verification.
- Optionally, rerun `hp_audit.py` after applying them as a regression check; no formal claim changes.
- I could not run `tools/log.py` (no shell); please log this triage.
