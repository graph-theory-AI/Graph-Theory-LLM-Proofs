```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "Bipartite graphs of maximum degree at most 20 form a subgraph-closed class with linear separator lower bounds and exponential expansion, while Maximum Independent Set is exactly polynomial-time solvable.",
  "would_publish": false,
  "caveats": "Non-APX-hardness is meant under the standard assumption P != NP; an omitted closure or richness hypothesis in the intended question could evade this counterexample."
}
```

# Counterexample to the stated problem

We use the standard definition that a balanced separator \(X\) in an \(n\)-vertex graph satisfies that every component of \(G-X\) has at most \(2n/3\) vertices. A class has sublinear separators if every \(n\)-vertex member has such a separator of size \(o(n)\), uniformly over the class.

Consider the class

\[
\mathcal C=\{G: G\text{ is bipartite and }\Delta(G)\le 20\}.
\]

We prove:

1. \(\mathcal C\) is subgraph-closed.
2. Maximum Independent Set is solvable exactly in polynomial time on \(\mathcal C\).
3. \(\mathcal C\) does not have sublinear separators; in fact, it contains infinitely many \(N\)-vertex graphs whose smallest balanced separator has size greater than \(N/12\).
4. Under the usual shallow-minor definition, \(\mathcal C\) has genuinely exponential expansion.

Thus \(\mathcal C\) contradicts both versions of the proposed hardness principle.

## 1. Subgraph closure

Every subgraph of a bipartite graph is bipartite, and taking a subgraph cannot increase maximum degree. Hence \(\mathcal C\) is subgraph-closed. It is also efficiently recognizable.

## 2. Maximum Independent Set is polynomial-time solvable

For every graph \(G\),

\[
\alpha(G)=|V(G)|-\tau(G),
\]

where \(\tau(G)\) is the minimum vertex-cover size: complements interchange independent sets and vertex covers.

For bipartite graphs, König's theorem gives

\[
\tau(G)=\nu(G),
\]

where \(\nu(G)\) is the maximum matching size. A maximum matching and a corresponding minimum vertex cover can be found in polynomial time. Consequently, a maximum independent set is obtained as the complement of that minimum vertex cover.

Thus Maximum Independent Set is in \(P\) on \(\mathcal C\), indeed even without the degree bound.

Under the standard assumption \(P\ne NP\), it therefore cannot be APX-hard under the usual approximation-preserving reductions. In particular, under an L-reduction, an exact optimum for the target problem would map back to an exact optimum for the source problem.

## 3. Linear separator lower bound

We give a self-contained probabilistic construction of bounded-degree bipartite graphs with no small balanced separator.

### Lemma

For every positive integer \(m\), there exists a bipartite graph \(G_m\) with bipartition \(L\cup R\), where

\[
|L|=|R|=m,
\]

maximum degree at most \(20\), and no partition

\[
V(G_m)=A\mathbin{\dot\cup}B\mathbin{\dot\cup}X
\]

such that

\[
\frac{2m}{3}\le |A|\le \frac{4m}{3},\qquad
|X|\le \frac m6,
\]

and there is no edge between \(A\) and \(B\).

### Proof

Choose \(d=20\) independent uniformly random bijections

\[
\pi_i:L\longrightarrow R,\qquad i=1,\dots,d,
\]

and let \(G\) be the simple graph whose edges are all pairs \(x\pi_i(x)\), with repeated edges suppressed. Then \(G\) is bipartite and has maximum degree at most \(d\).

Fix a partition \(V=A\dot\cup B\dot\cup X\) satisfying the displayed size conditions. Set

\[
u=\frac{|A\cap L|}{m},\qquad
v=\frac{|A\cap R|}{m},
\]

and

\[
z_L=\frac{|X\cap L|}{m},\qquad
z_R=\frac{|X\cap R|}{m}.
\]

Then

\[
\frac23\le u+v\le\frac43,\qquad z_L+z_R\le\frac16.
\]

The two types of possible \(A\)-\(B\) edges have total normalized rectangle size

\[
\begin{aligned}
F
&=\frac{|A\cap L||B\cap R|+|B\cap L||A\cap R|}{m^2}\\
&=u(1-v-z_R)+v(1-u-z_L)\\
&=(u+v)-2uv-u z_R-v z_L.
\end{aligned}
\]

Writing \(s=u+v\), we have \(uv\le s^2/4\) and

\[
u z_R+v z_L\le z_L+z_R\le\frac16.
\]

Therefore

\[
F\ge s-\frac{s^2}{2}-\frac16.
\]

For \(2/3\le s\le4/3\),

\[
s-\frac{s^2}{2}\ge\frac49,
\]

so

\[
F\ge \frac49-\frac16=\frac5{18}.
\]

Consequently, at least one of the two products

\[
|A\cap L||B\cap R|,
\qquad
|B\cap L||A\cap R|
\]

is at least \(5m^2/36\).

For subsets \(P\subseteq L\), \(Q\subseteq R\) with \(|P|=p\), \(|Q|=q\), a uniformly random bijection \(\pi:L\to R\) satisfies

