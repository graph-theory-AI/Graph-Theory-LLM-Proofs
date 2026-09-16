```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For even k, I obtain a sharp spanning bridge-count criterion and an explicit nearly spanning bound when every bridge-block has o(r^2) vertices.",
  "would_publish": false,
  "caveats": "The general conjecture and odd k >= 3 remain unresolved; novelty of these factor-theoretic consequences has not been checked."
}
```

## 1. Partial results

All graphs below are finite. A **bridge-block** means a component remaining after all bridges are deleted; it is not a vertex-biconnected block.

I prove the following special case of the conjecture.

### Theorem 1
Let \(k\ge 2\) be even, let \(r\ge 3k/2\), and let \(G\) be a simple \(r\)-regular graph on \(n\) vertices. Write
\[
B=\text{number of bridges of }G,\qquad
M=\max\{|C|:C\text{ is a bridge-block of }G\},
\]
and put
\[
a=r-\frac{3k}{2}+3.
\]
Then \(G\) has a \(k\)-regular subgraph \(H\) satisfying
\[
|V(H)|
\ge n-\frac{2BM}{a}
\ge
\left(1-\frac{2M}{(r-1)(r-3k/2+3)}\right)n. \tag{1}
\]

Consequently, for each fixed even \(k\), the conjecture holds along every family for which
\[
M=o(r^2).
\]
For example, if \(M\le Cr\), it suffices to take
\[
r\ge \max\left\{3k,\frac{8C}{\epsilon}\right\}.
\]

There is also a spanning conclusion without any bound on \(M\).

### Theorem 2
Under the same assumptions, if
\[
B\le r-\frac{3k}{2}+2, \tag{2}
\]
then \(G\) has a spanning \(k\)-factor.

For odd \(r\ge 3k/2\), the bridge-count threshold in (2) is sharp: there is a simple \(r\)-regular graph with exactly
\[
r-\frac{3k}{2}+3
\]
bridges and no spanning \(k\)-factor.

In particular, for fixed even \(k\), every \(r\)-regular graph with \(n=o(r^2)\) has a spanning \(k\)-factor once \(r\) is sufficiently large.

I also give a quantitative relaxation valid without the bridge-block-size hypothesis:

### Theorem 3
If \(k\) is even and \(r\ge 3k/2\), then \(G\) has a spanning subgraph \(F\) such that
\[
d_F(v)\in\{0,2,\ldots,k\}
\]
and
\[
\sum_{v\in V(G)}(k-d_F(v))
\le \frac{2kB}{r}
\le \frac{2kn}{r(r-1)}. \tag{3}
\]
Thus at most \(kn/[r(r-1)]\) vertices have degree different from \(k\).

For \(k=2\), this does give an actual regular subgraph:
\[
|V(H)|\ge
\left(1-\frac{2}{r(r-1)}\right)n
\qquad(r\ge3). \tag{4}
\]
The order \(r^{-2}\) of the loss in (4) is optimal in general, as shown below. For \(k\ge4\), however, (3) is not a solution to the conjecture.

These arguments use the standard Tutte \(f\)-factor theorem and the capacitated \(b\)-matching polytope theorem. I make no claim that their consequences here are new.

---

## 2. A factor lemma with a small deficiency budget

For a loopless graph \(Q\) with \(\Delta(Q)\le r\), define its total degree deficiency by
\[
D(Q)=\sum_{v\in V(Q)}(r-d_Q(v)).
\]

### Lemma 4
Let \(k\ge2\) be even and \(r\ge3k/2\). If \(Q\) has \(\beta\) bridges and
\[
D(Q)+\beta\le r-\frac{3k}{2}+2, \tag{5}
\]
then \(Q\) has a spanning \(k\)-factor.

#### Proof

For disjoint sets \(S,T\subseteq V(Q)\), put
\[
U=V(Q)\setminus(S\cup T).
\]
Let \(q=q(S,T)\) count the components \(C\) of \(Q[U]\) for which
\[
k|C|+e(C,T)
\]
is odd. Since \(k\) is even, these are precisely the components with \(e(C,T)\) odd.

