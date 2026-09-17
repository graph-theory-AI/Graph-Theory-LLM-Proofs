```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A verified k-outerplanar construction has natural path-LP gap k, and the gap remains unbounded after any fixed number of Sherali–Adams rounds.",
  "would_publish": false,
  "caveats": "This concerns relaxation gaps, not approximation hardness; it does not settle the algorithmic question or verify the current literature status."
}
```

# 1. Scope of the result

There are two different questions here:

1. Is there a constant-factor polynomial-time approximation **relative to the integer optimum**?
2. Does the natural multicommodity-flow LP have a constant integrality gap, permitting constant-factor rounding without congestion?

A negative answer to the second does not imply a negative answer to the first.

I checked the crossing-gadget construction in the previous attempt. It is valid for undirected graphs, and I give a complete proof below. I also strengthen its conclusion:

> Even after adding valid vertex-capacity inequalities, any fixed number of Sherali–Adams rounds applied to the natural **path formulation** still has an unbounded integrality gap on \(k\)-outerplanar graphs as \(k\) grows.

This rules out more than rounding the unstrengthened LP, but still does not establish approximation hardness.

All capacities below are one. Every terminal is a distinct leaf. Consequently, each commodity can carry at most one unit, so MaxEDP and unrestricted MaxIMF coincide on these instances.

## The relaxation

For commodity \(i\), let \(\mathcal P_i\) be its set of simple terminal-to-terminal paths. The natural path LP is
\[
\begin{aligned}
\max\quad &\sum_i\sum_{P\in\mathcal P_i}x_{i,P},\\
\text{subject to}\quad
&\sum_i\sum_{\substack{P\in\mathcal P_i\\e\in E(P)}}x_{i,P}\le 1
&& (e\in E),\\
&\sum_{P\in\mathcal P_i}x_{i,P}\le 1
&& (i\text{ a commodity}),\\
&x_{i,P}\ge 0.
\end{aligned}
\tag{LP}
\]
The per-commodity inequalities are redundant when its terminal has an incident capacity-one leaf edge.

On a subcubic graph with distinct leaf terminals, every integral routing is also vertex-disjoint. Thus the following are valid additional inequalities:
\[
\sum_i\sum_{\substack{P\in\mathcal P_i\\v\in V(P)}}x_{i,P}\le 1
\qquad(v\in V).
\tag{VC}
\]
These inequalities are not valid for general EDP instances; their validity here uses the stated degree and terminal restrictions.

# 2. An explicit planar obstruction

## Theorem 1

For every integer \(k\ge1\), there is a simple undirected unit-capacity instance \(H_k\) with \(2k\) commodities such that:

- \(H_k\) has maximum degree three and \(4k^2+2k\) vertices;
- its terminals are distinct leaves on the outer face;
- it has a \(k\)-outerplanar embedding;
- \(\operatorname{pw}(H_k)\le 2k\), and hence \(\operatorname{tw}(H_k)\le2k\);
- its integer optimum is \(1\), for both MaxEDP and MaxIMF;
- its optimum in (LP) is exactly \(k\), even after adding (VC).

In particular, its integrality gap is exactly \(k\).

## Construction

Write \(r=2k\). In the rectangle
\[
[0,1]\times[-r^2-1,r+1],
\]
draw the segments
\[
L_i:\ s_i=(0,i)\longrightarrow t_i=(1,-i^2),
\qquad 1\le i\le r.
\]
Their equations are
\[
y=i-i(i+1)x.
\]
For \(i\ne j\), their unique intersection is
\[
z_{ij}=
\left(\frac1{i+j+1},\frac{ij}{i+j+1}\right).
\]
Every pair intersects in the interior. No three segments concur: concurrence involving \(L_i,L_j,L_\ell\) would imply
\(i+j=i+\ell\).

Replace every crossing \(z_{ij}\), inside a sufficiently small disjoint neighborhood, by this planar gadget:

- the two incoming portions from the left meet at \(u_{ij}\);
- the two outgoing portions to the right meet at \(v_{ij}\);
- one edge joins \(u_{ij}\) to \(v_{ij}\).

The replacement can preserve strict \(x\)-monotonicity along each original segment. Choose all internal vertices to have distinct \(x\)-coordinates.

Let \(P_i\) be the resulting \(s_i\)-\(t_i\) path, and set
\[
H_k=\bigcup_{i=1}^{r}P_i.
\]

For completeness, the graph also has the following purely combinatorial specification. Interpret \(u_{ij}=u_{ji}\) and \(v_{ij}=v_{ji}\). Along \(P_i\), list
\[
s_i,\ u_{ij_1},v_{ij_1},\
u_{ij_2},v_{ij_2},\ldots,\
u_{ij_{r-1}},v_{ij_{r-1}},\ t_i,
\]
where
\[
j_1>j_2>\cdots>j_{r-1}
\]
lists \(\{1,\ldots,r\}\setminus\{i\}\). The edge set is the union of consecutive pairs in these lists.

