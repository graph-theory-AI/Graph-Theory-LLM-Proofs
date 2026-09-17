#!/usr/bin/env python3
"""Sparse-regime sweep: the truncated-tail lemma is tight for stars and
near-stars, so push the check into small-m graphs on larger n.

Reads graph6 on stdin.  For each graph with all imbalances positive:
  * verifies M_G is graphic (Erdos-Gallai);
  * verifies the lemma for every 1<=k<D with the WORST S (top-k, which
    minimises the tail since x -> min(k,x) is nondecreasing);
  * records the minimum slack over k.
"""
import sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from check_lemma import g6_edges, is_graphic

ok=0; bad_conj=[]; bad_lemma=[]; tight=0; minslack=None; minslack_g=None
for line in sys.stdin:
    r=g6_edges(line)
    if r is None: continue
    n,edges=r
    if not edges: continue
    deg=[0]*n
    for u,v in edges: deg[u]+=1; deg[v]+=1
    a=sorted((abs(deg[u]-deg[v]) for u,v in edges), reverse=True)
    if a[-1]==0: continue
    ok+=1
    if not is_graphic(a): bad_conj.append((line.strip(),deg,a))
    D=max(deg)
    sl=min((sum(min(k,x) for x in a[k:])-k*(D-k)) for k in range(1,D))
    if sl<0: bad_lemma.append((line.strip(),deg,a,sl))
    if sl==0: tight+=1
    if minslack is None or sl<minslack: minslack, minslack_g = sl, (line.strip(),deg,a)
print(f"hypothesis-satisfying graphs: {ok}   non-graphic M_G: {len(bad_conj)}   lemma violations: {len(bad_lemma)}   lemma-tight: {tight}")
if bad_conj: print("  CONJ FAIL:", bad_conj[:3])
if bad_lemma: print("  LEMMA FAIL:", bad_lemma[:3])
print("  min slack:", minslack, minslack_g)
