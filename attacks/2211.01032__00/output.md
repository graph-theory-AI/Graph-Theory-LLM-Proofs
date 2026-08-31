```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For the unconditioned model as stated, taking p=(log n)/(3n) makes isolated K2 components alone contribute asymptotically n^(1/3)log(n)/6 faces, far more than log(pn^2).",
  "would_publish": false,
  "caveats": "This refutes the unrestricted catalog wording, not a version conditioned on connectivity or restricted to the connected regime."
}
```

## 1. Statement and convention

For a graph \(G\), let \(D(G)\) be its set of directed edges. A rotation system is a product \(\rho=\prod_v\rho_v\), where \(\rho_v\) is a cyclic permutation of the darts with tail \(v\). If
\[
\alpha(u,v)=(v,u)
\]
is edge reversal, then the faces are the cycles of the facial permutation
\[
\phi=\rho\alpha.
\]

For disconnected graphs, the standard permutation definition is componentwise: the dart set of every edge-containing component is invariant under \(\phi\), and the total number of faces is the sum of the numbers of facial cycles on those components.

Under this interpretation, the conjecture as supplied—without a connectivity condition or a lower bound on \(p\)—is false, even when
\[
\log(pn^2)\longrightarrow\infty
\quad\text{and}\quad
np\longrightarrow\infty.
\]

## 2. Isolated-edge obstruction

Let \(X_2(G)\) denote the number of components of \(G\) isomorphic to \(K_2\).

An isolated \(K_2\) has two darts. Both local rotations are identities, so its facial permutation is the transposition of the two darts and hence has exactly one cycle. Consequently, for every rotation system,
\[
F(G,\rho)\ge X_2(G).
\]
Averaging over both \(G\) and the rotations gives
\[
\mathbb E F(G(n,p))\ge \mathbb E X_2(G(n,p)).
\]

For a fixed unordered pair \(\{u,v\}\), it is an isolated \(K_2\) precisely when \(uv\) is present and all \(2(n-2)\) other edges incident with \(u\) or \(v\) are absent. Hence
\[
\mathbb E X_2
 =\binom n2 p(1-p)^{2n-4}.
\tag{1}
\]

Now take
\[
p=\frac{\log n}{3n}.
\]
Since \(np^2=o(1)\),
\[
(1-p)^{2n-4}
 =\exp\!\left(-(2n-4)p+O(np^2)\right)
 =(1+o(1))n^{-2/3}.
\]
Substitution into (1) yields
\[
\mathbb E X_2
 =(1+o(1))
 \frac{n^2}{2}\frac{\log n}{3n}n^{-2/3}
 =(1+o(1))\frac{n^{1/3}\log n}{6}.
\]
Therefore
\[
\mathbb E F(G(n,p))
 \ge (1+o(1))\frac{n^{1/3}\log n}{6}.
\tag{2}
\]

On the other hand,
\[
\log(pn^2)
 =\log\!\left(\frac{n\log n}{3}\right)
 =\log n+\log\log n-\log 3
 =(1+o(1))\log n.
\]
Thus (2) gives
\[
\frac{\mathbb E F(G(n,p))}{\log(pn^2)}
 \longrightarrow\infty,
\]
rather than \(1\). This disproves the unrestricted statement.

More generally, writing \(p=d/n\), whenever \(d=o(\sqrt n)\),
\[
\mathbb E F(G(n,p))
 \ge (1+o(1))\frac{nd}{2}e^{-2d}.
\tag{3}
\]
For example, if \(d=(\tfrac12-\varepsilon)\log n\), the lower bound in (3) is of order
\[
n^{2\varepsilon}\log n,
\]
again much larger than \(\log(pn^2)\).

## 3. A separate dense-case partial result

The counterexample above does not address a version restricted to connected graphs or, for example, to
\[
p\ge \frac{\log n+\omega(1)}n.
\]
For that intended version, one can nevertheless improve the quoted lower bound for the endpoint case \(p=1\).

