```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every connected graph with m=n+1 satisfies the stronger bound s^+(G) >= n+5-2sqrt(5) > n, but the general conjecture remains unresolved here.",
  "would_publish": false,
  "caveats": "The proof covers all bicyclic graphs, including arbitrary pendant trees; novelty of this special case has not been independently checked."
}
```

# A proof for all connected bicyclic graphs

The general conjecture is not resolved below. The result is a complete proof of its boundary case \(m=n+1\), using a determinant argument rather than the moment bounds in the previous attempt.

## 1. Result

Write
\[
\delta(G)=s^+(G)-m.
\]

### Theorem
Every connected bicyclic graph \(G\), meaning \(m=n+1\), satisfies
\[
\boxed{\delta(G)\ge -2(\sqrt5-2).}
\]
Consequently,
\[
\boxed{s^+(G)\ge n+5-2\sqrt5>n.}
\]

The proof permits arbitrary subdivisions and arbitrary pendant trees. In particular, it is not restricted to claw-free graphs or graphs of diameter two.

We will also establish the auxiliary sharp bound
\[
s^+(H)\ge e(H)-(\sqrt5-2)
\tag{1}
\]
for graphs with at most one cycle.

---

## 2. An argument-integral formula

For a graph \(H\), define, for \(t>0\),
\[
D_H(t)=\det(tI+iA(H)),
\qquad
\Theta_H(t)=\sum_{\lambda\in\operatorname{Spec}(H)}
                 \arctan\frac{\lambda}{t}.
\]
Thus \(\Theta_H\) is a continuous argument of \(D_H(t)\), normalized by
\(\Theta_H(t)\to0\) as \(t\to\infty\). It need not always be the principal argument.

### Lemma 1
For every graph \(H\),
\[
\boxed{
\delta(H)=-\frac2\pi\int_0^\infty t\,\Theta_H(t)\,dt.
}
\tag{2}
\]

### Proof
Since \(\sum_\lambda\lambda=0\),
\[
t^2\Theta_H'(t)
=-\sum_\lambda\frac{\lambda t^2}{t^2+\lambda^2}
=\sum_\lambda\frac{\lambda^3}{t^2+\lambda^2}.
\]
Therefore
\[
\frac1\pi\int_0^\infty t^2\Theta_H'(t)\,dt
=\frac12\sum_\lambda\lambda|\lambda|
=s^+(H)-e(H).
\]
Here zero eigenvalues contribute zero.

As \(t\to0\), \(\Theta_H(t)\) is bounded. As \(t\to\infty\), the trace-zero identity gives
\(\Theta_H(t)=O(t^{-3})\). Integration by parts proves (2). ∎

Our task is therefore to bound \(\Theta_G(t)\) from above.

---

## 3. Matching polynomials and cycle contributions

Use the positive matching generating polynomial
\[
Z_H(t)=\sum_{M\text{ a matching of }H}t^{|V(H)|-2|M|}.
\]
For a forest,
\[
D_H(t)=Z_H(t)>0.
\tag{3}
\]

Let
\[
F_j(t)=Z_{P_j}(t),\qquad F_0=1,\quad F_1=t.
\]
The usual deletion recurrence is
\[
F_j=tF_{j-1}+F_{j-2}.
\tag{4}
\]
In particular,
\[
F_{j+2}\ge F_j,\qquad F_{2j}\ge1
\tag{5}
\]
for \(t>0\).

For a cycle of length \(\ell\), put
\[
g_\ell(t)=Z_{C_\ell}(t)=F_\ell(t)+F_{\ell-2}(t).
\tag{6}
\]
It follows that \(g_{\ell+2}\ge g_\ell\).

In the determinant expansion of \(D_H\), an edge used as a transposition has weight \(+1\). The two orientations of a cycle of length \(\ell\) together have weight
\[
c_\ell=-2(-i)^\ell
=
\begin{cases}
-2(-1)^{\ell/2},&\ell\text{ even},\\[2mm]
2i(-1)^{(\ell-1)/2},&\ell\text{ odd}.
\end{cases}
\tag{7}
\]
Consequently, if \(H\) has no two vertex-disjoint cycles, then
\[
D_H(t)
=Z_H(t)+\sum_{C\text{ a cycle of }H}c_{|C|}Z_{H-V(C)}(t).
\tag{8}
\]
This follows directly by grouping determinant permutations according to their cycles of length at least three.

Call an odd cycle **adverse** if its length is \(1\pmod4\). These are precisely the cycles whose contribution in (7) has positive imaginary part.

