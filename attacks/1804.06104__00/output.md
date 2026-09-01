```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general conjecture remains open, but every d-degenerate graph without a K2 component has a neighbour-sum-distinguishing proper edge colouring with at most Δ + 20(d+1)^2 colours.",
  "would_publish": false,
  "caveats": "The constant depends on degeneracy and hence is not universal; novelty relative to specialized sparse-graph literature has not been checked."
}
```

## 1. Statement and conventions

For a proper edge colouring \(c:E(G)\to[k]\), write
\[
\sigma_c(v)=\sum_{e\ni v}c(e).
\]
The colouring is **neighbour sum distinguishing** if
\[
\sigma_c(u)\ne \sigma_c(v)
\qquad\text{for every }uv\in E(G).
\]

A component isomorphic to \(K_2\) is an unavoidable obstruction: both endpoint sums equal the colour of its only edge. Thus the standard “no isolated edge” hypothesis is necessary.

The open problem asks whether there is an absolute constant \(C\) such that every finite simple graph with no \(K_2\)-component has such a colouring from \([\Delta+C]\).

I do not prove that. I prove the following sparse-graph version.

### Theorem

Let \(G\) be a finite simple graph of maximum degree \(\Delta\), with no component isomorphic to \(K_2\). If \(G\) is \(d\)-degenerate, where \(d\ge 1\), then
\[
\chi'_{\Sigma}(G)\le \Delta+20(d+1)^2.
\]

The proof is constructive and gives a polynomial-time algorithm.

Consequently:

- every fixed-degeneracy class satisfies a \(\Delta+O(1)\) bound;
- in particular, every simple planar graph with no isolated edge satisfies
  \[
  \chi'_{\Sigma}(G)\le \Delta+720,
  \]
  since planar graphs are \(5\)-degenerate;
- if \(d=o(\Delta^{1/4})\), the additive term here is \(o(\sqrt{\Delta})\).

No claim of novelty relative to specialized sparse-graph literature is made.

---

## 2. Constraint-finalization setup

Choose a vertex ordering
\[
v_1,v_2,\ldots,v_n
\]
such that every \(v_i\) has at most \(d\) neighbours among
\(\{v_1,\ldots,v_{i-1}\}\). Such an ordering exists by degeneracy.

An edge \(v_iv_j\), with \(i<j\), is coloured at **stage \(i\)**. Thus at stage \(i\) we colour simultaneously all edges
\[
X_i=\{v_iv_j:j>i\}.
\]
Put \(z=v_i\), \(t=|X_i|\), and let \(r\le d\) be the number of already coloured edges at \(z\).

For an edge \(e=uv\), define
\[
Q_e=(E(u)\setminus\{e\})\cup(E(v)\setminus\{e\})
\]
and
\[
\Phi_e(c)=
 \sum_{f\in E(u)\setminus\{e\}}c(f)
 -
 \sum_{f\in E(v)\setminus\{e\}}c(f).
\]
The colour of \(e\) cancels, so
\[
\sigma_c(u)-\sigma_c(v)=\Phi_e(c).
\]

Because there is no \(K_2\)-component, \(Q_e\ne\varnothing\) for every edge \(e\).

If \(f=v_pv_q\), define its colouring time by
\[
\tau(f)=\min\{p,q\}.
\]
For each edge \(e\), let
\[
T(e)=\max_{f\in Q_e}\tau(f).
\]
At stage \(T(e)\), every colour occurring in \(\Phi_e\) has become known. We require \(\Phi_e\ne0\) precisely at this stage. Once imposed, this condition cannot subsequently change.

The main point is that the constraints which become final at one stage have a restricted form.

---

## 3. Shape and number of constraints at one stage

Write the current edges as
\[
X_i=\{zw_1,\ldots,zw_t\},
\]
with prospective colours \(x_1,\ldots,x_t\).

### Lemma 1

At stage \(i\):

1. At most \(d+t\) newly finalized constraints come from edges incident with \(z\).
   - For a backward edge \(zu\), the current part of its constraint is
     \[
     x_1+\cdots+x_t.
     \]
   - For a forward edge \(zw_j\), the current part is
     \[
     \sum_{h\ne j}x_h.
     \]

