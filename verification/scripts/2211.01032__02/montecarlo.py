"""Monte Carlo checks for 2211.01032__02.

1. E[F(K_n)] growth vs writeup's upper claim (2+o(1)) ln n and lower
   (1/2) ln n - O(1); Mauk-Stahl conjecture says 2 ln n + O(1).
2. E[F(G(n,1/2))] vs writeup bound ~ (N/delta^2) H_N ~= 4 ln n.
3. Lemma 3.1 at n=60 (K_60), theta=0.3: Pr(L(a)=ell & light) <= 1/((1-th)^2 d^2)
   estimated by tracing the face of a fixed dart with on-demand full random
   rotations (unbiased; does NOT use the exposure lemma).
"""
import random, math
from collections import defaultdict

random.seed(12345)

def sample_F_complete(n):
    """One sample of F(K_n)."""
    # rho[v] = successor map on darts (v,w); represent dart (v,w) as w for rho_v
    succ = []
    for v in range(n):
        nbrs = [w for w in range(n) if w != v]
        random.shuffle(nbrs)
        s = {}
        for i, w in enumerate(nbrs):
            s[w] = nbrs[(i + 1) % len(nbrs)]
        succ.append(s)
    seen = set()
    F = 0
    for u in range(n):
        for v in range(n):
            if u == v or (u, v) in seen:
                continue
            F += 1
            x = (u, v)
            while x not in seen:
                seen.add(x)
                a, b = x
                x = (b, succ[b][a])
    return F

def sample_F_graph(adj):
    n = len(adj)
    succ = []
    for v in range(n):
        nbrs = list(adj[v])
        random.shuffle(nbrs)
        s = {}
        if nbrs:
            for i, w in enumerate(nbrs):
                s[w] = nbrs[(i + 1) % len(nbrs)]
        succ.append(s)
    seen = set()
    F = 0
    for u in range(n):
        for v in adj[u]:
            if (u, v) in seen:
                continue
            F += 1
            x = (u, v)
            while x not in seen:
                seen.add(x)
                a, b = x
                x = (b, succ[b][a])
    return F

print("--- E[F(K_n)] vs (2 +- o(1)) ln n ---")
for n, reps in [(50, 400), (100, 300), (200, 200), (400, 100), (800, 40)]:
    vals = [sample_F_complete(n) for _ in range(reps)]
    m = sum(vals) / reps
    sd = (sum((v - m) ** 2 for v in vals) / (reps - 1)) ** 0.5
    print(f"K_{n}: E[F] ~= {m:.3f} +- {sd/reps**0.5:.3f};  2 ln n = "
          f"{2*math.log(n):.3f};  0.5 ln n = {0.5*math.log(n):.3f}")

print("--- E[F(G(n,1/2))] ---")
for n, reps in [(100, 200), (200, 100), (400, 50)]:
    tot = 0.0
    for _ in range(reps):
        adj = [[] for _ in range(n)]
        for u in range(n):
            for v in range(u + 1, n):
                if random.random() < 0.5:
                    adj[u].append(v)
                    adj[v].append(u)
        tot += sample_F_graph(adj)
    N = None
    print(f"G({n},0.5): E[F] ~= {tot/reps:.3f};  4 ln n = {4*math.log(n):.3f}; "
          f"2 ln n = {2*math.log(n):.3f}")

print("--- Lemma 3.1 on K_60, theta=0.3, dart a=(0,1), lengths <= 12 ---")
n, theta, trials, CAP = 60, 0.3, 500_000, 12
d = n - 1
bound = 1.0 / ((1 - theta) ** 2 * d ** 2)
counts = defaultdict(int)
base = list(range(n))
for _ in range(trials):
    succ = {}   # vertex -> successor map, built on demand from a full shuffle
    a = (0, 1)
    x = a
    trans = defaultdict(int)  # r_C(v) counts
    L = 0
    closed = False
    while L < CAP:
        u, v = x
        s = succ.get(v)
        if s is None:
            
            nbrs = [w for w in base if w != v]
            random.shuffle(nbrs)
            s = {}
            for i in range(d):
                s[nbrs[i]] = nbrs[(i + 1) % d]
            succ[v] = s
        x = (v, s[u])
        trans[x[0]] += 1
        L += 1
        if x == a:
            closed = True
            break
    if closed:
        light = all(c <= theta * d for c in trans.values())
        if light:
            counts[L] += 1
print(f"bound per ell: {bound:.3e}  ({trials} trials => bound*trials = "
      f"{bound*trials:.1f})")
for ell in sorted(counts):
    p = counts[ell] / trials
    err = (counts[ell] ** 0.5) / trials
    print(f"  ell={ell}: Pr(L=ell & light) ~= {p:.3e} +- {err:.1e} "
          f"({counts[ell]} hits)  {'OK' if p <= bound + 3*err else 'VIOLATION?'}")
