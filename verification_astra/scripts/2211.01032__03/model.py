"""Flag / ribbon-graph model for signed rotation embeddings of K_n.

Flags: (u, v, s) with u != v, s in {0,1}.  id = (u*(n-1) + nb(u,v))*2 + s
where nb(u,v) = v - (v>u).

J_u  pairs (u,v,0)-(u,v,1)                       (the two sides of an incidence)
V_u  pairs (u,p_i,1)-(u,p_{i+1},0)               (arcs of the vertex disc)
A    pairs (u,v,s)-(v,u,s^tw)  with tw = 1 for an untwisted band (see below)

Faces = connected components of A u V  =  (cycles of A.V)/2.
"""
import numpy as np


def nb_index(n, u, v):
    return v - (v > u)


def build_A(n, twist):
    """twist: (n,n) symmetric 0/1 array, twist[u,v]=1 means the signature is -1.
    UNTWISTED band flips the side bit (convention, verified against the
    orientable permutation model in tests)."""
    N = 2 * n * (n - 1)
    A = np.empty(N, dtype=np.int64)
    u = np.repeat(np.arange(n), n - 1)
    slot = np.tile(np.arange(n - 1), n)
    v = slot + (slot >= u)                      # neighbour named by the slot
    tw = twist[u, v]
    for s in (0, 1):
        src = (u * (n - 1) + slot) * 2 + s
        tgt_slot = u - (u > v)                  # slot of u inside v's list
        dst = (v * (n - 1) + tgt_slot) * 2 + (s ^ (1 - tw))
        A[src] = dst
    return A


def build_V(n, P):
    """P: (n, n-1) array, P[u] a permutation of the slots = rotation at u."""
    N = 2 * n * (n - 1)
    V = np.empty(N, dtype=np.int64)
    base = (np.arange(n) * (n - 1))[:, None]
    cur = (base + P) * 2 + 1
    nxt = (base + np.roll(P, -1, axis=1)) * 2
    V[cur.ravel()] = nxt.ravel()
    V[nxt.ravel()] = cur.ravel()
    return V


def count_cycles(sigma):
    """number of cycles of a permutation given as an array (pointer jumping)"""
    N = len(sigma)
    m = np.arange(N, dtype=np.int64)
    s = sigma.copy()
    k = int(np.ceil(np.log2(max(N, 2)))) + 1
    for _ in range(k):
        m = np.minimum(m, m[s])
        s = s[s]
    return int(np.count_nonzero(m == np.arange(N)))


def faces_components(A, V):
    """component labels of A u V; returns (labels, n_components)"""
    N = len(A)
    sigma = A[V]                      # apply V then A
    m = np.arange(N, dtype=np.int64)
    s = sigma.copy()
    k = int(np.ceil(np.log2(max(N, 2)))) + 1
    for _ in range(k):
        m = np.minimum(m, m[s])
        s = s[s]
    # a face = a component of A u V = two cycles of sigma; merge i with A[i]
    lab = np.minimum(m, m[A])
    ncomp = int(np.count_nonzero(lab == np.arange(N)))
    return lab, ncomp


def random_sample(n, rng, nonorientable_only=False):
    P = np.argsort(rng.random((n, n - 1)), axis=1)
    while True:
        tw = np.zeros((n, n), dtype=np.int64)
        iu = np.triu_indices(n, 1)
        bits = rng.integers(0, 2, size=len(iu[0]))
        tw[iu] = bits
        tw = tw + tw.T
        if not nonorientable_only:
            break
        # orientable iff the signature is a coboundary: check by BFS
        if not is_orientable(n, tw):
            break
    return P, tw


def is_orientable(n, tw):
    col = -np.ones(n, dtype=int)
    col[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v in range(n):
            if v == u:
                continue
            c = col[u] ^ int(tw[u, v])
            if col[v] < 0:
                col[v] = c
                stack.append(v)
            elif col[v] != c:
                return False
    return True


# ---- reference: orientable face count from the permutation model -------------
def orientable_faces(n, P):
    """faces of the rotation system P with all-positive signature,
    via cycles of pi o iota on darts (u,v)."""
    darts = {}
    idx = 0
    for u in range(n):
        for v in range(n):
            if u != v:
                darts[(u, v)] = idx
                idx += 1
    perm = np.empty(idx, dtype=np.int64)
    rot = {}
    for u in range(n):
        order = [s + (s >= u) for s in P[u]]
        for i, v in enumerate(order):
            rot[(u, v)] = order[(i + 1) % (n - 1)]
    for (u, v), i in darts.items():
        # iota: (u,v) -> (v,u); then pi at v
        w = rot[(v, u)]
        perm[i] = darts[(v, w)]
    return count_cycles(perm)
