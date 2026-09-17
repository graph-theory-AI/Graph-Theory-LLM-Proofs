```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds with polynomial delay and polynomial space whenever H is an induced subgraph of two cliques joined by a perfect matching.",
  "would_publish": false,
  "caveats": "H-freeness is induced; this covers only a proper subclass of co-bipartite H, and novelty of the special case is not claimed."
}
```

# 1. An unconditional special case

Throughout, graphs are finite and simple, and \(H\)-free means induced-\(H\)-free.

Define \(J_t\) to have vertex set
\[
A=\{a_1,\ldots,a_t\},\qquad B=\{b_1,\ldots,b_t\},
\]
where \(A\) and \(B\) are cliques and the edges between them are exactly
\[
a_i b_i,\qquad 1\le i\le t.
\]
Thus \(J_2=C_4\), and \(J_3\) is the triangular prism.

The positive result proved below is the following.

**Theorem 1.** For every fixed \(t\ge 1\), minimal dominating sets of \(J_t\)-free incomparability graphs can be enumerated with \(n^{O(t)}\) delay and \(n^{O(t)}\) space.

Consequently, the conjecture holds whenever the fixed forbidden graph \(H\) has a partition into two cliques such that the edges between the parts form a matching. Either clique is allowed to be empty.

Indeed, every such \(H\) is an induced subgraph of some \(J_t\). To construct an embedding, assign the same index to the endpoints of each cross-edge, and assign distinct unused indices to all remaining vertices. If \(H\) has \(h\) vertices and \(m\) cross-edges, \(t=h-m\) suffices. An \(H\)-free graph is then necessarily \(J_t\)-free.

This includes, for example, every forbidden graph \(K_p\mathbin{\dot\cup}K_q\), as well as the graphs \(J_t\) themselves.

I set aside the earlier attempt’s bounded-VC reformulation: no transversal-enumeration conjecture is assumed here. The proof instead uses a cut parameter and a self-contained enumeration algorithm. At the end, I also prove an NP-completeness result explaining a limitation of extending the same search oracle to the whole conjectured class.

# 2. A structural bound from the forbidden graph

For a partition \(V(G)=L\mathbin{\dot\cup}R\), let
\[
\mu_G(L,R)
\]
be the maximum size of an induced matching in the bipartite graph consisting of the edges of \(G\) between \(L\) and \(R\). Edges within either part are discarded when computing this parameter.

**Lemma 2.** Let \(G\) be the incomparability graph of a poset \(P\), and let
\[
v_1,\ldots,v_n
\]
be any linear extension of \(P\). If \(G\) is \(J_t\)-free, then every prefix cut
\[
L_i=\{v_1,\ldots,v_i\},\qquad R_i=V(G)\setminus L_i
\]
satisfies
\[
\mu_G(L_i,R_i)\le t-1.
\]

**Proof.** Suppose a cut has an induced matching of size \(t\), with edges
\[
x_jy_j,\qquad x_j\in L_i,\quad y_j\in R_i,\quad 1\le j\le t.
\]
For distinct \(j,\ell\), the absence of the cross-edge \(x_jy_\ell\) means that these vertices are comparable in \(P\). Their positions in the linear extension force
\[
x_j<_P y_\ell. \tag{1}
\]

The vertices \(x_1,\ldots,x_t\) form an antichain. Otherwise, say \(x_j<_P x_\ell\), equation (1) gives
\[
x_j<_P x_\ell<_P y_j,
\]
contradicting \(x_jy_j\in E(G)\). Likewise, the vertices \(y_1,\ldots,y_t\) form an antichain: if \(y_j<_P y_\ell\), then
\[
x_\ell<_P y_j<_P y_\ell,
\]
again contradicting a matching edge.

Thus the \(x\)-vertices form a clique in \(G\), as do the \(y\)-vertices. Between these cliques there are exactly the matching edges. They induce \(J_t\), a contradiction. ∎

A poset representation can be obtained in polynomial time by transitively orienting \(\overline G\), using the standard polynomial-time transitive-orientation algorithm for comparability graphs. Thus the required linear extension is available from a graph-only input.

The remaining task is algorithmic: enumerate minimal dominating sets when all cuts of a supplied ordering have bounded \(\mu_G\).

# 3. Enumeration under a bounded cut-induced-matching parameter

We prove the following general statement.

**Proposition 3.** Suppose a graph \(G\) is supplied with an ordering whose prefix cuts all satisfy \(\mu_G(L_i,R_i)\le k\). Then minimal dominating sets of \(G\) can be enumerated with \(n^{O(k+1)}\) delay and \(n^{O(k+1)}\) space.

The proof has three ingredients:

1. bounded cut matchings give polynomially many truncated neighborhood profiles;
2. minimal domination admits a local encoding using two vertex sets;
3. these profiles support a polynomial-time extension oracle and hence enumeration.

