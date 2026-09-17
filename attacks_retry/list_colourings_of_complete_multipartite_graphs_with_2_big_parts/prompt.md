Attack the following open graph-theory problem.

Catalog id: list_colourings_of_complete_multipartite_graphs_with_2_big_parts
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/list_colourings_of_complete_multipartite_graphs_with_2_big_parts/
Original entry: http://www.openproblemgarden.org/op/list_colourings_of_complete_multipartite_graphs_with_2_big_parts
Problem attributed to: Allagan, Julian (posted 2014-04-12)

=== Problem statement (OpenProblemGarden) ===
Title: List Colourings of Complete Multipartite Graphs with 2 Big Parts
Question Given $ a,b\geq2 $ , what is the smallest integer $ t\geq0 $ such that $ \chi_\ell(K_{a,b}+K_t)= \chi(K_{a,b}+K_t) $ ?

=== Discussion / context (OpenProblemGarden) ===
The list chromatic number of a graph $ G $ , denoted $ \chi_\ell(G) $ , is the minimum $ k $ such that for every assignment of lists of size $ k $ to the vertices of $ G $ there is a proper colouring in which every vertex is mapped to a colour in its own list. For more background on the list chromatic number, see [3]. Given graphs $ G $ and $ H $ , the join of $ G $ and $ H $ , denoted $ G+H $ , is obtained by taking disjoint copies of $ G $ and $ H $ and adding all edges between them. Ohba [1] proved that for every graph $ G $ there exists $ t\geq0 $ such that $ \chi_\ell(G+K_t)= \chi(G+K_t) $ . The question above asks to determine the minimum value of $ t $ in the case that $ G $ is a complete bipartite graph. It seems that it was first studied in [4], although this is unclear; for the time being, we have chosen to attribute this problem to J. Allagan. Define $ \phi(a,b) $ to be the minimum $ t $ such that $ \chi_\ell(K_{a,b}+K_t)= \chi(K_{a,b}+K_t) $ . Note that, if $ G $ is a complete multipartite graph with at most one non-singleton part, then we see that $ \chi_\ell(G)=\chi(G) $ by colouring the vertices of the non-singleton part last. Thus, if $ a $ or $ b $ is equal to 1, then $ \phi(a,b)=0 $ . As it turns out, $ \phi(2,2)=\phi(2,3)=0 $ and $ \phi(3,3)=\phi(2,4)=1 $ . This can be deduced from the following result of [2] and the fact that $ \chi_\ell(K_{3,3})=\chi_\ell(K_{4,2})=3 $ : Theorem (Noel, Reed, Wu (2012)) If $ |V(G)|\leq 2\chi(G)+1 $ , then $ \chi_\ell(G)=\chi(G) $ . The above result of [2] implies that if $ a+b\geq 5 $ , then $ \phi(a,b)\leq a+b-5 $ . However it seems that, for most values of $ a,b $ , this bound is far from tight. A simple observation is that, since $ \chi_\ell(K_{a,b}+K_t)\geq \chi_\ell(K_{a,b}) $ for all $ t $ , we must have \[\phi(a,b)\geq \chi_\ell(K_{a,b}) - \chi(K_{a,b}) = \chi_\ell(K_{a,b}) -2.\] The following is a result of Allagan [4]: Theorem (Allagan (2009)) If $ a\geq5 $ , then \[\lfloor \sqrt{a}\rfloor - 1 \leq \phi(a,2)\leq \left\lceil\frac{-7+\sqrt{8a+17}}{2}\right\rceil.\] This implies that $ \phi(a,2)=1 $ for $ 4\leq a\leq 8 $ and that $ \phi(a,2)=2 $ for $ 9\leq a\leq 13 $ .

