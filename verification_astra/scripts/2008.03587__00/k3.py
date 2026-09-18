"""Exact z(G) for k=3 using unordered zombie triples (state space ~2.1M)."""
import sys, itertools
from collections import deque
from array import array
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/2008.03587__00')
from zgame import all_dist
from counterexample import build, G, H, gn, hn

def solve3(adj, k=3):
    n = len(adj); dist = all_dist(adj)
    nbc = [sorted(set(adj[v]) | {v}) for v in range(n)]
    combos = list(itertools.combinations_with_replacement(range(n), k))
    cid = {c: i for i, c in enumerate(combos)}
    M = len(combos); size = M * n
    Zwin = bytearray(size); Swin = bytearray(size); cnt = bytearray(size)
    qZ, qS = deque(), deque()
    for ci, c in enumerate(combos):
        base = ci * n; zset = set(c)
        dz = [dist[z] for z in c]
        for s in range(n):
            if min(dd[s] for dd in dz) <= 1:
                Zwin[base + s] = 1; qZ.append(base + s)
            if s not in zset:
                cnt[base + s] = sum(1 for t in nbc[s] if t not in zset)
                if cnt[base + s] == 0:
                    Swin[base + s] = 1; qS.append(base + s)
    while qZ or qS:
        while qZ:
            st = qZ.popleft(); t = st % n; ci = st // n; c = combos[ci]
            zset = set(c)
            if t in zset: continue
            base = ci * n
            for s in nbc[t]:
                if s in zset: continue
                i = base + s
                if Swin[i]: continue
                cnt[i] -= 1
                if cnt[i] == 0:
                    Swin[i] = 1; qS.append(i)
        while qS:
            st = qS.popleft(); s = st % n; ys = combos[st // n]
            preds = []
            ok = True
            for y in ys:
                dy = dist[y][s]
                pr = [x for x in adj[y] if dist[x][s] == dy + 1]
                if not pr: ok = False; break
                preds.append(pr)
            if not ok: continue
            seen = set()
            for xs in itertools.product(*preds):
                key = tuple(sorted(xs))
                if key in seen: continue
                seen.add(key)
                i = cid[key] * n + s
                if not Zwin[i]:
                    Zwin[i] = 1; qZ.append(i)
    wins = [c for ci, c in enumerate(combos) if all(Zwin[ci * n + s] for s in range(n))]
    return wins

w = solve3(G)
print("G: number of winning 3-zombie placements:", len(w))
print("examples:", [tuple(gn[x] for x in p) for p in w[:5]])
