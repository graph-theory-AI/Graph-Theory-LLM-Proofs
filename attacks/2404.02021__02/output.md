```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open: it holds for \(0<c\le 1\), and two broad pair-palette and binary stepping-up schemes are rigorously shown incapable of producing the required bounds for \(c>1\).",
  "would_publish": false,
  "caveats": "No lower bound \(2^{\Omega(n^c)}\) with fixed \(c>1\) is obtained, and the construction barriers do not apply to arbitrary 3-graphs."
}
```

# 1. Statement and reformulation

Write \(r_3(s,n)=r(K_s^{(3)},K_n^{(3)})\). Equivalently, \(r_3(s,n)>N\) if there is a 3-graph \(G\) on \(N\) vertices satisfying
\[
\omega_3(G)<s,\qquad \alpha(G)<n,
\]
where \(\omega_3(G)\) is the largest complete 3-uniform subgraph and \(\alpha(G)\) is the largest edge-free set.

The conjecture asks whether, for every fixed \(c>0\), one can choose a fixed \(s=s(c)\) and construct such \(G\) on
\[
N=2^{\Omega_s(n^c)}
\]
vertices.

I do not resolve the range \(c>1\). I give a self-contained proof for \(c\le 1\), followed by two rigorous obstructions to natural attempts based on graph palettes and the graph-to-3-graph first-difference construction.

# 2. The conjecture for \(0<c\le 1\)

## Proposition 2.1
For all sufficiently large \(n\),
\[
r_3(4,n)\ge 2^{n/2-O(1)}.
\]
Consequently, the conjecture holds for every \(0<c\le 1\), with \(s=4\).

### Proof

Let \(T\) be a tournament on \(N\) vertices, and define a 3-graph \(G_T\) by declaring a triple to be an edge precisely when it induces a directed 3-cycle in \(T\).

First, \(G_T\) is \(K_4^{(3)}\)-free. Indeed, every tournament on four vertices has a vertex of outdegree at least two. If \(v\) beats \(x\) and \(y\), then the tournament induced by \(\{v,x,y\}\) is transitive, so this triple is not an edge of \(G_T\).

Second, a set is independent in \(G_T\) exactly when its induced tournament has no directed triangle. A tournament without a directed triangle is transitive. Thus \(\alpha(G_T)\) is the largest transitive subtournament of \(T\).

Choose \(T\) uniformly at random. For a fixed \(n\)-set, the probability that its induced tournament is transitive is
\[
\frac{n!}{2^{\binom n2}},
\]
because there are \(n!\) transitive tournaments on a labeled \(n\)-set. Therefore, the expected number of transitive \(n\)-sets is at most
\[
\binom Nn \frac{n!}{2^{\binom n2}}
\le N^n2^{-\binom n2}.
\]
Taking
\[
N=\left\lfloor 2^{(n-1)/2-1}\right\rfloor
\]
makes this expectation at most \(2^{-n}<1\). Hence there exists a tournament \(T\) with no transitive \(n\)-vertex subtournament. The corresponding \(G_T\) is \(K_4^{(3)}\)-free and has \(\alpha(G_T)<n\). ∎

The supplied source gives the stronger lower bound \(2^{\Omega(n\log n)}\) for suitable fixed forbidden 3-graphs \(H\). Since any fixed \(h\)-vertex 3-graph \(H\) is a subgraph of \(K_h^{(3)}\),
\[
r(K_h^{(3)},K_n^{(3)})\ge r(H,K_n^{(3)}),
\]
so that result also implies the case \(c=1\).

# 3. A fixed pair-palette cannot exceed exponential growth

A common construction begins with a finite coloring of pairs and determines the color of a triple solely from the colors of its three constituent pairs.

## Proposition 3.1
Fix \(q,s\ge 2\). Let
\[
\phi:\binom{[N]}2\longrightarrow [q]
\]
be a \(q\)-coloring, and let
\[
P:[q]^3\longrightarrow\{\mathrm{red},\mathrm{blue}\}.
\]
For \(i<j<k\), color \(\{i,j,k\}\) by
\[
P\bigl(\phi(ij),\phi(ik),\phi(jk)\bigr).
\]
If the resulting 3-graph has neither a red \(K_s^{(3)}\) nor a blue \(K_n^{(3)}\), then
\[
N<2q^{\,q(s+n-2)+1}.
\]
In particular, for fixed \(q,s\), this construction has \(N\le 2^{O_{q,s}(n)}\).