Each internal vertex has degree three. Each central edge \(u_{ij}v_{ij}\) belongs to exactly \(P_i\) and \(P_j\); every other edge belongs to exactly one prescribed path. The lists produce no loops or parallel edges.

The number of vertices is
\[
2r+2\binom r2=r^2+r=4k^2+2k.
\]

The cyclic terminal order on the rectangle boundary is
\[
s_1,s_2,\ldots,s_r,t_1,t_2,\ldots,t_r.
\tag{1}
\]

## Integer optimum

Suppose two different commodities could be routed by edge-disjoint simple paths.

Their endpoints are distinct leaves, so neither path can use an endpoint of the other internally. If they shared any internal vertex, edge-disjointness would require four distinct incident edges there. This is impossible in a subcubic graph. Therefore the two paths would be vertex-disjoint.

For \(i<j\), however, (1) puts their endpoints in alternating cyclic order:
\[
s_i,s_j,t_i,t_j.
\]
Two disjoint arcs in a disk cannot join alternating boundary pairs. Indeed, an \(s_i\)-\(t_i\) arc, together with an appropriate boundary arc, separates \(s_j\) from \(t_j\).

Thus at most one commodity can be routed. Any prescribed path \(P_i\) routes one, giving
\[
\operatorname{OPT}_{\mathrm{EDP}}(H_k)=1.
\]

For MaxIMF, every commodity has a capacity-one terminal edge. An integral multiflow of value at least two would, after deleting flow cycles and decomposing into paths, give two edge-disjoint demand paths. Hence
\[
\operatorname{OPT}_{\mathrm{IMF}}(H_k)=1.
\tag{2}
\]

## Fractional optimum

Assign \(x_{i,P_i}=1/2\), and set all other path variables to zero. Every central edge has load one, and every other edge has load \(1/2\). This is feasible and has value
\[
r/2=k.
\tag{3}
\]
It also satisfies (VC): each internal vertex belongs to exactly two prescribed paths, and each terminal belongs to one.

For the reverse inequality, consider
\[
\ell:\quad x=\frac1{r+2}.
\]
Each \(L_i\) meets this line at its crossing with \(L_{r+1-i}\). Because \(r\) is even, these crossings pair up all \(r\) segments.

Choose their gadgets to straddle \(\ell\), with only the central edges crossing it, and choose every other gadget neighborhood to avoid \(\ell\). Then \(\ell\) crosses exactly the \(k\) edges
\[
u_{i,r+1-i}v_{i,r+1-i},
\qquad 1\le i\le k.
\]
These form an edge cut separating every source from every sink. Every demand path uses at least one cut edge, so any feasible fractional multiflow has total value at most \(k\).

Together with (3),
\[
\operatorname{OPT}_{\mathrm{LP}}(H_k)
=
\operatorname{OPT}_{\mathrm{LP+(VC)}}(H_k)
=k.
\tag{4}
\]

## Pathwidth bound

Order all vertices by increasing \(x\)-coordinate, putting all sources first and all sinks last. Every prescribed path is monotone in this order.

Every prefix cut has at most \(r\) edges: each cut edge belongs to a prescribed path, and each prescribed path crosses a prefix cut at most once.

Write the ordering as \(w_1,\ldots,w_N\), and define
\[
F_j=\{w_i:i\le j,\ w_i\text{ has a neighbor among }
w_{j+1},\ldots,w_N\}.
\]
Each vertex of \(F_j\) can be assigned a distinct prefix-cut edge, so
\[
|F_j|\le r.
\]
The bags
\[
B_j=F_{j-1}\cup\{w_j\}
\]
form a path decomposition. Every edge is covered when its later endpoint is introduced, and each vertex occurs in consecutive bags. Therefore
\[
\operatorname{pw}(H_k)\le r=2k.
\tag{5}
\]

The treewidth is genuinely unbounded. In fact,
\[
\operatorname{tw}(H_k)\ge k-1.
\tag{6}
\]
To see this, take any tree decomposition. The bags meeting a connected path \(P_i\) induce a subtree of its decomposition tree. These \(r\) subtrees pairwise intersect, because \(P_i\) and \(P_j\) share a central edge. By the Helly property for subtrees of a tree, some bag meets every \(P_i\). Each graph vertex belongs to at most two prescribed paths, so that bag has at least \(r/2=k\) vertices.

## Outerplanarity bound

We use the following elementary observation.

