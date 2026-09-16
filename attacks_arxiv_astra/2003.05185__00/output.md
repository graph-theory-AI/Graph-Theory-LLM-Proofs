```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a combinatorial MWIS algorithm for graphs with a supplied parity-consistent boundary and logarithmic-size remaining components, but not for all perfect graphs.",
  "would_publish": false,
  "caveats": "The boundary must be supplied; no novelty or improvement over the cited partial results is claimed."
}
```

## Scope of the result

I do not obtain a combinatorial polynomial-time algorithm for arbitrary perfect graphs.

The partial result below develops the even-set/submodular-minimization approach. It gives:

1. an exact characterization of when a boundary-extension function is supermodular after complementing some coordinates;
2. a reduction to **ordinary, finite-valued combinatorial submodular minimization**;
3. a fully implemented polynomial-time special case, with no residual MWIS oracle left unresolved.

The result applies to arbitrary graphs satisfying the additional hypotheses, not just perfect graphs. I do not claim that the structural reduction is new.

Weights are nonnegative integers encoded in binary. Negative-weight vertices can be deleted, and rational weights can be scaled to integers using a common denominator of polynomial encoding length.

## 1. An exact parity criterion

Let \(G\) be a finite simple graph, and let \(S\subseteq V(G)\).

An **induced \(S\)-path** is an induced path with distinct endpoints in \(S\) and all internal vertices outside \(S\). In particular, an edge of \(G[S]\) is an induced \(S\)-path.

Call a map
\[
\sigma:S\longrightarrow\{0,1\}
\]
**parity-consistent** if every induced \(S\)-path \(P\), with endpoints \(s,t\), satisfies
\[
|E(P)|\equiv \sigma(s)+\sigma(t)\pmod 2. \tag{1}
\]

Write \(S_i=\sigma^{-1}(i)\). For \(U\subseteq S\), define
\[
A_\sigma(U)=(U\cap S_0)\cup(S_1\setminus U).
\]
Thus coordinates in \(S_1\) are complemented.

For a nonnegative weight function \(w\), define
\[
\Phi_w(U)=
\max\{w(I): I\text{ is independent in }G,\ I\cap S=A_\sigma(U)\},
\tag{2}
\]
with value \(-\infty\) if no such independent set exists.

### Theorem 1

For fixed \(G,S,\sigma\), the following are equivalent:

1. \(\sigma\) is parity-consistent.
2. For every nonnegative integer weight function \(w\), the function \(\Phi_w\) is supermodular:
   \[
   \Phi_w(U)+\Phi_w(V)
   \le
   \Phi_w(U\cup V)+\Phi_w(U\cap V)
   \qquad(U,V\subseteq S).
   \tag{3}
   \]

Here sums involving \(-\infty\) have their usual extended-real meaning. If condition 1 fails, condition 2 has a witness using only weights \(0\) and \(1\).

When \(\sigma\) is constantly zero, condition 1 says precisely that \(S\) is an even set. Indeed, it forces \(S\) to be independent, and induced paths with additional vertices of \(S\) can be split into induced \(S\)-paths.

### Proof: parity implies supermodularity

Fix \(U,V\subseteq S\). If either term on the left of (3) is \(-\infty\), the inequality is immediate. Otherwise choose optimal independent sets \(I,J\) in (2) for \(U,V\), respectively.

The graph
\[
H=G[I\triangle J]
\]
is bipartite, with sides \(I\setminus J\) and \(J\setminus I\).

Consider a connected component \(C\) of \(H\), and boundary vertices \(s,t\in C\cap S\). A shortest \(s\)-\(t\) path in \(H\) is induced in \(G\). Split this path at its vertices in \(S\). Each resulting segment is an induced \(S\)-path. By (1), summing their parities gives
\[
\text{length of the path}\equiv \sigma(s)+\sigma(t)\pmod 2.
\]
Consequently, within \(C\),

- boundary vertices having equal \(\sigma\)-values lie on the same bipartition side;
- boundary vertices having different \(\sigma\)-values lie on opposite sides.

