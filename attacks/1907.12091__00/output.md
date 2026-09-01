```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but its exponential growth constant is exactly the optimal growth constant for two-terminal simple paths, and bounded-degree configuration-model graphs have annealed base at most 5/7^(2/3) < kappa_1.",
  "would_publish": false,
  "caveats": "The probabilistic bound is only annealed/typical, and determining the growth constant alone does not establish the exact O(kappa_1^m) bound."
}
```

# 1. Statement and outcome

Write
\[
\kappa=(2+2\sqrt2)^{1/5}=1.37012\ldots.
\]
The conjecture asserts that there is an absolute constant \(C\) such that every simple \(m\)-edge graph has at most \(C\kappa^m\) simple cycles.

I do not prove or disprove this. I obtain:

1. an exact reduction of the exponential-rate problem to maximizing the number of simple paths between two terminals;
2. a finite-gadget amplification criterion which would immediately produce a counterexample;
3. an annealed upper bound, strictly below \(\kappa\), for every bounded-degree configuration-model ensemble;
4. a self-contained transfer-matrix derivation of the constant \(2+2\sqrt2\).

The principal unresolved point remains a deterministic bound for exceptional, highly structured graphs.

# 2. Reduction to two-terminal paths

For \(m\ge 1\), let

- \(M_m\) be the maximum number of cycles in a simple graph with \(m\) edges;
- \(P_m\) be the maximum number of simple \(s\)-\(t\) paths in a simple graph \(H\) with \(m\) edges, maximized over distinct terminals \(s,t\).

Disconnected padding components may be added, so “exactly \(m\) edges” causes no difficulty.

## Proposition 2.1

Define
\[
\rho_C=\limsup_{m\to\infty}M_m^{1/m}.
\]
Then the limit
\[
\rho_P=\lim_{m\to\infty}P_m^{1/m}
\]
exists, and
\[
\boxed{\rho_C=\rho_P=\sup_{m\ge1}P_m^{1/m}.}
\]

### Proof

First, \(P_m\) is supermultiplicative. Given two two-terminal graphs
\((H_1,s_1,t_1)\) and \((H_2,s_2,t_2)\), identify \(t_1\) with \(s_2\), keeping all other vertices disjoint. Every choice of an \(s_1\)-\(t_1\) path and an \(s_2\)-\(t_2\) path gives an \(s_1\)-\(t_2\) path. Hence
\[
P_{a+b}\ge P_aP_b.
\]
Fekete’s lemma gives
\[
\rho_P=\lim_{m\to\infty}P_m^{1/m}
      =\sup_m P_m^{1/m}.
\]

For the upper comparison, let \(G\) have \(m\) edges. For \(e=uv\), cycles of \(G\) containing \(e\) are in bijection with simple \(u\)-\(v\) paths in \(G-e\). Therefore
\[
\sum_{e\in E(G)}p_{G-e}(u_e,v_e)
  =\sum_{\text{cycles }C}|E(C)|
  \ge 3c(G).
\]
It follows that
\[
M_m\le \frac m3 P_{m-1}.
\]
Taking \(m\)-th roots gives
\[
\rho_C\le \rho_P.
\]

Conversely, fix a two-terminal graph \(H\) with \(m\) edges and \(p\) simple terminal paths. Take \(k\ge3\) disjoint copies \(H_1,\dots,H_k\), and cyclically identify \(t_i\) with \(s_{i+1}\). The resulting graph is simple and has \(km\) edges. Choosing one terminal path in every copy produces a simple cycle, so
\[
M_{km}\ge p^k.
\]
Thus
\[
\rho_C\ge p^{1/m}.
\]
Taking the supremum over \(H\) proves the proposition. \(\square\)

## Consequences

The conjectured exponential base is therefore equivalent to
\[
\rho_P=\kappa.
\]

More strongly, the stated \(O(\kappa^m)\) conjecture would imply the following exact finite inequality.

## Corollary 2.2

