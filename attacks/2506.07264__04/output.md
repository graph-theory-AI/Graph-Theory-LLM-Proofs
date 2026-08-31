```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds strictly for every graph whose unique odd cycle is a triangle, in particular for all triangular unicyclic graphs, while the full conjecture would imply the general conjecture s^+(G) >= n-1.",
  "would_publish": false,
  "caveats": "Graphs with interacting odd cycles remain untreated, and novelty beyond the supplied literature review was not independently checked."
}
```

## 1. Statement and outcome

Write \(m=|E(G)|\), and define the signed square imbalance
\[
\Delta(G):=s^+(G)-s^-(G).
\]
Since
\[
s^+(G)+s^-(G)=\operatorname{tr}A(G)^2=2m,
\]
we have
\[
s^+(G)=m+\frac{\Delta(G)}2.
\]
Thus the catalog conjecture is equivalent to
\[
\Delta(G)\ge 2(n-m).
\]
For a unicyclic graph, \(m=n\), so it suffices to prove \(\Delta(G)\ge0\).

The main positive result below is stronger than the unicyclic case:

> **Theorem A.** Let \(G\) be a graph having exactly one odd cycle \(C\).
> - If \(|C|\equiv3\pmod4\), then \(\Delta(G)>0\).
> - If \(|C|\equiv1\pmod4\), then \(\Delta(G)<0\).
>
> Consequently, if the unique odd cycle is a triangle and \(G\) is connected, then
> \[
> s^+(G)>m\ge n.
> \]

This settles, in particular, every unicyclic graph containing a triangle, the sparse case identified in the source paper as the main obstacle.

I also prove a broader sufficient condition involving an odd-cycle-transversal edge, and a reduction showing that the full catalog conjecture would imply the still-open general conjecture \(s^+(H)\ge |V(H)|-1\).

---

## 2. A phase formula for \(\Delta(G)\)

Let
\[
\phi_G(x)=\det(xI-A(G))
\]
and, for \(t>0\), put
\[
\Phi_G(t):=i^{-n}\phi_G(it).
\]
Since the eigenvalues of \(A(G)\) are real, \(\Phi_G(t)\ne0\) for \(t>0\). Choose a continuous argument
\[
\theta_G(t)=\arg\Phi_G(t)
\]
normalized by \(\theta_G(t)\to0\) as \(t\to\infty\).

### Lemma 2.1
For every simple graph \(G\),
\[
\boxed{\quad
\Delta(G)=-\frac4\pi\int_0^\infty t\,\theta_G(t)\,dt.
\quad}
\]

### Proof

Let the eigenvalues be \(\lambda_1,\dots,\lambda_n\). For every real \(\lambda\),
\[
\lambda|\lambda|
 =\frac2\pi\int_0^\infty \frac{\lambda^3}{t^2+\lambda^2}\,dt.
\]
Therefore
\[
\Delta(G)
 =\frac2\pi\int_0^\infty
 \sum_{j=1}^n\frac{\lambda_j^3}{t^2+\lambda_j^2}\,dt.
\]
Because \(\sum_j\lambda_j=\operatorname{tr}A(G)=0\),
\[
\sum_j\frac{\lambda_j^3}{t^2+\lambda_j^2}
 =-t^2\sum_j\frac{\lambda_j}{t^2+\lambda_j^2}.
\]

On the other hand,
\[
\frac{d}{dt}\log\Phi_G(t)
 =\sum_j\frac{i}{it-\lambda_j},
\]
so
\[
\theta_G'(t)
 =\operatorname{Im}\sum_j\frac{i}{it-\lambda_j}
 =-\sum_j\frac{\lambda_j}{t^2+\lambda_j^2}.
\]
Hence
\[
\Delta(G)=\frac2\pi\int_0^\infty t^2\theta_G'(t)\,dt.
\]
Integration by parts gives the assertion. The boundary terms vanish: \(\theta_G(t)\) has a finite limit as \(t\downarrow0\), while \(\theta_G(t)=O(t^{-3})\) as \(t\to\infty\), since \(G\) is loopless and the first possible imaginary term in \(i^{-n}\phi_G(it)\) occurs in degree \(n-3\). ∎

Thus, if \(\Phi_G(t)\) stays in the lower half-plane for every \(t>0\), then \(\Delta(G)>0\).

---

## 3. Bipartite characteristic polynomials and an edge recurrence

