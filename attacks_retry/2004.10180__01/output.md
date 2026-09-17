```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An induced-matching reformulation gives a polynomial saving in every fixed-characteristic vector-space analogue, but not an unconditional saving for subsets of [n].",
  "would_publish": false,
  "caveats": "The integer problem remains unresolved; the saving is not uniform in the characteristic, and no novelty claim is made for the finite-field result."
}
```

## 1. Statement and scope

Call a set \(A\) **admissible** if every solution in \(A^5\) of
\[
x_1+x_2+2x_3=x_4+3x_5                                      \tag{1}
\]
has one of the forms
\[
x_1=x_4,\qquad x_2=x_3=x_5,                                \tag{T1}
\]
or
\[
x_2=x_4,\qquad x_1=x_3=x_5.                                \tag{T2}
\]
These are precisely the trivial patterns associated with the zero-sum partitions of the coefficient sequence \((1,1,2,-1,-3)\).

The question is whether there is an absolute \(\varepsilon>0\) such that every admissible \(A\subseteq[n]\) satisfies
\[
|A|=O(n^{1/2-\varepsilon}).
\]
I do not prove this.

The main partial result below is a polynomial bound for the corresponding problem in vector spaces of fixed characteristic.

### Theorem 1
Let \(p\ge5\) be prime and put
\[
\eta_p=\frac{1}{36(p-1)^2\log p}.
\]
For every \(d\ge1\), an admissible set \(A\subseteq\mathbb F_p^d\) satisfies
\[
|A|\le 2\sqrt2\,(p^d)^{1/2-\eta_p}.                         \tag{2}
\]

Consequently, the desired polynomial bound holds for integer sets having an order-\(4\) Freiman model in a fixed-characteristic vector space of size \(O(n)\). That is a genuine additional hypothesis, not something established here for arbitrary admissible sets.

The argument uses an induced matching hidden in (1), followed by a polynomial rank estimate. It does not rely on the previous attempt’s moment-curve construction or Fourier estimate.

## 2. The induced matching hidden in the equation

The following observations hold in any abelian group, with admissibility defined by (T1) and (T2).

First, the Sidon consequence from the previous attempt is valid: if
\[
a+b=c+d,
\]
then \((a,b,d,c,d)\) solves (1), and its triviality gives
\(\{a,b\}=\{c,d\}\) as multisets. The rank argument below uses stronger consequences.

### Lemma 2
Suppose \(A\) is admissible and \(m=|A|\). Both maps
\[
(a,b)\longmapsto b+2a,\qquad
(a,b)\longmapsto b+3a                                      \tag{3}
\]
are injective on \(A^2\).

Define
\[
Y=\{b+2a:a,b\in A,\ a\ne b\},\qquad
Z=\{b+3a:a,b\in A\}.
\]
In the bipartite graph on \(Y\sqcup Z\), join \(y\) to \(z\) when \(z-y\in A\). Then its edges are exactly
\[
b+2a\ \sim\ b+3a
\qquad(a,b\in A,\ a\ne b).                                  \tag{4}
\]
Thus the graph is a matching of size \(m(m-1)\), together with \(m\) isolated vertices in \(Z\). Each difference-label \(a\in A\) occurs on exactly \(m-1\) edges.

#### Proof

An equality
\[
b+2a=d+2c
\]
gives the solution
\[
(x_1,x_2,x_3,x_4,x_5)=(c,b,a,d,c).
\]
Either trivial pattern forces \(a=c\) and \(b=d\).

Similarly, an equality
\[
b+3a=d+3c
\]
gives the solution
\[
(a,b,a,d,c),
\]
whose triviality again forces \(a=c\) and \(b=d\). This proves injectivity.

Now let \(a\ne b\), and suppose
\[
x+(b+2a)=d+3c,\qquad x,a,b,c,d\in A.                         \tag{5}
\]
The corresponding solution of (1) is \((x,b,a,d,c)\). Pattern (T1) would require \(b=a\), which is excluded. Pattern (T2) gives
\[
x=a=c,\qquad b=d.
\]
Conversely, these equalities certainly give (5). Injectivity of the two maps in (3) proves the matching description. ∎

This has an exact linear-algebraic consequence.

