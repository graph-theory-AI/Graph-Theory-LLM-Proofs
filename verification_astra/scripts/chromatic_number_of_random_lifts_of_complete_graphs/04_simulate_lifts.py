"""
Simulate random n-lifts of K_5 and test 3-colourability by exact search.
Also checks the short-cycle Poisson means claimed in the writeup:
   mu_3 = 10 (triangles), mu_4 = 15 (4-cycles), mu_5 = 12 (5-cycles),
and the claim that the lift is a.a.s. non-bipartite.

Colouring test: degree-<3 kernelization + MRV/forward-checking backtracking.
"""
import random, sys, itertools
from collections import defaultdict

def random_lift_K5(n, rng):
    """vertices (v,i), v in 0..4, i in 0..n-1; one uniform random matching per base edge."""
    N = 5*n
    idx = lambda v, i: v*n + i
    adj = [[] for _ in range(N)]
    for u, v in itertools.combinations(range(5), 2):
        perm = list(range(n)); rng.shuffle(perm)
        for i in range(n):
            a, b = idx(u, i), idx(v, perm[i])
            adj[a].append(b); adj[b].append(a)
    return N, [set(a) for a in adj]

def three_colourable(N, adj, node_limit=8_000_000):
    """exact 3-colourability via kernelization + backtracking. returns (bool, nodes)"""
    deg = [len(a) for a in adj]
    alive = [True]*N
    adj = [set(a) for a in adj]
    stack = [v for v in range(N) if deg[v] < 3]
    removed = []
    while stack:
        v = stack.pop()
        if not alive[v] or len(adj[v]) >= 3: continue
        alive[v] = False; removed.append(v)
        for w in list(adj[v]):
            adj[w].discard(v)
            if len(adj[w]) < 3 and alive[w]: stack.append(w)
        adj[v] = set()
    verts = [v for v in range(N) if alive[v]]
    if not verts: return True, 0
    dom = {v: 0b111 for v in verts}
    nbr = {v: [w for w in adj[v] if alive[w]] for v in verts}
    nodes = [0]

    def bt(dom):
        nodes[0] += 1
        if nodes[0] > node_limit: raise RuntimeError("node limit")
        # pick unassigned var with fewest options
        best, bv = 4, None
        for v in verts:
            c = bin(dom[v]).count("1")
            if c == 0: return False
            if c > 1 and c < best: best, bv = c, v
        if bv is None: return True
        for col in range(3):
            if not (dom[bv] >> col) & 1: continue
            nd = dict(dom); nd[bv] = 1 << col
            # forward check / unit propagation
            queue = [bv]; ok = True
            while queue and ok:
                x = queue.pop()
                cx = nd[x]
                if bin(cx).count("1") != 1: continue
                for y in nbr[x]:
                    if nd[y] & cx:
                        newy = nd[y] & ~cx
                        if newy == 0: ok = False; break
                        was = bin(nd[y]).count("1")
                        nd[y] = newy
                        if bin(newy).count("1") == 1 and was > 1: queue.append(y)
            if ok and bt(nd): return True
        return False
    try:
        return bt(dom), nodes[0]
    except RuntimeError:
        return None, nodes[0]

def counts(N, adj):
    tri = 0; c4 = 0; c5 = 0
    A = [sorted(a) for a in adj]
    S = [set(a) for a in adj]
    for v in range(N):
        for u in A[v]:
            if u <= v: continue
            tri += len(S[u] & S[v])
    tri //= 3
    # 4- and 5-cycles by brute force over short walks (N is small)
    for v in range(N):
        for a in S[v]:
            for b in S[a]:
                if b == v: continue
                for c in S[b]:
                    if c == a or c == v: continue
                    if v in S[c]: c4 += 1
                    for e in S[c]:
                        if e in (v, a, b): continue
                        if v in S[e]: c5 += 1
    return tri, c4//8, c5//10

if __name__ == "__main__":
    rng = random.Random(20260917)
    print(f"{'n':>4} {'|V|':>5} {'trials':>7} {'3-col':>6} {'frac':>7} {'avg tri':>8} {'avg C4':>7} {'avg C5':>7} {'bip':>4}")
    for n, trials in [(3, 400), (5, 400), (8, 300), (12, 300), (20, 200), (30, 150), (50, 100), (80, 60), (120, 40)]:
        ok = 0; bad = 0; unk = 0; t3 = t4 = t5 = 0; bip = 0
        for _ in range(trials):
            N, adj = random_lift_K5(n, rng)
            if n <= 30:
                a, b, c = counts(N, adj); t3 += a; t4 += b; t5 += c
            r, _ = three_colourable(N, adj)
            if r is True: ok += 1
            elif r is False: bad += 1
            else: unk += 1
            # bipartite test
            col = {}; isbip = True
            for s in range(N):
                if s in col: continue
                col[s] = 0; st = [s]
                while st:
                    x = st.pop()
                    for y in adj[x]:
                        if y not in col: col[y] = 1-col[x]; st.append(y)
                        elif col[y] == col[x]: isbip = False; st = []; break
                if not isbip: break
            bip += isbip
        print(f"{n:>4} {5*n:>5} {trials:>7} {ok:>6} {ok/trials:>7.3f} "
              f"{t3/trials if n<=30 else float('nan'):>8.3f} {t4/trials if n<=30 else float('nan'):>7.3f} "
              f"{t5/trials if n<=30 else float('nan'):>7.3f} {bip:>4}   (not3col={bad}, unknown={unk})",
              flush=True)
    print("\nwriteup's Poisson means: mu_3=10, mu_4=15, mu_5=12")
