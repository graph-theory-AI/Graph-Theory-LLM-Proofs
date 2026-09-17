"""End-to-end check of the construction in attacks_retry/2603.02786__01/output.md.

For a given n and block size k:
  - greedily partition primes <= n into k-term APs with common difference divisible by
    Q = lcm(1..k-1) (Lemma 3's greedy), leftovers as singletons;
  - pack each block by Lemma 2 and each singleton alone, in consecutive intervals;
  - verify global pairwise disjointness by brute force;
  - compare the total length to S(n) = sum_{p<=n} p(n-p) and to the claimed
    upper bound S(n) + (t+u) n^2 + 2 Q k n t.
"""
from math import gcd, lcm
from sympy import primerange
import itertools

def block_pack(ds, n, Q):
    a = ds[0]; k = len(ds)
    nstar = n + ((a - n) % Q)
    b = [0]*k
    for i in range(k-1):
        b[i+1] = b[i] + ds[i]*(nstar - ds[i+1]) + Q*ds[i+1]
    return b

def greedy_blocks(primes, k, Q):
    pset = set(primes); used = set(); blocks = []
    ps = sorted(primes)
    changed = True
    while changed:
        changed = False
        for a in ps:
            if a in used: continue
            h = Q
            while a + (k-1)*h <= ps[-1]:
                blk = [a + i*h for i in range(k)]
                if all(x in pset and x not in used for x in blk):
                    blocks.append(blk); used.update(blk); changed = True
                    break
                h += Q
            if changed: break
    leftovers = [p for p in ps if p not in used]
    return blocks, leftovers

def run(n, k):
    Q = lcm(*range(1, k))
    primes = list(primerange(2, n+1))
    blocks, singles = greedy_blocks(primes, k, Q)
    placed = []          # (difference, list of points)
    offset = 0
    for blk in blocks:
        b = block_pack(blk, n, Q)
        pts = [[b[i] + offset + j*blk[i] for j in range(n)] for i in range(k)]
        lo = min(min(x) for x in pts); hi = max(max(x) for x in pts)
        assert lo == offset
        placed.extend(zip(blk, pts))
        offset = hi + 1
    for p in singles:
        pts = [offset + j*p for j in range(n)]
        placed.append((p, pts))
        offset = pts[-1] + 1
    total_len = offset
    # brute-force global disjointness
    seen = {}
    for d, pts in placed:
        for x in pts:
            if x in seen:
                return dict(status="COLLISION", n=n, k=k, at=x, d1=seen[x], d2=d)
            seen[x] = d
    assert len(seen) == n*len(primes)
    S = sum(p*(n-p) for p in primes)
    t, u = len(blocks), len(singles)
    claimed = S + (t+u)*n*n + 2*Q*k*n*t
    return dict(status="OK", n=n, k=k, Q=Q, nblocks=t, nsingles=u, npi=len(primes),
                total_len=total_len, S=S, ratio_len_over_S=round(total_len/S, 4),
                claimed_bound=claimed, bound_holds=total_len <= claimed)

for (n, k) in [(60,3),(100,3),(200,3),(400,3),(1000,3),(2000,3),(200,4),(1000,4),(2000,4),(5000,4),(5000,3)]:
    print(run(n, k))
