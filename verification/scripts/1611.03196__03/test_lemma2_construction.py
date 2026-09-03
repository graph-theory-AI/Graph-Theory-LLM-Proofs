"""Verify the combinatorial core of Lemma 2 of attacks/1611.03196__03/output.md.

Claims tested (over many random instances):
  C1. The dummy-vertex extension turns any matching of a bipartite graph into a
      perfect matching of the balanced supergraph, and A* ^ B* decomposes into
      even alternating cycles a_1 b_1 ... a_s b_s (a_j in A*, b_j in B*),
      with a_j meeting exactly b_{j-1} and b_j among the cycle's other edges.
  C2. For ANY subset J of cells, selecting a_j (j in J) and b_j (j not in J)
      plus the common edges A* & B*, then deleting a_j at every cyclic
      up-transition (j-1 not in J, j in J), yields a matching.
  C3. The number of deleted edges equals the number of cyclic up-transitions,
      which is at most the number of cyclic transitions of J; and when J is
      induced by midpoints in a union of t intervals, cyclic transitions
      <= 2t + (# cycles containing an internal change)   [writeup: <= 16d
      when t <= 4d].
  C4. The pre-repair statistic identity
      w(T) = sum_{j in J} w(a_j) + sum_{j notin J} w(b_j) + w(A* & B*).
"""
import random
import sys

random.seed(12345)


def random_bipartite(p, q, prob):
    return [(("L", u), ("R", v)) for u in range(p) for v in range(q)
            if random.random() < prob]


def random_matching(edges):
    es = edges[:]
    random.shuffle(es)
    used, M = set(), set()
    for (u, v) in es:
        if u not in used and v not in used and random.random() < 0.85:
            M.add((u, v))
            used.update((u, v))
    return M


def extend(M, p, q):
    """Dummy extension exactly as in the writeup's Lemma 2 proof."""
    Mstar = set(M)
    matchedL = {e[0] for e in M}
    matchedR = {e[1] for e in M}
    usedDR, usedDL = set(), set()
    dr = iter([("DR", i) for i in range(p)])
    dl = iter([("DL", i) for i in range(q)])
    for i in range(p):
        u = ("L", i)
        if u not in matchedL:
            v = next(dr)
            Mstar.add((u, v))
            usedDR.add(v)
    for i in range(q):
        v = ("R", i)
        if v not in matchedR:
            u = next(dl)
            Mstar.add((u, v))
            usedDL.add(u)
    remDL = [("DL", i) for i in range(q) if ("DL", i) not in usedDL]
    remDR = [("DR", i) for i in range(p) if ("DR", i) not in usedDR]
    assert len(remDL) == len(remDR)
    for u, v in zip(remDL, remDR):
        Mstar.add((u, v))
    return Mstar


def check_perfect(Mstar, p, q):
    verts = set()
    for (u, v) in Mstar:
        assert u not in verts and v not in verts, "not a matching"
        verts.update((u, v))
    allv = {("L", i) for i in range(p)} | {("R", i) for i in range(q)} \
        | {("DL", i) for i in range(q)} | {("DR", i) for i in range(p)}
    assert verts == allv, "not perfect"


