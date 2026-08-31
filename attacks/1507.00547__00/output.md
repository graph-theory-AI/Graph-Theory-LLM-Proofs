```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The problem remains open for every k≥3; I give an exact oriented-hypergraph reformulation, prove the root lower and logarithmic-factor upper bounds, and show that independent random one-valued maps necessarily have the logarithmic scale.",
  "would_publish": false,
  "caveats": "The factor (log m)^{1/k} is not removed, and no novelty over possible folklore is claimed."
}
```

## 1. Statement and notation

Under the standard definition used in the source, let \(V\) be an \(n\)-element set and let
\[
F:\binom Vk\longrightarrow \binom Vl
\]
satisfy \(F(S)\cap S=\varnothing\) for every \(S\in\binom Vk\). A set \(A\subseteq V\) is **free** if
\[
F(S)\cap A=\varnothing
\qquad\text{for every }S\in\binom Ak.
\]
Write
\[
\alpha(F)=\max\{|A|:A\text{ is free for }F\}
\]
and
\[
p(n,k,l)=\min_F\alpha(F).
\]

The question is whether, for every fixed \(k\),
\[
p(n,k,1)=\Theta_k(n^{1/k}).
\]

The supplied theorem gives
\[
p(n,k,(k-1)!)=\Theta_k(n^{1/k}).
\]
For \(k=2\), \((k-1)!=1\), so the question is already resolved. The unresolved cases are \(k\ge3\).

The conclusions proved below are
\[
c_k n^{1/k}\le p(n,k,1)
 \le \bigl(((k-1)(k-1)!+o(1))n\log n\bigr)^{1/k}.
\]
The upper bound is attained by an independent random map only up to constants: such a random map has largest free set
\[
\Theta_k((n\log n)^{1/k})
\]
with high probability. Thus a proof of the conjectured upper bound must use a substantially structured map.

---

## 2. Exact reformulation as an oriented hypergraph problem

Given a one-valued map \(f:\binom Vk\to V\), with \(f(S)\notin S\), define the \((k+1)\)-uniform hypergraph
\[
\mathcal H_f=\{S\cup\{f(S)\}:S\in\binom Vk\},
\]
where repeated edges are retained only once.

A set \(A\subseteq V\) is free for \(f\) if and only if it is independent in \(\mathcal H_f\). Hence
\[
\alpha(f)=\alpha(\mathcal H_f).
\]

Call a \((k+1)\)-uniform hypergraph \(\mathcal H\) **1-orientable toward its \(k\)-faces** if one can assign to each \(E\in\mathcal H\) a \(k\)-set
\[
\tau(E)\in\binom Ek
\]
such that all the sets \(\tau(E)\) are distinct.

### Proposition 2.1
For \(n\ge k+1\),
\[
p(n,k,1)=
\min\{\alpha(\mathcal H):
       \mathcal H\subseteq\binom V{k+1}
       \text{ is 1-orientable toward its \(k\)-faces}\}.
\]

### Proof

For a map \(f\), orient each distinct edge \(E\in\mathcal H_f\) toward one \(k\)-set \(S\) for which
\[
E=S\cup\{f(S)\}.
\]
Two distinct edges cannot be oriented toward the same \(S\), because \(S\) has only the single image \(f(S)\). Thus \(\mathcal H_f\) is 1-orientable.

Conversely, suppose \(\mathcal H\) is 1-orientable via \(\tau\). For every \(E\in\mathcal H\), define
\[
f(\tau(E))=E\setminus\tau(E).
\]
This is well-defined because the \(\tau(E)\) are distinct. Define \(f\) arbitrarily on all unassigned \(k\)-sets. Then
\[
\mathcal H\subseteq\mathcal H_f,
\]
so
\[
\alpha(f)=\alpha(\mathcal H_f)\le\alpha(\mathcal H).
\]
Taking minima in both directions proves the equality. ∎

If
\[
\partial_k\mathcal A
=\{S\in\binom Vk:S\subset E\text{ for some }E\in\mathcal A\}
\]
denotes the \(k\)-shadow of a subfamily \(\mathcal A\subseteq\mathcal H\), Hall's theorem gives the following exact criterion:
\[
\mathcal H\text{ is 1-orientable}
\quad\Longleftrightarrow\quad
|\mathcal A|\le |\partial_k\mathcal A|
\quad\text{for every }\mathcal A\subseteq\mathcal H.
\]