For odd \(\ell\), define
\[
\phi_\ell(t)=\arctan\frac{2}{g_\ell(t)}.
\]
Every adverse cycle has length at least five, and hence
\[
\phi_\ell(t)\le\phi_5(t)
\qquad(\ell\equiv1\pmod4).
\tag{9}
\]
Here
\[
g_5(t)=t^5+5t^3+5t.
\]

The determinant of \(C_5\) is \(g_5(t)+2i\), so
\(\Theta_{C_5}(t)=\phi_5(t)\). Its spectrum is
\[
2,\quad \frac{\sqrt5-1}{2},\quad \frac{\sqrt5-1}{2},
\quad-\frac{\sqrt5+1}{2},\quad-\frac{\sqrt5+1}{2}.
\]
Thus \(s^+(C_5)=7-\sqrt5\), and Lemma 1 gives the useful normalization
\[
\boxed{
\frac2\pi\int_0^\infty t\,\phi_5(t)\,dt=\sqrt5-2.
}
\tag{10}
\]

---

## 4. Graphs with at most one cycle

### Lemma 2
If \(H\) has at most one cycle, then, for all \(t>0\),
\[
\operatorname{Re}D_H(t)>0,
\qquad
\Theta_H(t)\le\phi_5(t).
\tag{11}
\]

### Proof
If \(H\) has no odd cycle, it is bipartite. Its nonzero eigenvalues occur in opposite pairs, so \(D_H(t)>0\) and \(\Theta_H(t)=0\).

Otherwise let \(C\) be its unique cycle, of odd length \(\ell\). Formula (8) gives
\[
D_H=Z_H+2i\varepsilon Z_{H-V(C)},
\qquad
\varepsilon=(-1)^{(\ell-1)/2}.
\]
The real part is positive.

Matchings of the vertex-disjoint union \(C\dot\cup(H-V(C))\) are matchings of \(H\), so
\[
Z_H\ge g_\ell Z_{H-V(C)}.
\tag{12}
\]
If \(\varepsilon=-1\), the argument is negative. If \(\varepsilon=1\), then
\[
\Theta_H
=\arctan\frac{2Z_{H-V(C)}}{Z_H}
\le\phi_\ell\le\phi_5.
\]
Because \(D_H\) stays in the open right half-plane, its principal argument is its normalized continuous argument. ∎

Combining this lemma with (2) and (10) proves (1), with equality for \(C_5\).

---

## 5. Bicyclic cores with intersecting cycles

The 2-core \(B\) of a connected bicyclic graph is connected and satisfies
\[
\sum_{v\in V(B)}(d_B(v)-2)=2.
\]
Suppressing vertices of degree two shows that it has one of three forms:

1. two cycles sharing exactly one vertex—a figure-eight;
2. three internally vertex-disjoint paths with the same endpoints—a theta graph;
3. two vertex-disjoint cycles joined by a path—a dumbbell.

We first treat the first two forms.

### Lemma 3
If \(B\) is a figure-eight or a theta graph, then, for all \(t>0\),
\[
\operatorname{Re}D_B(t)>0,
\qquad
\Theta_B(t)\le2\phi_5(t).
\tag{13}
\]

We use the elementary inequalities
\[
\arctan(x+y)\le\arctan x+\arctan y,
\qquad
\arctan(2x)\le2\arctan x
\quad(x,y\ge0).
\tag{14}
\]

### 5.1. Figure-eight cores

If both cycles are even, \(B\) is bipartite, so the conclusion is immediate.

Suppose first that both cycles are odd. Write
\[
D_B=R+iI.
\]
There is no even-cycle term in (8), so \(R=Z_B>0\). For either cycle \(C\),
\[
R\ge g_{|C|}Z_{B-V(C)}.
\]
Discarding all negative contributions to \(I\), we obtain
\[
\frac IR\le
\sum_{\substack{C\text{ adverse}\\\text{cycle of }B}}
\frac2{g_{|C|}}.
\]
Equations (9) and (14) yield
\[
\Theta_B\le
\sum_{C\text{ adverse}}\phi_{|C|}
\le2\phi_5.
\tag{15}
\]

Now suppose the cycles are an odd cycle \(C\) and an even cycle \(E\). If
\(|E|\equiv2\pmod4\), its real contribution in (8) is positive, and
\[
R\ge Z_B\ge g_{|C|}Z_{B-V(C)}.
\tag{16}
\]

If \(|E|\equiv0\pmod4\), then
\[
R=Z_B-2Z_{B-V(E)}.
\]
The following matching inequality compensates for this subtraction:
\[
Z_B\ge
g_{|C|}Z_{B-V(C)}+2Z_{B-V(E)}.
\tag{17}
\]
Indeed, the first term counts matchings using only edges of
\(C\dot\cup(B-V(C))\). Each of the two perfect matchings of \(E\), together with any matching of \(B-V(E)\), uses an edge of \(E\) incident with the shared vertex. These are two disjoint families, neither counted by the first term. Their respective generating polynomials are \(Z_{B-V(E)}\).

