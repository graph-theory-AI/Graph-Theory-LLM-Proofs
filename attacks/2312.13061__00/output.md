```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is not settled, but an alternating-terminal condition reduces extension to one bipartite perfect-matching computation and resolves all six-boundary instances except a precise four-terminal complement-linkage case.",
  "would_publish": false,
  "caveats": "The residual prescribed-pairing perfect-matching problem remains unsolved, and parts of the dual formulation may overlap the source paper."
}
```

# 1. Statement and scope

I do not obtain a polynomial-time algorithm for every fixed outer-face length.

I give:

1. an exact dual formulation as a precolored 3-edge-coloring problem in a plane bipartite cubic multipole;
2. a polynomial-time sufficient-and-necessary criterion when the non-distinguished boundary terminals alternate in a suitable sense;
3. a reduction of the first new case, outer length six, to one explicit four-terminal perfect-matching connectivity problem;
4. a six-vertex-wheel example showing that parity, bipartition balance, and the existence of each individual color matching are not sufficient.

The dual formulation is likely at least partly present in the source paper; I have not checked the full published text beyond the supplied summary.

# 2. The dual cubic multipole

Identify the four vertex colors with the elements of
\[
\Gamma=\mathbb Z_2^2=\{0,\alpha,\beta,\gamma\},
\qquad
\gamma=\alpha+\beta.
\]
The three nonzero elements will be called the three edge colors.

Let \(G\) be a triangulation of a disk with outer boundary \(C\). Construct a plane multipole \(H\) as follows.

- There is one vertex \(x_f\) for each internal triangular face \(f\) of \(G\).
- An internal edge of \(G\), incident with triangles \(f,f'\), gives an edge \(x_fx_{f'}\).
- An outer edge of \(G\), incident with an internal triangle \(f\), gives a semiedge at \(x_f\), whose free end lies on the boundary of the disk.

Every vertex of \(H\) has exactly three incidences, counting semiedges.

A proper 3-edge-coloring of \(H\) assigns \(\alpha,\beta,\gamma\) to its edges and semiedges so that the three incidences at every vertex receive all three colors.

## Lemma 2.1: Exact dual equivalence

Let \(\varphi\) be a precoloring of the outer vertices of \(G\). For every outer edge \(uv\), prescribe on the corresponding semiedge
\[
\psi(uv)=\varphi(u)+\varphi(v).
\]
If some outer edge has equal-colored ends, the answer is immediately no.

Otherwise, \(\varphi\) extends to a proper 4-coloring of \(G\) if and only if \(\psi\) extends to a proper 3-edge-coloring of \(H\).

### Proof

Suppose first that \(\kappa:V(G)\to\Gamma\) is a proper 4-coloring extending \(\varphi\). Give every primal edge \(uv\) the label
\[
\lambda(uv)=\kappa(u)+\kappa(v)\in\Gamma\setminus\{0\}.
\]
The three vertices of every triangular face have distinct colors. Consequently, the labels on its three edges are precisely
\(\alpha,\beta,\gamma\). Thus \(\lambda\) is a proper 3-edge-coloring of \(H\), with the prescribed values on its semiedges.

Conversely, suppose \(H\) has such a 3-edge-coloring. Transfer its labels to the corresponding primal edges. Around every triangular face, the three labels are \(\alpha,\beta,\gamma\), whose sum is zero. Hence the resulting \(\Gamma\)-valued edge labeling has zero sum around every 2-cell. Since the disk is simply connected, it is a coboundary: choose one outer vertex \(v_0\), set \(\kappa(v_0)=\varphi(v_0)\), and for any path \(v_0v_1\ldots v_r\), set
\[
\kappa(v_r)=\varphi(v_0)+\sum_{i=0}^{r-1}\lambda(v_iv_{i+1}).
\]
This is path-independent. Every edge has nonzero label, so \(\kappa\) is proper. Along the outer boundary, the prescribed labels are exactly the differences of \(\varphi\), and therefore \(\kappa=\varphi\) there. ∎

## Lemma 2.2: Bipartiteness

