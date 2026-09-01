```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For every m,m' and every orientation F of K_{1,4}, the pair is not dichromatically finite: suitable locally transitive orientations of L(K_{n,n}) are claw-free, directed-triangle-free, and have dichromatic number Ω(√n).",
  "would_publish": false,
  "caveats": "This uses the standard induced-subdigraph meaning of F-free and the cyclic-composition definition of Delta; the supplied 2026 preprint title may overlap, so novelty is not asserted."
}
```

# Statement

Let \(F\) be any orientation of \(K_{1,4}\), and let \(m,m'\geq 1\). Then
\[
\sup\{\vec\chi(D):D\text{ is }\{\Delta(1,m,m'),F\}\text{-free}\}=\infty.
\]
Thus there are no pairs \((m,m')\) for which \(\{\Delta(1,m,m'),F\}\) is \(\vec\chi\)-finite.

In fact, we prove the stronger assertion that there are oriented graphs of arbitrarily large dichromatic number which

1. contain no directed triangle, and
2. have claw-free underlying graph.

Since every \(\Delta(1,m,m')\) contains a directed triangle, and every induced \(K_{1,4}\) contains an induced claw, this implies the result.

# Construction

Let \(B_n=K_{n,n}\), with bipartition \(X\cup Y\). We construct an orientation \(D_n\) of its line graph \(L(B_n)\).

For every \(z\in X\cup Y\), independently choose a uniformly random linear order
\[
\prec_z
\]
of the \(n\) edges of \(B_n\) incident with \(z\).

The vertices of \(D_n\) are the edges of \(B_n\). If two edges \(e,f\) share the endpoint \(z\), orient their corresponding edge of \(L(B_n)\) as
\[
e\longrightarrow f \quad\Longleftrightarrow\quad e\prec_z f.
\]
Since two distinct edges of a simple graph share at most one endpoint, this is well-defined.

Thus every clique of \(L(B_n)\) consisting of the edges incident with a fixed vertex \(z\) is oriented transitively.

## Forbidden induced configurations

### The underlying graph is claw-free

Every line graph of a simple graph is claw-free. Directly, if \(e=xy\) is the center of a putative induced claw in \(L(B_n)\), each leaf corresponds to an edge incident with \(x\) or \(y\). Among three leaves, two meet the same endpoint of \(e\), so those two leaves are adjacent in the line graph, a contradiction.

Consequently \(L(B_n)\) has no induced \(K_{1,4}\), and \(D_n\) contains no induced copy of any orientation \(F\) of \(K_{1,4}\).

### There is no directed triangle

A triangle in \(L(B_n)\) corresponds to three pairwise intersecting edges of \(B_n\). Three pairwise intersecting edges in a simple graph either have a common endpoint or form a triangle. Since \(B_n\) is bipartite, they must have a common endpoint.

Such a triangle is oriented according to one of the orders \(\prec_z\), and hence is transitive. Therefore \(D_n\) has no directed triangle.

# The probabilistic dichromatic-number bound

For an oriented graph \(D\), write
\[
a(D)=\max\{|S|:D[S]\text{ is acyclic}\}.
\]
Then
\[
\vec\chi(D)\geq \frac{|V(D)|}{a(D)}.
\]

We shall show that, with positive probability,
\[
a(D_n)<7n^{3/2}.
\]

## Lemma 1: Counting acyclic orientations

For every finite simple graph \(Q\), the number \(A(Q)\) of acyclic orientations of \(Q\) satisfies
\[
A(Q)\leq \prod_{v\in V(Q)}\bigl(d_Q(v)+1\bigr).
\]

### Proof

An acyclic orientation is uniquely determined by its indegree sequence.

Indeed, suppose two acyclic orientations \(O,O'\) have the same indegree at every vertex, and let \(R\) be the set of edges on which they differ. Orient the edges of \(R\) as in \(O\). Equality of the two indegree sequences implies that, at each vertex, the number of edges of \(R\) entering it in \(O\) equals the number leaving it in \(O\). Thus, if \(R\neq\varnothing\), the oriented graph \(O[R]\) is a nonempty balanced digraph and therefore contains a directed cycle. This contradicts the acyclicity of \(O\). Hence \(R=\varnothing\).

There are at most \(d_Q(v)+1\) possible indegrees at \(v\), giving the asserted bound. \(\square\)

## Lemma 2: Probability that a fixed set is acyclic

Let \(S\subseteq E(B_n)\) have \(|S|=s\). Then
\[
\Pr\bigl(D_n[S]\text{ is acyclic}\bigr)
   \leq \left(\frac{2e^2n}{s}\right)^s.
\]

### Proof

Let \(G_S=(X\cup Y,S)\), and let \(d_z\) be the degree of \(z\) in \(G_S\). Restricting the independently chosen orders \(\prec_z\) to the edges of \(S\) gives independent uniform orders of the \(d_z\) incident edges. Hence there are
\[
\prod_{z\in X\cup Y} d_z!
\]
equiprobable local-order systems.

Moreover, the favorable local-order systems are exactly the acyclic orientations of \(L(G_S)\): every acyclic orientation restricts to a transitive orientation on each clique of edges incident with \(z\), and these transitive orientations recover the local orders.

For \(uv\in S\), its degree as a vertex of \(L(G_S)\) is
\[
d_u+d_v-2.
\]
By Lemma 1,
\[
\Pr\bigl(D_n[S]\text{ is acyclic}\bigr)
\leq
\frac{\displaystyle\prod_{uv\in S}(d_u+d_v-1)}
     {\displaystyle\prod_{z\in X\cup Y}d_z!}.
\]
Using \(d_u+d_v-1\leq d_u+d_v\) and
\[
d!\geq (d/e)^d,
\]
we obtain
\[
\begin{aligned}
\Pr\bigl(D_n[S]\text{ is acyclic}\bigr)
&\leq
e^{2s}
\frac{\displaystyle\prod_{uv\in S}(d_u+d_v)}
     {\displaystyle\prod_z d_z^{d_z}}\\
&=
e^{2s}\prod_{uv\in S}
\frac{d_u+d_v}{d_ud_v}\\
&=
e^{2s}\prod_{uv\in S}
\left(\frac1{d_u}+\frac1{d_v}\right).
\end{aligned}
\]
Now
\[
\begin{aligned}
\sum_{uv\in S}\left(\frac1{d_u}+\frac1{d_v}\right)
&=
|\{u\in X:d_u>0\}|+|\{v\in Y:d_v>0\}|\\
&\leq 2n.
\end{aligned}
\]
The arithmetic-geometric mean inequality therefore gives
\[
\prod_{uv\in S}\left(\frac1{d_u}+\frac1{d_v}\right)
\leq \left(\frac{2n}{s}\right)^s.
\]
Consequently
\[
\Pr\bigl(D_n[S]\text{ is acyclic}\bigr)
\leq \left(\frac{2e^2n}{s}\right)^s.
\]
\(\square\)

## Union bound

Let
\[
s=\left\lceil 7n^{3/2}\right\rceil,
\]
where \(n\) is sufficiently large that \(s\leq n^2\). By Lemma 2 and
\[
\binom{n^2}{s}\leq \left(\frac{en^2}{s}\right)^s,
\]
we have
\[
\begin{aligned}
\Pr\bigl(\exists S,\ |S|=s,\ D_n[S]\text{ acyclic}\bigr)
&\leq
\binom{n^2}{s}\left(\frac{2e^2n}{s}\right)^s\\
&\leq
\left(\frac{2e^3n^3}{s^2}\right)^s\\
&\leq
\left(\frac{2e^3}{49}\right)^s.
\end{aligned}
\]
Since \(2e^3<49\), this probability is strictly less than \(1\). Hence there exists a choice of the local orders for which no \(s\)-vertex set is acyclic. A larger acyclic set would contain an acyclic \(s\)-vertex subset, so for this choice
\[
a(D_n)\leq s-1<7n^{3/2}.
\]

Since \(|V(D_n)|=|E(K_{n,n})|=n^2\),
\[
\vec\chi(D_n)
\geq \frac{n^2}{a(D_n)}
> \frac{\sqrt n}{7}.
\]
Thus the dichromatic numbers of these directed-triangle-free, claw-free oriented graphs are unbounded.

# Application to \(\Delta(1,m,m')\)

Under the standard definition, \(\Delta(1,m,m')\) consists of three nonempty transitive blocks with all arcs between the blocks oriented cyclically. Selecting one vertex from each block gives a directed triangle. Therefore every directed-triangle-free oriented graph is \(\Delta(1,m,m')\)-free for every \(m,m'\geq1\).

The graphs \(D_n\) constructed above are simultaneously

- \(\Delta(1,m,m')\)-free,
- \(F\)-free for every orientation \(F\) of \(K_{1,4}\), and
- of unbounded dichromatic number.

It follows that no pair \((m,m')\) yields a \(\vec\chi\)-finite set \(\{\Delta(1,m,m'),F\}\).

# Gaps and scope

There is no mathematical gap under the source paper's induced-subdigraph convention. If “\(F\)-free” were instead meant in the non-induced subdigraph sense, claw-freeness would not suffice, but that is not the convention in the stated problem. The proof is existential rather than deterministic, though the random construction and positive-probability estimate are completely specified.