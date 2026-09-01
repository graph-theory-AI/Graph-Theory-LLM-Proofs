```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Clebsch-based lexicographic powers give explicit P6-free graphs with eta at least omega squared over three, and eta equal to omega squared when omega is a power of two.",
  "would_publish": false,
  "caveats": "This is only a lower bound for the P6 case; it gives neither an upper bound nor a fixed-clique counterexample, and its literature novelty was not checked."
}
```

# Mathematical writeup

## 1. Partial result

Let
\[
M_6(r)=\sup\{\eta(G):G\text{ is }P_6\text{-free and }\omega(G)=r\}.
\]

I prove the following.

**Theorem.** For every positive integer \(r\), there is an explicitly constructed \(P_6\)-free graph \(J_r\) such that
\[
\omega(J_r)=r
\qquad\text{and}\qquad
\eta(J_r)\ge \frac{r^2}{3}.
\]
If \(r\) is a power of two, the construction satisfies
\[
\eta(J_r)=r^2.
\]

Consequently, any function \(f\) witnessing the conjecture for \(H=P_6\) must satisfy
\[
f(r)\ge \frac{r^2}{3}
\]
for every \(r\), and \(f(2^d)\ge 4^d\). In particular, no subquadratic polynomial can \(\eta\)-bound the class of \(P_6\)-free graphs.

This does not settle existence of \(f\).

## 2. Preliminary observations

A set \(X\subseteq V(G)\) hits every maximum stable set if and only if
\[
\alpha(G-X)<\alpha(G).
\]
Thus
\[
\eta(G)=\min\{|X|:\alpha(G-X)<\alpha(G)\}.
\]

As a useful baseline, perfect graphs satisfy a sharp elementary bound.

**Lemma 2.1.** If \(G\) is perfect, then
\[
\eta(G)\leq \omega(G).
\]

**Proof.** Since \(\overline G\) is perfect,
\[
\chi(\overline G)=\omega(\overline G)=\alpha(G).
\]
Thus \(V(G)\) can be partitioned into \(\alpha(G)\) cliques
\[
Q_1,\dots,Q_{\alpha(G)}
\]
of \(G\). Every stable set contains at most one vertex from each \(Q_i\), so every stable set of size \(\alpha(G)\) contains exactly one vertex from every \(Q_i\). Hence each \(Q_i\) hits all maximum stable sets, and \(|Q_i|\leq\omega(G)\). ∎

The lower-bound construction below therefore necessarily uses nonperfect graphs.

## 3. A \(P_6\)-free base graph with \(\omega=2\) and \(\eta=4\)

Define a graph \(C\) on the sixteen even-cardinality subsets of \([5]=\{1,\dots,5\}\). Two vertices \(A,B\) are adjacent when
\[
|A\triangle B|=4.
\]
This is the usual sixteen-vertex Clebsch graph, but the definition above is all that is needed.

For \(i\in[5]\), write
\[
Q_i=[5]\setminus\{i\}.
\]

### Lemma 3.1
The graph \(C\) is triangle-free and \(P_6\)-free.

**Proof.**

For triangle-freeness, symmetric difference by any even set is an automorphism. If a triangle existed, translate one of its vertices to \(\varnothing\). Its other two vertices would then be distinct four-subsets \(Q_i,Q_j\). But
\[
|Q_i\triangle Q_j|=2,
\]
so they are nonadjacent, a contradiction.

Suppose now that \(p_1,\dots,p_6\) induce a \(P_6\). Using translations and coordinate permutations, we may normalize successively:
\[
p_1=\varnothing,\qquad p_2=Q_5,\qquad p_3=\{1,5\}.
\]
Indeed,
\[
N(Q_5)=\{\varnothing,15,25,35,45\}.
\]

Now
\[
N(15)=\{Q_1,Q_5,23,24,34\}.
\]
Since \(p_4\) is nonadjacent to \(p_1\), it is one of \(23,24,34\). Permuting \(2,3,4\), take \(p_4=23\).

