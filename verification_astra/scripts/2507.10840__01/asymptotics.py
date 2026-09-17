"""Symbolic/numeric check of the writeup's arithmetic in Sections 2 and 3."""
import sympy as sp, math
r, n, q, h = sp.symbols('r n q h', positive=True)

# identity claimed in section 3
lhs = (3*r-2)/(4*r-2); rhs = sp.Rational(3,4) - 1/(8*r-4)
print("(3r-2)/(4r-2) == 3/4 - 1/(8r-4) :", sp.simplify(lhs-rhs) == 0)

# section 2, h = 6q-1, n = 6q: ceil(2h/3) == 4q ?
print("section 2, ceil(2(6q-1)/3) vs 4q for q=1..12:",
      [( -(-(2*(6*Q-1))//3), 4*Q) for Q in range(1,13)],
      "all equal:", all(-(-(2*(6*Q-1))//3) == 4*Q for Q in range(1,2000)))

# max path weight: max(2r, 4r-2) == 4r-2 for r>=1
print("max(2r,4r-2)==4r-2 for r>=1:", all(max(2*R,4*R-2)==4*R-2 for R in range(1,200)))

# section 3: exact bound vs 3n/4 - C sqrt(n), optimising r (h=n-r odd)
def best_bound(N):
    best = None
    for R in range(2, N-4):
        H = N - R
        if H % 2 == 0 or H < 5: continue
        b = -(-((3*R-2)*H) // (4*R-2))
        if best is None or b > best[0]: best = (b, R, H)
    return best
print("  n   best bound   r    3n/4   (3n/4-bound)/sqrt(n)")
for N in [20, 50, 100, 400, 1000, 10000, 100000, 1000000]:
    b, R, H = best_bound(N) if N <= 10000 else (None,None,None)
    if b is None:   # large n: optimise analytically over the continuum
        Rc = max(2, round(math.sqrt(N/6)))
        while (N-Rc) % 2 == 0: Rc += 1
        H = N-Rc; R = Rc
        b = -(-((3*R-2)*H)//(4*R-2))
    print("%8d %10d %5d %9.1f %8.4f" % (N, b, R, 3*N/4, (3*N/4-b)/math.sqrt(N)))
# c < 3/4 for all large n?
for c in [0.6, 0.7, 0.74, 0.749]:
    Nmin = next(N for N in range(6, 4000000) if (lambda t: t is not None and t[0] >= c*N)(
        (lambda: (best_bound(N) if N <= 3000 else (lambda R: (-(-((3*R-2)*(N-R))//(4*R-2)), R, N-R))(
            (lambda x: x + ((N-x) % 2 == 0))(max(2, round(math.sqrt(N/6)))))))()))
    print("c=%.3f achieved from n >= %d" % (c, Nmin))
