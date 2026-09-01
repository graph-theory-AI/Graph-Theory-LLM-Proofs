```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open in general, but it holds for minimum degree at most one, all complete multipartite graphs, balanced joins, and optimally with multiplicity two whenever the complement is a pseudoforest.",
  "would_publish": false,
  "caveats": "Only special classes are resolved; the fractional argument does not round to a single subgraph, and novelty of the special cases has not been literature-checked."
}
```

# Mathematical writeup

## 1. Statement and notation

All graphs are finite and simple. For a spanning subgraph \(H\), write

\[
N_k(H)=|\{v\in V(H):d_H(v)=k\}|,\qquad
m(H)=\max_{k\ge 0}N_k(H).
\]

The conjecture asks whether every \(n\)-vertex graph \(G\) of minimum degree \(\delta\) has a spanning subgraph \(H\) such that

\[
m(H)\le \frac{n}{\delta+1}+2.
\tag{1}
\]

I do not prove this for arbitrary \(G\). I prove the following exact special cases.

1. The conjecture holds when \(\delta\le 1\).
2. If \(G\) contains a spanning \(K_{a,b}\), then an explicit bound on \(m(H)\) follows. Consequently:
   - the conjecture holds whenever the components of \(\overline G\) can be split into two groups of total orders within a factor \(2\);
   - in particular, it holds if no component of \(\overline G\) has more than \(2n/3\) vertices;
   - it holds for every complete multipartite graph.
3. If \(\overline G\) is a pseudoforest, then for \(n\ge4\) there is a spanning \(H\subseteq G\) with
   \[
   m(H)=2,
   \]
   which is best possible. In particular, the conjecture holds in the full dense range
   \[
   \delta(G)\ge n-3.
   \]

I also record an exact fractional relaxation valid for every graph.

---

## 2. An exact fractional version

### Proposition 2.1

For every graph \(G\) of minimum degree \(\delta\), there is a probability distribution on its spanning subgraphs such that, for every \(k\ge0\),

\[
\mathbb E N_k(H)\le \frac{n}{\delta+1}.
\tag{2}
\]

### Proof

Choose independent random variables \(X_v\), uniformly distributed on \([0,1]\), and put

\[
uv\in E(H)\quad\Longleftrightarrow\quad X_u+X_v\ge1.
\]

Fix a vertex \(v\) of degree \(d=d_G(v)\). Conditional on \(X_v=x\), the edges from \(v\) to its neighbors occur independently with probability \(x\). Hence

\[
d_H(v)\mid X_v=x\sim \operatorname{Bin}(d,x).
\]

For \(0\le k\le d\),

\[
\begin{aligned}
\Pr(d_H(v)=k)
&=\int_0^1 \binom dk x^k(1-x)^{d-k}\,dx\\
&=\binom dk \frac{k!(d-k)!}{(d+1)!}
=\frac1{d+1}.
\end{aligned}
\]

Therefore

\[
\mathbb E N_k(H)
=\sum_{\substack{v\in V(G)\\ d_G(v)\ge k}}\frac1{d_G(v)+1}
\le \frac{n}{\delta+1}.
\]

This proves (2). ∎

Thus the convex hull of all degree-histogram vectors of spanning subgraphs intersects the box with coordinate cap \(n/(\delta+1)\). The unresolved issue is an integral rounding statement: an average of histograms need not itself be the histogram of one subgraph. The additive constant \(2\) in the conjecture is precisely of the scale one might hope for from such a rounding theorem, but no such general theorem is proved here.

---

## 3. Minimum degree zero or one

### Proposition 3.1

If \(G\) has no isolated vertices, then it has a spanning subgraph \(H\) with

\[
m(H)\le \left\lfloor\frac n2\right\rfloor+1.
\tag{3}
\]

Consequently, the conjecture holds when \(\delta=1\). It is trivial when \(\delta=0\).

### Proof

Order the edges of \(G\) arbitrarily as \(e_1,\dots,e_m\), and let \(S_t\) be the set of vertices incident with at least one of \(e_1,\dots,e_t\). Since \(G\) has no isolated vertices, \(S_m=V(G)\).

Put \(r=\lfloor n/2\rfloor\), and choose the least \(t\) for which \(|S_t|\ge r\). Adding one edge introduces at most two new incident vertices, so

\[
r\le |S_t|\le r+1.
\]

