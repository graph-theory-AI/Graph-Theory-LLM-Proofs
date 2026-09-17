```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I determine phi(3,b) for 2 <= b <= 9, including phi(3,7)=phi(3,8)=2 and phi(3,9)=3, but do not obtain a general formula.",
  "would_publish": false,
  "caveats": "Novelty relative to the cited preprint is unverified; the general problem, and even phi(3,10), remain unresolved here."
}
```

# 1. Partial determination

Write
\[
G_{a,b,t}=K_{a,b}+K_t.
\]

I prove
\[
\boxed{G_{3,b,2}\text{ is }4\text{-choosable if and only if }b\le 8}
\tag{1}
\]
and
\[
\boxed{G_{3,9,3}\text{ is }5\text{-choosable}.}
\tag{2}
\]

Together with explicit bad-list assignments, these give
\[
\boxed{
\phi(3,b)=
\begin{cases}
0,&b=2,\\
1,&3\le b\le6,\\
2,&7\le b\le8,\\
3,&b=9.
\end{cases}}
\tag{3}
\]

The main extension of the previous attempt is a **mixed-list strengthening of its star argument**. This strengthening permits proofs at \(t=2\) and \(t=3\), rather than only at \(t=1\).

I also verify and retain the previous attempt’s general obstruction:
\[
b\ge k\left\lceil\frac{k}{a-1}\right\rceil+1
\quad\Longrightarrow\quad
G_{a,b,k-2}\text{ is not }k\text{-choosable},
\qquad a\ge3.
\tag{4}
\]

All arguments below are self-contained, apart from standard use of Hall’s marriage theorem. I do not claim that these small-parameter values are new relative to the literature mentioned in the question.

---

# 2. Preliminary observations

Let \(A,B\) be the independent parts, and \(C\) the joined clique.

After properly coloring \(A\cup C\), let \(S\) be its set of used colors. The coloring extends to \(B\) precisely when
\[
L(v)\nsubseteq S\qquad(v\in B).
\tag{5}
\]
The vertices of \(B\) can then be colored independently.

Also, if a graph \(H\) is \(r\)-choosable, then \(H+K_1\) is \((r+1)\)-choosable: color the new universal vertex and delete its color from the remaining lists. Thus chromatic-choosability persists along the sequence \(G_{a,b,t}\). In particular,
\[
G_{a,b,k-2}\text{ not }k\text{-choosable}
\quad\Longrightarrow\quad
\phi(a,b)\ge k-1.
\tag{6}
\]

Finally, if all vertices of one independent part have a common list color, the assignment is colorable. Color that part with the common color, then color the clique greedily, and color the other independent part last.

---

# 3. Explicit obstructions

## Proposition 1

Let \(a\ge3\) and \(k\ge2\). If
\[
b\ge k\left\lceil\frac{k}{a-1}\right\rceil+1,
\]
then \(G_{a,b,k-2}\) is not \(k\)-choosable.

### Proof

Set
\[
m=a-1,\qquad s=\left\lceil\frac{k}{m}\right\rceil.
\]
Take disjoint color sets \(P,Q\), with
\[
|P|=k,\qquad |Q|=s.
\]
Choose \(s\)-element subsets \(D_1,\dots,D_m\) of \(P\) whose union is \(P\). This is possible because \(ms\ge k\).

For \(A=\{u_0,u_1,\dots,u_m\}\), put
\[
L(u_0)=P,\qquad
L(u_i)=(P\setminus D_i)\cup Q\quad(1\le i\le m).
\]
Give all \(k-2\) clique vertices the list \(P\).

On the other side use a vertex \(v_0\) with list \(P\), and vertices \(v_{p,q}\), for \(p\in P,q\in Q\), with lists
\[
L(v_{p,q})=(P\setminus\{p\})\cup\{q\}.
\]

