```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A quantitative reversal argument proves the conjecture for cyclic compositions of transitive tournaments, including tournaments with three cyclically ordered transitive modules.",
  "would_publish": false,
  "caveats": "This is a self-contained special case, with no novelty claim; the catalog's reported general disproof is not independently verified here."
}
```

## 1. Scope and literature caveat

The updated catalog supplied in the question reports that the general conjecture has already been disproved for simple oriented graphs. I do not have an independently checked construction from that report, so I will not manufacture one or present the report as a self-contained disproof. The verdict above refers to the partial result proved below. The unrestricted tournament formulation is not settled here.

Throughout, graphs are finite and **oriented**: there are no loops, parallel arcs, or pairs of oppositely directed arcs. A directed cycle is vertex-simple and is counted up to cyclic rotation.

The main partial result gives an explicit arc and a quantitative lower bound on the reduction in cycle count.

## 2. The exact effect of an arc reversal

Write \(c(D)\) for the number of directed cycles of \(D\). For an arc \(e=uv\), let
\[
D^e=(D-e)+vu.
\]
For distinct vertices \(x,y\), let \(p_H(x,y)\) denote the number of vertex-simple directed \(x\)-to-\(y\) paths in \(H\).

Then
\[
\boxed{\quad
c(D^e)-c(D)
=
p_{D-e}(u,v)-p_{D-e}(v,u).
\quad}                                                    \tag{1}
\]

Indeed:

* The destroyed cycles are exactly those containing \(uv\). Deleting that arc gives a bijection with the directed \(v\)-to-\(u\) paths in \(D-e\).
* The created cycles are exactly those containing the new arc \(vu\). Deleting it gives a bijection with the directed \(u\)-to-\(v\) paths in \(D-e\).
* All other cycles are unchanged.

Thus a useful proof strategy is to inject the forward alternative paths into the reverse paths, and then exhibit reverse paths outside the image.

## 3. A quantitative positive theorem

### Construction

Let \(k\geq 3\), and let
\[
V_0,V_1,\ldots,V_{k-1}
\]
be disjoint nonempty vertex sets, with \(|V_i|=n_i\). Construct \(D\) as follows:

1. Each \(D[V_i]\) is a transitive tournament, with a fixed linear ordering.
2. Every possible arc from \(V_i\) to \(V_{i+1}\) is present, with indices modulo \(k\).
3. There are no other interclass arcs.

For \(k=3\), this construction is a tournament: it consists of three transitive modules oriented cyclically. For larger \(k\), it is an oriented graph, generally not a tournament.

Choosing one vertex from each class gives a directed cycle, so \(D\) is not acyclic.

### Theorem

For each \(i\), let \(u\) be the last vertex in the transitive ordering of \(V_i\), and let \(v\) be the first vertex in the ordering of \(V_{i+1}\). Then
\[
c(D)-c(D^{uv})
\ \geq\
\prod_{j\notin\{i,i+1\}}\left(2^{n_j}-1\right)
\ >0.                                                     \tag{2}
\]

Consequently, every graph in this class satisfies Ádám’s conjecture.

### Proof

By cyclically relabelling the classes, take \(i=0\). Put
\[
H=D-uv,
\]
and let \(\mathcal F\) and \(\mathcal R\) be the sets of directed simple \(u\)-to-\(v\) and \(v\)-to-\(u\) paths in \(H\), respectively.

We first construct an injection
\[
\Phi:\mathcal F\longrightarrow\mathcal R.
\]

Take
\[
P=(u,x_1,\ldots,x_r,v)\in\mathcal F.
\]
Because \(uv\) has been deleted, this path has internal vertices.

Since \(u\) is last in the ordering of \(V_0\), it has no out-neighbour inside \(V_0\). Its out-neighbours all belong to \(V_1\). Hence
\[
x_1\in V_1\setminus\{v\}.
\]
Similarly, since \(v\) is first in the ordering of \(V_1\), all its in-neighbours belong to \(V_0\). Thus
\[
x_r\in V_0\setminus\{u\}.
\]

