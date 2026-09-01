```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The prime-order asymptotics remain open, but the threshold genuinely depends on group structure: for example, T((Z/2Z)^3)=2 whereas T(Z/8Z)>=3.",
  "would_publish": false,
  "caveats": "This uses the usual convention that T(G) is the largest size up to which every subset is realizable; no global improvement for T(p) is obtained."
}
```

# 1. Definitions and results

Call \(C\subseteq G\) **realizable** if there is \(W\subseteq G\) such that

\[
C+W=G
\]

and \(C\) is minimal with this property. Equivalently, for every \(c\in C\) there is a private point

\[
x_c\in (c+W)\setminus ((C\setminus\{c\})+W).
\]

I use the standard threshold convention

\[
T(G)=\max\{t:\text{every nonempty }C\subseteq G,\ |C|\le t,\text{ is realizable}\}.
\]

If the source instead defines the least size of a nonrealizable set, all numerical threshold statements below shift by one.

The main partial conclusions are:

1. \(T(G)\) is not determined by \(|G|\):
   \[
   T((\mathbb Z/2\mathbb Z)^3)=2,
   \qquad
   T(\mathbb Z/8\mathbb Z)\ge 3.
   \]
2. There is an exact criterion for the realizability of a punctured subgroup \(H\setminus\{0\}\).
3. If \(G=A\oplus B\) with \(A,B\neq 0\), then
   \[
   T(G)\le |A|+|B|-2.
   \]
4. For \(G=\mathbb Z/p\mathbb Z\), every \(C\) satisfying
   \[
   |C-C|=2|C|-1<p
   \]
   is realizable. In particular, every arithmetic progression of length at most \((p-1)/2\) is realizable.

None of these gives a new global asymptotic upper or lower bound for \(T(p)\).

# 2. Every two-element set is realizable

## Lemma 2.1

Every one- or two-element subset of a finite abelian group is realizable.

### Proof

Singletons are immediate. Let \(C=\{0,d\}\), where \(d\neq 0\), and put \(H=\langle d\rangle\).

Choose \(S\subseteq H\) as follows:

- if \(|H|=2\), take \(S=\{0\}\);
- if \(|H|\ge 3\), take \(S=H\setminus\{0\}\).

Then

\[
S\cup(d+S)=H,
\qquad S\neq d+S.
\]

Let \(R\) be a transversal for \(G/H\), and set \(W=S+R\). Consequently,

\[
W\cup(d+W)=G,
\]

and the two sets \(W,d+W\), having equal cardinality but being unequal, each have a point outside the other. Thus both \(0\) and \(d\) have private points. Translation handles an arbitrary two-element \(C\). \(\square\)

# 3. An exact punctured-subgroup criterion

Let

\[
H[2]=\{h\in H:2h=0\},
\]

and let

\[
\nu(H)=\#\big((H\setminus\{0\})/{\sim}\big),
\qquad h\sim -h.
\]

By Burnside's lemma,

\[
\nu(H)=\frac{|H|+|H[2]|-2}{2}.
\]

## Theorem 3.1

Let \(H\le G\), with \(|H|\ge2\), and put \(C=H\setminus\{0\}\). Then \(C\) is realizable in \(G\) if and only if

\[
[G:H]\ge \nu(H).
\]

### Proof

Write \(q=[G:H]\), choose coset representatives \(r_1,\dots,r_q\), and decompose any proposed \(W\subseteq G\) into fibers

\[
A_i=(W\cap(r_i+H))-r_i\subseteq H.
\]

Since \(C\subseteq H\),

\[
(C+W)\cap(r_i+H)=r_i+(C+A_i).
\]

For \(C=H\setminus\{0\}\), one has

\[
C+A_i=H \quad\Longleftrightarrow\quad |A_i|\ge2.
\]

Indeed, a singleton \(A_i=\{a\}\) misses \(a\), while if \(A_i\) contains two distinct elements, then for every \(y\in H\) one can choose \(a\in A_i\) with \(a\ne y\), giving \(y=(y-a)+a\) with \(y-a\in C\).

Now fix \(c\in C\). Suppose \(c\) has a private point \(r_i+y\) in the \(i\)-th coset. This is equivalent to

\[
A_i\cap(y-C)=\{y-c\}.
\]

But

\[
y-C=H\setminus\{y\}.
\]

As coverage requires \(|A_i|\ge2\), the displayed equality forces

\[
A_i=\{y,y-c\}.
\]

Thus only a two-element fiber can provide private points. If \(A_i=\{u,v\}\), then the elements of \(C\) that can have private points in this fiber are exactly

\[
\{\pm(u-v)\};
\]

this is a singleton when \(u-v\) has order two.

