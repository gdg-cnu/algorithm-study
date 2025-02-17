import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
  n = int(input())
  height=list(map(int,input().split()))

  height.sort()
  result=0
  for j in range(2,n):
    l=height[j]-height[j-2] 
    result=max(result,l)
  print(result)

    