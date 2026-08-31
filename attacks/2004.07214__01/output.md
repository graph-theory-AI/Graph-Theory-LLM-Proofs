```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For induced H-freeness, the conjecture is equivalent under output-sensitive reductions to minimal-transversal enumeration for hypergraphs of fixed bounded VC dimension.",
  "would_publish": false,
  "caveats": "No output-polynomial algorithm for bounded-VC transversal enumeration is proved here; the argument assumes that H-free means induced-H-free."
}
```

# 1. Statement of the partial result

Throughout, \(H\)-free means **induced-\(H\)-free**.

For a graph \(G\), let

\[
\mathcal N(G)=\{N_G[v]:v\in V(G)\}
\]

be its closed-neighborhood hypergraph. Minimal dominating sets of \(G\) are exactly the minimal transversals of \(\mathcal N(G)\).

I prove two results.

### Theorem A
For every fixed co-bipartite graph \(H\), there is a constant \(d_H\) such that, for every induced-\(H\)-free incomparability graph \(G\),

\[
\operatorname{VCdim}(\mathcal N(G))\le d_H.
\]

The constant is effective, though very large.

### Theorem B
The following two algorithmic assertions are equivalent.

1. For every fixed co-bipartite \(H\), minimal dominating sets can be enumerated in output-polynomial time in induced-\(H\)-free incomparability graphs.
2. For every fixed \(d\), minimal transversals can be enumerated in output-polynomial time in hypergraphs of VC dimension at most \(d\).

Thus Conjecture 7.3 is, at the level of output-polynomial enumeration, exactly as difficult as bounded-VC-dimension hypergraph dualization. I do not prove the latter algorithmic assertion here.

---

# 2. Bounded neighborhood VC dimension

We first record a basic property of incomparability graphs.

## Lemma 2.1: traces on a chain are intervals

Let \(P\) be a poset, let \(G\) be its incomparability graph, and let

\[
c_1<c_2<\cdots<c_t
\]

be a chain of \(P\). For every \(v\in P\), the set

\[
N_G[v]\cap \{c_1,\ldots,c_t\}
\]

is an interval of this chain, allowing the empty interval and singletons.

### Proof

If \(v\notin\{c_1,\ldots,c_t\}\), it suffices to show that the elements of the chain incomparable with \(v\) form a convex set. Suppose \(i<j<k\) and \(v\) is incomparable with both \(c_i\) and \(c_k\). If \(c_j<v\), then \(c_i<c_j<v\), contradicting \(c_i\parallel v\). If \(v<c_j\), then \(v<c_j<c_k\), contradicting \(v\parallel c_k\). Hence \(v\parallel c_j\).

If \(v=c_i\), then \(v\) is comparable with every other member of the chain and

\[
N_G[v]\cap\{c_1,\ldots,c_t\}=\{c_i\}.
\]

So the trace is again an interval. ∎

## Corollary 2.2

A set shattered by \(\mathcal N(G)\) contains no three-element chain of \(P\).

### Proof

On a three-element chain \(c_1<c_2<c_3\), the trace \(\{c_1,c_3\}\) cannot occur by Lemma 2.1. Thus the chain is not shattered. Shattering is inherited by subsets. ∎

Consequently, every shattered set has height at most two. By partitioning it into its two rank levels, it is the union of two antichains. In particular:

## Corollary 2.3

If \(\mathcal N(G)\) shatters a set of size \(2n\), then it shatters an antichain of size \(n\).

---

## Lemma 2.4: a large shattered antichain forces any fixed co-bipartite graph

Let \(H\) be co-bipartite with a partition

\[
V(H)=X_H\mathbin{\dot\cup}Y_H
\]

into two nonempty cliques. Put

\[
p=|X_H|,\qquad q=|Y_H|,\qquad
k=p+\left\lceil\log_2 q\right\rceil.
\]

There is a constant \(n_H\) such that if \(\mathcal N(G)\) shatters an antichain of size \(n_H\) in a poset whose incomparability graph is \(G\), then \(G\) contains an induced copy of \(H\).

### Proof

Choose \(n=n_H\) sufficiently large that

\[
\frac{\binom{n}{\lfloor n/2\rfloor}}{2n+1}
   >
\sum_{i=0}^{k-1}\binom ni.
\tag{1}
\]

Such an \(n\) exists because the left-hand side grows exponentially in \(n\), while the right-hand side is polynomial in \(n\) for fixed \(k\).

