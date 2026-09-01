```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained maximal-independent-set argument gives max_k D(n,k) at most 3^{n/3+o(n)}, while the five-vertex lift gives 2^{n/5-O(1)}, leaving a substantial gap in the exponential base.",
  "would_publish": false,
  "caveats": "The exact exponential rate, and even existence of a limiting rate, remain open."
}
```

# Mathematical writeup

## 1. Definitions and statement

I use the standard token-jumping reconfiguration graph. For a graph \(G\), let \(\mathcal R_k(G)\) have as vertices the independent \(k\)-subsets of \(V(G)\), with two sets adjacent when their intersection has size \(k-1\). The distance between two sets is their graph distance in \(\mathcal R_k(G)\), provided they lie in the same component. Let \(D(n,k)\) be the maximum finite such distance over all \(n\)-vertex graphs, and put
\[
M(n):=\max_{0\le k\le n}D(n,k).
\]

The source construction yields an exponential lower bound with base \(2^{1/5}\). I give:

1. a self-contained version of the five-vertex doubling construction;
2. a profile-sensitive upper bound in terms of maximal independent sets;
3. the resulting uniform estimate
   \[
   2^{n/5-O(1)}
   \le M(n)
   \le \bigl(\lfloor n/2\rfloor+1\bigr)3^{n/3}-1;
   \]
4. a sharper upper bound when \(k/n\) is large.

Consequently,
\[
2^{1/5}
\le \liminf_{n\to\infty}M(n)^{1/n}
\le \limsup_{n\to\infty}M(n)^{1/n}
\le 3^{1/3}.
\]
Numerically, the known interval for a possible exponential base is
\[
1.14869\ldots\le \rho\le 1.44224\ldots.
\]

This does not determine the precise asymptotics.

---

## 2. A maximal-independent-set profile bound

Write \(\operatorname{MIS}(G)\) for the family of maximal, not necessarily maximum, independent sets of \(G\).

### Lemma 2.1

Let
\[
I_0,I_1,\dots,I_\ell
\]
be a shortest path in \(\mathcal R_k(G)\). For each \(i\), choose a maximal independent set \(M_i\supseteq I_i\). Then
\[
\ell+1
\le
\sum_{\substack{M\in\operatorname{MIS}(G)\\ |M|\ge k}}
\bigl(\min\{k,|M|-k\}+1\bigr).
\]

#### Proof

Fix a maximal independent set \(M\), and suppose \(I_i,I_j\subseteq M\), with \(i<j\). Since every subpath of a shortest path is shortest,
\[
j-i=d_{\mathcal R_k(G)}(I_i,I_j).
\]

Both sets are \(k\)-subsets of the independent set \(M\). Thus one can transform \(I_i\) into \(I_j\) entirely inside \(M\), replacing the elements of \(I_i\setminus I_j\) one at a time. Hence
\[
j-i\le |I_i\setminus I_j|.
\]
Moreover,
\[
|I_i\setminus I_j|\le k
\]
and, since \(I_i\cup I_j\subseteq M\),
\[
k+|I_i\setminus I_j|=|I_i\cup I_j|\le |M|,
\]
so
\[
|I_i\setminus I_j|\le |M|-k.
\]
Consequently
\[
j-i\le \min\{k,|M|-k\}.
\]

It follows that all indices assigned to a fixed \(M\) lie in an interval of length at most \(\min\{k,|M|-k\}\), and therefore there are at most
\[
\min\{k,|M|-k\}+1
\]
such indices. Summing over \(M\) proves the claim. \(\square\)

In particular, if
\[
T_k(G):=
\bigl|\{M\in\operatorname{MIS}(G):|M|\ge k\}\bigr|,
\]
then
\[
D_G(k)+1
\le
\bigl(\min\{k,n-k\}+1\bigr)T_k(G),
\tag{2.1}
\]
where \(D_G(k)\) denotes the largest finite distance in \(\mathcal R_k(G)\).

---

## 3. A weighted maximal-independent-set estimate

Define
\[
P_G(x):=\sum_{M\in\operatorname{MIS}(G)}x^{|M|}.
\]

### Lemma 3.1

For every \(x\ge1\) and every \(n\)-vertex graph \(G\),
\[
P_G(x)\le c(x)^n,
\qquad
c(x):=\max_{r\ge1}(rx)^{1/r}.
\tag{3.1}
\]

