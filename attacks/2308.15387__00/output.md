```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A binary vector-space difference colouring gives f(n,r,s) at most 2^s n/(r+1) when r=2^d-1, contradicting the proposed logarithmic factor already for s=1 and even for some s tending to infinity.",
  "would_publish": false,
  "caveats": "This refutes the statement exactly as supplied; a version with a lower restriction on s or a missing min{2^s,...} term is not resolved here."
}
```

# Statement and interpretation

Under the standard definition, for an \(r\)-edge-colouring \(\chi\) of \(K_n\) and \(C\subseteq [r]\), let \(G_C\) be the spanning graph consisting of edges whose colours lie in \(C\). Then
\[
f(n,r,s)=
\min_{\chi:E(K_n)\to[r]}
\max_{\substack{C\subseteq[r]\\ |C|\le s}}
\{\text{largest component order of }G_C\}.
\]

The supplied conjecture asserts, uniformly over
\[
1\le s\le \frac{\sqrt r}{\log r},
\]
that
\[
f(n,r,s)=\frac{s^2(\log r)^{1-o_r(1)}}r\,n
\]
for sufficiently large \(n\).

As written, this is false.

## Binary vector-space construction

### Lemma

Let \(d\ge1\), \(r=2^d-1\), and \(n=t2^d\). Then for every \(1\le s\le d\),
\[
f(n,r,s)\le \frac{2^s}{2^d}n=\frac{2^s}{r+1}n.
\]

### Proof

Index \(2^d\) equal vertex classes
\[
V_x,\qquad x\in\mathbb F_2^d,
\]
each of order \(t\).

Use the \(2^d-1\) nonzero vectors of \(\mathbb F_2^d\) as the colours. For \(x\ne y\), colour every edge between \(V_x\) and \(V_y\) by
\[
x+y\in\mathbb F_2^d\setminus\{0\}.
\]
Choose one fixed nonzero vector \(v_0\), and colour all edges inside each \(V_x\) by \(v_0\).

Now fix a set \(C\) of at most \(s\) colours and put
\[
H=\operatorname{span}_{\mathbb F_2}(C).
\]
Consider a path using only colours from \(C\). At a cross-edge of colour \(v\in C\), the cluster index changes from \(x\) to \(x+v\); at an edge inside one cluster, it does not change. Hence all cluster indices met by such a path lie in a single affine coset
\[
x+H.
\]
Since
\[
|H|\le 2^{|C|}\le 2^s,
\]
each component of \(G_C\) meets at most \(2^s\) vertex classes and therefore has at most
\[
2^s t=\frac{2^s}{2^d}n
\]
vertices. This holds for every \(C\) with \(|C|\le s\), proving the lemma. \(\square\)

All \(r=2^d-1\) colours occur, so the construction works even if “\(r\)-colouring” is required to be surjective.

# Contradiction to the conjecture

The endpoint \(s=1\) already suffices. For \(r=2^d-1\) and every \(n=t2^d\),
\[
f(n,r,1)\le \frac{2}{r+1}n.
\]
Consequently,
\[
\frac{r f(n,r,1)}n<2.
\]
The conjecture, on the other hand, requires
\[
\frac{r f(n,r,1)}n=(\log r)^{1-o_r(1)},
\]
which tends to infinity as \(r\to\infty\). Since \(t\) can be arbitrarily large, the phrase “\(n\) large enough” cannot avoid this construction.

There is also a counterexample with \(s\to\infty\), so merely excluding bounded \(s\) would not repair the statement. Let
\[
r_d=2^d-1,
\qquad
s_d=\left\lfloor \frac12\log_2 d\right\rfloor .
\]
Then
\[
s_d\le \frac{\sqrt{r_d}}{\log r_d}
\]
for all sufficiently large \(d\), while
\[
2^{s_d}\le \sqrt d=O\bigl((\log r_d)^{1/2}\bigr).
\]
The lemma gives, for arbitrarily large \(n\),
\[
f(n,r_d,s_d)
 \le O\left(\frac{(\log r_d)^{1/2}}{r_d}\,n\right).
\]
But the conjectured expression is
\[
\frac{s_d^2(\log r_d)^{1-o(1)}}{r_d}\,n.
\]
Eventually \(1-o(1)\ge 3/4\), so the conjectured quantity exceeds the proved upper bound by at least a constant multiple of
\[
s_d^2(\log r_d)^{1/4}\longrightarrow\infty.
\]
Thus the contradiction persists for an admissible sequence \(s_d\to\infty\).

# More general upper bound

The same construction gives an obstruction for every \(r\), not only \(r=2^d-1\). Let
\[
m=2^{\lfloor\log_2(r+1)\rfloor}.
\]
Then \(m-1\le r\) and \(m>(r+1)/2\). Using the construction with \(m-1\) colours and leaving the remaining labels unused gives
\[
f(n,r,s)\le \min\{2^s,m\}\left\lceil\frac nm\right\rceil .
\]
If all \(r\) colours are required to occur, split some original colour classes into additional colours. Any \(s\) refined colours are contained in at most \(s\) original colour classes, so the same component bound remains valid.

In particular, for fixed \(s\) and sufficiently large \(r,n\),
\[
f(n,r,s)\le \left(\frac{2^{s+1}}{r+1}+o_n(1)\right)n.
\]

For comparison, an elementary edge-counting argument gives
\[
f(n,r,s)\ge 1+\frac{s(n-1)}r.
\]
Indeed, the union of the \(s\) largest colour classes has at least
\[
\frac{s}{r}\binom n2
\]
edges. A graph on \(n\) vertices whose components all have order at most \(M\) has at most \(n(M-1)/2\) edges, forcing
\[
M\ge 1+\frac{s(n-1)}r.
\]
Hence, for every fixed \(s\),
\[
f(n,r,s)=\Theta_s\left(\frac nr\right)
\]
in the large-\(n,r\) regime, with no factor tending like a positive power of \(\log r\).

# Scope and likely missing qualification

There is no gap in the counterexample to the literal statement. The binary construction shows that a universal logarithmic formula cannot hold below approximately the \(\log_2\log r\) scale: one necessarily has an upper bound of order \(2^s n/r\).

Given how elementary this obstruction is, the supplied catalog statement may be missing either:

- a lower condition on \(s\) above the binary-vector-space obstruction range, or
- a term such as a minimum with \(2^s\).

No assertion is made here about such a corrected conjecture.