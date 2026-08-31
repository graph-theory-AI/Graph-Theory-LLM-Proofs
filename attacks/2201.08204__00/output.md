```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The Paley graph on 17 vertices is an explicit 6-chromatic example with clique number 3 in which every triangle-free induced subgraph is 3-colorable.",
  "would_publish": false,
  "caveats": "This gives only bounded chromatic number; no family with chromatic number tending to infinity is obtained."
}
```

# Statement and notation

Write
\[
p(G)=\max\{\chi(G[X]):X\subseteq V(G),\ G[X]\text{ is triangle-free}\}.
\]
The question asks whether there are graphs \(G\) with
\[
\omega(G)=3,\qquad p(G)\le 3,
\]
and arbitrarily large chromatic number.

I do not resolve the asymptotic question. I give:

1. an explicit example with \(\chi(G)=6\);
2. arbitrarily large-order blow-ups of this example, still with chromatic number \(6\);
3. a structural sufficient condition for \(p(G)\le3\);
4. an explanation of why the standard Mycielski amplification immediately fails.

## 1. A useful sufficient condition

### Lemma 1
If \(\alpha(G)\le3\), then every triangle-free induced subgraph of \(G\) is 3-colorable.

#### Proof
Suppose that a triangle-free induced subgraph \(H\) of \(G\) is not 3-colorable. Choose an induced subgraph \(J\subseteq H\) minimal by vertices subject to \(\chi(J)\ge4\).

For every \(v\in V(J)\), the graph \(J-v\) is 3-colorable. Hence \(\chi(J)=4\), and \(J\) is 4-vertex-critical. In particular,
\[
\delta(J)\ge3.
\]

Because \(J\) is triangle-free, every neighborhood \(N_J(v)\) is an independent set. Since
\[
\alpha(J)\le\alpha(G)\le3,
\]
we also have \(d_J(v)\le3\) for every \(v\). Thus \(J\) is a connected cubic graph.

Brooks' theorem now gives \(\chi(J)\le3\), unless \(J\) is \(K_4\) or an odd cycle. The first is not triangle-free, and an odd cycle has chromatic number \(3\). This is a contradiction. ∎

The bound \(\alpha(G)\le3\) is only a sufficient condition, but it produces a reasonably large finite example.

## 2. The Paley graph on 17 vertices

Let \(P\) be the graph with vertex set \(\mathbb Z_{17}\), where distinct \(x,y\) are adjacent exactly when
\[
x-y\in Q:=\{\pm1,\pm2,\pm4,\pm8\}
 =\{1,2,4,8,9,13,15,16\}.
\]

### Proposition 2
The graph \(P\) satisfies
\[
\omega(P)=3,\qquad \alpha(P)=3,\qquad \chi(P)=6,\qquad p(P)=3.
\]

#### Proof

**Clique number.** The set \(\{0,1,2\}\) is a triangle, so \(\omega(P)\ge3\).

Translations are automorphisms. Thus, if \(P\) contained a \(K_4\), there would be one containing \(0\), and the other three vertices would form a triangle in \(P[Q]=P[N(0)]\).

The neighborhoods within \(Q\) are:
\[
\begin{array}{c|c}
q&N(q)\cap Q\\ \hline
1&\{2,9,16\}\\
2&\{1,4,15\}\\
4&\{2,8,13\}\\
8&\{4,9,16\}\\
9&\{1,8,13\}\\
13&\{4,9,15\}\\
15&\{2,13,16\}\\
16&\{1,8,15\}.
\end{array}
\]
In every row, the three listed vertices are pairwise nonadjacent. Hence \(P[Q]\) is triangle-free, so \(P\) has no \(K_4\). Therefore \(\omega(P)=3\).

**Independence number.** The number \(3\) is a quadratic nonresidue modulo \(17\), and multiplication by \(3\) maps \(Q\) onto the set of nonzero nonresidues. Consequently,
\[
x\longmapsto 3x
\]
is an isomorphism from \(P\) to its complement. Therefore
\[
\alpha(P)=\omega(P)=3.
\]

**Chromatic number.** Since every color class has at most three vertices,
\[
\chi(P)\ge \left\lceil\frac{17}{3}\right\rceil=6.
\]
Conversely, the following is a partition into six independent sets:
\[
\begin{aligned}
&\{0,3,6\},\quad \{1,4,7\},\quad \{2,5,8\},\\
&\{9,12,15\},\quad \{10,13,16\},\quad \{11,14\}.
\end{aligned}
\]
Indeed, all differences occurring within these sets are congruent to \(\pm3\) or \(\pm6\), which are nonresidues modulo \(17\). Hence \(\chi(P)=6\).

Finally, \(\alpha(P)=3\), so Lemma 1 shows that every triangle-free induced subgraph of \(P\) is 3-colorable. The graph has an induced \(C_5\), for example on
\[
1,2,4,13,9
\]
in this cyclic order, so in fact \(p(P)=3\). ∎

