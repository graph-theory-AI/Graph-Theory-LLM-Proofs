"""End-to-end exhaustive verification of the block-tribes construction for t=2.

Parameters follow the writeup exactly: t=2, m=1 => u=1/2, s=1/4,
N = ceil(log 2 / -log(1-s)) = ceil(2.409) = 3, n = m*N = 3 hats per player.
Total sample space ({0,1}^3)^2 = 64 points -- fully exhaustive.

Also runs a second exhaustive case t=2, m=2, N=2 (n=4; N chosen small on purpose
so the state space stays 256 points; this does NOT use the writeup's N, so bound
(2) on c is not expected there -- we only test the machinery: fibers monotone,
Lemma 1 balancing, Pr(E_i)=1/2, and inequality (1)).

Checks per case:
  1. C (tribes event) is globally monotone; Pr(C) = 1 - (1-s)^N exactly.
  2. For each player i and each x_{-i}: fiber is monotone; its measure equals
     1-(1-u)^{M_i} with M_i = #eligible tribes; E[Q_i] = Pr(C).
  3. Lemma-1 balancing of each fiber gives a balanced monotone family; the
     resulting strategy is valid; Pr(E_i) = 1/2 exactly.
  4. Inequality (1): Pr(E_1 & E_2) >= Pr(C) - sum_i E|q_i - 1/2|.
  5. For the m=1 case with the writeup's N: 1/2 <= c < 1/2 + s/2  (eq. (2)),
     and Var(Q_i) <= 2u (eq. (5)), E|Q_i-1/2| <= sqrt(2u)+s/2 (eq. (6)).
"""
import math
from fractions import Fraction
from itertools import product

def leq(x, y):
    return (x & y) == x

def is_upclosed(S, pts):
    return all((y in S) for x in S for y in pts if leq(x, y))

def balance(F, pts, half):
    A = set(F)
    while len(A) < half:
        comp = [x for x in pts if x not in A]
        maximal = [x for x in comp if not any(leq(x, y) and x != y for y in comp)]
        A.add(min(maximal))
    while len(A) > half:
        minimal = [x for x in A if not any(leq(y, x) and x != y for y in A)]
        A.remove(min(minimal))
    return frozenset(A)

