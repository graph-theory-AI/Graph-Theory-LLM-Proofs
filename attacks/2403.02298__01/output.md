```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A block-compressed Lovasz-local-lemma construction improves the quoted lower bound to (1/(3sqrt(6))-o(1))sqrt(n)/ln(n), but does not close the sqrt(ln n) gap.",
  "would_publish": false,
  "caveats": "All logarithms are natural; only the numerical constant in the known lower-order bound is improved, and the conjecture remains open."
}
```

## 1. Statement of the partial result

Write \(\vec\alpha(D)\) for the maximum order of an acyclic induced subdigraph of an oriented graph \(D\). All logarithms below are natural.

I prove the following.

### Theorem
As \(n\to\infty\),
\[
\vec a(n)\leq \bigl(3\sqrt 6+o(1)\bigr)\sqrt n\,\ln n
\]
and consequently
\[
\boxed{\displaystyle
\vec t(n)\geq
\left(\frac1{3\sqrt6}-o(1)\right)\frac{\sqrt n}{\ln n}.}
\]

Numerically,
\[
3\sqrt6\approx 7.34847,
\qquad
\frac1{3\sqrt6}\approx0.136083.
\]
Thus, under the natural-log normalization, this improves the constants
\[
\frac{107}{8}=13.375,
\qquad
\frac8{107}\approx0.074766
\]
quoted in the prompt. It does not improve the logarithmic exponent and hence does not prove the conjecture.

The construction uses a random oriented graph and simultaneously excludes underlying triangles and coarse topological-order certificates by the asymmetric Lovász local lemma.

---

## 2. A coarse topological-order certificate

We first record the compression that avoids union-bounding over all \(k!\) linear orders.

### Lemma 1
Let \(D\) be an oriented graph, and let \(b,\ell\) be positive integers. Suppose that for every ordered collection
\[
(V_1,\dots,V_\ell)
\]
of pairwise disjoint \(b\)-element vertex sets, there are indices \(i<j\) and an arc directed from \(V_j\) to \(V_i\). Then
\[
\vec\alpha(D)<\ell b.
\]

#### Proof
Suppose instead that \(D[S]\) is acyclic for some \(|S|\geq \ell b\). Choose \(\ell b\) vertices of \(S\) and list them in a topological order. Divide this order into \(\ell\) consecutive blocks
\[
V_1,\dots,V_\ell
\]
of size \(b\).

Every arc between \(V_i\) and \(V_j\), with \(i<j\), must be directed from \(V_i\) to \(V_j\). Thus there is no arc from a later block to an earlier block, contradicting the hypothesis. \(\square\)

The point is that only the ordered blocks, rather than the full order inside each block, need to be recorded.

---

## 3. Random construction

Fix constants \(c,\beta,C>0\) satisfying
\[
c^2<\frac12,\qquad
0<\beta<\frac12-c^2,\qquad
\beta cC>1.
\tag{1}
\]

For sufficiently large \(n\), put
\[
p=\frac{c}{\sqrt n},
\qquad
\ell=\left\lceil\ln\ln n\right\rceil,
\]
and
\[
b=\left\lceil \frac{C\sqrt n\,\ln n}{\ell}\right\rceil,
\qquad
k=\ell b.
\]
Then
\[
k=(C+o(1))\sqrt n\,\ln n.
\tag{2}
\]

Independently for every unordered pair \(\{u,v\}\), choose one of the three states
\[
\text{absent},\qquad u\to v,\qquad v\to u
\]
with respective probabilities
\[
1-p,\qquad \frac p2,\qquad \frac p2.
\]
This always produces an oriented graph, though its underlying graph may contain triangles.

### Bad triangle events

For every triple \(X=\{x,y,z\}\), let \(T_X\) be the event that all three underlying edges on \(X\) are present. Thus
\[
\Pr(T_X)=p^3.
\tag{3}
\]

### Bad block events

For every ordered collection
\[
\mathcal V=(V_1,\dots,V_\ell)
\]
of pairwise disjoint \(b\)-sets, let \(B_{\mathcal V}\) be the event that there is no arc from a later block to an earlier block.

