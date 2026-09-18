"""Exhaustive check of Lemma 1 of attacks_retry/2106.03261__00/output.md over PG(2,q),
q odd, for a nondegenerate symmetric bilinear form B.

Lemma 1: if A0..A4,B0..B4 are 10 PAIRWISE DISTINCT points of PG(2,K), A0 and A1 are
nonisotropic, and every Petersen edge other than a3b3 joins orthogonal points, then
A3 _|_ B3.

We enumerate exhaustively.  The variants let us test which hypotheses are load-bearing:
  require_distinct : impose pairwise distinctness of the ten points
  require_noniso01 : impose B(A0,A0)!=0 and B(A1,A1)!=0
  require_noniso_all : impose nonisotropy of all ten (as in the construction)
"""
import itertools, sys
from collections import defaultdict

def pg_points(q):
    pts = []
    for z in range(q):
        pts.append((0,0,1) if False else None)
    pts = []
    pts += [(1,b,c) for b in range(q) for c in range(q)]
    pts += [(0,1,c) for c in range(q)]
    pts += [(0,0,1)]
    assert len(pts) == q*q+q+1
    return pts

def make(q, form):
    pts = pg_points(q)
    idx = {p:i for i,p in enumerate(pts)}
    N = len(pts)
    M = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            M[i][j] = form[i][j] % q
    def bil(p,r):
        s = 0
        for i in range(3):
            for j in range(3):
                s += M[i][j]*p[i]*r[j]
        return s % q
    orth = [set() for _ in range(N)]
    for i,p in enumerate(pts):
        for j,r in enumerate(pts):
            if bil(p,r) == 0: orth[i].add(j)
    iso = [bil(p,p)==0 for p in pts]
    return pts, idx, bil, orth, iso, N

def check(q, form, require_distinct=True, require_noniso01=True, require_noniso_all=False,
          report=True):
    pts, idx, bil, orth, iso, N = make(q, form)
    allp = set(range(N))
    def cand(v):
        if require_noniso_all: return [i for i in range(N) if not iso[i]]
        return list(range(N))
    base = cand(None)
    nA0 = [i for i in base if (not iso[i]) or not require_noniso01]
    nA1 = nA0
    total = 0; violations = 0; hist = defaultdict(int); examples = []
    for A0 in base:
        if require_noniso01 and iso[A0]: continue
        for A1 in orth[A0]:
            if A1 not in base: continue
            if require_noniso01 and iso[A1]: continue
            if require_distinct and A1 == A0: continue
            for A2 in orth[A1]:
                if A2 not in base: continue
                for A4 in orth[A0]:
                    if A4 not in base: continue
                    if require_distinct and A4 == A2: continue
                    A3s = orth[A2] & orth[A4]
                    for A3 in A3s:
                        if A3 not in base: continue
                        for B0 in orth[A0]:
                            if B0 not in base: continue
                            if require_distinct and B0 == A2: continue
                            B2s = orth[B0] & orth[A2]
                            for B2 in B2s:
                                if B2 not in base: continue
                                for B1 in orth[A1]:
                                    if B1 not in base: continue
                                    if require_distinct and (B1 == A4 or B1 == B0): continue
                                    B4s = orth[B1] & orth[A4]
                                    for B4 in B4s:
                                        if B4 not in base: continue
                                        if bil(pts[B2], pts[B4]) != 0: continue
                                        B3s = orth[B0] & orth[B1]
                                        for B3 in B3s:
                                            if B3 not in base: continue
                                            tup = (A0,A1,A2,A3,A4,B0,B1,B2,B3,B4)
                                            if require_distinct and len(set(tup)) != 10: continue
                                            total += 1
                                            val = bil(pts[A3], pts[B3])
                                            hist[val] += 1
                                            if val != 0:
                                                violations += 1
                                                if len(examples) < 3:
                                                    examples.append([pts[t] for t in tup])
    if report:
        print(f"  q={q} distinct={require_distinct} noniso01={require_noniso01} "
              f"nonisoAll={require_noniso_all}: configs={total} violations={violations} "
              f"hist={dict(sorted(hist.items()))}")
        for e in examples[:2]: print("     violating example:", e)
    return total, violations

if __name__ == '__main__':
    # form used in the writeup: B(X,Y) = X0Y2 + X2Y0 - X1Y1
    F1 = [[0,0,1],[0,-1,0],[1,0,0]]
    # a second, inequivalent-looking nondegenerate form (identity)
    F2 = [[1,0,0],[0,1,0],[0,0,1]]
    for q in [int(a) for a in sys.argv[1:]] or [5,7]:
        print(f"== q={q}, form X0Y2+X2Y0-X1Y1")
        check(q, F1, True, True, False)
        print(f"== q={q}, form identity")
        check(q, F2, True, True, False)
        print(f"== q={q}, form X0Y2+X2Y0-X1Y1, WITHOUT the nonisotropy of A0,A1")
        check(q, F1, True, False, False)
        print(f"== q={q}, form X0Y2+X2Y0-X1Y1, WITHOUT distinctness (noniso01 kept)")
        check(q, F1, False, True, False)
