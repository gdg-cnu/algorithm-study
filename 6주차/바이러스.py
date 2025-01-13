# 2606번
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())  # 컴퓨터 개수
v = int(input())  # 연결선 개수
graph = [[] for _ in range(n+1)]  # 인접 리스트 초기화
visited = [0] * (n+1)  # 방문 여부 체크

# 간선 정보 입력
for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 연결

# DFS 함수 정의
def dfs(v):
    visited[v] = 1
    for i in graph[v]:  # v와 연결된 모든 컴퓨터 탐색
        if visited[i] == 0:
            dfs(i)

# DFS 실행
dfs(1)
print(sum(visited) - 1)  # 1번 컴퓨터를 제외한 감염된 컴퓨터 수 출력
