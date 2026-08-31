```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "For every old vertex away from the crowned pentagon, criticality is equivalent to a precise (2,2,1) terminal-coloring condition on an associated cubic five-pole, and the 40-vertex dodecahedral corona is exhaustively verified to be vertex-critical.",
  "would_publish": false,
  "caveats": "The universal five-pole extension property remains unproved, and the catalog alternates between an existential and a universal formulation."
}
```

# 1. Statement and interpretation

The catalog gives two inequivalent formulations:

1. every graph produced by the corona construction is 4-vertex-critical;  
2. infinitely many corona graphs are 4-vertex-critical.

I address the stronger, apparently intended, universal assertion.

I use the following combinatorial description of the corona construction from the source. Let \(G_0\) be a \(\triangle\)-saturated arrangement graph, with the triangular faces chosen as one checkerboard class. Then \(G_0\) is the medial graph, and abstractly the line graph, of a cubic plane graph \(H\). A pentagonal face of \(G_0\) corresponds to a pentagonal face
\[
f=v_0v_1v_2v_3v_4
\]
of \(H\). Write
\[
b_i=v_iv_{i+1},\qquad a_i=v_iw_i,
\]
with indices modulo \(5\), where \(a_i\) is the third edge at \(v_i\).

In \(L(H)\), the three vertices
\[
b_{i-1},a_i,b_i
\]
form a triangle. The corona replaces
\[
b_{i-1}a_i\quad\text{by}\quad b_{i-1}x_i a_i
\]
and
\[
a_ib_i\quad\text{by}\quad a_i y_i b_i,
\]
and adds the decagonal cycle
\[
x_0y_0x_1y_1\cdots x_4y_4x_0.
\]
Thus
\[
\{a_i,x_i,y_i\},\qquad \{b_i,y_i,x_{i+1}\}
\]
are triangles, while the edges \(b_ib_{i+1}\) remain.

Everything below applies to this explicitly defined graph operation.

# 2. A preliminary point about “edge-critical”

There is an elementary implication that should be checked against the last sentence of the source abstract.

**Lemma 2.1.**  
Suppose \(G\) has no isolated vertices, \(\chi(G)=k\), and
\[
\chi(G-e)\le k-1
\]
for every edge \(e\). Then \(G\) is \(k\)-vertex-critical.

**Proof.** For any vertex \(v\), choose an incident edge \(e\). Then
\[
G-v\subseteq G-e,
\]
and hence \(\chi(G-v)\le k-1\). ∎

Consequently, if the “4-edge-critical” graphs mentioned in the abstract mean edge-critical with respect to ordinary vertex chromatic number, and if they are corona arrangement graphs, then they are automatically 4-vertex-critical. The excerpt only calls them planar graphs, not arrangement graphs, so this does not by itself resolve the catalog problem. If “edge-critical” refers instead to chromatic index, the lemma is irrelevant.

# 3. The cubic five-pole

Delete \(v_0,\dots,v_4\) from \(H\), retaining \(a_0,\dots,a_4\) as dangling semiedges. Denote the resulting cubic five-pole by \(P\). A proper 3-coloring of the line-graph part of the corona is precisely a proper 3-edge-coloring of \(P\).

It is useful to regard the three colors as the nonzero elements
\[
K^\ast=\mathbb Z_2^2\setminus\{0\}=\{A,B,C\},
\]
where \(A+B+C=0\). Three nonzero colors are pairwise distinct exactly when their sum is zero.

# 4. Exact local signature of the corona

Fix colors
\[
\alpha_i\in\{A,B,C\}
\]
on the five terminal edges \(a_i\). We ask when the local corona can be colored, with the \(b_i,x_i,y_i\) still free.

## Lemma 4.1 — corona signature

The local corona is 3-colorable with \(a_i\) colored \(\alpha_i\) if and only if the multiplicities of the colors among
\[
\alpha_0,\dots,\alpha_4
\]
are \(2,2,1\).

