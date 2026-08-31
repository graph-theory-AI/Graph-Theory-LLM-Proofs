```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds with an explicit polynomial in t for every fixed μ on every fixed-chromatic-number class, in particular for all bipartite graphs.",
  "would_publish": false,
  "caveats": "The passage from bounded chromatic number to arbitrary graphs remains open; the argument deliberately bounds treewidth, which is too crude for dense graphs."
}
```

## 1. Statement of the partial result

I interpret \(K_{t,t}\)-free as excluding an induced \(K_{t,t}\), in accordance with the source abstract. All arguments below also apply under ordinary \(K_{t,t}\)-exclusion.

For \(X\subseteq V(G)\), let
\[
\mu_G(X)=\max\{|M|:M\text{ is an induced matching of }G
\text{ and every edge of }M\text{ meets }X\}.
\]
Thus
\[
\operatorname{tree\text{-}\mu}(G)
 =\min_{\mathcal D}\max_{B\in\mathcal D}\mu_G(B).
\]

The following special case of the question can be proved.

### Theorem
For every pair of fixed positive integers \(\mu,r\), there is a polynomial
\[
P_{\mu,r}(t)
\]
such that every \(r\)-colorable induced-\(K_{t,t}\)-free graph \(G\) satisfying
\[
\operatorname{tree\text{-}\mu}(G)\leq \mu
\]
also satisfies
\[
\operatorname{tree\text{-}\alpha}(G)\leq P_{\mu,r}(t).
\]

In particular, the question has an affirmative answer for bipartite graphs.

A crude explicit degree is available. One may take
\[
P_{\mu,r}(t)=C_\mu r(r-1)t^{e_\mu},
\qquad
e_\mu=(\mu+1)^{\,2\lceil\log_2(\mu+1)\rceil},
\]
where \(C_\mu\) depends only on \(\mu\). No effort is made to optimize this exponent.

The proof has three ingredients.

---

## 2. A polynomial matching-versus-biclique lemma

For a bipartite graph \(H=(A,B;E)\), write \(\operatorname{im}(H)\) for its induced matching number.

### Lemma 2.1: homogeneous rectangles from bounded VC dimension
For every \(d\) there is \(c_d>0\) such that the following holds. Let \(H=(A,B;E)\) be bipartite with
\[
|A|,|B|\geq n,
\]
and suppose that the set system
\[
\{N_H(a):a\in A\}
\]
has VC dimension at most \(d\). Then there are \(A'\subseteq A\) and \(B'\subseteq B\), each of size at least
\[
c_d n^{1/(d+1)},
\]
such that \(A'\) is either complete or anticomplete to \(B'\).

#### Proof
Choose \(B_0\subseteq B\) of size
\[
s=\left\lfloor n^{1/(d+1)}\right\rfloor.
\]
By Sauer–Shelah,
\[
\left|\{N_H(a)\cap B_0:a\in A\}\right|
 \leq \sum_{i=0}^d\binom{s}{i}
 \leq C_d s^d
\]
for a constant \(C_d\).

Consequently, some \(A_0\subseteq A\) of size at least
\[
\frac{n}{C_ds^d}\geq c'_d n^{1/(d+1)}
\]
has a common trace on \(B_0\). Thus every vertex of \(B_0\) is either adjacent to all of \(A_0\) or to none of \(A_0\). One of these two classes in \(B_0\) has size at least \(s/2\). Truncating the larger side if necessary proves the claim. \(\square\)

Two applications, once in each direction across a specified matching, give the following.

