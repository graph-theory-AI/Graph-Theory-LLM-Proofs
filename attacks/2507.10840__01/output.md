```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but near-threshold covers are shown to be approximate plane Hamilton-path decompositions, and precise weighted and matching-based sufficient criteria are derived.",
  "would_publish": false,
  "caveats": "No point-set family satisfying a strict linear lower bound above n/2 is constructed; the reductions are mainly structural."
}
```

# 1. Statement and notation

Let \(A\) be a set of \(n\) points in general position, and let
\[
\pi(A)
\]
denote the minimum number of crossing-free geometric paths whose union contains every edge of \(K_n[A]\). Paths are simple graph-theoretic paths; different covering paths may share edges.

Every path has at most \(n-1\) edges, so
\[
\pi(A)\geq
\left\lceil \frac{\binom n2}{n-1}\right\rceil
=\left\lceil\frac n2\right\rceil.
\]
The problem asks whether this lower bound can be improved by a fixed positive linear proportion for infinitely many \(n\).

I do not resolve that question. I give below:

1. an exact decomposition for convex point sets;
2. a quantitative description of every cover with \(n/2+o(n)\) paths;
3. weighted and matching-based sufficient conditions for an affirmative answer;
4. an obstruction showing why separate degree and crossing-matching constraints cannot by themselves beat \(n/2\);
5. an exact finite optimization formulation suitable for searching for candidates.

# 2. Exact convex-position calibration

Although only the general-position problem is at issue, it is useful to record an exact construction showing how tightly the trivial lower bound can be attained.

## Proposition 2.1

If \(A\) consists of \(n\) points in convex position, then
\[
\pi(A)=\left\lceil\frac n2\right\rceil.
\]
For even \(n\), the edges partition into \(n/2\) crossing-free Hamilton paths.

### Proof

Label the vertices \(v_0,\dots,v_{n-1}\) in cyclic order, with indices modulo \(n\).

First let \(n=2m\). For \(0\leq i<m\), define
\[
P_i=
\bigl(
v_i,v_{i+1},v_{i-1},v_{i+2},v_{i-2},\ldots,
v_{i+(m-1)},v_{i-(m-1)},v_{i+m}
\bigr).
\]

The edges of \(P_i\) are
\[
A_r(i)=\{v_{i-r+1},v_{i+r}\},\qquad 1\leq r\leq m,
\]
and
\[
B_r(i)=\{v_{i+r},v_{i-r}\},\qquad 1\leq r<m.
\]

Cut the cyclic order at \(v_{i+m}\), and represent the vertices by signed indices
\[
-m,-m+1,\ldots,-1,0,1,\ldots,m-1.
\]
The intervals spanned by the successive chords are
\[
[0,1]\subset[-1,1]\subset[-1,2]\subset[-2,2]
 \subset\cdots\subset[-m+1,m].
\]
Thus any two nonadjacent edges are nested rather than alternating around the convex hull. Consequently, they do not cross, and \(P_i\) is a plane Hamilton path.

It remains to prove that these paths partition the edges. Every \(A_r(i)\) has endpoint-index sum
\[
2i+1\pmod {2m},
\]
while every \(B_r(i)\) has endpoint-index sum
\[
2i\pmod {2m}.
\]
For an odd residue \(s\), there are exactly \(m\) unordered non-loop pairs
\(\{a,b\}\) with \(a+b=s\pmod {2m}\). For an even residue there are exactly
\(m-1\), because the involution \(a\mapsto s-a\) has two fixed points, which correspond to loops. Hence \(P_i\) contains exactly all edges whose endpoint sum is \(2i\) or \(2i+1\). As \(i=0,\dots,m-1\), these sums partition all residues modulo \(2m\). Therefore the \(P_i\) partition \(E(K_{2m})\).

Now let \(n=2m+1\). For \(0\leq i\leq m\), set
\[
P_i=
\bigl(
v_i,v_{i+1},v_{i-1},v_{i+2},v_{i-2},\ldots,
v_{i+m},v_{i-m}
\bigr).
\]
The same nested-interval argument proves that each \(P_i\) is plane. Its edges are again precisely those with endpoint sums \(2i\) and \(2i+1\) modulo \(2m+1\). For each residue \(s\), there are exactly \(m\) non-loop pairs with endpoint sum \(s\). The pairs
\[
\{2i,2i+1\},\qquad 0\leq i\leq m,
\]
cover every residue, with only the residue \(0\) repeated. Thus the \(m+1\) paths cover all edges.

The general lower bound completes the proof. \(\square\)

This construction confirms that convex point sets cannot witness the conjectured strict inequality.

# 3. Structure of a near-\(n/2\) cover

The following accounting identity appears to be the most useful elementary reduction.

Let \(P_1,\ldots,P_k\) be a path cover, and write
\[
\ell_i=|E(P_i)|.
\]
For an edge \(e\), let \(\mu(e)\) be the number of covering paths containing it. Define

