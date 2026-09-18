"""
Fast version of 02: exact exponential rate of E[Z_n^2] for fibre-balanced
3-colourings of a random n-lift of K_5, versus the two upper bounds.

Exact rate (= Nir-Perez-Gimenez f(A,B) of their (38), maximized over B):
   Phi(A_1..A_5) = sum_v h(A_v) + sum_{e=vv'} lambda(A_v, A_v'),
   lambda(a,b) = -h(a) - h(b) + H(B*(a,b)),
B* = max-entropy coupling of a,b supported on K={(i,j,i',j'): i!=i', j!=j'}.
(lambda(a,b) = lim (1/n) log q_n(a,b) from Stirling on per(A)/n!.)

Writeup's Bregman bound: lambda(a,b) <= (L(a)+L(b))/2, L(a)=sum a log(1/3+a),
so Phi <= 5 * F(U) iff Lemma 1 holds.
NPG's relaxed bound: lambda(a,b) <= (1/2)[log(1-2/k+||a||^2)+log(1-2/k+||b||^2)]
  ... actually their per-edge bound is log z_e <= log(1-2/k+rho(A_v)) symmetrised.
"""
import numpy as np, math, itertools
from scipy.optimize import minimize

k, d = 3, 4
idx = [(i, j) for i in range(k) for j in range(k)]
MASK = np.array([[1.0 if (i != ii and j != jj) else 0.0 for (ii, jj) in idx] for (i, j) in idx])
U = np.full(9, 1/9)

def xlogx(x):
    x = np.asarray(x, float)
    return np.where(x > 1e-300, x*np.log(np.where(x > 1e-300, x, 1.0)), 0.0)
def h(a): return float(-xlogx(a).sum())
def L(a): return float(np.sum(np.where(np.asarray(a) > 0, np.asarray(a)*np.log(1/3+np.asarray(a)), 0.0)))

def lam(a, b, iters=3000, tol=1e-13):
    B = MASK * np.outer(a+1e-16, b+1e-16)
    for t in range(iters):
        r = B.sum(1); r[r == 0] = 1; B *= (a/r)[:, None]
        c = B.sum(0); c[c == 0] = 1; B *= (b/c)[None, :]
        if t % 25 == 0 and max(np.abs(B.sum(1)-a).max(), np.abs(B.sum(0)-b).max()) < tol:
            break
    err = max(np.abs(B.sum(1)-a).max(), np.abs(B.sum(0)-b).max())
    return -h(a)-h(b) + float(-xlogx(B).sum()), err

print("=== sanity at U ===")
lU, e = lam(U, U)
print(f"  lambda(U,U)={lU:.9f}  log(4/9)={math.log(4/9):.9f}  sinkhorn err={e:.1e}")
PhiU = 5*h(U) + 10*lU
print(f"  Phi(U,..,U)={PhiU:.8f}  2*(5log3+10log(2/3))={2*(5*math.log(3)+10*math.log(2/3)):.8f}")
print(f"  Phi/5 = {PhiU/5:.8f}   F_writeup(U)=H+2L = {h(U)+2*L(U):.8f}   2log(4/3)={2*math.log(4/3):.8f}")

def Fw(a): return h(a) + 2*L(a)
def gNPG(a): return h(a) + (d/2)*math.log(1-2/k+float(np.sum(np.asarray(a)**2)))
def Phi5(a): return (5*h(a) + 10*lam(a, a)[0])/5

print("\n=== family a_ii=(1+2t)/9, a_ij=(1-t)/9  (t=0 -> U, t=1 -> identical colourings) ===")
print("     t    exact Phi/5    F (writeup)    g (NPG relaxed)")
for t in [0, .05, .1, .15, .2, .25, .3, .4, .5, .7, 1.0]:
    a = np.array([[(1+2*t)/9 if i == j else (1-t)/9 for j in range(3)] for i in range(3)]).ravel()
    print(f"  {t:5.2f} {Phi5(a):13.8f} {Fw(a):14.8f} {gNPG(a):16.8f}")
print(f"  at U:  {PhiU/5:13.8f} {Fw(U):14.8f} {gNPG(U):16.8f}")

def proj(v):
    M = np.abs(v).reshape(3, 3) + 1e-12
    for _ in range(200):
        M = M/(3*M.sum(1, keepdims=True)); M = M/(3*M.sum(0, keepdims=True))
    return M.ravel()

rng = np.random.default_rng(11)
print("\n=== maximize over rho (all fibres equal), doubly stochastic/3 ===")
for name, fn in [("exact Phi/5", Phi5), ("F  writeup ", Fw), ("g  NPG     ", gNPG)]:
    best, arg = -1e18, None
    for _ in range(60):
        r = minimize(lambda v: -fn(proj(v)), rng.dirichlet(np.ones(9)), method='Nelder-Mead',
                     options=dict(maxiter=3000, maxfev=3000, xatol=1e-9, fatol=1e-11))
        if -r.fun > best: best, arg = -r.fun, proj(r.x)
    ref = fn(U)
    print(f"  {name}: max={best:.8f}  value at U={ref:.8f}  "
          f"{'U IS the max' if best <= ref+1e-7 else '*** U NOT the max ***'}")
    if best > ref+1e-7: print("    maximizer:\n", np.round(arg.reshape(3, 3), 6))

print("\n=== maximize exact Phi over 5 independent fibres (random restarts, Powell) ===")
def negPhi5full(v):
    As = [proj(v[9*i:9*i+9]) for i in range(5)]
    tot = sum(h(a) for a in As)
    for i, j in itertools.combinations(range(5), 2):
        tot += lam(As[i], As[j])[0]
    return -tot
best = -1e18
for s in [np.tile(U, 5)] + [rng.dirichlet(np.ones(9), size=5).ravel() for _ in range(6)]:
    r = minimize(negPhi5full, s, method='Powell', options=dict(maxiter=800, xtol=1e-7, ftol=1e-9))
    best = max(best, -r.fun)
print(f"  max Phi found = {best:.8f}   Phi(U,..,U) = {PhiU:.8f}   "
      f"{'OK: U is the max' if best <= PhiU+1e-5 else '*** EXCEEDS ***'}")

print("\n=== direct test of writeup ineq (10): lambda(a,b) <= (L(a)+L(b))/2 ===")
worst, n_ok = -1e18, 0
for _ in range(3000):
    a = proj(rng.dirichlet(np.ones(9)*rng.uniform(0.2, 3)))
    b = proj(rng.dirichlet(np.ones(9)*rng.uniform(0.2, 3)))
    lv, err = lam(a, b)
    if err > 1e-9: continue
    n_ok += 1
    worst = max(worst, lv - (L(a)+L(b))/2)
print(f"  max of lambda - (L+L)/2 over {n_ok} random pairs: {worst:.3e}  (<=0 means (10) holds)")

print("\n=== direct test of the Bregman step (8): lambda(a,b) <= sum_ab a log(1/3+b) ===")
worst = -1e18
for _ in range(3000):
    a = proj(rng.dirichlet(np.ones(9)*rng.uniform(0.2, 3)))
    b = proj(rng.dirichlet(np.ones(9)*rng.uniform(0.2, 3)))
    lv, err = lam(a, b)
    if err > 1e-9: continue
    rhs = float(np.sum(a*np.log(1/3+b)))
    worst = max(worst, lv - rhs)
print(f"  max of lambda - sum a log(1/3+b): {worst:.3e}  (<=0 means (8) holds)")
