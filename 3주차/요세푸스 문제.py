import sys
from collections import deque

n, k = map(int, input().split())

deq = deque(range(1, n+1)) 

res = []
while len(deq) != 0:
    for i in range(k-1):
        deq.append(deq.popleft())

    res.append(str(deq.popleft()))

print('<'+', '.join(res)+'>')

