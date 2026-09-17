```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sharper bridge enumeration, including an exact asymptotic for graphs with multiple bridges, is possible, but the required upper bound on bridgeless non-Hamiltonian graphs remains missing.",
  "would_publish": false,
  "caveats": "Connected simple unlabelled graphs are intended; standard regular-graph enumeration is used, and no novelty claim is made. The disconnected interpretation is false."
}
```

## 1. Interpretation and results

I use the interpretation implicit in the supplied attempt: **connected, simple cubic graphs, counted up to isomorphism**, with “1-connected” meaning vertex-connectivity exactly one. In a connected cubic graph, having a cut-vertex is equivalent to having a bridge.

Put \(N=2n\), and define
\[
\begin{aligned}
U_N&=\#\{\text{connected unlabelled simple cubic graphs on }N\text{ vertices}\},\\
B_N&=\#\{\text{such graphs having a bridge}\},\\
R_N&=\#\{\text{such graphs that are bridgeless and non-Hamiltonian}\}.
\end{aligned}
\]
Thus
\[
NH(n)=B_{2n}+R_{2n},\qquad NHB(n)=B_{2n}.
\]

I checked the local decompositions and Petersen-fragment construction in the supplied attempt. They are usable. The additional result below is a more precise enumeration of bridge graphs, especially those with more than one bridge.

Let \(E_m\) denote the number of connected unlabelled simple cubic graphs on \(m\) vertices with a distinguished edge, up to isomorphism. Let \(M_N\) count the graphs counted by \(B_N\) that have at least two bridges. Then
\[
\boxed{
B_N=E_{N-6}+5E_{N-8}+O(U_N/N^4).
}
\tag{1}
\]
In particular,
\[
\boxed{
B_N\sim \frac{32}{9}\frac{U_N}{N^2}.
}
\tag{2}
\]
More sharply,
\[
\boxed{
M_N\sim \frac{1024}{81}\frac{U_N}{N^4}.
}
\tag{3}
\]

There is also a structural refinement. If \(Q_N^{(s)}\) counts graphs with exactly one bridge whose smaller side has \(s\) vertices, then
\[
\boxed{
\frac{Q_N^{(7)}}{B_N}
=\frac{16}{3N}+o(N^{-1}),\qquad
\frac{Q_N^{(5)}}{B_N}
=1-\frac{16}{3N}+o(N^{-1}).
}
\tag{4}
\]
Furthermore, almost every graph counted by \(M_N\) has exactly two bridges, and two explicitly described configurations account equally for its leading term.

For comparison with the denominator, the Petersen-fragment construction gives
\[
\boxed{
R_N\ge
\left(\frac{256}{81}+o(1)\right)\frac{U_N}{N^3}.
}
\tag{5}
\]
Consequently,
\[
\frac{NHB(n)}{NH(n)}
\le 1-\frac{4}{9n}+o(n^{-1}).
\tag{6}
\]

These statements do **not** settle the connected conjecture. What is missing is an upper bound
\[
R_N=o(U_N/N^2).
\tag{7}
\]

---

## 2. Enumeration input and the unlabelled issue

The external enumeration input used here is the standard fixed-degree regular-graph asymptotic, including its unlabelled form. Write
\[
v_N=\frac{(3N-1)!!}{6^N N!}.
\]
If \(L_N\) counts connected labelled simple cubic graphs, then, along even \(N\),
\[
L_N\sim e^{-2}N!v_N,\qquad U_N\sim e^{-2}v_N.
\tag{8}
\]
The unlabelled assertion is part of the input; it is not inferred merely from asymmetry in the labelled model.

Directly,
\[
\frac{v_{N-2}}{v_N}
=\frac{12N}{(3N-1)(3N-5)}.
\tag{9}
\]
Hence, for every fixed even \(k\),
\[
\frac{U_{N-k}}{U_N}
\sim
\left(\frac{2}{\sqrt3}\right)^k N^{-k/2}.
\tag{10}
\]

Equation (8) also implies asymmetry for almost all unlabelled graphs. Indeed,
\[
U_N-\frac{L_N}{N!}
=\sum_{[G]}
\left(1-\frac1{|\operatorname{Aut}(G)|}\right)
=o(U_N).
\tag{11}
\]
Every symmetric class contributes at least \(1/2\). Therefore
\[
E_m\sim \frac{3m}{2}U_m.
\tag{12}
\]