Let \(A\) be a shattered antichain of size \(n\), and set \(r=\lfloor n/2\rfloor\). For every \(r\)-element subset \(R\subseteq A\), choose a vertex \(v_R\) such that

\[
N_G[v_R]\cap A=R.
\tag{2}
\]

Since \(A\) is an antichain, it is a clique in \(G\). Thus a vertex of \(A\) has trace \(A\) on \(A\). Because \(r<n\), every \(v_R\) lies outside \(A\), and (2) says precisely that \(v_R\) is incomparable with exactly the members of \(R\) among \(A\).

Let

\[
W=\{v_R:R\in\tbinom Ar\}.
\]

Consider a chain

\[
v_{R_1}<v_{R_2}<\cdots<v_{R_t}
\]

inside \(W\). For any fixed \(a\in A\), Lemma 2.1 shows that the indices \(i\) for which \(a\in R_i\) form an interval. Hence, as \(i\) increases, the indicator of membership of \(a\) changes at most twice. Across all \(n\) elements of \(A\), there are at most \(2n\) changes. Since the sets \(R_i\) are distinct, every passage from \(R_i\) to \(R_{i+1}\) changes at least one coordinate. Therefore

\[
t\le 2n+1.
\]

Thus the height of the poset induced by \(W\) is at most \(2n+1\). Partitioning \(W\) into at most \(2n+1\) antichains gives an antichain \(W'\subseteq W\) of size at least

\[
\frac{\binom nr}{2n+1}.
\]

Let

\[
\mathcal F=\{R\in\tbinom Ar:v_R\in W'\}.
\]

By (1) and the Sauer–Shelah bound, \(\mathcal F\) shatters some \(k\)-element set \(C\subseteq A\).

Write

\[
C=A_0\mathbin{\dot\cup} Z,\qquad |A_0|=p,\qquad
|Z|=\lceil\log_2q\rceil.
\]

Label \(A_0=\{a_1,\ldots,a_p\}\) according to the vertices of \(X_H\). For each \(y_j\in Y_H\), let

\[
B_j=\{a_i:a_iy_j\in E(H)\}\subseteq A_0.
\]

Choose \(q\) distinct subsets \(Z_1,\ldots,Z_q\subseteq Z\). This is possible by the choice of \(|Z|\). Since \(\mathcal F\) shatters \(C\), for every \(j\) there is \(R_j\in\mathcal F\) such that

\[
R_j\cap C=B_j\cup Z_j.
\]

The distinct codes \(Z_j\) ensure that the \(R_j\)'s, and hence the vertices \(v_{R_j}\), are distinct.

Now:

- \(A_0\) is an antichain in the poset, so it is a clique in \(G\);
- the vertices \(v_{R_1},\ldots,v_{R_q}\) belong to the antichain \(W'\), so they form a clique in \(G\);
- by construction,
  \[
  a_i v_{R_j}\in E(G)
  \quad\Longleftrightarrow\quad
  a_i\in R_j
  \quad\Longleftrightarrow\quad
  a_i y_j\in E(H).
  \]

Therefore the induced graph on

\[
A_0\cup\{v_{R_1},\ldots,v_{R_q}\}
\]

is isomorphic to \(H\). ∎

## Proof of Theorem A

Choose \(n_H\) as in Lemma 2.4. If \(\mathcal N(G)\) shattered \(2n_H\) vertices, Corollary 2.3 would give a shattered antichain of size \(n_H\), and Lemma 2.4 would produce an induced \(H\). Hence every induced-\(H\)-free incomparability graph satisfies

\[
\operatorname{VCdim}(\mathcal N(G))<2n_H.
\]

Thus one may take \(d_H=2n_H-1\). ∎

A useful immediate consequence is that, for every \(S\subseteq V(G)\), the number of distinct traces

\[
\{N_G[v]\cap S:v\in V(G)\}
\]

is \(O_H(|S|^{d_H})\).

---

# 3. From bounded-VC transversal enumeration to the conjecture

Assume that, for every fixed \(d\), minimal transversals of hypergraphs of VC dimension at most \(d\) can be enumerated in output-polynomial time.

Fix a co-bipartite \(H\), and let \(G\) be an induced-\(H\)-free incomparability graph. By Theorem A, \(\mathcal N(G)\) has VC dimension at most the fixed constant \(d_H\).

A set \(D\subseteq V(G)\) is dominating exactly when

\[
D\cap N_G[v]\ne\varnothing
\quad\text{for every }v\in V(G),
\]

that is, exactly when \(D\) is a transversal of \(\mathcal N(G)\). Inclusion-minimality is the same on both sides. Applying the assumed bounded-VC transversal algorithm to \(\mathcal N(G)\) therefore proves Conjecture 7.3.

This establishes one direction of Theorem B.

---

# 4. The converse output-sensitive reduction

We now show that Conjecture 7.3 would solve minimal-transversal enumeration for every fixed VC-dimension bound.

## 4.1 A dual VC-dimension bound

For a set system \(\mathcal F\subseteq 2^X\), its dual is the set system on ground set \(\mathcal F\) whose member corresponding to \(x\in X\) is

\[
F_x^*=\{F\in\mathcal F:x\in F\}.
\]

## Lemma 4.1

If \(\operatorname{VCdim}(\mathcal F)\le d\), then

\[
\operatorname{VCdim}(\mathcal F^*)<2^{d+1}.
\]

### Proof

Suppose that the dual shatters \(2^{d+1}\) members of \(\mathcal F\). Index those members as

\[
F_J,\qquad J\subseteq[d+1].
\]

For every \(i\in[d+1]\), dual shattering gives a point \(x_i\in X\) whose incidence pattern on these members is

\[
x_i\in F_J\quad\Longleftrightarrow\quad i\in J.
\]

The points \(x_1,\ldots,x_{d+1}\) are distinct, and

\[
F_J\cap\{x_1,\ldots,x_{d+1}\}
   =\{x_i:i\in J\}.
\]

Thus \(\mathcal F\) shatters \(d+1\) points, a contradiction. ∎

---

## 4.2 The graph construction

Fix \(d\), and let \(\mathcal K=(X,\mathcal E)\) be a hypergraph with VC dimension at most \(d\). Empty-edge and empty-family cases can be handled separately, and duplicate edges may be removed.

Construct a graph \(G_{\mathcal K}\) as follows:

- \(C=X\cup\{z\}\) is a clique;
- \(R=\{r_E:E\in\mathcal E\}\) is a clique;
- for \(x\in X\) and \(E\in\mathcal E\),
  \[
  xr_E\in E(G_{\mathcal K})\quad\Longleftrightarrow\quad x\in E;
  \]
- \(z\) has no neighbors in \(R\).

This graph is co-bipartite, hence an incomparability graph. Explicitly, take \(C\) and \(R\) as antichains and put

\[
c<r_E\quad\Longleftrightarrow\quad cr_E\notin E(G_{\mathcal K}).
\]

This is a height-two poset and its incomparability graph is exactly \(G_{\mathcal K}\).

## Lemma 4.2: its minimal dominating sets

The minimal dominating sets contained in \(C\) are exactly the minimal transversals of \(\mathcal K\), viewed as subsets of \(X\). There are no minimal dominating sets contained wholly in \(R\), and every mixed minimal dominating set has exactly two vertices. Consequently,

\[
|\operatorname{MDS}(G_{\mathcal K})|
 \le |\operatorname{Tr}(\mathcal K)|+(|X|+1)|\mathcal E|.
\tag{3}
\]

### Proof

Let \(D\subseteq C\). Because \(C\) is a clique, every nonempty \(D\) dominates \(C\). It dominates \(r_E\) precisely when \(D\cap E\ne\varnothing\), since \(z\) has no neighbor in \(R\). Thus \(D\cap X\) must be a transversal.

The vertex \(z\) cannot belong to a minimal such \(D\): deleting \(z\) changes neither domination of \(R\) nor domination of \(C\). Hence the \(C\)-contained minimal dominating sets are exactly the minimal transversals contained in \(X\).

A set contained in \(R\) cannot dominate \(z\).

Finally, if a dominating set meets both \(C\) and \(R\), then any one vertex from \(C\) together with any one vertex from \(R\) already dominates all of \(C\cup R\), because both parts are cliques. A mixed minimal dominating set therefore has one vertex in each part. There are at most \((|X|+1)|\mathcal E|\) such pairs. ∎

Thus an output-polynomial enumeration of all minimal dominating sets of \(G_{\mathcal K}\), followed by retaining only outputs contained in \(X\), would enumerate the minimal transversals of \(\mathcal K\). Estimate (3) ensures that the unwanted outputs cause only polynomial overhead.

It remains to find, for each fixed \(d\), one fixed co-bipartite graph excluded by every \(G_{\mathcal K}\).

---

## 4.3 A fixed forbidden graph

Set

\[
r=2^{d+1}.
\]

Define a connected bipartite graph \(U_r\) with bipartition

\[
L=\{\ell_0,\ell_1,\ldots,\ell_r\},
\qquad
B=\{b_S:S\subseteq[r]\},
\]

where

\[
\ell_0b_S\in E(U_r)\quad\text{for all }S,
\]

and, for \(i\in[r]\),

\[
\ell_i b_S\in E(U_r)\quad\Longleftrightarrow\quad i\in S.
\]

Let

\[
H_d=\overline{U_r}.
\]

Since \(U_r\) is bipartite, \(H_d\) is co-bipartite and depends only on \(d\).

## Lemma 4.3

For every hypergraph \(\mathcal K\) of VC dimension at most \(d\), the graph \(G_{\mathcal K}\) is induced-\(H_d\)-free.

### Proof

The complement \(\overline{G_{\mathcal K}}\) is bipartite with sides \(C=X\cup\{z\}\) and \(R\). For \(E\in\mathcal E\), the neighborhood of \(r_E\) in \(C\) is

\[
Q_E=\{z\}\cup(X\setminus E).
\]

Let

\[
\mathcal Q=\{Q_E:E\in\mathcal E\}.
\]

Complementing every set on \(X\) preserves VC dimension, and adjoining the common element \(z\) to every set does not increase VC dimension. Therefore

\[
\operatorname{VCdim}(\mathcal Q)\le d.
\tag{4}
\]

By Lemma 4.1,

\[
\operatorname{VCdim}(\mathcal Q^*)<r.
\tag{5}
\]

Suppose \(G_{\mathcal K}\) contained an induced \(H_d\). Then \(\overline{G_{\mathcal K}}\) would contain an induced \(U_r\). The graph \(U_r\) is connected, so its bipartition must align with the bipartition \(C,R\), up to swapping.

If \(L\) maps into \(C\) and \(B\) maps into \(R\), the vertices corresponding to \(b_S\), \(S\subseteq[r]\), give members of \(\mathcal Q\) whose traces on the selected vertices corresponding to \(\ell_1,\ldots,\ell_r\) are all \(2^r\) subsets. Thus \(\mathcal Q\) shatters \(r\) points, contradicting (4).

If \(L\) maps into \(R\) and \(B\) maps into \(C\), the same incidence matrix shows that the dual family \(\mathcal Q^*\) shatters the \(r\) selected members corresponding to \(\ell_1,\ldots,\ell_r\), contradicting (5).

Hence no induced \(U_r\) occurs in \(\overline{G_{\mathcal K}}\), and no induced \(H_d\) occurs in \(G_{\mathcal K}\). ∎

Assuming Conjecture 7.3 for the single graph \(H_d\), we can therefore enumerate all minimal dominating sets of \(G_{\mathcal K}\) in output-polynomial time. Lemma 4.2 then gives an output-polynomial enumeration of the minimal transversals of \(\mathcal K\).

This proves the converse implication and completes Theorem B.

---

# 5. What remains open

The argument does **not** prove an output-polynomial algorithm for minimal transversals of bounded-VC hypergraphs. Bounded VC dimension does not bound either the number or the cardinality of minimal transversals: for example, the hypergraph consisting of disjoint two-element edges has VC dimension one and \(2^n\) minimal transversals.

Thus the missing step is genuinely output-sensitive enumeration, not a polynomial bound on the output. I have not verified a published theorem resolving bounded-VC transversal enumeration in the required generality, and no such theorem is proved above.

The result nevertheless gives a fairly sharp reformulation:

- forbidden co-bipartite induced subgraphs force bounded closed-neighborhood VC dimension in incomparability graphs;
- bounded-VC hypergraph dualization reduces back to the conjecture using graphs that are themselves co-bipartite incomparability graphs;
- the reduction creates only polynomially many unwanted minimal dominating sets.

If “\(H\)-free” were intended to mean ordinary subgraph-free rather than induced-\(H\)-free, Theorem A would still give a necessary structural consequence, but the converse reduction would no longer establish the stated equivalence.