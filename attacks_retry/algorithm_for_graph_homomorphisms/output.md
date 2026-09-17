```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There is a polynomial-time reduction from N-vertex maximum-degree-five 3-coloring to balanced, connected homomorphism instances of order Θ(N/log N).",
  "would_publish": false,
  "caveats": "This is an unconditional reduction, not an unconditional nonexistence proof; its ETH interpretation is conditional, and no literature novelty is claimed."
}
```

# A stronger balanced-instance obstruction

I do not obtain an unconditional yes or no answer. I do obtain the following unconditional compression theorem, strengthening the supplied attempt.

**Theorem 1.** There is a deterministic polynomial-time reduction taking an \(N\)-vertex graph \(X\) of maximum degree at most five to connected, simple, loopless graphs \(G_X,H_X\) such that
\[
X\text{ is 3-colorable}
\quad\Longleftrightarrow\quad
G_X\longrightarrow H_X,
\]
and, for sufficiently large \(N\),
\[
|V(G_X)|=|V(H_X)|
=\Theta\!\left(\frac{N}{\log N}\right).
\]

Consequently:

1. An \(O(c^{|V(G)|+|V(H)|})\)-time algorithm would give a
   \[
   2^{O(N/\log N)}
   \]
   algorithm for maximum-degree-five 3-coloring.
2. More generally, a \(2^{o(n\log n)}\)-time homomorphism algorithm on balanced instances \(|V(G)|=|V(H)|=n\) would give a \(2^{o(N)}\)-time algorithm for that coloring problem.
3. Via a linear-size reduction proved below, the proposed plain-exponential homomorphism algorithm would give a
   \[
   2^{O((v+m)/\log(v+m))}
   \]
   algorithm for 3-SAT with \(v\) variables and \(m\) clauses.

The reduction is unconditional. Under the explicitly stated sparse ETH assumption, it rules out the requested running time—even on balanced, connected instances. I do **not** treat ETH as a theorem or use it to label the original problem disproved.

There are two improvements over the previous attempt:

- more careful grouping gives a list-homomorphism target of size \(2^{O(r)}\), rather than \(2^{O(r\log r)}\);
- the nested-marker idea can remove lists with **linear**, rather than exponential, overhead in the target order.

Both are proved below. All logarithms are base two.

## 1. Grouping with a \(2^{O(r)}\)-vertex target

A list-homomorphism instance consists of graphs \(P,R\) and sets
\[
\mathcal L(B)\subseteq V(R),\qquad B\in V(P).
\]
Its question is whether there is a homomorphism \(f:P\to R\) with \(f(B)\in\mathcal L(B)\) for every \(B\).

We first prove a grouping lemma.

**Lemma 2.** Fix \(\Delta\geq1\). Let \(X\) have \(N\) vertices and maximum degree at most \(\Delta\), and let
\[
4\Delta^2\leq r\leq\sqrt N.
\]
One can construct a list-homomorphism instance \((P,R,\mathcal L)\) such that
\[
X\text{ is 3-colorable}
\quad\Longleftrightarrow\quad
(P,R,\mathcal L)\text{ is satisfiable},
\]
with
\[
\frac Nr\leq |V(P)|=O_\Delta(N/r),
\qquad
|V(R)|=r4^r.
\]
The construction takes time polynomial in \(N+4^r\).

### 1.1 A balanced labeling of the square

We construct a proper coloring
\[
\lambda:V(X^2)\longrightarrow[r]
\]
having two additional properties. Put
\[
a=\left\lceil\frac{4N}{r}\right\rceil,
\qquad
b=\left\lceil\frac{4\Delta^2a}{r}\right\rceil.
\]
We require:

- every label class has size at most \(a\);
- for every two distinct labels \(\ell,\mu\), at most \(b\) edges of \(X\) run between their classes.

Process vertices in any order. When labeling a vertex \(v\), forbid:

1. labels already used within distance at most two of \(v\);
2. labels whose current class already has \(a\) vertices;
3. for each already labeled neighbor of \(v\), with label \(\mu\), labels \(\ell\) for which the current number of \(\ell\)-to-\(\mu\) edges is already \(b\).

The first rule forbids at most \(\Delta^2\leq r/4\) labels.

The second forbids at most
\[
N/a\leq r/4
\]
labels.

For a fixed neighbor label \(\mu\), there are at most \(\Delta a\) currently counted edges incident with its class. Thus the third rule forbids at most
\[
\frac{\Delta a}{b}\leq\frac{r}{4\Delta}
\]
labels for that neighbor. Over all neighbors it forbids at most \(r/4\) labels.

Hence fewer than \(r\) labels are forbidden.

The invariants are preserved. In particular, already labeled neighbors of \(v\) have distinct labels because they are pairwise at distance at most two in \(X\). Consequently, assigning a label to \(v\) increases each relevant label-pair edge count by at most one. This proves the claimed labeling.

### 1.2 Forming buckets

For each label \(\ell\), define an auxiliary graph \(F_\ell\) on \(\lambda^{-1}(\ell)\). Distinct vertices \(u,v\) are adjacent in \(F_\ell\) if their neighborhoods in \(X\) contain vertices of a common label.

For a vertex \(v\), there are at most \(\Delta\) labels on its neighbors. For each such label \(\mu\), at most \(b\) vertices of \(\lambda^{-1}(\ell)\) have a neighbor labeled \(\mu\), because there are at most \(b\) edges between these two label classes. Therefore
\[
\Delta(F_\ell)\leq\Delta b.
\]

Greedily color each \(F_\ell\) with at most \(\Delta b+1\) colors. Split each nonempty color class into buckets of size at most \(r\).

Write \(q\) for the total number of buckets. Then
\[
\frac Nr\leq q
\leq \frac Nr+r(\Delta b+1).
\]
Since
\[
b=O_\Delta(N/r^2+1)
\quad\text{and}\quad r\leq\sqrt N,
\]
we obtain
\[
q=O_\Delta(N/r).
\]

Every bucket consists of vertices with one common label, so it is independent in \(X\). More importantly:

> **For each bucket \(B\) and each label \(\mu\), at most one edge of \(X\) joins \(B\) to a vertex labeled \(\mu\).**

Indeed, one vertex of \(B\) cannot have two neighbors of label \(\mu\), by proper coloring of \(X^2\). Two different vertices of \(B\) cannot both have such neighbors, by the definition of \(F_\ell\).

Let \(P\) be the quotient graph on the buckets. In particular, every edge of \(P\) corresponds to exactly one edge of \(X\).

### 1.3 The target and the lists

Define \(R\) to have vertex set
\[
[r]\times\{0,1,2,3\}^{r}.
\]
Thus \(h:=|V(R)|=r4^r\).

Two configurations \((\ell,\alpha)\) and \((\mu,\beta)\) are adjacent precisely when
\[
\ell\neq\mu,\qquad
\alpha_\mu,\beta_\ell\in\{1,2,3\},
\qquad
\alpha_\mu\neq\beta_\ell.
\]
This is a simple undirected graph.

Let \(B\) be a bucket of label \(\ell\). Each assignment
\[
c_B:B\longrightarrow\{1,2,3\}
\]
produces a configuration \((\ell,\alpha)\), where
\[
\alpha_\mu=
\begin{cases}
c_B(x),&\text{if }xy\in E(X),\ x\in B,\ \lambda(y)=\mu,\\
0,&\text{if no such edge exists}.
\end{cases}
\]
The preceding uniqueness property makes this well defined. Put all configurations obtained this way into \(\mathcal L(B)\). There are at most \(3^{|B|}\leq3^r\) of them.

A proper 3-coloring of \(X\) supplies a list homomorphism: on each quotient edge, target adjacency checks the colors of the endpoints of its unique original edge.

