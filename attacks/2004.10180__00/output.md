```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The problem is equivalent up to a factor of three to the extremal problem for linear 3-graphs of Berge girth at least six, and an explicit moment-curve construction gives a lower bound \u03a9(n^{4/3}), leaving the exponent between 4/3 and 3/2.",
  "would_publish": false,
  "caveats": "No n^{3/2-o(1)} construction or fixed power-saving upper bound is obtained; the literature novelty of the 4/3 construction was not checked."
}
```

# Mathematical writeup

## 1. Formulation

For a graph \(G\), let
\[
\tau_\triangle(G)=\min\{|F|:F\subseteq E(G),\ G-F\text{ is triangle-free}\},
\]
and define
\[
f(n)=\max\{\tau_\triangle(G): |V(G)|=n,\ G\text{ is }C_5\text{-free}\}.
\]

Corollary 1.4 in the source says
\[
f(n)=o(n^{3/2}).
\]
Thus “\(3/2\) is best possible” cannot mean \(f(n)=\Omega(n^{3/2})\), which would contradict the little-\(o\) statement. The natural precise interpretation is
\[
f(n)=n^{3/2-o(1)}
\quad\text{along an infinite sequence,}
\]
or equivalently that there is no fixed \(\varepsilon>0\) for which
\[
f(n)=O(n^{3/2-\varepsilon}).
\]

I prove below that this is, up to a constant factor, exactly an extremal problem for 3-uniform hypergraphs of Berge girth at least six. I also give an explicit construction showing
\[
f(n)=\Omega(n^{4/3}).
\]

---

## 2. Reduction to high-girth linear triple systems

A 3-uniform hypergraph \(\mathcal H\) is linear if two distinct hyperedges meet in at most one vertex. A Berge cycle of length \(k\) consists of distinct hyperedges
\[
E_1,\ldots,E_k
\]
and distinct vertices
\[
v_1,\ldots,v_k
\]
such that
\[
\{v_i,v_{i+1}\}\subseteq E_i
\]
for every \(i\), with indices taken cyclically.

Let \(h(n)\) be the maximum number of hyperedges in an \(n\)-vertex linear 3-uniform hypergraph with no Berge cycle of length \(3,4,\) or \(5\).

### Lemma 2.1
Let \(\mathcal H\) be a linear 3-uniform hypergraph and let \(\partial_2\mathcal H\) be its 2-shadow, obtained by replacing each hyperedge by a triangle. Then
\[
\partial_2\mathcal H\text{ is }C_5\text{-free}
\quad\Longleftrightarrow\quad
\mathcal H\text{ has no Berge cycle of length }3,4,5.
\]

#### Proof

First suppose that \(\mathcal H\) has a Berge cycle.

- For a Berge \(5\)-cycle, the core vertices \(v_1,\ldots,v_5\) themselves form a \(C_5\) in the shadow.

- For a Berge \(4\)-cycle, write
  \[
  E_i\supseteq\{v_i,v_{i+1}\}.
  \]
  If \(w\) is the third vertex of \(E_1\), linearity ensures that \(w\) is distinct from all four core vertices. Then
  \[
  v_1,w,v_2,v_3,v_4,v_1
  \]
  is a \(C_5\) in the shadow.

- For a Berge \(3\)-cycle, let \(w_1,w_2\) be the third vertices of \(E_1,E_2\). Linearity ensures that
  \[
  v_1,w_1,v_2,w_2,v_3,v_1
  \]
  is a \(C_5\).

Conversely, suppose that
\[
v_1v_2v_3v_4v_5v_1
\]
is a \(C_5\) in \(\partial_2\mathcal H\). By linearity, each cycle edge \(v_iv_{i+1}\) is contained in a unique hyperedge \(E_i\).

One hyperedge can contain two consecutive cycle edges, but it cannot contain two nonconsecutive cycle edges, since those two graph edges have four distinct endpoints. Nor can one hyperedge contain three cycle edges. Thus, in the cyclic word
\[
E_1,E_2,E_3,E_4,E_5,
\]
equal entries occur only in disjoint adjacent pairs. Contract every adjacent equal pair. This produces between three and five distinct hyperedges, and the remaining boundary vertices give a Berge cycle of the corresponding length. Hence \(\mathcal H\) has a Berge cycle of length \(3,4,\) or \(5\). ∎

