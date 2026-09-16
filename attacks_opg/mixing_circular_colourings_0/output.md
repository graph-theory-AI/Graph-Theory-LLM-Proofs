```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For an n-vertex graph with an edge, the circular mixing threshold is rational, with reduced numerator at most n+1.",
  "would_publish": true,
  "caveats": "Finite loopless graphs; edgeless graphs require the usual lower-end normalization. Integrality and attainment are not established."
}
```

# A finite set of possible circular mixing thresholds

Write \(\mathcal R_{k,q}(G)\) for the graph whose vertices are the \((k,q)\)-colourings of \(G\), with two colourings adjacent when they differ at exactly one vertex. Thus mixing means that this graph is nonempty and connected.

For \(N\ge 2\), define
\[
\mathcal E_N
=
\left\{\frac ab:\ a,b\in\mathbb Z_{>0},\quad 2b\le a\le N\right\}.
\]

I prove the following stronger statement.

**Theorem.** Let \(G\) be a finite loopless graph with \(n\) vertices and at least one edge. Then
\[
\boxed{\mathfrak M_c(G)\in\mathcal E_{n+1}.}
\]
In particular, \(\mathfrak M_c(G)\) is rational, and its reduced numerator is at most \(n+1\).

The main point is that, outside a finite rational set, colourings with a fixed orientation of the edges form a connected reconfiguration class. Connections between these classes can then be tested using systems of difference constraints on at most \(n+1\) variables.

## 1. Connectivity of integer difference-constraint regions

We first need an elementary lemma.

**Lemma 1.** Let
\[
P=\left\{x\in\mathbb Z^s:
0\le x_i\le K,\quad
x_j-x_i\le c_{ij}\text{ for }(i,j)\in A
\right\},
\]
where all \(c_{ij}\) and \(K\) are integers. Regard \(A\) as a directed graph, with arc \(i\to j\) having weight \(c_{ij}\).

Suppose \(P\ne\varnothing\), and no directed simple cycle in \(A\) has total weight zero. Then the graph on \(P\) allowing a change of \(1\) or \(-1\) in one coordinate at a time is connected.

**Proof.**
First, \(P\) is closed under coordinatewise minimum. Indeed, for \(x,y\in P\), put \(z_i=\min(x_i,y_i)\). If \(z_i=x_i\), then
\[
z_j-z_i\le x_j-x_i\le c_{ij};
\]
the other case follows using \(y\).

It suffices to connect \(x\) to \(z=\min(x,y)\) by successive coordinate decreases. At a current point \(x\ge z\), let
\[
D=\{i:x_i>z_i\}.
\]
A coordinate \(i\in D\) can be decreased by one unless there is a tight outgoing constraint
\[
x_j-x_i=c_{ij}.
\]
The box constraints cannot prevent this decrease because \(x_i>z_i\ge0\).

Moreover, every such blocking coordinate \(j\) belongs to \(D\). Otherwise \(x_j=z_j\), so
\[
z_j-z_i\ge x_j-(x_i-1)=c_{ij}+1,
\]
contrary to \(z\in P\).

If every coordinate in \(D\) were blocked, choosing a blocking arc at each vertex of \(D\) would produce a directed cycle of tight constraints. Summing around it would give total weight zero, a contradiction.

Consequently some coordinate can be decreased. Integrality ensures that every nontight constraint has sufficient slack for a unit decrease. Repeating reaches \(z\), since \(\sum_i(x_i-z_i)\) strictly decreases. Applying the same argument to \(y\) completes the proof. \(\square\)

## 2. Partitioning colourings by edge orientations

Fix \(k,q\in\mathbb Z_{>0}\) with \(k\ge2q\). Every \((k,q)\)-colouring \(f\) induces an orientation \(D_f\) of \(G\): orient \(uv\) from \(u\) to \(v\) when \(f(u)<f(v)\).

For an orientation \(D\), let \(X_D(k,q)\) be the colourings inducing \(D\). These sets partition the colourings of \(G\). If \(u\to v\) is an edge of \(D\), the corresponding constraints are
\[
x_u-x_v\le -q,
\qquad
x_v-x_u\le k-q,
\]
together with \(0\le x_v\le k-1\).

The variable-to-variable constraint graph therefore has arc weights only of the forms
\[
-q,\qquad k-q.
\]
A directed simple cycle of length \(b\), containing \(a\) arcs of weight \(k-q\), has total weight
\[
a(k-q)+(b-a)(-q)=ak-bq.
\]
If this is zero, then \(a\ge1\) and
\[
\frac{k}{q}=\frac ba.
\]
Since \(b\le n\) and \(k/q\ge2\), this ratio belongs to \(\mathcal E_n\).

