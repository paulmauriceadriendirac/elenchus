#!/usr/bin/env python3
"""Finite truth-table checks for A4 v2, using only the Python standard library.

The exhaustive test implements A&G 2024a (1)-(5) by valuations, settings,
maximal background facts, and law deletion. Its comparison oracle uses graph
reachability. Infinite claims are proved in the manuscript, not by this script.
"""
from functools import lru_cache
from itertools import product
from fractions import Fraction
from pathlib import Path
import json


def subsets(mask):
    sub = mask
    while True:
        yield sub
        if not sub:
            break
        sub = (sub - 1) & mask


def check_all_models(n):
    # Every selected edge is oriented i -> i+1. Missing edges give components.
    all_edges = (1 << (n - 1)) - 1
    valuations = range(1 << n)
    universe = (1 << (1 << n)) - 1
    atom = [sum(1 << v for v in valuations if v & (1 << i)) for i in range(n)]
    law = [sum(1 << v for v in valuations
               if bool(v & (1 << i)) == bool(v & (1 << (i + 1))))
           for i in range(n - 1)]

    @lru_cache(None)
    def models(edges, facts):
        out = universe
        for i in range(n - 1):
            if edges & (1 << i):
                out &= law[i]
        for i in range(n):
            if facts & (1 << i):
                out &= atom[i]
        return out

    def entails(edges, facts, effect):
        return not (models(edges, facts) & (universe ^ atom[effect]))

    @lru_cache(None)
    def maximal_backgrounds(edges, effect):
        out = []
        for facts in range(1 << n):
            if entails(edges, facts, effect):
                continue
            if all(entails(edges, facts | (1 << i), effect)
                   for i in range(n) if not facts & (1 << i)):
                out.append(facts)
        return tuple(out)

    def truth_table_verdict(full_edges, cause, effect):
        # Clause 5 requires the equations for every full-model descendant.
        required = 0
        j = cause
        while j < n - 1 and full_edges & (1 << j):
            required |= 1 << j
            j += 1
        for chosen in subsets(full_edges):
            if chosen & required != required:
                continue
            for facts in maximal_backgrounds(chosen, effect):
                # Clauses 1 and 4 hold under all-true actuality and the stated
                # positive-literal deviancy assignment. Perform both settings.
                setting = facts | (1 << cause)
                remaining = chosen
                for i in range(n - 1):
                    if setting & (1 << (i + 1)):
                        remaining &= ~(1 << i)
                if entails(remaining, setting, effect):
                    return True
        return False

    checks = 0
    for edges in range(all_edges + 1):
        for cause in range(n):
            reachable = set()
            j = cause
            while j < n - 1 and edges & (1 << j):
                j += 1
                reachable.add(j)
            for effect in range(n):
                if cause == effect:
                    continue
                actual = truth_table_verdict(edges, cause, effect)
                expected = effect in reachable
                assert actual == expected, (n, edges, cause, effect, actual, expected)
                checks += 1
    return checks


def check_minimality():
    checks = 0
    for n_other in range(1, 7):
        # A literal is -1, absent 0, or +1. Histories set all variables and
        # the effect to the common value 0 or 1.
        def sufficient(conj):
            return all(not all(lit == 0 or (lit == 1) == bool(value)
                               for lit in conj) or bool(value)
                       for value in (0, 1))

        for conj in product((-1, 0, 1), repeat=n_other):
            minimal = sufficient(conj) and all(
                not sufficient(conj[:i] + (0,) + conj[i+1:])
                for i, lit in enumerate(conj) if lit)
            expected = sum(lit != 0 for lit in conj) == 1 and 1 in conj
            assert minimal == expected, (conj, minimal, expected)
            checks += 1
    return checks


def check_restrictions():
    # Genuine dyadic refinements: every old cover is split at the next level.
    for n in range(7):
        old = [Fraction(j, 2**n) for j in range(2**n + 1)]
        refined = {Fraction(j, 2**(n+1)) for j in range(2**(n+1)+1)}
        assert all((a+b)/2 in refined and a < (a+b)/2 < b
                   for a, b in zip(old, old[1:]))

    # Finite sample of N + Z: induced full-domain covers have no bridge,
    # but recomputing covers within the finite restriction supplies one.
    stages = [('a', i) for i in range(4)] + [('b', i) for i in range(-3, 4)]
    global_covers_restricted = {(x, y) for x, y in zip(stages, stages[1:])
                                if x[0] == y[0] and y[1] == x[1] + 1}
    finite_restriction_covers = set(zip(stages, stages[1:]))
    assert finite_restriction_covers - global_covers_restricted == {(('a', 3), ('b', -3))}
    return {'dyadic_refinements': 7, 'ordered_sum_bridge_checks': 1}


if __name__ == '__main__':
    result = {
        'causal_truth_table_queries': {str(n): check_all_models(n) for n in range(2, 7)},
        'conjunction_minimality_queries': check_minimality(),
        'restriction_checks': check_restrictions(),
        'scope': 'Finite checks only; the manuscript supplies the infinite proof.',
        'result': 'PASS',
    }
    text = json.dumps(result, indent=2) + '\n'
    Path(__file__).with_name('A4-checks.json').write_text(text)
    print(text, end='')