If every interior vertex of \(G\) has even degree, then the underlying graph of \(H\) is bipartite.

### Proof

Let \(Q\) be a cycle of \(H\). Its bounded side contains only dual faces corresponding to interior vertices of \(G\); faces corresponding to boundary vertices are incident with the exterior after the outer dual vertex is removed.

Modulo two, the length of \(Q\) equals the sum of the lengths of the dual faces inside \(Q\), since internal dual edges are counted twice. Those face lengths are the degrees of the corresponding interior primal vertices and hence are even. Thus every cycle of \(H\) is even. ∎

Thus the conjecture can be restated as follows.

> For every fixed \(k\), decide in polynomial time whether a prescribed coloring of the \(k\) boundary semiedges of a plane bipartite cubic multipole extends to a proper 3-edge-coloring.

# 3. Universal necessary conditions

Let \(X,Y\) be the bipartition of \(H\), and let \(s_i(X)\) and \(s_i(Y)\) denote the numbers of semiedges of color \(i\) incident with \(X\) and \(Y\), respectively.

## Lemma 3.1: Balance and parity

If the boundary state extends, then for each edge color \(i\),
\[
s_i(X)-s_i(Y)=|X|-|Y|.
\tag{1}
\]
Moreover, if \(k\) is the total number of semiedges and \(s_i=s_i(X)+s_i(Y)\), then
\[
s_i\equiv k\pmod 2.
\tag{2}
\]

### Proof

In a proper 3-edge-coloring, every vertex has exactly one incidence of color \(i\). If \(m_i\) is the number of internal edges of color \(i\), then
\[
|X|=m_i+s_i(X),\qquad |Y|=m_i+s_i(Y),
\]
which gives (1).

If \(n=|V(H)|\), counting incidences of color \(i\) gives
\[
n=2m_i+s_i,
\]
so \(s_i\equiv n\pmod2\). Counting all incidences gives
\[
3n=2|E(H)|+k,
\]
and hence \(n\equiv k\pmod2\). This proves (2). ∎

These identities are efficiently checkable but are not sufficient; see Section 7.

# 4. A matching formulation for one distinguished color

Fix one edge color \(a\), and call the other two \(b,c\).

Assume first that the prescribed semiedges incident with any one vertex have distinct prescribed colors; otherwise extension is locally impossible.

Let
\[
U_a=\{v\in V(H):\text{ no \(a\)-colored semiedge is incident with \(v\)}\}.
\]

In any extension, the internal edges colored \(a\) form a perfect matching of the induced graph \(H[U_a]\):

- vertices outside \(U_a\) already have their unique \(a\)-incidence on a semiedge;
- every vertex in \(U_a\) must be incident with exactly one internal \(a\)-edge;
- an \(a\)-edge cannot have an endpoint outside \(U_a\).

Thus:

## Lemma 4.1

If \(H[U_a]\) has no perfect matching, then the prescribed boundary state does not extend.

This is only a necessary condition in general. The issue is whether the complement of a chosen matching can be colored alternately with \(b,c\) while respecting the remaining boundary semiedges.

# 5. The alternating-terminal theorem

Let \(T_a\) be the set of semiedges whose prescribed color is \(b\) or \(c\). Their free ends occur in a cyclic order around the boundary.

For \(e\in T_a\), let \(v(e)\) be its vertex endpoint. Define
\[
q_a(e)
 =
 {\bf 1}_{v(e)\in Y}
 \mathbin{\oplus}
 {\bf 1}_{\psi(e)=c}
 \in\mathbb Z_2.
\tag{3}
\]
Swapping \(X,Y\), or swapping the names \(b,c\), complements every \(q_a(e)\), so the property that these values alternate is well-defined.

## Theorem 5.1: Alternating-terminal matching criterion

Suppose the values \(q_a(e)\), for \(e\in T_a\) in cyclic boundary order, alternate \(0,1,0,1,\ldots\). Then the prescribed boundary state extends to a proper 3-edge-coloring of \(H\) if and only if \(H[U_a]\) has a perfect matching.