\[
\Pr(\pi(P)\cap Q=\varnothing)
=
\frac{\binom{m-q}{p}}{\binom mp}
\le
\left(1-\frac qm\right)^p
\le e^{-pq/m},
\]

with probability zero if \(p>m-q\). It follows that one random matching has no \(A\)-\(B\) edge with probability at most

\[
e^{-5m/36}.
\]

For all \(d=20\) independent matchings, this probability is at most

\[
e^{-100m/36}.
\]

There are at most \(3^{2m}\) ordered partitions of the \(2m\) vertices into \(A,B,X\). Hence, by the union bound, the probability that some forbidden partition exists is at most

\[
3^{2m}e^{-100m/36}
=
\exp\left(m\left(2\log 3-\frac{100}{36}\right)\right)<1.
\]

Thus some choice of the twenty matchings has no forbidden partition. ∎

### Consequence for separators

Let \(N=2m\), and suppose \(X\) were a balanced separator in \(G_m\) with

\[
|X|\le \frac{N}{12}=\frac m6.
\]

The components of \(G_m-X\) all have size at most \(2N/3\). We can choose a union \(A\) of components satisfying

\[
\frac N3\le |A|\le\frac{2N}{3}.
\]

Indeed, if some component has size in this interval, use it; otherwise, greedily combine components of size less than \(N/3\) until their union first reaches \(N/3\).

Let

\[
B=V(G_m)\setminus(A\cup X).
\]

Then there are no edges between \(A\) and \(B\), and

\[
|B|
\ge N-\frac{2N}{3}-\frac{N}{12}
=\frac N4.
\]

This is precisely a partition excluded by the lemma. Therefore every balanced separator has size greater than \(N/12\).

Since such graphs exist for arbitrarily large \(N\), \(\mathcal C\) has neither sublinear nor strongly sublinear separators.

### Even simpler unbounded-degree example

If bounded degree was not intended, the class of all bipartite graphs already suffices. The graph \(K_{m,m}\) has \(N=2m\) vertices. If a separator leaves vertices on both sides, the remaining graph is connected, so balancing requires at least \(N/3\) deleted vertices; deleting an entire shore costs \(N/2\). Yet Maximum Independent Set remains polynomial-time solvable.

## 4. Exponential expansion

Let

\[
\nabla_r(\mathcal C)
=
\sup\left\{\frac{|E(H)|}{|V(H)|}:
H\text{ is an }r\text{-shallow minor of some }G\in\mathcal C
\right\}.
\]

We show

\[
2^{r-1}\le \nabla_r(\mathcal C)\le O(19^r).
\]

Thus the expansion is exponential both from above and below.

### Upper bound

In a graph of maximum degree \(D=20\), every radius-\(r\) connected subgraph has at most

\[
1+D\sum_{j=0}^{r-1}(D-1)^j=O(19^r)
\]

vertices. A branch set of an \(r\)-shallow minor therefore has \(O(19^r)\) vertices and at most \(O(19^r)\) incident edges. Hence every \(r\)-shallow minor has maximum degree, and therefore density, \(O(19^r)\).

### Lower bound

Fix \(r\ge1\) and put \(q=2^r\). Start with \(H=K_{q,q}\). For each vertex \(v\in V(H)\), take a rooted full binary tree \(T_v\) of depth \(r\), with exactly \(q\) leaves. Assign the \(q\) edges incident with \(v\) bijectively to the leaves of \(T_v\), and for each edge \(vw\in E(H)\), join its two assigned leaves.

The resulting graph \(G_r\) has maximum degree at most \(3\). It is bipartite: color roots corresponding to the two shores of \(H\) oppositely and extend the coloring down each tree. Since all leaves have the same depth, every added leaf-to-leaf edge joins opposite colors.

The trees \(T_v\) are disjoint connected branch sets of radius \(r\). Contracting each \(T_v\) recovers \(K_{q,q}\). Therefore \(K_{q,q}\) is an \(r\)-shallow minor of a member of \(\mathcal C\), and

\[
\nabla_r(\mathcal C)
\ge
\frac{|E(K_{q,q})|}{|V(K_{q,q})|}
=
\frac{q^2}{2q}
=
2^{r-1}.
\]

Hence \(\mathcal C\) also satisfies the proposed “exponential expansion” alternative.

# Conclusion and remaining caveat

The stated universal principle is false: separator complexity or exponential shallow-minor expansion does not by itself force hardness of Maximum Independent Set. Bipartiteness is preserved under taking subgraphs and makes Maximum Independent Set exactly solvable, while still allowing bounded-degree expanders and exponential shallow-minor expansion.

The only logical caveat is the standard one for complexity-theoretic counterexamples: a problem in \(P\) could formally also be APX-hard if \(P=NP\). Under the intended \(P\ne NP\) interpretation, however, this is a decisive counterexample. If the source intended an additional hypothesis—such as suitable closure under contractions, topological minors, or operations that prevent restriction to bipartite graphs—that strengthened question is not settled here.