Suppose a proper list coloring exists. The clique and \(u_0\) use \(k-1\) distinct colors from \(P\). Write their used-color set as \(P\setminus\{p\}\), and let \(y\) be the color of \(u_0\).

Choose \(i\) with \(y\in D_i\). Vertex \(u_i\) cannot use \(y\), nor any clique color. Consequently its color is either \(p\), or some \(q\in Q\).

* If it uses \(p\), all colors of \(L(v_0)=P\) occur on neighbors of \(v_0\).
* If it uses \(q\in Q\), all colors of \(L(v_{p,q})\) occur on neighbors of \(v_{p,q}\).

Both are impossible. Adding further vertices to \(B\) cannot repair the obstruction. ∎

For the present application, Proposition 1 gives
\[
\boxed{G_{3,7,1}\text{ is not }3\text{-choosable}}
\tag{7}
\]
and
\[
\boxed{G_{3,9,2}\text{ is not }4\text{-choosable}.}
\tag{8}
\]

---

# 4. A split-graph lemma

The following small surplus-list result will deal with colors occurring on almost all of \(B\).

## Lemma 2 — One extra color on a clique vertex

Let \(H=K_r+\overline{K_s}\), where \(s\le r\). Suppose every list has size at least \(r\), and at least one clique vertex has a list of size at least \(r+1\). Then \(H\) is \(L\)-colorable.

### Proof

Consider the bipartite list-incidence graph between the \(r\) clique vertices and their colors. Its list union has size at least \(r+1\).

After deleting any one color \(c\), Hall’s condition still holds:

* a set of at most \(r-1\) clique vertices has list union of size at least \(r-1\);
* all \(r\) clique vertices together have list union of size at least \(r\).

Thus the clique has a proper coloring avoiding any prescribed color.

Fix a clique coloring whose used-color set is \(S\), where \(|S|=r\). For every \(c\in S\), there is a clique coloring with used-color set
\[
(S\setminus\{c\})\cup\{q_c\},
\qquad q_c\notin S.
\tag{9}
\]
Indeed, delete the matching edge using \(c\). Since the list-incidence graph with \(c\) deleted has a matching saturating the clique, an augmenting path replaces \(c\) by one color outside \(S\), retaining the other colors of \(S\).

The original set \(S\), together with the \(r\) sets in (9), gives \(r+1\) distinct attainable \(r\)-element color sets.

An independent vertex with a list of size at least \(r\) can block at most one of these sets: its list must have size exactly \(r\) and equal the used-color set. Since there are at most \(r\) independent vertices, one clique coloring extends to all of them. ∎

## Corollary 3 — An almost-common color

Consider a \(k\)-list assignment on \(G_{a,b,k-2}\), with
\[
k\ge a+1.
\]
If some color occurs in at least \(b-1\) lists on \(B\), the assignment is colorable.

### Proof

If the color occurs in all \(B\)-lists, use the common-color observation.

Otherwise let \(p\) occur in all but one \(B\)-list, and let \(v\) be the exceptional vertex. Delete \(p\) from all lists on \(A\cup C\cup\{v\}\).

The vertices \(C\cup\{v\}\) form a clique of size \(r=k-1\). All remaining lists have size at least \(r\), and \(v\)'s list still has size \(r+1\). The independent part \(A\) has size \(a\le r\). Lemma 2 colors this subgraph avoiding \(p\). Color all other vertices of \(B\) with \(p\). ∎

---

# 5. The mixed-list star lemma

Here is the principal technical step.

## Lemma 4

Let \(H=K_{3,b}+K_1\). Suppose the universal vertex and the three vertices in the first independent part have lists of size at least three. All lists on the other independent part have size at least three.

Let \(n_3\) and \(n_4\) be the numbers of lists of size exactly three and exactly four on that other part. If
\[
\boxed{n_3\le6,\qquad 3n_3+n_4\le20,}
\tag{10}
\]
then \(H\) is \(L\)-colorable.

