# Causal Refinement and the Existence of a Direct Basis

**Abstract.** A theory that derives causation from globally direct regularities needs more than the existence of some such regularities. It needs a basis that connects the particular cause and effect. I establish this distinction for a deterministic relay interpretation of Andreas and Günther's regularity theory. In a specified class of ordered relays, their causal conditions hold exactly when a finite sequence of globally adjacent stages connects the candidate cause to the effect. Every finite representation of a relay can therefore support an endpoint verdict that its proposed global basis cannot recover. A dense relay illustrates an empty basis; an accumulating relay illustrates a missing final link; a third relay has an immediate predecessor at every stage except its source but still lacks the required connection. The last case defeats a merely local existence condition. The result is conditional on the admitted stage variables and stable regularities. Its philosophical consequence is a precise adequacy requirement for this reduction, rather than an unrestricted counterexample to the theory.

## 1. Direct links must do more than exist

A source sends a signal through a succession of stages to a receiver. A finite representation records a few stages and joins each to the next. More detailed representations insert further stages. At every finite resolution, the source remains connected to the receiver. Nevertheless, no particular link need remain direct throughout these refinements. If every interval admits another relevant stage, the globally direct links disappear.

There is a second possibility. Globally direct links may survive, and every stage except the source may even have an immediate predecessor. Yet the source and receiver can belong to different components of the surviving links. Local availability then fails to guarantee the connection needed for the endpoint verdict. This possibility matters because it defeats the natural repair of requiring a direct regularity at every caused stage.

My thesis is that, within a specified class of deterministic relays, Andreas and Günther's proposed direct basis recovers an endpoint causal verdict exactly when the endpoints are joined by a finite ascending sequence of covers. A cover is a pair of ordered stages with no stage between them. The result identifies the precise work an existence assumption must do. Merely having direct regularities, or having them everywhere locally, is insufficient.

The target is the model-independent construction in §5 of *A Regularity Theory of Causation* (Andreas and Günther 2024a). Their subsequent paper distinguishes the availability of a complete description from the assumptions needed to establish causal direction and develops a non-reductive account (2024b, §5.1.2). The present issue is different: even granting direction and a specified total domain, selecting globally direct regularities can lose connections preserved by every finite restriction. I do not claim that the authors have failed to notice model dependence, or that their later account endorses the reductive construction challenged here.

The argument has an explicit limitation. An ordered family of variables is not, by itself, a metaphysically possible causal process. The theorem applies once the stage variables count as apt, the stated regularities are stable, and the universe contains no additional direct route. These assumptions make the formal conclusion informative without concealing the remaining metaphysical question.

## 2. The regularity framework

Andreas and Günther represent a causal model by a set $L$ of direct non-redundant regularities and a set $F$ of true literals describing particular occurrences and absences (2024a, pp. 8–10). A non-redundant regularity expresses an effect as a minimally necessary disjunction of minimally sufficient conjunctions. The effect is placed on the left. Their entailment relation is ordinary classical entailment, so the formulas themselves permit backward as well as forward inference. A setting removes the regularities whose effect variables it sets, and adds the stipulated true literals. Settings thereby restrict how an actual occurrence can transmit information through the model.

For a candidate cause $C$ and effect $E$, their final account requires some $L'\subseteq L$ and $F'\subseteq F$ satisfying five conditions (2024a, pp. 17, 19). Both occurrences are actual. The facts $F'$ are maximal among subsets of $F$ that, together with $L'$, do not entail $E$. Setting first $F'$ and then $C$ in $L'$ must entail $E$. The specified excluded facts must satisfy the deviancy requirement. Finally, the laws for descendants of $C$ in the original model must remain in $L'$. This last requirement prevents the omission of an inconvenient causal route.

The central two conditions can be written:

$$L'\cup F'\not\models E,\qquad
F'\text{ is inclusion-maximal with this property},\tag{1}$$

$$\langle L',\varnothing\rangle[F'][\{C\}]\models E.\tag{2}$$

