```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A cut-count refinement extends the verified 68-vertex result to additional conditional cases and imposes explicit restrictions on any 70-vertex counterexample.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; the extensions beyond 68 vertices are conditional, and novelty is not claimed."
}
```

# Partial result: discounting harmless edges and counting small-cut obstructions

I do not obtain a proof or a counterexample to the unrestricted conjecture. The 68-vertex fractional-matching argument in the supplied lead checks out; I reprove it below. The additional result is a refinement that:

- discounts matching edges that cannot belong to a forbidden cut;
- bounds the probability that a particular odd cut is contained in the intersection;
- gives concrete necessary conditions for a counterexample on 70 vertices.

The only external theorem used is the standard perfect-matching polytope theorem. No computational checks are claimed.

Throughout, graphs are finite and loopless; parallel edges are allowed. It suffices to consider connected graphs, since successful pairs combine componentwise.

## 1. Main quantitative result

Call a perfect matching \(P\) **3-cut-respecting** if it meets every 3-edge-cut exactly once. Every bridgeless cubic graph has such a matching, as proved below.

For a 3-cut-respecting matching \(P\), put \(F=G-P\), and define
\[
b(P)=\bigl|\{uv\in P:\ u,v\text{ belong to different cycles of }F\}\bigr|.
\]
Also let
\[
a(P)=\bigl|\{D:\ D\text{ is a distinct 7-edge-cut of }G,\ D\subseteq P\}\bigr|.
\]
Cuts are counted as edge sets, so \(\delta(X)\) and \(\delta(V\setminus X)\) are counted only once.

**Theorem A.** Let \(G\) be a bridgeless cubic graph and \(P\) a 3-cut-respecting perfect matching. There is a perfect matching \(Q\) such that \(P\cap Q\) contains no odd edge-cut if either
\[
\boxed{b(P)<35}
\tag{1}
\]
or
\[
\boxed{3b(P)+2a(P)<135.}
\tag{2}
\]

These conditions have the following consequences.

1. Every bridgeless cubic graph on at most **68 vertices** satisfies the conjecture.
2. If \(G\) has 70 vertices, it satisfies the conjecture whenever some 3-cut-respecting \(P\):
   - has an edge joining two vertices of the same cycle of \(G-P\); or
   - contains at most fourteen distinct 7-edge-cuts.
3. Every bridgeless cubic graph on at most **88 vertices** having a 3-cut-respecting \(P\) with \(a(P)\le1\) satisfies the conjecture.
4. If \(P\) has \(\ell\) edges whose endpoints lie on the same complementary cycle, condition (1) becomes
   \[
   |V(G)|-2\ell<70.
   \]
   Thus this criterion is not merely an order bound.

The parameters have a direct interpretation. Contract every cycle of \(F\), retaining the edges of \(P\), to obtain a multigraph \(K\). Then \(b(P)\) is the number of nonloop edges of \(K\), and \(a(P)\) is the number of its 7-edge-cuts.

The assertions for 70 and 88 vertices are **conditional**, not universal order bounds.

---

## 2. Exact verification of a proposed pair

For \(X\subseteq V(G)\), cubicity gives
\[
3|X|=2|E(G[X])|+|\delta(X)|,
\]
and hence
\[
|\delta(X)|\equiv |X|\pmod 2.
\tag{3}
\]

**Lemma 1.** For any \(I\subseteq E(G)\), the following are equivalent:

1. \(I\) contains no odd edge-cut;
2. every component of \(G-I\) has even order.

**Proof.**
If a component \(H\) of \(G-I\) has odd order, then
\[
\delta(V(H))\subseteq I,
\]
and this cut is odd by (3).

Conversely, suppose that \(\delta(X)\subseteq I\) is odd. Then \(X\) is a union of components of \(G-I\). Equation (3) says that \(|X|\) is odd, so one of those components has odd order. \(\square\)

Consequently, a proposed pair of perfect matchings can be checked in linear time: delete their intersection and inspect the component orders.

---

## 3. The fractional matching used in the argument