2. Every newly finalized constraint from an edge not incident with \(z\) involves either one or two current variables.

3. For each \(x_j\), at most \(d\) one-variable constraints involve \(x_j\).

4. The two-variable constraints pair variables according to a matching.

5. Altogether, the number \(M_i\) of newly finalized constraints satisfies
   \[
   M_i\le d+(d+1)t.
   \]

#### Proof

After stage \(i\), the uncoloured graph is exactly
\[
H_i=G[\{v_{i+1},\ldots,v_n\}].
\]

If a target edge \(e\) is incident with \(z\), the first assertion follows directly: the colour of \(e\) itself cancels, while all other current edges at \(z\) remain in \(\Phi_e\).

Now let \(e=ab\) not be incident with \(z\). A current edge \(zw_j\) can occur in \(\Phi_e\) only if \(w_j\in\{a,b\}\). Hence at most two current variables occur.

Suppose \(w_j\) is an endpoint of such an edge \(e\) and \(T(e)=i\). Every uncoloured edge of \(H_i\) incident with \(w_j\), other than possibly \(e\) itself, would belong to \(Q_e\), contradicting \(T(e)=i\). Therefore:

- if \(w_j\) is isolated in \(H_i\), then possible target edges through \(w_j\) go to earlier vertices; apart from \(zw_j\), there are at most \(d-1\) such edges;
- if \(w_j\) has an edge in \(H_i\), that edge is unique and must itself be the target edge.

Thus at most \(d\) nonincident constraints can be charged to any \(x_j\). If a target edge has both endpoints among the \(w_j\)'s, it is an isolated edge of \(H_i\); consequently such two-variable target edges form a matching.

There are at most \(d+t\) incident target edges and at most \(dt\) nonincident ones, proving
\[
M_i\le d+t+dt=d+(d+1)t.
\]
\(\square\)

### Proper-colouring restrictions

Before choosing \(x_j\):

- at most \(d\) colours are already present at \(z\);
- at most \(d-1\) colours are already present at \(w_j\), since \(z\) is one of its at most \(d\) earlier neighbours.

Thus at most \(2d-1\) colours are locally forbidden for each \(x_j\), aside from the requirement that the \(x_j\)'s themselves be pairwise distinct.

---

## 4. Choosing the colours at a stage

Set
\[
C=20(d+1)^2,\qquad k=\Delta+C,
\]
and use the palette \([k]\).

We split according to \(t=|X_i|\).

### Case 1: \(1\le t<4(d+1)\)

Every newly finalized constraint is a nonconstant affine equation in the current variables, with each nonzero coefficient equal to \(1\) or \(-1\).

Order the variables arbitrarily. Assign each constraint to the last variable, in this order, which occurs in it. When that variable is selected, the constraint forbids at most one colour.

When choosing any \(x_j\), the number of forbidden colours is at most

- \(2d-1\) from properness at its endpoints;
- \(t-1\) from colours used on the other current edges;
- \(M_i\le d+(d+1)t\) from finalized sum constraints.

Hence it is at most
\[
(2d-1)+(t-1)+d+(d+1)t
  =3d-2+(d+2)t.
\]
Since \(t<4(d+1)\),
\[
3d-2+(d+2)t<20(d+1)^2\le k.
\]
Thus the variables can be chosen greedily.

If \(t=0\), no edge has colouring time \(i\), so no constraint is newly finalized at that stage.

### Case 2: \(t\ge4(d+1)\)

The many-variable constraints coming from forward edges incident with \(z\) can be made automatically nonzero by choosing the current colours sufficiently large.

Let
\[
\theta=\frac{(d-1)k}{t-1},
\qquad
P=\{a\in[k]:a>\theta\}.
\]

For each variable \(x_j\), remove from \(P\):

- the at most \(2d-1\) colours forbidden by properness;
- the at most \(d\) colours forbidden by one-variable finalized constraints.

Thus at most \(3d-1\) colours are removed.

