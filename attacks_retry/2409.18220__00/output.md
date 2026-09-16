```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove that a minimal counterexample has at most 18 vertices; the reported small-case verification further reduces the task to 1,584 explicit eighteen-vertex graphs.",
  "would_publish": false,
  "caveats": "The remaining finite verification was not executed here, and the referee report's alleged later full solution was not independently verified."
}
```

# A finite-obstruction reduction

I interpret the intended conjecture as
\[
\boxed{\quad s(G)\ge \frac45|V(G)|\qquad
\text{for every connected graph }G\text{ of order at least }5.\quad}
\tag{C}
\]
The order-four examples in the previous attempt do not address this statement.

I also do **not** use the referee report’s assertion that a later paper proves the full \(n-1\) conjecture: I have not independently verified that paper’s existence or argument.

The main unconditional result below is:

> **Theorem A.** Every counterexample to (C) contains a connected induced counterexample of order at most \(18\). Moreover, an induced-subgraph-minimal counterexample of order \(13,\ldots,18\) has a vertex whose deletion leaves components of order at most four.

There is a much smaller finite task if one accepts the small-case verification attributed to the source paper:

> **Theorem B.** Suppose that
> \[
> s(H)\ge |V(H)|-1
> \tag{B}
> \]
> has been verified for every connected graph of order at most \(10\). Then it suffices to check (C) on the following family:
> 
> * take a vertex \(v\) and seven pendant neighbors of \(v\);
> * take three mutually anticomplete connected graphs of orders \(4,3,3\);
> * join \(v\) to an arbitrary nonempty subset of each of those three graphs.
> 
> This family consists of exactly \(1,584\) isomorphism types.

The proof uses the partitioning method suggested in the question, together with a quantitative interlacing estimate. Neither theorem assumes the full square-energy conjecture.

---

## 1. Spectral preliminaries

Write \(s^\pm(M)\) for the positive and negative square energies of a real symmetric matrix.

### 1.1 Superadditivity on induced parts

For a symmetric matrix \(M\),
\[
s^+(M)=\max_{X\succeq0}
\left(2\operatorname{tr}(MX)-\operatorname{tr}(X^2)\right).
\tag{1}
\]
Indeed, the maximizing matrix is \(M_+\).

Restricting \(X\) to be block diagonal proves that, for pairwise disjoint vertex sets \(V_1,\ldots,V_k\),
\[
s^\pm(G)\ge \sum_{i=1}^k s^\pm(G[V_i]).
\tag{2}
\]
Consequently,
\[
s(G)\ge \sum_{i=1}^k s(G[V_i]).
\tag{3}
\]

Thus, if a minimal counterexample to (C) has a partition into two connected induced graphs, each of order at least five, (3) gives a contradiction.

### 1.2 Connected graphs on at most four vertices

We will use the elementary fact
\[
s^\pm(H)\ge |V(H)|-1
\qquad\text{when \(H\) is connected and }|V(H)|\le4.
\tag{4}
\]

Here is a verification, so that no computational small-case claim is needed for Theorem A.

For connected bipartite graphs,
\[
s^+(H)=s^-(H)=|E(H)|\ge |V(H)|-1.
\]
The nonbipartite cases on at most four vertices are \(K_3,K_4\), the paw, and the diamond \(K_4-e\).

The complete graphs have \(s^-(K_r)=r-1\) and \(s^+(K_r)=(r-1)^2\). Both the paw and the diamond:

* have maximum degree three, so \(\lambda_1^2\ge3\);
* have an eigenvalue \(-1\), from a pair of adjacent true twins;
* contain an induced \(P_3\), so their least eigenvalue is at most \(-\sqrt2\).

The last two eigenvalues are distinct. Hence their negative square energy is at least \(1+2=3\), proving (4).

---

## 2. A connected-partition lemma

> **Lemma 1.** Let \(k\ge2\), and let \(G\) be connected with
> \[
> |V(G)|\ge3k-2.
> \]
> Then either:
> 
> 1. \(V(G)\) has a partition into two sets inducing connected graphs, each of order at least \(k\); or
> 2. some vertex \(v\) has every component of \(G-v\) of order at most \(k-1\).

### Proof

Take a spanning tree \(T\) and a centroid \(v\) of \(T\). Thus every component of \(T-v\) has order at most \(|V(G)|/2\).

If one such component has order at least \(k\), it and its complement give the first alternative: both sets induce connected graphs, and both have order at least \(k\).

We may therefore suppose that every component of \(T-v\) has order at most \(k-1\). Call these components the tree branches.

