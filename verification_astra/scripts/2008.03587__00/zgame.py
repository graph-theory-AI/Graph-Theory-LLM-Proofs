"""Exact deterministic-zombie solver (independent re-implementation).

Rules (FHMP16 / arXiv:2008.03587, as stated in the writeup under review):
  * zombies pick their start vertices first, then the survivor picks;
  * a round = all zombies move simultaneously, EACH zombie MUST step to a
    neighbour strictly closer to the survivor's current vertex (the zombie
    player chooses which geodesic direction: "deterministic" version);
  * if a zombie lands on the survivor -> capture;
  * then the survivor moves to a neighbour or stays (stepping onto a zombie
    = capture);
  * survivor wins by evading forever.
z(G) = min k such that some k-placement beats EVERY survivor start.

Solved exactly as a finite reachability game by attractor computation with
predecessor counters (no iteration-to-fixpoint heuristics).
"""
from collections import deque
from array import array
import itertools


def bfs(adj, src, n):
    d = [-1] * n
    d[src] = 0
    q = deque([src])
    while q:
        u = q.popleft()
        for w in adj[u]:
            if d[w] < 0:
                d[w] = d[u] + 1
                q.append(w)
    return d


def all_dist(adj):
    n = len(adj)
    return [bfs(adj, v, n) for v in range(n)]


def solve(adj, k, survivor_may_stay=True):
    """Return (Zwin, n): Zwin[state] for state = zombie tuple + survivor,
    encoded base-n, zombie-to-move."""
    n = len(adj)
    dist = all_dist(adj)
    nb_closed = [sorted(set(adj[v]) | ({v} if survivor_may_stay else set()))
                 for v in range(n)]
    size = n ** (k + 1)
    Zwin = bytearray(size)
    cntS = [0] * size
    Swin = bytearray(size)

    pw = [n ** i for i in range(k + 1)]  # pw[0] multiplies survivor slot

    def enc(zs, s):
        v = s
        for i, z in enumerate(zs):
            v += z * pw[i + 1]
        return v

    queueZ = deque()
    # --- initialise Z-terminals: some zombie at distance <= 1 from survivor
    for zs in itertools.product(range(n), repeat=k):
        base = sum(z * pw[i + 1] for i, z in enumerate(zs))
        for s in range(n):
            if min(dist[z][s] for z in zs) <= 1:
                Zwin[base + s] = 1
                queueZ.append(base + s)
    # --- initialise S-node counters
    for zs in itertools.product(range(n), repeat=k):
        base = sum(z * pw[i + 1] for i, z in enumerate(zs))
        zset = set(zs)
        for s in range(n):
            if s in zset:
                continue
            cntS[base + s] = sum(1 for t in nb_closed[s] if t not in zset)

    queueS = deque()
    # S-nodes with no legal survivor response at all are immediate zombie wins
    for zs in itertools.product(range(n), repeat=k):
        base = sum(z * pw[i + 1] for i, z in enumerate(zs))
        zset = set(zs)
        for s in range(n):
            if s not in zset and cntS[base + s] == 0 and not Swin[base + s]:
                Swin[base + s] = 1
                queueS.append(base + s)

    def push_Zwin_effects(st):
        # st = (y, t) with Zwin true; decrement every S-node (y, s) with t in N[s]
        t = st % n
        ybase = st - t
        ys = [(ybase // pw[i + 1]) % n for i in range(k)]
        yset = set(ys)
        if t in yset:
            return  # such t were never counted
        for s in nb_closed[t]:           # t in N[s] <=> s in N[t] (closed, symmetric)
            if s in yset:
                continue
            idx = ybase + s
            if Swin[idx]:
                continue
            cntS[idx] -= 1
            if cntS[idx] == 0:
                Swin[idx] = 1
                queueS.append(idx)

    def push_Swin_effects(st):
        # st = (y, s) with Swin true; every Z-node (x, s) that can move to y wins
        s = st % n
        ys = [(st // pw[i + 1]) % n for i in range(k)]
        preds = []
        for i in range(k):
            y = ys[i]
            dy = dist[y][s]
            preds.append([x for x in adj[y] if dist[x][s] == dy + 1])
            if not preds[-1]:
                return
        for xs in itertools.product(*preds):
            idx = sum(x * pw[i + 1] for i, x in enumerate(xs)) + s
            if not Zwin[idx]:
                Zwin[idx] = 1
                queueZ.append(idx)

    while queueZ or queueS:
        while queueZ:
            push_Zwin_effects(queueZ.popleft())
        while queueS:
            push_Swin_effects(queueS.popleft())
    return Zwin, n, pw


def winning_placements(adj, k, survivor_may_stay=True, limit=None):
    Zwin, n, pw = solve(adj, k, survivor_may_stay)
    out = []
    for zs in itertools.combinations_with_replacement(range(n), k):
        base = sum(z * pw[i + 1] for i, z in enumerate(zs))
        if all(Zwin[base + s] for s in range(n)):
            out.append(zs)
            if limit and len(out) >= limit:
                break
    return out


def zombie_number(adj, kmax=3, survivor_may_stay=True):
    for k in range(1, kmax + 1):
        if winning_placements(adj, k, survivor_may_stay, limit=1):
            return k
    return None
