```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the first nontrivial exact value f(3)=4, obtain f(4)≥6, and identify a parameter inversion error in the catalogued lower bound.",
  "would_publish": false,
  "caveats": "No asymptotic upper-bound improvement is obtained; the small case may be folklore, and its novelty has not been literature-checked."
}
```

# Partial resolution of Problem 1.1

## 1. Definitions and an order formulation

Let \(D\) be a finite oriented graph and let \(\chi(D)\) denote the chromatic number of its underlying undirected graph. Subgraphs are allowed to omit arcs; this is the interpretation consistent with the quoted quadratic upper bound and with the tournament results.

Define
\[
a(D)=\max\{\chi(H):H\subseteq D\text{ is acyclic}\}.
\]
An acyclic subgraph of chromatic number at least \(k\) contains an acyclic subgraph of chromatic number exactly \(k\), by passing to a \(k\)-critical subgraph. Thus “\(k\)-chromatic” and “at least \(k\)-chromatic” are interchangeable here.

For a linear order \(\prec\) on \(V(D)\), let \(F_\prec(D)\) be the undirected graph consisting of those edges \(xy\) whose arc in \(D\) is directed from the earlier to the later endpoint.

### Lemma 1
\[
a(D)=\max_{\prec}\chi(F_\prec(D)).
\]

#### Proof
The arcs corresponding to \(F_\prec(D)\) all point forward in \(\prec\), so they form an acyclic subgraph of \(D\).

Conversely, if \(H\subseteq D\) is acyclic, choose a topological ordering of \(H\) and extend it to a linear order of \(V(D)\). Then the underlying graph of \(H\) is a subgraph of \(F_\prec(D)\), and hence
\[
\chi(H)\leq \chi(F_\prec(D)).
\]
∎

For any fixed order, the forward and backward edges partition \(E(D)\), and both classes form acyclic subgraphs. Consequently
\[
\chi(D)\leq a(D)^2.
\]
This gives
\[
f(k)\leq (k-1)^2+1=k^2-2k+2.
\]

Equivalently, if
\[
g(r)=\max\{\chi(D):a(D)\leq r\},
\]
then
\[
f(r+1)=g(r)+1,\qquad g(r)\leq r^2.
\]

## 2. Orientations in which every odd cycle is directed

The case \(r=2\) admits a useful exact characterization.

### Lemma 2
For an oriented graph \(D\), the following are equivalent:

1. \(a(D)\leq2\);
2. every odd cycle of the underlying graph is cyclically directed in \(D\).

#### Proof
If an odd cycle \(C\) is not cyclically directed, then the subgraph consisting only of the edges of \(C\) has no directed cycle: its only possible directed cycle would be \(C\) itself. It is therefore an acyclic \(3\)-chromatic subgraph.

Conversely, if an acyclic subgraph \(H\) is non-bipartite, then its underlying graph contains an odd cycle. That cycle cannot be cyclically directed, since otherwise \(H\) would contain a directed cycle. ∎

The key point is that such orientations can occur only on \(3\)-colorable graphs.

### Theorem 3
If every odd cycle of an oriented graph \(D\) is cyclically directed, then
\[
\chi(D)\leq3.
\]

#### Proof
Suppose otherwise. Passing to a subgraph, let \(Q\) be a \(4\)-critical underlying graph with the inherited orientation. Every odd cycle of \(Q\) is still cyclically directed.

Fix \(v\in V(Q)\), and put
\[
A=N_Q^+(v),\qquad B=N_Q^-(v).
\]
Since \(Q\) is \(4\)-critical, \(Q-v\) has a proper \(3\)-coloring.

We first observe that there is no odd path in \(Q-v\) with two distinct endpoints in \(A\). Indeed, if \(P\) were such a path with endpoints \(x,y\in A\), then
\[
v x\cup P\cup yv
\]
would be an odd cycle. At \(v\), both cycle edges point away from \(v\), so this cycle could not be cyclically directed. The same argument shows that there is no odd path in \(Q-v\) with both endpoints in \(B\).

Start with an arbitrary proper \(3\)-coloring \(\varphi\) of \(Q-v\), using colors \(1,2,3\).

We first make every vertex of \(A\) have color \(1\). If \(a\in A\) currently has color \(i\in\{2,3\}\), consider the component \(C\) containing \(a\) in the subgraph induced by colors \(1\) and \(i\). The component \(C\) cannot contain a vertex \(a'\in A\) of color \(1\), since a path in \(C\) from \(a\) to \(a'\) would have odd length. We may therefore interchange colors \(1\) and \(i\) on \(C\), increasing the number of vertices of \(A\) colored \(1\) without changing any already-correctly-colored vertex of \(A\). Iterating gives
\[
\varphi(A)=\{1\}.
\]

Next eliminate color \(3\) from \(B\). If \(b\in B\) has color \(3\), consider its component in the subgraph induced by colors \(2\) and \(3\). This component cannot contain a vertex of \(B\) colored \(2\), since that would give an odd path with both endpoints in \(B\). Swapping colors \(2\) and \(3\) on this component decreases the number of color-\(3\) vertices in \(B\). It does not affect \(A\), whose vertices all have color \(1\). Iterating gives
\[
\varphi(B)\subseteq\{1,2\}.
\]

Thus every neighbor of \(v\) has color \(1\) or \(2\), and we may assign color \(3\) to \(v\). This produces a proper \(3\)-coloring of \(Q\), contradicting \(\chi(Q)=4\). ∎

Equivalently:

> Every orientation of every \(4\)-chromatic graph contains a non-cyclically-oriented odd cycle.

