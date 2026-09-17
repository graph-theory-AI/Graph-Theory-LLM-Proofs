```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I establish a unit-vector-flow construction using noncommuting rotations and prove that every bounded Borel map satisfying the second conjecture's identities must be linear.",
  "would_publish": false,
  "caveats": "The unrestricted first conjecture is not settled; the Borel obstruction does not address arbitrary maps, and novelty is not claimed."
}
```

# Partial results on unit-vector flows

I obtain two self-contained results:

1. An exact criterion for **equivariant \(S^2\)-flows on two-layer graphs over finite groups**, extending the previous construction beyond abelian groups.
2. A rigidity theorem showing that **no Borel-measurable map \(q\)** can satisfy the second conjecture. In fact, every bounded Borel function satisfying its identities is the restriction of a linear functional.

Neither result settles the unrestricted first conjecture. The supplied catalog reports an unrestricted refutation of the second conjecture; I have not independently verified that paper and do not use its reported conclusion below.

I checked the previous attempt’s character-counting lemma and conservation calculation: they are valid. The construction below recovers that argument, but also allows the two relevant rotations to have different axes.

## 1. Conventions

For an oriented graph, an \(S^2\)-flow assigns a unit vector \(\phi(e)\in\mathbb R^3\) to each edge so that
\[
\sum_{e\text{ leaving }v}\phi(e)
-
\sum_{e\text{ entering }v}\phi(e)=0
\]
at every vertex.

Parallel edges are allowed. Reversing an edge orientation and negating its vector does not change the underlying flow.

A graph admitting such a flow cannot have a bridge: summing the conservation equations over one side of a bridge would force its vector to be zero.

# Part I. A construction using noncommuting rotations

## 2. Two-layer graphs over a finite group

Let \(\Gamma\) be a finite group, with identity \(1\), and let \(s,t\in\Gamma\setminus\{1\}\).

Define \(G(\Gamma;s,t)\) on
\[
\{u_g,v_g:g\in\Gamma\}
\]
using the indexed, oriented edges
\[
e_g:u_g\longrightarrow u_{gs},\qquad
f_g:v_g\longrightarrow v_{gt},\qquad
m_g:u_g\longrightarrow v_g.
\]

Different indices designate different edges. In particular, an element of order two produces parallel edges in its layer. The graph is cubic, and it is simple when both \(s\) and \(t\) have order at least three.

Left multiplication by \(h\in\Gamma\) is an automorphism, taking every subscript \(g\) to \(hg\).

Let
\[
\rho:\Gamma\longrightarrow SO(3)
\]
be a homomorphism. Call a flow **\(\rho\)-equivariant** if
\[
\phi(e_{hg})=\rho(h)\phi(e_g),
\]
and likewise for the \(f\)- and \(m\)-edges.

### Theorem 1 — Exact equivariant criterion

Write \(\theta_s,\theta_t\in[0,\pi]\) for the principal rotation angles of \(\rho(s)\) and \(\rho(t)\). Then \(G(\Gamma;s,t)\) admits a \(\rho\)-equivariant \(S^2\)-flow if and only if
\[
\boxed{\theta_s\ge \frac{\pi}{3}
\quad\text{and}\quad
\theta_t\ge \frac{\pi}{3}.}
\]

The rotations need not commute and need not have a common axis.

### Proof

Put
\[
R_s=\rho(s),\qquad R_t=\rho(t).
\]
An equivariant assignment is determined by three unit vectors \(p,r,w\), via
\[
\phi(e_g)=\rho(g)p,\qquad
\phi(f_g)=\rho(g)r,\qquad
\phi(m_g)=\rho(g)w.
\]

The conservation equations become
\[
(I-R_s^{-1})p=-w,\qquad
(I-R_t^{-1})r=w. \tag{1}
\]

#### Necessity

For a rotation \(R\) through principal angle \(\theta\),
\[
\|I-R^{-1}\|_{\mathrm{op}}=2\sin(\theta/2).
\]
Thus the first equation of (1), with \(\|p\|=\|w\|=1\), implies
\[
1\le 2\sin(\theta_s/2).
\]
This is equivalent to \(\theta_s\ge\pi/3\). The argument for \(t\) is identical.

#### Sufficiency

