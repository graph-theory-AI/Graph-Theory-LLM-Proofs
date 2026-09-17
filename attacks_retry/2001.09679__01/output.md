```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A verified stretching construction proves the desired reduction for almost-monotone normalized separator profiles and yields a quantitative monotonicity inequality for b_epsilon, but does not settle arbitrary one-sided profiles.",
  "would_publish": false,
  "caveats": "The general oscillatory-profile case remains unresolved; novelty of the partial results has not been checked."
}
```

# 1. Results obtained

Write
\[
\alpha=1-\varepsilon.
\]
The question concerns \(\alpha>1/2\).

For a graph \(G\), let \(\operatorname{sep}_\theta(G)\) be the minimum size of a vertex set whose deletion leaves components of order at most \(\theta |V(G)|\). Put
\[
\operatorname{sep}(G)=\operatorname{sep}_{2/3}(G),
\qquad
s_{\mathcal C}(n)=
\max_{\substack{G\in\mathcal C\\|V(G)|\le n}}\operatorname{sep}(G).
\]
I use the monotone, “at most \(n\)” convention here. The construction below also supplies a witness at every sufficiently large **exact** order, so this convention does not affect the conclusion.

I work with actual expansion-function inequalities, rather than relying on the previous attempt’s identification of \(b_\varepsilon\) with a limsup expansion exponent. In particular, the arguments below transfer universal \(\Omega\)-bounds, as required for a lower-expansion parameter.

## Theorem A: a profile-level sufficient condition

Let \(0<\alpha<1\). Suppose that \(\mathcal C\) is hereditary, that \(\nabla_{\mathcal C}(0)<\infty\), and that
\[
s_{\mathcal C}(n)\ge c n^\alpha
\]
for all sufficiently large \(n\). Suppose additionally that, for some constant \(A\),
\[
\frac{s_{\mathcal C}(p)}{p^\alpha}
\le
A\,\frac{s_{\mathcal C}(n)}{n^\alpha}
\qquad(1\le p\le n).
\tag{Q}
\]
Then there is a hereditary class \(\mathcal D\) satisfying
\[
s_{\mathcal D}(n)=\Theta(n^\alpha)
\tag{1}
\]
and, for every nonnegative integer \(r\),
\[
\nabla_{\mathcal D}(r)
\le
\max\{2,\nabla_{\mathcal C}(2r+1)\}.
\tag{2}
\]

Thus the conjectured reduction holds whenever the normalized separator profile \(s_{\mathcal C}(n)/n^\alpha\) is **almost nondecreasing**.

Condition (Q) includes:

* \(s_{\mathcal C}(n)=\Theta(n^\beta)\), for every \(\beta\ge\alpha\);
* \(s_{\mathcal C}(n)=\Theta(n^\beta L(n))\), where \(\beta\ge\alpha\) and \(L\) is positive and nondecreasing;
* more generally, profiles satisfying
  \[
  \liminf_{n\to\infty}\frac{s_{\mathcal C}(2n)}{s_{\mathcal C}(n)}>2^\alpha.
  \tag{3}
  \]

Consequently, restricting the one-sided parameter to classes satisfying (Q) gives exactly \(b_\varepsilon\), not a smaller parameter.

## Theorem B: quantitative stretching

Suppose
\[
0<\alpha<\beta<1,
\qquad
s_{\mathcal C}(n)=\Theta(n^\beta),
\]
and \(\mathcal C\) has finite expansion at every depth. Set
\[
q=\frac{\beta}{\alpha}-1>0.
\]
The class \(\mathcal D\) in Theorem A can be chosen so that:

1. if \(\nabla_{\mathcal C}(r)=O(r^p)\), then
   \[
   \nabla_{\mathcal D}(r)
   =
   O\!\left(r^{\,p/(1+2pq)}\right);
   \tag{4}
   \]