=== References listed by OpenProblemGarden ===
- [1] K. Ohba. On chromatic-choosable graphs, J. Graph Theory. 40 (2002) 130--135. MathSciNet.
- [2] J. A. Noel, B. A. Reed, H. Wu. A Proof of a Conjecture of Ohba. Submitted. pdf.
- [3] J. A. Noel. Choosability of Graphs with Bounded Order: Ohba's Conjecture and Beyond. Master's Thesis, McGill University. pdf.
- [4] J. A. D. Allagan. Choice Numbers, Ohba Numbers and Hall Numbers of some complete -partite graphs. PhD Thesis. Auburn University. 2009.

=== Catalog page (statement + literature review) ===
List Colourings of Complete Multipartite Graphs with 2 Big Parts — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The case $a = 2$ (equivalently $b = 2$) of the problem has been fully resolved: Cano, Gutknecht, Kappaganthula, Miller, Mudrock, and Thornburgh (2024) proved that $\tau_0(2,b) = \lfloor\sqrt{b}\rfloor - 1$ for all $b \geq 2$, improving Allagan's 2009 bounds and confirming his conjectured lower bound as exact. For general $a, b \geq 2$ the exact value of $\phi(a,b)$ remains open, with only the asymptotic lower bound $\tau_0(a,b) = \Omega(\sqrt{b})$ as $b\to\infty$ established.

 Cited literature (1)

 
 
 
partial On the Ohba Number and Generalized Ohba Numbers of Complete Bipartite Graphs
 (2024)
 

 
 Kennedy Cano, Emily Gutknecht, Gautham Kappaganthula, George Miller, Jeffrey A. Mudrock, Ezekiel Thornburgh · arXiv preprint · arXiv:2403.06291

Proves $\tau_0(2,b) = \lfloor\sqrt{b}\rfloor - 1$ for all $b\geq 2$ (settling the $K_{2,b}$ case of the problem exactly) and shows $\tau_0(a,b)=\Omega(\sqrt{b})$ for general $a\geq 2$.
 

 

 Reviewer notes. The 2024 paper uses the notation tau_0(a,b) for the same quantity as the OPG's phi(a,b). The paper had a latest revision dated February 2026 and may be under journal review. The Noel-Reed-Wu paper (reference [2] in OPG) was published in J. Graph Theory in 2015 (DOI 10.1002/jgt.21819), confirming Ohba's conjecture, but the journal page returned HTTP 403 so it was not verifiable via WebFetch. No paper was found that fully determines phi(a,b) for all a,b >= 2.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Question. Given $ a,b\geq2 $ , what is the smallest integer $ t\geq0 $ such that $ \chi_\ell(K_{a,b}+K_t)= \chi(K_{a,b}+K_t) $ ?

Keywords:
complete bipartite graph · complete multipartite graph · list coloring

Discussion

