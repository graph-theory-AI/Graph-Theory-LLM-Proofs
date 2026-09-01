```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted upper bound remains open, but one obtains an explicit lower bound Ω_d(n^{3-2/(d+1)}) and the conjectured exponent for hosts whose link graphs have small inclusion width.",
  "would_publish": false,
  "caveats": "No unrestricted n^{3-c/d} upper bound is proved; novelty of the elementary structural lemma is not asserted, and d=1 is exceptional."
}
```

## 1. Statement and interpretation

Let \(d\ge 2\), let \(L\) be a Latin square of order \(d\), and let \(H_L\) be the associated \(3\)-partite \(3\)-graph. Its \(1\)-skeleton is \(K_{d,d,d}\): every two vertices in different vertex classes lie together in exactly one edge of \(H_L\).

The meaningful uniform interpretation of the conjecture is that there are absolute constants \(c,C>0\) such that, for every \(d\) and every \(L\),
\[
 n^{3-C/d}\lesssim_d \operatorname{ex}(n,H_L)
 \lesssim_d n^{3-c/d}.
\]
The unrestricted upper bound of this form is not proved below.

I give:

1. an explicit general lower bound
   \[
   \operatorname{ex}(n,H_L)=\Omega_d\!\left(n^{3-\frac{2}{d+1}}\right);
   \]
2. a structural upper bound in terms of the inclusion width of the link graphs;
3. as a consequence, the conjectured \(3-\Theta(1/d)\) exponent for nested-link hosts, and more generally for hosts of sufficiently small link width.

Throughout, constants may depend on \(d\).

---

## 2. A cylindrical construction

Write \(z_d(N)=\operatorname{ex}(K_{N,N},K_{d,d})\).

### Proposition 2.1

For every Latin square \(L\) of order \(d\) and \(N\ge d\),
\[
\operatorname{ex}(3N,H_L)\ge N z_d(N).
\]

### Proof

Let \(G\subseteq A\times B\) be a \(K_{d,d}\)-free bipartite graph with
\[
|A|=|B|=N,\qquad e(G)=z_d(N).
\]
Let \(C\) be a set of size \(N\), and define the tripartite \(3\)-graph
\[
\mathcal G_G=\{(a,b,c):ab\in E(G),\ c\in C\}.
\]
Thus every \(c\in C\) has the same link graph \(G\), and
\[
e(\mathcal G_G)=N e(G)=N z_d(N).
\]

Suppose that \(\mathcal G_G\) contained \(H_L\). Since the \(1\)-skeleton of \(H_L\) is \(K_{d,d,d}\), any embedding into the tripartite host \(\mathcal G_G\) must send the three vertex classes of \(H_L\) to \(A,B,C\), up to a permutation of the classes. Indeed, the preimage of each host class is an independent set in \(K_{d,d,d}\), and its proper \(3\)-coloring is unique up to permuting the three classes.

Whichever two classes are sent to \(A\) and \(B\), all \(d^2\) pairs between their images must be edges of \(G\). This gives a \(K_{d,d}\) in \(G\), a contradiction. Hence \(\mathcal G_G\) is \(H_L\)-free. ∎

In fact, for these cylindrical hosts there is an exact equivalence:
\[
\mathcal G_G\text{ contains }H_L
\quad\Longleftrightarrow\quad
G\text{ contains }K_{d,d}.
\]
The reverse implication follows because a \(K_{d,d}\) in \(G\), together with any \(d\) vertices of \(C\), spans a complete \(K^{(3)}_{d,d,d}\), which contains \(H_L\).

---

## 3. Explicit probabilistic lower exponent

### Lemma 3.1

For fixed \(d\ge2\),
\[
z_d(N)=\Omega_d\!\left(N^{2-\frac{2}{d+1}}\right).
\]

### Proof

Take a random bipartite graph with two parts of size \(N\), including each edge independently with probability
\[
p=\gamma_d N^{-2/(d+1)},
\]
where \(\gamma_d>0\) is sufficiently small.

