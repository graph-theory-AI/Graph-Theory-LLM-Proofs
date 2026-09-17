```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when the cyclic classes have prime size or size four, and pairwise intersection forces the stronger bound 3n <= 2c(D)^2.",
  "would_publish": false,
  "caveats": "No general proof or counterexample is obtained; these are self-contained partial results, with no claim of literature novelty."
}
```

# 1. Results and conventions

I do not resolve the question in general. I obtain two strengthenings of the supplied attempt:

1. **A stronger obstruction.** Let \(D\) have \(n\) vertices and directed circumference \(c\). If every two longest directed cycles intersect, then
   \[
   \boxed{3n\le 2c^2.}
   \]
   More precisely, if \(3n>2c^2\), then **every** longest cycle has a vertex-disjoint automorphic image.

2. **Additional Hamiltonian cases.** Let \(h\) be the period of \(D\), and let \(m=n/h\) be the size of each cyclic class. Then \(D\) is Hamiltonian whenever
   \[
   \boxed{m=1,\quad m\text{ is prime},\quad\text{or}\quad m=4.}
   \]
   In particular, this holds whenever \(m\le 5\).

The first result strengthens the previous attempt’s valid \(n\ge c^2\) averaging obstruction. All arguments used below are proved explicitly.

Throughout, digraphs are finite, loopless, and simple; directed \(2\)-cycles are allowed. We consider \(n\ge2\), the one-vertex case being vacuous.

A weakly connected vertex-transitive digraph is strongly connected. Indeed, its automorphism group acts transitively on the strongly connected components. The condensation is therefore a finite vertex-transitive acyclic digraph. Since it has a source, all its vertices are sources, so it has no arcs. Weak connectivity forces there to be just one component. Consequently \(c\ge2\).

# 2. A stronger averaging obstruction

The improvement over elementary averaging comes from a restriction on configurations of three longest cycles.

## 2.1 A forbidden configuration

**Lemma 2.1.** Three longest directed cycles cannot have pairwise intersections consisting of three distinct singleton vertices.

**Proof.** Suppose \(C_1,C_2,C_3\) all have length \(c\), with
\[
V(C_1)\cap V(C_2)=\{x_{12}\},\qquad
V(C_2)\cap V(C_3)=\{x_{23}\},\qquad
V(C_3)\cap V(C_1)=\{x_{31}\},
\]
where the three displayed vertices are distinct.

On each \(C_i\), its two intersection vertices split it into two directed paths. These six paths can be assembled into two directed cycles:
\[
x_{12}\overset{C_1}{\longrightarrow}x_{31}
\overset{C_3}{\longrightarrow}x_{23}
\overset{C_2}{\longrightarrow}x_{12},
\]
and the cycle using the three complementary paths.

Both assembled cycles are simple: the original cycles have no intersections other than the three specified vertices. Their lengths sum to \(3c\), so one has length at least \(3c/2>c\), a contradiction. ∎

Thus, if longest cycles \(A,B\) meet only at \(v\), any longest cycle that meets each of \(A,B\) in exactly one vertex must contain \(v\).

## 2.2 A sparse fractional cover

The following elementary linear-algebra observation is useful.

**Lemma 2.2.** Let a transitive permutation group act on an \(n\)-element set, and let \(\mathcal F\) be an orbit of \(c\)-element subsets. There are distinct members
\[
A_1,\ldots,A_k\in\mathcal F,\qquad k\le n,
\]
and positive weights \(w_1,\ldots,w_k\) such that
\[
\sum_{i:\,v\in A_i}w_i=1
\quad\text{for every vertex }v.
\]
In particular,
\[
T:=\sum_{i=1}^k w_i=\frac nc,
\qquad
\max_i w_i\ge \frac1c.
\]

**Proof.** Every vertex belongs to the same positive number \(r\) of members of \(\mathcal F\). Giving every member weight \(1/r\) provides the required vertex sums.

If more than \(n\) weights are positive, the corresponding incidence vectors are linearly dependent. Suppose
\[
\sum_A z_A\mathbf 1_A=0
\]
is a nonzero dependence. Summing coordinates gives \(c\sum_Az_A=0\), so the coefficients have both signs. Subtracting a suitable positive multiple of this dependence from the weights preserves all vertex sums, keeps all weights nonnegative, and makes at least one weight zero. Repeating leaves at most \(n\) positive weights.

Summing the vertex equations gives \(cT=n\), and hence
\[
\max_iw_i\ge T/k\ge T/n=1/c.
\]
∎

## 2.3 The bound

