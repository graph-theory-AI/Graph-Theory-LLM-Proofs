```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the standard \u2113\u221e colour-count error, the exact worst case is determined for a spanning star plus k\u22121 isolates, forcing every universal leading coefficient to be at least (k\u22121)/(2k).",
  "would_publish": false,
  "caveats": "The excerpt omits the definition of f_h and the current numerical coefficient; no general upper bound for all spanning forests is improved."
}
```

## 1. Precise formulation used

The catalog statement does not define \(f_h(F)\). I use the standard \(\ell_\infty\) colour-count discrepancy.

Let \(h:E(K_N)\to[k]\) be balanced, meaning that every colour occurs on exactly \(\binom N2/k\) edges. For a spanning graph \(F\) on \(N\) vertices, define
\[
D_h(F):=
 \min_{\phi:V(F)\to V(K_N)\ {\rm bijective}}
 \max_{i\in[k]}
 \left|e_i(\phi(F))-\frac{e(F)}k\right|,
\]
where \(e_i(\phi(F))\) is the number of colour-\(i\) edges in the embedded copy \(\phi(F)\).

The result below gives an exact special case and, consequently, a lower bound on any possible leading coefficient in a general estimate \(D_h(F)\le C_k\Delta(F)+O_k(1)\).

---

## 2. Exact result for a spanning star forest

Let \(N=kn\), and suppose that
\[
\frac1k\binom{kn}{2}=\frac{n(kn-1)}2
\]
is an integer. Define
\[
F_{k,n}:=K_{1,k(n-1)}\cup (k-1)K_1.
\]
Thus \(F_{k,n}\) is a spanning forest on \(kn\) vertices with
\[
e(F_{k,n})=\Delta(F_{k,n})=k(n-1).
\]
Put
\[
q:=\frac{e(F_{k,n})}{k}=n-1
\]
and
\[
L_{k,n}:=\max\left\{n-1,\frac{(k-1)(n-2)}2\right\}.
\]

### Theorem
For every \(k\ge 3\) and every admissible \(n\ge 2k-2\),
\[
\max_{h\ {\rm balanced}}D_h(F_{k,n})=L_{k,n}.
\]
Equivalently,
\[
\max_h D_h(F_{k,n})=
\begin{cases}
n-1,&k=3,\\[2mm]
\dfrac{(k-1)(n-2)}2,&k\ge4.
\end{cases}
\]

The proof has two parts.

---

## 3. A degree-cap lemma

For a vertex \(v\), let \(d_i(v)\) denote its degree in colour \(i\).

### Lemma
Every balanced \(k\)-colouring of \(K_{kn}\) has a vertex \(v\) satisfying
\[
d_i(v)\le A:=\frac{(k+1)n}{2}-1
\qquad\text{for every }i\in[k].
\]

#### Proof
Set
\[
t:=A+1=\frac{(k+1)n}{2}.
\]
This is an integer. Indeed, this is immediate when \(k\) is odd. If \(k\) is even, balancedness requires \(n(kn-1)\) to be even; since \(kn-1\) is odd, \(n\) must be even.

Suppose for contradiction that every vertex has some colour-degree at least \(t\). Assign each vertex \(v\) one such colour \(c(v)\). Let
\[
X_i:=\{v:c(v)=i\},\qquad x_i:=|X_i|.
\]
Some \(x_i\ge n\).

Let \(M=n(kn-1)/2\) be the number of edges of each colour. For the corresponding \(i\),
\[
t x_i
 \le \sum_{v\in X_i}d_i(v)
 =2e_i(X_i)+e_i(X_i,V\setminus X_i).
\]
Since
\[
2e_i(X_i)+e_i(X_i,V\setminus X_i)
 =M+e_i(X_i)-e_i(V\setminus X_i),
\]
we have
\[
t x_i\le M+\binom{x_i}{2}. \tag{1}
\]
Also,
\[
t x_i\le \sum_{v\in V}d_i(v)=2M=n(kn-1),
\]
so
\[
x_i\le \frac{2(kn-1)}{k+1}. \tag{2}
\]

