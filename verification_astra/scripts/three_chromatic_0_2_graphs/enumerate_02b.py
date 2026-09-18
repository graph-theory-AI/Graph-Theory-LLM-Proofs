"""Enumerate connected (0,2)-graphs with geng, pruned by the counting bound
n-1 >= k(k-1)/2  (every vertex has exactly k(k-1)/2 vertices sharing 2 neighbours)."""
import subprocess, sys, itertools
import numpy as np, networkx as nx
sys.path.insert(0, __file__.rsplit('/',1)[0])
from enumerate_02 import is_02, chromatic_number, squares_span_cycle_space
GENG = "/usr/bin/geng"

def run(n, k):
    cmd = [GENG, "-q", "-c", f"-d{k}", f"-D{k}", str(n)]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True, bufsize=1<<20)
    cnt = 0
    for line in p.stdout:
        line = line.strip()
        if not line: continue
        cnt += 1
        G = nx.from_graph6_bytes(line.encode())
        if not is_02(G): continue
        bip = nx.is_bipartite(G); chi = chromatic_number(G)
        cd, rk = squares_span_cycle_space(G)
        flag = "LEMMA-FAILS" if rk != cd else "lemma-ok"
        mark = "   <<<< CHI=3 !!!!" if chi == 3 else ""
        print(f"FOUND n={n} k={k} g6={line} bipartite={bip} chi={chi} cycdim={cd} squarerank={rk} {flag}{mark}", flush=True)
    p.wait()
    return cnt

if __name__ == "__main__":
    nlo, nhi = int(sys.argv[1]), int(sys.argv[2])
    for n in range(nlo, nhi+1):
        for k in range(1, n):
            if (n*k) % 2: continue
            if k*(k-1)//2 > n-1: continue           # counting bound
            if (n*k*(k-1)) % 4: continue            # #lambda-2 pairs must be integral
            c = run(n, k)
            print(f"# scanned n={n} k={k}: {c} connected {k}-regular graphs", flush=True)
