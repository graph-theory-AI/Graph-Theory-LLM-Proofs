```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove 7-choosability when at most three vertices have degree at least eight in the K_{4,4}-minor-free case, or at most four in the K_{3,5}-minor-free case.",
  "would_publish": false,
  "caveats": "Neither unrestricted question is resolved; novelty of these restricted results has not been checked."
}
```

# A bounded-high-degree partial result

All graphs below are finite and simple.

## Theorem

1. Every \(K_{4,4}\)-minor-free graph with at most **three** vertices of degree at least \(8\) is \(7\)-choosable.
2. Every \(K_{3,5}\)-minor-free graph with at most **four** vertices of degree at least \(8\) is \(7\)-choosable.

Consequently, a vertex-minimal counterexample to the first question must have at least four vertices of degree at least \(8\), and one to the second must have at least five.

The same sufficient conditions can be checked separately in each component of the graph’s \(7\)-core, with degrees measured inside that core.

These are restricted results, not resolutions of either conjecture. The proof follows.

---

## 1. Critical graphs and their degree-seven vertices

The only external coloring input is the classical **degree-choosability theorem**:

> A connected graph is colorable from every list assignment satisfying  
> \[
> |L(v)|\ge d(v)
> \]
> unless every block is a complete graph or an odd cycle.

A connected graph whose blocks are complete graphs or odd cycles is called a **Gallai tree**.

Suppose one of the assertions of the theorem fails. Fix lists of size exactly seven and pass to a vertex-minimal induced subgraph \(G\) that is not colorable from those lists. The forbidden-minor condition and the bound on the number of vertices of degree at least eight are preserved.

Every vertex of \(G\) has degree at least seven: otherwise, color its deletion and extend greedily. Put
\[
A=\{v:d_G(v)\ge8\},\qquad B=\{v:d_G(v)=7\},\qquad a=|A|,
\]
and write \(F=G[B]\).

Every component of \(F\) is a Gallai tree. Indeed, color the vertices outside such a component \(T\). The residual list at \(v\in V(T)\) has size at least
\[
7-\bigl(d_G(v)-d_T(v)\bigr)=d_T(v).
\]
If \(T\) were not a Gallai tree, the degree-choosability theorem would extend the coloring.

### Endblocks

Call a block of \(F\) an endblock if it has at most one cutvertex in its component. A component consisting of one block contributes one endblock.

For an endblock \(C\), let \(U(C)\) be its vertices that are not cutvertices of its component. Thus:

- if \(C\) is a proper endblock, \(U(C)\) omits its unique cutvertex;
- if its component is just \(C\), then \(U(C)=V(C)\).

Throughout the proof \(a\le4\), so
\[
d_F(v)\ge 7-a\ge3.
\]
An endblock therefore cannot be an odd cycle or a clique of order at most three. Also, neither forbidden-minor class contains \(K_8\). Hence every endblock is a clique
\[
C\cong K_b,\qquad 8-a\le b\le7.
\]
For \(u\in U(C)\),
\[
|N_G(u)\cap A|=8-b. \tag{1}
\]

Define its support by
\[
S(C)=N_G(U(C))\cap A.
\]
Because \(U(C)\) is a clique, for every nonempty \(T\subseteq S(C)\), the set
\[
U(C)\cup T
\]
is connected. It can thus be contracted to connect the selected high-degree vertices. Moreover, if \(C,D\) are distinct endblocks, then \(U(D)\cap V(C)=\varnothing\).

### There are at least two endblocks

First, \(B\ne\varnothing\), since otherwise \(G\) would have at most four vertices and minimum degree at least seven.

If \(F\) had only one endblock, it would be a single clique \(K_b\). Set \(r=8-b\). Equation (1) gives
\[
e(A,B)=br,\qquad 1\le r\le a\le4.
\]
Every vertex of \(A\) has at most \(a-1\) neighbors in \(A\), so
\[
e(A,B)\ge a(9-a).
\]
Since \(x(9-x)\) is increasing on \([0,4]\),
\[
a(9-a)\ge r(9-r)=br+r>br,
\]
a contradiction. Thus \(F\) has at least two endblocks.

