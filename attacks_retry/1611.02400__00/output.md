```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The sharp full-routing capacity eventually equals floor(n/d)/n, and when n=md with fixed m>=4, the depth at which this saturation occurs is of order log d.",
  "would_publish": false,
  "caveats": "Uses the precise layered-path model below; strict asymptotic separation between consecutive fixed depths is not established."
}
```

# A finite-depth saturation theorem

The earlier attempt’s truncation argument is sound. I obtain a stronger result: the optimal capacity eventually reaches an explicit floor, and in a natural parameter regime the order of the required depth can be determined.

In particular, **strict worsening at every depth is false even when both \(d\) and \(n/d\) tend to infinity and the depth is \(o(d)\)**. This does not settle a formulation comparing successive *fixed* depths after optimizing over unrestricted width.

## 1. Precise model and results

Because the quoted conjecture is informal, I specify the model.

A depth-\(r\) network \(G\) has layers
\[
V_1,\ldots,V_r,\qquad |V_i|=n,
\]
with edges only between consecutive layers, and every bipartite graph \(G[V_i,V_{i+1}]\) is simple and \(d\)-regular. Assume \(1\le d\le n\).

A **full routing** consists of \(n\) vertex-disjoint paths, each meeting every layer once. A subrouting is **induced** if there are no edges between its distinct paths. Define
\[
c(G)=\min_{\mathcal P\text{ a full routing}}
\frac{\max\{|\mathcal Q|:\mathcal Q\subseteq\mathcal P
\text{ is induced}\}}{n},
\]
and
\[
C_r(n,d)=\max_G c(G).
\]
Thus \(C_r(n,d)\) is the best worst-case full-routing capacity among admissible networks.

If depth is instead counted by the number of interfaces, replace \(r-1\) by that depth throughout.

Here are the main results.

### Theorem 1 — Exact eventual capacity

Let \(d\ge2\), and put
\[
m=\left\lfloor\frac nd\right\rfloor,\qquad
k=m+1,\qquad
\theta=\frac{\lfloor n/k\rfloor-1}{d}.
\]
Then \(0\le\theta<1\), and
\[
\boxed{\quad
\binom nk\theta^{\,r-1}<1
\quad\Longrightarrow\quad
C_r(n,d)=\frac mn.
\quad}
\tag{1.1}
\]

Consequently, the sharp capacity is exactly \(\lfloor n/d\rfloor/n\) at all sufficiently large depths. A depth of \(O(n\log d)\) always suffices.

When \(n=md\), the more useful sufficient condition is
\[
\boxed{\quad
r-1>(m+1)^2\log(ed)
\quad\Longrightarrow\quad
C_r(md,d)=\frac1d.
\quad}
\tag{1.2}
\]

All logarithms are natural.

### Theorem 2 — The logarithmic depth scale is necessary

Fix an integer \(m\ge4\), and define
\[
R_*(m,d)=\min\{r\ge2:C_r(md,d)=1/d\}.
\]
Then
\[
\boxed{\qquad R_*(m,d)=\Theta_m(\log d)
\qquad(d\to\infty).\qquad}
\tag{1.3}
\]

Thus, for fixed width-to-degree ratio \(m\ge4\), the order of the depth at which the optimum saturates is determined.

The proofs are self-contained below.

---

## 2. Basic facts: monotonicity and the unavoidable floor

### Weak monotonicity

Every regular bipartite graph has a perfect matching: for \(S\) on one side,
\[
d|S|=e(S,N(S))\le d|N(S)|,
\]
so Hall’s condition holds. Repeatedly removing perfect matchings also gives a decomposition into \(d\) edge-disjoint perfect matchings.

If \(G^{-}\) is the prefix of a depth-\((r+1)\) network \(G\), every full routing of \(G^{-}\) extends through a perfect matching of the last interface. An induced subrouting of the extension restricts to an induced subrouting of the original routing. Hence
\[
c(G)\le c(G^{-}),
\qquad\text{and therefore}\qquad
C_{r+1}(n,d)\le C_r(n,d).
\tag{2.1}
\]

This verifies the corresponding argument in the previous attempt.

### A lower bound at every depth

Write
\[
n=md+s,\qquad 0\le s<d.
\]
Partition each layer into corresponding blocks of sizes
\[
d,\ldots,d,d+s,
\]
with \(m\) blocks altogether. Put edges only between corresponding blocks.

For a block of size \(b\ge d\), identify both sides with \(\mathbb Z_b\) and use the edges
\[
x\longleftrightarrow x+j,\qquad 0\le j<d.
\]
This is simple and \(d\)-regular.

