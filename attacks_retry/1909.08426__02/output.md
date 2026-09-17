```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A Ramsey-counting gluing theorem yields an FPT special case, while an explicit prime, highly co-connected family rules out bounded-distance bootstrapping.",
  "would_publish": false,
  "caveats": "The full conjecture remains unresolved here; the gluing pieces must already belong to FPT classes, and novelty is not assessed."
}
```

# 1. Statement and scope

Write
\[
H_t=P(t,t,t,t),\qquad Q_t=P(1,t,t,t).
\]
The problem is to decide whether an \(H_t\)-free graph \(G\) has an independent set of size \(k\), in time \(f_t(k)n^{O(1)}\).

I do not establish this for all \(H_t\)-free graphs. I prove two results:

1. **An FPT gluing theorem.** Two already-solvable hereditary classes can be glued across a cut containing no anticomplete pair of \(t\)-cliques. Its proof uses a degree-moment bound with exponent \(t\), rather than an exponent depending on a Ramsey number. Applied to the stated \(Q_t\)-free algorithm, this gives a precise additional special case.
2. **A stronger obstruction to bounded-distance approaches.** For every \(t\ge2\), there are prime \(H_t\)-free graphs with independence number two, arbitrarily highly connected complements, and arbitrarily large \(Q_t\)-deletion distance.

The only external algorithmic input is the source-paper theorem stated in the question: Independent Set is FPT on \(Q_t\)-free graphs for fixed \(t\). All other ingredients used below are proved. In particular, I do not rely on the previous attempt’s modular-defect theorem or its separator-recursion analysis.

For \(t=1\), the quoted source theorem already coincides with the conjecture.

# 2. A Ramsey degree-moment bound

Consider a graph with a vertex partition \(A\dot\cup B\). Say that the cut satisfies condition \(\mathsf D_t\) if

> there are no cliques \(C_A\subseteq A\), \(C_B\subseteq B\), each of size \(t\), that are anticomplete to each other.

For \(a\in A\), put
\[
D_B(a)=B\setminus N_G(a),\qquad d_B(a)=|D_B(a)|.
\]

The following quantitative strengthening of a direct Ramsey argument is useful.

## Lemma 2.1

Fix \(t\ge1\) and \(k\ge2\). There is a computable constant \(C=C(t,k)\) such that, whenever \(\mathsf D_t\) holds and
\[
\alpha(G[A])<k,\qquad \alpha(G[B])<k,
\]
we have
\[
\sum_{a\in A}(d_B(a)+1)^t
   \le C\bigl(|B|^t+|A|\bigr).                 \tag{1}
\]
The symmetric inequality also holds.

### Proof

Set
\[
\rho=\binom{t+k-2}{t-1}.
\]
The elementary Ramsey bound gives \(R(t,k)\le \rho\). Thus every \(\rho\)-vertex subset of either part contains a \(t\)-clique.

For a graph \(J\), let \(c_t(J)\) denote its number of \(t\)-cliques. If \(|V(J)|=m\ge\rho\) and \(\alpha(J)<k\), double-counting pairs consisting of a \(\rho\)-set and a \(t\)-clique within it gives
\[
c_t(J)\ge
\frac{\binom{m}{t}}{\binom{\rho}{t}}
\ge \frac{m^t}{t^t\rho^t}.                    \tag{2}
\]

On the other hand, every \(t\)-clique \(C\subseteq B\) has fewer than \(\rho\) common nonneighbors in \(A\). Otherwise those common nonneighbors would contain a \(t\)-clique, contradicting \(\mathsf D_t\). Consequently,
\[
\sum_{a\in A} c_t\bigl(G[D_B(a)]\bigr)
   \le (\rho-1)c_t(G[B]).                    \tag{3}
\]

