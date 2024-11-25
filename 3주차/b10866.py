from collections import deque
import sys

n=int(sys.stdin.readline())
d=deque()

for _ in range(n):
    input=sys.stdin.readline().rstrip()
    if input.startswith('push_back'):
        d.append(int(input.split()[1]))
    elif input.startswith('push_front'):
        d.insert(0,int(input.split()[1]))
    elif input=='pop_front':
        print(d.popleft() if d else -1)
    elif input=='pop_back':
        print(d.pop() if d else -1)
    elif input=='size':
        print(len(d))
    elif input=='empty':
        print(0 if d else 1)
    elif input=='front':
        print(d[0] if d else -1)
    elif input=='back':
        print(d[-1] if d else -1)