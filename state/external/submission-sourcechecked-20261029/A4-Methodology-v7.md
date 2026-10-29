# Methodology and verification: Causation

Companion to **A Switching Dilemma for Normality in Actual Causation**, version 7.

## Argument and source comparison

The essay compares witness transition profiles in explicit binary acyclic causal models under the original, updated and modified Halpern–Pearl definitions. Its impossibility claim is conditional on event coding, profile anonymity and the stated Pareto condition. It does not cover every principled normality ordering.

Halpern's *Actual Causality* was available for comparison, including the material on normality, late preemption and conservative extensions. The comparison with Wysocki's *Conjoined Cases* makes explicit that stronger normality obstructions already exist in a different setting. The claimed increment concerns identities across standard uncombined models and across the three definitions.

## Verification

The witness arguments were inspected directly. Under the modified definition the Suzy, Tracks and Doorbells witnesses share the same profile. Under the original and updated definitions the blocked-tracks witness adds one default-restoring root transition to the genuine-prevention profile. The additive identity is therefore
$$g_{\mathrm{Blocked}}=g_{\mathrm{Prevention}}+r.$$

The existing HP implementation was used to check the boundary score $(r,a,b,c,d)=(2,0,-1,-5,-3)$: the blocked-tracks witness has gain 3 and the clear-tracks witness gain 1. The supporting broader enumeration of preorders and random scores remains supplementary evidence; those complete searches were not repeated for this edition.

The general inference from separation to one particular frozen-mechanism inequality has been removed. That inequality is now restricted to additive repairs holding the other contributions fixed. The conformity lemma explicitly assumes a deterministic acyclic model with fixed context and nonintervened roots fixed.

## Scope and remaining limitations

The profile theorem establishes a limit on a baseline policy, not a refutation of normality-based causation. Alternative event codings, model choices and principled non-anonymous information can escape it. Applying the conformity lemma to Xiao and Xiong's availability requirement remains conditional on the fixed-context interpretation; changing exogenous background variables requires a separate analysis.

The principal open assessment is philosophical importance relative to the existing literature. The formal comparison may be useful, but the stronger novelty claim is not supported. This essay remains a reserve candidate. Review and computations are not independent expert endorsement.

## Matching files

The manuscript and anonymous PDF share the version 7 text. The source count is **5,520 words**, including title, abstract, headings, mathematical tokens and appendix; only the bibliography is excluded. This report is a scientific methods and verification note, not a complete production-history or eligibility audit.

