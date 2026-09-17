"""
Checks of Sections 3-6 of the writeup:
 * eigenvalues of P_0 = (J_3-I_3)/2 and P_1 = P_0 (x) P_0, a_n prefactor 4/3,
 * prefactor (16/15)^2 in (21) and the matrix M = (19 I_5 - 4A)/15, its spectrum,
 * R = (16/15)^20 det(M)^{-2} = 25 (16/15)^20 (15/23)^8,
 * non-backtracking matrix B of K_5, mu_l = tr(B^l)/(2l), delta_l = 2(-1/2)^l,
 * sum_{l>=3} mu_l delta_l^2  ==  log R   (the small-subgraph-conditioning match),
 * Ihara-Bass det(I-uB) = (1-u^2)^5 det(I-uA+3u^2 I),
 * E[Z_n] exactly for small n against Theta(n^{-5}) (4/3)^{5n}.
"""
import numpy as np, math, itertools
from math import comb, factorial, log

print("=== spectra ===")
A0 = np.ones((3, 3)) - np.eye(3)
P0 = A0/2
print("  eig(P0) =", np.round(np.sort(np.linalg.eigvals(P0).real), 6))
P1 = np.kron(P0, P0)
print("  eig(P1) =", np.round(np.sort(np.linalg.eigvals(P1).real), 6))
# det on 1-perp of I-P0^2  -> a_n prefactor
ev0 = np.sort(np.linalg.eigvals(P0).real)[:-1]
print("  det_{1perp}(I-P0^2)^(-1/2) =", np.prod(1-ev0**2)**-0.5, " (writeup: 4/3 =", 4/3, ")")
ev1 = np.sort(np.linalg.eigvals(P1).real)[:-1]
pref = (9/16)*np.prod(1-ev1**2)**-0.5
print("  (9/16)*det_{1perp}(I-P1^2)^(-1/2) =", pref, " (writeup (16/15)^2 =", (16/15)**2, ")")

print("\n=== M and R ===")
A = np.ones((5, 5)) - np.eye(5)
M = (19*np.eye(5) - 4*A)/15
print("  eig(M) =", np.round(np.sort(np.linalg.eigvals(M).real), 8), " (writeup 1/5 once, 23/15 four times)")
detM = np.linalg.det(M)
R = (16/15)**20 * detM**-2
print("  det M =", detM, " = (1/5)(23/15)^4 =", (1/5)*(23/15)**4)
print("  R = (16/15)^20 det(M)^-2 =", R, " = 25 (16/15)^20 (15/23)^8 =", 25*(16/15)**20*(15/23)**8)
print("  log R =", math.log(R))

print("\n=== non-backtracking matrix of K_5, cycle means ===")
V = range(5)
DE = [(u, v) for u in V for v in V if u != v]
n_de = len(DE)
B = np.zeros((n_de, n_de))
for i, (u, v) in enumerate(DE):
    for j, (x, y) in enumerate(DE):
        if v == x and y != u:
            B[i, j] = 1
print("  |directed edges| =", n_de, " row sums:", set(B.sum(1)))
Bl = np.eye(n_de)
mus, S = {}, 0.0
for l in range(1, 61):
    Bl = Bl @ B
    tr = np.trace(Bl)
    mu = tr/(2*l)
    mus[l] = mu
    if l >= 3:
        S += mu * (2*(-0.5)**l)**2
print("  tr(B^1..B^8) =", [round(float(np.trace(np.linalg.matrix_power(B, l))), 3) for l in range(1, 9)])
print("  mu_3, mu_4, mu_5, mu_6 =", [round(mus[l], 4) for l in (3, 4, 5, 6)],
      " (expected: 10 triangles, 15 four-cycles in K_5)")
print("  sum_{l>=3} mu_l delta_l^2 =", S, "   log R =", math.log(R),
      "   difference =", S - math.log(R))
print("  -2 log det(I - B/4) =", -2*math.log(np.linalg.det(np.eye(n_de)-B/4)))

print("\n=== Ihara-Bass check det(I-uB) = (1-u^2)^5 det(I-uA+3u^2 I) ===")
for u in [0.1, 0.25, 0.3]:
    lhs = np.linalg.det(np.eye(n_de) - u*B)
    rhs = (1-u**2)**5 * np.linalg.det(np.eye(5) - u*A + 3*u**2*np.eye(5))
    print(f"   u={u}: lhs={lhs:.10f} rhs={rhs:.10f}")
print("  at u=1/4:  I-A/4+3/16 I  vs (15/16)M  max|diff| =",
      np.abs((np.eye(5)-A/4+3/16*np.eye(5)) - (15/16)*M).max())

print("\n=== exact E Z_n (fibre-balanced 3-colourings) for n divisible by 3 ===")
def a_exact(n):
    """P[uniform bijection between two 3-coloured fibres (n/3 each) is rainbow-proper]
       = per(block 0-1 matrix)/n!  via inclusion-exclusion over forbidden same-colour pairs."""
    m = n//3
    # permanent of the 0-1 matrix with 3 forbidden m x m diagonal blocks:
    # per = sum_{j1,j2,j3} prod (-1)^{ji} C(m,ji)^2 ji! * (n - sum ji)!
    tot = 0
    for j1 in range(m+1):
        for j2 in range(m+1):
            for j3 in range(m+1):
                s = j1+j2+j3
                tot += (-1)**s * comb(m, j1)**2*factorial(j1) * comb(m, j2)**2*factorial(j2) \
                       * comb(m, j3)**2*factorial(j3) * factorial(n-s)
    return tot/factorial(n)
for n in [3, 6, 9, 12, 15, 18, 24, 30]:
    a = a_exact(n)
    approx = (4/3)*(2/3)**n
    M_n = factorial(n)//(factorial(n//3)**3)
    EZ = M_n**5 * a**10
    print(f"   n={n:3d}: a_n={a:.10e}  (4/3)(2/3)^n={approx:.10e}  ratio={a/approx:.6f}"
          f"   E Z_n={EZ:.6e}   n^-5(4/3)^(5n)={(n**-5.0)*(4/3)**(5*n):.6e}")
