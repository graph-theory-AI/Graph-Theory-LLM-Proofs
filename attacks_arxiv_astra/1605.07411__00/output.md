```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A direct argument gives an explicit χ-bound for every forest whose nontrivial components are brooms, but does not settle arbitrary forests.",
  "would_publish": false,
  "caveats": "This addresses ordinary undirected chromatic number; no novelty or improvement over the best known bounds is claimed."
}
```

## 1. Interpretation and scope

I address the **undirected** statement identified in the supplied source-relation notes. For a finite simple graph \(H\), let
\[
\operatorname{Forb}(H)=\{G:G\text{ has no induced subgraph isomorphic to }H\}.
\]
The question is whether this class admits a bound
\[
\chi(G)\le f_H(\omega(G))
\]
exactly when \(H\) is a forest.

The catalog mixes this statement with results about oriented graphs and dichromatic number. Those concern different statements and are not used below.

I prove an explicit special case covering disjoint unions of paths, stars, and, more generally, brooms. The proof is self-contained apart from the classical high-girth theorem used for the already-known necessary direction.

## 2. The necessary direction and the precise equivalence

If \(H\) contains a cycle, put \(h=|V(H)|\). Erdős’s high-girth/high-chromatic theorem gives graphs of girth greater than \(h\) and arbitrarily large chromatic number. These graphs contain no copy of \(H\), even as a non-induced subgraph. They are triangle-free, so their clique number is at most two. Consequently,
\[
H\text{ contains a cycle}\quad\Longrightarrow\quad
\operatorname{Forb}(H)\text{ is not }\chi\text{-bounded}.
\]

For completeness, the passage from trees to forests requires no closure theorem. If \(F\) has components \(T_1,\dots,T_m\), choose \(x_i\in V(T_i)\), add one new vertex \(v\), and add the edges \(vx_i\). The resulting graph \(T\) is a tree and \(T-v=F\). Thus
\[
\operatorname{Forb}(F)\subseteq \operatorname{Forb}(T).
\]
Therefore the assertion for all forests is indeed equivalent to the assertion for all trees. This explains the connection with Gyárfás–Sumner; it does not resolve the remaining direction.

## 3. An explicit partial theorem

For integers \(s,r\ge1\), define the **broom** \(B_{s,r}\) by taking an induced path
\[
x_1-\cdots-x_s
\]
and adding \(r\) new leaves adjacent to \(x_s\).

Thus every star with an edge is a broom, and
\[
P_t=B_{t-1,1}\qquad(t\ge2).
\]

### Theorem

Let \(F\) be a forest with \(h\) vertices and \(z\) isolated vertices. Suppose \(F\) has at least one edge and every nontrivial component has a representation
\[
B_{s_i,r_i}.
\]
Set
\[
r=\max_i r_i,\qquad a=h-r-1.
\]
Define
\[
f_F(1)=1
\]
and, for \(k\ge2\),
\[
\boxed{
f_F(k)=a f_F(k-1)+z+
2\binom{k+r-2}{r-1}-1.
}
\]
Then every \(F\)-free graph \(G\) with \(\omega(G)\le k\) satisfies
\[
\chi(G)\le f_F(k).
\]

If \(F=hK_1\), the elementary Ramsey bound instead gives
\[
\chi(G)\le |V(G)|
\le \binom{k+h-1}{h-1}-1.
\]

In particular, the conjecture holds for every forest whose components are brooms or isolated vertices.

The main point is the following local-to-global lemma.

## 4. A local bound for one broom

Write
\[
\rho(k,r)=\binom{k+r-2}{r-1}.
\]
The elementary Ramsey bound says that every graph on at least \(\rho(k,r)\) vertices contains either a \(K_k\) or an independent set of size \(r\). It follows by induction from the usual Ramsey recurrence.

### Lemma