Tutte’s \(f\)-factor theorem says that it suffices to prove
\[
\Phi(S,T):=
k(|S|-|T|)+2e(T)+e(T,U)-q\ge0 \tag{6}
\]
for every such pair \(S,T\).

Write
\[
A=e(T,U),\qquad L=e(S,U).
\]
We have \(q\le A\). Also,
\[
3q\le A+2L+2\beta. \tag{7}
\]
Indeed, consider a component counted by \(q\).

* If \(e(C,T)\ge3\), its contribution to \(A\) already pays for \(3\).
* If \(e(C,T)=1\) and \(e(C,S)\ge1\), its contribution to \(A+2L\) is at least \(3\).
* Otherwise its entire boundary consists of one edge to \(T\), and that edge is a bridge of \(Q\).

Distinct components in the last case correspond to distinct bridges, proving (7).

If \(|S|\ge|T|\), then \(q\le A\) immediately proves (6). Hence suppose
\[
d=|T|-|S|\ge1.
\]
Set
\[
D_S=\sum_{v\in S}(r-d_Q(v)),\qquad
D_T=\sum_{v\in T}(r-d_Q(v)).
\]
Subtracting the degree sums on \(S\) and \(T\) gives
\[
A-L=rd-D_T+D_S-2e(T)+2e(S).
\]
Using (7), we obtain
\[
\begin{aligned}
\Phi(S,T)
&\ge -kd+2e(T)+\frac23(A-L)-\frac23\beta\\
&=\left(\frac{2r}{3}-k\right)d
 +\frac23e(T)+\frac43e(S)
 -\frac23(D_T-D_S+\beta)\\
&\ge \frac{2r}{3}-k-\frac23(D(Q)+\beta)\\
&\ge-\frac43.
\end{aligned}
\]
Here \(r\ge3k/2\) justifies replacing \(d\) by \(1\).

Finally, \(\Phi(S,T)\) is an even integer: \(k\) is even and
\[
q\equiv e(T,U)\pmod2.
\]
Therefore \(\Phi(S,T)\ge-4/3\) implies \(\Phi(S,T)\ge0\). This verifies every inequality in Tutte’s theorem. ∎

Applying Lemma 4 with \(Q=G\), for which \(D(G)=0\), proves Theorem 2’s sufficient condition.

---

## 3. Counting bridges and proving Theorem 1

Let the bridge-blocks of \(G\) be \(C_1,\ldots,C_m\). Write
\[
s_i=|C_i|,\qquad b_i=e_G(C_i,V(G)\setminus C_i).
\]
Every boundary edge counted by \(b_i\) is a bridge, so
\[
\sum_i b_i=2B.
\]
If \(G\) has \(c\) connected components, contracting its bridge-blocks gives a forest, whence
\[
m=B+c.
\]

Simplicity and regularity imply
\[
s_i+b_i\ge r+1. \tag{8}
\]
Indeed, any vertex of \(C_i\) has at most \(s_i-1\) neighbors inside \(C_i\), and at most \(b_i\) incident edges leaving it.

Summing (8) yields
\[
n+2B\ge(r+1)(B+c).
\]
Thus
\[
B\le \frac{n-(r+1)c}{r-1}\le\frac{n}{r-1}. \tag{9}
\]

Each \(G[C_i]\) is bridgeless: every nonbridge edge of \(G\) belongs to a cycle, and deleting bridges removes no cycle edge. Moreover,
\[
D(G[C_i])
=\sum_{v\in C_i}(r-d_{G[C_i]}(v))
=b_i.
\]
By Lemma 4, \(G[C_i]\) has a spanning \(k\)-factor whenever
\[
b_i\le a-1.
\]

Take the union of these factors over all such blocks. This gives a \(k\)-regular subgraph \(H\) with
\[
|V(H)|=n-\sum_{i:b_i\ge a}s_i.
\]
There are at most \(2B/a\) blocks in this sum, and each has at most \(M\) vertices. Consequently,
\[
|V(H)|\ge n-\frac{2BM}{a}.
\]
Combining this with (9) proves (1).

