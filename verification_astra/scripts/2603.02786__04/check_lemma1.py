"""
Exact verification of Lemma 1 of attacks_retry/2603.02786__04/output.md.

Random composition of K: while remaining sum r>0, pick next part uniform on {1..r}.
Tiling of [nK]: blocks of lengths n*d_1,...,n*d_l; a block of length n*d starting
after position b is tiled by A(d,b+t)={b+t,...,b+t+(n-1)d}, t=1..d.
Then with prob 1/2 reflect x -> nK+1-x.
u_{d,a} := P(A(d,a) is a tile of the random tiling).

Checks:
 (5) E C_d(K) = 1/d
 (1) sum_a u_{d,a} = 1 for every d in [K]
 (2) sum_{d,a : x in A(d,a)} u_{d,a} = 1 for every x in [nK]
 (3) u_{d,a} <= 1/d
 (4) for k<K<=2k:  sum_{d<=k, a: x in A(d,a)} u_{d,a} <= 1 - (K-k)/(2K)
 support: a <= nK-(n-1)d
"""
from fractions import Fraction
from itertools import product
import sys

def compositions(K):
    """yield (composition tuple, probability as Fraction)"""
    stack = [((), Fraction(1), K)]
    while stack:
        comp, p, r = stack.pop()
        if r == 0:
            yield comp, p
            continue
        for s in range(1, r+1):
            stack.append((comp+(s,), p*Fraction(1, r), r-s))

def tiles_of(comp, n, K):
    """set of (d,a) tiles produced by the composition (unreflected)"""
    out = []
    b = 0
    for d in comp:
        for t in range(1, d+1):
            out.append((d, b+t))
        b += n*d
    return out

def weights(n, K):
    u = {}
    tot = Fraction(0)
    EC = {d: Fraction(0) for d in range(1, K+1)}
    for comp, p in compositions(K):
        tot += p
        for d in comp:
            EC[d] += p
        T = tiles_of(comp, n, K)
        for (d, a) in T:
            # unreflected, prob p/2
            u[(d, a)] = u.get((d, a), Fraction(0)) + p/2
            # reflected: A(d,a) -> {nK+1-(a+(n-1)d), ..., nK+1-a}, start a' = nK+1-a-(n-1)d
            a2 = n*K + 1 - a - (n-1)*d
            u[(d, a2)] = u.get((d, a2), Fraction(0)) + p/2
    assert tot == 1, tot
    return u, EC

def check(n, K, verbose=False):
    u, EC = weights(n, K)
    msgs = []
    # (5)
    for d in range(1, K+1):
        if EC[d] != Fraction(1, d):
            msgs.append(f"(5) FAIL n={n} K={K} d={d}: E C_d={EC[d]} != 1/{d}")
    # support
    for (d, a) in u:
        if not (1 <= a <= n*K-(n-1)*d):
            msgs.append(f"support FAIL n={n} K={K} (d,a)=({d},{a}) L_d={n*K-(n-1)*d}")
    # (1)
    for d in range(1, K+1):
        s = sum(v for (dd, a), v in u.items() if dd == d)
        if s != 1:
            msgs.append(f"(1) FAIL n={n} K={K} d={d}: sum={s}")
    # (3)
    for (d, a), v in u.items():
        if v > Fraction(1, d):
            msgs.append(f"(3) FAIL n={n} K={K} (d,a)=({d},{a}): u={v} > 1/{d}")
    # (2) and (4)
    load = {x: Fraction(0) for x in range(1, n*K+1)}
    for (d, a), v in u.items():
        for j in range(n):
            load[a+j*d] += v
    for x in range(1, n*K+1):
        if load[x] != 1:
            msgs.append(f"(2) FAIL n={n} K={K} x={x}: load={load[x]}")
    for k in range((K+1)//2, K):      # k < K <= 2k
        if not (k < K <= 2*k):
            continue
        bound = 1 - Fraction(K-k, 2*K)
        worst = Fraction(0)
        for x in range(1, n*K+1):
            s = Fraction(0)
            for (d, a), v in u.items():
                if d <= k and a <= x <= a+(n-1)*d and (x-a) % d == 0:
                    s += v
            worst = max(worst, s)
            if s > bound:
                msgs.append(f"(4) FAIL n={n} K={K} k={k} x={x}: {s} > {bound}")
        if verbose:
            print(f"   n={n} K={K} k={k}: max small-diff load = {float(worst):.6f}  bound {float(bound):.6f}")
    return msgs

if __name__ == "__main__":
    allmsgs = []
    for n in [2, 3, 4, 5]:
        for K in range(1, 11):
            m = check(n, K, verbose=(n == 3 and K in (6, 9, 10)))
            if m:
                allmsgs += m
            print(f"n={n} K={K}: {'OK' if not m else 'FAILURES'}")
    print()
    if allmsgs:
        print("FAILURES:")
        for m in allmsgs[:40]:
            print(" ", m)
    else:
        print("ALL CHECKS PASSED (properties 1,2,3,4,5 and support of Lemma 1).")
