```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a quasipolynomial bound for the full substitution closure, polynomial bounds for bounded-dichromatic generators, and a quadratic bound for the transitive/triangle-generated class.",
  "would_publish": false,
  "caveats": "The full polynomial-preservation conjecture remains unsettled here; novelty of the sharper bounds has not been checked."
}
```

# 1. Main partial result

Write \(\vec\chi(T)\) for the dichromatic number and
\[
\vec\omega(T)=\min_{\prec}\omega(T^\prec)
\]
for the directed clique number.

For an integer \(q\ge 1\), define
\[
s(q)=\min\left\{r\ge 0:\binom{r}{\lfloor r/2\rfloor}\ge q\right\}.
\]
Thus \(s(1)=0\), \(s(2)=2\), and
\[
s(q)=\log_2 q+O(\log\log(q+2)).
\]

I prove the following bound, uniformly over substitution depth.

**Theorem 1.**  
Suppose \(\mathcal T\) has a nondecreasing binding function \(f\ge 1\):
\[
\vec\chi(S)\le f(\vec\omega(S))\qquad(S\in\mathcal T).
\]
If \(T\in\mathcal T^{\mathrm{subst}}\), \(w=\vec\omega(T)\), and
\(q=\lceil f(w)\rceil\), then
\[
\boxed{\qquad
\vec\chi(T)\le w^{\,1+s(q)}.
\qquad} \tag{1}
\]

In particular:

* If \(f(w)\le Cw^a\), then
  \[
  \vec\chi(T)\le \exp\!\bigl(O_{C,a}((\log w)^2)\bigr).
  \]
  Thus polynomial boundedness is preserved **up to a quasipolynomial loss**.
* If the generators have bounded dichromatic number, say
  \(\vec\chi(S)\le q_0\) for every \(S\in\mathcal T\), then
  \[
  \boxed{\vec\chi(T)\le \vec\omega(T)^{\,1+s(q_0)}}. \tag{2}
  \]
  This is genuine polynomial preservation, with no restriction on substitution depth or branching.

I also prove the stronger special-case bound
\[
\boxed{\vec\chi(T)\le \vec\omega(T)^2
\quad\text{for }T\in
\{TT_1,TT_2,\overrightarrow C_3\}^{\mathrm{subst}}.} \tag{3}
\]

The arguments are self-contained and do not use the previous attempt’s ramification-depth theorem.

---

# 2. Covering tournament arcs by partial orders

A **poset contained in \(T\)** means a strict partial order \(P\) on \(V(T)\) such that
\[
x<_P y\quad\Longrightarrow\quad x\to y\text{ in }T.
\]

Let \(p(T)\) be the least positive integer \(r\) for which there are posets
\(P_1,\ldots,P_r\) contained in \(T\) whose comparabilities cover all its arcs:
\[
x\to y\quad\Longrightarrow\quad
x<_{P_i}y\text{ for some }i.
\]
Empty relations are allowed.

## Lemma 2.1: A poset cover gives a polynomial bound

For every ordering \(\prec\) of a nonempty tournament \(T\),
\[
\chi(T^\prec)\le \omega(T^\prec)^{p(T)}.
\]
Consequently,
\[
\vec\chi(T)\le \vec\omega(T)^{p(T)}.
\]

### Proof

Let \(P_1,\ldots,P_r\) cover the arcs of \(T\), and put
\(k=\omega(T^\prec)\).

For each \(i\), define another strict partial order \(Q_i\) by
\[
x<_{Q_i}y
\quad\Longleftrightarrow\quad
x<_{P_i}y\ \text{ and }\ y\prec x.
\]
This is the intersection of two transitive relations, hence is transitive.

Every chain in \(Q_i\) is a clique in \(T^\prec\), so its length is at most \(k\). Let \(c_i(v)\in\{1,\ldots,k\}\) be the maximum length of a \(Q_i\)-chain ending at \(v\). Comparable vertices in \(Q_i\) receive different values.

Color \(v\) by the vector
\[
(c_1(v),\ldots,c_r(v)).
\]
If \(xy\) is a backedge, orient it as \(x\to y\) with \(y\prec x\). Some \(P_i\) contains \(x<_{P_i}y\), so \(x<_{Q_i}y\), and the two vectors differ. This is a proper coloring of \(T^\prec\) with at most \(k^r\) colors.

A stable set in a backedge graph induces a transitive tournament. Taking an ordering attaining \(\vec\omega(T)\) proves the last assertion. ∎

## Lemma 2.2: Poset covers are preserved under substitution

If
\[
T=S(H_v:v\in V(S)),
\]
then
\[
p(T)\le \max\left\{p(S),\max_v p(H_v)\right\}.
\]

### Proof

Pad all the covers with empty posets so that they have a common size \(r\). Write \(P^S_i\) for the \(i\)-th poset on the quotient and \(P^v_i\) for the \(i\)-th poset inside \(H_v\).

Define \(P_i\) on \(V(T)\) as follows:

