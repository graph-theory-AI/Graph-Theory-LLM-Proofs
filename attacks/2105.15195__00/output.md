```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured value is proved for all colorings that are constant on sufficiently wide consecutive intervals, with arbitrary block order and scales, but not for general interlaced colorings.",
  "would_publish": false,
  "caveats": "The source denominator is 2r b_0-r, not 2^r b_0-r; the unrestricted reduction to interval-block colorings remains open."
}
```

## 1. Statement and correction of the constant

For \(A\subseteq \mathbb N\), write
\[
\Sigma(A)=\left\{\sum_{a\in F}a:\varnothing\ne F\subseteq A,\ |F|<\infty\right\},
\]
and
\[
\overline d_{\log}(S)
 =\limsup_{x\to\infty}\frac1{\log x}
   \sum_{\substack{n\le x\\n\in S}}\frac1n.
\]
Thus
\[
c_r=\inf_{\mathbb N=A_1\sqcup\cdots\sqcup A_r}
       \max_{1\le i\le r}\overline d_{\log}\bigl(\Sigma(A_i)\bigr).
\]

There is a transcription error in the catalog formula. The intended constant is
\[
C_r=
\left(1-\frac1{2b_0}\right)
\left(1+\frac1{2rb_0-r}\right),
\tag{1}
\]
not with denominator \(2^rb_0-r\), where \(b_0>1\) is the unique root of
\[
b^r-2rb+r-1=0.
\tag{2}
\]
Indeed, (2) gives
\[
b_0^r-1=2rb_0-r,
\]
and hence
\[
C_r
 =\frac{1-\frac1{2b_0}}{1-b_0^{-r}}
 =\frac{b_0^{r-1}}{2r}.
\tag{3}
\]
For \(r=2\), the expressions \(2r\) and \(2^r\) coincide, which hides the transcription error.

The conjecture is \(c_r=C_r\). The known construction proves \(c_r\le C_r\). Below I prove the reverse inequality for a broad class of interval-block colorings.

---

## 2. A geometric dilation theorem

For \(\lambda>1\), define
\[
D_{r,\lambda}(q)
 =\frac{1-\frac1{\lambda q}}{1-q^{-r}},
 \qquad q>1,
\]
and
\[
C_{r,\lambda}=\inf_{q>1}D_{r,\lambda}(q).
\tag{4}
\]

### Theorem 2.1

Let
\[
0<t_0<t_1<t_2<\cdots,\qquad t_k\longrightarrow\infty,
\]
and give every index \(k\) a label \(\gamma_k\in[r]\). Put
\[
J_k=[t_k,\lambda t_{k+1}]
\quad\text{and}\quad
U_i=\bigcup_{\gamma_k=i}J_k.
\]
Then
\[
\max_{1\le i\le r}
\limsup_{T\to\infty}\frac{|U_i\cap[0,T]|}{T}
\ge C_{r,\lambda}.
\tag{5}
\]

Here \(|\cdot|\) denotes Lebesgue measure. No periodicity or regularity of the sequence \((t_k)\) or of the color word \((\gamma_k)\) is assumed.

### Proof

Colors occurring only finitely often may be deleted. Suppose \(s\le r\) colors occur infinitely often. Since
\[
C_{s,\lambda}\ge C_{r,\lambda},
\]
it suffices to prove (5) with \(s\) in place of \(r\).

Assume for contradiction that every \(U_i\) has upper density strictly less than \(C_{s,\lambda}\). Choose
\[
\max_i\overline\delta(U_i)<D<C_{s,\lambda},
\qquad
\overline\delta(U)=\limsup_{T\to\infty}\frac{|U\cap[0,T]|}{T}.
\tag{6}
\]
Consequently, for all sufficiently large \(T\),
\[
|U_i\cap[0,T]|\le DT
\quad\text{for every active color }i.
\tag{7}
\]

Fix a color \(i\), and decompose \(U_i\) into connected components. Because both the left and right endpoints of the intervals \(J_k\) increase with \(k\), a component \(C\) has the form
\[
C=[t_f,\lambda t_{\ell+1}]
\]
for suitable first and last indices \(f\le \ell\) of intervals in that component. Define
\[
e_C=\lambda t_{\ell+1},\qquad
Q_C=\frac{t_{\ell+1}}{t_f},
\qquad
a_C=\frac{|C|}{e_C}
    =1-\frac1{\lambda Q_C}.
\tag{8}
\]

Let
\[
d_C=\frac{|U_i\cap[0,e_C]|}{e_C}.
\]
If \(C^-\) is the preceding component of the same color and
\[
R_C=\frac{e_C}{e_{C^-}},
\]
then disjointness of consecutive components gives the exact recurrence
\[
d_C=a_C+\frac{d_{C^-}}{R_C}.
\tag{9}
\]
For sufficiently late components, (7) gives \(d_C\le D\). From (9),
\[
1-\frac{a_C}{d_C}
 =\frac{d_{C^-}}{R_Cd_C},
\]
so
\[
\log\frac{d_{C^-}}{d_C}
 =\log R_C+\log\left(1-\frac{a_C}{d_C}\right)
 \le
 \log R_C+\log\left(1-\frac{a_C}{D}\right).
\tag{10}
\]

