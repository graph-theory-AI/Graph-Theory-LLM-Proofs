```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Recognizing the required triangle-free-induced-subgraph condition is Π₂^P-complete even for 4-chromatic K₄-free graphs whose triangles are vertex-disjoint.",
  "would_publish": false,
  "caveats": "This does not settle unbounded chromatic number; novelty of the complexity classification has not been checked."
}
```

# 1. Statement of the partial result

For a graph \(G\), write
\[
p(G)=\max\{\chi(G[X]):X\subseteq V(G),\ G[X]\text{ is triangle-free}\}.
\]
The question asks whether
\[
\{G:\omega(G)=3,\ p(G)\le 3\}
\]
has unbounded chromatic number.

I do not resolve that question. Instead, I establish an unconditional complexity classification of its hereditary condition. This takes a different route from the supplied finite Paley-graph example.

## Theorem
The recognition problem
\[
\text{given }G,\quad\text{decide whether }p(G)\le 3
\]
is \(\Pi_2^{\mathrm P}\)-complete.

Hardness holds even when:

1. \(\chi(G)=4\);
2. all triangles of \(G\) are vertex-disjoint, and there is at least one triangle, so \(\omega(G)=3\);
3. a proper \(4\)-coloring is supplied with the input.

The reduction below is explicit and uses only constant-sized gadgets.

Here, \(\Pi_2^{\mathrm P}\) is the class described by a polynomially bounded universal quantifier followed by a polynomially bounded existential quantifier, with a polynomial-time verification predicate.

### Membership in \(\Pi_2^{\mathrm P}\)

The property \(p(G)\le3\) is equivalent to
\[
\forall X\subseteq V(G)\ \exists c:V(G)\to\{1,2,3\}:
\quad
\bigl(G[X]\text{ contains a triangle}\bigr)
\ \lor\
\bigl(c|_X\text{ is proper}\bigr).
\]
The predicate is polynomial-time checkable. Thus recognition belongs to \(\Pi_2^{\mathrm P}\).

The rest of the proof establishes hardness.

# 2. Two fixed triangle-free coloring gadgets

We need equality and inequality constraints for \(3\)-colorings, without introducing triangles. Their behavior when a terminal is deleted is also important.

## 2.1 An equality gadget

Let \(M\) be the Mycielskian of \(C_5\). Its vertices are
\[
v_0,\ldots,v_4,\qquad u_0,\ldots,u_4,\qquad w,
\]
with indices modulo \(5\), and its edges are
\[
v_iv_{i+1},\qquad u_iv_{i-1},\qquad u_iv_{i+1},\qquad wu_i.
\]

The graph \(M\) is triangle-free. Indeed, the \(u_i\) form a stable set, the neighborhood of \(w\) is stable, and the two original neighbors of each \(u_i\) are nonadjacent.

Also, \(M\) is not \(3\)-colorable. To verify this directly, suppose it has a proper \(3\)-coloring with \(w\) colored \(3\). Every \(u_i\) then has color \(1\) or \(2\). In the coloring of the original \(C_5\), replace the color of each \(v_i\) colored \(3\) by the color of \(u_i\). This produces a proper \(2\)-coloring of \(C_5\): whenever \(v_i\) is recolored, \(u_i\) is adjacent to both of its original neighbors. This is impossible.

Define
\[
E=M-wu_0,
\]
with marked terminals \(w,u_0\).

The graph \(E\) has a proper \(3\)-coloring:
\[
c(w)=3,\qquad
(c(v_0),\ldots,c(v_4))
=(c(u_0),\ldots,c(u_4))
=(3,1,2,1,2).
\]

Consequently:

- in every proper \(3\)-coloring of \(E\), its terminals have the same color, since otherwise the deleted edge could be restored;
- any prescribed common terminal color extends to a proper \(3\)-coloring, by permuting the displayed coloring.

Thus \(E\) realizes exactly the equality relation on its two terminal colors.

The terminals are nonadjacent and have no common neighbor:
\[
N_E(w)=\{u_1,u_2,u_3,u_4\},\qquad
N_E(u_0)=\{v_1,v_4\}.
\]

## 2.2 An inequality gadget

Take a copy of \(E\), rename its terminals \(a,z\), and add a new vertex \(b\) adjacent only to \(z\). Call the resulting graph \(I\), with terminals \(a,b\).

