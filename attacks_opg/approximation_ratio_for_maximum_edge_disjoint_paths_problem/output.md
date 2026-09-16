```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A deterministic O(sqrt(h+1))-approximation is obtainable when a feedback vertex set of size h is supplied, but this does not improve the worst-case planar bound.",
  "would_publish": false,
  "caveats": "Requires a supplied feedback vertex set; novelty is not claimed; no new hardness result is established."
}
```

## 1. Statement of the partial result

I do not obtain an improved approximation for all planar graphs. The following structural special case is self-contained and does not require planarity of either the supply graph or the demands.

I use the standard **undirected, unit-capacity, unweighted MaxEDP** convention: each listed demand may be selected at most once. Terminal vertices may occur in several demands. Demand endpoints are distinct within each pair.

**Theorem.** Let \(G\) be an undirected graph, and suppose a set \(X\subseteq V(G)\) is supplied such that \(G-X\) is a forest. Write \(h=|X|\). There is a deterministic polynomial-time approximation algorithm for MaxEDP with ratio
\[
4\sqrt{2h}+6.
\]
More precisely, for every integer \(0\le L\le h\), there is an algorithm with ratio
\[
R_L=4L+6+\frac{2h}{L+1}.
\tag{1}
\]

Thus, on planar instances supplied with a feedback vertex set of size
\[
h=O(n^{1-\delta}),
\]
the ratio becomes \(O(n^{1/2-\delta/2})\), with no restriction on the placement of the demand pairs.

The proof has two ingredients:

1. a constant-factor comparison algorithm for paths passing through one specified vertex;
2. LP rounding for paths that visit \(X\) only a few times.

---

## 2. A rooted comparison lemma

**Lemma 1.** For any vertex \(v\), one can find in polynomial time a feasible routing of at least \(b/2\) demands whenever there exists a feasible routing of \(b\) demands whose paths all contain \(v\).

The paths returned by the algorithm need not themselves contain \(v\).

### Proof

Give each demand \(i=(s_i,t_i)\) two distinct endpoint tokens \(a_i,b_i\), located at \(s_i,t_i\), respectively. Tokens remain distinct even when their locations coincide.

For a set \(A\) of tokens, let \(r(A)\) be the maximum number of tokens in \(A\) that can be linked to \(v\) by mutually edge-disjoint paths. A token located at \(v\) has a length-zero link.

This rank is computable by a single-source maximum-flow calculation. Add a source with one unit-capacity arc to the location of each token. Replace each undirected supply edge by two opposite unit-capacity arcs. Oppositely directed flow on an edge can be canceled; integral flow then decomposes into edge-disjoint undirected links.

If \(T_U\) denotes the tokens located in \(U\), max-flow/min-cut gives
\[
r(A)=
\min_{U\subseteq V(G)\setminus\{v\}}
\bigl(|\delta(U)|+|A\setminus T_U|\bigr).
\tag{2}
\]

In particular, \(r\) is monotone and submodular. For completeness, choose minimizing sets \(U,W\) for token sets \(A,B\). Cut submodularity gives
\[
|\delta(U)|+|\delta(W)|
\ge |\delta(U\cup W)|+|\delta(U\cap W)|,
\]
and, elementwise,
\[
|A\setminus T_U|+|B\setminus T_W|
\ge
|(A\cup B)\setminus T_{U\cup W}|
+
|(A\cap B)\setminus T_{U\cap W}|.
\]
Together with (2), these inequalities prove submodularity.

Now process the demands in any order. Add a demand whenever the endpoint tokens of all demands selected so far remain jointly linkable to \(v\). Let \(A\) be the final token set and \(a\) the number of selected demands. Thus
\[
r(A)=|A|=2a.
\]

For every unselected demand \(i\), maximality implies
\[
r(A\cup\{a_i,b_i\})-r(A)\le 1.
\tag{3}
\]
Indeed, a rejected demand cannot become feasible after more endpoint tokens have been added. For a selected demand the same increment is zero.

Suppose \(b\) demands have an edge-disjoint routing through \(v\), and let \(B\) be their endpoint tokens. Splitting these paths at \(v\) shows that
\[
r(B)=2b.
\]
Submodularity and (3) yield
\[
\begin{aligned}
2b
&=r(B)\\
&\le r(A\cup B)\\
&\le r(A)+
\sum_{i\text{ among these }b\text{ demands}}
\bigl(r(A\cup\{a_i,b_i\})-r(A)\bigr)\\
&\le 2a+b.
\end{aligned}
\]
Hence \(a\ge b/2\).