Let \(k\ge2\), \(s,r\ge1\), and let \(\tau\ge1\) be an integer. Suppose \(G\) satisfies
\[
\omega(G)\le k,\qquad
\chi(G[N(v)])\le\tau\quad\text{for every }v\in V(G).
\]
If \(G\) is \(B_{s,r}\)-free, then
\[
\chi(G)\le (s-1)\tau+2\rho(k,r)-1.
\]

### Proof

Put
\[
\rho=\rho(k,r),\qquad L=2\rho-1,
\]
and suppose, for a contradiction, that
\[
\chi(G)>(s-1)\tau+L.
\]
We may replace \(G\) by a component of maximum chromatic number and hence assume it is connected.

#### Constructing a path with a high-chromatic remainder

We construct an induced path \(v_1,\dots,v_s\) and a connected induced subgraph \(C_s\) such that:

- \(C_s\) is disjoint from the path;
- \(C_s\) is anticomplete to \(v_1,\dots,v_{s-1}\);
- \(v_s\) has a neighbor in \(C_s\);
- \(\chi(C_s)\ge L\).

Start with any vertex \(v_1\), and choose a component \(C_1\) of \(G-v_1\) of maximum chromatic number. Then
\[
\chi(C_1)\ge\chi(G)-1,
\]
and connectivity ensures that \(v_1\) has a neighbor in \(C_1\).

Suppose \(v_1,\dots,v_i,C_i\) have been constructed, where \(i<s\). Delete \(N(v_i)\cap V(C_i)\) from \(C_i\), and choose a component \(C_{i+1}\) of maximum chromatic number in what remains. Since the deleted set has chromatic number at most \(\tau\),
\[
\chi(C_{i+1})\ge\chi(C_i)-\tau.
\]
The numerical hypothesis guarantees that this remainder is nonempty.

Because \(C_i\) is connected, some vertex
\[
v_{i+1}\in N(v_i)\cap V(C_i)
\]
has a neighbor in \(C_{i+1}\). This extends the induced path and preserves the required anticompleteness. At the end,
\[
\chi(C_s)\ge\chi(G)-1-(s-1)\tau\ge L.
\]

#### Attaching the leaves

Choose an induced subgraph \(J\subseteq C_s\) that is vertex-minimal subject to \(\chi(J)\ge L\). Then
\[
\chi(J)=L,\qquad \delta(J)\ge L-1=2\rho-2.
\]
Indeed, deleting a vertex leaves an \((L-1)\)-colorable graph, so a vertex of degree at most \(L-2\) would permit that coloring to extend.

Extend \(v_1,\dots,v_s\) towards \(J\), using a shortest path in \(G[V(C_s)\cup\{v_s\}]\), and stop immediately before entering \(J\). This gives an induced path \(P\), on at least \(s\) vertices, with last vertex \(q\), such that
\[
A:=N(q)\cap V(J)\ne\varnothing,
\]
while every other vertex of \(P\) is anticomplete to \(J\).

If \(|A|\ge\rho\), then \(A\) contains an independent set of size \(r\): a \(K_k\) in \(A\), together with \(q\), would contradict \(\omega(G)\le k\). These independent vertices, together with the last \(s\) vertices of \(P\), induce \(B_{s,r}\).

Otherwise \(|A|\le\rho-1\). Choose \(x\in A\). Since \(x\) itself belongs to \(A\),
\[
\begin{aligned}
|N_J(x)\setminus A|
&\ge \delta(J)-(|A|-1)\\
&\ge (2\rho-2)-(\rho-2)\\
&=\rho.
\end{aligned}
\]
Again, \(N_J(x)\setminus A\) contains an independent set of size \(r\). These vertices are nonadjacent to \(q\), by their exclusion from \(A\), and are anticomplete to every earlier vertex of \(P\). Thus they form the leaves of a broom whose handle is the last \(s\) vertices of \(P+x\).

Both cases contradict \(B_{s,r}\)-freeness. ∎

## 5. Combining broom components

We next establish the local inequality needed for the theorem.

