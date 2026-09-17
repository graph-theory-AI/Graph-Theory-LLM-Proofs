```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain a degree-(μ+1) polynomial bound for globally bounded induced matching number, improve the bounded-color case, and obtain polynomial-in-t bag guards giving a general bound with an additional log |V(G)| factor.",
  "would_publish": false,
  "caveats": "The uniform, n-independent polynomial bound remains unproved; no claim of literature novelty is made."
}
```

# 1. Conventions and results obtained

Graphs are finite and simple. As in the supplied abstract, \(K_{t,t}\)-free means **induced-\(K_{t,t}\)-free**. The case \(t=1\) is trivial, so assume \(t\ge 2\).

For \(X\subseteq V(G)\), write
\[
\mu_G(X)=\max\{|M|:M\text{ is an induced matching in }G
\text{ and every edge of }M\text{ meets }X\}.
\]
Write \(\operatorname{im}(G)\) for the global induced matching number.

Define
\[
\sigma_\mu(s)=\sum_{j=0}^{\mu}\binom{s}{j},
\]
where \(\binom{s}{j}=0\) for \(j>s\), and put
\[
b_\mu(t)=
\begin{cases}
2t-2,&\mu=1,\\[2mm]
\mu t+(t-1)\sigma_\mu(\mu t),&\mu\ge2.
\end{cases}
\]
Thus
\[
b_\mu(t)=O_\mu(t^{\mu+1}).
\]
Also put
\[
g_\mu(t)
=(\mu+2)b_\mu(t)
 +(t^\mu-1)\sigma_\mu\!\bigl(\mu b_\mu(t)\bigr).
\]
This is a polynomial in \(t\), with
\[
g_\mu(t)=O_\mu(t^{\mu^2+2\mu}).
\]
For \(\mu=1\), the explicit expression is better:
\[
g_1(t)=2t^2+3t-5.
\]

Here are the proved partial results.

### Theorem A

Let \(G\) be induced-\(K_{t,t}\)-free with
\(\operatorname{tree\text{-}\mu}(G)\le\mu\).

1. **Deleting a maximum independent set.** For every maximum independent set \(I\) of \(G\),
   \[
   \operatorname{tree\text{-}\alpha}(G-I)\le b_\mu(t).
   \]

2. **Globally bounded induced matching number.** If, additionally,
   \(\operatorname{im}(G)\le\mu\), then
   \[
   \operatorname{tree\text{-}\alpha}(G)\le b_\mu(t)+1.
   \]
   In particular, for \(2K_2\)-free graphs,
   \[
   \operatorname{tree\text{-}\alpha}(G)\le 2t-1.
   \]

3. **Bounded chromatic number.** If \(G\) is \(r\)-colorable, then
   \[
   \operatorname{tw}(G)\le r(r-1)b_\mu(t),
   \]
   and consequently
   \[
   \operatorname{tree\text{-}\alpha}(G)
   \le 1+r(r-1)b_\mu(t).
   \]

4. **A bound for the full class, with logarithmic dependence on order.** If \(n=|V(G)|\ge1\), then
   \[
   \operatorname{tree\text{-}\alpha}(G)
   \le 1+g_\mu(t)\lfloor\log_2 n\rfloor.
   \]

The main structural ingredient behind the fourth conclusion is the following local statement, which does not assume that \(X\) is a bag.

### Theorem B: polynomial-independence incident-edge covers

If \(G\) is induced-\(K_{t,t}\)-free and \(X\subseteq V(G)\) satisfies
\(\mu_G(X)\le\mu\), then there is \(C\subseteq V(G)\) such that

- \(C\) meets every edge having an endpoint in \(X\); and
- \(\alpha(G[C])\le g_\mu(t)\).

In particular, every bag of a tree-\(\mu\) decomposition has such a cover. These covers address the local-cover obstacle identified in the supplied attempt. They do **not**, by themselves, satisfy the running-intersection condition needed to replace the bags.

The bipartite argument below replaces the repeated VC-rectangle recursion in that attempt and improves its polynomial degree to \(\mu+1\).

# 2. A stronger bipartite matching bound

## 2.1. Two elementary neighborhood facts

Let \(H=(A,B;E)\) be bipartite with \(\operatorname{im}(H)\le\mu\).