The model-independent proposal selects a more demanding stock of regularities (2024a, p. 26). Stability requires a regularity to remain non-redundant under every apt extension of the variable set. Apt extensions exclude stronger dependencies, such as logical or mereological connections, supervenience, and grounding. Metaphysical directness then rules out a specified factorization through other stable regularities. An antecedent variable in a regularity for $E$ must not also occur in a stable regularity for an intermediate $Z$ that itself occurs in a stable regularity for $E$.

The restriction to stable factors matters. A factorization through an inapt extra variable does not show that the original regularity lacks metaphysical directness. Nor does an arbitrary refinement of a graph establish the relevant kind of factorization. Conversely, a regularity can remain non-redundant while becoming indirect: its truth and indispensability need not vanish when another stage explains its mediation.

This essay considers that latter source of model dependence. It does not analyze the separate possibility that an extension makes a regularity redundant. Its relays keep the relevant regularities non-redundant while changing which ones are direct.

## 3. A specified relay interpretation

Let $(T,<)$ be a linearly ordered set of stages. For each $t\in T$, introduce a distinct Boolean event type $X_t$. A stage is an occurrence at a particular relative position in a repeatable transmission arrangement. These are stage types across cases, rather than new names for a single token event. The admissible type histories for this simplified relay are an inactive history, in which every $X_t$ is false, and an active history, in which every $X_t$ is true. The actual history is active, so

$$F=\{X_t:t\in T\}.$$

Time orders the types: a regularity connecting distinct stages is oriented from the earlier to the later. This grants one of the options Andreas and Günther explicitly discuss for one-cause structures (2024a, pp. 8–9). No argument below derives direction from the symmetry of a biconditional.

For $s<t$, write

$$R_{st}: X_t\leftrightarrow X_s.$$

Each such regularity is non-redundant relative to the two histories. The singleton $\{X_s\}$ is sufficient for $X_t$. Its empty subset is not, because the inactive history remains possible. The one-disjunct expression $X_s$ is necessary for $X_t$, whereas deleting its only disjunct leaves a false antecedent and fails in the active history. Adding other stages preserves both histories and these minimality facts.

Indeed, among consistent conjunctions of literals about other stages, the minimally sufficient conjunctions for $X_t$ are exactly positive singletons. Any sufficient conjunction that is realizable in the active history contains a positive literal; that literal alone suffices. A conjunction consisting only of negative literals is satisfied in the inactive history and is not sufficient. A contradictory conjunction containing a positive literal is not minimal either. A disjunction of two or more positive singletons is redundant, since one alone is already necessary and sufficient. Thus the non-redundant regularities in this vocabulary reduce to the pairwise ones, subject to the chosen direction. Self-dependence is excluded.

There are three substantive scope assumptions. First, distinct stage occurrences are apt variables: no stage is introduced as a logical abbreviation for another or as a part-description of an overlapping interval. Second, the pairwise regularities remain stable under the full range of admitted apt extensions. Third, the admitted universe supplies no additional direct regularity that provides an independent route between the stages. Specifying a complete toy domain makes these assumptions explicit; it does not prove that this is a complete description of a physical signal.

Define $s\mathrel{J}t$ when $s<t$ and no $u\in T$ satisfies $s<u<t$. If an intermediate $u$ exists, $R_{su}$ and $R_{ut}$ furnish the required stable factorization of $R_{st}$. Conversely, in the specified vocabulary a factorization has to use an earlier antecedent, an intermediate stage, and the same later effect. No such intermediate exists for a cover. Consequently the globally direct basis is

$$L_J=\{R_{st}:s\mathrel{J}t\}.\tag{3}$$

All actual positive literals are taken to be more deviant than their negative counterparts. This is a transparent assignment satisfying the occurrence-based default used by the target account, with no contrary norm stipulated. The result therefore does not turn on a disputed ranking of omissions.

## 4. The exact recovery condition

**Proposition.** For distinct $s,t\in T$, the final conditions of Andreas and Günther's 2024a account applied to $(L_J,F)$ classify $X_s$ as a cause of $X_t$ if and only if there is a finite ascending $J$-path from $s$ to $t$.

*Proof.* Begin with any proposed subset $L'\subseteq L_J$. Forget the orientation temporarily and regard its pairwise biconditionals as edges of an undirected graph. Let $K$ be the connected component of $t$, where connection means connection by a finite edge path. Every satisfying valuation of $L'$ is constant on each component. Different components may be assigned different truth values: all edges stay inside components.

