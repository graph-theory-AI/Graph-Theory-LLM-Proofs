```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but it follows for graphs with at most n t^(2 gamma) triangles whenever epsilon plus gamma is less than 1/26, and every counterexample has a constrained Hall-ratio core.",
  "would_publish": false,
  "caveats": "The exact Section 4 quantifiers are unavailable, and the argument does not handle triangle-rich cores."
}
```

## 1. Adopted formulation

Write \(h(G)\) for the largest \(r\) such that \(G\) contains a \(K_r\)-minor. I interpret
\[
MR_t(s,k)
\]
as the least \(N\) such that every graph of order at least \(N\) contains a \(K_s\), an independent set of order \(k\), or a \(K_t\)-minor.

Thus the conjecture is naturally:

> For each fixed \(s\ge 4\), there exist \(\varepsilon_s>0\) and \(t_s\) such that every \(K_s\)-free graph \(G\) with \(h(G)<t\), where \(t\ge t_s\), satisfies
> \[
> \alpha(G)\ge \frac{|V(G)|}{t^{1-\varepsilon_s}}.
> \tag{C\(_s\)}
> \]

Here \(\varepsilon_s\) must depend on \(s\), since the proposed obstruction is \(\varepsilon_s\le 1/s\).

Define the Hall-ratio-type parameter
\[
\Phi_s(t)=
\sup\left\{\frac{|V(G)|}{\alpha(G)}:
  \omega(G)<s,\ h(G)<t\right\}.
\]
Up to rounding, the uniform bound on \(MR_t(s,k)\) is equivalent to
\[
\Phi_s(t)\le t^{1-\varepsilon_s}.
\tag{1}
\]
Indeed, (1) immediately gives
\[
MR_t(s,k)\le \lfloor t^{1-\varepsilon_s}(k-1)\rfloor+1.
\]
Conversely, if \(MR_t(s,k)\le Tk\) for every \(k\), apply this to \(q\) disjoint copies of a fixed admissible graph \(G\), with \(k=q\alpha(G)+1\), and let \(q\to\infty\). This gives \(|G|/\alpha(G)\le T\).

The only non-elementary input below is the supplied \(s=3\) theorem:

> For every \(0<\eta<1/26\), and all sufficiently large \(t\), every triangle-free graph \(F\) with \(h(F)<t\) satisfies
> \[
> \alpha(F)\ge \frac{|V(F)|}{t^{1-\eta}}.
> \tag{TF\(_\eta\)}
> \]

## 2. An alteration lemma for finding an induced triangle-free subgraph

Let \(\tau_3(G)\) denote the number of triangles of \(G\), and let
\[
\beta_3(G)=\max\{|X|:G[X]\text{ is triangle-free}\}.
\]

### Lemma 2.1
If \(G\) has \(n\) vertices and \(T=\tau_3(G)\), then, for every \(0\le p\le1\),
\[
\beta_3(G)\ge pn-p^3T.
\tag{2}
\]

#### Proof
Choose every vertex independently with probability \(p\), obtaining \(X\). Let \(Y\) be the number of triangles in \(G[X]\). Then
\[
\mathbb E|X|=pn,\qquad \mathbb EY=p^3T.
\]
From \(X\), delete one vertex from each triangle of \(G[X]\). The union of the deleted vertices has size at most \(Y\), and the remaining induced graph is triangle-free. Hence some choice of \(X\) leaves at least \(pn-p^3T\) vertices. ∎

Two consequences will be useful. If \(T\ge n/3\), take
\[
p=\sqrt{\frac{n}{3T}}
\]
to obtain
\[
\beta_3(G)\ge
\frac{2}{3\sqrt3}\frac{n^{3/2}}{\sqrt T}.
\tag{3}
\]
If \(T<n/3\), taking \(p=1\) gives
\[
\beta_3(G)\ge n-T>\frac{2n}{3}.
\tag{4}
\]

## 3. A triangle-sparse case of the conjecture

### Theorem 3.1
Let \(\gamma\ge0\) and \(\varepsilon>0\) satisfy
\[
\varepsilon+\gamma<\frac1{26}.
\tag{5}
\]
For all sufficiently large \(t\), every \(K_t\)-minor-free graph \(G\) on \(n\) vertices satisfying
\[
\tau_3(G)\le n t^{2\gamma}
\tag{6}
\]
has
\[
\alpha(G)\ge\frac{n}{t^{1-\varepsilon}}.
\tag{7}
\]
No assumption on \(\omega(G)\) is needed.

