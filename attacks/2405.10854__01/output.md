```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an initial-coefficient bound for simple graphs with an orientable triangular embedding and verify the conjecture through five vertices, but do not resolve the general case.",
  "would_publish": false,
  "caveats": "The argument uses fixed-graph rotation-system counts and, except for the small-order check, requires an orientable triangular embedding; later coefficient ratios remain uncontrolled."
}
```

# Mathematical writeup

## 1. Statement and conventions

Let \(a_g(G)\) denote the number of orientable rotation systems of \(G\) whose associated cellular embedding has genus \(g\). Thus vertices and edges of \(G\) are fixed; graph automorphisms are not factored out. This is the usual convention under which the total number of orientable embeddings is

\[
\prod_{v\in V(G)}(\deg(v)-1)!.
\]

If global mirror images are identified, all coefficients below, apart from the exceptional cycle case, are divided by two, so the log-concavity conclusions are unchanged.

The conjecture asks whether

\[
a_g(G)^2\geq a_{g-1}(G)a_{g+1}(G)
\]

for every \(g\), whenever \(G\) triangulates some closed surface.

I do not prove or disprove this. I prove two partial results:

1. a structural face-defect identity, together with a quantitative lower bound on the first coefficient after the minimum genus, for simple graphs admitting an orientable triangular embedding;
2. an exact verification for every simple graph on at most five vertices which triangulates any closed surface.

---

## 2. Face excess grades the genus

Assume that \(G\) is connected and simple and has an orientable triangular embedding of genus \(h\). Write \(n=|V(G)|\) and \(m=|E(G)|\).

Since the embedding is triangular,

\[
3f=2m
\]

and Euler's formula gives

\[
n-m+\frac{2m}{3}=2-2h.
\]

Hence

\[
m=3n-6+6h. \tag{2.1}
\]

For any orientable cellular embedding \(\Pi\) of \(G\), define its face excess by

\[
\delta(\Pi)=\sum_{F\in\mathcal F(\Pi)}\bigl(|\partial F|-3\bigr).
\]

Because \(G\) is simple and is the graph of a triangulation, it has no loops, parallel edges, or degree-one vertices. Thus every face in any cellular embedding has length at least three. Consequently \(\delta(\Pi)\geq0\).

If \(\Pi\) has genus \(g\) and \(f\) faces, then

\[
f=2-2g-n+m,
\]

and therefore

\[
\begin{aligned}
\delta(\Pi)
  &=2m-3f\\
  &=2m-3(2-2g-n+m)\\
  &=3n-m-6+6g\\
  &=6(g-h), \tag{2.2}
\end{aligned}
\]

where the last equality uses (2.1).

This proves:

### Proposition 2.1

If a connected simple graph \(G\) has an orientable triangular embedding of genus \(h\), then:

- \(a_g(G)=0\) for \(g<h\);
- the genus-\(h\) embeddings are exactly the triangular embeddings;
- every genus-\((h+k)\) embedding has total face excess exactly \(6k\).

In particular, a genus-\((h+1)\) embedding has one of the following nontriangular face-length patterns, with all remaining faces triangular:

\[
9;\quad 8,4;\quad 7,5;\quad 7,4,4;\quad 6,6;\quad
6,5,4;\quad 6,4,4,4;
\]
\[
5,5,5;\quad 5,5,4,4;\quad
5,4,4,4,4;\quad 4,4,4,4,4,4.
\]

This exact grading is potentially useful for a finite-defect analysis.

### Nonorientable triangular embeddings

If instead \(G\) triangulates the nonorientable surface of crosscap number \(k\), then

\[
m=3n-6+3k.
\]

For any orientable embedding of genus \(g\), the same calculation gives

\[
\delta(\Pi)=6g-3k. \tag{2.3}
\]

Hence every orientable embedding satisfies

\[
g\geq \left\lceil\frac{k}{2}\right\rceil.
\]

When \(k\) is odd, no orientable embedding can itself be triangular. This is one reason that “triangulates some surface” and “has an orientable triangular embedding” should be distinguished.

---

## 3. The first two nonzero coefficients cannot decrease

I next prove a quantitative version of

\[
a_{h+1}(G)\geq a_h(G)
\]

for a simple graph with an orientable triangular embedding of genus \(h\).

### 3.1. Adjacent switches

A rotation system specifies a cyclic order at each vertex. At a vertex of degree \(d\geq4\), interchange two cyclically consecutive darts. There are \(d\) distinct such neighboring cyclic orders.

At a degree-three vertex, all three adjacent interchanges give the same reversed cyclic order, so count this as one switch.

Define

\[
q(d)=
\begin{cases}
1,&d=3,\\
d,&d\geq4,
\end{cases}
\qquad
D(G)=\sum_{v\in V(G)}q(\deg v).
\]

The graph on all rotation systems obtained by these local switches is \(D(G)\)-regular.

Let \(\sigma\) be the permutation consisting of the vertex rotations, let \(\alpha\) reverse each edge-dart, and let