Lists of size at least five are unrestricted in number.

### Proof

Trim the four lists on the star to size three. Write \(R\) for the center list and \(L_1,L_2,L_3\) for the leaf lists.

A coloring of the star uses at most four colors, so lists of size at least five on \(B\) can be ignored.

If
\[
L_1\cap L_2\cap L_3\ne\varnothing,
\]
color all leaves alike and the center differently. Only two colors are used, and the coloring extends. Hence assume the triple intersection is empty.

## 5.1. Forced three-element lists

Define a graph \(J\) on the colors: \(uv\) is an edge when \(\{u,v\}\) meets all three leaf lists.

Put
\[
\mathcal F=
\{\{c,u,v\}:c\in R,\ uv\in E(J),\ c\notin\{u,v\}\}.
\tag{11}
\]
Because the triple intersection is empty, each member of \(\mathcal F\) is the exact used-color set of a proper star coloring.

Therefore, in an uncolorable assignment, every member of \(\mathcal F\) must occur as a three-element list on \(B\). A four-element list cannot block a three-color star coloring. In particular,
\[
|\mathcal F|\le n_3\le6.
\tag{12}
\]

Inclusion–exclusion gives
\[
|\mathcal F|
=
3e(J)-\sum_{c\in R}d_J(c)
-\sum_{\{c,d\}\subseteq R}|N_J(c)\cap N_J(d)|
+\mathbf1_{\{R\text{ induces a triangle}\}}.
\tag{13}
\]

Let
\[
x=|L_1\cap L_2|,\quad
y=|L_1\cap L_3|,\quad
w=|L_2\cap L_3|,
\]
and relabel so that \(x\ge y\ge w\). The possibilities are
\[
(0,0,0),(1,0,0),(2,0,0),(3,0,0),
(1,1,0),(2,1,0),(1,1,1),(2,1,1).
\tag{14}
\]

A color in the intersection of two leaf lists is adjacent in \(J\) precisely to the colors in the third list. This determines the following table.

| \((x,y,w)\) | Non-isolated part of \(J\) | Minimum \( |\mathcal F| \) |
|---|---|---:|
| \((3,0,0)\) | \(K_{3,3}\) | \(9\) |
| \((2,0,0)\) | \(K_{2,3}\) | \(6\) |
| \((1,1,0)\) | An edge with two pendant leaves at each endpoint | \(7\) |
| \((2,1,0)\) | \(K_{2,3}\), with a pendant edge at a vertex in the three-vertex part | \(8\) |
| \((1,1,1)\) | A triangle with one pendant leaf at each vertex | \(7\) |
| \((2,1,1)\) | \(K_{2,3}\), with an edge inside the three-vertex part | \(7\) |

Here are details verifying the minima, including all possible positions of \(R\).

* For \(K_{3,3}\), distributions \(3+0\) and \(2+1\) between its parts give \(9\) and \(15\).
* For \(K_{2,3}\), taking \(0,1,2\) vertices in its two-vertex part gives \(6,9,7\). Equality at six occurs only when \(R\) is its entire three-vertex part.
* For the double star, taking \(2,1,0\) centers gives minima \(7,7,11\).
* For \(K_{2,3}\) with a pendant edge, the two bipartition classes have size three. Taking either entire class gives \(9\) or \(8\). Otherwise the degree sum is at most nine, and the common-neighbor sum at most three, giving at least nine.
* For the triangle with pendant leaves, taking \(3,2,1,0\) triangle vertices gives minima \(7,8,11,15\).
* For \(K_{2,3}\) with the internal edge, taking \(2,1,0\) vertices in the two-vertex part gives minima \(7,9,7\).

If \(R\) contains an isolated color, its degree sum is at most six and its common-neighbor sum at most three. This gives at least nine in every displayed graph with at least six edges. For the double star, the common-neighbor sum is at most one, giving at least eight.

