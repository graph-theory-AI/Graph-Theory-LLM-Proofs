```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for finite vertex-transitive digraphs in a stronger rooted form, and a reciprocal-edge criterion gives another unconditional special case.",
  "would_publish": false,
  "caveats": "No general resolution or novelty claim; the catalog's conflicting claims about the k=3 literature were not independently verified."
}
```

## 1. Partial results

Throughout, digraphs are finite and loopless, with at most one arc in each direction between two vertices. Opposite arcs are allowed, and they form a directed cycle of length two.

Call a family of directed cycles **admissible** if it can be ordered as \(C_1,\ldots,C_k\) so that
\[
\left|V(C_j)\cap\bigcup_{i<j}V(C_i)\right|\le 1
\qquad (2\le j\le k).
\]

I establish two special cases.

**Theorem A — vertex-transitive case.**  
Let \(D\) be a finite vertex-transitive digraph of outdegree \(d\ge1\). For every prescribed vertex \(v\), there are \(d\) directed cycles whose pairwise intersections are exactly \(\{v\}\).

Consequently, Hoàng–Reed holds for every finite vertex-transitive digraph.

**Theorem B — reciprocal-edge criterion.**  
Let \(D\) have minimum outdegree at least \(k\). Form the undirected graph \(R\) on \(V(D)\) by putting \(xy\in E(R)\) precisely when both \(x\to y\) and \(y\to x\) are arcs of \(D\). If
\[
|V(D)|-c(R)\ge k-1,
\]
where \(c(R)\) counts all components, including isolated vertices, then \(D\) has an admissible family of \(k\) cycles. At least \(k-1\) of them can be chosen to have length two.

An explicit consequence of Theorem B is:

**Corollary.** If \(k\ge2\), \(D\) has \(n=k+1+t\) vertices and minimum outdegree at least \(k\), and
\[
t(t+1)<4k-2,
\]
then \(D\) satisfies the Hoàng–Reed conclusion.

These are self-contained partial results, not claims of new literature advances. None uses the disputed \(k=3\) history in the supplied catalog.

## 2. A product-set lemma

The proof of Theorem A uses the following finite-set inequality. A proof is included so that no specialized literature assertion is needed.

**Lemma 1.** Let \(A,B\) be finite subsets of a group, with \(1\in A\cap B\). Then
\[
|AB|\ge |A|+|B|-|A\cap B^{-1}|.
\tag{1}
\]

### Proof

First suppose
\[
A\cap B^{-1}=\{1\}.
\tag{2}
\]
Set \(C=AB\). Among all pairs \(P,Q\) satisfying
\[
1\in P\cap Q,\qquad P\cap Q^{-1}=\{1\},\qquad PQ\subseteq C,
\]
choose one maximizing \(|P|+|Q|\), and subject to that maximizing \(|P|\). Such a pair exists: the original pair is eligible, and every eligible \(P,Q\) lies in the finite set \(C\).

Suppose \(x\in P\cap Q\), with \(x\ne1\). Consider the two pairs
\[
\begin{aligned}
P^+&=P\cup Px, & Q^-&=Q\cap x^{-1}Q,\\
P^-&=P\cap Px^{-1}, & Q^+&=Q\cup xQ.
\end{aligned}
\tag{3}
\]
Both pairs contain \(1\) in both coordinates, and their products are contained in \(PQ\).

They also retain unique representation of the identity:

- For the first pair, a new representation would have the form
  \(p x q=1\), where \(p\in P\) and \(q\in Q^-\). Since \(xq\in Q\), the original uniqueness implies \(p=1\) and \(q=x^{-1}\). But \(x\in P\setminus\{1\}\) implies \(x^{-1}\notin Q\), a contradiction.
- For the second pair, a new representation would have the form
  \(p x q=1\), where \(p\in P^-\) and \(q\in Q\). Since \(px\in P\), uniqueness implies \(p=x^{-1}\) and \(q=1\). This contradicts \(x\in Q\setminus\{1\}\) and \(x^{-1}\in P\).

