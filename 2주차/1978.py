#1978번-소수찾기
n=int(input())
nums=list(map(int,input().split()))
k=0
for i in nums:
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
         k+=1
print(k)

