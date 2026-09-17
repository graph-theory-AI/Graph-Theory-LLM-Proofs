```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any universal constant must be at most (2r-4)/(2r-1), and this constant is sharp for independent blow-ups of a natural family of circle-tangent segment graphs.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains unresolved; the sharp result concerns a restricted family, and no novelty claim is made."
}
```

## 1. Result obtained

Write
\[
a_s(G)=\max\{|X|:G[X]\text{ is }K_s\text{-free}\}.
\]
The question is whether, for every fixed \(r\ge4\),
\[
\inf_{\substack{G\ne\varnothing\\G\text{ a }K_r\text{-free segment graph}}}
\frac{a_{r-1}(G)}{|V(G)|}>0.
\]

I do not establish this positivity. The partial result below gives an explicit restriction on the possible constant and a sharp linear theorem for a geometric subclass.

Set \(q=r-1\). For \(N\ge2q\), let
\[
H_{N,q}=C_N^{\,q-1};
\]
its vertices are \(\mathbb Z/N\mathbb Z\), and two vertices are adjacent when their cyclic distance is at most \(q-1\).

An **independent blow-up** replaces each vertex \(i\) by an independent set \(V_i\), making \(V_i,V_j\) complete to each other exactly when \(ij\) is an edge of the original graph.

### Theorem
Let \(r\ge4\), \(q=r-1\), and \(N\ge2q\).

1. Every independent blow-up \(G\) of \(H_{N,q}\) is a \(K_r\)-free segment graph.
2. Every such \(G\) satisfies
   \[
   a_{r-1}(G)\ge
   \frac{2r-4}{2r-1}|V(G)|.
   \tag{1}
   \]
3. The constant in (1) is best possible over this subclass. Specifically, the uniform \(t\)-fold independent blow-up of \(H_{2r-1,r-1}\) has
   \[
   |V(G)|=(2r-1)t,\qquad
   a_{r-1}(G)=(2r-4)t.
   \tag{2}
   \]

Consequently, any constant valid in the original conjecture must satisfy
\[
\boxed{c_r\le \frac{2r-4}{2r-1}.}
\]

For \(r=4\), this gives explicit \(K_4\)-free segment graphs on \(7t\) vertices whose largest induced triangle-free subgraph has exactly \(4t\) vertices.

The proof is self-contained.

---

## 2. Explicit segment representations

Put
\[
\theta_i=\frac{2\pi i}{N},\qquad
p_i=(\cos\theta_i,\sin\theta_i),\qquad
u_i=(-\sin\theta_i,\cos\theta_i).
\]
Consider the segment
\[
S_i=\{p_i+t u_i:-L\le t\le L\}.
\]
Thus \(S_i\) is tangent to the unit circle at its midpoint \(p_i\).

If the smaller angular separation of \(p_i,p_j\) is \(\phi\in(0,\pi)\), their supporting tangent lines intersect at distance
\[
\tan(\phi/2)
\]
from each tangency point. Indeed, after rotating so that \(p_i=(1,0)\), the other tangent line has equation
\[
x\cos\phi+y\sin\phi=1.
\]
Its intersection with \(x=1\) has
\[
y=\frac{1-\cos\phi}{\sin\phi}=\tan(\phi/2).
\]
Antipodal tangent lines are parallel.

For \(N>2q\), choose
\[
\tan\frac{\pi(q-1)}{N}
<L<
\tan\frac{\pi q}{N}.
\tag{3}
\]
Then \(S_i,S_j\) intersect exactly when their cyclic distance is at most \(q-1\). Thus their intersection graph is \(H_{N,q}\).

For \(N=2q\), choose any finite
\[
L>\tan\frac{\pi(q-1)}{N}.
\]
Every non-antipodal pair intersects, while antipodal pairs have parallel supporting lines. This again represents \(H_{N,q}\).

All the intersections corresponding to edges are transverse and lie in the relative interiors of both segments.

### Independent blow-ups preserve these representations

Here the proper-crossing observation from the previous attempt can be verified directly.

For each \(i\), replace \(S_i\) by any prescribed number of sufficiently close, distinct parallel translates.

- Translates belonging to the same \(i\) are pairwise disjoint.
- Every original edge is a proper crossing, so sufficiently small translations preserve it.
- Every original nonedge consists of two disjoint compact segments and hence has positive distance. Sufficiently small translations preserve that nonedge.

There are only finitely many original pairs, so one common perturbation tolerance works for all of them. This realizes every finite independent blow-up exactly.

No assertion that *every* segment graph admits a proper-crossing representation is being used.

---

## 3. Cliques in the powers of cycles

We next determine the relevant clique-free subsets exactly.

