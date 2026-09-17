```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sharp digon-matching bound proves the conjecture for k≥4 when n=2k+s, s≤k+2, and s(s+1)<28(k−2), using the established k=3 case.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; novelty of this elementary order-restricted consequence has not been checked."
}
```

## 1. Results obtained

All digraphs below are finite, loopless, and have no parallel arcs. Cycles are directed and vertex-disjoint. A **digon** is a directed cycle of length two.

The main positive result of this attack is the following order-restricted case.

**Theorem 1.** Let \(k\ge 4\), and let \(D\) have
\[
|V(D)|=2k+s,\qquad \delta^+(D)\ge 2k-1,
\]
where \(s\ge0\) is an integer. If
\[
\boxed{\quad s\le k+2,\qquad s(s+1)<28(k-2),\quad}
\]
then \(D\) contains \(k\) vertex-disjoint directed cycles.

This uses the established \(k=3\) case stated in the question. Without using that result, the same method proves:

**Theorem 2.** For \(k\ge2\), the conclusion holds under the conditions
\[
\boxed{\quad s\le k,\qquad s(s+1)<12(k-1).\quad}
\]

The mechanism is to force sufficiently many disjoint digons, delete them, and apply the \(k=3\) or \(k=1\) case to the remainder. I give an exact extremal calculation for this mechanism.

I also give an explicit high-girth sharpness family. In particular, it supplies a 49-vertex negative answer to the auxiliary question about minimum outdegree six and four cycles. It is **not** a counterexample to Bermond–Thomassen.

## 2. A sharp bound for packing digons

For a digraph \(D\), define its **digon graph** \(G\): it has vertex set \(V(D)\), with
\[
uv\in E(G)\quad\Longleftrightarrow\quad uv,vu\in A(D).
\]
Matchings in \(G\) are precisely collections of vertex-disjoint digons in \(D\).

### Proposition 3

Let \(r\ge0\) and \(n\ge2r+2\). Put
\[
A(n,r)=\frac{(n-2r-1)(n+2r)}{2n},
\qquad
B(n,r)=\frac{n-r-1}{2}.
\]
Among all \(n\)-vertex digraphs having no \(r+1\) vertex-disjoint digons, the largest possible minimum outdegree is
\[
\boxed{
n-1-\left\lceil\min\{A(n,r),B(n,r)\}\right\rceil.
}
\tag{1}
\]

Consequently, if
\[
\delta^+(D)\ge n-1-s
\quad\text{and}\quad
s<\min\{A(n,r),B(n,r)\},
\tag{2}
\]
then \(D\) has \(r+1\) vertex-disjoint digons.

### Proof of the upper bound

Suppose that the digon graph \(G\) has matching number at most \(r\), and that every vertex of \(D\) is missing at most \(s\) outgoing arcs.

By the Tutte–Berge formula, there is a set \(S\subseteq V(G)\) such that, writing
\[
a=|S|,\qquad m=n-a,\qquad q=o(G-S),
\]
we have
\[
q\ge n-2r+a.
\tag{3}
\]
Here \(o(G-S)\) denotes the number of odd components of \(G-S\). Since \(q\le n-a\), equation (3) implies \(0\le a\le r\).

Every pair of vertices in different components of \(G-S\) is a nonedge of \(G\), so at least one of the two corresponding directed arcs is missing from \(D\).

The number of pairs in different components is at least
\[
(q-1)\left(m-\frac q2\right).
\tag{4}
\]
Indeed, merge any even components into one of the odd components. Among partitions of \(m\) vertices into \(q\) nonempty groups, the number of cross-pairs is minimized when \(q-1\) groups are singletons and the remaining group has size \(m-q+1\).

On the other hand, at most \(sm\) directed arcs with both endpoints in \(V(D)\setminus S\) are missing. Thus
\[
(q-1)\left(m-\frac q2\right)\le sm.
\tag{5}
\]
The expression on the left is increasing in the integer \(q\) for \(1\le q\le m\). Substituting the lower bound from (3) therefore yields
\[
\frac{(n-2r+a-1)(n+2r-3a)}2\le s(n-a).
\tag{6}
\]