Next,
\[
N(23)=\{Q_2,Q_3,14,15,45\}.
\]
Nonadjacency to \(p_1=\varnothing\) excludes \(Q_2,Q_3\); distinctness excludes \(15\); and nonadjacency to \(p_2=Q_5\) excludes \(45\). Hence
\[
p_5=14.
\]
Finally,
\[
N(14)=\{Q_1,Q_4,23,25,35\}.
\]
Nonadjacency to \(p_1\) excludes \(Q_1,Q_4\), and distinctness excludes \(23\). But both \(25\) and \(35\) are adjacent to \(Q_5=p_2\), contradicting the required nonadjacency of \(p_6\) and \(p_2\). Thus \(C\) is \(P_6\)-free. ∎

### Lemma 3.2
The Clebsch graph satisfies
\[
\alpha(C)=5,\qquad \omega(C)=2,\qquad \eta(C)=4.
\]

**Proof.**

We already know \(C\) is triangle-free and has edges, so \(\omega(C)=2\).

Let \(S\) be a stable set and translate one of its vertices to \(\varnothing\). Every other member of \(S\) must then be a two-subset of \([5]\): four-subsets are adjacent to \(\varnothing\). Two distinct two-subsets are nonadjacent precisely when they intersect. Thus the nonzero members of \(S\) form a pairwise-intersecting family of two-subsets.

Such a family has size at most four. Indeed, either all its members contain a common point, giving at most four sets, or it contains a triangle
\[
12,\ 13,\ 23,
\]
in which case no fourth two-subset can meet all three. Therefore \(\alpha(C)\leq5\). Equality is attained by
\[
\{\varnothing\}\cup\{\{i,j\}:j\neq i\}.
\]

Moreover, equality in the pairwise-intersecting bound forces the four two-subsets to form a full star. Consequently every maximum stable set is an open neighborhood:
\[
N(Q_i)=\{\varnothing\}\cup\{\{i,j\}:j\neq i\},
\]
up to translation. Hence the maximum stable sets of \(C\) are exactly the sets \(N(v)\), \(v\in V(C)\).

It follows that a set \(X\) hits all maximum stable sets exactly when
\[
\bigcup_{x\in X}N(x)=V(C),
\]
that is, when \(X\) is a total dominating set. Since \(C\) is 5-regular, three open neighborhoods cover at most fifteen of the sixteen vertices. Therefore
\[
\eta(C)\geq4.
\]

For the reverse inequality, take
\[
X=\{\varnothing,Q_5,Q_1,15\}.
\]
Here:

- \(N(\varnothing)\) contains all five \(Q_i\);
- \(N(Q_5)\) contains \(\varnothing\) and \(15,25,35,45\);
- \(N(Q_1)\) contains \(\varnothing\) and \(12,13,14,15\);
- \(N(15)\) contains \(Q_1,Q_5,23,24,34\).

These neighborhoods cover all sixteen vertices. Hence \(\eta(C)\leq4\), proving equality. ∎

Thus \(C\) is already a \(P_6\)-free example with
\[
\eta(C)=4=2^2=\omega(C)^2.
\]

## 4. Lexicographic products multiply \(\eta\)

For graphs \(F,G\), let \(F[G]\) denote the lexicographic product: each vertex \(v\in V(F)\) is replaced by a copy \(G_v\) of \(G\), and \(G_u\) is complete to \(G_v\) exactly when \(uv\in E(F)\).

### Lemma 4.1
For nonempty graphs \(F,G\),
\[
\alpha(F[G])=\alpha(F)\alpha(G),\qquad
\omega(F[G])=\omega(F)\omega(G),
\]
and
\[
\eta(F[G])=\eta(F)\eta(G).
\]

**Proof.**

The first two identities are standard and follow by projecting a stable set or clique onto the corresponding vertices of \(F\).

For the \(\eta\)-identity, let \(X\subseteq V(F[G])\), and write
\[
X_v=X\cap V(G_v).
\]
Define
\[
T_X=\{v\in V(F): X_v\text{ hits all maximum stable sets of }G_v\}.
\]

Every maximum stable set of \(F[G]\) is obtained by choosing a maximum stable set \(S\) of \(F\), and then choosing independently a maximum stable set of \(G_v\) in each module \(v\in S\).

Therefore \(X\) hits all maximum stable sets of \(F[G]\) if and only if \(T_X\) hits all maximum stable sets of \(F\). Indeed, if some maximum stable set \(S\) of \(F\) avoids \(T_X\), then for every \(v\in S\) one can choose a maximum stable set of \(G_v\) avoiding \(X_v\); their union is a maximum stable set of \(F[G]\) avoiding \(X\).

