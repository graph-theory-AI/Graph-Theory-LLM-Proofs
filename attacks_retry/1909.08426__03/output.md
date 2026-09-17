```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There is an explicit polynomial kernel under a stronger diamond-type exclusion, while most clique-blown-up path cases admit an OR-composition ruling out polynomial kernels unless NP is contained in coNP/poly.",
  "would_publish": false,
  "caveats": "These are kernelization results, not a resolution of the FPT conjecture; the P7-free case is untouched, and novelty is not claimed."
}
```

# 1. Scope of the partial results

All graphs are finite and simple. The parameterized decision problem is to determine whether
\[
\alpha(G)\ge k.
\]
The integers \(t,\ell\ge 1\) are fixed, not parameters.

I do not prove or disprove the conjecture. I establish two narrower results:

1. **A constructive positive result.** For every fixed \(d\ge2\), Independent Set on graphs excluding
   \[
   D_d:=K_{d+2}-e
   \]
   as an induced subgraph has a polynomial kernel with \(O_d(k^{d+1})\) vertices. Taking \(d=t\), these graphs form a subclass of the conjectured class for every \(\ell\ge3\).

2. **A limitation on kernelization of the full class.** For
   \[
   \boxed{\ell\ge4,\ t\ge2}
   \qquad\text{or}\qquad
   \boxed{\ell=3,\ t\ge3},
   \]
   Independent Set on \(P_\ell(t)\)-free graphs has a polynomial-time OR-cross-composition. Consequently, a polynomial kernel would imply
   \[
   \mathrm{NP}\subseteq\mathrm{coNP}/\mathrm{poly}.
   \]

The second result does **not** obstruct FPT algorithms, superpolynomial-size kernels, or polynomial Turing kernels.

I have not checked whether these kernelization observations already appear in the literature and do not claim novelty.

# 2. A polynomial kernel under a diamond-type exclusion

For \(d=2\), the graph \(D_d\) is the diamond. In general, \(D_d\) consists of a \(d\)-clique and two nonadjacent vertices complete to that clique.

## Theorem 2.1

For every fixed \(d\ge2\), Independent Set on induced-\(D_d\)-free graphs admits a polynomial kernel with \(O_d(k^{d+1})\) vertices.

More explicitly, for \(k\ge2\), one may use the bound
\[
B_d(k)
=(d-1)(k-1)^{d+1}
+\sum_{j=1}^{d-1}(k-1)^j.
\]

The proof uses a large-clique reduction followed by a size bound.

## 2.1. Large maximal cliques have bounded external adjacency

### Lemma 2.2

Let \(G\) be \(D_d\)-free and let \(C\) be a maximal clique. Every vertex outside \(C\) has at most \(d-1\) neighbors in \(C\).

### Proof

Suppose that \(x\notin C\) has \(d\) neighbors \(q_1,\ldots,q_d\) in \(C\). Maximality of \(C\) supplies a vertex \(y\in C\) nonadjacent to \(x\). Then
\[
G[\{q_1,\ldots,q_d,x,y\}]
\]
is \(K_{d+2}-e\), with \(xy\) as its only missing edge. This is forbidden. ∎

The relevant maximal cliques can also be found in polynomial time.

### Lemma 2.3

If \(Q\) is a \(d\)-clique in a \(D_d\)-free graph, then
\[
C(Q):=Q\cup\bigcap_{v\in Q}N(v)
\]
is the unique maximal clique containing \(Q\).

### Proof

Any two nonadjacent common neighbors of \(Q\), together with \(Q\), would induce \(D_d\). Thus \(C(Q)\) is a clique.

Every vertex that could extend \(C(Q)\) is a common neighbor of \(Q\), and hence already belongs to \(C(Q)\). Uniqueness follows because every clique containing \(Q\) is contained in \(C(Q)\). ∎

Consequently, enumerating all \(d\)-cliques finds every maximal clique of size at least \(d\) in \(n^{d+O(1)}\) time.

## 2.2. The reduction rule

### Lemma 2.4

Let \(G\) be \(D_d\)-free, let \(k\ge2\), and let \(C\) be a maximal clique satisfying
\[
|C|\ge(d-1)(k-1)+1.
\]
Then
\[
\alpha(G)\ge k
\quad\Longleftrightarrow\quad
\alpha(G-C)\ge k-1.
\]

### Proof

An independent set contains at most one vertex of \(C\), proving the forward implication.

Conversely, let \(I\subseteq V(G)\setminus C\) be independent with \(|I|=k-1\). By Lemma 2.2,
\[
|N(I)\cap C|
\le\sum_{x\in I}|N(x)\cap C|
\le(d-1)(k-1)
<|C|.
\]
Some vertex of \(C\) is therefore nonadjacent to all of \(I\), and extends \(I\) to an independent set of size \(k\). ∎

This gives the safe rule
\[
(G,k)\longmapsto(G-C,k-1).
\]

## 2.3. A residual size bound

