```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For N=2^d, the partition counts satisfy log f(d) = log f_{<=2}(d) + o(N) = (N/2) log d + C N + o(N), where C = -1 + sqrt(3)/4 - log(sqrt(3)-1)/2.",
  "would_publish": false,
  "caveats": "Exponential-scale estimates only; f_{<=2} is interpreted as allowing dimensions 0,1,2. Novelty relative to the full source and subsequent literature has not been verified."
}
```

# An exponential-scale estimate for the partition functions

All logarithms are natural. I interpret a subcube as a coordinate subcube, and \(f_{\le 2}(d)\) as counting partitions into subcubes of dimensions \(0,1,2\). The supplied excerpt does not explicitly define that notation; the result for \(f(d)\) does not depend on this naming convention. Allowing or excluding \(Q_d\) itself as a part changes \(f(d)\) by only one.

The principal result below is a determination of the constant-order term in the logarithms of the partition counts. The matching estimates from the previous attempt also survive checking; I give an alternative verification at the end.

## 1. Statement of the partial result

Put
\[
N=2^d,\qquad
p_*=\sqrt3-1,
\]
and define
\[
C=-1+\frac{\sqrt3}{4}-\frac12\log(\sqrt3-1)
  =-0.4110346\ldots.
\]

Then
\[
\boxed{
\log f_{\le2}(d)
=\frac N2\log d+CN+o(N),
}
\tag{1}
\]
and
\[
\boxed{
\log f(d)
=\frac N2\log d+CN+o(N).
}
\tag{2}
\]

Equivalently, with
\[
\alpha=e^{2C}
=\frac{\exp(-2+\sqrt3/2)}{\sqrt3-1}
=0.43952\ldots,
\]
we have
\[
\boxed{
f_{\le2}(d)=(\alpha d)^{N/2}\exp(o(N)),
\qquad
f(d)=(\alpha d)^{N/2}\exp(o(N)).
}
\tag{3}
\]

The proof below, without optimizing errors, gives an error
\[
O\!\left(Nd^{-1/12}\log d\right)
\]
in (1) and (2).

