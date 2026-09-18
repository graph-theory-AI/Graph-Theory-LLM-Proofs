"""Fast direct test of the writeup's Bregman step (8) and its symmetrisation (10),
and of Lemma 1 restricted to the exact exponent, by random sampling + a symmetric
grid.  lambda(a,b) = -h(a)-h(b)+H(B*) is the exact rate of (1/n)log q_n(a,b)."""
import numpy as np, math
k = 3
idx = [(i, j) for i in range(k) for j in range(k)]
MASK = np.array([[1.0 if (i != ii and j != jj) else 0.0 for (ii, jj) in idx] for (i, j) in idx])
U = np.full(9, 1/9)
def xlogx(x):
    x = np.asarray(x, float); return np.where(x > 1e-300, x*np.log(np.where(x > 1e-300, x, 1.0)), 0.0)
def h(a): return float(-xlogx(a).sum())
def L(a): a = np.asarray(a); return float(np.sum(np.where(a > 0, a*np.log(1/3+a), 0.0)))
def lam(a, b, iters=4000, tol=1e-13):
    B = MASK*np.outer(a+1e-16, b+1e-16)
    for t in range(iters):
        r = B.sum(1); r[r == 0] = 1; B *= (a/r)[:, None]
        c = B.sum(0); c[c == 0] = 1; B *= (b/c)[None, :]
        if t % 20 == 0 and max(np.abs(B.sum(1)-a).max(), np.abs(B.sum(0)-b).max()) < tol: break
    return -h(a)-h(b)+float(-xlogx(B).sum()), max(np.abs(B.sum(1)-a).max(), np.abs(B.sum(0)-b).max())
def proj(v, it=60):
    M = np.abs(v).reshape(3, 3)+1e-12
    for _ in range(it):
        M = M/(3*M.sum(1, keepdims=True)); M = M/(3*M.sum(0, keepdims=True))
    return M.ravel()
rng = np.random.default_rng(5)
w8 = w10 = -1e18; nok = 0
for _ in range(20000):
    a = proj(rng.dirichlet(np.ones(9)*rng.uniform(0.15, 4)))
    b = proj(rng.dirichlet(np.ones(9)*rng.uniform(0.15, 4)))
    lv, err = lam(a, b)
    if err > 1e-9: continue
    nok += 1
    w8 = max(w8, lv - float(np.sum(a*np.log(1/3+b))))
    w10 = max(w10, lv - (L(a)+L(b))/2)
print(f"pairs tested: {nok}")
print(f"max [ lambda(a,b) - sum_ab a log(1/3+b) ]  = {w8:.3e}   <=0 means (8) holds")
print(f"max [ lambda(a,b) - (L(a)+L(b))/2      ]  = {w10:.3e}   <=0 means (10) holds")
# exact per-fibre exponent Phi/5 = h + 2*lambda(a,a) for equal fibres: max over a
best, arg = -1e18, None
for _ in range(20000):
    a = proj(rng.dirichlet(np.ones(9)*rng.uniform(0.15, 4)))
    lv, err = lam(a, a)
    if err > 1e-9: continue
    v = h(a) + 2*lv
    if v > best: best, arg = v, a
print(f"\nmax over 20000 random rho of exact per-fibre exponent h+2*lambda = {best:.8f}")
print(f"   value at U = {h(U)+2*lam(U,U)[0]:.8f}  (= 2 log(4/3) = {2*math.log(4/3):.8f})")
print("   maximizer:\n", np.round(arg.reshape(3, 3), 5))
