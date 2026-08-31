```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The Heawood graph is not countable: odd-characteristic projective-plane incidence graphs give relatively regular C4-free blow-ups with zero canonical Heawood copies.",
  "would_publish": false,
  "caveats": "No full characterization is obtained; prior appearance of this Fano-plane obstruction was not independently literature-checked."
}
```

## 1. Statement of the partial result

Let \(H\) be the Heawood graph, equivalently the Levi graph of the Fano plane. Thus
\[
v(H)=14,\qquad e(H)=21,
\]
and \(H\) is cubic of girth \(6\).

I prove the following.

**Theorem.**  
The Heawood graph is not countable in the canonical \(F\)-partite sense of Definition 1.3 of the source paper. More precisely, for every fixed \(\varepsilon>0\), there are arbitrarily large \(H\)-partite \(C_4\)-free graphs \(G\), with all vertex classes of the same size \(m\), such that for every \(xy\in E(H)\),

1. \((V_x,V_y)\) is \((\varepsilon,m^{-1/2})\)-regular;
2. its density is
   \[
   d(V_x,V_y)=\left(\frac1{\sqrt7}+o(1)\right)m^{-1/2};
   \]
3. \(G\) has no canonical copy of \(H\).

Consequently, the regular approximation predicts
\[
\Theta\!\left(m^{14}m^{-21/2}\right)=\Theta(m^{7/2})
\]
canonical Heawood copies, while the actual number is zero.

This also gives a general finite-geometric obstruction to countability.

---

## 2. The projective-plane host graph

Let \(q\) run through odd prime powers tending to infinity, for example \(q=3^r\). Let
\[
\Pi_q=\operatorname{PG}(2,q)
\]
be the Desarguesian projective plane of order \(q\). It has
\[
N=q^2+q+1
\]
points and the same number of lines. Every point lies on \(q+1\) lines, every line contains \(q+1\) points, and two distinct points lie on a unique common line.

Let \(B_q\) be the bipartite point-line incidence graph of \(\Pi_q\). Then \(B_q\) is \(C_4\)-free: a \(4\)-cycle would give two distinct lines through the same two distinct points.

Write the seven point-vertices and seven line-vertices of the Fano plane as
\[
\mathcal P_0=\{a,b,c,x,y,z,t\},\qquad \mathcal L_0=\{\ell_1,\ldots,\ell_7\}.
\]
Partition \(7m\) of the points of \(\Pi_q\) into seven disjoint sets
\[
P_a,P_b,P_c,P_x,P_y,P_z,P_t
\]
of size
\[
m=\left\lfloor \frac N7\right\rfloor,
\]
and partition \(7m\) lines similarly into sets \(L_{\ell}\), one for each Fano line.

For every incidence \(u\in\ell\) in the Fano plane, put between \(P_u\) and \(L_\ell\) precisely the incidences inherited from \(\Pi_q\). Put no other edges in \(G_q\). Thus \(G_q\) is an \(H\)-partite subgraph of \(B_q\), and hence is \(C_4\)-free.

---

## 3. Sparse regularity of every required pair

Let \(M\) be the point-line incidence matrix of \(\Pi_q\). Since two distinct points lie on one common line,
\[
MM^{\mathsf T}=qI+J.
\]
Therefore the largest singular value of \(M\) is \(q+1\), while all nontrivial singular values are \(\sqrt q\). It follows that for arbitrary sets \(X\) of points and \(Y\) of lines,
\[
\left|e(X,Y)-p_0|X||Y|\right|
   \leq \sqrt q\,\sqrt{|X||Y|},
\tag{3.1}
\]
where
\[
p_0=\frac{q+1}{N}=\frac1q+O(q^{-2}).
\]