\[
\varphi=\sigma\alpha
\]

be the face permutation. An adjacent switch changes \(\sigma\) by a 3-cycle on three darts at one vertex. In a triangular embedding, the three affected darts lie in three distinct face cycles: they correspond to three distinct triangular corners at that vertex. Multiplication by a 3-cycle on elements belonging to three distinct cycles merges those cycles into one. Thus the number of faces falls by two and the genus rises by one.

Therefore every one of the \(D(G)\) switches from a genus-\(h\) embedding produces a genus-\((h+1)\) embedding.

### 3.2. Bounding the reverse multiplicity

Suppose a genus-\((h+1)\) embedding is adjacent by such a switch to a triangular embedding. In the forward direction, three triangular faces were merged. Hence the target embedding has one face of length nine and all its other faces have length three.

A reverse switch is supported on three occurrences of the same vertex on that 9-face. Let \(k_v\) be the number of occurrences of \(v\) on its facial boundary. Since \(G\) has no loops, equal consecutive vertices cannot occur. Consequently

\[
k_v\leq 4
\]

for every \(v\). Moreover,

\[
\sum_v k_v=9.
\]

Each reverse switch determines a three-element subset among the occurrences of some vertex, and distinct switches have distinct supports. Hence the number of reverse switches is at most

\[
\sum_v \binom{k_v}{3}.
\]

Subject to \(k_v\leq4\) and \(\sum k_v=9\), this is at most

\[
\binom43+\binom43=8.
\]

Counting switch incidences between genera \(h\) and \(h+1\) now gives

\[
D(G)a_h(G)\leq \min\{D(G),8\}\,a_{h+1}(G).
\]

Thus:

### Proposition 3.1

Let \(G\) be connected and simple, with an orientable triangular embedding of genus \(h\), and suppose \(G\neq K_3\). Then

\[
\boxed{\displaystyle
a_{h+1}(G)\geq
\frac{D(G)}{\min\{D(G),8\}}\,a_h(G)
\geq a_h(G).
}
\]

If \(n_3\) denotes the number of degree-three vertices, then

\[
D(G)=2m-2n_3.
\]

This establishes a quantitative initial increase. It does not establish log-concavity, because that would additionally require

\[
\frac{a_{h+1}}{a_h}\geq \frac{a_{h+2}}{a_{h+1}},
\]

and I have no corresponding upper bound on the second ratio.

---

## 4. Exact verification through five vertices

Assume throughout this section that graphs are simple.

For a triangular embedding on a surface of Euler characteristic \(\chi\),

\[
m=3(n-\chi).
\]

In particular, \(m\geq3n-6\) and \(3\mid m\). Comparing this with \(m\leq\binom n2\) shows that for \(n\leq5\) the only possibilities are:

- \(n=3\): \(K_3\);
- \(n=4\): \(K_4\);
- \(n=5\): \(K_5-e\).

All three triangulate the sphere.

The first two genus distributions are immediate:

\[
\Gamma_{K_3}(x)=1,
\qquad
\Gamma_{K_4}(x)=2+14x.
\]

For completeness, I calculate \(K_5-e\) exactly.

### 4.1. A face-splicing observation

Let a new degree-three vertex \(y\) be joined to three existing vertices. To extend a rotation system of the old graph:

1. choose one insertion corner at each of the three neighbors;
2. choose one of the two cyclic orders at \(y\).

The three chosen corners can lie in one, two, or three old faces.

- If they lie in three distinct faces, either order at \(y\) merges the three faces, so \(\Delta f=-2\).
- If they lie in exactly two faces, either order gives \(\Delta f=0\).
- If they lie in one face, one order splits that face into three, giving \(\Delta f=2\), while the other gives \(\Delta f=0\).

Adding \(y\) changes \(n\) by \(1\) and \(m\) by \(3\), so

\[
g_{\mathrm{new}}=g_{\mathrm{old}}+1-\frac{\Delta f}{2}. \tag{4.1}
\]

### 4.2. Applying this to \(K_5-e\)

Write

\[
G=K_5-xy,
\]

where \(a,b,c\) are the three common neighbors of \(x\) and \(y\). Deleting \(y\) leaves the \(K_4\) on \(\{a,b,c,x\}\).

Each rotation system of \(K_4\) has:

- three insertion positions at each of \(a,b,c\);
- two choices at \(y\).

Thus it has

\[
3^3\cdot2=54
\]

extensions.

There are two planar rotations of \(K_4\). Its four faces can be denoted

\[
T=abc,\qquad P=abx,\qquad Q=acx,\qquad R=bcx.
\]

The corner-face choices are

\[
a:\{T,P,Q\},\qquad
b:\{T,P,R\},\qquad
c:\{T,Q,R\}.
\]

Exactly one triple has all corners in the same face, namely \((T,T,T)\). Exactly eleven triples use three distinct faces. Therefore, for each planar \(K_4\) rotation, the 54 extensions are distributed as follows:

