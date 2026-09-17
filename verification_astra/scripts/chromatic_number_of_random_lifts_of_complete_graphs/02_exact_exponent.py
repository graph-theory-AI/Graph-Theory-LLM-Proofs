"""
Exact exponential rate of E[Z_n^2] for fibre-balanced 3-colourings of a random
n-lift of K_5, and comparison with (i) the writeup's Bregman upper bound
F(rho)=H(rho)+2L(rho) and (ii) Nir-Perez-Gimenez's relaxed bound
g(A)=h(A)+(d/2)log(1-2/k+||A||^2)  (their eq. after Prop 5.1).

Exact rate (equals NPG's f(A,B) of their (38) after maximizing over B):
   Phi(A_1..A_5) = sum_v (1-d) h(A_v) + sum_{e=vv'} H(B*_e),
where B*_e is the maximum-entropy coupling of (A_v, A_v') supported on
K = {(i,j,i',j'): i != i', j != j'}.   Derivation: log(per/n!) rate, see report.
At A_v = U (all 1/9): Phi = -15 log 9 + 10 log 36 = 2.87680 = 2*log(EZ_n)/n.
"""
import numpy as np, math, itertools
from scipy.optimize import minimize

k, d = 3, 4
idx = [(i,j) for i in range(k) for j in range(k)]
MASK = np.array([[1.0 if (i!=ii and j!=jj) else 0.0 for (ii,jj) in idx] for (i,j) in idx])
U = np.full(k*k, 1.0/(k*k))

def xlogx(x):
    x = np.asarray(x, float)
    return np.where(x > 1e-300, x*np.log(np.where(x > 1e-300, x, 1.0)), 0.0)
def h(a):  return -xlogx(a).sum()
def L(a):  return float(np.sum(np.where(a > 0, a*np.log(1.0/k + a), 0.0)))

def maxent_coupling(a, b, iters=20000, tol=1e-14):
    """Max-entropy joint distribution on supp(MASK) with margins a (rows), b (cols)."""
    B = MASK * np.outer(np.sqrt(a+1e-300), np.sqrt(b+1e-300))
    for t in range(iters):
        r = B.sum(1); r[r == 0] = 1
        B *= (a/r)[:, None]
        c = B.sum(0); c[c == 0] = 1
        B *= (b/c)[None, :]
        if t % 50 == 0:
            err = np.abs(B.sum(1)-a).max() + np.abs(B.sum(0)-b).max()
            if err < tol: break
    return B, np.abs(B.sum(1)-a).max()+np.abs(B.sum(0)-b).max()

def lam_exact(a, b):
    """exact lim (1/n) log q_n(a,b) = -h(a)-h(b)+H(B*)"""
    B, err = maxent_coupling(a, b)
    return -h(a)-h(b) - xlogx(B).sum().item()*(-1)*0 + (-xlogx(B).sum()), err
# (clean:)
def lam(a, b):
    B, err = maxent_coupling(a, b)
    return -h(a)-h(b) + (-xlogx(B).sum()), err

print("=== sanity: at A=U ===")
lU, e = lam(U, U)
print(f"   h(U)={h(U):.6f} log9={math.log(9):.6f};  H(B*)={lU+2*h(U):.6f} log36={math.log(36):.6f}; err={e:.2e}")
print(f"   lambda(U,U)={lU:.8f}  log(4/9)={math.log(4/9):.8f}")
PhiU = 5*(1-d)*h(U) + 10*(lam(U,U)[0] + 2*h(U))
print(f"   Phi(U..U)={PhiU:.8f}   2*(5log3+10log(2/3))={2*(5*math.log(3)+10*math.log(2/3)):.8f}")

def Phi_equal(a):
    """all five fibres carry the same overlap matrix a (flattened 9-vector)"""
    l, _ = lam(a, a)
    return 5*h(a) + 10*l          # = sum_v h + sum_e lambda
