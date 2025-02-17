#1260_DFS와 BFS
import sys

def dfs(idx):
    global visited
    visited[idx]=1
    print(idx, end=' ')
    for next in range(1,n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)
    
def bfs():
    global q, visited
    while q:
        cur =  q.pop(0)
        print(cur, end=' ')
        for next in range(1,n+1):
            if not visited[next] and graph[cur][next]:
                visited[next]=1
                q.append(next)
    
input=sys.stdin.readline
n,m,v=list(map(int,input().split()))

graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
visited=[0]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

dfs(v)
print()

visited=[0]*(n+1)
q=[v]
visited[v]=1
bfs()