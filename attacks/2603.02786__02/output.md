```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "The conjectured asymptotic is proved when k = Omega(sqrt(n)) and k^2 <= n/2, with a capped prime-square upper bound obtained throughout the full range k < sqrt(n).",
  "would_publish": false,
  "caveats": "The range n/2 < k^2 < n remains open, and novelty has not been checked against the complete source text."
}
```

# 1. Statement and partial result

I use the following standard interpretation from the abstract. Put
\[
A_d(n)=\{d,2d,\ldots,\lfloor n/d\rfloor d\},
\]
and let \(m_k(n)\) be the minimum number of consecutive integer positions containing pairwise disjoint translates of \(A_1(n),\ldots,A_k(n)\). Changing between interval cardinality and diameter affects all estimates by \(O(1)\).

Write
\[
\pi(x)=|\{p\le x:p\text{ prime}\}|,\qquad
Q(k)=\sum_{p\le k}p^2,
\]
and
\[
\Phi(n,k)=\sum_{p\le k}\min\{p^2,n/2\}.
\]

The argument below proves the following.

## Theorem

Let \(k=\Omega(\sqrt n)\) and \(k<\sqrt n\). Then
\[
m_k(n)\ge n\pi(k)-Q(k)-o\!\left(\frac{nk}{\log k}\right)
\tag{1}
\]
and
\[
m_k(n)\le n\pi(k)-\Phi(n,k)
      +o\!\left(\frac{nk}{\log k}\right).
\tag{2}
\]

Consequently, if in addition
\[
k^2\le \frac n2,
\]
then
\[
m_k(n)=n\pi(k)-Q(k)+o\!\left(\frac{nk}{\log k}\right),
\]
and hence, by the prime number theorem and partial summation,
\[
m_k(n)\sim
\left(1-\frac{k^2}{3n}\right)\frac{k}{\log k}\,n.
\tag{3}
\]

Thus Conjecture 5 holds in the full constant-ratio subrange
\[
0<c\le \frac{k}{\sqrt n}\le \frac1{\sqrt2}.
\]

No unproved number-theoretic conjecture is used.

---

# 2. Lower bound from the prime subfamily

Consider only the translated copies corresponding to primes \(p\le k\). The convex hull of a translated copy of \(A_p(n)\) contains
\[
h_p=\bigl(\lfloor n/p\rfloor-1\bigr)p+1\ge n-2p+1\ge n-2k
\tag{4}
\]
consecutive integer positions.

For distinct primes \(p,q\), the two translated progressions lie in residue classes modulo \(p\) and \(q\). Their two hulls cannot have an intersection containing \(pq\) consecutive integers: by the Chinese remainder theorem, every \(pq\) consecutive integers contain a simultaneous solution of the two congruences, which would belong to both finite progressions.

Thus the hull intersection has fewer than \(pq\) positions.