Lemma 1 consequently gives:

**Lemma 2.** If \(k/q\notin\mathcal E_n\), every nonempty \(X_D(k,q)\) is connected by single-vertex recolourings. In fact, changes of one unit in the numerical colour suffice within \(X_D(k,q)\).

The exclusion of \(\mathcal E_n\) is important: zero-weight cycles can force several coordinates to move together, preventing single-coordinate connectivity.

## 3. Feasibility has only finitely many rational breakpoints

We next determine how the nonemptiness of \(X_D(k,q)\) can depend on the parameters.

**Lemma 3.** Fix an oriented graph \(D\) on \(s\) vertices. The nonemptiness of \(X_D(k,q)\):

1. depends only on the ratio \(k/q\), not on its integer representation; and
2. is constant on each open interval in
   \[
   (2,\infty)\setminus\mathcal E_s.
   \]

**Proof.**
Use the difference-constraint graph above, and add a reference vertex \(*\), with arcs
\[
*\longrightarrow i \text{ of weight }k-1,
\qquad
i\longrightarrow * \text{ of weight }0.
\]
Setting \(x_*=0\) imposes \(0\le x_i\le k-1\).

This integer difference-constraint system is feasible if and only if the augmented graph has no negative directed cycle. For completeness, sufficiency follows by taking shortest-path distances from \(*\). All vertices are reachable; without a negative cycle, these distances are finite integers and satisfy every constraint. The arcs incident with \(*\) ensure that the distances lie between \(0\) and \(k-1\).

It is enough to check simple directed cycles. There are two kinds.

* A cycle avoiding \(*\) has weight
  \[
  ak-bq,\qquad 1\le b\le s,\quad 0\le a\le b.
  \]
  If \(a=0\), it is always negative. Otherwise, nonnegativity is equivalent to
  \[
  \frac{k}{q}\ge\frac ba.
  \]

* A cycle containing \(*\) uses exactly one arc of weight \(k-1\) and one arc of weight \(0\). Its weight is
  \[
  ak-bq-1,\qquad 0\le b\le s-1,\quad 1\le a\le b+1.
  \]
  Since \(ak-bq\) is an integer,
  \[
  ak-bq-1\ge0
  \quad\Longleftrightarrow\quad
  ak-bq>0
  \quad\Longleftrightarrow\quad
  \frac{k}{q}>\frac ba.
  \]

Thus feasibility is determined by finitely many weak or strict comparisons of \(k/q\) with fixed rational numbers. Every comparison point lying in \([2,\infty)\) belongs to \(\mathcal E_s\). This proves both assertions. \(\square\)

The integrality step
\[
ak-bq-1\ge0\iff ak-bq>0
\]
is what removes any apparent dependence on the scale of the pair \((k,q)\).

## 4. Testing transitions between orientation classes

For fixed \(k,q\), construct a finite graph \(Q_{k,q}(G)\) as follows.

* Its vertices are the orientations \(D\) for which \(X_D(k,q)\ne\varnothing\).
* Two distinct orientations \(D,D'\) are adjacent if some colouring in \(X_D(k,q)\) and some colouring in \(X_{D'}(k,q)\) differ at exactly one vertex.

We can test each possible adjacency using another oriented graph, now with \(n+1\) vertices.

