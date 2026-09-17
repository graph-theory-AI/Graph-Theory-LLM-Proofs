```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit gap reduction shows that RFCPP has no polynomial-time o(log |V|)-approximation unless P=NP, and hence rules out constant-factor approximation under that assumption.",
  "would_publish": true,
  "caveats": "This is a complexity-theoretic negative answer, not a proof of P≠NP; it uses standard NP-completeness of directed two-linkage, and novelty has not been independently checked."
}
```

# A logarithmic inapproximability theorem for RFCPP

I obtain a negative answer under the standard complexity assumption \(P\ne NP\). The reduction also works when the requests form a matching.

The important point is not merely to construct instances with \(\operatorname{OPT}=o(|R|)\). Instead, the construction below turns an NP-complete linkage problem into a gap between

\[
\operatorname{OPT}=|R|
\qquad\text{and}\qquad
\operatorname{OPT}=O\!\left(\frac{|R|}{\log |V|}\right).
\]

## 1. Statement and conventions

A \(\rho\)-approximation for this maximization problem returns an enumeration realizing at least \(\operatorname{OPT}/\rho\) requests.

### Theorem
Unless \(P=NP\), RFCPP has no deterministic polynomial-time approximation algorithm with ratio \(o(\log |V(D)|)\). In particular, it has no polynomial-time constant-factor approximation.

The same conclusion holds when \(R\) is a matching.

For randomized algorithms with the usual success guarantee, the corresponding consequence is \(RP=NP\).

The proof uses the standard NP-completeness of the following problem:

> **Directed two-linkage.** Given a digraph \(G\) and four distinct vertices \(s_1,t_1,s_2,t_2\), decide whether there are vertex-disjoint directed paths \(s_1\leadsto t_1\) and \(s_2\leadsto t_2\).

No other hardness result is needed.

The acyclic-subgraph reformulation in the previous attempt is valid and will be used. Namely, RFCPP is equivalent to finding an acyclic subgraph that makes as many requested pairs comparable as possible. One direction follows by taking the forward arcs of an enumeration; the other follows by topologically ordering an acyclic subgraph.

---

## 2. A four-port linkage gadget

### 2.1 Normalizing the two-linkage instance

We may assume that the two-linkage instance satisfies:

1. \(s_1,s_2\) have indegree zero;
2. \(t_1,t_2\) have outdegree zero;
3. \(s_i\leadsto t_i\) exists individually for \(i=1,2\);
4. every vertex is reachable from at least one of \(s_1,s_2\), and can reach at least one of \(t_1,t_2\).

Here is a polynomial normalization preserving the answer. Delete all arcs entering the sources and leaving the sinks. This preserves every feasible two-linkage, because none of the four terminals can be internal to either path of a vertex-disjoint solution. If either individual required path is absent, replace the instance by the fixed NO-instance

\[
s_1\to z,\quad s_2\to z,\quad z\to t_1,\quad z\to t_2.
\]

Otherwise, delete vertices not reachable from the sources or unable to reach the sinks. The required reachability paths for retained vertices remain in the retained induced subgraph.

Write \(G\) for the normalized instance.

### 2.2 Construction of the core

Add four distinct new vertices, called ports,

\[
a,\ b,\ \ell,\ r.
\]

The **core** \(K\) consists of \(G\), these ports, and the arcs

\[
a\leftrightarrow s_1,\qquad
b\leftrightarrow t_2,\qquad
t_2\to s_1,\qquad
t_1\to\ell,\qquad
r\to s_2.
\tag{1}
\]

Here \(x\leftrightarrow y\) denotes both opposite arcs.

The ports \(a,b\) will be the outer ports. A recursively constructed network will be attached between the inner ports \(\ell,r\).

Two properties of this core are central.

### Lemma 1: the YES property
If the two-linkage instance is a YES-instance, \(K\) contains vertex-disjoint paths

\[
a\leadsto\ell
\quad\text{and}\quad
r\leadsto b.
\]

#### Proof
Extend the two vertex-disjoint paths in \(G\) by their respective port arcs:

\[
a\to s_1\leadsto t_1\to\ell,
\qquad
r\to s_2\leadsto t_2\to b.
\]
They remain vertex-disjoint. ∎

