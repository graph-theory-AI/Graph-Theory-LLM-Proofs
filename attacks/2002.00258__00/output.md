```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "The quoted belief has no fixed quantifiers or specified hopper variant, although the natural strong-hopper reading forces a rigid two-unit genus-jump configuration.",
  "would_publish": false,
  "caveats": "The conditional reductions below do not decide existence under the source paper's intended conventions."
}
```

# 1. Status of the statement

The sentence

> “Hoppers may show up when the Euler genus is large enough”

is not, literally, a proposition with a truth value. Even after importing a definition of hopper from the source, at least the following inequivalent formulations are possible:

\[
\begin{aligned}
(E_1)&\qquad \exists k\quad \mathcal H_k\neq\varnothing;\\
(E_2)&\qquad \forall K\ \exists k\ge K\quad \mathcal H_k\neq\varnothing;\\
(E_3)&\qquad \exists K\ \forall k\ge K\quad \mathcal H_k\neq\varnothing.
\end{aligned}
\]

Thus \(E_3\Rightarrow E_2\Rightarrow E_1\), but the converses need not hold, especially if hoppers are required to be 3-connected. It is also necessary to specify:

- whether “hopper” means a \(\widehat g\)-hopper or the dual \(\widehat g^+\)-hopper;
- whether weak hoppers are included;
- whether the level is \(\widehat g(G)\), \(\widehat g(G^+)\), or the genus of the obstruction assembled from the hopper;
- whether 3-connectivity is part of the definition.

Accordingly, the catalog sentence cannot presently be proved or disproved as written. The rest of this writeup treats the most natural strong-hopper formulation and derives exact necessary conditions.

# 2. Parameter setup

Let \(G\) be a finite graph with distinct nonadjacent roots \(x,y\), and put

\[
G^+=G+xy.
\]

Write \(\widehat g(G)\) for the Euler genus and define

\[
\theta(G)=\widehat g(G^+)-\widehat g(G).
\]

For every rooted minor operation \(\mu\) consisting of one edge deletion or contraction, set

\[
d_\mu=\widehat g(G)-\widehat g(\mu G),
\qquad
d_\mu^+=\widehat g(G^+)-\widehat g((\mu G)^+).
\]

Minor monotonicity gives \(d_\mu,d_\mu^+\ge 0\).

Two elementary facts will be used repeatedly.

### Lemma 2.1

For every rooted graph \(H\),

\[
0\le \theta(H)\le 2.
\]

Moreover,

\[
d_\mu^+-d_\mu=\theta(G)-\theta(\mu G).
\tag{2.1}
\]

#### Proof

The lower bound follows from \(H\subseteq H^+\). Given a minimum-genus embedding of \(H\), one can attach an orientable handle between suitable small neighborhoods of \(x\) and \(y\) and draw the new edge through it. This increases Euler genus by two, proving the upper bound.

The identity is algebraic:

\[
\begin{aligned}
d_\mu^+-d_\mu
&=\bigl(\widehat g(G^+)-\widehat g((\mu G)^+)\bigr)
 -\bigl(\widehat g(G)-\widehat g(\mu G)\bigr)\\
&=\theta(G)-\theta(\mu G).
\end{aligned}
\]

\(\square\)

# 3. The strong \(\widehat g\)-hopper condition

The natural strong condition is

\[
\mathcal M(G)
=
\Delta_1(\widehat g^+,G)\cup \Delta_2(\widehat g,G),
\tag{H1}
\]

together with

\[
\mathcal M(G)\setminus \Delta_1(\widehat g^+,G)\neq\varnothing.
\tag{H2}
\]

In terms of the drops, this says:

1. for every \(\mu\), either \(d_\mu^+\ge1\) or \(d_\mu\ge2\);
2. for at least one \(\mu\), \(d_\mu^+=0\).

The second condition distinguishes a genuine hopper from a graph that is simply \(\widehat g^+\)-critical.

## Proposition 3.1: rigid transition structure

If \(G\) satisfies (H1)–(H2), then:

1. \(\theta(G)=0\), so
   \[
   \widehat g(G^+)=\widehat g(G);
   \]
2. every operation with \(d_\mu^+=0\) satisfies
   \[
   d_\mu=2,\qquad \theta(\mu G)=2;
   \]
