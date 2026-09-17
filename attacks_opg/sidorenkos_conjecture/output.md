```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit folding argument proves Sidorenko for uniform-set disjointness graphs, including K_{5,5} minus a perfect matching, but does not resolve the general conjecture.",
  "would_publish": false,
  "caveats": "Special case only, with no novelty claim; the catalogue's purported open crown-graph example is covered by the proof."
}
```

## 1. A provable special case

I do not obtain a proof or counterexample for arbitrary bipartite \(H\). I give a self-contained proof for a substantial symmetric class. In particular, it covers \(K_{5,5}\) minus a perfect matching, so the catalogue’s designation of that graph as an unresolved instance is incorrect.

For integers \(a,b\ge 1\) and \(r\ge a+b\), define the bipartite **disjointness graph**
\[
D(r;a,b)
\]
as follows:

- its left vertices are the \(a\)-subsets of \([r]\);
- its right vertices are a separate copy of the \(b\)-subsets of \([r]\);
- a left vertex \(A\) and a right vertex \(B\) are adjacent precisely when \(A\cap B=\varnothing\).

Thus
\[
v(D)=\binom ra+\binom rb,
\qquad
m:=e(D)=\binom ra\binom{r-a}{b}.
\]

**Theorem.** For every such \(D=D(r;a,b)\) and every finite graph \(G\) with \(N\ge1\) vertices,
\[
t(D,G)\ge t(K_2,G)^m.
\]
Equivalently, writing \(p=2e(G)/N^2\),
\[
\operatorname{hom}(D,G)\ge p^mN^{\binom ra+\binom rb}.
\]

The proof actually establishes a stronger, decorated Hölder inequality. No novelty is claimed for this special case or the reflection method below.

## 2. A Cauchy–Schwarz folding criterion

Let \(H=(L\sqcup R,E)\) be a finite bipartite graph with \(m=|E|\ge1\). Assign to each edge \(e=uv\), with \(u\in L\), \(v\in R\), a nonnegative function
\[
f_e:[N]^2\longrightarrow[0,\infty).
\]
Define
\[
\mathcal T_H((f_e)_{e\in E})
=
\mathbb E_{(x_v)_{v\in V(H)}}
\prod_{\substack{uv\in E\\u\in L,\ v\in R}}
f_{uv}(x_u,x_v),
\]
where all vertex variables are independent and uniform on \([N]\). For a single function \(f\), write
\[
\tau_H(f)=\mathcal T_H((f)_{e\in E}).
\]

### Separating involutions and folds

Suppose \(\sigma\) is a bipartition-preserving automorphism of \(H\), with \(\sigma^2=\mathrm{id}\), and
\[
V(H)=S\sqcup V_+\sqcup V_-,
\]
where:

1. \(\sigma\) fixes every vertex of \(S\);
2. \(\sigma(V_+)=V_-\);
3. there are no edges between \(V_+\) and \(V_-\).

Define the two folds
\[
\phi_+(v)=
\begin{cases}
v,&v\in S\cup V_+,\\
\sigma(v),&v\in V_-,
\end{cases}
\qquad
\phi_-(v)=
\begin{cases}
v,&v\in S\cup V_-,\\
\sigma(v),&v\in V_+.
\end{cases}
\]
Both maps are endomorphisms of \(H\). For an edge decoration \(\mathbf f=(f_e)\), let
\[
\mathbf f^\phi=(f_{\phi(e)})_{e\in E}.
\]

**Folding inequality.**
\[
\boxed{\quad
\mathcal T_H(\mathbf f)^2
\le
\mathcal T_H(\mathbf f^{\phi_+})
\mathcal T_H(\mathbf f^{\phi_-}).
\quad} \tag{1}
\]

**Proof.** Condition on the variables indexed by \(S\), collectively denoted \(z\). Let \(C(z)\) be the product of the factors for edges contained in \(S\). Let \(A(z)\) and \(B(z)\) be the conditional expectations of the products contributed by the two halves, including their edges to \(S\).

