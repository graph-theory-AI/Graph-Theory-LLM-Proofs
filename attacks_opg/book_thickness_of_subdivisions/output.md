```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The conjecture is false even for exact one-subdivisions: graphs of unbounded book thickness can have one-subdivisions of book thickness at most 5.",
  "would_publish": false,
  "caveats": "Uses the published bounded-queue, unbounded-stack theorem cited in the question; no optimality of 5 is claimed."
}
```

# Disproof for the exact one-subdivision formulation

Write \(S(G)\) for the graph obtained by subdividing every edge of \(G\) **exactly once**. The following stronger statement follows from the published result cited in the question:
\[
\sup\{\operatorname{bt}(G):\operatorname{bt}(S(G))\le 5\}=\infty.
\]

The distinction between one subdivision and the six-edge paths mentioned in the catalog is important. Rather than leaving that distinction implicit, we can bypass it with an elementary layout construction.

## 1. The published input

A **queue layout** consists of a linear vertex order and an edge-colouring in which no two edges of the same colour are nested. Thus edges \(v_av_b\) and \(v_cv_d\), with \(a<b\) and \(c<d\), cannot have the same colour when
\[
a<c<d<b.
\]
The minimum number of colours is the **queue-number**, denoted \(\operatorname{qn}(G)\).

The established result we use is:

> **Dujmović–Eppstein–Hickingbotham–Morin–Wood.**  
> For every positive integer \(M\), there is a finite simple graph \(G\) such that
> \[
> \operatorname{qn}(G)\le 4
> \qquad\text{and}\qquad
> \operatorname{bt}(G)>M.
> \]

This is the result in the paper supplied in the question: *Stack-number is not bounded by queue-number*, **Combinatorica** 42 (2022), 151–164, arXiv:2011.04195. Stack-number and book thickness are the same parameter.

The remainder of the argument, including the exact-one-subdivision step, is proved below.

## 2. Converting a queue layout into a book embedding of the one-subdivision

**Lemma.** For every finite simple graph \(G\),
\[
\boxed{\operatorname{bt}(S(G))\le \operatorname{qn}(G)+1.}
\]

**Proof.** Fix a \(q\)-queue layout of \(G\), with vertex order
\[
v_1\prec v_2\prec\cdots\prec v_n
\]
and queues \(Q_1,\ldots,Q_q\).

For each edge \(e\), write
\[
e=v_{a(e)}v_{b(e)},\qquad a(e)<b(e),
\]
and let \(x_e\) be its unique subdivision vertex.

Construct a spine order for \(S(G)\) as follows:

1. Place all original vertices first, in the order \(v_1,\ldots,v_n\).
2. Place all subdivision vertices afterward, in **decreasing lexicographic order** of
   \[
   (a(e),b(e)).
   \]

Use pages \(P_0,P_1,\ldots,P_q\). Assign
\[
v_{a(e)}x_e\in P_0
\]
for every edge \(e\), and, when \(e\in Q_i\), assign
\[
v_{b(e)}x_e\in P_i.
\]

We check every type of page.

### Page \(P_0\)

Consider edges \(v_{a(e)}x_e\) and \(v_{a(f)}x_f\). If \(a(e)=a(f)\), they share an endpoint and do not cross.

Otherwise, assume \(a(e)<a(f)\). The subdivision vertices were ordered in decreasing lexicographic order, so \(x_f\prec x_e\). Consequently,
\[
v_{a(e)}\prec v_{a(f)}\prec x_f\prec x_e.
\]
The two edges are nested, not crossing. Thus \(P_0\) is a valid page.

### Page \(P_i\), for \(1\le i\le q\)

Consider \(e,f\in Q_i\). If \(b(e)=b(f)\), the corresponding edges on \(P_i\) share an endpoint.

Otherwise, assume \(b(e)<b(f)\). We must have
\[
a(e)\le a(f).
\]
Indeed, if \(a(f)<a(e)\), then
\[
a(f)<a(e)<b(e)<b(f),
\]
so \(f\) and \(e\) would be nested in the original queue \(Q_i\), a contradiction.

Since \(a(e)\le a(f)\) and \(b(e)<b(f)\), decreasing lexicographic order puts \(x_f\) before \(x_e\). Hence
\[
v_{b(e)}\prec v_{b(f)}\prec x_f\prec x_e,
\]
again giving nesting rather than crossing.

Every page is therefore crossing-free. The construction uses \(q+1\) pages and introduces exactly one vertex on each original edge. ∎

## 3. Contradiction to the proposed function

Apply the published theorem to obtain graphs of arbitrarily large book thickness and queue-number at most \(4\). The lemma gives, for every such graph,
\[
\operatorname{bt}(S(G))\le 5.
\]

Suppose the function in the question existed. Set
\[
C=\max\{f(1),f(2),f(3),f(4),f(5)\}.
\]
This maximum avoids assuming that \(f\) is monotone.

Choose a graph from the published theorem with
\[
\operatorname{bt}(G)>C.
\]
It is nonempty, and its exact one-subdivision satisfies
\[
1\le \operatorname{bt}(S(G))\le 5.
\]
The proposed inequality would therefore imply
\[
\operatorname{bt}(G)
\le f(\operatorname{bt}(S(G)))
\le C,
\]
a contradiction.

Thus **no such function exists**, with \(G'\) interpreted exactly as in the original statement.

## Scope and dependencies

This is not a new disproof. Its sole external input is the published bounded-queue, unbounded-stack theorem cited in the question; that theorem’s proof is not reproduced here. The conversion to an exact one-subdivision is explicit and complete, so neither the six-edge subdivision claim nor an additional conjecture is needed.