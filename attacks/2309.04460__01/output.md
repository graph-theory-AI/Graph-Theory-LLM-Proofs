```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A general random-activation lemma gives the desired decomposition whenever every cut is crossed by more than 2 log_2(2n) colours, which proves the question for any constant-fraction resilience definition of robust sublinear expansion.",
  "would_publish": false,
  "caveats": "The prompt omits the quantitative definition of robust sublinear expander; weaker logarithmic-resilience definitions admit the obstructions described below."
}
```

# 1. Statement of the partial result

For an edge-coloured graph \(G\), define its **colour cut-connectivity**
\[
\kappa_{\mathrm{col}}(G)
 =\min_{\varnothing\neq X\subsetneq V(G)}
 \bigl|\{\operatorname{col}(e):e\in \delta_G(X)\}\bigr|.
\]

The key result is the following.

## Theorem 1
Let \(G\) be an \(n\)-vertex edge-coloured graph; the colouring need not be proper. If
\[
\kappa_{\mathrm{col}}(G)>2\log_2(2(n-1)),
\]
then the colours of \(G\) can be partitioned into two classes so that the union of the edges of each class is a spanning connected subgraph.

More quantitatively, if every cut of \(G\) is crossed by at least \(k\) colours and every colour is independently assigned red or blue with probability \(1/2\), then
\[
\Pr(G_{\mathrm{red}}\text{ or }G_{\mathrm{blue}}\text{ is disconnected})
 \le 2(n-1)2^{-k/2}.
\]

Thus the desired decomposition exists whenever the right-hand side is less than \(1\).

# 2. Random-activation lemma

We prove a slightly more general one-sided assertion.

## Lemma 2
Suppose every nontrivial cut of an edge-coloured \(n\)-vertex graph \(G\) is crossed by at least \(k\) colours. Retain every colour independently with probability \(p\), and let \(G_p\) be the graph consisting of all edges of the retained colours. Then
\[
\Pr(G_p\text{ is disconnected})\le (n-1)(1-p)^{k/2}.
\]

### Proof

Fix a positive integer \(L\), and put
\[
q=1-(1-p)^{1/L}.
\]
Expose the retained colours in \(L\) rounds. In each round, every colour not activated earlier is independently activated with probability \(q\). A colour is present in the final graph if it is activated in at least one round. Therefore its final retention probability is
\[
1-(1-q)^L=p,
\]
independently over colours, so the final graph has exactly the law of \(G_p\).

Suppose that before a given round the current graph has \(c\) connected components. If \(C\) is one of these components, then every colour crossing the cut \(\delta_G(C)\) is still inactive. Indeed, if such a colour had already been activated, all its edges would be present, including an edge joining \(C\) to another current component.

There are at least \(k\) such crossing colours. Consequently, the probability that no colour crossing \(C\) is activated in the next round is at most
\[
a:=(1-q)^k.
\]

Let \(I\) be the number of old components receiving no newly activated crossing colour in this round. Then
\[
\mathbb E[I\mid\text{current graph}]\le ac.
\]

