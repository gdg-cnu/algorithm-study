import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
n = int(sys.stdin.readline())  # 노드의 개수 입력

graph = [[] for i in range(n+1)]  # 그래프 초기화

# 트리 구성
for i in range(n-1):  # 간선의 개수는 (노드 개수 - 1)
    a, b = map(int, sys.stdin.readline().split())  # 간선 정보 입력
    graph[a].append(b)  # 양방향 간선 설정
    graph[b].append(a)

visited = [0] * (n+1)  # 부모 노드를 저장할 배열

def dfs(v):
    for i in graph[v]:  # 현재 노드 v에 연결된 노드 탐색
        if visited[i] == 0:  # 아직 부모가 설정되지 않은 노드라면
            visited[i] = v  # 현재 노드를 부모로 설정
            dfs(i)  # 재귀적으로 탐색

dfs(1)  # 루트 노드(1번)에서 탐색 시작

# 결과 출력
for x in range(2, n+1):  # 2번 노드부터 n번 노드까지 부모 노드 출력
    print(visited[x])