2. writing \(K(r)=\max\{2,\nabla_{\mathcal C}(r)\}\), there are constants \(a_0,a_1>0\) such that
   \[
   \nabla_{\mathcal D}
   \left(\left\lfloor a_0rK(r)^{2q}\right\rfloor\right)
   \le a_1K(r)
   \tag{5}
   \]
   for all sufficiently large integers \(r\).

The adaptive inequality (5), rather than just the polynomial upper bound (4), transfers universal lower-expansion exponents.

In the notation of the question, it gives
\[
\boxed{
b_\varepsilon
\le
\frac{(1-\varepsilon)b_\eta}
     {(1-\varepsilon)+2(\varepsilon-\eta)b_\eta}
}
\qquad
(0<\eta<\varepsilon<1/2).
\tag{6}
\]
Here the values \(b_\eta\) are finite, as in the setting of the source paper. More generally, the argument below establishes (6) whenever the right-hand parameter is finite.

This is stronger than the qualitative monotonicity
\[
b_\varepsilon\le b_\eta.
\]
It does **not**, however, compare \(b'_\varepsilon\) and \(b_\varepsilon\) for an arbitrary one-sided class.

# 2. Two separator lemmas

## Lemma 1: weighted separators

Suppose \(G\) has order \(m\), and every nonempty induced subgraph \(F\) satisfies
\[
\operatorname{sep}(F)
\le Kt\left(\frac{|V(F)|}{m}\right)^\alpha.
\tag{7}
\]
Let \(P\subseteq V(G)\), with \(|P|=p\), and let \(F\) be any spanning subgraph of \(G[P]\). For every nonnegative vertex weighting of \(F\), there is a weighted \(2/3\)-balanced separator of size at most
\[
C_\alpha Kt\left(\frac p m\right)^\alpha,
\qquad
C_\alpha=\frac1{1-(2/3)^\alpha}.
\tag{8}
\]

### Proof

Apply an unweighted balanced separator to \(F\). Deleting edges cannot increase the required separator size, so (7) applies.

If a remaining component has more than \(2/3\) of the original total weight, recurse in that component. There is at most one such component. At each step its number of vertices decreases by a factor at most \(2/3\).

The total number of deleted vertices is at most
\[
Kt\left(\frac p m\right)^\alpha
\sum_{j\ge0}(2/3)^{j\alpha},
\]
which is (8). All components discarded from the recursion already have at most \(2/3\) of the original total weight. ∎

## Lemma 2: a robust witness

If \(G\) has order \(m\) and \(\operatorname{sep}(G)=t\), then it contains an induced subgraph \(H\) such that
\[
\frac{2m}{3}<|V(H)|\le m,
\qquad
\operatorname{sep}_{5/6}(H)\ge \frac t3.
\tag{9}
\]

If \(G\) also satisfies (7), then, putting
\[
h=|V(H)|,
\qquad
\tau=\operatorname{sep}_{5/6}(H),
\]
we have
\[
t/3\le\tau\le Kt
\tag{10}
\]
and
\[
\operatorname{sep}(F)
\le 3K\tau\left(\frac{|V(F)|}{h}\right)^\alpha
\tag{11}
\]
for every nonempty induced \(F\subseteq H\).

### Proof

Starting with \(G\), repeatedly take a \(5/6\)-balanced separator and continue inside the unique component, if any, having more than \(2m/3\) vertices.

If each of the first three separators had size less than \(t/3\), their union would have size less than \(t\). After three rounds, the component followed by the recursion would have order at most
\[
(5/6)^3m<2m/3.
\]
The union would therefore be a \(2/3\)-balanced separator of \(G\), a contradiction.

Thus one of the induced graphs encountered before termination satisfies (9). It has more than \(2m/3\) vertices. Furthermore,
\[
\tau\le\operatorname{sep}(H)\le Kt,
\]
and, for \(F\subseteq H\),
\[
\operatorname{sep}(F)
\le Kt\left(\frac{|V(F)|}{m}\right)^\alpha
\le 3K\tau\left(\frac{|V(F)|}{h}\right)^\alpha.
\]
∎

The change from balance \(2/3\) to balance \(5/6\) is useful: it permits arbitrary-order padding without losing the lower separator bound.

# 3. The stretching construction

The following finite-graph construction is the main ingredient.

Suppose \(G\) has order \(m\), admits an orientation of maximum outdegree at most \(d\), and satisfies
\[
\tau=\operatorname{sep}_{5/6}(G)\ge c_0m^\alpha
\tag{12}
\]
and
\[
\operatorname{sep}(F)
\le K_0\tau
\left(\frac{|V(F)|}{m}\right)^\alpha
\tag{13}
\]
for every nonempty induced \(F\subseteq G\).

Set
\[
L=\left\lceil\frac{\tau^{1/\alpha}}m\right\rceil,
\qquad
N_0=4(d+1)mL.
\tag{14}
\]
Then
\[
N_0=\Theta(\tau^{1/\alpha}),
\tag{15}
\]
with constants depending only on \(\alpha,c_0,d\).

For **every** integer \(N\ge N_0\), construct a graph \(T=T(G,L,N)\) of order exactly \(N\), as follows.

* Replace each directed edge \(u\to v\) by a path with \(L\) new internal vertices.
* Choose integers \(W_u\), each equal to \(\lfloor N/m\rfloor\) or \(\lceil N/m\rceil\), with
  \[
  \sum_{u\in V(G)}W_u=N.
  \]
* At \(u\), attach a pendant path having
  \[
  W_u-1-Ld^+(u)
  \]
  new vertices.

The last quantity is nonnegative because \(N\ge N_0\).

For each original vertex \(u\), let \(B_u\) consist of \(u\), all internal vertices on paths directed out of \(u\), and its pendant path. These blocks partition \(V(T)\), and
\[
|B_u|=W_u.
\]

## 3.1. The lower separator bound

I claim that
\[
\operatorname{sep}(T)\ge\tau.
\tag{16}
\]

Suppose \(X\subseteq V(T)\) has size less than \(\tau\), and put
\[
Y=\{u:B_u\cap X\ne\varnothing\}.
\]
Then \(|Y|\le |X|<\tau\). By the definition of \(\tau\), some component \(C\) of \(G-Y\) has more than \(5m/6\) vertices.

All blocks \(B_u\), \(u\in C\), survive and belong to one component of \(T-X\). Writing \(W=\lfloor N/m\rfloor\), that component has more than
\[
\frac56mW
\]
vertices. Since \(W\ge4\) and \(N<m(W+1)\),
\[
\frac56mW
\ge
\frac23m(W+1)
>
\frac23N.
\]
Thus \(X\) is not balanced, proving (16).

## 3.2. Uniform upper bounds in induced subgraphs

There is a constant \(C\), depending only on \(\alpha,d,K_0\), such that every induced subgraph \(J\subseteq T\) satisfies
\[
\operatorname{sep}(J)\le C|V(J)|^\alpha.
\tag{17}
\]

Let \(k=|V(J)|\). If \(J\) has no component of order greater than \(2k/3\), there is nothing to prove. Otherwise let \(Q\) be its unique oversized component.

If \(Q\) contains at most one original vertex, it is a tree, so one vertex suffices.

Suppose \(Q\) contains \(p\ge2\) original vertices. Form a skeleton \(F\) on these vertices, retaining an edge precisely when its complete subdivided path lies in \(Q\). Connectivity of \(Q\) implies connectivity of \(F\). A spanning tree of \(F\) uses \(p-1\) complete edge-paths, so
\[
L(p-1)\le k,
\qquad
p\le\frac{2k}{L}.
\tag{18}
\]

Assign the vertices of \(Q\) to its original vertices:

* each original vertex is assigned to itself;
* the internal vertices of a complete directed edge-path are assigned to its tail;
* a partial path segment attached to one original vertex is assigned to that vertex.

These assignments define weights on \(F\). Lemma 1 gives a weighted balanced separator \(S\) of \(F\) satisfying
\[
|S|
\le C_\alpha K_0\tau\left(\frac p m\right)^\alpha.
\tag{19}
\]

Delete the original vertices in \(S\). For each complete path directed from a vertex of \(S\) to a vertex outside \(S\), also delete the internal vertex next to its head. This costs at most \(d|S|\) additional vertices.

After these deletions, every component containing an original vertex has at most \(2|Q|/3\) vertices: no surviving mass assigned to \(S\) can attach to such a component. Components containing no original vertex are paths. At most one of these paths can have more than \(2k/3\) vertices; if one does, one additional vertex splits it sufficiently.

Consequently,
\[
\operatorname{sep}(J)\le(d+1)|S|+1.
\]
Finally, by (14) and (18),
\[
\tau\left(\frac p m\right)^\alpha
\le
2^\alpha\tau\left(\frac{k}{Lm}\right)^\alpha
\le
2^\alpha k^\alpha.
\]
This proves (17). Notice that the bound is independent of the padding order \(N\).

## 3.3. A radius-sensitive expansion bound

For every integer \(r\ge0\),
\[
\nabla_T(r)
\le
\max\left\{
2,\
\min\left\{
\nabla_G\!\left(\left\lfloor\frac{2r}{L+1}\right\rfloor\right),
\sqrt{\frac{dm}{2}}
\right\}
\right\}.
\tag{20}
\]

To prove this, consider an \(r\)-shallow minor \(M\) of \(T\). Partition its branch sets into:

* \(Z\): those containing an original vertex of \(G\);
* \(R\): those containing no original vertex.

A branch set in \(R\) is an interval inside one subdivided edge-path or pendant path. Its degree in \(M\) is at most two.

Project a branch set in \(Z\) to the original vertices it contains. The projection is connected. Distances inside the branch set are at most \(2r\), whereas traversing an original edge uses \(L+1\) edges of \(T\). Hence the projection has radius at most
\[
\left\lfloor\frac{2r}{L+1}\right\rfloor.
\]
Different projections are disjoint, and every edge of \(M[Z]\) corresponds to an edge between their projections. Thus \(M[Z]\) is a shallow minor of \(G\) at the indicated depth.

There is also a size-only bound. Since \(G\) has at most \(dm\) edges, any simple minor of \(G\) with \(z\) vertices has density at most
\[
\min\left\{\frac{dm}{z},\frac{z-1}{2}\right\}
\le\sqrt{\frac{dm}{2}}.
\]
Lastly,
\[
|E(M)|\le |E(M[Z])|+2|R|.
\]
Taking densities proves (20).

In particular, if \(G\in\mathcal C\), then
\[
\nabla_T(r)\le\max\{2,\nabla_{\mathcal C}(2r+1)\}.
\tag{21}
\]

# 4. Proof of Theorem A

Because \(\mathcal C\) is hereditary and \(\nabla_{\mathcal C}(0)<\infty\), all its graphs admit orientations of maximum outdegree at most one fixed integer \(d\). For example, use a degeneracy orientation.

A useful elementary property is
\[
s_{\mathcal C}(n+1)\le s_{\mathcal C}(n)+1.
\tag{22}
\]
Indeed, if \(G\) has \(n+1\) vertices, delete a vertex \(v\), take a balanced separator of \(G-v\), and add \(v\) to that separator. The resulting components have order at most \(2n/3\), and hence at most \(2(n+1)/3\).

The integer-valued function \(s_{\mathcal C}\) is nondecreasing and unbounded. By (22), it therefore attains every sufficiently large integer value.

For each sufficiently large integer \(t\), choose \(n_t\) with
\[
s_{\mathcal C}(n_t)=t,
\]
and a witness \(G_t\in\mathcal C\), of order \(m_t\le n_t\), with
\[
\operatorname{sep}(G_t)=t.
\]
The lower hypothesis gives
\[
t\ge c n_t^\alpha\ge c m_t^\alpha.
\tag{23}
\]
For every induced \(F\subseteq G_t\), of order \(p\), condition (Q) gives
\[
\operatorname{sep}(F)
\le s_{\mathcal C}(p)
\le At\left(\frac p{n_t}\right)^\alpha
\le At\left(\frac p{m_t}\right)^\alpha.
\tag{24}
\]

Apply Lemma 2 to obtain an induced graph \(H_t\) with
\[
\tau_t:=\operatorname{sep}_{5/6}(H_t)\in[t/3,At].
\tag{25}
\]
The graphs \(H_t\) satisfy (12)–(13) with uniform constants. Apply the stretching construction to each \(H_t\), including every padding order
\[
N\ge N_{0,t}.
\]
By (15) and (25),
\[
N_{0,t}\le C_0t^{1/\alpha}
\tag{26}
\]
for a fixed constant \(C_0\).

Let \(\mathcal D\) be the hereditary closure of all the resulting stretched graphs.

The uniform upper bound (17) proves
\[
s_{\mathcal D}(n)=O(n^\alpha).
\]

For the lower bound at an arbitrary sufficiently large **exact** order \(N\), choose
\[
t=\left\lfloor(N/C_0)^\alpha\right\rfloor.
\]
Then \(N_{0,t}\le N\), so the construction includes a stretched graph of order exactly \(N\). Its separator has order at least
\[
\tau_t\ge t/3=\Omega(N^\alpha).
\]
This proves (1).

Finally, (21) passes to the hereditary closure and gives (2). ∎

## Why the listed profile conditions suffice

For an exact power profile with \(\beta\ge\alpha\),
\[
\frac{s_{\mathcal C}(p)}{p^\alpha}
=O(p^{\beta-\alpha})
=O(n^{\beta-\alpha})
=O\!\left(\frac{s_{\mathcal C}(n)}{n^\alpha}\right).
\]
The same argument applies with an additional positive nondecreasing factor \(L\).

For (3), choose \(\gamma>\alpha\) so that eventually
\[
s_{\mathcal C}(2n)\ge2^\gamma s_{\mathcal C}(n).
\]
Iterating this inequality over dyadic scales and using monotonicity yields
\[
s_{\mathcal C}(p)
\le C s_{\mathcal C}(n)(p/n)^\gamma
\le C s_{\mathcal C}(n)(p/n)^\alpha.
\]
The finitely many small orders are absorbed into the constant.

# 5. Proof of Theorem B and the inequality for \(b_\varepsilon\)

Suppose now that
\[
s_{\mathcal C}(n)=\Theta(n^\beta),
\qquad \alpha<\beta.
\]
In the proof of Theorem A, the witnesses before and after applying Lemma 2 satisfy
\[
\tau=\Theta(m^\beta).
\]
Consequently their subdivision lengths satisfy
\[
L\ge a m^q,
\qquad
q=\frac{\beta}{\alpha}-1,
\tag{27}
\]
for some fixed \(a>0\).

## 5.1. Polynomial upper bounds

If \(\nabla_{\mathcal C}(r)=O(r^p)\), then (20) and (27) give
\[
\nabla_{\mathcal D}(r)
\le
O\left(
1+\sup_{m\ge1}
\min\{\sqrt m,\ 1+(r/m^q)^p\}
\right).
\]
Split the supremum at
\[
m=r^{\,2p/(1+2pq)}.
\]
For smaller \(m\), use the square-root bound; for larger \(m\), use the expansion bound. Both give
\[
\nabla_{\mathcal D}(r)
=
O\!\left(1+r^{p/(1+2pq)}\right).
\]
This proves (4), including \(p=0\).

## 5.2. Adaptive radii

Let
\[
K=K(r)=\max\{2,\nabla_{\mathcal C}(r)\}
\]
and put
\[
R=\left\lfloor\frac a4 rK^{2q}\right\rfloor.
\]

For a root graph of order \(m\), there are two cases.

* If \(m<K^2\), the size-only part of (20) bounds its contribution by \(O(K)\).
* If \(m\ge K^2\), then
  \[
  \frac{2R}{L+1}
  \le
  \frac{2R}{am^q}
  \le r/2.
  \]
  The expansion part of (20) bounds its contribution by \(K\).

Thus
\[
\nabla_{\mathcal D}(R)=O(K),
\]
uniformly over all roots and all padding orders. This proves (5).

## 5.3. Transfer of universal lower exponents

Put
\[
B(\alpha)=b_{1-\alpha}.
\]
Thus \(B(\alpha)\) is the supremum of exponents universally guaranteed as polynomial expansion lower bounds for hereditary classes with separator profile \(\Theta(n^\alpha)\).

Take
\[
0<x<B(\alpha).
\]
The constructed exact-\(\alpha\) class satisfies
\[
\nabla_{\mathcal D}(R)=\Omega(R^x).
\]
Together with (5), this implies
\[
K(r)\ge c\bigl(rK(r)^{2q}\bigr)^x,
\]
or
\[
K(r)^{1-2qx}\ge c r^x.
\tag{28}
\]

If \(2qx<1\), it follows that
\[
\nabla_{\mathcal C}(r)
=
\Omega\!\left(r^{\,x/(1-2qx)}\right).
\]
The class \(\mathcal C\) was arbitrary among exact-\(\beta\) classes with finite expansion. Classes having infinite expansion at some depth satisfy every polynomial lower bound automatically. Hence
\[
B(\beta)\ge\frac{x}{1-2qx}.
\tag{29}
\]

If \(B(\beta)<\infty\), letting \(x\) approach \(B(\alpha)\) in (29) gives
\[
B(\alpha)
\le
\frac{B(\beta)}{1+2qB(\beta)}.
\tag{30}
\]
Indeed, if \(B(\alpha)\ge1/(2q)\), taking \(x\uparrow1/(2q)\) would instead force \(B(\beta)=\infty\).

Substituting
\[
\alpha=1-\varepsilon,\qquad
\beta=1-\eta,\qquad
q=\frac{\varepsilon-\eta}{1-\varepsilon}
\]
gives (6). No assertion that an endpoint lower exponent is attained was used.

# 6. What remains unproved

Theorem A requires more than
\[
s_{\mathcal C}(n)=\Omega(n^\alpha).
\]
To isolate the difference, define
\[
R_\alpha(n)=
\frac{\displaystyle\max_{1\le p\le n}
                   s_{\mathcal C}(p)/p^\alpha}
     {\displaystyle s_{\mathcal C}(n)/n^\alpha}.
\]
Condition (Q) is exactly the assertion that \(R_\alpha(n)\) is bounded.

The one-sided hypothesis bounds the denominator away from zero, but does not bound this ratio: an earlier graph can have a much larger normalized separator than graphs witnessing the current scale. The proof above does not regularize such witnesses at a uniformly bounded cost.

Therefore:

* any class witnessing a strict inequality \(b'_\varepsilon<b_\varepsilon\) must have unbounded \(R_{1-\varepsilon}(n)\);
* the equality holds for the substantial restricted family in Theorem A;
* the quantitative inequality (6) strengthens the comparison between different **two-sided** parameters;
* neither result establishes the missing implication for arbitrary oscillatory one-sided profiles.

The stretching idea from the previous attempt survives verification. The radius-sensitive estimate (20) supplies the additional quantitative result, and the robust-witness/padding argument removes dependence on separator-order conventions. I do not have either a full regularization theorem for arbitrary one-sided profiles or a counterexample to the conjectured equality.