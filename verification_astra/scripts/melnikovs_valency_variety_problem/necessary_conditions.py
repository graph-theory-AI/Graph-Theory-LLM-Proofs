"""Mechanisation of the writeup's section-3 counting method (eqs (4)-(8), (11)),
used (i) to re-derive its t<=6 conclusions independently, and (ii) to ask the
question the writeup leaves open: can a counterexample avoid an isolated vertex?

For a graph of EVEN order n=2m with chromatic number k, t=n-w and minimum degree
>= delta, the writeup's inequalities are

  D + 2e + sum_i h_i^2 <= m^2                         (7)
  D >= D_0 = floor(w^2/4),   X := D - D_0 >= 0,  D even
  E := sum h_i^2 - Q_k(m) >= 0, E even
  b <= m - a + e,  a = min_i h_i                      (8)
  w=2r+1, b <= delta+r  =>  X >= (delta+r-b)^2        (5)
  w=2r,   b <= delta+r-1 => X >= (delta+r-1-b)(delta+r-b)   (6)

so a graph with these parameters can exist only if some (X,e,E) fits inside the
budget B = m^2 - D_0 - Q_k(m).  This is a NECESSARY condition only.
"""
import math

def Q(k, m):
    q, s = divmod(m, k)
    return (k - s) * q * q + s * (q + 1) * (q + 1)

def A_of_E(k, m, E):
    """min possible min_i h_i over all h with sum m and sum h^2 <= Q(k,m)+E."""
    best = None
    q, s = divmod(m, k)
    # search over the smallest part value a, greedily balancing the rest
    for a in range(0, q + 1):
        rest = m - a
        if k == 1:
            ss = a * a if rest == 0 else None
            if ss is None: continue
        else:
            ss = a * a + Q(k - 1, rest)
        if ss <= Q(k, m) + E:
            best = a
            break
    return best

def excluded_even(m, k, t, delta):
    """True if no graph of order 2m, chromatic number k, n-w=t, min degree>=delta
    can satisfy the writeup's inequalities."""
    w = 2 * m - t
    if w < 1 or t < 1:
        return True
    D0 = (w * w) // 4
    B = m * m - D0 - Q(k, m)
    if B < 0:
        return True
    odd = (w % 2 == 1)
    r = (w - 1) // 2 if odd else w // 2
    E = 0
    while E <= B:
        a = A_of_E(k, m, E)
        if a is None:
            E += 2; continue
        for e in range(0, (B - E) // 2 + 1):
            b = m - a + e                     # largest b allowed by (8)
            if odd:
                Xmin = (delta + r - b) ** 2 if b <= delta + r else 0
            else:
                Xmin = (delta + r - 1 - b) * (delta + r - b) if b <= delta + r - 1 else 0
            # D even, D0 parity fixes X parity
            X = Xmin
            if (X - 0) % 2 != (D0 % 2) * 0:   # placeholder; parity handled below
                pass
            if (D0 + X) % 2 != 0:
                X += 1
            if X + 2 * e + E <= B:
                return False
        E += 2
    return True

print("=== re-derivation of the writeup's table (13)/(14) for t<=6, k=3..8 ===")
print(" (largest even order 2m not excluded, by t and min-degree assumption)")
print(f"{'k':>2} {'t':>2} | {'delta>=0':>9} {'delta>=1':>9} | (2k-1)t  (2k-1)t+1")
for k in range(2, 7):
    for t in range(1, 8):
        res = {}
        for delta in (0, 1):
            best = 0
            for m in range(1, 400):
                if not excluded_even(m, k, t, delta):
                    best = 2 * m
            res[delta] = best
        print(f"{k:>2} {t:>2} | {res[0]:>9} {res[1]:>9} | {(2*k-1)*t:>7}  {(2*k-1)*t+1}")

print()
print("=== can a counterexample avoid isolated vertices?  (k=3) ===")
print(" a counterexample needs n >= (2k-1)t+2 = 5t+2")
print(f"{'t':>3} {'need n>=':>9} {'max n (delta>=0)':>17} {'max n (delta>=1, n even)':>25} {'max n (delta>=1, n odd)':>24}")
for t in range(1, 41):
    k = 3
    need = (2 * k - 1) * t + 2
    def maxn(delta, parity):
        best = 0
        for m in range(1, 600):
            if parity == 'even':
                if not excluded_even(m, k, t, delta):
                    best = 2 * m
            else:  # odd order n: add an isolated vertex -> order n+1=2m, w+1, same t, delta 0
                if not excluded_even(m, k, t, 0):
                    best = 2 * m - 1
        return best
    e0 = maxn(0, 'even')
    e1 = maxn(1, 'even')
    o1 = maxn(1, 'odd')
    flag = ""
    if max(e1, o1) >= need:
        flag = "  <-- delta>=1 counterexample NOT excluded"
    if t in (7, 8) or flag or t % 5 == 0:
        print(f"{t:>3} {need:>9} {e0:>17} {e1:>25} {o1:>24}{flag}")
