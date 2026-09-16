```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for subcubic critical graphs when the lists have a common color or use at most three distinct list types, and for arbitrary maximum degree when all list variation is confined to one star.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; these are self-contained partial results, with no claim of novelty."
}
```

## 1. Statements of the partial results

I work with finite simple graphs. A list assignment is **constant** if all its lists are identical.

The following cases can be proved.

**Theorem A — a subcubic case.**  
Let \(G\) be \(3\)-edge-critical, and let \(|L(e)|=3\) for every edge. Suppose there is a set \(T\) of colors such that
\[
|L(e)\cap T|=1\qquad\text{for every }e\in E(G).
\]
Then \(G\) is \(L\)-edge-colorable unless \(L\) is constant.

Consequently, the conjecture holds for a \(3\)-edge-critical graph whenever either:

1. all lists have a common color; or
2. at most three distinct lists occur.

The second consequence does not require a common color.

**Theorem B — variation on one star.**  
Let \(G\) be \(\Delta\)-edge-critical. Suppose there are a vertex \(v\) and a set \(S\) of \(\Delta\) colors such that
\[
L(f)=S\qquad\text{for every edge }f\text{ not incident with }v.
\]
If every list has size \(\Delta\) and the assignment is nonconstant, then \(G\) is \(L\)-edge-colorable.

I also give the full elementary verification for \(\Delta\leq 2\).

The main ingredient for Theorem A is a structural property of \(3\)-edge-critical graphs: deleting a suitable matching leaves exactly one odd cycle, and that odd cycle can be made nonmonochromatic under any prescribed nonconstant edge labelling.

---

## 2. Preliminary observations and the case \(\Delta=2\)

After isolated vertices are discarded, an edge-critical graph is connected. Indeed, if there were two edge-containing components, one would fail to be \(\Delta\)-edge-colorable; deleting an edge in another component would preserve that obstruction.

It also has minimum degree at least two. If \(e=uv\) had \(d(u)=1\), a \(\Delta\)-edge-coloring of \(G-e\) could be extended to \(e\): some color is missing at \(v\), and every color is missing at \(u\).

Thus there are no such simple graphs with \(\Delta\leq 1\). When \(\Delta=2\), the graph, apart from isolated vertices, must be an odd cycle.

We will use the following elementary list-coloring fact.

**Two-list fact.**

- Every path is edge-colorable from arbitrary lists of size two.
- Every even cycle is edge-colorable from arbitrary lists of size two.
- An odd cycle is edge-colorable from lists of size two unless all its lists are identical.

For a path, color greedily from an end. For a cycle with nonconstant lists, order its edges cyclically as \(e_1,\ldots,e_m\) so that \(L(e_1)\neq L(e_m)\). Choose
\[
a\in L(e_1)\setminus L(e_m),
\]
color \(e_1\) with \(a\), and color \(e_2,\ldots,e_m\) greedily, avoiding the preceding edge’s color. The last edge cannot receive \(a\), so the coloring closes properly. If the lists are constant, an even cycle can be colored alternately, whereas an odd cycle cannot.

This proves the conjecture completely for \(\Delta=2\).

---

## 3. A structural lemma for \(3\)-edge-critical graphs

**Lemma 1.**  
Let \(G\) be \(3\)-edge-critical.

1. For every edge \(e\), there is a matching \(M_e\) such that \(G-M_e\) has maximum degree at most two and has exactly one odd-cycle component \(C_e\), with \(e\in E(C_e)\).
2. Given any nonconstant edge labelling
   \[
   \lambda:E(G)\longrightarrow X,
   \]
   there is such a matching \(M\) whose unique odd-cycle component is not monochromatic under \(\lambda\).

### Proof of part 1

Fix \(e=uv\), and take a proper \(3\)-edge-coloring \(\varphi\) of \(G-e\).