Thus only \((2,0,0),(1,0,0),(0,0,0)\) remain.

## 5.2. The case \((2,0,0)\)

Write
\[
L_1=X\cup\{\xi\},\qquad
L_2=X\cup\{\eta\},\qquad
L_3=P,
\]
where \(|X|=2,|P|=3\), and all displayed color sets are disjoint.

By the table, (12) forces \(R=P\), \(|\mathcal F|=6\), and hence
\[
n_3=6,\qquad n_4\le2.
\]
Every forced triple contains a color from \(X\).

But each of the three sets
\[
\{\xi,\eta\}\cup T,\qquad T\in\binom P2,
\tag{15}
\]
is an attainable four-color set of the star. None contains a forced triple. Blocking all three requires three different four-element lists, contradicting \(n_4\le2\).

## 5.3. The case \((1,0,0)\)

Write
\[
L_1=\{h\}\cup U,\qquad
L_2=\{h\}\cup V,\qquad
L_3=P,
\]
where \(|U|=|V|=2, |P|=3\), and these sets are disjoint.

Now \(J\) is the star with center \(h\) and leaf set \(P\). If
\[
\varepsilon=\mathbf1_{\{h\in R\}},\qquad s=|R\cap P|,
\]
then
\[
|\mathcal F|=9-3\varepsilon-s-\binom{s}{2}.
\tag{16}
\]
The values at most six are \(6,5,3\).

### If \( |\mathcal F|=6\)

Again \(n_3=6\) and \(n_4\le2\). All forced triples contain \(h\).

There are at least three distinct attainable four-color sets avoiding \(h\):

* if \(R\) contains two colors of \(P\), use one of them on the center; varying the leaf colors already gives eight such sets;
* otherwise \(R=\{h,d,e\}\), with \(d,e\notin P\). Using \(d\) on the center gives at least six such sets, whether \(d\) lies in \(U\), in \(V\), or outside both.

The forced triples block none of these sets, and two four-element lists cannot block all of them.

### If \( |\mathcal F|=5\)

Necessarily
\[
R=\{h,p,d\},\qquad p\in P,\quad d\notin P\cup\{h\}.
\]
Coloring the center with \(h\) gives twelve attainable four-color sets
\[
\{h,u,v,q\},
\qquad u\in U,\ v\in V,\ q\in P.
\tag{17}
\]

The forced triples are two triples containing \(h\) and two colors of \(P\), and the three triples \(\{h,d,q\}\), \(q\in P\). They block at most six of the twelve sets in (17).

Each additional triple is contained in at most three sets in (17), and each four-element list blocks at most one. Hence all additional lists block at most
\[
3(n_3-5)+n_4\le20-15=5
\]
of the at least six remaining sets. This is insufficient.

### If \( |\mathcal F|=3\)

There are two possibilities.

* If \(R\) consists of \(h\) and two colors of \(P\), the twelve sets (17) contain no forced triple. Additional lists block at most
  \[
  3(n_3-3)+n_4\le11
  \]
  of them.
* If \(R=P\), consider the twelve attainable sets
  \[
  T\cup\{u,v\},
  \qquad T\in\binom P2,\ u\in U,\ v\in V.
  \tag{18}
  \]
  None contains \(h\), and thus none contains a forced triple. Each additional triple is contained in at most two of these sets, and each four-element list in at most one. Since \(n_3\ge3\), the total blocked is at most
  \[
  2(n_3-3)+n_4
  \le 3n_3+n_4-9
  \le11.
  \]

Both cases leave an extendable coloring.

## 5.4. Pairwise disjoint leaf lists

Finally suppose \(L_1,L_2,L_3\) are pairwise disjoint.

Choose the center color uniformly from \(R\), then independently choose each leaf color uniformly from its list after deleting the center color. Let \(S\) be the used-color set.

For every fixed triple \(T\),
\[
\Pr(T\subseteq S)\le\frac19.
\tag{19}
\]
Here is a verification.

