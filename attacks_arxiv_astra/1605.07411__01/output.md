```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove chi-boundedness for cyclic-triangle-free orientations and, using the quoted TT3-free theorem, bounded chromatic number for all K4-free oriented graphs avoiding a fixed oriented star.",
  "would_publish": false,
  "caveats": "The general conjecture is not proved; the K4-free result uses the source theorem as quoted, and novelty of these special cases is not asserted."
}
```

## 1. Partial results

Throughout, \(\chi(D)\) and \(\omega(D)\) refer to the underlying undirected graph of an oriented graph \(D\), **not** to dichromatic number. Write \(\vec C_3\) for the cyclically oriented triangle and \(TT_3\) for the transitive triangle.

I establish the following two statements.

**Partial theorem.** For every oriented star \(S\):

1. The class of \(S\)-free oriented graphs containing no \(\vec C_3\) is \(\chi\)-bounded. In particular, this holds for acyclic orientations.
2. The \(S\)-free oriented graphs whose underlying graphs are \(K_4\)-free have bounded chromatic number.

The first statement has a self-contained proof below. The second uses precisely the \(TT_3\)-free theorem quoted in the question.

It suffices to work with \(S_{k,k}\), where the center has \(k\) incoming and \(k\) outgoing leaves. Indeed, given \(S\), choose \(k\ge2\) at least as large as each of its two leaf counts. Then \(S\) is an induced subdigraph of \(S_{k,k}\), so every \(S\)-free oriented graph is \(S_{k,k}\)-free.

The main ingredient is a decomposition that applies without any restriction on triangle orientations.

## 2. A local clique-lowering decomposition

Let \(R(a,b)\) be the ordinary Ramsey number: every graph on \(R(a,b)\) vertices contains a clique of size \(a\) or a stable set of size \(b\).

We use the elementary fact that an oriented graph of maximum indegree at most \(d\), or maximum outdegree at most \(d\), has chromatic number at most \(2d+1\). Every induced subgraph has at most \(d\) times its order edges, and hence has a vertex of degree at most \(2d\).

For integers \(k,w\ge2\), define
\[
r=r_k(w)=(w-1)(k-1)+1,
\]
\[
b=b_k(w)=\binom{r}{k}\bigl(R(w,k)-1\bigr),
\]
and
\[
a_k(w)=4R(w,r)-2,
\qquad
q_k(w)=4b_k(w)+1.
\]

### Decomposition lemma

Let \(D\) be \(S_{k,k}\)-free with \(\omega(D)\le w\). There is a partition
\[
V(D)=X\ \dot\cup\ Y\ \dot\cup\ Z_1\ \dot\cup\cdots\dot\cup Z_q,
\qquad q=q_k(w),
\]
such that
\[
\chi(D[X])+\chi(D[Y])\le a_k(w),
\]
and, for every \(i\) and \(v\in Z_i\),
\[
\omega\!\left(D[N^+(v)\cap Z_i]\right)\le w-2,
\qquad
\omega\!\left(D[N^-(v)\cap Z_i]\right)\le w-2.
\tag{1}
\]

Here neighborhoods and clique numbers are taken in the underlying graph when appropriate.

### Proof

Put
\[
X=\{v:\alpha(D[N^-(v)])<r\},
\]
and
\[
Y=\{v\notin X:\alpha(D[N^+(v)])<r\}.
\]
Let \(B=V(D)\setminus(X\cup Y)\).

Every neighborhood has clique number at most \(w-1\). Consequently, each vertex of \(X\) has indegree at most \(R(w,r)-1\), while each vertex of \(Y\) has outdegree at most that number. The elementary coloring bound gives
\[
\chi(D[X])+\chi(D[Y])
\le 2\bigl(2(R(w,r)-1)+1\bigr)
=a_k(w).
\tag{2}
\]

Fix \(v\in B\). Choose stable sets
\[
W_v^-\subseteq N^-(v),\qquad
W_v^+\subseteq N^+(v),
\qquad |W_v^-|=|W_v^+|=r.
\]
These witnesses may lie anywhere in \(D\), not necessarily in \(B\).

