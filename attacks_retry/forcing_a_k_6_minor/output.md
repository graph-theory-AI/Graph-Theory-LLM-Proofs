```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Matching contraction and Tutte–Berge give a local short-cycle criterion for minimum degree seven, and show that minimum degree five suffices at girth at least five and six suffices without 4-cycles.",
  "would_publish": false,
  "caveats": "Neither unrestricted conjecture is resolved; the argument uses classical Mader and Tutte–Berge theorems, and no novelty claim is made."
}
```

## 1. Results

All graphs are finite and simple. For an edge \(e\) of \(G\), let

- \(t_G(e)\) be the number of triangles containing \(e\);
- \(q_G(e)\) be the number of **induced** \(4\)-cycles containing \(e\).

I prove the following sufficient condition.

**Theorem.** Let \(a\in\{0,1,2\}\). Suppose that
\[
\delta(G)\ge 5+a
\]
and, for every edge \(e\),
\[
2t_G(e)+q_G(e)\le 2a.
\tag{1}
\]
Then \(G\) contains a \(K_6\)-minor.

In particular:

1. **Every graph of girth at least five and minimum degree at least five contains a \(K_6\)-minor.**
2. **Every graph with no \(4\)-cycle and minimum degree at least six contains a \(K_6\)-minor.**
3. **Every graph of minimum degree at least seven with no induced \(4\)-cycle, and with each edge in at most two triangles, contains a \(K_6\)-minor.**

The first result improves the supplied attempt’s girth-five bound from six to five, and removes the bipartiteness assumption from its degree-five result. The second permits triangles.

I reuse and reprove the earlier attempt’s matching-contraction observation. Its clique-separator claims are not needed. The additional ingredient is a Tutte–Berge argument that handles unmatched vertices more effectively.

## 2. Classical inputs

I use Mader’s extremal bound:
\[
|E(H)|\le 4|V(H)|-10
\tag{2}
\]
for every \(K_6\)-minor-free simple graph \(H\) with at least four vertices. The cases of four and five vertices are immediate; the remaining cases are the classical extremal theorem for \(K_6\)-minors.

I also use the Tutte–Berge formula. Writing \(\nu(G)\) for the maximum matching size and \(o(G-S)\) for the number of odd-order components of \(G-S\),
\[
|V(G)|-2\nu(G)
=
\max_{S\subseteq V(G)}\bigl(o(G-S)-|S|\bigr).
\tag{3}
\]

A graph \(F\) is **factor-critical** if \(F-v\) has a perfect matching for every \(v\in V(F)\). A one-vertex graph is factor-critical.

## 3. Controlling edge loss under matching contraction

**Lemma 1.** Let \(M\) be a matching of size \(k\) in a simple graph \(G\), and let \(J\) be the simple graph obtained by contracting every edge of \(M\). Then
\[
|V(J)|=|V(G)|-k
\]
and
\[
|E(J)|
\ge
|E(G)|-k
-\sum_{e\in M}t_G(e)
-\frac12\sum_{e\in M}q_G(e).
\tag{4}
\]
Consequently, under condition (1),
\[
|E(J)|\ge |E(G)|-(a+1)k.
\tag{5}
\]

**Proof.** Regard the contraction as a partition into two-vertex blocks corresponding to edges of \(M\), and singleton blocks.

The \(k\) matching edges disappear. Additional loss comes from identifying multiple edges between the same two blocks.

For a two-vertex block and a singleton, two edges between the blocks form a triangle containing the matching edge. The extra loss is one.

Now consider two two-vertex blocks. There are at most four edges between them.

- With two such edges sharing an endpoint, there is a triangle containing a matching edge; the extra loss is one.
- With two such edges having disjoint endpoints, the four vertices induce a \(4\)-cycle whose opposite edges belong to \(M\); the extra loss is one.
- With three such edges, the four vertices span \(K_4\) minus an edge. There are two triangles containing matching edges, accounting for the extra loss of two.
- With four such edges, there are four triangles containing matching edges, more than enough to account for the extra loss of three.

