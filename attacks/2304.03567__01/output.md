```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit strong oriented-cactus family gives c_b <= 2/3, and the asymptotic constant is exactly 2/3 for strong cactus digraphs and, more generally, for a block-Hamiltonian class.",
  "would_publish": false,
  "caveats": "The general lower bound remains 1/3; root-counting conventions change only additive constants, and the elementary 2/3 upper bound may already be implicit in the full source."
}
```

## 1. Statement and normalization

I use the standard interpretation that a bi-tree is
\[
T=T^+\cup T^-,
\]
where \(T^+\) is an out-arborescence, \(T^-\) is an in-arborescence, their roots are identified, and
\[
V(T^+)\cap V(T^-)=\{r\}.
\]
It is balanced when \(|V(T^+)|=|V(T^-)|\). If this common order is \(t\), then the union has order \(2t-1\).

If the source counts the common root twice, or counts arcs rather than vertices, all estimates below change by at most an additive constant. In particular, the constants are unchanged.

The supplied result gives \(c_b\ge 1/3\). I prove:

\[
\boxed{\frac13\le c_b\le\frac23.}
\]

I also prove that \(2/3\) is the exact asymptotic constant for strong cactus digraphs, indeed for a somewhat larger block-Hamiltonian class.

---

## 2. The upper bound \(c_b\le 2/3\)

### Proposition 2.1

For every \(m\ge1\), there is a strongly connected digraph \(D_m\) on \(3m+1\) vertices whose largest balanced bi-tree has order exactly \(2m+1\).

#### Construction

Let \(S_m\) be the undirected tree consisting of a central vertex \(c\) and three internally disjoint paths of length \(m\) starting at \(c\). Let \(D_m=\overleftrightarrow{S_m}\), obtained by replacing every edge of \(S_m\) by the two opposite arcs.

Thus \(D_m\) is strong and
\[
|V(D_m)|=3m+1.
\]

#### Proof of the upper bound

Let \(T^+,T^-\) be a balanced bi-tree in \(D_m\), with common root \(r\), and put
\[
k=|V(T^+)|-1=|V(T^-)|-1.
\]

Because the underlying graph of \(D_m\) is a tree, each \(V(T^\pm)\) induces a connected vertex set containing \(r\). Moreover, a component of \(S_m-r\) cannot meet both \(T^+\) and \(T^-\): otherwise both trees would have to contain the unique neighbor of \(r\) in that component, contrary to their disjointness outside \(r\).

If \(r=c\), then \(S_m-c\) has three components, each of order \(m\). Since each component can meet at most one of the two constituent trees, one of \(T^+,T^-\) meets at most one component. Hence \(k\le m\).

If \(r\ne c\), then \(r\) lies on one of the three legs. Removing \(r\) gives at most two components, one of which is the terminal part of that leg and has at most \(m-1\) vertices. If both trees are nontrivial, they must use distinct components, so again \(k\le m\).

Consequently each constituent tree has order at most \(m+1\), and
\[
|V(T^+\cup T^-)|\le 2m+1.
\]

Equality is attained by taking \(r=c\), one complete leg as \(T^+\), and another complete leg as \(T^-\). Thus
\[
b(D_m)=2m+1.
\]

It follows that
\[
\frac{b(D_m)}{|V(D_m)|}
 =\frac{2m+1}{3m+1}\longrightarrow\frac23,
\]
so no constant larger than \(2/3\) can work universally. ∎

### Oriented version

The same asymptotic upper bound does not depend on allowing digons. Let \(O_M\) have a central vertex \(c\), and for \(i=1,2,3\) add the directed cycles
\[
c\to p_i\to q_i\to c
\]
and
\[
p_i\to z_{i,1}\to z_{i,2}\to\cdots\to z_{i,M}\to p_i.
\]
These cycles are otherwise vertex-disjoint. This is a strong oriented cactus on
\[
3M+7
\]
vertices.

