#10451번번
import sys
sys.setrecursionlimit(10**6) #런타임에러 방지지
input = sys.stdin.readline

# DFS 함수 정의
def dfs(v):
    visited[v] = 1  # 방문 처리
    next_node = numbers[v]  # 다음 노드
    if not visited[next_node]:  # 미방문 노드라면
        dfs(next_node)


T = int(input())  
for _ in range(T):
    N = int(input())  
    numbers = [0] + list(map(int, input().split())) #인덱스 1부터 시작하기 때문에 [0]을 더해줌
    visited = [0] * (N + 1) 

    count = 0 
    for i in range(1, N + 1):
        if not visited[i]:  # 방문하지 않은 정점이면
            dfs(i)  # DFS 수행
            count += 1  

    print(count)

    
