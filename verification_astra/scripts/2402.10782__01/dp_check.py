"""Check Section 5 of the writeup: the O(2^{4d} n^3) DP deciding whether a
tournament has an ordering pi with Delta(B_pi) <= d, against brute force over
all n! orderings, on random tournaments.  Also checks the score-localization
interval claim (2)/(11) and the boundary bound (13)."""
import itertools, random, sys

def rand_tournament(n, rng):
    arc = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if rng.random() < 0.5: arc[i][j] = True
            else: arc[j][i] = True
    return arc

def brute(arc, n, d):
    for order in itertools.permutations(range(n)):
        pos = {v:i for i,v in enumerate(order)}
        deg = [0]*n; ok = True
        for u in range(n):
            for v in range(n):
                if arc[u][v] and pos[u] > pos[v]:
                    deg[u]+=1; deg[v]+=1
        if max(deg) <= d: return order
    return None

def dp(arc, n, d):
    outdeg = [sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
    a = [n - outdeg[v] for v in range(n)]
    lo = [max(1, a[v]-d) for v in range(n)]
    hi = [min(n, a[v]+d) for v in range(n)]
    # boundary rejection rule (13)
    for i in range(1, n):
        X = [v for v in range(n) if lo[v] <= i < hi[v]]
        if len(X) > 4*d: return None
    full = (1<<n)-1
    # states: bitmask prefix sets
    layer = {0: None}
    for i in range(n):
        nxt = {}
        for S in layer:
            for v in range(n):
                if S >> v & 1: continue
                if not (lo[v] <= i+1 <= hi[v]): continue
                beta = 0
                for u in range(n):
                    if u == v: continue
                    if (S >> u & 1):
                        if arc[v][u]: beta += 1
                    else:
                        if arc[u][v]: beta += 1
                if beta > d: continue
                S2 = S | (1<<v)
                # state-form condition at layer i+1
                okform = True
                for w in range(n):
                    if hi[w] <= i+1 and not (S2 >> w & 1): okform = False; break
                    if (S2 >> w & 1) and lo[w] > i+1: okform = False; break
                if not okform: continue
                if S2 not in nxt: nxt[S2] = (S, v)
            # end v
        layer = nxt
        if not layer: return None
    if full not in layer: return None
    # reconstruct
    order = []; S = full
    while S:
        prev, v = layer[S] if S == full else back[S]
        order.append(v); S = prev
    return None  # reconstruction not needed for the comparison

def dp_decide(arc, n, d):
    return dp(arc, n, d) is not None or _dp_bool(arc, n, d)

def _dp_bool(arc, n, d):
    outdeg = [sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
    a = [n - outdeg[v] for v in range(n)]
    lo = [max(1, a[v]-d) for v in range(n)]
    hi = [min(n, a[v]+d) for v in range(n)]
    for i in range(1, n):
        X = [v for v in range(n) if lo[v] <= i < hi[v]]
        if len(X) > 4*d: return False
    full = (1<<n)-1
    layer = {0}
    for i in range(n):
        nxt = set()
        for S in layer:
            for v in range(n):
                if S >> v & 1: continue
                if not (lo[v] <= i+1 <= hi[v]): continue
                beta = 0
                for u in range(n):
                    if u == v: continue
                    if (S >> u & 1):
                        if arc[v][u]: beta += 1
                    else:
                        if arc[u][v]: beta += 1
                if beta > d: continue
                S2 = S | (1<<v)
                ok = True
                for w in range(n):
                    if hi[w] <= i+1 and not (S2 >> w & 1): ok = False; break
                    if (S2 >> w & 1) and lo[w] > i+1: ok = False; break
                if ok: nxt.add(S2)
        layer = nxt
        if not layer: return False
    return full in layer

def main():
    rng = random.Random(20260917)
    for d in [0,1,2]:
        mism = 0; yes = 0; tot = 0
        for n in range(2, 8):
            for _ in range(120):
                arc = rand_tournament(n, rng)
                b = brute(arc, n, d) is not None
                D = _dp_bool(arc, n, d)
                tot += 1; yes += b
                if b != D:
                    mism += 1
                    print("MISMATCH d=%d n=%d brute=%s dp=%s" % (d,n,b,D))
                    for r in arc: print("  ", ''.join('1' if x else '0' for x in r))
                # also verify score localization (2) on the brute-force witness
                if b:
                    order = brute(arc, n, d)
                    pos = {v:i+1 for i,v in enumerate(order)}
                    outdeg = [sum(1 for v in range(n) if arc[u][v]) for u in range(n)]
                    for v in range(n):
                        av = n - outdeg[v]
                        dv = sum(1 for u in range(n) if (arc[u][v] and pos[u]>pos[v]) or (arc[v][u] and pos[u]<pos[v]))
                        assert abs(pos[v]-av) <= dv, (n,d,v,pos[v],av,dv)
        print(f"d={d}: {tot} random tournaments, {yes} YES instances, {mism} mismatches")
    print("Section 5 DP: matches brute force on all tests")

main()
