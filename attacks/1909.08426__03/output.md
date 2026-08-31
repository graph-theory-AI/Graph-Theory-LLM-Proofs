```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains open, but deficient clique bags have Ramsey-bounded completion cells in every no-instance, and the ell=4 case is FPT with an additional parameter measuring induced P(1,t,t,t) obstructions.",
  "would_publish": false,
  "caveats": "The bounds are local or bi-parameterized; they do not give FPT in k alone and do not address the P7-free case."
}
```

## 1. Statement and interpretation

For positive integers \(t,\ell\), let \(P_\ell(t)\) be obtained from \(P_\ell\) by replacing every vertex by a clique of size \(t\), making consecutive cliques complete to one another, and making nonconsecutive cliques anticomplete. The parameter in Maximum Independent Set is the requested size \(k\), while \(t,\ell\) are fixed constants.

I do not prove or disprove the full conjecture. I give:

1. the range \(\ell\le 3\), which already follows from the source result;
2. a local Ramsey bound on every partially completed \(P_\ell(t)\);
3. examples showing that this bound is essentially best possible;
4. an FPT algorithm for \(P_4(t)\)-free graphs when additionally parameterized by their induced-\(P(1,t,t,t)\) deletion number;
5. an explicit family showing why that additional parameter cannot simply be bounded in terms of \(k\), even on connected and co-connected no-instances.

---

## 2. The already-covered range \(\ell\le 3\)

Let
\[
B_t:=P(1,t,t,t).
\]

### Proposition 2.1
For every fixed \(t\), Independent Set is FPT on \(P_\ell(t)\)-free graphs for \(\ell\le 3\). It is also FPT for \((\ell,t)=(4,1)\).

### Proof

For \(\ell=1\), \(P_1(t)=K_t\). If a \(K_t\)-free graph has at least \(R(k,t)\) vertices, Ramsey's theorem gives an independent set of size \(k\). Thus a no-instance has fewer than
\[
R(k,t)\le \binom{k+t-2}{t-1}
\]
vertices.

For \(\ell=2\), the two adjacent \(t\)-cliques form \(K_{2t}\), so
\[
P_2(t)=K_{2t}.
\]
The same argument gives a kernel with fewer than
\[
R(k,2t)\le \binom{k+2t-2}{2t-1}
\]
vertices.

For \(\ell=3\), the last three bags of \(B_t=P(1,t,t,t)\) induce \(P_3(t)\). Hence
\[
\operatorname{Forb}_{\mathrm{ind}}(P_3(t))
   \subseteq
\operatorname{Forb}_{\mathrm{ind}}(B_t).
\]
The FPT algorithm for \(B_t\)-free graphs established in the source paper therefore applies.

Finally, \(B_1=P_4=P_4(1)\). ∎

For \(t\ge2\), this containment does not cover \(P_4(t)\)-free graphs: \(B_t\) itself is \(P_4(t)\)-free simply because \(1+3t<4t\), but it is not \(B_t\)-free.

---

## 3. A Ramsey bound for deficient bags

A partial \(P_\ell(t)\)-model consists of pairwise disjoint sets
\[
C_1,\ldots,C_\ell
\]
such that every nonempty \(C_j\) is a clique, consecutive sets are complete to one another, and nonconsecutive sets are anticomplete.

Fix an index \(i\) and suppose
\[
|C_i|=s<t,\qquad |C_j|=t\quad(j\ne i),
\]
where \(s=0\) is allowed. Define the completion cell
\[
X_i(\mathcal C)
\]
to consist of vertices outside \(\bigcup_j C_j\) which are:

- complete to \(C_i\);
- complete to \(C_{i-1}\) and \(C_{i+1}\), when these exist;
- anticomplete to every \(C_j\) with \(|j-i|\ge2\).

### Lemma 3.1 — deficient-bag bound
If \(G\) is \(P_\ell(t)\)-free, then
\[
\omega\bigl(G[X_i(\mathcal C)]\bigr)<t-s.
\]
Consequently, if additionally \(\alpha(G)<k\), then
\[
|X_i(\mathcal C)|
   \le R(k,t-s)-1
   \le \binom{k+t-s-2}{t-s-1}-1.
\]

### Proof

If \(X_i(\mathcal C)\) contained a clique \(Q\) of size \(t-s\), then replacing \(C_i\) by \(C_i\cup Q\) would give an induced \(P_\ell(t)\): the new bag would be a \(t\)-clique, with precisely the required complete and anticomplete relations to the other bags. Thus \(X_i(\mathcal C)\) is \(K_{t-s}\)-free.

If \(|X_i(\mathcal C)|\ge R(k,t-s)\), Ramsey's theorem gives either a \(K_{t-s}\), which has just been excluded, or an independent set of size \(k\). ∎

### Important special case for \(P_4(t)\)

