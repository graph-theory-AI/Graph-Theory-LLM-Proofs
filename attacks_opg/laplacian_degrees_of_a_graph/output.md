```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The conjecture is true in full, as the supplied catalog reports, and a self-contained proof is given below.",
  "would_publish": false,
  "caveats": "Finite simple undirected graphs are assumed; no novelty is claimed, and historical attribution follows the supplied catalog."
}
```

## Status and statement

The supplied catalog attributes the resolution to Brouwer and Haemers (2008). I have not independently inspected that publication here. Rather than rely solely on the catalog’s status label, I give a self-contained proof below; I do not claim that this is new or that it reproduces their original argument.

**Theorem.** Let \(G\) be a connected simple graph on \(n\) vertices, with degrees
\[
d_1\ge \cdots\ge d_n
\]
and Laplacian eigenvalues
\[
t_1\ge \cdots\ge t_n=0.
\]
Then
\[
t_k\ge d_k-k+2\qquad(1\le k\le n-1).
\]
Equivalently, \(c_k=t_k+k-2\ge d_k\).

## Proof

The case \(n=1\) is vacuous. Assume \(n\ge2\), fix \(k<n\), and put
\[
d=d_k,\qquad q=d-k+2.
\]
Choose a set \(S\) of \(k\) vertices, each having degree at least \(d\). For a vertex set \(W\), write \(L[W]\) for the corresponding principal submatrix of \(L\), retaining the degrees in \(G\) on its diagonal.

We use the positive-semidefinite order \(\succeq\). Recall that
\[
x^{\mathsf T}Lx=\sum_{uv\in E(G)}(x_u-x_v)^2\ge0,
\]
and, because \(G\) is connected, \(\ker L=\operatorname{span}\{\mathbf1\}\).

### A preliminary observation

For every nonempty proper subset \(W\subsetneq S\),
\[
\begin{aligned}
L[W]
&=L(G[W])+
  \operatorname{diag}\bigl(d_G(v)-d_{G[W]}(v):v\in W\bigr)\\
&\succeq (d-|W|+1)I
 \succeq qI.
\end{aligned}
\tag{1}
\]
Here simplicity gives \(d_{G[W]}(v)\le |W|-1\).

Consequently, if a nonzero vector \(x\), supported on \(S\), satisfies
\[
x^{\mathsf T}Lx<q\|x\|^2,
\tag{2}
\]
then its coordinates on \(S\) are all nonzero and have the same sign.

Indeed, a zero coordinate would put its support in a proper subset of \(S\), contradicting (1). If \(x\) had both signs, its positive and negative parts would each be supported on a proper subset of \(S\). Each part would satisfy the lower bound in (1), and their cross term in the Laplacian quadratic form is nonnegative, since \(L\) has nonpositive off-diagonal entries. This again contradicts (2).

If \(q\le0\), the required inequality follows immediately from \(L\succeq0\). Since \(q\) is an integer, it remains to consider \(q\ge2\) and \(q=1\).

### Case 1: \(q\ge2\)

Put
\[
r=q-1=d-k+1\ge1.
\]
Suppose, for a contradiction, that \(t_k<q\).

Let \(\mathcal U\) be the span of orthonormal Laplacian eigenvectors corresponding to \(t_k,\ldots,t_n\). Its dimension is \(n-k+1\). The coordinate subspace of vectors supported on \(S\) has dimension \(k\), so these two subspaces have a nonzero intersection. Choose
\[
0\ne x\in\mathcal U,\qquad \operatorname{supp}(x)\subseteq S.
\]
All eigenvalues used in \(\mathcal U\) are less than \(q\), so (2) holds. By the preliminary observation, after replacing \(x\) by \(-x\) if necessary, we have
\[
y:=x|_S>0.
\]

Moreover, \(x\) is not constant because \(S\ne V(G)\). Connectedness therefore gives \(x^{\mathsf T}Lx>0\). Expanding \(x\) in the eigenbasis of \(\mathcal U\), and using \(\lambda^2<q\lambda\) for \(0<\lambda<q\), yields
\[
\|Lx\|^2<q\,x^{\mathsf T}Lx.
\tag{3}
\]

We will obtain the reverse inequality.

For \(v\in S\), let
\[
b_v=|N(v)\setminus S|,\qquad
R=\operatorname{diag}(b_v:v\in S),\qquad
B=L[S].
\]
Since each vertex of \(S\) has at most \(k-1\) neighbours in \(S\),
\[
b_v\ge d-(k-1)=r.
\]
Thus
\[
R\succeq rI,\qquad
B=L(G[S])+R\succeq rI.
\tag{4}
\]

