# Causal Refinement Without a Final Layer

**Abstract.** A causal connection may survive every finite refinement of its representation even though no constituent connection remains direct under all refinements. I use this distinction to identify an existence condition on a strategy for eliminating model relativity. Andreas and Günther propose to recover causation in the world through stable, metaphysically direct regularities. The question is whether such regularities must exist in sufficient abundance to support the causal connections being analyzed. A sequence of finite relay graphs makes the issue precise: each graph connects its endpoints, but their dense union has no adjacent points. The elementary construction does not by itself constitute a counterexample to the regularity theory, because the admissibility of the refinements and their realization by stable regularities require further argument. It does establish that invariance of a verdict cannot supply the missing existence condition. The resulting choice concerns causal granularity: defend a basis of direct connections, restrict the reduction's domain, or explain connection without such a basis.

## 1. A connection can outlast its direct links

Consider a signal passing from a source to a receiver. A coarse description records only the source and the receiver. A more detailed description records an intermediate stage of transmission. A still more detailed description records a stage between each previously recorded pair. Suppose every such finite description supports the same verdict: the source's activity causes the receiver's response. Nothing in that supposition says that some pair of recorded stages will eventually prove incapable of further causal analysis.

This distinction matters when model independence is obtained by requiring directness under every admissible enlargement of a model. A verdict can remain stable while its representation in terms of direct connections continually changes. Consequently, agreement among the refined models does not establish that there is a final stock of direct connections from which the verdict can be recovered.

My thesis is conditional: a reduction through globally unmediated connections requires a substantive existence condition in addition to invariance under refinement. The condition must ensure that enough globally unmediated connections exist to support the causation the reduction intends to explain. Without it, increasing detail can preserve the represented connection while eliminating every candidate for membership in its proposed basis.

Andreas and Günther's (2024) regularity theory supplies a precise setting for this question. Their account of model-independent causation invokes stable regularities that are metaphysically direct. Their definitions specify what membership in this class requires. My concern is with the further question whether the class supplies the needed connections. The contribution attempted here is an analysis of that dependence, rather than a new mathematical result about dense orders or a completed counterexample to their theory.

The distinction also prevents a misplaced objection to model-invariance projects generally. A theory may establish that some changes of model preserve a causal verdict without reducing all causal structure to globally direct links. Gallow's (2021) project of model invariance should not be identified with the particular reductive strategy considered here. The target is the passage from persistent verdicts to an adequate final basis, wherever that passage is required.

## 2. Stability and directness answer different questions

In a finite relay model, a connection is direct when the model contains no intermediate relay through which it is represented as proceeding. Adding a relay may remove its directness without removing either its truth or the endpoint connection. This familiar feature of modeling becomes philosophically consequential when directness is made independent of the selected variables.

Andreas and Günther distinguish two requirements in their discussion of reductiveness (2024, §5). A non-redundant regularity is stable when it remains non-redundant under every apt extension of the variable set. Aptness excludes extensions that introduce dependencies stronger than causation, including logical and mereological relations, supervenience, and grounding. A stable regularity is metaphysically direct when it lacks the specified factorization through other stable regularities. Their proposal then uses metaphysically direct regularities, together with propositions of particular fact and their remaining conditions, to define causation without relativity to a selected model.

These requirements perform different tasks. Stability addresses the persistence of a regularity's non-redundancy. Directness addresses mediation. A regularity might remain a genuine, non-redundant connection between two variables while an additional variable reveals how the connection proceeds. Conversely, a connection might be direct in a poorly chosen model but fail the stability condition when the model is enlarged. Neither requirement should be substituted for the other.

The distinction creates a question of existence. It is possible to specify what would count as an element of a basis without establishing that anything meets the specification. It is also possible for the specified elements to exist but be too sparse to recover the connections at issue. Thus the needed condition is stronger than the claim that some metaphysically direct regularities exist somewhere. For each causal connection within the reduction's intended domain, an appropriate derivation must be available using such regularities.

The authors acknowledge the possibility that metaphysically direct regularities will be extremely fine grained. They also close their discussion with a conditional formulation concerning having those regularities available (2024, §5). I do not attribute to them a proof that an adequate basis must exist. The question is what realizing that conditional proposal requires. A very fine basis still contains elements. A process in which every candidate connection admits further relevant mediation need not have a smallest causal grain at all. Nothing about how small the pieces become guarantees that the refinement terminates.