A related transfer principle will be useful later. For any isomorphism-invariant property \(\mathcal A\),
\[
U_N(\mathcal A)
\le
\frac{L_N(\mathcal A)}{N!}
+\left(U_N-\frac{L_N}{N!}\right).
\tag{13}
\]
Thus a property occurring with probability \(o(1)\) in the labelled model also occurs in \(o(U_N)\) unlabelled classes. This does **not** transfer arbitrary \(N^{-2}\)-scale estimates.

---

## 3. Exact decomposition of a bridge side

For odd \(s\), let \(A_s\) count connected unlabelled simple graphs with one vertex of degree two and all other vertices of degree three. The degree-two vertex is intrinsically distinguished.

There is an exact recurrence
\[
\boxed{
A_s=E_{s-1}+A_{s-2}+A_{s-4},
}
\qquad s\ge5,
\tag{14}
\]
with \(A_1=A_3=0\).

To verify it, let \(r\) be the degree-two vertex, with neighbours \(a,b\).

* If \(a,b\) are nonadjacent, suppress \(r\). The result is a simple cubic graph with a distinguished edge.
* If \(a,b\) are adjacent, let \(x,y\) be their respective third neighbours.
  * If \(x\ne y\), contract the triangle \(rab\) to a degree-two vertex. This gives an object counted by \(A_{s-2}\).
  * If \(x=y=t\), the vertices \(r,a,b,t\) induce a diamond. The remaining edge at \(t\) leads to the rest of the graph. Delete these four vertices; the endpoint in the rest becomes the unique degree-two vertex. This gives an object counted by \(A_{s-4}\).

Each operation has a unique inverse up to isomorphism, and all resulting graphs are connected and simple.

Using (9), (12), and induction in (14),
\[
A_s=O(sv_{s-1}),\qquad
A_s\sim E_{s-1}\sim \frac{3(s-1)}2U_{s-1}.
\tag{15}
\]

The first two values needed below are
\[
A_5=1,\qquad A_7=4.
\tag{16}
\]
The unique graph counted by \(A_5\), denoted \(F_5\), is \(K_4\) with one edge subdivided.

For \(A_7\), the connected simple cubic graphs on six vertices are \(K_{3,3}\) and the triangular prism. They have respectively one and two edge-orbits, so \(E_6=3\), and (14) gives \(A_7=3+1=4\).

### A uniform convolution estimate

For every fixed odd \(r\ge5\),
\[
\sum_{\substack{r\le s\le N/2\\s\text{ odd}}}
A_sA_{N-s}
=O(Nv_{N-r-1}).
\tag{17}
\]
Here and below the midpoint term can be included with any bounded multiplicity.

For completeness, by (15) it suffices to bound
\[
T_N(s)=s(N-s)v_{s-1}v_{N-s-1}.
\]
Equation (9) gives
\[
\frac{T_N(s+2)}{T_N(s)}
=\frac{h(s)}{h(N-s-2)},
\]
where
\[
h(x)=
\frac{(x+2)(9x^2-4)}{12x(x+1)}
=\frac1{12}\left(9x+9-\frac8x-\frac5{x+1}\right).
\]
The function \(h\) is increasing. The terms therefore decrease towards the midpoint. For \(s\le N/4\), their successive ratios are at most \(1/2\) for sufficiently large \(N\). The remaining central terms are exponentially smaller than the initial term. This proves (17).

In particular, the tails beginning at \(s=5,7,9,11\) have orders
\[
O(U_N/N^2),\quad O(U_N/N^3),\quad
O(U_N/N^4),\quad O(U_N/N^5),
\tag{18}
\]
respectively.

---

## 4. Counting distinguished bridges and removing the overcount

Let \(D_N\) count connected unlabelled cubic graphs with a distinguished bridge. Thus a graph contributes the number of its automorphism-orbits of bridges, not necessarily its number of bridges.

Deleting the distinguished bridge gives an unordered pair of objects counted by the \(A_s\). Hence
\[
D_N=
\sum_{\substack{5\le s<N/2\\s\text{ odd}}}
A_sA_{N-s}
+
\mathbf1_{\{N/2\text{ odd}\}}
\binom{A_{N/2}+1}{2}.
\tag{19}
\]
By (16)–(18),
\[
D_N=A_{N-5}+4A_{N-7}+O(U_N/N^4).
\]
Applying (14) twice gives
\[
\boxed{
D_N=E_{N-6}+5E_{N-8}+O(U_N/N^4).
}
\tag{20}
\]
In particular, \(B_N\le D_N=O(U_N/N^2)\).

