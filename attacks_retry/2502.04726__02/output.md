```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For spanning-path activity, exact computation is NP-hard even with a supplied optimal lollipop and only constantly many active vertices, while the number of chords gives an exact fixed-parameter algorithm.",
  "would_publish": false,
  "caveats": "The supplied excerpts omit the source definition of activity; the hardness result is not a result about rotation reachability, and 'simple' is not a formal running-time requirement."
}
```

# 1. Scope and results

The difficulty of **finding** an optimal lollipop does not, by itself, establish the difficulty of computing activity once the lollipop is supplied. These are different algorithmic problems.

I examine the following explicit definition. For a graph \(H\) and a specified root \(\rho\), put
\[
A(H,\rho)=
\{x\in V(H)\setminus\{\rho\}:
H\text{ has a Hamiltonian path from }\rho\text{ to }x\}.
\]
For a lollipop with cycle \(C\) and attachment vertex \(\rho\), **spanning-path activity** means membership in
\[
A(G[V(C)],\rho).
\]

The supplied excerpts do not give the source's definition of “active.” I therefore do not silently identify this definition with one based on reachability under rotations. The distinction matters.

Here are the results proved below.

> **Theorem 1.** Given a graph \(H\), an explicitly supplied Hamiltonian cycle, and vertices \(\rho,\tau\), deciding whether \(\tau\in A(H,\rho)\) is NP-complete.
>
> For every fixed integer \(k\ge 2\), NP-hardness already occurs on instances satisfying
> \[
> \delta(H)=k,
> \qquad
> |A(H,\rho)|\in\{3k-2,\,5k-3\}.
> \]
> Moreover, distinguishing these two possible cardinalities is NP-hard.

Thus the difficulty persists when the entire answer has **bounded size**, not merely when many active paths might exist.

> **Theorem 2.** These instances can be embedded as the cycles of explicitly supplied lollipops in graphs of minimum degree \(k\). Each supplied lollipop covers the entire graph, and its cycle is a longest cycle of the graph.

Consequently, the lollipops are optimal under the maximum-coverage-then-maximum-cycle convention, or with these two priorities reversed.

> **Theorem 3.** Suppose \(H\) has an explicitly supplied Hamiltonian cycle \(C\) of length \(m\), with \(q\) chords. Then \(A(H,\rho)\) can be computed in
> \[
> O\!\left(2^q(q+1)(m+q)\right)
> \]
> time and \(O(m+q)\) working space.
>
> Furthermore, all rooted Hamiltonian paths can be enumerated in \(2^{O(q)}m^{O(1)}\) time. Hence activity defined by reachability under specified endpoint rotations also admits a \(2^{O(q)}m^{O(1)}\)-time algorithm.

The first proof checks and strengthens the directed scaffold construction from the previous attempt.

# 2. A directed scaffold with only two possible terminal vertices

We start with directed Hamiltonian \(s\)-\(t\) path, restricted so that \(s\) has indegree zero and \(t\) has outdegree zero.

This restricted problem is NP-complete. Indeed, from an undirected Hamiltonian-cycle instance, choose a vertex \(z\), replace the other edges by both orientations, and replace \(z\) by a source \(s\) and a sink \(t\). For each former edge \(zy\), add \(s\to y\) and \(y\to t\). Collapsing \(s,t\) back to \(z\) proves the required equivalence.

Let \(D\) be such a directed instance, with
\[
V(D)=\{v_1,\ldots,v_n\}.
\]
Construct a digraph \(B\) with vertices \(a_v,c_v,b_v\) for each \(v\in V(D)\). Its arcs are:

* the four internal arcs
  \[
  a_v\to c_v,\quad c_v\to b_v,\quad
  b_v\to c_v,\quad c_v\to a_v;
  \]
* \(b_v\to a_w\) for every arc \(v\to w\) of \(D\);
* the scaffold arcs
  \[
  a_{v_i}\to b_{v_{i+1}},
  \]
  with indices modulo \(n\).

