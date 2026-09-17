"""Exact verification of the retry writeup's odd-walk lemma for explicit integer a,b,c.

All arithmetic is done EXACTLY in the real quadratic field Q(sqrt(D)), D = discriminant
of E^n F, represented as pairs (x, y) <-> x + y*sqrt(D) with x, y in Q.  No floating
point anywhere.  Checked for each triple:
  * the matrices E = J_a^2 J_b^2 and F = J_a J_c J_b of the writeup's formula (2);
  * least n >= 0 with discriminant (3) positive, and det(E^n F) != 0;
  * the walk x0, J_b x0, J_c J_b x0, J_a J_c J_b x0, ... (3 + 4n steps): every
    consecutive pair exactly orthogonal, every vector nonzero, every line exactly
    inside P_a u P_b u P_c, and the walk exactly closed projectively.
"""
from fractions import Fraction as Fr
import itertools, sympy as sp

class Q2:                      # x + y*sqrt(D)
    D = 0
    __slots__ = ('x', 'y')
    def __init__(self, x=0, y=0): self.x, self.y = Fr(x), Fr(y)
    def __add__(s, o): o = c(o); return Q2(s.x+o.x, s.y+o.y)
    def __radd__(s, o): return s + o
    def __sub__(s, o): o = c(o); return Q2(s.x-o.x, s.y-o.y)
    def __rsub__(s, o): return c(o) - s
    def __neg__(s): return Q2(-s.x, -s.y)
    def __mul__(s, o):
        o = c(o); return Q2(s.x*o.x + Q2.D*s.y*o.y, s.x*o.y + s.y*o.x)
    def __rmul__(s, o): return s * o
    def __eq__(s, o): o = c(o); return s.x == o.x and s.y == o.y
    def iszero(s): return s.x == 0 and s.y == 0
    def __repr__(s): return f"({s.x}+{s.y}*sqrt({Q2.D}))"
def c(o): return o if isinstance(o, Q2) else Q2(o, 0)

def cross(u, v):
    return [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
def dot(u, v): return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]

def run(a, b, c_):
    A, B, C = (sp.Matrix(t) for t in (a, b, c_))
    det = sp.Matrix.hstack(A, B, C).det()
    print(f"a={a} b={b} c={c_}  det={det}  dots=({A.dot(B)},{A.dot(C)},{B.dot(C)})")
    assert det != 0
    if A.dot(B) == 0 or A.dot(C) == 0 or B.dot(C) == 0:
        for P, Qv in itertools.combinations([A, B, C], 2):
            if P.dot(Qv) == 0:
                tri = [P, Qv, P.cross(Qv)]
                assert all(u.dot(v) == 0 for u, v in itertools.combinations(tri, 2))
                assert all(any(t.dot(d) == 0 for d in (A, B, C)) for t in tri)
                print("  perpendicular case -> exact triangle", [list(t) for t in tri], " OK\n"); return
    f1, f2 = A.cross(B), A.cross(A.cross(B))         # integer basis of P_a
    Bm = sp.Matrix.hstack(f1, f2); P = (Bm.T*Bm).inv()*Bm.T
    def opm(seq):
        cols = []
        for g in (f1, f2):
            x = g
            for d in seq: x = sp.Matrix(d).cross(x)
            s = sp.expand(P*x); assert sp.expand(Bm*s - x) == sp.zeros(3, 1)
            cols.append(s)
        return sp.Matrix.hstack(*cols)
    Em, Fm = opm([B, B, A, A]), opm([B, C, A])
    print("   E =", Em.tolist(), "  F =", Fm.tolist())
    n = 0
    while True:
        M = sp.expand(Em**n*Fm); D = sp.expand(sp.trace(M)**2 - 4*M.det())
        if D > 0: break
        n += 1; assert n < 400, "n exceeded the test cap (a,b nearly parallel)"
    assert M.det() != 0
    # move to exact quadratic field
    Dn, Dd = sp.fraction(sp.nsimplify(D)); Dn, Dd = int(Dn), int(Dd)
    Q2.D = Fr(Dn, Dd)
    lam = Q2(Fr(sp.Rational(sp.trace(M)))/2, Fr(1, 2))    # (tr + sqrt(D))/2
    m00, m01, m10, m11 = (Fr(sp.Rational(M[i, j])) for i, j in ((0,0),(0,1),(1,0),(1,1)))
    vec = [Q2(m01), lam - m00]
    if vec[0].iszero() and vec[1].iszero(): vec = [lam - m11, Q2(m10)]
    # check it really is an eigenvector: M vec = lam vec
    lhs = [Q2(m00)*vec[0] + Q2(m01)*vec[1], Q2(m10)*vec[0] + Q2(m11)*vec[1]]
    assert (lhs[0] - lam*vec[0]).iszero() and (lhs[1] - lam*vec[1]).iszero(), "not an eigenvector"
    f1q = [Q2(Fr(int(t))) for t in f1]; f2q = [Q2(Fr(int(t))) for t in f2]
    x0 = [f1q[i]*vec[0] + f2q[i]*vec[1] for i in range(3)]
    assert not all(t.iszero() for t in x0)
    Aq, Bq, Cq = ([Q2(Fr(int(t))) for t in V] for V in (A, B, C))
    walk = [x0]
    for d in [Bq, Cq, Aq] + n*[Bq, Bq, Aq, Aq]:
        nx_ = cross(d, walk[-1])
        assert not all(t.iszero() for t in nx_), "zero vector in the walk"
        walk.append(nx_)
    L = len(walk) - 1
    assert L == 3 + 4*n and L % 2 == 1
    for i in range(L):
        assert dot(walk[i], walk[i+1]).iszero(), f"step {i} not perpendicular"
    for p in walk:
        assert any(dot(p, d).iszero() for d in (Aq, Bq, Cq)), "line escapes the three planes"
    cr = cross(walk[0], walk[-1])
    assert all(t.iszero() for t in cr), "walk is not closed"
    print(f"   n={n}: EXACT odd closed walk of length {L}; all steps perpendicular,"
          f" all lines in P_a u P_b u P_c, exactly closed.  D={Q2.D}\n")

print("=== case 1: two normals perpendicular ==="); run([1,0,0],[0,1,0],[1,2,3])
print("=== case 2 ==="); run([0,0,1],[1,0,2],[1,1,1])
print("=== case 3 ==="); run([1,1,1],[1,2,3],[2,1,5])
print("=== case 4 ==="); run([0,0,1],[3,0,4],[1,1,7])
print("=== case 5 ==="); run([2,-1,3],[1,4,1],[5,2,-2])
print("=== case 6 ==="); run([1,0,0],[1,1,0],[1,1,1])
print("=== case 7 ==="); run([3,1,2],[1,-2,4],[2,5,1])
