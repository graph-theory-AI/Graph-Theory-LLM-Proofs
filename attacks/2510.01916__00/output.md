```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Unrestricted circuit distance is NP-hard for irredundant rational polygons when the target may lie in the relative interior of an edge, but the reduction does not make the target a vertex.",
  "would_publish": false,
  "caveats": "The usual formulation of Conjecture 21 appears to require both terminals to be vertices; if arbitrary rational boundary terminals are allowed, the argument proves the stated conjecture."
}
```

# 1. Statement and endpoint convention

I use the standard definition of a maximal circuit step. For
\[
P=\{x\in\mathbb R^2:Ax\le b\},
\]
a circuit direction is a nonzero \(g\) for which \(\operatorname{supp}(Ag)\) is inclusion-minimal. A signed maximal circuit step from \(x\in P\) in direction \(g\) is
\[
x\longmapsto x+\alpha g,\qquad
\alpha=\max\{\lambda\ge 0:x+\lambda g\in P\}.
\]

The usual Circuit Distance problem asks for the minimum number of such steps between two vertices. I do not obtain the vertex-to-vertex result. I prove the following nearby result.

## Theorem

The following problem is NP-hard:

- input: an irredundantly described rational polygon \(P\), a vertex \(s\), a rational point \(t\) in the relative interior of an edge of \(P\), and \(k\in\mathbb N\);
- question: is there an unrestricted, not necessarily monotone, circuit walk from \(s\) to \(t\) of length at most \(k\)?

The constructed polygon is centrally symmetric, has \(4m+4\) edges, and its circuit directions are exactly its edge directions.

If the source paper's formal definition permits arbitrary rational terminals rather than vertices, this proves the catalog statement. Under the customary vertex-terminal definition, it is only a partial result.

# 2. Circuits of an irredundant polygon

We first record the elementary two-dimensional fact used below.

## Lemma 1

Let \(P=\{x:Ax\le b\}\subset\mathbb R^2\) be full-dimensional, bounded, and irredundantly described. Its circuit directions are precisely its edge directions.

### Proof

If \(g\ne0\) is not annihilated by any row of \(A\), then
\(\operatorname{supp}(Ag)\) is the full row set. For any row \(a_i\), a nonzero vector \(h\in\ker a_i\) has strictly smaller support, so \(g\) is not a circuit.

Conversely, suppose \(a_i g=0\). All rows annihilating \(g\) are parallel. If a nonzero \(h\) had
\[
\operatorname{supp}(Ah)\subsetneq\operatorname{supp}(Ag),
\]
then \(h\) would be annihilated both by every row annihilating \(g\) and by an additional, nonparallel row. Two nonparallel rows have trivial common kernel in \(\mathbb R^2\), a contradiction. Thus \(g\) is a circuit. Since each row of an irredundant description supports an edge, these are exactly the edge directions. ∎

For any direction \(g\), the intersection of \(P\) with a line parallel to \(g\) is a segment. A maximal signed circuit step terminates at one endpoint of this segment.

# 3. Reduction from Exact Cover by 3-Sets

Let an instance of X3C be given by
\[
U=\{1,\dots,3q\},\qquad
\mathcal S=\{S_1,\dots,S_m\},
\]
where every \(S_i\) has three elements. Duplicate sets can be removed: using two copies of the same triple cannot occur in an exact cover.

Set
\[
R=q+1,
\]
and encode the sets by
\[
a_i=\sum_{r\in S_i}R^{r-1},
\qquad
B=\sum_{r=1}^{3q}R^{r-1}.
\]
Let
\[
A=\max_i a_i.
\]

The following standard positional-encoding property remains valid even though a circuit walk may reuse a direction.

## Lemma 2

For indices \(i_1,\dots,i_q\), repetitions allowed,
\[
a_{i_1}+\cdots+a_{i_q}=B
\]
if and only if \(S_{i_1},\dots,S_{i_q}\) form an exact cover of \(U\).

### Proof

At each base-\(R\) digit, the sum has a coefficient between \(0\) and \(q<R\), so no carrying occurs. Equality with \(B\), whose digits are all \(1\), says that every element of \(U\) occurs exactly once. This also excludes repeated triples. ∎

