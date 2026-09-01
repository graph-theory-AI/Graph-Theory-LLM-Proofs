```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A Perron-weight multiscale decomposition combined with Molloy's list-coloring theorem gives the universal bound χ(G) ≤ (e+o(1))ρ(G)ln ln ρ(G)/ln ρ(G), and proves the conjecture for asymptotically regular graphs.",
  "would_publish": false,
  "caveats": "An extra factor e ln ln ρ remains; novelty of this partial bound has not been literature-checked."
}
```

# Mathematical writeup

Throughout, logarithms are natural, and \(r=\rho(G)\). The asymptotics are uniform as \(r\to\infty\).

## 1. Result obtained

I do not prove Conjecture 1.7. I obtain the following universal improvement over Wilf’s bound \(\chi(G)\le r+1\).

### Theorem 1
Every triangle-free graph \(G\) satisfies
\[
\boxed{\quad
\chi(G)\le (e+o(1))\frac{\rho(G)\ln\ln \rho(G)}{\ln \rho(G)}.
\quad}
\]

I also record the immediate special case in which the conjectured leading constant follows.

### Proposition 2
For every family of triangle-free graphs satisfying
\[
\Delta(G)=(1+o(1))\rho(G)
\]
as \(\rho(G)\to\infty\), one has
\[
\chi(G)\le (1+o(1))\frac{\rho(G)}{\ln \rho(G)}.
\]
In particular, the conjecture holds for regular graphs and, more generally, asymptotically regular graphs in the displayed spectral sense.

Theorem 1 follows from a more precise multiscale reduction.

---

## 2. Maximum-degree input

Let \(L_\triangle(D)\) denote the least integer \(L\) such that every triangle-free graph of maximum degree at most \(D\) is \(L\)-choosable.

The list-coloring form of Molloy’s triangle-free maximum-degree theorem gives
\[
L_\triangle(D)\le (1+o(1))\frac{D}{\ln D}.
\tag{2.1}
\]

The formulation uniform over graphs of maximum degree *at most* \(D\) follows from the usual formulation in terms of the actual maximum degree: graphs whose actual maximum degree is at least \(\sqrt D\) are covered uniformly by Molloy’s theorem, while those of smaller maximum degree are \((\sqrt D+1)\)-choosable greedily, which is \(o(D/\ln D)\).

---

## 3. Perron-weight multiscale lemma

### Lemma 3
Let \(G\) be triangle-free with \(\rho(G)\le r\). For every real \(b>1\) and positive integer \(k\),
\[
\chi(G)
\le
k\left(
L_\triangle(\lceil br\rceil)
+
\left\lceil\frac{r}{b^{k-1}}\right\rceil
\right).
\tag{3.1}
\]

### Proof

It suffices to treat each nontrivial connected component separately, using the same collection of colors for all components. Let \(C\) be such a component, let
\[
s=\rho(C)\le r,
\]
and let \(x:V(C)\to\mathbb R_{>0}\) be a positive Perron eigenvector:
\[
\sum_{u\sim v}x_u=sx_v
\qquad\text{for every }v\in V(C).
\tag{3.2}
\]

Partition the vertices into Perron-weight levels
\[
V_i=\{v:b^i\le x_v<b^{i+1}\},
\qquad i\in\mathbb Z.
\]
Only finitely many levels are nonempty.

### Degree inside one level

For \(v\in V_i\), every neighbor \(u\in V_i\) satisfies \(x_u\ge b^i\). Hence
\[
d_{V_i}(v)b^i
\le
\sum_{\substack{u\sim v\\u\in V_i}}x_u
\le sx_v
<sb^{i+1}.
\]
Consequently
\[
\Delta(C[V_i])<bs\le br.
\tag{3.3}
\]

### Neighbors in much higher levels

Give level \(V_i\) residue \(i\bmod k\). If \(u\in V_j\) has the same residue as \(v\in V_i\), and \(j>i\), then \(j\ge i+k\). Therefore
\[
x_u\ge b^{i+k}>b^{k-1}x_v.
\]
Using (3.2), the number of such higher-level neighbors of \(v\) is strictly less than
\[
\frac{s}{b^{k-1}}\le \frac{r}{b^{k-1}}.
\tag{3.4}
\]

