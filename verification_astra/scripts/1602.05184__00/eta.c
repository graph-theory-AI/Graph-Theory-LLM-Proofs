/* Brute-force check of eta(G)=Sz(G)-W(G) over 2-connected graphs (graph6 on stdin).
   Reports every non-exceptional 2-connected graph with eta(G) < bound,
   where bound is given on the command line (default 2n), plus the minimum eta. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXN 16
static int n;
static unsigned adj[MAXN];
static int d[MAXN][MAXN];

static int decode(const char *s){
    int nn = s[0]-63;
    if(nn<0||nn>MAXN) return -1;
    n = nn;
    for(int i=0;i<n;i++) adj[i]=0;
    const char *p = s+1;
    int bit=0, byte=0, cur=0;
    for(int j=1;j<n;j++) for(int i=0;i<j;i++){
        if(bit==0){ cur = p[byte]-63; byte++; bit=6; }
        bit--;
        if((cur>>bit)&1){ adj[i]|=1u<<j; adj[j]|=1u<<i; }
    }
    return 0;
}

static void bfs(int s){
    for(int i=0;i<n;i++) d[s][i]=-1;
    int q[MAXN], h=0,t=0; q[t++]=s; d[s][s]=0;
    while(h<t){ int v=q[h++]; unsigned a=adj[v];
        while(a){ int u=__builtin_ctz(a); a&=a-1;
            if(d[s][u]<0){ d[s][u]=d[s][v]+1; q[t++]=u; } } }
}

int main(int argc,char**argv){
    long long boundmul = 2; long long boundadd = 0;
    if(argc>1) boundmul = atoll(argv[1]);
    if(argc>2) boundadd = atoll(argv[2]);
    char line[256];
    long long count=0, viol=0; long long minEta=-1; char minG[256]="";
    while(fgets(line,sizeof line,stdin)){
        int L=strlen(line); while(L&&(line[L-1]=='\n'||line[L-1]=='\r')) line[--L]=0;
        if(!L) continue;
        if(decode(line)<0){ fprintf(stderr,"bad line %s\n",line); return 1; }
        count++;
        long long m=0; for(int i=0;i<n;i++) m+=__builtin_popcount(adj[i]); m/=2;
        /* exceptional? */
        long long full=(long long)n*(n-1)/2;
        int exc=0;
        if(m==full) exc=1;                 /* K_n */
        else if(m==full-1) exc=1;          /* K_n - e = K_n^{n-2} */
        else {
            for(int v=0;v<n;v++) if(__builtin_popcount(adj[v])==2){
                /* G-v complete? */
                int ok=1;
                for(int i=0;i<n&&ok;i++){ if(i==v) continue;
                    for(int j=i+1;j<n;j++){ if(j==v) continue;
                        if(!((adj[i]>>j)&1)){ ok=0; break; } } }
                if(ok){ exc=1; break; } }
        }
        for(int i=0;i<n;i++) bfs(i);
        long long W=0; for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) W+=d[i][j];
        long long Sz=0;
        for(int u=0;u<n;u++){ unsigned a=adj[u]&~((1u<<(u+1))-1);
            while(a){ int v=__builtin_ctz(a); a&=a-1;
                int nu=0,nv=0;
                for(int w=0;w<n;w++){ if(d[w][u]<d[w][v]) nu++; else if(d[w][v]<d[w][u]) nv++; }
                Sz += (long long)nu*nv; } }
        long long eta = Sz-W;
        if(!exc){
            if(minEta<0||eta<minEta){ minEta=eta; strcpy(minG,line); }
            if(eta < boundmul*n+boundadd){ viol++; if(viol<=50) printf("VIOLATION n=%d eta=%lld graph6=%s\n",n,eta,line); }
        }
    }
    printf("n=%d graphs=%lld non-exceptional-min-eta=%lld (attained by %s) below-bound=%lld\n",
           n,count,minEta,minG,viol);
    return 0;
}