Conversely, choose for each list-selected configuration a witnessing assignment \(c_B\). These assignments combine into a coloring of \(X\), since buckets are independent. Every edge between buckets is properly colored by the target-adjacency test.

All construction steps take time polynomial in \(N+4^r\). This proves Lemma 2. \(\square\)

## 2. Removing lists with linear overhead

Here is the main improvement to the previous attempt’s gadget.

**Lemma 3.** Given a list-homomorphism instance \((P,R,\mathcal L)\) with
\[
|V(P)|=q,\qquad |V(R)|=h\geq1,
\]
one can construct, in polynomial time, an equivalent ordinary homomorphism instance \((S,T)\) with
\[
|V(S)|=q+27h+11,
\qquad
|V(T)|=28h+11.
\]
Both \(S\) and \(T\) are connected.

### 2.1 A linear-size critical anchor

Let \(A_t\) be the **complete join of \(t\) disjoint copies of \(C_5\)**: retain each cycle and add every edge between different cycles.

Then
\[
|V(A_t)|=5t,\qquad
\chi(A_t)=3t,\qquad
\omega(A_t)=2t.
\]
Moreover, for every \(v\in V(A_t)\),
\[
\chi(A_t-v)=3t-1.
\]
These statements follow from additivity of chromatic number and clique number under complete joins, and from \(C_5-v=P_4\).

Choose one edge in each cycle, and let \(D\) be the union of their endpoints. Thus \(D\) is a clique of size \(2t=\omega(A_t)\). In particular,

\[
\text{no vertex of }A_t\text{ is adjacent to every vertex of }D. \tag{1}
\]

Set
\[
t=5h+2,\qquad M=2h+1,
\]
and write \(A=A_t\). Choose distinct vertices
\[
p_1,\ldots,p_{M-1},z\in V(A)\setminus D.
\]
There are enough, since \(|V(A)\setminus D|=3t\).

Define
\[
D_i=D\cup\{p_1,\ldots,p_{i-1}\},
\qquad 1\leq i\leq M.
\]
Thus
\[
|D_i|=2t+i-1,\qquad z\notin D_M.
\]

### 2.2 The construction

Number \(V(R)=\{y_1,\ldots,y_h\}\).

The target \(T\) contains:

- the anchor \(A\);
- a marker clique \(q_1,\ldots,q_M\);
- a copy of \(R\).

Its cross edges are:

- \(q_i\) has neighborhood exactly \(D_i\) in \(A\);
- every \(y_j\) is adjacent to every vertex of \(D\cup\{z\}\);
- \(q_i y_j\) is an edge exactly when \(i\leq h\) and \(i\neq j\).

The source \(S\) contains the same anchor and marker clique, together with \(P\). Keep the same marker-to-anchor edges. For every \(x\in V(P)\):

- join \(x\) to every vertex of \(D\cup\{z\}\);
- join \(x\) to \(q_i\) for every \(i\in[h]\) such that \(y_i\notin\mathcal L(x)\).

There are no other cross edges.

A list homomorphism \(P\to R\) extends to \(S\to T\) by fixing the anchor and all markers. We prove the converse.

### 2.3 The anchor must map onto itself

There are \(M+h=3h+1\) vertices outside \(A\) in \(T\). Each has at most
\[
2t+2h
\]
neighbors in \(A\).

Fix \(v\in V(A)\), and start with a \((3t-1)\)-coloring of \(A-v\). Greedily color the outside vertices. At each step, at most
\[
(2t+2h)+(3h+1)-1
=2t+5h
=3t-2
\]
colors are forbidden. Hence
\[
\chi(T-v)\leq3t-1. \tag{2}
\]

Now let \(f:S\to T\) be a homomorphism. If \(f(A)\) omitted any anchor vertex \(v\), then (2) would yield a \((3t-1)\)-coloring of \(A\), contradicting \(\chi(A)=3t\).