Choose
\[
D=10q(A+B+1),\qquad W=D+A,
\]
and define
\[
x_*=qD+B,\qquad
M=x_*+(q+2)W+2.
\]
The only inequalities needed later are
\[
(q-1)W<x_*,\qquad M-qW>x_*.
\tag{1}
\]

Finally, put
\[
\varepsilon=\frac1{100mW},
\qquad
\delta=\varepsilon\sum_{i=1}^m(D+a_i).
\]
Then
\[
0<\delta\le \frac1{100},\qquad 1-2m\varepsilon>0.
\]

# 4. Construction of the polygon

Relabel so that
\[
a_1<a_2<\cdots<a_m.
\]
Define
\[
p_i=(D+a_i,1),\qquad n_i=(-(D+a_i),1).
\]

Starting at \(s=(0,0)\), take the following edge vectors in cyclic order:
\[
\begin{aligned}
&(M,0),\\
&\varepsilon p_m,\varepsilon p_{m-1},\dots,\varepsilon p_1,\\
&(0,1-2m\varepsilon),\\
&\varepsilon n_1,\varepsilon n_2,\dots,\varepsilon n_m,\\
&(-M,0),\\
&-\varepsilon p_m,-\varepsilon p_{m-1},\dots,-\varepsilon p_1,\\
&(0,-(1-2m\varepsilon)),\\
&-\varepsilon n_1,-\varepsilon n_2,\dots,-\varepsilon n_m.
\end{aligned}
\tag{2}
\]

These vectors sum to zero. Their polar angles are strictly increasing cyclically. Hence they form the boundary of a convex polygon \(P\). All edges have positive length, so its facet description is irredundant.

The geometry is especially simple:

- the bottom edge is
  \[
  E_0=[0,M]\times\{0\};
  \]
- the top edge is
  \[
  E_1=[0,M]\times\{1\};
  \]
- the right cap lies in
  \[
  [M,M+\delta]\times[0,1];
  \]
- the left cap lies in
  \[
  [-\delta,0]\times[0,1].
  \]

In particular,
\[
[0,M]\times[0,1]\subseteq P.
\]

By Lemma 1, the circuit directions, up to sign, are exactly
\[
(1,0),\quad (0,1),\quad (D+a_i,1),\quad (-(D+a_i),1)
\quad(1\le i\le m).
\tag{3}
\]

Define the target
\[
t=
\begin{cases}
(x_*,0),&q\text{ even},\\
(x_*,1),&q\text{ odd}.
\end{cases}
\tag{4}
\]
Since \(0<x_*<M\), this lies in the relative interior of \(E_0\) or \(E_1\).

Set \(k=q\).

All coordinates have bit length polynomial in the X3C input size, and the vertex list can be converted to an irredundant rational \(H\)-description in polynomial time.

# 5. Excluding every non-monotone shortcut

A nonhorizontal circuit direction in (3) satisfies
\[
|\Delta x|\le W|\Delta y|\le W
\tag{5}
\]
during any maximal step, because \(P\subseteq\mathbb R\times[0,1]\).

## Lemma 3

No circuit walk from \(s\) to \(t\) of length at most \(q\) uses a horizontal step.

### Proof

Suppose a walk uses a horizontal step, and consider its last such step. A horizontal section of \(P\) has one endpoint in the left band
\[
[-\delta,0]\times[0,1]
\]
and the other in the right band
\[
[M,M+\delta]\times[0,1].
\]
Thus the endpoint of the last horizontal step has either \(x\le0\) or \(x\ge M\).

There are at most \(q-1\) remaining steps, all nonhorizontal.

- If \(x\le0\), then by (5) the final \(x\)-coordinate is at most
  \[
  (q-1)W<x_*.
  \]
- If \(x\ge M\), then the final \(x\)-coordinate is at least
  \[
  M-(q-1)W>M-qW>x_*.
  \]

Both contradict the target coordinate \(x_*\). ∎

## Lemma 4

Except for the starting point \(s\), no walk of length at most \(q\) ending at \(t\) visits either cap.

