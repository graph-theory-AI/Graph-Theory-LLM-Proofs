```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general problem remains open, but arbitrary hypergraph transversal–matching gaps already occur on split graphs, the degeneracy hierarchy has a sharp threshold at 2, and recognition is undecidable for unrestricted effectively presented classes.",
  "would_publish": false,
  "caveats": "The positive 2-degenerate direction is imported from the supplied source; the undecidability result uses an explicit Turing-machine presentation model, and no full structural characterization is obtained."
}
```

# 1. Statement and scope

For a nonempty finite graph \(G\), let

\[
R(G)=\frac{\gamma(G)}{\rho(G)},
\qquad
R(\mathcal G)=\sup_{G\in\mathcal G,\;V(G)\neq\varnothing}R(G).
\]

The question asks for a structural characterization of the classes \(\mathcal G\) satisfying \(R(\mathcal G)<\infty\).

Without assumptions such as hereditary, monotone, minor-closed, or effective finite description, “characterize graph classes” is under-specified: arbitrary classes can encode arbitrary information. The results below make three precise points.

1. The problem contains the general hypergraph transversal-versus-matching problem, already on split graphs.
2. Combining an explicit construction with the reported theorem for 2-degenerate graphs gives a sharp degeneracy threshold.
3. In a natural algorithmic model, recognizing whether an arbitrary hereditary or monotone class has bounded ratio is undecidable.

These do not constitute the requested full structural characterization.

# 2. Hypergraph formulation and exact realization by split graphs

For a hypergraph \(\mathcal H\), write \(\tau(\mathcal H)\) for its transversal number and \(\nu(\mathcal H)\) for its matching number.

For a graph \(G\), let

\[
\mathcal N(G)=\bigl(V(G),\{N_G[v]:v\in V(G)\}\bigr)
\]

be its closed-neighborhood hypergraph. Directly from the definitions,

\[
\gamma(G)=\tau(\mathcal N(G)),
\qquad
\rho(G)=\nu(\mathcal N(G)).
\]

Thus the graph problem is an integral packing-covering problem for closed-neighborhood hypergraphs. More significantly, arbitrary hypergraph gaps can be realized exactly by split graphs.

## Proposition 2.1: Split realization

Let \(\mathcal H=(X,\mathcal E)\) be a finite hypergraph with at least one edge and with every edge nonempty. Construct a split graph \(S(\mathcal H)\) as follows:

- \(X\) induces a clique;
- for every \(E\in\mathcal E\), introduce an independent vertex \(v_E\);
- join \(v_E\) to precisely the vertices of \(E\).

Then

\[
\gamma(S(\mathcal H))=\tau(\mathcal H)
\quad\text{and}\quad
\rho(S(\mathcal H))=\nu(\mathcal H).
\]

### Proof

Let \(T\subseteq X\) be a minimum transversal of \(\mathcal H\). It is nonempty. Since \(X\) is a clique, \(T\) dominates all of \(X\), and since \(T\cap E\neq\varnothing\) for every \(E\), it dominates every \(v_E\). Hence

\[
\gamma(S(\mathcal H))\leq \tau(\mathcal H).
\]

Conversely, let \(D\) be a dominating set of \(S(\mathcal H)\). Begin with \(D\cap X\), and for each \(v_E\in D\), choose one arbitrary \(x_E\in E\). Set

\[
T=(D\cap X)\cup\{x_E:v_E\in D\}.
\]

Then \(|T|\leq |D|\). If \(v_F\notin D\), it must be dominated by a vertex of \(D\cap F\), so \(T\cap F\neq\varnothing\). If \(v_F\in D\), then \(x_F\in T\cap F\). Thus \(T\) is a transversal, proving

\[
\tau(\mathcal H)\leq\gamma(S(\mathcal H)).
\]

