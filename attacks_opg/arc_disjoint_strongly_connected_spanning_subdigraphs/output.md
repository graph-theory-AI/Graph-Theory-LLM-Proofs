```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A thin-tree and circulation argument gives an explicit O(log n / log log n) connectivity bound for Eulerian digraphs, but does not yield an absolute bound for general digraphs.",
  "would_publish": false,
  "caveats": "The result is restricted to Eulerian digraphs and its bound grows with n; novelty of this partial result is not claimed."
}
```

## 1. A quantitative Eulerian special case

I do not resolve the stated conjecture. The following is a precise partial result, with a proof using spanning-tree packing, matroid rounding, and integral flows.

All digraphs below are finite and loopless; parallel arcs are permitted, although the result applies in particular to simple digraphs. Write
\[
d_D^+(X)=|\delta_D^+(X)|,\qquad d_D^-(X)=|\delta_D^-((X))|.
\]
A digraph is \(k\)-arc-connected if \(d_D^+(X)\ge k\) for every nonempty proper vertex set \(X\). Call it Eulerian if every vertex has equal indegree and outdegree.

### Theorem
Let \(D\) be an Eulerian \(k\)-arc-connected digraph on \(n\ge2\) vertices. Suppose that \(k>8\) and
\[
\boxed{\quad k\ln(k/8)\ \ge\ 2\ln\bigl(3(n-1)\bigr).\quad} \tag{1}
\]
Then \(A(D)\) can be partitioned into two strongly connected spanning **Eulerian** subdigraphs.

Consequently, for every fixed \(\varepsilon>0\) and all sufficiently large \(n\), the condition
\[
k\ge \left\lceil(2+\varepsilon)\frac{\ln n}{\ln\ln n}\right\rceil
\]
suffices in the Eulerian case.

The proof has two main ingredients:

* Find two edge-disjoint spanning trees whose union uses at most half the edges of every underlying undirected cut.
* Use an integral circulation to extend one tree to an Eulerian subdigraph while avoiding the other tree.

The orientation of each tree is inherited from \(D\); a tree itself need not be an in- or out-branching.

## 2. A weighted cut bound

We first record a useful elementary consequence of spanning-tree packing.

### Lemma 1
Let \(G\) be an undirected multigraph on \(n\) vertices containing \(k\) edge-disjoint spanning trees. Fix a vertex \(r\), and let
\[
\mathcal C=\{X:\varnothing\ne X\subseteq V(G)\setminus\{r\}\}.
\]
Thus \(\mathcal C\) represents every nontrivial unordered cut exactly once. For \(0<q<1\),
\[
\sum_{X\in\mathcal C}q^{|\delta_G(X)|}
\le (1+q^k)^{n-1}-1. \tag{2}
\]

#### Proof
Let \(T_1,\dots,T_k\) be edge-disjoint spanning trees. Since
\[
|\delta_G(X)|\ge \sum_{i=1}^k|\delta_{T_i}(X)|,
\]
Hölder’s inequality gives
\[
\begin{aligned}
\sum_{X\in\mathcal C}q^{|\delta_G(X)|}
&\le
\sum_{X\in\mathcal C}\prod_{i=1}^kq^{|\delta_{T_i}(X)|}\\
&\le
\prod_{i=1}^k
\left(\sum_{X\in\mathcal C}q^{k|\delta_{T_i}(X)|}\right)^{1/k}.
\end{aligned}
\]

For a tree \(T\), the map \(X\mapsto\delta_T(X)\) is a bijection from \(\mathcal C\) to the nonempty subsets of \(E(T)\). Indeed, given an edge subset, the membership of each vertex in \(X\) is determined by parity along its path from \(r\). Therefore
\[
\sum_{X\in\mathcal C}q^{k|\delta_T(X)|}
=\sum_{\varnothing\ne F\subseteq E(T)}q^{k|F|}
=(1+q^k)^{n-1}-1.
\]
Substitution proves (2). \(\square\)

## 3. Rounding a union of two spanning trees

We need a negatively correlated distribution on unions of two spanning trees. For completeness, the relevant rounding fact is proved here.

### Lemma 2
Let \(x\) be a convex combination of bases of a finite matroid. There is a random base \(B\) such that, for every subset \(F\) of the ground set,
\[
\Pr(F\subseteq B)\le \prod_{e\in F}x_e. \tag{3}
\]

#### Proof
Maintain a convex combination of bases. Consider two bases \(B_1,B_2\) having positive coefficients \(a,b\). If they differ, choose
\[
e\in B_1\setminus B_2.
\]
By symmetric basis exchange, there is \(f\in B_2\setminus B_1\) for which both
\[
B_1-e+f,\qquad B_2-f+e
\]
are bases.

