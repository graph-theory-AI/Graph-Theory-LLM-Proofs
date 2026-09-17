```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Two structural sufficient conditions for prime targets, together with explicit constructions, settle every target on three, four, or five vertices.",
  "would_publish": false,
  "caveats": "No full characterization or literature-priority claim; the arguments still leave, for example, C3⊕C3 and transitive targets T_h with h≥7 untreated."
}
```

# 1. Results and conventions

I use the intended **nonvacuous** convention: the host must have at least one arc. Without this, a one-vertex host makes the question trivial for every \(H\) with at least two vertices. “Countable” includes finite.

Write \(T_h\) for the transitive tournament of order \(h\), and \(H^e\) for the result of reversing an arc \(e\).

A set \(M\subseteq V(H)\) is a **module** if every vertex outside \(M\) either dominates all of \(M\) or is dominated by all of \(M\). A tournament is **prime** if its only modules are the empty set, singletons, and its whole vertex set.

The results proved below are:

1. **Every tournament on three, four, or five vertices admits a countable arc-reversal-saturated host.**
2. A prime tournament \(H\) admits a countably infinite host if either:
   - some arc reversal of \(H\) is not strongly connected; or
   - \(H-v\) is prime for every vertex \(v\).
3. In particular, the first structural condition covers every prime tournament with a vertex of indegree one or outdegree one, including the entire family of alternating-wheel tournaments \(W_{2k+1}\).
4. For transitive targets, every nonvacuous saturated host is necessarily **finite and prime**. Explicit hosts exist for \(T_3,T_4,T_5,T_6\).

The lexicographic constructions and the five-vertex classification go beyond the supplied attempt. I recheck below the rational-order argument and all Paley-tournament certificates that I use from that attempt.

These are sufficient conditions, not a characterization.

# 2. A lexicographic construction for prime targets

## 2.1 A rooted-universal lexicographic tournament

Let \(B\) be a finite tournament with at least two vertices. Choose a periodic sequence
\[
b=(b_0,b_1,\ldots)
\]
in which every vertex of \(B\) occurs. Define
\[
V(L(B))=
\left\{x\in V(B)^{\mathbb N}:
x_i=b_i\text{ for all but finitely many }i\right\}.
\]
For distinct \(x,y\), let \(k\) be their first differing coordinate, and put
\[
x\to y \quad\Longleftrightarrow\quad x_k\to y_k\text{ in }B.
\]
This is a countably infinite tournament.

We need two properties.

**Lemma 2.1.**

1. Every finite prime subtournament of \(L(B)\) embeds into \(B\).
2. Fix \(x\in L(B)\), a coordinate bound \(k\), a subtournament \(J\subseteq B\), and a distinguished vertex \(a\in J\). There are infinitely many copies of \(J\) in \(L(B)\), rooted at \(x\) as \(a\), all agreeing with \(x\) through coordinate \(k\), and with pairwise disjoint sets of non-root vertices.

**Proof.**

For (1), let \(S\) induce a prime tournament, and let \(j\) be the first coordinate at which the members of \(S\) are not all equal. The nonempty fibers
\[
S_c=\{x\in S:x_j=c\},\qquad c\in V(B),
\]
are modules in \(L(B)[S]\). There are at least two fibers. Primality therefore forces every fiber to be a singleton. Projection onto coordinate \(j\) embeds \(L(B)[S]\) into \(B\).

For (2), choose \(j>k\) with \(x_j=a\). There are infinitely many such \(j\), because \(x\) differs from the periodic sequence \(b\) only finitely often. For each \(c\in J\), take the sequence obtained from \(x\) by changing coordinate \(j\) to \(c\). These sequences induce \(J\), with \(a\) represented by \(x\). Different choices of \(j\) give disjoint non-root sets. ∎

## 2.2 Prime targets with a one-arc directed cut

**Theorem 2.2.**  
Let \(H\) be a finite prime tournament of order at least three. Suppose that reversing some arc of \(H\) makes it not strongly connected. Then \(H\) has a countably infinite arc-reversal-saturated host.