If \(H\) is bipartite of order \(h\), define
\[
q_H(t):=i^{-h}\phi_H(it).
\]

### Lemma 3.1
For every bipartite graph \(H\) and every \(t>0\),
\[
q_H(t)>0.
\]

### Proof

The nonzero eigenvalues of a bipartite graph occur in pairs \(\pm\mu_j\). If the nullity is \(z\), then
\[
i^{-h}\phi_H(it)
 =t^z\prod_j(t^2+\mu_j^2)>0.
\]
∎

We shall also use the following determinant recurrence.

### Lemma 3.2
For an edge \(e=uv\),
\[
\boxed{\quad
\phi_G(x)=\phi_{G-e}(x)-\phi_{G-u-v}(x)
          -2\sum_{\substack{C\text{ a cycle}\\ e\in E(C)}}
             \phi_{G-V(C)}(x).
\quad}
\]

### Proof

Expand \(\det(xI-A(G))\) by permutations and classify terms according to their use of \(e\).

- Terms not using \(e\) give \(\phi_{G-e}(x)\).
- Terms using \(uv\) and \(vu\) as a transposition give
  \(-\phi_{G-u-v}(x)\).
- If \(e\) lies in a permutation cycle of length at least three, that permutation cycle corresponds to one of the two orientations of a graph cycle \(C\) containing \(e\). Each orientation contributes a factor \(-1\), and the remaining permutation contributes \(\phi_{G-V(C)}(x)\).

Summing gives the identity. ∎

---

## 4. An odd-cycle-transversal criterion

Suppose \(e=uv\) is such that \(B:=G-e\) is bipartite and \(u,v\) belong to the same bipartition class. Every cycle of \(G\) containing \(e\) is then odd.

For \(r\in\{1,3\}\), put
\[
S_r(t)=
 \sum_{\substack{C\ni e\\ |C|\equiv r\pmod4}}
 q_{G-V(C)}(t).
\]
Normalizing the recurrence in Lemma 3.2 gives
\[
\Phi_G(t)
 =q_{G-e}(t)+q_{G-u-v}(t)
   +2i\bigl(S_1(t)-S_3(t)\bigr).
\]
Its real part is strictly positive.

### Theorem 4.1
Under the preceding hypotheses, if
\[
S_3(t)\ge S_1(t)\qquad\text{for every }t>0,
\]
with strict inequality for some \(t\), then
\[
\Delta(G)>0.
\]

In particular, this holds if every cycle containing \(e\) has length \(3\pmod4\).

### Proof

The displayed formula places \(\Phi_G(t)\) in the closed lower half-plane, with positive real part, and strictly below the real axis for some interval. Thus
\[
-\frac{\pi}{2}<\theta_G(t)\le0
\]
and \(\theta_G\) is not identically zero. Lemma 2.1 yields \(\Delta(G)>0\). ∎

Consequently, any connected graph satisfying this condition and containing a cycle obeys
\[
s^+(G)=m+\frac{\Delta(G)}2>m\ge n.
\]

---

## 5. Graphs with exactly one odd cycle

We now prove Theorem A.

Let \(C\) be the unique odd cycle of \(G\), of length \(\ell\), and choose \(e=uv\in E(C)\). Then \(G-e\) contains no odd cycle, hence is bipartite. In the bipartition of \(G-e\), the vertices \(u,v\) lie in the same class because \(C-e\) has even length.

Moreover, \(C\) is the only cycle of \(G\) containing \(e\). Indeed, every \(u\)-\(v\) path in \(G-e\) has even length, so adding \(e\) to any such path creates an odd cycle; uniqueness forces that path to be \(C-e\).

The edge recurrence therefore becomes
\[
\Phi_G(t)
 =q_{G-e}(t)+q_{G-u-v}(t)
   -2i^{-\ell}q_{G-V(C)}(t).
\]
All three \(q\)-terms are positive.

- If \(\ell\equiv3\pmod4\), then \(i^{-\ell}=i\), so
  \[
  \Phi_G(t)=a(t)-2ib(t),
  \qquad a(t),b(t)>0.
  \]
  Hence \(\theta_G(t)\in(-\pi/2,0)\), and Lemma 2.1 gives
  \(\Delta(G)>0\).

- If \(\ell\equiv1\pmod4\), then \(i^{-\ell}=-i\), so
  \[
  \Phi_G(t)=a(t)+2ib(t),
  \qquad a(t),b(t)>0.
  \]
  Hence \(\theta_G(t)\in(0,\pi/2)\), and \(\Delta(G)<0\).