More generally, an \(l\)-valued set map corresponds to assigning each edge to a contained \(k\)-face with load at most \(l\). The Hall condition becomes
\[
|\mathcal A|\le l\,|\partial_k\mathcal A|
\quad\text{for every }\mathcal A\subseteq\mathcal H.
\]
Thus the source theorem supplies, in this language, a \((k-1)!\)-orientable \((k+1)\)-graph with independence number \(O(n^{1/k})\). The open problem asks whether capacity \(1\) suffices.

This formulation also explains why simply selecting one element from each \((k-1)!\)-element image is not automatic: bounded-load orientability does not ensure that one can retain a capacity-one subhypergraph with comparable independence number.

---

## 3. Universal lower bound

The lower bound follows by random sampling and deletion.

### Proposition 3.1
For fixed \(k,l\) and sufficiently large \(n\),
\[
p(n,k,l)\ge
\frac{k}{k+1}
\left(\frac{k!}{l(k+1)}\right)^{1/k}n^{1/k}.
\]
In particular,
\[
p(n,k,1)=\Omega_k(n^{1/k}).
\]

### Proof

For a given \(l\)-valued map, form the \((k+1)\)-graph
\[
\mathcal H=\{S\cup\{v\}:S\in\binom Vk,\ v\in F(S)\}.
\]
It has at most
\[
e(\mathcal H)\le l\binom nk\le \frac{l n^k}{k!}
\]
distinct edges.

Choose every vertex independently with probability
\[
\rho=\left(\frac{k!}{l(k+1)n^{k-1}}\right)^{1/k}.
\]
Let \(R\) be the resulting random set. Delete one vertex from each edge of \(\mathcal H[R]\). The remaining set is independent, hence free, and has size at least
\[
|R|-e(\mathcal H[R]).
\]
Therefore its expected size is at least
\[
n\rho-e(\mathcal H)\rho^{k+1}
 \ge n\rho-\frac{l n^k}{k!}\rho^{k+1}.
\]
By the definition of \(\rho\),
\[
\frac{l n^k}{k!}\rho^{k+1}
=\frac{n\rho}{k+1}.
\]
Consequently some free set has size at least
\[
\frac{k}{k+1}n\rho
=
\frac{k}{k+1}
\left(\frac{k!}{l(k+1)}\right)^{1/k}n^{1/k}.
\]
∎

This proves the conjectured order of magnitude from below, but not the required upper construction.

---

## 4. A logarithmic-factor upper bound for \(l=1\)

Choose the values \(f(S)\), independently for all \(S\in\binom Vk\), uniformly from \(V\setminus S\).

For a fixed \(r\)-set \(A\), the probability that it is free equals
\[
\left(\frac{n-r}{n-k}\right)^{\binom rk}.
\]
Indeed, for each \(S\in\binom Ak\), exactly \(n-r\) of the \(n-k\) possible images lie outside \(A\).

Let \(Z_r\) be the number of free \(r\)-sets. Then
\[
\mathbb E Z_r
=
\binom nr
\left(\frac{n-r}{n-k}\right)^{\binom rk}.
\]

Take
\[
r=C(n\log n)^{1/k},
\]
where \(k\ge2\) is fixed. Since \(r=o(n)\),
\[
\log\binom nr
=
r\log\frac nr+O(r)
\]
and
\[
\binom rk\log\frac{n-r}{n-k}
=
-(1+o(1))\frac{r^{k+1}}{k!n}.
\]
Also
\[
\log\frac nr
=
\frac{k-1}{k}\log n-\frac1k\log\log n+O_k(1).
\]
Hence
\[
\log\mathbb E Z_r
=
\left(
\frac{k-1}{k}
-\frac{C^k}{k!}
+o(1)
\right)r\log n.
\]

