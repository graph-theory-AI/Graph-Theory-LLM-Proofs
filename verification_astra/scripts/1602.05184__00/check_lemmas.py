"""Machine check of the lemmas in attacks_retry/1602.05184__00/output.md.

Enumerates all 2-connected graphs of a given order (graph6 on stdin, from nauty geng)
and checks, step by step, the statements the writeup relies on.
"""
import sys
from itertools import combinations
from collections import deque

def parse_g6(line):
    line = line.strip()
    n = ord(line[0]) - 63
    bits = []
    for ch in line[1:]:
        v = ord(ch) - 63
        bits.extend((v >> k) & 1 for k in range(5, -1, -1))
    adj = [set() for _ in range(n)]
    idx = 0
    for j in range(1, n):
        for i in range(j):
            if bits[idx]:
                adj[i].add(j); adj[j].add(i)
            idx += 1
    return n, adj

def dists(n, adj):
    D = []
    for s in range(n):
        d = [-1]*n; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            for u in adj[v]:
                if d[u] < 0:
                    d[u] = d[v]+1; q.append(u)
        D.append(d)
    return D

def edges(n, adj):
    return [(u, v) for u in range(n) for v in adj[u] if u < v]

def good_edges(D, E, a, b):
    out = []
    for (u, v) in E:
        if (D[a][u] < D[a][v] and D[b][v] < D[b][u]) or (D[a][v] < D[a][u] and D[b][u] < D[b][v]):
            out.append((u, v))
    return out

class G:
    def __init__(self, n, adj):
        self.n, self.adj = n, adj
        self.D = dists(n, adj)
        self.E = edges(n, adj)
        self.Dm = {}
        for a, b in combinations(range(n), 2):
            self.Dm[(a, b)] = len(good_edges(self.D, self.E, a, b)) - self.D[a][b]
    def Dpair(self, a, b):
        return self.Dm[(a, b)] if a < b else self.Dm[(b, a)]
    def c(self, a):
        return sum(self.Dpair(a, b) for b in range(self.n) if b != a)
    def eta(self):
        return sum(self.Dm.values())
    def eta_direct(self):
        W = sum(self.D[a][b] for a, b in combinations(range(self.n), 2))
        Sz = 0
        for (u, v) in self.E:
            nu = sum(1 for w in range(self.n) if self.D[w][u] < self.D[w][v])
            nv = sum(1 for w in range(self.n) if self.D[w][v] < self.D[w][u])
            Sz += nu*nv
        return Sz - W
    def q(self, u):
        tot = 0
        inc = [e for e in self.E if u in e]
        for a, b in combinations([x for x in range(self.n) if x != u], 2):
            ge = good_edges(self.D, self.E, a, b)
            tot += sum(1 for e in inc if e in ge)
        return tot

def is_2connected(n, adj):
    if n < 3: return False
    def conn(verts):
        verts = set(verts)
        if not verts: return True
        s = next(iter(verts)); seen = {s}; q = deque([s])
        while q:
            v = q.popleft()
            for u in adj[v]:
                if u in verts and u not in seen:
                    seen.add(u); q.append(u)
        return seen == verts
    if not conn(range(n)): return False
    for v in range(n):
        if not conn([x for x in range(n) if x != v]): return False
    return True

def induced(n, adj, keep):
    keep = sorted(keep); idx = {v: i for i, v in enumerate(keep)}
    a2 = [set() for _ in keep]
    for v in keep:
        for u in adj[v]:
            if u in idx: a2[idx[v]].add(idx[u])
    return len(keep), a2

def connected_sub(adj, S):
    S = set(S)
    if not S: return True
    s = next(iter(S)); seen = {s}; q = deque([s])
    while q:
        v = q.popleft()
        for u in adj[v]:
            if u in S and u not in seen:
                seen.add(u); q.append(u)
    return seen == S

def type_of(g, a):
    """Return 'I', 'II' or None according to Lemma 3.1's classification."""
    n, adj = g.n, g.adj
    A = adj[a]
    Out = set(range(n)) - A - {a}
    if any(g.D[a][v] > 2 for v in range(n)):
        return None
    # Type I
    for z in Out:
        NzA = adj[z] & A
        if len(NzA) != 2: continue
        p, q = tuple(NzA)
        if q not in adj[p]: continue
        X = Out - {z}
        if not X:
            return 'I'
        for (pp, qq) in ((p, q), (q, p)):
            if all((adj[x] & A) == {pp} for x in X) and connected_sub(adj, X) \
               and sum(1 for x in X if x in adj[z]) == 1:
                return 'I'
    # Type II
    for p in A:
        for q in A:
            if p >= q: continue
            X = {x for x in Out if (adj[x] & A) == {p}}
            Y = {y for y in Out if (adj[y] & A) == {q}}
            if not X or not Y or X | Y != Out: continue
            if not connected_sub(adj, X) or not connected_sub(adj, Y): continue
            cross = sum(1 for x in X for y in Y if y in adj[x])
            if cross == 1:
                return 'II'
    return None

