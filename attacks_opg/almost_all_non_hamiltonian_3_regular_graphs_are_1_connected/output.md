```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Sharp bridge enumeration and Petersen-fragment constructions give precise asymptotic bounds, but not the upper bound needed for the intended connected-graph conjecture.",
  "would_publish": false,
  "caveats": "Connected simple graphs are assumed, and no novelty claim is made. If disconnected graphs are included in NH(n), the stated limit is false."
}
```

# 1. Interpretation and partial result

I treat the intended version: **connected, simple cubic graphs, counted up to isomorphism**. The connectivity convention is essential; see Section 6.

Write \(N=2n\), and let
\[
\begin{aligned}
U_N&=\#\{\text{connected unlabelled simple cubic graphs on }N\text{ vertices}\},\\
B_N&=\#\{\text{such graphs containing a bridge}\},\\
R_N&=\#\{\text{such graphs that are bridgeless and non-Hamiltonian}\}.
\end{aligned}
\]
A connected cubic graph has a cut-vertex if and only if it has a bridge: at a cut-vertex, one component of its deletion receives only one of the three incident edges. Thus
\[
NH(n)=B_{2n}+R_{2n},\qquad NHB(n)=B_{2n}.
\]

The partial results below are
\[
\boxed{B_N\sim \frac{32}{9}\frac{U_N}{N^2}}
\tag{1}
\]
and
\[
\boxed{R_N\ge \left(\frac{256}{81}+o(1)\right)\frac{U_N}{N^3}.}
\tag{2}
\]

Moreover, almost every graph counted by \(B_N\) has exactly one bridge, and its smaller bridge-side has five vertices.

Consequently, the conjecture is equivalent to the still-unproved estimate
\[
R_N=o(U_N/N^2).
\tag{3}
\]
The lower bound (2) also gives the necessary convergence-rate restriction
\[
\boxed{\frac{NHB(n)}{NH(n)}
\le 1-\frac{4}{9n}+o(n^{-1}).}
\tag{4}
\]
In particular, if the conjecture is true, convergence cannot be faster than order \(1/n\).

These are enumeration results, not a resolution of the Hamiltonicity question.

---

# 2. Enumeration input and an important labelling issue

I use the classical fixed-degree labelled/unlabelled regular-graph enumeration theorem. If \(L_N\) counts connected labelled simple cubic graphs and
\[
v_N=\frac{(3N-1)!!}{6^N N!},
\]
then, along even \(N\),
\[
L_N\sim e^{-2}N!v_N,
\qquad
U_N\sim e^{-2}v_N.
\tag{5}
\]
The unlabelled assertion in (5) is a standard enumeration input; it is not being inferred merely from asymmetry with high probability in the labelled model.

Two consequences will be used repeatedly.

First,
\[
\frac{v_{N-2}}{v_N}
=\frac{12N}{(3N-1)(3N-5)}.
\tag{6}
\]
Hence, for every fixed even \(k\),
\[
\frac{U_{N-k}}{U_N}
\sim
\left(\frac{2}{\sqrt3}\right)^kN^{-k/2}.
\tag{7}
\]

Second, almost all **unlabelled** cubic graphs are asymmetric. Indeed,
\[
U_N-\frac{L_N}{N!}
=\sum_{[G]}\left(1-\frac1{|\operatorname{Aut}G|}\right)
=o(U_N),
\]
and each symmetric isomorphism class contributes at least \(1/2\).

More generally, any graph property holding with probability \(1-o(1)\) in the labelled model also holds for \(1-o(1)\) of the unlabelled isomorphism classes. For a bad property \(\mathcal A\),
\[
U_N(\mathcal A)
\le \frac{L_N(\mathcal A)}{N!}
+\left(U_N-\frac{L_N}{N!}\right).
\tag{8}
\]

This distinction matters at the rare-event scale considered here. The leading bridge-containing graphs have four automorphisms, so their labelled and unlabelled densities have different leading constants.

---

# 3. Sharp enumeration of bridge-containing graphs

## 3.1 Near-cubic graphs with one degree-two vertex

For odd \(s\), let \(A_s\) count connected unlabelled simple graphs having one vertex of degree two and all other vertices of degree three. The degree-two vertex is automatically distinguished.

Let \(E_m\) count connected unlabelled simple cubic graphs with a distinguished edge, up to isomorphism. Since almost all unlabelled cubic graphs are asymmetric,
\[
E_m\sim \frac{3m}{2}U_m.
\tag{9}
\]

There is an exact recurrence
\[
\boxed{A_s=E_{s-1}+A_{s-2}+A_{s-4},}
\qquad s\ge5,
\tag{10}
\]
with \(A_1=A_3=0\).

To prove it, let \(r\) be the degree-two vertex and let its neighbours be \(a,b\).