Let \(F\) have the parameters \(h,z,r,a\) above, and set
\[
L=2\rho(k,r)-1.
\]
Suppose \(G\) satisfies
\[
\omega(G)\le k,\qquad
\chi(G[N(v)])\le\tau\quad\text{for every }v.
\]
I claim that
\[
\boxed{
G\text{ is }F\text{-free}
\quad\Longrightarrow\quad
\chi(G)\le a\tau+z+L.
}
\]

Assume instead that
\[
\chi(G)>a\tau+z+L.
\]

First select the \(z\) isolated vertices of the desired copy, one at a time, deleting each selected vertex’s closed neighborhood before making the next selection. Each deletion costs at most \(\tau+1\) colors. Since \(a\ge z\), the displayed inequality guarantees that all these selections are possible.

Write the nontrivial components as
\[
H_1,\dots,H_m,\qquad H_i=B_{s_i,r_i},
\]
ordering them so that \(r_m=r\), and put \(h_i=|V(H_i)|\). After selecting the isolated vertices, the remaining graph has chromatic number greater than
\[
\left(\sum_{i=1}^m h_i-r-1\right)\tau+L.
\]

Now select \(H_1,\dots,H_m\) successively. After selecting a copy of \(H_i\), delete its entire closed neighborhood.

A useful saving is that \(H_i\) has no isolated vertices. Therefore, if \(S\) is its vertex set,
\[
N[S]=\bigcup_{v\in S}N(v),
\]
and hence
\[
\chi(G[N[S]])\le h_i\tau.
\]

Consequently, immediately before selecting \(H_i\), the remaining graph has chromatic number greater than
\[
\left(\sum_{j=i}^m h_j-r-1\right)\tau+L.
\]
This exceeds the threshold in the broom lemma:

- if \(i=m\), the coefficient of \(\tau\) is exactly \(s_m-1\);
- if \(i<m\), then \(h_m\ge r+1\), so
  \[
  \sum_{j=i}^m h_j-r-1\ge h_i\ge s_i-1;
  \]
- and \(r_i\le r\) implies
  \[
  2\rho(k,r_i)-1\le L.
  \]

Thus the lemma supplies the required induced copy of \(H_i\) at every step. The closed-neighborhood deletions ensure that all selected components are pairwise anticomplete. Together with the previously selected isolated vertices, they induce \(F\), a contradiction.

This proves the claimed local inequality.

## 6. Completing the chromatic bound

We prove the theorem by induction on \(k\).

For \(k=1\), every graph under consideration is edgeless, so its chromatic number is at most one.

Now let \(k\ge2\), and let \(G\) be \(F\)-free with \(\omega(G)\le k\). Every neighborhood induces an \(F\)-free graph of clique number at most \(k-1\). The induction hypothesis gives
\[
\chi(G[N(v)])\le f_F(k-1)
\quad\text{for every }v.
\]
Applying the local inequality with \(\tau=f_F(k-1)\), we obtain
\[
\chi(G)
\le a f_F(k-1)+z+2\rho(k,r)-1
=f_F(k).
\]
This completes the proof.

For the omitted edgeless case \(F=hK_1\), an \(F\)-free graph has no independent set of size \(h\). Together with the absence of \(K_{k+1}\), the elementary Ramsey bound gives the stated bound on its order.

As a small quantitative example, \(F=2K_2\) gives
\[
f_F(k)=2^k-1.
\]
At clique number two, the resulting bound \(\chi\le3\) is attained by \(C_5\), which has no induced \(2K_2\).

## 7. What remains unproved

The necessary direction is complete, and the sufficient direction above is complete for forests whose components are brooms or isolated vertices.

The missing step is sufficiency for a general tree. The critical-subgraph argument supplies independent terminal leaves at the end of one induced path; it does not supply the mutually compatible branching structure of an arbitrary tree. No general replacement for that step has been proved here.

Thus this is a rigorous, explicitly quantified special case—not a resolution of the full conjecture.