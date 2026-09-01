```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture reduces exactly to 4-connected triangulations; moreover, every bipyramid, and every triangular 3-sum of bipyramids and tetrahedra, has a connected 4-coloring complex.",
  "would_publish": false,
  "caveats": "The general 4-connected case, particularly the degree-4 and degree-5 configurations forced by Euler's formula, remains unresolved, and the novelty of these elementary reductions has not been checked."
}
```

# 1. Statement and conventions

Let \(T\) be a finite simple triangulation of the sphere. A 4-coloring is a proper map
\[
\phi:V(T)\longrightarrow \{1,2,3,4\}.
\]
A Kempe interchange chooses two colors \(a,b\), one connected component of the subgraph induced by the vertices colored \(a\) or \(b\), and interchanges \(a,b\) on that component. I use only the component relation of the 4-coloring complex: two colorings are in the same component precisely when they are related by Kempe interchanges.

Color permutations do not affect components. Indeed, a global transposition of \(a,b\) is obtained by interchanging \(a,b\) successively on every component of the \(a,b\)-induced subgraph.

The parity used below is the usual mod-2 degree of the simplicial map
\[
T\longrightarrow \partial K_4
\]
induced by \(\phi\).

# 2. A combinatorial description of parity

For \(i\in\{1,2,3,4\}\), let \(f_i(\phi)\) be the number of facial triangles whose color set is
\[
\{1,2,3,4\}\setminus\{i\}.
\]

## Lemma 2.1

The four integers \(f_i(\phi)\) have the same parity.

### Proof

Let \(i\ne j\), and let \(a,b\) be the other two colors. Every facial triangle counted by \(f_i\) or \(f_j\) contains exactly one \(a b\)-colored edge. Conversely, each \(a b\)-colored edge lies in two facial triangles, and the third color of each is either \(i\) or \(j\). Hence
\[
f_i(\phi)+f_j(\phi)=2e_{ab}(\phi),
\]
where \(e_{ab}(\phi)\) is the number of edges whose endpoint colors are \(a,b\). Thus \(f_i\equiv f_j\pmod 2\). ∎

Define
\[
p(\phi)=f_i(\phi)\pmod2,
\]
independently of \(i\). This agrees with the mod-2 topological degree.

## Lemma 2.2

Parity is invariant under a Kempe interchange.

### Proof

Suppose colors \(a,b\) are interchanged on a component \(C\). Choose a color \(i\notin\{a,b\}\). The triangles counted by \(f_i\) have color set \(\{a,b,c\}\), where \(c\) is the fourth color.

Any such triangle contains an \(a b\)-edge, so its \(a\)- and \(b\)-colored vertices lie in the same \(a,b\)-component. They are therefore either both switched or both left unchanged, and the triangle remains counted by \(f_i\). A triangle not containing both \(a,b\) cannot become one containing both after the interchange. Thus \(f_i\), and hence \(p\), is unchanged. ∎

Therefore every component of the coloring complex has a well-defined parity.

## Proposition 2.3: odd-degree formula

Let
\[
O(T)=\{v\in V(T):\deg_T(v)\text{ is odd}\}.
\]
For every color \(i\),
\[
p(\phi)\equiv
\sum_{\phi(v)=i}\deg_T(v)
\equiv
\bigl|O(T)\cap \phi^{-1}(i)\bigr|
\pmod2.
\]

### Proof

A triangulation on \(n\) vertices has \(2n-4\) faces, an even number. Every face containing color \(i\) contains exactly one vertex of color \(i\). Hence
\[
\sum_{\phi(v)=i}\deg_T(v)
  = (2n-4)-f_i(\phi)
  \equiv f_i(\phi)
  =p(\phi)\pmod2.
\]
Reducing the degree sum modulo \(2\) gives the second equality. ∎

Thus, in an even coloring, every color class contains an even number of odd-degree vertices; in an odd coloring, every color class contains an odd number of them. In particular:

- an odd coloring requires at least four odd-degree vertices;
- if \(T\) has at most two odd-degree vertices, every coloring is even;
- every bichromatic Kempe component contains an even number of odd-degree vertices.

For the last assertion, switching a component \(C\) between colors \(a,b\) changes the odd-degree count in color class \(a\) by \(|C\cap O(T)|\) modulo \(2\), while parity is invariant.

This formula is useful computationally: parity can be evaluated from a single color class without computing a degree of a simplicial map.

# 3. Exact factorization at a separating triangle