Consider one required pair \((P_u,L_\ell)\), and write its density as \(\rho_{u\ell}\). Applying (3.1) to the two classes gives
\[
|\rho_{u\ell}-p_0|
   \leq \frac{\sqrt q}{m}
   =O(q^{-3/2}).
\]
Hence
\[
\rho_{u\ell}=\frac1q+O(q^{-3/2}).
\tag{3.2}
\]
Since
\[
m=\left(\frac17+o(1)\right)q^2,
\]
we have
\[
m^{-1/2}=\left(\sqrt7+o(1)\right)\frac1q,
\]
and therefore
\[
\rho_{u\ell}
 =\left(\frac1{\sqrt7}+o(1)\right)m^{-1/2}.
\tag{3.3}
\]

Now let \(X\subseteq P_u\) and \(Y\subseteq L_\ell\) satisfy
\[
|X|\geq \varepsilon m,\qquad |Y|\geq \varepsilon m.
\]
Using (3.1) and the estimate for \(\rho_{u\ell}\),
\[
\begin{aligned}
|d(X,Y)-\rho_{u\ell}|
&\leq \frac{\sqrt q}{\sqrt{|X||Y|}}+\frac{\sqrt q}{m}\\
&\leq \left(\varepsilon^{-1}+1\right)\frac{\sqrt q}{m}\\
&=o(m^{-1/2}).
\end{aligned}
\]
For every fixed \(\varepsilon>0\), this is at most \(\varepsilon m^{-1/2}\) once \(q\) is sufficiently large. Thus all required pairs are \((\varepsilon,m^{-1/2})\)-regular.

In fact, a stronger relative cut estimate holds:
\[
\sup_{X\subseteq P_u,\;Y\subseteq L_\ell}
\frac{\left|e(X,Y)-\rho_{u\ell}|X||Y|\right|}
     {\rho_{u\ell}m^2}
=O(q^{-1/2}).
\tag{3.4}
\]
Thus the obstruction is not caused by a failure of macroscopic pairwise quasirandomness.

If desired, the partitions can be chosen randomly and equitably. Hypergeometric concentration then also gives
\[
\deg(v,L_\ell)=(1+o(1))\frac q7
\]
for every point \(v\), and the dual assertion for every line. Hence the example can be made sparse-superregular at the vertex-degree level as well.

---

## 4. Why there is no Heawood copy

It remains to prove that the Fano plane cannot be represented inside \(\operatorname{PG}(2,q)\) when \(q\) is odd.

Label the seven Fano lines by the triples
\[
\begin{gathered}
\{a,b,x\},\quad \{a,c,y\},\quad \{b,c,z\},\\
\{a,z,t\},\quad \{b,y,t\},\quad \{c,x,t\},\quad
\{x,y,z\}.
\end{gathered}
\tag{4.1}
\]

Suppose that seven distinct points with these prescribed collinearities existed in \(\operatorname{PG}(2,K)\), where \(\operatorname{char}K\neq2\).

The points \(a,b,c\) are noncollinear. Indeed, if they were collinear, then the three distinct line-vertices corresponding to the first three triples in (4.1) would all have to be the unique line through \(a,b,c\).

After a projective change of coordinates, put
\[
a=[1:0:0],\qquad b=[0:1:0],\qquad c=[0:0:1].
\]
Using a diagonal projectivity fixing these three coordinate points, we may also arrange
\[
x=[1:1:0],\qquad y=[1:0:1].
\]
Since \(z\) lies on \(bc\), write
\[
z=[0:1:\lambda],\qquad \lambda\neq0.
\]

The point \(t\) lies both on \(az\) and on \(by\). The line \(az\) has equation \(Z=\lambda Y\), while \(by\) has equation \(Z=X\). Hence
\[
t=[\lambda:1:\lambda].
\]
But \(t\) also lies on \(cx\), whose equation is \(X=Y\). Therefore \(\lambda=1\), so
\[
z=[0:1:1],\qquad t=[1:1:1].
\]

Finally, \(x,y,z\) must be collinear. Their determinant is
\[
\det
\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix}
=-2.
\]
This vanishes only in characteristic \(2\), contradicting the assumption that \(q\) is odd.

Thus there is no injective incidence-preserving realization of the Fano plane in \(\operatorname{PG}(2,q)\) for odd \(q\). Consequently \(G_q\) has no canonical Heawood copy. In fact, the entire incidence graph \(B_q\) is Heawood-free; an embedding with the two bipartition classes interchanged is ruled out by the dual version of the same argument.

