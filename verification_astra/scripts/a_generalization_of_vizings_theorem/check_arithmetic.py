"""
All numeric claims of sections 2-4 of the writeup, re-derived independently,
plus (a) an independent first-moment derivation confirming the CONSTANT in the
counting lemma (1)/(4), (b) a finite-N test of (1) on the extremal family K_N,
(c) the random-greedy lower bound on the matching number (sanity check that the
first-moment threshold is not below the truth), (d) how large n must be for the
o(N) error term to be harmless.
"""
import math
from math import log, exp, lgamma, comb

def f(x): return x + (1-x)*math.log(1-x)
def expo(x, s, c):  # the bracket in (10): x log(c/x) + x - s f(x)
    return x*log(c/x) + x - s*f(x)

print("="*78); print("A. Section 2.1 exponent at x=1/5, s=c=100")
x, s, c = 0.2, 100, 100
print(f"  x log(c/x)        = {x*log(c/x):.6f}   (writeup: (log 500)/5 = {log(500)/5:.6f})")
print(f"  f(x)              = {f(x):.8f}  >= x^2/2 = {x*x/2:.8f}  -> {f(x)>=x*x/2}")
print(f"  s f(x)            = {s*f(x):.6f}")
print(f"  exponent          = {expo(x,s,c):.6f}   writeup's bound (log500+1)/5-2 = {(log(500)+1)/5-2:.6f}")
print(f"  writeup claims  < -2/5 = -0.4 :  {expo(x,s,c) < -0.4}")

print("="*78); print("B. first-moment threshold x* (largest x with exponent >= 0), s=c=100")
lo, hi = 1e-9, 0.999999
for _ in range(200):
    mid = (lo+hi)/2
    if expo(mid,s,c) > 0: lo = mid
    else: hi = mid
print(f"  x* = {lo:.6f}  -> max facet-disjoint family <= {lo:.4f}*T (writeup uses the weaker x=0.2)")
print(f"  => first moment actually forces chi >= ~ {100/lo:.1f} colors (writeup only claims 451)")

print("="*78); print("C. random-greedy LOWER bound on matching number (sanity: truth must lie below x*)")
# y = fraction uncovered after greedy on s-uniform, avg vertex degree c: y=(1+(s-1)c)^{-1/(s-1)}
y = (1+(s-1)*c)**(-1/(s-1))
print(f"  greedy covers fraction {1-y:.6f} of vertices  ->  matching of size {(1-y):.4f}*T")
print(f"  consistency: greedy {1-y:.4f} <= first-moment ceiling {lo:.4f}: {1-y <= lo}")

print("="*78); print("D. pruning probability q (section 2.2)")
q = (math.e/4)**100
print(f"  q = (e/4)^100 = {q:.4e}   100q = {100*q:.4e}   (writeup: q < 1e-10)  {q<1e-10}")
print(f"  E Z >= 100T(1-100q) = {100*(1-100*q):.12f} T  > 99T : {100*(1-100*q) > 99}")
# exact Chernoff/Markov step: P(Bin(n-1,100/n) >= 200) <= 2^-200 (1+100/n)^(n-1) <= e^100/2^200
for n in (10**6, 10**12):
    p = 100/n
    bound = (1+p)**(n-1) / 2**200
    print(f"  n={n:g}: 2^-200 (1+100/n)^(n-1) = {bound:.4e}  <= (e/4)^100 = {q:.4e}: {bound<=q}")

print("="*78); print("E. final counting (section 3)")
print("  450 colors * (m-1) with m = T/5:  450*(T/5 - 1) = 90T - 450 < 90T < |E(H)|  -> >= 451 colors")
print(f"  conjectured bound r+d-1 = 200+100-1 = {200+100-1}; 451 > 299: {451>299}")