Every full routing stays within the designated blocks. Choosing one path from each block gives an induced subrouting of size \(m\). Thus
\[
C_r(n,d)\ge \frac{\lfloor n/d\rfloor}{n}
\qquad(r\ge2).
\tag{2.2}
\]

The issue is to prove that sufficiently many layers force a routing attaining this upper limit.

---

## 3. A packing lemma for perfect matchings

The following is the key new observation.

### Lemma 3.1

Let \(H=(A,B;E)\) be a simple \(d\)-regular bipartite graph with \(|A|=|B|=n\), and fix a decomposition
\[
E=M_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}M_d
\]
into perfect matchings.

Let \(S\subseteq A\), with \(|S|=k>n/d\). Call \(M_j\) **good for \(S\)** if its \(k\) edges incident with \(S\) form an induced matching.

Then at most
\[
\left\lfloor\frac nk\right\rfloor-1
\tag{3.1}
\]
of the \(d\) matchings are good for \(S\).

#### Proof

For each \(j\), write
\[
T_j=M_j(S)\subseteq B.
\]
If \(M_j\) is good, every vertex of \(T_j\) has exactly one neighbor in \(S\).

Consequently, if \(M_j\) is good and \(\ell\ne j\), then
\[
T_j\cap T_\ell=\varnothing.
\tag{3.2}
\]
Indeed, a vertex in the intersection would have to be matched from its unique neighbor in \(S\) by both matchings, contradicting their edge-disjointness.

Let \(t\) be the number of good matchings. They cannot all be good, since otherwise their images of \(S\) would be pairwise disjoint, giving \(dk\le n\).

Choose one non-good matching. Its image of \(S\), together with the images from all \(t\) good matchings, comprises \(t+1\) pairwise disjoint sets of size \(k\). Therefore
\[
(t+1)k\le n,
\]
which proves (3.1). \(\square\)

In particular, because \(k>n/d\),
\[
\frac{\lfloor n/k\rfloor-1}{d}
\le \frac{d-2}{d}.
\tag{3.3}
\]
So at least two colors of every 1-factorization destroy any candidate set larger than \(n/d\). The stronger bound (3.1), rather than just “two colors,” is important when \(n/d\) is small.

---

## 4. Propagating the packing bound through the layers

### Proposition 4.1

For any integer \(k\) with \(n/d<k\le n\), put
\[
\theta_{n,d}(k)=\frac{\lfloor n/k\rfloor-1}{d}.
\]
Every depth-\(r\) network has a full routing for which the number of induced \(k\)-subroutings is at most
\[
\binom nk\,\theta_{n,d}(k)^{\,r-1}.
\tag{4.1}
\]

In particular, if the quantity in (4.1) is less than \(1\), then
\[
c(G)\le\frac{k-1}{n}.
\tag{4.2}
\]

#### Proof

Fix a 1-factorization at each interface. Independently at each interface, choose one of its \(d\) perfect matchings uniformly. Their union gives a full routing.

Label its paths by their vertices in \(V_1\). Fix a \(k\)-element set \(I\subseteq V_1\).

Suppose that the paths labeled by \(I\) form an induced subrouting through the current layer. Let \(S\) be their current endpoints. They remain induced through the next layer only if the newly chosen perfect matching is good for \(S\). By Lemma 3.1, the conditional probability of this is at most \(\theta_{n,d}(k)\), regardless of the preceding choices.

It follows that
\[
\Pr(I\text{ gives an induced full subrouting})
\le \theta_{n,d}(k)^{\,r-1}.
\]
Summing over the \(\binom nk\) possible sets \(I\) proves the expectation bound (4.1), and hence the existence of a routing satisfying it.

If this expectation is below \(1\), some routing has no induced \(k\)-subrouting at all. This gives (4.2). \(\square\)

This argument can also be made deterministic by conditional expectations: at each interface, choose the color leaving the fewest surviving candidate \(k\)-sets.

### Proof of Theorem 1

Take
\[
k=\left\lfloor\frac nd\right\rfloor+1=m+1.
\]
Under condition (1.1), Proposition 4.1 gives \(C_r(n,d)\le m/n\). The reverse inequality is (2.2).

For an explicit general threshold, if \(0<\theta<1\), it suffices to take
\[
r\ge
2+\left\lfloor
\frac{\log\binom nk}{\log(1/\theta)}
\right\rfloor.
\tag{4.3}
\]
If \(\theta=0\), depth \(2\) already suffices.

For \(d\ge3\), equations (3.3) and
\[
\log\binom nk\le k\log(en/k)<k\log(ed)
\]
show that the ratio in (4.3) is at most
\[
\frac d2\,k\log(ed)
\le \frac{n+d}{2}\log(ed)
\le n\log(ed).
\]
This proves the \(O(n\log d)\) assertion.