I use the perfect-matching polytope theorem in the following form: the convex hull of perfect-matching incidence vectors is
\[
\left\{
x\in\mathbb R_{\ge0}^{E(G)}:
x(\delta(v))=1\quad(v\in V(G)),\qquad
x(\delta(X))\ge1\quad(|X|\text{ odd})
\right\}.
\tag{4}
\]

### Existence of a 3-cut-respecting matching

The constant vector \(x_e=1/3\) satisfies (4): every odd cut of a bridgeless cubic graph has at least three edges.

Write this vector as a convex combination of perfect matchings. Every 3-edge-cut has total weight exactly one. Since every perfect matching meets an odd cut at least once, every matching appearing with positive coefficient meets every 3-edge-cut exactly once.

Thus a 3-cut-respecting perfect matching exists.

### A parameterized distribution

**Lemma 2.** Let \(P\) be a perfect matching, and let \(q\ge3\) be odd. Suppose that no odd edge-cut of size less than \(q\) is contained in \(P\). Then
\[
x_e=
\begin{cases}
1/q,& e\in P,\\[1mm]
(q-1)/(2q),&e\notin P
\end{cases}
\tag{5}
\]
is a fractional perfect matching.

Moreover, in any convex decomposition of \(x\) into perfect matchings, every matching occurring with positive coefficient:

- meets every \(q\)-edge-cut contained in \(P\) exactly once;
- meets every 3-edge-cut exactly once.

**Proof.**
The vertex equations are immediate.

Let \(D\) be an odd cut, and put
\[
d=|D|,\qquad k=|D\setminus P|.
\]
Both \(|D|\) and \(|D\cap P|\) are odd, so \(k\) is even. We have
\[
x(D)=\frac d q+\frac{q-3}{2q}k.
\]

If \(k=0\), the hypothesis gives \(d\ge q\), and therefore \(x(D)\ge1\). If \(k\ge2\), then \(d\ge3\), whence
\[
x(D)\ge\frac{d+q-3}{q}\ge1.
\]
This proves (4).

A \(q\)-edge-cut contained in \(P\) has weight one, so every matching in the decomposition meets it exactly once.

Every 3-edge-cut also has weight one. For \(q=3\), this follows because \(x\) is constant. For \(q>3\), \(P\) cannot contain the whole cut and consequently meets it once; substituting \(d=3\), \(k=2\) gives \(x(D)=1\). \(\square\)

We henceforth regard a matching \(Q\) from such a convex decomposition as random. In particular,
\[
\Pr(e\in Q)=\frac1q\qquad(e\in P).
\tag{6}
\]
No independence is asserted or needed.

If \(P\) is 3-cut-respecting, Lemma 2 applies with \(q=5\). Every resulting \(P\cap Q\) contains neither a 3-edge-cut nor a 5-edge-cut.

---

## 4. Discounting edges that cannot lie in a forbidden cut

Fix \(P,q\) as in Lemma 2, and put \(F=G-P\). Let
\[
P^\times=\{uv\in P:\ u,v\text{ lie on different cycles of }F\},
\qquad b=|P^\times|.
\]

The useful observation is
\[
D\subseteq P,\ D\text{ an edge-cut}
\quad\Longrightarrow\quad
D\subseteq P^\times.
\tag{7}
\]
Indeed, if \(D=\delta(X)\subseteq P\), then no edge of \(F\) crosses \(X\). Thus \(X\) is a union of entire cycles of \(F\), and an edge joining two vertices on the same such cycle cannot belong to \(D\).

Define
\[
W(Q)=|P^\times\cap Q|.
\]
Equation (6) gives
\[
\mathbb E W(Q)=\frac bq.
\tag{8}
\]

Call \(Q\) unsuccessful if \(P\cap Q\) contains an odd cut. By Lemma 2, such a cut has size at least \(q+2\); by (7), all its edges are counted by \(W(Q)\). Hence
\[
Q\text{ unsuccessful}\quad\Longrightarrow\quad W(Q)\ge q+2.
\tag{9}
\]

Therefore:

**Corollary 3.** Under the hypotheses of Lemma 2, a suitable partner \(Q\) exists whenever
\[
\boxed{b<q(q+2).}
\tag{10}
\]

