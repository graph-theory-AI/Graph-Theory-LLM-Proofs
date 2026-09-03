"""Referee verification for 1909.11578__02.

Writeup claims: F_n = { S subset Z_n : ell(S) > ell(S^c) } (ell = longest
cyclic run) is increasing, intersecting, rotation-invariant; the lift
A_n = { x in [k]^n : S_1(x) in F_n } is symmetric intersecting with
|A_n|/k^n = mu_{1/k}(F_n) >= (1/(2k)) n^{-gamma_k}, i.e. only polynomially
small (so log_k|A_n| = n - O_k(log n), refuting log_k|A| <= n - c n^delta).

Checks:
 1. n <= 14 (exhaustive, bit tricks): F_n is increasing, complement-free,
    rotation-invariant, and pairwise intersecting (direct pair check n <= 12).
 2. k=3, n <= 7 (exhaustive over 3^n vectors): A_n is intersecting as a
    vector family; |A_n| = 3^n * mu_{1/3}(F_n) computed independently.
 3. Exact mu_{1/3}(F_n) for even n up to 24 (numpy-vectorized) -- decay trend
    consistent with a polynomial n^-gamma', not stretched-exponential.
 4. Monte Carlo at large n (k=3): conditional claim
    P(S notin F_n | I subset S) small, with m = ceil(3 log n / lambda).
"""
import itertools, math, random
import numpy as np

# ---------- bit-twiddling longest cyclic run ----------

def maxrun1(m, n):
    """longest cyclic run of 1-bits of m (an n-bit mask)."""
    full = (1 << n) - 1
    if m == full:
        return n
    r = 0
    while m:
        m &= ((m << 1) | (m >> (n - 1))) & full  # AND with cyclic shift
        r += 1
    return r

def ell_pair(m, n):
    full = (1 << n) - 1
    return maxrun1(m, n), maxrun1(full ^ m, n)

def in_F(m, n):
    a, b = ell_pair(m, n)
    return a > b

# ---------- check 1 ----------

def check_family_properties(n, pairwise_limit=12):
    full = (1 << n) - 1
    F = [m for m in range(1 << n) if in_F(m, n)]
    Fset = set(F)
    for m in F:
        # increasing
        for i in range(n):
            if not (m >> i) & 1:
                assert (m | (1 << i)) in Fset, (n, m, i, "not increasing")
        # complement-free
        assert (full ^ m) not in Fset, (n, m, "complement in F")
        # rotation invariance
        r = ((m << 1) | (m >> (n - 1))) & full
        assert r in Fset, (n, m, "not rotation invariant")
    if n <= pairwise_limit:
        for a, b in itertools.combinations(F, 2):
            assert a & b != 0, (n, a, b, "disjoint pair in F")
        pw = "pairwise-checked"
    else:
        pw = "pairwise implied (increasing+complement-free)"
    return len(F), pw

# ---------- check 3: exact mu via numpy ----------

def mu_exact_np(n, p):
    N = 1 << n
    masks = np.arange(N, dtype=np.uint64)
    full = np.uint64(N - 1)
    one = np.uint64(1)
    sh = np.uint64(n - 1)

    def maxrun_vec(mm):
        mm = mm.copy()
        r = np.zeros(N, dtype=np.int16)
        alive = mm != 0
        cnt = 0
        while alive.any() and cnt <= n:
            r[alive] += 1
            mm[alive] &= ((mm[alive] << one) | (mm[alive] >> sh)) & full
            alive = mm != 0
            cnt += 1
        return r

    r1 = maxrun_vec(masks)
    r1[N - 1] = n  # all-ones special case (loop would run n times anyway; force)
    r0 = maxrun_vec(masks ^ full)
    r0[0] = n
    inF = r1 > r0
    pop = np.zeros(N, dtype=np.int16)
    m = masks.copy()
    for i in range(n):
        pop += ((m >> np.uint64(i)) & one).astype(np.int16)
    w = pop[inF].astype(np.float64)
    return float(np.sum(np.exp(w * math.log(p) + (n - w) * math.log(1 - p)))), int(inF.sum())

