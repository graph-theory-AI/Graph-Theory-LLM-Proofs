```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but two disjoint models suffice for k at most 4, and for every k they suffice whenever the two models have five disjoint connecting paths, hence in every 5-connected graph.",
  "would_publish": false,
  "caveats": "The 3-connected case for k at least 5 remains unresolved; novelty of these elementary partial results has not been checked."
}
```

## 1. Statement of the partial results

Write \(L_k\) for the ladder with vertices
\[
a_1,\ldots ,a_k,b_1,\ldots ,b_k
\]
and edges \(a_i a_{i+1},b_i b_{i+1}\), and \(a_i b_i\).

The following results are proved below.

### Theorem A: the first four cases

Let \(G\) be 3-connected.

1. \(G\) contains \(L_2\) as a minor.
2. If \(G\) contains two vertex-disjoint \(L_2\)-minor models, then \(G\) contains \(L_3\) as a minor.
3. If \(G\) contains two vertex-disjoint \(L_3\)-minor models, then \(G\) contains \(L_4\) as a minor.
4. If \(G\) contains two vertex-disjoint \(L_4\)-minor models, then \(G\) contains \(L_5\) as a minor.

Thus the bumping theorem holds with \(N=2\) for \(2\leq k\leq4\), and these values are sharp. For \(k=1\), already \(N=1\) works.

### Theorem B: a five-linkage version for all \(k\)

Let \(k\geq3\). Suppose \(G\) contains two vertex-disjoint subdivisions \(S,T\) of \(L_k\), and there are five pairwise vertex-disjoint \(S\)-\(T\) paths. Then \(G\) contains \(L_{k+1}\) as a minor.

Since every minor model of a subcubic graph contains a subdivision of that graph, this has the following consequence.

### Corollary C

For every \(k\), every 5-connected graph containing two vertex-disjoint \(L_k\)-minor models contains \(L_{k+1}\) as a minor.

In particular, any obstruction to the original conjecture is necessarily caused by separations of order \(3\) or \(4\).

---

## 2. Preliminary lemmas

### 2.1. Replacing minor models by subdivisions

A standard elementary fact is needed.

**Lemma 2.1.**  
If \(H\) has maximum degree at most \(3\), then every \(H\)-minor model contains a subdivision of \(H\) inside the union of its branch sets.

**Proof.**  
For each branch set \(B_v\), retain a minimal tree joining the endpoints of the model edges corresponding to edges incident with \(v\). Since \(d_H(v)\leq3\), this tree is either a path or a subdivision of a three-edge star. Choosing its unique branching point when \(d_H(v)=3\), and suppressing unnecessary degree-two vertices, gives a subdivision of \(H\). Different branch sets remain disjoint. ∎

Hence throughout the proof we may replace pairwise disjoint ladder models by pairwise disjoint ladder subdivisions.

### 2.2. Rooted ladder models

An \(L_t\)-minor model is **rooted at \(x,y\)** if \(x\) and \(y\) belong to the two branch sets corresponding to the vertices of one end rung.

The following concatenation observation will be used repeatedly.

**Lemma 2.2 (Concatenation).**  
Suppose \(M_1,M_2\) are disjoint rooted models of \(L_p,L_q\), rooted respectively at \(x_1,x_2\) and \(y_1,y_2\). If there are disjoint paths
\[
P_1:x_1\longrightarrow y_1,\qquad
P_2:x_2\longrightarrow y_2
\]
whose interiors avoid \(M_1\cup M_2\), then their union contains an \(L_{p+q}\)-minor.

The crossed pairing \(x_1y_2,x_2y_1\) works as well.

**Proof.**  
Orient the rooted rung of \(M_1\) as its right end and that of \(M_2\) as its left end. Contract the interiors of \(P_1,P_2\). They become the two rail edges joining these end rungs, producing \(L_{p+q}\). In the crossed case, interchange the two rails of \(M_2\). ∎

---

## 3. Any two vertices in a sufficiently long ladder root a square

The following small lemma is the reason the cases \(k=3,4\) are accessible.

**Lemma 3.1.**  
Let \(k\geq3\), let \(S\) be a subdivision of \(L_k\), and let \(x\neq y\) be vertices of \(S\). Then \(S\) has an \(L_2\)-minor rooted at \(x,y\).

**Proof.**  
It is enough to find a cycle \(D\) through \(x,y\) such that one of the two \(x\)-\(y\) arcs of \(D\) has at least three edges. Contract the other arc to one edge and the longer arc to a three-edge path. The result is a 4-cycle in which the branch sets containing \(x,y\) are adjacent.

Let \(C\) be the perimeter cycle of the ladder subdivision.

- If \(x,y\in V(C)\), use \(C\), whose length is at least \(2k\geq6\).
- Suppose \(x\) lies internally on an internal rung \(R_i\). If \(y\in C\), take \(R_i\) together with the perimeter \(a_i\)-\(b_i\) arc containing \(y\). The rung has at least two edges, and either perimeter arc between \(a_i,b_i\) has at least three edges, so the cycle has length at least five.
- If both vertices lie internally on the same internal rung, use that rung and either perimeter arc.
- If they lie internally on distinct rungs \(R_i,R_j\), use those two rungs and the two rail segments between them. This cycle has length at least six.

