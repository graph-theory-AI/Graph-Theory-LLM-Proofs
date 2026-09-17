```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured stage count is sharp for affine masks over finite fields, and the universal lower bound holds for all k and n.",
  "would_publish": false,
  "caveats": "The upper bound for arbitrary masks is not proved; novelty of the special cases below has not been checked."
}
```

## 1. Results obtained

I do not resolve the general conjecture. I give self-contained proofs of:

1. The universal lower bound
   \[
   r(k,n)\ge 2n-1.
   \]
2. A matching upper bound for **affine masks** over every finite field, for every \(n\). These are masks parametrized by two affine surjections
   \[
   \mathbb F_q^n\longrightarrow \mathbb F_q^{n-1}.
   \]
   The proof constructs all routing paths using linear algebra.
3. The complete case \(r(k,2)=3\).
4. When \(n=3\), a five-stage routing for every mask consisting of \(k\) parallel copies of an arbitrary perfect matching.

The affine result is sharp within that mask class.

## 2. Word representation of the network

Put \(m=n-1\), and identify vertex labels with words in
\[
A^m,\qquad A=\{0,\ldots,k-1\}.
\]
The adjacency rule becomes
\[
(a_1,\ldots,a_m)\longrightarrow(a_2,\ldots,a_m,b),
\qquad b\in A.
\]

Write \(G_L\) for the network with \(L\) transitions, hence \(L+1\) vertex layers.

### Every routing is forward and uses every edge

A mask has \(k^{m+1}\) edges, counted with multiplicity, so a routing contains \(k^{m+1}\) paths. Each path between the end layers has length at least \(L\), while \(G_L\) has exactly \(Lk^{m+1}\) edges. Consequently, edge-disjointness forces every path to have length exactly \(L\), and every network edge is used.

Thus even if paths are initially interpreted as undirected, every routing path moves forward through the layers.

A forward path is specified by a word
\[
w_1w_2\cdots w_{m+L}.
\]
Its source and target are respectively
\[
(w_1,\ldots,w_m),\qquad(w_{L+1},\ldots,w_{L+m}),
\]
and its edge at transition \(h\) is specified by the length-\((m+1)\) window
\[
(w_h,\ldots,w_{h+m}).
\]

We obtain the following useful criterion:

> **Window criterion.** A collection of words, one for each distinguished mask edge, gives a routing if it has the prescribed endpoints and, at every transition, its length-\((m+1)\) windows run through \(A^{m+1}\) exactly once.

## 3. Universal lower bound

Let
\[
\rho(a_1,\ldots,a_m)=(a_m,\ldots,a_1),
\]
and take the mask consisting of \(k\) parallel edges from every \(x\in A^m\) to \(\rho(x)\).

I show that this single mask cannot be routed for any \(L<2m\).

### Case 1: \(L\le m\)

The two endpoints determine at most one forward path: their prescribed initial and terminal portions together cover the entire path word. Thus there cannot be \(k\ge2\) edge-disjoint forward paths between any prescribed pair \(x,\rho(x)\).

### Case 2: \(m<L<2m\)

Consider transition \(m\). Its edge window is
\[
(w_m,\ldots,w_{2m}).
\]
This window contains both
\[
w_m=x_m,\qquad w_{L+1}=y_1.
\]
The two positions are distinct, and the reversal demand requires \(y_1=x_m\).

Hence every routing path must use, at transition \(m\), an edge whose window has equality in these two specified positions. There are only \(k^m\) such edges, but the routing has \(k^{m+1}\) paths. This contradicts edge-disjointness.

Therefore \(L\ge2m\), giving
\[
\boxed{r(k,n)\ge2m+1=2n-1.}
\]

## 4. Affine masks attain the lower bound

Fix a prime power \(q\), and identify the digit alphabet with \(\mathbb F_q\), using the same identification at every layer.

Let
\[
E=\mathbb F_q^{m+1}.
\]
Take affine surjections
\[
x:E\longrightarrow\mathbb F_q^m,\qquad
y:E\longrightarrow\mathbb F_q^m.
\]
For each \(e\in E\), place one distinguished mask edge between \(x(e)\) and \(y(e)\).

Every fiber of either map has size \(q\), so this is a \(q\)-regular bipartite multigraph. Call it an **affine mask**.