With probability \(b/(a+b)\), replace \(B_1\) by \(B_1-e+f\). Otherwise replace \(B_2\) by \(B_2-f+e\). The current fractional vector changes only in coordinates \(e,f\), by respectively
\[
a(\mathbf 1_f-\mathbf 1_e)
\quad\text{or}\quad
b(\mathbf 1_e-\mathbf 1_f).
\]
Its conditional expected change is zero.

For a fixed \(F\), the function
\[
\prod_{g\in F}x_g
\]
is concave along this two-coordinate direction: it is constant or linear if \(F\) contains at most one of \(e,f\), and is a nonnegative multiple of a concave quadratic otherwise. Consequently its conditional expectation cannot increase.

Each exchange decreases the symmetric difference of the two selected bases. When they coincide, merge their coefficients. Repeating terminates at a single random base \(B\). At termination,
\[
\prod_{e\in F}x_e=\mathbf 1_{\{F\subseteq B\}},
\]
so the preceding supermartingale inequality proves (3). \(\square\)

We use the standard matroid-union theorem: the edge sets of an undirected graph that can be partitioned into two forests form a matroid. If the graph contains two edge-disjoint spanning trees, this matroid has rank \(2(n-1)\), and each of its bases is a union of two edge-disjoint spanning trees.

### Lemma 3
Let \(G\) contain \(k\) edge-disjoint spanning trees, where \(k>8\) satisfies (1). Then \(G\) has two edge-disjoint spanning trees \(T_R,T_B\) such that
\[
|\delta_{T_R\cup T_B}(X)|
\le \frac12|\delta_G(X)|
\qquad
(\varnothing\ne X\ne V(G)). \tag{4}
\]

#### Proof
Choose edge-disjoint spanning trees \(T_1,\dots,T_k\). In the two-forest matroid, each \(T_i\cup T_j\) is a base. The average of these bases is the vector
\[
x_e=
\begin{cases}
2/k,&e\in \bigcup_i E(T_i),\\
0,&\text{otherwise}.
\end{cases}
\]
Apply Lemma 2 to obtain a random base \(B\). It is a union of two edge-disjoint spanning trees.

Fix a cut with \(c=|\delta_G(X)|\), and put
\[
Z=|B\cap\delta_G(X)|,\qquad p=2/k.
\]
For \(s>0\), expanding the product and using (3) yields
\[
\begin{aligned}
\mathbb E e^{sZ}
&=\mathbb E\prod_{e\in\delta_G(X)}
   \bigl(1+(e^s-1)\mathbf 1_{\{e\in B\}}\bigr)\\
&\le \prod_{e\in\delta_G(X)}
   \bigl(1+(e^s-1)x_e\bigr)\\
&\le (1-p+pe^s)^c.
\end{aligned}
\]
Because \(p<1/2\), choosing \(e^s=(1-p)/p\) gives
\[
\Pr(Z\ge c/2)
\le \bigl(2\sqrt{p(1-p)}\bigr)^c
\le (8/k)^{c/2}. \tag{5}
\]

Set \(q=\sqrt{8/k}<1\). By a union bound over unordered cuts and Lemma 1,
\[
\Pr\left(\exists X:\ |B\cap\delta_G(X)|>\frac12|\delta_G(X)|\right)
\le (1+q^k)^{n-1}-1.
\]
Condition (1) implies
\[
(n-1)q^k
=(n-1)(8/k)^{k/2}\le \frac13.
\]
Hence the preceding probability is at most
\[
e^{1/3}-1<\frac12.
\]
In particular, a base \(B\) satisfying (4) exists. Partition it into its two spanning trees. \(\square\)

## 4. Completing the trees by an integral flow

### Lemma 4
Let \(D\) be Eulerian, and form an undirected multigraph \(G\) by replacing every arc of \(D\) by a separately labelled undirected edge. Suppose \(G\) has edge-disjoint spanning trees \(T_R,T_B\) satisfying (4). Then \(D\) has a partition into two strongly connected spanning Eulerian subdigraphs.

#### Proof
Interpret \(T_R,T_B\) as arc sets, retaining their orientations in \(D\). We will require all arcs of \(T_R\) to be red and all arcs of \(T_B\) to be blue.

Let
\[
R=A(D)\setminus(T_R\cup T_B),
\]
and define
\[
a(v)=d^-_{T_R}(v)-d^+_{T_R}(v).
\]
We seek a \(0\)-\(1\) flow \(f\) on \(R\) satisfying
\[
d_f^+(v)-d_f^-(v)=a(v). \tag{6}
\]
Then adding the arcs with \(f_e=1\) to \(T_R\) makes the red subdigraph Eulerian.

