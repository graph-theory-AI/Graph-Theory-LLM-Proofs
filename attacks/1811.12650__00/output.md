```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For every connected noncomplete n-vertex graph, the frozen proportion among its (Δ+1)-colourings is at most 4/(n+4), so Δ=o(n) is unnecessary in the intended asymptotic conclusion.",
  "would_publish": false,
  "caveats": "The complete graphs K_n defeat a literal all-graphs formulation; connectedness is essential, and the argument gives no quantitative mixing-time bound."
}
```

## 1. Precise statement

Let \(G\) be a finite simple graph of order \(n\) and maximum degree \(\Delta\), and put
\[
q=\Delta+1.
\]
Write \(\Omega_q(G)\) for the set of proper \(q\)-colourings and \(\mathcal F_q(G)\) for its frozen colourings, i.e. the isolated vertices of the single-vertex recolouring graph.

The natural precise version of the informal remark is:

> For every sequence of connected, noncomplete graphs \(G\) with \(n\to\infty\), a uniformly random \((\Delta+1)\)-colouring is nonfrozen with probability \(1-o(1)\), without any assumption on \(\Delta/n\).

The following uniform estimate proves this.

### Theorem

If \(G\) is connected and \(G\neq K_{\Delta+1}\), then
\[
\frac{|\mathcal F_q(G)|}{|\Omega_q(G)|}\le \frac{4}{n+4}.
\]
In particular, the frozen proportion tends to zero uniformly over all possible maximum degrees.

A slightly stronger structural estimate will emerge from the proof.

---

## 2. Consequences of being frozen

Fix a frozen colouring \(\sigma\in\mathcal F_q(G)\). For every vertex \(v\), all \(q-1=\Delta\) colours other than \(\sigma(v)\) must occur in \(N(v)\). Since \(d(v)\le\Delta\), it follows that

1. \(d(v)=\Delta\) for every \(v\), so \(G\) is \(\Delta\)-regular;
2. every colour occurs exactly once in the closed neighbourhood \(N[v]\).

In particular,
\[
\{\!\{\sigma(x):x\in N[v]\}\!\}=[q]
\]
as a multiset.

Call an edge \(xy\) a **true-twin edge** if
\[
N[x]=N[y].
\]
Let
\[
E^\circ=\{xy\in E(G):N[x]\neq N[y]\}
\]
be the set of non-true-twin edges.

---

## 3. Switching one bichromatic edge

For \(\sigma\in\mathcal F_q(G)\) and \(xy\in E(G)\), let \(\sigma^{xy}\) be obtained by exchanging the colours of \(x\) and \(y\).

### Lemma 1

The colouring \(\sigma^{xy}\) is proper. Moreover, it is frozen if and only if \(N[x]=N[y]\).

#### Proof

Put \(a=\sigma(x)\) and \(b=\sigma(y)\). Because \(\sigma\) is frozen, \(y\) is the unique neighbour of \(x\) coloured \(b\), and \(x\) is the unique neighbour of \(y\) coloured \(a\). Thus exchanging \(a\) and \(b\) on \(x,y\) creates no monochromatic edge.

The closed neighbourhoods of \(x\) and \(y\) still contain all \(q\) colours: both contain \(x\) and \(y\), so the switch merely permutes two entries. The same is true for a vertex adjacent to both \(x,y\), or to neither.

If \(z\notin\{x,y\}\) is adjacent to \(x\) but not \(y\), then in \(N[z]\) the switch replaces the unique occurrence of \(a\) by an additional occurrence of \(b\). Thus \(z\) now misses \(a\) and sees \(b\) twice, so it is not frozen. The analogous statement holds if \(z\) is adjacent to \(y\) but not \(x\).

Consequently \(\sigma^{xy}\) is frozen precisely when every vertex outside \(\{x,y\}\) is adjacent to either both endpoints or neither, which for adjacent \(x,y\) is equivalent to \(N[x]=N[y]\). ∎

Thus every pair
\[
(\sigma,e)\in\mathcal F_q(G)\times E^\circ
\]
produces a nonfrozen proper colouring.

---

## 4. The switching map has multiplicity at most two

Define
\[
\Phi:\mathcal F_q(G)\times E^\circ\longrightarrow
\Omega_q(G)\setminus\mathcal F_q(G),
\qquad
\Phi(\sigma,xy)=\sigma^{xy}.
\]

### Lemma 2

Every colouring in the codomain has at most two preimages under \(\Phi\).

#### Proof

Fix a nonfrozen colouring \(\tau\) having at least one preimage. Choose, according to a fixed ordering of \(V(G)\), a vertex \(z\) which is not frozen in \(\tau\).

