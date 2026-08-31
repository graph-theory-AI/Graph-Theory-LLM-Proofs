```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The converse holds for every uniformly K_{t,t}-free class, without any subgraph-closure assumption.",
  "would_publish": false,
  "caveats": "The dense case remains open; novelty was not literature-checked, and the standard monadic FO-transduction convention is assumed."
}
```

## Partial resolution: uniformly biclique-free classes

I use the standard notion of a monadic first-order transduction: one may first add finitely many arbitrary unary predicates, then apply a one-dimensional FO interpretation, possibly with finitely many copies. The proof below uses no copying.

For a graph \(G\) and \(A\subseteq V(G)\), write
\[
\mathcal N_G(A)=\{N_G(v)\cap A:v\in V(G)\}.
\]
Whether vertices of \(A\) themselves are included in this definition is immaterial below, since all counted witnesses lie outside \(A\).

### Theorem

Let \(\mathcal C\) be a graph class for which there is a fixed \(t\ge 2\) such that every \(G\in\mathcal C\) is \(K_{t,t}\)-free. Suppose every first-order transduction of \(\mathcal C\) has linear neighbourhood complexity. Then \(\mathcal C\) has bounded expansion, and hence bounded merge-width.

Consequently, the conjecture is true for uniformly \(K_{t,t}\)-free classes.

No hereditary or subgraph-closure hypothesis is needed.

---

## 1. Linear traces plus biclique exclusion force bounded degeneracy

We first need a two-sided sampling lemma.

### Lemma 1

Let \(G\) be \(K_{t,t}\)-free and suppose that, for every nonempty \(A\subseteq V(G)\),
\[
|\mathcal N_G(A)|\le a|A|.
\tag{1}
\]
There is a constant \(D=D(a,t)\) such that the following is impossible: two disjoint sets \(X,Y\subseteq V(G)\) with every vertex of \(X\) having at least \(D\) neighbours in \(Y\), and every vertex of \(Y\) having at least \(D\) neighbours in \(X\).

#### Proof

Suppose the common lower degree is \(D\ge 2t\). Choose a random subset \(A\subseteq X\) by retaining each vertex independently with probability
\[
p=\frac{2t}{D}.
\]

For \(y\in Y\), the random variable \(|N_G(y)\cap A|\) has mean at least \(2t\). By a standard Chernoff estimate,
\[
\Pr\bigl(|N_G(y)\cap A|\ge t\bigr)
 \ge q_t:=1-e^{-t/4}>0.
\tag{2}
\]

For a fixed realization of \(A\), put
\[
Y_A=\{y\in Y:|N_G(y)\cap A|\ge t\}.
\]
Any fixed trace \(S=N_G(y)\cap A\) with \(|S|\ge t\) can occur for at most \(t-1\) vertices of \(Y\). Indeed, \(t\) vertices having the same such trace, together with any \(t\) vertices of \(S\), would form a \(K_{t,t}\). Hence, using (1),
\[
|Y_A|\le (t-1)|\mathcal N_G(A)|
       \le (t-1)a|A|.
\tag{3}
\]
This also holds when \(A=\varnothing\), since then \(Y_A=\varnothing\).

Taking expectations in (3) and using (2) gives
\[
q_t|Y|
 \le (t-1)a\,p|X|
 =\frac{2t(t-1)a}{D}|X|.
\]
Thus
\[
|Y|\le \frac{A_0}{D}|X|,
\qquad
A_0:=\frac{2t(t-1)a}{q_t}.
\tag{4}
\]
Repeating the argument with \(X\) and \(Y\) interchanged gives
\[
|X|\le \frac{A_0}{D}|Y|.
\tag{5}
\]
Multiplying (4) and (5) and cancelling \(|X||Y|>0\), we obtain \(D\le A_0\).

Thus one may take
\[
D(a,t)=\max\left\{2t,\frac{2t(t-1)a}{1-e^{-t/4}}\right\},
\]
up to harmless integer rounding. ∎

### Corollary 2

A uniformly \(K_{t,t}\)-free class with linear neighbourhood complexity is uniformly degenerate.

#### Proof

Let \(G\) belong to the class, and let \(F\subseteq G\) be any subgraph of minimum degree \(\delta\). Choose a cut \(X\cup Y=V(F)\) maximizing the number of crossing edges. Local optimality of the cut implies that every vertex has at least half of its \(F\)-neighbours across the cut. Therefore the bipartite graph formed by all \(G\)-edges between \(X\) and \(Y\) has minimum degree at least \(\delta/2\).

