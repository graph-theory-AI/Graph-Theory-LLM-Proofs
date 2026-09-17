"""Check the writeup's intermediate numeric/structural claims on G and H."""
import sys, itertools
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/2008.03587__00')
from zgame import all_dist, solve
from counterexample import build, G, H, gn, gi, hn, hi

d = all_dist(G)
v0, v2, v4 = gi[('v',0)], gi[('v',2)], gi[('v',4)]
A = {gi[('v',0)]} | {gi[('A',j)] for j in range(1,25)}
B = {gi[('v',2)]} | {gi[('B',j)] for j in range(1,17)}
C = {gi[('v',4)]} | {gi[('C',j)] for j in range(1,9)}
outA = [v for v in range(len(G)) if v not in A]

print("connected:", all(x >= 0 for x in d[0]))
print("|A|,|B|,|C| =", len(A), len(B), len(C), " pairwise disjoint apart from path:",
      A & B == set() and A & C == set() and B & C == set())
print("max d(v0, x) over x outside A =", max(d[v0][x] for x in outA), "(writeup: 10)")
print("max d(v0, x) over x in A      =", max(d[v0][x] for x in A), "(writeup: 12)")
print("vertices outside A at distance 1 from v0:", [gn[x] for x in outA if d[v0][x]==1])
print("max d(v2,x) for x in B =", max(d[v2][x] for x in B), " max d(v4,x) for x in C =",
      max(d[v4][x] for x in C))
print("for x in A: d(x,v2)=d(x,v0)+2 :", all(d[x][v2]==d[x][v0]+2 for x in A))
print("for x in A: d(x,v4)=d(x,v0)+4 :", all(d[x][v4]==d[x][v0]+4 for x in A))
print("exceptional case (D,t)=(1,12): d(x,v2)=14 for the antipode, d(v1,v2)=1 :",
      [ (gn[x], d[x][v2]) for x in A if d[v0][x]==12 ], d[gi[('v',1)]][v2])

# --- Section 3 case analysis, exhaustively: for EVERY pair of starts in G,
#     does the rotation lemma certificate exist on A, B or C?
def phase(x, root, n, cyc, coordmap):
    if x in cyc: return coordmap[x]
    return (-d[root][x]) % n
def coords(cyc_tag, length, root):
    # cyclic coordinates along the ring
    cm = {root: 0}
    for j in range(1, length): cm[gi[(cyc_tag, j)]] = j
    return cm
cmA, cmB, cmC = coords('A',25,v0), coords('B',17,v2), coords('C',9,v4)
rings = [(A,25,12,v0,cmA), (B,17,8,v2,cmB), (C,9,4,v4,cmC)]

def certificate(x, y):
    """Is there a ring and an orientation with a valid rotation start q?"""
    for cyc, n, h, root, cm in rings:
        for orient in (1,-1):
            px = (orient*cm[x]) % n if x in cyc else (-d[root][x]) % n
            py = (orient*cm[y]) % n if y in cyc else (-d[root][y]) % n
            for q in range(n):
                if (q-px) % n in range(2,h+1) and (q-py) % n in range(2,h+1):
                    return (n, q)
    return None

missing = [(gn[x],gn[y]) for x in range(len(G)) for y in range(x,len(G))
           if certificate(x,y) is None]
print("pairs of starts in G with NO rotation certificate:", len(missing), missing[:5])
