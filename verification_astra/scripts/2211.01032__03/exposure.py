"""Verify |H_d| = 2^{d-1}(d-1)! and the writeup's exposure lemma (1):
after exposing r pairs of V_u, the V_u-mate of a free flag x is UNIFORM over the
2(d-r-1) free flags other than x and the opposite endpoint of x's J u Q path."""
import itertools, collections


def perfect_matchings(pts):
    pts = list(pts)
    if not pts:
        yield ()
        return
    a = pts[0]
    for i in range(1, len(pts)):
        b = pts[i]
        rest = pts[1:i] + pts[i + 1:]
        for m in perfect_matchings(rest):
            yield ((a, b),) + m


def one_cycle(J, W, m):
    """is J u W a single 2m-cycle?"""
    adj = collections.defaultdict(list)
    for (a, b) in list(J) + list(W):
        adj[a].append(b); adj[b].append(a)
    start = 0; prev = None; cur = 0; cnt = 0
    while True:
        nxts = [x for x in adj[cur] if x != prev] or adj[cur]
        nxt = nxts[0]
        prev, cur = cur, nxt
        cnt += 1
        if cur == start:
            break
    return cnt == 2 * m


for d in (2, 3, 4, 5):
    pts = list(range(2 * d))
    J = tuple((2 * i, 2 * i + 1) for i in range(d))
    H = [W for W in perfect_matchings(pts) if one_cycle(J, W, d)]
    print(f"d={d}: |H_d|={len(H)}  predicted 2^(d-1)(d-1)! = "
          f"{2**(d-1) * __import__('math').factorial(d-1)}")

# exposure lemma, d=5, several exposure patterns
import math
d = 5
pts = list(range(2 * d))
J = tuple((2 * i, 2 * i + 1) for i in range(d))
H = [W for W in perfect_matchings(pts) if one_cycle(J, W, d)]
Hset = [frozenset(frozenset(p) for p in W) for W in H]


def paths(Q):
    """components of J u Q (Q a set of frozensets); returns dict flag->other endpoint"""
    adj = collections.defaultdict(list)
    for p in list(J) + [tuple(q) for q in Q]:
        a, b = p; adj[a].append(b); adj[b].append(a)
    ends = {}
    seen = set()
    for v in pts:
        if len(adj[v]) == 1 and v not in seen:
            cur, prev = v, None
            while True:
                seen.add(cur)
                nx = [x for x in adj[cur] if x != prev]
                if not nx:
                    break
                prev, cur = cur, nx[0]
            ends[v] = cur; ends[cur] = v
    return ends


tests = [[], [(0, 2)], [(0, 2), (4, 6)], [(0, 2), (3, 5), (7, 9)], [(1,3),(5,7),(9,0),(2,4)]]
for Qlist in tests:
    Q = frozenset(frozenset(p) for p in Qlist)
    cand = [W for W in Hset if Q <= W]
    covered = set().union(*[set(q) for q in Q]) if Q else set()
    free = [v for v in pts if v not in covered]
    ends = paths(Q)
    r = len(Q)
    for x in free[:2]:
        dist = collections.Counter()
        for W in cand:
            for p in W:
                if x in p:
                    dist[tuple(p - {x})[0]] += 1
        allowed = set(free) - {x, ends[x]}
        ok = (set(dist) == allowed) and (len(set(dist.values())) == 1)
        print(f"  Q(r={r})={sorted(tuple(sorted(q)) for q in Q)} x={x}: "
              f"support size {len(dist)} (predicted {2*(d-r-1)}), uniform={ok}")
