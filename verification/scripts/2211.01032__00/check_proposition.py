"""Checks for the Proposition in Section 3 of attacks/2211.01032__00/output.md:
E[F(K_n)] >= log n - O(1) via good cyclic words.

1. Rotation lemma: for a uniform cyclic permutation of the m=n-1 neighbours of a
   vertex, the probability that t prescribed directed adjacencies with pairwise
   disjoint endpoints all hold is (m-1-t)!/(m-1)! = (n-t-2)!/(n-2)!.
   Verified by exhaustive enumeration of cyclic permutations.

2. For random good words (including repeated vertices), derive the per-vertex
   constraints rho_x(prev)=next, check the constraint endpoint-disjointness that
   goodness is claimed to guarantee, and verify the per-vertex satisfaction count
   equals (n-t_x-2)! by exhaustive enumeration at each vertex (n=8).

3. Monte Carlo on K_100: E[#good facial 5-cycles] vs bound (8):
   E C_5 >= (1/5)(1 - 2*5/n - 25/n^2). Also report mean total faces of K_n for
   n = 20, 50, 100 against ln n (Proposition claims E F >= ln n - O(1)).
"""
import itertools, math, random
random.seed(31415)

def cyclic_perms(elems):
    """All cyclic orders of elems as successor dicts."""
    e0, rest = elems[0], list(elems[1:])
    for perm in itertools.permutations(rest):
        order = [e0] + list(perm)
        yield {order[i]: order[(i + 1) % len(order)] for i in range(len(order))}

# ---------- 1. rotation lemma with generic disjoint pairs ----------
print("[1] Pr(t disjoint prescribed adjacencies) * (m-1)! == (m-1-t)! :")
for m, t in [(6, 1), (6, 2), (7, 3), (7, 2)]:
    elems = list(range(m))
    pairs = [(2 * i, 2 * i + 1) for i in range(t)]  # disjoint (a->b) constraints
    cnt = sum(all(s[a] == b for a, b in pairs) for s in cyclic_perms(elems))
    print(f"    m={m} t={t}: count={cnt}  (m-1-t)!={math.factorial(m-1-t)}")
    assert cnt == math.factorial(m - 1 - t)

# ---------- 2. per-vertex counts for actual good words (n=8) ----------
n = 8
V = list(range(n))

def is_good(w):
    k = len(w)
    darts = [(w[i], w[(i + 1) % k]) for i in range(k)]
    if any(a == b for a, b in darts):
        return False
    if len(set(darts)) != k:
        return False
    if any((b, a) in set(darts) for a, b in darts):
        return False
    return True

def constraints_of(w):
    """dict x -> list of (prev, next) pairs: rho_x(prev)=next."""
    k = len(w)
    cons = {}
    for i in range(k):
        x, a, b = w[(i + 1) % k], w[i], w[(i + 2) % k]
        cons.setdefault(x, []).append((a, b))
    return cons

tested = 0
trials = 0
while tested < 6 and trials < 100000:
    trials += 1
    k = random.choice([5, 6, 7])
    w = tuple(random.randrange(n) for _ in range(k))
    if not is_good(w):
        continue
    if len(set(w)) == len(w) and tested >= 3:
        continue  # after 3 words, insist on repeated-vertex words
    cons = constraints_of(w)
    ok_disjoint = all(len({y for pr in prs for y in pr}) == 2 * len(prs)
                      and all(x not in pr for pr in prs)
                      for x, prs in cons.items())
    per_vertex_ok = True
    for x, prs in cons.items():
        nbrs = [v for v in V if v != x]
        cnt = sum(all(s[a] == b for a, b in prs) for s in cyclic_perms(nbrs))
        expect = math.factorial(n - len(prs) - 2)
        if cnt != expect:
            per_vertex_ok = False
        tag = "OK" if cnt == expect else "MISMATCH"
        # printed compactly below
    print(f"[2] word {w} (k={k}, repeats={len(w)-len(set(w))}): "
          f"endpoint-disjointness={'OK' if ok_disjoint else 'FAIL'}, "
          f"per-vertex counts (n-t_x-2)! {'OK' if per_vertex_ok else 'MISMATCH'}")
    assert ok_disjoint and per_vertex_ok
    tested += 1

# ---------- 3. Monte Carlo on K_n ----------
def faces_random_Kn(n):
    """Random rotation system on K_n; returns list of face lengths and goodness."""
    nxt = {}
    for v in range(n):
        nb = [u for u in range(n) if u != v]
        random.shuffle(nb)
        for i, u in enumerate(nb):
            nxt[(v, u)] = (v, nb[(i + 1) % (n - 1)])
    seen = set()
    faces = []
    for v in range(n):
        for u in range(n):
            if u == v or (v, u) in seen:
                continue
            cyc = []
            cur = (v, u)
            while cur not in seen:
                seen.add(cur)
                cyc.append(cur)
                a, b = cur
                cur = nxt[(b, a)]
            faces.append(cyc)
    return faces

def good_face(cyc):
    darts = set(cyc)
    if len(darts) != len(cyc):
        return False
    return not any((b, a) in darts for a, b in cyc)

n, T = 100, 4000
c5 = tot = 0
for _ in range(T):
    fs = faces_random_Kn(n)
    tot += len(fs)
    c5 += sum(1 for f in fs if len(f) == 5 and good_face(f))
bound = (1 / 5) * (1 - 2 * 5 / n - 25 / n / n)
print(f"[3] K_{n}: MC E[#good facial 5-cycles]={c5/T:.4f} (T={T}) vs bound (8) {bound:.4f}; "
      f"heuristic n^5/(5(n-1)^5)={n**5/(5*(n-1)**5):.4f}")
for n in (20, 50, 100):
    T2 = 3000 if n <= 50 else 1500
    tot = 0
    for _ in range(T2):
        tot += len(faces_random_Kn(n))
    print(f"[3] E[F(K_{n})] MC = {tot/T2:.3f}   ln n = {math.log(n):.3f}   2 ln n = {2*math.log(n):.3f}")
