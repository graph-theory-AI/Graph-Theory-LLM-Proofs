```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is not resolved, but an FPT dense-module special case is proved and Ramsey, separator, and half-graph restrictions on any counterexample are isolated.",
  "would_publish": false,
  "caveats": "Neither the relevant modular defect nor the distance to the known special case is bounded by k."
}
```

# 1. Statement and outcome

For fixed \(t\ge 1\), let  
\[
H_t=P(t,t,t,t)
\]
be obtained from a four-vertex path by replacing every vertex with a clique of size \(t\). The parameterized decision problem is:

> Given an \(H_t\)-free graph \(G\) and \(k\), decide whether \(\alpha(G)\ge k\).

I do not prove or disprove that this problem is FPT. The main positive result below is an exact algorithm for \(H_t\)-free graphs with bounded “low-clique modular defect.” I also give two reductions isolating the remaining hard core and an example showing that the most immediate attempt to bootstrap the known \(P(1,t,t,t)\)-free result cannot work by a packing argument alone.

No claim of novelty relative to unpublished or unknown work is made.

# 2. Ramsey obstructions in a no-instance

Write \(R(a,b)\) for the usual Ramsey number.

## Proposition 2.1: exclusion of a fat \(P_4\)

Let
\[
q=R(t,k)\le \binom{t+k-2}{t-1}.
\]
Suppose that \(G\) is \(H_t\)-free and \(\alpha(G)<k\). Then there do not exist four pairwise disjoint sets
\[
V_1,V_2,V_3,V_4,\qquad |V_i|\ge q,
\]
such that, for \(i\ne j\),

- \(V_i\) is complete to \(V_j\) when \(|i-j|=1\);
- \(V_i\) is anticomplete to \(V_j\) when \(|i-j|>1\).

There are no restrictions on the edges internal to the \(V_i\).

### Proof

Since \(\alpha(G)<k\), each \(G[V_i]\), having at least \(R(t,k)\) vertices, contains a clique \(C_i\) of size \(t\). The prescribed cross-adjacencies imply that
\[
G[C_1\cup C_2\cup C_3\cup C_4]\cong P(t,t,t,t),
\]
a contradiction. \(\square\)

Thus every no-instance is free of a \(q\)-vertex-per-part homogeneous blow-up of \(P_4\). Notice that this is substantially weaker than being \(P(1,q,q,q)\)-free: the first part also has to be large.

A basic corollary is that, on the subclass with \(\omega(G)<t\), the problem has a kernel with fewer than \(R(t,k)\) vertices.

## Proposition 2.2: bounded exact clone classes

Suppose \(G\) is \(H_t\)-free and contains an induced \(P(s,t,t,t)\), with path bags
\[
A,B,C,D,\qquad |A|=s<t,\quad |B|=|C|=|D|=t.
\]
Define
\[
X=\{x\notin A\cup B\cup C\cup D:
 x\text{ is complete to }A\cup B
 \text{ and anticomplete to }C\cup D\}.
\]
Then
\[
\omega(G[X])<t-s.
\]
Consequently, if additionally \(\alpha(G)<k\), then
\[
|X|<R(t-s,k).
\]

### Proof

If \(X\) contained a clique \(Y\) of size \(t-s\), then \(A\cup Y,B,C,D\) would be the four clique bags of an induced \(H_t\). The Ramsey bound follows because \(G[X]\) has neither a clique of size \(t-s\) nor an independent set of size \(k\). \(\square\)

This says that every particular \(P(1,t,t,t)\) witness has only a bounded set of exact endpoint-clones in a no-instance. The difficulty is that there may be unboundedly many essentially unrelated witnesses.

# 3. Complement-side structure

Let
\[
F_t=\overline{H_t}.
\]
Since \(\overline{P_4}\cong P_4\), \(F_t\) is a \(P_4\) whose four vertices are substituted by independent sets of size \(t\).

## Lemma 3.1: connectivity of the forbidden complement

For every \(t\ge1\),
\[
\kappa(F_t)=t.
\]

### Proof

