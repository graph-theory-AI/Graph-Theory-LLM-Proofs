```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The entire class of n^ε-long subdivisions has 2-ply ball representations in dimension O(1+1/ε), and the order of this dimension bound is optimal.",
  "would_publish": false,
  "caveats": "This handles a subdivision family in the explicit thin-ball model, not the full tame-convex conjecture; novelty is not asserted."
}
```

# A quantitative representation theorem for polynomial subdivisions

I do not resolve the conjecture. I obtain a uniform, prescribed-length strengthening of the subdivision construction suggested in the previous attempt.

The distinction matters: proving that **some sufficiently long subdivision** of every graph has a geometric representation does not handle a candidate class whose subdivision lengths have already been prescribed. The result below does handle such classes, with polynomial subdivision lengths and a dimension independent of the underlying graph.

The supplied excerpt does not reproduce the definition of \(\sqsubseteq_s\). Accordingly, I state the geometric conclusion explicitly: the representations are exact intersection representations by positive-radius Euclidean balls, and their ply is two. I do not replace the source’s tameness condition by a local-degree condition.

## 1. Statement

For a finite simple graph \(H\), let \(S(H,\mathbf m)\) denote the graph obtained by replacing each edge \(e\) with a path having \(m_e\) internal vertices.

Fix \(\epsilon>0\), and let
\[
\mathcal S_\epsilon
 =
 \left\{
 S(H,\mathbf m):
 n=|V(H)|,\quad m_e\ge \lceil n^\epsilon\rceil
 \text{ for every }e\in E(H)
 \right\}.
\]

A family of closed balls is **2-ply** if no point belongs to more than two balls.

### Theorem

For every \(\epsilon>0\):

1. Every graph in \(\mathcal S_\epsilon\) has an exact 2-ply ball representation in \(\mathbb R^{D_\epsilon}\), where
   \[
   D_\epsilon=4+\left\lceil\frac{32768}{\epsilon}\right\rceil
   \]
   is one possible, deliberately unoptimized choice.

2. Every \(G\in\mathcal S_\epsilon\) satisfies
   \[
   \operatorname{col}_r(G)\le
   \max\{3,r^{1/\epsilon}\}
   \qquad(r\ge1).
   \]
   Thus a uniform polynomial bound is, for example,
   \[
   \operatorname{col}_r(G)\le 3+r^{\lceil1/\epsilon\rceil}.
   \]

3. Suppose all graphs obtained from \(K_n\) by putting exactly
   \(\lceil n^\epsilon\rceil\) internal vertices on every edge admit ball representations in a fixed dimension \(d\). Then
   \[
   \epsilon d\ge1.
   \]

The first two conclusions also hold for the induced-subgraph closure of \(\mathcal S_\epsilon\).

Consequently, the worst-case ball dimension of this subdivision family is
\[
\Theta(1+1/\epsilon),
\]
up to universal constant factors.

---

## 2. Strong coloring numbers of subdivisions

Recall that \(u\) is strongly \(r\)-reachable from \(v\) in an order \(\prec\) if \(u\preceq v\) and there is a \(v\)-\(u\) path of length at most \(r\) whose internal vertices all follow \(v\).

### Lemma 1

Let \(H\) have \(n\) vertices, and suppose every replacement path has at least \(L\) edges. There is one vertex order witnessing, simultaneously for all \(r\),
\[
\operatorname{col}_r(S(H,\mathbf m))
\le
\begin{cases}
3,&r<L,\\
\max\{3,n\},&r\ge L.
\end{cases}
\]

#### Proof

Order all branch vertices first. Orient each replacement path arbitrarily, and order its internal vertices from its initial endpoint toward its terminal endpoint. Combine these path orders in any way preserving the order on each path.

Let \(v\) be an internal vertex. A qualifying path from \(v\) cannot have a branch vertex as an internal vertex, because every branch vertex precedes \(v\). It therefore stays on \(v\)’s replacement path until it ends.

In the backward direction, it cannot pass the immediately preceding vertex of that path, since that vertex precedes \(v\). In the forward direction, all internal vertices follow \(v\), and the only possible earlier endpoint is the terminal branch vertex. Thus at most two vertices other than \(v\) are strongly reachable.

If \(v\) is a branch vertex, every vertex preceding \(v\) is also a branch vertex. Distinct branch vertices are at distance at least \(L\). Hence \(v\) strongly reaches only itself when \(r<L\), and at most all \(n\) branch vertices otherwise. ∎

