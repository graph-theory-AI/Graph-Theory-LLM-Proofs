```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Yes: a later theorem states that every even-hole-free graph of sufficiently large treewidth contains an induced diamond or a K4.",
  "would_publish": false,
  "caveats": "The deep later structure theorem is used as a black box, and no explicit numerical treewidth bound is extracted."
}
```

## Statement

Let \(\mathcal C\) be the class of finite simple graphs containing no induced even hole, no induced diamond \(K_4-e\), and no \(K_4\). The question asks whether there is an absolute constant \(c\) such that
\[
\operatorname{tw}(G)\le c\qquad\text{for every }G\in\mathcal C.
\]

The answer is affirmative.

## Later theorem resolving the question

The relevant later paper is:

Tara Abrishami, Maria Chudnovsky, Sepehr Hajebi, and Sophie Spirkl,  
*Induced subgraphs and tree decompositions XI. Local structure in even-hole-free graphs of large treewidth*, arXiv:2309.04390.

Its main result has the following consequence, stated in the form needed here.

> **Theorem.** There exists an absolute constant \(c\) such that every even-hole-free graph \(G\) with
> \[
> \operatorname{tw}(G)>c
> \]
> contains either a \(K_4\) or an induced diamond.

Equivalently, the class of \((\text{even hole},K_4,\text{diamond})\)-free graphs has bounded treewidth. This is precisely the structure theorem alluded to—but not verified—in the catalog review.

There is no convention issue concerning the word “diamond.” Even if a diamond in the theorem were understood merely as a subgraph on four vertices with five specified edges, the sixth edge either is absent, giving an induced diamond, or is present, giving a \(K_4\).

## Deduction

Let \(G\in\mathcal C\). If \(\operatorname{tw}(G)>c\), the theorem produces either:

1. a \(K_4\), contrary to the definition of \(\mathcal C\); or
2. an induced diamond, again contrary to the definition of \(\mathcal C\).

Therefore
\[
\operatorname{tw}(G)\le c
\]
for every \(G\in\mathcal C\). Thus \(\mathcal C\) has bounded treewidth.

A useful local way to see why the two forbidden four-vertex graphs naturally occur together is the following. For every vertex \(v\) of a \((K_4,\text{diamond})\)-free graph, \(G[N(v)]\) has maximum degree at most one. Indeed, if \(b\in N(v)\) had two neighbors \(a,c\in N(v)\), then \(v,a,b,c\) would induce a diamond when \(ac\notin E(G)\), and a \(K_4\) when \(ac\in E(G)\). Hence every open neighborhood is a disjoint union of isolated vertices and edges.

## Clique-width

Bounded treewidth implies bounded clique-width. For example, under the standard definitions, for \(k\ge1\),
\[
\operatorname{cw}(G)\le 3\cdot 2^{\,\operatorname{tw}(G)-1}.
\]
Consequently, every \(G\in\mathcal C\) satisfies
\[
\operatorname{cw}(G)\le 3\cdot 2^{c-1}.
\]

Thus both the treewidth and the clique-width are bounded.

## Scope and gap

The implication from the cited theorem is complete and covers all finite graphs in the class. What is not reproduced here is the long structural proof of that later theorem, nor is an explicit value of \(c\) extracted. The present writeup is therefore a literature resolution and direct corollary, not a new proof suitable for separate publication.