Define
\[
F(a)=\frac{(n-2r+a-1)(n+2r-3a)}2-s(n-a).
\]
This is a concave quadratic in \(a\), with coefficient \(-3/2\) on \(a^2\). Its endpoint values are
\[
F(0)=n\bigl(A(n,r)-s\bigr),
\]
and
\[
F(r)=(n-r)\bigl(B(n,r)-s\bigr).
\]
If \(s<\min\{A(n,r),B(n,r)\}\), both endpoint values are positive. Concavity gives \(F(a)>0\) throughout \(0\le a\le r\), contradicting (6). This also covers \(r=0\), when the interval consists of one point.

Taking \(s=n-1-\delta^+(D)\), which is an integer, proves the upper bound in (1).

### Sharpness

I include the constructions because they identify exactly where the digon method stops.

We use the following elementary orientation fact:

> An undirected graph \(H\) has an orientation with maximum outdegree at most an integer \(p\ge0\) if and only if
> \[
> e(H[W])\le p|W|
> \quad\text{for every }W\subseteq V(H).
> \tag{7}
> \]

For sufficiency, assign each edge to one of its endpoints, with capacity \(p\) at each vertex, and orient the edge away from its assigned endpoint. Hall’s theorem gives such an assignment: any set \(F\) of edges satisfies
\[
|F|\le e(H[V(F)])\le p|V(F)|.
\]
Necessity follows by counting tails of edges inside \(W\).

Now choose an undirected graph \(G\), let \(H=\overline G\), and orient \(H\). Construct \(D\) by:

* putting both arcs on every edge of \(G\);
* for every oriented edge \(u\to v\) of \(H\), putting \(v\to u\), but not \(u\to v\), in \(D\).

Then \(G\) is exactly the digon graph of \(D\), and
\[
d_D^+(v)=n-1-d_{\vec H}^+(v).
\tag{8}
\]

There are two extremal choices.

**First construction.** Let \(G\) consist of \(K_{2r+1}\) and \(n-2r-1\) isolated vertices. Its matching number is \(r\).

Its complement \(H\) has a clique of size \(n-2r-1\), an independent set of size \(2r+1\), and all edges between them. Its maximum induced-subgraph density is
\[
\max_{\varnothing\ne W\subseteq V(H)}
\frac{e(H[W])}{|W|}=A(n,r).
\]
To check this, a subset containing \(t\) clique vertices and \(b\) independent vertices has density
\[
\frac{\binom t2+tb}{t+b},
\]
which is nondecreasing when either \(t\) or \(b\) increases. Thus (7) supplies an orientation with maximum outdegree at most \(\lceil A(n,r)\rceil\).

**Second construction.** Let
\[
G=K_r\vee \overline K_{n-r}.
\]
Its matching number is \(r\), since its \(K_r\) is a vertex cover and can be matched into the independent set.

Here \(H\) consists of \(K_{n-r}\) and \(r\) isolated vertices. Its maximum induced-subgraph density is \(B(n,r)\), so it has an orientation with maximum outdegree at most \(\lceil B(n,r)\rceil\).

Using whichever construction has the smaller density, equation (8) gives minimum outdegree at least the value in (1). Together with the upper bound, this proves the exact formula. \(\square\)

## 3. Deducing the order-restricted cases

Let
\[
n=2k+s,\qquad \delta^+(D)\ge2k-1=n-1-s.
\]

Take \(b\in\{1,3\}\), with \(k\ge b+1\), and set
\[
r=k-b-1.
\]
Proposition 3 forces \(k-b\) disjoint digons whenever
\[
s<A(n,r),\qquad s<B(n,r).
\]

The two inequalities simplify as follows:
\[
A(n,r)-s
=
\frac{2(2b+1)(2k-b-1)-s(s+1)}{2n},
\tag{9}
\]
and
\[
B(n,r)-s=\frac{k+b-s}{2}.
\tag{10}
\]
Thus it suffices that
\[
s\le k+b-1,
\qquad
s(s+1)<2(2b+1)(2k-b-1).
\tag{11}
\]

