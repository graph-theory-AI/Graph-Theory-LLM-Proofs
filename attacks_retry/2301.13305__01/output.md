```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A Fano-plane argument gives d_{K_4}(n) <= 11/32 for n >= 7, and codes determined by boundedly many quadratic tests are eventually empty.",
  "would_publish": false,
  "caveats": "The unrestricted o(1) claim is not settled; novelty relative to all follow-up literature has not been verified."
}
```

# 1. Statement and partial results

Put
\[
V_n=\mathbb F_2^{E(K_n)},\qquad N=\binom n2.
\]
For \(X\in\binom{[n]}4\), let \(k_X\in V_n\) be the indicator of \(E(K_n[X])\). A family \(\mathcal A\subseteq V_n\) is a \(K_4\)-difference-free code if
\[
\mathcal A\cap(\mathcal A+k_X)=\varnothing
\qquad\text{for every }X\in\binom{[n]}4.
\]
Write
\[
d_{K_4}(n)=\max_{\mathcal A}\frac{|\mathcal A|}{2^N},
\]
where the maximum is over such codes.

I prove two partial results.

**Theorem A.** For every \(n\ge 7\),
\[
\boxed{d_{K_4}(n)\le \frac{11}{32}.}
\]

This improves the \(5/12\) bound in the supplied attempt. The proof below does not use its seven-vertex parity computation.

The second result concerns genuinely nonlinear families. A *quadratic test* means a polynomial \(q:V_n\to\mathbb F_2\) of degree at most two, with no restriction on its rank.

**Theorem B.** Fix \(r\ge1\), and set
\[
C_r=2r^2+r+2^r-1.
\]
Suppose a family has the form
\[
\mathcal A=\{G\in V_n:h(q_1(G),\ldots,q_r(G))=1\},
\]
where \(h:\mathbb F_2^r\to\{0,1\}\) is arbitrary and each \(q_i\) is quadratic. If
\[
n\ge R_{2^{C_r}}(4),
\]
then \(\mathcal A\) cannot be both nonempty and \(K_4\)-difference-free.

Here \(R_q(4)\) denotes the \(q\)-color Ramsey number of \(K_4\). Thus boundedly many quadratic tests—not merely boundedly many linear parity tests—cannot define a nonempty code for all sufficiently large \(n\).

Neither result proves the unrestricted conjecture.

# 2. A Fano-plane obstruction

## 2.1. An auxiliary graph with independence number \(22\)

Let \(Q\) be the Cayley graph on \(\mathbb F_2^6\) with generating set
\[
\{e_1,\ldots,e_6,\mathbf1\},
\]
where \(\mathbf1=(1,\ldots,1)\).

**Lemma 2.1.**
\[
\alpha(Q)=22.
\]

### Proof

Consider the linear map
\[
T(x)=x+\left(\sum_{i=1}^6x_i\right)\mathbf1.
\]
Because six is even, \(T^2\) is the identity. Moreover,
\[
T(e_i)=e_i+\mathbf1,\qquad T(\mathbf1)=\mathbf1.
\]
Consequently, \(T\) identifies \(Q\) with the graph in which two binary words are adjacent exactly when their Hamming distance is five or six.

Thus \(\alpha(Q)\) is the maximum size of a family \(\mathcal F\subseteq 2^{[6]}\) of Hamming diameter at most four. The family
\[
\{A\subseteq[6]:|A|\le2\}
\]
has size
\[
1+6+15=22
\]
and diameter at most four. It remains to prove the upper bound.

Apply coordinate down-compressions to \(\mathcal F\): replace \(A\ni i\) by \(A\setminus\{i\}\) whenever the latter is absent. These preserve size and do not increase diameter. To check the only potentially problematic case, suppose \(A\) is moved down while another retained set \(B\) contains \(i\). Then \(B\setminus\{i\}\) was already present, and
\[
d(A\setminus\{i\},B)=d(A,B\setminus\{i\}).
\]
Repeated compression therefore produces a down-set of the same size and diameter at most four.

If the resulting down-set uses at most five coordinates, its size is at most \(16\): in the five-dimensional cube, complementary pairs have distance five, so at most one member of each of the \(16\) pairs is allowed.

Otherwise all six singletons are present. The empty set is also present. No set of size at least five can occur, and a four-set cannot occur because its distance from an outside singleton is five. Hence the family consists of sets of sizes zero through three.

