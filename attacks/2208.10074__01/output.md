```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds with c=2 when deleting O(n^{1-ε}) vertices leaves bounded maximum degree, and with c=q+1 when O(n^{1-ε}) vertices suffice to reduce to treewidth q.",
  "would_publish": false,
  "caveats": "The extra modulator hypotheses are not consequences presently derived from strongly sublinear separators, so the unrestricted hereditary case remains open."
}
```

# Mathematical writeup

## 1. Statement and notation

Put
\[
\alpha:=1-\epsilon\in(0,1).
\]
Assume that there are constants \(A>0\) and \(\rho<1\), say \(\rho=2/3\), such that every \(k\)-vertex graph \(J\in\mathcal G\) has a set \(S\subseteq V(J)\) satisfying
\[
|S|\le A k^\alpha
\]
and every component of \(J-S\) has at most \(\rho k\) vertices.

For a graph \(G\), a representation
\[
G\subseteq H\boxtimes K_m
\]
is equivalent to a map
\[
\phi:V(G)\longrightarrow V(H)
\]
such that

1. \(|\phi^{-1}(x)|\le m\) for every \(x\in V(H)\), and
2. for every edge \(uv\in E(G)\), either \(\phi(u)=\phi(v)\) or \(\phi(u)\phi(v)\in E(H)\).

Indeed, one labels the vertices in each fibre injectively by \(V(K_m)\).

The general problem remains unresolved below. I prove an exact-exponent special case and isolate the obstruction to the standard recursive argument.

---

## 2. Basic consequences of the separator hypothesis

### Lemma 2.1: Passage to arbitrary subgraphs

Let \(\mathcal G^\downarrow\) be the class of all subgraphs of graphs in \(\mathcal G\). Then every \(k\)-vertex graph \(F\in\mathcal G^\downarrow\) has a balanced separator of order at most \(Ak^\alpha\).

#### Proof

Choose \(G\in\mathcal G\) containing \(F\) as a subgraph, and let
\[
J:=G[V(F)].
\]
Since \(\mathcal G\) is hereditary, \(J\in\mathcal G\). A balanced separator of \(J\) is also a balanced separator of \(F\), since deleting edges cannot merge components. ∎

Thus, for separator purposes, one may replace the hereditary class by its monotone closure.

### Lemma 2.2: Treewidth has the same exponent

There is a constant \(B=B(A,\alpha,\rho)\) such that
\[
\operatorname{tw}(G)+1\le B|V(G)|^\alpha
\]
for every \(G\in\mathcal G\).

#### Proof

Let \(w(n)\) be the maximum of \(\operatorname{tw}(J)+1\) over \(n\)-vertex graphs \(J\in\mathcal G\). For an \(n\)-vertex \(J\), choose a balanced separator \(S\). Recursively decompose each component \(C\) of \(J-S\), add \(S\) to every bag of the decomposition of \(J[C]\), and connect these decompositions through a central bag \(S\). This gives
\[
w(n)\le An^\alpha+\max_{|C|\le \rho n}w(|C|).
\]
Iterating,
\[
w(n)\le An^\alpha\sum_{i\ge 0}\rho^{\alpha i}+O(1)
 \le \frac{A}{1-\rho^\alpha}n^\alpha+O(1).
\]
The \(O(1)\) term can be absorbed into \(Bn^\alpha\). ∎

This is also the scale forced by any desired product representation: if
\[
G\subseteq H\boxtimes K_m,\qquad \operatorname{tw}(H)\le c,
\]
then replacing every bag of a width-\(c\) tree-decomposition of \(H\) by its product with \(V(K_m)\) gives
\[
\operatorname{tw}(G)+1\le (c+1)m.
\]

Thus the separator hypothesis gives the correct necessary treewidth bound, but bounded treewidth of the quotient is a stronger requirement.

### Lemma 2.3: Uniform clique and biclique exclusion

There is an integer \(s=s(A,\alpha)\) such that no graph in \(\mathcal G\) contains \(K_s\) or \(K_{s,s}\) as a subgraph.

#### Proof

A balanced separator in \(K_t\) has order at least \(t/3\). By Lemma 2.1,
\[
\frac t3\le At^\alpha,
\]
which bounds \(t\).

Similarly, a balanced separator in \(K_{t,t}\) has order at least \(2t/3\): after deleting fewer than \(2t/3\) vertices, if both bipartition classes remain nonempty, the remaining connected component has more than \(4t/3\) vertices. Hence
\[
\frac{2t}{3}\le A(2t)^\alpha,
\]
again bounding \(t\). ∎

This rules out simple dense blow-up counterexamples, but it does not by itself yield a bounded-treewidth quotient.

---

## 3. An exact-exponent partial theorem

I use the standard linear tree-partition theorem:

> **Tree-partition theorem.** There is an absolute constant \(C_0\) such that every graph \(J\) of treewidth at most \(k\) and maximum degree at most \(\Delta\) admits a partition indexed by a forest \(T\), with every part of size at most
> \[
> C_0(k+1)(\Delta+1),
> \]
> such that every edge of \(J\) has both ends in one part or in parts corresponding to adjacent vertices of \(T\).

Equivalently,
\[
J\subseteq T\boxtimes K_{C_0(k+1)(\Delta+1)}.
\]
Only the asymptotic \(O(k\Delta)\) form is needed here. This is the standard linear bound for tree-partition width; see, for example, D. R. Wood, *On tree-partition-width*, European J. Combin. 30 (2009), 1245–1253.

### Theorem 3.1

Suppose, in addition to the separator hypothesis, that there are constants \(D,\Delta\) such that every \(n\)-vertex \(G\in\mathcal G\) has a set \(X\subseteq V(G)\) with
\[
|X|\le Dn^\alpha
\qquad\text{and}\qquad
\Delta(G-X)\le \Delta.
\]
Then every such \(G\) satisfies
\[
G\subseteq H\boxtimes K_m,
\]
where
\[
\operatorname{tw}(H)\le 2
\qquad\text{and}\qquad
m=O(n^\alpha).
\]

In particular, the original conjecture holds with \(c=1\) for every uniformly bounded-degree hereditary class with strongly sublinear separators.

#### Proof

Let \(J:=G-X\). By Lemma 2.2,
\[
\operatorname{tw}(J)+1\le Bn^\alpha.
\]
Since \(\Delta(J)\le\Delta\), the tree-partition theorem gives a forest \(T\) and a map
\[
\psi:V(J)\to V(T)
\]
whose fibres have size at most
\[
C_0B(\Delta+1)n^\alpha,
\]
and such that every edge of \(J\) maps within one forest vertex or across a forest edge.

Add a new vertex \(z\) adjacent to every vertex of \(T\), and call the resulting graph \(H\). A cone over a forest has treewidth at most \(2\). Define
\[
\phi(v)=
\begin{cases}
z,&v\in X,\\
\psi(v),&v\in V(J).
\end{cases}
\]
Edges inside \(X\) are supported within the fibre over \(z\); every edge between \(X\) and \(J\) is supported because \(z\) is universal; and edges inside \(J\) are supported by the tree-partition.

The largest fibre has size at most
\[
\max\{Dn^\alpha,\ C_0B(\Delta+1)n^\alpha\}=O(n^\alpha).
\]
Thus \(G\subseteq H\boxtimes K_m\) with \(\operatorname{tw}(H)\le2\). If \(X=\varnothing\), one may take \(H=T\), giving \(c=1\). ∎

### A second sufficient condition

There is an even simpler modulator version.

### Proposition 3.2

Suppose every \(n\)-vertex \(G\in\mathcal G\) has a set \(X\) satisfying
\[
|X|=O(n^\alpha)
\qquad\text{and}\qquad
\operatorname{tw}(G-X)\le q
\]
for a fixed \(q\). Then the conjectured conclusion holds with \(c=q+1\).

#### Proof

Let \(J=G-X\), and let \(H\) be obtained from \(J\) by adding one universal vertex \(z\). Map all vertices of \(X\) to \(z\), and map each vertex of \(J\) to its corresponding vertex of \(H\). The fibres have size at most \(\max\{|X|,1\}=O(n^\alpha)\). Adding a universal vertex raises treewidth by at most one, so
\[
\operatorname{tw}(H)\le q+1.
\]
∎

---

## 4. The treewidth-two bound in Theorem 3.1 can be necessary

The high-degree part cannot in general be handled while retaining a forest quotient.

Let \(F_N\) be the fan consisting of a path
\[
v_1v_2\cdots v_N
\]
and a vertex \(a\) adjacent to every \(v_i\). The hereditary closure of the fans has treewidth at most \(2\), and consequently has uniformly bounded separators.

### Proposition 4.1

If
\[
F_N\subseteq T\boxtimes K_m
\]
for a forest \(T\), then
\[
N\le m^2+m-1.
\]
In particular, \(m=\Omega(\sqrt N)\).

#### Proof

Let \(x\in V(T)\) be the coordinate of \(a\). Every path vertex not mapped to \(x\) must be mapped to a neighbour of \(x\), because it is adjacent to \(a\).

Let \(R\) be the set of path vertices mapped to \(x\). Since the fibre over \(x\) also contains \(a\),
\[
|R|\le m-1.
\]
Deleting \(R\) from the path leaves at most \(|R|+1\le m\) intervals.

Consider one such interval. Consecutive vertices in it are mapped to neighbours of \(x\). Two distinct neighbours of \(x\) cannot be adjacent in a forest, since that would create a triangle with \(x\). Hence every vertex of the interval is mapped to the same forest vertex. Its length is therefore at most \(m\).