### Lemma 2: crossing closure in the NO case
Suppose the two-linkage instance is a NO-instance. In any acyclic subgraph \(H\subseteq K\), its port reachability relation satisfies

\[
a\leadsto_H\ell,\ r\leadsto_H b
\quad\Longrightarrow\quad
a\leadsto_H b,\ r\leadsto_H\ell,
\tag{2}
\]

and

\[
b\leadsto_H\ell,\ r\leadsto_H a
\quad\Longrightarrow\quad
b\leadsto_H a,\ r\leadsto_H\ell.
\tag{3}
\]

#### Proof
A simple \(a\)-to-\(\ell\) path in \(K\) necessarily consists of

\[
a\to s_1,\quad\text{a path in }G\text{ from }s_1\text{ to }t_1,
\quad t_1\to\ell.
\]

In particular, it cannot use \(t_2\to s_1\), since that would repeat \(s_1\). Similarly, a simple \(r\)-to-\(b\) path consists of a path in \(G\) from \(s_2\) to \(t_2\), extended by its port arcs.

In a NO-instance, any such two paths intersect. Switching at an intersection gives both reachabilities on the right of (2).

For (3), every simple \(b\)-to-\(\ell\) path begins

\[
b\to t_2\to s_1,
\]

while every \(r\)-to-\(a\) path ends through \(s_1\to a\). Thus these paths intersect at \(s_1\), and switching again proves the implication. ∎

The second implication holds regardless of the answer to the linkage instance.

---

## 3. Compressing a NO-core to a tree

Let \(Q\) be the undirected tree on the four ports and two new vertices \(x,y\), with edges

\[
ax,\ bx,\ xy,\ y\ell,\ yr.
\tag{4}
\]

Thus \(a,b\) form the outer pair, \(\ell,r\) the inner pair, and \(xy\) is the central edge.

We allow either \(Q\), or the four-leaf star \(Q/xy\) obtained by contracting the central edge.

### Lemma 3: exact port-reachability representation
If the linkage instance is NO, then for every acyclic \(H\subseteq K\), there is an oriented forest obtained by deleting edges from either \(Q\) or \(Q/xy\) whose reachability relation on the four ports is exactly that of \(H\).

#### Proof
Within the core, \(a\) and \(b\) each have only one neighbor. An acyclic subgraph cannot contain both directions of either incident bidirected edge. Consequently, each of \(a,b\) is a local source, a local sink, or isolated. An isolated port can be assigned either type.

The port \(r\) is a local source, and \(\ell\) a local sink. Hence all port reachabilities go from source-type ports to sink-type ports.

If \(a,b\) are both sources, all nontrivial port reachabilities have head \(\ell\). They are represented by an appropriately oriented substar of \(Q/xy\). If \(a,b\) are both sinks, all nontrivial port reachabilities have tail \(r\), and the same argument applies.

It remains to consider opposite types. First suppose \(a\) is a source and \(b\) a sink. The possible reachabilities are the four entries

\[
\begin{array}{c|cc}
 & b & \ell\\ \hline
a & a\leadsto b & a\leadsto\ell\\
r & r\leadsto b & r\leadsto\ell
\end{array}.
\]

Call \(a\leadsto\ell\) and \(r\leadsto b\) the two crossing entries.

* If both crossing entries are present, Lemma 2 forces all four entries. The contracted star, oriented from \(a,r\) toward \(b,\ell\), represents exactly this relation.
* If neither crossing entry is present, use the disjoint paths \(a\to x\to b\) and \(r\to y\to\ell\), retaining each only when its corresponding reachability is present. Omit \(xy\).
* If only \(a\leadsto\ell\) is present among the crossing entries, use
  \[
  a\to x\to y\to\ell.
  \]
  Add \(x\to b\) precisely when \(a\leadsto b\) is present, and add \(r\to y\) precisely when \(r\leadsto\ell\) is present.
* The case with only \(r\leadsto b\) is symmetric.

These constructions have exactly the prescribed port relations.

When \(b\) is a source and \(a\) a sink, use the same construction with \(a,b\) interchanged, invoking (3). This covers every case. ∎

### Why exact port reachability suffices

Suppose a digraph is assembled from cores and other pieces that meet only at ports. Replacing the restriction of an acyclic subgraph to each core by the forest in Lemma 3:

* preserves every reachability between vertices outside core interiors; and
* preserves acyclicity.

