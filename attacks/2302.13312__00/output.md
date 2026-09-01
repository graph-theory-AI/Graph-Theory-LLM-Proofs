```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The remaining \u0394=7 assertion holds for every planar graph of girth at least 5, and more generally for every graph of maximum degree at most 7 admitting repeated deletion of an edge whose endpoint degrees sum to at most 8.",
  "would_publish": false,
  "caveats": "The argument does not handle triangles or general 4-cycle-rich planar graphs; no proof or counterexample for unrestricted \u0394=7 is obtained."
}
```

# 1. Statement of the partial result

Throughout, graphs are finite and simple. A linear forest is a forest of maximum degree at most \(2\).

## Theorem

Let \(G\) be a planar graph with
\[
\Delta(G)\le 7
\qquad\text{and}\qquad
\operatorname{girth}(G)\ge 5.
\]
Then
\[
E(G)=E(F_1)\mathbin{\dot\cup}E(F_2)\mathbin{\dot\cup}E(F_3)
      \mathbin{\dot\cup} M,
\]
where each \(F_i\) is a linear forest and \(M\) is a matching.

Thus the open \(\Delta=7\) conjecture holds for planar graphs of girth at least \(5\).

The proof has two ingredients:

1. an extension lemma for an edge \(xy\) satisfying \(d(x)+d(y)\le 8\);
2. a light-edge lemma showing that every planar graph of girth at least \(5\) and maximum degree at most \(7\) has such an edge.

# 2. Paired proper edge-colourings