def Fwriteup(a, dd=d):
    return h(a) + (dd/2)*L(a)
def gNPG(a, dd=d):
    return h(a) + (dd/2)*math.log(1 - 2.0/k + float(np.sum(np.asarray(a)**2)))

print("\n=== Phi at U, per fibre ===")
print(f"   Phi_equal(U)/5 = {Phi_equal(U)/5:.8f}   F_writeup(U) = {Fwriteup(U):.8f}   g_NPG(U) = {gNPG(U):.8f}")

print("\n=== 1-parameter family a_ii=(1+2t)/9, a_ij=(1-t)/9 ===")
print("      t      Phi/5(exact)   F(writeup)     g(NPG relaxed)")
for t in [0,0.05,0.1,0.15,0.2,0.25,0.3,0.4,0.5,0.7,1.0]:
    A = np.array([[(1+2*t)/9 if i==j else (1-t)/9 for j in range(k)] for i in range(k)]).ravel()
    print(f"   {t:5.2f}  {Phi_equal(A)/5:12.8f} {Fwriteup(A):14.8f} {gNPG(A):14.8f}")

print("\n=== global search: maximize exact Phi over 5 independent doubly-stochastic/k matrices ===")
def proj(v):
    M = np.abs(v).reshape(k,k) + 1e-12
    for _ in range(300):
        M = M/(k*M.sum(1, keepdims=True)); M = M/(k*M.sum(0, keepdims=True))
    return M.ravel()
def negPhi5(v):
    As = [proj(v[9*i:9*i+9]) for i in range(5)]
    tot = sum(h(a) for a in As)
    for i, j in itertools.combinations(range(5), 2):
        tot += lam(As[i], As[j])[0]
    return -tot
rng = np.random.default_rng(7)
best, arg = -1e18, None
starts = [np.tile(U, 5)]
for _ in range(25):
    starts.append(rng.dirichlet(np.ones(9), size=5).ravel())
for s in starts:
    r = minimize(negPhi5, s, method='Powell', options=dict(maxiter=4000, xtol=1e-9, ftol=1e-11))
    if -r.fun > best: best, arg = -r.fun, r.x.copy()
print(f"   max Phi found = {best:.8f}   Phi(U,...,U) = {PhiU:.8f}   "
      f"{'OK: U is the max' if best <= PhiU+1e-6 else '*** EXCEEDS ***'}")

print("\n=== global search: equal-fibre exact Phi/5, and the two upper bounds ===")
for name, fn in [("exact Phi/5", lambda a: Phi_equal(a)/5),
                 ("F writeup  ", lambda a: Fwriteup(a)),
                 ("g NPG      ", lambda a: gNPG(a))]:
    best, arg = -1e18, None
    for _ in range(200):
        s = rng.dirichlet(np.ones(9))
        r = minimize(lambda v: -fn(proj(v)), s, method='Nelder-Mead',
                     options=dict(maxiter=6000, maxfev=6000, xatol=1e-10, fatol=1e-12))
        if -r.fun > best: best, arg = -r.fun, proj(r.x)
    ref = fn(U)
    print(f"   {name}: max={best:.8f} at U-value={ref:.8f}  "
          f"{'U is max' if best <= ref+1e-7 else '*** U NOT MAX ***'}")
    if best > ref + 1e-7:
        print("     maximizer:\n", np.round(arg.reshape(3,3), 6))

print("\n=== direct test of the writeup's key inequality (10): lambda(a,b) <= (L(a)+L(b))/2 ===")
worst = -1e18
for _ in range(4000):
    a = proj(rng.dirichlet(np.ones(9))); b = proj(rng.dirichlet(np.ones(9)))
    lv, err = lam(a, b)
    if err > 1e-8: continue
    slack = (L(a)+L(b))/2 - lv
    if -slack > worst: worst = -slack; wa, wb = a, b
print(f"   max violation of (10) over 4000 random pairs: {worst:.3e} (negative = inequality holds)")