Thus \(f(A)\) contains every vertex of the target anchor. The source and target anchors have the same order, so \(f|_A\) is a bijection onto \(A\), and hence an automorphism. Denote it by \(\sigma\).

### 2.4 The marker roles are fixed

Each marker is adjacent to all of \(D\). By (1), and because \(\sigma\) is an automorphism, no marker can map into \(A\).

The markers therefore map injectively to an \(M\)-clique outside \(A\). The only such clique is the marker clique. Indeed, a clique containing some \(y_j\) contains at most \(h\) vertices of \(R\) and at most \(h-1\) markers, for a total of at most
\[
2h-1<M.
\]

Consequently
\[
f(q_i)=q_{\pi(i)}
\]
for a permutation \(\pi\) of \([M]\). The marker-to-anchor edges imply
\[
\sigma(D_i)\subseteq D_{\pi(i)}.
\]
Taking cardinalities yields \(i\leq\pi(i)\) for every \(i\). Summing forces equality for every \(i\). Therefore
\[
f(q_i)=q_i,\qquad \sigma(D_i)=D_i. \tag{3}
\]

In particular, \(\sigma(z)\notin D_M\).

### 2.5 Data vertices land in their lists

Let \(x\in V(P)\). Its adjacency to all of \(D\) prevents \(f(x)\) from lying in \(A\), by (1).

It also cannot map to a marker. The edge \(xz\) would require that marker to be adjacent to \(\sigma(z)\), whereas every marker’s anchor neighborhood lies in \(D_M\), and \(\sigma(z)\notin D_M\).

Thus \(f(x)=y_j\) for some \(j\). For every forbidden index \(i\), the source edge \(xq_i\), together with (3), requires \(y_jq_i\in E(T)\). Hence \(j\neq i\). It follows that
\[
y_j\in\mathcal L(x).
\]
Edges of \(P\) map to edges of \(R\), so \(f|_P\) is the required list homomorphism.

Finally,
\[
|V(A)|=5t=25h+10.
\]
Adding the \(2h+1\) markers gives the stated orders. Connectedness follows because the anchor is connected and every marker and data vertex has a neighbor in it. This proves Lemma 3. \(\square\)

## 3. Choosing the parameter and balancing

Apply Lemma 2 with \(\Delta=5\) and, for sufficiently large \(N\),
\[
r=\left\lfloor\frac{\log N}{8}\right\rfloor.
\]
Its hypotheses hold for all sufficiently large \(N\). We obtain
\[
q=\Theta(N/r)
\]
and
\[
h=r4^r\leq rN^{1/4}
=o(N/r).
\]

Apply Lemma 3. The resulting ordinary instance has orders
\[
|V(S)|=q+27h+11,\qquad
|V(T)|=28h+11.
\]
In particular \(q\geq h\) for sufficiently large \(N\).

To balance the orders while retaining connectedness, add \(q-h\) **false twins** of a fixed vertex \(a\in V(T)\): each new vertex has neighborhood exactly \(N_T(a)\), and the new vertices are mutually nonadjacent.

Call the enlarged target \(T^+\). It contains \(T\), and it retracts onto \(T\): fix all old vertices and map every new twin to \(a\). Therefore, for every graph \(S\),
\[
S\to T^+\quad\Longleftrightarrow\quad S\to T.
\]
Since \(T\) is connected and \(a\) has positive degree, \(T^+\) remains connected.

Now
\[
|V(S)|=|V(T^+)|
=q+27h+11
=\Theta(N/\log N).
\]

All steps are polynomial-time in \(N\): here \(4^r\leq N^{1/4}\), lists have at most \(3^r\) entries per bucket, and the list-removal overhead is linear in \(h\).

The finitely many smaller input sizes can be handled directly. For example, output \(K_3\to K_3\) for a yes-instance and \(K_3\to P_3\) for a no-instance. Both pairs are balanced and connected.

This proves Theorem 1. \(\square\)