**Peeling lemma.** Suppose a vertex \(v\) of a plane graph can be joined to the unbounded face by a curve crossing at most \(q\) edge interiors and no other vertices. Then \(v\) is removed within \(q+1\) rounds of deleting all vertices incident with the unbounded face.

**Proof.** List the crossed edges from the exterior toward \(v\). The first is incident with the unbounded face, so its endpoints disappear in the first round. If the next crossed edge remains, it is then accessible from the unbounded face along the initial part of the curve, so its endpoints disappear in the next round. Continuing, after at most \(q\) rounds either \(v\) has already disappeared or the whole curve is open and exposes \(v\). \(\square\)

Now let \(v\) be an internal vertex of \(H_k\). Exactly two prescribed paths pass through \(v\). The vertical line through \(v\) contains no other graph vertex, and each of the remaining \(r-2\) prescribed paths meets it once.

Consequently, the total number of edge crossings on the two vertical rays from \(v\) is at most
\[
r-2=2k-2.
\]
One ray therefore crosses at most \(k-1\) edges. The peeling lemma removes \(v\) within \(k\) rounds. All terminals are already incident with the outer face.

Thus the displayed embedding is \(k\)-outerplanar, completing the theorem. \(\square\)

# 3. Fixed-depth Sherali–Adams also fails

The preceding example has a particularly simple fractional support:

- there are \(r=2k\) prescribed path variables;
- each capacity row contains at most two of them;
- globally, at most one can be chosen integrally.

This yields a hierarchy lower bound.

## Theorem 2

Apply Sherali–Adams to the \(0\)-\(1\) path formulation of (LP), optionally including (VC).

Use the convention that level \(t=0\) is the original LP, and level \(t\) includes every base inequality multiplied by
\[
\prod_{a\in A}x_a\prod_{b\in B}(1-x_b),
\qquad
A\cap B=\varnothing,\quad |A|+|B|\le t,
\]
followed by multilinearization.

For \(0\le t\le 2k-2\),
\[
\operatorname{OPT}_{\mathrm{SA}_t}(H_k)
\ge \frac{2k}{t+2}.
\tag{7}
\]
Since the integer optimum is one, this is also an integrality-gap lower bound.

In particular, every fixed number of rounds still has gap \(\Omega(k)\).

## Proof

Write \(z_i=x_{i,P_i}\) for the \(r\) prescribed path variables. Fix every other path variable to zero. Put
\[
p=\frac1{t+2}.
\]

Define lifted moments by
\[
y_{\varnothing}=1,\qquad y_{\{z_i\}}=p,
\]
and set every moment containing either

- a non-prescribed path variable, or
- two or more distinct prescribed path variables

equal to zero.

We verify all lifted inequalities using consistent local distributions.

For any set \(W\) of at most \(t+2\) prescribed variables, define a distribution \(D_W\) as follows:

- for each \(z_i\in W\), select the assignment with \(z_i=1\) and every other variable in \(W\) zero, with probability \(p\);
- select the all-zero assignment with the remaining probability
  \[
  1-|W|p\ge0.
  \]

These distributions are consistent under marginalization and induce exactly the moments above.

After fixing the non-prescribed variables to zero, every base row depends on at most two prescribed variables:

- an edge-capacity row contains at most two;
- a commodity row contains one;
- a vertex-capacity row in (VC) contains at most two;
- variable bounds contain at most one.

Every such row is satisfied by every assignment selecting at most one prescribed variable.

Consider a lifted inequality. Its multiplier involves at most \(t\) variables, and its base row involves at most two prescribed variables. After fixing the other variables to zero, the entire expression therefore depends on a set \(W\) of at most \(t+2\) prescribed variables.

On every assignment in the support of \(D_W\), both the base inequality and its multiplier are nonnegative. Their expected product is consequently nonnegative. By consistency, this expectation is precisely the corresponding lifted linear expression in the proposed moments.

Thus all Sherali–Adams inequalities are satisfied. The objective value is
\[
\sum_{i=1}^{r}y_{\{z_i\}}
=rp
=\frac{2k}{t+2}.
\]
This proves (7). \(\square\)

### Formulation caveat

Hierarchy levels depend on the formulation. The theorem concerns the explicitly defined **path-variable formulation**, including the indicated vertex strengthening. It does not assert the same behavior for every compact flow formulation, every stronger relaxation, or a semidefinite hierarchy.

It also does not rule out a number of rounds growing with \(k\).

# 4. A matching-order upper bound in the subcubic case

There is also a self-contained positive result for the restricted class used above.

## Proposition 3

