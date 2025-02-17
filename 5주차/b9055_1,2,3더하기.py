def fib(n, memo={}):
    if n==0:
        memo[n]=0
    elif n<=2:
        memo[n]=n
    elif n==3:
        memo[n]=4
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)+fib(n-3,memo)
    return memo[n]

t=int(input())
for _ in range(t):
    n=int(input())
    print(fib(n,memo={}))