In a proper \(3\)-coloring,
\[
c(a)=c(z)\ne c(b).
\]
Conversely, any prescribed distinct colors on \(a,b\) extend to a proper \(3\)-coloring of \(I\).

Thus \(I\) realizes exactly inequality.

Again, \(I\) is triangle-free, its terminals are nonadjacent, and no internal vertex is adjacent to both terminals: the only neighbor of \(b\) inside \(I\) is \(z\), and \(az\notin E(I)\).

## 2.3 Two extension facts

Both gadgets have the following useful properties.

**Terminal deletion.** If either terminal is deleted, any prescribed color on the remaining terminal extends to a proper \(3\)-coloring of what remains.

To see this, temporarily give the missing terminal a color satisfying the gadget’s equality or inequality relation, extend to the full gadget, and then delete that terminal.

**Four-color extension.** With colors drawn from a set of four colors, prescribed equal terminal colors for \(E\), or prescribed distinct terminal colors for \(I\), extend to a proper coloring using those four colors.

This follows by choosing three of the four colors containing the prescribed terminal colors and applying the preceding \(3\)-color extension property.

All gadget copies used below have pairwise disjoint interiors.

# 3. Encoding a quantified formula by coloring constraints

Start with an instance
\[
\forall x_1,\ldots,x_m\ \exists y_1,\ldots,y_n\quad
\Phi(x_1,\ldots,x_m,y_1,\ldots,y_n),
\tag{1}
\]
where \(\Phi\) is a \(3\)-CNF formula.

This is the canonical \(\Pi_2^{\mathrm P}\)-complete problem. Equivalently, its completeness follows from the definition of \(\Pi_2^{\mathrm P}\) by encoding the polynomial-time verification circuit as a \(3\)-CNF and placing the auxiliary variables in the existential block.

We may assume \(m\ge1\), by adding an unused universal variable.

## 3.1 Converting clauses to not-all-equal constraints

Let \(\operatorname{NAE}(a,b,c)\) mean that the three Boolean values are not all equal. For Boolean \(a,b,c\),
\[
a\lor b\lor c
\quad\Longleftrightarrow\quad
\exists z\,
\bigl(
\operatorname{NAE}(a,b,z)
\land
\operatorname{NAE}(\neg z,c,\mathrm{false})
\bigr).
\tag{2}
\]

For completeness:

- if \(a=b=\mathrm{false}\), the first constraint forces \(z=\mathrm{true}\), and the second then forces \(c=\mathrm{true}\);
- if \(a=b=\mathrm{true}\), choose \(z=\mathrm{false}\), and the second constraint is automatic;
- if \(a\ne b\), the first constraint is automatic, and \(z\) can be chosen to satisfy the second.

Apply (2) separately to every clause, using a fresh existential auxiliary variable \(z\).

## 3.2 A logical graph \(L_\Phi\)

First construct a graph expressing these constraints by ordinary \(3\)-coloring. Its edges will subsequently be replaced by triangle-free gadgets.

Introduce palette vertices
\[
\mathsf T,\mathsf F,\mathsf B
\]
forming a triangle. In a \(3\)-coloring, identify their three colors with their names.

For every Boolean variable \(q\), including auxiliary variables, introduce vertices \(q,\bar q\), with edges
\[
q\bar q,\qquad q\mathsf B,\qquad \bar q\mathsf B.
\]
Thus \(q,\bar q\) receive opposite colors \(\mathsf T,\mathsf F\).

For each NAE constraint with input vertices \(a,b,c\), introduce a triangle \(t_1t_2t_3\), together with edges
\[
t_1a,\qquad t_2b,\qquad t_3c.
\]
The constant false is represented by the palette vertex \(\mathsf F\).

This triangle extends to a \(3\)-coloring exactly when the Boolean input colors are not all equal:

- if all inputs have the same color, every \(t_j\) is restricted to the same two colors;
- if both Boolean colors occur, assign color \(\mathsf F\) to a triangle vertex whose input is \(\mathsf T\), color \(\mathsf T\) to one whose input is \(\mathsf F\), and color \(\mathsf B\) to the remaining vertex.

Finally, for each universal variable \(x_i\), introduce a vertex \(r_i\) adjacent to \(\bar x_i\).

Prescribing the color of \(r_i\) has the following effect:
\[
\begin{array}{c|c}
c(r_i)&\text{constraint on }x_i\\ \hline
\mathsf T&x_i=\mathrm{true}\\
\mathsf F&x_i=\mathrm{false}\\
\mathsf B&\text{no constraint}.
\end{array}
\tag{3}
\]

