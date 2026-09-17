```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove majority 3-colourability when deleting at most six vertices leaves a symmetric digraph, and when the graph of unreciprocated arcs is 3-colourable.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; novelty and optimality of these sufficient conditions are not claimed."
}
```

## 1. Partial results

Work with finite loopless digraphs, allowing both opposite arcs between a pair of vertices. Write
\[
d_X^+(v)=|N^+(v)\cap X|.
\]
A majority colouring satisfies
\[
d^+_{c^{-1}(c(v))}(v)\le \left\lfloor\frac{d^+(v)}2\right\rfloor
\quad\text{for every }v.
\]

Call a digraph **symmetric** if \(uv\) is an arc exactly when \(vu\) is an arc. Let \(H(D)\) be the undirected graph in which \(uv\) is an edge exactly when precisely one of \(uv,vu\) is an arc of \(D\).

I establish the following sufficient conditions.

**Partial theorem.** A digraph \(D\) has a majority \(3\)-colouring if either:

1. there is a set \(S\), with \(|S|\le 6\), such that \(D-S\) is symmetric; or
2. \(\chi(H(D))\le 3\).

The argument also proves directly that **every digraph on at most nine vertices has a majority \(3\)-colouring**.

These are self-contained special-case results, not a resolution of the conjecture. I have not verified whether these formulations already occur in the literature.

The main ingredient is a robust way to combine three suitable induced subdigraphs.

## 2. An auxiliary threshold property

Say that a digraph \(Q\) has property \(\mathcal T\) if, for every integer-valued function \(t\) on \(V(Q)\), there exists \(I\subseteq V(Q)\) such that
\[
\begin{cases}
d_I^+(v)\le t(v),&v\in I,\\
d_I^+(v)\ge t(v)+1,&v\notin I.
\end{cases} \tag{1}
\]
Thresholds may be negative. In particular, \(t(v)<0\) forces \(v\notin I\).

### Lemma 1: Basic examples and closure properties

1. Every symmetric digraph has property \(\mathcal T\).
2. Property \(\mathcal T\) is inherited by induced subdigraphs.
3. A digraph has property \(\mathcal T\) if each of its strongly connected components has it.

**Proof.**

For a symmetric digraph \(Q\), let \(e_Q(I)\) count the unordered adjacent pairs contained in \(I\). Choose \(I\) minimizing
\[
\Phi(I)=2e_Q(I)-\sum_{v\in I}(2t(v)+1).
\]
If \(v\in I\), removing \(v\) changes the potential by
\[
2t(v)+1-2d_I^+(v).
\]
Minimality and integrality imply \(d_I^+(v)\le t(v)\). If \(v\notin I\), adding \(v\) changes it by
\[
2d_I^+(v)-2t(v)-1,
\]
so minimality implies \(d_I^+(v)\ge t(v)+1\).

For induced-subdigraph closure, extend thresholds from \(U\subseteq V(Q)\) by assigning threshold \(-1\) to every vertex outside \(U\). Any resulting set \(I\) lies inside \(U\), and its restriction satisfies (1).

For strongly connected components, process sink components first. When processing a component \(C\), all its out-neighbours outside \(C\) have already been processed. Replace \(t(v)\), for \(v\in C\), by
\[
t(v)-d^+_{I\setminus C}(v),
\]
and apply property \(\mathcal T\) inside \(C\). Later choices cannot affect the inequalities already established. \(\square\)

In particular, acyclic digraphs and all digraphs on at most two vertices have property \(\mathcal T\).

### Lemma 2: The three-vertex case

Every digraph on at most three vertices has property \(\mathcal T\), except possibly the directed \(3\)-cycle. The directed \(3\)-cycle does indeed fail the property.

**Proof.**

Only the three-vertex case needs discussion.

First observe that if \(t(v)<0\), membership of \(v\) can be fixed as “outside”; if \(t(v)\ge d_Q^+(v)\), it can be fixed as “inside”. After fixing \(v\), subtract its contribution from the thresholds of its in-neighbours and solve the remaining two-vertex problem. Thus we may assume
\[
0\le t(v)<d_Q^+(v) \qquad(v\in V(Q)). \tag{2}
\]

By Lemma 1, we need only consider strongly connected \(Q\). If its underlying graph is not a triangle, strong connectivity forces every edge of its underlying path to be bidirected, so \(Q\) is symmetric.

Suppose its underlying graph is a triangle. If it has no bidirected pair, it is the directed \(3\)-cycle. If all three pairs are bidirected, Lemma 1 applies.

For the two remaining cases, use the following complement observation: a set satisfies (1) for thresholds \(t\) exactly when its complement satisfies (1) for thresholds
\[
t'(v)=d_Q^+(v)-1-t(v). \tag{3}
\]

