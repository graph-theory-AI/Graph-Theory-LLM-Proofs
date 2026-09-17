```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every even-edge complete bipartite graph K_{a,b}, I obtain d_{K_{a,b}}(n)=Theta(n^{-k}), where 2k is the largest even part size, together with a broader rooted-copy result.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; novelty of these self-contained special-case bounds has not been verified."
}
```

## 1. Scope and partial results

I use the source paper’s **positive-edge** formulation. Graphs on \([n]\) are identified with vectors in
\[
\mathbb F_2^{E(K_n)},
\]
so addition is symmetric difference. A copy of a fixed graph is padded with isolated vertices outside its vertex set.

All upper bounds below apply to **arbitrary codes**, not merely linear ones.

### Theorem 1: Complete bipartite graphs

Let \(a,b\ge 1\) be fixed and suppose \(ab\) is even. Define
\[
2k=\max\{t\in\{a,b\}:t\text{ is even}\}.
\]
Then
\[
\boxed{\displaystyle d_{K_{a,b}}(n)=\Theta_{a,b}(n^{-k}).}
\]

For example,
\[
d_{C_4}(n)=\Theta(n^{-1}),\qquad
d_{K_{2,4}}(n)=\Theta(n^{-2}),\qquad
d_{K_{4,6}}(n)=\Theta(n^{-3}).
\]

If \(a,b\) are both odd, then \(d_{K_{a,b}}(n)=1/2\) for \(n\ge a+b\): edge parity gives the lower bound, while translation by any one fixed copy gives the upper bound.

There is also a broader class for which the required decay follows.

### Theorem 2: Even numbers of identical rooted pieces

Let \(F\) have at least one edge, and let \(R\subseteq V(F)\) be independent. Construct \(H\) from \(2k\) copies of \(F\) by identifying corresponding vertices of \(R\), with all other vertices distinct. Then
\[
\boxed{\displaystyle d_H(n)=O_{F,R,k}(n^{-k}).}
\]

In particular, \(H\) has \(2k\,e(F)\) edges. This includes even stars, even matchings, and nonbipartite examples such as even numbers of triangles sharing a common vertex.

For vertex-disjoint triangles, the bound can also be matched:
\[
\boxed{\displaystyle d_{\,2kK_3}(n)=\Theta_k(n^{-k}).}
\]

The proofs follow.

## 2. A forbidden-distance bound for the binary cube

We first establish the quantitative ingredient used for the upper bounds.

### Lemma 3

For every fixed \(k\ge 1\), there is a constant \(C_k\) such that, whenever \(m\ge 2k\), every
\[
B\subseteq\mathbb F_2^m
\]
containing no two vectors at Hamming distance exactly \(2k\) satisfies
\[
\frac{|B|}{2^m}\le C_km^{-k}.
\]

### Proof

Let \(T\) be the adjacency operator of the graph on \(\mathbb F_2^m\) joining vectors at distance \(2k\). Its degree is
\[
D=\binom{m}{2k}.
\]

For \(S\subseteq[m]\), the character
\[
\chi_S(x)=(-1)^{\sum_{i\in S}x_i}
\]
is an eigenvector, with eigenvalue
\[
\lambda_S
=\sum_{\substack{I\subseteq[m]\\|I|=2k}}
  \prod_{i\in I}\varepsilon_i
=e_{2k}(\varepsilon_1,\ldots,\varepsilon_m),
\]
where \(\varepsilon_i=-1\) for \(i\in S\), \(\varepsilon_i=1\) otherwise, and \(e_j\) is the \(j\)-th elementary symmetric polynomial.

We claim that, uniformly over all choices of the signs,
\[
e_{2k}(\varepsilon_1,\ldots,\varepsilon_m)\ge -B_km^k
\tag{1}
\]
for a constant \(B_k\).

Put \(s=\sum_i\varepsilon_i\). The power sums satisfy
\[
p_j:=\sum_i\varepsilon_i^j=
\begin{cases}
s,&j\text{ odd},\\
m,&j\text{ even}.
\end{cases}
\]
Newton’s identities,
\[
j e_j=\sum_{i=1}^j(-1)^{i-1}p_i e_{j-i},
\]
show inductively that
\[
e_{2k}
=\frac{s^{2k}}{(2k)!}
 +\sum_{r=0}^{k-1}a_{k,r}(m)s^{2r},
\qquad
\deg a_{k,r}\le k-r.
\tag{2}
\]
For completeness, assign weight \(1\) to \(s\) and weight \(2\) to \(m\). The recurrence gives weighted degree at most \(j\), and the exponent of \(s\) has the same parity as \(j\). The leading term \(s^j/j!\) follows from the \(i=1\) term.

