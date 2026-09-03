"""Check inequality (1) of the writeup's mixing lemma on A_5.

Claim (writeup Section 3, eq. (1)): for u, v in l^2(H) orthogonal to constants
(normalized inner product <f,g> = (1/N) sum f(x) conj(g(x))),
    E_h |<lambda(h)u, v>|^2  <=  ||u||^2 ||v||^2 / D,
where D = D(H) is the minimal dimension of a nontrivial irrep (D(A_5) = 3).

We verify:
  1. random mean-zero u, v (many samples): ratio <= 1/D;
  2. alternating power-iteration maximization of the ratio: sup should be ~ 1/D;
  3. the exact identity |hA cap B|/N - alpha*beta = <lambda(h) u_A, u_B>;
  4. the variance bound E_h(|hA cap B|/N - ab)^2 <= a(1-a)b(1-b)/D on many
     random subsets A, B, including subgroup cosets (near-extremal cases).
"""
import itertools, random
import numpy as np

random.seed(1)
rng = np.random.default_rng(1)

# ---- build A_5 as permutations of range(5) ----
def is_even(p):
    inv = sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])
    return inv % 2 == 0

elements = [p for p in itertools.permutations(range(5)) if is_even(p)]
N = len(elements)
assert N == 60
index = {p: i for i, p in enumerate(elements)}

def compose(p, q):  # (p*q)(x) = p(q(x))
    return tuple(p[q[x]] for x in range(len(q)))

# left translation tables: L_h : x -> h x  (as index permutation)
L = np.zeros((N, N), dtype=int)
for hi, h in enumerate(elements):
    for xi, x in enumerate(elements):
        L[hi, xi] = index[compose(h, x)]

D = 3  # minimal nontrivial irrep dimension of A_5 (irreps: 1,3,3,4,5)

def second_moment(u, v):
    """E_h |<lambda(h)u, v>|^2 with normalized inner product.
    (lambda(h)u)(x) = u(h^{-1}x); equivalently <lambda(h)u,v> = (1/N) sum_x u(x) v(hx)."""
    tot = 0.0
    for hi in range(N):
        ip = np.dot(u, v[L[hi]]) / N
        tot += ip * ip
    return tot / N

# ---- 1. random mean-zero vectors ----
worst = 0.0
for _ in range(300):
    u = rng.standard_normal(N); u -= u.mean()
    v = rng.standard_normal(N); v -= v.mean()
    ratio = second_moment(u, v) / ((u @ u / N) * (v @ v / N))
    worst = max(worst, ratio)
print(f"random mean-zero vectors: max ratio = {worst:.6f}  (bound 1/D = {1/D:.6f})")
assert worst <= 1 / D + 1e-9

# ---- 2. alternating maximization of the ratio ----
# For fixed u, E_h |<lambda(h)u,v>|^2 = v^T M_u v / N^2 restricted to mean-zero v,
# with M_u = (1/N) sum_h w_h w_h^T, w_h(x) = u(h^{-1} x).  Maximize alternately.
u = rng.standard_normal(N); u -= u.mean(); u /= np.linalg.norm(u)
for it in range(30):
    W = u[np.argsort(L, axis=1)] if False else None
    # rows: w_h(x) = u at position where L maps... build directly:
    Wm = np.empty((N, N))
    for hi in range(N):
        # w_h = lambda(h) u, i.e. w_h(hx) = u(x)  =>  w_h[L[hi]] = u
        w = np.empty(N); w[L[hi]] = u; Wm[hi] = w
    M = Wm.T @ Wm / N
    # project onto mean-zero subspace and take top eigenvector for v, then swap roles
    P = np.eye(N) - np.ones((N, N)) / N
    Mz = P @ M @ P
    vals, vecs = np.linalg.eigh(Mz)
    v = vecs[:, -1]; v -= v.mean(); v /= np.linalg.norm(v)
    u, v = v, u
ratio = second_moment(u, u) / ((u @ u / N) ** 2)
print(f"alternating maximization: ratio = {ratio:.6f}  (should approach 1/D = {1/D:.6f})")
assert ratio <= 1 / D + 1e-9

# ---- 3 & 4. identity and variance bound on subsets ----
def check_sets(A_idx, B_idx, label):
    a = len(A_idx) / N; b = len(B_idx) / N
    uA = np.zeros(N); uA[list(A_idx)] = 1; uA -= a
    uB = np.zeros(N); uB[list(B_idx)] = 1; uB -= b
    Bset = set(B_idx)
    var = 0.0
    for hi in range(N):
        hA = {L[hi, x] for x in A_idx}
        X = len(hA & Bset) / N
        # identity check
        ip = np.dot(uA, uB[L[hi]]) / N
        assert abs((X - a * b) - ip) < 1e-12, (label, hi)
        var += (X - a * b) ** 2
    var /= N
    bound = a * (1 - a) * b * (1 - b) / D
    ok = var <= bound + 1e-12
    print(f"{label}: Var = {var:.6f}, bound a(1-a)b(1-b)/D = {bound:.6f}, ok = {ok}")
    assert ok

# random subsets
for trial in range(20):
    A_idx = rng.choice(N, size=rng.integers(5, 55), replace=False)
    B_idx = rng.choice(N, size=rng.integers(5, 55), replace=False)
    a = len(A_idx) / N; b = len(B_idx) / N
    uA = np.zeros(N); uA[A_idx] = 1; uA -= a
    uB = np.zeros(N); uB[B_idx] = 1; uB -= b
    Bset = set(B_idx.tolist())
    var = 0.0
    for hi in range(N):
        X = len({L[hi, x] for x in A_idx} & Bset) / N
        var += (X - a * b) ** 2
    var /= N
    assert var <= a * (1 - a) * b * (1 - b) / D + 1e-12, trial
print("20 random subset pairs: variance bound holds for all")

# extremal-ish case: A = B = copy of A_4 (point stabilizer of 4), a subgroup of index 5
A4 = [index[p] for p in elements if p[4] == 4]
assert len(A4) == 12
check_sets(A4, A4, "A = B = A_4 subgroup")

print("ALL MIXING CHECKS PASSED")
