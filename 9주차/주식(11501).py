import sys
input = sys.stdin.readline

t= int(input())

for i in range(t):
  n = int(input())
  prices=list(map(int,input().split()))
  maxPrice=prices[n-1]
  profit=0
  for i in range(n-1,-1,-1): # 주가를 뒤에서 부터 탐색색 
    if maxPrice<=prices[i]: #현재값이 maxPrice 보다 크면  
      maxPrice=prices[i]    # max값 갱신신
    else:                   # 현재값이 maxPrice보다 작으면 
      profit+=maxPrice-prices[i] #이익을 낼 수 있으므로 차익을 더해줌줌
  
  print(profit)

