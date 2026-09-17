```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained reconstruction proves sufficient degree–cut criteria and, in particular, distinguishes every n-vertex tree with maximum degree at least floor(n/2).",
  "would_publish": false,
  "caveats": "The general problem remains unresolved by this argument; novelty and the latest literature status have not been independently checked."
}
```

# Partial reconstruction via a complete rooted subtree invariant

I do not obtain a counterexample or a proof for arbitrary trees. I rechecked and reuse the cut expansion and connected-set derivative identity from the previous attempt. The reconstruction below replaces its leaf-divisibility argument with a different complete rooted invariant.

All trees are finite, simple, and unweighted. “Determined” means determined up to isomorphism **among all trees**, not merely within a specified class.

## 1. Partial result

For a tree \(T\) of order \(n\ge 2\), define
\[
D(T)=\Delta(T),
\]
\[
b(T)=\max_{e\in E(T)}
\min\{|V(C_1)|,|V(C_2)|\},
\]
where \(C_1,C_2\) are the components of \(T-e\), and
\[
\sigma(T)=\max_{uv\in E(T)}\bigl(\deg_T(u)+\deg_T(v)\bigr).
\]

### Theorem
Each of the following is sufficient for \(T\) to be determined by \(X_T\):
\[
\boxed{D(T)>b(T),}
\tag{A}
\]
\[
\boxed{\sigma(T)>n-b(T)+1,}
\tag{B}
\]
or
\[
\boxed{D(T)\ge \left\lfloor \frac n2\right\rfloor.}
\tag{C}
\]

In fact, a two-variable invariant determined by \(X_T\) already suffices in these cases.

Condition (A) permits a high-degree centroid with **no leaf neighbors**. Condition (B) gives a separate two-hub reconstruction. Condition (C) improves the previous attempt’s \(D\ge n/2\) bound by one degree when \(n\) is odd.

I do not claim these sufficient conditions are new in the literature.

---

## 2. Extracting connected-subtree size and boundary data

For a forest \(F\), put
\[
U_F(\mathbf y)=
\sum_{A\subseteq E(F)}
\prod_{C\in\operatorname{comp}(V(F),A)}y_{|C|}.
\]

Inclusion–exclusion over edges gives
\[
X_T=\sum_{A\subseteq E(T)}(-1)^{|A|}p_{\lambda(A)}.
\]
Because \(T\) is a tree,
\[
|A|=n-\ell(\lambda(A)).
\]
Consequently,
\[
[y_\lambda]U_T
=
(-1)^{n-\ell(\lambda)}[p_\lambda]X_T.
\tag{1}
\]
Thus \(X_T\) determines \(U_T\).

For a vertex set \(S\), let \(\partial_T S\) be the set of edges with exactly one endpoint in \(S\). Define
\[
W_T(z,q)=
\sum_{\substack{\varnothing\ne S\subseteq V(T)\\T[S]\text{ connected}}}
z^{|S|}q^{|\partial_T S|}.
\tag{2}
\]

### Lemma 1
The chromatic symmetric function of a tree determines \(W_T\).

#### Proof
Differentiating \(U_T\) marks one component of a retained-edge configuration:
\[
\frac{\partial U_T}{\partial y_k}
=
\sum_{\substack{|S|=k\\T[S]\text{ connected}}}U_{T-S}.
\tag{3}
\]
For a prescribed connected \(S\), all edges inside \(S\) must be retained, all edges leaving \(S\) deleted, and the edges of \(T-S\) are arbitrary. This proves (3).

A forest with \(m\) vertices and \(c\) components satisfies
\[
U_F(t,t,\ldots)=t^c(1+t)^{m-c}.
\]
For connected \(S\), every component of \(T-S\) has exactly one edge to \(S\); hence
\[
c(T-S)=|\partial_T S|.
\]
This also holds when \(S=V(T)\), with both quantities zero.

It follows that
\[
B_k(q):=
(1-q)^{n-k}
\left.
\frac{\partial U_T}{\partial y_k}
\right|_{y_j=q/(1-q)}
=
\sum_{\substack{|S|=k\\T[S]\text{ connected}}}
q^{|\partial_T S|}.
\tag{4}
\]
Therefore
\[
W_T(z,q)=\sum_{k=1}^n z^kB_k(q)
\]
is determined. ∎

Three parameters needed below are immediately recoverable:
\[
B_1(q)=\sum_v q^{\deg(v)},
\qquad
B_2(q)=\sum_{uv\in E(T)}q^{\deg(u)+\deg(v)-2}.
\tag{5}
\]
Thus \(D(T)\) and \(\sigma(T)\) are determined.