For the packing equality, two independent vertices \(v_E,v_F\) have disjoint closed neighborhoods exactly when \(E\cap F=\varnothing\). No two clique vertices can belong to a packing. Moreover, no clique vertex \(x\) can be packed together with any \(v_E\), since \(N[x]\) contains all of \(X\), while \(N[v_E]\) contains the nonempty set \(E\subseteq X\). Therefore every maximum packing is either a matching of hyperedges represented on the independent side or a singleton clique vertex. Since \(\nu(\mathcal H)\geq1\),

\[
\rho(S(\mathcal H))=\nu(\mathcal H).
\]

This proves the proposition. \(\square\)

Consequently, any characterization applying to arbitrary graph classes must, at a minimum, account for the transversal-to-matching ratios of arbitrary set-system classes.

## Corollary 2.2: A sharp bounded-rank result for split graphs

If every edge of \(\mathcal H\) has size at most \(r\), then

\[
\gamma(S(\mathcal H))\leq r\,\rho(S(\mathcal H)).
\]

Indeed, the union of the edges in a maximum matching is a transversal: otherwise another edge could be added to the matching. Its size is at most \(r\nu(\mathcal H)\).

The factor \(r\) is best possible. Let the ground set have size \(2r-1\), and let the edges be all its \(r\)-subsets. Any two edges intersect, so \(\nu=1\). A transversal must have size at least \(r\), since the complement of any set of size at most \(r-1\) contains an \(r\)-edge; conversely, every \(r\)-set is a transversal. Hence \(\tau=r\).

Graph-theoretically, this says that split graphs admitting a split partition \(C\cup I\) in which every nonisolated vertex of \(I\) has degree at most \(r\) satisfy the optimal bound \(\gamma\leq r\rho\). Isolated vertices contribute equally to \(\gamma\) and \(\rho\).

## An explicit unbounded split family

For \(n\geq2\), let the ground set be

\[
X_n=\binom{[n]}2,
\]

and for each \(i\in[n]\), let

\[
A_i=\{\{i,j\}:j\neq i\}.
\]

The hyperedges \(A_i\) are pairwise intersecting, since

\[
A_i\cap A_j=\{\{i,j\}\}.
\]

Thus \(\nu=1\). A transversal is precisely an edge cover of \(K_n\), and hence has minimum size \(\lceil n/2\rceil\). Therefore the split graph

\[
S_n=S(X_n,\{A_1,\dots,A_n\})
\]

satisfies

\[
\rho(S_n)=1,
\qquad
\gamma(S_n)=\left\lceil\frac n2\right\rceil.
\]

In particular, the ratio is unbounded even for split graphs of diameter two. Also, \(S_n\) occurs as an induced subgraph of \(S_{n+1}\).

# 3. A sharp degeneracy threshold

The following explicit family gives the negative half of a complete answer for the hierarchy of classes of \(d\)-degenerate graphs.

For \(n\geq3\), define a bipartite graph \(B_n\) with parts

\[
A_n=\{z,x_1,\dots,x_n\},
\qquad
Y_n=\{y_{ij}:1\leq i<j\leq n\},
\]

where

\[
N(y_{ij})=\{z,x_i,x_j\}.
\]

## Proposition 3.1

For \(n\geq4\),

\[
\rho(B_n)=2,
\qquad
\gamma(B_n)=1+\left\lceil\frac n2\right\rceil,
\]

and \(B_n\) is exactly 3-degenerate.

### Packing number

Every two vertices of \(A_n\) are at distance two:

- \(x_i,x_j\) have common neighbor \(y_{ij}\);
- \(z,x_i\) have a common neighbor \(y_{ij}\).

Every two vertices of \(Y_n\) have the common neighbor \(z\). Hence a packing contains at most one vertex from each bipartition class, so \(\rho(B_n)\leq2\).

For distinct \(i,j,k\), the vertices \(x_i\) and \(y_{jk}\) are nonadjacent and are at distance three. Their closed neighborhoods are disjoint, so they form a packing. Thus

\[
\rho(B_n)=2.
\]

