```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For Steiner triple systems obtained by three disjoint Fano switches in a binary projective system, universality is equivalent to the three switch centers forming a projective line.",
  "would_publish": false,
  "caveats": "This classifies only a restricted family; novelty relative to the point-intransitive constructions mentioned in the question has not been checked."
}
```

# A characterization for three disjoint Fano switches

I do not characterize arbitrary universal Steiner triple systems. I prove an exact characterization for a family of switched projective systems.

The balloon-palette argument suggested by the previous attempt is valid and is verified below. The additional step is a **sufficiency argument**: with exactly three disjoint switches, the balloon obstruction is the only obstruction to universality.

The only external theorem used is the standard nowhere-zero \(\mathbb F_2^3\)-flow theorem underlying the Fano-plane discussion in the question. In particular, a bridgeless graph with all degrees two or three has an edge assignment of nonzero vectors of \(\mathbb F_2^3\) whose sum at each vertex is zero.

## 1. Construction and theorem

Let \(V\) be a binary vector space of dimension \(d\geq 6\). The projective Steiner triple system on
\[
P=V\setminus\{0\}
\]
has blocks
\[
\{x,y,x+y\},\qquad x\ne y.
\]

Choose three three-dimensional subspaces
\[
U_1,U_2,U_3\leq V,\qquad U_i\cap U_j=\{0\}\quad(i\ne j),
\]
and distinguished points
\[
a_i\in U_i\setminus\{0\}.
\]

For each \(i\), replace the four Fano blocks in \(U_i\setminus\{0\}\) that avoid \(a_i\) by the four triples
\[
\{x,y,z\}\subseteq U_i\setminus\{0,a_i\},
\qquad x+y+z=a_i.
\]
Call the resulting system \(S\).

This is an STS: within \(U_i\setminus\{0\}\), the replacement is the relabeling
\[
a_i\longmapsto a_i,\qquad x\longmapsto x+a_i\quad(x\ne 0,a_i)
\]
of its Fano plane. The three replacements have disjoint point sets.

Equivalently, for distinct points \(x,y\), the third point of their block is
\[
x*_S y=
\begin{cases}
x+y+a_i,
&x,y\in U_i\setminus\{0,a_i\},\quad x+y\ne a_i,\\
x+y,&\text{otherwise}.
\end{cases}                                                     \tag{1}
\]

Let \(D\) be the one-ended graph obtained by subdividing one edge of \(K_4\) and attaching a dangling edge at the subdivision vertex. Let \(H\) be the simple cubic graph formed from three copies of \(D\) by identifying their dangling ends at one new vertex. Thus \(H\) has \(16\) vertices.

**Theorem.** The following are equivalent:

1. \(S\) is universal.
2. \(H\) is \(S\)-edge-colorable.
3. \(a_1+a_2+a_3=0\).

In particular, this gives explicitly specified universal, point-intransitive STS of orders \(63,127,\) and \(255\), each with no proper universal subsystem.

The implication \(1\Rightarrow2\) is immediate. We first prove \(2\Rightarrow3\), and then the substantive implication \(3\Rightarrow1\).

## 2. The exact balloon palette

For an STS \(T\), define
\[
\beta(T)=\{p:\ D\text{ has a \(T\)-coloring with dangling-edge color }p\}.
\]

By construction,
\[
H\text{ is \(T\)-colorable}
\quad\Longleftrightarrow\quad
\beta(T)\text{ contains a block of }T.                         \tag{2}
\]

For the switched system above, write
\[
A=\{a_1,a_2,a_3\}.
\]

**Lemma 1.**
\[
\beta(S)=A.
\]
Moreover, every coloring of \(D\) with dangling-edge color \(a_i\) uses at least one block inserted by switch \(i\).

### Each center occurs

Label the original vertices of \(K_4\) by \(u,v,r,s\), with \(uv\) subdivided by \(w\).

Fix \(i\), choose \(x,y\in U_i\) such that \(a_i,x,y\) are linearly independent, and choose \(z\notin U_i\). Assign
\[
\begin{array}{lll}
c(ur)=x, &c(us)=y, &c(rs)=z,\\
c(vr)=x+z, &c(vs)=y+z,\\
c(uw)=x+y+a_i, &c(vw)=x+y,
\end{array}
\]
and give the dangling edge color \(a_i\).