If \(M_m\le C\kappa^m\) for every \(m\), then every simple two-terminal graph \(H\) satisfies
\[
\boxed{p_H(s,t)\le \kappa^{|E(H)|}.}
\]

### Proof

Apply the cyclic amplification above:
\[
p_H(s,t)^k\le C\kappa^{k|E(H)|}.
\]
Taking \(k\)-th roots and then \(k\to\infty\) gives the result. \(\square\)

Thus a single finite graph satisfying
\[
p_H(s,t)>\kappa^{|E(H)|}
\]
would disprove the conjecture, indeed with a strictly larger exponential base.

The converse is not quite sufficient for the stated \(O\)-bound. The inequality \(P_m\le\kappa^m\) would only give
\[
M_m\le \frac m3\kappa^{m-1}.
\]
Eliminating this factor \(m\) is a genuine issue: equality of exponential growth constants only implies \(M_m\le(\kappa+\varepsilon)^m\) for every fixed \(\varepsilon>0\), not \(M_m=O(\kappa^m)\).

For a finite search, \(p_H(s,t)\) can be computed exactly by the subset recurrence
\[
D[\{s\},s]=1,\qquad
D[S,v]=\sum_{\substack{u\in S\setminus\{v\}\\uv\in E(H)}}D[S\setminus\{v\},u],
\]
with
\[
p_H(s,t)=\sum_{S\ni s,t}D[S,t].
\]
This takes \(O(|V(H)|^2 2^{|V(H)|})\) arithmetic operations. I have not performed a comprehensive enumeration.

# 3. Transfer matrix for the extremal constant

The following gives a self-contained realization of the constant in the conjecture.

Let
\[
X_n=C_n[K_2].
\]
Thus layer \(i\) consists of two adjacent vertices, and every vertex in layer \(i\) is adjacent to both vertices in layers \(i-1\) and \(i+1\). There are
\[
|E(X_n)|=n+4n=5n
\]
edges, and \(X_n\) is \(5\)-regular.

Let \(z_n\) be the number of edge sets \(F\subseteq E(X_n)\) for which every vertex has \(F\)-degree \(0\) or \(2\). Every cycle is such an edge set.

Process the layers cyclically. A boundary state
\[
(a,b)\in\{0,1,2\}^2
\]
records the numbers of selected edges entering the two current vertices from the preceding layer. One then chooses the vertical edge in the layer and a subset of the four edges to the next layer, requiring the completed degrees to lie in \(\{0,2\}\).

After grouping states under interchange of the two vertices, use
\[
A=00,\quad B=\{01,10\},\quad C=\{02,20\},\quad
D=11,\quad E=\{12,21\},\quad F=22.
\]
The equitable quotient of the \(9\times9\) transfer matrix is
\[
Q=
\begin{pmatrix}
1&0&2&4&0&1\\
0&4&0&0&2&0\\
1&0&0&1&0&0\\
1&0&2&2&0&0\\
0&2&0&0&0&0\\
1&0&0&0&0&0
\end{pmatrix}.
\]

It splits according to the parity of \(a+b\). The odd block is
\[
Q_{\rm odd}=
\begin{pmatrix}
4&2\\
2&0
\end{pmatrix},
\]
whose Perron root is
\[
\lambda=2+2\sqrt2.
\]

The even block, in the order \(A,C,D,F\), is
\[
Q_{\rm even}=
\begin{pmatrix}
1&2&4&1\\
1&0&1&0\\
1&2&2&0\\
1&0&0&0
\end{pmatrix}.
\]
Its characteristic polynomial is
\[
x^4-3x^3-7x^2-2x+2.
\]
The Perron root lies between \(4\) and \(4.8\), whereas
\(\lambda>4.8\). Thus the full transfer matrix has spectral radius
\(\lambda\). Consequently,
\[
z_n=\operatorname{tr}(T^n)\le 9\lambda^n.
\]

