
from collections import deque
import sys


input = sys.stdin.readline

f, s, g, u, d = map(int,input().split())

def bfs():
    q=deque([s])
    count=[0 for _ in range(f+1)]
    count[s]=1
    
    while q:
        now = q.popleft()

        if now==g:
            return count[now]-1
        
        for i in (u,-d):
            next=now+i
            if 1<=next<=f and count[next]==0 :
                q.append(next)
                count[next]=count[now]+1
    
    return "use the stairs"

print(bfs())