Consequently, this case is decidable by one bipartite perfect-matching computation.

### Proof

Necessity is Lemma 4.1. For sufficiency, let \(M\) be a perfect matching of \(H[U_a]\), and color its edges \(a\). The prescribed \(a\)-semiedges provide the \(a\)-incidence at all remaining vertices.

Let \(F\) consist of:

- all internal edges not in \(M\);
- all semiedges prescribed \(b\) or \(c\).

At every core vertex of \(H\), exactly two incidences belong to \(F\). Hence every component of \(F\) is either:

- a cycle containing no semiedges, or
- a path whose two ends are semiedges of \(T_a\).

Because \(H\) is bipartite, every cycle component has even length and can be colored alternately \(b,c\).

Consider a path component with end semiedges \(e,f\), incident with vertices \(u,v\). Suppose the internal part of the path contains \(m\) internal edges. Passing through a core vertex changes \(b\) to \(c\) or \(c\) to \(b\), while traversing an internal edge preserves its color. Thus the two prescribed end colors are compatible exactly when:

- they are equal if \(m\) is odd;
- they are different if \(m\) is even.

Since \(H\) is bipartite,
\[
m\equiv {\bf 1}_{u\in Y}\oplus{\bf 1}_{v\in Y}\pmod2.
\]
Substitution into (3) shows that the compatibility condition is precisely
\[
q_a(e)\ne q_a(f).
\tag{4}
\]

The path components of \(F\) give a noncrossing pairing of the boundary semiedges in \(T_a\). Every noncrossing perfect matching of cyclically ordered \(2r\) points pairs an odd-indexed point with an even-indexed point: if points \(i,j\) are paired, one of the two boundary intervals between them must contain an even number of points. Hence \(i\) and \(j\) have opposite parity.

Since the \(q_a\)-values alternate, every paired pair has opposite \(q_a\)-values. By (4), every path can therefore be colored consistently with its prescribed end colors. Together with arbitrary alternating colorings of the cycle components, this gives a proper 3-edge-coloring of \(H\). ∎

## Corollary 5.2: Dominant boundary difference

For arbitrary outer length, if some edge color \(a\) occurs on all but at most two boundary semiedges, extension is decidable by one perfect-matching computation and one parity check.

Indeed:

- with no \(b,c\)-terminal, every complement component is an even cycle;
- with two terminals, they must lie on the unique path component, and compatibility is exactly that their \(q_a\)-values differ.

This criterion is not restricted to precolorings using only three vertex colors.

# 6. What this gives for outer length six

Let \(k=6\), and let \(s_a,s_b,s_c\) be the numbers of boundary semiedges of the three edge colors.

By Lemma 3.1, any extendible state has all three counts even. Thus, up to permutation, the only possibilities are
\[
(6,0,0),\qquad (4,2,0),\qquad (2,2,2).
\]

If the distribution is not \((2,2,2)\), choose a color occurring at least four times. There are at most two terminals of the other colors, so Corollary 5.2 gives an exact polynomial-time decision.

Thus the only genuinely new six-boundary case has each edge color occurring exactly twice.

Fix a distinguished color \(a\). There are then four terminals in \(T_a\).

- If \(H[U_a]\) has no perfect matching, reject.
- In any extension, every path pairs opposite \(q_a\)-values, so there must be two terminals of each \(q_a\)-type.
- If the four \(q_a\)-values alternate around the boundary, Theorem 5.1 decides the instance.
- Otherwise, after cyclic rotation and complementation, their order is
  \[
  0,0,1,1.
  \tag{5}
  \]

There are only two noncrossing pairings of four cyclically ordered terminals. Under (5), exactly one is compatible:
\[
(t_1,t_4),\qquad (t_2,t_3).
\tag{6}
\]
The other pairing, \((t_1,t_2),(t_3,t_4)\), joins equal \(q_a\)-types.

Therefore the unresolved six-boundary case is exactly:

> Given a plane bipartite cubic multipole \(H\), four marked boundary semiedges \(t_1,t_2,t_3,t_4\), and \(U_a\), decide whether \(H[U_a]\) has a perfect matching \(M\) such that the components of the complement \(F\) pair the terminals as in (6).

