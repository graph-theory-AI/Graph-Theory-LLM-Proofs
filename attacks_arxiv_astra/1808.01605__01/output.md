```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when Delta(G)/(chi(G)-1) is bounded, with order-optimal quadratic and cubic thresholds for girths 5–6 and 7–8, respectively.",
  "would_publish": false,
  "caveats": "Arbitrary degree distributions remain uncontrolled; these self-contained special cases are not claimed to be new, and later literature has not been independently checked."
}
```

## 1. A quantitative special case

All graphs below are finite and simple. Subgraphs need not be induced, and forests have infinite girth.

I do not resolve the unrestricted conjecture. The following is a self-contained partial result.

**Theorem 1.** Fix \(A\ge 1\). For every positive integer \(k\) and every \(g\ge 3\), sufficiently large chromatic number forces the desired subgraph within the class
\[
\Delta(G)\le A\bigl(\chi(G)-1\bigr).
\]
For \(g\ge5\), permissible thresholds are
\[
\begin{array}{c|c}
g & c_A(k,g)\\ \hline
5,6 & 1+\left\lceil (12k)^2 A\right\rceil\\[2mm]
7,8 & 1+\left\lceil (32k)^3 A^2\right\rceil\\[2mm]
\text{arbitrary }g\ge5
&1+\left\lceil (32k)^s A^{s-1}\right\rceil,
\quad s=2\left\lfloor\frac{g-1}{2}\right\rfloor-1.
\end{array}
\]
Thus, if \(G\) satisfies the displayed degree condition and
\(\chi(G)\ge c_A(k,g)\), it contains a subgraph of girth at least \(g\) and average degree at least \(k\).

For fixed \(A\), the orders \(k^2\) for girths \(5,6\) and \(k^3\) for girths \(7,8\) cannot be improved.

The proof actually uses a second-moment condition weaker than a maximum-degree bound.

## 2. Sparsification controlled by the second degree moment

For a graph \(G\) with at least one edge, write
\[
d=\overline d(G),\qquad
D=\frac{\sum_{v\in V(G)}d_G(v)^2}{\sum_{v\in V(G)}d_G(v)}.
\]
Notice that
\[
1\le D\le\Delta(G).
\]

We will prove the following three bounds.

**Theorem 2.** Every such \(G\) contains:

1. a subgraph of girth at least \(6\) and average degree at least
   \[
   \frac{d}{12\sqrt D};
   \]
2. a subgraph of girth at least \(8\) and average degree at least
   \[
   \frac{d}{32D^{2/3}};
   \]
3. for every \(g\ge5\), a subgraph of girth at least \(g\) and average degree at least
   \[
   \frac{d}{32D^{1-1/s}},
   \qquad
   s=2\left\lfloor\frac{g-1}{2}\right\rfloor-1.
   \]

The key observation is that a random locally injective homomorphism can be obtained with a collision loss governed by \(D\), rather than by \(\Delta(G)\).

### 2.1. A transfer lemma

**Lemma.** Let \(F\) be a graph of order \(N\), size \(m_F\), and girth at least \(g\). Then \(G\) contains a subgraph \(H\) of girth at least \(g\) satisfying
\[
\overline d(H)\ge
d\,\frac{2m_F}{N^2}
\left(1-\frac{2(D-1)}N\right).
\tag{1}
\]

The bound is useful when the parenthesized factor is positive.

**Proof.** Assign each vertex \(v\in V(G)\) an independent uniform label
\[
f(v)\in V(F).
\]
Retain an edge \(uv\in E(G)\) precisely when:

- \(f(u)f(v)\in E(F)\);
- no other neighbor of \(u\) has label \(f(v)\);
- no other neighbor of \(v\) has label \(f(u)\).

Let \(H\) have all the vertices of \(G\) and the retained edges. The map \(f:H\to F\) is a homomorphism that is injective on every neighborhood.

Consequently, a cycle of \(H\) maps to a closed walk in \(F\) without an immediate reversal. Such a walk contains a cycle of length at most its own length. Hence
\[
\operatorname{girth}(H)\ge\operatorname{girth}(F)\ge g.
\]

For a fixed edge \(uv\),
\[
\Pr\bigl(f(u)f(v)\in E(F)\bigr)=\frac{2m_F}{N^2}.
\]
Conditional on the endpoint labels, a union bound gives collision probability at most
\[
\frac{d_G(u)+d_G(v)-2}{N}.
\]
Thus
\[
\Pr(uv\in E(H))
\ge
\frac{2m_F}{N^2}
\left(1-\frac{d_G(u)+d_G(v)-2}{N}\right).
\]
Writing \(m=|E(G)|\), we have
\[
\sum_{uv\in E(G)}\bigl(d_G(u)+d_G(v)-2\bigr)
=\sum_v d_G(v)^2-2m
=2m(D-1).
\]
Summing the probability bound and taking expectations proves (1). \(\square\)

### 2.2. Girth six: an affine-plane template