We can therefore orient the two sides of every component \(C\) so that one chosen side contains all of \(C\cap S_0\), and the other contains all of \(C\cap S_1\). If \(C\cap S=\varnothing\), choose either orientation.

Let \(K\) consist of the first chosen side from every component, together with \(I\cap J\). Let \(L\) consist of the other sides, again together with \(I\cap J\).

Both \(K\) and \(L\) are independent. In particular, a vertex of \(I\cap J\) has no neighbor in \(I\triangle J\). Every vertex has the same total multiplicity in \(I,J\) as in \(K,L\), so
\[
w(K)+w(L)=w(I)+w(J). \tag{4}
\]

On \(S_0\), all changing boundary choices go into \(K\); on \(S_1\), they go into \(L\). The unchanged choices belong to both sets or neither. Hence
\[
K\cap S=A_\sigma(U\cup V),
\qquad
L\cap S=A_\sigma(U\cap V).
\]
Using (4),
\[
\Phi_w(U\cup V)+\Phi_w(U\cap V)
\ge w(K)+w(L)
=\Phi_w(U)+\Phi_w(V).
\]
This proves supermodularity.

### Proof: a parity violation gives a weight witness

First suppose an edge \(st\in E(G[S])\) has \(\sigma(s)=\sigma(t)\). Freeze all other boundary vertices to be unselected. The assignments selecting only \(s\) and only \(t\) are feasible, but one of their coordinatewise union and intersection selects both. With all weights zero, the left side of (3) is finite and the right side is \(-\infty\). Thus (3) fails.

Now suppose an induced \(S\)-path
\[
P=s=v_0,v_1,\ldots,v_m=t,\qquad m\ge2,
\]
violates (1). Its endpoints are nonadjacent.

Give weight \(1\) to \(v_1,\ldots,v_{m-1}\), and weight \(0\) to every other vertex. Freeze all boundary vertices other than \(s,t\) to be unselected. Let \(F(B)\) be the optimum when exactly \(B\subseteq\{s,t\}\) is selected from \(S\).

Only the internal vertices of \(P\) contribute weight. Since \(P\) is induced, selecting an endpoint removes just the corresponding end vertex of this internal path. Directly,
\[
\begin{array}{c|cccc}
m & F(\varnothing)&F(\{s\})&F(\{t\})&F(\{s,t\})\\ \hline
2k   & k & k-1 & k-1 & k-1\\
2k+1 & k & k   & k   & k-1
\end{array}
\qquad(k\ge1).
\]
The first row also covers \(m=2\), when both endpoints forbid the same internal vertex.

Therefore
\[
\Delta:=
F(\varnothing)+F(\{s,t\})-F(\{s\})-F(\{t\})
=(-1)^m. \tag{5}
\]

Complementing either endpoint coordinate reverses the sign of this four-term difference. More explicitly, put
\[
B_0=S_1\setminus\{s,t\}.
\]
Then
\[
\begin{aligned}
&\Phi_w(B_0)+\Phi_w(B_0\cup\{s,t\})\\
&\qquad-\Phi_w(B_0\cup\{s\})-\Phi_w(B_0\cup\{t\})
=(-1)^{\sigma(s)+\sigma(t)}\Delta.
\end{aligned}
\]
Because \(P\) violates (1), this quantity is \(-1\). Supermodularity requires it to be nonnegative. This proves the converse. \(\square\)

## 2. Turning the criterion into an ordinary submodular minimization

The values \(-\infty\) in (2) should not be hidden inside a standard finite-valued oracle. The following construction removes them explicitly.

Assume \(\sigma\) is parity-consistent. Applying (1) to edges shows that \(G[S]\) is bipartite with sides \(S_0,S_1\).

A set \(A_\sigma(U)\) is independent exactly when
\[
x\in U\Longrightarrow y\in U
\quad
\text{for every }xy\in E(G[S]),\ x\in S_0,\ y\in S_1.
\tag{6}
\]
Let \(\mathcal D\) be the family of sets satisfying (6). It is closed under union and intersection.