* **If \(a,b\) are nonadjacent:** suppress \(r\). This gives a simple cubic graph with the newly created edge distinguished, contributing \(E_{s-1}\).

* **If \(a,b\) are adjacent:** let their third neighbours be \(x,y\), respectively.
  * If \(x\ne y\), replace the triangle \(rab\) by one degree-two vertex adjacent to \(x,y\). This is a bijection with the objects counted by \(A_{s-2}\).
  * If \(x=y=t\), the four vertices \(r,a,b,t\) induce a diamond, with a single edge from \(t\) to the rest. Delete these four vertices; the endpoint of that edge in the remaining graph becomes the unique degree-two vertex. This is a bijection with the objects counted by \(A_{s-4}\).

All resulting graphs remain connected and simple, and these cases are disjoint and exhaustive.

From (6), (9), and (10), induction gives the uniform bound
\[
A_s=O(sv_{s-1}).
\tag{11}
\]
The last two terms of (10) are then smaller than \(E_{s-1}\) by a factor \(O(1/s)\), so
\[
A_s\sim E_{s-1}\sim \frac{3(s-1)}2U_{s-1}.
\tag{12}
\]

In particular, \(A_5=1\). Its unique graph, denoted \(F_5\), is obtained by subdividing one edge of \(K_4\).

## 3.2 Counting distinguished bridges

Let \(D_N\) count connected unlabelled cubic graphs with a distinguished bridge, up to isomorphism. Equivalently,
\[
D_N=\sum_{[G]} \#\{\operatorname{Aut}(G)\text{-orbits of bridges of }G\}.
\]
Thus \(B_N\le D_N\).

Deleting a bridge produces two graphs counted by the \(A_s\). Both orders are odd and at least five. Consequently,
\[
D_N=
\sum_{\substack{5\le s<N/2\\s\text{ odd}}}A_sA_{N-s}
+
\mathbf1_{\{N/2\text{ odd}\}}
\binom{A_{N/2}+1}{2}.
\tag{13}
\]

The term \(s=5\) dominates:
\[
D_N=A_{N-5}+O(U_N/N^3).
\tag{14}
\]

Here is a uniform tail justification. By (11), it suffices to estimate
\[
T_N(s)=s(N-s)v_{s-1}v_{N-s-1}.
\]
For admissible \(s\),
\[
\frac{T_N(s+2)}{T_N(s)}
=\frac{h(s)}{h(N-s-2)},
\]
where
\[
h(x)=\frac{(x+2)(9x^2-4)}{12x(x+1)}
=\frac1{12}\left(9x+9-\frac8x-\frac5{x+1}\right).
\]
The function \(h\) is increasing for positive \(x\). Thus the terms decrease up to the midpoint. For \(s\le N/4\), their successive ratios are at most \(1/2\) for all sufficiently large \(N\). The remaining central range is exponentially smaller than the initial term. Therefore
\[
\sum_{\substack{7\le s\le N/2\\s\text{ odd}}}T_N(s)
=O(T_N(7))
=O(Nv_{N-8})
=O(U_N/N^3),
\]
proving (14).

By (12),
\[
D_N\sim \frac{3(N-6)}2U_{N-6}.
\tag{15}
\]

## 3.3 Removing the distinguished-bridge overcount

An upper bound on distinguished bridges alone is not enough: graphs can have several bridge-orbits. A matching lower bound avoids that issue.

Let \(E_m^{\mathrm{bf}}\) count edge-rooted bridgeless connected cubic graphs. Since
\[
B_m\le D_m=O(U_m/m^2),
\]
we have
\[
E_m-E_m^{\mathrm{bf}}
\le \frac{3m}{2}B_m
=O(U_m/m).
\]
Together with (9), this gives
\[
E_m^{\mathrm{bf}}\sim E_m.
\tag{16}
\]

Starting with an edge-rooted bridgeless cubic graph on \(N-6\) vertices:

1. subdivide its distinguished edge by a new vertex \(x\);
2. take a disjoint copy of \(F_5\), whose degree-two vertex is \(r\);
3. add the edge \(xr\).

The result is a simple connected cubic graph with **exactly one bridge**, namely \(xr\). For \(N>10\), its five-vertex side is uniquely recognizable, and deleting it and suppressing \(x\) recovers the edge-rooted input. Hence
\[
B_N\ge E_{N-6}^{\mathrm{bf}}.
\tag{17}
\]

Combining (15)–(17),
\[
B_N\sim \frac{3(N-6)}2U_{N-6}.
\]
Now (7), with \(k=6\), gives
\[
\frac{B_N}{U_N}
\sim \frac{3N}{2}\frac{64}{27N^3}
=\frac{32}{9N^2},
\]
which proves (1).

