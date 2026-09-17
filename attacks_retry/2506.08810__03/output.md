```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "The five-vertex tournament C3[TT2,TT2,1] is a counterexample: every countable tournament avoiding it has a distinct locally finite perturbation that still avoids it.",
  "would_publish": true,
  "caveats": "Perturbations are understood to be nonempty; the argument does not settle the weaker single-arc saturation question."
}
```

# 1. The counterexample

Let \(T_\ast\) be the five-vertex tournament with vertex partition
\[
A=\{a_0,a_1\},\qquad B=\{b_0,b_1\},\qquad \{c\},
\]
and orientations
\[
a_0\to a_1,\qquad b_0\to b_1,\qquad
A\to B\to \{c\}\to A.
\]
Thus
\[
T_\ast=C_3[\mathrm{TT}_2,\mathrm{TT}_2,1].
\]
Here, an arrow between sets means that all arcs between those sets have the indicated direction.

This tournament is nontransitive. I will prove the following, which directly contradicts the conjecture.

## Theorem
For every countably infinite \(T_\ast\)-free tournament \(S\), there is a \(T_\ast\)-free tournament \(S'\ne S\) on the same vertex set such that the pairs whose orientations differ between \(S\) and \(S'\) form a locally finite graph.

The key structural fact is stronger than needed:

> Every countable \(T_\ast\)-free tournament can be made transitive by a locally finite set of arc reversals.

No result from the previous attempt is needed below.

# 2. A criterion for locally finite distance from a transitive tournament

For a tournament \(S\), define an undirected graph \(J(S)\) on \(V(S)\) by declaring \(xy\) to be an edge precisely when the arc between \(x\) and \(y\) belongs to infinitely many directed triangles.

Write
\[
O(x)=N_S^+(x).
\]
For an arc \(x\to y\), its directed-triangle completions are exactly
\[
Z(x,y)=\{z:y\to z\to x\}.
\]
In particular,
\[
O(y)\setminus O(x)=Z(x,y).
\tag{1}
\]

## Lemma 1
A countable tournament \(S\) differs from some transitive tournament on \(V(S)\) by a locally finite set of arc reversals if and only if \(J(S)\) is locally finite.

### Proof

**Necessity.** Suppose \(L\) is transitive and the change graph \(D=D(S,L)\) is locally finite.

If \(xy\notin E(D)\), then every directed triangle \(xyz\) of \(S\) must have \(xz\in E(D)\) or \(yz\in E(D)\): otherwise that triangle would also occur in \(L\). Thus there are only finitely many directed triangles of \(S\) containing \(xy\). Consequently,
\[
J(S)\subseteq D,
\]
so \(J(S)\) is locally finite.

**Sufficiency.** Suppose \(J(S)\) is locally finite. For sets \(X,Y\), write
\[
X\subseteq^\ast Y
\quad\Longleftrightarrow\quad
X\setminus Y\text{ is finite}.
\]
Define an equivalence relation on \(V(S)\) by
\[
x\sim y
\quad\Longleftrightarrow\quad
O(x)\mathbin{\triangle}O(y)\text{ is finite}.
\]

On the equivalence classes, reverse almost-inclusion of outneighbourhoods defines a partial order: a class \(C\) precedes a distinct class \(D\) when
\[
O(y)\subseteq^\ast O(x)
\qquad(x\in C,\ y\in D).
\]
This is well-defined, and antisymmetry follows from the definition of \(\sim\). Choose a linear extension of this partial order.

If \(x\to y\) and \(xy\notin E(J(S))\), then (1) gives
\[
O(y)\subseteq^\ast O(x).
\]
Therefore, if \(x\) and \(y\) belong to different equivalence classes, their original orientation agrees with the chosen class order. Hence:

\[
\text{Every incorrectly oriented pair between classes belongs to }J(S).
\tag{2}
\]

It remains to order each equivalence class with only locally finite discrepancies.

Fix a class \(C\), choose \(r\in C\), and partition it as
\[
C=C^-\cup\{r\}\cup C^+,
\]
where
\[
C^-=\{x\in C:x\to r\},
\qquad
C^+=\{x\in C:r\to x\}.
\]
For every \(x\in C\), the sets \(O(x)\) and \(O(r)\) differ finitely. It follows that:

- every vertex of \(C^-\) has finite outdegree within \(C^-\);
- every vertex of \(C^+\) has finite indegree within \(C^+\);
- the pairs disagreeing with the orientation \(C^-\to C^+\) form a locally finite graph.

Enumerate \(C^-\) and \(C^+\), using finite enumerations when appropriate. Order \(C^-\) in reverse enumeration order and \(C^+\) in enumeration order, and concatenate them as
\[
C^- \;<\; r \;<\; C^+.
\tag{3}
\]

