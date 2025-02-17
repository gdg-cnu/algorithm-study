def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return n
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]

n=int(input())
res=fib(n,memo={})

print(res%10007)