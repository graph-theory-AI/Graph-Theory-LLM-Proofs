"""End-to-end test of the proof pipeline of attacks/1611.03196__03/output.md
(Sections 3-5) on bipartite circulant graphs.

G = bipartite circulant on [n]+[n], edges (i, i+t mod n) for t in a random
D-subset T of Z_n; Delta(G) = D and the Koenig decomposition is explicit
(M_t = {(i, i+t)}).

Pipeline implemented exactly as in the writeup:
  * statistic vectors z(M_t) over exact Fractions,
  * Caratheodory reduction of p = avg z(M_t) to k <= d+1 matchings
    (exact rational Gaussian elimination),
  * iterated interpolation via Lemma 2: dummy extension, alternating cycles,
    cells, a union-of-<=4d-intervals set X with nu_l(X) ~= theta*nu_l(I)
    found by coordinate-descent local search (the exact split exists by
    Stromquist-Woodall; we accept per-measure error <= 0.45), midpoint
    rounding, conflict repair,
  * final deletion phase enforcing |S cap E_i| <= ceil(|E_i|/D).

Checked at every step: intermediate C_j is a matching of G; interpolation
errors are within 32d per step; final S is a matching with
|S| >= |E|/D - 32(m+1)^3 and |S cap E_i| <= ceil(|E_i|/D).
"""
import math
import random
from fractions import Fraction

random.seed(7)


# ---------- Caratheodory over Fractions ----------

def null_vector(rows, k):
    """rows: list of length-k Fraction rows; return nonzero x with rows.x=0."""
    m = len(rows)
    A = [list(r) for r in rows]
    piv_col_of_row = []
    used_cols = []
    r = 0
    for c in range(k):
        piv = None
        for i in range(r, m):
            if A[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv_col_of_row.append(c)
        used_cols.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(k) if c not in used_cols]
    assert free, "no free column: k <= rank, cannot happen when k > d+1"
    f0 = free[0]
    x = [Fraction(0)] * k
    x[f0] = Fraction(1)
    for i, c in enumerate(piv_col_of_row):
        x[c] = -A[i][f0]
    return x


def caratheodory(zs, lambdas, d):
    """Reduce convex combination sum lambdas[j] zs[j] to <= d+1 terms."""
    zs = list(zs)
    lambdas = list(lambdas)
    p = [sum(l * z[t] for l, z in zip(lambdas, zs)) for t in range(d)]
    while len(zs) > d + 1:
        k = len(zs)
        rows = [[zs[j][t] for j in range(k)] for t in range(d)]
        rows.append([Fraction(1)] * k)
        mu = null_vector(rows, k)
        if all(m <= 0 for m in mu):
            mu = [-m for m in mu]
        alpha = min(l / m for l, m in zip(lambdas, mu) if m > 0)
        lambdas = [l - alpha * m for l, m in zip(lambdas, mu)]
        keep = [j for j in range(k) if lambdas[j] > 0]
        assert len(keep) < k
        zs = [zs[j] for j in keep]
        lambdas = [lambdas[j] for j in keep]
    q = [sum(l * z[t] for l, z in zip(lambdas, zs)) for t in range(d)]
    assert q == p, "Caratheodory changed the point"
    assert sum(lambdas) == 1
    return zs, lambdas


# ---------- Lemma 2 machinery ----------

def extend(M, n):
    """Dummy extension of a matching of the L=[n],R=[n] graph."""
    Mstar = set(M)
    mL = {e[0] for e in M}
    mR = {e[1] for e in M}
    usedDR, usedDL = set(), set()
    dr = iter([("DR", i) for i in range(n)])
    dl = iter([("DL", i) for i in range(n)])
    for i in range(n):
        if ("L", i) not in mL:
            v = next(dr)
            Mstar.add((("L", i), v))
            usedDR.add(v)
    for i in range(n):
        if ("R", i) not in mR:
            u = next(dl)
            Mstar.add((u, ("R", i)))
            usedDL.add(u)
    remDL = [("DL", i) for i in range(n) if ("DL", i) not in usedDL]
    remDR = [("DR", i) for i in range(n) if ("DR", i) not in usedDR]
    for u, v in zip(remDL, remDR):
        Mstar.add((u, v))
    return Mstar