For the stated explicit consequence, if \(M\le Cr\) and \(r\ge3k\), then
\[
\frac{2M}{(r-1)(r-3k/2+3)}
\le \frac{8C}{r}.
\]
This proves the claimed special case with an explicit \(r_0\). ∎

Notice that the argument actually gives the stronger local statement:

> If every bridge-block has at most \(r-3k/2+2\) incident bridges, then \(G\) has a spanning \(k\)-factor, regardless of the total number of bridges.

---

## 4. Sharpness of the spanning bridge threshold

Fix even \(k\ge2\) and odd \(r\ge3k/2\). Put
\[
h=\frac{k}{2}-1,\qquad b=r-\frac{3k}{2}+3.
\]

We need two connected bridgeless gadgets, each on \(r+2\) vertices.

* **\(Q_1\):** Start with \(K_{r+2}\). Delete a three-vertex path whose middle vertex \(p\) is designated as a port, and delete a perfect matching on the other \(r-1\) vertices.
* **\(Q_3\):** Start with \(K_{r+2}\). Delete a triangle on three designated ports, and delete a perfect matching on the remaining \(r-1\) vertices.

In \(Q_j\), each of its \(j\) ports has degree \(r-1\), and every other vertex has degree \(r\).

These gadgets are connected and bridgeless. For \(r\ge5\), their minimum degree is \(r-1\); they are connected, and every edge has a common neighbor because
\[
d(x)+d(y)-(r+2)\ge r-4\ge1.
\]
For \(r=3\), \(Q_3=K_{3,2}\), while \(Q_1\) is \(K_4-xy\) with a new vertex adjacent to \(x,y\); both are bridgeless.

Now take a new vertex \(v\), together with

* \(b\) disjoint copies of \(Q_1\);
* \(h\) disjoint copies of \(Q_3\).

Join \(v\) to every port. The resulting graph is simple and \(r\)-regular, since
\[
d(v)=b+3h=r.
\]
Its bridges are exactly the \(b\) edges joining \(v\) to the \(Q_1\)-copies.

Every cut in an even-regular subgraph has even size. Hence a \(k\)-regular subgraph can use none of the edges joining \(v\) to a \(Q_1\)-copy, and at most two of the three edges joining \(v\) to any \(Q_3\)-copy. Therefore, if \(v\) belonged to such a subgraph, its degree would be at most
\[
2h=k-2,
\]
a contradiction.

Thus every \(k\)-regular subgraph omits \(v\). The graph has exactly
\[
b=r-\frac{3k}{2}+3
\]
bridges, proving that the threshold in Theorem 2 is sharp for odd \(r\).

This is not a counterexample to the original conjecture: its order is
\[
1+(r-k+2)(r+2)=\Theta_k(r^2),
\]
and the forced omission established here is only one vertex.

---

## 5. A nearly \(k\)-regular even subgraph

Here is a different argument proving Theorem 3. It quantifies how close one can get to a factor, but it also exposes the remaining difficulty.

Delete all bridges from \(G\), obtaining a bridgeless graph \(R\). Let
\[
t(v)=r-d_R(v)
\]
be the number of bridges incident with \(v\), so that
\[
\sum_v t(v)=2B.
\]

Add \(k/2\) distinguishable loops at each vertex of \(R\), obtaining a multigraph \(J\). A loop contributes two to degree. Define a fractional edge vector by
\[
x_e=\frac{k}{r}\quad(e\in E(R)),\qquad
x_\ell=\frac{t(v)}r
\quad(\ell\text{ a loop at }v).
\]
Its degree at every vertex is exactly \(k\), and all coordinates lie in \([0,1]\).

I use the following standard form of the capacitated \(b\)-matching polytope theorem: in addition to the degree equations and \(0\le x_e\le1\), the \(k\)-factor polytope is described by
\[
x(\delta(U)\setminus A)
+\sum_{e\in A}(1-x_e)\ge1 \tag{10}
\]
whenever \(U\subseteq V(J)\), \(A\subseteq\delta(U)\), and \(k|U|+|A|\) is odd. Loops count twice in degree and do not belong to cuts.