The list chromatic number of a graph $ G $ , denoted $ \chi_\ell(G) $ , is the minimum $ k $ such that for every assignment of lists of size $ k $ to the vertices of $ G $ there is a proper colouring in which every vertex is mapped to a colour in its own list. For more background on the list chromatic number, see [3]. Given graphs $ G $ and $ H $ , the join of $ G $ and $ H $ , denoted $ G+H $ , is obtained by taking disjoint copies of $ G $ and $ H $ and adding all edges between them. Ohba [1] proved that for every graph $ G $ there exists $ t\geq0 $ such that $ \chi_\ell(G+K_t)= \chi(G+K_t) $ . The question above asks to determine the minimum value of $ t $ in the case that $ G $ is a complete bipartite graph. It seems that it was first studied in [4], although this is unclear; for the time being, we have chosen to attribute this problem to J. Allagan. Define $ \phi(a,b) $ to be the minimum $ t $ such that $ \chi_\ell(K_{a,b}+K_t)= \chi(K_{a,b}+K_t) $ . Note that, if $ G $ is a complete multipartite graph with at most one non-singleton part, then we see that $ \chi_\ell(G)=\chi(G) $ by colouring the vertices of the non-singleton part last. Thus, if $ a $ or $ b $ is equal to 1, then $ \phi(a,b)=0 $ . As it turns out, $ \phi(2,2)=\phi(2,3)=0 $ and $ \phi(3,3)=\phi(2,4)=1 $ . This can be deduced from the following result of [2] and the fact that $ \chi_\ell(K_{3,3})=\chi_\ell(K_{4,2})=3 $ : Theorem (Noel, Reed, Wu (2012)) If $ |V(G)|\leq 2\chi(G)+1 $ , then $ \chi_\ell(G)=\chi(G) $ . The above result of [2] implies that if $ a+b\geq 5 $ , then $ \phi(a,b)\leq a+b-5 $ . However it seems that, for most values of $ a,b $ , this bound is far from tight. A simple observation is that, since $ \chi_\ell(K_{a,b}+K_t)\geq \chi_\ell(K_{a,b}) $ for all $ t $ , we must have \[\phi(a,b)\geq \chi_\ell(K_{a,b}) - \chi(K_{a,b}) = \chi_\ell(K_{a,b}) -2.\] The following is a result of Allagan [4]: Theorem (Allagan (2009)) If $ a\geq5 $ , then \[\lfloor \sqrt{a}\rfloor - 1 \leq \phi(a,2)\leq \left\lceil\frac{-7+\sqrt{8a+17}}{2}\right\rceil.\] This implies that $ \phi(a,2)=1 $ for $ 4\leq a\leq 8 $ and that $ \phi(a,2)=2 $ for $ 9\leq a\leq 13 $ .

