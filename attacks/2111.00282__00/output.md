```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every pair of vertices differing on at most d other vertices in a graph of twin-width at most d is extendible as the first contraction of a 2d-sequence, giving a polynomially findable first move but not a full approximation algorithm.",
  "would_publish": false,
  "caveats": "The completion uses an unknown sequence of an induced subgraph; naive recursion can accumulate unbounded width even when d equals 1, and novelty relative to folklore has not been checked."
}
```

# Mathematical writeup

## 1. Formal interpretation of the challenge

I use the standard partition formulation of twin-width. For a partition \(\mathcal P\) of \(V(G)\), two distinct parts \(A,B\in\mathcal P\) are:

- black-adjacent if \(G[A,B]\) is complete;
- black-nonadjacent if \(G[A,B]\) is empty;
- red-adjacent otherwise.

A contraction replaces two parts by their union. The width of a contraction sequence is the maximum red degree occurring along it.

The algorithmic challenge is interpreted as asking for a computable function \(f\) and an FPT, or at least XP, algorithm which, whenever
\[
\operatorname{tww}(G)\le d,
\]
constructs a contraction sequence of width at most \(f(d)\). Whether the algorithm must also soundly certify \(\operatorname{tww}(G)>d\) is immaterial for the partial results below.

I do not obtain such a full algorithm.

---

## 2. A near-twin insertion lemma

For distinct vertices \(u,v\), put
\[
\delta_G(u,v)
=
\bigl|\{x\in V(G)\setminus\{u,v\}:
ux\in E(G)\mathbin{\mathsf{xor}}vx\in E(G)\}\bigr|.
\]
Thus \(\delta_G(u,v)\) is the number of external vertices on which \(u\) and \(v\) have different adjacency.

### Lemma 2.1: lifting a sequence after a near-twin contraction

Let \(u,v\in V(G)\) be distinct and let \(k=\delta_G(u,v)\). If \(G-u\) has a contraction sequence of width at most \(w\), then \(G\) has a contraction sequence of width at most \(w+k\) whose first contraction is \(uv\).

Moreover, given the sequence for \(G-u\), the new sequence can be constructed in polynomial time.

#### Proof

Let
\[
D=\{x\in V(G)\setminus\{u,v\}: ux\in E(G)\mathbin{\mathsf{xor}}vx\in E(G)\},
\qquad |D|=k.
\]

First contract \(u\) and \(v\). Now follow the given sequence for \(G-u\), with the following lifting rule: whenever the current part containing \(v\) in the sequence for \(G-u\) is \(B\), use \(B\cup\{u\}\) in the lifted sequence. All other parts are unchanged.

This is a valid contraction sequence. We bound its red degrees.

Consider a state of the sequence for \(G-u\), and let \(B\) be its part containing \(v\). Let \(C\) be another current part disjoint from \(D\).

- If \(B\) and \(C\) are already red-adjacent, adding \(u\) to \(B\) cannot make their bipartite adjacency homogeneous.
- If \(B\) and \(C\) are homogeneously adjacent or homogeneously nonadjacent, then \(v\) has the corresponding adjacency to every vertex of \(C\). Since \(C\cap D=\varnothing\), \(u\) has exactly the same adjacency to every vertex of \(C\). Hence \(B\cup\{u\}\) and \(C\) retain the same black relation.

Consequently, the relation involving the enlarged part \(B\cup\{u\}\) can differ from that involving \(B\) only for current parts containing at least one vertex of \(D\). There are at most \(k\) such parts. Therefore
\[
\deg_{\mathrm{red}}(B\cup\{u\})\le w+k.
\]

Every other current part has exactly the same relations as before except possibly its relation to \(B\cup\{u\}\). Its red degree therefore increases by at most one. If \(k\ge1\), this gives at most \(w+1\le w+k\); if \(k=0\), no relation changes at all.

Thus every lifted state has red degree at most \(w+k\). ∎

### Corollary 2.2: every locally admissible first pair is \(2d\)-extendible

If
\[
\operatorname{tww}(G)\le d
\quad\text{and}\quad
\delta_G(u,v)\le d,
\]
then there is a contraction sequence of width at most \(2d\) whose first contraction is \(uv\).

#### Proof

Twin-width is hereditary under vertex deletion: restricting every partition in a width-\(d\) sequence to \(V(G)\setminus\{u\}\), and suppressing repeated states, does not increase any red degree. Hence
\[
\operatorname{tww}(G-u)\le d.
\]
Apply Lemma 2.1 with \(w=d\) and \(k\le d\). ∎

