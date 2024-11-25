from collections import deque
import sys

n, k = map(int,sys.stdin.readline().split())

# 원형 큐 생성
d = deque(i for i in range(1,n+1))

res=[]
while len(d)!=0:
    # k번째 전 사람들은 뒤로 보냄
    for _ in range(0,k-1):
        d.append(d.popleft())
    # 맨 앞에 사람을 제거
    res.append(str(d.popleft()))

print('<'+', '.join(res)+'>')