Thus in every case there is a cycle of length at least five through \(x,y\). One of its two \(x\)-\(y\) arcs has at least three edges. ∎

---

## 4. A half-ladder rooting lemma

This is the main ingredient in the five-linkage result.

**Lemma 4.1 (Two-color rooting lemma).**  
Let \(k\geq3\), put
\[
h=\left\lfloor\frac{k}{2}\right\rfloor,
\qquad q=h+1.
\]
For every subdivision \(S\) of \(L_k\), there is a red-blue coloring of \(V(S)\) such that any two distinct vertices of the same color root an \(L_q\)-minor in \(S\).

**Proof.**

Use \(a_i,b_i\) for the branch vertices of the subdivision, and \(R_i\) for the subdivided \(i\)-th rung. Let \(C\) be its perimeter cycle.

Let \(Q\) be the \(a_{h+1}\)-\(b_{h+1}\) path in \(C\) going through the left end rung \(R_1\). Color
\[
V(Q)\setminus\{a_{h+1},b_{h+1}\}
\]
red, and color all other perimeter vertices blue.

For an internal rung \(R_i\), color its internal vertices red when \(i\leq h\), and blue when \(i\geq h+1\). Notice that both ends of each such rung already have this color.

First suppose that \(x,y\) lie on the perimeter.

### Red pair

Both are strictly internal to \(Q\). After possibly exchanging \(x,y\), their order on \(Q\) is
\[
a_{h+1},\ldots,x,\ldots,y,\ldots,b_{h+1}.
\]
Use:

- the \(x\)-\(y\) segment of \(Q\) as a new end rung;
- the \(x\)-\(a_{h+1}\) and \(y\)-\(b_{h+1}\) segments as two rails;
- the subladder on columns \(h+1,\ldots,k\).

This is a subdivision of
\[
L_{k-h+1},
\]
rooted at \(x,y\). Since \(k-h+1\geq h+1=q\), it contains a rooted \(L_q\)-minor.

### Blue pair

Let \(Q'\) be the perimeter path from \(a_h\) to \(b_h\) going through the right end rung \(R_k\). Every blue perimeter vertex is strictly internal to \(Q'\). Thus, in the same way, two blue vertices provide a new end rung attached to the subladder on columns \(1,\ldots,h\). This gives a rooted \(L_{h+1}=L_q\)-minor.

### Vertices internal to rungs

Suppose a root \(z\) lies internally on \(R_i\). Project it along \(R_i\) to one of \(a_i,b_i\). For two roots on different rungs, choose distinct projections. For two roots on the same rung, assign them in their order on that rung to its two ends. If the other root is already one endpoint of that rung, project the internal root to the other endpoint.

The projection paths are disjoint. Moreover:

- red internal rungs have index at most \(h\), and the red construction retains only the opposite, right-hand subladder;
- blue internal rungs have index at least \(h+1\), and the blue construction retains only the left-hand subladder.

Consequently the projection paths meet the rooted ladder model only at their projected endpoints. They may be absorbed into the corresponding root branch sets. Hence the original vertices, rather than merely their projections, are the roots. ∎

---

## 5. Proof of the five-linkage theorem

Let \(S,T\) be the two disjoint \(L_k\)-subdivisions.

The five given paths may be shortened so that each meets \(S\cup T\) only at its endpoints: orient each from \(S\) to \(T\), take the first encountered vertex of \(T\), and the last vertex of \(S\) preceding it.

Apply Lemma 4.1 independently to \(S\) and \(T\). Each connecting path now receives one of four color types:
\[
RR,\ RB,\ BR,\ BB,
\]
according to the colors of its endpoints in \(S\) and \(T\). Among five paths, two have the same type.

Their two endpoints in \(S\) therefore root an \(L_q\)-minor, and their two endpoints in \(T\) also root an \(L_q\)-minor, where
\[
q=\left\lfloor\frac{k}{2}\right\rfloor+1.
\]
By Lemma 2.2, the two connecting paths concatenate these into an \(L_{2q}\)-minor. Finally,
\[
2q=
2\left\lfloor\frac{k}{2}\right\rfloor+2
\geq k+1.
\]
Thus \(G\) contains \(L_{k+1}\) as a minor. This proves Theorem B. ∎

### 5.1. The 5-connected corollary

If \(G\) is 5-connected and \(k\geq3\), each ladder subdivision has at least six vertices. By the set version of Menger's theorem, there are five vertex-disjoint paths between the two subdivisions: deleting fewer than five vertices leaves at least one vertex of each subdivision and leaves \(G\) connected.

Theorem B applies. The cases \(k=1,2\) follow from Theorem A below. ∎

