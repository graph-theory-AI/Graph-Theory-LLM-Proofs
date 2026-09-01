```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full characterisation remains open, but for the diamond (equivalently, under the usual convention, the three-edge dipole) the forbidden class is exactly the graphs whose blocks are cliques or chordless cycles, giving the sharp bound χ≤max{κ,3}, while known ISK4-free Burling graphs give a general necessary obstruction.",
  "would_publish": false,
  "caveats": "This treats induced subdivisions and one target exactly; the K4 obstruction uses an established external construction, and no general sufficiency characterisation is obtained."
}
```

# 1. Interpretation

Consistent with the source paper, write \(\mathsf P(H)\) for the property

\[
\forall \kappa\ \exists c=c(H,\kappa)\quad
\bigl(\omega(G)\leq \kappa,\ \chi(G)>c\bigr)
\Longrightarrow
G\text{ contains an induced subdivision of }H.
\]

Thus “\(H\)-subdivision-free” must mean *having no induced subgraph isomorphic to a subdivision of \(H\)*.

If ordinary, non-induced subdivisions were intended, the question would have the trivial answer “all finite \(H\)”: choose a fixed simple subdivision \(H'\) of \(H\), use the classical fact that sufficiently large average degree forces a subdivision of \(H'\), and pass to a chromatic-critical subgraph of minimum degree at least \(\chi(G)-1\). The clique-number hypothesis would then be unnecessary.

The full induced problem remains open. I give:

1. an exact structural and quantitative result for the smallest nontrivial banana with three branches; and  
2. a general necessary condition obtained from the known \(K_4\) counterexample.

# 2. Exact result for the diamond

Let \(D=K_4-e\), the diamond. Its two degree-three vertices are joined by three internally vertex-disjoint paths of lengths \(1,2,2\).

Call a graph a **theta** if it is the union of three internally vertex-disjoint paths \(P_1,P_2,P_3\) with common distinct ends \(a,b\). Here a path of length one is allowed, but in a simple graph at most one of the three paths can have length one. An **induced theta** is such a union with no additional edges among its vertices.

Every subdivision of \(D\) is a theta. Conversely, every theta is a subdivision of \(D\): at least two of its three paths have an internal vertex, which can serve as the two degree-two vertices of \(D\). Thus induced \(D\)-subdivisions and induced thetas are the same objects.

## Theorem 2.1

For a finite simple graph \(G\), the following are equivalent.

1. \(G\) contains no induced subdivision of \(D\).
2. \(G\) contains no induced theta.
3. Every block of \(G\) is either a complete graph or a chordless cycle.

Consequently, if \(\omega(G)\leq\kappa\) and \(G\) contains no induced subdivision of \(D\), then

\[
\chi(G)\leq \max\{\kappa,3\}.
\]

For every integer \(\kappa\geq2\), this is sharp:

\[
\max\{\chi(G):\omega(G)\leq\kappa,\ G\text{ is induced-}D
\text{-subdivision-free}\}
=
\max\{\kappa,3\}.
\]

For \(\kappa=1\), the sharp bound is \(1\).

## 2.1. Two elementary theta lemmas

### Lemma 2.2

Every 2-connected graph which is not a cycle contains a theta as a not necessarily induced subgraph.

#### Proof

Let \(B\) be 2-connected and let \(C\) be a cycle of \(B\).

If \(C\) has a chord, that chord and the two arcs of \(C\) between its ends form a theta.

Otherwise, if \(B\neq C\), let \(Q\) be a component of \(B-V(C)\). Since \(B\) is 2-connected, \(Q\) has at least two distinct neighbors on \(C\); otherwise its unique attachment would be a cutvertex. A path through \(Q\) joining two such attachments, together with the two corresponding arcs of \(C\), is a theta. ∎

### Lemma 2.3

If a graph contains a theta as a subgraph, then it contains either an induced theta or an induced \(K_4\).

#### Proof

Choose a theta \(T=P_1\cup P_2\cup P_3\) with common ends \(a,b\), minimizing

\[
|E(P_1)|+|E(P_2)|+|E(P_3)|.
\]

If \(G[V(T)]\) has no edge outside \(T\), then \(T\) is induced.

