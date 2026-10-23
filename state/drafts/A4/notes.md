# A4 essay v1: notes

**Essay:** `state/drafts/A4/v1.md`. Word count by `tools/wordcount.py`: strict 5,763, wordlike 5,754. This is inside the 5,400–5,800 brief and over the CONFIG target of 5,600. The abstract is 149 words.

**Code:** `state/drafts/A4/models.py`.
- It is a copy of `state/ambitious/cards/A4_models.py`, extended at the end.
- The original checks still run unchanged with `python3 models.py --checks`.
- `python3 models.py --essay` runs the essay checks E0–E12 (about 7 seconds).

## Thesis in one sentence

Normality used as a filter on witness worlds can do one job, a licence requirement on deviant values. It cannot separate switching from preempting, because the two can be presented by models that agree in structure, actual values and defaults under every uniform coding.

## Results in the essay, and where each is checked

| Result | Claim | Hand proof | Machine check |
|---|---|---|---|
| Theorem 1 (necessity) | Under event, inertial or normal-course (all roots at default) coding, local uniform rankings are right on four cases iff l≡n, f≥n, u⋡n. The four cases: genuine prevention, chain, boulder, short circuit. | App. A; covers partial preorders | `--essay` E3, E4: exactly 2 of 75 weak orders survive, in all three definitions |
| Lemma (frozen witnesses) | A modified-HP witness without an equation violation means a root-level but-for cause. | yes | `--checks` §4: 423/423 random cases |
| Theorem 2(a) | Under event or inertial coding, Doorbells ≡ Locusts. | yes | E1 profiles; E4 MUS {DOOR:Df, NBP:Lo} in all definitions |
| Theorem 2(b) | Under either normal-course coding, Locusts ≡ short circuit. | yes | E4 MUS {NBP:Lo, SC:A} under C2 and C3 |
| Proposition 1 | Seedlings ≅ Doorbells, with identical defaults under all four codings. | isomorphism | E8, E10, E11 (licence, conformity, value-only, trigger; A&G (4) and (C5); NESS, CNESS) |
| Proposition 2 (A&G) | Generalizes Beckers's Backup 2, with the ancestor clause the kill test asked for. | yes | `--essay` E7: 41 random pairs, 0 counterexamples |
| Trigger-rule claim | Separates Doorbells from bare Locusts. | — | E9: under the original and updated definitions it fails only on Seedlings and the planted Locusts; under the modified definition it also fails on Billy's throw and the switch |

Coding note: under C3 (normal course given the background), Theorem 1's four cases admit 26 orders, so Theorem 1 is stated only for the other codings. Theorem 2(b) covers C3 without needing Theorem 1.

## Closest prior work and the exact increment

- **Halpern & Hitchcock 2015.**
  - What they did: the p. 19 conformity default, the p. 20 componentwise guideline, the §7.7 exceptions (pp. 34–36), the add-a-variable remedy (p. 36) and the question at p. 37.
  - Increment:
    - within the local uniform class, the exceptions (the licence rule) are forced and the default is excluded;
    - under the modified definition, the remedy is unavailable;
    - no ranking in the class handles Doorbells, Locusts and the short circuit together.
- **Halpern 2015.**
  - What he did: Ex. 3.9 treats the LT/RT switch by normality; Ex. 3.4 says the HH extension "applies without change" to the modified definition.
  - Increment: read as f<n, the LT/RT remark contradicts Theorem 1. The consistent (inertial) reading is defeated by Doorbells.
- **Beckers 2026.**
  - What he did: the switch/preemption dilemma for A&G, Backup 2, and the proof that A&G's 2025 definition is equivalent to their 2024 one.
  - Credited explicitly. Increment:
    - the counterexample needs no moral norm, and Proposition 2 predicts it;
    - the dilemma generalizes to every default-based account (Proposition 1), so no third horn exists.
- **Hitchcock 2007.**
  - What he did: default/deviant values, inertial variables, the PSR.
  - Used for the inertial coding and to motivate the trigger rule. Seedlings is the PSR-respecting version of Locusts.
- **Gallow 2021.**
  - What he did: Doorbells and its verdict (p. 85); his own model uses a four-valued switch variable.
  - The essay flags his multi-valued route variable, with route deviance, as the open alternative. It claims nothing about his theory's verdict on Locusts or Seedlings.

## What I read, and how

**Read in the relevant parts, from retrieved copies:**
- Halpern & Hitchcock 2015 (arXiv 1309.1226): pp. 16–37 (§§5–7, fns 8–18), in full for those pages.
- Halpern 2015 (arXiv 1505.00162): pp. 1–8, covering the definitions and Exs. 3.3–3.10.
- Beckers 2026 (arXiv 2606.24832v1): in full.
- A&G 2024 PPQ (local anchor):
  - pp. 5–8 (models, preemption);
  - pp. 12–19 (deviancy condition (4), omissions, Def. 2, condition (5), boulder);
  - pp. 26–29 (norms discussion, table).
  - Journal page = PDF page + 1. The plant-death quote is on p. 27, not the p. 26 the kill test gave.
