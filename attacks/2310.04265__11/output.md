```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A hereditary class whose members all satisfy directed clique number and dichromatic number at most two has a substitution closure containing digraphs of directed clique number two and arbitrarily large dichromatic number.",
  "would_publish": false,
  "caveats": "This uses the standard definitions for finite loopless digraphs and iterated substitution; the construction is oriented and the base class is hereditary."
}
```

# Counterexample

Write \(\vec\chi(D)\) for the dichromatic number and
\[
\vec\omega(D)=\min_{\prec}\omega(D^\prec)
\]
for the directed clique number defined through backedge graphs.

The conjecture is false, even for a hereditary class \(\mathcal C\) satisfying
\[
\vec\chi(J)=\vec\omega(J)\le 2
\qquad\text{for every }J\in\mathcal C.
\]

## 1. Basic observations

For every digraph \(D\),
\[
\vec\chi(D)=\min_{\prec}\chi(D^\prec).
\]

Indeed, a proper coloring of \(D^\prec\) partitions \(D\) into sets in which every arc points forward in \(\prec\), and hence into acyclic sets. Conversely, concatenate topological orderings of the color classes of a dichromatic coloring.

Consequently,
\[
\vec\omega(D)\le \vec\chi(D).
\]
Moreover,
\[
\vec\omega(D)=1 \quad\Longleftrightarrow\quad D\text{ is acyclic}.
\]

## 2. The base digraph associated with an ordered graph

Let \(H\) be a finite simple graph with an ordering
\[
V(H)=\{x_1,\dots,x_m\}.
\]
Define an oriented graph \(S(H)\) as follows. Besides the vertices \(x_1,\dots,x_m\), introduce one vertex \(a_{ij}\) for every edge \(x_ix_j\in E(H)\), where \(i<j\). For every such edge add the three arcs
\[
x_i\longrightarrow a_{ij},\qquad
a_{ij}\longrightarrow x_j,\qquad
x_j\longrightarrow x_i,
\]
and add no other arcs.

Thus each edge \(x_ix_j\) of \(H\) gives a directed triangle
\[
x_i\longrightarrow a_{ij}\longrightarrow x_j\longrightarrow x_i.
\]

Let
\[
X=\{x_1,\dots,x_m\},\qquad
A=\{a_{ij}:x_ix_j\in E(H),\,i<j\}.
\]
Then \(A\) is independent, while \(S(H)[X]\) is acyclic because every arc in \(X\) goes from a higher index to a lower index. Hence
\[
\vec\chi(S(H))\le 2.
\]
If \(H\) has an edge, \(S(H)\) contains a directed triangle, so in fact
\[
\vec\chi(S(H))=2.
\]

The same partition shows that every induced subdigraph of \(S(H)\) is 2-dicolorable.

Define
\[
\mathcal C=
\{J:\ J\text{ is isomorphic to an induced subdigraph of }S(H)
\text{ for some finite triangle-free graph }H\}.
\]
This is hereditary. Every \(J\in\mathcal C\) has \(\vec\chi(J)\le2\). If \(J\) is acyclic, then
\(\vec\chi(J)=\vec\omega(J)=1\); otherwise
\[
2\le\vec\omega(J)\le\vec\chi(J)\le2.
\]
Therefore
\[
\vec\chi(J)=\vec\omega(J)\le2
\]
for every nonempty \(J\in\mathcal C\). In particular, \(\mathcal C\) is \(\vec\chi\)-bounded, even by the identity function.

## 3. A substitution amplifier

Let \(G\) be a nonempty digraph, and let \(H\) be an ordered graph. Define \(F_H(G)\) from the skeleton \(S(H)\) by:

- replacing every edge-vertex \(a_{ij}\) by a copy \(G_{ij}\) of \(G\);
- leaving every \(x_i\) as a singleton.

Thus, for each edge \(x_ix_j\), \(i<j\), the cross-arcs are
\[
x_i\longrightarrow G_{ij},\qquad
G_{ij}\longrightarrow x_j,\qquad
x_j\longrightarrow x_i.
\]

### Lemma 1: Dichromatic amplification

If
\[
q=\vec\chi(G)
\quad\text{and}\quad
\chi(H)>q,
\]
then
\[
\vec\chi(F_H(G))=q+1.
\]

#### Proof

For the upper bound, color every copy \(G_{ij}\) using the same palette of \(q\) colors. There are no arcs between distinct copies because the vertices \(a_{ij}\) form an independent set in \(S(H)\). Hence each of those \(q\) color classes is acyclic. Color all vertices \(x_i\) with one additional color; their induced subdigraph is acyclic. Therefore
\[
\vec\chi(F_H(G))\le q+1.
\]

Suppose instead that \(F_H(G)\) has a \(q\)-dicoloring. Each copy \(G_{ij}\), having dichromatic number \(q\), must use every one of the \(q\) global colors.

