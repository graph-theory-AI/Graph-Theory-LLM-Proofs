```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured order holds when the graph order is a fixed multiple of its minimum degree, with a sharp leading asymptotic in the dense Dirac regime.",
  "would_publish": false,
  "caveats": "The constants are not uniform as |V(G)|/δ(G) grows, so the unrestricted conjecture remains unresolved; literature novelty of these special cases has not been checked."
}
```

# A positive-density result

All graphs below are finite and simple, and logarithms are natural.

Write \(\operatorname{ch}(G)\) for the largest \(r\) such that \(G\) contains a cyclic \(K_r\)-minor. For \(r\ge 3\), the contraction definition has the following equivalent formulation: there is a cycle \(C\) and a partition
\[
V(C)=I_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}I_r
\]
into nonempty cyclic intervals such that every two distinct intervals are joined by an edge of \(G\). Indeed, the branch sets of contractions along a cycle are precisely such intervals.

In particular,
\[
\operatorname{ch}(G)\le h(G),
\]
where \(h(G)\) is the ordinary Hadwiger number.

I obtain the following two special cases. Unlike the supplied attempt's sufficient condition, neither assumes a mixing property of a preselected Hamilton cycle.

### Theorem A: positive density

For every fixed \(c\in(0,1)\), there is a constant \(\kappa(c)>0\) such that every sufficiently large \(n\)-vertex graph of average degree at least \(cn\) satisfies
\[
\operatorname{ch}(G)\ge \kappa(c)\frac{n}{\sqrt{\ln n}}.
\tag{1}
\]

Consequently, for every fixed \(M>1\), the conjectured bound holds for graphs satisfying
\[
|V(G)|\le M\delta(G).
\]
More precisely, within this class, minimum degree \(O_M(\ell\sqrt{\ln\ell})\) guarantees a cyclic \(K_\ell\)-minor.

### Theorem B: sharp asymptotics above the Dirac threshold

For every fixed \(p\in(1/2,1)\),
\[
\min_{\substack{|V(G)|=n\\ \delta(G)\ge pn}}
\operatorname{ch}(G)
=
\left(\sqrt{-\ln(1-p)}+o(1)\right)\frac{n}{\sqrt{\ln n}}.
\tag{2}
\]

The lower bound in (2) is uniform over all graphs in the indicated class. Random graphs give the matching upper bound.

The principal limitation is that Theorem A's constant depends on the density \(c\). It therefore does not settle the case \(|V(G)|/\delta(G)\to\infty\).

---

# 1. Random groups with almost all pairwise adjacencies

The following elementary observation is useful because requiring *every* pair of initially chosen groups to be adjacent is unnecessarily expensive: one can delete a small number of defective groups.

### Lemma 1

Fix \(p\in(0,1)\) and \(\eta\in(0,1)\), and put
\[
q=1-p,\qquad \rho=-\ln q.
\]
Let \(F\) be an \(N\)-vertex graph with \(\delta(F)\ge pN\). Set
\[
s=\left\lceil
\sqrt{\frac{(1+\eta)\ln N}{(1-\eta)\rho}}
\right\rceil.
\tag{3}
\]
Suppose \(k=\Theta(N/s)\) and \(ks\le N\). Choose uniformly an ordered family of disjoint \(s\)-sets
\[
A_1,\ldots,A_k.
\]

With probability tending to one, deleting \(o(k)\) of these sets leaves a pairwise adjacent family.

Moreover, suppose a property \(\mathcal Q\) is possessed by a uniformly random \(s\)-subset of \(V(F)\) with probability \(1-o(1)\). The retained sets can all be required to possess \(\mathcal Q\).

#### Proof

For an \(s\)-set \(A\), define
\[
Z(A)=\{v\in V(F):N_F(v)\cap A=\varnothing\}.
\]
For a uniformly random \(A\),
\[
\mathbb E|Z(A)|
=
\sum_{v\in V(F)}
\frac{\binom{N-d_F(v)}s}{\binom Ns}
\le Nq^s.
\]
Call \(A\) good if
\[
|Z(A)|\le Nq^{(1-\eta)s}.
\]
Markov's inequality gives
\[
\Pr(A\text{ is not good})\le q^{\eta s}=o(1).
\tag{4}
\]

Conditional on \(A_i\), the set \(A_j\) is a uniformly random \(s\)-subset of \(V(F)\setminus A_i\). If \(A_i\) is good, then
\[
\begin{aligned}
\Pr(E_F(A_i,A_j)=\varnothing\mid A_i)
&\le
\left(\frac{|Z(A_i)|}{N-s}\right)^s\\
&\le
\left(\frac N{N-s}\right)^s
q^{(1-\eta)s^2}\\
&\le (1+o(1))N^{-1-\eta},
\end{aligned}
\tag{5}
\]
using (3) and \(s=O(\sqrt{\ln N})\).

