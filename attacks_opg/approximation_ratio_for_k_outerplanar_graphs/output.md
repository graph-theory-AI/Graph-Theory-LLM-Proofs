```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every k, an explicit k-outerplanar subcubic instance of treewidth at most 2k has natural MaxEDP/MaxIMF LP integrality gap exactly k.",
  "would_publish": false,
  "caveats": "This refutes a parameter-independent natural-LP bound, not constant-factor approximation relative to the integer optimum; no novelty is claimed."
}
```

## 1. What this resolves—and what it does not

The question combines two different assertions:

1. A polynomial-time algorithm approximates the **integer optimum** within an absolute constant.
2. The natural multicommodity-flow LP has an **absolute constant integrality gap**, and can consequently be rounded without congestion.

These are not equivalent. I give a self-contained negative answer to the second assertion when the constant must be independent of outerplanarity or treewidth.

I also prove a matching-order upper bound for a restricted class: on subcubic, unit-capacity graphs with leaf terminals, the worst natural-LP gap is \(\Theta(r)\), where \(r\) is the treewidth bound.

Neither result excludes a constant-factor algorithm using a different approach.

## 2. The LP and the lower-bound theorem

For demand pairs \((s_i,t_i)\), let \(\mathcal P_i\) be the set of simple \(s_i\)-\(t_i\) paths. The natural unit-capacity MaxEDP LP is
\[
\begin{aligned}
\max\quad &\sum_i\sum_{P\in\mathcal P_i}x_{i,P},\\
\text{subject to}\quad
&\sum_i\sum_{\substack{P\in\mathcal P_i\\e\in E(P)}}x_{i,P}\le 1
&&\text{for every edge }e,\\
&\sum_{P\in\mathcal P_i}x_{i,P}\le 1
&&\text{for every demand }i,\\
&x_{i,P}\ge 0.
\end{aligned}
\]
For unrestricted MaxIMF, omit the per-demand upper bounds. In the construction below, every terminal is a distinct degree-one vertex, so those upper bounds follow from edge capacities anyway.

**Theorem.** For every integer \(k\ge 1\), there is a simple undirected unit-capacity graph \(H_k\), with \(2k\) demand pairs, such that:

- \(H_k\) is subcubic and has \(4k^2+2k\) vertices;
- all terminals are distinct leaves on the outer face;
- \(H_k\) is \(k\)-outerplanar and has pathwidth at most \(2k\);
- the integer optimum is \(1\), for both MaxEDP and MaxIMF;
- the natural LP optimum is exactly \(k\).

Thus the integrality gap is exactly \(k\).

### Construction

Put \(r=2k\). In a rectangle, draw the \(r\) straight segments
\[
L_i:\quad s_i=(0,i)\longrightarrow t_i=(1,-i^2),
\qquad 1\le i\le r.
\]
The rectangle can be
\[
[0,1]\times[-r^2-1,r+1].
\]

The equation of \(L_i\) is
\[
y=i-i(i+1)x.
\]
For \(i\ne j\), the intersection of \(L_i\) and \(L_j\) is
\[
z_{ij}=
\left(\frac1{i+j+1},\frac{ij}{i+j+1}\right).
\]
Every pair intersects in the interior, and no three segments concur: concurrence of \(L_i,L_j,L_\ell\) would give \(i+j=i+\ell\).

Replace each crossing \(z_{ij}\) by the following planar gadget:

- the two portions entering from the left meet at a vertex \(u_{ij}\);
- the two portions leaving to the right meet at a vertex \(v_{ij}\);
- join \(u_{ij}\) to \(v_{ij}\) by one edge.

Perform these replacements in disjoint sufficiently small neighborhoods. The drawing remains strictly \(x\)-monotone along each original segment. The internal vertices can be chosen to have distinct \(x\)-coordinates.

Let \(P_i\) be the resulting \(s_i\)-\(t_i\) path. The graph is precisely
\[
H_k=\bigcup_{i=1}^r P_i.
\]

This also specifies the graph combinatorially: \(P_i\) visits the pairs
\[
u_{ij},v_{ij}
\]
in decreasing order of \(j\), omitting \(j=i\), with \(s_i\) first and \(t_i\) last. Take the union of the edges between consecutive vertices in these path descriptions.

Each internal vertex has degree three. Each central edge \(u_{ij}v_{ij}\) belongs to exactly \(P_i\) and \(P_j\), while every other edge belongs to exactly one prescribed path. No loops or parallel edges arise.