Now suppose \(n=md\). With \(k=m+1\),
\[
\theta
=\frac{\lfloor md/(m+1)\rfloor-1}{d}
<\frac{m}{m+1}
<e^{-1/(m+1)},
\]
while
\[
\binom{md}{m+1}\le(ed)^{m+1}.
\]
Therefore
\[
\binom{md}{m+1}\theta^{\,r-1}
<
\exp\!\left((m+1)\log(ed)-\frac{r-1}{m+1}\right),
\]
which is below \(1\) under (1.2). \(\square\)

### Small-degree cases

For \(d=1\), every routing is induced and \(C_r(n,1)=1\).

For \(d=2\), taking \(k=\lfloor n/2\rfloor+1\) gives \(\theta=0\). Thus the previous attempt’s even-\(n\) conclusion extends to all \(n\ge2\):
\[
C_r(n,2)=\frac{\lfloor n/2\rfloor}{n}
\qquad(r\ge2).
\tag{4.4}
\]

---

## 5. Plateaus with \(n/d\to\infty\) and \(r=o(d)\)

The saturation theorem is not confined to \(n=d\) or bounded degree.

For an integer \(u\ge2\), take
\[
d=u^4,\qquad n=u^5,\qquad m=u,
\]
and
\[
r_u=2+\left\lceil (u+1)^2\log(eu^4)\right\rceil.
\]
Then Theorem 1 gives
\[
C_{r_u}(u^5,u^4)
=
C_{r_u+1}(u^5,u^4)
=
\frac1{u^4}.
\tag{5.1}
\]
At the same time,
\[
\frac nd=u\longrightarrow\infty,
\qquad
\frac{r_u}{d}=O\!\left(\frac{\log u}{u^2}\right)\longrightarrow0.
\tag{5.2}
\]

Thus strict monotonicity fails even for this growing-degree, growing-width-ratio, sublinear-depth family.

### Connectedness does not rescue strictness here

For \(d\ge3\), the lower-bound construction can be made connected without losing its guarantee.

Start with the corresponding blocks from Section 2. In the first interface, choose one identity edge \(a_jb_j\) in each block. Delete these edges and insert
\[
a_jb_{j+1},
\]
with block indices taken cyclically. Leave all later interfaces unchanged.

Degrees are preserved. Each original block remains connected after deletion: the shifts \(1\) and \(2\) alone form a spanning cycle in that block’s first interface. The new edges join the blocks, so the entire network is connected.

For any full routing, in each starting block there is a path avoiding both its distinguished first-layer vertex \(a_j\) and distinguished second-layer vertex \(b_j\): at most two paths are excluded, and the block has at least \(d\ge3\) paths. Such a path stays in its original block and avoids all cross-block edges. Choosing one such path per block gives an induced subrouting of size \(m\).

Hence the exact large-depth value, and in particular the plateau family (5.1), can also be attained by connected networks.

---

## 6. Why logarithmic depth is necessary when \(n/d\) is fixed

I now prove Theorem 2. Its upper bound is already (1.2). For the lower bound, I construct networks in which every routing still has more than \(m\) mutually noninterfering paths at depth \(c_m\log d\).

The argument uses a small-submatrix estimate for random regular bipartite graphs.

### Lemma 6.1 — Local domination by independent edges

Let \(H\) be uniformly distributed over the simple \(d\)-regular bipartite graphs with parts of size \(n\). Suppose
\[
d\le n/4,\qquad t\le n/8.
\]
For fixed \(U,V\) of size \(t\) in the two parts, the random graph \(H[U,V]\) is stochastically dominated by independent edges of probability \(2d/n\).

#### Proof

Reveal the edges of \(U\times V\) one at a time. Consider an unrevealed edge \(uv\), conditioning on any positive-probability pattern of preceding revelations.

Let \(\Omega_1,\Omega_0\) be the compatible regular graphs containing and not containing \(uv\), respectively.

From \(H\in\Omega_1\), perform a switching
\[
uv,xy\ \mapsto\ uy,xv,
\]
where \(x\notin U\), \(y\notin V\), \(xy\in E(H)\), and \(uy,xv\notin E(H)\).

There are at least \(d(n-2t)\) edges between the complements of \(U,V\). At most \(d^2\) have \(x\in N(v)\), and at most \(d^2\) have \(y\in N(u)\). Thus each graph in \(\Omega_1\) admits at least
\[
d(n-2t-2d)
\]
valid switchings. They preserve every previously revealed edge status.

Conversely, each graph in \(\Omega_0\) admits at most \(d^2\) reverse switchings. Double counting gives
\[
|\Omega_1|d(n-2t-2d)\le|\Omega_0|d^2.
\]
Consequently,
\[
\Pr(uv\in E(H)\mid\text{previous revelations})
\le \frac{d}{n-2t-d}
\le \frac{2d}{n}.
\tag{6.1}
\]

