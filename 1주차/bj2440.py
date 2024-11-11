#2440
n=int(input())
# for i in range(n,0,-1):
#     print(i*"*")

#2441
# for i in range(n,0,-1):
#     print(" "*(n-i)+"*"*i)

#2442
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))