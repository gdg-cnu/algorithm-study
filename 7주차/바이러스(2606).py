#바이러스
# 그래프의 인접 행렬을 이용하여 입력 받은 쌍 1로 표시
#  dfs이용, 방문 리스트의 True의 개수를 통해 연결되어있는 노드의 수를 구함함
n=int(input()) #컴퓨터수
m=int(input()) #컴퓨터쌍의수


g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    g[a][b]=1
    g[b][a]=1

visited=[False]*(n+1)

def dfs(v):
    visited[v]=True
    for i in range(1,n+1):
        if not visited[i] and g[v][i]==1:
            dfs(i) 
dfs(1)
print(sum(visited)-1)
