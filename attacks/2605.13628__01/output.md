```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "At the natural q^n|S|^n scale the question remains open, but the verbatim q^{2n}-scale analogue is false and an explicit q^{(1+2 eta)n}-scale removal bound follows from slice rank.",
  "would_publish": false,
  "caveats": "The catalog question does not specify the normalization, treatment of zero difference, or whether three colored sets are intended."
}
```

# Mathematical writeup

## 1. A precise formulation

Let \(q\) be an odd prime power, let \(S\subseteq \mathbb F_q\) contain \(0\), and write
\[
s=|S|,\qquad G=\mathbb F_q^n,\qquad N=q^n,\qquad D=S^n.
\]

For three colored sets \(X,Y,Z\subseteq G\), define a restricted arithmetic triangle to be a triple
\[
(x,y,z)\in X\times Y\times Z
\]
such that
\[
x+z=2y,\qquad y-x\in D.
\]
Let \(m=m_S(X,Y,Z)\) be the number of these triangles. Let \(\tau=\tau_S(X,Y,Z)\) be the minimum of
\[
|X_0|+|Y_0|+|Z_0|
\]
over \(X_0\subseteq X,Y_0\subseteq Y,Z_0\subseteq Z\) whose deletion destroys every restricted triangle.

There are exactly
\[
N s^n
\]
restricted triangles in the complete instance \(X=Y=Z=G\), since one may choose \(x\in G\) and \(d=y-x\in S^n\).

Thus the natural relative removal statement is:

> **Natural restricted removal conjecture.**  
> For every \(\varepsilon>0\), there is a \(\delta=\delta(q,S,\varepsilon)>0\), independent of \(n\), such that
> \[
> \tau_S(X,Y,Z)\ge \varepsilon N
> \quad\Longrightarrow\quad
> m_S(X,Y,Z)\ge \delta N s^n.
> \tag{RR}
> \]

This is the formulation considered below.

---

## 2. The verbatim \(N^2\)-scale analogue is false

Suppose \(S\ne\mathbb F_q\), so \(s<q\), and take
\[
X=Y=Z=G.
\]
Then
\[
m=Ns^n=N^2\left(\frac{s}{q}\right)^n=o(N^2).
\]

On the other hand, the triangles with \(d=0\),
\[
(x,x,x),\qquad x\in G,
\]
form a matching of size \(N\) in the three colored vertex classes. Hence every triangle cover has size at least \(N\). Deleting an entire color class shows that
\[
\tau=N.
\]

The same counterexample works if zero differences are excluded: choose any fixed nonzero \(d_0\in S^n\). The \(N\) triples
\[
(x,x+d_0,x+2d_0),\qquad x\in G,
\]
again form a colored matching of size \(N\).

Consequently, a statement of the form
\[
m=o(N^2)\quad\Longrightarrow\quad \tau=o(N)
\]
is false for every proper \(S\). Normalization by \(Ns^n\), rather than \(N^2\), is essential.

At the opposite extreme, normalization only by \(N\) gives a trivial lemma: selecting one vertex from every triangle gives \(\tau\le m\). The question is therefore genuinely about the intermediate sparse scale \(Ns^n\).

---

## 3. The unrestricted case \(S=\mathbb F_q\)

For completeness, (RR) holds when \(S=\mathbb F_q\).

Set
\[
A=X,\qquad B=-2Y,\qquad C=Z.
\]
Restricted triangles are then simply solutions
\[
a+b+c=0,\qquad (a,b,c)\in A\times B\times C.
\]

Construct a tripartite graph with vertex classes \(U,V,W\), each a copy of \(G\), by putting

- \(uv\) in the graph if \(v-u\in A\);
- \(vw\) in the graph if \(w-v\in B\);
- \(wu\) in the graph if \(u-w\in C\).

Every arithmetic solution \(a+b+c=0\) produces exactly \(N\) graph triangles, one for each choice of \(u\). Conversely, every graph triangle gives such a solution. Hence the graph contains exactly \(Nm\) triangles.