### Proof: necessity

Suppose such a coloring exists. Since
\[
\{a_i,x_i,y_i\}
\quad\text{and}\quad
\{b_i,y_i,x_{i+1}\}
\]
are triangles,
\[
\alpha_i+x_i+y_i=0,
\qquad
b_i+y_i+x_{i+1}=0.
\]
Summing over \(i\) gives
\[
\sum_i\alpha_i=\sum_i b_i. \tag{4.1}
\]

The \(b_i\) properly color a \(5\)-cycle. Every color class in \(C_5\) has size at most \(2\), and a proper coloring of an odd cycle uses all three colors. Hence the color multiplicities among the \(b_i\) are \(2,2,1\). In particular, \(\sum b_i\ne0\).

Thus the \(\alpha_i\) cannot have multiplicities \(3,1,1\), since in that case all three color counts are odd and \(\sum\alpha_i=0\).

There is a second obstruction. If
\[
\alpha_i=\alpha_{i+1}=A,
\]
then both ordered pairs \((x_i,y_i)\) and \((x_{i+1},y_{i+1})\) consist of \(B,C\). The edge \(y_ix_{i+1}\) forces the two pairs to have the same orientation, and consequently \(b_i=A\). Therefore three cyclically consecutive equal \(\alpha\)'s force two consecutive \(b\)'s to be equal.

After excluding the \(3,1,1\) case using (4.1), the only multiplicity patterns other than \(2,2,1\) are
\[
5,0,0,\qquad 4,1,0,\qquad 3,2,0.
\]
The first two contain three cyclically consecutive equal entries. In the \(3,2,0\) case, either this again happens, or, up to dihedral symmetry and color exchange, the word is
\[
A,A,B,A,B.
\]
For this word, equality of the first two entries forces \(b_0=A\). If
\[
(x_0,y_0)=(x_1,y_1)=(B,C),
\]
the remaining constraints force
\[
(b_0,\dots,b_4)=(A,B,A,B,A),
\]
which is not a proper coloring of the cyclic edge \(b_4b_0\). If instead
\[
(x_0,y_0)=(x_1,y_1)=(C,B),
\]
either \(b_1=A=b_0\), or the final edge \(y_4x_0\) is monochromatic. Thus this case is also impossible.

Hence the multiplicities must be \(2,2,1\).

### Proof: sufficiency

Up to color permutation and dihedral symmetry, a cyclic word with multiplicities \(2,2,1\) is represented by one of the following three rows. The table gives explicit \(x\), \(y\), and \(b\) words.

\[
\begin{array}{c|c|c|c}
\alpha & x & y & b\\ \hline
AABBC & CCAAB & BBCCA & ACBAB\\
ABABC & BABAB & CCCCA & BABAC\\
AABCB & BBABC & CCCAA & ABABC
\end{array}
\]

In every column position, \(\alpha_i,x_i,y_i\) are the three colors; likewise \(b_i,y_i,x_{i+1}\) are the three colors. Each displayed \(b\)-word properly colors \(C_5\). This proves sufficiency. ∎

# 5. Recovery of the known 4-chromaticity

In any proper 3-edge-coloring of a cubic five-pole, each terminal color occurs an odd number of times.

Indeed, if \(n=|V(P)|\), and \(t_c\) is the number of terminals of color \(c\), then counting incidences of color \(c\) gives
\[
n\equiv t_c\pmod 2.
\]
Also
\[
3n=2|E_{\mathrm{int}}(P)|+5,
\]
so \(n\) is odd. Hence every \(t_c\) is odd. Since there are five terminals, their multiplicities must be
\[
3,1,1.
\]

Lemma 4.1 says that the corona would instead require multiplicities \(2,2,1\). Thus the corona is not 3-colorable. It is planar and has maximum degree \(4\), so it is 4-colorable; hence its chromatic number is exactly \(4\).