### Corollary 3
Let \(K\) be any field and let \(h:A\to K\). Form the \(Y\times Z\) matrix
\[
M_h(y,z)=
\begin{cases}
h(z-y),&z-y\in A,\\
0,&z-y\notin A.
\end{cases}
\]
Then
\[
\operatorname{rank}_K M_h=(m-1)|\operatorname{supp}h|.       \tag{6}
\]

#### Proof

By Lemma 2, after reordering rows and columns, the nonzero part of the matrix consists of the blocks
\[
h(a)I_{m-1},\qquad a\in A,
\]
and there are \(m\) additional zero columns. Each block with \(h(a)\ne0\) has rank \(m-1\). ∎

In particular, there is no issue when the characteristic divides \(m-1\): the factor \(m-1\) counts independent diagonal entries.

## 3. A polynomial rank bound

We now work in \(\mathbb F_p^d\), where \(p\ge5\).

For a real number \(u\ge0\), write
\[
N_p(d,u)=
\#\left\{\alpha\in\{0,1,\ldots,p-1\}^d:
                   \alpha_1+\cdots+\alpha_d\le u\right\}.
\]

### Lemma 4
Let \(A\subseteq\mathbb F_p^d\) be admissible, with \(m=|A|\). Suppose \(s,t\ge0\) satisfy
\[
s+2t=(p-1)d,
\]
and put
\[
K=N_p(d,s),\qquad L=N_p(d,t).
\]
If \(m>K\), then
\[
(m-1)(m-K)\le 2L.                                          \tag{7}
\]

#### Proof

For \(X,Y,Z\in\mathbb F_p^d\), consider
\[
P(X,Y,Z)=
\prod_{j=1}^d\left(1-(X_j+Y_j-Z_j)^{p-1}\right).
\]
As a function on \((\mathbb F_p^d)^3\),
\[
P(x,y,z)=1_{x+y=z}.                                        \tag{8}
\]

Its total degree is at most \((p-1)d\), and every individual coordinate has degree at most \(p-1\). Every monomial therefore has either

- total \(X\)-degree at most \(s\);
- total \(Y\)-degree at most \(t\); or
- total \(Z\)-degree at most \(t\).

Indeed, otherwise its total degree would exceed \(s+2t\). Assigning each monomial to one eligible class gives a decomposition
\[
P(X,Y,Z)
=
\sum_{|\alpha|\le s}X^\alpha P_\alpha(Y,Z)
+\sum_{|\beta|\le t}Y^\beta Q_\beta(X,Z)
+\sum_{|\gamma|\le t}Z^\gamma R_\gamma(X,Y),                 \tag{9}
\]
where the three sums have at most \(K,L,L\) terms, respectively.

Choose \(h:A\to\mathbb F_p\) satisfying
\[
\sum_{x\in A}h(x)x^\alpha=0
\qquad\text{for every }\alpha\in\{0,\ldots,p-1\}^d
\text{ with }|\alpha|\le s.                                \tag{10}
\]
The space of such functions has dimension at least \(m-K\). It contains a function with
\[
|\operatorname{supp}h|\ge m-K.                             \tag{11}
\]
To justify this over a finite field, let the solution space have dimension \(r\). There are \(r\) coordinates on which restriction is an isomorphism onto \(\mathbb F_p^r\); prescribe the value \(1\) on all those coordinates.

Multiply (9) by \(h(x)\) and sum over \(x\in A\), restricting \(y\in Y\) and \(z\in Z\), where \(Y,Z\) are from Lemma 2. By (8), the resulting matrix is \(M_h\). The first sum disappears by (10). Each term from the second or third sum is a rank-at-most-one matrix. Hence
\[
\operatorname{rank}M_h\le 2L.
\]
Corollary 3 and (11) give
\[
(m-1)(m-K)\le
(m-1)|\operatorname{supp}h|
=\operatorname{rank}M_h
\le2L.
\]
∎

## 4. Obtaining a strict power saving

Set
\[
s=\frac d3,\qquad
t=\frac{(p-1)d}{2}-\frac d6.
\]
These satisfy \(s+2t=(p-1)d\).

### Bounding \(K\)

Using the generating function at \(1/4\),
\[
\begin{aligned}
K
&\le
4^{d/3}\left(1+\frac14+\cdots+\frac1{4^{p-1}}\right)^d\\
&\le
\left(\frac43\,4^{1/3}\right)^d.
\end{aligned}                                               \tag{12}
\]
Put
\[
\kappa=\frac43\,4^{1/3}.
\]

