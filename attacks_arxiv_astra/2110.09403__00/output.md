```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The bound holds for clique-gluings of graphs with independence number at most two, with the stronger bound 2t-3, but the unrestricted problem is not resolved.",
  "would_publish": false,
  "caveats": "Self-contained special cases only; no novelty claim or improvement of the unrestricted upper bound."
}
```

## A structural special case

Write \(h(G)\) for the largest integer \(r\) such that \(G\) contains a \(K_r\)-minor. All graphs below are finite and simple.

A **clique-gluing construction** starts with a graph \(F_1\) and successively attaches graphs \(F_2,\ldots,F_m\). At each step, a clique of the new graph is identified with a clique of the graph already constructed; all other vertices are new, and no other edges are added. The identified clique may be empty. Edges of the identified clique are retained.

I prove the following.

**Theorem.** Let \(G\) be a nonempty graph admitting a clique-gluing construction in which every piece \(F_i\) satisfies \(\alpha(F_i)\le 2\). Then
\[
\chi_\ell(G)\le 2h(G)-1.
\]
Consequently, every \(K_t\)-minor-free graph in this class is \((2t-3)\)-choosable, for \(t\ge2\).

The class permits unbounded order and unbounded independence number: the restriction concerns the pieces, not the assembled graph. The proof uses a precoloring-extension statement, rather than assuming that choosability is preserved under clique-gluing.

Two additional consequences are:

* If \(\alpha(G)\le2\), then
  \[
  \chi_\ell(G)\le \left\lfloor\frac{3h(G)}2\right\rfloor.
  \]
* Every \(K_t\)-minor-free graph with at most \(3t+2\) vertices is \(2t\)-choosable.

No novelty is claimed for these special-case bounds.

## 1. An elementary list-coloring bound

**Lemma 1.** Every graph \(F\), with \(n=|V(F)|\) and \(\omega=\omega(F)\), satisfies
\[
\chi_\ell(F)\le \left\lfloor\frac{n+\omega}{2}\right\rfloor.
\tag{1}
\]

**Proof.** Induct on \(n\), the empty graph being immediate. Put
\[
k=\left\lfloor\frac{n+\omega}{2}\right\rfloor,
\]
and give every vertex a list of \(k\) colors.

Suppose first that two nonadjacent vertices \(u,v\) have a common available color \(c\). Color both with \(c\), delete them, and remove \(c\) from every remaining list. The remaining lists have size at least \(k-1\), while
\[
\left\lfloor
\frac{n-2+\omega(F-\{u,v\})}{2}
\right\rfloor
\le k-1.
\]
The induction hypothesis completes the coloring.

Otherwise, for each color \(c\), the vertices whose lists contain \(c\) form a clique. Thus each color occurs in at most \(\omega\) lists. For any vertex set \(X\),
\[
k|X|
\le
\omega\left|\bigcup_{v\in X}L(v)\right|.
\]
Since \(k\ge\omega\), the union on the right has size at least \(|X|\). Hall’s theorem therefore supplies distinct representatives for all lists, giving a proper coloring. \(\square\)

## 2. A clique-minor bound when \(\alpha\le2\)

**Lemma 2.** If \(F\) is nonempty and \(\alpha(F)\le2\), then
\[
|V(F)|+\omega(F)\le 3h(F).
\tag{2}
\]

**Proof.** Induct on \(n=|V(F)|\). Let \(Q\) be a maximum clique, of size \(\omega\).

If \(n\le2\omega\), then
\[
n+\omega\le3\omega\le3h(F).
\]
Assume henceforth that \(n>2\omega\).

We first show that \(F-Q\) contains an induced three-vertex path. Otherwise, every component of \(F-Q\) is a clique, and there are at most two components because \(\alpha(F)\le2\).

If there is at most one component, then \(|V(F-Q)|\le\omega\), contradicting \(n>2\omega\).

If there are two components, call their vertex sets \(A,B\). There are no edges between \(A\) and \(B\). Each \(q\in Q\) is complete to \(A\) or complete to \(B\): otherwise, a nonneighbor of \(q\) in each of \(A,B\), together with \(q\), would be an independent triple. Partition
\[
Q=Q_A\mathbin{\dot\cup}Q_B
\]
so that \(Q_A\) is complete to \(A\) and \(Q_B\) is complete to \(B\). Both \(A\cup Q_A\) and \(B\cup Q_B\) are cliques. Hence
\[
|A|+|Q_A|\le\omega,\qquad
|B|+|Q_B|\le\omega.
\]
Adding gives \(|A|+|B|\le\omega\), again contradicting \(n>2\omega\).

Thus \(F-Q\) contains an induced path \(x-y-z\). Its vertex set \(D\) is connected and dominating: since \(x,z\) are nonadjacent, every vertex outside \(D\) is adjacent to at least one of \(x,z\), or there would be an independent triple.