### Proposition 2.2
For every \(n\),
\[
h(n)\le f(n)\le 3h(n).
\]

#### Proof

For the lower bound, let \(\mathcal H\) be an \(n\)-vertex linear triple system counted by \(h(n)\), and put
\[
G=\partial_2\mathcal H.
\]
By Lemma 2.1, \(G\) is \(C_5\)-free. The triangles corresponding to distinct hyperedges of \(\mathcal H\) are edge-disjoint, so any triangle-hitting edge set must contain at least one edge from each of them. Therefore
\[
\tau_\triangle(G)\ge e(\mathcal H),
\]
and hence \(f(n)\ge h(n)\).

For the other direction, let \(G\) be an \(n\)-vertex \(C_5\)-free graph, and take a maximal family \(\mathcal T\) of pairwise edge-disjoint triangles of \(G\). Regard the members of \(\mathcal T\) as hyperedges. They form a linear 3-uniform hypergraph, and their shadow is a subgraph of \(G\), hence is \(C_5\)-free. Lemma 2.1 gives
\[
|\mathcal T|\le h(n).
\]

By maximality, every triangle of \(G\) shares a graph edge with some member of \(\mathcal T\). Deleting all three edges of every triangle in \(\mathcal T\) therefore makes \(G\) triangle-free. Thus
\[
\tau_\triangle(G)\le 3|\mathcal T|\le 3h(n).
\]
Taking the maximum over \(G\) proves the claim. ∎

Consequently, the exponent question is exactly equivalent to asking whether
\[
h(n)=n^{3/2-o(1)}.
\]

---

## 3. An explicit \(\Omega(n^{4/3})\) construction

### Theorem 3.1
There is an absolute constant \(c>0\) such that, for all sufficiently large \(n\), there exists an \(n\)-vertex \(C_5\)-free graph \(G\) with
\[
\tau_\triangle(G)\ge c n^{4/3}.
\]

It is enough to construct linear 3-uniform hypergraphs of Berge girth at least six with \(\Omega(n^{4/3})\) edges.

### 3.1 Field and moment curve

Let
\[
q=23^{\,2s+1}
\]
and let \(K=\mathbb F_q\). The elements \(-2\) and \(10\) are nonsquares in \(\mathbb F_{23}\), and they remain nonsquares in every odd-degree extension \(K/\mathbb F_{23}\).

Set
\[
\phi(a)=(a,a^2,a^3)\in K^3.
\]
Let \(V_0,V_1,V_2\) be three disjoint copies of \(K^3\). Put
\[
d_0=0,\qquad d_1=1,\qquad d_2=3.
\]

For every \(x\in K^3\) and \(a\in K\), define the hyperedge
\[
E(x,a)=
\bigl\{
(0,x),\,
(1,x+\phi(a)),\,
(2,x+3\phi(a))
\bigr\}.
\]
Let \(\mathcal H_q\) be the resulting 3-uniform hypergraph.

It has
\[
|V(\mathcal H_q)|=3q^3,\qquad
e(\mathcal H_q)=q^4.
\]

### 3.2 Linearity

Suppose \(E(x,a)\) and \(E(y,b)\) share vertices in two distinct parts \(i,j\). Then
\[
x+d_i\phi(a)=y+d_i\phi(b),
\]
and
\[
x+d_j\phi(a)=y+d_j\phi(b).
\]
Subtracting gives
\[
(d_i-d_j)(\phi(a)-\phi(b))=0.
\]
All differences among \(0,1,3\) are nonzero in characteristic \(23\), so \(\phi(a)=\phi(b)\). Looking at the first coordinate gives \(a=b\), and then \(x=y\). Hence \(\mathcal H_q\) is linear.

### 3.3 The cycle equation

Suppose
\[
E(x_1,a_1),\ldots,E(x_k,a_k)
\]
form a Berge cycle. Let \(p_j\in\{0,1,2\}\) be the part containing the intersection of \(E(x_j,a_j)\) and \(E(x_{j+1},a_{j+1})\).

The two core vertices contained in any one hyperedge are distinct, so
\[
p_{j-1}\ne p_j.
\]
Thus \(p_1,\ldots,p_k\) is a proper 3-coloring of the cycle \(C_k\).

