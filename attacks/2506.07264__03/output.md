```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "The conjecture holds for every connected graph of cycle rank at most two, with the explicit bicyclic bound s^+(G) >= n+5-2sqrt(5)>n.",
  "would_publish": false,
  "caveats": "Graphs with m>=n+2 remain unresolved, and the phase argument has not been independently refereed or checked against later literature."
}
```

# 1. Statement of the partial result

Write
\[
D(G):=s^+(G)-s^-(G).
\]
Since \(s^+(G)+s^-(G)=\operatorname{tr}A(G)^2=2m\),
\[
s^+(G)=m+\frac{D(G)}2. \tag{1}
\]

I prove the following.

### Theorem 1
Let \(G\) be a connected unicyclic graph, and let \(\ell\) be the length of its unique cycle.

1. If \(\ell\) is even, then \(G\) is bipartite and
   \[
   s^+(G)=n.
   \]
2. If \(\ell\equiv1\pmod4\), then
   \[
   n-\bigl(\sec(\pi/\ell)-1\bigr)\le s^+(G)<n.
   \]
3. If \(\ell\equiv3\pmod4\), then
   \[
   n<s^+(G)\le n+\bigl(\sec(\pi/\ell)-1\bigr).
   \]

Consequently, a connected unicyclic graph satisfies \(s^+(G)=n\) if and only if it is bipartite.

### Theorem 2
If \(G\) is connected and bicyclic, i.e. \(m=n+1\), then
\[
s^+(G)\ge n+5-2\sqrt5>n. \tag{2}
\]

Thus the conjecture is true for every connected graph with cycle rank
\[
m-n+1\le2.
\]
Indeed, a connected graph with \(m=n-1\) is a tree and has \(s^+=n-1\); the unicyclic case is covered by Theorem 1; and the bicyclic case is covered by Theorem 2. Therefore, any unresolved counterexample must be nonbipartite and satisfy
\[
m\ge n+2.
\]

I also prove at the end that the conjecture holds for every connected complete multipartite graph, regardless of its cycle rank.

---

# 2. A phase-integral formula for \(D(G)\)

Let \(A=A(G)\), with eigenvalues \(\lambda_1,\dots,\lambda_n\), and define
\[
q_G(t):=\det(tI+iA)=\prod_{j=1}^n(t+i\lambda_j),\qquad t>0.
\]
Choose the continuous argument
\[
\theta_G(t):=\sum_{j=1}^n\arctan\frac{\lambda_j}{t}.
\]
It satisfies \(\theta_G(t)\to0\) as \(t\to\infty\).

For a real number \(x\),
\[
x|x|=\frac2\pi\int_0^\infty \frac{x^3}{x^2+t^2}\,dt.
\]
Since \(\sum_j\lambda_j=\operatorname{tr}A=0\),
\[
\begin{aligned}
D(G)
 &=\frac2\pi\int_0^\infty
   \sum_j\frac{\lambda_j^3}{\lambda_j^2+t^2}\,dt\\
 &=-\frac2\pi\int_0^\infty
   t^2\sum_j\frac{\lambda_j}{\lambda_j^2+t^2}\,dt.
\end{aligned}
\]
On the other hand,
\[
\theta_G'(t)=-\sum_j\frac{\lambda_j}{t^2+\lambda_j^2}.
\]
Therefore
\[
D(G)=\frac2\pi\int_0^\infty t^2\theta_G'(t)\,dt.
\]
As \(t\to\infty\), the vanishing of \(\sum\lambda_j\) gives
\(\theta_G(t)=O(t^{-3})\), while \(\theta_G\) is bounded near zero. Integration by parts yields
\[
\boxed{\;
D(G)=-\frac4\pi\int_0^\infty t\,\theta_G(t)\,dt.
\;} \tag{3}
\]

Thus positive phase decreases \(s^+\), and negative phase increases it.

For a bipartite graph the spectrum is symmetric, so \(q_G(t)>0\), \(\theta_G(t)=0\), and \(D(G)=0\).

---

# 3. Unicyclic graphs

For a graph \(H\), let
\[
Z_H(t):=\sum_k m_k(H)t^{|V(H)|-2k},
\]
where \(m_k(H)\) is the number of \(k\)-edge matchings of \(H\). If
\[
\mu_H(x)=\sum_k(-1)^km_k(H)x^{|V(H)|-2k}
\]
is its matching polynomial, then
\[
\mu_H(it)=i^{|V(H)|}Z_H(t). \tag{4}
\]

