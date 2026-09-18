"""Section 8: the pendant-twin transformation makes R a matching and preserves OPT.

Exact brute force on small strong digraphs.  The transformed instance has
n + 2|R| vertices, so we cap that at TOTCAP (<= 9!) to keep the exhaustive
enumeration over enumerations feasible -- this is what the earlier run got wrong.
"""
import itertools, random, sys
from collections import defaultdict
from construction import realized, is_strong

TOTCAP = 9          # n + 2m  (9! = 362880 permutations per instance)

def opt(V, A, R):
    ml = sorted({x for r in R for x in r})
    best = 0
    for perm in itertools.permutations(V):
        v = realized(list(perm), A, ml, R)
        if v > best:
            best = v
            if best == len(R):
                break
    return best

def transform(V, A, R):
    V2 = list(V); A2 = list(A); R2 = []
    for k, (u, v) in enumerate(R):
        ur = ('n', k, 0); vr = ('n', k, 1)
        V2 += [ur, vr]
        A2 += [(ur, u), (u, ur), (vr, v), (v, vr)]
        R2.append((ur, vr))
    return V2, A2, R2

def run(trials, seed):
    rng = random.Random(seed); tested = 0; bad = 0; tot_nontrivial = 0
    while tested < trials:
        n = rng.randint(3, 5)
        m = rng.randint(1, 3)
        if n + 2*m > TOTCAP:
            continue
        V = list(range(n))
        A = [(u, v) for u in V for v in V if u != v and rng.random() < 0.45]
        if not A or not is_strong(V, A):
            continue
        pairs = [(u, v) for u in V for v in V if u < v]
        if len(pairs) < m:
            continue
        R = rng.sample(pairs, m)
        o1 = opt(V, A, R)
        V2, A2, R2 = transform(V, A, R)
        assert is_strong(V2, A2), 'transformed instance not strong'
        assert len({x for r in R2 for x in r}) == 2*len(R2), 'R2 not a matching'
        o2 = opt(V2, A2, R2)
        tested += 1
        if o1 < len(R):            # count instances where OPT<|R| (non-trivial ones)
            tot_nontrivial += 1
        if o1 != o2:
            bad += 1
            print('MISMATCH', V, A, R, 'OPT_old=', o1, 'OPT_new=', o2)
    return tested, bad, tot_nontrivial

if __name__ == '__main__':
    t, b, nt = run(400, 11)
    print(f"tested {t} random strong instances (n<=5, |R|<=3, n+2|R|<={TOTCAP});")
    print(f"  {nt} of them had OPT < |R| (so the equality is not vacuous);")
    print(f"  OPT mismatches after the matching transformation: {b}")