Suppose a set \(F\) of graph edges destroys all graph triangles. Call a label \(a\in A\) heavy if at least \(N/3\) of the \(N\) edges labeled \(a\) lie in \(F\), and similarly for labels in \(B,C\).

If \(a+b+c=0\) and none of \(a,b,c\) is heavy, then, as the translation parameter \(u\) ranges over \(G\), fewer than \(N/3\) corresponding triangles are blocked by deleted \(A\)-edges, fewer than \(N/3\) by deleted \(B\)-edges, and fewer than \(N/3\) by deleted \(C\)-edges. Some graph triangle therefore survives. Thus the heavy labels meet every arithmetic solution.

It follows that if \(\tau\ge\varepsilon N\), then there are at least \(\varepsilon N\) heavy labels, and therefore
\[
|F|\ge \frac{\varepsilon N^2}{3}.
\]
The graph has \(3N\) vertices, so it is \(\varepsilon/27\)-far from triangle-free. The ordinary graph triangle-removal lemma now gives a constant \(c_{\rm TR}(\varepsilon/27)>0\) such that
\[
Nm\ge c_{\rm TR}(\varepsilon/27)(3N)^3.
\]
Therefore
\[
m\ge 27c_{\rm TR}(\varepsilon/27)N^2.
\]

Thus (RR) holds for \(S=\mathbb F_q\). In particular, under the hypothesis \(s>(q+1)/2\), this covers all possibilities when \(q=3\).

---

## 4. A restricted tri-colored slice-rank bound

Assume now that
\[
s>\frac{q+1}{2}.
\]
Define
\[
r=2q-s-1
\]
and
\[
\gamma=\gamma(q,s)
   :=\inf_{0<t\le 1}
      t^{-r/3}(1+t+\cdots+t^{q-1}).
\tag{1}
\]
The inequality on \(s\) implies
\[
\frac r3<\frac{q-1}{2}.
\]
At \(t=1\), the expression in (1) equals \(q\), while its logarithmic derivative there is
\[
\frac{q-1}{2}-\frac r3>0.
\]
Moving slightly to the left of \(t=1\) therefore decreases the expression, so
\[
\gamma<q.
\]
Write
\[
\eta=1-\log_q\gamma>0.
\tag{2}
\]

### Lemma 1: induced matchings

Every induced matching in the restricted arithmetic-triangle hypergraph on three copies of \(G\) has size at most
\[
3\gamma^n.
\tag{3}
\]

#### Proof

For \(u,v,w\in\mathbb F_q\), consider
\[
Q(u,v,w)=
\left(1-(u+w-2v)^{q-1}\right)
\prod_{a\in\mathbb F_q\setminus S}(v-u-a).
\]
This is nonzero precisely when
\[
u+w=2v,\qquad v-u\in S.
\]
Its total degree is at most
\[
(q-1)+(q-s)=r.
\]

For vectors \(\boldsymbol u,\boldsymbol v,\boldsymbol w\in G\), put
\[
Q_n(\boldsymbol u,\boldsymbol v,\boldsymbol w)
   =\prod_{\ell=1}^n Q(u_\ell,v_\ell,w_\ell).
\]
As a polynomial function on \((\mathbb F_q^n)^3\), reduce all variables modulo \(T^q-T\). This does not increase total degree, and every individual exponent can then be assumed to lie in \(\{0,\ldots,q-1\}\). Every monomial has total degree at most \(rn\), so one of its three blocks of variables has degree at most \(rn/3\).

Let
\[
M_n=\#\left\{\alpha\in\{0,\ldots,q-1\}^n:
        |\alpha|\le \frac{rn}{3}\right\}.
