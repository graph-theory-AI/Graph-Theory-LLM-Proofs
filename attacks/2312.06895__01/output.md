```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general identity remains open, but edge-minimality gives a finite critical-core reduction, quantitative lower bounds for every q and t, and a complete proof for (q,t)=(2,3).",
  "would_publish": false,
  "caveats": "No exhaustive computation was run; the unresolved small-parameter cases, particularly q>=3, remain, and the (2,3) case may already be known."
}
```

## 1. Statement and notation

I interpret the \(q\)-color conjecture as follows. For integers \(q\ge 1\) and \(t\ge2\), let

\[
L_q(t):=r_{K_3}^{(q)}(K_t)
   =\min\bigl\{T(G):G\longrightarrow_q K_t\bigr\},
\]

where \(T(G)\) is the number of triangles of \(G\), and \(G\longrightarrow_q K_t\) means that every \(q\)-coloring of \(E(G)\) contains a monochromatic \(K_t\). Let

\[
R=R_q(t):=r_q(K_t).
\]

The conjecture is

\[
L_q(t)=\binom{R_q(t)}3.
\tag{C}
\]

The upper bound is immediate from \(K_R\longrightarrow_qK_t\).

I do not prove (C) in full. I give:

1. a local structural lemma for edge-minimal Ramsey graphs;
2. a general lower bound and a finite critical-core reduction;
3. a recursive all-\(q\) lower bound;
4. a complete proof of \(L_2(3)=20=\binom63\).

---

## 2. Edge-minimal Ramsey graphs are locally very triangular

For an edge \(e=xy\), write

\[
\lambda_G(e)=|N_G(x)\cap N_G(y)|,
\]

the number of triangles containing \(e\).

### Lemma 2.1
Let \(q\ge1\) and \(t\ge3\). If \(G\) is edge-minimal subject to \(G\longrightarrow_qK_t\), then every edge of \(G\) lies in at least

\[
d:=q(t-2)
\]

triangles.

#### Proof
Fix \(e=xy\in E(G)\). By edge-minimality, \(G-e\) has a \(q\)-edge-coloring \(\varphi\) with no monochromatic \(K_t\).

For each color \(c\), assign color \(c\) to \(e\). The resulting coloring of \(G\) must contain a monochromatic \(K_t\). Such a \(K_t\) must contain \(e\), because \(\varphi\) had none before \(e\) was inserted. Thus there is a set \(S_c\) of \(t-2\) vertices such that all edges of the \(K_t\) on

\[
\{x,y\}\cup S_c
\]

other than \(xy\) have color \(c\).