Deleting fewer than \(t\) vertices leaves at least one vertex in every one of the four bags. The remaining graph is still connected along the quotient path. Hence \(\kappa(F_t)\ge t\).

Deleting all \(t\) vertices in the second bag separates the first bag from the last two bags, so \(\kappa(F_t)\le t\). \(\square\)

This gives an exact separator reduction.

## Proposition 3.2: reduction to \(t\)-connected complements

Let \(J=\overline G\). Suppose
\[
V(J)=A\mathbin{\dot\cup}S\mathbin{\dot\cup}B,
\qquad E_J(A,B)=\varnothing,
\qquad |S|<t,
\]
with \(A,B\ne\varnothing\). Then
\[
\omega(J)=
\max\bigl\{\omega(J[A\cup S]),\omega(J[B\cup S])\bigr\}.
\]

Moreover, an induced \(F_t\) cannot use vertices from both \(A\) and \(B\).

### Proof

A clique cannot meet both \(A\) and \(B\), giving the displayed identity.

If an induced copy of \(F_t\) met both sides, deleting its vertices in \(S\) would disconnect it. This would be a separator of size less than \(t\), contradicting Lemma 3.1. \(\square\)

Consequently, a polynomial-time Turing reduction recursively decomposes \(J\) at separators of order less than \(t\). Since \(t\) is fixed, such a separator can be found by enumerating all sets of fewer than \(t\) vertices. The recursion has polynomial size, for instance \(n^{O(t)}\).

Thus it is enough to solve the conjecture for inputs satisfying

\[
\overline G\text{ is \(t\)-vertex-connected}.
\]

This does not give an algorithm for those cores.

## Proposition 3.3: exclusion of a fixed induced half-graph

Let \(L_m\) be the induced half-graph with independent sides
\[
\{a_1,\dots,a_m\},\qquad \{b_1,\dots,b_m\},
\]
and
\[
a_i b_j\in E(L_m)\quad\Longleftrightarrow\quad i\le j.
\]
If \(G\) is \(H_t\)-free, then \(\overline G\) is induced-\(L_{4t}\)-free.

### Proof

Inside \(L_{4t}\), set
\[
\begin{aligned}
X_1&=\{a_{2t+1},\dots,a_{3t}\},\\
X_2&=\{b_{3t+1},\dots,b_{4t}\},\\
X_3&=\{a_1,\dots,a_t\},\\
X_4&=\{b_{t+1},\dots,b_{2t}\}.
\end{aligned}
\]
Each \(X_i\) is independent. By the ordering of the indices,

- \(X_1\) is complete to \(X_2\);
- \(X_2\) is complete to \(X_3\);
- \(X_3\) is complete to \(X_4\);
- \(X_1\) is anticomplete to \(X_3\) and \(X_4\);
- \(X_2\) is anticomplete to \(X_4\).

Thus these sets induce \(F_t\). Therefore an induced \(L_{4t}\) in \(\overline G\) would yield an induced \(H_t\) in \(G\). \(\square\)

This is a genuine bounded-order/half-graph restriction, but I do not obtain an FPT clique algorithm from it.

# 4. An FPT special case via modular decomposition

The following is the strongest algorithmic partial result here.

A module \(M\) in a graph is a vertex set such that every vertex outside \(M\) is either complete or anticomplete to \(M\). At a node of the canonical modular decomposition, let
\[
G_u=Q(G_1,\dots,G_r)
\]
denote the substitution representation, where \(Q\) is the quotient on the child modules. The quotient is complete, edgeless, or prime.

For a prime node \(u\), define
\[
S_u=\{i\in [r]:\omega(G_i)<t\},
\]
and define the low-clique modular defect
\[
\delta_t(G)=\max_{u\text{ prime}} |S_u|,
\]
with maximum zero if there is no prime node.

## Theorem 4.1

For fixed \(t\), maximum-weight independent set on an \(H_t\)-free graph \(G\) with nonnegative vertex weights can be solved in time
\[
2^{\delta_t(G)}\,n^{t+O(1)}.
\]

