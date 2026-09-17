"""Brute-force checks for 2604.09449__03.

(A) Lemma 4  : exists matching R with ||h(R)-(h(P)+h(Q))/2|| <= 3 L d
(B) Prop 6   : exists matching M with ||h(M)-(1/r)h(K_rr)|| <= 3 L d B_d
(C) Thm 1(1) : exists Ham cycle H of K_{n,n} with ||h(H)-(2/n)h(G)|| <= 6 L d B_d
(D) Thm 1(2) : exists Ham cycle H of K_N     with ||h(H)-(2/(N-1))h(G)|| <= 6LdB_d+8Ld+2L
(E) structural: the writeup's auxiliary construction really yields Hamilton cycles of K_N
(F) the sibling counterexample (f_h = k for every matching) vs Prop 6's bound
"""
import itertools, math, random
import numpy as np

def B(d): return math.ceil(math.log2(d)) + 2 if d >= 2 else 2

def l1(v): return float(np.abs(v).sum())

def rand_labels(m, d, rng, L=1.0):
    # random vectors with l1 norm exactly L (adversarial-ish: signed)
    X = rng.standard_normal((m, d))
    X = X / np.abs(X).sum(axis=1, keepdims=True) * L
    return X

def perms(r): return list(itertools.permutations(range(r)))

# ---------- (A) and (B) ----------
def check_AB(r, d, trials, rng, L=1.0):
    P = perms(r)
    worstA = 0.0; worstB = 0.0
    for _ in range(trials):
        H = rand_labels(r*r, d, rng, L).reshape(r, r, d)   # H[u][v]
        sums = np.array([H[np.arange(r), p].sum(axis=0) for p in P])  # label sum per matching
        mean = H.reshape(-1, d).sum(axis=0) / r
        # (B)
        best = min(l1(s - mean) for s in sums)
        worstB = max(worstB, best / (3*L*d*B(d)))
        # (A) : sample pairs
        for _ in range(12):
            i = rng.integers(len(P)); j = rng.integers(len(P))
            mid = (sums[i] + sums[j]) / 2
            bestm = min(l1(s - mid) for s in sums)
            worstA = max(worstA, bestm / (3*L*d))
    return worstA, worstB

# ---------- (C) Hamilton cycles of K_{n,n} ----------
def ham_cycles_bip(n):
    # cycles a_1 b_{p(1)} a_2 b_{p(2)} ... ; enumerate all permutations (redundant but fine)
    for p in itertools.permutations(range(n)):
        yield p

def check_C(n, d, trials, rng, L=1.0):
    worst = 0.0
    for _ in range(trials):
        H = rand_labels(n*n, d, rng, L).reshape(n, n, d)
        tot = H.reshape(-1, d).sum(axis=0)
        target = 2.0/n * tot
        best = None
        for p in ham_cycles_bip(n):
            s = np.zeros(d)
            for i in range(n):
                s += H[i][p[i]] + H[(i+1) % n][p[i]]
            v = l1(s - target)
            best = v if best is None else min(best, v)
        worst = max(worst, best / (6*L*d*B(d)))
    return worst

# ---------- (D)+(E) Hamilton cycles of K_N ----------
def ham_cycles(N):
    for p in itertools.permutations(range(1, N)):
        c = (0,) + p
        if N > 2 and c[1] > c[-1]:      # canonical orientation
            continue
        yield c

def check_D(N, d, trials, rng, L=1.0):
    E = {}
    worst = 0.0
    cycles = list(ham_cycles(N))
    for _ in range(trials):
        lab = {}
        vecs = rand_labels(N*(N-1)//2, d, rng, L)
        for idx, e in enumerate(itertools.combinations(range(N), 2)):
            lab[e] = vecs[idx]
        S = sum(lab.values())
        target = 2.0/(N-1) * S
        best = None
        for c in cycles:
            s = np.zeros(d)
            for i in range(N):
                u, v = c[i], c[(i+1) % N]
                s += lab[(min(u, v), max(u, v))]
            val = l1(s - target)
            best = val if best is None else min(best, val)
        bound = 6*L*d*B(d) + 8*L*d + 2*L
        worst = max(worst, best/bound)
    return worst

def check_E(N):
    """The writeup's construction: A of size a=ceil(N/2) cyclically ordered, B*=B(+dummy),
    a perfect matching gaps->B* yields a Hamilton cycle of K_N."""
    a = (N+1)//2; b = N//2
    A = list(range(a)); Bs = list(range(a, N))
    dummy = None
    slots = Bs[:]
    if N % 2 == 1:
        dummy = 'star'; slots = Bs + [dummy]
    assert len(slots) == a
    ok = True
    for p in itertools.permutations(range(a)):
        # gap i gets slots[p[i]]
        cyc = []
        for i in range(a):
            cyc.append(A[i])
            s = slots[p[i]]
            if s != 'star':
                cyc.append(s)
        if sorted(cyc) != sorted(range(N)):
            ok = False; break
        if len(set(cyc)) != N:
            ok = False; break
    return ok

# ---------- (F) adversarial construction with f_h = k for every matching ----------
def check_F(k):
    r = k
    s = [1 if i % 2 == 0 else -1 for i in range(k)]
    H = np.zeros((r, r, k))
    for i in range(r):
        for j in range(r):
            H[i][j][i] = s[j]
    tot = H.reshape(-1, k).sum(axis=0)
    mean = tot / r
    vals = set()
    for p in itertools.permutations(range(r)):
        sm = H[np.arange(r), p].sum(axis=0)
        vals.add(round(l1(sm - mean), 9))
    return vals, 3*1*k*B(k)

if __name__ == "__main__":
    rng = np.random.default_rng(20260917)
    print("== (A) Lemma 4 / (B) Prop 6 : max ratio achieved/bound (must be <= 1) ==")
    for r, d in [(5,2),(5,3),(6,2),(6,3),(6,4),(7,3)]:
        a, bb = check_AB(r, d, 60, rng)
        print(f"  r={r} d={d}: LemmaA ratio {a:.3f}   Prop6 ratio {bb:.3f}")
    print("== (C) Theorem 1(1), K_{n,n} ==")
    for n, d in [(4,2),(5,2),(5,3),(6,3)]:
        print(f"  n={n} d={d}: ratio {check_C(n,d,40,rng):.3f}")
    print("== (D) Theorem 1(2), K_N ==")
    for N, d in [(5,2),(6,2),(6,3),(7,3)]:
        print(f"  N={N} d={d}: ratio {check_D(N,d,25,rng):.3f}")
    print("== (E) construction yields Hamilton cycles ==")
    for N in range(3, 11):
        print(f"  N={N}: {check_E(N)}")
    print("== (F) adversarial f_h=k instance vs Prop 6 bound 3k B_k ==")
    for k in [2,4,6,8]:
        vals, bd = check_F(k)
        print(f"  k={k}: attained values {sorted(vals)}  bound {bd}  ok {max(vals)<=bd}")
