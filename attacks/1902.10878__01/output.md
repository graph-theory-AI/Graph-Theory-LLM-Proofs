```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "An explicit family gives ψ(2/7,5/7) ≤ 23/28 < 6/7 = ψ(5/7,2/7).",
  "would_publish": true,
  "caveats": "The exact value of ψ(2/7,5/7) is not determined, and the separate exact-degree symmetry question remains open."
}
```

# Mathematical writeup

## 1. Definitions

For an \((x,y)\)-biconstrained triple \((G,A,B,C)\), the relevant degree conditions are

\[
\begin{aligned}
|N_B(a)|&\ge x|B| &&(a\in A),\\
|N_A(b)|&\ge x|A| &&(b\in B),\\
|N_C(b)|&\ge y|C| &&(b\in B),\\
|N_B(c)|&\ge y|B| &&(c\in C).
\end{aligned}
\]

For \(c\in C\), put

\[
R(c)=\{a\in A:N_B(a)\cap N_B(c)\neq\varnothing\}.
\]

Thus, equivalently,

\[
\psi(x,y)=
\inf_{(G,A,B,C)\ \text{\((x,y)\)-biconstrained}}
\max_{c\in C}\frac{|R(c)|}{|A|}.
\]

We prove the following stronger statement.

### Theorem

For every odd integer \(q\ge 7\),

\[
\psi\left(\frac2q,\frac{q-2}{q}\right)
\le
1-\frac{2(q-2)}{q(q+1)}
<
1-\frac1q
=
\psi\left(\frac{q-2}{q},\frac2q\right).
\]

Taking \(q=7\) gives

\[
\psi(2/7,5/7)\le \frac{23}{28}
<
\frac67
=
\psi(5/7,2/7).
\]

This disproves the proposed symmetry.

---

## 2. The reverse value

We first prove a general lemma.

### Lemma

If \(q\ge3\) is odd, then

\[
\psi\left(\frac{q-2}{q},\frac2q\right)=1-\frac1q.
\]

### Lower bound

Let \((G,A,B,C)\) be \(((q-2)/q,2/q)\)-biconstrained. Suppose, for a contradiction, that

\[
|R(c)|<\frac{q-1}{q}|A|
\qquad\text{for every }c\in C.
\]

Every \(c\) therefore has more than \(|A|/q\) vertices of \(A\) not reachable from it. If \(a\notin R(c)\), then \(N_B(a)\) and \(N_B(c)\) are disjoint. Consequently,

\[
|B|
\ge |N_B(a)|+|N_B(c)|
\ge \frac{q-2}{q}|B|+\frac2q|B|
=|B|.
\]

Equality holds throughout. In particular,

\[
|N_B(a)|=\frac{q-2}{q}|B|,
\qquad
|N_B(c)|=\frac2q|B|,
\qquad
N_B(a)=B\setminus N_B(c).
\tag{1}
\]

Since every \(c\) has a nonreachable \(a\), every \(c\) has exactly \(2|B|/q\) neighbors in \(B\). Hence

\[
e(B,C)=\frac2q|B||C|.
\]

On the other hand, every \(b\in B\) has at least \(2|C|/q\) neighbors in \(C\). Equality in the total edge count therefore implies

\[
|N_C(b)|=\frac2q|C|
\qquad\text{for every }b\in B.
\tag{2}
\]

Let \(S_1,\ldots,S_m\) be the distinct neighborhoods in \(B\) occurring among vertices of \(C\), and define

\[
C_i=\{c\in C:N_B(c)=S_i\},
\qquad
\beta_i=\frac{|C_i|}{|C|}.
\]

Thus \(\beta_i>0\) and \(\sum_i\beta_i=1\). Define also

\[
A_i=\{a\in A:N_B(a)=B\setminus S_i\},
\qquad
\alpha_i=\frac{|A_i|}{|A|}.
\]

By (1), for \(c\in C_i\), the vertices not reachable from \(c\) are exactly the vertices of \(A_i\). Our assumption therefore gives

