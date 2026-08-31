```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "Every subsequential limit is finite-support maximal, and any distinct limit at the standard 3-orientation level must carry a directed bi-infinite disagreement interface.",
  "would_publish": false,
  "caveats": "The argument does not exclude such an interface, and the disagreement lemma assumes the usual 3-orientation encoding of Schnyder woods."
}
```

## 1. Reduction to the perimeter limit

Let \(U_m\) denote the UIPT with boundary length \(m\), and let \(W_m\) be its maximal Schnyder wood. Let \(U_{\mathbb H}\) be the UIHPT and \(W_{\mathbb H}^{+}\) its unique maximal Schnyder wood.

By the quoted Theorem 1.2, for every fixed \(m\),
\[
(T_n^m,W^{+}(T_n^m))
   \xrightarrow[n\to\infty]{(d)}
(U_m,W_m)
\]
in the rooted decorated local topology. Thus the conjecture is equivalent to
\[
(U_m,W_m)\xrightarrow[m\to\infty]{(d)}
(U_{\mathbb H},W_{\mathbb H}^{+}).
\tag{1}
\]
I take as an input the standard undecorated convergence
\[
U_m\xrightarrow[m\to\infty]{(d)}U_{\mathbb H}.
\tag{2}
\]

The difficulty is that the map \(G\mapsto W^{+}(G)\) need not be continuous in the local topology.

## 2. What compactness gives unconditionally

Call a Schnyder configuration **finite-support maximal** if there is no legal upward Schnyder flip, or finite upward modification in the Schnyder lattice, whose entire support is finite.

### Proposition 2.1

The sequence \((U_m,W_m)\) is tight in the decorated local topology. Every subsequential limit \((U_{\mathbb H},\widehat W)\) has the following properties:

1. \(\widehat W\) satisfies every Schnyder axiom having a finite witness;
2. \(\widehat W\) is finite-support maximal.

Here \(\widehat W\) may a priori fail a genuinely global requirement, such as a prescribed destination of an infinite monochromatic path.

### Proof

Schnyder marks—orientations, colors, and any corner labels—take values in a finite alphabet. Tightness of the undecorated maps therefore implies tightness of the marked maps: after restricting to a finite collection of likely radius-\(R\) unmarked balls, only finitely many markings of those balls are possible.

Take a convergent subsequence
\[
(U_{m_j},W_{m_j})\xrightarrow[j\to\infty]{(d)}
(U_{\mathbb H},\widehat W).
\]

Any failure of a local vertex, edge, face, or cyclic-order rule is witnessed in some finite radius. The corresponding cylinder event has probability zero for every \(j\), and hence probability zero in the limit.

Now suppose \(\widehat W\) admitted a legal upward modification supported on a finite set. The support, together with every incidence needed to verify legality, is contained in some finite ball. Local convergence would transfer exactly the same legal upward modification to \(W_{m_j}\) for all sufficiently large \(j\). This contradicts maximality of \(W_{m_j}\). ∎

Thus any failure of (1) must be caused by a defect “at infinity”; no bounded region can contain a certificate that the limiting configuration is nonmaximal.

## 3. A disagreement-interface obstruction

The preceding statement can be sharpened in the usual encoding of Schnyder woods by \(3\)-orientations. The following lemma is independent of randomness.

### Lemma 3.1

Let \(G\) be a locally finite plane graph, and let \(O\) and \(O^{+}\) be two orientations having the same prescribed outdegree \(\alpha(v)\) at every vertex. Assume:

- both orientations admit the standard planar \(\alpha\)-orientation order;
- reversing a finite contractible directed cycle in the appropriate direction is an upward move;
- neither \(O\) nor \(O^{+}\) admits a finite upward move.

Orient every edge on which \(O\) and \(O^{+}\) disagree according to \(O\), and call the resulting directed graph \(D\). If \(O\ne O^{+}\), then \(D\) contains a directed double ray
\[
\ldots,v_{-1},v_0,v_1,\ldots .
\]

### Proof

At a vertex \(v\), let

- \(a(v)\) be the number of incident edges directed out of \(v\) in \(O\) and into \(v\) in \(O^{+}\);
- \(b(v)\) be the number directed into \(v\) in \(O\) and out of \(v\) in \(O^{+}\).

Since both orientations have the same outdegree at \(v\),
\[
a(v)-b(v)=\operatorname{outdeg}_{O}(v)
          -\operatorname{outdeg}_{O^{+}}(v)=0.
\]
Consequently,
\[
\operatorname{outdeg}_{D}(v)=\operatorname{indeg}_{D}(v).
\tag{3}
\]

