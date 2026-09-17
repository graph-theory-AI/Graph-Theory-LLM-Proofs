```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The intended conjecture holds for every properly edge-coloured target and for every colouring of K4 except, possibly, one explicit three-colour pattern.",
  "would_publish": false,
  "caveats": "These results concern the intended C-free formulation; the exceptional K4 pattern and the general higher-order case are not settled here."
}
```

## 1. Formulation and main partial result

Write \(C=(V(C),c)\) for the prescribed finite complete edge-coloured graph. A copy always means a **colour-preserving** copy.

The nontrivial saturation formulation is:

> Find a countably infinite \(C\)-free colouring \(\chi\) such that every colouring \(\chi'\ne\chi\) for which
> \[
> D=\{xy:\chi'(xy)\ne\chi(xy)\}
> \]
> is locally finite contains \(C\).

The requirement that \(\chi\) be \(C\)-free is missing from the catalog’s displayed statement. Without it, the assertion is immediate: take infinite classes indexed by \(V(C)\), with the prescribed colours between classes. A locally finite perturbation leaves an unchanged transversal copy, chosen greedily.

I address the intended \(C\)-free version and prove the following.

### Partial theorem

1. The conjecture holds whenever \(c\) is a **proper edge-colouring** of its complete graph.
2. For targets on four vertices using at least three colours, it holds except possibly for the following pattern, up to permuting vertices and colours:
   \[
   \boxed{
   \begin{aligned}
   c(14)=c(23)=c(34)&=a,\\
   c(12)=c(13)&=b,\\
   c(24)&=c.
   \end{aligned}}
   \tag{E}
   \]
   Here \(a,b,c\) are distinct colours.

The two-colour case, for targets of any order, follows from the main theorem quoted in the question.

The main construction below strengthens the supplied attempt’s connectivity condition. A further, finite rooted-profile test handles most four-vertex patterns, including the proper three-colouring of \(K_4\).

---

## 2. A rooted support criterion

For a colour \(s\), define
\[
J_s(C)=\bigl(V(C),\{uv:c(uv)\ne s\}\bigr).
\]

Call \(u,v\) **\(\ell\)-twins** if
\[
c(uv)=\ell,\qquad
c(uw)=c(vw)\quad\text{for every }w\notin\{u,v\}.
\]

### Theorem 1

Suppose \(n=|V(C)|\ge4\), and:

1. for some colour \(\ell\), \(C\) has no \(\ell\)-twins;
2. for every colour \(a\), there is a colour \(s=s(a)\) such that:
   - \(J_s(C)\) is 2-vertex-connected;
   - whenever \(c(uv)=a\), the graph \(J_s(C)-\{u,v\}\) is connected.

Then the conjecture holds for \(C\).

In particular, one 3-connected support graph \(J_s(C)\), together with the twin hypothesis, suffices. Unlike that stronger condition, the rooted criterion permits 2-separators whose endpoint colour is unsuitable for the current root edge.

### Construction

Start with a countably infinite monochromatic complete graph. It is \(C\)-free because \(C\) uses at least two colours.

An obligation consists of an existing pair \(x,y\) and a colour \(b\ne\chi(xy)\). Put
\[
a=\chi(xy).
\]
Choose a \(b\)-coloured edge \(pq\) of \(C\). Attach a bag with roots \(x,y\), representing \(p,q\), as follows.

For each \(r\in V(C)\setminus\{p,q\}\), introduce an infinite class \(W_r\). Colour:

- edges between distinct role classes, and from them to the roots, as prescribed by \(C\);
- edges within each \(W_r\) with colour \(\ell\);
- edges from the bag’s interior to every old vertex other than \(x,y\) with colour \(s(a)\).

The root edge \(xy\) retains colour \(a\), rather than its prescribed colour \(b\).

Attach one bag at each stage, processing all obligations fairly. This can be made completely explicit: label potential vertices by triples consisting of their birth stage, role and index, code obligations by natural numbers, and always process the least-coded available unprocessed obligation. Every obligation is eventually processed, since only finitely many obligations have smaller codes.

Every stage and the final union are countable.

### Each bag is \(C\)-free

Suppose a copy of \(C\) lay inside a bag. Project its vertices onto their roles.

Two vertices projecting to the same role would be \(\ell\)-twins in the copy: they have mutual colour \(\ell\) and identical colours to every other vertex of the copy. Thus the projection is injective.

There are exactly \(n\) roles and \(n\) vertices in the copy, so the projection is bijective. It would identify \(C\) with the role-level colouring obtained from \(C\) by changing \(pq\) from \(b\) to \(a\). This is impossible: the numbers of edges of colours \(a\) and \(b\) have changed.

### No forbidden copy straddles an attachment

Suppose a copy \(Q\) of \(C\) first appears after adding a bag with interior \(W\) and roots \(x,y\). Set
\[
I=V(Q)\cap W,\qquad
S=V(Q)\cap\{x,y\},\qquad
O=V(Q)\setminus(W\cup\{x,y\}).
\]

Here \(I\ne\varnothing\). If \(O=\varnothing\), the copy lies inside the bag, already ruled out.

Otherwise every edge between \(I\) and \(O\) has colour \(s=s(a)\). Consequently \(S\) separates two nonempty sets in the copy of \(J_s(C)\).

If \(|S|\le1\), this contradicts 2-connectivity. If \(|S|=2\), its two vertices have mutual colour \(a\), and the second rooted-support condition gives the contradiction.

Induction proves that every stage, and hence the union \(\chi\), is \(C\)-free.

### Local-finite robustness

Let \(\chi'\ne\chi\), with locally finite difference graph \(D\). Choose a changed edge \(xy\), where
\[
\chi(xy)=a,\qquad \chi'(xy)=b\ne a.
\]

The construction attached a bag for this obligation. Choose one vertex from each of its nonroot role classes, successively avoiding all \(D\)-neighbours of the roots and previously chosen vertices.

At every step only finitely many vertices are excluded, while the relevant class is infinite. Thus the selected vertices have no changed edge except \(xy\). That edge now has the prescribed colour \(b\), so these vertices form \(C\) in \(\chi'\). ∎

---

## 3. A stronger four-vertex attachment test

For \(K_4\), one can examine the root profiles rather than prohibit every potentially relevant 2-separator.

### A preliminary twin observation

If two coloured twin pairs overlap, their mutual colours are equal. Indeed, if \(u,v\) and \(u,w\) are twin pairs, then
\[
c(uv)=c(vw)=c(uw).
\]
Therefore twin pairs of different colours are vertex-disjoint.

On four vertices, at most two colours can occur as colours of twin pairs. Consequently:

> Every colouring of \(K_4\) using at least three colours has a colour \(\ell\) for which there are no \(\ell\)-twins.

Thus the internal-bag argument from Theorem 1 is always available in the four-vertex cases considered below.

### Root profiles

For an edge \(e=uv\), let \(e^*\) denote the edge on the other two vertices.

Write \(ab=ba\) for the two-element **multiset** of colours \(a,b\). Define
\[
\mathcal P(e)=
\bigl\{c(uw)c(vw):w\in V(C)\setminus\{u,v\}\bigr\}.
\]
Thus \(\mathcal P(e)\) records the unordered colour profiles of the two nonroot vertices.

For colours \(a,s\), put
\[
\mathcal F(a,s)=
\bigcup_{\substack{f\in E(K_4)\\c(f)=a,\ c(f^*)=s}}
\mathcal P(f).
\]

### Lemma 2: four-vertex profile criterion

Suppose that for every \(a\ne b\), there are:

- a colour \(s\) whose colour class is a matching;
- a \(b\)-coloured edge \(e\);

such that
\[
\mathcal P(e)\cap\mathcal F(a,s)=\varnothing.
\tag{1}
\]

Then the conjecture holds for \(C\).

#### Proof

Use the bag construction above, with \(e\) as the role-level root edge and \(s\) as the interface colour. Use a colour \(\ell\) with no \(\ell\)-twins.

Since the \(s\)-edges form a matching, \(J_s(C)\) is 2-connected. If a new forbidden copy straddles the bag, the separator argument therefore forces it to contain both roots.

There are only four vertices, so such a copy consists of the two roots, one new vertex and one old nonroot vertex. In the target, the root edge is some edge \(f\) of colour \(a\); its opposite edge has colour \(s\), because it crosses the interface. The new vertex’s profile therefore belongs to \(\mathcal F(a,s)\).

On the other hand, every new vertex has a root profile in \(\mathcal P(e)\). This contradicts (1). The rest of the construction and the local-finite robustness proof are unchanged. ∎

### 3.1. A perfect-matching colour always works

Suppose some colour \(s\) forms a perfect matching.

If the old root colour \(a\ne s\), then
\[
\mathcal F(a,s)=\varnothing,
\]
because every edge opposite an \(s\)-edge also has colour \(s\).

Now let \(a=s\), and let \(b\ne s\). Choose any \(b\)-edge as the role-level root edge. Each of its two nonroot vertices is the \(s\)-partner of one root. Hence every profile in \(\mathcal P(e)\) contains \(s\).

By contrast, for an \(s\)-coloured root edge of \(C\), every edge from a nonroot vertex to a root has colour different from \(s\). Thus no profile in \(\mathcal F(s,s)\) contains \(s\).

The profile test succeeds.

This settles, in particular, the proper three-colouring of \(K_4\). It also settles the pattern
\[
12,34:a,\qquad 13,14:b,\qquad 23,24:c,
\]
which has a coloured twin pair and two rainbow triangles.

### 3.2. Singleton colour classes

If \(s\) occurs on just one edge \(e_s\), then
\[
c(e_s^*)\ne a\quad\Longrightarrow\quad \mathcal F(a,s)=\varnothing.
\tag{2}
\]

Therefore, if the colours opposite the singleton colour classes are not all equal, a suitable singleton interface colour exists for every old colour \(a\).

### 3.3. Four additional certificates

The following four types need a nonempty-profile check. All colours displayed in a type are distinct.

\[
\begin{array}{c|l}
\text{Type}&\text{Colour classes}\\ \hline
A&a:14,24,34;\quad b:12,13;\quad c:23\\
B&a:23,24,34;\quad b:12,13;\quad c:14\\
C&a:14,24,34;\quad b:12;\quad c:23;\quad d:13\\
D&a:12,13,23;\quad b:14;\quad c:24;\quad d:34
\end{array}
\]

For old colours other than \(a\), (2) applies: the indicated singleton edges have \(a\)-coloured opposite edges.

For old colour \(a\), use these certificates:
\[
\begin{array}{c|c|c|c|c|c}
\text{Type}&\text{Change}&s&e&\mathcal P(e)&\mathcal F(a,s)\\ \hline
A&a\to b&c&12&\{bc,aa\}&\{ab\}\\
A&a\to c&c&23&\{bb,aa\}&\{ab\}\\
B&a\to b&c&12&\{ab,ac\}&\{aa,bb\}\\
B&a\to c&c&14&\{ab\}&\{aa,bb\}\\
C&a\to b&b&12&\{cd,aa\}&\{ac,ad\}\\
D&a\to b&b&14&\{ac,ad\}&\{aa,cd\}
\end{array}
\]
Every displayed intersection is empty. In Types \(C,D\), the calculations for \(a\to c\) and \(a\to d\) follow by permuting the three singleton colours and their corresponding vertices.

This covers every colour change for all four types.

---

## 4. Two lexicographic constructions

Two remaining four-vertex types are more conveniently handled without bags.

### 4.1. A rainbow triangle with a monochromatically joined vertex

Let \(C\) consist of a rainbow triangle in colours \(a,b,c\), together with a vertex joined to all three triangle vertices in colour \(a\).

Take
\[
X=\{x\in\{0,1\}^{\mathbb Z}:x_i=0\text{ for all but finitely many }i\}.
\]
Choose a periodic sequence \((\gamma_i)_{i\in\mathbb Z}\) containing all three colours. For distinct \(x,y\), set
\[
m(x,y)=\min\{i:x_i\ne y_i\},\qquad
\chi(xy)=\gamma_{m(x,y)}.
\]

The set \(X\) is countable. The colouring has no rainbow triangle: at the first coordinate where three sequences are not all equal, two of the three edges receive the same colour. In particular, it is \(C\)-free.

Suppose \(xy\) changes from \(r\) to \(t\), and let \(u\) be the third colour. For infinitely many \(j>m(x,y)\), one has \(\gamma_j=u\). Toggling the \(j\)-th coordinate of \(x\) gives a vertex \(z\) with
\[
\chi(xz)=u,\qquad \chi(yz)=r.
\]
Choose such a \(z\) avoiding the finitely many changed edges incident with \(x\) or \(y\). Then \(x,y,z\) form a rainbow triangle after the perturbation.

There are infinitely many sufficiently negative coordinates \(i\) with \(\gamma_i=a\), lying below every nonzero coordinate of \(x,y,z\). The vertex supported only at \(i\) is joined to all three in colour \(a\). Choose one avoiding all changed edges incident with the triangle.

This gives \(C\). Notice that the first part of the argument also proves saturation for the rainbow triangle itself.

### 4.2. The cyclic three-coloured tetrahedron

Use colours \(0,1,2\), and let \(C\) have vertices \(0,1,2,\infty\), with
\[
c(01)=0,\qquad c(12)=1,\qquad c(20)=2,
\qquad c(i\infty)=i.
\tag{3}
\]

Let \(\tau\) be the rainbow colouring of the three-symbol alphabet:
\[
\tau(0,1)=0,\qquad \tau(1,2)=1,\qquad \tau(2,0)=2.
\]

Put \(\alpha_i=i\bmod3\), and take
\[
X=\{x\in\{0,1,2\}^{\mathbb N}:x_i=\alpha_i
\text{ for all but finitely many }i\}.
\]
For distinct \(x,y\), colour \(xy\) by
\[
\chi(xy)=\tau(x_m,y_m),
\qquad m=\min\{i:x_i\ne y_i\}.
\]

The periodic default word matters: it ensures that every vertex has arbitrarily close alternatives in every colour.

More precisely, for every \(x\), colour \(t\), and \(M\), there are infinitely many \(z\) such that
\[
m(x,z)>M,\qquad \chi(xz)=t.
\tag{4}
\]
Indeed, at infinitely many sufficiently large coordinates, \(x_i=\alpha_i\) is an endpoint of the alphabet edge of colour \(t\); change just that coordinate to its other endpoint.

#### The original colouring is \(C\)-free

The target (3) has neither a coloured twin pair nor a vertex joined monochromatically to the other three.

For any four vertices of \(X\), inspect their first coordinate at which they are not all equal. They occupy two or three alphabet classes.

- If a class has size two, those two vertices are coloured twins within the four-vertex set.
- Otherwise the partition has sizes \(3+1\), and the singleton is joined monochromatically to the other three.

Thus these four vertices cannot induce (3).

#### Every locally finite perturbation creates \(C\)

Choose a changed edge. By cyclically shifting the indices in the following argument, it suffices to describe an old colour \(0\). At the first differing coordinate \(m\), orient the roots so that \(x_m=0\), \(y_m=1\).

**If the new colour is \(1\):**

Choose \(z\) in the third alphabet branch at coordinate \(m\), so
\[
\chi(xz)=2,\qquad \chi(yz)=1.
\]
There are infinitely many choices for \(z\).

Next choose \(w\) arbitrarily close to \(x\), beyond coordinate \(m\), with \(\chi(xw)=0\). Then
\[
\chi(yw)=0,\qquad \chi(zw)=2.
\]
After the change, the correspondence
\[
0\mapsto w,\quad 1\mapsto y,\quad
2\mapsto z,\quad \infty\mapsto x
\]
gives (3).

**If the new colour is \(2\):**

Choose \(u\) close to \(y\), beyond coordinate \(m\), with
\[
\chi(yu)=1.
\]
Then choose \(v\) still closer to \(y\), beyond the first difference between \(u,y\), with
\[
\chi(yv)=2.
\]
Consequently
\[
\chi(uv)=1,\qquad
\chi(xu)=\chi(xv)=0.
\]
After the change, use
\[
0\mapsto x,\quad 1\mapsto u,\quad
2\mapsto y,\quad \infty\mapsto v.
\]

In each case, the choices are infinite at every step, by the branch structure and (4). Choose each new vertex outside the \(D\)-neighbourhoods of all previously selected vertices. All required edges other than the chosen root edge are then unchanged. ∎

---

## 5. Exhaustive reduction of the four-vertex cases

Here is a complete finite case analysis establishing the four-vertex part of the partial theorem. It uses no computational enumeration.

There are six edges, so the possible numbers and multiplicities of colour classes are limited.

### Three colours

The multiplicity partitions are
\[
(4,1,1),\qquad (3,2,1),\qquad (2,2,2).
\]

#### Multiplicities \((4,1,1)\)

If the two singleton edges are opposite, their opposite colours differ, so §3.2 applies.

If they are adjacent, the target is a rainbow triangle together with a vertex joined monochromatically to it. Section 4.1 applies.

#### Multiplicities \((3,2,1)\)

If the size-two colour class is a matching, §3.1 applies.

Otherwise label its edges \(12,13\), with colour \(b\). Up to exchanging vertices \(2,3\), the singleton edge is one of:
\[
23,\qquad14,\qquad24.
\]

- Singleton \(23\) gives Type \(A\).
- Singleton \(14\) gives Type \(B\).
- Singleton \(24\) gives exactly the exceptional pattern (E).

Thus precisely one isomorphism type remains uncovered in this multiplicity class.

#### Multiplicities \((2,2,2)\)

If any colour class is a matching, §3.1 applies.

Otherwise each colour class is two adjacent edges. Their three centres are distinct: one vertex cannot be the centre of two such colour classes, since that would require four incident edges.

Let \(v\) be the fourth vertex. Its three incident edges have distinct colours, and the edge of each colour joins \(v\) to that colour’s centre. The remaining three edges therefore form a cyclically coloured triangle on the centres. This is exactly the target in §4.2.

### Four colours

The multiplicities are
\[
(3,1,1,1)\quad\text{or}\quad(2,2,1,1).
\]

#### Multiplicities \((3,1,1,1)\)

If two singleton edges are opposite, §3.2 applies.

Otherwise the three singleton edges form a star or a triangle. The target is respectively Type \(D\) or Type \(C\).

#### Multiplicities \((2,2,1,1)\)

A matching colour class is handled by §3.1.

Assume neither size-two class is a matching, and let the singleton edges be \(e,f\). Their opposite edges have different colours:

- if \(e,f\) are opposite, this is immediate;
- otherwise, if \(e^*,f^*\) had the same colour, the two remaining edges would be an opposite pair of the other repeated colour, contrary to the assumption.

Thus §3.2 applies.

### Five or six colours

There are at least four singleton colour classes, and every colour class has size at most two.

For any old colour \(a\), not all edges opposite the singleton classes can have colour \(a\): these are at least four distinct edges. Hence a singleton interface satisfying (2) exists for every old colour.

This completes the classification, with (E) as the sole uncovered four-vertex target using at least three colours.

---

## 6. Every properly edge-coloured target

It remains to justify the first part of the partial theorem for arbitrary order.

- For \(n=3\), the target is a rainbow triangle, handled in §4.1.
- For \(n=4\), if a colour repeats, it is a perfect matching, handled by §3.1. Otherwise all six colours are distinct, and §3.2 applies.
- Let \(n\ge5\). Every colour class is a matching. Hence \(J_s(C)\) is \(K_n\) with a matching removed.

Deleting at most two vertices from \(J_s(C)\) leaves a complete graph on at least three vertices with a matching removed, which is connected. Thus \(J_s(C)\) is 3-connected.

Also, no pair of vertices is a coloured twin pair: for distinct \(u,v,w\), properness gives
\[
c(uw)\ne c(vw).
\]
Theorem 1 therefore applies. ∎

---

## 7. The remaining gap

For the exceptional pattern (E), the obstruction to these attachment tests is explicit.

- \(J_a(C)\) is the path with edges \(12,13,24\), so it is not 2-connected.
- \(J_b(C)\) has vertex \(1\) of degree one.
- \(J_c(C)=K_4-24\), whose separating pair \(13\) has colour \(b\).

Thus Theorem 1 gives no interface for old colour \(b\).

The finer profile test also fails for the change \(b\to c\). The unique \(c\)-edge is \(24\), and
\[
\mathcal P(24)=\{ab,aa\}
=\mathcal F(b,c).
\]
The other two colour classes are not matchings, so Lemma 2 offers no alternative interface.

This is a limitation of the argument, **not a counterexample**. I have not constructed a saturation colouring for (E), nor proved that none exists. General larger targets failing the rooted criteria also remain unresolved here. No claim is made about subsequent literature resolving any of these remaining cases.