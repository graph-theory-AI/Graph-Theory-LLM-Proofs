```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained argument gives an O_k(log(alpha(D)+1)) stable-set bound and proves the desired constant bound for complete multipartite underlying graphs.",
  "would_publish": false,
  "caveats": "Finite digraphs are assumed; the general bound still depends on the stability number, and novelty of these partial results is not claimed."
}
```

## 1. Partial results

I work with finite loopless digraphs. A vertex of \(S\) is considered to reach \(S\) by a path of length zero.

The following quantitative bound does not resolve the conjecture, but makes the dependence on the stability number logarithmic.

**Proposition 1.** Let \(D\) be a \(k\)-arc-colored digraph, where \(k\geq 1\), and put \(a=\alpha(D)\geq 1\). Define
\[
L_k=\sum_{t=1}^{k}t\,\frac{k!}{(k-t)!},
\qquad
M(k,a)=1+\left\lceil 2k\ln(2ka)\right\rceil .
\]
There is a monochromatic-path absorbing set \(S\) that is a union of at most
\[
F_k(a):=L_kM(k,a)
\]
stable sets.

In fact, each of these stable sets can be chosen so that no monochromatic path joins two distinct vertices within it. Moreover,
\[
F_k(a)=O\!\left(k^2k!\log(2ka)\right).
\]

Here “absorbing” means that every vertex has a monochromatic path to a vertex of \(S\). The empty digraph is immediate and is omitted below.

A second result removes the dependence on \(a\) for a class allowing both unbounded stability number and unbounded chromatic number.

**Proposition 2.** If the underlying graph of \(D\) is complete multipartite, the conclusion of the conjecture holds with
\[
f_{\mathrm{multipartite}}(k)=F_{k+1}(1).
\]
The arc directions and colors between different parts need not be uniform.

The proofs are self-contained. I do not claim that these partial results are new.

## 2. Monochromatic reachability relations

For each color \(i\), define the reflexive relation
\[
xR_i y
\quad\Longleftrightarrow\quad
x=y\ \text{or there is a color-\(i\) directed path from \(x\) to \(y\)}.
\]
Each \(R_i\) is transitive.

Let \(H\) be the uncolored digraph with an arc \(xy\), for distinct vertices, whenever \(xR_i y\) for some \(i\). Thus:

* a stable set of \(H\) is stable in \(D\);
* \(\alpha(H)\leq \alpha(D)=a\);
* it suffices to find \(S\) such that every \(x\) satisfies \(xR_i s\) for some \(i\) and \(s\in S\).

All stable sets used below will be stable in \(H\).

## 3. Fractional absorption by stable sets

For a digraph \(G\) and a stable set \(I\), write
\[
N_G^-[I]=I\cup\{v:\text{ some arc }vu\text{ has }u\in I\}.
\]

**Lemma 1.** For every finite digraph \(G\), there is a probability distribution \(\mu\) on its stable sets such that
\[
\Pr_{I\sim\mu}\bigl[v\in N_G^-[I]\bigr]\geq \frac12
\qquad\text{for every }v\in V(G).
\]

**Proof.** First give the vertices arbitrary nonnegative weights \(w(v)\). I claim that some stable set \(I\) satisfies
\[
w(N_G^-[I])\geq \frac12w(V(G)).
\]

Construct \(I\) greedily. In a current induced subdigraph \(G[W]\), the identity
\[
\sum_{v\in W}w(v)
\left(
w(N^-_{G[W]}(v))-w(N^+_{G[W]}(v))
\right)=0
\]
shows, provided some remaining weight is positive, that one can choose a vertex \(v\) with
\[
w(N^-_{G[W]}(v))\geq w(N^+_{G[W]}(v)).
\]
Add \(v\) to \(I\), and delete \(v\) and all its neighbors in either direction.

At least half the weight deleted at this step belongs to
\[
\{v\}\cup N^-_{G[W]}(v),
\]
and hence is absorbed by \(v\). The selected vertices are stable, and the deleted blocks are disjoint. Stopping when no positive weight remains proves the claim.

Now consider the finite zero-sum game whose choices are a vertex \(v\) and a stable set \(I\), with payoff
\[
\mathbf 1_{\{v\in N_G^-[I]\}}.
\]
The weighted claim says that against every probability distribution on vertices, some stable set obtains expected payoff at least \(1/2\). Finite minimax gives the asserted distribution on stable sets. \(\square\)