This also checks that the combinatorial model above reproduces the source paper’s parity obstruction.

# 6. Exact criterion for deleting an old vertex away from the pentagon

Let \(e\) be an internal edge of \(P\), so the corresponding vertex of the arrangement graph is not one of
\[
a_0,\dots,a_4,b_0,\dots,b_4,x_0,\dots,x_4,y_0,\dots,y_4.
\]

## Proposition 6.1

The corona graph with the vertex corresponding to \(e\) deleted is 3-colorable if and only if \(P-e\) has a proper 3-edge-coloring in which the terminal colors \(a_0,\dots,a_4\) have multiplicities \(2,2,1\).

### Proof

In the deleted corona graph, every cubic vertex of \(P\) not incident with \(e\) still gives a triangle in the line graph and hence requires its three incident edges to have distinct colors. At either endpoint of \(e\), the two remaining edge-vertices are still adjacent and therefore receive distinct colors. Thus the coloring on the old vertices is exactly a proper 3-edge-coloring of \(P-e\).

Given such a coloring, the only remaining question is whether its terminal colors extend across the local corona. By Lemma 4.1, this happens exactly for terminal multiplicities \(2,2,1\). Conversely, any 3-coloring of the deleted corona restricts to such an edge-coloring of \(P-e\). ∎

This is the main partial reduction. In particular, a counterexample can be obtained by finding an admissible rooted five-pole \(P\) and an internal edge \(e\) such that every proper 3-edge-coloring of \(P-e\) gives a terminal multiset different from \(2,2,1\).

Equivalently, one can cut \(e\) into two additional semiedges. A candidate coloring is then a 3-edge-coloring of a seven-pole in which the original five terminals have multiplicities \(2,2,1\). This is a small, direct constraint-satisfaction problem.

The missing general statement is therefore:

\[
\boxed{\text{For every admissible }P\text{ and every internal }e,
\ P-e\text{ has a }(2,2,1)\text{ terminal coloring}.}
\]

I do not have a proof of this assertion. The ordinary Four Color Theorem only supplies Tait colorings of suitable cubic planar completions; it does not prescribe this five-terminal signature.

Deletions among the twenty local vertices \(a_i,b_i,x_i,y_i\) lead to analogous finite signature-intersection conditions. They also require some flexibility in the coloring signature of \(P\); a fixed Tait coloring of the original cubic graph does not automatically suffice.

# 7. A completely reproducible check of the smallest standard instance

Take \(H\) to be the dodecahedral graph, represented as the generalized Petersen graph \(G(10,2)\), and use the facial pentagon
\[
(v_0,v_2,v_4,v_6,v_8).
\]
Its medial graph is the standard icosidodecahedral six-pseudocircle arrangement: its straight-ahead decomposition consists of six simple decagons, every two meeting twice. The corona has \(30+10=40\) vertices.

The following pure-Python program constructs exactly the graph described above and exhaustively finds and verifies a 3-coloring after each of its forty vertex deletions.