For real \(x\), define
\[
G(x):=n(kn-1)+x(x-1)-(k+1)nx.
\]
Inequality (1) is equivalent to \(G(x_i)\ge0\). On the other hand,
\[
G(n)=-2n.
\]
Moreover, by (2),
\[
x_i<\frac{2kn}{k+1}\le \frac{(k+1)n}{2},
\]
where the last inequality is \(4k\le(k+1)^2\). Hence
\[
G'(x)=2x-1-(k+1)n<0
\]
throughout the interval containing \([n,x_i]\). Therefore
\[
G(x_i)\le G(n)=-2n<0,
\]
contradicting (1). ∎

---

## 4. Universal upper bound for \(F_{k,n}\)

Choose \(v\) as in the lemma and write \(d_i=d_i(v)\). A copy of \(F_{k,n}\) centred at \(v\) is obtained by selecting \(k-1\) other vertices to serve as the isolated vertices; all remaining vertices are leaves of the star.

Let
\[
B:=\frac{(k-1)(n-2)}2,\qquad L:=\max\{q,B\},\qquad U:=q+L.
\]
We claim that one can omit \(k-1\) neighbours so that the resulting star has at most \(U\) edges of every colour.

First, at most one \(d_i\) can exceed \(U\). Indeed, since \(L\ge B\),
\[
U\ge q+B=\frac{(k+1)n-2k}{2}.
\]
If two colour-degrees exceeded \(U\), their integer sum would be at least
\[
2(U+1)\ge (k+1)n-2k+2.
\]
But
\[
(k+1)n-2k+2-(kn-1)=n-2k+3>0
\]
because \(n\ge2k-2\), contradicting \(\sum_i d_i=kn-1\).

If some \(d_i>U\), then
\[
d_i-U\le A-U\le A-(q+B)=k-1.
\]
Omit \(d_i-U\) neighbours joined to \(v\) in colour \(i\), and then omit arbitrary additional neighbours until \(k-1\) vertices have been omitted. If no \(d_i>U\), omit any \(k-1\) neighbours.

Writing \(a_i\) for the colour counts in the resulting copy, we have
\[
0\le a_i\le U=q+L.
\]
Because \(L\ge q\),
\[
|a_i-q|\le L
\]
for every \(i\). Hence
\[
D_h(F_{k,n})\le L_{k,n}. \tag{3}
\]

---

## 5. A balanced colouring attaining the bound

Partition the \(kn\) vertices into equal classes
\[
V_1,\dots,V_k,\qquad |V_i|=n.
\]

### Odd \(k\)

Choose a regular tournament \(T\) on \([k]\). Colour every edge inside \(V_i\) with colour \(i\). For \(i\ne j\), if \(i\to j\) in \(T\), colour all edges between \(V_i\) and \(V_j\) with colour \(i\).

Every colour class has
\[
\binom n2+\frac{k-1}{2}n^2
 =\frac{n(kn-1)}2
\]
edges, so the colouring is balanced.

### Even \(k\)

In this case admissibility forces \(n\) to be even. Choose a perfect matching \(P\) of the index set \([k]\). The graph \(K_k-P\) has even degree \(k-2\), so orient it with every vertex having outdegree \((k-2)/2\).

For an oriented pair \(i\to j\), colour all edges between \(V_i\) and \(V_j\) with colour \(i\). For each matched pair \(\{i,j\}\in P\), choose an \(n/2\)-regular bipartite graph between \(V_i\) and \(V_j\); colour its edges \(i\) and the complementary edges \(j\). Again colour all edges inside \(V_i\) by \(i\).

Each colour now has
\[
\binom n2+\frac{k-2}{2}n^2+\frac12n^2
 =\frac{n(kn-1)}2
\]
edges, so this colouring is also balanced.

### Vertex colour-degrees

In both constructions, every \(v\in V_i\) has
\[
d_i(v)=A=\frac{(k+1)n}{2}-1. \tag{4}
\]
Moreover, at least one other colour has degree zero at \(v\):