In particular, for every function \(g_t\), the conjecture holds on the subclass satisfying
\[
\delta_t(G)\le g_t(k).
\]

### Proof

Process the modular decomposition bottom-up. Let \(w_i\) be the maximum weight of an independent set in \(G_i\).

For an edgeless quotient, all child modules are pairwise anticomplete, so the optimum is \(\sum_i w_i\). For a complete quotient, it is \(\max_i w_i\).

It remains to process a prime quotient \(Q\). Put
\[
S=S_u,\qquad L=[r]\setminus S.
\]

### Claim

The graph \(Q[L]\) is \(P_4\)-free.

Indeed, suppose \(i_1,i_2,i_3,i_4\in L\) induce a \(P_4\) in \(Q\). For each \(j\), the child graph \(G_{i_j}\) contains a clique \(C_j\) of size \(t\). Since cross-adjacencies between child modules are complete or anticomplete according to \(Q\), the four cliques \(C_1,C_2,C_3,C_4\) induce \(H_t\), a contradiction.

Therefore \(Q[L]\) is a cograph. For each independent set \(X\subseteq S\), define
\[
L_X=L\setminus N_Q(X).
\]
An independent set of \(Q\) whose intersection with \(S\) is exactly \(X\) can use an arbitrary independent set of the cograph \(Q[L_X]\). Hence its maximum weight is
\[
\sum_{i\in X}w_i+\alpha_w(Q[L_X]).
\]
It follows that
\[
\alpha_w(G_u)=
\max_{\substack{X\subseteq S\\Q[X]\text{ edgeless}}}
\left(
\sum_{i\in X}w_i+\alpha_w(Q[L_X])
\right).
\]

There are at most \(2^{|S|}\) choices for \(X\), and weighted independent set on a cograph is computed in polynomial time by the usual union/join recursion.

For fixed \(t\), whether a child graph contains \(K_t\) can be checked by enumerating \(t\)-subsets. Across the modular decomposition this contributes \(n^{t+O(1)}\). The claimed running time follows. \(\square\)

## Ramsey interpretation of the remaining defect

Suppose \(G\) is a no-instance for \(k\), and let \(G_i\) be a low-clique child at a modular-decomposition node. Then
\[
\omega(G_i)<t,\qquad \alpha(G_i)<k.
\]
Therefore
\[
|V(G_i)|<R(t,k).
\]

Thus every individual low-clique child is Ramsey-small. The unresolved issue is that a prime quotient may contain arbitrarily many such children.

This is not automatically bounded by \(k\). For example, for \(t\ge2\), let
\[
G_n=\overline{C_n},\qquad n\ge5.
\]
Then \(\alpha(G_n)=2\), while \(G_n\) is \(H_t\)-free because \(C_n\) cannot contain \(F_t\): every induced subgraph of \(C_n\) has maximum degree at most \(2\), whereas \(F_t\) has vertices of degree \(2t\). Since \(C_n\) is prime, the root children are singletons and
\[
\delta_t(G_n)=n.
\]
For \(t=2\), \(\overline{G_n}=C_n\) is also \(t\)-connected, so even the separator reduction does not bound this defect.

# 5. Lifting the known \(P(1,t,t,t)\)-free case

Let
\[
Q_t=P(1,t,t,t),
\]
with the singleton at an endpoint of the path. Let
\[
\tau_{Q_t}(G)=\min\{|X|:G-X\text{ is }Q_t\text{-free}\}.
\]

## Theorem 5.1

For fixed \(t\), Independent Set is FPT parameterized by
\[
k+\tau_{Q_t}(G).
\]

This holds even without assuming \(G\) is \(H_t\)-free.

### Proof

Let \(X\) be a set of size \(\tau=\tau_{Q_t}(G)\) such that \(G-X\) is \(Q_t\)-free.

For every independent set \(S\subseteq X\), invoke the known FPT algorithm for \(Q_t\)-free graphs on
\[
G_S=G-(X\cup N_G(S))
\]
with target \(k-|S|\).

