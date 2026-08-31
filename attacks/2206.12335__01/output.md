```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact threshold remains open; I prove a uniform mesoscopic-component bound and the value 1/2 for the natural independent equality-colour subclass.",
  "would_publish": false,
  "caveats": "No improvement on 1/2 <= p_giant <= 0.5847; arbitrary adjacent-edge dependence obstructs the required coalescence step."
}
```

# 1. Statement and outcome

Write \(N=2^n\), and let \(L_1(H)\) denote the order of the largest component of a spanning subgraph \(H\subseteq Q_n\). I use the standard formulation
\[
p_{\mathrm{giant}}
 =
 \inf\left\{p:\exists \gamma>0\text{ such that }
 \inf_{\mu\in\mathcal M_{1,\ge p}(Q_n)}
 \Pr_\mu\bigl(L_1\ge \gamma N\bigr)\longrightarrow 1
 \right\},
\]
where \(\mathcal M_{1,\ge p}(Q_n)\) is the class of 1-independent laws with every edge open with probability at least \(p\).

I do not determine \(p_{\mathrm{giant}}\). The rigorous interval remains
\[
\frac12\le p_{\mathrm{giant}}\le 0.5847.
\]

The contributions below are:

1. an explicit sharp construction proving the lower bound \(1/2\);
2. an unconditional, uniform lower bound \(L_1\ge N^{p-o(1)}\), together with a stronger mass statement;
3. a proof that the threshold is exactly \(1/2\) for independent equality-colour models;
4. a structural theorem showing why endpoint-factor counterexamples based on deterministic type confinement cannot work above \(1/2\);
5. an exact square calculation illustrating the remaining local-dependence obstruction.

## Marginal normalization

For upper-bound purposes one may assume every edge has marginal exactly \(p\). Indeed, if \(X_e\) has marginal \(p_e\ge p\), independently retain an open edge \(e\) with probability \(p/p_e\). The resulting process \(Y\subseteq X\) is still 1-independent and has every marginal exactly \(p\). Thus a giant in every exact-\(p\) thinning implies a giant in the original process.

# 2. A sharp lower-bound construction at \(p=1/2\)

Let
\[
L_k=\{x\in\{0,1\}^n:|x|=k\}
\]
be the \(k\)-th Hamming layer. Assign independent vertex colours as follows:

- if \(v\in L_{2j}\), give \(v\) the deterministic colour \(j\);
- if \(v\in L_{2j+1}\), give \(v\) colour \(j\) or \(j+1\), independently and with probability \(1/2\) each.

Declare an edge open exactly when its endpoints have the same colour.

This is 1-independent: edge sets with disjoint vertex supports depend on disjoint collections of independent vertex colours.

Every edge joins consecutive Hamming layers, one even and one odd. If it joins \(L_{2j}\) to \(L_{2j+1}\), its endpoints agree exactly when the odd-layer endpoint chooses colour \(j\). If it joins \(L_{2j-1}\) to \(L_{2j}\), they agree exactly when the odd-layer endpoint chooses colour \(j\). Hence every edge is open with probability exactly \(1/2\).

Every open path is monochromatic. Colour \(j\) occurs only in
\[
L_{2j-1}\cup L_{2j}\cup L_{2j+1}.
\]
Consequently, deterministically,
\[
L_1\le 3\max_k\binom nk
   =O\left(\frac{2^n}{\sqrt n}\right)
   =o(2^n).
\]
Thus there is no giant, even with probability one. This proves
\[
p_{\mathrm{giant}}\ge \frac12.
\]

The construction also identifies the basic extremal mechanism at \(1/2\): the dominant colour can change from one slab of Hamming layers to the next through a \(50\)-\(50\) transition layer.

# 3. An unconditional mesoscopic-component theorem

The following applies to every 1-independent model, without symmetry or endpoint-factor assumptions.

## Theorem 3.1

Let \(H\) be a 1-independent random subgraph of \(Q_n\) in which every edge has open probability at least \(p\). For every \(\varepsilon>0\),
\[
\Pr\left(L_1(H)\ge N^{p-\varepsilon}\right)
 \ge 1-n\exp(-\varepsilon^2N).
\]

More generally, for \(0\le a<p-\varepsilon\), with the same probability at least
\[
\frac{p-\varepsilon-a}{1-a}\,N
\]
vertices belong to components of order at least \(N^a\).

### Proof