The number of unordered pairs joining distinct blocks is
\[
R=\binom{\ell}{2}b^2
  =\frac{1-1/\ell}{2}k^2.
\tag{4}
\]
For each such pair, exactly one of its two possible orientations is forbidden by \(B_{\mathcal V}\). Therefore
\[
\Pr(B_{\mathcal V})
   =\left(1-\frac p2\right)^R
   \leq \exp\left(-\frac{pR}{2}\right).
\tag{5}
\]

---

## 4. Counting the block events

Let \(N_B\) be the number of ordered collections \(\mathcal V\). We have
\[
N_B\leq \frac{n^k}{(b!)^\ell}.
\]
Using \(b!\geq (b/e)^b\),
\[
\ln N_B
 \leq k\ln\left(\frac{en}{b}\right).
\]
Since
\[
b=(C+o(1))\frac{\sqrt n\,\ln n}{\ell}
\quad\text{and}\quad
\ln\ell=o(\ln n),
\]
it follows that
\[
\ln N_B
 \leq \left(\frac12+o(1)\right)k\ln n.
\tag{6}
\]

Moreover, by (2) and (4),
\[
pR
 =\left(\frac{cC}{2}+o(1)\right)k\ln n.
\tag{7}
\]

---

## 5. Applying the asymmetric Lovász local lemma

Use the standard dependency graph in which two events are adjacent when they involve a common unordered-pair variable.

Assign local-lemma activities
\[
x_T=(1+\delta_n)p^3,
\qquad
\delta_n=n^{-1/4},
\tag{8}
\]
to every triangle event, and
\[
x_B=\exp(-\beta pR)
\tag{9}
\]
to every block event.

Let
\[
W=N_Bx_B.
\]
By (6), (7), and \(\beta cC>1\),
\[
\ln W
 \leq
 \left(
 \frac12-\frac{\beta cC}{2}+o(1)
 \right)k\ln n,
\]
so
\[
W=\exp\bigl(-\Omega(k\ln n)\bigr)=o(1).
\tag{10}
\]

We use
\[
\prod_j(1-x_j)
 \geq
 \exp\left(-\sum_j\frac{x_j}{1-x_j}\right).
\tag{11}
\]

### 5.1 Triangle events

A triangle event has at most \(3(n-2)\) neighboring triangle events. The sum of the activities of all its neighboring block events is at most \(W\). Consequently,
\[
\sum_{E\sim T_X}\frac{x_E}{1-x_E}
 =O(np^3)+o(1)
 =O(n^{-1/2})+o(1)
 =o(\delta_n).
\]
Thus
\[
x_T\prod_{E\sim T_X}(1-x_E)
 \geq
 (1+\delta_n)p^3\exp(-o(\delta_n))
 \geq p^3
 =\Pr(T_X)
\]
for all sufficiently large \(n\).

### 5.2 Block events

A block event depends on \(R\) unordered-pair variables. Each such pair lies in at most \(n-2\) triples, so \(B_{\mathcal V}\) has at most \(R(n-2)\) neighboring triangle events. The total activity of its neighboring block events is again at most \(W=o(1)\). Hence
\[
\sum_{E\sim B_{\mathcal V}}\frac{x_E}{1-x_E}
 \leq
 Rn(1+o(1))p^3+o(1).
\]
Since \(np^2=c^2\),
\[
Rn p^3
 =c^2pR,
\]
and therefore
\[
\prod_{E\sim B_{\mathcal V}}(1-x_E)
 \geq
 \exp\left(-(c^2+o(1))pR\right).
\]
It follows that
\[
x_B\prod_{E\sim B_{\mathcal V}}(1-x_E)
 \geq
 \exp\left(-(\beta+c^2+o(1))pR\right).
\]
By (1),
\[
\beta+c^2<\frac12.
\]
Together with (5), this gives, for sufficiently large \(n\),
\[
\Pr(B_{\mathcal V})
 \leq
 \exp\left(-\frac{pR}{2}\right)
 \leq
 x_B\prod_{E\sim B_{\mathcal V}}(1-x_E).
\]

