```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A rooted supersaturation argument proves the conjecture whenever every base component split across the extension-vertex slots has uniformly bounded order, with a bounded-modulator generalization.",
  "would_publish": false,
  "caveats": "The argument does not handle an unbounded weak component spanning several slots; novelty of this elementary partial case has not been checked."
}
```

# Statement and notation

All digraph embeddings below are non-induced. Let \(u(H)\) denote the least \(N\) such that every tournament of order at least \(N\) contains \(H\). Thus a family \(\mathcal F\) is linearly unavoidable if there is \(c\) such that
\[
u(F)\le c|V(F)|\qquad(F\in\mathcal F).
\]

The following partial result applies somewhat more generally than the source definition of a \(k\)-extension. If that definition requires the added vertices to be universal, it is a special case.

## Theorem 1: bounded split components

Fix \(k,s\ge 0\), and let \(\mathcal F\) be linearly unavoidable. There is a constant \(C=C(\mathcal F,k,s)\) with the following property.

Let \(D\) be an acyclic digraph, let \(X\subseteq V(D)\) with \(|X|\le k\), and suppose
\[
F=D-X\in\mathcal F.
\]
Suppose \(D\) has a topological ordering \(\prec\) such that every weak component of \(F\) whose vertices lie in more than one interval determined by \(X\) has order at most \(s\). Then
\[
u(D)\le C|V(D)|.
\]

Here, if \(x_1\prec\cdots\prec x_m\) are the vertices of \(X\), the \(m+1\) intervals are
\[
(-\infty,x_1),\ (x_1,x_2),\ldots,(x_m,\infty).
\]

Thus the conjecture holds in particular when no weak component of \(F\) is split by the added vertices.

There is also the following bounded-modulator version.

## Theorem 2: bounded modulator

Fix \(k,a,s\ge0\). The conclusion of Theorem 1 remains valid if there is a set
\[
Z\subseteq V(F),\qquad |Z|\le a,
\]
such that every weak component of \(F-Z\) meeting more than one interval determined by \(X\cup Z\) in some topological ordering of \(D\) has order at most \(s\). The constant may additionally depend on \(a\).

Theorem 1 is the case \(a=0\).

# A rooted packing lemma

The proof uses the following elementary supersaturation statement.

## Lemma 3

Let \(Q\) be a fixed acyclic digraph on \(q\) vertices, with an ordered distinguished root set
\[
R=(r_1,\ldots,r_p),\qquad p<q.
\]
There is a constant \(B_Q\) such that, for every \(L\ge1\), every tournament on at least \(B_QL\) vertices contains embeddings
\[
\phi_1,\ldots,\phi_L:Q\hookrightarrow T
\]
such that