To check local finiteness within \(C^-\), consider its \(i\)-th enumerated vertex. Among vertices enumerated before it, there are only \(i\) possible discrepancies; among vertices enumerated after it, discrepancies are contained in its finite outneighbourhood in \(C^-\). The analogous argument for \(C^+\) uses finite indegree. Together with the third bullet above and the exact orientations through \(r\), this proves that the discrepancies inside \(C\) are locally finite.

Finally, order all vertices first by the chosen class order and then by the orders (3). Let \(L\) be the resulting transitive tournament. By (2), its cross-class discrepancies with \(S\) lie in the locally finite graph \(J(S)\); its within-class discrepancies are locally finite by construction. Each vertex therefore belongs to only finitely many changed pairs. ∎

# 3. Avoiding \(T_\ast\) forces \(J(S)\) to have maximum degree at most two

For an arc \(x\to y\), also define
\[
P(x,y)=\{p:x\to p\to y\}.
\]
These are the vertices that would complete a directed triangle if \(xy\) were reversed.

## Lemma 2
If \(S\) is \(T_\ast\)-free and \(x\to y\) has \(P(x,y)\ne\varnothing\), then
\[
|Z(x,y)|\le 2.
\]

### Proof
Choose \(p\in P(x,y)\). Suppose that \(Z(x,y)\) contains three vertices. Among them, two, say \(z_1,z_2\), have the same orientation relative to \(p\).

If \(p\to z_1,z_2\), then
\[
\{y,p\}\ \longrightarrow\ \{z_1,z_2\}\
\longrightarrow\ \{x\}\ \longrightarrow\ \{y,p\}.
\]
These five vertices induce \(T_\ast\).

If \(z_1,z_2\to p\), then
\[
\{z_1,z_2\}\ \longrightarrow\ \{x,p\}\
\longrightarrow\ \{y\}\ \longrightarrow\ \{z_1,z_2\},
\]
again inducing \(T_\ast\).

In either case, the two-vertex blocks automatically induce transitive tournaments. Both possibilities contradict \(T_\ast\)-freeness. ∎

## Lemma 3
In any tournament, the arcs \(x\to y\) satisfying
\[
P(x,y)=\varnothing
\tag{4}
\]
form an undirected graph of maximum degree at most two.

### Proof
At any vertex \(x\), at most one outgoing arc can satisfy (4). Indeed, if both \(x\to y\) and \(x\to z\) satisfied it, then one of \(y\to z\) and \(z\to y\) holds. In the first case,
\[
x\to y\to z
\]
contradicts \(P(x,z)=\varnothing\); the second case similarly contradicts \(P(x,y)=\varnothing\).

Likewise, at most one incoming arc at \(x\) can satisfy (4). Thus the corresponding undirected degree is at most two. ∎

## Corollary 4
For every \(T_\ast\)-free tournament \(S\),
\[
\Delta(J(S))\le 2.
\]
Consequently, every countable \(T_\ast\)-free tournament is a locally finite perturbation of a transitive tournament.

### Proof
If an arc belongs to infinitely many directed triangles, then \(Z(x,y)\) is infinite. Lemma 2 forces \(P(x,y)=\varnothing\). Therefore \(J(S)\) is a subgraph of the graph in Lemma 3, proving the degree bound. Lemma 1 gives the final assertion. ∎

# 4. Completing the disproof

Let \(S\) be any countably infinite \(T_\ast\)-free tournament.

**Case 1: \(S\) is nontransitive.** By Corollary 4, there is a transitive tournament \(L\) on \(V(S)\) whose change graph with \(S\) is locally finite. Since \(S\) is nontransitive, \(L\ne S\). Since \(T_\ast\) is nontransitive, \(L\) is \(T_\ast\)-free. Take \(S'=L\).

**Case 2: \(S\) is transitive.** Reverse any one arc to obtain \(S'\). Every directed triangle in \(S'\) must contain that reversed arc.

On the other hand, \(T_\ast\) contains the two edge-disjoint directed triangles
\[
c\to a_0\to b_0\to c
\qquad\text{and}\qquad
c\to a_1\to b_1\to c.
\]
They share a vertex but no arc. Thus \(T_\ast\) cannot occur in a tournament in which all directed triangles contain one fixed arc. Therefore \(S'\) is \(T_\ast\)-free, and its change graph with \(S\) consists of one edge.

Both cases produce a distinct \(T_\ast\)-free locally finite perturbation of \(S\). Hence no tournament \(S_{T_\ast}\) as required by the conjecture exists. \(\square\)

The counterexample addresses the full locally finite perturbation formulation, including its intended nonempty-perturbation convention. There is no remaining gap in this disproof; no assertion is made here about the weaker requirement involving only individual arc reversals.