Thus (16) holds also in this case. There is only one odd-cycle contribution, so the argument is at most \(\phi_5\). This proves the lemma for figure-eights.

### 5.2. Theta cores

Let the three paths have lengths \(a,b,c\). If their parities are all the same, every cycle is even and \(B\) is bipartite.

Otherwise label the paths so that \(a\) has the parity opposite to \(b,c\). The odd cycles have lengths
\[
a+b,\qquad a+c,
\]
and the even cycle \(E\) has length \(b+c\).

Put
\[
W_b=g_{a+b}F_{c-1},
\qquad
W_c=g_{a+c}F_{b-1}.
\tag{18}
\]
These count matchings of an odd cycle together with its vertex-complement. In particular,
\[
Z_B\ge W_b,\qquad Z_B\ge W_c.
\tag{19}
\]

Formula (8) gives
\[
D_B=R+iI,
\]
where
\[
R=Z_B-2(-1)^{(b+c)/2}F_{a-1},
\tag{20}
\]
and
\[
I=2\varepsilon_bF_{c-1}+2\varepsilon_cF_{b-1},
\quad
\varepsilon_b=(-1)^{(a+b-1)/2},
\quad
\varepsilon_c=(-1)^{(a+c-1)/2}.
\tag{21}
\]

#### Case A: \(b+c\equiv2\pmod4\)

The extra term in (20) is positive. Thus \(R\ge W_b,W_c\), and the same estimate as (15) gives
\[
\Theta_B\le2\phi_5.
\tag{22}
\]

#### Case B: \(b+c\equiv0\pmod4\), with \(a\) odd and \(b,c\) even

Consider the matchings counted by \(W_b\). They use no edge of the \(c\)-path incident with either common endpoint.

Each perfect matching of \(E\) must use such an edge: otherwise the \(c-1\) internal vertices of that path, an odd number, would have to be perfectly matched among themselves. Hence both perfect matchings of \(E\), combined with arbitrary matchings of the internal \(a\)-path, give families excluded from \(W_b\). Therefore
\[
Z_B\ge W_b+2F_{a-1}.
\]
By symmetry,
\[
Z_B\ge W_c+2F_{a-1}.
\]
After the subtraction in (20), this gives
\[
R\ge W_b,W_c>0.
\]
Again (22) follows.

#### Case C: \(b+c\equiv0\pmod4\), with \(a\) even and \(b,c\) odd

At least one perfect matching of \(E\) covers both common endpoints using the \(c\)-path. It is excluded from the matchings counted by \(W_b\). Consequently,
\[
Z_B\ge W_b+F_{a-1},
\qquad
R\ge W_b-F_{a-1}.
\tag{23}
\]
Since \(b,c\) are odd,
\[
F_{c-1}\ge1,
\]
and
\[
g_{a+b}\ge g_{a+1}
=F_{a+1}+F_{a-1}
=tF_a+2F_{a-1}
\ge2F_{a-1}.
\]
Thus \(W_b\ge2F_{a-1}\), and (23) gives
\[
R\ge\frac12W_b>0.
\]
Symmetrically,
\[
R\ge\frac12W_c.
\tag{24}
\]

Moreover, \(b+c\equiv0\pmod4\) with \(b,c\) odd means that their residues modulo four are opposite. Hence the two odd cycles have opposite residues modulo four: **exactly one is adverse**.

Let its length be \(\ell\), and let \(F\) denote the matching polynomial of its vertex-complement. Discarding the negative term in (21) and using (24),
\[
\frac IR\le\frac{2F}{\frac12g_\ell F}
=\frac4{g_\ell}.
\]
Therefore
\[
\Theta_B
\le\arctan\frac4{g_\ell}
\le2\arctan\frac2{g_\ell}
\le2\phi_5.
\]
All theta cases are covered, completing Lemma 3. ∎

---

## 6. Adding arbitrary pendant trees

### Lemma 4
If a connected bicyclic graph \(G\) has a figure-eight or theta 2-core, then
\[
\Theta_G(t)\le2\phi_5(t)
\qquad(t>0).
\tag{25}
\]

### Proof
Let \(B\) be the 2-core and let \(U=V(G)\setminus V(B)\). Every cycle of \(G\) is contained in \(B\).

