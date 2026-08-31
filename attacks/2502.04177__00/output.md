```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but it is equivalent to polynomial-in-r strong coloring numbers; I prove it for bounded-apex bounded-layered-treewidth classes and give polynomial-expansion stress tests with bn_r=2 and scol_r at least r^q.",
  "would_publish": false,
  "caveats": "No argument covers arbitrary polynomial-expansion classes, and the lower-bound families are not counterexamples."
}
```

# 1. Statement and conventions

All graphs are finite and simple. For an order \(\preceq\) of \(V(G)\), a vertex \(u\preceq v\) is strongly \(r\)-reachable from \(v\) if there is a \(v\)-\(u\) path of length at most \(r\) whose internal vertices are all strictly later than \(v\). The set of such vertices is denoted
\[
\operatorname{SReach}_r(G,\preceq,v),
\]
and
\[
\operatorname{scol}_r(G)
 =\min_{\preceq}\max_{v\in V(G)}
 |\operatorname{SReach}_r(G,\preceq,v)|.
\]

A depth-\(r\) bramble is a bramble all of whose members have radius at most \(r\); its order is the minimum size of a transversal, and \(\operatorname{bn}_r(G)\) is the maximum order of such a bramble.

I do not resolve the full question. The main rigorous conclusions below are:

1. Using the polynomial bound on shallow bramble number stated in the source paper, the conjecture is equivalent to asking whether every polynomial-expansion class has \(\operatorname{scol}_r\) polynomially bounded in \(r\) alone.
2. The conjecture holds for every class in which a bounded number of vertices can be deleted to leave bounded layered treewidth.
3. For every \(q\), there is a monotone polynomial-expansion class containing graphs \(G\) and radii \(r\) with
   \[
   \operatorname{bn}_r(G)=2
   \quad\text{and}\quad
   \operatorname{scol}_r(G)\ge r^q+1.
   \]
   Consequently, neither the degree of the desired polynomial nor its dependence on the expansion rate can be universal over all polynomial-expansion classes.

# 2. The bramble variable is existentially redundant

Let \(\mathcal C\) have polynomial expansion, and let \(\mathcal C^\downarrow\) be its subgraph closure. This closure still has polynomial expansion: every depth-\(r\) minor of a subgraph of \(G\) is also a depth-\(r\) minor of \(G\).

The result quoted from *Shallow brambles* therefore gives a polynomial \(p_{\mathcal C}\) such that
\[
\operatorname{bn}_r(G)\le p_{\mathcal C}(r)
\qquad
(G\in\mathcal C,\ r\ge0).
\]

Hence, for a fixed class \(\mathcal C\), the following are equivalent.

- There is a polynomial \(f_{\mathcal C}(r,b)\) such that
  \[
  \operatorname{scol}_r(G)
  \le f_{\mathcal C}\bigl(r,\operatorname{bn}_r(G)\bigr).
  \]
- There is a one-variable polynomial \(q_{\mathcal C}\) such that
  \[
  \operatorname{scol}_r(G)\le q_{\mathcal C}(r).
  \]

Indeed, the second statement implies the first by taking \(f_{\mathcal C}(r,b)=q_{\mathcal C}(r)\). Conversely, if \(f_{\mathcal C}\) has total degree \(d\), then on nonnegative arguments
\[
|f_{\mathcal C}(r,b)|\le C(1+r+b)^d
\]
for a constant \(C\). Substituting \(b\le p_{\mathcal C}(r)\) yields a polynomial bound in \(r\).

Thus the conjecture is, at the level of its quantifiers, exactly the polynomial strong-coloring-number problem for polynomial-expansion classes.

# 3. A tree-decomposition lemma

For a tree decomposition \(\mathcal T=(T,(B_t)_{t\in V(T)})\), define its radius-\(r\) local bag width by
\[
\lambda_r(\mathcal T)
 =
 \max_{\substack{t\in V(T)\\v\in V(G)}}
 |B_t\cap N_r^G[v]|
\]
and put
\[
\lambda_r(G)=\min_{\mathcal T}\lambda_r(\mathcal T).
\]

