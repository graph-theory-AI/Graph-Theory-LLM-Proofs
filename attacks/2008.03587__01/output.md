```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For G = K₂, every augmented subdivision G′ₖ has zombie number at most 2 = z(G) + 1, so the displayed strict inequality never holds.",
  "would_publish": false,
  "caveats": "This addresses the literal inequality > z(G)+1; the likely intended one-unit increase is a different question."
}
```

## Statement treated

I use the standard deterministic-zombie convention: zombies choose their initial vertices, the survivor then chooses its initial vertex, and every zombie move must decrease its distance to the survivor.

The displayed question asks whether, for every graph \(G\), some \(k\) satisfies
\[
z(G'_k)>z(G)+1.
\]
Since zombie numbers are integers, this asks for an increase of at least two.

## Lemma: cycles need at most two zombies

For every \(n\ge 3\),
\[
z(C_n)\le 2.
\]

Choose two initial zombie positions \(a,b\) so that the two \(a\)-\(b\) arcs have lengths
\[
\left\lfloor\frac n2\right\rfloor
\quad\text{and}\quad
\left\lceil\frac n2\right\rceil .
\]
If the survivor starts at \(a\) or \(b\), it is already caught. Otherwise it lies in the interior of one of these arcs, say \(Q\).

Suppose at some stage that the zombies are the endpoints of an arc \(Q\) of length \(L\le \lceil n/2\rceil\), with the survivor in its interior. From either endpoint, the distance to the survivor along \(Q\) is at most
\[
L-1\le \left\lceil\frac n2\right\rceil-1<\frac n2.
\]
Consequently, moving one step into \(Q\) is a legal distance-decreasing zombie move. Both zombies do so. Unless this captures the survivor, the arc between them containing the survivor has length \(L-2\). The survivor cannot leave that arc without stepping onto or passing through a zombie. Repetition therefore captures the survivor.

In fact,
\[
z(C_n)=2\qquad(n\ge4).
\]
Indeed, against one zombie the survivor initially chooses distance at least two. Whenever the zombie becomes adjacent, the survivor moves to its other cycle-neighbor, which is at distance two from the zombie when \(n\ge4\). Thus one zombie cannot capture.

## Counterexample

Take
\[
G=K_2
\]
with endpoints \(u,v\). Clearly \(z(K_2)=1\).

After subdividing its sole edge \(k\) times, the replacement is a path
\[
u-x_1-\cdots-x_k-v.
\]
Re-adding the original edge \(uv\) produces exactly the cycle
\[
G'_k\cong C_{k+2}
\]
under the usual convention that \(k\) new vertices are inserted. Hence
\[
z(G'_k)\le2=z(K_2)+1
\]
for every \(k\). In particular, the required strict inequality
\[
z(G'_k)>z(K_2)+1=2
\]
never holds. For the suggested value \(k=5\), one has \(G'_5=C_7\) and
\[
z(G'_5)=2.
\]

Any alternative indexing convention for subdivision only changes the length of the resulting cycle and not the argument.

## Likely intended formulation

The two formulations
\[
z(G'_k)>z(G)+1
\quad\text{and}\quad
z(G'_k)\ge z(G)+1
\]
are not equivalent. The latter is equivalent to the strict increase
\[
z(G'_k)>z(G).
\]
The example \(G=K_2\) separates them: for every \(k\ge2\),
\[
z(G'_k)=2=z(G)+1.
\]
Thus it refutes the displayed formulation but supports, rather than refutes, the likely intended one-unit-increase formulation.

As a small partial result for that corrected version, it holds for every nontrivial tree \(T\) when \(k\ge2\). Indeed, \(z(T)=1\). For any edge \(uv\in E(T)\), the original edge together with its subdivided replacement forms a cycle \(C_{k+2}\). Because \(uv\) is a bridge of \(T\), this cycle is a 1-Lipschitz retract of \(T'_k\): collapse the two components of \(T-uv\), together with their added subdivision paths, to \(u\) and \(v\), respectively. Therefore
\[
c(T'_k)\ge c(C_{k+2})=2,
\]
and hence
\[
z(T'_k)\ge c(T'_k)\ge2=z(T)+1.
\]

This does not settle the corrected formulation for general nontrivial graphs. If \(K_1\) is admitted, even that corrected formulation requires an exception, since \(K'_k=K_1\) for every \(k\).