For \(G\in\mathcal S_\epsilon\), take
\[
L=1+\min_e m_e\ge 1+n^\epsilon.
\]
If \(r\ge L\), then \(n\le r^{1/\epsilon}\). This proves part 2 of the theorem. Edgeless graphs are immediate.

There is also an exact lower bound that will be useful later.

### Lemma 2

Let \(G\) be obtained by replacing every edge of \(K_n\), \(n\ge3\), with a path of exactly \(L\) edges. Then
\[
\operatorname{col}_L(G)=n.
\]

#### Proof

The upper bound follows from Lemma 1.

For the lower bound, consider any order and let \(v\) be the last branch vertex. For each other branch vertex \(u\), follow the replacement path from \(v\) to \(u\), and stop at its first vertex preceding \(v\). Such a vertex exists because \(u\prec v\). It is strongly \(L\)-reachable from \(v\).

The \(n-1\) vertices obtained this way are distinct, since the replacement paths incident with \(v\) are internally disjoint and have distinct other endpoints. Including \(v\), its strong reachability set has size at least \(n\). ∎

In particular, the exponent \(1/\epsilon\) in part 2 cannot be decreased uniformly for this family.

---

## 3. Quantitatively separated straight-line drawings

The geometric construction starts with points whose small affine spans stay quantitatively separated.

### Lemma 3

For every \(n\ge2\) and \(d\ge3\), there exist points
\[
p_1,\ldots,p_n\in \overline B(0,1)\subseteq\mathbb R^d
\]
such that, with
\[
\delta=(2dn^4)^{-1/(d-2)},
\]
we have
\[
\operatorname{dist}\!\left(
p_i,\operatorname{aff}\{p_j:j\in J\}
\right)\ge\delta
\tag{1}
\]
whenever \(i\notin J\) and \(1\le |J|\le3\).

#### Proof

Choose the points independently and uniformly from the unit ball.

For any affine subspace \(A\) of dimension \(q\le2\), a volume estimate gives
\[
\Pr\bigl(\operatorname{dist}(p_i,A)<\delta\bigr)
\le
\frac{\kappa_q\kappa_{d-q}}{\kappa_d}\delta^{d-q}
\le d\delta^{d-2},
\tag{2}
\]
where \(\kappa_j\) denotes the volume of the \(j\)-dimensional unit ball.

For completeness, the first inequality bounds the relevant tube by a product of a \(q\)-dimensional unit ball and a \((d-q)\)-dimensional ball of radius \(\delta\). For \(q=2\), the volume ratio is \(d/2\); for \(q=1\), it is at most \(d\); and for \(q=0\), it is one.

Condition on the points indexed by \(J\), and apply (2) to their affine span. There are at most \(n^4\) choices of \((i,J)\). The union bound therefore bounds the probability of any failure by
\[
n^4d\delta^{d-2}=\frac12.
\]
Thus a configuration satisfying (1) exists. ∎

We next convert this configuration into balls.

### Lemma 4

For every \(d\ge3\), every \(n\)-vertex graph \(H\), and every choice
\[
m_e\ge
64(2d)^{2/(d-2)}\,n^{8/(d-2)},
\tag{3}
\]
the graph \(S(H,\mathbf m)\) has a 2-ply ball representation in \(\mathbb R^d\).

In particular, for \(d\ge4\), the simpler sufficient condition
\[
m_e\ge512\,n^{8/(d-2)}
\tag{4}
\]
holds.

#### Proof

Take the points from Lemma 3 and put a branch ball of radius
\[
R=\delta/4
\]
at each \(p_i\).

For an edge \(ij\), truncate the segment \(p_ip_j\) at distance \(R\) from each endpoint; denote the resulting segment by \(T_{ij}\).

We first verify the necessary clearances.

**Nonincident edges.** Suppose \(ij\) and \(k\ell\) have disjoint endpoints. For
\[
x\in[p_i,p_j],\qquad
y=(1-t)p_k+tp_\ell,
\]
condition (1), applied to the planes through \(p_i,p_j,p_k\) and through \(p_i,p_j,p_\ell\), gives
\[
\|x-y\|\ge t\delta,\qquad
\|x-y\|\ge(1-t)\delta.
\]
Consequently,
\[
\operatorname{dist}([p_i,p_j],[p_k,p_\ell])\ge\delta/2.
\]

**Incident edges.** If \(ij\) and \(ik\) are distinct, their angle \(\theta\) satisfies
\[
\sin\theta
=
\frac{\operatorname{dist}(p_j,\operatorname{aff}\{p_i,p_k\})}
{\|p_j-p_i\|}
\ge\delta/2.
\]
Every point of \(T_{ij}\) is at distance at least \(R\) from \(p_i\). Hence
\[
\operatorname{dist}(T_{ij},T_{ik})
\ge R\sin\theta
\ge\delta^2/8.
\]