At \(u\), the three colors form an inserted block of switch \(i\). At \(w\), they form a retained line through \(a_i\). Each remaining vertex receives an unchanged projective line: its colors include a nonzero point of \(U_i\) and a point outside \(U_i\), so its block cannot lie in any switching subspace. This proves \(a_i\in\beta(S)\).

### No other color occurs

Consider a coloring of \(D\), with dangling-edge color \(q\). Call an internal vertex **of type \(i\)** if its block was inserted by switch \(i\).

At a type-\(i\) vertex, the binary sum of its incident colors is \(a_i\). At every other vertex, that sum is zero. Summing over the five internal vertices gives
\[
q=\sum_i n_i a_i,                                           \tag{3}
\]
where \(n_i\) counts type-\(i\) vertices modulo two.

Adjacent vertices cannot have different types, because their common edge color would have to belong to two disjoint switching point sets. The internal graph of \(D\) has independence number two. Consequently, at most two types occur.

If exactly one type has odd multiplicity, (3) gives the corresponding center. Zero odd multiplicities would give the inadmissible color \(0\).

Suppose two types, \(i\) and \(j\), occur oddly. Then
\[
q=a_i+a_j\notin U_i\cup U_j.
\]
The subdivision vertex \(w\) cannot have either type, and is therefore unchanged. Among the other four vertices, the only nonadjacent pair is \(u,v\). Thus \(u,v\) have the two different types, while \(r,s\) are unchanged.

Put
\[
c(ur)=x_1,\quad c(us)=x_2,\qquad
c(vr)=y_1,\quad c(vs)=y_2,\quad c(rs)=z.
\]
Here \(x_1,x_2\in U_i\) and \(y_1,y_2\in U_j\). The unchanged blocks at \(r,s\) imply
\[
x_1+y_1+z=0,\qquad x_2+y_2+z=0.
\]
Hence
\[
x_1+x_2=y_1+y_2\in U_i\cap U_j=\{0\},
\]
contradicting the distinctness of the colors at \(u\).

Thus exactly one type occurs oddly. This proves both assertions of the lemma. \(\square\)

None of the centers belongs to any set \(U_i\setminus\{0,a_i\}\), so a block contained in \(A\) cannot be inserted. Therefore
\[
A\text{ contains an \(S\)-block}
\quad\Longleftrightarrow\quad a_1+a_2+a_3=0.                 \tag{4}
\]
Equations (2)–(4) prove \(2\Rightarrow3\).

For the remainder, assume
\[
a_1+a_2+a_3=0,
\qquad L=\langle a_1,a_2\rangle.
\]
Thus \(A=L\setminus\{0\}\).

## 3. Two auxiliary subspaces

The sufficiency proof uses two elementary geometric facts.

**Lemma 2.**

1. There is a three-dimensional subspace \(W\leq V\) disjoint from all three \(U_i\).
2. There is a five-dimensional subspace \(Y\leq V\), containing \(L\), on which every projective block is unchanged. Thus \(Y\setminus\{0\}\) is a projective STS subsystem of \(S\).

### Proof of part 1

If \(d=6\), use \(V=U_1\oplus U_2\). The third subspace is the graph of an invertible linear map between \(U_1\) and \(U_2\). After changing coordinates, the three subspaces are
\[
\{(x,0)\},\qquad \{(0,x)\},\qquad \{(x,x)\}.
\]
Identify the coordinate spaces with \(\mathbb F_8\). For \(\alpha\in\mathbb F_8\setminus\{0,1\}\),
\[
W=\{(x,\alpha x):x\in\mathbb F_8\}
\]
is disjoint from all three.

For \(d\geq7\), construct \(W\) greedily. If a subspace \(W_r\) of dimension \(r\leq2\) is disjoint from every \(U_i\), choose the next vector outside
\[
\bigcup_{i=1}^3(U_i+W_r).
\]
This union has size at most \(3\cdot2^{3+r}<2^d\). The resulting \(W_{r+1}\) remains disjoint from each \(U_i\).

### Proof of part 2

In \(V/L\), of dimension \(n=d-2\geq4\), the images
\[
E_i=(U_i+L)/L
\]
have dimension two.