The transitive orderings therefore give the arcs
\[
vx_1,\qquad x_ru.
\]
Consequently,
\[
\Phi(P)=(v,x_1,\ldots,x_r,u)
\]
is a directed simple path in \(H\). The map is injective because it preserves the complete ordered list of internal vertices.

Next we exhibit reverse paths outside its image.

For every \(j=2,\ldots,k-1\), choose a nonempty subset \(S_j\subseteq V_j\), and list its vertices in their transitive order. Concatenating these lists gives a path
\[
v,\ S_2,\ S_3,\ \ldots,\ S_{k-1},\ u.                    \tag{3}
\]
All required arcs exist by construction, and the path is simple.

There are exactly
\[
M=\prod_{j=2}^{k-1}(2^{n_j}-1)
\]
such paths. Every one starts, after \(v\), in \(V_2\). By contrast, every path in the image of \(\Phi\) starts, after \(v\), in \(V_1\setminus\{v\}\). Thus none of the paths in (3) lies in the image.

It follows that
\[
|\mathcal R|\geq |\mathcal F|+M.
\]
Applying (1),
\[
c(D^{uv})-c(D)
=|\mathcal F|-|\mathcal R|
\leq -M,
\]
which proves (2).

The argument also covers singleton classes. In those cases \(\mathcal F\) may be empty, but the displayed family of unmatched reverse paths remains nonempty. \(\square\)

### Tournament corollary

Suppose a tournament admits a partition into nonempty transitive subtournaments \(A,B,C\), with
\[
A\longrightarrow B\longrightarrow C\longrightarrow A.
\]
Let \(u\) be last in \(A\), and \(v\) first in \(B\). Reversing \(uv\) decreases the number of directed cycles by at least
\[
2^{|C|}-1.
\]

This gives arbitrarily large positive instances of the tournament version, including instances whose minimum indegree and outdegree are arbitrarily large.

## 4. A necessary condition for an oriented counterexample

There is also a useful elementary obstruction to counterexamples.

### Proposition

If a cyclic strongly connected component \(S\) of an oriented graph \(D\) contains a vertex of indegree one or outdegree one **within \(S\)**, then some arc reversal strictly decreases \(c(D)\).

### Proof

Suppose \(x\) has precisely one out-neighbour \(y\) in \(S\).

Every directed path in \(D\) between two vertices of \(S\) stays inside \(S\): a vertex on such a path is reachable from \(S\) and can reach \(S\), and therefore belongs to \(S\).

Hence there is no directed \(x\)-to-\(y\) path in \(D-xy\). On the other hand, strong connectivity supplies a directed \(y\)-to-\(x\) path, which necessarily avoids \(xy\). Equation (1) gives
\[
c(D^{xy})-c(D)
=
0-p_{D-xy}(y,x)<0.
\]
The indegree-one case is symmetric. \(\square\)

Thus, in any oriented counterexample, every vertex of every cyclic strongly connected component must have internal indegree and outdegree at least two.

In particular:

> **Every orientation of a \(3\)-degenerate graph satisfies the conjecture.**

To see this, choose a cyclic strongly connected component. Its underlying graph has a vertex of degree at most three. Strong connectivity makes both its internal indegree and outdegree positive; since their sum is at most three, one equals one. The proposition applies.

## 5. What remains missing

The main proof works because the chosen arc has a special endpoint-swapping property: every forward alternative path begins in the head’s transitive module and ends in the tail’s transitive module. Swapping the endpoints therefore preserves directedness, while leaving explicitly countable reverse paths unmatched.

An arbitrary tournament need not have such a partition or such an arc. No argument above supplies the required injection in general.

Accordingly, this answer provides:

* a quantitative theorem for a specified infinite class, including a tournament subclass;
* a necessary minimum-semidegree condition on any oriented counterexample;
* but neither an independently verified general counterexample nor a solution of the unrestricted tournament problem.