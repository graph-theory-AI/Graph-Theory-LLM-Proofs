```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The intended finite-girth conjecture holds for girth 4 and, for girth at least 5, reduces to targets of minimum degree at least 2, while the literal formulation fails for acyclic F.",
  "would_publish": false,
  "caveats": "The core cases F=C_g for g>=5 remain unresolved; forests must be excluded from the statement."
}
```

# Mathematical writeup

## 1. Precise formulation and an edge case

Use the standard convention that an acyclic graph has girth \(\infty\). As literally stated, the conjecture is false: take \(F=K_2\). Then \(F\) is triangle-free and has girth \(\infty\), while every finite graph \(G\) of girth \(\infty\) is a forest and hence satisfies
\[
\chi(G)\le 2.
\]
Thus graphs \(G\) of arbitrarily large chromatic number cannot have the same girth as \(F\).

Presumably the intended conjecture is therefore:

> **Finite-girth conjecture.** For every triangle-free graph \(F\) containing a cycle, there is a constant \(c_F\) and graphs \(G\) of arbitrarily large chromatic number such that
> \[
> \operatorname{girth}(G)=\operatorname{girth}(F)
> \]
> and every \(F\)-free induced subgraph of \(G\) has chromatic number at most \(c_F\).

I address this intended version below.

---

## 2. The conjecture holds when \(\operatorname{girth}(F)=4\)

### Proposition 2.1
Let \(F\) be triangle-free with \(\operatorname{girth}(F)=4\). Then the finite-girth conjecture holds for \(F\).

### Proof
Theorem 3 of the source paper, in the form supplied in the question, gives a constant \(c_F\) and triangle-free graphs \(G\) of arbitrarily large chromatic number such that every induced \(F\)-free subgraph of \(G\) has chromatic number at most \(c_F\).

Given \(k\), choose such a \(G\) with
\[
\chi(G)>\max\{k,c_F\}.
\]
Since \(G\) itself has chromatic number greater than \(c_F\), it cannot be \(F\)-free. Thus \(G\) contains an induced copy of \(F\), and consequently contains a \(4\)-cycle. On the other hand, \(G\) is triangle-free. Therefore
\[
\operatorname{girth}(G)=4=\operatorname{girth}(F).
\]
The required induced-subgraph property is exactly the one supplied by Theorem 3. \(\square\)

Thus the first genuinely unresolved girth is \(5\).

---

## 3. An induced-extension lemma for graphs of girth at least five

Say that \(F\) is a **rooted-forest extension** of an induced subgraph \(H\) if the vertices of \(F-H\) can be ordered as
\[
v_1,\ldots,v_m
\]
so that each \(v_i\) has exactly one neighbor in
\[
V(H)\cup\{v_1,\ldots,v_{i-1}\}.
\]
Equivalently, \(F-H\) consists of trees, each attached to \(H\) by one edge.

### Lemma 3.1
Let \(F\) be an \(n\)-vertex rooted-forest extension of \(H\). Let \(J\) be a graph of girth at least \(5\) with
\[
\delta(J)\ge 2n.
\]
Then every induced copy of \(H\) in \(J\) extends to an induced copy of \(F\).

### Proof
Fix an induced embedding of \(H\) into \(J\). We embed \(v_1,\ldots,v_m\) successively.

Suppose that the vertices embedded so far form a set \(A\), and let \(x\in A\) be the image of the unique earlier neighbor of the next vertex \(v_i\). We seek a vertex
\[
z\in N_J(x)\setminus A
\]
which has no neighbor in \(A\setminus\{x\}\).

For every \(y\in A\setminus\{x\}\):

- if \(xy\in E(J)\), then \(N_J(x)\cap N_J(y)=\varnothing\), since a common neighbor would form a triangle;
- if \(xy\notin E(J)\), then
  \[
  |N_J(x)\cap N_J(y)|\le 1,
  \]
  since two common neighbors would form a \(4\)-cycle.

Consequently, among the neighbors of \(x\),

- at most \(|A|\) are already used;
- at most \(|A|-1\) further vertices are adjacent to some member of \(A\setminus\{x\}\).

Since \(|A|\le n-1\), fewer than \(2n\) neighbors of \(x\) are forbidden. The inequality \(\deg_J(x)\ge2n\) therefore leaves a valid choice for \(z\).

At every step the new vertex is adjacent to precisely its prescribed parent among the already embedded vertices. Induction therefore produces an induced copy of \(F\). \(\square\)

The absence of \(4\)-cycles is essential to this argument: in a triangle-free graph containing \(K_{2,t}\), all neighbors of one prospective parent may also be adjacent to a previously embedded nonneighbor.

---

## 4. Reduction to the \(2\)-core

Recall that the \(2\)-core of a graph is the induced subgraph obtained by repeatedly deleting vertices of degree at most one.

### Proposition 4.1
Let \(F\) be a connected graph of girth \(g\ge5\), and let \(H\) be its nonempty \(2\)-core. Suppose there is a constant \(c_H\) and graphs \(G\) of arbitrarily large chromatic number and girth \(g\) such that every induced \(H\)-free subgraph of \(G\) is \(c_H\)-colorable.