Let \(G\) be unicyclic with unique cycle \(C\) of length \(\ell\). The permutation expansion of the characteristic polynomial gives
\[
\phi_G(x)=\mu_G(x)-2\mu_{G-V(C)}(x). \tag{5}
\]
Consequently,
\[
q_G(t)
 =Z_G(t)-2i^{-\ell}Z_{G-V(C)}(t). \tag{6}
\]

For odd \(\ell\), this becomes
\[
q_G(t)=
\begin{cases}
Z_G(t)+2iZ_{G-V(C)}(t),&\ell\equiv1\pmod4,\\[2mm]
Z_G(t)-2iZ_{G-V(C)}(t),&\ell\equiv3\pmod4.
\end{cases} \tag{7}
\]
Both matching-generating polynomials are strictly positive for \(t>0\). Hence
\[
\theta_G(t)>0\quad(\ell\equiv1\pmod4),\qquad
\theta_G(t)<0\quad(\ell\equiv3\pmod4). \tag{8}
\]
Equation (3) already proves that \(D(G)\ne0\), with the asserted sign.

## 3.1 Quantitative comparison with the bare cycle

Every matching consisting of a matching of \(C\) together with a matching of \(G-V(C)\) is a matching of \(G\). Hence, coefficientwise,
\[
Z_G(t)\ge Z_C(t)Z_{G-V(C)}(t).
\]
It follows from (7) that
\[
|\theta_G(t)|
 \le \delta_\ell(t):=\arctan\frac{2}{Z_{C_\ell}(t)}. \tag{9}
\]

For the bare odd cycle \(C_\ell\), equality holds in (9). Its eigenvalues are
\[
2\cos\frac{2\pi j}{\ell},\qquad 0\le j<\ell.
\]
A direct trigonometric sum gives
\[
s^+(C_\ell)=
\begin{cases}
\ell+1-\sec(\pi/\ell),&\ell\equiv1\pmod4,\\[1mm]
\ell-1+\sec(\pi/\ell),&\ell\equiv3\pmod4.
\end{cases} \tag{10}
\]
Since \(m(C_\ell)=\ell\),
\[
\frac4\pi\int_0^\infty t\,\delta_\ell(t)\,dt
 =2\bigl(\sec(\pi/\ell)-1\bigr). \tag{11}
\]
Combining (1), (3), (9), and (11) proves Theorem 1.

In particular, among cycles with length \(1\bmod4\), the largest possible negative contribution is attained at \(\ell=5\):
\[
2\bigl(\sec(\pi/5)-1\bigr)
 =2(\sqrt5-2). \tag{12}
\]

---

# 4. Sector language

For a fixed \(t>0\), associate to an odd cycle \(C_\ell\) the interval
\[
I_\ell(t)=
\begin{cases}
[0,\delta_\ell(t)],&\ell\equiv1\pmod4,\\
[-\delta_\ell(t),0],&\ell\equiv3\pmod4.
\end{cases}
\]
An even cycle contributes the interval \(\{0\}\).

Two elementary observations will be used repeatedly.

1. If nonzero complex numbers all have arguments in an interval of width less than \(\pi\), then every positive linear combination of them has argument in the same interval.

2. If \(U\) is unicyclic with odd cycle \(C_\ell\), then both \(q_U(t)\) and \(q_{U-v}(t)\), for every vertex \(v\), have arguments in \(I_\ell(t)\).  
   Indeed, if \(v\) lies on the cycle then \(U-v\) is a forest. Otherwise \(U-v\) has at most one unicyclic component, with the same cycle, together with forest components.

We also need two determinant identities.

### Bridge identity
If \(G\) is obtained from disjoint graphs \(X,Y\) by adding the bridge \(uv\), where \(u\in X,v\in Y\), then
\[
q_G=q_Xq_Y+q_{X-u}q_{Y-v}. \tag{13}
\]

### Coalescence identity
If \(G\) is obtained by identifying \(u\in X\) with \(v\in Y\), then
\[
q_G=q_Xq_{Y-v}+q_{X-u}q_Y-tq_{X-u}q_{Y-v}. \tag{14}
\]

Both follow directly from the standard vertex/bridge determinant expansions.

A final positivity fact is useful.

### Lemma 3
If \(B\) is bipartite and \(v\) is nonisolated, then
\[
q_B(t)>tq_{B-v}(t). \tag{15}
\]

