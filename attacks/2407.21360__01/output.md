```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any witness must have treewidth at least 3, and a concrete treewidth-3 construction gives the conjectured exponent provided a sharply isolated robust two-colour lemma for products of two fans can be proved.",
  "would_publish": false,
  "caveats": "The robust fan-square lemma is proved only in several substantial cases; mixed colour patterns on both apex arms remain unresolved."
}
```

# 1. Statement and notation

For \(m\ge 2\), let

\[
J_m:=K_1\vee P_m
\]

be the fan obtained by adding a universal vertex to an \(m\)-vertex path. Thus
\(\operatorname{tw}(J_m)=2\).

The proposed route to the conjectured exponent uses products \(J_m\boxtimes J_m\). Write \(x,y\) for the two fan apices, and write the path vertices as \(u_1,\dots,u_m\) and \(v_1,\dots,v_m\). In the product define

\[
z=(x,y),
\qquad
A=\{a_j:=(x,v_j):1\le j\le m\},
\]
\[
B=\{b_i:=(u_i,y):1\le i\le m\},
\qquad
Q=\{q_{ij}:=(u_i,v_j):1\le i,j\le m\}.
\]

The relevant elementary properties are:

* \(z\) is universal;
* \(A\) and \(B\) each induce a path;
* \(A\) is complete to \(B\);
* \(Q\) induces \(P_m\boxtimes P_m\);
* \(a_jq_{ij}\) and \(b_iq_{ij}\) are edges for every \(i,j\).

All arguments below use only these edges.

# 2. A necessary condition: \(t\ge 3\)

## Proposition 2.1

If both factors are \(3\)-colourable, then their strong product has a \(3\)-colouring with clustering at most the order of the smaller factor.

### Proof

Suppose \(|V(H_1)|\ge |V(H_2)|\), and let \(\phi\) be a proper \(3\)-colouring of \(H_1\). Colour

\[
(u,v)\in V(H_1\boxtimes H_2)
\]

with \(\phi(u)\).

If two adjacent product vertices of the same colour have distinct first coordinates \(u,u'\), then \(uu'\in E(H_1)\), contrary to properness of \(\phi\). Consequently every monochromatic component is contained in a fibre

\[
\{u\}\times V(H_2),
\]

and hence has at most \(|V(H_2)|\) vertices. Therefore the clustering is at most

\[
\min\{|V(H_1)|,|V(H_2)|\}
 \le \sqrt{|V(H_1\boxtimes H_2)|}.
\qquad\square
\]

Every graph of treewidth at most \(2\) is properly \(3\)-colourable. Thus no family with \(t\le2\) can have clustering
\(\Omega(N^{4/7})\), since \(N^{1/2}=o(N^{4/7})\).

Hence:

\[
\boxed{\text{Any value of \(t\) witnessing the conjecture must satisfy \(t\ge3\).}}
\]

# 3. A concrete treewidth-\(3\) candidate

The following stability statement would suffice.

## Robust fan-square statement

There exist constants \(\delta,\gamma>0\) such that, for every sufficiently large \(m\), the following holds.

If \(D\subseteq V(J_m\boxtimes J_m)\) satisfies \(|D|\le\delta m\), then every red-blue colouring of

\[
(J_m\boxtimes J_m)-D
\]

has a monochromatic component of order at least

\[
\gamma m^{4/3}.
\tag{RF}
\]

This is stronger than the ordinary two-colour lower bound because \(D\) may contain the universal vertex \(z\).

The exponent \(4/7\) follows exactly from (RF).

## Proposition 3.1

If (RF) holds, then Conjecture 8 holds with \(t=3\).

### Proof

Fix \(\alpha\in(0,\gamma)\), and choose a constant \(C>\alpha/\delta\). Put

\[
p=\left\lceil C m^{1/3}\right\rceil.
\]

Define

\[
H_1:=K_1\vee\bigl(pJ_m\bigr),
\qquad
H_2:=K_1\vee J_m,
\]

where \(pJ_m\) denotes the disjoint union of \(p\) copies of \(J_m\).

Both graphs have treewidth exactly \(3\):

* adding a universal vertex to a width-\(2\) decomposition gives width \(3\);
* each graph contains a \(K_4\), namely the outer apex together with a triangle in a copy of \(J_m\).

Their orders satisfy

\[
|V(H_1)|=1+p(m+1)=\Theta(m^{4/3}),
\qquad
|V(H_2)|=m+2=\Theta(m),
\]

so

\[
N:=|V(H_1\boxtimes H_2)|=\Theta(m^{7/3}).
\tag{1}
\]

Let \(r,s\) be the two outer universal vertices. Then \((r,s)\) is universal in \(H_1\boxtimes H_2\).

Suppose there is a \(3\)-colouring with clustering less than

\[
K:=\alpha m^{4/3}.
\]

Let \(c\) be the colour of \((r,s)\). Since \((r,s)\) is universal, all vertices of colour \(c\) lie in its monochromatic component. Hence fewer than \(K\) vertices in the whole product have colour \(c\).