**Theorem 2.3.** Let \(D\) be a vertex-transitive digraph of order \(n\) and circumference \(c\ge2\). Let \(\Gamma\le\operatorname{Aut}(D)\) be transitive, and let \(C\) be a longest cycle. If \(C\) meets every \(\Gamma\)-image of itself, then
\[
3n\le2c^2.
\]

Consequently, if \(3n>2c^2\), every longest cycle has a vertex-disjoint image under \(\Gamma\).

**Proof.** Let
\[
\mathcal F=\{gV(C):g\in\Gamma\}.
\]
The hypothesis implies that \(\mathcal F\) is pairwise intersecting: applying \(g^{-1}\) reduces the intersection of \(gV(C)\) and \(g'V(C)\) to the stated hypothesis.

Choose a weighted subfamily as in Lemma 2.2, and write \(w(A)\) for its weights. Its total weight is
\[
T=\frac nc.
\]

For a supported set \(A\), define its singleton-intersection neighborhood and its weight by
\[
N_1(A)=\{B:|A\cap B|=1\},\qquad
s(A)=\sum_{B\in N_1(A)}w(B).
\]
All sets under consideration are vertex sets of longest cycles.

The vertex-cover equations give
\[
c=\sum_B w(B)|A\cap B|.
\]
Writing \(a=w(A)\), pairwise intersection implies
\[
c\ge ca+s(A)+2\bigl(T-a-s(A)\bigr).
\]
Therefore
\[
s(A)\ge 2T+(c-2)a-c. \tag{2.1}
\]

Choose \(A\) with \(a\ge1/c\).

If \(s(A)=0\), then (2.1) gives \(2T\le c\), and hence
\[
n\le c^2/2<2c^2/3.
\]
So assume \(s(A)>0\), and choose \(B\in N_1(A)\), with \(b=w(B)>0\). Write \(A\cap B=\{v\}\).

By Lemma 2.1, every member of \(N_1(A)\cap N_1(B)\) contains \(v\). Neither \(A\) nor \(B\) belongs to this common neighborhood. Since the total weight through \(v\) is \(1\),
\[
w\bigl(N_1(A)\cap N_1(B)\bigr)\le1-a-b.
\]
The union of the two neighborhoods has weight at most \(T\). Thus
\[
s(A)+s(B)\le T+1-a-b. \tag{2.2}
\]

Adding (2.1) for \(A\) and \(B\), and comparing with (2.2), yields
\[
4T+(c-2)(a+b)-2c\le T+1-a-b,
\]
or
\[
3T\le2c+1-(c-1)(a+b).
\]
Since \(a\ge1/c\), \(b>0\), and \(c>1\),
\[
3T<2c+\frac1c.
\]
Multiplication by \(c\) gives
\[
3n<2c^2+1.
\]
Both \(3n\) and \(2c^2\) are integers, so \(3n\le2c^2\). ∎

### Consequence for the original conjecture

An affirmative answer would imply the universal circumference bound
\[
\boxed{c(D)\ge\sqrt{\frac{3n}{2}}.}
\]

This is stronger than the previous attempt’s necessary bound \(c(D)>\sqrt n\). It is **not a disproof**: I do not construct a connected vertex-transitive digraph satisfying \(3n>2c(D)^2\).

# 3. Hamiltonicity for prime-sized cyclic classes

Let \(h\) denote the period of the strongly connected digraph \(D\), namely the gcd of its directed closed-walk lengths. Its cyclic decomposition is
\[
V(D)=V_0\dot\cup\cdots\dot\cup V_{h-1},
\]
with every arc going from \(V_i\) to \(V_{i+1}\), indices modulo \(h\).

One can obtain these classes by fixing a root and taking directed root-to-vertex walk lengths modulo \(h\). Appending a return walk shows that this residue is well-defined.

Every automorphism shifts all class indices by the same amount. Vertex-transitivity therefore gives
\[
|V_i|=m=n/h.
\]
It also gives constant outdegree and indegree, which are equal by counting arcs; denote their common value by \(d\).

Let \(K\) be the subgroup fixing every cyclic class setwise. It acts transitively on each \(V_i\): an automorphism sending two vertices of the same class to one another cannot shift the classes nontrivially.

For each \(i\), let \(B_i\) be the bipartite graph between a left copy of \(V_i\) and a right copy of \(V_{i+1}\), whose edges represent arcs of \(D\). Each \(B_i\) is \(d\)-regular.

We will use two elementary observations.

### Faithfulness

If, in every \(B_i\), distinct right-side vertices have distinct neighborhoods, then \(K\) acts faithfully on each \(V_i\).

Indeed, an element of \(K\) fixing \(V_i\) pointwise must fix \(V_{i+1}\) pointwise, because its vertices are distinguished by their neighborhoods in \(V_i\). Continuing around the classes fixes all vertices.

### Matching monodromy

Choose an arc-perfect-matching
\[
\sigma_i:V_i\longrightarrow V_{i+1}
\]
in each slice. Their union is a directed cycle factor. Its cycles correspond to the cycles of
\[
\Pi=\sigma_{h-1}\cdots\sigma_0
\]
on \(V_0\). In particular, if \(\Pi\) is an \(m\)-cycle, the selected arcs form a Hamilton cycle.

**Theorem 3.1.** If the cyclic class size \(m\) is prime, then \(D\) is Hamiltonian.

**Proof.** Write \(m=p\).

If \(d=1\), strong connectivity makes \(D\) a single directed cycle. If \(d=p\), every slice is complete bipartite, so its matchings can be chosen to have any desired monodromy, including a \(p\)-cycle.

Assume
\[
2\le d<p.
\]

In each \(B_i\), equality of right-side neighborhoods defines a \(K\)-invariant equivalence relation on the \(p\)-element set \(V_{i+1}\). Transitivity implies that all equivalence classes have the same size. Since \(p\) is prime, either all neighborhoods are distinct or all are identical.

The latter is impossible: if all right-side neighborhoods were identical, each left-side degree would be either \(0\) or \(p\), contrary to \(0<d<p\). Thus the faithfulness observation applies.

Consequently \(K\) embeds faithfully into \(S_p\). Its transitivity implies \(p\mid |K|\), so Cauchy’s theorem supplies an element \(a\in K\) of order \(p\). Faithfulness on every cyclic class implies that \(a\) acts as a \(p\)-cycle on every \(V_i\).

Label each \(V_i\) by \(\mathbb Z_p\), so that \(a\) acts as \(x\mapsto x+1\). Invariance under \(a\) means that there is a set \(S_i\subseteq\mathbb Z_p\), of size \(d\), such that the arcs in the \(i\)-th slice are exactly
\[
(i,x)\longrightarrow(i+1,x+s),\qquad s\in S_i.
\]

Choose one \(s_i\in S_i\) in each slice and take the corresponding translation matching. Its monodromy is
\[
x\longmapsto x+\sum_{i=0}^{h-1}s_i.
\]
Since some \(S_i\) has at least two elements, varying that choice gives at least two possible sums. At least one is nonzero. A nonzero translation of \(\mathbb Z_p\) is a \(p\)-cycle, so this choice yields a Hamilton cycle. ∎

This argument does not assume that \(D\) is a Cayley digraph.

# 4. Cyclic classes of size four

Here all remaining degrees can also be handled.

**Theorem 4.1.** If every cyclic class has size four, then \(D\) is Hamiltonian.

**Proof.** The cases \(d=1\) and \(d=4\) were handled above. It remains to consider \(d=2,3\).

## 4.1 Degree two

Each \(B_i\) is a simple \(2\)-regular bipartite graph on eight vertices. It is therefore either
\[
C_8\qquad\text{or}\qquad C_4\dot\cup C_4.
\]
All slices have the same type: an automorphism sending a vertex of \(V_0\) to a vertex of \(V_1\) shifts every cyclic class forward by one.

### Case A: every slice is \(C_4\dot\cup C_4\)

Consider the bipartite graph with copies \(V_{\mathrm{out}}\) and \(V_{\mathrm{in}}\), whose edges are \(u_{\mathrm{out}}v_{\mathrm{in}}\) for arcs \(u\to v\). All its components are \(K_{2,2}\).

Make a directed multigraph \(Q\) whose vertices are these components. For \(v\in V(D)\), let \(I(v)\) be the component containing \(v_{\mathrm{in}}\), and \(O(v)\) the component containing \(v_{\mathrm{out}}\). Introduce an arc
\[
e_v:I(v)\longrightarrow O(v)
\]
in \(Q\).

Every vertex of \(Q\) has indegree and outdegree two. Moreover,
\[
u\to v\text{ in }D
\quad\Longleftrightarrow\quad
O(u)=I(v),
\]
because each bipartite component is complete. Thus \(D\) is the line digraph of \(Q\).

Strong connectivity of \(D\) implies strong connectivity of \(Q\). The balanced digraph \(Q\) has a directed Euler tour, obtained by the usual closed-trail splicing argument. Listing its arcs in Euler-tour order gives a Hamilton cycle of \(D\).

### Case B: every slice is \(C_8\)

The class-preserving automorphism group of a bipartite \(8\)-cycle is a dihedral group of order eight. A subgroup acting transitively on both parts must contain a rotation of order four.

For completeness, write this dihedral group as
\[
\langle r,s:r^4=s^2=1,\ srs=r^{-1}\rangle,
\]
where \(r\) rotates the \(8\)-cycle by two edges. A transitive subgroup has order divisible by four. If it has order eight, it contains \(r\). If it has order four but contains no element of order four, it is one of
\[
\langle r^2,s\rangle,\qquad \langle r^2,rs\rangle.
\]
Each of these Klein four groups is intransitive on one of the two bipartition classes.

Distinct vertices on either side of \(C_8\) have distinct neighborhoods. Hence \(K\) acts faithfully on every cyclic class and on each slice. Applying the preceding observation to its action on one slice gives \(a\in K\) of order four. Faithfulness on every class means that \(a\) acts as a \(4\)-cycle on each \(V_i\).

Label every class by \(\mathbb Z_4\) so that \(a\) acts as translation by one. The arcs in slice \(i\) then have the form
\[
(i,x)\longrightarrow(i+1,x+p_i),\qquad
(i,x)\longrightarrow(i+1,x+q_i).
\]
Since the slice is connected, \(q_i-p_i\) is odd. Indeed, alternating two-step walks between left vertices generate translation by \(q_i-p_i\); an even difference would split the slice into two \(4\)-cycles.

Choose either \(p_i\) or \(q_i\) in each slice. Changing one choice changes the parity of their sum. Thus the translation-matchings can be chosen so that their monodromy is translation by an odd element of \(\mathbb Z_4\). That is a \(4\)-cycle, yielding a Hamilton cycle of \(D\).

## 4.2 Degree three

If \(h=1\), the digraph is the complete loopless digraph on four vertices and is Hamiltonian. Assume \(h\ge2\).

In each slice, the missing arcs form a perfect matching. Label the classes successively so that the missing matching is the identity in the first \(h-1\) slices, and is some permutation \(F\in S_4\) in the final slice.

An allowed perfect matching is then a derangement in each of the first \(h-1\) slices, and has the form \(F\delta\), with \(\delta\) a derangement, in the final slice. Thus the possible monodromies are
\[
F\delta_{h-1}\cdots\delta_0.
\]

Every permutation of four points is a product of two derangements. Here is a short proof. Given \(\pi\in S_4\), seek a permutation \(\beta\) satisfying
\[
\beta(i)\ne i,\qquad \beta(i)\ne\pi(i)
\quad\text{for all }i.
\]
In the corresponding allowed bipartite graph, every row has degree at least two. Hall’s condition holds for sets of at most two rows. For any set of at least three rows, every column has an allowed neighbor, because a column is forbidden in at most two rows. Hence such a \(\beta\) exists. Then
\[
\alpha=\pi\beta^{-1}
\]
is also a derangement, and \(\pi=\alpha\beta\).

Since \(h\ge2\), fixing all but two of the \(\delta_i\)’s shows that the possible monodromies fill \(S_4\). In particular, one is a \(4\)-cycle. The corresponding cycle factor is Hamiltonian. ∎

Combining this with Theorem 3.1 and the trivial \(m=1\) case proves Hamiltonicity whenever \(m\le5\), and whenever \(m\) is prime.

# 5. Scope and remaining gap

The Hamiltonicity conclusion cannot simply be extended to arbitrary cyclic class sizes. For example, the digraph on \(\mathbb Z_6\) with arcs
\[
x\longrightarrow x+2,\qquad x\longrightarrow x+3
\]
is connected and vertex-transitive but not Hamiltonian.

Indeed, a directed cycle of length six using \(a\) steps of size two and \(6-a\) steps of size three would require
\[
2a+3(6-a)\equiv0\pmod6,
\]
so \(a\equiv0\pmod6\). Thus all steps would have the same size, and neither step size traverses six distinct vertices. On the other hand,
\[
0\to2\to5\to1\to4\to0
\]
is a \(5\)-cycle. Its circumference is therefore five, so it satisfies the intersection conjecture. Its period is one, since it has directed cycles of lengths two and three.

The unresolved part of the original question remains substantial:

- The arguments above do not settle general aperiodic digraphs of composite order, or general periodic digraphs with composite cyclic class size at least six.
- If \(c>n/2\), intersection follows immediately by counting vertices.
- An affirmative solution must now, by Theorem 2.3, imply
  \[
  c\ge\sqrt{3n/2}.
  \]
  I neither establish this bound unconditionally nor construct a digraph violating it.
- No general intersection argument is obtained in the range
  \[
  \sqrt{3n/2}\le c\le n/2.
  \]

Thus the general conjecture remains unresolved here, but the prime-class and four-class cases are completely covered, and the obstruction from automorphic averaging is strengthened using an additional constraint specific to longest directed cycles.