Thus \(\mathbb E Z_r\to0\) whenever
\[
C^k>\frac{k-1}{k}k!
=(k-1)(k-1)!.
\]
It follows that, for every fixed \(\varepsilon>0\),
\[
p(n,k,1)
\le
\left(\bigl((k-1)(k-1)!+\varepsilon\bigr)n\log n\right)^{1/k}
\]
for all sufficiently large \(n\). Equivalently,
\[
p(n,k,1)
\le
\bigl(((k-1)(k-1)!+o(1))n\log n\bigr)^{1/k}.
\]

This leaves exactly a factor \((\log n)^{1/k}\) above the desired bound.

---

## 5. Independent random maps really have the logarithmic scale

The preceding first-moment argument might conceivably be very wasteful. It is not, at least at the level of order of magnitude.

### Proposition 5.1
Fix \(k\ge2\). Let \(f(S)\) be chosen independently and uniformly from \(V\setminus S\). Then, with probability tending to \(1\),
\[
\alpha(f)=\Theta_k((n\log n)^{1/k}).
\]

The upper bound follows from the first moment above. It remains to prove the lower bound.

### Proof of the random lower bound

Let
\[
r=c(n\log n)^{1/k}
\]
for a sufficiently small positive constant \(c=c(k)\), and let \(Z\) count the free \(r\)-sets.

For an \(r\)-set \(A\), write \(\mathcal E_A\) for the event that \(A\) is free and set
\[
q=\frac{n-r}{n-k},
\qquad
N=\binom rk.
\]
Then
\[
\Pr(\mathcal E_A)=q^N.
\]

Fix two \(r\)-sets \(A,B\) with \(|A\cap B|=t\). Exactly \(\binom tk\) domain \(k\)-sets occur in both \(A\) and \(B\). For such a shared \(k\)-set, the image must avoid \(A\cup B\), giving probability
\[
\frac{n-2r+t}{n-k}.
\]
Consequently
\[
\frac{\Pr(\mathcal E_A\cap\mathcal E_B)}
     {\Pr(\mathcal E_A)\Pr(\mathcal E_B)}
=
R_t,
\]
where
\[
R_t=
\left(
\frac{(n-2r+t)(n-k)}{(n-r)^2}
\right)^{\binom tk}.
\]
For \(t<k\), this is exactly \(1\).

For \(n\) large enough that \(r\le n/4\), one has
\[
R_t\le
\exp\left(\frac{3t}{n}\binom tk\right)
\le
\exp\left(\frac{3t^{k+1}}{k!n}\right).
\tag{5.1}
\]

Let \(P_t\) denote the probability that two independent uniformly chosen \(r\)-sets intersect in exactly \(t\) elements. Put
\[
\mu=\frac{r^2}{n}.
\]
A union bound over the \(t\)-subsets of the first \(r\)-set gives
\[
P_t
\le
\Pr(|A\cap B|\ge t)
\le
\binom rt\left(\frac rn\right)^t
\le
\left(\frac{e\mu}{t}\right)^t.
\tag{5.2}
\]

By symmetry,
\[
\frac{\mathbb E Z^2}{(\mathbb E Z)^2}
=
\sum_{t=0}^r P_tR_t.
\tag{5.3}
\]

#### Case \(k\ge3\)

Here
\[
\mu=c^2n^{2/k-1}(\log n)^{2/k}=o(1).
\]
Choose, for example,
\[
c^k=\frac{k!(k-2)}{24k}.
\]
For every \(t\ge k\),
\[
\log\frac{t}{e\mu}
\ge
\frac{k-2}{2k}\log n
\]
for all sufficiently large \(n\). Also,
\[
\frac{3t^k}{k!n}
\le
\frac{3r^k}{k!n}
=
\frac{k-2}{8k}\log n+o(\log n).
\]
Combining (5.1) and (5.2),
\[
P_tR_t
\le
\exp\left(
-t\left[
\log\frac{t}{e\mu}
-\frac{3t^k}{k!n}
\right]\right)
\le
n^{-(k-2)t/(4k)}
\]
for all sufficiently large \(n\). Therefore
\[
\sum_{t=k}^rP_tR_t=o(1).
\]
Since \(R_t=1\) for \(t<k\), equation (5.3) gives
\[
\frac{\mathbb E Z^2}{(\mathbb E Z)^2}=1+o(1).
\]

#### Case \(k=2\)

