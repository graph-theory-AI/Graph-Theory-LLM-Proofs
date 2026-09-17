```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sharp special-case bound establishes Tuza's inequality whenever each edge lies in at most two triangles.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved, and novelty of this special case is not claimed."
}
```

## 1. A sharp restricted result

All graphs below are finite and simple. I do not obtain a proof or counterexample for arbitrary graphs. The following is the concrete partial result.

**Theorem.** Suppose every edge of \(G\) belongs to at most two triangles. Let \(q(G)\) be the number of four-vertex sets spanning a \(K_4\). Then
\[
\boxed{\quad
\tau(G)\le
\left\lfloor\frac{3\nu(G)+q(G)}2\right\rfloor
\le 2\nu(G).
\quad}
\]
In particular, if \(G\) is also \(K_4\)-free, then
\[
\tau(G)\le \frac32\nu(G).
\]
The first bound, including its rounding, is sharp.

The proof uses the special structure of the graph recording which triangles share edges.

## 2. Exact reduction to an ordinary graph

Let \(H\) have one vertex for each triangle of \(G\), with two vertices adjacent precisely when the corresponding triangles share an edge. Write
\[
N=|V(H)|,
\]
and let \(\alpha(H)\) and \(\mu(H)\) denote its independence number and maximum matching size.

Under the hypothesis that every edge belongs to at most two triangles,
\[
\boxed{\qquad
\nu(G)=\alpha(H),\qquad \tau(G)=N-\mu(H).
\qquad} \tag{1}
\]

The first identity follows directly from the definition.

For the upper bound in the second identity, take a maximum matching \(M\) of \(H\). For every matched pair of triangles, select their common edge in \(G\). For every unmatched triangle, select any one of its edges. This gives a transversal of size at most
\[
|M|+(N-2|M|)=N-\mu(H).
\]

For the reverse inequality, let \(X\) be any triangle transversal. Assign each triangle to one edge of \(X\) that it contains. Every selected edge receives at most two assignments. If \(a\) selected edges receive two assignments and \(b\) receive one, then
\[
N=2a+b,\qquad a+b\le |X|.
\]
The \(a\) pairs of triangles assigned to the same edge form a matching in \(H\), since every triangle was assigned exactly once. Hence
\[
\mu(H)\ge a\ge N-|X|,
\]
which proves (1).

In particular, a minimum triangle transversal can be computed in polynomial time in this class: enumerate the triangles, construct \(H\), and find a maximum matching.

### The structure of \(H\)

Every vertex of \(H\) has degree at most three. Indeed, each of the three edges of a triangle can belong to at most one other triangle.

Moreover:

**Claim.** Every triangle in \(H\) belongs to a connected component isomorphic to \(K_4\), arising from a \(K_4\) in \(G\).

To prove this, consider three pairwise adjacent triangles of \(G\). Their three pairwise shared edges must be distinct, since no edge belongs to three triangles. Label the first triangle \(abc\), and arrange that the second and third share \(ab\) and \(ac\), respectively, with it. Write them as \(abx\) and \(acy\). Their adjacency forces \(x=y\): the vertices \(b\) and \(c\) cannot supply their second common vertex.

Thus the three triangles are
\[
abc,\quad abx,\quad acx.
\]
All six edges on \(\{a,b,c,x\}\) are present, so \(bcx\) is also a triangle. Every edge of this \(K_4\) already belongs to two of its four triangles. Consequently, no outside triangle can share an edge with it. The four triangles therefore form an entire \(K_4\) component of \(H\). ∎

Conversely, every \(K_4\) in \(G\) gives such a component. Consequently,
\[
H=qK_4\;\dot\cup\;H_0, \tag{2}
\]
where \(q=q(G)\) and \(H_0\) is triangle-free with maximum degree at most three. This also shows that distinct \(K_4\)'s in \(G\) share no edges and that
\[
q\le \nu(G).
\]

## 3. A matching–independence lemma

The remaining ingredient is an ordinary graph inequality.

**Lemma.** If \(F\) is triangle-free and has maximum degree at most three, then
\[
|V(F)|-\mu(F)\le \frac32\alpha(F). \tag{3}
\]

### Step 1: Independent sets in connected components

We first prove that every nonempty connected triangle-free subcubic graph \(C\) satisfies
\[
3\alpha(C)\ge
\begin{cases}
|V(C)|+1,& C\text{ is not cubic},\\
|V(C)|,& C\text{ is cubic}.
\end{cases} \tag{4}
\]

Suppose \(C\) is not cubic. Every nonempty induced subgraph of \(C\) has a vertex of degree at most two. Otherwise, its vertices would all have degree three within that induced subgraph, leaving no edge to the rest of the connected graph \(C\); this would force the induced subgraph to be all of \(C\), contrary to \(C\) not being cubic.

Construct an independent set greedily: choose a minimum-degree vertex of the current graph and delete its closed neighborhood. Each step deletes at most three vertices. The last step deletes at most two vertices. Indeed, if it deleted three, the last remaining graph would have three vertices and minimum degree two, and hence would be a triangle.

