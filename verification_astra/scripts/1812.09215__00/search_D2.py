"""Exhaustive search over ALL Dictator->XOR bijections of Q_n with Lip(phi^{-1}) <= 2.

Parametrisation.  psi = phi^{-1} satisfies psi(y)_1 = XOR(y), so psi(y) = (XOR(y), g(y))
with g : Q_n -> F_2^{n-1}.  psi is a bijection iff g is injective on each parity class.
An edge y ~ y+e_a always flips the first coordinate of psi, so
    Lip(psi) <= 2   <=>   dist(g(y), g(y+e_a)) <= 1 for every cube edge.
We may normalise g(0) = 0 (translating g translates the x-side by a constant, which
changes neither the junta sizes of phi nor the Dictator->XOR property).

For every solution we compute the junta sizes of phi = psi^{-1} and report the minimum
over all solutions of  max_a |{i : phi_a depends on x_i}|.
The writeup's theorem says  n <= N_k(2) = k, i.e. that minimum must be exactly n.
"""
import sys
from itertools import product

def run(n, verbose=False):
    N = 1 << n
    m = n - 1
    M = 1 << m
    pc = [bin(x).count('1') for x in range(max(N, M))]
    nbrs = [[y ^ (1 << a) for a in range(n)] for y in range(N)]
    # BFS order from 0 so every new vertex has an already-assigned neighbour
    order, seen = [0], {0}
    qi = 0
    while qi < len(order):
        y = order[qi]; qi += 1
        for z in nbrs[y]:
            if z not in seen:
                seen.add(z); order.append(z)
    # candidate values at Hamming distance <= 1 from a given value
    close = [[v] + [v ^ (1 << j) for j in range(m)] for v in range(M)]

    g = [-1] * N
    used = [set(), set()]          # used g-values per parity class
    sols = []

    def dfs(idx):
        if idx == len(order):
            sols.append(tuple(g))
            return
        y = order[idx]
        par = pc[y] & 1
        assigned = [g[z] for z in nbrs[y] if g[z] >= 0]
        cand = set(close[assigned[0]]) if assigned else set(range(M))
        for v in assigned[1:]:
            cand &= set(close[v])
            if not cand:
                return
        for val in sorted(cand):
            if val in used[par]:
                continue
            g[y] = val; used[par].add(val)
            dfs(idx + 1)
            g[y] = -1; used[par].discard(val)

    # normalisation g(0) = 0
    g[0] = 0; used[0].add(0)
    dfs(1)

    best = None
    best_ex = None
    for sol in sols:
        psi = [ (pc[y] & 1) | (sol[y] << 1) for y in range(N) ]
        phi = [0] * N
        for y in range(N):
            phi[psi[y]] = y
        kk = 0
        for a in range(n):
            dep = sum(1 for i in range(n)
                      if any(((phi[x] >> a) & 1) != ((phi[x ^ (1 << i)] >> a) & 1) for x in range(N)))
            kk = max(kk, dep)
        if best is None or kk < best:
            best = kk; best_ex = psi
    return len(sols), best

for n in range(2, 7):
    cnt, best = run(n)
    print(f"n={n}: #(Dictator->XOR bijections with Lip(phi^-1)<=2, normalised) = {cnt};"
          f"  min over them of max junta size = {best};  writeup predicts {n}"
          f"   -> {'OK' if best == n else 'MISMATCH'}")
    sys.stdout.flush()
