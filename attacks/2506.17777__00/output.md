```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The problem remains open in general, but in dimension one it admits an exact word-theoretic characterization, yielding linear bounds and exact formulas whenever at most two parameters exceed one.",
  "would_publish": false,
  "caveats": "Novelty relative to the literature was not checked; the higher-dimensional problem and the resulting finite word parameter remain unresolved in general."
}
```

# 1. Statement and conventions

I use the source paper’s convention that an \(s\)-convex set is a union of at most \(s\) convex sets. In \(\mathbb R\), these are precisely unions of at most \(s\) intervals.

Write
\[
f_r(d;s_1,\ldots,s_r)
\]
for the number in the question. The partition parts are understood to be nonempty, as in the usual Tverberg convention. Allowing empty parts does not change the conclusions, since an empty part can be used to defeat the universal intersection property.

The general problem remains open. I prove the following one-dimensional result.

## Theorem 1: exact one-dimensional reduction

For \(\mathbf k=(k_1,\ldots,k_r)\in\mathbb N_0^r\), call a word \(u\) over the alphabet \([r]\) **\(\mathbf k\)-coverable** if it has a factorization into consecutive nonempty blocks
\[
u=B_1B_2\cdots B_t
\]
and labels \(\lambda_1,\ldots,\lambda_t\in[r]\) such that

1. the symbol \(\lambda_j\) does not occur in \(B_j\);
2. each \(i\in[r]\) is used as a label at most \(k_i\) times.

Let
\[
h_r(k_1,\ldots,k_r)
\]
be the minimum length of a word that is not \(\mathbf k\)-coverable. Then
\[
\boxed{
f_r(1;s_1,\ldots,s_r)
=
2r-2+h_r(s_1-1,\ldots,s_r-1).
}
\tag{1}
\]

In particular, this gives a finite exact algorithm for every fixed one-dimensional parameter vector.

Concrete consequences include:

\[
\boxed{f_2(1;s,t)=2\min\{s,t\}+1.}
\tag{2}
\]

Adding a parameter equal to \(1\) has an exact cost of two:
\[
\boxed{
f_{r+q}(1;s_1,\ldots,s_r,\underbrace{1,\ldots,1}_{q})
=
f_r(1;s_1,\ldots,s_r)+2q.
}
\tag{3}
\]

Thus, if all but two parameters are \(1\), then
\[
\boxed{
f_r(1;a,b,1,\ldots,1)
=
2\min\{a,b\}+2r-3.
}
\tag{4}
\]

If at most one parameter exceeds \(1\), then
\[
\boxed{f_r(1;s,1,\ldots,1)=2r-1.}
\tag{5}
\]

Finally, if all \(s_i=s\), then
\[
\boxed{
r(s+1)-1
\le f_r(1;s,\ldots,s)
\le
2r-1+r(r-1)(s-1).
}
\tag{6}
\]
In particular, for fixed \(r\),
\[
f_r(1;s,\ldots,s)=\Theta_r(s).
\]

This contrasts with the exponential dependence on \(s\) that occurs in sufficiently high dimension.

# 2. Proof of Theorem 1

Let
\[
x_1<x_2<\cdots <x_n
\]
be the points of \(P\subset\mathbb R\). A partition of \(P\) is represented by a word
\[
w=w_1w_2\cdots w_n,\qquad
w_j=i\Longleftrightarrow x_j\in P_i.
\]
Thus the one-dimensional problem depends only on the word.

For each color \(i\), let
\[
a_i=\min\{j:w_j=i\},\qquad
b_i=\max\{j:w_j=i\},
\]
and let
\[
H_i=[x_{a_i},x_{b_i}]=\operatorname{conv}(P_i).
\]
Put
\[
L=\max_i a_i,\qquad R=\min_i b_i.
\]
Then
\[
\bigcap_{i=1}^r H_i=
\begin{cases}
[x_L,x_R],&L\le R,\\
\varnothing,&L>R.
\end{cases}
\]

If \(L>R\), taking \(C_i=H_i\) already gives empty intersection. Hence every robust word must have \(L\le R\).

Define the **central word**
\[
u=w_Lw_{L+1}\cdots w_R.
\]

## Lemma 2

If the central word \(u\) is \((s_1-1,\ldots,s_r-1)\)-coverable, then the partition represented by \(w\) is not robust.

### Proof

Suppose
\[
u=B_1\cdots B_t
\]
is a legal factorization, with block \(B_j\) labelled \(\lambda_j\).