### Lemma 1
For \(N\ge2q+1\), the clique number of \(H_{N,q}\) is \(q\), and its \(q\)-cliques are precisely the sets of \(q\) cyclically consecutive vertices.

#### Proof

We use the following elementary fact about addition in \(\mathbb Z/N\mathbb Z\). For any nonempty \(T\) and any integer \(\ell\ge1\),
\[
\left|T+\{0,1,\ldots,\ell-1\}\right|
\ge \min\{N,\ |T|+\ell-1\}.
\tag{4}
\]
To see this, repeatedly add a one-step cyclic translate. Until the set becomes the whole cycle, its size increases by at least one.

Moreover, if \(T\) is not a cyclic interval and \(\ell\ge2\), then
\[
\left|T+\{0,1,\ldots,\ell-1\}\right|
\ge \min\{N,\ |T|+\ell\}.
\tag{5}
\]
Indeed, \(T\) then has at least two cyclic components, so the first enlargement increases its size by at least two.

Now let \(T\) be a clique of \(H_{N,q}\). Put
\[
J=\{q,q+1,\ldots,N-q\},
\qquad
\ell=|J|=N-2q+1.
\]
These are exactly the forbidden differences between vertices of a clique. Hence
\[
T\cap(T+J)=\varnothing.
\tag{6}
\]
Applying (4), and observing that \(T+J\) cannot be the whole cycle, gives
\[
N\ge |T|+|T+J|
\ge 2|T|+\ell-1.
\]
Since \(\ell=N-2q+1\), we obtain \(|T|\le q\).

Suppose now that \(|T|=q\). If \(T\) were not a cyclic interval, (5) would give
\[
|T+J|\ge q+\ell=N-q+1,
\]
contradicting (6). Thus every \(q\)-clique is cyclically consecutive. Conversely, any \(q\) consecutive vertices form a clique. ∎

### Lemma 2
For \(N\ge2q+1\),
\[
a_q(H_{N,q})=N-\left\lceil\frac Nq\right\rceil.
\tag{7}
\]
For \(N=2q\),
\[
a_q(H_{2q,q})=2q-2.
\tag{8}
\]

#### Proof

First suppose \(N\ge2q+1\). By Lemma 1, a set \(X\) is \(K_q\)-free exactly when its complement \(Z\) meets every cyclic interval of \(q\) consecutive vertices.

If \(z=|Z|\), the cyclic distances between consecutive vertices of \(Z\) must all be at most \(q\). Their sum is \(N\), so
\[
N\le qz.
\]
Thus \(z\ge\lceil N/q\rceil\).

Conversely, let \(z=\lceil N/q\rceil\). Place \(z\) vertices around the cycle with successive cyclic distances
\[
q,q,\ldots,q,\ N-(z-1)q.
\]
Every distance lies between \(1\) and \(q\), so this set meets every \(q\)-vertex cyclic interval. This proves (7).

For \(N=2q\), the graph is a complete graph with a perfect matching removed. Its \(q\)-cliques choose one vertex from each of the \(q\) opposite pairs. Therefore a subset is \(K_q\)-free exactly when it omits both vertices of at least one opposite pair. The maximum size is \(2q-2\). ∎

In particular, every \(H_{N,q}\), and therefore every independent blow-up of it, is \(K_{q+1}=K_r\)-free.

---

## 4. The weighted bound and arbitrary blow-ups

The independent blow-ups require a weighted, rather than merely an unweighted, statement.

Let \(w_i\ge0\) be arbitrary vertex weights and write
\[
W=\sum_i w_i.
\]
Choose a maximum \(K_q\)-free set \(X\) of \(H_{N,q}\). Every cyclic shift \(X+j\) is also \(K_q\)-free. Averaging over the \(N\) shifts,
\[
\frac1N\sum_{j\in\mathbb Z/N\mathbb Z}
\sum_{i\in X+j}w_i
=
\frac{|X|}{N}W.
\]
Consequently, some \(K_q\)-free set has weight at least
\[
\rho_{N,q}W,
\]
where
\[
\rho_{N,q}=
\begin{cases}
1-\dfrac1q,&N=2q,\\[6pt]
1-\dfrac{\lceil N/q\rceil}{N},&N\ge2q+1.
\end{cases}
\tag{9}
\]

We claim that
\[
\rho_{N,q}\ge 1-\frac3{2q+1}.
\tag{10}
\]
The case \(N=2q\) is immediate. Otherwise set \(k=\lceil N/q\rceil\ge3\). Then
\[
\frac{\lceil N/q\rceil}{N}
\le
\frac{k}{(k-1)q+1}
\le
\frac3{2q+1}.
\]
The last inequality is equivalent to
\[
(k-3)(q-1)\ge0.
\]
Equality in (10) occurs at \(N=2q+1\).