Apply this lemma to \(H[W]\), for any nonempty \(W\subseteq V(D)\). It gives a distribution \(\mu_W\) on stable subsets of \(W\) such that, for every \(v\in W\),
\[
\Pr_{I\sim\mu_W}
\bigl[\exists i,\ \exists u\in I:\ vR_i u\bigr]\geq \frac12.
\]
Set
\[
\varepsilon=\frac1{2k}.
\]
Consequently, \(W\) can be partitioned into \(W_1,\ldots,W_k\), allowing empty parts, so that
\[
\Pr_{I\sim\mu_W}
\bigl[\exists u\in I:\ vR_i u\bigr]\geq\varepsilon
\qquad(v\in W_i).
\tag{1}
\]
For each \(v\), simply choose one color attaining this bound.

## 4. A two-stage density lemma

The following is where transitivity of monochromatic reachability is used.

**Lemma 2.** Fix a transitive relation \(R\). Suppose \(\mu_A,\mu_B\) are probability distributions on stable subsets of \(A,B\), respectively, and every set in the support of \(\mu_B\) has size at most \(a\). Suppose also that
\[
\Pr_{I\sim\mu_A}[\exists u\in I:\ bRu]\geq\varepsilon
\qquad(b\in B),
\tag{2}
\]
and
\[
\Pr_{J\sim\mu_B}[\exists b\in J:\ cRb]\geq\varepsilon
\qquad(c\in C).
\tag{3}
\]
If
\[
a(1-\varepsilon)^m<\varepsilon,
\tag{4}
\]
then a union \(U\) of at most \(m\) stable sets from the support of \(\mu_A\) satisfies
\[
\forall c\in C\quad \exists u\in U:\ cRu.
\]

**Proof.** Independently sample \(I_1,\ldots,I_m\) from \(\mu_A\), and let \(U=\bigcup_j I_j\). Define
\[
B_U=\{b\in B:\exists u\in U,\ bRu\}.
\]
For each fixed \(b\in B\), condition (2) gives
\[
\Pr[b\notin B_U]\leq(1-\varepsilon)^m.
\]
A union bound, followed by averaging over \(J\sim\mu_B\), therefore yields
\[
\begin{aligned}
\mathbb E_U\,
\Pr_{J\sim\mu_B}[J\not\subseteq B_U]
&\leq
\mathbb E_{J\sim\mu_B}|J|(1-\varepsilon)^m\\
&\leq a(1-\varepsilon)^m
<\varepsilon.
\end{aligned}
\]
Fix an outcome \(U\) for which
\[
\Pr_{J\sim\mu_B}[J\not\subseteq B_U]<\varepsilon.
\]

For any \(c\in C\), condition (3) now guarantees a set \(J\) that both lies entirely in \(B_U\) and contains some \(b\) with \(cRb\). For this \(b\), some \(u\in U\) satisfies \(bRu\). Transitivity gives \(cRu\). \(\square\)

With \(\varepsilon=1/(2k)\), the choice \(m=M(k,a)\) satisfies (4), because
\[
a(1-\varepsilon)^m
\leq ae^{-\varepsilon m}
<\frac1{2k}
=\varepsilon.
\tag{5}
\]

## 5. Proof of Proposition 1

Construct a rooted partition tree. Its nodes carry subsets \(X_\sigma\subseteq V(D)\), where \(\sigma\) is a word of colors.

Start with
\[
X_{\varnothing}=V(D).
\]
Whenever \(\sigma\) has distinct entries and \(X_\sigma\neq\varnothing\), choose the distribution \(\mu_{X_\sigma}\) from Lemma 1 and partition
\[
X_\sigma=X_{\sigma 1}\,\dot\cup\,\cdots\,\dot\cup\,X_{\sigma k}
\]
using (1).

A child \(X_{\sigma i}\) is terminal if \(i\) has already appeared in \(\sigma\). Otherwise continue recursively. Empty children may be discarded.

Every branch terminates at the first repeated color, so it has length at most \(k+1\). The nonempty terminal sets partition \(V(D)\).