Thus the additional loss is at most
\[
T_M+Q_M,
\]
where \(T_M\) is the number of triangles containing an edge of \(M\), and \(Q_M\) is the number of induced \(4\)-cycles with two opposite edges in \(M\).

Every triangle contains at most one matching edge, so
\[
T_M=\sum_{e\in M}t_G(e).
\]
Every cycle counted by \(Q_M\) contributes twice to \(\sum_{e\in M}q_G(e)\). Hence
\[
Q_M\le \frac12\sum_{e\in M}q_G(e).
\]
This proves (4), and (1) gives (5). \(\square\)

For girth at least five, there is no additional loss at all:
\[
|E(J)|=|E(G)|-k.
\]
This verifies the matching-contraction identity used in the previous attempt.

Importantly, condition (1) is inherited by induced subgraphs: their triangle and induced-\(4\)-cycle counts cannot increase.

## 4. A matching-density lemma

The following is the step that replaces the bipartite vertex-cover argument.

**Lemma 2.** Let \(G\) have minimum degree at least \(d\). Suppose every induced factor-critical subgraph \(F\) satisfies
\[
|E(F)|\le \frac d2\bigl(|V(F)|-1\bigr).
\tag{6}
\]
Then, writing \(n=|V(G)|\), \(m=|E(G)|\), and \(k=\nu(G)\),
\[
m\ge d(n-k).
\tag{7}
\]

**Proof.** Put
\[
u=n-2k.
\]
Choose \(S\subseteq V(G)\) maximizing \(o(G-S)-|S|\), and, among such choices, maximizing \(|S|\). By Tutte–Berge,
\[
o(G-S)-|S|=u.
\tag{8}
\]

We first verify that every component of \(G-S\) is odd and factor-critical.

If a component \(C\) had even order, then for any \(v\in V(C)\), the graph \(C-v\) would have at least one odd component. Adding \(v\) to \(S\) would therefore not decrease \(o(G-S)-|S|\), contradicting the choice of \(S\).

Now let \(C\) be an odd component that is not factor-critical. There is a vertex \(v\in V(C)\) such that \(C-v\) has no perfect matching. Since \(C-v\) has even order, Tutte–Berge supplies a set
\[
T\subseteq V(C)\setminus\{v\}
\]
such that
\[
o(C-v-T)\ge |T|+2.
\]
Replacing \(S\) by \(S\cup T\cup\{v\}\) again does not decrease \(o(G-S)-|S|\), while increasing \(|S|\), a contradiction.

Thus all components of \(G-S\) are odd and factor-critical. Let their number be \(q\), and put \(s=|S|\). Equation (8) gives
\[
q-s=u.
\tag{9}
\]

Let \(m_{\rm out}=|E(G-S)|\). Applying (6) to these components,
\[
m_{\rm out}
\le \frac d2(n-s-q).
\tag{10}
\]
On the other hand,
\[
m
=
\sum_{v\notin S}d_G(v)-m_{\rm out}+|E(G[S])|.
\]
Consequently,
\[
\begin{aligned}
m
&\ge d(n-s)-\frac d2(n-s-q)+|E(G[S])|\\
&=\frac d2(n-s+q)+|E(G[S])|\\
&=\frac d2(n+u)+|E(G[S])|\\
&\ge d(n-k).
\end{aligned}
\]
This proves the lemma. \(\square\)

## 5. Proof of the theorem

Fix \(a\in\{0,1,2\}\), and set
\[
\lambda=a+1,\qquad d=a+5=4+\lambda.
\]
Suppose, for a contradiction, that \(G\) satisfies the theorem’s hypotheses but is \(K_6\)-minor-free.

By Lemma 1, for every induced subgraph \(H\) of \(G\) and every matching \(P\) in \(H\),
\[
|E(H/P)|\ge |E(H)|-\lambda |P|,
\tag{11}
\]
where \(H/P\) denotes the simplified matching contraction.

### 5.1 Factor-critical induced subgraphs satisfy the required bound

Let \(F\) be an induced factor-critical subgraph, of odd order \(h\).

If \(h\le5\), then \(h\le d\), and simplicity gives
\[
|E(F)|\le \binom h2
\le \frac d2(h-1).
\tag{12}
\]

