```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove decomposition theorems for directed expanders and for digraphs of bounded total degree imbalance, but neither yields a universal connectivity constant.",
  "would_publish": false,
  "caveats": "Extra hypotheses remain necessary for these arguments; novelty and the latest literature status have not been independently checked."
}
```

# Partial results

I do not prove or disprove the existence of an absolute \(k\) for arbitrary digraphs. I obtain two precise special-case results:

1. A **constant threshold for directed expanders with controlled maximum degree**, without an Eulerian assumption.
2. An extension of the previous attempt’s quantitative Eulerian result to digraphs with **bounded total degree imbalance**.

The first uses a different method. For the second, I recheck the previous attempt’s tree-rounding and circulation arguments and prove the additional steps needed outside the Eulerian case.

Throughout, digraphs are finite and loopless. Parallel arcs are allowed, but all results apply to simple digraphs. Let
\[
d_D^\pm(X)=|\delta_D^\pm(X)|.
\]
Thus \(D\) is \(k\)-arc-connected if \(d_D^+(X)\ge k\) for every nonempty proper \(X\subset V(D)\). Applying this to complements also gives \(d_D^-(X)\ge k\).

A spanning subdigraph is strongly connected exactly when every nonempty proper vertex set has an outgoing arc.

---

## 1. A constant-threshold result for directed expanders

Let \(U(D)\) be the underlying **simple** undirected graph: two vertices are adjacent when at least one arc joins them in either direction. Write
\[
\Delta=\Delta(U(D)).
\]

### Theorem 1
Let \(D\) have \(n\ge2\) vertices. Suppose that, for every \(X\) with
\(0<|X|\le n/2\),
\[
\boxed{\qquad
\min\{d_D^+(X),d_D^-(X)\}
\ge |X|\log_2\!\bigl(32(\Delta+1)\bigr).
\qquad} \tag{1}
\]
Then \(A(D)\) can be partitioned into two strongly connected spanning subdigraphs.

No balance condition on the indegrees and outdegrees is required.

### Proof

Color every arc independently red or blue with equal probability. We apply the asymmetric Lovász local lemma, in its standard form:

> If events \(E_i\) have a dependency graph and numbers \(0<x_i<1\) satisfy
> \[
> \Pr(E_i)\le x_i\prod_{j\sim i}(1-x_j),
> \]
> then the probability of avoiding all events is positive.

#### Counting connected vertex sets

In a graph of maximum degree \(\Delta\), the number of connected sets of size \(t\) containing a specified vertex is at most
\[
(4\Delta)^{t-1}. \tag{2}
\]
Indeed, choose a deterministic rooted, ordered spanning tree for each such set. There are at most \(4^{t-1}\) rooted ordered tree shapes with \(t\) vertices, and at most \(\Delta^{t-1}\) choices for the successive neighbor labels.

#### Bad events and their dependencies

For every nonempty \(X\) with \(|X|\le n/2\) and \(U(D)[X]\) connected, introduce four bad events:

- no red arc leaves \(X\);
- no blue arc leaves \(X\);
- no red arc enters \(X\);
- no blue arc enters \(X\).

By (1), each event associated with \(X\) has probability at most
\[
\bigl(32(\Delta+1)\bigr)^{-|X|}. \tag{3}
\]

An event associated with \(X\) depends only on arc colors on the boundary of \(X\). Two events have disjoint sets of relevant arc variables unless their vertex sets intersect or are adjacent in \(U(D)\).

Let \(N[X]\) denote the closed neighborhood of \(X\). For \(|X|=s\), we have
\[
|N[X]|\le(\Delta+1)s.
\]
Consequently, by (2), the number of possible neighboring events associated with sets of size \(t\) is at most
\[
4(\Delta+1)s(4\Delta)^{t-1}. \tag{4}
\]

