```json
{
  "verdict": "already_resolved",
  "confidence": "medium",
  "one_line": "Postle's fixed-surface bound for fixed-list critical girth-five graphs implies the conjecture after singleton lists are replaced by constant-genus three-list forcing gadgets.",
  "would_publish": false,
  "caveats": "The required input is the uniform fixed-list L-critical theorem, not merely finiteness of underlying choice-critical graphs."
}
```

## Statement of the result used

The relevant fixed-surface consequence of Postle’s work on 3-list-coloring graphs of girth at least five is the following.

> **Fixed-surface \(L\)-critical theorem.**  
> For every integer \(t\), there is an integer \(b(t)\) such that the following holds. Let \(F\) be a graph of girth at least five embeddable in a surface of Euler genus at most \(t\), and let \(M\) be a list assignment satisfying
> \[
> |M(v)|\ge 3\qquad\text{for every }v\in V(F).
> \]
> If \(F\) is \(M\)-critical—that is, \(F\) is not \(M\)-colorable but every proper subgraph of \(F\) is \(M\)-colorable—then
> \[
> |V(F)|\le b(t).
> \]

This is the fixed-list critical formulation arising from the critical-canvas/strong-hyperbolicity result in Luke Postle, *3 List Coloring Graphs of Girth at least Five on Surfaces*, arXiv:1710.06898. It is stronger than the weaker statement that only finitely many underlying graphs are critical with respect to list chromatic number. That distinction is essential below.

I now give a reduction from Conjecture 1.7 to this theorem. The reduction also avoids any assumptions that \(C_1,C_2\) are disjoint, facial, or nested in a particular way.

## A constant-size color-forcing gadget

We first need a fixed graph of girth at least five and chromatic number four.

### Lemma 1

There is a finite 4-critical graph \(Q\) of girth at least five.

#### Proof

For completeness, this follows by a standard probabilistic argument. Let \(X\sim G(n,100/n)\). The expected number of cycles of lengths three and four is bounded independently of \(n\). Hence, with probability tending to one, \(X\) has fewer than \(n/12\) such cycles.

On the other hand, putting \(m=\lceil n/4\rceil\),
\[
\Pr(\alpha(X)\ge m)
 \le {n\choose m}(1-100/n)^{\binom m2}
 \le 2^n\exp\left(-\frac{100}{n}\binom m2\right)
 =o(1).
\]
Thus, for sufficiently large \(n\), there is a graph \(X\) with fewer than \(n/12\) cycles of lengths three or four and with \(\alpha(X)<n/4+1\).

Delete at most one vertex from each cycle of length three or four. The resulting graph \(X'\) has girth at least five and at least \(11n/12\) vertices. For large \(n\),
\[
\alpha(X')\le \alpha(X)<n/4+1<\frac{|V(X')|}{3},
\]
so \(X'\) is not 3-colorable. An inclusion-minimal non-3-colorable subgraph \(Q\subseteq X'\) is 4-critical and still has girth at least five. ∎

Fix a vertex \(x\in V(Q)\). Since \(Q\) is 4-critical, \(Q-x\) has a proper 3-coloring. Moreover:

\[
\tag{1}
\text{In every 3-coloring of \(Q-x\), all three colors occur on \(N_Q(x)\).}
\]

Indeed, if one color were absent from \(N_Q(x)\), assigning that color to \(x\) would give a 3-coloring of \(Q\).

Consequently, for any four distinct colors \(c,a,b,d\), the list assignment
\[
M(x)=\{c,a,b\},\qquad
M(y)=\{a,b,d\}\quad(y\in V(Q)\setminus\{x\})
\]
has the following properties:

1. it is colorable, by coloring \(Q-x\) with \(a,b,d\) and assigning \(c\) to \(x\);
2. every such list-coloring assigns \(c\) to \(x\), since (1) rules out both \(a\) and \(b\) at \(x\).

Thus \(Q\), with these lists, is a gadget forcing its distinguished vertex to receive \(c\).

## Reduction to a fixed-surface critical graph

Let \(G,C_1,C_2,L\) satisfy the hypotheses of the conjecture, and suppose \(G\) is not \(L\)-colorable. Put
\[
S=V(C_1\cup C_2),\qquad r=|S|\le 2k.
\]
For \(v\in S\), write
\[
L(v)=\{c_v\}.
\]