Assume both angle inequalities hold. Choose unit axis vectors \(a_s,a_t\) for \(R_s,R_t\). There is a unit vector \(w\) perpendicular to both axes, since
\[
\dim(a_s^\perp\cap a_t^\perp)\ge 1.
\]
For nonparallel axes, one may take
\[
w=\frac{a_s\times a_t}{\|a_s\times a_t\|}.
\]

On \(a_s^\perp\), the map \(I-R_s^{-1}\) is invertible and multiplies lengths by
\[
\lambda_s=2\sin(\theta_s/2).
\]
Indeed, on that plane,
\[
\begin{aligned}
(I-R_s^{-1})^{\mathsf T}(I-R_s^{-1})
&=(I-R_s)(I-R_s^{-1})\\
&=2I-R_s-R_s^{-1}\\
&=4\sin^2(\theta_s/2)I.
\end{aligned}
\]
Define
\[
b_s=\left((I-R_s^{-1})|_{a_s^\perp}\right)^{-1}w.
\]
Then
\[
\|b_s\|=\lambda_s^{-1}\le 1.
\]
Define \(b_t\) and \(\lambda_t\) similarly.

Now set
\[
\boxed{
\begin{aligned}
p&=-b_s+\sqrt{1-\lambda_s^{-2}}\,a_s,\\
r&=\phantom{-}b_t+\sqrt{1-\lambda_t^{-2}}\,a_t.
\end{aligned}}
\tag{2}
\]
The two summands in each expression are perpendicular, so
\[
\|p\|=\|r\|=1.
\]
Also, \(I-R_s^{-1}\) annihilates \(a_s\), and similarly for \(t\). Consequently, (2) satisfies (1).

Finally, at \(u_g\),
\[
\begin{aligned}
\phi(e_g)-\phi(e_{gs^{-1}})+\phi(m_g)
&=\rho(g)\bigl(p-R_s^{-1}p+w\bigr)\\
&=0.
\end{aligned}
\]
At \(v_g\),
\[
\phi(f_g)-\phi(f_{gt^{-1}})-\phi(m_g)
=\rho(g)\bigl(r-R_t^{-1}r-w\bigr)=0.
\]
All assigned vectors are unit because every \(\rho(g)\) is orthogonal. This proves sufficiency. \(\square\)

For explicit calculations, if \(R\) is rotation through angle \(\theta\in(0,\pi]\) about the oriented unit axis \(a\), then for \(w\perp a\),
\[
\boxed{
\left((I-R^{-1})|_{a^\perp}\right)^{-1}w
=
\frac12\left(w-\cot(\theta/2)\,a\times w\right).
}
\tag{3}
\]

The construction also describes all equivariant solutions: choose any unit \(w\) perpendicular to both axes and allow either sign for each square-root term in (2).

## 3. Consequences

### 3.1. Polyhedral rotation groups

Let \(K\) be the rotation group of a regular tetrahedron, cube, or icosahedron. These groups are isomorphic to
\[
A_4,\qquad S_4,\qquad A_5,
\]
respectively.

Every nonidentity rotation in these groups has principal angle at least \(2\pi/5\), hence greater than \(\pi/3\). Theorem 1 therefore gives:

### Corollary 2

Suppose a finite group \(\Gamma\) has a homomorphism
\[
\pi:\Gamma\longrightarrow K,
\]
where \(K\) is one of the three polyhedral rotation groups above, and
\[
\pi(s)\ne 1,\qquad \pi(t)\ne 1.
\]
Then \(G(\Gamma;s,t)\) admits an \(S^2\)-flow.

In particular, this applies to every \(G(A_5;s,t)\) with \(s,t\ne1\).

This genuinely extends the *method* beyond one-dimensional characters: \(A_5\) has no nontrivial one-dimensional complex characters. It does not, by itself, establish novelty of the resulting graph family in the unit-flow literature.

### 3.2. An algebraically explicit icosahedral instance

Let
\[
\tau=\frac{1+\sqrt5}{2},
\]
and realize an icosahedron with vertex set
\[
\mathcal I=
\{(0,\pm1,\pm\tau),\;(\pm1,\pm\tau,0),\;(\pm\tau,0,\pm1)\}.
\]
Let \(\Gamma\) be its \(60\)-element rotation group.