Let \(\mathcal T\) be its collection of triples. These triples are pairwise intersecting. Put
\[
\overline{\mathcal T}
=\{[6]\setminus A:A\in\mathcal T\},
\]
which is also an intersecting family of triples. Every pair in the lower shadow
\[
\partial\overline{\mathcal T}
=\{B\in\tbinom{[6]}2:B\subseteq C
       \text{ for some }C\in\overline{\mathcal T}\}
\]
is disjoint from a triple in \(\mathcal T\), and therefore cannot belong to \(\mathcal F\). It follows that
\[
|\mathcal F|
\le 1+6+15-|\partial\overline{\mathcal T}|+|\mathcal T|.
\tag{2.1}
\]

We need the following elementary shadow inequality:
\[
|\partial\mathcal H|\ge|\mathcal H|
\quad\text{for every intersecting }
\mathcal H\subseteq\binom{[6]}3.
\tag{2.2}
\]

To prove it, choose a uniformly random cyclic ordering of the six vertices. Among its six consecutive triples, at most three can lie in \(\mathcal H\), because opposite triples are complementary. Let \(a\le3\) be the number that do.

Each selected triple supplies its two consecutive pairs to \(\partial\mathcal H\). If \(a>0\), these supply at least \(a+1\) distinct consecutive pairs: a nonempty proper set of starting positions on a cycle gains at least one position upon taking its union with its one-step translate. Thus, if \(b\) is the number of consecutive pairs belonging to \(\partial\mathcal H\),
\[
b\ge \frac43a.
\]
Taking expectations gives
\[
\frac6{\binom62}|\partial\mathcal H|
\ge
\frac43\frac6{\binom63}|\mathcal H|,
\]
which is precisely (2.2).

Apply (2.2) to \(\overline{\mathcal T}\) in (2.1). We obtain \(|\mathcal F|\le22\), proving the lemma. \(\square\)

## 2.2. Seven \(K_4\)'s whose sum is zero

Identify seven vertices with
\[
P=\mathbb F_2^3\setminus\{0\}.
\]
For each \(a\in P\), define
\[
X_a=\{v\in P:a\cdot v=1\}.
\]
Each \(X_a\) has four vertices.

For distinct \(u,v\in P\), the equations
\[
a\cdot u=a\cdot v=1
\]
have exactly two solutions \(a\in P\), since \(u,v\) are linearly independent over \(\mathbb F_2\). Therefore every edge of \(K_7\) belongs to exactly two of these seven copies of \(K_4\). Their incidence vectors satisfy
\[
\sum_{a\in P}k_{X_a}=0.
\tag{2.3}
\]

These are the complements of the seven lines of the Fano plane.

### Proof of Theorem A

For \(n\ge7\), use this configuration on seven of the vertices. Label its seven vectors \(k_1,\ldots,k_7\). Define
\[
\phi:\mathbb F_2^6\longrightarrow V_n,
\qquad
\phi(e_i)=k_i\quad(1\le i\le6).
\]
Equation (2.3) gives
\[
\phi(\mathbf1)=k_7.
\]

Let \(\mathcal A\) be a code of density \(\delta\). For each \(G\in V_n\), put
\[
I_G=\{x\in\mathbb F_2^6:G+\phi(x)\in\mathcal A\}.
\]
Whenever two vertices are adjacent in \(Q\), their images under \(\phi\) differ by one of \(k_1,\ldots,k_7\). Hence \(I_G\) is independent in \(Q\), and Lemma 2.1 gives
\[
|I_G|\le22.
\]
Averaging over uniformly random \(G\),
\[
64\delta=\mathbb E_G|I_G|\le22.
\]
Therefore
\[
\delta\le\frac{22}{64}=\frac{11}{32}.
\qquad\square
\]

Injectivity of \(\phi\) is not needed. Also, sharpness of the auxiliary bound \(\alpha(Q)=22\) does **not** assert sharpness of Theorem A for graph codes.

# 3. Quadratic factors have a subspace of popular differences

Theorem B follows from an elementary additive statement that is useful independently of graph codes.

For \(r\ge1\), set
\[
D_r=2r^2+r,\qquad
C_r=D_r+2^r-1,\qquad
\eta_r=2^{-(2r^2+3r+1)}.
\]

**Lemma 3.1 — Quadratic popular-difference lemma.**  
Let \(V\) be a finite-dimensional vector space over \(\mathbb F_2\). Suppose
\[
A=\{x\in V:h(q_1(x),\ldots,q_r(x))=1\}
\]
is nonempty, where the \(q_i\) have degree at most two and \(h\) is arbitrary.

Then there is a linear subspace \(W\le V\), of codimension at most \(C_r\), such that
\[
\frac{|A\cap(A+w)|}{|V|}\ge\eta_r
\qquad\text{for every }w\in W.
\tag{3.1}
\]
In particular,
\[
W\subseteq A+A.
\]

I give the details, including the low-rank cases.