**Fact 1: unions of neighborhoods have breadth at most \(\mu\).**  
For every \(A'\subseteq A\), there is \(D\subseteq A'\), with \(|D|\le\mu\), such that
\[
N_H(D)=N_H(A').
\]

Indeed, choose an inclusion-minimal subfamily of the neighborhoods of vertices of \(A'\) whose union is \(N_H(A')\). For each selected vertex \(a_i\), minimality supplies a private neighbor \(b_i\), adjacent to \(a_i\) and to no other selected vertex. The edges \(a_i b_i\) form an induced matching. Thus at most \(\mu\) vertices were selected. The same assertion holds with the two sides reversed.

**Fact 2: both neighborhood set systems have VC dimension at most \(\mu\).**  
If, for example, \(a_1,\dots,a_{\mu+1}\) were shattered by neighborhoods of vertices in \(B\), choose \(b_i\) whose trace on these vertices is exactly \(\{a_i\}\). Again, the edges \(a_i b_i\) would form an induced matching.

We use the elementary Sauer bound: a set system of VC dimension at most \(\mu\) on an \(s\)-element ground set has at most \(\sigma_\mu(s)\) distinct members. For completeness, its induction uses
\[
|\mathcal F|
=|\mathcal F_0\cup\mathcal F_1|
 +|\mathcal F_0\cap\mathcal F_1|,
\]
after deleting one ground-set element. The first family has VC dimension at most \(\mu\), and the second at most \(\mu-1\), giving the binomial recurrence.

## 2.2. Polynomial vertex cover lemma

### Lemma 2.1

If \(H=(A,B;E)\) is bipartite, has no \(K_{t,t}\), and
\(\operatorname{im}(H)\le\mu\), then \(H\) has a vertex cover of size at most \(b_\mu(t)\). In particular,
\[
\nu(H)\le b_\mu(t).
\]

### Proof

First prove the bound
\[
\mu t+(t-1)\sigma_\mu(\mu t),
\]
valid for every \(\mu\ge1\).

Starting with \(A\), perform \(t\) rounds. In each round, select at most \(\mu\) remaining vertices whose neighborhoods cover the neighborhoods of all remaining vertices, using Fact 1, and then remove the selected vertices. Empty selections are allowed.

Let \(S\) be the union of the selected vertices. Thus \(|S|\le\mu t\). Let
\[
B_*=\{b\in B:N_H(b)\cap(A\setminus S)\ne\varnothing\}.
\]
Every \(b\in B_*\) has a neighbor among the vertices selected in each round. Therefore
\[
|N_H(b)\cap S|\ge t.
\]

By Fact 2 and the Sauer bound, there are at most
\(\sigma_\mu(|S|)\) different traces \(N_H(b)\cap S\). Any trace of size at least \(t\) occurs for at most \(t-1\) vertices of \(B_*\), since \(t\) occurrences would give a \(K_{t,t}\). Hence
\[
|B_*|\le (t-1)\sigma_\mu(\mu t).
\]
Now \(S\cup B_*\) is a vertex cover: every edge whose \(A\)-endpoint is outside \(S\) has its \(B\)-endpoint in \(B_*\).

For \(\mu=1\), the neighborhoods of vertices in \(A\) are linearly ordered by inclusion; two incomparable neighborhoods would give an induced \(2K_2\). There are at most \(t-1\) vertices of \(A\) of degree at least \(t\), since \(t\) such vertices would have at least \(t\) common neighbors. The union of the neighborhoods of all remaining vertices has size at most \(t-1\), by nesting. These two sets form a vertex cover of size at most \(2t-2\). \(\square\)

This lemma is considerably stronger quantitatively than the matching bound in the previous attempt.

# 3. Independent transversals and polynomial bag guards

## 3.1. An independent-transversal lemma

### Lemma 3.1

Let \(G\) be induced-\(K_{t,t}\)-free. If
\[
Z_1,\dots,Z_r
\]
are pairwise disjoint independent sets, each of size at least \(t^{r-1}\), then there are pairwise nonadjacent vertices \(z_i\in Z_i\).

### Proof

Induct on \(r\); the case \(r=1\) is immediate. Truncate each part to size \(t^{r-1}\), and put \(L=t^{r-2}\).