Apply (2) when \(d_B(a)\ge\rho\), and bound \(d_B(a)^t\) by \(\rho^t\) otherwise. We obtain
\[
\begin{aligned}
\sum_{a\in A} d_B(a)^t
&\le \rho^t|A|
 +t^t\rho^t\sum_{a\in A}c_t\bigl(G[D_B(a)]\bigr)\\
&\le \rho^t|A|+t^t\rho^{t+1}|B|^t.
\end{aligned}
\]
Now use
\[
(x+1)^t\le 2^{t-1}(x^t+1).
\]
For example,
\[
C=2^{t-1}\bigl(\rho^t+1+t^t\rho^{t+1}\bigr)
\]
suffices. The symmetric argument is identical. \(\square\)

The important point is that the moment in (1) has exponent **\(t\)**. Merely observing that the nonedges across the cut contain no \(K_{\rho,\rho}\) would give a much less useful parameter-dependent exponent.

# 3. An FPT gluing theorem

## Theorem 3.1

Let \(\mathcal C_1,\mathcal C_2\) be hereditary graph classes on which Independent Set can be solved in times
\[
f_i(k)n^{c_i}\qquad (i=1,2).
\]
Fix \(t\).

Suppose the input includes a partition
\[
V(G)=A\dot\cup B
\]
such that
\[
G[A]\in\mathcal C_1,\qquad G[B]\in\mathcal C_2,
\]
and the cut satisfies \(\mathsf D_t\).

Then Independent Set is FPT on these inputs. More precisely, with
\[
c=\max\{\lceil c_1\rceil,\lceil c_2\rceil,t,2\},
\]
there is an algorithm with running time
\[
F(k)n^{c+t}.
\]

### Proof

First test whether either part contains an independent set of size \(k\). If so, answer yes. Otherwise,
\[
\alpha(G[A])<k,\qquad \alpha(G[B])<k,          \tag{4}
\]
and these inequalities continue to hold after restricting either part.

For each \(p\in\{1,\ldots,k-1\}\), test whether there is an independent set with exactly \(p\) vertices in \(A\) and \(k-p\) in \(B\). We use the following recursion, with current parts \(A',B'\) and remaining targets \(p',q'\).

