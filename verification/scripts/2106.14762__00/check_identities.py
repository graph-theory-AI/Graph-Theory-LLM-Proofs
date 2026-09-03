"""Numeric verification of the calculus identities in attacks/2106.14762__00/output.md.

Checks (numbering follows the writeup):
  (7)/(8)  total mass of eta = 1
  (12)     r(z) = (1-z)(1 + int_z^1 e^{y-z} dy) = (1-z)e^{1-z}
           expected run length 1 + int_z^1 e^{y-z} dy = e^{1-z}
  (14)     (1-z)e^{y-z} = r(z) e^{y-1}  for z < y
  (17)     H(z) = int_0^z (1-t)e^{1-t} dt = z e^{1-z}
  (20)     interior conditional mass e^{y-1} * y e^{1-y} = y; atom mass 1-y; total 1
  (15)     eta((a,b)x(c,d)) = (int_a^b r) (int_c^d e^{y-1} dy) for a<b<c<d
"""
import numpy as np

def integrate(f, a, b, m=200001):
    t = np.linspace(a, b, m)
    return np.trapezoid(f(t), t)

ok = True
def check(name, lhs, rhs, tol=1e-8):
    global ok
    err = abs(lhs - rhs)
    good = err < tol
    ok = ok and good
    print(f"{name:55s} lhs={lhs:.10f} rhs={rhs:.10f} err={err:.2e} {'OK' if good else 'FAIL'}")

# (12): r(z) and expected run length, at several z
for z in [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
    el = 1 + integrate(lambda y: np.exp(y - z), z, 1)
    check(f"(12) expected run length at z={z}", el, np.exp(1 - z))
    check(f"(12) r(z) at z={z}", (1 - z) * el, (1 - z) * np.exp(1 - z))

# (14): factorization identity at random (z,y) pairs with z<y
rng = np.random.default_rng(0)
for _ in range(5):
    z, y = np.sort(rng.uniform(0, 1, 2))
    check(f"(14) identity at z={z:.3f},y={y:.3f}",
          (1 - z) * np.exp(y - z),
          (1 - z) * np.exp(1 - z) * np.exp(y - 1), tol=1e-12)

# (17): H(z) = z e^{1-z}
for z in [0.1, 0.25, 0.5, 0.75, 1.0]:
    H = integrate(lambda t: (1 - t) * np.exp(1 - t), 0, z)
    check(f"(17) H(z) at z={z}", H, z * np.exp(1 - z))

# (8): total mass of eta = diagonal + off-diagonal = 1
diag = integrate(lambda z: 1 - z, 0, 1)
def offdiag_inner(z):
    return (1 - z) * (np.exp(1 - z) - 1)
off = integrate(offdiag_inner, 0, 1)
check("(8) total mass of eta (diag + offdiag)", diag + off, 1.0, tol=1e-6)
print(f"      diagonal mass = {diag:.6f} (should be 1/2), off-diagonal = {off:.6f}")

# (20): conditional masses at height y
for y in [0.1, 0.4, 0.6, 0.9]:
    check(f"(20) interior mass at y={y}", np.exp(y - 1) * y * np.exp(1 - y), y, tol=1e-12)
    check(f"(20) total conditional mass at y={y}",
          np.exp(y - 1) * y * np.exp(1 - y) + (1 - y), 1.0, tol=1e-12)

# (15): product form of eta on rectangles a<b<c<d
for (a, b, c, d) in [(0.0, 0.2, 0.3, 0.5), (0.1, 0.3, 0.6, 0.95), (0.4, 0.45, 0.5, 0.9)]:
    # lhs: double integral of (1-z)e^{y-z} over (a,b)x(c,d)
    lhs = integrate(lambda z: (1 - z) * (np.exp(d - z) - np.exp(c - z)), a, b)
    rhs = integrate(lambda t: (1 - t) * np.exp(1 - t), a, b) * (np.exp(d - 1) - np.exp(c - 1))
    check(f"(15) rectangle ({a},{b})x({c},{d})", lhs, rhs, tol=1e-6)

# y-marginal of R must be Lebesgue (permuton property): interior + atom = 1 for all y (same as (20))
# x-marginal check: integrate density e^{y-1} over {y: x < y e^{1-y}} plus boundary curve mass
# pushforward of boundary term: for x in (0,1), the atom at x = ye^{1-y} contributes when y solves it.
# Instead check total mass of R from formula (1):
interior_mass = integrate(lambda y: np.exp(y - 1) * y * np.exp(1 - y), 0, 1)  # = int y dy = 1/2
boundary_mass = integrate(lambda y: 1 - y, 0, 1)
check("(1) total mass of R", interior_mass + boundary_mass, 1.0, tol=1e-9)

print("\nALL IDENTITIES OK" if ok else "\nSOME CHECKS FAILED")
