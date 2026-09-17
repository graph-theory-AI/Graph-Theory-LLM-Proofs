"""Plane-graph machinery for refereeing `finding_k_edge_outerplanar_graph_embeddings`.

Multigraphs are supported (edge list with repetitions).  An embedding is a
rotation system sigma (for each vertex, a cyclic order of its incident
half-edges).  Half-edge 2i is the end of edge i at its first endpoint,
2i+1 the end at its second endpoint; alpha(h) = h ^ 1.

Faces are the orbits of phi(h) = sigma[alpha(h)].  Genus 0 <=> V-E+F=2
(for connected graphs).
"""
import itertools
from collections import deque


class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = list(edges)
        self.m = len(self.edges)
        self.inc = [[] for _ in range(n)]
        for i, (u, v) in enumerate(self.edges):
            self.inc[u].append(2 * i)
            self.inc[v].append(2 * i + 1)

    def vertex_of(self, h):
        u, v = self.edges[h >> 1]
        return u if h % 2 == 0 else v

    def connected(self):
        if self.n == 0:
            return True
        adj = [[] for _ in range(self.n)]
        for (u, v) in self.edges:
            adj[u].append(v)
            adj[v].append(u)
        seen = {0}
        dq = deque([0])
        while dq:
            x = dq.popleft()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    dq.append(y)
        return len(seen) == self.n


class Embedding:
    """A genus-0 rotation system together with the induced face structure."""

    def __init__(self, g, sigma):
        self.g = g
        self.sigma = sigma           # dict half-edge -> next half-edge at same vertex
        self.face_of = {}            # half-edge -> face id
        faces = []
        for h in range(2 * g.m):
            if h in self.face_of:
                continue
            fid = len(faces)
            cyc = []
            x = h
            while x not in self.face_of:
                self.face_of[x] = fid
                cyc.append(x)
                x = sigma[x ^ 1]
            faces.append(cyc)
        self.faces = faces
        self.nf = len(faces)

    def genus0(self):
        return self.g.n - self.g.m + self.nf == 2

    def sides(self, e):
        return self.face_of[2 * e], self.face_of[2 * e + 1]

    def faces_at_vertex(self, v):
        return {self.face_of[h] for h in self.g.inc[v]}

    def dual_dist(self, root):
        """BFS distance in the face-adjacency multigraph from face `root`."""
        d = [None] * self.nf
        d[root] = 0
        dq = deque([root])
        adj = [[] for _ in range(self.nf)]
        for e in range(self.g.m):
            a, b = self.sides(e)
            if a != b:
                adj[a].append(b)
                adj[b].append(a)
        while dq:
            x = dq.popleft()
            for y in adj[x]:
                if d[y] is None:
                    d[y] = d[x] + 1
                    dq.append(y)
        return d

    def layers(self, root):
        d = self.dual_dist(root)
        out = {}
        for e in range(self.g.m):
            a, b = self.sides(e)
            out[e] = 1 + min(d[a], d[b])
        return out

    def K(self, root):
        """Edge-outerplanarity of this embedding with outer face `root`."""
        if self.g.m == 0:
            return 0
        return max(self.layers(root).values())

    def peel_rounds(self, root):
        """Independent simulation: repeatedly delete every edge lying on the
        current outer *region*, tracking which original faces have been
        absorbed into it.  Returns the number of rounds."""
        S = {root}
        remaining = set(range(self.g.m))
        rounds = 0
        while remaining:
            rounds += 1
            dele = [e for e in remaining
                    if self.sides(e)[0] in S or self.sides(e)[1] in S]
            assert dele, "no edge on the outer face -- region tracking broken"
            for e in dele:
                a, b = self.sides(e)
                S.add(a)
                S.add(b)
            remaining -= set(dele)
        return rounds


def rotation_systems(g):
    """Yield every rotation system of g (cyclic order at each vertex)."""
    per_vertex = []
    for v in range(g.n):
        inc = g.inc[v]
        d = len(inc)
        opts = []
        if d == 0:
            opts = [[]]
        else:
            first = inc[0]
            for perm in itertools.permutations(inc[1:]):
                opts.append([first] + list(perm))
        per_vertex.append(opts)
    for combo in itertools.product(*per_vertex):
        sigma = {}
        for order in combo:
            d = len(order)
            for i, h in enumerate(order):
                sigma[h] = order[(i + 1) % d]
        yield sigma


def embeddings(g):
    """All genus-0 embeddings (as Embedding objects)."""
    for sigma in rotation_systems(g):
        emb = Embedding(g, sigma)
        if emb.genus0():
            yield emb


def min_edge_outerplanarity(g, require_vertex=None, require_edge=None):
    """Brute force: min over all plane embeddings & outer faces of K.
    Optionally require a vertex / an edge to be incident with the outer face."""
    best = None
    for emb in embeddings(g):
        for r in range(emb.nf):
            if require_vertex is not None and r not in emb.faces_at_vertex(require_vertex):
                continue
            if require_edge is not None and r not in emb.sides(require_edge):
                continue
            k = emb.K(r)
            if best is None or k < best:
                best = k
    return best