Let \(H\) have edge set \(\{e_1,\dots,e_t\}\). Its nonisolated vertex set is exactly \(S_t\). Hence every positive-degree class has size at most \(|S_t|\le r+1\), while

\[
N_0(H)=n-|S_t|\le r+1.
\]

This proves (3). For \(\delta=1\),

\[
\left\lfloor\frac n2\right\rfloor+1
\le \frac n2+2.
\]

If \(\delta=0\), the empty spanning subgraph has \(m(H)=n\le n+2\). ∎

---

## 4. A spanning-biclique construction

### Lemma 4.1

Suppose \(G\) contains a spanning complete bipartite graph \(K_{a,b}\), where \(1\le a\le b\). Then \(G\) has a spanning subgraph \(H\) satisfying

\[
m(H)\le \left\lceil\frac{b}{a+1}\right\rceil+1.
\tag{4}
\]

### Proof

Let the bipartition be

\[
A=\{x_1,\dots,x_a\},\qquad |B|=b,
\]

and put

\[
q=\left\lceil\frac{b}{a+1}\right\rceil.
\]

Choose nonnegative integers \(c_0,\dots,c_a\) such that

\[
\sum_{j=0}^a c_j=b,\qquad c_j\le q,
\]

and

\[
c_j\ge1\quad\text{for }1\le j\le a-1.
\tag{5}
\]

Such a choice exists: first put one unit in each of \(c_1,\dots,c_{a-1}\), and distribute the remaining units among the total capacity \(q(a+1)\ge b\).

Partition \(B\) into sets \(B_0,\dots,B_a\), where \(|B_j|=c_j\). For every \(y\in B_j\), let

\[
N_H(y)=\{x_1,\dots,x_j\}.
\]

Only edges of the spanning \(K_{a,b}\) are used. Every vertex of \(B_j\) has degree \(j\). On the other side,

\[
d_H(x_i)=\sum_{j=i}^a c_j.
\]

For \(1\le i<a\),

\[
d_H(x_i)-d_H(x_{i+1})=c_i>0
\]

by (5). Thus the degrees of the \(a\) vertices in \(A\) are pairwise distinct.

For any integer \(k\), at most \(q\) vertices of \(B\) have degree \(k\), and at most one vertex of \(A\) has degree \(k\). Therefore \(N_k(H)\le q+1\), proving (4). ∎

### Corollary 4.2: balanced joins

If \(G\) contains a spanning \(K_{a,b}\) with

\[
a\le b\le2a,
\]

then \(G\) has a spanning subgraph with \(m(H)\le3\), and hence satisfies the conjecture.

Indeed,

\[
\frac{b}{a+1}<2,
\]

so Lemma 4.1 gives \(m(H)\le3\). On the other hand, for every simple \(n\)-vertex graph,

\[
\frac{n}{\delta+1}+2\ge3.
\]

### Corollary 4.3: disconnected complements with no giant component

Suppose every component of \(\overline G\) has at most \(2n/3\) vertices. Then \(G\) satisfies the conjecture, in fact with \(m(H)\le3\).

To see this, partition the components of \(\overline G\) into two collections whose total orders \(a,b\) both lie between \(n/3\) and \(2n/3\). Such a partition exists:

- if some component has order between \(n/3\) and \(2n/3\), take it as one side;
- otherwise all components have order less than \(n/3\), and greedily combine components until their total first reaches \(n/3\).

There are no complement edges between the two resulting sides, so all cross-edges are present in \(G\). Thus \(G\) contains a spanning \(K_{a,b}\) with \(b\le2a\).

### Corollary 4.4: complete multipartite graphs

Every complete multipartite graph satisfies the conjecture.

### Proof

Let the largest part have order \(L\). Then

\[
\delta=n-L.
\]

If \(L\le2n/3\), Corollary 4.3 applies because the components of the complement are precisely the partite classes.

Suppose \(L>2n/3\), and set \(a=n-L=\delta\). If \(a=0\), the graph is edgeless and the assertion is trivial. Otherwise, the largest part and the union of all remaining parts give a spanning \(K_{a,L}\). Lemma 4.1 gives

\[
\begin{aligned}
m(H)
&\le \left\lceil\frac{L}{a+1}\right\rceil+1\\
&\le \frac{L}{a+1}+2\\
&\le \frac{n}{a+1}+2
=\frac{n}{\delta+1}+2.
\end{aligned}
\]

∎

