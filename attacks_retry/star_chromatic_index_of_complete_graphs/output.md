```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The 3n-O(1) packing lower bound is valid, and star colorings refining the Boolean one-factorization necessarily use superlinearly many colors.",
  "would_publish": false,
  "caveats": "Unrestricted linearity is not resolved; novelty and current literature status have not been independently checked."
}
```

## 1. Results and scope

Write \(s(n)=\chi_s'(K_n)\). I establish two partial results:

1. The packing argument in the previous attempt survives verification and gives
   \[
   \boxed{
   s(n)\ge
   \left\lceil
   \frac{3\binom n2}{\lfloor n/2\rfloor+2}
   \right\rceil
   =3n-O(1).
   }
   \]
   This is stronger than the lower bound quoted in the question, though I make no novelty claim.

2. There is an obstruction to a natural family of potential linear constructions. On \(N=2^d\) vertices labelled by \(\mathbb F_2^d\), consider the standard one-factorization in which the edge \(xy\) has base color \(x+y\). **Every star coloring obtained by splitting these base color classes uses \(\omega(N)\) colors.**

   The second statement concerns total colors, not just the maximum number of pieces into which one factor must be split. In fact, for each fixed \(r\), all but \(o(N)\) of the factors must be split into more than \(r\) colors.

The unrestricted conjecture remains undecided by these arguments.

---

## 2. Verification of the packing lower bound

### Packing characterization

Let a proper edge-coloring of a simple graph have nonempty color classes
\[
M_1,\ldots,M_k.
\]
Each \(M_i\) is a matching. For every unordered pair of edges \(e,f\in M_i\), form the four-element support
\[
B(e,f)=V(e)\cup V(f).
\]
These supports form an **indexed collection**: distinct pairs of edges remain distinct members even when their supports coincide.

**Lemma 1.** The coloring is a star edge-coloring if and only if every three-element vertex set is contained in at most one member of this indexed collection.

**Proof.**
Suppose two distinct members contain the same triple. They cannot arise from the same matching: supports of two distinct pairs of edges from one matching intersect in zero or two vertices.

Thus the two members arise from two edges of color \(a\) and two edges of a different color \(b\). These four distinct edges have a union on either four or five vertices.

- On four vertices, their union is a properly bichromatic \(4\)-cycle.
- On five vertices, three vertices have degree two and two have degree one. The union has maximum degree two and no odd cycle. An even cycle is also impossible, since only three vertices have degree two. Hence the union is a four-edge path.

Either configuration violates the star condition.

Conversely, the two same-colored edge pairs of a bichromatic four-edge path have supports sharing its three internal vertices. For a bichromatic \(4\)-cycle, the supports coincide. Either configuration violates the packing property. ∎

The indexing is essential for the \(4\)-cycle case.

### Counting

Now consider a star edge-coloring of \(K_n\). Put
\[
E=\binom n2,\qquad m_i=|M_i|,\qquad
B=\sum_{i=1}^k\binom{m_i}{2}.
\]
Then
\[
\sum_i m_i=E.
\]

Fix a vertex pair \(\{x,y\}\). The blocks containing this pair have pairwise disjoint sets of remaining vertices; otherwise two blocks would share a triple. Consequently, their number is at most
\[
\left\lfloor\frac{n-2}{2}\right\rfloor.
\]
Each block contains six vertex pairs, so
\[
6B\le E\left\lfloor\frac{n-2}{2}\right\rfloor.
\]
Therefore
\[
\begin{aligned}
\sum_i m_i^2
&=E+2B\\
&\le E\left(1+\frac13\left\lfloor\frac{n-2}{2}\right\rfloor\right)\\
&=\frac E3\bigl(\lfloor n/2\rfloor+2\bigr).
\end{aligned}
\]
Cauchy–Schwarz now gives
\[
E^2\le k\sum_i m_i^2
\le \frac{kE}{3}\bigl(\lfloor n/2\rfloor+2\bigr),
\]
which proves
\[
s(n)\ge
\left\lceil
\frac{3\binom n2}{\lfloor n/2\rfloor+2}
\right\rceil.
\]

Thus the earlier packing lead is correct. Its limitation is that it still provides only a constant-times-\(n\) lower bound.

---

## 3. A superlinear obstruction for Boolean refinements

Let
\[
G=\mathbb F_2^d,\qquad N=|G|=2^d.
\]
For each \(a\in G\setminus\{0\}\), define the perfect matching
\[
M_a=\bigl\{\{x,x+a\}:x\in G\bigr\}.
\]
Here repeated descriptions of the same edge are identified. These \(N-1\) matchings partition \(E(K_N)\).

A **Boolean refinement** is an edge-coloring in which every color class is contained in some \(M_a\). Let \(r_a\) be the number of nonempty colors used to split \(M_a\), so its total number of colors is
\[
k=\sum_{a\ne0}r_a.
\]

Let \(f_\oplus(N)\) be the minimum number of colors in a star Boolean refinement.

**Theorem 2.**
\[
\boxed{
\frac{f_\oplus(2^d)}{2^d}\longrightarrow\infty
\qquad(d\to\infty).
}
\]

Notice that a Boolean refinement cannot have a bichromatic four-edge path at all: if its successive base colors are \(a,b,a,b\), its final vertex equals its initial vertex. Thus, within this family, the obstruction is entirely bichromatic \(4\)-cycles.

The proof uses the established finite Hales–Jewett theorem and an elementary affine-flat counting lemma.

### 3.1. Hales–Jewett forces a forbidden square

For an integer \(r\ge1\), let \(h(r)\) be a dimension supplied by the finite Hales–Jewett theorem for an alphabet of size four and \(r\) colors.

The precise form used is this: every \(r\)-coloring of
\[
\bigl(\{0,1\}^2\bigr)^{h(r)}
\]
has a monochromatic combinatorial line. Such a line is obtained by fixing coordinates outside a nonempty set \(I\), and putting the same symbol \(s\in\{0,1\}^2\) into all coordinates in \(I\), for each of the four choices of \(s\).

Define the set of lightly split directions
\[
A_r=\{a\in G\setminus\{0\}:r_a\le r\}.
\]

**Lemma 3.** In a star Boolean refinement, \(A_r\) contains no affine subspace of dimension \(h(r)\).

**Proof.**
Suppose
\[
t+H\subseteq A_r,\qquad \dim H=h(r).
\]
Because \(0\notin A_r\), we have \(t\notin H\), so \(H\) and \(t+H\) are disjoint vertex sets.

Every edge between \(H\) and \(t+H\) has base color in \(t+H\):
\[
x+(t+y)=t+x+y\in t+H.
\]
For each such base color, label its refined colors by distinct members of \(\{1,\ldots,r\}\). Thus an actual color can be identified by a pair
\[
(\text{base color},\text{label}).
\]

Choose coordinates \(H\cong\mathbb F_2^{h(r)}\). Label each pair \((x,y)\in H\times H\) by the label of the edge
\[
\{x,t+y\}.
\]
Identify \(H\times H\) with words over the four-symbol alphabet \(\{0,1\}^2\). Hales–Jewett produces \(x,y,w\in H\), with \(w\ne0\), such that the four edges corresponding to
\[
(x,y),\quad(x+w,y),\quad(x,y+w),\quad(x+w,y+w)
\]
all have one label, say \(j\).

These edges form a \(4\)-cycle between
\[
\{x,x+w\}\subseteq H
\quad\text{and}\quad
\{t+y,t+y+w\}\subseteq t+H.
\]
One opposite pair has actual color
\[
(t+x+y,j),
\]
and the other opposite pair has actual color
\[
(t+x+y+w,j).
\]
The two colors are distinct because \(w\ne0\). This is a forbidden bichromatic \(4\)-cycle. ∎

This uses only the ordinary finite Hales–Jewett theorem, not its density version.

### 3.2. An elementary bound for affine-flat-free sets

We need a quantitative form of the fact that a positive-density subset of a large binary vector space contains any fixed-dimensional affine subspace.

**Lemma 4.** Let \(A\subseteq\mathbb F_2^d\), where \(N=2^d\). If \(A\) contains no affine subspace of dimension \(m\ge1\), then
\[
\boxed{
|A|\le
(2^m-1)^{\,2^{1-m}}\,
N^{\,1-2^{1-m}}.
}
\]

**Proof.**
Write \(\delta=|A|/N\), and let \(Q_j\) denote the normalized number of possibly degenerate \(j\)-dimensional cubes in \(A\):
\[
Q_j=
\mathbb E_{x,u_1,\ldots,u_j}
\prod_{\omega\in\mathbb F_2^j}
1_A\!\left(x+\sum_{i=1}^j\omega_i u_i\right).
\]
In particular, \(Q_0=\delta\).

Averaging over the last direction and the base point gives
\[
Q_j=
\mathbb E_{\mathbf u\in G^{j-1}}
\left(
\mathbb E_x
\prod_{\omega\in\mathbb F_2^{j-1}}
1_A(x+\omega\cdot\mathbf u)
\right)^2
\ge Q_{j-1}^2.
\]
Hence
\[
Q_{m-1}\ge \delta^{2^{m-1}}.
\]

Since \(A\) contains no affine \(m\)-flat, every counted \(m\)-cube has linearly dependent directions. There is therefore some nonzero
\[
\lambda\in\mathbb F_2^m
\quad\text{with}\quad
\sum_i\lambda_i u_i=0.
\]
For each fixed nonzero \(\lambda\), eliminate a direction whose coefficient is one. The remaining directions have the same span, so the valid tuples satisfying this relation are in bijection with valid \((m-1)\)-cubes. Taking a union bound over the \(2^m-1\) possible relations yields
\[
N^{m+1}Q_m
\le (2^m-1)N^mQ_{m-1}.
\]
Thus
\[
Q_{m-1}^2\le Q_m
\le \frac{2^m-1}{N}Q_{m-1}.
\]
If \(A\) is nonempty, division gives
\[
\delta^{2^{m-1}}
\le Q_{m-1}
\le \frac{2^m-1}{N}.
\]
Rearranging proves the stated bound. The empty-set case is immediate. ∎

### 3.3. Counting the lightly split factors

Apply Lemma 4 to \(A_r\), using Lemma 3. Set
\[
\varepsilon_r=2^{1-h(r)},\qquad
C_r=(2^{h(r)}-1)^{\varepsilon_r}.
\]
Then every star Boolean refinement satisfies
\[
\boxed{
|A_r|\le C_rN^{1-\varepsilon_r}.
}
\]
In particular, for every fixed \(r\), only \(o(N)\) factors are split into at most \(r\) colors.

Because every factor is nonempty,
\[
\begin{aligned}
k=\sum_{a\ne0}r_a
&\ge |A_r|+(r+1)(N-1-|A_r|)\\
&\ge (r+1)(N-1)-rC_rN^{1-\varepsilon_r}.
\end{aligned}
\]
Consequently, for each fixed \(r\),
\[
\frac{k}{N}\ge r+1-o_r(1).
\]
Since \(r\) is arbitrary, this proves Theorem 2.

The quantitative estimate is extremely weak because \(h(r)\) is a Hales–Jewett parameter, but the conclusion concerns **total** colors and is genuinely superlinear.

---

## 4. Why this does not settle the original problem

The distinction between arbitrary colorings and Boolean refinements is essential. We have
\[
\chi_s'(K_N)\le f_\oplus(N),
\]
not the reverse. Therefore the superlinearity of \(f_\oplus(N)\) does not imply superlinearity of \(\chi_s'(K_N)\).

Nor can every star coloring be made Boolean merely by relabelling its vertices. For example, on vertices \(1,\ldots,7\), use the three double-edge color classes
\[
\{13,24\},\qquad
\{15,26\},\qquad
\{34,57\},
\]
and give every remaining edge its own color. Their supports are
\[
1234,\qquad1256,\qquad3457,
\]
which pairwise intersect in at most two vertices. Lemma 1 therefore verifies that this is a star coloring.

If an injective labelling \(i\mapsto x_i\) into any binary vector space made each of these colors have constant XOR difference, then
\[
x_1+x_3=x_2+x_4,\qquad
x_1+x_5=x_2+x_6,\qquad
x_3+x_4=x_5+x_7.
\]
Adding these equations gives \(x_6=x_7\), contradicting injectivity. Adding vertices with fresh singleton edge colors extends this example to power-of-two orders.

There is nevertheless a useful consequence for prospective constructions:

> An \(O(N)\)-color star coloring cannot have every color class use only a bounded number of XOR differences under a labelling by \(\mathbb F_2^d\).

Indeed, splitting every color further by its XOR difference preserves the star property. A bounded number of differences per color would therefore produce an \(O(N)\)-color Boolean refinement, contrary to Theorem 2.

Thus a linear construction, if one exists, must escape this refinement framework in a substantial way. The unconditional conclusion established here remains
\[
\chi_s'(K_n)\ge 3n-O(1);
\]
neither a general linear upper bound nor a general superlinear lower bound has been proved.