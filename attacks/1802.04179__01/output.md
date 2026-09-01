```json
{
  "verdict": "already_resolved",
  "confidence": "medium",
  "one_line": "The Xu–Zhu theorem quoted in the catalog gives the strictly better universal bound χ_f(G)≤7/2=11/3−1/6, thereby confirming the informal conjecture.",
  "would_publish": false,
  "caveats": "The deduction is complete, but it relies on the stated 2025 DP-coloring theorem, whose preprint and proof I have not independently inspected here; the exact optimal constant remains open."
}
```

## Formal statement

Let \(\mathcal P_{4,5}\) be the class of finite planar graphs containing no cycles of length \(4\) or \(5\), and put
\[
\rho_{4,5}:=\sup\{\chi_f(G):G\in\mathcal P_{4,5}\}.
\]
Equivalently, \(\rho_{4,5}\) is the infimum of the real numbers \(r\) such that every graph in \(\mathcal P_{4,5}\) has fractional chromatic number at most \(r\).

Dvořák and Hu proved
\[
\rho_{4,5}\le \frac{11}{3}.
\]
The natural formalization of their informal conjecture is
\[
\rho_{4,5}<\frac{11}{3}.
\]

## Quoted subsequent theorem

The catalog attributes to Xu and Zhu, *Planar graphs without cycles of length 4 or 5 are \((7m:2m)\)-DP-colorable*, arXiv:2511.12914 (2025), the theorem:

> For every positive integer \(m\), every planar graph without a \(4\)-cycle or \(5\)-cycle is \((7m:2m)\)-DP-colorable.

Under the standard definition of multiple DP-coloring, this immediately implies ordinary \((7m:2m)\)-colorability.

## Lemma: DP-multicolorability implies ordinary multicolorability

If a graph \(G\) is \((a:b)\)-DP-colorable, then it is ordinarily \((a:b)\)-colorable.

### Proof

Consider the canonical \(a\)-fold correspondence cover. For each vertex \(v\), let
\[
L(v)=\{(v,i):i\in [a]\}.
\]
For every edge \(uv\in E(G)\), use the identity matching
\[
(v,i)(u,i),\qquad i\in[a],
\]
as the set of cross-fiber conflicts.

An \((a:b)\)-DP-coloring of this cover selects \(b\) elements from every \(L(v)\), with no selected conflicting pair across an edge. Define
\[
\varphi(v)=\{i:(v,i)\text{ is selected}\}.
\]
Then \(|\varphi(v)|=b\), and for every edge \(uv\),
\[
\varphi(u)\cap\varphi(v)=\varnothing.
\]
Thus \(\varphi\) is an ordinary \((a:b)\)-coloring. If the DP definition requires at least \(b\) selected elements per fiber, discard arbitrary excess elements. \(\square\)

## Consequence

Apply the quoted Xu–Zhu theorem with any \(m\ge1\), or just with \(m=1\). Every \(G\in\mathcal P_{4,5}\) is ordinarily \((7m:2m)\)-colorable, and hence
\[
\chi_f(G)\le \frac{7m}{2m}=\frac72.
\]
Therefore
\[
\rho_{4,5}\le\frac72.
\]
Since
\[
\frac{11}{3}-\frac72=\frac{1}{6}>0,
\]
we obtain
\[
\rho_{4,5}\le\frac72<\frac{11}{3}.
\]
This proves the precise non-optimality assertion suggested by Dvořák and Hu.

## Remaining gap

This does **not** determine \(\rho_{4,5}\); it only improves its upper bound. The prompt reports a lower bound \(3+\frac1{12}\), but also phrases that bound in terms of the strong fractional DP-chromatic parameter. Without inspecting the underlying construction, I would not conflate that parameter with ordinary fractional chromatic number. At minimum, \(K_3\in\mathcal P_{4,5}\) gives the elementary lower bound \(\rho_{4,5}\ge3\).

The only non-self-contained ingredient above is the quoted Xu–Zhu DP-coloring theorem. The logical implication from that theorem to the resolution of the cataloged conjecture is complete.