There is an explicitly known directed Hamiltonian cycle
\[
b_{v_1},c_{v_1},a_{v_1},
b_{v_2},c_{v_2},a_{v_2},
\ldots,
b_{v_n},c_{v_n},a_{v_n},
b_{v_1}.                                             \tag{1}
\]

Let \(E_B\) be the set of possible last vertices of directed Hamiltonian paths in \(B\) starting at \(a_s\).

> **Lemma 4.**
> \[
> E_B=
> \begin{cases}
> \{c_s\},&\text{if \(D\) has no Hamiltonian \(s\)-\(t\) path},\\[2mm]
> \{c_s,b_t\},&\text{if \(D\) has a Hamiltonian \(s\)-\(t\) path}.
> \end{cases}                                         \tag{2}
> \]

### Proof

Consider a directed Hamiltonian path starting at \(a_s\).

If its endpoint is not one of the vertices \(c_v\), every \(c_v\) is internal. Its predecessor and successor must then be \(a_v,b_v\), in some order. Consequently every block is traversed consecutively, either as
\[
a_v,c_v,b_v
\quad\text{or as}\quad
b_v,c_v,a_v.
\]
The first block is necessarily \(a_s,c_s,b_s\). After a forward block, the only unused external successor is \(a_w\), where \(v\to w\) is an arc of \(D\). Thus every block is forward, and contracting the blocks gives a Hamiltonian path of \(D\) starting at \(s\).

Since \(t\) has outdegree zero, this path must end at \(t\). Therefore the only possible endpoint of this type is \(b_t\), and it is possible exactly when \(D\) has a Hamiltonian \(s\)-\(t\) path.

Now suppose the endpoint is \(c_v\). All blocks other than the \(v\)-block are forced to be consecutive.

If \(v\ne s\), the path begins with forward blocks. Its first encounter with the \(v\)-block must be at \(a_v\). It cannot proceed to \(c_v\), since that would finish before visiting \(b_v\). It must therefore use
\[
a_v\to b_{\operatorname{next}(v)}.
\]
Thereafter all encountered blocks are reverse blocks, and the scaffold forces them to follow the cyclic enumeration until reaching \(b_v\). This traversal encounters every other block, including the already used \(s\)-block—a contradiction.

If \(v=s\), there is exactly the scaffold path obtained from (1) by starting at \(a_s\) and ending at \(c_s\). This proves (2). \(\square\)

# 3. A minimum-degree blow-up and its exact endpoint set

The following lemma gives more information than the usual directed-to-undirected Hamiltonicity reduction.

Let \(B\) be a loopless digraph with at least two vertices, with root \(z_0\). Write
\[
E(B,z_0)=
\{w:B\text{ has a directed Hamiltonian }z_0\text{-}w\text{ path}\}.
\]

Fix \(k\ge2\). For each \(z\in V(B)\), create a clique
\[
K_z=\{z^-,z^+\}\cup W_z,
\qquad |W_z|=k-1.
\]
Only the two ports \(z^-,z^+\) have neighbors outside this clique. For each arc \(z\to w\) of \(B\), add the undirected edge
\[
z^+w^-.
\]
Call the resulting graph \(U_k(B)\), rooted at \(z_0^-\).

Every private vertex in \(W_z\) has degree \(k\), and every port has degree at least \(k\). Thus
\[
\delta(U_k(B))=k.
\]
Also, a known directed Hamiltonian cycle of \(B\) immediately gives a known Hamiltonian cycle of \(U_k(B)\): replace each \(z\) by any spanning \(z^-\)-\(z^+\) path through \(K_z\).

For a set \(S\subseteq V(B)\), let \(N_B^+(S)\) denote its out-neighborhood.

> **Lemma 5.** Setting \(E=E(B,z_0)\), we have
> \[
> A(U_k(B),z_0^-)
> =
> \{w^+:w\in E\}
> \;\cup\!
> \bigcup_{z\in E\cup N_B^+(E)} W_z.                    \tag{3}
> \]