At the intersection in part \(p_j\),
\[
x_j+d_{p_j}\phi(a_j)
=
x_{j+1}+d_{p_j}\phi(a_{j+1}).
\]
Summing around the cycle gives
\[
\sum_{j=1}^k
\bigl(d_{p_j}-d_{p_{j-1}}\bigr)\phi(a_j)=0.
\tag{3.1}
\]

We show that for \(k=3,4,5\), equation (3.1) forces two consecutive parameters \(a_j,a_{j+1}\) to be equal. Since the corresponding hyperedges intersect, equality of their parameters would force equality of the whole hyperedges:
\[
E(x_j,a_j)=E(x_{j+1},a_{j+1}),
\]
contrary to the definition of a Berge cycle.

#### Berge triangles

A proper coloring of \(C_3\) uses all three parts. Thus (3.1) has the form
\[
\alpha\phi(a)+\beta\phi(b)+\gamma\phi(c)=0,
\qquad
\alpha+\beta+\gamma=0,
\]
where \(\alpha,\beta,\gamma\) are all nonzero.

Translate so that \(c=0\). From the first two coordinates,
\[
\alpha a+\beta b=0,\qquad
\alpha a^2+\beta b^2=0.
\]
Substitution gives
\[
-\frac{\alpha\gamma}{\beta}a^2=0.
\]
Hence \(a=b=0\), so all three parameters are equal. Thus there is no Berge \(3\)-cycle.

#### Berge \(4\)-cycles

If the part sequence uses only two parts, it alternates. Equation (3.1), using its first two coordinates, says that two unordered pairs of parameters have the same sum and sum of squares. Hence the pairs are equal as multisets. Every resulting matching identifies two consecutive positions of the \(4\)-cycle.

Otherwise, after rotation, the part sequence is
\[
A,B,A,C,
\]
where \(A,B,C\) are distinct elements of \(\{0,1,3\}\). Put
\[
\rho=A-C,\qquad \sigma=B-A.
\]
Then (3.1) becomes
\[
\rho\bigl(\phi(a_1)-\phi(a_4)\bigr)
=
\sigma\bigl(\phi(a_3)-\phi(a_2)\bigr).
\tag{3.2}
\]

Assume no consecutive parameters are equal. Comparing the first, second, and third coordinates of (3.2) gives
\[
a_1+a_4=a_2+a_3,
\]
and
\[
a_1a_4=a_2a_3.
\]
Thus
\[
\{a_1,a_4\}=\{a_2,a_3\}.
\]
The only matching that does not already identify consecutive positions is
\[
a_1=a_3,\qquad a_4=a_2.
\]
Substitution into the first coordinate of (3.2) then gives \(\rho=\sigma\), equivalently
\[
2A=B+C.
\]
But no member of \(\{0,1,3\}\) is the midpoint of the other two in characteristic \(23\):
\[
2\cdot0\ne1+3,\qquad
2\cdot1\ne0+3,\qquad
2\cdot3\ne0+1.
\]
Hence there is no Berge \(4\)-cycle.

#### Berge \(5\)-cycles

Every proper 3-coloring of \(C_5\), after rotation and reversal, has the form
\[
A,B,A,B,C,
\]
where \(A,B,C\) are distinct.

Set
\[
\xi=B-A,\qquad
\lambda=\frac{C-B}{B-A}.
\]
Writing (3.1) coordinatewise and translating all parameters by \(a_3\), define
\[
X=a_1-a_3,\quad
u=a_2-a_3,\quad
v=a_4-a_3,\quad
Z=a_5-a_3.
\]
For \(r=1,2,3\), equation (3.1) becomes
\[
u^r+v^r+\lambda Z^r=(1+\lambda)X^r.
\tag{3.3}
\]

We need the following elementary calculation.

### Lemma 3.2
Assume \(\lambda\notin\{0,-1,-2\}\). Every solution of (3.3) either satisfies \(Z=X\), or satisfies
\[
Z=\frac{\lambda-1}{\lambda+2}X,
\]
and the quadratic with roots \(u,v\) has discriminant
\[
\Delta=-2\frac{\lambda-1}{\lambda+2}X^2.
\tag{3.4}
\]

