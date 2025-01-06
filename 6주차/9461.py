# for 1 to T:
#     N=input
#     PN=[0]*101
#     PN[1],PN[2],PN[3],PN[4],PN[5]=1,1,1,2,2

#     for i = 6 to N+1:
#         PN[i]=PN[i-1]+PN[i-5]
#     print(PN[N])

T=int(input())

for _ in range(T):
    N=int(input())
    PN=[0]*101
    PN[1],PN[2],PN[3]=1,1,1
    for i in range(4,N+1):
        PN[i]=PN[i-2]+PN[i-3]
    print(PN[N])