These valuations are logical countermodels to the selected premises, not additional admissible type histories. This distinction follows from the account's classical entailment relation: once laws have been discarded, their constraints cannot be silently restored by restricting the valuations used to test entailment.

It follows that a set of actual facts $F'$ entails $X_t$ together with $L'$ exactly when it contains a literal from $K$. The unique maximal $F'$ satisfying (1) is therefore

$$F'_K=\{X_u:u\notin K\}.\tag{4}$$

This conclusion also holds when the domain is infinite. If no literal from $K$ is supplied, the valuation making $K$ false and every other component true is a countermodel. Maximality requires including every available fact outside $K$.

Setting $F'_K$ deletes no edge inside $K$. If $s\notin K$, setting $X_s$ cannot force $X_t$: the same valuation with $K$ false remains available. Suppose instead that $s\in K$. A cover graph of a linear order has at most one edge entering and at most one edge leaving a vertex. Its connected components are unbranched chains. Setting $X_s$ removes its incoming edge, if present, and fixes $X_s$ true. It then entails exactly the stages in $K$ reachable from $s$ by finitely many forward edges. If $t<s$, set the portion of the chain before $s$ false and the portion starting at $s$ true. The sole possible edge across that division was removed by the setting. This supplies a countermodel to (2). Thus any successful witness $L',F'$ requires a finite forward path in $L'$, and hence in $L_J$.

Conversely, suppose such a path in $L_J$ exists. Choose $L'=L_J$ and take $F'_K$ as in (4), now for the component in the full basis. The two endpoint occurrences are actual. Equation (1) holds by the component argument. Setting $F'_K$ and $X_s$ preserves the forward path and entails $X_t$, establishing (2). The stipulated deviancy ordering satisfies every relevant requirement on excluded facts. Choosing the whole basis leaves all descendant laws intact. All five conditions are satisfied. $\square$

The freedom to choose $L'$ cannot rescue a missing connection. Removing edges cannot create a forward path. The maximality condition also prevents facts outside the path from doing illicit work: it fixes the relevant background to the component complement, and those facts cannot bridge components.

Classical compactness explains part of the result but should not be overstated. A successful positive entailment has a finite subset of premises sufficient for that entailment. The entire causal test also includes maximality and constraints on omitted laws; compactness alone does not turn those requirements into a finite certificate. The component proof establishes the claim directly for this relay class.

## 5. Three ways a basis can fail

Consider first the dyadic stages in the unit interval:

$$D=\bigcup_{n\geq0}\{j/2^n:0\leq j\leq2^n\}.$$

Every distinct ordered pair has a midpoint in $D$. Thus $J$ is empty, and the proposition yields no causal connection between distinct stages. Nevertheless, every finite subset $V\subset D$ containing $0$ and $1$ has consecutive members. The direct basis relative to $V$ is its finite consecutive chain, which makes $X_0$ a cause of $X_1$. The disagreement is between taking directness globally and taking a causal verdict in each finite restriction.

A second example has stages $a_n=1-2^{-n}$ for $n\geq0$, together with the final stage $1$. The globally direct links $a_n J a_{n+1}$ exist. But no stage is immediately before $1$, and no finite cover path reaches it. The receiver is therefore uncaused in the global relay model, although every finite restriction containing source and receiver connects them. This establishes that a basis can be nonempty while failing at a particular endpoint.

The third example defeats the stronger local repair. Take the ordered sum

$$T=\mathbb N+\mathbb Z.$$

Write its stages as $a_0<a_1<\cdots$, followed by a second block containing $\cdots<b_{-1}<b_0<b_1<\cdots$. Every $a_n$ precedes every $b_k$. The notation specifies a perfectly coherent linear order; it is not a claim that there is a first member of the second block. If temporal coordinates are desired, put

$$a_n=\tfrac12(1-2^{-n}),\qquad
b_k=\tfrac34+\frac{\arctan k}{2\pi}.$$

Every stage except the initial $a_0$ has an immediate predecessor. Each $a_{n+1}$ immediately follows $a_n$, and each $b_{k+1}$ immediately follows $b_k$. Nevertheless, no link crosses from the first block to the second. Given $a_n<b_k$, the stage $a_{n+1}$ already intervenes. The direct graph has two components. In particular, $a_0$ has no finite cover path to $b_0$.