Consider
\[
F_{s,D}(Q)
 =s\log Q+
  \log\left(
    1-\frac{1-\frac1{\lambda Q}}{D}
  \right).
\tag{11}
\]
Whenever \(1-\frac1{\lambda Q}<D\),
\[
F_{s,D}(Q)\ge0
\]
is equivalent to
\[
D\ge
\frac{1-\frac1{\lambda Q}}{1-Q^{-s}}
=D_{s,\lambda}(Q).
\]
Since \(D<C_{s,\lambda}\), this is impossible. Moreover, \(a_C\le d_C\le D\) bounds \(Q_C\) in a compact interval. Hence there is some \(\eta>0\) such that every sufficiently late component satisfies
\[
\log\left(1-\frac{a_C}{D}\right)
 \le -s\log Q_C-\eta.
\tag{12}
\]

We now sum (10) over all sufficiently late components with block indices at most \(N\).

For each color, the left side telescopes:
\[
\sum_C\log\frac{d_{C^-}}{d_C}
 =\log\frac{d_{\mathrm{first}}}{d_{\mathrm{last}}}.
\]
Since
\[
d_C\ge a_C\ge 1-\frac1\lambda>0
\quad\text{and}\quad d_C\le D,
\]
the total left side is bounded independently of \(N\).

Similarly, for each color,
\[
\sum_C\log R_C
\le \log t_{N+1}+O(1),
\]
and hence, over the \(s\) active colors,
\[
\sum_C\log R_C
\le s\log t_{N+1}+O(1).
\tag{13}
\]

On the other hand,
\[
\log Q_C
 =\sum_{k=f(C)}^{\ell(C)}
   \log\frac{t_{k+1}}{t_k}.
\tag{14}
\]
Every block index belongs to some component of its own color, and its term
\(\log(t_{k+1}/t_k)\) occurs in the corresponding sum (14). Components meeting the two ends of the summation range contribute only \(O(1)\), because their \(Q_C\)'s are bounded. Therefore
\[
\sum_C\log Q_C
 \ge \log t_{N+1}-O(1).
\tag{15}
\]

Combining (12), (13), and (15), the total right side of (10) is at most
\[
s\log t_{N+1}
 -s\sum_C\log Q_C
 -\eta\,m_N+O(1)
\le O(1)-\eta\,m_N,
\tag{16}
\]
where \(m_N\) is the number of components being summed.

Every active color has infinitely many components. Indeed, if its intervals eventually formed a single unbounded component, then its union would contain a ray and have density \(1\), contrary to (6). Thus \(m_N\to\infty\), and (16) tends to \(-\infty\). This contradicts the bounded telescoping left side of (10). The theorem follows. ∎

---

## 3. Evaluation of the geometric constant

A differentiation gives
\[
D_{r,\lambda}'(q)=0
\quad\Longleftrightarrow\quad
q^r-\lambda rq+r-1=0.
\tag{17}
\]
For \(r\ge2\), this polynomial has a unique root
\[
b_{r,\lambda}>\lambda^{1/(r-1)}.
\]
It gives the unique minimum in (4). Since
\[
b_{r,\lambda}^r-1
 =r(\lambda b_{r,\lambda}-1),
\]
we obtain
\[
C_{r,\lambda}
 =D_{r,\lambda}(b_{r,\lambda})
 =\frac{b_{r,\lambda}^{\,r-1}}{\lambda r}.
\tag{18}
\]

For \(\lambda=2\), \(b_{r,2}=b_0\) from (2), and
\[
C_{r,2}=C_r.
\tag{19}
\]

---

## 4. Subset sums of a full integer interval

The following elementary lemma turns Theorem 2.1 into a statement about actual subset sums.

### Lemma 4.1

Let \(1\le N\le M\) and \(M\ge2N\). If
\[
B=\{N,N+1,\ldots,M\},
\qquad
S=\sum_{n=N}^M n,
\]
then
\[
[N,S-N]\cap\mathbb Z\subseteq\Sigma(B).
\tag{20}
\]

### Proof

Let \(m=M-N+1\). The sums of exactly \(j\) distinct members of \(B\) form every integer in
\[
L_j=jN+\binom j2
\quad\text{through}\quad
U_j=jM-\binom j2.
\tag{21}
\]
This standard fact follows, for example, by successively increasing the entries of a \(j\)-element subset.

For \(1\le j\le m-2\),
\[
U_j+1-L_{j+1}
 =j(M-N-j)-N+1.
\tag{22}
\]
The right side is a concave function of \(j\), and at both endpoints
\(j=1,m-2\) it equals \(M-2N\). Thus it is nonnegative. Hence the intervals in (21), for \(j=1,\ldots,m-1\), overlap consecutively. Their union begins at \(N\) and ends at
\[
U_{m-1}=S-N.
\]
This proves (20). ∎

---

## 5. The conjecture for wide interval-block colorings