Call the \(3M\) vertices \(z_{i,j}\) heavy. If the root is \(c\), then both constituent trees cannot meet the same set \(\{z_{i,1},\ldots,z_{i,M}\}\), since both would have to contain \(p_i\). Thus one tree contains heavy vertices from at most one lobe. If the root lies in the \(j\)-th branch of \(O_M-c\), at most one constituent tree contains \(c\); the other is confined to that branch and again contains at most \(M\) heavy vertices.

Hence one constituent tree has order at most \(M+7\). Balancedness gives
\[
b(O_M)\le 2M+13,
\]
and therefore
\[
\limsup_{M\to\infty}\frac{b(O_M)}{|V(O_M)|}\le\frac23.
\]

---

## 3. A tight \(2/3\) theorem for strong cactus digraphs

The upper examples above are extremal within a natural class.

### Definition

Call a strong digraph \(D\) **block-Hamiltonian** if every non-bridge block of its underlying undirected graph contains a directed Hamilton cycle. A bridge block of a strong digraph necessarily consists of a digon.

Every strong cactus digraph is block-Hamiltonian. Indeed, every non-bridge block is an undirected cycle. Its induced digraph is strong. If every edge is a digon, it plainly contains a directed spanning cycle. Otherwise, take a singly oriented edge \(v_0\to v_1\). A directed \(v_1\)-to-\(v_0\) path must use the complementary route around the undirected cycle, so together with \(v_0\to v_1\) it forms a directed cycle through the entire block.

### Theorem 3.1

Let \(D\) be a block-Hamiltonian strong digraph on \(n\ge3\) vertices. Then \(D\) contains a balanced bi-tree \(T\) satisfying
\[
|V(T)|\ge \frac{2n}{3}.
\]

In particular, every strong cactus digraph on \(n\ge3\) has such a bi-tree.

### Preliminary block-branch observation

Let \(\mathcal B\) be the block-cutvertex tree of the underlying graph of \(D\).

If \(x\) is a cutvertex and \(Q\) is a component of \(\mathcal B-x\), then the vertices represented by \(Q\), together with \(x\), induce a strong subdigraph. Indeed, a simple directed path from \(x\) to a vertex of that branch, or conversely, cannot leave the corresponding branch of the block tree and subsequently return without repeating \(x\).

Similarly, if \(B\) is a block and \(v\in V(B)\), then the vertices hanging from \(B\) at \(v\), together with \(v\), induce a strong subdigraph. Consequently each such rooted piece has both a spanning out-arborescence and a spanning in-arborescence rooted at its attachment vertex.

We shall repeatedly use the elementary fact that a rooted arborescence can be pruned to any smaller positive order while retaining its root: repeatedly delete a non-root leaf.

### Weighted centroid

Give every cutvertex-node of \(\mathcal B\) weight \(1\), and every block-node \(B\) weight equal to the number of non-cutvertices belonging to \(B\). These weights sum to \(n\).

Choose a weighted centroid \(q\) of \(\mathcal B\); every component of \(\mathcal B-q\) then has weight at most \(n/2\).

There are two cases.

---

### Case 1: \(q\) is a cutvertex

Write \(q=r\). The components of \(\mathcal B-r\) correspond to vertex-disjoint branches of orders
\[
w_1,\ldots,w_s,\qquad \sum_i w_i=n-1,
\]
with every \(w_i\le n/2\).

These branch weights can be divided into two classes whose sums \(a,b\) both satisfy
\[
a,b\ge \frac{n-1}{3}.
\]

To see this, put \(N=n-1\). For \(n\ge4\), every \(w_i\le n/2\le2N/3\); for \(n=3\) the assertion is immediate. If some \(w_i\in[N/3,2N/3]\), take it as one class. Otherwise accumulate weights, all smaller than \(N/3\), until the sum first reaches \(N/3\); the resulting sum is smaller than \(2N/3\).