Set
\[
z=\frac1{16(\Delta+1)},\qquad x_E=z^{|X|}
\]
for an event associated with \(X\). Equations (2)–(4) give
\[
\begin{aligned}
\sum_{F\sim E}x_F
&\le
4(\Delta+1)s
\sum_{t\ge1}(4\Delta)^{t-1}z^t\\
&=
\frac{4(\Delta+1)sz}{1-4\Delta z}
\le \frac{s}{3}.
\end{aligned}
\]
All \(x_F\le1/2\), so \(\log(1-x_F)\ge-2x_F\), and hence
\[
\prod_{F\sim E}(1-x_F)\ge e^{-2s/3}.
\]
It follows that
\[
x_E\prod_{F\sim E}(1-x_F)
\ge
\left(\frac1{16e^{2/3}(\Delta+1)}\right)^s
\ge
\left(\frac1{32(\Delta+1)}\right)^s.
\]
Together with (3), this verifies the local-lemma condition. Therefore a coloring avoiding all bad events exists.

#### Why avoiding these events gives strong connectivity

Suppose the red subdigraph is not strong. There is a nonempty proper \(S\) with no red arc leaving \(S\).

- If \(|S|\le n/2\), take a connected component \(X\) of \(U(D)[S]\). There are no arcs of \(D\) between different such components, so no red arc leaves \(X\), contradicting avoidance of its bad event.
- If \(|S|>n/2\), let \(T=V(D)\setminus S\). No red arc enters \(T\). A connected component of \(U(D)[T]\) then gives an avoided incoming-cut event.

Thus the red subdigraph is strong. The same argument applies to blue. \(\square\)

### A constant-connectivity corollary

Fix constants \(C\ge1\) and \(0<\varepsilon\le1\). Define
\[
k_0=
\left\lceil
\frac{2}{\varepsilon}
\log_2\!\left(\frac{64C}{\varepsilon}\right)
\right\rceil.
\]

Every \(k\)-arc-connected digraph, with \(k\ge k_0\), satisfying
\[
\Delta(U(D))\le Ck
\]
and
\[
d_D^\pm(X)\ge\varepsilon k|X|
\qquad(0<|X|\le n/2)
\]
has a strong arc decomposition.

To check the constants, put
\[
y=\varepsilon k,\qquad
L=\log_2(64C/\varepsilon).
\]
Then \(y\ge2L\ge12\), and
\[
\log_2(32(\Delta+1))
\le\log_2(64Ck)
=L+\log_2 y
\le L+y/2
\le y.
\]
Thus Theorem 1 applies.

This gives an absolute threshold within each fixed directed-expander class, independent of \(n\).

---

## 2. Extending the Eulerian bound to bounded imbalance

Define the total degree imbalance
\[
b=b(D):=
\sum_{v\in V(D)}
\max\{d_D^+(v)-d_D^-(v),0\}
=
\frac12\sum_v|d_D^+(v)-d_D^-(v)|.
\]
For every \(X\subseteq V(D)\),
\[
\left|d_D^+(X)-d_D^-(X)\right|\le b. \tag{5}
\]

### Theorem 2
Let \(D\) be a \(k\)-arc-connected digraph on \(n\ge2\) vertices, and put
\[
m=b(D)+2.
\]
Suppose
\[
k>4m
\]
and
\[
\boxed{\qquad
k\ln\!\left(\frac{k}{4m}\right)
-b(D)\ln\!\left(\frac{k}{m}\right)
\ge 2\ln\bigl(3(n-1)\bigr).
\qquad} \tag{6}
\]
Then \(A(D)\) can be partitioned into two strongly connected spanning subdigraphs, one of which is Eulerian.

In particular, for every fixed \(b_0\) and \(\varepsilon>0\), all sufficiently large \(n\) satisfy the following:

> Every digraph with \(b(D)\le b_0\) and arc-connectivity at least
> \[
> \left\lceil(2+\varepsilon)\frac{\ln n}{\ln\ln n}\right\rceil
> \]
> has a strong arc decomposition.

When \(b=0\), condition (6) becomes exactly the explicit Eulerian condition in the previous attempt. Both parts are then Eulerian.

### 2.1. Packing underlying spanning trees