Consider a block \(B_j\) labelled \(i\). Since \(B_j\) contains no \(i\), and every point of the central interval lies between the first and last \(i\)-point, all positions of \(B_j\) lie strictly between two consecutive occurrences of \(i\). Let \(G_j\) be the corresponding open interval between those consecutive \(i\)-points. Thus \(G_j\) contains the points represented by \(B_j\) but contains no point of \(P_i\).

For each \(i\), remove from \(H_i\) all gaps \(G_j\) whose label is \(i\), and put
\[
C_i=H_i\setminus \bigcup_{\lambda_j=i}G_j.
\]
At most \(s_i-1\) gaps are removed, so \(C_i\) is a union of at most \(s_i\) intervals. Moreover, \(P_i\subseteq C_i\).

The selected gaps cover the entire central interval \([x_L,x_R]\). Indeed, they cover every central sample point. Between two consecutive sample points, either both belong to one block, in which case its gap covers the intervening interval, or a block boundary occurs, in which case the left gap covers up to the right sample point and the right gap covers that endpoint.

Since
\[
\bigcap_i H_i=[x_L,x_R]
\]
and the selected gaps cover this interval,
\[
\bigcap_{i=1}^r C_i=\varnothing.
\]
Thus the partition is not robust. ∎

## Lemma 3

If the central word \(u\) is not \((s_1-1,\ldots,s_r-1)\)-coverable, then the word obtained by padding \(u\) with \(r-1\) suitable symbols on each side is robust.

### Proof

Write \(u=u_1\cdots u_m\). Before \(u\), place one occurrence of every color except \(u_1\). After \(u\), place one occurrence of every color except \(u_m\). Let the resulting word be \(w\).

Then the latest first occurrence is exactly the first position of \(u\), and the earliest last occurrence is exactly the final position of \(u\). Hence the common intersection of the ordinary convex hulls is precisely the interval corresponding to \(u\).

Suppose, contrary to the assertion, that there are \(s_i\)-convex sets \(C_i\supseteq P_i\) with
\[
\bigcap_i C_i=\varnothing.
\]
Replace \(C_i\) by \(C_i\cap H_i\). This does not increase the number of interval components, still contains \(P_i\), and preserves empty intersection.

Since \(C_i\cap H_i\) is a union of at most \(s_i\) intervals and contains both endpoints of \(H_i\), the complement
\[
H_i\setminus C_i
\]
has at most \(s_i-1\) interval components. None of these complementary intervals contains an \(i\)-colored point.

These complementary intervals, over all \(i\), cover the central interval. Sweep from left to right through the points of \(u\): at the first uncovered sample point choose one complementary interval containing it, and form a block consisting of the maximal consecutive sample points lying in that interval. Once this interval is left, it can never be used again. Repeating this gives a factorization of \(u\) into blocks, each avoiding the color of its chosen complementary interval, with color \(i\) used at most \(s_i-1\) times.

This is a legal \((s_1-1,\ldots,s_r-1)\)-covering of \(u\), a contradiction. ∎

## Completion of the proof

Let \(w\) be any robust word. Its central word must be non-coverable by Lemma 2, so its length is at least
\[
h_r(s_1-1,\ldots,s_r-1).
\]

Moreover,
\[
L-1\ge r-1,
\]
because all \(r\) colors have appeared by position \(L\). Similarly,
\[
n-R\ge r-1,
\]
because from position \(R\) onward there must be a last occurrence of each color. Therefore
\[
n\ge 2r-2+h_r(s_1-1,\ldots,s_r-1).
\]

Conversely, take a shortest non-coverable word and pad it as in Lemma 3. The resulting robust word has exactly
\[
2r-2+h_r(s_1-1,\ldots,s_r-1)
\]
letters. This proves (1). ∎

# 3. Exact consequences

## 3.1 Two parts

Let \(r=2\), and put \(k_1=s-1\), \(k_2=t-1\).

A block avoiding symbol \(1\) consists entirely of \(2\)'s, and a block avoiding \(2\) consists entirely of \(1\)'s. Hence a binary word is \((k_1,k_2)\)-coverable exactly when

- it has at most \(k_1\) runs of \(2\)'s;
- it has at most \(k_2\) runs of \(1\)'s.

The shortest word with \(k_1+1\) runs of \(2\)'s has length \(2k_1+1\), and similarly for \(1\). Consequently,
\[
h_2(k_1,k_2)=2\min\{k_1,k_2\}+1.
\]
By (1),
\[
f_2(1;s,t)
=2+h_2(s-1,t-1)
=2\min\{s,t\}+1.
\]

