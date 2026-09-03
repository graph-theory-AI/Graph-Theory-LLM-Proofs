"""Exact enumeration checks for writeup 2211.01032__02 on small graphs.

Model: darts = ordered pairs (u,v), uv in E. rho_v = uniform random cyclic
permutation of darts based at v (dart (v,w) is "based at v"). iota reverses
darts. Facial permutation Phi = rho o iota:  Phi((u,v)) = rho_v((v,u)).
F = number of cycles of Phi.

Checks (by full enumeration of all rotation systems):
 A. cycle-rooting identity  F = sum_a 1/L(a).
 B. Pr(specific oriented rooted simple cycle is facial) = prod 1/(d_i - 1)   [eq 4.1]
 C. Lemma 3.1:  Pr(L(a)=ell and C(a) light) <= 1/((1-theta)^2 delta^2), all ell, a.
 D. E X_ell >= (tr S^ell - B_ell)/ell  with B_ell = C(ell,2) n/delta^2  [eqs 4.3,4.7]
"""
import itertools, fractions, math
import numpy as np
from fractions import Fraction

def darts_of(G):
    return [(u, v) for u in G for v in G[u]]

def cyclic_perms(items):
    """All cyclic permutations of items, as dict successor maps."""
    items = list(items)
    if len(items) == 1:
        yield {items[0]: items[0]}
        return
    first = items[0]
    for perm in itertools.permutations(items[1:]):
        order = [first] + list(perm)
        yield {order[i]: order[(i + 1) % len(order)] for i in range(len(order))}

def faces_of(G, rot):
    """rot: dict vertex -> successor map on its darts. Returns list of faces
    (each a tuple of darts)."""
    Phi = {}
    for (u, v) in darts_of(G):
        Phi[(u, v)] = rot[v][(v, u)]
    seen, faces = set(), []
    for a in Phi:
        if a in seen:
            continue
        face, x = [], a
        while x not in seen:
            seen.add(x)
            face.append(x)
            x = Phi[x]
        faces.append(tuple(face))
    return faces

def check_graph(G, name, thetas, cycle_tests, max_ell_D):
    verts = sorted(G)
    n = len(verts)
    deg = {v: len(G[v]) for v in verts}
    delta = min(deg.values())
    D = darts_of(G)
    N = len(D)
    print(f"== {name}: n={n} degrees={sorted(deg.values())} N={N}")

    rot_choices = [list(cyclic_perms([(v, w) for w in G[v]])) for v in verts]
    total = 1
    for rc in rot_choices:
        total *= len(rc)
    print(f"   enumerating {total} rotation systems")

    EF = Fraction(0)
    # per (a, ell, theta): count of systems with L(a)=ell and light
    from collections import defaultdict
    light_count = {th: defaultdict(int) for th in thetas}
    cyc_count = defaultdict(int)   # oriented rooted cycle -> #systems facial
    X_count = defaultdict(int)     # ell -> total #(simple-cycle faces) over systems
    rooting_ok = True

    for combo in itertools.product(*rot_choices):
        rot = dict(zip(verts, combo))
        faces = faces_of(G, rot)
        EF += len(faces)
        # A. rooting identity: sum over DARTS of 1/L(a) equals F
        s = sum(Fraction(1, len(f)) for f in faces for _ in f)
        if s != len(faces):
            rooting_ok = False
        for f in faces:
            ell = len(f)
            # r_C(v) = # darts of face based at v
            r = defaultdict(int)
            for (u, v) in f:
                r[u] += 1
            for th in thetas:
                if all(r[v] <= th * deg[v] for v in r):
                    for a in f:
                        light_count[th][(a, ell)] += 1
            # vertex-simple boundary?
            bases = [u for (u, v) in f]
            if len(set(bases)) == ell:
                X_count[ell] += 1
                # record oriented rooted cycles (for check B): all rootings
                for i in range(ell):
                    key = tuple(bases[i:] + bases[:i])
                    cyc_count[key] += 1

    EF /= total
    print(f"   E[F] = {EF} = {float(EF):.4f}")
    print(f"   A. rooting identity F = sum 1/L(a): {'OK' if rooting_ok else 'FAIL'}")

    # B. facial-cycle probability
    okB = True
    for cyc in cycle_tests:
        ell = len(cyc)
        pred = Fraction(1)
        for v in cyc:
            pred /= (deg[v] - 1)
        got = Fraction(cyc_count.get(tuple(cyc), 0), total)
        ok = (got == pred)
        okB = okB and ok
        print(f"   B. Pr(cycle {cyc} facial) = {got} vs predicted {pred}: "
              f"{'OK' if ok else 'FAIL'}")

    # C. Lemma 3.1
    for th in thetas:
        bound = 1.0 / ((1 - th) ** 2 * delta ** 2)
        worst, warg = 0.0, None
        for (a, ell), c in light_count[th].items():
            p = c / total
            if p > worst:
                worst, warg = p, (a, ell)
        status = "OK" if worst <= bound + 1e-12 else "FAIL"
        print(f"   C. theta={th}: max_a,ell Pr(L(a)=ell & light) = {worst:.6f} "
              f"(at {warg}) <= bound {bound:.6f}: {status}")

    # D. E X_ell >= (tr S^ell - B_ell)/ell
    A = np.zeros((n, n))
    idx = {v: i for i, v in enumerate(verts)}
    for u in G:
        for v in G[u]:
            A[idx[u], idx[v]] = 1
    Dm12 = np.diag([deg[v] ** -0.5 for v in verts])
    S = Dm12 @ A @ Dm12
    for ell in range(3, max_ell_D + 1):
        EX = X_count[ell] / total
        trS = np.trace(np.linalg.matrix_power(S, ell))
        B = math.comb(ell, 2) * n / delta ** 2
        lower = (trS - B) / ell
        ok = EX >= lower - 1e-9
        print(f"   D. ell={ell}: E X_ell = {EX:.5f} >= (trS^l - B_l)/l = "
              f"{lower:.5f}: {'OK' if ok else 'FAIL'}  (trS^l={trS:.4f}, B_l={B:.3f})")
    print()

if __name__ == "__main__":
    # K5
    K5 = {v: [w for w in range(5) if w != v] for v in range(5)}
    check_graph(K5, "K5", thetas=[0.25, 0.5, 0.6],
                cycle_tests=[(0, 1, 2), (0, 1, 2, 3), (0, 2, 4, 1, 3)],
                max_ell_D=5)
    # Octahedron K_{2,2,2}: 6 vertices, 4-regular
    OCT = {v: [w for w in range(6) if w != v and w != (v + 3) % 6] for v in range(6)}
    check_graph(OCT, "Octahedron K_{2,2,2}", thetas=[0.5],
                cycle_tests=[(0, 1, 2), (0, 1, 3, 4)],
                max_ell_D=5)