---

## 5. Complements that are pseudoforests

A pseudoforest is a graph in which every connected component contains at most one cycle.

### Theorem 5.1

Let \(G\) be an \(n\)-vertex graph with \(n\ge4\). If \(\overline G\) is a pseudoforest, then \(G\) has a spanning subgraph \(H\) with

\[
m(H)=2.
\tag{6}
\]

This is optimal for every graph on at least two vertices.

The proof is a graph-packing argument.

### 5.1 The fixed multiplicity-two graph

Write

\[
a=\left\lfloor\frac n2\right\rfloor,\qquad
b=\left\lceil\frac n2\right\rceil.
\]

Let

\[
A=\{x_1,\dots,x_a\},\qquad
B=\{y_0,\dots,y_{b-1}\}.
\]

Define \(J_n\) to be the bipartite graph with

\[
x_i y_j\in E(J_n)\quad\Longleftrightarrow\quad j\ge i.
\tag{7}
\]

Then

\[
d_{J_n}(y_j)=j,\qquad d_{J_n}(x_i)=b-i.
\]

If \(n=2a\), every degree in \(\{0,\dots,a-1\}\) occurs exactly twice. If \(n=2a+1\), degree \(0\) occurs once and every degree in \(\{1,\dots,a\}\) occurs twice. Therefore

\[
m(J_n)=2.
\tag{8}
\]

Let \(U_n=\overline{J_n}\). Both \(A\) and \(B\) induce cliques in \(U_n\), and its cross-edges are

\[
x_i y_j\in E(U_n)\quad\Longleftrightarrow\quad j<i.
\tag{9}
\]

### 5.2 Embedding balanced bipartite forests in the triangular cross-graph

Let \(T_a\) be the bipartite graph with parts

\[
\{x_1,\dots,x_a\},\qquad \{y_0,\dots,y_{a-1}\},
\]

and edges \(x_i y_j\) whenever \(j<i\).

#### Lemma 5.2

Every bipartite forest with two parts of order \(a\) embeds as a subgraph of \(T_a\).

#### Proof

Induct on \(a\). Let the two parts of the forest be \(P,Q\), both of order \(a\). Since the forest has at most \(2a-1\) edges,

\[
\sum_{p\in P}d(p)\le2a-1.
\]

Thus some \(p\in P\) has degree at most one. If \(p\) has one neighbor, call it \(q\); if \(p\) is isolated, choose any \(q\in Q\).

By induction, the forest obtained by deleting \(p,q\) embeds in \(T_{a-1}\). Shift that embedding by sending its \(x_i\) to \(x_{i+1}\) and its \(y_j\) to \(y_{j+1}\). Finally send

\[
p\mapsto x_1,\qquad q\mapsto y_0.
\]

The possible edge \(pq\) maps to \(x_1y_0\). The vertex \(p\) has no other neighbors, while \(y_0\) is adjacent in \(T_a\) to every \(x_i\). Hence all edges are represented. ∎

### 5.3 A suitable near-bisection of a pseudoforest

We first use the following observation.

#### Lemma 5.3

Let \(F\) be a pseudoforest and \(0\le t\le |V(F)|\). There is a set \(S\subseteq V(F)\) of order \(t\) such that the bipartite graph formed by the edges between \(S\) and \(V(F)\setminus S\) is a forest.

#### Proof

Order the components of \(F\). Take whole components until the next whole component would make the total exceed \(t\). If necessary, take a connected set of the required remaining order from that next component; a connected set of every prescribed order exists by growing a set along a spanning tree.

Only one component \(C\) is split, and its selected part \(W\) induces a connected subgraph. If the cut edges contained a cycle, that cycle would be the unique cycle of \(C\), and its vertices would alternate between \(W\) and \(C\setminus W\). In a unicyclic graph, trees off the unique cycle attach at only one cycle vertex, so two distinct selected cycle vertices could not be joined inside \(C[W]\). This contradicts the connectedness of \(C[W]\). ∎

We need a slightly stronger odd-order version.

#### Lemma 5.4

Let \(F\) be a pseudoforest on \(n\ge4\) vertices.

- If \(n=2a\), there is a partition \(V(F)=P\cup Q\) with \(|P|=|Q|=a\) such that the crossing graph \(F[P,Q]\) is a forest.
- If \(n=2a+1\ge5\), there is a partition with \(|P|=a\), \(|Q|=a+1\), such that \(F[P,Q]\) is a forest and some \(z\in Q\) has no neighbor in \(P\).

