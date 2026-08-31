```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I do not resolve the conjecture, but prove an exact averaging obstruction, settle all abelian Cayley digraphs, and prove Hamiltonicity for several periodic vertex-transitive classes.",
  "would_publish": false,
  "caveats": "The general aperiodic non-Cayley case and the range sqrt(n)<c<=n/2 remain open; standard finite loopless simple-digraph conventions are assumed."
}
```

# 1. Statement and conventions

Let \(D\) be a finite loopless simple digraph of order \(n\), and let \(c(D)\) denote its directed circumference. The question is whether, whenever \(D\) is connected and vertex-transitive, every two directed cycles of length \(c(D)\) have a common vertex.

Here “connected” may mean connected after forgetting orientations. This distinction is immaterial:

**Lemma 1.1.** A weakly connected finite vertex-transitive digraph is strongly connected.

**Proof.** Automorphisms permute the strongly connected components. By vertex-transitivity, they act transitively on those components. The condensation is therefore a finite vertex-transitive acyclic digraph. A finite acyclic digraph has a source; transitivity would then make every vertex a source, so the condensation has no arcs. Weak connectivity forces it to have only one vertex. ∎

Thus throughout, \(D\) may be regarded as strongly connected.

# 2. An exact averaging obstruction

The following observation sharply constrains any affirmative solution.

**Lemma 2.1 (transitive averaging).**  
Let a finite group \(\Gamma\) act transitively on a set \(V\) of size \(n\). For \(A,B\subseteq V\),
\[
 \frac1{|\Gamma|}\sum_{g\in\Gamma}|gA\cap B|
 =\frac{|A||B|}{n}.
\]

**Proof.** Count triples \((g,a,b)\) with \(a\in A\), \(b\in B\), and \(ga=b\). For every ordered pair \((a,b)\), exactly \(|\Gamma|/n\) elements of \(\Gamma\) send \(a\) to \(b\). ∎

Apply this with \(A=B=V(C)\), where \(C\) is a longest directed cycle of length \(c\).

**Proposition 2.2.**  
If \(c>1\) and
\[
 n\ge c^2,
\]
then \(D\) contains two vertex-disjoint longest directed cycles.

**Proof.** Let \(\mathcal O=\{gV(C):g\in\Gamma\}\), where \(\Gamma\) is any transitive automorphism group, and put \(t=|\mathcal O|\). Lemma 2.1 gives
\[
 \sum_{A\in\mathcal O}|A\cap V(C)|=\frac{tc^2}{n}\le t.
\]
One member of the orbit is \(V(C)\) itself and contributes \(c>1\). If every other member met \(V(C)\), the sum would be at least
\[
 c+(t-1)>t,
\]
a contradiction. Hence some automorphic image of \(C\) is disjoint from \(C\). ∎

There is also a quantitative form. If \(z\) members of \(\mathcal O\) are disjoint from \(C\), then
\[
 \frac{tc^2}{n}
 \ge c+(t-z-1),
\]
and consequently
\[
 z\ge t+c-1-\frac{tc^2}{n}.
\]
In particular, if \(n=c^2\), there are at least \(c-1\) distinct members of the orbit disjoint from \(C\).

This has two immediate consequences.

1. An affirmative answer to the conjecture would imply the strict universal bound
   \[
   c(D)^2>n.
   \]
   Thus the intersection conjecture is stronger than a \(\sqrt n\)-circumference theorem.

2. Conversely, any connected vertex-transitive digraph with
   \[
   c(D)\le \sqrt n
   \]
   is automatically a counterexample.

At the other end, if \(c>n/2\), any two \(c\)-vertex subsets intersect. Hence the genuinely unresolved numerical range is
\[
 \sqrt n<c\le \frac n2,
\]
together with the problem of excluding \(c\le\sqrt n\) altogether.

The \(\Omega(n^{1/3})\) lower bound quoted in the supplied source is insufficient for this purpose, while no construction supplied in the question has circumference at most \(\sqrt n\).

# 3. Abelian Cayley digraphs satisfy the conjecture

Here is a substantial positive special case.

## 3.1 A normal-chain Cayley lemma

Write \(\operatorname{Cay}(G,S)\) with arcs
\[
 x\longrightarrow xs,\qquad s\in S.
\]

**Theorem 3.1.**  
Suppose that \(G\) has a strict chain
\[
 1=G_0<G_1<\cdots<G_d=G
\]
and elements \(s_i\in S\) such that
\[
 G_i=\langle G_{i-1},s_i\rangle
 \quad\text{and}\quad
 G_{i-1}\triangleleft G_i
\]
for every \(i\). Then \(\operatorname{Cay}(G,S)\) has a directed cycle of length strictly greater than \(|G|/2\).