Write
\[
\alpha=|Px\setminus P|,\qquad \beta=|xQ\setminus Q|.
\]
Translations are bijections, so the sums of the coordinate sizes in (3) are respectively
\[
|P|+|Q|+\alpha-\beta,\qquad
|P|+|Q|-\alpha+\beta.
\]
Maximality of \(|P|+|Q|\) forces \(\alpha=\beta\). The secondary maximality of \(|P|\), applied to \((P^+,Q^-)\), then forces \(\alpha=0\).

Thus \(Px=P\). Since \(1\in P\), this gives \(x^{-1}\in P\), contradicting \(x\in Q\setminus\{1\}\). Therefore
\[
P\cap Q=\{1\}.
\]
Because \(P\cup Q\subseteq PQ\subseteq C\),
\[
|AB|=|C|\ge |P|+|Q|-1\ge |A|+|B|-1.
\tag{4}
\]

For the general case, let \(r=|A\cap B^{-1}|\), and remove from \(A\) every element of \(A\cap B^{-1}\) except \(1\). The resulting set \(A_0\) has size \(|A|-r+1\) and satisfies \(A_0\cap B^{-1}=\{1\}\). Applying (4),
\[
|AB|\ge |A_0B|
\ge |A_0|+|B|-1
=|A|+|B|-r.
\]
This proves (1). \(\square\)

## 3. Rooted expansion in a vertex-transitive digraph

For \(F\subseteq V(D)\), write
\[
\Gamma(F)=F\cup N^+(F)
\]
for its closed outneighborhood.

**Lemma 2.** Let \(D\) be vertex-transitive of outdegree \(d\). If \(v\in F\) and
\[
F\cap N^-(v)=\varnothing,
\tag{5}
\]
then
\[
|\Gamma(F)\setminus F|\ge d.
\tag{6}
\]

### Proof

Let \(G=\operatorname{Aut}(D)\), acting transitively on \(V(D)\), and let
\[
H=\{g\in G:g(v)=v\},\qquad h=|H|.
\]
Every fiber of the map \(g\mapsto g(v)\) has size \(h\).

Define
\[
A=\{g\in G:g(v)\in F\},
\qquad
B=\{g\in G:g(v)\in \{v\}\cup N^+(v)\}.
\]
Then
\[
|A|=h|F|,\qquad |B|=h(d+1).
\tag{7}
\]

For \(g\in G\),
\[
g\in B^{-1}
\quad\Longleftrightarrow\quad
g(v)\in\{v\}\cup N^-(v).
\]
Indeed, apply \(g\) to the condition \(v\to g^{-1}(v)\). Hence (5) gives
\[
A\cap B^{-1}=H.
\tag{8}
\]

Moreover,
\[
AB=\{g\in G:g(v)\in\Gamma(F)\}.
\tag{9}
\]
For one inclusion, if \(g=ab\), then \(b(v)\in\Gamma(\{v\})\), so
\(g(v)\in\Gamma(\{a(v)\})\subseteq\Gamma(F)\).
Conversely, if \(g(v)\in\Gamma(F)\), choose \(f\in F\) with
\(g(v)\in\Gamma(\{f\})\), and choose \(a\in G\) with \(a(v)=f\).
Then \(a\in A\) and \(a^{-1}g\in B\).

Applying Lemma 1 and using (7)–(9),
\[
h|\Gamma(F)|
=|AB|
\ge h|F|+h(d+1)-h
=h(|F|+d).
\]
Division by \(h\) proves (6). \(\square\)

## 4. Proof of Theorem A

Fix \(v\in V(D)\). Split \(v\) into a source \(s\) and a sink \(t\):

- retain all arcs not incident with \(v\);
- replace each \(v\to u\) by \(s\to u\);
- replace each \(u\to v\) by \(u\to t\).

Internally vertex-disjoint \(s\)-\(t\) paths correspond exactly to directed cycles through \(v\) that are otherwise vertex-disjoint.

Let \(X\subseteq V(D)\setminus\{v\}\) be an internal vertex separator between \(s\) and \(t\). Equivalently, \(D-X\) has no directed cycle through \(v\). Let \(F\) be the set of vertices reachable from \(v\) in \(D-X\), including \(v\).

Then
\[
F\cap N^-(v)=\varnothing:
\]
otherwise a path from \(v\) to an in-neighbor of \(v\), followed by its arc to \(v\), would give a directed cycle through \(v\).