Because \(k\) is even, only odd \(|A|\) occur. Set
\[
\alpha=\frac{k}{r}\le\frac23,\qquad
d=|\delta_R(U)|,\qquad f=|A|.
\]
The left side of (10) is
\[
\alpha d+(1-2\alpha)f. \tag{11}
\]
Since \(R\) is bridgeless, a nonempty cut has \(d\ge2\). Empty cuts admit no odd \(A\).

All cases of (10) follow as follows.

* If \(\alpha\le1/2\), then \(f\ge1\), and (11) is at least
  \[
  1+\alpha(d-2)\ge1.
  \]
* If \(\alpha>1/2\) and \(d\) is even, then \(f\le d-1\), giving
  \[
  \alpha d+(1-2\alpha)f
  \ge1+(1-\alpha)(d-2)\ge1.
  \]
* If \(\alpha>1/2\) and \(d\) is odd, then \(d\ge3\) and \(f\le d\), giving
  \[
  \alpha d+(1-2\alpha)f
  \ge(1-\alpha)d\ge1.
  \]

Thus \(x\) belongs to the \(k\)-factor polytope of \(J\). Its total loop weight is
\[
\frac{k}{2}\sum_v\frac{t(v)}r=\frac{kB}{r}.
\]
By the convex-hull conclusion of the polytope theorem, some integral \(k\)-factor of \(J\) uses at most \(kB/r\) loops.

Erase those loops. The remaining ordinary-edge subgraph \(F\subseteq G\) satisfies
\[
d_F(v)\in\{0,2,\ldots,k\}
\]
and
\[
\sum_v(k-d_F(v))
=2(\text{number of selected loops})
\le\frac{2kB}{r}.
\]
Together with (9), this proves Theorem 3. ∎

### The consequence for \(k=2\)

When \(k=2\), a vertex incident with a selected loop has no selected ordinary edge. Such vertices are isolated after the loops are erased, so deleting them leaves a genuine \(2\)-regular subgraph. Therefore
\[
|V(H)|\ge n-\frac{2B}{r}
\ge\left(1-\frac{2}{r(r-1)}\right)n.
\]

The loss order cannot be improved below \(r^{-2}\) uniformly over odd \(r\). To see this, take a tree whose nonleaf vertices all have degree \(r\), and replace each leaf by a copy of \(Q_1\), attaching its port to the former leaf’s neighbor.

If the tree has \(I\) nonleaf vertices, it has
\[
L=(r-2)I+2
\]
leaves. The resulting simple graph is \(r\)-regular and has
\[
n=I+(r+2)L=(r^2-3)I+2r+4.
\]
Every edge incident with one of the \(I\) original nonleaf vertices is a bridge. Hence every \(2\)-regular subgraph omits all \(I\) of them. As \(I\to\infty\), the omitted proportion tends to
\[
\frac1{r^2-3}.
\]
Thus (4) has the optimal order of error, though not an optimal constant.

---

## 6. The unresolved gap

For even \(k\ge4\), Theorem 3 permits degrees \(2,4,\ldots,k-2\), not just \(0\) and \(k\). Deleting these deficient vertices does **not** preserve degree \(k\) at their neighbors.

This is a genuine logical obstruction, even when there is only one deficient vertex. Start with \(K_{k,k}\), choose \(v\) in one part and distinct neighbors \(a,b\) in the other, and form
\[
F=K_{k,k}-\{va,vb\}+ab.
\]
Then \(F\) is connected, \(d_F(v)=k-2\), and every other vertex has degree \(k\). Nevertheless, \(F\) has no nonempty \(k\)-regular subgraph: any selected vertex must retain all its incident edges, forcing its entire connected component—and therefore the deficient vertex—to be selected.

This is not an \(r\)-regular counterexample to the conjecture. It shows why the relaxed factor in Theorem 3 cannot simply be converted into the desired subgraph by discarding its few defective vertices.

Theorem 1 avoids this issue by discarding entire exceptional bridge-blocks. In an unrestricted graph, there are only \(O_k(n/r^2)\) such blocks, but their **total number of vertices** is uncontrolled. Resolving that concentration issue, or repairing the relaxed factor without a cascading loss of vertices, is beyond the arguments here. No new conclusion for odd \(k\ge3\) is established.