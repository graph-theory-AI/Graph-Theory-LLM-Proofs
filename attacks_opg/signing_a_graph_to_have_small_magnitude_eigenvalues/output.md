```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Explicit Hadamard constructions prove the conjectured bound for sufficiently thick independent-set blow-ups and for a near-complete regime, but do not resolve arbitrary regular graphs.",
  "would_publish": false,
  "caveats": "No novelty claim; blow-ups are not lifts and change the degree. The substantive conjecture is interpreted for d >= 2."
}
```

# Partial results

I work with finite simple graphs and the intended degree range \(d\ge 2\). Taken literally at \(d=1\), the displayed conjecture has the trivial exception \(K_2\), whose signed adjacency matrices have eigenvalues \(1,-1\). This is not the substantive open case.

For a real symmetric signed adjacency matrix \(S\), the required quantity is its operator norm:
\[
\|S\|=\max_{\lambda\in\operatorname{Spec}(S)}|\lambda|.
\]

Below are two self-contained special cases, including genuinely non-bipartite graphs. I then give an explicit obstruction to a natural attempt to extend the interlacing argument.

## 1. Independent-set blow-ups admit the required signings

For a graph \(G\) and an integer \(t\), let \(G^{(t)}\) denote its **independent-set \(t\)-blow-up**: replace each vertex \(v\) by \(t\) independent vertices, and replace each edge \(uv\) by a complete bipartite graph between the two corresponding sets.

Thus, if \(G\) is \(d\)-regular, then \(G^{(t)}\) is \(dt\)-regular. This construction is **not** a \(t\)-lift.

### Theorem 1

Let \(G\) be a \(d\)-regular graph, where \(d\ge 2\), and let \(t\ge d\). Then \(G^{(t)}\) has a symmetric signing \(S\) satisfying
\[
\boxed{\quad
\|S\|\le 2\sqrt{(d-1)(t-1)}
       <2\sqrt{dt-1}.
\quad}
\]
Consequently, \(G^{(t)}\) satisfies the conjecture.

More precisely, if \(q\) and \(N\) are the least powers of two satisfying
\[
q\ge d,\qquad N\ge t,
\]
then the construction gives
\[
\|S\|\le \sqrt{qN}.
\]

### Proof

We use only Sylvester Hadamard matrices, whose existence is elementary. Set
\[
H_1=(1),\qquad
H_{2a}=
\begin{pmatrix}
H_a&H_a\\
H_a&-H_a
\end{pmatrix}.
\]
For every power of two \(a\), the matrix \(H_a\) is symmetric, has entries in \(\{-1,1\}\), and satisfies
\[
H_aH_a^{\mathsf T}=aI_a.
\]

Since \(t\ge d\), we have \(N\ge q\). Write
\[
N=qb,
\]
where \(b\) is also a power of two.

We first sign \(G^{(N)}\), and then take an induced subgraph.

#### Step 1: Assign orthogonal channels to incidences

Write the columns of \(H_q\) as \(h_1,\ldots,h_q\). At each vertex \(v\), assign its incident edges distinct labels
\[
\ell_v(e)\in\{1,\ldots,q\}.
\]
This is possible because \(d\le q\). The labels at the two ends of an edge need not agree.

Index the \(N\) vertices above \(v\) by
\[
\{1,\ldots,q\}\times\{1,\ldots,b\}.
\]
For an edge \(e=uv\), define its signed \(N\times N\) block by
\[
B_{uv}
=
\bigl(h_{\ell_u(e)}h_{\ell_v(e)}^{\mathsf T}\bigr)
\otimes H_b.
\]
Every entry is \(1\) or \(-1\). Set \(B_{vu}=B_{uv}^{\mathsf T}\), and put zero blocks on nonedges and on the diagonal. This gives a symmetric signing \(B\) of \(G^{(N)}\).

#### Step 2: Compute its norm exactly

At every vertex, make the orthogonal change of basis
\[
U=\frac{H_q}{\sqrt q}\otimes I_b.
\]
Because
\[
\left(\frac{H_q}{\sqrt q}\right)^{\mathsf T}h_i
=\sqrt q\,e_i,
\]
the transformed block corresponding to \(e=uv\) is
\[
U^{\mathsf T}B_{uv}U
=qE_{\ell_u(e),\ell_v(e)}\otimes H_b.
\]

The distinct-label condition is crucial: each channel \((v,i)\) is used by at most one edge. Hence, after a permutation of coordinates, the whole transformed matrix is a direct sum of zero blocks and one block
\[
\begin{pmatrix}
0&qH_b\\
qH_b^{\mathsf T}&0
\end{pmatrix}
\]
for each edge of \(G\).

The square of each displayed block is \(q^2bI\). Therefore
\[
\|B\|=q\sqrt b=\sqrt{qN}.
\]

#### Step 3: Restrict to \(t\) vertices in each fiber

Keep any \(t\) vertices in each \(N\)-vertex fiber. The resulting principal submatrix \(S\) is a symmetric signing of \(G^{(t)}\). Compression cannot increase operator norm, so
\[
\|S\|\le \|B\|=\sqrt{qN}.
\]

For every integer \(a\ge2\), its least enclosing power of two is at most \(2a-2\). Thus
\[
q\le2d-2,\qquad N\le2t-2,
\]
and consequently
\[
\|S\|\le\sqrt{qN}
\le2\sqrt{(d-1)(t-1)}.
\]
Finally,
\[
(d-1)(t-1)=dt-d-t+1<dt-1.
\]
Since the degree of \(G^{(t)}\) is \(dt\), this proves the theorem. \(\square\)