Bibliography

 [1]
 K. Ohba. On chromatic-choosable graphs, J. Graph Theory. 40 (2002) 130--135. MathSciNet .
 MathSciNet

 [2]
 J. A. Noel, B. A. Reed, H. Wu. A Proof of a Conjecture of Ohba. Submitted. pdf .
 pdf

 [3]
 J. A. Noel. Choosability of Graphs with Bounded Order: Ohba's Conjecture and Beyond. Master's Thesis, McGill University. pdf .
 pdf

 [4]
 J. A. D. Allagan. Choice Numbers, Ohba Numbers and Hall Numbers of some complete $ k $ -partite graphs. PhD Thesis. Auburn University. 2009.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I characterize all pairs with phi(a,b) at most 1 and give an explicit general square-root lower bound, but do not determine phi for general pairs.",
  "would_publish": false,
  "caveats": "Novelty relative to existing work is unverified; no matching general upper bound is established."
}
```

## 1. Results obtained

Write
\[
\alpha=\min(a,b),\qquad \beta=\max(a,b).
\]
I prove the following partial determination:
\[
\boxed{
\begin{aligned}
\phi(a,b)=0
&\iff \alpha=2,\ \beta\le 3,\\
\phi(a,b)=1
&\iff
\begin{cases}
\alpha=2,\ 4\le\beta\le8,\quad\text{or}\\
\alpha=3,\ 3\le\beta\le6.
\end{cases}
\end{aligned}}
\tag{1}
\]
Thus the substantive small-parameter assertion is
\[
\boxed{K_{3,b}+K_1\text{ is }3\text{-choosable if and only if }b\le6.}
\tag{2}
\]

I also give the following general obstruction.

**Theorem A.** Let \(a\ge3\) and \(k\ge2\). If
\[
b\ge k\left\lceil\frac{k}{a-1}\right\rceil+1,
\tag{3}
\]
then \(K_{a,b}+K_{k-2}\) is not \(k\)-choosable. Consequently,
\[
\phi(a,b)\ge k-1.
\]

In particular, for \(3\le a\le b\),
\[
\boxed{\displaystyle
\phi(a,b)\ge
(a-1)\left\lfloor\sqrt{\frac{b-1}{a-1}}\right\rfloor-1.}
\tag{4}
\]
Hence, for every fixed \(a\ge3\),
\[
\liminf_{b\to\infty}\frac{\phi(a,b)}{\sqrt b}\ge\sqrt{a-1}.
\tag{5}
\]

Everything below is self-contained. I do **not** assert that these partial results are new; I have not independently checked their novelty against the cited preprint.

---

## 2. Two elementary observations

First, if \(H\) is \(r\)-choosable, then \(H+K_1\) is \((r+1)\)-choosable: color the new universal vertex arbitrarily and delete its color from all remaining lists.

Thus chromatic-choosability, once attained along
\[
K_{a,b},\ K_{a,b}+K_1,\ K_{a,b}+K_2,\ldots,
\]
persists. In particular, non-\(k\)-choosability at \(t=k-2\) implies \(\phi(a,b)\ge k-1\).

Second, let \(A,B\) be the two independent parts and let \(C\) be the joined clique. After properly coloring \(A\cup C\), with set \(S\) of used colors, the coloring extends to \(B\) precisely when
\[
L(v)\nsubseteq S\qquad\text{for every }v\in B.
\tag{6}
\]
This is because the vertices of \(B\) are mutually nonadjacent and are adjacent to every vertex of \(A\cup C\).

---

## 3. A general bad-list construction

Set
\[
m=a-1,\qquad s=\left\lceil\frac{k}{m}\right\rceil.
\]
Take disjoint color sets \(P,Q\) with
\[
|P|=k,\qquad |Q|=s.
\]
Choose \(s\)-element subsets
\[
D_1,\ldots,D_m\subseteq P,
\qquad
D_1\cup\cdots\cup D_m=P.
\]
Such subsets exist because \(ms\ge k\) and \(s\le k\): distribute the elements of \(P\) among \(m\) sets of capacity \(s\), then pad each set to size \(s\).

Let \(A=\{u_0,u_1,\ldots,u_m\}\). Assign
\[
L(u_0)=P,\qquad
L(u_i)=(P\setminus D_i)\cup Q\quad(1\le i\le m).
\]
Give each of the \(k-2\) clique vertices the list \(P\).

In \(B\), use one vertex \(v_0\) with list \(P\), and one vertex \(v_{p,q}\) for every \((p,q)\in P\times Q\), with
\[
L(v_{p,q})=(P\setminus\{p\})\cup\{q\}.
\]
There are \(1+ks\) vertices in \(B\), and all lists have size \(k\).

Suppose a proper list coloring existed. The clique vertices and \(u_0\) use \(k-1\) distinct colors from \(P\). Write this set as \(P\setminus\{p\}\), and let \(y\) be the color on \(u_0\).

Choose \(i\) with \(y\in D_i\). Vertex \(u_i\) cannot use \(y\), and it cannot use any clique color. Its color must therefore be either \(p\) or some \(q\in Q\).

* If it uses \(p\), every color of \(L(v_0)=P\) is used on neighbors of \(v_0\).
* If it uses \(q\in Q\), every color of
  \[
  L(v_{p,q})=(P\setminus\{p\})\cup\{q\}
  \]
  is used on neighbors of \(v_{p,q}\).

Both alternatives are impossible. This proves Theorem A. Extra vertices in \(B\) cannot repair the obstruction.

### The \(a=2\) variant

When \(a=2\), take \(D_1=P\) and \(|Q|=k\). Then \(u_1\) must use a color of \(Q\), so \(v_0\) is unnecessary. This gives
\[
K_{2,k^2}+K_{k-2}\text{ is not }k\text{-choosable}.
\tag{7}
\]

For \(k=3\), these constructions give the three obstructions
\[
K_{2,9}+K_1,\qquad K_{3,7}+K_1,\qquad K_{4,4}+K_1.
\tag{8}
\]
It remains to prove the corresponding positive assertions.

---

## 4. The upper bound for \(K_{3,6}+K_1\)

Let \(z\) be the universal vertex, with list \(R\), and let the three vertices of \(A\) have lists \(L_1,L_2,L_3\). All lists have size three.

We prove that at least seven three-element lists on \(B\) are required to prevent every coloring of the star induced by \(A\cup\{z\}\).

If
\[
L_1\cap L_2\cap L_3\ne\varnothing,
\]
color all three vertices of \(A\) alike and color \(z\) differently. Only two colors are used, so every three-element list on \(B\) retains an available color. We may therefore assume the triple intersection is empty.

### 4.1. Forced lists arising from three-colorings of the star

Define a graph \(H\) on the colors by declaring \(uv\in E(H)\) exactly when
\[
\{u,v\}\cap L_i\ne\varnothing\qquad(i=1,2,3).
\]
Thus an edge of \(H\) is a two-color transversal of the three leaf lists.

Let
\[
\mathcal F=
\bigl\{\{c,u,v\}:c\in R,\ uv\in E(H),\ c\notin\{u,v\}\bigr\}.
\tag{9}
\]
Every member of \(\mathcal F\) is the exact used-color set of a proper coloring of the star: color \(z\) with \(c\) and the leaves using \(u,v\).

Consequently, in an uncolorable assignment, **every member of \(\mathcal F\) must occur as a list on \(B\)**. Otherwise the corresponding star coloring extends by (6).

Here is a useful exact count:
\[
|\mathcal F|
=
3e(H)-\sum_{c\in R}d_H(c)
-\sum_{\{c,d\}\subseteq R}|N_H(c)\cap N_H(d)|
+\mathbf1_{\{R\text{ induces a triangle in }H\}}.
\tag{10}
\]
Indeed, the family obtained by fixing \(c\in R\) has size \(e(H)-d_H(c)\); intersections of two such families are counted by common neighbors, and the three-way intersection exists exactly when \(R\) is a triangle.

Put
\[
x=|L_1\cap L_2|,\quad
y=|L_1\cap L_3|,\quad
w=|L_2\cap L_3|.
\]
Relabeling the leaves allows \(x\ge y\ge w\). Since the triple intersection is empty,
\[
x+y,\ x+w,\ y+w\le3.
\]
The only possibilities are
\[
(0,0,0),(1,0,0),(2,0,0),(3,0,0),
(1,1,0),(2,1,0),(1,1,1),(2,1,1).
\tag{11}
\]

For six of these possibilities, formula (10) gives the following table. Only the non-isolated part of \(H\) is displayed.

| \((x,y,w)\) | Non-isolated part of \(H\) | Minimum \( |\mathcal F| \) |
|---|---|---:|
| \((3,0,0)\) | \(K_{3,3}\) | \(9\) |
| \((2,0,0)\) | \(K_{2,3}\) | \(6\) |
| \((1,1,0)\) | An edge with two pendant leaves at each endpoint | \(7\) |
| \((2,1,0)\) | \(K_{2,3}\), with a pendant edge added at a vertex in the three-vertex part | \(8\) |
| \((1,1,1)\) | A triangle with one pendant leaf at each vertex | \(7\) |
| \((2,1,1)\) | \(K_{2,3}\), with an edge added inside the three-vertex part | \(7\) |

For completeness, the finite checks underlying the table are as follows.

* For \(K_{3,3}\), distributing \(R\) between its parts as \(3+0\) or \(2+1\) gives \(9\) or \(15\).
* For \(K_{2,3}\), taking respectively \(0,1,2\) vertices of \(R\) in its two-vertex part gives \(6,9,7\).
* For the double star, taking \(2,1,0\) centers in \(R\) gives respectively \(7\), either \(7\) or \(9\), and \(11\).
* For \(K_{2,3}\) with the pendant edge, the bipartition has two parts of size three. Taking \(R\) to be one whole part gives \(9\) or \(8\). Otherwise the degree sum is at most \(9\), and only the two vertices in the same part can have common neighbors, at most three; (10) gives at least \(9\).
* For the triangle with pendant leaves, taking \(3,2,1,0\) triangle vertices gives minima \(7,8,11,15\).
* For \(K_{2,3}\) with the added internal edge, taking \(2,1,0\) vertices from the two-vertex part gives minima \(7,9,7\).

These checks also cover arbitrary additional isolated colors: if \(R\) contains an isolated vertex, its degree sum is at most \(6\), and the common-neighbor sum is at most \(3\). This gives at least \(9\) in every displayed graph with at least six edges. For the double star, the common-neighbor sum is at most one, giving at least \(8\).

Thus all displayed cases except \((2,0,0)\) already require at least seven lists on \(B\).

### 4.2. The exceptional \((2,0,0)\) case

Write
\[
L_1=X\cup\{u\},\qquad
L_2=X\cup\{v\},\qquad
L_3=P,
\]
where \(|X|=2\), \(|P|=3\), and the displayed sets and individual colors are mutually disjoint.

The table shows that \(|\mathcal F|=6\) is possible only when \(R=P\). Every member of \(\mathcal F\) then contains a color from \(X\).

But the star can be colored using \(u,v\) and two distinct colors of \(P\), with no color from \(X\). None of the six forced lists blocks that coloring. A seventh list is necessary.

### 4.3. The \((1,0,0)\) case

Write
\[
L_1=\{h\}\cup U,\qquad
L_2=\{h\}\cup V,\qquad
L_3=P,
\]
where \(|U|=|V|=2\), \(|P|=3\), and all these color sets are disjoint. Here \(H\) is the star with center \(h\) and leaf set \(P\).

Let
\[
\varepsilon=\mathbf1_{\{h\in R\}},\qquad s=|R\cap P|.
\]
Formula (10) becomes
\[
|\mathcal F|=9-3\varepsilon-s-\binom{s}{2}.
\tag{12}
\]
When this is at most six, its possible values are \(6,5,3\).

**If \(|\mathcal F|=6\):** all six forced triples contain \(h\). The star has a proper coloring avoiding \(h\): delete \(h\) from its lists, leaving lists of size at least two, and color its center first. That coloring requires an additional blocking list.

**If \(|\mathcal F|=5\):** necessarily
\[
R=\{h,p,d\},\qquad p\in P,\quad d\notin P\cup\{h\}.
\]
Coloring the center with \(h\) produces the twelve distinct attainable used-color sets
\[
\{h,u,v,q\},\qquad u\in U,\ v\in V,\ q\in P.
\tag{13}
\]
The five forced triples comprise two triples containing \(h\) and two colors of \(P\), and the three triples \(\{h,d,q\}\), \(q\in P\). They block at most six sets in (13). Any additional triple is contained in at most three sets in (13). Thus at least two further lists are needed, for at least seven altogether.

**If \(|\mathcal F|=3\):** there are two possibilities.

* If \(R\) consists of \(h\) and two colors of \(P\), use the twelve sets (13). None contains a forced triple, and each further triple blocks at most three of them. At least four additional lists are needed.
* If \(R=P\), use the twelve attainable sets
  \[
  T\cup\{u,v\},
  \qquad T\in\binom P2,\ u\in U,\ v\in V.
  \]
  None contains \(h\), so none contains a forced triple. Each additional triple is contained in at most two of these sets, again requiring more than three additional lists.

In every subcase, six lists on \(B\) are insufficient.

### 4.4. The \((0,0,0)\) case

Now \(L_1,L_2,L_3\) are pairwise disjoint.

Choose the center color uniformly from \(R\), and then independently choose each leaf color uniformly from its list after deleting the center color. This always produces a proper star coloring.

For any fixed three-element color set \(T\),
\[
\Pr(T\subseteq S)\le\frac19,
\tag{14}
\]
where \(S\) is the resulting used-color set. To verify this, distinguish the following possibilities.

* If \(T\) contains two colors from one leaf list, the center must use one of those two colors. For each such center choice, the relevant leaf uses the other with probability \(1/2\), and a second relevant leaf uses the third color with probability \(1/3\). The total is at most
  \[
  2\cdot\frac13\cdot\frac12\cdot\frac13=\frac19.
  \]
  Three colors from one leaf list cannot all occur.
* If \(T\) contains one color from each leaf list, put \(r=|T\cap R|\). Conditional on a center color in \(T\), its containment probability is \(1/9\); otherwise it is at most \(1/18\). Thus
  \[
  \Pr(T\subseteq S)
  \le \frac r{27}+\frac{3-r}{54}
  =\frac{r+3}{54}\le\frac19.
  \]
* If \(T\) contains a color outside all three leaf lists, that color must be the center color. The probability is at most \(1/27\), or zero if containment is impossible.

For at most six lists on \(B\), the union bound gives probability at most \(6/9<1\) that any is contained in \(S\). Hence some star coloring extends.

This completes the proof that \(K_{3,6}+K_1\) is \(3\)-choosable. Together with (8), it proves (2).

---

## 5. Completing the classification for \(\phi\le1\)

### The \(K_{2,b}+K_1\) case

If the two three-element lists on \(A\) intersect, color both vertices alike and the center differently; only two colors are used.

Otherwise the two leaf lists are disjoint three-element sets. Their two-color transversal graph is \(K_{3,3}\). The first row of the preceding table shows that there are at least nine distinct attainable three-color sets on the star. To block all of them requires at least nine lists on \(B\).

Therefore
\[
K_{2,b}+K_1\text{ is }3\text{-choosable}\iff b\le8,
\]
the reverse implication being supplied by (7).

For \(\alpha\ge4\), the graph contains \(K_{4,4}+K_1\), which is not \(3\)-choosable by (8). This exhausts the possibilities at \(t=1\).

### The \(t=0\) case

For \(K_{2,b}\), intersecting two-element lists on the two-vertex side can be colored alike. If they are disjoint, there are four distinct possible two-color sets on that side. At most three lists on the other side cannot block all four. Thus \(K_{2,b}\) is \(2\)-choosable for \(b\le3\), whereas \(K_{2,4}\) is not, by (7) with \(k=2\).

Also, \(K_{3,3}\) is not \(2\)-choosable: on each side assign the three lists
\[
\{1,2\},\quad\{1,3\},\quad\{2,3\}.
\]
Each side needs at least two colors, and the two sides must use disjoint color sets.

Combining these facts with persistence under adjoining universal vertices proves (1).

---

## 6. Consequences of the general construction

Assume \(3\le a\le b\), set \(m=a-1\), and put
\[
r=\left\lfloor\sqrt{\frac{b-1}{m}}\right\rfloor.
\]
Then \(r\ge1\). Taking \(k=mr\) in Theorem A gives
\[
k\left\lceil\frac{k}{a-1}\right\rceil+1
=mr^2+1\le b,
\]
and hence
\[
\phi(a,b)\ge mr-1.
\]
This proves (4) and (5).

Two particular consequences are
\[
\phi(a,a)\ge a-2\qquad(a\ge3)
\]
and
\[
\phi(3,9)\ge3.
\]
The latter follows from an explicit bad \(4\)-list assignment on \(K_{3,9}+K_2\), not merely from the list chromatic number of its bipartite subgraph.

## 7. What remains unresolved here

The construction supplies **non-choosability**, not a matching general choosability theorem. Except for the complete analysis at \(t\le1\), there is no justification for treating its obstruction threshold as exact.

For example, combining (4) with the Ohba bound supplied in the question gives
\[
(a-1)\left\lfloor\sqrt{\frac{b-1}{a-1}}\right\rfloor-1
\le \phi(a,b)\le a+b-5
\qquad(3\le a\le b),
\]
which still leaves a substantial gap. Thus this is a rigorous partial determination, not a solution of the general minimum-\(t\) problem.
