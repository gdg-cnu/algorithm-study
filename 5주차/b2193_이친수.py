#2193_이친수
def rec(x, memo):
    if memo[x]!=0:
        return memo[x]
    if x<=2:
        memo[x]=1
    else:
        memo[x]=rec(x-1,memo)+rec(x-2,memo)

    return memo[x]

n=int(input())
memo=[0]*(n+1)
print(rec(n,memo))