For the second assertion, any directed cycle after replacement would decompose into directed paths through the replacement pieces. Replace each such port-to-port path by an original path with the same endpoints. This produces a directed closed walk in the original acyclic subgraph, a contradiction.

This argument allows simultaneous replacement of all cores, including recursively nested ones.

---

## 4. Recursive strong instances

For each \(h\geq 0\), construct a two-port digraph \(F_h\).

### Base case

Let \(F_0\) be the bidirected path

\[
a_0\leftrightarrow z\leftrightarrow b_0.
\]

Its marked vertex is \(z\).

### Recursive step

Take a fresh copy of the core \(K\) and two disjoint copies \(F_{h-1}^{L}\), \(F_{h-1}^{R}\). Identify

\[
b_{h-1}^{L}=a_{h-1}^{R},
\qquad
\ell=a_{h-1}^{L},
\qquad
r=b_{h-1}^{R}.
\tag{5}
\]

The outer ports of \(F_h\) are the core’s \(a,b\).

The marked vertices are the \(2^h\) base-case vertices. Label them by binary strings \(w\in\{0,1\}^h\), according to the recursive left/right choices, and denote them by \(z_w\).

Define

\[
R_h=\bigl\{\{z_u,z_v\}:u,v\in\{0,1\}^h
\text{ differ in exactly one coordinate}\bigr\}.
\tag{6}
\]

Thus the request graph on the marked vertices is the \(h\)-dimensional hypercube. With \(N=2^h\),

\[
|R_h|=\frac{hN}{2}.
\tag{7}
\]

The construction has size \(O(2^h(|V(G)|+|A(G)|))\). In fact,

\[
|V(F_h)|=(|V(G)|+4)2^h-(|V(G)|+1).
\tag{8}
\]

### Lemma 4: strong connectivity
Every \(F_h\) is strongly connected, whether the linkage instance is YES or NO.

#### Proof
The base case is strong.

At an inductive step, the two child networks are strong and share one vertex, so their union is strong and connects \(\ell\) to \(r\).

The individually existing paths \(s_1\leadsto t_1\) and \(s_2\leadsto t_2\), together with the added connections, give a closed directed walk through

\[
s_1,\ t_1,\ \ell,\ r,\ s_2,\ t_2,\ s_1.
\]

Every vertex of \(G\) is reachable from one of the sources and can reach one of the sinks. Therefore it belongs to the same strongly connected component as this walk. The bidirected attachments include \(a,b\), and the strong child network includes all its vertices. ∎

### Lemma 5: completeness
If the linkage instance is YES, \(F_h\) has a directed \(a_h\)-to-\(b_h\) path containing all its marked vertices. Consequently,

\[
\operatorname{OPT}(F_h,R_h)=|R_h|.
\tag{9}
\]

#### Proof
Induct on \(h\). The claim is immediate for \(F_0\).

The two child paths concatenate, through their identified outer ports, to an \(\ell\)-to-\(r\) path containing all child marked vertices. Lemma 1 supplies vertex-disjoint core paths \(a\leadsto\ell\) and \(r\leadsto b\). Their interiors are disjoint from the child networks, so concatenating all three paths gives the required simple directed path.

Order its vertices along the path. Every marked pair, and therefore every request, is forward-connected. ∎

---

## 5. Soundness: compression to a triangle cactus

Define \(B_h\) as follows. Its vertices are all binary strings of length at most \(h\). For every string \(w\) of length less than \(h\), put a bidirected triangle on

\[
w,\quad w0,\quad w1.
\tag{10}
\]

Its underlying undirected graph is a cactus of triangles: parent and child triangles meet at a single vertex. The marked vertices are its leaves \(\{0,1\}^h\), with request set (6).

### Lemma 6: NO-case domination
If the linkage instance is NO, then

\[
\operatorname{OPT}(F_h,R_h)
\leq
\operatorname{OPT}(B_h,R_h).
\tag{11}
\]

#### Proof
Take any acyclic subgraph \(H\subseteq F_h\). Apply Lemma 3 to every core. Keep the restrictions to the base-case bidirected paths.

By the preceding replacement argument, the resulting digraph is acyclic and preserves every marked-vertex reachability present in \(H\).

