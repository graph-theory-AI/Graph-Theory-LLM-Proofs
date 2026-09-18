"""Exhaustive check for n=3: ALL 8! bijections of Q_3.

Keeps those that are mappings from Dictator to XOR (XOR(phi(x)) = x_1), then for
each computes k = max junta size of the output bits and D = Lip(phi^{-1}).
Checks the writeup's Theorem  n <= N_k(D)  and its pointwise refinement (11).
"""
from itertools import permutations

n = 3
N = 1 << n
pc = [bin(x).count('1') for x in range(N)]

def Nk(k, d):
    return sum((k - 1) ** r for r in range(d)) if d >= 1 else 0

results = {}
cnt = 0
viol_thm = []
viol_ptwise = []
for perm in permutations(range(N)):
    # phi(x) = perm[x]; Dictator -> XOR means parity(perm[x]) == x_1 (bit 0)
    ok = True
    for x in range(N):
        if pc[perm[x]] % 2 != (x & 1):
            ok = False
            break
    if not ok:
        continue
    cnt += 1
    inv = [0] * N
    for x in range(N):
        inv[perm[x]] = x
    # junta sizes
    kk = 0
    for a in range(n):
        dep = sum(1 for i in range(n)
                  if any(((perm[x] >> a) & 1) != ((perm[x ^ (1 << i)] >> a) & 1) for x in range(N)))
        kk = max(kk, dep)
    D = max(pc[inv[y] ^ inv[y ^ (1 << a)]] for y in range(N) for a in range(n))
    results.setdefault(kk, set()).add(D)
    if n > Nk(kk, D):
        viol_thm.append((perm, kk, D))
    # pointwise bound (11): for every x and every d, #{a : |R_a| <= d} <= N_k(d)
    for x in range(N):
        y = perm[x]
        Rsizes = [pc[x ^ inv[y ^ (1 << a)]] for a in range(n)]
        for d in range(1, n + 1):
            c = sum(1 for s in Rsizes if s <= d)
            if c > Nk(kk, d):
                viol_ptwise.append((perm, x, d, c, Nk(kk, d), kk))

print(f"Dictator->XOR bijections of Q_3: {cnt}")
print("k -> set of achievable D:")
for k in sorted(results):
    print(f"  k={k}: D in {sorted(results[k])}   min D = {min(results[k])}"
          f"   formula d_min = {min(d for d in range(1, 20) if Nk(k, d) >= n)}")
print("Theorem n <= N_k(D) violations:", len(viol_thm))
print("Pointwise bound (11) violations:", len(viol_ptwise))
