```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Hajós' bound is proved here for L(H) whenever H is simple, connected and Eulerian with |E(H)| <= 2|V(H)| + 5, including all line graphs of connected simple 4-regular graphs.",
  "would_publish": false,
  "caveats": "This is a restricted-class result; novelty has not been checked, and the general conjecture is not resolved."
}
```

## 1. Result and scope

Write \(c(G)\) for the minimum number of simple cycles in an edge-decomposition of \(G\).

I do not obtain a proof or counterexample for the full conjecture. The following is a self-contained partial result.

**Theorem.** Let \(H\) be a connected simple graph with at least one edge, all of whose degrees are even. Put
\[
h=|V(H)|,\qquad m=|E(H)|.
\]
If
\[
m\le 2h+5,
\]
then its line graph satisfies
\[
c(L(H))\le \left\lfloor\frac{m-1}{2}\right\rfloor.
\]

This is an instance of Hajós’ conjecture: \(L(H)\) has \(m\) vertices, and the vertex corresponding to \(uv\in E(H)\) has even degree
\[
d_H(u)+d_H(v)-2.
\]

In particular:

**Corollary.** Every line graph of a connected simple \(4\)-regular graph satisfies Hajós’ conjecture. These line graphs are \(6\)-regular.

The supplied attempt treated line graphs of roots with degrees in \(\{1,3\}\). Here the root has even degrees. I do not assume its weighted packing lemma or its claimed theorem. The shared idea—recombining local cycles—is proved again below in the form needed here.

## 2. An Euler-tour decomposition of the line graph

We first need an elementary clique decomposition.

**Lemma 1.** If \(M\) is a perfect matching of \(K_{2r}\), then \(K_{2r}-M\) decomposes into \(r-1\) Hamilton cycles.

**Proof.** The case \(r=1\) is immediate. For \(r\ge2\), use vertices
\[
\{\infty\}\cup\mathbb Z_{2r-1}.
\]
For \(i=0,\ldots,r-2\), take
\[
\bigl(\infty,i,i-1,i+1,i-2,i+2,\ldots,
i-(r-1),i+(r-1),\infty\bigr),
\]
with arithmetic modulo \(2r-1\).

These are Hamilton cycles. The finite edges in the \(i\)-th cycle are exactly the edges whose endpoint sums are \(2i-1\) or \(2i\). Thus the cycles are edge-disjoint. The unused finite edges have endpoint sum \(2r-3\); they match every finite vertex except \(2r-2\). The remaining unused edge is \(\infty(2r-2)\). Hence the unused edges form a perfect matching.

Relabeling sends that matching to any prescribed \(M\). \(\square\)

Now choose an Euler circuit of \(H\). Its cyclic sequence of edges is a Hamilton cycle \(A\) of \(L(H)\).

For each \(v\in V(H)\), the edges incident with \(v\) form a clique \(K_{d_H(v)}\) in \(L(H)\). The Euler circuit pairs those edges at its passages through \(v\), and \(A\) uses precisely the corresponding perfect matching \(M_v\) in this clique.

Because \(H\) is simple, these local cliques partition \(E(L(H))\). Lemma 1 therefore gives a decomposition consisting of:

- the Hamilton cycle \(A\);
- for each \(v\), a collection \(\mathcal D_v\) of
  \[
  b_v:=\frac{d_H(v)}2-1
  \]
  local Hamilton cycles on the set of edges incident with \(v\).

Its total number of cycles is
\[
1+\sum_v b_v=1+m-h.
\tag{1}
\]

The task is to save enough cycles by recombining members of the collections \(\mathcal D_v\).

## 3. A recombination lemma allowing matching chords

Call a simple cycle \(C\) of \(H\) **admissible** if the chords of \(C\) form a matching. In particular, every induced cycle and every \(4\)-cycle is admissible.

**Lemma 2.** Let
\[
C=v_1v_2\cdots v_\ell v_1
\]
be admissible, with \(b_{v_i}\ge1\) for every \(i\). Choose one local cycle
\[
D_i\in\mathcal D_{v_i}.
\]
Then the union of the \(D_i\) decomposes into two simple cycles.

**Proof.** Write \(e_i=v_iv_{i+1}\), cyclically. The local cycle \(D_i\) contains two edge-disjoint arcs between the vertices \(e_{i-1}\) and \(e_i\) of \(L(H)\). Color one arc red and the other blue.

An edge \(f\) of \(H\) outside \(C\) appears as a vertex in two of the selected local cycles exactly when \(f\) is a chord of \(C\). In that case, choose the arc colors so that \(f\) lies internally on a red arc at one endpoint and a blue arc at the other.

These choices are possible: the chords form a matching, so no vertex \(v_i\) participates in two such constraints.

Concatenate the red arcs around \(C\), and likewise the blue arcs. Each concatenation is a simple cycle:

- the vertices \(e_1,\ldots,e_\ell\) are distinct splice vertices;
- an edge of \(H\) leaving \(V(C)\) occurs in only one selected local cycle;
- a chord occurs at most once in each color, by construction.

The two resulting cycles partition all edges of the selected local cycles. \(\square\)

Consequently, an admissible cycle of length \(\ell\) saves \(\ell-2\) cycles.

More generally, let \(\mathcal F\) be a list of admissible cycles such that each vertex \(v\) occurs in at most \(b_v\) members of the list. Repetitions are allowed if the capacities permit them. Assign different members of \(\mathcal D_v\) to different occurrences of \(v\). The selected local cycles are edge-disjoint, so all recombinations can be performed independently. Thus
\[
c(L(H))
\le 1+m-h-W(\mathcal F),
\qquad
W(\mathcal F):=\sum_{C\in\mathcal F}(|V(C)|-2).
\tag{2}
\]

This bound is useful beyond the density range of the theorem.

## 4. An elementary capacitated packing lemma

We will apply (2) to the subgraph induced by vertices of degree at least four.

Two elementary observations provide the needed packing.

### 4.1. Finding admissible long cycles

If a graph contains a cycle of length at least four, choose a shortest such cycle \(C\).

- If \(|C|=4\), its possible chords are its two diagonals, which form a matching.
- If \(|C|\ge5\), it has no chord: a chord would produce a shorter cycle of length at least four.

Thus every graph containing a cycle of length at least four contains an admissible one of length at least four.

### 4.2. Graphs with no cycle longer than a triangle

**Lemma 3.** A simple graph on \(p\ge1\) vertices with no cycle of length at least four has at most
\[
\frac32(p-1)
\tag{3}
\]
edges.

**Proof.** Induct on \(p\). Choose a longest path \(v_1\cdots v_k\). All neighbors of \(v_1\) lie on the path, and none can be \(v_j\) with \(j\ge4\). Thus \(d(v_1)\le2\).

If \(d(v_1)\le1\), delete \(v_1\) and apply induction.

Otherwise its neighbors are \(v_2,v_3\). The rotated path
\[
v_2v_1v_3\cdots v_k
\]
is also longest, so \(v_2\) has no neighbor outside the path. A neighbor \(v_j\), \(j\ge4\), would give the cycle
\[
v_2v_1v_3\cdots v_jv_2,
\]
of length at least four. Hence \(v_2\) also has degree two, with neighbors \(v_1,v_3\).

Deleting \(v_1,v_2\) removes exactly three edges. Induction gives
\[
|E|\le 3+\frac32(p-3)=\frac32(p-1).
\]
The initial cases are immediate. \(\square\)

We can now state the packing result.

**Lemma 4.** Let \(Q\) be a simple graph on \(s\) vertices. Give each vertex an integer capacity \(b_v\ge1\), and suppose
\[
b_v=1\quad\Longrightarrow\quad d_Q(v)\le4.
\tag{4}
\]
There is a capacity-respecting list \(\mathcal F\) of admissible cycles with the following guaranteed weights:
\[
\begin{array}{c|c}
\text{Hypothesis}&W(\mathcal F)\text{ at least}\\ \hline
s\ge2,\quad |E(Q)|\ge2s-2&2\\
|E(Q)|\ge2s+2&3\\
|E(Q)|\ge2s+4&4.
\end{array}
\tag{5}
\]

**Proof.** We first record a counting observation for a selected \(k\)-cycle \(C\). Let
\[
Z=\{v\in V(C):b_v=1\},\qquad z=|Z|.
\]
After using \(C\), every vertex outside \(Z\) still has positive remaining capacity. Thus any one further cycle in \(Q-Z\) is compatible with \(C\).

The cycle \(C\) supplies at least
\[
\max(0,2z-k)
\]
edges inside \(Z\). By (4), the number of edges of \(Q\) incident with \(Z\) is at most
\[
4z-e_Q(Z).
\]
Assume \(s>z\). If \(Q-Z\) is a forest, it follows that
\[
\begin{aligned}
|E(Q)|
&\le 4z-e_Q(Z)+s-z-1\\
&\le s+3z-\max(0,2z-k)-1\\
&\le s+2k-1.
\end{aligned}
\tag{6}
\]
If \(Q-Z\) has no cycle of length at least four, Lemma 3 similarly gives
\[
\begin{aligned}
|E(Q)|
&\le 4z-e_Q(Z)+\frac32(s-z-1)\\
&\le \frac32(s+k-1).
\end{aligned}
\tag{7}
\]

We prove the three assertions.

**First assertion.** Since \(s\ge2\),
\[
2s-2>\frac32(s-1).
\]
Lemma 3 gives a cycle of length at least four. By Section 4.1, there is an admissible such cycle, of weight at least two.