* If \(T\) contains two colors from one leaf list, the center must use one of those two. The probability is at most
  \[
  2\cdot\frac13\cdot\frac12\cdot\frac13=\frac19.
  \]
* If \(T\) contains one color from each leaf list, let \(r=|T\cap R|\). Conditional on a center color in \(T\), the containment probability is \(1/9\); otherwise it is at most \(1/18\). Thus the unconditional probability is at most
  \[
  \frac r{27}+\frac{3-r}{54}\le\frac19.
  \]
* If \(T\) contains a color outside the three leaf lists, that color must be the center color, giving probability at most \(1/27\).

For every fixed four-element set \(T\),
\[
\Pr(T\subseteq S)\le\frac1{27}.
\tag{20}
\]
Indeed, if all four colors lie in the leaf-list union, their multiplicities among the three disjoint leaf lists must be \(2,1,1\); the probability is at most
\[
2\cdot\frac13\cdot\frac12\cdot\frac13\cdot\frac13=\frac1{27}.
\]
If one color lies outside the union, the probability is at most \(1/81\). Other patterns are impossible.

The union bound now gives
\[
\Pr(\text{some list on }B\text{ is contained in }S)
\le \frac{n_3}{9}+\frac{n_4}{27}
=\frac{3n_3+n_4}{27}
\le\frac{20}{27}<1.
\]
Some star coloring therefore extends. This completes all cases of the lemma. ∎

---

# 6. The exact \(4\)-choosability threshold

## Theorem 5

For \(b\ge2\),
\[
G_{3,b,2}\text{ is }4\text{-choosable}
\quad\Longleftrightarrow\quad b\le8.
\]

### Proof

It suffices to prove the positive direction for \(b=8\).

Take an arbitrary four-list assignment on \(G_{3,8,2}\), and let the clique vertices be \(z_1,z_2\). For a color \(p\), write
\[
c(p)=|\{v\in B:p\in L(v)\}|.
\]

If some color has \(c(p)\ge7\), Corollary 3 applies, since \(k=4\) and \(a=3\).

Otherwise every color satisfies \(c(p)\le6\). Choose any \(p\in L(z_1)\), color \(z_1\) with \(p\), and delete \(p\) from all remaining lists.

The remaining center \(z_2\) and the three vertices of \(A\) have lists of size at least three. On \(B\),
\[
n_3=c(p),\qquad n_4=8-c(p).
\]
Consequently
\[
n_3\le6,\qquad
3n_3+n_4=2c(p)+8\le20.
\]
Lemma 4 completes the coloring.

Thus \(G_{3,8,2}\) is four-choosable, and so are its induced subgraphs with \(b\le8\). For \(b\ge9\), Proposition 1 with \(a=3,k=4\) supplies a bad assignment. ∎

---

# 7. A \(5\)-choosability result at \(b=9\)

## Theorem 6

The graph \(G_{3,9,3}\) is five-choosable.

### Proof

Take an arbitrary five-list assignment, with clique vertices \(z_1,z_2,z_3\).

As before, let \(c(p)\) count the lists on \(B\) containing \(p\). If some \(c(p)\ge8\), Corollary 3 applies. Hence assume
\[
c(p)\le7\qquad\text{for every color }p.
\tag{21}
\]

Put
\[
P=L(z_1),\qquad Q=L(z_2),
\]
and, for distinct colors \(p,q\), let
\[
c(p,q)=|\{v\in B:p,q\in L(v)\}|.
\]

### Case 1: Some \(p\in P,q\in Q\), \(p\ne q\), satisfy \(c(p,q)\le6\)

Color \(z_1,z_2\) with \(p,q\), respectively, and delete both colors from the remaining lists.