### Domination number

Let \(D\) be a dominating set.

First suppose \(z\in D\). Then all vertices \(y_{ij}\) are dominated. Each \(x_i\) must either belong to \(D\) or be incident with a selected \(y_{ij}\). A selected \(x_i\) covers one of the \(x\)-vertices, while a selected \(y_{ij}\) covers two. Therefore at least \(\lceil n/2\rceil\) additional vertices are necessary, and a matching on the \(x_i\)'s, with one singleton if \(n\) is odd, attains this. Hence the minimum under \(z\in D\) is

\[
1+\left\lceil\frac n2\right\rceil.
\]

Now suppose \(z\notin D\). Put

\[
S=D\cap\{x_1,\dots,x_n\},
\qquad
U=\{x_1,\dots,x_n\}\setminus S,
\qquad
u=|U|.
\]

If \(x_i,x_j\in U\), then \(y_{ij}\) has none of \(z,x_i,x_j\) in \(D\), so \(y_{ij}\) itself must lie in \(D\). Thus, for \(u\geq2\), all \(\binom u2\) such vertices are forced. They also dominate every vertex in \(U\) and dominate \(z\). Consequently, the minimum with this value of \(u\) is

\[
n-u+\binom u2.
\]

For \(u\geq2\), this is minimized at \(u=2\), giving \(n-1\). If \(u=1\), one additional \(y\)-vertex is needed to dominate the sole unselected \(x_i\) and \(z\), again giving \(n\). If \(u=0\), one \(y\)-vertex is needed to dominate \(z\), giving \(n+1\). Hence the minimum with \(z\notin D\) is \(n-1\).

It follows that

\[
\gamma(B_n)
 =\min\left\{n-1,\ 1+\left\lceil\frac n2\right\rceil\right\}
 =1+\left\lceil\frac n2\right\rceil
\]

for every \(n\geq4\).

### Degeneracy

Every vertex \(y_{ij}\) has degree three. Any nonempty subgraph containing a \(y_{ij}\) therefore has a vertex of degree at most three; a subgraph containing no \(y_{ij}\) is edgeless. Thus \(B_n\) is 3-degenerate.

For \(n\geq4\), the whole graph has minimum degree at least three:

\[
\deg(y_{ij})=3,\qquad
\deg(x_i)=n-1\geq3,\qquad
\deg(z)=\binom n2.
\]

Hence its degeneracy is exactly three. \(\square\)

Therefore

\[
\frac{\gamma(B_n)}{\rho(B_n)}
 =\frac{1+\lceil n/2\rceil}{2}\longrightarrow\infty.
\]

## Corollary 3.2: Complete degeneracy classification

Let \(\mathcal D_d\) be the class of all graphs of degeneracy at most \(d\). Then

\[
R(\mathcal D_d)<\infty
\quad\Longleftrightarrow\quad
d\leq2.
\]

The positive implication for \(d\leq2\) is exactly the theorem from the supplied source asserting bounded ratio for all 2-degenerate graphs. The negative implication for every \(d\geq3\) follows from the graphs \(B_n\), which are bipartite and 3-degenerate.

Thus the source's 2-degenerate result is best possible with respect to degeneracy, even after restricting to bipartite graphs.

# 4. An effective undecidability barrier

The absence of restrictions on the description of \(\mathcal G\) is substantive, not merely terminological.

Consider the following presentation model: a graph class is specified by a Turing machine which, on input a finite adjacency matrix, decides whether the corresponding graph belongs to the class. Membership is required to be invariant under isomorphism.

## Theorem 4.1

There is no algorithm which, given such a membership decider and promised that its class is a hereditary subclass of the split graphs, determines whether \(R(\mathcal G)<\infty\).

The same is true when the promise is that \(\mathcal G\) is a monotone subclass of the bipartite 3-degenerate graphs.

### Proof

