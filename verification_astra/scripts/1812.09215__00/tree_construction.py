"""Verify the writeup's rooted-tree construction (Section 3) by brute force.

For each (k,d) build the BFS-truncated complete (k-1)-ary tree of height d-1 on n
vertices, define phi_v(x) = x_v XOR (XOR of children), and check:
  - phi is a bijection of Q_n,
  - XOR_v phi_v(x) = x_1 (dictator on the root),
  - each phi_v depends on at most k inputs,
  - Lip(phi) == 2 (for n>=2),
  - Lip(phi^{-1}) == max depth + 1 <= d.
"""
import itertools, sys

def build_tree(n, k):
    """BFS order in complete (k-1)-ary tree; returns parent list (0-indexed, root=0)."""
    if n == 1:
        return [None]
    b = k - 1
    if b < 1:
        return None
    parent = [None] * n
    nxt = 1
    for v in range(n):
        for _ in range(b):
            if nxt >= n:
                break
            parent[nxt] = v
            nxt += 1
        if nxt >= n:
            break
    if nxt < n:
        return None
    return parent

def depth(parent, v):
    d = 0
    while parent[v] is not None:
        v = parent[v]; d += 1
    return d

def popcount(x):
    return bin(x).count('1')

def check(n, k):
    parent = build_tree(n, k)
    if parent is None:
        return None
    children = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)
    h = max(depth(parent, v) for v in range(n))
    # phi as a function on bitmasks: bit i  <-> coordinate i (0-indexed, root = 0)
    def phi(x):
        y = 0
        for v in range(n):
            bit = (x >> v) & 1
            for w in children[v]:
                bit ^= (x >> w) & 1
            y |= bit << v
        return y
    img = [phi(x) for x in range(1 << n)]
    bij = (len(set(img)) == (1 << n))
    dict_xor = all(popcount(img[x]) % 2 == (x & 1) for x in range(1 << n))
    # junta sizes
    juntas = []
    for a in range(n):
        dep = set()
        for i in range(n):
            if any(((img[x] >> a) & 1) != ((img[x ^ (1 << i)] >> a) & 1) for x in range(1 << n)):
                dep.add(i)
        juntas.append(len(dep))
    # forward Lipschitz
    Lf = max(popcount(img[x] ^ img[x ^ (1 << i)]) for x in range(1 << n) for i in range(n))
    # inverse Lipschitz
    inv = [0] * (1 << n)
    for x in range(1 << n):
        inv[img[x]] = x
    Lb = max(popcount(inv[y] ^ inv[y ^ (1 << a)]) for y in range(1 << n) for a in range(n))
    return dict(n=n, k=k, height=h, bijection=bij, dictator_xor=dict_xor,
                max_junta=max(juntas), Lip_fwd=Lf, Lip_inv=Lb)

def Nk(k, d):
    return sum((k - 1) ** r for r in range(d))

bad = []
rows = []
for n in range(1, 15):
    for k in range(2, 8):
        r = check(n, k)
        if r is None:
            continue
        d_pred = 1
        while Nk(k, d_pred) < n:
            d_pred += 1
        ok = (r['bijection'] and r['dictator_xor'] and r['max_junta'] <= k
              and (r['Lip_fwd'] == 2 or n == 1) and r['Lip_inv'] <= max(d_pred, 1))
        rows.append((n, k, d_pred, r['Lip_inv'], r['Lip_fwd'], r['max_junta'], ok))
        if not ok:
            bad.append((n, k, r, d_pred))

print(f"{'n':>3} {'k':>3} {'d_min(formula)':>15} {'Lip(phi^-1)':>12} {'Lip(phi)':>9} {'max junta':>10} ok")
for row in rows:
    print(f"{row[0]:>3} {row[1]:>3} {row[2]:>15} {row[3]:>12} {row[4]:>9} {row[5]:>10} {row[6]}")
print()
print("FAILURES:", bad if bad else "none")