## Lemma 3.1
For every graph \(G\) and every \(r\ge0\),
\[
\operatorname{scol}_r(G)\le \lambda_r(G).
\]

### Proof

Fix a tree decomposition \(\mathcal T\). Form a supergraph \(H\) of \(G\) by making every bag \(B_t\) a clique. Equivalently, \(H\) is the intersection graph of the subtrees
\[
T_v=\{t:v\in B_t\},\qquad v\in V(G).
\]
Thus \(H\) is chordal, and every clique of \(H\) is contained in a bag of \(\mathcal T\).

Let
\[
\sigma=(v_1,\ldots,v_n)
\]
be a perfect elimination ordering of \(H\), and use the reverse order
\[
v_n\prec v_{n-1}\prec\cdots\prec v_1
\]
for \(G\).

Fix \(v_i\), and suppose \(u\prec v_i\) is strongly reachable from \(v_i\). Every internal vertex of a witnessing path has \(\sigma\)-index less than \(i\), while \(u\) has index greater than \(i\). Repeatedly choose an internal path vertex of minimum \(\sigma\)-index. Its two path-neighbours have larger indices and are therefore adjacent in \(H\), by the perfect-elimination property. Shortcutting this vertex eventually shows that \(u v_i\in E(H)\).

Consequently,
\[
\operatorname{SReach}_r(G,\prec,v_i)
 \subseteq
 \{v_i\}\cup N_H^+(v_i),
\]
where the right side is a clique of \(H\), hence is contained in some bag \(B_t\). Every strongly reachable vertex is also in \(N_r^G[v_i]\). Therefore
\[
|\operatorname{SReach}_r(G,\prec,v_i)|
 \le |B_t\cap N_r^G[v_i]|
 \le\lambda_r(\mathcal T).
\]
Minimizing over decompositions proves the claim. \(\square\)

There is also a bramble lower bound on this local decomposition parameter.

## Lemma 3.2
For every graph \(G\) and every \(r\ge0\),
\[
\operatorname{bn}_r(G)\le \lambda_{3r+1}(G).
\]

### Proof

Let \(\mathcal B\) be a depth-\(r\) bramble. For each \(B\in\mathcal B\), the set of decomposition nodes whose bags meet \(B\) is a subtree of \(T\). Touching bramble members give intersecting subtrees. By the Helly property for subtrees of a tree, some bag \(B_t\) meets every member of \(\mathcal B\).

Fix \(B_0\in\mathcal B\) and a centre \(c_0\) of \(B_0\). If \(B\in\mathcal B\) has centre \(c_B\), then \(B\) touches \(B_0\), so
\[
\operatorname{dist}_G(c_0,c_B)\le 2r+1.
\]
Every vertex of \(B\) is within distance \(r\) of \(c_B\), and hence every member of \(\mathcal B\) lies in \(N_{3r+1}[c_0]\). Therefore
\[
B_t\cap N_{3r+1}[c_0]
\]
is a transversal of \(\mathcal B\), and so its size is at least the order of \(\mathcal B\). \(\square\)

The direction in Lemma 3.2 is not enough for the conjecture: one would need an upper bound on a suitable ordered version of \(\lambda_r\), not this lower bound.

# 4. Bounded layered treewidth

A layering of \(G\) is a partition
\[
V(G)=V_0\cup\cdots\cup V_m
\]
such that each edge has endpoints in equal or consecutive layers. A tree decomposition has layered width at most \(k\) if
\[
|B_t\cap V_i|\le k
\]
for every bag \(B_t\) and every layer \(V_i\).

## Theorem 4.1
If \(G\) has layered treewidth at most \(k\), then
\[
\operatorname{scol}_r(G)\le k(2r+1)
\qquad(r\ge0).
\]

### Proof

Use a tree decomposition and layering witnessing layered width \(k\). If \(v\in V_i\), then
\[
N_r[v]\subseteq V_{i-r}\cup\cdots\cup V_{i+r}.
\]
Thus every bag satisfies
\[
|B_t\cap N_r[v]|\le k(2r+1).
\]
Lemma 3.1 now gives the result. \(\square\)

A bounded exceptional set can be placed first in the order.

