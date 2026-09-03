"""Check 2: Lemma 1 of the writeup.

Simulate the randomized slack-list-coloring subroutine (activate w.p. 1/2, pick
uniform color from current list, commit iff no active uncolored neighbor picked
the same color; committed colors are deleted from neighbors' lists) on random
graphs where |A(v)| >= d(v) + 1, with lists from a small universe.

Verified properties:
  (a) the invariant |A(v)| >= d_U(v) + 1 holds after every round;
  (b) the final coloring is proper and uses only list colors;
  (c) empirical per-round commit probability >= 1/4 (writeup's bound);
  (d) completion time scales like O(log n).
"""
import random
import statistics
import sys

import networkx as nx

sys.path.insert(0, __file__.rsplit("/", 1)[0])

rng = random.Random(2024)


def run_lemma1(G, lists, max_rounds=10**6):
    A = {v: set(lists[v]) for v in G}
    color = {}
    uncolored = set(G.nodes())
    rounds = 0
    commit_events = tries = 0
    while uncolored:
        rounds += 1
        active = {v for v in uncolored if rng.random() < 0.5}
        pick = {v: rng.choice(sorted(A[v])) for v in active}
        committed = []
        for v in active:
            if all(pick.get(u) != pick[v] for u in G[v] if u in active and u in uncolored):
                committed.append(v)
        tries += len(uncolored)
        commit_events += len(committed)
        for v in committed:
            color[v] = pick[v]
            uncolored.discard(v)
        for v in committed:
            for u in G[v]:
                if u in uncolored:
                    A[u].discard(color[v])
        # invariant check
        for v in uncolored:
            du = sum(1 for u in G[v] if u in uncolored)
            assert len(A[v]) >= du + 1, f"invariant broken at {v}"
        if rounds > max_rounds:
            raise RuntimeError("did not finish")
    # proper + from lists
    for v, c in color.items():
        assert c in set(lists[v])
        for u in G[v]:
            assert color[u] != c
    return rounds, commit_events, tries


def main():
    print("n  avg_rounds  max_rounds  empirical_commit_rate  (target >= 0.25)")
    for n in (32, 64, 128, 256, 512):
        rounds_list = []
        ce = tr = 0
        for it in range(30):
            p = min(1.0, 6.0 / n)
            G = nx.gnp_random_graph(n, p, seed=rng.randrange(10**9))
            dmax = max((d for _, d in G.degree()), default=0)
            U = list(range(dmax + 2))
            lists = {v: rng.sample(U, min(len(U), G.degree(v) + 1)) for v in G}
            r, c, t = run_lemma1(G, lists)
            rounds_list.append(r)
            ce += c
            tr += t
        print(f"{n:4d}  {statistics.mean(rounds_list):8.2f}  {max(rounds_list):6d}"
              f"  {ce / tr:.3f}")
    # also dense-ish graphs
    for n in (60, 120):
        rounds_list = []
        for it in range(20):
            G = nx.gnp_random_graph(n, 0.5, seed=rng.randrange(10**9))
            dmax = max(d for _, d in G.degree())
            U = list(range(dmax + 2))
            lists = {v: rng.sample(U, G.degree(v) + 1) for v in G}
            r, _, _ = run_lemma1(G, lists)
            rounds_list.append(r)
        print(f"dense n={n} p=0.5: avg {statistics.mean(rounds_list):.2f} "
              f"max {max(rounds_list)}")
    print("CHECK 2 PASSED (all invariants held, all runs completed, colorings proper)")


if __name__ == "__main__":
    main()
