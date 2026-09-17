"""NON-CIRCULAR check of writeup eq.(1):  P_n = m_n * E_Q[1/Z].

- P_n and m_n = E[Z] are estimated from UNIFORM instances (measure P).
- E_Q[1/Z] is estimated by genuinely sampling from Q: pick M uniform, then sample
  score matrices by REJECTION until M is stable, then enumerate Z. No use of the identity.
Also checks necessity of goodness condition 1 (C cap M(C) = empty).
"""
import itertools, random, sys
from identity_and_moments import all_pm, stable, parr, Ff, cycles

def main(n, trials_P, trials_Q, seed=0):
    rng = random.Random(seed)
    Ms = all_pm(n)
    # ---- measure P
    nsol = totZ = 0
    for _ in range(trials_P):
        U = [[rng.random() for _ in range(n)] for _ in range(n)]
        Z = sum(1 for m in Ms if stable(parr(m, n), U, n))
        totZ += Z
        if Z: nsol += 1
    P_n = nsol/trials_P; m_n = totZ/trials_P
    # ---- measure Q (independent rejection sampling)
    M0 = parr(Ms[0], n)
    tot_inv = 0.0; drops = 0; drop1_fail = 0; drop1_tested = 0; drop2_tested=0; drop2_fail=0
    for _ in range(trials_Q):
        while True:
            U = [[rng.random() for _ in range(n)] for _ in range(n)]
            if stable(M0, U, n): break
            drops += 1
        Z = sum(1 for m in Ms if stable(parr(m, n), U, n))
        tot_inv += 1.0/Z
        # goodness-condition necessity, planted on M0
        x, f, F = Ff(M0, U, n)
        cyc = cycles(F, n)
        if not cyc: continue
        C = [v for c in cyc for v in c]; Cs = set(C)
        cond1 = all(M0[v] not in Cs for v in C)
        cond2 = not any(U[u][v] < U[u][f[u]] and U[v][u] < U[v][f[v]]
                        for u, v in itertools.combinations(C, 2))
        def allsub_ok():
            for r in range(1, len(cyc)+1):
                for sub in itertools.combinations(range(len(cyc)), r):
                    D = [v for i in sub for v in cyc[i]]
                    q = list(M0)
                    for v in D: q[v] = f[v]; q[f[v]] = v
                    if any(q[q[v]] != v or q[v] == v for v in range(n)): return False
                    if not stable(q, U, n): return False
            return True
        if cond2 and not cond1:
            drop1_tested += 1
            if not allsub_ok(): drop1_fail += 1
        if cond1 and not cond2:
            drop2_tested += 1
            if not allsub_ok(): drop2_fail += 1
    EQ = tot_inv/trials_Q
    print(f"n={n}  P-trials={trials_P}  Q-trials={trials_Q}")
    print(f"  P_n (direct)        = {P_n:.5f}")
    print(f"  m_n = E[Z]          = {m_n:.5f}   [(n-1)!! * P(M stable) check: "
          f"{trials_Q/(trials_Q+drops):.5f} * {len(Ms)} = {len(Ms)*trials_Q/(trials_Q+drops):.5f}]")
    print(f"  E_Q[1/Z] (sampled)  = {EQ:.5f}")
    print(f"  m_n * E_Q[1/Z]      = {m_n*EQ:.5f}     vs P_n = {P_n:.5f}   "
          f"rel.diff {abs(m_n*EQ-P_n)/P_n:.4f}")
    print(f"  necessity: drop cond.1 -> {drop1_fail}/{drop1_tested} bad ; "
          f"drop cond.2 -> {drop2_fail}/{drop2_tested} bad")

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),
         seed=int(sys.argv[4]) if len(sys.argv) > 4 else 0)
