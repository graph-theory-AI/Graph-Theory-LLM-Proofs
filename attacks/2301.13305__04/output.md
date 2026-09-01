```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The problem remains open in general, but even stars are solved exactly, even matchings are determined within an additive constant, and general lower and upper bounds are proved.",
  "would_publish": false,
  "caveats": "No general asymptotic is obtained, and overlap with the cited 2023 follow-up has not been checked."
}
```

# Mathematical writeup

## 1. Definition and elementary reductions

Let \(g(n,H)=g(K_n,H)\) be the minimum number of colors in an arbitrary edge-coloring of \(K_n\) such that, for every copy \(H'\) of \(H\), some color occurs on an odd number of edges of \(H'\).

Copies are understood as non-induced. Isolated vertices of \(H\) may therefore be deleted once \(n\ge v(H)\), since every copy of the non-isolated part can be extended to a copy of \(H\).

Write
\[
h=v(H),\qquad q=e(H).
\]

If \(q\) is odd, then every coloring automatically has the required property, since a sum of color multiplicities equal to \(q\) cannot consist entirely of even integers. Thus
\[
g(n,H)=1\qquad(q\text{ odd}).
\]
The interesting case is \(q>0\) even.

---

## 2. General bounds for every fixed even-edge graph

Let \(\operatorname{ex}(n,H)\) denote the usual extremal number.

### Proposition 2.1

For every fixed \(H\) with \(q>0\) even,
\[
g(n,H)\ge
\left\lceil\frac{\binom n2}{\operatorname{ex}(n,H)}\right\rceil.
\]

Moreover, for all sufficiently large \(n\),
\[
g(n,H)=\Omega_H\!\left(\frac{\log n}{\log\log n}\right).
\]

#### Proof

A color class cannot contain a copy of \(H\): such a copy would be monochromatic, and its unique nonzero color multiplicity would be \(q\), which is even. Hence every color class is \(H\)-free and has at most \(\operatorname{ex}(n,H)\) edges. Summing over the color classes proves the first assertion.

For the second assertion, a valid coloring cannot contain a monochromatic \(K_h\), since such a clique contains a monochromatic copy of \(H\).

A crude multicolor Ramsey estimate suffices. Suppose \(K_N\) is colored with \(r\ge2\) colors, and set
\[
L=r(h-1)+1.
\]
If \(N\ge 2r^L\), repeatedly choose a vertex and retain a largest monochromatic neighborhood. This produces vertices
\[
v_1,\ldots,v_{L+1}
\]
and colors \(c_1,\ldots,c_L\) such that every edge \(v_iv_j\), \(i<j\), has color \(c_i\). Some color appears at least \(h\) times among the \(c_i\), and the corresponding vertices form a monochromatic \(K_h\). Consequently, a valid \(r\)-coloring satisfies
\[
n<2r^{\,r(h-1)+1}.
\]
Inverting this inequality gives
\[
r=\Omega_H\!\left(\frac{\log n}{\log\log n}\right).
\]
\(\square\)

The logarithmic bound matters mainly when the extremal-number bound is only constant, for example for non-bipartite \(H\).

### Proposition 2.2: a local-lemma upper bound

Let \(B_q\) be the \(q\)-th Bell number. Then
\[
g(n,H)\le
\min\left\{
\binom n2,\,
\left\lceil
\bigl(eB_q(2q^2n^{h-2}+1)\bigr)^{2/q}
\right\rceil
\right\}.
\]
In particular,
\[
g(n,H)=O_H\!\left(
n^{\min\{2,\,2(h-2)/q\}}
\right).
\]

#### Proof

Independently color every edge uniformly from \(r\) colors. For a fixed copy \(F\) of \(H\), let \(A_F\) be the event that every color has even multiplicity on \(E(F)\).