3. every rooted minor operation decreases \(\widehat g\) by at least one. Thus \(G\) is \(\widehat g\)-critical.

#### Proof

Choose \(\mu_0\) with \(d_{\mu_0}^+=0\). By (H1), \(d_{\mu_0}\ge2\). Equation (2.1) gives

\[
-d_{\mu_0}=\theta(G)-\theta(\mu_0G),
\]

or

\[
\theta(\mu_0G)=\theta(G)+d_{\mu_0}.
\]

Both theta-values lie between \(0\) and \(2\). Since \(d_{\mu_0}\ge2\), necessarily

\[
\theta(G)=0,\qquad d_{\mu_0}=2,\qquad \theta(\mu_0G)=2.
\]

The same argument applies to every operation with \(d_\mu^+=0\).

Now let \(\mu\) be arbitrary. If \(d_\mu^+=0\), then \(d_\mu=2\). Otherwise \(d_\mu^+\ge1\), and (2.1), together with \(\theta(G)=0\), yields

\[
d_\mu=d_\mu^++\theta(\mu G)\ge1.
\]

Thus every operation lowers \(\widehat g\). \(\square\)

This already rules out strong \(\widehat g\)-hoppers with Euler genus \(0\) or \(1\), because an exceptional operation would have genus \(\widehat g(G)-2<0\).

## Equivalent recognition criterion

Let \(p=\widehat g(G)\). Proposition 3.1 gives the following exact reformulation.

### Corollary 3.2

The graph \(G\) is a strong \(\widehat g\)-hopper if and only if:

1. \(\widehat g(G^+)=p\);
2. \(\widehat g(\mu G)\le p-1\) for every rooted minor operation \(\mu\);
3. at least one \(\mu\) satisfies
   \[
   \widehat g((\mu G)^+)=p;
   \]
4. whenever \(\widehat g((\mu G)^+)=p\), one has
   \[
   \widehat g(\mu G)=p-2.
   \]

Thus, after forgetting the roots and assuming all ordinary edge operations are allowable, \(G\) is an excluded minor for the minor-closed class

\[
\{H:\widehat g(H)\le p-1\}.
\]

Adding the edge \(xy\) preserves its Euler genus but destroys its minor-minimality in a very controlled way.

# 4. The two-edge signature

Suppose an exceptional operation is deletion of an edge \(e\), and put \(P=G-e\). Proposition 3.1 gives the four exact values

\[
\begin{array}{c|cccc}
H & P & P+e & P+xy & P+e+xy\\ \hline
\widehat g(H) & p-2 & p & p & p .
\end{array}
\tag{4.1}
\]

Consequently:

- adding \(e\) to \(P\) raises Euler genus by two;
- adding \(xy\) to \(P\) also raises Euler genus by two;
- adding both edges still raises Euler genus by only two.

Hence a hopper requires two distinct, redundant “two units of genus” insertions. This is considerably stronger than merely requiring a rooted graph \(P\) with \(\theta(P)=2\).

If the exceptional operation is contraction of \(e\), the corresponding necessary configuration is

\[
\widehat g(G/e)=p-2,\qquad
\widehat g((G/e)^+)=p,\qquad
\widehat g(G)=\widehat g(G^+)=p.
\tag{4.2}
\]

Here the inverse operation is a vertex split rather than a single edge insertion.

For deletion operations, one gets an even sharper finite list. Deleting one edge can lower Euler genus by at most two, because the edge can be reinserted using one handle. Combining this with Proposition 3.1, every edge deletion has one of the following signatures:

\[
(d_\mu,d_\mu^+,\theta(\mu G))
\in
\{(2,0,2),(1,1,0),(2,1,1),(2,2,0)\}.
\tag{4.3}
\]

The first is precisely the exceptional hopper transition.

# 5. Elementary structural consequences

Under the usual simple, connected-graph conventions, a strong hopper has minimum degree at least three.

Indeed:

- deleting a bridge does not change Euler genus;
- deleting a leaf edge does not change Euler genus;
- if a degree-two vertex has nonadjacent neighbors, contracting one incident edge merely suppresses a subdivision and does not change genus;
- if its neighbors are adjacent, deleting that adjacent edge does not change genus, since it can be redrawn alongside the two-edge path through the degree-two vertex.