For \(q=5\), this proves condition (1) of Theorem A. Since \(b\le |P|=|V(G)|/2\), it also verifies the universal 68-vertex bound.

---

## 5. Charging small-cut obstructions

The preceding argument treats all failures as having cost at least \(q+2\). It can be sharpened when there are few cuts of that size.

### Probability of containing a specified cut

Let \(D\subseteq P\) be an odd cut of size \(d\ge q\). Every perfect matching meets \(D\) at least once, so
\[
\mathbb E|Q\cap D|
\ge
1+(d-1)\Pr(D\subseteq Q).
\]
On the other hand, (6) gives
\[
\mathbb E|Q\cap D|=\frac dq.
\]
Consequently,
\[
\boxed{
\Pr(D\subseteq Q)\le \frac{d-q}{q(d-1)}.
}
\tag{11}
\]

For \(d=q\), this is zero, recovering the tight-cut conclusion. For \(q=5\), \(d=7\), it gives
\[
\Pr(D\subseteq Q)\le\frac1{15}.
\tag{12}
\]

### General cut-count criterion

For odd \(d\ge q+2\), let \(N_d\) be the number of distinct \(d\)-edge-cuts contained in \(P\).

**Theorem 4.** Under the hypotheses of Lemma 2, let \(r\ge q+2\) be odd. A suitable partner \(Q\) exists if
\[
\boxed{
\frac bq+
\sum_{\substack{q+2\le d<r\\d\text{ odd}}}
N_d\,\frac{(r-d)(d-q)}{q(d-1)}
<r.
}
\tag{13}
\]

**Proof.**
For each \(Q\), define
\[
Z(Q)=W(Q)+
\sum_{\substack{D\subseteq P\text{ an odd cut}\\q+2\le |D|<r}}
(r-|D|)\,\mathbf1_{\{D\subseteq Q\}}.
\]

If \(Q\) is unsuccessful, choose an odd cut \(D\subseteq P\cap Q\). Its size is at least \(q+2\).

- If \(|D|\ge r\), then \(W(Q)\ge r\).
- If \(|D|<r\), then \(W(Q)\ge |D|\), and the summand belonging to \(D\) supplies the remaining \(r-|D|\).

Thus
\[
Z(Q)\ge r\,\mathbf1_{\{Q\text{ unsuccessful}\}}.
\]
Taking expectations and applying (8) and (11),
\[
r\Pr(Q\text{ unsuccessful})
\le \mathbb E Z(Q)
\le
\frac bq+
\sum_{\substack{q+2\le d<r\\d\text{ odd}}}
N_d\,\frac{(r-d)(d-q)}{q(d-1)}.
\]
If the last expression is less than \(r\), not every matching in the decomposition is unsuccessful. \(\square\)

### Specialization to 7-edge-cuts

Take \(q=5\), \(r=9\). Only \(d=7\) occurs in (13), giving
\[
\frac b5+\frac{2N_7}{15}<9.
\]
Equivalently,
\[
3b+2N_7<135,
\]
which is condition (2) of Theorem A.

For example, if \(|V(G)|\le88\) and \(N_7\le1\), then
\[
3b+2N_7\le3\cdot44+2=134<135.
\]

This completes the proof of Theorem A and its stated consequences.

---

## 6. Restrictions on a hypothetical 70-vertex counterexample

At the first order not covered universally, equality in the fractional argument is restrictive.

**Proposition 5.** Suppose a 70-vertex bridgeless cubic graph \(G\) is a counterexample to the conjecture. Then, for every 3-cut-respecting perfect matching \(P\):

1. every edge of \(P\) joins different cycles of \(G-P\);
2. \(P\) contains at least fifteen distinct 7-edge-cuts.

If there are exactly fifteen such cuts, then every edge of \(P\) belongs to exactly three of them, and any two distinct cuts intersect in exactly one edge.

**Proof.**
Use the distribution in Lemma 2 with \(q=5\). Since \(G\) is assumed to be a counterexample, every \(Q\) in the support is unsuccessful.