For each coordinate \(i\), let \(E_i\) be the perfect matching consisting of all edges in direction \(i\). Since its edges are pairwise vertex-disjoint, their states are mutually independent under a 1-independent law. Thus, writing
\[
X_i=|E(H)\cap E_i|,
\]
Hoeffding's inequality gives
\[
\Pr\left(X_i<(p-\varepsilon)\frac N2\right)
 \le \exp(-\varepsilon^2N).
\]
A union bound over the \(n\) coordinates gives, except with probability at most \(n e^{-\varepsilon^2N}\),
\[
e(H)=\sum_{i=1}^nX_i
 \ge (p-\varepsilon)\frac{nN}{2}.
\tag{3.1}
\]

We use the standard edge-isoperimetric inequality
\[
e_{Q_n}(S)\le \frac{|S|\log_2|S|}{2}
\tag{3.2}
\]
for every \(S\subseteq V(Q_n)\). For completeness, it follows by induction after splitting \(Q_n\) into two \((n-1)\)-cubes: if the two parts of \(S\) have orders \(a\ge b\), there are at most \(b\) crossing edges, and
\[
a\log_2a+b\log_2b+2b
 \le (a+b)\log_2(a+b),
\]
because the binary entropy satisfies \(h_2(t)\ge 2t\) for \(0\le t\le1/2\).

Let the component orders of \(H\) be \(s_1,\dots,s_m\). Applying (3.2) to each component,
\[
e(H)\le \frac12\sum_{j=1}^m s_j\log_2s_j.
\tag{3.3}
\]
Equivalently,
\[
\frac1N\sum_{v\in V(Q_n)}\log_N|C_H(v)|
 =
 \frac1{nN}\sum_j s_j\log_2s_j
 \ge \frac{2e(H)}{nN}.
\tag{3.4}
\]
By (3.1), the right-hand side is at least \(p-\varepsilon\).

If \(L_1=L\), then the left-hand side of (3.4) is at most \(\log_NL\), proving
\[
L\ge N^{p-\varepsilon}.
\]

Now let \(\beta N\) vertices belong to components of order at least \(N^a\). Since \(\log_N|C(v)|<a\) for the remaining vertices and is at most \(1\) for all vertices,
\[
p-\varepsilon
 \le a(1-\beta)+\beta.
\]
Hence
\[
\beta\ge\frac{p-\varepsilon-a}{1-a}.
\]
This proves the theorem. \(\square\)

## Consequence above \(1/2\)

Taking \(a=1/2\) and \(\varepsilon=o(1)\), every model with fixed \(p>1/2\) satisfies, uniformly with high probability,
\[
\left|\left\{v:|C_H(v)|\ge \sqrt N\right\}\right|
 \ge (2p-1-o(1))N.
\tag{3.5}
\]
Thus a positive fraction of all vertices is covered by at most \(\sqrt N\) components of order at least \(\sqrt N\).

The open problem is precisely the missing coalescence step: (3.5) does not force one of these components to have linear order.

# 4. A site-percolation lemma

The following standard fact is included with an argument because it is used in the restricted-model result below.

## Lemma 4.1

For every fixed \(r>0\), independent site percolation of density \(r\) on \(Q_n\) has a component of order at least \(c_r2^n\) with probability tending to one, for some \(c_r>0\).

### Proof

Expose the occupied vertices in two independent rounds of densities \(r_1,r_2>0\), chosen so that
\[
1-r=(1-r_1)(1-r_2).
\]

In the first round, put an edge in \(H_1\) exactly when both its endpoints were retained. This is a 1-independent edge process with edge marginal
\[
s=r_1^2.
\]
Apply Theorem 3.1 with
\[
a=\frac s2,\qquad \varepsilon=\frac s4.
\]
With high probability, at least
\[
\beta N,\qquad
\beta=\frac{s/4}{1-s/2}>0,
\tag{4.1}
\]
vertices lie in first-round components of order at least \(N^a\). Let \(\mathcal K\) be this collection of components. Then
\[
|\mathcal K|\le N^{1-a}.
\tag{4.2}
\]

We need a deterministic path-packing fact. For every fixed \(\delta>0\), there are constants \(c_\delta,C_\delta>0\) such that any two disjoint sets \(A,B\subseteq Q_n\) with
\[
|A|,|B|\ge\delta N
\]
are joined by at least
\[
c_\delta\frac N{\sqrt n}
\]
pairwise vertex-disjoint paths of length at most \(C_\delta\sqrt n\).

