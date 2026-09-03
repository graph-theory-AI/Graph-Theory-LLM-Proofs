"""Second Mycielski iterate G_6 = mu^2(G) on 55 vertices: claimed
omega=4, zeta=6, chi=9. omega is cheap; chi and zeta are attempted with a
time budget (zeta lower bound = the expensive part: rule out a 5-cover).
"""
import sys, time
from graphlib import (from_edges, mycielski, zeta, chromatic_number,
                      clique_number, complement, bron_kerbosch)

n = 13
D = {1, 5, 8, 12}
edges = [(x, y) for x in range(n) for y in range(x + 1, n)
         if (x - y) % n not in D]
G = from_edges(n, edges)
M2 = mycielski(mycielski(G))
print(f"|V(mu^2(G))| = {M2[0]}  (claimed 55)")
t0 = time.time()
print(f"omega(mu^2(G)) = {clique_number(M2)}  (claimed 4)   [{time.time()-t0:.1f}s]")
t0 = time.time()
ncl = len(bron_kerbosch(M2)); nind = len(bron_kerbosch(complement(M2)))
print(f"maximal cliques: {ncl}, maximal independent sets: {nind}   [{time.time()-t0:.1f}s]")
t0 = time.time()
z = zeta(M2, ub=7)
print(f"zeta(mu^2(G)) = {z}  (claimed 6)   [{time.time()-t0:.1f}s]")
t0 = time.time()
c = chromatic_number(M2)
print(f"chi(mu^2(G)) = {c}  (claimed 9)   [{time.time()-t0:.1f}s]")