Define the closure
\[
c(U)=U\cup\bigl(N_G(U\cap S_0)\cap S_1\bigr).
\tag{7}
\]
This is the smallest member of \(\mathcal D\) containing \(U\), and
\[
c(U\cup V)=c(U)\cup c(V).
\tag{8}
\]

On \(\mathcal D\), let
\[
f(U)=-\Phi_w(U).
\]
Theorem 1 says that \(f\) is submodular on this lattice. If
\[
W=\sum_{v\in V(G)}w(v),
\]
then
\[
-W\le f(U)\le0\qquad(U\in\mathcal D).
\tag{9}
\]

Define, on all subsets of \(S\),
\[
\widehat f(U)
=
f(c(U))+(W+1)\bigl(|c(U)|-|U|\bigr).
\tag{10}
\]

### Lemma 2

The function \(\widehat f\) is finite-valued and submodular. Every minimizer belongs to \(\mathcal D\), and
\[
\min_{U\subseteq S}\widehat f(U)=-\alpha_w(G).
\tag{11}
\]

### Proof

For \(U,V\subseteq S\), put
\[
R=c(U)\cap c(V),\qquad T=c(U\cap V).
\]
Both sets are in \(\mathcal D\), and \(T\subseteq R\).

Using submodularity of \(f\), identity (8), and modularity of cardinality, we obtain
\[
\begin{aligned}
&\widehat f(U)+\widehat f(V)
-\widehat f(U\cup V)-\widehat f(U\cap V)\\
&\qquad\ge
f(R)-f(T)+(W+1)(|R|-|T|).
\end{aligned}
\tag{12}
\]
If \(R=T\), the right side is zero. Otherwise, (9) shows that it is at least
\[
-W+(W+1)=1.
\]
Thus \(\widehat f\) is submodular.

If \(U\notin\mathcal D\), then \(|c(U)|-|U|\ge1\), so
\[
\widehat f(U)\ge-W+(W+1)=1.
\]
But \(\varnothing\in\mathcal D\) and \(\widehat f(\varnothing)\le0\). Hence every minimizer is in \(\mathcal D\).

Finally, the map \(U\mapsto A_\sigma(U)\) bijects \(\mathcal D\) with the independent subsets of \(S\). Maximizing over all possible traces of an independent set on \(S\) gives
\[
\max_{U\in\mathcal D}\Phi_w(U)=\alpha_w(G),
\]
proving (11). \(\square\)

### The value oracle

For \(U\in\mathcal D\), put \(A=A_\sigma(U)\). If \(\mathcal C\) is the set of components of \(G-S\), then
\[
\Phi_w(U)
=
w(A)+
\sum_{C\in\mathcal C}
\alpha_w\!\left(G[C\setminus N_G(A)]\right).
\tag{13}
\]

Thus a value oracle for \(\widehat f\) uses MWIS only on induced subgraphs of the individual components of \(G-S\).

The standard combinatorial value-oracle algorithm for submodular-function minimization now applies to (10). This is the only non-elementary algorithmic primitive used here; no ellipsoid or linear-programming oracle is involved.

After finding a minimizing \(U\), recover the independent set by taking \(A_\sigma(U)\) and an optimum from each summand in (13).

## 3. A fully implemented special case

The preceding reduction becomes an unconditional algorithm when the remaining components are small.

### Theorem 3

Let \(G,w,S\) be given, with \(S\) supplied as part of the input. Let
\[
r=\max\{|C|:C\text{ is a component of }G-S\},
\]
taking \(r=0\) when \(S=V(G)\).

In time
\[
2^r n^{O(1)}\operatorname{poly}(L),
\tag{14}
\]
where \(L\) is the binary encoding length of the weights, one can:

- determine whether a parity-consistent map \(\sigma:S\to\{0,1\}\) exists;
- if one exists, find a maximum-weight independent set of \(G\).

Consequently, for every fixed \(c\), this is a combinatorial polynomial-time algorithm on certified instances satisfying
\[
r\le c\log_2(n+1)
\]
and admitting a parity-consistent map.

