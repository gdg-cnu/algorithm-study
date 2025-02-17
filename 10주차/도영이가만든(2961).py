import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

result = 1e9

for i in range(1,n+1):
  cases = combinations(arr,i)
  for c in cases:
    S,B=1,0
    for s,b in c:
      S*=s
      B+=b

    result=min(result,abs(S-B))

print(result)