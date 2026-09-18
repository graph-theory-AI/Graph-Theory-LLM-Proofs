"""Exhaustive check of Lemma 2 of attacks_retry/2603.02786__01/output.md.

Lemma 2: d_i = a + i*h (i=0..k-1) pairwise coprime, increasing, <= n, Q = lcm(1..k-1), Q | h.
Choose n* in [n, n+Q-1] with n* = a (mod Q).  b_0 = 0, b_{i+1} = b_i + d_i(n*-d_{i+1}) + Q d_{i+1}.
Claim: the A_{d_i}(b_i) = {b_i, b_i+d_i, ..., b_i+(n-1)d_i} are pairwise disjoint,
and all fit in an interval of length <= sum_i d_i(n-d_i) + n^2 + 2*Q*k*n.
"""
from math import gcd, lcm
from sympy import primerange, isprime
import itertools, random

def build(ds, n, Q):
    a = ds[0]
    k = len(ds)
    # n*: smallest >= n congruent to a mod Q
    nstar = n + ((a - n) % Q)
    assert n <= nstar <= n + Q - 1 and (nstar - a) % Q == 0
    b = [0]*k
    for i in range(k-1):
        b[i+1] = b[i] + ds[i]*(nstar - ds[i+1]) + Q*ds[i+1]
    return b, nstar

def check(ds, n, verbose=False):
    k = len(ds)
    Q = lcm(*range(1, k)) if k >= 2 else 1
    h = ds[1]-ds[0]
    assert all(ds[i+1]-ds[i] == h for i in range(k-1)), "not an AP"
    assert h % Q == 0, f"Q={Q} does not divide h={h}"
    assert all(gcd(x, y) == 1 for x, y in itertools.combinations(ds, 2)), "not coprime"
    assert ds[-1] <= n
    b, nstar = build(ds, n, Q)
    # pairwise disjointness by explicit set construction
    sets = [set(b[i] + j*ds[i] for j in range(n)) for i in range(k)]
    for i, j in itertools.combinations(range(k), 2):
        inter = sets[i] & sets[j]
        if inter:
            return ("DISJOINT_FAIL", ds, n, i, j, sorted(inter)[:3])
    lo = min(min(s) for s in sets); hi = max(max(s) for s in sets)
    length = hi - lo + 1
    bound = sum(d*(n-d) for d in ds) + n*n + 2*Q*k*n
    if length > bound:
        return ("LENGTH_FAIL", ds, n, length, bound)
    # also check the claimed formula Lambda for the length
    Lam = sum(ds[i]*(nstar-ds[i+1]) + Q*ds[i+1] for i in range(k-1)) + (n-1)*ds[-1] + 1
    if length != Lam:
        return ("LAMBDA_MISMATCH", ds, n, length, Lam)
    # check the A,B decomposition claim of the proof for each pair
    for i, j in itertools.combinations(range(k), 2):
        m = j - i
        p, q = ds[i], ds[j]
        A = sum((m-t)*(nstar-ds[i+t+1])//m + Q*(m-t-1)//m for t in range(m))
        B = sum(t*(nstar-ds[i+t+1])//m + Q*(t+1)//m for t in range(m))
        # integrality
        for t in range(m):
            for num in [(m-t)*(nstar-ds[i+t+1]), Q*(m-t-1), t*(nstar-ds[i+t+1]), Q*(t+1)]:
                if num % m != 0:
                    return ("NONINTEGRAL", ds, n, i, j, t, num, m)
        if b[j]-b[i] != A*p + B*q:
            return ("DECOMP_FAIL", ds, n, i, j, b[j]-b[i], A*p+B*q)
        if A < n - q or B < 1:
            return ("LEMMA1_HYP_FAIL", ds, n, i, j, A, n-q, B)
    return ("OK", ds, n, length, bound, Lam)

# ---- find prime APs with difference divisible by Q = lcm(1..k-1) ----
def prime_aps(k, nmax):
    Q = lcm(*range(1, k)) if k >= 2 else 1
    ps = list(primerange(2, nmax+1))
    pset = set(ps)
    out = []
    for a in ps:
        h = Q
        while a + (k-1)*h <= nmax:
            ds = [a + i*h for i in range(k)]
            if all(d in pset for d in ds):
                out.append(ds)
            h += Q
    return out

results = {"OK":0}
fails = []
for k in [3, 4, 5, 6]:
    aps = prime_aps(k, 400)
    random.seed(0)
    random.shuffle(aps)
    for ds in aps[:40]:
        for n in [ds[-1], ds[-1]+1, ds[-1]+7, 400, 401, 500]:
            if n < ds[-1]:
                continue
            r = check(ds, n)
            results[r[0]] = results.get(r[0], 0) + 1
            if r[0] != "OK":
                fails.append(r)
print("k-AP blocks tested; outcome counts:", results)
print("failures:", fails[:5])