### Proof

We use the following standard canonical-sequence argument. Put
\[
L=\left\lfloor \log_q(N/2)\right\rfloor.
\]
There are vertices \(v_1,\dots,v_L\) and colors \(a_1,\dots,a_L\) such that
\[
\phi(v_iv_j)=a_i\qquad (i<j).
\]
To construct them, after choosing \(v_i\), retain a largest color class among its edges to the remaining vertices. The retained set loses a factor of at most \(q\) at each step. The choice of \(L\) ensures the process lasts \(L\) steps.

For a fixed color \(a\), the vertices \(v_i\) with \(a_i=a\) span a pair-monochromatic clique of color \(a\): if \(i<j\), then \(\phi(v_iv_j)=a_i=a\).

Classify a color \(a\) as red-diagonal if
\[
P(a,a,a)=\mathrm{red},
\]
and blue-diagonal otherwise. A red-diagonal color can occur among the \(a_i\) at most \(s-1\) times, since \(s\) such indices would give a red \(K_s^{(3)}\). Hence at most \(q(s-1)\) indices receive red-diagonal colors.

The remaining at least \(L-q(s-1)\) indices receive blue-diagonal colors. One blue-diagonal color therefore occurs at least
\[
\frac{L-q(s-1)}q
\]
times. The corresponding vertices form a blue complete 3-graph. As there is no blue \(K_n^{(3)}\), we must have
\[
L\le q(s-1)+q(n-1).
\]
The asserted bound on \(N\) follows from the definition of \(L\). ∎

Thus no construction using a fixed finite pair palette can prove the conjecture for \(c>1\). The tournament construction above shows that the resulting exponential bound is of the correct order for this general framework.

A growing palette may evade Proposition 3.1, but then one must control all pair-colorings of an \(n\)-set, including highly degenerate ones. No such construction is obtained here.

# 4. Obstruction to the full binary first-difference stepping-up construction

The tempting argument is to start with a graph Ramsey coloring on \(m\) coordinates and lift it to \(2^m\) vertices. The following theorem shows that every construction whose triple color depends only on the two first-difference coordinates has an unavoidable exponential loss in the blue parameter.

Let
\[
V_m=\{0,1\}^m
\]
be ordered by binary numerical order. For \(x<y\), put
\[
\delta(x,y)=\max\{i:x_i\ne y_i\}.
\]
For \(x<y<z\), the two values
\[
\delta(x,y),\qquad \delta(y,z)
\]
are distinct.

Let
\[
\Gamma:\{(i,j)\in[m]^2:i\ne j\}\longrightarrow
\{\mathrm{red},\mathrm{blue}\}
\]
be arbitrary, and define
\[
\chi(x,y,z)=\Gamma\bigl(\delta(x,y),\delta(y,z)\bigr)
\qquad (x<y<z).
\]

## Theorem 4.1
Fix \(S\ge3\), and let
\[
A=R^{\mathrm{graph}}_3(S-1),
\]
the diagonal three-color graph Ramsey number for \(K_{S-1}\). If \(\chi\) contains neither a red \(K_S^{(3)}\) nor a blue \(K_n^{(3)}\), then, with
\[
b=\lceil\log_2 n\rceil,
\]
we have
\[
m<R^{\mathrm{graph}}(A,b)
 \le \binom{A+b-2}{A-1}.
\]
Consequently,
\[
|V_m|=2^m
 \le 2^{O_S((\log n)^{A-1})}.
\]

In particular, no full binary first-difference construction of this form can produce \(2^{\Omega(n^c)}\) vertices for any fixed \(c>0\).

### Proof

For each unordered coordinate pair \(i<j\), record its signature
\[
\sigma(i,j)=\bigl(\Gamma(i,j),\Gamma(j,i)\bigr).
\]
Call the signature \((\mathrm{blue},\mathrm{blue})\) safe. The other three signatures are unsafe.

