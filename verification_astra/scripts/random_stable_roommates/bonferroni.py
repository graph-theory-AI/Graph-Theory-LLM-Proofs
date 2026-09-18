"""Check the load-bearing truncated-binomial (Bonferroni) inequality of writeup Sec 5.1:
      for EVEN J and every integer c >= 0,   2^{-c} <= sum_{j=0}^{J} (-1/2)^j (c)_j / j!
   Note (c)_j/j! = binom(c,j), so the RHS is the truncated binomial series for (1-1/2)^c.
   The terms binom(c,j)2^{-j} are NOT monotone in j, so the naive alternating-series
   argument does not apply; we test exhaustively.
   Also check the FAILURE for odd J (should give a lower bound instead), confirming
   parity matters exactly as the writeup states.
"""
from math import comb
bad_even = []
bad_odd  = []
for c in range(0, 400):
    target = 2.0**(-c)
    for J in range(0, 61):
        T = sum((-0.5)**j * comb(c, j) for j in range(0, J+1))
        if J % 2 == 0:
            if T < target - 1e-12*max(1,abs(T)):
                bad_even.append((c, J, T, target))
        else:
            if T > target + 1e-12*max(1,abs(T)):
                bad_odd.append((c, J, T, target))
print("even-J violations of  2^-c <= T_J(c) :", len(bad_even), bad_even[:5])
print("odd-J  violations of  2^-c >= T_J(c) :", len(bad_odd), bad_odd[:5])

# exact rational check for a subrange (no floating point)
from fractions import Fraction
bad = []
for c in range(0, 120):
    target = Fraction(1, 2**c)
    for J in range(0, 41, 2):
        T = sum(Fraction((-1)**j, 2**j) * comb(c, j) for j in range(0, J+1))
        if T < target:
            bad.append((c, J, T, target))
print("exact-rational even-J violations:", len(bad), bad[:5])

# show non-monotonicity of the terms (why the naive argument fails)
c = 30
print("terms binom(30,j)2^-j for j=0..12:", [round(comb(c,j)*2.0**-j, 3) for j in range(13)])
