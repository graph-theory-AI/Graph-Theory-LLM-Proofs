```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For a fixed three-colour palette, I prove a polynomial two-colour-set bound for every forbidden pattern built from coloured edges and triangles by vertex substitution.",
  "would_publish": false,
  "caveats": "The full conjecture is not settled; the host palette is fixed, and no novelty is claimed."
}
```

## 1. Scope and statement of the partial result

I use the standard fixed-palette interpretation: the forbidden pattern and the host have edge colours in the same fixed palette, and copies preserve colour labels.

This qualification matters. If the host may use an unbounded number of colours, the literal displayed statement is false: take a two-coloured triangle having a repeated colour, and give every host edge a distinct colour. The host avoids the pattern, while every monochromatic vertex set has size at most two. This is not a counterexample to the intended fixed-palette conjecture.

The partial result below treats a substitution-closed family of forbidden patterns. Importantly, it does **not** assume that the host avoids rainbow triangles, except in one base case.

For a complete graph \(G\) coloured from \([3]=\{1,2,3\}\), put
\[
A(G)=\max\{|S|:G[S]\text{ uses at most two colours}\}.
\]

### Vertex substitution

Let \(F,J\) be coloured complete graphs, and let \(v\in V(F)\). The substitution
\[
H=F(v\leftarrow J)
\]
replaces \(v\) with a copy of \(J\). Edges inside \(F-v\) and \(J\) retain their colours, and, for every \(x\in V(F)\setminus\{v\}\), all edges from \(x\) to \(J\) receive the colour of \(xv\) in \(F\).

Let \(\mathcal S_3\) be the smallest class containing every \([3]\)-coloured edge and triangle and closed under vertex substitution.

### Theorem

For every \(H\in\mathcal S_3\), there are explicitly computable constants \(C_H\ge1\) and \(d_H>0\) such that every \(H\)-free three-colouring \(G\) satisfies
\[
|V(G)|\le C_H A(G)^{d_H}. \tag{1}
\]
Consequently, the conjectured polynomial conclusion holds for these patterns.

The following choices are valid for the initial patterns:
\[
\begin{array}{c|c|c}
H&C_H&d_H\\ \hline
\text{a coloured edge}&1&1\\
\text{a monochromatic triangle}&2&2\\
\text{a triangle using exactly two colours}&1&2\\
\text{a rainbow triangle}&1&3
\end{array} \tag{2}
\]
If \(H=F(v\leftarrow J)\) and \(a=|V(F)|\), valid recursive choices are
\[
\boxed{
\begin{aligned}
d_H&=(a-1)d_F+d_J,\\
C_H&=2^a C_F^{\,a-1}C_J.
\end{aligned}} \tag{3}
\]

I prove these statements below. The only structural theorem used is the classical Gallai partition theorem, stated explicitly in Section 2.

---

## 2. The edge and triangle cases

For each colour \(c\in[3]\), write
\[
a_c(G)=\max\{|S|:G[S]\text{ has no edge of colour }c\}.
\]
Thus
\[
A(G)=\max_{c\in[3]}a_c(G). \tag{4}
\]

### A forbidden coloured edge

If \(G\) avoids an edge of colour \(c\), then the entire graph avoids \(c\). Hence \(A(G)=|V(G)|\).

### A forbidden monochromatic triangle

Suppose \(G\) has no triangle monochromatic in colour \(c\). Let \(Q\) be the ordinary graph consisting of the edges of colour \(c\), and let \(\Delta\) be its maximum degree.

Every neighbourhood in \(Q\) is independent, so
\[
\Delta\le a_c(G).
\]
The greedy independent-set bound gives
\[
a_c(G)\ge \frac{n}{\Delta+1}.
\]
Therefore
\[
n\le a_c(G)(\Delta+1)
 \le a_c(G)\bigl(a_c(G)+1\bigr)
 \le 2A(G)^2. \tag{5}
\]

### A forbidden triangle using exactly two colours

Suppose the forbidden triangle has two edges of colour \(c\) and one edge of colour \(d\), where \(c\ne d\).

Again let \(Q\) consist of the edges of colour \(c\), with maximum degree \(\Delta\). For every vertex \(v\), the closed neighbourhood
\[
\{v\}\cup N_Q(v)
\]
contains no edge of colour \(d\): an edge of colour \(d\) between two neighbours of \(v\) would create the forbidden triangle.

Thus
\[
a_d(G)\ge \Delta+1.
\]
Combining this with the greedy bound in \(Q\),
\[
n\le a_c(G)(\Delta+1)
 \le a_c(G)a_d(G)
 \le A(G)^2. \tag{6}
\]

Both arguments remain valid with any fixed host palette.

### A forbidden rainbow triangle

Here the host palette has size three. Avoiding the fixed rainbow triangle is equivalent to having no triangle whose three edges have different colours.

I use the following standard theorem.

**Gallai partition theorem.**  
Every rainbow-triangle-free colouring of a complete graph on at least two vertices has a partition into at least two nonempty parts such that:

1. each pair of parts is joined monochromatically;
2. at most two colours occur on edges between parts.