- If \(p'=0\), invoke the \(\mathcal C_2\) algorithm on \(G[B']\) with target \(q'\).
- If \(q'=0\), invoke the \(\mathcal C_1\) algorithm on \(G[A']\) with target \(p'\).
- Reject immediately if a target exceeds its part’s size.
- Otherwise, branch over all vertices of the smaller current part.

For example, if \(|A'|\le |B'|\), branch on every \(a\in A'\), replacing the instance by
\[
\begin{aligned}
A''&=A'\setminus N_{G[A']}[a],\\
B''&=B'\setminus N_G(a),\\
(p'',q'')&=(p'-1,q').
\end{aligned}
\]
This is exact: every sought solution contains a vertex of \(A'\), and the corresponding branch permits precisely its possible remaining vertices.

It remains to bound the search tree without an exponent depending on \(k\).

For current part sizes \(a,b\), define
\[
\Phi(a,b)
=(a+1)^c(b+1)^t+(a+1)^t(b+1)^c.
\]

Suppose \(1\le a\le b\), so the algorithm branches on \(A'\). For the branch selecting \(v\in A'\), let
\[
d_v=|B'\setminus N_G(v)|.
\]
The new first part has size at most \(a-1\). By Lemma 2.1,
\[
\sum_{v\in A'}(d_v+1)^t
 \le C(b^t+a)
 \le 2C(b+1)^t.                             \tag{5}
\]
Since \(c\ge t\),
\[
\begin{aligned}
\sum_{v\in A'}(d_v+1)^c
&\le (b+1)^{c-t}\sum_{v\in A'}(d_v+1)^t\\
&\le 2C(b+1)^c.                             \tag{6}
\end{aligned}
\]
Combining (5) and (6),
\[
\sum_{\text{children}}\Phi(a_{\rm child},b_{\rm child})
 \le 2C\,\Phi(a,b).                          \tag{7}
\]
The same inequality holds when branching on \(B'\).

The depth is at most \(k\). Therefore the total potential over the recursion tree is at most
\[
(k+1)(2C)^k\Phi(|A|,|B|).
\]
At a leaf, the appropriate class algorithm costs at most a function of \(k\) times the leaf potential. At an internal node, forming all child vertex lists takes \(O((a+b)^2)\) time, which is \(O(\Phi(a,b))\), since \(c\ge2\).

Finally,
\[
\Phi(|A|,|B|)\le 2(n+1)^{c+t}.
\]
Including all choices of \(p\) proves the claimed running time. \(\square\)

### A point about the promise

The hypotheses \(\alpha(G[A])<k\) and \(\alpha(G[B])<k\) are **established by algorithmic calls**, not assumed because the entire input is a no-instance. Thus the running-time proof also applies when the desired independent set crosses the cut.

# 4. Consequences for \(H_t\)-free graphs

## 4.1. A two-part extension of the known class

Taking both \(\mathcal C_i\) to be the \(Q_t\)-free class gives the following.

## Corollary 4.1

For fixed \(t\), Independent Set is FPT on graphs supplied with a partition \(A\dot\cup B\) such that

1. \(G[A]\) and \(G[B]\) are \(Q_t\)-free; and
2. no \(t\)-clique in \(A\) is anticomplete to a \(t\)-clique in \(B\).

This holds without assuming that the whole graph is \(H_t\)-free.

The supplied partition is important: this corollary does not assert an algorithm for finding such a partition in an arbitrary graph.

This hypothesis is not merely bounded deletion distance to the known class. For \(t\ge2\), let
\[
G_r=Q_t^1*\cdots *Q_t^r
\]
be the complete join of \(r\) copies of \(Q_t\). Let \(A\) contain the singleton endpoint from each copy and let \(B=V(G_r)\setminus A\).

Then:

- \(A\) is a clique.
- \(G[B]\) is \(Q_t\)-free. Indeed, it is a complete join of graphs on \(3t\) vertices, and \(\overline{Q_t}\) is connected, so an induced \(Q_t\) cannot span two join factors.
- Every \(t\)-subset of \(A\) uses at least two copies. No vertex of \(B\) is anticomplete to it, so condition \(\mathsf D_t\) holds.
- \(G_r\) is \(H_t\)-free: \(\overline{H_t}\) is connected, so an induced \(H_t\) would have to lie in one factor, which has only \(3t+1<4t\) vertices.
- The \(Q_t\)-deletion distance is exactly \(r\): the original \(r\) copies give the lower bound, and deleting their singleton endpoints gives the upper bound.

These particular examples are easy by complete-join decomposition. Their purpose is to distinguish the gluing hypothesis from a bounded-modulator hypothesis.

## 4.2. An anchored special case with no supplied partition

The forbidden graph itself can force condition \(\mathsf D_t\).

## Corollary 4.2

Fix \(t\). Independent Set is FPT on the following recognizable subclass of \(H_t\)-free graphs.

There exist anticomplete \(t\)-cliques \(U,V\) such that the remaining vertices partition into \(X,Y\), where

\[
\begin{array}{c|cc}
 & U & V\\ \hline
X & \text{complete} & \text{anticomplete}\\
Y & \text{complete} & \text{complete},
\end{array}
\]
and both \(G[X]\) and \(G[Y]\) are \(Q_t\)-free.

### Proof

Suppose \(C_X\subseteq X\) and \(C_Y\subseteq Y\) were anticomplete \(t\)-cliques. Then
\[
C_X,\ U,\ C_Y,\ V
\]
would be the four consecutive clique bags of an induced \(H_t\). Thus the cut \(X\dot\cup Y\) satisfies \(\mathsf D_t\).

Every independent set uses at most one vertex from each of \(U,V\). Enumerate its intersection \(S\) with \(U\cup V\); there are \((t+1)^2\) possibilities. For each, apply Corollary 4.1 to
\[
G-(U\cup V\cup N_G(S))
\]
with target \(k-|S|\). Its two parts inherit \(Q_t\)-freeness and condition \(\mathsf D_t\).

The anchors can be found by enumerating disjoint \(t\)-sets \(U,V\). Their adjacency conditions can be checked directly, and \(Q_t\)-freeness of the resulting parts can be tested by enumerating \((3t+1)\)-sets. All of this is polynomial for fixed \(t\). \(\square\)

For \(t\ge2\), the graph \(Q_t\) itself belongs to this anchored subclass: take its second and fourth bags as \(U,V\). Thus combining this corollary with the source theorem gives a strict, recognizable extension of the source’s class, albeit a limited one.

# 5. A stronger obstruction to bounded-distance bootstrapping

The previous attempt exhibited unbounded \(Q_t\)-packing in no-instances whose complements were connected. The following construction shows that neither primeness nor arbitrarily high complement connectivity repairs this approach.

## Theorem 5.1

For every \(t\ge2\) and positive integers \(r,h\), there is a graph \(G\) such that

1. \(G\) is \(H_t\)-free;
2. \(\alpha(G)=2\);
3. \(G\) is prime;
4. \(\kappa(\overline G)\ge h\);
5. \(G\) contains \(r\) vertex-disjoint induced copies of \(Q_t\).

In particular, the \(Q_t\)-deletion distance is at least \(r\), even under all four preceding restrictions.

## 5.1. Complement notation

Let \(P^I(a,b,c,d)\) denote a four-vertex path whose vertices are replaced by independent sets of the indicated sizes. Complementing the clique-substituted paths and reordering their bags gives
\[
F_t:=\overline{H_t}\cong P^I(t,t,t,t),
\]
and
\[
B_t:=\overline{Q_t}\cong P^I(t,1,t,t).
\]

The graph \(B_t\) is bipartite, with bipartition sizes \(2t\) and \(t+1\), and has \(3t+1\) vertices.

## 5.2. Construction

Let \(Q_d\) be the \(d\)-dimensional hypercube. Choose
\[
d\ge \max\{h,3,r(19t+7)\}.
\]

Choose pairwise disjoint sets
\[
W_1,\ldots,W_r\subseteq V(Q_d)
\]
such that each \(W_i\) contains \(2t\) even-parity vertices and \(t+1\) odd-parity vertices, and every two distinct vertices in
\[
W=\bigcup_i W_i
\]
have Hamming distance at least five.

Here is an explicit choice. Allocate disjoint coordinate blocks:

- one block of size six for each required even-parity vertex;
- one block of size seven for each required odd-parity vertex.

Use the indicator vector of each block as the corresponding vertex. The number of coordinates required is
\[
r\bigl(6(2t)+7(t+1)\bigr)=r(19t+7),
\]
and distinct chosen vectors have Hamming distance at least twelve.

Starting from \(Q_d\), add edges inside each \(W_i\) so that \(J[W_i]\cong B_t\), respecting parity as its bipartition. Add no other edges. This is possible because each \(W_i\) was independent in the hypercube.

Finally, set
\[
G=\overline J.
\]

## 5.3. Common-neighbor control

We claim:

> If two distinct vertices of \(J\) have more than two common neighbors, they belong to the same \(W_i\). Moreover, two vertices in the same \(W_i\) have all their common neighbors inside \(W_i\). \(\tag{8}\)

Recall that two distinct hypercube vertices have at most two common neighbors.

- **Neither vertex is in \(W\).** Their neighborhoods were unchanged, so the claim follows from the hypercube property.

- **Exactly one vertex is in \(W\).** Say \(u\in W\) and \(v\notin W\). Vertex \(v\) is adjacent in the hypercube to at most one selected vertex: two such neighbors would be at Hamming distance two. Thus adding edges at \(u\) creates at most one additional common neighbor.

  Also, such an additional common neighbor cannot coexist with an old common neighbor. If \(w\in W\setminus\{u\}\) is newly adjacent to \(u\), \(wv\) is a hypercube edge, and \(z\) is an old common neighbor of \(u,v\), then
  \[
  u-z-v-w
  \]
  is a hypercube walk of length three, contradicting the distance condition on \(W\). Hence the common-neighbor count is still at most two.

- **Both vertices are in \(W\).** Their old neighborhoods are disjoint and lie outside \(W\). All their new neighbors lie in their own designated sets \(W_i\). Thus vertices in different designated sets have no common neighbors, and vertices in the same set have common neighbors only within that set.

This proves (8).

## 5.4. Excluding \(F_t\)

Suppose \(J\) contained an induced \(F_t\), with consecutive independent bags
\[
A,B,C,D,
\]
each of size \(t\).

Choose distinct \(b,b'\in B\). They have all \(2t\) vertices of \(A\cup C\) as common neighbors. Since \(2t>2\), property (8) puts \(b,b'\) in one set \(W_i\), and then
\[
A\cup C\subseteq W_i.
\]

Choose distinct \(c,c'\in C\). Their common neighbors include \(B\cup D\), and property (8) now implies
\[
B\cup D\subseteq W_i.
\]
Thus the entire copy would lie in \(W_i\), impossible because
\[
|W_i|=3t+1<4t.
\]

Therefore \(J\) is \(F_t\)-free, so \(G\) is \(H_t\)-free.

## 5.5. Independence number, connectivity, and packing

The graph \(J\) is bipartite and has edges. Hence
\[
\alpha(G)=\omega(J)=2.
\]

It contains \(Q_d\) as a spanning subgraph, so
\[
\kappa(J)\ge \kappa(Q_d)=d\ge h.
\]

For completeness, the lower bound \(\kappa(Q_d)\ge d\) follows by induction. View \(Q_d\) as two copies of \(Q_{d-1}\) joined by a perfect matching, and delete fewer than \(d\) vertices. If each layer loses at most \(d-2\) vertices, each remains connected by induction, and a matching edge survives. Otherwise all deleted vertices lie in one layer, and every surviving vertex in that layer has a matching neighbor in the intact layer.

Finally,
\[
G[W_i]\cong Q_t
\]
for every \(i\). These copies are vertex-disjoint, so every \(Q_t\)-deletion set has size at least \(r\).

## 5.6. Primeness

First, \(J\) has no two vertices with equal open neighborhoods.

- For a pair not contained in one \(W_i\), property (8) bounds its common-neighbor count by two, whereas every vertex has degree at least \(d\ge3\).
- For a pair within one \(W_i\), all common neighbors lie in \(W_i\), but each vertex retains hypercube neighbors outside \(W\).

Now consider a proper nontrivial module \(M\) in the connected bipartite graph \(J\).

If \(M\) meets both sides of the bipartition, no outside vertex can be complete to \(M\), because it lies on the same side as some vertex of \(M\). The module condition would therefore make \(M\) anticomplete to its complement, contradicting connectivity.

Thus \(M\) lies on one side of the bipartition. Its vertices must consequently have equal open neighborhoods, which was just ruled out. Hence \(J\) is prime.

Modules are preserved by complementation, so \(G\) is prime as well. This completes the proof. \(\square\)

### Consequence

There is no bound
\[
\tau_{Q_t}(G)\le f(k,t)
\]
for \(H_t\)-free no-instances, even after restricting to prime graphs whose complements have arbitrarily high vertex connectivity.

These examples also have no clique separator in the complement: \(J\) is bipartite, so every clique has size at most two, while \(\kappa(J)\ge3\).

They are **not counterexamples to FPT**. Indeed, their independence number is two. They are counterexamples only to the proposed structural bound that would permit a bounded-modulator lift of the known result.

# 6. What remains missing

The gluing theorem supplies an algorithm once the pieces already belong to hereditary FPT classes. The \(H_t\)-free condition forces the required dense-cut property for the nested anchor profiles in Corollary 4.2.

What is not proved is a decomposition theorem ensuring that arbitrary \(H_t\)-free graphs can be reduced to such pieces.

In particular, it would be circular to apply Theorem 3.1 with both classes equal to the entire \(H_t\)-free class. Nor can one freely iterate the gluing argument to unbounded depth: its polynomial exponent increases by \(t\) at each application. An iteration whose depth depends on \(k\) would generally give an XP bound rather than an FPT bound.

Thus the rigorous outcome is:

- an FPT closure theorem and a consequent special case;
- a strengthened obstruction to bounded-distance, bounded-separator, and elementary modular bootstrapping;
- no proof of the full conjecture and no hardness reduction against it.