Choose a three-dimensional subspace \(Z\leq V/L\) containing none of the \(E_i\). Such a choice exists: the proportion of three-dimensional subspaces containing any fixed two-dimensional subspace is
\[
\frac{(2^3-1)(2^3-2)}
     {(2^n-1)(2^n-2)}
\leq \frac15.
\]
The union of the three forbidden collections therefore occupies at most \(3/5\) of the choices.

Let \(Y\) be the inverse image of \(Z\). Then \(\dim Y=5\), \(L\subseteq Y\), and
\[
\dim(Y\cap U_i)\leq2.
\]
Also \(a_i\in Y\cap U_i\). If this intersection is two-dimensional, its unique projective line contains \(a_i\), and hence is retained by switch \(i\). It follows that every projective block inside \(Y\) is unchanged. \(\square\)

## 4. A graph lemma for leaf components

The next lemma isolates the structural fact needed to color a component incident with exactly one bridge.

**Lemma 3.** Let \(B\) be a finite simple connected bridgeless graph with one vertex \(w\) of degree two and all other vertices of degree three. There is a degree-three vertex \(r\), not adjacent to \(w\), such that \(B-r\) is connected and bridgeless.

### Proof

Suppress \(w\), obtaining a loopless bridgeless cubic multigraph \(C\), with distinguished edge \(e\). The graph \(C-e\) is simple.

First observe that deleting any vertex from a 3-edge-connected cubic graph leaves a connected bridgeless graph. Disconnection would require at least three edges from the deleted vertex to each remaining component. If a remaining edge were a bridge, its two sides would receive \(k\) and \(3-k\) edges from the deleted vertex; 3-edge-connectivity would require both
\[
1+k\geq3,\qquad 1+(3-k)\geq3,
\]
which is impossible.

If \(C\) is 3-edge-connected, choose a vertex not incident with \(e\). Such a vertex exists because \(C-e\) is simple, ruling out the two-vertex cubic multigraph.

Otherwise choose, with minimum cardinality, a nonempty vertex set \(X\) such that
\[
|\delta_C(X)|=2,\qquad e\notin E(C[X]).
\]
Such a side exists for any 2-edge cut. The two cut edges have distinct ends on each side, since \(C\) is bridgeless and cubic.

Close \(C[X]\) by adding an edge between its two degree-two vertices. The resulting cubic graph \(C_X\) is bridgeless: cycles crossing the original cut can be closed using the added edge.

It is also 3-edge-connected. Indeed, a 2-edge cut in \(C_X\) has a side containing at most one endpoint of the added edge. That side is a proper subset of \(X\) with a 2-edge boundary in \(C\), contradicting minimality.

The graph \(C_X\) has at least four vertices. Otherwise \(C[X]\) would consist of two parallel edges, contradicting the simplicity of \(C-e\), because \(e\notin E(C[X])\).

Choose \(r\in X\) away from the endpoints of the added edge. Then \(C_X-r\) is connected and bridgeless. Restoring the other side of the original 2-edge cut preserves these properties. To see this directly, cycles using an added closing edge can be rerouted through the opposite side of the cut. Thus \(C-r\) is connected and bridgeless.

The chosen \(r\) is not incident with \(e\). Subdividing \(e\) again proves the assertion for \(B\). \(\square\)

## 5. Every leaf component accepts every center

**Lemma 4.** Let \(B,w\) satisfy Lemma 3, and attach a dangling edge at \(w\). For each \(i\in\{1,2,3\}\), the resulting one-ended cubic graph has an \(S\)-coloring with dangling-edge color \(a_i\).

### Proof

Choose \(r\) as in Lemma 3, and write its neighbors as \(u_1,u_2,u_3\). Choose an inserted block of switch \(i\),
\[
T_i=\{t_1,t_2,t_3\},
\qquad t_1+t_2+t_3=a_i.
\]
These three vectors are linearly independent: three distinct nonzero binary vectors of rank two would sum to zero.

Let \(W\) be supplied by Lemma 2. Since \(B-r\) is bridgeless, it has a nowhere-zero \(W\)-flow
\[
g:E(B-r)\longrightarrow W\setminus\{0\}.
\]
Extend \(g\) by zero on the three edges incident with \(r\) and on the dangling edge.

