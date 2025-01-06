# dp[1]=1
# dp[2]=2 : 1+1, 2
# dp[3]= 4 :1+1+1, 1+2*2, 3
# dp[4]= 7: 1+1+1+1, 1+2*3, 2+2, 1+3*2
# dp[5]= 13 : 1+1+1+1+1, 1+2*4, 2+2+1*3, 3+1+1*3, 3+2
#
# T=input
# for 1 to T:
#     n=input
#     dp=[0]*(n+1)
#     
#     for i = 1 to n:
#         dp[1],dp[2],dp[3]=1,2,4
#         dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
# print(dp[n])

T=int(input())
for _ in range(T):
    n=int(input())
    dp=[0]*(n+1)
    for i in range(1,n+1):
        if i==1:
            dp[i]=1
        elif i==2:
            dp[i]=2
        elif i==3:
            dp[i]=4
        else: 
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    
    print(dp[n])
