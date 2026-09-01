```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A 12-vertex strongly 2-connected oriented graph has a crossing drawing in the annulus with every directed cycle of winding one, but two equally oriented forced facial triangles preclude any such crossing-free drawing.",
  "would_publish": true,
  "caveats": "This uses signed winding number and the standard definition that deleting any one vertex leaves a strongly connected digraph."
}
```

# An explicit counterexample

All subscripts below are taken modulo \(12\). A directed cycle means a vertex-simple directed cycle.

## 1. Construction

Let
\[
V(D)=\mathbb Z_{12}.
\]
For every \(i\in\mathbb Z_{12}\), include the two arcs
\[
i\longrightarrow i+1,\qquad i\longrightarrow i+2,
\]
and add the two exceptional arcs
\[
4\longrightarrow 0,\qquad 10\longrightarrow 6.
\]

Assign an “advance” \(a(e)\) to each arc by
\[
a(i,i+1)=1,\qquad a(i,i+2)=2,\qquad
a(4,0)=a(10,6)=8.
\]
In every case,
\[
\operatorname{head}(e)\equiv \operatorname{tail}(e)+a(e)\pmod {12}.
\]
Consequently, the total advance of every directed closed walk is a positive multiple of \(12\).

We prove that every directed cycle has total advance exactly \(12\).

## 2. Calculation of all directed cycles

### Cycles using neither exceptional arc

If \(C\) uses only arcs of advances \(1\) and \(2\), then
\[
a(C)\leq 2|C|\leq 24.
\]
If \(a(C)\geq24\), equality must hold throughout: \(C\) has twelve arcs and every arc has advance \(2\). But repeatedly adding \(2\) modulo \(12\) returns to the starting vertex after six steps, so this is not a simple twelve-vertex cycle. Therefore
\[
a(C)=12.
\]

### Cycles using exactly one exceptional arc

By translation by \(6\), it suffices to consider a cycle using \(4\to0\). The rest of the cycle is a directed path \(P\) from \(0\) to \(4\), using only advances \(1\) and \(2\). Its advance is congruent to \(4\pmod {12}\). Since \(P\) has at most eleven arcs, its advance is at most \(22\). Thus the only possibilities are
\[
a(P)=4\quad\text{or}\quad a(P)=16.
\]

We show that \(a(P)=16\) is impossible. Lift \(P\) to a strictly increasing sequence
\[
0=x_0<x_1<\cdots <x_k=16,
\qquad x_{j+1}-x_j\in\{1,2\},
\]
whose residues modulo \(12\) are distinct. The path cannot visit \(4\) before its endpoint and cannot revisit residue \(0\).

To pass \(4\) without landing on it, the lifted path must contain the step
\[
3\longrightarrow5.
\]
To pass \(12\) without revisiting residue \(0\), it must contain
\[
11\longrightarrow13.
\]
Thus the post-wrap portion starts at residue \(1\). From \(13\) to \(16\), the possible increment sequences are
\[
(1,2),\qquad(2,1),\qquad(1,1,1).
\]
Modulo \(12\), these respectively visit \(2\), \(3\), or both \(2\) and \(3\).

Before the wrap, the path already visits \(3\). If it also visits \(1\), that repeats the residue of \(13\). If it avoids \(1\), the only way to reach \(3\) from \(0\) with steps \(1,2\) is through \(2\), so one of the post-wrap residues \(2,3\) is repeated. This contradiction proves \(a(P)\neq16\).

Hence \(a(P)=4\), and the whole cycle has advance
\[
8+4=12.
\]
The same argument applies to \(10\to6\).

### Cycles using both exceptional arcs

Such a cycle, after cyclically choosing its starting point, would have the form
\[
4\to0\; P\;10\to6\; Q\;4,
\]
where \(P\) is a base-arc path from \(0\) to \(10\), and \(Q\) is a base-arc path from \(6\) to \(4\).

Each of \(P,Q\) has advance congruent to \(10\pmod {12}\), and hence advance at least \(10\). A simple cycle has at most twelve arcs, so after the two exceptional arcs it has at most ten base arcs. Their total advance is therefore at most \(20\). Equality is forced, so there are exactly ten base arcs and every one has advance \(2\).

In particular, \(P\) would begin
\[
0\to2\to4,
\]
revisiting the initial vertex \(4\) of the cycle before reaching \(10\). This is impossible. Thus no directed cycle uses both exceptional arcs.

We have proved:

\[
\boxed{\text{Every directed cycle of \(D\) has total advance \(12\).}}
\]

## 3. The hypothesis of the conjecture holds

### Strong \(2\)-connectivity