The absence of edges between the halves gives
\[
\mathcal T_H(\mathbf f)=\mathbb E_z C(z)A(z)B(z).
\]
Since \(C\ge0\), Cauchy–Schwarz gives
\[
\mathcal T_H(\mathbf f)^2
\le
\bigl(\mathbb E_z C(z)A(z)^2\bigr)
\bigl(\mathbb E_z C(z)B(z)^2\bigr).
\]
In the first factor, the second independent copy of the \(+\)-half can be identified with the \(-\)-half using \(\sigma\). Consequently that factor is exactly
\(\mathcal T_H(\mathbf f^{\phi_+})\). The other factor is analogous. \(\square\)

### Edge collapse implies a Hölder inequality

**Lemma.** Suppose some composition \(\Phi\) of folds of the preceding type sends every edge of \(H\) to a single edge \(e_*\). Then
\[
\boxed{\quad
\mathcal T_H((f_e)_{e\in E})
\le
\prod_{e\in E}\tau_H(f_e)^{1/m}.
\quad} \tag{2}
\]

**Proof.** If some \(f_e\) is identically zero, both sides of the desired inequality are zero. Otherwise \(\tau_H(f_e)>0\) for every \(e\): choose a positive entry \(f_e(s,t)\), map every left vertex to \(s\), and every right vertex to \(t\).

Normalize
\[
g_e=\frac{f_e}{\tau_H(f_e)^{1/m}},
\qquad\text{so that}\qquad
\tau_H(g_e)=1.
\]
Let \(\mathcal P=\{g_e:e\in E\}\), a finite palette of functions, and put
\[
M=\max_{\mathbf h\in\mathcal P^E}\mathcal T_H(\mathbf h).
\]
A monochromatic decoration has value \(1\), so \(M\ge1\).

Choose a maximizing decoration \(\mathbf h\). For any available pair of folds, (1) gives
\[
M^2
\le
\mathcal T_H(\mathbf h^{\phi_+})
\mathcal T_H(\mathbf h^{\phi_-})
\le M^2.
\]
Both folded decorations therefore also have value \(M\). By iteration, precomposition by any composition of folds preserves maximality.

In particular, \(\mathbf h^\Phi\) is maximizing. But every edge of this decoration carries the same function \(h_{e_*}\), so
\[
M=\mathcal T_H(\mathbf h^\Phi)=\tau_H(h_{e_*})=1.
\]
Thus \(\mathcal T_H((g_e))\le1\). Rescaling proves (2). \(\square\)

### Deduction of Sidorenko’s inequality

Let \(W\) be the adjacency matrix of \(G\). Decorate one edge of \(H\) by \(W\), and every other edge by the constant function \(1\). Then
\[
\mathcal T_H(\mathbf f)=\mathbb E_{x,y}W(x,y)=p.
\]
Applying (2),
\[
p\le \tau_H(W)^{1/m}=t(H,G)^{1/m}.
\]
Hence \(t(H,G)\ge p^m\). This includes \(p=0\).

It remains to verify the edge-collapse hypothesis for \(D(r;a,b)\).

## 3. Disjointness graphs admit an explicit collapse

### The separating involutions

Fix distinct ground elements \(p,q\in[r]\). The transposition \((p\,q)\), acting on all subset labels, induces a bipartition-preserving involution \(\sigma_{pq}\) of \(D(r;a,b)\).

Its fixed vertices are exactly the subsets containing both \(p,q\), or neither. Call their set \(S\). Partition the remaining vertices as follows:
\[
\begin{aligned}
V_+={}&
\{\text{left }A:p\in A,\ q\notin A\}\\
&\ \cup\{\text{right }B:q\in B,\ p\notin B\},\\[1mm]
V_-={}&
\{\text{left }A:q\in A,\ p\notin A\}\\
&\ \cup\{\text{right }B:p\in B,\ q\notin B\}.
\end{aligned}
\]

There are no edges between \(V_+\) and \(V_-\):

- a left vertex in \(V_+\) and a right vertex in \(V_-\) both contain \(p\);
- a left vertex in \(V_-\) and a right vertex in \(V_+\) both contain \(q\).

Thus \(\sigma_{pq}\) supplies a valid pair of folds.

Let \(\phi_{pq}\) denote the fold onto \(S\cup V_+\). Explicitly, it:

- replaces \(q\) by \(p\) in a left subset when \(q\) is present and \(p\) is absent;
- replaces \(p\) by \(q\) in a right subset when \(p\) is present and \(q\) is absent;
- fixes the subset otherwise.