* **Exactly one bidirected pair.** Relabel so that the arcs are
  \[
  a\leftrightarrow b,\qquad b\to c,\qquad c\to a.
  \]
  Under (2), \(t(a)=t(c)=0\), and \(t(b)\in\{0,1\}\). By taking complements if necessary, assume \(t(b)=0\). Then \(I=\{a\}\) satisfies (1).

* **Exactly two bidirected pairs.** Relabel so that the arcs are
  \[
  a\to b,\qquad a\leftrightarrow c,\qquad b\leftrightarrow c.
  \]
  Here \(t(b)=0\), while \(t(a),t(c)\in\{0,1\}\). By (3), we may assume \(t(a)=0\). Then \(I=\{c\}\) satisfies (1), regardless of \(t(c)\).

Finally, the directed \(3\)-cycle fails (1) when every threshold is zero: such an \(I\) would have to be an independent set receiving an arc from every vertex outside it, and no such set exists. \(\square\)

## 3. The three-block construction

**Theorem 3.** Suppose
\[
V(D)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}C
\]
and each of \(D[A],D[B],D[C]\) has property \(\mathcal T\). Then \(D\) has a majority \(3\)-colouring.

**Proof.**

The first step colours \(A\cup B\) so robustly that **every subsequent assignment of colours \(1,2\) to \(C\)** preserves the majority condition on \(A\cup B\).

Put \(S=A\cup B\). For \(v\in S\), define
\[
p(v)=d_S^+(v),\qquad q(v)=d_C^+(v),\qquad
s(v)=\left\lfloor\frac{p(v)-q(v)}2\right\rfloor.
\]

Apply property \(\mathcal T\) in \(D[A]\), with thresholds \(s(v)\), obtaining \(I\subseteq A\). Next apply it in \(D[B]\), with thresholds
\[
s(v)-d_I^+(v),
\]
obtaining \(J\subseteq B\).

Assign colour \(1\) to \(I\), colour \(2\) to \(J\), and colour \(3\) to
\[
R=S\setminus(I\cup J).
\]

For \(v\in I\), property \(\mathcal T\) gives \(d_I^+(v)\le s(v)\). For \(v\in J\), it gives
\[
d_J^+(v)\le s(v)-d_I^+(v)\le s(v).
\]
Thus, even if every out-neighbour of \(v\) in \(C\) receives \(v\)'s colour, its number of same-coloured out-neighbours is at most
\[
s(v)+q(v)
=\left\lfloor\frac{p(v)+q(v)}2\right\rfloor.
\tag{4}
\]

If \(v\in R\cap A\), then \(d_I^+(v)\ge s(v)+1\). If \(v\in R\cap B\), then
\[
d_J^+(v)\ge s(v)-d_I^+(v)+1.
\]
Consequently, every \(v\in R\) satisfies
\[
d_I^+(v)+d_J^+(v)\ge s(v)+1.
\]
Since \(C\) will use no colour \(3\), the number of same-coloured out-neighbours of \(v\in R\) is at most
\[
\begin{aligned}
p(v)-s(v)-1
&=\left\lceil\frac{p(v)+q(v)}2\right\rceil-1\\
&\le \left\lfloor\frac{d^+(v)}2\right\rfloor.
\end{aligned} \tag{5}
\]
This proves the promised robustness.

It remains to colour \(C\). For \(v\in C\), let
\[
p_C(v)=d_C^+(v),
\]
and let \(b_i(v)\) count its out-neighbours in \(S\) already assigned colour \(i\). Thus
\[
d^+(v)=p_C(v)+b_1(v)+b_2(v)+b_3(v).
\]

Apply property \(\mathcal T\) in \(D[C]\), with thresholds
\[
r(v)=\left\lfloor\frac{d^+(v)}2\right\rfloor-b_1(v),
\]
obtaining \(K\subseteq C\). Colour \(K\) with \(1\) and \(C\setminus K\) with \(2\).

For \(v\in K\), the number of same-coloured out-neighbours is at most
\[
b_1(v)+r(v)=\left\lfloor\frac{d^+(v)}2\right\rfloor.
\]
For \(v\in C\setminus K\), it is at most
\[
\begin{aligned}
b_2(v)+p_C(v)-d_K^+(v)
&\le b_2(v)+p_C(v)-r(v)-1\\
&=\left\lceil\frac{d^+(v)}2\right\rceil-b_3(v)-1\\
&\le\left\lfloor\frac{d^+(v)}2\right\rfloor.
\end{aligned}
\]
Together with (4)–(5), this covers every vertex. Negative thresholds and vertices of out-degree zero require no exceptions. \(\square\)

## 4. Deducing the stated special cases

### 4.1. A 3-colourable graph of unreciprocated arcs

Suppose \(\chi(H(D))\le3\), and let \(A,B,C\) be its colour classes. Within each class, every pair has either both opposite arcs or neither. Hence \(D[A],D[B],D[C]\) are symmetric.