Thus any two distinct truncated edge segments have distance at least
\[
\eta=\delta^2/8.
\tag{5}
\]
Also, a nonincident vertex has distance at least \(\delta\) from an edge segment, and distinct branch centers have distance at least \(\delta\).

Now consider an edge \(e=ij\), with
\[
D_e=\|p_i-p_j\|.
\]
Give all its internal vertices balls of radius
\[
a_e=\frac{2(D_e-2R)}{3m_e-1}.
\tag{6}
\]
Place their centers consecutively along \(p_ip_j\), beginning at distance \(R+a_e/2\) from \(p_i\), with spacing \(3a_e/2\).

Formula (6) makes the last center lie at distance \(R+a_e/2\) from \(p_j\). It also ensures:

- consecutive internal balls intersect;
- nonconsecutive internal balls are disjoint;
- only the first internal ball meets the initial branch ball;
- only the last internal ball meets the terminal branch ball.

Since \(D_e\le2\), condition (3), equivalently \(m_e\ge64\delta^{-2}\), gives
\[
a_e\le\frac4{3m_e-1}<\frac{\delta^2}{32}.
\]
Therefore balls on distinct edge chains are disjoint by (5). No internal ball meets a nonincident branch ball. Branch balls are pairwise disjoint.

This checks every possible pair of representing balls, so the intersection graph is exactly \(S(H,\mathbf m)\). A proper subdivision is triangle-free; consequently its exact intersection representation cannot have a point common to three balls. The representation is 2-ply.

Finally,
\[
64(2d)^{2/(d-2)}\le512
\qquad(d\ge4),
\]
which proves (4). ∎

Already, Lemma 4 proves a useful prescribed-length statement: in dimension approximately \(8/\epsilon\), every subdivision with at least \(C_\epsilon n^\epsilon\) internal vertices per edge has a 2-ply ball model. The next step removes the leading constant without losing the order of the dimension bound.

---

## 4. Short subdivisions when the number of branch vertices is small

### Lemma 5

If
\[
d\ge2048\log n,
\]
then every proper subdivision of every \(n\)-vertex graph has a 2-ply ball representation in \(\mathbb R^d\). Here “proper” means at least one internal vertex on every edge.

#### Proof

There exist unit vectors \(p_1,\ldots,p_n\in\mathbb R^d\) satisfying
\[
|\langle p_i,p_j\rangle|\le1/16
\qquad(i\ne j).
\tag{7}
\]

Indeed, choose each vector independently and uniformly from
\(\{-1/\sqrt d,1/\sqrt d\}^d\). The exponential-moment estimate for independent signs gives
\[
\Pr\bigl(|\langle p_i,p_j\rangle|>1/16\bigr)
\le2e^{-d/512}.
\]
A union bound bounds the probability of a bad pair by
\[
n^2e^{-d/512}\le n^{-2}<1.
\]

Use branch balls of radius \(R=2/3\), and use exactly the chain construction (6).

From (7),
\[
\sqrt{15/8}\le\|p_i-p_j\|\le\sqrt{17/8}<3/2.
\]
Thus branch balls are disjoint, and every internal-ball radius satisfies
\[
0<a_e\le D_e-\frac43<\frac16.
\tag{8}
\]

We verify that different chains stay disjoint.

For incident edges, the cosine of their angle lies between zero and
\[
\frac{1+3/16}{2-2/16}=\frac{19}{30}.
\]
Their sine is therefore greater than \(1/2\). The truncated segments have distance greater than
\[
R/2=1/3,
\]
whereas the sum of their internal-ball radii is less than \(1/3\).

For nonincident edges, the Gram matrix of their four endpoint vectors has minimum eigenvalue at least \(1-3/16=13/16\). A difference between points on the two segments has coefficient vector
\[
(1-s,s,-(1-t),-t),
\]
whose squared norm is at least one. The segment distance is therefore at least \(\sqrt{13/16}>1/3\).

Similarly, using three endpoint vectors, the distance from a nonincident vertex to an edge segment is at least
\[
\sqrt{(1-2/16)(3/2)}=\sqrt{21/16}>1.
\]
This exceeds \(R+a_e<5/6\).

All remaining intersection checks are exactly those in Lemma 4. Hence the representation is exact and 2-ply. ∎

### Completing the dimension bound

Set
\[
D=D_\epsilon=4+\left\lceil32768/\epsilon\right\rceil
\]
and
\[
N_\epsilon=512^{2/\epsilon}.
\]