For each of the \(p\) copies \(J_m^{(i)}\) inside \(H_1\), consider the induced block

\[
G_i:=J_m^{(i)}\boxtimes J_m.
\]

Let \(D_i\) be the set of colour-\(c\) vertices in \(G_i\). The blocks are vertex-disjoint and

\[
\sum_{i=1}^{p}|D_i|<K.
\]

Thus some \(i\) satisfies

\[
|D_i|<\frac{K}{p}
 \le \frac{\alpha}{C}m
 <\delta m.
\]

After deleting \(D_i\), only the other two colours occur in \(G_i\). By (RF), one of those colours has a component of order at least
\(\gamma m^{4/3}>K\), a contradiction.

It follows that every \(3\)-colouring has clustering
\(\Omega(m^{4/3})\). By (1),

\[
m^{4/3}
 =\Theta\!\left(N^{(4/3)/(7/3)}\right)
 =\Theta(N^{4/7}).
\]

Therefore these \(H_1,H_2\), both of treewidth \(3\), would prove the conjecture. \(\square\)

This explains the exponent structurally:

\[
\underbrace{m^2}_{\text{one fan-square block}}
,\qquad
\underbrace{m^{4/3}}_{\text{two-colour obstruction}}
,\qquad
\underbrace{m^{1/3}}_{\text{number of blocks}}
,\qquad
m^2m^{1/3}=m^{7/3}.
\]

# 4. What can be proved about the robust fan-square statement

## 4.1 A grid fragmentation lemma

Let \(Q_m=P_m\square P_m\).

### Lemma 4.1

If \(S\subseteq V(Q_m)\) and every component of \(Q_m-S\) has at most \(k\) vertices, then

\[
|S|+m\ge \frac{m^2-|S|}{\sqrt{k}}.
\tag{2}
\]

### Proof

For a finite set \(X\subseteq\mathbb Z^2\), its edge-boundary in the infinite square grid has size at least \(4\sqrt{|X|}\). This follows, for example, by counting the nonempty rows and columns met by \(X\).

Let \(C_1,\dots,C_r\) be the components of \(Q_m-S\), with
\(s_i=|C_i|\le k\). Boundary edges of the \(C_i\) either meet \(S\) or leave the \(m\times m\) box. Consequently,

\[
4\sum_i\sqrt{s_i}\le 4|S|+4m.
\]

On the other hand,

\[
\sum_i\sqrt{s_i}
 \ge \sum_i\frac{s_i}{\sqrt{k}}
 =\frac{m^2-|S|}{\sqrt{k}}.
\]

Combining these inequalities proves (2). \(\square\)

## 4.2 The universal vertex survives

### Lemma 4.2

There is an absolute \(c>0\) such that the following holds for all sufficiently large \(m\).

Let \(D\subseteq V(J_m\boxtimes J_m)\) with \(|D|\le m\), and suppose
\(z\notin D\). Every red-blue colouring of
\((J_m\boxtimes J_m)-D\) has a monochromatic component of order at least

\[
c m^{4/3}.
\]

### Proof

Suppose \(z\) is red and all monochromatic components have order at most \(k\). Since \(z\) is universal, every surviving red vertex belongs to the component containing \(z\). Thus there are at most \(k\) red vertices in total.

In the grid \(Q\), let

\[
S=(D\cap Q)\cup\{\text{red vertices of }Q\}.
\]

Then \(|S|\le |D|+k\), and every component of \(Q-S\) is blue and has at most \(k\) vertices. Lemma 4.1 gives

\[
k+|D|+m
 \ge \frac{m^2-k-|D|}{\sqrt{k}}.
\tag{3}
\]

For \(|D|\le m\), inequality (3) is impossible when
\(k<c m^{4/3}\) for a sufficiently small absolute \(c\). Hence
\(k=\Omega(m^{4/3})\). \(\square\)

In particular, taking \(D=\varnothing\) gives a self-contained proof that every \(2\)-colouring of \(J_m\boxtimes J_m\) has clustering
\(\Omega(m^{4/3})\).

Thus any counterexample to (RF) must delete \(z\).

## 4.3 One complete monochromatic arm

The same argument gives another useful case.

### Lemma 4.3

Suppose one of the arms, say \(A\), is disjoint from \(D\) and is monochromatic in the red-blue colouring. If \(|D|\le m\), then there is a monochromatic component of order \(\Omega(m^{4/3})\).

### Proof

Since \(A\) is a connected red path, every red grid vertex \(q_{ij}\) is adjacent to the red vertex \(a_j\). Hence all red grid vertices lie in the single red component meeting \(A\), and there are at most \(k\) of them. Apply Lemma 4.1 exactly as in Lemma 4.2. \(\square\)

## 4.4 Oppositely monochromatic arms, with arbitrary deletions

The next case is more substantial.

### Lemma 4.4