This proves Theorem A.

### Corollary 5.1
If \(G\) is connected and its unique odd cycle is a triangle, then
\[
s^+(G)>m\ge n.
\]

In particular:

> **Every connected unicyclic graph containing a triangle satisfies**
> \[
> \boxed{s^+(G)>n.}
> \]

---

## 6. A quantitative result for all unicyclic graphs

For a graph \(H\), let
\[
M_H(t)=\sum_{j\ge0}m_j(H)t^{|V(H)|-2j},
\]
where \(m_j(H)\) denotes the number of \(j\)-edge matchings.

Suppose \(G\) is unicyclic with unique cycle \(C_\ell\), where \(\ell\) is odd. The Sachs expansion gives
\[
\phi_G(x)=\mu_G(x)-2\mu_{G-V(C_\ell)}(x),
\]
where \(\mu\) is the matching polynomial. At \(x=it\),
\[
\Phi_G(t)
 =M_G(t)-2i^{-\ell}M_{G-V(C_\ell)}(t).
\]
It follows that
\[
|\Delta(G)|
 =\frac4\pi\int_0^\infty
 t\arctan\left(
 \frac{2M_{G-V(C_\ell)}(t)}{M_G(t)}
 \right)\,dt.
\]

Every union of a matching in \(C_\ell\) and a matching in
\(G-V(C_\ell)\) is a matching in \(G\). Hence, coefficientwise,
\[
M_G(t)\ge M_{C_\ell}(t)M_{G-V(C_\ell)}(t),
\]
and therefore
\[
|\Delta(G)|\le |\Delta(C_\ell)|.
\]

The eigenvalues of \(C_\ell\) are
\[
2\cos\frac{2\pi j}{\ell},\qquad 0\le j<\ell.
\]
A Dirichlet-kernel calculation gives
\[
\Delta(C_\ell)=
\begin{cases}
2\bigl(\sec(\pi/\ell)-1\bigr),
   &\ell\equiv3\pmod4,\\[2mm]
-2\bigl(\sec(\pi/\ell)-1\bigr),
   &\ell\equiv1\pmod4.
\end{cases}
\]
For example, when \(\ell=4r+1\), the positive cosine indices are
\(-r,\ldots,r\), and
\[
\sum_{j=-r}^r\cos\frac{4\pi j}{\ell}
 =-\frac1{2\cos(\pi/\ell)},
\]
which yields the second formula; the other congruence class is analogous.

We obtain:

### Theorem 6.1
Let \(G\) be unicyclic with odd cycle length \(\ell\). Then
\[
\operatorname{sgn}\Delta(G)=
\begin{cases}
+1,&\ell\equiv3\pmod4,\\
-1,&\ell\equiv1\pmod4,
\end{cases}
\]
and
\[
|\Delta(G)|
 \le 2\bigl(\sec(\pi/\ell)-1\bigr)\le2.
\]

For a triangular unicyclic graph,
\[
0<\Delta(G)\le2,
\]
and consequently
\[
\boxed{\quad n<s^+(G)\le n+1.\quad}
\]
The upper equality occurs for \(K_3\); attachments to the triangle make the matching-polynomial inequality strict.

For completeness, if the unique cycle is even, the graph is bipartite and
\[
s^+(G)=m=n.
\]
Thus the general bound \(s^+(G)\ge n-1\) also holds for every connected unicyclic graph.

---

## 7. The full conjecture implies the general \(n-1\) conjecture

There is a significant obstruction to extending the preceding proof to all graphs with triangles.

### Theorem 7.1
Let \(H\) be a connected graph of order \(h\ge2\), and choose an edge \(xy\in E(H)\). Construct \(G_k\) by:

1. adding a new vertex \(v\) adjacent to \(x\) and \(y\);
2. adding \(k\) pendant vertices adjacent only to \(v\).

Then \(G_k\) contains the triangle \(xvy\), and
\[
\boxed{\quad
\lim_{k\to\infty}
\bigl(s^+(G_k)-|V(G_k)|\bigr)
 =s^+(H)-(h-1).
\quad}
\]

### Proof