\[
D=\sum_{i=1}^k\bigl((n-1)-\ell_i\bigr)
\]
and
\[
R=\sum_{e\in E(K_n)}(\mu(e)-1).
\]

Here \(D\) is the total unused edge-capacity of the paths, while \(R\) is the total repeated-edge incidence.

## Proposition 3.1

Every path cover satisfies
\[
D+R=\left(k-\frac n2\right)(n-1).
\]

### Proof

Since every edge is covered,
\[
\sum_i\ell_i=\binom n2+R.
\]
Therefore
\[
D
=k(n-1)-\binom n2-R,
\]
which gives the identity. \(\square\)

## Consequences

If
\[
k=\frac n2+o(n),
\]
then
\[
D+R=o(n^2).
\]
Thus:

* the total number of omitted vertex incidences is \(o(n^2)\), because a path with \(\ell_i\) edges omits exactly
  \[
  n-(\ell_i+1)=(n-1)-\ell_i
  \]
  vertices;
* the total number of repeated edge incidences is \(o(n^2)\);
* for every fixed \(\eta>0\), all but \(o(n)\) of the paths contain at least \((1-\eta)n\) vertices.

In particular, a negative answer would require a nearly edge-disjoint family of almost Hamiltonian plane paths for every point set.

For even \(n\), the exact equality case is especially rigid.

## Corollary 3.2

Let \(n\) be even. Then \(\pi(A)=n/2\) if and only if \(E(K_n[A])\) admits a decomposition into \(n/2\) crossing-free Hamilton paths.

Moreover, in such a decomposition every vertex is an endpoint of exactly one of the paths.

### Proof

If \(k=n/2\), Proposition 3.1 gives \(D=R=0\). Thus every path has \(n-1\) edges, hence is Hamiltonian, and no edge is repeated.

At a fixed vertex \(v\), the sum of its degrees over all paths is \(n-1\). Since each of the \(n/2\) Hamilton paths contributes degree one or two,
\[
2\cdot\frac n2-(n-1)=1.
\]
Hence precisely one path contributes degree one at \(v\), and all the others contribute degree two. \(\square\)

More generally, if \(n\) is even and \(k=n/2+s\), then
\[
D+R=s(n-1).
\]
Thus proving the conjecture amounts to showing that some order types force \(\Omega(n^2)\) total omission or overlap in every family of plane paths covering all edges.

# 4. Weighted certificates

Let \(w:E(K_n[A])\to\mathbb R_{\geq0}\), and define
\[
W(w)=\sum_{e}w(e)
\]
and
\[
L_A(w)=\max_P\sum_{e\in E(P)}w(e),
\]
where the maximum is over all crossing-free paths \(P\).

## Proposition 4.1

For every nonnegative edge weighting,
\[
\pi(A)\geq \frac{W(w)}{L_A(w)}.
\]

### Proof

If \(P_1,\dots,P_k\) cover every edge, then
\[
\sum_{i=1}^k w(P_i)\geq W(w).
\]
On the other hand, each \(w(P_i)\leq L_A(w)\). \(\square\)

This is exactly the dual of the fractional path-cover linear program:
\[
\begin{array}{ll}
\text{minimize}&\displaystyle\sum_P x_P\\[2mm]
\text{subject to}&\displaystyle\sum_{P\ni e}x_P\geq1
\quad(e\in E(K_n[A])),\\
&x_P\geq0.
\end{array}
\]
The dual is
\[
\begin{array}{ll}
\text{maximize}&\displaystyle\sum_e y_e\\[2mm]
\text{subject to}&\displaystyle\sum_{e\in P}y_e\leq1
\quad(P\text{ plane}),\\
&y_e\geq0.
\end{array}
\]

Consequently, an affirmative answer would follow from point sets and weights satisfying
\[
L_A(w)\leq \frac{W(w)}{(1/2+\varepsilon)n}.
\]

# 5. A matching-based sufficient condition

For a geometric graph \(H\subseteq K_n[A]\), let
\[
\nu_{\mathrm{pl}}(H)
\]
be the maximum size of a crossing-free matching contained in \(H\).

## Proposition 5.1

Every crossing-free path \(P\) satisfies
\[
|E(P)\cap E(H)|\leq 2\nu_{\mathrm{pl}}(H).
\]
Consequently,
\[
\pi(A)\geq
\frac{|E(H)|}{2\nu_{\mathrm{pl}}(H)}.
\]

### Proof

Order the edges of \(P\) along the path. The odd-position edges form a matching, and the even-position edges form another matching. Both are crossing-free because \(P\) is crossing-free. Intersecting these two matchings with \(H\) gives two plane matchings in \(H\), each of size at most \(\nu_{\mathrm{pl}}(H)\).

The second assertion follows from Proposition 4.1 with the indicator weighting of \(E(H)\). \(\square\)

Hence the original problem has an affirmative answer if one can construct, for infinitely many \(n\), a geometric graph \(H_n\subseteq K_n[A_n]\) such that
\[
|E(H_n)|\geq (1+\delta)n\,\nu_{\mathrm{pl}}(H_n)
\]
for some fixed \(\delta>0\). This would give
\[
\pi(A_n)\geq \frac{1+\delta}{2}n.
\]

