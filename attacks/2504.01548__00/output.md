```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit 35-vertex graph at d=2 has chromatic number 18 and defective blowup chromatic number 17, improving the quoted universal lower bound to 18/17.",
  "would_publish": false,
  "caveats": "The upper bound 2 is unchanged, and novelty has not been checked beyond the literature review supplied in the prompt."
}
```

# Mathematical writeup

## 1. Result

Let
\[
c_*=\sup_{G,\ d\ge 0}\frac{\chi(G)}
 {\chi^d(G\boxtimes K_{d+1})}.
\]

I construct a graph \(G\) such that
\[
\chi(G)=18
\qquad\text{and}\qquad
\chi^2(G\boxtimes K_3)=17.
\]
Consequently,
\[
\boxed{\frac{18}{17}\le c_*\le 2}.
\]
Since \(18/17>30/29\), this improves the lower bound quoted in the question.

The construction also bootstraps to graphs of arbitrarily large chromatic number and to infinitely many defects.

---

## 2. Multiplicity formulation

Put \(q=d+1\). Given a coloring of \(G\boxtimes K_q\), let
\[
m_i(v)
\]
be the number of vertices in the \(K_q\)-fiber over \(v\) receiving color \(i\). Thus
\[
\sum_i m_i(v)=q.
\]

A vertex of color \(i\) in the fiber over \(v\) has same-colored degree
\[
m_i(v)-1+\sum_{u\in N_G(v)}m_i(u).
\]
Therefore the coloring is \((q-1)\)-defective if and only if
\[
m_i(v)+\sum_{u\in N_G(v)}m_i(u)\le q
\tag{2.1}
\]
whenever \(m_i(v)>0\).

We use this with \(q=3\).

---

## 3. An unsatisfiable multiset formula on 17 symbols

Let the set of symbols be
\[
\begin{aligned}
\Sigma={}&\{x_0,x_1,x_2,x_3\}\\
&\cup\{z_0,z_1,z_2\}\\
&\cup\{r_j,s_j:1\le j\le3\}\\
&\cup\{p_j,q_j:1\le j\le2\}.
\end{aligned}
\]
Thus \(|\Sigma|=4+3+6+4=17\).

A triple below is a multiset, so repetitions matter for the eventual defective coloring.

Define the family of positive triples
\[
\begin{aligned}
\mathcal P={}&
 \{(x_j,r_j,r_j),(x_j,s_j,s_j):1\le j\le3\}\\
&\cup
 \{(z_j,p_j,p_j),(z_j,q_j,q_j):1\le j\le2\}\\
&\cup\{(x_0,x_0,z_0)\},
\end{aligned}
\tag{3.1}
\]
and the family of negative triples
\[
\begin{aligned}
\mathcal N={}&
 \{(x_{j-1},r_j,s_j):1\le j\le3\}\\
&\cup
 \{(z_{j-1},p_j,q_j):1\le j\le2\}\\
&\cup\{(x_1,x_2,x_3),(z_0,z_1,z_2)\}.
\end{aligned}
\tag{3.2}
\]

Interpret a positive triple \((a,b,c)\) as the clause
\[
a\lor b\lor c
\]
and a negative triple as
\[
\neg a\lor\neg b\lor\neg c.
\]
Repeated literals have their usual logical meaning.

### Lemma 3.1
The resulting Boolean formula is unsatisfiable.

#### Proof

For symbols \(u,v,r,s\), the three clauses
\[
(v,r,r),\qquad (v,s,s),\qquad (\neg u,\neg r,\neg s)
\]
entail \(u\Rightarrow v\). Indeed, if \(u\) is true and \(v\) is false, the first two clauses force \(r=s=\mathrm{true}\), contradicting the negative clause.

It follows from the first three such blocks that
\[
x_0\Rightarrow x_1\Rightarrow x_2\Rightarrow x_3.
\]
The negative clause
\[
\neg x_1\lor\neg x_2\lor\neg x_3
\]
therefore forces \(x_0\) to be false.

Similarly,
\[
z_0\Rightarrow z_1\Rightarrow z_2,
\]
and the clause
\[
\neg z_0\lor\neg z_1\lor\neg z_2
\]
forces \(z_0\) to be false.

Finally, the positive triple \((x_0,x_0,z_0)\) is the clause
\[
x_0\lor z_0,
\]
a contradiction. ∎

---

## 4. Multiplicity capacities

For \(i\in\Sigma\), let

- \(P_i\) be the total multiplicity of \(i\) in all triples of \(\mathcal P\);
- \(\widehat P_i\) be its largest multiplicity in one positive triple;
- \(N_i\) and \(\widehat N_i\) be defined analogously for \(\mathcal N\).