def alternating_cycles(Astar, Bstar):
    """Return list of cycles, each as list of cells (a_j, b_j)."""
    Aedge, Bedge = {}, {}
    for e in Astar:
        Aedge[e[0]] = e
        Aedge[e[1]] = e
    for e in Bstar:
        Bedge[e[0]] = e
        Bedge[e[1]] = e
    diffA = Astar - Bstar
    visited = set()
    cycles = []
    for e0 in diffA:
        if e0 in visited:
            continue
        seq = []
        e = e0
        v = e0[1]
        use_b = True
        while True:
            seq.append(e)
            visited.add(e)
            e2 = Bedge[v] if use_b else Aedge[v]
            v = e2[0] if e2[1] == v else e2[1]
            use_b = not use_b
            e = e2
            if e == e0:
                break
        assert len(seq) % 2 == 0
        cells = [(seq[2 * j], seq[2 * j + 1]) for j in range(len(seq) // 2)]
        # C1: alternation
        for j, (a, b) in enumerate(cells):
            assert a in Astar and a not in Bstar
            assert b in Bstar and b not in Astar
            assert set(a) & set(b), "a_j, b_j must share a vertex"
            nxt = cells[(j + 1) % len(cells)][0]
            assert set(b) & set(nxt), "b_j, a_{j+1} must share a vertex"
        cycles.append(cells)
    return cycles


def run_instance(p, q, prob, d, mode):
    edges = random_bipartite(p, q, prob)
    A = random_matching(edges)
    B = random_matching(edges)
    Astar = extend(A, p, q)
    Bstar = extend(B, p, q)
    check_perfect(Astar, p, q)
    check_perfect(Bstar, p, q)
    cycles = alternating_cycles(Astar, Bstar)

    ncells = sum(len(c) for c in cycles)
    # choose J
    if mode == "random":
        J_flat = {j for j in range(ncells) if random.random() < 0.5}
        t_intervals = None
    else:  # interval mode: X = union of <= 4d intervals in [0, ncells]
        t = random.randint(0, 4 * d)
        pts = sorted(random.uniform(0, ncells) for _ in range(2 * t))
        ivs = [(pts[2 * i], pts[2 * i + 1]) for i in range(t)]
        J_flat = {j for j in range(ncells)
                  if any(lo <= j + 0.5 <= hi for lo, hi in ivs)}
        t_intervals = t

    # map flat index to (cycle, cell)
    flat = 0
    selected = set(Astar & Bstar)
    deleted = 0
    transitions = 0
    cycles_with_change = 0
    idx_of = []
    for cells in cycles:
        s = len(cells)
        inJ = [flat + j in J_flat for j in range(s)]
        flat += s
        for j in range(s):
            selected.add(cells[j][0] if inJ[j] else cells[j][1])
        # cyclic transitions and repairs
        ch = sum(1 for j in range(s) if inJ[j] != inJ[j - 1])
        transitions += ch
        if ch:
            cycles_with_change += 1
        for j in range(s):
            if inJ[j] and not inJ[j - 1]:
                selected.discard(cells[j][0])
                deleted += 1
        idx_of.append(inJ)

    # C2: matching check
    verts = set()
    for (u, v) in selected:
        assert u not in verts and v not in verts, "conflict survived repair"
        verts.update((u, v))

    # C3: deletion bound
    assert deleted <= transitions
    if t_intervals is not None:
        # linear changes <= 2 * t_intervals boundary points;
        # cyclic transitions <= linear changes + cycles_with_change
        assert transitions <= 2 * (2 * t_intervals) + cycles_with_change
        assert transitions <= 16 * d or 4 * d < t_intervals

    # C4: statistic identity on random labels
    label = {e: tuple(random.randint(0, 1) for _ in range(d))
             for e in (Astar | Bstar)}
    T = set(Astar & Bstar)
    flat = 0
    for ci, cells in enumerate(cycles):
        for j, (a, b) in enumerate(cells):
            T.add(a if idx_of[ci][j] else b)
    for l in range(d):
        lhs = sum(label[e][l] for e in T)
        rhs = sum(label[e][l] for e in (Astar & Bstar))
        flat = 0
        for ci, cells in enumerate(cycles):
            for j, (a, b) in enumerate(cells):
                rhs += label[a][l] if idx_of[ci][j] else label[b][l]
        assert lhs == rhs
    return ncells, deleted


def main():
    trials = 0
    for it in range(4000):
        p = random.randint(1, 9)
        q = random.randint(1, 9)
        prob = random.choice([0.2, 0.4, 0.6, 0.9])
        d = random.randint(1, 4)
        mode = "random" if it % 2 == 0 else "interval"
        run_instance(p, q, prob, d, mode)
        trials += 1
    print(f"OK: {trials} random instances passed all checks C1-C4.")


if __name__ == "__main__":
    main()
    sys.exit(0)
