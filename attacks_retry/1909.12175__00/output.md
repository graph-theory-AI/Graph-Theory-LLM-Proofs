```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a Fourier extension criterion, an exact alphabet obstruction for the dual Fano matroid, and the conjecture for every uniform 5-entropic matroid.",
  "would_publish": false,
  "caveats": "The general prime case remains unresolved; novelty of these special cases relative to the source and subsequent literature has not been checked."
}
```

# Partial results

Write \(H_q=H/\log q\). A matroid \(M=(E,r)\) is \(q\)-entropic if random variables \(X_e\), each with at most \(q\) values, satisfy
\[
H_q(X_S)=r(S)\qquad(S\subseteq E).
\]
Constants represent loops.

I do not obtain a proof or counterexample to the full conjecture. The following are rigorous partial results.

1. **One-element extension criterion.** Suppose a \(p\)-entropic realization becomes an \(\mathbb F_p\)-linear code after deleting one element and independently relabeling the remaining alphabets. Then the entire matroid is \(\mathbb F_p\)-representable. The deleted variable need not itself become a linear function.

2. **Consequences of \(M(K_4)\) rigidity.**
   - Every \(p\)-entropic one-element extension of \(M(K_4)\) is \(\mathbb F_p\)-representable.
   - The dual Fano matroid \(F_7^*\) is \(q\)-entropic exactly when \(q\) is a power of \(2\).
   - Every binary \(p\)-entropic matroid is \(\mathbb F_p\)-representable.

3. **Uniform matroids.**
   - Every uniform \(p\)-entropic matroid with rank or corank at most \(3\) is \(\mathbb F_p\)-representable.
   - Every uniform \(5\)-entropic matroid is \(\mathbb F_5\)-representable.
   - Any uniform counterexample at an odd prime \(p\) must have rank \(r\) and corank \(c\) satisfying
     \[
     4\le r,c\le p-2,\qquad r+c\ge p+2.
     \]

The \(M(K_4)\) coordinatization suggested in the previous attempt is valid; I give its proof before using it. The Fourier extension argument goes beyond intersection-generated extensions: it permits one entirely arbitrary extra element.

## 1. Codes and conditioning

Let \(B\) be a basis of a \(q\)-entropic matroid. Then \(X_B\) is uniform on \(q^{|B|}\) tuples, and every other variable is a function of \(X_B\).

For any \(S\subseteq E\), choose a basis \(I\) of \(M|S\). Since \(X_S\) is a function of \(X_I\), and includes \(X_I\), it is uniform on exactly \(q^{r(S)}\) outcomes.

Thus the joint support is a uniform code
\[
C\subseteq Q^E,\qquad |C|=q^{r(E)},
\]
whose projections satisfy
\[
|\pi_S(C)|=q^{r(S)}.
\tag{1}
\]

Deletion preserves \(q\)-entropicity. So does contraction: if \(e\) is a nonloop, conditioning on any value \(X_e=a\) gives
\[
H_q(X_S\mid X_e=a)=r(S\cup e)-1.
\tag{2}
\]
Indeed, the uniform support of \(X_{S\cup e}\) has \(q^{r(S\cup e)}\) outcomes, equally divided among the \(q\) values of \(X_e\).

In particular, a circuit of size \(k+1\) is represented by a \(k\)-ary quasigroup: any \(k\) of its variables determine the remaining one, and each such \(k\)-tuple is uniform on all \(q^k\) possibilities.

## 2. A Fourier one-element extension lemma

### Theorem 2.1

Let \(p\) be prime and \(M\) be \(p\)-entropic. Suppose that, in some entropic realization, the variables indexed by \(E-\{e\}\) become an \(\mathbb F_p\)-linear code after independent alphabet relabelings. Then \(M\) is \(\mathbb F_p\)-representable.

### Proof

Loops and coloops are immediate, so suppose \(e\) is neither.

Write the normalized realization on \(E-\{e\}\) as
\[
X_j=\ell_j(U),\qquad U\text{ uniform on }V=\mathbb F_p^r,
\]
where the forms \(\ell_j\in V^*\) span \(V^*\). Because \(e\) is not a coloop,
\[
T:=X_e=f(U).
\]

