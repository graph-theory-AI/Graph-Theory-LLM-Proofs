#!/usr/bin/env python3
"""Verify all arithmetic/algebraic claims in attacks/2009.03418__00/output.md."""
from fractions import Fraction as F

def H(n):
    return F(1, 4) * (n // 2) * ((n - 1) // 2) * ((n - 2) // 2) * ((n - 3) // 2)

ok = True
def check(label, cond):
    global ok
    print(f'{label}: {"OK" if cond else "FAIL"}')
    ok &= cond

# --- Section 1: Euler-type bound cr(G) >= m - (3n-6) for M_{7,t} (m = 21-t)
for t in (1, 2, 3):
    m = 21 - t
    lb = m - (3 * 7 - 6)
    check(f'Euler lower bound M_(7,{t}) >= {6 - t}', lb == 6 - t)

# --- Section 2 lower bound for M_{7,1}: 3c = sum c_v >= 2*cr(K6) + 5*cr(K6-e)
crK6_lb = 15 - (3 * 6 - 6)     # = 3 (Euler bound; also the true value)
crK6e_lb = 14 - (3 * 6 - 6)    # = 2 (Euler bound; also the true value)
check('cr(K6) >= 3 via Euler bound', crK6_lb == 3)
check('cr(K6-e) >= 2 via Euler bound', crK6e_lb == 2)
S = 2 * crK6_lb + 5 * crK6e_lb
check('sum c_v >= 16', S == 16)
import math
check('c >= ceil(16/3) = 6', math.ceil(F(16, 3)) == 6)
# each crossing survives 7-4 = 3 vertex deletions
check('crossing survives 3 of 7 deletions', 7 - 4 == 3)

# --- Section 3: formula values at n = 7
check('H(7) = 9', H(7) == 9)
k7 = 7 // 2
check('k = floor(7/2) = 3', k7 == 3)
for t in (1, 2, 3):
    val = H(7) - F(1, 2) * t * (k7 - 1) * (k7 - 2)
    check(f'catalog formula at (n=7,t={t}) = {9 - t}', val == 9 - t)
print('conjectured (odd-n reading) vs proved: t=1: 8 vs 6, t=2: 7 vs 4, t=3: 6 vs 3')

# sanity: the intended even-n conjecture at small even n
check('n=6,t=3 (octahedron, planar): formula = 0',
      H(6) - F(1, 2) * 3 * 2 * 1 == 0)
check('n=6,t=1 (K6-e): formula = 2 = known cr', H(6) - F(1, 2) * 1 * 2 * 1 == 2)
check('n=6,t=2: formula = 1 (>= Euler bound 13-12=1)',
      H(6) - F(1, 2) * 2 * 2 * 1 == 1)
# the catalog's floor(n/2) reading already fails trivially at n=5:
check('n=5,t=1 (K5-e, PLANAR): floor-reading formula = 1 (absurd)',
      H(5) - F(1, 2) * 1 * (2 - 1) * (2 - 2) == 1)

# --- Section 4: polynomial identities in k. All expressions below are
# polynomials in k of degree <= 4, so exact agreement at the 48 integer
# points k = 3..50 proves the identities.
ids_ok = [True] * 4
for kk in range(3, 51):
    K = F(kk)
    H2k = H(2 * kk)
    H2k1 = H(2 * kk - 1)
    # closed forms of H at even/odd arguments
    ids_ok[0] &= (H2k == F(1, 4) * K * (K - 1) ** 2 * (K - 2)
                  and H2k1 == F(1, 4) * (K - 1) ** 2 * (K - 2) ** 2)
    Ck = H2k - F(1, 2) * K * (K - 1) * (K - 2)
    ids_ok[1] &= Ck == F(1, 4) * K * (K - 1) * (K - 2) * (K - 3)
    Ak = F(2 * kk - 4, 2 * kk) * Ck
    ids_ok[2] &= Ak == F(1, 4) * (K - 1) * (K - 2) ** 2 * (K - 3)
    # conjectured value for M_(2k-1,k-1): n=2k-1, k'=floor(n/2)=k-1, t=k-1
    Qk = H2k1 - F(1, 2) * (K - 1) * (K - 2) * (K - 3)
    diff = Qk - Ak
    ids_ok[3] &= diff == F(1, 2) * (K - 1) * (K - 2) and diff > 0
check('H(2k), H(2k-1) closed forms (k=3..50)', ids_ok[0])
check('C_k = k(k-1)(k-2)(k-3)/4 (k=3..50)', ids_ok[1])
check('A_k = (k-1)(k-2)^2(k-3)/4 (k=3..50)', ids_ok[2])
check('Q_k - A_k = (k-1)(k-2)/2 > 0 (k=3..50)', ids_ok[3])
# deleting a vertex of M_(2k,k) leaves M_(2k-1,k-1): edge/count sanity
for kk in range(3, 8):
    n = 2 * kk
    m_before = n * (n - 1) // 2 - kk
    n2 = n - 1
    m_after = n2 * (n2 - 1) // 2 - (kk - 1)
    # removing a vertex of degree n-2 (its partner edge absent)
    check(f'M_(2k,k) minus vertex = M_(2k-1,k-1) edge count, k={kk}',
          m_before - (n - 2) == m_after)

print()
print('ALL ARITHMETIC CHECKS PASSED' if ok else 'SOME ARITHMETIC CHECK FAILED')