Indeed, the vertex-isoperimetric theorem for the cube gives
\[
|\partial_vU|\ge c_\delta\frac N{\sqrt n}
\]
whenever \(\delta N/2\le |U|\le(1-\delta/2)N\). Hence every \(A\)-\(B\) vertex separator has order \(\Omega_\delta(N/\sqrt n)\). Menger's theorem gives that many vertex-disjoint paths. Since the paths are disjoint and use at most \(N\) vertices altogether, at least half have length \(O_\delta(\sqrt n)\).

Condition on the first round. Consider any bipartition of \(\mathcal K\) whose two unions \(A,B\) both have order at least
\[
\delta N,\qquad \delta=\beta/3.
\]
Take the above family of short, vertex-disjoint \(A\)-\(B\) paths. Requiring every internal vertex of one path to be selected in the second round has probability at least
\[
r_2^{C_\delta\sqrt n}=\exp(-O(\sqrt n)).
\]
These events are independent for the vertex-disjoint paths. Therefore the probability that none is activated is at most
\[
\exp\left(
 -c_\delta\frac N{\sqrt n}\,r_2^{C_\delta\sqrt n}
\right)
 =
 \exp\bigl(-N^{1-o(1)}\bigr).
\tag{4.3}
\]
There are at most
\[
2^{|\mathcal K|}
 \le \exp\bigl((\log2)N^{1-a}\bigr)
\]
bipartitions. Since \(a>0\), the bound in (4.3) beats this count. Thus, with high probability, no bipartition of \(\mathcal K\) having linear mass on both sides remains disconnected after the second round.

If no final component contained at least \(\beta N/3\) vertices of the union in (4.1), the final components could be greedily partitioned into two families each containing at least \(\beta N/3\) such vertices. This contradicts the preceding conclusion. Hence a final component has order at least \(\beta N/3\). \(\square\)

# 5. Exact threshold for independent equality-colour models

Consider the following natural subclass. Each vertex \(v\) independently receives a colour \(Z_v\) from an arbitrary finite colour set, with a distribution \(\pi_v\) which may depend on \(v\). Declare
\[
uv\text{ open}\quad\Longleftrightarrow\quad Z_u=Z_v.
\tag{5.1}
\]
These are 1-independent models.

## Lemma 5.1: the \(1/2\) dot-product barrier

Let \(x,y\) be probability vectors. If
\[
\langle x,y\rangle>\frac12,
\]
then \(x\) and \(y\) have the same unique coordinate of maximum mass. Moreover that maximum is at least \(\langle x,y\rangle\).

### Proof

Certainly
\[
\langle x,y\rangle\le\max_i x_i,\qquad
\langle x,y\rangle\le\max_i y_i,
\]
so both vectors have a unique coordinate of mass greater than \(1/2\).

Let these coordinates be \(i\) and \(j\), with masses \(a=x_i>1/2\) and \(b=y_j>1/2\). If \(i\ne j\), then \(y_i\le1-b\) and \(y_k\le b\) for \(k\ne i\), whence
\[
\langle x,y\rangle
 \le a(1-b)+b(1-a)
 =\frac12-2\left(a-\frac12\right)\left(b-\frac12\right)
 <\frac12,
\]
a contradiction. \(\square\)

## Theorem 5.2

For the equality-colour class (5.1), the giant-component threshold is exactly
\[
p_{\mathrm{giant}}^{\mathrm{eq}}=\frac12.
\]

### Proof

The lower-bound construction in Section 2 belongs to this class.

Now suppose every edge has open probability at least \(p>1/2\). For every edge \(uv\),
\[
\Pr(uv\text{ open})
 =\sum_c\pi_u(c)\pi_v(c)
 =\langle\pi_u,\pi_v\rangle
 \ge p.
\]
By Lemma 5.1, the unique dominant colours at \(u\) and \(v\) agree. Since \(Q_n\) is connected, there is a single global colour \(c_\star\) such that
\[
\pi_v(c_\star)\ge p
\qquad\text{for every }v.
\tag{5.2}
\]

The indicators \(\mathbf 1_{\{Z_v=c_\star\}}\) are independent, though not necessarily identically distributed. Independently thin them to obtain an i.i.d. site-percolation set of density exactly \(p\). Every cube edge with both endpoints in this thinned set is open under (5.1). Lemma 4.1 therefore supplies an open component of order \(c_pN\) with high probability. \(\square\)

This special case captures the slab construction exactly: at \(p=1/2\), dominant colours may tie and can change between successive Hamming layers; strict inequality prevents such a change.

# 6. A broader endpoint-factor obstruction