### A fixed sorting sequence collapses every edge

Encode an edge \((A,B)\), where \(A\cap B=\varnothing\), by a word of length \(r\) over the alphabet
\[
\mathrm L<\mathrm O<\mathrm R,
\]
putting
\[
w_i=
\begin{cases}
\mathrm L,&i\in A,\\
\mathrm R,&i\in B,\\
\mathrm O,&i\notin A\cup B.
\end{cases}
\]
Every such word has \(a\) symbols \(\mathrm L\), \(b\) symbols \(\mathrm R\), and \(r-a-b\) symbols \(\mathrm O\).

For adjacent positions \(i,i+1\), the fold \(\phi_{i,i+1}\) is exactly the compare-and-swap operation for this order. Its nontrivial actions are
\[
(\mathrm O,\mathrm L)\mapsto(\mathrm L,\mathrm O),\qquad
(\mathrm R,\mathrm O)\mapsto(\mathrm O,\mathrm R),\qquad
(\mathrm R,\mathrm L)\mapsto(\mathrm L,\mathrm R).
\]
All other adjacent pairs remain unchanged.

Now perform the fixed sequence
\[
\phi_{1,2},\phi_{2,3},\ldots,\phi_{r-1,r},
\]
repeated \(r-1\) times. This is bubble sort: after each sweep, another largest remaining symbol has reached its final position, and the already sorted suffix is unchanged. Therefore every edge-word becomes
\[
\underbrace{\mathrm L\cdots\mathrm L}_{a}
\underbrace{\mathrm O\cdots\mathrm O}_{r-a-b}
\underbrace{\mathrm R\cdots\mathrm R}_{b}.
\]

Consequently the resulting composition sends every edge to
\[
A_*=\{1,\ldots,a\},
\qquad
B_*=\{r-b+1,\ldots,r\}.
\]
These sets are disjoint because \(a+b\le r\).

The edge-collapse lemma applies, proving the theorem.

## 4. The catalogue’s example, and a stronger bound

Taking \(a=b=1\) gives
\[
D(r;1,1)=K_{r,r}\setminus M,
\]
where \(M\) is a perfect matching. Hence every crown graph with \(r\ge2\) satisfies Sidorenko’s inequality. In particular,
\[
\boxed{
\operatorname{hom}(K_{5,5}\setminus M,G)
\ge
\left(\frac{2e(G)}{N^2}\right)^{20}N^{10}.
}
\]

There is also a useful strengthening. For any nonempty subgraph \(F\subseteq H\), decorate the edges of \(F\) by \(W\) and all remaining edges by \(1\). Inequality (2) gives
\[
t(F,G)\le t(H,G)^{e(F)/e(H)},
\]
or
\[
t(H,G)\ge t(F,G)^{e(H)/e(F)}. \tag{3}
\]
Missing vertices of \(F\) can simply be added as isolated vertices, which does not change its homomorphism density.

For \(H=K_{5,5}\setminus M\), the left vertices labelled \(1,2\) and the right vertices labelled \(3,4\) span a \(C_4\). Thus
\[
\boxed{
t(K_{5,5}\setminus M,G)\ge t(C_4,G)^5\ge p^{20}.
}
\]

For completeness, the last inequality follows from two applications of Cauchy–Schwarz. Set
\[
c(x,x')=\mathbb E_y W(x,y)W(x',y),
\qquad
d(y)=\mathbb E_x W(x,y).
\]
Then
\[
t(C_4,G)
=\mathbb E_{x,x'}c(x,x')^2
\ge \bigl(\mathbb E_y d(y)^2\bigr)^2
\ge p^4.
\]
Thus any \(C_4\)-density surplus also yields a quantitative surplus for the catalogue’s example.

## 5. What remains unresolved

Every Cauchy–Schwarz step above depends on a genuine separating involution, and the conclusion depends on a verified finite edge-collapse sequence. An arbitrary bipartite graph need not have even one nontrivial bipartition-preserving automorphism, let alone such a sequence.

Accordingly, this is a sufficient criterion and a fully proved special class—not a reduction that settles all bipartite graphs. The argument supplies neither a general proof nor a counterexample to Sidorenko’s conjecture.