Suppose a component of \(G-v\) has order at least \(k\). Contract its tree branches to obtain a connected auxiliary graph, assigning each contracted vertex the order of its branch. Each weight is at most \(k-1\).

Grow a connected set of auxiliary vertices until its total weight first reaches \(k\). Its weight is between \(k\) and \(2k-2\). The corresponding union \(S\) of tree branches induces a connected graph. Its complement is connected through \(v\), and
\[
|V(G)\setminus S|
\ge (3k-2)-(2k-2)=k.
\]
This again gives the first alternative.

Otherwise every component of \(G-v\) has order at most \(k-1\). ∎

For \(k=5\), every connected graph of order at least \(13\) either admits the desired \(5\)-versus-\(5\) partition or has a vertex with components of order at most four.

---

## 3. Square energy around a separating vertex

Let \(G-v\) have connected components
\[
C_1,\ldots,C_t,\qquad b_i=|V(C_i)|,
\]
and put
\[
n=|V(G)|,\qquad r=\max_i b_i.
\]
In this section assume
\[
s^\pm(C_i)\ge b_i-1 \quad\text{for every }i.
\tag{5}
\]
By (4), this assumption is automatic when \(r\le4\).

### 3.1 A basic bound

> **Lemma 2.** Under these assumptions,
> \[
> s^\pm(G)\ge n-r.
> \tag{6}
> \]

### Proof

Let \(B=A(G-v)\), and define
\[
\rho_+(M)=\max\{\lambda_{\max}(M),0\},\qquad
\rho_-(M)=\max\{-\lambda_{\min}(M),0\}.
\]
Interlacing gives, for either sign,
\[
s^\pm(G)\ge
s^\pm(B)+\rho_\pm(G)^2-\rho_\pm(B)^2.
\tag{7}
\]

Choose a component \(C_j\) attaining the relevant extremum of \(B\). Since \(G\) is connected, choosing one neighbor of \(v\) in each component gives an induced \(K_{1,t}\). Hence
\[
\rho_\pm(G)^2\ge t.
\tag{8}
\]
Using (5) and discarding the nonnegative quantity
\(s^\pm(C_j)-\rho_\pm(C_j)^2\), we obtain
\[
\begin{aligned}
s^\pm(G)
&\ge t+\sum_{i\ne j}s^\pm(C_i)\\
&\ge t+\sum_{i\ne j}(b_i-1)\\
&=n-b_j\\
&\ge n-r.
\end{aligned}
\]
This also covers the case where all components are single vertices. ∎

### 3.2 A quantitative improvement

Let
\[
u=\bigl|\{i:b_i\ge2\}\bigr|.
\]

> **Lemma 3.** If \(t\ge4\), then
> \[
> s^\pm(G)\ge n-r+\frac ut.
> \tag{9}
> \]
> Also, without the restriction \(t\ge4\),
> \[
> s^\pm(G)\ge n-u-1.
> \tag{10}
> \]

### Proof of (9)

For each component choose a neighbor \(x_i\) of \(v\). In each nonsingleton component, also choose a neighbor \(y_i\) of \(x_i\) within that component.

The induced graph \(F\) on these chosen vertices consists of:

* \(t-u\) ordinary pendant edges at \(v\);
* \(p\) paths \(v x_i y_i\);
* \(q\) triangles \(v x_i y_i v\),

where \(p+q=u\).

Write \(\lambda_{\min}(F)=-x\). Since \(F\) contains an induced \(K_{1,t}\),
\[
x\ge\sqrt t\ge2.
\]
The Schur complement at \(v\) gives
\[
x=\frac{t-u}{x}
  +\frac{px}{x^2-1}
  +\frac{2q}{x+1}.
\]
Therefore
\[
x^2
=t+\frac{p}{x^2-1}
  +q\frac{x-1}{x+1}.
\tag{11}
\]
For \(x\ge2\),
\[
\frac{x-1}{x+1}\ge \frac1{x^2-1}.
\]
Consequently,
\[
x^2\ge t+\frac{u}{x^2-1}.
\]
Writing \(z=x^2-t\), this implies
\[
z\ge
\frac{\sqrt{(t-1)^2+4u}-(t-1)}2
\ge \frac ut.
\tag{12}
\]
For the last inequality, the displayed quadratic root is at most one because \(u\le t\); its defining equation then gives
\(z=u/(t-1+z)\ge u/t\).

Interlacing now yields
\[
\rho_-(G)^2\ge t+\frac ut.
\]
For a nonnegative symmetric matrix, the largest eigenvalue is at least the absolute value of the least eigenvalue. Thus the same bound holds for \(\rho_+(G)^2\).

Substitute this improvement of (8) into the proof of Lemma 2.