Each possibility contradicts Proposition 3.1(3).

Thus a candidate is already a fairly rigid Euler-genus obstruction, and its exceptional minor must have \(\theta=2\).

# 6. The dual hopper convention

If instead “hopper” means the dual condition

\[
\forall\mu,\qquad d_\mu\ge1\ \text{or}\ d_\mu^+\ge2,
\]

with at least one operation satisfying \(d_\mu=0\), then the argument reverses.

### Proposition 6.1

Every such strong \(\widehat g^+\)-hopper satisfies

\[
\theta(G)=2.
\]

Every operation with \(d_\mu=0\) has

\[
d_\mu^+=2,\qquad \theta(\mu G)=0,
\]

and every operation lowers \(\widehat g^+\) by at least one.

#### Proof

For an operation with \(d_\mu=0\), equation (2.1) gives

\[
d_\mu^+=\theta(G)-\theta(\mu G)\le2.
\]

The hopper condition requires \(d_\mu^+\ge2\), so equality holds and the theta-values are \(2\) and \(0\). For any operation with \(d_\mu\ge1\),

\[
d_\mu^+=d_\mu+2-\theta(\mu G)\ge d_\mu\ge1.
\]

\(\square\)

This distinction is another reason the catalog sentence needs a precise definition.

# 7. Quantifiers and connectivity

If one uses only the parameter condition (H1)–(H2), without any connectivity requirement, then a single hopper produces hoppers at every larger Euler genus.

Let \(B_r\) be the 1-sum of \(r\) copies of \(K_5\). Euler genus is additive over 1-sums, so

\[
\widehat g(B_r)=r.
\]

Every edge deletion or contraction in \(B_r\) lowers its Euler genus by one. If \(G\) is a hopper and \(G_r=G\vee B_r\), with both roots retained in the \(G\)-summand, then

\[
\widehat g(G_r)=\widehat g(G)+r,\qquad
\widehat g(G_r^+)=\widehat g(G^+)+r.
\]

Operations in the \(G\)-summand retain the hopper transitions, while operations in \(B_r\) lower both parameters. Thus \(G_r\) is again a parameter-theoretic hopper.

This construction introduces a cutvertex and therefore does not preserve 3-connectivity. Consequently:

- in an unrestricted definition, existence of one hopper implies existence at every larger level;
- in the intended 3-connected building-block setting, this argument is inadmissible, and \(E_1,E_2,E_3\) remain distinct.

# 8. Exact finite-search test

For a proposed bound \(N\), a completely rigorous search can be made as follows.

For every simple graph \(G\) on at most \(N\) vertices and every nonedge \(xy\):

1. compute \(p=\widehat g(G)\);
2. reject unless \(\widehat g(G+xy)=p\);
3. for every edge deletion and contraction \(\mu\), compute
   \[
   a_\mu=\widehat g(\mu G),\qquad
   b_\mu=\widehat g((\mu G)^+);
   \]
4. reject if \(a_\mu>p-1\);
5. reject if \(b_\mu=p\) but \(a_\mu\ne p-2\);
6. accept precisely when at least one operation has \(b_\mu=p\).

Euler genus can be computed exactly, albeit very inefficiently, by enumerating all signed rotation systems, capping the boundary components of the associated ribbon graph, and minimizing

\[
2-|V|+|E|-|F|.
\]

A 3-connectivity filter can be imposed on \(G\), \(G^+\), or whichever graph the chosen definition requires. I have not executed such a search, so no numerical nonexistence claim is made here.

# 9. Remaining gap

The reductions above do not construct the configuration (4.1) or (4.2), nor do they rule it out. In particular, the four genus equalities in (4.1) are not sufficient: every other deletion and contraction must also satisfy the obstruction conditions of Corollary 3.2.

Thus, under the natural existential reading \(E_1\), the substantive problem remains:

> Does there exist an Euler-genus-threshold excluded minor \(G\) with nonadjacent roots \(x,y\) such that \(xy\) is genus-neutral, while every operation preserving the genus of \(G+xy\) lowers the genus of \(G\) by exactly two?

No proof or counterexample is obtained here. The main definite conclusion is that the catalog sentence needs formalization, together with the rigid necessary structure any genuine hopper must satisfy.