## 3. The finite relay construction

The structural point can be stated without assuming a contested theory of causation. For each nonnegative integer $n$, let

$$D_n=\{j/2^n: j=0,1,\ldots,2^n\}.$$

Think of these numbers as labels for the stages recorded in a finite representation of transmission. In graph $G_n$, put a directed edge from $j/2^n$ to $(j+1)/2^n$ for each admissible $j$. Each graph has a directed path from $0$ to $1$. The next graph inserts a new stage between the endpoints of every previous edge.

Three facts are immediate. First, each graph is finite. Second, each refinement preserves the ordering of the previously represented stages. Third, an edge of $G_n$ becomes a two-edge path in $G_{n+1}$. An observer who records only the old stages therefore recovers the same endpoint connectivity. No disagreement about that connectivity arises at any finite stage.

Now let $D$ be the union of the $D_n$, with its ordinary strict order. For any $x<y$ in $D$, the midpoint $(x+y)/2$ is also in $D$ and lies strictly between them. A *cover* in an ordered set is an ordered pair with no element strictly between its members. Thus the order on $D$ has no covers.

Define the globally direct relation $J$ on $D$ by

$$xJy\quad\text{iff}\quad x<y\ \text{and there is no }z\in D\text{ with }x<z<y.$$

Then $J$ is empty. Its transitive closure is empty too. Although $0<1$, the ordered pair $(0,1)$ cannot be recovered as a finite chain of globally direct steps.

There is no paradox. Each finite graph has an endpoint path, but the paths are made of edges whose directness depends on that graph. There is no path made of edges that remain direct throughout the entire refinement family. The statement that every model has a witness to connectivity has a different quantifier order from the statement that connectivity has a witness composed of globally direct links.

The construction also separates two limiting operations. One can take the union of the finite models' reachability relations; this recovers the ordering on the dyadic points. Or one can first identify which ordered pairs are globally adjacent, then close those pairs under composition; this yields nothing. The failure of the two procedures to agree is exactly the structural problem for a reduction that requires the second procedure to recover what survives the first.

Allowing infinitely many direct steps does not repair this particular example. There is no globally direct first step from any point to any later point. An infinite sequence whose successive members are related by $J$ is therefore unavailable. A continuous path or an order-preserving map could represent passage through the interval, but it would use resources other than composition of members of $J$.

This is an elementary observation about dense orders. Its role is to prevent an invalid inference, not to establish a new theorem in order theory. Whether the construction describes an admissible causal possibility remains a separate question.

## 4. What the construction puts at issue

For an uncomplicated transmission process, consider the following commitments.

(P1) There is a causal connection between its initial and final stages.

(P2) Every candidate unmediated connection within the process can be factored through another admissible intermediate stage; the factorization is relevant to the proposed account of directness.

(P3) The endpoint connection must be recovered from globally unmediated connections within that process, with no independent direct basis elsewhere supplying the derivation.

The three commitments cannot jointly hold. By P2, there are no globally unmediated connections of the required kind. By P3, their absence prevents the proposed recovery. That conflicts with P1. The relay construction illustrates this conflict for an especially simple ordering.

P3 includes an important restriction. It rules out an explanation that obtains the endpoint connection through other variables or other regularities outside the relay ordering. A dense chain somewhere inside a rich causal system does not show that the system lacks every alternative direct basis. Any counterexample to a complete theory must exclude the alternative routes that theory actually allows.

Nor does P2 follow merely from the ability to add another variable to a diagram. A variable might be a duplicate name, a conjunction of existing variables, or a description of part of an event whose relation to it is constitutive. Such additions may fail the aptness condition. To apply the argument to Andreas and Günther, one would need to exhibit stable regularities whose relevant factorizations survive scrutiny under their definitions, not simply relabel a familiar causal sequence.

For that reason, the construction establishes a burden on the reductive strategy rather than a refutation of the published account. The burden can be stated precisely: explain why the admitted causal domain contains enough metaphysically direct regularities, or explain why recovering causation does not require the domain to contain them. Stability by itself does not answer the question, since stability need not prevent further mediation.

The burden is metaphysical when the proposal concerns causation in the world. In a finite practical model, adjacency is guaranteed by the chosen representation. A finite list of recorded transmission stages has neighboring members. But finitude of our description is compatible with further structure in what it describes. Moving from the finite representation to model-independent causation removes the very selection of variables that guaranteed those neighbors.