A connected set has boundary one precisely when it is one side of a single-edge cut. Consequently,
\[
b(T)=
\max\left\{
a\le \left\lfloor n/2\right\rfloor:
[z^a q]W_T>0
\right\}.
\tag{6}
\]

In particular, all three conditions in the theorem transfer to any tree with the same \(X_T\).

---

## 3. A complete two-variable invariant for rooted trees

For a rooted tree \((T,r)\), define
\[
R_{T,r}(z,q)=
\sum_{\substack{r\in S\subseteq V(T)\\T[S]\text{ connected}}}
z^{|S|}q^{|\partial_T S|}.
\tag{7}
\]

If the branches at \(r\), rooted at their neighbors of \(r\), are
\[
(T_1,r_1),\ldots,(T_d,r_d),
\]
then
\[
\boxed{
R_{T,r}(z,q)
=
z\prod_{i=1}^d\bigl(q+R_{T_i,r_i}(z,q)\bigr).
}
\tag{8}
\]
Indeed, in each branch a connected set containing \(r\) either takes no vertex, contributing the boundary edge \(q\), or takes a connected set containing the branch root.

### Lemma 2
The polynomial \(R_{T,r}\) determines the rooted tree \((T,r)\).

#### Proof
For a rooted tree \((B,s)\) of order \(m\), write
\[
F_{B,s}(z,q)=q+R_{B,s}(z,q).
\]
As a polynomial in \(z\) over \(\mathbb Q[q]\), it is monic of degree \(m\), has constant coefficient \(q\), and satisfies
\[
F_{B,s}(z,0)=z^m.
\]
The last identity holds because the only nonempty connected set in \(B\) with boundary zero is \(V(B)\).

Thus every coefficient other than the leading coefficient is divisible by \(q\), while the constant coefficient is not divisible by \(q^2\). Eisenstein’s criterion at the prime \(q\) proves that \(F_{B,s}\) is irreducible in \(\mathbb Q[z,q]\).

Unique factorization applied to
\[
R_{T,r}/z=\prod_i F_{T_i,r_i}
\]
therefore recovers the multiset of branch factors. They are monic in \(z\), so there is no scalar ambiguity. Subtracting \(q\) recovers every \(R_{T_i,r_i}\), and induction reconstructs all rooted branches.

The base case is \(R_{T,r}=z\), the one-vertex rooted tree. ∎

This is the key change from the previous attempt: the complete rooted invariant requires only two variables.

---

## 4. A boundary separation principle

For a nonempty connected set \(S\) in a tree,
\[
|\partial_T S|
=
\sum_{v\in S}\deg_T(v)-2(|S|-1).
\]
Hence
\[
\boxed{
|S|+|\partial_T S|
=
2+\sum_{v\in S}(\deg_T(v)-1).
}
\tag{9}
\]

We also need an upper bound.

### Lemma 3
Suppose \(B\) is one component of \(T-e\), of order \(m\). For every nonempty connected \(S\subseteq V(B)\),
\[
|S|+|\partial_T S|\le m+1.
\tag{10}
\]

#### Proof
Each vertex of \(B-S\) has at most one neighbor in \(S\), since two such neighbors would create a cycle. Therefore
\[
|\partial_B S|\le m-|S|.
\]
There is at most one additional boundary edge, namely \(e\). ∎

For a polynomial \(P(z,q)\), denote by \(P^{>a}\) the sum of its monomials \(z^kq^j\) with \(k+j>a\).

### Proof of condition (A)

Recall that a centroid is a vertex \(r\) such that every component of \(T-r\) has order at most \(n/2\). A centroid exists: moving into a component of order greater than \(n/2\) strictly decreases the sum of distances to all vertices.

For any centroid \(r\),
\[
\max\{|V(B)|:B\text{ a branch at }r\}=b(T).
\tag{11}
\]
To see this, orient edges away from \(r\). The component away from \(r\) is always the smaller side of its edge cut, and its maximum order is attained by a largest branch at \(r\).

Moreover, every vertex other than \(r\) has degree at most \(b(T)\): it belongs to a branch of order at most \(b(T)\), with at most one possible edge out of that branch.

Suppose \(D>b\). It follows that the degree-\(D\) vertex is the unique centroid \(r\), and is unique.

