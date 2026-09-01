```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The problem remains open, but K1 and K2 recover the complete induced three-vertex profile, their behavior is classified exactly on forests, and shallow coefficients of any fixed H-family cannot determine a typical graph.",
  "would_publish": false,
  "caveats": "No finite family is shown to work or fail; the entropy obstruction applies only to the first o(n/sqrt(log n)) coefficients below the leading terms."
}
```

# Mathematical writeup

## 1. Statement and notation

Let \(\mathcal C_k(G)\) be the graph whose vertices are the proper \(k\)-colourings of \(G\), with two colourings adjacent when they differ at exactly one vertex of \(G\). For a fixed graph \(H\), write
\[
\pi_G^{(H)}(k)
\]
for the number of unlabelled induced copies of \(H\) in \(\mathcal C_k(G)\). Multiplying by \(|\operatorname{Aut}H|\) gives the corresponding number of labelled induced embeddings, so normalization will not affect equality questions.

The open problem asks whether some fixed finite family \(H_1,\dots,H_t\) has the property that, with probability tending to one for \(G\sim G(n,\tfrac12)\), equality of all the polynomials \(\pi_G^{(H_i)}\) forces isomorphism.

I do not resolve this. I establish three partial results:

1. \(\pi_G^{(K_1)}\) and \(\pi_G^{(K_2)}\) determine all four induced three-vertex subgraph counts of \(G\).
2. On forests, all clique generalized chromatic polynomials are determined exactly by the degree multiset. In particular, even the infinite family \(\{\pi^{(K_r)}:r\ge1\}\) does not distinguish forests.
3. For an arbitrary fixed finite \(H\)-family, the first
   \[
   L=o\!\left(\frac n{\sqrt{\log n}}\right)
   \]
   coefficients below the leading terms do not determine almost every graph. Thus any affirmative proof must genuinely use coefficients substantially deep inside at least one polynomial.

---

## 2. Clique copies and true-twin blow-ups

For \(v\in V(G)\) and \(r\ge2\), let \(G(v\to K_r)\) be the graph obtained by replacing \(v\) by an \(r\)-clique \(v_1,\dots,v_r\), each \(v_i\) adjacent to every former neighbour of \(v\).

### Lemma 2.1
For every \(r\ge2\),
\[
r!\,\pi_G^{(K_r)}(k)
   =\sum_{v\in V(G)} P_{G(v\to K_r)}(k),
\tag{2.1}
\]
where \(P_F\) is the ordinary chromatic polynomial.

### Proof
A clique of size at least three in a Hamming graph lies in a single coordinate fibre: fixing one colouring \(f_0\), if \(f_1\) differs from \(f_0\) at \(u\) and \(f_2\) differs from \(f_0\) at \(v\ne u\), then \(f_1,f_2\) differ at both \(u\) and \(v\), so are not adjacent. The same coordinate is also unique for a \(K_2\), being the unique vertex on which its two colourings differ.

Thus a \(K_r\) in \(\mathcal C_k(G)\) consists of \(r\) proper colourings agreeing away from one vertex \(v\), and taking \(r\) distinct permissible colours at \(v\). Ordering these \(r\) colourings is equivalent to properly colouring the labelled \(r\)-clique replacing \(v\). Each unlabelled \(K_r\) has \(r!\) orderings. ∎

For \(r=2\), set
\[
Q_G(k):=2\pi_G^{(K_2)}(k)
       =\sum_{v\in V(G)}P_{G(v\to K_2)}(k).
\tag{2.2}
\]

---

## 3. Recovering the induced three-vertex profile

Let
\[
n=|V(G)|,\qquad m=e(G),\qquad \tau=\#K_3(G),
\]
and put
\[
W(G):=\sum_{v\in V(G)}\binom{d(v)}2.
\]

The first coefficients of the ordinary chromatic polynomial are
\[
P_G(k)
 =k^n-mk^{n-1}
  +\left(\binom m2-\tau\right)k^{n-2}
  +O(k^{n-3}).
\tag{3.1}
\]
Consequently, \(P_G=\pi_G^{(K_1)}\) determines \(n,m,\tau\).

We next extract \(W(G)\) from \(Q_G\).

For \(F_v:=G(v\to K_2)\), one has
\[
e(F_v)=m+d(v)+1.
\tag{3.2}
\]
If
\[
\tau_v=e(G[N_G(v)])
\]
is the number of triangles of \(G\) containing \(v\), then
\[
\#K_3(F_v)=\tau+d(v)+\tau_v.
\tag{3.3}
\]
Indeed, a triangle through \(v\) gives two triangles after the replacement, while each neighbour of \(v\) gives a triangle containing both true twins. Also,
\[
\sum_v d(v)=2m,\qquad \sum_v\tau_v=3\tau.
\tag{3.4}
\]