In fact, the constructed host creates \(H\) after every nonempty finite set of arc reversals.

**Proof.**

A prime tournament of order at least three is strongly connected. Indeed, otherwise its strongly connected components give either a nontrivial module or a transitive tournament, which also has a nontrivial module.

Let \(F=H^e\) be not strongly connected. Choose a nontrivial directed cut
\[
V(F)=A\mathbin{\dot\cup}B,\qquad A\Rightarrow B.
\]
Since \(H\) is strongly connected, \(e\) crosses this cut. Thus there are \(a\in A\), \(b\in B\) such that
\[
b\to a\text{ in }H,\qquad a\to b\text{ in }F,
\]
and every other arc between \(A\) and \(B\) is directed from \(A\) to \(B\).

Take
\[
G=L(F).
\]
It is \(H\)-free: by Lemma 2.1(1), a prime copy of \(H\) in \(G\) would embed into \(F\). Since \(F\) has the same order as \(H\), that would imply \(F\cong H\), contrary to their different strong-connectivity status.

Now fix any arc \(x\to y\) of \(G\), and let \(k\) be its first differing coordinate. The two prefix fibers containing \(x\) and \(y\), respectively, have all arcs directed from the former to the latter.

Inside the first fiber, use Lemma 2.1(2) to place a copy of \(F[A]\), with \(a\) represented by \(x\). Inside the second, place a copy of \(F[B]\), with \(b\) represented by \(y\). Their union is a copy of \(F\), rooted at \(x\to y\). Reversing that arc produces \(H\).

Moreover, these witnesses can be chosen with pairwise disjoint non-root sets. Given a finite nonempty set of reversed arcs, select one of them, say \(xy\), and choose a witness whose non-root vertices avoid the endpoints of all the other reversed arcs. Only \(xy\) changes within that witness, so it becomes \(H\). ∎

Equivalently, the hypothesis says that \(H\) has a partition \(A,B\) with exactly one arc directed from \(B\) to \(A\).

**Corollary 2.3.**  
Every prime tournament with a vertex of indegree one or outdegree one admits a countably infinite host.

For example, a vertex of indegree one gives the required cut with \(A\) equal to that singleton.

## 2.3 An infinite family not covered by the supplied connectivity criterion

Define \(W_{2k+1}\) on
\[
\{v,t_1,\ldots,t_{2k}\}
\]
by
\[
t_i\to t_j\quad(i<j),
\]
and
\[
v\to t_i\quad(i\text{ odd}),\qquad
t_i\to v\quad(i\text{ even}).
\]

These tournaments are prime. To see this, a module avoiding \(v\) would have to be an interval in the transitive order \(t_1,\ldots,t_{2k}\); an interval with at least two vertices is distinguished by \(v\), because the directions alternate.

If a proper module contains \(v\) and at least one \(t_i\), every outside odd-indexed vertex must occur after all the \(t_i\)'s in the module, while every outside even-indexed vertex must occur before all of them. This first forces \(t_1,t_{2k}\) into the module, and then forces every \(t_i\) into it.

Finally, \(t_1\) has indegree one. Hence Theorem 2.2 gives:

**Corollary 2.4.**  
For every \(k\geq1\), \(W_{2k+1}\) has a countably infinite arc-reversal-saturated host.

For \(k\geq3\), these examples lie outside both the supplied two-vertex-deletion strong-connectivity criterion and the one-reversal-from-transitive family.

# 3. A different amalgamation: prime vertex-deletions

The following construction covers a second class of prime targets.

**Theorem 3.1.**  
Let \(H\) be a finite prime tournament of order at least three such that \(H-v\) is prime for every \(v\in V(H)\). Then \(H\) has a countably infinite arc-reversal-saturated host.

The important feature is that gadgets are attached only to arcs that are not already protected.

## 3.1 The extension lemma

Choose an arc \(e\) for which
\[
F=H^e\not\cong H.
\]
Such an arc exists. Otherwise the isomorphism class of \(H\) would be closed under every one-arc reversal and hence, by connectivity of the labeled arc-reversal hypercube, would contain every tournament of its order.