Use the seven colours
\[
\mathcal C=\{0,1,1',2,2',3,3'\},
\]
where \(0\) is the matching colour and the other six colours are paired as
\[
\{1,1'\},\quad \{2,2'\},\quad \{3,3'\}.
\]
For a nonzero colour \(c\), write \(\bar c\) for its partner.

Call a proper edge-colouring \(\varphi:E(G)\to\mathcal C\) **admissible** if, for each \(i\in\{1,2,3\}\), the subgraph formed by the edges with colours \(i,i'\) contains no cycle.

An admissible colouring is equivalent to the desired decomposition:

- colour \(0\) is a matching;
- the union of each paired set \(\{i,i'\}\) has maximum degree at most \(2\), since the colouring is proper, and is acyclic by admissibility, hence is a linear forest.

Conversely, each component of a linear forest is a path and can be alternately edge-coloured with the corresponding pair of colours. Thus any desired decomposition gives an admissible colouring.

# 3. The edge-extension lemma

## Lemma 1

Let \(G\) satisfy \(\Delta(G)\le7\), and let \(e=xy\in E(G)\) satisfy
\[
d_G(x)+d_G(y)\le8.
\]
Every admissible colouring of \(G-e\) extends to an admissible colouring of \(G\).

### Proof

Let \(S_x\) and \(S_y\) denote the sets of colours appearing at \(x\) and \(y\), respectively, in \(G-e\), and set
\[
I=S_x\cap S_y.
\]
Because the colouring is proper,
\[
|S_x|=d_G(x)-1,\qquad |S_y|=d_G(y)-1.
\]

Let \(A\) be the set of colours missing at both \(x\) and \(y\). Then
\[
\begin{aligned}
|A|
 &=7-|S_x\cup S_y|\\
 &=7-\bigl((d_G(x)-1)+(d_G(y)-1)-|I|\bigr)\\
 &=9-d_G(x)-d_G(y)+|I|\\
 &\ge |I|+1.
\end{aligned}
\]

Any colour \(c\in A\) can be assigned to \(xy\) while preserving properness. Such an assignment can fail admissibility only if \(c\ne0\) and adding \(xy\) creates a cycle alternating between \(c\) and \(\bar c\).

If this happens, then in \(G-e\) there is an \(x\)-\(y\) path alternating between \(c\) and \(\bar c\). Since \(c\) is missing at both endpoints, the first and last edges of that path must have colour \(\bar c\). Consequently,
\[
\bar c\in S_x\cap S_y=I.
\]

Thus every potentially bad colour \(c\in A\) has its distinct partner \(\bar c\) in \(I\). There are at most \(|I|\) such colours, while \(|A|\ge |I|+1\). Hence some \(c\in A\) is safe. Assigning this colour to \(xy\) gives an admissible extension. \(\square\)

## Consequence

Suppose a class of graphs of maximum degree at most \(7\) is closed under edge deletion, and every nonempty graph in the class has an edge \(xy\) with
\[
d(x)+d(y)\le8.
\]
Then every graph in the class has the desired decomposition, by induction on the number of edges.

# 4. A planar light-edge lemma at girth five

## Lemma 2

Every nonempty planar graph \(G\) with
\[
\Delta(G)\le7,\qquad \operatorname{girth}(G)\ge5
\]
has an edge \(xy\) satisfying
\[
d_G(x)+d_G(y)\le8.
\]

### Proof

Suppose otherwise. We may take a connected counterexample in which
\[
d(u)+d(v)\ge9                                           \tag{1}
\]
for every edge \(uv\).

Condition (1) and \(\Delta(G)\le7\) imply:

- \(G\) has no vertex of degree \(1\);
- every degree-\(2\) vertex has two degree-\(7\) neighbours;
- every degree-\(3\) vertex is adjacent only to vertices of degree \(6\) or \(7\).

Let \(s\) be the number of degree-\(2\) vertices. Suppress all degree-\(2\) vertices: replace each path \(x-v-y\), with \(d(v)=2\), by an edge \(xy\). Call the resulting plane graph \(H\), and mark each edge arising in this way.

The graph \(H\) is simple. Indeed:

- if \(xy\) were already an edge, then \(xvyx\) would be a triangle in \(G\);
- if two degree-\(2\) vertices had the same neighbours \(x,y\), they would form a \(4\)-cycle with \(x,y\).

Every marked edge joins two degree-\(7\) vertices, and there are exactly \(s\) marked edges. Suppression does not change the degrees of the remaining vertices, so all vertices of \(H\) have degrees between \(3\) and \(7\). Let \(n_i\) be the number of degree-\(i\) vertices of \(H\).

### Faces of \(H\)

A triangle of \(H\) containing \(r\) marked edges expands to a cycle of length \(3+r\) in \(G\). Since \(G\) has girth at least \(5\), every triangular face of \(H\) contains at least two marked edges. As marked edges join degree-\(7\) vertices, every vertex incident with a triangular face of \(H\) has degree \(7\).

For a face \(f\), let \(\ell(f)\) denote its boundary length. Euler's formula gives
\[
\sum_{v\in V(H)}(6-d_H(v))
 =
12+\sum_{f\in F(H)}(2\ell(f)-6).
\]
Hence
\[
3n_3+2n_4+n_5-n_7
 =
12+\sum_{f\in F(H)}(2\ell(f)-6).                       \tag{2}
\]

All face-corners incident with vertices of degrees \(3,4,5,6\) lie on nontriangular faces. Their total number is
\[
L=3n_3+4n_4+5n_5+6n_6.
\]
For every nontriangular face, \(\ell(f)\ge4\) and
\[
2\ell(f)-6\ge \frac{\ell(f)}2.
\]
It follows that
\[
\sum_{f\in F(H)}(2\ell(f)-6)\ge \frac L2.
\]
Substituting into (2) gives
\[
3n_3+2n_4+n_5-n_7
 \ge
12+\frac12(3n_3+4n_4+5n_5+6n_6),
\]
and therefore
\[
n_3\ge 8+n_5+2n_6+\frac23n_7.                          \tag{3}
\]

### Counting incidences at high-degree vertices

Every degree-\(3\) vertex is adjacent only to degree-\(6\) or degree-\(7\) vertices. In addition, the \(s\) marked edges consume \(2s\) incidences at degree-\(7\) vertices. Consequently,
\[
3n_3+2s\le6n_6+7n_7.                                   \tag{4}
\]

Let
\[
N=s+n_3+n_4+n_5+n_6+n_7
\]
be the number of vertices of \(G\), and let
\[
D=2s+3n_3+4n_4+5n_5+6n_6+7n_7
\]
be the sum of its degrees. Then
\[
3D-10N
 =
-4s-n_3+2n_4+5n_5+8n_6+11n_7.                         \tag{5}
\]

From (4),
\[
-4s\ge6n_3-12n_6-14n_7.
\]
Using this in (5),
\[
3D-10N
 \ge
5n_3+2n_4+5n_5-4n_6-3n_7.
\]
Now apply (3):
\[
\begin{aligned}
3D-10N
&\ge
40+2n_4+10n_5+6n_6+\frac13n_7\\
&>0.
\end{aligned}
\]
Thus \(G\) has average degree strictly greater than \(10/3\).

On the other hand, every simple planar graph of girth at least \(5\) has average degree strictly less than \(10/3\). This is the standard Euler bound; it also follows blockwise when bridges are present. This contradiction proves the lemma. \(\square\)

# 5. Proof of the partial theorem

Suppose \(G\) is a minimal counterexample among planar graphs of girth at least \(5\) and maximum degree at most \(7\).

By Lemma 2, \(G\) has an edge \(xy\) with
\[
d_G(x)+d_G(y)\le8.
\]
The graph \(G-xy\) remains planar, has girth at least \(5\), and has maximum degree at most \(7\). By minimality, it has an admissible seven-colouring. Lemma 1 extends this colouring over \(xy\), contradicting the choice of \(G\).

Hence every such \(G\) has an admissible colouring and therefore a partition into three linear forests and a matching. \(\square\)

The proof is constructive: repeatedly delete an edge of endpoint-degree sum at most \(8\), then restore the edges in reverse order using Lemma 1.

# 6. A further nonplanar sufficient condition

The same extension argument gives a maximum-average-degree result.

## Proposition

If
\[
\Delta(G)\le7
\qquad\text{and}\qquad
\operatorname{mad}(G)<\frac{28}{9},
\]
then \(G\) can be decomposed into three linear forests and a matching.

### Justification

It suffices to show that any graph of maximum degree at most \(7\) in which every edge has endpoint-degree sum at least \(9\) has average degree at least \(28/9\).

Give each vertex initial charge equal to its degree, and make the following transfers:

- every degree-\(7\) vertex sends \(5/9\) to each degree-\(2\) neighbour;
- every degree-\(6\) or degree-\(7\) vertex sends \(1/27\) to each degree-\(3\) neighbour.

A degree-\(2\) vertex has two degree-\(7\) neighbours and finishes with
\[
2+2\cdot\frac59=\frac{28}{9}.
\]
A degree-\(3\) vertex has three neighbours of degree at least \(6\) and finishes with
\[
3+3\cdot\frac1{27}=\frac{28}{9}.
\]
Vertices of degrees \(4\) and \(5\) already have charge greater than \(28/9\). A degree-\(6\) vertex cannot have degree-\(2\) neighbours and sends at most \(6/27\). A degree-\(7\) vertex sends at most \(7\cdot5/9\), so it also finishes with at least \(28/9\).

Thus every such graph has average degree at least \(28/9\). Therefore every subgraph of a graph with \(\operatorname{mad}<28/9\) has a light edge of degree-sum at most \(8\), and Lemma 1 applies recursively.

# 7. Why this does not settle the conjecture

The light-edge statement is false already at girth \(4\). For example, in \(K_{2,7}\), every edge has endpoint-degree sum
\[
7+2=9.
\]
Thus the edge-deletion induction cannot even start.

This is not a counterexample to the conjecture. If the degree-\(7\) vertices are \(x,y\) and the other vertices are \(v_0,\dots,v_6\), one valid decomposition is:

\[
\begin{array}{c|cc}
i & xv_i & yv_i\\ \hline
0 & M   & F_1\\
1 & F_1 & M\\
2 & F_1 & F_2\\
3 & F_2 & F_1\\
4 & F_2 & F_3\\
5 & F_3 & F_2\\
6 & F_3 & F_3
\end{array}
\]

Here \(M=\{xv_0,yv_1\}\); \(F_1,F_2\) are unions of two short paths, and
\[
F_3=v_5-x-v_6-y-v_4
\]
is a path.

Thus \(4\)-cycles create genuine obstructions to this particular induction without themselves violating the conjecture. The unrestricted planar \(\Delta=7\) case would require additional reducible configurations or recolouring operations capable of handling such heavy-edge cores. No such argument is supplied here, and the full conjecture remains open.