## 3.1. Three quadratic-form facts

For a quadratic polynomial \(p\) with \(p(0)=0\), its polar form is
\[
B_p(x,y)=p(x+y)+p(x)+p(y).
\]
It is alternating and bilinear, so its rank is even.

**Fact 1: a low-rank quadratic vanishes on a low-codimension subspace.**  
If \(\operatorname{rank}B_p=2t\), then
\[
p(x)=\sum_{i=1}^t u_i(x)v_i(x)+\ell(x)
\]
for suitable linear forms \(u_i,v_i,\ell\). This follows by putting the alternating form into symplectic normal form; the difference between two quadratic functions with the same polar form is linear. Therefore \(p\) vanishes on
\[
\bigcap_{i=1}^t\ker u_i\cap\ker\ell,
\]
whose codimension is at most \(t+1\).

**Fact 2: restriction decreases rank by at most twice the codimension.**  
If \(U\le V\) has codimension \(c\), then
\[
\operatorname{rank}(B|_{U\times U})
\ge \operatorname{rank}B-2c.
\tag{3.2}
\]
Indeed, in an adapted basis, deleting \(c\) rows and \(c\) columns decreases matrix rank by at most \(2c\).

**Fact 3: quadratic exponential sums are controlled by polar rank.**  
If a quadratic polynomial on an affine space has polar rank \(R\), then
\[
\left|\mathbb E_x(-1)^{p(x)}\right|\le2^{-R/2}.
\tag{3.3}
\]
For completeness, after parameterizing the affine space by a vector space \(U\), squaring the average gives
\[
\left|\mathbb E_x(-1)^{p(x)}\right|^2
=
\mathbb E_h(-1)^{p(h)+p(0)}
       \mathbb E_x(-1)^{B_p(x,h)}.
\]
The inner average is zero unless \(h\) lies in the radical of \(B_p\). Its radical has density \(2^{-R}\), proving (3.3).

## 3.2. Eliminating low-rank combinations

Choose \(a\in A\) and normalize the tests:
\[
p_i(x)=q_i(a+x)+q_i(a).
\]
Then \(p_i(0)=0\), and
\[
a+\{x:p_i(x)=0\text{ for every }i\}\subseteq A.
\tag{3.4}
\]

Start with \(U=V\). Consider the vector space of restrictions to \(U\) of the polynomials in \(\operatorname{span}\{p_1,\ldots,p_r\}\).

If it contains a nonzero polynomial whose polar rank is less than \(4r+2\), that rank is at most \(4r\). By Fact 1, we can restrict \(U\) to a subspace of codimension at most \(2r+1\) on which this polynomial vanishes identically.

Each such step strictly decreases the dimension of the space of restricted polynomials. There are therefore at most \(r\) steps. At termination,
\[
\operatorname{codim}_V U\le r(2r+1)=D_r,
\tag{3.5}
\]
and every nonzero remaining polynomial has polar rank at least \(4r+2\).

Let \(P_1,\ldots,P_k\), with \(k\le r\), be a basis of the remaining polynomial space. Put
\[
Z=\{x\in U:P_i(x)=0\text{ for }1\le i\le k\}.
\]
By (3.4),
\[
a+Z\subseteq A.
\tag{3.6}
\]

If \(k=0\), then \(Z=U\), and taking \(W=U\) proves the lemma, including (3.1). Assume henceforth that \(k>0\).

## 3.3. Removing all consistency obstructions

For each nonzero \(b\in\mathbb F_2^k\), write
\[
P_b=\sum_{i=1}^k b_iP_i,\qquad B_b=B_{P_b},
\]
and let
\[
R_b=\{s\in U:B_b(s,x)=0\text{ for all }x\in U\}
\]
be its radical.

The restriction \(P_b|_{R_b}\) is linear. Choose any extension of this restriction to a linear functional \(\ell_b\) on \(U\), and set
\[
W=\bigcap_{b\ne0}\ker\ell_b.
\]
Then
\[
\operatorname{codim}_V W
\le D_r+2^k-1\le C_r.
\tag{3.7}
\]

Fix \(s\in W\). Consider the system of linear equations in \(x\in U\):
\[
B_{P_i}(x,s)=P_i(s),
\qquad 1\le i\le k.
\tag{3.8}
\]
This system is consistent. Indeed, a linear dependence among its left-hand sides is specified by some \(b\) with
\[
B_b(x,s)=0\quad\text{for all }x\in U.
\]
Thus \(s\in R_b\), and the corresponding right-hand side is
\[
P_b(s)=\ell_b(s)=0.
\]
So every dependence among the equations has compatible right-hand side.

Let \(X_s\) be the affine solution space of (3.8). Its codimension in \(U\) is at most \(k\).