Since the polynomials in (2) depend only on \(k\), there is \(A_k\) such that, for \(m\ge1\),
\[
|a_{k,r}(m)|\le A_km^{k-r}.
\]
Writing \(u=s/\sqrt m\), we obtain
\[
e_{2k}\ge
m^k\left(
\frac{u^{2k}}{(2k)!}
-A_k\sum_{r=0}^{k-1}u^{2r}
\right).
\]
The polynomial in parentheses has positive leading coefficient and even degree, so it is bounded below on \(\mathbb R\). This proves (1).

Now let \(f=1_B\), let \(\alpha=|B|/2^m\), and write \(f=\alpha\mathbf1+g\). Use the inner product with uniform measure on the cube. Since \(B\) is independent,
\[
0=\langle f,Tf\rangle
 =D\alpha^2+\langle g,Tg\rangle.
\]
By (1),
\[
0\ge D\alpha^2-B_km^k\alpha(1-\alpha).
\]
If \(\alpha>0\), this yields
\[
\alpha\le
\frac{B_km^k}{D+B_km^k}
=O_k(m^{-k}),
\]
because \(\binom m{2k}=\Theta_k(m^{2k})\). ∎

## 3. Rooted copies give binary-cube slices

We prove Theorem 2.

Write
\[
r=|R|,\qquad t=|V(F)\setminus R|.
\]
Because \(R\) is independent and \(F\) has an edge, \(t\ge1\).

On \([n]\), choose one common root set of size \(r\), and
\[
q=\left\lfloor\frac{n-r}{t}\right\rfloor
\]
pairwise disjoint private vertex sets of size \(t\). Let \(F_1,\ldots,F_q\) be corresponding copies of \(F\), all agreeing on their roots.

Their edge sets are pairwise disjoint: two copies can share vertices only in \(R\), and there are no edges within \(R\). Consequently their edge vectors are linearly independent. They span a subspace
\[
V=\left\{\sum_{i=1}^q x_iF_i:x\in\mathbb F_2^q\right\}
\cong\mathbb F_2^q.
\]

Let \(\mathcal A\) be any \(H\)-code. On each coset \(z+V\), pull back \(\mathcal A\cap(z+V)\) to a subset of \(\mathbb F_2^q\). Two vectors at distance \(2k\) would give two graphs whose difference is the union of exactly \(2k\) of the rooted pieces—that is, a copy of \(H\).

Lemma 3 therefore gives
\[
|\mathcal A\cap(z+V)|\le C_kq^{-k}|V|.
\]
Summing over all cosets,
\[
\frac{|\mathcal A|}{2^{\binom n2}}
\le C_kq^{-k}
=O_{F,R,k}(n^{-k}).
\]
This proves Theorem 2.

### Application to the upper bound in Theorem 1

Interchange \(a,b\) if necessary so that \(a=2k\). Take \(F=K_{1,b}\), with its \(b\) leaves as roots. The union of \(2k\) rooted copies is \(K_{2k,b}\).

Here there are \(n-b\) available private vertices, so the preceding proof gives
\[
d_{K_{a,b}}(n)
\le C_k(n-b)^{-k}
=O_{a,b}(n^{-k}).
\tag{3}
\]

## 4. Small additive labels

The matching lower bound uses the following explicit construction.

### Lemma 4

For fixed \(k\ge1\) and every \(n\), there is a finite field \(L\) of characteristic two, with
\[
|L|\le 2^{k+1}(n+1)^k,
\]
and elements \(\gamma_1,\ldots,\gamma_n\in L\) such that
\[
\sum_{i\in S}\gamma_i\ne0
\tag{4}
\]
whenever \(S\ne\varnothing\) and either:

- \(|S|\) is odd; or
- \(|S|\le2k\).

### Proof

Choose
\[
s=\lceil\log_2(n+1)\rceil,\qquad q=2^s,
\]
and distinct nonzero \(x_1,\ldots,x_n\in\mathbb F_q\). In the \(\mathbb F_2\)-vector space
\[
U=\mathbb F_2\oplus\mathbb F_q^k,
\]
put
\[
u_i=(1,x_i,x_i^3,\ldots,x_i^{2k-1}).
\]

An odd number of these vectors cannot sum to zero, because their first coordinates sum to \(1\).