There is also a matching lower bound from the odd sector. On the four individual odd states \(01,10,12,21\), the transfer matrix is
\[
T_{\rm odd}=
\begin{pmatrix}
2&2&1&1\\
2&2&1&1\\
1&1&0&0\\
1&1&0&0
\end{pmatrix}.
\]
Its nonzero eigenvalues are
\[
2+2\sqrt2,\qquad 2-2\sqrt2.
\]

Every closed configuration in this odd sector is a single cycle. Indeed, it has an odd number of selected edges across every layer boundary. Hence it has an odd number of components winding around the base \(C_n\). Since there are only two vertices per layer, at most two disjoint winding components are possible, so there is exactly one. A further contractible cycle would have to use at most one remaining vertex in each layer; such a subgraph is a subgraph of the base cycle and cannot be contractible.

It follows that
\[
c(X_n)\ge
\operatorname{tr}(T_{\rm odd}^n)
=\lambda^n+(2-2\sqrt2)^n.
\]
Therefore
\[
\boxed{c(X_n)=\Theta(\lambda^n)=\Theta(\kappa^{5n}).}
\]

This also shows that the path-growth reduction in Section 2 is asymptotically tight.

# 4. Bounded-degree configuration models do not produce a typical counterexample

The next result concerns random graphs with a prescribed bounded degree sequence. It is not a deterministic theorem.

## Theorem 4.1

Let \(\boldsymbol d=(d_1,\dots,d_n)\) be degree sequences with
\[
\max_i d_i\le D
\]
for a fixed \(D\), and let \(m=\frac12\sum_i d_i\to\infty\). In the pairing/configuration model, let \(C\) denote the number of vertex-simple cycles of length at least \(3\). Then
\[
\mathbb E C
\le
\exp\!\left((\log b_*+o(1))m\right),
\]
where
\[
\boxed{b_*=\frac5{7^{2/3}}=1.36638\ldots<\kappa.}
\]

For a fixed \(d\ge3\), the \(d\)-regular pairing model has the exact annealed exponential base
\[
b_d=\frac{d-1}{(d+1)^{(d-2)/d}},
\]
and \(b_d\) is maximized over integers \(d\ge3\) at \(d=6\).

## Proof

Put \(L=2m\) and
\[
a_i=d_i(d_i-1).
\]
For \(k\) distinct prescribed vertices, choosing the two ordered stubs used at vertex \(i\) gives \(a_i\) possibilities. The probability that \(k\) prescribed pairs occur in a uniformly random pairing is
\[
\frac1{(L-1)(L-3)\cdots(L-(2k-1))}.
\]
Hence
\[
\mathbb E C_k
=
\frac{(k-1)!}{2}
\frac{e_k(a_1,\dots,a_n)}
{(L-1)(L-3)\cdots(L-(2k-1))},
\]
where \(e_k\) is the \(k\)-th elementary symmetric polynomial.

Let \(p_d\) be the proportion of vertices of degree \(d\), let
\[
\mu=\sum_d dp_d=\frac{2m}{n},
\]
and suppose that a cycle uses \(q_dn\) vertices of degree \(d\). Put
\[
\alpha=\sum_d q_d.
\]
Stirling’s formula gives the following exponential contribution per vertex:
\[
\begin{aligned}
F_p(q)=\;&
\sum_d p_d H\!\left(\frac{q_d}{p_d}\right)
+\alpha\log\alpha
+\sum_d q_d\log(d(d-1))\\
&-\frac{\mu}{2}\log\mu
+\frac{\mu-2\alpha}{2}\log(\mu-2\alpha),
\end{aligned}
\]
where \(H(x)=-x\log x-(1-x)\log(1-x)\).

For every \(z>0\),
\[
H(r)+r\log z\le\log(1+z).
\]
Taking
\[
t=\frac{\alpha}{\mu-2\alpha}
\]
and \(z=t\,d(d-1)\) yields
\[
F_p(q)\le
\Phi_p(t):=
\sum_d p_d\log(1+t\,d(d-1))
-\frac\mu2\log(1+2t).
\]