The universal quantifier is relevant: this applies to **every** pair with \(\delta_G(u,v)\le d\), not merely to a pair belonging to some unknown optimal sequence.

---

## 3. A polynomially identifiable first contraction

If \(\operatorname{tww}(G)\le d\), then the first contraction in a width-\(d\) sequence merges some pair \(u,v\) satisfying
\[
\delta_G(u,v)\le d,
\]
because immediately after merging them the new part has red degree exactly \(\delta_G(u,v)\).

Thus the following procedure is polynomial:

1. Compute \(\delta_G(u,v)\) for all pairs \(u,v\).
2. If every value exceeds \(d\), correctly conclude that \(\operatorname{tww}(G)>d\).
3. Otherwise select any pair with \(\delta_G(u,v)\le d\).

Under the promise \(\operatorname{tww}(G)\le d\), the selected pair is guaranteed by Corollary 2.2 to be the first contraction of some \(2d\)-sequence.

Naively this takes \(O(n^3)\) time.

This does not construct the rest of that \(2d\)-sequence: the proof invokes an unknown width-\(d\) sequence of \(G-u\). It only shows that choosing the first pair is not itself the obstruction.

---

## 4. A polynomial near-twin peeling procedure

The hereditary property gives a somewhat stronger polynomial-time object.

Starting with \(S=V(G)\), repeat while \(|S|\ge2\):

1. Find \(u,v\in S\) with
   \[
   \delta_{G[S]}(u,v)\le d.
   \]
2. If none exists, output \(G[S]\).
3. Otherwise record \(u\) with parent \(v\), and delete \(u\) from \(S\).

If \(\operatorname{tww}(G)\le d\), this procedure never gets stuck, regardless of which admissible pair and which endpoint are chosen: every remaining graph is induced and therefore still has twin-width at most \(d\).

Conversely, if the procedure stops on \(H=G[S]\), then \(H\) has no possible first contraction of width at most \(d\), so
\[
\operatorname{tww}(H)>d.
\]
By heredity,
\[
\operatorname{tww}(G)\ge \operatorname{tww}(H)>d.
\]

Hence in \(O(n^4)\) time one obtains either:

- a sound induced-subgraph certificate that \(\operatorname{tww}(G)>d\), or
- an ordering \(v_1,\dots,v_n\) and later parents \(p_i\) such that
  \[
  \left|
  \{v_j:j>i,\ v_j\ne p_i,\ 
  v_iv_j\in E(G)\mathbin{\mathsf{xor}}p_iv_j\in E(G)\}
  \right|\le d.
  \]

The difficulty is converting such an ordering into a bounded-width contraction sequence.

---

## 5. Why the peeling order does not directly solve the problem

For a completed peeling order \(v_1,\dots,v_n\), let \(p_i\) be the recorded parent of \(v_i\), and define its exception set
\[
X_i=
\{v_j:j>i,\ v_j\ne p_i,\ 
v_iv_j\in E(G)\mathbin{\mathsf{xor}}p_iv_j\in E(G)\}.
\]
We have \(|X_i|\le d\).

Form the exception graph \(E_X\) with edges \(v_ix\) for \(x\in X_i\), naturally oriented from the earlier to the later vertex. Thus this orientation has maximum out-degree at most \(d\).

If one contracts \(v_i\)'s current bag into \(p_i\)'s current bag in increasing order of \(i\), then at every stage:

> every red edge between two current bags is witnessed by an edge of \(E_X\) crossing those two bags.

Indeed, suppose there is no exception edge between current bags \(A\) and \(B\). Starting from any \(a\in A\), \(b\in B\), repeatedly replace the earlier of the two current vertices by its parent. At each replacement the other endpoint was still present when the earlier vertex was peeled. The adjacency can change only if the corresponding pair is an exception edge crossing \(A,B\). Thus, in the absence of such an edge, every adjacency between \(A\) and \(B\) equals the adjacency between their current representatives, so \(A,B\) are homogeneous.

Consequently, the red degree is bounded by the maximum degree of the quotient of \(E_X\) under the current parent bags. The problem is that bounded out-degree in \(E_X\) does not bound these quotient degrees: many exception edges can accumulate in one bag.

### Explicit obstruction at \(d=1\)