This completes \(L_\Phi\).

By the verified gadgets and (2), a \(3\)-coloring of \(L_\Phi\) with prescribed colors on the \(r_i\) exists exactly when the corresponding partial assignment in (3) can be completed to satisfy \(\Phi\).

# 4. Constructing the graph \(G_\Phi\)

The vertices already in \(L_\Phi\) will be called external vertices.

1. Replace every edge \(ab\) of \(L_\Phi\) by a fresh copy of the inequality gadget \(I\), identifying its terminals with \(a,b\). Delete the original edge.

2. For each \(i\), introduce three additional external vertices
   \[
   s_i^{\mathsf T},\quad s_i^{\mathsf F},\quad s_i^{\mathsf B},
   \]
   and make them a triangle.

3. For each \(d\in\{\mathsf T,\mathsf F,\mathsf B\}\), put an equality gadget \(E\) between \(s_i^d\) and the palette vertex \(d\).

4. Put an inequality gadget \(I\) between \(r_i\) and each of
   \[
   s_i^{\mathsf T},\ s_i^{\mathsf F},\ s_i^{\mathsf B}.
   \]

This defines \(G_\Phi\). Its size is linear in the size of the logical construction, since \(E\) and \(I\) are fixed graphs.

## Lemma 1
The only triangles of \(G_\Phi\) are
\[
s_i^{\mathsf T}s_i^{\mathsf F}s_i^{\mathsf B},
\qquad 1\le i\le m.
\]

### Proof
Among external vertices, the only edges left are the edges of these selector triangles.

Suppose a triangle contains an internal vertex of a gadget. Its other two vertices must belong to that same gadget, since gadget interiors have no outside neighbors. The triangle cannot lie entirely in the gadget, which is triangle-free.

The only remaining possibility is that its other two vertices are the gadget’s terminals, joined by an external edge. But no internal vertex of either gadget is adjacent to both terminals. This is also impossible. ∎

In particular, the triangles are vertex-disjoint and
\[
\omega(G_\Phi)=3.
\]

# 5. Canonical triangle-free induced subgraphs

For
\[
\tau=(\tau_1,\ldots,\tau_m)
\in\{\mathsf T,\mathsf F,\mathsf B\}^{m},
\]
define
\[
G_\Phi^\tau
=
G_\Phi-\{s_i^{\tau_i}:1\le i\le m\}.
\]

By Lemma 1, every \(G_\Phi^\tau\) is triangle-free.

Conversely, every triangle-free induced subgraph of \(G_\Phi\) is contained in some \(G_\Phi^\tau\): from each selector triangle, choose a vertex absent from that subgraph.

It follows that
\[
p(G_\Phi)\le3
\quad\Longleftrightarrow\quad
\chi(G_\Phi^\tau)\le3
\text{ for every }\tau.
\tag{4}
\]

## Lemma 2
The graph \(G_\Phi^\tau\) is \(3\)-colorable if and only if \(L_\Phi\) has a proper \(3\)-coloring in which
\[
c(r_i)=c(\tau_i)
\qquad(1\le i\le m),
\tag{5}
\]
where \(\tau_i\) denotes its corresponding palette vertex.

### Proof
Consider a \(3\)-coloring of \(G_\Phi^\tau\).

The gadgets replacing edges of \(L_\Phi\) enforce all inequalities of \(L_\Phi\). In particular, the palette vertices have three different colors.

The two surviving selector vertices for index \(i\) are forced by their equality gadgets to receive their named palette colors. Their inequality gadgets to \(r_i\) then force \(r_i\) to receive the third palette color, namely \(\tau_i\). Restriction to \(V(L_\Phi)\) gives the required coloring.

Conversely, suppose such a coloring of \(L_\Phi\) is given. Give each surviving selector vertex its named palette color. Every complete equality or inequality gadget now has terminal colors satisfying its relation, and therefore extends.

A gadget incident with the deleted selector vertex has only one terminal remaining. The terminal-deletion property from Section 2.3 supplies its extension. The interiors of all gadgets are disjoint, so these extensions are compatible. ∎

## Correctness of the reduction

Suppose (1) is true. Take any ternary choice \(\tau\).