Applying (3.1) to every \(F_v\), the coefficient
\[
s_G:=[k^{n-1}]Q_G(k)
\]
is
\[
\begin{aligned}
s_G
 &=\sum_v\left[
       \binom{m+d(v)+1}{2}
       -\bigl(\tau+d(v)+\tau_v\bigr)
      \right] \\
 &=n\binom{m+1}{2}+2m^2+W(G)-(n+3)\tau.
\end{aligned}
\tag{3.5}
\]
Therefore
\[
W(G)
 =s_G-n\binom{m+1}{2}-2m^2+(n+3)\tau.
\tag{3.6}
\]

Let \(N_i(G)\) denote the number of three-vertex subsets inducing exactly \(i\) edges. Then
\[
\begin{aligned}
N_3&=\tau,\\
N_2&=W-3\tau,\\
N_1&=m(n-2)-2W+3\tau,\\
N_0&=\binom n3-m(n-2)+W-\tau.
\end{aligned}
\tag{3.7}
\]
Here \(W\) counts a two-edge path once and a triangle three times, while \(m(n-2)\) counts edge incidences over three-vertex subsets.

### Proposition 3.1
The pair
\[
\bigl(\pi_G^{(K_1)},\pi_G^{(K_2)}\bigr)
\]
determines the complete induced three-vertex profile of \(G\).

This is strictly stronger than the information supplied by the first three coefficients of the ordinary chromatic polynomial: in particular, it also determines the number \(N_0\) of independent triples.

It is still far from identifying a random graph. There are only polynomially many possible induced three-vertex profiles, so almost no graph can be identified from that profile alone. The lower coefficients of \(Q_G\), rather than the information above, would have to carry the decisive global information.

---

## 4. Exact classification on forests

Let \(F\) be a forest with \(n\) vertices and \(c\) components, and define its degree generating polynomial
\[
D_F(x):=\sum_{v\in V(F)}x^{d(v)}.
\]

### Proposition 4.1
For every \(r\ge2\),
\[
r!\,\pi_F^{(K_r)}(k)
 =
 k^{c-1}(k)_r (k-1)^{\,n-c}
 D_F\!\left(\frac{k-r}{k-1}\right),
\tag{4.1}
\]
where \((k)_r=k(k-1)\cdots(k-r+1)\).

### Proof
Let \(v\) lie in a tree component of order \(s\), and put \(d=d(v)\). In \(F(v\to K_r)\):

- the replacing \(K_r\) can be coloured in \((k)_r\) ways;
- each of the \(d\) former neighbours of \(v\) must avoid all \(r\) colours, giving \(k-r\) choices;
- every remaining vertex in that tree component has \(k-1\) choices after its parent is coloured;
- the other \(c-1\) tree components contribute
  \[
  k^{c-1}(k-1)^{n-s-(c-1)}.
  \]

Hence
\[
P_{F(v\to K_r)}(k)
 =
 k^{c-1}(k)_r
 (k-r)^d
 (k-1)^{n-c-d}.
\tag{4.2}
\]
Summing over \(v\) and using Lemma 2.1 proves (4.1). ∎

Since
\[
P_F(k)=k^c(k-1)^{n-c},
\tag{4.3}
\]
we obtain the following exact consequence.

