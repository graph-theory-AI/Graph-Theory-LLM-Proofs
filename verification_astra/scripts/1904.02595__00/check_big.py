import sys
sys.path.insert(0,'/home/enatale/repos/lelarge/graph-theory-auto/verification_astra/scripts/1904.02595__00')
from core import build, IR, alpha
for factors in [[[2,1,1],[1,1,1],[1,1,1]], [[3,2,1],[1,1,1],[1,1]]]:
    verts,N,Nc=build(factors); n=len(verts)
    al,_=alpha(factors); ir,S=IR(Nc,n,verbose=True)
    print(factors,"|V|",n,"alpha",al,"IR",ir,"OK" if ir==al else "MISMATCH", flush=True)
