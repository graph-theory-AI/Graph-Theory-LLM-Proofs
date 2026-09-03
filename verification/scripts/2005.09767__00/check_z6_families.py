"""Verify the writeup's Section 3 (Z_6) construction mechanically.

For each test graph and many random f : E -> Z_6:
 1. find one admissible flow phi_0 (brute force; existence = JLPT input),
    set t(e) = f(e) - phi_0(e)  (all nonzero), classes via CRT Z_6 = F_2 x F_3
    (CRT map used: z mod 6 <-> (z mod 2, z mod 3)):
        A = {t = 3}, B = {t in {2,4}}, C = {t in {1,5}},  a+b+c = m.
 2. Family 1 (Sec 3.2): x binary flow, x=0 on A  ->  psi with psi(e) = 3*x(e).
    Check every member is a Z_6-flow avoiding t; check count >= 2^max(r-a,0).
 3. Family 2 (Sec 3.3): y ternary flow with y(e) != t mod 3 on B -> psi = 4*y ... i.e.
    psi(e) = CRT(0, y(e)). Check all avoid t; check count >= 3^(max(2r-b,0)/2).
 4. Family 3 (Sec 3.4): x binary flow with x=0 on C; lift y via Eulerian
    orientation of supp(x) (Lemma 2), psi = CRT(x, y). Check flow property,
    values in {0,1,5} with support = supp x, avoidance of t; count of distinct
    psi >= 2^max(r-c,0).
 5. Check total N(G,f) >= max of the three family bounds and >= 3^((4r-m)/6).
"""
import itertools, random
import numpy as np
from check_flows import cycle_space_basis, all_flows, GRAPHS

def crt(x2, x3):
    """element of Z_6 with given residues mod 2 and mod 3"""
    for z in range(6):
        if z % 2 == x2 and z % 3 == x3:
            return z
    raise AssertionError

def is_flow(n, edges, vec, k):
    net = [0] * n
    for (u, v), val in zip(edges, vec):
        net[u] -= val; net[v] += val
    return all(x % k == 0 for x in net)

def eulerian_lift(n, edges, x):
    """Lemma 2: given binary flow x (0/1 vector), return integer y with values in
    {-1,0,1}, supp y = supp x, y an integer circulation (Eulerian orientation)."""
    m = len(edges)
    sup = [i for i in range(m) if x[i] % 2]
    # multigraph on support; every vertex has even degree (loops add 2)
    inc = {v: [] for v in range(n)}
    for i in sup:
        u, v = edges[i]
        inc[u].append(i); inc[v].append(i)
    used = [False] * m
    y = [0] * m
    # decompose into closed walks (Hierholzer per component)
    for start_edge in sup:
        if used[start_edge]:
            continue
        # walk from tail of start_edge
        walk = []
        v0 = edges[start_edge][0]
        v = v0
        while True:
            nxt = None
            for i in inc[v]:
                if not used[i]:
                    nxt = i; break
            if nxt is None:
                break
            used[nxt] = True
            u1, v1 = edges[nxt]
            if u1 == v:      # traverse along orientation
                y[nxt] = 1;  v = v1
            else:            # traverse against orientation
                y[nxt] = -1; v = u1
            walk.append(nxt)
            if v == v0 and all(used[i] for i in inc[v]):
                break
        # (for even graphs Hierholzer closes each walk; conservation checked below)
    assert all(used[i] for i in sup)
    assert is_flow(n, edges, y, 10**9), "Eulerian lift is not an integer circulation"
    assert all((y[i] != 0) == (i in sup) for i in range(m))
    return y

def run(name, n, edges, trials=60, seed=7):
    m = len(edges); r = m - n + 1
    if 6 ** r > 6 ** 7:
        print(f"{name}: skipped (too big)"); return True
    flows6 = all_flows(n, edges, 6)
    basis = cycle_space_basis(n, edges)
    B2 = np.array(basis) % 2
    coef2 = np.array(list(itertools.product(range(2), repeat=r)))
    flows2 = coef2 @ np.array(basis) % 2
    B3 = np.array(basis) % 3
    coef3 = np.array(list(itertools.product(range(3), repeat=r)))
    flows3 = coef3 @ np.array(basis) % 3
    rng = random.Random(seed)
    ok = True
    for tr in range(trials):
        f = np.array([rng.randrange(6) for _ in range(m)])
        avoid = (flows6 != f[None, :]).all(axis=1)
        N = int(avoid.sum())
        if N == 0:
            print(f"{name}: JLPT FAILS?! f={f}"); ok = False; continue
        phi0 = flows6[np.argmax(avoid)]
        t = (f - phi0) % 6
        assert np.all(t != 0)
        A = [i for i in range(m) if t[i] == 3]
        Bc = [i for i in range(m) if t[i] in (2, 4)]
        C = [i for i in range(m) if t[i] in (1, 5)]
        a, b, c = len(A), len(Bc), len(C)
        assert a + b + c == m
        # Family 1: binary flows vanishing on A, embedded as psi = 3*x
        fam1 = flows2[(flows2[:, A] == 0).all(axis=1)] if A else flows2
        cnt1 = 0
        for x in fam1:
            psi = (3 * x) % 6
            assert is_flow(n, edges, psi, 6)
            assert all(int(p) != int(tt) for p, tt in zip(psi, t)), \
                f"family1 member hits t! {name} f={f}"
            cnt1 += 1
        assert cnt1 >= 2 ** max(r - a, 0), (name, "fam1 count", cnt1, r, a)
        # Family 2: ternary flows avoiding t mod 3 on B, psi = CRT(0, y)
        t3 = t % 3
        m2 = (flows3[:, Bc] != t3[Bc][None, :]).all(axis=1) if Bc else \
             np.ones(len(flows3), bool)
        cnt2 = 0
        for y in flows3[m2]:
            psi = [crt(0, int(yy)) for yy in y]
            assert is_flow(n, edges, psi, 6)
            assert all(int(p) != int(tt) for p, tt in zip(psi, t)), \
                f"family2 member hits t! {name} f={f}"
            cnt2 += 1
        assert cnt2 >= 3 ** (max(2 * r - b, 0) / 2) - 1e-9, (name, "fam2", cnt2)
        # Family 3: binary flows vanishing on C, Eulerian ternary lift
        fam3 = flows2[(flows2[:, C] == 0).all(axis=1)] if C else flows2
        seen_psi = set()
        for x in fam3:
            y = eulerian_lift(n, edges, [int(v) for v in x])
            psi = [crt(int(xx) % 2, int(yy) % 3) for xx, yy in zip(x, y)]
            assert is_flow(n, edges, psi, 6)
            assert all(p in (0, 1, 5) for p in psi)
            assert all(int(p) != int(tt) for p, tt in zip(psi, t)), \
                f"family3 member hits t! {name} f={f}"
            seen_psi.add(tuple(psi))
        cnt3 = len(seen_psi)
        assert cnt3 >= 2 ** max(r - c, 0), (name, "fam3", cnt3)
        # combined bound
        claimed = 3 ** ((4 * r - m) / 6)
        assert N >= max(cnt1, cnt2, cnt3) - 1e-9
        assert N >= claimed - 1e-9, (name, N, claimed)
    print(f"{name:22s} ok over {trials} random f  (r={r})")
    return ok

if __name__ == "__main__":
    allok = True
    for name, (n, edges) in GRAPHS.items():
        allok &= run(name, n, edges)
    print("ALL OK" if allok else "PROBLEM FOUND")
