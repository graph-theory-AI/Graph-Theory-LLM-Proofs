```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Two cops force one fixed cop's distance to tend to zero on every smooth monotone polar double, a class containing variable-curvature spheres.",
  "would_publish": false,
  "caveats": "Special geometric hypotheses only; arbitrary surfaces and finite-time exact capture are not settled, and novelty of the special case has not been checked."
}
```

## 1. Scope and statement of the partial result

I set aside the previous tiny-sphere counterexample as a resolution of the intended question. Instead, I give a positive, scale-invariant special case, with an explicit convergence strategy.

Players follow \(1\)-Lipschitz paths. A nonanticipative cop strategy assigns cop paths to each robber path using only the robber’s history. The result below forces more than arbitrarily close encounters: along every play, one fixed member of the two-cop team has distance tending to zero.

### The geometric class

Let \(H>0\). Suppose a smooth closed Riemannian surface \(M\) has coordinates
\[
(s,\theta)\in(0,2H)\times \mathbb S^1
\]
away from two poles \(N,S\), with metric
\[
g=ds^2+F(s,\theta)^2\,d\theta^2.
\]
The circles \(s=0\) and \(s=2H\) are collapsed to \(N\) and \(S\), respectively, and the metric is assumed to extend smoothly over both poles.

Assume:

1. **Equatorial reflection:**
   \[
   F(2H-s,\theta)=F(s,\theta).
   \]
2. **Strict radial monotonicity:** for each \(\theta\), the function
   \[
   s\longmapsto F(s,\theta)
   \]
   is strictly increasing on \([0,H]\).

Call such a surface a **monotone polar double**. This terminology is used only for this writeup.

The class includes round spheres and all spheroids—prolate or oblate ellipsoids of revolution—with their induced Riemannian metrics. It also permits angular dependence in \(F\), as illustrated below.

### Theorem

On every monotone polar double, two cops have a nonanticipative strategy such that, for every legal robber path, either there is a finite-time collision or there is an index \(i\in\{1,2\}\) satisfying
\[
\lim_{t\to\infty}d(C_i(t),R(t))=0.
\]

The index may depend on the play, but is fixed throughout the asserted limit.

Consequently, on this class, any team containing at least two cops can achieve convergence, without needing the radius-\(\tfrac12\) winning hypothesis.

---

## 2. The two-cop strategy

Place one cop at each pole. If the robber starts at a pole, there is immediate capture. Otherwise write its coordinates as
\[
R(t)=(s(t),\theta(t)),
\]
and set
\[
q(t)=\min\{s(t),2H-s(t)\}.
\]

Before capture, use a continuous lift of the angular coordinate along the robber’s path. Define a nondecreasing scalar \(x(t)\), starting at \(x(0)=0\), and place the cops at
\[
C_1(t)=(x(t),\theta(t)),\qquad
C_2(t)=(2H-x(t),\theta(t)).
\]
Thus both cops remain on the robber’s current meridian.

Until the first time \(x(t)=q(t)\), prescribe
\[
\dot x(t)
=
\sqrt{\,1-F(x(t),\theta(t))^2\dot\theta(t)^2\,}.
\tag{1}
\]

The first equality \(x=q\) is an exact collision with one of the cops.

### Legality

Before collision,
\[
0\le x(t)<q(t)\le H.
\]
By reflection symmetry and monotonicity,
\[
F(x(t),\theta(t))
<
F(q(t),\theta(t))
=
F(s(t),\theta(t)).
\tag{2}
\]
The robber’s speed constraint says, almost everywhere,
\[
\dot s(t)^2+
F(s(t),\theta(t))^2\dot\theta(t)^2
\le 1.
\tag{3}
\]
In particular, the square root in (1) is well-defined.

Both cops have speed exactly \(1\) almost everywhere before collision:
\[
|\dot C_1|^2
=\dot x^2+F(x,\theta)^2\dot\theta^2
=1,
\]
and reflection symmetry gives the same calculation for \(C_2\).

On every compact time interval before collision, the robber stays away from the poles, and the radicand in (1) is locally bounded away from zero. Standard local ODE existence and uniqueness therefore applies. The construction continues until collision or for all time. A finite endpoint where the robber reaches a pole is also covered by continuity of \(x\le q\).