Fix one value \(a\) of \(T\), and put
\[
h(u)=\mathbf 1_{\{f(u)=a\}}.
\]
This is nonconstant. Hence its Fourier expansion has a nonzero coefficient at some nonzero \(v\in V^*\):
\[
\widehat h(v)=\mathbb E\!\left[h(U)\exp\!\left(-\frac{2\pi i}{p}v(U)\right)\right]\ne0.
\tag{3}
\]

I claim that appending the column \(v\) to the representation \((\ell_j)\) represents \(M\).

For \(S\subseteq E-\{e\}\), let
\[
L_S=\operatorname{span}_{\mathbb F_p}\{\ell_j:j\in S\}.
\]

If \(e\in\operatorname{cl}_M(S)\), then \(T\), and therefore \(h\), is a function of \(X_S\). Consequently \(h\) is invariant under translations by \(L_S^\perp\). A nonzero Fourier coefficient of such a function must lie in \(L_S\), so (3) gives
\[
v\in L_S.
\tag{4}
\]

If \(e\notin\operatorname{cl}_M(S)\), then
\[
H(T,X_S)=H(T)+H(X_S),
\]
so \(T\) and \(X_S\) are independent. For every nonzero \(w\in L_S\), the character associated with \(w\) is a mean-zero function of \(X_S\). Hence
\[
\widehat h(w)=0.
\]
By (3),
\[
v\notin L_S.
\tag{5}
\]

Together, (4)–(5) give
\[
v\in L_S\quad\Longleftrightarrow\quad e\in\operatorname{cl}_M(S)
\]
for every \(S\). These are exactly the conditions required for the appended column to represent the extension. ∎

The distinction between **linearizing the matroid** and **linearizing its given code** is essential here. The proof produces a suitable linear form \(v\), not necessarily an alphabet relabeling of \(T\).

## 3. Checking the \(M(K_4)\) lead

Label \(M(K_4)\) by \(x,y,z,a,b,c\), with triangles
\[
xya,\quad xzb,\quad yzc,\quad abc.
\]
Choose \(x,y,z\) as a basis. A \(q\)-entropic realization has
\[
A=f(X,Y),\qquad B=g(X,Z),\qquad
C=h(Y,Z)=k(A,B),
\]
where all four displayed binary operations are quasigroups.

Fix \(x_0\). Relabel the alphabets of \(A,B\) so that
\[
f(x_0,y)=y,\qquad g(x_0,z)=z.
\]
Then \(k=h\). Define permutations
\[
\alpha_x(y)=f(x,y),\qquad \beta_x(z)=g(x,z).
\]
They satisfy
\[
h(\alpha_x(y),\beta_x(z))=h(y,z).
\tag{6}
\]

Consider
\[
\Gamma=\{(\alpha,\beta)\in\operatorname{Sym}(Q)^2:
h(\alpha(y),\beta(z))=h(y,z)\ \forall y,z\}.
\]
This is a group.

Its first-coordinate action is free. Indeed, if \(\alpha(y_0)=y_0\), injectivity of the row \(h(y_0,\cdot)\) implies \(\beta=\mathrm{id}\), after which column injectivity implies \(\alpha=\mathrm{id}\). Thus \(|\Gamma|\le q\).

But (6) supplies \(q\) distinct elements \((\alpha_x,\beta_x)\), since \(x\mapsto f(x,y)\) is a permutation for each fixed \(y\). Therefore
\[
|\Gamma|=q,
\]
and both coordinate actions are regular.

Identify the alphabets of \(Y,Z\) with the group \(G=\Gamma\) using these regular actions, and identify \(X\) with its corresponding group element. After relabeling,
\[
A=XY,\qquad B=XZ.
\]
The invariance of \(h\) under simultaneous left multiplication says that it depends only on \(Y^{-1}Z\). Quasigroup injectivity makes this dependence bijective. Relabeling \(C\) yields
\[
\boxed{A=XY,\qquad B=XZ,\qquad C=Y^{-1}Z.}
\tag{7}
\]

For prime \(q=p\), \(G\) is cyclic. Thus every \(p\)-entropic realization of \(M(K_4)\), not merely its underlying matroid, is coordinatewise equivalent to
\[
A=X+Y,\qquad B=X+Z,\qquad C=-Y+Z
\tag{8}
\]
over \(\mathbb F_p\).