Let \(C\) be a finite \(H\)-free tournament, and suppose that \(u\to v\) is **unprotected**, meaning that \(C^{uv}\) is also \(H\)-free.

Attach a copy of \(F\), identifying its distinguished reversed arc with \(u\to v\). Let \(W\) be its fresh vertices and put
\[
Z=V(C)\setminus\{u,v\}.
\]
For \(w\in W\) and \(z\in Z\), set
\[
w\to z\quad\Longleftrightarrow\quad u\to z.
\]
Thus every fresh vertex clones \(u\)'s relations to \(Z\). Call the extension \(D\).

**Lemma 3.2.**  
The tournament \(D\) is \(H\)-free.

**Proof.**

A copy \(K\cong H\) would have to meet both \(W\) and \(Z\), since neither \(C\) nor the attached \(F\) contains \(H\). Set
\[
P=V(K)\cap(W\cup\{u\}).
\]
In particular, \(P\neq\varnothing\).

If \(v\notin K\) and \(|P|\geq2\), then \(P\) is a proper nontrivial module of \(K\), contradicting primality of \(H\).

If \(v\in K\) and \(|P|\geq2\), then \(P\) is a proper nontrivial module of \(K-v\), contradicting primality of every vertex-deletion of \(H\).

Consequently \(P=\{w\}\) for some fresh vertex \(w\). Replace \(w\) by \(u\). Its relations to all vertices of \(K\cap Z\) remain unchanged. If \(v\) is present, its relation to \(u\) is either the relation in \(C\) or the relation in \(C^{uv}\). Thus the replacement gives a copy of \(H\) in one of those two tournaments, a contradiction. ∎

Reversing \(uv\) in \(D\) turns the attached \(F\) into \(H\).

## 3.2 Iteration

Start with a two-vertex tournament. Assign serial numbers to arcs as they appear.

In round \(r\):

1. add one new vertex dominating all existing vertices;
2. inspect all existing arcs with serial number at most \(r\);
3. whenever an inspected arc is unprotected, apply Lemma 3.2.

Adding a dominating vertex preserves \(H\)-freeness because \(H\) is strongly connected. Every round is finite, and every intermediate tournament is \(H\)-free. The union is countably infinite.

Every arc is eventually inspected. At that time it is either already protected or receives a witness. Protection persists under subsequent extensions. The union is therefore saturated, proving Theorem 3.1. ∎

# 4. Three prime five-vertex targets in one host

For tournaments \(A,B,C\), write
\[
\Delta(A,B,C)
\]
for their cyclic composition, with all arcs
\[
A\Rightarrow B,\qquad B\Rightarrow C,\qquad C\Rightarrow A.
\]

Let
\[
D=\Delta(T_2,T_2,T_1).
\]
Label its two nontrivial blocks
\[
a_0\to a_1,\qquad b_0\to b_1,
\]
and its remaining vertex \(c\), so that
\[
\{a_0,a_1\}\Rightarrow\{b_0,b_1\}\Rightarrow\{c\}
\Rightarrow\{a_0,a_1\}.
\]
Define
\[
C_5=D^{a_0b_1},\qquad
U_5=D^{a_0b_0},\qquad
W_5=D^{a_1b_0}.
\]
Here \(C_5\) is the regular five-vertex tournament, and these are precisely the three prime tournaments of order five. An elementary verification of the five-vertex classification appears in Section 7.

**Proposition 4.1.**  
The countable tournament \(L(C_3)\) is simultaneously arc-reversal-saturated for \(C_5,U_5,W_5\).

**Proof.**

Lemma 2.1(1) shows that \(L(C_3)\) contains no prime tournament of order five.

Fix an arc \(x\to y\), and consider its first differing coordinate. Its three coordinate fibers form a directed triangle, with the first two containing \(x,y\). Choose one vertex \(c\) in the third fiber.

Each of the first two fibers contains both an inneighbor and an outneighbor of its specified root. Consequently we can place a rooted copy of \(D\) with:

- \(x=a_0,y=b_1\), to create \(C_5\);
- \(x=a_0,y=b_0\), to create \(U_5\);
- \(x=a_1,y=b_0\), to create \(W_5\).

