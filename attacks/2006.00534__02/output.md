```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There are infinitely many finite abelian groups with solid non-maximal-supplement sets of size \u00281+o\u00281\u0029\u0029|G|^{1/4}, so the fourth-root exponent in Theorem 5 is optimal, while its logarithmic factor remains unresolved.",
  "would_publish": false,
  "caveats": "This leaves a factor \u0028log |G|\u0029^{1/4} between the known guarantee and the obstruction, and novelty beyond the supplied literature search was not independently checked."
}
```

## 1. Statement of the partial result

I use the definitions from the source paper:

- \(C\) is a supplement to \(W\) if the addition map
  \[
  C\times W\longrightarrow G,\qquad (c,w)\mapsto c+w
  \]
  is injective.
- It is a maximal supplement if it is not properly contained in another supplement to the same \(W\).
- \(C\) is solid if no proper superset \(C'\supsetneq C\) satisfies
  \(C'-C'=C-C\).

The construction below proves the following.

**Proposition.** There are infinitely many integers \(N\), finite abelian groups \(G\) of order \(N\), and solid subsets \(C\subseteq G\) such that \(C\) is not a maximal supplement for any \(W\subseteq G\), while
\[
|C|=(1+o(1))N^{1/4}.
\]

Consequently, if \(F(N)\) denotes the largest universal threshold such that every nonempty solid \(C\) of size at most \(F(N)\) is a maximal supplement in every abelian group of order \(N\), then along an infinite sequence
\[
F(N)\le (1+o(1))N^{1/4}.
\]
Together with Theorem 5, this leaves
\[
\left(\frac{N}{\log N}\right)^{1/4}
\ \ll\ F(N)\ \le\ (1+o(1))N^{1/4}
\]
in the relevant universal sense. Thus the exponent \(1/4\) is sharp; only the logarithmic factor, and possibly constants, remain open.

## 2. Two elementary characterizations

Let \(C,W\) be nonempty subsets of a finite abelian group \(G\).

### Supplement criterion

The pair \(C,W\) has unique sums if and only if
\[
(C-C)\cap(W-W)=\{0\}. \tag{1}
\]
Indeed, a nontrivial equality \(c+w=c'+w'\) is equivalent to
\(c-c'=w'-w\ne0\).

Moreover, assuming (1), \(C\) is maximal as a supplement to \(W\) if and only if
\[
G=C+(W-W). \tag{2}
\]
For \(x\notin C\), adjoining \(x\) destroys uniqueness precisely when there are
\(c\in C\) and \(w,w'\in W\) such that
\[
x+w=c+w',
\]
or equivalently \(x-c=w'-w\in W-W\). Thus every \(x\notin C\) is blocked exactly when (2) holds.

### Solidity criterion

A set \(C\) is solid if and only if
\[
\forall x\notin C\quad \exists c\in C
\quad\text{such that}\quad x-c\notin C-C. \tag{3}
\]
If (3) fails for some \(x\), then both \(x-C\) and \(C-x\) lie in \(C-C\), so
\[
(C\cup\{x\})-(C\cup\{x\})=C-C.
\]
Conversely, any proper superset with the same difference set supplies such an \(x\).

## 3. A general obstruction construction

Let \(K\) be a finite abelian group and let \(A\subseteq K\) satisfy

\[
A-A=K,\qquad \operatorname{Stab}(A)=\{0\}, \tag{4}
\]
where
\[
\operatorname{Stab}(A)=\{u\in K:A+u=A\}.
\]
Assume \(0\in A\).

Let \(s\ge4\) be an integer with
\[
s<|K\setminus A|. \tag{5}
\]
Put \(L=\mathbb Z_s\), write \(e=1\in L\), and define
\[
G=K\times L,\qquad
C=(A\times\{0\})\cup\{(0,e)\}. \tag{6}
\]

### Lemma 1: \(C\) is solid

From \(A-A=K\),
\[
C-C=
(K\times\{0\})
\cup((-A)\times\{e\})
\cup(A\times\{-e\}). \tag{7}
\]

Let \(x=(u,j)\notin C\).

- If \(j=0\), then \(u\notin A\), and
  \[
  x-(0,e)=(u,-e)\notin C-C.
  \]
- If \(j=e\), then \(u\ne0\). If \(u-a\in-A\) for every \(a\in A\), then
  \(u-A=-A\), hence \(A-u=A\), contradicting the trivial stabilizer in (4).
  Thus some \(a\in A\) satisfies
  \[
  x-(a,0)=(u-a,e)\notin C-C.
  \]
- If \(j=-e\), then
  \[
  x-(0,e)=(u,-2e)\notin C-C,
  \]
  since \(s\ge4\) makes \(-2e\notin\{0,e,-e\}\).
- If \(j\notin\{0,e,-e\}\), then for any \(a\in A\),
  \[
  x-(a,0)
  \]
  has second coordinate \(j\), whereas every element of \(C-C\) has second
  coordinate \(0,e\), or \(-e\).

Thus (3) holds, so \(C\) is solid.

### Lemma 2: \(C\) is not a maximal supplement

Suppose, for contradiction, that \(C\) is a maximal supplement to some \(W\).

Because \(K\times\{0\}\subseteq C-C\), criterion (1) implies that the projection
\[
\pi_L:W\longrightarrow L
\]
is injective: two distinct elements of \(W\) with the same \(L\)-coordinate would have a nonzero difference in \(K\times\{0\}\).

For every \(u\in K\setminus A\), let \(x_u=(u,0)\). By maximality and (2),
\[
x_u\in C+(W-W).
\]
It cannot be represented using a point \((a,0)\in A\times\{0\}\), because then
\[
(u-a,0)\in W-W;
\]
injectivity of \(\pi_L\) forces every \(W-W\) element with second coordinate zero to be zero, which would give \(u=a\in A\). Hence the representation must use \((0,e)\), and therefore
\[
(u,-e)\in W-W
\qquad\text{for every }u\in K\setminus A. \tag{8}
\]

On the other hand, because \(\pi_L\) is injective, for each \(\ell\in L\) there is at most one ordered pair \(w,w'\in W\) with
\[
\pi_L(w')=\ell,\qquad \pi_L(w)=\ell-e.
\]
Consequently,
\[
\bigl|(W-W)\cap(K\times\{-e\})\bigr|\le |L|=s. \tag{9}
\]
Equations (8) and (9) imply \(|K\setminus A|\le s\), contrary to (5).

Thus \(C\) is solid but is not a maximal supplement for any \(W\).

## 4. An asymptotically optimal difference basis

It remains to choose \(K,A\) with \(|A|=(1+o(1))\sqrt{|K|}\).

Let \(\ell\) range over odd primes, put \(q=\ell^2\), and work in the field
\(\mathbb F_q\). Choose \(\alpha\in\mathbb F_q\setminus\mathbb F_\ell\), and set
\[
B=\mathbb F_\ell\cup\alpha\mathbb F_\ell.
\]
Then
\[
|B|=2\ell-1,\qquad B-B=\mathbb F_q. \tag{10}
\]
Indeed, every \(z=u+\alpha v\), with \(u,v\in\mathbb F_\ell\), can be written as
\[
z=u-(-\alpha v)
\]
with both terms in \(B\).

Let
\[
K=(\mathbb F_q^2,+),
\]
and define
\[
P=\{(t,t^2):t\in\mathbb F_q\},\qquad
A=P\cup(\{0\}\times B). \tag{11}
\]
Then
\[
|A|=q+2\ell-2. \tag{12}
\]

We claim \(A-A=K\). If \((d,b)\in\mathbb F_q^2\) has \(d\ne0\), choose
\[
t=\frac{b/d+d}{2},\qquad r=\frac{b/d-d}{2}.
\]
Since the characteristic is odd,
\[
t-r=d,\qquad t^2-r^2=(t-r)(t+r)=b,
\]
so \((d,b)\in P-P\). If \(d=0\), equation (10) gives
\((0,b)\in(\{0\}\times B)-(\{0\}\times B)\). Hence \(A-A=K\).

Also \(A\) has trivial stabilizer. Under projection onto the first coordinate, the fiber over \(0\) has size \(2\ell-1\), whereas every nonzero fiber has size one. A translation preserving \(A\) must therefore have first coordinate zero. It must then preserve the unique point \((x,x^2)\) in any nonzero fiber, forcing its second coordinate to be zero.

Now put
\[
s=q^2-|A|-1=q^2-q-2\ell+1.
\]
For \(\ell\ge3\), we have \(s\ge4\), and
\[
s<|K\setminus A|=q^2-q-2\ell+2.
\]
The construction of the preceding section therefore applies.

The resulting group and solid set have
\[
|G|=q^2s
\]
and
\[
|C|=|A|+1=q+2\ell-1.
\]
Since \(q=\ell^2\) and \(s=(1-o(1))q^2\),
\[
|G|=(1-o(1))q^4
\]
and hence
\[
\frac{|C|}{|G|^{1/4}}
=
\frac{q+2\ell-1}{q\,(s/q^2)^{1/4}}
\longrightarrow 1.
\]

Thus
\[
|C|=(1+o(1))|G|^{1/4},
\]
while \(C\) is solid and is not a maximal supplement.

## 5. What remains open

This construction rules out every proposed universal threshold of order
\(\omega(|G|^{1/4})\). It therefore shows that the fourth-root exponent in Theorem 5 is not an artifact.

It does not determine whether the logarithmic loss in Theorem 5 is necessary. The remaining possibilities include, for example:

\[
F(N)=\Theta(N^{1/4})
\]
or
\[
F(N)=\Theta\!\left((N/\log N)^{1/4}\right),
\]
as well as intermediate logarithmic behavior. No argument above distinguishes these possibilities.