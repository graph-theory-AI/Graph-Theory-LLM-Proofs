"""Sanity check on the writeup's structural claims, over ALL graphs (not just regular
ones), for n <= 9: every (0,2)-graph found must be regular on each component, must
satisfy the matching property (1), must satisfy the Lemma, and must not have chi = 3.
This also covers disconnected graphs (geng without -c)."""
import subprocess, sys, os
import networkx as nx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enumerate_02 import chromatic_number, squares_span_cycle_space
from enum_fast import g6_adj, is_02_fast
from big_families import matching_property
GENG = "/usr/bin/geng"

nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 9
found = []
for n in range(1, nmax + 1):
    p = subprocess.Popen([GENG, "-q", str(n)], stdout=subprocess.PIPE, text=True,
                         bufsize=1 << 20)
    seen = 0
    for line in p.stdout:
        line = line.strip()
        if not line:
            continue
        seen += 1
        adj = g6_adj(line, n)
        if not is_02_fast(adj, n):
            continue
        G = nx.from_graph6_bytes(line.encode())
        degs = sorted(set(dict(G.degree()).values()))
        comp_reg = all(len(set(G.degree(v) for v in c)) == 1
                       for c in nx.connected_components(G))
        okm, _ = matching_property(G)
        cd, rk = squares_span_cycle_space(G)
        chi = chromatic_number(G)
        found.append((n, line, chi))
        print(f"n={n} g6={line:14s} degrees={degs} component-regular={comp_reg} "
              f"matching={okm} cycdim={cd} squarerank={rk} "
              f"lemma={'OK' if rk == cd else 'FAILS'} bip={nx.is_bipartite(G)} chi={chi}"
              + ("   <<<< CHI=3 !!!!" if chi == 3 else ""), flush=True)
    p.wait()
    print(f"# n={n}: scanned all {seen} graphs", flush=True)
print(f"# total (0,2)-graphs (incl. disconnected) on n<={nmax}: {len(found)}; "
      f"chi values seen: {sorted(set(c for _, _, c in found))}")