---

## 5. Failure of the counting lemma

Put
\[
p=m^{-1/2}.
\]
For every edge \(u\ell\in E(H)\), equation (3.3) gives
\[
\rho_{u\ell}
 =\left(\frac1{\sqrt7}+o(1)\right)p.
\]
The product-density prediction for canonical copies is therefore
\[
\begin{aligned}
m^{14}\prod_{u\ell\in E(H)}\rho_{u\ell}
&=\left(7^{-21/2}+o(1)\right)p^{21}m^{14}\\
&=\left(7^{-21/2}+o(1)\right)m^{7/2},
\end{aligned}
\]
which tends to infinity.

Definition 1.3 would, after fixing a counting error smaller than (say) half the displayed positive coefficient, force a positive constant multiple of \(m^{7/2}\) canonical copies once the regularity parameter is sufficiently small. But \(G_q\) has none. Since \(q\) can be chosen arbitrarily large after the regularity parameter is specified, this contradicts countability.

Hence the Heawood graph is not countable.

---

## 6. General finite-geometric obstruction

The same argument yields the following criterion.

**Proposition.**  
Let \(F\) be a fixed bipartite graph with bipartition \(A\cup B\), regarded as an incidence structure whose \(A\)-vertices are points and \(B\)-vertices are lines. Suppose:

1. \(e(F)<2v(F)\);
2. for an unbounded sequence of prime powers \(q\), there is no pair of injective maps
   \[
   A\longrightarrow \{\text{points of }\operatorname{PG}(2,q)\},\qquad
   B\longrightarrow \{\text{lines of }\operatorname{PG}(2,q)\}
   \]
   preserving every incidence corresponding to an edge of \(F\).

Then \(F\) is not countable.

Indeed, partition the points and lines into disjoint classes indexed by \(A\) and \(B\), and use projective incidence on every required pair. The spectral calculation above gives sparse regularity with density \(\Theta(m^{-1/2})\). Any canonical copy would be such an incidence representation. Meanwhile the regular prediction has order
\[
m^{v(F)}q^{-e(F)}
   =\Theta\!\left(q^{\,2v(F)-e(F)}\right),
\]
which tends to infinity under condition 1.

Thus countability of a sparse bipartite incidence graph imposes a nontrivial “representation over all sufficiently large characteristics” condition, not merely a girth or density condition.

---

## 7. Relation to the known necessary conditions

The Heawood graph satisfies both necessary conditions mentioned on the catalog page.

- It has girth \(6\), hence girth at least \(5\).
- It also satisfies \(m_2(H)<2\).

For the latter, let \(J\subseteq H\) have \(v=v(J)\ge3\). Since \(H\) has maximum degree \(3\) and girth \(6\):

- if \(3\le v\le5\), then \(J\) is a forest, so \(e(J)\le v-1\);
- if \(v=6\), then \(e(J)\le6\);
- if \(v=7\), then \(e(J)\le\lfloor 3v/2\rfloor=10=2v-4\);
- if \(v\ge8\), then
  \[
  e(J)\le\frac{3v}{2}\le2v-4.
  \]

Thus in every case
\[
e(J)\le2v(J)-4,
\]
and hence
\[
\frac{e(J)-1}{v(J)-2}
\le 2-\frac1{v(J)-2}<2.
\]
Therefore \(m_2(H)<2\).

So even the conjunction
\[
\text{girth}(F)\ge5
\quad\text{and}\quad
m_2(F)<2
\]
is not sufficient for countability.

---

## 8. Remaining gaps

This does not characterize all countable graphs and does not settle the Petersen or dodecahedral graphs. It supplies:

1. an explicit cubic graph of girth at least \(5\) that is not countable;
2. a general characteristic/representability obstruction;
3. evidence that a complete characterization must involve more than local sparsity parameters such as girth and \(m_2\).

I have not independently verified whether this specific Fano-plane observation has already appeared in the literature, so I make no novelty claim.