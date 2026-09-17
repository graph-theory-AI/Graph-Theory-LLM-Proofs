#!/usr/bin/env python3
"""Purely arithmetic re-derivation of steps (6) and (7) of the writeup.

(7) claims   max over 0<=l<=r=b+t of F_b(l)=C(l,2)-(b-1)l
             equals max{0, C(t+1,2)-C(b,2)}.
(6) claims   F_b(l) <= (k-1)t  for all 0<=l<=b+t,
             in the regime the writeup assumes: D>=4, 2<=k<D, b=D-k, 0<=t<=k.
Brute force over a large parameter box, plus a sympy identity check.
"""
from math import comb
import sympy as sp

# --- identity in (7): F_b(b+t) == C(t+1,2) - C(b,2) ---
b_, t_ = sp.symbols('b t')
F_end = sp.binomial(b_+t_, 2) - (b_-1)*(b_+t_)
target = sp.binomial(t_+1, 2) - sp.binomial(b_, 2)
diff = sp.simplify(sp.expand(sp.Rational(1,1)*( (b_+t_)*(b_+t_-1)/2 - (b_-1)*(b_+t_) ) - ( t_*(t_+1)/2 - b_*(b_-1)/2 )))
print("(7) endpoint identity  F_b(b+t) - [C(t+1,2)-C(b,2)] simplifies to:", diff)

F = lambda b,l: comb(l,2) - (b-1)*l
bad7 = bad6 = 0
ex6 = []
for D in range(4, 400):
    for k in range(2, D):
        b = D - k
        for t in range(0, k+1):
            r = b + t
            mx = max(F(b,l) for l in range(0, r+1))
            if mx != max(0, comb(t+1,2)-comb(b,2)):
                bad7 += 1
            if mx > (k-1)*t:
                bad6 += 1
                if len(ex6) < 5: ex6.append((D,k,b,t,mx,(k-1)*t))
print("(7) violations over D=4..399, all k,t :", bad7)
print("(6) violations over D=4..399, all k,t :", bad6, ex6)

# also check (6) in the excluded regime D<=3 to confirm it really does fail there
bad_low = []
for D in range(2, 4):
    for k in range(2, D):
        b = D-k
        for t in range(0, k+1):
            mx = max(F(b,l) for l in range(0, b+t+1))
            if mx > (k-1)*t: bad_low.append((D,k,b,t,mx,(k-1)*t))
print("(6) violations for D<=3 (regime the writeup excludes):", bad_low)