Let \(H_m\) be the half-graph with bipartition
\[
A=\{a_1,\dots,a_m\},\qquad B=\{b_1,\dots,b_m\},
\]
and edges
\[
a_ib_j\in E(H_m)\quad\Longleftrightarrow\quad i\le j.
\]

#### Claim 5.1

\[
\operatorname{tww}(H_m)\le1.
\]

#### Proof

Merge \(a_1,a_2\) to obtain \(A_2\), and then merge \(b_1,b_2\) to obtain \(B_2\). The only red edge is \(A_2B_2\).

Inductively, suppose
\[
A_i=\{a_1,\dots,a_i\},\qquad
B_i=\{b_1,\dots,b_i\}
\]
are joined by the only red edge.

First merge \(A_i\) with \(a_{i+1}\). The new bag remains red only to \(B_i\); it is complete to every future \(b_j\), \(j\ge i+1\), and anticomplete to future \(a\)-vertices. Then merge \(B_i\) with \(b_{i+1}\), again retaining only the single red edge to the enlarged \(A\)-bag. At the end merge \(A_m\) and \(B_m\).

Thus the entire sequence has width one. ∎

On the other hand, in the induced graph remaining after deleting
\[
a_1,\dots,a_{i-1},
\]
the vertices \(a_i,a_{i+1}\) differ only on \(b_i\). Hence
\[
\delta(a_i,a_{i+1})=1.
\]
A valid near-twin peeling order may therefore choose
\[
p(a_i)=a_{i+1}\qquad (1\le i<m).
\]

If these recorded parent contractions are performed consecutively, after forming
\[
A_i=\{a_1,\dots,a_i\},
\]
the bag \(A_i\) is red-adjacent to each of
\[
b_1,\dots,b_{i-1}.
\]
Indeed, for \(j<i\), some vertices of \(A_i\) are adjacent to \(b_j\) and some are not. Thus
\[
\deg_{\mathrm{red}}(A_i)=i-1.
\]

This gives arbitrarily large width from a legitimate \(1\)-near-twin peeling order, even though the graph itself has twin-width at most one. Equivalently, the exception graph here has natural out-degree one, but its quotient degree along the chosen parent contractions is unbounded.

The good width-one sequence repairs each discrepancy by alternately contracting the corresponding \(a\)- and \(b\)-bags. The local peeling information alone does not force this repair schedule.

---

## 6. Why the insertion lemma does not close an induction

A tempting recursive algorithm is:

1. choose \(u,v\) with \(\delta_G(u,v)\le d\);
2. recursively find a sequence for \(G-u\);
3. lift it using Lemma 2.1.

If the recursive sequence has width \(q\), the lifted one has width at most
\[
q+d,
\]
not \(q\). Repeating this gives an \(O(nd)\) bound rather than a function of \(d\). The half-graph construction above shows that such additive accumulation can genuinely occur for this recursion when \(d=1\).

Likewise, after an arbitrary admissible contraction the existence guarantee changes from \(d\) to at most \(2d\). Iterating only this guarantee leads to
\[
d,\,2d,\,4d,\,8d,\dots,
\]
rather than a parameter-only bound.

Thus the missing ingredient is a polynomial method that globally schedules the repairs of the bounded local discrepancy sets.

---

## 7. Fully resolved special case \(d=0\)

For completeness, the argument closes when \(d=0\).

If \(\operatorname{tww}(G)=0\), some pair \(u,v\) has
\[
\delta_G(u,v)=0;
\]
they are external twins. Contracting them creates no red edge, and Lemma 2.1 with \(k=0\) shows that any width-zero sequence of \(G-u\) lifts without loss. Recursively finding and contracting external twins therefore constructs a width-zero sequence in polynomial time. If no such pair exists at some stage, the graph has positive twin-width.

This is the familiar cograph case.

---

## 8. Complexity and remaining gap

Taking the NP-completeness assertion in the prompt as given, a polynomial algorithm with \(f(d)=d\) would imply \(P=NP\), already for \(d=4\). This does not obstruct an approximation with \(f(4)>4\).

The results above establish:

1. every \(d\)-near-twin pair is a \(2d\)-extendible first move;
2. such a pair, or a sound lower-bound core, is polynomially findable;
3. a complete bounded-exception peeling order is polynomially findable on every promised instance;
4. local exception bounds do not control the width of the induced parent-contraction sequence, even for twin-width one.

They do **not** give an XP or FPT construction of an \(f(d)\)-sequence for general unordered graphs. The catalogued challenge therefore remains open.