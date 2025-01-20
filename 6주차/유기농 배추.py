#1012번
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs 정의
def dfs(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1] # x축 이동: 위, 아래, 왼, 오
    dy = [1, -1, 0, 0] # y축 이동

    # 네 방향 탐색
    for i in range(4):
        nx = x + dx[i] # 다음 x축 좌표
        ny = y + dy[i] # 다음 y축 좌표
        # 범위 안에 있고 1이면(=배추이면) 지나간것을 -1로 표시하고 주변 탐색
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx, ny)

t = int(input()) 
for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    graph = [[0 for _ in range(m)] for _ in range(n)] #배추밭 초기화

    # 배추 위치 표시
    for _ in range(k):
        X, Y = map(int, input().split()) 
        graph[Y][X] = 1 #2차원 리스트에서는 행열로 입력해야되기 때문에 바꿔야됨

    # 배추 그룹 수(=배추흰지렁이 개수) 세기
    count = 0
    for a in range(m):
        for b in range(n): 
            if graph[b][a] == 1:  # 아직 방문하지 않은 배추 발견
                dfs(a, b)         # 해당 배추 그룹을 DFS로 탐색
                count += 1        # 탐색이 끝나면 count
    print(count)