Equivalently, in the original geometric language, two colored subsets of a line can be put into disjoint unions of \(s\) and \(t\) intervals exactly when their respective numbers of monochromatic runs do not exceed \(s\) and \(t\).

## 3.2 Deleting convex parameters

If \(k_{r+1}=0\), then
\[
h_{r+1}(k_1,\ldots,k_r,0)=h_r(k_1,\ldots,k_r).
\tag{7}
\]

One inequality follows because an old non-coverable word remains non-coverable: the new color has zero label capacity.

For the reverse inequality, take a word over the enlarged alphabet of length less than \(h_r\). Replace every occurrence of the new symbol by a fixed old symbol. The resulting old-alphabet word has a legal factorization. Restoring the new symbols cannot introduce a forbidden old label into any block, so the same factorization remains legal.

Combining (7) with (1) proves
\[
f_{r+1}(1;s_1,\ldots,s_r,1)
=f_r(1;s_1,\ldots,s_r)+2.
\]

Iterating gives (3). Together with the exact two-part formula, this proves (4) and (5).

# 4. The case \(s_i=2\) and permutation-complete words

Let \(\ell(r)\) be the minimum length of a word over \([r]\) containing every permutation of \([r]\) as a subsequence.

## Proposition 4

\[
h_r(1,\ldots,1)=\ell(r),
\]
and hence
\[
\boxed{
f_r(1;2,\ldots,2)=2r-2+\ell(r).
}
\tag{8}
\]

### Proof

Fix a permutation
\[
\pi=\pi_1\cdots\pi_r.
\]
A word fails to contain \(\pi\) as a subsequence if and only if it can be factored into \(r\) consecutive, possibly empty, blocks
\[
B_1\cdots B_r
\]
such that \(B_j\) avoids \(\pi_j\).

One direction follows greedily: take \(B_1\) to be the maximal initial block avoiding \(\pi_1\), then \(B_2\) maximal avoiding \(\pi_2\), and so on. If this process failed to cover the word after \(r\) blocks, the boundary occurrences would exhibit \(\pi\) as a subsequence.

Conversely, if such a factorization exists and \(\pi\) were a subsequence, the block indices containing the selected occurrences would form a nondecreasing sequence \(j_1,\ldots,j_r\) with \(j_t\ne t\) for every \(t\). No such sequence exists: it must cross the diagonal and hence have a fixed point.

Thus a word is coverable with each color used at most once exactly when it omits some permutation. It is non-coverable exactly when it contains every permutation. ∎

The first values are elementary:
\[
\ell(1)=1,\qquad \ell(2)=3,\qquad \ell(3)=7.
\]
For example,
\[
1213121
\]
contains all six permutations of \(\{1,2,3\}\).

To see that length six is impossible, if some symbol occurs only once, then there must be at least three symbols before it and three after it in order to realize both orders of the other two symbols on each side. Hence a length-six universal word would use every symbol exactly twice. Ordering the first occurrences as \(1,2,3\), the requirement that \(321\) occur forces the second \(2\) before the second \(1\), leaving no occurrence of \(2\) after an occurrence of \(3\) followed by \(1\); hence \(312\) is missing.

Consequently,
\[
f_3(1;2,2,2)=4+\ell(3)=11.
\]

I have not verified the literature concerning the exact determination of \(\ell(r)\) for larger \(r\), so I make no claim about its status.

# 5. Explicit one-dimensional estimates

Let
\[
A=\{i:s_i>1\},\qquad a=|A|,\qquad
K=\sum_{i\in A}(s_i-1).
\]

If \(a=0\), then \(h_r=1\). If \(a\ge1\), consider the periodic word on the active alphabet \(A\) of length
\[
(a-1)K+1.
\]
Every \(a\) consecutive letters contain all active symbols. Hence a block avoiding its label has length at most \(a-1\). A legal factorization has at most \(K\) blocks, so it can cover at most \((a-1)K\) letters. Therefore
\[
h_r(s_1-1,\ldots,s_r-1)\le (a-1)K+1.
\]
Using (1),
\[
\boxed{
f_r(1;s_1,\ldots,s_r)
\le
2r-1+(a-1)\sum_{i\in A}(s_i-1).
}
\tag{9}
\]

For the symmetric case this is
\[
f_r(1;s,\ldots,s)
\le 2r-1+r(r-1)(s-1).
\]

For a lower bound, a robust \(r\)-part partition must induce a robust two-part partition on every pair of colors: otherwise disjoint admissible containers for that pair already force the full intersection to be empty. Hence, by (2),
\[
|P_i|+|P_j|\ge 2\min\{s_i,s_j\}+1.
\tag{10}
\]