By (9), \(W(Q)\ge7\). Hence
\[
7\le\mathbb EW(Q)=\frac{b(P)}5\le\frac{|P|}5=7.
\]
All inequalities are equalities. Thus \(b(P)=35=|P|\), proving the first assertion, and every supported \(Q\) satisfies
\[
|P\cap Q|=7.
\]
Its intersection contains an odd cut of size at least seven, so \(P\cap Q\) itself is a 7-edge-cut.

For each such cut \(D\), let
\[
p_D=\Pr(P\cap Q=D).
\]
These probabilities sum to one, and (12) gives \(p_D\le1/15\). At least fifteen distinct cuts are therefore necessary.

Suppose there are exactly fifteen, denoted \(D_1,\ldots,D_{15}\). Then each has probability \(1/15\). For every \(e\in P\),
\[
\frac15=\Pr(e\in Q)
=\frac1{15}\bigl|\{i:e\in D_i\}\bigr|,
\]
so \(e\) belongs to exactly three cuts.

For fixed \(i\), every matching whose intersection with \(P\) is \(D_j\) meets \(D_i\) in exactly \(D_i\cap D_j\). As \(D_i\) is odd,
\[
|D_i\cap D_j|\ge1.
\]
Moreover,
\[
\frac75
=\mathbb E|Q\cap D_i|
=\frac1{15}\left(7+\sum_{j\ne i}|D_i\cap D_j|\right).
\]
The fourteen terms in the sum are positive integers and sum to fourteen. Each is therefore one. \(\square\)

The equality case has a concise incidence description: label the fifteen cuts by fifteen points, and replace each of the 35 edges of \(P\) by the triple of cuts containing it. Every pair of points occurs in exactly one triple—a Steiner triple system on fifteen points.

This is only a **necessary condition**. It does not establish that such a graph exists, nor rule out counterexamples with more than fifteen relevant cuts.

---

## 7. The stronger 68-vertex conclusion also checks out

For completeness, the supplied lead's stronger assertion is valid:

**Proposition 6.** Every bridgeless cubic graph on at most 68 vertices has three perfect matchings with empty common intersection.

**Proof.**
Choose a 3-cut-respecting \(P\). From the \(q=5\) distribution choose \(Q\) with
\[
|P\cap Q|\le\left\lfloor\frac{|V(G)|}{10}\right\rfloor\le6.
\]
Both matchings meet every 3-edge-cut once, and their intersection contains no 5-edge-cut.

Define
\[
y_e=\frac{3-\mathbf1_P(e)-\mathbf1_Q(e)}7.
\]
The incident weights at each vertex sum to one. For an odd cut \(D\):

- if \(|D|=3\), then \(y(D)=(9-2)/7=1\);
- if \(|D|=5\), the two matchings cannot both contain \(D\), so
  \[
  |P\cap D|+|Q\cap D|\le8,
  \qquad y(D)\ge(15-8)/7=1;
  \]
- if \(|D|\ge7\), every edge has weight at least \(1/7\), so \(y(D)\ge1\).

Thus \(y\) is a fractional perfect matching. If \(R\) is drawn from a convex decomposition of \(y\), then
\[
\mathbb E|P\cap Q\cap R|
=\frac{|P\cap Q|}{7}
\le\frac67<1.
\]
Some \(R\) has \(P\cap Q\cap R=\varnothing\).

Such a triple implies the desired conclusion: an odd cut contained in \(P\cap Q\) would have to meet \(R\), contradicting the empty common intersection. \(\square\)

---

## 8. What remains unresolved

The refinements distinguish the following two issues:

- **Harmless common edges:** edges of \(P\) lying within one complementary cycle cannot participate in a cut contained in \(P\), and need not be charged against the obstruction-size bound.
- **Small-cut failures:** a specified 7-edge-cut is contained in the sampled second matching with probability at most \(1/15\), allowing additional cases when few such cuts exist.

However, I have not proved that every bridgeless cubic graph admits a 3-cut-respecting \(P\) for which these criteria hold. In particular, I have not excluded a 70-vertex graph for which every such \(P\) has no intracycle matching edges and contains at least fifteen relevant 7-edge-cuts.

Thus the unrestricted conjecture remains unresolved by this attack. The established additions are Theorem A, its general cut-count version (13), and the boundary restrictions in Proposition 5.