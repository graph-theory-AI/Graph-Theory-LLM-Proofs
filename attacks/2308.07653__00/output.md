```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a universal lower bound \(m(C_t\\times C_s)\\ge 8\), reprove exactness \(m(C_3\\times C_s)=8\) for \(s>36\), and obtain sharper upper bounds for \(16\\le s\\le36\).",
  "would_publish": false,
  "caveats": "Exact values remain open when both dimensions are at least four and for most \(C_3\\times C_s\) with \(s\\le36\)."
}
```

## 1. Statement of the partial result

Throughout, \(C_t\times C_s\) denotes the Cartesian product, and \(t,s\ge 3\).

Let \(m(H)\) be the largest cardinality of a family \(\mathcal C\) of spanning subgraphs of \(H\) such that \(A\triangle B\) is connected and spanning for every distinct \(A,B\in\mathcal C\).

I prove the following.

### Theorem

1. For every \(t,s\ge3\),
   \[
   8\le m(C_t\times C_s)\le16.
   \]

2. More generally, if a connectivity code of size \(M\) exists in \(C_t\times C_s\), then
   \[
   s\,R_{2^t}(M)\le \binom M2,
   \qquad
   t\,R_{2^s}(M)\le \binom M2,
   \]
   where, writing \(M=aq+b\) with \(0\le b<q\),
   \[
   R_q(M):=(q-b)\binom a2+b\binom{a+1}{2}.
   \]

3. Consequently, for \(s\ge3\),
   \[
   m(C_3\times C_s)\le
   \begin{cases}
   16,&3\le s\le15,\\
   12,&s=16,\\
   11,&17\le s\le18,\\
   10,&19\le s\le22,\\
   9,&23\le s\le36,\\
   8,&s\ge37.
   \end{cases}
   \]
   In particular,
   \[
   \boxed{m(C_3\times C_s)=8\quad\text{for all }s>36.}
   \]
   By symmetry the same holds with \(t\) and \(s\) interchanged.

The supplied source already records \(m(C_3\times C_3)=16\). The intermediate cases in the displayed table are not settled here.

---

## 2. The elementary upper bound \(m\le16\)

Let \(H=C_t\times C_s\), which is 4-regular. Fix a vertex \(v\). For each codeword \(A\), record the four-bit incidence vector of \(A\) on the four edges incident with \(v\).

These vectors must be distinct: if two codewords \(A,B\) have the same incidence vector, then \(A\triangle B\) has no edge incident with \(v\), so \(v\) is isolated in \(A\triangle B\). Therefore
\[
|\mathcal C|\le2^4=16.
\]

---

## 3. A linear construction of eight codewords for every torus

### 3.1 Vector-labelled edges

Let \(H\) be a graph and let
\[
\lambda:E(H)\longrightarrow \mathbb F_2^3
\]
be an edge labelling. For \(x\in\mathbb F_2^3\), define
\[
E_x:=\{e\in E(H):x\cdot\lambda(e)=1\}.
\]
Then
\[
E_x\triangle E_y=E_{x+y}.
\]
Thus, if \((V(H),E_x)\) is connected for every \(x\ne0\), the eight subgraphs
\[
\{(V(H),E_x):x\in\mathbb F_2^3\}
\]
form a connectivity code.

We construct such a labelling for every \(C_t\times C_s\).

---

### 3.2 A base labelling of \(C_3\times C_s\)

Write the three vertices in each \(C_3\)-layer as \(A_j,B_j,C_j\), where \(j\in\mathbb Z_s\).

Put
\[
e_A=(1,0,0),\qquad e_B=(0,1,0),\qquad e_C=(0,0,1),
\]
and label the longitudinal edges by
\[
\lambda(A_jA_{j+1})=e_A,\quad
\lambda(B_jB_{j+1})=e_B,\quad
\lambda(C_jC_{j+1})=e_C.
\]

Set
\[
u=(1,1,1),\qquad v=(1,1,0),\qquad w=(1,0,1),\qquad z=(0,1,1).
\]
Notice that \(u,v,w\) form a basis of \(\mathbb F_2^3\).

For the three edges inside layer \(j\), use the following periodic labelling:

\[
\begin{array}{c|ccc}
j\bmod3&
A_jB_j&B_jC_j&C_jA_j\\ \hline
0&u&z&w\\
1&v&u&w\\
2&w&v&z
\end{array}
\tag{3.1}
\]

The selected intralayer edges for the seven nonzero \(x\)'s are:

\[
\begin{array}{c|ccc}
x&j\equiv0&j\equiv1&j\equiv2\\ \hline
100&AB,CA&AB,BC,CA&AB,BC\\
010&AB,BC&AB,BC&BC,CA\\
001&AB,BC,CA&BC,CA&AB,CA\\
110&BC,CA&CA&AB,CA\\
101&BC&AB&BC,CA\\
011&CA&AB,CA&AB,BC\\
111&AB&BC&\varnothing
\end{array}
\tag{3.2}
\]

This table proves connectivity:

- If \(x\) has weight one, exactly one of the three longitudinal row-cycles is selected, and the selected intralayer edges connect all three vertices of every layer to that cycle.
- If \(x\) has weight two, two longitudinal row-cycles are selected. In every layer, the remaining vertex has a selected edge to one of them, and one of the layer types joins the two selected row-cycles.
- If \(x=111\), all three longitudinal row-cycles are selected. A type-0 layer supplies an \(AB\)-edge and a type-1 layer supplies a \(BC\)-edge, so the three cycles are joined.

Every \(s\ge3\) contains the layer types \(0,1,2\). Hence this gives eight codewords in every \(C_3\times C_s\).

To pass from \(C_3\times C_s\) to arbitrary \(C_t\times C_s\), we use a row-insertion operation.

---

### 3.3 Row-insertion lemma

Suppose a vector-labelled graph contains edges
\[
A_jB_j,\qquad j\in\mathbb Z_s,
\]
with labels \(a_j\). Replace every \(A_jB_j\) by a path
\[
A_jR_jB_j,
\]
giving both new path edges the label \(a_j\). Add cycle edges \(R_jR_{j+1}\), with labels \(d_j\).

For fixed \(x\ne0\), call \(R_j\) an anchor if
\[
x\cdot a_j=1.
\]
The selected old graph, after subdividing each selected \(A_jB_j\), remains connected and contains all anchors. Therefore the new selected graph is connected provided every component of
\[
\bigl(\{R_j\},\,\{R_jR_{j+1}:x\cdot d_j=1\}\bigr)
\]
contains an anchor.

This gives the following immediate lemma.

### Lemma

If, for every \(x\ne0\), every new vertex \(R_j\) has a path of selected \(R\)-cycle edges to an anchor, then row insertion preserves the property that every nonzero \(E_x\) is connected.

---

### 3.4 Labels for the inserted rows

For the base edge family \(A_jB_j\), the labels in (3.1) are
\[
a_j=
\begin{cases}
u,&j\equiv0\pmod3,\\
v,&j\equiv1\pmod3,\\
w,&j\equiv2\pmod3.
\end{cases}
\tag{3.3}
\]

Normally put
\[
d_j=a_j+a_{j+1},
\tag{3.4}
\]
with indices modulo \(s\), subject to these modifications:

- If \(s\equiv1\pmod3\), replace
  \[
  d_{s-1}=0
  \quad\text{by}\quad
  d_{s-1}=v+w.
  \tag{3.5}
  \]
- If \(s\equiv2\pmod3\), replace
  \[
  d_0=d_{s-2}=u+v
  \quad\text{by}\quad
  d_0=d_{s-2}=u+v+w.
  \tag{3.6}
  \]

We verify the anchor condition. For fixed \(x\ne0\), put
\[
U=x\cdot u,\qquad V=x\cdot v,\qquad W=x\cdot w.
\]
Since \(u,v,w\) are a basis, \((U,V,W)\ne(0,0,0)\).

With the unmodified rule (3.4), the edge \(R_jR_{j+1}\) is selected exactly when the two adjacent anchor bits differ.

#### Case \(s\equiv0\pmod3\)

Every three consecutive labels are \(u,v,w\) in some order. Thus no three consecutive anchor bits can all be zero. Every nonanchor has an anchor as a neighbour, and the intervening edge is selected.

#### Case \(s\equiv1\pmod3\)

At the cyclic join the label sequence contains
\[
\cdots,v,w,u,u,v,w,\cdots.
\]
Only the patterns \((U,V,W)=010\) and \(001\) can create a run of three zero anchor bits there. In both cases
\[
x\cdot(v+w)=V+W=1,
\]
so the modified edge between the two consecutive \(u\)-positions joins the otherwise unsupported vertices to an anchored side. If \(U=1\), those positions are themselves anchors; if \(V=W=1\), each is adjacent to an anchor. Hence every component contains an anchor.

#### Case \(s\equiv2\pmod3\)

The exceptional cyclic segment is
\[
w,u,v,u,v,w.
\]
If \(W=0\), the original transition rule already suffices. If \(W=1\), there are four possibilities:

- \(001\): the status sequence is \(1,0,0,0,0,1\). The two modified \(u\)-\(v\) edges are selected, attaching the first two zero vertices to the left anchor and the last two to the right anchor.
- \(101\): the zero vertices are the two \(v\)-positions. The modified edges are absent, but each zero \(v\)-vertex retains its other selected edge to an anchor.
- \(011\): symmetrically, the two zero \(u\)-vertices each retain a selected edge to an anchor.
- \(111\): every position is an anchor.

Thus the anchor condition holds in all cases.

We may consequently insert a new row while preserving connectivity of all seven nonzero \(E_x\). Moreover, either of the two new seams replacing the old \(A_jB_j\)-seam again has labels \(a_j\), so the operation can be repeated. Starting from \(C_3\times C_s\) and repeating it \(t-3\) times gives \(C_t\times C_s\).

Therefore
\[
\boxed{m(C_t\times C_s)\ge8\qquad(t,s\ge3).}
\]

---

## 4. Collision counting across cyclic interfaces

Let \(\mathcal C\) be a connectivity code of size \(M\) in \(C_t\times C_s\). For each \(j\in\mathbb Z_s\), let
\[
F_j=\{(i,j)(i,j+1):i\in\mathbb Z_t\}
\]
be the \(t\)-edge interface between consecutive \(C_t\)-layers.

For \(A\in\mathcal C\), record its signature
\[
\sigma_j(A):=E(A)\cap F_j\in\{0,1\}^t.
\]

If \(\sigma_j(A)=\sigma_j(B)\), then \(A\triangle B\) has no edge in \(F_j\). A fixed pair \(A,B\) can have equal signatures at at most one interface: if it had equal signatures at two distinct interfaces \(F_j,F_k\), then \(A\triangle B\) would contain no edge across either interface. Those two interfaces separate the cyclic sequence of layers into two nonempty arcs, so \(A\triangle B\) would be disconnected.

It remains to count how many pairs must collide at one interface. There are \(q=2^t\) possible signatures. If the \(M\) codewords are distributed among these \(q\) signatures with fiber sizes \(n_1,\dots,n_q\), the number of colliding pairs is
\[
\sum_{r=1}^q\binom{n_r}{2}.
\]
This is minimized when the fiber sizes differ by at most one. Writing \(M=aq+b\), \(0\le b<q\), the minimum is
\[
R_q(M)=(q-b)\binom a2+b\binom{a+1}{2}.
\]
Summing collisions over all \(s\) interfaces, while observing that each unordered codeword pair is counted at most once, gives
\[
sR_{2^t}(M)\le\binom M2.
\tag{4.1}
\]
Interchanging the factors gives
\[
tR_{2^s}(M)\le\binom M2.
\tag{4.2}
\]

---

## 5. Consequences for \(C_3\times C_s\)

Here \(q=2^3=8\), and the degree bound gives \(M\le16\). For \(9\le M\le16\),
\[
R_8(M)=M-8.
\]
Thus a code of size \(M\) must satisfy
\[
s(M-8)\le\binom M2.
\tag{5.1}
\]

The relevant thresholds are:

\[
\begin{array}{c|c}
M&\text{necessary upper bound on }s\\ \hline
9&36\\
10&22\\
11&18\\
12&16\\
13&15\\
14&15\\
15&15\\
16&15
\end{array}
\]

Together with the universal lower bound \(8\), this yields

\[
m(C_3\times C_s)\le
\begin{cases}
16,&3\le s\le15,\\
12,&s=16,\\
11,&17\le s\le18,\\
10,&19\le s\le22,\\
9,&23\le s\le36,\\
8,&s\ge37.
\end{cases}
\]

Hence
\[
m(C_3\times C_s)=8\qquad(s>36).
\]

The same conclusions hold for \(C_t\times C_3\).

---

## 6. What remains open

This does not determine \(m(C_t\times C_s)\) in general.

- When \(t,s\ge4\), the collision inequality is vacuous for \(M\le16\), since a \(t\)-edge interface already has at least \(16\) possible signatures.
- For \(C_3\times C_s\), the exact values remain undetermined here for
  \[
  4\le s\le36,
  \]
  except for the supplied known value \(m(C_3\times C_3)=16\).
- In particular, the bounds above leave open whether sizes \(9,10,11,\) or \(12\) actually occur in the indicated ranges.

Thus the full catalog problem remains open, but the universal construction and the collision hierarchy give a self-contained exact result for all sufficiently long width-three tori and sharper finite-width bounds.