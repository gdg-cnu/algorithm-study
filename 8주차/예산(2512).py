import sys

input=sys.stdin.readline

n=int(input())
lst=list(map(int,input().split())) # 예산 요청청
m=int(input())

start, end = 0, max(lst)
while start <= end: # 이분탐색
    if sum(lst) <= m:
        break
    mid = (start+end) // 2 # 상한액
    total=0
    for i in lst:
        if i >= mid: # 요청한 금액이 상한액보다 큰 경우우
            total += mid 
        else: # 요청한 금액이 상한액보다 작은 경우우
            total += i
    if total <= m: # 예산 총액이 총 예산 이하
        start = mid + 1
    else: # 예산 총액이 총 예산 초과과
        end = mid - 1

print(end)

                 



        
        
            


