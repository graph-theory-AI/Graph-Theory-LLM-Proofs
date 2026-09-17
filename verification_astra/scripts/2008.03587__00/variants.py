"""Convention-robustness: does the counterexample survive rule variants?"""
import sys, itertools
from collections import deque
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/2008.03587__00')
from zgame import winning_placements, all_dist
from counterexample import build, G, H, gn, hn

# --- variant 1: survivor must move (may not stay put) -----------------------
for name, adj in (("G", G), ("H", H)):
    for k in (1, 2):
        w = winning_placements(adj, k, survivor_may_stay=False, limit=3)
        print(f"[survivor must move] {name}: k={k} -> {len(w)} winning placements"
              + ("" if not w else " e.g. " + str([tuple((gn if name=='G' else hn)[x] for x in p) for p in w])))

# --- variant 2: SURVIVOR moves first, then zombies --------------------------
def solve_survivor_first(adj, k):
    n = len(adj); dist = all_dist(adj)
    nbc = [sorted(set(adj[v]) | {v}) for v in range(n)]
    pw = [n ** i for i in range(k + 1)]
    # S-node (z, s): survivor to move.  Z-node (z, s): zombies to move.
    Swin = bytearray(n ** (k + 1)); Zwin = bytearray(n ** (k + 1))
    cntS = [0] * (n ** (k + 1))
    qZ, qS = deque(), deque()
    for zs in itertools.product(range(n), repeat=k):
        base = sum(z * pw[i + 1] for i, z in enumerate(zs)); zset = set(zs)
        for s in range(n):
            if min(dist[z][s] for z in zs) <= 1:
                if not Zwin[base + s]:
                    Zwin[base + s] = 1; qZ.append(base + s)
            if s in zset:
                if not Swin[base + s]:
                    Swin[base + s] = 1; qS.append(base + s)
            else:
                cntS[base + s] = sum(1 for t in nbc[s] if t not in zset)
                if cntS[base + s] == 0:
                    Swin[base + s] = 1; qS.append(base + s)
    def effZ(st):  # Zwin(z,t) -> survivor-node (z,s) with t in N[s]
        t = st % n; zb = st - t
        zs = [(zb // pw[i + 1]) % n for i in range(k)]; zset = set(zs)
        if t in zset: return
        for s in nbc[t]:
            if s in zset: continue
            i = zb + s
            if Swin[i]: continue
            cntS[i] -= 1
            if cntS[i] == 0:
                Swin[i] = 1; qS.append(i)
    def effS(st):  # Swin(y,s) -> Z-node (x,s) that can move to y
        s = st % n
        ys = [(st // pw[i + 1]) % n for i in range(k)]
        preds = []
        for y in ys:
            dy = dist[y][s]
            pr = [x for x in adj[y] if dist[x][s] == dy + 1]
            if not pr: return
            preds.append(pr)
        for xs in itertools.product(*preds):
            i = sum(x * pw[j + 1] for j, x in enumerate(xs)) + s
            if not Zwin[i]: Zwin[i] = 1; qZ.append(i)
    while qZ or qS:
        while qZ: effZ(qZ.popleft())
        while qS: effS(qS.popleft())
    return Swin, pw, n   # game starts with the survivor to move

for name, adj, nm in (("G", G, gn), ("H", H, hn)):
    for k in (1, 2):
        Swin, pw, n = solve_survivor_first(adj, k)
        found = []
        for zs in itertools.combinations_with_replacement(range(n), k):
            base = sum(z * pw[i + 1] for i, z in enumerate(zs))
            if all(Swin[base + s] for s in range(n)):
                found.append(tuple(nm[x] for x in zs))
                if len(found) >= 3: break
        print(f"[survivor moves first] {name}: k={k} -> {len(found)} winning placements"
              + ("" if not found else " e.g. " + str(found)))