Let \(G\) be a unit-capacity graph of maximum degree three, with all terminals distinct leaves, and suppose \(\operatorname{tw}(G)\le r\). Then
\[
\frac{\operatorname{OPT}_{\mathrm{LP}}(G)}
     {\operatorname{OPT}_{\mathrm{integer}}(G)}
\le \frac32(r+1).
\tag{8}
\]
If (VC) is included, the upper bound improves to \(r+1\).

The proof provides explicit rounding when a tree decomposition and a finite fractional path solution are supplied.

## Proof

Take a feasible fractional solution and define its vertex load by
\[
\lambda(v)=\sum_{i,P:\,v\in V(P)}x_{i,P}.
\]

At a nonterminal vertex, every path containing \(v\) uses two incident edges. Hence
\[
2\lambda(v)
=\sum_{e\ni v}\operatorname{load}(e)
\le \deg(v)\le3.
\]
At a terminal leaf, \(\lambda(v)\le1\). Thus
\[
\lambda(v)\le\frac32
\qquad(v\in V).
\tag{9}
\]
With (VC), we instead have \(\lambda(v)\le1\).

Root a width-\(r\) tree decomposition \((T,(B_a)_{a\in V(T)})\). For each fractional path \(P\), put
\[
S_P=\{a:B_a\cap V(P)\ne\varnothing\}.
\]
This is a connected subtree: bags containing one vertex form a subtree, and the subtrees for consecutive vertices of \(P\) intersect in a bag containing their edge.

Let \(a(P)\) be the rootmost node of \(S_P\). Repeat:

1. Choose a remaining path \(P\) whose \(a(P)\) has maximum depth.
2. Select \(P\) integrally.
3. Delete every remaining path meeting \(P\) in a graph vertex.

The selected paths are vertex-disjoint. They also represent distinct commodities, since two paths for the same commodity share their terminal leaves.

Suppose \(Q\) is deleted when \(P\) is chosen. The subtrees \(S_P\) and \(S_Q\) intersect. Their rootmost nodes are therefore comparable, and the choice of \(P\) makes \(a(Q)\) an ancestor of \(a(P)\). Connectivity then implies
\[
a(P)\in S_Q.
\]
Thus every path deleted at this step meets \(B_{a(P)}\).

The fractional weight deleted at the step is at most
\[
\sum_{v\in B_{a(P)}}\lambda(v)
\le \frac32(r+1).
\]
Charging each fractional path to its deletion step gives
\[
\operatorname{value}(\text{fractional solution})
\le \frac32(r+1)\,
   \operatorname{number}(\text{selected paths}),
\]
proving (8). Using \(\lambda(v)\le1\) gives \(r+1\) for the vertex-strengthened LP. \(\square\)

Consequently, if \(\Gamma(r)\) is the worst natural-LP gap on this subcubic, leaf-terminal class with treewidth at most \(r\), then, for \(r\ge2\),
\[
\left\lfloor\frac r2\right\rfloor
\le \Gamma(r)\le\frac32(r+1).
\]
Therefore
\[
\boxed{\Gamma(r)=\Theta(r).}
\tag{10}
\]
The lower bound already holds in planar graphs.

Combining Theorem 2 with the same upper bound shows that, for every fixed \(t\), the worst level-\(t\) Sherali–Adams gap on this class is also \(\Theta(r)\), with constants allowed to depend on \(t\).

# 5. Consequences and the unresolved part

## What is established

The parameter-independent natural-LP assertion is false:

- no absolute constant bounds its integrality gap over all \(k\)-outerplanar graphs as \(k\) varies;
- no absolute constant bounds it independently of treewidth;
- adding the valid vertex-capacity inequalities above does not fix this;
- any fixed number of Sherali–Adams rounds on the path formulation still does not fix it.

Since
\[
|V(H_k)|=4k^2+2k,
\]
the examples also give an \(\Omega(\sqrt n)\) gap in planar subcubic graphs.

## What is not established

These examples do **not** exclude a constant-factor approximation relative to the integer optimum. On \(H_k\), returning any prescribed path is optimal.

They also do not refute a guarantee \(f(k)\) or \(f(r)\) that is constant when the relevant parameter is fixed. Thus the interpretation of “constant” in the original question matters.

Finally, I have not independently verified the cited theorem statements. The supplied literature summary, if interpreted as asserting a uniform constant natural-LP gap with congestion one on all planar graphs, is incompatible with Theorem 1. This identifies a problem with that interpretation of the summary, not necessarily with any cited paper. Congestion is important: all \(2k\) prescribed paths in this construction can be routed simultaneously with congestion two.

**Conclusion.** The previous construction survives checking, and its obstruction extends to fixed-depth Sherali–Adams strengthening. This is a rigorous negative answer to the parameter-independent **LP-gap** version and a linear-gap characterization for a restricted bounded-treewidth class. The algorithmic approximation question is not resolved by this argument, and no novelty claim is made.