Let \(q\) be a power of two. Over \(\mathbb F_q\), form a bipartite graph \(F_q\) with parts
\[
P=\mathbb F_q^2,\qquad L=\mathbb F_q^2,
\]
where the point \((x,y)\) is adjacent to the line label \((a,b)\) exactly when
\[
y=ax+b.
\]

This graph has
\[
N=2q^2,\qquad m_F=q^3.
\]
It has no \(4\)-cycle: two distinct points lie on at most one of these lines. Being bipartite, it therefore has girth at least \(6\).

Choose the smallest power of two satisfying
\[
q\ge\sqrt{2D}.
\]
Then
\[
q<2\sqrt{2D}<3\sqrt D,
\]
and
\[
1-\frac{2(D-1)}N
=1-\frac{D-1}{q^2}\ge\frac12.
\]
Applying the transfer lemma,
\[
\overline d(H)
\ge d\cdot\frac1{2q}\cdot\frac12
=\frac d{4q}
\ge\frac d{12\sqrt D}.
\]
This proves Theorem 2(1).

### 2.3. Girth eight: a symplectic incidence template

Again let \(q\) be a power of two. Equip \(\mathbb F_q^4\) with the nondegenerate alternating form
\[
\langle x,y\rangle
=x_1y_2-x_2y_1+x_3y_4-x_4y_3.
\]

Construct a bipartite incidence graph \(F_q\) whose vertices are:

- the one-dimensional subspaces, called points;
- the two-dimensional totally isotropic subspaces, called lines.

Adjacency is containment.

There are
\[
M=\frac{q^4-1}{q-1}=(q+1)(q^2+1)
\]
points. Every line contains \(q+1\) points. A point \(P\) lies on \(q+1\) lines, because these lines correspond to the one-dimensional subspaces of the two-dimensional quotient \(P^\perp/P\). Double counting incidences shows that there are also \(M\) lines. Therefore
\[
N=2M,\qquad m_F=M(q+1).
\]

There is no \(4\)-cycle, since two distinct points determine at most one line.

There is also no \(6\)-cycle. Such a cycle would give three distinct points joined pairwise by three distinct isotropic lines. The three points cannot lie in one two-dimensional subspace, because then all three lines would coincide. Their representatives therefore span a three-dimensional totally isotropic subspace. This is impossible: if \(W\) is totally isotropic, then \(W\subseteq W^\perp\), so nondegeneracy implies
\[
\dim W\le2.
\]
Thus \(F_q\) has girth at least \(8\).

Choose the smallest power of two satisfying
\[
q\ge(2D)^{1/3}.
\]
Then \(M\ge q^3\ge2D\), so the transfer lemma gives
\[
\overline d(H)
\ge d\cdot\frac{q+1}{2M}\cdot\frac12
=\frac d{4(q^2+1)}.
\]
Here \(q\ge2\) and \(q<2(2D)^{1/3}\), whence
\[
q^2+1\le\frac54q^2
<5(2D)^{2/3}
<8D^{2/3}.
\]
Consequently,
\[
\overline d(H)\ge\frac d{32D^{2/3}},
\]
proving Theorem 2(2).

### 2.4. Arbitrary girth: a probabilistic template

Fix \(g\ge5\), and put
\[
r=\left\lfloor\frac{g-1}{2}\right\rfloor,\qquad s=2r-1.
\]
Thus \(r\ge2\) and \(2r+2\ge g\).

For any positive integer \(t\), start with \(K_{t,t}\) and retain each edge independently with probability
\[
p=\frac12t^{-(1-1/s)}.
\]
The expected number of retained edges is
\[
\frac12t^{1+1/s}.
\]

For \(2\le j\le r\), the expected number of cycles of length \(2j\) is at most
\[
\frac{t^{2j}p^{2j}}{2j}
\le 4^{-j}t^{2j/s}
\le4^{-j}t^{1+1/s}.
\]
Therefore the expected total number of cycles of lengths \(4,6,\ldots,2r\) is at most
\[
t^{1+1/s}\sum_{j=2}^{\infty}4^{-j}
=\frac1{12}t^{1+1/s}.
\]

There is a realization for which the number of edges minus the number of these short cycles is at least
\[
\left(\frac12-\frac1{12}\right)t^{1+1/s}
\ge\frac38t^{1+1/s}.
\]
Delete at most one edge for each short cycle. This produces a graph \(F\) on \(2t\) vertices with
\[
\operatorname{girth}(F)\ge2r+2\ge g,
\qquad
m_F\ge\frac38t^{1+1/s}.
\tag{2}
\]

Now take
\[
t=\lceil2D\rceil.
\]
Since \(D\ge1\),
\[
2D\le t\le3D.
\]
The transfer lemma and (2) yield
\[
\begin{aligned}
\overline d(H)
&\ge
d\,\frac{m_F}{2t^2}
\left(1-\frac{D-1}{t}\right)\\
&\ge\frac{3d}{32t^{1-1/s}}\\
&\ge\frac d{32D^{1-1/s}}.
\end{aligned}
\]
The last step uses \(3^{1-1/s}\le3\). This proves Theorem 2(3).

