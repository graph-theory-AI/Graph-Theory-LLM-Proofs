"""Exhaustive enumeration of Dictator->XOR bijections of Q_n whose output bits are
k-juntas, for small (n,k).  Reports the minimum achievable D = Lip(phi^{-1}) and
compares with the writeup's formula  d_min = min{ d : n <= N_k(d) }.

DFS over output coordinates phi_1,...,phi_{n-1} with exact fiber-size pruning
(after j coordinates every fiber of (phi_1..phi_j) must have size 2^{n-j});
phi_n is then forced by the Dictator->XOR condition phi_1+...+phi_n = x_1.
"""
import sys
from itertools import combinations

def candidates(n, k):
    """All truth tables (as 2^n-bit ints) of functions with at most k relevant vars."""
    N = 1 << n
    out = set()
    for size in range(0, k + 1):
        for S in combinations(range(n), size):
            # enumerate all functions of the variables in S
            for tt in range(1 << (1 << size)):
                f = 0
                for x in range(N):
                    idx = 0
                    for b, i in enumerate(S):
                        idx |= ((x >> i) & 1) << b
                    if (tt >> idx) & 1:
                        f |= 1 << x
                out.add(f)
    return sorted(out)

def relevant(n, f):
    N = 1 << n
    return [i for i in range(n)
            if any(((f >> x) & 1) != ((f >> (x ^ (1 << i))) & 1) for x in range(N))]

def Nk(k, d):
    return sum((k - 1) ** r for r in range(d))

def run(n, k, report_every=None):
    N = 1 << n
    pc = [bin(x).count('1') for x in range(N)]
    cands = candidates(n, k)
    dict_tt = 0
    for x in range(N):
        if x & 1:
            dict_tt |= 1 << x
    candset = set(cands)
    best = None
    best_phi = None
    count = 0

    def dfs(j, groups, chosen, acc):
        nonlocal best, best_phi, count
        if j == n - 1:
            last = acc ^ dict_tt
            if last not in candset:
                return
            # final bijectivity: groups have size 2, last must split each
            for grp in groups:
                a, b = grp
                if ((last >> a) & 1) == ((last >> b) & 1):
                    return
            phi_tts = chosen + [last]
            phi = [0] * N
            for x in range(N):
                v = 0
                for a, tt in enumerate(phi_tts):
                    v |= ((tt >> x) & 1) << a
                phi[x] = v
            inv = [0] * N
            for x in range(N):
                inv[phi[x]] = x
            D = max(pc[inv[y] ^ inv[y ^ (1 << a)]] for y in range(N) for a in range(n))
            count += 1
            if best is None or D < best:
                best = D; best_phi = phi_tts
            return
        for tt in cands:
            ng = []
            ok = True
            for grp in groups:
                z = [x for x in grp if not ((tt >> x) & 1)]
                o = [x for x in grp if ((tt >> x) & 1)]
                if len(z) != len(o):
                    ok = False; break
                ng.append(z); ng.append(o)
            if not ok:
                continue
            dfs(j + 1, ng, chosen + [tt], acc ^ tt)

    dfs(0, [list(range(N))], [], 0)
    pred = min(d for d in range(1, 4 * n + 4) if Nk(k, d) >= n)
    return count, best, pred

for (n, k) in [(3, 2), (3, 3), (4, 2), (4, 3), (5, 2), (6, 2), (4, 4)]:
    cnt, best, pred = run(n, k)
    print(f"n={n:2d} k={k}: #maps={cnt:8d}  min D = {best}   formula d_min = {pred}"
          f"   -> {'OK' if best == pred else 'MISMATCH'}")
    sys.stdout.flush()
