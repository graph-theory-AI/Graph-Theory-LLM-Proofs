```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an 8/9 bound for planar graphs of girth at least five, but do not resolve the conjecture when 4-cycles are allowed.",
  "would_publish": false,
  "caveats": "The special-case proof is self-contained; its novelty has not been checked, and the general 7/8 conjecture remains unresolved here."
}
```

## 1. Partial result

All graphs below are finite and simple. Write
\[
\tau_2(G)=\min\{|S|:G-S\text{ is }2\text{-degenerate}\},
\]
so that \(\alpha_2(G)=|V(G)|-\tau_2(G)\).

I obtain the following strengthening of the conjecture under an additional girth hypothesis.

**Theorem.** Every planar graph \(G\) of girth at least five satisfies
\[
\tau_2(G)\le \left\lfloor\frac{|V(G)|}{9}\right\rfloor.
\]
Consequently,
\[
\alpha_2(G)\ge \left\lceil\frac{8|V(G)|}{9}\right\rceil.
\]

The proof is constructive. Its main ingredient is a nine-vertex reduction: in a graph of minimum degree at least three, deleting one carefully chosen vertex permits at least eight further vertices to be removed in a \(2\)-degeneracy ordering.

I am not claiming that this girth-five result is new; I have not verified its literature status.

## 2. A boundary lemma for small cubic components

We use the standard Euler bound
\[
m\le \frac53(n-2)                                      \tag{1}
\]
for a connected simple planar graph of girth at least five with \(n\ge4\). For a forest, this follows from \(m=n-1\); otherwise it follows by face counting.

**Lemma 1.** Let \(G\) be planar of girth at least five. Let \(C\) be a connected set of vertices, each of degree exactly three in \(G\), and suppose \(N_G(C)\setminus C\neq\varnothing\). Put
\[
c=|C|,\qquad t=|N_G(C)\setminus C|.
\]
If \(c=1\), then \(t=3\). If \(2\le c\le7\), then \(t\ge4\).

**Proof.** Let \(e=|E(G[C])|\), and let \(b\) be the number of edges from \(C\) to its external neighborhood. Since every vertex of \(C\) has degree three,
\[
2e+b=3c.
\]
Let \(F\) consist of \(C\), its external neighbors, and precisely the edges having at least one endpoint in \(C\). Thus \(F\) is connected, planar, has girth at least five, and
\[
|V(F)|=c+t,\qquad |E(F)|=e+b=3c-e.                    \tag{2}
\]

For \(c=1\), simplicity gives \(t=3\). For \(c=2\), \(G[C]\) is an edge, and no external vertex can be adjacent to both endpoints, since that would create a triangle. Hence \(t=4\). For \(c=3\), \(G[C]\) is a path, and an external vertex adjacent to two of its vertices would create a triangle or a \(4\)-cycle. Hence \(t=5\).

Now suppose \(4\le c\le7\) and, toward a contradiction, \(t\le3\). Equation (1), together with the girth restriction on \(G[C]\), gives the following bounds:
\[
\begin{array}{c|c|c|c}
c & \text{maximum }e & \text{minimum }|E(F)|
  & \text{maximum }|E(F)|\text{ if }t\le3\\ \hline
4&3&9&8\\
5&5&10&10\\
6&6&12&11\\
7&8&13&13
\end{array}
\]
Thus \(c=4,6\) are impossible.

If \(c=5\), equality forces \(G[C]\) to be a \(5\)-cycle. Every vertex of that cycle has exactly one external neighbor. Those five neighbors are distinct: two vertices of a \(5\)-cycle have distance at most two, so a common external neighbor would create a triangle or a \(4\)-cycle. Thus \(t=5\), a contradiction.

If \(c=7\), equality forces
\[
t=3,\qquad e=8,\qquad b=5,\qquad |E(F)|=13.
\]
The three vertices outside \(C\) have total degree five in \(F\), and each has positive degree. One is therefore a leaf. Deleting that leaf leaves a planar graph of girth at least five with nine vertices and twelve edges, contradicting
\[
12>\frac53(9-2).
\]
This proves the lemma. \(\square\)

## 3. A large reducible set

Removing a vertex of degree at most two will be called **peeling** it. A graph is \(2\)-degenerate exactly when repeated peeling removes every vertex.

A useful elementary observation is that, if \(C\) is a connected set of degree-three vertices and a vertex adjacent to \(C\) is deleted, then every vertex of \(C\) can subsequently be peeled. Start with a vertex of \(C\) that lost a neighbor, and propagate through the connected graph \(G[C]\).

**Lemma 2.** Let \(G\) be a connected planar graph of girth at least five and minimum degree at least three. Either:

1. \(G\) is cubic; or
2. there is a vertex \(x\) of degree at least four such that the components of the degree-three subgraph adjacent to \(x\) contain at least eight vertices in total.

Consequently, some single-vertex deletion followed by peeling removes at least nine vertices.

**Proof.** Let
\[
D=\{v:d_G(v)=3\},\qquad B=\{v:d_G(v)\ge4\}.
\]
Euler’s bound gives
\[
10|V(G)|-6|E(G)|\ge20,
\]
or equivalently
\[
|D|-\sum_{x\in B}(3d_G(x)-10)\ge20.                 \tag{3}
\]

If \(B=\varnothing\), the graph is connected and cubic. Equation (3) gives \(|V(G)|\ge20\), and deleting any vertex allows the entire graph to be peeled.

