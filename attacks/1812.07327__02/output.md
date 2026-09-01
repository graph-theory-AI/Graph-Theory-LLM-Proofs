```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The converse holds whenever unbounded expansion has uniformly almost-regular witnesses; quantitatively, an average-d graph of maximum degree O(d) has a 1-shallow minor with Hall ratio Omega(sqrt(d)).",
  "would_publish": false,
  "caveats": "Arbitrarily irregular dense shallow minors are not covered, so this neither proves nor disproves Problem 8."
}
```

# 1. Statement and notation

Write \(H\preccurlyeq_r G\) when \(H\) is an \(r\)-shallow minor of \(G\). Thus the vertices of \(H\) are represented by pairwise disjoint connected branch sets of radius at most \(r\) in a subgraph of \(G\).

The Hall ratio is
\[
 \rho(G)=\max_{\varnothing\neq X\subseteq V(G)}
          \frac{|X|}{\alpha(G[X])}.
\]
This agrees with the definition using all subgraphs, since replacing a subgraph by the induced subgraph on the same vertex set cannot increase its independence number.

The forward implication is immediate. If the densities of all \(r\)-shallow minors are bounded by \(b_r\), then every subgraph of such a shallow minor has average degree at most \(2b_r\), and hence is \(\lfloor 2b_r\rfloor\)-degenerate. Therefore
\[
 \rho(H)\leq \chi(H)\leq \lfloor 2b_r\rfloor+1.
\]

I do not prove the converse. I prove below a finite result which establishes it whenever the dense shallow minors witnessing failure of bounded expansion can be chosen almost regular.

# 2. Composition of shallow minors

We use the standard composition bound
\[
 J\preccurlyeq_s H,\qquad H\preccurlyeq_r G
 \quad\Longrightarrow\quad
 J\preccurlyeq_{r+s(2r+1)}G. \tag{2.1}
\]

Indeed, let \(B_x\) be the radius-\(r\) branch set representing \(x\in V(H)\), with center \(c_x\). An edge \(xy\in E(H)\) can be traversed between \(c_x\) and \(c_y\) in at most \(2r+1\) edges of \(G\). Replacing a radius-\(s\) branch set in \(H\) by the union of its \(B_x\)'s therefore gives radius at most
\[
 r+s(2r+1).
\]
In particular, composing with a \(1\)-shallow minor costs depth at most
\[
 3r+1. \tag{2.2}
\]

# 3. A probabilistic matching-contraction lemma

The main partial result is the following.

## Lemma 3.1

For every \(L\geq 1\), there is \(d_0(L)\) such that the following holds. Let \(B\) be a simple bipartite graph satisfying
\[
 d\leq \deg_B(v)\leq Ld
 \qquad\text{for every }v\in V(B),
 \tag{3.1}
\]
where \(d\geq d_0(L)\). Then \(B\) has a \(1\)-shallow minor \(Q\) satisfying
\[
 \rho(Q)\geq \frac{\sqrt d}{64L^2}. \tag{3.2}
\]

### Proof

Let the two parts of \(B\) be \(A\) and \(C\), with
\[
 |A|=a,\qquad |C|=b.
\]
Counting edges using (3.1) gives
\[
 a\leq Lb,\qquad b\leq La. \tag{3.3}
\]

Set
\[
 \theta=\frac{1}{16L^3},\qquad k=\lfloor \theta a\rfloor.
\]
For sufficiently large \(d\), (3.3) and \(b\geq d\) ensure that \(k\geq \theta a/2\).

Choose uniformly a \(k\)-element set \(X\subseteq A\). Independently for each \(x\in X\), choose a uniformly random neighbor \(y_x\in C\). This gives \(k\) chosen edges \(xy_x\), with distinct \(A\)-endpoints but not necessarily distinct \(C\)-endpoints.

Let \(Z\) count unordered pairs \(x,x'\in X\) for which \(y_x=y_{x'}\). Since every degree is at least \(d\),
\[
\begin{aligned}
 \mathbb E Z
 &\leq
 \frac{k(k-1)}{a(a-1)}
 \frac{1}{d^2}
 \sum_{y\in C}\binom{\deg(y)}2  \\
 &\leq
 \frac{k^2}{a^2}\frac{b(Ld)^2}{2d^2}
 \leq \frac{L^3k^2}{2a}
 \leq \frac{k}{32}.
\end{aligned}
\]
Consequently,
\[
 \Pr(Z>k/4)\leq \frac18. \tag{3.4}
\]