Choose a color \(\alpha\) missing at \(u\) and a color \(\beta\) missing at \(v\). The sets of missing colors at \(u\) and \(v\) are disjoint: otherwise we could color \(e\). In particular, \(\alpha\neq\beta\), color \(\beta\) occurs at \(u\), and color \(\alpha\) occurs at \(v\).

The \(\alpha\beta\)-component containing \(u\) must also contain \(v\). Otherwise, interchanging \(\alpha\) and \(\beta\) in that component would make \(\beta\) missing at both ends of \(e\), again allowing an extension.

Consequently this component is an alternating path \(P\) from \(u\) to \(v\). It starts with color \(\beta\) and ends with color \(\alpha\), so it has even length. Therefore
\[
C_e=P+e
\]
is an odd cycle.

Let \(\gamma\) be the third color, and let
\[
M_e=\{f\in E(G-e):\varphi(f)=\gamma\}.
\]
This is a matching.

Every vertex other than \(u,v\) has degree at most two in \(G-M_e\), since only its \(\alpha\)- and \(\beta\)-colored edges remain. At \(u\), the remaining edges are \(e\) and its \(\beta\)-colored edge; at \(v\), they are \(e\) and its \(\alpha\)-colored edge. Thus \(G-M_e\) has maximum degree at most two, and \(C_e\) is a component.

Every other component inherits a proper edge-coloring with \(\alpha,\beta\). Hence its cycles are even. This proves part 1.

### Proof of part 2

Because \(G\) is connected on its edges and \(\lambda\) is nonconstant, there are incident edges \(e,f\) with
\[
\lambda(e)\neq\lambda(f).
\]
Let their common endpoint be \(v\).

Construct \(C_e\) and \(C_f\) as in part 1. Each cycle uses two edges incident with \(v\). Since \(d(v)\leq3\), these two pairs of edges intersect. Thus \(C_e\) and \(C_f\) share an edge incident with \(v\).

If both cycles were monochromatic, their shared edge would imply
\[
\lambda(e)=\lambda(f),
\]
a contradiction. At least one of \(C_e,C_f\) is therefore nonmonochromatic, and its associated matching proves part 2. \(\square\)

---

## 4. Proof of Theorem A

Suppose \(L\) is nonconstant and \(T\) meets every list in exactly one color. Put
\[
R(e)=L(e)\setminus T.
\]
Each \(R(e)\) has size two.

First, we may arrange that the assignment \(R\) is nonconstant.

If it is already nonconstant, nothing is needed. Otherwise, write
\[
R(e)=\{a,b\}\qquad\text{for every }e.
\]
Then
\[
L(e)=\{a,b,t_e\},\qquad t_e\in T.
\]
Since \(L\) is nonconstant, the colors \(t_e\) are not all equal. Replace \(T\) by the singleton \(\{a\}\). It still meets each list exactly once, and the new residual lists
\[
L(e)\setminus\{a\}=\{b,t_e\}
\]
are nonconstant.

Thus assume \(R\) is nonconstant. Apply Lemma 1 with the edge labelling
\[
\lambda(e)=R(e).
\]
We obtain a matching \(M\) such that \(G-M\) has maximum degree at most two, exactly one odd-cycle component \(C\), and nonconstant residual lists on \(C\).

Now color:

- each edge \(e\in M\) with the unique color in \(L(e)\cap T\);
- every component of \(G-M\) from its two-element lists \(R(e)\).

The first step is proper because \(M\) is a matching. The second is possible by the two-list fact: paths and even cycles always work, and the unique odd cycle has nonconstant lists.

Finally, colors on \(M\) lie in \(T\), whereas all colors used on \(G-M\) lie outside \(T\). Hence no conflict occurs between the two parts.

This is an \(L\)-edge-coloring of \(G\). \(\square\)

### Common-color consequence

If a color \(c\) belongs to every list, take \(T=\{c\}\). Theorem A applies immediately.

### At-most-three-list-types consequence

The following set-system observation supplies the required set \(T\).

