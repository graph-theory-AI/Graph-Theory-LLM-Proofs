```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "For the natural formulation that every convex drawing should admit a pseudocircular extension, I prove a one-page special case, an NP certificate theorem, and a universal four-intersection completion, but not the required two-intersection result.",
  "would_publish": false,
  "caveats": "The catalog gives a characterization request rather than a formal conjecture, and exact conventions for carrier curves at common graph vertices must be fixed."
}
```

# 1. Precise formulation

The catalog entry is not itself a proposition with a truth value: “characterize convex drawings in terms of pseudocircular drawings” could ask for an equivalence, one implication, or additional axioms on a pseudocircular extension. I use the following natural central question.

Let \(D\) be a simple topological drawing of \(K_n\) on \(S^2\). For every triangle \(T\), its image is a Jordan curve and hence bounds two closed disks. A side \(\Delta\) of \(T\) is **convex** if, whenever vertices \(x,y\) lie in \(\Delta\), the entire drawn edge \(D[xy]\) lies in \(\Delta\). The drawing is convex if every triangle has a convex side.

A **pseudocircular extension** is a family
\[
\{\Gamma_e:e\in E(K_n)\}
\]
of Jordan curves such that:

1. \(D[e]\) is a subarc of \(\Gamma_e\);
2. \(\Gamma_e\) contains no graph vertex other than the endpoints of \(e\);
3. every two distinct carrier curves meet at most twice.

Away from prescribed graph vertices, intersections may be assumed transverse and pairwise. If the source uses a slightly different convention at common endpoints, the arguments below require the corresponding local adjustment only.

The natural conjectural implication is

\[
\tag{PC}
D\text{ convex}\quad\Longrightarrow\quad D\text{ pseudocircular}.
\]

The result quoted in the prompt already proves (PC) when \(D\) is hereditarily convex: hereditary-convex drawings are pseudospherical, and pseudospherical drawings are, by definition, pseudocircular. Thus only convex drawings admitting no hereditary choice of sides remain relevant.

I do not prove (PC) and do not construct a counterexample.

# 2. Two elementary structural facts about convexity

## Proposition 2.1: Convexity is \(7\)-local

A simple drawing \(D\) is convex if and only if every induced subdrawing on at most seven vertices is convex.

### Proof

Convexity is preserved by deleting vertices: a side convex for \(D\) remains convex after deleting vertices and their incident edges.

Conversely, suppose \(D\) is not convex. Then some triangle \(T\) has neither side convex. For each of its two sides \(\Delta_i\), choose vertices \(x_i,y_i\in \Delta_i\) such that
\[
D[x_i y_i]\not\subseteq \Delta_i.
\]
The induced drawing on
\[
V(T)\cup\{x_0,y_0,x_1,y_1\}
\]
has at most seven vertices, and the same two witness edges show that neither side of \(T\) is convex in that subdrawing. Hence that induced subdrawing is not convex. ∎

This does not give a local characterization of pseudocircular extendibility, but it provides a bounded certificate for failure of convexity.

## Proposition 2.2: Hereditary convexity is a 2-SAT property

Let \(\mathcal T\) be the set of triangles of \(D\). Label the two sides of \(T\) by \(\Delta_T^0,\Delta_T^1\), and introduce one Boolean variable \(X_T\), where \(X_T=i\) means that \(\Delta_T^i\) is selected.

Construct a 2-CNF formula \(\Phi_D\) as follows.

1. If \(\Delta_T^i\) is not convex, include the unit clause
   \[
   X_T\ne i.
   \]