The expected number of edges is
\[
\mathbb E e(G)=\gamma_d N^{2-\frac{2}{d+1}}.
\]
The expected number \(X\) of copies of \(K_{d,d}\) is at most
\[
\binom Nd^2 p^{d^2}
 \le \frac{\gamma_d^{d^2}}{(d!)^2}
 N^{2d-\frac{2d^2}{d+1}}
 =
 \frac{\gamma_d^{d^2}}{(d!)^2}
 N^{2-\frac{2}{d+1}}.
\]
Choose \(\gamma_d\) so that \(\mathbb E X\le \frac12\mathbb E e(G)\). Some realization then satisfies
\[
e(G)-X\ge \tfrac12\gamma_d N^{2-\frac{2}{d+1}}.
\]
Deleting one edge from each remaining \(K_{d,d}\) uses at most \(X\) deletions and leaves a \(K_{d,d}\)-free graph of the asserted size. ∎

Combining Proposition 2.1 and Lemma 3.1 gives:

### Corollary 3.2

For every \(d\ge2\) and every Latin square \(L\) of order \(d\),
\[
\boxed{\operatorname{ex}(n,H_L)
 =\Omega_d\!\left(n^{3-\frac{2}{d+1}}\right).}
\]

This is denser than the direct random-hypergraph alteration bound
\(\Omega_d(n^{3-3/(d+1)})\).

For \(d=2\), the cylinder construction can be improved using a projective-plane incidence graph. Such a graph is \(C_4=K_{2,2}\)-free and has \(\Theta(N^{3/2})\) edges, giving
\[
\operatorname{ex}(n,H_L)=\Omega(n^{5/2})
\qquad(d=2).
\]

---

## 4. Baseline unrestricted upper bound

Since
\[
H_L\subseteq K^{(3)}_{d,d,d},
\]
one has
\[
\operatorname{ex}(n,H_L)
 \le \operatorname{ex}\bigl(n,K^{(3)}_{d,d,d}\bigr)
 =O_d\!\left(n^{3-\frac1{d^2}}\right).
\]

For completeness, the exponent follows from the standard double-convexity argument. In a balanced tripartite host with parts \(A,B,C\) of size \(N\), let \(G_c\) be the bipartite link of \(c\) on \(A,B\). If the host is \(K^{(3)}_{d,d,d}\)-free, every fixed \(K_{d,d}\) on \(A,B\) belongs to at most \(d-1\) of the links, so
\[
\sum_{c\in C} \#K_{d,d}(G_c)
 \le (d-1)\binom Nd^2.
\]
For a link with \(e_c\gg_d N^{2-1/d}\), two applications of convexity give
\[
\#K_{d,d}(G_c)
 \gg_d \frac{e_c^{d^2}}{N^{2d^2-2d}}.
\]
Applying convexity once more over \(c\in C\) yields
\[
m^{d^2}\ll_d N^{3d^2-1},
\]
and hence \(m=O_d(N^{3-1/d^2})\). A random tripartition retains a constant fraction of the edges of an arbitrary \(3\)-graph.

Thus the presently relevant gap is
\[
\Omega_d\!\left(n^{3-\frac{2}{d+1}}\right)
 \le \operatorname{ex}(n,H_L)
 \le O_d\!\left(n^{3-\frac1{d^2}}\right).
\]

---

## 5. A link-poset upper bound

Let \(\mathcal G\subseteq A\times B\times C\) be a tripartite \(3\)-graph. For \(c\in C\), write
\[
G_c=\{ab:(a,b,c)\in E(\mathcal G)\}
\]
for its link graph on \(A,B\).

Define \(q_C(\mathcal G)\) to be the minimum number of subfamilies into which \(\{G_c:c\in C\}\) can be partitioned so that within each subfamily the link graphs are linearly ordered by inclusion. Equivalently, after harmlessly ordering repeated links, this is the width of the inclusion poset by Dilworth's theorem.

