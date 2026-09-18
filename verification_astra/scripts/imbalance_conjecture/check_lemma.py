#!/usr/bin/env python3
"""
Referee check for attacks_opg/imbalance_conjecture.

Two things are tested on every graph whose edge imbalances are all positive:

  (A) THE CONJECTURE: M_G = multiset {|d(u)-d(v)| : uv in E} is graphic
      (Erdos-Gallai test).

  (B) THE WRITEUP'S "TRUNCATED-TAIL LEMMA" (eq. (1)):
        for every 1 <= k < D and every S subset E with |S|=k,
            sum_{e not in S} min(k, a_e) >= k(D-k).
      The minimum of the LHS over all S of size k is attained when S
      is the set of k edges with the largest a_e, so it suffices to
      test S = top-k.  (min(k,.) is monotone in a_e.)

Input: graph6 lines on stdin (from nauty's geng).
"""
import sys

def g6_edges(line):
    line = line.strip()
    if not line:
        return None
    b = line.encode()
    i = 0
    if b[0] == 126:  # '~' large n
        if b[1] == 126:
            n = ((b[2]-63) << 30) | ((b[3]-63) << 24) | ((b[4]-63) << 18) | \
                ((b[5]-63) << 12) | ((b[6]-63) << 6) | (b[7]-63)
            i = 8
        else:
            n = ((b[1]-63) << 12) | ((b[2]-63) << 6) | (b[3]-63)
            i = 4
    else:
        n = b[0]-63
        i = 1
    bits = []
    for c in b[i:]:
        v = c-63
        bits.extend((v >> j) & 1 for j in (5,4,3,2,1,0))
    edges = []
    p = 0
    for col in range(1, n):
        for row in range(col):
            if bits[p]:
                edges.append((row, col))
            p += 1
    return n, edges

def is_graphic(seq):
    """Erdos-Gallai."""
    d = sorted(seq, reverse=True)
    n = len(d)
    if n == 0:
        return True
    if any(x < 0 for x in d):
        return False
    if sum(d) % 2:
        return False
    if d[0] > n-1:
        return False
    for k in range(1, n+1):
        lhs = sum(d[:k])
        rhs = k*(k-1) + sum(min(k, x) for x in d[k:])
        if lhs > rhs:
            return False
    return True

def analyse(n, edges):
    deg = [0]*n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    imb = [abs(deg[u]-deg[v]) for u, v in edges]
    if any(a == 0 for a in imb):
        return None            # hypothesis fails
    if not edges:
        return None
    D = max(deg)
    a = sorted(imb, reverse=True)
    m = len(a)
    lemma_fail = []
    for k in range(1, D):     # 1 <= k < D
        tail = sum(min(k, x) for x in a[k:])
        if tail < k*(D-k):
            lemma_fail.append((k, tail, k*(D-k)))
    return dict(D=D, m=m, a=a, deg=deg, graphic=is_graphic(a),
                lemma_fail=lemma_fail)

def main():
    nA = nB = 0            # counts of hypothesis-satisfying graphs
    bad_conj, bad_lemma = [], []
    tight_lemma = 0
    total = 0
    for line in sys.stdin:
        r = g6_edges(line)
        if r is None:
            continue
        total += 1
        n, edges = r
        res = analyse(n, edges)
        if res is None:
            continue
        nA += 1
        if not res['graphic']:
            bad_conj.append((line.strip(), res))
            if len(bad_conj) > 5:
                break
        if res['lemma_fail']:
            bad_lemma.append((line.strip(), res))
            if len(bad_lemma) > 5:
                break
        else:
            D = res['D']
            if any(sum(min(k, x) for x in res['a'][k:]) == k*(D-k)
                   for k in range(1, D)):
                tight_lemma += 1
    print(f"graphs read              : {total}")
    print(f"satisfying imb(e)>0, m>0 : {nA}")
    print(f"M_G NOT graphic          : {len(bad_conj)}")
    for g, r in bad_conj[:5]:
        print("   COUNTEREXAMPLE TO CONJECTURE", g, r)
    print(f"lemma (1) violations     : {len(bad_lemma)}")
    for g, r in bad_lemma[:5]:
        print("   LEMMA FAILS", g, "deg=", r['deg'], "a=", r['a'],
              "fails at (k,tail,k(D-k))=", r['lemma_fail'])
    print(f"graphs where lemma tight : {tight_lemma}")

if __name__ == "__main__":
    main()
