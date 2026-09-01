```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but the mixed ordinary/non-nested Ramsey number is determined exactly, every putative counterexample must have an ordinary n-matching in each color, and the case n=2 is proved.",
  "would_publish": false,
  "caveats": "The hard case where both colors have ordinary n-matchings remains; the global upper bound is not improved, and no unreported computation is claimed."
}
```

## 1. Statement and notation

Let \(M(n)\) denote the least \(m\) such that every red-blue coloring of the edges of the ordered complete graph on
\[
1<2<\cdots <m
\]
contains a monochromatic non-nested matching of size \(n\).

For an ordered graph \(G\), write

- \(\nu(G)\) for its ordinary matching number;
- \(\nu_{\mathrm{nn}}(G)\) for its maximum non-nested matching size.

If independent edges are written as \(e_i=a_i b_i\), where \(a_i<b_i\), then they form a non-nested matching precisely when, after ordering them so that
\[
a_1<a_2<\cdots<a_k,
\]
one also has
\[
b_1<b_2<\cdots<b_k.
\]

I do not resolve the conjecture \(M(n)=3n-1\). I prove three partial results:

1. \(M(1)=2\) and \(M(2)=5\).
2. An exact asymmetric theorem: for \(1\le r\le b\), the least \(N\) forcing either a red ordinary \(r\)-matching or a blue non-nested \(b\)-matching is
   \[
   2b+r-1.
   \]
   In particular, every counterexample to \(M(n)=3n-1\) must contain an ordinary \(n\)-matching in both colors.
3. The conjectured conclusion holds whenever one color contains a clique on \(2n-1\) consecutive vertices. Thus the standard lower-bound construction cannot be extended by one vertex while retaining its monochromatic interval clique.

The second result is an elementary consequence of Tutte–Berge together with an ordered biclique observation. I have not checked whether this precise mixed formulation is already folklore.

---

## 2. The standard lower bound

On \(3n-2\) vertices, partition the vertices into sets \(A,B\) with
\[
|A|=2n-1,\qquad |B|=n-1.
\]
Color all edges inside \(A\) red and every edge having an endpoint in \(B\) blue.

The red graph is \(K_{2n-1}\), so its ordinary matching number is \(n-1\). Every blue edge meets \(B\), so \(B\) is a blue vertex cover and the blue matching number is at most \(n-1\). Therefore neither color has even an ordinary matching of size \(n\), and hence
\[
M(n)\ge 3n-1.
\]

---

## 3. A monochromatic biclique always gives a non-nested matching

### Lemma 3.1
Let \(A,B\) be disjoint sets of \(t\) ordered vertices. If every edge between \(A\) and \(B\) has the same color, then there is a non-nested matching of that color of size \(t\), irrespective of how \(A\) and \(B\) are interleaved.

### Proof
Write
\[
A=\{a_1<\cdots<a_t\},\qquad B=\{b_1<\cdots<b_t\}.
\]
Take the matching
\[
a_i b_i,\qquad 1\le i\le t.
\]
Set
\[
\ell_i=\min\{a_i,b_i\},\qquad r_i=\max\{a_i,b_i\}.
\]
Because both \(a_i\) and \(b_i\) increase strictly with \(i\), so do \(\ell_i\) and \(r_i\). Thus no edge in the matching nests another. ∎

Consequently, a putative counterexample to the conjecture contains no monochromatic \(K_{n,n}\), even with arbitrarily interleaved bipartition classes.

---

## 4. An exact mixed Ramsey theorem

Define \(R_{\mathrm{mix}}(r,b)\) to be the least \(N\) such that every red-blue coloring of ordered \(K_N\) contains either

- a red ordinary matching of size \(r\), or
- a blue non-nested matching of size \(b\).

### Theorem 4.1
For \(1\le r\le b\),
\[
R_{\mathrm{mix}}(r,b)=2b+r-1.
\]

The main graph-theoretic ingredient is the following stronger, order-free statement.

### Lemma 4.2
Let \(1\le r\le b\), and let \(G\) be a graph on
\[
N=2b+r-1
\]
vertices with \(\nu(G)\le r-1\). Then \(\overline G\) contains \(K_{b,b}\).

### Proof
By the Tutte–Berge formula, there is a set \(S\subseteq V(G)\), with \(s=|S|\), such that
\[
o(G-S)-s
   =N-2\nu(G)
   \ge (2b+r-1)-2(r-1)
   =2b-r+1.
\]
Thus, if \(q=o(G-S)\),
\[
q\ge s+2b-r+1.
\]
Since \(q\le N-s\), this implies \(s\le r-1\). Put
\[
D=r-1-s.
\]
Then
\[
0\le D\le r-1\le b-1.
\]