## 4. A self-contained connection to 3-SAT

For completeness, the needed bounded-degree coloring reduction does not require a literature assumption.

### 4.1 From 3-SAT to a linear-size 3-coloring instance

Replace each clause \(a\lor b\lor c\) by
\[
\operatorname{NAE}(a,b,s)
\quad\land\quad
\operatorname{NAE}(\neg s,c,F),
\]
where \(s\) is fresh and \(F\) is the constant false.

These two constraints have an extension in \(s\) exactly when \(a\lor b\lor c\) is true:

- if \(a=b=F\), the first forces \(s=T\), and the second then forces \(c=T\);
- if \(a=b=T\), take \(s=F\);
- if \(a\neq b\), again take \(s=F\).

Create a palette triangle with vertices \(T,F,B\). For every Boolean variable, create two adjacent literal vertices, both adjacent to \(B\). They must receive the two palette colors \(T,F\) in opposite orders.

For each \(\operatorname{NAE}(\ell_1,\ell_2,\ell_3)\) constraint, create a fresh triangle \(z_1z_2z_3\) and join \(z_i\) to \(\ell_i\). This triangle can be colored exactly when the literal colors are not all equal:

- if all are equal, its vertices have only two available colors;
- otherwise, assign color \(T\) to a triangle vertex whose literal has color \(F\), color \(F\) to one whose literal has color \(T\), and color \(B\) to the remaining vertex.

The graph has \(O(v+m)\) vertices and edges.

### 4.2 Reducing the maximum degree to five

Replace a vertex of degree \(d\geq1\) by \(d\) clones, one for each original incident edge. Force consecutive clones to have equal colors using the following gadget:

- add two adjacent auxiliary vertices;
- join both auxiliaries to both clones.

If the clones have different colors, both auxiliaries are forced to use the third color, contradicting their adjacency. If the clones have the same color, the auxiliaries can use the other two colors.

Every clone has one original-edge incidence and belongs to at most two equality gadgets. Its degree is consequently at most
\[
1+2+2=5.
\]
Auxiliary vertices have degree three. Isolated original vertices can simply be retained.

The construction has size linear in the number of original vertices and edges. Thus 3-SAT reduces to maximum-degree-five 3-coloring with
\[
N=O(v+m).
\]

Combining this with Theorem 1 proves the unconditional implication
\[
\boxed{
O(c^{|V(G)|+|V(H)|})\text{-time homomorphism}
\ \Longrightarrow\
2^{O((v+m)/\log(v+m))}\text{-time 3-SAT}.
}
\]

## 5. What the result settles—and what it does not

Assume **sparse ETH**, meaning that 3-SAT with \(m=O(v)\) has no deterministic \(2^{o(v)}\)-time algorithm. Then Theorem 1 and the preceding reduction imply:

> There is no \(2^{o(n\log n)}\)-time homomorphism algorithm even when both input graphs are connected and have exactly \(n\) vertices.

Indeed,
\[
n=\Theta(N/\log N)
\quad\Longrightarrow\quad
n\log n=\Theta(N).
\]
The straightforward enumeration of all \(n^n\) maps gives a \(2^{O(n\log n)}\) upper bound on balanced instances, so this is conditionally tight in the order of the exponent.

In particular, the proposed \(c^{|V(G)|+|V(H)|}\) running time would be \(c^{2n}=2^{O(n)}\) on these hard instances and is incompatible with sparse ETH.

This also identifies the issue with the catalog’s explanation: considering \(h\gg n\) does not protect an algorithm required to work on **all** inputs. Balanced hard instances already suffice. The independent proof above avoids relying on any missing quantifiers in the cited literature summaries.

**Remaining gap.** No unconditional nonexistence theorem follows. I have neither constructed the requested algorithm nor excluded the resulting faster SAT algorithm without a complexity assumption. The unconditional contribution here is the compression theorem and the linear-overhead list-removal construction; no novelty claim is made for their consequences.