We next construct a \(U_i\)-valued assignment \(h\). Prescribe
\[
h(ru_j)=t_j,\qquad h(\text{dangling edge})=a_i.
\]
On \(B-r\), require vertex sums
\[
\sum_{e\ni v}h(e)=
\begin{cases}
t_j,&v=u_j,\\
a_i,&v=w,\\
0,&\text{otherwise}.
\end{cases}                                                    \tag{5}
\]
The four prescribed charges sum to zero, so (5) has a solution supported on a tree joining \(u_1,u_2,u_3,w\). Explicitly, choose a spanning tree and assign to each tree edge the sum of the charges on one side of that edge.

After pruning branches containing no charge, this supporting tree has at most four leaves. Since its maximum degree is three, it has at most two degree-three vertices.

For an automorphism \(M\in\operatorname{GL}(W)\), define
\[
c(e)=h(e)+M(g(e)).                                            \tag{6}
\]
All these colors are nonzero. At \(r\), they form the inserted block \(T_i\). At every other vertex, their sum is zero; hence the three nonzero colors are distinct and form a projective line.

It remains to choose \(M\) so that no such projective line was removed by one of the switches.

No vertex other than \(r\) has all its colors in \(U_i\), because its edges in \(B-r\) have nonzero \(W\)-components.

Fix \(j\ne i\). At each \(u_k\), and at \(w\), one incident edge has a nonzero color in \(U_i\), so its colors cannot all lie in \(U_j\). At any other vertex, an incident edge with \(h(e)=0\) has color in \(W\setminus\{0\}\), also outside \(U_j\).

Consequently, a projective line lying in \(U_j\) can occur only at one of the at most two degree-three vertices of the supporting tree of \(h\).

At such a vertex, choose two incident edges, with
\[
h\text{-values }p,q,\qquad g\text{-values }x,y.
\]
Both pairs are linearly independent. For its colors to lie in \(U_j\), we need
\[
p+M(x)\in U_j,\qquad q+M(y)\in U_j.                           \tag{7}
\]
Since \(U_j\cap W=\{0\}\), each condition determines its \(W\)-value uniquely, if a solution exists. Thus (7) prescribes the images of two independent vectors under \(M\). At most four elements of \(\operatorname{GL}(W)\) meet those prescriptions.

There are at most two exceptional vertices and two indices \(j\ne i\), so at most
\[
2\cdot2\cdot4=16
\]
automorphisms are forbidden. But
\[
|\operatorname{GL}(3,2)|=7\cdot6\cdot4=168.
\]
Choose an automorphism outside the forbidden set. Then (6) is an \(S\)-coloring, with dangling-edge color \(a_i\). \(\square\)

## 6. Coloring an arbitrary simple cubic graph

We now prove \(3\Rightarrow1\).

It suffices to treat a connected simple cubic graph \(G\).

If \(G\) is bridgeless, color it by a nowhere-zero binary three-dimensional flow inside the unchanged projective subsystem \(Y\).

Suppose \(G\) has bridges. Delete all bridges and contract each resulting component to a node. The quotient is a tree \(T\).

Its components have the following forms:

- An isolated vertex of \(G\), incident with three bridges.
- A nontrivial bridgeless graph with internal degrees two or three. Each degree-two vertex is incident with exactly one bridge.

In particular, every leaf of \(T\) represents a graph of the form in Lemma 3.

### Assigning colors to the bridges

Assign every bridge a color from
\[
A=L\setminus\{0\}
\]
so that the sum at every nonleaf node of \(T\) is zero.

This is always possible. Root \(T\) at a leaf and assign its incident edge arbitrarily. Suppose a nonleaf node has parent-edge color \(p\), and \(m\geq1\) child edges. Choose their nonzero \(L\)-colors to sum to \(p\):

- If \(m\) is odd, use \(p\) on every child edge.
- If \(m\) is even, use the other two nonzero vectors of \(L\) on two child edges and \(p\) on the remaining \(m-2\).

At a node of degree three, the resulting colors are precisely the three distinct points of \(A\). Thus an isolated vertex of \(G\) already receives a valid \(S\)-block.

### Extending into nonleaf components

Let \(B\) be a nontrivial component corresponding to a nonleaf node. Its prescribed boundary colors sum to zero.