Because \(y\) is nonnegative,
\[
\begin{aligned}
\|Lx\|^2
&=\|By\|^2+
  \sum_{w\notin S}
  \left(\sum_{v\in N(w)\cap S}y_v\right)^2\\
&\ge \|By\|^2+
  \sum_{w\notin S}\sum_{v\in N(w)\cap S}y_v^2\\
&=y^{\mathsf T}(B^2+R)y.
\end{aligned}
\tag{5}
\]

On the other hand,
\[
B^2+R-qB
=(B-I)(B-rI)+(R-rI)\succeq0.
\tag{6}
\]
To justify the last step, every eigenvalue \(\beta\) of \(B\) satisfies \(\beta\ge r\ge1\), so
\[
(\beta-1)(\beta-r)\ge0;
\]
also \(R-rI\succeq0\) by (4).

Combining (5) and (6),
\[
\|Lx\|^2
\ge q\,y^{\mathsf T}By
=q\,x^{\mathsf T}Lx,
\]
contradicting (3). Hence \(t_k\ge q\) in this case.

### Case 2: \(q=1\)

Here \(d=k-1\), and necessarily \(k\ge2\). Let \(H=G[S]\).

If \(H\) is disconnected, each of its vertices has at most \(k-2\) neighbours in \(S\). Since every vertex of \(S\) has degree at least \(k-1\) in \(G\), each has at least one neighbour outside \(S\). Therefore
\[
L[S]\succeq I,
\]
and principal-submatrix interlacing gives \(t_k\ge1\).

We may thus assume that \(H\) is connected. Since \(G\) is connected and \(S\) is proper, choose \(w\notin S\) adjacent to a vertex of \(S\). Consider the \((k+1)\times(k+1)\) matrix
\[
M=L[S\cup\{w\}]-I.
\]
Its off-diagonal entries are nonpositive, and their nonzero pattern is connected. By (1),
\[
M[W]\succeq0
\qquad\text{for every nonempty }W\subsetneq S.
\tag{7}
\]
Also,
\[
M_{ww}=d_G(w)-1\ge0.
\tag{8}
\]

We claim that \(M\) has at most one negative eigenvalue.

Suppose otherwise. By Perron–Frobenius, applied to \(\alpha I-M\) for sufficiently large \(\alpha\), a least-eigenvalue eigenvector of \(M\) is strictly positive, and that eigenvalue is simple. Hence another negative eigenvalue \(\lambda<0\) has an eigenvector \(z\) with both positive and negative coordinates.

At least one of the two sign supports of \(z\) is either a proper subset of \(S\) or the singleton \(\{w\}\). To see this, consider the sign support not containing \(w\). It is contained in \(S\); if it equals all of \(S\), the other sign support must be \(\{w\}\). If \(z_w=0\), both sign supports are proper subsets of \(S\).

Choose such a sign support \(W\). Equations (7) and (8) imply \(M[W]\succeq0\). Multiplying the eigenvalue equations by \(z_i\) and summing over \(i\in W\), we obtain
\[
\lambda\sum_{i\in W}z_i^2
=
z_W^{\mathsf T}M[W]z_W
+
\sum_{\substack{i\in W\\j\notin W}}M_{ij}z_i z_j
\ge0.
\]
The first term is nonnegative. Every summand in the second is also nonnegative: \(M_{ij}\le0\), while \(z_i\) and \(z_j\) have opposite signs or \(z_j=0\). This contradicts \(\lambda<0\), proving the claim.

Thus at least \(k\) eigenvalues of \(M\) are nonnegative. Consequently, the \(k\)-th largest eigenvalue of \(L[S\cup\{w\}]=M+I\) is at least \(1\). Interlacing now gives
\[
t_k(G)\ge1=q.
\]

### Conclusion

All possibilities for the integer \(q=d_k-k+2\) have been covered. Therefore
\[
t_k\ge d_k-k+2
\]
for every \(1\le k\le n-1\), and hence
\[
\boxed{c_k(G)=t_k+k-2\ge d_k(G).}
\]

There are no remaining mathematical gaps in this argument under the standard simple-graph convention. The only qualification concerns historical verification: the attribution of the already-known resolution is taken from the supplied catalog.