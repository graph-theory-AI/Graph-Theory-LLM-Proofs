```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The supplied path theorem proves the conjecture whenever, in each component of P, the vertices having degree at least three in H lie on a single path.",
  "would_publish": false,
  "caveats": "This is a structural corollary of the supplied path theorem, not a resolution; no novelty claim is made."
}
```

## 1. A partial theorem

All graphs below are finite and simple. An **ideal** is closed under isomorphism and taking induced subgraphs.

A \(P\)-filleting of \(H\) is a subdivision of \(H\) in which the edges of \(P\) remain unsubdivided and every other edge is subdivided at least once. The argument below also forces arbitrarily large lower bounds on the lengths of the latter replacement paths.

The only external result used is the path case, Theorem 2.3 as supplied in the question.

Define the set of **branch vertices**
\[
B(H)=\{v\in V(H):d_H(v)\ge 3\}.
\]
Since \(P\) is a forest, any two vertices connected in \(P\) have a unique \(P\)-path. Define the **protected branch core** \(C=C_H(P)\) by
\[
E(C)=
\bigcup_{\substack{x,y\in B(H),\ x\ne y\\
x,y\text{ connected in }P}}
E(P[x,y]).
\]
We may regard \(C\) as spanning \(V(H)\), with unused vertices isolated.

Thus, in each component of \(P\), the nontrivial part of \(C\) is the minimal subtree connecting its branch vertices of \(H\).

### Partial theorem
Let \(P\) be a forest of \(H\). Suppose \(C_H(P)\) is a linear forest. Then every coherent ideal contains a \(P\)-filleting of \(H\).

More strongly, for every integer \(k\ge2\), it contains such a filleting in which every edge outside \(P\) is replaced by a path of length at least \(k\).

The hypothesis is equivalent to:

> In each component of \(P\), all vertices belonging to \(B(H)\) lie on one path of that component.

In particular, this proves the conjecture:

- whenever \(P\) is a linear forest;
- for every forest \(P\subseteq H\) if \(H\) has at most three branch vertices;
- when \(H=P\) is a forest whose branch vertices, in each component, lie on one path.

The proof has two ingredients: joining protected paths using deletable connectors, and relocating degree-two vertices along subdivision paths.

## 2. Extending the supplied theorem to linear forests

### Lemma 1
Let \(R\) be a linear forest of \(H\), and let \(k\ge2\). Every coherent ideal contains a subdivision \(F\) of \(H\) such that:

1. every edge of \(R\) has replacement length one;
2. every edge of \(H\setminus E(R)\) has replacement length at least \(k\).

### Proof
Add isolated vertices to \(R\) so that it spans \(V(H)\). The empty graph is trivial, so assume \(V(H)\ne\varnothing\).

First replace every edge of \(H\setminus E(R)\) by a path of length \(k\), obtaining a graph \(H_k\). Do not alter the edges of \(R\).

List and orient the path components of \(R\). Join successive components using two-edge paths with fresh internal vertices. Also add one fresh vertex at each end of the resulting path. Let \(Q\) be this single path, and let \(J\) consist of \(H_k\) together with these added connector edges.

In particular:

- \(Q\) contains every original vertex of \(H\);
- its edges belonging to \(H_k\) are exactly the edges of \(R\);
- every connector edge belongs to \(Q\);
- none of the internal vertices introduced in forming \(H_k\) belongs to \(Q\).

Apply the supplied path theorem to \((J,Q)\). The coherent ideal contains a \(Q\)-filleting \(T\) of \(J\).

Delete all the fresh connector vertices. Since their incident edges belonged to \(Q\), those edges were not subdivided; consequently this deletion removes the connector paths completely. What remains is a subdivision of \(H\). Its \(R\)-edges are unchanged, and each other original edge of \(H\) has replacement length at least \(k\).

The remaining graph belongs to the ideal by heredity. \(\square\)