Finally, compute the edge-disjoint links for the selected endpoint tokens. Concatenate the two links belonging to each demand, reversing one of them. This produces an \(s_i\)-\(t_i\) trail. Delete cycles to obtain a simple path. All resulting paths remain edge-disjoint because each uses only edges of its own two links. ∎

---

## 3. Fractionally packing paths with few visits to \(X\)

Call a path **short** if it contains at most \(L\) vertices of \(X\).

For each demand \(i\), let \(\mathcal P_i^L\) be its simple short paths. Consider the path-packing LP
\[
\begin{array}{ll}
\text{maximize}
&\displaystyle F=\sum_i\sum_{P\in\mathcal P_i^L}x_{i,P},\\[1ex]
\text{subject to}
&\displaystyle
\sum_i\sum_{\substack{P\in\mathcal P_i^L\\ e\in E(P)}}x_{i,P}\le 1
\qquad(e\in E(G)),\\[2ex]
&\displaystyle
\sum_{P\in\mathcal P_i^L}x_{i,P}\le 1
\qquad(i\text{ a demand}),\\[2ex]
&x_{i,P}\ge 0.
\end{array}
\tag{4}
\]

Every integral routing consisting of short paths is feasible for this LP.

### Polynomial-time implementation

The restriction defining short paths does not make (4) computationally problematic.

For each commodity, use a layered directed network with states
\[
(u,j),\qquad u\in V(G),\quad 0\le j\le L,
\]
where \(j\) counts visits to \(X\), including the initial vertex when appropriate. Traversing an edge into \(X\) increments the counter; other traversals leave it unchanged. Connect all admissible states at the destination to a commodity-specific sink.

Use a fractional flow of value at most one for each commodity. For every original supply edge, impose one capacity constraint aggregating its flow over **all layers, both orientations, and all commodities**.

This is a polynomial-size LP. Decompose its flows into paths in the layered networks. Their projections may be walks, but deleting cycles produces simple original paths without increasing either edge usage or the number of visits to \(X\). Conversely, every simple short path lifts to the layered network.

Consequently, (4) can be solved with a polynomial-size path support. Zero variables are discarded below.

---

## 4. Rounding the short-path LP

**Lemma 2.** A feasible solution of (4) of value \(F\) can be rounded deterministically in polynomial time to a feasible routing of at least
\[
\frac{F}{4L+6}
\]
demands.

### 4.1 Splitting \(X\) into leaves

Replace every vertex \(x\in X\) by a separate degree-one copy for each edge incident with \(x\). In particular, an edge with both endpoints in \(X\) becomes an isolated edge between two such copies.

The resulting graph \(\widehat G\) is a forest: it consists of \(G-X\), with leaves attached, together with isolated edges and possibly isolated vertices. Its edges are in bijection with \(E(G)\).

A simple path \(P\) containing at most \(L\) vertices of \(X\) becomes a union of at most \(L+1\) nonempty paths in \(\widehat G\). Splitting an internal vertex of \(P\cap X\) increases the number of pieces by one; splitting an endpoint does not.

Root every component of \(\widehat G\). For a nonempty path segment \(S\), let its **top** be its vertex closest to the root. Mark the one or two edges of \(S\) incident with its top.

The following elementary observation controls intersections.

**Top-edge observation.** If segments \(S,T\) share an edge and the top of \(S\) is at least as deep as the top of \(T\), then \(T\) contains a marked edge of \(S\).

To see this, take a shared edge in a downward branch of \(S\) from its top. If \(T\) avoided the first edge of that branch, then \(T\), being connected and containing the shared edge, would lie entirely below that first edge. Its top would therefore be strictly deeper than the top of \(S\), a contradiction.

For each original path \(P\), let \(M(P)\) be the marked edges of all its segments. Then
\[
|M(P)|\le 2(L+1).
\tag{5}
\]

### 4.2 Orienting the conflict graph

Construct a conflict graph whose vertices are the positive, demand-labelled path variables in (4). Two vertices conflict if their paths share a supply edge or belong to the same demand.

Orient each conflict as follows.

* For a shared-edge conflict, choose a shared edge and its two containing segments in \(\widehat G\). Orient from the path whose segment has the deeper top, breaking ties arbitrarily.
* If there is no shared edge and the conflict is solely a common demand, orient arbitrarily.

By the top-edge observation, every outgoing neighbor of \(P\) either

* uses an edge of \(M(P)\), or
* belongs to the same demand as \(P\).

