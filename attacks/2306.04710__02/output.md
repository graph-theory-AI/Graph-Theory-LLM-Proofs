```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the intended oriented-graph convention, I obtain an exact multipartite/link reformulation, an O(sqrt(n)) upper bound, several bounded special cases, and examples of dichromatic number four, but neither a constant bound nor an unbounded counterexample family.",
  "would_publish": false,
  "caveats": "The quantitative bound uses the established fact that Delta(1,2,2) is a hero in tournaments; novelty of these elementary partial results has not been checked."
}
```

# 1. Statement and conventions

Write
\[
H=\Delta(1,2,2).
\]
Thus \(H\) has bags \(A=\{a\}\), \(B=\{b_1,b_2\}\), and \(C=\{c_1,c_2\}\), where \(B,C\) induce transitive tournaments and
\[
A\to B\to C\to A.
\]

The problem asks whether there is an absolute constant \(C\) such that every
\[
\{H,K_1+\vec P_2\}\text{-free oriented graph }D
\]
satisfies \(\vec\chi(D)\le C\).

I use the oriented-graph convention: no loops and no digons. This is necessary for the intended problem. If digons were permitted and induced containment required exact equality of arc sets, bidirected complete graphs would be immediate counterexamples.

I do not resolve the existence of \(C\).

# 2. Reduction to multipartite tournaments

## Lemma 2.1

An oriented graph is induced-\((K_1+\vec P_2)\)-free if and only if its underlying graph is complete multipartite.

### Proof

Define \(x\sim y\) when \(x=y\) or \(x,y\) are nonadjacent. The only issue is transitivity. If \(x\sim y\) and \(y\sim z\), but \(x,z\) are adjacent, then the subdigraph on \(\{x,y,z\}\) consists of one directed edge \(xz\) or \(zx\), together with the isolated vertex \(y\). This is \(K_1+\vec P_2\), a contradiction.

Thus \(\sim\) is an equivalence relation. Its classes are stable sets, and every two vertices in different classes are adjacent. ∎

Consequently the problem is equivalent to:

> Is the dichromatic number of \(H\)-free multipartite tournaments bounded?

Every copy of \(H\), being a tournament, necessarily uses five distinct partite classes.

A useful elementary fact is the following.

## Lemma 2.2

Every shortest directed cycle in a multipartite tournament is either

1. a directed triangle using three partite classes, or
2. a directed \(4\)-cycle alternating between two partite classes.

### Proof

Let
\[
v_1\to v_2\to\cdots\to v_\ell\to v_1
\]
be a shortest directed cycle. If two nonconsecutive vertices belong to different parts, then they are adjacent, and either orientation of that chord produces a shorter directed cycle. Hence every nonconsecutive pair belongs to the same part.

If \(\ell\ge5\), then \(v_1\) is nonconsecutive with both \(v_3\) and \(v_4\). Thus \(v_1,v_3,v_4\) lie in one part, contradicting the arc \(v_3v_4\). Therefore \(\ell\le4\). For \(\ell=4\), the nonconsecutive pairs \(v_1,v_3\) and \(v_2,v_4\) are respectively in the same parts. ∎

Thus a coloring of a multipartite tournament is acyclic exactly when it has no monochromatic directed triangle and no monochromatic alternating directed \(C_4\).

# 3. Exact local form of the forbidden tournament

For a vertex \(v\), define a bipartite graph \(L_v\) with sides
\[
A_v=N^+(v),\qquad B_v=N^-(v),
\]
where \(xy\in E(L_v)\), for \(x\in A_v,y\in B_v\), exactly when \(x\to y\) in \(D\).

## Proposition 3.1

The multipartite tournament \(D\) contains \(H=\Delta(1,2,2)\) if and only if, for some \(v\), the link \(L_v\) contains a \(K_{2,2}\)
\[
\{x_1,x_2\}\times\{y_1,y_2\}
\]
whose four vertices belong to four distinct partite classes.

### Proof

If such a \(K_{2,2}\) exists, then
\[
v\to \{x_1,x_2\}\to\{y_1,y_2\}\to v.
\]
The pairs \(x_1,x_2\) and \(y_1,y_2\) are adjacent because they lie in distinct parts. Whichever way those two arcs are oriented, each pair is a transitive tournament of order two. Hence these five vertices induce \(H\).