#### Proof

Let
\[
S=u+v,\qquad P=uv.
\]
The first two equations in (3.3) give
\[
S=(1+\lambda)X-\lambda Z
\]
and determine \(P\). Substituting these into
\[
u^3+v^3=S^3-3PS
\]
and comparing with the third equation in (3.3) yields
\[
\frac{\lambda(\lambda+1)}2
(X-Z)^2
\bigl((1-\lambda)X+(\lambda+2)Z\bigr)=0.
\]
This gives the two stated alternatives. In the second alternative, direct substitution into \(S^2-4P\) gives (3.4). ∎

For the six possible orderings of \(A,B,C\in\{0,1,3\}\), the values of \(\lambda\) and the nonsquare factor in (3.4) are:

\[
\begin{array}{c|c|c}
\lambda&
-2(\lambda-1)/(\lambda+2)&
\text{square class}\\
\hline
2&-1/2&-2\\
1/2&2/5&10\\
-2/3&5/2&10\\
-3/2&10&10\\
-3&-8&-2\\
-1/3&8/5&10
\end{array}
\]

Here “square class” means equality up to multiplication by a nonzero square. Since both \(-2\) and \(10\) are nonsquares in \(K\), the discriminant in the second alternative of Lemma 3.2 is a nonsquare whenever \(X\ne0\). But the discriminant of a quadratic having roots \(u,v\in K\) is \((u-v)^2\), a square. Therefore the second alternative is impossible unless \(X=0\), in which case it also gives \(Z=0\).

Thus every solution has
\[
X=Z,
\]
that is,
\[
a_1=a_5.
\]
These are consecutive cyclic positions, so the corresponding adjacent hyperedges would be identical. Hence there is no Berge \(5\)-cycle.

We have proved that \(\mathcal H_q\) is linear and has no Berge cycle of length \(3,4,\) or \(5\).

---

## 4. The resulting graph

Let
\[
G_q=\partial_2\mathcal H_q.
\]
By Lemma 2.1, \(G_q\) is \(C_5\)-free.

The \(q^4\) hyperedges of \(\mathcal H_q\) give \(q^4\) pairwise edge-disjoint triangles in \(G_q\), so
\[
\tau_\triangle(G_q)\ge q^4.
\]
Conversely, deleting all edges between \(V_0\) and \(V_1\) deletes exactly one edge from each of these triangles. The remaining graph is bipartite with bipartition
\[
V_0\cup V_1,\qquad V_2.
\]
Hence
\[
\tau_\triangle(G_q)=q^4.
\]

Since
\[
|V(G_q)|=3q^3,
\]
this is
\[
\tau_\triangle(G_q)
=
3^{-4/3}|V(G_q)|^{4/3}.
\]

The allowed field sizes satisfy \(q_{s+1}=23^2q_s\). For an arbitrary sufficiently large \(n\), choose the largest such \(q\) with \(3q^3\le n\) and add isolated vertices. This gives an absolute \(c>0\) with
\[
f(n)\ge c n^{4/3}.
\]

Combining this with Corollary 1.4,
\[
\boxed{\quad
c n^{4/3}\le f(n)=o(n^{3/2}).
\quad}
\]

In particular, no universal bound \(o(n^{4/3})\) is possible.

---

## 5. Remaining gap

The original question remains unresolved by this argument. By Proposition 2.2, proving optimality of \(3/2\) amounts to constructing linear 3-uniform hypergraphs of Berge girth at least six with
\[
n^{3/2-o(1)}
\]
hyperedges. Disproving optimality requires a fixed \(\varepsilon>0\) and an upper bound
\[
h(n)=O(n^{3/2-\varepsilon}).
\]
Neither is obtained here.

There is also a consistency check concerning the prompt’s summary of Proposition 1.7. If that proposition actually supplied \(r\)-uniform hypergraphs of standard Berge girth greater than five with \(n^{3/2-o(1)}\) edges, one could choose an arbitrary triple inside each hyperedge; Berge girth would be preserved, and the resulting 3-graph would settle the present problem affirmatively. Thus the exact proposition must have a weaker girth hypothesis, a different notion of girth, or some other restriction preventing that transfer. I have not used it without the exact statement.