There is also a coloring formulation. Let \(\chi_{\mathrm{pm}}(A)\) be the minimum number of crossing-free matchings covering \(E(K_n[A])\). Splitting every path into its odd and even edges gives
\[
\chi_{\mathrm{pm}}(A)\leq 2\pi(A),
\]
and therefore
\[
\pi(A)\geq\frac{\chi_{\mathrm{pm}}(A)}2.
\]
Thus a construction with
\[
\chi_{\mathrm{pm}}(A)\geq(1+\delta)n
\]
would also settle the problem affirmatively.

I do not know such a construction.

# 6. Why the elementary crossing-matching argument stops at \(n/2\)

Let \(M\) be a pairwise-crossing matching. Every plane path contains at most one edge of \(M\), but
\[
|M|\leq \frac n2.
\]
Thus one such family gives at most the trivial lower bound.

The same remains true after summing independent degree and crossing-matching inequalities.

## Proposition 6.1

Let \(a_v\geq0\) be vertex weights, and let \(M_1,\dots,M_t\) be pairwise-crossing matchings with coefficients \(b_j\geq0\). Define
\[
w(uv)=a_u+a_v+\sum_{j:uv\in M_j}b_j.
\]
If one bounds each plane path separately by
\[
w(P)\leq 2\sum_v a_v+\sum_{j=1}^t b_j,
\]
then the resulting weighted lower bound is at most \(n/2\).

### Proof

Put \(A_0=\sum_v a_v\) and \(B_0=\sum_jb_j\). The proposed path bound follows from \(\deg_P(v)\leq2\) and \(|P\cap M_j|\leq1\).

The total edge weight is
\[
W=(n-1)A_0+\sum_j b_j|M_j|
 \leq (n-1)A_0+\frac n2 B_0.
\]
But
\[
(n-1)A_0+\frac n2 B_0
\leq
\frac n2(2A_0+B_0).
\]
Therefore the quotient obtained from these separately summed constraints is at most \(n/2\). \(\square\)

This does not rule out using several crossing matchings. It identifies what would be needed: a genuine incompatibility preventing one path from nearly saturating all the individual constraints simultaneously.

For example, suppose \(M_1,\dots,M_t\) are almost-perfect pairwise-crossing matchings and
\[
\max_P \sum_{j=1}^t |E(P)\cap M_j|
   \leq (1-\eta)t
\]
for a fixed \(\eta>0\). Weighting each edge by its number of occurrences among the \(M_j\) would give
\[
\pi(A)\geq
\left(\frac{1}{2(1-\eta)}-o(1)\right)n>\frac n2.
\]
Thus a family of crossing matchings with a uniform simultaneous-transversal deficit would solve the problem. The separate constraints alone do not provide that deficit.

# 7. Exact finite computation

For a fixed rational-coordinate point set \(A\), \(\pi(A)\) can be computed exactly as a finite set-cover integer program.

Enumerate every simple vertex sequence
\[
(v_0,\dots,v_r),\qquad 1\leq r\leq n-1,
\]
up to reversal, and retain it when no two nonadjacent segments
\(v_{i-1}v_i\) and \(v_{j-1}v_j\) cross. For rational coordinates, proper crossing is tested exactly using orientation determinants:
\[
\operatorname{orient}(a,b,c)\operatorname{orient}(a,b,d)<0,
\qquad
\operatorname{orient}(c,d,a)\operatorname{orient}(c,d,b)<0.
\]

For every retained path \(P\), introduce \(x_P\in\{0,1\}\) and solve
\[
\begin{array}{ll}
\text{minimize}&\displaystyle\sum_Px_P,\\[2mm]
\text{subject to}&\displaystyle\sum_{P\ni e}x_P\geq1
\quad(e\in E(K_n[A])).
\end{array}
\]
Binary variables suffice because using the identical path twice is never beneficial. The LP relaxation and its dual give exact weighted certificates of the form in Proposition 4.1.

A reproducible small-order-type search would need to archive:

* rational coordinates or an oriented-matroid chirotope;
* the complete generated path list;
* the integer optimum;
* for fractional bounds, an exact rational dual solution.

I have not run such a search and therefore make no small-\(n\) computational claim.

# 8. Remaining gap

The main unresolved step is to find an order type forcing a positive proportion of the capacity loss
\[
D+R.
\]
The elementary obstructions are all tight at \(n/2\):

* edge count gives \(n/2\);
* degree constraints give \(n/2\);
* one pairwise-crossing matching gives at most \(n/2\);
* arbitrary nonnegative sums of those constraints still give at most \(n/2\) unless one proves a simultaneous incompatibility;
* convex order types attain \(\lceil n/2\rceil\) exactly.

Thus an affirmative construction must exploit a global incompatibility among many nearly Hamiltonian plane paths, or equivalently a geometric graph with an unusually small plane-matching number relative to its edge count. No such construction is established here.