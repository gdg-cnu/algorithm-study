# 최대공약수, 최소공배수
# 1번
a,b=map(int,input().split())
list=[]
for i in range(1,min(a,b)+1):
    if a%i ==0 and b%i ==0:
        list.append(i)

print(max(list))
print(max(list)*(a//max(list))*(b//max(list)))

# 2번
import math
a,b=map(int,input().split())

print(math.gcd(a,b)) #최대공약수
print(math.lcm(a,b)) #최소공배수
