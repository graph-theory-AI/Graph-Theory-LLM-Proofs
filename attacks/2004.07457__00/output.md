```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For the slice k_A=Δ_A=r fixed, I obtain constant-factor optimal bounds k_B=Θ_r(Δ_B^{1/r}), an asymptotically exact threshold when the B-lists are pairwise disjoint, and the exact (2,2) boundary.",
  "would_publish": false,
  "caveats": "Only a special slice is treated, a factor (r!)^{1/r} remains in the unrestricted case, and overlap with bounds implicit in the source paper has not been checked."
}
```

# Partial resolution of a fixed-one-sided-degree slice

## 1. Statement of the partial result

Lists are understood to have at least the prescribed sizes; they may always be trimmed to the exact sizes.

Fix integers \(r,D,q\ge 2\), and consider bipartite graphs \(G=(A\cup B,E)\) satisfying
\[
\Delta(G[A,B]\text{ on }A)\le r,\qquad
\Delta(G[A,B]\text{ on }B)\le D,
\]
with lists of size \(r\) on \(A\) and \(q\) on \(B\). Thus this is the slice
\[
\Delta_A=k_A=r,\qquad \Delta_B=D,\qquad k_B=q.
\]

Set
\[
\lambda_r:=\frac{r^r}{(r-1)^{r-1}},
\qquad
c_r:=\lambda_r^{-1}=\frac{(r-1)^{r-1}}{r^r}.
\]

### Theorem 1: unrestricted sufficient condition

Every such graph is \((r,q)\)-choosable provided
\[
\boxed{\quad q^r\ge r!\bigl(1+\lambda_r(D-1)\bigr).\quad}
\tag{1}
\]

For fixed \(r\), this gives \(q=O_r(D^{1/r})\).

### Private-\(B\)-palette variant