If \(c\ne c'\), then \(S_c\cap S_{c'}=\varnothing\): otherwise an edge from \(x\) to a common vertex would simultaneously have colors \(c\) and \(c'\). Therefore

\[
\left|\bigcup_{c=1}^q S_c\right|=q(t-2),
\]

and every vertex in this union is a common neighbor of \(x,y\). Hence
\(\lambda_G(e)\ge q(t-2)\). ∎

### Lemma 2.2
If \(G\longrightarrow_qK_t\), then

\[
\chi(G)\ge R_q(t).
\]

#### Proof
If \(\chi(G)\le R-1\), properly color \(V(G)\) by at most \(R-1\) labels. Take a \(q\)-coloring of \(K_{R-1}\) without a monochromatic \(K_t\), and color an edge \(uv\in E(G)\) by the color assigned to the pair of vertex labels of \(u,v\). A clique of \(G\) has distinct vertex labels, so a monochromatic \(K_t\) in \(G\) would give one in \(K_{R-1}\), a contradiction. ∎

---

## 3. A quantitative lower bound

Let \(G_0\subseteq G\) be an edge-minimal \(q\)-Ramsey subgraph, and let \(J\subseteq G_0\) be an \(R\)-critical subgraph. Such a \(J\) exists by taking a subgraph minimal subject to chromatic number at least \(R\). Write \(m(J)=|E(J)|\).

Every edge of \(J\) lies in at least \(d=q(t-2)\) triangles of \(G_0\). A triangle of \(G_0\) contains at most three edges of \(J\). Therefore

\[
d\,m(J)\le 3T(G_0)\le 3T(G).
\tag{3.1}
\]

Since \(J\) is \(R\)-critical, \(\delta(J)\ge R-1\), and hence

\[
m(J)\ge \binom R2.
\]

Consequently:

### Proposition 3.1
For all \(q\ge1\) and \(t\ge3\),

\[
\boxed{
L_q(t)\ge
\left\lceil
\frac{q(t-2)}3\binom{R_q(t)}2
\right\rceil
=
\left\lceil
\frac{q(t-2)}{R_q(t)-2}
\binom{R_q(t)}3
\right\rceil .
}
\tag{3.2}
\]

This is generally much weaker than the conjectured value, but it is uniform in both parameters.

A slight improvement follows from standard critical-graph facts. A noncomplete \(R\)-critical graph has at least \(R+2\) vertices, and Dirac's critical edge bound gives

\[
2m(J)\ge (R-1)|V(J)|+R-3.
\tag{3.3}
\]

Thus, unless \(J=K_R\),

\[
m(J)\ge \frac{R^2+2R-5}{2}.
\]

We obtain

\[
L_q(t)\ge
\min\left\{
\binom R3,\,
\left\lceil
\frac{q(t-2)(R^2+2R-5)}6
\right\rceil
\right\}.
\tag{3.4}
\]

In particular, (C) follows whenever

\[
q(t-2)(R^2+2R-5)
\ge R(R-1)(R-2).
\tag{3.5}
\]

This numerical criterion is not strong for the presently difficult parameters, but it is unconditional.

---

## 4. A finite critical-core reduction

Set

\[
C=\binom R3,\qquad d=q(t-2),\qquad
M=\left\lfloor\frac{3(C-1)}d\right\rfloor.
\tag{4.1}
\]

Suppose \(G\) were a counterexample with \(T(G)\le C-1\), and choose an edge-minimal Ramsey subgraph \(G_0\).

Applying Lemma 2.1 to all edges of \(G_0\),

\[
d|E(G_0)|\le3T(G_0)\le3(C-1),
\]

so

\[
|E(G_0)|\le M.
\tag{4.2}
\]

Moreover, \(G_0\) is connected and every edge lies in a triangle, hence \(\delta(G_0)\ge2\), so

\[
|V(G_0)|\le |E(G_0)|\le M.
\tag{4.3}
\]

Let \(J\subseteq G_0\) be \(R\)-critical. It cannot be \(K_R\), since then \(G_0\) would already contain \(C\) triangles. Thus \(|V(J)|\ge R+2\). Combining (3.1), (3.3), and \(m(J)\le M\), we obtain

\[
R+2\le |V(J)|
\le
N:=
\left\lfloor
\frac{2M-(R-3)}{R-1}
\right\rfloor.
\tag{4.4}
\]

### Proposition 4.1
For a fixed pair \((q,t)\), any counterexample to (C) contains a noncomplete \(R_q(t)\)-critical graph \(J\) whose order lies in the explicitly finite interval

\[
R_q(t)+2\le |V(J)|\le N,
\]

with \(N\) given by (4.4), and the entire edge-minimal Ramsey graph has at most \(M\) vertices and edges.

Thus a finite verification of the relevant critical graphs suffices for each fixed pair.

For example, using \(R_3(3)=17\),

\[
C=680,\qquad d=3,\qquad M=679,\qquad N=84.
\]

Hence a counterexample to \(L_3(3)=680\) would have a noncomplete \(17\)-critical core on between \(19\) and \(84\) vertices. This remains far too large for a naive enumeration, but it is a concrete finite reduction.

The absolute constant \(K\) in the graph-coloring theorem quoted in the source paper also combines directly with Lemma 2.1: if

\[
q(t-2)\ge K,
\]

then the conjectured equality follows. Thus, assuming the quoted theorem, only finitely many parameter pairs \((q,t)\) can remain outside its range. The prompt does not give an explicit numerical value of \(K\), so I do not attempt to list them.

---

## 5. The exact case \((q,t)=(2,3)\)

We now prove

\[
L_2(3)=20.
\tag{5.1}
\]

Recall \(R_2(3)=6\): the red \(5\)-cycle and its blue complement color \(K_5\) without a monochromatic triangle, while the standard pigeonhole argument shows \(K_6\longrightarrow_2K_3\). Thus \(K_6\) gives the upper bound \(L_2(3)\le20\).

We use two standard, proved facts about critical graphs:

1. If \(H\) is noncomplete and \(k\)-critical, then
   \[
   2|E(H)|\ge (k-1)|V(H)|+k-3.
   \tag{5.2}
   \]
2. If \(H\) is \(k\)-critical and \(|V(H)|\le2k-2\), then \(\overline H\) is disconnected. Equivalently, \(H\) is a nontrivial join of critical graphs.

These are the usual Dirac edge bound and Gallai decomposition lemma.

### Lemma 5.1
Every \(6\)-critical graph on at most \(10\) vertices contains at least \(20\) triangles.

#### Proof
Let \(J\) be such a graph. By the Gallai decomposition lemma, \(\overline J\) is disconnected. Decompose \(J\) maximally as a join

\[
J=J_1\vee\cdots\vee J_s,
\]

where every \(J_i\) is critical and \(\overline{J_i}\) is connected. Put \(k_i=\chi(J_i)\); then

\[
\sum_i k_i=6.
\]

Except when the multiset \(\{k_i\}\) is exactly \(\{1,5\}\), some subcollection has chromatic sum \(2\) or \(3\). Grouping factors accordingly, write \(J=A\vee B\) with \((\chi(A),\chi(B))=(2,4)\) or \((3,3)\).

For any join,

\[
T(A\vee B)=T(A)+T(B)+|E(A)||V(B)|+|V(A)||E(B)|.
\tag{5.3}
\]

**Case 1: \((\chi(A),\chi(B))=(2,4)\).**  
A \(2\)-critical graph is \(K_2\), so

\[
T(J)=T(B)+2|E(B)|+|V(B)|.
\]

If \(B=K_4\), this equals \(4+12+4=20\). Otherwise, by (5.2),

\[
2|E(B)|\ge3|V(B)|+1,
\]

and \(|V(B)|\ge5\). Hence

\[
T(J)\ge2|E(B)|+|V(B)|
\ge4|V(B)|+1\ge21.
\]

**Case 2: \((\chi(A),\chi(B))=(3,3)\).**  
Every \(3\)-critical graph is an odd cycle. Thus \(|E(A)|=|V(A)|\), and similarly for \(B\). If both are \(K_3\), then \(J=K_6\) and has \(20\) triangles. If at least one cycle has length at least \(5\), the cross terms in (5.3) are already at least

\[
2|V(A)||V(B)|\ge 2\cdot3\cdot5=30.
\]

**Exceptional case \(\{k_i\}=\{1,5\}\).**  
Then

\[
J=K_1\vee B,
\]

where \(B\) is \(5\)-critical and \(\overline B\) is connected. The Gallai lemma applied to \(B\) gives \(|V(B)|\ge9\), while \(|V(J)|\le10\), so \(|V(B)|=9\). By (5.2),

\[
2|E(B)|\ge 4\cdot9+2=38,
\]

so \(|E(B)|\ge19\).

Moreover, \(B\) contains a triangle. Indeed, if \(B\) were triangle-free, then \(\delta(B)\ge4\). Choose \(v\) with \(d(v)\ge4\). Its neighborhood is independent, and \(B-N(v)\) has at most five vertices and is triangle-free, hence is \(3\)-colorable. Giving \(N(v)\) a fourth color would \(4\)-color \(B\), contradicting \(\chi(B)=5\).

Therefore

\[
T(J)=T(B)+|E(B)|\ge1+19=20.
\]

All cases are covered. ∎

### Theorem 5.2
\[
L_2(3)=20.
\]

#### Proof
Suppose \(G\longrightarrow_2K_3\) and \(T(G)\le19\). Choose an edge-minimal Ramsey subgraph \(G_0\), and then a \(6\)-critical subgraph \(J\subseteq G_0\).

By Lemma 2.1, every edge of \(G_0\), hence every edge of \(J\), lies in at least two triangles of \(G_0\). Counting incidences between edges of \(J\) and triangles of \(G_0\),

\[
2|E(J)|\le3T(G_0)\le57,
\]

so \(|E(J)|\le28\).

If \(J=K_6\), then \(G_0\) already contains \(20\) triangles, a contradiction. Otherwise, the critical edge bound gives

\[
5|V(J)|+3\le2|E(J)|\le56,
\]

hence \(|V(J)|\le10\). Lemma 5.1 then implies \(T(J)\ge20\), again a contradiction.

Thus every \(2\)-Ramsey graph for \(K_3\) has at least \(20\) triangles, and \(K_6\) attains this bound. ∎

The trivial cases also satisfy the conjecture: \(L_q(2)=0=\binom23\), and \(L_1(t)=\binom t3\).

---

## 6. A recursive lower bound using vertex partitions

There is another unconditional bound valid for all numbers of colors.

### Proposition 6.1
Let \(a,b\ge1\), \(q=a+b\), and \(t\ge3\). Then

\[
\boxed{
L_{a+b}(t)\ge
\bigl(R_a(t)-1\bigr)^2L_b(t).
}
\tag{6.1}
\]

#### Proof
Put \(s=R_a(t)-1\), and fix an \(a\)-coloring of \(K_s\) without a monochromatic \(K_t\).

Let \(G\longrightarrow_{a+b}K_t\), and partition \(V(G)\) into \(s\) labeled parts \(V_1,\dots,V_s\). If no \(G[V_i]\) were \(b\)-Ramsey for \(K_t\), color each \(G[V_i]\) with the \(b\)-color palette without a monochromatic \(K_t\). Color every edge between \(V_i\) and \(V_j\) by the color of \(ij\) in the fixed \(a\)-coloring, using a disjoint palette.

A monochromatic \(K_t\) in one of the \(b\) colors would lie within a single part; one in an \(a\) color would use at most one vertex from each part and project to a monochromatic \(K_t\) in the template. Both are impossible. Therefore every such partition has at least one part inducing a \(b\)-Ramsey graph, and hence

\[
\sum_{i=1}^s T(G[V_i])\ge L_b(t).
\tag{6.2}
\]

Now assign each vertex independently and uniformly to one of the \(s\) parts. A fixed triangle lies wholly within one part with probability \(1/s^2\). Taking expectations in (6.2),

\[
\frac{T(G)}{s^2}\ge L_b(t),
\]

which proves (6.1). ∎

In particular,

\[
L_q(t)\ge
\bigl(R_{q-1}(t)-1\bigr)^2\binom t3
\tag{6.3}
\]

and, by iterating with \(a=1\),

\[
L_q(t)\ge
(t-1)^{2(q-1)}\binom t3.
\tag{6.4}
\]

These bounds do not reach the conjectured cubic expression, but they may be useful when \(t\) is fixed and \(q\) varies.

---

## 7. Fully specified finite computational test

For a fixed \((q,t)\), after computing \(R=R_q(t)\), set \(C,d,M\) as in (4.1). Any counterexample has an edge-minimal subgraph \(G_0\) satisfying:

- \(G_0\) is connected;
- \(|V(G_0)|,|E(G_0)|\le M\);
- \(T(G_0)\le C-1\);
- every edge belongs to at least \(d=q(t-2)\) triangles.

One may therefore generate all connected unlabeled simple graphs satisfying these bounds and test whether they are \(q\)-Ramsey for \(K_t\). The avoiding-coloring SAT instance has variables \(x_{e,c}\) for \(e\in E(G)\) and \(c\in[q]\), with:

1. exactly one \(x_{e,c}\) true for each edge \(e\);
2. for every copy \(Q\cong K_t\) and every color \(c\), the clause
   \[
   \bigvee_{e\in E(Q)}\neg x_{e,c}.
   \]

The graph is \(q\)-Ramsey exactly when this CNF is unsatisfiable. A complete computation should use canonical graph generation and retain independently checkable SAT/DRAT certificates. I have not executed this search.

---

## 8. Remaining gap

The unresolved step is to convert the relatively small local triangle multiplicity

\[
\lambda_G(e)\ge q(t-2)
\]

into the global cubic lower bound \(\binom{R_q(t)}3\) for the finitely many parameter pairs not covered by the absolute-\(K\) theorem. The incidence estimate alone only gives the fraction

\[
\frac{q(t-2)}{R_q(t)-2}
\]

of the conjectured answer. For instance, the first genuinely multicolor case \((q,t)=(3,3)\) reduces to \(17\)-critical cores on \(19\)–\(84\) vertices, but the argument above does not classify or exclude those cores.

Thus the full \(q\)-color conjecture remains open here.