It follows that each quotient coset can account for at most one orbit of the involution \(c\mapsto-c\). Hence all elements of \(C\) can be essential only if

\[
q\ge\nu(H).
\]

Conversely, if \(q\ge\nu(H)\), assign one quotient coset to each orbit \(\{\pm d\}\), and in that coset take the fiber \(\{0,d\}\). Any remaining fibers may be arbitrary two-element subsets of \(H\). Every fiber covers its \(H\)-coset, and the fiber \(\{0,d\}\) gives private points to both \(d\) and \(-d\). Therefore \(C\) is realizable. \(\square\)

## Corollary 3.2

If

\[
[G:H]<\frac{|H|+|H[2]|-2}{2},
\]

then

\[
T(G)\le |H|-2.
\]

For an elementary abelian \(2\)-group \(H\), this condition becomes

\[
[G:H]<|H|-1.
\]

This gives an exact version of one subgroup-based obstruction.

# 4. Structure dependence at order eight

## Proposition 4.1

\[
T((\mathbb Z/2\mathbb Z)^3)=2.
\]

The same is true for \(\mathbb Z/4\mathbb Z\oplus\mathbb Z/2\mathbb Z\).

### Proof

In \(G=(\mathbb Z/2\mathbb Z)^3\), let \(H\) be a two-dimensional subspace. Then

\[
|H|=4,\qquad [G:H]=2,\qquad \nu(H)=3.
\]

By Theorem 3.1, the three-element set

\[
C=H\setminus\{0\}
\]

is not realizable. Lemma 2.1 shows that every set of size at most two is realizable, so \(T(G)=2\).

The group \(\mathbb Z/4\mathbb Z\oplus\mathbb Z/2\mathbb Z\) also contains a subgroup \(H\cong(\mathbb Z/2\mathbb Z)^2\) of index two, and the same argument applies. \(\square\)

## Proposition 4.2

Every three-element subset of \(\mathbb Z/8\mathbb Z\) is realizable. Consequently,

\[
T(\mathbb Z/8\mathbb Z)\ge3.
\]

### Proof

Translation and the automorphism \(x\mapsto-x\) preserve realizability. A three-element subset of the cyclically ordered group \(\mathbb Z/8\mathbb Z\) is classified under these operations by its three positive circular gaps. Up to permutation, the possibilities are

\[
(1,1,6),\ (1,2,5),\ (1,3,4),\ (2,2,4),\ (2,3,3).
\]

Thus it suffices to treat the five representatives in the table below. The last column gives, in the same order as the elements of \(C\), one private point for each \(c\).

\[
\begin{array}{c|c|c|c}
C&W&\{c+W:c\in C\}&\text{private points}\\ \hline
\{0,1,2\}&\{0,3,6\}
 &\{0,3,6\},\{1,4,7\},\{2,5,0\}
 &(3,1,2)\\
\{0,1,3\}&\{0,2,4,5\}
 &\{0,2,4,5\},\{1,3,5,6\},\{3,5,7,0\}
 &(2,1,7)\\
\{0,1,4\}&\{0,2,4,7\}
 &\{0,2,4,7\},\{1,3,5,0\},\{4,6,0,3\}
 &(2,1,6)\\
\{0,2,4\}&\{0,1,5,6\}
 &\{0,1,5,6\},\{2,3,7,0\},\{4,5,1,2\}
 &(6,3,4)\\
\{0,2,5\}&\{0,1,4,7\}
 &\{0,1,4,7\},\{2,3,6,1\},\{5,6,1,4\}
 &(7,2,5)
\end{array}
\]

In every row the three translates cover all eight residues, and the listed point for each \(c\) lies in \(c+W\) but in neither of the other two translates. Hence all five representatives are realizable. \(\square\)

Combining Propositions 4.1 and 4.2 gives

\[
T((\mathbb Z/2\mathbb Z)^3)
<
T(\mathbb Z/8\mathbb Z).
\]

Thus the value of \(T(G)\), not merely the currently available upper-bound construction, genuinely depends on the group structure beyond \(|G|\).

# 5. A direct-product obstruction

## Proposition 5.1

Let \(G=A\oplus B\), where \(|A|,|B|\ge2\), and let

\[
C=(A\times\{0\})\cup(\{0\}\times B).
\]

Then \(C\) is not realizable. Consequently,

\[
T(A\oplus B)\le |A|+|B|-2.
\]

### Proof

Regard \(A\times\{b\}\) as a row and \(\{a\}\times B\) as a column. For \(W\subseteq G\),

- \((A\times\{0\})+W\) fills every row that meets \(W\);
- \((\{0\}\times B)+W\) fills every column that meets \(W\).

If there were both an empty row and an empty column, their intersection would not lie in \(C+W\). Thus coverage forces either every row or every column to meet \(W\).