This is not an ordinary perfect-matching condition: it constrains connectivity in the complement of the matching.

For completeness, if \(H[U_a]\) has a unique perfect matching, then the residual case is polynomial. One computes that matching, forms \(F\), and checks its terminal pairing. Uniqueness itself can be tested by checking for an alternating cycle relative to a found matching.

# 7. A six-boundary obstruction beyond individual matching tests

Let \(G\) consist of a 6-cycle
\[
v_1v_2\ldots v_6v_1
\]
and an interior vertex \(z\) adjacent to all six boundary vertices. The only interior vertex has degree six, so \(G\) is near-Eulerian.

Precolor the boundary by
\[
\varphi(v_1),\ldots,\varphi(v_6)
 =
 0,\alpha,0,\beta,0,\gamma.
\tag{7}
\]
This is a proper coloring of the outer cycle and uses all four colors. Since \(z\) is adjacent to boundary vertices of all four colors, (7) does not extend.

The dual multipole is a 6-cycle \(x_1\ldots x_6x_1\), with one semiedge at each \(x_i\). The boundary difference word is
\[
\alpha,\alpha,\beta,\beta,\gamma,\gamma.
\tag{8}
\]
With the alternating bipartition
\[
X=\{x_1,x_3,x_5\},\qquad
Y=\{x_2,x_4,x_6\},
\]
each edge color occurs once on each side. Thus (8) satisfies both the parity condition and the bipartition-balance condition.

Moreover, for each of the three choices of distinguished color \(a\), the graph \(H[U_a]\) has a perfect matching. For example, for \(a=\alpha\), it is the induced path on \(x_3,x_4,x_5,x_6\), with unique perfect matching
\[
\{x_3x_4,x_5x_6\}.
\]
Nevertheless, its complement gives the incompatible terminal pairing.

Hence the following are not sufficient, even for outer length six:

1. the parity identities;
2. the bipartition-balance identities;
3. existence of the required internal matching for each individual edge color.

For comparison, on the same wheel the boundary difference word
\[
\beta,\gamma,\alpha,\beta,\gamma,\alpha
\]
integrates to the three-color boundary precoloring
\[
0,\beta,\alpha,0,\beta,\alpha,
\]
which extends by coloring the hub \(\gamma\). Thus the four-terminal residual problem has both yes- and no-instances.

# 8. General exact upper bound from treewidth

There is also a standard deterministic subexponential algorithm, though it does not approach the desired polynomial bound.

Replace each semiedge of \(H\) by an edge to a new leaf. Proper 3-edge-coloring becomes ordinary vertex 3-coloring of the line graph, with the leaf-edge vertices precolored.

If \(H\) has treewidth \(w\), a tree decomposition of its line graph of width at most
\[
3(w+1)-1
\]
is obtained by replacing every bag \(B\) by the set of edges incident with vertices of \(B\). Standard color-assignment dynamic programming therefore runs in
\[
3^{\,3w+O(1)}|V(H)|
\]
time.

Since a planar \(N\)-vertex graph has a tree decomposition of width \(O(\sqrt N)\), this gives a deterministic
\[
2^{O(\sqrt N)}
\]
algorithm for the unrestricted boundary-extension problem. This is a generic planar bound and does not prove the conjecture.

# 9. Remaining gap

The substantive unresolved point is the following connectivity-constrained matching problem:

- choose a perfect matching \(M\) of \(H[U_a]\);
- the complementary degree-two subgraph must realize one of a prescribed finite set of noncrossing pairings of the boundary terminals.

For fixed outer length there are only constantly many possible pairings, but I do not have a polynomial algorithm for deciding whether a specified pairing is realizable. An ordinary matching oracle controls which edges belong to \(M\), not which terminals lie in the same component of its complement.

Already with four terminals this is exactly the residual \((2,2,2)\) case above. I neither prove this residual problem polynomial nor establish hardness. Consequently, the general conjecture remains open.