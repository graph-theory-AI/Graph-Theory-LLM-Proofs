"""Section 8, NON-VACUOUS test: the earlier random test only produced instances with
OPT = |R|, where preservation is trivial.  Here we use instances with OPT < |R|.

Instance family: bidirected star (centre c, leaves u,v,w), R = all 3 leaf pairs.
By the star/MAX-CUT correspondence OPT = MAXCUT(K_3) = 2 < 3 = |R|.
After the pendant-twin transformation the digraph has 10 vertices; we brute force all
10! = 3628800 enumerations.
"""
import itertools, sys
from collections import defaultdict
from construction import realized, is_strong

def opt_bruteforce(V, A, R, verbose_cap=None):
    ml = sorted({x for r in R for x in r}, key=repr)
    best = 0
    n = len(V)
    # pre-index
    idx = {v: i for i, v in enumerate(V)}
    arcs = [(idx[u], idx[v]) for u, v in A]
    midx = {idx[m]: k for k, m in enumerate(ml)}
    reqs = [(idx[x], idx[y]) for x, y in R]
    out = defaultdict(list)
    for u, v in arcs:
        out[u].append(v)
    for perm in itertools.permutations(range(n)):
        pos = [0]*n
        for i, v in enumerate(perm):
            pos[v] = i
        bits = [0]*n
        for i in range(n-1, -1, -1):
            v = perm[i]
            b = (1 << midx[v]) if v in midx else 0
            for w in out.get(v, ()):
                if pos[w] > i:
                    b |= bits[w]
            bits[v] = b
        c = 0
        for x, y in reqs:
            if (bits[x] >> midx[y]) & 1 or (bits[y] >> midx[x]) & 1:
                c += 1
        if c > best:
            best = c
            if best == len(R):
                return best
    return best

def transform(V, A, R):
    V2 = list(V); A2 = list(A); R2 = []
    for k, (u, v) in enumerate(R):
        ur = ('n', k, 0); vr = ('n', k, 1)
        V2 += [ur, vr]
        A2 += [(ur, u), (u, ur), (vr, v), (v, vr)]
        R2.append((ur, vr))
    return V2, A2, R2

if __name__ == '__main__':
    # bidirected star K_{1,3}
    V = ['c', 'u', 'v', 'w']
    A = []
    for x in ['u', 'v', 'w']:
        A += [('c', x), (x, 'c')]
    R = [('u', 'v'), ('u', 'w'), ('v', 'w')]
    assert is_strong(V, A)
    o1 = opt_bruteforce(V, A, R)
    print(f"original: |V|={len(V)} |R|={len(R)}  OPT={o1}   (MAXCUT(K_3)=2 expected)")
    V2, A2, R2 = transform(V, A, R)
    assert is_strong(V2, A2)
    assert len({x for r in R2 for x in r}) == 2*len(R2), "R2 is not a matching"
    print(f"transformed: |V|={len(V2)} |R|={len(R2)} (a matching); brute forcing {len(V2)}! enumerations ...")
    sys.stdout.flush()
    o2 = opt_bruteforce(V2, A2, R2)
    print(f"transformed OPT={o2}")
    print("PRESERVED" if o1 == o2 else "*** OPT NOT PRESERVED ***")

    # second family: bidirected star with 4 leaves, R = C_4 (MAXCUT=4=|R|, trivial)
    # and R = K_4 minus perfect matching? use R = triangle on 3 of the 4 leaves + one more
    V = ['c', 'u', 'v', 'w']
    A = [('c', x) for x in ['u', 'v', 'w']] + [(x, 'c') for x in ['u', 'v', 'w']]
    for R in ([('u','v'),('u','w')], [('u','v'),('v','w'),('u','w')]):
        o1 = opt_bruteforce(V, A, R)
        V2, A2, R2 = transform(V, A, R)
        o2 = opt_bruteforce(V2, A2, R2)
        print(f"  |R|={len(R)}: OPT_old={o1} OPT_new={o2} {'ok' if o1==o2 else '*** MISMATCH ***'}")
