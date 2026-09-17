```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The intended bound holds for every real p >= 2 when the graph has at most two negative adjacency eigenvalues, and also for every connected graph of adjacency rank at most four.",
  "would_publish": false,
  "caveats": "The general K_n-comparator conjecture is not resolved; novelty of these special cases has not been checked."
}
```

## 1. Target and partial result

I use the intended formulation identified in the supplied correction:
\[
\mathcal E_p^-(G)\ge \mathcal E_p^-(K_n)=n-1
\qquad(p\ge2).
\tag{C}
\]
The previous \(K_3\) example is discarded as a counterexample to this formulation: its negative \(p\)-energy is exactly \(2=n-1\).

All graphs below are finite and simple. Write \(\nu_+(G)\) and \(\nu_-(G)\) for the numbers of positive and negative adjacency eigenvalues, counted with multiplicity.

### Theorem
Let \(G\) be a connected graph of order \(n\). If either
\[
\nu_-(G)\le2
\qquad\text{or}\qquad
\nu_+(G)=1,
\]
then
\[
\mathcal E_p^-(G)\ge n-1
\]
for every real \(p\ge2\).

Consequently, the conjecture holds for:

- every connected graph with vertex-cover number at most two;
- every connected graph whose adjacency matrix has rank at most four.

The proof is self-contained. The substantive case is \(\nu_-(G)\le2\).

## 2. Passing from \(p=2\) to all real \(p\ge2\)

Suppose \(n\ge2\), and let \(a_1,\dots,a_q>0\) be the magnitudes of the negative eigenvalues. Since a nonempty graph has a positive adjacency eigenvalue, \(1\le q\le n-1\). The power-mean inequality gives
\[
\mathcal E_p^-(G)
\ge q^{1-p/2}\bigl(\mathcal E_2^-(G)\bigr)^{p/2}.
\]
Thus, if \(\mathcal E_2^-(G)\ge n-1\), then
\[
\mathcal E_p^-(G)
\ge (n-1)\left(\frac{n-1}{q}\right)^{p/2-1}
\ge n-1.
\tag{1}
\]
The one-vertex case is immediate.

In particular, a proof of the unrestricted \(p=2\) conjecture would settle the entire real-\(p\) formulation. Below it suffices to work at \(p=2\).

Set
\[
s(H)=\mathcal E_2^-(H),\qquad
t(H)=\mathcal E_1^-(H).
\]
Because adjacency matrices have trace zero, \(t(H)\) is also the sum of the positive eigenvalues.

## 3. Three spectral facts

### 3.1. Induced-subgraph monotonicity

If \(H\) is an induced subgraph of \(G\), Cauchy interlacing gives
\[
t(H)\le t(G).
\tag{2}
\]
Indeed, each of the negative eigenvalues of \(H\), ordered increasingly, is bounded below by the corresponding eigenvalue of \(G\). Summing their negative magnitudes proves (2).

### 3.2. Graphs with one positive eigenvalue

Let \(H\) be connected, with \(h\ge2\) vertices and \(b\) edges. For each vertex \(v\),
\[
\begin{aligned}
\sum_{u\in N(v)}d(u)
&=2b-d(v)-\sum_{\substack{w\ne v\\w\notin N(v)}}d(w)\\
&\le 2b-d(v)-\bigl(h-1-d(v)\bigr)\\
&=2b-h+1.
\end{aligned}
\]
The left side is the \(v\)-th row sum of \(A(H)^2\). Hence
\[
\rho(H)^2\le 2b-h+1.
\tag{3}
\]
If \(\nu_+(H)=1\), then
\[
s(H)=2b-\rho(H)^2\ge h-1.
\tag{4}
\]
This proves the one-positive-eigenvalue case of the theorem.

We will use (4) for complete multipartite graphs. Such a nonempty graph has exactly one positive eigenvalue: if its parts are \(V_1,\dots,V_r\), then on the codimension-one subspace \(\sum_v x_v=0\),
\[
x^\top A(H)x
=-\sum_{i=1}^r\left(\sum_{v\in V_i}x_v\right)^2\le0.
\]
Thus there is at most one positive eigenvalue, and nonemptiness supplies one. Consequently,
\[
s(H)\ge |V(H)|-1
\tag{5}
\]
for every connected complete multipartite graph, including the trivial one-vertex case.