For \(j\ge2\), call \(v\in Z_1\) bad for \(j\) if \(v\) has fewer than \(L\) nonneighbors in \(Z_j\). There are at most \(t-1\) vertices bad for \(j\). Otherwise, \(t\) bad vertices would have at least
\[
t^{r-1}-t(L-1)=t
\]
common neighbors in \(Z_j\), giving an induced \(K_{t,t}\).

Since
\[
t^{r-1}\ge 1+(r-1)(t-1),
\]
some \(z_1\in Z_1\) is bad for no \(j\). Its nonneighbors in each \(Z_j\) contain an independent set of size \(L\). Apply induction to those \(r-1\) sets. \(\square\)

The important point is that \(r\) will be \(\mu+1\), so the required part size is polynomial in \(t\).

## 3.2. A cover when one side is independent

### Lemma 3.2

Let \(I\) be an independent set in an induced-\(K_{t,t}\)-free graph \(G\), and suppose \(\mu_G(I)\le\mu\). Write \(b=b_\mu(t)\). There is a set \(C\) covering every edge incident with \(I\) such that
\[
\alpha(G[C])
\le
(\mu+1)b+(t^\mu-1)\sigma_\mu(\mu b).
\]

### Proof

Put \(R=V(G)\setminus I\). For \(v\in R\), its **trace** is
\[
S_v=N_G(v)\cap I.
\]

### High-degree vertices

Let
\[
R_{\mathrm{high}}=\{v\in R:|S_v|\ge b+1\}.
\]
Then
\[
\alpha(G[R_{\mathrm{high}}])\le b.
\]
Indeed, an independent set \(J\subseteq R_{\mathrm{high}}\) of size \(b+1\) has a matching into \(I\) saturating \(J\), by a greedy choice of distinct neighbors. But \(G[I\cup J]\) is bipartite, induced-\(K_{t,t}\)-free, and every one of its induced matchings meets \(I\). Lemma 2.1 forbids such a matching.

All remaining vertices have traces of size at most \(b\).

### Heavy trace classes

Set \(h=t^\mu\). A trace \(S\) of a vertex in \(R\setminus R_{\mathrm{high}}\) is called **heavy** if
\[
\alpha\bigl(G[\{v\in R\setminus R_{\mathrm{high}}:S_v=S\}]\bigr)\ge h.
\]

The union of all heavy traces is the union of at most \(\mu\) of them.

To prove this, suppose an inclusion-minimal family of heavy traces with the same union has more than \(\mu\) members. Choose \(\mu+1\) of them, \(S_1,\dots,S_{\mu+1}\), and private elements
\[
x_i\in S_i\setminus\bigcup_{j\ne i}S_j.
\]
For each \(i\), choose an independent set of size \(h\) from the trace class of \(S_i\). These sets are disjoint. Lemma 3.1 gives independent representatives \(y_1,\dots,y_{\mu+1}\). Then
\[
\{x_i y_i:1\le i\le\mu+1\}
\]
is an induced matching: the \(x_i\) are independent, the \(y_i\) are independent, and the private-element condition gives exactly the prescribed cross edges. This contradicts \(\mu_G(I)\le\mu\).

Let \(I_0\) be the union of all heavy traces. Consequently,
\[
|I_0|\le\mu b.
\]

### The remaining light traces

Let
\[
R_{\mathrm{light}}
=\{v\in R\setminus R_{\mathrm{high}}:S_v\not\subseteq I_0\}.
\]
Every trace represented here is nonheavy.

Take any independent set \(J\subseteq R_{\mathrm{light}}\). In the bipartite graph \(G[I\cup J]\), Fact 1 shows that
\[
U:=\bigcup_{v\in J}S_v
\]
is the union of at most \(\mu\) traces. Therefore \(|U|\le\mu b\). By Fact 2 and the Sauer bound, at most \(\sigma_\mu(\mu b)\) distinct traces occur in \(J\). Each occurs at most \(h-1\) times, since it is nonheavy. Hence
\[
|J|\le(h-1)\sigma_\mu(\mu b).
\]

Finally, take
\[
C=I_0\cup R_{\mathrm{high}}\cup R_{\mathrm{light}}.
\]
If an edge \(iv\), with \(i\in I\), is not covered by \(I_0\), then \(i\notin I_0\), so \(S_v\not\subseteq I_0\); thus \(v\) lies in one of the other two parts of \(C\). Therefore \(C\) covers all edges incident with \(I\). The three preceding bounds give the claimed independence bound. \(\square\)

