```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit closure-of-a-regular-tree family has the conjectured lower bound for every level-homogeneous colouring, and any substantially smaller arbitrary colouring must have a constant-coloured root fibre, but the unrestricted c≥4 case remains open.",
  "would_publish": false,
  "caveats": "The matching lower bound assumes level-homogeneity; the unrestricted root-fibre lemma does not suffice to control colourings inside different branches."
}
```

## 1. Statement and status

Write
\[
\alpha_c:=\frac{c}{c^2-c+1}.
\]
The conjecture asks for fixed \(t=t(c)\) and infinitely many pairs \((H,P)\), with \(\operatorname{tw}(H)=t\), such that every \(c\)-colouring of \(H\boxtimes P\) has a monochromatic component of order
\[
\Omega\!\left(|V(H\boxtimes P)|^{\alpha_c}\right).
\]

The supplied source establishes this without restrictions for \(c=2,3\). I do not settle the unrestricted case \(c\ge4\). I prove two related statements:

1. an unrestricted structural lemma showing that, on a natural candidate family, every colouring with clustering below order \(q^c\) has a monochromatic root fibre; and
2. the full conjectured lower bound on that family for all colourings invariant under rooted-tree automorphisms, equivalently colourings depending only on tree depth and path position.

The second result gives an explicit treewidth
\[
t=c(c-1)
\]
for the symmetric version of the conjecture.

---

## 2. The candidate graphs

Let \(T_{q,h}\) be the complete rooted \(q\)-ary tree of height \(h\), with levels \(0,\dots,h\). Let
\[
C_{q,h}
\]
be its closure: two distinct vertices are adjacent precisely when one is an ancestor of the other.

We use
\[
h:=c(c-1),\qquad H_q:=C_{q,h},\qquad P:=P_q,
\]
where \(P_q\) has \(q\) vertices.

### Basic parameters

The number of vertices is
\[
|V(H_q)|=1+q+\cdots+q^h=\Theta(q^h),
\]
and hence
\[
n_q:=|V(H_q\boxtimes P_q)|
 =\Theta(q^{h+1})
 =\Theta(q^{c^2-c+1}).
\]

Moreover,
\[
\operatorname{tw}(H_q)=h=c(c-1).
\]
Indeed, eliminating vertices in nonincreasing order of depth is a perfect elimination ordering: the remaining neighbours of a vertex are its ancestors, which form a clique. Thus the treewidth is at most \(h\), while every root-to-leaf path is a clique of order \(h+1\).

Consequently,
\[
q^c=\Theta\!\left(n_q^{c/(c^2-c+1)}\right).
\]

---

## 3. A one-layer obstruction

The following elementary lemma explains the choice \(h=c(c-1)\).

### Lemma 3.1

For positive integers \(r,s,q\), every \(r\)-colouring of \(C_{q,rs}\) has a monochromatic component of order at least \(q^s\).

#### Proof

Induct on \(r\). For \(r=1\), the graph is connected and has at least \(q^s\) vertices.

Suppose \(r\ge2\), and let \(\gamma\) be the colour of the root. Since the root is adjacent to every other vertex, all \(\gamma\)-coloured vertices lie in its monochromatic component. If there are at least \(q^s\) such vertices, we are done.

Otherwise, consider the \(q^s\) rooted subtrees beginning at level \(s\). If every such subtree contained a \(\gamma\)-coloured vertex, the root component would contain at least \(q^s\) vertices. Hence some one of these subtrees contains no vertex of colour \(\gamma\). It induces \(C_{q,(r-1)s}\) and is coloured with at most \(r-1\) colours. Induction completes the proof. \(\square\)

Taking \(r=c\) and \(s=c-1\), every individual \(H_q\)-layer in \(H_q\boxtimes P_q\) contains a monochromatic component of order at least \(q^{c-1}\). The conjectured product lower bound asks, in effect, for an additional factor \(q\).

---

## 4. An unrestricted root-fibre rigidity lemma

Let \(\rho\) denote the root of \(T_{q,h}\).

### Lemma 4.1

For every \(c\ge2\), if the colour sequence on
\[
\{(\rho,i):i\in V(P_q)\}
\]
is not constant, then the colouring of \(H_q\boxtimes P_q\) has a monochromatic component of order at least \(q^c/2\).