Let \(B,C,D\) be \(t\)-cliques inducing \(P_3(t)\), in that order, and put
\[
L(B,C,D)=
 \{x:x\text{ is complete to }B
       \text{ and anticomplete to }C\cup D\}.
\]
In a \(P_4(t)\)-free no-instance,
\[
|L(B,C,D)|\le R(k,t)-1.
\]

More generally, if \(S\subseteq L(B,C,D)\) is a clique of size \(s<t\), then
\[
\left|
 \{x\in L(B,C,D)\setminus S:x\text{ is complete to }S\}
\right|
\le R(k,t-s)-1.
\]

Thus every fixed three-bag core has only \(O_t(k^{t-1})\) possible vertices in its missing endpoint role, and the possible clique extensions of any partial endpoint are bounded by successively smaller Ramsey numbers.

### Algorithmic form

For fixed \(t,\ell\), all partial models can be enumerated in
\[
n^{(\ell-1)t+s+O(1)}
\]
time. If some completion cell has at least
\[
\binom{k+t-s-2}{t-s-1}
\]
vertices, the algorithm may safely return YES.

This is constructive: the standard recursive proof of
\[
R(a,b)\le\binom{a+b-2}{a-1}
\]
finds either the independent \(a\)-set or the clique \(b\)-set by partitioning into the neighborhood and antineighborhood of a vertex. Since the latter outcome is forbidden here, it returns an independent \(k\)-set.

This is only a one-sided preprocessing rule; it does not decide all remaining instances.

---

## 4. Near-tightness of the completion bound

The dependence on a Ramsey number cannot be replaced by a bound independent of \(k\).

### Proposition 4.1
Fix \(t\ge2\), \(k\ge3\), and \(0\le s<t\). Put \(r=t-s\). There is a \(P_4(t)\)-free graph \(G\) with \(\alpha(G)<k\) containing a partial model whose deficient endpoint has size \(s\) and whose completion cell has size
\[
R(k-1,r)-1.
\]

### Construction

By the definition of the Ramsey number, there is a graph \(X\) on
\[
R(k-1,r)-1
\]
vertices with
\[
\alpha(X)<k-1,\qquad \omega(X)<r.
\]

Let
\[
A=
\begin{cases}
X,&s=0,\\
K_s\vee X,&s>0,
\end{cases}
\]
where \(\vee\) denotes complete join. Construct \(G\) by substituting
\[
A,K_t,K_t,K_t
\]
into the four vertices of a \(P_4\). Thus consecutive parts are complete and nonconsecutive parts are anticomplete.

We have
\[
\omega(A)\le s+(r-1)=t-1.
\]

### Why \(G\) is \(P_4(t)\)-free

The canonical four \(t\)-vertex bags of \(P_4(t)\) have the following elementary modular property:

> Every proper module of \(P_4(t)\) is contained in one canonical bag.

Indeed, projecting a module onto the four bags would give a module of \(P_4\), and \(P_4\) is prime. If the projection met all four bags but the module were proper, a vertex in a partially met bag would distinguish vertices in that bag from vertices in a nonneighboring bag.

Each of the four host parts \(A,K_t,K_t,K_t\) is a module of \(G\). Therefore, if an induced \(P_4(t)\) met more than one host part, its intersection with every host part would be a proper module of the induced \(P_4(t)\), and hence would be contained in one target bag. Covering all four target bags then requires all four host parts, one target bag per host part. In particular, the copy would require a \(t\)-clique inside \(A\), contrary to \(\omega(A)<t\).

The copy cannot lie wholly inside one host part: the three \(K_t\) parts are too small, while \(A\) has clique number below \(t\), whereas \(P_4(t)\) contains a \(K_{2t}\). Thus \(G\) is \(P_4(t)\)-free.

### Independence number

Let \(a=\alpha(A)\). Since \(\alpha(X)\le k-2\), we have \(a\le k-2\). An independent set in \(G\) can use \(A\) together with at most one of the third and fourth host parts, or it can use one vertex from each of the second and fourth parts. Hence
\[
\alpha(G)=\max\{a+1,2\}=a+1\le k-1.
\]

Finally, take the \(K_s\) factor of \(A\) as the deficient first bag, and the other three host parts as the full bags. Its completion cell is exactly \(X\), of size \(R(k-1,t-s)-1\).

Thus Lemma 3.1 is tight up to replacing \(k\) by \(k-1\). ∎

---

## 5. An additional-parameter FPT result for \(\ell=4\)

Let
\[
\tau_t(G)=\min\{|Z|:G-Z\text{ is induced-}B_t\text{-free}\},
\qquad B_t=P(1,t,t,t).
\]

### Theorem 5.1
For every fixed \(t\), Independent Set is FPT parameterized by
\[
k+\tau_t(G).
\]
In particular, this holds on \(P_4(t)\)-free graphs.