Directly from (3.1)–(3.2),
\[
\begin{array}{c|cccc}
i & P_i & \widehat P_i & N_i & \widehat N_i\\ \hline
x_0 &2&2&1&1\\
z_0 &1&1&2&1\\
x_1,x_2,z_1 &2&1&2&1\\
x_3,z_2 &2&1&1&1\\
r_j,s_j,p_j,q_j &2&2&1&1
\end{array}
\tag{4.1}
\]
where the last row ranges over all relevant auxiliary symbols.

In every row,
\[
\widehat P_i+N_i\le3
\qquad\text{and}\qquad
\widehat N_i+P_i\le3.
\tag{4.2}
\]

These are precisely the inequalities needed for the defective coloring.

---

## 5. Construction of \(G\)

Create:

1. a clique
   \[
   C=\{c_i:i\in\Sigma\}\cong K_{17};
   \]
2. one vertex \(v_M\) for every \(M\in\mathcal P\);
3. one vertex \(v_M\) for every \(M\in\mathcal N\).

There are \(11\) positive and \(7\) negative triples, so
\[
|V(G)|=17+11+7=35.
\]

Add edges as follows.

- The vertices \(C\) form a clique.
- Every positive triple vertex is adjacent to every negative triple vertex.
- There are no edges within the positive side or within the negative side.
- For \(i\in\Sigma\), join \(c_i\) to \(v_M\) if and only if \(i\) does not occur in the multiset \(M\).

No other edges are present.

---

## 6. Ordinary chromatic number

### Proposition 6.1
\[
\chi(G)=18.
\]

#### Lower bound

Suppose that \(G\) had a proper \(17\)-coloring. Since \(C\cong K_{17}\), its vertices use all \(17\) colors. Relabel the colors so that \(c_i\) receives color \(i\).

A triple vertex \(v_M\) is adjacent to \(c_i\) whenever \(i\notin\operatorname{supp}(M)\). Hence \(v_M\) must receive a color belonging to \(\operatorname{supp}(M)\).

Let \(T\subseteq\Sigma\) be the set of colors used on positive triple vertices. Every positive triple has a member in \(T\). Since the positive and negative sides are completely joined, no negative triple vertex can use a color in \(T\). Thus every negative triple has a member outside \(T\).

Assign Boolean value true precisely to the symbols in \(T\). Then every positive clause has a true literal and every negative clause has a false underlying variable. This gives a satisfying assignment to the formula of Section 3, contradicting Lemma 3.1.

Therefore \(\chi(G)\ge18\).

#### Upper bound

Color the clique \(C\) with \(17\) distinct colors. Give all positive triple vertices one new color. For each negative triple vertex \(v_M\), choose any \(i\in\operatorname{supp}(M)\) and color \(v_M\) with the color of \(c_i\).

The negative side is independent, and \(v_M\) is not adjacent to \(c_i\). All positive vertices use the new color. This is a proper \(18\)-coloring, so \(\chi(G)\le18\). ∎

---

## 7. A \(2\)-defective \(17\)-coloring of \(G\boxtimes K_3\)

Use the \(17\) colors indexed by \(\Sigma\).

- In the fiber over \(c_i\), give all three vertices color \(i\).
- In the fiber over a triple vertex \(v_M\), assign its three vertices the colors appearing in the multiset \(M\), with repetitions.

Consider a clique vertex \(c_i\). A color-\(i\) vertex in its fiber has exactly two same-colored neighbors inside its fiber. Every adjacent triple vertex omits \(i\), by the definition of the forcing edges. Thus it has no additional same-colored neighbors.

Now let \(M\in\mathcal P\), and suppose \(i\) occurs in \(M\) with multiplicity \(m_i(M)\). The only adjacent clause vertices carrying color \(i\) lie on the negative side, and their total color-\(i\) multiplicity is \(N_i\). Also, \(v_M\) is not adjacent to \(c_i\). Hence (2.1) becomes
\[
m_i(M)+N_i\le \widehat P_i+N_i\le3.
\]
Similarly, for \(M\in\mathcal N\),
\[
m_i(M)+P_i\le \widehat N_i+P_i\le3.
\]
Thus every color class has maximum degree at most \(2\), and
\[
\chi^2(G\boxtimes K_3)\le17.
\tag{7.1}
\]