Also, a complete multipartite graph with at most three parts has adjacency rank at most three, since vertices in the same part have identical rows. It therefore has at most two negative eigenvalues.

### 3.3. A third-moment identity when \(\nu_-\le2\)

Let \(H\) be nonempty with at most two negative eigenvalues. Denote its edge and triangle counts by \(m\) and \(\tau\). Pad the negative eigenvalues with zero if necessary, writing them as \(-a,-b\), with \(a,b\ge0\). Let its positive eigenvalues be \(x_1,\dots,x_r\), and put
\[
t=\sum_i x_i=a+b,\qquad
u=\sum_{i<j}x_ix_j,\qquad
v=\sum_{i<j<k}x_ix_jx_k.
\]
In particular, \(v\ge0\).

Using \(\operatorname{tr}A^2=2m\) and \(\operatorname{tr}A^3=6\tau\),
\[
2m=(t^2-2u)+(t^2-2ab),
\]
and
\[
6\tau=(t^3-3tu+3v)-(t^3-3tab).
\]
Eliminating \(u-ab\) yields
\[
\boxed{\quad s(H)=m+\frac{v-2\tau}{t(H)}.\quad}
\tag{6}
\]

Two consequences are important:

- If \(H\) is triangle-free, then
  \[
  s(H)\ge m.
  \tag{7}
  \]
- If \(H\) also has at most two positive eigenvalues, then \(v=0\), so
  \[
  s(H)=m-\frac{2\tau}{t(H)}.
  \tag{8}
  \]

## 4. Structure forced by a triangle and \(\nu_-\le2\)

Now suppose \(G\) is connected, \(\nu_-(G)\le2\), and \(G\) contains a triangle \(v_1v_2v_3\).

Order these three vertices first and write
\[
A(G)=
\begin{pmatrix}
B&C\\
C^\top&D
\end{pmatrix},
\qquad B=J_3-I_3.
\]
Since
\[
B^{-1}=\frac12J_3-I_3
\]
and \(B\) has two negative eigenvalues, block Gaussian congruence and Sylvester’s law of inertia show that
\[
M:=D-C^\top B^{-1}C
\]
is positive semidefinite.

For a vertex \(w\) outside the triangle, let
\[
d_T(w)=|N(w)\cap\{v_1,v_2,v_3\}|.
\]
Its diagonal entry in \(M\) is
\[
M_{ww}=d_T(w)-\frac{d_T(w)^2}{2}.
\tag{9}
\]
Thus \(d_T(w)\ne3\). If \(d_T(w)=0\), then \(M_{ww}=0\); positive semidefiniteness forces the whole \(w\)-th row of \(M\) to be zero. Since the corresponding column of \(C\) is zero, \(w\) would be isolated in \(G\), contrary to connectedness. Therefore every outside vertex has exactly one or two neighbors on the triangle.

For \(i=1,2,3\), define
\[
X_i=\{v_i\}\cup
\{w:N(w)\cap\{v_1,v_2,v_3\}
=\{v_1,v_2,v_3\}\setminus\{v_i\}\},
\]
and
\[
Y_i=\{w:N(w)\cap\{v_1,v_2,v_3\}=\{v_i\}\}.
\]

Vertices with two triangle neighbors have zero diagonal in \(M\), hence zero rows. Substitution into \(D=C^\top B^{-1}C+M\) gives:

1. each \(X_i\) is independent;
2. all edges between \(X_i\) and \(X_j\), \(i\ne j\), are present;
3. a vertex in \(Y_i\) is adjacent to every vertex of \(X_i\), and to no vertex of \(X_j\), \(j\ne i\).

For example, these calculations use
\[
(\mathbf1-e_i)^\top B^{-1}(\mathbf1-e_j)=1-\delta_{ij},
\qquad
(\mathbf1-e_i)^\top B^{-1}e_j=\delta_{ij}.
\]

It remains to determine the graph on \(Y=Y_1\cup Y_2\cup Y_3\). Each of these vertices has \(M_{ww}=1/2\). For distinct \(u,v\),
\[
M_{uv}=
\begin{cases}
A_{uv}+\frac12,&u,v\in Y_i,\\[2mm]
A_{uv}-\frac12,&u\in Y_i,\ v\in Y_j,\ i\ne j.
\end{cases}
\tag{10}
\]
The positive-semidefinite inequality
\[
|M_{uv}|\le\sqrt{M_{uu}M_{vv}}=\frac12
\]
forces each \(Y_i\) to be independent.

