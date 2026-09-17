"""Algebraic enumeration of CANONICAL Petersen copies in G_q (writeup 2106.03261__00).

Vertices (x,y) in F_q^2 with 2y != x^2; edge between class u and class v (uv in E(P))
iff y+y' = x x' + c_uv.  Free parameters: A0=(x0,y0), then A1,A2,A4,B0,B1 each pinned by
one neighbour equation; A3,B2,B4,B3 are then forced by two equations each; the remaining
constraints are the b2b4 edge and the a3b3 edge (with the twist constant).

This solves the same system as brute force but in O(m k^4) with early pruning, so it
reaches q where the untwisted control is expected to be non-empty (~q^6/10^10 copies).
"""
import sys
from collections import defaultdict

def run(q, twisted, cls_perm=None, verbose=True):
    assert (q-1) % 10 == 0 and q % 2 == 1
    k = (q-1)//10
    PVo = ['a0','a1','a2','a3','a4','b0','b1','b2','b3','b4']
    order = cls_perm if cls_perm else PVo
    nz = list(range(1,q))
    I = {v: set(nz[i*k:(i+1)*k]) for i,v in enumerate(order)}
    sq = [(x*x) % q for x in range(q)]
    inv = [0]*q
    for a in range(1,q): inv[a] = pow(a, q-2, q)
    def ok(x,y): return (2*y) % q != sq[x]
    c_a3b3 = 1 if twisted else 0
    total = 0; samples = []
    Ia0,Ia1,Ia2,Ia3,Ia4 = I['a0'],I['a1'],I['a2'],I['a3'],I['a4']
    Ib0,Ib1,Ib2,Ib3,Ib4 = I['b0'],I['b1'],I['b2'],I['b3'],I['b4']
    for x0 in Ia0:
        for y0 in range(q):
            if not ok(x0,y0): continue
            for x1 in Ia1:
                y1 = (x0*x1 - y0) % q
                if not ok(x1,y1): continue
                for x2 in Ia2:
                    y2 = (x1*x2 - y1) % q
                    if not ok(x2,y2): continue
                    for x4 in Ia4:
                        y4 = (x0*x4 - y0) % q
                        if not ok(x4,y4): continue
                        # A3 _|_ A2 and A3 _|_ A4  (c=0 on a2a3 and a3a4)
                        x3 = ((y2-y4) * inv[(x2-x4) % q]) % q
                        if x3 not in Ia3: continue
                        y3 = (x2*x3 - y2) % q
                        if not ok(x3,y3): continue
                        for u0 in Ib0:
                            v0 = (x0*u0 - y0) % q
                            if not ok(u0,v0): continue
                            # B2 _|_ B0 and B2 _|_ A2
                            u2 = ((v0-y2) * inv[(u0-x2) % q]) % q
                            if u2 not in Ib2: continue
                            v2 = (u0*u2 - v0) % q
                            if not ok(u2,v2): continue
                            for u1 in Ib1:
                                v1 = (x1*u1 - y1) % q
                                if not ok(u1,v1): continue
                                # B4 _|_ B1 and B4 _|_ A4
                                u4 = ((v1-y4) * inv[(u1-x4) % q]) % q
                                if u4 not in Ib4: continue
                                v4 = (u1*u4 - v1) % q
                                if not ok(u4,v4): continue
                                # B3 _|_ B0 and B3 _|_ B1
                                u3 = ((v0-v1) * inv[(u0-u1) % q]) % q
                                if u3 not in Ib3: continue
                                v3 = (u0*u3 - v0) % q
                                if not ok(u3,v3): continue
                                # remaining edge b2b4 (c=0)
                                if (v2+v4) % q != (u2*u4) % q: continue
                                # remaining edge a3b3 (c = twist)
                                if (y3+v3) % q != (x3*u3 + c_a3b3) % q: continue
                                total += 1
                                if len(samples) < 2:
                                    samples.append(dict(a0=(x0,y0),a1=(x1,y1),a2=(x2,y2),
                                        a3=(x3,y3),a4=(x4,y4),b0=(u0,v0),b1=(u1,v1),
                                        b2=(u2,v2),b3=(u3,v3),b4=(u4,v4)))
    return total, samples

def run14(q, cls_perm=None):
    """Same enumeration but WITHOUT imposing the a3b3 relation: returns
    (#configs satisfying the 14 edges, histogram of B(A3,B3)=y3+v3-x3*u3)."""
    assert (q-1) % 10 == 0 and q % 2 == 1
    k = (q-1)//10
    PVo = ['a0','a1','a2','a3','a4','b0','b1','b2','b3','b4']
    order = cls_perm if cls_perm else PVo
    nz = list(range(1,q))
    I = {v: set(nz[i*k:(i+1)*k]) for i,v in enumerate(order)}
    sq = [(x*x) % q for x in range(q)]
    inv = [0]*q
    for a in range(1,q): inv[a] = pow(a,q-2,q)
    def ok(x,y): return (2*y) % q != sq[x]
    hist = defaultdict(int)
    Ia0,Ia1,Ia2,Ia3,Ia4 = I['a0'],I['a1'],I['a2'],I['a3'],I['a4']
    Ib0,Ib1,Ib2,Ib3,Ib4 = I['b0'],I['b1'],I['b2'],I['b3'],I['b4']
    for x0 in Ia0:
        for y0 in range(q):
            if not ok(x0,y0): continue
            for x1 in Ia1:
                y1 = (x0*x1-y0) % q
                if not ok(x1,y1): continue
                for x2 in Ia2:
                    y2 = (x1*x2-y1) % q
                    if not ok(x2,y2): continue
                    for x4 in Ia4:
                        y4 = (x0*x4-y0) % q
                        if not ok(x4,y4): continue
                        x3 = ((y2-y4)*inv[(x2-x4)%q]) % q
                        if x3 not in Ia3: continue
                        y3 = (x2*x3-y2) % q
                        if not ok(x3,y3): continue
                        for u0 in Ib0:
                            v0 = (x0*u0-y0) % q
                            if not ok(u0,v0): continue
                            u2 = ((v0-y2)*inv[(u0-x2)%q]) % q
                            if u2 not in Ib2: continue
                            v2 = (u0*u2-v0) % q
                            if not ok(u2,v2): continue
                            for u1 in Ib1:
                                v1 = (x1*u1-y1) % q
                                if not ok(u1,v1): continue
                                u4 = ((v1-y4)*inv[(u1-x4)%q]) % q
                                if u4 not in Ib4: continue
                                v4 = (u1*u4-v1) % q
                                if not ok(u4,v4): continue
                                u3 = ((v0-v1)*inv[(u0-u1)%q]) % q
                                if u3 not in Ib3: continue
                                v3 = (u0*u3-v0) % q
                                if not ok(u3,v3): continue
                                if (v2+v4) % q != (u2*u4) % q: continue
                                hist[(y3+v3-x3*u3) % q] += 1
    return hist

if __name__ == '__main__':
    import time
    for q in [int(a) for a in sys.argv[1:]] or [61,101]:
        t=time.time(); hist = run14(q); el=time.time()-t
        tot = sum(hist.values())
        print(f"q={q}: 14-edge canonical configs = {tot}; "
              f"histogram of B(A3,B3) = {dict(sorted(hist.items()))}   [{el:.1f}s]")
        for tw in (False,True):
            t=time.time(); n,s = run(q,tw); el=time.time()-t
            print(f"   twisted={tw}: canonical Petersen copies = {n}  [{el:.1f}s]")