- for odd \(k\), every colour corresponding to an out-neighbour of \(i\) in the tournament has degree zero at \(v\);
- for even \(k\), the same holds for each oriented out-neighbour in \(K_k-P\).

Consider any embedded copy of \(F_{k,n}\), centred at \(v\). Removing the \(k-1\) isolated vertices deletes at most \(k-1\) edges of colour \(i\). Thus the star retains at least
\[
A-(k-1)=q+B
\]
edges of colour \(i\), giving discrepancy at least \(B\). The zero colour remains zero and therefore has discrepancy \(q\). Consequently,
\[
D_h(F_{k,n})\ge\max\{q,B\}=L_{k,n}. \tag{5}
\]
Combining (3) and (5) proves the theorem.

---

## 6. Consequence for the leading coefficient

Let \(C_k\) be any coefficient for which one hopes to prove
\[
D_h(F)\le C_k\Delta(F)+O_k(1)
\]
for every balanced \(k\)-colouring and every admissible spanning forest \(F\).

For the forests above,
\[
\Delta(F_{k,n})=k(n-1)
\]
and
\[
\frac{D_h(F_{k,n})}{\Delta(F_{k,n})}
\longrightarrow \frac{k-1}{2k}
\qquad(n\to\infty).
\]
Therefore necessarily
\[
\boxed{C_k\ge\frac{k-1}{2k}}.
\]

For \(k=3\), the exact value on this family is
\[
D_h(F_{3,n})=\frac{\Delta(F_{3,n})}{3}.
\]
For \(k\ge4\),
\[
D_h(F_{k,n})
 =\frac{k-1}{2k}\Delta(F_{k,n})-\frac{k-1}{2}.
\]

---

## 7. Recolouring-distance interpretation

If the source instead defines \(f_h(F)\) as the minimum number of edges that must be recoloured to obtain exactly \(q=e(F)/k\) edges of every colour, then for a colour-count vector \(a=(a_1,\dots,a_k)\) this number is
\[
\rho(a)=\sum_i(a_i-q)_+
       =\frac12\sum_i|a_i-q|.
\]

For the explicit balanced colouring above, one obtains
\[
\rho_h(F_{k,n})
 =
 \left\lfloor\frac{(k-1)(n-1)}2\right\rfloor
 =
 \left\lfloor\frac{k-1}{2k}\Delta(F_{k,n})\right\rfloor.
\]

Indeed, before omitting the \(k-1\) isolated vertices, the positive surplus over \(q=n-1\) is

\[
\frac{(k-1)(n+1)}2
\]
for odd \(k\), and
\[
\frac{(k-1)n+k-2}{2}
\]
for even \(k\). Each omitted edge reduces this surplus by at most one, while omitting \(k-1\) edges of the centre's own colour attains the corresponding decrease of \(k-1\).

Thus the same asymptotic lower coefficient
\[
\frac{k-1}{2k}
\]
also applies to the recolouring-distance normalization.

For \(k=3\), the preceding universal upper construction has all three colour counts in \([0,2q]\) and total \(3q\), which implies recolouring distance at most \(q\). Hence the star-forest special case is exact under this normalization as well:
\[
\max_h\rho_h(F_{3,n})=n-1=\frac{\Delta(F_{3,n})}{3}.
\]

---

## 8. Remaining gaps

1. This does not improve the general upper bound for arbitrary spanning forests.
2. The example has \(\Delta\) comparable to the order of the host. It does not address a separately restricted regime such as \(\Delta=o(n)\), if that is intended.
3. The exact definition and normalization of \(f_h(F)\), and the numerical coefficient currently proved in the source paper, are absent from the supplied statement. The result therefore cannot be asserted to improve that coefficient directly.
4. The exact family contains isolated vertices. If isolates are disallowed, replacing them by \(k-1\) disjoint edges and shortening the large star preserves the asymptotic lower coefficient, though not the exact formula above.

Thus the general optimization problem remains open, but the coefficient in any universal linear estimate cannot be smaller than \((k-1)/(2k)\), and the extremal value is completely determined for a natural spanning star-forest family.