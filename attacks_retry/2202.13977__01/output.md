```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the desired linear pure-pair bound for every three-backedge target when the host admits an ordering with uniformly bounded backedge codegrees.",
  "would_publish": false,
  "caveats": "Bounded backedge codegrees are an additional host hypothesis; the unrestricted question, including the D5 case, is not settled."
}
```

## 1. A restricted-host theorem

The sparse-backedge approach can be extended beyond the high-girth setting in the previous attempt. The result below permits triangles and bounded common-neighbor multiplicities, and requires no separate edge-density assumption. It also applies to every forest-ordered target, not just targets with three backedges.

The argument is self-contained; it does not use the previous attempt’s normal-form or nesting lemmas.

For an ordering \(\pi=(v_1,\ldots,v_n)\) of a tournament \(G\), write \(J_\pi(G)\) for its backedge graph:
\[
v_iv_j\in E(J_\pi(G))
\quad\Longleftrightarrow\quad
i<j\text{ and }v_j\to v_i.
\]
For an undirected graph \(J\), define its maximum codegree by
\[
\kappa(J)=\max_{x\ne y}|N_J(x)\cap N_J(y)|.
\]
Thus \(\kappa(J)\le t\) means that \(J\) contains no \(K_{2,t+1}\) as a—not necessarily induced—subgraph.

Also define
\[
p(G)=\max\{\min(|A|,|B|): A,B\subseteq V(G),\ A\cap B=\varnothing,\ A\to B\}.
\]

### Theorem

Let \(H\) be a tournament on \(h\ge2\) vertices with an ordering whose backedge graph \(F\) is a forest. Let \(r\) be the number of nonisolated vertices of \(F\), and let \(t\ge0\) be an integer.

If a tournament \(G\), with \(n>1\) vertices, has an ordering \(\pi\) satisfying
\[
\kappa(J_\pi(G))\le t,
\]
then either \(G\) contains \(H\), or
\[
p(G)\ge \frac{n}{2h(r+6)(t+2)}. \tag{1}
\]

In particular, for each fixed \(t\), all forest-ordered targets have the desired strong EH conclusion within this restricted class of hosts.

---

## 2. Three elementary tools

Fix an ordering of \(G\), put \(J=J_\pi(G)\), and suppose that \(G\) has no pure pair with both sides of size \(s\).

Two sets are **separated** if every vertex of one precedes every vertex of the other in the ordering. Separated, \(J\)-anticomplete sets of size \(s\) would constitute a pure pair. We use this observation repeatedly.

### 2.1. Bounded codegrees bound degrees when pure pairs are small

If \(\kappa(J)\le t\), then
\[
\Delta(J)<(t+2)s. \tag{2}
\]

Indeed, suppose some vertex \(v\) has at least \((t+2)s\) neighbors in \(J\). Let \(A\) be the first \(s\) vertices of \(N_J(v)\) in the ordering.

Each \(a\in A\) has at most \(t\) neighbors inside \(N_J(v)\), since
\[
|N_J(a)\cap N_J(v)|\le t.
\]
Consequently, among the at least \((t+1)s\) remaining vertices of \(N_J(v)\), at most \(ts\) have a neighbor in \(A\). We can therefore choose \(s\) of them forming a set \(B\) anticomplete to \(A\). All vertices of \(A\) precede all vertices of \(B\), so \(A\to B\), a contradiction.

### 2.2. A cleaning observation

Let \(X,Y\) be separated sets, and let \(L\ge1\). If
\[
|Y|\ge Ls,
\]
then fewer than \(s\) vertices of \(X\) have fewer than \(L\) neighbors in \(Y\).

Otherwise, choose \(s\) such vertices, forming \(X'\). Their combined neighborhood in \(Y\) has size at most \((L-1)s\). At least \(s\) vertices of \(Y\) are therefore anticomplete to \(X'\), again yielding a pure pair.

### 2.3. Independent representatives

We will use the following elementary consequence of the symmetric Lovász local lemma.

**Lemma.** Let \(J\) have maximum degree at most an integer \(D\ge1\). If \(W_1,\ldots,W_k\) are disjoint sets with
\[
|W_i|\ge6D
\]
for every \(i\), then there is an independent set containing exactly one vertex from each \(W_i\).