Thus outgoing conflicts are witnessed by at most
\[
\beta=2L+3
\tag{6}
\]
resources: the marked edges and the demand label.

Write \(x_P\) for the fractional weight of a labelled path. Each resource has total fractional load at most one, and \(P\) itself contributes \(x_P\) to every one of its witnessing resources. Therefore
\[
\sum_{Q\in N^+(P)}x_Q
\le \beta(1-x_P).
\tag{7}
\]
This inequality continues to hold in every induced subgraph of the conflict graph.

### 4.3 A weighted greedy independent set

Consider any nonempty remaining vertex set \(W\). For \(P\in W\), let
\[
d_W(P)=x_P+\sum_{Q\in N_W(P)}x_Q
\]
be the total weight of its closed neighborhood.

Using (7),
\[
\begin{aligned}
\sum_{P\in W}x_Pd_W(P)
&=
\sum_{P\in W}x_P^2
+
2\sum_{\substack{P\to Q\\P,Q\in W}}x_Px_Q\\
&\le
\sum_{P\in W}x_P^2
+
2\beta\sum_{P\in W}x_P(1-x_P)\\
&\le
2\beta\sum_{P\in W}x_P.
\end{aligned}
\tag{8}
\]
Hence some \(P\in W\) has \(d_W(P)\le 2\beta\).

Repeatedly choose a vertex of minimum closed-neighborhood weight, retain it, and delete its closed neighborhood. Each retained vertex deletes weight at most \(2\beta\). Since the original total weight is \(F\), at least
\[
\frac{F}{2\beta}=\frac{F}{4L+6}
\]
vertices are retained.

They form an independent set in the conflict graph, so their original paths are edge-disjoint and represent distinct demands. This proves Lemma 2. ∎

---

## 5. Combining short paths and rooted routings

Fix \(L\).

1. Solve and round (4), obtaining a routing of size \(a_0\).
2. For each \(v\in X\), run Lemma 1, obtaining a routing of size \(a_v\).
3. Return the largest candidate. Write its size as \(z\).

Consider an optimum routing, partitioned into \(q_{\mathrm{short}}\) short paths and \(q_{\mathrm{long}}\) remaining paths.

By Lemma 2,
\[
q_{\mathrm{short}}
\le (4L+6)a_0
\le (4L+6)z.
\tag{9}
\]

For \(v\in X\), let \(b_v\) be the number of long optimum paths containing \(v\). Every long path contains at least \(L+1\) vertices of \(X\), so
\[
(L+1)q_{\mathrm{long}}
\le \sum_{v\in X}b_v.
\]
Lemma 1 gives \(b_v\le 2a_v\), and consequently
\[
q_{\mathrm{long}}
\le \frac{2h}{L+1}z.
\tag{10}
\]
When \(h=0\), there are no long paths, and the same inequality holds.

Adding (9) and (10) proves
\[
\operatorname{OPT}
\le
\left(4L+6+\frac{2h}{L+1}\right)z,
\]
which is (1).

Now take
\[
t=\max\left\{1,\left\lceil\sqrt{h/2}\right\rceil\right\},
\qquad L=t-1.
\]
For \(h>0\),
\[
R_L=4t+2+\frac{2h}{t}
\le 4\sqrt{2h}+6.
\]
For \(h=0\), \(R_0=6\), so the same bound holds.

All steps—the layered LP, flow decomposition, conflict-graph rounding, and the \(h\) rooted procedures—are polynomial-time. The output has congestion exactly one. ∎

---

## 6. What this does and does not settle

The result gives a genuine improvement on the subclass with a supplied sublinear-size feedback vertex set:
\[
h=o(n)
\quad\Longrightarrow\quad
O(\sqrt{h+1})=o(\sqrt n).
\]
It applies to arbitrary terminal placements, not merely fully planar instances.

However, planarity alone does not force \(h=o(n)\). A \(q\times q\) grid contains
\[
\left\lfloor q/2\right\rfloor^2
\]
vertex-disjoint four-cycles, so every feedback vertex set has size \(\Omega(q^2)=\Omega(n)\). The theorem therefore retains a square-root-order guarantee on grids. Taking \(X=V(G)\) also gives only \(O(\sqrt n)\), even without planarity.

Accordingly:

* **No improved worst-case ratio for unrestricted planar MaxEDP is established.**
* No new inapproximability result is established; the hardness development reported in the supplied catalog is not rederived here.
* I make no novelty claim for this feedback-vertex-set bound. Its role here is a fully proved structural partial result, not a claimed resolution of the original problem.