Set \(x_i\) according to \(\tau_i\) whenever \(\tau_i\in\{\mathsf T,\mathsf F\}\). Complete the remaining \(x_i\) arbitrarily. By (1), there is an assignment to the \(y_i\) satisfying \(\Phi\). Consequently \(L_\Phi\) has the coloring required in Lemma 2, and \(G_\Phi^\tau\) is \(3\)-colorable.

Equation (4) gives \(p(G_\Phi)\le3\).

Conversely, suppose (1) is false. Choose a Boolean assignment to the universal variables for which no existential assignment satisfies \(\Phi\). Let \(\tau_i\) be \(\mathsf T\) or \(\mathsf F\) according to that assignment.

By (3), no coloring required in Lemma 2 exists. Thus \(G_\Phi^\tau\) is a triangle-free induced subgraph that is not \(3\)-colorable.

We have proved
\[
p(G_\Phi)\le3
\quad\Longleftrightarrow\quad
\forall x\ \exists y\ \Phi(x,y).
\tag{6}
\]

This establishes \(\Pi_2^{\mathrm P}\)-hardness.

# 6. Every output graph is exactly \(4\)-chromatic

It remains to verify the promised chromatic restriction independently of the truth of the formula.

## Lower bound

In a hypothetical \(3\)-coloring of the full graph \(G_\Phi\), a selector triangle uses all three colors. The three inequality gadgets from that triangle to \(r_i\) force \(r_i\) to differ from all three colors. This is impossible.

Thus
\[
\chi(G_\Phi)\ge4.
\]

## Upper bound

Here is an explicit \(4\)-coloring procedure.

First assign colors to the external vertices:

- give \(\mathsf T,\mathsf F,\mathsf B\) colors \(1,2,3\), respectively;
- for every Boolean variable \(q\), give \(q,\bar q\) colors \(1,2\), respectively;
- give every \(r_i\) color \(4\);
- in each logical NAE triangle \(t_1t_2t_3\), give \(t_1,t_2\) colors \(3,4\), and give \(t_3\) whichever of \(1,2\) differs from its input’s color;
- give \(s_i^{\mathsf T},s_i^{\mathsf F},s_i^{\mathsf B}\) colors \(1,2,3\).

Every NAE input has color \(1\) or \(2\). Therefore the assignment just described is proper on all edges of the logical graph \(L_\Phi\), regardless of whether its NAE constraints are Boolean-satisfiable.

Moreover:

- every equality gadget has equally colored terminals;
- every inequality gadget has differently colored terminals;
- every actual selector triangle is properly colored.

The four-color extension property from Section 2.3 extends this assignment through every gadget. Hence
\[
\chi(G_\Phi)\le4.
\]

Therefore
\[
\boxed{\chi(G_\Phi)=4,\qquad \omega(G_\Phi)=3.}
\]

The coloring is polynomial-time constructible and may be included in the reduction’s output.

Finally, every output contains an induced \(C_5\) inside a gadget. Thus \(p(G_\Phi)\ge3\), while \(\chi(G_\Phi)=4\) gives \(p(G_\Phi)\le4\). The reduction actually distinguishes
\[
p(G_\Phi)=3
\quad\text{from}\quad
p(G_\Phi)=4.
\]

This completes the theorem.

# 7. Relation to the original question and the remaining gap

The classification concerns the exact hereditary condition in the question, rather than merely a sufficient condition such as bounded independence number. It shows that deciding this condition is already \(\Pi_2^{\mathrm P}\)-complete within a very restricted \(K_4\)-free class.

It does **not** provide chromatic amplification. Every graph in the reduction has chromatic number exactly \(4\).

There is also a simple structural reason that vertex-disjoint triangles cannot themselves furnish the requested unbounded family.

## Proposition
If all triangles of \(G\) are vertex-disjoint and \(p(G)\le3\), then
\[
\chi(G)\le6.
\]

### Proof
Choose a set \(A\) containing exactly one vertex from each triangle. Both \(G[A]\) and \(G-A\) are triangle-free: neither contains an entire triangle of \(G\). Each is therefore \(3\)-colorable. Using disjoint palettes gives \(\chi(G)\le6\). ∎

Thus computational hardness persists even in a subclass where the chromatic number is bounded under the desired condition.

The unresolved issue remains whether the full class
\[
\{G:\omega(G)=3,\ p(G)\le3\}
\]
has unbounded chromatic number. The argument above yields neither an unbounded family nor a universal chromatic upper bound for that class.