Then the same graphs satisfy the conjectured conclusion for \(F\), with
\[
c_F=\max\{c_H,2|V(F)|\}.
\]

### Proof
The components deleted in forming the \(2\)-core are trees, each attached to \(H\) by exactly one edge. Hence \(F\) is a rooted-forest extension of \(H\). Also every cycle of \(F\) lies in \(H\), so
\[
\operatorname{girth}(H)=\operatorname{girth}(F)=g.
\]

Fix one of the assumed host graphs \(G\), and let \(S\subseteq V(G)\) induce an \(F\)-free graph. Suppose for a contradiction that
\[
q:=\chi(G[S])>\max\{c_H,2|V(F)|\}.
\]
Choose an induced subgraph \(J\subseteq G[S]\), minimal by vertex inclusion subject to \(\chi(J)=q\). The standard critical-graph argument gives
\[
\delta(J)\ge q-1\ge 2|V(F)|.
\]
Indeed, if some vertex had degree at most \(q-2\), a \((q-1)\)-coloring after deleting it could be extended to that vertex.

Since \(q>c_H\), the graph \(J\) contains an induced copy of \(H\). Moreover, \(J\) has girth at least \(g\ge5\). Lemma 3.1 now extends this copy of \(H\) to an induced copy of \(F\), contradicting the choice of \(S\). Therefore
\[
\chi(G[S])\le \max\{c_H,2|V(F)|\}.
\]
\(\square\)

### Corollary 4.2
For girth at least \(5\), it is enough to prove the conjecture for connected triangle-free graphs of minimum degree at least \(2\).

### Justification
If \(F\) is disconnected but has a cycle, first form a connected triangle-free graph \(F^+\) containing \(F\) as an induced subgraph by connecting its components in a tree-like manner with new paths of length two. These new edges are bridges, so
\[
\operatorname{girth}(F^+)=\operatorname{girth}(F).
\]
If the conclusion holds for \(F^+\), it holds for \(F\), because every induced \(F\)-free graph is automatically \(F^+\)-free.

Now take the \(2\)-core \(H\) of \(F^+\). It has minimum degree at least two and the same girth. Proposition 4.1 transfers the conclusion from \(H\) to \(F^+\), and hence to \(F\).

In particular, once the conjecture is known for \(C_g\), Proposition 4.1 immediately extends it to every connected unicyclic graph whose unique cycle has length \(g\).

---

## 5. A finite-girth substitute for forests

Although forests invalidate the literal “same girth” statement, the induced-subgraph conclusion itself is easy in hosts of finite girth at least five.

### Proposition 5.1
For every fixed tree \(T\) on \(n\) vertices and every graph \(G\) of girth at least \(5\), every induced \(T\)-free subgraph of \(G\) is \(2n\)-colorable.

### Proof
If an induced \(T\)-free subgraph had chromatic number greater than \(2n\), a vertex-critical induced subgraph would have minimum degree at least \(2n\). Applying Lemma 3.1 with \(H\) a single root vertex would produce an induced copy of \(T\), a contradiction. \(\square\)

Since graphs of arbitrarily large chromatic number and arbitrarily large prescribed finite girth exist by the standard probabilistic construction, one obtains hosts of arbitrarily large chromatic number and arbitrarily large finite girth in which all induced \(T\)-free subgraphs have bounded chromatic number. What is impossible is making the host girth equal to \(\infty\).

---

## 6. The remaining core obstruction

The reduction does not resolve even the basic case \(F=C_g\), \(g\ge5\). In a graph \(G\) of girth at least \(g\), every \(g\)-cycle is automatically induced: a chord would split it into a shorter cycle. Thus for \(F=C_g\) the desired statement becomes:

> Find girth-\(g\) graphs \(G\) of arbitrarily large chromatic number such that every induced subgraph containing no \(g\)-cycle has bounded chromatic number.

Equivalently, every high-chromatic induced subgraph must contain a shortest cycle.

One useful necessary condition can be expressed through the \(g\)-cycle hypergraph \(\mathcal C_g(G)\), whose vertices are \(V(G)\) and whose hyperedges are the vertex sets of the \(g\)-cycles. If every \(C_g\)-free induced subgraph of \(G\) is \(c\)-colorable, then
\[
\chi(G)\le c\,\chi(\mathcal C_g(G)).
\]
Indeed, a proper coloring of \(\mathcal C_g(G)\) partitions \(V(G)\) into sets containing no \(g\)-cycle, each of which is \(c\)-colorable. Consequently, any successful family must have shortest-cycle hypergraphs of unbounded chromatic number. Merely taking arbitrary high-girth, high-chromatic graphs does not guarantee this concentration of shortest cycles.

The odd-girth theorem from the source paper does not close this gap: for example, an odd-girth-\(5\) host may still contain \(4\)-cycles and therefore have ordinary girth \(4\).

Hence the corrected finite-girth conjecture remains open for \(g\ge5\), already for \(F=C_5\) and \(F=C_6\). The results above settle girth \(4\), isolate the cyclic \(2\)-core as the only essential part for larger girth, and identify the acyclic defect in the catalog formulation.