#### Proof
Choose \(\eta\) with
\[
\varepsilon+\gamma<\eta<\frac1{26}.
\]
Apply Lemma 2.1 with
\[
p=\frac{1}{\sqrt3\,t^\gamma}.
\]
Using (6),
\[
p^3\tau_3(G)
 \le \frac{1}{3\sqrt3\,t^{3\gamma}}nt^{2\gamma}
 =\frac{n}{3\sqrt3\,t^\gamma}.
\]
Consequently \(G\) has an induced triangle-free subgraph \(F\) satisfying
\[
|V(F)|\ge
\frac{2}{3\sqrt3}\frac{n}{t^\gamma}.
\]
It is also \(K_t\)-minor-free. By \((\mathrm{TF}_\eta)\),
\[
\alpha(G)\ge\alpha(F)
 \ge \frac{2}{3\sqrt3}
       \frac{n}{t^{1-\eta+\gamma}}.
\]
Since \(\eta-\gamma-\varepsilon>0\), the fixed multiplicative constant is absorbed for sufficiently large \(t\), yielding (7). ∎

Thus the catalog conjecture holds, with any
\[
\varepsilon<\frac1{26}-\gamma,
\]
for every \(K_s\)-free candidate having at most \(nt^{2\gamma}\) triangles. In particular, the full \(s=3\) exponent extends to graphs with only \(O(n)\) triangles.

A local sufficient condition is that every vertex lies in at most \(O(t^{2\gamma})\) triangles, since then (6) follows by double counting.

## 4. Necessary structure of a counterexample

The preceding argument also gives a useful obstruction statement.

### Proposition 4.1
Fix
\[
0<\varepsilon<\eta<\frac1{26},
\qquad
\zeta=\eta-\varepsilon.
\]
Suppose that, for sufficiently large \(t\), a \(K_s\)-free, \(K_t\)-minor-free graph \(G\) satisfies
\[
\frac{|V(G)|}{\alpha(G)}>t^{1-\varepsilon}.
\tag{8}
\]
Then \(G\) contains an induced subgraph \(H\), with
\[
m=|V(H)|,\qquad a=\alpha(H),\qquad r=\frac ma,
\]
having all the following properties:

1. \(r>t^{1-\varepsilon}\);
2. \(\delta(H)\ge r-1\);
3. every induced triangle-free subgraph of \(H\) has fewer than
   \[
   \frac{m}{t^\zeta}
   \tag{9}
   \]
   vertices;
4. 
   \[
   \tau_3(H)>\frac4{27}m t^{2\zeta};
   \tag{10}
   \]
5. for every \((s-3)\)-clique \(Q\) of \(H\),
   \[
   |N_H(Q)|<\frac{m}{t^\zeta};
   \tag{11}
   \]
6. for a constant \(c_s>0\),
   \[
   m\ge c_s r^{(s-1)/(s-2)}.
   \tag{12}
   \]

For \(s=4\), (11) becomes
\[
\Delta(H)<\frac{m}{t^\zeta},
\tag{13}
\]
and hence
\[
m>(r-1)t^\zeta
  >\frac12t^{\,1+\eta-2\varepsilon}
\tag{14}
\]
for sufficiently large \(t\).

#### Proof

Choose \(H\) attaining the maximum
\[
r=\max_{\varnothing\ne J\subseteq_{\mathrm{ind}}G}
  \frac{|V(J)|}{\alpha(J)}.
\]
Then \(r\ge |G|/\alpha(G)>t^{1-\varepsilon}\).

For \(v\in V(H)\), the induced graph
\[
H-N_H[v]
\]
has independence number at least
\[
\frac{m-d_H(v)-1}{r}
\]
by maximality of \(r\). Adding \(v\) gives
\[
a\ge
1+\frac{m-d_H(v)-1}{r}.
\]
Since \(a=m/r\), this implies
\[
d_H(v)+1\ge r,
\]
proving property 2.

Let \(F\) be any induced triangle-free subgraph of \(H\). By \((\mathrm{TF}_\eta)\),
\[
|V(F)|\le t^{1-\eta}\alpha(F)
       \le t^{1-\eta}a
       =\frac{t^{1-\eta}m}{r}
       <\frac{m}{t^\zeta}.
\]
This proves property 3.

Let \(T=\tau_3(H)\). For sufficiently large \(t\), (9) gives
\(\beta_3(H)<2m/3\). Thus (4) rules out \(T<m/3\). Applying (3),
\[
\frac{m}{t^\zeta}>
\beta_3(H)\ge
\frac{2}{3\sqrt3}\frac{m^{3/2}}{\sqrt T}.
\]
Rearranging gives
\[
T>\frac4{27}m t^{2\zeta},
\]
which is property 4.