### Corollary 3.1

Every \(p\)-entropic one-element extension of \(M(K_4)\) is \(\mathbb F_p\)-representable.

This follows immediately from Theorem 2.1.

For example, an odd-prime-entropic matroid cannot have an \(F_7\) minor. In the usual labeling, the extra Fano point must lie simultaneously in
\[
\operatorname{span}(x,c),\quad
\operatorname{span}(y,b),\quad
\operatorname{span}(z,a).
\]
With (8), the first two spaces intersect in the line spanned by \((1,-1,1)\). This line meets the third space nontrivially only in characteristic \(2\).

## 4. An exact obstruction for the dual Fano matroid

### Theorem 4.1

For every integer \(q\ge2\),
\[
F_7^*\text{ is }q\text{-entropic}
\quad\Longleftrightarrow\quad
q=2^m\text{ for some }m\ge1.
\]

### Proof

Use elements \(x,y,z,w,a,b,c\), with basis \(x,y,z,w\), and the following seven four-element circuits:
\[
\begin{array}{llll}
xyza,&xywb,&xzwc,&xabc,\\
zwab,&ywac,&yzbc.&
\end{array}
\tag{9}
\]
For instance, these are the circuits of the binary matrix with columns
\[
e_1,e_2,e_3,e_4,\;
e_1+e_2+e_3,\;
e_1+e_2+e_4,\;
e_1+e_3+e_4.
\]

Suppose there is a \(q\)-entropic realization. Condition on \(X=x_0\). The resulting matroid is \(M(K_4)\), with triangles
\[
yza,\quad ywb,\quad zwc,\quad abc.
\]
By (7), after fixed alphabet relabelings there is a group \(G\) of order \(q\) such that on this conditional slice,
\[
A=YZ,\qquad B=YW,\qquad C=Z^{-1}W.
\tag{10}
\]

We now use the three circuits in (9) avoiding \(x\).

The circuit \(zwab\) says that \(B\) is a function of \((Z,W,A)\). On the slice \(X=x_0\), this triple takes every value in \(G^3\), and (10) identifies the function. Consequently, globally,
\[
B=AZ^{-1}W.
\tag{11}
\]
The same argument applied to \(ywac\) gives
\[
C=A^{-1}YW.
\tag{12}
\]
Finally, \(yzbc\) gives
\[
BC^{-1}=YZ.
\tag{13}
\]

Substituting (11)–(12) into (13),
\[
A Z^{-1}Y^{-1}A=YZ.
\]
Writing \(u=YZ\), this is
\[
Au^{-1}A=u,
\qquad\text{or equivalently}\qquad
(u^{-1}A)^2=1.
\tag{14}
\]

For fixed \(Y,Z\), as \(X\) varies, \(A\) takes every value of \(G\). This follows from the circuit \(xyza\): its defining ternary quasigroup is bijective in \(X\). Therefore (14) says that every element of \(G\) has square \(1\).

A group of exponent \(2\) is abelian, hence is an elementary abelian \(2\)-group. Thus \(q=2^m\).

Conversely, the displayed binary matrix represents \(F_7^*\) over every field \(\mathbb F_{2^m}\). Uniformly sampling its input vector gives a \(2^m\)-entropic realization. ∎

This conditioning argument addresses a limitation identified in the previous attempt: here the group structure in one contraction fiber **does** propagate, because three circuit functions are completely determined on that fiber.

### Corollary 4.2

Every binary \(p\)-entropic matroid is \(\mathbb F_p\)-representable.

For \(p=2\), this is immediate. For odd \(p\), minor closure, Corollary 3.1, and Theorem 4.1 exclude \(F_7\) and \(F_7^*\) minors. By the standard excluded-minor characterization of regular binary matroids, the matroid is regular, and therefore representable over \(\mathbb F_p\).

## 5. Uniform matroids: elementary sharp bounds

For \(U_{r,n}\), formulation (1) is equivalent to a code
\[
C\subseteq Q^n,\qquad |C|=q^r,
\]
such that projection onto any \(r\) coordinates is bijective. Equivalently, distinct codewords have Hamming distance at least
\[
n-r+1.
\tag{15}
\]

### 5.1. Rank two and corank two