### Proof

We first consider Hamiltonian paths whose two endpoints are ports.

Every private vertex has both of its path neighbors inside its own clique. In the restriction of the path to \(K_z\), a component containing a private vertex must therefore have its two ends at the ports. There cannot be another component containing private vertices, since its ends would also have to be those same ports. A cycle component is impossible because the whole graph under consideration is a path.

Thus each \(K_z\) is traversed consecutively, from one port to the other. Starting at \(z_0^-\) forces the first traversal to end at \(z_0^+\). Every subsequent external edge then enters a minus-port, so every clique is traversed in the same forward orientation. Contracting the cliques gives a directed Hamiltonian path in \(B\) starting at \(z_0\).

This proves that the possible port endpoints are precisely
\[
\{w^+:w\in E\}.                                      \tag{4}
\]
A path with both global endpoints in \(K_{z_0}\) cannot be an exception: the forced spanning traversal of that clique would already contain both endpoints, leaving no room for the other cliques.

Now let a Hamiltonian path end at a private vertex \(x\in W_z\). Every other clique is again traversed consecutively. There are two possibilities for its restriction to \(K_z\).

**Case 1: \(K_z\) is a single terminal segment.**  
This requires \(z\ne z_0\). The segment is entered at \(z^-\). Since \(K_z\) is a clique, we may reorder this final segment so that it ends at \(z^+\). By (4), \(z\in E\).

Conversely, if \(z\in E\), a path ending at \(z^+\) can have its final clique reordered to end at any prescribed vertex of \(W_z\).

**Case 2: One port is isolated in the restriction to \(K_z\), while all remaining vertices of \(K_z\) form the terminal segment ending at \(x\).**  
These are the only remaining possibilities: private vertices other than \(x\) have degree two in the restricted path, so any additional component would need unavailable port endpoints.

The isolated port is \(z^-\). For \(z\ne z_0\), this follows from the forward orientation before the first encounter with \(K_z\). For \(z=z_0\), the path must leave the root port immediately and return to the clique at its other port.

Let the vertex immediately following this isolated \(z^-\) be \(w^+\). Thus \(w\to z\) is an arc of \(B\). Because \(x\) is adjacent to \(z^-\), rotate the path at \(z^-\): replace the suffix following \(z^-\) by its reversal, preceded by the old endpoint \(x\). The resulting Hamiltonian path ends at \(w^+\), and every clique is now consecutive. By (4), \(w\in E\). Hence \(z\in N_B^+(E)\).

Conversely, if \(w\in E\) and \(w\to z\), take an expanded directed Hamiltonian path ending at \(w^+\). Order the \(z\)-clique so that \(x\) immediately follows \(z^-\). Rotating at \(z^-\), using \(w^+z^-\), produces a path ending at \(x\).

This proves (3). \(\square\)

The rotation in this proof starts from an **arbitrary existing Hamiltonian path**. It does not establish reachability from the supplied cycle.

# 4. Hardness with a bounded-size answer

Apply Lemma 5 to the digraph \(B\) of Section 2, rooted at \(a_s\). Put
\[
H=U_k(B),\qquad \rho=(a_s)^-,\qquad \tau=(b_t)^+.
\]
The known cycle (1) provides an explicitly known Hamiltonian cycle of \(H\).

Because \(t\) has no outgoing arcs in \(D\),
\[
N_B^+(c_s)=\{a_s,b_s\},
\qquad
N_B^+(b_t)=\{c_t\}.
\]
Define the two disjoint, explicitly known sets
\[
A_0=
\{(c_s)^+\}\cup W_{c_s}\cup W_{a_s}\cup W_{b_s}
\]
and
\[
A_1=
\{(b_t)^+\}\cup W_{b_t}\cup W_{c_t}.
\]
Equations (2) and (3) give
\[
A(H,\rho)=
\begin{cases}
A_0,&\text{if the source instance is negative},\\
A_0\cup A_1,&\text{if the source instance is positive}.
\end{cases}                                         \tag{5}
\]

