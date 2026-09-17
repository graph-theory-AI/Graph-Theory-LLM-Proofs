Attack the following open graph-theory problem.

Catalog id: list_total_colouring_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/list_total_colouring_conjecture/
Original entry: http://www.openproblemgarden.org/op/list_total_colouring_conjecture
Problem attributed to: Borodin, Oleg V., Kostochka, Alexandr V., Woodall, Douglas R. (posted 2013-08-29)

=== Problem statement (OpenProblemGarden) ===
Title: List Total Colouring Conjecture
Conjecture If $ G $ is the total graph of a multigraph, then $ \chi_\ell(G)=\chi(G) $ .

=== Discussion / context (OpenProblemGarden) ===
The list chromatic number of a graph $ G $ , denoted $ \chi_\ell(G) $ , is defined here . Given a multigraph $ H $ , the total graph $ T(H) $ of $ H $ is a graph on vertex set $ V(T(H)):=V(H)\cup E(H) $ where \item two elements of $ V(H) $ are adjacent in $ T(H) $ if and only if they are adjacent in $ H $ ; \item two elements of $ E(H) $ are adjacent in $ T(H) $ if and only if they share an endpoint; \item an element of $ V(H) $ is adjacent to an element of $ E(H) $ in $ T(H) $ if it is incident with it. This problem is related to the List (Edge) Colouring Conjecture as well as the Total Colouring Conjecture. Kostochka and Woodall [KW] conjectured that $ \chi_\ell(G^2)=\chi(G^2) $ for every graph $ G $ ; this was known as the List Square Colouring Conjecture. It is stronger than the List Total Colouring Conjecture since, given a multigraph $ H $ , the total graph of $ H $ can be obtained by subdividing each edge of $ H $ and taking the square. Moreover, the graph obtained from $ H $ by subdividing each edge is bipartite and one part of the bipartition consists of vertices of degree $ 2 $ . Thus, the List Total Colouring Conjecture corresponds to this (very) special case of the List Square Colouring Conjecture. However, the List Square Colouring Conjecture is not true in general. For a family of counterexamples, see the paper of Kim and Park [KP].

=== References listed by OpenProblemGarden ===
- *[BKW] O. V. Borodin, A. V. Kostochka, and D. R. Woodall. List edge and list totalcolourings of multigraphs. J. Combin. Theory Ser. B, 71(2):184–204, 1997.
- [KW] A. V. Kostochka and D. R. Woodall. Choosability conjectures and multicircuits. Discrete Math., 240(1-3):123–143, 2001.
- [KP] Seog-Jin Kim and Boram Park: Counterexamples to the List Square Coloring Conjecture, submitted.

=== Catalog page (statement + literature review) ===
List Total Colouring Conjecture — Graph-theory open problems

 
 Status
 open
 high confidence
 

 The List Total Colouring Conjecture — that $\chi_\ell(G)=\chi(G)$ whenever $G$ is the total graph of a multigraph — remains open. The stronger List Square Colouring Conjecture was already known to be false at the time of posting (Kim–Park 2013, cited in the problem statement itself); subsequent work by Hasanvand (2022) extended those counterexamples to bipartite planar graphs and their line graphs, but neither result bears on the LTCC. No proof or disproof of the LTCC has been identified in the post-2013 literature.

 Cited literature (2)

 
 
 
partial The List Square Coloring Conjecture fails for bipartite planar graphs and their line graphs
 (2022)
 

 
 Morteza Hasanvand · arXiv preprint · arXiv:2211.00622

Extends the failure of the List Square Colouring Conjecture (the strictly stronger conjecture) to bipartite planar graphs and their line graphs; explicitly notes the LTCC remains open and motivates revised restricted versions.
 

 
 
partial On the Alon-Tarsi Number of Some Line and Total graphs
 (2023)
 

 
 S. Prajnanaswaroopa · arXiv preprint · arXiv:2312.09951

Establishes ATN(T(G)) ≤ Δ(G)+3 for any graph G, giving a weak upper bound on the list chromatic number of total graphs; does not prove χ_ℓ(T(H))=χ(T(H)) for multigraph total graphs.
 

 

 Reviewer notes. The Kim–Park counterexamples to the List Square Colouring Conjecture (arXiv:1305.2566, submitted May 2013) predate the OPG posting and are already cited in the problem statement, so they are not counted as post-posting results. The Hasanvand (2022) paper is directly about the LSCC (not LTCC) but is included as it is the most relevant post-2013 development in the surrounding area. The Prajnanaswaroopa (2023) paper provides a bound Δ+3 on the Alon-Tarsi number of total graphs, which is weaker than what would be needed for the LTCC. No special-case proof of the LTCC for specific multigraph families was found in the post-2013 search.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. If $ G $ is the total graph of a multigraph, then $ \chi_\ell(G)=\chi(G) $ .