Suppose \(h\ge7\). Factor-criticality supplies a matching \(P\) of size
\[
|P|=\frac{h-1}{2}.
\]
The quotient \(F/P\) has
\[
\frac{h+1}{2}\ge4
\]
vertices and is \(K_6\)-minor-free. Applying (2) and (11),
\[
\begin{aligned}
|E(F)|
&\le |E(F/P)|+\lambda\frac{h-1}{2}\\
&\le 4\frac{h+1}{2}-10+\lambda\frac{h-1}{2}\\
&=\frac{4+\lambda}{2}(h-1)-6\\
&=\frac d2(h-1)-6.
\end{aligned}
\tag{13}
\]
In particular, condition (6) holds for every induced factor-critical subgraph.

### 5.2 Contracting a maximum matching gives the contradiction

Write
\[
n=|V(G)|,\qquad m=|E(G)|,\qquad k=\nu(G).
\]
Lemma 2 gives
\[
m\ge d(n-k).
\tag{14}
\]

Contract a maximum matching, obtaining \(J\). Using (11) and (14),
\[
\begin{aligned}
|E(J)|
&\ge m-\lambda k\\
&\ge d(n-k)-\lambda k\\
&=4(n-k)+\lambda(n-2k)\\
&\ge4(n-k)\\
&=4|V(J)|.
\end{aligned}
\tag{15}
\]

Under the counterexample assumption, \(n\ge7\): minimum degree at least five forces \(n\ge6\), and the only six-vertex graph with minimum degree at least five is \(K_6\). Therefore
\[
|V(J)|=n-k\ge\lceil n/2\rceil\ge4.
\]
But \(J\) is \(K_6\)-minor-free, so (2) contradicts (15). This proves the theorem. \(\square\)

## 6. Consequences for the original conjectures

### Girth at least five

Here \(t_G(e)=q_G(e)=0\) for every edge. Taking \(a=0\) proves:
\[
\boxed{\text{Girth at least five and minimum degree at least five force a }K_6\text{-minor}.}
\]

No bipartiteness is required.

### No \(4\)-cycle

If \(G\) has no \(4\)-cycle, then \(q_G(e)=0\). Also, an edge belongs to at most one triangle: two triangles \(uvx\) and \(uvy\) would give the \(4\)-cycle
\[
u\,x\,v\,y\,u.
\]
Thus \(2t_G(e)+q_G(e)\le2\), and \(a=1\) gives
\[
\boxed{\text{No }4\text{-cycle and minimum degree at least six force a }K_6\text{-minor}.}
\]

### A degree-seven local criterion

Taking \(a=2\) proves the original minimum-degree conjecture whenever
\[
2t_G(e)+q_G(e)\le4
\qquad\text{for every edge }e.
\]
This includes graphs with no induced \(4\)-cycle in which every edge belongs to at most two triangles.

### Short-cycle transversal consequences

Deleting a set \(X\) reduces minimum degree by at most \(|X|\). Hence a graph \(G\) with \(\delta(G)\ge7\) contains a \(K_6\)-minor if either:

- some set of at most one vertex meets every \(4\)-cycle; or
- some set of at most two vertices meets every triangle and every \(4\)-cycle.

Consequently, any counterexample to the minimum-degree-seven conjecture must satisfy all of the following:

1. Some edge \(e\) has
   \[
   2t_G(e)+q_G(e)\ge5.
   \]
2. No single vertex meets every \(4\)-cycle.
3. No two vertices meet every triangle and every \(4\)-cycle.

Since seven-connectivity implies minimum degree at least seven, the same sufficient conditions also settle the seven-connected conjecture within these classes.

## 7. What remains unresolved

The argument does not handle arbitrary concentrations of overlapping triangles and induced \(4\)-cycles. Those configurations can cause substantial edge loss under matching contraction, and nothing proved here excludes them in a hypothetical minimum-degree-seven counterexample.

Thus neither unrestricted conjecture is proved or disproved. These are rigorous special cases and necessary conditions on a counterexample. They improve the supplied attempt’s matching-based conclusions, but I have not verified whether these formulations already appear in the literature, and I make no novelty claim.