A bad coloring of the \(q\) labeled edges partitions them into nonempty even-sized color classes. Such a partition has at most \(q/2\) blocks. There are at most \(B_q\) set partitions, and at most \(r^{q/2}\) ways to assign colors to their blocks. Hence
\[
\Pr(A_F)\le B_q r^{-q/2}.
\]

Events corresponding to copies with disjoint edge sets are independent. A fixed host edge lies in at most
\[
2q\,n^{h-2}
\]
labeled copies of \(H\): choose which edge of \(H\) maps to it, choose its orientation, and then map the remaining vertices. Therefore \(A_F\) is dependent on at most
\[
2q^2n^{h-2}
\]
other events.

The symmetric Lovász local lemma applies whenever
\[
eB_qr^{-q/2}(2q^2n^{h-2}+1)\le1,
\]
which gives the displayed bound. Coloring every edge uniquely supplies the \(\binom n2\) alternative. \(\square\)

For example, this gives \(O(n)\) for \(C_4\), \(O(n^{2/3})\) for \(K_4\), and \(O(n^{3/5})\) for \(K_5\). The prompt reports a much stronger \(n^{o(1)}\) bound for \(K_5\).

---

## 3. Exact solution for every even star

Let \(S_{2k}=K_{1,2k}\), the star with \(2k\) edges.

### Theorem 3.1

For \(n\ge 2k+1\),
\[
\boxed{
g(n,S_{2k})=
\begin{cases}
n-2k+1,&n\ \text{even},\\[2mm]
n-2k+2,&n\ \text{odd}.
\end{cases}}
\]

#### Proof: local characterization

Fix a vertex \(v\), and let \(d_i(v)\) be the number of edges of color \(i\) incident with \(v\). A parity-bad \(S_{2k}\) centered at \(v\) exists if and only if
\[
\sum_i \left\lfloor\frac{d_i(v)}2\right\rfloor\ge k. \tag{3.1}
\]
Indeed, a bad star consists of \(k\) pairs of equally colored incident edges. Conversely, if the sum in (3.1) is at least \(k\), choose \(k\) such pairs.

Thus every valid coloring satisfies
\[
\sum_i \left\lfloor\frac{d_i(v)}2\right\rfloor\le k-1
\qquad\text{for every }v. \tag{3.2}
\]

Let \(t_v\) be the number of colors present at \(v\). For every positive integer \(d\),
\[
d-1\le 2\left\lfloor \frac d2\right\rfloor.
\]
Therefore
\[
(n-1)-t_v
 =\sum_{i:d_i(v)>0}(d_i(v)-1)
 \le 2\sum_i\left\lfloor\frac{d_i(v)}2\right\rfloor
 \le 2k-2.
\]
Hence
\[
t_v\ge n-2k+1,
\]
so every valid coloring uses at least \(n-2k+1\) colors.

Suppose now that \(n\) is odd and equality held. Then every vertex would see every one of the \(r=n-2k+1\) colors, and equality would hold throughout the preceding inequalities. Equality in
\[
d-1\le2\lfloor d/2\rfloor
\]
occurs only when \(d\) is odd. Thus, in every color class, every vertex would have positive odd degree. This is impossible on an odd number of vertices by the handshaking lemma. Hence for odd \(n\),
\[
r\ge n-2k+2.
\]

#### Proof: constructions

If \(n\) is even, take a 1-factorization
\[
E(K_n)=F_1\sqcup\cdots\sqcup F_{n-1}.
\]
Merge \(F_1,\ldots,F_{2k-1}\) into one color and retain all other factors as separate colors. This uses
\[
1+(n-1-(2k-1))=n-2k+1
\]
colors. At every vertex, the merged color has degree \(2k-1\), and every other color has degree one. Thus the left side of (3.2) equals \(k-1\).

If \(n\) is odd, take a 1-factorization of \(K_{n+1}\) and delete one vertex. This gives a proper \(n\)-edge-coloring of \(K_n\) in which every vertex misses exactly one color. Merge any \(2k-1\) color classes. At each vertex the merged color has degree either \(2k-1\) or \(2k-2\), while all other colors have degree at most one. Again (3.2) holds, and the number of colors is
\[
1+n-(2k-1)=n-2k+2.
\]
This proves the theorem. \(\square\)

