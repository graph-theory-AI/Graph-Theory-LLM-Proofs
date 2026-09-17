```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The sharp bound floor((2k+1)/3) holds for every four-terminal graft, without the previous attempt's independence restriction.",
  "would_publish": false,
  "caveats": "Uses Mader's classical free-path min–max theorem; no novelty claim, and the conjecture for unbounded terminal sets remains unresolved."
}
```

## 1. A stronger four-terminal result

Write
\[
\lambda(G,T)=\min\{|\delta_G(X)|:|X\cap T|\text{ is odd}\},
\]
and let \(\nu(G,T)\) be the maximum number of pairwise edge-disjoint \(T\)-joins.

The restriction that the nonterminals be independent can be removed from the supplied partial result.

**Theorem.** Let \(G\) be a finite loopless multigraph and let \(|T|=4\). If \(\lambda(G,T)\ge k\), where \(k\) is a nonnegative integer, then
\[
\boxed{\nu(G,T)\ge \left\lfloor\frac{2k+1}{3}\right\rfloor.}
\tag{1}
\]
For every positive integer \(k\), equality is attained by a simple bipartite graph.

Consequently, the conjectured inequality holds for all four-terminal grafts with \(c=1/3\), and this constant is best possible in that class. There is **no restriction on the graph induced by the nonterminals**.

The proof below uses the classical free-path min–max theorem. It does not use the previous attempt’s exact formula. The sharp examples are independently checked in Section 4. I do not claim novelty for the four-terminal theorem.

## 2. The classical min–max theorem used

For a graph \(H\) with a specified terminal set \(A\), an **\(A\)-path** is a path whose ends are distinct members of \(A\) and whose internal vertices are outside \(A\). Let \(\mu(H,A)\) denote the maximum number of pairwise edge-disjoint \(A\)-paths.

I use the following standard form of **Mader’s free-path theorem**.

For every family
\[
\mathcal X=(X_a:a\in A)
\]
of pairwise disjoint vertex sets with \(a\in X_a\), put
\[
W=V(H)\setminus\bigcup_{a\in A}X_a.
\]
Let \(\omega_H(\mathcal X)\) be the number of components \(C\) of \(H[W]\) for which \(|\delta_H(C)|\) is odd. Then
\[
\boxed{
\mu(H,A)=
\min_{\mathcal X}
\frac12\left(
\sum_{a\in A}|\delta_H(X_a)|
-\omega_H(\mathcal X)
\right).
}
\tag{2}
\]

Every expression on the right is an integer. Indeed, it also equals
\[
\left|\bigcup_{\{a,b\}\subseteq A}E_H(X_a,X_b)\right|
+
\sum_{C\in\operatorname{comp}(H[W])}
\left\lfloor\frac{|\delta_H(C)|}{2}\right\rfloor .
\tag{3}
\]

The upper-bound direction follows by counting the passages of edge-disjoint paths through these regions. The converse is the substantive classical theorem. This is the only non-elementary external ingredient below.

### Converting saturated free paths into four-terminal join packings

Let
\[
T=\{t_1,t_2,t_3,t_4\},
\]
and fix an integer \(q\ge1\). Form \(H_q\) by adding new vertices \(z_1,\dots,z_4\), with \(q\) parallel edges between \(z_i\) and \(t_i\). Use
\[
A=\{z_1,z_2,z_3,z_4\}
\]
as the free-path terminal set.

If \(H_q\) has \(2q\) edge-disjoint \(A\)-paths, then every edge incident with every \(z_i\) is used: the paths have \(4q\) ends in total, exactly the available terminal degree.

Delete the first and last edges of each path. This gives edge-disjoint paths in \(G\) between distinct members of \(T\), with exactly \(q\) path ends at each \(t_i\).

Make an auxiliary multigraph \(F\) on \(\{1,2,3,4\}\), one edge for each such path. Then \(F\) is \(q\)-regular. If \(n_{ij}\) denotes its edge multiplicities, regularity gives
\[
n_{12}=n_{34},\qquad
n_{13}=n_{24},\qquad
n_{14}=n_{23}.
\]
Thus its edges partition into \(q\) perfect matchings.

For each matching, take the union of the two corresponding paths in \(G\). Every original terminal is an endpoint exactly once; occurrences as an internal vertex contribute even degree. Hence this union is a \(T\)-join. The resulting \(q\) joins are edge-disjoint.

Therefore
\[
\mu(H_q,A)=2q
\quad\Longrightarrow\quad
\nu(G,T)\ge q.
\tag{4}
\]

## 3. Proof of the lower bound

If \(k=0\), the assertion is trivial. If \(k=1\) or \(2\), the required packing size is one. Positive minimum \(T\)-cut size implies that every connected component meets \(T\) evenly, which guarantees a \(T\)-join. For example, in a rooted spanning tree, select a parent edge precisely when the subtree below it contains an odd number of terminals.