2. For triangles \(T,T'\) and \(i,j\in\{0,1\}\), if
   \[
   D[T']\subseteq \Delta_T^i
   \quad\text{but}\quad
   \Delta_{T'}^j\not\subseteq \Delta_T^i,
   \]
   include the binary clause
   \[
   (X_T\ne i)\ \lor\ (X_{T'}\ne j).
   \]

Then \(D\) is hereditarily convex if and only if \(\Phi_D\) is satisfiable.

### Proof

A hereditary assignment chooses a convex side for every triangle, so it satisfies all unit clauses. If it selected \(X_T=i\) and \(X_{T'}=j\) for one of the forbidden pairs in item 2, it would violate the nesting requirement. Hence it satisfies \(\Phi_D\).

Conversely, let an assignment satisfy \(\Phi_D\). The unit clauses ensure that every selected side is convex. If \(D[T']\subseteq \Delta_T^{X_T}\), then the clause in item 2 excludes every choice for \(T'\) whose selected side is not contained in \(\Delta_T^{X_T}\). Thus the selected sides satisfy the hereditary nesting condition. ∎

All side-convexity and side-containment tests can be performed from the planarization and its rotation system. Consequently, hereditary convexity is recognizable in polynomial time by 2-SAT.

By the theorem quoted in the catalog, every drawing for which \(\Phi_D\) is satisfiable is pseudocircular. Therefore a genuinely unresolved instance of (PC) must be a convex drawing for which the implication graph of \(\Phi_D\) contains a contradictory cycle. This observation does not handle such a cycle; it only isolates the residual class.

# 3. A direct special case: one-page drawings

Call \(D\) **one-page** if there is a closed disk \(B\subset S^2\) such that every vertex lies on \(\partial B\), every edge interior lies in \(\operatorname{int}B\), and \(\partial B\) otherwise avoids the drawing.

## Proposition 3.1

Every simple one-page drawing has a pseudocircular extension. In particular, (PC) holds for convex drawings satisfying the one-page condition.

### Proof

Let \(B^{-}=\overline{S^2\setminus B}\), another disk. Choose a homeomorphism
\[
r:B\longrightarrow B^{-}
\]
that fixes \(\partial B\) pointwise. For every edge \(e=uv\), define
\[
\Gamma_e=D[e]\cup r(D[e]).
\]
The two arcs have precisely their endpoints \(u,v\) in common, so \(\Gamma_e\) is a Jordan curve containing \(D[e]\).

Consider two independent edges \(e,f\). If they cross in \(B\), then their reflected copies cross once in \(B^{-}\), and hence
\[
|\Gamma_e\cap\Gamma_f|=2.
\]
If they do not cross, neither do their reflected copies, and the carrier curves are disjoint.

If \(e,f\) are adjacent, the unperturbed carriers have only their common graph vertex in common. Under a convention allowing prescribed nontransverse contacts at graph vertices, this already gives at most two common points. If carrier curves are required to cross properly at the common vertex, modify the reflected arcs inside a sufficiently small exterior neighborhood of each graph vertex. Arrange the reflected germs in the order making every pair of full carrier curves alternate at the vertex, and connect them to the unchanged reflected arcs by a wiring diagram. The required permutation can be drawn so that every pair of strands crosses at most once. Consequently, two adjacent carriers have their common endpoint and at most one additional crossing. These neighborhoods are mutually disjoint and contain no independent pair of edges, so no other pair count changes.

Thus every carrier pair meets at most twice. ∎

This is essentially a doubling argument for pseudosegments in a disk. It may be subsumed by stronger known results for face-convex or pseudolinear drawings; I make no novelty claim.

# 4. Pseudocircular extendibility has polynomial certificates

A combinatorial drawing is encoded by its planarization, rotations at original vertices and crossings, the marked trails corresponding to graph edges, and the order of crossings along every edge.

## Proposition 4.1

For combinatorially encoded simple drawings, deciding whether a pseudocircular extension exists belongs to NP.

The same is true if one additionally imposes any fixed finite list of local pseudospherical-type conditions, such as requiring exactly two intersections for specified pairs or bounding how often an original edge meets another carrier.

### Proof

Let \(m=|E(K_n)|\). Suppose an extension exists. New intersections may be put in general position: no new intersection need coincide with an original vertex or crossing, and no three carriers need meet at a new point. Since every carrier pair meets at most twice, the union of the carriers has \(O(m^2)\) intersection incidences.

A certificate records the planarized union
\[
H=\bigcup_{e\in E(K_n)}\Gamma_e.
\]
More explicitly, it records:

1. for each \(e\), a cyclic word listing the vertices and crossings encountered along \(\Gamma_e\);
2. the interval of this cyclic word corresponding to the fixed original arc \(D[e]\);
3. which labels represent original graph vertices, original crossings, and new carrier intersections;
4. the cyclic rotation of half-edges at every node;
5. the pairing of half-edges belonging to each carrier through every crossing.

Each carrier meets every other carrier at most twice, so each cyclic word has length \(O(m)\), and the entire certificate has size \(O(m^2\log m)\).

The verifier checks in polynomial time that:

- every \(\Gamma_e\) is a simple cycle;
- the marked original intervals reproduce the prescribed crossing orders of \(D\);
- deleting completion arcs and suppressing their crossings with original edges recovers the planarization of \(D\);
- no carrier contains an unrelated graph vertex;
- every carrier pair has at most two common labels;
- at an ordinary crossing the two pairs of half-edges alternate;
- the supplied rotation system is spherical.

For the last condition, let \(\rho\) be the rotation permutation on darts and \(\alpha\) the dart-reversal involution. Counting cycles of the face permutation \(\rho\alpha\) gives \(F\); since \(H\) is connected, the verifier checks
\[
|V(H)|-|E(H)|+F=2.
\]
Thus the rotation system realizes \(H\) on \(S^2\).

Conversely, a certificate passing these tests gives a planar embedding of \(H\). Smoothing each marked pair of opposite half-edges produces Jordan carrier curves. The marked subembedding has the same rotation system and crossing orders as \(D\), so an ambient homeomorphism identifies it with the given drawing. The resulting carriers form the desired pseudocircular extension. ∎

This gives an exact finite search procedure. For fixed \(n\), one can enumerate all combinatorial simple drawings, filter them for convexity, and then enumerate all carrier certificates with at most \(2\binom m2\) pairwise intersection incidences. I did not execute such an enumeration, so I claim no verified small-\(n\) result.

# 5. A universal four-intersection completion

The following indicates how close a purely local construction gets to pseudocircularity.

## Proposition 5.1

Every simple topological drawing of every finite graph has carrier Jordan curves \(\Gamma_e\supseteq D[e]\) such that every pair of carriers meets at most four times. New intersections can be made transverse, and no carrier need contain an unrelated graph vertex.

### Proof

Choose disjoint small disks around all original vertices and crossings. Outside these disks, the drawing consists of pairwise disjoint compact arc segments. Give each such segment a narrow rectangular strip, with all strips mutually disjoint.

For every edge \(e\), choose a continuous side along \(D[e]\) and draw a parallel return arc \(e^+\) through these strips.

At an original crossing of edges \(e\) and \(f\), straighten the picture inside its disk so that \(e,f\) are respectively horizontal and vertical. Route \(e^+,f^+\) as nearby horizontal and vertical arcs. Then
\[
e\cup e^+
\quad\text{and}\quad
f\cup f^+
\]
have at most four intersections in that disk, one for each of
\[
e\cap f,\qquad e\cap f^+,\qquad e^+\cap f,\qquad e^+\cap f^+.
\]

It remains to connect each return arc to its edge endpoints. Around a vertex \(v\), straighten the incident original branches into radial arcs with pairwise non-antipodal directions \(\theta_i\). Make the return branch associated with direction \(\theta_i\) leave \(v\) in the opposite direction \(\theta_i+\pi\), and then turn monotonically through an angle slightly less than \(\pi\) to reach the required side of its parallel strip. Such branches can be chosen so that:

- a return branch crosses any original radial branch at most once;
- two return branches cross at most once;
- a return branch does not cross its own original branch.

For two edges \(e,f\) incident with \(v\), their carrier curves therefore have at most the following four common points in the vertex disk:
\[
v,\qquad e^+\cap f,\qquad e\cap f^+,\qquad e^+\cap f^+.
\]
A generic perturbation removes unintended triple points.

Finally, put
\[
\Gamma_e=D[e]\cup e^+.
\]
The two constituent arcs have only their endpoints in common, so \(\Gamma_e\) is a Jordan curve. Two nonincident, noncrossing original edges have disjoint chosen neighborhoods; two crossing edges interact only in their unique crossing disk; and two adjacent edges interact only in their common vertex disk. Hence every pair of carriers meets at most four times. ∎

Four is the first possible transverse bound above two: any two Jordan curves on \(S^2\) cross an even number of times. Indeed, one curve bounds a disk, and the other enters and leaves that disk equally often.

For two independent original edges \(e,f\) that cross once, a pseudocircular extension must add exactly one further intersection. Writing \(e^*,f^*\) for their complementary carrier arcs, after generic perturbation the target equation is
\[
1+
|e\cap f^*|+
|e^*\cap f|+
|e^*\cap f^*|
=2.
\]
The regular-neighborhood construction instead realizes all three additional terms and gives four intersections.

Moreover, this excess cannot be removed while both complementary arcs remain parallel through the same small crossing disk: every left-to-right strand meets every bottom-to-top strand. At least one complementary arc must make a genuinely global bypass. The missing step is to use convex sides to choose these bypasses simultaneously without causing some other carrier pair to meet more than twice.

# 6. Remaining gap

The unresolved core is therefore:

> Given a convex drawing whose hereditary-side 2-SAT formula is unsatisfiable, construct complementary arcs \(e^*\) so that every originally meeting pair of carriers acquires exactly one additional intersection, while every originally disjoint pair acquires at most two.

Neither convexity’s \(7\)-local witness property nor the NP certificate theorem supplies such arcs. Conversely, they do not provide a finite obstruction proving that no such arcs exist. The four-intersection construction shows that arbitrary simple drawings have a close relaxation, but convexity has not been used to reduce four to two.

Thus there is presently no complete proof, no explicit convex non-pseudocircular counterexample, and no claimed publishable resolution here.