---

## 2. Two elementary minor certificates

We will repeatedly use the following explicit observations.

### Certificate I: a \(7\)-clique and one branch set

Let \(Q\cong K_7\), and let \(X\) be a connected set disjoint from \(Q\).

- If \(X\) has at least four neighbors in \(Q\), then \(Q\cup X\) contains a \(K_{4,4}\)-minor.
- If it has at least three neighbors in \(Q\), then \(Q\cup X\) contains a \(K_{3,5}\)-minor.

Contract \(X\). For the first assertion, put four neighbors on one side and the remaining three clique vertices together with \(X\) on the other. For the second, use three neighbors against the remaining four clique vertices and \(X\).

### Certificate II: a \(6\)-clique and two branch sets

Let \(Q\cong K_6\), and let \(X,Y\) be disjoint connected sets outside \(Q\).

- Four common neighbors of \(X,Y\) in \(Q\) give a \(K_{4,4}\)-minor.
- Three common neighbors give a \(K_{3,5}\)-minor.

After contracting \(X,Y\), put the common neighbors on one side and all remaining vertices on the other. No edge between \(X\) and \(Y\) is required.

---

## 3. The \(K_{4,4}\)-minor-free case

Assume \(a\le3\).

By (1), every endblock has order \(5,6,\) or \(7\).

### Endblocks of order five

Such an endblock has at least four vertices in \(U(C)\), each adjacent to all three vertices of \(A\). Four of these vertices, against the remaining clique vertex and the three high-degree vertices, give a \(K_{4,4}\) subgraph.

Thus no endblock has order five.

### Endblocks of order six

Here \(|U(C)|\ge5\), and each vertex of \(U(C)\) has two neighbors in \(A\).

Its support must have size three. Otherwise two high-degree vertices have at least five common neighbors in the \(6\)-clique, contradicting Certificate II.

Furthermore,
\[
e(U(C),A)=2|U(C)|\ge10,
\]
so some \(z\in A\) has at least four neighbors in \(U(C)\).

### Endblocks of order seven

Here every vertex of \(U(C)\) has exactly one neighbor in \(A\). Certificate I implies that each high-degree vertex has at most three neighbors in the entire \(7\)-clique.

Thus \(|S(C)|\) is two or three. If it is two, then necessarily:

- \(C\) is a proper endblock;
- \(|U(C)|=6\);
- each of its two support vertices has exactly three neighbors in \(U(C)\).

### A full-support endblock is impossible

Suppose some endblock has support of size three. There is another endblock, and the possibilities are:

- **Two \(6\)-cliques.** In the first, choose \(z\in A\) with at least four neighbors in its interior. Use the interior of the second to connect the other two high-degree vertices, avoiding \(z\). Every interior vertex of the first has a neighbor among those two. Certificate II gives a \(K_{4,4}\)-minor.
- **A \(6\)-clique and a \(7\)-clique.** The \(6\)-clique has full support, so its interior connects all support vertices of the \(7\)-clique. The resulting branch set has at least six neighbors in that \(7\)-clique. Apply Certificate I.
- **Two \(7\)-cliques, at least one with full support.** Use the full-support clique’s interior to connect all support vertices of the other. Again apply Certificate I.

Therefore every endblock is a proper \(7\)-clique supported on a pair of high-degree vertices, with three interior neighbors at each endpoint.

Two endblocks cannot have the same support pair: one would connect the pair outside the other, giving Certificate I.

Nor can there be three distinct support pairs. Since \(|A|\le3\), these would be
\[
\{x,y\},\quad \{x,z\},\quad \{y,z\}.
\]
Outside the first endblock, the other two connect \(x\) to \(y\) through \(z\), again giving Certificate I.

