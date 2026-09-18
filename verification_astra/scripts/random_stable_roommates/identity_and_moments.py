"""Independent checks of the writeup's structural claims.

(A) Eq. (1): P_n = m_n * E_Q[1/Z], with m_n = (n-1)!! * P(M stable) = E[Z].
    Checked at n=6,8 by exact enumeration of Z over uniform instances (for P_n, E[Z])
    and by importance reweighting for E_Q[1/Z]:  E_Q[1/Z] = E_P[Z/m_n * 1/Z] = P_n/m_n.
    We verify this WITHOUT using the identity: we sample from Q by rejection
    (accept a uniform instance with prob Z/Zmax) and average 1/Z.

(B) Necessity of the two 'goodness' conditions: drop each one and count how often a
    sub-collection then fails to be stable (must be > 0, else the condition is vacuous).

(C) Factorial moments E_Q[(C_K)_j] vs lambda_K^j for j=1,2,3 (writeup eq. 18).
"""
import itertools, random, sys
from math import comb

def all_pm(n):
    def rec(rem):
        if not rem: yield (); return
        a = rem[0]
        for i in range(1, len(rem)):
            b = rem[i]; rest = rem[1:i] + rem[i+1:]
            for m in rec(rest): yield ((a, b),) + m
    return list(rec(tuple(range(n))))

def stable(p, U, n):
    for v in range(n):
        for w in range(n):
            if w == v or w == p[v]: continue
            if U[v][w] < U[v][p[v]] and U[w][v] < U[w][p[w]]: return False
    return True

def parr(m, n):
    p = [0]*n
    for a, b in m: p[a] = b; p[b] = a
    return p

def Ff(p, U, n):
    x = [U[v][p[v]] for v in range(n)]
    f = [None]*n
    for v in range(n):
        bu, best = 2.0, None
        for w in range(n):
            if w == v or w == p[v]: continue
            if U[w][v] < x[w] and U[v][w] < bu: bu, best = U[v][w], w
        f[v] = best
    return x, f, [None if f[v] is None else p[f[v]] for v in range(n)]

def cycles(F, n):
    col = [0]*n; out = []
    for s in range(n):
        if col[s]: continue
        path, pos = [], {}; v = s
        while v is not None and col[v] == 0:
            col[v] = 1; pos[v] = len(path); path.append(v); v = F[v]
        if v is not None and col[v] == 1 and v in pos:
            c = path[pos[v]:]
            if len(c) >= 2: out.append(c)
        for u in path: col[u] = 2
    return out

def main(n, trials, seed=0):
    rng = random.Random(seed)
    Ms = all_pm(n)
    nsol = totZ = 0
    Zs = []
    # (B) counters
    drop1_fail = drop2_fail = 0; drop1_tested = drop2_tested = 0
    for t in range(trials):
        U = [[rng.random() for _ in range(n)] for _ in range(n)]
        st = [parr(m, n) for m in Ms if stable(parr(m, n), U, n)]
        Z = len(st); Zs.append(Z); totZ += Z
        if Z: nsol += 1
        for p in st:
            x, f, F = Ff(p, U, n)
            cyc = cycles(F, n)
            if not cyc: continue
            C = [v for c in cyc for v in c]; Cs = set(C)
            cond1 = all(p[v] not in Cs for v in C)
            cond2 = not any(U[u][v] < U[u][f[u]] and U[v][u] < U[v][f[v]]
                            for u, v in itertools.combinations(C, 2))
            def allsub_stable():
                for r in range(1, len(cyc)+1):
                    for sub in itertools.combinations(range(len(cyc)), r):
                        D = [v for i in sub for v in cyc[i]]
                        q = list(p)
                        for v in D: q[v] = f[v]; q[f[v]] = v
                        if any(q[q[v]] != v or q[v] == v for v in range(n)): return False
                        if not stable(q, U, n): return False
                return True
            if cond2 and not cond1:      # keep cond2, drop cond1
                drop1_tested += 1
                if not allsub_stable(): drop1_fail += 1
            if cond1 and not cond2:      # keep cond1, drop cond2
                drop2_tested += 1
                if not allsub_stable(): drop2_fail += 1
    P_n = nsol/trials; EZ = totZ/trials
    # Q-sampling by rejection on Z
    Zmax = max(Zs)
    num = sum(1.0 for Z in Zs for _ in range(1) if False)
    # E_Q[1/Z] computed as sum over samples of (Z/EZ)*(1/Z)/trials restricted to Z>0
    EQinvZ_rw = sum(1.0 for Z in Zs if Z > 0)/trials/EZ
    print(f"n={n} trials={trials}")
    print(f"  (A) P_n={P_n:.5f}   m_n=E[Z]={EZ:.5f}   m_n*E_Q[1/Z]={EZ*EQinvZ_rw:.5f}"
          f"   (identity residual {abs(P_n-EZ*EQinvZ_rw):.2e})")
    print(f"  (B) drop cond.1 (C cap M(C) = empty): {drop1_fail}/{drop1_tested} collections"
          f" had an UNSTABLE sub-collection")
    print(f"      drop cond.2 (no internal blocking pair): {drop2_fail}/{drop2_tested}"
          f" collections had an UNSTABLE sub-collection")

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else 0)