- Gallow 2021 (pgrim.org copy): pp. 47, 83–86 only.
- Hitchcock 2007: pp. 495–511 (§§1, 5–7), read from a JSTOR-formatted copy on a course website (joelvelasco.net). The copy's provenance is unofficial, but the text is the published article.

**Not read at all:** Beckers 2021 (anchor). It is cited only for the NESS/CNESS definitions that the code implements; the kill test audited that code against Defs 4–9.

**Cited via others' presentations only:**
- Hall 2007: the LT/RT model, as Halpern 2015 (p. 8) attributes it.
- Hitchcock 2001: the boulder case, as A&G present it (p. 18).
- Halpern 2016: cited as unread, plus Beckers's (p. 10) report that it keeps a normality treatment of the switch.

**Unread; nothing is attributed to them:**
- Harinen 2017:
  - PhilSci-Archive returned a TLS failure, then 503;
  - PhilArchive returned 403;
  - academia.edu returned 403;
  - OpenAlex was rate-limited (429).
- Blanchard & Schaffer 2017: the search found no copy.
- The 2025 Australasian Philosophical Review symposium on A&G: not attempted, because the call budget was exhausted.
- A&G 2024 Phil Stud: unread. (C5) is taken from Beckers's statement of the 2025 definition.
- Synthese 2023, DOI 10.1007/s11229-023-04101-w, on isomorphs: unread.

**Web calls used: 12 of the 12 allowed.**
1. curl to PhilSci-Archive (TLS failure).
2. curl to PhilSci-Archive again (TLS failure).
3. WebFetch PhilSci-Archive (503).
4. WebSearch for Harinen.
5. WebFetch PhilSci-Archive eprint page (503).
6. WebFetch PhilArchive (403).
7. and 8. OpenAlex (429).
9. WebFetch academia.edu (403).
10. WebSearch for Blanchard & Schaffer.
11. WebSearch for Hitchcock 2007.
12. curl download of Hitchcock 2007.

The anchor PDFs (HH, Halpern, Gallow, Beckers 2026) were downloaded separately, as the brief directed.

**References:**
- `tools/verify_refs.py` returned VERIFIED for A&G 2024, Beckers 2021, Gallow 2021, HH 2015, Hitchcock 2001, Hitchcock 2007, Hall 2007 and Halpern 2016.
- Two were checked by hand:
  - Beckers 2026: arXiv PDF header "arXiv:2606.24832v1 [cs.AI] 23 Jun 2026"; title and author confirmed.
  - Halpern 2015: arXiv:1505.00162v1 PDF retrieved; title and author confirmed. It is cited as the arXiv version, because the IJCAI page range was not verified.

**Quotations:** all were checked word for word against the retrieved texts, with pages:
- HH pp. 18, 19, 20, 26, 34, 36, 37;
- Halpern 2015 pp. 6, 8;
- Gallow p. 85 (two quotations);
- Beckers 2026 p. 11;
- A&G p. 27.

The PSR is paraphrased, not quoted, because the OCR'd angle brackets were uncertain.

## Three weakest points

1. **Prior-art risk.**
   - Harinen 2017 ("normal effects") may already press the Locusts point against HH.
   - Blanchard & Schaffer 2017 and Synthese 2023 may already have "isomorphs that share their defaults".
   - Halpern 2016 may already restrict normality under the modified definition, which would pre-empt the lemma's point.
   - The APR 2025 symposium may contain A&G's refined deviancy notion.
   - All of these are unread. Fetch requests are needed before v2.
2. **Dependence on the binary route-variable format and on the verdicts.**
   - The essay concedes that aptness or effect grain may draw the line. Its significance therefore rests on how much the HP/A&G literature relies on binary route models; Halpern's three-variable switch model already avoids normality.
   - Doorbells is my binary simplification of Gallow's four-valued model.
   - The swarm-causes verdict could be contested on "normal effect" grounds. The essay replies, but Harinen is unread.
3. **The class restriction and the "triviality" charge.**
   - Theorem 1 is relative to local uniform rankings, which HH disclaim, and it does not hold under C3.
   - Proposition 1 is immediate from isomorphism; its value depends on readers accepting that the defaults coincide under every principled coding.
   - A referee could propose a principled non-uniform coding, for example a stricter inertial reading on which a freshly sown field counts as standing.

## Fixes against the kill test

- Numbers corrected: 75 weak orders, 2 survivors, 36 queries in 25 models. The original 32-query battery was extended by 4 queries.
- Theorem 1 is stated as a necessity result from four forcing cases; sufficiency is relative to the battery.
- Lemma restated against HH p. 36 (remedy) and p. 37 (their question). The kill test said HH raise no question; they do, on p. 37.
- A&G: Beckers is credited for the counterexample and the equivalence; Proposition 2 has the ancestor clause. I avoided Beckers's AG5/AG6 labels, because his reference list and his text appear to swap them.
- HH's rules are grounded in HH 2015 §6 (p. 19 assumption, p. 20 guideline), not in the "Default Rules" of the compact-representations paper.
- The Seedlings isomorph is new relative to the kill test. It answers the trigger-rule (non-local) escape that the kill test did not consider.
