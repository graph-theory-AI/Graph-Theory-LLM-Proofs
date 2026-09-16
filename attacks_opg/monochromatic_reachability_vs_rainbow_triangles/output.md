```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for at most five vertices and for feedback-vertex number at most one, and every minimal counterexample has minimum in- and out-degree at least two.",
  "would_publish": false,
  "caveats": "The general three-colour case is unresolved here; novelty of these self-contained partial results has not been checked."
}
```

# Partial results

Throughout, tournaments are finite and nonempty. Write \(x\leadsto y\) if there is a monochromatic directed path from \(x\) to \(y\), allowing the trivial path when \(x=y\). A **monochromatic-path source** is a vertex \(x\) with \(x\leadsto y\) for every vertex \(y\). The colour may depend on \(y\).

I prove the following.

1. In any vertex-minimal counterexample, monochromatic unreachability has a precise cyclic form, and every vertex has in-degree and out-degree at least two.
2. With **any number of colours**, absence of a rainbow directed triangle guarantees a monochromatic-path source whenever deleting at most one vertex makes the tournament transitive.
3. With **at most four colours**, the conclusion holds on at most five vertices. In fact, the five-vertex obstructions with an unrestricted palette can be classified explicitly: they use exactly five colours.

These do not settle the three-colour conjecture for larger tournaments.

## 1. The cyclic structure of a minimal obstruction

For an edge-coloured tournament \(T\), define its **unreturnable-arc digraph** \(U(T)\) by
\[
xy\in E(U(T))
\quad\Longleftrightarrow\quad
xy\in E(T)\ \text{and}\ y\not\leadsto x.
\]

A vertex \(v\) is a monochromatic-path source precisely when
\[
d^-_{U(T)}(v)=0.
\]
Indeed, if \(v\not\leadsto w\), then the tournament edge must be \(w\to v\), and this edge belongs to \(U(T)\).

### Lemma 1
Suppose \(T\) has no rainbow directed triangle and no monochromatic-path source, but every proper induced subtournament has a monochromatic-path source. Then its vertices can be labelled
\[
v_0,v_1,\ldots,v_{n-1}
\]
cyclically so that
\[
U(T)=v_0v_1\cdots v_{n-1}v_0.
\]
Consequently,
\[
\{w:v_i\leadsto w\}
   =V(T)\setminus\{v_{i-1}\},
\tag{1}
\]
with indices taken modulo \(n\).

#### Proof
Every vertex has positive in-degree in \(U(T)\), so \(U(T)\) contains a directed cycle.

If such a cycle had vertex set \(S\subsetneq V(T)\), then every vertex of \(T[S]\) would fail to reach its predecessor on that cycle monochromatically: such a path does not exist even in \(T\). Thus \(T[S]\) would have no monochromatic-path source, contrary to minimality.

Therefore \(U(T)\) contains a directed Hamilton cycle. Any additional arc of \(U(T)\) would be a chord of this cycle and, together with a suitable segment of the cycle, would produce a shorter directed cycle. This is again impossible. Hence \(U(T)\) is exactly the Hamilton cycle.

The characterization of sources above now gives (1). ∎

The significant point is that a minimal obstruction does not merely have a cycle of unreachability: **each vertex fails to reach exactly one other vertex**.

## 2. A semidegree obstruction

### Lemma 2
Under the hypotheses of Lemma 1,
\[
\delta^+(T)\ge 2
\qquad\text{and}\qquad
\delta^-(T)\ge 2.
\]

#### Proof
The Hamilton cycle in \(U(T)\) already excludes in-degree or out-degree zero.

Suppose that \(x\) has just one out-neighbour, \(y\), and let the colour of \(x\to y\) be \(a\). Let \(p\) be the predecessor of \(x\) in the cycle \(U(T)\).

By (1), \(x\) reaches every vertex except \(p\). Every nontrivial monochromatic path starting at \(x\) begins with \(x\to y\), so all these paths have colour \(a\). In particular,
\[
y\overset{a}{\leadsto} z
\qquad
\text{for every }z\notin\{x,p\}.
\tag{2}
\]

The unique vertex not reachable from \(y\) is \(x\). Thus \(y\) has a monochromatic path to \(p\), say of colour \(b\). Necessarily \(b\ne a\), since otherwise \(x\to y\) could be prepended to obtain a monochromatic path from \(x\) to \(p\).

