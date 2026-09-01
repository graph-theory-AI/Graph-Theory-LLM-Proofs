```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open in general, but C=2 holds for every connected vertex-transitive digraph admitting a transitive abelian automorphism group, and more generally for a class of normal-chain Cayley digraphs.",
  "would_publish": false,
  "caveats": "The argument does not cover non-Cayley digraphs or general nonabelian Cayley digraphs, and it assumes the intended connected nontrivial formulation."
}
```

# Mathematical writeup

## 1. Formulation and conventions

For a finite loopless digraph \(D\), write

- \(\lambda(D)\) for the maximum number of vertices in a directed path;
- \(c(D)\) for the maximum number of vertices in a directed cycle.

The question asks whether there is an absolute \(C\) such that
\[
\lambda(D)\le Cc(D)
\]
for every connected vertex-transitive digraph \(D\).

If lengths are counted in edges instead, all estimates below remain valid, with a Hamilton path having length \(n-1\) rather than \(n\).

Connectedness, or some other nontriviality assumption, is necessary if paths are counted by vertices: an edgeless vertex-transitive digraph has a one-vertex path and no directed cycle. I use the connected formulation indicated by the source context.

A finite weakly connected vertex-transitive digraph is automatically strongly connected. Indeed, transitivity gives constant outdegree and indegree, and equality of the total indegree and outdegree shows these two constants are equal. Hence for every \(X\subseteq V(D)\),
\[
|\delta^+(X)|=|\delta^-(X)|.
\]
A source component of the condensation therefore has neither incoming nor outgoing arcs, contradicting weak connectivity unless it is all of \(D\).

---

## 2. A coset-stacking lemma

We use the right Cayley-digraph convention:
\[
\operatorname{Cay}(G,S):\qquad g\longrightarrow gs \quad (s\in S).
\]

### Lemma 2.1

Let \(H\triangleleft G\) be a proper normal subgroup. Suppose:

1. \(\operatorname{Cay}(H,T)\), where \(T\subseteq S\cap H\), has a Hamilton path;
2. \(\operatorname{Cay}(G/H,\overline S)\) has a Hamilton directed cycle, with every quotient arc lifted by an element of \(S\).

Then \(\operatorname{Cay}(G,S)\) has a Hamilton path and a directed cycle of length at least
\[
|G|-|H|+1.
\]

#### Proof

Put \(q=|H|\) and \(m=[G:H]\). Let
\[
P_H=(x_0=e,x_1,\ldots,x_{q-1}=h)
\]
be a Hamilton path in \(\operatorname{Cay}(H,T)\).

Write a Hamilton cycle in the quotient as
\[
\overline a_0=H,\overline a_1,\ldots,\overline a_{m-1},\overline a_m=H.
\]
For each \(j\), choose \(s_j\in S\) labelling the quotient arc
\[
\overline a_j\longrightarrow\overline a_{j+1}.
\]

Define representatives recursively by
\[
a_0=e,\qquad a_{j+1}=a_jhs_j.
\]
Since \(h\in H\) and \(H\triangleleft G\), we have \(a_jH=\overline a_j\).

For each \(0\le j<m\), take the left translate
\[
P_j=(a_jx_0,a_jx_1,\ldots,a_jx_{q-1}).
\]
This path covers precisely the coset \(a_jH\). Its terminal vertex is \(a_jh\), and there is an \(s_j\)-arc
\[
a_jh\longrightarrow a_jhs_j=a_{j+1}.
\]
Thus
\[
P_0,s_0,P_1,s_1,\ldots,s_{m-2},P_{m-1}
\]
is a Hamilton path of \(G\): the quotient cycle ensures that the \(m\) cosets are distinct and exhaust \(G/H\).

The terminal vertex \(a_{m-1}h\) has an \(s_{m-1}\)-arc to
\[
a_m=a_{m-1}hs_{m-1}.
\]
Because \(\overline a_m=H\), we have \(a_m\in H\). Hence \(a_m=x_r\) for some \(0\le r\le q-1\) in the first block \(P_0\). The suffix of the Hamilton path beginning at \(x_r\), followed by the final \(s_{m-1}\)-arc back to \(x_r\), is a simple directed cycle. Its length is
\[
|G|-r\ge |G|-(q-1)=|G|-|H|+1.
\]
This proves the lemma. \(\square\)