### Proof of (10)

Partition the vertices into:

* \(v\) together with all singleton components of \(G-v\), inducing a star;
* the \(u\) nonsingleton components.

The star has square energy \(t-u\). Thus (2) and (5) give
\[
s^\pm(G)\ge
(t-u)+\sum_{b_i\ge2}(b_i-1)
=n-u-1.
\]
∎

Combining the estimates, for \(t\ge4\) we have
\[
\boxed{\quad
s(G)\ge
\max\left\{n-u-1,\ n-r+\frac ut\right\}.
\quad}
\tag{13}
\]

---

## 4. Proof of Theorem A

Let \(G\) be a connected induced-subgraph-minimal counterexample to (C).

It cannot have a connected vertex partition with both parts of order at least five: both proper induced parts would satisfy (C), contradicting (3).

If \(n\ge13\), Lemma 1 therefore supplies a vertex \(v\) whose deletion leaves components of order at most four. Lemma 2 gives
\[
s(G)\ge n-4.
\]
For \(n\ge20\),
\[
n-4\ge \frac45n,
\]
a contradiction. Thus \(n\le19\).

It remains to exclude \(n=19\). In that case \(t\ge5\). If \(u\le2\), (10) gives
\[
s(G)\ge18-u\ge16>\frac{76}{5}.
\]
If \(u\ge3\), then
\[
18=\sum_i b_i\ge t+u,
\]
so
\[
\frac ut\ge\frac{u}{18-u}\ge\frac3{15}=\frac15.
\]
Equation (9) consequently gives
\[
s(G)\ge19-4+\frac15=\frac{76}{5}.
\]
This is again a contradiction.

Hence every induced-subgraph-minimal counterexample has order at most \(18\), with the asserted separating-vertex structure whenever its order is at least \(13\). ∎

This theorem is unconditional: it does not use the source’s reported computer verification.

---

## 5. Reduction using the reported base check

For the rest of this section, assume the explicit finite statement (B):
\[
s(H)\ge |V(H)|-1
\quad\text{for every connected }H\text{ of order at most }10.
\]

This assumption is reportedly verified in the source paper, but I have not independently rerun or certified that computation.

### 5.1 Orders \(11\)–\(14\)

* **Order \(11\).** Delete a vertex whose deletion leaves the graph connected, obtaining
  \[
  s(G)\ge 9>\frac{44}{5}.
  \]

* **Order \(12\).** Apply Lemma 1 with \(k=2\). A connected partition has both parts of order at most ten, giving \(s(G)\ge12-2=10\). Otherwise \(G\) is a star, which has square energy eleven.

* **Order \(13\).** Apply Lemma 1 with \(k=3\). A partition gives \(s(G)\ge11\). Otherwise Lemma 2, with \(r\le2\), gives the same bound.

* **Order \(14\).** Apply Lemma 1 with \(k=4\). A partition gives \(s(G)\ge12\). Otherwise \(r\le3\).
  
  If \(r\le2\), Lemma 2 suffices. If \(u\le1\), (10) gives \(s(G)\ge12\). In the remaining case \(r=3\) and \(u\ge2\). Since at least one component has order three,
  \[
  13=\sum_i b_i\ge t+u+1,
  \]
  whence \(t\le12-u\) and
  \[
  \frac ut\ge\frac2{10}=\frac15.
  \]
  Equation (9) gives
  \[
  s(G)\ge14-3+\frac15=\frac{56}{5}.
  \]

Thus all four orders satisfy (C).

### 5.2 Orders \(15\)–\(17\)

Suppose a smallest remaining counterexample has order \(n\in\{15,16,17\}\). Lemma 1 again gives a vertex \(v\) with component orders at most four.

Let \(b_1\ge b_2\) be the two largest component orders.

If
\[
b_1+b_2\ge n-10,
\tag{14}
\]
partition \(G\) into those two components and the connected remainder containing \(v\). Each part has order at most ten. By (B),
\[
s(G)\ge n-3\ge\frac45n.
\tag{15}
\]

If (14) fails, the remaining possibilities are:

| \(n\) | Possibility when \(r=4\) | Lower bound |
|---|---|---|
| \(15\) | Impossible: \(b_1+b_2\ge4+1=5=n-10\) | — |
| \(16\) | One order-four component; all others singletons | Partition into that component and a star: \(s(G)\ge n-2\) |
| \(17\) | One order-four component; all others have order at most two | Delete that component and apply Lemma 2: \(s(G)\ge n-3\) |

If \(r\le3\), Lemma 2 directly gives \(s(G)\ge n-3\). This excludes all three orders.

