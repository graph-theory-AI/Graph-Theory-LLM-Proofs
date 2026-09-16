```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For digraphs of any fixed bounded independence number, I prove that minimum outdegree 2d+(2+o(1))sqrt(d log d) suffices, with asymptotically optimal leading coefficient.",
  "would_publish": false,
  "caveats": "This elementary special-case bound is not claimed to be new; it does not settle F(2,2) for unrestricted digraphs."
}
```

## 1. Interpretation and partial result

I use finite loopless digraphs without parallel arcs; opposite arcs are allowed. Both partition classes must be nonempty.

The source sentence evidently has a transcription error: the intended hypothesis is minimum outdegree at least **\(f(d)\)**, not merely \(d\). The literal version is false, for example for the bidirected complete graph on \(d+1\) vertices. I address the intended threshold question.

Write \(\alpha(D)\) for the independence number of the underlying undirected graph: an independent set contains no arc in either direction between its vertices.

The following gives a special case with **no restriction on the order or maximum indegree**.

### Theorem
Let \(a,d,r\) be positive integers with \(r\ge 2d\). Suppose
\[
a(2r+2d+1)\sum_{j=0}^{d-1}\binom rj+1<2^r. \tag{1}
\]
Then every digraph \(D\) satisfying
\[
\alpha(D)\le a,\qquad \delta^+(D)\ge r
\]
has a partition into nonempty sets \(A,B\) such that
\[
\delta^+(D[A])\ge d,\qquad \delta^+(D[B])\ge d.
\]

Consequently, if \(F_a(d)\) denotes the threshold restricted to digraphs with independence number at most \(a\), then, for every fixed \(a\),
\[
\boxed{\quad
2d+1\le F_a(d)
\le 2d+(2+o(1))\sqrt{d\log d}.
\quad} \tag{2}
\]
Here \(\log\) is natural and the asymptotic statement is as \(d\to\infty\).

In particular, this applies to all semicomplete digraphs, including tournaments, since these have independence number one. As a concrete consequence of (1),
\[
F_1(2)\le 8.
\]

## 2. Controlling the number of low-outdegree vertices

The structural ingredient is elementary.

### Lemma
If \(\alpha(D)\le a\), then for every integer \(t\ge0\),
\[
\bigl|\{v:d_D^+(v)\le t\}\bigr|\le a(2t+1). \tag{3}
\]

### Proof
Let \(S=\{v:d_D^+(v)\le t\}\), and let \(H\) be the underlying undirected graph of \(D[S]\).

For every \(W\subseteq S\), the digraph \(D[W]\) has at most \(t|W|\) arcs. Therefore \(H[W]\) has at most \(t|W|\) edges and has a vertex of degree at most \(2t\).

Repeatedly select such a vertex for an independent set and delete it together with its neighbors. Each selection deletes at most \(2t+1\) vertices. Thus
\[
\alpha(D)\ge\alpha(H)\ge \frac{|S|}{2t+1},
\]
which proves (3). \(\square\)

The important feature is that this bounds the number of low-outdegree vertices independently of \(|V(D)|\).

## 3. Proof of the splitting theorem

Color every vertex independently red or blue, each with probability \(1/2\).

For a vertex \(v\), let \(E_v\) be the event that \(v\) has fewer than \(d\) outneighbors of its own color. Conditional on the color of \(v\), its outneighbors still have independent fair colors. Hence, writing \(k=d_D^+(v)\),
\[
\Pr(E_v)=p_k^{(d)},\qquad
p_k^{(s)}:=2^{-k}\sum_{j=0}^{s-1}\binom kj. \tag{4}
\]

We will bound the sum of these failure probabilities using (3).

### A binomial-tail calculation

Pascal’s identity gives
\[
p_t^{(s)}-p_{t+1}^{(s)}
=2^{-t-1}\binom{t}{s-1}. \tag{5}
\]
Also \(p_t^{(s)}\to0\) as \(t\to\infty\), with \(s\) fixed.

Put
\[
N_t=\bigl|\{v:d_D^+(v)\le t\}\bigr|.
\]
Since all outdegrees are at least \(r\), telescoping (5) yields
\[
\begin{aligned}
\sum_v\Pr(E_v)
&=\sum_{t=r}^{\infty}
N_t\bigl(p_t^{(d)}-p_{t+1}^{(d)}\bigr)\\
&\le
a\sum_{t=r}^{\infty}
(2t+1)2^{-t-1}\binom{t}{d-1}. \tag{6}
\end{aligned}
\]