The proposition therefore denies that $X_{a_0}$ causes $X_{b_0}$. This is compatible with plentiful local causal verdicts: every noninitial stage has an immediate predecessor that counts as its cause. The condition that every caused stage occurs in a metaphysically direct regularity is satisfied, and even the stronger incoming-link condition is satisfied at every noninitial stage. Neither recovers the selected endpoint verdict.

Every finite restriction containing $a_0$ and $b_0$ nevertheless yields that verdict. A finite subset of the first block has a last member, and a finite subset of the second block has a first member. They become consecutive in the restriction, creating a bridge that disappears in the total domain. Recomputing directness after restricting the vocabulary must not be confused with restricting the global direct graph. These operations produce different graphs precisely at that bridge.

The appropriate adequacy condition is therefore relational. For each pair whose causal connection is to be recovered in this relay class, the effect must lie in the finite forward cover closure of the cause. A condition mentioning each stage separately does not suffice. Outside this class, branching, negative literals, and nontransitive cases require the full original conditions; the relay result is not a general replacement definition of causation.

## 6. What the result demands of a reduction

The formal alternatives are now exact. One can reject a proposed endpoint verdict, reject the specified relay domain as inapt, or accept that the globally direct basis is inadequate for that verdict. The theorem does not select an alternative by calling the construction a signal. A defender can reasonably deny that the two uniform histories contain enough structure to distinguish transmission from common dependence or coincident activation. That objection targets the causal interpretation, not the logical recovery result.

Likewise, different times do not automatically make distinct stage variables apt. A continuous process may be better represented by extended events, or some stage relations may be constitutive. The construction avoids the simple error of treating overlapping interval-parts as independent events, but it does not prove that instantaneous occurrences satisfy every metaphysical requirement. Its strongest justified application is conditional: if these relays are admitted with the stated endpoint verdicts, global directness imposes a finite-connectivity condition that excludes them.

This is a more demanding condition than a smallest positive temporal scale. An ordinary discrete chain can supply the required links without any uniform lower bound on their durations. Conversely, the third example has a predecessor for every noninitial stage and still fails. What matters is not a numerical grain but whether the relevant ordered intervals are generated by finitely composable covers.

A possible alternative assesses stable verdicts across finite representations. Define a relay-specific criterion: some finite representation containing $s,t$ classifies $s$ as a cause of $t$, and every larger finite restriction of the same specified domain does so. For the present relay class this criterion holds exactly when $s<t$, because every finite restriction supplies a consecutive chain between its ordered endpoints. It therefore agrees with the global-basis criterion on ordinary finite chains but disagrees in all three examples above.

This is a comparison, not a completed causal theory. If the quantifier ranged over all extensions, including the entire infinite domain evaluated by its global direct basis, the examples would no longer establish the proposed stability. Nor does local availability of direct regularities prove equivalence between the two criteria: the third example directly disproves that claim. An alternative criterion must specify both the permissible representations and the size of the extensions it quantifies over.

There is also a substantive cost to replacing directness. Its role in ordinary preemption is to preserve information about an inactive route; admitting arbitrary indirect regularities risks bypassing that information (Andreas and Günther 2024a, pp. 6–7, 10–11). A general theory based on stable finite verdicts would need to retain that discrimination and handle the account's short-circuit and switching cases. Success on the relays does not establish success on those cases.

The result thus sharpens an existence question into an adequacy test. A reduction through direct regularities owes a reason why its selected basis recovers the particular causal relations it intends to analyze. For ordered relays, that requirement is finite cover connectivity. Neither persistence through finite refinement nor the existence of a direct predecessor at each stage establishes it.

## References

Andreas, Holger, and Mario Günther. 2024a. “A Regularity Theory of Causation.” *Pacific Philosophical Quarterly* 105: 2–32. https://doi.org/10.1111/papq.12447.

Andreas, Holger, and Mario Günther. 2024b. “A Lewisian Regularity Theory.” *Philosophical Studies* 181: 2145–2176. https://doi.org/10.1007/s11098-024-02149-z.