To control the distinguished-bridge overcount, let \(C_s\) count those objects in \(A_s\) that themselves have a bridge. Let \(E_m^B\) count edge-rooted cubic graphs that have a bridge somewhere. The same local decomposition gives
\[
\boxed{
C_s=E_{s-1}^B+C_{s-2}+A_{s-4}.
}
\tag{21}
\]
The diamond case always creates a bridge; the other two cases preserve whether a bridge exists.

Since
\[
E_m^B\le \frac{3m}{2}B_m=O(v_m/m),
\]
equations (9), (15), and (21) imply
\[
C_s=O(v_{s-1}/s)=O(A_s/s^2).
\tag{22}
\]
Also,
\[
C_5=C_7=0,\qquad C_9=1.
\tag{23}
\]

Let \(J_N\) count distinguished-bridge objects whose underlying graph has at least two bridges. Up to harmless treatment of the midpoint,
\[
J_N\le
\sum_{\substack{5\le s\le N/2\\s\text{ odd}}}
\bigl(C_sA_{N-s}+A_sC_{N-s}\bigr).
\tag{24}
\]
The first sum starts at \(s=9\), so it is \(O(U_N/N^4)\) by (17). In the second sum, \(N-s\ge N/2\), so (22) gives an additional factor \(O(N^{-2})\) relative to (19). Therefore
\[
J_N=O(U_N/N^4).
\tag{25}
\]
Since
\[
0\le D_N-B_N\le J_N,
\]
equation (1) follows.

Using (10) and (12),
\[
B_N\sim E_{N-6}
\sim \frac{3N}{2}U_{N-6}
\sim \frac{32}{9}\frac{U_N}{N^2},
\]
proving (2).

### The smaller bridge side

For sufficiently large \(N\), the unique-bridge counts satisfy the exact identities
\[
Q_N^{(5)}=A_{N-5}-C_{N-5},
\qquad
Q_N^{(7)}=4(A_{N-7}-C_{N-7}).
\]
Consequently,
\[
\begin{aligned}
Q_N^{(5)}&=E_{N-6}+E_{N-8}+O(U_N/N^4),\\
Q_N^{(7)}&=4E_{N-8}+O(U_N/N^4).
\end{aligned}
\tag{26}
\]
As
\[
\frac{E_{N-8}}{E_{N-6}}\sim \frac{4}{3N},
\]
these identities prove (4).

---

## 5. The leading term for multiple bridges

The bound (25) can be sharpened to the exact asymptotic (3).

First,
\[
E_m^B\sim \frac{3m}{2}B_m.
\tag{27}
\]
To justify this without assuming rare-event asymmetry, consider the following family: start with an asymmetric bridgeless cubic graph on \(m-6\) vertices, subdivide a chosen edge, and attach \(F_5\) by a bridge at the new subdivision vertex.

This family has \((1+o(1))E_{m-6}\sim B_m\) classes. Its automorphisms are supported inside the fixed five-vertex fragment. Hence each graph has \(3m/2-O(1)\) edge-orbits. This proves (27).

Equations (21), (22), and (27) now give
\[
\begin{aligned}
C_s
&\sim
\frac{9}{4}s^2U_{s-7}
+\frac32sU_{s-5}\\
&\sim
\frac92sU_{s-5}.
\end{aligned}
\tag{28}
\]

Returning to \(J_N\), the leading terms in (24) can be identified exactly. A marked bridge with smaller side five contributes \(C_{N-5}\). The first possible bridged smaller side has order nine, and \(C_9=1\), contributing \(A_{N-9}\). All remaining contributions are \(O(U_N/N^5)\), by (17) and (22). Thus
\[
J_N=C_{N-5}+A_{N-9}+O(U_N/N^5)
\sim 6NU_{N-10}.
\tag{29}
\]

We next construct two disjoint families, each with exactly two bridge-orbits.

### Family I: two independent five-vertex pendant pieces

Start with an asymmetric bridgeless cubic core \(H\) on \(m=N-12\) vertices. Choose two nonincident edges. Subdivide each chosen edge and attach one copy of \(F_5\) by a bridge at each new vertex.

The number of choices of two nonincident edges is
\[
\binom{3m/2}{2}-3m\sim \frac98m^2.
\]
Both bridges have five-vertex pendant sides. Deleting these sides and suppressing the two degree-two vertices recovers the core and the unordered pair of chosen edges. The construction is therefore injective on isomorphism classes.