Keywords:
list coloring · Total coloring · total graphs

Discussion

The list chromatic number of a graph $ G $ , denoted $ \chi_\ell(G) $ , is defined here . Given a multigraph $ H $ , the total graph $ T(H) $ of $ H $ is a graph on vertex set $ V(T(H)):=V(H)\cup E(H) $ where \item two elements of $ V(H) $ are adjacent in $ T(H) $ if and only if they are adjacent in $ H $ ; \item two elements of $ E(H) $ are adjacent in $ T(H) $ if and only if they share an endpoint; \item an element of $ V(H) $ is adjacent to an element of $ E(H) $ in $ T(H) $ if it is incident with it. This problem is related to the List (Edge) Colouring Conjecture as well as the Total Colouring Conjecture. Kostochka and Woodall [KW] conjectured that $ \chi_\ell(G^2)=\chi(G^2) $ for every graph $ G $ ; this was known as the List Square Colouring Conjecture. It is stronger than the List Total Colouring Conjecture since, given a multigraph $ H $ , the total graph of $ H $ can be obtained by subdividing each edge of $ H $ and taking the square. Moreover, the graph obtained from $ H $ by subdividing each edge is bipartite and one part of the bipartition consists of vertices of degree $ 2 $ . Thus, the List Total Colouring Conjecture corresponds to this (very) special case of the List Square Colouring Conjecture. However, the List Square Colouring Conjecture is not true in general. For a family of counterexamples, see the paper of Kim and Park [KP].

Bibliography

★ [BKW]
 O. V. Borodin, A. V. Kostochka, and D. R. Woodall. List edge and list totalcolourings of multigraphs. J. Combin. Theory Ser. B, 71(2):184–204, 1997.

 [KW]
 A. V. Kostochka and D. R. Woodall. Choosability conjectures and multicircuits. Discrete Math., 240(1-3):123–143, 2001.

 [KP]
 Seog-Jin Kim and Boram Park: Counterexamples to the List Square Coloring Conjecture, submitted.

