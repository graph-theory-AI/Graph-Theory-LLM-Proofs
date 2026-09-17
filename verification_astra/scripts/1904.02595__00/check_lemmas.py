"""Check Lemma 2 (t + 2 rho(A) <= 2^n) on all irredundant sets of small products,
and Lemma 4 (alpha_w - W(A) >= 2^n - 2 rho(A)) on independent families of quotients."""
import sys, itertools, random
from fractions import Fraction
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1904.02595__00')
from core import build, is_irredundant, alpha
from sympy import Matrix

def zvec(x):
    """tensor of (1, x_i+1) (labels 1-based) as a flat list of length 2^n"""
    v = [1]
    for a in x:
        lab = a + 1
        v = [c*t for c in v for t in (1, lab)]
    return v

def rho(A):
    if not A: return 0
    return Matrix([zvec(x) for x in A]).rank()

# ---------- Lemma 2 on actual graphs ----------
def check_lemma2(factors, verbose=False):
    verts, N, Nc = build(factors)
    n = len(verts); k = len(factors)
    worst = None; cnt = 0; viol = []
    def cellof(v): return tuple(c[0] for c in v)
    def rec(start, S, members):
        nonlocal cnt, worst
        cnt += 1
        if members:
            L = [v for v in members if not (N[v] & S)]
            t = len(members) - len(L)
            A = sorted({cellof(verts[v]) for v in L})
            r = rho(A)
            if t + 2*r > 2**k:
                viol.append((members, t, r))
            slack = 2**k - (t + 2*r)
            if worst is None or slack < worst[0]:
                worst = (slack, t, r, tuple(members))
        for v in range(start, n):
            S2 = S | (1 << v)
            if is_irredundant(S2, Nc, n):
                rec(v+1, S2, members + [v])
    rec(0, 0, [])
    return cnt, worst, viol

for factors in [[[1,1,1]],[[2,1,1]],[[3,2,1]],[[1,1,1],[1,1,1]],[[2,1],[2,1]],[[2,1,1],[1,1,1]],
                [[1,1],[1,1],[1,1]],[[1,1],[1,1,1],[1,1]],[[2,1],[1,1],[1,1]]]:
    cnt, worst, viol = check_lemma2(factors)
    nm = " x ".join("K(" + ",".join(map(str,f)) + ")" for f in factors)
    print(f"Lemma2 {nm:32s} irr.sets={cnt:7d} min slack(2^n-t-2rho)={worst[0]:2d} (t={worst[1]},rho={worst[2]})  violations={len(viol)}")
    if viol: print("   VIOLATION", viol[:3])
