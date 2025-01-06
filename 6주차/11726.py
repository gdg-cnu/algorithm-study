# n
# 1:1
# 2:2
# 3:3
# 4:5
# 5:8

# n= input
# count=[0]*1001
# count[1],count[2]=1,2
# for i= 3 to n:
#     count[i]=count[i-1]+count[i-2]
# print(count[n]%10007)   

n=int(input())
count=[0]*1001
count[1],count[2]=1,2
for i in range(3,n+1):
    count[i]=count[i-1]+count[i-2]
print(count[n]%10007)
    