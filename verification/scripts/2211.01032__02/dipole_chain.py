"""Check Section 5 of the writeup: chained dipoles multigraph has F >= k+1
for EVERY rotation system, where k = number of dipoles, each dipole having an
even number M of parallel edges. Also checks F(dipole) = M - 2g parity claim.

Multigraph darts: each edge e = {u,v} gives darts (e,u->v) and (e,v->u).
"""
import itertools, random
from collections import defaultdict

def faces_count(vert_darts, rot):
    """vert_darts: v -> list of darts based at v; rot: v -> successor map.
    Dart = (edge_id, tail, head). Phi(x) = rot[head(x)][reverse(x)]."""
    Phi = {}
    for v, ds in vert_darts.items():
        for d in ds:
            eid, t, h = d
            rev = (eid, h, t)
            Phi[rev] = rot[t][d]  # careful below; we build directly instead
    # rebuild cleanly: Phi(x) = rho_{head(x)}( iota(x) )
    Phi = {}
    all_darts = [d for ds in vert_darts.values() for d in ds]
    for x in all_darts:
        eid, t, h = x
        iota_x = (eid, h, t)
        Phi[x] = rot[h][iota_x]
    seen, F = set(), 0
    for a in all_darts:
        if a in seen:
            continue
        F += 1
        x = a
        while x not in seen:
            seen.add(x)
            x = Phi[x]
    return F

def build_chain(k, M):
    """k dipoles, vertices (2i, 2i+1) joined by M parallel edges; bridge from
    vertex 2i+1 to 2i+2."""
    vert_darts = defaultdict(list)
    eid = 0
    for i in range(k):
        u, v = 2 * i, 2 * i + 1
        for _ in range(M):
            vert_darts[u].append((eid, u, v))
            vert_darts[v].append((eid, v, u))
            eid += 1
    for i in range(k - 1):
        u, v = 2 * i + 1, 2 * i + 2
        vert_darts[u].append((eid, u, v))
        vert_darts[v].append((eid, v, u))
        eid += 1
    return dict(vert_darts)

def random_rot(vert_darts):
    rot = {}
    for v, ds in vert_darts.items():
        ds = ds[:]
        random.shuffle(ds)
        rot[v] = {ds[i]: ds[(i + 1) % len(ds)] for i in range(len(ds))}
    return rot

random.seed(7)

# 1. single dipole, M=4: F should always be even (F = M - 2g, M even), F>=2
vd = build_chain(1, 4)
Fs = set()
for _ in range(20000):
    Fs.add(faces_count(vd, random_rot(vd)))
print(f"single dipole M=4: observed F values {sorted(Fs)} (expect even, >=2)")

# 2. chain of k=3 dipoles with M=4, bridges: claim F >= k+1 = 4 always
vd = build_chain(3, 4)
minF, cnt = 99, defaultdict(int)
for _ in range(20000):
    F = faces_count(vd, random_rot(vd))
    cnt[F] += 1
    minF = min(minF, F)
print(f"chain k=3, M=4: min F over 20000 samples = {minF} (claim >= 4); "
      f"distribution {dict(sorted(cnt.items()))}")

# 3. scaling: k = n/2 dipoles with M = n edges, n = 12 -> F >= n/2+1 = 7
n = 12
vd = build_chain(n // 2, n)
minF = 999
tot = 0
REPS = 2000
for _ in range(REPS):
    F = faces_count(vd, random_rot(vd))
    minF = min(minF, F)
    tot += F
print(f"chain n={n} (k={n//2}, M={n}): min F = {minF} (claim >= {n//2+1}), "
      f"mean F = {tot/REPS:.2f}")
