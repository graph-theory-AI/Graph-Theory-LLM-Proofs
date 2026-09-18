"""Symbolic check of the key identity (1)-(2) in Lemma 1 of
attacks_retry/2106.03261__00/output.md, over a general commutative ring:
   B(A3,B3) = B(B2,B4)
with A0=[1:0:0], A1=[0:1:0], B=diag(alpha,beta,gamma), A2=[x:0:z], A4=[0:y:w],
B0=[0:s:t], B1=[r:0:u], and A3,B3,B2,B4 obtained as cross products of polar vectors.
"""
import sympy as sp

al,be,ga,x,y,z,w,r,s,t,u = sp.symbols('alpha beta gamma x y z w r s t u')
M = sp.diag(al,be,ga)
def polar(P): return M*sp.Matrix(P)
def cross(a,b): return sp.Matrix(a).cross(sp.Matrix(b))
def B(P,Q): return (sp.Matrix(P).T * M * sp.Matrix(Q))[0,0]

A0 = sp.Matrix([1,0,0]); A1 = sp.Matrix([0,1,0])
A2 = sp.Matrix([x,0,z]); A4 = sp.Matrix([0,y,w])
B0 = sp.Matrix([0,s,t]); B1 = sp.Matrix([r,0,u])

A3 = cross(polar(A2), polar(A4))
B3 = cross(polar(B0), polar(B1))
B2 = cross(polar(B0), polar(A2))
B4 = cross(polar(B1), polar(A4))

print("A3 =", sp.simplify(A3.T))
print("B3 =", sp.simplify(B3.T))
print("B2 =", sp.simplify(B2.T))
print("B4 =", sp.simplify(B4.T))
print("writeup table (1) match:")
print("  A3 == (-be*ga*z*y, -al*ga*x*w, al*be*x*y)?",
      sp.simplify(A3 - sp.Matrix([-be*ga*z*y, -al*ga*x*w, al*be*x*y])) == sp.zeros(3,1))
print("  B3 == ( be*ga*s*u,  al*ga*t*r, -al*be*s*r)?",
      sp.simplify(B3 - sp.Matrix([be*ga*s*u, al*ga*t*r, -al*be*s*r])) == sp.zeros(3,1))
print("  B2 == ( be*ga*s*z,  al*ga*t*x, -al*be*s*x)?",
      sp.simplify(B2 - sp.Matrix([be*ga*s*z, al*ga*t*x, -al*be*s*x])) == sp.zeros(3,1))
print("  B4 == (-be*ga*u*y, -al*ga*r*w,  al*be*r*y)?",
      sp.simplify(B4 - sp.Matrix([-be*ga*u*y, -al*ga*r*w, al*be*r*y])) == sp.zeros(3,1))

lhs = sp.expand(B(A3,B3)); rhs = sp.expand(B(B2,B4))
print("B(A3,B3) =", lhs)
print("B(B2,B4) =", rhs)
print("identity (2)  B(A3,B3) - B(B2,B4) == 0 :", sp.simplify(lhs-rhs) == 0)
claimed = sp.expand(-al*be**2*ga**2*z*y*s*u - al**2*be*ga**2*x*w*t*r - al**2*be**2*ga*x*y*s*r)
print("matches writeup's displayed value:", sp.simplify(lhs - claimed) == 0)

# orthogonality checks of the constructed points against their two defining points
for nm,(P,p1,p2) in {'A3':(A3,A2,A4),'B3':(B3,B0,B1),'B2':(B2,B0,A2),'B4':(B4,B1,A4)}.items():
    print(f"  {nm} _|_ both defining points:",
          sp.simplify(B(P,p1))==0 and sp.simplify(B(P,p2))==0)

# and the form used in the construction
X0,X1,X2,Y0,Y1,Y2 = sp.symbols('X0 X1 X2 Y0 Y1 Y2')
Bc = sp.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
print("construction form det:", Bc.det())
xx,yy = sp.symbols('xx yy')
print("B((1,x,y),(1,x,y)) =", sp.expand((sp.Matrix([1,xx,yy]).T*Bc*sp.Matrix([1,xx,yy]))[0,0]))
x2,y2 = sp.symbols('x2 y2')
print("B((1,x,y),(1,x2,y2)) =", sp.expand((sp.Matrix([1,xx,yy]).T*Bc*sp.Matrix([1,x2,y2]))[0,0]))
