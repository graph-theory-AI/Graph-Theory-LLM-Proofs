```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "In the standard layered-path model, capacity is weakly nonincreasing under adding a layer, while strict pointwise worsening is false already for 2-regular networks.",
  "would_publish": false,
  "caveats": "The source sentence does not specify weak versus strict monotonicity or the intended asymptotic regime; the large-d strict version remains open."
}
```

# Mathematical writeup

## 1. Formalization

The quoted conjecture is informal: “interference worsens” does not specify whether the desired conclusion is weak monotonicity, strict finite-parameter monotonicity, or an asymptotic separation as \(d\to\infty\).

I use the standard layered-path formulation. A depth-\(r\) network has layers
\[
V_1,\dots,V_r,\qquad |V_i|=N,
\]
and each consecutive bipartite graph \(G[V_i,V_{i+1}]\) is \(d\)-regular. A \(k\)-routing is a collection \(\mathcal P\) of \(k\) mutually vertex-disjoint paths, each meeting every layer once. Let
\[
\iota_G(\mathcal P)
\]
denote the largest size of a subcollection \(\mathcal Q\subseteq\mathcal P\) whose union induces exactly the paths in \(\mathcal Q\), with no cross-edges between different paths.

Define
\[
c_k(G)=\min_{\substack{\mathcal P\text{ a }k\text{-routing}}}
\frac{\iota_G(\mathcal P)}{k}
\]
and the sharp extremal capacity
\[
C_r(N,d,k)=\max_G c_k(G),
\]
where the maximum is over depth-\(r\), layerwise \(d\)-regular networks. For full task sets write
\[
C_r(N,d)=C_r(N,d,N).
\]

An index shift is needed if the source counts links rather than layers, but none of the conclusions below changes.

---

## 2. Weak monotonicity is immediate from truncation

### Proposition 2.1
For all admissible \(N,d,k,r\),
\[
C_{r+1}(N,d,k)\le C_r(N,d,k).
\]

More strongly, if \(G\) is a depth-\((r+1)\) network and \(G^{-}\) is its prefix on \(V_1,\dots,V_r\), then
\[
c_k(G)\le c_k(G^{-}).
\]

### Proof

Choose a \(k\)-routing \(\mathcal P\) in \(G^{-}\) attaining \(c_k(G^{-})\), and let \(S\subseteq V_r\) be its set of endpoints.

The last bipartite graph \(G[V_r,V_{r+1}]\) has a matching saturating \(S\). Indeed, for every \(X\subseteq V_r\),
\[
d|X|=e(X,N(X))\le d|N(X)|,
\]
so \(|N(X)|\ge |X|\), and Hall's theorem applies. Use such a matching to extend every path in \(\mathcal P\), producing a \(k\)-routing \(\mathcal P^+\) in \(G\).

If \(\mathcal Q^+\subseteq\mathcal P^+\) is induced in \(G\), then deleting its last vertices gives an induced subrouting of \(\mathcal P\) in \(G^{-}\): any cross-edge in the prefix would still be a cross-edge in the full network. Consequently,
\[
\iota_G(\mathcal P^+)\le \iota_{G^{-}}(\mathcal P).
\]
Therefore
\[
c_k(G)\le
\frac{\iota_G(\mathcal P^+)}k
\le
\frac{\iota_{G^{-}}(\mathcal P)}k
=c_k(G^{-}).
\]
Taking the maximum over depth-\((r+1)\) networks proves the proposition. \(\square\)

Thus, if the conjecture only asks for weak monotonicity of the sharp capacity, it is proved by this elementary argument. The fact that the source labels something open strongly suggests that a strict or asymptotic form was intended.

---

## 3. Strict finite-parameter monotonicity is false

### 3.1 An exact \(d=2\) result

For a perfect matching \(M\) in a simple \(d\)-regular bipartite graph, contract each edge of \(M\), and for every edge outside \(M\), put an edge between the two contracted matching edges containing its endpoints. This produces a loopless multigraph \(X_M\). Every vertex of \(X_M\) has degree
\[
2(d-1).
\]
Moreover, induced submatchings of \(M\) correspond exactly to independent sets in \(X_M\).

If \(I\) is independent in a nonempty \(D\)-regular multigraph, then
\[
D|I|=e(I,\overline I)\le D|\overline I|,
\]
and hence \(|I|\le N/2\). It follows that for every \(d\ge2\),
\[
C_2(N,d)\le \frac12.
\]

For \(d=2\), this bound remains sharp at every depth.

### Proposition 3.1
If \(N\) is even, then for every \(r\ge2\),
\[
C_r(N,2)=\frac12.
\]

### Proof

The upper bound follows from Proposition 2.1 and \(C_2(N,2)\le1/2\).