Its size is
\[
\left(\frac98+o(1)\right)N^2U_{N-12}
\sim \frac32NU_{N-10}.
\tag{30}
\]
The two bridges lie in different automorphism-orbits because contraction recovers an asymmetric core.

### Family II: a five-vertex piece behind a diamond

Let \(D_4=K_4-e\), with its two degree-two vertices as terminals. Start with an asymmetric bridgeless cubic core on \(m=N-10\) vertices and subdivide a chosen edge. Attach a chain
\[
\text{core subdivision vertex}\;-\;D_4\;-\;F_5,
\]
using the terminals and the degree-two vertex of \(F_5\).

There are exactly two bridges. Their smaller sides have orders nine and five, respectively. The bridge decomposition uniquely recovers the input, so this family has
\[
\left(\frac32+o(1)\right)NU_{N-10}
\tag{31}
\]
classes. Its bridges are in distinct orbits because their cut-side orders differ.

The two families are disjoint. Together they have
\[
(3+o(1))NU_{N-10}
\]
classes and contribute twice that many objects to \(J_N\). By (29), they exhaust \(J_N\) asymptotically. Every remaining multiple-bridge class contributes at least one object to the remaining part of \(J_N\), so there are only \(o(U_N/N^4)\) remaining classes.

Therefore
\[
M_N\sim 3NU_{N-10}
\sim \frac{1024}{81}\frac{U_N}{N^4},
\]
proving (3). In particular,
\[
\frac{M_N}{B_N}\sim \frac{32}{9N^2}.
\tag{32}
\]

This also proves the stated structural description: almost every multiple-bridge graph has exactly two bridges, and Families I and II each account for half of them asymptotically.

---

## 6. A verified bridgeless non-Hamiltonian family

The denominator still requires separate information. Here is a self-contained verification of the Petersen-fragment lower bound from the supplied attempt.

### 6.1 The fragment

Let \(P\) be the Petersen graph, choose a vertex \(p\), and put
\[
F=P-p.
\]
Then \(F\) has nine vertices and twelve edges, with three degree-two terminals.

The relevant facts are:

1. \(P\) is 3-edge-connected.
2. \(P\) is non-Hamiltonian.
3. \(F\) has no spanning path whose endpoints are two terminals.
4. Automorphisms of \(F\) induce every permutation of its terminals.

Here are direct checks.

For 3-edge-connectivity, use that \(P\) has girth five. A smaller side of an edge cut has at most five vertices. A set of at most four vertices induces a forest; a five-vertex set induces at most five edges. Thus
\[
|\delta(S)|=3|S|-2e(S)
\]
excludes cuts of size one or two.

For non-Hamiltonicity, use the outer-pentagon/inner-pentagram presentation. A Hamilton cycle would use two or four spokes. With two spokes, their indices must differ by one for the outer spanning path, but by two for the inner spanning path. With four spokes, the forced edges form two five-cycles. Both cases are impossible.

A terminal-to-terminal spanning path in \(F\), completed through \(p\), would give a Hamilton cycle of \(P\).

Finally, in the model \(P=KG(5,2)\), take \(p=\{1,2\}\). Permutations of \(\{3,4,5\}\) fix \(p\) and induce all permutations of its three neighbours. They therefore give all terminal permutations of \(F\).

### 6.2 Suitable cores are asymptotically all cores

Let \(\mathcal H_m\) be the class of connected unlabelled simple cubic graphs that are

* asymmetric;
* 3-edge-connected;
* free of any subgraph isomorphic to \(F\).

Then
\[
|\mathcal H_m|\sim U_m.
\tag{33}
\]

For the connectivity assertion, in the cubic configuration model the expected number of sets of size \(s\) having exactly \(c\) crossing edges is
\[
\binom ms
\binom{3s}{c}\binom{3(m-s)}c c!\,
\frac{(3s-c-1)!!(3(m-s)-c-1)!!}{(3m-1)!!}.
\tag{34}
\]
In a simple cubic graph, the minimum possible smaller-side sizes for \(c=0,1,2\) are respectively \(4,5,4\). Their initial terms have orders \(m^{-2},m^{-2},m^{-1}\).

Summing causes no loss of order. Direct division of consecutive admissible terms gives, away from fixed-size endpoints,
\[
\frac{s}{m-s}
\left(1+O(s^{-1})+O((m-s)^{-1})\right).
\]
The initial range is geometrically decreasing, and the central range is exponentially smaller, as in the proof of (17). Thus the probability of an edge cut of size at most two is \(O(m^{-1})\), after conditioning on simplicity and connectedness.