Let the components of \(G-S\) have orders
\[
a_1,\ldots,a_Q.
\]
There are at least \(q\) components, so
\[
Q\ge q\ge s+2b-r+1=2b-D.
\]
Moreover,
\[
\sum_{i=1}^{Q}a_i=N-s=2b+D.
\]

We claim that the components can be divided into two collections, each containing at least \(b\) vertices in total.

Order the component sizes so that
\[
a_1\le a_2\le\cdots\le a_Q,
\]
and let \(k\) be minimal with
\[
a_1+\cdots+a_k\ge b.
\]
The total excess over singleton components satisfies
\[
\sum_{i=1}^{Q}(a_i-1)
  =(2b+D)-Q
  \le 2D.
\]

If \(a_k\le D+1\), then by the minimality of \(k\),
\[
a_1+\cdots+a_k\le (b-1)+(D+1)=b+D.
\]
Hence the remaining components have total order at least
\[
(2b+D)-(b+D)=b,
\]
as required.

Suppose instead that \(a_k\ge D+2\). Every component with index at least \(k\) then contributes at least \(D+1\) to the excess. Since the total excess is at most \(2D\), there can be at most one such component. Thus \(k=Q\). But then
\[
a_1+\cdots+a_{k-1}\ge Q-1\ge 2b-D-1\ge b,
\]
because \(D\le b-1\). This contradicts the minimality of \(k\).

Therefore the desired division exists. Let \(U_1,U_2\) be unions of the two collections of components, and choose
\[
A\subseteq U_1,\qquad B\subseteq U_2,
\qquad |A|=|B|=b.
\]
There are no \(G\)-edges between distinct components of \(G-S\), so every edge between \(A\) and \(B\) lies in \(\overline G\). Hence \(\overline G\) contains \(K_{b,b}\). ∎

### Proof of Theorem 4.1

For the upper bound, apply Lemma 4.2 to the red graph. If it has no ordinary \(r\)-matching, then the blue graph contains \(K_{b,b}\), which by Lemma 3.1 contains a blue non-nested \(b\)-matching. Therefore
\[
R_{\mathrm{mix}}(r,b)\le 2b+r-1.
\]

For sharpness, consider \(2b+r-2\) vertices partitioned into
\[
|A|=2b-1,\qquad |B|=r-1.
\]
Color all edges inside \(A\) blue and every other edge red. The blue graph has matching number at most \(b-1\), while every red edge meets \(B\), so the red graph has matching number at most \(r-1\). Thus
\[
R_{\mathrm{mix}}(r,b)>2b+r-2.
\]
This proves equality. ∎

### Corollary 4.3
If a red-blue coloring of ordered \(K_{3n-1}\) has no monochromatic non-nested \(n\)-matching, then
\[
\nu(R)\ge n\qquad\text{and}\qquad \nu(B)\ge n.
\]

### Proof
Apply Theorem 4.1 with \(r=b=n\). Since there is no blue non-nested \(n\)-matching, the red graph must have an ordinary \(n\)-matching. Interchanging the colors gives an ordinary blue \(n\)-matching. ∎

Thus the conjecture is reduced to the genuinely ordered residual case where both colors already have ordinary \(n\)-matchings. The Tutte–Berge obstruction cannot occur in a counterexample.

---

## 5. Exact solution for \(n=2\)

### Proposition 5.1
\[
M(2)=5.
\]

### Proof
The lower-bound coloring on \(K_4\) consists of a red triangle and a blue star centered at the fourth vertex. Neither color has a matching of size \(2\), so \(M(2)\ge5\).

For the upper bound, suppose the edges of ordered \(K_5\) are colored with no monochromatic non-nested matching of size \(2\). Consider the following five graph edges:
\[
12,\quad 35,\quad 24,\quad 13,\quad 45.
\]
Consecutive terms in the cyclic list
\[
12-35-24-13-45-12
\]
are disjoint and non-nested:

- \(12\) and \(35\) are separated;
- \(35\) and \(24\) cross;
- \(24\) and \(13\) cross;
- \(13\) and \(45\) are separated;
- \(45\) and \(12\) are separated.

Therefore every consecutive pair in this \(5\)-cycle must receive opposite colors. That would give a proper \(2\)-coloring of an odd cycle, which is impossible. Hence \(K_5\) always has the desired matching. ∎

Together with the trivial \(M(1)=2\), this settles the first two values.

---

## 6. A consecutive monochromatic \(K_{2n-1}\) is sufficient

This treats the structure occurring in the standard lower-bound coloring.

### Proposition 6.1
Let \(N\ge3n-1\). Suppose a red-blue coloring of ordered \(K_N\) contains a red clique
\[
C=\{c_1<\cdots<c_{2n-1}\}
\]
whose vertices form a consecutive interval in the ambient order. Then the coloring contains either a red or a blue non-nested matching of size \(n\).