On the other hand, \(G\) contains \(K_{17}\). Its \(3\)-fold clique blowup is \(K_{51}\). A \(2\)-defective color class in a complete graph contains at most three vertices, so at least \(17\) colors are required. Therefore
\[
\chi^2(G\boxtimes K_3)\ge17.
\tag{7.2}
\]

Combining (7.1) and (7.2),
\[
\boxed{\chi^2(G\boxtimes K_3)=17}.
\]

Together with Proposition 6.1,
\[
\boxed{\frac{\chi(G)}{\chi^2(G\boxtimes K_3)}=\frac{18}{17}}.
\]

---

## 8. Bootstrapping

The example has the same robustness mentioned in the source paper.

### Infinitely many defects

For any \(t\ge1\), multiply every fiber multiplicity above by \(t\). This gives fibers of size \(3t\), and all inequalities scale from
\[
m_i(v)+\sum_{u\in N(v)}m_i(u)\le3
\]
to
\[
tm_i(v)+\sum_{u\in N(v)}tm_i(u)\le3t.
\]
Hence
\[
\chi^{3t-1}(G\boxtimes K_{3t})=17.
\]

### Arbitrarily large chromatic number

Let \(G_s\) be the join of \(s\) disjoint copies of \(G\). Then
\[
\chi(G_s)=18s.
\]
Use pairwise disjoint sets of \(17\) defective colors on the \(s\) copies. This gives
\[
\chi^2(G_s\boxtimes K_3)\le17s.
\]
The joins of the \(K_{17}\)'s form a \(K_{17s}\), so equality holds:
\[
\chi^2(G_s\boxtimes K_3)=17s.
\]
Thus the ratio remains \(18/17\).

---

## 9. An upper-side structural observation

The following does not improve the global upper bound \(2\), but identifies a case where the original equality conjecture is valid.

### Lemma 9.1
Suppose a defective coloring of \(G\boxtimes K_q\) with \(k\) colors has the property that every fiber uses at most two distinct colors. Then \(\chi(G)\le k\).

#### Proof sketch with the integrality point included

Normalize the fiber multiplicities by
\[
p_i(v)=\frac{m_i(v)}q.
\]
For every used pair \((v,i)\),
\[
p_i(v)+\sum_{\substack{u\in N(v)\\p_i(u)>0}}p_i(u)\le1.
\tag{9.1}
\]

Create an auxiliary graph whose vertices are the used pairs \((v,i)\), partitioned by \(v\), with an edge between \((u,i)\) and \((v,i)\) whenever \(uv\in E(G)\). Give \((v,i)\) weight \(p_i(v)\). Each part has size at most two and total weight one.

One must choose one auxiliary vertex from every part, with no two chosen vertices adjacent. This is a weighted two-choice independent-transversal problem. It is always feasible under (9.1). A concise proof uses the standard \(2\)-SAT implication digraph:

- a conflict edge \(ab\) produces implications \(a\to\bar b\) and \(b\to\bar a\);
- along an implication \(a\to\bar b\),
  \[
  w(\bar b)=1-w(b)\ge w(a)
  \]
  by (9.1);
- if the formula were unsatisfiable, some \(a,\bar a\) would lie in one strongly connected component, forcing every weight in that component to equal \(1/2\);
- equality in (9.1) then forces every occurrence there to have exactly one conflict neighbor;
- the part edges and conflict edges consequently form alternating even cycles, on which the implication map has two orbits exchanged by the part involution, so \(a\) and \(\bar a\) cannot be strongly connected.

Thus an independent transversal exists. Choosing its color at each base vertex gives a proper \(k\)-coloring of \(G\). ∎

Two consequences are:

1. For every graph \(G\),
   \[
   \chi^1(G\boxtimes K_2)=\chi(G).
   \]
2. If \(\chi^d(G\boxtimes K_{d+1})\le3\), then
   \[
   \chi(G)\le \chi^d(G\boxtimes K_{d+1}).
   \]
   For the case of three defective colors, take a chromatic-critical subgraph of minimum degree at least \(3\). A vertex using all three colors would, after summing (9.1) over those colors, satisfy
   \[
   1+\deg(v)\le3,
   \]
   a contradiction. Hence every fiber uses at most two colors, and Lemma 9.1 applies.

In particular, the equality conjecture is valid for all graphs with \(\chi(G)\le4\), for every \(d\).

---

## 10. Remaining gap

The construction proves only
\[
\frac{18}{17}\le c_*.
\]
It gives no improvement to the established upper bound
\[
c_*\le2.
\]
In particular, there is presently no argument here excluding examples with ratios substantially larger than \(18/17\), nor a construction approaching \(2\). The exact value of \(c_*\) therefore remains open.