If a connected set \(S\) avoids \(r\), it lies in a branch of order at most \(b\), so Lemma 3 gives
\[
|S|+|\partial_T S|\le b+1.
\]
If \(S\) contains \(r\), then (9) gives
\[
|S|+|\partial_T S|\ge D+1>b+1.
\]
Therefore
\[
\boxed{R_{T,r}=W_T^{>b+1}.}
\tag{12}
\]

The right-hand side is determined by \(X_T\), and Lemma 2 reconstructs \((T,r)\). Any tree with the same \(X_T\) has the same \(D>b\), so the same argument applies to it. This proves (A). ∎

---

## 5. Reconstruction from a sufficiently strong central edge

The edge version needs a little more work because an edge-containing polynomial initially forgets which branches belong to which endpoint.

### Lemma 4
Let \(e=uv\) be a marked edge of \(T\). Suppose the components of \(T-e\) have maximum order \(M\), and put
\[
s=\deg_T(u)+\deg_T(v).
\]
If
\[
s\ge M+1,
\tag{13}
\]
then \(W_T\), together with \(M,s\), determines \((T,e)\), allowing interchange of the endpoints.

#### Proof

### Step 1: Recover the polynomial of connected sets containing \(e\)

Let
\[
K_e(z,q)=
\sum_{\substack{T[S]\text{ connected}\\u,v\in S}}
z^{|S|}q^{|\partial_T S|}.
\]
A connected set not containing both endpoints lies in one component of \(T-e\), so Lemma 3 bounds its total degree by \(M+1\).

A connected set containing both endpoints has, by (9),
\[
|S|+|\partial_T S|
=
s+\sum_{w\in S\setminus\{u,v\}}(\deg_T(w)-1)
\ge s.
\tag{14}
\]

Put
\[
H=W_T^{>M+1}.
\]

If \(s>M+1\), these bounds immediately give
\[
K_e=H.
\tag{15}
\]

Now suppose \(s=M+1\). Equality in (14) occurs exactly when every additional vertex is a leaf. Such leaves must be adjacent to \(u\) or \(v\).

Let \(\ell\) be the number of leaves outside \(\{u,v\}\) adjacent to either endpoint, and let \(h\) be the number of non-leaf vertices outside \(\{u,v\}\) adjacent to either endpoint. Because \(T\) has no triangle,
\[
\ell+h=s-2.
\]
The connected three-vertex sets counted by \(H\) are exactly those obtained from \(\{u,v\}\) by adding one of these \(h\) non-leaf neighbors. Thus
\[
h=[z^3]H(z,1),
\qquad
\ell=s-2-h.
\tag{16}
\]
The missing terms are precisely the choices of a subset of the \(\ell\) leaf neighbors:
\[
\boxed{
K_e
=
H+z^2q^h(z+q)^\ell.
}
\tag{17}
\]
So \(K_e\) is recovered in both cases.

### Step 2: Recover all branches attached to the two endpoints

Let \(T_u,T_v\) be the components of \(T-e\), rooted at \(u,v\), and put
\[
A=R_{T_u,u},\qquad B=R_{T_v,v}.
\]
Then
\[
K_e=AB.
\tag{18}
\]

Let \((B_i,r_i)\) be all the branches attached to either endpoint after deleting \(u,v\). By (8),
\[
\frac{K_e}{z^2}
=
\prod_i\bigl(q+R_{B_i,r_i}\bigr).
\tag{19}
\]
Eisenstein irreducibility and Lemma 2 recover the multiset of these rooted branch trees. Their assignment to \(u\) or \(v\) is not yet known.

### Step 3: Recover the assignment to the endpoints

Write \(R_i=R_{B_i,r_i}\) and \(W_i=W_{B_i}\), and compute
\[
L=\sum_i\bigl(W_i+(q-1)R_i\bigr).
\tag{20}
\]
This counts all connected sets avoiding both endpoints. Indeed, within a branch, a set containing its root acquires one additional boundary edge in \(T\).

Connected sets in \(T\) fall into four disjoint types: containing both endpoints, only \(u\), only \(v\), or neither. Hence
\[
W_T=AB+q(A+B)+L.
\tag{21}
\]
Thus both
\[
AB=K_e,
\qquad
A+B=\frac{W_T-K_e-L}{q}
\tag{22}
\]
are recovered.

In an integral domain, the sum and product determine an unordered pair. Explicitly, if \(A',B'\) have the same sum and product, then
\[
(A-A')(A-B')=0,
\]
so \(A=A'\) or \(A=B'\), and the other equality follows from the sums.