The following product inequality gives the required polynomial bound:
\[
\boxed{a_1(G)a_2(G)a_3(G)\ge n.} \tag{7}
\]

**Proof.** Induct on \(n\). The assertion is immediate for \(n=1\).

Take a Gallai partition \(V_1,\dots,V_t\), and, after renaming colours, suppose all interpart edges have colours \(1\) or \(2\). Put
\[
a_{c,i}=a_c(G[V_i]).
\]
We have
\[
a_1(G)\ge \max_i a_{1,i},
\qquad
a_2(G)\ge \max_i a_{2,i}.
\]
Moreover, optimal colour-\(3\)-avoiding sets from all parts can be united, because no interpart edge has colour \(3\). Hence
\[
a_3(G)\ge\sum_i a_{3,i}.
\]
It follows that
\[
\begin{aligned}
a_1(G)a_2(G)a_3(G)
&\ge
\left(\max_i a_{1,i}\right)
\left(\max_i a_{2,i}\right)
\sum_i a_{3,i}\\
&\ge \sum_i a_{1,i}a_{2,i}a_{3,i}\\
&\ge \sum_i |V_i|\\
&=n,
\end{aligned}
\]
where the penultimate inequality is the induction hypothesis. This proves (7). \(\square\)

By (4) and (7),
\[
A(G)\ge n^{1/3}. \tag{8}
\]
This proves all the initial bounds in (2).

---

## 3. A quantitative substitution lemma

The closure argument applies to any fixed palette, not just three colours.

For an \(m\)-coloured complete graph \(G\), let
\[
A_m(G)=\max\{|S|:G[S]\text{ uses at most }m-1\text{ colours}\}.
\]

### Lemma

Let \(m\ge2\). Suppose that every \(F\)-free \(m\)-coloured complete graph \(Q\) satisfies
\[
|V(Q)|\le C_F A_m(Q)^{d_F},
\]
and every \(J\)-free such graph satisfies
\[
|V(Q)|\le C_J A_m(Q)^{d_J},
\]
where \(C_F,C_J\ge1\) and \(d_F,d_J>0\).

Let
\[
H=F(v\leftarrow J),\qquad a=|V(F)|\ge2.
\]
Then every \(H\)-free \(m\)-coloured complete graph \(G\) satisfies
\[
|V(G)|
\le
2^a C_F^{\,a-1}C_J\,
A_m(G)^{(a-1)d_F+d_J}. \tag{9}
\]

### Proof

Write
\[
n=|V(G)|,\qquad s=A_m(G),\qquad T=C_Js^{d_J}.
\]

For each colour-preserving embedding
\[
\phi:F-v\longrightarrow G,
\]
let \(X_\phi\) consist of all vertices \(x\notin\phi(V(F-v))\) such that
\[
\operatorname{col}_G(x\phi(u))
=
\operatorname{col}_F(vu)
\qquad
\text{for every }u\in V(F-v).
\]

If \(G[X_\phi]\) contained \(J\), then that copy of \(J\), together with \(\phi(F-v)\), would form \(H\). Therefore \(G[X_\phi]\) is \(J\)-free. Since \(A_m\) cannot increase when taking an induced subgraph,
\[
|X_\phi|
\le C_J A_m(G[X_\phi])^{d_J}
\le C_Js^{d_J}
=T. \tag{10}
\]

There are at most \(n^{a-1}\) embeddings of \(F-v\). Consequently, the number of colour-preserving labelled copies of \(F\) in \(G\) is at most
\[
Tn^{a-1}. \tag{11}
\]

Now form an \(a\)-uniform hypergraph \(\mathcal H\) on \(V(G)\): an \(a\)-set is an edge of \(\mathcal H\) if it supports a colour-preserving copy of \(F\). Its number of edges is at most the quantity in (11).

Choose each vertex independently with probability
\[
p=(2Tn^{a-2})^{-1/(a-1)}.
\]
Here \(0<p\le1\), since \(T\ge1\).

If \(S\) is the random vertex set, then
\[
\begin{aligned}
\mathbb E\bigl[|S|-e(\mathcal H[S])\bigr]
&\ge pn-p^aTn^{a-1}\\
&=\frac{pn}{2}.
\end{aligned}
\]
From any \(S\), deleting at most one vertex per hyperedge leaves an independent set in \(\mathcal H\). Thus there is a set \(U\subseteq V(G)\) such that \(G[U]\) is \(F\)-free and
\[
|U|
\ge \frac{pn}{2}
=
2^{-a/(a-1)}
\left(\frac nT\right)^{1/(a-1)}. \tag{12}
\]

On the other hand, the assumed bound for \(F\) gives
\[
|U|
\le C_F A_m(G[U])^{d_F}
\le C_Fs^{d_F}. \tag{13}
\]
Combining (12) and (13) yields
\[
n
\le 2^a C_F^{\,a-1}Ts^{(a-1)d_F}
=
2^a C_F^{\,a-1}C_Js^{(a-1)d_F+d_J},
\]
as required. \(\square\)

This proof uses neither another conjecture nor a compatibility assumption about which colour is omitted by the large sets.

---