**Proof.** We first construct, inductively, a Hamilton directed path in
\[
 \operatorname{Cay}(G_i,\{s_1,\dots,s_i\}).
\]

For \(i=1\), the powers of \(s_1\) give such a path. Suppose that
\[
 P=(1=p_0,p_1,\dots,p_{h-1}=e)
\]
is a Hamilton path in \(G_{i-1}\), where \(h=|G_{i-1}|\). Put
\[
 q=[G_i:G_{i-1}]
\]
and define
\[
 x_0=1,\qquad x_{k+1}=x_kes_i.
\]
Concatenate the \(q\) translated copies
\[
 x_kP=(x_kp_0,\dots,x_kp_{h-1}),
 \qquad 0\le k<q.
\]
The endpoint \(x_ke\) of one copy is joined to the start
\[
 x_{k+1}=x_kes_i
\]
of the next by an \(s_i\)-arc.

Because \(G_{i-1}\triangleleft G_i\), in the quotient one has
\[
 x_{k+1}G_{i-1}=x_kG_{i-1}\,s_iG_{i-1}.
\]
Thus the \(x_kG_{i-1}\) are the \(q\) distinct cosets of \(G_{i-1}\). The concatenation is therefore a Hamilton path in \(G_i\).

Apply this at the final step. Let \(H=G_{d-1}\), \(h=|H|\), \(q=[G:H]\), and let \(E=x_{q-1}e\) be the endpoint of the constructed Hamilton path in \(G\). There is an arc
\[
 E\longrightarrow Es_d=x_q.
\]
Moreover, \(x_qH=H\), so \(x_q\in H\), and therefore \(x_q\) occurs in the first \(H\)-block of the Hamilton path. If it occurs at position \(j\), then \(0\le j\le h-1\), and the suffix beginning at \(x_q\), followed by the arc \(E\to x_q\), is a directed cycle of length
\[
 |G|-j\ge |G|-h+1.
\]
Since the chain is strict, \(q\ge2\), so \(h\le |G|/2\). Hence this cycle has length at least
\[
 |G|-h+1>\frac{|G|}{2}.
\]
If \(d=1\), the Cayley digraph is Hamiltonian directly. ∎

**Corollary 3.2.**  
Every connected Cayley digraph on a finite abelian group has circumference greater than half its order. Consequently, every two longest directed cycles intersect.

**Proof.** Choose an inclusion-minimal generating subset
\[
 \{s_1,\dots,s_d\}\subseteq S.
\]
Every prefix generates a strictly larger subgroup, and all subgroups of an abelian group are normal. Theorem 3.1 applies. Two subsets of size greater than \(n/2\) must intersect. ∎

This includes all connected directed circulants and, more generally, all vertex-transitive digraphs admitting a regular abelian automorphism group.

# 4. Periodic vertex-transitive digraphs with small cyclic classes

Let \(h\) be the period of the strongly connected digraph \(D\), namely the gcd of the lengths of its directed closed walks. For \(h\ge2\), there is the standard cyclic decomposition
\[
 V(D)=V_0\dot\cup\cdots\dot\cup V_{h-1},
\]
where every arc goes from \(V_i\) to \(V_{i+1}\), indices being taken modulo \(h\).

Vertex-transitivity implies that all classes have the same size \(m=n/h\). It also implies constant indegree and outdegree; these constants are equal, say \(d\). Thus the bipartite digraph from \(V_i\) to \(V_{i+1}\) is \(d\)-regular.

## 4.1 Monodromy of chosen matchings

Choose in every slice a perfect matching
\[
 \sigma_i:V_i\longrightarrow V_{i+1}
\]
consisting of arcs. The union of these matchings is a spanning directed cycle factor. Its components correspond to the cycles of
\[
 \Pi=\sigma_{h-1}\sigma_{h-2}\cdots\sigma_0
\]
on \(V_0\). In particular, the selected matchings form a Hamilton cycle precisely when \(\Pi\) is an \(m\)-cycle.

## 4.2 A product-of-derangements lemma

**Lemma 4.1.** For \(m\ge4\), every permutation in \(S_m\) is a product of two derangements.

**Proof.** Given \(\pi\in S_m\), consider the bipartite graph in which row \(i\) may be matched to every column except \(i\) and \(\pi(i)\). We claim that this graph has a perfect matching \(\beta\).