1. \(\phi_i(r_j)=\phi_{i'}(r_j)\) for all \(i,i'\) and all \(j\); and
2. the sets \(\phi_i(V(Q)\setminus R)\) are pairwise disjoint.

### Proof

Set
\[
M=2^{q-1}.
\]
Every tournament of order \(M\) contains a transitive subtournament of order \(q\), and hence contains \(Q\), since \(Q\) is acyclic.

Let \(T\) have order \(N\ge M\), and let \(\mathcal U\) be the collection of \(q\)-subsets of \(V(T)\) supporting a copy of \(Q\). Double-counting pairs \((S,U)\) with
\[
|S|=M,\quad U\in\mathcal U,\quad U\subseteq S
\]
gives
\[
|\mathcal U|
 \ge
 \frac{\binom NM}{\binom{N-q}{M-q}}
 =
 \frac{\binom Nq}{\binom Mq}.
\]
Choose one embedding of \(Q\) on every support \(U\in\mathcal U\). There are at most \(N^p\) possible ordered images of the roots, so some ordered root image occurs for at least
\[
e\ge \frac{\binom Nq}{\binom Mq N^p}
\]
of the chosen embeddings.

Put \(d=q-p\). For \(N\ge2q\),
\[
\binom Nq\ge \frac{(N/2)^q}{q!},
\]
and hence
\[
e\ge
\frac{N^d}{A_Q},
\qquad
A_Q:=2^q q!\binom Mq.
\]

Take the \(d\)-sets consisting of the non-root images of these embeddings. They form a simple \(d\)-uniform hypergraph. Any one edge intersects at most
\[
d\binom{N-1}{d-1}\le dN^{d-1}
\]
edges. Greedy matching therefore gives at least
\[
\frac{e}{dN^{d-1}}
\ge
\frac{N}{A_Qd}
\]
pairwise disjoint non-root sets.

Thus one may take, for example,
\[
B_Q=\max\{M,2q,A_Qd\}.
\]
This proves the lemma. \(\square\)

# Proof of Theorem 2

Let \(c\ge1\) satisfy
\[
u(F)\le c|V(F)|\qquad(F\in\mathcal F).
\]
Fix \(D,X,Z\) as in Theorem 2, and put
\[
Y=X\cup Z,\qquad |Y|=p\le k+a.
\]
Fix the asserted topological ordering, and write
\[
y_1\prec y_2\prec\cdots\prec y_p.
\]
A vertex has slot \(i\in\{0,\ldots,p\}\) if it lies after \(y_i\) and before \(y_{i+1}\), with the evident endpoint conventions.

We construct a fixed acyclic rooted template \(Q_{p,s}\).

## The template

Its roots are \(y_1,\ldots,y_p\), with all arcs
\[
y_i\to y_j\qquad(i<j).
\]

For every slot \(i\in\{0,\ldots,p\}\), add one reservoir vertex \(z_i\), with
\[
y_h\to z_i \quad\Longleftrightarrow\quad h\le i.
\]

For every \(1\le r\le s\) and every nondecreasing sequence
\[
\tau=(t_1,\ldots,t_r),\qquad 0\le t_1\le\cdots\le t_r\le p,
\]
add a petal
\[
P_\tau=\{v^\tau_1,\ldots,v^\tau_r\}.
\]
Put
\[
v^\tau_i\to v^\tau_j\qquad(i<j),
\]
and give \(v^\tau_j\) the root incidences appropriate to slot \(t_j\):
\[
y_h\to v^\tau_j \quad\Longleftrightarrow\quad h\le t_j.
\]
No arcs are required between distinct petals, between petals and reservoir vertices, or between distinct reservoir vertices.

This digraph is acyclic: order everything slot by slot, preserving the order inside each petal. Its order is the fixed number
\[
q_{p,s}
=
p+(p+1)+
\sum_{r=1}^{s}r\binom{p+r}{r}.
\]

Let \(B_{p,s}\) be the constant supplied by Lemma 3 for this rooted template, and set
\[
B=\max_{0\le p\le k+a} B_{p,s}.
\]

## Finding common roots and reservoirs

Write \(n=|V(F)|\), and set
\[
L=\lceil cn\rceil.
\]
In every tournament \(T\) of order at least \(BL\), Lemma 3 gives \(L\) copies
\[
\phi_1,\ldots,\phi_L
\]
of \(Q_{p,s}\), all sharing the same root images, and otherwise pairwise disjoint.

Map \(Y\) to these common roots in topological order. For every slot \(i\), define
\[
S_i=\{\phi_j(z_i):1\le j\le L\}.
\]
Then \(|S_i|=L\), the sets \(S_i\) are pairwise disjoint, and every vertex of \(S_i\) has the required orientation to every root in \(Y\).

## Embedding the large nonsplit components

For each slot \(i\), let \(F_i\) be the union of all weak components of \(F-Z\) lying entirely in slot \(i\) and not designated as bounded split components.

Since \(F_i\) is a subdigraph of \(F\),
\[
u(F_i)\le u(F)\le cn\le L.
\]
Consequently \(T[S_i]\) contains \(F_i\).

These embeddings can be chosen independently. There are no arcs in \(F-Z\) between different weak components, and all arcs between \(F_i\) and \(Y\) have the correct orientation because the relevant vertices lie in slot \(i\).

## Embedding the bounded split components

Let \(C\) be a weak component of \(F-Z\) meeting more than one slot. By hypothesis,
\[
r:=|V(C)|\le s.
\]
List its vertices in the chosen topological order:
\[
c_1\prec\cdots\prec c_r,
\]
and let \(t_j\) be the slot containing \(c_j\). Then
\[
(t_1,\ldots,t_r)
\]
is a nondecreasing sequence and hence is represented by a petal \(P_\tau\) in \(Q_{p,s}\).

Assign distinct rooted copies \(\phi_j(Q_{p,s})\) to the split components. This is possible because the number of such components is at most \(n\le L\). Map
\[
c_\ell\longmapsto \phi_j(v^\tau_\ell).
\]
The petal is transitive in topological order, so it contains every arc of \(C\), and its incidences to \(Y\) agree with those of \(C\). Different residual weak components have no arcs between them.

Combining the root map, the embeddings into the reservoirs, and these petal embeddings yields a copy of \(D\).

Finally,
\[
BL\le B(c+1)n\le B(c+1)|V(D)|.
\]
The finitely many cases \(n=0\) can be absorbed into the constant. This proves Theorem 2 and hence Theorem 1. \(\square\)

# Consequences

### 1. Component-respecting extensions

If no weak component of \(F\) is split by the extension vertices, take \(a=s=0\). Hence every fixed \(k\)-extension operation which inserts the new vertices only between weak components preserves linear unavoidability.

For \(k=1\), this says that if the added vertex lies topologically between whole weak components of \(F\), the resulting family is linearly unavoidable.

### 2. Bases with bounded weak-component order

Fix \(s\). The family of all acyclic digraphs whose weak components have order at most \(s\) is itself linearly unavoidable. Indeed, every tournament on \(2^{s-1}\) vertices contains a transitive \(s\)-vertex tournament, hence every acyclic digraph of order at most \(s\). Allocating one such block to every component gives a linear bound.

Every component then automatically satisfies the bounded-split hypothesis. Therefore:

> For every fixed \(k,s\), all \(k\)-extensions of acyclic digraphs whose weak components have order at most \(s\) are linearly unavoidable.

This includes, for example, arbitrary disjoint unions of transitive triangles, which are not oriented forests.

### 3. Bounded topological modulators

Taking \(s=0\) in Theorem 2 shows that the conjecture holds whenever deleting a bounded set \(Z\) makes every remaining weak component lie wholly within one interval determined by \(X\cup Z\).

# Remaining gap

The general conjecture permits a weak component \(C\) of unbounded order whose vertices occupy several slots. The reservoir argument embeds the portions of \(C\) in different slots independently, but then does not enforce the arcs of \(C\) running between those portions.

One could place all of \(C\) into a petal, but then the template \(Q\) would have order growing with \(|C|\). The constant in Lemma 3 would consequently depend exponentially or worse on \(|C|\), destroying linearity. Ordinary linear unavoidability of \(F\) gives an unrooted copy of \(F\); it does not directly give a copy respecting a prescribed slot profile around a common set of extension vertices.

Thus the proof isolates, but does not solve, the central unresolved case: an added vertex cutting through an arbitrarily large weak component.