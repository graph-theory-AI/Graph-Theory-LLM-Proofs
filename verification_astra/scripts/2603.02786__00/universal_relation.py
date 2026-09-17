"""For ANY triple p0<p1<p2 put d1=p1-p0, d2=p2-p0, d3=p2-p1.
Then h=(h01,h02,h12)=(d1,-d2,d3) satisfies ALL the congruences of (3.4):
   sum_{j!=i} h_ij * inv(p_j) mod p_i == 0   for every i.
So every triple is 'bad' at frequency ||h||_inf ~ p2-p0.  Lemma 3.1 is therefore
only true because H = H(k,eta) is FIXED while the primes spread over [aX,bX]:
close triples (differences <= H) are exactly the bounded set of bad tuples it
discards.  Verified below on random triples."""
from sympy import primerange
import random, math
P = list(primerange(10**4, 10**4+3000))
rnd = random.Random(0)
worst = 0
for _ in range(300):
    p0,p1,p2 = sorted(rnd.sample(P,3))
    d1,d2,d3 = p1-p0, p2-p0, p2-p1
    g = math.gcd(math.gcd(d1,d2),d3)
    h = {(0,1): d1//g, (0,2): -d2//g, (1,2): d3//g}
    h.update({(j,i): v for (i,j),v in list(h.items())})
    ps=[p0,p1,p2]
    ok = all(sum(h[(i,j)]*pow(ps[j],-1,ps[i]) for j in range(3) if j!=i) % ps[i] == 0
             for i in range(3))
    assert ok, (p0,p1,p2)
    worst = max(worst, max(abs(v) for v in h.values()))
print("universal relation verified on 300 random triples; max ||h||_inf seen =", worst)
# and it is the ONLY obstruction at small H for well separated primes:
def bad_h_upto(ps,H):
    import itertools
    inv={(i,j):pow(ps[j],-1,ps[i]) for i in range(3) for j in range(3) if i!=j}
    out=[]
    for hv in itertools.product(range(-H,H+1),repeat=3):
        if not any(hv): continue
        h={(0,1):hv[0],(0,2):hv[1],(1,2):hv[2]}
        h.update({(j,i):v for (i,j),v in list(h.items())})
        if all(sum(h[(i,j)]*inv[(i,j)] for j in range(3) if j!=i)%ps[i]==0 for i in range(3)):
            out.append(hv)
    return out
for ps in ([6007,6011,6029],[6007,6373,6997],[6113,6521,6959]):
    print(ps, "bad h with ||h||<=12:", bad_h_upto(ps,12))