The following elementary bound is useful independently.

### Lemma 2.5

For integers \(d,a,q\ge1\), if \(G\) is \(D_d\)-free and
\[
\alpha(G)\le a,\qquad \omega(G)\le q,
\]
then
\[
|V(G)|
\le F_d(a,q)
:=q a^d+\sum_{j=1}^{d-1}a^j.
\]

Here \(D_1=P_3\).

### Proof

We induct on \(d\).

For \(d=1\), a \(P_3\)-free graph is a disjoint union of cliques. It has at most \(a\) components, each of size at most \(q\), so
\[
|V(G)|\le aq=F_1(a,q).
\]

Now let \(d\ge2\). For every vertex \(v\), the graph \(G[N(v)]\) is \(D_{d-1}\)-free: adding \(v\) to an induced \(D_{d-1}\) in its neighborhood would produce an induced \(D_d\). By induction,
\[
|N(v)|\le F_{d-1}(a,q).
\]

Choose a maximal independent set \(S\). It is dominating and has size at most \(a\). Hence
\[
\begin{aligned}
|V(G)|
&\le \sum_{v\in S}|N[v]|\\
&\le a\bigl(1+F_{d-1}(a,q)\bigr)\\
&=q a^d+\sum_{j=1}^{d-1}a^j.
\end{aligned}
\]
∎

## 2.4. The kernelization algorithm

First handle \(k\le1\) and \(k>n\) directly. Repeatedly apply Lemma 2.4 whenever possible, using Lemma 2.3 to locate an eligible maximal clique.

Suppose this process stops with current target \(r\ge2\). Set
\[
a=r-1,\qquad q=(d-1)(r-1).
\]
Since no eligible clique remains,
\[
\omega(G)\le q.
\]

If the residual instance is a NO-instance, then \(\alpha(G)\le a\), so Lemma 2.5 gives
\[
|V(G)|
\le q a^d+\sum_{j=1}^{d-1}a^j
=B_d(r)
\le B_d(k).
\]

Thus:

- if the residual graph has more than \(B_d(r)\) vertices, return a fixed YES-instance;
- otherwise retain the residual instance.

Each clique reduction lowers the target, and the entire procedure takes \(n^{d+O(1)}\) time. Induced-\(D_d\)-freeness is preserved throughout. This proves Theorem 2.1. ∎

## 2.5. Relation to the conjectured class

For \(1\le d\le t\) and \(\ell\ge3\), the graph \(P_\ell(t)\) contains an induced \(D_d\): take \(d\) vertices from an internal bag and one vertex from each neighboring bag.

Therefore
\[
\operatorname{Forb}_{\mathrm{ind}}(D_t)
\subseteq
\operatorname{Forb}_{\mathrm{ind}}(P_\ell(t)).
\]

In particular:

### Corollary 2.6

For every fixed \(t\ge2\) and \(\ell\ge3\), Independent Set has an \(O_t(k^{t+1})\)-vertex kernel on the subclass of \(P_\ell(t)\)-free graphs that are also induced-\((K_{t+2}-e)\)-free.

This is a stronger-forbidden-subgraph result, **not** a proof for an additional full pair \((\ell,t)\).

# 3. A polynomial-kernel obstruction for the full class

I use the standard OR-cross-composition theorem in the following form:

> If an NP-hard language OR-cross-composes into a parameterized problem, with output parameter polynomially bounded in the maximum input length and the logarithm of the number of inputs, then a polynomial kernel for the parameterized problem implies  
> \[
> \mathrm{NP}\subseteq\mathrm{coNP}/\mathrm{poly}.
> \]

Below, the composition itself is particularly simple and fully specified.

## 3.1. The NP-hard source language

Independent Set remains NP-hard on triangle-free graphs. Here is a direct reduction establishing the fact needed below.

Given a graph \(G\) with \(m\) edges, replace every edge \(uv\) by a path
\[
u-a_{uv}-b_{uv}-v.
\]
Call the resulting triangle-free graph \(T(G)\).

For a chosen set \(S\subseteq V(G)\) of original vertices, the maximum number of internal vertices that can be added independently is
\[
m-e_G(S).
\]
Indeed, an edge-path contributes one internal vertex unless both its original endpoints are selected, in which case it contributes none. Therefore
\[
\alpha(T(G))
=m+\max_{S\subseteq V(G)}\bigl(|S|-e_G(S)\bigr).
\]

Deleting at most one chosen endpoint for each edge of \(G[S]\) leaves an independent set of size at least \(|S|-e_G(S)\). Consequently
\[
|S|-e_G(S)\le\alpha(G).
\]
Equality is attained when \(S\) is a maximum independent set. Thus
\[
\boxed{\alpha(T(G))=m+\alpha(G).}
\]

The threshold transformation is \(k\mapsto m+k\), proving the required NP-hardness.

## 3.2. The composition

