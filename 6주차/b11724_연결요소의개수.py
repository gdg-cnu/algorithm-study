#11724_연결요소의 개수
#연결요소 - 노드끼리 연결되어 있는 묶음의 개수

import sys
sys.setrecursionlimit(5000)

input=sys.stdin.readline
n,m=map(int,input().split())

graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
cnt=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

#dfs
def dfs(idx):
    visited[idx]=1
    for next in range(1,n+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)
