#1260번
N,M,V = map(int,input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    # 간선의 두 정점을 양방향 간선으로 설정정
    graph[a][b] = graph[b][a] = 1

#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#dfs 함수 만들기(stack)
def dfs(V):
    visited1[V] = 1 #방문처리
    print(V, end=' ')
    for i in range(1, N+1):
        # 만약 간선이 존재하고 방문하지 않은 점이 있다면 재귀호출출
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

#bfs 함수 만들기(queue)
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)