### Bounding \(L\)

Let \(U_1,\ldots,U_d\) be independent and uniform on
\(\{0,1,\ldots,p-1\}\). Then
\[
\frac{L}{p^d}
=
\Pr\left(
\sum_{j=1}^d U_j
\le \frac{(p-1)d}{2}-\frac d6
\right).
\]
The elementary bounded-variable exponential estimate gives
\[
L\le p^d\exp\left(-\frac{d}{18(p-1)^2}\right).              \tag{13}
\]

For completeness, write \(R=p-1\). Convexity and
\(\mathbb E(U_j-R/2)=0\) give
\[
\mathbb E e^{-\lambda(U_j-R/2)}
\le \cosh(\lambda R/2)
\le e^{\lambda^2R^2/8}.
\]
Markov's inequality, with \(\lambda=2/(3R^2)\), yields (13).

Define
\[
B_p=\sqrt p\exp\left(-\frac{1}{36(p-1)^2}\right).
\]
Then
\[
L\le B_p^{2d}.
\]
Also, for \(p\ge5\),
\[
\kappa<\frac{11}{5}
<\sqrt5\,e^{-1/576}
\le B_p,
\]
so (12) gives
\[
K\le B_p^d.                                                \tag{14}
\]

If \(m<2K\), then \(m<2B_p^d\). Otherwise \(m\ge2K\ge2\), and Lemma 4 yields
\[
\frac{m^2}{4}
\le (m-1)(m-K)
\le2L.
\]
Thus in either case
\[
m\le2\sqrt2\,B_p^d.
\]
Finally,
\[
B_p^d
=(p^d)^{1/2-\eta_p},
\qquad
\eta_p=\frac{1}{36(p-1)^2\log p}.
\]
This proves Theorem 1, including the cases \(m=0,1\).

For the same admissibility convention, characteristics \(2\) and \(3\) are even simpler: injectivity of \(b+2a\), respectively \(b+3a\), forces \(m\le1\).

## 5. A precise integer subclass—and the remaining gap

An injective map
\[
\phi:A\longrightarrow\mathbb F_p^d
\]
is an **order-\(4\) Freiman isomorphism** if it preserves, in both directions, all equalities
\[
a_1+a_2+a_3+a_4=b_1+b_2+b_3+b_4,
\]
with repetitions allowed.

### Corollary 5
Fix \(p\ge5\) and \(C>0\). Suppose an admissible set \(A\subseteq[n]\) has an order-\(4\) Freiman isomorphism into \(\mathbb F_p^d\), where
\[
p^d\le Cn.
\]
Then
\[
|A|=O_{p,C}\bigl(n^{1/2-\eta_p}\bigr).                      \tag{15}
\]

#### Proof

Equation (1) is an equality between two four-term sums:
\[
x_1+x_2+x_3+x_3=x_4+x_5+x_5+x_5.
\]
Therefore \(\phi(A)\) is admissible. Apply Theorem 1 and \(p^d\le Cn\). ∎

This identifies a setting in which a polynomial gain really does hold. It does **not** establish that arbitrary admissible integer sets have such models.

There are two specific transfer gaps:

1. **Reduction modulo a large prime gives no fixed saving.**  
   Taking \(p>4n\) faithfully models the relevant equation in \(\mathbb F_p\), but here \(d=1\) and
   \[
   \eta_p\longrightarrow0.
   \]
   The resulting estimate is only
   \[
   |A|\le2\sqrt2\,\sqrt p\,
          \exp\left(-\frac{1}{36(p-1)^2}\right),
   \]
   not a power improvement in \(n\).

2. **Base-\(p\) digits do not automatically give a Freiman model.**  
   For fixed \(p\), coordinatewise equations modulo \(p\) can arise from nonzero digit discrepancies divisible by \(p\). Conversely, integer equations can involve carries. Thus the ordinary digit map into \(\mathbb F_p^d\) does not justify applying Theorem 1 to an arbitrary \(A\subseteq[n]\).

Accordingly, the unconditional numerical bound for integer sets is not improved here beyond the \(o(\sqrt n)\) bound supplied in the question. The verified progress is the induced-matching/rank formulation and its polynomial consequence in fixed characteristic; the growing-characteristic or carry-sensitive case remains uncovered.