For \(k=1\), this recovers the edge-chromatic number of \(K_n\):
\[
g(n,P_3)=
\begin{cases}
n-1,&n\text{ even},\\
n,&n\text{ odd}.
\end{cases}
\]

A family of even stars is governed by its smallest member: if \(k_0=\min k\), then avoiding a bad \(S_{2k_0}\) forces the left side of (3.1) to be at most \(k_0-1\), and hence also excludes every larger bad even star.

---

## 4. Even matchings: an additive-constant determination

Let \(M_t\) denote a matching with \(t\) edges. Thus \(M_{2k}\) has \(4k\) vertices.

We first need an elementary fact.

### Lemma 4.1

The minimum number of colors needed to color \(E(K_m)\) so that each color class is pairwise intersecting is
\[
m-2\qquad(m\ge4).
\]

#### Proof

For the upper bound, color all edges whose smaller endpoint is \(i\) by \(i\), for \(i=1,\ldots,m-3\), and color the triangle on the final three vertices with one last color. This uses \(m-2\) intersecting classes.

For the lower bound, an intersecting family of edges either has a common endpoint or is contained in a triangle. Let there be \(s\) star-type classes and \(t\) triangle-type classes. Choose one center for every star-type class, and let \(S\) be the set of chosen centers. All edges induced by \(V(K_m)\setminus S\) must lie in triangle-type classes. Hence
\[
3t\ge \binom{m-s}{2}.
\]
Writing \(x=m-s\),
\[
s+t\ge m-x+\frac{x(x-1)}6
      =m-2+\frac{(x-3)(x-4)}6
      \ge m-2.
\]
\(\square\)

This is the \(2\)-subset case of the Kneser-graph chromatic-number theorem, but the proof above is self-contained.

### Theorem 4.2

For every \(n\ge4k\),
\[
\boxed{
n-4k+2\le g(n,M_{2k})\le n-2k.
}
\]
Consequently, for every fixed \(k\),
\[
g(n,M_{2k})=n+O_k(1).
\]
For \(k=1\),
\[
\boxed{g(n,2K_2)=n-2.}
\]

#### Proof: lower bound

Call two disjoint edges of the same color a monochromatic \(2\)-matching. If there were \(k\) vertex-disjoint monochromatic \(2\)-matchings, their union would be a matching with \(2k\) edges, and every color would occur an even number of times. Thus a valid coloring contains at most \(k-1\) vertex-disjoint monochromatic \(2\)-matchings.

Choose a maximal collection of such configurations, and let \(S\) be the union of their endpoints. Then
\[
|S|\le4(k-1).
\]
On \(U=V(K_n)\setminus S\), no color class contains two disjoint edges. Thus every color class restricted to \(K_U\) is intersecting. Lemma 4.1 yields
\[
r\ge |U|-2\ge n-4(k-1)-2=n-4k+2.
\]

#### Proof: upper bound

Start with the \(n-2\)-coloring from Lemma 4.1, whose color classes are all intersecting. Merge any \(2k-1\) of these classes into one color. The resulting coloring has
\[
(n-2)-(2k-1)+1=n-2k
\]
colors.

Every matching uses at most one edge from each unmerged class and at most \(2k-1\) edges from the merged class. If a matching of size \(2k\) had every color occurring evenly, every unmerged color would occur zero times, forcing all \(2k\) edges into the merged class, a contradiction. \(\square\)

For \(k\ge2\), the remaining additive gap is only \(2k-2\).

---

## 5. Complete classification when the forbidden graphs have two edges

Up to isolated vertices, there are only two graphs with two edges: \(P_3\) and \(2K_2\). For sufficiently large \(n\):

