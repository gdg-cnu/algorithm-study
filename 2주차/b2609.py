a, b = map(int, input().split())
amax=[]
bmax=[]
maxNum=[]

for i in range(1,a+1):
    if a%i==0:
        amax.append(i)

for i in range(1,b+1):
    if b%i==0:
        bmax.append(i)

for i in amax:
    for j in bmax:
        if i==j:
            maxNum.append(i)

gcd=max(maxNum)
lcm=(a*b)//max(maxNum)

print(gcd)
print(lcm)