> **Theorem.** Every affine mask is routable in
> \[
> G_{2m}=(\operatorname{SE}(q,m+1))^{2m}.
> \]
> Thus \(2n-1\) stages suffice for every affine mask.

The proof uses the following linear-algebra lemma.

### 4.1. A two-flag basis lemma

A complete flag in a \(d\)-dimensional vector space \(H\) is a chain
\[
0=F_0<F_1<\cdots<F_d=H,\qquad \dim F_i=i.
\]

> **Lemma.** Given two complete flags \(F\) and \(G\) in \(H\), there is an ordered basis \(z_1,\ldots,z_d\) such that, for every \(0\le i\le d\),
> \[
> H=F_{d-i}\oplus\langle z_1,\ldots,z_i\rangle
> \tag{1}
> \]
> and
> \[
> H=G_i\oplus\langle z_{i+1},\ldots,z_d\rangle.
> \tag{2}
> \]

**Proof.** We first note that any two nonzero vectors have a hyperplane containing neither. If they are independent, choose a linear functional taking value \(1\) on both; if dependent, choose a functional nonzero on one. Its kernel works. This is valid even over \(\mathbb F_2\).

Proceed by induction on \(d\), with \(d=1\) immediate.

Choose
\[
z_1\notin F_{d-1},
\]
and choose a hyperplane \(K\) containing neither \(z_1\) nor the line \(G_1\). Let
\[
p:H\longrightarrow K
\]
be projection along \(\langle z_1\rangle\). Define complete flags in \(K\) by
\[
F'_a=p(F_a),\qquad
G'_a=K\cap G_{a+1},
\qquad 0\le a\le d-1.
\]
They have the asserted dimensions because \(z_1\notin F_{d-1}\) and \(G_1\not\subseteq K\).

Apply induction to obtain a basis \(z_2,\ldots,z_d\) of \(K\).

For \(i\ge1\), induction gives
\[
p(F_{d-i})\cap\langle z_2,\ldots,z_i\rangle=0.
\]
Since \(p\) is injective on \(F_{d-i}\), this implies
\[
F_{d-i}\cap\langle z_1,\ldots,z_i\rangle=0.
\]
Also,
\[
G_i\cap\langle z_{i+1},\ldots,z_d\rangle
=
G'_{i-1}\cap\langle z_{i+1},\ldots,z_d\rangle
=0.
\]
The dimensions give (1) and (2); the boundary cases are immediate. ∎

### 4.2. Constructing the routing

Write
\[
x(e)=(\alpha_1(e)+a_1,\ldots,\alpha_m(e)+a_m),
\]
\[
y(e)=(\beta_1(e)+b_1,\ldots,\beta_m(e)+b_m),
\]
where
\[
\alpha_1,\ldots,\alpha_m,\qquad
\beta_1,\ldots,\beta_m
\]
are two linearly independent lists in
\[
W=E^*,\qquad \dim W=m+1.
\]

Choose an \(m\)-dimensional hyperplane \(H\le W\) containing neither \(\alpha_m\) nor \(\beta_1\).

For \(0\le a<m\), set
\[
F_a=H\cap\langle\alpha_{m-a},\ldots,\alpha_m\rangle,
\]
\[
G_a=H\cap\langle\beta_1,\ldots,\beta_{a+1}\rangle,
\]
and set \(F_m=G_m=H\).

These are complete flags in \(H\). Indeed, each displayed span contains a vector outside \(H\), so intersecting it with \(H\) lowers its dimension by exactly one.

Use the lemma to choose \(z_1,\ldots,z_m\in H\). For each demand \(e\in E\), define its path word by
\[
\begin{split}
w(e)=(&x_1(e),\ldots,x_m(e),\\
      &z_1(e),\ldots,z_m(e),\\
      &y_1(e),\ldots,y_m(e)).
\end{split}
\tag{3}
\]
This has length \(3m\), hence specifies a path with \(2m\) transitions and the required endpoints.

It remains to verify every edge-window condition.