Let \(B\) count non-good sets and \(D\) count nonadjacent pairs of good sets. Then
\[
\mathbb EB=o(k)
\]
and
\[
\mathbb ED
\le (1+o(1))\binom{k}{2}N^{-1-\eta}
=o(k).
\]
Thus \(B+D=o(k)\) with high probability. Delete the non-good sets and then one endpoint of every remaining nonadjacent pair.

If \(\mathcal Q\) is imposed, the expected number of sets failing it is also \(o(k)\), so these can be deleted as well. \(\square\)

The lemma alone does **not** give a minor: the sets need not be connected. The next argument supplies paths through them.

---

# 2. Proof of Theorem A

## 2.1. Extracting a robust dense core

Let \(G\) have \(n\) vertices and average degree at least \(cn\). Among its nonempty induced subgraphs, choose \(H\) maximizing
\[
D=\frac{e(H)}{|H|^{3/2}}.
\]
Write \(m=|H|\). Since
\[
D\ge \frac{e(G)}{n^{3/2}}\ge \frac c2\sqrt n
\]
and
\[
D\le \frac12\sqrt m,
\]
we have
\[
m\ge c^2n.
\tag{6}
\]

Put
\[
a=\frac{c^2}{2},\qquad
\theta=1-\frac1{\sqrt2},\qquad
b=\theta a.
\]
Then
\[
D\sqrt m\ge an.
\tag{7}
\]

For each \(v\in V(H)\), maximality gives
\[
e(H)-d_H(v)\le D(m-1)^{3/2}.
\]
Consequently,
\[
d_H(v)
\ge D\bigl(m^{3/2}-(m-1)^{3/2}\bigr)
\ge D\sqrt m
\ge an.
\tag{8}
\]

Also, if \(S\subseteq V(H)\) and \(1\le s=|S|\le m/2\), then
\[
\begin{aligned}
e_H(S,V(H)\setminus S)
&\ge D\bigl(m^{3/2}-s^{3/2}-(m-s)^{3/2}\bigr)\\
&\ge D\left(s\sqrt m-s\sqrt{m/2}\right)\\
&=\theta D\sqrt m\,s\\
&\ge bn|S|.
\end{aligned}
\tag{9}
\]

Thus \(H\) has linear minimum degree and a robust edge-expansion property.

### Claim 2

There is a constant \(L=L(c)\) such that
\[
\operatorname{diam}(H-X)\le L
\tag{10}
\]
whenever \(|X|\le bn/2\).

One may take
\[
L=2\left\lceil\frac1b\right\rceil.
\]

#### Proof

Put \(J=H-X\). For \(S\subseteq V(J)\) with \(1\le |S|\le |J|/2\), (9) gives
\[
e_J(S,V(J)\setminus S)
\ge bn|S|-|X||S|
\ge \frac{bn}{2}|S|.
\]
Each vertex outside \(S\) sends at most \(|S|\) edges into \(S\), so
\[
|N_J(S)\setminus S|\ge \frac{bn}{2}.
\tag{11}
\]

Therefore, while a distance ball has at most \(|J|/2\) vertices, each additional radius adds at least \(bn/2\) vertices. Every ball of radius \(\lceil1/b\rceil\) consequently has more than \(|J|/2\) vertices. Any two such balls intersect, proving (10). \(\square\)

## 2.2. Choosing terminals and routing a cycle

Apply Lemma 1 to \(H\) with density parameter \(a\) and \(\eta=1/2\). This is legitimate because (8) implies
\[
\delta(H)\ge an\ge am.
\]
Let
\[
\rho_a=-\ln(1-a),\qquad
s=\left\lceil\sqrt{\frac{3\ln m}{\rho_a}}\right\rceil,
\]
and choose
\[
k=\left\lfloor\frac{bn}{4Ls}\right\rfloor
\]
disjoint random terminal sets, each of size \(s\). Notice that \(ks\le m\), and \(k=\Theta(m/s)\).

Lemma 1 supplies
\[
t=(1-o(1))k
\]
pairwise adjacent terminal sets
\[
A_1,\ldots,A_t.
\]

Order all their terminals cyclically, placing all terminals of \(A_i\) consecutively. Let
\[
T=ts
\]
be the total number of terminals.

We now join successive terminals by internally vertex-disjoint paths, in their specified cyclic order. At a routing step, forbid:

* every terminal except the two current endpoints;
* all internal vertices used in previous routing paths.

If each previous routing path has length at most \(L\), fewer than
\[
T+(T-1)(L-1)\le LT
\le Lks
\le \frac{bn}{4}
\]
vertices are forbidden. Claim 2 therefore supplies the next path of length at most \(L\). This works also for the final connection back to the first terminal.

