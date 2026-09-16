```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A substitution-based attack gives a sharp polynomial bound for graphs assembled from templates of at most five vertices and explicit upper bounds on possible exponents for prime forbidden graphs.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; no new unrestricted forbidden-graph case or novelty for these restricted results is claimed."
}
```

## 1. Scope and partial result

I use the intended condition \(\delta(H)>0\). I do not obtain a proof or counterexample for arbitrary \(H\).

The approach below examines **substitution constructions**. It gives a sharp result for a restricted host class, followed by quantitative restrictions on any exponent in the conjecture. All arguments are self-contained.

For a graph \(F\) on \(\{1,\ldots,r\}\), write
\[
F[G_1,\ldots,G_r]
\]
for the graph obtained by replacing vertex \(i\) with \(G_i\), making the \(i\)-th and \(j\)-th blocks complete to one another exactly when \(ij\in E(F)\).

For \(k\ge2\), let \(\mathcal M_k\) be the class generated from \(K_1\) by substitutions whose templates have between two and \(k\) vertices. All substituted graphs are nonempty. Equivalently, these graphs admit a recursive substitution decomposition with template order at most \(k\).

### Theorem 1
Let \(G\in\mathcal M_k\), and put \(n=|V(G)|\). Then
\[
\max\{\alpha(G),\omega(G)\}
   \ge n^{1/(2\log_2 k)}.
\tag{1}
\]

For \(k=5\), the following stronger bound holds:
\[
\alpha(G)\omega(G)\ge n^{\log_5 4},
\qquad
\max\{\alpha(G),\omega(G)\}\ge n^{\log_5 2}.
\tag{2}
\]
The exponent
\[
\log_5 2\approx0.430677
\]
is optimal for \(\mathcal M_5\), even if a constant multiplicative factor is permitted.

The five-cycle is a **template** here, not the forbidden graph. Thus this is not a proof about all \(C_5\)-free graphs.

---

## 2. The general bounded-template bound

For
\[
G=F[G_1,\ldots,G_r],
\]
put
\[
a_i=\alpha(G_i),\qquad b_i=\omega(G_i).
\]
The substitution identities are
\[
\alpha(G)=\max_{\substack{I\subseteq V(F)\\I\text{ independent}}}
              \sum_{i\in I}a_i,
\qquad
\omega(G)=\max_{\substack{K\subseteq V(F)\\K\text{ a clique}}}
              \sum_{i\in K}b_i.
\tag{3}
\]

Write \(A=\alpha(G)\), \(B=\omega(G)\), and \(z_i=a_i b_i\). For any two distinct blocks \(i,j\),
\[
AB\ge z_i+z_j.
\tag{4}
\]
Indeed, if \(ij\) is an edge, then
\[
AB\ge \max\{a_i,a_j\}(b_i+b_j)\ge a_i b_i+a_jb_j.
\]
If it is a nonedge, interchange the roles of \(a\) and \(b\).

Set \(p=\log_2 k\). We prove by induction that
\[
|V(G)|\le\bigl(\alpha(G)\omega(G)\bigr)^p.
\tag{5}
\]
The singleton case is immediate. At a substitution node, order the blocks so that
\(z_1\ge z_2\ge\cdots\ge z_r\). By induction,
\[
|V(G)|\le\sum_i z_i^p
 \le z_1^p+(k-1)z_2^p
 \le(z_1+z_2)^p
 \le(AB)^p.
\]
The penultimate inequality follows from \(k=2^p\) and
\[
(x+y)^p-x^p\ge(2^p-1)y^p
\qquad(x\ge y\ge0,\ p\ge1);
\]
the left side is nondecreasing in \(x\), so its minimum over \(x\ge y\) occurs at \(x=y\).

Taking square roots in (5) proves (1). In particular, constructions using any fixed finite collection of substitution templates cannot by themselves produce a counterexample to Erdős–Hajnal.

---

## 3. The sharp five-vertex bound

Set
\[
q=\log_4 5.
\]
We will prove
\[
|V(G)|\le\bigl(\alpha(G)\omega(G)\bigr)^q
\qquad(G\in\mathcal M_5).
\tag{6}
\]

Two weighted inequalities handle all possible templates.

### 3.1 Perfect templates

Recall that \(F\) is perfect if every induced subgraph \(J\) satisfies
\(\chi(J)=\omega(J)\).

**Lemma 2.** Suppose \(F\) is perfect and \(a_i,b_i\) are positive integers. Define
\[
A=\max_{I\text{ independent}}\sum_{i\in I}a_i,
\qquad
B=\max_{K\text{ a clique}}\sum_{i\in K}b_i.
\]
Then
\[
\sum_i a_i b_i\le AB.
\tag{7}
\]