#### Proof
Both quantities are positive. Jacobi's cofactor identity gives
\[
\frac{q_{B-v}}{q_B}=\bigl((tI+iA(B))^{-1}\bigr)_{vv}.
\]
Now
\[
(tI+iA)^{-1}=(tI-iA)(t^2I+A^2)^{-1}.
\]
Because \(B\) is bipartite, \(A(t^2I+A^2)^{-1}\) has zero diagonal. Therefore
\[
\bigl((tI+iA)^{-1}\bigr)_{vv}
 =t\bigl((t^2I+A^2)^{-1}\bigr)_{vv}<\frac1t,
\]
where strictness follows from \(v\) being nonisolated. This proves (15). \(\square\)

---

# 5. Bicyclic cores of cactus type

A connected bicyclic graph has, after repeatedly deleting leaves, one of three possible cores:

1. two vertex-disjoint cycles joined by a path;
2. two cycles sharing one vertex;
3. a theta graph, consisting of three internally disjoint paths with common endpoints.

First consider the first two types.

## 5.1 Two cycles joined by a path

Choose a bridge on the path between the cycles. Its deletion separates the graph into two unicyclic graphs \(U_1,U_2\). By (13),
\[
q_G=q_{U_1}q_{U_2}+q_{U_1-u}q_{U_2-v}.
\]
Each product has phase in
\[
I_{\ell_1}(t)+I_{\ell_2}(t).
\]
Since each \(\delta_{\ell_j}(t)<\pi/2\), this sum interval has width less than \(\pi\). The sector-convexity observation therefore shows that \(q_G\) has phase in the same interval.

## 5.2 Two cycles sharing a vertex

Let the two unicyclic pieces be \(U_1,U_2\), identified at a cycle vertex. Put
\[
a_j=q_{U_j-v_j}>0.
\]

If both cycles are odd, write
\[
q_{U_j}=M_j+iI_j,\qquad M_j>0.
\]
Equation (14) gives
\[
q_G=(M_1a_2+a_1M_2-ta_1a_2)
   +i(I_1a_2+a_1I_2). \tag{16}
\]
The matching recurrence at the identified cycle vertex gives
\[
M_j>ta_j.
\]
Thus the real part \(R\) in (16) satisfies
\[
R\ge M_1a_2,\qquad R\ge a_1M_2. \tag{17}
\]
Consequently, the positive contribution to \(I/R\) is at most
\[
\frac{(I_1)_+}{M_1}+\frac{(I_2)_+}{M_2}.
\]
Using
\[
\arctan(x+y)\le\arctan x+\arctan y\qquad(x,y\ge0),
\]
the phase of \(q_G\) lies in \(I_{\ell_1}+I_{\ell_2}\).

If one cycle is even, say \(U_2\) is bipartite, then (14) becomes
\[
q_G=a_2q_{U_1}+a_1(q_{U_2}-ta_2).
\]
The second term is positive by Lemma 3, so it pulls the phase of \(q_{U_1}\) toward zero. If both cycles are even, the whole graph is bipartite.

Thus all bicyclic cactus cores satisfy the required two-cycle sector bound.

---

# 6. Theta cores

Let the three internally disjoint paths have lengths \(r_1,r_2,r_3\). Put
\[
F_k(t):=Z_{P_k}(t),
\]
where \(P_k\) is the path on \(k\) vertices. Then
\[
F_0=1,\qquad F_1=t,\qquad F_k=tF_{k-1}+F_{k-2}. \tag{18}
\]

Eliminating the internal vertices of a path of length \(r\) in the matrix
\(tI+iA\) contributes
\[
a_r=
\begin{cases}
0,&r=1,\\[1mm]
\dfrac{F_{r-2}}{F_{r-1}},&r\ge2,
\end{cases}
\qquad
c_r=\frac{(-1)^r i^{\,r-2}}{F_{r-1}}. \tag{19}
\]
Thus \(c_r\) is real for even \(r\), purely imaginary for odd \(r\), and
\[
|c_r|=\frac1{F_{r-1}}.
\]

After all internal vertices are eliminated,
\[
q_\Theta(t)
 =\left(\prod_{j=1}^3F_{r_j-1}\right)(d^2-z^2), \tag{20}
\]
where
\[
d=t+\sum_j a_{r_j},\qquad z=\sum_j c_{r_j}. \tag{21}
\]
The prefactor in (20) is positive. It remains to control the phase of
\(d^2-z^2\).

If the theta graph is nonbipartite, exactly two of its three cycles are odd. There are two parity cases.

## 6.1 One odd path and two even paths