Suppose every column meets \(W\). Fix nonzero \(a\in A\). For any

\[
x=(a,0)+w,\qquad w=(u,v)\in W,
\]

the column with first coordinate \(a+u\) contains some \(w'=(a+u,v')\in W\). Therefore

\[
x=(0,v-v')+w',
\]

a representation using an element of the vertical axis distinct from \((a,0)\). Hence \((a,0)\) has no private point.

If not every column meets \(W\), then every row must meet \(W\), and the symmetric argument shows that every nonzero element of the vertical axis has no private point. Thus \(C\) cannot be minimal. \(\square\)

This gives the familiar \(O(\sqrt{|G|})\) obstruction when \(G\) has two direct factors of comparable orders. It is unavailable for \(\mathbb Z/p\mathbb Z\).

# 6. A prime-order positive result

The following criterion gives a substantial class of large realizable subsets in prime cyclic groups.

## Lemma 6.1

Let \(C\subseteq G\), put \(D=C-C\), and define

\[
U=\{x\in G:x-C\subseteq D\}.
\]

If \(U=C\), then \(C\) is realizable.

### Proof

Take

\[
W=\{0\}\cup(G\setminus D).
\]

For \(x\in C\), the representation \(x=x+0\) covers \(x\). If \(x\notin C=U\), there is some \(c\in C\) with \(x-c\notin D\), so \(x=c+(x-c)\in C+W\). Thus \(C+W=G\).

Moreover, every \(c\in C\) is private at the point \(c\). Indeed, if

\[
c=c'+w,\qquad c'\in C,\quad w\in W,
\]

then \(w=c-c'\in D\). Since \(W\cap D=\{0\}\), one has \(w=0\) and \(c'=c\). \(\square\)

## Proposition 6.2

Let \(C\subseteq\mathbb Z/p\mathbb Z\), \(k=|C|\), and suppose

\[
|C-C|=2k-1<p.
\]

Then \(C\) is realizable.

### Proof

With \(D,U\) as above, one has \(C\subseteq U\) and

\[
U-C\subseteq D.
\]

By Cauchy–Davenport,

\[
|U-C|\ge \min(p,|U|+k-1).
\]

Since \(|D|<p\), this gives

\[
|U|+k-1\le |D|=2k-1,
\]

hence \(|U|\le k\). As \(C\subseteq U\) and \(|C|=k\), it follows that \(U=C\). Lemma 6.1 applies. \(\square\)

More generally, if \(|C-C|<p\), the same argument yields

\[
|U\setminus C|
\le |C-C|-(2|C|-1).
\]

Thus the explicit \(W\) in Lemma 6.1 fails to cover at most the difference-set excess beyond the Cauchy–Davenport minimum.

## Corollary 6.3

Every arithmetic progression in \(\mathbb Z/p\mathbb Z\) of length at most \((p-1)/2\) is realizable.

Indeed, such a progression has \(|C-C|=2|C|-1<p\).

This excludes arithmetic progressions and, more generally, all extremal small-difference sets from serving as prime-order upper-bound examples. It does not control arbitrary \(C\), whose difference set may be much larger.

# 7. Exact finite verification as SAT

For a fixed \(C\subseteq G\), realizability has the following exact SAT formulation.

Use Boolean variables \(w_g\), \(g\in G\), and witness variables \(y_{c,x}\), \(c\in C,x\in G\). Add:

- coverage clauses
  \[
  \bigvee_{c\in C} w_{x-c}
  \qquad(x\in G);
  \]
- one witness for every \(c\):
  \[
  \bigvee_{x\in G} y_{c,x};
  \]
- witness implications
  \[
  y_{c,x}\Longrightarrow w_{x-c},
  \]
  \[
  y_{c,x}\Longrightarrow \neg w_{x-c'}
  \qquad(c'\in C\setminus\{c\}).
  \]

The formula is satisfiable exactly when \(C\) is realizable. Thus \(T(G)\) can be found by testing subsets in increasing cardinality, preferably modulo translations and automorphisms.

A useful search bound is

\[
\left\lceil\frac{|G|}{|C|}\right\rceil
\le |W|
\le |G|-|C|+1.
\]

The lower bound follows from coverage. For the upper bound, choose one private point \(x_c\) for each \(c\). These points are distinct, and \(c+W\) contains none of the other \(|C|-1\) private points.

# 8. Remaining gap

The order-eight example conclusively answers the qualitative structural part: \(T(G)\) is not a function of \(|G|\) alone.

The prime-order asymptotic question remains open. The arguments above establish only special realizable classes and do not improve either the universal lower bound from the source or the supplied \(O(p^{3/4+\varepsilon})\) upper bound. In particular, they do not determine whether \(T(p)\) has a different exponent from values attained at suitably composite orders.