**Proof.**
Replace vertex \(i\) of \(F\) by a clique of order \(b_i\). This graph is perfect and has clique number \(B\). A proper \(B\)-colouring partitions its vertices into \(B\) stable sets. Give each copy of vertex \(i\) weight \(a_i\). Each colour class has total weight at most \(A\), whereas the total weight is \(\sum_i a_i b_i\). This proves (7).

For completeness, the perfection assertion follows by repeated replication of a vertex as an adjacent true twin. Here is the replication argument. It suffices to colour an induced subgraph containing both twins \(v,v'\). Delete \(v'\), obtaining a perfect graph \(J\), and put \(s=\omega(J)\).

* If an \(s\)-clique contains \(v\), the replicated graph has clique number \(s+1\), and an \(s\)-colouring of \(J\) plus one new colour suffices.
* Otherwise, take an \(s\)-colouring of \(J\), with \(S\) the colour class containing \(v\). Every \(s\)-clique meets \(S\setminus\{v\}\). Thus
  \(J-(S\setminus\{v\})\) has clique number at most \(s-1\), and perfection gives an \((s-1)\)-colouring. The set
  \((S\setminus\{v\})\cup\{v'\}\) is stable and receives one further colour.

Induced subgraphs containing at most one twin are isomorphic to induced subgraphs of the original perfect graph. This covers every case. \(\square\)

Consequently, if the substituted graphs satisfy (6) and \(F\) is perfect, then
\[
\begin{aligned}
|V(G)|
&\le\sum_i(a_i b_i)^q\\
&\le\left(\sum_i a_i b_i\right)^q\\
&\le(AB)^q.
\end{aligned}
\tag{8}
\]

### 3.2 The five-cycle template

Index \(C_5\) by \(\mathbb Z/5\mathbb Z\), with edges \(i(i+1)\).

**Lemma 3.** Suppose \(x_i,y_i\ge0\) satisfy
\[
x_i+x_{i+2}\le1,
\qquad
y_i+y_{i+1}\le1
\qquad(i\in\mathbb Z/5\mathbb Z).
\tag{9}
\]
Then
\[
\sum_{i=0}^4(x_i y_i)^q\le1.
\tag{10}
\]

**Proof.**
Consider the polytope
\[
P=\{z\in\mathbb R_{\ge0}^5:z_i+z_{i+1}\le1\}.
\]
Every vertex of \(P\) is either the incidence vector of an independent set of \(C_5\), or
\[
(1/2,1/2,1/2,1/2,1/2).
\tag{11}
\]

Here is a direct verification. All coordinates lie in \([0,1]\). For a feasible vector having fractional coordinates, form the graph on those coordinates using the tight inequalities \(z_i+z_{i+1}=1\). If a component is bipartite, alternately adding and subtracting a sufficiently small \(\varepsilon\) on its two sides gives two distinct feasible vectors with the original vector as their midpoint. Such a vector is not a polytope vertex. The only possible nonbipartite tight component is the entire five-cycle; its five equations force (11).

The same description applies to the polytope defined by the \(x\)-constraints, since the distance-two graph of \(C_5\) is another five-cycle.

The function
\[
f(x,y)=\sum_i(x_i y_i)^q
\]
is convex in either vector when the other is fixed. Therefore its maximum over the product of the two polytopes is attained at a pair of vertices. There are four cases:

1. If both vectors are integral, the support of \(x\) is a clique of the original \(C_5\), while the support of \(y\) is independent. Their intersection has size at most one, so \(f(x,y)\le1\).
2. If exactly one vector is the all-half vector, the other has support of size at most two. Hence
   \[
   f(x,y)\le2(1/2)^q\le1.
   \]
3. If both are the all-half vector, then
   \[
   f(x,y)=5(1/4)^q=1.
   \]

Thus (10) holds. \(\square\)

Now suppose
\[
G=C_5[G_0,\ldots,G_4].
\]
By (3),
\[
A=\max_i(a_i+a_{i+2}),\qquad
B=\max_i(b_i+b_{i+1}).
\]
Thus \(x_i=a_i/A\) and \(y_i=b_i/B\) satisfy (9). Applying the induction hypothesis and Lemma 3 gives
\[
|V(G)|
\le\sum_i(a_i b_i)^q
=(AB)^q\sum_i(x_i y_i)^q
\le(AB)^q.
\tag{12}
\]

### 3.3 Why these two cases cover every template

Every graph on at most five vertices is perfect unless it is \(C_5\).

To verify this without invoking a perfect-graph characterization, choose a minimally nonperfect induced subgraph \(J\) and let \(r=\chi(J)>\omega(J)\). Minimality makes \(J\) vertex-critical, so
\[
\delta(J)\ge r-1.
\]

* If \(r=3\), then \(J\) is triangle-free and nonbipartite. On at most five vertices it must contain a five-cycle, and triangle-freeness prohibits its chords. Hence \(J=C_5\).
* If \(r=4\), a four-vertex \(J\) would be \(K_4\). On five vertices, the minimum-degree bound implies that \(\overline J\) is a matching together with isolated vertices. Such a graph \(J\) has \(\chi(J)=\omega(J)\), a contradiction.
* If \(r=5\), then \(J=K_5\), again a contradiction.

Thus every substitution step in \(\mathcal M_5\) is covered by (8) or (12). Induction proves (6), and hence (2).

### 3.4 Sharpness

Let \(T_0=K_1\), and recursively define
\[
T_{t+1}=C_5[T_t,T_t,T_t,T_t,T_t].
\]
Then
\[
|V(T_t)|=5^t,\qquad
\alpha(T_t)=\omega(T_t)=2^t.
\tag{13}
\]
Therefore equality holds in (2). No exponent larger than \(\log_5 2\) works on \(\mathcal M_5\), even with a fixed positive multiplicative constant.

For comparison, the same perfect-template argument with \(q=1\) gives the sharp exponent \(1/2\) on \(\mathcal M_k\) for \(2\le k\le4\). Sharp examples are disjoint unions of \(t\) cliques of order \(t\).

---

## 4. Consequences for prime forbidden graphs

A set \(M\subseteq V(H)\) is a **module** if every vertex outside \(M\) is either complete or anticomplete to \(M\). Call \(H\) prime if it has no module \(M\) with
\[
2\le |M|<|V(H)|.
\]

### Lemma 4
If \(H\) is prime, substitution preserves \(H\)-freeness: if \(F,G_1,\ldots,G_r\) are \(H\)-free, then so is \(F[G_1,\ldots,G_r]\).

**Proof.**
Suppose an induced copy of \(H\) meets more than one substitution block. Its intersection with each block is a proper module of the copy. Primeness implies that every such intersection has size at most one. The occupied blocks therefore give an induced copy of \(H\) in \(F\), a contradiction.

If the copy meets only one block, it contradicts that block’s \(H\)-freeness. \(\square\)

It follows that, for every prime graph \(H\) with at least six vertices,
\[
\mathcal M_5\subseteq\{H\text{-free graphs}\}.
\tag{14}
\]
Thus Theorem 1 proves a sharp polynomial bound on a subclass of the \(H\)-free graphs. Conversely, the examples \(T_t\) show that every admissible Erdős–Hajnal exponent for such an \(H\) must satisfy
\[
\boxed{\delta(H)\le\log_5 2.}
\tag{15}
\]

### A stronger asymptotic upper bound as \(|H|\) grows

The same amplification argument permits random seeds.

**Proposition 5.** Let \(H\) be prime of order \(h\ge12\). Any admissible exponent satisfies
\[
\boxed{
\delta(H)\le
\frac{\log_2(h-1)}
     {\lfloor(h-3)/2\rfloor}
=
(2+o(1))\frac{\log_2 h}{h}.
}
\tag{16}
\]
This remains necessary even if the desired lower bound is allowed a positive multiplicative constant.

**Proof.**
Put
\[
\ell=\left\lfloor\frac{h-3}{2}\right\rfloor,
\qquad N=2^\ell,
\]
and choose \(F\sim G(N,1/2)\).

For any specified labelled \(h\)-vertex graph, the expected number of induced embeddings in \(F\) is at most
\[
N^h2^{-\binom h2}
\le2^{-h}.
\]
Consequently, the expected total number of induced embeddings of
\[
H,\quad K_h,\quad\overline{K_h}
\]
is at most \(3\cdot2^{-h}<1\). There exists an \(H\)-free graph \(F\) of order \(N\) with
\[
\alpha(F),\omega(F)\le h-1.
\]

Let \(F^{(t)}\) be its \(t\)-fold uniform substitution power. Lemma 4 gives \(H\)-freeness, while (3) gives
\[
|V(F^{(t)})|=N^t,
\qquad
\max\{\alpha(F^{(t)}),\omega(F^{(t)})\}
\le(h-1)^t.
\]
A bound \(c|V(G)|^\delta\) on every \(H\)-free graph would therefore imply
\[
cN^{t\delta}\le(h-1)^t.
\]
Taking \(t\)-th roots and letting \(t\to\infty\) proves (16). \(\square\)

---

## 5. What remains uncontrolled

The lower bounds above depend on **bounded substitution-template order**, not merely on excluding an induced graph \(H\). No argument here derives the required decomposition for an arbitrary \(H\)-free graph.

The prime-graph constructions give upper bounds on possible exponents, but they are not counterexamples: for each fixed seed, their homogeneous sets still have positive-power size.

Thus this attack establishes:

* polynomial homogeneous sets for every bounded-template substitution class;
* the exact exponent for template order at most five;
* infinite \(H\)-free constructions restricting possible exponents for prime \(H\).

It does **not** establish a positive exponent for an arbitrary forbidden \(H\), and no new unrestricted case of the Erdős–Hajnal conjecture is claimed.