The construction in (17) accounts for \(1-o(1)\) of all bridge-containing graphs. This proves the structural assertion about their unique bridge and five-vertex side.

### Labelled version

The graph \(F_5\) has four automorphisms, all fixing its degree-two vertex. When the core is asymmetric, the constructed graph has exactly these four automorphisms. Asymmetric cores account for \(1-o(1)\) of the preceding construction.

It follows that, for labelled connected cubic graphs,
\[
\boxed{\frac{B_N^{\mathrm{lab}}}{L_N}
\sim \frac{8}{9N^2}.}
\tag{18}
\]

---

# 4. A bridgeless non-Hamiltonian family of order \(U_N/N^3\)

The next construction establishes (2). The counting is made injective explicitly.

## 4.1 The Petersen fragment

Let \(P\) be the Petersen graph, choose a vertex \(p\), and put
\[
F=P-p.
\]
Then \(F\) has nine vertices, twelve edges, and three degree-two vertices, called its terminals.

The following properties are needed:

1. \(P\) is 3-edge-connected and non-Hamiltonian.
2. \(F\) has no spanning path whose endpoints are two terminals.
3. \(\operatorname{Aut}(F)\) induces all six permutations of the terminals; the kernel of this action has order two.

For completeness:

* Write the Petersen graph with outer vertices \(u_i\), inner vertices \(v_i\), and edges
  \[
  u_iu_{i+1},\quad u_iv_i,\quad v_iv_{i+2},
  \qquad i\pmod5.
  \]
  A Hamilton cycle must use two or four spokes. With two spokes, the outer spanning path requires their indices to differ by \(1\), whereas the inner spanning path requires them to differ by \(2\), a contradiction. With four spokes, rotate so that \(u_0v_0\) is omitted. The forced edges give two five-cycles:
  \[
  u_0u_1v_1v_4u_4u_0,\qquad
  u_2u_3v_3v_0v_2u_2.
  \]
  Thus there is no Hamilton cycle.
* Its girth is five. A smaller side of an edge cut has at most five vertices. Sets of at most four vertices induce forests, and a five-vertex set induces at most five edges. The formula
  \[
  |\delta(S)|=3|S|-2e(S)
  \]
  then excludes cuts of size one or two.
* A terminal-to-terminal spanning path in \(F\), together with \(p\), would give a Hamilton cycle in \(P\).
* In the model \(P=KG(5,2)\), take \(p=\{1,2\}\). The five maximum independent sets are precisely the four-element stars, so \(\operatorname{Aut}(P)=S_5\). The stabilizer of \(p\) is \(S_2\times S_3\); its \(S_3\) factor permutes the terminals and its \(S_2\) factor fixes them. Every automorphism of \(F\) extends over \(p\), establishing the claim.

## 4.2 Almost all cores are suitable

Let \(\mathcal H_m\) consist of connected unlabelled simple cubic graphs that are

* asymmetric;
* 3-edge-connected;
* free of any subgraph isomorphic to \(F\).

Then
\[
|\mathcal H_m|\sim U_m.
\tag{19}
\]

Here are the required probabilistic estimates.

In the cubic configuration model, the expected number of vertex sets of size \(s\) having exactly \(c\) crossing edges is
\[
\binom ms
\binom{3s}{c}\binom{3(m-s)}c c!\,
\frac{(3s-c-1)!!(3(m-s)-c-1)!!}{(3m-1)!!}.
\tag{20}
\]
In a simple cubic graph, for \(c=0,1,2\), the respective minimum possible smaller-side sizes are \(4,5,4\). Summing (20) over \(s\le m/2\) gives \(O(m^{-1})\): the initial terms have orders \(m^{-2},m^{-2},m^{-1}\), respectively, and the same successive-term argument used in Section 3 bounds the tails. Conditioning on simplicity and connectedness costs only a bounded factor. Thus a labelled connected cubic graph is 3-edge-connected with probability \(1-o(1)\).