Also,
\[
\Gamma(F)\subseteq F\cup X,
\]
because an outneighbor of \(F\) outside \(X\) is reachable from \(v\). Lemma 2 therefore gives
\[
|X|\ge |\Gamma(F)\setminus F|\ge d.
\]
Directed vertex-Menger now supplies \(d\) internally vertex-disjoint \(s\)-\(t\) paths. Identifying \(s,t\) back into \(v\) gives the asserted \(d\) cycles. \(\square\)

In particular, any \(k\le d\) of these cycles form an admissible family in any order.

As a consistency check, if \(D\) has \(n\) vertices and directed girth \(g\), these cycles give
\[
n\ge 1+d(g-1),
\]
and consequently
\[
g\le 1+\left\lfloor\frac{n-1}{d}\right\rfloor
=\left\lceil\frac nd\right\rceil.
\]
Thus the argument also recovers the Caccetta–Häggkvist bound within this special class.

## 5. Proof of Theorem B and the order bound

### The reciprocal-edge criterion

The maximum number of edges in a forest contained in \(R\) is
\[
r=|V(D)|-c(R).
\]
Assume \(r\ge k-1\), and choose a forest \(T\subseteq R\) with exactly \(k-1\) edges, viewing all other vertices as isolated vertices of \(T\).

Root each component of \(T\), and let \(U\) be the set of roots. Since a rooted tree has one fewer edge than vertices,
\[
|V(D)\setminus U|=k-1.
\]
Therefore
\[
\delta^+(D[U])\ge k-(k-1)=1.
\]
The finite digraph \(D[U]\) contains a directed cycle \(C_1\).

For every parent–child edge of \(T\), take its directed two-cycle in \(D\). Add these \(k-1\) cycles in an order in which parents precede children. The child of each newly added edge has not appeared in any earlier cycle: it is not a root, and its descendants have not yet been processed. Thus each new two-cycle meets the preceding union in at most its parent.

Together with \(C_1\), these are the required \(k\) cycles. \(\square\)

### A numerical sufficient condition

Let \(m=|E(R)|\), and put \(n=|V(D)|\). There is at most one arc per unordered pair, apart from the additional arc contributed by a reciprocal pair. Hence
\[
nk\le |A(D)|\le \binom n2+m,
\]
so
\[
m\ge nk-\binom n2.
\tag{10}
\]

If \(R\) has forest rank \(r\), with component sizes \(s_1,\ldots,s_c\), then
\[
\begin{aligned}
m
&\le \sum_i\binom{s_i}{2}\\
&=\frac12\sum_i\bigl((s_i-1)^2+(s_i-1)\bigr)\\
&\le \frac12(r^2+r)
=\binom{r+1}{2}.
\end{aligned}
\tag{11}
\]
Consequently,
\[
nk-\binom n2>\binom{k-1}{2}
\tag{12}
\]
forces \(r\ge k-1\), and Theorem B applies.

Writing \(n=k+1+t\), condition (12) becomes exactly
\[
t(t+1)<4k-2.
\]
This proves the stated corollary.

## 6. Where the attack stops

The rooted expansion inequality is not available merely from a minimum-outdegree hypothesis. In fact, the stronger conclusion of Theorem A is false for an arbitrary prescribed root.

For \(k\ge2\), take a bidirected complete graph on
\[
W=\{a_0,a_1,\ldots,a_k\},
\]
add a vertex \(z\), and add the arcs
\[
z\to a_i\quad(1\le i\le k),\qquad a_0\to z.
\]
The resulting digraph has minimum outdegree \(k\). But every directed cycle through \(z\) also contains \(a_0\), so there cannot even be two cycles through \(z\) that are otherwise vertex-disjoint.

This is **not** a counterexample to Hoàng–Reed: the bidirected clique already contains the required family. It does identify a genuine obstruction to extending the vertex-transitive argument verbatim.

The reciprocal-edge argument, meanwhile, gives no information for oriented digraphs when \(k\ge2\). Thus arbitrary non-vertex-transitive oriented digraphs remain outside both mechanisms. The general Hoàng–Reed conjecture is neither proved nor disproved by this attack.