**Second assertion.** Simplicity and \(|E(Q)|\ge2s+2\) imply \(s\ge6\).

If \(Q\) has no \(4\)-cycle, a shortest cycle of length at least four has length at least five and supplies weight at least three.

Otherwise choose a \(4\)-cycle \(C\). If \(Q-Z\) were a forest, (6) would give
\[
|E(Q)|\le s+7<2s+2,
\]
a contradiction. Choose a shortest cycle in \(Q-Z\); it is induced, hence admissible. Together with \(C\), it gives weight at least \(2+1=3\).

**Third assertion.** Here simplicity implies \(s\ge7\).

If \(Q\) has a \(4\)-cycle \(C\), then \(Q-Z\) must contain a cycle of length at least four. Otherwise (7) would give
\[
|E(Q)|\le \frac32(s+3)<2s+4.
\]
Choose an admissible cycle of length at least four in \(Q-Z\). Together with \(C\), its weight is at least four.

Suppose instead that \(Q\) has no \(4\)-cycle. Choose a shortest cycle of length at least four. It is induced and has length at least five. Length at least six already supplies weight four.

The remaining case is an induced \(5\)-cycle \(C\). If \(Q-Z\) were a forest, (6) would give
\[
|E(Q)|\le s+9<2s+4.
\]
Thus \(Q-Z\) contains a cycle. Taking a shortest one gives an admissible second cycle and total weight at least \(3+1=4\).

In each two-cycle construction, common vertices have capacity at least two because the second cycle avoids \(Z\). This proves all three assertions. \(\square\)

## 5. Proof of the theorem

Return to \(H\). Set
\[
S=\{v:d_H(v)\ge4\},\qquad D=\{v:d_H(v)=2\},
\]
and write
\[
s=|S|,\qquad d=|D|,\qquad h=s+d.
\]
Let
\[
Q=H[S],\qquad e_D=|E(H[D])|.
\]

Counting degrees in \(D\) gives
\[
m=|E(Q)|+2d-e_D,
\]
or equivalently
\[
|E(Q)|=m-2d+e_D.
\tag{8}
\]
Assign the capacities
\[
b_v=\frac{d_H(v)}2-1\qquad(v\in S).
\]
These are positive integers and satisfy (4).

Because \(Q\) is induced in \(H\), every admissible cycle of \(Q\) is also admissible in \(H\).

### The sparse case

If \(m\le2h-3\), the initial decomposition (1) already gives
\[
c(L(H))\le m-h+1\le\frac{m-1}{2}.
\tag{9}
\]

### The remaining cases

Suppose \(m\ge2h-2\). We first check that \(s\ge2\).

If \(s=0\), then \(H\) is a cycle, so \(m=h\) and \(h\ge3\), contrary to \(m\ge2h-2\).

If \(s=1\), then \(Q\) has no edges. Equation (8), together with \(m\ge2h-2=2d\), forces \(e_D=0\). Every degree-two vertex would then need two distinct neighbors in the singleton \(S\), impossible in a simple graph. Hence \(s\ge2\).

Put
\[
k=m-2h.
\]
By (8),
\[
|E(Q)|\ge2s+k.
\tag{10}
\]
Since \(m\le2h+5\), the remaining possibilities are covered by the following table:
\[
\begin{array}{c|c|c}
k&\text{Packing lemma used}&W(\mathcal F)\text{ at least}\\ \hline
-2,-1,0,1&\text{first assertion}&2\\
2,3&\text{second assertion}&3\\
4,5&\text{third assertion}&4.
\end{array}
\tag{11}
\]
In each row,
\[
W(\mathcal F)\ge \frac{k+3}{2}
=\frac{m-2h+3}{2}.
\]
Consequently, (2) yields
\[
\begin{aligned}
c(L(H))
&\le 1+m-h-W(\mathcal F)\\
&\le 1+m-h-\frac{m-2h+3}{2}\\
&=\frac{m-1}{2}.
\end{aligned}
\]
The cycle count is integral, proving
\[
\boxed{c(L(H))\le\left\lfloor\frac{m-1}{2}\right\rfloor.}
\]

For a \(4\)-regular root, \(m=2h\), so this gives
\[
c(L(H))\le h-1
=\left\lfloor\frac{|V(L(H))|-1}{2}\right\rfloor.
\]

## 6. What remains unresolved

The proof above is complete for the stated class. Its limitations are structural, not omitted cases:

1. An arbitrary Eulerian graph need not be a line graph.
2. Even among line graphs of even-degree roots, the argument does not give the required saving for every root with \(m>2h+5\).

The general recombination bound (2) identifies a possible route further: sufficiently heavy admissible-cycle packings, with capacities \(d_H(v)/2-1\), would give additional cases. No general assertion about such packings is assumed here.

I have not checked whether the restricted theorem, or a stronger theorem encompassing it, already appears in the literature. No external paper is needed for the proof above.