### Proof

Because \(B_t\) has fixed size \(d=1+3t\), a deletion set \(Z\) of size at most \(p\) can be found by the standard bounded-search-tree algorithm:

1. find an induced copy of \(B_t\);
2. branch on deleting one of its \(d\) vertices;
3. stop after depth \(p\).

Detection takes \(n^{O_t(1)}\) time, so the search takes
\[
d^{p}n^{O_t(1)}.
\]
Iterative deepening finds a set \(Z\) of size \(\tau_t(G)\).

Now enumerate every independent set \(S\subseteq Z\). For each one, invoke the source paper's FPT algorithm on
\[
G-Z-N(S)
\]
with target \(k-|S|\). This graph is an induced subgraph of the \(B_t\)-free graph \(G-Z\), and is therefore \(B_t\)-free.

Every independent set \(I\) in \(G\) occurs in the branch \(S=I\cap Z\), and conversely an independent set returned in that branch can be united with \(S\). The total running time is
\[
(1+3t)^{\tau_t(G)}n^{O_t(1)}
  +2^{\tau_t(G)}f_t(k)n^{O_t(1)},
\]
where \(f_t\) comes from the source algorithm. ∎

The same argument works with the maximum number \(\nu_t(G)\) of vertex-disjoint induced \(B_t\)'s as additional parameter: the union of any maximal such packing is a deletion set of size at most
\[
(1+3t)\nu_t(G).
\]

---

## 6. Why the additional parameter is not controlled by \(k\)

The preceding theorem does not imply the conjecture, even after restricting to connected and co-connected graphs.

### Proposition 6.1
For every \(t\ge2\) and every \(m\ge3\), there is a connected and co-connected \(P_4(t)\)-free graph \(G^{(m)}\) such that
\[
\alpha(G^{(m)})=2
\]
and \(G^{(m)}\) contains \(m\) vertex-disjoint induced copies of \(B_t\).

### Construction and proof

Let \(F_i\), \(1\le i\le m\), be disjoint copies of \(\overline{B_t}\). Join \(F_i\) to \(F_{i+1}\) by exactly one edge, so these new edges form bridges between consecutive blocks. Let the resulting connected graph be \(F\), and put
\[
G^{(m)}=\overline F.
\]

Each \(F_i\) is bipartite: \(\overline{P_4}\cong P_4\), and complementation turns the clique bags of \(B_t\) into independent bags. Adding bridges between the blocks creates no triangles. Hence \(F\) is triangle-free, and therefore
\[
\alpha(G^{(m)})=\omega(F)\le2.
\]
Since \(F\) has edges, equality holds.

Each block induces \(B_t\) in \(G^{(m)}\), giving \(m\) vertex-disjoint copies.

It remains to show that \(G^{(m)}\) is \(P_4(t)\)-free. Let
\[
J=\overline{P_4(t)}.
\]
This is an independent-set blow-up of a \(P_4\), with all four bags of size \(t\). Every edge of \(J\) lies in a \(K_{t,t}\), and hence, because \(t\ge2\), lies on a four-cycle. Thus \(J\) has no bridge.

An induced copy of \(J\) in \(F\) cannot meet two different blocks \(F_i\): any connected induced subgraph spanning blocks must use one of the unique interblock edges, and that edge is then a bridge of the induced subgraph. Nor can \(J\) lie inside one \(F_i\), because
\[
|V(F_i)|=1+3t<4t=|V(J)|.
\]
Therefore \(F\) is induced-\(J\)-free, equivalently \(G^{(m)}\) is induced-\(P_4(t)\)-free.

Finally, \(F\) is connected, so \(G^{(m)}\) is co-connected. The graph \(G^{(m)}\) is also connected: between distinct blocks all edges are present except the single complement of a bridge. Given a nonadjacent pair, choose a vertex in a third block avoiding the at most two exceptional bridge endpoints; it is adjacent to both. ∎

Taking \(k=3\), these are no-instances with unbounded \(\tau_t\) and \(\nu_t\). Thus neither the obstruction-deletion result nor a bounded packing argument yields FPT parameterized by \(k\) alone.

---

## 7. Remaining gap

The deficient-bag lemma gives strong control after fixing all other bags: in a no-instance every role-completion cell has size bounded by a polynomial in \(k\) for fixed \(t\). What is missing is a global way to compress or organize the potentially unbounded number of different cores. Proposition 6.1 shows that even many vertex-disjoint \(P(1,t,t,t)\) obstructions can occur in connected, co-connected \(P_4(t)\)-free no-instances.

No argument above addresses the central \(t=1,\ell=7\) case: when \(t=1\), the completion-cell lemma merely says that a partial induced path cannot be extended to a forbidden path, which is tautological. Thus the full conjecture, and in particular FPT for general \(P_7\)-free graphs, remains unresolved.