### Lemma 2.2: two-way homogeneous matching blocks
Fix \(d\). There is \(c'_d>0\) such that, if a bipartite graph \(H=(A,B)\) has a specified matching
\[
M=\{a_i b_i:i\in I\cup J\},
\qquad |I|=|J|=n,
\]
and the \(A\)-neighborhood set system has VC dimension at most \(d\), then there are
\[
I'\subseteq I,\qquad J'\subseteq J,
\]
with
\[
|I'|=|J'|\geq c'_d n^{1/(d+1)^2},
\]
such that each of the two bipartite pairs
\[
A_{I'}\times B_{J'}
\quad\text{and}\quad
A_{J'}\times B_{I'}
\]
is homogeneous.

#### Proof
Apply Lemma 2.1 to \(A_I,B_J\), and then apply it again to the reverse pair formed by the resulting subsets of \(A_J,B_I\). Taking subsets preserves the first homogeneous relation. \(\square\)

### Lemma 2.3: polynomial matching Ramsey lemma
For every fixed \(d,k\), there is a constant \(C_{d,k}\) such that the following holds.

Suppose \(H=(A,B)\) is bipartite, its \(A\)-neighborhood set system has VC dimension at most \(d\), and \(H\) contains a specified matching \(M\) of size at least
\[
C_{d,k}t^{E_{d,k}},
\qquad
E_{d,k}=\bigl((d+1)^2\bigr)^{\lceil\log_2 k\rceil}.
\]
Then either:

1. \(H\) contains \(K_{t,t}\), or
2. \(M\) contains an induced submatching of size \(k\).

#### Proof
We induct on \(k\). The assertion for \(k=1\) is immediate.

For \(k\geq2\), split the index set of \(M\) into two almost equal sets \(I,J\). By Lemma 2.2, after passing to subsets \(I'\subseteq I\), \(J'\subseteq J\) of size
\[
\Omega_d\bigl(|M|^{1/(d+1)^2}\bigr),
\]
both directional blocks are homogeneous.

If either block is complete and \(|I'|=|J'|\geq t\), it gives \(K_{t,t}\). Otherwise both directional blocks are anticomplete. Put
\[
k_1=\lfloor k/2\rfloor,\qquad k_2=\lceil k/2\rceil.
\]
Provided \(I'\) and \(J'\) are large enough, induction gives an induced \(k_1\)-submatching on \(I'\) and an induced \(k_2\)-submatching on \(J'\), unless a \(K_{t,t}\) already occurs. Since both cross-blocks are anticomplete, the union of these two submatchings is an induced \(k\)-submatching.

The recurrence is
\[
R_{d,k}(t)
 \leq C_d
 \max\{t,R_{d,k_1}(t),R_{d,k_2}(t)\}^{(d+1)^2}.
\]
A balanced recursion has depth \(\lceil\log_2 k\rceil\), yielding the stated exponent. \(\square\)

The connection with induced matchings is immediate.

### Corollary 2.4
For every fixed \(\mu\), there is a polynomial
\[
Q_\mu(t)\leq C_\mu t^{e_\mu},
\qquad
e_\mu=(\mu+1)^{2\lceil\log_2(\mu+1)\rceil},
\]
such that every bipartite \(K_{t,t}\)-free graph \(H\) with
\[
\operatorname{im}(H)\leq\mu
\]
has matching number
\[
\nu(H)<Q_\mu(t).
\]

#### Proof
If the neighborhood system of a bipartite graph shatters \(b_1,\dots,b_s\), choose \(a_i\) whose trace on these vertices is \(\{b_i\}\). Then
\[
\{a_i b_i:1\leq i\leq s\}
\]
is an induced matching. Hence the VC dimension is at most \(\operatorname{im}(H)\leq\mu\).

Apply Lemma 2.3 with \(d=\mu\) and \(k=\mu+1\) to the endpoints of any matching of size \(Q_\mu(t)\). Both alternatives are forbidden. \(\square\)

This corollary is the main quantitative point: for fixed induced matching number, a bipartite graph with no \(K_{t,t}\) has matching number polynomial in \(t\).

---

## 3. From a tree-\(\mu\) decomposition to controlled cuts

Let \((T,\{B_x\}_{x\in V(T)})\) be a tree decomposition witnessing
\[
\mu_G(B_x)\leq\mu
\qquad\text{for every }x\in V(T).
\]

Choose for each vertex \(v\in V(G)\) a home node \(h(v)\in T\) with \(v\in B_{h(v)}\). By attaching one leaf for each graph vertex and replacing high-degree nodes by subcubic trees, one obtains a subcubic tree \(S\) whose leaves are in bijection with \(V(G)\).

The refinement can be chosen with the following property.

### Lemma 3.1
For every edge \(e\in E(S)\), let
\[
(U_e,W_e)
\]
be the corresponding partition of \(V(G)\). There is an original bag \(B_x\) such that every edge of \(G\) between \(U_e\) and \(W_e\) has at least one endpoint in \(B_x\).

#### Proof
For a cut corresponding to an original edge \(xy\in E(T)\), suppose \(uv\in E(G)\) has homes on opposite sides. The bag-subtrees of \(u\) and \(v\) intersect. If neither contains the tree edge \(xy\), those subtrees lie on opposite sides and cannot intersect. Thus at least one of \(u,v\) lies in the adhesion \(B_x\cap B_y\).

For a cut introduced while replacing a node \(x\) by a subcubic tree, the cut separates groups of components of \(T-x\), together with vertices homed at \(x\). If neither endpoint of a crossing graph edge lies in \(B_x\), the two corresponding bag-subtrees are confined to distinct components of \(T-x\), again contradicting their intersection. \(\square\)

Consequently, every induced matching of \(G\) consisting of edges crossing a cut of \(S\) has size at most \(\mu\).

A useful conclusion, valid without any coloring assumption, is:

### Corollary 3.2: polynomial independent-cut matching bound
For every cut \((U,W)\) of \(S\), and all independent sets
\[
X\subseteq U,\qquad Y\subseteq W,
\]
the bipartite graph \(G[X,Y]\) has matching number less than \(Q_\mu(t)\).

#### Proof
Every induced matching of \(G[X,Y]\) is an induced matching of \(G\), because \(X\) and \(Y\) are independent and all possible edges between them occur in \(G[X,Y]\). It consists of crossing edges and is covered by the bag supplied by Lemma 3.1. Thus
\[
\operatorname{im}(G[X,Y])\leq\mu.
\]
A \(K_{t,t}\) in \(G[X,Y]\) would be an induced \(K_{t,t}\) in \(G\). Apply Corollary 2.4. \(\square\)

This is the part of the argument that remains applicable to arbitrary graphs.

---

## 4. Fixed chromatic number

Assume now that \(G\) has a proper coloring
\[
V(G)=V_1\cup\cdots\cup V_r.
\]

Fix a cut \((U,W)\) of \(S\). For every ordered pair \(i\neq j\), consider
\[
H_{ij}=G[U\cap V_i,\;W\cap V_j].
\]
Both sides are independent. Therefore Corollary 3.2 gives
\[
\nu(H_{ij})<Q_\mu(t).
\]

Every matching in the full crossing graph splits into at most \(r(r-1)\) matchings according to the ordered color pair of its endpoints. Hence every crossing graph has matching number at most
\[
K=r(r-1)Q_\mu(t).
\]

It remains to turn this into a treewidth bound.

### Lemma 4.1
Let \(S\) be a subcubic tree whose leaves are \(V(G)\). If the crossing graph of every edge-cut of \(S\) has matching number at most \(K\), then
\[
\operatorname{tw}(G)+1\leq 3K.
\]

#### Proof
For each tree edge \(e\), the crossing graph is bipartite. By König's theorem, it has a vertex cover \(C_e\) with
\[
|C_e|\leq K.
\]

We use bramble duality. Suppose \(\mathcal B\) is a bramble of order greater than \(3K\). For a tree edge \(e\), some member of \(\mathcal B\) avoids \(C_e\). Every connected set avoiding \(C_e\) lies wholly on one side of the cut, because \(C_e\) covers all crossing edges. Moreover, all bramble members avoiding \(C_e\) lie on the same side: members on opposite sides would be disjoint and anticomplete. Orient \(e\) toward that side.

The oriented tree has a sink \(x\). If \(x\) is internal, let \(e_1,e_2,e_3\) be its incident edges, omitting nonexistent ones when the degree is smaller. Since
\[
|C_{e_1}\cup C_{e_2}\cup C_{e_3}|\leq3K,
\]
there is \(B\in\mathcal B\) avoiding their union. For each \(i\), the set \(B\) must lie on the side of \(e_i\) containing \(x\). The intersection of these sides is empty, because the outward branches at \(x\) partition the leaves. This is a contradiction.

If the sink is a leaf corresponding to \(v\), then \(C_e\cup\{v\}\) hits the bramble and has size at most \(K+1\leq3K\), again a contradiction.

Thus every bramble has order at most \(3K\). By the treewidth–bramble duality,
\[
\operatorname{tw}(G)+1\leq3K.
\]
\(\square\)

Combining the estimates,
\[
\operatorname{tree\text{-}\alpha}(G)
 \leq \operatorname{tw}(G)+1
 \leq 3r(r-1)Q_\mu(t)
 \leq C_\mu r(r-1)t^{e_\mu}.
\]

This proves the stated theorem. For bipartite graphs, \(r=2\), so
\[
\operatorname{tree\text{-}\alpha}(G)
 \leq 6Q_\mu(t)
 =O_\mu\!\left(t^{e_\mu}\right).
\]

---

## 5. What remains open

The bounded-color hypothesis enters only when a crossing matching is partitioned into \(r(r-1)\) matchings between pairs of independent sets. Corollary 3.2 gives polynomial control of every such independent-to-independent matching, but an arbitrary graph may require arbitrarily many color classes.

This is not merely a cosmetic defect. In the induced-\(K_{t,t}\)-free convention, a complete graph has
\[
\operatorname{tree\text{-}\mu}=1,\qquad
\operatorname{tree\text{-}\alpha}=1,
\]
while balanced cuts can have arbitrarily large ordinary matching number. Thus any argument passing through ordinary treewidth necessarily overcharges dense sets that have independence number \(1\).

A natural missing cut statement would be to control
\[
\min\{\alpha_G(C):C\text{ meets every edge across a prescribed cut}\}
\]
by a polynomial in \(t\) for fixed \(\mu\), and then synthesize such low-independence cut covers into one tree decomposition. The matrix lemma above proves the required matching bound when the relevant endpoint sets are independent, but I do not have a rigorous method for handling arbitrary dense endpoint sets or for performing the required global synthesis.

Accordingly, the general question remains unresolved here.