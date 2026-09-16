```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The outward orientation of the ten-vertex spider with leg lengths 2, 3, and 4 is tournament anti-Sidorenko, as certified by an explicit nonnegative identity.",
  "would_publish": false,
  "caveats": "The general conjecture remains unsettled; novelty and the precise meaning of the catalog's named '2-3-4 tree' have not been independently checked."
}
```

## 1. A concrete special case

Let \(S\) be the tree obtained by identifying one endpoint of three paths of lengths \(2,3,4\). Thus \(S\) has ten vertices and nine edges. Orient every edge **away from the common endpoint**, obtaining an oriented tree \(D\).

I prove that \(D\) is tournament anti-Sidorenko. The proof gives an exact nonnegative certificate, not merely a computational check.

A tournament kernel is a measurable function
\[
W:[0,1]^2\longrightarrow[0,1],
\qquad W(x,y)+W(y,x)=1
\]
almost everywhere. For an oriented graph \(F\), write
\[
t(F,W)=\int_{[0,1]^{V(F)}}\prod_{ij\in E(F)}W(x_i,x_j)\,\prod_i dx_i.
\]

### Theorem
For the orientation \(D\) just described,
\[
t(D,W)\le 2^{-9}
\]
for every tournament kernel \(W\).

More quantitatively, put
\[
u(x)=\int_0^1(2W(x,y)-1)\,dy,
\qquad s=\int_0^1u(x)^2\,dx.
\]
Then
\[
2^9t(D,W)\le 1-\frac74s.
\]
Equality in \(t(D,W)\le 2^{-9}\) holds exactly when \(W\) has outdegree \(1/2\) almost everywhere.

This tree is not a caterpillar: deleting its leaves leaves a vertex of degree three. It also has six vertices of even degree, so it is outside the original special case stated in the question.

## 2. Operator setup

All inner products and integrals below are over \([0,1]\), with real-valued functions.

Let \(A\) be the integral operator with kernel
\[
A(x,y)=2W(x,y)-1.
\]
Let \(Jf=(\int f)\mathbf 1\), and put
\[
K=J+A.
\]
Thus \(K\) has kernel \(2W\). Antisymmetry gives
\[
A^*=-A,\qquad K^*=J-A.
\]
Both \(K\) and \(K^*\) preserve nonnegative functions.

Define
\[
u=A\mathbf1,\qquad v=A^2\mathbf1,\qquad w=A^3\mathbf1,
\]
and
\[
s=\|u\|_2^2,\qquad q=\|v\|_2^2,\qquad r=\|w\|_2^2.
\]
Skew-adjointness gives
\[
\int u=0,\qquad \int v=-s,\qquad \int w=0,
\]
and
\[
\langle u,v\rangle=\langle v,w\rangle=0,
\qquad
\langle u,w\rangle=-q.
\tag{1}
\]

Now set
\[
p=K^2\mathbf1=1+u+v,\qquad
f=p-1=u+v,\qquad
h=Ap=u+v+w.
\]
Writing
\[
a=\int p=1-s,
\]
we have
\[
Kp=a+h.
\]
Also,
\[
b=\int Kp=1-2s.
\]
Finally, put
\[
g=A(Kp),
\qquad K^2p=b+g.
\]

Because \(Kp\ge0\) and both \(K,K^*\) preserve nonnegativity,
\[
b+g=K(Kp)\ge0,\qquad b-g=K^*(Kp)\ge0.
\tag{2}
\]

The identities in (1) imply
\[
\|f\|_2^2=s+q,\qquad
\|h\|_2^2=s-q+r,\qquad
\langle h,u\rangle=s-q.
\tag{3}
\]
In particular,
\[
\|h\|_2^2-\langle h,u\rangle=r,
\qquad
\|f\|_2^2+\|h\|_2^2=2s+r.
\tag{4}
\]

## 3. An exact identity for the spider density

Conditioning on the common endpoint of the three paths gives
\[
Z:=2^9t(D,W)
 =\int (K^2\mathbf1)(K^3\mathbf1)(K^4\mathbf1)
 =\int p(a+h)(b+g).
\tag{5}
\]

We first simplify this expression using skew-adjointness. Since \(h=Ap\),
\[
\int ph=\langle p,Ap\rangle=0.
\]
Moreover,
\[
\int pg
=\langle p,A(Kp)\rangle
=-\langle Ap,Kp\rangle
=-a\int h-\|h\|_2^2.
\]
As \(b=a+\int h\), expanding (5) therefore yields
\[
Z=a^3-a\|h\|_2^2+\int phg.
\tag{6}
\]