Thus
\[
N\le |R|+m\cdot m\le m-1+m^2.
\]
∎

Consequently, for every \(\alpha<1/2\), this hereditary class has \(O(1)\), hence \(O(n^\alpha)\), separators, but it does not admit the desired representation with \(c=1\) and \(m=O(n^\alpha)\). On the other hand, Theorem 3.1 applies with \(X=\{a\}\), and \(c=2\) works. Thus the increase from treewidth \(1\) to \(2\) in that partial theorem is genuine.

---

## 5. Why the direct recursive-separator construction misses the exponent

The following calculation precisely describes the obstruction in the standard proof.

### Lemma 5.1: Fragmentation by accumulated separators

For every \(1\le r\le n\), every \(n\)-vertex \(G\in\mathcal G\) has a set \(X\) such that every component of \(G-X\) has at most \(r\) vertices and
\[
|X|\le C_\alpha\,\frac{n}{r^{1-\alpha}},
\]
where \(C_\alpha\) depends only on \(A,\alpha,\rho\).

#### Proof

Recursively apply balanced separators to every current part of order greater than \(r\). Consider recursion nodes whose orders lie in
\[
[r\rho^{-j},\,r\rho^{-(j+1)}).
\]
No two such nodes are comparable in the recursion tree, because passing to a child multiplies order by at most \(\rho\). Hence their vertex sets are pairwise disjoint, and the sum of their orders is at most \(n\).

For a node of order \(x\) in this range,
\[
x^\alpha=x\,x^{\alpha-1}
 \le x\,(r\rho^{-j})^{\alpha-1}.
\]
Thus the total number of separator vertices contributed by this range is at most
\[
Anr^{\alpha-1}\rho^{j(1-\alpha)}.
\]
Summing over \(j\ge0\) gives
\[
|X|
 \le \frac{A}{1-\rho^{1-\alpha}}\,
       nr^{\alpha-1}.
\]
The terminal components have order at most \(r\). ∎

Putting \(X\) in the centre of a star and every component in a leaf gives
\[
m=O\left(\max\left\{\frac{n}{r^{1-\alpha}},r\right\}\right).
\]
Optimizing at
\[
r\asymp n^{1/(2-\alpha)}
\]
gives
\[
m=O\left(n^{1/(2-\alpha)}\right),
\]
whose exponent is strictly larger than \(\alpha\).

More generally, suppose one repeats this construction for \(t\) levels, each time putting the accumulated separator into a universal quotient vertex. Let \(p_t\) denote the resulting exponent, with \(p_0=1\). Balancing
\[
\frac{n}{r^{1-\alpha}}
\quad\text{against}\quad
r^{p_{t-1}}
\]
gives
\[
p_t=\frac{p_{t-1}}{p_{t-1}+1-\alpha}.
\]
Writing \(q=1-\alpha\), one obtains
\[
\frac1{p_t}=1+q\frac1{p_{t-1}},
\]
and hence
\[
p_t=\frac{\alpha}{1-(1-\alpha)^{t+1}}.
\]
Therefore
\[
p_t>\alpha
\]
for every fixed \(t\), although \(p_t\downarrow\alpha\). This reproduces the basic exponent-slack phenomenon in the source paper. It also explains why merely iterating separators and coning over the recursive quotients cannot prove the conjecture: every coning step consumes one unit of quotient treewidth, while finitely many such steps leave a positive exponent gap.

This is only a limitation of that construction, not a lower bound against all possible product representations.

---

## 6. Endpoint \(\epsilon=1\)

If \(\alpha=0\), the separation number is uniformly bounded. By Lemma 2.1 the same is true for every subgraph, and the standard equivalence between separation number and treewidth then gives uniformly bounded treewidth. Thus one may simply take
\[
H=G,\qquad m=1.
\]
So the endpoint \(\epsilon=1\) is affirmative.

---

## 7. Remaining gap

The exact result above covers:

- uniformly bounded maximum degree, with \(c=1\);
- graphs that become bounded-degree after deleting \(O(n^{1-\epsilon})\) vertices, with \(c=2\);
- graphs with an \(O(n^{1-\epsilon})\)-vertex modulator to bounded treewidth.

The separator hypothesis alone has not been shown to provide either type of modulator. For example, forests can have many high-degree vertices, so simply collecting all high-degree vertices is not a viable general strategy, even though forests themselves already have quotient treewidth \(1\).

The unresolved step is therefore to control nested high-degree or high-attachment structures without paying one additional unit of quotient treewidth at every separator scale. The calculations in Section 5 show that the straightforward recursive-cone construction cannot reach the exact exponent with boundedly many levels. No proof or counterexample for the unrestricted hereditary case is obtained here.