If \(U_{2,n}\) is \(q\)-entropic, fix a codeword \(c\). For each coordinate, exactly \(q-1\) other codewords agree with \(c\) there. Distinct codewords can agree in at most one coordinate. Therefore
\[
n(q-1)\le q^2-1,
\]
giving
\[
n\le q+1.
\tag{16}
\]

If \(U_{n-2,n}\) is \(q\)-entropic, its code has minimum distance at least \(3\). Its radius-one Hamming balls are disjoint, so
\[
q^{n-2}\bigl(1+n(q-1)\bigr)\le q^n.
\]
Again,
\[
n\le q+1.
\tag{17}
\]

### 5.2. Rank three over an odd alphabet

Suppose \(U_{3,n}\) is \(q\)-entropic. Contracting one element and applying (16) gives \(n\le q+2\).

Assume \(n=q+2\). Fix a codeword \(c\), and let \(A_i(c)\) count other codewords agreeing with \(c\) in exactly \(i\) coordinates. Only \(i=0,1,2\) are possible. Counting coordinate-pair agreements gives
\[
A_2(c)=\binom n2(q-1),
\]
while counting coordinate agreements gives
\[
A_1(c)+2A_2(c)=n(q^2-1).
\]
Consequently,
\[
A_1(c)=n(q-1)(q+2-n)=0.
\tag{18}
\]
Any two distinct codewords thus agree in either zero or two coordinates.

Let \(D\) be the binary incidence matrix whose rows are codewords and whose columns are coordinate-symbol pairs:
\[
D_{c,(i,a)}=\mathbf 1_{\{c_i=a\}}.
\]
If \(q\) is odd, then \(n=q+2\) is odd. Equation (18) gives, over \(\mathbb F_2\),
\[
DD^{\mathsf T}=I_{q^3}.
\]
Hence
\[
q^3\le nq=q(q+2),
\]
which is false for odd \(q\ge3\). Therefore
\[
\boxed{U_{3,n}\text{ \(q\)-entropic},\ q\text{ odd}
\ \Longrightarrow\ n\le q+1.}
\tag{19}
\]

### 5.3. Corank three over an odd alphabet

Suppose \(U_{n-3,n}\) is \(q\)-entropic. Its code has minimum distance at least \(4\). Puncturing one coordinate produces a length-\(n-1\) code of the same size and minimum distance at least \(3\). The Hamming bound gives
\[
n\le q+2.
\]

Suppose equality holds. Every singly punctured code is then a perfect radius-one code: its disjoint radius-one balls exactly fill \(Q^{q+1}\).

Relabel symbols so that \(0\in C\). Choose distinct coordinates \(j,k\), and a word \(w\) whose support is exactly \(\{j,k\}\).

For each \(i\notin\{j,k\}\), perfectness after puncturing \(i\) gives a unique \(c\in C\) whose puncturing is within distance one of the puncturing of \(w\). This \(c\) is not zero. Since \(d(c,0)\ge4\), necessarily
\[
\operatorname{supp}(c)=\{j,k,i,\ell\}
\]
for some \(\ell\notin\{j,k,i\}\), with \(c\) agreeing with \(w\) at \(j,k\).

The same codeword is the unique nearby codeword after puncturing \(\ell\). Thus \(i\mapsto\ell\) is a fixed-point-free involution on the \(n-2=q\) coordinates outside \(\{j,k\}\).

It follows that \(q\) is even. Therefore
\[
\boxed{U_{n-3,n}\text{ \(q\)-entropic},\ q\text{ odd}
\ \Longrightarrow\ n\le q+1.}
\tag{20}
\]

### 5.4. Consequences for prime alphabets

For prime \(p\), all uniform matroids \(U_{r,n}\) with \(n\le p+1\) are \(\mathbb F_p\)-representable. An explicit representation uses any \(n\) columns from
\[
(1,t,t^2,\ldots,t^{r-1})^{\mathsf T}\quad(t\in\mathbb F_p),
\qquad
(0,\ldots,0,1)^{\mathsf T}.
\tag{21}
\]
The requisite determinants are Vandermonde determinants. Uniform matroids of rank or corank at most one are representable over every field, with no length restriction.

Equations (16)–(20) therefore prove the conjecture for uniform matroids having rank or corank at most \(3\), for every odd prime. For \(p=2\), any uniform matroid with both rank and corank at least two has a \(U_{2,4}\) minor, contradicting (16).

