# 소수개수 세기
n = int(input())
m = map(int, input().split())
count = 0

for j in m:
  for i in range(2, j+1):
    if j % i == 0:
      if j == i:
        count += 1
      
      break

print(count)
