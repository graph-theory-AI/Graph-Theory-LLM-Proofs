"""Referee check for 2004.07214__00, Section 5 (input representation):

Claim: an occurrence of S_t in a poset corresponds in G = Inc(P) to an induced
K_t (join by perfect matching) K_t, and every transitive orientation of the
complement pattern (K_{t,t} minus a perfect matching) yields a poset isomorphic
to S_t.  Hence S_t-freeness does not depend on the chosen transitive
orientation.

We enumerate ALL transitive orientations of K_{t,t} minus a perfect matching
for t = 2, 3, 4, 5 and check each resulting strict order is isomorphic to S_t.
"""

import itertools


def transitive_orientations(edges, n):
    """All orientations of the given undirected edges that are transitive
    (as strict orders on [n], only among the given adjacent pairs)."""
    edges = list(edges)
    for bits in itertools.product([0, 1], repeat=len(edges)):
        rel = set()
        for (e, b) in zip(edges, bits):
            rel.add(e if b else (e[1], e[0]))
        # transitivity within the orientation, and no path shortcuts through
        # nonadjacent pairs
        ok = True
        for (a, b) in rel:
            for c in range(n):
                if (b, c) in rel:
                    if (a, c) not in rel:
                        ok = False
                        break
            if not ok:
                break
        if ok:
            yield rel


def standard_example(t):
    """S_t on elements a_i = i, b_j = t + j."""
    return {(i, t + j) for i in range(t) for j in range(t) if i != j}


def isomorphic(rel1, rel2, n):
    for perm in itertools.permutations(range(n)):
        if {(perm[a], perm[b]) for (a, b) in rel1} == rel2:
            return True
    return False


def main():
    for t in range(2, 6):
        n = 2 * t
        # complement pattern: K_{t,t} minus perfect matching,
        # shores {0..t-1} and {t..2t-1}, matching i -- t+i removed
        edges = [(i, t + j) for i in range(t) for j in range(t) if i != j]
        st = standard_example(t)
        total = 0
        good = 0
        for rel in transitive_orientations(edges, n):
            total += 1
            if isomorphic(rel, st, n):
                good += 1
        print(f"t={t}: K_{{t,t}} minus PM has {total} transitive "
              f"orientations, {good} isomorphic to S_t "
              f"({'OK' if total == good and total > 0 else 'PROBLEM'})")


if __name__ == "__main__":
    main()