For \(1\le i\le m\), the \(i\)-th window has linear parts
\[
\alpha_i,\ldots,\alpha_m,z_1,\ldots,z_i.
\]
Now
\[
\begin{aligned}
\langle z_1,\ldots,z_i\rangle
\cap\langle\alpha_i,\ldots,\alpha_m\rangle
&=\langle z_1,\ldots,z_i\rangle\cap F_{m-i}\\
&=0.
\end{aligned}
\]
Their dimensions sum to \(m+1\), so these linear forms constitute a basis of \(W\).

For \(1\le j\le m\), window \(m+j\) has linear parts
\[
z_j,\ldots,z_m,\beta_1,\ldots,\beta_j.
\]
Similarly,
\[
\begin{aligned}
\langle z_j,\ldots,z_m\rangle
\cap\langle\beta_1,\ldots,\beta_j\rangle
&=\langle z_j,\ldots,z_m\rangle\cap G_{j-1}\\
&=0,
\end{aligned}
\]
and again the dimensions sum to \(m+1\).

Consequently, every window map in (3) is an affine bijection
\[
E\longrightarrow\mathbb F_q^{m+1}.
\]
The window criterion proves that the paths are mutually edge-disjoint. ∎

The construction is effective: hyperplanes, projections, and bases give a polynomial-time linear-algebra algorithm for a succinct description of all paths.

### 4.3. Sharpness within the affine class

The reversal mask from Section 3 is affine: take
\[
x(e_1,\ldots,e_{m+1})=(e_1,\ldots,e_m),
\qquad y=\rho\circ x.
\]
It fails at every smaller number of stages. Thus the affine-mask theorem attains the exact worst-case stage count for that class.

## 5. Two additional special cases

### 5.1. All masks when \(n=2\)

Here \(\operatorname{SE}(k,2)=K_{k,k}\).

Every \(k\)-regular bipartite multigraph decomposes into \(k\) perfect matchings: Hall’s condition follows from regularity, and one removes perfect matchings successively. Regard these matchings as edge colors \(c\in A\).

Route a demand edge \(ab\) of color \(c\) through the middle vertex \(c\):
\[
a\longrightarrow c\longrightarrow b.
\]
Properness of the coloring gives edge-disjointness. Together with the lower bound,
\[
\boxed{r(k,2)=3\quad\text{for every }k\ge2.}
\]

### 5.2. Bundled permutation masks when \(n=3\)

Let \(\pi:A^2\to A^2\) be any permutation. Consider the mask with \(k\) parallel edges
\[
x\longrightarrow\pi(x)
\]
for each \(x\in A^2\).

Write \(x=(a,b)\) and \(\pi(x)=(c,d)\). Form an auxiliary bipartite multigraph with vertex classes indexed by \(b\) and \(c\), placing one distinguished edge \(e_x\) from \(b\) to \(c\) for every \(x\). It is \(k\)-regular.

Properly edge-color it by
\[
h(x)\in\mathbb Z/k\mathbb Z.
\]
For each of the \(k\) demand copies, indexed by \(p\in\mathbb Z/k\mathbb Z\), put
\[
s=p+h(x)
\]
and use the path word
\[
(a,b,p,s,c,d).
\]

Its four edge windows are
\[
(a,b,p),\qquad(b,p,s),\qquad(p,s,c),\qquad(s,c,d).
\]
Each is a bijective label of the \(k^3\) demands:

- \((a,b,p)\) directly identifies the demand.
- From \((b,p,s)\), the color \(h=s-p\) and vertex \(b\) identify \(e_x\).
- From \((p,s,c)\), the color \(h=s-p\) and vertex \(c\) identify \(e_x\).
- From \((s,c,d)\), the permutation \(\pi\) identifies \(x\), after which \(p=s-h(x)\).

Thus every such mask is routable in five stages, for arbitrary \(k\) and arbitrary, possibly nonlinear, \(\pi\).

This does **not** establish \(r(k,3)=5\) for arbitrary masks.

## 6. The unresolved step

A general regular mask need not admit the affine parametrization used above. The affine proof relies essentially on vector-space intersections and the two-flag basis lemma; it does not provide middle-word labels satisfying all window conditions for an arbitrary mask.

Therefore the general assertion
\[
r(k,n)\le2n-1
\]
remains unproved here. The sharp affine-mask theorem and the bundled \(n=3\) construction are restricted results, not a resolution of the Shuffle-Exchange Conjecture.