The resulting union is a simple cycle. On that cycle, the terminals of each \(A_i\) occur consecutively relative to the other terminal sets. Assign the intervening nonterminal vertices to obtain cyclic intervals \(I_i\supseteq A_i\). Since every pair \(A_i,A_j\) is adjacent, every pair \(I_i,I_j\) is adjacent. Hence these intervals form a cyclic \(K_t\)-model.

Using (6), so that \(\ln m=\ln n+O_c(1)\), we obtain
\[
\operatorname{ch}(G)
\ge
\left(
\frac{b}{4L}\sqrt{\frac{\rho_a}{3}}-o(1)
\right)\frac{n}{\sqrt{\ln n}}.
\]
For example,
\[
\kappa(c)=\frac{b}{8L}\sqrt{\frac{\rho_a}{3}}
\]
works for all sufficiently large \(n\). This proves Theorem A. \(\square\)

### Minimum-degree consequence

Suppose \(d=\delta(G)\) and \(n\le Md\), where \(M>1\) is fixed. Theorem A applies with \(c=1/M\), giving
\[
\operatorname{ch}(G)\ge \kappa(1/M)\frac{n}{\sqrt{\ln n}}.
\]
Since \(x/\sqrt{\ln x}\) is increasing for sufficiently large \(x\), and \(n>d\),
\[
\operatorname{ch}(G)\ge \kappa(1/M)\frac{d}{\sqrt{\ln d}}.
\tag{12}
\]
Inverting (12) yields the asserted \(O_M(\ell\sqrt{\ln\ell})\) threshold.

---

# 3. The sharp lower bound in the Dirac regime

Fix \(p>1/2\), and suppose \(\delta(G)\ge pn\). Put
\[
\rho=-\ln(1-p).
\]

Fix \(\eta\in(0,1)\), and choose \(s\) as in (3). Set
\[
r=\left\lceil\frac{n}{(\ln n)^{1/4}}\right\rceil,
\qquad
k=\left\lfloor\frac{n-r}{s}\right\rfloor.
\]
Choose uniformly a reserve set \(R\) of size \(r\), and then disjoint \(s\)-sets
\[
A_1,\ldots,A_k
\]
from the remaining vertices. Their joint marginal distribution is the uniform distribution used in Lemma 1.

Two additional properties hold with high probability.

## 3.1. Almost all blocks have Hamilton paths

For a uniformly random \(s\)-set \(A\), conditional on \(v\in A\), the degree of \(v\) in \(G[A]\) is hypergeometric with mean at least \(p(s-1)\). Since \(p>1/2\), a hypergeometric lower-tail bound gives
\[
\Pr\bigl(\delta(G[A])<s/2\bigr)
\le s e^{-\gamma_p s}
=o(1)
\tag{13}
\]
for some constant \(\gamma_p>0\).

Dirac's theorem therefore implies that a uniformly random block induces a Hamiltonian graph with probability \(1-o(1)\). By the additional-property clause of Lemma 1, we may retain
\[
t=(1-o(1))k
\tag{14}
\]
pairwise adjacent blocks, each having a Hamilton path.

## 3.2. The reserve joins arbitrary endpoint pairs

For distinct vertices \(u,v\),
\[
|N_G(u)\cap N_G(v)|
\ge d_G(u)+d_G(v)-n
\ge (2p-1)n.
\]
A hypergeometric tail bound, followed by a union bound over all vertex pairs, shows that with high probability
\[
|R\cap N_G(u)\cap N_G(v)|
\ge \frac{2p-1}{2}\,r
\tag{15}
\]
simultaneously for every distinct \(u,v\). Here the failure probability for an individual pair is \(e^{-\Omega_p(r)}\).

Moreover,
\[
\frac{r}{k}=\Theta_p\bigl((\ln n)^{1/4}\bigr)\longrightarrow\infty.
\tag{16}
\]

Choose a Hamilton path \(P_i\) in each retained \(G[A_i]\), with endpoints \(u_i,v_i\). By (15) and (16), we can greedily choose distinct vertices
\[
x_i\in R\cap N_G(v_i)\cap N_G(u_{i+1}),
\]
with indices interpreted cyclically.

Thus
\[
P_1x_1P_2x_2\cdots P_tx_t
\]
is a cycle. Its intervals
\[
V(P_i)\cup\{x_i\}
\]
are pairwise adjacent, because the original \(A_i\)'s were pairwise adjacent. Hence
\[
\operatorname{ch}(G)\ge t.
\]

From (3), (14), and \(r=o(n)\),
\[
\operatorname{ch}(G)
\ge
\left(
\sqrt{\frac{1-\eta}{1+\eta}\rho}-o(1)
\right)\frac{n}{\sqrt{\ln n}}.
\]
Since this holds for every fixed \(\eta>0\),
\[
\operatorname{ch}(G)
\ge
\left(\sqrt{\rho}-o(1)\right)\frac{n}{\sqrt{\ln n}}.
\tag{17}
\]

