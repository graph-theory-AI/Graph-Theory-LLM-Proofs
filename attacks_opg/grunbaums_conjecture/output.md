```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The full conjecture was disproved by Kochol (2009), using snarks with polyhedral embeddings in orientable surfaces.",
  "would_publish": false,
  "caveats": "Literature-based resolution using the published result identified in the supplied catalog; no explicit embedding is reconstructed here."
}
```

## 1. The stated conjecture is already disproved

The 2007 discussion predates the counterexamples recorded in the supplied literature review. The relevant published reference, whose AMS entry the supplied catalog reports as directly verified, is:

> M. Kochol, **Polyhedral embeddings of snarks in orientable surfaces**, *Proceedings of the American Mathematical Society* **137** (2009), 1613–1619.  
> DOI: **10.1090/S0002-9939-08-09698-6**.

The part of the reported result needed here is:

**Known counterexample theorem.** There exists a snark \(H\) admitting a polyhedral cellular embedding in a closed orientable surface.

Only the facts that \(H\) is cubic and is not properly \(3\)-edge-colorable are needed from the snark condition. Below I verify carefully why such an embedding contradicts the *exact* triangulation formulation in the question.

## 2. Passing from a polyhedrally embedded snark to a counterexample

**Lemma.** If a cubic graph \(H\) has a polyhedral cellular embedding in a closed surface \(\Sigma\), then its embedded dual \(T=H^*\) is a simple loopless triangulation of \(\Sigma\). Moreover, \(T^*\cong H\).

**Proof.** The polyhedral condition gives the following properties:

1. Every facial boundary of \(H\) is a simple cycle.
2. Two distinct faces have closures intersecting in the empty set, a single vertex, or a single edge.

The vertices of \(T\) correspond to the faces of \(H\), and each edge of \(H\) supplies an edge of \(T\).

**There are no dual loops.** If an edge \(e\) of \(H\) had the same face on both sides, the boundary walk of that face would traverse \(e\) twice. This contradicts property 1. Thus the endpoints of every edge of \(T\) are distinct.

**There are no parallel dual edges.** Two edges of \(T\) joining the same two vertices would correspond to two distinct edges shared by the same two faces of \(H\). This contradicts property 2.

**Every dual face is a triangle.** A face of \(T\) corresponds to a vertex \(v\) of \(H\). Since \(H\) is cubic, its boundary has length three. Furthermore, the three face-corners around \(v\) belong to three distinct faces of \(H\): otherwise one facial boundary would visit \(v\) more than once, contrary to property 1. Consequently, each face boundary of \(T\) is a genuine \(3\)-cycle, not merely a closed walk of length three.

Thus \(T\) is a simple loopless triangulation. Cellular duality preserves the underlying surface and is involutive up to embedded graph isomorphism, so \(T^*\cong H\). \(\square\)

Now apply the lemma to the orientably embedded snark supplied by Kochol’s result. The resulting graph \(T\) satisfies every hypothesis of the conjecture:

\[
T\text{ is simple and loopless, and triangulates an orientable surface.}
\]

But
\[
T^*\cong H,
\]
and \(H\) has no proper \(3\)-edge-coloring. Therefore \(T\) violates the asserted conclusion.

## 3. Scope and dependence of this resolution

This is a **literature-based disproof**, not a new counterexample construction. The nontrivial existence theorem is imported from the published result identified in the supplied materials; its graph and rotation system are not reproduced or independently checked here. The duality argument above checks why the reported theorem supplies the required counterexamples.

No claim about the smallest counterexample genus is needed for this conclusion. Nor does this argument settle the face-width weakenings: existence of a polyhedrally embedded snark does not, by itself, produce counterexamples of arbitrarily large face-width on a fixed surface.

Accordingly, the full conjecture should not be treated as an open research target. The restricted-genus and large-face-width questions are separate problems.