### Corollary 4.2
Let \(F,F'\) be forests, and fix any \(r\ge2\). Then
\[
P_F=P_{F'}
\quad\text{and}\quad
\pi_F^{(K_r)}=\pi_{F'}^{(K_r)}
\]
if and only if \(F\) and \(F'\) have the same degree multiset.

Moreover, if an arbitrary graph \(G'\) has the same two polynomials as a forest \(F\), then \(G'\) is itself a forest with the same degree multiset.

### Proof
Equality of ordinary chromatic polynomials gives the same \(n\), the same number \(c\) of components, and the same number \(m=n-c\) of edges. The number of components is the multiplicity of the root \(0\). Since every graph with \(n\) vertices and \(c\) components has at least \(n-c\) edges, with equality exactly for forests, \(G'\) must also be a forest.

After cancelling the common nonzero factor in (4.1), equality of the \(K_r\)-polynomials gives
\[
D_F\!\left(\frac{k-r}{k-1}\right)
 =
D_{F'}\!\left(\frac{k-r}{k-1}\right).
\]
The substitution \((k-r)/(k-1)\) is nonconstant for \(r\ge2\), hence assumes infinitely many values. Therefore \(D_F=D_{F'}\), which is exactly equality of degree multisets. The converse follows directly from (4.1). ∎

Thus even the entire infinite clique family \(\{\pi^{(K_r)}:r\ge1\}\) sees only the degree multiset on forests.

For an explicit collision, let
\[
\begin{aligned}
E(T_1)&=\{ab,ac,ad,be,cf\},\\
E(T_2)&=\{ab,ad,ae,bc,cf\}.
\end{aligned}
\]
Both trees have degree multiset
\[
\{3,2,2,1,1,1\},
\]
but they are not isomorphic: in \(T_1\) the degree-three vertex has two degree-two neighbours, while in \(T_2\) it has only one. Consequently
\[
\pi_{T_1}^{(K_r)}=\pi_{T_2}^{(K_r)}
\qquad\text{for every }r\ge1.
\tag{4.4}
\]

This is not a counterexample to the catalog problem, since a successful family may contain nonclique graphs \(H\).

---

## 5. A structural representation of generalized chromatic polynomials

The following representation is useful for bounding the information in the leading coefficients.

Let \(F\) be a fixed graph. For each map
\[
\delta:E(F)\longrightarrow V(G),
\]
construct an auxiliary graph \(L(F,\delta;G)\) as follows. Begin with variables
\[
z_{a,v},\qquad a\in V(F),\ v\in V(G).
\]
For every edge \(ab\in E(F)\):

- identify \(z_{a,v}\) and \(z_{b,v}\) for every \(v\ne\delta(ab)\);
- require \(z_{a,\delta(ab)}\ne z_{b,\delta(ab)}\).

Also require
\[
z_{a,u}\ne z_{a,v}
\qquad
\text{for every }a\in V(F),\ uv\in E(G).
\]
After taking the equality quotient, the inequality constraints form a graph \(L(F,\delta;G)\); a loop means that there are no valid assignments.

A homomorphism \(F\to\mathcal C_k(G)\) uniquely specifies, for every edge \(ab\), the vertex \(\delta(ab)\) on which the two colourings differ. Conversely, the constraints above specify exactly such a homomorphism. Therefore
\[
\operatorname{hom}\!\left(F,\mathcal C_k(G)\right)
 =
 \sum_{\delta:E(F)\to V(G)}
 P_{L(F,\delta;G)}(k).
\tag{5.1}
\]

If \(h=|V(F)|\), \(e=|E(F)|\), and \(c=c(F)\), then
\[
cn\le |V(L(F,\delta;G))|\le cn+he.
\tag{5.2}
\]
Indeed, away from the at most \(e\) exceptional coordinates chosen by \(\delta\), all variables belonging to one component of \(F\) are identified. Furthermore,
\[
e(L(F,\delta;G))
 \le h\binom n2+\binom h2.
\tag{5.3}
\]

Labelled induced embeddings can be written as a fixed linear combination of homomorphism counts. Explicitly, inclusion-exclusion over the nonedges of \(H\) gives
\[
\operatorname{indemb}(H,X)
 =
 \sum_{J:\,H\subseteq J\subseteq K_h}
 (-1)^{e(J)-e(H)}\operatorname{injhom}(J,X),
\tag{5.4}
\]
and Möbius inversion on vertex partitions expresses every injective homomorphism count as a fixed linear combination of ordinary homomorphism counts of quotients of \(J\). Combining (5.1)–(5.4), every generalized chromatic polynomial is a fixed linear combination of chromatic polynomials of the auxiliary graphs above.

---

## 6. Shallow coefficients cannot identify a typical graph

For a nonzero polynomial
\[
I_{H,G}(k):=|\operatorname{Aut}H|\,\pi_G^{(H)}(k),
\]
write
\[
d_{H,G}=\deg I_{H,G},
\qquad
a_{H,j}(G)=[k^{d_{H,G}-j}]I_{H,G}(k).
\]

### Lemma 6.1
For every fixed nonempty graph \(H\), there are constants \(A_H,C_H\) such that, for every sufficiently large \(n\) and every \(n\)-vertex graph \(G\):

1. either \(I_{H,G}=0\), or
   \[
   d_{H,G}=c(H)n+q
   \qquad\text{for some }0\le q\le C_H;
   \tag{6.1}
   \]
2. for \(0\le j\le n/2\),
   \[
   |a_{H,j}(G)|\le n^{A_H(j+1)}.
   \tag{6.2}
   \]

### Proof
First suppose \(H\) is connected. Along a spanning tree of an induced copy of \(H\) in \(\mathcal C_k(G)\), all its colourings agree outside the bounded set of coordinates on which its edges differ. Once those differing coordinates and the equality patterns at them are fixed, the number of copies of that type is the chromatic polynomial of an auxiliary graph with
\[
n+O_H(1)
\]
vertices. Distinct feasible types contribute positively, so a nonzero polynomial has degree \(n+O_H(1)\).

If \(H\) has \(c\) components, one may initially choose the configurations in its components independently, giving degree
\[
cn+O_H(1).
\]
Configurations in which vertices belonging to different components coincide or become adjacent identify their colourings at all or all but one of the \(n\) coordinates, reducing the degree by at least \(n-O_H(1)\). This proves (6.1).

For the coefficient bound, use (5.1)–(5.4). Terms arising from a graph \(F\) with fewer than \(c(H)\) components have degree at most
\[
(c(H)-1)n+O_H(1)
\]
and hence do not contribute to the first \(n/2\) coefficients for sufficiently large \(n\).

For the remaining terms, the relevant auxiliary graph has
\[
N=c(H)n+O_H(1)
\]
vertices and \(M=O_H(n^2)\) edges. The absolute value of the coefficient of \(k^{N-r}\) in a chromatic polynomial is at most
\[
\binom Mr;
\]
this follows, for example, from the broken-circuit interpretation of chromatic coefficients. At depth \(j\) from \(d_{H,G}\), one has \(r\le j+O_H(1)\). There are at most
\[
n^{|E(F)|}=n^{O_H(1)}
\]
choices of \(\delta\). Since only finitely many \(F\) occur in (5.4), this gives
\[
|a_{H,j}(G)|
 \le C_H n^{O_H(1)}
       (C_Hn^2)^{j+C_H}
 \le n^{A_H(j+1)}.
\]
∎

Now fix a finite family
\[
\mathcal H=\{H_1,\dots,H_t\}.
\]
For \(L=L(n)\), let \(\mathsf T_{\mathcal H,L}(G)\) consist, for each \(H_i\), of the zero/nonzero flag, the degree, and the first \(L\) coefficients
\[
a_{H_i,0}(G),\dots,a_{H_i,L-1}(G).
\]

### Theorem 6.2
If
\[
L=o\!\left(\frac n{\sqrt{\log n}}\right),
\tag{6.3}
\]
then
\[
\Pr_{G\sim G(n,1/2)}
 \left[
 \mathsf T_{\mathcal H,L}(G)
 \text{ determines }G\text{ up to isomorphism}
 \right]
 \longrightarrow0.
\tag{6.4}
\]
In fact, the probability is at most
\[
\exp\left(-\left(\frac{\log2}{2}+o(1)\right)n^2\right).
\tag{6.5}
\]

### Proof
By Lemma 6.1, for fixed \(H_i\) the degree has only \(O_{H_i}(1)\) possible values, apart from the zero polynomial. The \(j\)-th coefficient has at most
\[
2n^{A_{H_i}(j+1)}+1
\]
possible values. Hence the total number \(R_n\) of truncated profiles satisfies
\[
\log R_n
 \le O_{\mathcal H}\!\left(
        \sum_{j=0}^{L-1}(j+1)\log n
      \right)
 =O_{\mathcal H}(L^2\log n)
 =o(n^2).
\tag{6.6}
\]

For each profile which determines an isomorphism class, at most \(n!\) labelled graphs realize that class. Since \(G(n,\tfrac12)\) is uniform on the \(2^{\binom n2}\) labelled graphs,
\[
\Pr(\text{unique truncated profile})
 \le
 \frac{R_n\,n!}{2^{\binom n2}}
 =
 \exp\left(
   -\left(\frac{\log2}{2}+o(1)\right)n^2
 \right).
\]
∎

---

## 7. What remains open

Theorem 6.2 is only a shallow-coefficient obstruction. A fixed generalized chromatic polynomial has degree \(c(H)n+O_H(1)\), so it has \(\Theta(n)\) potentially useful coefficients. The theorem discards coefficients at depth
\[
\Omega\!\left(\frac n{\sqrt{\log n}}\right),
\]
and those coefficients can be extremely large and may encode genuinely global structure.

Thus none of the following has been proved here:

- that any finite \(H\)-family distinguishes almost every graph;
- that every finite \(H\)-family has a typical collision;
- that \(\{K_1,K_2\}\), or any other explicit finite family, suffices for random graphs.

The exact forest calculation and the coefficient-entropy bound show respectively that clique patterns alone can be weak and that a bounded or shallow coefficient analysis cannot settle the problem. They do not resolve the behavior of the full generalized chromatic polynomials on dense random graphs.