We therefore recover \(\{A,B\}\). Lemma 2 reconstructs the two rooted halves, and joining their roots reconstructs \((T,e)\). ∎

---

## 6. Proof of condition (B)

Put
\[
b=b(T),\qquad M=n-b.
\]
Choose an edge \(e\) whose smaller side has order \(b\). Both sides have order at most \(M\).

For every other edge \(f=ab\), the connected set \(\{a,b\}\) lies within one side of \(T-e\). Lemma 3 gives
\[
\deg_T(a)+\deg_T(b)\le M+1.
\tag{23}
\]

Consequently, if
\[
\sigma(T)>M+1,
\]
the edge \(e\) must attain \(\sigma(T)\); indeed, it is the unique edge doing so. Lemma 4 applies with
\[
s=\sigma(T)>M+1.
\]

The parameters \(M,s\) are determined by \(W_T\), and the same reasoning supplies the required edge in every tree with the same \(W_T\). Hence the reconstruction is valid among all trees. This proves (B). ∎

---

## 7. Proof of condition (C)

Orders at most three are immediate. Assume \(n\ge4\) and
\[
D\ge\left\lfloor n/2\right\rfloor.
\]

If \(D>b\), condition (A) applies. Otherwise, since
\[
b\le\left\lfloor n/2\right\rfloor,
\]
we must have
\[
D=b=\left\lfloor n/2\right\rfloor,
\qquad
n\in\{2D,2D+1\}.
\tag{24}
\]

Choose a vertex \(r\) of degree \(D\), and let \(B\) be the maximum order of a branch at \(r\). Since the other \(D-1\) branches are nonempty,
\[
B\le n-D.
\tag{25}
\]
If \(B<D\), then \(r\) is a centroid, and (11) would give
\[
b=B<D,
\]
a contradiction. Thus
\[
D\le B\le n-D.
\tag{26}
\]
By (24), an edge \(e=ru\) to a branch of order \(B\) therefore cuts \(T\) into parts of orders
\[
D,\quad n-D.
\]
Since \(B\ge D\ge2\), the vertex \(u\) is not a leaf. Hence
\[
\deg_T(r)+\deg_T(u)\ge D+2\ge n-D+1.
\tag{27}
\]

Put \(M=n-D=n-b\). As in (23), every other edge has endpoint-degree sum at most \(M+1\). Thus \(e\) attains \(\sigma(T)\), and
\[
s=\sigma(T)\ge M+1.
\]
Lemma 4 reconstructs \((T,e)\).

Every tree with the same \(W_T\) has the same \(n,D,b,\sigma\), so the same construction applies to it with the same \(M,s\). This proves (C), including the equality case needed for odd \(n\). ∎

---

## 8. Classes permitted by the criteria

Two constructions illustrate that the criteria are not merely leaf-rich variants of the previous argument.

### Many arbitrary small branches

Take \(d\) arbitrary rooted trees, each of order at most \(d-1\), and attach their roots to a new vertex \(r\). Then
\[
D=d>b(T).
\]
Condition (A) applies. None of the branches needs to be a singleton, so \(r\) need not have any leaf neighbors. These trees can have as many as
\[
1+d(d-1)
\]
vertices.

### Two hubs with arbitrary rooted branches

Fix \(k\ge2\). Take two arbitrary rooted \(k\)-vertex trees. For each, add a new hub adjacent to its root and to \(k-1\) new leaves. Join the two hubs.

The resulting tree has
\[
n=4k,\qquad D=k+1,\qquad b=2k,\qquad \sigma=2k+2.
\]
Thus
\[
\sigma>n-b+1=2k+1,
\]
and condition (B) applies, even though
\[
D<\left\lfloor n/2\right\rfloor.
\]

---

## 9. What remains unresolved

The partial results above have no conjectural steps. Their limitation is the extraction of the complete rooted invariant.

For a centroid of degree \(D\), sets containing it have
\[
|S|+|\partial S|\ge D+1,
\]
whereas sets avoiding it have
\[
|S|+|\partial S|\le b+1.
\]
When \(D\le b\), these ranges generally overlap. Similarly, for an edge without the required degree-sum separation, the polynomial of edge-containing connected sets cannot be extracted by the truncation used above.

The full chromatic symmetric function contains information beyond \(W_T\); this argument does not show how to use that additional information to resolve the overlap. It produces **no non-isomorphic trees with equal chromatic symmetric functions** and does not establish uniqueness for arbitrary trees. Stanley’s general question is therefore unresolved by this work.