Define the exceptional out-neighbors of \(v\) by
\[
E_v^+=
\{x\in N^+(v):x\text{ has at least }k
\text{ nonneighbors in }W_v^-\}.
\]

For each \(k\)-subset \(I\subseteq W_v^-\), let
\[
M_I=\{x\in N^+(v):x\text{ is anticomplete to }I\}.
\]
The set \(M_I\) has no stable \(k\)-set. Such a set, together with \(I\) and center \(v\), would induce \(S_{k,k}\). Also \(\omega(D[M_I])\le w-1\). Thus
\[
|M_I|\le R(w,k)-1.
\]
Taking the union over all choices of \(I\) yields
\[
|E_v^+|
\le \binom{r}{k}\bigl(R(w,k)-1\bigr)
=b.
\tag{3}
\]
Interchanging incoming and outgoing neighborhoods gives a set
\[
E_v^-\subseteq N^-(v),\qquad |E_v^-|\le b,
\tag{4}
\]
such that every vertex of \(N^-(v)\setminus E_v^-\) has at most \(k-1\) nonneighbors in \(W_v^+\).

I claim that
\[
\omega\!\left(D[N^+(v)\setminus E_v^+]\right)\le w-2.
\tag{5}
\]
Suppose instead that \(C\) is a clique of size \(w-1\) in this set. Each \(x\in C\) misses at most \(k-1\) vertices of \(W_v^-\). Since
\[
|W_v^-|=(w-1)(k-1)+1,
\]
some vertex \(u\in W_v^-\) is adjacent to every vertex of \(C\). Then
\[
C\cup\{u,v\}
\]
is an underlying clique of size \(w+1\), a contradiction. The same argument proves
\[
\omega\!\left(D[N^-(v)\setminus E_v^-]\right)\le w-2.
\tag{6}
\]

It remains to avoid all exceptional incidences within each \(Z_i\). Form an auxiliary undirected graph \(F\) on \(B\), placing an edge \(vx\) whenever
\[
x\in B\cap(E_v^+\cup E_v^-).
\]
Each vertex selects at most \(2b\) such edges. Hence, for every \(U\subseteq B\),
\[
|E(F[U])|\le 2b|U|.
\]
Therefore \(F\) is \(4b\)-degenerate and admits a proper coloring with \(q=4b+1\) colors. Let its color classes be \(Z_1,\ldots,Z_q\).

If \(v,x\in Z_i\), then \(x\notin E_v^+\cup E_v^-\). Thus (5) and (6) imply (1). Together with (2), this proves the lemma. \(\square\)

## 3. Cyclic-triangle-free orientations

We now obtain a \(\chi\)-bound for all clique numbers, provided that cyclic triangles are forbidden.

**Theorem.** Fix \(k\ge2\). There is an explicit function \(f_k\) such that every \(\{S_{k,k},\vec C_3\}\)-free oriented graph \(D\) satisfies
\[
\chi(D)\le f_k(\omega(D)).
\]
One may take
\[
f_k(0)=0,\qquad f_k(1)=1,\qquad f_k(2)=4k-2,
\]
and, for \(w\ge3\),
\[
f_k(w)=a_k(w)+q_k(w)f_k(w-1).
\tag{7}
\]
For fixed \(k\), this bound satisfies
\[
f_k(w)\le \exp\!\bigl(O_k(w\log(w+1))\bigr).
\tag{8}
\]

### Proof

The cases \(\omega(D)\le1\) are immediate.

If \(\omega(D)\le2\), every neighborhood is stable. Thus a vertex with at least \(k\) in-neighbors and \(k\) out-neighbors would be the center of an induced \(S_{k,k}\). Every vertex therefore has indegree at most \(k-1\) or outdegree at most \(k-1\). Partitioning according to these alternatives gives
\[
\chi(D)\le (2k-1)+(2k-1)=4k-2.
\]

Now let \(w\ge3\), and assume the assertion for clique bound \(w-1\). Apply the decomposition lemma.

