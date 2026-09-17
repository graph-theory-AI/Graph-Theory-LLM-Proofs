"""Fast exhaustive search for connected (0,2)-graphs using nauty geng.

Pruning used:
  * a (0,2)-graph is regular (adjacent vertices have equal degree via the
    neighbourhood matching), so it suffices to enumerate regular graphs;
  * every vertex u has exactly k(k-1)/2 vertices v with |N(u) cap N(v)| = 2,
    because the k(k-1) length-2 paths leaving u are shared 2 per such v.
    Hence n-1 >= k(k-1)/2.
  * the number of lambda=2 pairs is n*k*(k-1)/4, so 4 | n*k*(k-1).

For each (0,2)-graph found we report bipartiteness, chromatic number, and whether
the writeup's Lemma holds (the quadrangles span the cycle space over R, equivalently
every square-closed antisymmetric edge function is a potential difference).
"""
import subprocess, sys, os
import numpy as np, networkx as nx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from enumerate_02 import chromatic_number, squares_span_cycle_space
GENG = "/usr/bin/geng"


def g6_adj(s, n):
    """decode graph6 -> list of int bitmasks"""
    data = [ord(c) - 63 for c in s]
    if data[0] == 63:
        raise ValueError("large graph6")
    bits = []
    for d in data[1:]:
        for i in range(5, -1, -1):
            bits.append((d >> i) & 1)
    adj = [0] * n
    idx = 0
    for j in range(1, n):
        for i in range(j):
            if bits[idx]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            idx += 1
    return adj


def is_02_fast(adj, n):
    for i in range(n):
        ai = adj[i]
        for j in range(i + 1, n):
            c = bin(ai & adj[j]).count('1')
            if c != 0 and c != 2:
                return False
    return True


def run(n, k, log):
    cmd = [GENG, "-q", "-c", f"-d{k}", f"-D{k}", str(n)]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
    seen = found = 0
    for line in p.stdout:
        line = line.strip()
        if not line:
            continue
        seen += 1
        adj = g6_adj(line, n)
        if not is_02_fast(adj, n):
            continue
        found += 1
        G = nx.from_graph6_bytes(line.encode())
        bip = nx.is_bipartite(G)
        chi = chromatic_number(G)
        cd, rk = squares_span_cycle_space(G)
        flag = "LEMMA-FAILS" if rk != cd else "lemma-ok"
        mark = "   <<<< CHI=3 !!!!" if chi == 3 else ""
        print(f"FOUND n={n} k={k} g6={line} bipartite={bip} chi={chi} "
              f"cycdim={cd} squarerank={rk} {flag}{mark}", file=log, flush=True)
    p.wait()
    print(f"# n={n} k={k}: scanned {seen} connected {k}-regular graphs, "
          f"{found} are (0,2)", file=log, flush=True)


if __name__ == "__main__":
    nlo, nhi = int(sys.argv[1]), int(sys.argv[2])
    log = sys.stdout
    for n in range(nlo, nhi + 1):
        for k in range(1, n):
            if (n * k) % 2:
                continue
            if k * (k - 1) // 2 > n - 1:
                continue
            if (n * k * (k - 1)) % 4:
                continue
            run(n, k, log)