The preceding dot-product mechanism extends beyond equality colours.

Suppose each vertex \(v\) independently receives a finite type \(Z_v\), and each edge \(uv\) is determined by \(Z_u,Z_v\) and an independent edge seed. Form the deterministic support graph \(\Gamma\) whose vertices are pairs \((v,a)\), and where
\[
(u,a)(v,b)\in E(\Gamma)
\]
whenever \(uv\in E(Q_n)\) and the conditional probability that \(uv\) is open given \(Z_u=a,Z_v=b\) is positive.

Let \(\mathscr D\) be the components of \(\Gamma\), and define
\[
x_{v,D}
 =\Pr\bigl((v,Z_v)\in D\bigr).
\]
For an edge \(uv\), openness implies that \((u,Z_u)\) and \((v,Z_v)\) lie in the same support component. Independence of \(Z_u,Z_v\) therefore gives
\[
\Pr(uv\text{ open})
 \le \sum_{D\in\mathscr D}x_{u,D}x_{v,D}.
\tag{6.1}
\]

If every edge has probability at least \(p>1/2\), Lemma 5.1 applied to the probability vectors \((x_{u,D})_D\) and \((x_{v,D})_D\) shows that their dominant support component is the same. Connectivity of \(Q_n\) gives one deterministic support component \(D_\star\) such that
\[
x_{v,D_\star}\ge p
\qquad\text{for every }v.
\tag{6.2}
\]
Consequently, with high probability, at least \((p-o(1))N\) sampled type-vertices belong to \(D_\star\).

Thus, above \(1/2\), an endpoint-factor counterexample cannot work merely by confining every open component to a deterministic type class of sublinear mass. There must be a type class of linear mass.

The limitation is important: the sampled vertices belonging to \(D_\star\) need not form one open component. The support graph records only which transitions are possible, not which occur in a particular realization. This is exactly where the argument stops for general endpoint rules.

# 7. An exact local obstruction on a square

Let a square have cyclic edges \(e_1,e_2,e_3,e_4\), and consider connectivity between the opposite vertices incident with \(e_1,e_4\) and \(e_2,e_3\).

For any edge marginals at least \(p\),
\[
\Pr(\text{opposite vertices connected})
 \ge \Pr(e_1,e_2\text{ both open})
 \ge 2p-1.
\tag{7.1}
\]
This bound is sharp even under 1-independence.

Let \(q=1-p\), and put the following distribution on the open edge set:
\[
\begin{array}{c|c}
\text{open set}&\text{probability}\\ \hline
\{e_1,e_3\}&q^2\\
\{e_1,e_4\}&pq\\
\{e_2,e_3\}&pq\\
\{e_2,e_4\}&q^2\\
\{e_1,e_2,e_3,e_4\}&2p-1.
\end{array}
\tag{7.2}
\]
The probabilities sum to one, every edge has marginal \(p\), and
\[
\Pr(e_1=e_3=1)=q^2+(2p-1)=p^2,
\]
with the analogous identity for \(e_2,e_4\). Thus the two pairs of disjoint edges are independent, which is exactly the nontrivial 1-independence condition on \(C_4\).

In (7.2), the designated opposite vertices are connected only in the all-open outcome, so their connection probability is exactly \(2p-1\).

This shows that a proof based only on two-terminal estimates in individual squares cannot obtain stronger local amplification. The distribution (7.2) is only a square law; no claim is made that it extends consistently to all overlapping squares of \(Q_n\).

# 8. Precise remaining gap

For \(p>1/2\), Theorem 3.1 yields a positive linear mass contained in at most \(\sqrt N\) components of size at least \(\sqrt N\). If there is no giant, unions of components produce a balanced cut all of whose crossing edges are closed.

For a fixed cut and a fixed matching \(M\) in its edge boundary, 1-independence gives
\[
\Pr(M\text{ is entirely closed})\le(1-p)^{|M|}.
\]
That does not suffice for an adaptive cut determined by the realization. Balanced Hamming-ball cuts can have boundary matching number only \(\Theta(N/\sqrt n)\), while there are far too many possible cuts for a direct union bound.

The sprinkling argument in Lemma 4.1 succeeds because the second site round is independent of the first-round components. An arbitrary 1-independent edge process has no comparable conditional insertion tolerance: conditioning on an incident open edge can force another incident edge to be closed. The square law (7.2) demonstrates the severity of this local negative dependence.

Therefore the required coalescence of the mesoscopic components remains unproved, and this attack does not improve the currently stated numerical interval.