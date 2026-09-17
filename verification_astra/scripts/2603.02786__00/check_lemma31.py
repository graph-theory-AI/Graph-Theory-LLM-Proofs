"""Lemma 3.1 (generic prime blocks).  Two independent checks:
 (a) the Fourier/congruence criterion: is there a nonzero h, ||h||_inf<=H, with
     sum_{j!=i} h_ij * inv(p_j) = 0 (mod p_i) for every i?   (=> "bad" block)
 (b) direct: exact count of residue vectors (r_1..r_k) realising k(k-1)/2
     prescribed arcs of length rho, compared with the heuristic rho^E * prod p_i.
"""
import itertools, math, random
import numpy as np
from sympy import primerange

def bad_h(ps, H):
    k = len(ps)
    pairs = [(i,j) for i in range(k) for j in range(i+1,k)]
    inv = {(i,j): pow(ps[j], -1, ps[i]) for i in range(k) for j in range(k) if i!=j}
    found = []
    for hv in itertools.product(range(-H,H+1), repeat=len(pairs)):
        if all(v==0 for v in hv): continue
        h = {}
        for (i,j),v in zip(pairs,hv): h[(i,j)] = v; h[(j,i)] = v
        if all(sum(h[(i,j)]*inv[(i,j)] for j in range(k) if j!=i) % ps[i] == 0
               for i in range(k)):
            found.append(hv)
    return found

def exact_count(ps, arcs, rho):
    """k=3 only: exact number of (r0,r1,r2) with Z_ij in arcs[(i,j)] (length rho)."""
    p0,p1,p2 = ps
    def zset(pa, pb, lo):
        """residue pairs (ra,rb) with z/(pa*pb) in [lo,lo+rho): return array of z"""
        P = pa*pb
        start = int(math.ceil(lo*P)); ln = int(rho*P)
        return (np.arange(start, start+ln) % P)
    z01 = zset(p0,p1,arcs[(0,1)]); z02 = zset(p0,p2,arcs[(0,2)]); z12 = zset(p1,p2,arcs[(1,2)])
    r01 = np.stack([z01 % p0, z01 % p1])
    r02 = np.stack([z02 % p0, z02 % p2])
    r12 = np.stack([z12 % p1, z12 % p2])
    # index by r0
    tot = 0
    from collections import defaultdict
    d01 = defaultdict(list); d02 = defaultdict(list)
    for a,b in zip(r01[0], r01[1]): d01[a].append(b)
    for a,b in zip(r02[0], r02[1]): d02[a].append(b)
    s12 = set(zip(r12[0].tolist(), r12[1].tolist()))
    for r0 in d01:
        if r0 not in d02: continue
        for r1 in d01[r0]:
            for r2 in d02[r0]:
                if (r1,r2) in s12: tot += 1
    return tot, len(z01)*len(z02)*len(z12)/(p0*p1*p2)*1.0

if __name__ == "__main__":
    rnd = random.Random(0)
    print("== (a) bad-block test, k=3, H=3, primes in [6000,7000] ==")
    P = list(primerange(6000,7000))
    nbad = 0; ntr = 0
    for _ in range(40):
        ps = sorted(rnd.sample(P,3)); ntr += 1
        f = bad_h(ps,3)
        if f: nbad += 1; print("  BAD block", ps, "witness h =", f[:3])
    print(f"  bad blocks: {nbad}/{ntr}")

    print("== (b) exact realisability count for the block used in the packing test ==")
    ps = [6007,6011,6029]
    rho = 0.03
    for trial in range(6):
        arcs = {(0,1): rnd.random(), (0,2): rnd.random(), (1,2): rnd.random()}
        got, expect = exact_count(ps, arcs, rho)
        print(f"  arcs={ {k:round(v,4) for k,v in arcs.items()} }  exact#={got}"
              f"  heuristic rho^3*p0p1p2={expect*ps[0]*ps[1]*ps[2]:.0f}")