Hence \(F\) has exactly two endblocks, with distinct support pairs
\[
S(C)=\{x,y\},\qquad S(D)=\{x,z\}.
\]
Both are proper, so \(F\) is connected.

Let \(c\) be the cutvertex of \(C\). It has six neighbors in \(C\), and \(d_G(c)=7\). Since it is a cutvertex of \(F\), it has exactly one neighbor in \(B\setminus V(C)\) and no neighbor in \(A\). Consequently,
\[
F-V(C)
\]
is connected.

The vertex \(y\) has exactly three neighbors in \(C\), and at most two in \(A\). Since \(d_G(y)\ge8\), it has a neighbor in \(B\setminus V(C)\). This connected graph also contains a neighbor of \(x\) in \(U(D)\). Thus \(x\) and \(y\) are connected outside \(C\).

Contracting such a connection gives a branch set adjacent to all six vertices of \(U(C)\), contradicting Certificate I.

This proves part 1.

---

## 4. The \(K_{3,5}\)-minor-free case

Now assume \(a\le4\).

### Possible endblocks and supports

An endblock has order between four and seven.

**Order four is impossible.** At least three interior vertices are adjacent to all four high-degree vertices. Those three vertices are adjacent to the other five vertices of \(C\cup A\), giving a \(K_{3,5}\) subgraph.

For the remaining orders, (1) and the minor certificates give:

| Order of \(C\) | Neighbors in \(A\) of each \(u\in U(C)\) | Consequences |
|---|---:|---|
| \(5\) | \(3\) | \(|S(C)|=4\) |
| \(6\) | \(2\) | \(|S(C)|\ge3\); each pair of high vertices has at most two common neighbors in \(U(C)\) |
| \(7\) | \(1\) | \(|S(C)|\ge3\); each high vertex has at most two neighbors in \(C\) |

Here are the details needed later.

For a \(5\)-clique, support of size three would mean that three interior vertices are adjacent to all three support vertices. Together with the other two clique vertices this is a \(K_{3,5}\). Thus the support has size four.

For a \(6\)-clique, three common neighbors of a pair of high-degree vertices are forbidden by Certificate II. Since \(|U(C)|\ge5\), the support therefore has size at least three. Moreover:

- some support vertex has at least three neighbors in \(U(C)\);
- if the support has size three, **every** support vertex has at least three neighbors in \(U(C)\).

For the second claim, a support vertex can be missed only by vertices adjacent to the other support pair, and there are at most two such vertices.

The assertion for a \(7\)-clique follows directly from Certificate I.

### Elimination of \(7\)-clique endblocks

Suppose \(C\cong K_7\), and choose another endblock \(D\). Its support has size at least three.

Contract the connected set
\[
U(D)\cup S(D).
\]
At most one vertex of \(A\) lies outside \(S(D)\), and that vertex has at most two neighbors in \(C\). The contracted set therefore has at least
\[
|U(C)|-2\ge4
\]
neighbors in \(C\), contradicting Certificate I.

### Elimination of \(6\)-clique endblocks

Suppose an endblock has order six, and choose another endblock. The other has order five or six.

First suppose at least one of their supports has size four. We can choose a \(6\)-clique \(C\) as the target and another endblock \(D\) with support \(A\) as connector; if necessary, interchange two \(6\)-cliques.

Choose \(z\in A\) having at least three neighbors in \(U(C)\). Contract
\[
U(D)\cup(A\setminus\{z\})
\]
to a branch set \(X\). Every vertex of \(U(C)\) has two neighbors in \(A\), so every such vertex is adjacent to \(X\). Thus \(z\) and \(X\) have at least three common neighbors in \(C\), contradicting Certificate II.

It remains that both endblocks are \(6\)-cliques with supports of size three.

- If their supports are the same set \(S\), choose \(z\in S\) and contract the other two support vertices together with the other endblock’s interior. This branch set and \(z\) have at least three common neighbors in the target clique.
- If the supports differ, choose
  \[
  z\in S(C)\setminus S(D).
  \]
  Contract \(U(D)\cup S(D)\). Every vertex of \(U(C)\) has a neighbor in this branch set, and \(z\) has at least three neighbors in \(U(C)\).