The edge set of that cycle is an acyclic \(3\)-chromatic subgraph.

## 3. Exact value of \(f(3)\)

### Corollary 4
\[
\boxed{f(3)=4}.
\]

#### Proof
A cyclically oriented triangle has chromatic number \(3\), but every acyclic subgraph is a proper subgraph of the triangle and hence is bipartite. Thus \(f(3)\geq4\).

Conversely, Theorem 3 shows that every orientation of a \(4\)-chromatic graph contains an acyclic \(3\)-chromatic subgraph. Hence \(f(3)\leq4\). ∎

For completeness,
\[
f(1)=1,\qquad f(2)=2,\qquad f(3)=4.
\]

In the notation above, Theorem 3 says exactly
\[
g(2)=3,
\]
improving the general estimate \(g(2)\leq4\).

## 4. A lower bound for \(f(4)\), and a general finite lower bound

Let \(T_5\) be the cyclic tournament on \(\mathbb Z_5\), with
\[
i\to j \quad\Longleftrightarrow\quad j-i\pmod 5\in\{1,2\}.
\]
It has no transitive subtournament on four vertices. Indeed, by translation symmetry it is enough to delete \(0\); the remaining vertices contain the directed triangle
\[
1\to2\to4\to1.
\]

Every \(4\)-chromatic graph on at most five vertices contains a \(K_4\). To see this, take a \(4\)-critical subgraph \(H\). If \(|H|=4\), then \(H=K_4\). If \(|H|=5\), then \(\delta(H)\geq3\), so \(\overline H\) is a matching. Two missing disjoint edges would make \(H\) \(3\)-colorable, while with at most one missing edge \(H\) contains a \(K_4\).

It follows that an acyclic \(4\)-chromatic subgraph of \(T_5\) would contain all arcs of a \(K_4\), and these arcs would form a transitive subtournament, a contradiction. Therefore \(a(T_5)\leq3\), while \(\chi(T_5)=5\). Hence
\[
\boxed{f(4)\geq6}.
\]
Together with the general upper bound,
\[
6\leq f(4)\leq10.
\]

More generally, one obtains a modest self-contained bound.

### Proposition 5
For every \(k\geq4\),
\[
f(k)\geq k+2.
\]

#### Proof
First note that every \(k\)-chromatic graph on at most \(k+1\) vertices contains \(K_k\). Indeed, in a \(k\)-critical subgraph \(H\), either \(|H|=k\), giving \(K_k\), or \(|H|=k+1\). In the latter case \(\delta(H)\geq k-1\), so \(\overline H\) is a matching. Since \(\chi(H)=k\), that matching has exactly one edge, and \(H=K_{k+1}-e\), which contains \(K_k\).

For \(k=4\), \(T_5\) has no transitive \(4\)-vertex subtournament. For \(k\geq5\), a random tournament on \(k+1\) vertices has expected number of transitive \(k\)-subtournaments
\[
\frac{(k+1)k!}{2^{\binom{k}{2}}}.
\]
At \(k=5\) this is \(720/1024<1\), and the ratio of successive expressions is
\[
\frac{k+2}{2^k}<1.
\]
Thus there exists a tournament \(T\) on \(k+1\) vertices with no transitive \(k\)-subtournament.

If \(T\) contained an acyclic \(k\)-chromatic subgraph, its underlying graph would contain \(K_k\), and the corresponding tournament on those \(k\) vertices would be acyclic, hence transitive. This is impossible. Thus a counterexample exists at chromatic number \(k+1\), proving \(f(k)\geq k+2\). ∎

## 5. The catalogued asymptotic lower bound appears to use the inverse parameter

The catalog states that the best lower bound is
\[
1+\left\lfloor\sqrt{k-1}\right\rfloor.
\]
For the extracted definition of \(f(k)\), this cannot be the relevant benchmark: trivially \(f(k)\geq k\).

The square-root expression is instead the direct guarantee. If
\[
h(n)=\min_{\chi(D)=n}a(D),
\]
then the forward/backward partition gives
\[
h(n)\geq\lceil\sqrt n\rceil
      =1+\left\lfloor\sqrt{n-1}\right\rfloor.
\]
Upon inversion, this is precisely the upper bound
\[
f(k)\leq(k-1)^2+1.
\]

Moreover, the tournament construction stated in the supplied abstract already implies a substantially stronger lower bound for the inverse function \(f\). Namely, if for each large \(n\) there is an \(n\)-vertex tournament \(T_n\) satisfying
\[
a(T_n)\leq n^{3/4+o(1)},
\]
then, for every fixed \(\delta>0\), taking
\[
n=\left\lfloor k^{4/3-\delta}\right\rfloor
\]
gives \(a(T_n)<k\) for sufficiently large \(k\). Since \(\chi(T_n)=n\),
\[
\boxed{f(k)\geq k^{4/3-o(1)}}.
\]
Thus the bounds supported by the supplied source are
\[
k^{4/3-o(1)}
   \leq f(k)
   \leq k^2-2k+2.
\]

## 6. Remaining gap

The full asymptotic problem remains unresolved. In the equivalent notation
\[
g(r)=\max\{\chi(D):a(D)\leq r\},
\]
the known general argument gives \(g(r)\leq r^2\), while the tournament construction gives \(g(r)\geq r^{4/3-o(1)}\). The argument above determines only the first nontrivial case,
\[
g(2)=3,
\]
and does not extend directly to \(r\geq3\), where the obstruction to an acyclic \((r+1)\)-chromatic subgraph is no longer represented by a single odd cycle.