Consequently, for every hitting set \(X\),
\[
|X|\geq \eta(G)|T_X|\geq \eta(G)\eta(F).
\]
Conversely, take a minimum hitter \(T\) in \(F\) and, for each \(v\in T\), a minimum hitter inside \(G_v\). Their union has size \(\eta(F)\eta(G)\) and hits every maximum stable set of \(F[G]\). ∎

### Lemma 4.2
If \(F\) and all substituted graphs \(G_v\) are \(P_6\)-free, then their substitution is \(P_6\)-free.

**Proof.**

The path \(P_6\) has no proper non-singleton module. To see this, if \(M\) were such a module, connectedness gives an edge \(xy\) with \(x\in M\), \(y\notin M\). Since \(y\) has a neighbor in \(M\), it must be complete to \(M\), so \(|M|\leq2\). If \(|M|=2\), its two vertices must be the two path-neighbors of \(y\), and the next path vertex distinguishes them, again contradicting modularity.

Now consider an induced \(P_6\) in a substitution. Its intersection with each substituted module is a module of that induced path. Hence either the entire path lies in one substituted graph, or it uses at most one vertex from each module and projects to an induced \(P_6\) in \(F\). Both alternatives are excluded. ∎

## 5. Quadratic lower bound

Let
\[
G_0=K_1,\qquad G_{d+1}=C[G_d].
\]
By the preceding lemmas,
\[
\omega(G_d)=2^d,\qquad
\alpha(G_d)=5^d,\qquad
\eta(G_d)=4^d,
\]
and every \(G_d\) is \(P_6\)-free. In particular,
\[
\eta(G_d)=\omega(G_d)^2.
\]

This proves the assertion for clique numbers that are powers of two. To obtain every clique number, let
\[
r=\sum_{d\in D}2^d
\]
be the binary expansion of \(r\), and put \(m=\max D\).

For each \(d\in D\), replace every vertex of \(G_d\) by an independent set of size \(5^{m-d}\). Equivalently, define
\[
H_d=G_d[E_{5^{m-d}}],
\]
where \(E_q\) is the edgeless graph on \(q\) vertices. Since
\[
\omega(E_q)=1,\qquad \alpha(E_q)=q,\qquad \eta(E_q)=1,
\]
we have
\[
\omega(H_d)=2^d,\qquad
\alpha(H_d)=5^m,\qquad
\eta(H_d)=4^d.
\]
All \(H_d\) remain \(P_6\)-free.

Finally, let \(J_r\) be the join of all the graphs \(H_d\), \(d\in D\). Since all cross-edges are present,
\[
\omega(J_r)=\sum_{d\in D}2^d=r.
\]
A stable set lies inside a single join factor. Since all factors have the same independence number \(5^m\), the maximum stable sets of \(J_r\) are precisely the maximum stable sets of the individual factors. Therefore a hitter must hit the maximum stable sets in every factor, and
\[
\eta(J_r)=\sum_{d\in D}4^d.
\]
The join is also \(P_6\)-free by Lemma 4.2, viewing it as a substitution into a complete graph.

It remains to compare the final sum with \(r^2\). For distinct powers of two \(a_i\),
\[
\left(\sum_i a_i\right)^2\leq 3\sum_i a_i^2.
\]
This follows by induction: if \(a\) is the largest power and \(T\) is the sum of the remaining powers, then \(T<a\), and
\[
(a+T)^2
 =a^2+2aT+T^2
 \leq 3a^2+3\sum_{\text{tail}}a_i^2.
\]
Applying this with \(a_i=2^d\) gives
\[
r^2\leq 3\sum_{d\in D}4^d=3\eta(J_r).
\]
Thus
\[
\eta(J_r)\geq \frac{r^2}{3}.
\]

## 6. What remains open

This construction does not disprove the conjecture:

1. The clique number grows with \(\eta\). A counterexample would require a fixed \(r\) and \(P_6\)-free graphs of clique number \(r\) with unbounded \(\eta\).
2. No upper bound for \(P_6\)-free graphs is obtained.
3. The argument only treats a lower-bound aspect of the first open path case \(H=P_6\), not arbitrary forests.
4. I have not verified whether this particular Clebsch-product lower bound already appears in the literature.

The rigorous conclusion is that the \(P_6\) case, if true, is quantitatively at least quadratic in the clique number.