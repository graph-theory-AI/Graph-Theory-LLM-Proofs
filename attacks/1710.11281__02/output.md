```json
{
  "verdict": "disproved",
  "confidence": "medium",
  "one_line": "Under the literal equal-speed continuous-time interpretation, a sufficiently small round sphere is caught trivially within radius 1/2, while an antipodal delayed-shadowing strategy keeps the robber a fixed positive distance from one cop forever.",
  "would_publish": false,
  "caveats": "This addresses the same-team, unnormalized continuous-time formulation; a normalized or turn-based version may remain open."
}
```

## Statement made precise

Consider the standard continuous-time pursuit game on a closed Riemannian surface \(M\):

- each player follows a \(1\)-Lipschitz path;
- the cop chooses its initial position first;
- the robber observes the cop continuously and may use a causal strategy;
- radius-\(\frac12\) capture means that \(d(C(t),R(t))<\frac12\) for some \(t\);
- “arbitrarily close” means
  \[
  \inf_{t\ge 0} d(C(t),R(t))=0.
  \]

Under this interpretation, the proposed implication is false, already for one cop on a round sphere.

## Delayed-shadowing lemma

Let \(X\) be a metric space with an isometry \(A\) satisfying
\[
d(x,A(x))=D>0\qquad\text{for every }x\in X.
\]
Thus \(A\) is a fixed-point-free constant-displacement isometry.

Given any \(1\)-Lipschitz cop path \(C:[0,\infty)\to X\), fix \(0<\tau<D\) and define
\[
R(t)=
\begin{cases}
A(C(0)),&0\le t\le \tau,\\[2mm]
A(C(t-\tau)),&t\ge \tau.
\end{cases}
\]

This is a legal \(1\)-Lipschitz robber path. Indeed, after time \(\tau\) it is an isometric copy of the cop's earlier path, and the two pieces agree at \(t=\tau\). For \(0\le t\le \tau\),
\[
d(C(t),R(t))
=d(C(t),A(C(0)))
\ge D-d(C(t),C(0))
\ge D-\tau.
\]
For \(t\ge\tau\),
\[
\begin{aligned}
d(C(t),R(t))
&=d(C(t),A(C(t-\tau)))\\
&\ge d(C(t),A(C(t)))
   -d(A(C(t)),A(C(t-\tau)))\\
&=D-d(C(t),C(t-\tau))\\
&\ge D-\tau.
\end{aligned}
\]
Consequently,
\[
d(C(t),R(t))\ge D-\tau>0
\qquad\text{for every }t\ge0.
\]

Importantly, this robber strategy uses only the cop's position at time \(t-\tau\). It is therefore causal with a strict positive delay and does not require knowledge of the cop's future or instantaneous velocity. Against a causal cop strategy, the resulting play can be constructed successively on intervals of length \(\tau\).

## Counterexample

Let \(M\) be the round sphere of radius
\[
\rho=\frac{1}{4\pi}.
\]
Its intrinsic diameter is
\[
D=\pi\rho=\frac14<\frac12.
\]

### Radius-\(\frac12\) capture

For every two points \(x,y\in M\),
\[
d(x,y)\le \operatorname{diam}(M)=\frac14<\frac12.
\]
Thus one cop wins the radius-\(\frac12\) game trivially: the robber is within capture distance at the initial time, and indeed at every later time, irrespective of either player's motion.

### Failure of arbitrary proximity

Let \(A\) be the antipodal map. It is an isometry and
\[
d(x,A(x))=D=\frac14
\]
for every \(x\in M\).

Apply the delayed-shadowing lemma with
\[
\tau=\frac{D}{2}=\frac18.
\]
Against every possible cop path, the robber has a causal legal strategy satisfying
\[
d(C(t),R(t))\ge D-\tau=\frac18
\qquad\text{for all }t\ge0.
\]
Hence one cop cannot force even distance below \(1/8\), and therefore cannot force arbitrary proximity or an exact collision.

Thus, writing \(c_{1/2}(M)\) for the radius-\(\frac12\) cop number and \(c_{\mathrm{prox}}(M)\) for the minimum number forcing arbitrarily small distance,
\[
c_{1/2}(M)=1
\qquad\text{but}\qquad
c_{\mathrm{prox}}(M)\ge2.
\]

This disproves the same-number implication in the literal unnormalized formulation.

## Scope and remaining gap

The counterexample exploits the mismatch between two notions:

- capture at a fixed positive radius is sensitive to rescaling the metric;
- the qualitative ability of an equal-speed robber to shadow an antipodal pursuer is preserved by rescaling.

Accordingly, a nontrivial repaired question would need additional hypotheses, for example a curvature, diameter, injectivity-radius, or movement-scale normalization. The argument also does not address interpretations in which:

1. additional cops may be introduced for the convergence objective;
2. play is turn-based and a cop may move to the robber's currently stationary position;
3. “after capture” the robber is required to stop, in which case exact occupation is tautological.

Those differently formalized versions may remain open.