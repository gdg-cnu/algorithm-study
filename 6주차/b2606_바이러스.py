#2606_바이러스

import sys
sys.setrecursionlimit(5000)

def dfs(idx):
    global visited, graph
    visited[idx]=1
    for next in range(1,n+1):
        # 주어진 idx와 연결된 노드만 탐색
        if visited[next]==0 and graph[idx][next]==1:
            dfs(next)

input = sys.stdin.readline

n=int(input())
m=int(input())

graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)

cnt=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

dfs(1)

print(sum(visited)-1)