Suppose the changed vertex is \(v\). Necessarily \(D,D'\) agree on every edge not incident with \(v\). Replace \(v\) by two nonadjacent twins \(v_0,v_1\), each having the original neighbourhood of \(v\). Orient:

* the edges at \(v_0\) as in \(D\);
* the edges at \(v_1\) as in \(D'\);
* all other edges in their common direction.

A colouring respecting this orientation specifies the unchanged colours on \(V(G)\setminus\{v\}\), the old colour at \(v_0\), and the new colour at \(v_1\). It therefore gives exactly the desired transition.

Conversely, every such transition yields a colouring of this oriented twin graph. Because \(D\ne D'\), at least one incident edge is oppositely oriented, so the two twin colours are automatically different.

Thus adjacency in \(Q_{k,q}(G)\) is determined by finitely many feasibility tests of the type in Lemma 3, on \(n+1\) vertices.

When \(k/q\notin\mathcal E_n\), Lemma 2 says that all nonempty orientation classes are connected. Hence
\[
\mathcal R_{k,q}(G)\text{ is nonempty and connected}
\quad\Longleftrightarrow\quad
Q_{k,q}(G)\text{ is nonempty and connected}.
\]
Indeed, a connected quotient can be lifted by moving within each class to the endpoint of the next transition; the converse follows by projecting a reconfiguration path.

We have proved the central stability statement.

**Proposition 4.** Let \(I\) be a component interval of
\[
(2,\infty)\setminus\mathcal E_{n+1}.
\]
Then either \(G\) is \((k,q)\)-mixing for every pair of positive integers with \(k/q\in I\), or it is \((k,q)\)-mixing for none of those pairs.

**Proof.**
Throughout \(I\), Lemma 3 makes every vertex-feasibility and transition-feasibility test defining \(Q_{k,q}(G)\) constant. Thus the finite graph \(Q_{k,q}(G)\) is unchanged.

Also \(I\cap\mathcal E_n=\varnothing\), so all its nonempty orientation classes are connected by Lemma 2. The quotient criterion now proves the assertion. \(\square\)

No assertion of scale invariance at the exceptional ratios is needed.

## 5. A self-contained upper bound

We also need to know that all sufficiently large ratios are mixing. The same machinery gives
\[
G\text{ is }(k,q)\text{-mixing whenever }k/q\ge n+1.
\]

Indeed, the palette
\[
C=\{0,q,2q,\ldots,nq\}
\]
has \(n+1\) colours, and every two distinct palette colours satisfy the \((k,q)\)-constraint when \(k\ge(n+1)q\).

For any colouring \(f\), its induced orientation \(D_f\) is acyclic, since colours strictly increase along directed edges. A topological ordering therefore gives an injective palette colouring belonging to \(X_{D_f}(k,q)\). Because \(k/q\ge n+1\) lies outside \(\mathcal E_n\), Lemma 2 connects \(f\) to this palette colouring.

Finally, all injective maps from \(V(G)\) into \(C\) are connected by single-vertex moves that preserve injectivity. To reach a target injective map, fix vertices one at a time. If a desired colour is occupied by another, not-yet-fixed vertex, first move that vertex to an unused palette colour. An unused colour always exists because there are \(n+1\) palette colours and only \(n\) vertices.

All these intermediate maps are proper circular colourings. This proves the upper bound, including nonemptiness.

## 6. Extracting the threshold

Define the set of bad ratios by
\[
B_G=
\left\{
r\in\mathbb Q_{\ge2}:
\begin{array}{l}
\text{there exist }k,q\in\mathbb Z_{>0}\text{ with }k/q=r\\
\text{such that }G\text{ is not }(k,q)\text{-mixing}
\end{array}
\right\}.
\]
The existential quantifier accommodates possible dependence on the integer representation at exceptional ratios.

Because \(G\) has an edge, it is not \((2,1)\)-mixing: either it has no proper \(2\)-colouring, or the colours on its nontrivial components cannot change. Thus \(2\in B_G\). Section 5 shows that \(B_G\) has no element at least \(n+1\).

By Proposition 4, on every component interval \(I\) of
\[
(2,\infty)\setminus\mathcal E_{n+1},
\]
either
\[
B_G\cap I=\mathbb Q\cap I
\qquad\text{or}\qquad
B_G\cap I=\varnothing.
\]
At the finitely many points of \(\mathcal E_{n+1}\), arbitrary behaviour is possible and harmless.

Consequently \(B_G\) is a union of selected rational open intervals between consecutive points of \(\mathcal E_{n+1}\), together with a subset of \(\mathcal E_{n+1}\). It follows that
\[
\sup B_G\in\mathcal E_{n+1}.
\]

Finally,
\[
\mathfrak M_c(G)=\sup B_G.
\]
Every rational \(\ell>\sup B_G\) satisfies the defining universal mixing condition, while every \(\ell<\sup B_G\) fails it. Whether the condition holds at equality does not affect the infimum.

This proves the theorem. \(\square\)

## Scope and exceptional cases

The proof does **not** assume that every orientation class is connected. That can fail at ratios in \(\mathcal E_n\), where zero-weight cycles force coordinate differences. Those cases are covered by retaining all exceptional ratios as possible bad points; their detailed behaviour cannot create an irrational supremum.

The argument establishes neither that the threshold is always an integer nor that it is attained.

For edgeless graphs, every colouring reconfiguration graph is connected. Their threshold is therefore the chosen lower endpoint under the usual normalization—for example, \(2\) if thresholds are restricted to \([2,\infty)\). If the displayed definition is read literally with arbitrarily negative \(\ell\), an edgeless graph instead gives \(-\infty\); that is a trivial normalization issue in the quoted statement, separate from the substantive rationality question.