Replace every arc of \(D\) by a separately labeled undirected edge, obtaining a multigraph \(G\). For every nontrivial cut,
\[
|\delta_G(X)|=d_D^+(X)+d_D^-(X)\ge2k.
\]
The Nash–Williams–Tutte spanning-tree packing theorem therefore supplies \(k\) edge-disjoint spanning trees.

Explicitly, for a partition into \(r\ge2\) nonempty parts, summing the \(2k\) lower bounds on their boundaries shows that there are at least \(kr\ge k(r-1)\) edges between parts, as required by the packing theorem.

We next find a suitably sparse union of \(m\) of these trees—not necessarily members of the original packing.

### 2.2. A weighted cut estimate

Fix a root \(r\), and let
\[
\mathcal C=\{X:\varnothing\ne X\subseteq V(G)\setminus\{r\}\}.
\]
This represents each nontrivial unordered cut once.

If \(G\) contains \(k\) edge-disjoint spanning trees, then, for \(0<q<1\),
\[
\sum_{X\in\mathcal C}q^{|\delta_G(X)|}
\le (1+q^k)^{n-1}-1. \tag{7}
\]

To prove this, let \(T_1,\ldots,T_k\) be such a packing. Hölder’s inequality gives
\[
\begin{aligned}
\sum_{X\in\mathcal C}q^{|\delta_G(X)|}
&\le
\sum_{X\in\mathcal C}
\prod_{i=1}^kq^{|\delta_{T_i}(X)|}\\
&\le
\prod_{i=1}^k
\left(
\sum_{X\in\mathcal C}q^{k|\delta_{T_i}(X)|}
\right)^{1/k}.
\end{aligned}
\]
For a tree \(T\), the map \(X\mapsto\delta_T(X)\) is a bijection from \(\mathcal C\) to the nonempty subsets of \(E(T)\): recover membership in \(X\) by parity along paths from \(r\). Thus every factor inside the product equals
\[
(1+q^k)^{n-1}-1,
\]
proving (7).

### 2.3. Rounding a union of \(m\) trees

We use the following matroid rounding fact:
if \(x\) is a convex combination of bases of a finite matroid, there is a random base \(B\) satisfying
\[
\Pr(F\subseteq B)\le\prod_{e\in F}x_e
\qquad\text{for every }F. \tag{8}
\]

Here is a verification. Select two bases \(B_1,B_2\) in the current convex combination, with coefficients \(\alpha,\beta>0\). Symmetric basis exchange supplies \(e\in B_1\setminus B_2\) and \(f\in B_2\setminus B_1\) such that both exchanged sets are bases. With probability \(\beta/(\alpha+\beta)\), replace \(B_1\) by \(B_1-e+f\); otherwise replace \(B_2\) by \(B_2-f+e\).

The fractional vector changes only in coordinates \(e,f\), with conditional expected change zero. For fixed \(F\), the product
\[
\prod_{g\in F}x_g
\]
is concave along this two-coordinate direction: it is constant or linear unless both exchanged coordinates occur, in which case it is a nonnegative multiple of a concave quadratic. Its conditional expectation therefore cannot increase.

Each exchange reduces the symmetric difference of the selected bases. Once they coincide, merge their coefficients. Iteration terminates at one base; the product then becomes \(\mathbf1_{\{F\subseteq B\}}\). This proves (8).

By the matroid-union theorem, edge sets partitionable into \(m\) forests form a matroid. Its rank here is \(m(n-1)\), and every base is a union of \(m\) edge-disjoint spanning trees.

Average the unions of all \(m\)-element subsets of the fixed packing \(T_1,\ldots,T_k\). The resulting vector is
\[
x_e=
\begin{cases}
m/k,&e\in\bigcup_i E(T_i),\\
0,&\text{otherwise}.
\end{cases}
\]
Apply (8), and write \(p=m/k<1/4\).