Let \(z\) be the first vertex after \(y\) on this \(b\)-coloured path. Since \(y\) is the only out-neighbour of \(x\), we have the directed triangle
\[
x\to y\to z\to x.
\]
Its first two edges have distinct colours \(a,b\). Absence of a rainbow directed triangle forces the colour of \(z\to x\) to belong to \(\{a,b\}\).

It cannot be \(b\), because then \(y\to z\to x\) would be monochromatic. Hence \(z\to x\) has colour \(a\).

If \(z\ne p\), equation (2), followed by \(z\to x\), gives an \(a\)-coloured path from \(y\) to \(x\), another contradiction. Therefore \(z=p\), and \(p\to x\) has colour \(a\).

But \(x\) reaches every vertex other than \(p\) in colour \(a\). Prepending \(p\to x\) shows that \(p\) reaches every vertex in colour \(a\), contradicting the assumption that \(T\) has no monochromatic-path source. Thus \(\delta^+(T)\ge2\).

For the in-degree assertion, reverse every arc. Equation (1) becomes the same cyclic condition with the cyclic order reversed, and absence of rainbow directed triangles is preserved. The preceding out-degree argument uses only that cyclic condition, so it applies to the reversed tournament. Hence \(\delta^-(T)\ge2\). ∎

### Corollary 3: a hereditary low-degree special case
Let \(T\) have no rainbow directed triangle, with an arbitrary number of colours. Suppose every nonempty induced subtournament has a vertex whose in-degree or out-degree, within that subtournament, is at most one. Then \(T\) has a monochromatic-path source.

#### Proof
Otherwise, choose a vertex-minimal induced subtournament without such a source and apply Lemma 2. ∎

### Corollary 4: feedback-vertex number at most one
Let \(T\) be an edge-coloured tournament with no rainbow directed triangle. If deleting at most one vertex makes \(T\) transitive, then \(T\) has a monochromatic-path source, regardless of the number of colours.

#### Proof
Let \(q\) be a vertex such that \(T-q\) is transitive.

An induced subtournament not containing \(q\) is transitive and therefore has a vertex of out-degree zero. In an induced subtournament containing \(q\) and at least one other vertex, take the last vertex in the transitive ordering of the vertices other than \(q\). Its only possible out-neighbour is \(q\), so its out-degree is at most one.

Corollary 3 applies. The case in which \(T\) itself is transitive is immediate. ∎

## 3. Complete analysis through five vertices

The semidegree lemma immediately excludes minimal obstructions on at most four vertices. The five-vertex case has additional rigidity.

### Theorem 5
An edge-coloured tournament on at most five vertices, using at most four colours, has either a rainbow directed triangle or a monochromatic-path source.

More precisely, if a five-vertex tournament has neither, with no restriction on the number of colours, then it uses exactly five colours and has one of the two forms described below.

#### Proof

Assume there is no rainbow directed triangle and no monochromatic-path source, and choose a vertex-minimal obstruction.

By Lemma 2 it has at least five vertices. Thus it has exactly five, and every vertex has in-degree and out-degree two. Label the cycle from Lemma 1 as
\[
v_0\to v_1\to v_2\to v_3\to v_4\to v_0.
\]
All indices in this section are modulo five.

Write \(a_i\) for the colour of \(v_i\to v_{i+1}\).

We first record a useful consequence of unreturnability:

> If a directed triangle contains two consecutive edges of \(U(T)\), those two edges have the same colour.

Indeed, for
\[
x\to y\to z\to x
\]
with \(x\to y,y\to z\in U(T)\), the colour of \(z\to x\) cannot equal either of the other two colours: either equality would give a monochromatic return path for one of those two unreturnable arcs. Since the triangle is not rainbow, its first two colours must therefore agree.

### 3.1. The chord orientations are forced

After removing the five cycle edges, every vertex has one remaining incoming and one remaining outgoing edge. The underlying graph of these remaining edges is another five-cycle. Hence they are oriented in one of two ways:
\[
v_i\to v_{i+2}\quad\text{for all }i,
\tag{3}
\]
or
\[
v_{i+2}\to v_i\quad\text{for all }i.
\tag{4}
\]

In case (4), each triangle
\[
v_i\to v_{i+1}\to v_{i+2}\to v_i
\]
contains two consecutive edges of \(U(T)\). The observation above gives
\[
a_i=a_{i+1}
\quad\text{for every }i.
\]
The Hamilton cycle would then be monochromatic, contradicting unreturnability of its edges.

Thus (3) holds. Let \(b_i\) be the colour of \(v_i\to v_{i+2}\).

