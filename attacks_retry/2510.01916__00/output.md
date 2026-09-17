```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The vertex-terminal conjecture remains unresolved here, but the fixed edge-midpoint variant is NP-complete, and rational polygons attain the general vertex-distance upper bound.",
  "would_publish": false,
  "caveats": "The hardness reduction still has a nonvertex target; the separate vertex-truncation construction has no proved polynomial encoding bound."
}
```

## 1. Results and endpoint convention

I use the vertex-terminal interpretation of Circuit Distance: the input specifies two vertices \(s,t\) of a rational polygon, and every circuit step must be maximal.

I do **not** prove NP-hardness for that interpretation. I establish two partial results:

1. **Sharp vertex-distance examples.** For every \(d\ge 1\), there is a rational polygon with \(2d+1\) edges, no parallel edges, and two vertices at circuit distance exactly \(d\). Thus the elementary upper bound \(\lfloor f/2\rfloor\), for an \(f\)-gon, is attained for every odd \(f\).
2. **A strengthened boundary-terminal hardness result.** Circuit Distance is NP-complete, under the promise \(k\le f\), even when
   - \(P\) is centrally symmetric and irredundantly described;
   - \([0,1]\times\{0\}\) and \([0,1]\times\{1\}\) are edges;
   - \[
     [0,1]^2\subseteq P\subseteq
     [-1/100,1+1/100]\times[0,1];
     \]
   - the terminals are the fixed points
     \[
     s=(0,0),\qquad t=(1/2,0).
     \]
   Here \(s\) is a vertex, but \(t\) is the midpoint of an edge.

The second result reuses—and verifies—the positional encoding and cap-exclusion mechanism from the supplied attempt. Choosing the strip length differently makes the target a fixed midpoint. The first result is a separate vertex-terminal construction. I make no literature-priority claim for that auxiliary diameter result.

## 2. Definitions and elementary facts

Let
\[
P=\{x\in\mathbb R^2:Ax\le b\}
\]
be full-dimensional, bounded, and irredundantly described. A circuit direction is a nonzero \(g\) for which \(\operatorname{supp}(Ag)\) is inclusion-minimal.

A maximal signed circuit step is
\[
x\longmapsto x+\alpha g,\qquad
\alpha=\max\{\lambda\ge0:x+\lambda g\in P\}>0.
\]

### Edge directions are precisely the circuits

If no row of \(A\) annihilates \(g\), its support is the full row set and is not minimal. Conversely, suppose \(a_i g=0\). Any vector with strictly smaller support would have to be annihilated by \(a_i\) and by another, nonparallel row. In dimension two this forces the vector to be zero. Thus the circuits are exactly the facet-edge directions.

In particular, traversing an edge between its endpoints is a maximal circuit step. Consequently, any two vertices of an \(f\)-gon have circuit distance at most
\[
\left\lfloor\frac f2\right\rfloor.
\tag{1}
\]

### Verification and membership in NP

A certificate is a sequence of signed edge-direction indices. Given its current point \(x\) and direction \(g\), a verifier computes
\[
\alpha=\min_{i:a_i g>0}\frac{b_i-a_i x}{a_i g}.
\tag{2}
\]

Polynomially many steps can be verified with polynomial bit complexity. Indeed, after clearing the input denominators, a step blocked by row \(a_i\) is the rational affine transformation
\[
x\longmapsto
\left(I-\frac{g a_i}{a_i g}\right)x
+\frac{b_i g}{a_i g}.
\]
Composing \(k\) such transformations increases bit length by only a polynomial in the input length and \(k\).

Thus the vertex-terminal problem is in NP by (1). The boundary-terminal problem is also in NP under the explicit promise \(k\le f\). No unrestricted polynomial certificate bound for arbitrary boundary terminals is being assumed.

## 3. A vertex construction attaining the upper bound

The following lemma gives a controlled way to increase a vertex distance.

### Lemma: double truncation increases distance by one

