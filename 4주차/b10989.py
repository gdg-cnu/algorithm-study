import sys

n=int(sys.stdin.readline())
arr=[0]*10001

# 계수정렬
for i in range(n):
    x=(int(sys.stdin.readline()))
    arr[x]+=1

for i in range(1,10001):
    if arr[i]!=0:
        for _ in range(arr[i]):
            print(i)