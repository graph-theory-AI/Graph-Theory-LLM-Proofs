"""Brute-force deterministic zombie number solver (FHMP16 / arXiv:2008.03587 rules).

Game: z zombies pick start vertices; then the survivor picks a start vertex
(placed on a zombie = immediately caught). Rounds: all zombies move
simultaneously, each MUST move to a neighbour strictly closer to the survivor
(i.e. along some geodesic; the zombie player chooses which one -- the
"deterministic / free-will" version). If a zombie lands on the survivor,
capture. Otherwise the survivor moves to an adjacent vertex or stays; the
survivor never steps onto a zombie (that is capture). Survivor wins by
evading forever. Finite state space => fixed-point (attractor) computation.

z(G) = min z such that some zombie placement beats every survivor placement.

No external dependencies (pure stdlib).
"""

import itertools
from collections import deque


def bfs_dist(adj, src):
    d = {src: 0}
    q = deque([src])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if w not in d:
                d[w] = d[u] + 1
                q.append(w)
    return d


def all_dist(adj):
    return {v: bfs_dist(adj, v) for v in adj}


def zombie_moves(adj, dist, zs, s):
    """All joint moves: each zombie moves to a neighbour closer to s."""
    options = []
    for z in zs:
        opts = [w for w in adj[z] if dist[w][s] == dist[z][s] - 1]
        options.append(opts)  # nonempty in a connected graph when z != s
    return itertools.product(*options)


def solve(adj, nzomb):
    """win[(sorted zombie tuple, survivor)] = zombies (to move) force capture."""
    dist = all_dist(adj)
    nodes = list(adj)
    states = [(zt, v)
              for zt in itertools.combinations_with_replacement(sorted(nodes, key=repr), nzomb)
              for v in nodes]
    win = {st: False for st in states}
    changed = True
    while changed:
        changed = False
        for (zt, v) in states:
            if win[(zt, v)]:
                continue
            if v in zt:
                win[(zt, v)] = True
                changed = True
                continue
            for mv in zombie_moves(adj, dist, zt, v):
                nz = tuple(sorted(mv, key=repr))
                if v in nz:
                    good = True  # captured on the zombie move
                else:
                    good = True
                    for w in list(adj[v]) + [v]:
                        if w in nz:
                            continue  # stepping onto a zombie = loss for survivor
                        if not win[(nz, w)]:
                            good = False
                            break
                if good:
                    win[(zt, v)] = True
                    changed = True
                    break
    return win


def k_zombies_suffice(adj, k):
    nodes = list(adj)
    win = solve(adj, k)
    for zs in itertools.combinations_with_replacement(sorted(nodes, key=repr), k):
        if all(win[(zs, s)] for s in nodes):
            return True
    return False


def zombie_number(adj, kmax=4):
    for k in range(1, kmax + 1):
        if k_zombies_suffice(adj, k):
            return k
    return None


# ---------------- graph builders (pure dict-of-sets) ----------------

def cycle(n):
    return {i: {(i - 1) % n, (i + 1) % n} for i in range(n)}


def path(n):
    adj = {i: set() for i in range(n)}
    for i in range(n - 1):
        adj[i].add(i + 1)
        adj[i + 1].add(i)
    return adj


def complete(n):
    return {i: set(range(n)) - {i} for i in range(n)}


def augmented_subdivision(adj, k):
    """G'_k: subdivide every edge k times, then re-add the original edges."""
    H = {v: set() for v in adj}
    edges = {frozenset((u, v)) for u in adj for v in adj[u]}

    def add(a, b):
        H.setdefault(a, set()).add(b)
        H.setdefault(b, set()).add(a)

    for e in edges:
        u, v = tuple(e)
        prev = u
        for i in range(k):
            x = ("sub", u, v, i)
            add(prev, x)
            prev = x
        add(prev, v)
        add(u, v)  # re-add the original edge
    return H


def is_cycle_of_length(adj, n):
    if len(adj) != n:
        return False
    if any(len(nb) != 2 for nb in adj.values()):
        return False
    # connected 2-regular graph on n vertices = C_n
    seen = bfs_dist(adj, next(iter(adj)))
    return len(seen) == n


if __name__ == "__main__":
    # 1. z(K2) = 1 (writeup claim)
    print("z(K2) =", zombie_number(complete(2)))

    # 2. z(C_n) for n = 3..9 (writeup claims z(C_n) <= 2, and = 2 for n >= 4)
    for n in range(3, 10):
        print(f"z(C_{n}) =", zombie_number(cycle(n)))

    # 3. (K2)'_k is C_{k+2}; z((K2)'_k) for k = 1..7 (writeup: <= 2 always)
    for k in range(1, 8):
        H = augmented_subdivision(complete(2), k)
        print(f"(K2)'_{k} is C_{k+2}: {is_cycle_of_length(H, k + 2)}, "
              f"z = {zombie_number(H)}")

    # 4. The real Question 4.2 (>= version) on K2: z((K2)'_k) >= z(K2)+1 = 2?
    for k in range(2, 6):
        H = augmented_subdivision(complete(2), k)
        print(f"z((K2)'_{k}) >= 2 :", zombie_number(H) >= 2)

    # 5. Tree partial claim: z(P3) = 1 and z((P3)'_k) >= 2 for k = 2, 3
    print("z(P3) =", zombie_number(path(3)))
    for k in (2, 3):
        H = augmented_subdivision(path(3), k)
        print(f"z((P3)'_{k}) =", zombie_number(H), f"(n={len(H)})")