A tournament containing no cyclic triangle is transitive: if \(x\to y\) and \(y\to z\), then the edge between \(x,z\) must be \(x\to z\). Consequently, every clique of \(D\) is transitively oriented.

Suppose some \(D[Z_i]\) contained a clique \(C\) of size \(w\). Its transitive orientation has a source \(v\), so
\[
C\setminus\{v\}\subseteq N^+(v)\cap Z_i
\]
would be a clique of size \(w-1\), contrary to (1). Therefore
\[
\omega(D[Z_i])\le w-1.
\]

Each \(D[Z_i]\) remains \(S_{k,k}\)-free and \(\vec C_3\)-free. By induction, each has chromatic number at most \(f_k(w-1)\). Using disjoint palettes for the parts gives precisely (7).

For the growth estimate, the elementary Ramsey bound yields
\[
R(w,r_k(w))
\le \binom{w+r_k(w)-2}{w-1}
=\binom{k(w-1)}{w-1}
\le 2^{k(w-1)}.
\]
Also
\[
R(w,k)=O_k(w^{k-1}),
\qquad
\binom{r_k(w)}k=O_k(w^k).
\]
Hence
\[
a_k(w)=\exp(O_k(w)),
\qquad
q_k(w)=O_k(w^{2k-1}).
\]
Unrolling (7), or bounding its products by a constant to the power \(w\) times \((w!)^{2k-1}\), proves (8). \(\square\)

This proves the first part of the partial theorem for every oriented star, by the initial reduction to \(S_{k,k}\).

## 4. All orientations of \(K_4\)-free graphs

For the second result, use the established theorem quoted in the question:

> For each \(k\), there is a finite constant \(c_k\) such that every \(\{S_{k,k},TT_3\}\)-free oriented graph has chromatic number at most \(c_k\).

No numerical value of \(c_k\) is assumed.

**Corollary.** Every \(S_{k,k}\)-free oriented graph \(D\) with \(\omega(D)\le3\) satisfies
\[
\begin{split}
\chi(D)\le {}&
4R(3,2k-1)-2\\
&+\left[
4\binom{2k-1}{k}\bigl(R(3,k)-1\bigr)+1
\right]c_k.
\end{split}
\tag{9}
\]

### Proof

Apply the decomposition lemma with \(w=3\). In every resulting \(D[Z_i]\), both the in-neighborhood and the out-neighborhood of every vertex are stable.

Thus \(D[Z_i]\) contains no \(TT_3\): a transitive triangle has a source whose out-neighborhood contains an edge. Each \(D[Z_i]\) is also \(S_{k,k}\)-free, so the quoted theorem gives
\[
\chi(D[Z_i])\le c_k.
\]
Adding the palettes gives
\[
\chi(D)\le a_k(3)+q_k(3)c_k,
\]
which is (9). \(\square\)

For example, when \(k=2\), the bound is
\[
\chi(D)\le 22+25c_2.
\]
This result permits both cyclic and transitive triangles; only an underlying \(K_4\) is forbidden.

## 5. Why this does not prove the full conjecture

The decomposition lowers the clique number of each **one-sided neighborhood**, but need not lower the clique number of the entire piece.

Already for \(w=4\), consider the tournament with arcs
\[
1\to2,\quad 2\to3,\quad 3\to4,\quad 4\to1,
\quad 1\to3,\quad 2\to4.
\]
Every vertex has indegree and outdegree at most two. Thus every one-sided neighborhood has clique number at most
\[
2=w-2,
\]
yet the underlying graph is \(K_4\). It also contains both triangle orientations.

This is not a counterexample to the conjecture. It shows exactly why the above induction cannot simply continue:

- Without cyclic triangles, every clique has a source, and local clique lowering forces a genuine clique-number decrease.
- At clique bound three, local clique lowering eliminates all transitive triangles, allowing the quoted source theorem to finish.
- For arbitrary orientations at larger clique bounds, neither conclusion follows.

Accordingly, the unrestricted conjecture remains unresolved by this argument. I have not checked whether these special cases or their bounds are already implicit in the source paper or subsequent literature, so I make no novelty claim.