A chord with both ends on one \(P_i\) would shorten that path and produce a smaller theta. Hence every extra edge has ends in the interiors of two distinct paths, say \(x\in P_i\) and \(y\in P_j\).

Write

\[
\begin{aligned}
p&=|E(P_i[a,x])|,&p'&=|E(P_i[x,b])|,\\
q&=|E(P_j[a,y])|,&q'&=|E(P_j[y,b])|,
\end{aligned}
\]

and let \(r=|E(P_k)|\), where \(k\notin\{i,j\}\).

Using the edge \(xy\), there is a theta with ends \(a,x\) and total path length

\[
p+(q+1)+(r+p')=p+p'+q+r+1.
\]

The original total is \(p+p'+q+q'+r\). Minimality therefore gives \(q'=1\). Applying the analogous construction with ends \(b,x\) gives \(q=1\). By symmetry, \(p=p'=1\).

Thus \(P_i=a-x-b\) and \(P_j=a-y-b\). On the four vertices \(\{a,b,x,y\}\), all edges except possibly \(ab\) are present:

\[
ax,xb,ay,yb,xy\in E(G).
\]

If \(ab\notin E(G)\), these four vertices induce a diamond, which is itself an induced theta with ends \(x,y\). If \(ab\in E(G)\), they induce \(K_4\). ∎

## 2.2. Structure of induced-theta-free blocks

### Lemma 2.4

Every 2-connected induced-theta-free graph is either a complete graph or a chordless cycle.

#### Proof

Let \(B\) be 2-connected and induced-theta-free. If \(B\) is a cycle, there is nothing to prove. Otherwise, Lemmas 2.2 and 2.3 imply that \(B\) contains a \(K_4\).

Let \(K\) be a maximal clique of \(B\) containing this \(K_4\). Suppose \(K\neq V(B)\).

First observe that every vertex \(v\in V(B)\setminus K\) has at most one neighbor in \(K\). Indeed, if \(v\) has two neighbors \(x,y\in K\), maximality of \(K\) gives a vertex \(z\in K\) nonadjacent to \(v\). Then \(\{v,x,y,z\}\) induces a diamond: \(x,y,z\) form a triangle, and \(v\) is adjacent precisely to \(x,y\) among them. This is an induced theta, a contradiction.

Let \(Q\) be a component of \(B-K\). Since \(B\) is 2-connected, \(Q\) has at least two distinct neighbors in \(K\). Choose a shortest path

\[
P=v_0v_1\cdots v_\ell
\]

whose distinct ends \(v_0,v_\ell\) belong to \(K\) and whose internal vertices lie outside \(K\). The preceding observation gives \(\ell\geq3\).

By minimality, \(P\) is induced. Choose

\[
c\in K\setminus\{v_0,v_\ell\},
\]

which is possible because \(|K|\geq4\). No internal vertex of \(P\) is adjacent to \(c\). Otherwise, if \(c v_i\in E(G)\) and \(i\leq\ell-2\), then

\[
v_0v_1\cdots v_i c
\]

would be a shorter path with distinct ends in \(K\) and interior outside \(K\). If \(i=\ell-1\), then \(v_i\) would have the two distinct neighbors \(c,v_\ell\) in \(K\), contrary to the preceding observation.

It follows that the induced subgraph on \(V(P)\cup\{c\}\) consists exactly of the three \(v_0\)-\(v_\ell\) paths

\[
v_0v_\ell,\qquad v_0cv_\ell,\qquad P.
\]

This is an induced theta, again a contradiction. Hence \(K=V(B)\), and \(B\) is complete. ∎

## 2.3. Completion of Theorem 2.1

If \(G\) is induced-theta-free, Lemma 2.4 shows that every block with at least three vertices is a clique or a chordless cycle; bridges are \(K_2\)'s.

Conversely, suppose every block of \(G\) is a clique or a chordless cycle. A theta is 2-connected, so every theta subgraph lies in a single block. No induced subgraph of a clique is a theta, and a cycle has maximum degree two and hence contains no theta. Thus \(G\) is induced-theta-free.

Finally, a graph assembled along cutvertices can be colored block by block. A clique block needs at most \(\omega(G)\) colors, and a cycle block needs at most three. Permuting the colors in each new block makes its cutvertex agree with the already colored part. Therefore

\[
\chi(G)\leq \max\{\omega(G),3\}.
\]

Sharpness follows from:

- \(C_5\), for \(\kappa=2\);
- \(K_\kappa\), for every \(\kappa\geq3\).

Both have only cycle or clique blocks and therefore contain no induced theta. ∎

### Remark 2.5: the first three dipoles

Under the usual subdivision convention, let \(M_r\) be the multigraph consisting of two vertices joined by \(r\) parallel edges.

- \(M_1\)-subdivision-free graphs are edgeless.
- \(M_2\)-subdivision-free graphs are forests: every graph containing a cycle contains a shortest, hence induced, cycle.
- \(M_3\)-subdivision-free graphs are precisely those described in Theorem 2.1; equivalently one may use the simple target \(D=K_4-e\).

Thus the first three single-banana cases admit exact structure and exact chromatic bounds.

# 3. A general necessary obstruction

The following established counterexample theorem is part of the background to Scott's induced-subdivision conjecture:

> For every \(t\), there is a triangle-free graph \(B_t\) with  
> \(\chi(B_t)>t\) and with no induced subdivision of \(K_4\).

This is the ISK4-free high-chromatic construction obtained from the Pawlik/Burling graphs; the relevant structural result appears in Chalopin–Esperet–Li–Ossona de Mendez, *Restricted frame graphs and a conjecture of Scott*. I use this as an external known theorem rather than reprove the construction.

There is a useful transfer principle.

## Proposition 3.1

Let \(F\) be an induced subgraph of \(H\). If \(\mathsf P(H)\) holds, then \(\mathsf P(F)\) holds.

#### Proof

Every induced subdivision \(S\) of \(H\) contains an induced subdivision of \(F\): retain the branch vertices corresponding to \(V(F)\), together with all subdivided edge-paths corresponding to edges of \(F\). Since \(F\) is induced in \(H\), no omitted edge of \(H\) has both ends among the retained branch vertices, and hence the retained subgraph is induced in \(S\).

Therefore every \(F\)-subdivision-free graph is also \(H\)-subdivision-free. Any chromatic bound for the latter class applies to the former. ∎

## Corollary 3.2

If \(H\) contains, as an induced subgraph, a subdivision of \(K_4\), then \(\mathsf P(H)\) fails, already for \(\kappa=2\).

#### Proof

Let \(F\) be the induced subdivision of \(K_4\) in \(H\). Every subdivision of \(F\) is also a subdivision of \(K_4\). Hence each graph \(B_t\) above is \(F\)-subdivision-free. Proposition 3.1 then shows that \(B_t\) is \(H\)-subdivision-free. Since \(\omega(B_t)=2\) and \(\chi(B_t)\) is unbounded, \(\mathsf P(H)\) fails. ∎

In particular, for a simple graph \(H\),

\[
\mathsf P(H)\quad\Longrightarrow\quad \omega(H)\leq3,
\]

because any four pairwise adjacent vertices induce a \(K_4\).

The word “induced” in Proposition 3.1 is essential. Ordinary subgraph or topological-minor containment is insufficient: an induced \(K_4\) does not contain an induced diamond, even though the diamond is obtained by deleting an edge from \(K_4\).

# 4. What remains open

Theorem 2.1 is a complete and sharp answer only for the diamond/three-branch banana. Qualitative pervasiveness of this target is already subsumed by the banana-tree theorem in the source paper; the additional point here is the exact host-graph structure and sharp linear bound.

Corollary 3.2 gives a general necessary condition, but it is far from sufficient. For example, even small graphs with no induced subdivision of \(K_4\), such as a diamond with a pendant edge attached at one of its degree-two vertices, are not decided by the arguments above.

The minimal-theta proof also does not extend directly to four or more parallel branches. Chords in a minimal four-branch configuration may leave only an induced three-branch theta or a clique; neither is forbidden when the target has four branches. Thus a new structural or recursive argument would be required.

Accordingly, no full characterisation of the multigraphs \(H\) satisfying \(\mathsf P(H)\) is obtained here.