In particular,
\[
|A_0|=3k-2,\qquad |A_1|=2k-1.
\]
Thus the active-set cardinality is either \(3k-2\) or \(5k-3\), and
\[
\tau\in A(H,\rho)
\iff
D\text{ has a Hamiltonian }s\text{-}t\text{ path}.
\]

All constructions have polynomial size for fixed \(k\). Membership of the fixed-endpoint decision problem in NP follows by exhibiting the Hamiltonian path; the supplied Hamiltonian cycle can also be checked in polynomial time. This proves Theorem 1.

An important consequence of (5) is that **even computing the number of active vertices is NP-hard**, despite that number being bounded by a constant depending only on \(k\).

## Embedding into a visibly optimal lollipop

Add \(k\) vertices \(p_1,\ldots,p_k\), making
\[
\{\rho,p_1,\ldots,p_k\}
\]
a clique and adding no other edges incident with the new vertices. Let \(G\) be the resulting graph, let \(C\) be the known Hamiltonian cycle of \(H\), and take
\[
P=p_1p_2\cdots p_k\rho.
\]

Here “lollipop” means an ordinary path and cycle meeting precisely at the attachment endpoint; the path is not required to be induced.

We have:

* \(\delta(G)=k\);
* \(V(P)\cup V(C)=V(G)\);
* every cycle of \(G\) lies entirely in \(H\) or entirely in the added clique, because \(\rho\) is their only common vertex;
* the cycle \(C\) has \(|V(H)|>k+1\) vertices and is therefore a longest cycle of \(G\).

Hence this lollipop simultaneously maximizes coverage and cycle length. Its cycle omits exactly \(k\) vertices.

For cycle-only spanning-path activity,
\[
A(G[V(C)],\rho)=A(H,\rho)
\]
immediately.

The same equivalence holds if an active path is instead a spanning path of the whole lollipop starting at \(p_1\), without necessarily preserving the specified order of the handle: any such path ending in \(H-\rho\) must exhaust the added clique before passing through the cut vertex \(\rho\). Its remaining portion is a Hamiltonian path of \(H\) starting at \(\rho\).

This proves Theorem 2. Optimality is a promise here, not something that an NP verifier is being asked to certify.

# 5. An exact algorithm parameterized by the number of chords

Let
\[
C=v_0v_1\cdots v_{m-1}v_0,\qquad v_0=\rho,
\]
be a supplied Hamiltonian cycle of \(H\), and let
\[
Q=E(H)\setminus E(C),\qquad q=|Q|.
\]

## 5.1 A small candidate set

Let \(B\) consist of \(\rho\) and all endpoints of chords. Then
\[
A(H,\rho)\subseteq N_C(B)\setminus\{\rho\}.           \tag{6}
\]

To prove this, take a Hamiltonian \(\rho\)-\(x\) path. Since \(x\) has path degree one, some incident cycle edge \(xy\) is unused. If \(y\ne\rho\), then \(y\) is an internal path vertex. To compensate for this unused cycle edge, it must use a chord. Thus \(y\in B\), proving (6).

Consequently,
\[
|A(H,\rho)|\le \min\{m-1,\,4q+2\}.                  \tag{7}
\]
Set
\[
Y=N_C(B)\setminus\{\rho\};
\]
only vertices in \(Y\) need to be tested.

## 5.2 Enumerate used chords, not vertex orderings

Fix a candidate endpoint \(x\in Y\), and suppose a Hamiltonian \(\rho\)-\(x\) path uses exactly the chord set \(F\subseteq Q\). Let \(D\subseteq E(C)\) be its omitted cycle edges.

The degree equations are
\[
d_D(v)=d_F(v)+\mathbf 1_{\{v=\rho\}}+\mathbf 1_{\{v=x\}}
\qquad(v\in V(H)).                                  \tag{8}
\]