The appearance of \(\dot\theta\) does not introduce anticipation. It is determined almost everywhere by the observed angular history. Equivalently, (1) defines a nonanticipative path functional: two robber paths agreeing up to time \(T\) produce identical cop paths up to time \(T\).

---

## 3. Proof of convergence

Assume there is no finite-time collision.

### Radial progress dominates the robber’s radial motion

Equations (1)–(3) imply
\[
\dot x^2
=
1-F(x,\theta)^2\dot\theta^2
\ge
1-F(s,\theta)^2\dot\theta^2
\ge
\dot s^2.
\]
Hence
\[
\dot x\ge |\dot s|
\qquad\text{almost everywhere}.
\tag{4}
\]

Define the radial gap
\[
b(t)=q(t)-x(t)>0.
\]
The function \(q\) is absolutely continuous, with
\[
|\dot q|\le |\dot s|
\]
almost everywhere. Consequently,
\[
\dot b=\dot q-\dot x\le 0.
\tag{5}
\]
Thus \(b\) is nonincreasing.

The cops’ distance from the robber is controlled by this gap:
\[
\min_{i=1,2}d(C_i(t),R(t))\le b(t),
\tag{6}
\]
because a segment of their common meridian joins the robber to the nearer cop and has length \(b(t)\).

### A positive limiting gap is impossible

For \(0<\varepsilon<H\), define
\[
\eta_\varepsilon
=
\min_{\substack{\theta\in\mathbb S^1\\0\le u\le H-\varepsilon}}
\left[
1-
\frac{F(u,\theta)^2}{F(u+\varepsilon,\theta)^2}
\right].
\tag{7}
\]
Strict monotonicity makes the expression positive everywhere on its compact parameter set. Its denominator never vanishes there. Therefore
\[
\eta_\varepsilon>0.
\]

Whenever \(b(t)\ge\varepsilon\), we have \(q(t)\ge x(t)+\varepsilon\), so
\[
\begin{aligned}
\dot x(t)^2
&=1-F(x(t),\theta(t))^2\dot\theta(t)^2\\
&\ge
1-\frac{F(x(t),\theta(t))^2}
        {F(q(t),\theta(t))^2}\\
&\ge\eta_\varepsilon.
\end{aligned}
\tag{8}
\]
A gap at least \(\varepsilon\) forever would therefore make \(x(t)\) grow at least linearly, contradicting \(x(t)\le H\).

Together with (5), this proves
\[
b(t)\longrightarrow 0.
\tag{9}
\]
It also gives a quantitative bound: by time
\[
T_\varepsilon=\frac{H}{\sqrt{\eta_\varepsilon}},
\tag{10}
\]
the gap is at most \(\varepsilon\), and remains at most \(\varepsilon\) thereafter.

### One fixed cop converges

It remains to justify that the cops need not alternate indefinitely as the only close cop.

Since \(x\) is nondecreasing and bounded, it has a limit \(x_\infty\). By (4),
\[
\int_0^\infty |\dot s(t)|\,dt
\le
\int_0^\infty \dot x(t)\,dt
=x_\infty\le H.
\]
Thus the robber’s meridional coordinate has a limit \(s_\infty\).

Equation (9) now gives
\[
x_\infty=\min\{s_\infty,2H-s_\infty\}.
\]

If \(s_\infty\le H\), then
\[
d(C_1(t),R(t))
\le |s(t)-x(t)|
\longrightarrow 0.
\]
If \(s_\infty\ge H\), the corresponding inequality for \(C_2\) gives convergence. When \(s_\infty=H\), both cops converge to the robber in distance.

This proves the theorem. If a finite collision occurs instead, the colliding cop may thereafter follow the robber’s path exactly.

---

## 4. A delayed implementation for arbitrary proximity

Continuous-time strategy conventions are a genuine issue in this problem. The weaker conclusion—arbitrarily close encounters—can also be implemented using delayed observations, rather than instantaneous angular tracking.

Choose \(\varepsilon_n\downarrow0\), with \(0<\varepsilon_n<H\). At the beginning \(T_n\) of phase \(n\), put the cops at the poles and feed the preceding strategy the virtual robber
\[
V_n(u)=R\bigl(T_n+\max\{u-\varepsilon_n,0\}\bigr),
\qquad u\ge0.
\]
This is a legal \(1\)-Lipschitz path, and
\[
d\bigl(V_n(u),R(T_n+u)\bigr)\le\varepsilon_n.
\]