Call an \(r\)-coloring a **wide interval-block coloring** if, after changing finitely many integers, there are integers
\[
N_0<N_1<N_2<\cdots
\]
and labels \(\gamma_k\in[r]\) such that

1. every integer in
   \[
   B_k=[N_k,N_{k+1}-1]
   \]
   has color \(\gamma_k\); and

2. eventually
   \[
   N_{k+1}-1\ge2N_k.
   \tag{23}
   \]

The colors and block widths may otherwise be completely arbitrary.

### Theorem 5.1

Every wide interval-block \(r\)-coloring satisfies
\[
\max_i\overline d_{\log}\bigl(\Sigma(A_i)\bigr)\ge C_r.
\tag{24}
\]

### Proof

Fix \(1<\lambda<2\). Put \(t_k=\log N_k\).

By Lemma 4.1, the subset sums of \(B_k\) contain
\[
[N_k,S_k-N_k],
\]
where
\[
S_k=\sum_{n=N_k}^{N_{k+1}-1}n.
\]
Condition (23) gives
\[
S_k-N_k\gg N_{k+1}^2.
\]
Therefore, for every fixed \(\lambda<2\) and all sufficiently large \(k\),
\[
[N_k,\lfloor N_{k+1}^{\lambda}\rfloor]
 \subseteq\Sigma(B_k)
 \subseteq\Sigma(A_{\gamma_k}).
\tag{25}
\]

Under the change of variables \(u=\log n\), the integer interval in (25) corresponds, up to endpoint errors \(o(1)\), to
\[
[t_k,\lambda t_{k+1}].
\]
Moreover,
\[
\sum_{a\le n\le b}\frac1n
 =\log\frac ba+O(1/a).
\tag{26}
\]
Since (23) implies that the \(N_k\) grow at least geometrically, the accumulated errors in (26) are bounded. Thus Theorem 2.1 implies
\[
\max_i\overline d_{\log}\bigl(\Sigma(A_i)\bigr)
 \ge C_{r,\lambda}.
\]
Letting \(\lambda\uparrow2\), and using (18), gives
\[
C_{r,\lambda}\longrightarrow C_{r,2}=C_r.
\]
This proves (24). ∎

---

## 6. Matching construction inside this class

The lower bound above is sharp even within the restricted class.

Take
\[
t_k=b_0^k,\qquad
N_k=\left\lceil e^{t_k}\right\rceil,
\]
and color the block \([N_k,N_{k+1})\) by \(k\bmod r\).

If a subset sum of color \(i\) has its largest summand in block \(k\), then it lies between \(N_k\) and
\[
\sum_{n<N_{k+1}}n<\frac12N_{k+1}^2.
\]
Consequently,
\[
\Sigma(A_i)
 \subseteq
 \bigcup_{k\equiv i\;(\mathrm{mod}\ r)}
 \left[N_k,\frac12N_{k+1}^2\right].
\tag{27}
\]

On the logarithmic scale, these are, up to \(O(1)\) endpoint errors,
\[
[b_0^k,\,2b_0^{k+1}].
\]
Because
\[
b_0>2^{1/(r-1)},
\]
successive intervals of the same color are disjoint. At the right endpoint of the interval indexed by \(k\), the logarithmic density is asymptotic to
\[
\frac{
 \sum_{j\ge0}(2b_0-1)b_0^{k-rj}
}{
 2b_0^{k+1}
}
=
\frac{1-\frac1{2b_0}}{1-b_0^{-r}}
=C_r.
\tag{28}
\]
Between right endpoints, the density decreases through each gap and increases through each occupied interval, so (28) is the upper density. Hence
\[
\max_i\overline d_{\log}\bigl(\Sigma(A_i)\bigr)\le C_r.
\]

Together with Theorem 5.1, this proves:

### Corollary 6.1

If \(c_r^{\mathrm{block}}\) denotes the infimum defining \(c_r\), restricted to wide interval-block colorings, then
\[
c_r^{\mathrm{block}}
 =C_r
 =\frac{b_0^{r-1}}{2r}.
\tag{29}
\]

Thus the conjectured construction is optimal not merely among cyclic geometric constructions, but among all sufficiently wide interval-block colorings, with arbitrary scale sequence and arbitrary block-color word.

---

## 7. Remaining gap

This does not prove \(c_r=C_r\) for unrestricted colorings. The essential unproved step would be a reduction from an arbitrary coloring to the geometric situation of Theorem 2.1.

For a full monochromatic interval \([N,M]\), Lemma 4.1 supplies a consecutive interval of subset sums extending to order \(M^2\), which is exactly what creates the dilation
\[
[\log N,\log M]\longmapsto[\log N,2\log M].
\]
An arbitrary coloring may interlace its colors at every integer and need not contain any wide monochromatic interval. Dense monochromatic subsets can also have modular obstructions, so Lemma 4.1 has no immediate replacement preserving both endpoints on the logarithmic scale.

Therefore the unrestricted \(r\ge3\) conjecture remains unresolved here. The proved result isolates the missing issue: the scale-optimization and arbitrary block-scheduling part of the conjecture is valid; what remains is an additive-combinatorial reduction handling interlaced color classes.