The remaining star has lists of size at least three. On \(B\), the numbers of lists of size three and four are
\[
n_3=c(p,q),\qquad
n_4=c(p)+c(q)-2c(p,q).
\]
Therefore
\[
n_3\le6
\]
and
\[
3n_3+n_4
=c(p,q)+c(p)+c(q)
\le6+7+7=20.
\]
Lists retaining size five are harmless. Lemma 4 completes the coloring.

### Case 2: Every such pair has \(c(p,q)\ge7\)

By (21), every such pair actually has
\[
c(p,q)=c(p)=c(q)=7.
\]
Thus \(p\) and \(q\) occur in exactly the same seven lists on \(B\).

All colors in \(P\cup Q\) have the same seven-vertex support. To see this for two colors of \(P\), choose a color of \(Q\) different from both; this is possible because \(|Q|=5\). The assertion for colors of \(Q\) follows similarly.

Each of those seven \(B\)-lists contains \(P\cup Q\). Since they have size five and \(|P|=|Q|=5\), it follows that
\[
P=Q=R
\]
for a five-element set \(R\). Seven vertices of \(B\) have list \(R\), while the other two \(B\)-lists are disjoint from \(R\).

Choose \(p\in R\), and delete \(p\) from all lists on \(A\cup C\). These lists have size at least four. Color the three clique vertices greedily, then the three vertices of \(A\). This gives a proper coloring of \(A\cup C\) avoiding \(p\).

Both \(z_1\) and \(z_2\) receive colors in \(R\). Since \(A\cup C\) has six vertices, at most four colors outside \(R\) are used. Each of the two \(B\)-lists disjoint from \(R\) has five colors, so each retains an available color. The seven vertices with list \(R\) can all receive \(p\).

This completes both cases. ∎

---

# 8. Deducing the values of \(\phi(3,b)\)

For \(b=2\), the graph is \(K_{2,3}\), which is two-choosable. Indeed, if the two lists on the two-vertex side intersect, color those vertices alike. Otherwise there are four distinct possible two-color sets on that side, and three lists on the opposite side cannot block all four.

For \(3\le b\le6\), Lemma 4 with \(n_3=b,n_4=0\) shows that \(G_{3,b,1}\) is three-choosable. But \(K_{3,3}\) is not two-choosable: on each side use the lists
\[
\{1,2\},\quad\{1,3\},\quad\{2,3\}.
\]
Each side needs at least two colors, whereas the two sides must use disjoint color sets. Thus
\[
\phi(3,b)=1\qquad(3\le b\le6).
\]

For \(b=7,8\), Proposition 1 gives non-three-choosability at \(t=1\), while Theorem 5 gives four-choosability at \(t=2\). Therefore
\[
\phi(3,7)=\phi(3,8)=2.
\]

Finally, Proposition 1 gives non-four-choosability of \(G_{3,9,2}\), and Theorem 6 gives five-choosability of \(G_{3,9,3}\). Hence
\[
\phi(3,9)=3.
\]

This proves (3).

---

# 9. General bound and remaining gap

The verified obstruction also gives, for \(3\le a\le b\),
\[
\boxed{
\phi(a,b)\ge
(a-1)\left\lfloor
\sqrt{\frac{b-1}{a-1}}
\right\rfloor-1.
}
\tag{22}
\]
Indeed, put \(m=a-1\), \(r=\lfloor\sqrt{(b-1)/m}\rfloor\), and apply Proposition 1 with \(k=mr\). Then
\[
k\left\lceil\frac{k}{m}\right\rceil+1
=mr^2+1\le b.
\]
In particular,
\[
\liminf_{b\to\infty}\frac{\phi(a,b)}{\sqrt b}\ge\sqrt{a-1}
\qquad(a\ge3\text{ fixed}).
\tag{23}
\]

The results above do **not** determine \(\phi(a,b)\) in general. They establish an exact \(4\)-choosability threshold for the \(a=3\) family and one further exact value at \(t=3\). They do not provide a matching general upper bound for (22), nor do they determine \(\phi(3,10)\).