Now take \(k\) pairwise disjoint color palettes
\[
P_0,\ldots,P_{k-1},
\]
each of size
\[
Q=
L_\triangle(\lceil br\rceil)
+
\left\lceil\frac{r}{b^{k-1}}\right\rceil.
\]

For each residue separately, process its nonempty levels in decreasing order. When coloring \(V_i\), assign to \(v\in V_i\) the list obtained from \(P_{i\bmod k}\) by deleting all colors already used on its neighbors in higher levels of the same residue. By (3.4), at most
\[
\left\lceil\frac{r}{b^{k-1}}\right\rceil
\]
colors are deleted, so every resulting list has size at least
\[
L_\triangle(\lceil br\rceil).
\]
By (3.3) and the definition of \(L_\triangle\), the triangle-free graph \(C[V_i]\) can be properly colored from these lists.

Edges joining different residues have endpoints in disjoint palettes. Edges within one level are handled by the list coloring of that level. For an edge joining two levels of the same residue, the lower endpoint avoided the color already assigned to the higher endpoint. Thus the resulting coloring is proper and uses at most \(kQ\) colors. This proves (3.1). ∎

---

## 4. Optimization

Fix \(b>1\) and choose
\[
k
=
1+\left\lceil
\log_b\bigl(\ln r\,\ln\ln r\bigr)
\right\rceil.
\tag{4.1}
\]
Then
\[
b^{k-1}\ge \ln r\,\ln\ln r,
\]
and hence
\[
\frac{r}{b^{k-1}}
\le
\frac{r}{\ln r\,\ln\ln r}
=
o\left(\frac r{\ln r}\right).
\tag{4.2}
\]

For fixed \(b\), (2.1) gives
\[
L_\triangle(\lceil br\rceil)
\le
(b+o(1))\frac r{\ln r}.
\tag{4.3}
\]
Moreover,
\[
k=
\left(\frac1{\ln b}+o(1)\right)\ln\ln r.
\tag{4.4}
\]
Substituting (4.2)–(4.4) into Lemma 3 yields
\[
\chi(G)
\le
\left(\frac{b}{\ln b}+o(1)\right)
\frac{r\ln\ln r}{\ln r}.
\tag{4.5}
\]

The function \(b/\ln b\) is minimized for \(b=e\), with minimum \(e\). Therefore
\[
\chi(G)
\le
(e+o(1))
\frac{r\ln\ln r}{\ln r},
\]
proving Theorem 1.

This is \(o(r)\), and hence is a genuine logarithmic improvement over the general spectral estimate \(\chi(G)\le r+1\).

---

## 5. Asymptotically regular case

If
\[
\Delta(G)=(1+o(1))r,
\]
then Molloy’s maximum-degree theorem directly gives
\[
\chi(G)
\le
(1+o(1))\frac{\Delta(G)}{\ln\Delta(G)}
=
(1+o(1))\frac r{\ln r}.
\]
This proves Proposition 2.

More generally, if \(\Delta(G)\le C\rho(G)\) for a fixed \(C\), the same argument gives
\[
\chi(G)\le (C+o(1))\frac{\rho(G)}{\ln\rho(G)}.
\]

---

## 6. Remaining gap

The universal result is weaker than Conjecture 1.7 by a factor asymptotic to \(e\ln\ln r\).

In the proof, Perron levels of the same color palette must be separated by a multiplicative factor much larger than \(\ln r\); otherwise a vertex can have too many already-colored higher-level neighbors, and too many colors may be deleted from its list. With fixed level ratio \(b\), achieving this separation requires approximately
\[
\frac{\ln\ln r}{\ln b}
\]
disjoint palettes. This is exactly where the \(\ln\ln r\) loss occurs. Optimizing the level ratio only gives the constant \(e\); it cannot remove that loss within this disjoint-palette scheme.

Thus a proof of the conjecture appears to require a genuinely coordinated coloring across many Perron-weight scales, rather than coloring residue classes with disjoint palettes.