Now let \(p\) be odd, and suppose \(U_{r,r+c}\) is \(p\)-entropic with \(r,c\ge3\). Contracting \(r-3\) elements and applying (19) gives
\[
c+3\le p+1,
\]
while deleting \(c-3\) elements and applying (20) gives
\[
r+3\le p+1.
\]
Hence
\[
r,c\le p-2.
\tag{22}
\]

For \(p=5\), if \(r,c\ge3\), equation (22) forces \(r=c=3\). If one of \(r,c\) equals two, (16) or (17) gives \(r+c\le6\). Thus every nontrivial uniform \(5\)-entropic matroid has at most six elements and is represented by (21).

This proves:

### Theorem 5.1

Every uniform \(5\)-entropic matroid is \(\mathbb F_5\)-representable. More precisely, for \(r,n-r\ge2\),
\[
U_{r,n}\text{ is \(5\)-entropic}\quad\Longleftrightarrow\quad n\le6.
\]

For an odd-prime uniform counterexample, (19)–(22) and (21) require
\[
4\le r,c\le p-2,\qquad r+c\ge p+2.
\]

## 6. Another sufficient condition: transitive coordinate symmetry

There is also a useful prime-specific linearization criterion.

### Proposition 6.1

Let \(C\subseteq Q^E\) have size \(p^r\), where \(|Q|=p\) is prime. Suppose a group of coordinatewise alphabet permutations preserves \(C\) and acts transitively on it. Then \(C\) is coordinatewise equivalent to an affine \(\mathbb F_p\)-linear code.

### Proof

Let \(G\) be the acting group and \(H\) a codeword stabilizer. Since
\[
[G:H]=p^r,
\]
a Sylow \(p\)-subgroup \(P\) containing a Sylow \(p\)-subgroup of \(H\) satisfies
\[
[P:P\cap H]=p^r.
\]
Thus \(P\) acts transitively on \(C\).

Each coordinate image of \(P\) is a \(p\)-subgroup of \(\operatorname{Sym}(p)\), so it is trivial or cyclic of order \(p\). Relabeling each nonconstant coordinate identifies its action with translations of \(\mathbb F_p\).

The image of \(P\) is consequently an additive subgroup
\[
W\le\mathbb F_p^E.
\]
Such a subgroup is an \(\mathbb F_p\)-subspace, and transitivity gives \(C=c+W\). ∎

In particular, prime-alphabet entropic realizations arising from uniform group-coset variables are linearizable: left multiplication supplies precisely this coordinatewise transitive action.

## 7. Why these arguments do not finish the conjecture

The main obstacle to induction is precise:

> Knowing that a deletion matroid is \(\mathbb F_p\)-representable does not imply that the given entropic realization of that deletion can be linearized.

This already fails at \(p=5\) for \(U_{2,3}\). Let \(X,Y\) be independent uniform symbols and let \(Z=f(X,Y)\), where \(f\) is the Latin square
\[
\begin{array}{c|ccccc}
 &0&1&2&3&4\\ \hline
0&0&1&2&3&4\\
1&1&0&3&4&2\\
2&2&3&4&0&1\\
3&3&4&1&2&0\\
4&4&2&0&1&3
\end{array}.
\]
Every pair among \(X,Y,Z\) is independent, and the triple has entropy \(2\log5\). This realizes \(U_{2,3}\).

However, the top-left \(2\times2\) subsquare is an intercalate:
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Intercalates are preserved by row, column, and symbol permutations. A Latin square \(ax+by\) over an odd-prime field, with \(a,b\ne0\), has no intercalate: the two repeated-symbol equations would force \(2a(x_1-x_2)=0\). Thus this realization is not coordinatewise equivalent to a linear one, even though its matroid is representable.

Accordingly:

- The Fourier lemma cannot be applied using representability of deletions alone.
- The dual-Fano argument propagates a conditional group structure through particular circuits; arbitrary matroids need not provide those circuits.
- The uniform bounds settle \(p=5\), but leave a nonempty parameter range for larger primes.
- Nonuniform, nonbinary matroids remain untreated in general, including at \(p=5\).

No computational search or independent literature verification is being claimed here. These are standalone partial proofs, not a resolution of the catalog conjecture.