If \(Q\) is an \((s-3)\)-clique, then \(H[N_H(Q)]\) is triangle-free: a triangle in \(N_H(Q)\), together with \(Q\), would form a \(K_s\). Property 3 therefore gives (11). More precisely, \(H[N_H(Q)]\) has no \(K_{t-s+3}\)-minor, since such a minor together with the vertices of \(Q\) would give a \(K_t\)-minor.

Finally, the elementary Ramsey recurrence gives
\[
R(s,a+1)\le \binom{a+s-1}{s-1}\le C_s a^{s-1}.
\]
Since \(H\) is \(K_s\)-free and has independence number \(a\),
\[
m<R(s,a+1)\le C_s a^{s-1}.
\]
As \(m=ra\), this yields
\[
a\ge C_s^{-1/(s-2)}r^{1/(s-2)}
\]
and hence (12).

For \(s=4\), an \((s-3)\)-clique is a single vertex, so (11) is exactly (13). Combining it with \(\delta(H)\ge r-1\) gives (14). ∎

There is also the clique-count consequence
\[
(s-2)k_{s-2}(H)
 =\sum_{Q\in\mathcal K_{s-3}(H)}|N_H(Q)|
 <\frac{m}{t^\zeta}k_{s-3}(H),
\tag{15}
\]
where \(k_j(H)\) denotes the number of \(j\)-cliques.

For \(s=4\), this gives
\[
e(H)<\frac{m^2}{2t^\zeta}.
\]

## 5. A separator-based special case

The following independent criterion isolates another sufficient condition.

### Proposition 5.1
Fix \(s\ge3\). Suppose every induced subgraph \(J\) of a \(K_s\)-free graph \(G\) has a \(2/3\)-balanced separator of size at most
\[
C t^\lambda\sqrt{|V(J)|}.
\tag{16}
\]
Then
\[
\alpha(G)\ge
c_{s,C}\frac{|V(G)|}
 {t^{\,2\lambda(s-2)/(s-1)}}.
\tag{17}
\]

Consequently, if
\[
\lambda<\frac{s-1}{2(s-2)},
\tag{18}
\]
then \(G\) satisfies the conjectured form
\[
\alpha(G)\ge\frac{|V(G)|}{t^{1-\varepsilon}}
\]
for every
\[
0<\varepsilon<
1-\frac{2\lambda(s-2)}{s-1}
\]
and sufficiently large \(t\).

#### Proof
Recursively apply the separators until every remaining component has order at most
\[
M=C' t^{2\lambda},
\]
where \(C'\) is sufficiently large in terms of \(C\).

The total number of deleted separator vertices is \(O(Ct^\lambda n/\sqrt M)\). This follows by charging the separator of a recursive piece of order \(x\) uniformly to its \(x\) vertices: along every recursion path the piece orders decrease by a factor at least \(2/3\), so the total charge to a vertex is \(O(t^\lambda/\sqrt M)\). Choosing \(C'\) large leaves at least \(n/2\) vertices.

For fixed \(s\), the Ramsey recurrence gives
\[
\alpha(J)\ge c_s |V(J)|^{1/(s-1)}
\]
for every \(K_s\)-free graph \(J\). If \(J\) is a remaining component of order \(m_J\le M\), then
\[
\alpha(J)\ge
c_s\frac{m_J}{M^{(s-2)/(s-1)}}.
\]
Independent sets from the remaining components can be united. Summing over them proves (17). ∎

This proposition is only a criterion: the catalog hypotheses do not themselves provide (16) with an exponent \(\lambda\) satisfying (18).

## 6. What remains open

The main missing step is substantial. Neither \(K_s\)-freeness nor exclusion of a \(K_t\)-minor implies the triangle bound in Theorem 3.1. For example, complete tripartite graphs are \(K_4\)-free and can contain \(\Theta(n^3)\) triangles, although their independence ratio is only \(3\). Thus one needs a genuine dichotomy showing that a triangle-rich graph either already has a large independent set or contains a large clique minor.

The core reduction makes this more precise. A counterexample can be assumed to have:

- minimum degree at least \(t^{1-\varepsilon}-1\);
- no induced triangle-free set of relative size \(t^{-(\eta-\varepsilon)}\);
- at least a polynomial number \(t^{2(\eta-\varepsilon)}\) of triangles per vertex on average;
- very small common neighborhoods of every \((s-3)\)-clique.

I do not have an argument showing that these conditions force a \(K_t\)-minor, nor an explicit graph satisfying them and violating the conjecture. Hence this is a partial result only.