For every branch in the first class, take a spanning out-arborescence rooted at \(r\), and for every branch in the second class take a spanning in-arborescence rooted at \(r\). Their respective orders are \(a+1\) and \(b+1\). Prune the larger one until both have order
\[
t=1+\min(a,b).
\]
Then
\[
|V(T)|=2t-1
 \ge 1+\frac{2(n-1)}3
 =\frac{2n+1}{3}
 >\frac{2n}{3}.
\]

---

### Case 2: \(q\) is a block

For every \(v\in V(q)\), let \(P_v\) consist of \(v\) together with all vertices in the branches hanging from \(q\) at \(v\), and put
\[
w(v)=|P_v|.
\]
The sets \(P_v\) partition \(V(D)\). By the centroid property,
\[
w(v)\le\frac n2
\]
for every cutvertex \(v\) of \(q\), while a non-cutvertex has \(w(v)=1\).

The block \(q\) has a directed Hamilton cycle; a bridge block is treated as a directed cycle of length two. List its vertices in cyclic order. We need the following elementary weighted-cycle fact.

#### Weighted interval lemma

If nonnegative integer weights of total \(n\) are arranged cyclically and every weight is at most \(n/2\), then some cyclic interval and its complement both have weight at least \(n/3\).

Indeed, start at any point and take a shortest interval of weight at least \(n/3\). If its weight is at most \(2n/3\), it works. Otherwise its last term alone has weight greater than \(n/3\) and at most \(n/2\), so that singleton works.

Apply the lemma and denote the lighter interval by \(J\), of weight \(s\), and its complement by \(I\), of weight \(L\). Thus
\[
\frac n3\le s\le L.
\]

Choose the root \(r\) as the first vertex of \(I\) along the directed Hamilton cycle.

Construct an out-tree by taking the directed path along all vertices of \(I\) and, at each \(v\in I\), attaching a spanning out-arborescence of \(D[P_v]\) rooted at \(v\). Its order is \(L\).

Construct an in-tree by taking the directed path along \(J\) ending at \(r\), and at each \(v\in J\), attaching a spanning in-arborescence of \(D[P_v]\) rooted at \(v\). Its order is \(s+1\), the extra vertex being the common root \(r\).

These trees meet only at \(r\). Pruning the larger gives two trees of common order
\[
t=\min(L,s+1).
\]

If \(L>s\), integrality gives \(L\ge s+1\), so \(t=s+1\), and
\[
2t-1=2s+1>\frac{2n}{3}.
\]
If \(L=s=n/2\), then \(t=n/2\), so
\[
2t-1=n-1\ge\frac{2n}{3}
\]
for \(n\ge3\).

This completes the proof of Theorem 3.1. ∎

---

## 4. Consequences

1. The supplied general lower bound and Proposition 2.1 give
   \[
   \boxed{\frac13\le c_b\le\frac23}.
   \]

2. For strong cactus digraphs,
   \[
   \inf_D \frac{b(D)}{|V(D)|}\longrightarrow\frac23
   \]
   asymptotically. The lower bound is Theorem 3.1, and either the bidirected tripods \(D_m\) or the oriented family \(O_M\) gives asymptotic equality.

3. The same \(2/3\) lower bound holds whenever the digraph contains a spanning strong block-Hamiltonian subdigraph. In particular, it holds when the digraph contains a spanning bidirected tree; hence it holds for every symmetric strong digraph.

4. Any genuine example forcing \(c_b<2/3\) must use structure absent from block-Hamiltonian strong spanning subgraphs. In particular, a non-Hamiltonian two-connected strong block is necessary for such an obstruction.

---

## 5. Remaining gap

Nothing above improves the universal lower bound \(1/3\). Thus the exact value remains unresolved:
\[
\frac13\le c_b\le\frac23.
\]

The cactus argument relies crucially on a directed Hamilton cycle in the centroid block, which permits the weighted branches to be divided into two consecutive intervals. General strong blocks need not have such a cycle, and the argument does not extend to them.