The theorem does **not** assert a polynomial-time algorithm for finding a suitable \(S\).

### Proof and algorithm

#### Step 1: find or reject the parity labeling

For every edge \(st\in E(G[S])\), impose
\[
\sigma(s)\oplus\sigma(t)=1.
\]

Next, for every component \(C\) of \(G-S\), every pair \(s,t\in S\), and every nonempty subset \(R\subseteq C\), test whether
\[
G[R\cup\{s,t\}]
\]
is a path with endpoints \(s,t\). This test uses connectivity and the vertex degrees in the induced graph.

Whenever it is such a path, impose
\[
\sigma(s)\oplus\sigma(t)\equiv |R|+1\pmod2. \tag{15}
\]

Every induced \(S\)-path of length at least two is tested: its internal vertices lie in one component of \(G-S\). Edges were handled separately. Hence the resulting system is equivalent to parity consistency.

These are pairwise XOR constraints, solvable by graph traversal. The enumeration takes at most
\[
O\!\left(n^3\,2^r(r+2)^2\right)
\]
time. If the constraints are inconsistent, the supplied boundary does not satisfy the theorem’s hypothesis.

#### Step 2: implement the residual MWIS calls

For each component \(C\), enumerate its vertex subsets, retaining the independent ones and their weights.

For any boundary choice \(A\), the required value
\[
\alpha_w(G[C\setminus N_G(A)])
\]
is obtained by scanning these subsets and taking the heaviest one disjoint from \(N_G(A)\).

Thus each evaluation of (13), and hence of (10), takes
\[
2^r n^{O(1)}\operatorname{poly}(L)
\]
time.

#### Step 3: minimize and reconstruct

Apply a combinatorial submodular-minimization algorithm to \(\widehat f\). It makes polynomially many oracle calls and performs polynomially many additional operations.

All oracle values have polynomial encoding length: they are formed from sums of input weights and the penalty \(W+1\). There is no expansion proportional to the numerical magnitudes of the weights.

Lemma 2 gives the optimum value, and (13) reconstructs an optimum independent set. This proves (14). \(\square\)

This avoids enumerating \(2^{|S|}\) boundary assignments. The boundary may contain almost all vertices.

## 4. Why perfection alone does not supply the missing condition

There is already an obstruction on a small chordal perfect graph.

Let \(G\) be the path
\[
s-a-b-t
\]
together with a vertex \(z\) adjacent to all four path vertices. Take
\[
S=\{s,t\}.
\]

The graph is perfect: every induced subgraph avoiding \(z\) is an induced subgraph of a path; adding the universal vertex \(z\) increases both its chromatic number and clique number by one.

But there are two induced \(S\)-paths:
\[
s-z-t \quad\text{of length }2,
\qquad
s-a-b-t \quad\text{of length }3.
\]
The first forces \(\sigma(s)=\sigma(t)\), while the second forces the opposite. Thus this boundary admits no parity-consistent labeling.

By Theorem 1, no fixed complementation of these two boundary coordinates makes the extension function supermodular for all nonnegative weights. So “the graph is perfect” cannot replace the parity hypothesis, even on this elementary example.

Moreover, the logarithmic-component special case is genuinely restricted. In \(K_n\), parity consistency forces \(G[S]\) to be bipartite, so \(|S|\le2\). The remaining component then has at least \(n-2\) vertices. Large cliques therefore do not satisfy that corollary, although their MWIS problem is of course trivial.

## Conclusion and remaining gap

The proved partial result is an exact parity criterion for submodular boundary optimization, together with a combinatorial algorithm for supplied boundaries whose remaining components have logarithmic size.

It does not provide:

- an appropriate boundary for an arbitrary perfect graph;
- a more general decomposition covering all perfect graphs;
- or a different combinatorial mechanism for the unrestricted case.

Thus it is not a solution, nor a counterexample, to the requested open problem. The general combinatorial polynomial-time MWIS algorithm remains unresolved by this argument.