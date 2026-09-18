"""Exhaustive search over ALL connected graphs on n vertices (via nauty geng) for a
counterexample to fvs <= 2*fp, using the rigorous upper bound UB(fp) of small_search.py.
Usage: python3 minimality.py <n>
"""
import subprocess
import sys
import networkx as nx

from build import all_cycles, max_disjoint, fvs_bruteforce
from small_search import fp_upper


def geng(n, args=("-c",)):
    p = subprocess.run(["geng", *args, str(n)], capture_output=True, text=True)
    for line in p.stdout.splitlines():
        line = line.strip()
        if line:
            yield nx.from_graph6_bytes(line.encode())


if __name__ == "__main__":
    n = int(sys.argv[1])
    tot = planar = deep = hits = 0
    for G in geng(n):
        tot += 1
        if not nx.check_planarity(G)[0]:
            continue
        planar += 1
        k, _ = fvs_bruteforce(G)
        if k < 3:          # fvs > 2*fp >= 2 forces fvs >= 3
            continue
        deep += 1
        ub = fp_upper(G)
        if k > 2 * ub:
            hits += 1
            print(f"COUNTEREXAMPLE n={n} fvs={k} UB(fp)={ub} g6={nx.to_graph6_bytes(G, header=False).strip()}")
    print(f"n={n}: connected={tot} planar={planar} fvs>=3={deep} counterexamples={hits}")