Lemma 1 bounds \(\delta/2\) by a constant depending only on \(a,t\). Hence every subgraph of every \(G\) has a bounded-degree vertex. Thus the class is uniformly \(d\)-degenerate for some \(d=d(a,t)\). In particular,
\[
|E(G[Z])|\le d|Z|
\tag{6}
\]
for every \(Z\subseteq V(G)\). ∎

Only the identity transduction has been used so far.

---

## 2. FO transductions detect bounded-length subdivisions

We now use the hypothesis for particular path-reading transductions.

Fix \(L\). Let \(H\) have a topological model in \(G\in\mathcal C\) in which every edge of \(H\) is represented by a path of length at most \(L\), all model paths having pairwise disjoint interiors. Let \(B\subseteq V(G)\) be the branch vertices, so
\[
|B|=|V(H)|=:n.
\]
For \(1\le \ell\le L\), let \(m_\ell\) be the number of model paths of length exactly \(\ell\).

We prove \(m_\ell=O_\ell(n)\).

### Paths of length one

Every length-one model edge is an edge of \(G[B]\). Therefore, by (6),
\[
m_1\le |E(G[B])|\le dn.
\tag{7}
\]

### Paths of a fixed length \(\ell\ge2\)

Let \(\mathcal P\) be the family of length-\(\ell\) model paths, and write \(m=|\mathcal P|\). If \(m<n\), there is nothing to prove, so assume \(m\ge n\).

Define the conflict graph \(J\) on \(\mathcal P\): two model paths are adjacent in \(J\) if some interior vertex of one is adjacent in \(G\) to some interior vertex of the other.

For \(\mathcal U\subseteq\mathcal P\), the union \(I_{\mathcal U}\) of their interiors has exactly
\[
(\ell-1)|\mathcal U|
\]
vertices. Every edge of \(J[\mathcal U]\) is witnessed by an edge of \(G[I_{\mathcal U}]\), and hence
\[
|E(J[\mathcal U])|
 \le |E(G[I_{\mathcal U}])|
 \le d(\ell-1)|\mathcal U|.
\]
It follows that \(J\) has degeneracy at most \(2d(\ell-1)\), and therefore is colourable with
\[
k_\ell:=2d(\ell-1)+1
\tag{8}
\]
colours. Choose a colour class \(\mathcal S\) with
\[
|\mathcal S|\ge \frac{m}{k_\ell}.
\tag{9}
\]
No edge of \(G\) joins interiors of two distinct paths in \(\mathcal S\).

For \(P\in\mathcal S\), define
\[
q(P)=
\bigl|\{b\in B: b\text{ has a neighbour in the interior of }P\}\bigr|.
\]
Since the interiors are disjoint,
\[
\sum_{P\in\mathcal S}q(P)
 \le e_G(B,I_{\mathcal S})
 \le d\bigl(n+(\ell-1)|\mathcal S|\bigr).
\tag{10}
\]
Because \(m\ge n\) and \(|\mathcal S|\ge m/k_\ell\),
\[
\frac n{|\mathcal S|}\le k_\ell.
\]
Thus the average value of \(q(P)\) over \(\mathcal S\) is at most
\[
d(k_\ell+\ell-1).
\]
By Markov's inequality, there is \(\mathcal S_0\subseteq\mathcal S\) with
\[
|\mathcal S_0|\ge \frac{|\mathcal S|}{2}
              \ge \frac{m}{2k_\ell}
\tag{11}
\]
and
\[
q(P)\le s_\ell:=\left\lceil2d(k_\ell+\ell-1)\right\rceil
\quad\text{for all }P\in\mathcal S_0.
\tag{12}
\]

### The path-reading transduction

Orient every path
\[
P=u x_1x_2\cdots x_{\ell-1}v
\]
in \(\mathcal S_0\) arbitrarily. Add unary predicates

- \(P_B\), marking the branch set \(B\);
- \(Q_i\), marking all vertices \(x_i\), for \(1\le i\le\ell-1\).

Consider the fixed FO transduction \(\mathsf T_\ell\) whose output domain is
\[
P_B\cup Q_1.
\]
It adds edges only between \(Q_1\) and \(P_B\). For \(\ell=2\), a vertex \(x\in Q_1\) is adjacent in the output to \(b\in P_B\) precisely when \(xb\in E(G)\).