---

## 3. Normal-chain Cayley digraphs

### Theorem 3.1

Let \(D=\operatorname{Cay}(G,S)\). Suppose there are elements
\[
s_1,\ldots,s_k\in S
\]
such that, with
\[
G_i=\langle s_1,\ldots,s_i\rangle,
\]
one has a strict chain
\[
\{e\}=G_0<G_1<\cdots<G_k=G
\]
and
\[
G_{i-1}\triangleleft G_i
\qquad\text{for every }i.
\]
Then \(D\) has a Hamilton path and
\[
c(D)\ge |G|-|G_{k-1}|+1>\frac{|G|}{2}.
\]
In particular,
\[
\lambda(D)<2c(D).
\]

#### Proof

Proceed inductively along the chain. The trivial group has a one-vertex Hamilton path. Suppose a Hamilton path has been constructed in \(G_{i-1}\).

Because
\[
G_i/G_{i-1}=\langle s_iG_{i-1}\rangle
\]
is cyclic, repeated multiplication by \(s_iG_{i-1}\) gives a Hamilton directed cycle in the quotient. Lemma 2.1 therefore gives a Hamilton path in \(G_i\).

At the final step, Lemma 2.1 also gives
\[
c(D)\ge |G|-|G_{k-1}|+1.
\]
Since \(G_{k-1}\) is proper, its index is at least \(2\), so
\[
|G_{k-1}|\le \frac{|G|}{2}.
\]
Thus \(c(D)\ge |G|/2+1\), while the Hamilton path gives \(\lambda(D)=|G|\). Hence \(\lambda(D)<2c(D)\). \(\square\)

---

## 4. Abelian Cayley digraphs

### Corollary 4.1

If \(A\) is a finite abelian group and \(S\subseteq A\) generates \(A\), then
\[
\operatorname{Cay}(A,S)
\]
has a Hamilton path and a directed cycle of length greater than \(|A|/2\). Consequently,
\[
\lambda\bigl(\operatorname{Cay}(A,S)\bigr)
 <2c\bigl(\operatorname{Cay}(A,S)\bigr).
\]

#### Proof

Choose an inclusion-minimal generating subset
\[
T=\{s_1,\ldots,s_k\}\subseteq S.
\]
For any ordering of \(T\), all prefix subgroups
\[
A_i=\langle s_1,\ldots,s_i\rangle
\]
are strict: otherwise \(s_i\) would be generated by earlier elements and would be redundant in \(T\). Since \(A\) is abelian,
\[
A_{i-1}\triangleleft A_i.
\]
Theorem 3.1 applies to the spanning subdigraph \(\operatorname{Cay}(A,T)\), and its path and cycle are also present in \(\operatorname{Cay}(A,S)\). \(\square\)

A refined version follows from choosing any \(t\in T\) last. If
\[
H_t=\langle T\setminus\{t\}\rangle,
\]
then
\[
c\bigl(\operatorname{Cay}(A,S)\bigr)\ge |A|-|H_t|+1.
\]

### Corollary 4.2

The bound \(C=2\) holds for every connected vertex-transitive digraph admitting a transitive abelian subgroup of automorphisms.

#### Proof

Let \(A\le\operatorname{Aut}(D)\) be abelian and transitive. Its action is regular: if \(a\in A\) fixes one vertex \(v\), then for every \(w=b(v)\),
\[
a(w)=ab(v)=ba(v)=b(v)=w,
\]
so \(a\) is the identity automorphism.

After identifying \(V(D)\) with \(A\), the digraph is therefore a Cayley digraph \(\operatorname{Cay}(A,S)\). Connectedness implies that \(S\) generates \(A\), and Corollary 4.1 applies. \(\square\)

Thus this settles, with \(C=2\), all connected circulant digraphs and all Cayley digraphs of finite abelian groups.

