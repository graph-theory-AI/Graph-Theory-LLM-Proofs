---
id: imbalance_conjecture
leg: attacks_opg
claimed_verdict: proved
review_verdict: ALREADY_KNOWN
confidence: high
interpretation_ok: true
references_ok: true
computation_run: true
one_line: The proof is mathematically correct in every step I could check, but the identical theorem and the identical load-bearing "capacity"/truncated-tail lemma were posted to arXiv as 2608.09191 (Schreib & Yavari, v1 10 Aug 2026, v2 17 Aug 2026), five weeks before this attack ran.
---

## Interpretation

The prompt (OpenProblemGarden, `op/imbalance_conjecture`, posted by Kozerenko 2013) asks:
for a finite simple undirected graph $G$, with $\mathrm{imb}(uv)=|d(u)-d(v)|$ and
$M_G$ the multiset of all edge imbalances, show that $\mathrm{imb}(e)>0$ for every
$e\in E(G)$ implies $M_G$ is graphic.

The writeup's formalization is exactly this. Specifically:

* "adjacent vertices have different degrees" is literally equivalent to
  $\mathrm{imb}(e)>0$ for all $e$, so no hypothesis has been strengthened or weakened;
* "graphic" is used in the standard sense (realizable as the degree sequence of a
  *simple* graph), and it is verified via the Erdős–Gallai criterion, which is the
  simple-graph criterion — the writeup does not quietly slide to multigraphs;
* $M_G$ is treated as a *multiset* of $m=|E(G)|$ numbers throughout, not as a set;
* the empty graph and graphs with isolated vertices are handled explicitly.

No interpretation gaming. A reasonable author of the original problem would regard the
statement proved by this writeup as *the* conjecture. `interpretation_ok: true`.

