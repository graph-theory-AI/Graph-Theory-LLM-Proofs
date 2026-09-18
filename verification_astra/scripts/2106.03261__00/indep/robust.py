"""Robustness of the canonical-copy counts to the choice of the partition
F_q^* = I_{a0} u ... u I_{b4}.  The writeup only says "partition into ten sets of equal
size", so the conclusion must not depend on which partition.  We use random partitions.
Also records the histogram of B(A3,B3) over the 14-edge configurations, which must be
concentrated on 0 (Lemma 1).
"""
import random, sys
from collections import defaultdict

def run(q, seed, twisted):
    k = (q-1)//10
    PVo = ['a0','a1','a2','a3','a4','b0','b1','b2','b3','b4']
    nz = list(range(1,q)); random.Random(seed).shuffle(nz)
    I = {v: set(nz[i*k:(i+1)*k]) for i,v in enumerate(PVo)}
    sq = [(x*x) % q for x in range(q)]
    inv = [0]*q
    for a in range(1,q): inv[a] = pow(a,q-2,q)
    ok = lambda x,y: (2*y) % q != sq[x]
    cc = 1 if twisted else 0
    Ia0,Ia1,Ia2,Ia3,Ia4 = I['a0'],I['a1'],I['a2'],I['a3'],I['a4']
    Ib0,Ib1,Ib2,Ib3,Ib4 = I['b0'],I['b1'],I['b2'],I['b3'],I['b4']
    tot = 0; hist = defaultdict(int)
    for x0 in Ia0:
        for y0 in range(q):
            if not ok(x0,y0): continue
            for x1 in Ia1:
                y1=(x0*x1-y0)%q
                if not ok(x1,y1): continue
                for x2 in Ia2:
                    y2=(x1*x2-y1)%q
                    if not ok(x2,y2): continue
                    for x4 in Ia4:
                        y4=(x0*x4-y0)%q
                        if not ok(x4,y4): continue
                        x3=((y2-y4)*inv[(x2-x4)%q])%q
                        if x3 not in Ia3: continue
                        y3=(x2*x3-y2)%q
                        if not ok(x3,y3): continue
                        for u0 in Ib0:
                            v0=(x0*u0-y0)%q
                            if not ok(u0,v0): continue
                            u2=((v0-y2)*inv[(u0-x2)%q])%q
                            if u2 not in Ib2: continue
                            v2=(u0*u2-v0)%q
                            if not ok(u2,v2): continue
                            for u1 in Ib1:
                                v1=(x1*u1-y1)%q
                                if not ok(u1,v1): continue
                                u4=((v1-y4)*inv[(u1-x4)%q])%q
                                if u4 not in Ib4: continue
                                v4=(u1*u4-v1)%q
                                if not ok(u4,v4): continue
                                u3=((v0-v1)*inv[(u0-u1)%q])%q
                                if u3 not in Ib3: continue
                                v3=(u0*u3-v0)%q
                                if not ok(u3,v3): continue
                                if (v2+v4)%q != (u2*u4)%q: continue
                                hist[(y3+v3-x3*u3)%q]+=1
                                if (y3+v3)%q == (x3*u3+cc)%q: tot+=1
    return tot, hist

if __name__ == '__main__':
    q = int(sys.argv[1]); seeds = [int(a) for a in sys.argv[2:]] or list(range(6))
    for sd in seeds:
        t1,h = run(q, sd, True)
        t0,_ = run(q, sd, False)
        nz = sum(v for kk,v in h.items() if kk != 0)
        print(f"q={q} seed={sd}: 14-edge configs={sum(h.values())}, "
              f"#with B(A3,B3)!=0 = {nz}; canonical copies twisted={t1} untwisted={t0}")
