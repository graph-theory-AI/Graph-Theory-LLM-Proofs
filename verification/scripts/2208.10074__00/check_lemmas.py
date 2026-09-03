"""Referee checks for attack 2208.10074__00.

Verifies computationally the three lemmas and the recursion of the writeup:
  Lemma 1: if G <= H x K_m (strong product) with td(H) <= t, colouring each
           vertex by the depth of its H-projection, every nonempty connected
           set of G has a colour occurring between 1 and m times.
  Lemma 2: edge perimeter in Z^2: p(A) >= 4*sqrt(|A|) for finite nonempty A.
  Lemma 3: fragmentation: sum_j p(A_j) <= p(A) + 4|R| for the components A_j
           of A - R, and M = max |A_j| >= (4(|A|-|R|)/(p(A)+4|R|))^2 when
           |A| > |R| (as used in the writeup's induction).
  Recursion: a_{i+1} = (2 a_i/(b_i+4C))^2 equals a_i^2/(4(1+C(i+1))^2) with
           b_i = 4+4Ci, and L_i = -log a_i satisfies L_i <= K_C 2^i.
"""
import itertools, math, random

random.seed(20260902)

# ---------------------------------------------------------------- Lemma 2 ---
def perimeter(A):
    """Edge perimeter of a set of Z^2 cells (edges to the complement in Z^2)."""
    A = set(A)
    p = 0
    for (x, y) in A:
        for nb in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if nb not in A:
                p += 1
    return p

def check_lemma2_exhaustive(w=4, h=4):
    cells = [(x, y) for x in range(w) for y in range(h)]
    worst = float("inf")
    bad = 0
    for mask in range(1, 1 << (w*h)):
        A = [cells[i] for i in range(w*h) if mask >> i & 1]
        p = perimeter(A)
        slack = p - 4*math.sqrt(len(A))
        worst = min(worst, slack)
        if slack < -1e-9:
            bad += 1
    print(f"Lemma 2: all {2**(w*h)-1} nonempty subsets of {w}x{h} box: "
          f"violations={bad}, min(p(A)-4*sqrt(|A|)) = {worst:.6f}")
    assert bad == 0

# ---------------------------------------------------------------- Lemma 3 ---
def components(A):
    A = set(A)
    seen, comps = set(), []
    for s in A:
        if s in seen:
            continue
        comp, stack = set(), [s]
        seen.add(s)
        while stack:
            (x, y) = stack.pop()
            comp.add((x, y))
            for nb in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if nb in A and nb not in seen:
                    seen.add(nb)
                    stack.append(nb)
        comps.append(comp)
    return comps

def random_connected_subset(w, h, target):
    """Random connected set of lattice cells inside a w x h box."""
    start = (random.randrange(w), random.randrange(h))
    A = {start}
    frontier = [start]
    while len(A) < target and frontier:
        (x, y) = random.choice(frontier)
        nbs = [(a, b) for (a, b) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
               if 0 <= a < w and 0 <= b < h and (a, b) not in A]
        if not nbs:
            frontier.remove((x, y))
            continue
        c = random.choice(nbs)
        A.add(c)
        frontier.append(c)
    return A

def check_lemma3_random(trials=3000):
    worst_perim_slack = float("inf")
    worst_M_slack = float("inf")
    for _ in range(trials):
        w = h = random.randrange(4, 11)
        A = random_connected_subset(w, h, random.randrange(2, w*h))
        R = set(random.sample(sorted(A), random.randrange(0, len(A))))
        comps = components(A - R)
        lhs = sum(perimeter(c) for c in comps)
        rhs = perimeter(A) + 4*len(R)
        worst_perim_slack = min(worst_perim_slack, rhs - lhs)
        assert lhs <= rhs, (A, R)
        if comps and len(A) > len(R):
            M = max(len(c) for c in comps)
            bound = (4*(len(A)-len(R)) / (perimeter(A)+4*len(R)))**2
            worst_M_slack = min(worst_M_slack, M - bound)
            assert M >= bound - 1e-9, (A, R)
    print(f"Lemma 3: {trials} random (A,R) pairs: perimeter inequality and "
          f"largest-component bound both hold "
          f"(min slacks {worst_perim_slack}, {worst_M_slack:.4f})")