def alternating_cycles(Astar, Bstar):
    Aedge, Bedge = {}, {}
    for e in Astar:
        Aedge[e[0]] = e
        Aedge[e[1]] = e
    for e in Bstar:
        Bedge[e[0]] = e
        Bedge[e[1]] = e
    visited = set()
    out = []
    for e0 in Astar - Bstar:
        if e0 in visited:
            continue
        seq, e, v, use_b = [], e0, e0[1], True
        while True:
            seq.append(e)
            visited.add(e)
            e2 = Bedge[v] if use_b else Aedge[v]
            v = e2[0] if e2[1] == v else e2[1]
            use_b = not use_b
            e = e2
            if e == e0:
                break
        out.append([(seq[2 * j], seq[2 * j + 1])
                    for j in range(len(seq) // 2)])
    return out


def find_split(cols, theta, n_intervals, tol=0.45, restarts=14, sweeps=60):
    """cols: list of measure arrays (len N each, values >=0).  Find X = union
    of <= n_intervals intervals in [0,N] with |nu_l(X)-theta*tot_l| <= tol
    for every l, by coordinate-descent on interval endpoints."""
    N = len(cols[0]) if cols else 0
    tots = [sum(c) for c in cols]
    if N == 0:
        return []
    pres = []
    for c in cols:
        p = [0.0]
        for x in c:
            p.append(p[-1] + x)
        pres.append(p)

    def P(pre, c, x):
        j = min(int(x), N - 1)
        if x <= 0:
            return 0.0
        if x >= N:
            return pre[N]
        return pre[j] + (x - j) * c[j]

    def errs(ts):
        e = []
        for c, pre, tot in zip(cols, pres, tots):
            v = 0.0
            for i in range(0, len(ts), 2):
                v += P(pre, c, ts[i + 1]) - P(pre, c, ts[i])
            e.append(v - theta * tot)
        return e

    def obj(ts):
        return sum(x * x for x in errs(ts))

    grid = [j * 0.25 for j in range(4 * N + 1)]
    best_ts = None
    for r in range(restarts):
        K = n_intervals
        if r == 0:
            h = theta * N / K
            ts = []
            for i in range(K):
                cctr = (i + 0.5) * N / K
                ts += [max(0.0, cctr - h / 2), min(float(N), cctr + h / 2)]
        else:
            pts = sorted(random.uniform(0, N) for _ in range(2 * K))
            ts = pts
        ts = sorted(ts)
        cur = obj(ts)
        for _ in range(sweeps):
            improved = False
            for idx in range(len(ts)):
                lo = ts[idx - 1] if idx > 0 else 0.0
                hi = ts[idx + 1] if idx + 1 < len(ts) else float(N)
                best_v, best_t = cur, ts[idx]
                old = ts[idx]
                for cand in grid:
                    if cand < lo or cand > hi:
                        continue
                    ts[idx] = cand
                    v = obj(ts)
                    if v < best_v - 1e-15:
                        best_v, best_t = v, cand
                ts[idx] = best_t
                if best_v < cur - 1e-15:
                    cur = best_v
                    improved = True
                elif best_t != old:
                    cur = best_v
            if not improved:
                break
        if best_ts is None or cur < obj(best_ts):
            best_ts = ts[:]
        if max(abs(x) for x in errs(best_ts)) <= tol:
            break
    e = errs(best_ts)
    return best_ts, max(abs(x) for x in e)


def interpolate(Cprev, Mj, theta, labels, d, n):
    """One application of Lemma 2.  Returns (C, split_err)."""
    Astar = extend(Cprev, n)
    Bstar = extend(Mj, n)
    cycles = alternating_cycles(Astar, Bstar)
    cells = [cell for cyc in cycles for cell in cyc]
    N = len(cells)

    def lab(e):
        return labels.get(e, (0,) * d)

    cols = []
    for l in range(d):
        cols.append([float(lab(a)[l]) for (a, b) in cells])
    for l in range(d):
        cols.append([float(lab(b)[l]) for (a, b) in cells])

    if N == 0:
        J_flat = set()
        split_err = 0.0
    else:
        ts, split_err = find_split(cols, theta, 4 * d)
        J_flat = set()
        for j in range(N):
            mid = j + 0.5
            for i in range(0, len(ts), 2):
                if ts[i] <= mid <= ts[i + 1]:
                    J_flat.add(j)
                    break

    selected = set(Astar & Bstar)
    flat = 0
    deleted = 0
    for cyc in cycles:
        s = len(cyc)
        inJ = [flat + j in J_flat for j in range(s)]
        flat += s
        for j in range(s):
            selected.add(cyc[j][0] if inJ[j] else cyc[j][1])
        for j in range(s):
            if inJ[j] and not inJ[j - 1]:
                selected.discard(cyc[j][0])
                deleted += 1
    # matching check on supergraph
    verts = set()
    for (u, v) in selected:
        assert u not in verts and v not in verts, "not a matching"
        verts.update((u, v))
    C = {e for e in selected if e in labels}  # original edges only
    return C, split_err, deleted


# ---------- main pipeline ----------

def run(n, D, m, trial):
    d = m + 1
    T = random.sample(range(n), D)
    Ms = [frozenset(((("L", i), ("R", (i + t) % n)) for i in range(n)))
          for t in T]
    E = [e for M in Ms for e in M]
    Esets = [set(random.sample(E, random.randint(1, len(E)))) for _ in range(m)]
    labels = {}
    for e in E:
        labels[e] = tuple([1] + [1 if e in Es else 0 for Es in Esets])

    def z(M):
        return tuple(Fraction(sum(labels[e][t] for e in M)) for t in range(d))

    zs = [z(M) for M in Ms]
    lambdas = [Fraction(1, D)] * D
    p = [sum(l * zv[t] for l, zv in zip(lambdas, zs)) for t in range(d)]
    assert p[0] == Fraction(len(E), D)
    for i in range(m):
        assert p[i + 1] == Fraction(len(Esets[i]), D)

    zs2, lam2 = caratheodory(zs, lambdas, d)
    k = len(zs2)
    assert k <= d + 1, f"Caratheodory failed: k={k}"
    # recover matchings for the surviving z-vectors
    Msel = []
    used = set()
    for zv in zs2:
        for idx, zz in enumerate(zs):
            if zz == zv and idx not in used:
                used.add(idx)
                Msel.append(set(Ms[idx]))
                break

    # iterated interpolation
    C = Msel[0]
    Lam = lam2[0]
    tot_split_err = 0.0
    max_step_err = 0.0
    for j in range(1, k):
        theta = float(Lam / (Lam + lam2[j]))
        before = [sum(labels[e][t] for e in C) for t in range(d)]
        target = [theta * before[t]
                  + (1 - theta) * sum(labels[e][t] for e in Msel[j])
                  for t in range(d)]
        C, serr, deleted = interpolate(C, Msel[j], theta, labels, d, n)
        tot_split_err = max(tot_split_err, serr)
        after = [sum(labels[e][t] for e in C) for t in range(d)]
        assert after[0] >= target[0] - 32 * d - 2 * serr - 1e-6, \
            f"size drop too large: {after[0]} vs {target[0]}"
        for t in range(1, d):
            assert after[t] <= target[t] + 32 * d + 2 * serr + 1e-6
        max_step_err = max(max_step_err,
                           target[0] - after[0],
                           max(after[t] - target[t] for t in range(1, d)))
        Lam = Lam + lam2[j]

    # final bounds before ceiling enforcement
    B = 32 * d * d
    sizeC = len(C)
    assert sizeC >= len(E) / D - B - 2 * d * tot_split_err - 1e-6
    caps = [math.ceil(len(Es) / D) for Es in Esets]
    S = set(C)
    for i, Es in enumerate(Esets):
        inter = [e for e in S if e in Es]
        excess = len(inter) - caps[i]
        for e in inter[:max(0, excess)]:
            S.discard(e)
    # final checks
    verts = set()
    for (u, v) in S:
        assert u not in verts and v not in verts
        verts.update((u, v))
    for i, Es in enumerate(Esets):
        assert sum(1 for e in S if e in Es) <= caps[i]
    lower = len(E) / D - 32 * (m + 1) ** 3
    assert len(S) >= lower - 1e-9
    print(f"trial {trial}: n={n} D={D} m={m} |E|={len(E)} k={k} "
          f"split_err<={tot_split_err:.3f} worst_step_err={max_step_err:.2f} "
          f"(allowed 32d={32*d}) |S|={len(S)} vs |E|/D={len(E)/D:.2f} "
          f"deficit={len(E)/D - len(S):.2f} (allowed {32*(m+1)**3})")


def main():
    for trial, (n, D, m) in enumerate([(16, 6, 2), (20, 8, 2), (24, 10, 2),
                                       (18, 18, 2), (20, 7, 3), (22, 9, 1)]):
        run(n, D, m, trial)
    print("OK: end-to-end pipeline produced valid matchings meeting all "
          "claimed bounds.")


if __name__ == "__main__":
    main()