Every row has degree at least \(m-2\). Hall's condition is immediate for sets of at most \(m-2\) rows. If a set contains at least \(m-1\) rows, every column has an allowed incident edge because a column is forbidden in at most two rows, while \(m-1\ge3\). Hence Hall's condition holds.

Thus
\[
 \beta(i)\ne i,\qquad \beta(i)\ne\pi(i)
\]
for every \(i\). Put \(\alpha=\pi\beta^{-1}\). Then \(\beta\) is a derangement, and \(\alpha(y)=y\) would imply, for \(i=\beta^{-1}(y)\),
\[
 \pi(i)=\beta(i),
\]
which is forbidden. Thus \(\alpha\) is also a derangement and \(\pi=\alpha\beta\). ∎

## 4.3 Hamiltonicity theorem

**Theorem 4.2.**  
Suppose \(D\) is a finite vertex-transitive digraph of period \(h\ge2\), cyclic class size \(m\), and outdegree \(d\). Then \(D\) is Hamiltonian in each of the following cases:
\[
 d=1,\qquad d=m,\qquad d=m-1.
\]
Consequently, \(D\) is Hamiltonian whenever \(m\le3\).

**Proof.**

- If \(d=1\), then \(D\) is a disjoint union of directed cycles. Strong connectivity makes it one Hamilton cycle.

- If \(d=m\), every possible arc from \(V_i\) to \(V_{i+1}\) is present. We may choose the matchings so that their monodromy is any prescribed permutation of \(V_0\), in particular an \(m\)-cycle.

It remains to consider \(d=m-1\). In each slice, the missing arcs form a perfect matching
\[
 f_i:V_i\longrightarrow V_{i+1}.
\]
Choose identifications along the \(f_i\)'s. If
\[
 F=f_{h-1}\cdots f_0
\]
is the resulting permutation of \(V_0\), then every allowed perfect matching in the \(i\)-th slice has the form \(f_i\delta_i\), where \(\delta_i\) is a derangement. Hence the possible monodromies are
\[
 F\delta_{h-1}\cdots\delta_0.
\]

If \(m\ge4\), Lemma 4.1 says that products of two derangements fill \(S_m\). Since \(h\ge2\), the possible monodromies therefore include every permutation of \(V_0\), and in particular an \(m\)-cycle.

For \(m=2\), the case \(d=m-1\) is already \(d=1\).

It remains only \(m=3,d=2\). Here every \(\delta_i\) is one of the two \(3\)-cycles and is therefore even. We show that \(F\) is even.

Let \(\Gamma_0\) be the subgroup of automorphisms fixing every cyclic class setwise. It acts transitively on \(V_0\): an automorphism sending one vertex of \(V_0\) to another cannot shift the cyclic classes. If \(\gamma_i\) is the restriction of \(\gamma\in\Gamma_0\) to \(V_i\), invariance of the uniquely missing matching gives
\[
 \gamma_{i+1}f_i=f_i\gamma_i.
\]
After composition around the cyclic decomposition,
\[
 \gamma_0F=F\gamma_0.
\]
Thus the centralizer of \(F\) in \(S_3\) contains a transitive subgroup. This is impossible when \(F\) is a transposition, because the centralizer of a transposition fixes the third point. Hence \(F\) is even.

All possible monodromies are consequently even. Fix all choices except one \(\delta_i\), and vary that \(\delta_i\) between the two \(3\)-cycles. This produces two distinct even monodromies. At most one is the identity, so at least one is a \(3\)-cycle. The corresponding cycle factor is a Hamilton cycle. ∎

For \(h=1\) and \(n\le3\), Hamiltonicity follows directly from vertex-transitivity and regularity. Thus the “cyclic class size at most three” conclusion also holds without assuming \(h\ge2\).

# 5. Consequences and remaining gap

The results above establish the desired intersection property in the following cases:

1. \(c(D)>n/2\), trivially;
2. all connected abelian Cayley digraphs, and more generally Cayley digraphs admitting the normal-chain generating sequence of Theorem 3.1;
3. periodic vertex-transitive digraphs whose cyclic classes have size at most three;
4. periodic vertex-transitive digraphs with outdegree \(1\), \(m-1\), or \(m\), where \(m\) is the cyclic class size.

They also show that any affirmative solution must prove the new universal lower bound
\[
 c(D)>\sqrt n.
\]
Conversely, finding a vertex-transitive digraph with \(c(D)\le\sqrt n\) would immediately disprove the conjecture by automorphic averaging.

What remains untreated is substantial: in particular, general aperiodic vertex-transitive digraphs without a regular abelian subgroup, and periodic digraphs with larger cyclic classes and intermediate outdegree. No explicit counterexample or complete proof is obtained here.