#24097번-조합

def C(n,m):
    ans=1
    for i in range(1,m+1):
        ans*=n
        ans//=i
        n-=1
    print(int(ans))
    return

n,m=map(int,input().split())
C(n,m)