## 4. Consequences and an explicit five-vertex example

The theorem in Section 1 follows by induction on a substitution construction of \(H\), using the initial bounds from Section 2 and the lemma.

The multiplicative constant in (1) can be removed by slightly reducing the exponent. Indeed, for \(n\ge2\),
\[
A(G)\ge2,
\]
and hence
\[
C_H\le A(G)^{\log_2 C_H}.
\]
Therefore (1) implies
\[
\boxed{
A(G)\ge n^{\varepsilon_H},
\qquad
\varepsilon_H=\frac{1}{d_H+\log_2 C_H}.
} \tag{14}
\]
The case \(n=1\) is immediate. Thus the conclusion holds for every \(n\), not merely asymptotically.

### Example

Let \(R\) be a rainbow triangle, and replace one vertex of \(R\) by another rainbow triangle. The resulting pattern \(H\) has five vertices.

More explicitly, take vertices \(x,y,u_1,u_2,u_3\), with:

- \(u_1,u_2,u_3\) forming a rainbow triangle;
- every \(xu_i\) having colour \(1\);
- every \(yu_i\) having colour \(2\);
- \(xy\) having colour \(3\).

For this pattern, the recursion gives
\[
d_H=2\cdot3+3=9,
\qquad
C_H=2^3=8.
\]
Consequently, every \(H\)-free three-colouring satisfies
\[
A(G)\ge (n/8)^{1/9},
\]
and, uniformly for all \(n\),
\[
A(G)\ge n^{1/12}. \tag{15}
\]

Hosts avoiding this five-vertex pattern are allowed to contain rainbow triangles. Thus (15) is genuinely an extension beyond the Gallai base case.

The same substitution lemma, starting only with coloured edges, also proves a special case for **every fixed number of colours**: all patterns obtained by iterated substitution from coloured edges satisfy the corresponding missing-colour conclusion.

---

## 5. The rainbow base exponent is optimal as a power of \(n\)

For completeness, an elementary construction shows that the exponent \(1/3\) in (8) cannot be increased. This is not a counterexample to the conjecture.

Fix \(t\ge2\), and put
\[
L=\lceil4\log_2 t\rceil.
\]
There exists a two-colouring of \(K_t\) with no monochromatic \(K_L\). Indeed, in a uniformly random two-colouring, the expected number of monochromatic \(K_L\)'s is
\[
2\binom tL2^{-\binom L2}<1
\]
when \(L\le t\); when \(L>t\), the assertion is automatic.

Choose such a colouring and make three recoloured copies with palettes
\[
\{1,2\},\qquad \{1,3\},\qquad \{2,3\}.
\]

Construct a three-colouring on vertex set \([t]^3\). Given distinct
\[
x=(x_1,x_2,x_3),\qquad y=(y_1,y_2,y_3),
\]
let \(j\) be their first differing coordinate, and colour \(xy\) according to the \(j\)-th two-colouring applied to \(x_jy_j\).

### No rainbow triangle

For three vertices, examine the first coordinate at which they are not all equal.

- If their three values at that coordinate are distinct, all three edges receive colours from one two-colour palette.
- If exactly two values coincide, the two edges joining the third vertex to those two vertices receive the same colour.

Thus the construction has no rainbow triangle.

### Bounding two-colour sets

Fix a colour \(c\), and consider a set avoiding \(c\).

At a coordinate whose palette contains \(c\), the occupied coordinate values must form a monochromatic clique in the other colour, so there are at most \(L-1\) occupied branches. At the one coordinate whose palette omits \(c\), there are at most \(t\) branches.

Applying this recursively gives
\[
a_c(G)\le t(L-1)^2.
\]
Since this holds for every \(c\),
\[
A(G)\le t(L-1)^2.
\]
With \(n=t^3\), this is
\[
A(G)=O\!\left(n^{1/3}(\log n)^2\right). \tag{16}
\]

Therefore no exponent larger than \(1/3\) can hold uniformly for rainbow-triangle-free three-colourings. The lower bound above does not establish a matching logarithmic factor.

---

## 6. Exact limitation of the argument

The substitution family is proper.

For example, colour \(K_4\) by
\[
\begin{array}{c|c}
\text{colour}&\text{edges}\\ \hline
1&12,\ 34\\
2&13,\ 24\\
3&14,\ 23.
\end{array}
\]
Every vertex sees its three neighbours in three different colours.

A **module** in a coloured complete graph is a vertex set \(M\) such that every vertex outside \(M\) sends a single colour to all of \(M\). The displayed \(K_4\) has no module of size two or three. But every pattern with more than three vertices obtained by the substitution construction has a proper module: the vertex set inserted in its final substitution. Hence this \(K_4\) pattern is not covered by the theorem. I make no claim here about the literature status of this particular pattern.

The proof stops precisely where it needs a substituted module. That module allows an embedding of \(F-v\) to define a candidate set \(X_\phi\), inside which a copy of \(J\) completes the desired pattern. For an arbitrary prime coloured pattern, this mechanism supplies no bound.

Thus the outcome is a rigorous, quantitative special case—not a resolution of the multicolour Erdős–Hajnal conjecture.