Choose a complement
\[
Y=L\oplus Z,\qquad \dim Z=3.
\]
Take a nowhere-zero \(Z\)-flow \(g\) on \(B\).

Because the boundary colors sum to zero, there is an \(L\)-valued assignment \(h\) to its internal edges whose vertex sum equals the boundary color at a boundary vertex, and equals zero elsewhere. Again, a spanning-tree construction supplies such an assignment.

Color an internal edge \(e\) by
\[
h(e)+g(e).
\]
Every internal color is nonzero, and at every vertex of \(B\), including its prescribed bridge, the three colors sum to zero. They therefore form a projective block in \(Y\), all of which are unchanged in \(S\).

### Extending into leaf components

A leaf component has one prescribed bridge color \(a_i\). Lemma 4 extends that color into the component.

These independent extensions agree on every bridge and color all of \(G\). This proves universality and completes the theorem. \(\square\)

## 7. Explicit examples with no proper universal subsystem

There is a useful strengthening when
\[
V=U_1+U_2+U_3.
\]

**Corollary.** Under this spanning assumption and \(a_1+a_2+a_3=0\), every proper STS subsystem of \(S\) fails to color \(H\). In particular, \(S\) has no proper universal subsystem.

### Proof

Suppose a subsystem \(R\) colors \(H\). Since
\[
\beta(R)\subseteq\beta(S)=A,
\]
the central block of that coloring must be \(A\). Thus all three centers belong to \(R\), and \(R\) has a balloon coloring with each boundary color \(a_i\).

By the strengthened assertion in Lemma 1, \(R\) contains an inserted block \(T_i\) of each switch. Within the switched Fano plane on \(U_i\setminus\{0\}\), a block together with the point \(a_i\) outside that block generates the whole Fano plane. Hence
\[
U_i\setminus\{0\}\subseteq R\qquad(i=1,2,3).
\]

Let \(Q\) be the point set of \(R\). Then \(Q\cup\{0\}\) is closed under binary addition:

- If the old line \(\{x,y,x+y\}\) is retained, closure of the subsystem gives \(x+y\in Q\).
- If that line was removed, it lies in some \(U_i\), all of whose nonzero points already belong to \(Q\).

Therefore \(Q\cup\{0\}\) contains \(U_1+U_2+U_3=V\), so \(R=S\). \(\square\)

Here are three completely specified examples. Let \(e_1,\ldots,e_d\) be a binary basis, and set
\[
U_1=\langle e_1,e_2,e_3\rangle,\qquad
U_2=\langle e_4,e_5,e_6\rangle,
\]
with centers
\[
a_1=e_1,\qquad a_2=e_4,\qquad a_3=e_1+e_4.
\]
Choose \(U_3\) as follows:
\[
\begin{array}{c|c|c}
d&U_3&|S|\\ \hline
6&\langle e_1+e_4,\ e_2+e_5,\ e_3+e_6\rangle&63\\
7&\langle e_1+e_4,\ e_2+e_5,\ e_7\rangle&127\\
8&\langle e_1+e_4,\ e_7,\ e_8\rangle&255.
\end{array}
\]
The subspaces are pairwise disjoint outside zero and span \(V\). Apply the three switches described in Section 1—delete twelve projective blocks and insert twelve blocks.

Each resulting system is universal, and every proper subsystem fails on \(H\).

They are also point-intransitive: the intrinsically defined palette
\[
\beta(S)=\{a_1,a_2,a_3\}
\]
is a nonempty proper subset of the point set invariant under every automorphism.

## 8. What remains unresolved

The result establishes, for the three-switch family,
\[
\boxed{\quad S\text{ universal}\iff H\text{ is \(S\)-colorable}
\iff a_1+a_2+a_3=0.\quad}
\]

It does **not** establish that the \(16\)-vertex graph \(H\) tests universality for arbitrary STS. Nor does it establish that every universal STS contains one of these examples.

The proof relies on two special features of this family:

1. Every possible leaf component accepts each of the three switch centers.
2. An unchanged projective subsystem accommodates all zero-sum boundary assignments needed at nonleaf components.

Neither property has been established here for general point-intransitive systems. Thus the original classification problem remains unresolved. Novelty of this restricted characterization, especially relative to the point-intransitive constructions mentioned in the question, also remains unchecked.