Let \(A=A(H)\) and \(b=e_x+e_y\). There are \(k-1\) zero eigenvalues coming from differences of pendant-leaf vectors. On the remaining invariant subspace, with the normalized all-leaves vector, the adjacency matrix is
\[
B_k=
\begin{pmatrix}
0&\sqrt{k}&b^{T}\\
\sqrt{k}&0&0\\
b&0&A
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
p_k(z)
 =(z^2-k)\phi_H(z)
   -z\,b^T\operatorname{adj}(zI-A)b.
\]
On every bounded region,
\[
-\frac1k p_k(z)\longrightarrow \phi_H(z).
\]
Exactly two roots escape to infinity, while the other \(h\) roots converge, with multiplicity, to the eigenvalues of \(H\).

For the two escaping roots, write
\[
d=b^Tb,\qquad a=b^TAb.
\]
For large \(z\),
\[
b^T(zI-A)^{-1}b
 =\frac d z+\frac a{z^2}+O(z^{-3}).
\]
The two large eigenvalues solve
\[
z^2-k-zb^T(zI-A)^{-1}b=0,
\]
and hence, with \(L_k=\sqrt{k+d}\),
\[
\rho_{+,k}
 =L_k+\frac{a}{2L_k^2}+O(L_k^{-3}),
\qquad
\rho_{-,k}
 =-L_k+\frac{a}{2L_k^2}+O(L_k^{-3}).
\]
Thus
\[
\rho_{+,k}^2-\rho_{-,k}^2=O(k^{-1/2})\longrightarrow0.
\]
Since \(x\mapsto x|x|\) is continuous, the bounded eigenvalues give
\[
\Delta(G_k)\longrightarrow\Delta(H).
\]

If \(m=|E(H)|\), then
\[
|V(G_k)|=h+k+1,\qquad |E(G_k)|=m+k+2.
\]
Therefore
\[
s^+(G_k)-|V(G_k)|
 =\frac{\Delta(G_k)}2+m-h+1.
\]
Passing to the limit gives
\[
\frac{\Delta(H)}2+m-h+1
 =s^+(H)-(h-1),
\]
as claimed. ∎

### Consequence

If the catalog conjecture were true, then every \(G_k\) above would satisfy
\[
s^+(G_k)-|V(G_k)|\ge0.
\]
Taking \(k\to\infty\) would imply
\[
s^+(H)\ge h-1
\]
for every connected graph \(H\).

Conversely, any counterexample \(H\) to the general \(n-1\) conjecture would, for all sufficiently large \(k\), produce explicit counterexamples \(G_k\) to the catalog conjecture.

This is only a logical transfer, not a counterexample, because no such \(H\) is presently available here. It does show that the catalog conjecture is at least as strong as the general positive-square-energy conjecture.

Taking \(H=K_2\) also shows that the strict surplus in the triangular unicyclic theorem is not uniform:
\[
s^+(G_k)-|V(G_k)|\longrightarrow0^+.
\]

---

## 8. Why the proof does not cover all triangle-containing graphs

When several odd cycles interact, the normalized characteristic polynomial can receive imaginary contributions of both signs:
\[
\Phi_G(t)
 =\text{positive real part}
  +2i\left(
      \sum_{|C|\equiv1(4)}q_{G-C}(t)
      -
      \sum_{|C|\equiv3(4)}q_{G-C}(t)
    \right)
\]
in the one-edge-near-bipartite setting. There is then no general half-plane control on \(\Phi_G(t)\).

Nor can one simply take a spanning triangular unicyclic subgraph and add the remaining edges: positive square energy is not manifestly monotone under increasing adjacency entries. Even in a weighted direction this monotonicity fails locally. For \(P_5\), let \(A_+\) denote the positive part of its adjacency matrix. A direct diagonalization gives
\[
(A_+)_{1,5}=\frac{\sqrt3-3}{12}<0.
\]
Consequently, if \(E_{15}\) adds a weighted edge between the endpoints,
\[
\left.\frac d{dt}s^+(A(P_5)+tE_{15})\right|_{t=0}
 =4(A_+)_{1,5}
 =\frac{\sqrt3-3}{3}<0.
\]
This is not an unweighted counterexample—at \(t=1\) one obtains \(C_5\), whose \(s^+\) is larger than that of \(P_5\)—but it rules out a naive entrywise-monotonicity argument.

Hence the remaining gap is genuine: the argument proves the conjecture for unique-odd-cycle graphs and a broader odd-cycle-transversal class, but it does not control arbitrary multicyclic graphs containing triangles.