Let \(T=T_1\#_Q T_2\) be obtained by deleting the interiors of facial triangles \(Q\) in two triangulations \(T_1,T_2\) and identifying their boundaries. Equivalently, \(Q\) is a separating triangle of \(T\), and \(T_1,T_2\) are the triangulations on its two sides.

Write \(\mathcal C(T)\) for the set of Kempe components.

## Theorem 3.1

There is a natural bijection
\[
\mathcal C(T)\cong \mathcal C(T_1)\times\mathcal C(T_2).
\]
Under this bijection,
\[
p(C_1,C_2)=p(C_1)+p(C_2)\pmod2.
\]

### Proof of the component factorization

Order the vertices of \(Q\) as \(q_1,q_2,q_3\). Call a coloring normalized if
\[
\phi(q_1)=1,\qquad \phi(q_2)=2,\qquad \phi(q_3)=3.
\]
Every coloring has a unique color permutation which normalizes it.

For a triangulation \(S\) containing \(Q\), let \(\sim_Q\) be the equivalence relation on normalized colorings generated by Kempe interchanges on bichromatic components disjoint from \(Q\).

We first claim that ordinary Kempe components of \(S\) are in bijection with the \(\sim_Q\)-classes.

Indeed, consider a Kempe interchange between colors \(a,b\).

- If the chosen component avoids \(Q\), it is already an allowed \(\sim_Q\)-move.
- If it meets \(Q\), it is the unique \(a,b\)-component meeting \(Q\). This is because either both colors occur on \(Q\), in which case their two boundary vertices are adjacent, or one of the colors is the missing color \(4\), in which case there is only one relevant boundary vertex.

After switching this component, normalize again by the transposition \((a\,b)\). The composite operation is exactly the operation of switching every other \(a,b\)-component. All those other components avoid \(Q\). Thus a boundary-meeting Kempe move, after normalization, is a sequence of \(Q\)-avoiding moves.

Conversely, every \(Q\)-avoiding move is an ordinary Kempe move. Since global color permutations themselves are Kempe-equivalent to the identity, the claim follows.

Now a normalized coloring of \(T\) is exactly a pair of normalized colorings of \(T_1,T_2\). Moreover, every bichromatic component of \(T\) disjoint from \(Q\) lies wholly on one side of \(Q\), and it is a component disjoint from \(Q\) in that factor. Hence the normalized relative equivalence relation on \(T\) is the direct product of the relative equivalence relations on \(T_1,T_2\). This proves
\[
\mathcal C(T)\cong \mathcal C(T_1)\times\mathcal C(T_2).
\]

### Proof of the parity formula

For normalized colorings, each deleted triangle \(Q\) has color set \(\{1,2,3\}\), so
\[
f_4(T)=f_4(T_1)+f_4(T_2)-2.
\]
Reducing modulo \(2\) gives
\[
p(T)=p(T_1)+p(T_2).
\]
∎

# 4. Reduction to 4-connected triangulations

The preceding theorem yields an exact reduction of the conjecture.

## Corollary 4.1

The conjecture holds for all planar triangulations if and only if it holds for all triangulations with no separating triangle, apart from the harmless base case \(K_4\).

### Proof

Split a triangulation repeatedly along separating triangles. By Theorem 3.1, its component set is the product of the component sets of the resulting prime pieces, and component parity is the sum of the factor parities.

If the original coloring complex is disconnected, at least one factor coloring complex is disconnected. If that factor has components of both parities, then fixing components in all other factors produces components of both parities in the original triangulation.

Conversely, suppose a triangulation were a counterexample: it is disconnected, but all its components have the same parity. Fixing a component in one factor and varying a component in another shows that the component parities in every factor are constant. At least one factor is disconnected, and that factor is itself a counterexample. ∎

For a simple maximal planar graph on more than four vertices, absence of separating triangles is equivalent to 4-connectivity. Consequently:

## Corollary 4.2

A vertex-minimal counterexample would be 4-connected. In particular, it would have minimum degree at least \(4\), and by Euler's formula it would contain a vertex of degree \(4\) or \(5\).

This isolates the genuinely unresolved local cases.

## Corollary 4.3: stellar subdivision

Let \(T^+\) be obtained by inserting a vertex of degree \(3\) into a face of \(T\). Then
\[
|\mathcal C(T^+)|=|\mathcal C(T)|,
\qquad
p_{T^+}(C)=p_T(C)+1\pmod2.
\]

### Proof

This operation is precisely the triangular connected sum \(T\#K_4\). The coloring complex of \(K_4\) has one component, and its parity is odd. Apply Theorem 3.1. ∎

Hence the existence of any counterexample would imply the existence of an all-even counterexample and of an all-odd counterexample: subdividing one face preserves disconnection and reverses every component parity.

Equivalently, the original conjecture may be written as:

> If parity is constant over all 4-colorings of \(T\), then its 4-coloring complex is connected.

# 5. An infinite 4-connected special case: bipyramids

Let \(B_m\), \(m\ge3\), be the bipyramid over the cycle
\[
R=r_0r_1\cdots r_{m-1}r_0.
\]
Thus \(B_m\) has two nonadjacent apices \(x,y\), each adjacent to every rim vertex. For \(m\ge4\), \(B_m\) is 4-connected.

## Lemma 5.1

All proper 3-colorings of a cycle \(C_m\) are Kempe-equivalent.

### Proof

Use colors \(1,2,3\). Suppose color \(3\) occurs \(t\) times. The vertices of colors \(1,2\) between consecutive occurrences of color \(3\) form alternating paths, each of which is a component of the \(1,2\)-induced subgraph.

If \(t\ge2\), choose a vertex \(z\) of color \(3\). If its two neighbors have distinct colors \(1,2\), switch colors \(1,2\) on one of the two alternating gaps adjacent to \(z\). The neighbors of \(z\) then have the same color, say \(1\). Now \(z\) is an isolated component of the \(2,3\)-induced subgraph, so it may be changed from \(3\) to \(2\). This lowers \(t\) by one.

Repeating gives:

- if \(m\) is even, a 2-coloring of the cycle;
- if \(m\) is odd, a coloring with exactly one vertex of color \(3\), the remaining path alternating \(1,2\).

For even \(m\), all 2-colorings differ only by color permutation.

For odd \(m\), the unique vertex of color \(3\) can be moved one step around the cycle: its neighbor of, say, color \(2\), together with the color-\(3\) vertex, is a two-vertex \(2,3\)-Kempe component. Switching it moves the exceptional color \(3\) by one position. Color permutations handle the remaining choices. ∎

## Proposition 5.2

The 4-coloring complex of every bipyramid \(B_m\) is connected.

### Proof

Consider a 4-coloring \(\phi\).

If \(\phi(x)=\phi(y)=d\), the rim is a proper coloring of \(C_m\) with the other three colors. Every Kempe interchange between two of those three colors is confined to the rim. By Lemma 5.1 all such colorings belong to one component.

If \(\phi(x)\ne\phi(y)\), then every rim vertex must avoid both apex colors. Hence the rim uses the remaining two colors alternately, which is possible only for even \(m\). The two apices are isolated components of the subgraph induced by their two colors. Switching one apex changes its color to that of the other apex, reducing to the preceding case.

Finally, global color permutations are Kempe-equivalent to the identity. Thus all 4-colorings of \(B_m\) lie in one component. ∎

## Proposition 5.3

Every 4-coloring of \(B_m\) is even.

### Proof

Every rim vertex has degree \(4\). The apices have degree \(m\).

If \(m\) is even, all vertices have even degree, so Proposition 2.3 gives parity zero.

If \(m\) is odd, the two apices are the only odd-degree vertices. They must receive the same color, since distinct apex colors would force a 2-coloring of the odd rim cycle. Thus every color class contains either zero or two odd-degree vertices, again giving parity zero. ∎

This is a nontrivial all-even family: if any \(B_m\) had disconnected coloring complex, it would immediately disprove the conjecture, but Proposition 5.2 rules this out.

Combining this with Theorem 3.1 gives:

## Corollary 5.4

Every triangulation obtained by triangular 3-sums of tetrahedra and bipyramids has a connected 4-coloring complex. This includes all stacked triangulations.

# 6. A useful edge-flip observation

Let \(T_{13}\) and \(T_{24}\) differ by flipping the diagonal of a quadrilateral \(v_1v_2v_3v_4\). If a coloring \(\phi\) is proper for both triangulations, then the four boundary vertices necessarily have four distinct colors. In that case
\[
p_{T_{13}}(\phi)=p_{T_{24}}(\phi)+1\pmod2.
\]

Indeed, after naming the cyclic colors \(1,2,3,4\), the two faces using diagonal \(v_1v_3\) omit colors \(4,2\), while the two faces using diagonal \(v_2v_4\) omit colors \(3,1\). Thus each \(f_i\) changes by one modulo \(2\).

This indicates why a direct degree-\(4\) reduction is not automatic: edge flips reverse parity on their common colorings, while colorings with an alternating two-colored boundary do not extend across either diagonal.

# 7. Remaining gap

The separating-triangle argument reduces the conjecture exactly to 4-connected triangulations. Such a triangulation has a vertex of degree \(4\) or \(5\), but neither local configuration admits the clean product decomposition available for a triangle boundary:

- around a degree-\(4\) vertex, the neighbor cycle may use either two or three colors;
- replacing the vertex by a diagonal loses the alternating two-colored boundary states;
- colorings proper for both diagonal choices have four boundary colors and opposite parity in the two flipped triangulations;
- Kempe components can pass through the exterior of the neighbor cycle, so the local state cannot be treated independently.

I do not have a complete reduction for these degree-\(4\) or degree-\(5\) cases. Thus the conjecture is not proved or disproved here. The rigorous progress is the exact prime decomposition, the odd-degree parity formula, and the connectedness result for the infinite 4-connected bipyramid family.