For every \(v\in S\), take a separate copy \(Q_v\) of \(Q\), identifying its distinguished vertex \(x\) with \(v\). Choose three new colors
\[
a_v,b_v,d_v
\]
which are distinct from one another and from every original color; the colors can also be chosen private to \(v\).

Let \(\widehat G\) be the union of \(G\) and these copies \(Q_v\). Define a list assignment \(\widehat L\) by
\[
\widehat L(u)=L(u)\qquad(u\in V(G)\setminus S),
\]
\[
\widehat L(v)=\{c_v,a_v,b_v\}\qquad(v\in S),
\]
and
\[
\widehat L(z)=\{a_v,b_v,d_v\}
   \qquad(z\in V(Q_v)\setminus\{v\}).
\]
Every \(\widehat L\)-list has size at least three.

By the forcing property,
\[
\widehat G\text{ is }\widehat L\text{-colorable}
\quad\Longleftrightarrow\quad
G\text{ is }L\text{-colorable}.
\]
Indeed, every coloring of \(\widehat G\) assigns \(c_v\) to every \(v\in S\), while any \(L\)-coloring of \(G\) extends independently over all copies \(Q_v\). Hence \(\widehat G\) is not \(\widehat L\)-colorable.

### Girth and genus

Each \(Q_v\) meets \(G\) in the single vertex \(v\). Therefore every cycle of \(\widehat G\) lies entirely in \(G\) or in one copy of \(Q\). It follows that \(\widehat G\) has girth at least five.

Let \(h\) be an orientable genus in which \(Q\) embeds. Genus is subadditive under vertex amalgamation, so \(\widehat G\) embeds in an orientable surface of genus at most
\[
rh\le 2kh.
\]
This bound depends only on \(k\), not on \(G\).

## Extracting the bounded obstruction

Choose an inclusion-minimal non-\(\widehat L\)-colorable subgraph \(J\subseteq\widehat G\). Then \(J\) is \(\widehat L|_{V(J)}\)-critical. By the fixed-surface theorem,
\[
|V(J)|\le b(2kh),
\]
where we absorb the harmless conversion between orientable genus and Euler genus into the definition of \(b\).

Now define
\[
H=(J\cap G)\cup C_1\cup C_2.
\]
Then \(H\subseteq G\), it contains both prescribed cycles, and
\[
|V(H)|\le |V(J)|+|S|
          \le b(2kh)+2k.
\]

It remains to prove that \(H\) is not \(L\)-colorable. Suppose otherwise that \(\psi\) is an \(L\)-coloring of \(H\). In particular,
\[
\psi(v)=c_v\qquad(v\in S).
\]

For each \(v\in S\), fix a 3-coloring of \(Q_v-v\) using the private colors \(a_v,b_v,d_v\), which exists because \(Q-v\) is 3-colorable. Color the vertices of
\[
J\cap (Q_v-v)
\]
by the restriction of this fixed coloring. If \(v\in V(J)\), then its color under \(\psi\) is \(c_v\), which is distinct from all three private colors, so every edge from \(v\) into \(Q_v-v\) is properly colored.

Together with \(\psi\) on \(J\cap G\), these colorings give an \(\widehat L\)-coloring of all of \(J\), contradicting the choice of \(J\). Therefore \(H\) is not \(L\)-colorable.

Taking
\[
\boxed{K(k)=2k+b(2kh)}
\]
proves the conjecture. The quantitative linear-in-genus form of Postle’s theorem would moreover give \(K(k)=O(k)\).

## Status and caveat

The reduction is complete and covers overlapping, equal, nonfacial, or otherwise arbitrarily situated cycles. In fact, it proves the stronger statement with \(V(C_1\cup C_2)\) replaced by any bounded set of singleton-list vertices.

The only substantive external input is the uniform theorem for graphs critical with respect to a fixed list assignment. Merely knowing that there are finitely many underlying graphs that are critical for the list chromatic number would not suffice: an \(L\)-critical graph need not be critical for choice number. The critical-canvas formulation of Postle’s result is the needed fixed-assignment statement.