Let \(s,v\) be distinct vertices of a rational polygon \(P\), with circuit distance \(d\). Assume that neither edge incident with \(v\) has a parallel edge elsewhere in \(P\).

Then one can truncate a sufficiently small neighborhood of \(v\) using two new facets, obtaining a rational polygon \(P'\) and a new vertex \(v'\), such that

- \(P'\) has exactly two more edges than \(P\);
- all old edges survive;
- \(s\) remains a vertex;
- \(\operatorname{dist}_{P'}(s,v')=d+1\).

The new edge directions can be chosen different from all old edge directions.

#### Proof

Let \(e_1,e_2\) denote the two edge directions at \(v\).

**Step 1: adding nearby directions does not shorten the distance to \(v\).**

Choose two additional direction lines \(a,b\), approaching \(e_1,e_2\), respectively. Temporarily allow these directions for maximal steps in the unchanged polygon \(P\).

For sufficiently close choices, no such augmented walk of length at most \(d-1\) reaches \(v\). Suppose otherwise. There would be a sequence of choices \(a_n,b_n\) converging to \(e_1,e_2\), and augmented walks of a common length \(h\le d-1\), ending at \(v\).

Normalize directions to unit length. Passing to a subsequence, every direction label and every point of the walks has a limit. Delete zero-length limit steps.

A positive limit step can fail to be maximal only if its limiting segment lies in an edge \(F\) and stops in the relative interior of \(F\). Such a failure cannot come from an unchanged direction: near a relative-interior point of \(F\), the endpoints lie on \(F\), and a maximal step in a fixed direction parallel to \(F\) ends at an endpoint of \(F\).

Therefore the first nonmaximal positive limit step, if any, comes from one of the two varying directions. Its limiting edge \(F\) is parallel to \(e_1\) or \(e_2\). By the hypothesis on parallel edges, \(F\) is incident with \(v\).

All preceding positive limit steps form a valid old circuit walk. From the current point on \(F\), one edge step reaches \(v\), using the appropriate sign. This yields an old walk to \(v\) of length at most \(h<d\), a contradiction. If every positive limit step is maximal, the entire limiting walk gives the same contradiction.

Fix rational directions \(a,b\) sufficiently close that the augmented distance to \(v\) remains \(d\). Choose their normals strictly between the two facet normals at \(v\), so that they can be used to truncate \(v\).

**Step 2: isolate the short reachable points.**

Let \(R\) be the finite set of points reachable from \(s\) in at most \(d-1\) augmented steps in \(P\). It is finite because there are finitely many direction choices and each maximal step is determined by its starting point and signed direction.

We have \(v\notin R\). Choose a neighborhood \(U\) of \(v\), disjoint from \(R\) and from every other old vertex.

Cut off \(v\) with two facets of directions \(a,b\), meeting at a point \(v'\) in the interior of \(P\), sufficiently close to \(v\). The removed corner and both new edges then lie in \(U\). The replacement boundary is
\[
u,\ v',\ w,
\]
where \(u,w\) lie on the two old incident edges.

No walk of length at most \(d-1\) is changed by these cuts. For otherwise, at the first changed step, its endpoint in the uncut polygon would lie in the removed corner, hence in \(U\), contradicting the definition of \(R\).

**Step 3: choose \(v'\) to avoid every \(d\)-step arrival.**

The directions \(a,b\) are now fixed, while the two facet offsets—and hence \(v'\)—may still vary.

If a \(d\)-step walk ends at \(v'\), its penultimate point belongs to \(R\).

- Its last direction cannot be \(a\) or \(b\): the line through \(v'\) in that direction intersects \(P'\) in the corresponding new edge, entirely contained in \(U\), whereas the penultimate point lies outside \(U\).
- For an old direction \(g\), the target would have to lie on
  \[
  p+\mathbb R g
  \]
  for some \(p\in R\).

There are only finitely many such lines. Choose a rational \(v'\), sufficiently close to \(v\), avoiding their union. Then its distance from \(s\) is at least \(d+1\).

For the reverse inequality, take an old shortest \(d\)-step walk to \(v\). Its first \(d-1\) steps are unchanged. Its last step now stops on one of the two new edges, from which one edge step reaches \(v'\). Thus its new length is \(d+1\). ∎

### Corollary

For every \(d\ge1\), there is a rational \((2d+1)\)-gon, with no parallel edges, containing two vertices at circuit distance exactly \(d\).

#### Proof

Start with a rational triangle and two distinct vertices, at distance \(1\). Apply the lemma \(d-1\) times, always choosing the new directions nonparallel to every existing edge.

The resulting polygon has
\[
3+2(d-1)=2d+1
\]
edges and the distinguished distance is \(d\). Equality with the upper bound follows from (1). ∎

This construction rules out a dimension-two constant-distance shortcut. It does **not** yet provide a polynomial-size terminal gadget: the proof uses successively small perturbations and finite reachable sets, without a polynomial bound on the required coordinate encoding.

## 4. NP-completeness with a fixed edge-midpoint target

I now prove the boundary-terminal theorem.

### 4.1. Positional encoding

Reduce from Exact Cover by 3-Sets. Write the instance as
\[
U=\{1,\dots,3q\},\qquad
\mathcal S=\{S_1,\dots,S_m\}.
\]
We may assume that the triples are distinct and that
\[
2\le q\le m,\qquad q\ \text{is even}.
\]
Trivial instances can be handled separately. If necessary, adjoining three new elements appearing together in one new forced triple changes the parity of \(q\).

Put
\[
R=q+1,\qquad
a_i=\sum_{r\in S_i}R^{r-1},\qquad
B=\sum_{r=1}^{3q}R^{r-1}.
\]
For any \(q\) indices, repetitions allowed,
\[
\sum_{j=1}^q a_{i_j}=B
\quad\Longleftrightarrow\quad
S_{i_1},\dots,S_{i_q}\text{ form an exact cover}.
\tag{3}
\]
Indeed, every digit coefficient in the sum is at most \(q<R\), so there is no carrying. Equality says that every element occurs exactly once.

Let
\[
A=\max_i a_i,\qquad
D=10q(A+B+1),\qquad
w_i=D+a_i,\qquad W=D+A.
\]
Define
\[
x_*=qD+B,\qquad M=2x_*.
\]
The crucial inequality is
\[
(q-1)W<x_*.
\tag{4}
\]
Since \(M=2x_*\), it also gives
\[
M-(q-1)W>x_*.
\tag{5}
\]

### 4.2. Polygon construction

Relabel the sets so that
\[
a_1<a_2<\cdots<a_m.
\]
Set
\[
p_i=(w_i,1),\qquad n_i=(-w_i,1),\qquad
\varepsilon=\frac1{100mW},
\]
and
\[
\delta=\varepsilon\sum_{i=1}^m w_i\le\frac1{100}.
\]

Starting at \(s=(0,0)\), use these edge vectors in cyclic order:
\[
\begin{aligned}
&(M,0),\\
&\varepsilon p_m,\ldots,\varepsilon p_1,\\
&(0,1-2m\varepsilon),\\
&\varepsilon n_1,\ldots,\varepsilon n_m,\\
&(-M,0),\\
&-\varepsilon p_m,\ldots,-\varepsilon p_1,\\
&(0,-(1-2m\varepsilon)),\\
&-\varepsilon n_1,\ldots,-\varepsilon n_m.
\end{aligned}
\tag{6}
\]

These positive-length vectors are strictly cyclically ordered and sum to zero, so they form a convex polygon \(P\). Its description by the resulting facet inequalities is irredundant.

The polygon is centrally symmetric, has \(4m+4\) edges, and satisfies
\[
[0,M]\times[0,1]\subseteq P
\subseteq[-\delta,M+\delta]\times[0,1].
\]
Its bottom and top edges are exactly
\[
[0,M]\times\{0\},\qquad [0,M]\times\{1\}.
\]
The remaining edges form a left cap with \(x\le0\) and a right cap with \(x\ge M\).

Its circuit directions, up to sign, are
\[
(1,0),\quad(0,1),\quad(w_i,1),\quad(-w_i,1)
\qquad(1\le i\le m).
\tag{7}
\]

Take
\[
t=(x_*,0),\qquad k=q.
\]
Thus \(t\) is the midpoint of the bottom edge.

All numbers in the construction have bit length polynomial in the X3C instance size.

### 4.3. Excluding unrestricted shortcuts

For every nonhorizontal circuit step,
\[
|\Delta x|\le W|\Delta y|\le W,
\tag{8}
\]
because the polygon has vertical width \(1\).

Consider a walk of length at most \(q\) from \(s\) to \(t\).

**It cannot contain a horizontal step.** Consider its last horizontal step. A maximal horizontal step ends either in the left cap, with \(x\le0\), or in the right cap, with \(x\ge M\). At most \(q-1\) subsequent nonhorizontal steps remain.

From the left cap, their final coordinate is at most \((q-1)W<x_*\). From the right cap, it is at least \(M-(q-1)W>x_*\). Both are impossible.

**It cannot visit either cap after its first step.** All steps are now nonhorizontal. A cap visit after at least one step leaves at most \(q-1\) steps, and the identical bounds (4)–(5) exclude reaching \(t\).

Therefore every point after the start lies in the relative interior of the bottom or top edge. Every nonvertical step crosses the full strip and changes its horizontal coordinate by exactly
\[
\pm w_i.
\]

**There must be exactly \(q\) steps, all with positive horizontal displacement.** Fewer steps have total horizontal displacement at most \((q-1)W<x_*\). If one of \(q\) steps has nonpositive horizontal displacement, the same bound applies to the total.

Thus every successful walk has displacement
\[
x_*=\sum_{j=1}^q w_{i_j}
=qD+\sum_{j=1}^q a_{i_j}.
\]
By (3), it yields an exact cover.

Conversely, an exact cover gives a walk by alternating the directions
\[
(w_{i_j},1)\quad\text{and}\quad(w_{i_j},-1).
\]
All partial horizontal sums lie in \([0,x_*]\), so the corresponding segments cross the contained rectangle and are maximal steps between its two horizontal edges. Since \(q\) is even, the walk ends at \((x_*,0)\).

Hence
\[
\operatorname{dist}_P(s,t)\le q
\quad\Longleftrightarrow\quad
\text{the X3C instance has an exact cover}.
\tag{9}
\]

### 4.4. Fixed terminals and the promised geometry

Apply the invertible affine map
\[
(x,y)\longmapsto(x/M,y).
\]
Invertible affine maps preserve edge directions, maximality, and circuit-walk length. The terminals become
\[
s=(0,0),\qquad t=(1/2,0),
\]
and
\[
[0,1]^2\subseteq P
\subseteq[-1/100,1+1/100]\times[0,1].
\]

Finally, \(k=q\le m<4m+4=f\). The membership-in-NP argument from Section 2 therefore applies. This proves the stated NP-completeness result.

## 5. What remains missing

The midpoint theorem does not establish vertex-to-vertex hardness. A midpoint of a facet is not an extreme point, and calling it a collinear “vertex” does not change that.

Making it an endpoint of a long computational edge creates a tangent shortcut: any previously reached point on that edge can move directly to the new endpoint in one maximal edge step.

The double-truncation lemma demonstrates that genuine vertices can be protected by additional facets. However, it does not complete the reduction for two separate reasons:

1. It does not preserve all intended arithmetic arrivals at a prescribed nonvertex point.
2. Its perturbation argument supplies no polynomial bound on the bit length needed after \(O(q)\) successive truncations.

Thus there is still no polynomial-time reduction with two vertex terminals in this writeup. If the formal source definition permits arbitrary rational boundary terminals, Section 4 settles that variant; I do not use the endpoint ambiguity to claim that Conjecture 21 has been proved.