### Consequences and sharpness within this construction

1. **Arbitrary non-bipartite bases are allowed.**  
   If \(G\) contains an odd cycle, choosing one vertex from each corresponding fiber gives the same odd cycle in \(G^{(t)}\). Thus Theorem 1 is not merely another bipartite case.

2. **The \(d\)-blow-up always works.**  
   Every \(d\)-regular \(G\) has a \(d^2\)-regular blow-up satisfying
   \[
   \|S\|\le 2d-2<2\sqrt{d^2-1}.
   \]

3. **Some of these signings are optimal.**  
   If both \(d\) and \(t\) are powers of two, with \(t\ge d\), then \(q=d\) and \(N=t\). There are no unused channels, and the construction satisfies
   \[
   S^2=dt\,I.
   \]
   Hence
   \[
   \|S\|=\sqrt{dt}.
   \]
   This is the smallest possible norm for a signing of a \(dt\)-regular graph: if the graph has \(M\) vertices, then
   \[
   \operatorname{tr}(S^2)=Mdt,
   \]
   so at least one eigenvalue has squared magnitude at least \(dt\).

## 2. A near-complete regime

The same Hadamard matrices also give a direct result for the original graph, without taking a blow-up.

### Proposition 2

Let \(G\) be a \(d\)-regular graph on \(n\) vertices, and let \(L\) be the least power of two with \(L\ge n\). Then \(G\) has a symmetric signing satisfying
\[
\boxed{\quad \|S\|\le\sqrt L+n-d.\quad}
\]
In particular, the conjecture holds whenever
\[
\sqrt L+n-d\le2\sqrt{d-1}.
\]

### Proof

Let \(K\) be an \(n\times n\) principal submatrix of the symmetric Sylvester matrix \(H_L\). Then
\[
\|K\|\le\sqrt L.
\]

Define \(R\) by retaining the entries of \(K\) on the diagonal and on nonedges of \(G\), and setting its other entries to zero. Every row of \(R\) has exactly \(n-d\) nonzero entries, all of magnitude one. Since \(R\) is symmetric,
\[
\|R\|\le n-d.
\]

Now
\[
S=K-R
\]
is a symmetric signing of the adjacency matrix of \(G\). Therefore
\[
\|S\|\le\|K\|+\|R\|\le\sqrt L+n-d.
\]
\(\square\)

Writing
\[
r=n-1-d
\]
for the degree of the complement, and using \(L\le2n-2\), a sufficient condition is
\[
\sqrt{2d+2r}+r+1\le2\sqrt{d-1}.
\]
Consequently, for every fixed
\[
0<c<2-\sqrt2,
\]
the conjecture holds for all sufficiently large \(d\) whenever
\[
r\le c\sqrt d.
\]
Indeed, after division by \(\sqrt d\), the sufficient inequality has limiting left-hand side at most \(\sqrt2+c<2\).

This covers a genuinely non-bipartite regime: here \(n=d+O(\sqrt d)<2d\) for large \(d\), whereas a \(d\)-regular bipartite graph must have at least \(2d\) vertices.

## 3. Why the obvious two-sided interlacing attempt fails

The MSS theorem cited in the question supplies, for an arbitrary \(d\)-regular graph, a signing with
\[
\lambda_{\max}(S)\le2\sqrt{d-1}.
\]
For bipartite graphs, spectral symmetry supplies the lower bound as well. For a general graph, negating a signing only exchanges the two ends; it does not guarantee that the same signing controls both.

A natural proposed repair is to study
\[
q_s(x)=\det(xI-S_s^2),
\]
whose largest root is exactly \(\|S_s\|^2\). One might hope that these polynomials form an interlacing family under independent random edge signs.

They do not, even for \(C_4\).

### Exact calculation on \(C_4\)

Under a uniform random signing, the product of the four edge signs is equally likely to be \(1\) or \(-1\).

- If the product is \(1\), switching gives the unsigned cycle, whose spectrum is
  \[
  \{2,0,0,-2\}.
  \]
  Thus
  \[
  q_+(x)=x^2(x-4)^2.
  \]

- If the product is \(-1\), the spectrum is
  \[
  \{\sqrt2,\sqrt2,-\sqrt2,-\sqrt2\},
  \]
  so
  \[
  q_-(x)=(x-2)^4.
  \]

It follows that
\[
\mathbb E\,q_s(x)
=\frac12x^2(x-4)^2+\frac12(x-2)^4.
\]
Putting \(y=x-2\), this becomes
\[
y^4-4y^2+8=(y^2-2)^2+4.
\]
It is strictly positive for every real \(x\), and therefore has **no real roots**.

Thus the direct uniform-average characteristic-polynomial strategy for \(S_s^2\) fails at the real-rootedness step. This is not a counterexample to the conjecture—\(C_4\) is easy—but it rules out this particular straightforward extension of the MSS mechanism.

## 4. What remains unresolved

The arguments above are complete under their stated hypotheses, but neither removes the central difficulty.

- The blow-up construction uses many coordinates per original vertex to place its incident edges in mutually orthogonal channels. Compressing back to one vertex per fiber loses the useful norm bound. It does not produce a good \(2\)-lift of the original graph.
- The dense construction relies on having few missing edges.
- The squared-characteristic-polynomial calculation blocks only one natural approach, not all possible interlacing methods.

In particular, these arguments do not establish the conjecture for a general non-bipartite cubic graph, or for arbitrary regular graphs without either special structure. I make no claim that the two Hadamard observations are new or, by themselves, publication-worthy.