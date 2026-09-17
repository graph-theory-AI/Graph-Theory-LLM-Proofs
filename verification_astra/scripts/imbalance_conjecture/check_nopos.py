#!/usr/bin/env python3
"""Same as check_lemma.py but WITHOUT the positivity hypothesis:
find graphs whose imbalance multiset is NOT graphic, to calibrate how
load-bearing the hypothesis imb(e)>0 is, and to see how much slack the
writeup's truncated-tail lemma really has."""
import sys
sys.path.insert(0, __file__.rsplit('/',1)[0])
from check_lemma import g6_edges, is_graphic

worst = []
bad = []
cnt = 0
for line in sys.stdin:
    r = g6_edges(line)
    if r is None: continue
    n, edges = r
    if not edges: continue
    cnt += 1
    deg=[0]*n
    for u,v in edges: deg[u]+=1; deg[v]+=1
    imb=sorted((abs(deg[u]-deg[v]) for u,v in edges), reverse=True)
    if not is_graphic(imb):
        bad.append((line.strip(), deg, imb, sum(1 for x in imb if x==0)))
    # min slack of the lemma over k, restricted to the positive part
    D=max(deg); m=len(imb)
    s=min((sum(min(k,x) for x in imb[k:]) - k*(D-k)) for k in range(1,D)) if D>=2 else None
    if s is not None:
        worst.append((s, line.strip(), deg, imb))
worst.sort()
print("graphs with >=1 edge:", cnt)
print("M_G NOT graphic (no positivity assumed):", len(bad))
for g,deg,imb,z in bad[:10]:
    print("   ", g, "deg=",deg, "imb=",imb, "#zeros=",z)
print("smallest lemma slack (over ALL graphs, incl. imb=0 ones):")
for s,g,deg,imb in worst[:6]:
    print("   slack=",s, g, "deg=",deg,"imb=",imb)