\[
\alpha_i>\frac1q
\qquad (1\le i\le m).
\tag{3}
\]

For \(b\in B\), set

\[
I(b)=\{i:b\in S_i\}.
\]

Equation (2) gives

\[
\sum_{i\in I(b)}\beta_i=\frac2q.
\tag{4}
\]

In particular, \(I(b)\neq\varnothing\).

If \(i\in I(b)\), then every vertex of \(A_i\) is nonadjacent to \(b\). Since \(b\) has at least \((q-2)|A|/q\) neighbors in \(A\), it has at most \(2|A|/q\) nonneighbors. Hence

\[
\sum_{i\in I(b)}\alpha_i\le\frac2q.
\tag{5}
\]

By (3), two terms in this sum would already have sum strictly greater than \(2/q\). Thus \(|I(b)|=1\) for every \(b\). From (4), if \(I(b)=\{i\}\), then

\[
\beta_i=\frac2q.
\]

Every \(S_i\) is nonempty, so every index \(i\) occurs as \(I(b)=\{i\}\) for some \(b\). Therefore all \(\beta_i=2/q\), and hence

\[
1=\sum_{i=1}^m\beta_i=\frac{2m}{q}.
\]

This is impossible because \(q\) is odd. Thus some \(c\in C\) satisfies

\[
|R(c)|\ge\frac{q-1}{q}|A|,
\]

proving

\[
\psi\left(\frac{q-2}{q},\frac2q\right)\ge1-\frac1q.
\]

### Upper bound

Let \(A=\{a_i:i\in\mathbb Z_q\}\), \(B=\{b_i:i\in\mathbb Z_q\}\), and \(C=\{c_i:i\in\mathbb Z_q\}\). Put

\[
S_i=\{b_i,b_{i+1}\}.
\]

Define

\[
N_B(a_i)=B\setminus S_i,
\qquad
N_B(c_i)=S_i.
\]

Every \(a_i\) has \(q-2\) neighbors in \(B\), and every \(b\) has \(q-2\) neighbors in \(A\). Every \(c_i\) has two neighbors in \(B\), and every \(b\) has two neighbors in \(C\). Thus this is \(((q-2)/q,2/q)\)-biconstrained.

The vertex \(c_i\) does not reach \(a_i\). If \(j\ne i\), then the distinct two-element sets \(S_i,S_j\) satisfy \(S_i\setminus S_j\neq\varnothing\), so \(c_i\) and \(a_j\) have a common neighbor in \(B\). Hence \(c_i\) reaches exactly \(q-1\) vertices of \(A\). Therefore

\[
\psi\left(\frac{q-2}{q},\frac2q\right)\le1-\frac1q.
\]

This proves the lemma.

---

## 3. An asymmetric construction in the other direction

Let \(q\ge7\) be odd and put

\[
h=\frac{q-3}{2},
\qquad
m=h+3=\frac{q+3}{2}.
\]

Let \(B\) consist of \(h\) disjoint pairs

\[
P_1,\ldots,P_h
\]

and three additional vertices \(r_{12},r_{13},r_{23}\). Thus \(|B|=2h+3=q\).

Define \(m\) distinct two-element subsets of \(B\):

\[
S_i=P_i \quad (1\le i\le h),
\]

and

\[
\begin{aligned}
S_{h+1}&=\{r_{12},r_{13}\},\\
S_{h+2}&=\{r_{12},r_{23}\},\\
S_{h+3}&=\{r_{13},r_{23}\}.
\end{aligned}
\]

### The set \(A\)

For each \(i\in\{1,\ldots,m\}\), take a set \(A_i\) of \(q-2\) vertices, each with neighborhood exactly \(S_i\) in \(B\). Add three further vertices \(U\), each complete to \(B\).

Thus

\[
|A|=m(q-2)+3
=\frac{q(q+1)}2.
\]