#### Proof

Choose consecutive path vertices \(i,i+1\) such that
\[
\phi(\rho,i)=\alpha\ne\beta=\phi(\rho,i+1).
\]
Let \(K_\alpha\) and \(K_\beta\) be the corresponding monochromatic components.

At depth \(c\) there are \(q^c\) pairwise disjoint rooted subtrees, each isomorphic to
\[
C_{q,h-c}=C_{q,c(c-2)}.
\]
Consider their vertices in product layer \(i\).

Every \(\alpha\)-coloured vertex in this layer is adjacent to \((\rho,i)\), and hence belongs to \(K_\alpha\). Every \(\beta\)-coloured vertex in layer \(i\) is diagonally adjacent to \((\rho,i+1)\), and hence belongs to \(K_\beta\).

If these depth-\(c\) subtrees together contain at least \(q^c\) vertices of colours \(\alpha\) or \(\beta\) in layer \(i\), then
\[
\max\{|K_\alpha|,|K_\beta|\}\ge \frac{q^c}{2}.
\]

Otherwise, one of the \(q^c\) subtrees contains no vertex of colour \(\alpha\) or \(\beta\) in layer \(i\). For \(c\ge3\), its copy of \(C_{q,c(c-2)}\) is therefore coloured with at most \(c-2\) colours. Lemma 3.1, with \(r=c-2\) and \(s=c\), gives a monochromatic component of order at least \(q^c\). For \(c=2\), a subtree avoiding both available colours cannot exist.

Thus in all cases there is a component of order at least \(q^c/2\). \(\square\)

### Corollary 4.2

Suppose a \(c\)-colouring has clustering less than \(q^c/2\). Then the root fibre is monochromatic, say of colour \(\alpha\), and the total number of \(\alpha\)-coloured vertices in the entire product is less than \(q^c/2\).

#### Proof

Constancy follows from Lemma 4.1. The root fibre is connected. Every other \(\alpha\)-coloured vertex \((v,i)\) is adjacent to \((\rho,i)\), so every \(\alpha\)-coloured vertex lies in the same component. \(\square\)

In particular, more than \(q^c/2\) of the depth-\(c\) rooted subtrees are entirely free of colour \(\alpha\) throughout their product with \(P_q\). Each such clean subtree has height
\[
h-c=c(c-2)
\]
and is coloured with \(c-1\) colours.

This does not finish the induction. For \(c-1\) colours and desired component size \(q^c\), the natural critical height would be
\[
(c-1)^2=c(c-2)+1,
\]
exactly one more than the height of a clean subtree. Thus the straightforward induction loses one tree level. The large number of parallel clean subtrees would have to be exploited through their common ancestors.

---

## 5. Matching lower bound for level-homogeneous colourings

Call a colouring \(\phi\) **level-homogeneous** if there is a function
\[
f:\{0,\dots,h\}\times V(P_q)\longrightarrow [c]
\]
such that
\[
\phi(v,i)=f(\operatorname{depth}(v),i).
\]
Equivalently, the colouring is invariant under all root-preserving automorphisms of \(T_{q,h}\).

### Theorem 5.1

For every fixed \(c\ge2\), every level-homogeneous \(c\)-colouring of
\[
C_{q,c(c-1)}\boxtimes P_q
\]
has clustering at least
\[
\frac{q^c}{c\bigl((c-1)^2+1\bigr)}.
\]
There is also a level-homogeneous \(c\)-colouring with clustering at most \(2q^c\).

Thus the optimal clustering among level-homogeneous colourings is
\[
\Theta_c(q^c)
 =\Theta_c\!\left(n_q^{c/(c^2-c+1)}\right).
\]

#### Proof of the lower bound

For a colour \(\alpha\) and path position \(i\), let
\[
D_\alpha(i):=\{d\in\{0,\dots,h\}:f(d,i)=\alpha\}.
\]

Suppose first that, for some \(\alpha,i\), there are \(d<e\) in \(D_\alpha(i)\) with
\[
e-d\ge c.
\]
Choose a vertex \(x\) at depth \(d\). All \(q^{e-d}\) descendants of \(x\) at depth \(e\) have colour \(\alpha\) in layer \(i\), and each is adjacent to \((x,i)\). Hence one monochromatic component has at least
\[
q^{e-d}\ge q^c
\]
vertices.