#### Proof

We induct on \(n\). The empty graph on no vertices has \(P_G(x)=1\), so the assertion holds.

Let \(v\) be a minimum-degree vertex, and put \(d=\deg(v)\), \(r=d+1\). Every maximal independent set intersects \(N[v]\), since otherwise \(v\) could be added.

For \(w\in N[v]\), if \(M\) is a maximal independent set containing \(w\), then
\[
M\setminus\{w\}
\]
is a maximal independent set of \(G-N[w]\). Indeed, if a vertex outside \(N[w]\) had no neighbor in \(M\setminus\{w\}\), it would also have no neighbor in \(M\), contradicting maximality of \(M\).

Therefore
\[
P_G(x)
\le
x\sum_{w\in N[v]} P_{G-N[w]}(x).
\]
Since \(v\) has minimum degree, every \(w\in N[v]\) satisfies
\[
|N[w]|\ge d+1=r.
\]
Using the induction hypothesis and \(c(x)\ge1\),
\[
P_G(x)
\le xr\,c(x)^{n-r}
\le c(x)^n,
\]
because \(c(x)^r\ge rx\) by definition. \(\square\)

For \(x\ge1\), only \(r=1,2,3\) can attain the maximum in (3.1), and direct comparison gives
\[
c(x)=
\begin{cases}
(3x)^{1/3},&1\le x\le 9/8,\\[2mm]
(2x)^{1/2},&9/8\le x\le2,\\[2mm]
x,&x\ge2.
\end{cases}
\tag{3.2}
\]

Since every maximal independent set counted by \(T_k(G)\) contributes at least \(x^k\) to \(P_G(x)\),
\[
T_k(G)\le x^{-k}P_G(x)\le x^{-k}c(x)^n.
\]
Combining this with (2.1) gives the following.

### Theorem 3.2

For every \(n,k\),
\[
D(n,k)+1
\le
\bigl(\min\{k,n-k\}+1\bigr)
\inf_{x\ge1}\frac{c(x)^n}{x^k}.
\tag{3.3}
\]

There is also the elementary state-count bound
\[
D(n,k)+1\le \binom nk.
\tag{3.4}
\]

---

## 4. Explicit dependence on \(k/n\)

Let \(\alpha=k/n\). Optimizing (3.3) using (3.2) gives
\[
D(n,k)+1
\le
\bigl(\min\{k,n-k\}+1\bigr)b(\alpha)^n,
\tag{4.1}
\]
where
\[
b(\alpha)=
\begin{cases}
3^{1/3},&0\le\alpha\le1/3,\\[2mm]
\dfrac32\left(\dfrac89\right)^\alpha,
   &1/3\le\alpha\le1/2,\\[3mm]
2^{1-\alpha},&1/2\le\alpha\le1.
\end{cases}
\tag{4.2}
\]

For example,
\[
b(2/5)
=
\frac32\left(\frac89\right)^{2/5}
=
1.4310\ldots,
\]
while \(b(1/2)=\sqrt2\).

Taking \(x=1\) in (3.3) yields the uniform estimate
\[
M(n)+1
\le
\bigl(\lfloor n/2\rfloor+1\bigr)3^{n/3}.
\tag{4.3}
\]

A useful parameterized consequence comes from taking \(x=2\), for which \(c(2)=2\).

### Corollary 4.1

For every \(n,k\),
\[
D(n,k)
\le
\bigl(\min\{k,n-k\}+1\bigr)2^{n-k}-1.
\tag{4.4}
\]
In particular, writing \(k=n-r\),
\[
D(n,n-r)\le (r+1)2^r-1.
\tag{4.5}
\]

Thus, for fixed deficit \(r=n-k\), the diameter is bounded independently of \(n\).

---

## 5. The five-vertex doubling construction

For completeness, here is a direct construction producing the lower exponential rate.

### Lemma 5.1: endpoint-gated doubling