Related conjectures

 
 related to
 Choosability of Graph Powers
 open
 The source page explicitly says these questions 'are also related to the so-called List Total Colouring Conjecture'. Both descend from the disproved List Square Colouring Conjecture ch(G^2)=chi(G^2): LTCC is its special case on squares of subdivisions (total graphs), Noel's question is a weakened o(k^2)-bound version for all graphs. No implication either way: a positive answer to Noel's question allows a superlinear gap, far weaker than the exact equality LTCC demands on total graphs; and LTCC, restricted to total graphs, cannot bound ch(G^2) for general G. Explicitly stated relatedness, no derivable implication: related_only.
 

 
 related to
 Total Colouring Conjecture
 partial
 Both conjectures concern the same object, since chi''(H) = chi(T(H)). But they assert logically independent things: LTCC says the list chromatic number of a total graph equals its chromatic number (choosability = colorability), while TCC bounds that chromatic number by Delta(H)+2. Truth of LTCC gives no bound on chi(T(H)), and truth of TCC says nothing about list colorings, so neither implies the other. The OPG context itself only says the problem 'is related to ... the Total Colouring Conjecture'. (Note: their conjunction would give chi_ell(T(H)) <= Delta+2, but separately no implication holds.)
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds, with an exact formula, for multigraphs obtained by gluing simple cycles and parallel-edge bundles at cut vertices.",
  "would_publish": false,
  "caveats": "This is a restricted special case, with no novelty claim; the general conjecture remains unresolved here."
}
```

## 1. Statement of the partial result

I use the standard convention that multigraphs are finite and loopless. All degrees count multiplicities.

Let \(\mathcal C\) consist of multigraphs obtained from the following pieces by disjoint unions and identifications at single vertices:

- isolated vertices;
- simple cycles \(C_r\), \(r\ge 3\);
- two vertices joined by \(m\ge 1\) parallel edges.

Equivalently, the underlying simple graph is a cactus, and an edge belonging to a cycle of that simple graph has multiplicity one. Parallel edges are allowed on its bridges.

For \(H\in\mathcal C\) with at least one edge, put
\[
\mu(H)=\max_{uv\in E(H)}\mu(uv)
\]
and
\[
b(H)=
\begin{cases}
4,&\text{if \(H\) has a simple cycle block \(C_r\) with \(3\nmid r\)},\\
0,&\text{otherwise}.
\end{cases}
\]

**Theorem.** For every \(H\in\mathcal C\) with at least one edge,
\[
\boxed{\quad
\chi_\ell(T(H))=\chi(T(H))
=\max\{\Delta(H)+1,\ \mu(H)+2,\ b(H)\}.
\quad}
\]
For a nonempty edgeless graph, both parameters equal \(1\).

The proof is self-contained. It also supplies reducible end blocks for a minimal-counterexample approach to the general conjecture. I make no claim that this special case is new.

## 2. Lower bounds

For each vertex \(v\), the vertex \(v\) together with all incident edges forms a clique in \(T(H)\). Hence
\[
\chi(T(H))\ge d_H(v)+1.
\]

If \(u,v\) are joined by \(m\) parallel edges, those edges together with \(u,v\) form a clique of order \(m+2\). Thus
\[
\chi(T(H))\ge \mu(H)+2.
\]

Finally,
\[
T(C_r)\cong C_{2r}^{\,2}.
\]
A proper \(3\)-coloring of this square must repeat with period three: every three consecutive vertices form a triangle. Consequently it exists only if \(3\mid 2r\), equivalently \(3\mid r\).

The total graph of a cycle block is an induced subgraph of \(T(H)\). Therefore a cycle block whose length is not divisible by three gives the lower bound \(4\).

Together these prove the asserted lower bound.

## 3. Two elementary list-coloring lemmas

### Lemma 1: squares of paths with degree-sized lists

If \(n\ge 4\), then \(P_n^2\) is colorable from any lists satisfying
\[
|L(x)|\ge d_{P_n^2}(x).
\]

**Proof.** First consider the diamond \(D=K_4-e\). Let its nonadjacent vertices be \(a,d\), with lists of size two, and its other vertices be \(b,c\), with lists of size three. Trimming larger lists causes no problem.

If \(L(a)\cap L(d)\ne\varnothing\), give \(a,d\) a common color. Each of \(b,c\) retains at least two colors, so they can receive distinct colors.

Suppose instead that \(L(a),L(d)\) are disjoint.

- If \(|L(b)\cup L(c)|\ge4\), choose arbitrary colors for \(a,d\). Afterwards each of \(b,c\) has at least one available color, and their available lists have union of size at least two. They can therefore be colored distinctly.
- Otherwise \(L(b)=L(c)=S\), where \(|S|=3\). Since \(L(a)\cup L(d)\) has size four, one of \(a,d\) can receive a color outside \(S\). Color it that way and color the other arbitrarily. At most one color of \(S\) has been used, leaving two colors for \(b,c\).

Thus the diamond is colorable from degree-sized lists.

Now label the vertices of \(P_n\) as \(x_1,\ldots,x_n\). The first four vertices induce a diamond in \(P_n^2\). Color
\[
x_n,x_{n-1},\ldots,x_5
\]
in that order. Every vertex being colored has an uncolored neighbor, so a list of size at least its degree always leaves a color available. The remaining lists on the diamond have sizes at least its internal degrees, and the preceding argument finishes the coloring. \(\square\)

### Lemma 2: a triangle-end-block extension

Let \(F\) have vertices \(x,y,u,w,e\), where

- \(x,u,w,y\) induce a \(4\)-cycle in that order;
- \(e\) is adjacent to all four.

Then \(F\) is colorable whenever
\[
|L(x)|,|L(y)|\ge2,\qquad
|L(u)|,|L(w)|\ge3,\qquad
|L(e)|\ge4.
\]

**Proof.** Trim the lists to these sizes, and write them as \(A,B,U,W,Q\), respectively. Choose distinct
\[
a\in A,\qquad b\in B
\]
for \(x,y\).

The remaining graph is the triangle \(u,w,e\), with lists
\[
U\setminus\{a\},\qquad
W\setminus\{b\},\qquad
Q\setminus\{a,b\},
\]
each of size at least two. Such a triangle is uncolorable only if all three lists are the same two-element set \(S\), by Hall’s condition. In that event,
\[
U=S\cup\{a\},\qquad
W=S\cup\{b\},\qquad
Q=S\cup\{a,b\}.
\]

If \(A\) contains \(a'\notin\{a,b\}\), change the color of \(x\) to \(a'\).

- If \(a'\notin Q\), then \(Q\setminus\{a',b\}\) has size three.
- If \(a'\in S\), then \(Q\setminus\{a',b\}\) contains \(a\), whereas \(W\setminus\{b\}=S\) does not.

In either case, the three residual lists have union of size at least three and satisfy Hall’s condition. The same argument applies if \(B\) contains a color outside \(\{a,b\}\).

The only remaining case is \(A=B=\{a,b\}\). Swap the colors of \(x,y\). Now \(U\setminus\{b\}=U\) has size three, so again the remaining triangle is colorable. \(\square\)

## 4. Extending over end blocks with at least four colors

We prove the following upper bound:
\[
\chi_\ell(T(H))
\le
\max\{4,\Delta(H)+1,\mu(H)+2\}
\qquad(H\in\mathcal C,\ E(H)\ne\varnothing).
\tag{1}
\]

More precisely, fix \(k\ge4\) such that
\[
k\ge\Delta(H)+1,\qquad k\ge\mu(H)+2,
\]
and give every vertex and edge of \(H\) a list of at least \(k\) colors.

It suffices to consider connected \(H\). Induct on its number of blocks. Choose an end block \(B\), with attachment vertex \(v\); if \(H\) has only one block, choose any vertex of it as \(v\). Delete the other vertices of \(B\) and its edges, and color the remaining multigraph inductively.

### Case A: a parallel-edge bundle

Suppose \(B\) consists of \(m\) edges between \(v\) and a new vertex \(u\). There are
\[
t=d_H(v)-m
\]
already colored edges at \(v\).

Each new edge loses at most \(t+1\) colors: those used on \(v\) and its already colored incident edges. Thus each retains at least
\[
k-(t+1)
=k-d_H(v)+m-1
\ge m
\]
colors. The \(m\) new edges can receive pairwise distinct colors.

The vertex \(u\) then has at most \(m+1\) forbidden colors, so it can be colored because \(k\ge m+2\).

### Case B: a simple cycle

Write the cycle as
\[
v,v_1,\ldots,v_{r-1},v,
\]
and let
\[
x=vv_1,\qquad y=vv_{r-1}.
\]
There are \(t=d_H(v)-2\) already colored edges at \(v\). Each of \(x,y\) consequently retains at least
\[
k-(t+1)=k-d_H(v)+1\ge2
\]
colors.

If \(r=3\), the five uncolored elements form exactly the graph of Lemma 2:

- \(x,y\) have lists of size at least two;
- \(v_1,v_2\) lose only the color of \(v\), and retain at least three;
- \(v_1v_2\) retains at least four.

So the coloring extends.

Suppose \(r\ge4\). Choose distinct colors for \(x,y\). The remaining elements, in the order
\[
v_1,\ v_1v_2,\ v_2,\ldots,
v_{r-2}v_{r-1},\ v_{r-1},
\]
induce \(P_{2r-3}^2\).

Their residual list sizes are at least
\[
2,\ 3,\ 4,\ldots,4,\ 3,\ 2.
\]
Indeed, the two end vertices lose at most the colors of \(v\) and their incident boundary edge; the two end-adjacent edge-elements lose at most one boundary-edge color; all other elements lose none.

These are exactly the degree requirements in Lemma 1. Hence the coloring extends.

This completes the induction and proves (1).

## 5. The three-color case

The only gap between (1) and the theorem occurs when the asserted answer is three.

Then \(\mu(H)=1\) and \(\Delta(H)\le2\). Thus every component is a path, an isolated vertex, or a simple cycle whose length is divisible by three.

Total graphs of paths are \(3\)-choosable: color the alternating vertex-edge sequence along the path, so that each element has at most two previously colored neighbors.

For completeness, here is a direct proof for the relevant cycles.

### Lemma 3: \(C_N^2\) is \(3\)-choosable when \(3\mid N\) and \(N\ge6\)

Use indices modulo \(N\), and set
\[
P(x_0,\ldots,x_{N-1})
=
\prod_{i=0}^{N-1}
(x_i-x_{i+1})(x_i-x_{i+2}).
\]
Its factors correspond exactly to the edges of \(C_N^2\), with a chosen orientation.

We will show
\[
[x_0^2x_1^2\cdots x_{N-1}^2]P=6.
\tag{2}
\]

We use the following elementary coefficient identity. If \(S_i\) is any three-element set of complex numbers, then, for any polynomial of total degree at most \(2N\),
\[
[x_0^2\cdots x_{N-1}^2]P
=
\sum_{a\in\prod_iS_i}
\frac{P(a)}
{\displaystyle
 \prod_i\prod_{b\in S_i\setminus\{a_i\}}(a_i-b)}.
\tag{3}
\]
This follows from univariate Lagrange interpolation applied to monomials: the corresponding functional annihilates degrees zero and one and takes value one on degree two. If a monomial of total degree at most \(2N\) has an exponent exceeding two, another exponent is less than two, so that monomial is annihilated.

To compute the coefficient, take every \(S_i\) to be
\[
R=\{1,\omega,\omega^2\},\qquad \omega^3=1,\quad\omega\ne1.
\]
Only proper \(3\)-colorings of \(C_N^2\) contribute. There are exactly six, all periodic with period three.

For every such assignment, \(a_{i+1},a_{i+2}\) are the two elements of \(R\setminus\{a_i\}\). Therefore
\[
(a_i-a_{i+1})(a_i-a_{i+2})
=
\prod_{b\in R\setminus\{a_i\}}(a_i-b).
\]
Every nonzero summand in (3) is consequently \(1\), proving (2).

Now take arbitrary three-element color lists and inject their finite union into \(\mathbb C\). If there were no proper list coloring, \(P\) would vanish on the entire product of the lists. Identity (3) would then make the coefficient in (2) zero, a contradiction. \(\square\)

For a cycle \(C_r\) with \(3\mid r\), we have
\[
T(C_r)\cong C_{2r}^2,
\]
so Lemma 3 applies.

Thus the asserted upper bound also holds when it equals three. Together with the lower bounds, this proves the theorem.

## 6. A consequence for a minimal counterexample

The extension arguments above do **not** require the already colored remainder to belong to \(\mathcal C\).

Consequently, if a counterexample to the full conjecture exists and \(H\) is chosen minimizing
\[
|V(H)|+|E(H)|,
\]
then:

1. \(H\) is connected.
2. \(\chi(T(H))\ge4\).
3. No end block of \(H\) is a simple cycle or a two-vertex parallel-edge bundle.

For item 2, a total chromatic number at most three forces \(H\) to be simple with maximum degree at most two; the preceding path and cycle arguments settle all those cases.

For item 3, put \(k=\chi(T(H))\), remove such an end block, and use minimality to color the remainder from its \(k\)-lists. The inequalities
\[
k\ge\Delta(H)+1,\qquad k\ge\mu(H)+2
\]
are automatic clique bounds. Section 4 then extends the coloring, contradicting the choice of \(H\).

Thus these end blocks are genuinely reducible in a minimal-counterexample attack.

## 7. Where the argument stops

The restriction on parallel edges in cycle blocks is important to this **proof method**. The analogous extension statement already fails for a triangle having one doubled edge.

Take vertices \(v,u,w\), with edges
\[
x=vu,\qquad y=vw,
\]
and two parallel edges \(p,q\) between \(u,w\). Also attach an external edge at \(v\).

Prescribe color \(6\) on \(v\) and color \(7\) on that external edge. Give the uncolored elements the following four-element lists:
\[
\begin{array}{c|c}
\text{element}&\text{list}\\ \hline
x&\{1,2,6,7\}\\
y&\{3,4,6,7\}\\
u&\{1,2,5,6\}\\
w&\{3,4,5,6\}\\
p,q&\{1,2,3,4\}.
\end{array}
\]

Any extension must color \(x\) from \(\{1,2\}\) and \(y\) from \(\{3,4\}\). The four edges \(x,y,p,q\) form a clique, so they use all four colors \(1,2,3,4\).

Both colors \(1,2\) then occur on edges incident with \(u\), forcing \(u\) to receive color \(5\). Similarly, \(w\) is forced to receive color \(5\). Since \(u,w\) are adjacent, extension is impossible.

**This is not a counterexample to the List Total Colouring Conjecture:** the boundary colors were prescribed, rather than forced by a complete list assignment. It shows only that the end-block extension proof cannot be carried over mechanically to multicycles.

The general conjecture—including multigraphs with such blocks and general \(2\)-connected cores—is not settled by this argument.