Consider the ambient undirected graph obtained by putting the full tree \(Q\) in every core position. Each central edge \(xy\) is a bridge: it is the only connection between that core’s outer part and its entire recursively attached inner network.

Some of these bridges have already been contracted by Lemma 3. Contract all remaining central bridges, deleting any resulting loops. This does not create a directed cycle. Indeed, identifying the ends of an ambient bridge could create a directed cycle only if there were already a path between its ends avoiding that bridge.

After these contractions, the underlying graph is exactly the graph obtained by subdividing every edge of \(B_h\) once, together with the two pendant outer-port edges at the top.

To see the triangle corresponding to a recursive node, its three main vertices are:

* that node’s contracted center;
* the left child’s outer center, or marked vertex in the base case;
* the right child’s outer center, or marked vertex in the base case.

The three port identifications in (5) supply the three subdivision vertices around this triangle.

A directed path between marked vertices cannot use either top pendant vertex internally. Suppress the degree-two subdivision vertices along such paths. Then take a topological order of the contracted acyclic digraph, restrict it to the main vertices, and orient all edges of \(B_h\) forward in that order.

Every marked-vertex reachability under consideration survives. This proves (11). ∎

The central-edge bridge property is important: the proof does not contract arbitrary edges of an acyclic digraph.

---

## 6. A request bound for the triangle cactus

The remaining argument is purely combinatorial.

### Lemma 7
For \(h\geq1\), with \(N=2^h\),

\[
\operatorname{OPT}(B_h,R_h)\leq 3N.
\tag{12}
\]

#### Proof
Fix an enumeration of \(B_h\), and consider its forward subgraph.

For a vertex \(v\) of the rooted binary tree, define:

* \(A_v\): the number of marked leaves below \(v\) that can reach \(v\);
* \(B_v\): the number of marked leaves below \(v\) reachable from \(v\);
* \(F_v=A_v+B_v\);
* \(q_v=\min\{A_v,B_v\}\).

For a marked leaf, allow a zero-length path, so

\[
A_v=B_v=1,\qquad F_v=2,\qquad q_v=1.
\tag{13}
\]

The descendant subgraph below \(v\) meets the rest of \(B_h\) only at \(v\). Consequently, if \(x,y\) are its children,

\[
A_v=\sum_{\substack{u\in\{x,y\}\\u\text{ precedes }v}} A_u,
\qquad
B_v=\sum_{\substack{u\in\{x,y\}\\v\text{ precedes }u}} B_u.
\tag{14}
\]

For an internal vertex \(v\), put

\[
L_v=F_x+F_y-F_v.
\tag{15}
\]

Equation (14) selects exactly one of \(A_u,B_u\) from each child. Therefore

\[
L_v\geq q_x+q_y.
\tag{16}
\]

### Requests assigned to one node

Assign a request to the least common ancestor of its leaves in the rooted binary tree.

At each internal vertex, the assigned requests form a perfect matching between its left and right descendant leaf sets: the suffixes after the differing coordinate are identical.

Let \(M_v\) be the number of realized requests assigned to \(v\). Name the two children so that \(x\) precedes \(y\) in the enumeration. Every realized request crossing their descendant sets must run from a leaf reaching \(x\) to a leaf reachable from \(y\). Since these requests form a matching,

\[
M_v\leq \min\{A_x,B_y\}.
\tag{17}
\]

There are three positions of \(v\) relative to its children.

* If \(v\) precedes both children, then
  \[
  L_v=A_x+A_y,
  \]
  so \(M_v\leq L_v\).
* If \(v\) follows both children, then
  \[
  L_v=B_x+B_y,
  \]
  so again \(M_v\leq L_v\).
* If \(x\) precedes \(v\), which precedes \(y\), then
  \[
  A_v=A_x,\qquad B_v=B_y,
  \]
  and \(M_v\leq q_v\).

Thus, uniformly,

\[
M_v\leq L_v+q_v.
\tag{18}
\]

### Summing the inequalities

Let \(o\) denote the root. Telescoping (15) gives

\[
\sum_{v\text{ internal}}L_v=2N-F_o.
\tag{19}
\]

Summing (16), and using \(q_v=1\) at each of the \(N\) leaves, gives

\[
\sum_{v\text{ internal}}L_v
\geq
N+\sum_{\substack{v\text{ internal}\\v\ne o}}q_v.
\tag{20}
\]