Conversely, use the singleton bag of a copy of \(H\) as \(v\), and its two order-two bags as the two sides of the \(K_{2,2}\). ∎

In particular:

## Corollary 3.2

If \(D\) is \(H\)-free, \(x_1,x_2\in N^+(v)\) lie in distinct parts, then
\[
N^-(v)\cap N^+(x_1)\cap N^+(x_2)
\]
is contained in a single partite class.

The symmetric statements obtained by reversing arcs also hold.

Thus every link is \(K_{2,2}\)-free after disregarding \(K_{2,2}\)'s whose one side is contained in a single original part. This “part-rainbow \(K_{2,2}\)-free” condition appears to be the central local obstruction.

# 4. A general sublinear upper bound

It is established in the ordinary tournament-hero theory that \(H=\Delta(1,2,2)\) is a hero in tournaments. Fix an integer \(c_H\) such that every \(H\)-free tournament has dichromatic number at most \(c_H\).

Let the partite classes of \(D\) have sizes
\[
s_1\ge s_2\ge\cdots\ge s_p,
\qquad s_{p+1}=0.
\]

## Theorem 4.1

Every \(n\)-vertex \(H\)-free multipartite tournament satisfies
\[
\vec\chi(D)\le
\min_{0\le h\le p}\bigl(h+c_Hs_{h+1}\bigr).
\tag{4.1}
\]
In particular,
\[
\vec\chi(D)\le 2\sqrt{c_Hn}+c_H.
\tag{4.2}
\]

### Proof

Color each of the \(h\) largest parts with its own color. Every remaining part has at most \(s_{h+1}\) vertices. Partition all remaining vertices into
\[
L_1,\ldots,L_{s_{h+1}}
\]
so that every \(L_j\) contains at most one vertex from each original part. Each \(D[L_j]\) is therefore a tournament. It is \(H\)-free, so it can be colored with at most \(c_H\) colors. Using disjoint palettes for the layers gives (4.1).

For (4.2), choose an integer
\[
t=\left\lceil\sqrt{\frac n{c_H}}\right\rceil.
\]
Color every part of size greater than \(t\) separately. There are at most \(n/t\) such parts. The remaining vertices can be partitioned into \(t\) tournament layers, yielding
\[
\vec\chi(D)\le \frac nt+c_Ht
 \le 2\sqrt{c_Hn}+c_H.
\]
∎

Consequences include:

- bounded maximum part size \(s\) gives \(\vec\chi(D)\le c_Hs\);
- if all but \(r\) parts have size at most \(s\), then
  \[
  \vec\chi(D)\le r+c_Hs;
  \]
- any unbounded counterexample sequence must have both an unbounded number of parts and unbounded part sizes.

This is sublinear but does not imply the required constant bound.

# 5. A bounded-mixedness special case

Call a pair of parts \(P_i,P_j\) **mixed** if neither \(P_i\to P_j\) nor \(P_j\to P_i\) holds uniformly. Let \(M(D)\) be the graph whose vertices are the partite classes, with the mixed pairs as edges.

## Proposition 5.1

\[
\vec\chi(D)\le c_H\,\chi(M(D)).
\]

### Proof

Properly color \(M(D)\). In one color class of \(M(D)\), every pair of original parts is uniformly oriented. Therefore the union of these parts is a stable-set blow-up of a quotient tournament \(Q\).

The quotient \(Q\) is \(H\)-free: a copy of \(H\) in \(Q\) would give a copy in \(D\) by choosing one vertex from each of the corresponding parts. Hence \(\vec\chi(Q)\le c_H\).

A transitive color class of \(Q\) lifts to an acyclic subdigraph of \(D\), since all inter-part arcs follow the corresponding transitive order. Thus the union associated with one color of \(M(D)\) has dichromatic number at most \(c_H\). Using separate palettes proves the result. ∎

Hence the conjecture holds for every subclass in which \(\chi(M(D))\) is bounded. Any negative construction must have mixed-pair graphs of unbounded chromatic number.

# 6. The universal bound, if it exists, is at least four

The restriction to at most four partite classes is completely understood.

## Proposition 6.1

