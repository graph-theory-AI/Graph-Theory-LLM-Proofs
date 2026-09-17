---
id: a_generalization_of_vizings_theorem
leg: attacks_opg
claimed_verdict: disproved
review_verdict: MINOR_GAPS
confidence: medium
interpretation_ok: true
references_ok: true
computation_run: true
one_line: I could not break the argument — every step, including the entropy matching-counting lemma, checks out under brute-force and independent re-derivation — but the single load-bearing error term (the o(N) in the counting lemma) is never quantified and in fact decays only like a 99th root, so the counterexample exists only for n around 10^455; that quantification is missing from the writeup.
---

## Interpretation

The conjecture (OPG, Rosenfeld 2007, verified against the live page
<http://www.openproblemgarden.org/op/a_generalization_of_vizings_theorem>): for a *simple*
$d$-uniform hypergraph $H$ in which every $(d-1)$-set lies in at most $r$ edges, there is an
$(r+d-1)$-colouring of $E(H)$ in which two edges sharing $d-1$ vertices get different colours.
The writeup calls this a *facet colouring* and attacks it at $d=100$, $r=200$ (bound $299$).

The formalisation is the intended one:

* "simple" for a $d$-uniform hypergraph means no repeated edges. The constructed $H$ is a
  sub-family of the transversal $100$-sets of a $100$-partite vertex set, so its edges are
  distinct $100$-sets: simple, $100$-uniform. It is not "simple" in the (occasional) Berge sense
  of *linear*, but that reading is untenable here — under it no two edges could share $d-1\ge 2$
  vertices and the conjecture would be vacuous for $d\ge3$.
* $d=2$ recovers Vizing, as the OPG discussion demands: "$d-1=1$ set in at most $r$ edges" is
  $\Delta\le r$, "share $d-1=1$ vertex" is adjacency, bound $r+1$. Correct.
* The $99$-sets that are *not* transversals of $99$ distinct classes lie in no edge at all, so
  the codegree hypothesis really does hold for **every** $99$-set, not just the transversal ones.
  The writeup states this explicitly.

I also checked that the conjecture is *sharp*, not a strawman, by computing the exact facet
chromatic number of complete $d$-uniform hypergraphs: for $H=\binom{[d+k]}{d}$ one has $r=k+1$
and the conjectured bound $r+d-1=d+k$ is attained with equality in many cases
($(d,n)=(2,3),(2,5),(3,4),(3,5),(3,6),(4,5),(5,6),(5,7),(6,7),(7,8)$). So a counterexample cannot be a
small dense object; it must be a large spread-out one, which is what the writeup produces.

A useful equivalent form, which I used throughout as a cross-check: let $F$ be the *facet
hypergraph* (vertices = the $(d-1)$-sets, one edge $\{$the $d$ facets of $e\}$ per $e\in E(H)$).
Then $F$ is $d$-uniform, **linear** (two $d$-sets sharing two $(d-1)$-subsets are equal), has
$\Delta(F)\le r$, and a facet colouring of $H$ is exactly a proper *edge* colouring of $F$. So
Rosenfeld's conjecture says $\chi'(F)\le\Delta(F)+d-1$ for every *realisable* $F$. (For general
linear hypergraphs that is wildly false — a projective plane of order $q$ has $k=\Delta=q+1$ and
$\chi'=q^2+q+1$ — but a projective plane is not realisable as a facet hypergraph, since $d$-sets
pairwise meeting in $d-1$ points form either a star or a subfamily of a $(d+1)$-set. All of the
conjecture's content is in this realisability constraint, and the writeup respects it by building
an actual $H$.)

A reasonable author of the original problem would accept this as a disproof for $d=100$ (and,
via §4, for all large $d$), while noting that small uniformities, in particular $d=3$, remain
open. The writeup says exactly that.

## Step-by-step findings

| # | Step | Label | Note |
|---|------|-------|------|
| 1 | Lemma (1): $\log a_m(F)\le m(\log(D/x)-(s-1))-N(1-x)\log(1-x)+o(N)$ | VALID | Normalisation independently confirmed: I computed the first moment of the number of $m$-matchings in a random $D$-regular $s$-uniform hypergraph from exact log-factorials and it equals the RHS to 5–7 decimals for $s\in\{2,3,5,100\}$, $D\in\{50,1000\}$, $x\in\{0.2,0.5,0.9\}$ (ratios $0.99983$–$0.99999$). For $s=2$, $x=1$ it is Brégman/Kahn–Lovász. |
| 2 | §1.1 setup: $Z$, $\Delta$, "bad relative to $M$", hypothesis (2) | VALID | Note the definition makes every $e\in M$ bad ($|e\cap e|=s\ge2$). This is not a slip — it is exactly what forces $\varepsilon\ge w(M(v))/\Delta$, and §1.2 accounts for it ("total weight of bad original edges is at most 1"). Without it (3) would be false (a single edge gives $Z=1$ vs bound $e^{-(s-1)}$). |
| 3 | Eq (5): $H(M)+\mathbb E\sum_{e\in M}\log w(e)=\log Z$ | VALID | Immediate from $\log\Pr(M)=\sum\log w(e)-\log Z$. |
| 4 | Eq (6): label process + chain rule | VALID but terse | Verified in full: labels are independent of $M$, so $H(M)=H(M\mid\text{labels})\le\sum_v H(Z_v\mid Z_{>v},\text{labels})$ with $Z_v=M(v)$ iff $v$ is first in $M(v)$; "$v$ uncovered" $\Leftrightarrow$ "$v$ first in $M(v)$"; each edge weight is charged once; combining with $H(P)+\sum P_i\log w_i\le\log\sum w_i$ conditionally gives (6). The writeup compresses this into two sentences. |
| 5 | $\Pr(v\text{ first}\mid t)=t^{s-1}$; a non-bad $e\ni v$ survives w.p. $t^{s(s-1)}$; $\mathbb E[S_v\mid\cdot]\le\Delta t^{s(s-1)}+\varepsilon\Delta$ | VALID | The $s-1$ other vertices of a non-bad $e$ lie in $s-1$ *distinct* matching edges, none equal to $M(v)$ (else $e$ would be bad), so the $s(s-1)$ labels are distinct and independent of the conditioning event, which involves only $M(v)$. |
| 6 | Jensen + substitution $u=t^s$ $\Rightarrow$ (3) | VALID | $t^{s(s-1)}=u^{s-1}$, $t^{s-1}dt=du/s$. **Brute-force verified**: 95 explicit weighted hypergraphs ($s=2,3,4,5$, $L\le12$, exact $Z$, exact optimal $\varepsilon$ over all perfect matchings) — no violation; see Computational check. |
| 7 | Eq (4): $\varepsilon\to0\Rightarrow\log Z\le\frac Ls(\log\Delta-(s-1)+o(1))$ | **GAP** | True, but the *rate* is never given and it is the linchpin. $\int_0^1\log(u^{s-1}+\varepsilon)du+(s-1)\approx(s-1)\varepsilon^{1/(s-1)}$ (confirmed numerically). For $s=100$ this is a 99th root: $\varepsilon=10^{-8}$ still gives an error of $82$ per vertex. See Caveats. |
| 8 | §1.2 auxiliary $K$: weights $w$, weighted $(D/x)$-regularity | VALID | Re-derived ($\binom{b-1}{s-2}/\binom{b}{s-1}=(s-1)/b$, $b=(s-1)N(1-x)$) **and verified exactly by code** on $C_4,C_6,K_4,K_{3,3}$ and AG(2,3): old and new weighted degrees both exactly $D/x$. |
| 9 | (2) holds for $K$ with $\varepsilon=\Delta^{-1}+O(N^{-1})$ | VALID | Bad *original* edges through $v$: only $M(v)$ itself (linearity; an auxiliary edge has one old vertex). Bad *auxiliary* edges: $\binom s2$ pairs, each colliding with prob $O(1/\min\{N,b-s\})=O(1/N)$; total $\le\Delta\cdot O(1/N)$. $\Delta/N=n/(x\cdot100n^{99})\to0$. |
| 10 | PM($K$) $\leftrightarrow$ $m$-matchings of $F$; identity (7) | VALID | **Verified exactly by code**: #PM$(K)=a_m(F)\cdot b!/((s-1)!)^u$ and $Z$ equals (7) on all five test instances; every PM uses exactly $u$ auxiliary edges, as claimed. |
| 11 | Stirling step (9) | VALID | Re-derived: the $-u\log((s-1)!)$ from the partition count and the $+u\log((s-1)!)$ inside $\log\binom{b}{s-1}$ cancel, and $b\log b-(s-1)u\log b=0$ since $b=(s-1)u$; what is left is $u(\log\frac{(1-x)D}{x}-(s-1))+O(\log N)$. Exactly as printed. |
| 12 | (8) $-$ (9) $\Rightarrow$ (1) | VALID | $u[\log(D/x)-\log((1-x)D/x)]=u\log\frac1{1-x}=-N(1-x)\log(1-x)$. |
| 13 | §2: $F$ is $100$-uniform, $n$-regular, linear; $N=100T$, $T=n^{99}$ | VALID | $100\cdot n^{99}$ facets; a facet lies in exactly $n$ transversal edges; two transversal $100$-sets sharing two $99$-subsets coincide. |
| 14 | Colour classes $\leftrightarrow$ matchings of $F$ | VALID | Two edges share $99$ vertices iff they share a facet. |
| 15 | (10): substitute $p=c/D$, $c=pD=100$ | VALID | $\frac Ns[x\log(c/x)+x(1-s)-s(1-x)\log(1-x)]$ agrees with the writeup's $\frac Ns[x\log(c/x)+x-sf(x)]$. |
| 16 | $f(x)\ge x^2/2$ | VALID | $f'(x)=-\log(1-x)$, $f(0)=f'(0)=0$, $f''=1/(1-x)\ge1$. |
| 17 | Exponent $\le(\log500+1)/5-2<-2/5$; (12); (13) | VALID | Exact value $-0.705594$; the writeup's own weakened bound is $-0.557078<-0.4$. First-moment Markov gives $\Pr(A^c)\le\mathbb E[\#]$. |
| 18 | §2.2 pruning; $\Pr(X\ge200)\le2^{-200}(1+100/n)^{n-1}\le(e/4)^{100}$ | VALID | $\mathbb E2^X=(1+p)^{n-1}$; $q=(e/4)^{100}=1.67\times10^{-17}$, well under the claimed $10^{-10}$. Conditional distribution $\mathrm{Bin}(n-1,100/n)$ and the threshold ($\deg>200\Leftrightarrow X\ge200$) are both right. |
| 19 | $\mathbb EZ\ge100T(1-100q)>99T$ | VALID | $100q=1.67\times10^{-15}$. |
| 20 | $Z\le200T$ deterministically | VALID | $100Z=\sum_f\deg_H(f)\le200\cdot100T$. |
| 21 | $\mathbb E[Z\mathbf1_A]>99T-200Te^{-T/5}>90T$; good outcome exists | VALID | If $Z\le90T$ on all of $A$ then $\mathbb E[Z\mathbf1_A]\le90T$. |
| 22 | §3: $450(m-1)<90T<|E(H)|\Rightarrow\chi\ge451>299$ | VALID | $450(T/5-1)=90T-450$. |
| 23 | $H$ simple, $100$-uniform, max $99$-codegree $\le200$ | VALID | Sub-family of distinct transversal $100$-sets; pruned facets have degree $0$; non-transversal $99$-sets have degree $0$. |
| 24 | §4: $x=a/d$, $a=\lceil5\log d\rceil$, exponent $x(2\log d-\log a+1-a/2)<0$; $\chi\ge(1-o(1))d^2/(5\log d)$ vs $3d-1$ | VALID (order of limits sloppy) | I recomputed the exponent bound for $d=20,50,100,1000$: $-2.4124,-1.6687,-1.1923,-0.2184$, all $<0$ as claimed. The separation $d^2/(5\log d)>3d-1$ only kicks in around $d\approx60$–$100$ ($d=50$: $127.8<149$; $d=100$: $434.3>299$), consistent with the writeup's "for sufficiently large $d$"; the ratio does diverge. Only the reading "for each fixed $d$, let $n\to\infty$" is justified; the writeup mixes $o_d(1)$ and $o_n(1)$ without saying so. |
| 25 | "'sufficiently large $n$' is justified by the proved asymptotic counting lemma" | **GAP** | Formally true, but the writeup gives the reader no way to see that a valid $n$ exists. Quantifying step 7 (which I did) shows the required $n$ is about $10^{455}$. |

No step is ERROR. I attacked the two places the task flagged — simplicity and parameter
consistency — and both are clean: $H$ is a set of distinct $100$-sets, hence simple; and every
parameter ($d=100$, $r=200$, $c=pD=100$, $s=100$, $x=1/5$, $m=T/5=xN/s$, $N=100T$, $T=n^{99}$,
$n\equiv0\bmod5$ so $m\in\mathbb Z$, $b=(s-1)u$) is mutually consistent.

## Reference check

The writeup invokes **no** external result ("No unproved conjecture or literature assertion is
used"), so there is nothing to misquote; the counting lemma is proved from scratch. I checked:

* **OPG entry** (fetched live, <http://www.openproblemgarden.org/op/a_generalization_of_vizings_theorem>):
  statement, the $d=2$/Vizing remark and the Kempe-chain comment match `prompt.md` verbatim. The
  only post-2007 content is a 2009 comment asking for a reference for Rosenfeld's conjecture; no
  resolution, no counterexample, no bibliography. Status: open.
* **Priority.** Repeated searches (Rosenfeld + Vizing + hypergraph + codegree; chromatic index of
  linear $k$-uniform hypergraphs; $\Delta/\log\Delta$-type lower bounds) turned up no counterexample
  to this conjecture and no paper attacking it. The active neighbouring literature is different:
  Berge–Füredi (arXiv:2403.06850, arXiv:2510.07494), Erdős–Faber–Lovász and Kang–Kelly–Kühn–
  Methuku–Osthus (arXiv:2110.06181, which concerns *intersecting* edges, not $(d-1)$-sharing ones),
  and Alon–Kim on $t$-simple hypergraphs. So **not** ALREADY_KNOWN as far as I can tell.
* **Consistency with known theorems.** Pippenger–Spencer/Kahn give $\chi'(F)=(1+o(1))\Delta$ for
  linear $k$-uniform $F$ with $\Delta\to\infty$ and $k$ *fixed*. The writeup's regime has
  $\Delta=2d$ with $d\to\infty$, i.e. $k\asymp\Delta$, which those theorems do not cover (and
  projective planes show they cannot be extended there). No contradiction.

## Computational check

Scripts in `verification_astra/scripts/a_generalization_of_vizings_theorem/`.

1. `check_entropy_bound.py` — brute-force test of inequality **(3)**, which the writeup asserts
   *exactly* (no error term). For each instance: all perfect matchings enumerated, $Z$ computed
   exactly, $\Delta$ exact, and the *smallest valid* $\varepsilon$ computed as
   $\max_{M,v}\frac1\Delta\sum_{e\ni v,\ e\ \mathrm{bad}\ \mathrm{rel.}\ M}w(e)$; RHS by Simpson.
   95 instances: $K_{D,D}$ ($D\le6$), $K_{2k}$, complete $3$- and $4$-uniform hypergraphs, AG(2,3),
   and 83 random weighted instances ($s=2,3,4,5$, $L\le12$, weights spanning $e^{-6}$–$e^{2}$).
   **No violation.** Typical near-tight cases: $K_{6,6}$ $\log Z=6.5793$ vs bound $7.6214$;
   AG(2,3) $\log Z=1.3863$ vs bound $2.1498$.
2. `check_construction_12.py` — §1.2 bookkeeping. On $C_4$, $C_6$, $K_4$, $K_{3,3}$ (s=2) and
   AG(2,3) (s=3, $m=2$): weighted degrees of old and new vertices are **exactly** $D/x$ in all
   five cases; every perfect matching of $K$ uses exactly $u$ auxiliary edges; and identity **(7)**
   holds exactly, e.g. AG(2,3): $\#\mathrm{PM}(K)=1080=a_2(F)\cdot 6!/(2!)^3=12\cdot90$ and
   $Z=2.56$ = predicted $2.56$. (One line prints "FAIL" for $C_4$: that is my auxiliary-edge
   *detector*, which distinguishes aux edges by weight, and for $C_4$ the aux weight happens to be
   $1$; the counts on that line match.)
3. `check_arithmetic.py` — every number in §§2–4, plus two independent tests of the lemma:
   * exponent at $x=1/5$, $s=c=100$: $x\log(c/x)=1.242922$, $f(x)=0.02148516\ge x^2/2=0.02$,
     $sf(x)=2.148516$, **exponent $=-0.705594$** (writeup's weakened value $-0.557078$, claim $<-0.4$ ✓);
   * first-moment threshold $x^\*=0.143523$ — so the writeup's own method actually yields
     $\chi\gtrsim690$ (using $|E(H)|>99T$), and its claimed $451$ is conservative by ~$1.5\times$;
   * random-greedy matching heuristic covers $0.0887$ of the vertices, comfortably below $x^\*$
     (a necessary consistency check: had greedy exceeded $x^\*$ the lemma would be wrong);
   * $q=(e/4)^{100}=1.6728\times10^{-17}$, $100q=1.67\times10^{-15}$, $\mathbb EZ\ge99.9999\ldots T$;
   * **independent confirmation of the constant $-(s-1)$**: the first moment of $m$-matchings in a
     random $D$-regular $s$-uniform hypergraph, computed from exact log-factorials, equals the
     lemma's RHS to within $10^{-4}$ relative for $s\in\{2,3,5,100\}$;
   * finite-$N$ test of (1) on $K_N$ ($s=2$, $D=N-1$, exact $a_m$): for $x=0.2,0.6$ the bound holds
     with slack $\to0$ per vertex; **for $x=1$ the bound is violated** by $\approx0.847$ at *every* $N$ tested
     ($N=100,10^3,10^4,10^6,10^8$), i.e. by an additive $O(1)$, which is $o(N)$ — so (1) is *false without* its $o(N)$ term and
     is asymptotically exactly tight. This is not an error in the writeup (which keeps the $o(N)$),
     but it shows the error term is load-bearing.
4. `check_small_cases.py` / `check_small_random.py` — the conjecture itself on small hypergraphs.
   Complete $d$-uniform hypergraphs: the bound $r+d-1$ is attained with equality at
   $(d,n)=(2,3),(2,5),(3,4),(3,5),(3,6),(4,5),(5,6),(5,7),(6,7),(7,8)$ (exact $\chi$ by branch
   and bound), and is never exceeded.
   2357 random instances with $d\in\{3,4,5\}$, $n\le d+4$: **0 violations**, minimum slack $0$.
   So there is no small counterexample; the conjecture is sharp and non-trivial.

What I could **not** check computationally: the counterexample itself. It is non-constructive and,
by my own quantification of the error term, needs $n\approx10^{455}$ — about $10^{457}$ vertices
and $10^{45000}$ edges. Nothing of that kind can be instantiated. I therefore verified every
*ingredient* by brute force instead, which is the most that is possible here.

## Caveats

1. **The unquantified $o(N)$ is the whole ball game.** Step (4)'s $o(1)$ is
   $\int_0^1\log(u^{s-1}+\varepsilon)du+(s-1)\approx(s-1)\varepsilon^{1/(s-1)}$, with
   $\varepsilon\approx x/D=x/n$, and it is multiplied by $L/s=(m+u)=0.802N=80.2T$. The writeup's
   margin is only $0.2T$ (it proves $\log\mathbb E\le-0.4T+o(N)$ and needs $\le-0.2T$). So one needs
   $99\,(0.2/n)^{1/99}\cdot 80.2\cdot 100<0.2$, i.e. $n>10^{454.6}$ (or $10^{436.4}$ using the true
   exponent $-0.7056$ instead of the writeup's $-0.4$). This *is* finite, so the theorem stands,
   but the writeup never checks that its $o(N)$ can be beaten by a constant margin — and with a
   99th-root decay this is exactly the kind of thing that fails. A referee would require this
   paragraph. I supplied it; the conclusion survives.
2. **Uniformity claim.** "The error is uniform over $F$, with $s,x$ fixed" is asserted, never
   proved. It happens to be true (the error depends only on $D,N,s,x$ through
   $\varepsilon=x/D+O(1/N)$ and Stirling's $O(\log N)$), and the application does not even need
   uniformity, since $F$ is fixed for each $n$.
3. **Order of limits in §4.** $o_d(1)$ and $o_n(1)$ are used interchangeably. Only "for each fixed
   $d$, let $n\to\infty$, then $d\to\infty$" is justified by what is proved.
4. **Compressed entropy step (6).** "applied conditionally at each reveal, followed by the entropy
   chain rule" hides the argument that "$v$ uncovered" $=$ "$v$ first in $M(v)$" and that each edge
   is charged exactly once. Standard (Kahn–Lovász), and correct, but written as one sentence.
5. **Definition of "bad" silently includes $e\in M$.** Correct and necessary, but a careless reader
   who excludes $e=f$ obtains a false (3); the writeup never flags it.
6. **Edge cases** are fine: $x\in(0,1)$ and $s\ge2$ as required; $m=T/5\in\mathbb Z$ because $5\mid n$;
   $b=(s-1)u\gg s$; $Z=0$ handled. The conclusion says nothing about $d=2,3$ (where it is Vizing /
   open), about small $r$, or about explicit constructions — all stated honestly in the writeup's
   own "Scope and limitations" and `caveats` field.
7. **Gap between the claim and what is proved:** none in the restrictive direction — the verdict
   line ("simple $100$-uniform, max $99$-codegree $\le200$, $\ge451$ colours vs $299$") is exactly
   what §3 delivers. If anything the writeup undersells: its own first moment gives $x^\*=0.1435$
   and hence $\gtrsim690$ colours; and the random-greedy heuristic (covered fraction $0.0887$) suggests the truth is nearer $1100$.

## Referee summary

I set out to break this and could not. The suspicious-looking parts are all sound: the
hypergraph really is simple (a family of distinct transversal $100$-sets), the parameters are
mutually consistent, the $99$-codegree bound holds for *all* $99$-sets and not just the
transversal ones, and the entropy matching-counting lemma — which is where a single-pass proof
would normally invent a false Brégman-type bound — is genuinely correct: I verified its exact
form (3) by brute force on 95 weighted hypergraphs, verified the auxiliary-hypergraph bookkeeping
of §1.2 exactly on five explicit instances, and independently re-derived its constant $-(s-1)$
as the first moment for random $D$-regular $s$-uniform hypergraphs, matching to five digits. All
arithmetic in §§2–4 re-derived and confirmed (the exponent is $-0.7056$, better than the claimed
$-0.4$; $q=1.67\times10^{-17}$; $450(m-1)<90T$). The one real deficiency is that the proof's
single load-bearing approximation, the $o(N)$ in the counting lemma, is never quantified: its
true rate is $(s-1)\varepsilon^{1/(s-1)}$, a 99th root for $s=100$, so the counterexample exists
only for $n\gtrsim10^{455}$, and the writeup gives the reader no way to see that any valid $n$
exists at all. I did that computation and the conclusion survives, so this is MINOR_GAPS rather
than MAJOR_GAP, but a journal would demand it before accepting. Confidence is medium rather than
high because the result is a non-constructive claim about an object of size $10^{45000}$ that
cannot be instantiated or spot-checked, and because a correct disproof of a 2007 OPG conjecture
by a single unrefereed pass is a strong prior against; I found no counterexample to the
counterexample, and no prior art (the OPG page is still open with only a 2009 comment asking for
a reference), but a second expert reading of §1.1 is warranted before anyone claims priority.