## 3. Passing from chromatic number to the partial result

Let
\[
R=\chi(G),
\]
and take a vertex-critical subgraph \(J\subseteq G\) with \(\chi(J)=R\). Every vertex of \(J\) has degree at least \(R-1\): otherwise an \((R-1)\)-coloring of \(J-v\) would extend to \(v\). Hence
\[
\overline d(J)\ge R-1.
\]

Under the hypothesis
\[
\Delta(G)\le A(R-1),
\]
we also have
\[
D(J)\le\Delta(J)\le A(R-1).
\]

The three conclusions of Theorem 2 therefore give, respectively,
\[
\overline d(H)\ge\frac{\sqrt{R-1}}{12\sqrt A},
\]
\[
\overline d(H)\ge\frac{(R-1)^{1/3}}{32A^{2/3}},
\]
and
\[
\overline d(H)\ge
\frac{(R-1)^{1/s}}{32A^{1-1/s}}.
\]
These are at least \(k\) at the thresholds asserted in Theorem 1.

In fact, the same thresholds work whenever an \(R\)-critical subgraph \(J\) satisfies merely
\[
D(J)\le A\,\overline d(J),
\tag{3}
\]
equivalently,
\[
\frac1{|V(J)|}\sum_{v\in V(J)}d_J(v)^2
\le A\,\overline d(J)^2.
\]
Thus bounded normalized degree second moment suffices.

### Why the quadratic and cubic orders are necessary

A graph of average degree at least \(k\) contains a nonempty subgraph of minimum degree at least
\[
\delta=\lceil k/2\rceil.
\]
Indeed, repeatedly deleting vertices of degree less than \(k/2\) cannot delete every vertex: the sum of their degrees at deletion would then be less than \(k|V|/2\), contradicting the initial edge count.

If this subgraph has girth at least \(2r+1\), a breadth-first search to depth \(r\) gives
\[
|V|\ge
1+\delta\sum_{i=0}^{r-1}(\delta-1)^i.
\tag{4}
\]
Collisions among the vertices counted in this search would create a cycle of length at most \(2r\).

For fixed \(r\), (4) is \(\Omega(k^r)\). A complete graph with fewer vertices than this bound cannot contain the target subgraph, and complete graphs satisfy
\[
\Delta(G)=\chi(G)-1.
\]
Taking \(r=2\) or \(r=3\) proves the claimed quadratic and cubic lower orders.

## 4. Exact elementary cases of the original conjecture

Let \(C(k,g)\) denote the least **integer** threshold, when one exists. The following cases can be determined exactly:
\[
C(k,3)=k+1,\qquad C(k,4)=2k,
\]
and
\[
C(1,g)=2,\qquad C(2,g)=g.
\]

Here are the arguments.

- **\(g=3\).** A graph of chromatic number at least \(k+1\) has a critical subgraph of minimum degree at least \(k\). The lower bound is \(K_k\).

- **\(g=4\).** Start with a critical subgraph of minimum degree at least \(2k-1\). In a maximum cut, every vertex has at least half its incident edges crossing the cut, hence at least \(k\) crossing edges. The resulting bipartite graph has average degree at least \(k\).

  Conversely, every triangle-free graph on \(n\le2k-1\) vertices has at most \(n^2/4\) edges, so its average degree is less than \(k\). Thus \(K_{2k-1}\) is a lower-bound example. For this average-degree formulation, no fractional-chromatic theorem is needed.

- **\(k=1\).** A single edge suffices, and chromatic number \(2\) is necessary and sufficient.

- **\(k=2\).** If \(\chi(G)\ge g\), take a critical subgraph of minimum degree at least \(g-1\). Every neighbor of an endpoint of a longest path lies on that path; its last neighbor along the path produces a cycle of length at least \(g\). That cycle has average degree \(2\).

  Conversely, every subgraph of \(K_{g-1}\) with girth at least \(g\) is a forest, and thus has average degree less than \(2\).

## 5. The remaining gap

The proof does **not** establish (3), with a bound depending only on the desired parameters, from large chromatic number alone.

Criticality does not directly control the degree second moment. For example, an odd wheel with rim length \(\ell\) is \(4\)-vertex-critical, but
\[
D=\frac{\ell^2+9\ell}{4\ell}=\frac{\ell+9}{4},
\]
which is unbounded. Joining such a wheel with a fixed clique gives the same phenomenon at any prescribed chromatic number at least \(4\). These graphs are not counterexamples to the conjecture; they show only why the critical-subgraph step does not automatically supply the needed moment bound.

Thus the precise progress is:

- all elementary parameter regimes above are covered exactly;
- every girth is covered for controlled degree distributions;
- girths \(5\)–\(8\) have order-optimal thresholds in that setting.

Finding a suitable dense subgraph with controlled degree distribution—or bypassing that requirement entirely—is the unresolved step in this attack. No proof or counterexample for the unrestricted conjecture is obtained.