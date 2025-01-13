#11724번
# 계속 시간초과 뜸 
import sys
sys.setrecursionlimit(10**6) # 기본 재귀 호출 제한 -> 안 하면 런타임에러 뜸
input=sys.stdin.readline
N,M=map(int, input().rstrip().split())

# 인접 행렬 생성
graph = [[0] * (N + 1) for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1  # 양방향 간선 설정

# 방문 체크 리스트
visited = [0] * (N + 1)

# DFS 함수
def dfs(v):
    visited[v] = 1  # 방문 처리
    for i in range(1, N + 1):  # 모든 노드 탐색
        if graph[v][i] == 1 and not visited[i]:  # 간선 존재 & 미방문
            dfs(i)

# 연결 요소 개수 계산
count = 0
for i in range(1, N + 1):
    if not visited[i]:  # 미방문 노드 발견 시
        dfs(i)  # DFS 호출
        count += 1  # 연결 요소 증가

print(count)
