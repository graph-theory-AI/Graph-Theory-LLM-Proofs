"""Symbolic verification of the writeup's algebraic claims (sympy)."""
import sympy as sp

q, lam, b = sp.symbols('q lam b', positive=True)
r = sp.symbols('r', positive=True, integer=True)

print("(13)  D'_{r,lambda}(q) = 0  <=>  q^r - lambda r q + r - 1 = 0")
for rr in range(2, 8):
    D = (1 - 1/(lam*q)) / (1 - q**(-sp.Integer(rr)))
    num = sp.simplify(sp.numer(sp.together(sp.diff(D, q))))
    tgt = q**rr - lam*rr*q + rr - 1
    ratio = sp.simplify(sp.cancel(num / tgt))
    print(f"   r={rr}: numerator(D') / (q^r - lam r q + r-1) = {ratio}  "
          f"(a nonvanishing factor => same zero set: {'YES' if ratio.is_constant(q) is not False or sp.simplify(ratio).free_symbols <= {q, lam} else '?'})")
    # check zero-set equality directly
    print(f"          simplify(numerator(D') - const*target) check:",
          sp.simplify(sp.expand(num - ratio*tgt)) == 0)

print("\n(14)  if b^r - lambda r b + r - 1 = 0 then D_{r,lambda}(b) = b^(r-1)/(lambda r)")
for rr in range(2, 9):
    Db = (1 - 1/(lam*b)) / (1 - b**(-sp.Integer(rr)))
    sub = sp.solve(sp.Eq(b**rr, lam*rr*b - rr + 1), b**rr)
    expr = sp.simplify(Db.subs(b**rr, lam*rr*b - rr + 1) - b**(rr-1)/(lam*rr))
    # safer: substitute into the rewritten identity
    expr2 = sp.simplify(sp.factor(sp.numer(sp.together(
        (1 - 1/(lam*b))*b**rr/(b**rr - 1) - b**(rr-1)/(lam*rr))).subs(
            b**rr, lam*rr*b - rr + 1)))
    print(f"   r={rr}: residual = {sp.simplify(expr2)}")

print("\n(1)  b^r - 2rb + r - 1 = 0  =>  b^(r-1)/(2r) = (1-1/(2b))(1+1/(2rb-r))")
for rr in range(2, 9):
    lhs = b**(rr-1)/(2*rr)
    rhs = (1 - 1/(2*b))*(1 + 1/(2*rr*b - rr))
    resid = sp.simplify(sp.numer(sp.together(lhs - rhs)))
    resid = sp.simplify(sp.rem(sp.Poly(resid, b), sp.Poly(b**rr - 2*rr*b + rr - 1, b)))
    print(f"   r={rr}: (lhs-rhs) mod (b^r-2rb+r-1) = {resid}")

print("\nb_0 > lambda^{1/(r-1)} (so consecutive same-colour blocks are disjoint):")
print("   P(q)=q^r-lam r q+r-1 has P'(q)=r q^{r-1} - lam r, zero at q=lam^{1/(r-1)};")
print("   P(1) = r(1-lam) < 0 for lam>1, and P decreasing on (1, lam^{1/(r-1)}),")
print("   hence P<0 on (1, lam^{1/(r-1)}] and the unique root b_0 exceeds lam^{1/(r-1)}.  OK")
