#10451_순열사이클

import sys
sys.setrecursionlimit(5000)

def dfs(idx):
    visited[idx]=1
    next=graph[idx]
    if visited[next]==0:
        dfs(next)

input=sys.stdin.readline

t=int(input())
for _ in range(t):
    cnt=0
    n=int(input())
    graph=list(map(int,input().split()))
    visited=[0]*(n+1)
    graph.insert(0,0)
    for i in range(1,n+1):
        if visited[i]==0:
            dfs(i)
            cnt+=1
    print(cnt)