Lemma 1 and Theorem 3 prove the second assertion of the partial theorem.

There is no restriction here on arcs between the three blocks. In particular, this condition permits arbitrarily large out-degree and dichromatic number.

### 4.2. A tournament lemma

For the six-exceptional-vertices result, we need a small packing fact.

**Lemma 4.** Every tournament on six vertices can be partitioned into two transitive triples.

**Proof.**

Every tournament on at least four vertices contains a transitive triple: choose two out-neighbours or two in-neighbours of one vertex.

Choose a transitive triple
\[
A=\{a_1,a_2,a_3\},
\qquad a_1\to a_2\to a_3,\quad a_1\to a_3.
\]
Let \(B\) be the complementary triple. If \(B\) is transitive, we are done. Otherwise, \(B\) is a directed cycle.

Consider the nine swaps exchanging \(a\in A\) with \(b\in B\).

For each fixed \(a\), at most one swap makes
\[
(B\setminus\{b\})\cup\{a\}
\]
cyclic. Indeed, the cyclic pairs correspond to arcs of the directed cycle \(B\) going from an out-neighbour of \(a\) to an in-neighbour of \(a\); there is at most one such arc. Thus at least six swaps make the new \(B\)-triple transitive.

For fixed \(b\), at most two swaps make the new \(A\)-triple cyclic. A pair \(a_i,a_j\), \(i<j\), forms a cyclic triple with \(b\) precisely when
\[
b\to a_i,\qquad a_j\to b.
\]
There are at most two such pairs. If there are exactly two, necessarily
\[
b\to a_1,\qquad a_3\to b. \tag{6}
\]

Suppose no swap makes both triples transitive. Then all at least six swaps making the new \(B\)-triple transitive must make the new \(A\)-triple cyclic. Since the latter number is at most six, equality holds throughout. In particular, every \(b\in B\) satisfies (6), so every \(b\) sends an arc to \(a_1\).

But then all three swaps involving \(a_1\) make the new \(B\)-triple transitive. The other two vertices of \(A\) each give at least two such swaps, for a total of at least seven—a contradiction. \(\square\)

### 4.3. Deleting six vertices to obtain symmetry

Suppose \(|S|\le6\) and \(D-S\) is symmetric.

Choose a tournament on \(S\) that agrees with every unreciprocated arc of \(D[S]\): orient pairs that are bidirected or nonadjacent arbitrarily. If necessary, add dummy vertices to obtain a six-vertex tournament.

By Lemma 4, partition this tournament into two transitive triples. Restricting the parts to \(S\) gives
\[
S=A\mathbin{\dot\cup}B,\qquad |A|,|B|\le3.
\]
Neither \(D[A]\) nor \(D[B]\) can be precisely a directed \(3\)-cycle, since all three arcs of such a cycle would have been retained in the tournament. Therefore both have property \(\mathcal T\), by Lemma 2.

The third block \(C=V(D)\setminus S\) is symmetric, so Theorem 3 applies.

This proves the first assertion.

### 4.4. Order at most nine

Every nine-vertex tournament contains a transitive triple; its remaining six vertices split into two transitive triples by Lemma 4.

For any digraph on at most nine vertices, form a tournament retaining its unreciprocated arcs and pad to nine vertices. Restrict the resulting three transitive triples back to the original vertices. Each induced digraph has at most three vertices and is not a directed \(3\)-cycle. Lemma 2 and Theorem 3 therefore give a majority \(3\)-colouring.

The proofs are constructive once the relevant partition or exceptional set is supplied. No computational enumeration is being claimed.

## 5. What remains unresolved

The substantive gap is that an arbitrary digraph need not admit a partition into three induced subdigraphs having property \(\mathcal T\).

This limitation is particularly clear for tournaments. By induced-subdigraph closure and the directed-triangle obstruction, a tournament has property \(\mathcal T\) only if it is transitive. Conversely, transitive tournaments have the property because they are acyclic. Thus, on tournaments, Theorem 3 requires a partition into three transitive subtournaments.

There are tournaments not admitting such a partition. For an explicit example, start with a directed triangle and perform two further iterations of replacing each vertex by a copy of the previous tournament, with inter-copy arcs following a directed triangle. The resulting tournament has \(27\) vertices. Any transitive subtournament meets at most two top-level copies; recursively, it has at most \(2^3=8\) vertices. Three transitive sets therefore cannot cover all \(27\) vertices.

That tournament is **not** a counterexample to majority \(3\)-colourability: colouring its three top-level copies differently gives each vertex only \(4\) same-coloured out-neighbours out of \(13\). It simply demonstrates that the auxiliary decomposition criterion is genuinely insufficient for the full conjecture.

Accordingly, the unrestricted majority \(3\)-colouring problem remains unresolved by this argument.