### Proposition
For a random rotation system of \(K_n\),
\[
\mathbb E F(K_n)\ge \log n-O(1).
\tag{4}
\]

This remains a factor \(2\) below the conjectured value
\[
\log(n^2)=2\log n.
\]

### Proof

Write the darts of \(K_n\) as ordered pairs \((u,v)\), \(u\ne v\). Let \(C_k\) be the number of facial cycles of length \(k\).

Consider a cyclic word
\[
w=(v_0,v_1,\ldots,v_{k-1}),
\]
with indices modulo \(k\), and set
\[
e_i=(v_i,v_{i+1}).
\]
Call the word good if:

1. \(v_i\ne v_{i+1}\) for every \(i\);
2. the darts \(e_i\) are pairwise distinct;
3. no two of the \(e_i\) are reversals of one another.

If the \(v_i\) are chosen independently and uniformly from \([n]\), then, for \(k\ge5\),

- a loop occurs with probability at most \(k/n\);
- two darts coincide with probability at most \(\binom{k}{2}/n^2\);
- reversed darts occur with probability at most
  \[
  \frac{k}{n}+\frac{\binom{k}{2}}{n^2};
  \]
  the \(k/n\) term accounts for consecutive immediate reversals.

Thus the number \(\lvert\mathcal W_k\rvert\) of good words satisfies
\[
\lvert\mathcal W_k\rvert
 \ge n^k\left(1-\frac{2k}{n}-\frac{k^2}{n^2}\right).
\tag{5}
\]

For a fixed good word, the condition that it be a facial cycle is
\[
\rho_{v_{i+1}}(v_i)=v_{i+2}
\qquad(0\le i<k).
\tag{6}
\]
At a vertex \(x\), suppose (6) imposes \(t_x\) prescribed directed adjacencies in the cyclic order on the \(n-1\) neighbors of \(x\). Goodness ensures that these \(t_x\) prescribed adjacencies have pairwise disjoint endpoints: a common endpoint would give either a repeated dart or both orientations of an edge.

There are \((n-2)!\) cyclic permutations of the \(n-1\) neighbors of \(x\). Contracting the \(t_x\) prescribed directed adjacencies shows that exactly
\[
(n-t_x-2)!
\]
of them satisfy all the constraints. Therefore
\[
\Pr(\text{constraints at }x)
 =\frac{(n-t_x-2)!}{(n-2)!}
 \ge (n-1)^{-t_x}.
\]
The rotations at distinct vertices are independent and \(\sum_x t_x=k\), so
\[
\Pr(w\text{ is facial})\ge (n-1)^{-k}.
\tag{7}
\]

Each facial \(k\)-cycle gives exactly \(k\) cyclic words, one for every choice of starting dart. From (5) and (7),
\[
\mathbb E C_k
 \ge \frac{\lvert\mathcal W_k\rvert}{k(n-1)^k}
 \ge \frac1k\left(1-\frac{2k}{n}-\frac{k^2}{n^2}\right),
\tag{8}
\]
where we used \((n/(n-1))^k\ge1\).

Summing (8) for \(5\le k\le n/10\) gives
\[
\begin{aligned}
\mathbb E F(K_n)
&\ge
 \sum_{k=5}^{\lfloor n/10\rfloor}
 \left(\frac1k-\frac2n-\frac{k}{n^2}\right)\\
&=\log n-O(1),
\end{aligned}
\]
proving (4).

## 4. Scope and remaining gap

- The isolated-\(K_2\) calculation is a complete counterexample to the unconditioned statement supplied in the prompt.
- If the source intended \(G(n,p)\) conditioned on being connected, or assumed \(p\) above the connectivity threshold, that hypothesis is essential and the counterexample does not apply.
- Under such a corrected interpretation, the conjectured coefficient remains open. The additional \(K_n\) argument gives only
  \[
  \mathbb E F(K_n)\ge \log n-O(1),
  \]
  versus the desired \(2\log n+o(\log n)\), and supplies no matching upper bound.