Fix \(\delta<1/4\). There exists \(c_\delta>0\) such that the following holds for all sufficiently large \(m\).

Let \(|D|\le\delta m\). Suppose every vertex of \(A-D\) is red and every vertex of \(B-D\) is blue. Then every red-blue colouring of
\((J_m\boxtimes J_m)-D\) has a monochromatic component of order at least

\[
c_\delta m^{4/3}.
\]

### Proof

Assume all monochromatic components have order at most \(k\).

Let

\[
d_A=|D\cap A|,\quad d_B=|D\cap B|,
\quad d_Q=|D\cap Q|.
\]

Let \(r\) be the number of global red components meeting \(A-D\), and let \(s\) be the number of global blue components meeting \(B-D\).

Every grid vertex \(q_{ij}\notin D\) with \(a_j,b_i\notin D\) belongs to one of these \(r+s\) components: if it is red, it is adjacent to \(a_j\), and if it is blue, it is adjacent to \(b_i\). Therefore

\[
(m-d_A)(m-d_B)-d_Q\le (r+s)k.
\]

Since \(|D|\le\delta m\),

\[
r+s\ge \frac{m^2}{2k}
\tag{4}
\]

for all sufficiently large \(m\).

Now consider the red path \(A-D\). Its path-components form a sequence, each contained in one of the \(r\) global red components. A sequence using \(r\) labels has at least \(r-1\) transitions between unequal labels. By retaining every third such transition, we obtain at least

\[
t_A\ge \frac{r-1}{3}
\]

pairwise disjoint vertical gap-strips. No such strip contains a red left-to-right grid path, since such a path would merge the two corresponding red components.

Consequently, in each row and each selected vertical strip there is at least one blue or deleted grid vertex. For every row whose \(B\)-anchor survives, a blue such vertex belongs to one of the \(s\) blue components meeting \(B\). Hence

\[
t_A(m-d_B)\le sk+d_Q.
\tag{5}
\]

Symmetrically, there are at least \(t_B\ge(s-1)/3\) disjoint horizontal gap-strips and

\[
t_B(m-d_A)\le rk+d_Q.
\tag{6}
\]

Finally, every selected vertical strip and selected horizontal strip must have a deleted grid vertex in their intersection. Indeed, if their rectangular intersection were completely red-blue coloured, the standard grid crossing dichotomy gives either

* a red left-to-right path, merging the two red \(A\)-components, or
* a blue top-to-bottom path, merging the two blue \(B\)-components.

The strong grid contains all diagonal adjacencies, so the usual version with one colour using diagonal adjacency applies directly. Since the chosen strips are pairwise disjoint,

\[
d_Q\ge t_A t_B
 \ge \frac{(r-1)(s-1)}9.
\tag{7}
\]

Suppose without loss of generality that \(r\ge s\). From (4),

\[
r\ge \frac{m^2}{4k}.
\tag{8}
\]

For \(k=O(m^{4/3})\), the term \(d_Q\le\delta m\) is negligible compared with \(rm\). Thus (5), with constants weakened, gives

\[
s\ge \frac{rm}{Ck}
\tag{9}
\]

for an absolute constant \(C\). Substituting (8) and (9) into (7),

\[
d_Q
 \ge c\,rs
 \ge c\,\frac{r^2m}{k}
 \ge c'\frac{m^5}{k^3}.
\]

Since \(d_Q\le\delta m\),

\[
k^3\ge \frac{c'}{\delta}m^4,
\]

and hence

\[
k\ge c_\delta m^{4/3}.
\]

This proves the lemma. \(\square\)

# 5. The remaining gap

Lemmas 4.2–4.4 cover:

* the case where the universal vertex \(z\) is not deleted;
* the case where an entire arm survives monochromatically;
* the case where the two surviving arms are oppositely monochromatic, with arbitrary deletion locations.

They do not cover the following configuration:

1. \(z\in D\);
2. both arms have mixed colour traces, or deletions split both arms;
3. the same colour may occur on both arms.

The last point is delicate. Since \(A\) is complete to \(B\), all arm vertices of a colour appearing on both sides lie in one global component. This gives useful control over grid vertices matching an arm colour. However, a grid vertex whose two surviving anchors have the same colour may take the opposite colour and then need not attach to either arm. Large regions of such “unanchored” vertices are exactly what prevents the preceding component-count and crossing argument from immediately extending.

A naive treatment discards all rows and columns whose anchors are deleted. This incurs an exceptional Cartesian set of size

\[
|D\cap A|\,|D\cap B|,
\]

which may be quadratic in \(|D|\) and is too large for the desired linear deletion threshold. A sharper mesh-isoperimetric or crossing argument is needed.

Thus the robust statement (RF), and consequently Conjecture 8, is not proved here. What is established is:

\[
\boxed{t\ge3\text{ is necessary, and a proof of (RF) would establish the conjecture with the optimal }t=3.}
\]

The missing issue is a concrete finite stability problem for \(J_m\boxtimes J_m\), rather than an exponent-optimization problem.