Group determinant permutations according to the matching \(M\) formed by their transpositions using edges outside \(B\). Put
\[
S_M=V(M)\cap V(B),
\qquad
u_M=|U\setminus V(M)|.
\]
The determinant expansion gives the exact identity
\[
D_G(t)=\sum_M t^{u_M}D_{B-S_M}(t),
\tag{26}
\]
where the sum is over matchings consisting of edges outside \(B\).

If \(S_M=\varnothing\), Lemma 3 applies. If \(S_M\ne\varnothing\), the path descriptions of a figure-eight and a theta graph show that \(B-S_M\) has at most one cycle. Lemma 2 therefore applies.

Every summand in (26) has positive real part and argument at most \(2\phi_5(t)\). A positive linear combination of complex numbers in the open right half-plane has argument between their smallest and largest arguments. Hence \(D_G\) has positive real part and principal argument at most \(2\phi_5(t)\).

Its principal argument is continuous and tends to zero at infinity, so it equals \(\Theta_G(t)\). ∎

This step covers all pendant trees, without imposing restrictions on their size or shape.

---

## 7. Two vertex-disjoint cycles

It remains to handle dumbbell cores, again allowing arbitrary pendant trees.

### Lemma 5
If a connected bicyclic graph \(G\) has two vertex-disjoint cycles, then
\[
\Theta_G(t)\le2\phi_5(t)
\qquad(t>0).
\tag{27}
\]

### Proof
Let its cycles be \(C_1,C_2\). Every edge outside these cycles is a bridge.

For a matching \(M\) consisting of noncycle edges, put
\[
S_i=V(M)\cap V(C_i),
\]
and let \(u_M\) be the number of vertices outside the two cycles not covered by \(M\). The same determinant grouping as before gives
\[
D_G(t)=
\sum_M t^{u_M}
D_{C_1-S_1}(t)D_{C_2-S_2}(t).
\tag{28}
\]
Whenever \(S_i\ne\varnothing\), \(C_i-S_i\) is a forest, so its determinant is positive real.

Let \(\alpha_i(t)\) be the principal argument of \(D_{C_i}(t)\). From (7),
\[
\alpha_i=
\begin{cases}
0,&|C_i|\text{ even},\\
\phi_{|C_i|},&|C_i|\equiv1\pmod4,\\
-\phi_{|C_i|},&|C_i|\equiv3\pmod4.
\end{cases}
\tag{29}
\]
Every summand in (28) has argument in
\[
[L,U],
\]
where
\[
L=\min(0,\alpha_1)+\min(0,\alpha_2),
\qquad
U=\max(0,\alpha_1)+\max(0,\alpha_2).
\]
The width of this interval is
\[
U-L=|\alpha_1|+|\alpha_2|<\pi.
\]
Thus it defines a convex angular sector, and the sum in (28) also lies in that sector.

Furthermore,
\[
-\pi<L\le0\le U<\pi.
\]
The resulting principal argument is continuous and tends to zero at infinity, so it is \(\Theta_G\). Finally, only adverse cycles contribute to \(U\), and (9) gives
\[
\Theta_G\le U\le2\phi_5.
\]
∎

---

## 8. Conclusion

Every connected bicyclic graph has one of the three 2-core forms considered above. Lemmas 4 and 5 therefore establish, uniformly,
\[
\Theta_G(t)\le2\phi_5(t)
\qquad(t>0).
\]
Using (2) and (10),
\[
\begin{aligned}
s^+(G)-m
&=-\frac2\pi\int_0^\infty t\,\Theta_G(t)\,dt\\
&\ge-\frac4\pi\int_0^\infty t\,\phi_5(t)\,dt\\
&=-2(\sqrt5-2).
\end{aligned}
\]
Since \(m=n+1\),
\[
s^+(G)\ge n+5-2\sqrt5
=n+0.527864\ldots>n.
\]
This proves the stated special-case theorem.

For example, two 5-cycles joined by a path have induced claws and diameter greater than two. The theorem covers this entire family, together with arbitrary pendant trees, so it goes beyond the two classes specifically listed in the prompt.

## 9. What remains unresolved

The argument does **not** prove the conjecture for general graphs with \(m\ge n+2\).

The cycle-rank-two restriction is used essentially:

- an intersecting-cycle core is only a figure-eight or theta graph;
- its determinant has no products of vertex-disjoint cycle contributions;
- in the disjoint-cycle case, there are only two cycle phases, whose total angular range is strictly less than \(\pi\).

No corresponding phase bound for arbitrary higher-cycle-rank cores is established here. Nor does choosing a spanning bicyclic subgraph extend the result: the proof supplies no monotonicity inequality for positive square energy under edge addition.

Thus the precise partial conclusion is a complete resolution of the boundary case \(m=n+1\), not a resolution of the full conjecture.