```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "Every Eulerian graph with an odd number of edges, in particular the triangle, is a counterexample.",
  "would_publish": false,
  "caveats": "This concerns the displayed inequality without an outer floor and uses the standard definition of an Alon-Tarsi orientation."
}
```

## Statement

Under the standard definition, an orientation \(D\) is Alon–Tarsi if
\[
\operatorname{diff}(D)
 =\sum_{A\in\mathcal E(D)}(-1)^{|A|}
\neq 0,
\]
where \(\mathcal E(D)\) is the family of Eulerian spanning subdigraphs of \(D\), including the empty subdigraph.

The proposed statement is false.

## A general obstruction

**Lemma.** If \(D\) is an Eulerian orientation with an odd number of edges, then \(D\) is not an Alon–Tarsi orientation.

**Proof.** For every Eulerian subdigraph \(A\subseteq D\), its edge-complement \(D\setminus A\) is also Eulerian, since at each vertex
\[
d^+_{D\setminus A}(v)-d^-_{D\setminus A}(v)
=
\bigl(d_D^+(v)-d_D^-(v)\bigr)
-
\bigl(d_A^+(v)-d_A^-(v)\bigr)
=0.
\]
If \(|E(D)|\) is odd, then
\[
|E(D)\setminus E(A)|=|E(D)|-|E(A)|
\]
has parity opposite to that of \(|E(A)|\). Thus complementation is a parity-reversing bijection between the even and odd Eulerian subdigraphs. Consequently
\[
\operatorname{diff}(D)=0.
\]
Hence \(D\) is not Alon–Tarsi. \(\square\)

Now let \(G\) be any graph in which every vertex has even degree, say \(d_G(v)=2k_v\), and suppose \(|E(G)|\) is odd. If a spanning subgraph \(H\) had an orientation \(D\) satisfying the displayed bound, then integrality of the outdegree would give
\[
d_D^+(v)\ge \frac{2k_v-1}{2}=k_v-\frac12
\quad\Longrightarrow\quad
d_D^+(v)\ge k_v=\frac{d_G(v)}2.
\]
Summing over all vertices,
\[
|E(H)|=\sum_v d_D^+(v)
   \ge \frac12\sum_v d_G(v)
   =|E(G)|.
\]
Since \(H\subseteq G\), equality must hold. Therefore \(H=G\) and
\[
d_D^+(v)=\frac{d_G(v)}2=d_D^-(v)
\]
at every vertex. Thus \(D\) is an Eulerian orientation with the odd number \(|E(G)|\) of edges, so the lemma shows that \(D\) cannot be Alon–Tarsi.

## Smallest explicit counterexample

Take \(G=C_3\). Every vertex has degree \(2\), so the required inequality is
\[
d_D^+(v)\ge \frac{2-1}{2}=\frac12,
\]
hence \(d_D^+(v)\ge1\). Summing forces \(H=C_3\) and every vertex to have outdegree \(1\), so \(D\) is a directed triangle. Its only Eulerian subdigraphs are the empty subdigraph and the whole directed triangle. One has zero edges and the other three edges, giving one even and one odd Eulerian subdigraph. Therefore \(D\) is not Alon–Tarsi.

The same argument applies to every odd cycle.

## Caveat concerning the formulation

The counterexample relies on the inequality exactly as displayed:
\[
d_D^+(v)\ge \frac{d_G(v)-1}{2}.
\]
If the intended bound were instead
\[
d_D^+(v)\ge \left\lfloor\frac{d_G(v)-1}{2}\right\rfloor,
\]
then a degree-two vertex would only require outdegree \(0\), and this counterexample would not apply. Given how elementary the triangle obstruction is, the source and catalog should be checked for a missing floor or an omitted hypothesis. Under the supplied statement, however, there is no gap in the disproof.