Sequential coupling with independent uniform random variables now gives the asserted stochastic domination. \(\square\)

### Random layered construction

Fix \(m\ge4\), put \(n=md\), and define
\[
b_m=-\log(1-2/m),\qquad
c_m=\frac{1}{4mb_m}.
\]
Take any integer
\[
2\le r\le c_m\log n.
\tag{6.2}
\]
At each interface, independently choose a uniform simple \(d\)-regular bipartite graph.

Set
\[
a=(1-2/m)^{2(r-1)}
\]
and
\[
t=1+\left\lceil\frac{4r\log n}{a}\right\rceil.
\tag{6.3}
\]
Since \(r\le c_m\log n\),
\[
a^{-1}\le e^{2b_mr}\le n^{1/(2m)}.
\]
Hence, for fixed \(m\),
\[
t=O_m\!\left(n^{1/(2m)}(\log n)^2\right)
=o(n^{1/m}),
\tag{6.4}
\]
and in particular \(t\le n/8\) for sufficiently large \(n\).

Consider \(t\) labeled, vertex-disjoint potential paths: this means choosing \(t\) distinct vertices in every layer and pairing their labels across layers. There are at most \(n^{rt}\) such choices.

Ignore whether the path edges themselves exist. Ask only whether **every pair of the \(t\) potential paths has a cross-edge between them**. This is an increasing event in the selected \(t\times t\) interface submatrices.

By Lemma 6.1, its probability is at most its probability when all these edges are independent with probability \(2/m\). For any pair of labels, there are \(2(r-1)\) possible cross-edges. Different label pairs use disjoint sets of edges. Therefore the probability is at most
\[
(1-a)^{\binom t2}
\le \exp\!\left(-\frac{a\,t(t-1)}2\right).
\]
The union bound gives
\[
\begin{aligned}
\Pr(\text{some such }t\text{-tuple is pairwise conflicting})
&\le
\exp\!\left(rt\log n-\frac{a\,t(t-1)}2\right)\\
&\le \exp(-rt\log n)<1,
\end{aligned}
\tag{6.5}
\]
where the second inequality follows from (6.3).

Thus there exists a network in which the conflict graph of **every** full routing is \(K_t\)-free. Here the conflict graph has one vertex for each routed path, with adjacency precisely when the two paths have a cross-edge.

### Applying the elementary Ramsey bound

The elementary Ramsey bound says that every graph on at least
\[
\binom{m+t-1}{m}
\]
vertices has either an independent set of size \(m+1\) or a clique of size \(t\). This follows from the usual two-term Ramsey recursion and Pascal’s identity.

By (6.4),
\[
\binom{m+t-1}{m}=O_m(t^m)=o(n).
\]
Consequently, for all sufficiently large \(n\), every full-routing conflict graph of the constructed network has an independent set of size \(m+1\). Therefore
\[
C_r(md,d)\ge\frac{m+1}{md}>\frac1d
\qquad\text{whenever }2\le r\le c_m\log(md),
\tag{6.6}
\]
for sufficiently large \(d\), depending on \(m\).

Combining (6.6), monotonicity, and (1.2) yields
\[
c_m\log(md)<R_*(m,d)
\le 2+\left\lceil(m+1)^2\log(ed)\right\rceil
\]
up to the harmless integer rounding on the lower bound. This proves
\[
R_*(m,d)=\Theta_m(\log d).
\qquad\square
\]

---

## 7. What this resolves, and what remains

The proved conclusions are:

1. **Weak monotonicity:** adding a layer cannot increase sharp capacity.
2. **Exact eventual saturation:**
   \[
   C_r(n,d)=\frac{\lfloor n/d\rfloor}{n}
   \]
   after an explicit finite depth.
3. **A tight-order special case:** for fixed \(m\ge4\) and \(n=md\), the saturation depth is \(\Theta_m(\log d)\).
4. **Failure of unrestricted strict monotonicity:** optimal capacities have plateaus even with
   \[
   d\to\infty,\qquad n/d\to\infty,\qquad r=o(d),
   \]
   and connected attaining networks are available.

What is **not** proved is a strict asymptotic loss between successive fixed depths \(r\) and \(r+1\), for example after defining
\[
A_r(d)=\sup_{n\ge d}C_r(n,d)
\]
and comparing \(A_r(d)\) and \(A_{r+1}(d)\) as \(d\to\infty\).

The plateau results let depth grow with the parameters; they do not settle that fixed-depth comparison. Because the catalog’s prose does not distinguish these formulations, I report **partial**, rather than claiming a resolution of its intended asymptotic conjecture.