The vertex count is
\[
2r+2\binom r2=r^2+r=4k^2+2k.
\]

The terminal order around the rectangle is
\[
s_1,s_2,\ldots,s_r,t_1,t_2,\ldots,t_r.
\]

### Fractional optimum: exactly \(k\)

Assign flow \(1/2\) to every prescribed path \(P_i\). Every central edge has load \(1\), and every other edge has load \(1/2\). This is feasible and has value
\[
r/2=k.
\]

For the matching upper bound, consider the vertical line
\[
\ell:\quad x=\frac1{r+2}.
\]
Each segment \(L_i\) meets \(\ell\) at its crossing with
\[
L_{r+1-i}.
\]
Because \(r\) is even, these crossings pair up all \(r\) segments.

Choose the corresponding gadgets to straddle \(\ell\), and all other gadget neighborhoods to avoid \(\ell\). Then \(\ell\) crosses exactly the \(k\) central edges
\[
u_{i,r+1-i}v_{i,r+1-i},
\qquad 1\le i\le k.
\]
These edges form a cut separating every source from every sink. Every demand path crosses that cut, so any fractional multiflow has total value at most its capacity \(k\).

Consequently,
\[
\operatorname{OPT}_{\mathrm{LP}}(H_k)=k.
\]

### Integer optimum: exactly \(1\)

Suppose two demands could be routed by edge-disjoint simple paths.

Because all terminals are distinct leaves, neither path can use another terminal internally. If the paths shared an internal vertex, their edge-disjointness would require four distinct incident edges there. This is impossible in a subcubic graph. Thus the two paths would actually be vertex-disjoint.

For \(i<j\), however, their endpoints occur around the rectangle in the alternating order
\[
s_i,s_j,t_i,t_j.
\]
Two vertex-disjoint arcs inside a disk cannot join alternating boundary pairs. Indeed, an \(s_i\)-\(t_i\) arc separates the disk into two sides, with \(s_j\) and \(t_j\) on opposite sides.

Hence no two demands can be routed simultaneously. Since any one \(P_i\) is feasible,
\[
\operatorname{OPT}_{\mathrm{EDP}}(H_k)=1.
\]

For MaxIMF, the capacity-one terminal edges allow at most one unit for each commodity. An integral multiflow of value at least two would therefore give two edge-disjoint demand paths after deleting flow cycles. Thus
\[
\operatorname{OPT}_{\mathrm{IMF}}(H_k)=1
\]
as well.

### Pathwidth at most \(2k\)

Order the vertices by increasing \(x\)-coordinate, putting all sources first and all sinks last.

Each prescribed path is monotone in this order. Therefore every prefix of the ordering has at most \(r\) edges joining it to its complement: each crossing edge belongs to at least one prescribed path, and each prescribed path crosses the prefix cut at most once.

Write the ordering as \(w_1,\ldots,w_N\), and put
\[
F_j=\{w_i:i\le j,\ w_i\text{ has a neighbor among }w_{j+1},\ldots,w_N\}.
\]
Since every vertex of \(F_j\) is incident with a distinct prefix-cut edge,
\[
|F_j|\le r.
\]
The bags
\[
B_j=F_{j-1}\cup\{w_j\},\qquad 1\le j\le N,
\]
form a path decomposition: every edge is covered when its later endpoint is introduced, and every vertex occurs in consecutive bags. Their sizes are at most \(r+1\).

Thus
\[
\operatorname{pw}(H_k)\le r=2k,
\qquad
\operatorname{tw}(H_k)\le 2k.
\]

### \(k\)-outerplanarity

We use an elementary observation about outer-face peeling.

**Peeling observation.** If a vertex \(v\) of a plane graph can be connected to the unbounded face by a curve crossing at most \(q\) edge interiors and no other vertices, then \(v\) is deleted within \(q+1\) rounds of deleting all outer-face vertices.

To prove this, list the crossed edges from the exterior toward \(v\). The first crossed edge is incident with the outer face, so its endpoints disappear in the first round. The curve then reaches the second edge from the unbounded face of the remaining graph. Continuing inductively opens the entire curve after at most \(q\) rounds, exposing \(v\).

Now let \(v\) be an internal vertex of \(H_k\). Exactly two prescribed paths pass through \(v\). The vertical line through \(v\) contains no other graph vertex, and each of the remaining \(r-2\) prescribed paths meets it once. Consequently, the total number of graph-edge intersections above and below \(v\) is at most
\[
r-2=2k-2.
\]
One of the two vertical rays from \(v\) therefore crosses at most \(k-1\) edges. The peeling observation shows that \(v\) disappears within \(k\) rounds.