We next bound the size of an induced matching among the chosen edges. Fix \(S\subseteq A\), \(|S|=s\). The probability that \(S\subseteq X\) is at most
\[
 \left(\frac{k}{a}\right)^s.
\]
For \(x\in S\), define its private neighbors relative to \(S\) by
\[
 P_x(S)=N(x)\setminus
 \bigcup_{x'\in S\setminus\{x\}}N(x').
\]
The chosen edges \(\{xy_x:x\in S\}\) form an induced matching only if
\[
 y_x\in P_x(S)\qquad\text{for every }x\in S.
\]
The sets \(P_x(S)\) are pairwise disjoint, and hence
\[
 \sum_{x\in S}|P_x(S)|\leq b\leq La.
\]
By the arithmetic-geometric mean inequality, conditional on \(S\subseteq X\),
\[
 \Pr\bigl(\{xy_x:x\in S\}\text{ is induced}\bigr)
 \leq
 \prod_{x\in S}\frac{|P_x(S)|}{d}
 \leq
 \left(\frac{La}{sd}\right)^s.
\]
Taking a union bound over all \(s\)-element sets \(S\subseteq A\) gives
\[
 \Pr(\text{there is a chosen induced matching of size }s)
 \leq
 \left(\frac{eLka}{s^2d}\right)^s. \tag{3.5}
\]

Choose
\[
 s=\left\lceil 2\sqrt{\frac{eLka}{d}}\right\rceil.
\]
Then the right side of (3.5) is at most \(4^{-s}\leq 1/4\). Together with (3.4), there is therefore an outcome such that:

1. \(Z\leq k/4\);
2. the chosen edges contain no induced matching of size \(s\).

For each repeated \(C\)-endpoint, retain just one of its chosen edges. The resulting set \(M\) is a matching. If \(r_y\) chosen edges ended at \(y\), then
\[
 r_y-1\leq \binom{r_y}{2},
\]
so the number of discarded edges is at most \(Z\). Thus
\[
 |M|\geq \frac{3k}{4}. \tag{3.6}
\]

Contract every edge of \(M\), and retain between two contracted vertices an edge exactly when \(B\) has an edge joining the corresponding matching edges. Call the resulting graph \(Q\). This is a \(1\)-shallow minor of \(B\). An independent set in \(Q\) is exactly an induced submatching of \(M\). Therefore
\[
 \alpha(Q)<s.
\]
For sufficiently large \(d\), the floor and ceiling errors give
\[
 s\leq 3a\sqrt{\frac{eL\theta}{d}},
 \qquad k\geq \frac{\theta a}{2}.
\]
Using (3.6),
\[
 \rho(Q)\geq\frac{|M|}{\alpha(Q)}
 >\frac{3k}{4s}
 \geq \frac18\sqrt{\frac{\theta d}{eL}}
 =\frac{\sqrt d}{32\sqrt e\,L^2}
 \geq\frac{\sqrt d}{64L^2}.
\]
This proves the lemma. \(\square\)

# 4. Almost-regular graphs

Lemma 3.1 implies a convenient non-bipartite statement.

## Theorem 4.1

For every \(C\geq1\), there are constants \(c_C>0\) and \(D_0(C)\) such that every graph \(G\) with
\[
 \overline d(G)=D\geq D_0(C),
 \qquad
 \Delta(G)\leq CD,
 \tag{4.1}
\]
has a \(1\)-shallow minor \(Q\) with
\[
 \rho(Q)\geq c_C\sqrt D. \tag{4.2}
\]

### Proof

Take a maximum cut of \(G\), and let \(B_0\) be the resulting bipartite spanning subgraph. If \(n=|V(G)|\), then
\[
 |E(B_0)|\geq \frac12|E(G)|=\frac{Dn}{4}.
\]

Repeatedly delete from \(B_0\) every vertex whose current degree is less than \(D/8\). This process cannot delete every vertex: if it did, summing the degree of each vertex at its deletion time would give
\[
 |E(B_0)|<\frac{Dn}{8},
\]
a contradiction. We obtain a nonempty bipartite subgraph \(B\) such that
\[
 \frac D8\leq \deg_B(v)\leq CD
 \qquad\text{for every }v\in V(B).
\]
Apply Lemma 3.1 with \(d=D/8\) and \(L=8C\). This yields (4.2), with an explicit but inessential constant such as
\[
 c_C=\frac{1}{64(8C)^2\sqrt 8}.
\]
\(\square\)

