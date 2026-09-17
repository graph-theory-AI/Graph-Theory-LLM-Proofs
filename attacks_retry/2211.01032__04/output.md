```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for every connected graph of cyclomatic number at most five, and a minimum-cycle-rank counterexample would have a bridgeless simple triangle-free cubic representative.",
  "would_publish": false,
  "caveats": "This uses the standard labelled signed-rotation-system model; cycle rank at least six remains unresolved, and literature novelty of the auxiliary identities has not been checked."
}
```

# 1. Partial results

Write
\[
\beta(G)=|E(G)|-|V(G)|+1
\]
for the cyclomatic number of a connected graph. Loops and parallel edges are allowed, and darts are labelled.

I prove the following.

### Theorem
Under the uniformly random local-rotation model and its signed-rotation analogue:

1. The conjecture holds for every connected graph \(G\) with
   \[
   1\leq \beta(G)\leq 5.
   \]

2. Consequently, it holds whenever every component obtained by deleting all bridges has cyclomatic number at most five.

3. If the conjecture has a counterexample, then among counterexamples of minimum cyclomatic number there is one that is **simple, bridgeless, cubic, and triangle-free**. Such a counterexample must have at least ten vertices.

The proof gives two local reduction inequalities and exact exponential-moment identities for cubic graphs. These go beyond a small-case enumeration.

I re-establish the signed-intersection-form framework used in the supplied previous attempt; the proof below does not depend on that attempt’s numerical tables.

---

# 2. Probability conventions and the intersection form

Let
\[
a(G)=\mathbb E[F]
\]
be the orientable expected face count. Let
\[
b(G)=\mathbb E[F_{\mathrm s}]
\]
be the expected face count when the rotations are uniform and every edge independently receives a fair twist bit. Thus \(F_{\mathrm s}\) includes both orientable and nonorientable outcomes. Put
\[
\Delta(G)=a(G)-b(G).
\]

For a connected graph of cycle rank \(r\), exactly a proportion \(2^{-r}\) of signatures are balanced, hence orientable. Conditional on being balanced, vertex switching shows that the rotation distribution gives the usual orientable model. Therefore, if \(a_-(G)\) denotes the average conditioned on nonorientability,
\[
b(G)=2^{-r}a(G)+(1-2^{-r})a_-(G).
\]
For \(r\geq1\),
\[
b(G)\leq a(G)
\quad\Longleftrightarrow\quad
a_-(G)\leq a(G).
\tag{2.1}
\]
Thus proving \(\Delta(G)\geq0\) settles either convention for “random nonorientable embedding.” For a tree, the conditional nonorientable model is undefined, but \(a(G)=b(G)=1\).

## 2.1. Binary intersection forms

Let
\[
Z=Z_1(G;\mathbb F_2)
\]
be the cycle space, of dimension \(r\). For an edge \(e\), let
\[
\ell_e:Z\longrightarrow\mathbb F_2
\]
record whether a cycle-space vector uses \(e\).

A ribbon embedding has a symmetric mod-\(2\) intersection form \(B\) on \(Z\). Its number of faces satisfies
\[
F=1+\nu(B),
\tag{2.2}
\]
where \(\nu\) denotes nullity over \(\mathbb F_2\).

Indeed, the ribbon surface retracts onto \(G\), and for a connected compact surface with \(F\) boundary components, the radical of its mod-\(2\) intersection form has dimension \(F-1\). The boundary classes span that radical, with their single relation that their sum is zero.

For an orientable rotation system \(R\), write its alternating intersection form as \(A_R\). If \(t_e\) is the twist bit of edge \(e\), then
\[
B_{R,t}
=
A_R+\sum_{e\in E(G)}t_e\,\ell_e\ell_e^{\mathsf T}.
\tag{2.3}
\]
One way to verify the effect of twisting a nonbridge \(e\) is to choose a spanning tree avoiding \(e\), normalize its signs, and contract it. Twisting \(e\) then changes just the diagonal entry of the corresponding loop-band. In invariant notation, this change is \(\ell_e\ell_e^{\mathsf T}\). A bridge has \(\ell_e=0\) and does not affect the form.

