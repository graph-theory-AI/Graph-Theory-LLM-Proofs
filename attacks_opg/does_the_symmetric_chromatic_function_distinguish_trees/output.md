```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained reconstruction argument proves the conjecture for an explicit leaf-rich-centroid class, including every tree whose maximum degree is at least half its order.",
  "would_publish": false,
  "caveats": "The general problem is not settled; novelty of the sufficient condition and the latest literature status have not been verified."
}
```

## 1. Partial result

All trees below are finite, simple, and unweighted. “Determined” means determined up to isomorphism among trees.

For a vertex \(r\) of a tree \(T\) with at least two vertices, define
\[
b_T(r)=\max\{|V(C)|:C\text{ is a component of }T-r\},
\]
and let \(\ell_T(r)\) be the number of leaf-neighbors of \(r\).

### Theorem
Suppose that \(T\) has a vertex \(r\) satisfying
\[
\boxed{\ell_T(r)\ge b_T(r)-1.}
\]
Then \(T\) is determined by its chromatic symmetric function.

In particular:

### Corollary
Every \(n\)-vertex tree \(T\) satisfying
\[
\boxed{\Delta(T)\ge n/2}
\]
is determined by its chromatic symmetric function.

The theorem permits arbitrary rooted trees as branches at \(r\), provided there are sufficiently many leaves directly adjacent to \(r\). Thus it is not restricted to caterpillars, spiders, or trees with few branching vertices.

I give a self-contained proof. I do not claim that this sufficient condition is new.

---

## 2. Replacing the chromatic symmetric function by a cut polynomial

Use independent variables \(y_1,y_2,\ldots\). For a forest \(F\), put
\[
U_F(\mathbf y)
=
\sum_{A\subseteq E(F)}
\prod_{C\in\operatorname{comp}(V(F),A)}y_{|C|}.
\]

For a tree \(T\) on \(n\) vertices, inclusion–exclusion in the definition of \(X_T\) gives
\[
X_T
=
\sum_{A\subseteq E(T)}(-1)^{|A|}p_{\lambda(A)},
\]
where \(\lambda(A)\) lists the component orders of \((V(T),A)\).

Because \(T\) is a tree,
\[
|A|=n-\ell(\lambda(A)).
\]
Consequently,
\[
[y_\lambda]U_T
=
(-1)^{n-\ell(\lambda)}[p_\lambda]X_T.
\]
The power-sum functions form a basis over \(\mathbb Q\), so, for trees,
\[
X_T=X_{T'}\quad\Longleftrightarrow\quad U_T=U_{T'}.
\]

We may therefore work entirely with \(U_T\).

---

## 3. Information recoverable from \(U_T\)

### 3.1. The largest smaller side of an edge cut

Define
\[
b(T)=
\max_{e\in E(T)}
\min\{|V(C_1)|,|V(C_2)|\},
\]
where \(C_1,C_2\) are the components of \(T-e\).

The terms of \(U_T\) having exactly two factors correspond precisely to deleting one edge. Hence \(U_T\) determines \(b(T)\):
\[
b(T)=
\max\left\{
a\le \lfloor n/2\rfloor:
[y_a y_{n-a}]U_T>0
\right\}.
\]

Recall that a **centroid** is a vertex \(r\) for which every component of \(T-r\) has order at most \(n/2\). Every tree has a centroid.

If \(r\) is any centroid, then
\[
\boxed{b_T(r)=b(T).}
\]
Indeed, orient each edge away from \(r\). Its component away from \(r\) is contained in a branch at \(r\), and therefore has order at most \(n/2\). Its order is consequently the smaller side of that edge cut. The maximum occurs on an edge joining \(r\) to a largest branch.

### 3.2. Degrees and endpoint-degree sums

For \(1\le k\le n\), differentiation gives
\[
\frac{\partial U_T}{\partial y_k}
=
\sum_{\substack{S\subseteq V(T)\\ |S|=k\\T[S]\text{ connected}}}
U_{T-S}.
\tag{1}
\]
To see this, mark a component of order \(k\) in an edge-subset configuration. For a prescribed connected vertex set \(S\), all edges of \(T[S]\) must be retained, all edges leaving \(S\) must be deleted, and the edges of \(T-S\) are arbitrary.

A forest with \(m\) vertices and \(c\) components satisfies
\[
U_F(t,t,\ldots)=t^c(1+t)^{m-c}.
\]
For connected \(S\), the number of components of \(T-S\) equals the number \(|\partial S|\) of edges leaving \(S\). Thus, if
\[
H_k(t)=
\left.\frac{\partial U_T}{\partial y_k}\right|_{y_j=t\text{ for all }j},
\]
then
\[
(1-q)^{n-k}H_k\!\left(\frac{q}{1-q}\right)
=
\sum_{\substack{|S|=k\\T[S]\text{ connected}}}q^{|\partial S|}.
\tag{2}
\]

For \(k=1\), this recovers
\[
\sum_{v\in V(T)}q^{\deg(v)}.
\tag{3}
\]
For \(k=2\), it recovers
\[
J_T(q):=
\sum_{uv\in E(T)}q^{\deg(u)+\deg(v)-2}.
\tag{4}
\]