Take \(c=1/4\), so
\[
r=\frac14\sqrt{n\log n},
\qquad
\mu=\frac1{16}\log n.
\]
Let \(T=n^{1/4}\). For \(t\le T\), (5.1) gives
\[
R_t\le \exp\left(\frac{3T^3}{2n}\right)=1+o(1)
\]
uniformly.

For \(t>T\),
\[
\log\frac{t}{e\mu}\ge\frac15\log n
\]
for large \(n\), while
\[
\frac{3t^2}{2n}
\le
\frac{3r^2}{2n}
=
\frac{3}{32}\log n.
\]
Thus, using (5.1) and (5.2),
\[
\sum_{t>T}P_tR_t=o(1).
\]
Again (5.3) yields
\[
\frac{\mathbb E Z^2}{(\mathbb E Z)^2}=1+o(1).
\]

In both cases, the Paley–Zygmund inequality gives
\[
\Pr(Z>0)
\ge
\frac{(\mathbb E Z)^2}{\mathbb E Z^2}
=1-o(1).
\]
Thus a random map has a free set of size \(c_k(n\log n)^{1/k}\) with high probability. Together with the first-moment upper bound, this proves the proposition. ∎

Therefore independent random choices cannot establish the conjectured \(O(n^{1/k})\) upper bound. Strong dependencies or an algebraic/design construction would be required.

---

## 6. Exact finite feasibility formulation

For computational investigation, fix integers \(n,k,r\). Introduce binary variables
\[
x_{S,v}\in\{0,1\},
\qquad
S\in\binom{[n]}k,\quad v\in[n]\setminus S,
\]
where \(x_{S,v}=1\) means \(f(S)=v\).

The condition that \(f\) is a one-valued map is
\[
\sum_{v\notin S}x_{S,v}=1
\qquad
\text{for every }S\in\binom{[n]}k.
\tag{6.1}
\]

The condition that every \(r\)-set \(R\) is nonfree is
\[
\sum_{S\in\binom Rk}
\ \sum_{v\in R\setminus S}x_{S,v}
\ge1
\qquad
\text{for every }R\in\binom{[n]}r.
\tag{6.2}
\]

Thus (6.1)–(6.2) form an exact \(0\)-\(1\) feasibility formulation:

- it is feasible if and only if there exists a map with \(\alpha(f)<r\);
- equivalently, it is feasible if and only if \(p(n,k,1)<r\).

The naive linear relaxation is weak at the conjectured scale. Indeed, setting
\[
x_{S,v}=\frac1{n-k}
\]
satisfies (6.1), and the left side of (6.2) becomes
\[
\binom rk\frac{r-k}{n-k}.
\]
For \(r=Cn^{1/k}\), this is asymptotic to
\[
\frac{C^{k+1}}{k!}n^{1/k},
\]
which tends to infinity. Hence any useful computational or optimization approach must exploit integrality rather than only the basic fractional covering constraints. No computational run is claimed here.

---

## 7. Small values of \(k\)

- If \(k=1\) is admitted, then for \(n\ge2\),
  \[
  p(n,1,1)=\left\lceil\frac n3\right\rceil.
  \]
  Indeed, the underlying graph of a loopless functional digraph is a pseudoforest, hence 3-colorable, giving an independent set of size at least \(\lceil n/3\rceil\). Disjoint directed triangles, with one directed \(4\)-cycle or \(2\)-cycle for the remainder, attain this bound.

- For \(k=2\), the theorem quoted in the problem already has
  \[
  (k-1)!=1,
  \]
  and therefore
  \[
  p(n,2,1)=\Theta(\sqrt n).
  \]

- For every \(k\ge3\), the argument above leaves
  \[
  \Omega_k(n^{1/k})
  \le p(n,k,1)
  \le O_k((n\log n)^{1/k}).
  \]

## 8. Remaining gap

A complete proof would require constructing a 1-orientable \((k+1)\)-uniform hypergraph on \(n\) vertices with independence number \(O_k(n^{1/k})\). A disproof would require a universal lower bound growing faster than \(n^{1/k}\) for all such 1-orientable hypergraphs. Neither is obtained here.

The random-model calculation also rules out the most immediate probabilistic construction: independent uniform images produce the extra factor \((\log n)^{1/k}\) with high probability.