\]
Assign each monomial to one of its blocks of degree at most \(rn/3\), and group according to the monomial in that block. This gives
\[
\operatorname{slice\mbox{-}rank}(Q_n)\le 3M_n.
\]
For every \(0<t\le1\),
\[
M_n t^{rn/3}
 \le \sum_{\alpha\in\{0,\ldots,q-1\}^n}t^{|\alpha|}
 =(1+t+\cdots+t^{q-1})^n.
\]
Hence
\[
M_n\le\gamma^n.
\]

Now let
\[
e_i=(x_i,y_i,z_i),\qquad 1\le i\le L,
\]
be an induced matching. Then
\[
Q_n(x_i,y_j,z_k)\ne0
\quad\Longleftrightarrow\quad
i=j=k.
\]
Thus the restriction of \(Q_n\) to these index sets is a diagonal tensor with \(L\) nonzero diagonal entries. Such a tensor has slice rank exactly \(L\), while restricting a tensor cannot increase slice rank. Therefore
\[
L\le 3\gamma^n.
\]

For reference, the diagonal-tensor fact follows by contracting any proposed slice decomposition in the first coordinate against a vector orthogonal to all first-coordinate slice functions. A \(d\)-dimensional subspace of \(\mathbb F_q^L\) contains a vector with at least \(d\) nonzero coordinates, and the resulting diagonal matrix has rank at least \(L-r_1\), forcing \(r_2+r_3\ge L-r_1\). Hence the total number of slices is at least \(L\). ∎

As a special case, if \(A\subseteq G\) contains no nonconstant restricted progression, then \(Q_n\) restricted to \(A^3\) is diagonal, giving
\[
|A|\le 3\gamma^n.
\tag{4}
\]

---

## 5. A power-scale restricted removal theorem

### Theorem 2

For all \(X,Y,Z\subseteq G\),
\[
m_S(X,Y,Z)
   \ge
   \frac{4}{6561}\,
   \frac{\tau_S(X,Y,Z)^3}{\gamma^{2n}}.
\tag{5}
\]
Consequently, if
\[
\tau_S(X,Y,Z)\ge\varepsilon N,
\]
then
\[
m_S(X,Y,Z)
 \ge
 \frac{4}{6561}\varepsilon^3
 \left(\frac{q^3}{\gamma^2}\right)^n
 =
 \frac{4}{6561}\varepsilon^3N^{1+2\eta}.
\tag{6}
\]

#### Proof

Let \(H\) be the tripartite hypergraph of restricted triangles. A maximal matching has size
\[
L\ge\frac{\tau}{3},
\]
because the three endpoints of a maximal matching form a vertex cover.

Fix such a matching \(e_1,\ldots,e_L\). Every nonmatching edge of \(H\) contained in the union of these endpoints uses vertices from three distinct matching edges. Indeed, any two coordinates of an arithmetic triangle determine the third uniquely, since \(q\) is odd. Thus an edge sharing two vertices with \(e_i\) would equal \(e_i\).

Independently retain every matching edge with probability \(p\). Let \(R\) be the set of retained indices, and let \(C_R\) count the nonmatching triangles among their endpoints. Then
\[
\mathbb E|R|=pL,\qquad
\mathbb E C_R\le p^3m.
\]
Deleting at most one retained matching edge for every such extra triangle leaves an induced matching of size at least
\[
|R|-C_R.
\]
By Lemma 1, every induced matching has size at most
\[
B:=3\gamma^n.
\]
It follows that, for every \(p\),
\[
B\ge pL-p^3m.
\]
Choose
\[
p=\sqrt{\frac{L}{3m}},
\]
which is at most \(1\) because \(m\ge L\). Then
\[
B\ge \frac{2}{3\sqrt3}\frac{L^{3/2}}{m^{1/2}}.
\]
Therefore
\[
m\ge \frac{4L^3}{27B^2}.
\]
Using \(L\ge\tau/3\) and \(B=3\gamma^n\) gives
\[
m\ge
\frac{4}{27}\frac{(\tau/3)^3}{9\gamma^{2n}}
=
\frac{4}{6561}\frac{\tau^3}{\gamma^{2n}}.
\]
This proves (5), and (6) follows from (2). ∎