In particular, \(U_T\) determines the degree sequence, \(\Delta(T)\), and the multiset of endpoint-degree sums over edges.

### 3.3. Recognizing a sufficiently high-degree centroid

Write \(b=b(T)\). If
\[
D:=\Delta(T)>b,
\]
then the vertex of degree \(D\) is the unique centroid.

Indeed, fix any centroid \(r\). Every other vertex lies in a branch of order at most \(b\), and has degree at most \(b\). Thus the vertex of degree \(D>b\) must be \(r\), and is unique.

Moreover, \(U_T\) determines the number of leaf-neighbors of this centroid:
\[
\boxed{\ell_T(r)=[q^{D-1}]J_T(q).}
\tag{5}
\]

Here is the separation that justifies (5). An edge not incident with \(r\) lies inside a branch \(S\) of order at most \(b\). For adjacent \(u,v\in S\),
\[
\deg_{T[S]}(u)+\deg_{T[S]}(v)\le |S|.
\]
At most one endpoint has an additional edge to \(r\), so
\[
\deg_T(u)+\deg_T(v)\le b+1.
\]
On the other hand, an edge incident with \(r\) has endpoint-degree sum at least \(D+1>b+1\). Among these edges, the sum equals \(D+1\) exactly when the other endpoint is a leaf. This proves (5).

---

## 4. A complete invariant for rooted trees

For a rooted tree \((T,r)\), define
\[
P_{T,r}(z;\mathbf y)
=
\sum_{A\subseteq E(T)}
z^{|C_r(A)|}
\prod_{\substack{C\in\operatorname{comp}(V(T),A)\\C\ne C_r(A)}}
y_{|C|},
\]
where \(C_r(A)\) is the component containing \(r\).

Let \(\Phi\) be the \(\mathbb Q[\mathbf y]\)-linear map defined on positive powers of \(z\) by
\[
\Phi(z^s)=y_s.
\]
Then
\[
\Phi(P_{T,r})=U_T.
\tag{6}
\]

Suppose the branches at \(r\), rooted at their neighbors of \(r\), are
\[
(T_1,r_1),\ldots,(T_d,r_d).
\]
Deleting or retaining each edge incident with \(r\) gives the factorization
\[
\boxed{
P_{T,r}(z)
=
z\prod_{i=1}^{d}\bigl(U_{T_i}+P_{T_i,r_i}(z)\bigr).
}
\tag{7}
\]

### Lemma 1
The polynomial \(P_{T,r}\) determines the rooted tree \((T,r)\).

#### Proof
For a rooted tree \((S,s)\) of order \(m\), consider
\[
F_{S,s}(z)=U_S+P_{S,s}(z).
\]
The term \(y_m\) occurs in \(U_S\) with coefficient \(1\), and every other term of \(U_S\) uses only variables of index less than \(m\). Also, \(P_{S,s}\) does not involve \(y_m\). Hence
\[
F_{S,s}(z)
=
y_m+f(y_1,\ldots,y_{m-1},z).
\]
This is irreducible in the polynomial ring: it is linear in \(y_m\) with coefficient \(1\).

Furthermore, \(F_{S,s}\) is monic of degree \(m\) in \(z\). Thus unique factorization applied to (7) recovers the multiset of branch factors \(F_{T_i,r_i}\), without scalar ambiguity.

Since \(P_{T_i,r_i}(0)=0\),
\[
U_{T_i}=F_{T_i,r_i}(0),
\qquad
P_{T_i,r_i}(z)=F_{T_i,r_i}(z)-F_{T_i,r_i}(0).
\]
Induction on the order now recovers every rooted branch and hence \((T,r)\). The one-vertex tree is the base case. ∎

---

## 5. Recovering the rooted invariant from a sufficiently leafy root

The following is the central algebraic step.

### Lemma 2
Let \((T,r)\) and \((T',r')\) have the same order. Suppose that, for some \(b\ge1\),

1. every branch at either root has order at most \(b\);
2. both roots have at least \(b-1\) leaf-neighbors.

