import sys; sys.path.insert(0,'/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/2008.03587__00')
from zgame import zombie_number

def mk(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    return [sorted(a) for a in adj]

def cycle(n): return mk(n, [(i,(i+1)%n) for i in range(n)])
def path(n):  return mk(n, [(i,i+1) for i in range(n-1)])
def K(n):     return mk(n, [(i,j) for i in range(n) for j in range(i+1,n)])

print("z(K2) =", zombie_number(K(2)))
print("z(K3) =", zombie_number(K(3)))
for n in range(3,12):
    print(f"z(C_{n}) =", zombie_number(cycle(n)))
for n in range(2,8):
    print(f"z(P_{n}) =", zombie_number(path(n)))
# star / spider (trees) should be 1
print("z(star K1,5) =", zombie_number(mk(6,[(0,i) for i in range(1,6)])))
# Petersen graph: cop number 3 -> zombie number >= 3
pet = mk(10,[(0,1),(1,2),(2,3),(3,4),(4,0),(5,7),(7,9),(9,6),(6,8),(8,5),(0,5),(1,6),(2,7),(3,8),(4,9)])
print("z(Petersen) =", zombie_number(pet, kmax=4))
