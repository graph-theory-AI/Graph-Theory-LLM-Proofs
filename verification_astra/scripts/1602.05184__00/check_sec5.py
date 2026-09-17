"""Checks for Section 5 of the writeup: the cone identity (12), Lemma 5.2, Prop 5.3,
and the sharpness families of Section 7."""
import sys
from itertools import combinations
sys.path.insert(0, '.')
from check_lemmas import parse_g6, G, induced_counts, exceptional, is_2connected

def cone(n, adj):
    a2 = [set(s) for s in adj] + [set(range(n))]
    for v in range(n): a2[v].add(n)
    return n+1, a2

def is_Km_minus_e(m, adj):
    return sum(len(a) for a in adj)//2 == m*(m-1)//2 - 1

def is_clique_plus_pendant(m, adj):
    for v in range(m):
        if len(adj[v]) == 1:
            rest = [x for x in range(m) if x != v]
            if all(y in adj[x] for x, y in combinations(rest, 2)): return True
    return False

def connected(n, adj):
    seen = {0}; st = [0]
    while st:
        v = st.pop()
        for u in adj[v]:
            if u not in seen: seen.add(u); st.append(u)
    return len(seen) == n

fails = []
count = 0
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    m, adj = parse_g6(line)
    if not connected(m, adj): continue
    count += 1
    p3, p4, c4, nm = induced_counts(m, adj)
    F = 2*p3 + p4 + 4*c4
    nc, ac = cone(m, adj)
    gc = G(nc, ac)
    eta_cone = gc.eta()
    # (12) cone identity
    if eta_cone != F: fails.append(("cone_identity", line, eta_cone, F))
    complete = (nm == 0)
    if not complete:
        exc = is_Km_minus_e(m, adj) or is_clique_plus_pendant(m, adj)
        if exc:
            if F != 2*m-4: fails.append(("L5.2_exception_value", line, F, 2*m-4))
        else:
            if F < 3*m-7: fails.append(("L5.2_bound", line, F, 3*m-7))
        # Prop 5.3: cone is 2-connected, non-exceptional => eta >= 3n-10
        if is_2connected(nc, ac) and not exceptional(nc, ac):
            if eta_cone < 3*nc-10: fails.append(("P5.3", line, eta_cone, 3*nc-10))
print(f"connected graphs checked: {count}")
print("ALL PASSED" if not fails else f"FAILURES: {fails[:5]} ... total {len(fails)}")
