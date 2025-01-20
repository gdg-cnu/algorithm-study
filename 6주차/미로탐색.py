# 2178번 
# 1. dx,dy리스트 만들기
# 2. queue 생성하고 시작점 추가
# 3. queue에 넣은 값 빼기
# 4. 상하좌우 탐색 후 1일 경우 1씩 더해주기, 0이면 무시
# 5. 최단거리 값 출력

from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

#bfs 함수 정의의
def BFS(x, y):
    # 이동할 상, 하, 좌, 우 방향 정의
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 위치 벗어나면 안되므로 조건 추가
            if nx<0 or nx>=N or ny<0 or ny>=M or graph[nx][ny]==0:
                continue

            # 벽이 아니므로 이동 가능
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    # 마지막 값에서 카운트 값 뽑기, index는 0부터 시작하기 때문에 1빼기기
    return graph[N-1][M-1]

print(BFS(0,0))