Now use
\[
(2t+1)\binom{t}{d-1}
=(2d-1)\binom{t}{d-1}
  +2d\binom{t}{d}. \tag{7}
\]
Applying (5) to the two resulting sums gives
\[
\sum_v\Pr(E_v)
\le a\bigl((2d-1)p_r^{(d)}+2d\,p_r^{(d+1)}\bigr). \tag{8}
\]

Furthermore,
\[
\begin{aligned}
p_r^{(d+1)}
&=p_r^{(d)}+2^{-r}\binom rd\\
&\le p_r^{(d)}
\left(1+\frac{\binom rd}{\binom r{d-1}}\right)
=\frac{r+1}{d}\,p_r^{(d)}.
\end{aligned}
\]
Thus
\[
\sum_v\Pr(E_v)
\le a(2r+2d+1)p_r^{(d)}. \tag{9}
\]

### Ensuring both classes are nonempty

This needs explicit attention: avoiding all \(E_v\) does not exclude a monochromatic coloring.

Let \(M\) be the event that the coloring is monochromatic. If \(n=|V(D)|\), then
\[
\Pr(M)=2^{1-n}\le2^{-r},
\]
because \(n\ge r+1\).

By the union bound,
\[
\Pr\left(M\cup\bigcup_vE_v\right)
\le
a(2r+2d+1)2^{-r}
\sum_{j=0}^{d-1}\binom rj
+2^{-r}.
\]
Condition (1) makes this strictly less than one. Therefore some coloring has both colors present and gives every vertex at least \(d\) outneighbors of its own color. Its color classes are the required partition. \(\square\)

## 4. Quantitative consequences

### Existence for every fixed independence bound

For fixed \(a,d\), the left side of (1), apart from the constant term, grows only polynomially in \(r\), whereas \(2^r\) grows exponentially. Thus \(F_a(d)\) is finite.

For \(a=1,d=2,r=8\), condition (1) reads
\[
(16+4+1)(1+8)+1=190<256.
\]
Hence every semicomplete digraph of minimum outdegree at least eight admits the desired partition with internal minimum outdegree two.

### Asymptotically optimal leading coefficient

For \(X\sim\operatorname{Bin}(r,1/2)\), the standard exponential-moment bound gives
\[
p_r^{(d)}
=\Pr(X\le d-1)
\le
\exp\left(-\frac{(r-2d+2)^2}{2r}\right). \tag{10}
\]
For completeness, this follows by applying exponential Markov to \(r/2-X\), using
\(\cosh x\le e^{x^2/2}\), and optimizing the parameter.

Fix \(a\) and \(\varepsilon>0\), and choose
\[
r=\left\lceil
2d+(2+\varepsilon)\sqrt{d\log d}
\right\rceil.
\]
Then
\[
\frac{(r-2d+2)^2}{2r}
=
\left(1+\varepsilon+\frac{\varepsilon^2}{4}+o(1)\right)\log d.
\]
Consequently,
\[
a(2r+2d+1)p_r^{(d)}
=O_a(d)\,
d^{-1-\varepsilon-\varepsilon^2/4+o(1)}
\longrightarrow0.
\]
Also \(2^{-r}\to0\), so the theorem applies for all sufficiently large \(d\). This proves the upper bound in (2).

For the lower bound, take the bidirected complete graph on \(2d+1\) vertices. Its minimum outdegree is \(2d\) and its independence number is one. Each part having internal minimum outdegree at least \(d\) would need at least \(d+1\) vertices, which is impossible. Thus
\[
F_a(d)\ge2d+1
\]
for every \(a\ge1\).

The same lower bound holds even within tournaments: the cyclic regular tournament on \(4d+1\) vertices has minimum outdegree \(2d\), whereas a subtournament of minimum outdegree \(d\) needs at least \(2d+1\) vertices.

Thus the coefficient \(2\) multiplying \(d\) is optimal. No optimality is claimed for the square-root error term.

## 5. What remains unresolved

The dependence on \(\alpha(D)\) is essential to this argument. Without it, there can be arbitrarily many vertices of the same fixed outdegree, and the sum in (9) has no graph-independent bound.

For example, take the bidirected complete bipartite graph with sides of sizes \(r\) and \(N\), where \(N\ge r\). It has minimum outdegree \(r\), but \(N\) vertices have outdegree exactly \(r\). For fixed \(r,d\),
\[
\sum_v\Pr(E_v)\ge Np_r^{(d)}\longrightarrow\infty.
\]
Nevertheless, when \(r,N\ge2d\), this graph is easily splittable: divide each original bipartition class into two sets of size at least \(d\), and pair the corresponding sets.

So the failure here is a limitation of the counting and union-bound method, not a counterexample to the conjecture. The argument supplies no universal bound for \(F(2,2)\), and the unrestricted threshold question is not settled by this work.