#DFS와 BFS
# N, M, V=input
# 초기값을 0으로하는 그래프의 인접행렬 g 선언
# 정점 a,b 입력 후 g의 해당 위치에 1 넣기기 (양방향주의)
# dfs와 bfs 그래프의 방문 여부를 담을 리스트 생성

# dfs(v) *스택,재귀 이용
# 방문처리 # 방문 후 정점 출력
# 방문기록에 없고, 인덱스에 값이 있다면 방문한다. 재귀 함수 활용용

# bfs(v) * 큐 사용
# deque를 이용하여 방문할 곳을 순서대로 넣을 큐 생성
# 방문 처리 후
# while문을 통해 q에 값이 없을 때까지 반복
# q 맨 앞에 있는 정점을 popleft하고 걔를 기준으로 방문할 수 있는 모든 정점 append
from collections import deque

N, M, v = map(int,input().split())
g = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int,input().split())
    g[a][b] = 1
    g[b][a] = 1

visited1=[False]*(N+1)
visited2=[False]*(N+1)

def dfs(v):
    visited1[v]=True
    print(v,end=" ")
    for i in range(1,N+1):
        if not visited1[i] and g[v][i]==1:
            dfs(i)

def bfs(v):
    q=deque([v])
    visited2[v]=True
    while q:
        v=q.popleft()
        print(v,end=" ")
        for i in range(1, N+1):
            if not visited2[i] and g[v][i]==1:
                q.append(i)
                visited2[i]=True

dfs(v)
print()
bfs(v)