Thus regular graphs, bounded-ratio almost-regular graphs, and graphs having dense almost-regular subgraphs cannot furnish counterexamples.

# 5. Consequence for Problem 8

## Corollary 5.1

Suppose that for some fixed \(r\) and \(C\), there are graphs \(G_i\in\mathcal C\) and subgraphs
\[
 H_i\subseteq J_i,\qquad J_i\preccurlyeq_r G_i,
\]
such that
\[
 D_i=\overline d(H_i)\longrightarrow\infty,
 \qquad
 \Delta(H_i)\leq C D_i.
 \tag{5.1}
\]
Then the Hall ratios of the \((3r+1)\)-shallow minors of members of \(\mathcal C\) are unbounded.

### Proof

By Theorem 4.1, each \(H_i\) has a \(1\)-shallow minor \(Q_i\) with
\[
 \rho(Q_i)\geq c_C\sqrt{D_i}\longrightarrow\infty.
\]
Since a subgraph of an \(r\)-shallow minor is still an \(r\)-shallow minor,
\[
 H_i\preccurlyeq_r G_i.
\]
Composition (2.2) then gives
\[
 Q_i\preccurlyeq_{3r+1}G_i.
\]
Hence no value \(f_6(3r+1)\) can bound all these Hall ratios. \(\square\)

Consequently, the proposed converse is valid for every class with the following regularisability property:

> Whenever the densities of its \(r\)-shallow minors are unbounded, those shallow minors contain subgraphs of unbounded average degree whose maximum degree is at most a fixed multiple of their average degree.

Any counterexample must fail this property at the depth witnessing unbounded expansion. In particular, all its dense witnesses must become increasingly degree-irregular in a strong hereditary sense.

As a concrete sanity check, the hypercubes cannot be a counterexample. More directly than Theorem 4.1, \(Q_d\) contains the \(1\)-subdivision of \(K_d\): use the unit vectors \(e_i\) as branch vertices and \(e_i+e_j\) as the subdivision vertex for the edge \(ij\). Hence \(K_d\preccurlyeq_1Q_d\).

# 6. Further necessary conditions

Assume that the function \(f_6\) in the problem exists.

First, \(\mathcal C\) is nowhere dense: since \(\rho(K_t)=t\), no \(r\)-shallow minor can contain \(K_{f_6(r)+1}\) as a subgraph.

There is also a useful biclique restriction. The graph \(K_{t,t}\) has \(K_t\) as a \(1\)-shallow minor: contract the \(t\) edges of a perfect matching. Therefore, if \(H\preccurlyeq_r G\) with \(G\in\mathcal C\), then \(H\) cannot contain
\[
 K_{t,t},\qquad t=f_6(3r+1)+1. \tag{6.1}
\]
Indeed, otherwise composition would give
\[
 K_t\preccurlyeq_{3r+1}G,
\]
contradicting \(\rho(K_t)=t>f_6(3r+1)\).

The standard common-neighborhood count then gives the order-dependent bound
\[
 \overline d(H)
 \leq 2t+2(t-1)^{1/t}|V(H)|^{1-1/t}. \tag{6.2}
\]
For completeness, in a \(K_{t,t}\)-free graph,
\[
 \sum_{v}\binom{\deg(v)}t
 \leq (t-1)\binom{|V(H)|}{t},
\]
because every \(t\)-vertex set has at most \(t-1\) common neighbors. Convexity of \(k\mapsto\binom{k}{t}\) gives (6.2).

Bound (6.2) is far weaker than bounded expansion, but it shows that a counterexample must simultaneously avoid large fixed bicliques at every relevant shallow depth.

# 7. Remaining gap

The unresolved step is a degree-regularisation theorem strong enough to apply Theorem 4.1 to arbitrary dense shallow minors. From a graph of average degree \(D\), one can always extract a subgraph of minimum degree at least \(D/2\), but this gives no upper bound on its maximum degree. The probabilistic matching argument above uses an upper-to-lower degree ratio bounded independently of \(D\).

I have not proved that the assumed Hall-ratio bounds themselves force such a regularisation, nor have I constructed a sequence of increasingly irregular graphs evading all bounded-depth matching contractions. Thus:

- there is no complete proof of the converse here;
- there is no counterexample;
- the almost-regular case, including regular and bounded-irregularity witnesses at arbitrary fixed shallow depth, is covered rigorously.