There are \(H\)-free multipartite tournaments of dichromatic number exactly \(4\). Consequently, no positive solution can have universal bound below \(4\).

### Proof

Take four stable sets \(P_1,\dots,P_4\), each of size \(m\), where \(m\) is a sufficiently large multiple of \(3\). Orient every inter-part edge independently and uniformly at random.

There can be no copy of \(H\), since \(H\) requires five distinct partite classes. Also \(\vec\chi(D)\le4\) by coloring the four parts separately.

We show that, with positive probability, no acyclic set has size at least \(4m/3\). Fix a vertex set \(S\), with \(s_i=|S\cap P_i|\), and fix a linear order of \(S\). The probability that this order is a topological order of \(D[S]\) is
\[
2^{-e(S)},\qquad
e(S)=\sum_{i<j}s_is_j.
\]
If \(|S|\ge4m/3\), subject to \(s_i\le m\), the quantity \(e(S)\) is minimized by putting \(m\) vertices in one part and \(m/3\) in another. Hence
\[
e(S)\ge \frac{m^2}{3}.
\]

The number of choices of a set and an order is at most \(2^{4m}(4m)!\). Therefore
\[
\Pr\left(\text{some acyclic }S\text{ has }|S|\ge\frac{4m}{3}\right)
 \le 2^{4m}(4m)!\,2^{-m^2/3},
\]
which tends to zero as \(m\to\infty\).

Thus, for some orientation,
\[
\max\{|S|:D[S]\text{ acyclic}\}<\frac{4m}{3}.
\]
Three acyclic color classes cannot cover all \(4m\) vertices, so \(\vec\chi(D)\ge4\). ∎

Thus the optimal bound for the subclass with at most four parts is exactly four.

# 7. Structure around a directed triangle

Let
\[
a\to b\to c\to a
\]
be a directed triangle, and discard temporarily all vertices in the three parts containing \(a,b,c\). Define the three corner classes
\[
\begin{aligned}
X_a&=\{x:c\to x\to b\},\\
X_b&=\{x:a\to x\to c\},\\
X_c&=\{x:b\to x\to a\}.
\end{aligned}
\]
There is no condition on the relation between \(x\in X_a\) and \(a\), and similarly cyclically.

When writing \(X\to Y\) below, this means every existing arc between distinct-part vertices of \(X,Y\) has that direction.

## Proposition 7.1

If \(D\) is \(H\)-free, then
\[
X_b\to X_a\to X_c\to X_b.
\tag{7.1}
\]

### Proof

Take \(x\in X_b\) and \(y\in X_c\) in distinct parts. If \(x\to y\), then
\[
a\to\{b,x\}\to\{c,y\}\to a
\]
is a copy of \(H\). Hence \(y\to x\), proving \(X_c\to X_b\). The other two relations follow cyclically. ∎

Let \(\sigma(X)\) denote the number of original partite classes meeting \(X\).

## Proposition 7.2

If all three corner classes are nonempty, then at most one of them has support on at least five partite classes. Moreover,
\[
\vec\chi\bigl(D[X_a\cup X_b\cup X_c]\bigr)
 \le
\max\left\{8,\vec\chi(D[X_a]),\vec\chi(D[X_b]),\vec\chi(D[X_c])\right\}.
\tag{7.2}
\]

### Proof

Suppose, for example, that \(X_a,X_b\) each meet at least five parts and choose \(z\in X_c\). Each of \(X_a,X_b\) meets at least four parts other than the part of \(z\). Choose two parts meeting \(X_b\), and then two parts meeting \(X_a\) avoiding the first two and the part of \(z\). Selecting one vertex from each chosen part gives an arc in \(X_b\), an arc in \(X_a\), and the singleton \(z\). By (7.1),
\[
z\to X_b\to X_a\to z,
\]
so these five vertices induce \(H\), a contradiction.

Thus, when all three classes are nonempty, at least two of them are supported on at most four parts and hence have dichromatic number at most four.

Choose the possibly large class \(X\) and color it optimally. Color each of the other two classes with four colors, using disjoint four-color palettes. A color is then used in \(X\) and in at most one of the two small classes. The arcs between those two sets all point in one direction, so their union in that color is acyclic. This proves (7.2).