**Proof.** Restrict each \(W_i\) to size \(M=6D\), and independently choose one vertex uniformly from each set.

For every edge \(xy\) joining distinct sets, the event that both endpoints are selected has probability \(M^{-2}\). It depends only on events involving one of its two vertex classes. Since at most \(MD\) edges meet any one class, its dependency degree is at most \(2MD-1\). Thus
\[
e\,M^{-2}(2MD)=\frac{2eD}{M}=\frac e3<1.
\]
The symmetric local lemma gives a choice with no selected edge. If there are no such events, the conclusion is immediate. \(\square\)

---

## 3. Proof of the theorem

Suppose that \(G\) is \(H\)-free. Set
\[
p=p(G),\qquad s=p+1,\qquad
D=(t+2)s,\qquad K=(r+6)(t+2).
\]
Because \(n>1\), we have \(p\ge1\). By (2),
\[
\Delta(J)<D. \tag{3}
\]

We show that
\[
n<hK(p+1). \tag{4}
\]

Suppose instead that \(n\ge hKs\). Partition the ordering of \(G\) into \(h\) consecutive blocks
\[
V_1,\ldots,V_h,
\qquad |V_i|\ge Ks.
\]
Block \(V_i\) corresponds to vertex \(i\) in the fixed forest ordering of \(H\).

We first embed the nonisolated vertices of \(F\), then select its isolated vertices.

### 3.1. Prepare the nontrivial components

If \(r=0\), skip directly to Section 3.3. Otherwise \(r\ge2\).

Root each nontrivial component of \(F\), and put
\[
L=(r-2)t+1.
\]
For each nonisolated vertex \(i\), define \(U_i\subseteq V_i\), working from the leaves towards the roots, by
\[
U_i=
\left\{
x\in V_i:
|N_J(x)\cap U_j|\ge L
\text{ for every child }j\text{ of }i
\right\}.
\]
For a leaf, this simply says \(U_i=V_i\).

If \(d_i\) is the number of children of \(i\), then
\[
|U_i|\ge |V_i|-d_i(s-1). \tag{5}
\]

To prove this inductively, observe that every already constructed child set satisfies
\[
|U_j|
\ge Ks-(r-1)(s-1)
\ge \bigl(K-r+1\bigr)s
\ge Ls.
\]
The last inequality follows from
\[
K-(L+r-1)=8t+r+12>0.
\]
By the cleaning observation, each child excludes at most \(s-1\) vertices from its parent block. This proves (5).

### 3.2. Embed the nonisolated vertices

Process the rooted forest in an order in which parents precede children. We choose a vertex \(x_i\in U_i\) for each nonisolated vertex \(i\), maintaining an induced copy of the portion of \(F\) already processed.

**Choosing a root.** Suppose \(q\) vertices have already been chosen. A root has no required neighbor among them. Its \(d_i\) children are still unchosen, so
\[
q+d_i\le r-1.
\]
Using (3) and (5), the number of available vertices in \(U_i\) having no neighbor among previously selected vertices is at least
\[
\begin{aligned}
|U_i|-qD
&\ge Ks-d_i(s-1)-qD\\
&\ge Ks-(r-1)D\\
&=7D>0.
\end{aligned}
\]
Choose one.

**Choosing a nonroot.** Let \(a\) be its parent. Since \(x_a\in U_a\), there are at least \(L\) candidates in
\[
N_J(x_a)\cap U_i.
\]
Every previously selected vertex \(w\ne x_a\) rules out at most \(t\) candidates, because
\[
|N_J(x_a)\cap N_J(w)|\le t.
\]
There are at most \(r-2\) such vertices. Hence at least
\[
L-(r-2)t=1
\]
candidate remains.

It is adjacent to its parent and to no other previously selected vertex, exactly as required in a forest. Distinct block assignments ensure that all chosen vertices are distinct.

We have now embedded all nonisolated vertices of \(F\), with the correct block assignments and with no unwanted edges.

### 3.3. Select the isolated vertices

For each isolated vertex \(i\) of \(F\), delete from \(V_i\) every neighbor of one of the \(r\) selected vertices. Let the remaining set be \(W_i\). By (3),
\[
|W_i|\ge Ks-rD=6D.
\]
The independent-representatives lemma supplies one vertex from each such \(W_i\), with all these additional vertices pairwise nonadjacent in \(J\).