### Unsafe monochromatic coordinate sets give red combs

Suppose \(d_1>\cdots>d_{S-1}\) are coordinates such that every pair has the same unsafe signature. At least one of the two orientations in this signature is red.

Inside the binary cube on these coordinates, construct a comb with \(S\) leaves. At the branching node with coordinate \(d_i\), put one leaf in one child and continue the rest of the comb in the other child. Choose the continuation side so that whenever a triple first separates at \(d_i\), its ordered pair of \(\delta\)-values uses the red orientation of the common signature.

For any three leaves, there is a unique shallowest comb node \(d_i\) at which one leaf separates from the other two. The other two separate later at some \(d_j<d_i\). Thus the two consecutive \(\delta\)-values are either
\[
(d_i,d_j)\quad\text{or}\quad(d_j,d_i),
\]
with the orientation determined by the chosen continuation side. Every triple is therefore red. This gives a red \(K_S^{(3)}\), a contradiction.

Hence no \(S-1\) coordinates can have all pair signatures equal to the same unsafe signature.

### The safe-coordinate graph

Define a graph \(J\) on \([m]\) by
\[
ij\in E(J)\quad\Longleftrightarrow\quad \sigma(i,j)
=(\mathrm{blue},\mathrm{blue}).
\]

If \(J\) had an independent set of size \(A\), the pairs of this set would be colored by the three unsafe signatures. By the definition of \(A\), there would be \(S-1\) coordinates with a common unsafe signature, contradicting the preceding paragraph. Thus
\[
\alpha(J)<A.
\]

If \(J\) had a clique \(D\) of size \(b\), consider the complete binary subcube obtained by varying precisely the coordinates in \(D\). It has \(2^b\ge n\) vertices. For any ordered triple in this subcube, its two distinct \(\delta\)-coordinates lie in \(D\), and both possible orientations of that coordinate pair are blue. Hence the entire subcube is blue, contradicting the absence of a blue \(K_n^{(3)}\). Therefore
\[
\omega(J)<b.
\]

A graph on \(m\) vertices with \(\alpha(J)<A\) and \(\omega(J)<b\) can exist only when
\[
m<R^{\mathrm{graph}}(A,b).
\]
The standard graph Ramsey recurrence gives
\[
R^{\mathrm{graph}}(A,b)\le \binom{A+b-2}{A-1},
\]
which proves the theorem. ∎

## Corollary 4.2: the naive graph stepping-up loss

In the usual symmetric lift,
\[
\Gamma(i,j)=\phi(\{i,j\})
\]
for a red-blue graph coloring \(\phi\). There is then only one unsafe signature, namely \((\mathrm{red},\mathrm{red})\). The preceding proof sharpens to
\[
m<R^{\mathrm{graph}}\bigl(S-1,\lceil\log_2 n\rceil\bigr),
\]
and hence
\[
2^m\le 2^{O_S((\log n)^{S-2})}.
\]

This explains why inserting a strong off-diagonal graph Ramsey coloring into the obvious graph-to-3-graph stepping-up construction does not prove the conjecture: a graph blue clique of size \(b\) becomes a blue 3-uniform clique of size \(2^b\), so the graph parameter is only \(b\asymp\log n\).

# 5. Remaining gap

The arguments establish only the already-accessible range \(c\le1\). They also rule out two substantial but restricted approaches:

1. Any fixed finite pair-palette construction has independence number \(\Omega(\log N)\), so it gives at most \(N=2^{O(n)}\).
2. Any coloring of the full binary cube depending only on the ordered pair of first-difference coordinates has
   \[
   N\le 2^{(\log n)^{O_S(1)}}
   \]
   when the red clique number is fixed.

Neither statement is an upper bound for general \(r_3(s,n)\). A successful proof for \(c>1\) must use genuinely 3-uniform global dependencies, a growing palette with strong entropy control, or a stepping-up mechanism not captured by first differences on the full binary cube. No such construction, and no counterexample to the conjecture, is provided here.