## 3.1. Small representatives for truncated neighborhood profiles

Let \(B\) be a bipartite graph with sides \(L,R\). For \(S\subseteq L\) and an integer \(r\ge1\), define the profile
\[
\sigma_r(S)(v)=\min\{r,|N_B(v)\cap S|\},\qquad v\in R.
\]

**Lemma 4.** If the maximum induced matching size of \(B\) is at most \(k\), every profile \(\sigma_r(S)\) has a representative \(S'\subseteq S\) of size at most
\[
(2r-1)k.
\]

**Proof.** Choose an inclusion-minimal \(S'\subseteq S\) having the same profile as \(S\). For each \(x\in S'\), deleting \(x\) changes a coordinate of the profile. Hence there is a vertex \(y_x\in R\) such that
\[
x\in N_B(y_x),\qquad 1\le |N_B(y_x)\cap S'|\le r. \tag{2}
\]

Construct an auxiliary graph \(F\) on \(S'\). For each \(x\), join \(x\) to every other vertex of \(N_B(y_x)\cap S'\). Regard these as edges generated by \(x\). Each vertex generates at most \(r-1\) edges. Consequently, for every \(U\subseteq S'\),
\[
|E(F[U])|\le (r-1)|U|.
\]
Thus \(F\) is \((2r-2)\)-degenerate and is colorable with \(2r-1\) colors. It has an independent set \(I\) of size at least
\[
\frac{|S'|}{2r-1}.
\]

For distinct \(x,x'\in I\), independence gives
\[
x'\notin N_B(y_x),\qquad x\notin N_B(y_{x'}).
\]
In particular, the vertices \(y_x\), \(x\in I\), are distinct, and the edges \(xy_x\) form an induced matching in \(B\). Therefore
\[
\frac{|S'|}{2r-1}\le |I|\le k.
\]
This proves the bound. ∎

It follows that all profiles can be generated by enumerating subsets of size at most \((2r-1)k\) and removing duplicate vectors. Their number is at most
\[
\sum_{j=0}^{(2r-1)k}\binom nj.
\tag{3}
\]
For fixed \(k,r\), this takes polynomial time and space. The same conclusion holds with \(L\) and \(R\) interchanged.

We will use only \(r=2\) and \(r=1\).

## 3.2. A local encoding of minimal domination

A dominating set \(D\) is inclusion-minimal if and only if every \(d\in D\) has a private vertex: some \(w\) satisfying
\[
N_G[w]\cap D=\{d\}. \tag{4}
\]

Introduce a second vertex set
\[
W=\{w:|N_G[w]\cap D|=1\}.
\]
For each vertex \(v\), write
\[
\delta_v=\mathbf 1_{v\in D},\qquad
\omega_v=\mathbf 1_{v\in W},
\]
and define
\[
c_D(v)=\min\{2,|N_G[v]\cap D|\},\qquad
c_W(v)=\min\{1,|N_G[v]\cap W|\}.
\]

The pair \((D,W)\) encodes a minimal dominating set exactly when the following local conditions hold at every vertex:
\[
\begin{aligned}
&c_D(v)\ge1,\\
&\omega_v=1\quad\Longleftrightarrow\quad c_D(v)=1,\\
&\delta_v=1\quad\Longrightarrow\quad c_W(v)=1.
\end{aligned}
\tag{5}
\]

The first condition is domination. The second defines \(W\). For \(d\in D\), the third supplies a vertex \(w\in N_G[d]\cap W\); symmetry of adjacency and the definition of \(W\) then give (4). Conversely, private vertices imply the third condition.

Importantly, \(W\) is uniquely determined by \(D\).

## 3.3. A polynomial-time extension oracle

We now decide the following problem under the layout hypothesis of Proposition 3:

> Given disjoint sets \(I,O\subseteq V(G)\), does there exist a minimal dominating set \(D\) such that
> \[
> I\subseteq D,\qquad D\cap O=\varnothing?
> \tag{6}
> \]

At cut \((L_i,R_i)\), a state consists of four profiles:
\[
(\alpha_D,\alpha_W,\beta_D,\beta_W).
\]
They represent, respectively:

- counts into \(R_i\) from \(D\cap L_i\), capped at \(2\);
- counts into \(R_i\) from \(W\cap L_i\), capped at \(1\);
- counts into \(L_i\) from \(D\cap R_i\), capped at \(2\);
- counts into \(L_i\) from \(W\cap R_i\), capped at \(1\).

The possible profiles in each coordinate are generated using Lemma 4. By (3), the number of states at a cut is
\[
n^{8k+O(1)}.
\tag{7}
\]
We may include all combinations of the four profiles. Consistency between the coordinates will be enforced by a complete path through the dynamic program.

Here are the transitions explicitly. Suppose the next vertex is
\[
v=v_{i+1},
\]
and choose its two labels
\[
\delta=\mathbf1_{v\in D},\qquad \omega=\mathbf1_{v\in W}.
\]
The choice of \(\delta\) must respect (6).

Write
\[
r_D=2,\quad r_W=1,\qquad \epsilon_D=\delta,\quad\epsilon_W=\omega.
\]
A state at cut \(i\) and a primed state at cut \(i+1\) are connected by this labeled transition if, for \(X\in\{D,W\}\),
\[
\alpha'_X(w)
=\min\{r_X,\alpha_X(w)+\epsilon_X\mathbf1_{vw\in E(G)}\},
\qquad w\in R_{i+1},
\tag{8}
\]
and
\[
\beta_X(u)
=\min\{r_X,\beta'_X(u)+\epsilon_X\mathbf1_{uv\in E(G)}\},
\qquad u\in L_i.
\tag{9}
\]
Finally, calculate
\[
c_X(v)=
\min\{r_X,\alpha_X(v)+\beta'_X(v)+\epsilon_X\},
\qquad X\in\{D,W\},
\tag{10}
\]
and require the three conditions in (5).

Notice that these rules only add nonnegative contributions and truncate. They never attempt to subtract from a saturated count.

There is a unique initial state: its left-to-right profiles are zero vectors and its right-to-left profiles have empty domain. There is similarly a unique final state, with empty-domain left-to-right profiles and zero right-to-left profiles. The oracle asks whether the resulting layered directed graph has a path from the initial state to the final state.

### Correctness

Any minimal dominating set satisfying (6), together with its uniquely determined \(W\), gives its actual profiles at every cut. These satisfy (8)–(10), so they define an accepting path.

Conversely, take an accepting path and read its vertex labels to obtain sets \(D,W\). Forward induction using (8) shows that every \(\alpha\)-profile on the path is the actual profile of the labeled prefix. Backward induction from the final zero profiles using (9) shows that every \(\beta\)-profile is the actual profile of the labeled suffix. Equation (10) therefore gives the actual truncated closed-neighborhood counts at each processed vertex. The local conditions (5) hold everywhere, so \(D\) is a minimal dominating set satisfying (6).

Thus the oracle is exact.

### Complexity

All profile lists have polynomial size for fixed \(k\). By (7), even testing every pair of states in consecutive layers and all four label choices takes \(n^{O(k+1)}\) time and space. This is deliberately a crude bound; no optimization is needed for the claimed result.

## 3.4. Enumeration

Perform depth-first search on the binary decisions
\[
v_i\in D\quad\text{or}\quad v_i\notin D.
\]
Before entering a child, invoke the extension oracle for the resulting forced-in and forced-out sets. Prune a child if the answer is negative.

Every unpruned node has an output descendant. Each minimal dominating set appears at exactly one leaf. Between consecutive output leaves, depth-first search makes only \(O(n)\) oracle calls, including unsuccessful child tests. The same bound applies before the first output and after the last output.

The delay and space are therefore \(n^{O(k+1)}\), proving Proposition 3. The empty graph can be handled separately by outputting its unique minimal dominating set, \(\varnothing\).

Combining Proposition 3 with Lemma 2, using \(k=t-1\), proves Theorem 1.

# 4. A further rigorous limitation: extension is NP-complete inside the conjectured class

The preceding algorithm uses an arbitrary-membership extension oracle. Such an oracle cannot simply be assumed available for all the classes in the conjecture.

**Theorem 5.** Fix
\[
H_0=\overline{C_{10}}.
\]
The following decision problem is NP-complete, even when the input graph is a co-bipartite, \(H_0\)-free incomparability graph:

> Given \(G\) and \(I\subseteq V(G)\), does some minimal dominating set of \(G\) contain \(I\)?

This is an extension-problem result, **not** a hardness result for output-polynomial enumeration.

## 4.1. From satisfiability to extending a minimal vertex cover

Start with a 3-CNF formula. Add unused variables if necessary so that it has at least three variables.

Construct a graph \(F\) with:

- literal vertices \(p_i,n_i\) for each variable;
- a selector vertex \(s_i\) for each variable;
- a clause vertex \(c_j\) for each clause.

Add the edges
\[
p_in_i,\qquad s_ip_i,\qquad s_in_i
\]
for each variable. Join \(c_j\) to the literal vertices appearing in its clause. There are no other edges.

Put
\[
I=\{s_i\}_i\cup\{c_j\}_j.
\]
In particular, \(|I|\ge3\).

A maximal independent set avoiding \(I\) must contain exactly one of \(p_i,n_i\) for every variable: independence forbids both, while maximality requires domination of \(s_i\). Maximality at each \(c_j\) says that at least one selected literal satisfies its clause.

Conversely, a satisfying assignment gives a maximal independent set avoiding \(I\): select its true literal for every variable. Unselected literal vertices are dominated by their selected partners, selectors are dominated, and clauses are dominated.

Since complements of maximal independent sets are exactly minimal vertex covers, we have proved
\[
\text{the formula is satisfiable}
\quad\Longleftrightarrow\quad
F\text{ has a minimal vertex cover containing }I.
\tag{11}
\]

## 4.2. The two-clique encoding, checked directly

Let \(X=V(F)\). Construct \(G_F\) with two cliques
\[
C=X\cup\{z\},\qquad
R=\{r_e:e\in E(F)\}.
\]
For \(x\in X\), put
\[
xr_e\in E(G_F)\quad\Longleftrightarrow\quad x\in e.
\]
The vertex \(z\) has no neighbor in \(R\).

This is the two-clique encoding appearing in the supplied attempt; the properties needed here are verified below.

First, \(G_F\) is an incomparability graph: take \(C\) and \(R\) as antichains and declare
\[
c<r_e\quad\Longleftrightarrow\quad cr_e\notin E(G_F).
\]
This defines a height-two poset.

Next:

1. Minimal dominating sets contained in \(C\) are exactly minimal vertex covers of \(F\), viewed as subsets of \(X\).
2. No dominating set is contained entirely in \(R\), because such a set cannot dominate \(z\).
3. Every minimal dominating set meeting both cliques has size two, since any one vertex from each clique already dominates the whole graph.

For item 1, a set \(D\subseteq C\) dominates \(R\) exactly when \(D\cap X\) is a vertex cover of \(F\). The graph \(F\) has edges, so such a cover is nonempty and also dominates \(C\). The vertex \(z\) is redundant whenever it belongs to such a dominating set. Inclusion-minimality is therefore exactly minimality as a vertex cover.

Since \(|I|\ge3\), a minimal dominating set containing \(I\) cannot be a mixed two-vertex set. Consequently,
\[
G_F\text{ has a minimal dominating set containing }I
\quad\Longleftrightarrow\quad
F\text{ has a minimal vertex cover containing }I.
\tag{12}
\]

## 4.3. Why the constructed graphs exclude \(\overline{C_{10}}\)

The complement \(\overline{G_F}\) is bipartite with sides \(C,R\).

Suppose \(G_F\) contained an induced \(H_0=\overline{C_{10}}\). Its complement would give an induced \(C_{10}\) in \(\overline{G_F}\). Because \(C_{10}\) is connected, its bipartition must align with \(C,R\), up to swapping. There would therefore be five selected vertices in each part.

In \(H_0\), every vertex has exactly three neighbors across this five-by-five partition: it is adjacent to all opposite-side vertices except its two cycle neighbors. But every vertex \(r_e\in R\) has only two neighbors in all of \(C\) in \(G_F\). This is impossible.

Thus every \(G_F\) is \(H_0\)-free.

Equations (11) and (12) prove NP-hardness. Membership in NP follows by checking domination and checking that deleting any selected vertex destroys domination. This completes the proof of Theorem 5.

The result shows that a polynomial-time arbitrary-membership extension oracle is a genuinely stronger requirement than the desired enumeration algorithm. It does not contradict the conjecture: enumerating all minimal dominating sets need not decide extension in polynomial input time.

# 5. What remains missing

The positive theorem covers exactly the forbidden graphs that embed in some \(J_t\), not all co-bipartite graphs.

There is a concrete reason the width argument does not automatically extend. Let \(H\) be the diamond \(K_4-e\). Every \(J_s\) is diamond-free: every triangle lies inside one of its two cliques, and a fourth vertex has either three neighbors or at most one neighbor in that triangle, never exactly two.

On the other hand, consider the height-two poset representing \(J_s\):
\[
a_i<b_j\quad\Longleftrightarrow\quad i\ne j.
\]
In any linear extension, immediately before the first \(b_j\) appears, at least \(s-1\) of the \(a_i\)'s have already appeared. Their matching partners all remain on the other side of the cut. Hence that cut has an induced matching of size at least \(s-1\).

Thus even a fixed co-bipartite forbidden graph can allow unbounded cut parameters along these poset layouts. This is a limitation of the sufficient condition proved here, not evidence against the conjecture.

The established progress is therefore:

- an unconditional polynomial-delay, polynomial-space algorithm for a uniform infinite family of forbidden co-bipartite graphs;
- an explicit NP-completeness result for unrestricted extension in another fixed co-bipartite-forbidden subclass.

No output-polynomial algorithm for arbitrary co-bipartite \(H\), and no counterexample to the original conjecture, is established here.