If \(a\) vertices were selected, then
\[
|V(C)|\le 3(a-1)+2=3a-1,
\]
proving the first part of (4).

Now suppose \(C\) is cubic. Select a vertex \(v\) and delete \(N[v]\), which has four vertices. The remaining graph is nonempty: a simple cubic graph on four vertices is \(K_4\), which is not triangle-free. Each remaining connected component is noncubic, because a cubic component would have no edge to \(N[v]\), contradicting the connectedness of \(C\).

If the remaining components are \(C_1,\ldots,C_t\), then \(t\ge1\), and the first part of (4) gives
\[
\alpha(C)
\ge 1+\sum_{i=1}^t\alpha(C_i)
\ge 1+\frac{|V(C)|-4+t}{3}
\ge \frac{|V(C)|}{3}.
\]
This proves (4).

A cubic graph has even order. Therefore (4) implies the convenient uniform statement
\[
3\alpha(C)\ge |V(C)|+\mathbf 1_{\{|V(C)|\text{ odd}\}}. \tag{5}
\]

### Step 2: Apply the Tutte–Berge formula

The Tutte–Berge formula guarantees a set \(S\subseteq V(F)\) such that
\[
|V(F)|-2\mu(F)=o(F-S)-|S|,
\]
where \(o(F-S)\) is the number of odd-order components of \(F-S\).

Apply (5) to every component of \(F-S\). Their independent sets can be combined, so
\[
\begin{aligned}
3\alpha(F)
&\ge 3\alpha(F-S)\\
&\ge |V(F)|-|S|+o(F-S)\\
&=2\bigl(|V(F)|-\mu(F)\bigr).
\end{aligned}
\]
This is (3). The empty graph satisfies it as well. ∎

## 4. Proof of the theorem

By (1) and (2),
\[
\nu(G)=q+\alpha(H_0)
\]
and
\[
\tau(G)=2q+\bigl(|V(H_0)|-\mu(H_0)\bigr).
\]
Apply the lemma to \(H_0\):
\[
\begin{aligned}
\tau(G)
&\le 2q+\frac32\alpha(H_0)\\
&=2q+\frac32\bigl(\nu(G)-q\bigr)\\
&=\frac{3\nu(G)+q}{2}.
\end{aligned}
\]
Taking the floor gives the asserted integer bound. Since \(q\le\nu(G)\), this is at most \(2\nu(G)\). ∎

## 5. Sharpness

Let \(W_5\) denote the wheel formed from a five-cycle by adding a vertex adjacent to all five cycle vertices. Its only triangles are its five spokes-and-rim triangles. Their intersection graph is \(C_5\), so (1) gives
\[
\nu(W_5)=2,\qquad \tau(W_5)=3.
\]
Every edge belongs to at most two triangles, and \(W_5\) is \(K_4\)-free. Thus the factor \(3/2\) cannot be improved in that subclass.

For the complete bound, take a disjoint union of

- \(q\) copies of \(K_4\);
- \(r\) copies of \(W_5\);
- \(s\) copies of \(K_3\), where \(s\in\{0,1\}\).

Then
\[
\nu(G)=q+2r+s,\qquad
\tau(G)=2q+3r+s,
\]
and the number of \(K_4\)'s is exactly \(q\). Therefore
\[
\tau(G)=
\left\lfloor\frac{3\nu(G)+q}{2}\right\rfloor.
\]
This realizes equality for every integer pair \(0\le q\le\nu(G)\).

## 6. A deletion extension and the remaining gap

There is also a direct quantitative extension to arbitrary graphs. Let
\[
B=\{e\in E(G):e\text{ belongs to at least three triangles of }G\},
\]
put \(b=|B|\), and let \(G_0=G-B\). Write \(q_0=q(G_0)\). Deleting \(B\) and then applying the theorem gives
\[
\boxed{\quad
\tau(G)\le
b+\left\lfloor\frac{3\nu(G_0)+q_0}{2}\right\rfloor
\le
\left\lfloor\frac{3\nu(G)+q_0+2b}{2}\right\rfloor.
\quad}
\]
In particular, Tuza's inequality follows whenever
\[
2b+q_0\le \nu(G)+1.
\]
This is a sufficient condition, not a universal bound on \(b\).

The unrestricted problem remains untouched when many high-multiplicity edges interact. Both essential features of the proof can then fail:

1. one selected edge can cover more than two triangles, so \(\tau(G)=|V(H)|-\mu(H)\) need not hold;
2. triangles in \(H\) need not arise from isolated \(K_4\)'s in \(G\).

For example, five triangles sharing one common edge have \(\tau=\nu=1\), but their intersection graph is \(K_5\), for which
\[
|V(H)|-\mu(H)=3.
\]
This is not a counterexample to Tuza's conjecture; it demonstrates the loss of information in the pairwise matching reduction once an edge belongs to more than two triangles. No argument above controls that general case.