# ---------- check 2: lifted vector family ----------

def check_lift(n, k):
    A = []
    for x in itertools.product(range(1, k + 1), repeat=n):
        m = 0
        for i, v in enumerate(x):
            if v == 1:
                m |= 1 << i
        if in_F(m, n):
            A.append(x)
    for x, y in itertools.combinations(A, 2):
        assert any(xi == yi for xi, yi in zip(x, y)), (x, y, "non-agreeing pair in A_n")
    mu, _ = mu_exact_np(n, 1.0 / k)
    assert abs(len(A) - mu * k ** n) < 1e-6 * k ** n, (len(A), mu * k ** n)
    return len(A), mu

# ---------- check 4: Monte Carlo at large n ----------

def montecarlo_conditional(n, k, trials, seed=0):
    rng = np.random.default_rng(seed)
    p = 1.0 / k
    lam = -math.log(1 - p)
    m = math.ceil(3 * math.log(n) / lam)
    assert m < n, (m, n)
    bad = 0
    for _ in range(trials):
        bits = np.empty(n, dtype=np.int8)
        bits[:m] = 1
        bits[m:] = (rng.random(n - m) < p).astype(np.int8)
        # longest cyclic run of zeros
        z = np.flatnonzero(bits == 0)
        if z.size == 0:
            zeros = 0
        else:
            gaps = np.diff(z)
            # runs of consecutive zero-positions
            brk = np.flatnonzero(gaps > 1)
            starts = np.concatenate(([0], brk + 1))
            ends = np.concatenate((brk, [z.size - 1]))
            runlens = ends - starts + 1
            zeros = int(runlens.max())
            # cyclic wrap: bits[0] can't be 0 (forced 1), so no wrap of zeros
        # ell(S) >= m by construction; S in F_n iff zeros < ell(S); the writeup
        # only needs zeros <= m-1  =>  in F. Count failures of zeros < m.
        if zeros >= m:
            bad += 1
    return m, bad, trials

if __name__ == "__main__":
    print("=== Check 1: family properties of F_n ===")
    for n in range(3, 15):
        sz, pw = check_family_properties(n)
        print(f"  n={n:2d}: |F_n|={sz:6d}  increasing/complement-free/rotation-inv OK; intersecting: {pw}")

    print("=== Check 2: lifted vector family A_n, k=3 ===")
    for n in range(4, 8):
        sz, mu = check_lift(n, 3)
        print(f"  n={n}: |A_n|={sz:5d} = 3^n * mu_(1/3)(F_n) (mu={mu:.6f}); pairwise intersecting OK")

    print("=== Check 3: exact mu_(1/3)(F_n) decay trend ===")
    prev = None
    for n in range(8, 25, 2):
        mu, cnt = mu_exact_np(n, 1.0 / 3.0)
        note = ""
        if prev:
            expo = math.log(prev / mu) / math.log(n / (n - 2))
            note = f"  local exponent: mu ~ n^-{expo:.2f}"
        print(f"  n={n:2d}: mu={mu:.6e} (|F_n|={cnt}){note}")
        prev = mu
    print("  (polynomial decay expected, exponent -> ~ log(3)/log(3/2) - 1 + o(1);")
    print("   stretched-exponential k^{-c n^delta} decay would show exploding exponent)")

    print("=== Check 4: Monte Carlo conditional bound, k=3 ===")
    for n, trials in ((1000, 20000), (10000, 20000), (100000, 5000)):
        m, bad, tr = montecarlo_conditional(n, 3, trials, seed=n)
        print(f"  n={n:6d}: m={m:3d}, P(S notin F | I subset S) est. {bad}/{tr}"
              f"  (claimed <= n^-2 = {n**-2:.0e})")