Suppose
\[
\tau=\sigma^{xy}
\]
for some frozen \(\sigma\) and \(xy\in E^\circ\). By Lemma 1, \(z\) is not one of \(x,y\), and it is adjacent to exactly one endpoint. Rename the endpoints so that \(z\) is adjacent to \(x\) and not to \(y\).

In the closed neighbourhood \(N[z]\), the colouring \(\tau\) has exactly one missing colour \(a\) and exactly one repeated colour \(b\). Necessarily,
\[
\tau(x)=b,\qquad \tau(y)=a.
\]
There are exactly two vertices of \(N[z]\) coloured \(b\), so there are at most two possibilities for \(x\).

Once \(x\) is fixed, \(y\) is uniquely determined. Indeed, the switch preserves the colour multiset on \(N[x]\), because \(x,y\in N[x]\). Hence \(N[x]\) contains every colour exactly once under \(\tau\), and \(y\) is its unique vertex coloured \(a\).

Thus each of the two possible choices of \(x\) determines at most one edge \(xy\) and hence at most one frozen predecessor \(\sigma=\tau^{xy}\). Therefore
\[
|\Phi^{-1}(\tau)|\le 2.
\]
∎

Double-counting gives the stronger estimate
\[
|\mathcal F_q(G)|\,|E^\circ|
   \le 2\bigl(|\Omega_q(G)|-|\mathcal F_q(G)|\bigr).
\tag{1}
\]

---

## 5. There are at least \(n/2\) non-true-twin edges

Assume \(\mathcal F_q(G)\neq\varnothing\); otherwise the theorem is immediate.

Suppose some vertex \(v\) is incident only with true-twin edges. Then for every \(u\in N(v)\),
\[
N[u]=N[v].
\]
It follows that \(N[v]\) is a clique: for any distinct \(u,w\in N[v]\), one has \(w\in N[u]\). Moreover, no vertex of \(N[v]\) has a neighbour outside \(N[v]\). Thus \(N[v]\) is a component isomorphic to \(K_q\).

Since \(G\) is connected, this would imply \(G=K_q\), contrary to the hypothesis. Hence every vertex is incident with at least one edge of \(E^\circ\). Therefore
\[
2|E^\circ|\ge n.
\tag{2}
\]

Combining (1) and (2), and writing \(F=|\mathcal F_q(G)|\), \(C=|\Omega_q(G)|\), gives
\[
C-F\ge \frac{|E^\circ|}{2}F\ge \frac n4F.
\]
Consequently
\[
\frac FC\le \frac{1}{1+n/4}=\frac{4}{n+4},
\]
as claimed. ∎

---

## 6. Consequence for Glauber dynamics

The recolouring-connectivity theorem quoted in the source says, in the connected noncomplete setting, that all nonfrozen \(q\)-colourings lie in one component of the recolouring graph, while the frozen colourings are isolated. Denote the nontrivial component by \(\Omega^\star\). Then
\[
\Omega^\star=\Omega_q(G)\setminus\mathcal F_q(G)
\]
and hence
\[
\frac{|\Omega^\star|}{|\Omega_q(G)|}
\ge 1-\frac{4}{n+4}.
\]

The usual Glauber chain restricted to \(\Omega^\star\) has the uniform distribution on \(\Omega^\star\) as its stationary distribution. If \(\pi\) is uniform on all colourings and \(\pi^\star\) is uniform on \(\Omega^\star\), then
\[
\|\pi^\star-\pi\|_{\mathrm{TV}}
=\frac{|\mathcal F_q(G)|}{|\Omega_q(G)|}
\le \frac{4}{n+4}.
\]
Thus the stationary/limiting distribution on the nontrivial component is uniformly \(o(1)\)-close to the uniform distribution on all \((\Delta+1)\)-colourings, with no restriction on \(\Delta\).

Equivalently, a uniformly random colouring is nonfrozen with probability at least
\[
1-\frac{4}{n+4}.
\]

---

## 7. Necessary qualifications

1. **Complete graphs.** For \(G=K_n\), one has \(\Delta=n-1\), \(q=n\), and every proper \(n\)-colouring is frozen. Thus a literal assertion covering all connected graphs after simply deleting \(\Delta=o(n)\) is false. The theorem resolves the substantive noncomplete case.

2. **Connectedness is essential.** If \(G\) is the disjoint union of \(r\) copies of \(K_q\), then \(\Delta=q-1=o(rq)\) as \(r\to\infty\), yet every proper \(q\)-colouring is frozen. Thus the catalog statement must retain the connectedness hypothesis from the source context.

3. **No mixing-time conclusion.** The argument proves that the unique nontrivial component supports an almost-uniform stationary distribution. It does not bound the time required for Glauber dynamics to approach that distribution; in particular, it does not prove a polynomial-time sampling algorithm.