\[
g(n,P_3)=
\begin{cases}
n-1,&n\text{ even},\\
n,&n\text{ odd},
\end{cases}
\qquad
g(n,2K_2)=n-2.
\]

For a prescribed family containing both types, every two distinct edges of \(K_n\) must receive different colors: two same-colored edges are either adjacent or disjoint and would form a bad copy of one of the two graphs. Therefore
\[
g(n,\{P_3,2K_2\})=\binom n2.
\]

Thus the problem is completely solved for families whose nontrivial even-edge members have exactly two edges.

---

## 6. Two useful linear-size algebraic constructions

### Proposition 6.1: an odd-edge component

If \(H\) has a connected component with an odd number of edges, then
\[
g(n,H)\le n-1.
\]

#### Proof

Order the vertices of \(K_n\), orient every edge toward the larger endpoint, and color an edge by its smaller endpoint. Consider an odd-edge component \(C\) of a copy of \(H\). The number of \(C\)-edges colored by a vertex \(v\) is its outdegree in this orientation. The sum of these outdegrees over \(V(C)\) is \(e(C)\), which is odd. Hence some color occurs oddly. \(\square\)

More generally, this order coloring works whenever \(H\) has no vertex ordering
\[
v_1,\ldots,v_h
\]
in which every \(v_i\) has an even number of neighbors among \(v_{i+1},\ldots,v_h\). In particular, it works if every non-isolated vertex of \(H\) has odd degree.

### Proposition 6.2: exactly two odd-degree vertices

If \(H\) has exactly two odd-degree vertices, then
\[
g(n,H)\le 2^{\lceil\log_2n\rceil}-1<2n.
\]

#### Proof

Inject \(V(K_n)\) into the vector space \(\mathbb F_2^d\), where \(d=\lceil\log_2n\rceil\), writing the label of \(v\) as \(x_v\). Color
\[
uv\quad\text{by}\quad x_u+x_v.
\]
The color is nonzero because the labels are distinct, so at most \(2^d-1\) colors are used.

Suppose every color occurred evenly on a copy of \(H\). The xor of its edge colors would then be zero. On the other hand,
\[
\bigoplus_{uv\in E(H)}(x_u+x_v)
  =\bigoplus_{\deg_H(v)\text{ odd}}x_v.
\]
If \(a,b\) are the two odd-degree vertices, this equals
\[
x_a+x_b\ne0,
\]
a contradiction. \(\square\)

### Forest consequences

If \(F\) is a fixed forest with \(f\) non-isolated vertices, then
\[
\operatorname{ex}(n,F)\le(f-2)n.
\]
Indeed, a graph with more than \((f-2)n\) edges has a nonempty subgraph of minimum degree at least \(f-1\), obtained by deleting vertices of degree at most \(f-2\). Such a graph greedily contains every \(f\)-vertex forest.

Therefore
\[
g(n,F)\ge\frac{n-1}{2(f-2)}.
\]

Combining this with Propositions 6.1 and 6.2 gives:

- If an even-edge forest \(F\) has an odd-edge component, then
  \[
  g(n,F)=\Theta_F(n).
  \]
- If \(F\) has exactly two odd-degree vertices, then
  \[
  g(n,F)=\Theta_F(n).
  \]

In particular, for every fixed even-length path \(P_{2k+1}\),
\[
g(n,P_{2k+1})=\Theta_k(n).
\]

---

## 7. An explicit estimate for \(C_4\) in \(K_n\)

### Proposition 7.1

For \(n\ge4\),
\[
\left\lceil
\frac{2(n-1)}{1+\sqrt{4n-3}}
\right\rceil
\le g(n,C_4)\le
\begin{cases}
n,&n\text{ odd},\\
n+1,&n\text{ even}.
\end{cases}
\]

Thus
\[
\Omega(\sqrt n)\le g(n,C_4)\le n+1.
\]

#### Upper bound

Let \(m\) be the least odd integer at least \(n\), and label the vertices injectively by elements of \(\mathbb Z_m\). Color
\[
xy\quad\text{by}\quad x+y\pmod m.
\]
This coloring is proper.