Write
\[
b_i=d_F(v_i)+\mathbf 1_{\{v_i=\rho\}}+\mathbf 1_{\{v_i=x\}},
\]
and let \(\epsilon_i\in\{0,1\}\) indicate whether \(v_iv_{i+1}\) is deleted. Equation (8) becomes
\[
\epsilon_{i-1}+\epsilon_i=b_i
\qquad(i\bmod m).                                   \tag{9}
\]

For fixed \(F,x\), there are at most two solutions:

1. Choose \(\epsilon_{m-1}\in\{0,1\}\).
2. Determine \(\epsilon_0,\ldots,\epsilon_{m-2}\) successively using (9).
3. Reject if any determined value is outside \(\{0,1\}\).
4. Check the remaining equation at \(v_{m-1}\).

For each resulting deletion set \(D\), form
\[
J=(V(H),(E(C)\setminus D)\cup F).
\]
Equation (8) guarantees that \(\rho,x\) have degree one and all other vertices have degree two. Therefore
\[
J\text{ is a Hamiltonian }\rho\text{-}x\text{ path}
\iff J\text{ is connected}.                         \tag{10}
\]

This gives a completely specified algorithm:

* enumerate \(F\subseteq Q\);
* enumerate \(x\in Y\);
* solve (9) using its two possible initial values;
* test connectivity as in (10);
* mark every successful \(x\).

Every Hamiltonian rooted path appears: its used chords and omitted cycle edges satisfy precisely these equations. Conversely, every accepted graph is a spanning path with the required endpoints.

There are \(2^q\) chord sets and at most \(4q+2\) candidate endpoints. Each pair requires \(O(m+q)\) time, giving
\[
O\!\left(2^q(q+1)(m+q)\right)
\]
time. Processing the candidates successively requires only \(O(m+q)\) working space.

For example, when \(q=0\), the algorithm returns exactly the two neighbors of \(\rho\) on the cycle.

## 5.3 Rotation-defined activity

The same enumeration gives the bound
\[
\#\{\text{Hamiltonian paths rooted at }\rho\}
\le 2^{q+1}|Y|
\le (8q+4)2^q.                                     \tag{11}
\]
Indeed, the used chord set, endpoint, and solution of (9) determine the path's edge set, and its orientation is fixed by its root.

Suppose activity instead means reachability from specified initial cycle paths under endpoint rotations. Enumerate all rooted Hamiltonian paths as above, construct their rotation graph, and perform graph search from the prescribed initial paths.

A usual rotation transforms
\[
(p_0,\ldots,p_i,\ldots,p_{m-1})
\]
into
\[
(p_0,\ldots,p_i,p_{m-1},p_{m-2},\ldots,p_{i+1})
\]
when \(p_ip_{m-1}\) is an edge. Any restrictions on allowable pivots can simply be imposed when generating transitions.

By (11), the explicit state graph has \(2^{O(q)}\) vertices, and its construction and search take \(2^{O(q)}m^{O(1)}\) time. This proves Theorem 3 without identifying rotation reachability with arbitrary path existence.

# 6. What this does and does not settle

For **spanning-path activity**, the computational conclusion is sharp:

* recognizing one active vertex is NP-complete;
* computing all active vertices, or even their number, is NP-hard;
* this remains true with a supplied optimal lollipop, prescribed fixed minimum degree, and a constant-size active set.

Thus a general polynomial-time exact algorithm for this formulation would imply \(P=NP\). The NP-completeness theorem itself is unconditional; no assumption that \(P\ne NP\) was used.

For **rotation-reachability activity**, the hardness proof does not apply. What is proved here is the chord-parameterized exact algorithm.

The remaining gap in answering the catalog question literally is identification of the source's precise activity and optimality definitions, together with the informal word “simple.” I have not independently verified those missing definitions or a literature novelty claim. Accordingly, I would not present the original Question 4.2 as settled on the supplied information alone.