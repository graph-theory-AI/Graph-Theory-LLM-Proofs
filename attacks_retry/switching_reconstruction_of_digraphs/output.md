```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I construct a twelve-vertex counterexample with antiparallel pairs and prove a rigid equality-case theorem for the oriented-graph problem.",
  "would_publish": false,
  "caveats": "The explicit example is not oriented; the no-digon problem remains unresolved here, and novelty of the structural theorem is unchecked."
}
```

# 1. Scope and results

The switching deck is a **multiset**, with one card for each vertex.

There is a consequential convention issue. If “digraph” permits antiparallel pairs of arcs, then the question as written has an explicit affirmative answer: Section 2 constructs two nonisomorphic, strongly connected digraphs on twelve vertices with identical switching decks.

That construction is **not an oriented graph**. Consequently, it must not be presented as resolving the no-digon problem discussed in the catalog’s literature summary. For that formulation, I obtain the following partial result.

> **Extremal-orbit theorem.** Let \(D\) be an oriented graph with connected underlying graph, of order
> \[
> n\equiv4\pmod8,\qquad n\ge12.
> \]
> Let \(r(D)\) be the number of distinct labelled digraphs in its switching class that are isomorphic to \(D\).
>
> If \(D\) is switching-nonreconstructible and
> \[
> r(D)=2^{n/2-2},
> \]
> then there is a unique pairing of its vertices such that the switches producing copies of \(D\) are exactly the unions of an even number of pairs. Its nonisomorphic mate is unique, has the same orbit size, and is obtained by switching unions of an odd number of pairs.
>
> Moreover, every permutation preserving the switching class preserves this pairing.

Here a “pairing” means a partition into two-element sets; the pairs need not be edges.

This strengthens the previous attempt at the boundary of its orbit-size obstruction. I rederive the cube reduction rather than assuming that attempt is correct.

---

# 2. A twelve-vertex example when antiparallel pairs are allowed

## 2.1 Construction

Take six vertices
\[
a_i^0,a_i^1\qquad (i=1,2,3),
\]
four vertices
\[
c_s\qquad
\left(s\in\mathcal E:=\{000,011,101,110\}\right),
\]
and two further vertices \(z_1,z_2\).

For \(t=(t_1,t_2,t_3)\in\{0,1\}^3\), define \(D_t\) as follows.

1. On each pair \(\{a_i^0,a_i^1\}\), put the single arc
   \[
   a_i^{t_i}\longrightarrow a_i^{1-t_i}.
   \]

2. For every \(s\in\mathcal E\) and \(i\in\{1,2,3\}\), put **both** arcs between
   \[
   c_s\quad\text{and}\quad a_i^{s_i}.
   \]

3. Put both arcs between every \(z_j\) and every \(c_s\).

There are no other arcs. In particular, this specifies a loopless simple digraph, but not an oriented graph.

Set
\[
D=D_{000},\qquad E=D_{100}.
\]

## 2.2 Isomorphism types are distinguished by parity

I claim that
\[
D_t\cong D_u
\quad\Longleftrightarrow\quad
t_1+t_2+t_3\equiv u_1+u_2+u_3\pmod2. \tag{1}
\]

First consider an isomorphism between two members of this family.

The six \(a\)-vertices are intrinsically identifiable: they are precisely the vertices incident with an asymmetric arc. Those asymmetric arcs identify the three unordered pairs
\[
\{a_i^0,a_i^1\}.
\]
Thus an isomorphism induces a permutation \(\rho\) of these three pairs, together with endpoint flips \(f_i\in\{0,1\}\):
\[
a_i^b\longmapsto a_{\rho(i)}^{\,b+f_i}.
\]

The four \(c\)-vertices are also intrinsically identifiable: among the other six vertices, they have neighbors among the \(a\)-vertices, whereas the \(z\)-vertices do not.

The neighborhoods of the \(c\)-vertices among the \(a\)-vertices encode exactly the even-parity binary triples. Coordinate permutations preserve parity, while endpoint flips change it by
\[
f_1+f_2+f_3.
\]
Preserving this family of neighborhoods therefore requires
\[
f_1+f_2+f_3=0.
\]
The orientation vector transforms by the same endpoint flips and coordinate permutation, so its parity is preserved.

Conversely, if \(t\) and \(u\) have the same parity, let \(f=t+u\). The map
\[
a_i^b\mapsto a_i^{b+f_i},\qquad
c_s\mapsto c_{s+f},\qquad
z_j\mapsto z_j
\]
is an isomorphism \(D_t\to D_u\). This proves (1), and in particular
\[
D\not\cong E.
\]