Consequently, under (B), a minimal counterexample must have order exactly \(18\).

---

## 6. The eighteen-vertex cases

Let \(G\) be such a minimal counterexample, with the separating vertex \(v\).

If \(r\le3\), Lemma 2 gives \(s(G)\ge15\). If there are two order-four components, partition off those two components; the remainder has order ten, so (B) again gives
\[
s(G)\ge15.
\]

We may therefore assume that there is exactly one order-four component.

If all remaining components have order at most two, partition off the order-four component and use Lemma 2 on the remainder:
\[
s(G)\ge3+(14-2)=15.
\]
Thus there is also an order-three component.

If \(u\le2\), (10) gives \(s(G)\ge15\). If \(u\ge4\), the order-four and order-three components imply
\[
17=\sum_i b_i\ge t+u+3.
\]
Hence
\[
\frac ut\ge \frac{u}{14-u}\ge\frac4{10}=\frac25,
\]
and (9) gives
\[
s(G)\ge18-4+\frac25=\frac{72}{5}.
\]

The only remaining possibility is \(u=3\), with nonsingleton component orders
\[
(4,3,2)\quad\text{or}\quad(4,3,3).
\tag{16}
\]

### 6.1 Eliminating the profile \((4,3,2)\)

There are eight singleton components. After partitioning off the order-four and order-three components, the remaining graph consists of \(v\), eight pendant neighbors, and one order-two component.

This remaining graph is either a tree, or a triangle with eight pendant edges at one triangle vertex. In either case its square energy is at least ten.

For completeness, a triangle with \(a\) pendant edges at one vertex has square energy at least \(a+2\). For \(a\ge1\), its spectrum consists of zeros, an eigenvalue \(-1\), and the eigenvalues of
\[
\begin{pmatrix}
0&\sqrt a&\sqrt2\\
\sqrt a&0&0\\
\sqrt2&0&1
\end{pmatrix}.
\]
This matrix has exactly one negative eigenvalue, say \(-x\), and
\[
x^2=a+\frac{2x}{x+1}.
\]
Since \(x\ge1\),
\[
a+1\le x^2<a+2.
\]
Thus
\[
s^-=1+x^2\ge a+2,
\]
while, using the \(a+3\) edges,
\[
s^+=2(a+3)-s^->a+3.
\]
The case \(a=0\) is \(K_3\).

Therefore the profile \((4,3,2)\) gives
\[
s(G)\ge3+2+10=15.
\]

Only \((4,3,3)\), with seven singleton components, remains. This is precisely the family in Theorem B.

### 6.2 Counting the remaining graphs

A branch is specified by a connected graph \(C\) and a nonempty subset \(S\subseteq V(C)\), where \(S=N(v)\cap V(C)\). Two such specifications are equivalent when an isomorphism maps both \(C\) and \(S\) to each other.

For order three there are eight branch types:

* five for \(P_3\);
* three for \(K_3\).

For order four the counts are:

| \(C\) | Nonempty-subset orbits under \(\operatorname{Aut}(C)\) |
|---|---:|
| \(P_4\) | 9 |
| \(K_{1,3}\) | 7 |
| \(C_4\) | 5 |
| Paw | 11 |
| Diamond | 8 |
| \(K_4\) | 4 |
| **Total** | **44** |

The two order-three branches form an unordered pair, allowing repetition. Thus the number of graphs is
\[
44\binom{8+1}{2}=44\cdot36=\boxed{1584}.
\]
There is no ambiguity from changing the central vertex: it has degree at least ten, while every other vertex has degree at most four. This completes the proof of Theorem B. ∎

---

## 7. What remains unproved

The argument establishes the following **finite certificate implication**:
\[
\boxed{\text{(B) and the \(1,584\)-graph check imply (C) in every order.}}
\]

The remaining check is fully specified:

1. Enumerate the \(44\) marked connected order-four graphs \((C,S)\).
2. Enumerate unordered pairs, with repetition, of the eight marked connected order-three graphs.
3. Form the corresponding eighteen-vertex graph with seven additional pendant neighbors of the common central vertex.
4. Compute its integer characteristic polynomial.
5. Isolate its real algebraic roots, retaining multiplicities, and compare both sums of squared positive/negative roots with
   \[
   \frac{72}{5}.
   \]

An exact real-algebraic implementation avoids the issue of floating-point comparisons near equality.

**I have not executed this enumeration.** Nor have I independently certified the reported verification (B). Consequently, the finite reductions above are proved, but the original \(4n/5\) conjecture is **not claimed proved here**. The remaining gap is a concrete finite verification, not an unidentified infinite family or another conjecture.