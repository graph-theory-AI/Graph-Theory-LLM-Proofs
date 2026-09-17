```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit construction proves the conjectured bound for every uniform blow-up of the regular cyclic tournament on 3^r vertices, and for its arbitrary one-vertex extensions when the part size is odd.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; no universal asymptotic improvement is obtained, and novelty of the special-case constructions is unchecked."
}
```

## 1. Statement of the partial results

Write \(\nu(T)\) for the **maximum** size of an arc-disjoint transitive-triple packing, and put
\[
g(n)=\left\lceil\frac{n(n-3)}6\right\rceil.
\]
The conjecture is \(\nu(T)\ge g(|T|)\).

For odd \(N=2h+1\), let \(R_N\) be the regular cyclic tournament on \(\mathbb Z_N\), with
\[
i\longrightarrow j
\quad\Longleftrightarrow\quad
j-i\pmod N\in\{1,\ldots,h\}.
\]
A *uniform blow-up* of \(R_N\) replaces each vertex \(i\) by a set \(V_i\) of the same size \(m\), directs all arcs between parts according to \(R_N\), and permits an arbitrary tournament inside each part.

**Theorem 1.** Let \(r,m\ge1\), set \(N=3^r\), and let \(T\) be any uniform blow-up of \(R_N\) with part size \(m\). Then
\[
\nu(T)\ge g(Nm).
\]
If \(m\) is odd, adjoining one vertex with completely arbitrary incident orientations also gives a tournament satisfying the conjecture.

The case \(r=1\) is the equal-size cyclic three-part construction from the previous attempt. The higher values use different quotient tournaments, beginning with \(R_9\).

A second consequence of the method is:

**Theorem 2.** Start with one-vertex tournaments and repeatedly perform the following operation: take five previously constructed tournaments of the same order, and orient the arcs between them according to an arbitrary five-vertex tournament. Every tournament obtained this way satisfies the conjecture.

Both results follow from a leave-controlled lifting lemma. Only the elementary edge-colouring device from the previous attempt is reused; the needed form is proved below. No packing-cover equality is assumed.

---

## 2. A lifting lemma

The **leave** of a packing is the spanning digraph consisting of its unused arcs.

### Edge-colouring fact

The edges of \(K_m\) can be properly coloured with \(m\) colours. When \(m\) is odd, the colouring can be chosen so that each colour misses exactly one vertex, and these missing vertices are all different.

For odd \(m>1\), label vertices and colours by \(\mathbb Z_m\) and colour \(\{a,b\}\) by
\[
\frac{a+b}{2}\pmod m.
\]
Colour \(c\) misses exactly vertex \(c\).

For even \(m\), use a one-factorization with \(m-1\) colours and add one unused colour. Explicitly, for even \(m\ge4\), label the vertices by
\[
\{\infty\}\cup\mathbb Z_{m-1}.
\]
Give \(\{\infty,a\}\) colour \(a\), and give \(\{a,b\}\) colour \((a+b)/2\) modulo \(m-1\). The cases \(m=1,2\) are immediate.

### Lifting lemma

**Lemma 3.** Suppose that a tournament \(Q\) on \(k\) vertices has a transitive-triple packing whose underlying leave is a disjoint union of cycles and isolated vertices. Let \(s\) be the number of isolated vertices.

Replace every vertex \(i\) of \(Q\) by an arbitrary \(m\)-vertex tournament \(T_i\), with uniform interpart orientations prescribed by \(Q\). If
\[
\nu(T_i)\ge g(m)
\]
for every isolated vertex \(i\) of the leave, then the resulting tournament satisfies the conjecture.

In particular, if the leave is a spanning union of cycles, there is **no assumption at all** on the tournaments inside the parts.

**Proof.** Let \(\mathcal P\) be the given packing in \(Q\), and put \(p=|\mathcal P|\). The leave has \(k-s\) edges, so
\[
3p=\binom{k}{2}-(k-s). \tag{1}
\]

There are three stages.

**First, lift the triples of \(\mathcal P\).** Label every part by \(\mathbb Z_m\). For each triple on quotient vertices \(i,j,\ell\), take the \(m^2\) triples
\[
\{(i,a),(j,b),(\ell,a+b)\},
\qquad a,b\in\mathbb Z_m.
\]
They are transitive because the quotient triple is transitive. They decompose all arcs between its three pairs of parts: for each such pair, its two labels determine the third label uniquely.

Different members of \(\mathcal P\) use different pairs of parts, so these lifted packings are arc-disjoint.