For two integer intervals of cardinalities \(a,b\), with centers \(c,c'\), whose intersection has at most \(L\) positions, one has
\[
|c-c'|\ge \min\{a,b\}-L-O(1).
\tag{5}
\]
Indeed, if the shorter interval is contained in the longer, the assertion is trivial unless its length exceeds \(L\), in which case containment is impossible; otherwise it follows directly by writing the overlap in terms of the center separation.

Order the prime hulls by their centers, say their prime labels in this order are
\[
p_1,p_2,\ldots,p_r,\qquad r=\pi(k).
\]
Equations (4) and (5) give
\[
c_{i+1}-c_i\ge n-2k-p_ip_{i+1}-O(1).
\]
Adding these inequalities, including the two endpoint half-lengths, shows that every containing interval has length at least
\[
r(n-2k)-\sum_{i=1}^{r-1}p_ip_{i+1}-O(r).
\tag{6}
\]

By \(2xy\le x^2+y^2\),
\[
\sum_{i=1}^{r-1}p_ip_{i+1}
 \le \frac12\sum_{i=1}^{r-1}(p_i^2+p_{i+1}^2)
 \le \sum_{p\le k}p^2=Q(k).
\tag{7}
\]
Therefore
\[
m_k(n)\ge n\pi(k)-Q(k)-O(k\pi(k)).
\tag{8}
\]
Since \(k=\Omega(\sqrt n)\) and \(k<\sqrt n\), we have \(n=\Theta(k^2)\), and
\[
k\pi(k)=o\!\left(\frac{nk}{\log k}\right).
\]
This proves (1).

---

# 3. Packing one largest-prime-factor class into an \(n\)-interval

The upper bound uses the following exact residue-class packing lemma.

## Lemma 1

For every prime \(p\), there are residue classes
\[
C_d\pmod d,\qquad P^+(d)=p,
\]
that are pairwise disjoint as subsets of \(\mathbb Z\). Here \(P^+(d)\) denotes the largest prime factor of \(d\).

### Proof

Proceed inductively over the primes. For a prime \(p\), choose distinct residues modulo \(p\) indexed by

- a terminal symbol \(0\);
- a recursive symbol \(*\);
- one symbol for each prime \(q<p\).

There are
\[
2+\pi(p-1)\le p
\]
such symbols.

If \(C=r+d\mathbb Z\) is a residue class, define its lift into the child \(\alpha\pmod p\) by
\[
L_\alpha(C)=\alpha+pC
           =\alpha+pr+pd\mathbb Z.
\]

Every \(d\) with \(P^+(d)=p\) has a unique representation
\[
d=p^e a,\qquad e\ge1,\quad p\nmid a.
\]

- If \(a=1\), start with the terminal class modulo \(p\) and apply the recursive lift \(e-1\) times.
- If \(a>1\), let \(q=P^+(a)<p\). By induction there is a class \(C_a\pmod a\) in the \(q\)-system. First lift \(C_a\) into the \(q\)-child modulo \(p\), and then apply the recursive lift \(e-1\) times.

Two resulting classes whose first nonrecursive symbols differ lie in different residue classes modulo \(p\). If both begin with a recursive symbol, remove that common lift and continue. Since every modulus has finite \(p\)-adic valuation, this process terminates. Hence the classes are pairwise disjoint. ∎

Every interval of \(n\) consecutive integers contains at least \(\lfloor n/d\rfloor\) members of every residue class modulo \(d\). Choosing \(\lfloor n/d\rfloor\) consecutive such members gives a translate of \(A_d(n)\). It follows that, for each fixed prime \(p\), all progressions with largest prime factor \(p\) can be packed into one interval of \(n\) positions.

This alone gives the elementary \(n\pi(k)\)-type upper bound. The next construction recovers a nontrivial part of the prime-square correction.

---

# 4. A simultaneous two-neighbour congruence lemma

## Lemma 2

Let \(p\) be prime and let \(A,B\not\equiv0\pmod p\). There are nonzero integers \(u,v\) such that
\[
Au\equiv Bv\pmod p,
\qquad
|u|,|v|\le 2\sqrt p.
\tag{9}
\]

### Proof

Put \(\alpha=BA^{-1}\pmod p\) and \(h=\lceil\sqrt p\rceil\). Among
\[
0,\alpha,2\alpha,\ldots,h\alpha\pmod p
\]
two circular representatives differ by at most \(p/h\le\sqrt p\). Hence for some \(1\le |v|\le h\) there is a nonzero signed integer \(u\), with \(|u|\le\sqrt p\), such that
\[
\alpha v\equiv u\pmod p.
\]
Multiplying by \(A\) proves (9). ∎

---

# 5. Large-prime blocks with controlled adjacent overlap

Set
\[
R=\left\lfloor\sqrt{\log k}\right\rfloor,
\qquad
H=\operatorname{lcm}(1,2,\ldots,R).
\]
Since \(H\le R^R\),
\[
H=k^{o(1)}.
\tag{10}
\]

Call a prime large if \(p>k/R\), and list the large primes increasingly:
\[
p_1<p_2<\cdots<p_t.
\]
For such a prime, all \(d\le k\) with \(P^+(d)=p_i\) are precisely
\[
d=ap_i,\qquad 1\le a\le \left\lfloor\frac{k}{p_i}\right\rfloor\le R,
\]
for sufficiently large \(k\).

For each internal index \(i\), Lemma 2 supplies integers
\[
u_{i,-},u_{i,+}
\]
with absolute value at most \(2\sqrt{p_i}\), and a nonzero residue \(c_i\pmod{p_i}\), such that
\[
c_i\equiv p_{i-1}u_{i,-}
     \equiv p_{i+1}u_{i,+}\pmod{p_i}.
\tag{11}
\]
At the two endpoints only the one relevant representation is needed.

Choose
\[
B=\left\lceil 10HRk^{3/2}\right\rceil.
\tag{12}
\]
By (10),
\[
B=k^{3/2+o(1)}=o(k^2/R^2).
\tag{13}
\]

For consecutive large primes put
\[
w_i=\min\{p_ip_{i+1},n/2\}.
\]
Choose \(D_i\) to be the least multiple of \(Hp_i\) satisfying
\[
D_i\ge n-w_i+2B,
\tag{14}
\]
and define block anchors recursively by
\[
S_1=0,\qquad S_{i+1}=S_i+D_i.
\]

Because \(w_i\gg B+Hp_i\), one has \(D_i<n\), and
\[
D_i<n-w_i+2B+Hp_i.
\tag{15}
\]

For \(1\le a\le k/p_i\), assign the modulus \(ap_i\) the residue class
\[
S_i+Ha c_i\pmod{ap_i}.
\tag{16}
\]

## Internal disjointness

For \(a\ne b\), the two residues in (16) differ modulo \(p_i\) by
\[
Hc_i(a-b)\not\equiv0\pmod{p_i},
\]
since \(p_i>R\), \(p_i\nmid H\), and \(c_i\not\equiv0\pmod{p_i}\). Thus all classes belonging to one large prime are pairwise disjoint.

## Adjacent blocks

Consider \(p_i\) and \(p_{i+1}\), and write \(p=p_i,q=p_{i+1}\). Since \(D_i\) is divisible by \(Hp\), it is divisible by \(ap\) for every \(a\le R\). Thus, relative to the anchor \(S_{i+1}\), the left class in (16) is
\[
qHa\,u_{i,+}\pmod{ap},
\]
while the right class corresponding to \(bq\) is
\[
pHb\,u_{i+1,-}\pmod{bq}.
\]

A simultaneous solution is therefore
\[
z_{a,b}
 =qHa\,u_{i,+}+pHb\,u_{i+1,-}.
\tag{17}
\]
Indeed, the second summand is divisible by \(ap\), because \(a\mid H\), and the first summand is divisible by \(bq\), because \(b\mid H\).

Moreover,
\[
|z_{a,b}|<B.
\tag{18}
\]
Since \(p,q>R\),
\[
\operatorname{lcm}(ap,bq)
 =pq\,\operatorname{lcm}(a,b)\ge pq.
\tag{19}
\]
Hence all intersections of these two infinite residue classes are of the form
\[
S_{i+1}+z_{a,b}
 +\ell\,\operatorname{lcm}(ap,bq).
\]
Equations (18) and (19) show that there is no such intersection in
\[
[S_{i+1}+B,\;S_{i+1}+pq-B].
\tag{20}
\]

Now let the core interval for group \(i\) be the \(n\)-position interval
\[
I_i=[S_i+B,S_i+B+n).
\]
Its intersection with the next core begins at \(S_{i+1}+B\), and by (14) its other endpoint is at most
\[
S_{i+1}+B+n-D_i
 \le S_{i+1}+B+w_i-2B
 \le S_{i+1}+pq-B.
\]
Thus \(I_i\cap I_{i+1}\) is contained in the collision-free interval (20).

Finally,
\[
D_i\ge n/2+2B.
\]
Consequently,
\[
D_i+D_{i+1}>n,
\]
so nonconsecutive core intervals are disjoint. Thus only adjacent groups need the congruence analysis above.

Select, for every \(ap_i\), the required \(\lfloor n/(ap_i)\rfloor\) consecutive points from its residue class lying in \(I_i\). This gives pairwise disjoint translated copies of every progression assigned to a large prime.

---

# 6. Length of the construction

The large-prime portion occupies an interval of length at most
\[
n+\sum_{i=1}^{t-1}D_i.
\]
Using (15),
\[
\begin{aligned}
n+\sum_{i=1}^{t-1}D_i
&\le
tn-\sum_{i=1}^{t-1}w_i
 +2B(t-1)+H\sum_{i=1}^{t-1}p_i\\
&=
tn-\sum_{i=1}^{t-1}w_i
 +o\!\left(\frac{nk}{\log k}\right).
\end{aligned}
\tag{21}
\]
Indeed, \(t\le k\), \(B=k^{3/2+o(1)}\), \(H=k^{o(1)}\), and \(n=\Theta(k^2)\).

For every prime \(p\le k/R\), use Lemma 1 to put all moduli with largest prime factor \(p\) in their own \(n\)-position interval. Put \(A_1(n)\) in one further interval. Concatenating these intervals with the large-prime construction gives
\[
m_k(n)
\le n\pi(k)-\sum_{i=1}^{t-1}w_i
 +o\!\left(\frac{nk}{\log k}\right).
\tag{22}
\]

Let \(f(x)=\min\{x^2,n/2\}\). Since \(p_i<p_{i+1}\),
\[
\left|
\min\{p_ip_{i+1},n/2\}-f(p_i)
\right|
\le p_i(p_{i+1}-p_i).
\]
Summing,
\[
\sum_{i=1}^{t-1}w_i
=
\sum_{\substack{k/R<p\le k\\p\ {\rm prime}}}
\min\{p^2,n/2\}
+O(n+k^2).
\tag{23}
\]
The omitted small-prime contribution satisfies
\[
\sum_{p\le k/R}\min\{p^2,n/2\}
\le \sum_{m\le k/R}m^2
=O(k^3/R^3)
=o\!\left(\frac{nk}{\log k}\right),
\tag{24}
\]
because \(R=\sqrt{\log k}\) and \(n=\Theta(k^2)\).

Combining (22)–(24) proves
\[
m_k(n)\le n\pi(k)-\Phi(n,k)
 +o\!\left(\frac{nk}{\log k}\right),
\]
which is (2).

---

# 7. Deduction of the conjecture for \(k^2\le n/2\)

If \(k^2\le n/2\), then \(p^2\le n/2\) for every \(p\le k\), so
\[
\Phi(n,k)=Q(k).
\]
The lower and upper bounds therefore agree:
\[
m_k(n)=n\pi(k)-Q(k)
 +o\!\left(\frac{nk}{\log k}\right).
\]

The prime number theorem and partial summation give
\[
\pi(k)\sim\frac{k}{\log k},
\qquad
Q(k)=\sum_{p\le k}p^2\sim\frac{k^3}{3\log k}.
\]
Hence
\[
m_k(n)
=
\left(1-\frac{k^2}{3n}+o(1)\right)
\frac{nk}{\log k},
\]
proving (3).

---

# 8. What remains for \(n/2<k^2<n\)

The general capped upper bound is strictly weaker than the conjectured one once \(k^2>n/2\). For example, if
\[
\frac{k}{\sqrt n}\to c\in(1/\sqrt2,1),
\]
the bounds above become
\[
\left(c-\frac{c^3}{3}+o(1)\right)
 \frac{n^{3/2}}{\log k}
\le m_k(n)
\]
and
\[
m_k(n)
\le
\left(\frac c2+\frac1{3\sqrt2}+o(1)\right)
 \frac{n^{3/2}}{\log k}.
\]

The obstruction in the construction is precise. Recovering an overlap close to \(p_ip_{i+1}>n/2\) makes three or more consecutive \(n\)-blocks overlap. The residue choices above synchronize all intersections of adjacent largest-prime-factor groups, but they do not control intersections between nonadjacent groups occupying the same positions. Resolving those simultaneous congruence constraints, without losing a positive proportion of the total \(\sum p^2\) saving, is the remaining gap.