Hence assume \(k\ge3\), and put
\[
q=\left\lfloor\frac{2k+1}{3}\right\rfloor.
\]
We show that every expression in Mader’s formula for \((H_q,A)\) is at least \(2q\).

### 3.1. Expressing an arbitrary obstruction

Take any admissible family \(X_1,\dots,X_4\) in (2), where \(z_i\in X_i\). Define
\[
Y_i=X_i\cap V(G),\qquad
W=V(G)\setminus\bigcup_{i=1}^4Y_i,
\]
and
\[
B=\sum_{i=1}^4|\delta_G(Y_i)|.
\]

We need two counts describing the positions of the **original** terminals:
\[
M=\sum_i|Y_i\cap T|,
\qquad
a=|\{i:t_i\in Y_i\}|.
\]
Thus \(M\) terminals lie in the four regions, and \(a\) lie in their correctly indexed regions. Set
\[
\sigma=2a-M.
\]

A pendant edge \(z_it_i\) contributes:

* zero to \(\sum_j|\delta_{H_q}(X_j)|\) if \(t_i\in Y_i\);
* two if \(t_i\in Y_j\) for \(j\ne i\);
* one if \(t_i\in W\).

Consequently, the total contribution of the added edges is
\[
2q(M-a)+q(4-M)=q(4-\sigma).
\]

For a component \(C\) of \(G[W]\), write \(m_C=|C\cap T|\). Its boundary in \(H_q\) has size
\[
|\delta_{H_q}(C)|=|\delta_G(C)|+qm_C.
\]
Let \(h\) count the components for which this number is odd. The expression in Mader’s theorem is therefore
\[
\Phi=\frac12\bigl(B+q(4-\sigma)-h\bigr).
\tag{5}
\]

### 3.2. A harmless normalization

Suppose a component \(C\) of \(G[W]\) contains no original terminal and satisfies
\[
|\delta_G(C)|=1.
\]
Its unique boundary edge goes to some \(Y_i\). Move all of \(C\) into \(Y_i\).

This decreases both \(B\) and \(h\) by one, so it leaves \(\Phi\) unchanged. It also leaves \(M,a,\sigma\) unchanged. Repeating this operation, we may assume that
\[
C\cap T=\varnothing
\quad\Longrightarrow\quad
|\delta_G(C)|\ne1.
\tag{6}
\]

Thus it suffices to bound \(\Phi\) for normalized families.

### 3.3. Two estimates

First,
\[
h\le B.
\tag{7}
\]
To see this, every component counted by \(h\) has positive boundary in \(G\). If \(m_C\) is even, being counted forces \(|\delta_G(C)|\) to be odd. If \(m_C\) is odd, then
\[
|\delta_G(C)|\ge k.
\]
Also,
\[
\sum_C|\delta_G(C)|\le B,
\]
because edges between different \(Y_i\)'s are counted twice in \(B\), while edges from \(W\) to the regions are counted once.

For the stronger estimate, let \(z\) be the number of components \(C\) of \(G[W]\) containing a positive even number of original terminals. Then
\[
\boxed{3h\le B+2z.}
\tag{8}
\]

Indeed, consider a component counted by \(h\).

* If \(m_C=0\), its boundary in \(G\) is odd and, by (6), at least three.
* If \(m_C\) is odd, its boundary is at least \(k\ge3\).
* If \(m_C\) is positive and even, its boundary is odd and at least one; allowing an extra two accounts for this case.

Summing these inequalities proves (8).

Let \(o\) denote the number of regions \(Y_i\) containing an odd number of original terminals. Every such region defines a \(T\)-cut, so
\[
B\ge ok.
\tag{9}
\]
Moreover,
\[
o\ge\sigma.
\tag{10}
\]
For a pointwise verification, put \(m_i=|Y_i\cap T|\) and
\(a_i=\mathbf1_{\{t_i\in Y_i\}}\). Then
\[
2a_i-m_i\le m_i\bmod2;
\]
summing gives (10).

Finally,
\[
\sigma\le M,\qquad 2z\le4-M,
\]
and hence
\[
\boxed{\sigma+2z\le4.}
\tag{11}
\]

### 3.4. Finishing the estimate

If \(\sigma\le0\), equations (5) and (7) immediately give
\[
\Phi
=2q+\frac{B-h-q\sigma}{2}
\ge2q.
\]

Suppose now that \(\sigma>0\). By (8)–(10),
\[
B-h\ge\frac23(B-z)
\ge\frac23(\sigma k-z).
\]
Since \(3q\le2k+1\),
\[
\frac23(\sigma k-z)
\ge
\sigma q-\frac{\sigma+2z}{3}
\ge \sigma q-\frac43,
\]
where the last step uses (11). Substitution in (5) yields
\[
\Phi\ge2q-\frac23.
\]
But \(\Phi\) is an integer, by (3). Therefore
\[
\Phi\ge2q.
\]