Take \(s\) to be rotation through \(2\pi/3\) about
\[
a=\frac{(1,1,1)}{\sqrt3},
\]
and \(t\) to be rotation through \(2\pi/5\) about
\[
b=\frac{(0,1,\tau)}{\sqrt{\tau+2}}.
\]
Both preserve \(\mathcal I\). A unit vector perpendicular to their axes is
\[
w=\frac{(\tau-1,-\tau,1)}2.
\]
Indeed,
\[
(\tau-1)^2+\tau^2+1=4,
\]
and its dot products with both axes vanish.

Using (3), take
\[
\begin{aligned}
p&=-\frac12\left(w-\frac1{\sqrt3}a\times w\right)
    +\sqrt{\frac23}\,a,\\[2mm]
r&=\frac12\left(w-\cot(\pi/5)b\times w\right)
    +\sqrt{\frac{5-\sqrt5}{10}}\,b.
\end{aligned}
\]
Then
\[
\phi(e_g)=gp,\qquad
\phi(f_g)=gr,\qquad
\phi(m_g)=gw
\]
gives all edge vectors explicitly.

Here \(G(\Gamma;s,t)\) is a simple cubic graph on \(120\) vertices. All coordinates in the construction are algebraic.

### 3.3. Recovery of the abelian construction

For completeness, the previous attempt follows from Theorem 1 by making every rotation fix a common axis.

If \(A\) is finite abelian and \(x\in A\) has order \(k\), then a uniformly chosen character \(\chi\in\widehat A\) has \(\chi(x)\) uniformly distributed over the \(k\)-th roots of unity. The number satisfying
\[
|1-\chi(x)|\ge1
\]
is
\[
N(k)=k+1-2\left\lceil \frac{k}{6}\right\rceil.
\]
Thus
\[
N(2)=1,\qquad N(k)>\frac{k}{2}\quad(k\ge3).
\]
The latter inequality is immediate for \(3\le k\le6\); for \(k>6\), use
\[
N(k)>\frac{2k}{3}-1>\frac{k}{2}.
\]

Consequently, for nonzero \(s,t\in A\), there is a character satisfying
\[
|1-\chi(s)|\ge1,\qquad |1-\chi(t)|\ge1.
\]
If both elements have order two, choose a character of \(\langle s,t\rangle\) taking both to \(-1\), and extend it to \(A\). Character extension here is elementary: when adjoining an element \(x\) with least positive \(m\) such that \(mx\) lies in the existing subgroup, choose an \(m\)-th root of the prescribed value at \(mx\).

Letting \(\rho(g)\) rotate a fixed plane by multiplication by \(\chi(g)\) gives the hypotheses of Theorem 1. Hence every \(G(A;s,t)\), including every generalized Petersen graph, has an \(S^2\)-flow.

### 3.4. Graph covers

Every finite graph cover of a graph constructed above also has an \(S^2\)-flow. Orient lifted edges according to their images and pull back the vectors. The local bijection defining a graph cover preserves every conservation equation.

# Part II. A rigidity theorem for measurable maps \(q\)

## 4. Statement

Three distinct points \(x,y,z\in S^2\) are equidistant on a great circle precisely when
\[
x+y+z=0.
\]
Their pairwise inner products are then \(-1/2\).

### Theorem 3 — Borel rigidity

Let \(f:S^2\to\mathbb R\) be bounded and Borel measurable. Suppose
\[
f(-x)=-f(x)
\]
and
\[
f(x)+f(y)+f(z)=0
\quad\text{whenever }x+y+z=0,\qquad x,y,z\in S^2.
\]
Then there is a vector \(c\in\mathbb R^3\) such that
\[
\boxed{f(x)=c\cdot x\qquad\text{for every }x\in S^2.}
\]

In particular, no Borel-measurable map \(q\) in the second conjecture exists.

## 5. Proof by circular averaging

Fix \(n\in S^2\). Let \(R_n(\theta)\) denote rotation about the axis \(n\), and define
\[
\overline f_n(x)
=
\frac1{2\pi}\int_0^{2\pi} f(R_n(\theta)x)\,d\theta.
\]
Bounded Borel measurability makes this integral well defined for every \(x\).