All terminals already lie on the outer face. Hence the displayed embedding is \(k\)-outerplanar. This completes the theorem. \(\square\)

## 3. A matching-order upper bound for a restricted class

The linear treewidth dependence above is not merely an artifact of the construction.

**Proposition.** On subcubic unit-capacity graphs whose terminals are leaves, the natural LP has integrality gap at most
\[
\frac32(r+1)
\]
when the graph has treewidth at most \(r\). Planarity is not required.

### Proof

Take a feasible fractional solution, represented by weighted simple paths. For each vertex \(v\), let
\[
\lambda(v)=\sum_{P\ni v}x_P.
\]
At a nonterminal vertex, every path containing \(v\) uses two incident edges. Hence
\[
2\lambda(v)\le \deg(v)\le 3.
\]
At a terminal leaf, \(\lambda(v)\le1\). Thus
\[
\lambda(v)\le\frac32
\quad\text{for every vertex }v.
\]

Root a width-\(r\) tree decomposition \((T,(B_t))\). For a graph path \(P\), define
\[
S_P=\{t\in V(T):B_t\cap V(P)\ne\varnothing\}.
\]
This is a connected subtree: the bags containing each graph vertex are connected, and adjacent vertices of \(P\) occur together in some bag. Let \(a(P)\) be the rootmost node of \(S_P\).

Repeatedly perform the following operation on the remaining fractional paths:

1. choose a path \(P\) for which \(a(P)\) has maximum depth;
2. select \(P\) integrally;
3. delete every remaining path that intersects \(P\) in a graph vertex.

The selected paths are vertex-disjoint, hence form a feasible EDP solution.

Consider a path \(Q\) deleted when \(P\) is selected. Because \(P\) and \(Q\) intersect, \(S_P\) and \(S_Q\) intersect. Their rootmost nodes are therefore comparable in the rooted tree. By the choice of \(P\), \(a(Q)\) is an ancestor of \(a(P)\), possibly equal to it. Connectivity of \(S_Q\) then gives
\[
a(P)\in S_Q.
\]
Thus every deleted path meets the bag \(B_{a(P)}\).

The total fractional weight deleted in this step is at most
\[
\sum_{v\in B_{a(P)}}\lambda(v)
\le \frac32(r+1).
\]
Charging each fractional path to the step that deletes it yields
\[
\operatorname{value}(\text{selected paths})
\ge
\frac{2}{3(r+1)}\operatorname{value}(\text{fractional solution}).
\]
This proves the proposition. \(\square\)

If \(\Gamma(r)\) denotes the worst LP gap on this subclass with treewidth at most \(r\), the construction with \(k=\lfloor r/2\rfloor\) gives, for \(r\ge2\),
\[
\left\lfloor\frac r2\right\rfloor
\le \Gamma(r)\le \frac32(r+1).
\]
Therefore
\[
\Gamma(r)=\Theta(r),
\]
with the lower bound already attained in planar graphs.

## 4. Consequences and remaining gap

### What is ruled out

There is no absolute constant \(C\) such that every natural-LP solution in every \(k\)-outerplanar graph can be rounded, without congestion, to a routing of value at least \(\operatorname{LP}/C\), independently of \(k\). The same holds independently of the treewidth bound.

The examples also have
\[
|V(H_k)|=4k^2+2k,
\]
so they exhibit an \(\Omega(\sqrt n)\) natural-LP gap in planar subcubic graphs.

Accordingly, any reading of the supplied literature review that asserts constant-fraction, congestion-one rounding of this LP on **all bounded-genus graphs** cannot be correct as stated. Genus zero already contains these counterexamples. I have not independently checked the precise cited theorem statements and do not claim a corrected version of them.

Congestion matters here: with congestion two, all \(2k\) prescribed paths \(P_i\) can be routed simultaneously.

### What is not ruled out

These examples do **not** establish approximation hardness. On these very instances, returning any one prescribed path is optimal.

They also do not refute a bound depending on a fixed parameter, such as \(f(k)\) or \(f(r)\): a gap of \(k\) is still constant when \(k\) is fixed.

Thus the rigorous conclusion is:

> The parameter-independent natural-LP integrality-gap assertion is false. The existence of an absolute-constant approximation relative to the integer optimum is not settled by this argument.