Every vertex in \(A_i\) has two neighbors in \(B\), and hence has exactly \((2/q)|B|\) neighbors. The three universal vertices have more.

A vertex of a pair \(P_i\) is adjacent to the \(q-2\) vertices of \(A_i\) and to the three universal vertices, giving

\[
q-2+3=q+1=\frac2q|A|
\]

neighbors in \(A\). Each of \(r_{12},r_{13},r_{23}\) belongs to two of the final three sets \(S_i\), and hence has

\[
2(q-2)+3=2q-1\ge q+1
\]

neighbors in \(A\). Thus the \(A\)-\(B\) pair is \(2/q\)-biconstrained.

### The set \(C\)

For each \(1\le i\le h\), take two vertices of type \(i\); for each of \(i=h+1,h+2,h+3\), take one vertex of type \(i\). A type-\(i\) vertex \(c\) has

\[
N_B(c)=B\setminus S_i.
\]

There are \(2h+3=q\) vertices in \(C\). Every \(c\) has \(q-2\) neighbors in \(B\).

A vertex in \(P_i\) is omitted precisely by the two \(C\)-vertices of type \(i\), and so has \(q-2\) neighbors in \(C\). Each \(r_{jk}\) lies in two of the final sets \(S_i\), whose types each occur once, so it too is omitted by exactly two vertices of \(C\). Thus every \(b\in B\) has \(q-2\) neighbors in \(C\).

The resulting triple is therefore

\[
\left(\frac2q,\frac{q-2}{q}\right)\text{-biconstrained}.
\]

### Its second neighborhoods

Let \(c\) have type \(i\). Its \(B\)-neighborhood is \(B\setminus S_i\).

It has no two-edge path to any vertex of \(A_i\), because vertices of \(A_i\) have neighborhood \(S_i\). If \(j\ne i\), then \(S_j\) and \(S_i\) are distinct two-element sets, so

\[
S_j\setminus S_i\neq\varnothing.
\]

Thus every vertex of \(A_j\) has a common \(B\)-neighbor with \(c\). The three universal vertices are also reached. Consequently, precisely the \(q-2\) vertices of \(A_i\) are not reached by \(c\). Hence every \(c\in C\) reaches the proportion

\[
1-\frac{q-2}{q(q+1)/2}
=
1-\frac{2(q-2)}{q(q+1)}
\]

of \(A\). Therefore

\[
\psi\left(\frac2q,\frac{q-2}{q}\right)
\le
1-\frac{2(q-2)}{q(q+1)}.
\]

For \(q>5\),

\[
\frac{2(q-2)}{q(q+1)}-\frac1q
=
\frac{q-5}{q(q+1)}>0,
\]

so

\[
1-\frac{2(q-2)}{q(q+1)}
<
1-\frac1q.
\]

Combining this with the lemma proves the theorem.

---

## 4. Smallest displayed instance

For \(q=7\), take

\[
\begin{aligned}
S_1&=\{1,2\},&
S_2&=\{3,4\},\\
S_3&=\{5,6\},&
S_4&=\{5,7\},&
S_5&=\{6,7\}.
\end{aligned}
\]

There are five \(A\)-vertices of each type \(S_i\), together with three vertices complete to \(B\), for \(|A|=28\). There are two \(C\)-vertices of types \(1,2\), and one of each of types \(3,4,5\), for \(|C|=7\); a type-\(i\) vertex has neighborhood \(B\setminus S_i\).

Every \(C\)-vertex misses exactly five of the 28 vertices in \(A\), so

\[
\psi(2/7,5/7)\le\frac{23}{28}.
\]

The lemma gives

\[
\psi(5/7,2/7)=\frac67=\frac{24}{28}.
\]

Thus

\[
\boxed{\psi(2/7,5/7)<\psi(5/7,2/7)}.
\]

## Gaps and scope

There is no remaining gap in the counterexample under the standard definition of a biconstrained triple. The construction uses vertices of \(A\) complete to \(B\), so it does not address the paper’s separate exact-degree symmetry question.