All asymmetric local-lemma inequalities are therefore satisfied. With positive probability, none of the triangle events and none of the block events occurs.

For such an outcome:

1. the underlying graph is triangle-free;
2. every ordered collection of \(\ell\) disjoint \(b\)-sets contains an arc from a later block to an earlier block.

Lemma 1 now gives
\[
\vec\alpha(D)<k
=(C+o(1))\sqrt n\,\ln n.
\tag{12}
\]

---

## 6. Optimization of the constant

Conditions (1) are feasible for a given \(C\) precisely when
\[
C>\frac{1}{c(1/2-c^2)}
\]
for some \(0<c<1/\sqrt2\). Now
\[
\max_{0<c<1/\sqrt2}c\left(\frac12-c^2\right)
\]
is attained at
\[
c=\frac1{\sqrt6}
\]
and equals
\[
\frac1{3\sqrt6}.
\]
Thus every \(C>3\sqrt6\) is admissible. From (12),
\[
\vec a(n)
 \leq
 \bigl(3\sqrt6+o(1)\bigr)\sqrt n\,\ln n.
\]

Finally, every dichromatic coloring of \(D\) has color classes of order at most \(\vec\alpha(D)\). Hence
\[
\vec\chi(D)\geq\frac{n}{\vec\alpha(D)},
\]
which yields
\[
\vec t(n)
 \geq
 \left(\frac1{3\sqrt6}-o(1)\right)
 \frac{\sqrt n}{\ln n}.
\]

This proves the stated partial theorem.

---

## 7. What would be needed to reach the conjectured order

The block argument also isolates a sufficient endpoint property.

Let \(G\) be a fixed triangle-free graph. For an ordered collection
\[
\mathcal V=(V_1,\dots,V_\ell),
\]
let \(e_\times(\mathcal V)\) denote the number of edges joining different blocks. If the edges of \(G\) are oriented independently and uniformly, then
\[
\Pr(B_{\mathcal V})=2^{-e_\times(\mathcal V)}.
\]
Consequently, if
\[
\min_{\mathcal V}e_\times(\mathcal V)>\log_2 N_B,
\tag{13}
\]
some orientation of \(G\) has no acyclic set of order \(k=\ell b\).

For
\[
k=K\sqrt{n\ln n}
\]
and slowly growing \(\ell\), one has
\[
\ln N_B=\left(\frac12+o(1)\right)k\ln n.
\]
Thus (13) would follow, for sufficiently large \(K\), from a triangle-free graph satisfying a robust cross-density estimate of the form
\[
e_\times(\mathcal V)
 \geq
 \gamma\sqrt{\frac{\ln n}{n}}\,
 \frac{k^2}{2}
\]
for every such ordered block collection, where \(\gamma>0\) is constant. This would give
\[
\vec\alpha(D)=O(\sqrt{n\ln n})
\]
and prove the conjectured lower bound for \(\vec t(n)\).

The ordinary Ramsey property
\[
\alpha(G)=O(\sqrt{n\ln n})
\]
does not supply this estimate: it only ensures the existence of an edge in sufficiently large sets, whereas the block argument needs \(\Theta(k\ln n)\) suitably distributed cross-edges.

There is also a clear barrier in the local-lemma construction above. For edge probability \(p\), a block event has probability roughly
\[
\exp(-pR/2),
\]
while its \(R(n-2)\) neighboring triangle events impose a local-lemma cost of order
\[
np^3R=(np^2)pR.
\]
Positive slack in this direct variable-event local lemma therefore requires \(np^2=O(1)\). At the conjectural triangle-free-process density
\[
p\asymp\sqrt{\frac{\ln n}{n}},
\]
one has \(np^2\asymp\ln n\), so this proof cannot be pushed to the endpoint. A genuinely stronger triangle-free-process lower-tail or robust cross-density estimate is still missing.

Thus the conjecture remains unresolved.