Since \(p=1+f\) and
\[
g=A(a+h)=au+Ah,
\]
we have
\[
\int phg
=\langle h,g\rangle+\int fhg
=a\langle h,u\rangle+\int fhg.
\]
Using (4) in (6), we obtain the particularly simple identity
\[
\boxed{\displaystyle
Z=a^3-ar+\int fhg.
}
\tag{7}
\]

## 4. The nonnegative certificate

Define
\[
L=\frac14\int
\left[
(b+g)(f-h)^2+(b-g)(f+h)^2
\right].
\tag{8}
\]
By (2), every integrand in (8) is nonnegative, so \(L\ge0\).

Expanding the squares and using (4),
\[
\begin{aligned}
L
&=\frac b2\bigl(\|f\|_2^2+\|h\|_2^2\bigr)-\int fhg\\
&=b\left(s+\frac r2\right)-\int fhg.
\end{aligned}
\]
Substituting this into (7), and observing that \(a-b/2=1/2\), gives
\[
Z=a^3+bs-\frac r2-L.
\]
Consequently,
\[
\begin{aligned}
1-Z
&=1-(1-s)^3-(1-2s)s+\frac r2+L\\
&=2s-s^2+s^3+\frac r2+L.
\end{aligned}
\]
Thus we have the exact certificate
\[
\boxed{\displaystyle
1-2^9t(D,W)
=
s\left(\left(s-\frac12\right)^2+\frac74\right)
+\frac12\|A^3\mathbf1\|_2^2
+\frac14\int
\left[
(b+g)(f-h)^2+(b-g)(f+h)^2
\right].
}
\tag{9}
\]

Every term on the right is nonnegative. This proves
\[
2^9t(D,W)\le1-\frac74s\le1.
\]

If equality holds in the anti-Sidorenko inequality, (9) forces \(s=0\), hence \(A\mathbf1=0\). Conversely, if \(A\mathbf1=0\), then \(K\mathbf1=\mathbf1\), so all three path messages in (5) equal \(1\), and equality holds. This completes the theorem.

## 5. Passage to finite tournaments

Let \(T\) be an \(n\)-vertex tournament. Partition \([0,1]\) into \(n\) equal intervals. Define \(W_T\) using the adjacency matrix of \(T\) on distinct intervals and set \(W_T=1/2\) on each diagonal block.

This is a tournament kernel. The kernel obtained by instead putting zero on the diagonal blocks represents ordinary homomorphisms into \(T\), and is pointwise at most \(W_T\). Hence
\[
\frac{\operatorname{hom}(D,T)}{n^{10}}
\le t(D,W_T)\le 2^{-9}.
\]
Therefore
\[
\operatorname{hom}(D,T)\le 2^{-9}n^{10},
\]
the tournament anti-Sidorenko bound. It also implies the usual asymptotic injective-copy formulation.

## 6. An infinite extension family

The special case above extends under the following elementary operation.

### Grafting lemma
Let \(F\) have a tournament anti-Sidorenko orientation. At any vertex of \(F\), identify the root of a rooted tree \(R\) in which **every vertex has an even number of children**. The resulting tree also has a tournament anti-Sidorenko orientation.

#### Proof
At each vertex of \(R\), orient half its child-edges outward and half inward. Let \(F_x\) denote the normalized conditional density of a rooted descendant subtree, with its root fixed at \(x\).

Inductively, \(0\le F_x\le1\). Indeed, the assertion is immediate for a leaf. At a vertex with \(2k\) children, assuming it for the child subtrees, positivity of \(K,K^*\) gives
\[
F_x\le
(K\mathbf1(x))^k(K^*\mathbf1(x))^k
=(1+u(x))^k(1-u(x))^k
=(1-u(x)^2)^k\le1.
\]
Integrating the new vertices therefore multiplies the original nonnegative density integrand by a factor at most \(1\). ∎

Applying this lemma to \(D\) produces infinitely many further non-caterpillar examples.

## 7. Scope and remaining gap

The argument proves a specific non-caterpillar case, and a family obtained from it by grafting. It does **not** prove the conjecture for arbitrary trees.

The key algebraic feature is that the three branch messages are consecutive iterates
\[
K^2\mathbf1,\quad K^3\mathbf1,\quad K^4\mathbf1.
\]
This permits the cancellations in (7) and the nonnegative identity (9). No analogous certificate for arbitrary collections of branch messages is established here.

The explicit tree proved above is the spider with leg lengths \(2,3,4\). I have not independently checked whether this is exactly the tree called the “2-3-4 tree” in the follow-up mentioned in the supplied catalog, or whether this special-case inequality already appears elsewhere.