This proves the lower half of Theorem B.

---

# 4. Matching random-graph obstruction

The ordinary-minor obstruction from the supplied attempt is valid. I reprove the needed version here, including its leading constant.

### Lemma 3

Let \(p_n\to p\in(0,1)\), put \(\rho=-\ln(1-p)\), and let \(G_n\sim G(n,p_n)\). Then, with high probability,
\[
h(G_n)\le
\left(\sqrt{\rho}+o(1)\right)\frac{n}{\sqrt{\ln n}}.
\tag{18}
\]

#### Proof

Fix \(A>\sqrt{\rho}\), and put
\[
t=\left\lceil A\frac{n}{\sqrt{\ln n}}\right\rceil.
\]
Choose a sufficiently small fixed \(\alpha>0\) such that
\[
\frac{\rho}{A^2(1-\alpha)^2}<1.
\tag{19}
\]

Consider any fixed family of pairwise disjoint nonempty sets
\[
B_1,\ldots,B_t.
\]
At least \(\alpha t\) of them have size at most
\[
S=\frac{n}{(1-\alpha)t}.
\tag{20}
\]
Otherwise the larger sets alone would contain more than \(n\) vertices.

Write \(q_n=1-p_n\). By (19)–(20), there is a fixed \(\lambda<1\) such that, for all sufficiently large \(n\),
\[
q_n^{S^2}\ge n^{-\lambda}.
\]
For every pair of small sets,
\[
\Pr(E(B_i,B_j)=\varnothing)
=q_n^{|B_i||B_j|}
\ge n^{-\lambda}.
\]
The adjacency events for different unordered pairs of branch sets use disjoint random edge sets and are independent. Therefore the probability that the fixed family is pairwise adjacent is at most
\[
\exp\bigl(-\Omega(t^2n^{-\lambda})\bigr)
=
\exp\left(-\Omega\left(\frac{n^{2-\lambda}}{\ln n}\right)\right).
\tag{21}
\]

There are at most \((t+1)^n\) ordered families of disjoint sets, by assigning each vertex a label in \(\{0,1,\ldots,t\}\). Because \(\lambda<1\), a union bound using (21) tends to zero.

Thus, with high probability, there is no pairwise adjacent family of \(t\) disjoint nonempty sets—even without requiring their connectivity. In particular there is no \(K_t\)-minor. Letting \(A\downarrow\sqrt\rho\) proves (18). \(\square\)

To finish Theorem B, choose
\[
p_n=p+n^{-1/4}.
\]
For all sufficiently large \(n\), this is less than one, and binomial concentration gives
\[
\delta(G(n,p_n))\ge pn
\]
with high probability. Lemma 3 and \(\operatorname{ch}\le h\) give the matching upper bound in (2).

## The universal necessary order

The same calculation recovers the lower bound
\[
f(\ell)\ge(\beta-o(1))\ell\sqrt{\ln\ell},
\qquad
\beta=\max_{0<p<1}
\frac{p}{\sqrt{-\ln(1-p)}}=0.638\ldots .
\tag{22}
\]

Indeed, fix \(p\), choose \(c<1/\sqrt{-\ln(1-p)}\), and take
\[
n=\left\lfloor c\ell\sqrt{\ln\ell}\right\rfloor.
\]
Lemma 3 excludes a \(K_\ell\)-minor with high probability, while minimum degree is
\[
(pc+o(1))\ell\sqrt{\ln\ell}.
\]
Let \(c\) tend to its permitted limit and optimize over \(p\).

This recovers, rather than improves, the obstruction in the supplied attempt. The maximizing \(p\) lies above \(1/2\), so Theorem B shows that this random obstruction is asymptotically sharp within the corresponding dense minimum-degree regime.

---

# 5. What remains unresolved

The positive-density proof constructs a cycle through random terminal groups; it does not require a suitable Hamilton cycle to be supplied in advance. This removes the interval-mixing hypothesis from the previous attempt when \(n=O(\delta(G))\).

However, its quantitative dependence on density is essential to the argument:

* the robust core has guaranteed minimum degree only of order \(c^2n\);
* the permissible number of deleted routing vertices depends on \(c\);
* the resulting \(\kappa(c)\) tends to zero as \(c\to0\).

Thus substituting \(c=\delta(G)/n\) when this ratio tends to zero does **not** yield
\[
\operatorname{ch}(G)=\Omega\!\left(\frac{\delta(G)}
{\sqrt{\ln\delta(G)}}\right)
\]
with an absolute constant.

Accordingly, this is a proof of substantial dense special cases, but it gives no unrestricted improvement over the source paper's \(O(\ell^2)\) upper bound.