Only the direction of the additional vertex within each of the first two fibers needs to be selected appropriately. Reversing \(xy\) produces the desired target. ∎

# 5. Explicit finite hosts

All arithmetic certificates in this section can be checked directly; no computational search result is being assumed.

## 5.1 Quadratic-residue tournaments

For \(q\in\{3,7,11,19\}\), let \(P_q\) have vertex set \(\mathbb Z_q\), with
\[
x\to y\quad\Longleftrightarrow\quad y-x\in R_q,
\]
where
\[
\begin{aligned}
R_3&=\{1\},\\
R_7&=\{1,2,4\},\\
R_{11}&=\{1,3,4,5,9\},\\
R_{19}&=\{1,4,5,6,7,9,11,16,17\}.
\end{aligned}
\]
Translations and multiplication by a nonzero quadratic residue are automorphisms. In particular, each \(P_q\) is arc-transitive.

### Transitive targets

These tournaments give hosts for \(T_3,T_4,T_5,T_6\), respectively.

To check freeness, it suffices to inspect the outneighborhood of \(0\):

- In \(P_3\), it has one vertex.
- In \(P_7\), it is the directed triangle on \(\{1,2,4\}\).
- In \(P_{11}\), it is the regular five-vertex tournament, in cyclic order
  \[
  1,4,5,9,3.
  \]
  It has no \(T_4\), since every vertex has only two outneighbors within this set.
- In \(P_{19}\), put \(R=R_{19}\). The outneighbors of \(1\) within \(R\) are
  \[
  \{5,6,7,17\},
  \]
  which are not transitive because
  \[
  5\to6\to17\to5.
  \]
  Multiplication by elements of \(R\) acts transitively on \(R\). Thus every vertex of \(P_{19}[R]\) has exactly four outneighbors there, and those four are nontransitive. A \(T_5\) in \(R\) would have a source whose entire four-element outneighborhood was transitive, which is impossible.

A transitive set has a source, so these observations prove the claimed freeness of the four hosts.

After reversing \(0\to1\), the following rows are transitive orders:

\[
\begin{array}{c|c|l}
\text{host}&\text{target}&\text{transitive order after reversal}\\ \hline
P_3&T_3&1,2,0\\
P_7&T_4&1,3,5,0\\
P_{11}&T_5&8,1,2,6,0\\
P_{19}&T_6&14,1,12,2,18,0.
\end{array}
\]

In every row, all forward differences belong to the specified residue set except \(0-1\), whose arc has been reversed. Arc-transitivity completes the saturation verification.

## 5.2 Further targets saturated by \(P_7\)

Set
\[
E=\Delta(C_3,T_1,T_1).
\]

Every five-vertex subtournament of \(P_7\) is isomorphic to \(U_5\). Indeed, arc-transitivity implies transitivity on unordered pairs, hence on their five-vertex complements. For the complement of \(\{0,1\}\), the isomorphism from the definition of \(U_5\) above is
\[
a_0\mapsto4,\quad a_1\mapsto5,\quad
b_0\mapsto2,\quad b_1\mapsto6,\quad c\mapsto3.
\]
This verifies the assertion directly.

Thus \(P_7\) is free of \(D,E,C_5,W_5\). On the fixed vertex set
\[
S=\{2,3,4,5,6\},
\]
we have the following certificates:

\[
\begin{array}{c|c|l}
\text{target}&\text{arc reversed}&\text{certificate}\\ \hline
D&2\to4&
(a_0,a_1;b_0,b_1;c)=(4,5;2,6;3)\\
E&2\to3&
\{2,4,5\}\Rightarrow\{6\}\Rightarrow\{3\}
\Rightarrow\{2,4,5\},\ \{2,4,5\}\cong C_3\\
C_5&2\to6&
\text{all five resulting outdegrees are }2\\
W_5&3\to4&
(a_0,a_1;b_0,b_1;c)=(2,6;4,3;5)
\text{ in }D^{a_1b_0}.
\end{array}
\]

Arc-transitivity therefore proves:

**Proposition 5.1.**  
The finite tournament \(P_7\) is arc-reversal-saturated for each of
\[
T_4,\quad D,\quad E,\quad C_5,\quad W_5.
\]

# 6. Targets one reversal from a transitive tournament

I include the short argument because it supplies several entries in the small-order classification.

**Proposition 6.1.**  
If \(H\) is nontransitive and \(H^e\cong T_h\) for some arc \(e\), then the transitive tournament on \(\mathbb Q\) is \(H\)-free and arc-reversal-saturated.

**Proof.**

Orient \(x\to y\) when \(x<y\). The host is \(H\)-free because all its finite subtournaments are transitive.

Suppose the distinguished endpoints occupy positions \(i<j\) in \(T_h\). For any \(x<y\), select \(i-1\) points below \(x\), \(j-i-1\) between \(x,y\), and \(h-j\) above \(y\). These points together with \(x,y\) form the required rooted \(H^e\). Reversing \(xy\) creates \(H\). ∎

# 7. Complete positive result through order five

Let \(\oplus\) denote a transitive sum: all arcs go from the left summand to the right. Put
\[
D_4=\Delta(T_2,T_1,T_1).
\]

The twelve five-vertex tournaments, grouped by isomorphism type, have the following hosts:

\[
\begin{array}{l|l}
\text{target}&\text{host}\\ \hline
T_5&P_{11}\\
T_2\oplus C_3,\quad T_1\oplus C_3\oplus T_1,\quad C_3\oplus T_2
&(\mathbb Q,<)\\
T_1\oplus D_4,\quad D_4\oplus T_1&(\mathbb Q,<)\\
\Delta(T_3,T_1,T_1)&(\mathbb Q,<)\\
D=\Delta(T_2,T_2,T_1)&P_7\\
E=\Delta(C_3,T_1,T_1)&P_7\\
C_5&P_7\\
U_5&L(C_3)\\
W_5&P_7.
\end{array}
\]

The six nontransitive targets assigned to \(\mathbb Q\) arise from \(T_5\) by reversing, respectively, an arc whose endpoints are at distance two, three, or four in its linear order.

For completeness, here is an elementary verification that the table is exhaustive.

## 7.1 Non-strong tournaments

Strongly connected components of a tournament are transitively ordered. On four vertices there is a unique strongly connected tournament, namely \(D_4\). Hence a non-strong five-vertex tournament is one of
\[
T_5,
\]
the three possible placements of one \(C_3\) among two singleton components, or the two placements of a singleton beside \(D_4\). These are exactly the first six types in the table.

## 7.2 Nonprime strong tournaments

A proper module in a strong five-vertex tournament cannot have size four.

A three-vertex module gives a three-vertex strong quotient, necessarily \(C_3\), and hence gives either
\[
\Delta(T_3,T_1,T_1)
\quad\text{or}\quad
E.
\]

A two-vertex module gives the strong four-vertex quotient \(D_4\). Inflating a vertex in its two-vertex block produces \(\Delta(T_3,T_1,T_1)\); inflating either singleton produces \(D\).

Thus the only nonprime strong five-vertex tournaments are
\[
\Delta(T_3,T_1,T_1),\qquad D,\qquad E.
\]

## 7.3 The remaining strong tournaments

A strong five-vertex tournament has all outdegrees in \(\{1,2,3\}\), with total ten. Its sorted degree sequence is therefore one of
\[
(2,2,2,2,2),\qquad
(1,2,2,2,3),\qquad
(1,1,2,3,3).
\]

- The regular case is uniquely \(C_5\). For a quick forcing argument, fix a vertex \(v\), write its outneighbors as \(a\to b\), and its inneighbors as \(c\to d\). The degree requirements force
  \[
  b\to c,d,\qquad a\to c,\qquad d\to a,
  \]
  and determine the regular five-cycle.

