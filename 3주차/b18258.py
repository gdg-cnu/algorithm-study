import sys
from collections import deque

queue=deque()

n=int(sys.stdin.readline())
for _ in range(n):
    q=sys.stdin.readline().rstrip()
    if q.startswith('push'):
        queue.append(int(q.split()[1]))
    elif q=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif q == 'empty':
        print(0 if queue else 1)
    elif q == 'size':
        print(len(queue))
    elif q == 'front':
        print(queue[0] if queue else -1)
    elif q == 'back':
        print(queue[-1] if queue else -1)