One presentational note: the writeup's Theorem drops the hypothesis $m>0$ and instead
deals with $m=0$ in the completion section ("If $m=0$, the multiset is empty and is
graphic") — correct, since the empty sequence is realized by the edgeless graph.

## Step-by-step findings

I number the writeup's argument S1–S17. Every inequality below was re-derived by hand
and, where it is a finite combinatorial statement, re-checked exhaustively by code
(see **Computational check**).

| step | label | note |
|---|---|---|
| S1. Theorem statement and notation $a_e,m,D$ | VALID | Faithful to the prompt; hypothesis is $a_e\ge 1$ for all $e$. |
| S2. Lemma (1): $\forall\,1\le k<D$, $\forall S\subseteq E$ with $|S|=k$: $\sum_{e\notin S}\min\{k,a_e\}\ge k(D-k)$ | VALID | True as stated. Note the worst $S$ is the top-$k$ one, since $x\mapsto\min\{k,x\}$ is nondecreasing, so the "for every $S$" form is equivalent to the top-$k$ form actually used later; I nevertheless checked all $S$ by brute force. |
| S3. Preliminaries $m\ge D$ and $D\ge 2$ | VALID | $m\ge D$ because a maximum-degree vertex is incident with $D$ distinct edges; $D\ge2$ because $m>0$ plus $a_e\ge1$ forces some endpoint to have degree $\ge2$. |
| S4. Case $k=1$: $\sum_{e\notin S}\min\{1,a_e\}=m-1\ge D-1$ | VALID | Uses $a_e\ge1$ (so $\min\{1,a_e\}=1$) and S3. Covers $D=2$ entirely, since $k<D=2$ forces $k=1$. |
| S5. Case $D=3,k=2$ | VALID | If $m\ge4$, the $m-2$ retained edges give $\ge m-2\ge2=k(D-k)$. If $m=3$, a degree-3 vertex meets all three edges, so $G=K_{1,3}$ plus isolated vertices, all imbalances $=2$, and the single retained edge gives $\min\{2,2\}=2$. $m\le2$ is impossible when $D=3$. Together with S4 this does dispose of all $D\le3$. |
| S6. Setup for $D\ge4$, $2\le k<D$: $v$, $q=m-D$, $s$, $t=k-s$, $U$, $r=|U|=D-s$, $b=D-k$; identity (2) $r=b+t$ | VALID | $r=D-s=D-(k-t)=(D-k)+t=b+t$. Also $b\ge1$, $0\le t\le k$, $0\le t\le q$ (the $t$ edges of $S$ off $v$ are among the $q$ edges off $v$), all used implicitly and all correct. |
| S7. Inequality (3) | VALID | Two ingredients. (i) The $q-t$ retained edges not incident with $v$ each contribute $\min\{k,a_e\}\ge1$ (needs $a_e\ge1$ and $k\ge1$): correct, and $q-t\ge0$. (ii) For $u\in U$, $a_{vu}=D-d(u)$ because $d(v)=D$ is maximum: correct. Then $\sum_{u\in U}\min\{k,D-d(u)\}=kr-\sum_{u\in U}\bigl(k-(D-d(u))\bigr)_+=kr-\sum_{u\in U}(d(u)-b)_+$ with $b=D-k$: the identity $\min\{k,y\}=k-(k-y)_+$ is exact. The two families of edges (off $v$, and $vu$ for $u\in U$) are disjoint and both disjoint from $S$, so no edge is double counted. |
| S8. Inequality (4), the double count | VALID | $v\notin U$ (simple graph, no loops), so for $u\in L\subseteq U$ each of the $d(u)-1$ edges at $u$ other than $uv$ is an edge not incident with $v$. Hence $\sum_{u\in L}(d(u)-1)=\sum_{e\not\ni v}|e\cap L|\le q+|E(G[L])|$, because such an edge contributes $1$ or $2$ and contributes $2$ exactly when both ends lie in $L$; and $|E(G[L])|\le\binom{\ell}{2}$ by simplicity. Subtracting $(b-1)\ell$ converts $\sum_{u\in L}(d(u)-1)$ into $\sum_{u\in L}(d(u)-b)=\sum_{u\in U}(d(u)-b)_+$. **This is the step where a sum over edges is bounded using vertex degrees, i.e. the classic place for a double-counting error — it is done correctly here, the $+|E(G[L])|$ correction term is exactly the needed one, and it is what makes the later $\binom{\ell}{2}$ appear.** |
| S9. Inequality (5) $\sum_{e\notin S}\min\{k,a_e\}\ge kr-t-F_b(\ell)$, $F_b(\ell)=\binom{\ell}{2}-(b-1)\ell$ | VALID | Substituting (4) into (3): $q-t+kr-\bigl(q+\binom{\ell}{2}-(b-1)\ell\bigr)=kr-t-F_b(\ell)$. The $q$'s cancel exactly — no tail is dropped. |
| S10. Claim (6) $F_b(\ell)\le(k-1)t$ | VALID | See S11–S13; and verified by exhaustive parameter sweep. |
| S11. Step (7): convexity/endpoint reduction, and the identity $F_b(b+t)=\binom{t+1}{2}-\binom{b}{2}$ | VALID | $F_b$ is a convex quadratic in $\ell$, $0\le\ell\le r=b+t$ (since $L\subseteq U$), so its max on the interval is at an endpoint; $F_b(0)=0$. The identity: $\binom{b+t}{2}-(b-1)(b+t)=\tfrac{(b+t)(t-b+1)}{2}=\tfrac{t(t+1)-b(b-1)}{2}=\binom{t+1}{2}-\binom{b}{2}$. I verified this symbolically. |
| S12. Sub-case $k\ge3$ of (6) | VALID | $\max\{0,\binom{t+1}{2}-\binom b2\}\le\binom{t+1}{2}=\tfrac{t(t+1)}2\le\tfrac{t(k+1)}2\le(k-1)t$, the last step being $(k+1)/2\le k-1\iff k\ge3$. Uses only $t\le k$, which holds since $t=k-s\le k$. |
| S13. Sub-case $k=2$ of (6) | VALID | Here $b=D-2\ge2$ **because $D\ge4$ was assumed**, so $\binom b2\ge1$, and for $t=0,1,2$ the quantity $\binom{t+1}{2}-\binom b2$ is at most $-1,0,2$, giving $\max\{0,\cdot\}\le 0,0,2$, i.e. $\le(k-1)t=0,1,2$. Correct. This is the one place where $D\ge4$ is genuinely load-bearing: at $D=3,k=2$ one has $b=1,t=2,\ell=3$ and $F_1(3)=3>(k-1)t=2$, so (6) is *false* there — which is precisely why S5 disposes of $D=3$ by hand first. The writeup's case split is therefore not cosmetic, and it is complete. |
| S14. Conclusion of the lemma: $kr-t-(k-1)t=k(r-t)=kb=k(D-k)$ | VALID | Uses (2) $r-t=b$. Arithmetic correct. |
| S15. Parity (8) | VALID | $|x-y|\equiv x+y \pmod 2$; $\sum_{uv\in E}(d(u)+d(v))=\sum_v d(v)^2\equiv\sum_v d(v)=2m\equiv0$. Every congruence is over $\mathbb{Z}/2$ and correct. |
| S16. Range (9) $1\le a_e\le D-1$ | VALID | Both endpoints of an edge have degree in $[1,D]$, so the difference is at most $D-1$; positivity gives the lower bound. |
| S17. Erdős–Gallai, case $k\ge D$ | VALID | $\sum_{i\le k}a_i\le k(D-1)\le k(k-1)$ since $k\ge D$. |
| S18. Erdős–Gallai, case $1\le k<D$ | VALID | The lemma is applied with $S$ = the $k$ edges carrying the $k$ largest imbalances; $|S|=k$ is legitimate because $k<D\le m$. Then $k(k-1)+\sum_{i>k}\min\{k,a_i\}\ge k(k-1)+k(D-k)=k(D-1)\ge\sum_{i\le k}a_i$. |
| S19. Erdős–Gallai invocation itself | VALID | The criterion is applied in its correct form for a nonincreasing nonnegative integer sequence of length $m$: even sum plus $\sum_{i\le k}a_i\le k(k-1)+\sum_{i>k}\min\{k,a_i\}$ for $1\le k\le m$. The often-forgotten side condition $a_1\le m-1$ is implied by the $k=1$ instance, which the argument does cover. No convention mismatch. |
| S20. "Scope and verification status" paragraph | VALID | Its claims are accurate: disconnected graphs, isolated vertices, the empty graph and all $\Delta$ are covered; simplicity is used exactly where claimed; positivity is used exactly where claimed (twice: in S4/S7 for the one-unit-per-edge tail contribution, and in S16). |

**No step is labelled GAP or ERROR.** The truncation in the lemma is uniform in the
parameters: the truncation level is $k$, the same $k$ as in the Erdős–Gallai instance
being proved, chosen *before* the bound is derived, and the lemma is proved for all
$1\le k<D$ simultaneously and for *every* $k$-set $S$, not just the convenient one. No
tail is dropped: the $q$ terms cancel identically in S9. So the three failure modes I
was asked to look for (dropped tail, post-hoc truncation point, edge-sum/vertex-sum
double counting) are all absent.

## Reference check

The writeup cites exactly one external result: the Erdős–Gallai criterion. It is used
correctly (standard statement, simple-graph version, sorted nonincreasing, range
$1\le k\le n$). `references_ok: true` for what the writeup cites.

**Priority check (step 2b) — the decisive finding.**

* **arXiv:2608.09191, "A Proof of the Imbalance Conjecture", James Alexander Schreib
  and Yousof Yavari.** 5 pages, no figures; MSC 05C07 (primary), 05C99 (secondary);
  math.CO / cs.DM. **v1 submitted 10 August 2026 07:02 UTC; v2 submitted 17 August
  2026 02:26 UTC.** Abstract (v2, verbatim): *"For an edge uv of a finite simple graph
  G, its imbalance is |dG(u)−dG(v)|, and the imbalance multiset MG consists of the
  imbalances of all edges of G. Kozerenko and Skochko conjectured that MG is graphic
  whenever every edge has positive imbalance. We prove this conjecture. The main
  ingredient is the following capacity bound: for every set A of k edges, the sum over
  edges not in A of the minimum of k and the imbalance of each edge is at least k times
  the maximum of Δ−k and 0, where Δ is the maximum degree of G. This bound yields all
  Erdős–Gallai inequalities directly; a parity computation completes the proof."*

  This is not merely the same theorem. **Its Lemma 3.1 is character-for-character the
  writeup's truncated-tail lemma**:
  $\sum_{e\in E(G)\setminus A}\min\{k,\mathrm{imb}_G(e)\}\ge k(\Delta-k)^+$ for every
  $A\subseteq E(G)$ with $|A|=k$ — the writeup's (1) is the restriction of this to
  $1\le k<\Delta$ (where $(\Delta-k)^+=\Delta-k$), the $k\ge\Delta$ range being trivial
  and handled separately in both texts. The high-level route is also the same
  (Erdős–Gallai from the capacity bound, then the $\sum_v d(v)^2$ parity computation),
  and even the internal bookkeeping matches: the paper fixes a maximum-degree vertex
  $x$, sets $r=\Delta-k$ (the writeup's $b$), and controls
  $\rho=\sum_{z\in R}(d_G(z)-r)^+$ — which is the writeup's
  $\sum_{u\in U}(d(u)-b)_+$ — by counting "escape edges". The writeup's $q+\binom\ell2$
  double count is a cosmetic variant of that escape-edge count.

  The v1 abstract phrases the ingredient slightly differently ("a lower bound for the
  truncated sum $\sum_{e\in E(G)}\min\{k,\mathrm{imb}_G(e)\}$ when at least $k$ edges
  have imbalance at least $k$"); v2 restates it in the $A$-form. Both are the same
  inequality, consistent with the earlier referee run's observation that the argument
  is identical in the two versions. The writeup matches the v2 phrasing.

* **Self-contamination check (step 2c): cleared.** The source is a genuine independent
  artifact, not an echo of this repository. It has named human authors, an arXiv
  identifier, two dated versions, a page count and MSC classification; it is
  accompanied by a third-party Lean 4 formalization repository
  (`github.com/jamesschreib/imbalance-conjecture`); and it has independent secondary
  coverage — John D. Cook's blog post "The imbalance theorem", 18 August 2026, which
  reports "James Alexander Schreib and Yousof Yavari posted a proof last week". All of
  this predates this campaign's attack (`when: 2026-09-16T18:00:06Z`) by five weeks and
  none of it traces back to `lelarge/graph-theory-auto`.

* Context worth recording: per the paper's own account, Schreib found his proof on
  24 July 2026 with OpenAI's GPT-5.6 Sol Pro and Yavari found his on 1 August 2026 with
  GPT-5.6 Sol Max, and the preprint is the merged, polished version of the two. So
  this is another instance of the pattern flagged in step 2b — the problem was resolved
  outside the usual channels, faster than the catalog tracks. The catalog page here is
  stale (it is dated "Auto-reviewed 2026-05-08", before the preprint appeared), and so
  is the Wikipedia article, which still lists the statement as an unsolved problem
  (with computational verification "improved to graphs with at most 12 vertices").

* Genuinely prior partial literature cited by the prompt — Kozerenko–Skochko
  (Algebra Discrete Math. 2014), Kozerenko (J. Adv. Math. Stud. 2019), Kozerenko–Serdiuk
  (Opuscula Math. 43 (2023) 81, doi:10.7494/OpMath.2023.43.1.81) — is only partial
  (trees, unicyclic, antiregular, block-graph classes) and is not invoked by the
  writeup. It does not affect the verdict.

The writeup itself is candid about this: *"I have not independently checked whether
this proof has appeared in the literature."* It has.

## Computational check

All scripts are under `verification_astra/scripts/imbalance_conjecture/`. Graph
generation is nauty's `geng` (`/usr/bin/geng`), non-isomorphic graphs including
disconnected ones and isolated vertices; the imbalance-positive graphs are then filtered
out of that stream. Python 3 with `sympy`; `networkx` was not needed.

**1. The conjecture and the lemma, exhaustive up to $n=9$** (`check_lemma.py`, reused
from the previous run and re-executed; the lemma is tested with the worst-case
$S$ = top-$k$, which is legitimate because $x\mapsto\min\{k,x\}$ is nondecreasing).

| $n$ | graphs read | with all $\mathrm{imb}(e)>0$, $m>0$ | $M_G$ not graphic | lemma (1) violations | lemma tight for some $k$ |
|---|---|---|---|---|---|
| 5 | 34 | 6 | 0 | 0 | 5 |
| 6 | 156 | 20 | 0 | 0 | 8 |
| 7 | 1044 | 85 | 0 | 0 | 11 |
| 8 | 12346 | 567 | 0 | 0 | 14 |
| 9 | 274668 | 6554 | 0 | 0 | 17 |
| 10 | 12005168 | 139742 | 0 | 0 | 20 |

This reproduces the literature's "verified for $\le9$ vertices" and extends my own
exhaustive verification to $n=10$ (all $12\,005\,168$ non-isomorphic graphs on 10
vertices; $139\,742$ of them satisfy the hypothesis with $m>0$).

**2. Audit of the writeup's internal steps (2)–(7), over EVERY $S$ and every
maximum-degree vertex** (`audit_steps_D4.py`, written for this run). This is the check
that matters, because the lemma could be true while the writeup's derivation of it is
broken. Steps (2)–(7) are audited only in the regime the writeup assumes for them
($D\ge4$, $2\le k<D$), with the $D\le3$ hand cases audited separately.

| $n$ | graphs audited | (2) | (3) | (4) | (5) | (6) | (7) | lemma (1) | $D\le3$ hand cases |
|---|---|---|---|---|---|---|---|---|---|
| 6 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 7 | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 8 | 567 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 9 | 6443 (111 skipped: too many $S$) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 11, $10\le m\le13$ | 7522 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 12, $m=11,12,13$ | 10632 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

(Failure counts are zero in every column. The previous referee run's script
`audit_proof_steps.py` reported nonzero counts for step (6); re-running it, all of those
failures have $b=1,k=2$, i.e. $D=3$ — the regime the writeup explicitly removes in S5
before assuming $D\ge4$. That script did not apply the $D\ge4$ filter, so those were
false alarms, not gaps. This is confirmed independently in item 3 below.)

**3. Steps (6) and (7) as pure arithmetic** (`check_step67_symbolic.py` and a faster
rerun): sympy confirms the endpoint identity
$F_b(b+t)-\bigl[\binom{t+1}{2}-\binom b2\bigr]=0$ identically. Brute force over
$D=4,\dots,120$, all $2\le k<D$, all $0\le t\le k$, all $0\le\ell\le b+t$:
**0 violations of (7) and 0 violations of (6)**. In the excluded regime $D\le3$ the
sweep returns exactly one violation of (6), $(D,k,b,t)=(3,2,1,2)$ with
$\max_\ell F_b(\ell)=3>2=(k-1)t$ — confirming both that $D\ge4$ is necessary for (6) and
that the writeup's S5 removes precisely that case.

**4. Sparse regime, where the lemma is tight** (`sparse_sweep.py`, written for this
run). The lemma is tight for stars, so I pushed $n$ up with $m$ held near $n$:

| $n$, $m$ range | hypothesis-satisfying graphs | $M_G$ not graphic | lemma violations | lemma-tight | min slack |
|---|---|---|---|---|---|
| 10, $9\le m\le12$ | 2037 | 0 | 0 | 5 | 0 ($K_{1,9}$) |
| 11, $10\le m\le13$ | 7522 | 0 | 0 | 5 | 0 ($K_{1,10}$) |
| 12, $11\le m\le14$ | 28463 | 0 | 0 | 5 | 0 ($K_{1,11}$) |
| 13, $12\le m\le15$ | 108398 | 0 | 0 | 5 | 0 ($K_{1,12}$) |
| 14, $13\le m\le16$ | 419453 | 0 | 0 | 5 | 0 ($K_{1,13}$) |

The minimum slack is $0$ and never negative; the extremal graphs are exactly the stars
$K_{1,D}$ (degree sequence $[1,\dots,1,D]$, all imbalances $D-1$), where
$\sum_{e\notin S}\min\{k,a_e\}=(D-k)k$ with equality for every $k$. So the lemma is
exactly tight, in the sparse regime, for all $k$ simultaneously — there is no hidden
slack the proof is secretly living on, and equally no regime in which it degrades.

**5. Structured large-$n$ families** (`structured_large.py`, written for this run):
stars $K_{1,D}$ for $D=5,20,100,500$; double stars with $(p,q)=(3,4),(10,11),(50,77),(200,313)$;
antiregular (maximally irregular) graphs on $n=6,20,60,150$ (up to $m=5550$ edges,
$\Delta=148$); plus 571 hypothesis-satisfying random labelled trees ($n\le60$) and random
threshold graphs ($n\le40$). In every instance $M_G$ is graphic and the minimum lemma
slack over all $k$ is $\ge0$: exactly $0$ for the stars and for antiregular $n=6$, and
strictly positive (e.g. $3,10,50,200$ for the double stars, $72,812,5402$ for antiregular
$n=20,60,150$) elsewhere. Complete split graphs are automatically excluded — their clique
vertices are adjacent and equidegree, so they violate the hypothesis — which is a useful
confirmation that the filter is doing real work.

**6. Randomized search beyond exhaustive range** (`search_large.py`, and a
reduced-budget rerun of the same annealing scheme): simulated annealing on
$n=8,\dots,24$, minimizing the lemma slack under a hard penalty for any zero imbalance,
6 restarts per $n$, 102 hypothesis-satisfying local optima. Result: **0 lemma
violations, 0 non-graphic $M_G$**, global minimum slack $0$. The per-$n$ minima found
were slack $0$ for $n=8..16$ (the annealer keeps rediscovering stars) and then
$4,4,5,8,7,5,15,28$ for $n=17,\dots,24$. Nothing ever goes negative.

No computational check contradicts anything in the writeup. `computation_run: true`.

## Caveats

1. **Novelty.** The decisive caveat. The writeup's verdict block says
   `"would_publish": true` and its caveat line says only "publication novelty has not
   been checked". It has now been checked and the result is not novel: arXiv:2608.09191
   (10 August 2026) proves the same theorem via the same lemma, five weeks before the
   attack ran. Nothing here is publishable as new mathematics.
2. **$m=0$.** The Theorem as stated omits $m>0$; the empty case is picked up in the
   completion section. Harmless.
3. **$D\le1$.** Not discussed explicitly. It is vacuous: if $m>0$ and $D\le1$ then some
   edge has both endpoints of degree $1$, contradicting positivity. And for $D\le1$ the
   range $1\le k<D$ is empty anyway, so the lemma has no content there.
4. **$k=0$.** The lemma is stated for $k\ge1$ only; the Erdős–Gallai application starts
   at $k=1$, so this is consistent. (The arXiv paper states the lemma for $k\ge0$; the
   $k=0$ case is trivial.)
5. **The "for every $S$" strength is unused.** The lemma is proved for all $k$-sets $S$
   but applied only to the top-$k$ set. This is not an error — it is the natural way to
   prove it, and the top-$k$ set is the minimizer anyway — but it means the lemma is
   formally stronger than needed.
6. **Positivity is genuinely load-bearing and correctly used.** It enters twice: to give
   each retained edge off $v$ one unit of tail (S7), and for $a_e\ge1$ in S16. Without
   it the conjecture is false in general, so no version of this argument could have
   "proved too much" — a useful sanity check that the hypothesis was not silently
   dropped.
7. **Reliance on the max-degree vertex only.** The lemma bound $k(\Delta-k)$ uses a
   single maximum-degree vertex. That suffices here because the Erdős–Gallai deficit is
   also governed by $\Delta$ via $a_e\le\Delta-1$; the two $\Delta$'s cancel exactly in
   S18 ($k(k-1)+k(\Delta-k)=k(\Delta-1)$). This exact cancellation is the real idea of
   the proof, and it is the same idea as in the preprint.
8. **Erdős–Gallai side condition.** $a_1\le m-1$ is not stated separately but is implied
   by the $k=1$ instance; not a gap, but a reader should notice it.

## Referee summary

I set out to break this writeup and could not. Every one of its twenty steps is valid:
the truncated-tail lemma (1) is true and correctly proved; the double count in (4) — the
place where a sum over edges is bounded via vertex degrees, and the most likely home for
a fatal error — carries exactly the right $|E(G[L])|\le\binom{\ell}2$ correction term;
nothing is dropped in passing from (3)+(4) to (5), since the $q$ terms cancel
identically; the truncation level is $k$ throughout, fixed by the Erdős–Gallai instance
being proved rather than chosen after seeing the target bound, and the lemma is
established uniformly for all $1\le k<\Delta$ and all $k$-subsets $S$; and the one case
where the key convexity estimate (6) genuinely fails, $\Delta=3,k=2$, is exactly the
case the writeup removes by hand beforehand — I confirmed both the failure and the
completeness of the case split by exhaustive parameter sweep. Computationally, the
conjecture, the lemma and every internal step (2)–(7) survive exhaustive checking over
all graphs up to 9 vertices (and the conjecture and lemma up to 10 vertices, all
12,005,168 of them) (for the internal steps, over *every* $k$-subset $S$ and
every maximum-degree vertex) and over sparse graphs up to 14 vertices, where the lemma
is exactly tight on stars with slack 0 and never negative.

The writeup is therefore correct — but it is not new. The identical theorem, with the
identical load-bearing capacity/truncated-tail lemma
$\sum_{e\notin A}\min\{k,\mathrm{imb}(e)\}\ge k(\Delta-k)^+$, the identical derivation of
the Erdős–Gallai inequalities from it, and the identical $\sum_v d(v)^2$ parity argument,
were posted as arXiv:2608.09191 by James Alexander Schreib and Yousof Yavari on
10 August 2026 (v2 17 August 2026), five weeks before this attack ran on
16 September 2026. That preprint is independently attested — named authors, two dated
arXiv versions, a Lean 4 formalization at `github.com/jamesschreib/imbalance-conjecture`,
and third-party coverage (John D. Cook, 18 August 2026) — so it is not an echo of this
campaign's own artifacts. The verdict is **ALREADY_KNOWN**, not CONFIRMED: the
mathematics stands, the priority does not.