def exceptional(n, adj):
    m = sum(len(a) for a in adj)//2
    full = n*(n-1)//2
    if m == full or m == full-1: return True
    for v in range(n):
        if len(adj[v]) == 2:
            rest = [x for x in range(n) if x != v]
            if all(y in adj[x] for x, y in combinations(rest, 2)): return True
    return False

def induced_counts(n, adj):
    """(#induced P3, #induced P4, #induced C4, #nonedges)"""
    p3 = p4 = c4 = 0
    nm = 0
    for u, v in combinations(range(n), 2):
        if v not in adj[u]: nm += 1
    for trip in combinations(range(n), 3):
        e = [(x, y) for x, y in combinations(trip, 2) if y in adj[x]]
        if len(e) == 2: p3 += 1
    for quad in combinations(range(n), 4):
        e = [(x, y) for x, y in combinations(quad, 2) if y in adj[x]]
        if len(e) == 3:
            deg = {v: 0 for v in quad}
            for x, y in e: deg[x] += 1; deg[y] += 1
            if sorted(deg.values()) == [1, 1, 2, 2]: p4 += 1
        elif len(e) == 4:
            deg = {v: 0 for v in quad}
            for x, y in e: deg[x] += 1; deg[y] += 1
            if sorted(deg.values()) == [2, 2, 2, 2]: c4 += 1
    return p3, p4, c4, nm

C5 = None
def is_C5(n, adj):
    return n == 5 and all(len(adj[v]) == 2 for v in range(n))

fails = {}


def fail(tag, line, extra=""):
    fails.setdefault(tag, []).append((line, extra))

def main():
    count = 0
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        n, adj = parse_g6(line)
        count += 1
        g = G(n, adj)
        eta = g.eta()
        # (A) identity eta = sum D  == Sz - W
        if eta != g.eta_direct(): fail("A_eta_identity", line)
        exc = exceptional(n, adj)
        # main theorem
        if not exc and eta < min(2*n, 3*n-10): fail("THEOREM", line, f"eta={eta}")
        universal = [v for v in range(n) if len(adj[v]) == n-1]
        # (C) Lemma 3.1 structure + c(a)>=2
        for a in range(n):
            ca = g.c(a)
            if a not in universal:
                if ca < 2: fail("L3.1_(4)_c>=2", line, f"a={a},c={ca}")
                if ca <= 3:
                    t = type_of(g, a)
                    if t is None: fail("L3.1_structure", line, f"a={a},c={ca}")
        # (G) Lemma 5.1 identity for diam<=2
        diam = max(g.D[i][j] for i in range(n) for j in range(n))
        if diam <= 2:
            p3, p4, c4, nm = induced_counts(n, adj)
            if eta != 2*(p3-nm)+p4+4*c4: fail("L5.1_identity", line, f"eta={eta}")
        # (B) Lemma 2.1(3),(4) for dominated vertices
        for u in range(n):
            doms = [v for v in range(n) if v != u and (adj[u] | {u}) <= (adj[v] | {v})]
            if not doms: continue
            nn, a2 = induced(n, adj, [x for x in range(n) if x != u])
            h = G(nn, a2)
            qu = g.q(u)
            if eta - h.eta() != g.c(u) + qu: fail("L2.1_(3)", line, f"u={u}")
            simplicial = all(y in adj[x] for x, y in combinations(adj[u], 2))
            if simplicial and qu != 0: fail("L2.1_(4a)", line, f"u={u}")
            if not simplicial and qu < 2: fail("L2.1_(4b)", line, f"u={u}")
            if simplicial and not is_2connected(nn, a2): fail("simplicial_del_2conn", line, f"u={u}")
        if not universal:
            low = [a for a in range(n) if g.c(a) <= 3]
            # (E) Lemma 4.2
            for a in low:
                if all(y in adj[x] for x, y in combinations(adj[a], 2)) and eta < 2*n:
                    fail("L4.2", line, f"a={a},eta={eta}")
            # (D) Lemma 4.1 and (F) Prop 4.3
            if low and not is_C5(n, adj):
                ok41 = False; ok43 = False
                for u in range(n):
                    doms = [v for v in range(n) if v != u and (adj[u] | {u}) <= (adj[v] | {v})]
                    if not doms: continue
                    nn, a2 = induced(n, adj, [x for x in range(n) if x != u])
                    if not is_2connected(nn, a2): continue
                    ok41 = True
                    if eta - G(nn, a2).eta() >= 4: ok43 = True
                if not ok41: fail("L4.1", line)
                if eta < 2*n and not ok43: fail("P4.3", line, f"eta={eta}")

    print(f"checked {count} graphs on n={n}")
    if not fails:
        print("ALL CHECKS PASSED")
    else:
        for k, v in fails.items():
            print(f"FAIL {k}: {len(v)} instances, e.g. {v[:3]}")


if __name__ == "__main__":
    main()