If \(n\ge N_\epsilon\), then
\[
n^\epsilon\ge512\,n^{\epsilon/2}.
\]
Also \(8/(D-2)\le\epsilon/2\). Thus
\[
m_e\ge n^\epsilon\ge512\,n^{8/(D-2)},
\]
and Lemma 4 applies.

If \(2\le n<N_\epsilon\), then
\[
2048\log n
<
\frac{4096\log512}{\epsilon}
<
\frac{32768}{\epsilon}
\le D.
\]
Lemma 5 applies. The case \(n=1\) is immediate.

This proves part 1 of the theorem. Deleting balls proves the representation statement for the induced-subgraph closure. Restricting an order proves the corresponding coloring-number statement.

---

## 5. The dimension dependence is necessary

The lower bound follows from a direct packing argument.

### Lemma 6

If \(G\) is the intersection graph of a \(k\)-ply family of positive-radius balls in \(\mathbb R^d\), then
\[
\operatorname{col}_r(G)\le k(2r+1)^d
\qquad(r\ge1).
\tag{9}
\]

#### Proof

Order the balls by nonincreasing radius.

Fix a vertex \(v\), represented by \(B(x,\rho)\). Let \(u\ne v\) be strongly \(r\)-reachable from \(v\). Along a qualifying path, every internal ball has radius at most \(\rho\), whereas \(u\)’s ball has radius at least \(\rho\).

The last internal ball on such a path lies inside
\[
B(x,(2r-1)\rho).
\]
Therefore \(u\)’s ball intersects that ball.

Any ball of radius at least \(\rho\) intersecting \(B(x,(2r-1)\rho)\) contains a radius-\(\rho\) ball whose center lies in \(B(x,2r\rho)\). To see this, move from its center toward \(x\), stopping after a distance equal to its radius minus \(\rho\), or at \(x\), whichever occurs first.

Choose one such radius-\(\rho\) subball for every strongly reachable vertex, including \(v\). All these subballs lie in
\[
B(x,(2r+1)\rho).
\]
Their ply is at most \(k\), because each lies in its original representing ball. Volume comparison yields
\[
|\operatorname{SReach}_r(v)|\,\kappa_d\rho^d
\le
k\kappa_d((2r+1)\rho)^d.
\]
This proves (9). ∎

Now let \(G_n\) be the graph obtained from \(K_n\) by giving every edge
\[
m_n=\lceil n^\epsilon\rceil
\]
internal vertices, and put \(L_n=m_n+1\). Lemma 2 gives
\[
\operatorname{col}_{L_n}(G_n)=n.
\]

Every \(G_n\) is triangle-free. Thus **any** exact ball representation of \(G_n\) is automatically 2-ply. If all these graphs have representations in \(\mathbb R^d\), Lemma 6 implies
\[
n\le2(2L_n+1)^d\le2\cdot7^d n^{\epsilon d}.
\]
Letting \(n\to\infty\) forces
\[
\epsilon d\ge1.
\]

If zero-radius balls are allowed, they can first be inflated slightly without changing this finite triangle-free intersection graph: every nonedge has a positive separation gap. Thus allowing degenerate balls does not evade the lower bound.

---

## 6. What this says—and does not say—about the conjecture

The open question must be interpreted uniformly over a graph class; otherwise the premise is vacuous because \(\operatorname{col}_r(G)\le |V(G)|\) for each individual finite graph.

For that uniform interpretation, the result above establishes the following substantial positive case:

> Arbitrary underlying graphs, with arbitrary prescribed subdivision lengths at least \(n^\epsilon\), already have fixed-dimensional 2-ply ball representations. The dimension depends only on \(\epsilon\), not on the underlying graph or its order.

These models use no uncontrolled aspect ratios. Balls also satisfy the strong elementary comparison property that, for \(a\le b\), every point of a radius-\(b\) ball lies in a translate of a radius-\(a\) ball contained in it. Thus the construction supplies genuine geometric structure, not merely a favorable vertex order.

In the thin-ball specialization of the intended tame framework, this rules out the entire polynomial-subdivision family as a source of the desired separation. It strengthens the previous attempt’s existential routing result and corrects its coarse coloring-number estimate.

However:

- the dimension lower bound is only a ball-representation lower bound;
- it is finite for every fixed \(\epsilon\);
- no obstruction to arbitrary tame convex representations has been established;
- no representation theorem for all classes with polynomial strong coloring numbers has been established.

The missing ingredient for the original conjecture remains an obstruction to **all fixed-dimensional tame convex representations** that is not already reflected by polynomial strong coloring numbers. The argument above does not provide one.