\[
\begin{array}{c|c}
\text{new genus}&\text{number}\\ \hline
0&1\\
1&31\\
2&22.
\end{array}
\]

The remaining fourteen rotations of \(K_4\) have genus one and two faces. For such a rotation \(R\), let

\[
s(R)=\sum_F k_a(F)k_b(F)k_c(F),
\]

where \(k_v(F)\) is the number of corners of \(F\) at \(v\). This is the number of insertion triples lying in one face.

Fix a planar rotation of \(K_4\) and independently reverse local rotations. A direct face-permutation trace gives:

\[
\begin{array}{c|c|c|c}
\text{sign pattern}&\text{number}&
\text{corner counts at }(a,b,c)&s(R)\\ \hline
\text{unique minority vertex in }\{a,b,c\}
  &6&(0,1,1),(3,2,2)&12\\
\text{unique minority vertex }x
  &2&(1,1,1),(2,2,2)&9\\
\text{two signs of each type}
  &6&(1,1,1),(2,2,2)&9.
\end{array}
\]

Hence

\[
\sum_R s(R)=6\cdot12+2\cdot9+6\cdot9=144.
\]

For the fourteen toroidal rotations, these 144 extensions retain genus one; the other

\[
14\cdot54-144=612
\]

have genus two.

Combining the planar and toroidal sources gives

\[
\boxed{\Gamma_{K_5-e}(x)=2+206x+656x^2.}
\]

The only nontrivial log-concavity inequality is

\[
206^2=42436>2\cdot656=1312.
\]

Thus the conjecture holds for every simple graph on at most five vertices that triangulates a closed surface.

If mirror images are identified, the sequence is

\[
(1,103,328),
\]

which is again log-concave.

---

## 5. Reproducible exhaustive enumerator

The following code enumerates fixed-graph orientable rotation systems exactly.

```python
from itertools import permutations, product, combinations
from collections import Counter

def genus_distribution(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    adj = [set() for _ in range(n)]
    for u, v in E:
        assert u != v
        adj[u].add(v)
        adj[v].add(u)

    all_orders = []
    for v in range(n):
        nbrs = sorted(adj[v])
        assert nbrs
        root = nbrs[0]
        # One representative for each cyclic order.
        all_orders.append([
            (root,) + p for p in permutations(nbrs[1:])
        ])

    darts0 = {(u, v) for u, v in E} | {(v, u) for u, v in E}
    ans = Counter()

    for orders in product(*all_orders):
        succ = {}
        for v, order in enumerate(orders):
            d = len(order)
            for i, u in enumerate(order):
                succ[(v, u)] = order[(i + 1) % d]

        unseen = set(darts0)
        faces = 0
        while unseen:
            faces += 1
            dart = next(iter(unseen))
            while dart in unseen:
                unseen.remove(dart)
                u, v = dart
                dart = (v, succ[(v, u)])

        numerator = 2 - n + len(E) - faces
        assert numerator >= 0 and numerator % 2 == 0
        ans[numerator // 2] += 1

    return ans

K3 = list(combinations(range(3), 2))
K4 = list(combinations(range(4), 2))
K5_minus_e = [
    e for e in combinations(range(5), 2) if e != (3, 4)
]

assert genus_distribution(3, K3) == Counter({0: 1})
assert genus_distribution(4, K4) == Counter({0: 2, 1: 14})
assert genus_distribution(5, K5_minus_e) == Counter({
    0: 2, 1: 206, 2: 656
})
```

The first unresolved orientably triangulating simple graphs occur on six vertices. There are exactly two sphere triangulations:

- the octahedral graph \(K_6\) minus a perfect matching, with \(6^6=46656\) rotation systems;
- \(K_2\vee P_4\), with \(82944\) rotation systems.

Thus both are within reach of the displayed exhaustive routine.

If nonorientable triangulations are included, \(K_6\) is an additional six-vertex case. An explicit projective-plane triangulation has vertex set
\(\{\infty\}\cup\mathbb Z_5\) and faces

\[
\{\infty,i,i+1\},
\qquad
\mathbb Z_5\setminus\{i,i+2\},
\qquad i\in\mathbb Z_5.
\]

Every edge occurs in two faces, every vertex link is a cycle, and

\[
6-15+10=1.
\]

A naïve rotation-system enumeration of \(K_6\) has \(24^6=191102976\) cases, so symmetry reduction would be preferable.

---

## 6. Remaining gap

The face-excess identity gives a rigid description of each fixed distance from the minimum genus, and Proposition 3.1 rules out an initial decrease. It does not control the ratios after the first step. In particular, I do not have an injection or switching argument proving

\[
a_{h+1}^2\geq a_h a_{h+2}.
\]

Nor have I found a triangularly embeddable graph violating this inequality. The nonorientable-only case is additionally outside the main switching argument because its minimum orientable embeddings need not be triangular. Thus the original conjecture remains unresolved.