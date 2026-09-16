```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a quantitative disjoint-union closure theorem for modulators, but do not resolve the unknown connected-target cases.",
  "would_publish": false,
  "caveats": "The closure result may be standard; no novelty claim or new connected chordal case is asserted."
}
```

## 1. Formulation and scope

All graphs are finite and simple, and “\(H\)-free” means having no **induced** subgraph isomorphic to \(H\).

A graph \(H\) **modulates even-hole-free graphs** if, for every integer \(q\geq 1\), there is a finite bound \(b_H(q)\) such that
\[
G\text{ even-hole-free},\qquad \omega(G)\leq q,\qquad G\text{ \(H\)-free}
\quad\Longrightarrow\quad
\operatorname{tw}(G)\leq b_H(q).
\]

The conjecture asserts this for every chordal \(H\) with \(\omega(H)\leq 3\).

I do not prove or disprove the full conjecture. The partial result below establishes closure under disjoint unions, with an explicit additive treewidth bound. In fact, it proves a bounded vertex-deletion statement using only the exclusion of induced \(C_4\)'s.

## 2. A bounded-deletion theorem

Write \(\dot\cup\) for disjoint union.

**Theorem.** Let
\[
H=H_1\dot\cup\cdots\dot\cup H_k,
\]
where the \(H_i\) are nonempty graphs, and put \(h=|V(H)|\). For \(q\geq 1\), define
\[
M(q,h)=\left\lfloor\frac{(q-1)^2h^3}{4}\right\rfloor+1,
\qquad
D(q,h)=hM(q,h)-1.
\]
If \(G\) is induced-\(C_4\)-free, \(\omega(G)\leq q\), and \(G\) is \(H\)-free, then there are an index \(i\) and a set \(X\subseteq V(G)\) such that
\[
|X|\leq D(q,h)
\quad\text{and}\quad
G-X\text{ is \(H_i\)-free}.
\]

In particular, the deletion bound depends only on the forbidden graph and the clique bound, not on \(|V(G)|\).

### 2.1. An edge bound

We first prove the estimate
\[
e(J)\leq \frac{q-1}{2}\,n\sqrt{n-1}
\leq \frac{q-1}{2}\,n^{3/2}
\tag{1}
\]
for every induced-\(C_4\)-free graph \(J\) on \(n\geq 1\) vertices with \(\omega(J)\leq q\).

For \(q=1\), the graph is edgeless. Assume \(q\geq 2\), and put \(r=q-1\).

For any nonadjacent vertices \(x,y\), their common neighborhood is a clique: two nonadjacent common neighbors would form an induced \(C_4\) with \(x,y\). Moreover,
\[
|N(x)\cap N(y)|\leq r,
\tag{2}
\]
because adjoining \(x\) to that common-neighbor clique gives a clique.

Let \(d(v)\) be the degree of \(v\), let \(e=e(J)\), and count
\[
T=\sum_{v\in V(J)}
\left(\binom{d(v)}2-e(J[N(v)])\right).
\]
Equivalently, \(T\) counts a nonadjacent pair together with a common neighbor. Thus, by (2),
\[
T\leq r\left(\binom n2-e\right).
\tag{3}
\]

The neighborhood of any vertex has clique number at most \(r\). Turán’s bound therefore gives
\[
e(J[N(v)])
\leq \left(1-\frac1r\right)\frac{d(v)^2}{2}.
\]
Consequently,
\[
T\geq \frac1{2r}\sum_v d(v)^2-e.
\tag{4}
\]
Combining (3) and (4),
\[
\sum_v d(v)^2
\leq r^2n(n-1)-2r(r-1)e
\leq r^2n(n-1).
\]
Cauchy–Schwarz now yields
\[
4e^2=\left(\sum_v d(v)\right)^2
\leq n\sum_v d(v)^2
\leq r^2n^2(n-1),
\]
which proves (1).

### 2.2. Many disjoint copies force anticomplete copies

Set \(M=M(q,h)\). Suppose \(G\) contains \(M\) induced copies of each \(H_i\), with **all \(kM\) copies pairwise vertex-disjoint**. Let their union have vertex set \(U\), so
\[
|U|=Mh.
\]

Independently for each \(i\), choose one of its \(M\) copies uniformly at random. Let \(Z\) count edges between selected copies belonging to different indices \(i\).