### A genuinely non-Hamiltonian example

Let
\[
D=\operatorname{Cay}(\mathbb Z_6,\{2,3\}).
\]
It has the Hamilton path
\[
0,2,4,1,3,5
\]
and the directed \(5\)-cycle
\[
0,2,4,1,3,0.
\]
It has no Hamilton cycle: if a six-step closed walk uses \(a\) steps of size \(2\) and \(6-a\) steps of size \(3\), then its total displacement is
\[
2a+3(6-a)=18-a.
\]
Closure modulo \(6\) forces \(a=0\) or \(a=6\), but using only \(3\)'s or only \(2\)'s repeats after \(2\) or \(3\) steps. Hence \(c(D)=5\). The abelian result therefore is not merely a restatement of Hamiltonicity.

---

## 5. Two general structural inequalities

These do not prove the conjecture, but they constrain any possible counterexample family.

### Proposition 5.1: valency versus circumference

Let \(D\) be a finite loopless vertex-transitive digraph of outdegree \(d\). Then
\[
d\le c(D)-1.
\]

#### Proof

Let
\[
P=(v_1,\ldots,v_p)
\]
be a longest directed path. Every outneighbor of \(v_p\) belongs to \(P\), since otherwise \(P\) could be extended.

If \(v_p\to v_i\), then
\[
v_i,v_{i+1},\ldots,v_p,v_i
\]
is a directed cycle of length \(p-i+1\), so \(p-i+1\le c(D)\). Thus every outneighbor of \(v_p\) is among the final \(c(D)-1\) vertices preceding \(v_p\). Hence \(d\le c(D)-1\). \(\square\)

### Proposition 5.2: a return-distance bound

Let \(P\) be any simple directed path from \(x\) to \(y\), with \(\ell\) edges, in a strongly connected digraph \(D\). Then
\[
\ell\le \bigl(c(D)-1\bigr)\operatorname{dist}(y,x).
\]

#### Proof

Let \(R\) be a shortest directed path from \(y\) back to \(x\), of length
\[
r=\operatorname{dist}(y,x).
\]
The closed walk \(P R\), with edge occurrences distinguished, decomposes into simple directed cycles.

Every cycle in this decomposition contains at least one occurrence from \(R\), because the occurrences belonging to \(P\) alone form a directed path and contain no cycle. Therefore there are at most \(r\) cycles in the decomposition. Each has at most \(c(D)\) edges and at least one \(R\)-edge, hence contains at most \(c(D)-1\) occurrences from \(P\). Since all \(\ell\) edges of \(P\) occur in the decomposition,
\[
\ell\le r(c(D)-1).
\]
\(\square\)

For a longest path \(P=(v_1,\ldots,v_p)\), this gives
\[
p-1\le \bigl(c(D)-1\bigr)\operatorname{dist}(v_p,v_1)
 \le \bigl(c(D)-1\bigr)\operatorname{diam}^+(D).
\]
In particular, any family with \(\lambda(D)/c(D)\to\infty\) must have the reverse distance between the endpoints of every longest path tending to infinity at least on the order of \(\lambda(D)/c(D)\).

---

## 6. Relation to the source bound and remaining gap

The supplied source theorem
\[
c(D)=\Omega(n^{1/3})
\]
immediately yields an unconditional polynomial comparison
\[
\lambda(D)\le n=O\!\left(c(D)^3\right).
\]
Thus the open question is whether the exponent \(3\) can be reduced all the way to \(1\).

The abelian argument above relies essentially on normality: it stacks Hamilton paths in the cosets of \(H\), follows a Hamilton cycle in the quotient, and ensures that the final arc returns to the first coset. For a general nonabelian Cayley digraph, a subgroup generated by all but one generator need not be normal, so the translated blocks can revisit cosets or fail to cover them. General vertex-transitive digraphs may not admit any regular automorphism subgroup at all.

Accordingly, the argument proves a substantial natural special case but neither supplies a universal constant nor constructs an unbounded-ratio family. I have not checked whether the elementary abelian Cayley special case already appears in the literature, so no novelty claim is made.