## 3.4. Finding simultaneous zeros

For every nonzero \(b\), the polar rank of \(P_b\) on the direction space of \(X_s\) is, by Fact 2, at least
\[
4r+2-2k\ge2k+2.
\]
Hence Fact 3 gives
\[
\left|\mathbb E_{x\in X_s}(-1)^{P_b(x)}\right|
\le2^{-k-1}.
\]
Fourier expansion of the indicator of simultaneous zero yields
\[
\begin{aligned}
\Pr_{x\in X_s}\bigl(P_1(x)=\cdots=P_k(x)=0\bigr)
&=
2^{-k}\sum_{b\in\mathbb F_2^k}
  \mathbb E_{x\in X_s}(-1)^{P_b(x)}\\
&\ge
2^{-k}\bigl(1-(2^k-1)2^{-k-1}\bigr)\\
&\ge 2^{-k-1}.
\end{aligned}
\tag{3.9}
\]

For every such zero \(x\), equations (3.8) imply
\[
P_i(x+s)
=P_i(x)+P_i(s)+B_{P_i}(x,s)=0.
\]
Thus \(x,x+s\in Z\), and (3.6) gives
\[
a+x,\ a+x+s\in A.
\]

Finally, (3.5), the codimension bound for \(X_s\), and (3.9) give
\[
\begin{aligned}
\frac{|A\cap(A+s)|}{|V|}
&\ge
2^{-D_r-k}\,2^{-k-1}\\
&\ge
2^{-(D_r+2r+1)}
=\eta_r.
\end{aligned}
\]
This proves Lemma 3.1. \(\square\)

# 4. Application to graph codes

### Proof of Theorem B

Suppose \(\mathcal A\) is nonempty and determined by \(r\) quadratic tests. Lemma 3.1 supplies a subspace
\[
W\subseteq \mathcal A+\mathcal A
\]
of codimension \(s\le C_r\).

Choose linear functionals \(L_1,\ldots,L_s\) defining \(W\):
\[
W=\bigcap_{j=1}^s\ker L_j.
\]
Color each edge \(e\in E(K_n)\) by
\[
\bigl(L_1(\mathbf1_e),\ldots,L_s(\mathbf1_e)\bigr)
\in\mathbb F_2^s.
\]
There are at most \(2^{C_r}\) colors.

If \(n\ge R_{2^{C_r}}(4)\), there is a four-set \(X\) whose six edges have a common color. Since six is even,
\[
L_j(k_X)
=\sum_{e\in E(K_n[X])}L_j(\mathbf1_e)=0
\]
for every \(j\). Thus
\[
k_X\in W\subseteq\mathcal A+\mathcal A.
\]
Because \(k_X\ne0\), its representation as a sum of two members of \(\mathcal A\) uses distinct members. Their symmetric difference is precisely \(K_n[X]\), a contradiction. \(\square\)

The quadratic ranks may grow with \(N\). Thus this is not simply the bounded-dimensional linear-factor obstruction in different notation.

## A robust version

The popular-difference conclusion also excludes sufficiently accurate approximation by bounded quadratic factors.

Let \(\mathcal A\) be any \(K_4\)-difference-free code and let \(\mathcal B\) be a nonempty family determined by \(r\) quadratic tests. If
\[
n\ge R_{2^{C_r}}(4),
\]
then
\[
\boxed{\frac{|\mathcal A\triangle\mathcal B|}{2^N}
\ge \frac{\eta_r}{2}.}
\tag{4.1}
\]

Indeed, the preceding Ramsey argument finds \(k_X\) in the subspace supplied for \(\mathcal B\), so
\[
\mathbb E_G1_{\mathcal B}(G)1_{\mathcal B}(G+k_X)\ge\eta_r,
\]
whereas the corresponding correlation for \(\mathcal A\) is zero. For Boolean functions \(f,g\),
\[
\left|
\mathbb E f(G)f(G+s)-\mathbb E g(G)g(G+s)
\right|
\le 2\mathbb E|f-g|,
\]
which proves (4.1).

# 5. What remains unresolved

The two arguments give different restrictions on a hypothetical positive-density sequence of codes:

- its density is at most \(11/32\);
- it cannot be described, or approximated arbitrarily accurately, using a fixed number of quadratic tests.

The first is still a constant bound. The second places no restriction on families whose quadratic-description complexity grows with \(n\). No argument here forces an arbitrary dense code to have bounded quadratic structure.

Accordingly, these results do **not** establish
\[
d_{K_4}(n)=o(1),
\]
and they do not produce a counterexample. The partial results above are self-contained; their novelty relative to the complete literature is not asserted.