Put \(F'=F-D\). Since \(Q\subseteq V(F')\),
\[
\omega(F')=\omega.
\]
Moreover, a clique-minor model in \(F'\), together with \(D\) as one additional branch set, gives
\[
h(F)\ge h(F')+1.
\]
The induction hypothesis now yields
\[
n+\omega
=(|V(F')|+\omega(F'))+3
\le3h(F')+3
\le3h(F).
\]
This proves (2). \(\square\)

Combining Lemmas 1 and 2 gives the announced bound
\[
\boxed{\alpha(F)\le2
\quad\Longrightarrow\quad
\chi_\ell(F)\le
\left\lfloor\frac{3h(F)}2\right\rfloor.}
\tag{3}
\]

## 3. Extending a coloring from a clique

The following lemma is the ingredient needed for clique-gluing.

**Lemma 3.** Let \(H\ge1\) be an integer. Suppose a graph \(F\) satisfies
\[
\omega(F)\le H,
\qquad
|V(F)|+\omega(F)\le3H.
\tag{4}
\]
Let \(S\) be any clique of \(F\), already properly colored. If every vertex outside \(S\) has a list of at least \(2H-1\) colors, then the coloring of \(S\) extends to a proper list coloring of \(F\).

**Proof.** Write \(s=|S|\), so \(s\le H\).

First suppose \(s\le H-1\). Delete all colors used on \(S\) from every remaining list. Each remaining list has size at least \(2H-1-s\). By Lemma 1 and (4),
\[
\chi_\ell(F-S)
\le
\left\lfloor
\frac{|V(F)|-s+\omega(F-S)}2
\right\rfloor
\le
\left\lfloor\frac{3H-s}{2}\right\rfloor.
\]
The available list size is sufficient, since
\[
s+\left\lfloor\frac{3H-s}{2}\right\rfloor
=
\left\lfloor\frac{3H+s}{2}\right\rfloor
\le2H-1.
\]
Coloring \(F-S\) from these reduced lists gives the required extension.

Now suppose \(s=H\). Then \(\omega(F)=H\), and (4) implies
\[
|V(F-S)|\le H.
\]
No vertex outside \(S\) is adjacent to all of \(S\), because that would create an \((H+1)\)-clique. Thus each uncolored vertex has at most \(H-1\) neighbors in \(S\). Removing only the colors used on those neighbors leaves at least
\[
(2H-1)-(H-1)=H
\]
colors at every uncolored vertex. Since there are at most \(H\) such vertices, a greedy coloring completes the extension. \(\square\)

## 4. Proof of the clique-gluing theorem

Let \(H=h(G)\), and give every vertex of \(G\) a list of \(2H-1\) colors.

Every piece \(F_i\) occurs as a subgraph of the final graph \(G\). Therefore
\[
h(F_i)\le H.
\]
Since \(\alpha(F_i)\le2\), Lemma 2 gives
\[
|V(F_i)|+\omega(F_i)\le3h(F_i)\le3H,
\]
and also \(\omega(F_i)\le H\). Thus each piece satisfies Lemma 3.

Color \(F_1\), using Lemma 3 with an empty precolored clique. At every subsequent step, the already-colored vertices of the new piece are exactly its identified clique. Lemma 3 extends this coloring to the new vertices.

New vertices have no old neighbors outside the identified clique, so each extension preserves properness on the entire graph constructed so far. Eventually all of \(G\) is colored. Hence
\[
\chi_\ell(G)\le2h(G)-1.
\]
If \(G\) has no \(K_t\)-minor, then \(h(G)\le t-1\), giving
\[
\boxed{\chi_\ell(G)\le2t-3.}
\]

## 5. A general order bound and necessary counterexample conditions

For an arbitrary \(K_t\)-minor-free graph, one still has \(\omega(G)\le t-1\). Consequently, Lemma 1 gives
\[
\chi_\ell(G)
\le
\left\lfloor\frac{|V(G)|+t-1}{2}\right\rfloor.
\]
In particular,
\[
\boxed{|V(G)|\le3t+2
\quad\Longrightarrow\quad
\chi_\ell(G)\le2t.}
\tag{5}
\]

Thus any counterexample must satisfy the sharper inequality
\[
|V(G)|+\omega(G)\ge4t+2,
\]
and hence must have at least \(3t+3\) vertices.

A vertex-minimal counterexample would additionally satisfy
\[
G\text{ connected},\qquad
\delta(G)\ge2t,\qquad
\alpha(G)\ge3.
\]
Connectedness follows by considering components. For the minimum-degree assertion, fix a bad \(2t\)-list assignment. If a vertex had degree at most \(2t-1\), minimality would permit coloring its deletion, after which its color could be chosen greedily. The independence-number assertion follows from (3).

## What remains unresolved

These arguments do **not** prove the proposed bound for arbitrary \(K_t\)-minor-free graphs.

The crucial minor estimate (2) uses the fact that the nonadjacent endpoints of an induced three-vertex path dominate the graph. That implication fails when an independent triple is allowed. The extension argument therefore has no established input for arbitrary large pieces, and no suitable clique-gluing decomposition is obtained here for general minor-free graphs.

The unrestricted upper bound is not improved, and no counterexample to \(\chi_\ell(G)\le2t\) is produced.