The graph \(G_S\) is an induced subgraph of \(G-X\), hence remains \(Q_t\)-free. Moreover,
\[
\alpha(G)\ge k
\]
if and only if one of these \(2^\tau\) calls answers yes: for any independent set \(I\), take \(S=I\cap X\), and conversely combine \(S\) with an independent set in \(G_S\).

The set \(X\) can itself be found by a bounded search tree. Whenever the current graph contains an induced \(Q_t\), every deletion set must contain at least one of its \(1+3t\) vertices, so branch on those vertices. Induced \(Q_t\) can be detected in \(n^{1+3t+O(1)}\) time because \(t\) is fixed. Thus finding \(X\) takes
\[
(1+3t)^\tau n^{O(t)}
\]
time. \(\square\)

A maximal family of vertex-disjoint induced \(Q_t\)'s yields a deletion set by taking the union of its copies. Hence the same argument is FPT in \(k\) plus the maximum number of vertex-disjoint \(Q_t\)'s.

Unfortunately, that packing number is not bounded in a no-instance.

## Proposition 5.2: unbounded packing obstruction

For every \(t\ge2\) and every \(r\), there is an \(H_t\)-free graph \(G_r\) such that

- \(\alpha(G_r)=2\);
- \(\overline{G_r}\) is connected;
- \(G_r\) contains \(r\) vertex-disjoint induced copies of \(Q_t\).

### Construction and proof

Let
\[
B_t=\overline{Q_t}.
\]
It is a connected bipartite graph on \(3t+1\) vertices.

Take \(r\) disjoint copies \(B_t^1,\dots,B_t^r\). For each \(i<r\), add exactly one edge between \(B_t^i\) and \(B_t^{i+1}\), with no other inter-copy edges. Orient the bipartitions of successive copies so that the resulting graph \(J_r\) is bipartite. Every added inter-copy edge is a bridge.

The graph \(J_r\) contains no induced \(F_t\). An induced \(F_t\) cannot lie in a single block because
\[
|V(B_t)|=3t+1<4t=|V(F_t)|.
\]
It cannot meet more than one block because \(F_t\) is \(t\)-connected, and \(t\ge2\), whereas different blocks are separated by a bridge.

Set
\[
G_r=\overline{J_r}.
\]
Then \(G_r\) is \(H_t\)-free. Since \(J_r\) is bipartite,
\[
\alpha(G_r)=\omega(J_r)=2.
\]
Also, \(J_r\) is connected, and each original block induces \(Q_t\) in \(G_r\). Thus the asserted packing has size \(r\). \(\square\)

Consequently, neither the \(Q_t\)-deletion distance nor the \(Q_t\)-packing number can be bounded by a function of \(k,t\), even after decomposing complete joins.

# 6. A useful closure observation

The graph \(H_t\) has no false twins: no two nonadjacent vertices have the same open neighborhood. Therefore the class of \(H_t\)-free graphs is closed under replacing vertices by independent sets of false twins.

Indeed, if an induced \(H_t\) in such an independent blow-up used two vertices from the same substituted set, those two vertices would be false twins inside the copy. Thus every substituted set contributes at most one vertex, and projection gives an induced \(H_t\) in the original graph.

As a consequence, weighted Independent Set with integer weights capped by \(k\) reduces to unweighted Independent Set by replacing a vertex of weight \(w\) by \(w\) independent twins, without leaving the \(H_t\)-free class. Thus weighted quotient problems are not a fundamentally stronger version of this conjecture.

# 7. Remaining gap

The preceding results leave the following core untreated:

1. \(\overline G\) may be \(t\)-connected and induced-\(L_{4t}\)-free.
2. A prime modular quotient may have arbitrarily many \(K_t\)-free children.
3. In a no-instance, each such child has fewer than \(R(t,k)\) vertices, but their number is unbounded.
4. There may be arbitrarily many induced \(P(1,t,t,t)\) witnesses, so the known source-paper algorithm cannot be lifted through a bounded modulator or packing argument.

An FPT algorithm for this prime, highly connected, Ramsey-small-module core would resolve the conjecture. None of the arguments above supplies such an algorithm, and no hardness reduction is obtained either.