If \(U_T=U_{T'}\), then \((T,r)\cong(T',r')\).

#### Proof
Write
\[
P_{T,r}(z)=\sum_{s=1}^{n}q_s(\mathbf y)z^s.
\]
Every non-root component in its definition lies inside one branch at \(r\). Thus each \(q_s\) involves only \(y_1,\ldots,y_b\).

Using (6), for every \(s>b\) we therefore have
\[
q_s=\frac{\partial U_T}{\partial y_s}.
\tag{8}
\]
There are no extra derivative contributions, because none of the coefficients \(q_t\) involves \(y_s\).

Apply the same observation to \(T'\). Since \(U_T=U_{T'}\),
\[
\deg_z\bigl(P_{T,r}-P_{T',r'}\bigr)\le b.
\tag{9}
\]

A leaf branch contributes the factor \(z+y_1\) in (7). Consequently, both rooted polynomials are divisible by
\[
G_b(z):=z(z+y_1)^{b-1},
\]
whose \(z\)-degree is \(b\). By (9), their difference has the form
\[
P_{T,r}-P_{T',r'}=c(\mathbf y)G_b(z).
\]

Applying \(\Phi\) gives
\[
0
=
c(\mathbf y)
\sum_{j=0}^{b-1}
\binom{b-1}{j}y_1^{\,b-1-j}y_{j+1}.
\]
The displayed sum is nonzero—it is \(U\) for the star on \(b\) vertices. The polynomial ring is an integral domain, so \(c=0\).

Thus \(P_{T,r}=P_{T',r'}\), and Lemma 1 completes the proof. ∎

Notice that Lemma 2 assumes the leaf condition for both trees. The next step establishes why that condition transfers to an arbitrary tree with the same \(X\).

---

## 6. Proof of the theorem

Let \(T\) have a vertex \(r\) satisfying
\[
\ell:=\ell_T(r)\ge b_T(r)-1,
\]
and write \(b=b_T(r)\). Suppose \(X_T=X_{T'}\), equivalently \(U_T=U_{T'}\).

If \(b=1\), then \(T\) is a star. Its degree sequence forces \(T'\) to be the same star. Hence assume \(b\ge2\).

There is a non-leaf branch of order \(b\), in addition to the \(\ell\) leaf branches. Therefore
\[
n\ge 1+b+\ell\ge 2b.
\]
Thus \(r\) is a centroid, and
\[
b=b(T)=b(T').
\]

Let \(D=\deg_T(r)\). Since \(r\) has at least \(b-1\) leaf branches and at least one non-leaf branch,
\[
D\ge b.
\]
Every other vertex has degree at most \(b\), so \(D=\Delta(T)=\Delta(T')\).

There are two cases.

### Case 1: \(D>b\)

By Section 3.3, \(T'\) has a unique centroid \(r'\) of degree \(D\). Equations (4)–(5) show that
\[
\ell_{T'}(r')=\ell_T(r)\ge b-1.
\]
Both centroids have all branches of order at most \(b\). Lemma 2 gives
\[
(T,r)\cong(T',r').
\]

### Case 2: \(D=b\)

The inequalities above force \(r\) to have exactly \(b-1\) leaf branches and exactly one non-leaf branch, of order \(b\). Hence
\[
n=2b.
\]

Choose a vertex \(r'\) of degree \(b\) in \(T'\). Each branch at \(r'\) has order at most
\[
n-D=b,
\]
because the other \(D-1\) branches each contain at least one vertex. Thus \(r'\) is a centroid.

Since \(b(T')=b\), one branch at \(r'\) has order \(b\). The other \(b-1\) branches together contain
\[
(2b-1)-b=b-1
\]
vertices, so all are leaves. Again Lemma 2 applies.

This proves the theorem in every case. ∎

---

## 7. Consequences

### 7.1. Maximum degree at least half the order

Let \(r\) have degree \(D\ge n/2\), and put \(b=b_T(r)\), \(\ell=\ell_T(r)\).

If \(b=1\), \(T\) is a star. Otherwise, count one branch of order \(b\), the \(\ell\) leaf branches, and the remaining non-leaf branches:
\[
n-1
\ge
b+\ell+2(D-\ell-1).
\]
Rearranging,
\[
\ell\ge b+2D-n-1\ge b-1.
\]
The theorem applies, proving the corollary. ∎

### 7.2. Leaf padding of an arbitrary rooted tree

Let \((R,r)\) be any rooted tree with at least two vertices, and let
\[
b=\max\{|V(C)|:C\text{ is a component of }R-r\}.
\]
Attach \(b-1\) new leaves to \(r\). The resulting tree is determined by its chromatic symmetric function.

This allows the original branches to have arbitrary depth and branching structure. It does **not**, however, imply that the unpadded tree \(R\) is determined.

---

## 8. What remains unresolved

The rooted polynomial \(P_{T,r}\) is a complete rooted invariant. For a centroid, \(U_T\) determines its coefficients of \(z^s\) for \(s>b(T)\). The leaf hypothesis is what forces the missing low-degree coefficients.

There is a genuine algebraic obstruction to simply dropping that hypothesis. For \(b\ge2\), set
\[
g(z)=z(z+y_1)^{b-2},\qquad
a=\Phi(g),\qquad c=\Phi(zg).
\]
Then
\[
K(z)=g(z)(az-c)
\]
is nonzero, has \(z\)-degree \(b\), is divisible by \(z(z+y_1)^{b-2}\), and satisfies
\[
\Phi(K)=a\Phi(zg)-c\Phi(g)=0.
\]
Thus the high-degree tail and one fewer guaranteed leaf factor do not suffice for this purely algebraic reconstruction argument.

These kernel elements are **not counterexamples involving non-isomorphic trees**: the additional restrictions on genuine rooted-tree polynomials have not been addressed in general. The existence or nonexistence of a pair of non-isomorphic trees with equal chromatic symmetric functions is therefore not resolved here.