We claim each resulting list has size at least \(t+d+2\). Put
\[
q=\frac{d-1}{t-1}<\frac14.
\]
Since \(t\le\Delta\), we have \(k\ge t+C\), and therefore
\[
\begin{aligned}
|P|-t
&\ge k-\theta-t\\
&=k(1-q)-t\\
&\ge (t+C)(1-q)-t\\
&=C(1-q)-qt\\
&>\frac{3C}{4}-d.
\end{aligned}
\]
After deleting \(3d-1\) further colours, the resulting list has size greater than
\[
t+\frac{3C}{4}-4d+1\ge t+d+2.
\]

The two-variable constraints form a matching by Lemma 1. Choose one variable as a pivot. Assign all other variables greedily from their lists, respecting distinctness and, whenever the second endpoint of a matching constraint is assigned, avoiding its one prohibited value.

For the pivot, after excluding:

- the \(t-1\) already used colours;
- at most one colour from its matching constraint,

at least \(d+2\) choices remain.

The constraints from backward edges incident with \(z\) forbid at most \(d\) possible values of the total
\[
x_1+\cdots+x_t.
\]
Different pivot colours give different totals, so one of the remaining choices avoids all these constraints.

It remains to check the constraints from forward edges \(zw_j\) that become final at this stage. For such an edge, \(w_j\) has no uncoloured incident edge after stage \(i\); hence it has at most \(d-1\) other incident edges. If \(P_j\) denotes the sum of their colours, then
\[
P_j\le(d-1)k.
\]
On the \(z\)-side, excluding \(zw_j\), there are the \(t-1\) other current colours, each larger than \(\theta\). Therefore
\[
\sum_{h\ne j}x_h
  >(t-1)\theta
  =(d-1)k
  \ge P_j.
\]
Adding the already coloured positive contributions at \(z\) only increases the left side, so the endpoint sums are automatically different.

This completes the colour choice at every stage.

---

## 5. Completion of the proof

Proceed through stages \(1,\ldots,n\).

The local restrictions ensure that the resulting edge colouring is proper. For every edge \(e=uv\), the set \(Q_e\) is nonempty, and at stage \(T(e)\) the construction imposes
\[
\Phi_e(c)\ne0.
\]
Subsequent stages cannot alter \(\Phi_e\). At the end,
\[
\sigma_c(u)-\sigma_c(v)
=\Phi_e(c)\ne0.
\]
Thus the colouring is neighbour sum distinguishing and uses at most
\[
\Delta+20(d+1)^2
\]
colours. This proves the theorem. \(\square\)

---

## 6. A sharper special case: forests

The quadratic-degeneracy constant is far from sharp for \(d=1\).

### Proposition

Every forest with no \(K_2\)-component has a neighbour-sum-distinguishing proper edge colouring from \([\Delta+1]\).

#### Proof

Root every nontrivial component at a vertex of degree at least \(2\). Colour the edges incident with each root arbitrarily and distinctly.

Process vertices away from the root. Suppose the parent edge of a nonroot vertex \(v\) has colour \(a\), and the already fixed parent sum is \(S\).

If \(v\) is a leaf, then
\[
\sigma(v)=a<S,
\]
because its parent has degree at least \(2\).

Otherwise, let \(s=d(v)-1\). Choose \(s\) distinct colours from
\[
[\Delta+1]\setminus\{a\}
\]
for the child edges. This available set has \(\Delta\) elements and
\[
1\le s\le\Delta-1,
\]
so its \(s\)-subsets have at least two different sums. Choose one whose sum is not \(S-a\). Then \(\sigma(v)\ne S\). Continue recursively.

The colouring remains proper and distinguishes every parent-child edge. \(\square\)

This is sharp: on \(P_4\), every proper \(2\)-edge colouring alternates the two colours, so the two internal vertices receive the same sum. Hence \(P_4\) needs \(\Delta+1=3\) colours.

---

## 7. What remains open

The theorem only gives
\[
\Delta+O(d^2),
\]
where \(d\) is the degeneracy. In dense graphs one can have \(d=\Theta(\Delta)\), so this supplies no universal additive constant and does not resolve the catalogued problem or the stronger \(\Delta+2\) conjecture.

The dependence on \(d\) enters when many constraints become final during a stage with only \(O(d)\) current edges: the direct greedy argument may have to pay for \(O(d^2)\) affine exclusions. Eliminating all dependence on degeneracy would require a substantially different mechanism.