# Human input policy

Source of the rules: the competition's detailed rules and FAQ
(https://www.zacharygoodsell.com/ai-philosophy-competition-rules.html and
https://www.zacharygoodsell.com/ai-philosophy-competition-faq.html; re-read them in Phase 0).
This file is our operational summary in our own words; where they differ, the live pages win.

**The test.** Did an AI originate and develop every substantive philosophical contribution in the
essay — ideas, arguments, theories, distinctions, objections, replies, cases? Humans may set the
task, build the workflow, choose among AI outputs, fetch materials, and give generic feedback that
names a problem without supplying its diagnosis or solution.

## How the orchestrator handles every human message

1. Log it verbatim: `python3 tools/log.py human --class <class>` with the text on stdin.
2. Classify it as one of:
   - `logistics` — run control: start, pause, resume, change a CONFIG value, "skip the relay".
   - `courier` — a fetched source or a pasted reply from another AI model, delivered unedited.
   - `topic-choice` — a topic, question, debate, text, tradition or position to defend/attack, so
     long as the position is not itself a novel contribution.
   - `selection` — choosing among AI-generated candidates or drafts.
   - `generic-feedback` — names a problem without philosophical content (menu below).
   - `method` — a generic methodological instruction (list below).
   - `rejected-substantive` — contains a premise, argument, distinction, case, counterexample,
     objection, reply, diagnosis, or a novel thesis, or steers toward one by hint.
3. Act on every class except `rejected-substantive`. For that class: do not act on any of its
   content, say which rule it would breach, and ask for a generic rephrasing. If a message mixes
   classes, act only on the permitted part and say exactly what was set aside.
4. Never let rejected content leak: do not paraphrase it into a task, a plan, or a file other than
   `methodology/human_inputs.md`.

## Permitted generic methodological instructions (examples)

Make the premises explicit · test whether the argument is valid · compare several possible
arguments · look for counterexamples · consult the relevant literature · check whether the idea
is already in the literature · write an objections-and-replies section · rewrite or rearrange a
part · delete material · check quotations, references and formal reasoning · consult the
PhilPapers Survey or other data on what philosophers find contested or important · study
prize-winning or "best of the year" papers to calibrate what counts as a contribution · use
methods from experimental philosophy or metaphilosophy to evaluate claims · read the published
literature on AI-generated philosophy · ask another AI model to referee or criticise.

## Generic feedback menu (the human may say any of these verbatim)

- This section is unclear.
- I'm not persuaded by the central argument.
- This premise needs more support.
- This reply does not answer the objection.
- Consider whether there are counterexamples to the main thesis.
- The contribution relative to existing work is not clear.
- Check whether this idea already exists in the literature.
- The essay tries to do too much. / The essay does too little.
- The introduction does not state the thesis clearly.
- The significance of the result is not explained.
- Engage more with the most relevant literature.
- Verify the formal claims.
- Cut material that does not serve the main argument.
- Look for the strongest objection a specialist would raise.

Adding *why* ("…because it overlooks the difference between X and Y") turns feedback into a
substantive contribution. Name the problem; let the agents find the reason.

## Borderline cases, decided

| Human says | Class | Why |
|---|---|---|
| "Write about <a named debate>." | topic-choice | A topic. |
| "Defend <a named, established position>." | topic-choice | A known position, not a novel one. |
| "Read everything philosopher P wrote and extend it in light of recent science." | topic-choice + method | Choosing a corpus and a direction is permitted; the agents choose which science and what the extension is. |
| "…extend P's account of A using discovery D." | rejected-substantive, unless the pairing of P and D is already standard in the literature | When the pairing is the insight, naming it supplies the idea. |
| "Consult the PhilPapers Survey to see which questions are contested." | method | Topic research. |
| "Look at the prize-winning papers to see what works." | method | Calibration. |
| "Here is a PDF you asked for." | courier | Fetching on request. |
| "Here is a paper you should read" (unrequested, chosen by the human) | courier if the paper is broadly relevant; rejected-substantive if its selection effectively hands over an argument | The rules forbid curating materials so narrowly that the selection supplies the argument. |
| "Your reply to objection 2 is weak." | generic-feedback | Names a problem. |
| "Your reply to objection 2 fails because premise 3 is false." | rejected-substantive | Supplies the diagnosis. |
| "Isn't there a counterexample where…" | rejected-substantive | Supplies a case. |
| "Use a formal model." | method | Generic. |
| "Use a formal model with features X, Y and Z." | rejected-substantive | Fine control over method. |
| "I prefer candidate B." | selection | Choosing among outputs. |
