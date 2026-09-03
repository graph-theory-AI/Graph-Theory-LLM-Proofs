"""Numerical sanity checks for the claimed proof of Alon-Klartag Conjecture 2.4
(attack 1610.00239__00).

The writeup's proof is probabilistic/asymptotic (no single finite witness), so we
check every quantitative ingredient empirically:

  A. Lemma 1: w(RK cap B_2) <= C1 * R * sqrt(log(2 + n/R^2)) for K = conv{0,+-v_i}.
     Worst case v_i = e_i in R^n (then RK cap B_2 = {||z||_1<=R} cap B_2 and the
     sup is computable essentially exactly by soft-thresholding).  We report the
     ratio  w_hat / (R sqrt(log(2+n/R^2)))  across R; it should stay bounded by a
     modest constant.

  B. Escape property (Lemma 2 + step 3): for x_i = e_i, G = Gamma/sqrt(t) Gaussian,
     t = ceil(C0 * eps^-2 * log(2+eps^2 n)),   check
        (i)  ||G e_i|| <= 2 for all i,
        (ii) ||G h|| >= 1/4 for many random unit h with rho(h)=||h||_1 <= 1/eps
             (random effectively-sparse directions, plus adversarial h minimizing
             ||G h|| via projected gradient descent on the constraint set).

  C. Full construction (Theorem): random unit x_i, y_j in R^k; p_i = G x_i;
     for each y_j find q_j with ||q_j||<=4 and ||P q_j - T y_j||_inf <= eps
     (least squares + projected subgradient polish);  also check the boxed
     inequality (1):  ||T* z|| <= 4 ||P* z|| + eps ||z||_1  on random and
     adversarial z (minimizing (4||P*z|| + eps||z||_1)/||T*z|| by projected
     gradient descent).

Only numpy is required.
"""
import numpy as np

rng = np.random.default_rng(20260902)


# ---------------------------------------------------------------- A. Lemma 1
def width_l1l2(g, R):
    """sup <g,z> over ||z||_1 <= R, ||z||_2 <= 1  (near-exact via thresholding)."""
    a = np.sort(np.abs(g))[::-1]
    best = 0.0
    # candidate thresholds: 0 and each |g|_(i)
    thetas = np.concatenate([[0.0], a])
    ga = np.abs(g)
    for theta in thetas:
        u = np.maximum(ga - theta, 0.0)
        n1, n2 = u.sum(), np.linalg.norm(u)
        if n2 == 0:
            continue
        s = max(n2, n1 / R)
        best = max(best, float(np.dot(ga, u)) / s)
    return best


def check_lemma1():
    print("=== A. Lemma 1: width of RK cap B_2 (v_i = e_i, n=400) ===")
    n = 400
    for R in [1.0, 2.0, 4.0, 8.0, 14.0, 20.0]:
        vals = [width_l1l2(rng.standard_normal(n), R) for _ in range(60)]
        w = float(np.mean(vals))
        bound = R * np.sqrt(np.log(2 + n / R**2))
        print(f"  R={R:5.1f}  w_hat={w:8.3f}  R*sqrt(log(2+n/R^2))={bound:8.3f}"
              f"  ratio={w/bound:6.3f}")


# ------------------------------------------------- B. escape property
def project_l1l2_sphere(h, R, iters=50):
    """Project (heuristically) onto {||h||_2 = 1, ||h||_1 <= R}: alternate."""
    for _ in range(iters):
        n1 = np.abs(h).sum()
        if n1 > R:
            # soft-threshold to reduce l1 norm to R
            h = soft_to_l1(h, R)
        h = h / np.linalg.norm(h)
        if np.abs(h).sum() <= R + 1e-9:
            break
    return h


def soft_to_l1(v, R):
    a = np.abs(v)
    if a.sum() <= R:
        return v
    # binary search threshold
    lo, hi = 0.0, a.max()
    for _ in range(60):
        mid = (lo + hi) / 2
        if np.maximum(a - mid, 0).sum() > R:
            lo = mid
        else:
            hi = mid
    u = np.maximum(a - hi, 0) * np.sign(v)
    return u


def check_escape():
    print("\n=== B. Escape: x_i=e_i, ||Gh||>=1/4 on {||h||=1, ||h||_1<=1/eps} ===")
    C0 = 8.0
    for (n, eps) in [(400, 0.25), (400, 0.1), (1000, 0.06)]:
        t = int(np.ceil(C0 * np.log(2 + eps**2 * n) / eps**2))
        t = min(t, 4000)
        G = rng.standard_normal((t, n)) / np.sqrt(t)
        colnorms = np.linalg.norm(G, axis=0)
        R = 1.0 / eps
        # random effectively sparse unit vectors
        worst = np.inf
        for _ in range(300):
            s = max(1, int(R**2))
            idx = rng.choice(n, size=min(s, n), replace=False)
            h = np.zeros(n)
            h[idx] = rng.standard_normal(len(idx))
            h = project_l1l2_sphere(h, R)
            worst = min(worst, np.linalg.norm(G @ h))
        # adversarial: minimize ||Gh|| by projected gradient descent
        h = rng.standard_normal(n)
        h = project_l1l2_sphere(h, R)
        lr = 0.05
        for it in range(400):
            grad = G.T @ (G @ h)
            h = h - lr * grad
            h = project_l1l2_sphere(h, R)
        adv = np.linalg.norm(G @ h)
        print(f"  n={n:5d} eps={eps:5.2f} t={t:5d}  max||Ge_i||={colnorms.max():.3f}"
              f"  min||Gh|| rand={worst:.3f} adv={adv:.3f}  (need >=0.25)")