### Proof

By Lemma 3 all steps are nonhorizontal.

If the walk reaches the right cap, its \(x\)-coordinate is at least \(M\). Even after \(q\) further nonhorizontal steps, its \(x\)-coordinate remains greater than
\[
M-qW>x_*.
\]

If it reaches the left cap after at least one step, at most \(q-1\) steps remain. Starting from \(x\le0\), its final \(x\)-coordinate is at most
\[
(q-1)W<x_*.
\]
Both are impossible. ∎

It follows that every successful walk, after leaving \(s\), stays in the relative interiors of \(E_0\) and \(E_1\). Every nonhorizontal, nonvertical step therefore crosses the entire vertical width of the rectangle and changes \(x\) by exactly
\[
\pm(D+a_i).
\tag{6}
\]
A vertical step changes \(x\) by zero.

## Lemma 5

Every walk from \(s\) to \(t\) of length at most \(q\) has exactly \(q\) steps, all of which have positive horizontal displacement.

### Proof

A walk with at most \(q-1\) steps has final \(x\)-coordinate at most
\[
(q-1)W<x_*.
\]
Hence a successful walk has exactly \(q\) steps.

If one step is vertical, the remaining \(q-1\) steps contribute at most \((q-1)W<x_*\).

If one step has negative horizontal displacement, that step contributes at most \(-D\), while the other \(q-1\) steps contribute at most \(W\) each. Hence the total is at most
\[
(q-1)W-D < (q-1)W < x_*.
\]
Thus all \(q\) steps have positive horizontal displacement. ∎

Consequently, every successful walk has total displacement
\[
qD+\sum_{j=1}^q a_{i_j}.
\]
It reaches \(t\) exactly when
\[
\sum_{j=1}^q a_{i_j}=B.
\tag{7}
\]

By Lemma 2, this is equivalent to an exact cover.

Conversely, given an exact cover \(S_{i_1},\dots,S_{i_q}\), start from \(s\) and alternately use

- \((D+a_{i_j},1)\) from the bottom edge to the top edge;
- \((D+a_{i_j},-1)\) from the top edge to the bottom edge.

All partial \(x\)-coordinates lie between \(0\) and \(x_*<M\). The resulting chords lie in the contained rectangle, so they are maximal steps between \(E_0\) and \(E_1\). After \(q\) steps the walk ends at \(t\).

This proves the theorem.

# 6. Complexity status of the vertex-terminal problem

For completeness, the usual vertex-to-vertex Circuit Distance problem on rational polygons is in NP.

If the polygon has \(f\) geometric edges, its two vertices can always be joined along the shorter boundary arc in at most
\[
\left\lfloor\frac f2\right\rfloor
\]
edge steps, and every edge step is a maximal circuit step. Thus instances with larger \(k\) are automatically yes-instances, and otherwise a certificate has \(O(f)\) directions and signs.

In dimension two, circuit directions can be enumerated from the rows of \(A\). Given the current rational point and a signed direction \(g\), the maximal step length is
\[
\alpha=\min_{i:a_i g>0}
\frac{b_i-a_i x}{a_i g}.
\]
Exact rational arithmetic verifies the whole walk in polynomial time. Hence, if Conjecture 21 is proved, the problem is NP-complete rather than merely NP-hard.

# 7. Remaining gap

The target \(t\) in (4) is not a vertex. This is not a cosmetic defect.

If one simply terminates the horizontal state edge at \(t\), then from every point on that edge a maximal step parallel to the edge reaches \(t\) immediately. Since the construction visits each of the two state edges repeatedly, this creates very short false-positive walks. Marking \(t\) as a collinear “vertex” does not make it an extreme point, while bending or truncating the edge introduces exactly this tangent shortcut.

Thus a proof of the original vertex-to-vertex conjecture still needs a terminal gadget that converts the relative-interior target into a genuine vertex while excluding:

1. tangent moves along the target's incident edges;
2. walks entering the terminal cap from one of the long state-edge endpoints;
3. uses of the new terminal edge directions earlier in the walk.

No such gadget is established here, so I do not claim Conjecture 21 in its usual vertex-terminal formulation.