The integral max-flow/min-cut theorem says that such a flow exists precisely when
\[
\sum_{v\in X}a(v)\le d_R^+(X)
\qquad(X\subseteq V(D)).
\]
Here the inequality is equivalent to
\[
d^-_{T_R}(X)+d^+_{T_B}(X)\le d_D^+(X). \tag{7}
\]
But
\[
d^-_{T_R}(X)+d^+_{T_B}(X)
\le |\delta_{T_R\cup T_B}(X)|
\le \frac12|\delta_G(X)|.
\]
Since \(D\) is Eulerian, every cut is balanced, so
\[
\frac12|\delta_G(X)|=d_D^+(X).
\]
Thus (7) holds for every \(X\), and an integral flow satisfying (6) exists.

Color \(T_R\) and the flow arcs red, and all remaining arcs blue. The red subdigraph is Eulerian by construction. The blue subdigraph is Eulerian because it is the complement of an Eulerian arc set in an Eulerian digraph. Their underlying graphs are connected because they contain \(T_R\) and \(T_B\), respectively.

Finally, a finite Eulerian digraph with connected underlying graph is strongly connected. Otherwise a source component of its condensation has no entering arcs; cut balance then forces it to have no leaving arcs either, contradicting underlying connectivity.

Both colors therefore give strongly connected spanning subdigraphs. \(\square\)

### Proof of the theorem

For the underlying multigraph \(G\),
\[
|\delta_G(X)|
=d_D^+(X)+d_D^-(X)
=2d_D^+(X)\ge2k.
\]
Thus \(G\) is \(2k\)-edge-connected.

The Nash–Williams–Tutte spanning-tree packing theorem gives \(k\) edge-disjoint spanning trees. Indeed, for a partition into \(r\ge2\) nonempty parts, the number of edges between parts is at least
\[
\frac12(2kr)=kr\ge k(r-1),
\]
which verifies the theorem’s partition condition.

Now apply Lemma 3 and then Lemma 4.

For the asymptotic consequence, if
\[
k=\left\lceil(2+\varepsilon)\frac{\ln n}{\ln\ln n}\right\rceil,
\]
then
\[
k\ln(k/8)=(2+\varepsilon+o(1))\ln n,
\]
which exceeds \(2\ln(3(n-1))\) for sufficiently large \(n\). \(\square\)

## 5. A small obstruction: \(k=2\) does not suffice

For completeness, there is a simple four-vertex obstruction, itself Eulerian.

Take vertices \(\mathbb Z/4\mathbb Z\), with arcs
\[
i\longrightarrow i-1,
\qquad
i\longrightarrow i+2
\quad(i\in\mathbb Z/4\mathbb Z).
\]
This digraph has eight arcs and indegree and outdegree two at every vertex.

It is 2-arc-connected:

* A singleton or its complement has outgoing cut size two.
* For a two-vertex set \(X\),
  \[
  d^+(X)=4-|A(D[X])|\ge2.
  \]

If it had two arc-disjoint strong spanning subdigraphs, each would need at least four arcs. Since there are only eight arcs, each would have exactly four and hence would be a directed Hamilton cycle.

There is, however, only one directed Hamilton cycle. If a four-cycle uses \(a\) arcs of increment \(2\), its total increment modulo \(4\) is
\[
2a-(4-a)\equiv3a\pmod4.
\]
Closure forces \(a=0\) or \(a=4\). The latter only traverses opposite pairs and is not a Hamilton cycle. Thus the only Hamilton cycle consists of all four increment-\(-1\) arcs. Its complement consists of two directed 2-cycles.

Therefore any universal constant in the original conjecture must be at least three.

## 6. Remaining gap

The partial theorem does **not** establish the conjecture, for two separate reasons.

1. **The connectivity threshold grows with \(n\).**  
   The argument supplies no absolute constant, even under the Eulerian restriction.

2. **Eulerian balance is essential to the completion step.**  
   It makes underlying cut size equal to twice outgoing cut size, and it ensures that both complementary flow-defined subdigraphs are Eulerian. Without balance, containing an undirected spanning tree does not imply strong connectivity.

Thus the argument proves a quantitative special case—indeed with both parts Eulerian—but supplies neither a universal \(k\) for arbitrary digraphs nor counterexamples of unbounded arc-connectivity. I have not verified whether this particular quantitative bound is already in the literature, so I make no novelty claim.