"""Symbolic check of Lemma 1 of attacks_retry/2106.03261__00/output.md.

Setup of the writeup's proof: diagonal symmetric form B = diag(a,b,g) on K^3,
A0=[1:0:0], A1=[0:1:0], A2=[x:0:z], A4=[0:y:w], B0=[0:s:t], B1=[r:0:u].
Then A3 = pol(A2) ^ pol(A4), B3 = pol(B0) ^ pol(B1),
     B2 = pol(B0) ^ pol(A2), B4 = pol(B1) ^ pol(A4).
Claim (eq. (2)): B(A3,B3) = B(B2,B4) identically.
"""
import sympy as sp

a, b, g, x, z, y, w, s, t, r, u = sp.symbols('alpha beta gamma x z y w s t r u')
M = sp.diag(a, b, g)

def pol(P):           # coefficient vector of the polar line of P
    return M * P

def meet(L1, L2):     # intersection point of two lines = cross product
    return sp.Matrix(list(L1.cross(L2)))

def bil(P, Q):
    return sp.expand((P.T * M * Q)[0, 0])

A0 = sp.Matrix([1, 0, 0]); A1 = sp.Matrix([0, 1, 0])
A2 = sp.Matrix([x, 0, z]); A4 = sp.Matrix([0, y, w])
B0 = sp.Matrix([0, s, t]); B1 = sp.Matrix([r, 0, u])

A3 = meet(pol(A2), pol(A4))
B3 = meet(pol(B0), pol(B1))
B2 = meet(pol(B0), pol(A2))
B4 = meet(pol(B1), pol(A4))

print("A3 =", A3.T)
print("B3 =", B3.T)
print("B2 =", B2.T)
print("B4 =", B4.T)

lhs = bil(A3, B3)
rhs = bil(B2, B4)
print("B(A3,B3) =", sp.factor(lhs))
print("B(B2,B4) =", sp.factor(rhs))
print("difference simplifies to:", sp.simplify(lhs - rhs))
assert sp.simplify(lhs - rhs) == 0
# also compare with the writeup's displayed expression (2)
claimed = sp.expand(-a*b**2*g**2*z*y*s*u - a**2*b*g**2*x*w*t*r - a**2*b**2*g*x*y*s*r)
print("matches displayed (2):", sp.simplify(lhs - claimed) == 0)

# sanity: check the built points really satisfy the 14 non-a3b3 Petersen edges
edges = [('a0','a1'),('a1','a2'),('a2','a3'),('a3','a4'),('a4','a0'),
         ('a0','b0'),('a1','b1'),('a2','b2'),('a4','b4'),
         ('b0','b2'),('b2','b4'),('b1','b3'),('b3','b0'),('b1','b4'),
         ('a3','b3')]
pts = {'a0':A0,'a1':A1,'a2':A2,'a3':A3,'a4':A4,
       'b0':B0,'b1':B1,'b2':B2,'b3':B3,'b4':B4}
auto = []
for (p,qq) in edges:
    v = sp.simplify(bil(pts[p], pts[qq]))
    auto.append(((p,qq), v))
for e, v in auto:
    print(e, "-> B =", v if v != 0 else 0, "(identically zero)" if v == 0 else "")