For the fixed fragment \(F\), there are \(O(m^9)\) vertex placements and a bounded number of half-edge assignments per placement. Twelve prescribed pairs have probability \(O(m^{-12})\). Hence
\[
\mathbb E[\#F]=O(m^{-3}).
\tag{35}
\]
Conditioning costs only a bounded factor. Equation (13), together with unlabelled asymmetry, proves (33).

### 6.3 Insertion, connectivity, and injectivity

For \(H\in\mathcal H_m\), choose a vertex \(v\). Delete \(v\), insert \(F\), and attach its three terminals to the three former neighbours of \(v\). All six attachment bijections give isomorphic graphs because every terminal permutation is induced by an automorphism of \(F\).

The result has
\[
N=m+8
\]
vertices and is non-Hamiltonian: a Hamilton cycle must use exactly two edges of the fragment’s three-edge boundary, inducing a forbidden terminal-to-terminal spanning path in \(F\).

It is also 3-edge-connected. The useful general observation is the following. Delete a vertex from a 3-edge-connected cubic graph. For a nonempty proper subset \(A\) of the remaining piece, let \(t\) be its number of terminals and \(q\) its number of edges to the rest of that piece. The two corresponding cuts in the original graph give
\[
q+t\ge3,\qquad q+3-t\ge3,
\]
so
\[
q\ge\max(t,3-t)\ge2.
\tag{36}
\]
A cut splitting both pieces of the insertion has at least four edges. A cut splitting at most one piece corresponds to a cut in one of the original cubic graphs and has at least three.

For injectivity, let \(S\) be the inserted nine-vertex set. Suppose another nine-vertex set \(T\) induces a copy of \(F\).

* If \(S,T\) overlap but are unequal, then, for \(N>18\), \(T\) splits both pieces. By (36), \(|\delta(T)|\ge4\), contradicting the three-edge boundary of \(F\).
* If \(S,T\) are disjoint, \(T\) already gives an \(F\)-subgraph in the core \(H\), contrary to its definition.

Thus the inserted fragment is unique. Contracting it recovers the vertex-rooted core.

Each asymmetric core has \(m\) distinct vertex-rootings. The resulting family therefore has exactly
\[
m|\mathcal H_m|
\sim (N-8)U_{N-8}
\sim \frac{256}{81}\frac{U_N}{N^3}
\]
classes. All are 3-edge-connected and non-Hamiltonian, proving (5).

---

## 7. What remains unresolved

Combining (2) and (5),
\[
\frac{R_N}{B_N}
\ge \left(\frac89+o(1)\right)\frac1N,
\]
which gives (6).

But this is a lower bound on the wrong part of the denominator for proving the conjecture. The desired limit requires
\[
R_N=o(U_N/N^2).
\]
The bridge enumeration, even including the more precise multiple-bridge asymptotic, supplies no such estimate.

In particular, I have not proved that almost every bridgeless non-Hamiltonian cubic graph contains the Petersen fragment. Non-Hamiltonicity arising from other local structures or from global constraints remains uncontrolled. Knowing only that almost all cubic graphs are Hamiltonian would give an \(o(U_N)\) exceptional set, which is insufficient here.

There is also no conclusion about the proposed strict monotonicity.

---

## 8. If disconnected graphs are included

The connectivity convention changes the answer.

Suppose \(NH(n)\) includes disconnected cubic graphs, while \(NHB(n)\) counts graphs of vertex-connectivity exactly one. For \(N>8\), every graph
\[
K_4\;\dot\cup\;H,
\]
where \(H\) is connected cubic on \(N-4\) vertices, is non-Hamiltonian and is not counted by \(NHB(n)\). These give \(U_{N-4}\) distinct classes. Hence
\[
NH(n)\ge B_N+U_{N-4}.
\]
By (10),
\[
U_{N-4}\sim \frac{16}{9}\frac{U_N}{N^2}.
\]
Together with (2), this yields
\[
\boxed{
\limsup_{n\to\infty}\frac{NHB(n)}{NH(n)}
\le
\frac{32/9}{32/9+16/9}
=\frac23.
}
\]

Thus the disconnected interpretation is false. For the intended connected interpretation, the results above sharpen the numerator analysis but do not resolve the conjecture.