Write
\[
z=x_1+x_2+iy,
\]
where \(x_1,x_2\) arise from the even paths. Put
\[
d_0=t+a_{\rm odd}.
\]
For an even path,
\[
a_j\ge |x_j|,
\]
because \(F_{r_j-2}\ge1\). Set
\[
P_j=a_j+x_j,\qquad Q_j=a_j-x_j.
\]
These are nonnegative. For \(y>0\), factorization of \(d^2-z^2\) gives
\[
\theta_\Theta
 =f(P_1+P_2)-f(Q_1+Q_2),\qquad
f(s)=\arctan\frac{y}{d_0+s}. \tag{22}
\]
The phase of the odd cycle formed from the odd path and even path \(j\) is
\[
\theta_j=f(P_j)-f(Q_j). \tag{23}
\]

Here \(f\) is decreasing and \(-f'\) is nonnegative and decreasing. An interval-packing argument gives
\[
(\theta_\Theta)_+\le(\theta_1)_++(\theta_2)_+, \tag{24}
\]
and, after interchanging \(P_j,Q_j\),
\[
(-\theta_\Theta)_+\le(-\theta_1)_++(-\theta_2)_+. \tag{25}
\]
For completeness, when \(\sum P_j<\sum Q_j\),
\[
f\Bigl(\sum P_j\Bigr)-f\Bigl(\sum Q_j\Bigr)
 =\int_{\sum P_j}^{\sum Q_j}(-f'(s))\,ds.
\]
Discarding indices with \(P_j\ge Q_j\) can only enlarge this integral, and the remaining interval can be partitioned into pieces shifted no farther left than the intervals \([P_j,Q_j]\). Since \(-f'\) is decreasing, (24) follows. The other inequalities are analogous.

Thus the theta phase lies between the sums of the negative and positive phases of its two odd cycles.

## 6.2 One even path and two odd paths

Write
\[
z=x+i(y_1+y_2).
\]
Replacing simultaneously \(x,y_1,y_2\) by their negatives does not change \(z^2\), so assume \(x>0\). Put
\[
D_0=t+a_{\rm even}.
\]
For \(D>x\) and \(Y\ge0\), define
\[
K_D(Y):=
 \arctan\frac{Y}{D-x}
 -\arctan\frac{Y}{D+x}. \tag{26}
\]
If \(y_1+y_2<0\), the positive theta phase is
\[
K_{D_0+a_1+a_2}(-y_1-y_2). \tag{27}
\]
The positive phase of the odd cycle using odd path \(j\) is
\[
K_{D_0+a_j}(|y_j|)
\]
when \(y_j<0\).

We use three elementary properties:

1. \(K_D(Y)\) decreases with \(D\).
2. \(K_D\) is subadditive:
   \[
   K_D(Y_1+Y_2)\le K_D(Y_1)+K_D(Y_2). \tag{28}
   \]
   Indeed,
   \[
   K_D(Y)=\int_{D-x}^{D+x}\frac{Y}{s^2+Y^2}\,ds,
   \]
   and \(Y/(s^2+Y^2)\) is subadditive in \(Y\). A direct calculation gives
   \[
   \frac{a}{s^2+a^2}+\frac{b}{s^2+b^2}
   -\frac{a+b}{s^2+(a+b)^2}\ge0.
   \]
3. \(K_D(Y)\) is increasing for \(0\le Y\le1\) whenever
   \(D^2-x^2>1\). Indeed,
   \[
   \frac{\partial K_D}{\partial Y}
   =
   \frac{2x(D^2-x^2-Y^2)}
   {((D-x)^2+Y^2)((D+x)^2+Y^2)}. \tag{29}
   \]

For an odd path,
\[
|y_j|=\frac1{F_{r_j-1}}\le1.
\]
Moreover, for the even path of length \(e\),
\[
D_0^2-x^2=\frac{F_{e+1}}{F_{e-1}}>1. \tag{30}
\]
This follows either from the path Schur complement or from the recurrence (18).

If both \(y_j\) have the sign producing positive phase, (28) and monotonicity in \(D\) bound the theta phase by the sum of the two odd-cycle phases. If only one has that sign and the total phase remains positive, then cancellation gives a resulting magnitude at most \(1\); properties 1 and 3 bound it by the phase of that one cycle. Applying the same argument after complex conjugation gives the lower bound.

Therefore every nonbipartite theta core has phase in the sum of the sectors associated with its two odd cycles.

---

# 7. Reattaching trees

It remains to justify that pendant trees cannot move the phase outside the same sector.

Suppose every induced subgraph of \(H\) has \(q\)-phase in a fixed interval \(I\) of width less than \(\pi\). Add a new leaf \(w\) adjacent to \(u\). For any induced subgraph containing both \(u,w\), the leaf recurrence gives
\[
q_{K+w}=tq_K+q_{K-u}. \tag{31}
\]
Both summands have phase in \(I\), so their positive linear combination does as well. If \(u\) is absent, \(w\) is isolated and only contributes a positive factor \(t\). Hence the hereditary sector property is preserved when a leaf is added.

For each bare bicyclic core considered above, every proper induced subgraph has at most unicyclic components, whose cycles are among the two core odd cycles:

- removing a vertex from a theta core leaves at most one cycle;
- removing a vertex from a figure-eight or dumbbell core leaves at most the two original cycles in separate unicyclic components.

Thus every induced subgraph of the bare core lies in the same two-cycle sector. Repeatedly applying (31) reattaches all trees.

We have therefore proved that for every connected bicyclic graph,
\[
\theta_G(t)
 \le \sum_{\substack{C\text{ one of the at most two}\\
                     \text{core odd cycles}\\
                     |C|\equiv1\pmod4}}
       \delta_{|C|}(t). \tag{32}
\]

---

# 8. Proof of the explicit bicyclic bound

Every cycle with length \(1\bmod4\) has length at least \(5\). From (11) and (12),
\[
\frac4\pi\int_0^\infty t\,\delta_\ell(t)\,dt
 \le 2(\sqrt5-2).
\]
There are at most two such core cycles. Equations (3) and (32) therefore give
\[
D(G)\ge-4(\sqrt5-2)=8-4\sqrt5. \tag{33}
\]
Since \(m=n+1\), equation (1) yields
\[
\begin{aligned}
s^+(G)
 &\ge n+1+\frac{8-4\sqrt5}{2}\\
 &=n+5-2\sqrt5\\
 &>n.
\end{aligned}
\]
This proves Theorem 2.

---

# 9. A separate arbitrary-density case: complete multipartite graphs

Let
\[
G=K_{n_1,\dots,n_r},\qquad n=\sum_i n_i,
\]
be connected, so \(r\ge2\).

The adjacency quadratic form on the part-constant subspace is a rank-one positive form minus a positive diagonal form, so \(G\) has exactly one positive eigenvalue, its Perron root \(\rho\). Hence
\[
s^+(G)=\rho^2.
\]
The Perron equations give
\[
\sum_{i=1}^r\frac{n_i}{\rho+n_i}=1. \tag{34}
\]

If \(r\ge3\), let \(x=\sqrt n\). The function
\[
a\longmapsto \frac{a}{x+a}
\]
is increasing and concave, and splitting a positive integer part strictly increases the sum. Thus among partitions of \(n\) into at least three positive parts, the minimum of
\[
\sum_i\frac{n_i}{x+n_i}
\]
is attained at \((1,1,n-2)\). At this partition,
\[
\begin{aligned}
\frac2{x+1}+\frac{n-2}{x+n-2}-1
 &=\frac2{x+1}-\frac{x}{x+n-2}\\
 &=\frac{x+n-4}{(x+1)(x+n-2)}>0.
\end{aligned}
\]
Since the left side of (34) is strictly decreasing in \(\rho\), it follows that
\[
\rho>\sqrt n,
\]
and hence \(s^+(G)>n\).

If \(r=2\), then \(G=K_{a,b}\) and
\[
s^+(G)=ab.
\]
Thus \(s^+(G)=a+b\) precisely when
\[
(a-1)(b-1)=1,
\]
so \(a=b=2\). Therefore \(C_4\) is the only connected complete multipartite graph satisfying \(s^+=n\), and it is bipartite unicyclic.

---

# 10. What remains open

The argument proves the conjecture when
\[
m\le n+1
\]
and for complete multipartite graphs. It does not cover general connected graphs with
\[
m\ge n+2.
\]

The obstruction to extending the method directly is structural. With three or more independent cycles:

- the relevant phase sectors can have total width at least \(\pi\), so positive sums need not remain in one convex sector;
- collections of vertex-disjoint cycles contribute product terms to the characteristic polynomial;
- cores can have many overlapping cycles not controlled by only two fundamental odd-cycle phases.

Thus the full conjecture remains unresolved, but any counterexample must be a nonbipartite graph with cycle rank at least three and cannot be complete multipartite.