## 5. Three responses and their costs

A defender may deny that endless admissible mediation is possible. Perhaps causal processes have an ultimate grain, or perhaps the correct regularities cannot be factored indefinitely even if space and time are divisible. This response is coherent. It supplies the kind of existence condition the argument requests.

The distinction between temporal and causal divisibility is essential here. A continuum of times does not imply a continuum of causal intermediaries. The signal's state at one instant might stand in a relation of constitution, rather than causation, to a temporally extended transmission event. Alternatively, an appropriate causal description might take extended processes as basic. Nothing in the order construction settles these questions.

The price of the response is therefore not an implausible commitment to spatial atoms. It is a commitment to some reason why the relevant causal factorization stops or has enough irreducible structure. That reason must be supplied independently of the fact that finite models have direct links. If such a reason is available, the objection is answered for the domain it covers.

A second response restricts the reduction's domain. The theory might be intended for causal structures with an adequate direct basis. Then dense structures without such a basis fall outside its scope. The restriction could leave a valuable account of many ordinary cases. Its significance depends on whether the excluded possibilities are dispensable for the theory's intended metaphysics.

Here an explicit qualification matters. A theory of causation in causally discrete systems and a reduction of causation as such make different claims. The first is not discredited merely because it is conditional. The second cannot obtain its unrestricted scope from an assumption that causal structures have the form required for the reduction to work.

A third response abandons the requirement that connection always be recovered from globally unmediated pieces. The order on $D$ remains available despite its lack of covers. Likewise, a causal theory might characterize the relation among extended stages or impose conditions on whole families of finite representations. The absence of a direct basis would then cease to imply the absence of connection.

This response raises a new task. If the proposed reduction was intended to explain the causal relation through independent facts, it cannot simply insert that same relation as a primitive ordering. A family of models also requires a principled account of which representations belong to it and which changes preserve their subject matter. The dense-order example identifies a possible form for a replacement; it does not complete a reductive theory using that form.

The options consequently differ in philosophical commitment. One supports an adequate irreducible basis. Another accepts a restricted reduction. The third changes what a reduction must recover and how. Calling all three model independence would conceal the substantive choice.

## 6. Objections that remain decisive

The strongest objection is that the construction has not established a metaphysically possible instance of P2 satisfying the target theory's full conditions. That objection succeeds against any claim to have refuted the theory. A full counterexample would need a specified domain of particular facts, verified stable regularities, an account of apt extensions, and a demonstration that every potential direct derivation fails. The present argument supplies none of those by stipulating numerical labels alone.

Nevertheless, it would be a mistake to infer that the question of existence disappears. A definition of metaphysical directness can be perfectly precise and still fail to guarantee an adequate basis. If the proposed reduction depends on that guarantee, the gap must be closed by an additional argument, whether or not the relay structure can be realized.

A second objection is that ordinary causal judgments should be suspended for a process with endless mediation. P1 would then fail. This is another coherent response. It treats the availability of a direct basis as a condition on causation, rather than as a consequence of an independently accepted causal connection. To defend it, one would need to explain why preserving transmission at every finite level nevertheless leaves the endpoint verdict mistaken or unsupported. The formal construction itself does not decide that dispute.

A third objection concerns significance. The observation may be too general, and too familiar, to distinguish a particular contemporary account from longstanding discussions of direct causation. That is a genuine limitation of the argument's present form. Its force depends on locating an actual dependence on the missing existence condition and showing that a plausible response changes the account's commitments. Merely displaying another dense order would not advance the debate.

The justified conclusion is accordingly narrower than a rejection of regularity theories. Invariance of causal verdicts under finite refinement does not establish an adequate basis of globally direct connections. A reduction that relies on that basis must explain its existence. Once that explanation is explicit, disagreement can concern the world's causal structure rather than the harmless fact that our models omit detail.

## References

Andreas, Holger, and Mario Günther. 2024. “A Regularity Theory of Causation.” *Pacific Philosophical Quarterly* 105: 2–32. https://doi.org/10.1111/papq.12447.

Gallow, J. Dmitri. 2021. “A Model-Invariant Theory of Causation.” *The Philosophical Review* 130: 45–96. https://pgrim.org/philosophersannual/41articles/gallow-amodel.pdf.