# ---------------------------------------------------------------- Lemma 1 ---
def random_forest_closure(nv, t):
    """Random rooted forest of height <= t on nv vertices; return (depth, closure-adjacency)."""
    depth = {}
    parent = {}
    for v in range(nv):
        cands = [None] + [u for u in range(v) if depth[u] < t]
        p = random.choice(cands)
        parent[v] = p
        depth[v] = 1 if p is None else depth[p] + 1
    def ancestors(v):
        anc = set()
        u = parent[v]
        while u is not None:
            anc.add(u)
            u = parent[u]
        return anc
    adj = {v: set() for v in range(nv)}
    for v in range(nv):
        for u in ancestors(v):
            adj[v].add(u)
            adj[u].add(v)
    return depth, adj

def check_lemma1_random(trials=300):
    for _ in range(trials):
        t = random.randrange(1, 5)
        nv = random.randrange(2, 9)
        m = random.randrange(1, 4)
        depth, hadj = random_forest_closure(nv, t)
        # H = random subgraph of the closure (td(H) <= t witnessed by the forest)
        # G = random subgraph of H x K_m on a random subset of V(H) x [m]
        verts = [(v, i) for v in range(nv) for i in range(m)]
        gverts = random.sample(verts, random.randrange(1, len(verts)+1))
        gadj = {x: set() for x in gverts}
        for (a, b) in itertools.combinations(gverts, 2):
            va, vb = a[0], b[0]
            allowed = (va == vb) or (vb in hadj[va])
            if allowed and random.random() < 0.6:
                gadj[a].add(b)
                gadj[b].add(a)
        # colour = depth of projection; check every connected set X of G
        # (sampled) has its minimum colour occurring between 1 and m times.
        for _ in range(20):
            k = random.randrange(1, len(gverts)+1)
            seed = random.choice(gverts)
            X, stack = {seed}, [seed]
            while stack and len(X) < k:
                x = stack.pop()
                nbs = [y for y in gadj[x] if y not in X]
                random.shuffle(nbs)
                for y in nbs:
                    if len(X) < k:
                        X.add(y)
                        stack.append(y)
            # X is connected by construction
            mincol = min(depth[v] for (v, i) in X)
            cnt = sum(1 for (v, i) in X if depth[v] == mincol)
            projs = {v for (v, i) in X if depth[v] == mincol}
            assert 1 <= cnt <= m, (X, mincol, cnt, m)
            assert len(projs) == 1, (X, projs)  # all min-colour vertices in one fiber
    print(f"Lemma 1: {trials} random (H,K_m,G) instances x 20 connected sets: "
          f"minimum colour always occurs 1..m times, in a single H-fiber")

# -------------------------------------------------------------- recursion ---
def check_recursion():
    from fractions import Fraction
    for C in (Fraction(1, 2), Fraction(1), Fraction(3), Fraction(10)):
        # exact rational check of the closed form for a few steps
        b, a = Fraction(4), Fraction(1)
        for i in range(8):
            a_next = (2*a/(b + 4*C))**2
            closed = a*a / (4*(1 + C*(i+1))**2)
            assert a_next == closed, (C, i)
            b += 4*C
            a = a_next
        # log-domain recursion L_{i+1} = 2 L_i + log 4 + 2 log(1+C(i+1));
        # check sup_i L_i / 2^i is finite (it is a partial sum of a
        # convergent series sum_j 2^{-j-1}(log4 + 2 log(1+C(j+1)))).
        Cf = float(C)
        L = 0.0
        ratio_max = 0.0
        for i in range(60):
            L = 2*L + math.log(4) + 2*math.log(1 + Cf*(i+1))
            ratio_max = max(ratio_max, L / 2**(i+1))
        tail = sum(2**(-j-1)*(math.log(4) + 2*math.log(1 + Cf*(j+1)))
                   for j in range(2000))
        assert ratio_max <= tail + 1e-9
        print(f"recursion C={float(C)}: exact closed form matches; "
              f"sup L_i/2^i over i<=60 = {ratio_max:.4f} <= series bound "
              f"K_C = {tail:.4f}")

# ---- sanity: N large enough threshold and contradiction for a small t -------
def check_end_to_end(C=1.0, t=3):
    # compute a_i, b_i and the N threshold making the induction run t steps
    a = [1.0]; b = [4.0]
    for i in range(t):
        a.append((2*a[-1]/(b[-1] + 4*C))**2)
        b.append(b[-1] + 4*C)
    N_needed = max(2*C/a[i] for i in range(t))
    print(f"end-to-end (C={C}, t={t}): a_i = {[f'{x:.3e}' for x in a]}, "
          f"induction valid once N >= {N_needed:.1f}; a_t*N^2 > 0 gives the contradiction")

if __name__ == "__main__":
    check_lemma2_exhaustive()
    check_lemma3_random()
    check_lemma1_random()
    check_recursion()
    check_end_to_end()
    print("ALL CHECKS PASSED")