def run_case(m, N, check_eq2):
    t = 2
    n = m * N
    u = Fraction(1, 2 ** m)
    s = u ** t
    pts = list(range(1 << n))
    half = 1 << (n - 1)
    full_tribe = (1 << m) - 1  # mask of one tribe within a stack

    def tribes_all_black(x1, x2):
        for a in range(N):
            mask = full_tribe << (a * m)
            if (x1 & mask) == mask and (x2 & mask) == mask:
                return True
        return False

    C = {(x1, x2) for x1 in pts for x2 in pts if tribes_all_black(x1, x2)}
    total = Fraction(1, 1 << (2 * n))
    prC = len(C) * total
    prC_formula = 1 - (1 - s) ** N
    print(f"[t=2, m={m}, N={N}, n={n}]  Pr(C) = {prC} = {float(prC):.6f}; "
          f"formula 1-(1-s)^N = {prC_formula}; match: {prC == prC_formula}")
    assert prC == prC_formula

    # global monotonicity of C (in all 2n coordinates jointly)
    for (x1, x2) in C:
        for b in range(n):
            assert (x1 | (1 << b), x2) in C and (x1, x2 | (1 << b)) in C
    print("  C is globally monotone: OK")

    if check_eq2:
        assert Fraction(1, 2) <= prC < Fraction(1, 2) + s / 2, "eq (2) fails"
        print(f"  eq (2): 1/2 <= c={float(prC):.6f} < 1/2+s/2={float(Fraction(1,2)+s/2):.6f}: OK")

    # fibers, Lemma 1, strategy
    fiber_meas = {1: {}, 2: {}}
    A_choice = {1: {}, 2: {}}
    for other in pts:  # x_{-i} for i=1 is x2, and vice versa (symmetric roles)
        # player 1's fiber given x2=other
        F1 = frozenset(x1 for x1 in pts if (x1, other) in C)
        # player 2's fiber given x1=other
        F2 = frozenset(x2 for x2 in pts if (other, x2) in C)
        for i, F in ((1, F1), (2, F2)):
            assert is_upclosed(F, pts), "fiber not monotone"
            # eligible tribes for player i given the OTHER player's stack
            M = sum(1 for a in range(N)
                    if (other >> (a * m)) & full_tribe == full_tribe)
            q = Fraction(len(F), 1 << n)
            assert q == 1 - (1 - u) ** M, "fiber measure formula fails"
            A = balance(F, pts, half)
            assert len(A) == half and is_upclosed(A, pts)
            assert (F <= A) if len(F) <= half else (A <= F)
            fiber_meas[i][other] = q
            A_choice[i][other] = A
    print("  every fiber monotone; measure = 1-(1-u)^M; Lemma-1 balancing valid: OK")

    EQ = {i: sum(fiber_meas[i].values()) / len(pts) for i in (1, 2)}
    assert EQ[1] == prC and EQ[2] == prC, "E[Q_i] != Pr(C)"
    print(f"  E[Q_i] = Pr(C) exactly: OK")

    # success events
    prE = {}
    succ = 0
    lossC = {1: 0, 2: 0}
    for x1 in pts:
        for x2 in pts:
            e1 = x1 in A_choice[1][x2]
            e2 = x2 in A_choice[2][x1]
            if e1 and e2:
                succ += 1
            prE[1] = prE.get(1, 0) + (1 if e1 else 0)
            prE[2] = prE.get(2, 0) + (1 if e2 else 0)
    prE1 = Fraction(prE[1], 1 << (2 * n))
    prE2 = Fraction(prE[2], 1 << (2 * n))
    assert prE1 == Fraction(1, 2) and prE2 == Fraction(1, 2), "Pr(E_i) != 1/2"
    print("  Pr(E_1) = Pr(E_2) = 1/2 exactly (valid balanced strategy): OK")

    prSucc = Fraction(succ, 1 << (2 * n))
    Edev = {i: sum(abs(fiber_meas[i][o] - Fraction(1, 2)) for o in pts) / len(pts)
            for i in (1, 2)}
    lower = prC - Edev[1] - Edev[2]
    print(f"  exact success Pr(E1&E2) = {prSucc} = {float(prSucc):.6f}")
    print(f"  bound (1): Pr(C) - sum E|q_i-1/2| = {float(lower):.6f}; "
          f"holds: {prSucc >= lower}")
    assert prSucc >= lower

    if check_eq2:
        VarQ = sum((fiber_meas[1][o] - EQ[1]) ** 2 for o in pts) / len(pts)
        print(f"  Var(Q_i) = {float(VarQ):.6f} <= 2u = {float(2*u):.6f}: {VarQ <= 2*u}")
        assert VarQ <= 2 * u
        bnd6 = math.sqrt(2 * float(u)) + float(s) / 2
        print(f"  E|Q-1/2| = {float(Edev[1]):.6f} <= sqrt(2u)+s/2 = {bnd6:.6f}: "
              f"{float(Edev[1]) <= bnd6}")
        assert float(Edev[1]) <= bnd6
    print()
    return prSucc


# Case 1: the writeup's own parameters for t=2, m=1.
s1 = Fraction(1, 4)
N1 = math.ceil(math.log(2) / -math.log(1 - float(s1)))
print(f"writeup N for (t=2,m=1): ceil(log2/-log(1-1/4)) = {N1}")
assert N1 == 3
run_case(m=1, N=3, check_eq2=True)

# Case 2: machinery check on m=2 with small N=2 (not the writeup's N).
run_case(m=2, N=2, check_eq2=False)

print("End-to-end construction VERIFIED on exhaustive cases.")