Suppose a \(4\)-cycle \(x_1x_2x_3x_4x_1\) were bad. Properness implies that its two pairs of equal colors must lie on opposite edges:
\[
x_1+x_2=x_3+x_4,\qquad
x_2+x_3=x_4+x_1.
\]
Subtracting gives
\[
2x_1=2x_3.
\]
Since \(m\) is odd, multiplication by \(2\) is invertible in \(\mathbb Z_m\), so \(x_1=x_3\), contradicting distinctness.

#### Lower bound

Each color class is \(C_4\)-free. If a \(C_4\)-free graph has degrees \(d_1,\ldots,d_n\) and \(e\) edges, then every pair of vertices has at most one common neighbor, so
\[
\sum_v\binom{d_v}{2}\le\binom n2.
\]
By Cauchy–Schwarz,
\[
\sum_v\binom{d_v}{2}
\ge \frac{2e^2}{n}-e.
\]
Solving the resulting quadratic inequality gives
\[
e\le \frac{n(1+\sqrt{4n-3})}{4}.
\]
Dividing \(\binom n2\) by this bound proves the assertion. \(\square\)

As a small exact check, \(g(4,C_4)=3\). Two colors are impossible because the three \(4\)-cycles in \(K_4\) sum to zero over \(\mathbb F_2\), whereas requiring odd intersection with one chosen color would assign right-hand side \(1\) to all three equations. Three colors are attained by giving two adjacent edges distinct singleton colors and all remaining edges a third color.

---

## 8. Prescribed finite families

Let \(g(n,\mathcal H)\) denote the corresponding family parameter.

1. Odd-edge members of \(\mathcal H\) impose no restriction and may be discarded.

2. Trivially,
   \[
   g(n,\mathcal H)\ge\max_{H\in\mathcal H}g(n,H).
   \]

3. If \(c_H\) is a valid coloring for each \(H\), their common refinement
   \[
   c(e)=(c_H(e))_{H\in\mathcal H}
   \]
   is valid for the whole family. Hence
   \[
   g(n,\mathcal H)\le\prod_{H\in\mathcal H}g(n,H).
   \]

4. A direct local-lemma argument gives a better general estimate for fixed finite families. If
   \[
   h_*=\max_{H\in\mathcal H}v(H),\qquad
   q_*=\min_{H\in\mathcal H,\ e(H)\text{ even}}e(H),
   \]
   then
   \[
   g(n,\mathcal H)
   =O_{\mathcal H}\!\left(
   n^{\min\{2,\,2(h_*-2)/q_*\}}
   \right).
   \]

5. A family of even stars is controlled exactly by its smallest star, and a family of even matchings is likewise controlled by its smallest matching: a bad larger matching can be partitioned into monochromatic edge-pairs, any prescribed number of which form a smaller bad even matching.

---

## 9. What remains unresolved

These arguments do not determine \(g(n,H)\) for arbitrary \(H\). Significant gaps remain even for small sparse graphs. For example, if \(T\) is the tree obtained by subdividing every edge of \(K_{1,3}\), then \(v(T)=7\) and \(e(T)=6\). The results above give only
\[
\Omega(n)\le g(n,T)\le O(n^{5/3}).
\]
This tree has no odd-edge component and has four odd-degree vertices, so neither linear algebraic construction above applies.

Likewise, this writeup leaves:

- an additive gap \(2k-2\) for \(M_{2k}\), \(k\ge2\);
- the gap \(\Omega(\sqrt n)\) versus \(O(n)\) for \(C_4\) in \(K_n\);
- very large gaps for many connected even-edge graphs.

The supplied catalog reports stronger specialized results for \(K_5\) and for \(C_4\) in the bipartite host \(K_{n,n}\). I have not checked whether the exact star formula or matching bounds above already appear in that follow-up, so no novelty claim is made.