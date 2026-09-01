```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For finite simple graphs, stars satisfy the conjectured conclusion, while arbitrarily high-minimum-degree obstructions at edge-connectivity 2m-2 force every possible witness to have f(m) at least 2m-1 for m at least 3.",
  "would_publish": false,
  "caveats": "Uses a published modulo-orientation theorem for the upper bound and does not handle nonstar subdivisions or general bounded-leaf trees."
}
```

# Mathematical writeup

## 1. Statement and graph convention

Write \(S_m=K_{1,m}\) for the star with \(m\) leaves and \(m\) edges. I interpret all graphs as finite and simple, and copies in a decomposition as ordinary injective subgraphs isomorphic to \(T\).

The simplicity assumption is essential. If unrestricted parallel edges were allowed, the extracted conjecture would be false: for any proposed \(f\) and any tree \(T\) with \(t\ge 2\) edges, two vertices joined by a sufficiently large multiple of \(t\) parallel edges would have arbitrarily large minimum degree and edge-connectivity but would contain no copy of \(T\).

The main partial result is the following.

### Theorem

For every integer \(m\ge 3\):

1. Every
   \[
   c_m=\begin{cases}
   3m-3,&m\ \text{odd},\\
   3m-2,&m\ \text{even}
   \end{cases}
   \]
   edge-connected simple graph \(G\) with \(m\mid |E(G)|\) has an \(S_m\)-decomposition. No additional minimum-degree hypothesis is needed.

2. For every integer \(D\), there is a simple graph \(G=G(m,D)\) such that
   \[
   \lambda(G)=2m-2,\qquad \delta(G)\ge D,\qquad m\mid |E(G)|,
   \]
   but \(G\) has no \(S_m\)-decomposition.

Consequently, if \(f\) satisfies the catalog conjecture, then necessarily
\[
\boxed{f(m)\ge 2m-1\quad\text{for every }m\ge3.}
\]

If \(\kappa_m^\star\) denotes the least connectivity which, without any minimum-degree assumption, forces an \(S_m\)-decomposition whenever the number of edges is divisible by \(m\), then
\[
2m-1\le \kappa_m^\star\le
\begin{cases}
3m-3,&m\text{ odd},\\
3m-2,&m\text{ even}.
\end{cases}
\]
In particular, for the claw,
\[
5\le \kappa_3^\star\le 6.
\]

## 2. Stars and modulo orientations

The relevant elementary equivalence is as follows.

### Lemma 1

A simple graph \(G\) has an \(S_m\)-decomposition if and only if it has an orientation satisfying
\[
d_G^+(v)\equiv 0\pmod m
\qquad\text{for every }v\in V(G).
\]

#### Proof

Given an \(S_m\)-decomposition, orient every edge of each star away from its center. If \(v\) is the center of \(q_v\) stars, then
\[
d_G^+(v)=m q_v.
\]

Conversely, suppose every outdegree is divisible by \(m\). At each vertex \(v\), partition its outgoing edges arbitrarily into groups of \(m\). Because \(G\) is simple, the \(m\) edges in any group have distinct other endpoints and therefore form an \(S_m\) centered at \(v\). Every edge is grouped exactly once, namely at its tail. ∎

## 3. Positive result for stars

We use the established modulo-orientation theorem of Lovász, Thomassen, Wu and Zhang, from *Nowhere-zero 3-flows and modulo \(k\)-orientations*, J. Combin. Theory Ser. B 103 (2013), 587–598:

> If \(k\ge3\), \(p:V(G)\to\mathbb Z_k\), and
> \[
> \sum_{v\in V(G)}p(v)\equiv |E(G)|\pmod k,
> \]
> then \(G\) has an orientation with
> \[
> d_G^+(v)\equiv p(v)\pmod k
> \]
> whenever \(G\) is \((3k-3)\)-edge-connected for odd \(k\), or \((3k-2)\)-edge-connected for even \(k\).

Apply this theorem with \(k=m\) and \(p(v)=0\) for every \(v\). The compatibility condition is precisely \(m\mid |E(G)|\). Lemma 1 then gives an \(S_m\)-decomposition.

Thus the conjectured conclusion holds for every star, with connectivity linear in its number of leaves and with no extra minimum-degree requirement.

## 4. A \((2m-2)\)-edge-connected quotient with no star decomposition

Fix \(m\ge3\), and put
\[
r=2m-2.
\]
We first construct an \(r\)-regular, \(r\)-edge-connected graph \(H_m\) with
\[
m\mid |E(H_m)|
\]
but with no orientation whose outdegrees are all divisible by \(m\).

### Construction of \(H_m\)

Let \(F_m\) be a graph with a tripartition
\[
A\cup B\cup C,
\]
where
\[
|A|=2m-2,\qquad |B|=|C|=m+1.
\]
Thus \(|V(F_m)|=4m\).