Certificate II applies in both cases.

Therefore **every endblock is a \(5\)-clique**, and \(a=4\).

### The only remaining endblock pattern

Write
\[
A=\{a_1,a_2,a_3,a_4\}.
\]
Every interior vertex of a \(5\)-clique endblock is adjacent to exactly three vertices of \(A\); call its unique nonneighbor in \(A\) its *missing label*.

Suppose an endblock \(C\) has three interior vertices whose missing labels lie in a set of at most two high-degree vertices. Choose a two-element set \(P\subseteq A\) containing those labels, and choose another endblock \(D\).

Contract
\[
U(D)\cup P
\]
to one branch set. Keep the other two high-degree vertices as singleton branch sets. The selected three vertices of \(U(C)\) are adjacent to all three outside branch sets. Together with the other two vertices of \(C\), this gives a \(K_{3,5}\)-minor.

Thus this pattern is impossible.

If \(|U(C)|=5\), the pigeonhole principle gives three vertices whose missing labels use at most two labels. The same holds when \(|U(C)|=4\) and some label repeats. Consequently every endblock is proper and has exactly four interior vertices, with the four missing labels all different.

We finish by excluding this rigid pattern.

### Two rigid endblocks force a minor

Choose two endblocks \(C,D\) in the same component of \(F\); this is possible because every endblock is proper. Write
\[
U(C)=\{u_1,u_2,u_3,u_4\},\qquad
U(D)=\{v_1,v_2,v_3,v_4\},
\]
where \(u_i\) and \(v_i\) both miss exactly \(a_i\). Let \(c,d\) be the respective cutvertices.

Initially form four connected branch sets
\[
T_1=\{a_1,v_2\},\quad
T_2=\{a_2,v_3\},\quad
T_3=\{a_3,v_4\},\quad
T_4=\{a_4,v_1\}.
\]
Each is connected, and they are pairwise adjacent because the \(v_i\) form a clique.

Choose a \(c\)-\(d\) path in \(F\) avoiding \(U(C)\cup U(D)\), and adjoin all its vertices except \(c\) to \(T_1\). This preserves disjointness and connectivity, and makes \(c\) adjacent to \(T_1\). If \(c=d\), the adjacency already follows from \(cv_2\).

After contracting the \(T_i\), we have:

- the clique \(C=\{c,u_1,u_2,u_3,u_4\}\);
- a clique on \(T_1,T_2,T_3,T_4\);
- all edges \(u_iT_j\) with \(i\ne j\);
- the edge \(cT_1\).

Contract \(cu_1\) to a vertex \(w\). The resulting eight-vertex graph contains \(K_8\) with at most the three independent edges
\[
u_2T_2,\qquad u_3T_3,\qquad u_4T_4
\]
missing.

It contains a \(K_{3,5}\) subgraph with parts
\[
\{w,u_2,T_2\}
\quad\text{and}\quad
\{T_1,u_3,T_3,u_4,T_4\}.
\]
This is the final contradiction, proving part 2.

---

## 5. The \(7\)-core extension and the remaining gap

The \(7\)-core is obtained by repeatedly deleting vertices of current degree at most six. If each component of the resulting core satisfies the corresponding high-degree bound in the theorem, color those components from their seven-element lists. Restore deleted vertices in reverse order; each has at most six already colored neighbors, so the coloring extends.

Thus the partial result applies more generally when, inside each \(7\)-core component, there are at most

- three vertices of degree at least eight in the \(K_{4,4}\)-minor-free case;
- four in the \(K_{3,5}\)-minor-free case.

The unrestricted questions remain unresolved by this argument. In a minimal obstruction with more high-degree vertices, the supports of low-degree endblocks can be larger and need not overlap in the ways used above. No bound on that number has been established here, and the numerical thresholds in the theorem are not claimed to be sharp.