```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For the restricted class of graphs of diameter at most two, I establish sharp order g^{1/3} for both genus-extremal cop numbers, without settling the full conjecture.",
  "would_publish": false,
  "caveats": "The unrestricted upper bound is not improved; this elementary special-case result is not claimed to be novel."
}
```

## 1. A sharp-order special case

I do not obtain a proof or counterexample to Conjecture 8. The following gives a complete genus-dependent result for a natural restricted class.

All graphs below are finite, simple, and connected. We use the usual visible-robber game, with the cops moving first and either side allowed to stay put. Write \(c(G)\) for the cop number.

Define
\[
c_2(g)=\max\{c(G):G\text{ embeds in the orientable surface of genus }g,\
\operatorname{diam}(G)\le2\},
\]
and define \(\mathrm{ec}_2(g)\) analogously for the nonorientable surface with \(g\) crosscaps. “Embeds” does not require that the specified genus be the minimum possible.

### Theorem
For every integer \(g\ge8\),
\[
\frac14 g^{1/3}\le c_2(g)\le 6+(48g)^{1/3},
\]
and
\[
\frac14 g^{1/3}\le \mathrm{ec}_2(g)\le 6+(24g)^{1/3}.
\]
Consequently,
\[
c_2(g)=\Theta(g^{1/3}),
\qquad
\mathrm{ec}_2(g)=\Theta(g^{1/3}).
\]

Thus, within diameter two, the extremal exponent is \(1/3\), strictly smaller than the conjectured unrestricted exponent \(1/2\).

## 2. Upper bound

We first give two elementary cop strategies.

### Lemma 1
If \(G\) has \(n\ge2\) vertices and diameter at most two, then
\[
c(G)\le \delta(G)
\qquad\text{and}\qquad
c(G)\le 2\sqrt n.
\]

#### Proof of the minimum-degree bound

Choose a vertex \(v\) of minimum degree. The open neighborhood \(N(v)\) is a dominating set:

- \(v\) has a neighbor in \(N(v)\);
- vertices of \(N(v)\) are occupied if cops are placed there;
- every other vertex is at distance two from \(v\), hence adjacent to a vertex of \(N(v)\).

Placing one cop at each vertex of \(N(v)\) therefore guarantees capture on the first cops’ move.

#### Proof of the square-root bound

Put
\[
t=\lceil\sqrt n\rceil.
\]
Construct a set of stationary-cop positions greedily. Initially let \(R=V(G)\). While some \(v\in R\) satisfies
\[
|N[v]\cap R|\ge t,
\]
select \(v\) as a stationary-cop position and replace \(R\) by \(R\setminus N[v]\).

If \(r\) positions have been selected, then
\[
r\le \frac nt,
\]
because each selection removes at least \(t\) previously unremoved vertices. At termination,
\[
|N[v]\cap R|\le t-1\qquad(v\in R).
\]
Place the \(r\) stationary cops at the selected vertices, and use another \(t-1\) mobile cops.

A robber starting outside \(R\) is captured on the first cops’ move. Otherwise, let \(v\in R\) be the robber’s starting vertex. Assign distinct mobile cops to the vertices of
\[
T=N[v]\cap R.
\]
There are at most \(t-1\) targets. Since \(G\) has diameter at most two, each assigned cop can reach its target within two cops’ moves.

After the first robber move:

- if the robber has left \(R\), a stationary cop captures on the next move;
- if the robber remains in \(R\), its position lies in \(T\), all of which is occupied on the second cops’ move.

Thus these cops guarantee capture. Their number is at most
\[
r+t-1\le \frac nt+t-1\le 2\sqrt n.
\]
This proves the lemma. \(\square\)

### Combining the strategies with Euler’s inequality

Let \(G\) embed in a surface of Euler genus \(h\): thus \(h=2g\) for an orientable surface of genus \(g\), and \(h=g\) for a nonorientable surface with \(g\) crosscaps.

For a simple graph with \(n\ge3\) vertices and \(m\) edges, Euler’s inequality gives
\[
2m\le 6n-12+6h.
\]
Write \(k=c(G)\). If \(k\le6\), the desired bound is immediate. Suppose \(k>6\). Lemma 1 yields
\[
\delta(G)\ge k,
\qquad
n\ge \frac{k^2}{4}.
\]
Consequently,
\[
(k-6)n
\le (\delta(G)-6)n
\le 2m-6n
\le 6h-12
\le 6h.
\]
It follows that
\[
(k-6)k^2\le24h.
\]
Since \(k>6\),
\[
(k-6)^3\le (k-6)k^2\le24h,
\]
and therefore
\[
c(G)\le6+(24h)^{1/3}.
\]
Graphs with at most two vertices need only one cop, so no exceptional small graph remains.

Substituting \(h=2g\) and \(h=g\) proves the two upper bounds.

## 3. Matching lower bounds

We construct diameter-two graphs with cop number proportional to \(q\) and both surface genera \(O(q^3)\).

### Lemma 2
If \(G\) contains no cycle of length four, then
\[
c(G)\ge \left\lceil\frac{\delta(G)}2\right\rceil.
\]