For the fixed fragment \(F\), configuration-model subgraph counting gives
\[
\mathbb E[\#F]=O(m^{9-12})=O(m^{-3}).
\]
Indeed, there are \(O(m^9)\) vertex placements and a bounded number of half-edge assignments, each requiring twelve prescribed pairs.

Transfer by (8), followed by the asymmetry consequence of (5), proves (19).

## 4.3 Inflation and injectivity

For \(H\in\mathcal H_m\), choose a vertex \(v\). Delete \(v\), insert a copy of \(F\), and join its three terminals to the former neighbours of \(v\).

All six attachment bijections give isomorphic graphs, because \(\operatorname{Aut}(F)\) induces the full symmetric group on the terminals. The new order is
\[
N=m+8.
\]

The resulting graph \(G\) is non-Hamiltonian. The inserted fragment has a three-edge boundary, so a Hamilton cycle would use exactly two of those edges and induce a terminal-to-terminal spanning path in \(F\), which is impossible.

It is also 3-edge-connected. To see this, consider either of the two pieces obtained by deleting a vertex from a 3-edge-connected cubic graph. If a nonempty proper subset \(A\) of that piece contains \(t\) of its three terminals and has \(q\) edges to the rest of the piece, then
\[
q+t\ge3,\qquad q+3-t\ge3,
\]
so
\[
q\ge\max(t,3-t)\ge2.
\tag{21}
\]
A cut splitting both pieces therefore has at least four edges. A cut not splitting both corresponds to a cut in one of the original 3-edge-connected graphs and has at least three edges.

Finally, the inserted \(F\) is uniquely recognizable when \(N>18\). Let \(S\) be its vertex set, and suppose another nine-vertex set \(T\) induces an \(F\)-fragment.

* If \(S,T\) overlap but are unequal, then \(T\) splits both pieces. Equation (21) gives \(|\delta(T)|\ge4\), contradicting the three-edge boundary of an \(F\)-fragment.
* If \(S,T\) are disjoint, then \(T\) already gives a copy of \(F\) in the core \(H\), contrary to its definition.

Thus contraction of the unique fragment recovers the vertex-rooted core. The construction is injective on vertex-rooted isomorphism classes.

Because every core is asymmetric, it has \(m\) distinct vertex-rootings. Therefore the resulting family \(\mathcal P_N\) satisfies
\[
|\mathcal P_N|=m|\mathcal H_m|
\sim (N-8)U_{N-8}.
\]
Using (7),
\[
\boxed{|\mathcal P_N|
\sim \frac{256}{81}\frac{U_N}{N^3}.}
\tag{22}
\]
Every graph in this family is 3-edge-connected and non-Hamiltonian, proving (2).

The uniqueness argument is important: without it, counting rooted cores would not justify counting distinct output graphs.

### Labelled version

Each output has exactly two automorphisms: contraction forces every automorphism to fix the asymmetric core, leaving precisely the order-two kernel acting inside \(F\). Consequently,
\[
\boxed{\frac{|\mathcal P_N^{\mathrm{lab}}|}{L_N}
\sim \frac{128}{81N^3}.}
\tag{23}
\]

The two conventions therefore give:

| Counting convention | Bridge density | Explicit bridgeless non-Hamiltonian family |
|---|---:|---:|
| Unlabelled | \(\displaystyle \frac{32}{9N^2}\) | \(\displaystyle \frac{256}{81N^3}\) |
| Labelled | \(\displaystyle \frac{8}{9N^2}\) | \(\displaystyle \frac{128}{81N^3}\) |

---

# 5. What this establishes—and the remaining gap

For unlabelled counts, (1) and (2) imply
\[
\frac{R_N}{B_N}
\ge \left(\frac89+o(1)\right)\frac1N.
\]
Hence
\[
\frac{B_N}{B_N+R_N}
\le 1-\frac{8}{9N}+o(N^{-1}),
\]
which becomes (4) after substituting \(N=2n\).

The conjecture itself requires an **upper** bound:
\[
R_N=o(U_N/N^2).
\]
No such bound follows from the arguments above. The bare assertion that almost all cubic graphs are Hamiltonian gives only \(R_N=o(U_N)\), which is insufficient at this scale.

In particular, I have not shown that almost every bridgeless non-Hamiltonian graph contains a Petersen fragment. Global obstructions, and other local obstructions, remain uncontrolled. Nor does the argument establish the proposed strict monotonicity.

---

# 6. If disconnected graphs are included, the limit is not one

Suppose \(NH(n)\) literally includes disconnected cubic graphs, while “1-connected” has its usual meaning of connected but not 2-connected.

For \(N>8\), every graph
\[
K_4\;\dot\cup\;H,
\]
where \(H\) is a connected cubic graph on \(N-4\) vertices, is non-Hamiltonian and is not 1-connected. These give exactly \(U_{N-4}\) distinct isomorphism classes.

Thus
\[
NH(n)\ge B_N+U_{N-4}.
\]
By (7),
\[
U_{N-4}\sim \frac{16}{9}\frac{U_N}{N^2},
\]
whereas (1) gives the constant \(32/9\) for \(B_N\). Therefore
\[
\boxed{\limsup_{n\to\infty}\frac{NHB(n)}{NH(n)}
\le \frac{32/9}{32/9+16/9}=\frac23.}
\]

For labelled counts, the analogous bound is \(12/13\).

So the disconnected interpretation is false. For the intended connected version, the substantive outcome here is the sharp numerator asymptotic, its dominant structural description, and the explicit \(N^{-3}\)-scale bridgeless obstruction family—not a proof of the conjecture.