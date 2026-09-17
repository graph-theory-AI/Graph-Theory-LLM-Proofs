```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "An explicit seven-vertex planar oriented graph has maximum acyclic induced order four, and an infinite family has acyclic fraction tending to one half.",
  "would_publish": false,
  "caveats": "No claim of novelty or historical priority; the supplied open-status report is incompatible with this explicit construction."
}
```

## 1. A seven-vertex counterexample

For a digraph \(D\), write
\[
\alpha_{\mathrm{ac}}(D)=\max\{|A|:D[A]\text{ is acyclic}\}.
\]

Let \(D\) have vertex set
\[
V(D)=\{a,b,c,x,y,p,q\}
\]
and exactly the following arcs:
\[
\begin{array}{lll}
a\to b, & b\to c, & c\to a,\\[2mm]
a\to x, & b\to x, & x\to y,\qquad y\to a,\quad y\to b,\\[2mm]
x\to p, & y\to p, & p\to q,\qquad q\to x,\quad q\to y.
\end{array}
\]
There are no loops or pairs of oppositely directed arcs, so this is an oriented graph.

### Planarity

The underlying graph consists of:

- the triangle \(abc\);
- a copy of \(K_4\) on \(\{a,b,x,y\}\), glued to that triangle along \(ab\);
- a copy of \(K_4\) on \(\{x,y,p,q\}\), glued along \(xy\).

These gluings preserve planarity. Explicitly, to attach a \(K_4\) along an existing edge \(uv\), place a new vertex \(r\) in a face incident with \(uv\), drawing \(ur,vr\) so that \(uvr\) bounds a small triangle inside that face. Place the second new vertex inside this triangle and join it to all three corners. This adds precisely the five edges needed for the \(K_4\), without crossings.

Thus the specified orientation is planar.

### Every feedback vertex set has at least three vertices

The graph contains the following five directed triangles:
\[
\begin{aligned}
C_0&:a\to b\to c\to a,\\
C_a&:a\to x\to y\to a,\\
C_b&:b\to x\to y\to b,\\
C_x&:x\to p\to q\to x,\\
C_y&:y\to p\to q\to y.
\end{aligned}
\]

Suppose a set \(S\) of at most two vertices meets every directed cycle.

To meet \(C_0\), the set \(S\) must contain a vertex of \(\{a,b,c\}\). Since both \(C_x\) and \(C_y\) are disjoint from \(\{a,b,c\}\), the at most one remaining vertex of \(S\) must meet both of them. It must therefore belong to
\[
V(C_x)\cap V(C_y)=\{p,q\}.
\]

Consequently \(S\) contains neither \(x\) nor \(y\). Meeting \(C_a\) now requires \(a\in S\), while meeting \(C_b\) requires \(b\in S\). Together with the required vertex in \(\{p,q\}\), this gives \(|S|\ge3\), a contradiction.

Thus every feedback vertex set has size at least three, and
\[
\alpha_{\mathrm{ac}}(D)\le 7-3=4.
\]
Equality holds: the vertices \(\{c,a,x,p\}\) induce exactly the directed path
\[
c\to a\to x\to p.
\]
Therefore
\[
\boxed{\alpha_{\mathrm{ac}}(D)=4<\frac35\cdot7=\frac{21}{5}.}
\]

This disproves the conjecture as stated.

## 2. An infinite family approaching the fraction \(1/2\)

The counterexample extends to a family with an exact, easily proved acyclic induced order.

### Construction

For each integer \(k\ge1\), let \(D_k\) have vertices
\[
\{z\}\cup\{a_i,b_i:1\le i\le k\}.
\]
Start with the directed triangle
\[
a_1\to b_1\to z\to a_1.
\]
For each \(i=2,\ldots,k\), add the five arcs
\[
a_{i-1}\to a_i,\qquad
b_{i-1}\to a_i,\qquad
a_i\to b_i,\qquad
b_i\to a_{i-1},\qquad
b_i\to b_{i-1}.
\]

At every step, the underlying graph gains a \(K_4\) glued along the existing edge \(a_{i-1}b_{i-1}\). Hence every \(D_k\) is planar and oriented, with
\[
|V(D_k)|=2k+1.
\]
The seven-vertex example above is \(D_3\).

### Exact acyclic induced order

We prove
\[
\boxed{\alpha_{\mathrm{ac}}(D_k)=k+1.}
\]

Let \(A\) induce an acyclic subdigraph, and put
\[
s_i=|A\cap\{a_i,b_i\}|\in\{0,1,2\}.
\]
For \(i\ge2\), if \(s_i=2\), then \(s_{i-1}=0\). Indeed, retaining either preceding vertex would retain one of the directed triangles
\[
a_{i-1}\to a_i\to b_i\to a_{i-1},
\qquad
b_{i-1}\to a_i\to b_i\to b_{i-1}.
\]

Let \(N_0\) and \(N_2\) count the indices with \(s_i=0\) and \(s_i=2\), respectively. Each index \(i\ge2\) with \(s_i=2\) has a distinct preceding index with value zero. Thus
\[
N_2\le N_0+\mathbf 1_{\{s_1=2\}}.
\]
Also, if \(s_1=2\), then \(z\notin A\), because \(a_1b_1z\) is a directed triangle. Consequently
\[
\begin{aligned}
|A|
&=k-N_0+N_2+\mathbf 1_{\{z\in A\}}\\
&\le k+\mathbf 1_{\{s_1=2\}}+\mathbf 1_{\{z\in A\}}\\
&\le k+1.
\end{aligned}
\]

Conversely,
\[
\{z,a_1,a_2,\ldots,a_k\}
\]
induces exactly the directed path
\[
z\to a_1\to a_2\to\cdots\to a_k.
\]
This proves the claimed equality.

It follows that
\[
\frac{\alpha_{\mathrm{ac}}(D_k)}{|V(D_k)|}
=\frac{k+1}{2k+1}
=\frac12+\frac{1}{4k+2}
\longrightarrow\frac12.
\]
For every \(k\ge3\),
\[
k+1<\frac35(2k+1).
\]

## 3. Scope and status

The construction shows more than a small rounding obstruction: **no universal bound \(\alpha_{\mathrm{ac}}(D)\ge c|V(D)|\) with \(c>1/2\) can hold for all planar oriented graphs.** It does not establish a matching universal \(1/2\) lower bound.

The disproof is entirely explicit and does not depend on a literature citation. I have not independently verified its historical provenance, so I make no novelty claim. The supplied catalog’s assertion that the stated \(3/5\) conjecture remains open cannot be correct.