- In the second degree sequence, let \(p\) have degree three and \(q\) degree one. If \(q\to p\), the other three vertices form a directed triangle and the tournament is \(E\). Otherwise let \(r\) be the unique inneighbor of \(p\), and \(s\) the unique outneighbor of \(q\). If \(r=s\), the degree constraints give \(D\). If \(r\neq s\), the three middle vertices are forced into the transitive order
  \[
  s\to t\to r,
  \]
  giving \(U_5\).

- In the third degree sequence, label the high-degree pair \(p\to p'\), the low-degree pair \(q\to q'\), and the middle vertex \(r\). The degree constraints force \(p'\) to dominate \(q,q',r\), and \(q\) to lose to \(p,p',r\). The unique outneighbor of \(q'\) is therefore either \(p\) or \(r\). The former gives \(\Delta(T_3,T_1,T_1)\), and the latter gives \(W_5\).

The three remaining strong types \(C_5,U_5,W_5\) are consequently prime, by the preceding classification of nonprime strong tournaments.

This establishes completeness of the table without relying on an external enumeration.

On four vertices, the targets are \(T_4\), \(T_1\oplus C_3\), \(C_3\oplus T_1\), and \(D_4\). The first has host \(P_7\); the other three are one reversal from \(T_4\) and have host \(\mathbb Q\). On three vertices, \(C_3\) has host \(\mathbb Q\), while \(T_3\) has host \(C_3\).

We have proved:

**Theorem 7.1.**  
Every tournament \(H\) with
\[
3\leq |H|\leq5
\]
admits a nonvacuous countable arc-reversal-saturated host. The transitive target \(T_6\) also admits a finite host.

# 8. A necessary structural condition for transitive targets

The transitive case has an additional restriction not present in the preceding constructions.

**Proposition 8.1.**  
If \(G\) is a nonvacuous \(T_h\)-free arc-reversal-saturated tournament, where \(h\geq3\), then:

1. \(G\) is finite, with
   \[
   |G|\leq 2^{h-1}-1;
   \]
2. \(G\) is prime.

**Proof.**

Every tournament on \(2^{h-1}\) vertices contains \(T_h\). This follows by induction: some vertex has at least \(2^{h-2}\) outneighbors or at least that many inneighbors, and one applies the induction hypothesis there. This proves (1), including exclusion of infinite hosts.

For (2), suppose \(M\) is a proper module with \(|M|\geq2\). Choose \(u\in M\), \(v\notin M\), and reverse their arc. Let \(S\) be the vertex set of a resulting \(T_h\).

The original \(G[S]\) is nontransitive, so it contains a directed triangle. Every such triangle must contain both \(u,v\), since the reversal makes \(G[S]\) transitive. Let its third vertex be \(w\). Necessarily \(w\notin M\): \(v\) has the same relation to all of \(M\), so no directed triangle can contain \(v\) and two vertices of \(M\).

If \(S\) contained another \(x\in M\setminus\{u\}\), then \(x,v,w\) would form the same directed triangle as \(u,v,w\) did before the reversal. None of its arcs was reversed, a contradiction. Hence
\[
S\cap M=\{u\}.
\]

The original tournament on \(S\setminus\{v\}\) is a \(T_{h-1}\). Choose \(x\in M\setminus\{u\}\). Relative to its other \(h-2\) vertices, \(u\) and \(x\) have identical directions. Replacing \(u\) in its transitive order by the oriented pair \(u,x\) therefore produces a \(T_h\) already in \(G\), again a contradiction. ∎

In particular, the transitive-target existence problem is a finite decidable search problem, albeit with a rapidly growing search space. The explicit constructions above settle \(h=3,4,5,6\), not arbitrary \(h\).

# 9. Remaining gaps

The central characterization is still open in this attack.

The new positive results cover two complementary prime-target classes:

- a single exceptional arc across a directed cut;
- prime targets whose every vertex-deletion is prime.

They also complete the positive answer through order five. However, they do not handle arbitrary modular structure, nor do they supply finite saturated hosts for all transitive targets.

For example, these arguments do not decide the six-vertex target
\[
C_3\oplus C_3.
\]
They also leave the existence question for \(T_h\), \(h\geq7\), unresolved here.

Thus the partial theorems and explicit certificates above are established, but a complete answer to Problem 23 is not.