Index
\[
B=\{b_i:i\in\mathbb Z_{m+1}\},\qquad
C=\{c_i:i\in\mathbb Z_{m+1}\}.
\]

Between \(B\) and \(C\), start with the \(4\)-regular bipartite graph
\[
R=\{b_ic_{i+j}:i\in\mathbb Z_{m+1},\ j\in\{0,1,2,3\}\},
\]
and delete the two edges \(b_0c_0,b_1c_1\). Denote the resulting graph by \(R'\). Hence:

- \(b_0,b_1,c_0,c_1\) have degree \(3\) in \(R'\);
- every other vertex of \(B\cup C\) has degree \(4\);
- \(|E(R')|=4m+2\);
- \(\Delta(R')\le4\).

Choose a matching
\[
M
\]
between \(A\) and
\[
(B\setminus\{b_0,b_1\})\cup(C\setminus\{c_0,c_1\})
\]
which saturates both sets; they each have size \(2m-2\).

Define \(F_m\) to have:

- every edge between \(A\) and \(B\cup C\), except the edges of \(M\);
- the edges of \(R'\);
- no edges within \(A,B,\) or \(C\).

Every vertex of \(A\) has degree
\[
2m+2-1=2m+1.
\]
Every vertex of \(B\cup C\) incident with \(M\) has \(2m-3\) neighbors in \(A\) and four in the opposite one of \(B,C\), while each of \(b_0,b_1,c_0,c_1\) has \(2m-2\) neighbors in \(A\) and three in the opposite part. Thus \(F_m\) is \((2m+1)\)-regular.

Let
\[
H_m=\overline{F_m}.
\]
Since \(|V(H_m)|=4m\), the graph \(H_m\) is \(r\)-regular:
\[
d_{H_m}(v)=4m-1-(2m+1)=2m-2=r.
\]

Moreover, \(F_m\) is tripartite, so it has no \(K_4\). Therefore
\[
\alpha(H_m)=\omega(F_m)\le3. \tag{1}
\]

Finally,
\[
|E(H_m)|=\frac{4m(2m-2)}2=4m(m-1),
\]
which is divisible by \(m\).

### Lemma 2

\[
\lambda(H_m)=2m-2.
\]

#### Proof

The upper bound follows from regularity. For the lower bound, let \(S\subset V(H_m)\) be nonempty and proper. Replacing \(S\) by its complement if necessary, put
\[
s=|S|\le 2m.
\]

If \(s\le r=2m-2\), then
\[
|\partial_{H_m}(S)|
=rs-2e_{H_m}(S)
\ge rs-s(s-1)
=s(r-s+1).
\]
The last expression is at least \(r\) for \(1\le s\le r\).

It remains to consider \(s=2m-1\) and \(s=2m\). Since \(H_m=\overline{F_m}\),
\[
|\partial_{H_m}(S)|
=s(r-s+1)+2e_{F_m}(S). \tag{2}
\]

Write
\[
a=|S\cap A|,\qquad q=|S\cap(B\cup C)|.
\]
The edges of \(F_m\) between \(A\) and \(B\cup C\) form a complete bipartite graph minus a matching, and hence contribute at least
\[
aq-\min\{a,q\}. \tag{3}
\]

If \(s=2m-1\), equation (2) becomes
\[
|\partial_{H_m}(S)|=2e_{F_m}(S).
\]
If \(a,q\ge1\), let \(x=\min\{a,q\}\) and \(y=\max\{a,q\}\). Since \(x+y=2m-1\), we have \(y\ge m\), and (3) gives
\[
e_{F_m}(S)\ge x(y-1)\ge m-1.
\]
If \(a=0\), then \(S\) is obtained from \(B\cup C\) by deleting three vertices. Since \(R'\) has \(4m+2\) edges and maximum degree at most four,
\[
e_{F_m}(S)\ge 4m+2-12=4m-10\ge m-1.
\]
Thus \(|\partial_{H_m}(S)|\ge2m-2=r\).

If \(s=2m\), equation (2) becomes
\[
|\partial_{H_m}(S)|=-2m+2e_{F_m}(S).
\]
It is therefore enough to prove \(e_{F_m}(S)\ge2m-1\).

If \(a,q\ge2\), set \(x=\min\{a,q\}\). Then \(2\le x\le m\), and (3) gives
\[
e_{F_m}(S)\ge x(2m-x-1)\ge2m-1.
\]
The last inequality follows by checking the two endpoints \(x=2,m\), since the displayed quadratic is concave.

If \(a=1\), the \(A\)--\((B\cup C)\) edges contribute at least \(2m-2\), while the \(2m-1\) selected vertices of \(B\cup C\) induce at least
\[
4m+2-12=4m-10\ge1
\]
edges of \(R'\).

If \(a=0\), only two vertices of \(B\cup C\) are omitted, so
\[
e_{F_m}(S)\ge4m+2-8=4m-6\ge2m-1.
\]
Thus every nontrivial cut has at least \(r\) edges. ∎

### Lemma 3

The graph \(H_m\) has no orientation satisfying
\[
d_{H_m}^+(v)\equiv0\pmod m
\qquad\text{for every }v.
\]

#### Proof

Since every vertex has degree \(2m-2<2m\), its outdegree in such an orientation would have to be either \(0\) or \(m\).

Let \(z\) be the number of vertices of outdegree zero. Summing all outdegrees gives
\[
m(4m-z)=|E(H_m)|=4m(m-1),
\]
and hence \(z=4\).

The vertices of outdegree zero must form an independent set: an edge between two such vertices could not be oriented into both endpoints. This contradicts \(\alpha(H_m)\le3\) from (1). ∎

By Lemma 1, \(H_m\) itself has no \(S_m\)-decomposition. Its minimum degree is only \(2m-2\), so an inflation step is needed to make the minimum degree arbitrarily large.

## 5. Raising the minimum degree without removing the obstruction

Fix \(D\). Choose
\[
N\equiv1\pmod{2m}
\]
so large that
\[
N-1\ge \max\{D,2m-2\}.
\]

Replace every vertex \(x\in V(H_m)\) by a clique \(C_x\) of order \(N\). For every edge \(xy\in E(H_m)\), add one edge between \(C_x\) and \(C_y\). Call the resulting simple graph \(G\).

Because
\[
\binom N2=\frac{N(N-1)}2
\]
is divisible by \(m\), and \(m\mid |E(H_m)|\), we have
\[
m\mid |E(G)|.
\]
Also,
\[
\delta(G)\ge N-1\ge D.
\]

For edge-connectivity, if a cut splits some clique \(C_x\), the internal clique edges crossing the cut number at least \(N-1\ge2m-2\). If no clique is split, the cut projects to a cut of \(H_m\), and hence has at least \(2m-2\) edges. Conversely, isolating an entire clique \(C_x\) gives a cut of size \(d_{H_m}(x)=2m-2\). Therefore
\[
\lambda(G)=2m-2.
\]

Suppose \(G\) had an \(S_m\)-decomposition. By Lemma 1, orient its edges so that every vertex has outdegree divisible by \(m\). For a fixed clique \(C_x\),
\[
\sum_{v\in C_x}d_G^+(v)
=
|E(C_x)|+\bigl|\{\text{edges directed from }C_x\text{ to }V(G)\setminus C_x\}\bigr|.
\]
The left side and \(|E(C_x)|\) are divisible by \(m\). Consequently the number of external edges directed out of \(C_x\) is divisible by \(m\). Directing the corresponding quotient edge of \(H_m\) in the same direction would therefore give an orientation of \(H_m\) in which every outdegree is divisible by \(m\), contradicting Lemma 3.

This proves the claimed arbitrary-minimum-degree obstruction.

## 6. Consequences for the catalog conjecture

For \(T=S_m\), both the number of leaves and the number of edges equal \(m\). If a witnessing function had
\[
f(m)\le2m-2,
\]
take the preceding construction with \(D=f(m)\). Then \(G\) would be \(f(m)\)-edge-connected, would satisfy
\[
\delta(G)\ge f(|E(T)|)=f(m),
\]
and would have its number of edges divisible by \(|E(T)|=m\), but it would have no \(T\)-decomposition. Hence every possible global witness must satisfy
\[
f(m)\ge2m-1.
\]

Together with the path theorem in the source paper, one can also obtain a single function satisfying the desired implication for the restricted class consisting of all paths and all stars: take pointwise maxima of the source paper's path minimum-degree constants and the constants \(c_m\) above.

## 7. Remaining gap

This does not settle the bounded-leaf conjecture. The key structural identity for a tree with \(m\) leaves is
\[
m-2=\sum_{\deg_T(v)\ge3}(\deg_T(v)-2),
\]
so the number of branching vertices is bounded by \(m-2\), while arbitrarily many degree-two vertices may lie on the paths between them.

For a star, the decomposition problem is exactly a modulo-outdegree orientation problem. Once an edge is subdivided, degree-two roles contribute one outgoing edge under a rooted orientation, and that clean divisibility characterization disappears. In particular, every three-leaf tree is a subdivision of the claw, but the argument above only handles the unsubdivided claw; it neither constructs the three prescribed arms nor controls their intersections.

Thus the principal open case \(m=3\) remains open here, except for the claw itself and the necessary bound \(f(3)\ge5\).