For \(\ell\ge3\), define
\[
\theta_\ell(x,b):=
E(x,b)\ \lor\
\exists z_2\cdots z_{\ell-1}
\left(
 \bigwedge_{i=2}^{\ell-1}Q_i(z_i)
 \land E(x,z_2)
 \land\bigwedge_{i=2}^{\ell-2}E(z_i,z_{i+1})
 \land E(z_{\ell-1},b)
\right),
\tag{13}
\]
and join \(x\in Q_1\) to \(b\in P_B\) when \(\theta_\ell(x,b)\) holds.

This is a fixed monadic FO transduction depending only on \(\ell\). Since no edge of \(G\) joins interiors of distinct paths in \(\mathcal S_0\), any position-respecting chain in (13) remains inside a single model path. Consequently, for the representative \(x_1\) of a path \(P\),

1. its output neighbourhood in \(B\) contains the two endpoints of \(P\);
2. its output neighbourhood in \(B\) is contained in the set of branch vertices having a neighbour in the interior of \(P\).

By (12), this trace therefore has size at most \(s_\ell\).

Moreover, a fixed trace \(S\subseteq B\) can arise from at most
\[
\binom{s_\ell}{2}
\tag{14}
\]
members of \(\mathcal S_0\): the two endpoints of the corresponding edge of the simple graph \(H\) form a distinct unordered pair contained in \(S\).

Let \(c_\ell\) be the linear-neighbourhood-complexity constant for \(\mathsf T_\ell(\mathcal C)\). Taking \(A=B\) in the output graph gives
\[
\frac{|\mathcal S_0|}{\binom{s_\ell}{2}}
 \le |\mathcal N_{\mathsf T_\ell(G)}(B)|
 \le c_\ell n.
\]
Combining this with (11),
\[
m
 \le
2k_\ell\binom{s_\ell}{2}c_\ell n.
\tag{15}
\]

Thus \(m_\ell=O_\ell(n)\) for every \(\ell\ge2\).

Summing (7) and (15), for every fixed \(L\) there is \(C_L\) such that every graph \(H\) having a topological model in a member of \(\mathcal C\), with paths of length at most \(L\), satisfies
\[
|E(H)|\le C_L|V(H)|.
\tag{16}
\]

---

## 3. From (16) to bounded merge-width

The standard shallow-topological-minor characterization of bounded expansion says that a class has bounded expansion if and only if, for every fixed \(L\), densities of topological minors modeled by paths of length at most \(L\) are uniformly bounded. Equation (16) therefore proves that \(\mathcal C\) has bounded expansion.

The established inclusion
\[
\text{bounded expansion}\ \Longrightarrow\ \text{bounded merge-width}
\]
then proves the desired converse for uniformly \(K_{t,t}\)-free classes. Together with the source paper's left-to-right implication, this gives the full equivalence in that setting.

The proof actually needs much less than “all transductions”: it uses only

1. linear neighbourhood complexity of \(\mathcal C\) itself, and
2. linear neighbourhood complexity of the explicit path-reading transductions \(\mathsf T_\ell\), one for each \(\ell\ge2\).

---

## 4. A general hereditary reduction

There is also a simple reduction useful for the unrestricted conjecture.

Let \(\operatorname{Ind}(\mathcal C)\) denote the induced-subgraph closure of \(\mathcal C\). The transduction that uses a unary predicate \(U\) and outputs \(G[U]\) has image exactly \(\operatorname{Ind}(\mathcal C)\). Since FO transductions are closed under composition,
\[
\text{all transductions of }\mathcal C\text{ have linear complexity}
\]
implies
\[
\text{all transductions of }\operatorname{Ind}(\mathcal C)
\text{ have linear complexity}.
\]
Merge-width is induced-subgraph monotone, by restricting a merge sequence. Hence it is enough to prove the full conjecture for hereditary classes.

---

## 5. What remains open

The argument fundamentally uses \(K_{t,t}\)-freeness in Lemma 1: a trace containing \(t\) sampled vertices can then occur at most \(t-1\) times. Without biclique exclusion, a large trace may be repeated arbitrarily often. Complete graphs and complete bipartite graphs demonstrate that this is not merely a defect of the proof: they have unbounded degeneracy but are highly mergeable and have bounded merge-width.

Thus a full proof cannot replace the premise simply by bounded expansion. It must exploit repeated large traces as mergeable dense structure and organize these repetitions coherently across all scales. The sampling argument only detects equality on one sampled set; it does not produce the global nested partitions required for a merge sequence. That is the unresolved dense case.

I have not independently verified whether the uniformly \(K_{t,t}\)-free special case above already appears in the post-2025 literature. The supplied review states that the 2026 sparse follow-up proves the merge-width/bounded-expansion equivalence but does not directly address the neighbourhood-complexity implication proved here.