"""Independent check of the MECHANICS of the writeup's Lemma 1 proof.

For explicit sequences t_0<t_1<... and explicit label words gamma_k we build
U_i = union of J_k=[t_k, lambda t_{k+1}] over gamma_k=i, find the connected components,
and verify, numerically and exactly:

 (S) every component of U_i is exactly [t_f, lambda t_{l+1}] with f,l its extreme indices;
 (A) the recurrence (6):   d_C = a_C + d_{C^-}/R_C ;
 (B) the telescoping bound (11):  sum_C log R_C <= r log t_{N+1} + O(1)  [O(1) independent of N];
 (C) the covering estimate (12):   sum_C log Q_C >= log t_{N+1} - O(1)   [O(1) independent of N];
 (D) the identity behind (8):  log(d_{C^-}/d_C) = log R_C + log(1 - a_C/d_C).

A failure of (B) or (C) with a drift growing in N would break the proof of Lemma 1.
"""
import math
import numpy as np

RNG = np.random.default_rng(31415)
LAM = 2.0


def components(tk, gamma, i, lam=LAM):
    """connected components of U_i; returns list of (f, l)."""
    idx = [k for k in range(len(tk) - 1) if gamma[k] == i]
    comps = []
    for k in idx:
        if comps and tk[k] <= lam * tk[comps[-1][1] + 1] + 1e-12:
            comps[-1] = (comps[-1][0], max(comps[-1][1], k))
        else:
            comps.append((k, k))
    return comps


def check(tk, gamma, r, lam=LAM, tag=""):
    K = len(tk) - 1
    allc = []
    bad = []
    for i in range(r):
        comps = components(tk, gamma, i, lam)
        # (S) structure: the component must be the full interval [t_f, lam t_{l+1}]
        for (f, l) in comps:
            lo, hi = tk[f], lam * tk[l + 1]
            # every J_k with f<=k<=l, gamma_k=i must lie inside, and coverage connected
            segs = sorted((tk[k], lam * tk[k + 1]) for k in range(f, l + 1) if gamma[k] == i)
            cur = segs[0][1]
            for (a, b) in segs[1:]:
                if a > cur + 1e-12:
                    bad.append(("S-disconnected", i, f, l))
                cur = max(cur, b)
            if abs(segs[0][0] - lo) > 1e-9 or abs(cur - hi) > 1e-9:
                bad.append(("S-endpoints", i, f, l))
        # measures, d_C, a_C, Q_C, R_C
        meas = 0.0
        prevE = None
        prevd = None
        for (f, l) in comps:
            e = lam * tk[l + 1]
            meas += e - tk[f]
            d = meas / e
            a = 1 - 1.0 / (lam * (tk[l + 1] / tk[f]))
            Q = tk[l + 1] / tk[f]
            if prevE is not None:
                R = e / prevE
                if abs(d - (a + prevd / R)) > 1e-9 * max(1, d):        # (A)
                    bad.append(("A-recurrence", i, f, l, d, a + prevd / R))
                lhs = math.log(prevd / d)
                rhs = math.log(R) + math.log(1 - a / d)
                if abs(lhs - rhs) > 1e-9:                               # (D)
                    bad.append(("D-identity", i, f, l, lhs, rhs))
                allc.append(dict(i=i, f=f, l=l, Q=Q, R=R, d=d, a=a))
            prevE, prevd = e, d
    sumlogR = sum(math.log(c["R"]) for c in allc)
    sumlogQ = sum(math.log(c["Q"]) for c in allc)
    B = sumlogR - r * math.log(tk[K])          # (B): should stay bounded above
    C = sumlogQ - math.log(tk[K])              # (C): should stay bounded below
    return B, C, bad, len(allc)


def report(name, make_tk, make_gamma, r, Ks):
    print(f"\n--- {name} (r={r}) ---")
    print(f"{'K':>7} {'#comps':>7} {'(B) sum logR - r log t_K':>26} "
          f"{'(C) sum logQ - log t_K':>24} {'structure failures':>19}")
    for K in Ks:
        tk = make_tk(K)
        gamma = make_gamma(K)
        B, C, bad, nc = check(tk, gamma, r)
        print(f"{K:>7} {nc:>7} {B:>26.6f} {C:>24.6f} {len(bad):>19}")
        if bad:
            print("    first failures:", bad[:3])


if __name__ == "__main__":
    b3 = 2.2618022452602
    # 1. the extremal cyclic configuration, r=3: t_k geometric with ratio b3^(1/M)
    M = 12
    for r, b in [(3, 2.2618022452602), (4, 1.8549627501624)]:
        report(f"extremal cyclic, ratio b_0={b:.6f} split into {M} blocks",
               lambda K, b=b: np.array([b ** (j / M) for j in range(K + 1)]),
               lambda K, r=r: np.array([(j // M) % r for j in range(K)]),
               r, [120, 240, 480, 960])

    # 2. arithmetic t_k (the case actually used in Section 4: t_k ~ k log 2) with a
    #    NON-cyclic random colour word on geometrically growing runs
    for r in [3, 4]:
        def mk_t(K):
            return np.arange(1, K + 2, dtype=float)

        def mk_g(K, r=r):
            g = np.empty(K, dtype=int)
            k = 0
            pos = 1.0
            prev = -1
            while k < K:
                pos *= RNG.uniform(1.5, 4.0)
                nxt = min(K, int(pos))
                c = RNG.integers(0, r)
                while c == prev:
                    c = RNG.integers(0, r)
                g[k:nxt] = c
                prev = c
                k = max(nxt, k + 1)
            return g
        report(f"arithmetic t_k=k, random non-cyclic runs", mk_t, mk_g, r,
               [2000, 8000, 32000, 128000])

    # 3. adversarial: many colours interleaved finely (runs of length 1)
    for r in [3, 5]:
        report("arithmetic t_k=k, length-1 runs cycling",
               lambda K: np.arange(1, K + 2, dtype=float),
               lambda K, r=r: np.array([j % r for j in range(K)]), r,
               [2000, 8000, 32000])