**Second, use the cycles of the leave to cover internal arcs.** Give each underlying leave cycle a cyclic successor relation. This direction is only bookkeeping; it need not agree with the tournament orientation.

If \(j\) is the successor of \(i\), properly colour the edges of \(K_{V_i}\) with the vertices of \(V_j\). For every internal edge \(uv\) coloured \(w\in V_j\), take
\[
\{u,v,w\}.
\]
This triple is transitive: \(w\) either dominates both \(u,v\), or is dominated by both.

Properness prevents repeated cross-arcs. Each leave pair of parts is used in just one of these families, and none was used in the first stage. Thus this stage adds
\[
(k-s)\binom m2
\]
triples.

**Third, pack inside the isolated parts.** Use \(g(m)\) triples in each such part.

The total number is at least
\[
m^2p+(k-s)\binom m2+s\,g(m).
\]
Using (1) and \(g(m)\ge m(m-3)/6\), this is at least
\[
\begin{aligned}
&m^2\frac{k(k-3)+2s}{6}
 +(k-s)\frac{m(m-1)}2
 +s\frac{m(m-3)}6\\
&\hspace{35mm}=\frac{km(km-3)}6.
\end{aligned}
\]
Since the packing size is an integer, it is at least \(g(km)\). \(\square\)

For the main application, \(s=0\). The crucial task is therefore to construct a suitable packing in \(R_{3^r}\).

---

## 3. An explicit difference construction

Call a set \(\{a,b,c\}\) of three distinct positive integers a **Schur triple** if \(a+b=c\).

**Lemma 4.** For every \(j\ge0\), the interval
\[
\left\{1,\ldots,3q_j\right\},
\qquad
q_j=\frac{3^j-1}{2},
\]
can be partitioned into \(q_j\) Schur triples.

**Proof.** The case \(q_0=0\) is empty. Suppose a partition exists for \(q\). Replace each of its triples \(a+b=c\) by
\[
\begin{split}
&\{3a-1,\ 3b,\ 3c-1\},\\
&\{3a,\ 3b+1,\ 3c+1\},\\
&\{3a+1,\ 3b-1,\ 3c\}.
\end{split} \tag{2}
\]
Each displayed set is a Schur triple.

For each old number \(t\), its three replacements
\[
3t-1,\quad 3t,\quad 3t+1
\]
are used exactly once. Consequently (2), over all old triples, partitions
\[
\{2,\ldots,9q+1\}.
\]
Add the triple
\[
\{1,9q+2,9q+3\}.
\]
The result partitions \(\{1,\ldots,9q+3\}\) into \(3q+1\) Schur triples. Since
\[
q_{j+1}=3q_j+1,
\]
the induction follows. \(\square\)

**Proposition 5.** For every \(r\ge1\), \(R_{3^r}\) has a packing of size \(g(3^r)\) whose leave is a directed Hamilton cycle.

**Proof.** Set
\[
N=3^r,\qquad h=\frac{N-1}{2},\qquad q=\frac{N-3}{6}.
\]
Lemma 4, with \(j=r-1\), partitions
\[
\{1,\ldots,h-1\}
\]
into \(q\) Schur triples.

For every such triple \(a+b=c\), take all \(N\) translates
\[
\{i,\ i+a,\ i+c\},
\qquad i\in\mathbb Z_N. \tag{3}
\]
Their arcs have positive cyclic differences \(a,b,c\), respectively. Because all three differences are at most \(h\), each triple in (3) is transitive.

Moreover, these \(N\) triangles cover every arc of each of the three difference classes \(a,b,c\) exactly once. Different Schur triples use disjoint difference classes. Hence the resulting packing has
\[
Nq=\frac{N(N-3)}6=g(N)
\]
members.

Its leave consists exactly of
\[
i\longrightarrow i+h,\qquad i\in\mathbb Z_N.
\]
Since \(\gcd(N,h)=1\), these arcs form a directed Hamilton cycle. \(\square\)

For example, in \(R_9\), the nine triples
\[
\{i,i+1,i+3\},\qquad i\in\mathbb Z_9,
\]
cover difference classes \(1,2,3\), leaving the directed Hamilton cycle of difference \(4\).

---

## 4. Uniform blow-ups and one arbitrary extra vertex

### Proof of the first assertion of Theorem 1

Apply Lemma 3 to the packing from Proposition 5. Its leave has no isolated vertices, so every internal tournament is permitted.

The construction gives exactly
\[
m^2\frac{N(N-3)}6+N\binom m2
=\frac{Nm(Nm-3)}6
=g(Nm)
\]
triples. This proves the first assertion.