Every request is assigned exactly once. Combining (18)–(20),

\[
\begin{aligned}
\sum_{v\text{ internal}}M_v
&\leq \sum_v L_v+\sum_v q_v\\
&\leq 2\sum_vL_v-N+q_o\\
&=3N-2F_o+q_o\\
&\leq3N.
\end{aligned}
\]

This holds for every enumeration. ∎

Combining Lemmas 6 and 7, a NO-instance of two-linkage produces

\[
\operatorname{OPT}(F_h,R_h)\leq3\cdot2^h.
\tag{21}
\]

---

## 7. The approximation gap

The construction gives the unconditional gap statement

\[
\begin{array}{ll}
\text{two-linkage YES:}
&\displaystyle \operatorname{OPT}(F_h,R_h)=h2^{h-1},\\[2mm]
\text{two-linkage NO:}
&\displaystyle \operatorname{OPT}(F_h,R_h)\leq3\cdot2^h.
\end{array}
\tag{22}
\]

The ratio between the YES value and the NO upper bound is

\[
\frac{h2^{h-1}}{3\cdot2^h}=\frac h6.
\tag{23}
\]

### Excluding every constant ratio

Suppose a polynomial-time \(\rho\)-approximation exists for some fixed constant \(\rho\). Choose a fixed integer \(h>6\rho\).

The construction is polynomial in the two-linkage input size because \(h\) is fixed. In the YES case, the approximation must output more than \(3\cdot2^h\) realized requests; in the NO case, no enumeration can do so.

The output value is polynomial-time computable by reachability in the forward subgraph. Hence the approximation would decide directed two-linkage in polynomial time, implying \(P=NP\).

### Logarithmic inapproximability

Let \(q\) be the size of the normalized linkage instance, and choose

\[
h=\lceil\log_2 q\rceil.
\]

The constructed instance has polynomial size, with

\[
|V(F_h)|=O(q^2),
\qquad
\log |V(F_h)|=\Theta(h).
\]

An \(o(\log |V|)\)-approximation therefore has ratio \(o(h)\), eventually smaller than \(h/6\), and again distinguishes the two cases in (22). Finitely many smaller input sizes can be handled directly.

The same construction also excludes an \(o(\log |R|)\)-approximation, since

\[
\log |R_h|=\Theta(h).
\]

---

## 8. Restricting the requests to a matching

The following exact transformation preserves strong connectivity and the optimum.

For each request \(r=\{u,v\}\), add two new vertices \(u_r,v_r\), with bidirected edges

\[
u_r\leftrightarrow u,\qquad v_r\leftrightarrow v.
\]

Replace \(r\) by \(\{u_r,v_r\}\). The new request set is a matching.

Any forward path realizing \(\{u_r,v_r\}\) must pass through \(u\) and \(v\). Restricting the enumeration to the old vertices therefore realizes the original request.

Conversely, given an enumeration realizing an original request in the direction \(u\leadsto v\), place \(u_r\) immediately before \(u\) and \(v_r\) immediately after \(v\). All such insertions can be made simultaneously, using separate before/after blocks at each old vertex. Thus every originally realized request remains realized.

Consequently, the optima are equal, and solutions transfer without loss. The added size is \(O(|R|)\), which preserves the polynomial-size logarithmic-gap construction.

---

## 9. What this establishes, and what it does not

The reduction proves:

\[
\boxed{\text{A deterministic polynomial-time constant approximation for RFCPP would imply }P=NP.}
\]

Conversely, if \(P=NP\), RFCPP can be solved exactly in polynomial time: the decision question “is there an enumeration realizing at least \(k\) requests?” is in NP, and standard search-to-decision recovers an optimal enumeration. Thus deterministic constant-factor approximability is equivalent to \(P=NP\).

For randomized approximation algorithms, the threshold test above has no false positives on NO-instances. Standard success guarantees would therefore put directed two-linkage in \(RP\), implying \(RP=NP\).

This is stronger than an obstruction to satisfying a constant fraction of all requests: the YES/NO construction supplies the missing approximation-hardness gap. The argument does not use Proposition 4 of the source paper or assume another graph-theoretic conjecture.

The remaining caveats are complexity-theoretic and bibliographic: this does not prove \(P\ne NP\), and I have not independently checked whether an equivalent reduction has appeared elsewhere.