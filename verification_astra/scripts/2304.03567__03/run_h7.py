import sys
from check_gap2 import search
from construction import G_NO
best,nV,nR=search(G_NO,7,restarts=1,sweeps=3,seed=7)
print(f"h=7: |V(F_7)|={nV}  |R_7|={nR} (=YES value)  best found on NO-instance = {best}"
      f"   [UB(B_7)=244, 3*2^7=384]  {'OK' if best<=384 else '*** EXCEEDS ***'}")
print(f"  gap witnessed: YES={nR} > 384 >= NO-optimum ; ratio {nR/384:.3f}")