Switching at a vertex reverses its rotation and toggles its incident signatures. Consequently, at a loopless cubic vertex with incident edges \(e_1,e_2,e_3\), reversing the rotation changes \(A_R\) by
\[
L_v=\sum_{i=1}^3\ell_{e_i}\ell_{e_i}^{\mathsf T}.
\tag{2.4}
\]
Here
\[
\ell_{e_1}+\ell_{e_2}+\ell_{e_3}=0.
\tag{2.5}
\]

---

# 3. An edge-deletion identity

We first record the linear algebra needed for the reductions.

### Bordering lemma
Let \(M\) be symmetric, let \(K=\ker M\), and let \(w\) be a column vector. Consider
\[
M'=
\begin{pmatrix}
M&w\\
w^{\mathsf T}&t
\end{pmatrix}.
\]

* If \(w\) does not annihilate \(K\), then
  \[
  \nu(M')=\nu(M)-1.
  \]
* If \(w\) annihilates \(K\), choose \(z\) with \(Mz=w\). Then \(M'\) is congruent to
  \[
  M\oplus[t+w^{\mathsf T}z].
  \]

In particular:

* if \(M\) is alternating and \(t=0\), the nullity increment is \(+1\) when \(w\) annihilates \(K\), and \(-1\) otherwise;
* if \(t\) is independent and fair, the expected increment is \(1/2\) when \(w\) annihilates \(K\), and \(-1\) otherwise.

These statements follow by eliminating a nonsingular part of \(M\), or directly by elementary congruences. In the alternating case,
\[
w^{\mathsf T}z=z^{\mathsf T}Mz=0.
\]

## 3.1. Monofacial probabilities in algebraic form

For a nonbridge \(e\), define
\[
p_e^+
=
\Pr\bigl(\ell_e\text{ annihilates }\ker A_R\bigr),
\]
and similarly
\[
p_e^{\mathrm s}
=
\Pr\bigl(\ell_e\text{ annihilates }\ker B_{R,t}\bigr).
\]

Then
\[
a(G)-a(G-e)=1-2p_e^+,
\tag{3.1}
\]
and
\[
b(G)-b(G-e)=2-3p_e^{\mathrm s}.
\tag{3.2}
\]
Moreover,
\[
p_e^{\mathrm s}\geq\frac12,
\qquad
b(G)-b(G-e)\leq\frac12.
\tag{3.3}
\]

Here is a verification. Choose a cycle-space basis whose first \(r-1\) vectors lie in \(G-e\), so that \(\ell_e\) is the last coordinate. The intersection matrix is a bordering of the matrix for \(G-e\).

If the bordering vector does not annihilate the smaller radical, the nullity drops by one and every vector in the new radical has last coordinate zero. Otherwise:

* orientably, the nullity rises by one, and the new radical has a vector with last coordinate one;
* in the signed model, the final diagonal bit is fair, so with equal probabilities the nullity stays unchanged or rises by one.

This gives (3.1)–(3.3).

Deleting the darts of \(e\) from uniform cyclic orders leaves uniform cyclic orders on \(G-e\), so the smaller-form averages really are \(a(G-e)\) and \(b(G-e)\).

---

# 4. Digon and triangle reductions

Two expansions will be useful.

* \(D(G,e)\): replace an edge \(e=ab\) by
  \[
  a-x,\qquad xy\text{ twice},\qquad y-b.
  \]
  This increases the cycle rank by one.

* \(Y(G,v)\): replace a cubic vertex \(v\) by a triangle, attaching its three former incident edges to the three triangle vertices. This also increases the cycle rank by one.

For \(Y(G,v)\), assume that none of the three edges incident with \(v\) is a bridge.

## 4.1. Exact expectation recurrences

For a nonbridge \(e\),
\[
a(D(G,e))
=
\frac{a(G)+a(G-e)+1}{2},
\tag{4.1}
\]
\[
b(D(G,e))
=
\frac{3b(G)+b(G-e)+1}{4}.
\tag{4.2}
\]

If \(e_1,e_2,e_3\) are incident with \(v\), then
\[
a(Y(G,v))
=
\frac{a(G)+\sum_{i=1}^3a(G-e_i)+1}{4},
\tag{4.3}
\]
\[
b(Y(G,v))
=
\frac{5b(G)+\sum_{i=1}^3b(G-e_i)+1}{8}.
\tag{4.4}
\]

### Proof of the local distributions

In each expansion, identify the enlarged cycle space with
\[
Z(G)\oplus\langle c\rangle,
\]
where \(c\) is the new digon or triangle cycle.

For the digon expansion, deleting one of the parallel edges and suppressing the new degree-two vertices recovers \(G\). The old intersection form is therefore distributed exactly as the form for \(G\). The cross-term with \(c\) lies in
\[
\{0,\ell_e\}.
\]
Reversing either new cubic rotation toggles that cross-term by \(\ell_e\), so it is uniform on this two-element list.

For the triangle expansion, delete one internal triangle edge and identify the resulting subdivided graph with \(G\). The rotations at the other two new vertices independently toggle the cross-term by \(\ell_{e_1}\) and \(\ell_{e_2}\). Thus the cross-term is uniform on
\[
\{0,\ell_{e_1},\ell_{e_2},\ell_{e_3}\}.
\]
It lies in their span because a cycle avoiding the old vertex is disjoint from the new triangle.

In both constructions, the new diagonal entry is zero orientably. In the signed model, twisting the deleted internal edge changes only that new diagonal entry, so it is an independent fair bit.

Applying the bordering lemma gives the increments
\[
a(D)-a(G)=p_e^+,
\qquad
b(D)-b(G)=-\frac14+\frac34p_e^{\mathrm s},
\]
and
\[
a(Y)-a(G)=\frac{\sum_i p_{e_i}^+-1}{2},
\]
\[
b(Y)-b(G)=\frac{3\sum_i p_{e_i}^{\mathrm s}-5}{8}.
\]
Substitution from (3.1) and (3.2) proves the recurrences. ∎

## 4.2. The digon comparison

Writing
\[
\delta_e=b(G)-b(G-e),
\]
equations (4.1)–(4.2) give
\[
\Delta(D(G,e))
=
\frac{\Delta(G)+\Delta(G-e)}2
+\frac{1-\delta_e}{4}.
\]
Using \(\delta_e\leq1/2\),
\[
\boxed{\;
\Delta(D(G,e))
\geq
\frac{\Delta(G)+\Delta(G-e)}2+\frac18.
\;}
\tag{4.5}
\]

Thus, if the conjecture holds for \(G\) and \(G-e\), it holds strictly for the digon expansion.

## 4.3. A cubic-vertex estimate

We need a slightly stronger estimate for the triangle expansion.

### Lemma
At a cubic vertex with three nonbridge incident edges,
\[
\sum_{i=1}^3 p_{e_i}^{\mathrm s}\geq\frac{15}{8}.
\tag{4.6}
\]
Equivalently,
\[
\sum_{i=1}^3\bigl(b(G)-b(G-e_i)\bigr)\leq\frac38.
\tag{4.7}
\]

### Proof

Put
\[
U=\langle \ell_{e_1},\ell_{e_2}\rangle.
\]
The three edge functionals are nonzero, and their sum is zero. Thus they are precisely the three nonzero elements of the two-dimensional space \(U\).

Condition on the rotations and all other edge signs. The three remaining independent twist bits add
\[
t_1\ell_{e_1}\ell_{e_1}^{\mathsf T}
+t_2\ell_{e_2}\ell_{e_2}^{\mathsf T}
+t_3(\ell_{e_1}+\ell_{e_2})(\ell_{e_1}+\ell_{e_2})^{\mathsf T}.
\]
These additions make the symmetric \(2\times2\) block on the quotient dual to \(U\) uniform.

Let \(W=\bigcap_{\ell\in U}\ker\ell\). Split off a nonsingular part of the form restricted to \(W\). On the remaining space the matrix has the shape
\[
\begin{pmatrix}
S&E\\
E^{\mathsf T}&0
\end{pmatrix},
\]
where \(S\) is uniform symmetric \(2\times2\), and \(E\) is fixed. Put \(t=\operatorname{rank}E\).

The projection of the radical onto the two-dimensional quotient is the radical of the restriction of \(S\) to
\[
L=\ker E^{\mathsf T},
\qquad \dim L=2-t.
\]
That restriction is a uniform symmetric form on \(L\).

If this projected radical has dimension \(j\), exactly
\[
2^{2-j}-1
\]
of the three nonzero functionals in \(U\) annihilate the full radical. The resulting conditional expectations are
\[
\begin{array}{c|c}
t&\text{expected number of annihilating nonzero functionals}\\ \hline
0&15/8\\
1&2\\
2&3
\end{array}
\]
For \(t=0\), this uses the rank counts \(1,3,4\) for the eight symmetric \(2\times2\) matrices. Hence the expectation is always at least \(15/8\).

Equation (4.7) follows from (3.2):
\[
\sum_i\bigl(b(G)-b(G-e_i)\bigr)
=
6-3\sum_i p_{e_i}^{\mathrm s}
\leq\frac38.
\]
∎

Combining this with (4.3)–(4.4) gives
\[
\boxed{\;
\Delta(Y(G,v))
\geq
\frac{\Delta(G)+\sum_{i=1}^3\Delta(G-e_i)}4
+\frac{5}{64}.
\;}
\tag{4.8}
\]

So a triangle expansion also satisfies the conjecture strictly whenever all the smaller graphs appearing on the right satisfy it.

---

# 5. A minimum counterexample can be taken cubic and triangle-free

## 5.1. Cubic resolution preserves the comparison on average

Deleting a pendant edge or suppressing a degree-two vertex preserves both expected face counts. In the signed model, suppression replaces the two edge signs by their sum, which remains a fair bit.

After these operations, suppose all degrees are at least three. Replace every degree-\(d\) vertex by a fixed trivalent tree with \(d\) ports. Assign the original incident darts uniformly to those ports.

Contracting the internal tree edges recovers the original graph. For every fixed internal rotation system, the uniform port assignment produces a uniform cyclic order of the original darts. Independently at the different vertices, this produces exactly the original random-rotation distribution.

The same assertion holds for the signed model: normalize the internal tree-edge signs to zero by switching. Switching reverses some local rotations but preserves their uniform distribution, and the remaining edge signs are still independent and fair.

Consequently, if \(H_\lambda\) ranges over the cubic resolutions specified by the port assignments,
\[
\Delta(G)=\mathbb E_\lambda[\Delta(H_\lambda)].
\tag{5.1}
\]
Every \(H_\lambda\) has the same cycle rank as \(G\). Therefore a counterexample has a cubic resolution that is also a counterexample.

A connected cubic graph of cycle rank \(r\) has
\[
|V|=2r-2.
\tag{5.2}
\]

## 5.2. Bridges, loops, digons, and triangles

If a bridge joins connected graphs \(G_1,G_2\), then in every signed embedding
\[
F(G)=F(G_1)+F(G_2)-1.
\]
Thus
\[
\Delta(G)=\Delta(G_1)+\Delta(G_2).
\tag{5.3}
\]

Now take a counterexample of minimum cycle rank and a cubic counterexample of that rank supplied by (5.1).

* It has no bridge. Both sides of a bridge in a cubic graph have positive, strictly smaller cycle rank, contradicting minimality and (5.3).

* It has no loop: the third incident edge at a looped cubic vertex would be a bridge.

* The two-vertex graph with three parallel edges is not a counterexample. Its orientable overlap matrix is uniform on
  \[
  0,\qquad
  \begin{pmatrix}0&1\\1&0\end{pmatrix},
  \]
  giving
  \[
  a=2,\qquad b=\frac{13}{8}.
  \]

* Otherwise, a double edge is a digon expansion of a smaller graph. Its two external neighbours are distinct; if they coincided, the remaining edge at that common neighbour would be a bridge. The graph outside the digon is connected, since otherwise an external digon edge would be a bridge. Hence the inverse reduction produces \(G\) and \(G-e\) of strictly smaller cycle rank, and (4.5) rules out the counterexample.

* Once parallel edges are excluded, contracting a triangle produces a smaller cubic graph \(G\), with no bridge incident to the contracted vertex. The three graphs \(G-e_i\) are connected and have still smaller cycle rank. Equation (4.8) rules out the counterexample.

This proves:

### Structural conclusion
If the conjecture fails, a counterexample of minimum cycle rank has a representative that is simple, bridgeless, cubic, and triangle-free.

---

# 6. Exact exponential moments for cubic graphs

The remaining small-rank cases are handled without enumerating all rotation systems.

For a loopless cubic graph, every cycle-space vector induces a vertex-disjoint union of cycles. For \(x\in Z_1(G;\mathbb F_2)\), let \(c(x)\) be its number of cycle components, with \(c(0)=0\). Define
\[
P_G(z)=\sum_{x\in Z_1(G;\mathbb F_2)}z^{c(x)}.
\]

### Proposition
For a connected loopless cubic graph of cycle rank \(r\),
\[
\boxed{\;
\mathbb E\!\left[2^{F-1}\right]
=
2^{-r}P_G(3),
\;}
\tag{6.1}
\]
and
\[
\boxed{\;
\mathbb E\!\left[2^{F_{\mathrm s}-1}\right]
=
2^{-r}P_G(2).
\;}
\tag{6.2}
\]

### Proof

Fix a cycle-space vector \(x\), and let \(W_x\) be the vertices on its cycle components. Write \(\beta(H)\) for the cycle-space dimension even when \(H\) is disconnected.

In the signed model, (2.3) gives
\[
B_{R,t}x
=
A_Rx+\sum_{e\in E(x)}t_e\ell_e.
\]
The span of these edge functionals has dimension
\[
r-\beta(G-W_x).
\]
Indeed, its annihilator consists of cycles avoiding the edges of \(x\); in a cubic graph, such cycles must avoid all vertices of \(x\).

Moreover, \(A_Rx\) belongs to that span: it vanishes on cycles disjoint from \(W_x\), because those cycles are geometrically disjoint from \(x\). Therefore
\[
\Pr(x\in\ker B_{R,t})
=
2^{-r+\beta(G-W_x)}.
\tag{6.3}
\]

For the orientable model, reversing a cubic rotation at a vertex on \(x\) changes \(A_Rx\) by the functional of the third edge at that vertex, by (2.4)–(2.5). Let \(Q_x\) be the set of these third edges. The span of their functionals has dimension
\[
r-\beta(G-Q_x)
=
r-c(x)-\beta(G-W_x).
\]
The relevant affine space contains zero: choose the rotations so that each component of \(x\) is a facial cycle. These choices are compatible because the components are vertex-disjoint. Hence
\[
\Pr(x\in\ker A_R)
=
2^{-r+c(x)+\beta(G-W_x)}.
\tag{6.4}
\]

Now sum over \(x\), using
\[
2^{\nu(M)}=|\ker M|.
\]

The sum
\[
\sum_x2^{\beta(G-W_x)}
\]
counts ordered pairs of vertex-disjoint cycle-space subgraphs. Their union is a cycle-space subgraph \(z\), and each cycle component of \(z\) may be assigned to either member of the pair. Thus the sum equals \(P_G(2)\).

Similarly,
\[
\sum_x2^{c(x)+\beta(G-W_x)}
\]
counts the same pairs with weight \(2^{c(x)}\). Each component of the union contributes weight \(2\) if assigned to the first member and weight \(1\) if assigned to the second. The sum therefore equals \(P_G(3)\).

Equations (2.2), (6.3), and (6.4) prove the proposition. ∎

These are identities for one exponential moment, not by themselves a proof comparing the means. The small dimensions below provide the additional control needed.

---

# 7. Proof for cycle rank at most five

For \(r=0\), both models have one face. For \(r=1\), the orientable intersection matrix is the zero \(1\times1\) matrix, whereas the signed matrix is a fair scalar. Thus
\[
a(G)=2,\qquad b(G)=\frac32.
\]

Suppose there were a counterexample with \(r\leq5\), and choose one of minimum cycle rank. By Section 5, it has a simple, bridgeless, triangle-free cubic representative \(H\), with
\[
|V(H)|=2r-2.
\]

There is no simple triangle-free cubic graph on two or four vertices. It remains to consider \(r=4\) and \(r=5\).

## 7.1. Cycle rank four

A simple triangle-free cubic graph on six vertices is \(K_{3,3}\). To see this, choose a vertex and its three neighbours. The neighbours are independent, and each must be adjacent to both remaining vertices.

Every nonzero cycle-space vector of \(K_{3,3}\) is a single cycle: two disjoint cycles would require at least eight vertices. Therefore
\[
P_{K_{3,3}}(2)=1+15\cdot2=31,
\]
\[
P_{K_{3,3}}(3)=1+15\cdot3=46.
\]

The graph is nonplanar by the elementary bipartite planar bound \(m\leq2n-4\). Its alternating \(4\times4\) intersection matrix consequently has nullity only \(0\) or \(2\). From (6.1),
\[
\mathbb E[2^{\nu(A_R)}]=\frac{46}{16}.
\]
It follows that
\[
\Pr(\nu(A_R)=2)
=
\frac{46/16-1}{3}
=
\frac58,
\]
and hence
\[
a(K_{3,3})=1+2\cdot\frac58=\frac94.
\]

On the other hand, Jensen’s inequality and (6.2) give
\[
b(K_{3,3})
=
1+\mathbb E[\nu(B)]
\leq
1+\log_2\mathbb E[2^{\nu(B)}]
=
1+\log_2\frac{31}{16}
<2.
\]
Thus \(K_{3,3}\) is not a counterexample.

## 7.2. Cycle rank five

Let \(H\) be a simple triangle-free cubic graph on eight vertices.

Every nonzero cycle-space vector has either one cycle component or two components. In the latter case it consists of two disjoint \(4\)-cycles. Let
\[
k=\#\{x\in Z_1(H;\mathbb F_2):c(x)=2\}.
\]
Since the cycle space has \(32\) elements,
\[
P_H(2)=63+2k,
\qquad
P_H(3)=94+6k.
\tag{7.1}
\]

We first show
\[
0\leq k\leq6.
\tag{7.2}
\]
A \(4\)-cycle can belong to at most one such pair: the remaining four vertices induce a triangle-free graph, and hence contain at most one \(4\)-cycle. At a fixed vertex, a \(4\)-cycle is determined by a pair of its neighbours and another common neighbour of that pair. There are at most
\[
\binom32\cdot2=6
\]
such cycles through the vertex. Thus the total number of \(4\)-cycles is at most
\[
\frac{8\cdot6}{4}=12,
\]
and \(2k\leq12\).

### Lower bound on the orientable mean

An alternating \(5\times5\) matrix has
\[
1\leq \nu(A_R)\leq5.
\]
The chord joining the endpoints of \(2^u\) on \([1,5]\) gives
\[
u\geq1+\frac{2}{15}(2^u-2).
\]
Using (6.1) and (7.1),
\[
\begin{aligned}
a(H)
&\geq
2+\frac{2}{15}
\left(\frac{94+6k}{32}-2\right)\\
&=
2+\frac{k+5}{40}.
\end{aligned}
\tag{7.3}
\]

### Upper bound on the signed mean

Jensen’s inequality gives
\[
b(H)\leq1+\log_2\frac{63+2k}{32}.
\]
Using the tangent bound
\[
\log_2 x\leq1+\frac{x-2}{2\ln2},
\]
we obtain
\[
b(H)
\leq
2+\frac{2k-1}{64\ln2}.
\tag{7.4}
\]

If \(k=0\), the right side is less than \(2\), whereas (7.3) is greater than \(2\).

If \(1\leq k\leq6\), use \(\ln2>5/8\) and \(2k-1\leq k+5\):
\[
b(H)
<
2+\frac{2k-1}{40}
\leq
2+\frac{k+5}{40}
\leq a(H).
\]
Thus no such eight-vertex graph is a counterexample.

This proves the conjecture for every connected graph of cycle rank at most five.

Finally, repeated use of bridge additivity (5.3) proves the stated extension to graphs whose bridge-deleted components all have cycle rank at most five. ∎

---

# 8. What remains open

The argument leaves the general conjecture unresolved. A minimum-cycle-rank counterexample, if one exists, must now have a simple bridgeless triangle-free cubic representative of cycle rank at least six, hence at least ten vertices.

The exponential-moment identities show
\[
\mathbb E[2^{F-1}]
\geq
\mathbb E[2^{F_{\mathrm s}-1}]
\]
for every cubic graph, since \(P_G(3)\geq P_G(2)\). But comparison of this one exponential moment does **not** imply comparison of the means. The small-rank proof used additional nullity restrictions that become too weak in general.

Nor can one remove the rotation average. For example,
\[
A=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
has nullity zero, while adding a uniform diagonal gives average nullity \(1/4\). Thus a pointwise comparison for individual orientable rotations is false.

The results above are therefore a genuine partial resolution, not a proof of the full conjecture.