## 2.3 Their decks agree

Switching an \(a\)-vertex reverses exactly one asymmetric arc. All its antiparallel pairs remain unchanged. Hence it toggles one coordinate of \(t\), changing parity.

Switching any \(c\)-vertex or \(z\)-vertex changes nothing, since every incident adjacency is antiparallel.

There are six vertices of each kind. Consequently,
\[
\operatorname{Deck}(D)
=
6[D]+6[E]
=
\operatorname{Deck}(E). \tag{2}
\]

The antiparallel subdigraph is connected: distinct even triples in \(\mathcal E\) agree in one coordinate, and hence their \(c\)-vertices have a common \(a\)-neighbor; the \(z\)-vertices join all four \(c\)-vertices. Thus \(D\) and \(E\) are even **strongly connected**.

This is a complete twelve-vertex counterexample under the convention allowing digons. Its reliance on digons is essential to the argument: they supply structural information without responding to switching.

---

# 3. The oriented case: definitions and theorem

For the remainder, let \(D\) be an oriented graph with connected underlying graph, on a fixed vertex set \(V\), \(|V|=n\).

For \(S\subseteq V\), let \(D^S\) denote switching every vertex of \(S\), and write
\[
\mathcal C(D)=\{D^S:S\subseteq V\}.
\]
This is the full labelled switching class, not the switching deck.

Connectedness gives
\[
D^S=D^T
\quad\Longleftrightarrow\quad
T=S\ \text{or}\ T=V\setminus S. \tag{3}
\]
Define
\[
r(D)=\bigl|\{F\in\mathcal C(D):F\cong D\}\bigr|.
\]

Also define the switching-class symmetry group
\[
\Gamma(D)=
\{\pi\in\operatorname{Sym}(V):\pi\mathcal C(D)=\mathcal C(D)\}.
\]
Its orbit on \(D\) consists exactly of the labelled members of \(\mathcal C(D)\) isomorphic to \(D\). Thus
\[
r(D)=\frac{|\Gamma(D)|}{|\operatorname{Aut}(D)|}. \tag{4}
\]

Here is the precise structural result.

### Theorem

Suppose
\[
n\equiv4\pmod8,\qquad n\ge12,
\]
and \(D,E\) are nonisomorphic with the same switching deck. If
\[
r(D)=2^{n/2-2},
\]
then, after putting \(E\) in the labelled switching class of \(D\), there is a unique pairing
\[
\mathcal M=\{P_1,\ldots,P_d\},\qquad d=n/2,
\]
such that
\[
D^S\cong D
\quad\Longleftrightarrow\quad
S\text{ is a union of an even number of pairs of }\mathcal M, \tag{5}
\]
and
\[
D^S\cong E
\quad\Longleftrightarrow\quad
S\text{ is a union of an odd number of pairs of }\mathcal M. \tag{6}
\]

In particular:

* \(r(E)=2^{n/2-2}\);
* every element of \(\Gamma(D)\) preserves \(\mathcal M\);
* \(E\) is the unique nonisomorphic mate of \(D\).

I prove this next.

---

# 4. Equal decks and distance distributions in the cube

## 4.1 Placing mates in one switching class

An isomorphism between one card of \(D\) and one card of \(E\) lets us relabel \(E\) so that
\[
E=D^{\{u,v\}}
\]
for suitable vertices \(u,v\). Thus equal-deck mates can always be placed in one switching class.

Identify subsets of \(V\) with vectors in \(\mathbb F_2^n\). Partition this cube into parts \(U_i\), according to the isomorphism type of \(D^S\).

Let \(q_{ij}\) be the number of one-coordinate flips from a point of \(U_i\) into \(U_j\). This is well-defined because isomorphic digraphs have identical switching decks. Counting cube edges between parts yields
\[
|U_i|q_{ij}=|U_j|q_{ji}. \tag{7}
\]

Let
\[
A=\{S:D^S\cong D\},\qquad
B=\{S:D^S\cong E\}.
\]
By (3),
\[
|A|=2r(D),\qquad |B|=2r(E). \tag{8}
\]

Define
\[
f=\frac{\mathbf1_A}{|A|}-\frac{\mathbf1_B}{|B|}.
\]
For the cube adjacency operator
\[
(Tf)(x)=\sum_{i=1}^n f(x+e_i),
\]
equation (7) gives, for \(x\in U_j\),
\[
(Tf)(x)
=
\frac{q_{jA}}{|A|}-\frac{q_{jB}}{|B|}
=
\frac{q_{Aj}-q_{Bj}}{|U_j|}.
\]
The equal-deck hypothesis therefore says precisely that
\[
Tf=0. \tag{9}
\]

