"""Exhaustive/near-exhaustive check of Lemma 4:
   alpha_w(Q) - W(A) >= 2^n - 2 rho(A)   for every NONEMPTY independent A in Q = prod K_{q_i}, q_i>=3.
Also checks Lemma 3 (compression: independence preserved, weight non-decreasing, rank non-increasing)."""
import sys, itertools, random
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1904.02595__00')
from sympy import Matrix
import networkx as nx

def zvec(x):
    v = [1]
    for a in x:
        v = [c*t for c in v for t in (1, a+1)]
    return v

def rho(A):
    if not A: return 0
    return Matrix([zvec(x) for x in A]).rank()

def indep(x, y):
    return any(x[i] == y[i] for i in range(len(x)))

def alpha_w(qs, s):
    Om = list(itertools.product(*[range(q) for q in qs]))
    G = nx.Graph()
    for x in Om:
        w = 1
        for i, a in enumerate(x): w *= s[i][a]
        G.add_node(x, weight=w)
    for x, y in itertools.combinations(Om, 2):
        if indep(x, y): G.add_edge(x, y)
    cl, wt = nx.max_weight_clique(G, weight='weight')
    return wt

def W(A, s):
    tot = 0
    for x in A:
        w = 1
        for i, a in enumerate(x): w *= s[i][a]
        tot += w
    return tot

def enum_indep(Om, cap=None):
    """all nonempty independent families, as sorted tuples"""
    out = []
    m = len(Om)
    def rec(start, cur):
        if cur:
            out.append(tuple(cur))
            if cap and len(out) > cap: raise StopIteration
        for i in range(start, m):
            x = Om[i]
            if all(indep(x, y) for y in cur):
                cur.append(x); rec(i+1, cur); cur.pop()
    try:
        rec(0, [])
    except StopIteration:
        pass
    return out

def compress(A, i, qs):
    """coordinate-i compression"""
    fibers = {}
    for x in A:
        key = x[:i] + x[i+1:]
        fibers.setdefault(key, []).append(x[i])
    out = []
    for key, labs in fibers.items():
        for k in range(len(labs)):
            out.append(key[:i] + (k,) + key[i:])
    return sorted(out)

def run(qs, s, cap=None, label=""):
    n = len(qs)
    Om = list(itertools.product(*[range(q) for q in qs]))
    aw = alpha_w(qs, s)
    fams = enum_indep(Om, cap)
    worst = None; viol = 0; c3 = 0
    for A in fams:
        r = rho(A)
        lhs = aw - W(A, s)
        rhs = 2**n - 2*r
        if lhs < rhs:
            viol += 1
            if viol <= 3: print("  LEMMA4 VIOLATION", A, "alpha_w", aw, "W", W(A,s), "rho", r)
        slack = lhs - rhs
        if worst is None or slack < worst[0]: worst = (slack, A, r)
        # Lemma 3 spot check
        for i in range(n):
            B = compress(A, i, qs)
            okind = all(indep(x,y) for x,y in itertools.combinations(B,2))
            if not okind or W(B,s) < W(A,s) or rho(B) > r:
                c3 += 1
                if c3 <= 3: print("  LEMMA3 VIOLATION", A, i, B, okind, W(B,s), W(A,s), rho(B), r)
    print(f"L4 {label} q={qs} s={s} alpha_w={aw} families={len(fams)} min slack={worst[0]} (at {worst[1]}, rho={worst[2]}) violations={viol}; L3 violations={c3}")

random.seed(7)
# n=1
for q in [3,4,5]:
    run((q,), [sorted([random.randint(1,4) for _ in range(q)], reverse=True)], label="n=1")
# n=2 exhaustive
for qs in [(3,3),(3,4),(4,4)]:
    for trial in range(3):
        s = [sorted([random.randint(1,4) for _ in range(q)], reverse=True) for q in qs]
        run(qs, s, label="n=2")
    run(qs, [[1]*q for q in qs], label="n=2 unit")