This is stronger than the trivial \(m\ge\tau\): since \(\eta>0\), an instance requiring deletion of a positive proportion of the vertices contains at least \(N^{1+2\eta}\) restricted triangles.

---

## 6. One-set, nonconstant progressions

Let \(A\subseteq G\), let \(m_A\) count ordered pairs \((x,d)\) with
\[
d\in S^n\setminus\{0\},
\qquad x,x+d,x+2d\in A,
\]
and let \(\rho(A)\) be the minimum number of elements that must be deleted from \(A\) to destroy all such progressions.

Color three copies of \(A\). Any colored vertex cover gives, by taking the union of its underlying points, a deletion set for \(A\). Hence the colored cover number is at least \(\rho(A)\).

The polynomial \(Q_n\) also detects zero-difference triples. Among the endpoints of any colored matching there are at most \(N\) such additional triples, one for each possible common underlying point. Repeating the preceding random extraction with these at most \(N\) extra obstructions gives
\[
m_A+N
 \ge
 \frac{4}{6561}\frac{\rho(A)^3}{\gamma^{2n}}.
\tag{7}
\]
Thus
\[
\rho(A)\ge\varepsilon N
\quad\Longrightarrow\quad
m_A+N\ge
\frac{4}{6561}\varepsilon^3N^{1+2\eta}.
\tag{8}
\]

Combining this with (4), a set of fixed positive density has power-scale supersaturation. For example, if \(|A|\ge\alpha N\), then for sufficiently large \(n\),
\[
\rho(A)\ge |A|-3\gamma^n\ge\frac{\alpha N}{2},
\]
and hence
\[
m_A=\Omega_{q,S,\alpha}\!\left(N^{1+2\eta}\right).
\]

---

## 7. Why this does not prove the natural relative lemma

The total number of possible restricted triangles is \(Ns^n\). Dividing (6) by this quantity yields only
\[
\frac{m}{Ns^n}
 \ge
 \frac{4}{6561}\varepsilon^3
 \left(\frac{q^2}{s\gamma^2}\right)^n.
\tag{9}
\]

In fact, the exponential factor in (9) is strictly less than \(1\). To see this, put \(a=r/3\). For \(K=\lfloor2a\rfloor\), pairing the terms \(j\) and \(K-j\) gives, for every \(0<t\le1\),
\[
\sum_{j=0}^{q-1}t^{j-a}
 \ge K+1.
\]
Since \(r\ge q-1\),
\[
\gamma\ge
\left\lfloor\frac{2(q-1)}3\right\rfloor+1.
\]
For \(q\ge7\), this is greater than \(\sqrt{2q}\), while \(s>q/2\) gives
\[
\frac q{\sqrt s}<\sqrt{2q}.
\]
The cases \(q=3,5\) are immediate:
\[
2>\sqrt3,\qquad 3>\frac52.
\]
Thus in every admissible case
\[
\gamma>\frac q{\sqrt s},
\qquad\text{so}\qquad
\frac{q^2}{s\gamma^2}<1.
\]

Therefore (9) decays exponentially with \(n\). The argument does not establish a positive dimension-independent density at the natural \(Ns^n\) scale.

## 8. Remaining gap

Under the precise formulation (RR), the unresolved step is to prove either

\[
\tau\ge\varepsilon q^n
\quad\Longrightarrow\quad
m\ge\delta(\varepsilon,q,S)\,q^n|S|^n
\]
for every proper admissible \(S\), or to construct sets \(X_n,Y_n,Z_n\) for which
\[
\tau_S(X_n,Y_n,Z_n)=\Omega(q^n)
\quad\text{but}\quad
m_S(X_n,Y_n,Z_n)=o(q^n|S|^n).
\]

The slice-rank argument above gives a genuine but exponentially smaller supersaturation scale. Hence it does not settle the natural restricted arithmetic triangle-removal problem.