Take triangle-free instances
\[
(G_1,k),\ldots,(G_r,k)
\]
with the same target. Construct their complete join
\[
J=G_1\vee\cdots\vee G_r.
\]
Every vertex of one summand is adjacent to every vertex of every other summand. Hence
\[
\boxed{\alpha(J)=\max_i\alpha(G_i).}
\]
Thus
\[
(J,k)\text{ is YES}
\quad\Longleftrightarrow\quad
\text{at least one }(G_i,k)\text{ is YES}.
\]

The construction is polynomial in the total input length. The output parameter is still \(k\).

To fit the cross-composition definition, use valid explicitly encoded triangle-free instances with \(1\le k\le |V(G)|\), and group them by \(k\). This is a polynomial equivalence relation: among inputs of length at most \(N\), there are at most \(N\) such target values. Invalid inputs can be placed in a separate NO-class.

It remains to verify that \(J\) belongs to the required graph class.

## 3.3. Case \(\ell\ge4,\ t\ge2\)

The complement of \(P_\ell\) is connected for every \(\ell\ge4\): vertex \(1\) is adjacent in the complement to every vertex numbered at least \(3\), and vertex \(2\) is adjacent to vertex \(4\).

Replacing these vertices by nonempty independent sets preserves connectivity, so
\[
\overline{P_\ell(t)}
\]
is connected.

It follows that the class of \(P_\ell(t)\)-free graphs is closed under complete joins. Indeed, a copy of \(P_\ell(t)\) meeting two join summands would have disconnected complement, which is impossible.

Moreover, \(P_\ell(t)\) contains a triangle when \(t\ge2\), since two consecutive bags induce \(K_{2t}\). Each triangle-free \(G_i\) is therefore \(P_\ell(t)\)-free, and so is their join \(J\).

## 3.4. Case \(\ell=3,\ t\ge3\)

Suppose \(J\) contains \(P_3(t)\), with bags \(A,B,C\), in that order.

The bags \(A\) and \(C\) are anticomplete. Since different join summands are complete to one another, all vertices of \(A\cup C\) must lie in a single summand \(G_i\). But \(A\) is a \(t\)-clique, contradicting triangle-freeness when \(t\ge3\).

Thus \(J\) is also \(P_3(t)\)-free in this range.

Combining these arguments gives the following result.

## Theorem 3.1

Fix \(t,\ell\) satisfying either
\[
\ell\ge4,\ t\ge2,
\]
or
\[
\ell=3,\ t\ge3.
\]
If Independent Set on \(P_\ell(t)\)-free graphs admits a polynomial kernel, then
\[
\mathrm{NP}\subseteq\mathrm{coNP}/\mathrm{poly}.
\]
∎

For comparison, the cases \(\ell\le2\) have elementary polynomial Ramsey kernels: the forbidden graph is \(K_t\) or \(K_{2t}\). The argument above gives no polynomial-kernel conclusion for \((\ell,t)=(3,2)\) or for \(t=1\).

# 4. Why the positive reduction does not extend directly

The key property in Section 2 was that a vertex outside a maximal clique has at most \(d-1\) neighbors in it. This fails substantially under the conjecture’s hypothesis. More importantly, the resulting clique-deletion rule can become incorrect.

Fix \(t\ge2\), and let
\[
G=K_q\vee P_4,
\]
where the path has vertices \(a,b,c,d\), in that order. Let
\[
C=V(K_q)\cup\{b,c\}.
\]

Then:

- \(C\) is a maximal clique;
- \(\alpha(G)=2\);
- \(G-C\) consists of the two independent vertices \(a,d\).

Consequently,
\[
(G,3)\text{ is NO},\qquad (G-C,2)\text{ is YES}.
\]
Thus deleting a sufficiently large maximal clique and lowering the target by one is not generally safe.

Nevertheless, \(G\) is \(P_4(t)\)-free. Since \(\overline{P_4(t)}\) is connected, an induced copy would have to lie in one join summand. It cannot lie in \(K_q\), because \(P_4(t)\) is not complete, nor in the four-vertex summand \(P_4\), because \(4t>4\). It follows also that \(G\) is \(P_\ell(t)\)-free for every \(\ell\ge4\).

This is **not** a counterexample to the conjecture. It identifies precisely why the polynomial-kernel proof needs its stronger exclusion.

# 5. Remaining gap

I rechecked the previous attempt’s local completion-cell observation: a clique of the missing size in such a cell does complete the forbidden induced graph, so the stated local Ramsey bound is sound. That local fact does not control the total number of different cores or provide a global kernel.

The OR-composition gives a formal reason not to expect a **polynomial-size many-one kernel** throughout most of the \(t\ge2\) range, unless the standard complexity collapse occurs. It does not rule out the desired \(f(k)n^{O(1)}\) algorithms.

The unresolved step remains a global algorithmic treatment of arbitrary interactions between large cliques, without the bounded external adjacency supplied by \(D_d\)-freeness. No such treatment is obtained here. In particular, these arguments provide no FPT algorithm for general \(P_7\)-free graphs.