## Lemma 4.2
For every \(A\subseteq V(G)\),
\[
\operatorname{scol}_r(G)
 \le |A|+\operatorname{scol}_r(G-A).
\]

### Proof

Put all vertices of \(A\) first, and then use an order witnessing \(\operatorname{scol}_r(G-A)\).

For \(v\notin A\), a strong path to a vertex outside \(A\) cannot use a vertex of \(A\) internally, since every vertex of \(A\) is earlier than \(v\). Thus the only additional strongly reachable vertices are the at most \(|A|\) vertices of \(A\). A vertex in \(A\) has at most \(|A|\) earlier possible endpoints. \(\square\)

## Corollary 4.3
Suppose there are constants \(a,k\) such that every \(G\in\mathcal C\) has a set \(A_G\) with
\[
|A_G|\le a
\]
and \(G-A_G\) of layered treewidth at most \(k\). Then
\[
\operatorname{scol}_r(G)\le a+k(2r+1).
\]
Hence the conjecture holds for \(\mathcal C\), with a polynomial independent of \(\operatorname{bn}_r(G)\).

This covers bounded layered-treewidth classes and bounded-apex extensions of them. The polynomial-expansion hypothesis is not needed for this special case.

# 5. A stress test with \(\operatorname{bn}_r=2\)

The next construction shows that the degree of the desired polynomial must depend on the class.

## Lemma 5.1
If
\[
\operatorname{girth}(G)>6r+3,
\]
then
\[
\operatorname{bn}_r(G)\le2.
\]

### Proof

Let \(\mathcal B\) be a depth-\(r\) bramble, choose \(B_0\in\mathcal B\), and let \(c\) be a centre of \(B_0\). As in Lemma 3.2, every member of \(\mathcal B\) lies in \(N_{3r+1}[c]\).

If a radius-\(R\) ball contains a cycle, a breadth-first-search tree together with a non-tree edge gives a cycle of length at most \(2R+1\). Since
\[
2(3r+1)+1=6r+3,
\]
the induced graph on \(N_{3r+1}[c]\) is a forest.

Every bramble in a forest has order at most \(2\). For completeness, subdivide every forest edge once. For each connected set \(X\), add to \(X\) the midpoint of every edge incident with \(X\). Touching sets become intersecting subtrees. Pairwise intersecting subtrees have a common point. If that point is an original vertex, one vertex hits all sets; if it is the midpoint of an edge \(xy\), then \(\{x,y\}\) hits all sets. \(\square\)

## Theorem 5.2
For every integer \(q\ge1\), there is a monotone graph class \(\mathcal D_q\) with polynomial expansion such that, for infinitely many \(r\), it contains a graph \(G_r\) satisfying
\[
\operatorname{bn}_r(G_r)=2
\quad\text{and}\quad
\operatorname{scol}_r(G_r)\ge r^q+1.
\]

### Construction of the cores

Let \(L\) be sufficiently large and put
\[
d=L^q,\qquad N=d^8.
\]
There exists a simple graph \(H_L\) on \(N\) vertices, with girth at least \(8\), and exactly
\[
m=dN
\]
edges.

Here is a self-contained probabilistic proof. In \(G(N,p)\), take
\[
p=\frac{4d}{N}.
\]
If \(M\) is the number of edges and \(X\) the number of cycles of lengths \(3,\ldots,7\), then
\[
\mathbb E M=2d(N-1)
\]
and
\[
\mathbb E X
 \le\sum_{j=3}^7\frac{(Np)^j}{2j}
 =\sum_{j=3}^7\frac{(4d)^j}{2j}
 =O(d^7).
\]
Since \(dN=d^9\), for sufficiently large \(d\),
\[
\mathbb E(M-X)>dN.
\]
Choose a realization with \(M-X\ge dN\), delete at most one edge per short cycle, and then delete arbitrary additional edges until exactly \(dN\) remain.

Let \(G_L\) be obtained by replacing every edge of \(H_L\) by a path of length exactly \(L\).

### Shallow bramble number