We may therefore assume that every nonempty \(D_\alpha(i)\) has diameter at most \(c-1\), and consequently
\[
|D_\alpha(i)|\le c. \tag{5.1}
\]

There are
\[
h+1=c(c-1)+1
\]
tree levels. At every fixed path position \(i\):

- no colour can be absent, since the other \(c-1\) colours could cover at most
  \[
  c(c-1)=h
  \]
  levels by (5.1);
- at least one colour occurs on exactly \(c\) levels, since otherwise all \(c\) colours together would again cover at most \(c(c-1)=h\) levels.

If \(|D_\alpha(i)|=c\), then the diameter bound forces
\[
D_\alpha(i)=\{a,a+1,\dots,a+c-1\}
\]
for some \(a\in\{0,\dots,h-c+1\}\).

For each path position, select one such pair \((\alpha,a)\). There are at most
\[
C_c:=c(h-c+2)
   =c\bigl((c-1)^2+1\bigr)
\]
possible pairs. Hence some fixed pair \((\alpha,a)\) is selected on a set \(I\) of at least
\[
|I|\ge \frac{q}{C_c}
\]
path positions.

Fix a vertex \(x\) at depth \(a\). We claim that all vertices \((x,i)\), \(i\in I\), lie in one \(\alpha\)-component. Indeed, every colour, including \(\alpha\), occurs at some depth at every path position. Fix a root-to-leaf path through \(x\). Between any two positions \(i,j\in I\), at each intermediate path position \(k\), choose an \(\alpha\)-coloured vertex on this root-to-leaf path. Consecutive chosen tree vertices are comparable and their path coordinates are consecutive, so they are adjacent in the strong product. At the endpoints choose \(x\). This gives an \(\alpha\)-coloured path from \((x,i)\) to \((x,j)\).

For every \(i\in I\), all \(q^{c-1}\) descendants of \(x\) at depth \(a+c-1\) have colour \(\alpha\) in layer \(i\), and all are adjacent to \((x,i)\). These sets are disjoint for different \(i\). Thus one component has at least
\[
|I|q^{c-1}
 \ge \frac{q^c}{C_c}
\]
vertices.

#### Matching upper bound within the restricted class

Partition the \(h+1=c(c-1)+1\) depth levels into \(c\) consecutive blocks: one block of \(c\) levels and \(c-1\) blocks of \(c-1\) levels. Assign a distinct colour to each block, independently of the path coordinate.

A block consisting of \(L\) consecutive levels has monochromatic \(H_q\)-components of order at most
\[
1+q+\cdots+q^{L-1}\le 2q^{L-1}.
\]
After taking the product with \(P_q\), each such component has order at most
\[
2q^L.
\]
Since \(L\le c\), the clustering is at most \(2q^c\). \(\square\)

---

## 6. Why this does not prove the conjecture

The level-homogeneous proof uses uniformity in an essential way. If the same colour occurs at depths \(d\) and \(e\ge d+c\), level-homogeneity ensures that all \(q^{e-d}\) descendants at depth \(e\) have that colour. In an arbitrary colouring, a repeat on a single root-to-leaf path gives only one lower vertex and need not produce a large component.

Similarly, Lemma 3.1 supplies a component of order \(q^{c-1}\) in every individual \(H_q\)-layer, but the selected components may:

- have different colours in different path layers;
- lie in pairwise incomparable rooted subtrees; and
- fail to be adjacent across consecutive path layers.

There is no valid averaging or automorphism argument that makes an arbitrary colouring level-homogeneous while preserving an upper bound on its component sizes.

Lemma 4.1 does force a hypothetical low-clustering colouring to have a monochromatic root fibre, but after deleting that sparse root colour one obtains many disjoint \((c-1)\)-coloured subproducts of height \(c(c-2)\). A single such subproduct admits a simple \((c-1)\)-colouring with clustering \(O(q^{c-1})\), so the required \(q^c\) bound must come from interactions through the upper \(c\) tree levels. I do not control those interactions for arbitrary branch-dependent colourings.

Accordingly, the unrestricted conjecture remains open here for \(c\ge4\); no counterexample and no improvement over the supplied paper’s general lower exponent is claimed.