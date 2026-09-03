"""Re-derive every numeric inequality in the writeup's Lemma (Section 3).

Self-contained, no external dependencies.
"""
import math
from fractions import Fraction
from itertools import product

ok = True

def check(name, cond):
    global ok
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

print("1. min of s - s^2/2 on [2/3, 4/3] equals 4/9 (concave => min at endpoints)")
f = lambda s: s - s * s / 2
ends = [Fraction(2, 3), Fraction(4, 3)]
vals = [e - e * e / 2 for e in ends]
check("f(2/3) = 4/9", vals[0] == Fraction(4, 9))
check("f(4/3) = 4/9", vals[1] == Fraction(4, 9))
# dense numeric scan as well
scan_min = min(f(2 / 3 + i * (2 / 3) / 10 ** 5) for i in range(10 ** 5 + 1))
check("numeric scan min >= 4/9 - 1e-9", scan_min >= 4 / 9 - 1e-9)

print("2. F >= 4/9 - 1/6 = 5/18")
check("4/9 - 1/6 == 5/18", Fraction(4, 9) - Fraction(1, 6) == Fraction(5, 18))

print("3. F = (u+v) - 2uv - u*zR - v*zL identity (symbolic-by-sampling)")
good = True
for u, v, zR, zL in product([0, .13, .4, .66, 1], repeat=4):
    lhs = u * (1 - v - zR) + v * (1 - u - zL)
    rhs = (u + v) - 2 * u * v - u * zR - v * zL
    if abs(lhs - rhs) > 1e-12:
        good = False
check("algebraic identity holds", good)

print("4. F >= s - s^2/2 - 1/6 given uv <= s^2/4 and u zR + v zL <= zL + zR <= 1/6")
# u zR + v zL <= zR + zL needs u,v <= 1: true since |A cap L| <= m. Check logic numerically:
good = True
for _ in range(200000):
    import random
    u, v = random.random(), random.random()
    s = u + v
    if not (2 / 3 <= s <= 4 / 3):
        continue
    zL = random.random() / 6
    zR = 1 / 6 - zL
    F = (u + v) - 2 * u * v - u * zR - v * zL
    if F < s - s * s / 2 - 1 / 6 - 1e-12:
        good = False
check("bound F >= s - s^2/2 - 1/6 on random samples", good)

print("5. One of the two products >= (5/18)/2 * m^2 = 5 m^2/36")
check("(5/18)/2 == 5/36", Fraction(5, 18) / 2 == Fraction(5, 36))

print("6. Hypergeometric bound C(m-q,p)/C(m,p) <= (1-q/m)^p <= exp(-pq/m)")
good = True
for m in [5, 10, 20, 37]:
    for p in range(0, m + 1):
        for q in range(0, m + 1):
            if p > m - q:
                continue  # probability is 0, bound trivially holds
            lhs = Fraction(math.comb(m - q, p), math.comb(m, p))
            mid = (1 - Fraction(q, m)) ** p
            if lhs > mid:
                good = False
            if float(mid) > math.exp(-p * q / m) + 1e-12:
                good = False
check("C(m-q,p)/C(m,p) <= (1-q/m)^p <= e^{-pq/m} for m in {5,10,20,37}", good)

print("7. Union bound: 3^{2m} * exp(-100 m/36) < 1 for all m >= 1")
coeff = 2 * math.log(3) - 100 / 36
print(f"     2*ln(3) = {2*math.log(3):.6f}, 100/36 = {100/36:.6f}, difference = {coeff:.6f}")
check("2 ln 3 - 100/36 < 0", coeff < 0)
check("holds numerically for m=1..1000", all(
    (2 * m) * math.log(3) - 100 * m / 36 < 0 for m in range(1, 1001)))

print("8. Separator consequence arithmetic (N = 2m)")
check("N/12 == m/6", Fraction(1, 12) * 2 == Fraction(1, 6))
check("|B| >= N - 2N/3 - N/12 = N/4",
      Fraction(1) - Fraction(2, 3) - Fraction(1, 12) == Fraction(1, 4))
check("interval [N/3, 2N/3] == [2m/3, 4m/3]",
      Fraction(1, 3) * 2 == Fraction(2, 3) and Fraction(2, 3) * 2 == Fraction(4, 3))
# feasibility of greedy: total non-separator vertices >= 11N/12 >= N/3
check("11/12 >= 1/3", Fraction(11, 12) >= Fraction(1, 3))

print("\nALL PASS" if ok else "\nSOME CHECKS FAILED")
