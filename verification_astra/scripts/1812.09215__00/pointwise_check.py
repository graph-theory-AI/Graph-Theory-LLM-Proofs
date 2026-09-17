"""Independent brute-force test of the writeup's key pointwise bound (11):

  for every x, with y = phi(x) and R_a = { i : phi^{-1}(y)_i != phi^{-1}(y+e_a)_i },
      #{ a : |R_a| <= d }  <=  N_k(d) = 1 + (k-1) + ... + (k-1)^{d-1}   for every d >= 1.

Also tests the more general Claim (6):  |A_d(T)| <= N_k(d-|T|+1) for every nonempty
T of size <= d, where A_d(T) = { a : T subset R_a, |R_a| <= d }.

Run over all Dictator->XOR bijections of Q_n whose output bits are k-juntas,
enumerated exactly as in search_junta_minD.py.
"""
import sys
from itertools import combinations

def candidates(n, k):
    N = 1 << n
    out = set()
    for size in range(0, k + 1):
        for S in combinations(range(n), size):
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

def Nk(k, d):
    return sum((k - 1) ** r for r in range(d)) if d >= 1 else 0

def run(n, k):
    N = 1 << n
    pc = [bin(x).count('1') for x in range(N)]
    cands = candidates(n, k)
    candset = set(cands)
    dict_tt = 0
    for x in range(N):
        if x & 1:
            dict_tt |= 1 << x
    stats = {'maps': 0, 'viol11': 0, 'viol6': 0, 'tight11': 0}

    def analyse(phi_tts):
        phi = [0] * N
        for x in range(N):
            v = 0
            for a, tt in enumerate(phi_tts):
                v |= ((tt >> x) & 1) << a
            phi[x] = v
        inv = [0] * N
        for x in range(N):
            inv[phi[x]] = x
        # actual junta sizes (may be < k)
        kk = 0
        for a in range(n):
            dep = sum(1 for i in range(n)
                      if any(((phi[x] >> a) & 1) != ((phi[x ^ (1 << i)] >> a) & 1) for x in range(N)))
            kk = max(kk, dep)
        stats['maps'] += 1
        for x in range(N):
            y = phi[x]
            R = [x ^ inv[y ^ (1 << a)] for a in range(n)]   # bitmask of R_a
            assert all(r & 1 for r in R), "coordinate 1 not in some R_a"
            assert len(set(R)) == n, "R_a not distinct"
            for d in range(1, n + 1):
                c = sum(1 for r in R if pc[r] <= d)
                if c > Nk(kk, d):
                    stats['viol11'] += 1
                if c == Nk(kk, d):
                    stats['tight11'] += 1
                # full Claim (6)
                for size in range(1, d + 1):
                    for T in combinations(range(n), size):
                        Tm = 0
                        for i in T:
                            Tm |= 1 << i
                        c2 = sum(1 for r in R if (r & Tm) == Tm and pc[r] <= d)
                        if c2 > Nk(kk, d - size + 1):
                            stats['viol6'] += 1

    def dfs(j, groups, chosen, acc):
        if j == n - 1:
            last = acc ^ dict_tt
            if last not in candset:
                return
            for grp in groups:
                a, b = grp
                if ((last >> a) & 1) == ((last >> b) & 1):
                    return
            analyse(chosen + [last])
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
    return stats

for (n, k) in [(3, 3), (4, 2), (4, 3)]:
    s = run(n, k)
    print(f"n={n} k<={k}: maps={s['maps']}, violations of (11) = {s['viol11']}, "
          f"violations of Claim (6) = {s['viol6']}, tight instances of (11) = {s['tight11']}")
    sys.stdout.flush()