# ------------------------------------------------- C. full construction
def solve_q(P, c, eps, qmax=4.0):
    """Find q, ||q||<=qmax, ||P q - c||_inf <= eps if possible.
    Least squares first, then projected subgradient on max-residual."""
    t = P.shape[1]
    q, *_ = np.linalg.lstsq(P, c, rcond=None)
    if np.linalg.norm(q) > qmax:
        q = q * (qmax / np.linalg.norm(q))
    best = q.copy()
    bestval = np.abs(P @ q - c).max()
    lr0 = 0.5
    for it in range(2000):
        r = P @ q - c
        i = int(np.argmax(np.abs(r)))
        gsub = np.sign(r[i]) * P[i]
        q = q - lr0 / np.sqrt(it + 1) * gsub
        nq = np.linalg.norm(q)
        if nq > qmax:
            q = q * (qmax / nq)
        val = np.abs(P @ q - c).max()
        if val < bestval:
            bestval, best = val, q.copy()
        if bestval <= eps * 0.98:
            break
    return best, bestval


def check_construction():
    print("\n=== C. Full construction: random unit x_i, y_j ===")
    C0 = 8.0
    for (n, m, k, eps) in [(300, 300, 300, 0.2), (600, 200, 100, 0.1),
                           (500, 100, 500, 0.3)]:
        t = int(np.ceil(C0 * np.log(2 + eps**2 * n) / eps**2))
        X = rng.standard_normal((n, k)); X /= np.linalg.norm(X, axis=1, keepdims=True)
        Y = rng.standard_normal((m, k)); Y /= np.linalg.norm(Y, axis=1, keepdims=True)
        # add correlated clusters to X to stress the atomic-norm geometry
        X[: n // 3] = X[0] + 0.05 * rng.standard_normal((n // 3, k))
        X[: n // 3] /= np.linalg.norm(X[: n // 3], axis=1, keepdims=True)
        G = rng.standard_normal((t, k)) / np.sqrt(t)
        P = X @ G.T            # rows are p_i
        pmax = np.linalg.norm(P, axis=1).max()
        qmax_seen, errmax, fails = 0.0, 0.0, 0
        for j in range(m):
            c = X @ Y[j]        # T y_j
            q, val = solve_q(P, c, eps)
            qmax_seen = max(qmax_seen, np.linalg.norm(q))
            errmax = max(errmax, val)
            if val > eps + 1e-9:
                fails += 1
        # inequality (1) on random z
        ratio_min = np.inf
        for _ in range(500):
            z = rng.standard_normal(n) * (rng.random(n) < 0.1)
            if np.abs(z).sum() == 0:
                continue
            lhs = np.linalg.norm(X.T @ z)
            rhs = 4 * np.linalg.norm(P.T @ z) + eps * np.abs(z).sum()
            ratio_min = min(ratio_min, rhs / max(lhs, 1e-12))
        # adversarial z: minimize rhs/lhs by gradient descent
        z = rng.standard_normal(n)
        for it in range(600):
            lhs_v = X.T @ z; lhs = np.linalg.norm(lhs_v)
            rhs_v = P.T @ z; rhs = 4 * np.linalg.norm(rhs_v)
            l1 = np.abs(z).sum()
            f = (rhs + eps * l1) / max(lhs, 1e-12)
            gr = (4 * P @ (rhs_v / max(rhs / 4, 1e-12)) + eps * np.sign(z)) / lhs \
                 - (rhs + eps * l1) / lhs**3 * (X @ lhs_v)
            z = z - 0.1 * gr / max(np.linalg.norm(gr), 1e-12) * np.linalg.norm(z)
            z = z / np.linalg.norm(z)
        lhs = np.linalg.norm(X.T @ z)
        rhs = 4 * np.linalg.norm(P.T @ z) + eps * np.abs(z).sum()
        adv_ratio = rhs / max(lhs, 1e-12)
        print(f"  n={n} m={m} k={k} eps={eps} t={t}: max||p_i||={pmax:.3f} "
              f"max||q_j||={qmax_seen:.3f} max_err={errmax:.4f} "
              f"(eps={eps}) fails={fails}")
        print(f"     ineq(1): min rhs/lhs random z = {ratio_min:.3f}, "
              f"adversarial = {adv_ratio:.3f}  (need >= 1)")


if __name__ == "__main__":
    check_lemma1()
    check_escape()
    check_construction()