Every family in Mader’s formula has value at least \(2q\). On the other hand, \(H_q\) has total degree \(4q\) at its four new terminals, so it cannot contain more than \(2q\) edge-disjoint \(A\)-paths. Thus
\[
\mu(H_q,A)=2q.
\]
The conversion in (4) supplies \(q\) edge-disjoint \(T\)-joins, proving (1). \(\square\)

## 4. Sharpness for every minimum cut value

Here is a direct verification of the extremal family from the supplied attempt.

For nonnegative integers \(a_1,a_2,a_3,a_4\), construct a simple bipartite graph with terminal side
\[
T=\{t_1,t_2,t_3,t_4\}.
\]
For each \(i\), add \(a_i\) nonterminals adjacent to exactly \(T\setminus\{t_i\}\). Put
\[
A=a_1+a_2+a_3+a_4.
\]

Every \(T\)-cut can be complemented so that its shore contains just one terminal, say \(t_i\). Each nonterminal adjacent to \(t_i\) contributes at least one edge to such a cut, and the singleton cut \(\delta(\{t_i\})\) attains this lower bound. Hence
\[
\lambda(G,T)=A-\max_i a_i.
\tag{12}
\]

Every nonterminal has degree three. A \(T\)-join uses either zero or two of its incident edges, so a nonterminal can be used by at most one join in a packing. Every join needs at least four terminal incidences and thus at least two nonterminals. Therefore
\[
\nu(G,T)\le\left\lfloor\frac A2\right\rfloor.
\tag{13}
\]

Choose the parameters as follows:
\[
\begin{array}{c|c|c}
k &(a_1,a_2,a_3,a_4)&\lfloor A/2\rfloor\\ \hline
3r &(r,r,r,r)&2r\\
3r+1 &(r+1,r+1,r,r)&2r+1\\
3r+2 &(r+1,r+1,r+1,r)&2r+1.
\end{array}
\]
Here \(r\ge0\), omitting the zero-cut instance in the first row. Equation (12) gives \(\lambda=k\), while (13) equals the lower bound proved above. Thus
\[
\nu(G,T)=\left\lfloor\frac{2k+1}{3}\right\rfloor
\]
for every positive \(k\).

In particular:

* \(k=3r\) shows that the coefficient \(2/3\) cannot be improved, even with four terminals.
* \(k=3r+2\) gives
  \[
  \nu=\frac23k-\frac13,
  \]
  so \(c=1/3\) is optimal for the four-terminal class.

## 5. Why this does not settle the general conjecture

There are two specifically four-terminal steps.

1. The obstruction estimate uses
   \[
   \sigma+2z\le4.
   \]
   This makes the possible deficit in \(\Phi\) strictly less than one, so integrality eliminates it. With an unbounded terminal set, this rounding argument no longer gives a uniform additive loss.

2. A regular loopless multigraph on four vertices decomposes into perfect matchings. A regular multigraph on an arbitrary even number of vertices need not do so. Thus saturating terminal degrees by free paths is not, in general, enough to obtain the desired number of joins.

The Petersen graph also confirms that the improved four-terminal constant cannot hold universally. For completeness, this obstruction can be checked directly.

Use vertices \(a_i,b_i\), indexed modulo five, and edges
\[
a_i a_{i+1},\qquad b_i b_{i+2},\qquad a_i b_i,
\]
and take \(T=V(G)\). The graph is cubic and bridgeless. Every odd-vertex cut has odd size, so
\[
\lambda(G,T)=3.
\]

Two disjoint \(T\)-joins would each have degree one at every vertex: two positive odd degrees must sum to at most three. They would therefore be disjoint perfect matchings.

Every perfect matching has either one or five spokes \(a_ib_i\). The number of spokes must be odd; three spokes are impossible because the two remaining indices would have to be adjacent both in the outer and inner five-cycles. With one spoke, the remaining matching is forced. The five-spoke matching meets every other matching; among single-spoke matchings, consecutive spoke indices give a shared inner edge, and indices at cyclic distance two give a shared outer edge. Thus every two perfect matchings intersect, and
\[
\nu(G,T)=1.
\]
Any universal inequality of the proposed form must consequently have
\[
1\ge \frac23\cdot3-c,
\qquad\text{so}\qquad
\boxed{c\ge1.}
\]

**Conclusion.** The four-terminal special case admits the sharp bound (1) for completely arbitrary nonterminal structure. The proof uses a proved classical min–max theorem, with no additional conjectural step. It does not establish the desired bound for unbounded \(|T|\), and it does not improve the general guarantee stated in the question.