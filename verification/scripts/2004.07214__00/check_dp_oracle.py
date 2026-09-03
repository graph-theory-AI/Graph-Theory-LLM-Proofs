"""Referee check for 2004.07214__00, Lemmas 2+3 (the extension oracle).

We implement the dynamic program EXACTLY as described in the writeup
(suffix signature sets U_i computed right to left; main states (s, u);
transitions as in steps 1-5), specialized to the 4-label minimal-dominating-set
problem of Lemma 3 (labels (delta, omega) in {0,1}^2, truncation d = 2,
local conditions (1), with inclusion set I forcing delta=1 and exclusion set O
forcing delta=0).

We compare its yes/no answer against a brute-force test of
"exists minimal dominating set D with I subseteq D subseteq V \\ O"
on many random graphs with random orders and random I, O.
"""

import itertools
import random

random.seed(98765)

LABELS = [(0, 0), (0, 1), (1, 0), (1, 1)]  # (delta, omega)
D_TRUNC = 2


def trunc(x):
    return min(D_TRUNC, x)


def brute_force_exists(n, adj, I, O):
    V = list(range(n))
    for bits in itertools.product([0, 1], repeat=n):
        D = {v for v in V if bits[v]}
        if not (I <= D and not (D & O)):
            continue
        # dominating?
        if any(not (({v} | adj[v]) & D) for v in V):
            continue
        # minimal? every d in D has a private neighbor (closed nbhd)
        ok = True
        for d in D:
            if not any(len((({p} | adj[p]) & D)) == 1 and d in ({p} | adj[p])
                       for p in ({d} | adj[d])):
                ok = False
                break
        if ok:
            return True
    return False


def allowed_labels(v, I, O):
    out = []
    for (de, om) in LABELS:
        if v in I and de != 1:
            continue
        if v in O and de != 0:
            continue
        out.append((de, om))
    return out


def dp_feasible(n, adj, order, I, O):
    """The writeup's DP. order is the vertex ordering v_1..v_n."""
    pos = {v: i for i, v in enumerate(order)}

    # ---- suffix signature sets U_i, i = n down to 0.
    # U[i] = set of q-tuples of signatures toward A_i of allowable labelings
    # of B_i. Signature representation: tuple over a in A_i (in order) of a
    # 4-tuple of truncated counts, one per label.
    U = [None] * (n + 1)
    U[n] = {tuple((0, 0, 0, 0) for _ in range(n))}
    for i in range(n - 1, -1, -1):
        v = order[i]  # v_{i+1} in 1-based writeup notation
        newset = set()
        for u in U[i + 1]:
            # u has domain A_{i+1} = order[:i+1]
            for lab in allowed_labels(v, I, O):
                li = LABELS.index(lab)
                sig = []
                for a_idx in range(i):  # domain A_i = order[:i]
                    a = order[a_idx]
                    counts = list(u[a_idx])
                    if a in adj[v]:
                        counts[li] = trunc(counts[li] + 1)
                    sig.append(tuple(counts))
                newset.add(tuple(sig))
        U[i] = newset

    # ---- main DP over states (s, u) at cut i.
    # s: signature of prefix labeling toward B_i: tuple over b in B_i
    #    (order[i:]) of 4-tuple truncated counts.
    # u: element of U[i].
    s0 = tuple((0, 0, 0, 0) for _ in range(n))  # domain B_0 = V
    states = {(s0, u) for u in U[0]}

    for i in range(n):
        v = order[i]
        newstates = set()
        for (s, u) in states:
            # s domain: order[i:], so coordinate of v is s[0]
            sv = s[0]
            for lab in allowed_labels(v, I, O):
                li = LABELS.index(lab)
                de, om = lab
                for u2 in U[i + 1]:
                    # step 1: signature toward A_i of suffix(u2) + v(lab)
                    sig = []
                    for a_idx in range(i):
                        a = order[a_idx]
                        counts = list(u2[a_idx])
                        if a in adj[v]:
                            counts[li] = trunc(counts[li] + 1)
                        sig.append(tuple(counts))
                    # step 2: must equal u
                    if tuple(sig) != u:
                        continue
                    # step 3: truncated label-neighbor counts of v
                    # neighbors in A_i from s (coordinate v), in B_{i+1} from
                    # u2 (coordinate of v = index i in domain A_{i+1})
                    u2v = u2[i]
                    cD = trunc(sv[2] + sv[3] + u2v[2] + u2v[3] + de)
                    cW = trunc(sv[1] + sv[3] + u2v[1] + u2v[3] + om)
                    # step 4: local predicate (1)
                    if cD < 1:
                        continue
                    if om == 1 and cD != 1:
                        continue
                    if de == 1 and cW < 1:
                        continue
                    # step 5: new prefix signature on B_{i+1} = order[i+1:]
                    news = []
                    for b_idx in range(i + 1, n):
                        b = order[b_idx]
                        counts = list(s[b_idx - i])
                        if b in adj[v]:
                            counts[li] = trunc(counts[li] + 1)
                        news.append(tuple(counts))
                    newstates.add((tuple(news), u2))
        states = newstates
    return len(states) > 0


def random_graph(n, p):
    adj = {v: set() for v in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def main():
    trials = 0
    mismatches = 0
    for n in range(1, 9):
        reps = {1: 10, 2: 20, 3: 40, 4: 80, 5: 120, 6: 120, 7: 60, 8: 30}[n]
        for _ in range(reps):
            p = random.random()
            adj = random_graph(n, p)
            order = list(range(n))
            random.shuffle(order)
            # random disjoint I, O
            I, O = set(), set()
            for v in range(n):
                r = random.random()
                if r < 0.25:
                    I.add(v)
                elif r < 0.5:
                    O.add(v)
            bf = brute_force_exists(n, adj, I, O)
            dp = dp_feasible(n, adj, order, I, O)
            trials += 1
            if bf != dp:
                mismatches += 1
                print("MISMATCH", n, sorted((a, sorted(adj[a]))
                                            for a in adj), order, I, O, bf, dp)
    print(f"extension oracle DP vs brute force: {trials} random instances "
          f"(n=1..8, random graphs, random orders, random I/O): "
          f"{mismatches} mismatches")


if __name__ == "__main__":
    main()