For a fixed cut of size \(c\), let \(Z=|B\cap\delta_G(X)|\). Expanding the moment-generating function and using (8), for \(s>0\),
\[
\mathbb E e^{sZ}
\le (1-p+pe^s)^c.
\]
Choose \(e^s=(1-p)/p\). Markov’s inequality gives
\[
\begin{aligned}
\Pr\left(Z>\frac{c-b}{2}\right)
&\le
e^{sb/2}\bigl(2\sqrt{p(1-p)}\bigr)^c\\
&\le Mq^c,
\end{aligned} \tag{9}
\]
where
\[
M=\left(\frac{k}{m}\right)^{b/2},
\qquad
q=\sqrt{\frac{4m}{k}}<1.
\]

Combining (7) and (9), the probability that some cut violates
\[
|B\cap\delta_G(X)|\le\frac{|\delta_G(X)|-b}{2} \tag{10}
\]
is at most
\[
M\bigl((1+q^k)^{n-1}-1\bigr).
\]
Put \(u=(n-1)q^k\). Condition (6) says precisely that
\[
Mu\le\frac13.
\]
Since \(M\ge1\), also \(u\le1/3\). Thus the failure probability is at most
\[
M(e^u-1)\le Mue^u\le \frac{e^{1/3}}3<1.
\]
Consequently, a union \(B\) of \(m=b+2\) edge-disjoint spanning trees satisfying (10) exists.

### 2.4. Completing one tree to an Eulerian part

Partition \(B\) into:

- one spanning tree \(T_E\);
- a union \(T_H\) of the other \(b+1\) spanning trees.

Interpret these edges as their original arcs.

We seek a \(0\)-\(1\) circulation on \(D\) that includes every arc of \(T_E\) and excludes every arc of \(T_H\). The lower-bound reduction to integral max-flow says that this exists if and only if
\[
d_{T_E}^-(X)+d_{T_H}^+(X)\le d_D^+(X)
\qquad(X\subseteq V(D)). \tag{11}
\]
Indeed, these are the circulation cut conditions with lower bound \(1\) on \(T_E\), upper bound \(0\) on \(T_H\), and bounds \(0,1\) elsewhere. Integral capacities give an integral circulation.

For a nontrivial cut, writing \(c=|\delta_G(X)|\), equations (5) and (10) give
\[
\begin{aligned}
d_{T_E}^-(X)+d_{T_H}^+(X)
&\le |B\cap\delta_G(X)|\\
&\le \frac{c-b}{2}\\
&\le d_D^+(X).
\end{aligned}
\]
The empty and full vertex sets satisfy (11) trivially. Hence the circulation exists.

Let \(E\) be its selected arc set, and let \(H=A(D)\setminus E\).

The subdigraph \(E\) is balanced and its underlying graph contains \(T_E\). A balanced weakly connected digraph is strong: every cut has equal incoming and outgoing sizes, and weak connectivity prevents both from being zero. Thus \(E\) is a strong Eulerian spanning subdigraph.

The complementary subdigraph \(H\) contains \(b+1\) edge-disjoint underlying spanning trees, so
\[
d_H^+(X)+d_H^-(X)\ge b+1
\]
for every nontrivial \(X\). Since \(E\) is balanced,
\[
d_H^+(X)-d_H^-(X)
=d_D^+(X)-d_D^-(X)\ge-b.
\]
Therefore
\[
d_H^+(X)\ge\frac{(b+1)-b}{2}=\frac12.
\]
This is an integer, so it is at least \(1\). Thus \(H\) is also strong, proving Theorem 2.

Finally, for fixed \(b\), if
\[
k=\left\lceil(2+\varepsilon)\frac{\ln n}{\ln\ln n}\right\rceil,
\]
then
\[
k\ln(k/(4m))=(2+\varepsilon+o(1))\ln n,
\qquad
b\ln(k/m)=o(\ln n).
\]
Hence (6) holds for sufficiently large \(n\). The same reasoning is uniform over \(0\le b\le b_0\). \(\square\)

### A stronger-connectivity variant

The same argument produces two \(r\)-arc-connected spanning parts, one Eulerian, if one replaces
\[
m=b+2
\quad\text{by}\quad
m=b+4r-2
\]
in (6). Reserve \(2r-1\) trees for the Eulerian part and \(b+2r-1\) for its complement. Their outgoing cut sizes are then at least \(r\), by the same integer cut calculations.