Consider a terminal set
\[
C=X_{c_1\cdots c_t i},
\]
where \(c_1,\ldots,c_t\) are distinct and \(i=c_j\) for some \(j\leq t\). Put
\[
A=X_{c_1\cdots c_{j-1}},
\qquad
B=X_{c_1\cdots c_t}.
\]
Since \(B\) is contained in the color-\(i\) child of \(A\), equation (1) at node \(A\) gives
\[
\Pr_{I\sim\mu_A}[\exists u\in I:\ bR_i u]\geq\varepsilon
\qquad(b\in B).
\]
Equation (1) at node \(B\) gives
\[
\Pr_{J\sim\mu_B}[\exists b\in J:\ cR_i b]\geq\varepsilon
\qquad(c\in C).
\]
Every stable set in \(H[B]\) has size at most \(a\). Lemma 2, with \(R=R_i\) and \(m=M(k,a)\), thus produces a union \(U_C\) of at most \(M(k,a)\) stable sets such that every vertex of \(C\) has a color-\(i\) path to \(U_C\).

It remains to count terminal nodes. There are at most
\[
\frac{k!}{(k-t)!}
\]
distinct-color words of length \(t\). Each has at most \(t\) children whose appended color repeats an earlier one. Hence there are at most
\[
\sum_{t=1}^{k}t\,\frac{k!}{(k-t)!}=L_k
\]
terminal nodes.

Taking
\[
S=\bigcup_{\text{terminal }C}U_C
\]
absorbs every vertex and covers \(S\) by at most \(L_kM(k,a)\) stable sets of \(H\). This proves the proposition.

Finally,
\[
L_k
\leq k\,k!\sum_{s=0}^{k-1}\frac1{s!}
<e\,k\,k!,
\]
which gives the stated asymptotic bound. The same proof actually permits replacing \(\alpha(D)\) by the potentially smaller \(\alpha(H)\). \(\square\)

## 6. Complete multipartite underlying graphs

Define
\[
T(r):=F_r(1).
\]
Proposition 1 implies that every \(r\)-colored tournament has a monochromatic absorbing set of at most \(T(r)\) vertices: its stable sets have size at most one. This is within the already-established tournament regime mentioned in the question.

Now suppose that the underlying graph of \(D\) is complete multipartite, with stable parts
\[
P_1,\ldots,P_q.
\]

Construct a tournament \(\widehat D\) on the same vertex set:

* between different parts, retain one available original arc, with its original color;
* within each part, orient every pair arbitrarily and give these new arcs a single new color \(0\).

Thus \(\widehat D\) uses at most \(k+1\) colors. Choose a monochromatic absorbing set
\[
X\subseteq V(\widehat D),
\qquad |X|\leq T(k+1).
\]
Let
\[
S=\bigcup_{\{j:P_j\cap X\neq\varnothing\}}P_j.
\]
This is a union of at most \(|X|\leq T(k+1)\) stable sets of \(D\).

For any vertex \(v\), take a monochromatic path in \(\widehat D\) from \(v\) to some \(x\in X\).

* If its color is an original color, every arc of the path belongs to \(D\), so it is an original monochromatic path to \(S\).
* If its color is \(0\), the entire path stays within one part \(P_j\). Since \(x\in P_j\cap X\), we already have \(v\in P_j\subseteq S\).
* A zero-length path likewise means \(v\in S\).

This proves Proposition 2. \(\square\)

## 7. What remains unresolved

The unrestricted conjecture requires a bound depending only on \(k\). Proposition 1 instead gives
\[
O_k\bigl(\log(\alpha(D)+1)\bigr).
\]

The precise source of this dependence is the estimate
\[
\mathbb E_{J\sim\mu_B}|J|(1-\varepsilon)^m
\leq a(1-\varepsilon)^m
\]
in Lemma 2. A sampled stable set \(J\) may contain arbitrarily many vertices, and the argument controls the probability that **every** vertex of \(J\) is absorbed. Nothing above replaces this size-dependent estimate by a bound depending only on \(k\).

Nor can one simply apply the result again inside \(S\): concatenating an original monochromatic path to \(S\) with a differently colored path inside \(S\) need not produce a monochromatic path.

Thus the argument establishes the quantitative bound and the complete-multipartite special case, but supplies neither a proof nor a counterexample for arbitrary finite digraphs.