The number of models cannot be reduced to one even under 5-connectivity: for \(k\geq3\), the graph \(K_{2k}\) is 5-connected, contains \(L_k\), and cannot contain \(L_{k+1}\) because it has only \(2k\) vertices.

---

## 6. Proof of the first four cases

### 6.1. The case \(k=1\)

Every 3-connected graph contains \(L_2=C_4\) as a minor.

Indeed, if it has a cycle of length at least four, that cycle contains a \(C_4\)-minor. Otherwise choose a triangle \(C\). Under the standard convention a 3-connected graph has at least four vertices, so \(G-C\neq\varnothing\). Every component of \(G-C\) has all three vertices of \(C\) as neighbors; otherwise at most two vertices separate that component. Contracting such a component gives a \(K_4\)-minor, and hence a \(C_4\)-minor.

Thus \(N=1\) works for \(k=1\).

### 6.2. The case \(k=2\)

Let \(S,T\) be disjoint subdivisions of \(L_2=C_4\); in particular, they are disjoint cycles.

By 3-connectivity and Menger's theorem, there are three vertex-disjoint \(S\)-\(T\) paths, with distinct endpoints on each cycle. Contract the three arcs into which the endpoints divide \(S\), and similarly for \(T\). Contract the connecting paths as well. The result is the triangular prism: two triangles joined by a perfect matching.

The triangular prism contains \(L_3\). Explicitly, if the triangles are
\[
s_1s_2s_3s_1,\qquad t_1t_2t_3t_1
\]
and the matching is \(s_it_i\), delete \(s_1s_2\) and \(t_1t_2\). The remaining graph consists of the three internally disjoint \(s_3\)-\(t_3\) paths
\[
s_3t_3,\qquad
s_3s_1t_1t_3,\qquad
s_3s_2t_2t_3,
\]
and is exactly \(L_3\).

Thus two \(L_2\)-models suffice.

### 6.3. The case \(k=3\)

Let \(S,T\) be disjoint \(L_3\)-subdivisions. Two disjoint \(S\)-\(T\) paths exist already by 2-connectivity; in particular they exist in a 3-connected graph.

By Lemma 3.1, their two endpoints in \(S\) root an \(L_2\)-minor, and their two endpoints in \(T\) root another \(L_2\)-minor. Lemma 2.2 concatenates them into
\[
L_{2+2}=L_4.
\]

### 6.4. The case \(k=4\)

Let \(S,T\) be disjoint \(L_4\)-subdivisions. By 3-connectivity there are three disjoint \(S\)-\(T\) paths.

Apply Lemma 4.1 to \(S\). Here
\[
q=\left\lfloor\frac42\right\rfloor+1=3.
\]
Among the three endpoints in \(S\), two have the same color. Their corresponding paths have two distinct endpoints in \(T\).

The selected endpoints in \(S\) root an \(L_3\)-minor by Lemma 4.1. Their endpoints in \(T\) root an \(L_2\)-minor by Lemma 3.1. Concatenating gives
\[
L_{3+2}=L_5.
\]

This proves Theorem A. ∎

### Sharpness for \(2\leq k\leq4\)

One model does not suffice:

- \(K_4\) contains \(L_2\) but has too few vertices for \(L_3\).
- The triangular prism \(C_3\square K_2\) contains a spanning \(L_3\) but has too few vertices for \(L_4\).
- The cube \(C_4\square K_2\) contains a spanning \(L_4\) but has too few vertices for \(L_5\).

All three graphs are 3-connected. Hence \(N=2\) is optimal for \(k=2,3,4\).

---

## 7. Structural consequence for a possible counterexample

Let \(k\geq3\), and suppose \(G\) is 3-connected and \(L_{k+1}\)-minor-free. For any two disjoint \(L_k\)-subdivisions \(S,T\), Theorem B shows that there cannot be five disjoint \(S\)-\(T\) paths. Menger's theorem therefore gives an \(S\)-\(T\) separator of size at most four.

Because \(G\) is 3-connected and both \(S,T\) have at least six vertices, no set of at most two vertices separates them. Thus every pair of disjoint \(L_k\)-models in such a graph is separated by a set of order \(3\) or \(4\).

This isolates the unresolved part of the conjecture: one must control how many near-maximal ladders can accumulate across a system of 3- and 4-separations.

---

## 8. Remaining gap

For two models in a merely 3-connected graph, Menger supplies only three connecting paths. The coloring in Lemma 4.1 gives four possible endpoint-color types. Three paths need not contain two of the same type. One can force a same-colored pair at one ladder, but not simultaneously at both.

For \(k=4\), this is enough because the first model contributes a rooted \(L_3\) and an arbitrary pair in the second contributes a rooted \(L_2\). For \(k\geq5\),
\[
\left(\left\lfloor\frac{k}{2}\right\rfloor+1\right)+2<k+1,
\]
so that argument no longer bumps the ladder.

Consequently, the universal-\(N_0\) conjecture for 3-connected graphs and \(k\geq5\) remains open. The argument above neither proves a universal constant nor produces a counterexample.