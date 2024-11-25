from collections import deque

def card(d):
    d.popleft()
    if d:
        d.append(d.popleft())

n = int(input())
d = deque(range(1,n+1))

while len(d)>1:
    card(d)

print(d[0])