Let
\[
z_d(A,B)=\max\{e(G):G\subseteq A\times B,\ G\text{ is }K_{d,d}\text{-free}\}.
\]

### Theorem 5.1

If \(\mathcal G\) is \(H_L\)-free, then
\[
\boxed{
e(\mathcal G)
 \le (d-1)q_C(\mathcal G)\,|A||B|
      +|C|\,z_d(A,B).
}
\]

### Proof

Partition the links into \(q=q_C(\mathcal G)\) inclusion chains. Consider one chain
\[
G_{c_1}\supseteq G_{c_2}\supseteq\cdots\supseteq G_{c_s}.
\]

If \(s\ge d\), then \(G_{c_d}\) must be \(K_{d,d}\)-free. Indeed, if \(X\subseteq A\) and \(Y\subseteq B\), both of size \(d\), span a \(K_{d,d}\) in \(G_{c_d}\), then they span a \(K_{d,d}\) in each of
\[
G_{c_1},\ldots,G_{c_d}.
\]
Consequently, the host contains every triple in
\[
X\times Y\times\{c_1,\ldots,c_d\},
\]
which is a \(K^{(3)}_{d,d,d}\) and therefore contains \(H_L\), a contradiction.

It follows that every link from the \(d\)-th onward has at most \(z_d(A,B)\) edges. The first \(d-1\) links have at most \(|A||B|\) edges each. Thus the contribution of this chain is at most
\[
(d-1)|A||B|+s\,z_d(A,B).
\]
This also holds when \(s<d\). Summing over all \(q\) chains proves the result. ∎

For balanced parts, the usual \(K_{d,d}\) counting bound gives
\[
z_d(N,N)=O_d(N^{2-1/d}).
\]
Therefore:

### Corollary 5.2

If \(|A|=|B|=|C|=N\) and
\[
q_C(\mathcal G)\le N^{1-1/d},
\]
then every \(H_L\)-free \(\mathcal G\) satisfies
\[
e(\mathcal G)=O_d(N^{3-1/d}).
\]

In particular, this holds if the link graphs \(\{G_c:c\in C\}\) are themselves nested under inclusion.

Together with the cylindrical construction, the extremal number within the nested-link class satisfies
\[
\Omega_d\!\left(N^{3-\frac{2}{d+1}}\right)
 \le \operatorname{ex}_{\rm nested}(N,H_L)
 \le O_d(N^{3-1/d}).
\]
Thus the conjectured \(3-\Theta(1/d)\) dependence is valid for this structural class of hosts.

For \(d=2\), the projective-plane construction and the \(C_4\)-free upper bound yield the sharper statement
\[
\operatorname{ex}_{\rm nested}(N,H_L)=\Theta(N^{5/2}).
\]

Theorem 5.1 can of course be applied with any of the three vertex classes playing the role of \(C\).

---

## 6. What remains missing

The link-poset estimate identifies a genuine obstruction but does not control it. Rearranging Theorem 5.1 in the balanced case gives
\[
q_C(\mathcal G)
 \ge
 \frac{e(\mathcal G)-N z_d(N)}{(d-1)N^2}.
\]
Hence an \(H_L\)-free host with
\[
e(\mathcal G)\gg N^{3-1/d}
\]
must have a family of
\(\Omega_d(e(\mathcal G)/N^2)\) pairwise incomparable links. The same conclusion holds in all three flattenings.

Arbitrary collections of \(N\) subsets of an \(N^2\)-element universe can be complete antichains, so inclusion theory alone gives no further bound. The unresolved step is to exploit the special fact that these incomparable subsets are bipartite link graphs and to force \(d\) different links to supply the \(d\) one-factors prescribed by \(L\). No argument establishing this at density \(N^{-c/d}\) is provided here.

Finally, for \(d=1\), \(H_L\) is a single edge and \(\operatorname{ex}(n,H_L)=0\); the conjecture should therefore be read for \(d\ge2\), or as a statement about the dependence on large \(d\).