#### Proof

The even case is Lemma 5.3 with \(t=a\).

Now let \(n=2a+1\ge5\).

If \(F\) is disconnected, choose a smallest component \(D\). Then \(|D|\le a\). Apply Lemma 5.3 to \(F-D\) to choose \(P\) of order \(a\); let \(Q=V(F)\setminus P\). The crossing graph is a forest, and every vertex of \(D\subseteq Q\) has no neighbor in \(P\).

Suppose \(F\) is connected.

- If \(F\) is a tree, choose a leaf \(z\) with neighbor \(w\), put \(z,w\in Q\), and complete the partition arbitrarily. Then \(z\) has no crossing neighbor, and every subgraph of a tree is a forest.
- Suppose \(F\) is unicyclic but is not itself a cycle. Choose a leaf \(z\) with neighbor \(w\), and put \(z,w\in Q\).
  - If the unique cycle is odd, it cannot be contained in the bipartite crossing graph, so the crossing graph is a forest.
  - If the unique cycle is even, choose an edge \(pq\) of that cycle with \(p,q\ne w\), put \(p,q\in P\), and complete \(P\) to order \(a\) while keeping \(z,w\in Q\). Then the edge \(pq\) is not a crossing edge, so the unique cycle is broken.
- Finally, if \(F=C_n\), then \(n\) is odd. Put three consecutive cycle vertices in \(Q\), and let \(z\) be the middle one. Complete \(Q\) to order \(a+1\). Both neighbors of \(z\) lie in \(Q\), and the odd cycle cannot lie in the crossing graph.

This proves the assertion. ∎

### 5.4 Packing the pseudoforest

Let \(F\) be any pseudoforest on \(n\ge4\) vertices.

If \(n=2a\), use Lemma 5.4 to partition \(F\) into equal parts \(P,Q\) whose crossing graph is a forest. By Lemma 5.2, embed that crossing forest in the cross-graph (9) of \(U_n\). All edges of \(F\) internal to \(P\) or \(Q\) are automatically represented because both corresponding sides of \(U_n\) are cliques. Thus

\[
F\subseteq U_n.
\tag{10}
\]

If \(n=2a+1\), use the odd partition from Lemma 5.4. Map the crossing-isolated vertex \(z\in Q\) to \(y_a\), which has no cross-neighbors in \(U_n\). After deleting \(z\), the two parts have order \(a\), and their crossing forest embeds by Lemma 5.2. Again all internal edges are represented by the two cliques. Thus (10) also holds in the odd case.

Now take \(F=\overline G\). After relabeling, (10) says

\[
E(\overline G)\subseteq E(U_n)=E(\overline{J_n}).
\]

Consequently,

\[
E(J_n)\cap E(\overline G)=\varnothing,
\]

so the relabeled copy of \(J_n\) is a spanning subgraph of \(G\). By (8), it has \(m(J_n)=2\). This proves Theorem 5.1.

Finally, \(2\) is the smallest possible value for any simple graph on \(n\ge2\) vertices. If all vertex degrees were distinct, they would have to be exactly \(0,1,\dots,n-1\), but a graph cannot simultaneously have an isolated vertex and a vertex of degree \(n-1\). ∎

### Corollary 5.5: the dense range

If

\[
\delta(G)\ge n-3,
\]

then

\[
\Delta(\overline G)=n-1-\delta(G)\le2.
\]

Every graph of maximum degree at most two is a pseudoforest. Hence for \(n\ge4\), Theorem 5.1 gives a spanning \(H\subseteq G\) with \(m(H)=2\). This is stronger than (1), whose right-hand side is always at least \(3\).

For \(n\le3\), the conjecture is immediate from \(m(H)\le n\le3\).

---

## 6. What remains open

The arguments above do not cover a general graph of minimum degree \(\delta\ge2\). In particular:

- the threshold construction proves only a fractional/expected degree-histogram bound;
- the spanning-biclique construction requires a strong join structure;
- the multiplicity-two construction relies on packing against a pseudoforest complement.

An arbitrary connected complement with several cycles, or an arbitrary sparse graph of minimum degree two or more, need not have any of these structures. No rounding argument is supplied that converts Proposition 2.1 into a single spanning subgraph with additive error \(2\). Thus the full conjecture remains unresolved here.