In the symmetric case, minimizing \(\sum_i|P_i|\) subject to
\[
|P_i|+|P_j|\ge2s+1
\]
gives
\[
\sum_i|P_i|\ge s+(r-1)(s+1)=r(s+1)-1.
\]
This proves (6).

More generally, if the \(a\) active parameters have minimum \(m\ge2\), then
\[
f_r(1;s_1,\ldots,s_r)
\ge 2(r-a)+a(m+1)-1.
\tag{11}
\]

# 6. Consequences in arbitrary dimension

A bad collinear configuration in \(\mathbb R\) remains bad when embedded in \(\mathbb R^d\): the interval containers used above are convex subsets of the containing line and hence convex subsets of \(\mathbb R^d\). Therefore
\[
f_r(d;s_1,\ldots,s_r)
\ge f_r(1;s_1,\ldots,s_r).
\tag{12}
\]

Also, since every convex set is \(s_i\)-convex,
\[
f_r(d;s_1,\ldots,s_r)
\ge f_r(d;1,\ldots,1)
=(r-1)(d+1)+1.
\tag{13}
\]

Thus
\[
\boxed{
f_r(d;s_1,\ldots,s_r)
\ge
\max\!\left\{
(r-1)(d+1)+1,\,
2r-2+h_r(s_1-1,\ldots,s_r-1)
\right\}.
}
\tag{14}
\]

A fully explicit symmetric consequence is
\[
\boxed{
f_r(d;s,\ldots,s)
\ge
\max\{(r-1)(d+1)+1,\ r(s+1)-1\}.
}
\tag{15}
\]

These estimates are not competitive with the supplied \(s^r\)-type lower bound in its high-dimensional range, but they apply in every dimension and are sharp in several one-dimensional regimes.

# 7. Exact finite computation of the one-dimensional number

The parameter \(h_r(\mathbf k)\) is recognized by a finite nondeterministic automaton.

A state is
\[
(\lambda,b_1,\ldots,b_r),
\]
where \(\lambda\) is the label of the current block and \(b_i\) is the number of \(i\)-labelled blocks started so far. On reading symbol \(a\), one may:

- continue the current block if \(\lambda\ne a\);
- start a new \(i\)-labelled block for any \(i\ne a\) with \(b_i<k_i\).

A word is coverable exactly when at least one state remains reachable. Determinizing and breadth-first searching until the reachable-state set becomes empty gives \(h_r\).

Here is a complete Python implementation.

```python
from collections import deque

def h_and_obstruction(k):
    """
    Input:
        k = tuple/list of nonnegative integers (k_1,...,k_r)
    Output:
        (h, word), where word is a shortest non-k-coverable word.
        Letters in word are returned as 1,...,r.
    """
    k = tuple(k)
    r = len(k)

    # A configuration is (current_label, used_tuple).
    # current_label = -1 only in the initial configuration.
    initial_config = (-1, (0,) * r)
    initial_set = frozenset([initial_config])

    def advance(reachable, letter):
        out = set()

        for label, used in reachable:
            # Continue the current block.
            if label != -1 and label != letter:
                out.add((label, used))

            # Start a new block labelled i.
            for i in range(r):
                if i == letter or used[i] >= k[i]:
                    continue
                new_used = list(used)
                new_used[i] += 1
                out.add((i, tuple(new_used)))

        return frozenset(out)

    queue = deque([(initial_set, ())])
    seen = {initial_set}

    while queue:
        reachable, word = queue.popleft()

        for a in range(r):
            nxt = advance(reachable, a)
            new_word = word + (a,)

            if not nxt:
                return len(new_word), tuple(x + 1 for x in new_word)

            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, new_word))


def f_line(s):
    h, obstruction = h_and_obstruction(
        tuple(x - 1 for x in s)
    )
    return 2 * len(s) - 2 + h, obstruction
```

The periodic-word argument above gives an a priori finite stopping bound.

# 8. Remaining gaps

1. Formula (1) is an exact characterization of the \(d=1\) problem, but it does not give a closed form for \(h_r(\mathbf k)\) in general.
2. Even the subcase \(s_i=2\) leads to the shortest-word parameter \(\ell(r)\); no general exact formula is proved here.
3. The construction is intrinsically one-dimensional. The order structure and the fact that complements inside a convex hull are intervals are both essential.
4. Apart from the collinear lower bounds (12)–(15), this argument does not improve the known general-dimensional upper or high-dimensional lower bounds supplied in the prompt.
5. I have not checked whether the one-dimensional characterization or some of its consequences already appear in the literature, so I do not claim novelty.