"""Brute-force check for small even n:
   - P_n = P(a stable matching exists), E[Z] (should -> sqrt(e) = 1.6487)
   - validity of the writeup's Exchange Lemma:
       given a stable matching M, A(v)={w != v,M(v): w prefers v to M(w)},
       f(v)=argmin_{w in A(v)} U_{vw}, F(v)=M(f(v)).
       For every collection C of cycles of F of length >=2 that is "good"
       (C cap M(C) = empty; no u,v in C with U_uv < U_{u,f(u)} and U_vu < U_{v,f(v)}),
       every sub-collection yields a stable matching, hence Z >= 2^c.
"""
import itertools, random, sys
import numpy as np

def all_perfect_matchings(n):
    verts = list(range(n))
    def rec(rem):
        if not rem:
            yield ()
            return
        a = rem[0]
        for i in range(1, len(rem)):
            b = rem[i]
            rest = rem[1:i] + rem[i+1:]
            for m in rec(rest):
                yield ((a, b),) + m
    return list(rec(tuple(verts)))

def is_stable(M_partner, U, n):
    for v in range(n):
        for w in range(n):
            if w == v or w == M_partner[v]:
                continue
            if U[v][w] < U[v][M_partner[v]] and U[w][v] < U[w][M_partner[w]]:
                return False
    return True

def partner_array(m, n):
    p = [0]*n
    for a, b in m:
        p[a] = b; p[b] = a
    return p

def build_F(M_partner, U, n):
    x = [U[v][M_partner[v]] for v in range(n)]
    f = [None]*n
    for v in range(n):
        best, bu = None, 2.0
        for w in range(n):
            if w == v or w == M_partner[v]:
                continue
            if U[w][v] < x[w]:          # w prefers v to M(w)
                if U[v][w] < bu:
                    bu, best = U[v][w], w
        f[v] = best
    F = [None if f[v] is None else M_partner[f[v]] for v in range(n)]
    return x, f, F

def cycles_of(F, n):
    # directed cycles of the partial map F, length >= 2
    colour = [0]*n   # 0 unvisited, 1 in progress, 2 done
    cyc = []
    for s in range(n):
        if colour[s]: continue
        path, pos = [], {}
        v = s
        while v is not None and colour[v] == 0:
            colour[v] = 1; pos[v] = len(path); path.append(v)
            v = F[v]
        if v is not None and colour[v] == 1 and v in pos:
            c = path[pos[v]:]
            if len(c) >= 2:
                cyc.append(c)
        for u in path: colour[u] = 2
    return cyc

def main(n, trials, seed=0):
    rng = random.Random(seed)
    matchings = all_perfect_matchings(n)
    nsol = 0; tot_Z = 0
    exchange_tests = 0; exchange_fail = 0; zbound_fail = 0
    for t in range(trials):
        U = [[rng.random() for _ in range(n)] for _ in range(n)]
        stab = []
        for m in matchings:
            p = partner_array(m, n)
            if is_stable(p, U, n):
                stab.append(p)
        Z = len(stab)
        tot_Z += Z
        if Z: nsol += 1
        for p in stab:
            x, f, F = build_F(p, U, n)
            cyc = cycles_of(F, n)
            if not cyc: continue
            C = [v for c in cyc for v in c]
            good = all(p[v] not in C for v in C)
            if good:
                for u, v in itertools.combinations(C, 2):
                    if U[u][v] < U[u][f[u]] and U[v][u] < U[v][f[v]]:
                        good = False; break
            if not good: continue
            exchange_tests += 1
            # every sub-collection must be stable
            ok = True
            for rsize in range(1, len(cyc)+1):
                for sub in itertools.combinations(range(len(cyc)), rsize):
                    D = [v for i in sub for v in cyc[i]]
                    q = list(p)
                    for v in D:
                        q[v] = f[v]; q[f[v]] = v
                    # sanity: q is a perfect matching
                    assert all(q[q[v]] == v and q[v] != v for v in range(n))
                    if not is_stable(q, U, n):
                        ok = False
            if not ok:
                exchange_fail += 1
            if Z < 2**len(cyc):
                zbound_fail += 1
    print(f"n={n} trials={trials}: P_n={nsol/trials:.4f}  E[Z]={tot_Z/trials:.4f}")
    print(f"   exchange-lemma instances tested (good collections): {exchange_tests}")
    print(f"   sub-collections that were NOT stable: {exchange_fail}")
    print(f"   instances where Z < 2^c : {zbound_fail}")

if __name__ == "__main__":
    n = int(sys.argv[1]); trials = int(sys.argv[2])
    main(n, trials, seed=int(sys.argv[3]) if len(sys.argv) > 3 else 0)