Fix a Turing machine \(M\). Say that \(n\) is eligible if \(M\) has not halted during its first \(n\) computation steps. Let \(\mathcal E\) denote the class of all edgeless graphs.

For the hereditary version, define

\[
\mathcal C_M^{\mathrm{her}}
 =
 \mathcal E
 \cup
 \left\{
 H:
 H\text{ is an induced subgraph of }S_n
 \text{ for some eligible }n\geq4
 \right\}.
\]

This class is hereditary and consists of split graphs.

It is uniformly decidable from \(M\). Indeed, suppose an \(h\)-vertex graph occurs as an induced subgraph of some \(S_n\). Every selected independent vertex carries one label \(i\), and every selected clique vertex carries a pair-label \(\{i,j\}\). The total number of labels appearing among the selected vertices is at most \(2h\). Relabeling those labels shows that the same induced graph occurs in some \(S_m\) with

\[
4\leq m\leq \max\{4,2h\}
\quad\text{and}\quad
m\leq n.
\]

Eligibility is downward closed: if \(n\) is eligible and \(m\leq n\), then \(m\) is eligible. Thus, on input \(H\), it suffices to simulate \(M\) for \(m\) steps and brute-force test induced-subgraph isomorphism for the finitely many values

\[
4\leq m\leq\max\{4,2|V(H)|\}.
\]

If \(M\) never halts, every \(n\) is eligible, so \(S_n\in\mathcal C_M^{\mathrm{her}}\) for all \(n\), and the ratios are unbounded.

If \(M\) halts after \(t\) steps, only finitely many \(n\) are eligible. Apart from the edgeless graphs, all members of \(\mathcal C_M^{\mathrm{her}}\) then have bounded order. Edgeless graphs have \(\gamma=\rho\). Hence \(R(\mathcal C_M^{\mathrm{her}})<\infty\).

Therefore

\[
R(\mathcal C_M^{\mathrm{her}})<\infty
\quad\Longleftrightarrow\quad
M\text{ halts}.
\]

An algorithm deciding boundedness would decide the halting problem.

For the monotone version, replace \(S_n\) by the bipartite 3-degenerate graphs \(B_n\), and define

\[
\mathcal C_M^{\mathrm{mon}}
 =
 \mathcal E
 \cup
 \left\{
 H:
 H\text{ is a subgraph of }B_n
 \text{ for some eligible }n\geq4
 \right\}.
\]

This class is monotone, bipartite, and 3-degenerate. The same finite-support argument applies: selected vertices of \(B_n\) involve at most \(2h\) indices, in addition to the distinguished vertex \(z\). Thus membership is again decidable by testing only finitely many \(B_m\). If \(M\) does not halt, all \(B_n\) belong and the ratio is unbounded; if \(M\) halts, all nonedgeless members have bounded order. This gives the second undecidability assertion. \(\square\)

This does not preclude a structural theorem for naturally or finitely described graph classes. It does show that no effective characterization can cover arbitrary machine-presented hereditary or monotone classes.

# 5. What is settled and what remains open

The arguments establish:

- an exact reduction from arbitrary hypergraph transversal/matching gaps to domination/packing gaps on split graphs;
- the optimal factor \(r\) for split realizations of hypergraphs of rank at most \(r\);
- explicit unbounded-ratio split graphs with \(\rho=1\);
- explicit bipartite 3-degenerate graphs with \(\rho=2\) and unbounded domination number;
- the sharp dichotomy that the class of all \(d\)-degenerate graphs has bounded ratio exactly for \(d\leq2\);
- undecidability of the unrestricted effective class-recognition problem, even under hereditary-split or monotone-bipartite-3-degenerate promises.

The principal gap is unchanged: there is no structural necessary-and-sufficient condition for broad natural families such as arbitrary hereditary or monotone classes. The split-graph reduction is an exact reformulation rather than such a graph-structural characterization. Moreover, I have not independently checked whether some of these elementary constructions already appear in the source paper, so no novelty claim is made.