"""Sharpness families of Section 7 and the formula (17) eta(K_m^t)=2(m-1-t)(t-1)."""
import sys
sys.path.insert(0, '/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1602.05184__00')
from check_lemmas import G, is_2connected, exceptional

def Knt(n, t):
    adj = [set(range(n-1)) - {i} for i in range(n-1)] + [set(range(t))]
    for i in range(t): adj[i].add(n-1)
    return n, adj

def cone_path(n):
    """K_1 join P_{n-1}: apex n-1, path 0-1-...-n-2"""
    adj = [set() for _ in range(n)]
    for i in range(n-2):
        adj[i].add(i+1); adj[i+1].add(i)
    for i in range(n-1):
        adj[i].add(n-1); adj[n-1].add(i)
    return n, adj

def clique_plus_edge(n):
    """clique of order n-2 on 0..n-3 (p=0,q=1) plus x=n-2,y=n-1 with edges p-x, x-y, y-q"""
    adj = [set() for _ in range(n)]
    for i in range(n-2):
        for j in range(n-2):
            if i != j: adj[i].add(j)
    x, y = n-2, n-1
    adj[0].add(x); adj[x].add(0)
    adj[x].add(y); adj[y].add(x)
    adj[y].add(1); adj[1].add(y)
    return n, adj

print("m,t : eta(K_m^t) formula 2(m-1-t)(t-1)")
bad = 0
for m in range(4, 13):
    for t in range(1, m-1):
        n, adj = Knt(m, t)
        e = G(n, adj).eta(); f = 2*(m-1-t)*(t-1)
        if e != f: print("MISMATCH", m, t, e, f); bad += 1
print("K_m^t formula ok" if not bad else "K_m^t FORMULA FAILS")

for n in range(5, 16):
    nn, adj = cone_path(n)
    g = G(nn, adj)
    print(f"n={n} K_1 v P_(n-1): eta={g.eta()} 3n-10={3*n-10} 2conn={is_2connected(nn,adj)} exceptional={exceptional(nn,adj)}")
for n in range(5, 16):
    nn, adj = clique_plus_edge(n)
    g = G(nn, adj)
    print(f"n={n} clique+matched edge: eta={g.eta()} 2n={2*n} 2conn={is_2connected(nn,adj)} exceptional={exceptional(nn,adj)}")