This proof also gives a purely combinatorial fact: for fixed \(H,R,k\), the constructed pair \((J,Q)\) works for **every** \(Q\)-filleting of \(J\).

## 3. Recovering protected terminal portions

The next lemma explains why protected edges outside the branch core need not be supplied directly by the path theorem.

### Lemma 2
Let \(P\) be a forest of \(H\), and put \(C=C_H(P)\). Suppose \(F\) is a subdivision of \(H\) in which:

- every edge of \(C\) has replacement length one;
- every edge outside \(C\) has replacement length at least \(k\), where \(k\ge2\).

Then \(F\) has an induced subgraph that is a \(P\)-filleting of \(H\), with every edge outside \(P\) having replacement length at least \(k\).

### Proof
Fix the given subdivision representation of \(F\). The images of the vertices in \(B(H)\) will remain fixed. We may relocate the images of vertices of degree at most two along the corresponding paths.

#### Decomposition into threads

In a component of \(H\) containing a branch vertex, decompose its edges into maximal chains whose internal vertices have degree two in \(H\). Such a chain has:

- two distinct branch vertices as ends;
- a branch vertex and a leaf as ends; or
- the same branch vertex at both ends, forming a cycle through degree-two vertices.

Call these chains **threads**.

A thread with distinct branch ends belongs entirely to \(C\) exactly when all its edges belong to \(P\). Every other thread has no edge in \(C\).

Indeed, a \(P\)-path between branch vertices cannot stop or leave a thread at an internal degree-two vertex. If it uses a thread, it traverses the whole thread between two distinct branch ends. Conversely, a thread contained in \(P\) with distinct branch ends is itself one of the paths defining \(C\).

We now handle all threads and all remaining components.

#### Threads contained in \(C\)

These already have exactly their original lengths, and all their edges belong to \(P\). Keep them unchanged.

#### Other threads containing an edge outside \(P\)

Let such a thread have \(m\) edges, of which \(p\) belong to \(P\). None of its edges belongs to \(C\), so its corresponding path or closed path in \(F\) has length
\[
L\ge km.
\]

Assign replacement length one to each of its \(p\) protected edges, and initially assign length \(k\) to every other edge. The required total is
\[
p+k(m-p)\le km\le L.
\]
There is at least one edge outside \(P\). Add the entire surplus
\[
L-\bigl(p+k(m-p)\bigr)
\]
to the length assigned to one such edge.

These assignments partition the existing path into replacement paths of exactly the desired lengths. Relabel its internal degree-two vertices accordingly. Nothing is deleted in this case. The branch ends remain fixed.

This also handles a closed thread: because \(P\) is a forest, it cannot contain every edge of that closed thread.

#### Other threads entirely contained in \(P\)

Such a thread cannot have two distinct branch ends, since then it would belong to \(C\). It cannot be closed, since \(P\) is a forest. Therefore it runs from a branch vertex to a leaf.

If it has \(m\) original edges, retain just the first \(m\) edges of its replacement path, starting at the fixed branch end, and delete the remaining terminal portion. Relabel the retained vertices in order. This gives the required unsubdivided pendant path.

#### Components with no branch vertices

A connected graph of maximum degree at most two is an isolated vertex, a path, or a cycle.

- Keep an isolated vertex.
- For a path component having an edge outside \(P\), use the same length reassignment as above.
- For a path component entirely contained in \(P\), retain a subpath of its original length.
- A cycle component has an edge outside \(P\), because \(P\) is a forest. Keep the whole subdivided cycle and reassign its edge lengths cyclically, again using the displayed inequality.

These cases cover every component of \(H\).

Finally, the operations produce an **induced** subgraph of \(F\). We only deleted terminal portions of threads or portions of isolated path components. Different thread interiors have no edges between them, and all shared branch vertices were kept fixed. Relabelling degree-two vertices introduces no graph operation or additional adjacency.

The resulting induced subgraph is the required \(P\)-filleting. \(\square\)

