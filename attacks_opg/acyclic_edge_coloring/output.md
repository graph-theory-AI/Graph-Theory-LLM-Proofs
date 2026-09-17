```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit construction proves a'(K_{p,p}) = p+2 for every odd prime p, but does not resolve the conjecture for general graphs.",
  "would_publish": false,
  "caveats": "A sharp special-case verification only; no claim of novelty or reliance on the unverified recent literature."
}
```

## Result obtained

Write \(a'(G)\) for the acyclic chromatic index of \(G\). Equivalently, an edge-colouring is acyclic if it is proper and the union of any two colour classes is a forest.

I do not obtain a proof or counterexample for arbitrary simple graphs. The following is a fully checkable dense special case.

**Theorem.** For every odd prime \(p\),
\[
a'(K_{p,p})=p+2.
\]
Moreover,
\[
a'(K_{m,p})=p\qquad(1\le m<p).
\]

The proof gives further exact values:
\[
a'(K_{p-1,p-1})=p,
\]
and, for \(p\ge5\),
\[
a'(K_{p-2,p-2})=p.
\]
Consequently, the conjectured bound holds for every complete bipartite graph \(K_{m,n}\), with \(1\le m\le n\), whenever an odd prime belongs to \(\{n,n+1,n+2\}\).

No novelty is claimed for these special cases.

## 1. Why two extra colours are necessary for odd balanced orders

We first establish a lower bound that does not require primality.

**Lemma 1.** If \(n\ge3\) is odd, then
\[
a'(K_{n,n})\ge n+2.
\]

**Proof.** Suppose that \(K_{n,n}\) has an acyclic edge-colouring with a palette of \(n+1\) colours.

Every colour class is a matching, hence has at most \(n\) edges. At most one colour class can have \(n\) edges: two such classes would be perfect matchings, whose union contains cycles.

Thus the total number of edges is at most
\[
n+n(n-1)=n^2.
\]
Equality is necessary. Therefore there is exactly one perfect colour class \(M_0\), and the other classes
\[
M_1,\ldots,M_n
\]
each have \(n-1\) edges.

For \(i\ge1\), let \(u_i\) and \(v_i\) be the vertices missed by \(M_i\) on the left and right, respectively. The graph \(M_0\cup M_i\) is an acyclic graph on \(2n\) vertices with \(2n-1\) edges and maximum degree two. It is therefore a Hamiltonian path, with endpoints \(u_i,v_i\).

Set
\[
e_i=u_iv_i,\qquad N_i=M_i\cup\{e_i\}.
\]
Then \(N_i\) is a perfect matching, and \(M_0\cup N_i\) is a Hamiltonian cycle.

Order the vertices in each bipartition class. A perfect matching \(N\) determines a permutation; denote its sign by \(\varepsilon(N)\). If two perfect matchings form an alternating Hamiltonian cycle on \(2n\) vertices, their relative permutation is an \(n\)-cycle. Consequently,
\[
\varepsilon(N_i)\varepsilon(M_0)=(-1)^{n-1}=1.
\]
Thus all the \(N_i\) have the same sign.

Now fix \(i\). The edge \(e_i\) belongs neither to \(M_i\) nor to \(M_0\): in particular, it cannot be an edge of the Hamiltonian path \(M_0\cup M_i\) joining its endpoints. Since the graph is complete bipartite, \(e_i\) belongs to some \(M_j\), where \(j\ne0,i\).

The forest \(M_i\cup M_j\) has \(2n-2\) edges on \(2n\) vertices, hence exactly two components. One component is the isolated edge \(e_i\), because \(M_i\) misses both its endpoints. The other component is a path on the remaining \(2n-2\) vertices, with endpoints \(u_j,v_j\).

It follows that \(N_i\cup N_j\) consists of:

- their common edge \(e_i\); and
- an alternating cycle on the other \(2n-2\) vertices, obtained by adding \(e_j\) to that path.

Their relative permutation therefore has one fixed point and one \((n-1)\)-cycle. Hence
\[
\varepsilon(N_i)\varepsilon(N_j)=(-1)^{n-2}=-1,
\]
contradicting the fact that all \(N_i\) have the same sign. \(\square\)

For later use, also note the elementary bound
\[
a'(K_{n,n})\ge n+1\qquad(n\ge2).
\]
Indeed, in a proper \(n\)-edge-colouring every colour class would be perfect, immediately producing bichromatic cycles.

## 2. A cyclic factorization with one cycle per colour pair

Let \(q\) be prime. Label both parts of \(K_{q,q}\) by \(\mathbb F_q\), and give edge \(xy\) the colour
\[
c(x,y)=y-x.
\]
For \(a\in\mathbb F_q\), the colour class is the perfect matching
\[
M_a=\{(x,x+a):x\in\mathbb F_q\}.
\]

For distinct colours \(a,b\), traversing an \(M_a\)-edge from left to right and then an \(M_b\)-edge backwards sends
\[
x\longmapsto x+a-b.
\]
Because \(q\) is prime and \(a-b\ne0\), this translation has a single orbit on \(\mathbb F_q\). Therefore:

**Lemma 2.** For every distinct \(a,b\), the union \(M_a\cup M_b\) is a single Hamiltonian cycle of length \(2q\).

The colouring of the whole \(K_{q,q}\) is thus emphatically **not** acyclic. But deleting any vertex destroys every bichromatic cycle.

In particular, restricting this colouring gives an acyclic \(q\)-edge-colouring of every \(K_{r,s}\) with
\[
1\le r,s\le q,\qquad \min(r,s)<q.
\]

Taking \(q=p\), \(r=m<p\), and \(s=p\) proves
\[
a'(K_{m,p})\le p.
\]
The reverse inequality follows from its maximum degree \(p\).

## 3. Repairing the balanced graph with two new colours

Now let \(p\ge5\) be prime. Start with the preceding \(p\)-colouring of \(K_{p,p}\).

Choose \(g\in\mathbb F_p^\times\) of multiplicative order \(p-1\), and consider the perfect matching
\[
T=\{(x,gx):x\in\mathbb F_p\}.
\]
Such a \(g\) exists because the multiplicative group of a finite field is cyclic.

The original colour of \((x,gx)\) is
\[
(g-1)x.
\]
Since \(g\ne1\), these colours run through all of \(\mathbb F_p\). Thus \(T\) meets each original colour class exactly once.

Introduce two new colours \(\alpha,\beta\). Recolour the two edges of \(T\) indexed by \(x\in\{0,1\}\) with \(\alpha\), and recolour all the other edges of \(T\) with \(\beta\). Explicitly,
\[
\chi(x,y)=
\begin{cases}
\alpha,&y=gx,\ x\in\{0,1\},\\
\beta,&y=gx,\ x\notin\{0,1\},\\
y-x,&y\ne gx.
\end{cases}
\]

This uses \(p+2\) colours. It is proper because \(T\) is a matching and the original colouring was proper.

We check every possible pair of colours.

### Two original colours

For distinct \(a,b\in\mathbb F_p\), their original union was a single Hamiltonian cycle. Recolouring \(T\) removes one edge from each of these two colour classes. The remaining two-colour graph is therefore a forest.

### The two new colours

Their union is \(T\), a matching. In particular, it contains no cycle.

### One original colour and one new colour

Fix \(a\in\mathbb F_p\). The matchings \(M_a\) and \(T\) share exactly the edge indexed by
\[
x_a=\frac{a}{g-1}.
\]

Traversing a \(T\)-edge and then an \(M_a\)-edge backwards sends
\[
x\longmapsto gx-a.
\]
This affine permutation fixes \(x_a\), and
\[
(gx-a)-x_a=g(x-x_a).
\]
Multiplication by \(g\) has a single orbit on \(\mathbb F_p^\times\). Consequently, as a simple graph, \(M_a\cup T\) consists of:

- the isolated common edge indexed by \(x_a\); and
- one alternating cycle of length \(2(p-1)\).

That unique cycle uses \(p-1\) edges of \(T\).

But the \(\alpha\)-class contains only two edges, and the \(\beta\)-class contains only \(p-2\) edges. Since \(p\ge5\), both numbers are strictly smaller than \(p-1\). Thus neither new colour supplies all the \(T\)-edges of this cycle.

The actual subgraphs on colours \(\{a,\alpha\}\) and \(\{a,\beta\}\) are subgraphs of \(M_a\cup T\), so neither contains a cycle.

These three cases exhaust all colour pairs. Hence \(\chi\) is acyclic, proving
\[
a'(K_{p,p})\le p+2\qquad(p\ge5).
\]

### The remaining odd prime \(p=3\)

Use the construction of Section 2 with modulus \(5\), restricted to left and right labels \(\{0,1,2\}\):
\[
\chi(x,y)=y-x\pmod5.
\]
Lemma 2 shows that this is an acyclic five-colouring of \(K_{3,3}\).

Combining these upper bounds with Lemma 1 proves
\[
\boxed{a'(K_{p,p})=p+2\quad\text{for every odd prime }p.}
\]

## 4. Further exact cases

Restricting the unmodified prime-modulus colouring gives
\[
a'(K_{p-1,p-1})\le p.
\]
The regular-graph lower bound from Section 1 gives the reverse inequality, so
\[
\boxed{a'(K_{p-1,p-1})=p.}
\]

For \(p\ge5\), restriction also gives
\[
a'(K_{p-2,p-2})\le p.
\]
Since \(p-2\) is odd and at least three, Lemma 1 gives
\[
a'(K_{p-2,p-2})\ge(p-2)+2=p.
\]
Thus
\[
\boxed{a'(K_{p-2,p-2})=p.}
\]

More generally, suppose \(1\le m\le n\) and an odd prime \(p\) lies in \(\{n,n+1,n+2\}\).

- If \(p=n\), the balanced construction or the unbalanced restriction gives at most \(n+2\) colours.
- If \(p>n\), restrict the unmodified prime-modulus colouring to \(K_{m,n}\). It uses \(p\le n+2\) colours.

This proves the claimed prime-interval special case of the conjecture.

## 5. Where the general argument fails

The construction relies on two strong properties:

1. every pair of original colour classes forms **one** cycle;
2. a matching meeting each original colour exactly once can be chosen with controlled intersections with those classes.

The first property already fails for the analogous cyclic colouring at composite orders. For example, modulo \(9\), colours \(0\) and \(3\) induce three disjoint six-cycles. A repair that recolours only one edge from each original colour removes at most two edges from their union, leaving at least one of those cycles intact.

This is an obstruction to this particular repair scheme, **not** a counterexample to the conjecture. Arbitrary graphs can likewise have many bichromatic components, with no available prime cyclic structure to control them.

Thus the proof establishes sharp dense special cases—including infinitely many graphs requiring all \(\Delta+2\) colours—but provides no universal \(\Delta+2\) construction. The general conjecture remains unresolved by this argument.