This verifies the normalized cube reduction from the previous attempt.

## 4.2 All distance distributions satisfy an exact identity

The characters
\[
\chi_R(x)=(-1)^{\sum_{i\in R}x_i}
\]
are eigenfunctions of \(T\), with eigenvalue \(n-2|R|\). Hence \(f\) is supported on Fourier level
\[
d=n/2.
\]

Furthermore, \(f(x+\mathbf1)=f(x)\), since switching every vertex changes nothing. Thus \(d\) must be even, recovering the obstruction \(4\mid n\).

Let \(T_j\) be the distance-\(j\) operator on the cube:
\[
(T_jf)(x)=\sum_{\operatorname{wt}(y)=j}f(x+y).
\]
On Fourier level \(d=n/2\), its eigenvalues \(c_j\) satisfy
\[
\sum_{j=0}^n c_jz^j
=(1-z)^d(1+z)^d
=(1-z^2)^d. \tag{10}
\]
Consequently,
\[
c_{2\ell}=(-1)^\ell\binom d\ell,\qquad c_{2\ell+1}=0.
\]

For \(x\in A\), put
\[
a_j(x)=|\{a\in A:\operatorname{dist}(x,a)=j\}|,
\qquad
b_j(x)=|\{b\in B:\operatorname{dist}(x,b)=j\}|.
\]
The equation \(T_jf=c_jf\) becomes
\[
a_j(x)-\frac{|A|}{|B|}b_j(x)=c_j. \tag{11}
\]

Summing the positive coefficients in (10) gives
\[
\sum_{c_j>0}c_j
=\sum_{\ell\text{ even}}\binom d\ell
=2^{d-1}.
\]
Since \(a_j(x)\ge c_j\) whenever \(c_j>0\),
\[
|A|\ge2^{d-1}.
\]
Applying the same argument to \(-f\) gives the corresponding bound for \(B\). Therefore
\[
r(D),r(E)\ge2^{d-2}. \tag{12}
\]

Unlike a support-size bound alone, (11) also describes what equality forces.

---

# 5. Proof of the extremal-orbit theorem

Assume now that
\[
|A|=2^{d-1}.
\]

## 5.1 Equality forces a doubly-even linear code

Equality in the preceding sum leaves no room for additional positive-support points. For every \(x\in A\),

* points of \(A\) occur only at distances divisible by four;
* points of \(B\) occur only at distances congruent to two modulo four.

