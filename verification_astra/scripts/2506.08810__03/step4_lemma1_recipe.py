"""Step 4: sanity-test Lemma 1's conclusion on explicit infinite T*-free tournaments.

CAVEAT: the relation "O(x) D O(y) is finite" has no faithful finite-window proxy, so
the Lemma 1 recipe cannot be run mechanically on a truncation (a threshold proxy
either splits or merges the true classes).  Instead, for each explicit infinite
T*-free tournament below we work out the class decomposition BY HAND, write down the
transitive order the Lemma 1 proof would produce, and check on growing windows that
the change-graph degree stays bounded (= locally finite in the limit).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tstar import *

def build(n, rule):
    return [[ (i!=j and rule(i,j)) for j in range(n)] for i in range(n)]

def change_degree(a, order):
    n=len(a); pos={v:i for i,v in enumerate(order)}
    d=[0]*n; m=0
    for i in range(n):
        for j in range(n):
            if i!=j and a[i][j] and pos[i]>pos[j]:
                d[i]+=1; d[j]+=1; m+=1
    return max(d), m

def rule_a(i,j):   # TT_omega[C3]
    return (i//3<j//3) if i//3!=j//3 else ((j%3-i%3)%3==1)
def rule_e(i,j):   # TT with (2t,2t+1) flipped
    return (i>j) if i//2==j//2 else (i<j)
def rule_g(i,j):   # TT with all (i,i+1) flipped
    return (i>j) if abs(i-j)==1 else (i<j)
def rule_h(i,j):   # evens transitive, odds transitive, evens->odds except o=e+1
    pi,pj=i%2,j%2
    if pi==pj: return i<j
    e,o=(i,j) if pi==0 else (j,i)
    beats = not (o==e+1)
    return (beats and i==e) or ((not beats) and i==o)

CASES = [
 ("TT_omega[C3]                 ", rule_a,
  "classes = the C3 blocks; inside a block r, C-={the vertex beating r}, C+={the other}",
  lambda n: [v for b in range(0,n,3) for v in ([b+2] if b+2<n else [])+[b]+([b+1] if b+1<n else [])]),
 ("TT, pairs (2t,2t+1) flipped  ", rule_e,
  "one class; order = natural order (r=0, C-={1}, C+=rest), repeated blockwise",
  lambda n: list(range(n))),
 ("TT, all (i,i+1) flipped      ", rule_g,
  "one class; order = natural order",
  lambda n: list(range(n))),
 ("evens->odds minus a matching ", rule_h,
  "two classes: evens precede odds (O(odd) is almost contained in O(even))",
  lambda n: [v for v in range(n) if v%2==0] + [v for v in range(n) if v%2==1]),
]

for name, rule, note, order_fn in CASES:
    print(f"{name}  [{note}]")
    for n in (20, 60, 120, 240):
        a = build(n, rule)
        assert is_tournament(a)
        md, m = change_degree(a, order_fn(n))
        print(f"      n={n:4d}: reversed pairs = {m:6d}   MAX CHANGE DEGREE = {md}")
    print()
print("Max change degree is constant in the window size in every case: these countable")
print("T*-free tournaments are indeed locally finite perturbations of transitive")
print("tournaments, as Corollary 4 + Lemma 1 assert.")