The averaged function is invariant under rotations about \(n\), so
\[
\overline f_n(x)=F_n(n\cdot x)
\]
for a bounded function \(F_n:[-1,1]\to\mathbb R\). Moreover,
\[
F_n(-u)=-F_n(u),\qquad F_n(1)=f(n).
\]
Averaging the given identity shows that \(\overline f_n\) satisfies the same equilateral-triple identity.

We next prove
\[
F_n(u)=u f(n)\qquad(-1\le u\le1). \tag{4}
\]

### Which latitude triples are possible?

There are unit vectors \(x_1,x_2,x_3\) satisfying
\[
x_1+x_2+x_3=0,\qquad n\cdot x_i=u_i,
\]
if and only if
\[
u_1+u_2+u_3=0,\qquad
u_1^2+u_2^2+u_3^2\le\frac32. \tag{5}
\]

To see this, start with an equilateral triple \(p_1,p_2,p_3\) in a plane. For a vector \(v\) in that plane,
\[
\sum_{i=1}^3(v\cdot p_i)^2=\frac32\|v\|^2.
\]
The map \(v\mapsto(v\cdot p_1,v\cdot p_2,v\cdot p_3)\) maps the plane bijectively onto the subspace with coordinate sum zero. Thus (5) says exactly that the required planar projection of a unit axis has length at most one. Complete it by a perpendicular component and rotate the configuration to the prescribed axis \(n\).

It follows that
\[
F_n(s)+F_n(t)=F_n(s+t)
\]
whenever
\[
s^2+t^2+(s+t)^2\le\frac32. \tag{6}
\]
In particular, this holds whenever \(s,t,s+t\in[-1/2,1/2]\).

A bounded locally additive function is linear near zero. Here is the needed continuity argument: if \(|F_n|\le B\) and \(N|h|\le1/2\), repeated local additivity gives
\[
N F_n(h)=F_n(Nh),
\]
so
\[
|F_n(h)|\le \frac BN.
\]
Taking \(N=\lfloor1/(2|h|)\rfloor\) proves continuity at zero. Local additivity and rational approximation therefore give
\[
F_n(u)=a_nu\qquad(|u|\le1/2)
\]
for some \(a_n\).

For every \(|u|\le1\), the triple of latitudes
\[
u,\quad -u/2,\quad -u/2
\]
satisfies (5). Hence
\[
F_n(u)=2F_n(u/2)=a_nu.
\]
Evaluating at \(u=1\) gives \(a_n=f(n)\), proving (4).

### Recovering \(f\) from its first moment

Let \(\sigma\) be normalized surface-area measure on \(S^2\), and put
\[
c=3\int_{S^2} y f(y)\,d\sigma(y).
\]
Using spherical coordinates about \(n\), followed by (4),
\[
\begin{aligned}
n\cdot c
&=3\int_{S^2}(n\cdot y)f(y)\,d\sigma(y)\\
&=\frac32\int_{-1}^{1}uF_n(u)\,du\\
&=\frac32 f(n)\int_{-1}^{1}u^2\,du\\
&=f(n).
\end{aligned}
\]
This holds for every \(n\in S^2\), proving the theorem. \(\square\)

### Consequence for the proposed \(q\)

If a Borel map
\[
q:S^2\longrightarrow\{\pm1,\pm2,\pm3,\pm4\}
\]
satisfied the proposed identities, Theorem 3 would give \(q(x)=c\cdot x\).

If \(c=0\), this violates the prescribed range everywhere. If \(c\ne0\), it violates the range on the great circle \(c^\perp\cap S^2\). Thus no such Borel map exists.

The same argument excludes **every bounded, nowhere-zero Borel function** satisfying the two identities, regardless of its permitted range.

# 6. What remains unproved

There are two separate limitations.

1. **The graph construction is not universal.**  
   I have not reduced arbitrary bridgeless graphs to the two-layer graphs above or their covers. Furthermore, Theorem 1’s necessary angle condition applies only to flows equivariant under the specified representation. Failure of that condition is not an obstruction to an unrestricted \(S^2\)-flow.

2. **The original second conjecture imposes no measurability.**  
   A finite-valued function need not be Borel measurable. The averaging proof therefore does not furnish an unrestricted counterexample to the second conjecture and does not replace verification of the finite configurations reported in the catalog.

Thus the justified verdict is **partial**: a broader explicit construction for the first conjecture and a complete rigidity theorem for a regularity-restricted version of the second.