The colors on \(x_1,\dots,x_m\) do not form a proper \(q\)-coloring of \(H\), since \(\chi(H)>q\). Thus some edge \(x_ix_j\), \(i<j\), has both endpoints colored with the same color \(c\). The copy \(G_{ij}\) contains a vertex \(y\) of color \(c\). But
\[
x_i\longrightarrow y\longrightarrow x_j\longrightarrow x_i
\]
is then a monochromatic directed triangle, a contradiction. Hence
\[
\vec\chi(F_H(G))\ge q+1.
\]
This proves the lemma. \(\square\)

### Lemma 2: Directed clique number remains two

If \(H\) is triangle-free and \(\vec\omega(G)\le2\), then
\[
\vec\omega(F_H(G))\le2.
\]

#### Proof

Choose an ordering \(\prec_G\) of \(G\) for which
\[
\omega(G^{\prec_G})\le2.
\]

Order \(F_H(G)\) as follows:
\[
x_1,\quad
\{\text{all blocks }G_{1j}\},\quad
x_2,\quad
\{\text{all blocks }G_{2j}\},\quad
\dots,\quad
x_m,
\]
where every block \(G_{ij}\) is ordered internally according to \(\prec_G\), and the blocks within one slot are ordered arbitrarily.

For every edge \(x_ix_j\) with \(i<j\), this gives
\[
x_i\prec G_{ij}\prec x_j.
\]
Consequently, both \(x_i\to G_{ij}\) and \(G_{ij}\to x_j\) point forward. The arc \(x_j\to x_i\) is backward. There are no other cross-arcs. Therefore the backedge graph in this ordering is exactly
\[
H\ \dot\cup\ \biguplus_{x_ix_j\in E(H)}G^{\prec_G}.
\]
Since \(H\) is triangle-free and each \(G^{\prec_G}\) has clique number at most two, this backedge graph has clique number at most two. Thus
\[
\vec\omega(F_H(G))\le2.
\]
\(\square\)

If \(H\) has an edge, \(F_H(G)\) contains a directed triangle, so it is not acyclic. In that case Lemma 2 gives
\[
\vec\omega(F_H(G))=2.
\]

## 4. Fully explicit choice of the graphs \(H\)

We use the Mycielski construction only to obtain explicitly specified triangle-free graphs of arbitrarily large chromatic number.

For a graph \(H\) with vertices \(v_1,\dots,v_t\), its Mycielskian \(\mu(H)\) has:

- the original vertices \(v_i\);
- new vertices \(u_i\);
- one additional vertex \(w\);

with the old edges of \(H\), edges \(u_iv_j\) whenever \(v_iv_j\in E(H)\), and edges \(wu_i\) for every \(i\).

If \(H\) is triangle-free, then \(\mu(H)\) is triangle-free. Also,
\[
\chi(\mu(H))=\chi(H)+1.
\]
For completeness, the upper bound is obtained by giving \(u_i\) the color of \(v_i\) and giving \(w\) a new color. For the lower bound, in a hypothetical \(\chi(H)\)-coloring of \(\mu(H)\), rename the color of \(w\) as the last color. No \(u_i\) has that color. Recolor every old \(v_i\) having the last color with the color of \(u_i\); this produces a \((\chi(H)-1)\)-coloring of \(H\), a contradiction.

Set
\[
H_n=\mu^{\,n+1}(K_2).
\]
Then \(H_n\) is triangle-free and
\[
\chi(H_n)=n+3.
\]

## 5. The unbounded sequence in the substitution closure

Let
\[
G_0=S(K_2).
\]
This is a directed triangle, so
\[
\vec\chi(G_0)=\vec\omega(G_0)=2.
\]

Recursively define
\[
G_{n+1}=F_{H_n}(G_n).
\]

Because \(S(H_n)\in\mathcal C\), the one-vertex digraph belongs to \(\mathcal C\), and \(G_{n+1}\) is obtained by substituting \(G_n\) into the edge-vertices of \(S(H_n)\), every \(G_n\) belongs to the substitution closure of \(\mathcal C\).

We prove inductively that
\[
\vec\chi(G_n)=n+2,
\qquad
\vec\omega(G_n)=2.
\]

The assertion holds for \(G_0\). Assuming it for \(G_n\), we have
\[
\chi(H_n)=n+3>\vec\chi(G_n)=n+2.
\]
Lemma 1 gives
\[
\vec\chi(G_{n+1})=n+3.
\]
Since \(H_n\) is triangle-free, Lemma 2 gives
\[
\vec\omega(G_{n+1})\le2.
\]
The digraph \(G_{n+1}\) contains directed triangles, so it is not acyclic; hence
\[
\vec\omega(G_{n+1})=2.
\]

Therefore the substitution closure of \(\mathcal C\) contains digraphs \(G_n\) satisfying
\[
\vec\omega(G_n)=2
\quad\text{and}\quad
\vec\chi(G_n)=n+2.
\]
No function of \(\vec\omega\) can bound their dichromatic numbers.

Thus the closure under substitution of a \(\vec\chi\)-bounded class need not be \(\vec\chi\)-bounded. The conjecture is disproved.