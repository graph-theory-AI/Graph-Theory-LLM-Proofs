"""End-to-end test of the writeup's Section 5.1 block construction, INCLUDING
the composite-indexed progressions (bundles B_{p_i}(n) = {A_{a p_i}(n) : a}).

Every ingredient is instantiated literally:
  I_i = [S_i, S_i+W-1], S_i=(i-1)g, g=ceil(n(h(u)+nu)), W=n+ceil(Cx)+1   (5.1)
  forbidden arc = image of I_i cap I_j under z -> z/(p_i p_j) mod 1
  J_ij  : arc of length rho in the complement, >= 4 rho from the forbidden arc
  Lemma 3.1 : residues r_i with Z_ij(r_i,r_j) in J_ij   (found by search on a
              block verified to be CRT-generic up to frequency Hmax)
  Lemma 2.1 : greedy colouring of the unshifted A_a(N_i)
  Lemma 4.1 : Bohr set { s : ||inv(p_j) s / p_i|| < rho  for all j != i }
  shift of colour c of bundle i = S_i + t_{i,c},  t = r_i + s_{i,c} (mod p_i)
Then every shifted progression is expanded and pairwise disjointness is checked
by brute force, together with containment in an interval of size (k-1)g+W.
"""
import math, random, itertools, sys
from sympy import primerange

# ---------- Lemma 2.1 colouring ----------
def colour_bundle(N):
    root = math.isqrt(N)
    divs = [[] for _ in range(N+1)]
    for d in range(1, N+1):
        for m in range(d, N+1, d): divs[m].append(d)
    col = {a: a-1 for a in range(1, root+1)}
    big = list(range(root+1, N+1))
    adj = {a: set() for a in big}
    for a in big:
        for k in range(1, N//a+1):
            for b in divs[k*a]:
                if b > root and b != a and (a*b)//math.gcd(a, b) <= N:
                    adj[a].add(b)
    for a in sorted(big, key=lambda t: -len(adj[t])):
        used = {col[b] for b in adj[a] if b in col}
        c = root
        while c in used: c += 1
        col[a] = c
    return col

# ---------- Lemma 3.1 goodness test ----------
def is_good_block(ps, H):
    k = len(ps); pairs = [(i,j) for i in range(k) for j in range(i+1,k)]
    inv = {(i,j): pow(ps[j], -1, ps[i]) for i in range(k) for j in range(k) if i != j}
    for hv in itertools.product(range(-H, H+1), repeat=len(pairs)):
        if not any(hv): continue
        h = {}
        for (i,j), v in zip(pairs, hv): h[(i,j)] = v; h[(j,i)] = v
        if all(sum(h[(i,j)]*inv[(i,j)] for j in range(k) if j != i) % ps[i] == 0
               for i in range(k)):
            return False, hv
    return True, None

def run(n, ps, u, nu, C, rho, Hmax, seed=1):
    k = len(ps); x = math.isqrt(n); rnd = random.Random(seed)
    good, w = is_good_block(ps, Hmax)
    print(f"block {ps}: CRT-generic up to ||h||_inf<={Hmax}? {good} {'' if good else w}")
    assert good
    h = max(0.0, 1.0-u*u)
    g = math.ceil(n*(h+nu)); W = n + math.ceil(C*x) + 1
    S = [i*g for i in range(k)]
    assert all(p <= C*x for p in ps) and all(p >= u*x for p in ps)
    print(f"n={n} x={x} u={u} nu={nu} C={C} rho={rho}  g={g} W={W} span={(k-1)*g+W}")
    J = {}
    for i in range(k):
        for j in range(i+1, k):
            P = ps[i]*ps[j]
            a0, b0 = max(S[i],S[j]), min(S[i],S[j])+W-1
            L = b0-a0+1
            # (5.2): W-g <= min(u^2,1) n - nu n/2 <= p_i p_j - nu n /2
            assert W-g <= min(u*u,1.0)*n - nu*n/2 + 1, "(5.2) left inequality fails"
            assert min(u*u,1.0)*n <= P, "(5.2) right inequality fails"
            assert L < P
            flo = (a0 % P)/P; flen = (L-1)/P
            comp = 1.0-flen
            assert comp >= 9*rho, f"complement {comp:.4f} < 9rho={9*rho:.4f}"
            J[(i,j)] = ((flo+flen+4*rho) % 1.0, rho)
            print(f"  pair({i},{j}): |I_i^I_j|={L} period={P} forbidden={flen:.4f} complement={comp:.4f}")
    inv = {(i,j): pow(ps[j],-1,ps[i]) for i in range(k) for j in range(k) if i != j}
    def Z(i,j,ri,rj):
        P = ps[i]*ps[j]
        return ((ri*ps[j]*inv[(i,j)] + rj*ps[i]*inv[(j,i)]) % P)/P
    r = None
    for _ in range(3_000_000):
        cand = [rnd.randrange(p) for p in ps]
        if all(((Z(i,j,cand[i],cand[j]) - J[(i,j)][0]) % 1.0) < rho
               for i in range(k) for j in range(i+1,k)):
            r = cand; break
    assert r is not None, "Lemma 3.1 residues not found"
    print("  Lemma 3.1 residues r =", r)
    bohr = []
    for i in range(k):
        cs = [inv[(i,j)] for j in range(k) if j != i]
        B = [s for s in range(ps[i])
             if all(min((c*s) % ps[i], ps[i]-((c*s) % ps[i]))/ps[i] < rho for c in cs)]
        bohr.append(B)
    occupied = {}; npts = 0
    for i in range(k):
        Ni = n//ps[i]
        col = colour_bundle(Ni); ncol = len(set(col.values()))
        print(f"  bundle p={ps[i]}: N_i={Ni}  R(N_i)={ncol}  |Bohr|={len(bohr[i])}")
        assert ncol <= len(bohr[i]), "Lemma 4.1 does not supply enough residues"
        cmap = {c: bohr[i][t] for t, c in enumerate(sorted(set(col.values())))}
        for a in range(1, Ni+1):
            t = (r[i] + cmap[col[a]] - S[i]) % ps[i]
            shift = S[i] + t; d = a*ps[i]
            for m in range(d, n+1, d):
                z = shift + m; npts += 1
                if z in occupied:
                    sys.exit(f"*** COLLISION at {z}: {occupied[z]} vs (bundle {i}, d={d})")
                occupied[z] = (i, d)
    lo, hi = min(occupied), max(occupied)
    assert hi-lo+1 <= (k-1)*g+W
    print(f"  PASS: {npts} points, all pairwise disjoint; occupied span {hi-lo+1} <= {(k-1)*g+W}")

if __name__ == "__main__":
    # bin u in [1.5,1.6] (so h(u)=0), C=2, k=3, all three host windows overlap.
    run(n=10**8, ps=[15013,15511,15991], u=1.5, nu=0.10, C=2.0, rho=0.06, Hmax=25, seed=11)