Suppose \(B\neq\varnothing\). Let \(\mathcal C\) be the components of \(G[D]\). For \(x\in B\), define
\[
W(x)=\sum_{\substack{C\in\mathcal C\\x\in N_G(C)}} |C|,
\]
where each component is counted only once.

Assume, for a contradiction, that
\[
W(x)\le7\qquad\text{for every }x\in B.              \tag{4}
\]
Every component \(C\in\mathcal C\) has an external neighbor, since \(G\) is connected and not cubic. Thus (4) implies \(|C|\le7\).

Distribute a charge of \(|C|\) equally among the distinct external neighbors of \(C\). By Lemma 1:

- a singleton component sends \(1/3\) to each neighbor;
- a nonsingleton component sends at most \(|C|/4\) to each neighbor.

Let \(q(x)\) be the total charge received by \(x\in B\). The total charge is
\[
\sum_{x\in B}q(x)=|D|.                              \tag{5}
\]

First let \(d_G(x)=4\). If all adjacent components are singletons, then
\[
q(x)\le\frac43<2.
\]
Otherwise, let \(a\) be the number of adjacent singleton components. Since at least one incident edge goes to a nonsingleton component, \(a\le3\). Therefore
\[
q(x)\le \frac{W(x)}4+\frac{a}{12}
       \le \frac74+\frac3{12}
       =2
       =3d_G(x)-10.                                 \tag{6}
\]

If \(d_G(x)\ge5\), every component has at least three external neighbors, so
\[
q(x)\le \frac{W(x)}3
       \le\frac73
       \le 3d_G(x)-10.                              \tag{7}
\]

Summing (6) and (7), and using (5), gives
\[
|D|\le\sum_{x\in B}(3d_G(x)-10),
\]
contradicting (3). Thus some \(x\in B\) has \(W(x)\ge8\).

Delete this \(x\). All degree-three components adjacent to \(x\) can then be peeled. Together with \(x\), this removes at least nine vertices. \(\square\)

## 4. Proof of the theorem

Apply the following procedure to \(G\).

1. Peel every available vertex of degree at most two.
2. If nothing remains, stop.
3. Choose a connected component of the remaining graph, which has minimum degree at least three.
4. Use Lemma 2 to delete one vertex, and then exhaust all possible peeling.
5. Repeat.

Call the vertices explicitly deleted in step 4 **paid vertices**, and let \(S\) be their set. Every other vertex is peeled. In the order in which they were peeled, those vertices form a \(2\)-degeneracy ordering of \(G-S\). Hence \(G-S\) is an induced \(2\)-degenerate subgraph.

Each paid deletion accounts for at least nine vertices that have not been removed in an earlier round. Consequently,
\[
9|S|\le |V(G)|,
\]
which proves
\[
\tau_2(G)\le |S|\le\left\lfloor\frac{|V(G)|}{9}\right\rfloor.
\]
\(\square\)

### Slightly sharper bookkeeping

Every planar graph of girth at least five and minimum degree at least three has at least twenty vertices, by (3).

If the algorithm uses \(k\ge1\) paid deletions, its final paid round removes the entire remaining graph, which immediately before that round has minimum degree at least three and therefore has at least twenty vertices. The preceding paid rounds each remove at least nine vertices. Thus
\[
n\ge9(k-1)+20.
\]
In fact, the proof gives
\[
\boxed{\displaystyle
\tau_2(G)\le
\max\left\{0,\left\lfloor\frac{n-11}{9}\right\rfloor\right\}.}
\]
In particular, every planar graph of girth at least five on at most nineteen vertices is already \(2\)-degenerate.

The construction requires no search over deletion sets: in each noncubic minimum-degree-three component, compute its degree-three components and the quantities \(W(x)\), and choose a vertex with \(W(x)\ge8\).

## 5. Why this does not settle the original conjecture

The argument uses the absence of \(4\)-cycles essentially, both in Lemma 1 and in the Euler inequality (3). It does not establish a comparable reduction for all triangle-free planar graphs.

Indeed, the stronger \(8/9\) conclusion is false when \(4\)-cycles are allowed. There are connected equality examples for the original \(7/8\) bound of arbitrarily large order.

Let
\[
G_k=C_4\square P_{2k}.
\]
This is a triangle-free planar graph on \(8k\) vertices, drawn as \(2k\) concentric \(4\)-cycles with corresponding vertices joined.

Pair consecutive layers:
\[
(1,2),(3,4),\ldots,(2k-1,2k).
\]
Each pair induces a cube. These \(k\) cubes are vertex-disjoint, and every deletion set producing a \(2\)-degenerate graph must meet each of them. Hence
\[
\tau_2(G_k)\ge k.
\]

Conversely, delete one fixed-coordinate vertex in each even-numbered layer. The first layer then peels completely. The second layer, with one vertex deleted, becomes a path whose vertices have at most one neighbor in the third layer, so it also peels. Repeat with successive pairs of layers. Thus
\[
\tau_2(G_k)\le k.
\]
Therefore
\[
\alpha_2(G_k)=8k-k=\frac78|V(G_k)|.
\]

So the partial result isolates the remaining difficulty: **the girth-five case admits a stronger nine-vertex reduction, while the \(4\)-cycle case must accommodate genuinely tight eight-vertex structures.** No argument covering that remaining case is established here.