* inside \(H_v\), use \(P^v_i\);
* for distinct modules \(H_u,H_v\), put every vertex of \(H_u\) below every vertex of \(H_v\) precisely when \(u<_{P^S_i}v\).

This is the lexicographic substitution of posets, and is a poset. Its comparabilities are arcs of \(T\).

Every internal arc is covered by an internal poset. Every arc between two modules is covered by a poset covering the corresponding quotient arc. Thus \(P_1,\ldots,P_r\) cover \(T\). ∎

## Lemma 2.3: Dichromatic colorings give small poset covers

If \(\vec\chi(S)\le q\), then
\[
p(S)\le 1+s(q).
\]

### Proof

Partition \(V(S)\) into transitive sets \(C_1,\ldots,C_q\), allowing empty sets. Put \(r=s(q)\), and assign distinct subsets
\[
L_1,\ldots,L_q\subseteq [r],
\qquad |L_j|=\lfloor r/2\rfloor.
\]

First define \(P_0\) as the disjoint union of the transitive orders on the \(C_j\). It covers all arcs within the color classes.

For each \(i\in[r]\), define \(P_i\) by
\[
x<_{P_i}y
\]
exactly when \(x\to y\), with \(x\in C_a\), \(y\in C_b\), and
\[
i\in L_a\setminus L_b.
\]
This relation has no chain of length three: a middle vertex would have to belong simultaneously to a label containing \(i\) and a label not containing \(i\). Hence \(P_i\) is a strict partial order.

If \(a\ne b\), the distinct equal-sized labels satisfy
\(L_a\setminus L_b\ne\varnothing\). Therefore every arc from \(C_a\) to \(C_b\) is covered by some \(P_i\). Together with \(P_0\), these posets cover all arcs. ∎

---

# 3. Proof of the quasipolynomial bound

Fix a substitution expression for \(T\), and put \(w=\vec\omega(T)\).

Every quotient appearing in the expression is isomorphic to an induced subtournament of \(T\): choose one representative from each of its nonempty child modules. Directed clique number is induced-subtournament monotone, so every such quotient \(S\) satisfies
\[
\vec\omega(S)\le w.
\]
Consequently,
\[
\vec\chi(S)\le f(w)\le q,
\qquad q=\lceil f(w)\rceil.
\]

By Lemma 2.3, every quotient has a poset cover of size at most \(1+s(q)\). Repeated application of Lemma 2.2 therefore gives
\[
p(T)\le 1+s(q).
\]
Lemma 2.1 now proves
\[
\vec\chi(T)\le w^{1+s(q)},
\]
as claimed.

For clarity, an entirely elementary explicit estimate is
\[
s(q)\le 2\lceil\log_2 q\rceil.
\]
Indeed, \(q\) distinct binary strings of length \(\lceil\log_2q\rceil\) can be encoded as equal-sized subsets by choosing one element from each of that many disjoint pairs. Thus
\[
\vec\chi(T)
\le
w^{\,1+2\lceil\log_2\lceil f(w)\rceil\rceil}.
\]
If \(f\) is polynomial, the exponent is \(O(\log w)\), not a constant.

This proves Theorem 1 and its bounded-dichromatic-generator corollary.

---

# 4. A quadratic bound for cyclic substitution

Let
\[
\mathcal C=\{TT_1,TT_2,\overrightarrow C_3\}^{\mathrm{subst}}.
\]
The preceding argument already gives a cubic bound for \(\mathcal C\), because its generators have dichromatic number at most two. The following argument improves this to quadratic.

We use \(\vec\chi(\varnothing)=\omega(\varnothing)=0\) when restricting to subsets.

## 4.1. Weighted coloring of a directed triangle

For
\[
T=\overrightarrow C_3(A,B,C),
\qquad A\to B\to C\to A,
\]
put \(a=\vec\chi(A)\), \(b=\vec\chi(B)\), and \(c=\vec\chi(C)\). Then
\[
\vec\chi(T)
=
\max\left\{
a,b,c,\left\lceil\frac{a+b+c}{2}\right\rceil
\right\}. \tag{4}
\]

For the lower bound, a transitive color class meets at most two of the three modules, while the modules require at least \(a+b+c\) module-color incidences.

For the upper bound, let the right-hand side be \(k\). Choose subsets
\(I_A,I_B,I_C\subseteq[k]\) of sizes \(a,b,c\) with empty triple intersection. Such subsets exist because each size is at most \(k\) and their sum is at most \(2k\): equivalently, choose complements of sizes \(k-a,k-b,k-c\) whose union is \([k]\). One explicit construction lays these complements consecutively around a cyclic list of the \(k\) colors.

Assign the local transitive color classes in each module bijectively to its assigned colors. Each global color meets at most two modules, and its union is transitive. This proves (4), including cases with empty modules.

## 4.2. A poset associated with the substitution expression

For a fixed expression representing \(T\in\mathcal C\), construct a poset \(P_T\) recursively.