Suppose a nonempty set \(S\), of size \(r\le2k\), had \(\sum_{i\in S}u_i=0\). Set
\[
p_j=\sum_{i\in S}x_i^j.
\]
We have \(p_j=0\) for every odd \(j\le2k-1\). In characteristic two,
\[
p_{2j}=p_j^2,
\]
so \(p_j=0\) for all \(1\le j\le2k\). In particular,
\[
\sum_{i\in S}x_i^j=0,\qquad 1\le j\le r.
\tag{5}
\]

The \(r\times r\) matrix \((x_i^j)_{1\le j\le r,\ i\in S}\) has determinant
\[
\left(\prod_{i\in S}x_i\right)
\prod_{\substack{i,i'\in S\\i<i'}}(x_{i'}-x_i)\ne0.
\]
But (5) says that this invertible matrix annihilates the all-ones vector, a contradiction.

Finally, \(U\) has dimension \(1+ks\) over \(\mathbb F_2\). Choose any \(\mathbb F_2\)-linear isomorphism
\[
U\longrightarrow L:=\mathbb F_{2^{1+ks}}
\]
and let \(\gamma_i\) be the images of \(u_i\). Only an additive isomorphism is required. The nonzero-sum properties are preserved, and
\[
|L|=2q^k\le2^{k+1}(n+1)^k.
\]
∎

## 5. Matching lower bound for complete bipartite graphs

Continue with \(2k\) equal to the largest even member of \(\{a,b\}\). Use the labels from Lemma 4, and define an \(\mathbb F_2\)-linear map
\[
\Phi:\mathbb F_2^{E(K_n)}\longrightarrow L,
\qquad
\Phi(G)=\sum_{\{i,j\}\in E(G)}\gamma_i\gamma_j.
\]

Consider any copy of \(K_{a,b}\), with disjoint parts \(A,B\). Its image factors:
\[
\Phi(K_{A,B})
=\sum_{i\in A}\sum_{j\in B}\gamma_i\gamma_j
=\left(\sum_{i\in A}\gamma_i\right)
 \left(\sum_{j\in B}\gamma_j\right).
\tag{6}
\]
Each part size is either odd or even and at most \(2k\). Lemma 4 makes both factors in (6) nonzero. Since \(L\) is a field,
\[
\Phi(K_{A,B})\ne0.
\]

It follows that \(\ker\Phi\) is a \(K_{a,b}\)-code: the difference of two elements of the kernel has image zero, whereas every forbidden difference has nonzero image.

Moreover,
\[
\frac{|\ker\Phi|}{2^{\binom n2}}
=\frac1{|\operatorname{im}\Phi|}
\ge\frac1{|L|}
\ge\frac1{2^{k+1}(n+1)^k}.
\tag{7}
\]
Combining (3) and (7) proves Theorem 1.

Thus a linear construction attains the correct polynomial order, while the upper bound rules out denser **nonlinear** constructions up to a constant factor.

## 6. A nonbipartite sharp-order example

Let \(H=2kK_3\), the vertex-disjoint union of \(2k\) triangles. Theorem 2, with \(F=K_3\) and \(R=\varnothing\), gives
\[
d_H(n)=O_k(n^{-k}).
\]

For the reverse inequality, use Lemma 4 and define
\[
\Psi(G)=\sum_{\substack{\{i,j\}\in E(G)\\i<j}}\gamma_i.
\]
For a triangle with vertices \(i<j<\ell\),
\[
\Psi(K_{\{i,j,\ell\}})
=\gamma_i+\gamma_i+\gamma_j
=\gamma_j.
\]
Consequently a union of \(2k\) vertex-disjoint triangles has image equal to the sum of \(2k\) distinct labels. This is nonzero by Lemma 4.

Hence \(\ker\Psi\) is an \(H\)-code of density at least \(1/|L|=\Omega_k(n^{-k})\), proving
\[
d_{2kK_3}(n)=\Theta_k(n^{-k}).
\]

## 7. What remains unresolved

These results establish the proposed decay for:

- every complete bipartite graph with a positive even number of edges;
- every graph formed from an even number of identical pieces glued along an independent root set;
- in particular, several nonbipartite families.

They also settle the family version whenever \(\mathcal H\) contains one of these graphs, since
\[
d_{\mathcal H}(n)\le d_H(n).
\]

However, an arbitrary even-edge graph need not admit the rooted-piece decomposition. For example, the argument gives no decaying upper bound for \(K_4\): private vertices belonging to different rooted pieces are nonadjacent, which is incompatible with a complete graph.

Thus the implication
\[
e(H)>0\text{ even}\quad\Longrightarrow\quad d_H(n)\to0
\]
is **not proved here in general**. The special-case arguments above are complete, but I make no claim that these bounds are new; their precise literature status has not been independently checked.