The path
\[
v_i\to v_{i+2}\to v_{i+4}
\]
would reach the forbidden predecessor of \(v_i\) if its two colours agreed. Therefore
\[
b_i\ne b_{i+2}.
\tag{5}
\]

The directed triangle
\[
v_i\to v_{i+1}\to v_{i+3}\to v_i
\]
has colours \(a_i,b_{i+1},b_{i+3}\). Its latter two colours are distinct by (5), so
\[
a_i\in\{b_{i+1},b_{i+3}\}.
\tag{6}
\]

### 3.2. The choices in (6) must be uniform

Call the choice \(a_i=b_{i+1}\) the first choice, and \(a_i=b_{i+3}\) the second choice. These choices are distinct by (5).

Suppose the second choice occurs at \(i\), while the first occurs at \(i+2\). Then
\[
v_{i+2}\to v_{i+3}\to v_i\to v_{i+1}
\]
is monochromatic, of colour \(b_{i+3}\). It reaches the predecessor of \(v_{i+2}\), contradicting (1).

Thus a second choice at \(i\) forces a second choice at \(i+2\). Repeated addition of two visits all residues modulo five. Consequently, either
\[
a_i=b_{i+1}\quad\text{for every }i,
\tag{7}
\]
or
\[
a_i=b_{i+3}\quad\text{for every }i.
\tag{8}
\]

### 3.3. All five chord colours are distinct

Suppose \(b_i=b_{i+1}\).

Under (7), the path
\[
v_{i-1}\to v_i\to v_{i+1}\to v_{i+3}
\]
is monochromatic. Since \(i+3\equiv(i-1)-1\pmod5\), it reaches the forbidden predecessor of its starting vertex.

Under (8), the path
\[
v_i\to v_{i+2}\to v_{i+3}\to v_{i+4}
\]
is monochromatic and again reaches the forbidden predecessor.

Both are impossible. Hence
\[
b_i\ne b_{i+1}
\quad\text{for every }i.
\tag{9}
\]

Together, (5) and (9) imply that \(b_0,\ldots,b_4\) are pairwise distinct. Equations (7) and (8) show that these are exactly the colours used on all ten edges.

In particular, at most four colours cannot suffice for an obstruction on five vertices. ∎

## 4. The five-colour boundary example

For completeness, the forced five-vertex patterns really do give obstructions when five colours are allowed.

Take vertex set \(\mathbb Z_5\), with edges
\[
i\to i+1,\qquad i\to i+2.
\]
Choose five distinct colours \(b_0,\ldots,b_4\), and set
\[
\operatorname{col}(i\to i+2)=b_i,
\qquad
\operatorname{col}(i\to i+1)=b_{i+1}.
\tag{10}
\]

Every directed triangle has the form
\[
i\to i+1\to i+3\to i.
\]
Its colours under (10) are
\[
b_{i+1},\ b_{i+1},\ b_{i+3},
\]
so it is not rainbow.

For each \(j\), the colour-\(b_j\) edges form exactly the two-edge path
\[
j-1\to j\to j+2.
\]
It follows that
\[
\{w:i\leadsto w\}=\{i,i+1,i+2,i+3\}.
\]
Thus every vertex fails to reach its predecessor, and there is no monochromatic-path source.

The alternative pattern
\[
\operatorname{col}(i\to i+1)=b_{i+3}
\]
works similarly: its colour-\(b_j\) edges form the path \(j\to j+2\to j+3\). This also establishes sufficiency of both forms in the five-vertex classification.

This example is **not** a counterexample to the problem: it uses five colours. Nor does it refute the unrestricted-palette version asking for a rainbow directed cycle of any length, since its directed Hamilton cycle is rainbow.

Its underlying tournament has feedback-vertex number two: every four-vertex induced subtournament contains a directed triangle, while \(\{0,1,2\}\) is transitive. Thus the feedback-one result cannot be extended to feedback two with an unrestricted palette.

## 5. What remains unresolved

For the original three-colour problem, the proved restrictions are:

- a smallest counterexample has at least six vertices;
- every vertex has in-degree and out-degree at least two;
- its unreturnable-arc digraph is exactly a directed Hamilton cycle;
- each vertex monochromatically reaches every vertex except its predecessor on that cycle;
- its feedback-vertex number is at least two.

The five-vertex argument relies crucially on the remaining chord graph being a single cycle, which forces the uniform alternatives (7)–(8). That argument does not cover larger tournaments. In particular, I have not excluded a three-coloured minimal obstruction of order six or more, and I do not claim a proof of the general conjecture.