Every cycle of \(G_L\) has length at least \(8L\). For \(L\ge2\),
\[
8L>6L+3.
\]
Lemma 5.1 gives
\[
\operatorname{bn}_L(G_L)\le2.
\]
Since \(G_L\) has an edge, the two singleton sets consisting of its endpoints form a depth-\(L\) bramble of order \(2\). Hence
\[
\operatorname{bn}_L(G_L)=2.
\]

### Strong coloring number lower bound

Fix any linear order of \(V(G_L)\). For an incidence \((v,e)\), where \(v\) is an endpoint of an edge \(e\in E(H_L)\), call \((v,e)\) active if the subdivided \(e\)-path contains a vertex earlier than \(v\).

Every original edge has at least one active incidence: on its subdivided path, if the minimum vertex is one endpoint, the other incidence is active; if the minimum is internal, both incidences are active. Thus the total number of active incidences is at least \(m\).

If \((v,e)\) is active, walk from \(v\) along the subdivided \(e\)-path and let \(x\) be the first vertex earlier than \(v\). Every internal vertex of the \(v\)-\(x\) subpath is later than \(v\), and the path has length at most \(L\). Hence \(x\) is strongly \(L\)-reachable from \(v\). For a fixed \(v\), different incident edges give different such vertices.

Averaging over the \(N\) original vertices, some \(v\) has at least
\[
\frac{m}{N}=d=L^q
\]
such vertices. Therefore
\[
\operatorname{scol}_L(G_L)\ge L^q+1.
\]

### Polynomial expansion

We have
\[
|V(G_L)|
 =N+(L-1)m
 \le 2L\,d^9
 =2L^{9q+1}.
\]

Consider a depth-\(s\) minor \(J\) of \(G_L\).

If
\[
4s+1<L,
\]
call a branch set principal if it contains an original vertex of \(H_L\). Two principal branch sets cannot be adjacent: otherwise two distinct original vertices of \(H_L\) would be at distance at most \(4s+1<L\) in \(G_L\). A nonprincipal branch set lies in the interior of a single subdivided edge and has at most two neighbouring branch sets. Therefore every edge of \(J\) has a nonprincipal endpoint and
\[
|E(J)|\le 2|V(J)|,
\]
so the average degree of \(J\) is at most \(4\).

If \(4s+1\ge L\), then
\[
L\le5(s+1),
\]
and the crude bound
\[
\overline d(J)<|V(G_L)|
 \le 2\cdot 5^{9q+1}(s+1)^{9q+1}
\]
is polynomial in \(s\).

Thus \(\{G_L:L\ge L_0\}\), and also its subgraph closure \(\mathcal D_q\), has polynomial expansion.

For completeness, these classes themselves satisfy the conjecture. Order all original vertices before all subdivision vertices. If \(r<L\), a strong path from an internal vertex cannot pass through an original vertex internally, and on each of the two directions along its subdivided edge there is at most one strongly reachable earlier vertex. Hence
\[
\operatorname{scol}_r(G_L)\le3
\qquad(r<L).
\]
If \(r\ge L\), then
\[
\operatorname{scol}_r(G_L)\le |V(G_L)|
 \le2r^{9q+1}.
\]
The same bounds hold for subgraphs.

# 6. Consequences and remaining gap

Theorem 5.2 has two consequences.

1. There is no single class-independent polynomial \(F(r,b)\) valid for every polynomial-expansion class. Indeed, setting \(b=2\) and choosing \(q\) larger than the degree of \(F(r,2)\) gives a contradiction.
2. Even the smallest nontrivial value \(\operatorname{bn}_r=2\) does not prevent \(\operatorname{scol}_r\) from being an arbitrarily high fixed power of \(r\). The exponent must be allowed to depend on the expansion profile of the class.

This is not a counterexample to the stated conjecture because for each fixed \(q\) the class \(\mathcal D_q\) admits a polynomial bound.

The unresolved step is therefore genuinely structural: one needs to derive a polynomial strong-coloring-number bound from an arbitrary polynomial expansion bound. Lemma 3.1 does this when there is a tree decomposition with polynomially bounded local bag intersections, and Theorem 4.1 supplies such decompositions for bounded layered treewidth. Polynomial expansion alone is not currently shown here to provide a comparable ordered decomposition, even after recursively handling exceptional vertices. Hence the general conjecture remains open.