If one corner class is empty, the other two are joined in one direction by (7.1), so they can use the same palette and (7.2) again holds. ∎

Vertices outside the three base parts partition into these corner classes and the two uniform classes
\[
U^+=\{x:x\to a,b,c\},\qquad
U^-=\{x:a,b,c\to x\}.
\]
If \(U^+=U^-=\varnothing\), Proposition 7.2 gives the recursive estimate
\[
\vec\chi(D)
 \le
3+\max\left\{8,\vec\chi(D[X_a]),\vec\chi(D[X_b]),\vec\chi(D[X_c])\right\}.
\tag{7.3}
\]

This localizes potentially large dichromatic number to one corner class, but it does not finish an induction: the additive cost from the three base parts can accumulate along a nested sequence, and the two uniform classes are not controlled by (7.1).

# 8. Completion and rainbow reformulation

There is an exact completion formulation which clarifies why the ordinary tournament-hero theorem does not immediately solve the problem.

## Lemma 8.1

For a multipartite tournament \(D\),
\[
\vec\chi(D)
=
\min_Q \vec\chi(Q),
\tag{8.1}
\]
where \(Q\) ranges over tournaments obtained by linearly ordering every part of \(D\) and adding the corresponding transitive arcs inside that part.

### Proof

For every completion \(Q\), deleting the added arcs cannot create a directed cycle, so
\[
\vec\chi(D)\le\vec\chi(Q).
\]

Conversely, let \(A_1,\dots,A_k\) be an optimal acyclic coloring of \(D\), and choose a topological order of each \(D[A_i]\). In each original part \(P\), linearly order the sets \(P\cap A_i\) in arbitrary block order, while preserving within \(P\cap A_i\) the chosen topological order. Complete \(P\) according to this linear order. Then every \(Q[A_i]\) remains acyclic, so \(\vec\chi(Q)\le k\). ∎

In every such completion, the original parts are transitive sets. Moreover, \(D\) is \(H\)-free exactly when every copy of \(H\) in the completion has two vertices in the same original part: there is no part-rainbow copy of \(H\).

Thus the conjecture can be restated as asking whether the minimum tournament chromatic number over these transitive completions is bounded under the absence of a part-rainbow \(H\).

One cannot simply choose an \(H\)-free completion. For example, take four parts
\[
\{a\},\quad \{b_1,b_2\},\quad \{c_1\},\quad\{c_2\},
\]
with
\[
a\to\{b_1,b_2\}\to\{c_1,c_2\}\to a
\]
and an arbitrary arc between \(c_1,c_2\). The multipartite tournament is \(H\)-free because it has only four parts, but either orientation added between \(b_1,b_2\) creates a copy of \(H\).

# 9. Fully specified finite search formulation

For a prescribed part profile, a finite search can be encoded exactly as follows.

- Introduce one Boolean orientation variable for every pair of vertices in distinct parts.
- For every choice of five vertices in distinct parts, every singleton \(a\), and every ordered partition of the other four vertices into pairs \(B,C\), add the clause forbidding
  \[
  a\to B,\qquad B\to C,\qquad C\to a.
  \]
  The internal arcs of \(B,C\) need not be specified.
- To require \(\vec\chi(D)>k\), enumerate every map \(f:V(D)\to[k]\). For each \(f\), require at least one monochromatic directed triangle or one monochromatic alternating directed \(C_4\). Lemma 2.2 shows that these are exactly the obstructions to acyclicity.

Equivalently, this is an \(\exists\forall\)-QBF with existential orientation variables and universal color variables. I have not run this search, so I claim no computational data.

# 10. Remaining gap

The results above narrow a possible negative family considerably. Such a family must simultaneously have:

1. an unbounded number of parts;
2. unbounded part sizes;
3. mixed-pair graphs of unbounded chromatic number;
4. every triangle link part-rainbow-\(K_{2,2}\)-free;
5. no decomposition allowing the one-large-corner argument to terminate with bounded depth.

The unresolved issue is controlling many large, nonuniform bipartite orientations whose \(K_{2,2}\)'s are systematically hidden inside original parts. Neither the layer bound nor the local link and corner structure yields an order-independent constant. Thus the hero status of \(\Delta(1,2,2)\) remains unresolved here.