Represent \(M\) as a Gram matrix. The Gram vectors corresponding to vertices in \(Y\) have squared norm \(1/2\); by (10), every pair has inner product of magnitude \(1/2\). They are therefore all collinear. Vectors belonging to the same \(Y_i\) are identical. Assigning a sign to each nonempty \(Y_i\), we conclude that two different groups \(Y_i,Y_j\) are completely joined precisely when their signs agree.

Consequently:

- every component of \(G[Y]\) is either a singleton or a connected complete multipartite graph with at most three parts;
- \(\operatorname{rank}M\le1\);
- by inertia additivity,
  \[
  \nu_+(G)=1+\operatorname{rank}M\le2.
  \tag{11}
  \]

Finally, put \(X=X_1\cup X_2\cup X_3\). No triangle meets both \(X\) and \(Y\): the neighbors in \(X\) of a vertex of \(Y_i\) lie in the independent set \(X_i\), and the neighbors in \(Y\) of a vertex of \(X_i\) lie in the independent set \(Y_i\).

## 5. Completing the two-negative-eigenvalue case

If \(G\) is triangle-free, (7) immediately gives
\[
s(G)\ge |E(G)|\ge n-1.
\]

Suppose instead that \(G\) contains a triangle. Use the preceding structure, and partition its vertices into the induced subgraphs
\[
H_0=G[X],\qquad H_1,\dots,H_k,
\]
where \(H_1,\dots,H_k\) are the components of \(G[Y]\).

Every \(H_i\) is connected and complete multipartite with at most three parts, or is a singleton. Let \(m_i,\tau_i\) be its edge and triangle counts. Let \(m_\times\) count edges between distinct blocks. Because all triangles lie within blocks,
\[
m(G)=m_\times+\sum_{i=0}^k m_i,
\qquad
\tau(G)=\sum_{i=0}^k\tau_i.
\tag{12}
\]
Moreover, every \(H_i\), \(i\ge1\), has an edge to \(H_0\), so
\[
m_\times\ge k.
\tag{13}
\]

By (11), \(G\) has at most two positive and two negative eigenvalues. Thus (8) applies to \(G\). It also applies to each nonsingleton \(H_i\). Combining (2), (8), and (12),
\[
\begin{aligned}
s(G)
&=m_\times+
  \sum_{i=0}^k\left(m_i-\frac{2\tau_i}{t(G)}\right)\\
&\ge m_\times+\sum_{i=0}^k s(H_i).
\end{aligned}
\tag{14}
\]
For singleton blocks the corresponding terms are zero, so no division by zero is needed.

Using (5) and (13),
\[
s(G)
\ge k+\sum_{i=0}^k\bigl(|V(H_i)|-1\bigr)
=k+n-(k+1)
=n-1.
\]
This proves the \(p=2\) result for \(\nu_-(G)\le2\). Equation (1) proves it for every real \(p\ge2\). Together with Section 3.2, the theorem is complete. \(\square\)

## 6. Consequences and limitations

If \(G\) has a vertex cover of size at most two, deleting those vertices leaves a zero adjacency matrix. Interlacing therefore gives \(\nu_-(G)\le2\), proving the first stated consequence.

If \(\operatorname{rank}A(G)\le4\), then either \(\nu_-(G)\le2\), or the existence of a positive eigenvalue forces \(\nu_+(G)=1\). This proves the second consequence.

The bound is sharp: complete graphs have one positive eigenvalue and satisfy
\[
\mathcal E_p^-(K_n)=n-1
\]
for every \(p\ge2\).

**What remains unresolved here:** arbitrary connected graphs with at least three negative and at least two positive eigenvalues. The restriction on negative inertia is load-bearing: it makes the triangle Schur complement positive semidefinite, which forces the block structure used above. With three or more negative eigenvalues that Schur complement can be indefinite, and this proof supplies no replacement.

Thus this is a rigorous special-case result for the intended conjecture, not a resolution of the general problem. No claim of literature novelty is made.