---

## 3. Rechecking the lower obstruction: \(k=2\) is insufficient

The four-vertex example in the previous attempt is valid.

Take vertices \(\mathbb Z/4\mathbb Z\), with arcs
\[
i\longrightarrow i-1,
\qquad
i\longrightarrow i+2.
\]
Every vertex has indegree and outdegree two. Singleton cuts and their complements have outgoing size two. A two-vertex set has outgoing size
\[
4-|A(D[X])|\ge2.
\]
Thus the digraph is \(2\)-arc-connected.

Two arc-disjoint strong spanning subdigraphs would each need at least four arcs. There are only eight arcs, so both would have to be directed Hamilton cycles.

Suppose a Hamilton cycle uses \(a\) arcs of increment \(2\) and \(4-a\) arcs of increment \(-1\). Closure modulo four requires
\[
2a-(4-a)\equiv0\pmod4,
\]
so \(a=0\) or \(a=4\). The latter produces only opposite-pair \(2\)-cycles. Hence the only Hamilton cycle uses all increment-\(-1\) arcs, and its complement is not strong.

Therefore any universal constant must satisfy
\[
k\ge3.
\]

---

## 4. Why the remaining gap is genuine

### 4.1. Arc-connectivity does not imply the expansion hypothesis

This remains true even for simple Eulerian digraphs with maximum underlying degree \(O(k)\).

Take a long cycle of disjoint copies of \(K_{k+1}\), join consecutive copies by perfect matchings, and replace every undirected edge by both directed arcs. Any cut splitting a clique has at least \(k\) outgoing arcs. A cut that is a union of whole cliques has at least \(2(k+1)\) outgoing arcs. Thus the digraph is \(k\)-arc-connected.

However, a set consisting of many consecutive whole cliques has just \(2(k+1)\) outgoing arcs, independently of its number of vertices. Its directed expansion tends to zero as the cycle length grows.

Thus Theorem 1 cannot be invoked from a fixed arc-connectivity assumption alone.

### 4.2. High arc-connectivity does not even guarantee an Eulerian spanning subdigraph

Here is an explicit simple construction, showing why an unrestricted reduction to the Eulerian case cannot work.

Fix \(k\ge1\) and \(q>k\). Take disjoint sets \(S,T,P\), with
\[
|S|=|T|=k,\qquad |P|=q.
\]
Include:

- both directions of every edge within \(S\) and within \(T\);
- all arcs from \(S\) to \(P\);
- all arcs from \(P\) to \(T\);
- a directed perfect matching from \(T\) to \(S\).

This digraph has arc-connectivity \(k\). To verify the lower bound:

- A cut splitting \(S\) has at least \(k-1\) outgoing arcs within \(S\), and at least one further outgoing arc through \(P\), through \(T\), or through the matching.
- The same argument applies to a cut splitting \(T\).
- If neither \(S\) nor \(T\) is split, the four possibilities for their inclusion give at least \(k\) outgoing arcs directly from the listed arc types.

A singleton in \(P\) has exactly \(k\) outgoing arcs, proving equality.

But a strong Eulerian spanning subdigraph would need at least one arc entering each vertex of \(P\), hence at least \(q\) arcs from \(S\) to \(P\). Balance across the cut \(S\) would require at least \(q\) arcs entering \(S\), whereas only the \(k\) matching arcs enter \(S\). This is impossible.

**This is not a counterexample to the original conjecture:** the two desired strong spanning subdigraphs need not be Eulerian. It only rules out a universal strategy that first seeks an Eulerian spanning subdigraph.

### 4.3. The quantitative bound still grows with \(n\)

Even when \(b=0\), Theorem 2 requires connectivity of order
\[
\frac{\ln n}{\ln\ln n},
\]
not an absolute constant.

Accordingly, the arguments above provide neither:

- a fixed \(k\) sufficient for every digraph, nor
- counterexamples with unbounded arc-connectivity.

They establish the stated special cases only. I make no claim that these bounds are new or are the current best bounds in their respective classes.