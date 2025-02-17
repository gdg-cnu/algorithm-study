t=int(input())

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    elif n<=2:
        return 1
    
    memo[n]=fib(n-2,memo)+fib(n-3,memo)
    return memo[n]


for _ in range(t):
    n=int(input())
    res=fib(n,memo={})
    print(res)