print("="*78); print("F. independent confirmation of the CONSTANT in (1)/(4):")
print("   first moment for a RANDOM D-regular s-uniform hypergraph (config model),")
print("   computed numerically from exact log-factorials, vs the lemma's bound.")
for s_ in (2,3,5,100):
    for Dv in (50, 1000):
        for xv in (0.2, 0.5, 0.9):
            L = 10**7
            L -= L % (s_* 10)
            m = int(xv*L/s_)
            M = L*Dv//s_                       # number of edges
            # log #(m-matchings of s-sets in [L])
            lognum = lgamma(L+1) - m*lgamma(s_+1) - lgamma(m+1) - lgamma(L-s_*m+1)
            # log p^m, p = M / C(L,s)
            logC = lgamma(L+1)-lgamma(s_+1)-lgamma(L-s_+1)
            logp = math.log(M) - logC
            first_moment = lognum + m*logp
            lemma = m*(log(Dv/xv)-(s_-1)) - L*(1-xv)*log(1-xv)
            print(f"  s={s_:3d} D={Dv:5d} x={xv:.1f}:  first moment/L = {first_moment/L:+.8f}"
                  f"   lemma bound/L = {lemma/L:+.8f}   ratio = {first_moment/lemma:.8f}")

print("="*78); print("G. finite-N test of (1) on the extremal family: complete graph K_N (s=2, D=N-1)")
print("   a_m = N!/((N-2m)! m! 2^m)  exactly; bound = m(log(D/x)-1) - N(1-x)log(1-x)")
for N in (100, 1000, 10**4, 10**6, 10**8):
    for xv in (0.2, 0.6, 1.0):
        m = int(xv*N/2); xx = 2*m/N
        loga = lgamma(N+1)-lgamma(N-2*m+1)-lgamma(m+1)-m*log(2)
        D = N-1
        bnd = m*(log(D/xx)-1) - (N*(1-xx)*log(1-xx) if xx<1 else 0.0)
        print(f"  N={N:>9d} x={xx:.2f}: log a_m = {loga:.4f}  bound = {bnd:.4f}"
              f"  (bound-log a_m)/N = {(bnd-loga)/N:+.6f}  {'OK' if bnd>=loga else 'VIOLATED'}")

print("="*78); print("H. size of the o(N) error: how large must n be? (log10 arithmetic)")
# eps ~ x/D = x/n ; delta := int_0^1 log(u^{s-1}+eps)du + (s-1)  ~ (s-1)*eps^{1/(s-1)}
# the error in (1) is (L/s)*delta with L/s = m+u = N(x/s + 1 - x), and N = 100T
def delta(s_, eps, npts=200001):
    n_ = npts if npts%2 else npts+1; h=1.0/(n_-1); tot=0.0
    for i in range(n_):
        u = i*h; val = math.log(u**(s_-1)+eps)
        tot += (1 if i in (0,n_-1) else (4 if i%2 else 2))*val
    return tot*h/3 + (s_-1)
print("  check the asymptotic form of delta against the numerical integral, s=100:")
for eps in (1e-2, 1e-4, 1e-8):
    print(f"    eps={eps:.0e}: numeric delta = {delta(100,eps):10.6f}   (s-1)eps^(1/(s-1)) = {99*eps**(1/99):10.6f}")
LoverN = x/s + 1 - x
print(f"  (m+u)/N = {LoverN}")
for slack, name in [(0.2, "writeup's chain (needs o(N) <= 0.2T)"),
                    (abs(expo(x,s,c))-0.4, "using the true exponent")]:
    thr = slack/(100*LoverN*99)               # required eps^(1/99)
    log10eps = 99*math.log10(thr)
    log10n = math.log10(x) - log10eps
    print(f"  {name}: need eps^(1/99) < {thr:.4e} -> eps < 10^{log10eps:.1f} -> n > 10^{log10n:.1f}")
    print(f"      => |V(H)| = 100n ~ 10^{log10n+2:.0f}, |E(H_0)| = n^100 ~ 10^{100*log10n:.0f}")

print("="*78); print("I. section 4 asymptotics")
for d in (20, 50, 100, 1000):
    a = math.ceil(5*log(d)); xv = a/d
    val = xv*(2*log(d)-log(a)+1-a/2)
    print(f"  d={d:5d}: a={a:3d} x={xv:.5f}  exponent bound = {val:+.6f} {'<0 OK' if val<0 else 'FAIL'}"
          f"   chi >= ~ d^2/(5 log d) = {d*d/(5*log(d)):.1f}  vs conjectured 3d-1 = {3*d-1}")