Run the strategy for the finite time in (10), with tolerance \(\varepsilon_n\). At the end of the phase, some cop is within \(2\varepsilon_n\) of the actual robber. Then return the cops to the poles and start the next phase. These relocations take finite time because \(M\) is compact.

During each phase, the response uses a fixed initial observation followed by observations delayed by \(\varepsilon_n\). Thus plays can be constructed successively without simultaneous-reaction ambiguities. Since there are only two cops, one fixed cop is within \(2\varepsilon_n\) along an infinite subsequence of phases.

This delayed implementation proves arbitrary proximity. The unphased strategy above proves the stronger full-time limit in the nonanticipative path-strategy formulation.

---

## 5. Relation to the fixed-radius question

There is an elementary lower bound that makes this a genuine special case of the strategy-strengthening implication under an injectivity-radius normalization.

### Lemma: one-cop evasion below the injectivity radius

Let \(M\) be any compact closed Riemannian manifold. Under the usual cops-first placement convention, one cop cannot force radius-\(r\) capture when
\[
0<r<\operatorname{inj}(M).
\]

#### Proof

Choose numbers \(\rho,h>0\) such that
\[
r<\rho,\qquad \rho+2h<\operatorname{inj}(M).
\]
The robber starts at distance \(\rho\) from the cop.

At each time \(nh\), let the current separation be \(d_n\).

* If \(d_n\le\rho+h\), the robber follows, for time \(h\), the unit-speed extension away from the cop of the minimizing cop-to-robber geodesic. Its total length from the cop’s position at time \(nh\) is at most
  \[
  d_n+h\le\rho+2h<\operatorname{inj}(M),
  \]
  so this extension remains minimizing. At intermediate time \(nh+u\),
  \[
  d(C(nh+u),R(nh+u))
  \ge (d_n+u)-u=d_n.
  \]

* If \(d_n>\rho+h\), the robber waits. Throughout the interval,
  \[
  d(C(nh+u),R(nh+u))
  \ge d_n-u>\rho.
  \]

Induction gives separation at least \(\rho>r\) for all time. The strategy only uses observations at the interval beginnings. \(\square\)

In particular, one cop cannot force arbitrary proximity on any compact closed Riemannian surface. Therefore the minimum number of cops forcing convergence on a monotone polar double is exactly two.

Now suppose a monotone polar double satisfies
\[
\operatorname{inj}(M)>\tfrac12.
\]
Any team winning the radius-\(\tfrac12\) game must contain at least two cops. The theorem then supplies a convergence strategy using two members of that same team; additional cops may remain idle. Arbitrary initial cop positions cause no difficulty: the two designated cops first move to the poles.

Thus **the proposed strengthening holds for every winning team on injectivity-normalized monotone polar doubles**.

---

## 6. Breadth of the class and remaining gap

The hypotheses are not restricted to constant curvature or even to an angularly independent metric coefficient.

For example, take \(H=\pi/2\), choose a nonzero smooth function \(h\) satisfying
\[
h(\pi-s)=h(s)
\]
and supported in
\[
(\pi/6,\pi/3)\cup(2\pi/3,5\pi/6),
\]
and put
\[
F(s,\theta)=\sin s+\delta h(s)\cos(2\theta).
\]
For sufficiently small nonzero \(\delta\):

* the metric is exactly round near the poles, hence extends smoothly there;
* reflection symmetry holds;
* \(F_s>0\) on \(0<s<\pi/2\);
* the curvature is nonconstant.

These give smooth variable-curvature examples covered by the theorem. Rescaling preserves the hypotheses and the convergence conclusion, so the result does not depend on making the entire surface smaller than the capture radius.

The unresolved step is substantial: an arbitrary Riemannian surface need not possess these global meridians, the equatorial reflection, or the monotonicity that makes angular tracking affordable for both cops. A radius-\(\tfrac12\) winning strategy does not, by itself, provide any of them. The argument therefore does not establish the general upgrade, and it does not force finite-time exact collision.

I make no novelty claim for this special case; the contribution here is the self-contained strategy and its proof.