The forest assumption is essential here: an entirely protected cycle cannot generally be shortened by taking an induced subgraph.

### Proof of the partial theorem
When \(C_H(P)\) is a linear forest, apply Lemma 1 with \(R=C_H(P)\), then apply Lemma 2. Both resulting graphs remain in the ideal by heredity. \(\square\)

## 4. A useful consequence: at most three branch vertices

The assertion for graphs with at most three branch vertices deserves an explicit check.

Every leaf of a nontrivial component of \(C_H(P)\) belongs to \(B(H)\). Otherwise that leaf could not lie on a path whose two ends belong to \(B(H)\).

If \(C_H(P)\) were not linear, one of its components would contain a vertex \(v\) of degree at least three. That component would have at least three leaves. Those leaves belong to \(B(H)\), and so does \(v\), because
\[
d_H(v)\ge d_{C_H(P)}(v)\ge3.
\]
Thus \(H\) would have at least four distinct branch vertices.

Consequently:

### Corollary
If \(H\) has at most three vertices of degree at least three, then Conjecture 2.4 holds for every forest \(P\) of \(H\).

The same argument works if each component of \(P\) contains at most three branch vertices of \(H\).

## 5. An exact obstruction to this reduction method

There is a precise reason why the preceding argument does not immediately extend to all forests.

### Proposition
For a forest \(P\subseteq H\), the following are equivalent:

1. \(C_H(P)\) is a linear forest.
2. There exist a graph \(J\) and a path \(Q\subseteq J\) such that **every** \(Q\)-filleting of \(J\) contains an induced \(P\)-filleting of \(H\).

### Proof
The implication \(1\Rightarrow2\) follows from the construction in Lemma 1, with \(R=C_H(P)\) and \(k=2\), followed by Lemma 2.

For the converse, fix any proposed pair \((J,Q)\). Choose
\[
L>\max\{|E(P)|,1\},
\]
and form \(T\) by leaving \(Q\) unchanged and replacing every edge outside \(Q\) by a path of length exactly \(L\). This is a \(Q\)-filleting of \(J\).

Suppose \(T\) contains a \(P\)-filleting \(S\) of \(H\). Every branch vertex of \(H\) has degree at least three in \(S\), so its image must be an original vertex of \(J\): all newly introduced vertices of \(T\) have degree two.

Consider a \(P\)-path between two branch vertices of \(H\). Its image in \(S\) has length at most \(|E(P)|<L\), since none of its edges was subdivided. Its ends are original vertices of \(J\).

Such a path cannot enter the interior of a replacement path for an edge outside \(Q\). If it did, the degree-two internal vertices would force it to traverse that entire replacement path, requiring at least \(L\) edges. Therefore the whole protected path lies in \(Q\).

Taking the union over all such protected paths shows that \(C_H(P)\) embeds as a subgraph of \(Q\). Hence its maximum degree is at most two, and, being a forest, it is linear. \(\square\)

Thus the partial theorem captures exactly what can be obtained by this particular **universal one-model reduction** to the supplied path theorem.

This is not a counterexample to the conjecture: the deliberately constructed long \(Q\)-filleting is not asserted to be coherent.

## 6. What remains unresolved

A concrete case not reached by this argument is
\[
H=K_4,\qquad P=K_{1,3},
\]
where \(P\) consists of the three edges incident with one vertex of \(K_4\). Here every vertex is a branch vertex, so
\[
C_H(P)=P,
\]
which is not linear.

The required filleting has a degree-three vertex adjacent directly to three other degree-three vertices. The proposition shows that no universal extraction from a single path-filleting can force this configuration.

The missing step is therefore substantive: one must exploit coherence to retain a genuinely branching collection of connections between branch vertices. Contracting subdivision paths does not solve this, because ideals need not be closed under contractions.

Accordingly, the argument proves the stated special class but neither proves nor disproves Conjecture 2.4 in general.