* At a singleton, use the empty relation.
* At a transitive composition \(A\to B\), put all of \(P_A\) below all of \(P_B\).
* At a cyclic composition \(A\to B\to C\to A\), use
  \[
  P_T=(P_A\oplus P_B)\ \sqcup\ P_C.
  \]
  Thus all vertices of \(A\) are below all vertices of \(B\), and there are no comparabilities between \(C\) and \(A\cup B\).

Every comparability of \(P_T\) is an arc of \(T\).

The key property is stronger than what is needed merely to define this poset.

**Lemma 4.1.**  
For every \(U\subseteq V(T)\), if an ordering \(\prec\) of \(U\) is a linear extension of \(P_T[U]\), then
\[
\vec\chi(T[U])\le \omega(T[U]^\prec). \tag{5}
\]

### Proof

Induct on the substitution expression. Singletons and empty sets are immediate. At a transitive composition, the dichromatic number is the maximum of the child dichromatic numbers, so induction applies.

Consider a cyclic node, and use \(A,B,C\) for the three child vertex sets after intersection with \(U\). Set
\[
G=T[U]^\prec,\qquad w=\omega(G).
\]
Since \(\prec\) extends \(P_T[U]\), every vertex of \(A\) precedes every vertex of \(B\).

Choose a cut of the order after all of \(A\) and before all of \(B\). Such a cut also exists when either set is empty. Let \(C_L,C_R\) be the vertices of \(C\) before and after the cut. Put
\[
a=\omega(G[A]),\quad b=\omega(G[B]),\quad
c_L=\omega(G[C_L]),\quad c_R=\omega(G[C_R]).
\]

Every vertex of \(C_L\) precedes every vertex of \(B\), and \(B\to C_L\). Therefore these two sets are completely joined in \(G\), giving
\[
b+c_L\le w.
\]
Similarly, \(A\) and \(C_R\) are completely joined in \(G\), so
\[
a+c_R\le w. \tag{6}
\]

Write
\[
d_A=\vec\chi(T[A]),\quad d_B=\vec\chi(T[B]),\quad
d_C=\vec\chi(T[C]).
\]
Induction gives
\[
d_A\le a,\qquad d_B\le b,\qquad
d_C\le c_L+c_R.
\]
Hence, by (6),
\[
d_A+d_B+d_C\le 2w.
\]
Applying induction to each entire child also gives
\[
d_A,d_B,d_C\le w.
\]
Formula (4) now yields \(\vec\chi(T[U])\le w\). ∎

## 4.3. Removing the linear-extension assumption

Take any ordering \(\prec\) of \(V(T)\), and put \(w=\omega(T^\prec)\). Define
\[
x<_Q y
\quad\Longleftrightarrow\quad
x<_{P_T}y\ \text{ and }\ y\prec x.
\]
As in Lemma 2.1, \(Q\) has height at most \(w\).

Partition \(V(T)\) into at most \(w\) antichains \(U_1,\ldots,U_w\) of \(Q\), using longest-chain ranks. On each \(U_i\), the order \(\prec\) is a linear extension of \(P_T[U_i]\): a violated comparability would be a comparability of \(Q\).

Lemma 4.1 gives
\[
\vec\chi(T[U_i])
\le \omega(T[U_i]^\prec)
\le w.
\]
Using disjoint palettes for the \(U_i\),
\[
\vec\chi(T)\le w^2.
\]
Finally minimize over \(\prec\). This proves (3).

---

# 5. Consequence for the balanced cyclic test family

Define, as in the previous attempt,
\[
R_0=TT_1,\qquad
R_{n+1}=\overrightarrow C_3(R_n,R_n,R_n).
\]
Formula (4) independently verifies
\[
d_0=1,\qquad
d_{n+1}=\left\lceil\frac{3d_n}{2}\right\rceil,
\qquad d_n=\vec\chi(R_n).
\]
In particular,
\[
d_n\ge (3/2)^n.
\]

The quadratic theorem therefore implies
\[
\boxed{\qquad
\vec\omega(R_n)\ge \sqrt{d_n}
\ge (3/2)^{n/2}.
\qquad} \tag{7}
\]

Thus the balanced cyclic family cannot have the subexponential directed clique growth suggested as a possible counterexample route in the previous attempt. More generally, the entire transitive/triangle-generated substitution class has a quadratic binding function, not merely the balanced examples.

---

# 6. What remains unresolved

The general estimate is
\[
\vec\chi(T)
\le
w^{\,1+s(\lceil f(w)\rceil)}.
\]
For a nonconstant polynomial \(f\), its exponent can grow proportionally to \(\log w\). Consequently, this argument does **not** yield a polynomial binding function for arbitrary polynomially bounded generators.

The unresolved step is to remove that growing exponent—or to construct a class where such a loss is genuinely necessary. Neither is established here.

The progress is therefore:

1. a quasipolynomial bound for the full substitution closure;
2. polynomial preservation for all bounded-dichromatic generator classes;
3. a quadratic bound for the cyclic substitution class highlighted in the supplied context.

The original polynomial-preservation question remains open in this writeup.