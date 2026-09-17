"""(a) brute-force Lemma 2.2, (b) the numeric inequality block (6.5),
(c) the doubly-stochastic alternating walk, (d) the cyclic-window counting,
(e) the Section-4 Cayley recipe on a toy scale."""
import itertools, math, random
import networkx as nx

# ---------- (a) Lemma 2.2 -----------------------------------------------------
# "If z1,z2,z3 are within distance r of z and pairwise at distance > r, then
#  some vertex of degree >= 3 lies within distance r of z."
print("=== Lemma 2.2 (integer-vertex version) ===")
rng = random.Random(5)
bad = 0; tested = 0; hits = 0
for trial in range(4000):
    nn = rng.randint(4, 11)
    G = nx.gnp_random_graph(nn, rng.uniform(0.15, 0.5), seed=rng.randrange(10**9))
    if not nx.is_connected(G):
        continue
    d = dict(nx.all_pairs_shortest_path_length(G))
    B = {v for v in G if G.degree(v) >= 3}
    for z in G:
        for r in range(1, 5):
            cand = [x for x in G if d[z][x] <= r]
            for zs in itertools.combinations(cand, 3):
                if all(d[a][b] > r for a, b in itertools.combinations(zs, 2)):
                    tested += 1
                    hits += 1
                    if not any(d[z][b] <= r for b in B):
                        bad += 1
print(f"hypothesis instances found: {hits}, violations of conclusion: {bad}")

# ---------- (b) inequality block (6.5) ---------------------------------------
print()
print("=== inequality block (6.5), evaluated at the extreme A+1 = g/10000 ===")
def check(g):
    A1 = g / 10000.0          # A+1 at its largest allowed value
    D_ = 10 * A1
    E_ = 30 * D_
    s = math.floor(g / 10)
    S_ = g
    M_ = 100 * g * g
    return {
        "s-3 > 2E":             (s - 3 > 2 * E_,          s - 3, 2 * E_),
        "S*s > 2+2E":           (S_ * s > 2 + 2 * E_,     S_ * s, 2 + 2 * E_),
        "S > s+1":              (S_ > s + 1,              S_, s + 1),
        "M/2-D > S*s+2+E":      (M_ / 2 - D_ > S_ * s + 2 + E_, M_ / 2 - D_, S_ * s + 2 + E_),
        "2s < g/2":             (2 * s < g / 2,           2 * s, g / 2),
        "g-s >= 2s":            (g - s >= 2 * s,          g - s, 2 * s),
        "S >= 1000 D":          (S_ >= 1000 * D_,         S_, 1000 * D_),
        "M > S*s+s+1":          (M_ > S_ * s + s + 1,     M_, S_ * s + s + 1),
        "S(s+1) > S*s+s+1":     (S_ * (s + 1) > S_ * s + s + 1, S_ * (s + 1), S_ * s + s + 1),
    }
for g in (10000, 100000):
    print(f"g={g}")
    for k, (ok, lhs, rhs) in check(g).items():
        print(f"   {k:22s} {'OK ' if ok else 'FAIL'}  {lhs:.6g} vs {rhs:.6g}")
# smallest g for which all hold
gmin = None
for g in range(10, 20000):
    if all(v[0] for v in check(g).values()):
        gmin = g; break
print("smallest g for which the whole block (6.5) holds:", gmin)

# ---------- (c)+(d) alternating walk is uniform, window counting -------------
print()
print("=== alternating non-backtracking walk: stationarity of the uniform measure ===")
from verify_construction import H, red, blue
V = list(H.nodes())
def colour(e):
    e = (min(e), max(e)); return 'R' if e in red else 'B'
dir_edges = [(u, v) for u in V for v in H[u]]
print("directed edges:", len(dir_edges), " |E_R|,|E_B| =", len(red), len(blue))
import collections
p = {e: 1.0 / len(dir_edges) for e in dir_edges}
for step in range(6):
    q = collections.defaultdict(float)
    for (u, v), m in p.items():
        c = colour((u, v))
        nxt = [(v, w) for w in H[v] if colour((v, w)) != c]
        for e2 in nxt:
            q[e2] += m / len(nxt)
    dev = max(abs(q[e] - 1.0 / len(dir_edges)) for e in dir_edges)
    outdeg = {len([w for w in H[v] if colour((v, w)) != colour((u, v))]) for (u, v) in dir_edges}
    p = dict(q)
    print(f"  step {step+1}: out-degree set {outdeg}, max deviation from uniform = {dev:.3e}")

print()
print("=== cyclic-window counting: each edge of a cycle lies in exactly s windows ===")
for L in (7, 12, 26):
    for s in (2, 3, 5):
        if s >= L: continue
        cnt = collections.Counter()
        for start in range(L):
            for j in range(s):
                cnt[(start + j) % L] += 1
        assert set(cnt.values()) == {s}, (L, s, cnt)
        print(f"  cycle length {L}, window {s}: every edge counted exactly {s} times  OK")

# ---------- (e) Section-4 Cayley recipe, toy scale ---------------------------
print()
print("=== Section 4 recipe: residually-finite separation of short reduced words ===")
def reduced_words(g):
    letters = ['a', 'A', 'b', 'B']
    inv = {'a': 'A', 'A': 'a', 'b': 'B', 'B': 'b'}
    out = []
    cur = ['']
    for L in range(1, g):
        nxt = []
        for w in cur:
            for x in letters:
                if w and inv[x] == w[-1]:
                    continue
                nxt.append(w + x)
        out.extend(nxt); cur = nxt
    return out

def perms_for_word(w):
    """Return permutations a_w, b_w on {0..k} realising 0 -> k along w."""
    k = len(w)
    pa, pb = {}, {}
    for i, x in enumerate(w, start=1):
        if x == 'a':
            tgt = pa
            if i - 1 in tgt and tgt[i - 1] != i: return None
            tgt[i - 1] = i
        elif x == 'A':
            tgt = pa
            if i in tgt and tgt[i] != i - 1: return None
            tgt[i] = i - 1
        elif x == 'b':
            tgt = pb
            if i - 1 in tgt and tgt[i - 1] != i: return None
            tgt[i - 1] = i
        else:
            tgt = pb
            if i in tgt and tgt[i] != i - 1: return None
            tgt[i] = i - 1
    for tgt in (pa, pb):
        if len(set(tgt.values())) != len(tgt): return None
        dom = [x for x in range(k + 1) if x not in tgt]
        rng_ = [x for x in range(k + 1) if x not in set(tgt.values())]
        for a, b in zip(sorted(dom), sorted(rng_)):
            tgt[a] = b
    return tuple(pa[i] for i in range(k + 1)), tuple(pb[i] for i in range(k + 1))

ok = True
for g in (4, 5, 6, 7):
    ws = reduced_words(g)
    fails = 0
    for w in ws:
        pr = perms_for_word(w)
        if pr is None:
            fails += 1; continue
        pa, pb = pr
        x = 0
        for ch in w:
            if ch == 'a': x = pa[x]
            elif ch == 'A': x = pa.index(x)
            elif ch == 'b': x = pb[x]
            else: x = pb.index(x)
        if x != len(w):
            fails += 1
    print(f"  g={g}: {len(ws)} nonempty reduced words of length < g, "
          f"words whose own coordinate fails to send 0 -> |w|: {fails}")
    ok &= (fails == 0)
print("Section-4 partial-permutation recipe works on every short reduced word:", ok)