In particular,
\[
\operatorname{wt}(a+a')\equiv0\pmod4
\qquad(a,a'\in A). \tag{13}
\]
We have \(0\in A\). Let \(L\) be the binary linear span of \(A\).

Equation (13) implies that the vectors in \(A\) are pairwise orthogonal over \(\mathbb F_2\). Indeed,
\[
2|\operatorname{supp}(a)\cap\operatorname{supp}(a')|
=
\operatorname{wt}(a)+\operatorname{wt}(a')
-\operatorname{wt}(a+a')
\]
is divisible by four. It follows that \(L\) is self-orthogonal and every word of \(L\) has weight divisible by four. Thus
\[
d-1\le\dim L\le d. \tag{14}
\]

The upper possibility cannot occur when \(n\equiv4\pmod8\). For completeness, here is a short proof of the needed coding fact.

If \(L=L^\perp\) is a doubly-even binary code of length \(n=2d\), character orthogonality gives
\[
\begin{aligned}
2^d
&=\sum_{x\in L}\mathrm i^{\operatorname{wt}(x)}\\
&=2^{-d}\sum_{y\in L}
(1+\mathrm i)^{n-\operatorname{wt}(y)}
(1-\mathrm i)^{\operatorname{wt}(y)}\\
&=(1+\mathrm i)^n.
\end{aligned}
\]
The last equality uses \(4\mid\operatorname{wt}(y)\). Hence
\[
e^{\mathrm i\pi n/4}=1,
\]
so \(8\mid n\), a contradiction.

Therefore \(\dim L=d-1\). Since \(A\subseteq L\) and both have \(2^{d-1}\) elements,
\[
A=L. \tag{15}
\]
In particular, distinct words of \(A\) have distance at least four.

## 5.2 A negative-support point produces a pairing

Choose \(b\in B\).

Every neighbor \(z\) of \(b\) has at least one neighbor in \(B\). Equation \(Tf(z)=0\) then implies that \(z\) has a neighbor in \(A\).

It has **at most one** neighbor in \(A\), since two such neighbors would be distinct words of \(A\) at distance two. Thus every one of the \(n\) neighbors of \(b\) is adjacent to exactly one word of \(A\).

A word of \(A\) at distance two from \(b\) accounts for exactly two such neighbors. Hence there are exactly
\[
d=n/2
\]
words \(a_1,\ldots,a_d\in A\) at distance two from \(b\).

Put
\[
p_i=b+a_i.
\]
Each \(p_i\) has weight two. Their supports are pairwise disjoint: otherwise \(p_i+p_j=a_i+a_j\) would have weight two, contradicting the minimum distance of \(A\).

Thus their supports form a pairing
\[
\mathcal M=\{P_1,\ldots,P_d\}
\]
of all \(n\) vertices.

Moreover,
\[
p_i+p_j\in A.
\]
These vectors generate the \((d-1)\)-dimensional code consisting of unions of an even number of pairs. Comparing dimensions with (15) proves (5).

Also \(b+p_i=a_i\in A\), so \(b\) belongs to the coset consisting of odd unions of pairs.

## 5.3 The pairing and the negative support are unique

The code of even unions of \(d\) pairs determines its pairing when \(d\ge3\).

To see this, fix a vertex \(u\). Among weight-four codewords:

* its mate occurs together with \(u\) in \(d-1\) words;
* every other vertex occurs together with \(u\) in exactly one word.

Here \(d\ge6\), so these are distinguishable.

Repeating the preceding construction for any \(b'\in B\) must therefore produce the same pairing. Consequently, all of \(B\) lies in its odd-union coset, which has \(2^{d-1}\) elements.

But (12) already gives \(|B|\ge2^{d-1}\). Therefore \(B\) is exactly that coset, proving (6) and
\[
r(E)=r(D).
\]

## 5.4 The entire switching-class symmetry group preserves the pairing

Let \(\pi\in\Gamma(D)\), and choose \(c\) with
\[
\pi D=D^c.
\]
Because \(\pi D\cong D\), we have \(c\in A\).

The induced action on switching vectors is
\[
S\longmapsto c+\pi S.
\]
It preserves the isomorphism-type part \(A\). Since \(A\) is linear and \(c\in A\),
\[
\pi A=A.
\]
The pairing is determined by this code, so \(\pi\) preserves the pairing.

Finally, \(A\) depends only on \(D\), and determines both the pairing and its odd-union coset. Thus every nonisomorphic equal-deck mate of \(D\) belongs to the same part \(B\). The mate is unique. This completes the proof. \(\square\)

---

# 6. What the theorem says specifically at twelve vertices

For a connected twelve-vertex oriented graph, a counterexample must have \(r(D)\ge16\). The theorem completely describes the boundary case \(r(D)=16\).

There must be six uniquely determined pairs, and the switching-set weight enumerators must be
\[
\sum_{D^S\cong D}z^{|S|}
=
1+15z^4+15z^8+z^{12}, \tag{16}
\]
and
\[
\sum_{D^S\cong E}z^{|S|}
=
6z^2+20z^6+6z^{10}. \tag{17}
\]

More importantly, these sets cannot merely have the displayed weight distributions: they must be exactly the even and odd unions of the six pairs.

This gives an additional exclusion criterion:

> If a connected twelve-vertex switching class has no invariant pairing under \(\Gamma(D)\), then none of its size-sixteen isomorphism orbits can be switching-nonreconstructible.

The pairing configuration is also sufficient when it occurs as two complete isomorphism-type parts. Indeed, in sign coordinates its indicator difference is
\[
\prod_{\{u,v\}\in\mathcal M}
\frac{x_u+x_v}{2},
\]
a homogeneous Fourier polynomial of degree \(n/2\). It is annihilated by cube adjacency, so the reversible calculation in Section 4 gives equal decks.

Thus the theorem identifies an exact, highly constrained obstruction at the minimum possible orbit size; it does not merely supply another numerical necessary condition.

# 7. Remaining gap

For the intended **oriented-graph** problem, this does not decide whether counterexamples on twelve or more vertices exist. In particular:

* I have not ruled out realization of the pairing configuration by an oriented graph.
* Larger isomorphism orbits remain uncontrolled by the equality argument.
* The structural theorem concerns connected underlying graphs and does not classify disconnected oriented counterexamples.
* No exhaustive computation or novelty claim is made.

For digraphs **with antiparallel pairs**, however, Section 2 is a fully specified twelve-vertex counterexample. The distinction between these two conventions cannot safely be suppressed.