```python
from itertools import combinations

def U(i): return ("u", i % 10)
def V(i): return ("v", i % 10)

def edge(a, b):
    return tuple(sorted((a, b)))

# Dodecahedral graph = generalized Petersen graph G(10,2).
H = set()
for i in range(10):
    H.add(edge(U(i), U(i + 1)))
    H.add(edge(U(i), V(i)))
    H.add(edge(V(i), V(i + 2)))
assert len(H) == 30

vertices_H = {z for e in H for z in e}
inc = {z: [] for z in vertices_H}
for e in H:
    for z in e:
        inc[z].append(e)
assert all(len(inc[z]) == 3 for z in inc)

def old(e):
    return ("E", e)

adj = {}

def link(a, b):
    adj.setdefault(a, set()).add(b)
    adj.setdefault(b, set()).add(a)

def unlink(a, b):
    assert b in adj[a] and a in adj[b]
    adj[a].remove(b)
    adj[b].remove(a)

# L(H).
for z in vertices_H:
    for e, f in combinations(inc[z], 2):
        link(old(e), old(f))

face = [V(0), V(2), V(4), V(6), V(8)]
X, Y = [], []

for i in range(5):
    vi = face[i]
    bp = edge(face[i - 1], vi)
    bn = edge(vi, face[(i + 1) % 5])
    a = next(e for e in inc[vi] if e != bp and e != bn)

    x = ("x", i)
    y = ("y", i)
    X.append(x)
    Y.append(y)

    # Subdivide bp--a by x and a--bn by y.
    unlink(old(bp), old(a))
    unlink(old(a), old(bn))
    link(old(bp), x)
    link(x, old(a))
    link(old(a), y)
    link(y, old(bn))

    # Corona edge through the corner a.
    link(x, y)

# Remaining corona edges, through the b_i corners.
for i in range(5):
    link(Y[i], X[(i + 1) % 5])

assert len(adj) == 40
assert sum(len(adj[z]) for z in adj) // 2 == 80
assert all(len(adj[z]) == 4 for z in adj)

def three_coloring(drop):
    verts = set(adj)
    verts.remove(drop)
    color = {}

    def search():
        if len(color) == len(verts):
            return dict(color)

        uncolored = [z for z in verts if z not in color]

        def score(z):
            saturation = len({
                color[w] for w in adj[z] if w in color
            })
            remaining_degree = sum(
                w in verts and w not in color for w in adj[z]
            )
            return saturation, remaining_degree, repr(z)

        z = max(uncolored, key=score)
        forbidden = {color[w] for w in adj[z] if w in color}

        # Canonical introduction of color names removes S_3 symmetry.
        largest_used = max(color.values(), default=-1)
        number_of_choices = min(2, largest_used + 1) + 1

        for c in range(number_of_choices):
            if c not in forbidden:
                color[z] = c
                ans = search()
                if ans is not None:
                    return ans
                del color[z]
        return None

    return search()

def verify(cert, drop):
    verts = set(adj)
    verts.remove(drop)
    assert set(cert) == verts
    assert set(cert.values()) <= {0, 1, 2}
    for z in verts:
        for w in adj[z]:
            if w in verts:
                assert cert[z] != cert[w]

bad = []
for q in sorted(adj, key=repr):
    cert = three_coloring(q)
    if cert is None:
        bad.append(q)
    else:
        verify(cert, q)

print(len(adj), sum(len(adj[z]) for z in adj) // 2)
print("bad deletions =", bad)
assert bad == []
```

The terminal output is

```text
40 80
bad deletions = []
```

Together with the parity proof of non-3-colorability, this verifies that the 40-vertex dodecahedral corona is 4-vertex-critical. This is only one member and is consistent with the experiments reported in the source.

# 8. Remaining gap and suggested counterexample search

The universal conjecture is reduced, but not proved. For each internal edge \(e\) of the five-pole \(P\), solve the following finite CSP:

- assign one of three colors to every edge of \(P-e\);
- require pairwise distinct incident colors at degree-three vertices;
- require the two remaining colors to differ at each endpoint of \(e\);
- require the five terminal colors to have multiplicities \(2,2,1\).

An unsatisfiable instance, provided the medial straight-ahead cycles of \(H\) form an admissible pseudocircle arrangement, gives an explicit noncritical corona. For a rigorous computational disproof, one should provide:

1. the rotation system of \(H\) and its rooted pentagonal face;
2. the straight-ahead-cycle decomposition proving arrangement admissibility;
3. the offending edge \(e\);
4. a checkable SAT/DRAT certificate that the above CSP is unsatisfiable.

Conversely, a proof must use additional structure of five-poles coming from pseudocircle arrangements; ordinary cubic planarity and the parity lemma alone do not supply the required terminal-color flexibility.

Thus the conjecture remains open in its universal form, but its global content is isolated in a precise five-terminal extension problem.