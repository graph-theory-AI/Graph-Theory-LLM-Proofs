"""
Check Lemma 1 of the writeup:
   F(rho) = H(rho) + 2 L(rho) <= F(U) = 2 log(4/3),
for 3x3 nonnegative rho of total mass 1 with row sums 1/3,
H(rho) = -sum rho log rho,  L(rho) = sum rho log(1/3 + rho).

Writeup's reduction: F(rho) = -log 3 + (1/3) sum_{a,b} g(3 rho_ab),
   g(x) = 2x log(1+x) - x log x,
and the row inequality (5):  g(x1)+g(x2)+g(x3) <= 3g(1/3) when sum x_i = 1.

General d: g_d(x) = (d/2) x log(1+x) - x log x.
"""
import numpy as np, math
from scipy.optimize import minimize

def xlogx(x):
    x = np.asarray(x, float)
    return np.where(x > 0, x*np.log(np.where(x > 0, x, 1.0)), 0.0)

def g(x, d=4.0):
    x = np.clip(np.asarray(x, float), 0.0, None)
    return (d/2)*x*np.log1p(x) - xlogx(x)

print("=== (a) g'' formula check:  g''(x) = (x^2+2x-1)/(x(1+x)^2) for d=4 ===", flush=True)
h = 1e-5
for x0 in [0.1, 0.2, 1/3, math.sqrt(2)-1, 0.6, 0.9]:
    num = (g(x0+h)-2*g(x0)+g(x0-h))/h**2
    print(f"   x={x0:.6f} numeric g''={float(num):+.7f}  formula={(x0**2+2*x0-1)/(x0*(1+x0)**2):+.7f}")
print("   sign change at sqrt(2)-1 =", math.sqrt(2)-1,
      "; 3*g''(1/3) =", 3*((1/3)**2+2/3-1)/((1/3)*(4/3)**2), "(writeup: Hessian -9/8)")

print("\n=== (b) phi''(x) numerator N(x)=x^4-10x^3-32x^2+34x-9 on [1/3,1) ===", flush=True)
xs = np.linspace(1/3, 0.9999, 40001)
N = xs**4 - 10*xs**3 - 32*xs**2 + 34*xs - 9
print("   max N on [1/3,1) =", N.max(), "(writeup claims N<0)")
phi = lambda x, d=4.0: g(x, d) + 2*g((1-x)/2, d)
e = 1e-4
d2 = (phi(xs[100:-100]+e)-2*phi(xs[100:-100])+phi(xs[100:-100]-e))/e**2
print("   max phi'' numerically on [1/3,1):", d2.max())
print("   phi(1/3) =", float(phi(1/3)), "  max_{x in [1/3,1)} phi =", float(np.max(phi(xs))))

print("\n=== (c) row inequality: max of g_d(x1)+g_d(x2)+g_d(x3), sum=1 ===", flush=True)
NG = 1500
for d in [3.0, 4.0, 4.5, 4.571, 4.6, 5.0, 6.0]:
    best, arg = -1e18, None
    for a in range(NG+1):
        rem = 1 - a/NG
        b = np.arange(0, NG+1-a)/NG
        vals = g(a/NG, d) + g(b, d) + g(rem-b, d)
        j = int(np.argmax(vals))
        if vals[j] > best: best, arg = float(vals[j]), (a/NG, float(b[j]), float(rem-b[j]))
    f = lambda t: -float(g(t[0], d)+g(t[1], d)+g(max(1-t[0]-t[1], 0.0), d))
    r = minimize(f, [arg[0], arg[1]], method='Nelder-Mead',
                 options=dict(xatol=1e-13, fatol=1e-15, maxiter=5000))
    if -r.fun > best and min(r.x[0], r.x[1], 1-r.x.sum()) >= -1e-12:
        best, arg = -r.fun, (r.x[0], r.x[1], 1-r.x.sum())
    unif = float(3*g(1/3, d))
    flag = "uniform IS the max" if best <= unif + 1e-9 else "*** UNIFORM NOT MAX ***"
    print(f"   d={d:5.3f}: max={best:.10f} at {tuple(round(v,6) for v in arg)}  3g(1/3)={unif:.10f}  {flag}")
print("   (local criterion g_d''(1/3) < 0  <=>  d < 96/21 =", 96/21, ")")

print("\n=== (d) direct max of F_d over 3x3 rho, row sums 1/3 / row+col sums 1/3 ===", flush=True)
def F(rho, d=4.0):
    rho = np.asarray(rho, float).reshape(3, 3)
    return float(-xlogx(rho).sum() + (d/2)*np.sum(np.where(rho > 0, rho*np.log(1/3+rho), 0.0)))

def project_rows(v):
    M = np.abs(v).reshape(3, 3) + 1e-14
    return M/(3*M.sum(axis=1, keepdims=True))

def project_both(v):
    M = np.abs(v).reshape(3, 3) + 1e-14
    for _ in range(400):
        M = M/(3*M.sum(axis=1, keepdims=True))
        M = M/(3*M.sum(axis=0, keepdims=True))
    return M

rng = np.random.default_rng(0)
for d in [4.0, 5.0]:
    for name, proj in [("rows only", project_rows), ("rows+cols", project_both)]:
        best, argb = -1e18, None
        for _ in range(150):
            v0 = rng.dirichlet(np.ones(9))
            r = minimize(lambda v: -F(proj(v), d), v0, method='Nelder-Mead',
                         options=dict(maxiter=4000, maxfev=4000, xatol=1e-10, fatol=1e-12))
            if -r.fun > best: best, argb = -r.fun, proj(r.x)
        FU = F(np.full((3, 3), 1/9), d)
        flag = "OK (U is max)" if best <= FU + 1e-8 else "*** EXCEEDS F(U) ***"
        print(f"   d={d}, {name}: max F={best:.10f}  F(U)={FU:.10f}  {flag}", flush=True)
        if best > FU + 1e-8: print(np.round(argb, 6))
print("   2log(4/3) =", 2*math.log(4/3))