An edge between a particular copy of \(H_i\) and a particular copy of \(H_j\), where \(i\neq j\), is counted with probability \(1/M^2\). Edges internal to copies, or between copies of the same type, contribute nothing to \(Z\). Hence (1) gives
\[
\mathbb E Z
\leq \frac{e(G[U])}{M^2}
\leq \frac{q-1}{2}\frac{(Mh)^{3/2}}{M^2}
=\frac{(q-1)h^{3/2}}{2\sqrt M}
<1.
\]
The strict inequality follows from the definition of \(M\); when \(q=1\), the expectation is zero.

Since \(Z\) is a nonnegative integer, some selection has \(Z=0\). Those selected copies are pairwise anticomplete, and therefore induce \(H\).

We have proved:

> \(M\) globally vertex-disjoint induced copies of each \(H_i\) force an induced copy of \(H_1\dot\cup\cdots\dot\cup H_k\).

### 2.3. Completing the deletion argument

Greedily seek \(M\) induced copies of \(H_1\), then \(M\) of \(H_2\), and so on, always avoiding every vertex already used.

The process cannot finish: otherwise the preceding packing argument produces an induced \(H\), contrary to the hypothesis.

At its first failure, suppose the next required graph is \(H_i\). Let \(X\) consist of all vertices used previously. Then \(G-X\) is \(H_i\)-free. Since the process stopped before using all \(Mh\) vertices of the proposed packing, and every \(H_i\) is nonempty,
\[
|X|\leq Mh-1=D(q,h).
\]
This proves the theorem. \(\square\)

## 3. Consequence for modulators

**Corollary.** Suppose each \(H_i\) modulates even-hole-free graphs, with nonnegative bounds \(b_i(q)\). Then
\[
H=H_1\dot\cup\cdots\dot\cup H_k
\]
also modulates even-hole-free graphs. One valid bound is
\[
\boxed{
b_H(q)=
\max_{1\leq i\leq k} b_i(q)
+
h\left(
\left\lfloor\frac{(q-1)^2h^3}{4}\right\rfloor+1
\right)-1.
}
\tag{5}
\]

**Proof.** Let \(G\) be even-hole-free, \(H\)-free, and satisfy \(\omega(G)\leq q\). It is induced-\(C_4\)-free, so the theorem gives \(X\) and \(i\) with
\[
|X|\leq D(q,h),\qquad G-X\text{ \(H_i\)-free}.
\]
The graph \(G-X\) remains even-hole-free and has clique number at most \(q\). Thus
\[
\operatorname{tw}(G-X)\leq b_i(q).
\]
Adding \(X\) to every bag of a tree decomposition gives
\[
\operatorname{tw}(G)
\leq \operatorname{tw}(G-X)+|X|
\leq \max_i b_i(q)+D(q,h).
\]
The same inequality holds when \(G-X\) is empty, using a single bag \(X\). \(\square\)

The reverse implication is immediate: if \(H\) modulates, then every induced subgraph of \(H\), and hence every component of \(H\), modulates.

For a concrete application, taking as input the cone-over-a-forest cases reported in the question, (5) applies to every target
\[
H=\mathop{\dot\bigcup}_{i=1}^{k}(K_1\vee F_i),
\]
where each \(F_i\) is a forest. This includes arbitrarily many disjoint triangles. The closure proof itself is independent of those literature inputs.

## 4. Why this does not settle the connected cases

General chordal targets require more than disjoint unions: triangles and other pieces must be attached along prescribed cliques. The bounded-deletion theorem does **not** extend directly to such attachments.

For example, let \(D\) be the diamond, consisting of two triangles sharing an edge. For every \(s\),
\[
G_s=sK_3
\]
is chordal, even-hole-free, \(D\)-free, and has clique number three. Nevertheless, making \(G_s\) triangle-free requires deleting at least \(s\) vertices. Thus there is no bounded-deletion analogue that replaces “disjoint union of two triangles” by “two triangles sharing an edge.”

The same limitation occurs with connected hosts: connect \(s\) vertex-disjoint triangles by bridges. The resulting graph is still chordal and diamond-free and still requires at least \(s\) deletions to become triangle-free.

These examples have treewidth two, so they are **not** counterexamples to the conjecture. They show precisely why the deletion argument cannot justify the needed clique-attachment step.

**Conclusion.** The quantitative disjoint-union closure theorem is fully proved above. No argument is supplied for the unresolved connected chordal targets, and I have not checked whether this closure observation already appears in the cited literature.