Delete the vertices of the resulting \(k-b\) digons. In the remaining induced digraph \(D'\),
\[
\delta^+(D')
\ge (2k-1)-2(k-b)
=2b-1.
\tag{12}
\]

* For \(b=1\), every finite digraph of positive minimum outdegree contains a directed cycle: follow outgoing arcs until a vertex repeats. This supplies the last cycle. Conditions (11) become
  \[
  s\le k,\qquad s(s+1)<12(k-1),
  \]
  proving Theorem 2.

* For \(b=3\), apply the established three-cycle theorem stated in the question to \(D'\), whose minimum outdegree is at least five. Conditions (11) become
  \[
  s\le k+2,\qquad s(s+1)<28(k-2),
  \]
  proving Theorem 1.

All cycles in \(D'\) avoid the previously deleted digons, so the resulting packing has exactly the required \(k\) members. \(\square\)

The sharper window allows an order surplus \(s\) of approximately \(\sqrt{28k}\). This is an order-restricted result, not an improvement to the general minimum-outdegree bound.

## 4. Explicit sharpness examples of arbitrarily large directed girth

The discussion’s girth strengthening cannot circumvent the obstruction at outdegree \(2k-2\). Here is a self-contained construction.

Fix \(k\ge2\) and \(L\ge2\), and put
\[
q=2k-1,\qquad d=2k-2.
\]
Take \(q\) distinguished vertices
\[
X=\{x_1,\ldots,x_q\}.
\]
For every \(i\), introduce \(L-1\) disjoint sets
\[
Y_{i,1},\ldots,Y_{i,L-1},
\]
each of size \(d\). Put in precisely these arcs:

1. \(x_i\to y\) for every \(y\in Y_{i,1}\);
2. all arcs from \(Y_{i,j}\) to \(Y_{i,j+1}\), for \(1\le j<L-1\);
3. \(y\to x_h\) for every \(y\in Y_{i,L-1}\) and every \(h\ne i\).

Call the resulting digraph \(D_{k,L}\).

### Degree and girth

Every vertex has outdegree exactly \(d=2k-2\).

Every directed cycle visits \(X\). Between consecutive visits to \(X\), it traverses exactly \(L\) arcs. A traversal beginning at \(x_i\) cannot return immediately to \(x_i\), so every cycle visits at least two vertices of \(X\). Conversely, any two distinct distinguished vertices support a cycle of length \(2L\). Therefore
\[
g(D_{k,L})=2L.
\tag{13}
\]

### Exact cycle-packing number

Every cycle consumes at least two vertices of the set \(X\), which has size \(2k-1\). Hence
\[
\nu_{\mathrm{cyc}}(D_{k,L})\le k-1.
\]
Pairing \(2k-2\) of the distinguished vertices and taking one \(2L\)-cycle for each pair attains this bound. Thus
\[
\boxed{
\delta^+(D_{k,L})=2k-2,\quad
g(D_{k,L})=2L,\quad
\nu_{\mathrm{cyc}}(D_{k,L})=k-1.
}
\tag{14}
\]

In particular, the necessary outdegree threshold cannot be lowered below \(2k-1\), even under an arbitrarily large prescribed lower bound on directed girth.

### The auxiliary four-cycle question

Take \(k=4\) and \(L=2\). There are seven distinguished vertices and six additional vertices for each distinguished vertex, for a total of
\[
7(1+6)=49
\]
vertices. Explicitly, its arcs are
\[
x_i\to y_{i,j},
\qquad
y_{i,j}\to x_h\quad(h\ne i),
\]
where \(1\le i,h\le7\) and \(1\le j\le6\).

This is an oriented bipartite digraph with minimum outdegree six and directed girth four. Every cycle uses at least two of the seven distinguished vertices, so it has no four vertex-disjoint cycles.

This answers the auxiliary question negatively. The supplied catalog already reports failure of the stronger girth conjecture; I make no novelty claim for this construction.

## 5. What remains unresolved

The exact calculation in Proposition 3 concerns **digons**, not arbitrary directed cycles. Outside the stated order windows, sufficiently many digons need not exist. In particular, oriented digraphs have no digons at all, so this mechanism does not address the central unrestricted difficulty.

The high-girth examples have minimum outdegree \(2k-2\), one below the conjectured threshold. They establish necessity, not a counterexample at \(2k-1\).

Thus the Bermond–Thomassen conjecture itself remains unresolved by this attack. The proved progress here is the order-restricted positive result and the exact auxiliary extremal calculation; their novelty has not been established.