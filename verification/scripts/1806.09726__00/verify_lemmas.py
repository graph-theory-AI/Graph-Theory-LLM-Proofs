#!/usr/bin/env python3
"""Computational verification for referee report 1806.09726__00.

Checks the writeup's claims about the online Ramsey game against a random
Painter (each queried edge independently red w.p. p, blue w.p. 1-p):

  Lemma 1: Builder finds a red K_4 in expected O(p^-2) queries.
           (round: 3L red neighbors of v, L = ceil(1/p); query all edges
            between the three parts A,B,C of size L; a red tripartite
            triangle + v gives a red K_4; success prob >= c_0 per round.)
  Lemma 2: for p <= 1/n, greedy builds a blue K_n in expected O(n^2) queries.
  Lower bound sanity: with p = n^-3, prob of any red edge among the first
           q = floor(n(n-1)/4) queries is <= qp = O(1/n).

Also re-derives the second-moment quantities of Lemma 1 exactly.
"""
import math
import random

random.seed(12345)


# ---------- exact second-moment quantities of Lemma 1 ----------

def second_moment_report():
    print("=== Lemma 1 second-moment quantities (exact) ===")
    print(f"{'p':>8} {'L':>6} {'Lp':>6} {'EX=L^3p^3':>10} {'3L^4p^5':>10} "
          f"{'PZ lower bd':>12}")
    for p in [0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.001]:
        L = math.ceil(1 / p)
        EX = L**3 * p**3
        cross = 3 * L**4 * p**5          # bound on covariance term
        # Paley-Zygmund / Cauchy-Schwarz: P(X>0) >= (EX)^2 / E[X^2]
        # E[X^2] <= (EX)^2 + EX + 3 L^4 p^5
        pz = EX**2 / (EX**2 + EX + cross)
        assert EX >= 1.0, (p, EX)
        assert L * p <= 1.5, (p, L * p)
        print(f"{p:>8} {L:>6} {L*p:>6.3f} {EX:>10.4f} {cross:>10.4f} "
              f"{pz:>12.4f}")
    print()


# ---------- simulate one round of the Lemma 1 strategy ----------

def lemma1_round(p):
    """Return (queries_used, success) for one round of the strategy."""
    L = math.ceil(1 / p)
    queries = 0
    red = 0
    # step 2: query v--fresh until 3L red neighbors
    while red < 3 * L:
        queries += 1
        if random.random() < p:
            red += 1
    # steps 3-4: parts A,B,C of size L; query all cross edges,
    # look for a red tripartite triangle
    AB = [[random.random() < p for _ in range(L)] for _ in range(L)]
    BC = [[random.random() < p for _ in range(L)] for _ in range(L)]
    CA = [[random.random() < p for _ in range(L)] for _ in range(L)]
    queries += 3 * L * L
    success = False
    for a in range(L):
        Bs = [b for b in range(L) if AB[a][b]]
        if not Bs:
            continue
        Cs = [c for c in range(L) if CA[c][a]]
        if not Cs:
            continue
        for b in Bs:
            for c in Cs:
                if BC[b][c]:
                    success = True
                    break
            if success:
                break
        if success:
            break
    return queries, success


def lemma1_report():
    print("=== Lemma 1 simulation: red K_4 via rounds ===")
    print(f"{'p':>6} {'trials':>7} {'P(round ok)':>12} {'E[q]/p^-2':>10} "
          f"{'E[queries to K4]/p^-2':>22}")
    for p, trials in [(0.5, 4000), (0.3, 4000), (0.2, 3000), (0.1, 2000),
                      (0.05, 800), (0.02, 300)]:
        succ = 0
        qtot = 0
        # per-round stats
        for _ in range(trials):
            q, s = lemma1_round(p)
            qtot += q
            succ += s
        p_ok = succ / trials
        eq = qtot / trials
        # full strategy: repeat rounds until success
        tot_trials = max(60, trials // 10)
        full = 0
        for _ in range(tot_trials):
            tq = 0
            while True:
                q, s = lemma1_round(p)
                tq += q
                if s:
                    break
            full += tq
        efull = full / tot_trials
        print(f"{p:>6} {trials:>7} {p_ok:>12.3f} {eq * p * p:>10.3f} "
              f"{efull * p * p:>22.3f}")
    print()


# ---------- Lemma 2: greedy blue clique ----------

def lemma2_trial(n, p):
    queries = 0
    size = 0
    while size < n:
        # test one fresh candidate against the current clique
        ok = True
        for _ in range(size):
            queries += 1
            if random.random() < p:
                ok = False
                break
        if ok:
            size += 1
    return queries


def lemma2_report():
    print("=== Lemma 2 simulation: greedy blue K_n, p = 1/n ===")
    print(f"{'n':>6} {'trials':>7} {'E[queries]':>12} {'/ C(n,2)':>9} "
          f"{'e bound':>8}")
    for n, trials in [(10, 3000), (20, 2000), (40, 1000), (80, 400),
                      (160, 100)]:
        p = 1.0 / n
        tot = sum(lemma2_trial(n, p) for _ in range(trials))
        e = tot / trials
        c2 = n * (n - 1) / 2
        print(f"{n:>6} {trials:>7} {e:>12.1f} {e / c2:>9.3f} "
              f"{math.e:>8.3f}")
    print()


# ---------- lower bound arithmetic ----------

def lower_bound_report():
    print("=== Lower bound arithmetic: p = n^-3, q = floor(n(n-1)/4) ===")
    print(f"{'n':>6} {'q':>10} {'q < C(n,2)':>11} {'qp':>12}")
    for n in [10, 30, 100, 1000]:
        p = n ** -3
        q = (n * (n - 1)) // 4
        c2 = n * (n - 1) // 2
        print(f"{n:>6} {q:>10} {str(q < c2):>11} {q * p:>12.5f}")
    print()
    # exponent bookkeeping for the contradiction claim
    print("Conjectured exponent (2/3)m at m=4:", 2 / 3 * 4, "= 8/3 =",
          8 / 3)
    print("Paper's Conjecture 9 corrections: c_4 (m=4 = 1 mod 3) = 2/3 ->",
          "2m/3 - c_4 =", 2 * 4 / 3 - 2 / 3)
    print("c_5 (m=5 = 2 mod 3) = (2*5+8)/(6*5-3) =", (2 * 5 + 8) / (6 * 5 - 3),
          "-> 2m/3 - c_5 =", 2 * 5 / 3 - 18 / 27)


if __name__ == "__main__":
    second_moment_report()
    lemma1_report()
    lemma2_report()
    lower_bound_report()
