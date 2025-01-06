# 1:1 1
# 2:1 10
# 3:2 100,101
# 4:3 1000,1010,1001
# 5:5 10000, 10100,10010, 10001, 10101
# 6:8

# n=input
# dp=[0]*(n+1)

# for 1 to n:
#     if i == 1 or 2:
#         dp[i]=1
#     else:
#         dp[i]=dp[i-1]+dp[i-2]

n=int(input())
dp=[0]*(n+1)

for i in range(1,n+1):
    if (i==1) or (i==2):
        dp[i]=1
    else:
        dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