**Lemma 2.**  
For any family of at most three sets, each of size three, there is a set meeting each member of the family in exactly one element.

**Proof.**  
Repeat sets if necessary and write the family as \(A,B,C\), allowing repetitions.

If \(A\cap B\cap C\neq\varnothing\), a singleton from this intersection works.

Otherwise every element occurs in either one or two of these three sets. The total number of occurrences is
\[
|A|+|B|+|C|=9.
\]
Since this is odd, some element occurs exactly once. Relabel the sets so that
\[
x\in A\setminus(B\cup C).
\]

If \(B\cap C\neq\varnothing\), choose \(y\in B\cap C\). The empty triple intersection gives \(y\notin A\), so \(\{x,y\}\) meets each set exactly once.

If \(B\cap C=\varnothing\), choose
\[
y\in B\setminus A,\qquad z\in C\setminus A.
\]
Both choices exist: \(A,B,C\) have the same size, while \(x\in A\setminus B\) and \(x\in A\setminus C\). Since \(B,C\) are disjoint, \(\{x,y,z\}\) meets each set exactly once. \(\square\)

Applying Lemma 2 to the distinct list values, then Theorem A, proves the claimed three-list-type case.

---

## 5. Proof of Theorem B: variation confined to one star

Let
\[
F=\{f\in E(G):f\text{ is incident with }v\},\qquad r=|F|\leq\Delta.
\]
All lists outside \(F\) equal \(S\).

Since the assignment is nonconstant, some edge \(e\in F\) has \(L(e)\neq S\). Choose
\[
b\in L(e)\setminus S.
\]
Take a proper edge-coloring \(\varphi\) of \(G-e\) using the palette \(S\).

We first choose pairwise distinct colors \(a_f\in L(f)\), for \(f\in F\), with \(a_e=b\). For each \(f\neq e\),
\[
|L(f)\setminus\{b\}|\geq \Delta-1\geq r-1.
\]
Thus the remaining \(r-1\) colors can be chosen greedily, avoiding \(b\) and all previously chosen colors.

For each \(f\in F\setminus\{e\}\) with \(a_f\in S\), prescribe
\[
\pi(\varphi(f))=a_f.
\]
The colors \(\varphi(f)\) on \(F\setminus\{e\}\) are distinct, and the prescribed target colors are distinct. Therefore these prescriptions extend to a permutation \(\pi\) of \(S\).

Apply \(\pi\) to the coloring \(\varphi\). Then recolor each edge \(f\in F\setminus\{e\}\) with \(a_f\), and color \(e\) with \(b\).

This is proper:

- At \(v\), the colors \(a_f\) are pairwise distinct.
- If \(a_f\in S\), its color agrees with \(\pi(\varphi(f))\), so it creates no new conflict with edges outside \(F\).
- If \(a_f\notin S\), it cannot conflict with an edge outside \(F\), since all those edges use colors in \(S\).

Every edge receives a color from its list. This proves Theorem B. \(\square\)

---

## 6. What remains unresolved

The exact-transversal hypothesis in Theorem A is a genuine restriction. For example, the four list types
\[
\{1,2,3\},\quad
\{1,2,4\},\quad
\{1,3,4\},\quad
\{2,3,4\}
\]
have no set \(T\) meeting every list exactly once. Indeed, summing the four required intersection sizes would give
\[
3|T\cap\{1,2,3,4\}|=4,
\]
which is impossible.

This is **not** a counterexample to the conjecture; it identifies a family outside Theorem A.

The proof’s limitation is also concrete. Without a separating color set \(T\), coloring the matching \(M\) may exclude two different colors from an edge of \(G-M\), one at each endpoint. Its remaining list may then have only one color, so the two-list path-and-cycle argument no longer applies.

Thus the unrestricted conjecture remains unresolved here, including general \(3\)-list assignments on \(3\)-edge-critical graphs. The results above establish the stated subcubic and star-supported special cases without relying on any unproved conjecture or external literature claim.