For every \(z\in\mathbb Z_{12}\), the graph \(D-z\) contains the directed Hamilton cycle
\[
z+1\to z+2\to\cdots\to z-1\to z+1.
\]
All but its final arc have advance \(1\), while the final arc \(z-1\to z+1\) has advance \(2\). Hence \(D-z\) is strongly connected for every \(z\), so \(D\) is strongly \(2\)-connected.

### Drawing in the annulus

Model the universal cover of the annulus as
\[
\mathbb R\times(0,1),
\]
with deck transformation \((x,y)\mapsto(x+12,y)\). Place vertex \(i\) at a point with first coordinate \(i\). For every arc \(e=i\to j\), draw a lift from the chosen lift of \(i\) to the lift of \(j\) whose first coordinate is \(i+a(e)\). Choose these curves generically so that they avoid nonincident vertices; crossings are allowed.

A directed cycle lifts with horizontal displacement equal to its total advance. By the preceding calculation, that displacement is always \(12\). Hence every directed cycle has signed winding number \(+1\).

Thus \(D\) satisfies the complete hypothesis.

## 4. No required crossing-free drawing exists

Let \(U\) be the underlying undirected graph of \(D\), and let \(H\subseteq U\) consist of the edges
\[
\{i,i+1\},\qquad \{i,i+2\}.
\]
Thus \(H=C_{12}^{\,2}\), the square of the twelve-cycle.

### The forced planar embedding

The graph \(H\) is the graph of the hexagonal antiprism. It has a sphere embedding with the two hexagonal faces
\[
E=(0,2,4,6,8,10)
\]
and
\[
O=(1,3,5,7,9,11),
\]
and with the twelve remaining faces being the triangles on three cyclically consecutive vertices.

Moreover, \(H\) is \(3\)-connected. Indeed, deleting two adjacent vertices from the original twelve-cycle leaves a connected path, while deleting two nonadjacent vertices leaves two paths that are reconnected by the distance-two edges across the deleted vertices. Adding edges cannot lower vertex-connectivity, so
\[
U=H+\{0,4\}+\{6,10\}
\]
is also \(3\)-connected.

Inside the hexagonal face \(E\), draw the added edges \(0\,4\) and \(6\,10\). They cut off two facial triangles
\[
T_1=(0,2,4),\qquad T_2=(6,8,10).
\]
By uniqueness of the sphere embedding of a \(3\)-connected planar graph, these remain facial cycles in every planar embedding of \(U\), up to a simultaneous reflection.

Their directed versions in \(D\) are
\[
\vec T_1:\quad 0\to2\to4\to0
\]
and
\[
\vec T_2:\quad 6\to8\to10\to6.
\]
Both follow the same direction around the even hexagon \(E\). Consequently, in every sphere embedding they have the same facial orientation: either both are clockwise around their facial disks or both are counterclockwise.

### The annular obstruction

Suppose, for contradiction, that \(D\) had a crossing-free drawing in an annulus in which every directed cycle had winding \(+1\). Fill the two boundary components of the annulus with disks. This produces a sphere embedding of \(U\) and two marked points \(p,q\), one in each filled disk.

A simple cycle has nonzero winding in the annulus precisely when it separates \(p\) from \(q\). Since \(T_1\) is facial, for \(\vec T_1\) to have nonzero winding, exactly one of \(p,q\) must lie in the facial disk bounded by \(T_1\). The same is true for \(T_2\). As the two facial disks are disjoint, after interchanging \(p,q\) if necessary we must have
\[
p\in F_1,\qquad q\in F_2,
\]
where \(F_i\) is the facial disk bounded by \(T_i\).

Orient the sphere, and orient \(\partial F_i\) with \(F_i\) on its left. Because \(\vec T_1,\vec T_2\) have the same facial orientation, there is one sign \(\varepsilon\in\{1,-1\}\) such that
\[
[\vec T_1]=\varepsilon[\partial F_1],
\qquad
[\vec T_2]=\varepsilon[\partial F_2].
\]
But in the annulus obtained by deleting disks in \(F_1,F_2\),
\[
[\partial F_1]+[\partial F_2]=0
\]
in first homology. Therefore
\[
[\vec T_1]=-[\vec T_2].
\]
Their winding numbers are necessarily opposite. They cannot both have winding \(+1\), a contradiction.

Hence the required crossing-free annular drawing does not exist.

## Conclusion

The digraph
\[
A(D)=\{i\to i+1,\ i\to i+2:i\in\mathbb Z_{12}\}
 \cup\{4\to0,\ 10\to6\}
\]
is an explicit counterexample to Conjecture 1.2 under the standard signed interpretation of winding number. The graph is even planar; the obstruction is that its two forced facial directed triangles have the same facial orientation, whereas two boundary-parallel cycles at opposite ends of an annulus must have opposite facial orientations in the capped sphere.