## 3.3. From an independent set to an arbitrary bag

We use the following elementary exchange observation.

### Lemma 3.3

If \(I\) is a maximum independent set of a graph \(F\), then every independent set \(J\subseteq V(F)\setminus I\) has a matching into \(I\) saturating \(J\).

### Proof

For every \(J'\subseteq J\),
\[
|N_F(J')\cap I|\ge |J'|;
\]
otherwise replacing \(N_F(J')\cap I\) by \(J'\) would enlarge \(I\). Hall’s theorem applies. \(\square\)

### Proof of Theorem B

Choose a maximum independent set \(I\) of \(G[X]\). I claim that
\[
\alpha(G[X\setminus I])\le b_\mu(t).
\]
For any independent \(J\subseteq X\setminus I\), Lemma 3.3 gives a matching into \(I\) saturating \(J\). The induced bipartite graph on \(I\cup J\) has induced matching number at most \(\mu\), since all its edges meet \(X\). Lemma 2.1 therefore gives \(|J|\le b_\mu(t)\).

Apply Lemma 3.2 to \(I\), obtaining a cover \(C_I\) of all edges incident with \(I\). Then
\[
C_X=(X\setminus I)\cup C_I
\]
covers every edge incident with \(X\). By subadditivity of independence number under unions,
\[
\begin{aligned}
\alpha(G[C_X])
&\le b_\mu(t)+\alpha(G[C_I])\\
&\le(\mu+2)b_\mu(t)
 +(t^\mu-1)\sigma_\mu\!\bigl(\mu b_\mu(t)\bigr)\\
&=g_\mu(t).
\end{aligned}
\]
This proves Theorem B. \(\square\)

# 4. Consequences for tree decompositions

## 4.1. Polynomial-independence balanced separators

### Lemma 4.1

Every induced-\(K_{t,t}\)-free graph \(G\) with
\(\operatorname{tree\text{-}\mu}(G)\le\mu\) and \(n\ge2\) has a set \(C\) with
\[
\alpha(G[C])\le g_\mu(t)
\]
such that every component of \(G-C\) has at most \(n/2\) vertices.

### Proof

Take a witnessing tree decomposition. Assign each graph vertex to one bag containing it, and choose a centroid node \(x\) of the resulting vertex weights on the decomposition tree. Then every component of \(G-B_x\) has at most \(n/2\) vertices.

Use Theorem B to obtain a cover \(C\) of all edges incident with \(B_x\), with \(\alpha(G[C])\le g_\mu(t)\).

Every vertex of \(B_x\setminus C\) is isolated in \(G-C\), because all its incident edges meet \(C\). Every other component of \(G-C\) is contained in a component of \(G-B_x\). Thus all components have at most \(n/2\) vertices. \(\square\)

Both induced biclique exclusion and the bound on tree-\(\mu\) are inherited by induced subgraphs. Recursively apply Lemma 4.1. At each step, add the separator to every bag of the decompositions recursively constructed for the components.

This is a valid tree decomposition: the separator appears throughout the decompositions attached below it, edges to the separator are covered, and different components have no edges between them. Along any root-to-leaf recursion chain, at most \(\lfloor\log_2 n\rfloor\) separators occur before reaching a one-vertex graph. Consequently,
\[
\operatorname{tree\text{-}\alpha}(G)
\le 1+g_\mu(t)\lfloor\log_2 n\rfloor.
\]
This proves Theorem A(4).

## 4.2. Deleting a maximum independent set

Let \(I\) be a maximum independent set of \(G\), and let \((T,\{B_x\})\) witness tree-\(\mu\) at most \(\mu\).

Fix a bag \(B_x\) and an independent set
\[
J\subseteq B_x\setminus I.
\]
Lemma 3.3 gives a matching from \(J\) into \(I\) saturating \(J\). In the induced bipartite graph \(G[I\cup J]\), every edge meets \(J\subseteq B_x\), so its induced matching number is at most \(\mu\). Lemma 2.1 gives
\[
|J|\le b_\mu(t).
\]

Thus the restricted decomposition
\[
(T,\{B_x\setminus I\})
\]
of \(G-I\) has bag independence number at most \(b_\mu(t)\). This proves Theorem A(1).

Notice that the matching partners in \(I\) need not belong to the bag. The definition of \(\mu_G(B_x)\), which counts matchings merely touching the bag, is exactly what makes this argument work.

## 4.3. Globally bounded induced matching number

Suppose \(\operatorname{im}(G)\le\mu\), and choose a maximum independent set \(I\). For every independent \(J\subseteq V(G)\setminus I\), Lemmas 3.3 and 2.1 give
\[
|J|\le b_\mu(t).
\]
Therefore
\[
\alpha(G-I)\le b_\mu(t).
\]

Take a central bag \(V(G)\setminus I\), and, for every \(i\in I\), attach a bag
\[
(V(G)\setminus I)\cup\{i\}.
\]
This is a tree decomposition, since \(I\) is independent. Its bag independence number is at most \(b_\mu(t)+1\). This proves Theorem A(2).

For \(\mu=1\), the resulting bound is \(2t-1\).

## 4.4. Bounded chromatic number

Here is a useful general observation about incident-edge covers.

### Lemma 4.2

Suppose a graph has a tree decomposition such that, for every bag \(B\), all edges incident with \(B\) have a vertex cover of cardinality at most \(k\). Then
\[
\operatorname{tw}(G)\le k.
\]

### Proof

Use the standard treewidth–bramble duality.

Every bramble is hit by some bag \(B\): the nodes whose bags meet a connected bramble member form a subtree, and these subtrees pairwise intersect; the Helly property for subtrees supplies a common node.

Let \(C\) be a cover of all edges incident with \(B\), with \(|C|\le k\). A bramble member avoiding \(C\) nevertheless meets \(B\). Any vertex of \(B\setminus C\) is isolated in \(G-C\), so such a connected member must be a singleton. There can be only one distinct singleton of this kind, because different ones do not touch. Hence \(C\), together with at most one vertex, hits the bramble.

Every bramble therefore has order at most \(k+1\), and treewidth–bramble duality gives \(\operatorname{tw}(G)\le k\). \(\square\)

Now let \(V_1,\dots,V_r\) be color classes of \(G\), and fix a bag \(B\). For every ordered pair \(i\ne j\), consider the bipartite graph with sides
\[
B\cap V_i,\qquad V_j,
\]
containing all edges of \(G\) between these sides. It has induced matching number at most \(\mu\), because every edge meets \(B\); its sides are independent, so induced matchings here are induced matchings in \(G\). It also has no \(K_{t,t}\).

Lemma 2.1 gives a vertex cover of size at most \(b_\mu(t)\) for each ordered pair. The union of these \(r(r-1)\) covers meets every edge incident with \(B\). Lemma 4.2 now yields
\[
\operatorname{tw}(G)\le r(r-1)b_\mu(t).
\]
This proves Theorem A(3), including the edgeless case \(r=1\).

# 5. What remains unresolved

The partial results above do not give the required polynomial independent of \(n\).

The obstruction in the present argument is precise:

- Theorem B supplies low-independence covers of all edges incident with individual bags.
- Those covers can contain vertices far outside their original bags.
- Replacing bags by the covers does not preserve edge coverage and the running-intersection condition.
- The recursive construction repairs these issues, but accumulates one separator per level and hence the factor \(\log n\).

The maximum-independent-set deletion result also does not automatically extend to all of \(G\). For example, deleting one part of \(K_{n,n}\) leaves an edgeless graph, whereas
\[
\operatorname{tree\text{-}\alpha}(K_{n,n})=n.
\]
This is not a counterexample to the question; it shows why reinserting an independent set requires additional control.

There is one further valid obstruction bound. The proof of Lemma 4.2, using Theorem B instead of cardinality covers, shows that **every bramble has a hitting set of independence number at most \(g_\mu(t)+1\)**. I do not infer a tree-independence bound from this: the standard cardinality version of treewidth–bramble duality does not, without an additional argument, justify substituting independence number for cardinality.

Thus the general question remains open in this attack. The completed progress consists of the degree-\(\mu+1\) bipartite cover bound, the unbounded-chromatic global-induced-matching special case, the improved bounded-color result, and polynomial local guards yielding the stated logarithmic-order bound.