For comparison, writing \(n=N/2\), the matching estimates are
\[
\log m(d)
=n\left(\log d-1+O\!\left(\frac{\log d}{d}\right)\right),
\tag{4}
\]
\[
\log m'(d)
=n\left(\log d-1+\frac{2}{\sqrt d}
+O\!\left(\frac{\log d}{d}\right)\right).
\tag{5}
\]
Consequently,
\[
\frac1N\log\frac{f(d)}{m(d)}
\longrightarrow C+\frac12
=0.0889653\ldots,
\tag{6}
\]
and the same limit holds with \(f_{\le2}\) in place of \(f\), or \(m'\) in place of \(m\).

I do **not** assert that this constant is absent from the full source paper or subsequent literature: those were not available for verification here.

---

# 2. An entropy bound for uniform hypergraph perfect matchings

We first prove the upper-bound tool, including its applicability to hypergraphs with repeated edges. Repeated edges are regarded as separately labelled choices.

## Lemma 1

Let \(H\) be an \(r\)-uniform multihypergraph on \(v\) vertices. Suppose its maximum degree is at most \(D\), and every pair of distinct vertices belongs to at most \(B\) edges, counting multiplicity. If \(B/D=o(1)\), then
\[
\log \operatorname{pm}(H)
\le
\frac vr\bigl(\log D-(r-1)\bigr)+o(v).
\tag{7}
\]
The error is uniform over such hypergraphs.

For fixed \(r\ge3\), one may take the error to be
\[
O_r\!\left(v(B/D)^{1/(r-1)}\right).
\tag{8}
\]
For \(r=2\), it is
\[
O\!\left(v(B/D)\log(2D/B)\right).
\]

### Proof

If there are no perfect matchings, there is nothing to prove. Otherwise choose a uniformly random perfect matching \(M\), and independently give the vertices independent uniform priorities in \([0,1]\). Expose, in decreasing priority order, the edge of \(M\) containing each vertex.

When vertex \(x\) is reached, its matching edge is already determined unless \(x\) has the largest priority in that edge. If it is not already determined, its possible values are among the edges containing \(x\) all of whose vertices are still uncovered.

For a fixed matching \(M\), call a candidate edge **bad** if it meets some edge of \(M\) in at least two vertices. Write \(b_x(M)\) for the number of bad candidate edges containing \(x\).

Condition on the priority of \(x\) being \(t\), and on \(x\) being first in its matching edge. A nonbad candidate edge containing \(x\) meets \(r-1\) other matching edges, all distinct. It is still available only if all \(r(r-1)\) vertices of those matching edges have priorities less than \(t\). Thus its conditional availability probability is
\[
t^{r(r-1)}.
\]
A bad candidate has availability probability at most one.

The entropy chain rule and Jensen's inequality therefore give
\[
H(M)\le
\sum_x\int_0^1 t^{r-1}
\,\mathbb E_M\log\!\left(Dt^{r(r-1)}+b_x(M)\right)\,dt.
\tag{9}
\]

For every fixed \(M\),
\[
\sum_x b_x(M)
\le
r\cdot \frac vr\binom r2 B
=
v\binom r2 B.
\tag{10}
\]
Indeed, choose a pair lying in one matching edge, then an edge containing that pair, then one of its \(r\) vertices.

Applying Jensen once more, now over \(x\) and \(M\), yields
\[
H(M)\le
v\int_0^1 t^{r-1}
\log\!\left(Dt^{r(r-1)}+\binom r2B\right)\,dt.
\tag{11}
\]
Set \(\eta=\binom r2B/D\). The right side is
\[
\frac vr\log D-\frac{r-1}{r}v
+
v\int_0^1t^{r-1}
\log\!\left(1+\eta t^{-r(r-1)}\right)\,dt.
\]
After substituting \(u=t^r\), the error integral becomes
\[
\frac1r\int_0^1\log\!\left(1+\eta u^{-(r-1)}\right)\,du.
\tag{12}
\]
This is \(O_r(\eta^{1/(r-1)})\) for \(r\ge3\), and \(O(\eta\log(2/\eta))\) for \(r=2\). Since \(H(M)=\log\operatorname{pm}(H)\), the lemma follows. ∎

---

# 3. Upper bound for edge-and-square partitions

For \(U\subseteq V(Q_d)\), let \(Z_{24}(U)\) count partitions of \(U\) into edges and squares, with no singletons.

Define, for \(0\le p\le1\),
\[
\Phi(p)=
-\frac p2\log p
-\frac{1-p}{4}\log\bigl(2(1-p)\bigr)
-\frac{3-p}{4},
\tag{13}
\]
with the usual convention \(0\log0=0\).

We will prove the following uniform bound:
\[
\boxed{
\log Z_{24}(U)
\le
\frac{|U|}{2}\log d+C|U|+o(N),
}
\tag{14}
\]
where the \(o(N)\) is uniform over \(U\).

The key is to turn a mixed-size partition problem into a uniform hypergraph perfect-matching problem.

## 3.1. Padding edges with dummy vertices

Write \(V=|U|\), and fix a profile with \(a\) edges and \(b\) squares:
\[
2a+4b=V.
\]
Put
\[
T=2a,\qquad p=T/V.
\]
Temporarily assume
\[
V\ge d^4,\qquad T\ge d^2,\qquad b\ge1.
\tag{15}
\]

Introduce \(T\) dummy vertices. Construct a 4-uniform multihypergraph as follows:

* every edge of \(Q_d[U]\), together with every pair of dummy vertices, is a hyperedge;
* every square contained in \(U\) is included with multiplicity \(L\), where
  \[
  L=\left\lfloor\frac{(T-1)(V-T)}{d-1}\right\rfloor.
  \]

Let \(F_{a,b}(U)\) denote the number of original partitions with this profile. A perfect matching of the augmented hypergraph necessarily uses exactly \(a=T/2\) padded edges and \(b\) square edges. Hence its number of perfect matchings is exactly
\[
F_{a,b}(U)\,
\frac{T!}{2^a}\,L^b.
\tag{16}
\]

Set
\[
\Delta=\frac{Vd(T-1)}2.
\]
A real vertex has degree at most
\[
d\binom T2+L\binom d2\le\Delta.
\]
A dummy vertex has degree at most
\[
\frac{Vd}{2}(T-1)=\Delta.
\]

The codegrees are also small relative to \(\Delta\):

* two real vertices have codegree at most
  \[
  \binom T2+L(d-1)\le V(T-1);
  \]
* a real and a dummy vertex have codegree at most \(d(T-1)\);
* two dummy vertices have codegree at most \(Vd/2\).

Thus the maximum codegree divided by \(\Delta\) is at most
\[
\max\left\{\frac2d,\frac2V,\frac1{T-1}\right\}
=O(1/d)
\tag{17}
\]
in the range (15).

Lemma 1 gives
\[
\log\left(F_{a,b}(U)\frac{T!}{2^a}L^b\right)
\le
\frac{V+T}{4}(\log\Delta-3)+O(Vd^{-1/3}).
\tag{18}
\]

Using Stirling's formula and the definition of \(L\), cancellation of the terms involving \(\log V\) gives
\[
\log F_{a,b}(U)
\le
\frac V2\log d+V\Phi(p)
+O(Vd^{-1/3}+\log V+d).
\tag{19}
\]
Here rounding \(L\) changes the logarithm by at most \(O(d/T)\); the factor \(T-1\), rather than \(T\), contributes only a bounded upper error. Also, replacing \(\log(d-1)\) by \(\log d\) is valid for this upper bound.

## 3.2. Boundary profiles

The omitted cases cause no difficulty, but must be included.

* If \(T=0\), apply Lemma 1 directly to the square hypergraph. Its maximum degree is \(\binom d2\), and its maximum codegree is \(d-1\). This gives (19) with \(p=0\).
* If \(b=0\), apply the \(r=2\) case directly to \(Q_d[U]\), obtaining the bound with \(p=1\).
* If \(0<T<d^2\), first choose the \(a<d^2/2\) edges in at most
  \[
  (Vd/2)^a=\exp(O(d^3))
  \]
  ways, then apply the pure-square bound to the remaining vertices.
* If \(V<d^4\), the crude bound
  \[
  Z_{24}(U)\le \left(d+\binom d2\right)^V
  \]
  contributes only \(O(d^4\log d)=o(N)\) to the logarithm.

There are at most \(N+1\) profiles. Thus, uniformly over \(U\),
\[
\log Z_{24}(U)
\le
\frac V2\log d+
V\max_{0\le p\le1}\Phi(p)
+
O(Nd^{-1/3}+d^4\log d).
\tag{20}
\]

Finally,
\[
\Phi'(p)
=-\frac12\log p+\frac14\log(2(1-p)),
\]
and
\[
\Phi''(p)=-\frac1{2p}-\frac1{4(1-p)}<0.
\]
The unique maximizer satisfies
\[
p^2=2(1-p),
\]
so it is \(p_*=\sqrt3-1\). Substitution gives
\[
\Phi(p_*)=
-1+\frac{\sqrt3}{4}-\frac12\log(\sqrt3-1)=C.
\]
This proves (14).

---

# 4. Singletons and larger cubes do not change the constant

Consider an arbitrary subcube partition. Call its singleton parts and its parts of dimension at least three **exceptional**. Once the exceptional parts are chosen, the remaining set \(U\) must be partitioned into edges and squares.

By (14),
\[
f(d)\le
d^{N/2}e^{CN+o(N)}
\sum_{\mathcal E}
\prod_{B\in\mathcal E}
d^{-|B|/2}e^{-C|B|},
\tag{21}
\]
where the sum is over vertex-disjoint collections of exceptional cubes.

Dropping the disjointness restriction bounds this sum by
\[
\prod_{B\text{ exceptional}}
\left(1+d^{-|B|/2}e^{-C|B|}\right).
\]
Its logarithm is at most
\[
N
\sum_{\substack{0\le k\le d\\k=0\text{ or }k\ge3}}
\frac{\binom dk}{2^k}
d^{-2^{k-1}}e^{-C2^k}.
\tag{22}
\]
Here \(N\binom dk/2^k\) is the number of \(k\)-dimensional coordinate subcubes.

The \(k=0\) term is \(e^{-C}N/\sqrt d\). The \(k=3\) term is \(O(N/d)\). The sum for \(k\ge4\) is \(O(N/d^2)\): for all sufficiently large \(d\),
\[
e^{-C2^k}\le d^{2^{k-1}/4},
\]
and therefore
\[
\frac{\binom dk}{2^k}
d^{-2^{k-1}}e^{-C2^k}
\le
\frac{d^{\,k-\frac34 2^{k-1}}}{2^k k!}
\le \frac{d^{-2}}{2^k k!}.
\]
Consequently, (22) is \(o(N)\). We have proved
\[
\log f(d)\le\frac N2\log d+CN+o(N).
\tag{23}
\]

The remaining task is a matching lower bound using only dimensions \(0,1,2\).

---

# 5. A permanent lower bound for nearly regular bipartite graphs

We will leave a positive proportion of vertices after choosing squares, and complete their partition using edges and singletons.

## Lemma 2

Let \(G\) be bipartite with both classes of size \(h\), maximum degree at most \(D\ge1\), and \(E\) edges. Then
\[
\boxed{
\log m'(G)\ge
h(\log D-1)-\left(h-\frac ED\right)\log D.
}
\tag{24}
\]

### Proof

Let \(A\) be the bipartite adjacency matrix. There exists a nonnegative matrix \(F\) such that every row and column of \(A+F\) sums to \(D\): fill the row and column deficits, whose totals agree.

Put
\[
C_0=A+F/D,
\qquad
\delta=h-E/D.
\]
The total sum of the entries of \(F\) is \(D\delta\).

For every positive vector \(x\), weighted AM–GM, with weights \(A_{ij}/D\) and \(F_{ij}/D\) in row \(i\), gives
\[
(C_0x)_i
\ge
D\prod_j x_j^{A_{ij}/D}(x_j/D)^{F_{ij}/D}.
\]
Multiplying over rows, and using the column sums of \(A+F\), gives
\[
\frac{\prod_i(C_0x)_i}{\prod_jx_j}
\ge D^{h-\delta}.
\tag{25}
\]

The capacity form of the van der Waerden permanent bound therefore implies
\[
\operatorname{per}(C_0)
\ge \frac{h!}{h^h}D^{h-\delta}.
\tag{26}
\]
For completeness, this capacity form follows directly by scaling a positive matrix to a doubly stochastic matrix and applying van der Waerden; nonnegative matrices follow by approximation.

On the other hand, expansion according to the entries chosen from \(A\) gives
\[
\operatorname{per}(A+F/D)
=
\sum_{M\text{ a matching of }G}
\operatorname{per}\bigl((F/D)[X\setminus V(M),Y\setminus V(M)]\bigr).
\]
Every residual matrix in this sum has row sums at most one, so each residual permanent is at most one. Hence
\[
\operatorname{per}(C_0)\le m'(G).
\]
Combining this with \(h!\ge(h/e)^h\) proves the lemma. ∎

---

# 6. Counting many well-distributed square packings

A random greedy process supplies square packings for which the residual cube graph is nearly regular.

I include the probabilistic approximation needed for this step, rather than assuming a hypergraph counting theorem.

## Lemma 3: a fixed-time greedy-process estimate

Let \(H\) be a simple \(r\)-uniform, \(D\)-regular hypergraph with maximum codegree at most \(B\), where \(B/D\to0\).

Give each edge an independent exponential clock of rate \(1/D\). When its clock rings, accept the edge if all its vertices are still uncovered.

Let \(I_v(t)\) indicate that \(v\) is uncovered at time \(t\). For fixed \(k,T\), uniformly over distinct \(v_1,\ldots,v_k\) and \(0\le t\le T\),
\[
\mathbb E\prod_{i=1}^k I_{v_i}(t)
=
y(t)^k+O_{r,k,T}\bigl((B/D)^{1/3}\bigr),
\tag{27}
\]
where
\[
y(t)=(1+(r-1)t)^{-1/(r-1)}.
\tag{28}
\]

### Proof

To determine whether a vertex is uncovered at time \(t\), inspect its incident clocks before \(t\); for an incident edge with clock \(s<t\), recursively inspect its other vertices before time \(s\). Clock times strictly decrease along every recursive path.

First consider this backwards exploration on the infinite \(D\)-regular \(r\)-uniform hypertree. The expected number of vertices reached at depth \(\ell\), from \(k\) initial queries, is at most
\[
k\frac{((r-1)T)^\ell}{\ell!}.
\]
Indeed, there are at most \(D^\ell(r-1)^\ell\) possible paths, while the probability of their clocks occurring in the required decreasing order in \([0,T]\) is at most \((T/D)^\ell/\ell!\). Thus the expected total exploration size is at most
\[
k e^{(r-1)T}.
\tag{29}
\]

Couple the finite-hypergraph exploration to \(k\) independent hypertree explorations, stopping upon reaching \(K\) vertices. Before this stopping time, at most \(O_r(K^2B)\) non-parent edge incidences can connect two already encountered vertices.

A lazy revelation of clocks makes the coupling bound explicit. Reveal a clock's value only if it falls before the current query time; otherwise record only the resulting lower bound on that clock. An unrevealed or lower-truncated exponential clock has conditional probability at most \(T/D\) of falling in any relevant additional time interval. Replacing a previously encountered non-parent edge by a fresh tree edge can therefore fail with probability at most \(2T/D\). An active edge that repeats a previously encountered vertex is covered by the same count.

Consequently, the coupling failure probability before size \(K\) is
\[
O_{r,k,T}(K^2B/D).
\]
By (29), the probability that the tree exploration exceeds size \(K\) is \(O_{r,k,T}(1/K)\). Taking \(K\) of order \((D/B)^{1/3}\) gives total error
\[
O_{r,k,T}((B/D)^{1/3}).
\tag{30}
\]

It remains to identify the limit on the hypertree. Let \(q_D(t)\) be the survival probability at a vertex with its parent edge omitted. Branch independence gives
\[
q_D(t)=
\left(
1-\frac1D\int_0^t e^{-s/D}q_D(s)^{r-1}\,ds
\right)^{D-1}.
\]
Differentiating,
\[
q_D'(t)=
-\left(1-\frac1D\right)e^{-t/D}
q_D(t)^{\,r-1/(D-1)}.
\]
On every fixed interval, these solutions converge uniformly, with error \(O(1/D)\), to the solution of
\[
y'=-y^r,\qquad y(0)=1.
\]
That solution is (28). The root survival probability differs from \(q_D(t)\) by \(O(1/D)\). Combining independent tree roots with (30) proves (27). ∎

## 6.1. Application to the square hypergraph

Let \(H_d\) have the vertices of \(Q_d\), with its squares as 4-edges. Then
\[
D=\binom d2,\qquad B=d-1,
\]
so Lemma 3 has error
\[
\theta=O(d^{-1/3}),
\qquad
y(t)=(1+3t)^{-1/3}.
\tag{31}
\]

Let \(W(t)\) be the uncovered vertices, and let \(A(t)\) be the number of squares wholly contained in \(W(t)\).

Applying Lemma 3 to sets of at most eight vertices gives
\[
\mathbb E|W(t)|=Ny(t)+O(N\theta),
\qquad
\operatorname{Var}|W(t)|=O(N^2\theta+N),
\tag{32}
\]
and
\[
\mathbb EA(t)=\frac{ND}{4}y(t)^4+O(ND\theta),
\]
\[
\operatorname{Var}A(t)
=O((ND)^2\theta+ND^2).
\tag{33}
\]
For (33), disjoint pairs of squares use the eight-vertex estimate; the number of intersecting ordered square pairs is \(O(ND^2)\).

We also need the residual degrees in the ordinary cube graph. Set
\[
X_v(t)=\sum_{u\sim v}I_u(t).
\]
Using the one-, two-, and three-vertex estimates in Lemma 3,
\[
\mathbb E\!\left[
I_v(t)\bigl(X_v(t)-dy(t)\bigr)^2
\right]
=O(d+d^2\theta).
\tag{34}
\]

Choose
\[
\varepsilon=d^{-1/12}.
\]
Then \(\theta=O(\varepsilon^4)\). Chebyshev's inequality on a time grid of mesh \(\varepsilon\), followed by monotonic interpolation, shows that, with probability \(1-O(\varepsilon)\), uniformly on a fixed bounded time interval,
\[
|W(t)|/N=y(t)+O(\varepsilon),
\tag{35}
\]
\[
A(t)/(ND/4)=y(t)^4+O(\varepsilon).
\tag{36}
\]
Indeed, each grid-point failure probability is \(O(\theta/\varepsilon^2)=O(\varepsilon^2)\), and there are \(O(1/\varepsilon)\) grid points.

At any fixed time, (34) and Markov's inequality also show, with probability \(1-O(\varepsilon)\), that all but \(O(\varepsilon N)\) surviving vertices have residual graph degree
\[
dy(t)+O(\varepsilon d).
\tag{37}
\]

## 6.2. Stop after a prescribed number of squares

Fix \(0<p<1\), put \(q=1-p\), and take
\[
s=\lfloor qN/4\rfloor.
\]
Let \(\tau_s\) be the time of the \(s\)-th accepted square.

The clock process, viewed only at accepted edges, chooses uniformly from the currently available squares. This follows from the memoryless property: an available square has not rung previously, and unavailable squares never become available again.

Let \(t_0\) satisfy \(y(t_0)=p\). By (35), with probability tending to one,
\[
\tau_s=t_0+O(\varepsilon).
\]
To transfer (37) to this random time, apply it at the two fixed times \(t_0\pm K\varepsilon\), for a sufficiently large constant \(K\). Their surviving sets differ by \(O(\varepsilon N)\) vertices, by (35), and residual degrees decrease with time. It follows that after \(s\) accepted squares, all but \(O(\varepsilon N)\) remaining vertices have graph degree
\[
pd+O(\varepsilon d).
\tag{38}
\]

Furthermore, after \(i\le s\) accepted squares, the number of available squares is at least
\[
(1-O(\varepsilon))
\frac{ND}{4}\left(1-\frac{4i}{N}\right)^4.
\tag{39}
\]

Call an ordered greedy trajectory good if it has (38) at its endpoint and satisfies (39) at every step. The probability of a good trajectory is \(1-o(1)\).

The probability of any particular good ordered trajectory is at most the reciprocal of the product of the lower bounds in (39). Each unordered square packing has at most \(s!\) orders. Therefore the number \(P_s\) of square packings satisfying (38) obeys
\[
P_s\ge
\frac{1-o(1)}{s!}
\prod_{i=0}^{s-1}
\left[
(1-O(\varepsilon))
\frac{ND}{4}\left(1-\frac{4i}{N}\right)^4
\right].
\tag{40}
\]

Taking logarithms, applying Stirling, and using a Riemann sum gives
\[
\log P_s
\ge
N\left[
\frac q4\left(\log\frac Dq-3\right)-p\log p
\right]-o(N).
\tag{41}
\]
The integral behind this simplification is
\[
\int_0^q\log(1-x)\,dx=-p\log p-q.
\]

Since \(D=\binom d2\),
\[
\log P_s
\ge
N\left[
\frac q2\log d
-\frac q4\log(2q)
-\frac{3q}{4}
-p\log p
\right]-o(N).
\tag{42}
\]

---

# 7. Completing the square packings with edges and singletons

Fix one of the packings counted in (42), and let \(R\) be the cube graph induced on its remaining vertices.

Every square has two vertices in each parity class, so \(R\) is bipartite with equally sized classes:
\[
h=\frac{pN}{2}+O(1).
\]
By (38), all but \(O(\varepsilon N)\) vertices have degree \(pd+O(\varepsilon d)\).

Delete edges incident to exceptional vertices. The resulting spanning subgraph \(R'\) has maximum degree at most
\[
D_0=pd+O(\varepsilon d)
\]
and
\[
hD_0-e(R')=O(\varepsilon Nd).
\]
Lemma 2 therefore gives
\[
\log m'(R)
\ge \log m'(R')
\ge
\frac{pN}{2}\bigl(\log(pd)-1\bigr)
-O(\varepsilon N\log d)-o(N).
\tag{43}
\]
Because \(\varepsilon\log d\to0\), the error is \(o(N)\).

Every matching of \(R\), together with its unmatched singleton vertices and the selected squares, produces a partition counted by \(f_{\le2}(d)\). The square packing and residual matching are recoverable from the partition, so there is no overcounting.

Combining (42) and (43) yields, for every fixed \(0<p<1\),
\[
\log f_{\le2}(d)
\ge
\frac N2\log d+N\Phi(p)-o(N).
\tag{44}
\]
Taking \(p=p_*=\sqrt3-1\), where \(\Phi(p_*)=C\), gives
\[
\log f_{\le2}(d)
\ge
\frac N2\log d+CN-o(N).
\tag{45}
\]

Together with
\[
f_{\le2}(d)\le f(d)
\]
and the upper bound (23), this proves (1) and (2).

---

# 8. Verification of the matching estimates

Here is a short independent verification of the previous attempt's matching conclusion. It uses only the ordinary van der Waerden and Brégman permanent inequalities; the \(k\)-permanent extension is unnecessary.

Let \(G\) be \(d\)-regular bipartite with both classes of size \(n\), and let \(M_k(G)\) count its \(k\)-edge matchings.

The standard perfect-matching bounds are
\[
d^n\frac{n!}{n^n}
\le m(G)\le(d!)^{n/d}.
\tag{46}
\]
For \(Q_d\), where \(n=2^{d-1}\), Stirling gives (4).

## Lower bound for all matchings

Put \(r=n-k\). If \(A\) is the bipartite adjacency matrix, the block matrix
\[
B=
\begin{pmatrix}
\frac{k}{nd}A & \frac1n J_{n\times r}\\[2mm]
\frac1n J_{r\times n} & 0
\end{pmatrix}
\]
is doubly stochastic. Its permanent is
\[
\operatorname{per}(B)
=
(r!)^2
\left(\frac{k}{nd}\right)^k
n^{-2r}M_k(G).
\]
Van der Waerden's inequality therefore gives
\[
M_k(G)\ge
\frac{(n+r)!}{(n+r)^{n+r}}
\frac{n^{2r}(nd/k)^k}{(r!)^2}.
\tag{47}
\]

Choose \(r=\lfloor n/\sqrt d\rfloor\). Stirling's formula in (47) gives
\[
\log m'(G)
\ge
n\left(\log d-1+\frac2{\sqrt d}\right)
-O(n/d+\log n).
\tag{48}
\]

## Upper bound for all matchings

Fix the \(k\) saturated vertices in one bipartition class, and append \(n-k\) all-one rows to their adjacency matrix. Brégman's inequality gives
\[
M_k(G)\le
\binom nk
\frac{(d!)^{k/d}(n!)^{(n-k)/n}}{(n-k)!}.
\tag{49}
\]

Write
\[
a=\frac{\log(d!)}d,\qquad \rho=\frac{n-k}{n}.
\]
Uniformly in \(k\), the logarithm of the right side of (49) is
\[
n\left[
(1-\rho)a
-2\rho\log\rho
-(1-\rho)\log(1-\rho)
\right]+O(\log n).
\tag{50}
\]
Its maximum occurs where
\[
\rho^2=e^{-a-1}(1-\rho),
\]
and the maximum, divided by \(n\), is
\[
a+\rho-\log(1-\rho)
=
\log d-1+\frac2{\sqrt d}
+O\!\left(\frac{\log d}{d}\right).
\]
Summing over the \(n+1\) possible sizes adds only \(O(\log n)\). For the hypercube this proves (5).

Combining (4) and (5) also confirms the previous attempt's ratio estimate:
\[
\boxed{
\log\frac{m'(d)}{m(d)}
=
\frac{2^d}{\sqrt d}
+
O\!\left(\frac{2^d\log d}{d}\right).
}
\tag{51}
\]

---

# 9. Scope and unresolved issues

The displayed partition asymptotics have complete upper and lower arguments above. In particular, the upper bound covers singleton parts and every dimension \(3,\ldots,d\), not merely bounded-dimensional parts.

What remains unresolved here is finer enumeration:

1. The next term in \(\log m(d)\) is not determined.
2. Formula (5) determines the first monomer correction for all matchings, but not smaller-order terms.
3. Formulas (1) and (2) determine the constant free energy for the partition functions, but not their next corrections or multiplicative asymptotics.
4. Although
   \[
   \log\frac{f(d)}{f_{\le2}(d)}=o(2^d),
   \]
   this does not determine the actual size of that ratio.
5. The full source and follow-up literature have not been checked, so the argument is presented as an independently justified estimate, not as a verified claim of publication-level novelty.