### Proof
Let \(L\) be the vertices before \(C\), and \(R\) those after \(C\). Thus
\[
|L|+|R|\ge n.
\]
Assume there is no red non-nested \(n\)-matching.

We first determine many forced blue edges.

#### Edges from the left

Let \(x\in L\) and \(1\le i\le n\). If \(xc_i\) were red, then the following would be a red non-nested matching of size \(n\):

- the edge \(xc_i\);
- the edges
  \[
  c_jc_{i+j},\qquad 1\le j\le i-1;
  \]
- consecutive pairs on the remaining vertices
  \[
  c_{2i},c_{2i+1},\ldots,c_{2n-1}.
  \]

The latter set has even order \(2(n-i)\). When the displayed edges are ordered by their left endpoints, their right endpoints also increase, so the matching is non-nested. Consequently,
\[
xc_i\text{ is blue for every }x\in L,\ 1\le i\le n. \tag{6.1}
\]

#### Edges to the right

By the reversed argument, if \(z\in R\) and \(n\le i\le2n-1\), then \(c_i z\) must be blue. Explicitly, if it were red, put \(d=2n-1-i\), pair the first \(2(i-n)\) clique vertices consecutively, pair
\[
c_{2(i-n)+j}\ \text{with}\ c_{i+j},
\qquad 1\le j\le d,
\]
and add \(c_i z\). This is again a red non-nested \(n\)-matching. Hence
\[
c_i z\text{ is blue for every }z\in R,\ n\le i\le2n-1. \tag{6.2}
\]

Choose nonnegative integers \(\ell,r\) such that
\[
\ell+r=n,\qquad \ell\le |L|,\qquad r\le |R|.
\]
This is possible because \(|L|+|R|\ge n\).

Choose
\[
x_1<\cdots<x_\ell\in L,\qquad
z_1<\cdots<z_r\in R.
\]
By (6.1) and (6.2), all edges in
\[
\{x_jc_j:1\le j\le\ell\}
\cup
\{c_{n+j-1}z_j:1\le j\le r\}
\]
are blue. Within each group the left and right endpoints increase together. If both groups are nonempty, then \(\ell<n\), so
\[
c_\ell<c_n,
\]
and the two groups are separated. Therefore these \(n\) blue edges form a non-nested matching. ∎

Thus a counterexample on \(3n-1\) vertices cannot contain a monochromatic clique on \(2n-1\) consecutive vertices.

---

## 7. Exact SAT formulation for finite checks

Although I have not run a solver or produced a proof certificate, finite instances admit a compact, fully explicit CNF encoding.

For every edge \(e\) of \(K_m\), introduce a Boolean variable \(x_e\), with \(x_e=1\) meaning red.

A non-nested perfect matching on a fixed ordered set of \(2n\) vertices is encoded by a Dyck word of length \(2n\):

- positions marked \(L\) are the left endpoints;
- positions marked \(R\) are the right endpoints;
- the \(k\)-th \(L\) is paired with the \(k\)-th \(R\).

The Dyck prefix condition ensures that every left endpoint precedes its partner. Conversely, every non-nested perfect matching arises uniquely this way. Hence there are \(C_n\) such matchings on a fixed \(2n\)-set, where
\[
C_n=\frac1{n+1}\binom{2n}{n}.
\]

For every non-nested \(n\)-matching \(Q\), add the two clauses
\[
\bigvee_{e\in Q}x_e,
\qquad
\bigvee_{e\in Q}\neg x_e.
\]
The first forbids \(Q\) from being all blue; the second forbids it from being all red. The resulting formula is satisfiable exactly when a counterexample exists.

It has
\[
\binom m2
\]
variables and
\[
2C_n\binom{m}{2n}
\]
clauses. For \(n=3,m=8\), this is \(28\) variables and
\[
2\cdot 5\cdot\binom86=280
\]
clauses. No satisfiability result for this instance is asserted here; a certified UNSAT output would be needed for a computer-assisted theorem.

---

## 8. Remaining gap

The main conjecture is still open after these reductions. A counterexample on \(3n-1\) vertices would have to satisfy at least the following:

1. both color graphs have ordinary matching number at least \(n\);
2. neither color contains a monochromatic \(K_{n,n}\);
3. neither color contains a clique on \(2n-1\) consecutive vertices.

The mixed theorem stops precisely because an ordinary monochromatic \(n\)-matching need not be non-nested. There is no direct uncrossing operation: if red edges \(ad\) and \(bc\) are nested with
\[
a<b<c<d,
\]
the two non-nested replacement pairings
\[
\{ab,cd\},\qquad \{ac,bd\}
\]
need not be red. Thus the residual case requires genuinely two-color ordered structure, not just ordinary matching theory.

The catalogued \((2+\sqrt3)n\) upper bound is not improved by the arguments above.