Now consider an independent blow-up with \(|V_i|=w_i\), where the weights are nonnegative integers. A selected vertex set is \(K_q\)-free if and only if the set of fibers that it meets is \(K_q\)-free in the base graph. Therefore
\[
a_q(G)=
\max_{\substack{X\subseteq V(H_{N,q})\\H_{N,q}[X]\text{ is }K_q\text{-free}}}
\sum_{i\in X}w_i.
\tag{11}
\]
Equations (9)–(11) prove
\[
a_q(G)\ge
\frac{2q-2}{2q+1}|V(G)|,
\]
which is (1).

For a uniform \(t\)-fold blow-up, (11) also gives the exact equality
\[
a_q(G)=t\,a_q(H_{N,q}).
\]
Taking \(N=2q+1\) and using (7) proves (2).

---

## 5. The explicit obstruction to a larger constant

At \(N=2q+1\), the only nonedges of \(H_{N,q}\) have cyclic difference \(\pm q\). Since
\[
\gcd(q,2q+1)=1,
\]
these nonedges form one cycle. Hence
\[
H_{2q+1,q}\cong \overline{C_{2q+1}}.
\]

Thus the obstruction can be stated particularly simply:

> Uniform independent blow-ups of \(\overline{C_{2r-1}}\) are \(K_r\)-free segment graphs and have \(K_{r-1}\)-free induced-subgraph ratio exactly
> \[
> \frac{2r-4}{2r-1}.
> \]

The blow-up verification is important: it makes this an asymptotic obstruction, not merely a small exceptional graph.

For \(r=4\), one may take seven segments tangent to the unit circle at equally spaced points, each with half-length \(L=2\). Their graph is \(C_7^2\cong\overline{C_7}\). Its triangles are exactly the cyclic triples of consecutive vertices, and a largest triangle-free subset has four vertices. Parallel replication gives the asserted examples on \(7t\) vertices.

---

## 6. A somewhat broader geometric special case

The regular spacing is not essential for a linear conclusion.

Consider \(N\) distinct equal-length segments tangent to a common circle, each centered at its tangency point. Suppose their intersection graph \(H\) is \(K_{q+1}\)-free.

After rescaling, let the circle have radius one and the common half-length be \(L\). Put
\[
\delta=2\arctan L<\pi.
\]
Two segments intersect exactly when the smaller angular separation of their tangency points is at most \(\delta\).

Order the tangency points cyclically. If two segments intersect, all tangency points on the shorter arc between them lie in an arc of length at most \(\delta\). The corresponding segments are pairwise intersecting. Since \(H\) is \(K_{q+1}\)-free, this arc contains at most \(q\) tangency points.

Consequently, when \(N\ge2q\),
\[
H\subseteq H_{N,q}
\]
in this cyclic ordering. The weighted argument above therefore applies unchanged: every independent blow-up \(G\) of \(H\) satisfies
\[
a_q(G)\ge \frac{2q-2}{2q+1}|V(G)|.
\tag{12}
\]

If \(N<2q\), retaining the \(q-1\) heaviest fibers—or all fibers if there are fewer—gives instead
\[
a_q(G)\ge \frac{q-1}{2q-1}|V(G)|.
\tag{13}
\]
Thus all independent blow-ups of these \(K_r\)-free tangent families satisfy the conjectured linear conclusion, with the uniform bound
\[
\boxed{
a_{r-1}(G)\ge \frac{r-2}{2r-3}|V(G)|.
}
\]
The sharper bound (12) holds whenever the base family has at least \(2r-2\) segments.

Endpoint intersections cause no difficulty here: a sufficiently small common lengthening makes them proper while preserving every nonedge. The blow-up construction then applies.

This subclass allows both the number of directions and the balanced biclique size to grow.

---

## 7. What remains missing

The decisive property above is the circular ordering: an intersecting pair forces all intervening tangency points on a suitable arc to correspond to a clique. This bounds every edge’s cyclic span by \(r-2\), enabling the averaging argument.

Arbitrary segment representations have no such implication. Segments whose directions or locations lie “between” those of an intersecting pair need not intersect one another. Thus there is no justified extension of the cyclic-order argument to general segment graphs.

The partial result supplies:

- an explicit asymptotic upper bound on any proposed universal constant;
- an exact weighted solution for independent blow-ups of the specified cycle powers;
- a linear geometric special case beyond regular spacing.

It does **not** rule out a sequence of \(K_r\)-free segment graphs with
\[
a_{r-1}(G)/|V(G)|\longrightarrow0,
\]
nor does it establish a positive universal lower bound.