They are also nonadjacent to the previously selected vertices. Thus the selected vertices induce exactly \(F\), and one selected vertex lies in each corresponding block. Their tournament is therefore an ordered copy of \(H\), contradicting \(H\)-freeness.

This proves (4). Finally, \(p+1\le2p\), so
\[
n<hK(p+1)\le2hKp.
\]
Substituting \(K=(r+6)(t+2)\) proves (1). \(\square\)

---

## 4. Application to every target with at most three backedges

There is a small point needed to cover all such targets: their given three-edge backedge graph need not itself be a forest. Nevertheless, they always admit a forest ordering.

### Lemma

Every tournament admitting an ordering with at most three backedges also admits a forest ordering.

**Proof.** A graph with at most three edges is a forest unless its edges form a triangle.

In the remaining case, let the triangle vertices occur as \(a<b<c\). Its three edges are all the backedges of the tournament. Move \(c\) to immediately before \(a\), leaving every other relative order unchanged.

The new backedge graph consists of:

- the edge \(ab\);
- a star centered at \(c\), whose leaves are the vertices originally strictly between \(a\) and \(c\), other than \(b\);
- isolated vertices.

The edge \(ab\) is disjoint from that star. Hence this is a forest. \(\square\)

Consequently, the theorem proves the following restricted version of the question:

### Corollary

Fix a tournament \(H\) on \(h\ge2\) vertices admitting an ordering with at most three backedges, and fix \(t\ge0\). Every \(H\)-free tournament \(G\) admitting an ordering with maximum backedge codegree at most \(t\) satisfies
\[
p(G)\ge
\frac{|G|}{2h(h+6)(t+2)}. \tag{6}
\]

There are better constants when the initial backedge graph is already a forest:

- Since three edges have at most six nonisolated endpoints,
  \[
  p(G)\ge\frac{|G|}{24h(t+2)}.
  \]
- For the path-plus-isolates model
  \[
  F=P_4\mathbin{\dot\cup}(h-4)K_1,
  \]
  we have \(r=4\), giving
  \[
  p(G)\ge\frac{|G|}{20h(t+2)}. \tag{7}
  \]

In particular, a backedge graph with no four-cycle as a subgraph has codegree at most one. For the path-plus-isolates targets, (7) therefore gives
\[
p(G)\ge\frac{|G|}{60h},
\]
allowing triangles and imposing no separate density bound.

---

## 5. A necessary feature of any counterexample sequence

The theorem also gives a robust obstruction to constructing a counterexample.

Fix a forest-ordered target \(H\). Suppose that \(H\)-free tournaments \(G_m\) satisfy
\[
|G_m|\longrightarrow\infty,
\qquad
\frac{p(G_m)}{|G_m|}\longrightarrow0.
\]
Then, for every fixed \(\delta>0\) and integer \(t\ge0\), all sufficiently large \(m\) have the following property:

> For every ordering of \(G_m\), and every set \(X\subseteq V(G_m)\) with \(|X|\ge\delta|G_m|\), the backedge graph induced on \(X\) contains \(K_{2,t+1}\) as a subgraph.

Indeed, otherwise the theorem applied to \(G_m[X]\) would give
\[
p(G_m)\ge p(G_m[X])
\ge
\frac{\delta |G_m|}{2h(r+6)(t+2)},
\]
contradicting the assumed limit.

Thus a counterexample cannot merely avoid the previous attempt’s high-girth hypothesis: its backedge graphs must have unbounded common-neighbor multiplicities on every linear-sized subset, in every ordering.

## 6. The unresolved gap

This does **not** prove that the \(D_5\)-free condition can be omitted.

The missing issue remains arbitrary hosts. The fact that the forbidden target has three backedges places no bounded-codegree condition on a host ordering in this argument. The theorem supplies a uniform strong EH constant only after a fixed codegree bound \(t\) is imposed; allowing \(t\) to grow with the host size does not establish the strong EH-property.

Accordingly:

- the unrestricted \(D_5\) case is not settled here;
- no counterexample is constructed;
- the rigorous progress is a bounded-codegree host theorem covering all three-backedge targets—and, more generally, all forest-ordered targets.