Suppose \(G\) has independence number \(k\), and \(A,B\) are maximum independent sets at distance
\[
d_{\mathcal R_k(G)}(A,B)=d.
\]
Then there is a graph \(G'\) on \(|V(G)|+5\) vertices, with independence number \(k+2\), containing two maximum independent sets at distance exactly
\[
2d+3.
\]

#### Construction

Add vertices \(z_0,z_1,z_2,z_3,z_4\). On these five vertices, declare the only independent pairs to be
\[
P=\{z_0,z_1\},\quad
E=\{z_1,z_2\},\quad
F=\{z_2,z_3\},\quad
Q=\{z_3,z_4\}.
\]
Equivalently, the complement induced on these vertices is the path
\[
z_0z_1z_2z_3z_4.
\]

The four vertices \(z_0,z_1,z_3,z_4\) have no neighbors in \(V(G)\). The central vertex \(z_2\) is adjacent to every vertex of \(V(G)\setminus B\) and to no vertex of \(B\).

Since \(\alpha(G)=k\) and the new five-vertex graph has independence number two, \(\alpha(G')=k+2\).

Every independent \((k+2)\)-set of \(G'\) is of one of the following forms:

- \(P\cup I\), where \(I\) is a maximum independent set of \(G\);
- \(Q\cup I\), where \(I\) is a maximum independent set of \(G\);
- \(E\cup B\);
- \(F\cup B\).

Indeed, an independent pair containing \(z_2\) is compatible with a \(k\)-set of old vertices only when that old set is contained in \(B\), and hence equals \(B\).

Thus the relevant component of \(\mathcal R_{k+2}(G')\) consists of two copies of \(\mathcal R_k(G)\), joined only by
\[
P\cup B
\;-\;
E\cup B
\;-\;
F\cup B
\;-\;
Q\cup B.
\]
Consequently,
\[
d_{\mathcal R_{k+2}(G')}
  (P\cup A,Q\cup A)
=
d(A,B)+3+d(B,A)
=
2d+3.
\]
\(\square\)

Start with \(G_0=K_2\), \(k_0=1\), and its two singleton independent sets, whose distance is \(d_0=1\). Iterating Lemma 5.1 gives
\[
n_m=5m+2,\qquad
k_m=2m+1,
\]
and
\[
d_{m+1}=2d_m+3.
\]
Therefore
\[
d_m=2^{m+2}-3.
\tag{5.1}
\]

Hence
\[
M(5m+2)\ge 2^{m+2}-3.
\]
Adding vertices that are universal and pairwise adjacent does not alter the \(k_m\)-reconfiguration graph once \(k_m\ge2\). Thus, for every sufficiently large \(n\),
\[
M(n)\ge 2^{n/5-O(1)}.
\tag{5.2}
\]

This recovers the exponential rate relevant to the source result.

As another consequence, add \(m\) isolated vertices to \(G_m\). Every maximum independent set must contain them, so distances are unchanged. This gives
\[
D(6m+2,3m+1)\ge 2^{m+2}-3.
\tag{5.3}
\]
Here \(k=n/2\) and \(n-k=3m+1\), so the exponential dependence on the deficit in (4.5) cannot in general be replaced by a polynomial dependence.

---

## 6. Why the five-vertex lift is not trivially compressible

The preceding lift uses two control tokens. Its two unrestricted control states \(P,Q\) must not be adjacent; otherwise one could move directly between the two copies without visiting the gate. For \(r\) control tokens, nonadjacency requires
\[
|P\cap Q|\le r-2,
\]
so
\[
|P\cup Q|\ge r+2.
\]
If a further control vertex, absent from both \(P\) and \(Q\), is required to impose the endpoint gate, then the control gadget has at least
\[
r+3\ge5
\]
vertices, since \(r=1\) cannot give two nonadjacent singleton states.

Thus five vertices are optimal within this particular “two unrestricted copies plus a new gate vertex” architecture. This is not a global lower bound on the size of all possible recursive gadgets.

---

## 7. Final bounds and unresolved gap

The rigorous conclusion is
\[
2^{n/5-O(1)}
\le
\max_k D(n,k)
\le
3^{n/3+o(n)}.
\]

Equivalently,
\[
1.14869\ldots
\le
\liminf M(n)^{1/n}
\le
\limsup M(n)^{1/n}
\le
1.44224\ldots.
\]

The upper argument is intrinsically lossy: the extremal count \(3^{n/3}\) is attained, up to residue issues, by disjoint unions of triangles, but their reconfiguration graphs have only linear diameter. A resolution will therefore need to exploit the metric overlap structure among maximal independent sets, rather than merely count them.

No argument above proves that \(M(n)^{1/n}\) converges, nor does it match the lower and upper exponential bases. The original asymptotic question remains open.