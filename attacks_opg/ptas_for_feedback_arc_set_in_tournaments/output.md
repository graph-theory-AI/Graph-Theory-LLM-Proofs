```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Yes: Kenyon-Mathieu and Schudy established a PTAS for feedback arc set in tournaments at STOC 2007.",
  "would_publish": false,
  "caveats": "This invokes the published PTAS identified in the supplied catalog; it is not a new proof of that algorithm."
}
```

## 1. Established resolution

The question has an affirmative answer and was resolved before the stated 2013 posting date. The relevant publication, already identified in your catalog, is:

> C. Kenyon-Mathieu and W. Schudy, **“How to rank with few errors,”** STOC 2007.  
> DOI: **10.1145/1250790.1250806**.

Its PTAS for tournament ranking applies directly to the unweighted feedback arc set problem asked here. No extension to arbitrary arc weights is needed.

Below is the precise connection between the ranking formulation and the arc-deletion formulation.

## 2. Feedback arc sets and vertex orderings

Let \(T=(V,A)\) be a tournament, with \(n=|V|\). For a linear ordering
\[
\pi:V\longrightarrow\{1,\ldots,n\},
\]
define its set of **backward arcs** by
\[
B_T(\pi)=\{(u,v)\in A:\pi(u)>\pi(v)\},
\]
and let \(b_T(\pi)=|B_T(\pi)|\).

Write
\[
\operatorname{fas}(T)
=\min\{|F|:F\subseteq A,\ T-F\text{ is acyclic}\}.
\]

**Lemma.**
\[
\operatorname{fas}(T)=\min_{\pi} b_T(\pi).
\]

**Proof.** For every ordering \(\pi\), all arcs of \(T-B_T(\pi)\) point forward in \(\pi\). A directed cycle would require positions to increase strictly around a cycle, which is impossible. Thus \(B_T(\pi)\) is a feedback arc set, and
\[
\operatorname{fas}(T)\leq \min_\pi b_T(\pi).
\]

Conversely, let \(F\) be any feedback arc set. Since \(T-F\) is acyclic, it has a topological ordering \(\pi\). Every arc outside \(F\) points forward in this ordering, so
\[
B_T(\pi)\subseteq F.
\]
Taking \(F\) minimum gives
\[
\min_\pi b_T(\pi)\leq \operatorname{fas}(T).
\]
Together these prove the equality. \(\square\)

## 3. Applying the published PTAS

The unweighted specialization of the Kenyon-Mathieu–Schudy theorem gives a polynomial-time approximation scheme for minimizing \(b_T(\pi)\).

A sufficient, standard randomized formulation is: for every fixed \(\varepsilon>0\), an algorithm running in time polynomial in \(n\) returns, with constant success probability, an ordering \(\widehat\pi\) satisfying
\[
b_T(\widehat\pi)
\leq (1+\varepsilon)\min_\pi b_T(\pi).
\]
The success probability can be amplified by independent repetitions and retaining the ordering with the fewest backward arcs.

To obtain the requested feedback arc set:

1. Run this ordering approximation scheme on \(T\).
2. Return \(F=B_T(\widehat\pi)\).

By the lemma, \(F\) is a feedback arc set and, whenever the approximation guarantee holds,
\[
|F|
=b_T(\widehat\pi)
\leq (1+\varepsilon)\min_\pi b_T(\pi)
=(1+\varepsilon)\operatorname{fas}(T).
\]
Constructing \(F\) from the ordering takes \(O(n^2)\) time, so the total running time remains polynomial for every fixed \(\varepsilon\).

The zero-optimum case causes no difficulty: test first whether \(T\) is acyclic and, if so, return the empty set. This also handles tournaments with at most one vertex. As usual, a PTAS requires polynomial running time for each fixed \(\varepsilon\), not necessarily polynomial dependence on \(1/\varepsilon\).

## 4. Scope of this writeup

The substantive external ingredient is the **published PTAS theorem**, not another conjecture. Its algorithm and approximation analysis are not reproved here; the reduction from its ranking objective to the stated feedback-arc-deletion objective is complete.

Consequently, the appropriate status is **already resolved**, rather than a new proof or partial progress. The later semi-streaming result concerns stronger resource restrictions and is not needed to answer the original question.