Call a list assignment **private on \(B\)** if
\[
L(b)\cap L(b')=\varnothing
\qquad\text{for all distinct }b,b'\in B.
\]

In that restricted class, the sufficient condition improves to
\[
\boxed{\quad q^r\ge 1+\lambda_r(D-1).\quad}
\tag{2}
\]

Moreover, this condition is asymptotically sharp:

### Theorem 2: asymptotically sharp obstruction with private palettes

For every fixed \(r\ge2\) and every \(\varepsilon>0\), for all sufficiently large \(q\) there is a bipartite graph and a private-\(B\)-palette list assignment such that

\[
\Delta_A=r,\qquad
\Delta_B\le (c_r+\varepsilon)q^r,
\]
all \(A\)-lists have size \(r\), all \(B\)-lists have size \(q\), and the assignment is not colorable.

Consequently, if \(D_r^{\mathrm{priv}}(q)\) denotes the least opposite-side degree at which such a private-palette counterexample exists, then
\[
\boxed{\quad
D_r^{\mathrm{priv}}(q)
  =\bigl(c_r+o(1)\bigr)q^r.
\quad}
\tag{3}
\]

For the original unrestricted problem, define
\[
F_r(D):=\min\{q\le D:
 \text{ every graph with }\Delta_A\le r,\Delta_B\le D
 \text{ is }(r,q)\text{-choosable}\}.
\]
Then, for fixed \(r\) and \(D\to\infty\),
\[
\boxed{\quad
(\lambda_rD)^{1/r}(1-o(1))
 \le F_r(D)
 \le (r!\lambda_rD)^{1/r}(1+o(1)).
\quad}
\tag{4}
\]

Thus this slice is determined up to a multiplicative factor \((r!)^{1/r}\). Under private \(B\)-palettes, the answer is asymptotically
\[
F_r^{\mathrm{priv}}(D)
  =(\lambda_rD)^{1/r}(1+o(1)).
\]

For \(r=2\), these bounds become
\[
(2-o(1))\sqrt D
 \le F_2(D)
 \le (2\sqrt2+o(1))\sqrt D,
\tag{5}
\]
while in the private-palette variant,
\[
F_2^{\mathrm{priv}}(D)=(2+o(1))\sqrt D.
\]

The analogous assertions hold after interchanging \(A\) and \(B\).

---

## 2. Local-lemma upper bound

I use the following standard cluster-expansion form of the Lovász Local Lemma.

### Lemma 3: independent-neighborhood local lemma

Let \(\{E_i:i\in I\}\) be finite events with dependency graph \(H\). For \(\mu_i>0\), put
\[
\Phi_i(\boldsymbol\mu)
 =
 \sum_{\substack{J\subseteq \{i\}\cup N_H(i)\\
                  J\text{ independent in }H}}
 \prod_{j\in J}\mu_j.
\]
If
\[
\Pr(E_i)\le \frac{\mu_i}{\Phi_i(\boldsymbol\mu)}
\qquad\text{for every }i,
\]
then
\[
\Pr\Bigl(\bigcap_i\overline{E_i}\Bigr)>0.
\]

This is the usual strengthened local-lemma induction, with the independent-set recurrence
\[
Z(S)=Z(S\setminus\{v\})+\mu_v Z(S\setminus N[v]).
\]

### Proof of Theorem 1

Choose, independently and uniformly, a color
\[
\phi(b)\in L(b)
\]
for every \(b\in B\).

For \(a\in A\), let \(E_a\) be the event that every color in \(L(a)\) is used by a neighbor of \(a\). If \(d(a)<r\), this event is impossible. If \(d(a)=r\), it can occur only when the \(r\) neighbors of \(a\) receive the \(r\) distinct colors of \(L(a)\) in some order. Hence
\[
\Pr(E_a)\le \frac{r!}{q^r}.
\tag{6}
\]

Two events are independent whenever their corresponding \(A\)-vertices have disjoint neighborhoods in \(B\). The dependency graph is therefore the intersection graph of the \(r\)-sets \(N(a)\).

Fix an event \(E_a\). For each \(b\in N(a)\), the other events involving \(b\) form a clique of size at most \(D-1\). Thus the neighborhood of \(E_a\) is covered by \(r\) cliques, each of size at most \(D-1\).

Assign the same parameter \(\mu>0\) to every event. An independent set in the closed neighborhood of \(E_a\)

- is either \(\{E_a\}\), contributing \(\mu\); or
- does not contain \(E_a\), in which case it contains at most one event from each of the \(r\) cliques.

Therefore
\[
\Phi_a(\boldsymbol\mu)
 \le \mu+\bigl(1+(D-1)\mu\bigr)^r.
\tag{7}
\]

Take
\[
\mu=\frac1{(r-1)(D-1)}.
\]
A direct calculation gives
\[
\frac{\mu}
     {\mu+(1+(D-1)\mu)^r}
 =
 \frac1{1+(D-1)\lambda_r}.
\tag{8}
\]

Consequently, the local lemma applies whenever
\[
\frac{r!}{q^r}
 \le \frac1{1+(D-1)\lambda_r},
\]
which is exactly (1).

With positive probability no \(E_a\) occurs. For such a coloring of \(B\), every \(a\in A\) has a color in \(L(a)\) not used by any neighbor. Since \(A\) is independent, these colors may be chosen independently for all \(a\), completing the coloring. ∎

### Proof of the private-palette upper bound

If the \(B\)-lists are pairwise disjoint, a given \(A\)-vertex can be blocked by at most one ordered color assignment to its \(r\) neighbors: each color of \(L(a)\) belongs to at most one \(B\)-list. Thus (6) improves to
\[
\Pr(E_a)\le \frac1{q^r}.
\]
The rest of the proof is unchanged, yielding (2). ∎

---

## 3. An asymptotically matching obstruction

The construction below is an atomic \(r\)-ary constraint gadget encoded as a bipartite list assignment.

### 3.1 Rooted forcing gadgets

All \(B\)-vertices will have pairwise disjoint \(q\)-element palettes.

Fix integers
\[
1=s_0<s_1<\cdots<s_\ell=q.
\]

A level-\(i\) rooted gadget has:

- a root \(x\in B\) with a private \(q\)-list \(L(x)\);
- a designated target subset \(S_x\subseteq L(x)\) of size \(s_i\);

and will have the property that every proper list coloring forces
\[
\phi(x)\in S_x.
\tag{9}
\]

At level \(\ell\), where \(s_\ell=q\), take just the root with no constraints.

Suppose the level-\((i+1)\) gadget has been constructed. For every color
\[
c\in L(x)\setminus S_x,
\]
introduce \(r-1\) disjoint copies of the level-\((i+1)\) gadget, with roots
\[
y_{c,1},\ldots,y_{c,r-1}
\]
and designated target sets \(T_{c,j}\), each of size \(s_{i+1}\).

For every tuple
\[
(d_1,\ldots,d_{r-1})
 \in T_{c,1}\times\cdots\times T_{c,r-1},
\]
introduce a vertex \(a\in A\) adjacent to
\[
x,y_{c,1},\ldots,y_{c,r-1}
\]
and give it the list
\[
L(a)=\{c,d_1,\ldots,d_{r-1}\}.
\]
These are \(r\) distinct colors because the \(B\)-palettes are private.

### Lemma 4: forcing property

Every coloring of the level-\(i\) gadget has \(\phi(x)\in S_x\). Conversely, every choice of \(\phi(x)\in S_x\) extends to a coloring of the gadget.

#### Proof

Induct on \(i\) from \(\ell\) downwards.

Suppose \(\phi(x)=c\notin S_x\). By induction, every helper root \(y_{c,j}\) receives some color
\[
d_j\in T_{c,j}.
\]
The \(A\)-vertex corresponding to \((d_1,\ldots,d_{r-1})\) then has all \(r\) of its list colors used by its neighbors, so it cannot be colored. Hence \(\phi(x)\in S_x\).

Conversely, suppose \(\phi(x)\in S_x\). Color all helper gadgets inductively. Every connector associated with a forbidden color \(c\notin S_x\) may itself be colored \(c\), because \(x\) does not use \(c\), and no helper palette contains \(c\). ∎

### 3.2 Degree calculation

At level \(i<\ell\), the root is incident with
\[
(q-s_i)s_{i+1}^{\,r-1}
\tag{10}
\]
connector vertices.

If this gadget appears as a helper inside its parent, its root has an additional
\[
s_i^{\,r-1}
\tag{11}
\]
incident connectors from that parent. Hence every \(B\)-degree is at most
\[
\max\left\{
q^{r-1},
\ 
(q-s_i)s_{i+1}^{\,r-1}+s_i^{\,r-1}
 :0\le i<\ell
\right\}.
\tag{12}
\]

Every \(A\)-vertex has degree exactly \(r\).

### 3.3 Choice of the target sizes

Recall
\[
c_r=\max_{0\le x\le1}x^{r-1}(1-x)
    =\frac{(r-1)^{r-1}}{r^r}.
\]

Fix \(C>c_r\). There is a finite real sequence
\[
0=x_0<x_1<\cdots<x_\ell=1
\]
such that
\[
(1-x_i)x_{i+1}^{\,r-1}\le C
\qquad(0\le i<\ell).
\tag{13}
\]

Indeed, starting from \(x_0=0\), iterate
\[
x_{i+1}
 =\left(\frac{C}{1-x_i}\right)^{1/(r-1)}
\]
until the right-hand side is at least \(1\), and then set \(x_{i+1}=1\). The iteration is strictly increasing because
\[
C>x^{r-1}(1-x)
\]
for every \(x\in[0,1]\). It reaches \(1\) after finitely many steps; otherwise a limiting fixed point would contradict \(C>c_r\).

For large \(q\), choose integers \(s_i=x_iq+O(1)\), with \(s_0=1\) and \(s_\ell=q\). Equations (12) and (13) then give
\[
\Delta_B\le Cq^r+O(q^{r-1}).
\tag{14}
\]

### 3.4 Closing the contradiction

Take \(r\) disjoint copies of the level-zero gadget. Their roots
\[
x_1,\ldots,x_r
\]
are forced to respective singleton colors
\[
\alpha_1,\ldots,\alpha_r.
\]
Add one final \(A\)-vertex adjacent to all \(x_i\), with list
\[
\{\alpha_1,\ldots,\alpha_r\}.
\]
This vertex is blocked in every coloring.

Choosing \(C\) strictly between \(c_r\) and \(c_r+\varepsilon\), and then taking \(q\) sufficiently large in (14), proves Theorem 2. ∎

---

## 4. Consequences for the original slice

The private-palette construction is a valid list assignment in the unrestricted problem. It therefore supplies the lower bound in (4).

For the upper bound, Theorem 1 gives
\[
q^r\ge r!\lambda_rD+O_r(1).
\]
For the lower bound, choose \(q\) so that
\[
(c_r+\varepsilon)q^r\le D.
\]
The construction shows that this \(q\) does not suffice. Letting \(\varepsilon\to0\) gives
\[
q\lesssim (\lambda_rD)^{1/r}.
\]
This proves (4).

The only difference between the two constants comes from the factor \(r!\) in (6): without restrictions on overlaps among the \(B\)-lists, an \(A\)-vertex can in principle be blocked by as many as \(r!\) permutations of its list.

---

## 5. Exact finite result for \(r=q=2\)

### Proposition 5

For \(D\ge2\), every graph with
\[
\Delta_A\le2,\qquad \Delta_B\le D
\]
is \((2,2)\)-choosable if and only if \(D\le2\).

#### Proof for \(D\le2\)

The whole graph has maximum degree at most \(2\), so every component is a path or a cycle. Since the graph is bipartite, every cycle is even.

Paths are greedily 2-choosable. For an even cycle:

- if all 2-lists are equal, alternate the two colors;
- otherwise choose an edge \(v_nv_1\) with \(L(v_n)\ne L(v_1)\), choose
  \(c\in L(v_1)\setminus L(v_n)\), color \(v_1\) with \(c\), and greedily color
  \(v_2,\ldots,v_n\). The final vertex automatically differs from \(v_1\)
  because \(c\notin L(v_n)\).

Thus every component is colorable.

#### Counterexample for \(D=3\)

Let \(B=\{x,y,p,s\}\), with pairwise disjoint lists
\[
\begin{aligned}
L(x)&=\{x_0,x_1\},&
L(y)&=\{y_0,y_1\},\\
L(p)&=\{p_0,p_1\},&
L(s)&=\{s_0,s_1\}.
\end{aligned}
\]

Add five vertices to \(A\):

- two adjacent to \(x,p\), with lists
  \[
  \{x_1,p_0\},\qquad \{x_1,p_1\};
  \]
- two adjacent to \(y,s\), with lists
  \[
  \{y_1,s_0\},\qquad \{y_1,s_1\};
  \]
- one adjacent to \(x,y\), with list
  \[
  \{x_0,y_0\}.
  \]

If \(x\) receives \(x_1\), whichever color \(p\) receives blocks one of the first two \(A\)-vertices. Hence \(x=x_0\). Similarly \(y=y_0\). The final \(A\)-vertex is then blocked.

The degrees are
\[
d(x)=d(y)=3,\qquad d(p)=d(s)=2,
\]
and every \(A\)-vertex has degree \(2\). This also works for every \(D\ge3\). ∎

In particular,
\[
F_2(2)=2,\qquad F_2(3)=3.
\]

---

## 6. An exact complete-bipartite calculation

Let \(K_{m,2}\) have its \(m\)-vertex side in \(A\) and its two-vertex side \(\{u,v\}\) in \(B\).

### Proposition 6

The graph \(K_{m,2}\) is \((2,q)\)-choosable if and only if
\[
m<q^2.
\]

#### Proof

Let \(S=L(u)\) and \(T=L(v)\).

If \(S\cap T\ne\varnothing\), give \(u\) and \(v\) the same common color. Their two colors do not exhaust any 2-element \(A\)-list.

If \(S\cap T=\varnothing\), an \(A\)-vertex can block at most one ordered pair
\[
(s,t)\in S\times T,
\]
namely when its list is \(\{s,t\}\). Thus fewer than \(q^2\) vertices cannot block all \(q^2\) pairs.

Conversely, for \(m\ge q^2\), take disjoint \(q\)-sets \(S,T\), and for every \((s,t)\in S\times T\) include an \(A\)-vertex with list \(\{s,t\}\). Every choice for \(u,v\) blocks the corresponding vertex. ∎

The more elaborate forcing construction above lowers the required maximum \(B\)-degree from \(q^2\) for this single complete bipartite graph to asymptotically \(q^2/4\) over general graphs.

---

## 7. Trivial boundary and endpoint pairs

### List size one never suffices in the permitted range

If \(k_A=1\), \(\Delta_A\ge1\), and \(k_B=q\le\Delta_B\), take a star centered at \(b\in B\) with \(q\) leaves in \(A\). Give \(b\) the list
\[
\{1,\ldots,q\}
\]
and force the \(i\)-th leaf to use color \(i\). The center has no available color. Thus no allowed pair with \(k_A=1\) is universally sufficient. The same holds with the sides interchanged.

### The endpoint \((\Delta_A,\Delta_B)\) always works when both caps are at least two

Suppose every \(a\in A\) has a list of size \(\Delta_A\ge2\) and every \(b\in B\) has a list of size \(\Delta_B\ge2\).

For a connected component:

- If some vertex has list size strictly larger than its degree, root a spanning tree there and color vertices in reverse tree order. Every non-root has an uncolored parent, while the root has more colors than neighbors.
- Otherwise every list size equals the actual degree. The component then has minimum degree at least \(2\), so it contains a shortest, hence induced, even cycle \(C\). Color vertices outside \(C\) in decreasing distance from \(C\). Each has an uncolored neighbor toward \(C\), so a color is available. Each vertex of \(C\) then retains at least two colors, and the even cycle is 2-choosable.

Hence every such graph is \((\Delta_A,\Delta_B)\)-choosable.

---

## 8. Remaining gaps

1. The unrestricted fixed-\(r\) slice still has a factor
   \[
   (r!)^{1/r}
   \]
   between the upper and lower bounds. For \(r=2\), the current argument only yields
   \[
   (2-o(1))\sqrt D
   \le F_2(D)
   \le(2\sqrt2+o(1))\sqrt D.
   \]

2. The exact private-palette result does not settle arbitrary overlapping lists. The overlap permits one \(A\)-vertex to represent several permutations of its list, but such permutations also have additional algebraic structure not used by the local-lemma estimate.

3. Nothing here characterizes the main regime \(k_A<\Delta_A\), apart from the trivial \(k_A=1\) obstruction. That regime contains the difficult logarithmic and near-symmetric questions from the source paper.

4. I have not verified whether the source paper's general criteria already imply some or all of the upper bounds above. The forcing construction and the exact private-palette asymptotic are presented self-containedly, but no claim of literature novelty is made.