We first show that \(D\) has no directed cycle. If \(C\) were such a cycle, then \(O\) directs \(C\) one way and \(O^{+}\) directs it the opposite way. Relative to the finite side of \(C\), exactly one of these two directed cycles is upward-flippable. It would therefore provide a finite upward move in either \(O\) or \(O^{+}\), contrary to the hypotheses.

Take any directed edge of the nonempty graph \(D\). Equation (3) allows it to be extended indefinitely both forwards and backwards. If a vertex were repeated, or the forward and backward extensions met, a directed cycle would result. Hence all vertices encountered are distinct, and the extension is a directed double ray. ∎

### Consequence for the conjecture

On a realization of \(U_{\mathbb H}\), compare the orientation \(\widehat O\) underlying a subsequential limit \(\widehat W\) with the orientation \(O_{\mathbb H}^{+}\) underlying the maximal wood.

Proposition 2.1 says that \(\widehat O\) has no finite upward move, while maximality gives the same property for \(O_{\mathbb H}^{+}\). Therefore, under the standard \(3\)-orientation correspondence,

\[
\widehat O\ne O_{\mathbb H}^{+}
\quad\Longrightarrow\quad
D(\widehat O,O_{\mathbb H}^{+})
\text{ contains a directed double ray.}
\tag{4}
\]

If the orientation uniquely determines the coloring once the boundary color normalization is fixed, then (4) applies to the full Schnyder wood. Otherwise a separate color-only disagreement would also have to be excluded.

Thus a counterexample to the conjecture cannot be a localized defect: it must be an infinite interface entering and leaving every sufficiently large neighborhood of the root.

## 4. A finite-radius sufficient criterion

The obstruction can also be formulated as a concrete local-rigidity estimate.

Fix \(r<R\). For a complete radius-\(R\) map patch \(P\), let \(\mathcal L_R(P)\) be the finite set of all Schnyder markings of \(P\) which:

1. satisfy every local Schnyder rule whose incidence data are contained in \(P\);
2. admit no upward flip whose support and legality certificate are contained in the interior of \(P\).

Call \(P\) **\((r,R)\)-rigid** if every two elements of \(\mathcal L_R(P)\) agree on the radius-\(r\) subpatch. Put
\[
q_{r,R}
 =\mathbb P\!\left(
 B_R(U_{\mathbb H})\text{ is not }(r,R)\text{-rigid}
 \right).
\]

Both \(W_m|_{B_R}\) and \(W_{\mathbb H}^{+}|_{B_R}\) belong to the appropriate set \(\mathcal L_R\). Coupling the unmarked radius-\(R\) balls optimally therefore gives
\[
\begin{aligned}
d_{\mathrm{TV}}\bigl(
 \mathcal L(B_r(U_m,W_m)),
 \mathcal L(B_r(U_{\mathbb H},W_{\mathbb H}^{+}))
\bigr)
&\le
d_{\mathrm{TV}}\bigl(
 \mathcal L(B_R(U_m)),
 \mathcal L(B_R(U_{\mathbb H}))
\bigr)
+q_{r,R}.
\end{aligned}
\tag{5}
\]
For fixed \(R\), the first term tends to zero by (2). Consequently, the conjecture would follow from the finite-volume estimate
\[
\forall r,\qquad \lim_{R\to\infty}q_{r,R}=0.
\tag{6}
\]

At the orientation level, failure of \((r,R)\)-rigidity forces a two-sided disagreement arm from \(B_r\) to the boundary of \(B_R\): balance at interior vertices allows both forward and backward continuation, while a closed continuation would give an upward cycle in one of the two configurations.

## 5. Remaining gap

Neither uniqueness of the globally maximal UIHPT wood nor one-endedness of the UIHPT rules out the double ray in (4). A one-ended plane graph can contain many proper double rays—for example, the half-plane square grid—so a probabilistic or Schnyder-specific argument is needed.

The unresolved step is therefore one of the following equivalent forms:

- rule out a compatible directed bi-infinite disagreement interface;
- prove the rigidity estimate (6);
- prove that every finite-support maximal local Schnyder configuration on the UIHPT is the globally maximal wood, including all asymptotic path conditions.

I do not have such an argument. Hence this is a structural reduction and finite-volume criterion, not a proof of the conjecture.