For the lower bound, identify every layer with \(\mathbb Z_N\), and between two consecutive layers put the edges
\[
x\longleftrightarrow x,\qquad x\longleftrightarrow x+1
\quad (x\in\mathbb Z_N).
\]
Each consecutive bipartite graph is a cycle \(C_{2N}\), and hence has exactly two perfect matchings: all edges \(x\mapsto x\), or all edges \(x\mapsto x+1\).

For any full routing, at every interface the conflict graph on the \(N\) paths is the same cycle \(C_N\): choosing either perfect matching only translates the path labels. Therefore the total conflict graph over all layers is still \(C_N\). Since \(N\) is even,
\[
\alpha(C_N)=N/2.
\]
Every full routing consequently has a largest induced subrouting of exactly \(N/2\) paths. Thus this network has capacity \(1/2\), proving equality. \(\square\)

This is a connected example, so the failure of strictness is not an artifact of disconnected block constructions.

### 3.2 Complete-block examples

More generally, suppose \(d\mid N\). Partition each layer into \(N/d\) corresponding blocks of size \(d\), and put a copy of \(K_{d,d}\) between corresponding blocks at every interface.

Every full routing contains exactly \(d\) paths in each block. An induced subrouting can contain at most one path from each block, while choosing one path from each block is induced. Hence this network has capacity exactly
\[
\frac1d
\]
at every depth.

In the special case \(N=d\), every simple \(d\)-regular bipartite interface is necessarily \(K_{d,d}\). Therefore the sharp extremal quantity itself satisfies
\[
C_r(d,d)=\frac1d
\qquad\text{for every }r\ge2.
\]
Thus strict monotonicity for all finite \(N,d\) is false, even with unbounded \(d\).

---

## 4. A monotone improvement of the quoted upper bound

Suppose the source theorem is used in its advertised uniform form
\[
C_s(N,d)\le A\,\frac{s}{d^{\,1-1/s}}
\]
with an absolute constant \(A\), in the parameter range under consideration.

By Proposition 2.1, every depth-\(r\) network may be truncated to any smaller depth \(s\). Consequently,
\[
C_r(N,d)
\le
A\min_{2\le s\le r}\frac{s}{d^{\,1-1/s}}.
\tag{4.1}
\]

This is stronger than simply applying the source theorem with \(s=r\), particularly when \(r\) exceeds \(\log d\). Writing \(L=\log d\),
\[
\frac{s}{d^{1-1/s}}
=\frac{s}{d}e^{L/s}.
\]
As a continuous function of \(s\), this is minimized at \(s=L\). Hence, for \(d\) sufficiently large,
\[
C_r(N,d)\le
\begin{cases}
O\!\left(\dfrac{r}{d^{1-1/r}}\right),&2\le r\le \log d,\\[1.2ex]
O\!\left(\dfrac{\log d}{d}\right),&r\ge \log d.
\end{cases}
\tag{4.2}
\]

Together with the complete-block construction, for \(d\mid N\) and \(r\ge\log d\) this gives
\[
\frac1d
\le C_r(N,d)
\le O\!\left(\frac{\log d}{d}\right).
\tag{4.3}
\]

Thus the known depth-\(r\) upper bound can at least be replaced by a genuinely nonincreasing envelope, and for depths at least logarithmic in \(d\) the remaining uncertainty is only a logarithmic factor above the elementary \(1/d\) construction. If the constant in the source theorem is not uniform in \(s\), only the fixed-\(s\) version of (4.1) is justified.

---

## 5. What remains open

There are three inequivalent readings of the catalog sentence:

1. **Weak monotonicity**
   \[
   C_{r+1}(N,d,k)\le C_r(N,d,k).
   \]
   This is proved by Proposition 2.1.

2. **Strict monotonicity for every finite parameter choice.**  
   This is false: \(C_r(N,2)=1/2\) for every even \(N\), and \(C_r(d,d)=1/d\) for every depth.

3. **An asymptotic strict degradation**, for example after taking a suitable large-\(N\) extremal limit and asking whether, for fixed \(r\),
   \[
   C_{r+1}(d)=o(C_r(d))
   \qquad(d\to\infty),
   \]
   or whether the exponent of \(d\) strictly improves with each added layer. This is not settled here. The complete-block examples and the \(d=2\) calculation do not refute such a formulation if it explicitly requires \(d\to\infty\) and \(N/d\to\infty\).

A precise statement of that asymptotic regime is indispensable. Merely comparing the two universal upper bounds
\[
O\!\left(d^{-1/2}\right)
\quad\text{and}\quad
O\!\left(r d^{-1+1/r}\right)
\]
does not by itself prove a strict comparison between the sharp capacities at two depths; that would also require matching lower information at the shallower depth or a direct separation argument.