### Controlling the leave for odd \(m\)

When \(m\) is odd, use the colouring in which colour \(a\) misses vertex \(a\). Between each successive pair of parts along the quotient’s directed Hamilton cycle, the unused arcs are then precisely the matching joining equal labels.

Thus the blow-up packing has a leave consisting of \(m\) vertex-disjoint directed cycles, each of length \(N\).

The following observation now applies.

**Lemma 6.** Let \(n\) be divisible by \(3\). Suppose a tournament \(T\) has a packing of size \(g(n)\) whose leave is a spanning disjoint union of directed cycles. Then adding one arbitrary vertex preserves the conjectured bound.

**Proof.** Let the new vertex be \(x\). An old leave arc \(u\to v\) is *bad* if
\[
x\to u\to v\to x;
\]
otherwise, it extends through \(x\) to a transitive triple.

At any old vertex \(v\), its incoming and outgoing leave arcs cannot both be bad: the incoming one would require \(v\to x\), while the outgoing one would require \(x\to v\).

Therefore the underlying graph of good leave arcs has minimum degree at least \(1\) and maximum degree at most \(2\). Its components are paths on at least two vertices and cycles. Every such component on \(t\) vertices has a matching of size at least \(t/3\), since
\[
\left\lfloor\frac t2\right\rfloor\ge \frac t3
\]
for \(t\ge2\), with cycles having \(t\ge3\).

There is consequently a matching of at least \(n/3\) good leave edges. Extending \(n/3\) of them through \(x\) adds that many arc-disjoint transitive triples. Finally,
\[
g(n+1)-g(n)=\frac n3
\qquad (3\mid n).
\]
This proves the lemma. \(\square\)

For odd \(m\), the controlled leave above satisfies Lemma 6. Theorem 1 follows in full. \(\square\)

---

## 5. Five-way substitution

The isolated-vertex allowance in Lemma 3 gives another family beyond the three-part construction.

**Lemma 7.** Every five-vertex tournament has two arc-disjoint transitive triples. Their underlying leave is a four-cycle and an isolated vertex.

**Proof.** Choose a transitive triple \(\{a,b,c\}\), and let the remaining vertices be \(x,y\), with \(x\to y\).

If some \(\{x,y,z\}\), \(z\in\{a,b,c\}\), is transitive, it is arc-disjoint from \(\{a,b,c\}\).

Otherwise all three such triples are cyclic, forcing
\[
y\to\{a,b,c\}\to x.
\]
Then
\[
\{y,a,b\},\qquad \{x,b,c\}
\]
are transitive and arc-disjoint.

Any two arc-disjoint triangles on five vertices share exactly one vertex. Removing their six underlying edges from \(K_5\) leaves a \(K_{2,2}\) on the other four vertices and isolates their common vertex. \(\square\)

Now take five equal parts of size \(m\), with an arbitrary five-vertex quotient. Choose the quotient packing supplied by Lemma 7. If the internal tournament corresponding to its isolated vertex satisfies the conjecture, Lemma 3 gives a packing of size at least
\[
2m^2+4\binom m2+g(m)
=g(5m). \tag{4}
\]
The other four internal tournaments may be arbitrary.

Inductively applying (4), starting with one-vertex tournaments, proves Theorem 2. In particular, arbitrary choices of five-vertex quotients at every node of a balanced substitution tree produce tournaments of order \(5^k\) satisfying the bound.

---

## 6. Scope and the remaining obstacle

These arguments establish the stated special cases, but do not prove the conjecture for arbitrary tournaments.

The decisive property is an explicitly constructed packing whose leave is a union of cycles. An arbitrary tournament need not have a homogeneous quotient of the forms used here, and no argument above produces such a leave in general.

Even the extension argument has a definite limitation. On a directed nine-cycle
\[
v_0\to v_1\to\cdots\to v_8\to v_0,
\]
two new vertices can both dominate precisely
\[
v_0,v_2,v_4,v_6
\]
among the old vertices. Then the four edges
\[
v_0v_1,\ v_2v_3,\ v_4v_5,\ v_6v_7
\]
are bad for both new vertices. Only five leave edges are available, whereas extending a packing of size \(g(9)=9\) to the target \(g(11)=15\) by this mechanism would require six distinct good leave edges. This is an obstruction to that extension mechanism, **not** a counterexample to the conjecture: repacking old triangles or using a triangle containing both new vertices remains possible.

Thus the universal bound and any improvement to the stated universal asymptotic lower bound remain unresolved here. The constructions are self-contained, but I have not checked whether these particular special-case results are already in the literature.