Thus the answer to the finite version of the question is affirmative through chromatic number \(6\).

## 3. Stable blow-ups

The construction gives graphs of arbitrarily large order, although not unbounded chromatic number.

### Proposition 3
Let \(F\) satisfy \(p(F)\le3\). Replace every vertex \(v\in V(F)\) by a nonempty stable set \(B_v\), and make \(B_u\) complete to \(B_v\) exactly when \(uv\in E(F)\). Denote the resulting graph by \(F^\ast\). Then
\[
p(F^\ast)\le3,\qquad
\omega(F^\ast)=\omega(F),\qquad
\chi(F^\ast)=\chi(F).
\]

#### Proof
A clique contains at most one vertex from each bag, and its set of bags is a clique of \(F\). Conversely, choosing one vertex from every bag of a clique of \(F\) gives a clique in \(F^\ast\). Thus the clique numbers agree.

Selecting one vertex from every bag gives an induced copy of \(F\), while a coloring of \(F\) extends by coloring every bag monochromatically. Hence the chromatic numbers agree.

Let \(H\) be a triangle-free induced subgraph of \(F^\ast\), and let
\[
S=\{v:H\cap B_v\ne\varnothing\}.
\]
If \(F[S]\) contained a triangle, selecting one vertex of \(H\) from each corresponding bag would give a triangle in \(H\). Thus \(F[S]\) is triangle-free and is 3-colorable. Coloring every vertex in \(H\cap B_v\) with the color assigned to \(v\) gives a 3-coloring of \(H\). ∎

Applying this to \(P\) gives arbitrarily large graphs with
\[
\omega=3,\qquad \chi=6,\qquad p=3.
\]
It does not increase chromatic number.

## 4. A local structural criterion

A minimal triangle-free non-3-colorable graph necessarily contains a large induced star.

### Proposition 4
Every triangle-free 4-chromatic graph contains an induced \(K_{1,4}\). Consequently, every induced-\(K_{1,4}\)-free graph \(G\) satisfies \(p(G)\le3\).

#### Proof
Let \(J\) be a triangle-free 4-critical graph. If \(\Delta(J)\le3\), Brooks' theorem gives \(\chi(J)\le3\), since \(J\) is neither \(K_4\) nor an odd cycle. Therefore some vertex has at least four neighbors. These neighbors are pairwise nonadjacent because \(J\) is triangle-free, and hence they and their center induce a \(K_{1,4}\).

The second assertion follows by applying this to any hypothetical triangle-free non-3-colorable induced subgraph. ∎

This criterion cannot itself yield an unbounded family. Indeed, if \(G\) is both \(K_4\)-free and induced-\(K_{1,4}\)-free, then \(N(v)\) contains neither a triangle nor an independent set of size four. The elementary Ramsey bound \(R(3,4)=9\) gives
\[
d(v)\le8
\]
for every \(v\), and Brooks' theorem then gives \(\chi(G)\le8\).

Stable blow-ups of \(P\) show that the induced-\(K_{1,4}\)-free condition is far from necessary.

## 5. Why Mycielski amplification fails

The natural attempt to pass from the 6-chromatic example to a 7-chromatic one is to take its Mycielskian. This does not preserve the desired property.

Recall that the Mycielskian \(M(G)\) has original vertices \(v_i\), twins \(u_i\), and an apex \(w\), with
\[
u_iv_j\in E(M(G))\quad\Longleftrightarrow\quad v_iv_j\in E(G),
\]
and \(w\) adjacent to all twins. It satisfies
\[
\omega(M(G))=\omega(G),\qquad
\chi(M(G))=\chi(G)+1.
\]

Moreover, if \(H\) is an induced subgraph of \(G\), then the corresponding originals, twins, and apex induce \(M(H)\) in \(M(G)\).

The Paley graph \(P\) contains the induced cycle
\[
P[\{1,2,4,13,9\}]\cong C_5.
\]
Therefore \(M(P)\) contains an induced copy of \(M(C_5)\). The latter is triangle-free and 4-chromatic. Hence
\[
\omega(M(P))=3,\qquad \chi(M(P))=7,
\]
but
\[
p(M(P))\ge4.
\]

Thus the standard clique-preserving chromatic amplification fails exactly at the next chromatic level.

# Gap

The construction above proves only a finite lower threshold:
\[
\max\{\chi(G):\omega(G)=3,\ p(G)\le3\}\ge6.
\]
Stable blow-ups increase order but not chromatic number. The condition \(\alpha(G)\le3\) cannot yield an unbounded family, since Ramsey's theorem bounds the order of graphs with both clique and independence number at most three. The Mycielski operation does not preserve the property.

I obtain neither:

- a family with \(\chi(G)\to\infty\) and \(p(G)\le3\), nor
- a universal upper bound on \(\chi(G)\) under these hypotheses.

Accordingly, the catalogued question remains open.