Now set \(w_d=p_dd/\mu\). These are nonnegative and sum to one, ignoring degree-zero vertices. Then
\[
\frac{2\Phi_p(t)}{\mu}
=
\sum_{d\ge1}w_d
\left[
\frac2d\log(1+t\,d(d-1))
-\log(1+2t)
\right].
\]
Consequently,
\[
\frac{2\Phi_p(t)}{\mu}
\le
\max_{d\ge1}
\left[
\frac2d\log(1+t\,d(d-1))
-\log(1+2t)
\right].
\]

For \(d\ge3\), the expression in brackets is maximized at
\[
t=\frac1{d-1},
\]
with value
\[
\log b_d
=
\log(d-1)-\frac{d-2}{d}\log(d+1).
\]
For \(d=1,2\), the supremum is \(0\).

A direct exact comparison for \(d=3,\dots,7\), followed by differentiation for real \(d\ge7\), shows that the largest integer value is attained at \(d=6\):
\[
b_* = b_6=\frac5{7^{2/3}}.
\]
Indeed, for
\[
h(x)=\log(x-1)-\left(1-\frac2x\right)\log(x+1),
\]
one has \(h'(x)<0\) for \(x\ge7\).

Finally,
\[
b_*^{15}=\frac{5^{15}}{7^{10}}
<112
<56+40\sqrt2
=(2+2\sqrt2)^3
=\kappa^{15},
\]
so \(b_*<\kappa\).

There are only polynomially many possible degree-use types \(q\), so summing over \(k\) and over all types changes the estimate only by \(\exp(o(m))\). This proves the upper bound.

For the \(d\)-regular model, the exponent for cycles of length \(\alpha n\) is
\[
F_d(\alpha)=
-(1-\alpha)\log(1-\alpha)
+\alpha\log(d(d-1))
-\frac d2\log d
+\frac{d-2\alpha}{2}\log(d-2\alpha).
\]
It is strictly concave and is maximized at
\[
\alpha=\frac d{d+1}.
\]
At this point
\[
F_d^{\max}
=
\frac d2\log(d-1)-\frac{d-2}{2}\log(d+1),
\]
which, after dividing by \(m/n=d/2\), gives \(\log b_d\). \(\square\)

## Corollary 4.2

Fix \(d\ge3\), and let \(G\) be a uniformly random simple \(d\)-regular graph. For every \(r>b_d\),
\[
\Pr\big(c(G)>r^{|E(G)|}\big)\longrightarrow0.
\]
In particular, one may choose \(r<\kappa\).

Indeed, in the fixed-\(d\) pairing model the probability of simplicity tends to
\[
\exp\!\left(-\frac{d^2-1}{4}\right)>0,
\]
and Markov’s inequality applies before conditioning.

Thus typical regular graphs, including the potentially dangerous degrees \(5\) and \(6\), have a strict exponential margin:
\[
b_5=\frac4{6^{3/5}}=1.3651\ldots,\qquad
b_6=\frac5{7^{2/3}}=1.36638\ldots<\kappa.
\]

# 5. Remaining gap

The configuration-model theorem does not constrain exponentially rare structured graphs. The strip \(C_n[K_2]\) itself is \(5\)-regular and has rate \(\kappa\), strictly above the \(5\)-regular annealed rate. Thus a deterministic extremal argument must exploit more than the degree distribution.

The path reduction identifies a concrete sharp target:
\[
p_H(s,t)\le \kappa^{|E(H)|}
\quad\text{for every finite simple two-terminal graph }H.
\]
Proving this would settle the exponential growth constant, but an additional argument would still be needed to remove the possible polynomial prefactor and obtain the conjectured \(O(\kappa^m)\).

Accordingly, neither a complete proof nor a counterexample is obtained. I have not independently verified whether the path reduction or the annealed calculation already appears in the cited literature, so no novelty claim is made.