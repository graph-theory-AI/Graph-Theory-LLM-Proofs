#!/usr/bin/env python3
"""Randomised (annealing) hunt, for n beyond exhaustive range, for
   (a) a counterexample to the imbalance conjecture, and
   (b) a violation of the writeup's truncated-tail lemma
         sum_{i>k} min(k,a_i) >= k(D-k)   for 1<=k<D,
       restricted to graphs with all edge imbalances positive.
   Also tracks the stronger clean form  sum_{all e} min(k,a_e) >= k*D.
Score minimised: 1000*(#zero-imbalance edges) + min_k slack."""
import random, itertools, sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from check_lemma import is_graphic

def stats(n, adj):
    deg = [len(adj[i]) for i in range(n)]
    edges = [(u,v) for u in range(n) for v in adj[u] if u < v]
    if not edges: return None
    imb = sorted((abs(deg[u]-deg[v]) for u,v in edges), reverse=True)
    z = sum(1 for x in imb if x == 0)
    D = max(deg); m = len(imb)
    if D < 2: return None
    slack_tail = min(sum(min(k,x) for x in imb[k:]) - k*(D-k) for k in range(1,D))
    slack_all  = min(sum(min(k,x) for x in imb)      - k*D     for k in range(1,D))
    return z, slack_tail, slack_all, deg, imb, edges

def anneal(n, iters=40000, seed=0):
    rnd = random.Random(seed)
    adj = [set() for _ in range(n)]
    for u,v in itertools.combinations(range(n),2):
        if rnd.random() < 0.3: adj[u].add(v); adj[v].add(u)
    best = None; cur = None
    for it in range(iters):
        u,v = rnd.sample(range(n),2)
        if v in adj[u]: adj[u].discard(v); adj[v].discard(u); undo=('add',u,v)
        else: adj[u].add(v); adj[v].add(u); undo=('del',u,v)
        s = stats(n,adj)
        sc = 10**6 if s is None else 1000*s[0] + s[1]
        T = max(0.01, 3.0*(1-it/iters))
        if cur is None or sc <= cur or rnd.random() < pow(2.718,-(sc-cur)/T):
            cur = sc
            if s and s[0]==0 and (best is None or s[1] < best[1]):
                best = s
        else:
            if undo[0]=='add': adj[u].add(v); adj[v].add(u)
            else: adj[u].discard(v); adj[v].discard(u)
    return best

overall = {}
viol = []
nongraphic = []
for n in range(8, 25):
    bn = None
    for seed in range(30):
        b = anneal(n, 30000, seed*977+n)
        if b is None: continue
        if bn is None or b[1] < bn[1]: bn = b
        if b[1] < 0: viol.append((n,b))
        if not is_graphic(b[4]): nongraphic.append((n,b))
    if bn:
        overall[n] = bn
        print(f"n={n:3d}  min tail-slack found = {bn[1]:4d}   (min sum_all-kD slack = {bn[2]:4d})"
              f"  deg={sorted(bn[3],reverse=True)}")
        sys.stdout.flush()
print()
print("lemma violations found :", len(viol))
for n,b in viol[:5]: print("   n=",n,"deg=",b[3],"imb=",b[4])
print("non-graphic M_G found  :", len(nongraphic))
for n,b in nongraphic[:5]: print("   n=",n,"deg=",b[3],"imb=",b[4])