#### Proof

Fix an integer \(k\) such that \(2k<\delta(G)\).

For distinct vertices \(v,x\), the absence of a four-cycle implies
\[
|N(v)\cap N(x)|\le1.
\]
Thus a cop at \(x\ne v\) dominates at most two vertices of \(N(v)\): possibly \(x\) itself, and at most one common neighbor of \(x\) and \(v\). The \(k\) cops together therefore dominate at most \(2k\) vertices of \(N(v)\).

Initially choose any vertex \(v\) not occupied by a cop. Such a vertex exists because
\[
n\ge\delta(G)+1>2k+1.
\]
Since \(|N(v)|>2k\), some neighbor of \(v\) is outside all the cops’ closed neighborhoods. The robber starts there.

Maintain the invariant that, immediately after each robber move, the robber is outside every cop’s closed neighborhood. On the next cops’ move, no cop can reach the robber. At the resulting position, each cop dominates at most two neighbors of the robber, so an undominated neighbor remains available. Moving there restores the invariant.

Hence \(k\) cops cannot win. This holds for every integer \(k<\delta(G)/2\), proving the lemma. \(\square\)

### The finite-field construction

Let \(q=2^r\), where \(r\ge1\). Define \(X_q\) as follows:

- its vertices are the one-dimensional subspaces of \(\mathbb F_q^3\);
- distinct vertices \([u]\) and \([v]\) are adjacent exactly when
  \[
  u_1v_1+u_2v_2+u_3v_3=0.
  \]

This is well-defined under rescaling representatives. The bilinear form is nondegenerate, including in characteristic two.

The graph has
\[
n=q^2+q+1
\]
vertices and the following properties.

**Degree.** For nonzero \(u\), its orthogonal complement is a two-dimensional subspace, containing \(q+1\) one-dimensional subspaces. Removing \([u]\) itself if necessary gives
\[
q\le \deg([u])\le q+1.
\]

**No four-cycles.** For distinct projective points \([u]\) and \([v]\), the intersection
\[
u^\perp\cap v^\perp
\]
is one-dimensional. Thus two distinct vertices have at most one common neighbor, excluding four-cycles.

**Diameter at most two.** If \([u]\) and \([v]\) are nonadjacent, the unique projective point in \(u^\perp\cap v^\perp\) is distinct from both: equality with either would imply \(u\cdot v=0\). It is therefore a common neighbor.

Lemma 2 now gives
\[
c(X_q)\ge \frac q2.
\]

### Bounding the required genera

We use a basic embedding observation. If a connected graph has \(n\) vertices, \(m\) edges, and cycle rank
\[
\beta=m-n+1,
\]
then it has an orientable embedding of genus at most \(\beta/2\), and a nonorientable embedding with at most \(\beta+1\) crosscaps.

Indeed, give the graph an orientable ribbon neighborhood and cap all its boundary components by disks. If there are \(b\ge1\) boundary components, the resulting orientable genus \(a\) satisfies
\[
2-2a=n-m+b,
\]
so
\[
2a=\beta+1-b\le\beta.
\]
Adding a crosscap in a disk disjoint from the graph gives a nonorientable embedding with \(2a+1\le\beta+1\) crosscaps.

For \(X_q\),
\[
m\le \frac{(q+1)(q^2+q+1)}2,
\]
and hence
\[
\begin{aligned}
\beta
&=m-n+1\\
&\le \frac{(q-1)(q^2+q+1)}2+1\\
&=\frac{q^3+1}{2}.
\end{aligned}
\]
Therefore \(X_q\) embeds in an orientable surface of genus at most
\[
\frac{q^3+1}{4}
\]
and a nonorientable surface with at most
\[
\frac{q^3+3}{2}
\]
crosscaps. For \(q\ge2\), both quantities are at most \(q^3\).

Now let \(g\ge8\), and choose the largest power of two \(q\) satisfying \(q^3\le g\). Then
\[
q\le g^{1/3}<2q.
\]
The graph \(X_q\) is admissible for both restricted extremal functions, and
\[
c(X_q)\ge\frac q2>\frac14g^{1/3}.
\]
This proves both lower bounds and completes the theorem. \(\square\)

## 4. What remains unresolved

The decisive inequality in the upper bound is
\[
c(G)\le\delta(G),
\]
which here follows from diameter two. It converts Euler’s inequality into
\[
g=\Omega\!\left(c(G)^3\right).
\]

That inequality is unavailable for general graphs. In particular, adding a leaf makes the minimum degree one without reducing the cop number of the original graph: the original graph is a retract of the enlarged graph. Thus minimum degree cannot control the unrestricted problem.

The two-round strategy also depends essentially on every mobile cop being within distance two of every target. Neither argument supplies a replacement for graphs of arbitrary diameter.

Accordingly, the principal gap in Conjecture 8 remains untouched: proving
\[
c(g),\ \mathrm{ec}(g)\le g^{1/2+\varepsilon}
\]
for every fixed \(\varepsilon>0\) and all sufficiently large \(g\). The result above settles a restricted genus-exponent problem, but does not improve the unrestricted linear upper bound.