Contract the old components and consider the graph formed by newly activated edges. Every non-isolated component of this contracted graph contains at least two old components. Hence, if \(c'\) denotes the number of components after the round,
\[
c'\le I+\frac{c-I}{2}=\frac{c+I}{2}.
\]
Writing
\[
\beta=\frac{1+a}{2},
\]
we obtain, whenever \(c\ge2\),
\[
\begin{aligned}
\mathbb E[c'-1\mid\text{current graph}]
 &\le \frac{(1+a)c}{2}-1\\
 &=\beta c-1\\
 &\le \beta(c-1),
\end{aligned}
\]
because \(\beta\le1\). The same inequality is trivial when \(c=1\).

After \(L\) rounds,
\[
\mathbb E[c_L-1]\le (n-1)\beta^L,
\]
and therefore
\[
\Pr(G_p\text{ disconnected})
 \le (n-1)\beta^L.
\]

Now
\[
a=(1-q)^k=(1-p)^{k/L},
\]
so
\[
\beta^L
 =\left(\frac{1+(1-p)^{k/L}}2\right)^L.
\]
Letting \(L\to\infty\),
\[
\beta^L\longrightarrow (1-p)^{k/2}.
\]
The final law is the same for every \(L\), so taking the limit in the upper bound proves
\[
\Pr(G_p\text{ disconnected})\le(n-1)(1-p)^{k/2}.
\]
\(\square\)

Applying Lemma 2 with \(p=1/2\) separately to the red and blue marginal distributions and then using a union bound proves Theorem 1.

# 3. Consequence for robust expanders

Theorem 1 resolves Question 10.2 under the following natural quantitative meaning of robustness.

Assume there is an absolute constant \(\eta>0\) such that, writing \(d=\bar d(G)\), for every nonempty \(X\subseteq V(G)\) with \(|X|\le n/2\), deleting any set \(F\) of at most
\[
\eta d|X|
\]
edges still leaves an external neighbour of \(X\). The actual lower bound on \(|N_{G-F}(X)|\) may be sublinear; only its positivity is used.

Let \(r\) be the number of colours crossing \(\delta_G(X)\). Properness implies that every colour contributes at most \(|X|\) crossing edges. Hence
\[
|\delta_G(X)|\le r|X|.
\]
If \(r\le\eta d\), deleting \(F=\delta_G(X)\) would be permitted and would leave \(X\) with no external neighbour, a contradiction. Therefore
\[
\kappa_{\mathrm{col}}(G)>\eta d.
\]

It follows from Theorem 1 that the required decomposition exists whenever
\[
\eta d>2\log_2(2(n-1)).
\]
In particular, if logarithms in the question are natural, any
\[
d\ge C\log n
\]
with, for example,
\[
C=\frac{5}{\eta\ln 2}
\]
is sufficient.

The same conclusion holds for two other common formulations of robustness:

1. **Maximum-degree deletion:** if expansion survives every \(F\) with
   \(\Delta(F)\le\eta d\), take \(F\) to be the union of all crossing colour classes. Properness gives \(\Delta(F)\le r\).

2. **Colour deletion:** if expansion survives deletion of any \(\eta d\) colours, then a cut crossed by at most \(\eta d\) colours is immediately impossible.

Thus, if the source paper's definition of “robust sublinear expander” has any of these constant-fraction resilience properties, the argument above is a complete proof of Question 10.2.

# 4. Why the omitted quantitative definition matters

Ordinary sublinear expansion, or robustness only against an \(o(d)\)-fraction of incident edges, does not by itself force the conclusion.

Here is a basic obstruction. Let
\[
V=\mathbb F_2^r,\qquad
W=\{x\in\mathbb F_2^r:x_r=0\}.
\]
Choose a set
\[
A\subseteq W\setminus\{0\}
\]
containing \(e_1,\dots,e_{r-1}\), and add the generator \(e_r\). Form the Cayley graph
\[
G=\operatorname{Cay}\bigl(\mathbb F_2^r,A\cup\{e_r\}\bigr),
\]
colouring the edge \(\{x,x+a\}\) by \(a\).

Each colour class is a perfect matching, so the colouring is proper. All generators except \(e_r\) preserve the two cosets of \(W\), and therefore \(e_r\) is the unique colour crossing the cut
\[
W,\quad \mathbb F_2^r\setminus W.
\]
Every spanning connected colour-union must use colour \(e_r\). Hence two colour-disjoint spanning connected subgraphs cannot exist.

The degree can nevertheless be made at least \(C\log n\) for any prescribed constant \(C\), simply by choosing \(|A|\) appropriately; here \(n=2^r\).

Moreover, this graph satisfies a fairly strong weak-robustness condition. Since it contains the standard hypercube \(Q_r\), the cube edge-isoperimetric inequality gives
\[
|\delta_G(X)|\ge \min\{|X|,n-|X|\}.
\]
Consequently, for \(|X|\le 2n/3\),
\[
|\delta_G(X)|\ge |X|/2.
\]
If \(d=\Theta(\log n)\) and
\[
|F|\le \frac{d}{(\log n)^2}|X|,
\]
then for sufficiently large \(n\),
\[
e_{G-F}(X,V\setminus X)\ge |X|/4.
\]
Since \(G\) is \(d\)-regular,
\[
|N_{G-F}(X)|\ge \frac{|X|}{4d}
              \ge \frac{|X|}{(\log n)^2}
\]
for sufficiently large \(n\).

Thus, if “robust sublinear expander” were intended to mean only
\[
|F|\le \frac{d|X|}{(\log n)^2}
\quad\Longrightarrow\quad
|N_{G-F}(X)|\ge \frac{|X|}{(\log n)^2},
\]
the displayed Cayley graphs would be counterexamples to Question 10.2.

# 5. Precise status and gap

The mathematical core is therefore reduced to checking one point in the source paper's definition:

- If robustness permits deletion of \(\eta\bar d(G)|X|\) edges, or \(\eta\bar d(G)\) colours, for an absolute \(\eta>0\), then Question 10.2 is proved by Theorem 1.

- If the permitted deletion scale is only \(o(\bar d(G))|X|\), then that implication is false in general; the Cayley obstruction above already handles the log-squared version.

Because the quantitative definition was not included in the prompt, I cannot responsibly label the original source question fully proved or disproved. The random-activation theorem itself has no remaining gap.